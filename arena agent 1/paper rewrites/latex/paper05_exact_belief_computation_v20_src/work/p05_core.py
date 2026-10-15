"""Exact module for paper05 v20: blind survivable sets on the parameter cube.

Model (all arithmetic in integer tenths of stock above the floor):
  cells theta in {+1,-1}^m, actions U = {+1,-1}^m u {hold}, per-step drift
  D(u, theta) = -5 + 2 <u, theta> for sign actions and D = -5 for the hold
  (i.e. d = -1/2 + <u,theta>/5 in stock units); slack s = 10 (z - 1) >= 0.
A set S of cells is *blind-survivable from slack L* when one action sequence
(the same for every cell) keeps every cell of S at slack >= 0 for ever from
the common start L.  Everything here is exact (fractions / integers).
"""
from fractions import Fraction as Q
from itertools import product, combinations
from functools import lru_cache
import math

try:
    from exactlp import simplex_max
except ImportError:  # pragma: no cover
    from .exactlp import simplex_max

HOLD = None


# ---------------------------------------------------------------- basics
def cells(m):
    return [tuple(x) for x in product((1, -1), repeat=m)]


def sign_actions(m):
    return [tuple(x) for x in product((1, -1), repeat=m)]


def actions(m):
    return sign_actions(m) + [HOLD]


def ip(u, th):
    return sum(a * b for a, b in zip(u, th))


def ham(a, b):
    return sum(1 for x, y in zip(a, b) if x != y)


def D(u, th):
    """per-step drift in tenths"""
    if u is HOLD:
        return -5
    return -5 + 2 * ip(u, th)


def drift_by_distance(m, h):
    """drift (tenths) of a sign action at Hamming distance h from the cell"""
    return 2 * m - 5 - 4 * h


def rstar(m):
    """radius of the largest Hamming ball kept by a constant matched action"""
    return (2 * m - 5) // 4


def ball(center, r):
    m = len(center)
    return frozenset(th for th in cells(m) if ham(center, th) <= r)


# ---------------------------------------------------- the linear criterion
def game_value(S):
    """V(S) = max_{y in [-1,1]^m} min_{theta in S} <theta, y>, exactly, with a
    maximiser y and an optimal dual q (probability on S attaining
    min_q ||sum q_theta theta||_1 = V(S)).  S is blind-survivable from some
    finite slack iff V(S) >= 5/2 (Theorem: linear criterion)."""
    S = list(S)
    m = len(S[0])
    # variables w_1..w_m in [0,2] (y = w - 1), t' >= 0 (t = t' - m); maximise t'
    # constraints: t' - theta.w <= m - sum(theta);  w_i <= 2
    A, b = [], []
    for th in S:
        A.append([-x for x in th] + [1])
        b.append(m - sum(th))
    for i in range(m):
        A.append([1 if j == i else 0 for j in range(m)] + [0])
        b.append(2)
    c = [0] * m + [1]
    val, x, duals = simplex_max(c, A, b)
    V = val - m
    y = tuple(x[i] - 1 for i in range(m))
    q = duals[:len(S)]
    s = sum(q)
    q = tuple(qi / s for qi in q) if s else None
    # exact confirmation of both sides
    assert min(ip(th, y) for th in S) == V
    if q is not None:
        pooled = [sum(qi * th[i] for qi, th in zip(q, S)) for i in range(m)]
        assert sum(abs(p) for p in pooled) == V, "dual certificate must attain V"
    return V, y, dict(zip(S, q)) if q is not None else None


def survivable_some_level(S):
    return game_value(S)[0] >= Q(5, 2)


def horizon_bound(L, V):
    """if V(S) < 5/2, no blind sequence keeps all of S alive for more than
    floor(L / (5 - 2V)) steps from slack L (Corollary: finite-horizon bound)."""
    assert V < Q(5, 2)
    return math.floor(Q(L) / (5 - 2 * V))


def product_mixture(y):
    """the product measure on sign actions with mean y (p_i(+1) = (1+y_i)/2)"""
    m = len(y)
    p = {}
    for u in sign_actions(m):
        w = Q(1)
        for ui, yi in zip(u, y):
            w *= (1 + ui * yi) / 2
        if w:
            p[u] = w
    return p


def mixture_drifts(p, S):
    return {th: sum(w * D(u, th) for u, w in p.items()) for th in S}


def periodic_word(p):
    """a word realising the rational mixture p (common denominator)"""
    den = 1
    for w in p.values():
        den = den * w.denominator // math.gcd(den, w.denominator)
    word = []
    for u, w in sorted(p.items()):
        word += [u] * int(w * den)
    return word


def word_dip(word, S, L=0):
    """minimal slack reached by any cell of S along the periodic word from L
    (over one period; a word with nonnegative period totals attains its
    minimum in the first period)"""
    worst = 0
    for th in S:
        s = 0
        for u in word:
            s += D(u, th)
            worst = min(worst, s)
    return -worst


def interleave(word):
    """reorder a word to reduce the dip: greedy, choose next the action
    maximising the current minimum slack over cells (used only to exhibit
    witnesses; thresholds are computed exactly by the game)."""
    return word


# ----------------------------------------------- thresholds: the slack game
def minimal_winning_slacks(S, cap, acts=None):
    """Antichain of minimal winning slack vectors of the safety game on
    N^S (capped at `cap`): x is winning iff some blind sequence keeps every
    coordinate >= 0 for ever.  Greatest fixed point by iterating
    W_{k+1} = {x : exists u, x + D(u) >= 0 and x + D(u) in W_k} on up-sets,
    represented by their minimal elements.  Returns (antichain, k)."""
    S = list(S)
    m = len(S[0])
    acts = acts if acts is not None else actions(m)
    Dv = [tuple(D(u, th) for th in S) for u in acts]
    n = len(S)

    def minimal(vecs):
        vecs = sorted(set(vecs), key=lambda v: (sum(v), v))
        keep = []
        for v in vecs:
            if not any(all(w[i] <= v[i] for i in range(n)) for w in keep):
                keep.append(v)
        return keep

    cur = [tuple([0] * n)]
    k = 0
    while True:
        new = []
        for w in cur:
            for d in Dv:
                x = tuple(max(w[i] - d[i], 0) for i in range(n))
                if max(x) <= cap:
                    new.append(x)
        new = minimal(new)
        k += 1
        if new == cur:
            return cur, k
        cur = new
        if not cur:
            return cur, k


def threshold(S, cap=None):
    """L*(S): least common slack from which S is blind-survivable (None if
    S is not survivable within the cap; with cap >= an explicit winning
    level the answer is exact)."""
    S = list(S)
    if cap is None:
        V, y, q = game_value(S)
        if V < Q(5, 2):
            return None
        p = product_mixture(y)
        cap = word_dip(periodic_word(p), S) + 2 * max(abs(D(u, th)) for u in actions(len(S[0])) for th in S)
    ac, _ = minimal_winning_slacks(S, cap)
    if not ac:
        return None
    return min(max(w) for w in ac)


def first_step_bound(S):
    """every sequence loses max over cells of the first drop: L >= min_u max_theta (-D)^+"""
    m = len(next(iter(S)))
    return min(max(max(-D(u, th), 0) for th in S) for u in actions(m))


# ------------------------------------------------------------ feedback game
def classes(S, u):
    out = {}
    for th in S:
        out.setdefault(D(u, th), []).append(th)
    return out


def feedback_threshold(S, blind_thr, max_L=60):
    """least L from which S is survivable when the stock is observed
    (the common slack of an information class reveals the inner products):
    F(S, L) = [L >= L*_blind(S)] or exists a splitting u with every class
    c surviving from L + D_c.  blind_thr: callable S -> L* or None."""
    S = frozenset(S)
    m = len(next(iter(S)))
    memo = {}

    def F(T, L):
        key = (T, L)
        if key in memo:
            return memo[key]
        if L < 0:
            memo[key] = False
            return False
        b = blind_thr(T)
        if b is not None and L >= b:
            memo[key] = True
            return True
        ok = False
        for u in actions(m):
            cl = classes(T, u)
            if len(cl) <= 1:
                continue
            if all(L + d >= 0 and F(frozenset(c), L + d) for d, c in cl.items()):
                ok = True
                break
        memo[key] = ok
        return ok

    for L in range(0, max_L + 1):
        if F(S, L):
            return L
    return None


# ------------------------------------------------------------- cliques
def maximal_cliques(V, adj):
    """Bron-Kerbosch with pivoting; adj: dict vertex -> set"""
    out = []

    def bk(R, P, X):
        if not P and not X:
            out.append(frozenset(R))
            return
        piv = max(P | X, key=lambda v: len(adj[v] & P))
        for v in list(P - adj[piv]):
            bk(R | {v}, P & adj[v], X & adj[v])
            P = P - {v}
            X = X | {v}

    bk(set(), set(V), set())
    return out


def distance_graph(m, dmax):
    V = cells(m)
    adj = {v: set() for v in V}
    for a, b in combinations(V, 2):
        if ham(a, b) <= dmax:
            adj[a].add(b)
            adj[b].add(a)
    return V, adj


def kleitman_bound(m, d):
    """Kleitman (1966): a set of diameter <= d in {0,1}^m has at most
    sum_{i<=r} C(m,i) elements if d = 2r, and 2 sum_{i<=r} C(m-1,i) if d = 2r+1."""
    r = d // 2
    if d % 2 == 0:
        return sum(math.comb(m, i) for i in range(r + 1))
    return 2 * sum(math.comb(m - 1, i) for i in range(r + 1))


# ------------------------------------------------- symmetry (hyperoctahedral)
def canonical(S):
    """canonical form of a set of cells under coordinate permutations and
    sign flips (pure python; fine for m <= 5 and for a few sets at m = 6)"""
    S = list(S)
    m = len(S[0])
    best = None
    from itertools import permutations
    for perm in permutations(range(m)):
        for flips in product((1, -1), repeat=m):
            img = tuple(sorted(tuple(th[perm[i]] * flips[i] for i in range(m)) for th in S))
            if best is None or img < best:
                best = img
    return best


def orbit_size(S):
    """|G| / |Stab(S)| by counting stabilising group elements"""
    S = frozenset(S)
    m = len(next(iter(S)))
    from itertools import permutations
    stab = 0
    for perm in permutations(range(m)):
        for flips in product((1, -1), repeat=m):
            img = frozenset(tuple(th[perm[i]] * flips[i] for i in range(m)) for th in S)
            if img == S:
                stab += 1
    return (math.factorial(m) * 2 ** m) // stab


# -------------------------------------------- maximal survivable subsets
def maximal_survivable_in(C, lp_cache=None):
    """all inclusion-maximal survivable-from-some-level subsets of the clique
    C, by branching on the support of the infeasibility certificate."""
    lp_cache = {} if lp_cache is None else lp_cache
    found = set()
    seen = set()

    def rec(T):
        if T in seen:
            return
        seen.add(T)
        if T not in lp_cache:
            lp_cache[T] = game_value(T)
        V, y, q = lp_cache[T]
        if V >= Q(5, 2):
            found.add(T)
            return
        supp = [th for th, w in q.items() if w > 0]
        for th in supp:
            rec(T - {th})

    rec(frozenset(C))
    return {T for T in found if not any(T < U for U in found)}


def globally_maximal(T, dmax, lp_cache=None):
    lp_cache = {} if lp_cache is None else lp_cache
    m = len(next(iter(T)))
    for th in cells(m):
        if th in T:
            continue
        if all(ham(th, x) <= dmax for x in T):
            U = T | {th}
            if U not in lp_cache:
                lp_cache[U] = game_value(U)
            if lp_cache[U][0] >= Q(5, 2):
                return False
    return True


def pair_bound_distance(m):
    """pairs are survivable from some level iff h <= m - 5/2"""
    return math.floor(m - Q(5, 2))


# ------------------------------------------------------- alpha-set masks
def alpha_masks(m, k, L, use_numpy=True):
    """number of distinct k-step outcome vectors (which cells survive k
    steps from slack L) over all |U|^k action words"""
    C = cells(m)
    U = actions(m)
    Dm = [[D(u, th) for th in C] for u in U]
    if use_numpy:
        try:
            import numpy as np
        except ImportError:
            use_numpy = False
    if use_numpy:
        d = np.asarray(Dm, dtype=np.int16)
        nU = len(U)
        seq = np.indices((nU,) * k, dtype=np.uint8).reshape(k, -1)
        stock = np.full((seq.shape[1], len(C)), L, dtype=np.int16)
        alive = np.ones_like(stock, dtype=bool)
        for t in range(k):
            stock += d[seq[t]]
            alive &= stock >= 0
        packed = np.packbits(alive, axis=1)
        return len(np.unique(packed, axis=0))
    masks = set()
    for word in product(range(len(U)), repeat=k):
        s = [L] * len(C)
        alive = [True] * len(C)
        for a in word:
            for i in range(len(C)):
                s[i] += Dm[a][i]
                if s[i] < 0:
                    alive[i] = False
        masks.add(tuple(alive))
    return len(masks)


def survives(word, th, L, steps=None):
    """exact simulation of a (periodic) word from slack L for `steps` steps"""
    steps = steps if steps is not None else len(word)
    s = L
    for t in range(steps):
        s += D(word[t % len(word)], th)
        if s < 0:
            return False
    return True


def value_at_belief(b, k, L, m):
    """V_k(b) at a rational belief b on the cells: max over k-words of the
    mass of cells surviving k steps (definition-level) -- exact"""
    C = cells(m)
    U = actions(m)
    best = Q(0)
    for word in product(U, repeat=k):
        mass = sum(b[i] for i, th in enumerate(C) if survives(word, th, L, k))
        best = max(best, mass)
    return best


# ------------------------------------------- forward reachability (exact)
def forward_horizon(S, L, max_steps=200, acts=None, keep=None):
    """exact maximal survival horizon of S from common slack L: the number
    of steps some blind word keeps every cell alive.  Forward reachability
    with dominance pruning (only maximal reachable slack vectors are kept,
    which is sound because the winning region is an up-set).  Returns
    (steps, final_frontier_size) with steps = max_steps if no death is forced
    within the budget (then the horizon is >= max_steps)."""
    S = list(S)
    m = len(S[0])
    acts = acts if acts is not None else actions(m)
    Dv = [tuple(D(u, th) for th in S) for u in acts]
    n = len(S)

    def maximal(vecs):
        vecs = sorted(set(vecs), key=lambda v: (-sum(v), v))
        out = []
        for v in vecs:
            if not any(all(w[i] >= v[i] for i in range(n)) for w in out):
                out.append(v)
        return out

    R = [tuple([L] * n)]
    for t in range(1, max_steps + 1):
        nxt = []
        for s in R:
            for d in Dv:
                x = tuple(s[i] + d[i] for i in range(n))
                if min(x) >= 0:
                    nxt.append(x)
        R = maximal(nxt)
        if keep is not None:
            R = [tuple(min(x, keep) for x in v) for v in R]
            R = maximal(R)
        if not R:
            return t - 1, 0
    return max_steps, len(R)


def minimal_winning_saturated(S, cap, acts=None):
    """greatest fixed point of the *saturated* slack game (stocks are clipped
    at `cap`; a weaker player, hence sound): antichain of minimal winning
    vectors in [0,cap]^S."""
    S = list(S)
    m = len(S[0])
    acts = acts if acts is not None else actions(m)
    Dv = [tuple(D(u, th) for th in S) for u in acts]
    n = len(S)

    def minimal(vecs):
        vecs = sorted(set(vecs), key=lambda v: (sum(v), v))
        keep = []
        for v in vecs:
            if not any(all(w[i] <= v[i] for i in range(n)) for w in keep):
                keep.append(v)
        return keep

    # up-set W (within the box) represented by minimal elements; predecessor:
    # x in W' iff exists u: clip(x + D(u)) in W  <=>  x >= w - D(u) for some w
    # in Min W, componentwise, with the clip: coordinates where w_i - D_i(u) >
    # cap are unreachable, so such (w,u) give no predecessor; coordinates
    # where w_i <= clip are fine since clip(x_i + D_i) >= w_i iff x_i + D_i >= w_i
    # (as w_i <= cap).
    cur = [tuple([0] * n)]
    k = 0
    while True:
        new = []
        for w in cur:
            for d in Dv:
                x = tuple(max(w[i] - d[i], 0) for i in range(n))
                if max(x) <= cap:
                    new.append(x)
        new = minimal(new)
        k += 1
        if new == cur or not new:
            return new, k
        cur = new


def certified_threshold(S, caps=(6, 12, 24, 48), max_steps=400):
    """L*(S) with a two-sided certificate: upper bound from the saturated
    game (winning from L), lower bound from exact forward reachability
    (forced death from L-1 within `max_steps`).  Returns dict."""
    S = list(S)
    best = None
    for cap in caps:
        ac, k = minimal_winning_slacks(S, cap)
        if ac:
            L = min(max(w) for w in ac)
            if best is None or L < best["L"]:
                best = {"L": L, "cap": cap, "antichain": len(ac), "iters": k}
            else:
                break  # larger cap did not lower the threshold
    if best is None:
        return {"L": None}
    L = best["L"]
    if L == 0:
        best.update(lower="trivial", certified=True)
        return best
    steps, frontier = forward_horizon(S, L - 1, max_steps=max_steps)
    best.update(lower_steps=steps if frontier == 0 else None, frontier=frontier)
    best["certified"] = (frontier == 0)
    return best


def winning_word(S, L, cap, acts=None):
    """an explicit eventually-periodic blind word keeping S alive from common
    slack L, extracted from the saturated-game winning region (cap must be
    large enough that the game wins from L).  Returns (prefix, period) as
    lists of actions, or None."""
    S = list(S)
    m = len(S[0])
    acts = acts if acts is not None else actions(m)
    ac, _ = minimal_winning_slacks(S, cap, acts)
    if not ac or min(max(w) for w in ac) > L:
        return None
    n = len(S)
    Dv = [tuple(D(u, th) for th in S) for u in acts]

    def winning(x):
        return any(all(x[i] >= w[i] for i in range(n)) for w in ac)

    s = tuple([L] * n)
    seen = {}
    word = []
    while s not in seen:
        seen[s] = len(word)
        for u, d in zip(acts, Dv):
            x = tuple(min(s[i] + d[i], cap) for i in range(n))
            if min(x) >= 0 and winning(x):
                word.append(u)
                s = x
                break
        else:
            return None
    k = seen[s]
    return word[:k], word[k:]

#!/usr/bin/env python3
"""
ws_core.py -- exact core for paper11c v5 ("worked systems audit").

Everything is computed from the primitives with exact arithmetic
(integers, bitmasks, fractions).  No number in the manuscript or in the
supplement is typed by hand: run_all.py calls the functions below and
writes work/results.json, from which the tables and the verifier are
generated.

Contents
  1. the shared two-coordinate system (grid {0..CAP}^2, instruments 0/1/2)
  2. a generic fibrewise belief-game engine (observation map x protocol
     convention) with exact greatest-fixed-point kernels
  3. kernels on the pair population, on the whole belief universe,
     maximal viable beliefs, stabilisation horizons
  4. stationary-policy unions (memoryless, one-step memory)
  5. decentralised unanimity laws and the statewise factoring
  6. observation-design census over all partitions of the corner-free safe
     states (dynamic vs one-step adequacy)
  7. one-step adequacy on the four-state target, incompatibility graph,
     Helly numbers
  8. hidden-regime model (frozen / mode-blind)
  9. review timing on regime graphs (max-plus)
 10. continuous benchmark fibre, static duality, drift audit, floors,
     margins (fractions)
"""
from fractions import Fraction as Q
from itertools import product, combinations
from functools import lru_cache
import math

# ----------------------------------------------------------------------------
# 1. shared system
# ----------------------------------------------------------------------------

def make_system(cap=3):
    """Return the primitives of the shared system with cap `cap`."""
    states = [(a, b) for a in range(cap + 1) for b in range(cap + 1)]
    safe = [x for x in states if x[0] >= 1 and x[1] >= 1]

    def step(x, u):
        z1, z2 = x
        if u == 0:
            return (max(0, z1 - 1), max(0, z2 - 1))
        if u == 1:
            return (min(cap, z1 + 1), max(0, z2 - 1))
        return (max(0, z1 - 1), min(cap, z2 + 1))
    return dict(cap=cap, states=states, safe=safe, step=step,
                safeset=frozenset(safe))


SYS = make_system(3)
CAP = 3
STATES = SYS['states']
SAFE = SYS['safe']                     # 9 states, sorted lexicographically
SAFESET = SYS['safeset']
step = SYS['step']
CORNER = (1, 1)
CORNER_FREE = [x for x in SAFE if x != CORNER]   # 8 states
PAIRS = sorted(frozenset({x, y}) for x in SAFE for y in SAFE if x < y)
assert len(PAIRS) == 36

obs_full = lambda x: x
obs_agg = lambda x: x[0] + x[1]

def safe_actions(x, actions=(1, 2), sysd=SYS):
    """R(x): instruments keeping x in the safe set for one step."""
    return [u for u in actions if sysd['step'](x, u) in sysd['safeset']]


def label(x):
    return f"{x[0]}{x[1]}"


def blabel(B):
    return "|".join(label(x) for x in sorted(B))

# ----------------------------------------------------------------------------
# 2. generic fibrewise belief-game engine
# ----------------------------------------------------------------------------
# A node is (tokens, register).  A token is a state (conventions 'free',
# 'ledger', 'optimistic', 'first', 'last') or a (state, last-action) pair
# (convention 'branch').  options(node) returns the list of admissible
# option sets: each option is a frozenset of successor nodes that must ALL
# be viable for the option to certify the node.  The kernel is the greatest
# fixed point of  W = {n : exists option O of n with O subset of W}  on the
# reachable node graph, which equals the limit of the finite-horizon family
# W_h (W_0 = everything reachable, W_{h+1} = {n in W_h : exists O subset W_h}).


class BeliefGame:
    def __init__(self, obs, convention='free', actions=(1, 2), sysd=SYS):
        self.obs = obs
        self.conv = convention
        self.actions = tuple(actions)
        self.sysd = sysd
        self.step = sysd['step']
        self.safeset = sysd['safeset']
        self._opt = {}

    # -- fibres -----------------------------------------------------------
    def fibres(self, tokens):
        cells = {}
        if self.conv == 'branch':
            for (x, l) in tokens:
                cells.setdefault(self.obs(x), set()).add((x, l))
        else:
            for x in tokens:
                cells.setdefault(self.obs(x), set()).add(x)
        def mn(k):
            c = cells[k]
            return min(x for x, l in c) if self.conv == 'branch' else min(c)
        keys = sorted(cells, key=mn)
        return [(k, frozenset(cells[k])) for k in keys]

    def fibre_actions(self, fibre, register):
        """Common admissible actions of a fibre under the protocol."""
        if self.conv == 'branch':
            acts = [u for u in self.actions
                    if all(self.step(x, u) in self.safeset for x, l in fibre)
                    and all(u != l for x, l in fibre)]
        else:
            acts = [u for u in self.actions
                    if all(self.step(x, u) in self.safeset for x in fibre)]
            if self.conv != 'free' and register is not None:
                acts = [u for u in acts if u != register]
        return acts

    # -- options ----------------------------------------------------------
    def options(self, node):
        if node in self._opt:
            return self._opt[node]
        tokens, reg = node
        fib = self.fibres(tokens)
        acts = [self.fibre_actions(f, reg) for _, f in fib]
        res = []
        if all(acts):
            for choice in product(*acts):
                if self.conv == 'branch':
                    succ = frozenset((self.step(x, u), u)
                                     for (_, f), u in zip(fib, choice)
                                     for (x, l) in f)
                    parts = [p for _, p in self.fibres(succ)]
                    res.append(frozenset((p, None) for p in parts))
                    continue
                succ = frozenset(self.step(x, u)
                                 for (_, f), u in zip(fib, choice) for x in f)
                parts = [p for _, p in self.fibres(succ)]
                if self.conv == 'free':
                    res.append(frozenset((p, None) for p in parts))
                elif self.conv == 'ledger':        # pessimistic: all issued
                    issued = sorted(set(choice))
                    res.append(frozenset((p, r) for p in parts for r in issued))
                elif self.conv == 'optimistic':    # favourable thread
                    for r in sorted(set(choice)):
                        res.append(frozenset((p, r) for p in parts))
                elif self.conv == 'first':
                    res.append(frozenset((p, choice[0]) for p in parts))
                elif self.conv == 'last':
                    res.append(frozenset((p, choice[-1]) for p in parts))
                else:
                    raise ValueError(self.conv)
        self._opt[node] = res
        return res

    def initial(self, B):
        if self.conv == 'branch':
            return (frozenset((x, None) for x in B), None)
        return (frozenset(B), None)

    # -- kernels ----------------------------------------------------------
    def reachable(self, roots):
        seen = set(roots)
        stack = list(roots)
        while stack:
            n = stack.pop()
            for O in self.options(n):
                for m in O:
                    if m not in seen:
                        seen.add(m)
                        stack.append(m)
        return seen

    def kernel_nodes(self, roots):
        """Greatest fixed point on the reachable graph; also returns the
        horizon family sizes until stabilisation."""
        R = self.reachable(roots)
        W = set(R)
        history = [len(W)]
        while True:
            newW = {n for n in W if any(O <= W for O in self.options(n))}
            history.append(len(newW))
            if newW == W:
                break
            W = newW
        return W, history

    def kernel(self, beliefs):
        roots = [self.initial(B) for B in beliefs]
        W, hist = self.kernel_nodes(roots)
        viable = frozenset(B for B in beliefs if self.initial(B) in W)
        return viable, hist

    def horizon_family(self, beliefs, hmax=12):
        """W_h on the given beliefs for h = 0..hmax (finite-horizon
        recursion from W_0 = all reachable nodes)."""
        roots = [self.initial(B) for B in beliefs]
        R = self.reachable(roots)
        W = set(R)
        fam = [frozenset(B for B in beliefs if self.initial(B) in W)]
        for h in range(hmax):
            W = {n for n in W if any(O <= W for O in self.options(n))}
            fam.append(frozenset(B for B in beliefs if self.initial(B) in W))
        return fam


def all_beliefs(states=SAFE):
    out = []
    for r in range(1, len(states) + 1):
        for c in combinations(states, r):
            out.append(frozenset(c))
    return out


UNIVERSE = all_beliefs(SAFE)          # 511 non-empty beliefs
assert len(UNIVERSE) == 511


def maximal_sets(family):
    fam = list(family)
    return sorted((B for B in fam
                   if not any(B < C for C in fam)),
                  key=lambda B: (-len(B), sorted(B)))


def is_downset(family, universe=None):
    fam = set(family)
    for B in fam:
        for x in B:
            C = B - {x}
            if C and C not in fam:
                return False
    return True


CLASSES = [  # (key, name, obs, convention)
    ('inst', 'institutional', obs_agg, 'ledger'),
    ('agg', 'aggregate', obs_agg, 'free'),
    ('codex', 'codex', obs_full, 'ledger'),
    ('full', 'full', obs_full, 'free'),
]


def class_kernels(conv_override=None, beliefs=PAIRS, actions=(1, 2), sysd=SYS):
    out = {}
    for key, name, obs, conv in CLASSES:
        c = conv
        if conv_override is not None and conv == 'ledger':
            c = conv_override
        if sysd is not SYS:
            # rebuild observation maps for other caps (same formulas)
            pass
        g = BeliefGame(obs, c, actions, sysd)
        K, hist = g.kernel(beliefs)
        out[key] = dict(name=name, kernel=K, size=len(K), history=hist)
    return out

# ----------------------------------------------------------------------------
# 3b. two-instrument no-repeat = alternation: closed forms
# ----------------------------------------------------------------------------

def alternation_trajectory(x, a, steps=24, sysd=SYS):
    """States visited under strict alternation starting with instrument a."""
    traj = [x]
    u = a
    for _ in range(steps):
        x = sysd['step'](x, u)
        traj.append(x)
        u = 3 - u
    return traj


def alternation_safe(x, a, sysd=SYS):
    return all(y in sysd['safeset'] for y in alternation_trajectory(x, a, sysd=sysd))


def ledger_kernel_closed_form(beliefs, obs, sysd=SYS):
    """Closed form of the pessimistic-ledger no-repeat kernel with two
    instruments: choose a first instrument per fibre (safe on the fibre);
    afterwards the whole belief alternates globally, and must survive the
    global alternation from every issued phase."""
    out = set()
    for B in beliefs:
        cells = {}
        for x in B:
            cells.setdefault(obs(x), set()).add(x)
        fib = list(cells.values())
        acts = [[u for u in (1, 2) if all(sysd['step'](x, u) in sysd['safeset']
                                           for x in f)] for f in fib]
        if not all(acts):
            continue
        ok = False
        for choice in product(*acts):
            succ = {sysd['step'](x, u) for f, u in zip(fib, choice) for x in f}
            issued = set(choice)
            if all(alternation_safe(y, 3 - r, sysd) for y in succ for r in issued):
                ok = True
                break
        if ok:
            out.add(B)
    return frozenset(out)


def branch_kernel_closed_form(beliefs, obs, sysd=SYS, horizon=24):
    """Closed form of the per-branch (correlated, unobserved register)
    no-repeat kernel: a fibre-constant phase assignment whose alternating
    threads are safe and phase-coherent (tokens sharing a fibre at any time
    carry the same next instrument)."""
    out = set()
    for B in beliefs:
        cells = {}
        for x in B:
            cells.setdefault(obs(x), set()).add(x)
        fib = list(cells.values())
        ok = False
        for choice in product((1, 2), repeat=len(fib)):
            threads = []
            good = True
            for f, a in zip(fib, choice):
                for x in f:
                    tr = alternation_trajectory(x, a, horizon, sysd)
                    if not all(y in sysd['safeset'] for y in tr):
                        good = False
                        break
                    threads.append((tr, a))
                if not good:
                    break
            if not good:
                continue
            # phase coherence: at time t, next instrument of a thread with
            # first instrument a is a if t even else 3-a
            coherent = True
            for t in range(horizon + 1):
                seen = {}
                for tr, a in threads:
                    nxt = a if t % 2 == 0 else 3 - a
                    o = obs(tr[t])
                    if o in seen and seen[o] != nxt:
                        coherent = False
                        break
                    seen[o] = nxt
                if not coherent:
                    break
            if coherent:
                ok = True
                break
        if ok:
            out.add(B)
    return frozenset(out)

# ----------------------------------------------------------------------------
# 4. stationary policies
# ----------------------------------------------------------------------------

def closed_loop_safe(x, policy, obs, memory=False, sysd=SYS, steps=40):
    """Deterministic closed loop under a stationary policy; memory=True
    means the policy reads (observation, last instrument)."""
    last = None
    for _ in range(steps):
        if x not in sysd['safeset']:
            return False
        u = policy[(obs(x), last)] if memory else policy[obs(x)]
        x = sysd['step'](x, u)
        last = u
    return x in sysd['safeset']


def stationary_union(obs, memory=False, no_repeat=False, sysd=SYS,
                     beliefs=PAIRS, actions=(1, 2)):
    """Union over all deterministic stationary policies of the sustained
    beliefs; also the set of sustained states per policy."""
    cells = sorted({obs(x) for x in sysd['safe']})
    if memory:
        keys = [(c, l) for c in cells for l in (None,) + tuple(actions)]
    else:
        keys = cells
    policies = 0
    sustained_states = []
    union = set()
    best = 0
    for choice in product(actions, repeat=len(keys)):
        pol = dict(zip(keys, choice))
        if no_repeat and memory and any(pol[(c, l)] == l for (c, l) in keys
                                        if l is not None):
            continue
        policies += 1
        S = frozenset(x for x in sysd['safe']
                      if closed_loop_safe(x, pol, obs, memory, sysd))
        sustained_states.append(S)
        best = max(best, len(S))
        for B in beliefs:
            if B <= S:
                union.add(B)
    return dict(policies=policies, union=frozenset(union),
                max_states=best,
                sustained=sorted({S for S in sustained_states}, key=lambda S: (-len(S), sorted(S))))

# ----------------------------------------------------------------------------
# 5. decentralised unanimity
# ----------------------------------------------------------------------------

LAWS = [dict(zip(range(CAP + 1), t)) for t in product((1, 2), repeat=CAP + 1)]
LAW_PAIRS = [(l1, l2) for l1 in LAWS for l2 in LAWS]
assert len(LAW_PAIRS) == 256


def law_str(l):
    return "".join(str(l[z]) for z in range(CAP + 1))


def unanimity_step(x, l1, l2, sysd=SYS):
    u = l1[x[0]] if l1[x[0]] == l2[x[1]] else 0
    return sysd['step'](x, u)


def law_sustains_state(x, l1, l2, sysd=SYS):
    seen = set()
    while x not in seen:
        if x not in sysd['safeset']:
            return False
        seen.add(x)
        x = unanimity_step(x, l1, l2, sysd)
    return True


def law_sustains_belief(B, l1, l2, sysd=SYS):
    cur, seen = frozenset(B), set()
    while True:
        if not cur <= sysd['safeset']:
            return False
        if cur in seen:
            return True
        seen.add(cur)
        cur = frozenset(unanimity_step(x, l1, l2, sysd) for x in cur)


def sustainers():
    """S(x) = indices of law pairs sustaining x, for every safe state."""
    return {x: frozenset(i for i, (l1, l2) in enumerate(LAW_PAIRS)
                         if law_sustains_state(x, l1, l2)) for x in SAFE}


def decentralised_kernel(beliefs, S=None):
    S = S or sustainers()
    return frozenset(B for B in beliefs
                     if frozenset.intersection(*[S[x] for x in B]))


def behavioural_class(l):
    return tuple(l[z] for z in range(1, CAP + 1))

# ----------------------------------------------------------------------------
# 6. observation-design census (free protocol, corner-free safe states)
# ----------------------------------------------------------------------------

def set_partitions(items):
    items = list(items)
    if not items:
        yield []
        return
    first, rest = items[0], items[1:]
    for p in set_partitions(rest):
        for i in range(len(p)):
            yield p[:i] + [[first] + p[i]] + p[i + 1:]
        yield p + [[first]]


def bit_index(states):
    return {x: i for i, x in enumerate(states)}


def kernel_free_bitmask(cells, states=CORNER_FREE, sysd=SYS, actions=(1, 2)):
    """Exact kernel of the free-protocol belief game for the observation
    partition `cells` (list of lists of states) on subsets of `states`.
    Returns the set of viable belief masks (non-empty) and the horizon
    history."""
    idx = bit_index(states)
    n = len(states)
    cellmasks = []
    for c in cells:
        m = 0
        for x in c:
            if x in idx:
                m |= 1 << idx[x]
        if m:
            cellmasks.append(m)
    # image of a fibre mask under action u: None if some successor unsafe
    # or outside `states`; else mask
    succ_bit = {}
    for x in states:
        for u in actions:
            y = sysd['step'](x, u)
            succ_bit[(x, u)] = idx[y] if y in idx else None
    img_cache = {}

    def image(m, u):
        key = (m, u)
        if key in img_cache:
            return img_cache[key]
        out = 0
        mm = m
        while mm:
            b = mm & -mm
            i = b.bit_length() - 1
            j = succ_bit[(states[i], u)]
            if j is None:
                out = None
                break
            out |= 1 << j
            mm ^= b
        img_cache[key] = out
        return out

    full = (1 << n) - 1
    W = set(range(1, full + 1))
    W.add(0)
    history = [len(W) - 1]
    opts = {}
    for B in range(1, full + 1):
        fib = [B & c for c in cellmasks if B & c]
        choices = []
        ok = True
        for f in fib:
            cs = [(u, image(f, u)) for u in actions]
            cs = [(u, im) for u, im in cs if im is not None]
            if not cs:
                ok = False
                break
            choices.append(cs)
        if not ok:
            opts[B] = []
            continue
        lst = []
        for ch in product(*choices):
            s = 0
            for u, im in ch:
                s |= im
            parts = tuple(s & c for c in cellmasks if s & c)
            lst.append(parts)
        opts[B] = lst
    while True:
        newW = {B for B in W if B == 0 or any(all(p in W for p in parts)
                                               for parts in opts[B])}
        history.append(len(newW) - 1)
        if newW == W:
            break
        W = newW
    W.discard(0)
    return W, history


def mask_to_set(m, states=CORNER_FREE):
    return frozenset(x for i, x in enumerate(states) if m >> i & 1)


def incompatibility_edges(states, sysd=SYS, actions=(1, 2)):
    return {(a, b) for a in states for b in states if a < b
            and not set(safe_actions(a, actions, sysd)) & set(safe_actions(b, actions, sysd))}


def one_step_adequate(partition, edges):
    return all(not ({a, b} <= set(F)) for F in partition for (a, b) in edges)


def design_census(states=CORNER_FREE, sysd=SYS):
    """Census over all set partitions of `states`: dynamic adequacy of the
    whole set, kernel size, one-step adequacy."""
    edges = incompatibility_edges(states, sysd)
    rows = []
    for P in set_partitions(states):
        cells = [sorted(c) for c in P]
        cells.sort()
        W, hist = kernel_free_bitmask(cells, states, sysd)
        full = (1 << len(states)) - 1
        maxs = maximal_sets(mask_to_set(m, states) for m in W) if W else []
        rows.append(dict(cells=cells, ncells=len(cells),
                         kernel=len(W), full_viable=(full in W),
                         one_step=one_step_adequate(cells, edges),
                         max_belief=max((len(B) for B in maxs), default=0),
                         n_max=len(maxs),
                         pairs=sum(1 for m in W if bin(m).count('1') == 2),
                         stab=len(hist) - 2))
    return rows, edges

# ----------------------------------------------------------------------------
# 7. one-step adequacy on the four-state target, Helly numbers
# ----------------------------------------------------------------------------

TARGET = [(1, 2), (2, 1), (2, 2), (3, 1)]


def helly_number(sets):
    """Largest size of an inclusion-minimal subfamily with empty
    intersection (the Helly number of the family)."""
    lst = [frozenset(s) for s in sets]
    best = 0
    for r in range(1, len(lst) + 1):
        for sub in combinations(lst, r):
            inter = frozenset.intersection(*sub)
            if not inter:
                minimal = all(frozenset.intersection(*(sub[:i] + sub[i + 1:]))
                              for i in range(r)) if r > 1 else True
                if minimal:
                    best = max(best, r)
    return best


def target_census():
    edges = incompatibility_edges(TARGET)
    parts = [tuple(tuple(sorted(F)) for F in sorted(P)) for P in set_partitions(TARGET)]
    parts = sorted(set(tuple(sorted(P)) for P in parts))
    adequate = [P for P in parts if one_step_adequate(P, edges)]
    R = {x: tuple(safe_actions(x)) for x in TARGET}
    # inclusion-exclusion over the two edges
    def merges(P, a, b):
        return any({a, b} <= set(F) for F in P)
    e = sorted(edges)
    n_e = [sum(1 for P in parts if merges(P, *ed)) for ed in e]
    n_both = sum(1 for P in parts if all(merges(P, *ed) for ed in e))
    # maximal common-action sets of the target
    subsets = [frozenset(c) for r in range(1, 5) for c in combinations(TARGET, r)]
    common = [S for S in subsets if set.intersection(*[set(R[x]) for x in S])]
    maxcommon = maximal_sets(common)
    a2 = [frozenset({1}), frozenset({2}), frozenset({1, 2})]
    a3 = [frozenset(s) for s in ({1, 2}, {2, 3}, {1, 3}, {1}, {2}, {3})]
    return dict(partitions=parts, n=len(parts), adequate=adequate,
                n_adequate=len(adequate), edges=e, n_e=n_e, n_both=n_both,
                R=R, maxcommon=maxcommon,
                two_cell=[P for P in adequate if len(P) == 2],
                helly2=helly_number(a2), helly3=helly_number(a3))

# ----------------------------------------------------------------------------
# 8. hidden-regime model
# ----------------------------------------------------------------------------

def step_regime(x, u, r, cap=CAP):
    z = [x[0], x[1]]
    z[u - 1] = min(cap, z[u - 1] + 1)
    z[r - 1] = max(0, z[r - 1] - 1)
    return (z[0], z[1])


def frozen_viable(x, r, steps=24):
    for _ in range(steps):
        x = step_regime(x, r if x[r - 1] < CAP else 3 - r, r)
        if x not in SAFESET:
            return False
    return True


@lru_cache(maxsize=None)
def mode_blind_win(x, h):
    if h == 0:
        return x in SAFESET
    return any(all(mode_blind_win(step_regime(x, u, rr), h - 1) for rr in (1, 2))
               for u in (1, 2))


def regime_results():
    frozen = {r: frozenset(x for x in SAFE if frozen_viable(x, r)) for r in (1, 2)}
    pin = all(step_regime(x, r, r) == x for x in SAFE for r in (1, 2) if x[r - 1] < CAP)
    H = 12
    mb = frozenset(x for x in SAFE if mode_blind_win(x, H) and mode_blind_win(x, H - 2))
    frozen_pairs = {r: sum(1 for B in PAIRS if B <= frozen[r]) for r in (1, 2)}
    mb_pairs = sum(1 for B in PAIRS if B <= mb)
    return dict(frozen=frozen, pin=pin, mode_blind=mb,
                frozen_pairs=frozen_pairs, mb_pairs=mb_pairs)

# ----------------------------------------------------------------------------
# 9. review timing on regime graphs (max-plus)
# ----------------------------------------------------------------------------

def worst_damage_free(T, dmax=Q(1)):
    return T * dmax


def worst_damage_alt(T, d=(Q(1), Q(1, 2))):
    best = Q(0)
    for start in (0, 1):
        best = max(best, sum(d[(start + i) % 2] for i in range(T)))
    return best


def maxplus_worst(T, d, edges):
    """Worst cumulative damage over admissible regime paths of length T on a
    regime graph (max-plus matrix power)."""
    regs = sorted(d)
    cur = {r: d[r] for r in regs}
    best = max(cur.values())
    for _ in range(T - 1):
        cur = {r: max([d[r] + cur[q] for q in regs if (q, r) in edges] or [None])
               for r in regs}
        cur = {r: v for r, v in cur.items() if v is not None}
        best = max(best, max(cur.values()))
    return best


def brute_worst(T, d, edges):
    regs = sorted(d)
    best = None
    for seq in product(regs, repeat=T):
        if all((seq[i - 1], seq[i]) in edges for i in range(1, T)):
            v = sum(d[r] for r in seq)
            best = v if best is None else max(best, v)
    return best


def timing_grid():
    grid = [Q(n, 10) for n in range(10, 41)]
    tos = [1, 2, 3]
    rows = []
    viable_free = viable_alt = 0
    strict_real_bad, strict_floor_bad = [], []
    for z in grid:
        sig = math.floor(z - 1)
        row = []
        for T in tos:
            Df = worst_damage_free(T)
            Da = worst_damage_alt(T)
            vf = Df <= z - 1
            va = Da <= z - 1
            viable_free += vf
            viable_alt += va
            if ((z - 1) > T) != vf:
                strict_real_bad.append((z, T))
            if (sig > T) != vf:
                strict_floor_bad.append((z, T))
            row.append((vf, va))
        rows.append((z, sig, row))
    d3 = {0: Q(1), 1: Q(1, 2), 2: Q(1, 4)}
    E3 = {(a, b) for a in d3 for b in d3 if a != b}
    dp_ok = all(maxplus_worst(T, d3, E3) == brute_worst(T, d3, E3) for T in range(1, 7))
    alt_by_T = {T: sum(1 for z in grid if worst_damage_alt(T) <= z - 1) for T in tos}
    return dict(grid=grid, rows=rows, cells=len(grid) * 3, viable_free=viable_free,
                viable_alt=viable_alt, alt_by_T=alt_by_T,
                strict_real_bad=strict_real_bad, strict_floor_bad=strict_floor_bad,
                dp_ok=dp_ok, d3=d3,
                worst3=[maxplus_worst(T, d3, E3) for T in range(1, 7)])

# ----------------------------------------------------------------------------
# 10. continuous benchmark fibre, duality, drift, floors, margins
# ----------------------------------------------------------------------------

def cap1(Y):
    return Q(3, 2) - (Y - 2) / 10


def cap2(Y):
    return Q(59, 50) - (Y - 2) / 10


DEMAND = Q(2)


def benchmark():
    """Two capped instruments u_i in [0, c_i(Y)] must meet the demand
    u_1 + u_2 >= 2; the caps fall linearly in the pressure Y."""
    Ystar = Q(2) + (cap1(Q(2)) + cap2(Q(2)) - DEMAND) * 5  # cap sum has slope -1/5
    assert cap1(Ystar) + cap2(Ystar) == DEMAND
    dual = (Q(1, 2), Q(1, 2))                       # normalised dual weights

    def margin(Y):
        # dual-weighted deficiency  lambda.(demand split) - lambda.caps  with
        # the demand row u_1 + u_2 >= 2 priced at the normalised weights
        return DEMAND / 2 - (dual[0] * cap1(Y) + dual[1] * cap2(Y))
    rows = []
    for Y in [Q(4), Q(9, 2), Q(5), Q(27, 5), Q(11, 2), Q(6), Q(7)]:
        s = cap1(Y) + cap2(Y)
        rows.append(dict(Y=Y, c1=cap1(Y), c2=cap2(Y), sum=s, feasible=s >= DEMAND,
                         margin=margin(Y) if s < DEMAND else Q(0)))
    witness5 = (Q(6, 5), Q(4, 5))
    assert witness5[0] <= cap1(Q(5)) and witness5[1] <= cap2(Q(5)) and sum(witness5) >= DEMAND
    marg6 = margin(Q(6))
    # robustness radius: raising both caps by delta restores feasibility iff
    # 2 delta >= DEMAND - (c1 + c2), i.e. delta >= marg6 (dual weights sum to 1)
    radius = (DEMAND - (cap1(Q(6)) + cap2(Q(6)))) / 2
    return dict(Ystar=Ystar, rows=rows, witness5=witness5, dual=dual,
                margin6=marg6, radius6=radius,
                margin_law_check=all((r['Y'] - Ystar) / 10 == r['margin']
                                     for r in rows if r['Y'] > Ystar),
                below_radius_still_obstructed=(cap1(Q(6)) + radius / 2) + (cap2(Q(6)) + radius / 2) < DEMAND,
                at_radius_feasible=(cap1(Q(6)) + radius) + (cap2(Q(6)) + radius) >= DEMAND)


def _game_values(rows, U, lams):
    """primal = max_u min_j r_j(u); dual = min_lambda max_u sum lambda_j r_j(u)."""
    primal = max(min(r(u) for r in rows) for u in U)
    ustar = [u for u in U if min(r(u) for r in rows) == primal]
    dualv = min(max(sum(l * r(u) for l, r in zip(lam, rows)) for u in U) for lam in lams)
    lstar = [lam for lam in lams if max(sum(l * r(u) for l, r in zip(lam, rows)) for u in U) == dualv]
    return primal, ustar, dualv, lstar


def duality():
    grid = [Q(n, 100) for n in range(0, 101)]
    lams = [(Q(n, 100), 1 - Q(n, 100)) for n in range(0, 101)]
    rows = [lambda u: Q(2, 5) - u, lambda u: u - Q(3, 5)]
    primal, ustar, dualv, lstar = _game_values(rows, grid, lams)
    # nonconvex control set {0, 1}, payoff rows (-1, +1) and (+1, -1)
    nrows = [lambda u: Q(-1) if u == 0 else Q(1), lambda u: Q(1) if u == 0 else Q(-1)]
    np_, nu, nd, nl = _game_values(nrows, [Q(0), Q(1)], lams)
    # feasible contrast: rows 2/5 - u and u - 1/5
    frows = [lambda u: Q(2, 5) - u, lambda u: u - Q(1, 5)]
    fp, fu, fd, fl = _game_values(frows, grid, lams)
    # Helly-tight triple
    halfs = [lambda v: v[0] >= 1, lambda v: v[1] >= 1, lambda v: v[0] + v[1] <= 1]
    pts = [(Q(a, 2), Q(b, 2)) for a in range(0, 5) for b in range(0, 5)]
    pairwise = all(any(h1(p) and h2(p) for p in pts) for h1, h2 in combinations(halfs, 2))
    triple = any(all(h(p) for h in halfs) for p in pts)
    return dict(primal=primal, ustar=ustar, dual=dualv, lstar=lstar,
                nonconvex_primal=np_, nonconvex_dual=nd,
                feasible_primal=fp, feasible_dual=fd, feasible_u=fu,
                helly_pairwise=pairwise, helly_triple=triple)


def drift():
    g = lambda s: s * s
    lead = Q(1, 10)
    rows = []
    for s in [Q(1), Q(5, 4), Q(3, 2), Q(7, 4), Q(2)]:
        naive = g(s + lead) - g(s)         # s/5 + 1/100
        corrected = g(s + lead) - g(s) - (2 * s * lead + lead * lead)
        rows.append(dict(s=s, naive=naive, corrected=corrected))
    formula_ok = all(r['naive'] == r['s'] / 5 + Q(1, 100) for r in rows)
    # sign law: correction error e gives drift 2 s e + e^2
    sign_ok = all(((2 * Q(1) * e + e * e) > 0) == (e > 0) for e in (Q(-1, 20), Q(1, 20)))
    return dict(rows=rows, formula_ok=formula_ok, sign_ok=sign_ok)


def floors():
    grid = [Q(n, 20) for n in range(-20, 21)]
    f1 = lambda u: u - Q(1, 2)
    f2 = lambda u: -u - Q(1, 2)
    each = all(any(f(u) >= 0 for u in grid) for f in (f1, f2))
    common = any(f1(u) >= 0 and f2(u) >= 0 for u in grid)
    value = max(min(f1(u), f2(u)) for u in grid)
    return dict(each=each, common=common, value=value)


# ----------------------------------------------------------------------------
# convenience
# ----------------------------------------------------------------------------

def fr(q):
    q = Q(q)
    return str(q.numerator) if q.denominator == 1 else f"{q.numerator}/{q.denominator}"


if __name__ == '__main__':
    import time
    t0 = time.time()
    ks = class_kernels()
    print({k: v['size'] for k, v in ks.items()}, [v['history'] for v in ks.values()])
    print('branch', {k: v['size'] for k, v in class_kernels('branch').items()})
    print('opt', {k: v['size'] for k, v in class_kernels('optimistic').items()})
    print('first', {k: v['size'] for k, v in class_kernels('first').items()})
    print('last', {k: v['size'] for k, v in class_kernels('last').items()})
    S = sustainers()
    print('dec', len(decentralised_kernel(PAIRS, S)))
    print(time.time() - t0)

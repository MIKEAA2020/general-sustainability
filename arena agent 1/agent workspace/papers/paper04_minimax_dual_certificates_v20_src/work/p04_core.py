#!/usr/bin/env python3
"""
p04_core.py -- exact module for paper04 v20 (minimax dual certificates of the
common-action obstruction).

Everything is in exact rational arithmetic (fractions.Fraction).  Floating
point is used only, optionally, to *propose* dual weights through SciPy's
HiGHS; every proposed certificate is then verified exactly.

Contents
  * exact linear algebra and polytopes given by inequalities (vertex
    enumeration, support functions, membership);
  * finite row systems psi_i(u) = c_i + v_i.u over a compact convex U:
    the exact lower value  max_{u in U} min_i psi_i(u)  (an LP solved by
    vertex enumeration in (u,t)-space), feasibility, exact verification of
    measure certificates, minimal infeasible subfamilies (Helly numbers);
  * the general-k tight family and its control-affine realization;
  * the convex-hull characterization of the non-convex case;
  * the polyhedral (Farkas with control-set facets) recovery;
  * the two-stock benchmark: model, caps, margin function, demand-floor law;
  * the two-patch finite codex for the obstruction taxonomy;
  * finite review envelopes with action-dependent partitions: node
    recursion, policy-tree enumeration, tower/martingale checks, robust value
    over a coupling class;
  * the integrated (finite-horizon) certificate of the three-branch instance.
"""
from fractions import Fraction as Q
import itertools, random

# =============================================================== linear algebra
def solve_linear(A, b):
    """Solve A x = b exactly (square); return None if singular."""
    n = len(A)
    M = [list(map(Q, row)) + [Q(bi)] for row, bi in zip(A, b)]
    for col in range(n):
        piv = next((r for r in range(col, n) if M[r][col] != 0), None)
        if piv is None:
            return None
        M[col], M[piv] = M[piv], M[col]
        pv = M[col][col]
        M[col] = [x / pv for x in M[col]]
        for r in range(n):
            if r != col and M[r][col] != 0:
                f = M[r][col]
                M[r] = [x - f * y for x, y in zip(M[r], M[col])]
    return tuple(M[i][n] for i in range(n))


def dot(a, b):
    return sum(Q(x) * Q(y) for x, y in zip(a, b))


# ==================================================================== polytopes
class Polytope:
    """{u in R^k : a.u <= c for (a, c) in ineqs}; assumed bounded when
    support functions are requested."""

    def __init__(self, ineqs, k):
        self.ineqs = [(tuple(map(Q, a)), Q(c)) for a, c in ineqs]
        self.k = k
        self._verts = None

    @staticmethod
    def box(lo, hi, k):
        ineqs = []
        for i in range(k):
            e = [0] * k
            e[i] = 1
            ineqs.append((tuple(e), hi))
            ineqs.append((tuple(-x for x in e), -Q(lo)))
        return Polytope(ineqs, k)

    def with_ineqs(self, extra):
        return Polytope(self.ineqs + list(extra), self.k)

    def contains(self, u, strict=False):
        return all((dot(a, u) < c) if strict else (dot(a, u) <= c) for a, c in self.ineqs)

    def vertices(self):
        if self._verts is None:
            vs = set()
            for sub in itertools.combinations(range(len(self.ineqs)), self.k):
                A = [self.ineqs[i][0] for i in sub]
                b = [self.ineqs[i][1] for i in sub]
                x = solve_linear(A, b)
                if x is not None and self.contains(x):
                    vs.add(x)
            self._verts = sorted(vs)
        return self._verts

    def support(self, g):
        """h_U(g) = max_{u in U} g.u"""
        return max(dot(g, v) for v in self.vertices())

    def argsupport(self, g):
        return max(self.vertices(), key=lambda v: dot(g, v))


def simplex_param(m):
    """The simplex of dimension m-1 in coordinates theta_1..theta_{m-1}
    (theta_m = 1 - sum)."""
    ineqs = []
    for i in range(m - 1):
        e = [0] * (m - 1)
        e[i] = -1
        ineqs.append((tuple(e), 0))
    ineqs.append((tuple([1] * (m - 1)), 1))
    return Polytope(ineqs, m - 1)


# ================================================================= row systems
# a row is (v, c) with psi(u) = c + v.u ; the common safe-action set is
# {u in U : psi_i(u) >= 0 for all i}.
def psi(row, u):
    return row[1] + dot(row[0], u)


def lower_value(rows, U):
    """max_{u in U} min_i psi_i(u), exactly, with a maximizer.
    LP in (u, t): maximize t s.t. t - v_i.u <= c_i, u in U."""
    k = U.k
    lifted = [(tuple([-x for x in v] + [1]), c) for v, c in rows]
    lifted += [(tuple(list(a) + [0]), c) for a, c in U.ineqs]
    best, arg = None, None
    for sub in itertools.combinations(range(len(lifted)), k + 1):
        A = [lifted[i][0] for i in sub]
        b = [lifted[i][1] for i in sub]
        x = solve_linear(A, b)
        if x is None:
            continue
        if all(dot(a, x) <= c for a, c in lifted):
            if best is None or x[-1] > best:
                best, arg = x[-1], x[:-1]
    return best, arg


def feasible(rows, U):
    t, _ = lower_value(rows, U)
    return t >= 0


def pooled(rows, lam):
    v = tuple(sum(Q(l) * Q(r[0][i]) for l, r in zip(lam, rows)) for i in range(len(rows[0][0])))
    c = sum(Q(l) * Q(r[1]) for l, r in zip(lam, rows))
    return v, c


def certificate_margin(rows, U, lam):
    """eps = -max_{u in U} sum_i lam_i psi_i(u); a certificate iff eps > 0."""
    assert all(Q(l) >= 0 for l in lam) and sum(map(Q, lam)) == 1
    v, c = pooled(rows, lam)
    return -(c + U.support(v))


def dual_value_finite(rows, U):
    """min over lam in the simplex of max_{u in U} sum lam_i psi_i(u), exactly:
    the pooled function is affine so the inner max is over the vertices of U;
    the outer min is an LP over the simplex solved by vertex enumeration."""
    m = len(rows)
    verts = U.vertices()
    vals = [[psi(r, w) for r in rows] for w in verts]          # vals[w][i]
    # variables theta_1..theta_{m-1}; theta_m = 1 - sum; minimize s with
    # sum_i theta_i vals[w][i] <= s for all w  <=>  -s + sum_i theta_i (vals[w][i]-vals[w][m-1]) <= -vals[w][m-1]
    S = simplex_param(m)
    lifted = [(tuple(list(a) + [0]), c) for a, c in S.ineqs]
    for w in range(len(verts)):
        coef = [vals[w][i] - vals[w][m - 1] for i in range(m - 1)] + [-1]
        lifted.append((tuple(coef), -vals[w][m - 1]))
    best, arg = None, None
    for sub in itertools.combinations(range(len(lifted)), m):
        A = [lifted[i][0] for i in sub]
        b = [lifted[i][1] for i in sub]
        x = solve_linear(A, b)
        if x is None:
            continue
        if all(dot(a, x) <= c for a, c in lifted):
            if best is None or x[-1] < best:
                best, arg = x[-1], x[:-1]
    lam = tuple(list(arg) + [1 - sum(arg)])
    return best, lam


def minimal_infeasible_size(rows, U, screen=None):
    """Smallest s such that some s-subfamily of rows is infeasible over U
    (exact), together with one such subfamily.  `screen(rows_subset)` may be a
    cheap float oracle returning False only when the subset is certainly
    feasible; every verdict used is confirmed exactly."""
    n = len(rows)
    for s in range(1, n + 1):
        for sub in itertools.combinations(range(n), s):
            subrows = [rows[i] for i in sub]
            if screen is not None and screen(subrows) is False:
                continue
            if not feasible(subrows, U):
                return s, sub
    return None, None


def float_feasible(rows, U):
    """float oracle via HiGHS: returns True/False/None (None = unsure)."""
    try:
        import numpy as np
        from scipy.optimize import linprog
    except Exception:
        return None
    k = U.k
    # maximize t s.t. t - v.u <= c ; A u <= c
    A_ub, b_ub = [], []
    for v, c in rows:
        A_ub.append([-float(x) for x in v] + [1.0]); b_ub.append(float(c))
    for a, c in U.ineqs:
        A_ub.append([float(x) for x in a] + [0.0]); b_ub.append(float(c))
    res = linprog(c=[0.0] * k + [-1.0], A_ub=np.array(A_ub), b_ub=np.array(b_ub),
                  bounds=[(None, None)] * (k + 1), method="highs")
    if res.status != 0:
        return None
    t = -res.fun
    if t > 1e-7:
        return True
    if t < -1e-7:
        return False
    return None


def feasible_fast(rows, U, den=10**6):
    """Exact feasibility verdict with a float LP as a guide: a rationalized
    LP maximizer that passes the exact test certifies feasibility; otherwise
    the exact LP decides."""
    f = float_feasible(rows, U)
    if f is True:
        try:
            import numpy as np
            from scipy.optimize import linprog
            k = U.k
            A_ub, b_ub = [], []
            for v, c in rows:
                A_ub.append([-float(x) for x in v] + [1.0]); b_ub.append(float(c))
            for a, c in U.ineqs:
                A_ub.append([float(x) for x in a] + [0.0]); b_ub.append(float(c))
            res = linprog(c=[0.0] * k + [-1.0], A_ub=np.array(A_ub), b_ub=np.array(b_ub),
                          bounds=[(None, None)] * (k + 1), method="highs")
            u = tuple(Q(float(x)).limit_denominator(den) for x in res.x[:k])
            if U.contains(u) and all(psi(r, u) >= 0 for r in rows):
                return True
        except Exception:
            pass
    return feasible(rows, U)


def helly_study(k, m, n_inst, seed, lo=-1, hi=1, coef=3, fast=False, rank1=False):
    """Random row systems with integer coefficients in [-coef, coef] over the
    box [lo, hi]^k.  Returns (n_infeasible, histogram of the minimal
    infeasible-subfamily size).  With rank1=True all drift coefficient vectors
    are multiples of one random vector (rank-one drift coefficients)."""
    rng = random.Random(seed)
    U = Polytope.box(lo, hi, k)
    hist, infeasible = {}, 0
    feas = feasible_fast if fast else feasible
    for _ in range(n_inst):
        if rank1:
            g = tuple(Q(rng.randint(-coef, coef)) for _ in range(k))
            rows = [(tuple(a * gi for gi in g), Q(rng.randint(-coef, coef)))
                    for a in [Q(rng.randint(-coef, coef)) for _ in range(m)]]
        else:
            rows = [(tuple(Q(rng.randint(-coef, coef)) for _ in range(k)), Q(rng.randint(-coef, coef)))
                    for _ in range(m)]
        if feas(rows, U):
            continue
        infeasible += 1
        s = None
        for size in range(1, m + 1):
            found = False
            for sub in itertools.combinations(range(m), size):
                if not feas([rows[i] for i in sub], U):
                    found = True
                    break
            if found:
                s = size
                break
        hist[s] = hist.get(s, 0) + 1
    return infeasible, hist


# ================================================ the general-k tight family
def tight_rows(k):
    """rows u_i >= 1 (i < k) and sum u_i <= k-1 ; any k are consistent, all
    k+1 are not."""
    rows = []
    for i in range(k):
        v = [0] * k
        v[i] = 1
        rows.append((tuple(v), Q(-1)))
    rows.append((tuple([-1] * k), Q(k - 1)))
    return rows


def tight_realization(k):
    """A control-affine plant realizing tight_rows(k): x in R^{k+1},
    q_i(x) = x_i, xdot = f0 + G u with f0 = (-1,...,-1, k-1), G = [I_k; -1^T].
    Returns (f0, G) and the rows read off at x = 0 (all facets active)."""
    f0 = tuple([Q(-1)] * k + [Q(k - 1)])
    G = [tuple(Q(1) if j == i else Q(0) for j in range(k)) for i in range(k)] + [tuple([Q(-1)] * k)]
    rows = [(G[j], f0[j]) for j in range(k + 1)]      # grad q_j = e_j
    return f0, G, rows


# ============================================== the convex-hull characterization
def value_over_hull(rows, points):
    """max over conv(points) of min_i psi_i(u), via the simplex parametrization."""
    m = len(points)
    rows_theta = []
    for r in rows:
        vals = [psi(r, p) for p in points]
        rows_theta.append((tuple(vals[i] - vals[m - 1] for i in range(m - 1)), vals[m - 1]))
    S = simplex_param(m)
    return lower_value(rows_theta, S)[0]


def value_over_points(rows, points):
    """max over the finite set itself."""
    return max(min(psi(r, p) for r in rows) for p in points)


# ======================================================= the two-stock benchmark
BENCH = dict(r=(Q(1), Q(4, 5)), Kcap=(Q(10), Q(10)), comp=Q(1, 20), shock=Q(1, 10),
             floor=Q(2), demand=Q(2), ucap=Q(2))


def bench_drift(x, u, d, P=BENCH):
    """xdot_i = r_i x_i (1 - x_i/K_i) - comp x_1 x_2 - u_i + d_i"""
    return tuple(P["r"][i] * x[i] * (1 - x[i] / P["Kcap"][i]) - P["comp"] * x[0] * x[1] - u[i] + d[i]
                 for i in range(2))


def bench_U(P=BENCH, demand=None):
    D = P["demand"] if demand is None else demand
    U = Polytope.box(0, P["ucap"], 2)
    return U.with_ineqs([((-1, -1), -D)])


def bench_caps(Y, P=BENCH):
    f = P["floor"]
    c1 = P["r"][0] * f * (1 - f / P["Kcap"][0]) - P["comp"] * f * (Y - f) - P["shock"]
    c2 = P["r"][1] * f * (1 - f / P["Kcap"][1]) - P["comp"] * f * (Y - f) - P["shock"]
    return c1, c2


def bench_rows(Y, P=BENCH, all_atoms=False):
    """rows of the active bundle on the fibre {x1 + x2 = Y, x_i >= floor}:
    atoms ((2, Y-2), facet 1, d) and ((Y-2, 2), facet 2, d).  With
    all_atoms=True both shock values are kept; otherwise the worst shock."""
    f = P["floor"]
    atoms = []
    shocks = [-P["shock"], P["shock"]] if all_atoms else [-P["shock"]]
    for d1 in shocks:
        x = (f, Y - f)
        c = bench_drift(x, (Q(0), Q(0)), (d1, Q(0)))[0]
        atoms.append(((Q(-1), Q(0)), c))
    for d2 in shocks:
        x = (Y - f, f)
        c = bench_drift(x, (Q(0), Q(0)), (Q(0), d2))[1]
        atoms.append(((Q(0), Q(-1)), c))
    return atoms


def bench_margin_formula(Y, P=BENCH):
    """closed form (27 - 5Y)/50 at the printed parameters, in general
    (cap1 + cap2 - D)/2"""
    c1, c2 = bench_caps(Y, P)
    return (c1 + c2 - P["demand"]) / 2


def bench_Ystar(D, P=BENCH):
    """critical aggregate as a function of the demand floor: cap1(Y)+cap2(Y) = D"""
    f = P["floor"]
    const = sum(P["r"][i] * f * (1 - f / P["Kcap"][i]) for i in range(2)) - 2 * P["shock"] + 2 * P["comp"] * f * f
    slope = 2 * P["comp"] * f
    return (const - D) / slope


# ================================================== two-patch finite codex
PATCH_CAP = 3


def patch_step(x, u, g=1, cap=PATCH_CAP):
    """spare patch u (grows by g); the other grows by g and is harvested by 2."""
    y = [min(cap, x[0] + g), min(cap, x[1] + g)]
    other = 1 - u
    y[other] -= 2
    return tuple(y)


def patch_states(cap=PATCH_CAP):
    return [(a, b) for a in range(cap + 1) for b in range(cap + 1)]


def patch_safe(x):
    return x[0] >= 1 and x[1] >= 1


def patch_kernel(actions=(0, 1), g=1):
    S = {x for x in patch_states() if patch_safe(x)}
    while True:
        S2 = {x for x in S if any(patch_step(x, u, g) in S for u in actions)}
        if S2 == S:
            return S
        S = S2


def patch_safe_actions(x, actions=(0, 1), g=1, target=None):
    target = {y for y in patch_states() if patch_safe(y)} if target is None else target
    return {u for u in actions if patch_step(x, u, g) in target}


# ================================================== finite review envelopes
class ReviewProblem:
    """Finite review tree with action-dependent partitions.
    scenarios: list of (omega, prob) with rational probs summing to one.
    actions: list (per stage k = 0..K-1) of finite action lists.
    obs(k, omega, prefix): the observation received before stage k, a
      hashable label; it may depend on the action prefix a_0..a_{k-1}.
    G(omega, actions): rational pathwise functional."""

    def __init__(self, scenarios, actions, obs, G):
        self.sc = [(w, Q(p)) for w, p in scenarios]
        assert sum(p for _, p in self.sc) == 1
        self.actions = actions
        self.K = len(actions)
        self.obs = obs
        self.G = G

    # ---- histories: a history at stage k is the tuple of (obs_0, a_0, obs_1, a_1, ..., obs_k)
    def cell(self, k, prefix, label):
        """scenarios (with mass) compatible with the observation sequence up
        to stage k given the action prefix"""
        out = []
        for w, p in self.sc:
            ok = True
            for j in range(k + 1):
                if self.obs(j, w, prefix[:j]) != label[j]:
                    ok = False
                    break
            if ok:
                out.append((w, p))
        return out

    def node_value(self, k, prefix, label):
        """N_k at the history (label_0..label_k, a_0..a_{k-1}); returns
        (value, best action, dict action->value)."""
        members = self.cell(k, prefix, label)
        mass = sum(p for _, p in members)
        assert mass > 0
        vals = {}
        for a in self.actions[k]:
            pre = prefix + (a,)
            if k == self.K - 1:
                vals[a] = sum(p * Q(self.G(w, pre)) for w, p in members) / mass
            else:
                tot = Q(0)
                for lab in sorted({self.obs(k + 1, w, pre) for w, _ in members}, key=repr):
                    sub = [(w, p) for w, p in members if self.obs(k + 1, w, pre) == lab]
                    sm = sum(p for _, p in sub)
                    v, _, _ = self.node_value(k + 1, pre, label + (lab,))
                    tot += sm * v
                vals[a] = tot / mass
        best = max(vals.values())
        arg = [a for a in self.actions[k] if vals[a] == best]
        return best, arg, vals

    def root_value(self):
        """sum over initial cells of mu(C) N_0(C)"""
        labels = sorted({self.obs(0, w, ()) for w, _ in self.sc}, key=repr)
        tot = Q(0)
        detail = {}
        for lab in labels:
            members = self.cell(0, (), (lab,))
            mass = sum(p for _, p in members)
            v, arg, vals = self.node_value(0, (), (lab,))
            detail[lab] = (v, arg, vals)
            tot += mass * v
        return tot, detail

    # ---- policy trees (adapted, over reachable histories)
    def histories(self):
        """list of reachable histories as (k, prefix, label) in generation
        order, each with its children structure, by DFS from the roots"""
        out = []

        def rec(k, prefix, label):
            out.append((k, prefix, label))
            if k == self.K - 1:
                return
            members = self.cell(k, prefix, label)
            for a in self.actions[k]:
                pre = prefix + (a,)
                for lab in sorted({self.obs(k + 1, w, pre) for w, _ in members}, key=repr):
                    rec(k + 1, pre, label + (lab,))
        for lab in sorted({self.obs(0, w, ()) for w, _ in self.sc}, key=repr):
            rec(0, (), (lab,))
        return out

    def count_policies(self):
        """number of adapted policy trees = product over reachable decision
        nodes along consistent action choices; computed recursively"""
        def cnt(k, prefix, label):
            if k == self.K - 1:
                return len(self.actions[k])
            members = self.cell(k, prefix, label)
            tot = 0
            for a in self.actions[k]:
                pre = prefix + (a,)
                prod = 1
                for lab in sorted({self.obs(k + 1, w, pre) for w, _ in members}, key=repr):
                    prod *= cnt(k + 1, pre, label + (lab,))
                tot += prod
            return tot
        total = 1
        for lab in sorted({self.obs(0, w, ()) for w, _ in self.sc}, key=repr):
            total *= cnt(0, (), (lab,))
        return total

    def policies(self):
        """generate every adapted policy tree as a dict history -> action"""
        def gen(k, prefix, label):
            if k == self.K - 1:
                for a in self.actions[k]:
                    yield {(k, prefix, label): a}
                return
            members = self.cell(k, prefix, label)
            for a in self.actions[k]:
                pre = prefix + (a,)
                labs = sorted({self.obs(k + 1, w, pre) for w, _ in members}, key=repr)
                subgens = [list(gen(k + 1, pre, label + (lab,))) for lab in labs]
                for combo in itertools.product(*subgens):
                    d = {(k, prefix, label): a}
                    for c in combo:
                        d.update(c)
                    yield d
        roots = sorted({self.obs(0, w, ()) for w, _ in self.sc}, key=repr)
        rootgens = [list(gen(0, (), (lab,))) for lab in roots]
        for combo in itertools.product(*rootgens):
            d = {}
            for c in combo:
                d.update(c)
            yield d

    def run(self, pol, w):
        prefix, label = (), ()
        for k in range(self.K):
            label = label + (self.obs(k, w, prefix),)
            prefix = prefix + (pol[(k, prefix, label)],)
        return prefix

    def policy_value(self, pol):
        return sum(p * Q(self.G(w, self.run(pol, w))) for w, p in self.sc)

    def tower_value(self, pol):
        """iterated conditional expectation along the policy's own filtration"""
        def rec(k, prefix, label, members):
            a = pol[(k, prefix, label)]
            pre = prefix + (a,)
            mass = sum(p for _, p in members)
            if k == self.K - 1:
                return sum(p * Q(self.G(w, pre)) for w, p in members) / mass
            tot = Q(0)
            for lab in sorted({self.obs(k + 1, w, pre) for w, _ in members}, key=repr):
                sub = [(w, p) for w, p in members if self.obs(k + 1, w, pre) == lab]
                tot += sum(p for _, p in sub) * rec(k + 1, pre, label + (lab,), sub)
            return tot / mass
        tot = Q(0)
        for lab in sorted({self.obs(0, w, ()) for w, _ in self.sc}, key=repr):
            members = self.cell(0, (), (lab,))
            tot += sum(p for _, p in members) * rec(0, (), (lab,), members)
        return tot

    def martingale_ok(self, pol):
        """M at every node equals the mass-weighted average of M at its
        children (the tower law along the fixed policy's filtration)"""
        ok = True

        def M(k, prefix, label, members):
            nonlocal ok
            a = pol[(k, prefix, label)]
            pre = prefix + (a,)
            mass = sum(p for _, p in members)
            if k == self.K - 1:
                return sum(p * Q(self.G(w, pre)) for w, p in members) / mass
            tot = Q(0)
            for lab in sorted({self.obs(k + 1, w, pre) for w, _ in members}, key=repr):
                sub = [(w, p) for w, p in members if self.obs(k + 1, w, pre) == lab]
                tot += sum(p for _, p in sub) * M(k + 1, pre, label + (lab,), sub)
            val = tot / mass
            # direct conditional expectation of the terminal functional on this node
            direct = sum(p * Q(self.G(w, self.run(pol, w))) for w, p in members) / mass
            if direct != val:
                ok = False
            return val
        for lab in sorted({self.obs(0, w, ()) for w, _ in self.sc}, key=repr):
            members = self.cell(0, (), (lab,))
            M(0, (), (lab,), members)
        return ok

    def defeat_mass(self, pol):
        """mu{G^pi < 0}"""
        return sum(p for w, p in self.sc if Q(self.G(w, self.run(pol, w))) < 0)


# ------------------------------------------------------------ the two-window instance
def two_window(z0=Q(2), actions=(-2, 0, 2), prior_s=Q(1, 2)):
    scen = []
    for s in (1, -1):
        for d1 in (-1, 1):
            for d2 in (-1, 1):
                p = (prior_s if s == 1 else 1 - prior_s) * Q(1, 4)
                scen.append(((s, d1, d2), p))

    def obs(k, w, prefix):
        if k == 0:
            return "blind"
        s, d1, d2 = w
        return z0 + s * prefix[0] + d1           # the review observes z_1 exactly

    def G(w, a):
        s, d1, d2 = w
        z2 = z0 + s * (a[0] + a[1]) + d1 + d2
        return 2 - abs(z2)
    return ReviewProblem(scen, [list(actions), list(actions)], obs, G)


def open_loop_values(z0=Q(2), actions=(-2, 0, 2)):
    vals = {}
    for u1 in actions:
        for u2 in actions:
            tot = Q(0)
            for s in (1, -1):
                for d1 in (-1, 1):
                    for d2 in (-1, 1):
                        z2 = z0 + s * (u1 + u2) + d1 + d2
                        tot += Q(1, 8) * (2 - abs(z2))
            vals[(u1, u2)] = tot
    return vals


# -------------------------------------------- instances A, B, C of the record
def instance_A():
    """K = 3, Omega = {-1,1}^3 uniform, partitions sign(d1) -> (sign d1, sign d2)
    -> singletons, two actions per stage"""
    scen = [(d, Q(1, 8)) for d in itertools.product((-1, 1), repeat=3)]

    def obs(k, w, prefix):
        return w[:k + 1] if k < 2 else w

    def G(d, a):
        return -(abs(d[0]) * a[0]) + (d[1] if d[1] > 0 else 0) * a[1] + d[2] - Q(1, 2)
    return ReviewProblem(scen, [[0, 1]] * 3, obs, G)


def instance_B():
    """K = 2, blind first stage, the second stage observes the whole path"""
    scen = [(d, Q(1, 4)) for d in itertools.product((-1, 1), repeat=2)]

    def obs(k, w, prefix):
        return "blind" if k == 0 else w

    def G(d, a):
        return a[0] * d[0] + a[1] * d[1] - Q(1, 4) * abs(a[0])
    return ReviewProblem(scen, [[-1, 0, 1]] * 2, obs, G)


def instance_C(fine):
    """refinement: Omega = {-1,1}^3; first observation sign(d1) (coarse) or
    (sign d1, sign d2) (fine); second observation the whole path"""
    scen = [(d, Q(1, 8)) for d in itertools.product((-1, 1), repeat=3)]

    def obs(k, w, prefix):
        if k == 0:
            return w[:2] if fine else w[:1]
        return w

    def G(d, a):
        return a[0] * (1 if (d[0] > 0 and d[1] > 0) else -1) + a[1] * d[2]
    return ReviewProblem(scen, [[0, 1]] * 2, obs, G)


def matching_instance(partition):
    """hidden x in {1,2,3} uniform, one action a in {1,2,3} per observed block,
    margin -|x - a|"""
    scen = [(x, Q(1, 3)) for x in (1, 2, 3)]
    block = {}
    for i, B in enumerate(partition):
        for x in B:
            block[x] = i

    def obs(k, w, prefix):
        return block[w]

    def G(x, a):
        return -abs(x - a[0])
    return ReviewProblem(scen, [[1, 2, 3]], obs, G)


def posterior_only_instance():
    """blind first action a1 in {0,1}; then a fair bit s is revealed; terminal
    reward 1[a1 = s]; second stage has a single dummy action"""
    scen = [(0, Q(1, 2)), (1, Q(1, 2))]

    def obs(k, w, prefix):
        return "blind" if k == 0 else w

    def G(s, a):
        return 1 if a[0] == s else 0
    return ReviewProblem(scen, [[0, 1], [0]], obs, G)


# ------------------------------------------------- coupling class on the two-window instance
def coupling_polytope_vertices():
    """couplings mu on {+-1}^3 with uniform coordinate marginals: vertices
    of {mu >= 0, sum = 1, P(s=1) = P(d1=1) = P(d2=1) = 1/2}"""
    scen = list(itertools.product((1, -1), (-1, 1), (-1, 1)))
    eqs = [([1] * 8, Q(1))]
    for coord, val in ((0, 1), (1, 1), (2, 1)):
        eqs.append(([1 if w[coord] == val else 0 for w in scen], Q(1, 2)))
    verts = set()
    for zeros in itertools.combinations(range(8), 4):
        A = [row for row, _ in eqs]
        b = [c for _, c in eqs]
        for z in zeros:
            e = [0] * 8
            e[z] = 1
            A.append(e)
            b.append(Q(0))
        x = solve_linear(A, b)
        if x is not None and all(v >= 0 for v in x):
            verts.add(tuple(x))
    return scen, sorted(verts)


def coupling_vertices_bfs():
    """cross-check: basic feasible solutions of {mu >= 0, A mu = b} by support
    enumeration (supports of size <= rank = 4 with independent columns)"""
    scen = list(itertools.product((1, -1), (-1, 1), (-1, 1)))
    A = [[Q(1)] * 8]
    b = [Q(1)]
    for coord in range(3):
        A.append([Q(1) if w[coord] == 1 else Q(0) for w in scen])
        b.append(Q(1, 2))
    verts = set()
    for size in range(1, 5):
        for supp in itertools.combinations(range(8), size):
            # solve the 4 x size system in least-squares-free exact way: pick 'size'
            # independent equations via Gaussian elimination on the augmented matrix
            M = [[A[r][j] for j in supp] + [b[r]] for r in range(4)]
            # row reduce
            rows, cols = 4, size
            piv_cols, r = [], 0
            for c in range(cols):
                p = next((i for i in range(r, rows) if M[i][c] != 0), None)
                if p is None:
                    continue
                M[r], M[p] = M[p], M[r]
                pv = M[r][c]
                M[r] = [x / pv for x in M[r]]
                for i in range(rows):
                    if i != r and M[i][c] != 0:
                        f = M[i][c]
                        M[i] = [x - f * y for x, y in zip(M[i], M[r])]
                piv_cols.append(c)
                r += 1
            if len(piv_cols) < cols:
                continue                                  # dependent columns
            if any(all(x == 0 for x in M[i][:cols]) and M[i][cols] != 0 for i in range(rows)):
                continue                                  # inconsistent
            x = [Q(0)] * cols
            for i, c in enumerate(piv_cols):
                x[c] = M[i][cols]
            if all(v >= 0 for v in x):
                mu = [Q(0)] * 8
                for j, c in enumerate(supp):
                    mu[c] = x[j]
                verts.add(tuple(mu))
    return sorted(verts)


def robust_values_two_window(z0=Q(2), den=10**6):
    """Robust values over the coupling class M (uniform coordinate marginals)
    of the two-window instance.
      upper  R+ = min_{mu in M} max_pi E_mu G^pi   (the adversary chooses the
                  coupling after seeing the policy class),
      lower  R- = max_pi min_{mu in M} E_mu G^pi   (one policy against all couplings).
    R- is exact by vertex enumeration of M.  R+ is proposed by HiGHS and then
    certified exactly on both sides: a rational mu* in M with
    max_pi <mu*, G^pi> = R+ and a rational mixture w* over policies with
    min over the vertices of M of <mu, sum_pi w_pi G^pi> = R+.
    Returns dict(upper, lower, mu_star, w_star (sparse), n_policies, certified)."""
    import numpy as np
    from scipy.optimize import linprog
    P = two_window(z0)
    scen, verts = coupling_polytope_vertices()
    pols = list(P.policies())
    table = [[Q(P.G(w, P.run(pol, w))) for w in scen] for pol in pols]
    lower = max(min(sum(m * g for m, g in zip(mu, row)) for mu in verts) for row in table)
    npol = len(pols)
    A_ub = np.array([[float(g) for g in row] + [-1.0] for row in table])
    b_ub = np.zeros(npol)
    A_eq = [[1.0] * 8 + [0.0]]
    b_eq = [1.0]
    for coord in range(3):
        A_eq.append([1.0 if w[coord] == 1 else 0.0 for w in scen] + [0.0])
        b_eq.append(0.5)
    res = linprog(c=[0.0] * 8 + [1.0], A_ub=A_ub, b_ub=b_ub, A_eq=np.array(A_eq), b_eq=np.array(b_eq),
                  bounds=[(0, None)] * 8 + [(None, None)], method="highs")
    assert res.status == 0
    mu_star = tuple(Q(x).limit_denominator(den) for x in res.x[:8])
    in_M = (sum(mu_star) == 1 and all(x >= 0 for x in mu_star) and
            all(sum(x for x, w in zip(mu_star, scen) if w[c] == 1) == Q(1, 2) for c in range(3)))
    upper_from_mu = max(sum(m * g for m, g in zip(mu_star, row)) for row in table)
    duals = -res.ineqlin.marginals
    w = [Q(float(x)).limit_denominator(den) for x in duals]
    s = sum(w)
    w = [x / s for x in w] if s != 0 else w
    mix = [sum(wp * row[j] for wp, row in zip(w, table)) for j in range(8)]
    lower_from_w = min(sum(m * g for m, g in zip(mu, mix)) for mu in verts)
    certified = in_M and (upper_from_mu == lower_from_w)
    return dict(upper=upper_from_mu, lower=lower, mu_star=dict(zip(scen, mu_star)),
                w_star={i: x for i, x in enumerate(w) if x != 0}, n_policies=npol,
                certified=certified, lp_value=res.fun, lower_from_w=lower_from_w,
                mix=dict(zip(scen, mix)))


# ================================================= the three-branch integrated certificate
N3 = [(Q(1), Q(0)), (Q(-3, 5), Q(4, 5)), (Q(-3, 5), Q(-4, 5))]
HEX_VERTS = N3 + [(-v[0], -v[1]) for v in N3]
LAM3 = [Q(3, 8), Q(5, 16), Q(5, 16)]
PPOS3 = Q(34, 25)


def h_hex(g):
    return max(dot(g, w) for w in HEX_VERTS)


def gamma_h(tau, lam=LAM3, support=h_hex):
    """integrated certificate Gamma_h(tau) with horizon T = tau + 1:
    sum lam_l beta_l + int_0^tau (T-s) h_U(-sum lam_l n_l) ds
                     + sum_l lam_l int_tau^T (T-s) h_U(-n_l) ds,
    beta_l = 2 - 34/25 - T (free drift at unit speed)."""
    T = tau + 1
    beta = 2 - PPOS3 - T
    pooled_n = tuple(sum(l * n[i] for l, n in zip(lam, N3)) for i in range(2))
    window = support(tuple(-x for x in pooled_n)) * (T * tau - tau * tau / 2)
    post = sum(l * support(tuple(-x for x in n)) * Q(1, 2) for l, n in zip(lam, N3))
    return sum(lam) * beta + window + post


def gamma_h_wrong_sign(tau, lam=LAM3, support=h_hex):
    T = tau + 1
    beta = 2 - PPOS3 - T
    pooled_n = tuple(sum(l * n[i] for l, n in zip(lam, N3)) for i in range(2))
    window = support(pooled_n) * (T * tau - tau * tau / 2)
    post = sum(l * support(n) * Q(1, 2) for l, n in zip(lam, N3))
    return sum(lam) * beta + window + post


if __name__ == "__main__":
    # smoke tests
    U = Polytope.box(0, 1, 1)
    print("two-floor:", lower_value([((Q(-1),), Q(2, 5)), ((Q(1),), Q(-3, 5))], U))
    print("contrast :", lower_value([((Q(-1),), Q(2, 5)), ((Q(1),), Q(-1, 5))], U))
    for k in (1, 2, 3, 4):
        rows = tight_rows(k)
        Uk = Polytope.box(0, k, k)
        print("tight", k, lower_value(rows, Uk)[0], all(feasible([rows[i] for i in s], Uk) for s in itertools.combinations(range(k + 1), k)))
    print("bench caps(6):", bench_caps(Q(6)), "margin(6):", lower_value(bench_rows(Q(6)), bench_U()), "formula", bench_margin_formula(Q(6)))
    print("Ystar(2) =", bench_Ystar(Q(2)))
    P = two_window()
    print("two-window root:", P.root_value()[0], "policies:", P.count_policies())
    print("gamma_h(1/5) =", gamma_h(Q(1, 5)))

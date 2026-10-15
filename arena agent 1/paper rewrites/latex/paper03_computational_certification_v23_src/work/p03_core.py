"""Exact machinery for the three-branch delayed-observation instance of
paper03 (computational certification), v23.

Everything is in exact rational arithmetic (fractions.Fraction) except the
optional HiGHS solve, whose floating-point optimum is compared against the
exact value only.  The module builds the finite program (5) of the paper for
an arbitrary mesh aligned with the observation times and for an arbitrary
refining information schedule, evaluates the mesh-independent primal/dual
witness pair, prices information splits through the erosion identity, and
evaluates the shared-authority ladder.
"""
from fractions import Fraction as Q
from math import isqrt
import itertools

# ---------------------------------------------------------------- plant data
T = Q(6, 5)
TAU = Q(1, 5)
PPOS = Q(34, 25)            # initial critical position along n_j
BPOS = Q(2)                 # position facets n_i . p <= 2
BVEL = Q(6, 5)              # |v_1|, |v_2| <= 6/5
n = [(Q(1), Q(0)), (Q(-3, 5), Q(4, 5)), (Q(-3, 5), Q(-4, 5))]
# hexagon U = conv{+-n_j} = {|u2| <= 4/5, |2u1 + u2| <= 2, |2u1 - u2| <= 2}
Fm = [(Q(0), Q(1)), (Q(0), Q(-1)), (Q(2), Q(1)), (Q(2), Q(-1)), (Q(-2), Q(1)), (Q(-2), Q(-1))]
fv = [Q(4, 5), Q(4, 5), Q(2), Q(2), Q(2), Q(2)]
VERTS = [n[0], n[1], n[2], (-n[0][0], -n[0][1]), (-n[1][0], -n[1][1]), (-n[2][0], -n[2][1])]
LAM = [Q(3, 8), Q(5, 16), Q(5, 16)]
ETA = [(Q(0), Q(0), Q(0), Q(0), Q(1, 4), Q(1, 4)),
       (Q(0), Q(1, 2), Q(0), Q(3, 10), Q(0), Q(0)),
       (Q(1, 2), Q(0), Q(3, 10), Q(0), Q(0), Q(0))]
# facets: 0,1,2 position (n_i . p <= 2); 3: v1<=6/5, 4: -v1<=6/5, 5: v2<=6/5, 6: -v2<=6/5
FACETS = 7


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1]


def in_U(v):
    return all(dot(Fm[r], v) <= fv[r] for r in range(6))


def h_U(g):
    """support function of the hexagon"""
    return max(dot(g, w) for w in VERTS)


def phi_U(g):
    """phi_U(g) = min_{v in U} g.v = -h_U(-g)"""
    return min(dot(g, w) for w in VERTS)


# -------------------------------------------------------- trajectories (exact)
def critical_peak(legs, j, horizon=T):
    """Critical coordinate of branch j under a list of control legs
    [(duration, u), ...] followed by u=0; returns (peak over [0,horizon],
    list of (t, position, velocity) breakpoints).  Exact: position is
    quadratic on each leg, so the peak is at a leg endpoint or at the interior
    stationary point."""
    c, w, t = PPOS, Q(1), Q(0)
    peak = c
    pts = [(t, c, w)]
    for dur, u in legs + [(horizon - sum(d for d, _ in legs), (Q(0), Q(0)))]:
        if dur <= 0:
            continue
        a = dot(n[j], u)
        # position c + w s + a s^2/2 on [0,dur]
        cand = [c + w * dur + a * dur * dur / 2]
        if a < 0 and 0 < -w / a < dur:
            s = -w / a
            cand.append(c + w * s + a * s * s / 2)
        peak = max([peak] + cand)
        c, w, t = cand[0], w + a * dur, t + dur
        pts.append((t, c, w))
    return peak, pts


def facet_values(legs, j, horizon=T, step=Q(1, 400)):
    """Max over a fine rational time grid of all seven facet functions along
    branch j (p, v in R^2) under the legs; used only as a cross-check of the
    closed-form arguments (the closed forms are proved in the text)."""
    p = (PPOS * n[j][0], PPOS * n[j][1])
    v = (n[j][0], n[j][1])
    t = Q(0)
    worst = [-Q(10)] * FACETS
    schedule = legs + [(horizon - sum(d for d, _ in legs), (Q(0), Q(0)))]
    for dur, u in schedule:
        if dur <= 0:
            continue
        k = 0
        while True:
            s = min(step * k, dur)
            pp = (p[0] + v[0] * s + u[0] * s * s / 2, p[1] + v[1] * s + u[1] * s * s / 2)
            vv = (v[0] + u[0] * s, v[1] + u[1] * s)
            vals = [dot(n[i], pp) - BPOS for i in range(3)] + [vv[0] - BVEL, -vv[0] - BVEL, vv[1] - BVEL, -vv[1] - BVEL]
            worst = [max(a, b) for a, b in zip(worst, vals)]
            if s >= dur:
                break
            k += 1
        p = (p[0] + v[0] * dur + u[0] * dur * dur / 2, p[1] + v[1] * dur + u[1] * dur * dur / 2)
        v = (v[0] + u[0] * dur, v[1] + u[1] * dur)
        t += dur
    return worst


# ------------------------------------------------------------- the finite LP
def build_lp(mesh, info, modes=(0, 1, 2)):
    """mesh: sorted list of Fractions (0 = mesh[0], T = mesh[-1]); every time in
    `info` must be a mesh point.  info: list of (time, partition) with
    partitions refining in time; partition = list of frozensets of modes.
    Returns dict with blocks [(J_index, cell)], rows [(coef{block: (cx,cy)},
    beta, ebar, label)], and the mesh.
    """
    assert mesh[0] == 0 and mesh[-1] == T
    times = [t for t, _ in info]
    assert all(t in mesh for t in times)
    intervals = list(zip(mesh[:-1], mesh[1:]))

    def partition_at(b0):
        part = info[0][1]
        for t, p in info:
            if t <= b0:
                part = p
        return part

    blocks = []
    for k, (b0, b1) in enumerate(intervals):
        for C in partition_at(b0):
            blocks.append((k, C))
    bidx = {bl: i for i, bl in enumerate(blocks)}
    rows = []
    for j in modes:
        for i in range(FACETS):
            for tg in mesh:
                coef = {}
                e = Q(0)
                if i < 3:
                    beta = BPOS - (PPOS + tg) * dot(n[i], n[j])
                else:
                    comp = 0 if i in (3, 4) else 1
                    sgn = Q(1) if i in (3, 5) else Q(-1)
                    beta = BVEL - sgn * n[j][comp]
                for (k, C) in blocks:
                    if j not in C:
                        continue
                    b0, b1 = intervals[k]
                    if b0 >= tg:
                        continue
                    ell = b1 - b0
                    assert b1 <= tg  # labels at mesh points: no partial blocks
                    if i < 3:
                        alpha = (tg - b0) * ell - ell * ell / 2
                        coef[bidx[(k, C)]] = (n[i][0] * alpha, n[i][1] * alpha)
                        e += ell * ell / 4          # affine kernel, h_U(+-n_i) = 1
                    else:
                        cx, cy = coef.get(bidx[(k, C)], (Q(0), Q(0)))
                        lst = [cx, cy]
                        lst[comp] += sgn * ell
                        coef[bidx[(k, C)]] = (lst[0], lst[1])
                rows.append((coef, beta, e, (j, i, tg)))
    return {"mesh": mesh, "intervals": intervals, "blocks": blocks, "bidx": bidx, "rows": rows}


def lp_dimensions(lp):
    Qb = len(lp["blocks"])
    return {"Q": Qb, "variables": 2 * Qb + 1, "rows": len(lp["rows"]) + 6 * Qb}


def row_value(lp, coef, v):
    return sum(cx * v[b][0] + cy * v[b][1] for b, (cx, cy) in coef.items())


def primal_value(lp, v):
    """max_a (A_a v - beta_a - ebar_a) for a block assignment v (dict block->(x,y));
    asserts actuator feasibility."""
    for b in range(len(lp["blocks"])):
        assert in_U(v[b]), "block value outside U"
    return max(row_value(lp, coef, v) - beta - e for coef, beta, e, _ in lp["rows"])


def witness_primal(lp):
    """pre-observation blocks 0; post blocks of cell {j} at -n_j (standard instance)."""
    v = {}
    for b, (k, C) in enumerate(lp["blocks"]):
        if len(C) == 1:
            (j,) = tuple(C)
            v[b] = (-n[j][0], -n[j][1])
        else:
            v[b] = (Q(0), Q(0))
    return v


def witness_dual(lp):
    """lambda on the three endpoint critical rows; mu_{J,j} = lambda_j a_J eta_j on
    post blocks.  Returns (objective, stationarity_ok)."""
    rows = lp["rows"]
    lam_rows = {}
    for idx, (coef, beta, e, lab) in enumerate(rows):
        j, i, tg = lab
        if i == j and tg == T:
            lam_rows[idx] = LAM[j]
    assert len(lam_rows) == 3
    # stationarity: sum_a lam_a A_a[block] + F^T mu[block] = 0 for every block
    grad = {b: [Q(0), Q(0)] for b in range(len(lp["blocks"]))}
    for idx, w in lam_rows.items():
        coef = rows[idx][0]
        for b, (cx, cy) in coef.items():
            grad[b][0] += w * cx
            grad[b][1] += w * cy
    mu_obj = Q(0)
    ok = True
    for b, (k, C) in enumerate(lp["blocks"]):
        b0, b1 = lp["intervals"][k]
        if len(C) == 1:
            (j,) = tuple(C)
            aJ = (T - b0) ** 2 / 2 - (T - b1) ** 2 / 2
            mu = [LAM[j] * aJ * ETA[j][r] for r in range(6)]
            mu_obj += sum(mu[r] * fv[r] for r in range(6))
            ftm = [sum(mu[r] * Fm[r][d] for r in range(6)) for d in (0, 1)]
            if grad[b][0] + ftm[0] != 0 or grad[b][1] + ftm[1] != 0:
                ok = False
        else:
            if grad[b][0] != 0 or grad[b][1] != 0:
                ok = False
    obj = -sum(w * (rows[idx][1] + rows[idx][2]) for idx, w in lam_rows.items()) - mu_obj
    return obj, ok


def mesh_law(mesh):
    return Q(3, 50) - sum((b1 - b0) ** 2 for b0, b1 in zip(mesh[:-1], mesh[1:])) / 4


def solve_highs(lp):
    """Solve the finite program with scipy/HiGHS (dual simplex). Returns
    (rho, iterations, seconds) or None if scipy is unavailable."""
    try:
        import numpy as np
        from scipy.optimize import linprog
        import time
    except Exception:
        return None
    nb = len(lp["blocks"])
    nv = 2 * nb + 1
    A, bvec = [], []
    for coef, beta, e, _ in lp["rows"]:
        r = np.zeros(nv)
        for b, (cx, cy) in coef.items():
            r[2 * b] = float(cx)
            r[2 * b + 1] = float(cy)
        r[-1] = -1.0
        A.append(r)
        bvec.append(float(beta + e))
    for b in range(nb):
        for k in range(6):
            r = np.zeros(nv)
            r[2 * b] = float(Fm[k][0])
            r[2 * b + 1] = float(Fm[k][1])
            A.append(r)
            bvec.append(float(fv[k]))
    c = np.zeros(nv)
    c[-1] = 1.0
    bounds = [(None, None)] * nv
    t0 = time.perf_counter()
    res = linprog(c, A_ub=np.array(A), b_ub=np.array(bvec), bounds=bounds, method="highs-ds")
    dt = time.perf_counter() - t0
    assert res.status == 0, res.message
    return res.fun, int(res.nit), dt


def uniform_mesh(h):
    K = T / h
    assert K.denominator == 1 and (TAU / h).denominator == 1
    return [h * k for k in range(int(K) + 1)]


def refined_mesh(n_pre, n_post, tau=TAU):
    """pre-window split into n_pre equal blocks, post-window into n_post."""
    pre = [tau * k / n_pre for k in range(n_pre)]
    post = [tau + (T - tau) * k / n_post for k in range(n_post + 1)]
    return pre + post


STD_INFO = [(Q(0), [frozenset({0, 1, 2})]), (TAU, [frozenset({0}), frozenset({1}), frozenset({2})])]


# ---------------------------------------------------- erosion / ladder / roots
def erosion_split(partition, tau=TAU):
    """Erosion (12) of the triple certificate (labels at t* = tau+1, weights
    LAM) when the blind cell {1,2,3} is replaced from time 0 by `partition`:
    integral over [0,tau] of phi_U(sum g) - sum_C phi_U(g_C) with g_C(s) =
    sum_{j in C} lam_j (t*-s) n_j.  Since every g_C is (t*-s) times a fixed
    vector, the integrand is (t*-s) times a constant."""
    tstar = tau + 1
    total = (Q(0), Q(0))
    for j in range(3):
        total = (total[0] + LAM[j] * n[j][0], total[1] + LAM[j] * n[j][1])
    coarse = phi_U(total)
    fine = Q(0)
    for C in partition:
        g = (sum(LAM[j] * n[j][0] for j in C), sum(LAM[j] * n[j][1] for j in C))
        fine += phi_U(g)
    const = coarse - fine                       # >= 0 by superadditivity
    integral = tstar * tau - tau * tau / 2      # int_0^tau (t* - s) ds
    return const * integral


def shared_authority(B):
    """t*(B) = max_{w in U} min_{j in B} (-n_j . w), exact over vertices and
    pairwise equal-projection points on the hexagon's edges."""
    cands = list(VERTS)
    # equal-projection points on edges: solve on each edge segment
    for a, b in itertools.combinations(range(len(VERTS)), 2):
        pa, pb = VERTS[a], VERTS[b]
        for i, j in itertools.combinations(B, 2):
            d = (n[i][0] - n[j][0], n[i][1] - n[j][1])
            da, db = dot(d, pa), dot(d, pb)
            if da != db:
                s = da / (da - db)
                if 0 <= s <= 1:
                    cands.append((pa[0] + s * (pb[0] - pa[0]), pa[1] + s * (pb[1] - pa[1])))
    best, arg = None, None
    for w in cands:
        if not in_U(w):
            continue
        val = min(-dot(n[j], w) for j in B)
        if best is None or val > best:
            best, arg = val, w
    return best, arg


def pair_gamma(t, tau):
    """exact pair dual Gamma_B(tau; s*) = -7/50 + (1-t) tau - t(1-t) tau^2/2"""
    return -Q(7, 50) + (1 - t) * tau - t * (1 - t) * tau * tau / 2


def quad_root_bracket(A, Bc, C, lo, hi, iters=60):
    """smallest root of A x^2 + B x + C in [lo,hi] by exact bisection (sign change)."""
    f = lambda x: A * x * x + Bc * x + C
    assert f(lo) * f(hi) < 0
    for _ in range(iters):
        mid = (lo + hi) / 2
        if f(lo) * f(mid) <= 0:
            hi = mid
        else:
            lo = mid
    return lo, hi


def exact_rank(rows_coef, nvars):
    """rank over Q of the safety-row matrix (Gaussian elimination in Fractions)."""
    M = []
    for coef in rows_coef:
        r = [Q(0)] * nvars
        for b, (cx, cy) in coef.items():
            r[2 * b] = cx
            r[2 * b + 1] = cy
        M.append(r)
    rank = 0
    col = 0
    nrows = len(M)
    while rank < nrows and col < nvars:
        piv = next((i for i in range(rank, nrows) if M[i][col] != 0), None)
        if piv is None:
            col += 1
            continue
        M[rank], M[piv] = M[piv], M[rank]
        pv = M[rank][col]
        M[rank] = [x / pv for x in M[rank]]
        for i in range(nrows):
            if i != rank and M[i][col] != 0:
                fac = M[i][col]
                M[i] = [a - fac * b for a, b in zip(M[i], M[rank])]
        rank += 1
        col += 1
    return rank

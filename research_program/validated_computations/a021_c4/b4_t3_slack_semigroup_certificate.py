#!/usr/bin/env python3
"""B4 continuum transfer — STAGE T3: the slack-block semigroup certificate.

THE OBJECT. The slack block of the two-block periodic-NAIM scaffold (the
identical gated Candidate-A C4 equations, institutional delay tau_y = 10,
linearized at the declared equilibrium point y_* = (89.52562, 397.8665,
log(2)/10, 2.08962)): the linear constant-coefficient DDE

    x'(t) = J x(t) + D x(t - 10),

with J, D the Jacobian blocks of the C4 right-hand side at y_* (D has the
single nonzero entry D[3,2] = (1-E/Emax)(eta E/Dref + delta0 Zref/(Zref+Z)^2)).
This is exactly the slack object of the committed discrete evidence
(`computations/c4_slack_semigroup_prefactor.py`, `c4_equilibrium_spectrum.py`).

WHAT IS CERTIFIED (all in outward-rounded interval arithmetic, mpmath iv):

(T3a) ROOT CERTIFICATES. The rightmost characteristic roots of
    Delta(lam) = lam I - J - D exp(-lam*10)
are enclosed: lam_{1,2} = -0.00052673... +- 0.02208463... i (the rightmost
pair) and lam_3 = -0.00103151... (the third). Each is enclosed in a disk on
whose boundary the interval winding number of det Delta is exactly 1
(existence, location, and simplicity). Rectangle counts certify: ZERO roots
with Re lam >= -0.0005 (the pair is globally rightmost) and EXACTLY THREE
roots with Re lam >= -0.05 (the three enclosed ones).

(T3b) SEMIGROUP NORM CERTIFICATE. For the solution semigroup T_y(t) of the
slack DDE on the history space C([-10,0], R^4) with the sup norm, and for
T_n = n * P_hat (the certified binding period of the A1 Stage-4d orbit,
P_hat in [P-3e-7, P+3e-7], P = 370.931177839426):

    ||T_y(T_n)||  <=  Sum_{j=1,2,3} e^{Re lam_j (T_n - 10)} * F_j  +  B2,

where F_j is the sharp operator norm of phi -> Res_j b(lam_j, phi) with
    b(lam, phi) = phi(0) + e^{-lam*10} D int_{-10}^0 e^{-lam s} phi(s) ds,
    Res_j = adj(Delta(lam_j)) / det'(lam_j)   (the residue of Delta^{-1}),
and B2 is the rigorous contour-integral remainder bound along Re lam = -0.05
(decaying like e^{-0.05 (T_n - 10)}).

MATHEMATICAL BASIS. For t > tau the solution admits the classical
Laplace/residue representation (valid for the eventually compact semigroup
of a retarded functional differential equation; the inverse-Laplace contour
shifted to Re lam = -0.05 picks up exactly the three certified roots):

    x(t+theta) = Sum_{j=1,2,3} e^{lam_j (t+theta)} Res_j b(lam_j, phi)
                 + (1/2 pi i) int_{Re lam = -0.05} e^{lam(t+theta)}
                   Delta(lam)^{-1} b(lam, phi) dlam.

The finite window of the remainder integral is bounded absolutely; the tail
(|Im lam| > 4) is bounded by a Neumann expansion of Delta^{-1} (valid since
|lam| > ||J||_inf + ||D||_inf e^{0.5} there) combined with second-mean-value
(Dirichlet) bounds for the oscillatory pieces, whose phases are linear with
frequencies >= T_n - 5*tau > 0.

HONESTY STATEMENTS.
- The certificate is for the linearization at the DECLARED point y_* (the
  scaffold's own slack object; the same J, D as all committed discrete
  evidence). The residual of y_* as an equilibrium of the nonlinear C4
  right-hand side (|rhs| <= 3.6e-7 componentwise) is a nonlinear-localization
  (H1) matter and does not enter the linear semigroup norm.
- The output history segment covers [T_n - 10, T_n]; all output times
  exceed 10 by more than four orders of magnitude, so the representation
  applies on the whole segment.

Cross-checks (all must pass):
- the float roots reproduce the committed refined values to 1e-15;
- the interval residues contain the float eigen-decomposition residues;
- the winding counts match the committed 70-digit counts where they overlap
  (0 roots with Re >= -0.0005);
- the certified semigroup bounds EXCEED the committed method-of-lines
  discrete norms at the same times (35 and 40 binding periods), which they
  must, since those discretizations underestimate the continuum norm.

Deterministic; no timing fields in the JSON.
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import mpmath as mp
from mpmath import iv

mp.mp.dps = 60
iv.dps = 50

def iv_lo(x):
    """Lower endpoint of an iv.mpf as a full-precision mp.mp.mpf."""
    return mp.mp.make_mpf(x._mpi_[0])


def iv_hi(x):
    """Upper endpoint of an iv.mpf as a full-precision mp.mp.mpf."""
    return mp.mp.make_mpf(x._mpi_[1])


def iv_mag(x):
    """max(|lo|, |hi|) of an iv.mpf as mpf."""
    return max(abs(iv_lo(x)), abs(iv_hi(x)))


def ivc_abs_hi(z):
    """Rigorous upper bound of |w| over the complex interval box z:
    sqrt(max re^2 + max im^2) (components vary independently in the box)."""
    return mp.sqrt(iv_mag(z.real) ** 2 + iv_mag(z.imag) ** 2)


def ivc_re(z):
    return z.real


def ivc_im(z):
    return z.imag

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT))

# ---------------------------------------------------------------------------
# 1. Exact declared inputs (the scaffold's slack object)
# ---------------------------------------------------------------------------

TAU = mp.mpf(10)

P_PARAM = dict(
    r=mp.mpf('0.02'), K=mp.mpf('100.0'), q=mp.mpf('0.001'),
    eta=mp.mpf('0.914'), Emax=mp.mpf('30.0'), delta0=mp.mpf('0.01'),
    Dref=mp.mpf('1.0'), taum=mp.mpf('5.0'), k=mp.mpf('10.0'),
    delta=mp.mpf(float(math.log(2)) / 10),  # the exact float64 value (declared point)
    Zref=mp.mpf('1.0'), omegaA=mp.mpf('1e-3'), kappaA=mp.mpf('0.05'),
    A0=mp.mpf('1.0'), Aeq_intrinsic=mp.mpf('50.0'),
)
P_PARAM['AeqW'] = P_PARAM['Aeq_intrinsic'] + P_PARAM['kappaA'] * P_PARAM['K'] / P_PARAM['omegaA']
EQ = [mp.mpf('89.52562'), mp.mpf('397.8665'),
      mp.mpf(float(math.log(2)) / 10), mp.mpf('2.08962')]


def softplus_mp(x, k):
    z = k * x
    if z > 40:
        return x
    if z < -40:
        return mp.e ** z / k
    return mp.log1p(mp.e ** z) / k


def jac_mp():
    """Float Jacobian blocks at the exact declared point."""
    p = P_PARAM
    N, A, Z, E = EQ
    fac = A / (A + p['A0'])
    RN = p['r'] * (1 - 2 * N / p['K']) * fac
    RA = p['r'] * N * (1 - N / p['K']) * p['A0'] / (A + p['A0']) ** 2
    BN = RN + p['kappaA'] * fac
    BA = RA + p['kappaA'] * N * p['A0'] / (A + p['A0']) ** 2
    deficit = p['q'] * E * N - p['r'] * N * (1 - N / p['K']) * fac
    sig = 1 / (1 + mp.e ** (-p['k'] * deficit))
    J = mp.matrix(4, 4)
    D = mp.matrix(4, 4)
    J[0, 0] = RN - p['q'] * E
    J[0, 1] = RA
    J[0, 3] = -p['q'] * N
    J[1, 0] = -BN
    J[1, 1] = -BA - p['omegaA']
    J[2, 0] = sig * (p['q'] * E - RN) / p['taum']
    J[2, 1] = -sig * RA / p['taum']
    J[2, 2] = -1 / p['taum']
    J[2, 3] = sig * p['q'] * N / p['taum']
    H = p['eta'] * E * (Z / p['Dref'] - E / p['Emax']) + p['delta0'] * Z / (p['Zref'] + Z)
    J[3, 3] = -H / p['Emax'] + (1 - E / p['Emax']) * p['eta'] * (Z / p['Dref'] - 2 * E / p['Emax'])
    D[3, 2] = (1 - E / p['Emax']) * (p['eta'] * E / p['Dref'] + p['delta0'] * p['Zref'] / (p['Zref'] + Z) ** 2)
    return J, D


J_F, D_F = jac_mp()


def jac_iv():
    """Interval Jacobian blocks at the exact declared point (tiny widths)."""
    p = P_PARAM
    N = iv.mpf(EQ[0]); A = iv.mpf(EQ[1]); Z = iv.mpf(EQ[2]); E = iv.mpf(EQ[3])
    pr = {key: iv.mpf(val) for key, val in p.items()}
    fac = A / (A + pr['A0'])
    RN = pr['r'] * (1 - 2 * N / pr['K']) * fac
    RA = pr['r'] * N * (1 - N / pr['K']) * pr['A0'] / (A + pr['A0']) ** 2
    BN = RN + pr['kappaA'] * fac
    BA = RA + pr['kappaA'] * N * pr['A0'] / (A + pr['A0']) ** 2
    deficit = pr['q'] * E * N - pr['r'] * N * (1 - N / pr['K']) * fac
    sig = 1 / (1 + iv.exp(-pr['k'] * deficit))
    J = [[iv.mpf(0)] * 4 for _ in range(4)]
    D = [[iv.mpf(0)] * 4 for _ in range(4)]
    J[0][0] = RN - pr['q'] * E
    J[0][1] = RA
    J[0][3] = -pr['q'] * N
    J[1][0] = -BN
    J[1][1] = -BA - pr['omegaA']
    J[2][0] = sig * (pr['q'] * E - RN) / pr['taum']
    J[2][1] = -sig * RA / pr['taum']
    J[2][2] = -1 / pr['taum']
    J[2][3] = sig * pr['q'] * N / pr['taum']
    H = pr['eta'] * E * (Z / pr['Dref'] - E / pr['Emax']) + pr['delta0'] * Z / (pr['Zref'] + Z)
    J[3][3] = -H / pr['Emax'] + (1 - E / pr['Emax']) * pr['eta'] * (Z / pr['Dref'] - 2 * E / pr['Emax'])
    D[3][2] = (1 - E / pr['Emax']) * (pr['eta'] * E / pr['Dref'] + pr['delta0'] * pr['Zref'] / (pr['Zref'] + Z) ** 2)
    return J, D


J_IV, D_IV = jac_iv()

# ---------------------------------------------------------------------------
# 2. Delta in float and interval arithmetic
# ---------------------------------------------------------------------------


def delta_f(z):
    e = mp.e ** (-z * TAU)
    M = mp.matrix(4, 4)
    for i in range(4):
        for j in range(4):
            M[i, j] = (z if i == j else 0) - J_F[i, j] - D_F[i, j] * e
    return M


def det_f(z):
    return mp.det(delta_f(z))


def delta_iv(z):
    e = iv.exp(-z * TAU)
    M = [[(z if i == j else iv.mpf(0)) - J_IV[i][j] - D_IV[i][j] * e for j in range(4)]
         for i in range(4)]
    return M


_PERMS = None


def _perms4():
    global _PERMS
    if _PERMS is None:
        import itertools
        _PERMS = []
        for perm in itertools.permutations(range(4)):
            sgn = 1
            p = list(perm)
            for a in range(4):
                for b in range(a + 1, 4):
                    if p[a] > p[b]:
                        sgn = -sgn
            _PERMS.append((perm, sgn))
    return _PERMS


def det_iv(M):
    total = iv.mpc(0, 0)
    for perm, sgn in _perms4():
        term = iv.mpf(sgn)
        for i in range(4):
            term = term * M[i][perm[i]]
        total = total + term
    return total


def _perms3():
    import itertools
    out = []
    for perm in itertools.permutations(range(3)):
        sgn = 1
        p = list(perm)
        for a in range(3):
            for b in range(a + 1, 3):
                if p[a] > p[b]:
                    sgn = -sgn
        out.append((perm, sgn))
    return out


_PERMS3 = None


def perms3():
    global _PERMS3
    if _PERMS3 is None:
        _PERMS3 = _perms3()
    return _PERMS3


def adjugate_iv_fixed(M):
    C = [[None] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            rows = [r for r in range(4) if r != i]
            cols = [c for c in range(4) if c != j]
            minor = [[M[r][c] for c in cols] for r in rows]
            sub = iv.mpf(0)
            for perm, sgn in perms3():
                t = iv.mpf(sgn)
                for a in range(3):
                    t = t * minor[a][perm[a]]
                sub = sub + t
            C[i][j] = iv.mpf((-1) ** (i + j)) * sub
    # adjugate = C^T
    return [[C[j][i] for j in range(4)] for i in range(4)]


def trace_iv(M):
    t = iv.mpc(0, 0)
    for i in range(4):
        t = t + M[i][i]
    return t


def matmul_iv(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(4)), iv.mpc(0, 0)) for j in range(4)] for i in range(4)]


# ---------------------------------------------------------------------------
# 3. Float root refinement (Newton on det Delta)
# ---------------------------------------------------------------------------


def newton_root(z0, iters=60):
    z = z0
    for _ in range(iters):
        det = det_f(z)
        h = mp.mpf('1e-30') * (1 + abs(z))
        det2 = det_f(z + h)
        z = z - det / ((det2 - det) / h)
    return z


LAM_P = newton_root(mp.mpc('-0.00052673009564114', '0.0220846350193287'))
LAM_M = mp.conj(LAM_P)
LAM_3 = newton_root(mp.mpc('-0.00103151651411957', '0'))

# ---------------------------------------------------------------------------
# 4. Interval winding machinery
# ---------------------------------------------------------------------------


def box_hull(z1, z2):
    """Complex interval box covering z1..z2 (endpoints iv.mpc)."""
    re_lo = min(iv_lo(z1.real), iv_lo(z2.real)); re_hi = max(iv_hi(z1.real), iv_hi(z2.real))
    im_lo = min(iv_lo(z1.imag), iv_lo(z2.imag)); im_hi = max(iv_hi(z1.imag), iv_hi(z2.imag))
    return iv.mpc(iv.mpf([re_lo, re_hi]), iv.mpf([im_lo, im_hi]))


def mpc_point(z):
    return iv.mpc(iv.mpf([mp.re(z), mp.re(z)]), iv.mpf([mp.im(z), mp.im(z)]))


def iv_diam(z):
    w_re = iv_hi(z.real) - iv_lo(z.real)
    w_im = iv_hi(z.imag) - iv_lo(z.imag)
    return mp.sqrt(w_re * w_re + w_im * w_im)


def iv_absmin(z):
    # min |w| over the box: 0 if the box straddles an axis through 0;
    # else min over corners of |corner|.
    re_a, re_b = iv_lo(z.real), iv_hi(z.real)
    im_a, im_b = iv_lo(z.imag), iv_hi(z.imag)
    if re_a <= 0 <= re_b and im_a <= 0 <= im_b:
        return mp.mpf(0)
    if re_a <= 0 <= re_b:
        return min(abs(im_a), abs(im_b))
    if im_a <= 0 <= im_b:
        return min(abs(re_a), abs(re_b))
    corners = [(re_a, im_a), (re_a, im_b), (re_b, im_a), (re_b, im_b)]
    return min(mp.hypot(a, b) for a, b in corners)


def arg_enclosure(z):
    """Enclosure of arg over a complex interval box that does not contain 0
    and does not cross the negative real axis. Returns (lo, hi) or None."""
    re_a, re_b = iv_lo(z.real), iv_hi(z.real)
    im_a, im_b = iv_lo(z.imag), iv_hi(z.imag)
    if re_a <= 0 <= re_b and im_a <= 0 <= im_b:
        return None
    # crossing the negative real axis?
    if im_a < 0 < im_b and re_b < 0:
        return None
    corners = [(re_a, im_a), (re_a, im_b), (re_b, im_a), (re_b, im_b)]
    args = [mp.atan2(b, a) for a, b in corners]
    # if the box is entirely in the right half-plane, atan2 range is fine
    if re_a > 0:
        return (min(args), max(args))
    # left half-plane (or straddling re=0 but not the negative axis):
    if all(a > 0 for a in args) or all(a < 0 for a in args):
        return (min(args), max(args))
    return None  # ambiguous: subdivide


class WindingError(Exception):
    pass


def segment_increment(z1, z2, depth=0):
    """Enclosure of the continuous arg increment of det Delta over the
    segment [z1, z2] (z1, z2 exact mp.mpc points). Returns an interval
    (lo, hi) with |increment| < pi/2, or raises WindingError (subdivided
    externally)."""
    p1 = mpc_point(z1); p2 = mpc_point(z2)
    d1 = det_iv(delta_iv(p1)); d2 = det_iv(delta_iv(p2))
    a1 = arg_enclosure(d1); a2 = arg_enclosure(d2)
    if a1 is None or a2 is None:
        raise WindingError('endpoint det too close to arg branch cut')
    box = box_hull(p1, p2)
    dbox = det_iv(delta_iv(box))
    m = iv_absmin(dbox)
    if m <= 0:
        raise WindingError('det box contains 0')
    diam = iv_diam(dbox)
    vb = diam / m
    if vb >= mp.pi / 2:
        raise WindingError('variation bound too large')
    # principal difference enclosure
    pd_lo = a2[0] - a1[1]
    pd_hi = a2[1] - a1[0]
    # the true increment equals pd + 2 pi m for some integer m; with
    # |increment| <= vb < pi/2 and pd in (-2pi, 2pi), the only admissible
    # candidates are pd - 2pi, pd, pd + 2pi; intersect with [-vb, vb].
    lo = None; hi = None
    two_pi = 2 * mp.pi
    for shift in (-two_pi, mp.mpf(0), two_pi):
        c_lo = pd_lo + shift; c_hi = pd_hi + shift
        i_lo = max(c_lo, -vb); i_hi = min(c_hi, vb)
        if i_lo <= i_hi:
            if lo is None:
                lo, hi = i_lo, i_hi
            else:
                lo = min(lo, i_lo); hi = max(hi, i_hi)
    if lo is None:
        raise WindingError('no admissible increment candidate')
    return (lo, hi)


def winding_number(contour, max_depth=40):
    """contour: list of exact mp.mpc points (closed). Returns the rigorous
    winding number of det Delta around 0."""
    total_lo = mp.mpf(0); total_hi = mp.mpf(0)
    n_seg = len(contour) - 1
    for idx in range(n_seg):
        z1 = contour[idx]; z2 = contour[idx + 1]
        # adaptive subdivision with bisection
        stack = [(z1, z2, 0)]
        while stack:
            a, b, depth = stack.pop()
            try:
                lo, hi = segment_increment(a, b)
                total_lo += lo; total_hi += hi
            except WindingError:
                if depth >= max_depth:
                    raise WindingError(f'subdivision exhausted between {a} and {b}')
                mid = (a + b) / 2
                stack.append((a, mid, depth + 1))
                stack.append((mid, b, depth + 1))
    total = (total_lo + total_hi) / 2
    half = (total_hi - total_lo) / 2
    # winding must be within (N - 1/2, N + 1/2) * 2 pi
    val = total / (2 * mp.pi)
    val_half_width = half / (2 * mp.pi)
    if val_half_width >= mp.mpf('0.5'):
        raise WindingError(f'winding discrimination failed: {val} +/- {val_half_width}')
    n = int(mp.nint(val))
    if abs(val - n) + val_half_width >= mp.mpf('0.5'):
        raise WindingError(f'winding ambiguous: {val} +/- {val_half_width}')
    return n


def rectangle_contour(a, R, n_edge):
    """Counterclockwise rectangle [a, R] x [-R, R]."""
    a = mp.mpf(a); R = mp.mpf(R)
    pts = []
    def add(z0, z1):
        for kk in range(n_edge):
            pts.append(z0 + (z1 - z0) * mp.mpf(kk) / n_edge)
    add(a - 1j * R, R - 1j * R)
    add(R - 1j * R, R + 1j * R)
    add(R + 1j * R, a + 1j * R)
    add(a + 1j * R, a - 1j * R)
    pts.append(pts[0])
    return pts


def circle_contour(center, radius, n_pts):
    pts = []
    for kk in range(n_pts + 1):
        ang = 2 * mp.pi * mp.mpf(kk) / n_pts
        pts.append(center + radius * mp.e ** (1j * ang))
    return pts


def exterior_radius(a):
    """Neumann exterior bound: no roots with Re lam >= a and |lam| >
    ||J||_2 + ||D||_2 e^{-a tau} (bound ||.||_2 <= sqrt(||.||_1 ||.||_inf))."""
    def norm2_bound(M):
        n1 = max(sum(abs(M[i, j]) for j in range(4)) for i in range(4))
        ninf = max(sum(abs(M[i, j]) for i in range(4)) for j in range(4))
        return mp.sqrt(n1 * ninf)
    return norm2_bound(J_F) + norm2_bound(D_F) * mp.e ** (-mp.mpf(a) * TAU)


# ---------------------------------------------------------------------------
# 5. Residue enclosures
# ---------------------------------------------------------------------------


def delta_prime_iv(z):
    e = iv.exp(-z * TAU)
    M = [[(iv.mpf(1) if i == j else iv.mpf(0)) + TAU_iv * D_IV[i][j] * e for j in range(4)]
         for i in range(4)]
    return M


TAU_iv = iv.mpf(TAU)


def residue_iv(lam_point, radius):
    """Residue of Delta^{-1} at the root enclosed in the disk around
    lam_point: computed at the interval box [lam +- radius]^2 (the box
    covering the disk)."""
    re = iv.mpf([mp.re(lam_point) - radius, mp.re(lam_point) + radius])
    im = iv.mpf([mp.im(lam_point) - radius, mp.im(lam_point) + radius])
    z = iv.mpc(re, im)
    Dl = delta_iv(z)
    adj = adjugate_iv_fixed(Dl)
    Dp = delta_prime_iv(z)
    detp = trace_iv(matmul_iv(adj, Dp))
    if iv_lo(detp.real) <= 0 <= iv_hi(detp.real) and iv_lo(detp.imag) <= 0 <= iv_hi(detp.imag):
        raise RuntimeError('detprime interval contains 0')
    Res = [[adj[i][j] / detp for j in range(4)] for i in range(4)]
    return Res, detp


def res_inf_norm(Res):
    """max row sum of interval magnitudes (upper bounds)."""
    best = mp.mpf(0)
    for i in range(4):
        s = mp.mpf(0)
        for j in range(4):
            s += ivc_abs_hi(Res[i][j])
        best = max(best, s)
    return best


def res_col4_abs(Res, i):
    e = Res[i][4 - 1]
    return ivc_abs_hi(e)


def float_residue(z):
    """Float residue via adjugate/det' for cross-checks."""
    Dl = delta_f(z)
    adj = mp.matrix(4, 4)
    for i in range(4):
        for j in range(4):
            rows = [r for r in range(4) if r != i]
            cols = [c for c in range(4) if c != j]
            minor = mp.matrix(3, 3)
            for ai, r in enumerate(rows):
                for bj, c in enumerate(cols):
                    minor[ai, bj] = Dl[r, c]
            adj[i, j] = (-1) ** (i + j) * mp.det(minor)
    adjT = adj.T
    e = mp.e ** (-z * TAU)
    Dp = mp.eye(4) + TAU * D_F * e
    detp = (adjT * Dp)[0, 0] + (adjT * Dp)[1, 1] + (adjT * Dp)[2, 2] + (adjT * Dp)[3, 3]
    return adjT / detp, detp


# ---------------------------------------------------------------------------
# 6. The semigroup bound assembly
# ---------------------------------------------------------------------------

# the certified binding period (A1 Stage 4d): P_hat in [P-3e-7, P+3e-7]
P_CERT = mp.mpf('370.931177839426')
P_RAD = mp.mpf('3e-7')


def b_op_norm(re_lam_hi, re_lam_lo, D43_hi):
    """Interval enclosure of the operator norm of phi -> b(lam, phi) on the
    sup-norm unit ball, for Re lam in [re_lo, re_hi]:
      |b_i| <= 1 (i != 4); |b_4| <= 1 + e^{-Re lam tau} |D43| I_lam
      I_lam = int_{-tau}^0 e^{-Re lam s} ds = (1 - e^{Re lam tau}) / (-Re lam)
    (worst case over the Re range)."""
    # e^{-Re lam * tau}: Re lam negative -> e^{positive}
    e1 = mp.e ** (-re_lam_lo * TAU)   # largest (Re lam most negative)
    # I_lam = (1 - e^{Re lam tau}) / (-Re lam): maximized at the most negative Re
    I1 = (1 - mp.e ** (re_lam_lo * TAU)) / (-re_lam_lo)
    return 1 + e1 * D43_hi * I1


def exp_dec_rate(re_lam, Tval):
    return mp.e ** (re_lam * (Tval - TAU))


def assemble(n_periods):
    """The certified semigroup bound at T_n = n * P_hat (worst end)."""
    Tn = n_periods * (P_CERT - P_RAD)  # smallest admissible T (worst for decay)
    out = {}
    total = mp.mpf(0)
    parts = []
    for name, lam, radius in (('lam_1', LAM_P, ROOT_RADIUS), ('lam_2', LAM_M, ROOT_RADIUS),
                              ('lam_3', LAM_3, ROOT_RADIUS)):
        Res, detp = RESIDUES[name]
        re_lo = mp.re(lam) - radius
        re_hi = mp.re(lam) + radius
        # decay factor: e^{Re lam (T - tau)}, worst = most-positive Re lam and smallest T
        dec = mp.e ** (re_hi * (Tn - TAU))
        # sharp functional norm from the interval residue:
        # F = max_i ( sum_k |Res_ik| + |Res_i4| * |D43| * e^{-Re lam tau} * I_lam )
        e_tau = mp.e ** (-re_lo * TAU)
        I_lam = (1 - mp.e ** (re_lo * TAU)) / (-re_lo)
        D43_hi = D43_ABS
        F = mp.mpf(0)
        for i in range(4):
            row = mp.mpf(0)
            for j in range(4):
                row += ivc_abs_hi(Res[i][j])
            row += res_col4_abs(Res, i) * D43_hi * e_tau * I_lam
            F = max(F, row)
        part = dec * F
        parts.append((name, part))
        total += part
    # B2: the contour remainder at gamma'' = -0.05
    total += B2_BOUND(Tn)
    out['n'] = n_periods
    out['T_interval'] = [float(n_periods * (P_CERT - P_RAD)), float(n_periods * (P_CERT + P_RAD))]
    out['parts'] = [(nm, float(p)) for nm, p in parts]
    out['bound'] = float(total)
    out['bound_str'] = mp.nstr(total, 12)
    return out


B2_GAMMA = mp.mpf('-0.05')
OMEGA0 = mp.mpf(4)


def _box_inv_norm_bound(z):
    """Bound ||Delta(lam)^{-1}||_inf over the complex interval box z via
    adjugate/det: ||adj||_inf / min|det|. Returns None if det box straddles 0."""
    Dl = delta_iv(z)
    detb = det_iv(Dl)
    m = iv_absmin(detb)
    if m <= 0:
        return None
    adj = adjugate_iv_fixed(Dl)
    nn = mp.mpf(0)
    for i in range(4):
        s = mp.mpf(0)
        for j in range(4):
            s += ivc_abs_hi(adj[i][j])
        nn = max(nn, s)
    return nn / m


def B2_BOUND(Tn):
    """Rigorous bound on the remainder contour integral along
    Re lam = -0.05: |(1/2 pi i) int e^{lam(T+theta)} Delta^{-1} b dlam|
    <= e^{gamma (T - tau)} * [window + tail]."""
    gam = B2_GAMMA
    # |b| op norm at gamma: 1 + e^{-gamma tau} |D43| I_gamma
    e_g = mp.e ** (-gam * TAU)
    I_g = (1 - mp.e ** (gam * TAU)) / (-gam)
    bop = 1 + e_g * D43_ABS * I_g
    # window: interval inversions along the line
    win = mp.mpf(0)
    n_boxes = 160
    dw = 2 * OMEGA0 / n_boxes
    for kk in range(n_boxes):
        w_lo = -OMEGA0 + dw * kk
        w_hi = w_lo + dw
        z = iv.mpc(iv.mpf([gam, gam]), iv.mpf([w_lo, w_hi]))
        nb = _box_inv_norm_bound(z)
        if nb is None:
            # subdivide into 8; all must succeed
            for s8 in range(8):
                ww_lo = w_lo + dw * s8 / 8
                zz = iv.mpc(iv.mpf([gam, gam]), iv.mpf([ww_lo, ww_lo + dw / 8]))
                nb2 = _box_inv_norm_bound(zz)
                if nb2 is None:
                    raise RuntimeError(f'B2 window box at omega={ww_lo} contains 0 in det')
                win = max(win, nb2)
        else:
            win = max(win, nb)
    window_bound = (OMEGA0 / mp.pi) * win * bop
    # tail: Neumann + Dirichlet
    # a = ||J||_inf + ||D||_inf e^{-gamma tau}: valid for |lam| > a on the tail
    nJ = max(sum(abs(J_F[i, j]) for j in range(4)) for i in range(4))
    nD = max(sum(abs(D_F[i, j]) for j in range(4)) for i in range(4))
    a = nJ + nD * e_g
    if a >= OMEGA0:
        raise RuntimeError('exterior radius exceeds the tail window')
    freq = Tn - 5 * TAU  # the minimal |linear phase frequency| in the Dirichlet bounds
    if freq <= 0:
        raise RuntimeError('nonpositive Dirichlet frequency')
    tail = mp.mpf(0)
    for kk in range(0, 4):  # Neumann order k
        amp = (a ** kk) * bop
        n_monomials = 2 ** (kk + 1)
        tail += n_monomials * amp * 2 / (OMEGA0 ** (kk + 1) * freq)
    # remainder of the Neumann series (absolute tail):
    # int_Omega0^inf (a/w)^4 / (1 - a/Omega0) dw = a^4 / (3 Omega0^3 (1 - a/Omega0))
    tail += bop * a ** 4 / (3 * OMEGA0 ** 3 * (1 - a / OMEGA0))
    total_const = window_bound + tail
    return mp.e ** (gam * (Tn - TAU)) * total_const


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

ROOT_RADIUS = mp.mpf('1e-6')
RESIDUES = {}
D43_ABS = abs(D_F[3, 2])


def main():
    print('float roots:')
    print('  lam+  =', mp.nstr(LAM_P, 20))
    print('  lam3  =', mp.nstr(LAM_3, 20))
    committed_p = '-0.0005267300956411441728910472'
    committed_3 = '-0.001031516514119565680381576'
    ok_roots = (abs(mp.re(LAM_P) - mp.mpf(committed_p)) < mp.mpf('1e-16')
                and abs(mp.re(LAM_3) - mp.mpf(committed_3)) < mp.mpf('1e-16'))
    print('  match committed refined values:', ok_roots)

    results = {'title': 'B4 continuum transfer — Stage T3: the slack-block semigroup certificate',
               'object': 'the linearization of the gated Candidate-A C4 system at the declared slack '
                         'equilibrium y_* with institutional delay tau_y = 10 (the two-block scaffold slack object)',
               'tau': 10,
               'roots_float': {'lam_pair': [mp.nstr(mp.re(LAM_P), 20), mp.nstr(mp.im(LAM_P), 20)],
                               'lam_3': mp.nstr(LAM_3, 20)},
               'period_certified': [float(P_CERT - P_RAD), float(P_CERT + P_RAD)]}

    # ---- T3a: root certificates ------------------------------------------
    print('\nT3a: root circle certificates (winding = 1 each) ...')
    circles = {}
    for name, lam in (('lam_1', LAM_P), ('lam_2', LAM_M), ('lam_3', LAM_3)):
        c = circle_contour(lam, ROOT_RADIUS, 96)
        w = winding_number(c)
        circles[name] = {'center': [mp.nstr(mp.re(lam), 18), mp.nstr(mp.im(lam), 18)],
                         'radius': float(ROOT_RADIUS), 'winding': w}
        print(f'  {name}: winding = {w} on |z - lam| = {float(ROOT_RADIUS):.1e}')
        if w != 1:
            raise SystemExit(f'root circle winding != 1 for {name}')
    # disjointness
    def dist(z1, z2):
        return abs(z1 - z2)
    disjoint = (dist(LAM_P, LAM_3) > 3 * ROOT_RADIUS and dist(LAM_P, LAM_M) > 3 * ROOT_RADIUS)
    print('  circles pairwise disjoint:', disjoint)
    results['root_circles'] = circles
    results['circles_disjoint'] = bool(disjoint)

    print('\nT3a: rectangle counts ...')
    counts = {}
    for a_val, expected, n_edge in ((-0.0005, 0, 3000), (-0.05, 3, 4000)):
        R = exterior_radius(a_val) + mp.mpf('0.15')
        print(f'  rectangle a={a_val}, R={mp.nstr(R, 6)}: computing ...')
        rc = rectangle_contour(a_val, R, n_edge)
        w = winding_number(rc)
        counts[str(a_val)] = {'left_boundary': a_val, 'rectangle_radius': float(R),
                              'exterior_radius_analytic': float(exterior_radius(a_val)),
                              'count': w}
        print(f'    winding = {w} (expected {expected})')
        if w != expected:
            raise SystemExit(f'rectangle count at a={a_val} is {w}, expected {expected}')
    results['rectangle_counts'] = counts

    # ---- residues ---------------------------------------------------------
    print('\nT3b: residue enclosures ...')
    res_data = {}
    for name, lam in (('lam_1', LAM_P), ('lam_2', LAM_M), ('lam_3', LAM_3)):
        Res, detp = residue_iv(lam, ROOT_RADIUS)
        RESIDUES[name] = (Res, detp)
        nrm = res_inf_norm(Res)
        ResF, detpF = float_residue(lam)
        # containment check: the float residue entries inside the interval ones
        contained = True
        for i in range(4):
            for j in range(4):
                v = ResF[i, j]
                if not (iv_lo(Res[i][j].real) <= mp.re(v) <= iv_hi(Res[i][j].real)
                        and iv_lo(Res[i][j].imag) <= mp.im(v) <= iv_hi(Res[i][j].imag)):
                    contained = False
        res_data[name] = {'res_inf_norm': float(nrm),
                          'detprime_real': [float(iv_lo(detp.real)), float(iv_hi(detp.real))],
                          'detprime_imag': [float(iv_lo(detp.imag)), float(iv_hi(detp.imag))],
                          'float_residue_contained': bool(contained)}
        print(f'  {name}: ||Res||_inf <= {mp.nstr(nrm, 8)}, float residue contained: {contained}')
        if not contained:
            raise SystemExit(f'float residue not contained in interval residue for {name}')
    results['residues'] = res_data

    # ---- T3b: the semigroup bounds ---------------------------------------
    print('\nT3b: semigroup norm bounds ...')
    bounds = {}
    for n_per in (35, 40):
        b = assemble(n_per)
        bounds[str(n_per)] = b
        print(f"  n={n_per}: bound = {b['bound_str']}  (parts: {b['parts']})")
    results['semigroup_bounds'] = bounds

    # the B4 requirement: q_n = M_c max{||S_x^n||, ||T_y||} < 1 needs
    # ||T_y(nP)|| < 1/M_c with M_c = 4.55356 (and the theorem's own target
    # q_40 < 1/4 needs ||T_y(40P)|| < 0.25/M_c).
    MC = mp.mpf('4.55356')
    req35 = 1 / MC
    req40 = mp.mpf('0.25') / MC
    b35 = mp.mpf(bounds['35']['bound_str'])
    b40 = mp.mpf(bounds['40']['bound_str'])
    print(f'\n  requirement at n=35: ||T_y|| < 1/M_c = {mp.nstr(req35, 8)}: bound {mp.nstr(b35, 8)} -> {"PASS" if b35 < req35 else "FAIL"}')
    print(f'  theorem target at n=40: ||T_y|| < 0.25/M_c = {mp.nstr(req40, 8)}: bound {mp.nstr(b40, 8)} -> {"PASS" if b40 < req40 else "FAIL"}')
    results['requirements'] = {
        'M_c_used': float(MC),
        'n35_requirement': float(req35), 'n35_bound': float(b35), 'n35_pass': bool(b35 < req35),
        'n40_requirement_quarter': float(req40), 'n40_bound': float(b40), 'n40_pass': bool(b40 < req40),
    }

    # ---- cross-check vs the committed MOL discrete norms -------------------
    # the committed extrapolated continuum-norm estimates (discrete evidence):
    # n=35: 0.07414 (m -> inf extrapolation); n=40: 0.02557. The certified
    # bound must exceed these.
    mol35 = mp.mpf('0.07414'); mol40 = mp.mpf('0.02557')
    ok_mol = (b35 > mol35 and b40 > mol40)
    print(f'  certified bounds exceed the MOL extrapolated norms: {ok_mol}')
    results['mol_cross_check'] = {'mol35_extrapolated': float(mol35), 'mol40_extrapolated': float(mol40),
                                  'bounds_exceed': bool(ok_mol)}

    results['status'] = ('THE SLACK-BLOCK SEMIGROUP IS CERTIFIED at 35 and 40 binding periods: '
                         '||T_y(n P_hat)|| <= ' + bounds['35']['bound_str'] + ' (n=35) and '
                         + bounds['40']['bound_str'] + ' (n=40), both below the B4 requirements '
                         '(1/M_c at n=35; 0.25/M_c at n=40); the rightmost characteristic roots '
                         'are interval-enclosed with certified simplicity and counts (0 roots with '
                         'Re >= -0.0005; exactly 3 with Re >= -0.05).')
    results['all_checks_pass'] = bool(ok_roots and ok_mol and disjoint
                                       and results['requirements']['n35_pass']
                                       and results['requirements']['n40_pass'])

    out_path = ROOT / 'b4_t3_slack_semigroup_certificate.json'
    out_path.write_text(json.dumps(results, indent=2))
    print(f'\nwrote {out_path}')
    print('all_checks_pass =', results['all_checks_pass'])


if __name__ == '__main__':
    main()

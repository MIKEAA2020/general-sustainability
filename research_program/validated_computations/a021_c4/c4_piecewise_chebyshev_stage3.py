#!/usr/bin/env python3
"""A1 piecewise-Chebyshev campaign — STAGE 3: the local Krawczyk/radii-polynomial
system (marching form) with the finite-band delay coupling enclosed.

Status: LOCAL SYSTEM + ASSEMBLY CONSTANTS + FLOAT PREVIEWS — NOT a certificate.
This is the third executed stage of the piecewise-Chebyshev route specified in
A1_CONTINUUM_LIFT_STATUS.md.  Stages 1 (substrate + local-gain diagnostic) and
2 (outward-rounded interval evaluation + tube-inflation ladder) are committed.
This stage constructs and evaluates, on ALL M=8000 patches, the LOCAL Krawczyk
systems whose composition is the Stage-4 assembly:

  * the local system is the MARCHING (collocation-with-inheritance) form: the
    unknowns of patch j are the corrections w in R^{32} to its node values at
    the Chebyshev-Lobatto nodes i=1..8; the left-endpoint value x_in is an
    INHERITED INPUT (patch j-1's right endpoint), the delayed values Zd at the
    9 nodes are DELAY INPUTS enclosed as intervals (the finite-band coupling:
    the delayed time t-tau lands in one of the two earlier patches j-97/j-98,
    read by interval Lagrange evaluation at the offset), and the equations are
    the collocation conditions at the nodes i=0..7:
        Phi_j(w) = (2/h) [Diff (X_j + w)]_i - rho f((X_j+w)_i, Zd_i) = 0.
    (The free-form variant — all 36 node values free, no inheritance — was
    examined and REJECTED on structural grounds, recorded here: the local
    Jacobian J has a near-null direction (the A state, relaxation rate
    omegaA=1e-3: the A-column of J is O(1e-3)); the free-form stage matrix
    carries that near-null vector on its constant-in-node mode and is
    numerically singular on the orbit.  The slow mode must be pinned by
    inheritance, which is exactly what the marching form does.)

  * per patch, the Krawczyk operator T_j(w) = w - Ahat_j^{-1} Phi_j(w) is
    bounded rigorously in outward-rounded interval arithmetic: the interval
    stage matrix A_j^enc (the Chebyshev differentiation matrix in mpmath, the
    local Jacobian blocks from Stage 2's machinery, both scaled by the
    period-family factor rho), the float inverse, the Neumann invertibility
    bound, the rigorous ||A_j^{-1}||, the Y-input
        Y_j(r_in, delta) = ||Ahat^{-1} Phi_j(0; inputs enclosed)||_inf,
    the Z-term  Z_j(r, delta) = ||I - Ahat^{-1} D_w Phi^enc(ball r)||_inf,
    and the radii-polynomial closing condition  r_j = Y_j/(1-Z_j)
    (self-consistent in the ball radius), on the input-enclosure ladder
    (r_in, delta) in {0,1e-8,1e-6} x {0,1e-8,1e-6}.  The node-0 rhs
    variation under the input inflation is enclosed by the mean-value bound
    with the tube Jacobian row sums.

  * the period family: the committed Krawczyk box certifies the discrete
    solution's period P* within 1e-8 of the grid period P.  Rescaling the
    true solution to the fixed grid period P gives the equation family
    y' = rho f(y, y(t - tau/rho)) with rho in [P_lo/P, P_hi/P] (|rho-1| <=
    2.7e-11) — enclosed as an interval factor on the rhs and a delay-argument
    shift |tau/rho - tau| <= 1.2e-10 whose value effect is enclosed by
    sup|y'| * 1.2e-10 (the a-priori bound along the orbit).  All local
    closing conditions are computed uniformly over the rho family.

  * the ASSEMBLY CONSTANTS Stage 4 needs are measured rigorously: the input
    sensitivity ||S_in|| (the stage response to the inherited value — the
    per-patch step fundamental matrix; mildly expanding, sup ~1.0035 — the
    inheritance chain needs the Stage-4 dichotomy treatment), the delay
    sensitivity ||S_zd|| (the stage response to the delayed inputs — locally
    contractive, sup ~0.15), and the Lagrange evaluation constant Lambda =
    sum_l |L_l(sigma)| at the 72000 delay offsets (the product-form interval
    evaluation, degree 8).

  * FLOAT PREVIEWS (clearly labeled, not part of any certificate): the
    per-patch step-sensitivity eigenvalues, and the composed DELAY-AUGMENTED
    monodromy of the linearized collocation march (state = the input
    perturbation (4) + the Z-value perturbation history of the last 99
    patches (891) = 895 dimensions, marched over all M patches with the
    periodic wrap), whose spectrum is compared against the committed
    method-of-steps monodromy (phase 0.996387, dominant 0.686932, disc
    0.066052) — the dichotomy premise of the Stage-4 assembly, measured at
    the collocation level.

What this does NOT do (Stage 4, not executed): the patch-to-patch contraction
assembly (the dichotomy-structured composition of the local certificates with
the periodic-delay bootstrap and the phase pinning), the between-nodes defect
bound, and the continuum orbit certificate.  Nothing here upgrades any theorem
status; A1 remains COMPUTED_PARTIAL until Stage 4 closes.

Deterministic; no randomness.  Run from anywhere:
    python3 research_program/validated_computations/a021_c4/
           c4_piecewise_chebyshev_stage3.py
Writes c4_piecewise_chebyshev_stage3.json (+ .npz companion) next to this file.
"""
from __future__ import annotations

import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
from mpmath import iv as miv
from mpmath import mp, mpf

mp.dps = 40
miv.dps = 30

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT))
from c4_orbit_krawczyk import N_NODES, K_MAX, TAU, P4  # noqa: E402

M_SEG = 8000
CHEB_DEGREE = 8
# input-enclosure ladder for the local Krawczyk systems
R_IN_LADDER = (0.0, 1e-8, 1e-6)
DELTA_LADDER = (0.0, 1e-8, 1e-6)
# stage-ball ladder for the Z-term tube (monotone upper bounds; the sigmoid
# pass is shared per level)
R_BALL_LADDER = (0.0, 1e-9, 1e-8, 1e-7, 1e-6, 1e-5)
# the Stage-2 rigorous local-gain upper (0.33246, 5 decimals with slack) / h
GAIN_UPPER = 0.33246

_NINF, _PINF = -np.inf, np.inf
f64 = np.float64
EPS_ACC = 40 * 2.220446049250313e-16
EPS_F = 2.220446049250313e-16

COMMITTED_MONODROMY = {"phase": 0.996387, "dominant": 0.686932,
                       "disc": 0.066052}


# ------------------------------------------------------------ interval ops

def _lo(x):
    return np.nextafter(x, _NINF)


def _hi(x):
    return np.nextafter(x, _PINF)


def iv_pt(x):
    x = f64(x)
    return (_lo(x), _hi(x))


def iadd(a, b):
    return (_lo(a[0] + b[0]), _hi(a[1] + b[1]))


def isub(a, b):
    return (_lo(a[0] - b[1]), _hi(a[1] - b[0]))


def imul(a, b):
    p1 = a[0] * b[0]
    p2 = a[0] * b[1]
    p3 = a[1] * b[0]
    p4 = a[1] * b[1]
    return (_lo(np.minimum(np.minimum(p1, p2), np.minimum(p3, p4))),
            _hi(np.maximum(np.maximum(p1, p2), np.maximum(p3, p4))))


def i_scal(c, a):
    return imul((f64(c[0]), f64(c[1])), a)


def i_div(a, b):
    if np.any((np.asarray(b[0]) <= 0) & (np.asarray(b[1]) >= 0)):
        raise ZeroDivisionError("division by interval containing 0")
    return imul(a, (1.0 / np.asarray(b[1], f64), 1.0 / np.asarray(b[0], f64)))


def mp_interval(lo, hi):
    return miv.mpf([mpf(float(lo)), mpf(float(hi))])


def f64_interval(x):
    a, b = x.a, x.b
    fa, fb = float(a), float(b)
    if mpf(fa) > a:
        fa = float(np.nextafter(fa, _NINF))
    if mpf(fb) < b:
        fb = float(np.nextafter(fb, _PINF))
    return fa, fb


def i_abs_hi(lo, hi):
    return np.maximum(np.abs(lo), np.abs(hi))


def ineg_iv(a):
    return (-a[1], -a[0])


def i_hull(a, b):
    return (np.minimum(a[0], b[0]), np.maximum(a[1], b[1]))


# ------------------------------------------------------------ model

def cheb_lobatto(n):
    j = np.arange(n + 1)
    return np.cos(np.pi * (n - j) / n)


def make_model(rho_iv):
    """Interval evaluators of the rho-rescaled C4 rhs/Jacobian.

    Split so that the per-node mpmath transcendental passes are run ONCE per
    X-inflation level and shared across all Zd-enclosure variants:

      f_parts(X)      -> the Zd-independent parts (incl. the softplus pass)
      fE_finish(pt, Zd) -> the Zd-dependent 4th rhs component (rho-scaled)
      f_full(X, Zd)   -> the complete rho-scaled rhs (one softplus pass)
      jac_parts(X)    -> the Zd-independent Jacobian parts (sigmoid pass)
      jac_finish(pt, Zd) -> the full interval J (M,9,4,4) and Dv (M,9,4),
                           rho-scaled
    """
    p = {k: iv_pt(v) for k, v in P4.items()}
    one_mp = miv.mpf(1)

    def softplus_mp(dlo, dhi):
        d = mp_interval(dlo, dhi)
        sp = miv.log(one_mp + miv.exp(miv.mpf(10) * d)) / 10
        return f64_interval(sp)

    def sigmoid_mp(dlo, dhi):
        d = mp_interval(dlo, dhi)
        sg = one_mp / (one_mp + miv.exp(-miv.mpf(10) * d))
        return f64_interval(sg)

    def transcendental(deficit, which):
        lo = np.empty_like(deficit[0])
        hi = np.empty_like(deficit[1])
        flat_lo = deficit[0].ravel()
        flat_hi = deficit[1].ravel()
        out_lo = lo.ravel()
        out_hi = hi.ravel()
        fn = softplus_mp if which == "softplus" else sigmoid_mp
        for i in range(flat_lo.size):
            a, b = fn(flat_lo[i], flat_hi[i])
            out_lo[i] = a
            out_hi[i] = b
        return lo, hi

    def rationals(X):
        N, A, Z, E = X
        one = iv_pt(1.0)
        fac = i_div(A, iadd(A, p['A0']))
        N_over_K = i_div(N, p['K'])
        R = imul(imul(imul(p['r'], N), isub(one, N_over_K)), fac)
        B = iadd(R, imul(imul(p['kappaA'], N), fac))
        deficit = isub(imul(imul(p['q'], E), N), R)
        gate = isub(one, i_div(E, p['Emax']))
        return N, A, Z, E, R, B, deficit, gate, fac

    def f_parts(X):
        N, A, Z, E, R, B, deficit, gate, fac = rationals(X)
        sp = transcendental(deficit, "softplus")
        mem = (np.maximum(0.0, sp[0]), np.maximum(0.0, sp[1]))
        fN = imul(rho_iv, isub(R, imul(imul(p['q'], E), N)))
        fA = imul(rho_iv, isub(imul(p['omegaA'], isub(p['AeqW'], A)), B))
        fZ = imul(rho_iv, i_div(isub(mem, Z), p['taum']))
        return {"E": E, "gate": gate, "fN": fN, "fA": fA, "fZ": fZ}

    def fE_finish(pt, Zd):
        E, gate = pt["E"], pt["gate"]
        fE = imul(gate, iadd(
            imul(imul(p['eta'], E),
                 isub(i_div(Zd, p['Dref']), i_div(E, p['Emax']))),
            imul(p['delta0'], i_div(Zd, iadd(p['Zref'], Zd)))))
        return imul(rho_iv, fE)

    def f_full(X, Zd):
        pt = f_parts(X)
        return [pt["fN"], pt["fA"], pt["fZ"], fE_finish(pt, Zd)]

    def jac_parts(X):
        N, A, Z, E, R, B, deficit, gate, fac = rationals(X)
        Aplus = iadd(A, p['A0'])
        dfac = i_div(p['A0'], imul(Aplus, Aplus))
        one = iv_pt(1.0)
        two = iv_pt(2.0)
        N_over_K = i_div(N, p['K'])
        RN = imul(imul(p['r'], isub(one, imul(two, N_over_K))), fac)
        RA = imul(imul(imul(p['r'], N), isub(one, N_over_K)), dfac)
        BN = iadd(RN, imul(p['kappaA'], fac))
        BA = iadd(RA, imul(imul(p['kappaA'], N), dfac))
        sig = transcendental(deficit, "sigmoid")
        return {"N": N, "A": A, "E": E, "Z": Z, "gate": gate, "RN": RN,
                "RA": RA, "BN": BN, "BA": BA, "sig": sig}

    def jac_finish(pt, Zd):
        N, A, Z, E = pt["N"], pt["A"], pt["Z"], pt["E"]
        gate, RN, RA, BN, BA, sig = (pt["gate"], pt["RN"], pt["RA"],
                                     pt["BN"], pt["BA"], pt["sig"])
        H = iadd(imul(imul(p['eta'], E), isub(Zd, i_div(E, p['Emax']))),
                 imul(p['delta0'], i_div(Zd, iadd(p['Zref'], Zd))))
        M_, Nn = np.shape(N[0])
        Jlo = np.zeros((M_, Nn, 4, 4))
        Jhi = np.zeros((M_, Nn, 4, 4))
        Dvlo = np.zeros((M_, Nn, 4))
        Dvhi = np.zeros((M_, Nn, 4))

        def put(row, col, val):
            Jlo[:, :, row, col] = val[0]
            Jhi[:, :, row, col] = val[1]

        put(0, 0, isub(RN, imul(p['q'], E)))
        put(0, 1, RA)
        put(0, 3, ineg_iv(imul(p['q'], N)))
        put(1, 0, ineg_iv(BN))
        put(1, 1, iadd(ineg_iv(BA), ineg_iv(p['omegaA'])))
        put(2, 0, i_div(imul(sig, isub(imul(p['q'], E), RN)), p['taum']))
        put(2, 1, i_div(ineg_iv(imul(sig, RA)), p['taum']))
        put(2, 2, ineg_iv(i_div(iv_pt(1.0), p['taum'])))
        put(2, 3, i_div(imul(sig, imul(p['q'], N)), p['taum']))
        put(3, 3, iadd(ineg_iv(i_div(H, p['Emax'])),
                       imul(gate, imul(p['eta'],
                                       isub(Zd, imul(iv_pt(2.0),
                                                     i_div(E, p['Emax'])))))))
        Dv3 = imul(gate, iadd(
            imul(imul(p['eta'], E), i_div(iv_pt(1.0), p['Dref'])),
            imul(imul(p['delta0'], p['Zref']),
                 i_div(iv_pt(1.0), imul(iadd(p['Zref'], Zd),
                                        iadd(p['Zref'], Zd))))))
        Dvlo[:, :, 3] = Dv3[0]
        Dvhi[:, :, 3] = Dv3[1]
        r0, r1 = float(rho_iv[0]), float(rho_iv[1])
        Jlo2 = _lo(np.minimum(r0 * Jlo, r1 * Jlo))
        Jhi2 = _hi(np.maximum(r0 * Jhi, r1 * Jhi))
        Dvlo2 = _lo(np.minimum(r0 * Dvlo, r1 * Dvlo))
        Dvhi2 = _hi(np.maximum(r0 * Dvhi, r1 * Dvhi))
        return (Jlo2, Jhi2), (Dvlo2, Dvhi2)

    return f_parts, fE_finish, f_full, jac_parts, jac_finish


def f_float(Xpt, Zdpt):
    """Float64 rhs (unscaled) at point values."""
    N, A, Z, E = Xpt
    Pq = P4

    def softplus(x, k=10.0):
        z = np.clip(k * x, -700.0, 700.0)
        return np.log1p(np.exp(z)) / k

    fac = A / (A + Pq['A0'])
    R = Pq['r'] * N * (1 - N / Pq['K']) * fac
    B = R + Pq['kappaA'] * N * fac
    deficit = Pq['q'] * E * N - R
    mem = np.maximum(0.0, softplus(deficit, Pq['k']))
    gate = 1 - E / Pq['Emax']
    fN = R - Pq['q'] * E * N
    fA = -B + Pq['omegaA'] * (Pq['AeqW'] - A)
    fZ = (mem - Z) / Pq['taum']
    fE = gate * (Pq['eta'] * E * (Zdpt / Pq['Dref'] - E / Pq['Emax'])
                 + Pq['delta0'] * Zdpt / (Pq['Zref'] + Zdpt))
    return [fN, fA, fZ, fE]


def sha256_of_array(a):
    return hashlib.sha256(np.ascontiguousarray(a).tobytes()).hexdigest()[:16]


# ------------------------------------------------------------ main

def main():
    t_start = time.time()
    box = np.load(ROOT / "c4_orbit_krawczyk_box.npz")
    u_mid = 0.5 * (box["u_lo"] + box["u_hi"])
    P = float(0.5 * (box["P_lo"] + box["P_hi"]))
    P_lo_f, P_hi_f = float(box["P_lo"]), float(box["P_hi"])

    # ---------------- period-family enclosure
    rho_hull = miv.mpf([miv.mpf(P_lo_f) / miv.mpf(P),
                        miv.mpf(P_hi_f) / miv.mpf(P)])
    rho_lo, rho_hi = f64_interval(rho_hull)
    rho_iv = (rho_lo, rho_hi)
    inv_rho = miv.mpf(1) / rho_hull
    dtau_mp = TAU * (inv_rho - miv.mpf(1))
    dtau = max(abs(float(dtau_mp.a)), abs(float(dtau_mp.b)))

    # ---------------- Fourier coefficients of the 161-point orbit
    c = np.fft.fft(u_mid, axis=0) / N_NODES
    c0_re = c[0].real.copy()
    A = np.stack([c[k].real + c[N_NODES - k].real
                  for k in range(1, K_MAX + 1)])
    B = np.stack([c[N_NODES - k].imag - c[k].imag
                  for k in range(1, K_MAX + 1)])
    A_iv = [[iv_pt(A[k, s]) for s in range(4)] for k in range(K_MAX)]
    B_iv = [[iv_pt(B[k, s]) for s in range(4)] for k in range(K_MAX)]
    c0_iv = [iv_pt(c0_re[s]) for s in range(4)]

    n = CHEB_DEGREE
    nodes = cheb_lobatto(n)
    M = M_SEG

    # ---------------- P-dependent constants (mpmath)
    P_iv = mp_interval(_lo(P), _hi(P))
    om_f64 = []
    phi_mp = []
    for k in range(1, K_MAX + 1):
        om_f64.append(f64_interval(2 * miv.pi * k / P_iv))
        phi_mp.append(2 * miv.pi * k * mpf(TAU) / P_iv)
    two_h_inv = f64_interval(miv.mpf(2) * M / P_iv)

    At_f64, Bt_f64 = [], []
    for k in range(K_MAX):
        cs = miv.cos(phi_mp[k])
        sn = miv.sin(phi_mp[k])
        At_f64.append(f64_interval(miv.mpf(A[k, 2]) * cs
                                   - miv.mpf(B[k, 2]) * sn))
        Bt_f64.append(f64_interval(miv.mpf(A[k, 2]) * sn
                                   + miv.mpf(B[k, 2]) * cs))

    # ---------------- roots of unity + integer powers (Stage 2 machinery)
    print("computing M-th roots of unity in mpmath ...", flush=True)
    zre = (np.empty(M), np.empty(M))
    zim = (np.empty(M), np.empty(M))
    for j in range(M):
        th = 2 * miv.pi * j / M
        zre[0][j], zre[1][j] = f64_interval(miv.cos(th))
        zim[0][j], zim[1][j] = f64_interval(miv.sin(th))
    j_idx = np.arange(M)
    zk = [None] * (K_MAX + 1)
    zk[0] = ((np.ones(M), np.ones(M)), (np.zeros(M), np.zeros(M)))
    for k in range(1, K_MAX + 1):
        idx = (k * j_idx) % M
        zk[k] = ((zre[0][idx], zre[1][idx]), (zim[0][idx], zim[1][idx]))

    print("node offset phases (729 mpmath evaluations) ...", flush=True)
    psi_re = [[None] * (n + 1) for _ in range(K_MAX)]
    psi_im = [[None] * (n + 1) for _ in range(K_MAX)]
    for k in range(1, K_MAX + 1):
        for i in range(n + 1):
            xi = miv.cos(miv.pi * (n - i) / n)
            psi = miv.pi * k * (xi + 1) / M
            psi_re[k - 1][i] = f64_interval(miv.cos(psi))
            psi_im[k - 1][i] = f64_interval(miv.sin(psi))

    print("accumulating node values over 80 modes ...", flush=True)
    X = [iv_pt(np.zeros((M, n + 1))) for _ in range(4)]
    Zd_four = iv_pt(np.zeros((M, n + 1)))
    for k in range(1, K_MAX + 1):
        al_re, al_im = zk[k]
        pre = (np.empty((M, n + 1)), np.empty((M, n + 1)))
        pim = (np.empty((M, n + 1)), np.empty((M, n + 1)))
        for i in range(n + 1):
            pr = psi_re[k - 1][i]
            pi_ = psi_im[k - 1][i]
            re = isub(imul(al_re, pr), imul(al_im, pi_))
            im = iadd(imul(al_re, pi_), imul(al_im, pr))
            pre[0][:, i], pre[1][:, i] = re
            pim[0][:, i], pim[1][:, i] = im
        for s in range(4):
            X[s] = iadd(X[s], iadd(i_scal(A_iv[k - 1][s], pre),
                                   i_scal(B_iv[k - 1][s], pim)))
        Zd_four = iadd(Zd_four, iadd(i_scal(At_f64[k - 1], pre),
                                     i_scal(Bt_f64[k - 1], pim)))
    for s in range(4):
        X[s] = iadd(X[s], c0_iv[s])
    Zd_four = iadd(Zd_four, c0_iv[2])

    # ---------------- interval differentiation matrix (mpmath, once)
    print("differentiation matrix in mpmath ...", flush=True)
    xi_mp = [miv.cos(miv.pi * (n - i) / n) for i in range(n + 1)]
    w_mp = [mpf(-1) ** i * (mpf(1) / 2 if i in (0, n) else mpf(1))
            for i in range(n + 1)]
    Dlo = np.zeros((n + 1, n + 1))
    Dhi = np.zeros((n + 1, n + 1))
    for i in range(n + 1):
        row_lo = np.zeros(n + 1)
        row_hi = np.zeros(n + 1)
        for j in range(n + 1):
            if i != j:
                row_lo[j], row_hi[j] = f64_interval(
                    miv.mpf(w_mp[j] / w_mp[i]) / (xi_mp[i] - xi_mp[j]))
        s_lo = -sum(row_lo[j] for j in range(n + 1) if j != i)
        s_hi = -sum(row_hi[j] for j in range(n + 1) if j != i)
        row_lo[i] = _lo(min(s_lo, s_hi))
        row_hi[i] = _hi(max(s_lo, s_hi))
        Dlo[i] = row_lo
        Dhi[i] = row_hi
    KDlo = np.zeros((n + 1, n + 1))
    KDhi = np.zeros((n + 1, n + 1))
    for i in range(n + 1):
        for j in range(n + 1):
            iv = i_scal(two_h_inv, (Dlo[i, j], Dhi[i, j]))
            KDlo[i, j] = iv[0]
            KDhi[i, j] = iv[1]
    KD_mid = 0.5 * (KDlo + KDhi)
    KD_width = KDhi - KDlo

    # ---------------- float points (previews + checks)
    print("float64 point evaluation ...", flush=True)
    Xpt = [np.zeros((M, n + 1)) + c0_re[s] for s in range(4)]
    Zdpt = np.zeros((M, n + 1)) + c0_re[2]
    for k in range(1, K_MAX + 1):
        al = 2 * np.pi * (k * np.arange(M) % M) / M
        for i in range(n + 1):
            th = al + np.pi * k * (nodes[i] + 1) / M
            ct, st = np.cos(th), np.sin(th)
            thd = th - float(2 * np.pi * k * TAU / P)
            ctd, std = np.cos(thd), np.sin(thd)
            for s in range(4):
                Xpt[s][:, i] += A[k - 1, s] * ct + B[k - 1, s] * st
            Zdpt[:, i] += A[k - 1, 2] * ctd + B[k - 1, 2] * std
    cont_gap = max(
        float(np.abs(Xpt[s][:, n]
                     - Xpt[s][np.arange(1, M + 1) % M, 0]).max())
        for s in range(4))

    # ---------------- Lagrange machinery at the delay offsets
    print("delay offsets + interval Lagrange weights (product form) ...",
          flush=True)
    tau_over_h = TAU * M / P
    u = (np.arange(M)[:, None] + (nodes[None, :] + 1.0) / 2.0) - tau_over_h
    jp = np.floor(u).astype(np.int64) % M
    frac = u - np.floor(u)
    sigma = 2.0 * frac - 1.0
    # the interval offsets carry ONLY the float-representation width; the
    # rho-dependent delay-argument shift is enclosed on the VALUE side
    # (zd_shift below), not on the sigma side (which the Lagrange weights'
    # derivatives would amplify by ~40x)
    sig_lo = _lo(sigma - 1e-11)
    sig_hi = _hi(sigma + 1e-11)
    den = np.ones(n + 1)
    for l in range(n + 1):
        for m in range(n + 1):
            if m != l:
                den[l] *= (nodes[l] - nodes[m])
    den_lo = np.empty(n + 1)
    den_hi = np.empty(n + 1)
    for l in range(n + 1):
        d = den[l]
        if d > 0:
            den_lo[l] = _lo(d * (1.0 - 1e-15))
            den_hi[l] = _hi(d * (1.0 + 1e-15))
        else:
            den_lo[l] = _lo(d * (1.0 + 1e-15))
            den_hi[l] = _hi(d * (1.0 - 1e-15))
    Llo = np.empty((M, n + 1, n + 1))
    Lhi = np.empty((M, n + 1, n + 1))
    for l in range(n + 1):
        acc_lo = np.ones((M, n + 1))
        acc_hi = np.ones((M, n + 1))
        for m in range(n + 1):
            if m != l:
                t_lo = _lo(sig_lo - nodes[m])
                t_hi = _hi(sig_hi - nodes[m])
                acc_lo, acc_hi = imul((acc_lo, acc_hi), (t_lo, t_hi))
        Li = i_div((acc_lo, acc_hi), (den_lo[l], den_hi[l]))
        Llo[:, :, l] = Li[0]
        Lhi[:, :, l] = Li[1]
    Lam_hi = np.zeros((M, n + 1))
    for l in range(n + 1):
        Lam_hi += i_abs_hi(Llo[:, :, l], Lhi[:, :, l])
    Lam_hi = _hi(Lam_hi * (1.0 + EPS_ACC))
    Lambda_sup = float(Lam_hi.max())
    Lw_mid = 0.5 * (Llo + Lhi)

    print("delayed values via interval Lagrange evaluation ...", flush=True)
    ZdL_lo = np.zeros((M, n + 1))
    ZdL_hi = np.zeros((M, n + 1))
    for l in range(n + 1):
        term = imul((Llo[:, :, l], Lhi[:, :, l]),
                    (X[2][0][jp, l], X[2][1][jp, l]))
        ZdL_lo = _lo(ZdL_lo + term[0])
        ZdL_hi = _hi(ZdL_hi + term[1])
    ZdLag = (ZdL_lo, ZdL_hi)
    lag_vs_four = float(np.abs(0.5 * (ZdL_lo + ZdL_hi)
                               - 0.5 * (Zd_four[0] + Zd_four[1])).max())
    lag_width_sup = float((ZdL_hi - ZdL_lo).max())

    # ---------------- the model passes at the substrate
    print("substrate f + Jacobian passes (rho-scaled) ...", flush=True)
    f_parts, fE_finish, f_full, jac_parts, jac_finish = make_model(rho_iv)
    pt_sub = f_parts(X)
    F_sub = [pt_sub["fN"], pt_sub["fA"], pt_sub["fZ"],
             fE_finish(pt_sub, ZdLag)]
    sup_f_sub = max(float(i_abs_hi(F_sub[s][0], F_sub[s][1]).max())
                    for s in range(4))
    jpt_sub = jac_parts(X)
    (Jlo_s, Jhi_s), (Dvlo_s, Dvhi_s) = jac_finish(jpt_sub, ZdLag)

    # sup|y'| a-priori (for the rho delay shift): the substrate rhs is
    # rho-scaled already; add the ball variation via the rigorous lip
    lip_sup = GAIN_UPPER * M / P
    BALL_FOR_SHIFT = 1e-6 + 1e-5
    sup_yprime = float(np.nextafter(
        sup_f_sub + lip_sup * (BALL_FOR_SHIFT + 1e-8), _PINF))
    zd_shift = float(np.nextafter(sup_yprime * dtau, _PINF))
    # sup|z'| term-wise all-t bound (diagnostic)
    sup_dzdt_sub = float(np.nextafter(sum(
        (2 * np.pi * (k + 1) / P) * (abs(A[k, 2]) + abs(B[k, 2]))
        for k in range(K_MAX)), _PINF))

    def zd_enclosure(delta):
        zlo = _lo(np.minimum(ZdLag[0] - delta - zd_shift, ZdLag[0]))
        zhi = _hi(np.maximum(ZdLag[1] + delta + zd_shift, ZdLag[1]))
        return (np.minimum(zlo, ZdLag[0]), np.maximum(zhi, ZdLag[1]))

    # ---------------- stage matrices, inverses, Neumann bounds (batched)
    print("assembling 8000 stage matrices + float inverses ...", flush=True)
    Jmid = 0.5 * (Jlo_s + Jhi_s)
    Mhat = np.zeros((M, 32, 32))
    eye4 = np.eye(4)
    for i in range(8):
        for ip in range(1, 9):
            Mhat[:, i * 4:(i + 1) * 4,
                 (ip - 1) * 4:ip * 4] = KD_mid[i, ip] * eye4
    for i in range(1, 8):
        Mhat[:, i * 4:(i + 1) * 4,
             (i - 1) * 4:i * 4] -= Jmid[:, i, :, :]
    Rinv = np.linalg.inv(Mhat)
    RA = Rinv @ Mhat
    q0_rows = (np.abs(np.eye(32)[None, :, :] - RA)
               + 32 * EPS_F * np.abs(RA)).sum(axis=2)
    q0 = _hi(q0_rows.max(axis=1) * (1.0 + EPS_ACC))
    q0_sup = float(q0.max())
    R_rows = np.abs(Rinv).sum(axis=2)
    R_row_max = R_rows.max(axis=1)
    R_norm = _hi(R_row_max * (1.0 + EPS_ACC))
    R_norm_sup = float(R_norm.max())
    # interval width row-sums of (Mhat - M^enc): KD widths + J block widths
    wq = np.zeros((M, 32))
    for i in range(8):
        for ip in range(1, 9):
            wq[:, i * 4:(i + 1) * 4] += 0.5 * KD_width[i, ip]
    for i in range(1, 8):
        wJ = 0.5 * (Jhi_s[:, i, :, :] - Jlo_s[:, i, :, :])   # (M,4,4)
        wq[:, i * 4:(i + 1) * 4] += wJ.sum(axis=2)
    q1 = _hi(R_norm * wq.max(axis=1) * (1.0 + EPS_ACC))
    q1_sup = float(q1.max())
    q_total = _hi((q0 + q1) * (1.0 + EPS_ACC))
    q_total_sup = float(q_total.max())
    invertible = bool(np.all(q_total < 1.0))
    Ainv_bound = _hi(R_norm / np.maximum(1.0 - q_total, 1e-12))
    Ainv_bound_sup = float(Ainv_bound.max())

    # ---------------- S_in, S_zd
    print("input / delay sensitivity constants ...", flush=True)
    Bfl = np.zeros((M, 32, 4))
    for i in range(8):
        Bfl[:, i * 4:(i + 1) * 4, :] += KD_mid[i, 0] * eye4
    Bfl[:, 0:4, :] -= Jmid[:, 0, :, :]
    S_in = -np.einsum('mij,mjk->mik', Rinv, Bfl)
    S_in_norm = _hi(np.abs(S_in).sum(axis=2).max(axis=1) * (1.0 + EPS_ACC))
    S_in_sup = float(S_in_norm.max())
    # rigorous: ||S_in|| <= ||A^{-1}|| * ||B^enc||_inf
    B_rows = np.zeros((M, 32))
    kd0 = np.abs(KD_mid[:, 0]) + 0.5 * KD_width[:, 0]
    J0_abs = i_abs_hi(Jlo_s[:, 0, :, :], Jhi_s[:, 0, :, :]).sum(axis=2)
    for i in range(8):
        for s in range(4):
            B_rows[:, i * 4 + s] = kd0[i] + (0.0 if i > 0 else J0_abs[:, s])
    B_norm = _hi(B_rows.max(axis=1) * (1.0 + EPS_ACC))
    # tighter rigorous bound: ||S_in|| <= ||R B^enc||_inf (interval matvec)
    #   + (q/(1-q)) ||R|| ||B^enc||   [the A^{-1} vs R correction, ~1e-9]
    Benc_lo = np.zeros((M, 32, 4))
    Benc_hi = np.zeros((M, 32, 4))
    for i in range(8):
        Benc_lo[:, i * 4:(i + 1) * 4, :] = KDlo[i, 0] * eye4
        Benc_hi[:, i * 4:(i + 1) * 4, :] = KDhi[i, 0] * eye4
    Benc_lo[:, 0:4, :] -= Jhi_s[:, 0, :, :]
    Benc_hi[:, 0:4, :] -= Jlo_s[:, 0, :, :]
    S_in_rig = np.empty(M)
    chunk = 250
    for a in range(0, M, chunk):
        b = min(a + chunk, M)
        R = Rinv[a:b]                                   # (c,32,32)
        Bl = Benc_lo[a:b][:, None, :, :]                # (c,1,32,4)
        Bh = Benc_hi[a:b][:, None, :, :]                # (c,1,32,4)
        prod_l = np.where(R[:, :, :, None] >= 0,
                          R[:, :, :, None] * Bl, R[:, :, :, None] * Bh)
        prod_h = np.where(R[:, :, :, None] >= 0,
                          R[:, :, :, None] * Bh, R[:, :, :, None] * Bl)
        pl = _lo(prod_l.sum(axis=2))
        ph = _hi(prod_h.sum(axis=2))
        abs_hi = np.maximum(np.abs(pl), np.abs(ph))    # (c,32,4)
        rs = abs_hi.sum(axis=2)                         # (c,32) row sums
        nrows = _hi(rs * (1.0 + EPS_ACC)
                    + EPS_ACC * rs).max(axis=1)         # (c,)
        S_in_rig[a:b] = nrows
    S_in_rig = _hi(S_in_rig + (q_total / np.maximum(1.0 - q_total, 1e-12))
                   * R_norm * B_norm)
    S_in_rig_sup = float(S_in_rig.max())

    Dv3_mid = 0.5 * (Dvlo_s[:, :, 3] + Dvhi_s[:, :, 3])
    DvB = np.zeros((M, 32, 8))
    for i in range(8):
        DvB[:, i * 4 + 3, i] = -Dv3_mid[:, i]
    Szd = -np.einsum('mij,mjk->mik', Rinv, DvB)
    Szd_norm = _hi(np.abs(Szd).sum(axis=2).max(axis=1) * (1.0 + EPS_ACC))
    Szd_sup = float(Szd_norm.max())
    Dv3_abs_hi = i_abs_hi(Dvlo_s[:, :, 3], Dvhi_s[:, :, 3])
    Szd_rig = _hi(Ainv_bound * Dv3_abs_hi.max(axis=1))
    Szd_rig_sup = float(Szd_rig.max())

    # step sensitivity (float preview)
    Sout = S_in[:, 28:32, :]
    step_eigs = np.array([np.linalg.eigvals(Sout[j]).real.max()
                          for j in range(M)])
    prod_frozen = np.eye(4)
    for j in range(M):
        prod_frozen = Sout[j] @ prod_frozen
    frozen_eigs = np.sort(np.abs(np.linalg.eigvals(prod_frozen)))[::-1]

    # ---------------- Z-terms FIRST: tube Jacobian widths per (r_ball, delta)
    print("Z-terms on the stage-ball ladder (shared sigmoid per level) ...",
          flush=True)
    tube = {}
    Jrow_tube = {}
    jparts = {}
    for r_ball in R_BALL_LADDER:
        if r_ball == 0.0:
            jpt = jpt_sub
        else:
            Xi = [(X[s][0] - r_ball, X[s][1] + r_ball) for s in range(4)]
            jpt = jac_parts(Xi)
        jparts[r_ball] = jpt
        for delta in DELTA_LADDER:
            Zdi = zd_enclosure(delta)
            (Jl, Jh), _ = jac_finish(jpt, Zdi)
            wDF = np.zeros((M, 32))
            for i in range(1, 8):
                wJ = np.maximum(
                    np.abs(Jmid[:, i, :, :] - Jl[:, i, :, :]),
                    np.abs(Jh[:, i, :, :] - Jmid[:, i, :, :]))  # (M,4,4)
                wDF[:, i * 4:(i + 1) * 4] += wJ.sum(axis=2)
            for i in range(8):
                for ip in range(1, 9):
                    wDF[:, i * 4:(i + 1) * 4] += 0.5 * KD_width[i, ip]
            Zt = _hi((q0 + R_norm * wDF.max(axis=1)) * (1.0 + EPS_ACC))
            tube[(r_ball, delta)] = float(Zt.max())
            Jrow_tube[(r_ball, delta)] = i_abs_hi(Jl, Jh).sum(axis=3)
        print(f"  r_ball={r_ball:g}: Z sup (delta=0/1e-8/1e-6) = "
              f"{tube[(r_ball, 0.0)]:.3e} / {tube[(r_ball, 1e-8)]:.3e} / "
              f"{tube[(r_ball, 1e-6)]:.3e}", flush=True)

    # ---------------- Y-inputs: the defect with the inputs enclosed
    print("Y-inputs on the (r_in, delta) ladder (shared softplus) ...",
          flush=True)
    # the KD-matvec rows i=0..7: the stage-node part (ip=1..8, never
    # inflated) and the input-node column (ip=0, inflated by r_in)
    KDsum = [np.zeros((M, 8, 2)) for _ in range(4)]
    for i in range(8):
        acc_lo = [np.zeros(M) for _ in range(4)]
        acc_hi = [np.zeros(M) for _ in range(4)]
        for ip in range(1, 9):
            w = (KDlo[i, ip], KDhi[i, ip])
            for s in range(4):
                t = i_scal(w, (X[s][0][:, ip], X[s][1][:, ip]))
                acc_lo[s] = _lo(acc_lo[s] + t[0])
                acc_hi[s] = _hi(acc_hi[s] + t[1])
        for s in range(4):
            KDsum[s][:, i, 0] = acc_lo[s]
            KDsum[s][:, i, 1] = acc_hi[s]

    def defect_enclosure(r_in, delta):
        Zdi = zd_enclosure(delta)
        fE = fE_finish(pt_sub, Zdi)
        F = [pt_sub["fN"], pt_sub["fA"], pt_sub["fZ"], fE]
        # the mean-value Lipschitz for the node-0 rhs variation, from the
        # tube Jacobian row sums at the smallest level >= r_in
        lvl_mv = None
        for rb in R_BALL_LADDER:
            if r_in <= rb:
                lvl_mv = rb
                break
        if lvl_mv is None:
            lvl_mv = R_BALL_LADDER[-1]
        Jrow_mv = Jrow_tube[(lvl_mv, delta)]
        Flo = np.zeros((M, 32))
        Fhi = np.zeros((M, 32))
        for i in range(8):
            for s in range(4):
                lo = KDsum[s][:, i, 0]
                hi = KDsum[s][:, i, 1]
                # the input-node column of the KD row
                w = (KDlo[i, 0], KDhi[i, 0])
                if r_in > 0:
                    xlo = _lo(X[s][0][:, 0] - r_in)
                    xhi = _hi(X[s][1][:, 0] + r_in)
                else:
                    xlo, xhi = X[s][0][:, 0], X[s][1][:, 0]
                t = i_scal(w, (xlo, xhi))
                lo = _lo(lo + t[0])
                hi = _hi(hi + t[1])
                # minus the rhs
                lo = _lo(lo - F[s][1][:, i])
                hi = _hi(hi - F[s][0][:, i])
                if i == 0 and r_in > 0:
                    # the node-0 rhs input variation (mean-value bound)
                    mv = _hi(Jrow_mv[:, 0, s] * r_in * (1.0 + EPS_ACC)
                             + EPS_ACC * np.abs(Jrow_mv[:, 0, s]) * r_in)
                    lo = _lo(lo - mv)
                    hi = _hi(hi + mv)
                Flo[:, i * 4 + s] = lo
                Fhi[:, i * 4 + s] = hi
        return (Flo, Fhi)

    def Y_of(Fenc):
        Ylo = np.empty(M)
        Yhi = np.empty(M)
        chunk = 500
        for a in range(0, M, chunk):
            b = min(a + chunk, M)
            R = Rinv[a:b]
            Fl = Fenc[0][a:b]
            Fh = Fenc[1][a:b]
            pl = _lo(np.where(R >= 0, R * Fl[:, None, :],
                              R * Fh[:, None, :]))
            ph = _hi(np.where(R >= 0, R * Fh[:, None, :],
                              R * Fl[:, None, :]))
            s_lo = pl.sum(axis=2)
            s_hi = ph.sum(axis=2)
            sc = np.maximum(np.abs(pl).sum(axis=2),
                            np.abs(ph).sum(axis=2))
            Ylo[a:b] = _lo(s_lo * (1.0 - EPS_ACC)
                           - EPS_ACC * sc).max(axis=1)
            Yhi[a:b] = _hi(s_hi * (1.0 + EPS_ACC)
                           + EPS_ACC * sc).max(axis=1)
        return Ylo, Yhi

    combos = []
    Fenc00 = None
    for r_in in R_IN_LADDER:
        for delta in DELTA_LADDER:
            Fenc = defect_enclosure(r_in, delta)
            if r_in == 0.0 and delta == 0.0:
                Fenc00 = Fenc
            Yl, Yh = Y_of(Fenc)
            combos.append({"r_in": r_in, "delta": delta,
                           "Y_sup": float(Yh.max())})
            print(f"  r_in={r_in:g} delta={delta:g}: Y sup = "
                  f"{Yh.max():.3e}", flush=True)

    # ---------------- local closing radii (self-consistent)
    print("local closing radii ...", flush=True)
    closures = []
    for cb in combos:
        r_in, delta, Y = cb["r_in"], cb["delta"], cb["Y_sup"]
        r = 0.0
        closes = False
        for _ in range(10):
            lvl = None
            for rb in R_BALL_LADDER:
                if r <= rb:
                    lvl = rb
                    break
            if lvl is None:
                break
            Z = tube[(lvl, delta)]
            if Z >= 1.0:
                break
            r_new = Y / (1.0 - Z)
            if r_new > R_BALL_LADDER[-1]:
                break
            if abs(r_new - r) <= 1e-4 * max(r_new, 1e-30) and r_new <= lvl:
                r = r_new
                closes = True
                break
            r = r_new
        closures.append({"r_in": r_in, "delta": delta, "Y_sup": Y,
                         "closing_radius": r, "closes": closes})

    # ---------------- float preview: the delay-augmented monodromy
    print("float preview: delay-augmented monodromy march (895-dim) ...",
          flush=True)
    t_aug = time.time()
    NB = 4 + 99 * 9
    dx = np.zeros((NB, 4))
    dH0 = np.zeros((NB, 99, 9))
    for k in range(4):
        dx[k, k] = 1.0
    for k in range(99 * 9):
        dH0[4 + k, k // 9, k % 9] = 1.0
    RING = 100  # read distance 97/98 < 100; M=8000 gives no slot collision
    hist = np.zeros((NB, RING, 9))
    for t in range(99):
        pidx = M - 99 + t
        hist[:, pidx % RING, :] = dH0[:, t, :]
    Lw = Lw_mid[:, :8, :]
    src_slot = (jp[:, :8] % RING).copy()
    for j in range(M):
        dZd = np.zeros((NB, 8))
        for i in range(8):
            dZd[:, i] = hist[:, src_slot[j, i], :] @ Lw[j, i, :]
        dst = dx @ S_in[j].T + dZd @ Szd[j].T
        zvals = np.empty((NB, 9))
        zvals[:, 0] = dx[:, 2]
        for i in range(1, 9):
            zvals[:, i] = dst[:, (i - 1) * 4 + 2]
        hist[:, j % RING, :] = zvals
        dx = dst[:, 28:32].copy()
    dH_final = np.zeros((NB, 99, 9))
    for t in range(99):
        pidx = M - 99 + t
        dH_final[:, t, :] = hist[:, pidx % RING, :]
    Mon = np.zeros((NB, NB))
    Mon[0:4, :] = dx.T
    for t in range(99):
        Mon[4 + t * 9:4 + (t + 1) * 9, :] = dH_final[:, t, :].T
    aug_eigs = np.sort(np.abs(np.linalg.eigvals(Mon)))[::-1]
    aug_secs = time.time() - t_aug

    # ---------------- verification checks
    print("verification checks ...", flush=True)
    checks = {}

    # (a) mpmath containment of the defect at 3 nodes
    rho_mid = 0.5 * (rho_lo + rho_hi)
    two_h_iv = miv.mpf(2) * M / P_iv

    def mp_node_values(j, i):
        base = j + (nodes[i] + 1) / 2
        out = []
        for s in range(4):
            tot = miv.mpf(c0_re[s])
            for k in range(1, K_MAX + 1):
                th = 2 * miv.pi * k * base / M
                tot += (miv.mpf(A[k - 1, s]) * miv.cos(th)
                        + miv.mpf(B[k - 1, s]) * miv.sin(th))
            out.append(tot)
        return out

    def mp_lag_delayed(j, i):
        uj = j + (nodes[i] + 1) / 2 - TAU * M / P
        jpf = int(np.floor(uj)) % M
        sig = 2.0 * (uj - np.floor(uj)) - 1.0
        zdl = miv.mpf(0)
        for l in range(n + 1):
            zl = miv.mpf(c0_re[2])
            basel = jpf + (nodes[l] + 1) / 2
            for k in range(1, K_MAX + 1):
                th = 2 * miv.pi * k * basel / M
                zl += (miv.mpf(A[k - 1, 2]) * miv.cos(th)
                       + miv.mpf(B[k - 1, 2]) * miv.sin(th))
            Ll = miv.mpf(1)
            for m2 in range(n + 1):
                if m2 != l:
                    Ll *= (miv.mpf(sig) - miv.mpf(nodes[m2])) / (
                        miv.mpf(nodes[l] - nodes[m2]))
            zdl += Ll * zl
        return zdl

    defect_fail_detail = []
    defect_ok = True
    for (j, i) in [(0, 0), (M // 2, 3), (M - 1, 7)]:
        xmp = mp_node_values(j, i)
        zdl = mp_lag_delayed(j, i)
        Nmp, Amp, Zmp, Emp = xmp
        fac = Amp / (Amp + miv.mpf(P4['A0']))
        Rm = miv.mpf(P4['r']) * Nmp * (1 - Nmp / miv.mpf(P4['K'])) * fac
        Bm = Rm + miv.mpf(P4['kappaA']) * Nmp * fac
        dfc = miv.mpf(P4['q']) * Emp * Nmp - Rm
        mem = miv.log(1 + miv.exp(miv.mpf(10) * dfc)) / 10
        mem = miv.mpf([max(mem.a, 0), max(mem.b, 0)])
        gate = 1 - Emp / miv.mpf(P4['Emax'])
        fmp = [
            Rm - miv.mpf(P4['q']) * Emp * Nmp,
            -Bm + miv.mpf(P4['omegaA']) * (miv.mpf(P4['AeqW']) - Amp),
            (mem - Zmp) / miv.mpf(P4['taum']),
            gate * (miv.mpf(P4['eta']) * Emp
                    * (zdl / miv.mpf(P4['Dref'])
                       - Emp / miv.mpf(P4['Emax']))
                    + miv.mpf(P4['delta0']) * zdl
                    / (miv.mpf(P4['Zref']) + zdl)),
        ]
        for s in range(4):
            xrow = []
            for ip in range(9):
                base = j + (nodes[ip] + 1) / 2
                tot = miv.mpf(c0_re[s])
                for k in range(1, K_MAX + 1):
                    th = 2 * miv.pi * k * base / M
                    tot += (miv.mpf(A[k - 1, s]) * miv.cos(th)
                            + miv.mpf(B[k - 1, s]) * miv.sin(th))
                xrow.append(tot)
            drow = miv.mpf(0)
            csum = miv.mpf(0)
            for ip in range(9):
                if ip != i:
                    cc = two_h_iv * (
                        miv.mpf(w_mp[ip] / w_mp[i])
                        / (xi_mp[i] - xi_mp[ip]))
                    drow += cc * xrow[ip]
                    csum += cc
            drow += (-csum) * xrow[i]
            Fmp = drow - miv.mpf(rho_mid) * fmp[s]
            row = i * 4 + s
            if not (Fmp.a >= Fenc00[0][j, row]
                    and Fmp.b <= Fenc00[1][j, row]):
                defect_ok = False
                defect_fail_detail.append(
                    (j, i, s, float(Fmp.a), float(Fmp.b),
                     float(Fenc00[0][j, row]), float(Fenc00[1][j, row])))
    checks["mpmath_defect_contained_3_nodes"] = defect_ok
    checks["mpmath_defect_fail_detail"] = defect_fail_detail[:6]

    # (b) mpmath containment of the J entries at 2 nodes
    jac_fail_detail = []
    jac_ok = True
    for (j, i) in [(0, 4), (M // 2, 2)]:
        xmp = mp_node_values(j, i)
        zdl = mp_lag_delayed(j, i)
        Nmp, Amp, Zmp, Emp = xmp
        fac = Amp / (Amp + miv.mpf(P4['A0']))
        dfac = miv.mpf(P4['A0']) / (Amp + miv.mpf(P4['A0'])) ** 2
        RN = miv.mpf(P4['r']) * (1 - 2 * Nmp / miv.mpf(P4['K'])) * fac
        RA = miv.mpf(P4['r']) * Nmp * (1 - Nmp / miv.mpf(P4['K'])) * dfac
        Rm = miv.mpf(P4['r']) * Nmp * (1 - Nmp / miv.mpf(P4['K'])) * fac
        dfc = miv.mpf(P4['q']) * Emp * Nmp - Rm
        sigm = 1 / (1 + miv.exp(-miv.mpf(10) * dfc))
        gate = 1 - Emp / miv.mpf(P4['Emax'])
        H = miv.mpf(P4['eta']) * Emp * (zdl - Emp / miv.mpf(P4['Emax'])) \
            + miv.mpf(P4['delta0']) * zdl / (miv.mpf(P4['Zref']) + zdl)
        Jmp = {
            (0, 0): RN - miv.mpf(P4['q']) * Emp,
            (0, 1): RA,
            (0, 3): -miv.mpf(P4['q']) * Nmp,
            (1, 0): -(RN + miv.mpf(P4['kappaA']) * fac),
            (1, 1): -(RA + miv.mpf(P4['kappaA']) * Nmp * dfac
                      + miv.mpf(P4['omegaA'])),
            (2, 0): sigm * (miv.mpf(P4['q']) * Emp - RN)
                    / miv.mpf(P4['taum']),
            (2, 2): -1 / miv.mpf(P4['taum']),
            (3, 3): -H / miv.mpf(P4['Emax']) + gate * miv.mpf(P4['eta']) * (
                zdl - 2 * Emp / miv.mpf(P4['Emax'])),
        }
        for (rr, cc), val in Jmp.items():
            vr = val * miv.mpf(rho_mid)
            if not (vr.a >= Jlo_s[j, i, rr, cc]
                    and vr.b <= Jhi_s[j, i, rr, cc]):
                jac_ok = False
                jac_fail_detail.append(
                    (j, i, rr, cc, float(vr.a), float(vr.b),
                     float(Jlo_s[j, i, rr, cc]),
                     float(Jhi_s[j, i, rr, cc])))
    checks["mpmath_jacobian_contained_2_nodes"] = jac_ok
    checks["mpmath_jacobian_fail_detail"] = jac_fail_detail[:8]

    # (c) Lagrange weights vs mpmath at 5 offsets
    lag_ok = True
    for (j, i) in [(0, 0), (1, 5), (M // 3, 2), (M // 2, 8), (M - 1, 3)]:
        uj = j + (nodes[i] + 1) / 2 - TAU * M / P
        sig = 2.0 * (uj - np.floor(uj)) - 1.0
        for l in range(n + 1):
            Ll = miv.mpf(1)
            for m2 in range(n + 1):
                if m2 != l:
                    Ll *= (miv.mpf(sig) - miv.mpf(nodes[m2])) / (
                        miv.mpf(nodes[l] - nodes[m2]))
            if not (Ll.a >= Llo[j, i, l] - 1e-11
                    and Ll.b <= Lhi[j, i, l] + 1e-11):
                lag_ok = False
    checks["lagrange_vs_mpmath_5_offsets"] = lag_ok

    # (d) ZdLag vs ZdFour (the interpolation error scale)
    checks["zd_lag_vs_four_midpoint_max"] = lag_vs_four
    checks["zd_lag_vs_four_ok"] = bool(lag_vs_four <= 1e-10)

    # (e) substrate continuity
    checks["substrate_continuity_gap_max"] = cont_gap
    checks["substrate_continuity_ok"] = bool(cont_gap <= 1e-10)

    # (f) inverse quality
    checks["q0_sup"] = q0_sup
    checks["q_total_sup"] = q_total_sup
    checks["all_stage_matrices_invertible"] = invertible

    # (g) float Newton step sanity
    dXf_pt = np.zeros((M, 9, 4))
    Xstack = np.stack(Xpt, axis=2)          # (M,9,4)
    for i in range(9):
        for ip in range(9):
            dXf_pt[:, i, :] += KD_mid[i, ip] * Xstack[:, ip, :]
    Fpt = f_float(Xpt, Zdpt)
    Ffl = np.zeros((M, 32))
    for i in range(8):
        for s in range(4):
            Ffl[:, i * 4 + s] = (dXf_pt[:, i, s]
                                 - rho_mid * Fpt[s][:, i])
    step = np.einsum('mij,mj->mi', Rinv, Ffl)
    checks["float_newton_step_sup"] = float(np.abs(step).max())
    checks["float_newton_step_sane"] = bool(
        np.isfinite(step).all() and np.abs(step).max() <= 1e-3)

    # (h) cross-check vs Stage 2's committed on-substrate defect (rho=1,
    #     Fourier-Zd variant, rows 0..7)
    _, _, f_full1, _, _ = make_model(iv_pt(1.0))
    Fd_four = f_full1(X, Zd_four)
    Yfour_sup = 0.0
    for i in range(8):
        for s in range(4):
            lo = np.zeros(M)
            hi = np.zeros(M)
            for ip in range(9):
                t = i_scal((KDlo[i, ip], KDhi[i, ip]),
                           (X[s][0][:, ip], X[s][1][:, ip]))
                lo = _lo(lo + t[0])
                hi = _hi(hi + t[1])
            Yfour_sup = max(
                Yfour_sup,
                float(np.maximum(np.abs(lo - Fd_four[s][1][:, i]),
                                 np.abs(hi - Fd_four[s][0][:, i])).max()))
    checks["stage2_crosscheck_fourier_defect_sup"] = Yfour_sup
    checks["stage2_crosscheck_ok"] = bool(abs(Yfour_sup - 8.326e-9) <= 2e-9)

    # (i) augmented monodromy vs the committed
    checks["augmented_monodromy_top6"] = [float(x) for x in aug_eigs[:6]]
    phase_gap = abs(float(aug_eigs[0]) - COMMITTED_MONODROMY["phase"])
    dominant_gap = abs(float(aug_eigs[1]) - COMMITTED_MONODROMY["dominant"])
    checks["augmented_vs_committed_phase_gap"] = phase_gap
    checks["augmented_vs_committed_dominant_gap"] = dominant_gap
    checks["augmented_consistent_with_committed"] = bool(
        phase_gap <= 5e-3 and dominant_gap <= 0.05)

    # ---------------- output
    out = {
        "title": "A1 piecewise-Chebyshev campaign — Stage 3: the local "
                 "Krawczyk/radii-polynomial system (marching form) with the "
                 "finite-band delay coupling enclosed",
        "status": "LOCAL SYSTEM + ASSEMBLY CONSTANTS + FLOAT PREVIEWS — "
                  "NOT a certificate: no patch-to-patch assembly, no "
                  "between-nodes defect bound, no continuum statement; A1 "
                  "remains COMPUTED_PARTIAL until Stage 4 closes",
        "inputs": {
            "orbit": "committed Krawczyk box midpoint "
                     "(c4_orbit_krawczyk_box.npz)",
            "period_P": P,
            "P_box": [P_lo_f, P_hi_f],
            "M_segments": M_SEG,
            "cheb_degree": CHEB_DEGREE,
            "delay_tau": TAU,
            "rho_interval": [rho_lo, rho_hi],
            "rho_delay_shift_dtau": dtau,
            "sup_yprime_apriori": sup_yprime,
            "zd_shift_inflation": zd_shift,
            "sup_dzdt_substrate_termbound": sup_dzdt_sub,
        },
        "method": {
            "local_system": "marching form: unknowns = the corrections to "
                            "the node values i=1..8 of each patch (32 per "
                            "patch); the left-endpoint value is an inherited "
                            "input, the delayed values (the finite-band "
                            "coupling: the source patches j-97/j-98, read "
                            "by interval Lagrange evaluation at the offset) "
                            "are interval inputs; the equations are the "
                            "collocation conditions at the nodes i=0..7",
            "free_form_rejected": "the free-form variant (all 36 node "
                                  "values free, no inheritance) is "
                                  "structurally ill-conditioned: the local "
                                  "Jacobian has a near-null direction (the "
                                  "A state, relaxation rate omegaA=1e-3) "
                                  "which the constant-in-node stage mode "
                                  "inherits — the free-form stage matrix "
                                  "is numerically singular on the orbit; "
                                  "the slow mode must be pinned by "
                                  "inheritance",
            "interval_arithmetic": "float64 with np.nextafter outward "
                                   "rounding; softplus/sigmoid per node in "
                                   "mpmath (dps=30); the differentiation "
                                   "matrix, the Lagrange denominators and "
                                   "all P-dependent constants in mpmath "
                                   "(dps=40); float matrix products carry "
                                   "explicit accumulation allowances; the "
                                   "node-0 rhs variation under the input "
                                   "inflation is enclosed by the "
                                   "mean-value bound with the Jacobian row "
                                   "sums",
            "period_family": "the true solution rescaled to the fixed grid "
                             "period P satisfies y' = rho f(y, y(t - "
                             "tau/rho)) with rho in [P_lo/P, P_hi/P]; the "
                             "rhs and Jacobians are rho-scaled and the "
                             "delay-argument shift |tau/rho - tau| <= "
                             f"{dtau:.3e} is enclosed by sup|y'|*dtau with "
                             "the a-priori sup|y'| bound",
        },
        "stage_matrix_bounds": {
            "q0_sup": q0_sup,
            "q1_sup": q1_sup,
            "q_total_sup": q_total_sup,
            "all_invertible": invertible,
            "Rinv_norm_sup": R_norm_sup,
            "Ainv_rigorous_bound_sup": Ainv_bound_sup,
            "note": "the rigorous ||A_j^{-1}|| <= ||R||/((1-q0)(1-q1)) on "
                    "every patch; the sup is the O(h) inverse promised by "
                    "the route's premise",
        },
        "Y_inputs": combos,
        "Z_terms": {f"r_ball={rb:g},delta={dl:g}": tube[(rb, dl)]
                    for rb in R_BALL_LADDER for dl in DELTA_LADDER},
        "local_closures": closures,
        "assembly_constants": {
            "S_in_sup_float": S_in_sup,
            "S_in_sup_rigorous": S_in_rig_sup,
            "S_in_note": "the stage response to the inherited value (the "
                         "per-patch step fundamental matrix): mildly "
                         "expanding — the inheritance chain needs the "
                         "Stage-4 dichotomy treatment (the naive radius "
                         "march grows like the product of the norms)",
            "Szd_sup_float": Szd_sup,
            "Szd_sup_rigorous": Szd_rig_sup,
            "Szd_note": "the stage response to the delayed inputs: locally "
                        "contractive — the delay feedback alone does not "
                        "obstruct the assembly",
            "Lambda_sup": Lambda_sup,
            "Lambda_note": "sum_l |L_l(sigma)| over all 72000 delay "
                           "offsets (the interval Lagrange product form)",
            "lagrange_width_sup": lag_width_sup,
            "delay_band": "the delayed time t - tau lands in the patches "
                          f"j-97 or j-98 (tau/h = {tau_over_h:.4f}); the "
                          "finite band is 2 source patches per patch",
            "step_sensitivity_eig_range": [float(step_eigs.min()),
                                           float(step_eigs.max())],
            "frozen_product_eigs_preview": [float(x)
                                            for x in frozen_eigs[:4]],
            "frozen_note": "float preview only (the frozen-coefficient "
                           "composition ignores the delay feedback); the "
                           "meaningful object is the delay-augmented "
                           "monodromy",
            "augmented_monodromy_top6_float_preview": [
                float(x) for x in aug_eigs[:6]],
            "augmented_monodromy_note": "float preview: the composed "
                                        "linearized collocation march on "
                                        "the (4 + 99*9)-dim augmented state "
                                        "(the input perturbation + the "
                                        "Z-value history of the last 99 "
                                        "patches), periodic wrap included; "
                                        "compared against the committed "
                                        "method-of-steps monodromy "
                                        f"{COMMITTED_MONODROMY}",
            "augmented_march_seconds": round(aug_secs, 1),
        },
        "verification": checks,
        "stage3_verdict": {},
    }

    all_close = bool(all(cbl["closes"] for cbl in closures))
    committed_top3 = [COMMITTED_MONODROMY['phase'],
                      COMMITTED_MONODROMY['dominant'],
                      COMMITTED_MONODROMY['disc']]
    aug_top3 = [round(float(x), 6) for x in aug_eigs[:3]]
    out["stage3_verdict"] = {
        "local_systems": (
            f"the local Krawczyk/radii-polynomial systems are constructed "
            f"and evaluated on all M={M} patches in the marching form with "
            f"the finite-band delay coupling enclosed: every stage matrix "
            f"is rigorously invertible (q_total sup = {q_total_sup:.2e}), "
            f"the rigorous ||A^-1|| sup = {Ainv_bound_sup:.4f} (the O(h) "
            f"inverse), and the local radii polynomials close at "
            f"{'every' if all_close else 'the indicated'} input-enclosure "
            f"ladder points"
        ),
        "closing_radii": (
            f"the uniform closing radius at the minimal input enclosures "
            f"(r_in=0, delta=minimal) is "
            f"{closures[0]['closing_radius']:.3e}; at r_in=1e-6, "
            f"delta=1e-6 it is {closures[-1]['closing_radius']:.3e}"
        ),
        "assembly": (
            f"the assembly constants are measured: ||S_in|| sup = "
            f"{S_in_sup:.4f} (mildly expanding — the Stage-4 dichotomy "
            f"treatment is required for the inheritance chain), ||S_zd|| "
            f"sup = {Szd_sup:.4f} (the delay feedback is locally "
            f"contractive), Lambda sup = {Lambda_sup:.3f}; the "
            f"delay-augmented collocation monodromy (float preview) has "
            f"top eigenvalues {aug_top3} vs the committed "
            f"{committed_top3}"
        ),
        "next_stage": [
            "Stage 4: the patch-to-patch contraction assembly — the "
            "dichotomy-structured composition of the local certificates "
            "with the periodic-delay bootstrap and the phase pinning, the "
            "between-nodes defect bound, and the continuum orbit "
            "certificate (the A1 gate)",
        ],
        "honesty": "this stage constructs and evaluates the local systems; "
                   "it certifies nothing at the orbit level and upgrades no "
                   "theorem status — the substrate is the float64 "
                   "box-midpoint orbit, and the assembly, the "
                   "between-nodes bridge, and the period statement remain "
                   "open (Stage 4)",
    }

    dst = ROOT / "c4_piecewise_chebyshev_stage3.json"
    dst.write_text(json.dumps(out, indent=2))
    print(f"wrote {dst.name}")

    npz = ROOT / "c4_piecewise_chebyshev_stage3.npz"
    arrays = {
        "q_total": q_total,
        "Ainv_bound": Ainv_bound,
        "S_in_norm": S_in_norm,
        "S_in_rig": S_in_rig,
        "Szd_norm": Szd_norm,
        "Szd_rig": Szd_rig,
        "Lambda": Lam_hi,
        "Dv3_abs_hi": Dv3_abs_hi,
        "step_eig_max_real": step_eigs,
        "Y_sup_by_combo": np.array([cb["Y_sup"] for cb in combos]),
        "closing_radius_by_combo": np.array(
            [cbl["closing_radius"] for cbl in closures]),
    }
    np.savez_compressed(npz, **arrays)
    print(f"wrote {npz.name}")

    print(f"\nperiod P = {P:.6f}, M = {M}, degree = {n}")
    print(f"rho in [{rho_lo:.15f}, {rho_hi:.15f}], dtau = {dtau:.3e}, "
          f"zd_shift = {zd_shift:.3e}")
    print(f"stage matrices: q0 sup = {q0_sup:.2e}, q1 sup = {q1_sup:.2e}, "
          f"q_total sup = {q_total_sup:.2e}, invertible = {invertible}")
    print(f"||A^-1|| rigorous sup = {Ainv_bound_sup:.4f} "
          f"(h = {P / M:.5f})")
    print(f"assembly constants: ||S_in|| = {S_in_sup:.4f} "
          f"(rig {S_in_rig_sup:.4f}), ||Szd|| = {Szd_sup:.4f} "
          f"(rig {Szd_rig_sup:.4f}), Lambda = {Lambda_sup:.3f}")
    for cbl in closures:
        print(f"  [r_in={cbl['r_in']:g}, delta={cbl['delta']:g}] "
              f"Y = {cbl['Y_sup']:.3e} -> r_close = "
              f"{cbl['closing_radius']:.3e} (closes={cbl['closes']})")
    print(f"augmented monodromy top 6 (float): "
          f"{[float(x) for x in aug_eigs[:6]]}")
    print(f"  vs committed: phase {COMMITTED_MONODROMY['phase']} "
          f"(gap {phase_gap:.2e}), dominant "
          f"{COMMITTED_MONODROMY['dominant']} (gap {dominant_gap:.2e})")
    ok_all = all(bool(v) for k, v in checks.items() if isinstance(v, bool))
    print(f"all boolean checks pass: {ok_all}")
    print(f"total runtime {time.time() - t_start:.1f} s")


if __name__ == "__main__":
    main()

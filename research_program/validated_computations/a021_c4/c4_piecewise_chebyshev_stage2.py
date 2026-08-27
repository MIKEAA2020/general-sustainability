#!/usr/bin/env python3
"""A1 piecewise-Chebyshev campaign — STAGE 2: outward-rounded interval
evaluation of the local collocation defects and Jacobian blocks.

Status: INTERVAL EVALUATION (machinery + measurement) — NOT a certificate.
This is the second executed stage of the piecewise-Chebyshev route specified
in A1_CONTINUUM_LIFT_STATUS.md.  Stage 1 (substrate + local-gain diagnostic,
float64) is committed; this stage re-evaluates the same substrate in
outward-rounded interval arithmetic and adds the tube-inflation ladder that
Stage 3's radii polynomials need.  No Krawczyk operator, no radii polynomial,
no patch-to-patch assembly: nothing here upgrades any theorem status, and A1
remains COMPUTED_PARTIAL until Stage 4 closes.

What it produces (all rigorously enclosed, every operation outward-rounded):

  1. interval enclosures of the substrate node values X and delayed values
     Zd at ALL M=8000 patches x 9 Chebyshev-Lobatto nodes, via an exact
     phase decomposition: at the algebraic node times
     t = (P/M)(j + (xi_i+1)/2) the node phase 2*pi*k*t/P is P-free
     (= 2*pi*k*j/M + pi*k*(xi_i+1)/M), so the patch phases are exact M-th
     roots of unity (computed once in mpmath, then integer powers by
     rigorous binary powering in float64 intervals) and the node offsets
     are 729 mpmath phase evaluations — the enclosure widths stay at the
     ~1e-14 level instead of the ~1e-11 a naive interval product chain
     would give;
  2. interval enclosures of BOTH derivatives on every patch — the local
     Chebyshev spectral derivative (2/h)*Diff*X with the differentiation
     matrix enclosed once in mpmath, and the Fourier derivative of the
     underlying K=80 interpolant (per-mode, no matrix amplification);
  3. interval enclosures of the DDE right-hand side f(X, Zd) (rational
     part in float64 intervals, the softplus memory term per node in
     mpmath) and hence of BOTH collocation defects
        Y_cheb = (2/h)*Diff*X - f(X, Zd)      (the Stage-3 Y-input)
        Y_four = dX_fourier/dt - f(X, Zd)     (the orbit's own defect)
     at every node of every patch;
  4. interval enclosures of the Jacobian blocks (J, Dv) at every node
     (sigmoid per node in mpmath) and the rigorous local-gain interval
        g in [h*(min colsum |J| + sum |Dv|), h*(max colsum |J| + sum |Dv|)]
     (column-sum = the 1-norm Stage 1 measured) whose upper end is the
     Lipschitz constant Stage 3 charges;
  5. a tube-inflation ladder (delta in {0, 1e-8, 1e-6}): the same f/J/defect
     evaluation on boxes inflated by +/-delta — the machinery Stage 3 needs
     for tube (radii-polynomial) evaluation, with the width growth measured;
  6. verification checks: (a) an independent full-mpmath evaluation of the
     Fourier sum AND the delayed value at five nodes is contained in the
     interval node values; (b) a float64 point evaluation via the same
     decomposition agrees with the interval midpoints to the documented
     float64 phase-rounding scale; (c) the recomputed float64 gain sup
     (Stage 1's quantity, 0.3325 at M=8000) lies inside the interval gain.

Node convention (documented difference from Stage 1): the nodes here are the
EXACT algebraic node times t = (P/M)(j + (xi_i+1)/2); Stage 1 evaluated at
the float64 expression j*h + 0.5*h*(xi+1).  The two differ by at most a few
ulp(371) ~ 2e-13 in time, which moves the defect by <= ~1e-11, far below the
reported defect ~7.9e-9 — the recomputed float gain is compared against
Stage 1's committed 0.3325 reading.

Deterministic; no randomness.  Run from anywhere:
    python3 research_program/validated_computations/a021_c4/
           c4_piecewise_chebyshev_stage2.py
Writes c4_piecewise_chebyshev_stage2.json (+ .npz companion) next to this
file.
"""
from __future__ import annotations

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
from c4_monodromy import jac_point  # noqa: E402

M_SEG = 8000
CHEB_DEGREE = 8
INFLATION = (0.0, 1e-8, 1e-6)

_NINF, _PINF = -np.inf, np.inf
f64 = np.float64


# ------------------------------------------------------------ interval ops
# An interval is a pair (lo, hi) of float64 arrays (or scalars) with lo<=hi.
# Every operation rounds outward with np.nextafter, so results rigorously
# contain the exact real result of the same operation sequence.

def _lo(x):
    return np.nextafter(x, _NINF)


def _hi(x):
    return np.nextafter(x, _PINF)


def iv_pt(x):
    """Point float64 -> tight interval."""
    x = f64(x)
    return (_lo(x), _hi(x))


def iadd(a, b):
    return (_lo(a[0] + b[0]), _hi(a[1] + b[1]))


def isub(a, b):
    return (_lo(a[0] - b[1]), _hi(a[1] - b[0]))


def ineg(a):
    return (-a[1], -a[0])


def imul(a, b):
    p1 = a[0] * b[0]
    p2 = a[0] * b[1]
    p3 = a[1] * b[0]
    p4 = a[1] * b[1]
    return (_lo(np.minimum(np.minimum(p1, p2), np.minimum(p3, p4))),
            _hi(np.maximum(np.maximum(p1, p2), np.maximum(p3, p4))))


def i_scal(c, a):
    """Scalar interval c times array interval a (broadcast)."""
    return imul((f64(c[0]), f64(c[1])), a)


def i_div(a, b):
    if np.any((np.asarray(b[0]) <= 0) & (np.asarray(b[1]) >= 0)):
        raise ZeroDivisionError("division by interval containing 0")
    return imul(a, (1.0 / np.asarray(b[1], f64), 1.0 / np.asarray(b[0], f64)))


def mp_interval(lo, hi):
    """float64 lo/hi -> mpmath interval."""
    return miv.mpf([mpf(float(lo)), mpf(float(hi))])


def f64_interval(x):
    """mpmath interval -> float64 (lo, hi) scalars, outward."""
    a, b = x.a, x.b
    fa, fb = float(a), float(b)
    if mpf(fa) > a:
        fa = float(np.nextafter(fa, _NINF))
    if mpf(fb) < b:
        fb = float(np.nextafter(fb, _PINF))
    return fa, fb


def i_abs_lo(lo, hi):
    """Lower bound of |x| on [lo, hi] (elementwise)."""
    return np.where((lo <= 0) & (hi >= 0), 0.0,
                    np.minimum(np.abs(lo), np.abs(hi)))


def i_abs_hi(lo, hi):
    return np.maximum(np.abs(lo), np.abs(hi))


# ------------------------------------------------------------ model (interval)

def make_f_and_jac():
    """Return interval evaluators of the C4 rhs and Jacobian.

    Rational parts are vectorised float64 intervals; the softplus memory
    term (f) and the sigmoid (J) are evaluated per node in mpmath.
    Dref = 1 (exact), matching the committed rhs (zdel - E/Emax) ==
    (zdel/Dref - E/Emax).
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

    def f_iv(X, Zd):
        """X: list of 4 interval arrays (M,9); Zd: interval array (M,9)."""
        N, A, Z, E = X
        one = iv_pt(1.0)
        fac = i_div(A, iadd(A, p['A0']))
        N_over_K = i_div(N, p['K'])
        R = imul(imul(imul(p['r'], N), isub(one, N_over_K)), fac)
        B = iadd(R, imul(imul(p['kappaA'], N), fac))
        deficit = isub(imul(imul(p['q'], E), N), R)
        gate = isub(one, i_div(E, p['Emax']))
        sp = transcendental(deficit, "softplus")
        mem = (np.maximum(0.0, sp[0]), np.maximum(0.0, sp[1]))
        fN = isub(R, imul(imul(p['q'], E), N))
        fA = isub(imul(p['omegaA'], isub(p['AeqW'], A)), B)
        fZ = i_div(isub(mem, Z), p['taum'])
        fE = imul(gate, iadd(
            imul(imul(p['eta'], E),
                 isub(i_div(Zd, p['Dref']), i_div(E, p['Emax']))),
            imul(p['delta0'], i_div(Zd, iadd(p['Zref'], Zd)))))
        return [fN, fA, fZ, fE], deficit

    def jac_iv(X, Zd, deficit):
        """Interval Jacobian blocks at every node.

        Returns ((Jlo, Jhi), (Dvlo, Dvhi)) with J (M,9,4,4), Dv (M,9,4).
        """
        N, A, Z, E = X
        Aplus = iadd(A, p['A0'])
        fac = i_div(A, Aplus)
        dfac = i_div(p['A0'], imul(Aplus, Aplus))
        one = iv_pt(1.0)
        two = iv_pt(2.0)
        N_over_K = i_div(N, p['K'])
        RN = imul(imul(p['r'], isub(one, imul(two, N_over_K))), fac)
        RA = imul(imul(imul(p['r'], N), isub(one, N_over_K)), dfac)
        BN = iadd(RN, imul(p['kappaA'], fac))
        BA = iadd(RA, imul(imul(p['kappaA'], N), dfac))
        sig = transcendental(deficit, "sigmoid")
        gate = isub(one, i_div(E, p['Emax']))
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
        put(0, 3, ineg(imul(p['q'], N)))
        put(1, 0, ineg(BN))
        put(1, 1, iadd(ineg(BA), ineg(p['omegaA'])))
        put(2, 0, i_div(imul(sig, isub(imul(p['q'], E), RN)), p['taum']))
        put(2, 1, i_div(ineg(imul(sig, RA)), p['taum']))
        put(2, 2, ineg(i_div(one, p['taum'])))
        put(2, 3, i_div(imul(sig, imul(p['q'], N)), p['taum']))
        put(3, 3, iadd(ineg(i_div(H, p['Emax'])),
                       imul(gate, imul(p['eta'],
                                       isub(Zd, imul(two,
                                                     i_div(E, p['Emax'])))))))
        Dv3 = imul(gate, iadd(
            imul(imul(p['eta'], E), i_div(one, p['Dref'])),
            imul(imul(p['delta0'], p['Zref']),
                 i_div(one, imul(iadd(p['Zref'], Zd),
                                 iadd(p['Zref'], Zd))))))
        Dvlo[:, :, 3] = Dv3[0]
        Dvhi[:, :, 3] = Dv3[1]
        return (Jlo, Jhi), (Dvlo, Dvhi)

    return f_iv, jac_iv, p


# ------------------------------------------------------------ helpers

def cheb_lobatto(n):
    j = np.arange(n + 1)
    return np.cos(np.pi * (n - j) / n)


def f_float(Xpt, Zdpt):
    """Float64 rhs at point values (mirrors c4_monodromy.rhs)."""
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


def diff_float(Xpt, P):
    """Float64 (2/h)*Diff*X with the Stage-1 differentiation matrix."""
    n = CHEB_DEGREE
    nodes = cheb_lobatto(n)
    w = np.ones(n + 1)
    w[0] = w[-1] = 0.5
    w *= (-1.0) ** np.arange(n + 1)
    Diff = np.zeros((n + 1, n + 1))
    for i in range(n + 1):
        for j in range(n + 1):
            if i != j:
                Diff[i, j] = (w[j] / w[i]) / (nodes[i] - nodes[j])
        Diff[i, i] = -np.sum(Diff[i, :])
    out = np.zeros_like(Xpt)
    for i in range(n + 1):
        for j in range(n + 1):
            out[:, i] += Diff[i, j] * Xpt[:, j]
    return out * (2.0 * M_SEG / P)


# ------------------------------------------------------------ main

def main():
    t_start = time.time()
    box = np.load(ROOT / "c4_orbit_krawczyk_box.npz")
    u_mid = 0.5 * (box["u_lo"] + box["u_hi"])
    P = float(0.5 * (box["P_lo"] + box["P_hi"]))

    # Fourier coefficients of the 161-point orbit (float64), wrapped freqs.
    # X_s(t) = Re(c_0) + sum_{k>=1} [A_k cos(theta_k) + B_k sin(theta_k)]
    # with A_k = c_k.re + c_{-k}.re, B_k = c_{-k}.im - c_k.im  (exact for
    # the full 161-mode interpolant, no conjugate-symmetry assumption).
    c = np.fft.fft(u_mid, axis=0) / N_NODES
    c0_re = c[0].real.copy()
    A = np.stack([c[k].real + c[N_NODES - k].real
                  for k in range(1, K_MAX + 1)])          # (80, 4)
    B = np.stack([c[N_NODES - k].imag - c[k].imag
                  for k in range(1, K_MAX + 1)])          # (80, 4)
    A_iv = [[iv_pt(A[k, s]) for s in range(4)] for k in range(K_MAX)]
    B_iv = [[iv_pt(B[k, s]) for s in range(4)] for k in range(K_MAX)]
    c0_iv = [iv_pt(c0_re[s]) for s in range(4)]

    n = CHEB_DEGREE
    nodes = cheb_lobatto(n)
    M = M_SEG

    # ---- P-dependent per-mode constants in mpmath (tight intervals)
    P_iv = mp_interval(_lo(P), _hi(P))
    om_f64, phi_f64 = [], []
    phi_mp = []
    for k in range(1, K_MAX + 1):
        w = 2 * miv.pi * k / P_iv
        f = 2 * miv.pi * k * mpf(TAU) / P_iv
        om_f64.append(f64_interval(w))
        phi_f64.append(f64_interval(f))
        phi_mp.append(f)
    two_h_inv = f64_interval(miv.mpf(2) * M / P_iv)
    h_f64 = f64_interval(P_iv / M)

    # folded delay coefficients (Z component): the delayed value reuses the
    # SAME phase factors via
    #   A cos(th-phi) + B sin(th-phi) = At cos(th) + Bt sin(th),
    #   At = A cos(phi) - B sin(phi),  Bt = A sin(phi) + B cos(phi).
    At_f64, Bt_f64 = [], []
    for k in range(K_MAX):
        cs = miv.cos(phi_mp[k])
        sn = miv.sin(phi_mp[k])
        At_f64.append(f64_interval(miv.mpf(A[k, 2]) * cs - miv.mpf(B[k, 2]) * sn))
        Bt_f64.append(f64_interval(miv.mpf(A[k, 2]) * sn + miv.mpf(B[k, 2]) * cs))

    # ---- roots of unity z_j = e^{2 pi i j/M}, mpmath once per j
    print("computing M-th roots of unity in mpmath ...", flush=True)
    zre = (np.empty(M), np.empty(M))
    zim = (np.empty(M), np.empty(M))
    for j in range(M):
        th = 2 * miv.pi * j / M
        zre[0][j], zre[1][j] = f64_interval(miv.cos(th))
        zim[0][j], zim[1][j] = f64_interval(miv.sin(th))

    # ---- integer powers z^k: z^k = e^{2 pi i k j / M} is AGAIN an M-th
    # root of unity (index (k*j) mod M) — a pure permutation of the
    # rigorous mpmath table, exact and width-1-ulp (no binary powering
    # needed, which would inflate the widths through repeated products)
    print("integer powers z^k by exact table permutation ...", flush=True)
    j_idx = np.arange(M)
    zk = [None] * (K_MAX + 1)
    zk[0] = ((np.ones(M), np.ones(M)), (np.zeros(M), np.zeros(M)))
    for k in range(1, K_MAX + 1):
        idx = (k * j_idx) % M
        zk[k] = ((zre[0][idx], zre[1][idx]), (zim[0][idx], zim[1][idx]))

    # ---- node offsets e^{i psi_{k,i}}, psi = pi k (xi_i+1)/M  (P-free)
    print("node offset phases (729 mpmath evaluations) ...", flush=True)
    psi_re = [[None] * (n + 1) for _ in range(K_MAX)]
    psi_im = [[None] * (n + 1) for _ in range(K_MAX)]
    for k in range(1, K_MAX + 1):
        for i in range(n + 1):
            xi = miv.cos(miv.pi * (n - i) / n)
            psi = miv.pi * k * (xi + 1) / M
            psi_re[k - 1][i] = f64_interval(miv.cos(psi))
            psi_im[k - 1][i] = f64_interval(miv.sin(psi))

    # ---- accumulate X, dX_fourier, Zd over the modes (the mode sums are
    # accumulated on zero BEFORE adding c0, so the interval rounding of the
    # accumulation stays at the mode-sum scale, not the ~300 value scale)
    print("accumulating node values / derivatives over 80 modes ...",
          flush=True)
    X = [iv_pt(np.zeros((M, n + 1))) for _ in range(4)]
    dXf = [iv_pt(np.zeros((M, n + 1))) for _ in range(4)]
    Zd = iv_pt(np.zeros((M, n + 1)))
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
            # X += A cos + B sin   (cos = phase re, sin = phase im)
            X[s] = iadd(X[s], iadd(i_scal(A_iv[k - 1][s], pre),
                                   i_scal(B_iv[k - 1][s], pim)))
            # dX += omega_k (B cos - A sin)
            dXf[s] = iadd(dXf[s], imul(om_f64[k - 1],
                                       isub(i_scal(B_iv[k - 1][s], pre),
                                            i_scal(A_iv[k - 1][s], pim))))
        # Zd with the folded delay coefficients
        Zd = iadd(Zd, iadd(i_scal(At_f64[k - 1], pre),
                           i_scal(Bt_f64[k - 1], pim)))
    for s in range(4):
        X[s] = iadd(X[s], c0_iv[s])
    Zd = iadd(Zd, c0_iv[2])

    # ---- interval differentiation matrix (mpmath, once)
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

    # ---- local Chebyshev derivative dX_cheb = (2/h) Diff X, vectorised
    print("interval spectral derivative on all patches ...", flush=True)
    dXc_lo = [np.zeros((M, n + 1)) for _ in range(4)]
    dXc_hi = [np.zeros((M, n + 1)) for _ in range(4)]
    for s in range(4):
        for i in range(n + 1):
            col_lo = np.zeros(M)
            col_hi = np.zeros(M)
            for j in range(n + 1):
                term = i_scal((Dlo[i, j], Dhi[i, j]),
                              (X[s][0][:, j], X[s][1][:, j]))
                col_lo = _lo(col_lo + term[0])
                col_hi = _hi(col_hi + term[1])
            dXc_lo[s][:, i] = col_lo
            dXc_hi[s][:, i] = col_hi
    dXc = [imul(two_h_inv, (dXc_lo[s], dXc_hi[s])) for s in range(4)]

    # ---------------------------------------------------------- float points
    print("float64 point evaluation via the same decomposition ...",
          flush=True)
    Xpt = [np.zeros((M, n + 1)) + c0_re[s] for s in range(4)]
    dXpt = [np.zeros((M, n + 1)) for _ in range(4)]
    Zdpt = np.zeros((M, n + 1)) + c0_re[2]
    phif = np.array([2 * np.pi * k * TAU / P for k in range(1, K_MAX + 1)])
    for k in range(1, K_MAX + 1):
        al = 2 * np.pi * (k * np.arange(M) % M) / M
        for i in range(n + 1):
            th = al + np.pi * k * (nodes[i] + 1) / M
            ct, st = np.cos(th), np.sin(th)
            thd = th - phif[k - 1]
            ctd, std = np.cos(thd), np.sin(thd)
            for s in range(4):
                Xpt[s][:, i] += A[k - 1, s] * ct + B[k - 1, s] * st
                dXpt[s][:, i] += (2 * np.pi * k / P) * (
                    -A[k - 1, s] * st + B[k - 1, s] * ct)
            Zdpt[:, i] += A[k - 1, 2] * ctd + B[k - 1, 2] * std

    # agreement of the float points with the interval midpoints
    float_agree = max(
        float(np.abs(Xpt[s] - 0.5 * (X[s][0] + X[s][1])).max())
        for s in range(4))
    float_agree = max(float_agree,
                      float(np.abs(Zdpt - 0.5 * (Zd[0] + Zd[1])).max()))
    float_agree_ok = bool(float_agree <= 3e-12)

    # float gain sup (Stage 1's quantity: h*(max column sum |J| + |Dv|_1))
    print("float64 gain sup (Stage-1 quantity, algebraic-node convention) ...",
          flush=True)
    gpt = np.zeros((M, n + 1))
    h_fl = P / M
    for j in range(M):
        for i in range(n + 1):
            J, Dv = jac_point(Xpt[0][j, i] * 0 +
                              np.array([Xpt[0][j, i], Xpt[1][j, i],
                                        Xpt[2][j, i], Xpt[3][j, i]]),
                              Zdpt[j, i])
            gpt[j, i] = h_fl * (np.abs(J).sum(axis=0).max()
                                + np.abs(Dv).sum())
    gain_float_sup = float(gpt.max())

    # ---------------------------------------------------------- verification
    print("independent mpmath cross-check at 5 nodes (X and Zd) ...",
          flush=True)
    rng_nodes = [(0, 0), (M // 3, 4), (M // 2, 8), (3 * M // 4, 2), (M - 1, 6)]
    xcheck_ok = True
    zdcheck_ok = True
    xcheck_width = 0.0
    for (j, i) in rng_nodes:
        xi = miv.cos(miv.pi * (n - i) / n)
        base = j + (xi + 1) / 2
        for s in range(4):
            tot = miv.mpf(c0_re[s])
            for k in range(1, K_MAX + 1):
                th = 2 * miv.pi * k * base / M
                tot += (miv.mpf(A[k - 1, s]) * miv.cos(th)
                        + miv.mpf(B[k - 1, s]) * miv.sin(th))
            if not (tot.a >= X[s][0][j, i] and tot.b <= X[s][1][j, i]):
                xcheck_ok = False
            xcheck_width = max(xcheck_width, float(tot.b - tot.a))
        totz = miv.mpf(c0_re[2])
        for k in range(1, K_MAX + 1):
            th = 2 * miv.pi * k * base / M - phi_mp[k - 1]
            totz += (miv.mpf(A[k - 1, 2]) * miv.cos(th)
                     + miv.mpf(B[k - 1, 2]) * miv.sin(th))
        if not (totz.a >= Zd[0][j, i] and totz.b <= Zd[1][j, i]):
            zdcheck_ok = False

    # ---------------------------------------------------------- f, J, ladder
    f_iv, jac_iv, _ = make_f_and_jac()

    def evaluate(Xi, Zdi, label):
        print(f"  interval f + Jacobian ({label}) ...", flush=True)
        t0 = time.time()
        F, deficit = f_iv(Xi, Zdi)
        (Jlo, Jhi), (Dvlo, Dvhi) = jac_iv(Xi, Zdi, deficit)
        Yc = [isub(dXc[s], F[s]) for s in range(4)]
        Yf = [isub(dXf[s], F[s]) for s in range(4)]
        # gain interval per node: column sums (the 1-norm, as in Stage 1)
        col_hi = i_abs_hi(Jlo, Jhi).sum(axis=2).max(axis=2)     # (M,9)
        col_lo = i_abs_lo(Jlo, Jhi).sum(axis=2).max(axis=2)
        dv_hi = i_abs_hi(Dvlo, Dvhi).sum(axis=2)
        dv_lo = i_abs_lo(Dvlo, Dvhi).sum(axis=2)
        g_hi = (np.nextafter(h_f64[0] * (col_hi + dv_hi), _NINF),
                np.nextafter(h_f64[1] * (col_hi + dv_hi), _PINF))
        g_lo = (np.nextafter(h_f64[0] * (col_lo + dv_lo), _NINF),
                np.nextafter(h_f64[1] * (col_lo + dv_lo), _PINF))
        res = {
            "label": label,
            "f_width_sup": float(max((F[s][1] - F[s][0]).max()
                                     for s in range(4))),
            "Y_cheb_abs_sup_upper": float(max(
                i_abs_hi(Yc[s][0], Yc[s][1]).max() for s in range(4))),
            "Y_cheb_width_sup": float(max(
                (Yc[s][1] - Yc[s][0]).max() for s in range(4))),
            "Y_four_abs_sup_upper": float(max(
                i_abs_hi(Yf[s][0], Yf[s][1]).max() for s in range(4))),
            "Y_four_width_sup": float(max(
                (Yf[s][1] - Yf[s][0]).max() for s in range(4))),
            "gain_sup_lower": float(g_lo[1].max()),
            "gain_sup_upper": float(g_hi[1].max()),
            "J_width_sup": float((Jhi - Jlo).max()),
            "Dv_width_sup": float((Dvhi - Dvlo).max()),
        }
        return res, Yc, Yf, g_lo, g_hi, round(time.time() - t0, 1)

    ladder = []
    Yc_base = Yf_base = g_base = None
    contain_defect = None
    for delta in INFLATION:
        if delta == 0.0:
            Xi, Zdi = X, Zd
            label = "delta=0 (on-substrate)"
        else:
            Xi = [(X[s][0] - delta, X[s][1] + delta) for s in range(4)]
            Zdi = (Zd[0] - delta, Zd[1] + delta)
            label = f"delta={delta:g} (tube inflation)"
        res, Yc, Yf, g_lo, g_hi, secs = evaluate(Xi, Zdi, label)
        if delta == 0.0:
            Yc_base, Yf_base, g_base = Yc, Yf, (g_lo, g_hi)
            # float defect containment (tolerance = the float64 evaluation
            # error scale of the matvec, documented)
            Fpt = f_float(Xpt, Zdpt)
            ok = True
            for s in range(4):
                Yc_pt = diff_float(Xpt[s], P) - Fpt[s]
                Yf_pt = dXpt[s] - Fpt[s]
                if not (np.all(Yc_pt >= Yc[s][0] - 1e-9) and
                        np.all(Yc_pt <= Yc[s][1] + 1e-9) and
                        np.all(Yf_pt >= Yf[s][0] - 1e-9) and
                        np.all(Yf_pt <= Yf[s][1] + 1e-9)):
                    ok = False
            contain_defect = ok
        ladder.append(res)
        print(f"    -> {label}: sup|Y_cheb| <= {res['Y_cheb_abs_sup_upper']:.3e} "
              f"gain sup in [{res['gain_sup_lower']:.4f}, "
              f"{res['gain_sup_upper']:.4f}] ({secs} s)", flush=True)

    gain_lo = ladder[0]["gain_sup_lower"]
    gain_hi = ladder[0]["gain_sup_upper"]
    gain_contains = bool(gain_lo - 1e-9 <= gain_float_sup <= gain_hi + 1e-9)
    stage1_gain = 0.3325
    stage1_agrees = bool(abs(gain_float_sup - stage1_gain) <= 1e-3)

    out = {
        "title": "A1 piecewise-Chebyshev campaign — Stage 2: "
                 "outward-rounded interval evaluation of the local "
                 "collocation defects and Jacobian blocks",
        "status": "INTERVAL EVALUATION (machinery + measurement) — NOT a "
                  "certificate: no Krawczyk operator, no radii polynomial, "
                  "no patch-to-patch assembly; A1 remains COMPUTED_PARTIAL "
                  "until Stage 4 closes",
        "inputs": {
            "orbit": "committed Krawczyk box midpoint "
                     "(c4_orbit_krawczyk_box.npz)",
            "period_P": P,
            "M_segments": M_SEG,
            "cheb_degree": CHEB_DEGREE,
            "nodes_convention": "exact algebraic node times "
                                "t = (P/M)(j + (xi_i+1)/2); Stage 1's "
                                "float64 node expression differs by "
                                "<= 2e-13 in time (defect-level effect "
                                "<= ~1e-11, far below the 7.9e-9 signal)",
            "delay_tau": TAU,
        },
        "method": {
            "phases": "exact decomposition: at the algebraic nodes the "
                      "phase 2 pi k t/P is P-free (= 2 pi k j/M + "
                      "pi k (xi_i+1)/M); patch phases = M-th roots of "
                      "unity computed once in mpmath — the integer power "
                      "z^k is again an M-th root of unity, taken by exact "
                      "integer table permutation (width 1 ulp, no binary "
                      "powering); node offsets = 729 mpmath evaluations; "
                      "the delay folded per mode "
                      "(At = A cos(phi) - B sin(phi), "
                      "Bt = A sin(phi) + B cos(phi))",
            "interval_arithmetic": "float64 with np.nextafter outward "
                                   "rounding everywhere; softplus (f) and "
                                   "sigmoid (J) per node in mpmath (dps=30); "
                                   "differentiation matrix and all "
                                   "P-dependent constants in mpmath (dps=40)",
            "full_spectrum": "the full 161-mode wrapped-frequency "
                             "interpolant via A_k = c_k.re + c_-k.re, "
                             "B_k = c_-k.im - c_k.im (no conjugate-symmetry "
                             "assumption — matches the Stage-1 evaluator)",
        },
        "measurements_delta0": {
            "X_width_sup": float(max((X[s][1] - X[s][0]).max()
                                     for s in range(4))),
            "Zd_width_sup": float((Zd[1] - Zd[0]).max()),
            "dX_cheb_width_sup": float(max((dXc[s][1] - dXc[s][0]).max()
                                           for s in range(4))),
            "dX_fourier_width_sup": float(max((dXf[s][1] - dXf[s][0]).max()
                                              for s in range(4))),
        },
        "inflation_ladder": ladder,
        "verification": {
            "mpmath_crosscheck_X_contained_5_nodes": bool(xcheck_ok),
            "mpmath_crosscheck_Zd_contained_5_nodes": bool(zdcheck_ok),
            "mpmath_crosscheck_max_width": xcheck_width,
            "float_midpoint_agreement_max": float_agree,
            "float_midpoint_agreement_ok": float_agree_ok,
            "float_agreement_note": "the float64 evaluator agrees with the "
                                    "interval midpoints to <= 3e-12 (the "
                                    "float64 phase-rounding scale); the "
                                    "RIGOROUS containment is the mpmath "
                                    "cross-check",
            "float_defect_contained_tol_1e-9": bool(contain_defect),
            "float_gain_sup_recomputed": gain_float_sup,
            "stage1_gain_value": stage1_gain,
            "gain_interval_contains_float": gain_contains,
            "gain_agrees_with_stage1_4digits": stage1_agrees,
            "stage1_defect_value_M8000": 7.865e-09,
        },
        "stage2_verdict": {},
    }

    d0 = ladder[0]
    out["stage2_verdict"] = {
        "Y_input": (
            f"the Stage-3 Y-input is rigorously enclosed: sup |Y_cheb| <= "
            f"{d0['Y_cheb_abs_sup_upper']:.3e} with interval width <= "
            f"{d0['Y_cheb_width_sup']:.3e}"
        ),
        "fourier_defect": (
            f"the orbit's own DDE defect (Fourier derivative) is enclosed: "
            f"sup |Y_four| <= {d0['Y_four_abs_sup_upper']:.3e} "
            f"(width <= {d0['Y_four_width_sup']:.3e}) — to be compared "
            f"with Stage 1's 7.865e-9 float reading"
        ),
        "gain": (
            f"the rigorous local-gain interval at M=8000 is "
            f"[{gain_lo:.14f}, {gain_hi:.14f}] (width "
            f"{gain_hi - gain_lo:.1e}); the recomputed float64 sup is "
            f"{gain_float_sup:.14f} (Stage 1's committed reading: 0.3325, "
            f"rounded to 4 decimals) — the O(1)-local-gain premise now "
            f"holds in interval arithmetic, not just float"
        ),
        "tube_machinery": (
            f"the inflation ladder runs end-to-end: at delta=1e-6 the gain "
            f"sup upper is {ladder[-1]['gain_sup_upper']:.4f} and the "
            f"defect-interval width sup is "
            f"{ladder[-1]['Y_cheb_width_sup']:.3e} — the Stage-3 tube "
            f"evaluation machinery works and its width growth is measured"
        ),
        "next_stages": [
            "Stage 3: the local Krawczyk/radii-polynomial system on the "
            "patches with the finite-band delay coupling enclosed (consumes "
            "the interval Y-input and the tube-Jacobian machinery delivered "
            "here)",
            "Stage 4: patch-to-patch contraction assembly and the continuum "
            "orbit certificate (the A1 gate)",
        ],
        "honesty": "this stage encloses and measures; it certifies nothing "
                   "and upgrades no theorem status — the substrate is the "
                   "float64 box-midpoint orbit, NOT an enclosure of the "
                   "true DDE solution",
    }

    dst = ROOT / "c4_piecewise_chebyshev_stage2.json"
    dst.write_text(json.dumps(out, indent=2))
    print(f"wrote {dst.name}")

    npz = ROOT / "c4_piecewise_chebyshev_stage2.npz"
    arrays = {}
    for s in range(4):
        arrays[f"Yc{s}_lo"] = Yc_base[s][0]
        arrays[f"Yc{s}_hi"] = Yc_base[s][1]
        arrays[f"Yf{s}_lo"] = Yf_base[s][0]
        arrays[f"Yf{s}_hi"] = Yf_base[s][1]
    arrays["gain_lo"] = g_base[0][1]
    arrays["gain_hi"] = g_base[1][1]
    np.savez_compressed(npz, **arrays)
    print(f"wrote {npz.name}")

    print(f"\nperiod P = {P:.3f}, M = {M}, degree = {n}")
    m0 = out["measurements_delta0"]
    print(f"X width sup     = {m0['X_width_sup']:.3e}")
    print(f"dX_cheb width   = {m0['dX_cheb_width_sup']:.3e}")
    print(f"dX_four width   = {m0['dX_fourier_width_sup']:.3e}")
    for r in ladder:
        print(f"[{r['label']}] sup|Y_cheb| <= {r['Y_cheb_abs_sup_upper']:.3e} "
              f"(width {r['Y_cheb_width_sup']:.3e})  "
              f"sup|Y_four| <= {r['Y_four_abs_sup_upper']:.3e}  "
              f"gain sup in [{r['gain_sup_lower']:.4f}, "
              f"{r['gain_sup_upper']:.4f}]")
    v = out["verification"]
    print(f"verification: mpmath X contained = {xcheck_ok}, "
          f"Zd contained = {zdcheck_ok} "
          f"(max width {xcheck_width:.2e}); "
          f"float midpoint agreement {float_agree:.2e} (ok={float_agree_ok}); "
          f"float defect contained = {contain_defect}; "
          f"float gain sup {gain_float_sup:.4f} in "
          f"[{gain_lo:.4f}, {gain_hi:.4f}] ({gain_contains}); "
          f"Stage-1 agreement = {stage1_agrees}")
    print(f"total runtime {time.time() - t_start:.1f} s")


if __name__ == "__main__":
    main()

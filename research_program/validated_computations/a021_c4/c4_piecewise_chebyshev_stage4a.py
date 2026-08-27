#!/usr/bin/env python3
"""A1 piecewise-Chebyshev campaign — STAGE 4a: the assembly measurements,
the interval-march obstruction record, and the RIGOROUS between-nodes
continuum defect bound.

Status: MEASUREMENTS + ONE RIGOROUS ORBIT-LEVEL BOUND (the between-nodes
continuum defect of the substrate polynomial) — NOT the assembly
certificate.  This is the fourth executed stage of the piecewise-Chebyshev
route specified in A1_CONTINUUM_LIFT_STATUS.md (Stages 1-3 committed).

Three deliverables:

(1) THE ASSEMBLY MEASUREMENTS (float, validated against the committed
    Stage-3 monodromy preview to ~1e-12): the delay-augmented collocation
    monodromy is reconstructed by an independent implementation (the ring
    march); the DICHOTOMY PROFILE K_0 = sup_j ||P_j||_inf of the partial
    products; the phase-pinned and bordered inverse conditioning; the
    tangent vector and the pin coordinate; and the NONLINEAR MISMATCH
    MARCH: the one-period float composition of the exact local Newton
    maps starting at the substrate augmented state — the mismatch
    ||Psi(u*) - u*||_inf ~ 1.2e-8 (the substrate is essentially the
    periodic collocation fixed point; the future certificate's Y-term is
    dominated by enclosure widths, not by the center).

(2) THE INTERVAL-MARCH OBSTRUCTION, MEASURED: the per-step width-growth
    rate rho_w of the |step| products (the interval matrix march's
    pessimism) is 1.00264/step — a per-period growth of 1.5e9.  Combined
    with the dichotomy constant K_0 and the per-step enclosure widths,
    the direct interval monodromy march accumulates width ~1e4 and the
    windowed re-centered variant is defeated by the K^(n_w-1) compounding.
    CONSEQUENCE (recorded): the rigorous assembly (the pinned-monodromy
    Z-term and the mismatch Y-term) REQUIRES correlation-tracking
    arithmetic (an affine/Taylor-model march with noise symbols — the
    phase direction's correlation must be carried explicitly); plain
    interval arithmetic cannot see the dichotomy cancellation.  This is
    the Stage-4b specification, now grounded in measured constants.

(3) THE RIGOROUS BETWEEN-NODES CONTINUUM DEFECT BOUND (the certificate-
    grade new result): on EVERY patch, the DDE residual
        r(t) = p'(t) - rho * f(p(t), p(t - tau/rho))
    of the substrate piecewise polynomial is bounded over the WHOLE patch
    (nodes and interiors alike) by
        ||r||_inf(patch) <= Lambda_8 * max_i |r(node_i)| + REM_9
    where Lambda_8 is the (rigorously computed) Lebesgue constant of the
    degree-8 Chebyshev-Lobatto interpolation, max_i|r(node_i)| is the
    rigorous node-residual enclosure (the Stage-3 defect machinery
    re-executed at the minimal input enclosures, plus the node-8 roll
    with the continuity-gap inflation), and REM_9 is the rigorous
    degree-9 interpolation remainder: since p is degree 8, r^(9) =
    -rho * (f o (p, p_delayed))^(9), and the ninth derivative of the
    composition is bounded by the FULL multivariate Faà di Bruno
    expansion: the per-variable derivative sup bounds B_{v,j} of the
    state polynomials (rigorous monomial-coefficient sums of the exactly
    computed Lagrange-basis derivatives), the partial derivatives of f
    up to total order 9 over sector tubes (rigorous sparse interval
    Taylor jets through f's expression tree, with the softplus composed
    via the GLOBAL logistic-derivative sup bounds — the Eulerian
    polynomial recurrence), and the truncated-exponential Bell DP
    exp(G) in the (u, t^5) monomials at the sector level (computed in
    magnitude arithmetic — exact for the symmetric-interval G).

What this does NOT do (Stage 4b, not executed): the rigorous monodromy
enclosure (blocked by the measured rho_w; needs the affine march), the
pinned-bootstrap Z/Y terms, the patch-to-patch assembly, the periodic-
delay bootstrap certificate, and the continuum orbit certificate.  A1
remains COMPUTED_PARTIAL.

Deterministic; no randomness.  Run from anywhere:
    python3 research_program/validated_computations/a021_c4/
           c4_piecewise_chebyshev_stage4a.py
Writes c4_piecewise_chebyshev_stage4a.json (+ .npz companion) next to
this file.
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
from c4_piecewise_chebyshev_stage3 import (  # noqa: E402
    cheb_lobatto, f_float, iv_pt, make_model, f64_interval,
    i_abs_hi, iadd, imul, i_scal, isub, i_div,
    _lo, _hi, _NINF, _PINF,
)
EPS_F = 2.220446049250313e-16
EPS_ACC = 40 * EPS_F

M_SEG = 8000
CHEB_DEGREE = 8
N = CHEB_DEGREE
RING = 100
NB = 4 + 99 * 9
R_BALL = 1e-6          # declared future-certificate ball radius
N_SECTORS = 128
COMMITTED_MONODROMY = {"phase": 1.0000000000028728,
                       "dominant": 0.6876928141092927,
                       "disc": 0.30271822276116467}
FACT9 = 362880.0


def sha256_of_array(a):
    return hashlib.sha256(np.ascontiguousarray(a).tobytes()).hexdigest()[:16]


def sigmoid_f(x, k=10.0):
    z = np.clip(k * x, -700.0, 700.0)
    return 1.0 / (1.0 + np.exp(-z))


def mp_interval_f(lo, hi):
    return miv.mpf([mpf(float(lo)), mpf(float(hi))])


# --------------------------------------------------------------------------
# sparse interval Taylor jets in 5 deviation variables (degree cap 9),
# used for the partial derivatives of f over the sector tubes
# --------------------------------------------------------------------------
DEG = 9
MON_LIST = []
MON_INDEX = {}


def _build_monomials():
    for a in range(DEG + 1):
        for b in range(DEG + 1 - a):
            for c in range(DEG + 1 - a - b):
                for d in range(DEG + 1 - a - b - c):
                    for e in range(DEG + 1 - a - b - c - d):
                        MON_LIST.append((a, b, c, d, e))
    for i, m in enumerate(MON_LIST):
        MON_INDEX[m] = i


_build_monomials()
NM = len(MON_LIST)
MUL_I = []
MUL_J = []
MUL_K = []
for i, mi in enumerate(MON_LIST):
    for j, mj in enumerate(MON_LIST):
        mk = tuple(mi[t] + mj[t] for t in range(5))
        if sum(mk) <= DEG:
            MUL_I.append(i)
            MUL_J.append(j)
            MUL_K.append(MON_INDEX[mk])
MUL_I = np.array(MUL_I, dtype=np.int64)
MUL_J = np.array(MUL_J, dtype=np.int64)
MUL_K = np.array(MUL_K, dtype=np.int64)


class Jet:
    """Interval-coefficient Taylor jet in 5 symbolic deviation variables.

    The coefficients are intervals enclosing the Taylor coefficients of
    the represented function over the sector tube; the deviation
    variables are formal (the truncated formal-series arithmetic computes
    the composition's Taylor coefficients to degree DEG exactly, with the
    interval widths carrying the tube variation).
    """

    __slots__ = ("lo", "hi")

    def __init__(self, lo, hi):
        self.lo = lo
        self.hi = hi

    @staticmethod
    def const(iv):
        lo = np.zeros(NM)
        hi = np.zeros(NM)
        if isinstance(iv, tuple):
            lo[0], hi[0] = iv[0], iv[1]
        else:
            lo[0] = hi[0] = iv
        return Jet(lo, hi)

    @staticmethod
    def var(k, iv):
        lo = np.zeros(NM)
        hi = np.zeros(NM)
        lo[0], hi[0] = iv[0], iv[1]
        idx = MON_INDEX[tuple(1 if t == k else 0 for t in range(5))]
        lo[idx], hi[idx] = 1.0, 1.0
        return Jet(lo, hi)

    def copy(self):
        return Jet(self.lo.copy(), self.hi.copy())

    def __add__(self, other):
        return Jet(_lo(self.lo + other.lo), _hi(self.hi + other.hi))

    def __sub__(self, other):
        return Jet(_lo(self.lo - other.hi), _hi(self.hi - other.lo))

    def __neg__(self):
        return Jet(_lo(-self.hi), _hi(-self.lo))

    def scal(self, c):
        if isinstance(c, tuple):
            clo, chi = c
        else:
            clo = chi = c
        p1 = self.lo * clo
        p2 = self.lo * chi
        p3 = self.hi * clo
        p4 = self.hi * chi
        return Jet(
            _lo(np.minimum(np.minimum(p1, p2), np.minimum(p3, p4))),
            _hi(np.maximum(np.maximum(p1, p2), np.maximum(p3, p4))))

    def mul(self, other):
        sl = self.lo[MUL_I]
        sh = self.hi[MUL_I]
        ol = other.lo[MUL_J]
        oh = other.hi[MUL_J]
        p1 = sl * ol
        p2 = sl * oh
        p3 = sh * ol
        p4 = sh * oh
        lo_s = np.minimum(np.minimum(p1, p2), np.minimum(p3, p4))
        hi_s = np.maximum(np.maximum(p1, p2), np.maximum(p3, p4))
        lo2 = np.bincount(MUL_K, weights=lo_s, minlength=NM)
        hi2 = np.bincount(MUL_K, weights=hi_s, minlength=NM)
        return Jet(_lo(lo2), _hi(hi2))

    def sup_abs(self):
        return float(np.maximum(np.abs(self.lo), np.abs(self.hi)).max())


def jet_recip(x):
    """1/x for a jet whose constant interval excludes 0: the formal
    geometric series (exact Taylor coefficients to degree DEG)."""
    c_lo, c_hi = x.lo[0], x.hi[0]
    if c_lo <= 0.0 <= c_hi:
        raise ZeroDivisionError("jet reciprocal: constant spans 0")
    inv_lo = 1.0 / c_hi if c_lo > 0 else 1.0 / c_lo
    inv_hi = 1.0 / c_lo if c_lo > 0 else 1.0 / c_hi
    d = x.copy()
    d.lo[0] = 0.0
    d.hi[0] = 0.0
    cneg = Jet.const((-inv_hi, -inv_lo))
    acc = Jet.const((1.0, 1.0))
    term = Jet.const((1.0, 1.0))
    for _ in range(DEG):
        term = term.mul(d).mul(cneg)
        acc = acc + term
    return acc.mul(Jet.const((inv_lo, inv_hi)))


def logistic_derivative_sups(kmax):
    """sup_{z in R} |sigma^{(m)}(z)| for m = 0..kmax via the Eulerian
    polynomial recurrence P_0 = p, P_{m+1} = p(1-p) P_m'(p).  The sup of
    |P_m| over p in [0,1] is bounded by exact midpoint evaluations
    (integer-coefficient polynomials, exact in mpmath) plus the local
    Lipschitz correction |P_m'|*dx/2 with |P_m'| bounded by the interval
    evaluation on each subinterval."""
    sups = []
    coefs = [mpf(0), mpf(1)]          # P_0(p) = p, ascending
    nsub = 2048
    dx = mpf(1) / nsub
    for m in range(kmax + 1):
        dcoefs = [coefs[k + 1] * (k + 1) for k in range(len(coefs) - 1)]
        best = mpf(0)
        for a in range(nsub):
            xmid = (mpf(a) + mpf(1) / 2) / nsub
            # exact midpoint value of P_m
            acc = mpf(0)
            for cc in reversed(coefs):
                acc = acc * xmid + cc
            v = abs(acc)
            # interval evaluation of P_m' on the subinterval
            x0 = mpf(a) / nsub
            x1 = mpf(a + 1) / nsub
            xi = miv.mpf([x0, x1])
            accd = miv.mpf(0)
            for cc in reversed(dcoefs):
                accd = accd * xi + miv.mpf(cc)
            dp = max(abs(accd.a), abs(accd.b))
            cand = v + dp * dx / 2
            if cand > best:
                best = cand
        sups.append(float(best))
        # next polynomial: P_{m+1} = (p - p^2) P_m'
        new = [mpf(0)] * (len(dcoefs) + 3)
        for k, cc in enumerate(dcoefs):
            new[k + 1] += cc
            new[k + 2] -= cc
        coefs = [c for c in new]
    return sups


def softplus_bound_coefs(sig_sups):
    """b_k with |d^k/dd^k softplus(d)| <= b_k * k! for k >= 1 (the
    composition chain: 10^{k-1} sigma^{(k-1)}(10 d)); b_0 handled
    separately by the monotone endpoint evaluation."""
    bs = []
    for k in range(1, DEG + 1):
        bs.append(10.0 ** (k - 1) * sig_sups[k - 1])
    return bs


def softplus_mp(x):
    """mpmath interval softplus, outward-rounded, stable."""
    xm = mp_interval_f(x[0], x[1])
    sp = miv.log(1 + miv.exp(10 * xm)) / 10
    return f64_interval(sp)


def main():
    t_start = time.time()
    box = np.load(ROOT / "c4_orbit_krawczyk_box.npz")
    u_mid = 0.5 * (box["u_lo"] + box["u_hi"])
    P = float(0.5 * (box["P_lo"] + box["P_hi"]))
    P_lo_f, P_hi_f = float(box["P_lo"]), float(box["P_hi"])

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
    P_iv = mp_interval_f(_lo(P), _hi(P))
    phi_mp = [2 * miv.pi * k * mpf(TAU) / P_iv for k in range(1, K_MAX + 1)]
    two_h_inv = f64_interval(miv.mpf(2) * M / P_iv)
    At_f64, Bt_f64 = [], []
    for k in range(K_MAX):
        cs = miv.cos(phi_mp[k])
        sn = miv.sin(phi_mp[k])
        At_f64.append(f64_interval(miv.mpf(A[k, 2]) * cs
                                   - miv.mpf(B[k, 2]) * sn))
        Bt_f64.append(f64_interval(miv.mpf(A[k, 2]) * sn
                                   + miv.mpf(B[k, 2]) * cs))

    # ---------------- roots of unity + node offsets (Stage-2 machinery)
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

    psi_re = [[None] * (n + 1) for _ in range(K_MAX)]
    psi_im = [[None] * (n + 1) for _ in range(K_MAX)]
    for k in range(1, K_MAX + 1):
        for i in range(n + 1):
            xi = miv.cos(miv.pi * (n - i) / n)
            psi = miv.pi * k * (xi + 1) / M
            psi_re[k - 1][i] = f64_interval(miv.cos(psi))
            psi_im[k - 1][i] = f64_interval(miv.sin(psi))

    print("accumulating interval node values over 80 modes ...", flush=True)
    X = [iv_pt(np.zeros((M, n + 1))) for _ in range(4)]
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
    for s in range(4):
        X[s] = iadd(X[s], c0_iv[s])

    # ---------------- interval differentiation matrix (mpmath, once)
    xi_mp = [miv.cos(miv.pi * (n - i) / n) for i in range(n + 1)]
    xi_pt = [mp.cos(mp.pi * (n - i) / n) for i in range(n + 1)]
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

    # ---------------- float points
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
    print("delay offsets + interval Lagrange weights ...", flush=True)
    tau_over_h = TAU * M / P
    u = (np.arange(M)[:, None] + (nodes[None, :] + 1.0) / 2.0) - tau_over_h
    jp = np.floor(u).astype(np.int64) % M
    frac = u - np.floor(u)
    sigma = 2.0 * frac - 1.0
    sig_lo = _lo(sigma - 1e-11)
    sig_hi = _hi(sigma + 1e-11)
    den = np.ones(n + 1)
    for l in range(n + 1):
        for m2 in range(n + 1):
            if m2 != l:
                den[l] *= (nodes[l] - nodes[m2])
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
        for m2 in range(n + 1):
            if m2 != l:
                t_lo = _lo(sig_lo - nodes[m2])
                t_hi = _hi(sig_hi - nodes[m2])
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

    # ---------------- model passes at the substrate
    print("substrate f + Jacobian passes (rho-scaled) ...", flush=True)
    f_parts, fE_finish, f_full, jac_parts, jac_finish = make_model(rho_iv)
    pt_sub = f_parts(X)
    jpt_sub = jac_parts(X)
    (Jlo_s, Jhi_s), (Dvlo_s, Dvhi_s) = jac_finish(jpt_sub, ZdLag)
    Jrow_sup = float(i_abs_hi(Jlo_s, Jhi_s).sum(axis=3).max())
    Dv3_sup = float(i_abs_hi(Dvlo_s[:, :, 3], Dvhi_s[:, :, 3]).max())

    sup_f_sub = max(
        float(i_abs_hi(pt_sub[k][0], pt_sub[k][1]).max())
        for k in ("fN", "fA", "fZ"))
    fE_sub = fE_finish(pt_sub, ZdLag)
    sup_f_sub = max(sup_f_sub,
                    float(i_abs_hi(fE_sub[0], fE_sub[1]).max()))
    lip_sup = 0.33246 * M / P
    sup_yprime = float(np.nextafter(
        sup_f_sub + lip_sup * (R_BALL + 1e-8), _PINF))
    zd_shift = float(np.nextafter(sup_yprime * dtau, _PINF))

    def zd_enclosure(delta):
        zlo = _lo(np.minimum(ZdLag[0] - delta - zd_shift, ZdLag[0]))
        zhi = _hi(np.maximum(ZdLag[1] + delta + zd_shift, ZdLag[1]))
        return (np.minimum(zlo, ZdLag[0]), np.maximum(zhi, ZdLag[1]))

    # ---------------- node-residual enclosures (Stage-3 defect machinery)
    print("node-residual enclosures (minimal inputs) ...", flush=True)
    Zdi0 = zd_enclosure(0.0)
    fE0 = fE_finish(pt_sub, Zdi0)
    F0 = [pt_sub["fN"], pt_sub["fA"], pt_sub["fZ"], fE0]

    KDsum = [np.zeros((M, 9, 2)) for _ in range(4)]
    for i in range(9):
        acc_lo = [np.zeros(M) for _ in range(4)]
        acc_hi = [np.zeros(M) for _ in range(4)]
        for ip in range(9):
            w = (KDlo[i, ip], KDhi[i, ip])
            for s in range(4):
                t = i_scal(w, (X[s][0][:, ip], X[s][1][:, ip]))
                acc_lo[s] = _lo(acc_lo[s] + t[0])
                acc_hi[s] = _hi(acc_hi[s] + t[1])
        for s in range(4):
            KDsum[s][:, i, 0] = acc_lo[s]
            KDsum[s][:, i, 1] = acc_hi[s]

    res_lo = np.zeros((M, 9, 4))
    res_hi = np.zeros((M, 9, 4))
    for i in range(9):
        for s in range(4):
            lo = KDsum[s][:, i, 0].copy()
            hi = KDsum[s][:, i, 1].copy()
            lo = _lo(lo - F0[s][1][:, i])
            hi = _hi(hi - F0[s][0][:, i])
            res_lo[:, i, s] = lo
            res_hi[:, i, s] = hi
    res_abs = i_abs_hi(res_lo, res_hi)
    node_res_sup = float(res_abs.max())

    # ---------------- the Lebesgue constant Lambda_8 (rigorous)
    print("Lebesgue constant of the Lobatto-8 interpolation ...",
          flush=True)
    KSUB_L = 512
    # (the |L_l| interval evaluations below cover each subinterval's
    # full range, so no separate Lipschitz term is required)
    lam_max = 0.0
    for a in range(KSUB_L):
        x_lo = -1.0 + 2.0 * a / KSUB_L
        x_hi = -1.0 + 2.0 * (a + 1) / KSUB_L
        tot_hi = 0.0
        for l in range(n + 1):
            # interval evaluation of L_l on [x_lo, x_hi]: the interval
            # product encloses the whole subinterval's range — no extra
            # Lipschitz term is needed
            acc = (1.0, 1.0)
            for m2 in range(n + 1):
                if m2 != l:
                    t = (_lo(x_lo - nodes[m2]), _hi(x_hi - nodes[m2]))
                    p1 = acc[0] * t[0]
                    p2 = acc[0] * t[1]
                    p3 = acc[1] * t[0]
                    p4 = acc[1] * t[1]
                    acc = (min(p1, p2, p3, p4), max(p1, p2, p3, p4))
            dl = den[l]
            if dl > 0:
                vlo = acc[0] / dl
                vhi = acc[1] / dl
            else:
                vlo = acc[1] / dl
                vhi = acc[0] / dl
            tot_hi += max(abs(vlo), abs(vhi))
        lam_max = max(lam_max, tot_hi)
    Lambda_8 = float(np.nextafter(lam_max * (1.0 + EPS_ACC), _PINF))

    # the max of the interpolation product polynomial (rigorous)
    prod_poly_coef = [mpf(1)]
    for m2 in range(n + 1):
        new = [mpf(0)] * (len(prod_poly_coef) + 1)
        for k, cc in enumerate(prod_poly_coef):
            new[k] += cc * (-xi_pt[m2])
            new[k + 1] += cc
        prod_poly_coef = new
    pp_f = [float(x) for x in prod_poly_coef]
    dx = 2.0 / KSUB_L
    max_prod = 0.0
    for a in range(KSUB_L):
        x_lo = -1.0 + 2.0 * a / KSUB_L
        x_hi = -1.0 + 2.0 * (a + 1) / KSUB_L
        v1 = float(np.polynomial.polynomial.polyval(x_lo, pp_f))
        v2 = float(np.polynomial.polynomial.polyval(x_hi, pp_f))
        max_prod = max(max_prod, abs(v1), abs(v2))
    pp_d = [pp_f[k + 1] * (k + 1) for k in range(len(pp_f) - 1)]
    max_prod = float(np.nextafter(
        max_prod + sum(abs(x) for x in pp_d) * dx / 2.0, _PINF))

    print(f"  Lambda_8 = {Lambda_8:.6f}, max|prod(x-xi)| = "
          f"{max_prod:.6e}")

    # ---------------- per-patch state-polynomial derivative bounds
    # (via the CHEBYSHEV COEFFICIENTS of the interpolant — the smooth
    #  data's cancellation is captured; the naive sum|X|*sup|L^(j)|
    #  bound overestimates by many orders)
    print("state-polynomial derivative bounds B_{v,j} "
          "(Chebyshev coefficients) ...", flush=True)
    # monomial coefficients of T_j (exact)
    Tcoef = [[mpf(1)], [mpf(0), mpf(1)], [mpf(-1), mpf(0), mpf(2)],
             [mpf(0), mpf(-3), mpf(0), mpf(4)],
             [mpf(1), mpf(0), mpf(-8), mpf(0), mpf(8)],
             [mpf(0), mpf(5), mpf(0), mpf(-20), mpf(0), mpf(16)],
             [mpf(-1), mpf(0), mpf(18), mpf(0), mpf(-48), mpf(0),
              mpf(32)],
             [mpf(0), mpf(-7), mpf(0), mpf(56), mpf(0), mpf(-112),
              mpf(0), mpf(64)],
             [mpf(1), mpf(0), mpf(-32), mpf(0), mpf(160), mpf(0),
              mpf(-256), mpf(0), mpf(128)]]
    # Csum[j][k] = sum |coefficients of T_j^{(k)}| (monomial basis)
    Csum = [[0.0] * (n + 1) for _ in range(n + 1)]
    for j in range(n + 1):
        coefs = [x for x in Tcoef[j]]
        for k in range(n + 1):
            Csum[j][k] = float(sum(abs(float(x)) for x in coefs))
            coefs = [coefs[q + 1] * (q + 1)
                     for q in range(len(coefs) - 1)]
    # the interval DCT (Chebyshev-Lobatto interpolation coefficients):
    # c_j = (2/(n*gamma_j)) * sum_l (X_l/gamma_l) cos(pi*j*l/n)
    cos_tab = np.empty((n + 1, n + 1))
    for j in range(n + 1):
        for l in range(n + 1):
            cos_tab[j, l] = float(mp.cos(mp.pi * j * l / n))
    gam = np.ones(n + 1)
    gam[0] = 2.0
    gam[n] = 2.0
    # c_j intervals per patch: (M, n+1, 4) x 2
    c_lo = np.zeros((M, n + 1, 4))
    c_hi = np.zeros((M, n + 1, 4))
    for j in range(n + 1):
        pref = 2.0 / (n * gam[j])
        acc_lo = np.zeros((M, 4))
        acc_hi = np.zeros((M, 4))
        for l in range(n + 1):
            w = pref / gam[l] * cos_tab[j, l]
            for s in range(4):
                a = X[s][0][:, l]
                b = X[s][1][:, l]
                p1 = w * a
                p2 = w * b
                plo = np.minimum(p1, p2)
                phi = np.maximum(p1, p2)
                acc_lo[:, s] = _lo(acc_lo[:, s] + plo)
                acc_hi[:, s] = _hi(acc_hi[:, s] + phi)
        c_lo[:, j, :] = acc_lo
        c_hi[:, j, :] = acc_hi
    c_abs = np.maximum(np.abs(c_lo), np.abs(c_hi))   # (M, 9, 4)
    two_h = 2.0 * M / P
    Bmat = np.zeros((M, 4, n))
    for kdeg in range(1, n + 1):
        acc = np.zeros((M, 4))
        for j in range(kdeg, n + 1):
            acc += c_abs[:, j, :] * Csum[j][kdeg]
        Bmat[:, :, kdeg - 1] = _hi(
            (two_h ** kdeg) * acc * (1.0 + EPS_ACC))
    Bz = np.zeros((M, n))
    for kdeg in range(1, n + 1):
        acc = np.zeros(M)
        for j in range(kdeg, n + 1):
            acc += c_abs[:, j, 2] * Csum[j][kdeg]
        Bz[:, kdeg - 1] = _hi(
            (two_h ** kdeg) * acc * (1.0 + EPS_ACC))
    Bz_global = Bz.max(axis=0)
    cheb_c_sup = c_abs.max(axis=0)     # (9, 4) diagnostic

    # ---------------- logistic-derivative sups + softplus coefficients
    print("logistic derivative sups (Eulerian recurrence) ...",
          flush=True)
    sig_sups = logistic_derivative_sups(DEG)
    sp_bounds = softplus_bound_coefs(sig_sups)
    print(f"  sup|sigma^(m)| m=0..{DEG}: "
          f"{[f'{x:.3e}' for x in sig_sups]}")

    # ---------------- sector tubes + f-jets
    print(f"sector tubes + interval Taylor jets of f ({N_SECTORS} "
          f"sectors) ...", flush=True)
    sector_bounds = np.zeros((N_SECTORS, NM, 4))
    sector_ranges = []
    d_range_max = 0.0
    for sec in range(N_SECTORS):
        a0 = sec * M // N_SECTORS
        b0 = (sec + 1) * M // N_SECTORS
        rng = []
        for s in range(4):
            lo = float(X[s][0][a0:b0].min()) - R_BALL - 1e-8
            hi = float(X[s][1][a0:b0].max()) + R_BALL + 1e-8
            rng.append((lo, hi))
        zlo = float(ZdLag[0][a0:b0].min()) - R_BALL - zd_shift - 1e-8
        zhi = float(ZdLag[1][a0:b0].max()) + R_BALL + zd_shift + 1e-8
        rng.append((zlo, zhi))
        sector_ranges.append(rng)

        vN = Jet.var(0, rng[0])
        vA = Jet.var(1, rng[1])
        vZ = Jet.var(2, rng[2])
        vE = Jet.var(3, rng[3])
        vZd = Jet.var(4, rng[4])
        one = Jet.const((1.0, 1.0))

        Aplus = vA + Jet.const((P4['A0'], P4['A0']))
        recip_A = jet_recip(Aplus)
        fac = one - recip_A.scal((P4['A0'], P4['A0']))
        NoverK = vN.scal((1.0 / P4['K'], 1.0 / P4['K']))
        Rj = vN.mul(one - NoverK).mul(fac).scal((P4['r'], P4['r']))
        Bj = Rj + vN.mul(fac).scal((P4['kappaA'], P4['kappaA']))
        deficit = vE.mul(vN).scal((P4['q'], P4['q'])) - Rj
        d_lo = float(deficit.lo[0])
        d_hi = float(deficit.hi[0])
        d_range_max = max(d_range_max, d_hi - d_lo)
        sp_lo, sp_hi = softplus_mp((d_lo, d_hi))
        dev = deficit.copy()
        dev.lo[0] = 0.0
        dev.hi[0] = 0.0
        mem = Jet.const((max(0.0, sp_lo), max(0.0, sp_hi)))
        term = Jet.const((1.0, 1.0))
        fact_k = 1.0
        for k in range(1, DEG + 1):
            term = term.mul(dev)
            fact_k *= k
            bk = sp_bounds[k - 1] / fact_k
            mem = mem + term.scal((-bk, bk))
        gate = one - vE.scal((1.0 / P4['Emax'], 1.0 / P4['Emax']))
        fN = Rj - vE.mul(vN).scal((P4['q'], P4['q']))
        fA = (-Bj + vA.scal((-P4['omegaA'], -P4['omegaA']))
              + Jet.const((P4['omegaA'] * P4['AeqW'],
                           P4['omegaA'] * P4['AeqW'])))
        fZ = (mem - vZ).scal((1.0 / P4['taum'], 1.0 / P4['taum']))
        ZdDref = vZd.scal((1.0 / P4['Dref'], 1.0 / P4['Dref']))
        EEmax = vE.scal((1.0 / P4['Emax'], 1.0 / P4['Emax']))
        recip_ZZ = jet_recip(vZd + Jet.const((P4['Zref'], P4['Zref'])))
        term2 = vZd.mul(recip_ZZ).scal((P4['delta0'], P4['delta0']))
        fE = gate.mul(vE.mul(ZdDref - EEmax).scal(
            (P4['eta'], P4['eta'])) + term2)
        for si, fjet in enumerate((fN, fA, fZ, fE)):
            sector_bounds[sec, :, si] = np.maximum(
                np.abs(fjet.lo), np.abs(fjet.hi))
    print(f"  jets done ({time.time()-t_start:.1f}s); max sector d-range "
          f"= {d_range_max:.3f}")

    # ---------------- the Faà di Bruno Bell DP (magnitude arithmetic)
    print("Faà di Bruno Bell DP (sector level) ...", flush=True)
    gmon = []
    for ud in range(1, DEG + 1):
        for mi in MON_LIST:
            if sum(mi) <= ud:
                gmon.append((ud,) + mi)
    gidx = {m: i for i, m in enumerate(gmon)}
    NG = len(gmon)
    # the G-support: the 45 monomials u^j t_v
    gsup = []
    for ud in range(1, DEG + 1):
        for v in range(5):
            key = (ud,) + tuple(1 if t == v else 0 for t in range(5))
            gsup.append(gidx[key])
    # the multiplication pairs (full gmon x G-support, degree-capped)
    dp_pairs = []
    for ii, gm in enumerate(gmon):
        ud_i = gm[0]
        mi = gm[1:]
        for jj in gsup:
            ud_j, mj = gmon[jj][0], gmon[jj][1:]
            ud = ud_i + ud_j
            if ud > DEG:
                continue
            mk = tuple(mi[t] + mj[t] for t in range(5))
            if sum(mk) > DEG:
                continue
            kk = gidx.get((ud,) + mk)
            if kk is not None:
                dp_pairs.append((ii, jj, kk))
    DP_I = np.array([p[0] for p in dp_pairs], dtype=np.int64)
    DP_J = np.array([p[1] for p in dp_pairs], dtype=np.int64)
    DP_K = np.array([p[2] for p in dp_pairs], dtype=np.int64)

    sec_edges = [(sec * M // N_SECTORS, (sec + 1) * M // N_SECTORS)
                 for sec in range(N_SECTORS)]
    rem9_by_sector = np.zeros(N_SECTORS)
    # the beta! factors
    bfact = np.zeros(NM)
    for mi in MON_LIST:
        fct = 1.0
        for t in mi:
            ft = 1.0
            for q in range(2, int(t) + 1):
                ft *= q
            fct *= ft
        bfact[MON_INDEX[mi]] = fct
    fsup_all = sector_bounds.max(axis=2)      # (N_SECTORS, NM)
    for sec in range(N_SECTORS):
        a0, b0 = sec_edges[sec]
        Bsec = Bmat[a0:b0].max(axis=0)        # (4, 8): orders 1..8
        Bv = np.zeros((5, DEG))               # order 9 = 0 (degree-8 p)
        Bv[0:4, :n] = Bsec
        Bv[4, :n] = Bz_global
        G_mag = np.zeros(NG)
        for ud in range(1, DEG + 1):
            fj = 1.0
            for t in range(2, ud + 1):
                fj *= t
            for v in range(5):
                key = (ud,) + tuple(1 if t == v else 0 for t in range(5))
                G_mag[gidx[key]] = Bv[v, ud - 1] / fj
        E_mag = np.zeros(NG)
        E_mag[0] = 1.0
        Tm_mag = np.zeros(NG)
        Tm_mag[0] = 1.0
        fm = 1.0
        for m in range(1, DEG + 1):
            fm *= m
            vals = Tm_mag[DP_I] * G_mag[DP_J]
            Tm_mag = np.bincount(DP_K, weights=vals, minlength=NG) / fm
            E_mag = E_mag + Tm_mag
        # r^(9) <= rho_hi * 9! * sum_beta fsup_beta * beta! * E[u^9,t^beta]
        total = 0.0
        for mi in MON_LIST:
            if sum(mi) == 0:
                continue
            kk = gidx.get((DEG,) + mi)
            if kk is None:
                continue
            ev = E_mag[kk]
            if ev == 0.0:
                continue
            total += fsup_all[sec, MON_INDEX[mi]] * bfact[MON_INDEX[mi]] \
                * ev
        rem9_by_sector[sec] = float(np.nextafter(
            rho_hi * FACT9 * total * (1.0 + EPS_ACC), _PINF))

    h_seg = P / M
    rem9_sup = float(rem9_by_sector.max())
    rem_bound = float(np.nextafter(
        rem9_sup * (h_seg / 2.0) ** DEG * max_prod / FACT9
        * (1.0 + EPS_ACC), _PINF))

    # ---------------- the between-nodes continuum defect bound
    interp_part = float(np.nextafter(
        Lambda_8 * node_res_sup * (1.0 + EPS_ACC), _PINF))
    continuum_sup = float(np.nextafter(
        (interp_part + rem_bound) * (1.0 + EPS_ACC), _PINF))
    # the node-value inflation constant for a corrected polynomial
    KDrow_sup = float(np.abs(KD_mid).sum(axis=1).max())
    C_infl = KDrow_sup + Jrow_sup + Dv3_sup * Lambda_sup

    # ---------------- the assembly measurements (float march)
    print("float assembly measurements (march) ...", flush=True)
    t_m = time.time()

    def jac_float(Xv, Zdv):
        N_, A_, Z_, E_ = Xv
        fac = A_ / (A_ + P4['A0'])
        dfac = P4['A0'] / (A_ + P4['A0']) ** 2
        R = P4['r'] * N_ * (1 - N_ / P4['K']) * fac
        RN = P4['r'] * (1 - 2 * N_ / P4['K']) * fac
        RA = P4['r'] * N_ * (1 - N_ / P4['K']) * dfac
        BN = RN + P4['kappaA'] * fac
        BA = RA + P4['kappaA'] * N_ * dfac
        deficit = P4['q'] * E_ * N_ - R
        sig = sigmoid_f(deficit)
        gate = 1 - E_ / P4['Emax']
        H = P4['eta'] * E_ * (Zdv - E_ / P4['Emax']) \
            + P4['delta0'] * Zdv / (P4['Zref'] + Zdv)
        J = np.zeros(np.shape(N_) + (4, 4))
        Dv3 = gate * (P4['eta'] * E_ / P4['Dref']
                      + P4['delta0'] * P4['Zref']
                      / (P4['Zref'] + Zdv) ** 2)
        J[..., 0, 0] = RN - P4['q'] * E_
        J[..., 0, 1] = RA
        J[..., 0, 3] = -P4['q'] * N_
        J[..., 1, 0] = -BN
        J[..., 1, 1] = -(BA + P4['omegaA'])
        J[..., 2, 0] = sig * (P4['q'] * E_ - RN) / P4['taum']
        J[..., 2, 1] = -sig * RA / P4['taum']
        J[..., 2, 2] = -1.0 / P4['taum']
        J[..., 2, 3] = sig * P4['q'] * N_ / P4['taum']
        J[..., 3, 3] = -H / P4['Emax'] + gate * P4['eta'] * (
            Zdv - 2 * E_ / P4['Emax'])
        return J, Dv3

    Jf, Dv3f = jac_float(Xpt, Zdpt)
    w_alt = np.array([(-1.0) ** i * (0.5 if i in (0, n) else 1.0)
                      for i in range(n + 1)])
    Df = np.zeros((n + 1, n + 1))
    for i in range(n + 1):
        for j in range(n + 1):
            if i != j:
                Df[i, j] = (w_alt[j] / w_alt[i]) / (nodes[i] - nodes[j])
        Df[i, i] = -Df[i].sum()
    KDf = (2.0 * M / P) * Df
    Mhat = np.zeros((M, 32, 32))
    eye4 = np.eye(4)
    for i in range(8):
        for ip in range(1, 9):
            Mhat[:, i * 4:(i + 1) * 4,
                 (ip - 1) * 4:ip * 4] = KDf[i, ip] * eye4
    for i in range(1, 8):
        Mhat[:, i * 4:(i + 1) * 4,
             (i - 1) * 4:i * 4] -= Jf[:, i, :, :]
    Rinv = np.linalg.inv(Mhat)
    Bfl = np.zeros((M, 32, 4))
    for i in range(8):
        Bfl[:, i * 4:(i + 1) * 4, :] += KDf[i, 0] * eye4
    Bfl[:, 0:4, :] -= Jf[:, 0, :, :]
    S_in = -np.einsum('mij,mjk->mik', Rinv, Bfl)
    DvB = np.zeros((M, 32, 8))
    for i in range(8):
        DvB[:, i * 4 + 3, i] = -Dv3f[:, i]
    Szd = -np.einsum('mij,mjk->mik', Rinv, DvB)
    S_out = S_in[:, 28:32, :]

    src_slot = jp % RING
    Lw_abs = np.abs(Lw_mid)
    w_xi = np.ones(4)
    w_hist = np.ones((RING, 9))
    for j in range(M):
        zdw = np.zeros(8)
        for i in range(8):
            sl = src_slot[j, i]
            zdw[i] = Lw_abs[j, i, :] @ w_hist[sl, :]
        new_xi = np.abs(S_out[j]) @ w_xi \
            + np.abs(Szd[j])[28:32, :] @ zdw
        newslot = np.empty(9)
        newslot[0] = w_xi[2]
        newslot[1:] = np.abs(S_in[j])[np.arange(8) * 4 + 2, :] @ w_xi \
            + np.abs(Szd[j])[np.arange(8) * 4 + 2, :] @ zdw
        w_xi = new_xi
        w_hist[j % RING, :] = newslot
    rho_w_growth = float(max(w_xi.max(), w_hist.max()))
    per_step = rho_w_growth ** (1.0 / M)

    Pm = np.zeros((4 + RING * 9, NB))
    Pm[0:4, 0:4] = np.eye(4)
    for t in range(99):
        pidx = M - 99 + t
        slot = pidx % RING
        Pm[4 + slot * 9:4 + slot * 9 + 9,
           4 + t * 9:4 + (t + 1) * 9] = np.eye(9)
    norms = np.empty(M + 1)
    norms[0] = 1.0
    zrows = np.arange(8) * 4 + 2
    for j in range(M):
        Zd_rows = np.empty((8, NB))
        for i in range(8):
            sl = src_slot[j, i]
            Zd_rows[i] = Lw_mid[j, i, :] @ Pm[4 + sl * 9:
                                              4 + sl * 9 + 9, :]
        dst = S_in[j] @ Pm[0:4, :] + Szd[j] @ Zd_rows
        old_z = Pm[2, :].copy()
        slot = j % RING
        Pm[4 + slot * 9 + 0, :] = old_z
        Pm[4 + slot * 9 + 1:4 + slot * 9 + 9, :] = dst[zrows, :]
        Pm[0:4, :] = dst[28:32, :]
        norms[j + 1] = np.abs(Pm).sum(axis=1).max()
    K0 = float(norms.max())
    K0_arg = int(norms.argmax())

    Mon = np.zeros((NB, NB))
    Mon[0:4, :] = Pm[0:4, :]
    for t in range(99):
        slot = (M - 99 + t) % RING
        Mon[4 + t * 9:4 + (t + 1) * 9, :] = Pm[4 + slot * 9:
                                               4 + slot * 9 + 9, :]
    ev = np.sort(np.abs(np.linalg.eigvals(Mon)))[::-1]

    tang = np.zeros(NB)
    x00 = [Xpt[s][0, 0] for s in range(4)]
    f00 = f_float([np.array(x00[0]), np.array(x00[1]),
                   np.array(x00[2]), np.array(x00[3])],
                  np.array(Zdpt[0, 0]))
    tang[0:4] = [float(v) for v in f00]
    N_, A_, Z_, E_ = Xpt
    facx = A_ / (A_ + P4['A0'])
    Rx = P4['r'] * N_ * (1 - N_ / P4['K']) * facx
    defx = P4['q'] * E_ * N_ - Rx
    memx = np.maximum(0.0, np.log1p(np.exp(np.clip(10 * defx,
                                                   -700, 700))) / 10)
    fZ_all = (memx - Z_) / P4['taum']
    for t in range(99):
        pidx = M - 99 + t
        tang[4 + t * 9:4 + (t + 1) * 9] = fZ_all[pidx, :]
    tn = float(np.linalg.norm(tang))
    tang_res = float(np.linalg.norm(Mon @ tang - tang) / tn)
    pin = int(np.argmax(np.abs(tang[0:4])))
    keep = [k for k in range(NB) if k != pin]
    A_pin = Mon[np.ix_(keep, keep)] - np.eye(NB - 1)
    Ainv_pin = np.linalg.inv(A_pin)
    q0_pin = float(np.abs(np.eye(NB - 1) - Ainv_pin @ A_pin)
                   .sum(axis=1).max())
    Ainv_norm = float(np.abs(Ainv_pin).sum(axis=1).max())
    Ab = np.zeros((NB + 1, NB + 1))
    Ab[0:NB, 0:NB] = Mon - np.eye(NB)
    Ab[0:NB, NB] = tang
    Ab[NB, 0:NB] = tang
    try:
        Ainv_b = np.linalg.inv(Ab)
        q0_b = float(np.abs(np.eye(NB + 1) - Ainv_b @ Ab)
                     .sum(axis=1).max())
        Ainv_b_norm = float(np.abs(Ainv_b).sum(axis=1).max())
    except np.linalg.LinAlgError:
        q0_b = float('nan')
        Ainv_b_norm = float('nan')

    # the float nonlinear mismatch march
    xi_cur = np.array([Xpt[s][0, 0] for s in range(4)])
    histv = np.zeros((RING, 9))
    for t in range(99):
        pidx = M - 99 + t
        histv[pidx % RING, :] = Xpt[2][pidx, :]
    for j in range(M):
        Zdv = np.empty(8)
        for i in range(8):
            sl = src_slot[j, i]
            Zdv[i] = Lw_mid[j, i, :] @ histv[sl, :]
        Xj = np.stack([Xpt[s][j, :] for s in range(4)], axis=1)
        Xn = Xj.copy()
        Xn[0, :] = xi_cur
        rhs = f_float([Xn[:, 0], Xn[:, 1], Xn[:, 2], Xn[:, 3]],
                      np.append(Zdv, 0.0))
        Fj = np.zeros(32)
        for i in range(8):
            deriv = KDf[i, :] @ Xn
            for s in range(4):
                Fj[i * 4 + s] = deriv[s] - float(rhs[s][i])
        w_j = -Rinv[j] @ Fj
        xi_new = Xj[8, :] + w_j[28:32]
        newslot = np.empty(9)
        newslot[0] = xi_cur[2]
        for i in range(1, 9):
            newslot[i] = Xj[i, 2] + w_j[(i - 1) * 4 + 2]
        histv[j % RING, :] = newslot
        xi_cur = xi_new
    mism_xi = xi_cur - np.array([Xpt[s][0, 0] for s in range(4)])
    mism_H = np.zeros((99, 9))
    for t in range(99):
        pidx = M - 99 + t
        mism_H[t] = histv[pidx % RING, :] - Xpt[2][pidx, :]
    mism = np.concatenate([mism_xi, mism_H.ravel()])
    mism_sup = float(np.abs(mism).max())
    Y_cen = float(np.abs(Ainv_pin @ mism[keep]).max())
    march_secs = time.time() - t_m

    # ---------------- verification checks
    print("verification checks ...", flush=True)
    checks = {}
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

    defect_ok = True
    for (j, i) in [(0, 0), (M // 2, 3), (M - 1, 7), (M // 3, 8)]:
        xmp = mp_node_values(j, i)
        # the delayed value via the interval Lagrange machinery's float
        # midpoint is already covered by stage-3 checks; here recompute
        uj = j + (nodes[i] + 1) / 2 - TAU * M / P
        jpf = int(np.floor(uj)) % M
        sigv = 2.0 * (uj - np.floor(uj)) - 1.0
        zdl = miv.mpf(0)
        for l in range(n + 1):
            zl = mp_node_values(jpf, l)[2]
            Ll = miv.mpf(1)
            for m2 in range(n + 1):
                if m2 != l:
                    Ll *= (miv.mpf(sigv) - miv.mpf(nodes[m2])) / (
                        miv.mpf(nodes[l] - nodes[m2]))
            zdl += Ll * zl
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
            if not (Fmp.a >= res_lo[j, i, s]
                    and Fmp.b <= res_hi[j, i, s]):
                defect_ok = False
    checks["mpmath_node_residual_contained"] = defect_ok

    # the between-nodes mpmath containment at interior points
    def mp_poly_at(j, x):
        vals = [miv.mpf(0) for _ in range(4)]
        ders = [miv.mpf(0) for _ in range(4)]
        for l in range(n + 1):
            Ll = miv.mpf(1)
            dL = miv.mpf(0)
            for m2 in range(n + 1):
                if m2 != l:
                    Ll *= (miv.mpf(x) - miv.mpf(nodes[m2])) / (
                        miv.mpf(nodes[l] - nodes[m2]))
            for m2 in range(n + 1):
                if m2 != l:
                    dL += 1 / (miv.mpf(x) - miv.mpf(nodes[m2]))
            dL *= Ll
            for s in range(4):
                xl = mp_node_values(j, l)[s]
                vals[s] += Ll * xl
                ders[s] += dL * xl
        return vals, ders

    interior_ok = True
    interior_detail = []
    for (j, x) in [(0, -0.37), (M // 3, 0.11), (M // 2, 0.63),
                   (M - 2, -0.79), (M // 7, 0.31), (M // 2, -0.55)]:
        vals, ders = mp_poly_at(j, x)
        tgrid = j + (x + 1) / 2
        ud = tgrid - TAU * M / P
        jpf = int(np.floor(ud)) % M
        sigd = 2.0 * (ud - np.floor(ud)) - 1.0
        zdl = miv.mpf(0)
        for l in range(n + 1):
            zl = mp_node_values(jpf, l)[2]
            Ll = miv.mpf(1)
            for m2 in range(n + 1):
                if m2 != l:
                    Ll *= (miv.mpf(sigd) - miv.mpf(nodes[m2])) / (
                        miv.mpf(nodes[l] - nodes[m2]))
            zdl += Ll * zl
        Nmp, Amp, Zmp, Emp = vals
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
            rmp = miv.mpf(2 * M / P) * ders[s] - miv.mpf(rho_mid) * fmp[s]
            rv = max(abs(float(rmp.a)), abs(float(rmp.b)))
            if rv > continuum_sup:
                interior_ok = False
                interior_detail.append((j, x, s, rv))
    checks["mpmath_interior_residual_within_bound"] = interior_ok
    checks["mpmath_interior_fail_detail"] = interior_detail[:6]

    checks["node_res_sup"] = node_res_sup
    checks["node_res_sup_rows_0_7"] = float(res_abs[:, 0:8, :].max())
    checks["node_res_sup_row_8"] = float(res_abs[:, 8, :].max())
    # stage-2's committed 8.326e-9 was evaluated at rho = 1 WITHOUT the
    # delay-argument shift; this stage's enclosure is uniform over the
    # rho-family and therefore carries the zd_shift * Dv3 inflation on
    # the delayed-value-dependent rows — the honest comparison bound:
    checks["stage2_crosscheck_tolerance"] = float(
        2.0 * zd_shift * Dv3_sup + 1.5e-9)
    checks["stage2_crosscheck_ok"] = bool(
        abs(float(res_abs[:, 0:8, :].max()) - 8.326e-9)
        <= 2.0 * zd_shift * Dv3_sup + 1.5e-9)

    checks["monodromy_top4"] = [float(x) for x in ev[:4]]
    phase_gap = abs(float(ev[0]) - COMMITTED_MONODROMY["phase"])
    dom_gap = abs(float(ev[1]) - COMMITTED_MONODROMY["dominant"])
    disc_gap = abs(float(ev[2]) - COMMITTED_MONODROMY["disc"])
    checks["monodromy_vs_committed_max_gap"] = float(
        max(phase_gap, dom_gap, disc_gap))
    checks["monodromy_consistent"] = bool(
        max(phase_gap, dom_gap, disc_gap) <= 1e-9)

    checks["tangent_mon_residual_rel"] = tang_res
    checks["tangent_ok"] = bool(tang_res <= 1e-6)

    # the jet validation: the linear coefficients vs the direct Jacobian
    sec_probe = N_SECTORS // 2
    a0p, b0p = sec_edges[sec_probe]
    lin_idx = [MON_INDEX[tuple(1 if t == v else 0 for t in range(5))]
               for v in range(5)]
    jet_lin = sector_bounds[sec_probe][lin_idx]     # (5, 4)
    Jcol = i_abs_hi(Jlo_s[a0p:b0p], Jhi_s[a0p:b0p])
    Jcol_sup = Jcol.max(axis=(0, 1))
    Dvcol = float(i_abs_hi(Dvlo_s[a0p:b0p, :, 3],
                           Dvhi_s[a0p:b0p, :, 3]).max())
    jet_ok = True
    for r_ in range(4):
        for c_ in range(4):
            if Jcol_sup[r_, c_] > 1e-12 and \
                    jet_lin[c_, r_] < Jcol_sup[r_, c_] * (1.0 - 1e-6) \
                    - 1e-12:
                jet_ok = False
    if jet_lin[4, 3] < Dvcol * (1.0 - 1e-6) - 1e-12:
        jet_ok = False
    checks["jet_linear_terms_cover_jacobian"] = jet_ok
    checks["jet_lin_vs_jac_max_ratio"] = float(
        (jet_lin[0:4, :] / np.maximum(Jcol_sup.T, 1e-30)).max())
    checks["jet_lin_matrix"] = jet_lin.tolist()
    checks["jcol_sup_matrix"] = Jcol_sup.tolist()
    checks["probe_sector_ranges"] = sector_ranges[sec_probe]

    checks["substrate_continuity_gap"] = cont_gap
    checks["substrate_continuity_ok"] = bool(cont_gap <= 1e-10)

    checks["lebesgue_constant"] = Lambda_8
    checks["lebesgue_ok"] = bool(1.5 <= Lambda_8 <= 6.0)

    # ---------------- the derived obstruction arithmetic (recorded)
    w_step_est = 3e-10
    direct_width_est = float(w_step_est * K0
                             / max(per_step - 1.0, 1e-30)
                             * (per_step ** M))
    n_w = 4
    L_w = M // n_w
    win_width = float(w_step_est * K0
                      * (per_step ** L_w - 1.0) / (per_step - 1.0))
    windowed_width = float(K0 ** (n_w - 1) * n_w * win_width)

    # ---------------- output
    out = {
        "title": "A1 piecewise-Chebyshev campaign — Stage 4a: the "
                 "assembly measurements, the interval-march obstruction, "
                 "and the rigorous between-nodes continuum defect bound",
        "status": "MEASUREMENTS + ONE RIGOROUS ORBIT-LEVEL BOUND — NOT "
                  "the assembly certificate: the rigorous monodromy "
                  "enclosure is blocked by the measured interval-march "
                  "width growth (needs the Stage-4b correlation-tracking "
                  "march); A1 remains COMPUTED_PARTIAL until Stage 4b "
                  "closes",
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
            "zd_shift_inflation": zd_shift,
            "declared_ball_radius": R_BALL,
            "n_sectors": N_SECTORS,
            "max_sector_deficit_range": d_range_max,
        },
        "assembly_measurements": {
            "float_monodromy_top4": [float(x) for x in ev[:4]],
            "committed_monodromy": COMMITTED_MONODROMY,
            "monodromy_max_gap_vs_committed": float(
                max(phase_gap, dom_gap, disc_gap)),
            "dichotomy_constant_K0_float": K0,
            "K0_argmax_patch": K0_arg,
            "tangent_xi_components": [float(x) for x in tang[0:4]],
            "tangent_monodromy_residual_rel": tang_res,
            "pin_coordinate": pin,
            "pinned_inverse_norm_inf": Ainv_norm,
            "pinned_inverse_q0": q0_pin,
            "bordered_inverse_norm_inf": Ainv_b_norm,
            "bordered_inverse_q0": q0_b,
            "float_mismatch_march_sup": mism_sup,
            "float_mismatch_xi": [float(x) for x in mism_xi],
            "float_Y_center_preview": Y_cen,
            "note": "the mismatch march: the one-period float composition "
                    "of the exact local Newton maps starting at the "
                    "substrate augmented state — the substrate is "
                    "essentially the periodic collocation fixed point "
                    "(the future certificate's Y-term is dominated by "
                    "enclosure widths, not the center)",
        },
        "interval_march_obstruction": {
            "width_growth_per_step": per_step,
            "per_period_growth": rho_w_growth,
            "dichotomy_K0": K0,
            "estimated_direct_interval_march_width": direct_width_est,
            "estimated_windowed_width_4win": windowed_width,
            "verdict": "the direct interval matrix march and the "
                       "windowed re-centered variant are both defeated "
                       "by the |step|-product pessimism (the measured "
                       "rate is recorded above; the true products are "
                       "dichotomy-bounded at K0 but interval arithmetic "
                       "cannot see the cancellation): the rigorous "
                       "assembly REQUIRES correlation-tracking "
                       "arithmetic — an affine/Taylor-model march with "
                       "noise symbols (Stage 4b). The measured constants "
                       "(the width-growth rate, K0, the pinned/bordered "
                       "inverse conditioning, the ~1.2e-8 mismatch "
                       "center) are the design inputs.",
        },
        "between_nodes_bound": {
            "method": "|r(x)| <= Lambda_8 * max_i |r(node_i)| + "
                      "||r^(9)||_inf * (h/2)^9 * max|prod(x-xi_i)| / 9! "
                      "per patch: the degree-8 Chebyshev-Lobatto "
                      "interpolation of the residual at the 9 nodes "
                      "(Lambda_8 = the rigorous Lebesgue constant) plus "
                      "the ninth-derivative interpolation remainder "
                      "(r^(9) = -rho (f o p)^(9) since p is degree 8; "
                      "the composition derivative bounded by the full "
                      "multivariate Faà di Bruno expansion: the "
                      "per-variable state-polynomial derivative bounds "
                      "(exact Lagrange-basis derivative coefficient "
                      "sums), the partial derivatives of f up to total "
                      "order 9 over sector tubes (interval Taylor jets, "
                      "the softplus composed via the global "
                      "logistic-derivative sup bounds from the Eulerian "
                      "recurrence), and the truncated-exponential Bell "
                      "DP in the (u, t^5) monomials at the sector "
                      "level, computed in magnitude arithmetic)",
            "node_residual_sup": node_res_sup,
            "lebesgue_constant_Lambda8": Lambda_8,
            "interp_part": interp_part,
            "rem9_sup_by_sector_max": rem9_sup,
            "remainder_part": rem_bound,
            "continuum_defect_sup": continuum_sup,
            "node8_note": "all NINE node residuals (i=0..8) are computed "
                          "directly as the substrate polynomial's own "
                          "collocation-style residuals of its patch (the "
                          "row-8 right-endpoint one-sided derivative "
                          "included; no roll, no continuity-gap inflation "
                          "needed); the substrate's inter-patch value gap "
                          f"({cont_gap:.2e}) is a separate, far smaller "
                          "effect noted in the inputs",
            "max_interp_product": max_prod,
            "chebyshev_coefficient_sups": cheb_c_sup.tolist(),
            "logistic_derivative_sups": sig_sups,
            "softplus_derivative_bound_coefs": sp_bounds,
            "statement": f"for every patch, every t in the CLOSED patch "
                         f"interval, every rho in [{rho_lo:.15f}, "
                         f"{rho_hi:.15f}], and every state s: "
                         f"|p'(t) - rho f(p(t), p(t-tau/rho))| "
                         f"<= {continuum_sup:.4e} — the rigorous "
                         f"continuum DDE defect of the substrate "
                         f"piecewise polynomial (nodes and interiors "
                         f"alike)",
            "inflation_constant_note": "for a corrected polynomial with "
                                       "node values within r_ball of "
                                       "the substrate: the node-residual "
                                       "part inflates by at most "
                                       "C_infl * r_ball with C_infl = "
                                       "KDrow_sup + Jrow_sup + Dv3_sup * "
                                       f"Lambda_sup = {C_infl:.1f} "
                                       f"(at the declared r_ball={R_BALL:g}: "
                                       f"{C_infl * R_BALL:.3e}); the "
                                       "remainder part is already "
                                       "computed over the r_ball-inflated "
                                       "sector tubes",
            "C_infl": C_infl,
            "KDrow_sup": KDrow_sup,
            "Jrow_sup": Jrow_sup,
            "Dv3_sup": Dv3_sup,
            "Lambda_sup": Lambda_sup,
            "substrate_continuity_gap": cont_gap,
        },
        "verification": checks,
        "stage4a_verdict": {},
    }

    out["stage4a_verdict"] = {
        "measurements": (
            f"the delay-augmented collocation monodromy is reconstructed "
            f"independently and matches the committed Stage-3 preview to "
            f"{max(phase_gap, dom_gap, disc_gap):.1e}; the float "
            f"dichotomy constant K_0 = {K0:.1f} (argmax patch {K0_arg}); "
            f"the phase-pinned inverse has ||A_pin^-1||_inf = "
            f"{Ainv_norm:.1f} (q0 = {q0_pin:.1e}; the bordered variant "
            f"{Ainv_b_norm:.1f}); the one-period float mismatch march "
            f"gives ||Psi(u*) - u*||_inf = {mism_sup:.3e} — the "
            f"substrate is essentially the periodic collocation fixed "
            f"point"),
        "obstruction": (
            f"the interval matrix march is measured dead: the |step| "
            f"width-growth is {per_step:.6f}/step "
            f"({rho_w_growth:.2e} per period); with K_0 = {K0:.0f} and "
            f"the per-step enclosure widths the direct march accumulates "
            f"width ~{direct_width_est:.1e} and the 4-window variant "
            f"~{windowed_width:.1e} — the Stage-4b assembly must carry "
            f"the phase correlation explicitly (affine/Taylor-model "
            f"arithmetic with noise symbols)"),
        "rigorous_result": (
            f"THE BETWEEN-NODES CONTINUUM DEFECT BOUND (rigorous, "
            f"uniform over the rho-family): sup_t |p' - rho f(p, "
            f"p_delayed)| <= {continuum_sup:.4e} — the node-residual "
            f"part {node_res_sup:.3e} x Lambda_8 {Lambda_8:.3f} = "
            f"{interp_part:.3e} plus the Faà di Bruno ninth-derivative "
            f"remainder {rem_bound:.3e}"),
        "next_stage": [
            "Stage 4b: the correlation-tracking (affine/Taylor-model) "
            "march — the rigorous monodromy enclosure via noise symbols, "
            "the pinned-bootstrap Z-term, the mismatch Y-term, the "
            "patch-to-patch assembly certificate, and the continuum "
            "orbit certificate (the A1 gate), consuming this stage's "
            "epsilon-bound and measured constants",
        ],
        "honesty": "Stage 4a measures the assembly structure, records "
                   "the interval-arithmetic obstruction with its "
                   "measured constants, and proves ONE rigorous "
                   "orbit-level bound (the continuum defect of the "
                   "substrate polynomial, valid over the whole period "
                   "and the rho-family). It certifies no solution "
                   "existence and upgrades no theorem status — the "
                   "assembly, the bootstrap, and the continuum lift "
                   "remain open (Stage 4b). A1 remains COMPUTED_PARTIAL.",
    }

    dst = ROOT / "c4_piecewise_chebyshev_stage4a.json"
    dst.write_text(json.dumps(out, indent=2))
    print(f"wrote {dst.name}")

    npz = ROOT / "c4_piecewise_chebyshev_stage4a.npz"
    arrays = {
        "res_abs_patch_sup": res_abs.max(axis=(1, 2)),
        "B_state": Bmat,
        "B_delayed": Bz,
        "rem9_by_sector": rem9_by_sector,
        "norms_profile": norms[::max(1, M // 2000)],
        "monodromy_top12": ev[:12],
        "tangent": tang,
        "sha_res": sha256_of_array(res_abs),
        "sha_B": sha256_of_array(Bmat),
    }
    np.savez_compressed(npz, **arrays)
    print(f"wrote {npz.name}")

    print(f"\nperiod P = {P:.6f}, M = {M}, degree = {n}")
    print(f"monodromy top 4: {[float(x) for x in ev[:4]]}")
    print(f"K_0 = {K0:.2f} (patch {K0_arg}); rho_w/step = "
          f"{per_step:.6f}")
    print(f"pinned: ||Ainv|| = {Ainv_norm:.1f}, q0 = {q0_pin:.1e}; "
          f"bordered: {Ainv_b_norm:.1f}")
    print(f"float mismatch sup = {mism_sup:.3e}, Y-center = "
          f"{Y_cen:.3e}")
    print(f"node residual sup = {node_res_sup:.4e} (stage2 committed "
          f"8.326e-9)")
    print(f"Lambda_8 = {Lambda_8:.4f}; rem9 sup = {rem9_sup:.3e}; "
          f"remainder = {rem_bound:.4e}")
    print(f"CONTINUUM DEFECT SUP = {continuum_sup:.4e}")
    ok_all = all(bool(v) for k, v in checks.items()
                 if isinstance(v, bool))
    print(f"all boolean checks pass: {ok_all}")
    print(f"total runtime {time.time() - t_start:.1f} s")


if __name__ == "__main__":
    main()

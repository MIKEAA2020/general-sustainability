#!/usr/bin/env python3
"""B4 continuum transfer — STAGE T2: the binding-block stable-complement
PRODUCT CERTIFICATE (the deflated n-period affine march).

Certifies, in the 4b affine noise-symbol arithmetic (point-tight stage-
matrix widths, block-wrapped magnitude accumulation, signed column
propagation), the interval enclosure of the DEFLATED n-period evolution

    S_int^n = (Mon * D)^n  +  Delta_n,     D = I - t t^T,

of the collocation system's monodromy (Mon: the committed float one-period
monodromy, cross-checked against the committed Stage-4b JSON; t: the
certified tangent, ||Mon t - t||/||t|| ~ 3.3e-8), for n = 1..40 periods.
The deflation D is applied to the input of every period (the graph-
transform normal evolution; the tangent-orthogonal realization of the
stable complement), the carried noise is deflated SIGNED (sharp) at each
period boundary and rewrapped into per-coordinate extents (the 4b block-
wrap pattern at period granularity), and the fresh injections are the
point-tight interval evaluation widths excited by the total column
magnitudes (the unit-ball worst case).

Output per period: the float center norm rowsum_r |(Mon D)^p| and the
noise extents ext_p[r]; the certificate

    ||S_int^p||_inf <= max_r ( rowsum_r |(Mon D)^p| + ext_p[r] ).

HONESTY: this certifies the COLLOCATION system's stable-complement product
with its interval evaluation uncertainty — closing, in interval arithmetic,
the first unsoundness channel of the committed discrete evidence (the
discretized binding projections). The operator-level continuum lift (the
true DDE variational monodromy vs the collocation monodromy) is NOT
enclosed here; the solution-level lift is the committed Stage-4d
certificate. The A1-4c discipline applies: the claim is exactly what the
machinery certifies.

[Setup machinery identical to the committed Stage-4b:]


[Original Stage-4b header: the correlation-tracking
(block-wrapped affine noise-symbol) march, the rigorous monodromy enclosure,
and the PERIODIC COLLOCATION FIXED-POINT CERTIFICATE (the bordered assembly
with the period perturbation as the bordering unknown).

Deliverables:

(1) THE CORRELATION-TRACKING AFFINE MARCH (the Stage-4a obstruction's
    prescribed fix): the operator columns (the unit basis + the p-column)
    are marched by the SIGNED float stage matrices (the dichotomy
    cancellation preserved), while the interval stage matrices' evaluation
    widths and the tube (r-ball) Jacobian widths are injected as FRESH
    NOISE SYMBOLS, block-aggregated: within each block of BLOCK steps the
    injections are accumulated by the magnitude march (the measured
    in-block pessimism 1.00264^BLOCK, paid ONCE per block — never
    compounded across blocks), and at the block boundary the accumulated
    box enters as 895 fresh coordinate symbols whose coefficients again
    propagate SIGNED.  The per-step |P|-pessimism rate 1.00264/step (1.5e9
    per period) that kills the direct interval march is thereby confined
    to the intra-block accumulation.

(2) THE RIGOROUS MONODROMY ENCLOSURE: the float monodromy (validated
    against the committed preview) plus the additive extent vector
    T_op(r) (the noise-symbol zonotope's row-sum extent) — the enclosure
    Mon_int = Mon_float + [-T_op, T_op] covering the rho-family
    (|rho-1| <= 2.7e-11, carried in the stage-matrix widths) and the
    r-ball tube (the Jacobian widths on the inflated node tubes).

(3) THE MISMATCH ENCLOSURE (the Y-term center): the one-period composition
    of the exact local Newton maps evaluated in mpmath (dps 30) — the
    center reproduces the Stage-4a float mismatch (1.185e-8) with the
    float rounding eliminated — plus its own affine noise-symbol widths.

(4) THE BORDERED ASSEMBLY CERTIFICATE: the joint system in (delta, p)
    (the augmented-state correction and the period perturbation),
        F(delta, p) = ( Psi_{P+p}(u_hat + delta) - u_hat - delta,
                        t_hat . delta ),
    with the bordering column dPsi/dp (marched in float with the
    (a)-formulation's exact derivative structures: KD = 2M/P
    P-INDEPENDENT, drho/dp scaling the rhs/Jacobian, dLw/dsigma *
    dsigma/dp at the delay landings (indexed by the landing PATCH),
    dRinv/dp = -Rinv dMhat/dp Rinv) and the phase pin t_hat.delta = 0.
    The Krawczyk operator with the float bordered inverse R (||R||_inf
    ~ 254, the Stage-4a measured conditioning) closes on the ball B(0,r)
    when  Y + Z(r) * r <= r,  Y = ||R F(0)|| (the preconditioned
    mismatch), Z(r) = q0 + || |R| T_op(r) ||.  Closure ==> THE EXACT
    PERIODIC COLLOCATION SOLUTION EXISTS: a fixed point of the one-period
    local-Newton map at a period P + p* with |p*| <= r, within r of the
    substrate (sup-norm, the augmented state).

Verification (all must pass): the float monodromy vs the committed
preview eigenvalues; the tangent residual; the mismatch center vs the
Stage-4a float value; the bordered inverse Neumann residual; the
p-column vs a centered finite difference of the parameterized map; the
magnitude-vs-signed unit-propagation check of the block machinery; the
mpmath probe-column containment; the Krawczyk closure inequality.

Honesty: what this certifies is the DISCRETE fixed point (the exact
periodic collocation solution of the marching system at a period within
the certified p-ball).  The continuum orbit-to-solution lift (the
function-space resolvent applied to the Stage-4a between-nodes defect
bound) remains the recorded next step (Stage 4c).  A1's theorem status is
NOT promoted by this file alone.

Deterministic; no randomness; no timing fields in the JSON.
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
    cheb_lobatto, iv_pt, make_model, f64_interval,
    i_abs_hi, iadd, imul, i_scal, isub, i_div,
    _lo, _hi, _NINF, _PINF,
)

EPS_F = 2.220446049250313e-16
EPS_ACC = 40 * EPS_F
mpF = mpf

M_SEG = 8000
CHEB_DEGREE = 8
N = CHEB_DEGREE
RING = 100
NB = 4 + 99 * 9          # 895: the augmented state
NR = 4 + RING * 9        # 904: the full ring buffer (march state)

def ring_to_state_rows(Mat):
    """Project ring rows (NR, k) to the augmented-state rows (NB, k)."""
    out = np.zeros((NB, Mat.shape[1]))
    out[0:4, :] = Mat[0:4, :]
    for t in range(99):
        slot = (M_SEG - 99 + t) % RING
        out[4 + t * 9:4 + (t + 1) * 9, :] = \
            Mat[4 + slot * 9:4 + slot * 9 + 9, :]
    return out


def state_to_ring_rows(Mat):
    """Embed augmented-state rows (NB, k) into the ring rows (NR, k)
    (slot 0 left at zero — never read before written)."""
    out = np.zeros((NR, Mat.shape[1]))
    out[0:4, :] = Mat[0:4, :]
    for t in range(99):
        slot = (M_SEG - 99 + t) % RING
        out[4 + slot * 9:4 + slot * 9 + 9, :] = \
            Mat[4 + t * 9:4 + (t + 1) * 9, :]
    return out
ZROWS = np.arange(8) * 4 + 2
BLOCK = 500
COMMITTED_MONODROMY = {"phase": 1.0000000000028728,
                       "dominant": 0.6876928141092927,
                       "disc": 0.30271822276116467}
STAGE4A_FLOAT_MISMATCH = 1.1846054803754669e-08
R_LADDER = [3e-5, 1e-5, 3e-6, 1e-6, 3e-7]


def sha256_of_array(a):
    return hashlib.sha256(np.ascontiguousarray(a).tobytes()).hexdigest()[:16]


def f_rhs_float(Xv, Zdv):
    """Unscaled float rhs at point values (Xv: 4 arrays, Zdv: array)."""
    N_, A_, Z_, E_ = Xv
    fac = A_ / (A_ + P4['A0'])
    R = P4['r'] * N_ * (1 - N_ / P4['K']) * fac
    B = R + P4['kappaA'] * N_ * fac
    deficit = P4['q'] * E_ * N_ - R
    mem = np.maximum(0.0, np.log1p(np.exp(np.clip(10 * deficit,
                                                  -700, 700))) / 10)
    gate = 1 - E_ / P4['Emax']
    fN = R - P4['q'] * E_ * N_
    fA = -B + P4['omegaA'] * (P4['AeqW'] - A_)
    fZ = (mem - Z_) / P4['taum']
    fE = gate * (P4['eta'] * E_ * (Zdv / P4['Dref'] - E_ / P4['Emax'])
                 + P4['delta0'] * Zdv / (P4['Zref'] + Zdv))
    return [fN, fA, fZ, fE]


CKPT = ROOT / "c4_piecewise_chebyshev_stage4b_ckpt.npz"


def main():
    t_start = time.time()
    phase = sys.argv[1] if len(sys.argv) > 1 else "all"
    box = np.load(ROOT / "c4_orbit_krawczyk_box.npz")
    u_mid = 0.5 * (box["u_lo"] + box["u_hi"])
    P = float(0.5 * (box["P_lo"] + box["P_hi"]))
    P_lo_f, P_hi_f = float(box["P_lo"]), float(box["P_hi"])

    rho_hull = miv.mpf([miv.mpf(P_lo_f) / miv.mpf(P),
                        miv.mpf(P_hi_f) / miv.mpf(P)])
    rho_lo, rho_hi = f64_interval(rho_hull)
    rho_iv = (rho_lo, rho_hi)
    d_rho = max(abs(1.0 - rho_lo), abs(rho_hi - 1.0))

    # ---------------- Fourier coefficients of the 161-point orbit
    c = np.fft.fft(u_mid, axis=0) / N_NODES
    c0_re = c[0].real.copy()
    A = np.stack([c[k].real + c[N_NODES - k].real
                  for k in range(1, K_MAX + 1)])
    B = np.stack([c[N_NODES - k].imag - c[k].imag
                  for k in range(1, K_MAX + 1)])

    n = CHEB_DEGREE
    nodes = cheb_lobatto(n)
    M = M_SEG

    # ---------------- P-dependent constants (mpmath)
    P_iv = miv.mpf([mpf(_lo(P)), mpf(_hi(P))])
    two_h_inv = f64_interval(miv.mpf(2) * M / P_iv)
    dKD_scale = float(2 * M / P / P)
    d_rho_dp = 1.0 / P

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
    A_iv = [[iv_pt(A[k, s]) for s in range(4)] for k in range(K_MAX)]
    B_iv = [[iv_pt(B[k, s]) for s in range(4)] for k in range(K_MAX)]
    c0_iv = [iv_pt(c0_re[s]) for s in range(4)]
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
    KD_w = 0.5 * (KDhi - KDlo)
    D_mid = 0.5 * (Dlo + Dhi)

    # ---------------- float node points (the substrate)
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

    # ---------------- Lagrange machinery at the delay offsets
    # sigma enclosed to f64 ulp width: the p-dependence is carried
    # SIGNED by the p-column (dLw/dsigma * dsigma/dp), so the sigma
    # interval only covers the arithmetic rounding.
    print("delay offsets + interval Lagrange weights ...", flush=True)
    tau_over_h = f64_interval(miv.mpf(TAU) * M / P_iv)
    tau_over_h_mid = 0.5 * (tau_over_h[0] + tau_over_h[1])
    u_off = (np.arange(M)[:, None]
             + (nodes[None, :] + 1.0) / 2.0) - tau_over_h_mid
    jp = np.floor(u_off).astype(np.int64) % M
    frac = u_off - np.floor(u_off)
    sigma = 2.0 * frac - 1.0
    sig_lo = _lo(sigma - 4 * EPS_F)
    sig_hi = _hi(sigma + 4 * EPS_F)
    dsig_dp = float(2 * TAU * M / (P * P))

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
    Lw_mid = 0.5 * (Llo + Lhi)
    Lw_w = 0.5 * (Lhi - Llo)
    Lw_abs = np.abs(Lw_mid) + Lw_w
    dLw_dsig = np.empty((M, n + 1, n + 1))
    for l in range(n + 1):
        acc = np.zeros((M, n + 1))
        for m2 in range(n + 1):
            if m2 != l:
                acc += 1.0 / (sigma - nodes[m2])
        dLw_dsig[:, :, l] = Lw_mid[:, :, l] * acc

    src_slot = jp % RING

    # ---------------- point-tight interval model at the substrate
    print("substrate f + Jacobian passes (rho-scaled, point-tight) ...",
          flush=True)
    f_parts, fE_finish, f_full, jac_parts, jac_finish = make_model(rho_iv)
    X_pt_iv = [iv_pt(Xpt[s]) for s in range(4)]
    pt_sub = f_parts(X_pt_iv)
    jpt_sub = jac_parts(X_pt_iv)
    ZdL_lo = np.zeros((M, n + 1))
    ZdL_hi = np.zeros((M, n + 1))
    for l in range(n + 1):
        xz_lo, xz_hi = iv_pt(Xpt[2][jp, l])
        term = imul((Llo[:, :, l], Lhi[:, :, l]), (xz_lo, xz_hi))
        ZdL_lo = _lo(ZdL_lo + term[0])
        ZdL_hi = _hi(ZdL_hi + term[1])
    ZdLag = (ZdL_lo, ZdL_hi)
    (Jlo_s, Jhi_s), (Dvlo_s, Dvhi_s) = jac_finish(jpt_sub, ZdLag)
    Jmid = 0.5 * (Jlo_s + Jhi_s)
    Jwid = 0.5 * (Jhi_s - Jlo_s)
    Dv3_mid = 0.5 * (Dvlo_s[:, :, 3] + Dvhi_s[:, :, 3])
    Dv3_w = 0.5 * (Dvhi_s[:, :, 3] - Dvlo_s[:, :, 3])
    fsub = f_rhs_float(Xpt, Zdpt)

    # ---------------- stage matrices + refined inverses + widths
    print("assembling stage matrices, refined inverses, widths ...",
          flush=True)
    Mhat = np.zeros((M, 32, 32))
    eye4 = np.eye(4)
    for i in range(8):
        for ip in range(1, 9):
            Mhat[:, i * 4:(i + 1) * 4,
                 (ip - 1) * 4:ip * 4] = KD_mid[i, ip] * eye4
    for i in range(1, 8):
        Mhat[:, i * 4:(i + 1) * 4,
             (i - 1) * 4:i * 4] -= Jmid[:, i, :, :]
    Rinv0 = np.linalg.inv(Mhat)
    RA = np.einsum('mij,mjk->mik', Mhat, Rinv0)
    Rinv = np.einsum('mij,mjk->mik', Rinv0, 2 * np.eye(32)[None] - RA)

    # rigorous residual ||I - Rinv Mhat_int||_inf per patch (interval)
    # Mhat_int's entry widths (conservative: each row's entries widened
    # by that row's total width sum / 2)
    wq = np.zeros((M, 32))
    for i in range(8):
        for ip in range(1, 9):
            wq[:, i * 4:(i + 1) * 4] += 0.5 * KD_w[i, ip]
    for i in range(1, 8):
        wq[:, i * 4:(i + 1) * 4] += Jwid[:, i, :, :].sum(axis=2)
    q0_rows = np.empty(M)
    E_abs = np.empty((M, 32, 32))
    chunk = 500
    ones3232 = np.ones((1, 32, 32))
    for a in range(0, M, chunk):
        b_ = min(a + chunk, M)
        Rm = Rinv[a:b_]
        Mlo = Mhat[a:b_] - 0.5 * wq[a:b_:, :, None] * ones3232
        Mhi_ = Mhat[a:b_] + 0.5 * wq[a:b_:, :, None] * ones3232
        pl = np.where(Rm[:, :, :, None] >= 0,
                      Rm[:, :, :, None] * Mlo[:, None, :, :],
                      Rm[:, :, :, None] * Mhi_[:, None, :, :])
        ph = np.where(Rm[:, :, :, None] >= 0,
                      Rm[:, :, :, None] * Mhi_[:, None, :, :],
                      Rm[:, :, :, None] * Mlo[:, None, :, :])
        sl = pl.sum(axis=2)
        sh = ph.sum(axis=2)
        eye32 = np.eye(32)[None, :, :]
        sl = _lo(sl - eye32)
        sh = _hi(sh - eye32)
        E_abs[a:b_] = np.maximum(np.abs(sl), np.abs(sh))
        rsum = E_abs[a:b_].sum(axis=2)
        q0_rows[a:b_] = _hi((rsum + EPS_ACC * rsum).max(axis=1))
    q0 = float(q0_rows.max())
    R_rows = np.abs(Rinv).sum(axis=2)              # (M, 32)
    R_norm_rows = _hi(R_rows.max(axis=1) * (1.0 + EPS_ACC))   # (M,)
    R_norm = float(R_norm_rows.max())
    q_total_rows = _hi((q0_rows + R_norm_rows * wq.max(axis=1))
                       * (1.0 + EPS_ACC))          # (M,)
    q_total_sup = float(q_total_rows.max())
    rad_Rinv_row = _hi(
        R_rows
        * (q_total_rows / np.maximum(1.0 - q_total_rows, 1e-12))[:, None]
        * (1.0 + EPS_ACC))                        # (M, 32)
    rad_Rinv_sup = float(rad_Rinv_row.max())

    # S_in, S_zd (float) + rigorous additive width bounds
    Bfl = np.zeros((M, 32, 4))
    for i in range(8):
        Bfl[:, i * 4:(i + 1) * 4, :] += KD_mid[i, 0] * eye4
    Bfl[:, 0:4, :] -= Jmid[:, 0, :, :]
    S_in = -np.einsum('mij,mjk->mik', Rinv, Bfl)
    DvB = np.zeros((M, 32, 8))
    for i in range(8):
        DvB[:, i * 4 + 3, i] = -Dv3_mid[:, i]
    Szd = -np.einsum('mij,mjk->mik', Rinv, DvB)
    S_out = S_in[:, 28:32, :]

    Bfl_abs = np.zeros((M, 32, 4))
    for i in range(8):
        Bfl_abs[:, i * 4:(i + 1) * 4, :] += (np.abs(KD_mid[i, 0])
                                              + 0.5 * KD_w[i, 0]) * eye4
    J0_abs = i_abs_hi(Jlo_s[:, 0, :, :], Jhi_s[:, 0, :, :]).sum(axis=2)
    for s in range(4):
        Bfl_abs[:, s, s] += J0_abs[:, s]
    Bfl_w = np.zeros((M, 32, 4))
    for i in range(8):
        Bfl_w[:, i * 4:(i + 1) * 4, :] += 0.5 * KD_w[i, 0] * eye4
    Bfl_w[:, 0:4, 0:4] += Jwid[:, 0, :, :]
    Dv3_abs = i_abs_hi(Dvlo_s[:, :, 3], Dvhi_s[:, :, 3])
    # THE ENTRY-WISE INVERSE-UNCERTAINTY PROPAGATION (the ~3000x tighter
    # replacement for the row-sum rad(Rinv) bound):
    #   S_int = -Rinv (I-E)^{-1} Bfl_int,  E = I - Rinv Mhat_int
    #   rad(S)[i,j] <= sum_k |Rinv[i,k]| WB[k,j]
    #               + sum_k (|Rinv| E_abs)[i,k] (|Bfl|+WB)[k,j] / (1-q)
    Bfl_abs_hi = np.zeros((M, 32, 4))
    for i in range(8):
        Bfl_abs_hi[:, i * 4:(i + 1) * 4, :] = \
            (np.abs(KD_mid[i, 0]) + 0.5 * KD_w[i, 0]) * eye4
    for s in range(4):
        Bfl_abs_hi[:, s, s] += J0_abs[:, s]
    Bfl_abs_hi = np.maximum(Bfl_abs_hi, Bfl_abs)
    inv_factor = 1.0 / np.maximum(1.0 - q_total_rows, 1e-12)   # (M,)
    RE = np.einsum('mik,mkj->mij', np.abs(Rinv), E_abs)       # (M,32,32)
    rad_sin_full = _hi(
        np.einsum('mik,mkj->mij', np.abs(Rinv), Bfl_w)
        + np.einsum('mik,mkj->mij', RE, Bfl_abs_hi + Bfl_w)
        * inv_factor[:, None, None])
    DvBw = np.zeros((M, 32, 8))
    DvBa = np.zeros((M, 32, 8))
    for i in range(8):
        DvBw[:, i * 4 + 3, i] = Dv3_w[:, i]
        DvBa[:, i * 4 + 3, i] = Dv3_abs[:, i]
    rad_szd_full = _hi(
        np.einsum('mik,mkj->mij', np.abs(Rinv), DvBw)
        + np.einsum('mik,mkj->mij', RE, DvBa + DvBw)
        * inv_factor[:, None, None])

    # ---------------- the substrate's augmented state + the p-affine part
    print("substrate augmented state + p-column affine pieces ...",
          flush=True)
    xi_sub = np.stack([Xpt[s][:, 0] for s in range(4)], axis=1)
    H_sub = Xpt[2]
    Xstack = np.stack([Xpt[s] for s in range(4)], axis=1)  # (M, 9, 4)
    F_sub = np.zeros((M, 32))
    for i in range(8):
        deriv_i = np.einsum('p,msp->ms', KD_mid[i, 1:9],
                            Xstack[:, :, 1:9])
        deriv_i = deriv_i + KD_mid[i, 0] * xi_sub
        for s in range(4):
            F_sub[:, i * 4 + s] = deriv_i[:, s] - fsub[s][:, i]
    F_sup = float(np.abs(F_sub).max())
    # the (a)-formulation (the Stage-3 rho-family): the collocation on
    # the FIXED grid [0, P]: KD = 2M/P is P-INDEPENDENT; the p-family
    # enters ONLY through rho = (P+p)/P scaling the rhs/Jacobian and the
    # delay offsets tau*M/(P+p): dMhat/dp = -(d rho/dp) J-blocks only
    dMhat = np.zeros((M, 32, 32))
    for i in range(1, 8):
        dMhat[:, i * 4:(i + 1) * 4,
              (i - 1) * 4:i * 4] -= Jmid[:, i, :, :] * d_rho_dp
    dRinv = -np.einsum('mij,mjk,mkl->mil', Rinv, dMhat, Rinv)
    ZdP = np.zeros((M, 8))
    for j in range(M):
        for i in range(8):
            # the landing PATCH (jp), not the ring slot (jp % RING): the
            # substrate history rows of Xpt[2] are indexed by patch
            # 0..M-1; indexing by the ring slot read the WRONG patch for
            # every landing patch >= 100 (98% of steps), corrupting the
            # p-column's phase (A-state) component -- caught by the
            # p-column finite-difference check (rel_gap 0.354, exactly
            # one coordinate: xi[1])
            ZdP[j, i] = (dLw_dsig[j, i, :] * dsig_dp) @ H_sub[jp[j, i]]
    F_p = np.zeros((M, 32))
    for i in range(8):
        for s in range(4):
            F_p[:, i * 4 + s] = - d_rho_dp * fsub[s][:, i]
        F_p[:, i * 4 + 3] -= Dv3_mid[:, i] * ZdP[:, i]
    w_p = -(np.einsum('mij,mj->mi', dRinv, F_sub)
            + np.einsum('mij,mj->mi', Rinv, F_p))

    # ---------------- float marches: monodromy, tangent, p-column
    print("float marches (monodromy, tangent, p-column) ...", flush=True)
    Pm = np.zeros((NR, NB))
    Pm[0:4, 0:4] = np.eye(4)
    for t in range(99):
        pidx = M - 99 + t
        slot = pidx % RING
        Pm[4 + slot * 9:4 + slot * 9 + 9,
           4 + t * 9:4 + (t + 1) * 9] = np.eye(9)
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
        Pm[4 + slot * 9 + 1:4 + slot * 9 + 9, :] = dst[ZROWS, :]
        Pm[0:4, :] = dst[28:32, :]
    Mon = ring_to_state_rows(Pm)
    ev = np.sort(np.abs(np.linalg.eigvals(Mon)))[::-1]

    tang = np.zeros(NB)
    x00 = [Xpt[s][0, 0] for s in range(4)]
    f00 = f_rhs_float([np.array(x00[0]), np.array(x00[1]),
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

    # the p-column: A_p(j+1) = P_j A_p(j) + w_p  (the per-step affine
    # injection w_p carries ALL fixed-state p-dependence: dRinv, the
    # rho-scaled rhs, and the landing movement through the residual's
    # Dv3 . ZdP channel; the ring slots' own p-columns propagate through
    # the linear part)
    Ap_ring = np.zeros(NR)
    for j in range(M):
        Zd_p_lin = np.empty(8)
        for i in range(8):
            sl = src_slot[j, i]
            Zd_p_lin[i] = Lw_mid[j, i, :] @ Ap_ring[4 + sl * 9:
                                                    4 + sl * 9 + 9]
        dst = S_in[j] @ Ap_ring[0:4] + Szd[j] @ Zd_p_lin
        aff = w_p[j]
        old_z = Ap_ring[2]
        slot = j % RING
        new_state = Ap_ring.copy()
        new_state[0:4] = dst[28:32] + aff[28:32]
        newslot = np.empty(9)
        newslot[0] = old_z
        newslot[1:9] = dst[ZROWS] + aff[ZROWS]
        new_state[4 + slot * 9:4 + slot * 9 + 9] = newslot
        Ap_ring = new_state
    Ap = ring_to_state_rows(Ap_ring[:, None])[:, 0]

    Bmat = np.zeros((NB + 1, NB + 1))
    Bmat[0:NB, 0:NB] = Mon - np.eye(NB)
    Bmat[0:NB, NB] = Ap
    Bmat[NB, 0:NB] = tang
    Rb = np.linalg.inv(Bmat)
    q0_b = float(np.abs(np.eye(NB + 1) - Rb @ Bmat).sum(axis=1).max())
    Rb_norm = float(np.abs(Rb).sum(axis=1).max())

    # ---------------- THE AFFINE OPERATOR MARCH (block-wrapped symbols)
    print("affine operator march machinery ...", flush=True)
    sin_abs = np.abs(S_in)
    sout_abs = np.abs(S_out)
    szd_abs = np.abs(Szd)
    # the per-entry width blocks used by the injections:
    #   the xi-output rows (28:32) and the Z-rows of the new slot
    rso_b = rad_sin_full[:, 28:32, :]          # (M, 4, 4)
    rsz_b = rad_sin_full[:, ZROWS, :]           # (M, 8, 4)
    zso_b = rad_szd_full[:, 28:32, :]           # (M, 4, 8)
    zsz_b = rad_szd_full[:, ZROWS, :]            # (M, 8, 8)

    def operator_march(rad_tube_sin, rad_tube_szd, rad_tube_b, r_p):
        """The block-wrapped affine operator march. rad_tube_* may be
        None (the eval-only pass); r_p = the p-symbol amplitude (the
        ball radius; 0 for the eval-only pass).  Returns (Mon_cols,
        Ap_final, T_unc): the marched unit columns (= the float
        monodromy), the marched p-column, and the additive extent
        covering BOTH the monodromy's and the p-column's uncertainty
        (the p-column's coefficients are bounded by the same
        per-coordinate injection extents — conservative and valid)."""
        C = np.zeros((NR, NB + 1))
        C[0:4, 0:4] = np.eye(4)
        for t in range(99):
            pidx = M - 99 + t
            slot = pidx % RING
            C[4 + slot * 9:4 + slot * 9 + 9,
              4 + t * 9:4 + (t + 1) * 9] = np.eye(9)
        b_box = np.zeros(NR)
        if rad_tube_sin is None:
            rso = rso_b
            rsz = rsz_b
            zso = zso_b
            zsz = zsz_b
            rad_b = np.zeros(M)
        else:
            rso = rso_b + rad_tube_sin[:, 28:32, :]
            rsz = rsz_b + rad_tube_sin[:, ZROWS, :]
            zso = zso_b + rad_tube_szd[:, 28:32, :]
            zsz = zsz_b + rad_tube_szd[:, ZROWS, :]
            rad_b = rad_tube_b
        for j in range(M):
            w = np.abs(C).sum(axis=1)
            w_eff = w + r_p * np.abs(C[:, NB])
            zdw = np.empty(8)
            for i in range(8):
                sl = src_slot[j, i]
                zdw[i] = Lw_abs[j, i, :] @ w_eff[4 + sl * 9:
                                                 4 + sl * 9 + 9]
            # the per-entry injections: inj_x (4,), inj_slot (8,)
            inj_x = rso[j] @ w_eff[0:4] + zso[j] @ zdw
            inj_slot = rsz[j] @ w_eff[0:4] + zsz[j] @ zdw
            # the p-column's own tube injection (the b_j's tube
            # variation), added on the touched coordinates
            rb = rad_b[j]
            # the in-block magnitude accumulation
            bx = b_box[0:4]
            zdw_b = np.empty(8)
            for i in range(8):
                sl = src_slot[j, i]
                zdw_b[i] = Lw_abs[j, i, :] @ b_box[4 + sl * 9:
                                                   4 + sl * 9 + 9]
            b_x_new = (sout_abs[j] @ bx + szd_abs[j][28:32] @ zdw_b
                       + np.abs(inj_x) + rb)
            b_slot_new = np.empty(9)
            b_slot_new[0] = b_box[2]
            b_slot_new[1:9] = (sin_abs[j][ZROWS] @ bx
                               + szd_abs[j][ZROWS] @ zdw_b
                               + np.abs(inj_slot) + rb)
            # the signed update of all columns
            ncols = C.shape[1]
            Zd_rows = np.empty((8, ncols))
            for i in range(8):
                sl = src_slot[j, i]
                Zd_rows[i] = Lw_mid[j, i, :] @ C[4 + sl * 9:
                                                 4 + sl * 9 + 9, :]
            dst = S_in[j] @ C[0:4, :] + Szd[j] @ Zd_rows
            aff = w_p[j]
            old_z = C[2, :].copy()
            slot = j % RING
            C[4 + slot * 9 + 1:4 + slot * 9 + 9, :] = dst[ZROWS, :]
            C[4 + slot * 9 + 0, :] = old_z
            C[0:4, :] = dst[28:32, :]
            C[0:4, NB] += aff[28:32]
            C[4 + slot * 9 + 1:4 + slot * 9 + 9, NB] += aff[ZROWS]
            b_box = b_box.copy()
            b_box[0:4] = b_x_new
            b_box[4 + slot * 9:4 + slot * 9 + 9] = b_slot_new
            if (j + 1) % BLOCK == 0:
                newcols = np.zeros((NR, NR))
                newcols[np.arange(NR), np.arange(NR)] = b_box
                C = np.hstack([C, newcols])
                b_box = np.zeros(NR)
        Mon_cols = ring_to_state_rows(C[:, 0:NB])
        Ap_final = ring_to_state_rows(C[:, NB:NB + 1])[:, 0]
        sym = np.abs(ring_to_state_rows(C[:, NB + 1:]))
        T_unc = _hi(sym.sum(axis=1) * (1.0 + EPS_ACC))
        return Mon_cols, Ap_final, T_unc

    # ---------------- the tube widths (the J-ladder machinery)
    print("tube Jacobian widths machinery ...", flush=True)

    def tube_widths(r_ball):
        Xi = [(X[s][0] - r_ball, X[s][1] + r_ball) for s in range(4)]
        jpt = jac_parts(Xi)
        infl = np.zeros((M, n + 1))
        for l in range(n + 1):
            infl += Lw_abs[:, :, l] * r_ball
        Zd_lo = _lo(ZdLag[0] - infl)
        Zd_hi = _hi(ZdLag[1] + infl)
        (Jl, Jh), (Dvl, Dvh) = jac_finish(jpt, (Zd_lo, Zd_hi))
        Dv3_w_t = 0.5 * (Dvh[:, :, 3] - Dvl[:, :, 3])
        Dv3_abs_t = i_abs_hi(Dvl[:, :, 3], Dvh[:, :, 3])
        Bfl_w_t = np.zeros((M, 32, 4))
        Bfl_w_t[:, 0:4, 0:4] = 0.5 * (Jh - Jl)[:, 0, :, :]
        Bfl_abs_t = np.zeros((M, 32, 4))
        Bfl_abs_t[:, 0:4, 0:4] = i_abs_hi(Jl[:, 0, :, :], Jh[:, 0, :, :])
        rad_sin_t = (np.einsum('mik,mkj->mij', np.abs(Rinv), Bfl_w_t)
                     + rad_Rinv_row[:, :, None]
                     * Bfl_abs_t.sum(axis=1)[:, None, :])
        DvBw_t = np.zeros((M, 32, 8))
        DvBa_t = np.zeros((M, 32, 8))
        for i in range(8):
            DvBw_t[:, i * 4 + 3, i] = Dv3_w_t[:, i]
            DvBa_t[:, i * 4 + 3, i] = Dv3_abs_t[:, i]
        rad_szd_t = (np.einsum('mik,mkj->mij', np.abs(Rinv), DvBw_t)
                     + rad_Rinv_row[:, :, None]
                     * DvBa_t.sum(axis=1)[:, None, :])
        j_rows = i_abs_hi(Jl, Jh).sum(axis=3).max(axis=2)  # (M, n+1)
        # THE SOUND INJECTION-TUBE BOUND: the per-step affine injection
        # w_p's variation over the r-ball, channel-explicit (delta w_p =
        # -(ddRinv.F_sub + dRinv.dF + dRinv_t.F_p + Rinv.dF_p)):
        #   (d-3) Rinv.Dv3.dZdP -- the landing-H tube through the weight
        #         DERIVATIVES: sum_l |dL_l/dsigma| |H[patch]| |dsig/dp| r.
        #         The DOMINANT channel (up to 15.6x the old sum|Lw|
        #         proxy, which was therefore unsound); the signed
        #         cancellation of the weight-derivative sum (exact on the
        #         constant history mode) does NOT apply here because the
        #         slot-tube variations are independent.
        #   (d-2) Rinv.dDv3.ZdP -- the Dv3 tube width over the Zd-tube
        #         times the ACTUAL substrate |ZdP| (signed sup ~3e-4;
        #         the crude ZdHm bound would overestimate ~3.5e4x).
        #   (d-1) Rinv.rho'.dJ -- the rho-scaled Jacobian tube variation.
        #   (b)   dRinv.dF -- |dRinv| <= Rn^2 rho' |J|row; |dF| <=
        #         (kd + j + dv.lw) r.
        #   (c)   dRinv_t.F_p -- |dRinv_t| <= 2 Rn^2 jw_row (the tube
        #         inverse variation through the J-widths); |F_p| <=
        #         rho' fmag + dv |ZdP|.
        #   (a)   ddRinv.F_sub -- 3 Rn^2 rho' jw F_sup (negligible).
        ZdHm = (np.abs(dLw_dsig[:, :8, :])
                * np.abs(H_sub[jp[:, :8], :])).sum(axis=2)      # (M, 8)
        Jw_t = 0.5 * (Jh - Jl)                                 # (M,9,4,4)
        jw_r = Jw_t.sum(axis=3).max(axis=(1, 2))               # (M,)
        jmid_r = i_abs_hi(Jl, Jh).sum(axis=3).max(axis=(1, 2))  # (M,)
        dv_r = Dv3_abs_t[:, :8].max(axis=1)                    # (M,)
        lw_r = Lw_abs[:, :8].sum(axis=2).max(axis=1)           # (M,)
        kd_sup = float(np.abs(KD_mid).sum(axis=1).max())
        jmid_sup = float(jmid_r.max())
        dv_sup = float(dv_r.max())
        lw_sup = float(lw_r.max())
        jw_sup = float(jw_r.max())
        ZdP_abs = np.abs(ZdP)                                  # (M, 8)
        ZdP_sup = float(ZdP_abs.max())
        # the sound rhs-magnitude bound at the substrate (the float sups
        # inflated by 1e-6 -- covering the point-interval rounding and
        # the rho-family width 2.7e-11 with four orders of margin)
        N_, A_, Z_, E_ = Xpt
        facv = A_ / (A_ + P4['A0'])
        Rv = P4['r'] * N_ * (1 - N_ / P4['K']) * facv
        fNv = Rv - P4['q'] * E_ * N_
        fAv = (-(Rv + P4['kappaA'] * N_ * facv)
               + P4['omegaA'] * (P4['AeqW'] - A_))
        defv = P4['q'] * E_ * N_ - Rv
        memv = np.maximum(
            0.0, np.log1p(np.exp(np.clip(10 * defv, -700, 700))) / 10)
        fZv = (memv - Z_) / P4['taum']
        fmag_sup = (1 + 1e-6) * max(
            float(np.abs(fNv).max()), float(np.abs(fAv).max()),
            float(np.abs(fZv).max())) + 1e-6
        b_d3 = (R_norm_rows[:, None]
                * (Dv3_abs_t[:, :8] * ZdHm * abs(dsig_dp)
                   * r_ball)).max(axis=1)
        b_d2 = (R_norm_rows[:, None]
                * (Dv3_w_t[:, :8] * ZdP_abs)).max(axis=1)
        b_d1 = R_norm_rows * (1.0 / P) * jmid_r * r_ball
        b_b = (R_norm_rows ** 2 * (1.0 / P) * jmid_r
               * (kd_sup + jmid_sup + dv_sup * lw_sup) * r_ball)
        b_c = (2.0 * R_norm_rows ** 2 * jw_r
               * ((1.0 / P) * fmag_sup + dv_sup * ZdP_sup))
        b_a = np.full(M, 3.0 * (float(R_norm_rows.max()) ** 2)
                      * (1.0 / P) * jw_sup * F_sup)
        b_tube = _hi(b_d3 + b_d2 + b_d1 + b_b + b_c + b_a)
        return rad_sin_t, rad_szd_t, b_tube

    
    # =====================================================================
    # THE DEFLATED n-PERIOD AFFINE MARCH (B4 Stage T2)
    # =====================================================================
    import json as _json
    import time as _time
    t_t2 = _time.time()

    # ---- the committed cross-checks (Mon, tangent) ----------------------
    ref = _json.loads((ROOT / "c4_piecewise_chebyshev_stage4b.json").read_text())
    ev_now = sorted((float(v) for v in np.abs(np.linalg.eigvals(Mon))),
                    reverse=True)
    ev_ref = [float(v) for v in ref["phaseA"]["monodromy_top4"]]
    ev_ok = all(abs(a - b) < 1e-9 for a, b in zip(ev_now, ev_ref))
    tang_res = float(np.abs(Mon @ tang - tang).max() / np.abs(tang).max())
    print(f"Mon top-4 vs committed 4b JSON: {ev_ok}")
    print(f"tangent residual ||Mon t - t||/||t|| = {tang_res:.3e}")

    # ---- the deflation ---------------------------------------------------
    t2 = tang / np.linalg.norm(tang)
    Dm = np.eye(NB) - np.outer(t2, t2)
    D_abs_colsum = np.abs(Dm).sum(axis=0)      # colsum_k |D[j,k]|
    print(f"||t||_1 = {np.linalg.norm(t2, 1):.2f}, "
          f"||D||_inf = {np.abs(Dm).sum(axis=1).max():.2f}")

    # the float deflated powers by direct matrix products (cross-check)
    S1 = Mon @ Dm
    # spectral cross-reference: the committed discrete deflation
    vals_d, vecs_d = np.linalg.eig(Mon)
    ip = int(np.argmin(np.abs(vals_d - 1))); lam_d = vals_d[ip]; v_d = vecs_d[:, ip]
    valsL, vecsL = np.linalg.eig(Mon.T)
    jp2 = int(np.argmin(np.abs(valsL - lam_d)))
    w_d = vecsL[:, jp2]; w_d = w_d / (w_d @ v_d)
    P_sp = np.outer(v_d, w_d)
    S_sp = Mon - lam_d * P_sp
    print(f"committed-style spectral deflation: lam_phase = {lam_d:.10f}")

    # ---- free the heavy setup arrays (copies of the needed views) --------
    rso_b = np.ascontiguousarray(rso_b); rsz_b = np.ascontiguousarray(rsz_b)
    zso_b = np.ascontiguousarray(zso_b); zsz_b = np.ascontiguousarray(zsz_b)
    import gc as _gc
    for _n in ("pl", "ph", "Mhat", "Rinv0", "RA", "E_abs", "RE", "dMhat",
               "dRinv", "Rinv", "DvB", "DvBw", "DvBa", "Jlo_s", "Jhi_s",
               "Jmid", "Jwid", "rad_szd_full", "rad_sin_full",
               "ZdLag", "Llo", "Lhi", "KD_mid", "KD_w", "D_mid",
               "dLw_dsig", "Xpt", "jp", "cos_tab", "gam", "cheb_w",
               "Rinv_rows", "q_total_rows", "Rb", "Bmat"):
        if _n in dir():
            try:
                exec(f"del {_n}")
            except Exception:
                pass
    _gc.collect()
    import resource as _res
    print(f"RSS after setup cleanup: "
          f"{_res.getrusage(_res.RUSAGE_SELF).ru_maxrss/1e6:.2f} GB",
          flush=True)

    # ---- the march state -------------------------------------------------
    # columns: [0:NB] = the float deflated evolution (input set for the
    # current period, in the AUGMENTED-STATE layout), then NB noise-symbol
    # columns (diag(ext), the rewrapped carried noise).
    # The ring layout conversion happens inside the period loop.
    n_float = NB

    # per-step needed rows for the magnitude sums: the state rows + the
    # union of the 8 source slots per step (precomputed index list per j)
    needed_rows = []
    for j in range(M):
        rows = {0, 1, 2, 3}
        for i in range(8):
            sl = src_slot[j, i]
            rows.update(range(4 + sl * 9, 4 + sl * 9 + 9))
        needed_rows.append(np.array(sorted(rows)))
    print(f"march: M={M} steps/period, BLOCK={BLOCK}, "
          f"avg needed rows {np.mean([len(r) for r in needed_rows]):.0f}")

    def _diag_ring(ext):
        """NR x NR diagonal matrix with ext (ring layout) on the diagonal."""
        out = np.zeros((NR, NR))
        out[np.arange(NR), np.arange(NR)] = ext
        return out

    def march_one_period(C):
        """March the ring-layout columns C (NR x ncols) one period with the
        4b affine pattern at point-tight widths (eval semantics): the signed
        update applies to ALL columns; the fresh injections (excited by the
        total column magnitudes w) accumulate in the magnitude box b_box,
        which block-wraps into fresh coordinate-symbol columns at each
        500-step block boundary (the 4b pattern — the cross-block signed
        propagation is PRESERVED within the period). Columns [0:NB] are the
        float evolution; everything after is noise. Returns (C, b_box):
        the marched columns and the final (empty) box."""
        ncols = C.shape[1]
        b_box = np.zeros(NR)
        for j in range(M):
            rows = needed_rows[j]
            w = np.abs(C[rows, :]).sum(axis=1)
            w_full = np.zeros(NR)
            w_full[rows] = w
            w_eff = w_full
            zdw = np.empty(8)
            for i in range(8):
                sl = src_slot[j, i]
                zdw[i] = Lw_abs[j, i, :] @ w_eff[4 + sl * 9:4 + sl * 9 + 9]
            inj_x = rso_b[j] @ w_eff[0:4] + zso_b[j] @ zdw
            inj_slot = rsz_b[j] @ w_eff[0:4] + zsz_b[j] @ zdw
            bx = b_box[0:4]
            zdw_b = np.empty(8)
            for i in range(8):
                sl = src_slot[j, i]
                zdw_b[i] = Lw_abs[j, i, :] @ b_box[4 + sl * 9:4 + sl * 9 + 9]
            b_x_new = (sout_abs[j] @ bx + szd_abs[j][28:32] @ zdw_b
                       + np.abs(inj_x))
            b_slot_new = np.empty(9)
            b_slot_new[0] = b_box[2]
            b_slot_new[1:9] = (sin_abs[j][ZROWS] @ bx
                               + szd_abs[j][ZROWS] @ zdw_b
                               + np.abs(inj_slot))
            Zd_rows = np.empty((8, ncols))
            for i in range(8):
                sl = src_slot[j, i]
                Zd_rows[i] = Lw_mid[j, i, :] @ C[4 + sl * 9:4 + sl * 9 + 9, :]
            dst = S_in[j] @ C[0:4, :] + Szd[j] @ Zd_rows
            old_z = C[2, :].copy()
            slot = j % RING
            C[4 + slot * 9 + 1:4 + slot * 9 + 9, :] = dst[ZROWS, :]
            C[4 + slot * 9 + 0, :] = old_z
            C[0:4, :] = dst[28:32, :]
            b_box = b_box.copy()
            b_box[0:4] = b_x_new
            b_box[4 + slot * 9:4 + slot * 9 + 9] = b_slot_new
            if (j + 1) % BLOCK == 0:
                C = np.hstack([C, _diag_ring(b_box)])
                b_box = np.zeros(NR)
                ncols = C.shape[1]
        return C, b_box

    # ---- the period loop --------------------------------------------------
    results_periods = []
    X_prev = np.eye(NB)              # the unit basis (augmented state)
    ext_in_prev = np.zeros(NB)       # no carried noise at period 0
    S_pow = np.eye(NB)               # the direct float (Mon D)^p (cross-check)
    rec = {}
    t_loop = _time.time()
    start_p = 1
    ckpt = ROOT / "b4_t2_checkpoint.npz"
    if ckpt.exists():
        try:
            z = np.load(ckpt, allow_pickle=True)
            start_p = int(z["p"]) + 1
            X_prev = z["X_prev"]; ext_in_prev = z["ext_in_prev"]
            S_pow = z["S_pow"]
            results_periods = [dict(r) for r in z["results"]]
            print(f"RESUMED from checkpoint p={start_p - 1}", flush=True)
        except Exception as e:
            print(f"checkpoint load failed ({e}); fresh start", flush=True)
    for p in range(start_p, 41):
        Xin = Dm @ X_prev
        C = np.hstack([state_to_ring_rows(Xin),
                       state_to_ring_rows(np.diag(ext_in_prev))])
        Cm, b_fin = march_one_period(C)
        X_p = ring_to_state_rows(Cm[:, :NB])
        # the output noise zonotope (state layout), processed in chunks:
        # ext_p (the UNDEFLATED output uncertainty) and ext_in (the deflated
        # carried noise, signed deflation then collapse) without
        # materializing the full zonotope twice
        ncol_noise = Cm.shape[1] - NB
        ext_p = np.zeros(NB)
        ext_in = np.zeros(NB)
        CH = 2000
        for c0 in range(0, ncol_noise, CH):
            blk = ring_to_state_rows(Cm[:, NB + c0:NB + min(c0 + CH, ncol_noise)])
            ext_p += np.abs(blk).sum(axis=1)
            ext_in += np.abs(Dm @ blk).sum(axis=1)
            del blk
        del Cm, C
        _gc.collect()
        # the certificate at p
        center_norm = float(np.abs(X_p).sum(axis=1).max())
        bound_p = float((np.abs(X_p).sum(axis=1) + ext_p).max())
        # the direct float cross-check
        S_pow = S1 @ S_pow
        if p in (1, 2, 5, 10, 15, 20, 25, 30, 35, 40):
            gap = float(np.abs(X_p - S_pow).max())
            print(f"  period {p:2d}: center {center_norm:.6e}, "
                  f"ext sup {float(ext_p.max()):.3e}, "
                  f"bound {bound_p:.6e}, gap {gap:.2e}, "
                  f"[{(time.time()-t_loop)/p:.1f}s/period]", flush=True)
            rec[p] = {"center_norm": center_norm,
                      "ext_sup": float(ext_p.max()),
                      "bound": bound_p, "float_gap": gap}
        results_periods.append({"p": p, "center_norm": center_norm,
                                "ext_sup": float(ext_p.max()),
                                "bound": bound_p})
        X_prev = X_p
        ext_in_prev = ext_in
        if p % 5 == 0:
            np.savez_compressed(
                ROOT / "b4_t2_checkpoint.npz",
                p=p, X_prev=X_prev, ext_in_prev=ext_in_prev,
                S_pow=S_pow,
                results=np.array(results_periods, dtype=object),
                allow_pickle=True)
    t_march = _time.time() - t_t2
    print(f"march total: {t_march:.1f}s")

    # ---- the assembly ------------------------------------------------------
    MC = 4.590009620   # the Stage-T4 certified upper bound
    t3 = _json.loads((ROOT / "b4_t3_slack_semigroup_certificate.json").read_text())
    slack35 = t3["semigroup_bounds"]["35"]["bound"]
    slack40 = t3["semigroup_bounds"]["40"]["bound"]
    b35 = [r for r in results_periods if r["p"] == 35][0]["bound"]
    b40 = [r for r in results_periods if r["p"] == 40][0]["bound"]
    q35 = MC * max(b35, slack35)
    q40 = MC * max(b40, slack40)
    print(f"\nASSEMBLY: ||S_x^35||_int <= {b35:.6e}, ||T_y(35P)|| <= {slack35:.6e}")
    print(f"  q_35 = M_c * max = {q35:.6f}  (< 1 required): "
          f"{'PASS' if q35 < 1 else 'FAIL'}")
    print(f"ASSEMBLY: ||S_x^40||_int <= {b40:.6e}, ||T_y(40P)|| <= {slack40:.6e}")
    print(f"  q_40 = M_c * max = {q40:.6f}  (< 1/4 target): "
          f"{'PASS' if q40 < 0.25 else 'FAIL'}")

    # the committed discrete cross-reference (the spectral deflation, dt=0.05)
    sp_pows = {}
    A_sp = np.eye(NB)
    for n in range(1, 41):
        A_sp = A_sp @ S_sp
        if n in (10, 20, 25, 30, 35, 40):
            sp_pows[n] = float(np.linalg.norm(A_sp, np.inf))

    out = {
        "title": "B4 continuum transfer — Stage T2: the binding-block "
                 "stable-complement product certificate",
        "object": "the deflated n-period evolution (Mon D)^n + Delta_n of the "
                  "collocation monodromy, D = I - t t^T (the certified tangent), "
                  "in the 4b affine noise-symbol arithmetic at point-tight widths",
        "cross_checks": {
            "monodromy_top4_vs_committed_4b": {"now": ev_now, "ref": ev_ref,
                                                "pass": bool(ev_ok)},
            "tangent_residual": tang_res,
            "float_gap_max": max(v["float_gap"] for v in rec.values()),
            "committed_spectral_deflation_powers": sp_pows,
        },
        "deflation": {"tangent_l1": float(np.linalg.norm(t2, 1)),
                      "D_inf_norm": float(np.abs(Dm).sum(axis=1).max()),
                      "phase_eigenvalue_committed_style": float(lam_d.real)},
        "periods": results_periods,
        "assembly": {
            "M_c": MC,
            "binding_35": b35, "slack_35": slack35, "q_35": q35,
            "q_35_pass": bool(q35 < 1),
            "binding_40": b40, "slack_40": slack40, "q_40": q40,
            "q_40_quarter_pass": bool(q40 < 0.25),
        },
        "honesty": "certifies the COLLOCATION system's stable-complement "
                   "product with interval evaluation uncertainty; the "
                   "operator-level continuum lift (true DDE variational "
                   "monodromy vs collocation) is not enclosed — the "
                   "solution-level lift is the committed Stage-4d certificate",
    }
    out["all_checks_pass"] = bool(ev_ok and all(
        v["float_gap"] < 1e-9 for v in rec.values()) and q35 < 1)
    (ROOT / "b4_t2_binding_product_certificate.json").write_text(
        _json.dumps(out, indent=1, sort_keys=True))
    print(f"wrote b4_t2_binding_product_certificate.json")
    print(f"all_checks_pass = {out['all_checks_pass']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

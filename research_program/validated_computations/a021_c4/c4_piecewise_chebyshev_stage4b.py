#!/usr/bin/env python3
"""A1 piecewise-Chebyshev campaign — STAGE 4b: the correlation-tracking
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

    # ---------------- the mpmath mismatch center
    print("mpmath mismatch march (the center) ...", flush=True)
    t_mm = time.time()
    mpm_xi = [mpf(float(Xpt[s][0, 0])) for s in range(4)]
    mpm_history = [[mpf(0)] * 9 for _ in range(RING)]
    for t in range(99):
        pidx = M - 99 + t
        mpm_history[pidx % RING] = [mpf(float(v))
                                    for v in Xpt[2][pidx, :]]
    for j in range(M):
        Zdv = [mpf(0)] * 8
        for i in range(8):
            sl = src_slot[j, i]
            acc = mpf(0)
            for l in range(9):
                lv = Lw_mid[j, i, l]
                if lv != 0.0:
                    acc += mpf(float(lv)) * mpm_history[sl][l]
            Zdv[i] = acc
        Xn_mp = [[mpf(float(Xpt[s][j, i])) for s in range(4)]
                 for i in range(9)]
        for s in range(4):
            Xn_mp[0][s] = mpm_xi[s]

        def f_mp_row(i):
            Nx, Ax, Zx, Ex = (Xn_mp[i][s] for s in range(4))
            Zd = Zdv[i]
            fac = Ax / (Ax + mpF(P4['A0']))
            R = mpF(P4['r']) * Nx * (1 - Nx / mpF(P4['K'])) * fac
            deficit = mpF(P4['q']) * Ex * Nx - R
            mem = max(mpF(0), mp.log(1 + mp.exp(10 * deficit)) / 10)
            gate = 1 - Ex / mpF(P4['Emax'])
            fN = R - mpF(P4['q']) * Ex * Nx
            fA = (-(R + mpF(P4['kappaA']) * Nx * fac)
                  + mpF(P4['omegaA']) * (mpF(P4['AeqW']) - Ax))
            fZ = (mem - Zx) / mpF(P4['taum'])
            fE = gate * (mpF(P4['eta']) * Ex
                         * (Zd / mpF(P4['Dref']) - Ex / mpF(P4['Emax']))
                         + mpF(P4['delta0']) * Zd
                         / (mpF(P4['Zref']) + Zd))
            return [fN, fA, fZ, fE]

        Fj = [mpf(0)] * 32
        for i in range(8):
            deriv = [mpf(0)] * 4
            for ip in range(9):
                kd = KD_mid[i, ip]
                if kd != 0.0:
                    kdm = mpf(float(kd))
                    for s in range(4):
                        deriv[s] += kdm * Xn_mp[ip][s]
            fr = f_mp_row(i)
            for s in range(4):
                Fj[i * 4 + s] = deriv[s] - fr[s]
        wj = [mpf(0)] * 32
        for r_ in range(32):
            acc = mpf(0)
            row = Rinv[j][r_]
            for c_ in range(32):
                rv = row[c_]
                if rv != 0.0:
                    acc += mpf(float(rv)) * Fj[c_]
            wj[r_] = -acc
        new_xi = [Xn_mp[8][s] + wj[28 + s] for s in range(4)]
        newslot = [mpf(0)] * 9
        newslot[0] = mpm_xi[2]
        for i in range(1, 9):
            newslot[i] = Xn_mp[i][2] + wj[(i - 1) * 4 + 2]
        mpm_history[j % RING] = newslot
        mpm_xi = new_xi
    mism_xi_mp = [mpm_xi[s] - mpf(float(Xpt[s][0, 0])) for s in range(4)]
    mism_H_mp = np.zeros((99, 9))
    for t in range(99):
        pidx = M - 99 + t
        for k in range(9):
            mism_H_mp[t, k] = float(mpm_history[pidx % RING][k]
                                    - mpf(float(Xpt[2][pidx, k])))
    m_center = np.concatenate([[float(v) for v in mism_xi_mp],
                               mism_H_mp.ravel()])
    m_center_sup = float(np.abs(m_center).max())
    mm_secs = time.time() - t_mm

    # ---------------- the mismatch march's affine widths
    print("mismatch affine width march ...", flush=True)
    t_w = time.time()
    b_box = np.zeros(NR)
    xi_c = np.array([Xpt[s][0, 0] for s in range(4)])
    hist_c = np.zeros((RING, 9))
    for t in range(99):
        pidx = M - 99 + t
        hist_c[pidx % RING, :] = Xpt[2][pidx, :]
    sym_boxes = []
    xmag_cache = np.abs(np.stack([Xpt[s] for s in range(4)],
                                 axis=1))  # (M, 4, 9)
    Lw_w_abs = np.abs(Lw_w)
    for j in range(M):
        # the defect width: rad(KD) . |X|  (the f-part is evaluated
        # exactly in mpmath at point values — no width; the Zd-width
        # enters via the Szd response below; the Rinv-width times |F|
        # ~ 5e-16 * 1e-8 is negligible and recorded in the docstring)
        Fw = np.zeros(32)
        for i in range(8):
            for s in range(4):
                acc = 0.0
                for ip in range(9):
                    acc += 0.5 * KD_w[i, ip] * xmag_cache[j, s, ip]
                Fw[i * 4 + s] = acc
        w_w = np.abs(Rinv[j]) @ Fw
        zdw = np.empty(8)
        for i in range(8):
            sl = src_slot[j, i]
            zdw[i] = Lw_w_abs[j, i, :] @ np.abs(hist_c[sl])
        ww_zd = np.abs(Szd[j]) @ zdw
        inj = np.zeros(NR)
        inj[0:4] = w_w[28:32] + ww_zd[28:32]
        inj_slot = np.empty(9)
        inj_slot[0] = 0.0
        inj_slot[1:9] = w_w[ZROWS] + ww_zd[ZROWS]
        inj[4 + (j % RING) * 9:4 + (j % RING) * 9 + 9] = inj_slot
        # the in-block accumulation
        bx = b_box[0:4]
        zdw_b = np.empty(8)
        for i in range(8):
            sl = src_slot[j, i]
            zdw_b[i] = Lw_abs[j, i, :] @ b_box[4 + sl * 9:
                                               4 + sl * 9 + 9]
        b_x_new = (sout_abs[j] @ bx + szd_abs[j][28:32] @ zdw_b
                   + np.abs(inj[0:4]))
        b_slot_new = np.empty(9)
        b_slot_new[0] = b_box[2]
        b_slot_new[1:9] = (sin_abs[j][ZROWS] @ bx
                           + szd_abs[j][ZROWS] @ zdw_b
                           + np.abs(inj_slot[1:9]))
        b_box = b_box.copy()
        b_box[0:4] = b_x_new
        b_box[4 + (j % RING) * 9:4 + (j % RING) * 9 + 9] = b_slot_new
        # advance the float center
        Zdv = np.empty(8)
        for i in range(8):
            sl = src_slot[j, i]
            Zdv[i] = Lw_mid[j, i, :] @ hist_c[sl]
        Xj = np.stack([Xpt[s][j, :] for s in range(4)], axis=1)
        Xn = Xj.copy()
        Xn[0, :] = xi_c
        rhs = f_rhs_float([Xn[:, 0], Xn[:, 1], Xn[:, 2], Xn[:, 3]],
                          np.append(Zdv, 0.0))
        Fj = np.zeros(32)
        for i in range(8):
            deriv = KD_mid[i, :] @ Xn
            for s in range(4):
                Fj[i * 4 + s] = deriv[s] - float(rhs[s][i])
        w_j = -Rinv[j] @ Fj
        xi_old_z = xi_c[2]
        xi_c = Xj[8, :] + w_j[28:32]
        newslot = np.empty(9)
        newslot[0] = xi_old_z
        for i in range(1, 9):
            newslot[i] = Xj[i, 2] + w_j[(i - 1) * 4 + 2]
        hist_c[j % RING, :] = newslot
        if (j + 1) % BLOCK == 0:
            sym_boxes.append(b_box.copy())
            b_box = np.zeros(NR)
    T_m = np.zeros(NB)
    for bi, bb in enumerate(sym_boxes):
        Cb = np.zeros((NR, NR))
        Cb[np.arange(NR), np.arange(NR)] = bb
        for j in range((bi + 1) * BLOCK, M):
            Zd_rows = np.empty((8, NR))
            for i in range(8):
                sl = src_slot[j, i]
                Zd_rows[i] = Lw_mid[j, i, :] @ Cb[4 + sl * 9:
                                                 4 + sl * 9 + 9, :]
            dst = S_in[j] @ Cb[0:4, :] + Szd[j] @ Zd_rows
            old_z = Cb[2, :].copy()
            slot = j % RING
            Cb[4 + slot * 9 + 0, :] = old_z
            Cb[4 + slot * 9 + 1:4 + slot * 9 + 9, :] = dst[ZROWS, :]
            Cb[0:4, :] = dst[28:32, :]
        T_m += np.abs(ring_to_state_rows(Cb)).sum(axis=1)
    T_m = _hi(T_m * (1.0 + EPS_ACC))
    mmw_secs = time.time() - t_w

    if phase == "A":
        print("saving phase-A checkpoint ...", flush=True)
        np.savez_compressed(
            CKPT,
            Mon=Mon, tang=tang, Ap=Ap, Rb=Rb, ev=ev,
            q0_b=q0_b, Rb_norm=Rb_norm,
            q0=q0, q_total_sup=q_total_sup,
            rad_Rinv_sup=rad_Rinv_sup, R_norm=R_norm,
            rad_Rinv_row=rad_Rinv_row, R_norm_rows=R_norm_rows,
            rad_sin_full=rad_sin_full, rad_szd_full=rad_szd_full,
            E_abs=E_abs, q_total_rows=q_total_rows,
            Rinv=Rinv, S_in=S_in, Szd=Szd,
            Lw_mid=Lw_mid, Lw_abs=Lw_abs, Lw_w=Lw_w,
            dLw_dsig=dLw_dsig, src_slot=src_slot, jp=jp,
            ZdP=ZdP, w_p=w_p, F_sup=np.array([F_sup]),
            X0=X[0][0], X1=X[0][1], X2=X[1][0], X3=X[1][1],
            X4=X[2][0], X5=X[2][1], X6=X[3][0], X7=X[3][1],
            ZdLag_lo=ZdLag[0], ZdLag_hi=ZdLag[1],
            Llo=Llo, Lhi=Lhi,
            KD_mid=KD_mid, KD_w=KD_w, D_mid=D_mid,
            Xpt0=Xpt[0], Xpt1=Xpt[1], Xpt2=Xpt[2], Xpt3=Xpt[3],
            Zdpt=Zdpt, nodes=nodes, den=den,
            m_center=m_center, T_m=T_m,
            P=np.array([P]), P_lo=np.array([P_lo_f]),
            P_hi=np.array([P_hi_f]),
            rho_lo=np.array([rho_lo]), rho_hi=np.array([rho_hi]),
            d_rho=np.array([d_rho]),
            dsig_dp=np.array([dsig_dp]),
            dKD_scale=np.array([dKD_scale]),
            d_rho_dp=np.array([d_rho_dp]),
            mism_xi_mp=np.array([[float(v) for v in mism_xi_mp]]),
        )
        jout = {
            "phase": "A",
            "mismatch_mpmath_center_sup": float(np.abs(m_center).max()),
            "stage4a_float_sup": STAGE4A_FLOAT_MISMATCH,
            "T_m_sup": float(T_m.max()),
            "monodromy_top4": [float(v) for v in ev[:4]],
            "bordered_q0": q0_b,
            "bordered_inverse_norm": Rb_norm,
            "p_column_sup": float(np.abs(Ap).max()),
            "q0_refined": float(q0),
            "F_sup": F_sup,
        }
        with open(ROOT / "c4_piecewise_chebyshev_stage4b_phaseA.json",
                  "w") as f:
            json.dump(jout, f, indent=1, sort_keys=True)
        print(f"phase A done in {time.time() - t_start:.1f}s", flush=True)
        return 0

    # ---------------- the Krawczyk assembly
    print("Krawczyk assembly ...", flush=True)
    m_pad = np.zeros(NB + 1)
    m_pad[0:NB] = m_center
    Y_center_vec = Rb @ m_pad
    Y_center = float(np.abs(Y_center_vec).max())
    T_m_pad = np.zeros(NB + 1)
    T_m_pad[0:NB] = T_m
    Y_ext = float((np.abs(Rb) @ T_m_pad).max())
    Y = _hi(Y_center + Y_ext)

    ladder = {}
    closure_found = False
    r_cert = None
    Z_cert = None
    T_op_cert = None
    for r_try in R_LADDER:
        print(f"  r = {r_try:g}: tube widths + operator march ...",
              flush=True)
        rad_sin_t, rad_szd_t, b_tube = tube_widths(r_try)
        Mon_cols, Ap_fin, T_unc = operator_march(
            rad_sin_t, rad_szd_t, b_tube, r_try)
        mon_gap = float(np.abs(Mon_cols - Mon).max())
        # the Z-term: the additive monodromy extent through R (the
        # zonotope enters unscaled), plus the p-column's own uncertainty
        # (bounded by the same per-coordinate extent) which multiplies
        # the p-amplitude (<= r): Z = q0 + (1 + r) * || |R| T_unc ||
        T_all = np.zeros(NB + 1)
        T_all[0:NB] = T_unc
        ZT = float((np.abs(Rb) @ T_all).max())
        Z = _hi(q0_b + (1.0 + r_try) * ZT)
        closure = bool(Y + Z * r_try <= r_try)
        print(f"    mon_gap={mon_gap:.2e} Z={Z:.6f} Y={Y:.3e} "
              f"Y+Zr={Y + Z * r_try:.3e} closure={closure}", flush=True)
        ladder[f"r_{r_try:g}"] = {
            "Z": float(Z), "Y_plus_Zr": float(Y + Z * r_try),
            "closure": closure, "mon_gap": mon_gap,
            "T_unc_sup": float(T_unc.max()),
        }
        if closure and not closure_found:
            closure_found = True
            r_cert = r_try
            Z_cert = float(Z)
            T_op_cert = T_unc.copy()
            break

    # ---------------- verification checks
    print("verification checks ...", flush=True)
    checks = {}
    mon_ev_gap = float(max(abs(ev[0] - COMMITTED_MONODROMY["phase"]),
                           abs(ev[1] - COMMITTED_MONODROMY["dominant"]),
                           abs(ev[2] - COMMITTED_MONODROMY["disc"])))
    checks["monodromy_eigenvalues_vs_committed"] = {
        "top4": [float(v) for v in ev[:4]],
        "max_gap": mon_ev_gap, "pass": bool(mon_ev_gap < 1e-6)}

    tang_res = float(np.linalg.norm(Mon @ tang - tang) / tn)
    checks["tangent_residual"] = {
        "value": tang_res, "pass": bool(tang_res < 1e-6)}

    mism_gap = abs(m_center_sup - STAGE4A_FLOAT_MISMATCH)
    checks["mismatch_center_vs_stage4a"] = {
        "mpmath_sup": m_center_sup,
        "stage4a_float": STAGE4A_FLOAT_MISMATCH,
        "gap": mism_gap,
        "pass": bool(mism_gap < 1e-6)}

    checks["mismatch_enclosure_width"] = {
        "T_m_sup": float(T_m.max()),
        "center_sup": m_center_sup,
        "pass": bool(T_m.max() < 1e-5)}

    checks["bordered_inverse"] = {
        "q0": q0_b, "norm": Rb_norm,
        "pass": bool(q0_b < 1e-9 and Rb_norm < 1e4)}

    # the p-column finite-difference check
    print("  p-column finite difference ...", flush=True)

    def float_mismatch_at_p(p_val):
        # the (a)-formulation (matching the analytic p-column and
        # certify.py's check): KD = 2M/P FIXED; the p-family enters only
        # through rho scaling the rhs and the delay offsets
        two_h = 2.0 * M / P
        rho_v = (P + p_val) / P
        toh = TAU * M / (P + p_val)
        uo = (np.arange(M)[:, None]
              + (nodes[None, :] + 1.0) / 2.0) - toh
        jpf = np.floor(uo).astype(np.int64) % M
        fracf = uo - np.floor(uo)
        sigf = 2.0 * fracf - 1.0
        Lwf = np.empty((M, n + 1, n + 1))
        for l in range(n + 1):
            acc = np.ones((M, n + 1))
            for m2 in range(n + 1):
                if m2 != l:
                    acc *= (sigf - nodes[m2])
            Lwf[:, :, l] = acc / den[l]
        KDp = two_h * D_mid
        xi_c = np.array([Xpt[s][0, 0] for s in range(4)])
        hist_c = np.zeros((RING, 9))
        for t in range(99):
            pidx = M - 99 + t
            hist_c[pidx % RING, :] = Xpt[2][pidx, :]
        srcf = jpf % RING
        for j in range(M):
            Zdv = np.empty(8)
            for i in range(8):
                sl = srcf[j, i]
                Zdv[i] = Lwf[j, i, :] @ hist_c[sl]
            Xj = np.stack([Xpt[s][j, :] for s in range(4)], axis=1)
            Xn = Xj.copy()
            Xn[0, :] = xi_c
            fac = Xn[:, 1] / (Xn[:, 1] + P4['A0'])
            R = P4['r'] * Xn[:, 0] * (1 - Xn[:, 0] / P4['K']) * fac
            deficit = P4['q'] * Xn[:, 3] * Xn[:, 0] - R
            mem = np.maximum(0.0, np.log1p(np.exp(np.clip(
                10 * deficit, -700, 700))) / 10)
            gate = 1 - Xn[:, 3] / P4['Emax']
            Zd9 = np.append(Zdv, 0.0)
            fN = rho_v * (R - P4['q'] * Xn[:, 3] * Xn[:, 0])
            fA = rho_v * (-(R + P4['kappaA'] * Xn[:, 0] * fac)
                          + P4['omegaA'] * (P4['AeqW'] - Xn[:, 1]))
            fZ = rho_v * (mem - Xn[:, 2]) / P4['taum']
            fE = rho_v * gate * (
                P4['eta'] * Xn[:, 3]
                * (Zd9 / P4['Dref'] - Xn[:, 3] / P4['Emax'])
                + P4['delta0'] * Zd9 / (P4['Zref'] + Zd9))
            Fj = np.zeros(32)
            for i in range(8):
                deriv = KDp[i, :] @ Xn
                for s in range(4):
                    Fj[i * 4 + s] = deriv[s] - [fN, fA, fZ, fE][s][i]
            w_j = -Rinv[j] @ Fj
            xi_old_z = xi_c[2]
            xi_c = Xj[8, :] + w_j[28:32]
            newslot = np.empty(9)
            newslot[0] = xi_old_z
            for i in range(1, 9):
                newslot[i] = Xj[i, 2] + w_j[(i - 1) * 4 + 2]
            hist_c[j % RING, :] = newslot
        mism_xi = xi_c - np.array([Xpt[s][0, 0] for s in range(4)])
        mism_H = np.zeros((99, 9))
        for t in range(99):
            pidx = M - 99 + t
            mism_H[t] = hist_c[pidx % RING, :] - Xpt[2][pidx, :]
        return np.concatenate([mism_xi, mism_H.ravel()])

    h_fd = 1e-7
    m_plus = float_mismatch_at_p(+h_fd)
    m_minus = float_mismatch_at_p(-h_fd)
    fd_pcol = (m_plus - m_minus) / (2 * h_fd)
    denom_ = max(1.0, float(np.abs(Ap).max()))
    pcol_gap = float(np.abs(fd_pcol - Ap).max() / denom_)
    checks["p_column_finite_difference"] = {
        "h": h_fd, "rel_gap": pcol_gap,
        "Ap_sup": float(np.abs(Ap).max()),
        "fd_sup": float(np.abs(fd_pcol).max()),
        "pass": bool(pcol_gap < 5e-3)}

    # the eval-only operator march + the consistency checks
    print("  eval-only operator march + containment ...", flush=True)
    Mon_cols0, Ap0, T_unc0 = operator_march(None, None, None, 0.0)
    mon_gap0 = float(np.abs(Mon_cols0 - Mon).max())
    checks["operator_march_monodromy_consistency"] = {
        "mon_gap": mon_gap0, "pass": bool(mon_gap0 < 1e-9)}
    ap_gap0 = float(np.abs(Ap0 - Ap).max())
    checks["operator_march_pcolumn_consistency"] = {
        "ap_gap": ap_gap0,
        "pass": bool(ap_gap0 < 1e-9 * max(1.0, float(np.abs(Ap).max())))}

    # the magnitude-vs-signed unit-propagation check (the block
    # machinery's validity): at probe (block, coordinate) points, the
    # in-block magnitude march of a unit injection must contain the
    # signed march's absolute result
    print("  magnitude-vs-signed block check ...", flush=True)
    mag_ok = True
    mag_detail = []
    for (j0, k0) in [(1000, 0), (3500, 440), (7000, 890)]:
        box = np.zeros(NR)
        box[k0] = 1.0
        col = np.zeros(NR)
        col[k0] = 1.0
        for j in range(j0, min(j0 + 200, M)):
            bx = box[0:4]
            zdw_b = np.empty(8)
            for i in range(8):
                sl = src_slot[j, i]
                zdw_b[i] = Lw_abs[j, i, :] @ box[4 + sl * 9:
                                                 4 + sl * 9 + 9]
            b_x_new = sout_abs[j] @ bx + szd_abs[j][28:32] @ zdw_b
            b_slot_new = np.empty(9)
            b_slot_new[0] = box[2]
            b_slot_new[1:9] = (sin_abs[j][ZROWS] @ bx
                               + szd_abs[j][ZROWS] @ zdw_b)
            box = box.copy()
            box[0:4] = np.abs(b_x_new)
            box[4 + (j % RING) * 9:4 + (j % RING) * 9 + 9] = np.abs(
                b_slot_new)
            Zd_r = np.empty(8)
            for i in range(8):
                sl = src_slot[j, i]
                Zd_r[i] = Lw_mid[j, i, :] @ col[4 + sl * 9:
                                                4 + sl * 9 + 9]
            dst = S_in[j] @ col[0:4] + Szd[j] @ Zd_r
            old_z = col[2]
            slot = j % RING
            col = col.copy()
            col[4 + slot * 9 + 0] = old_z
            col[4 + slot * 9 + 1:4 + slot * 9 + 9] = dst[ZROWS]
            col[0:4] = dst[28:32]
        viol = float((np.abs(col) - box).max())
        mag_ok = mag_ok and (viol <= 1e-12)
        mag_detail.append({"j0": j0, "k0": k0, "violation": viol})
    checks["magnitude_vs_signed_block_propagation"] = {
        "detail": mag_detail, "pass": bool(mag_ok)}

    # the mpmath probe-column containment: Mon[:,k] +- T_unc0 contains
    # an independent mpmath evaluation of the signed float product
    print("  mpmath probe-column containment ...", flush=True)
    contain_ok = True
    contain_detail = []
    for k in [0, 400]:
        unit_ring = np.zeros(NR)
        unit_state = np.zeros((NB, 1))
        unit_state[k, 0] = 1.0
        unit_ring_full = state_to_ring_rows(unit_state)[:, 0]
        Ck_mp = [mpf(float(v)) for v in unit_ring_full]
        for j in range(M):
            Zd_r = [mpf(0)] * 8
            for i in range(8):
                sl = src_slot[j, i]
                acc = mpf(0)
                for l in range(9):
                    lv = Lw_mid[j, i, l]
                    if lv != 0.0:
                        acc += mpf(float(lv)) * Ck_mp[4 + sl * 9 + l]
                Zd_r[i] = acc
            dst = [mpf(0)] * 32
            for r_ in range(32):
                acc = mpf(0)
                for c_ in range(4):
                    sv = S_in[j][r_, c_]
                    if sv != 0.0:
                        acc += mpf(float(sv)) * Ck_mp[c_]
                for i in range(8):
                    sv = Szd[j][r_, i]
                    if sv != 0.0:
                        acc += mpf(float(sv)) * Zd_r[i]
                dst[r_] = acc
            old_z = Ck_mp[2]
            slot = j % RING
            newC = list(Ck_mp)
            newC[4 + slot * 9 + 0] = old_z
            for i in range(1, 9):
                newC[4 + slot * 9 + i] = dst[ZROWS[i - 1]]
            for s in range(4):
                newC[s] = dst[28 + s]
            Ck_mp = newC
        # project the ring to the state and compare
        ring_np = np.array([float(v) for v in Ck_mp])
        state_np = ring_to_state_rows(ring_np[:, None])[:, 0]
        worst = 0.0
        for r_ in range(NB):
            val = float(state_np[r_])
            lo_ = Mon[r_, k] - T_unc0[r_]
            hi_ = Mon[r_, k] + T_unc0[r_]
            if not (lo_ <= val <= hi_):
                contain_ok = False
                worst = max(worst, min(abs(val - lo_), abs(val - hi_)))
        contain_detail.append({"k": k, "worst_violation": worst})
    checks["mpmath_probe_column_containment"] = {
        "probes": [0, 400], "detail": contain_detail,
        "T_unc0_sup": float(T_unc0.max()),
        "pass": bool(contain_ok)}

    checks["krawczyk_closure"] = {
        "found": closure_found, "r": r_cert, "Z": Z_cert, "Y": float(Y),
        "pass": bool(closure_found)}

    all_pass = all(bool(v.get("pass", False)) for v in checks.values())

    # ---------------- output
    print("writing outputs ...", flush=True)
    out = {
        "title": ("A1 piecewise-Chebyshev campaign — Stage 4b: the "
                  "correlation-tracking affine march, the rigorous "
                  "monodromy enclosure, and the periodic collocation "
                  "fixed-point certificate"),
        "status": ("THE ASSEMBLY CERTIFICATE "
                   + ("CLOSED" if closure_found
                      else "NOT CLOSED at the tested radii (the "
                           "obstruction constants recorded honestly)")
                   + ("; the discrete periodic collocation fixed point "
                      "of the one-period local-Newton map is certified "
                      "to exist within r (sup-norm, the augmented "
                      "state) of the substrate, at a period P + p* "
                      "with |p*| <= r" if closure_found else "")
                   + ". The continuum orbit-to-solution lift (the "
                     "function-space resolvent applied to the Stage-4a "
                     "between-nodes defect bound) remains Stage 4c."),
        "inputs": {
            "orbit": "committed Krawczyk box midpoint "
                     "(c4_orbit_krawczyk_box.npz)",
            "period_P": P,
            "P_box": [P_lo_f, P_hi_f],
            "rho_family_halfwidth": d_rho,
            "M_segments": M,
            "cheb_degree": n,
            "block_length": BLOCK,
            "n_blocks": M // BLOCK,
        },
        "stage_matrices": {
            "refined_inverse_q0_sup": float(q0),
            "q_total_sup": q_total_sup,
            "rad_Rinv_row_sup": rad_Rinv_sup,
            "R_norm_sup": float(R_norm),
            "rad_sin_rowsum_sup": float(rad_sin_full.sum(axis=2).max()),
            "rad_szd_rowsum_sup": float(rad_szd_full.sum(axis=2).max()),
        },
        "float_marches": {
            "monodromy_top4": [float(v) for v in ev[:4]],
            "tangent_residual_rel": tang_res,
            "p_column_sup": float(np.abs(Ap).max()),
            "bordered_q0": q0_b,
            "bordered_inverse_norm": Rb_norm,
        },
        "mismatch": {
            "mpmath_center_sup": m_center_sup,
            "stage4a_float_sup": STAGE4A_FLOAT_MISMATCH,
            "center_gap": mism_gap,
            "T_m_sup": float(T_m.max()),
        },
        "krawczyk": {
            "Y_center": Y_center, "Y_ext": Y_ext, "Y": float(Y),
            "ladder": ladder,
            "closure_found": closure_found,
            "certified_radius": r_cert,
            "certified_Z": Z_cert,
            "certified_T_op_sup": (float(T_op_cert.max())
                                   if T_op_cert is not None else None),
        },
        "verification": checks,
        "all_checks_pass": bool(all_pass),
    }
    jpath = ROOT / "c4_piecewise_chebyshev_stage4b.json"
    with open(jpath, "w") as f:
        json.dump(out, f, indent=1, sort_keys=True)
    npzpath = ROOT / "c4_piecewise_chebyshev_stage4b.npz"
    np.savez_compressed(
        npzpath,
        Mon=Mon, tang=tang, Ap=Ap,
        m_center=m_center, T_m=T_m,
        T_unc_eval=T_unc0,
        T_unc_cert=(T_op_cert if T_op_cert is not None else T_unc0),
        Y_center_vec=Y_center_vec,
    )
    print(f"done: closure={closure_found} r={r_cert} "
          f"all_checks_pass={all_pass}", flush=True)
    print(f"total secs: {time.time() - t_start:.1f}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())

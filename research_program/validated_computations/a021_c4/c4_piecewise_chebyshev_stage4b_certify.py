#!/usr/bin/env python3
"""A1 Stage 4b — PHASE B (the certification): loads the Phase-A checkpoint
and runs, per invocation (one unit of work per call, each within the
sandbox window):
    python3 ..._stage4b_certify.py eval          # the eval-only march
    python3 ..._stage4b_certify.py r:<radius>    # a tube march (e.g. r:1e-6)
    python3 ..._stage4b_certify.py checks        # the verification checks
    python3 ..._stage4b_certify.py final         # assemble the JSON
Results accumulate in c4_piecewise_chebyshev_stage4b_results.json.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT))
from c4_piecewise_chebyshev_stage3 import (  # noqa: E402
    cheb_lobatto, iv_pt, make_model, f64_interval,
    i_abs_hi, iadd, imul, i_scal, isub,
    _lo, _hi, _NINF, _PINF,
)
from mpmath import iv as miv
from mpmath import mp, mpf

mp.dps = 40
miv.dps = 30

EPS_F = 2.220446049250313e-16
EPS_ACC = 40 * EPS_F
M_SEG = 8000
N = 8
RING = 100
NB = 4 + 99 * 9
NR = 4 + RING * 9
ZROWS = np.arange(8) * 4 + 2
BLOCK = 500
CKPT = ROOT / "c4_piecewise_chebyshev_stage4b_ckpt.npz"
RES = ROOT / "c4_piecewise_chebyshev_stage4b_results.json"
STAGE4A_FLOAT_MISMATCH = 1.1846054803754669e-08
COMMITTED_MONODROMY = {"phase": 1.0000000000028728,
                       "dominant": 0.6876928141092927,
                       "disc": 0.30271822276116467}


def ring_to_state_rows(Mat):
    out = np.zeros((NB, Mat.shape[1]))
    out[0:4, :] = Mat[0:4, :]
    for t in range(99):
        slot = (M_SEG - 99 + t) % RING
        out[4 + t * 9:4 + (t + 1) * 9, :] = \
            Mat[4 + slot * 9:4 + slot * 9 + 9, :]
    return out


def state_to_ring_rows(Mat):
    out = np.zeros((NR, Mat.shape[1]))
    out[0:4, :] = Mat[0:4, :]
    for t in range(99):
        slot = (M_SEG - 99 + t) % RING
        out[4 + slot * 9:4 + slot * 9 + 9, :] = \
            Mat[4 + t * 9:4 + (t + 1) * 9, :]
    return out


def f_rhs_float(Xv, Zdv):
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


from c4_orbit_krawczyk import P4  # noqa: E402


def load_all():
    ck = np.load(CKPT)
    d = {k: ck[k] for k in ck.files}
    # E_abs is reconstructed by the phase-A script and stored
    d['E_abs'] = ck['E_abs'] if 'E_abs' in ck.files else None
    d['X_iv'] = [(d['X0'], d['X1']), (d['X2'], d['X3']),
                 (d['X4'], d['X5']), (d['X6'], d['X7'])]
    d['ZdLag'] = (d['ZdLag_lo'], d['ZdLag_hi'])
    d['Xpt'] = [d['Xpt0'], d['Xpt1'], d['Xpt2'], d['Xpt3']]
    d['rho_iv'] = (float(d['rho_lo'][0]), float(d['rho_hi'][0]))
    return d


def operator_march(d, rad_tube_sin, rad_tube_szd, rad_tube_b, r_p):
    """The block-wrapped affine operator march (Phase-B version, with the
    incremental extent update)."""
    S_in = d['S_in']
    Szd = d['Szd']
    Lw_mid = d['Lw_mid']
    Lw_abs = d['Lw_abs']
    src_slot = d['src_slot']
    ZdP = d['ZdP']
    w_p = d['w_p']
    S_out = S_in[:, 28:32, :]
    sin_abs = np.abs(S_in)
    sout_abs = np.abs(S_out)
    szd_abs = np.abs(Szd)
    rad_sin_full = d['rad_sin_full']
    rad_szd_full = d['rad_szd_full']
    rso_b = rad_sin_full[:, 28:32, :]
    rsz_b = rad_sin_full[:, ZROWS, :]
    zso_b = rad_szd_full[:, 28:32, :]
    zsz_b = rad_szd_full[:, ZROWS, :]
    M = M_SEG
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
    C = np.zeros((NR, NB + 1))
    C[0:4, 0:4] = np.eye(4)
    for t in range(99):
        slot = (M - 99 + t) % RING
        C[4 + slot * 9:4 + slot * 9 + 9,
          4 + t * 9:4 + (t + 1) * 9] = np.eye(9)
    b_box = np.zeros(NR)
    w = np.abs(C).sum(axis=1)
    for j in range(M):
        w_eff = w + r_p * np.abs(C[:, NB])
        # the delayed extents + the delayed reads (shared gather)
        zdw = np.empty(8)
        Zd_rows = np.empty((8, C.shape[1]))
        zdw_b = np.empty(8)
        for i in range(8):
            sl = src_slot[j, i]
            blk = C[4 + sl * 9:4 + sl * 9 + 9, :]
            zdw[i] = Lw_abs[j, i, :] @ w_eff[4 + sl * 9:
                                             4 + sl * 9 + 9]
            Zd_rows[i] = Lw_mid[j, i, :] @ blk
            zdw_b[i] = Lw_abs[j, i, :] @ b_box[4 + sl * 9:
                                               4 + sl * 9 + 9]
        inj_x = rso[j] @ w_eff[0:4] + zso[j] @ zdw
        inj_slot = rsz[j] @ w_eff[0:4] + zsz[j] @ zdw
        rb = rad_b[j]
        # the in-block magnitude accumulation
        bx = b_box[0:4]
        b_x_new = (sout_abs[j] @ bx + szd_abs[j][28:32] @ zdw_b
                   + np.abs(inj_x) + rb)
        b_slot_new = np.empty(9)
        b_slot_new[0] = b_box[2]
        b_slot_new[1:9] = (sin_abs[j][ZROWS] @ bx
                           + szd_abs[j][ZROWS] @ zdw_b
                           + np.abs(inj_slot) + rb)
        # the signed update of all columns
        dst = S_in[j] @ C[0:4, :] + Szd[j] @ Zd_rows
        aff = w_p[j]
        old_z = C[2, :].copy()
        slot = j % RING
        newslot = np.empty((9, C.shape[1]))
        newslot[0] = old_z
        newslot[1:9] = dst[ZROWS, :]
        C[4 + slot * 9:4 + slot * 9 + 9, :] = newslot
        C[0:4, :] = dst[28:32, :]
        C[0:4, NB] += aff[28:32]
        C[4 + slot * 9 + 1:4 + slot * 9 + 9, NB] += aff[ZROWS]
        # the incremental extent update
        w[0:4] = np.abs(C[0:4, :]).sum(axis=1)
        w[4 + slot * 9:4 + slot * 9 + 9] = np.abs(
            C[4 + slot * 9:4 + slot * 9 + 9, :]).sum(axis=1)
        b_box = b_box.copy()
        b_box[0:4] = b_x_new
        b_box[4 + slot * 9:4 + slot * 9 + 9] = b_slot_new
        if (j + 1) % BLOCK == 0:
            newcols = np.zeros((NR, NR))
            newcols[np.arange(NR), np.arange(NR)] = b_box
            C = np.hstack([C, newcols])
            b_box = np.zeros(NR)
            w = np.abs(C).sum(axis=1)
    Mon_cols = ring_to_state_rows(C[:, 0:NB])
    Ap_final = ring_to_state_rows(C[:, NB:NB + 1])[:, 0]
    sym = np.abs(ring_to_state_rows(C[:, NB + 1:]))
    T_unc = _hi(sym.sum(axis=1) * (1.0 + EPS_ACC))
    return Mon_cols, Ap_final, T_unc


def tube_widths(d, r_ball):
    M = M_SEG
    E_abs = d['E_abs']
    X = d['X_iv']
    ZdLag = d['ZdLag']
    Lw_abs = d['Lw_abs']
    jp = d['jp']
    Rinv = d['Rinv']
    rad_Rinv_row = d['rad_Rinv_row']
    R_norm_rows = d['R_norm_rows']
    KD_mid = d['KD_mid']
    P = float(d['P'][0])
    dsig_dp = float(d['dsig_dp'][0])
    dKD_scale = float(d['dKD_scale'][0])
    rho_iv = d['rho_iv']
    f_parts, fE_finish, f_full, jac_parts, jac_finish = make_model(rho_iv)
    n = N
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
    # THE TUBE'S INVERSE VARIATION (the entry-wise E_treatment): the
    # Mhat's tube widths (the J-widths over the inflated tube) drive the
    # inverse's variation through the same (I-E)^{-1} structure:
    #   WM_tube: the J-blocks widened by the tube J-widths (nodes 1..7)
    #   E_tube_abs = E_abs + |Rinv| @ WM_tube
    #   rad_sin_t = |Rinv| @ WB_tube
    #              + (|Rinv| @ E_tube_abs) @ (Bfl_abs_t + WB_tube)/(1-q_t)
    Jw_t = 0.5 * (Jh - Jl)                      # (M, 9, 4, 4)
    WM_tube = np.zeros((M, 32, 32))
    for i in range(1, 8):
        WM_tube[:, i * 4:(i + 1) * 4,
                (i - 1) * 4:i * 4] = Jw_t[:, i, :, :]
    E_tube_abs = E_abs + np.einsum('mik,mkj->mij', np.abs(Rinv), WM_tube)
    q_t_rows = _hi((E_tube_abs.sum(axis=2)) * (1.0 + EPS_ACC))
    q_t = float(q_t_rows.max())
    if q_t >= 1.0:
        raise RuntimeError(f"tube Neumann q = {q_t} >= 1")
    inv_t = 1.0 / np.maximum(1.0 - q_t_rows, 1e-12)
    RE_t = np.einsum('mik,mkj->mij', np.abs(Rinv), E_tube_abs)
    rad_sin_t = _hi(
        np.einsum('mik,mkj->mij', np.abs(Rinv), Bfl_w_t)
        + np.einsum('mik,mkj->mij', RE_t, Bfl_abs_t + Bfl_w_t)
        * inv_t[:, :, None])
    DvBw_t = np.zeros((M, 32, 8))
    DvBa_t = np.zeros((M, 32, 8))
    for i in range(8):
        DvBw_t[:, i * 4 + 3, i] = Dv3_w_t[:, i]
        DvBa_t[:, i * 4 + 3, i] = Dv3_abs_t[:, i]
    rad_szd_t = _hi(
        np.einsum('mik,mkj->mij', np.abs(Rinv), DvBw_t)
        + np.einsum('mik,mkj->mij', RE_t, DvBa_t + DvBw_t)
        * inv_t[:, :, None])
    # THE SOUND INJECTION-TUBE BOUND: the per-step affine injection w_p's
    # variation over the r-ball, channel-explicit (delta w_p =
    # -(ddRinv.F_sub + dRinv.dF + dRinv_t.F_p + Rinv.dF_p)):
    #   (d-3) Rinv.Dv3.dZdP -- the landing-H tube through the weight
    #         DERIVATIVES: sum_l |dL_l/dsigma| |H[patch]| |dsig/dp| r.
    #         The DOMINANT channel (up to 15.6x the old sum|Lw| proxy,
    #         which was therefore unsound); the signed cancellation of
    #         the weight-derivative sum (exact on the constant history
    #         mode) does NOT apply here because the slot-tube variations
    #         are independent.
    #   (d-2) Rinv.dDv3.ZdP -- the Dv3 tube width over the Zd-tube times
    #         the ACTUAL substrate |ZdP| (signed sup ~3e-4; the crude
    #         ZdHm bound would overestimate ~3.5e4x).
    #   (d-1) Rinv.rho'.dJ -- the rho-scaled Jacobian tube variation.
    #   (b)   dRinv.dF -- |dRinv| <= Rn^2 rho' |J|row; |dF| <=
    #         (kd + j + dv.lw) r.
    #   (c)   dRinv_t.F_p -- |dRinv_t| <= 2 Rn^2 jw_row (the tube inverse
    #         variation through the J-widths); |F_p| <= rho' fmag + dv |ZdP|.
    #   (a)   ddRinv.F_sub -- 3 Rn^2 rho' jw F_sup (negligible).
    H_sub = d['Xpt2']
    dLw_dsig = d['dLw_dsig']
    ZdP = d['ZdP']
    F_sup = float(d['F_sup'][0])
    ZdHm = (np.abs(dLw_dsig[:, :8, :])
            * np.abs(H_sub[jp[:, :8], :])).sum(axis=2)          # (M, 8)
    Jw_t = 0.5 * (Jh - Jl)                                     # (M,9,4,4)
    jw_r = Jw_t.sum(axis=3).max(axis=(1, 2))                    # (M,)
    jmid_r = i_abs_hi(Jl, Jh).sum(axis=3).max(axis=(1, 2))      # (M,)
    dv_r = Dv3_abs_t[:, :8].max(axis=1)                         # (M,)
    lw_r = Lw_abs[:, :8].sum(axis=2).max(axis=1)                # (M,)
    kd_sup = float(np.abs(KD_mid).sum(axis=1).max())
    jmid_sup = float(jmid_r.max())
    dv_sup = float(dv_r.max())
    lw_sup = float(lw_r.max())
    jw_sup = float(jw_r.max())
    ZdP_abs = np.abs(ZdP)                                      # (M, 8)
    ZdP_sup = float(ZdP_abs.max())
    # the sound rhs-magnitude bound at the substrate (the float sups
    # inflated by 1e-6 -- covering the point-interval rounding and the
    # rho-family width 2.7e-11 with four orders of margin)
    Xpt = d['Xpt']
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
    b_a = np.full(M_SEG, 3.0 * (float(R_norm_rows.max()) ** 2)
                  * (1.0 / P) * jw_sup * F_sup)
    b_tube = _hi(b_d3 + b_d2 + b_d1 + b_b + b_c + b_a)
    return rad_sin_t, rad_szd_t, b_tube


def load_results():
    if RES.exists():
        with open(RES) as f:
            return json.load(f)
    return {}


def save_results(r):
    with open(RES, "w") as f:
        json.dump(r, f, indent=1, sort_keys=True)


def main():
    t0 = time.time()
    mode = sys.argv[1] if len(sys.argv) > 1 else "final"
    d = load_all()
    res = load_results()
    Mon = d['Mon']
    tang = d['tang']
    Ap = d['Ap']
    Rb = d['Rb']
    q0_b = float(d['q0_b'])
    Rb_norm = float(d['Rb_norm'])
    m_center = d['m_center']
    T_m = d['T_m']

    if mode == "eval":
        print("eval-only operator march ...", flush=True)
        Mon_cols0, Ap0, T_unc0 = operator_march(d, None, None, None, 0.0)
        mon_gap = float(np.abs(Mon_cols0 - Mon).max())
        ap_gap = float(np.abs(Ap0 - Ap).max())
        res["eval"] = {
            "mon_gap": mon_gap, "ap_gap": ap_gap,
            "T_unc0_sup": float(T_unc0.max()),
        }
        np.save(ROOT / "c4_stage4b_Tunc_eval.npy", T_unc0)
        print(f"  mon_gap={mon_gap:.2e} ap_gap={ap_gap:.2e} "
              f"T_unc0_sup={T_unc0.max():.3e}", flush=True)
        save_results(res)
        print(f"done in {time.time() - t0:.1f}s", flush=True)
        return 0

    if mode.startswith("r:"):
        r_try = float(mode[2:])
        print(f"tube widths + operator march at r={r_try:g} ...",
              flush=True)
        rad_sin_t, rad_szd_t, b_tube = tube_widths(d, r_try)
        Mon_cols, Ap_fin, T_unc = operator_march(
            d, rad_sin_t, rad_szd_t, b_tube, r_try)
        mon_gap = float(np.abs(Mon_cols - Mon).max())
        m_pad = np.zeros(NB + 1)
        m_pad[0:NB] = m_center
        Y_center = float(np.abs(Rb @ m_pad).max())
        T_m_pad = np.zeros(NB + 1)
        T_m_pad[0:NB] = T_m
        Y_ext = float((np.abs(Rb) @ T_m_pad).max())
        Y = _hi(Y_center + Y_ext)
        T_all = np.zeros(NB + 1)
        T_all[0:NB] = T_unc
        ZT = float((np.abs(Rb) @ T_all).max())
        Z = _hi(q0_b + (1.0 + r_try) * ZT)
        closure = bool(Y + Z * r_try <= r_try)
        res[f"r_{r_try:g}"] = {
            "Z": float(Z), "Y": float(Y),
            "Y_center": Y_center, "Y_ext": Y_ext,
            "Y_plus_Zr": float(Y + Z * r_try),
            "closure": closure, "mon_gap": mon_gap,
            "T_unc_sup": float(T_unc.max()),
        }
        print(f"  mon_gap={mon_gap:.2e} Z={Z:.6f} Y={Y:.3e} "
              f"Y+Zr={Y + Z * r_try:.3e} closure={closure}", flush=True)
        save_results(res)
        print(f"done in {time.time() - t0:.1f}s", flush=True)
        return 0

    if mode == "checks":
        print("verification checks ...", flush=True)
        checks = {}
        ev = d['ev']
        mon_ev_gap = float(max(abs(ev[0] - COMMITTED_MONODROMY["phase"]),
                               abs(ev[1] - COMMITTED_MONODROMY["dominant"]),
                               abs(ev[2] - COMMITTED_MONODROMY["disc"])))
        checks["monodromy_eigenvalues_vs_committed"] = {
            "top4": [float(v) for v in ev[:4]],
            "max_gap": mon_ev_gap, "pass": bool(mon_ev_gap < 1e-6)}
        tn = float(np.linalg.norm(tang))
        tang_res = float(np.linalg.norm(Mon @ tang - tang) / tn)
        checks["tangent_residual"] = {
            "value": tang_res, "pass": bool(tang_res < 1e-6)}
        m_sup = float(np.abs(m_center).max())
        checks["mismatch_center_vs_stage4a"] = {
            "mpmath_sup": m_sup,
            "stage4a_float": STAGE4A_FLOAT_MISMATCH,
            "gap": abs(m_sup - STAGE4A_FLOAT_MISMATCH),
            "pass": bool(abs(m_sup - STAGE4A_FLOAT_MISMATCH) < 1e-6)}
        checks["mismatch_enclosure_width"] = {
            "T_m_sup": float(T_m.max()), "center_sup": m_sup,
            "pass": bool(T_m.max() < 1e-5)}
        checks["bordered_inverse"] = {
            "q0": q0_b, "norm": Rb_norm,
            "pass": bool(q0_b < 1e-9 and Rb_norm < 1e4)}
        if "eval" in res:
            checks["operator_march_monodromy_consistency"] = {
                "mon_gap": res["eval"]["mon_gap"],
                "pass": bool(res["eval"]["mon_gap"] < 1e-9)}
            checks["operator_march_pcolumn_consistency"] = {
                "ap_gap": res["eval"]["ap_gap"],
                "pass": bool(res["eval"]["ap_gap"]
                             < 1e-9 * max(1.0, float(np.abs(Ap).max())))}
        # the p-column finite-difference check
        print("  p-column finite difference ...", flush=True)
        Xpt = d['Xpt']
        nodes = d['nodes']
        den = d['den']
        Rinv = d['Rinv']
        Lw_mid = d['Lw_mid']
        src_slot = d['src_slot']
        D_mid = d['D_mid']
        M = M_SEG
        n = N
        P = float(d['P'][0])

        def float_mismatch_at_p(p_val):
            # the (a)-formulation: KD = 2M/P fixed; rho scales the rhs;
            # the delay offsets tau*M/(P+p) carry the p-dependence
            two_h = 2.0 * M / P
            rho_v = (P + p_val) / P
            toh = 4.5 * M / (P + p_val)
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

        h_fd = 1e-6
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
        print(f"  pcol_gap={pcol_gap:.3e}", flush=True)

        # the magnitude-vs-signed block check
        print("  magnitude-vs-signed block check ...", flush=True)
        S_in = d['S_in']
        Szd = d['Szd']
        S_out = S_in[:, 28:32, :]
        sin_abs = np.abs(S_in)
        sout_abs = np.abs(S_out)
        szd_abs = np.abs(Szd)
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
                    zdw_b[i] = Lw_abs_row(d, j, i) @ box[4 + sl * 9:
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
        print(f"  mag_ok={mag_ok}", flush=True)

        # the mpmath probe-column containment (one column)
        print("  mpmath probe-column containment ...", flush=True)
        if "eval" in res and (ROOT / "c4_stage4b_Tunc_eval.npy").exists():
            T_unc0 = np.load(ROOT / "c4_stage4b_Tunc_eval.npy")
            k = 400
            unit_state = np.zeros((NB, 1))
            unit_state[k, 0] = 1.0
            unit_ring = state_to_ring_rows(unit_state)[:, 0]
            Ck_mp = [mpf(float(v)) for v in unit_ring]
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
            ring_np = np.array([float(v) for v in Ck_mp])
            state_np = ring_to_state_rows(ring_np[:, None])[:, 0]
            worst = 0.0
            ok = True
            for r_ in range(NB):
                val = float(state_np[r_])
                lo_ = Mon[r_, k] - T_unc0[r_]
                hi_ = Mon[r_, k] + T_unc0[r_]
                if not (lo_ <= val <= hi_):
                    ok = False
                    worst = max(worst, min(abs(val - lo_),
                                           abs(val - hi_)))
            checks["mpmath_probe_column_containment"] = {
                "probe": k, "worst_violation": worst,
                "T_unc0_sup": float(T_unc0.max()),
                "pass": bool(ok)}
            print(f"  probe containment ok={ok} worst={worst:.2e}",
                  flush=True)
        else:
            checks["mpmath_probe_column_containment"] = {
                "pass": False, "note": "eval march not yet run"}
        res["checks"] = checks
        save_results(res)
        print(f"done in {time.time() - t0:.1f}s", flush=True)
        return 0

    if mode == "final":
        print("assembling final JSON ...", flush=True)
        ladder = {k: v for k, v in res.items()
                  if k.startswith("r_")}
        closure_found = any(v.get("closure") for v in ladder.values())
        r_cert = None
        Z_cert = None
        for k, v in ladder.items():
            if v.get("closure"):
                r_cert = float(k[2:])
                Z_cert = v["Z"]
                break
        checks = res.get("checks", {})
        all_pass = all(bool(v.get("pass", False))
                       for v in checks.values()) if checks else False
        ev = d['ev']
        out = {
            "title": ("A1 piecewise-Chebyshev campaign — Stage 4b: the "
                      "correlation-tracking affine march, the rigorous "
                      "monodromy enclosure, and the bordered assembly "
                      "certificate attempt"),
            "status": ("THE ASSEMBLY CERTIFICATE "
                       + ("CLOSED" if closure_found
                          else "NOT CLOSED at the tested radii — the "
                               "obstruction constants recorded honestly")
                       + ("; the discrete periodic collocation fixed "
                          "point of the one-period local-Newton map is "
                          "certified to exist within r (sup-norm, the "
                          "augmented state) of the substrate, at a "
                          "period P + p* with |p*| <= r"
                          if closure_found else "")
                       + ". The continuum orbit-to-solution lift "
                         "remains the recorded next step."),
            "method": {
                "march": ("the block-wrapped affine noise-symbol march: "
                          "the operator columns propagate SIGNED (the "
                          "dichotomy cancellation preserved); the "
                          "interval stage-matrix evaluation widths and "
                          "the tube Jacobian widths inject as fresh "
                          "noise symbols, in-block magnitude-accumulated "
                          "(the 1.00264^BLOCK pessimism paid once per "
                          "block) and block-wrapped into 895 coordinate "
                          "symbols"),
                "bordering": ("the joint (delta, p) system with the "
                              "tangent phase pin and the marched "
                              "dPsi/dp bordering column (the "
                              "(a)-formulation's exact derivative "
                              "structures: KD = 2M/P P-INDEPENDENT, "
                              "drho/dp scaling the rhs/Jacobian, "
                              "dLw/dsigma*dsigma/dp at the delay "
                              "landings (indexed by the landing PATCH), "
                              "dRinv/dp=-Rinv dMhat/dp Rinv)"),
                "krawczyk": ("Y = ||R F(0)|| (the mpmath mismatch "
                             "center + the affine widths), Z = q0 + "
                             "(1+r)|| |R| T_unc(r) ||; the closure "
                             "Y + Z r <= r"),
            },
            "phaseA": {
                "monodromy_top4": [float(v) for v in ev[:4]],
                "bordered_q0": float(d['q0_b']),
                "bordered_inverse_norm": float(d['Rb_norm']),
                "p_column_sup": float(np.abs(d['Ap']).max()),
                "refined_inverse_q0": float(d['q0']),
                "mismatch_mpmath_center_sup":
                    float(np.abs(d['m_center']).max()),
                "mismatch_T_m_sup": float(d['T_m'].max()),
            },
            "ladder": ladder,
            "closure_found": closure_found,
            "certified_radius": r_cert,
            "certified_Z": Z_cert,
            "verification": checks,
            "all_checks_pass": bool(all_pass),
        }
        jpath = ROOT / "c4_piecewise_chebyshev_stage4b.json"
        with open(jpath, "w") as f:
            json.dump(out, f, indent=1, sort_keys=True)
        print(f"written {jpath.name}: closure={closure_found} "
              f"all_checks_pass={all_pass}", flush=True)
        return 0

    print(f"unknown mode {mode}")
    return 1


def Lw_abs_row(d, j, i):
    return d['Lw_abs'][j, i, :]


if __name__ == "__main__":
    sys.exit(main())

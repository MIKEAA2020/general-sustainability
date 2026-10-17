#!/usr/bin/env python3
"""
A005 two-pool specialization test — Edwards Aquifer, San Antonio Pool.

Scored comparison of the H1 two-pool discrete specialization of the A005
groundwater template against the one-pool H0 and the retention baselines on
the locked Wave E panel, four fixed windows.

H1 state form (linear specialization of the A005 template balances
C_f dH_f = R_nat - q_p - l_fs - L_f,  C_s dH_s = l_fs - q_ps - L_s,
l_fs = kappa (H_f - H_s)):

    H_f,t+1 = c0 + cR R_t + cP P_t + cF H_f,t + cL (H_s,t - H_f,t)
              clipped to [H_DRY, H_CAP] after the update (same rule as H0)
    H_s,t+1 = d0 + dF H_f,t + dS H_s,t,   with dF = 1 - dS

The restriction dF = 1 - dS is the template's own "slow pool has no direct
recharge, fills only by leakage" structure (no slow pumpage; constant slow
loss absorbed in d0 <= 0). Two further normalizations are required for
identification and are declared as part of the test protocol:

(i) common J-17 datum for H_s: the template leakage law l_fs = kappa (H_f - H_s)
    is meaningful only with both heads on one datum, and the slow-pool datum
    is otherwise NOT identified -- at fixed dS the design column containing
    H_s carries the vector dS^t, which lies exactly in the span of the
    intercept and the cumulative-loss column w_t = (1 - dS^t)/(1 - dS), so
    the likelihood is exactly flat along H_s -> H_s + gamma (with compensating
c0, d0). The equilibrium initialization H_s,0 = H_f,0 is therefore declared:
    no initial leakage disequilibrium is asserted, and no free transient
    parameter is granted to absorb early-window residual mismatch.
(ii) the affine scale freedom H_s -> beta H_s is killed by dF = 1 - dS.

Estimator: conditional least squares on the one-step fast equation
(conditional expectation of H_f given the observed H_f path), profiled over
the slow pole dS on a deterministic grid; for fixed dS the remaining
parameters enter linearly, with the constant slow loss entering through the
cumulative weight w_t = (1 - dS^t)/(1 - dS) at coefficient theta = cL*d0.

Baselines naive_persist / M1 / M2 / M2m reproduce run_ladder.py exactly
(verbatim function copies; checked against results/fixed_window_scores.csv).

Determinism: fixed grid, numpy.linalg.lstsq, no random numbers, no network.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd
from numpy.linalg import lstsq

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "results"
OUT.mkdir(exist_ok=True)

H_DRY = 610.0
H_CAP = 710.0
K_INST = 660.0  # post-2007 Stage I; Brier target only
WINDOWS = {
    "dor_drawdown": (1934, 1950, 1951, 1956),
    "dor_recovery": (1934, 1956, 1957, 1961),
    "prepermit_wet": (1980, 1990, 1991, 1995),
    "cpm_era": (1997, 2014, 2015, 2023),
}

# --- H1 fit grid (deterministic, declared) --------------------------------
DS_GRID = np.round(np.arange(0.005, 1.0, 0.005), 4)      # 199 values, 0.005..0.995
DS_INTERIOR = (0.015, 0.985)                             # interiority band for dS*
N_PARAMS_H1 = 7                                          # c0,cR,cP,cF,cL,d0,dS
BASELINES = ["naive_persist", "M1", "M2", "M2m"]
RULE_MARGIN = 0.95                                       # >=5% RMSE margin
RULE_MIN_WINS = 3                                        # of 4 windows
RULE_LAG1_TOL = 0.1                                      # lag-1 autocorr tolerance


# --- Verbatim from run_ladder.py (H0/baseline reproduction) ---------------

def clip_H(h: float) -> float:
    return float(np.clip(h, H_DRY, H_CAP))


def load_panel() -> pd.DataFrame:
    p = pd.read_csv(DATA / "annual_panel.csv")
    p = p[p["year"].between(1934, 2023)].copy()
    need = ["H_mean", "R_total", "P_wells"]
    if p[need].isna().any().any():
        raise SystemExit("incomplete primary panel 1934-2023")
    return p.reset_index(drop=True)


def fit_ar1(H: np.ndarray) -> dict:
    y = H[1:]
    X = np.column_stack([np.ones(len(y)), H[:-1]])
    coef, *_ = lstsq(X, y, rcond=None)
    a, phi = float(coef[0]), float(coef[1])
    resid = y - (a + phi * H[:-1])
    return {"a": a, "phi": float(np.clip(phi, -0.99, 1.05)), "sig": float(np.std(resid, ddof=1)) if len(resid) > 2 else 1.0}


def fit_m2(H: np.ndarray, R: np.ndarray, P: np.ndarray) -> dict:
    # dH_t = alpha + beta R_t + gamma P_t + delta H_{t-1}
    dH = H[1:] - H[:-1]
    X = np.column_stack([np.ones(len(dH)), R[1:], P[1:], H[:-1]])
    coef, *_ = lstsq(X, dH, rcond=None)
    alpha, beta, gamma, delta = [float(c) for c in coef]
    fitted = X @ coef
    resid = dH - fitted
    phi = 0.0
    if len(resid) > 3:
        den = float(np.dot(resid[:-1], resid[:-1]))
        phi = float(np.clip((np.dot(resid[1:], resid[:-1]) / den) if den > 0 else 0.0, -0.95, 0.95))
    return {
        "alpha": alpha,
        "beta": beta,
        "gamma": gamma,
        "delta": delta,
        "phi": phi,
        "sig": float(np.std(resid, ddof=1)) if len(resid) > 2 else 1.0,
        "last_resid": float(resid[-1]) if len(resid) else 0.0,
        "_resid": resid,
    }


def step_m2(H, R, P, p, resid=0.0) -> float:
    nxt = H + p["alpha"] + p["beta"] * R + p["gamma"] * P + p["delta"] * H + resid
    return clip_H(nxt)


def forecast_m2(H0, R_path, P_path, p, use_ar=False, last_resid=0.0) -> np.ndarray:
    H = float(H0)
    resid = last_resid
    out = []
    for R, P in zip(R_path, P_path):
        if use_ar:
            resid = p["phi"] * resid
        else:
            resid = 0.0
        H = step_m2(H, R, P, p, resid)
        out.append(H)
    return np.asarray(out)


def scores(y, yhat) -> dict:
    y = np.asarray(y, dtype=float)
    yhat = np.asarray(yhat, dtype=float)
    err = yhat - y
    out = {
        "n": int(len(y)),
        "rmse": float(np.sqrt(np.mean(err**2))),
        "mae": float(np.mean(np.abs(err))),
        "brier_660": float(np.mean(((yhat < K_INST).astype(float) - (y < K_INST).astype(float)) ** 2)),
    }
    if len(y) > 1:
        out["direction"] = float(np.mean(np.sign(np.diff(y)) == np.sign(np.diff(yhat))))
    else:
        out["direction"] = float("nan")
    return out


# --- H1 two-pool estimation ------------------------------------------------

def _design(x, R, P, s_path, w_vec):
    """One-step design rows for t = 0..T-2 (predict x_{t+1})."""
    T = len(x)
    tmax = T - 1
    ones = np.ones(tmax)
    return np.column_stack(
        [ones, R[:tmax], P[:tmax], x[:tmax], s_path[:tmax] - x[:tmax], w_vec[:tmax]]
    )


def fit_h1(x: np.ndarray, R: np.ndarray, P: np.ndarray) -> dict:
    """Profiled conditional least squares for the two-pool state form.

    Profiles the slow pole dS over DS_GRID; the slow head is initialized at
    equilibrium, H_s,0 = H_f,0 (declared datum normalization -- the slow
    head's datum is otherwise unidentified, see module docstring). For each
    dS, OLS of
        x_{t+1} = c0 + cR R_t + cP P_t + cF x_t + cL (s_t^{(0)} - x_t) + theta w_t
    with s^{(0)} the d0=0 slow path and w_t = (1 - dS^t)/(1 - dS), so that
    theta = cL * d0 carries the constant slow loss.
    """
    T = len(x)
    tmax = T - 1
    t_arr = np.arange(T)
    y = x[1:]
    s0 = float(x[0])  # equilibrium initialization

    best = None  # (sse, ds, coef)
    profile_ds = np.empty(len(DS_GRID))
    for i_ds, dS in enumerate(DS_GRID):
        powers = dS ** t_arr                      # dS^t, t = 0..T-1
        # a_t = sum_{j<t} dS^{t-1-j} x_j  (slow-pool accumulation of x)
        a = np.empty(T)
        a[0] = 0.0
        for t in range(1, T):
            a[t] = x[t - 1] + dS * a[t - 1]
        b = (1.0 - dS) * a                        # d0=0 slow path with s0=0
        w = (1.0 - powers) / (1.0 - dS)           # cumulative d0 weight
        s0_path = powers * s0 + b                 # d0=0 slow path given s0
        X = _design(x, R, P, s0_path, w)
        coef, *_ = lstsq(X, y, rcond=None)
        resid = y - X @ coef
        sse = float(resid @ resid)
        profile_ds[i_ds] = sse
        if best is None or sse < best[0]:
            best = (sse, float(dS), coef)

    sse, dS, coef = best
    c0, cR, cP, cF, cL, theta = [float(c) for c in coef]
    d0 = theta / cL if abs(cL) > 1e-10 else 0.0
    degenerate_leakage = abs(cL) <= 1e-10

    # final slow path with fitted d0
    powers = dS ** t_arr
    a = np.empty(T)
    a[0] = 0.0
    for t in range(1, T):
        a[t] = x[t - 1] + dS * a[t - 1]
    b = (1.0 - dS) * a
    w = (1.0 - powers) / (1.0 - dS)
    s_path = powers * s0 + b + d0 * w

    # winning 6-column fitting design (for the condition number) ...
    s0_path_win = powers * s0 + b
    X6 = _design(x, R, P, s0_path_win, w)
    # ... and the physically interpretable 5-column fast equation
    # x_{t+1} = c0 + cR R_t + cP P_t + cF x_t + cL (s_t - x_t) + eps
    # (identical fitted values: cL*(s0_path - x) + theta*w = cL*(s_path - x))
    X5 = np.column_stack(
        [np.ones(tmax), R[:tmax], P[:tmax], x[:tmax], s_path[:tmax] - x[:tmax]]
    )
    fitted = X5 @ np.array([c0, cR, cP, cF, cL])
    resid = y - fitted
    sse_check = float(resid @ resid)
    n_obs = tmax
    df = max(n_obs - N_PARAMS_H1, 1)
    resid_se = float(np.sqrt(sse_check / df))

    leak = cL * (s_path[:tmax] - x[:tmax])
    leak_rms = float(np.sqrt(np.mean(leak**2)))
    leak_rms_demeaned = float(np.sqrt(np.mean((leak - leak.mean()) ** 2)))  # datum-invariant

    def lag1(v):
        v = np.asarray(v, float)
        den = float(np.dot(v, v))
        return float(np.dot(v[1:], v[:-1]) / den) if den > 0 else 0.0

    M = np.array([[cF - cL, cL], [1.0 - dS, dS]])
    poles = np.linalg.eigvals(M)
    cond = float(np.linalg.cond(X6))

    # storage / leakage coefficients (annual step): C_f = 1/cR, kappa = cL*C_f, C_s = kappa/(1-dS)
    C_f = 1.0 / cR if abs(cR) > 1e-12 else float("nan")
    kappa = cL * C_f
    C_s = kappa / (1.0 - dS) if abs(1.0 - dS) > 1e-12 else float("nan")

    # profile diagnostics
    prof_min = float(profile_ds.min())
    band = DS_GRID[profile_ds <= 1.01 * prof_min]
    flat = {
        "profile_sse_min": prof_min,
        "profile_sse_max": float(profile_ds.max()),
        "profile_sse_max_over_min": float(profile_ds.max() / prof_min) if prof_min > 0 else float("inf"),
        "ds_band_within_1pct": [float(band.min()), float(band.max())] if len(band) else None,
        "ds_band_width": float(band.max() - band.min()) if len(band) else 0.0,
        "profile_ds": [float(v) for v in profile_ds],
        "initialization": "H_s,0 = H_f,0 (equilibrium; declared datum normalization)",
    }

    params = {
        "c0": c0, "cR": cR, "cP": cP, "cF": cF, "cL": cL,
        "d0": d0, "dS": dS, "dF": 1.0 - dS, "s0": float(s0),
        "theta_cL_d0": theta,
        "kappa_leakage": float(kappa),
        "C_f_storage": float(C_f),
        "C_s_storage": float(C_s),
        "poles": [[float(np.real(p)), float(np.imag(p))] for p in poles],
        "poles_real": bool(np.all(np.abs(np.imag(poles)) < 1e-9)),
        "poles_max_abs": float(np.max(np.abs(poles))),
        "design_condition_number": cond,
        "degenerate_leakage": degenerate_leakage,
        "n_obs": int(n_obs),
        "n_params": N_PARAMS_H1,
        "residual_df": int(df),
        "sse": sse_check,
        "residual_se": resid_se,
        "leakage_contribution_rms": leak_rms,
        "leakage_contribution_rms_demeaned_datum_invariant": leak_rms_demeaned,
        "resid_lag1_autocorr": lag1(resid),
        "resid": [float(v) for v in resid],
        "slow_path": [float(v) for v in s_path],
        "profile": flat,
    }
    return params


def fit_eliminated(x: np.ndarray, R: np.ndarray, P: np.ndarray) -> dict:
    """Unrestricted eliminated form (restricted ARX(2)) profiled over the slow
    pole — identification cross-check only, not the scored object.

    x_{t+1} = A + B x_t + C x_{t-1} + cR (R_t + rho R_{t-1}) + cP (P_t + rho P_{t-1})
    Identified combos: psi = B - rho (fast own-persistence), product cL*dF =
    C + psi*rho, constant combination A = (1-rho) c0 + cL d0.
    """
    T = len(x)
    y = x[2:]
    x1, x2 = x[1:-1], x[:-2]
    R1, R2 = R[1:-1], R[:-2]
    P1, P2 = P[1:-1], P[:-2]
    best = None
    prof = np.empty(len(DS_GRID))
    for i, rho in enumerate(DS_GRID):
        X = np.column_stack([np.ones(len(y)), x1, x2, R1 + rho * R2, P1 + rho * P2])
        coef, *_ = lstsq(X, y, rcond=None)
        resid = y - X @ coef
        sse = float(resid @ resid)
        prof[i] = sse
        if best is None or sse < best[0]:
            best = (sse, float(rho), [float(c) for c in coef])
    sse, rho, coef = best
    A, B, C, D, F = coef
    psi = B - rho
    product = C + psi * rho
    disc = B * B + 4.0 * C
    poles = (
        [float((B + np.sqrt(disc)) / 2.0), float((B - np.sqrt(disc)) / 2.0)]
        if disc >= 0
        else [float("nan"), float("nan")]
    )
    band = DS_GRID[prof <= 1.01 * prof.min()]
    return {
        "rho_star": rho,
        "A": A, "B": B, "C_arx": C, "cR": D, "cP": F,
        "psi_fast_own": float(psi),
        "cL_dF_product": float(product),
        "product_template_sign_positive": bool(product > 0),
        "poles_real": bool(disc >= 0),
        "poles": poles,
        "sse_min": float(prof.min()),
        "profile_sse_max_over_min": float(prof.max() / prof.min()) if prof.min() > 0 else float("inf"),
        "ds_band_within_1pct": [float(band.min()), float(band.max())] if len(band) else None,
        "n_obs": int(len(y)),
        "note": "OLS on the eliminated equation; composite error is MA(1)-type, so this is an identification cross-check, not the scored fit",
    }


def forecast_h1(Hf0, Hs0, p, R_path, P_path) -> np.ndarray:
    """Causal two-pool forecast; H_f clipped after each update (H0 clip rule)."""
    Hf, Hs = float(Hf0), float(Hs0)
    out = []
    for R, P in zip(R_path, P_path):
        Hf_next = clip_H(p["c0"] + p["cR"] * R + p["cP"] * P + p["cF"] * Hf + p["cL"] * (Hs - Hf))
        Hs_next = p["d0"] + (1.0 - p["dS"]) * Hf + p["dS"] * Hs
        Hf, Hs = Hf_next, Hs_next
        out.append(Hf)
    return np.asarray(out)


def h1_admissibility(p: dict) -> dict:
    dS, dF = p["dS"], p["dF"]
    cL, cF, cR, cP, d0 = p["cL"], p["cF"], p["cR"], p["cP"], p["d0"]
    kappa, C_f, C_s = p["kappa_leakage"], p["C_f_storage"], p["C_s_storage"]
    checks = {
        "A1_slow_pole_in_open_unit_interval": bool(0.0 < dS < 1.0),
        "A1b_slow_pole_interior_of_grid": bool(DS_INTERIOR[0] <= dS <= DS_INTERIOR[1]),
        "A2_leakage_coefficient_positive_and_bounded": bool(0.0 < cL <= 1.0),
        "A3_slow_pool_fills_only_by_leakage": bool(dF > 0.0),
        "A4_flux_signs_cR_positive_cP_negative": bool(cR > 0.0 and cP < 0.0),
        "A5_fast_persistence_in_open_unit_interval": bool(0.0 < cF <= 1.0),
        "A6_poles_real_and_stable": bool(p["poles_real"] and p["poles_max_abs"] < 1.0),
        "A7_constant_slow_loss_nonpositive": bool(d0 <= 0.0),
        "A8_storage_coefficients_positive": bool(kappa > 0.0 and C_f > 0.0 and C_s > 0.0),
    }
    failed = [k for k, v in checks.items() if not v]
    return {
        "checks": checks,
        "failed_checks": failed,
        "admissible": len(failed) == 0,
        "degenerate_leakage": p["degenerate_leakage"],
    }


def lag1_autocorr(v) -> float:
    v = np.asarray(v, float)
    den = float(np.dot(v, v))
    return float(np.dot(v[1:], v[:-1]) / den) if den > 0 else 0.0


def main():
    panel = load_panel()
    years = panel["year"].to_numpy()
    H = panel["H_mean"].to_numpy(float)
    R = panel["R_total"].to_numpy(float)
    P = panel["P_wells"].to_numpy(float)

    # locked-panel digest
    with open(DATA / "annual_panel.csv", "rb") as f:
        panel_sha = hashlib.sha256(f.read()).hexdigest()

    # H0/baseline reproduction reference (read-only)
    ref_path = OUT / "fixed_window_scores.csv"
    ref = pd.read_csv(ref_path)
    repro = []

    rows = []
    record = {
        "object": "A005 H1 two-pool discrete specialization, scored test, Edwards San Antonio Pool (J-17 annual mean, ft AMSL)",
        "runner": "wave_e_edwards/src/run_twopool.py",
        "determinism": (
            "fixed grid (dS: 0.005..0.995 step 0.005), equilibrium initialization H_s,0 = H_f,0, "
            "numpy.linalg.lstsq, deterministic tie-break by grid order; no random numbers; no network"
        ),
        "data": {
            "path": "wave_e_edwards/data/annual_panel.csv",
            "sha256": panel_sha,
            "years": [1934, 2023],
            "n": int(len(panel)),
            "H_mean_range": [float(H.min()), float(H.max())],
            "drivers": ["R_total", "P_wells"],
            "stored_not_used": ["R_east", "Q_comal"],
        },
        "h1_model": {
            "fast": "H_f,t+1 = c0 + cR R_t + cP P_t + cF H_f,t + cL (H_s,t - H_f,t), clipped to [610,710]",
            "slow": "H_s,t+1 = d0 + dF H_f,t + dS H_s,t with dF = 1 - dS (slow pool fills only by leakage)",
            "normalizations": [
                "common J-17 datum for H_s, fixed by the equilibrium initialization H_s,0 = H_f,0 "
                "(the slow head's datum is otherwise unidentified: at fixed dS the likelihood is "
                "exactly flat along H_s -> H_s + gamma)",
                "dF = 1 - dS (template slow balance, no slow pumpage, constant slow loss in d0)",
            ],
            "identification_caveat": (
                "the affine scale freedom H_s -> beta H_s is killed by dF = 1 - dS; the datum "
                "freedom is killed by the declared initialization; what remains identified is "
                "(dS, cR, cP, cF, cL, d0) at the declared normalization, while the unrestricted "
                "record identifies only psi = cF - cL and the product cL*dF "
                "(see eliminated_form cross-check)"
            ),
            "estimator": "conditional least squares on the one-step fast equation, profiled over the slow pole dS",
            "flux_convention": "last training (R,P) persisted, identical to M2",
        },
        "preregistered_retention_rule": {
            "statement": (
                "H1 is retained as an admitted object ONLY IF on held-out data it (i) beats naive persistence, "
                "M1, M2 and M2m on RMSE of H_mean in at least 3 of the 4 fixed windows, with a >=5% RMSE margin "
                "relative to the best of those baselines in each winning window; AND (ii) the fitted parameters "
                "are physically admissible in all four windows; AND (iii) the residual-discipline check passes: "
                "the leakage term's contribution does not exceed the residual standard error in any window and "
                "the residual lag-1 autocorrelation does not increase relative to H0 by more than 0.1. "
                "Otherwise H1 is NOT retained and the verdict is the negative certificate."
            ),
            "margin": "RMSE(H1) <= 0.95 * min(baseline RMSE)",
            "min_winning_windows": RULE_MIN_WINS,
            "lag1_tolerance": RULE_LAG1_TOL,
        },
        "windows": {},
        "h0_reproduction_check": {"compared_against": "wave_e_edwards/results/fixed_window_scores.csv", "rows": []},
    }

    cond_i_wins = []
    cond_ii_all_admissible = True
    cond_iii_leak_ok = True
    cond_iii_lag1_ok = True

    for wname, (a0, a1, b0, b1) in WINDOWS.items():
        tr = (years >= a0) & (years <= a1)
        te = (years >= b0) & (years <= b1)
        i_tr = np.where(tr)[0]
        i_te = np.where(te)[0]
        Htr, Rtr, Ptr = H[tr], R[tr], P[tr]
        n_te = len(i_te)
        y = H[te]

        # --- baselines (verbatim run_ladder conventions) ---
        p1 = fit_ar1(Htr)
        p2 = fit_m2(Htr, Rtr, Ptr)
        H0 = H[i_tr[-1]]
        persist = np.full(n_te, H0)
        m1 = []
        hcur = H0
        for _ in range(i_te[-1] - i_tr[-1]):
            hcur = clip_H(p1["a"] + p1["phi"] * hcur)
            m1.append(hcur)
        offset = i_te[0] - (i_tr[-1] + 1)
        m1 = np.asarray(m1[offset: offset + n_te])
        R_last, P_last = R[i_tr[-1]], P[i_tr[-1]]
        R_mean, P_mean = float(np.mean(Rtr)), float(np.mean(Ptr))
        steps = i_te[-1] - i_tr[-1]
        m2 = forecast_m2(H0, [R_last] * steps, [P_last] * steps, p2)[offset: offset + n_te]
        m2m = forecast_m2(H0, [R_mean] * steps, [P_mean] * steps, p2)[offset: offset + n_te]

        # --- H1 ---
        h1p = fit_h1(Htr, Rtr, Ptr)
        elim = fit_eliminated(Htr, Rtr, Ptr)
        Hs0 = h1p["slow_path"][i_tr[-1] - i_tr[0]]
        h1 = forecast_h1(H0, Hs0, h1p, [R_last] * steps, [P_last] * steps)[offset: offset + n_te]
        h1m = forecast_h1(H0, Hs0, h1p, [R_mean] * steps, [P_mean] * steps)[offset: offset + n_te]  # diagnostic only

        models = {
            "naive_persist": persist,
            "M1": m1,
            "M2": m2,
            "M2m": m2m,
            "H1_two_pool": h1,
        }
        sc = {name: scores(y, yhat) for name, yhat in models.items()}
        sc_diag = {"H1_two_pool_mean_flux_DIAGNOSTIC": scores(y, h1m)}

        for name, yhat in models.items():
            s = sc[name]
            rows.append(
                {
                    "window": wname,
                    "model": name,
                    "train": f"{a0}-{a1}",
                    "test": f"{b0}-{b1}",
                    **s,
                }
            )
            repro_row = {
                "window": wname, "model": name,
                "rmse_this_run": s["rmse"],
            }
            ref_row = ref[(ref["window"] == wname) & (ref["model"] == name)]
            if name in BASELINES:
                if len(ref_row):
                    r = float(ref_row["rmse"].iloc[0])
                    repro_row["rmse_reference"] = r
                    repro_row["abs_diff"] = abs(s["rmse"] - r)
                    repro_row["match"] = bool(abs(s["rmse"] - r) < 1e-9)
                else:
                    repro_row["rmse_reference"] = None
                    repro_row["abs_diff"] = None
                    repro_row["match"] = False  # reference row missing
            else:
                repro_row["rmse_reference"] = None
                repro_row["abs_diff"] = None
                repro_row["match"] = None  # H1 not in the reference ladder
            record["h0_reproduction_check"]["rows"].append(repro_row)

        # --- admissibility ---
        adm = h1_admissibility(h1p)
        if not adm["admissible"]:
            cond_ii_all_admissible = False

        # --- residual discipline ---
        h0_resid = p2["_resid"]
        h0_lag1 = lag1_autocorr(h0_resid)
        h1_lag1 = h1p["resid_lag1_autocorr"]
        leak_ok = bool(h1p["leakage_contribution_rms"] <= h1p["residual_se"])
        lag1_inc = float(h1_lag1 - h0_lag1)
        lag1_ok = bool(lag1_inc <= RULE_LAG1_TOL)
        if not leak_ok:
            cond_iii_leak_ok = False
        if not lag1_ok:
            cond_iii_lag1_ok = False
        discipline = {
            "leakage_contribution_rms_ft": h1p["leakage_contribution_rms"],
            "h1_residual_se_ft": h1p["residual_se"],
            "leakage_leq_residual_se": leak_ok,
            "h0_resid_lag1_autocorr": h0_lag1,
            "h1_resid_lag1_autocorr": h1_lag1,
            "lag1_increase": lag1_inc,
            "lag1_increase_le_0.1": lag1_ok,
            "h0_resid_se_ft": p2["sig"],
        }

        # --- rule condition (i), this window ---
        base_rmse = {b: sc[b]["rmse"] for b in BASELINES}
        h1_rmse = sc["H1_two_pool"]["rmse"]
        best_base = min(base_rmse.values())
        beats_all = all(h1_rmse < v for v in base_rmse.values())
        margin_ok = bool(h1_rmse <= RULE_MARGIN * best_base)
        margin_pct = float(100.0 * (1.0 - h1_rmse / best_base)) if best_base > 0 else float("nan")
        window_win = bool(beats_all and margin_ok)
        if window_win:
            cond_i_wins.append(wname)

        record["windows"][wname] = {
            "train": [int(a0), int(a1)],
            "test": [int(b0), int(b1)],
            "n_train": int(len(i_tr)),
            "n_test": int(n_te),
            "h0_params": {k: p2[k] for k in ("alpha", "beta", "gamma", "delta", "phi", "sig")},
            "h1_params": {k: v for k, v in h1p.items() if k not in ("resid", "slow_path", "profile")},
            "h1_slow_path_train": h1p["slow_path"],
            "h1_profile": h1p["profile"],
            "eliminated_form_crosscheck": elim,
            "admissibility": adm,
            "residual_discipline": discipline,
            "scores": sc,
            "scores_diagnostic_nonpreregistered": sc_diag,
            "rule_condition_i_window": {
                "h1_rmse": h1_rmse,
                "baseline_rmse": base_rmse,
                "best_baseline_rmse": best_base,
                "beats_all_baselines": beats_all,
                "margin_pct_vs_best": margin_pct,
                "margin_ge_5pct": margin_ok,
                "window_win": window_win,
            },
            "paths": {
                "year": years[te].tolist(),
                "obs": y.tolist(),
                **{name: np.asarray(yhat, float).tolist() for name, yhat in models.items()},
            },
        }

    # --- retention rule evaluation ---
    n_wins = len(cond_i_wins)
    cond_i = bool(n_wins >= RULE_MIN_WINS)
    cond_ii = bool(cond_ii_all_admissible)
    cond_iii = bool(cond_iii_leak_ok and cond_iii_lag1_ok)
    retained = bool(cond_i and cond_ii and cond_iii)
    repro_all = all(
        (r["match"] is None) or bool(r["match"]) for r in record["h0_reproduction_check"]["rows"]
    )
    record["h0_reproduction_check"]["all_baseline_rows_match"] = repro_all

    record["retention_rule_evaluation"] = {
        "condition_i_beat_baselines_with_margin": {
            "winning_windows": cond_i_wins,
            "n_winning_windows": n_wins,
            "required": RULE_MIN_WINS,
            "pass": cond_i,
        },
        "condition_ii_physical_admissibility": {
            "per_window": {w: record["windows"][w]["admissibility"]["admissible"] for w in WINDOWS},
            "failed_checks_per_window": {
                w: record["windows"][w]["admissibility"]["failed_checks"] for w in WINDOWS
            },
            "pass": cond_ii,
        },
        "condition_iii_residual_discipline": {
            "per_window": {
                w: {
                    "leakage_leq_residual_se": record["windows"][w]["residual_discipline"]["leakage_leq_residual_se"],
                    "lag1_increase_le_0.1": record["windows"][w]["residual_discipline"]["lag1_increase_le_0.1"],
                }
                for w in WINDOWS
            },
            "pass": cond_iii,
        },
        "retained": retained,
        "verdict": "RETAINED" if retained else "NOT_RETAINED_NEGATIVE_CERTIFICATE",
    }

    df = pd.DataFrame(rows)
    df.to_csv(OUT / "twopool_fixed_window_scores.csv", index=False)
    with open(OUT / "twopool_results.json", "w") as f:
        json.dump(record, f, indent=2)

    print("=== Two-pool specialization test: fixed windows (RMSE ft) ===")
    print(df[["window", "model", "n", "rmse", "mae", "brier_660", "direction"]].to_string(index=False, float_format=lambda x: f"{x:9.3f}"))
    print("\n=== H1 fitted parameters (per window) ===")
    for w, wd in record["windows"].items():
        p = wd["h1_params"]
        print(
            f"{w:15s} dS={p['dS']:.3f} cL={p['cL']:+.4f} cF={p['cF']:+.4f} cR={p['cR']:+.5f} "
            f"cP={p['cP']:+.5f} d0={p['d0']:+.4f} s0={p['s0']:.1f} poles={p['poles']}"
        )
        print(
            f"{'':15s} admissible={wd['admissibility']['admissible']} "
            f"failed={wd['admissibility']['failed_checks']} "
            f"leak_rms={p['leakage_contribution_rms']:.3f} vs resid_se={p['residual_se']:.3f} "
            f"lag1 H0={wd['residual_discipline']['h0_resid_lag1_autocorr']:+.3f} "
            f"H1={wd['residual_discipline']['h1_resid_lag1_autocorr']:+.3f}"
        )
    print("\n=== Retention rule ===")
    print(json.dumps(record["retention_rule_evaluation"], indent=2))
    print(f"\nH0/baseline reproduction vs fixed_window_scores.csv: all match = {repro_all}")


if __name__ == "__main__":
    main()

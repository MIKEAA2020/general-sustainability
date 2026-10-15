#!/usr/bin/env python3
"""
Wave E scored model ladder — Northern cod (NAFO 2J3KL).

Observation: NCAM M-shift SSB, DFO SAR 2016/026 Table A2 (1983–2015).
Catch: coarse regime series from SAR prose, not STATLANT (see data/SOURCES.md).
F and M from Table A2 are NOT used as forecast drivers.

Claim types follow the general theory ledger:
  [D] definition, [L] logical, [E] empirical, [M] modelling, [N] normative.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.optimize import minimize

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "results"
OUT.mkdir(exist_ok=True)

EPS = 1e-3


def load():
    tab = pd.read_csv(DATA / "ncam_2016_table_a2.csv")
    years = tab["year"].to_numpy()
    ssb = tab["ssb_kt"].to_numpy(dtype=float)
    lrp = float(np.mean(ssb[(years >= 1983) & (years <= 1989)]))
    # [E] approximate catch regimes from SAR 2016 prose (pass 1)
    c_reg = np.where(years <= 1991, 240.0, np.where(years == 1992, 120.0, 5.0)).astype(float)
    # [E] year-by-year reconstructed landings (pass 2)
    cat = pd.read_csv(DATA / "catch_schijns_2021.csv")
    c_ann = cat.set_index("year").loc[years, "catch_kt"].to_numpy(dtype=float)
    rv = pd.read_csv(DATA / "rv_fall_abundance_schijns_table3.csv")
    idx = rv.set_index("year").loc[years, "rv_abundance_index"].to_numpy(dtype=float)
    return years, ssb, c_reg, c_ann, idx, lrp


def surplus(S, r, K, s_allee=None):
    S = np.maximum(S, EPS)
    K = max(K, 10.0)
    g = r * S * (1.0 - S / K)
    if s_allee is not None:
        gap = max(K - s_allee, 10.0)
        g = g * (S - s_allee) / gap
    return g


def step(S, C, r, K, s_allee=None, resid=0.0):
    nxt = S + surplus(S, r, K, s_allee) - C + resid
    return float(np.clip(nxt, EPS, 1.0e6))


def fit_params(S, C, allee=False):
    """One-step LS on a training window. [M]"""
    dS = np.diff(S)
    C_use = C[:-1]
    S0 = S[:-1]

    def pack(theta):
        r, K = theta[0], theta[1]
        s = theta[2] if allee else None
        return r, K, s

    def obj(theta):
        r, K, s = pack(theta)
        if r <= 0 or K <= np.max(S0) * 0.5:
            return 1e12
        if allee and not (0.0 < s < 0.8 * K):
            return 1e12
        pred = np.array([surplus(s0, r, K, s) - c for s0, c in zip(S0, C_use)])
        return float(np.mean((pred - dS) ** 2))

    x0 = [0.3, max(np.max(S) * 1.5, 500.0)]
    bounds = [(1e-3, 2.0), (np.max(S0) + 10.0, 5000.0)]
    if allee:
        x0.append(max(np.min(S0) * 0.5, 5.0))
        bounds.append((0.0, np.max(S0)))
    res = minimize(obj, x0, method="L-BFGS-B", bounds=bounds)
    r, K, s = pack(res.x)
    fitted = np.array([surplus(s0, r, K, s) - c for s0, c in zip(S0, C_use)])
    resid = dS - fitted
    phi = 0.0
    sig = float(np.std(resid, ddof=1)) if len(resid) > 2 else 1.0
    if len(resid) > 3:
        num = np.dot(resid[1:], resid[:-1])
        den = np.dot(resid[:-1], resid[:-1])
        phi = float(np.clip(num / den if den > 0 else 0.0, -0.95, 0.95))
    return {
        "r": float(r),
        "K": float(K),
        "s_allee": None if s is None else float(s),
        "phi": phi,
        "sig": max(sig, 1.0),
        "ok": bool(res.success),
        "sse": float(res.fun),
    }


def forecast_path(S_start, C_path, p, use_ar=False, last_resid=0.0):
    S = float(S_start)
    out = []
    resid = last_resid
    for C in C_path:
        if use_ar:
            resid = p["phi"] * resid
        else:
            resid = 0.0
        S = step(S, C, p["r"], p["K"], p["s_allee"], resid)
        out.append(S)
    return np.array(out)


def scores(y, yhat, lrp):
    y = np.asarray(y, dtype=float)
    yhat = np.asarray(yhat, dtype=float)
    err = yhat - y
    rmse = float(np.sqrt(np.mean(err**2)))
    mae = float(np.mean(np.abs(err)))
    log_rmse = float(np.sqrt(np.mean((np.log(yhat) - np.log(y)) ** 2)))
    # Brier for below-LRP using a hard 0/1 forecast from the point prediction
    brier = float(np.mean(((yhat < lrp).astype(float) - (y < lrp).astype(float)) ** 2))
    if len(y) > 1:
        d_obs = np.sign(np.diff(y))
        d_hat = np.sign(np.diff(yhat))
        direction = float(np.mean(d_obs == d_hat))
    else:
        direction = np.nan
    return {
        "n": int(len(y)),
        "rmse": rmse,
        "mae": mae,
        "log_rmse": log_rmse,
        "brier_below_lrp": brier,
        "direction_hit": direction,
    }


@dataclass
class Spec:
    name: str
    allee: bool
    use_regime_C: bool
    use_ar: bool
    delay: int  # 0 = use S_origin, 1 = use S_{origin-1} if available
    note: str


SPECS = [
    Spec("M1_autonomous_Schaefer", False, False, False, 0,
         "Output/autonomous: constant C estimated on train. A014 class."),
    Spec("M1b_autonomous_Allee", True, False, False, 0,
         "Autonomous Allee + constant C."),
    Spec("M2_stockflow_regimeC", False, True, False, 0,
         "Stock-flow: known catch regime, constant productivity."),
    Spec("M3_AR_residual", False, True, True, 0,
         "M2 + AR(1) surplus residual persisted into the test window."),
    Spec("M4_delayed_info", False, True, True, 1,
         "M3 with assessment delay: forecast starts from last available SSB."),
]


def catch_for_model(years, C_reg, train_sl, use_regime):
    if use_regime:
        return C_reg.copy()
    Cbar = float(np.mean(C_reg[train_sl]))
    return np.full_like(C_reg, Cbar, dtype=float)


def run_fixed_windows(years, ssb, C_reg, lrp):
    windows = {
        "collapse": (1983, 1990, 1991, 1995),
        "recovery": (1995, 2007, 2008, 2015),
    }
    rows = []
    paths = {}
    for wname, (a0, a1, b0, b1) in windows.items():
        tr = (years >= a0) & (years <= a1)
        te = (years >= b0) & (years <= b1)
        # need last train state
        i_tr = np.where(tr)[0]
        i_te = np.where(te)[0]
        for spec in SPECS:
            C_all = catch_for_model(years, C_reg, tr, spec.use_regime_C)
            p = fit_params(ssb[tr], C_all[tr], allee=spec.allee)
            start_idx = i_tr[-1] - spec.delay
            if start_idx < i_tr[0]:
                start_idx = i_tr[0]
            S0 = ssb[start_idx]
            # steps from start_idx to each test year
            lead0 = i_te[0] - start_idx
            C_path = C_all[start_idx + 1 : i_te[-1] + 1]
            last_resid = 0.0
            if spec.use_ar and len(i_tr) > 2:
                fitted = np.array(
                    [
                        surplus(ssb[j], p["r"], p["K"], p["s_allee"]) - C_all[j]
                        for j in i_tr[:-1]
                    ]
                )
                last_resid = (np.diff(ssb[i_tr]) - fitted)[-1]
            yhat_full = forecast_path(S0, C_path, p, spec.use_ar, last_resid)
            # align to test years
            offset = i_te[0] - (start_idx + 1)
            yhat = yhat_full[offset : offset + len(i_te)]
            sc = scores(ssb[te], yhat, lrp)
            row = {
                "window": wname,
                "model": spec.name,
                "train": f"{a0}-{a1}",
                "test": f"{b0}-{b1}",
                **sc,
                **{k: p[k] for k in ("r", "K", "s_allee", "phi", "sig", "ok", "sse")},
            }
            rows.append(row)
            paths[f"{wname}:{spec.name}"] = {
                "year": years[te].tolist(),
                "obs": ssb[te].tolist(),
                "pred": yhat.tolist(),
            }
    return pd.DataFrame(rows), paths


def run_rolling(years, ssb, C_reg, lrp, min_train=8, horizons=(1, 5)):
    rows = []
    n = len(years)
    for origin in range(min_train - 1, n - 1):
        tr = np.zeros(n, dtype=bool)
        tr[: origin + 1] = True
        for spec in SPECS:
            C_all = catch_for_model(years, C_reg, tr, spec.use_regime_C)
            if np.sum(tr) < 5:
                continue
            p = fit_params(ssb[tr], C_all[tr], allee=spec.allee)
            start_idx = origin - spec.delay
            if start_idx < 0:
                start_idx = 0
            S0 = ssb[start_idx]
            last_resid = 0.0
            i_tr = np.where(tr)[0]
            if spec.use_ar and len(i_tr) > 2:
                fitted = np.array(
                    [
                        surplus(ssb[j], p["r"], p["K"], p["s_allee"]) - C_all[j]
                        for j in i_tr[:-1]
                    ]
                )
                last_resid = (np.diff(ssb[i_tr]) - fitted)[-1]
            for h in horizons:
                if origin + h >= n:
                    continue
                C_path = C_all[start_idx + 1 : origin + h + 1]
                yhat_full = forecast_path(S0, C_path, p, spec.use_ar, last_resid)
                yhat = float(yhat_full[-1])
                y = float(ssb[origin + h])
                rows.append(
                    {
                        "origin": int(years[origin]),
                        "horizon": int(h),
                        "model": spec.name,
                        "obs": y,
                        "pred": yhat,
                        "below_lrp_obs": int(y < lrp),
                        "below_lrp_pred": int(yhat < lrp),
                        "sqerr": (yhat - y) ** 2,
                        "abserr": abs(yhat - y),
                        "log_sqerr": (np.log(yhat) - np.log(y)) ** 2,
                    }
                )
    df = pd.DataFrame(rows)
    summary = (
        df.groupby(["model", "horizon"], as_index=False)
        .agg(
            n=("sqerr", "size"),
            rmse=("sqerr", lambda s: float(np.sqrt(np.mean(s)))),
            mae=("abserr", "mean"),
            log_rmse=("log_sqerr", lambda s: float(np.sqrt(np.mean(s)))),
            brier=("below_lrp_pred", lambda s: float(np.mean((s - df.loc[s.index, "below_lrp_obs"]) ** 2))),
        )
    )
    return df, summary


def naive_baselines(years, ssb, lrp):
    """Persistence and train-mean: required beating targets. [E]"""
    rows = []
    n = len(years)
    for origin in range(7, n - 1):
        for h in (1, 5):
            if origin + h >= n:
                continue
            y = ssb[origin + h]
            persist = ssb[origin]
            mean = float(np.mean(ssb[: origin + 1]))
            for name, yhat in (("naive_persist", persist), ("naive_train_mean", mean)):
                rows.append(
                    {
                        "origin": int(years[origin]),
                        "horizon": h,
                        "model": name,
                        "obs": float(y),
                        "pred": float(yhat),
                        "below_lrp_obs": int(y < lrp),
                        "below_lrp_pred": int(yhat < lrp),
                        "sqerr": (yhat - y) ** 2,
                        "abserr": abs(yhat - y),
                        "log_sqerr": (np.log(max(yhat, EPS)) - np.log(y)) ** 2,
                    }
                )
    df = pd.DataFrame(rows)
    summary = (
        df.groupby(["model", "horizon"], as_index=False)
        .agg(
            n=("sqerr", "size"),
            rmse=("sqerr", lambda s: float(np.sqrt(np.mean(s)))),
            mae=("abserr", "mean"),
            log_rmse=("log_sqerr", lambda s: float(np.sqrt(np.mean(s)))),
            brier=("below_lrp_pred", lambda s: float(np.mean((s - df.loc[s.index, "below_lrp_obs"]) ** 2))),
        )
    )
    return df, summary


def survey_scaled_state(ssb, idx, train_sl):
    """Median q = SSB / RV index on the training window. [M]
    RV is an assessment *input*, not a fully independent stock.
    Used only as a delayed/noisy start state, never as an F/M driver.
    """
    q = np.median(ssb[train_sl] / np.maximum(idx[train_sl], 1.0))
    return q * idx, float(q)


def run_survey_start(years, ssb, C, idx, lrp):
    """M2 dynamics, start from q*I instead of SSB (information/filter ablation)."""
    rows = []
    n = len(years)
    for origin in range(7, n - 1):
        tr = np.zeros(n, dtype=bool)
        tr[: origin + 1] = True
        zhat, q = survey_scaled_state(ssb, idx, tr)
        p = fit_params(ssb[tr], C[tr], allee=False)
        for h in (1, 5):
            if origin + h >= n:
                continue
            C_path = C[origin + 1 : origin + h + 1]
            yhat = float(forecast_path(zhat[origin], C_path, p, False, 0.0)[-1])
            y = float(ssb[origin + h])
            rows.append(
                {
                    "origin": int(years[origin]),
                    "horizon": int(h),
                    "model": "M2_survey_start",
                    "obs": y,
                    "pred": yhat,
                    "q": q,
                    "below_lrp_obs": int(y < lrp),
                    "below_lrp_pred": int(yhat < lrp),
                    "sqerr": (yhat - y) ** 2,
                    "abserr": abs(yhat - y),
                    "log_sqerr": (np.log(max(yhat, EPS)) - np.log(y)) ** 2,
                }
            )
    df = pd.DataFrame(rows)
    summary = (
        df.groupby(["model", "horizon"], as_index=False)
        .agg(
            n=("sqerr", "size"),
            rmse=("sqerr", lambda s: float(np.sqrt(np.mean(s)))),
            mae=("abserr", "mean"),
            log_rmse=("log_sqerr", lambda s: float(np.sqrt(np.mean(s)))),
            brier=("below_lrp_pred", lambda s: float(np.mean((s - df.loc[s.index, "below_lrp_obs"]) ** 2))),
        )
    )
    return df, summary


def main():
    years, ssb, C_reg, C_ann, idx, lrp = load()
    meta = {
        "series": "NCAM M-shift SSB, DFO SAR 2016/026 Table A2",
        "n_years": int(len(years)),
        "year_min": int(years.min()),
        "year_max": int(years.max()),
        "lrp_1980s_mean_kt": lrp,
        "ssb_2015_over_lrp": float(ssb[years == 2015][0] / lrp),
        "catch_pass1": "regime 240/120/5 kt from SAR prose",
        "catch_pass2": "Schijns et al. 2021 Table 1, tonnes/1000",
        "catch_2015_schijns_kt": float(C_ann[years == 2015][0]),
        "xtencam": "full SSB table not extracted; not pooled",
    }

    # Pass 1 (regime C) kept for comparison
    win_reg, paths_reg = run_fixed_windows(years, ssb, C_reg, lrp)
    roll_reg, sum_reg = run_rolling(years, ssb, C_reg, lrp)
    naive_df, naive_sum = naive_baselines(years, ssb, lrp)

    # Pass 2: annual catch
    win_ann, paths_ann = run_fixed_windows(years, ssb, C_ann, lrp)
    roll_ann, sum_ann = run_rolling(years, ssb, C_ann, lrp)
    surv_df, surv_sum = run_survey_start(years, ssb, C_ann, idx, lrp)

    win_reg.insert(0, "catch", "regime")
    win_ann.insert(0, "catch", "annual")
    win_all = pd.concat([win_reg, win_ann], ignore_index=True)

    sum_reg.insert(0, "catch", "regime")
    sum_ann.insert(0, "catch", "annual")
    naive_sum.insert(0, "catch", "na")
    surv_sum.insert(0, "catch", "annual")
    roll_all = pd.concat([sum_reg, sum_ann, naive_sum, surv_sum], ignore_index=True)

    win_all.to_csv(OUT / "fixed_window_scores.csv", index=False)
    roll_ann.to_csv(OUT / "rolling_forecasts.csv", index=False)
    roll_all.to_csv(OUT / "rolling_summary.csv", index=False)
    surv_df.to_csv(OUT / "survey_start_forecasts.csv", index=False)
    with open(OUT / "paths.json", "w") as f:
        json.dump({"regime": paths_reg, "annual": paths_ann}, f, indent=2)
    with open(OUT / "meta.json", "w") as f:
        json.dump(meta, f, indent=2)

    print("LRP (1983-1989 mean SSB) =", round(lrp, 2), "kt")
    print("2015 SSB / LRP =", round(meta["ssb_2015_over_lrp"], 3))
    print("2015 Schijns catch =", meta["catch_2015_schijns_kt"], "kt")
    cols = ["catch", "window", "model", "rmse", "mae", "log_rmse"]
    print("\n=== Fixed windows (both catch series) ===")
    print(win_all[cols].to_string(index=False, float_format=lambda x: f"{x:8.2f}"))
    print("\n=== Rolling summary ===")
    print(roll_all.to_string(index=False, float_format=lambda x: f"{x:8.2f}"))


if __name__ == "__main__":
    main()

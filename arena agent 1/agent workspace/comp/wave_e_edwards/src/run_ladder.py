#!/usr/bin/env python3
"""
Wave E scored model ladder — Edwards Aquifer, San Antonio Pool.

Primary z: calendar-year mean J-17 elevation (ft AMSL).
Retention: causal models vs naive persistence on z only.
M2_oracle and the Comal fibre cannot promote a module.
"""

from __future__ import annotations

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
K_INST = 660.0  # post-2007 Stage I; Brier only interpreted for origins >= 2007
FIBRE_FIT = (1934, 1950)
MIN_TRAIN = 15
WINDOWS = {
    "dor_drawdown": (1934, 1950, 1951, 1956),
    "dor_recovery": (1934, 1956, 1957, 1961),
    "prepermit_wet": (1980, 1990, 1991, 1995),
    "cpm_era": (1997, 2014, 2015, 2023),
}


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
    # ΔH_t = α + β R_t + γ P_t + δ H_{t-1}
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
    }


def step_m2(H, R, P, p, resid=0.0) -> float:
    nxt = H + p["alpha"] + p["beta"] * R + p["gamma"] * P + p["delta"] * H + resid
    return clip_H(nxt)


def forecast_m1(H0: float, p: dict, h: int) -> float:
    H = float(H0)
    for _ in range(h):
        H = clip_H(p["a"] + p["phi"] * H)
    return H


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


def run_fixed(panel: pd.DataFrame):
    years = panel["year"].to_numpy()
    H = panel["H_mean"].to_numpy(float)
    R = panel["R_total"].to_numpy(float)
    P = panel["P_wells"].to_numpy(float)
    rows = []
    paths = {}
    for wname, (a0, a1, b0, b1) in WINDOWS.items():
        tr = (years >= a0) & (years <= a1)
        te = (years >= b0) & (years <= b1)
        i_tr = np.where(tr)[0]
        i_te = np.where(te)[0]
        Htr, Rtr, Ptr = H[tr], R[tr], P[tr]
        p1 = fit_ar1(Htr)
        p2 = fit_m2(Htr, Rtr, Ptr)
        H0 = H[i_tr[-1]]
        H0_delay = H[i_tr[-2]] if len(i_tr) > 1 else H0
        n_te = len(i_te)
        # persist / mean
        y = H[te]
        persist = np.full(n_te, H0)
        mean = np.full(n_te, float(np.mean(Htr)))
        # M1 iterate
        m1 = []
        hcur = H0
        for _ in range(i_te[-1] - i_tr[-1]):
            hcur = clip_H(p1["a"] + p1["phi"] * hcur)
            m1.append(hcur)
        offset = i_te[0] - (i_tr[-1] + 1)
        m1 = np.asarray(m1[offset : offset + n_te])
        # causal M2: persist last train fluxes
        R_last, P_last = R[i_tr[-1]], P[i_tr[-1]]
        R_mean, P_mean = float(np.mean(Rtr)), float(np.mean(Ptr))
        steps = i_te[-1] - i_tr[-1]
        m2 = forecast_m2(H0, [R_last] * steps, [P_last] * steps, p2)[offset : offset + n_te]
        m2m = forecast_m2(H0, [R_mean] * steps, [P_mean] * steps, p2)[offset : offset + n_te]
        m3 = forecast_m2(H0, [R_last] * steps, [P_last] * steps, p2, True, p2["last_resid"])[
            offset : offset + n_te
        ]
        delay_steps = i_te[-1] - (i_tr[-1] - 1)
        m4_full = forecast_m2(H0_delay, [R_last] * delay_steps, [P_last] * delay_steps, p2, True, p2["last_resid"])
        m4 = m4_full[(i_te[0] - i_tr[-1]) : (i_te[0] - i_tr[-1]) + n_te]
        # oracle: realized R,P on the interval after last train year
        R_or = R[i_tr[-1] + 1 : i_te[-1] + 1]
        P_or = P[i_tr[-1] + 1 : i_te[-1] + 1]
        mor = forecast_m2(H0, R_or, P_or, p2)[offset : offset + n_te]
        models = {
            "naive_persist": persist,
            "naive_mean": mean,
            "M1": m1,
            "M2": m2,
            "M2m": m2m,
            "M3": m3,
            "M4": m4,
            "M2_oracle": mor,
        }
        for name, yhat in models.items():
            sc = scores(y, yhat)
            rows.append(
                {
                    "window": wname,
                    "model": name,
                    "train": f"{a0}-{a1}",
                    "test": f"{b0}-{b1}",
                    **sc,
                    "beta": p2["beta"] if name.startswith("M2") or name in {"M3", "M4"} else np.nan,
                    "gamma": p2["gamma"] if name.startswith("M2") or name in {"M3", "M4"} else np.nan,
                    "phi_m1": p1["phi"] if name == "M1" else np.nan,
                }
            )
            paths[f"{wname}:{name}"] = {
                "year": years[te].tolist(),
                "obs": y.tolist(),
                "pred": np.asarray(yhat, float).tolist(),
            }
    return pd.DataFrame(rows), paths


def run_rolling(panel: pd.DataFrame):
    years = panel["year"].to_numpy()
    H = panel["H_mean"].to_numpy(float)
    R = panel["R_total"].to_numpy(float)
    P = panel["P_wells"].to_numpy(float)
    n = len(years)
    rows = []
    for origin in range(MIN_TRAIN - 1, n - 1):
        Htr, Rtr, Ptr = H[: origin + 1], R[: origin + 1], P[: origin + 1]
        p1 = fit_ar1(Htr)
        p2 = fit_m2(Htr, Rtr, Ptr)
        H0 = H[origin]
        H0_delay = H[origin - 1]
        R_last, P_last = R[origin], P[origin]
        R_mean, P_mean = float(np.mean(Rtr)), float(np.mean(Ptr))
        for h in (1, 5):
            if origin + h >= n:
                continue
            y = float(H[origin + h])
            preds = {
                "naive_persist": H0,
                "naive_mean": float(np.mean(Htr)),
                "M1": forecast_m1(H0, p1, h),
                "M2": float(forecast_m2(H0, [R_last] * h, [P_last] * h, p2)[-1]),
                "M2m": float(forecast_m2(H0, [R_mean] * h, [P_mean] * h, p2)[-1]),
                "M3": float(forecast_m2(H0, [R_last] * h, [P_last] * h, p2, True, p2["last_resid"])[-1]),
                "M4": float(forecast_m2(H0_delay, [R_last] * (h + 1), [P_last] * (h + 1), p2, True, p2["last_resid"])[-1]),
                "M2_oracle": float(forecast_m2(H0, R[origin + 1 : origin + h + 1], P[origin + 1 : origin + h + 1], p2)[-1]),
            }
            for name, yhat in preds.items():
                rows.append(
                    {
                        "origin": int(years[origin]),
                        "horizon": int(h),
                        "model": name,
                        "obs": y,
                        "pred": float(yhat),
                        "below_660_obs": int(y < K_INST),
                        "below_660_pred": int(yhat < K_INST),
                        "sqerr": (yhat - y) ** 2,
                        "abserr": abs(yhat - y),
                    }
                )
    df = pd.DataFrame(rows)
    summary = (
        df.groupby(["model", "horizon"], as_index=False)
        .agg(
            n=("sqerr", "size"),
            rmse=("sqerr", lambda s: float(np.sqrt(np.mean(s)))),
            mae=("abserr", "mean"),
            brier_660=("below_660_pred", lambda s: float(np.mean((s - df.loc[s.index, "below_660_obs"]) ** 2))),
        )
    )
    return df, summary


def fit_fibre_map(panel: pd.DataFrame):
    m = panel[panel["year"].between(*FIBRE_FIT) & panel["Q_comal"].notna()]
    H = m["H_mean"].to_numpy(float)
    Q = m["Q_comal"].to_numpy(float)
    X = np.column_stack([np.ones(len(H)), H])
    coef, *_ = lstsq(X, Q, rcond=None)
    return float(coef[0]), float(coef[1])


def fibre_after_freeze(panel: pd.DataFrame, roll: pd.DataFrame, c0: float, c1: float):
    """Apply frozen map to already-issued H forecasts. Cannot change retention."""
    years = panel["year"].to_numpy()
    Q = panel["Q_comal"].to_numpy(float)
    ymap = {int(y): float(q) for y, q in zip(years, Q) if np.isfinite(q)}
    rows = []
    sub = roll[roll["horizon"] == 1].copy()
    for rec in sub.itertuples(index=False):
        target = rec.origin + rec.horizon
        if target not in ymap:
            continue
        qhat = c0 + c1 * rec.pred
        qobs = ymap[target]
        rows.append(
            {
                "origin": rec.origin,
                "model": rec.model,
                "Q_obs": qobs,
                "Q_hat": qhat,
                "sqerr": (qhat - qobs) ** 2,
            }
        )
    df = pd.DataFrame(rows)
    summary = (
        df.groupby("model", as_index=False)
        .agg(n=("sqerr", "size"), rmse=("sqerr", lambda s: float(np.sqrt(np.mean(s)))))
    )
    return df, summary


def retention(summary: pd.DataFrame) -> dict:
    h1 = summary[summary["horizon"] == 1].set_index("model")["rmse"]
    persist = float(h1["naive_persist"])
    order = ["M1", "M2", "M2m", "M3", "M4"]
    simpler = {
        "M1": persist,
        "M2": min(persist, float(h1["M1"])),
        "M2m": min(persist, float(h1["M1"])),
        "M3": min(persist, float(h1["M2"])),
        "M4": min(persist, float(h1["M3"])),
    }
    listed = []
    for m in order:
        if float(h1[m]) < persist and float(h1[m]) < simpler[m]:
            listed.append(m)
    # Class demotion (protocol + manuscript §5): M2m with constant
    # fluxes is affine AR(1), not extra stock-flow structure.
    class_demoted = [m for m in listed if m == "M2m"]
    retained_as_structure = [m for m in listed if m not in class_demoted]
    return {
        "primary": "rolling h=1 RMSE of annual-mean J-17 (ft)",
        "persist_h1": persist,
        "listed_by_point_rule": listed,
        "class_demoted": class_demoted,
        "retained_as_structure": retained_as_structure,
        "rejected": [m for m in order if m not in listed],
        "oracle_excluded": True,
        "fibre_excluded": True,
        "rule": "list if primary RMSE < persist AND < next-simpler causal model; then demote constant-flux M2m (AR(1), not extra structure)",
    }


def main():
    panel = load_panel()
    fixed, paths = run_fixed(panel)
    roll, summary = run_rolling(panel)
    c0, c1 = fit_fibre_map(panel)
    fibre_df, fibre_sum = fibre_after_freeze(panel, roll, c0, c1)
    dec = retention(summary)
    dec["fibre_map"] = {"fit": "1934-1950", "c0": c0, "c1": c1}

    # post-2007 Brier slice (interpretation window for 660)
    modern = roll[roll["origin"] >= 2007]
    modern_sum = (
        modern.groupby(["model", "horizon"], as_index=False)
        .agg(
            n=("sqerr", "size"),
            rmse=("sqerr", lambda s: float(np.sqrt(np.mean(s)))),
            brier_660=("below_660_pred", lambda s: float(np.mean((s - modern.loc[s.index, "below_660_obs"]) ** 2))),
        )
        if len(modern)
        else pd.DataFrame()
    )

    meta = {
        "omega": "Edwards Aquifer San Antonio Pool / J-17 annual mean ft AMSL",
        "years": [1934, 2023],
        "n": int(len(panel)),
        "H_1934": float(panel.loc[panel.year == 1934, "H_mean"].iloc[0]),
        "H_1956": float(panel.loc[panel.year == 1956, "H_mean"].iloc[0]),
        "Hmin_1956": float(panel.loc[panel.year == 1956, "H_min"].iloc[0]),
        "H_1992": float(panel.loc[panel.year == 1992, "H_mean"].iloc[0]),
        "Hmax_1992": float(panel.loc[panel.year == 1992, "H_max"].iloc[0]),
        "H_2023": float(panel.loc[panel.year == 2023, "H_mean"].iloc[0]),
        "K_inst_660": K_INST,
        "K_phys_note": "Comal ceases ~618 ft; 1956 daily min 612.51",
        "retention": dec,
    }

    fixed.to_csv(OUT / "fixed_window_scores.csv", index=False)
    roll.to_csv(OUT / "rolling_forecasts.csv", index=False)
    summary.to_csv(OUT / "rolling_summary.csv", index=False)
    fibre_df.to_csv(OUT / "fibre_comal_forecasts.csv", index=False)
    fibre_sum.to_csv(OUT / "fibre_comal_summary.csv", index=False)
    modern_sum.to_csv(OUT / "rolling_modern_2007.csv", index=False)
    with open(OUT / "paths.json", "w") as f:
        json.dump(paths, f, indent=2)
    with open(OUT / "meta.json", "w") as f:
        json.dump(meta, f, indent=2)

    print("=== Fixed windows (RMSE ft) ===")
    print(fixed[["window", "model", "rmse", "mae", "brier_660"]].to_string(index=False, float_format=lambda x: f"{x:8.3f}"))
    print("\n=== Rolling summary ===")
    print(summary.to_string(index=False, float_format=lambda x: f"{x:8.3f}"))
    print("\n=== Fibre Comal (after freeze) ===")
    print(fibre_sum.to_string(index=False, float_format=lambda x: f"{x:8.3f}"))
    print("\n=== Retention ===")
    print(json.dumps(dec, indent=2))


if __name__ == "__main__":
    main()

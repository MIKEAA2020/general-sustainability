#!/usr/bin/env python3
"""
Pass 2 — causal recharge forecasts, scored on J-17.

Retention: rolling h=1 RMSE of H, vs persist AND vs M1.
R-forecast RMSE is reported and cannot retain.
M2_precip_oracle cannot retain.
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

H_DRY, H_CAP = 610.0, 710.0
MIN_TRAIN = 15
WINDOWS = {
    "dor_drawdown": (1934, 1950, 1951, 1956),
    "dor_recovery": (1934, 1956, 1957, 1961),
    "prepermit_wet": (1980, 1990, 1991, 1995),
    "cpm_era": (1997, 2014, 2015, 2023),
}


def clip_H(h):
    return float(np.clip(h, H_DRY, H_CAP))


def load():
    p = pd.read_csv(DATA / "annual_panel.csv")
    p = p[p.year.between(1934, 2023)].copy()
    need = ["H_mean", "R_total", "P_wells", "nino34_son", "pcp_mean"]
    if p[need].isna().any().any():
        raise SystemExit("incomplete pass-2 panel")
    return p.reset_index(drop=True)


def ols(X, y):
    coef, *_ = lstsq(X, y, rcond=None)
    return np.asarray(coef, float)


def fit_m2(H, R, P):
    dH = H[1:] - H[:-1]
    X = np.column_stack([np.ones(len(dH)), R[1:], P[1:], H[:-1]])
    c = ols(X, dH)
    return {"alpha": c[0], "beta": c[1], "gamma": c[2], "delta": c[3]}


def step_m2(H, R, P, p):
    return clip_H(H + p["alpha"] + p["beta"] * R + p["gamma"] * P + p["delta"] * H)


def fit_ar1(H):
    y = H[1:]
    c = ols(np.column_stack([np.ones(len(y)), H[:-1]]), y)
    return {"a": float(c[0]), "phi": float(np.clip(c[1], -0.99, 1.05))}


def fit_rmap(R, son, pcp, kind):
    """Predict R[1:] from information at the previous year."""
    y = R[1:]
    if kind == "ar":
        X = np.column_stack([np.ones(len(y)), R[:-1]])
    elif kind == "enso":
        X = np.column_stack([np.ones(len(y)), son[:-1]])
    elif kind == "precip":
        X = np.column_stack([np.ones(len(y)), pcp[:-1]])
    elif kind == "combo":
        X = np.column_stack([np.ones(len(y)), R[:-1], son[:-1], pcp[:-1]])
    elif kind == "precip_now":
        # contemporaneous R_t ~ pcp_t  (oracle when pcp_{t+k} is used)
        X = np.column_stack([np.ones(len(R)), pcp])
        return {"kind": kind, "coef": ols(X, R)}
    else:
        raise ValueError(kind)
    return {"kind": kind, "coef": ols(X, y)}


def pred_R(rmap, R_t, son_t, pcp_t, pcp_future=None):
    c = rmap["coef"]
    k = rmap["kind"]
    if k == "ar":
        return float(c[0] + c[1] * R_t)
    if k == "enso":
        return float(c[0] + c[1] * son_t)
    if k == "precip":
        return float(c[0] + c[1] * pcp_t)
    if k == "combo":
        return float(c[0] + c[1] * R_t + c[2] * son_t + c[3] * pcp_t)
    if k == "precip_now":
        return float(c[0] + c[1] * pcp_future)
    raise ValueError(k)


def forecast_H(H0, R_path, P_path, p2):
    H = float(H0)
    out = []
    for R, P in zip(R_path, P_path):
        H = step_m2(H, R, P, p2)
        out.append(H)
    return np.asarray(out)


def scores(y, yhat):
    y, yhat = np.asarray(y, float), np.asarray(yhat, float)
    err = yhat - y
    return {
        "n": int(len(y)),
        "rmse": float(np.sqrt(np.mean(err**2))),
        "mae": float(np.mean(np.abs(err))),
    }


def run_fixed(panel):
    years = panel.year.to_numpy()
    H = panel.H_mean.to_numpy(float)
    R = panel.R_total.to_numpy(float)
    P = panel.P_wells.to_numpy(float)
    son = panel.nino34_son.to_numpy(float)
    pcp = panel.pcp_mean.to_numpy(float)
    kinds = ["ar", "enso", "precip", "combo", "precip_now"]
    rows = []
    for wname, (a0, a1, b0, b1) in WINDOWS.items():
        tr = (years >= a0) & (years <= a1)
        te = (years >= b0) & (years <= b1)
        i_tr, i_te = np.where(tr)[0], np.where(te)[0]
        p2 = fit_m2(H[tr], R[tr], P[tr])
        p1 = fit_ar1(H[tr])
        H0 = H[i_tr[-1]]
        n_te = len(i_te)
        offset = i_te[0] - (i_tr[-1] + 1)
        steps = i_te[-1] - i_tr[-1]
        P_last = P[i_tr[-1]]
        # persist / M1
        persist = np.full(n_te, H0)
        hcur = H0
        m1 = []
        for _ in range(steps):
            hcur = clip_H(p1["a"] + p1["phi"] * hcur)
            m1.append(hcur)
        m1 = np.asarray(m1[offset : offset + n_te])
        models = {"naive_persist": persist, "M1": m1}
        rmaps = {k: fit_rmap(R[tr], son[tr], pcp[tr], k) for k in kinds}
        for k, rmap in rmaps.items():
            if k == "precip_now":
                R_path = [pred_R(rmap, None, None, None, pcp[i_tr[-1] + j + 1]) for j in range(steps)]
                name = "M2_precip_oracle"
            else:
                Rhat = pred_R(rmap, R[i_tr[-1]], son[i_tr[-1]], pcp[i_tr[-1]])
                R_path = [Rhat] * steps
                name = f"M2_R{k}" if k != "combo" else "M2_combo"
            yhat = forecast_H(H0, R_path, [P_last] * steps, p2)[offset : offset + n_te]
            models[name] = yhat
            # R score on the test years
            Rhat_te = np.array(R_path[offset : offset + n_te])
            rsc = scores(R[te], Rhat_te)
            rows.append(
                {
                    "window": wname,
                    "model": name,
                    "target": "R",
                    **rsc,
                }
            )
        y = H[te]
        for name, yhat in models.items():
            sc = scores(y, yhat)
            rows.append({"window": wname, "model": name, "target": "H", **sc})
    return pd.DataFrame(rows)


def run_rolling(panel):
    years = panel.year.to_numpy()
    H = panel.H_mean.to_numpy(float)
    R = panel.R_total.to_numpy(float)
    P = panel.P_wells.to_numpy(float)
    son = panel.nino34_son.to_numpy(float)
    pcp = panel.pcp_mean.to_numpy(float)
    n = len(years)
    kinds = ["ar", "enso", "precip", "combo"]
    rows = []
    for origin in range(MIN_TRAIN - 1, n - 1):
        sl = slice(0, origin + 1)
        p2 = fit_m2(H[sl], R[sl], P[sl])
        p1 = fit_ar1(H[sl])
        rmaps = {k: fit_rmap(R[sl], son[sl], pcp[sl], k) for k in kinds}
        rmaps["precip_now"] = fit_rmap(R[sl], son[sl], pcp[sl], "precip_now")
        H0, P_last = H[origin], P[origin]
        for h in (1, 5):
            if origin + h >= n:
                continue
            yH = float(H[origin + h])
            yR = float(R[origin + h])
            preds = {
                "naive_persist": H0,
                "M1": (lambda hh: (lambda x: [x := clip_H(p1["a"] + p1["phi"] * x) for _ in range(hh)][-1])(H0))(h),
            }
            R_paths = {}
            for k in kinds:
                Rhat = pred_R(rmaps[k], R[origin], son[origin], pcp[origin])
                R_paths[k] = [Rhat] * h
            R_paths["precip_now"] = [
                pred_R(rmaps["precip_now"], None, None, None, pcp[origin + j + 1]) for j in range(h)
            ]
            name_of = {
                "ar": "M2_Rar",
                "enso": "M2_enso",
                "precip": "M2_precip",
                "combo": "M2_combo",
                "precip_now": "M2_precip_oracle",
            }
            for k, path in R_paths.items():
                preds[name_of[k]] = float(forecast_H(H0, path, [P_last] * h, p2)[-1])
                rows.append(
                    {
                        "origin": int(years[origin]),
                        "horizon": int(h),
                        "model": name_of[k],
                        "target": "R",
                        "obs": yR,
                        "pred": float(path[-1]),
                        "sqerr": (path[-1] - yR) ** 2,
                        "abserr": abs(path[-1] - yR),
                    }
                )
            # persist-R as R baseline
            rows.append(
                {
                    "origin": int(years[origin]),
                    "horizon": int(h),
                    "model": "R_persist",
                    "target": "R",
                    "obs": yR,
                    "pred": float(R[origin]),
                    "sqerr": (R[origin] - yR) ** 2,
                    "abserr": abs(R[origin] - yR),
                }
            )
            rows.append(
                {
                    "origin": int(years[origin]),
                    "horizon": int(h),
                    "model": "R_mean",
                    "target": "R",
                    "obs": yR,
                    "pred": float(np.mean(R[sl])),
                    "sqerr": (np.mean(R[sl]) - yR) ** 2,
                    "abserr": abs(np.mean(R[sl]) - yR),
                }
            )
            for name, yhat in preds.items():
                rows.append(
                    {
                        "origin": int(years[origin]),
                        "horizon": int(h),
                        "model": name,
                        "target": "H",
                        "obs": yH,
                        "pred": float(yhat),
                        "sqerr": (yhat - yH) ** 2,
                        "abserr": abs(yhat - yH),
                    }
                )
    return pd.DataFrame(rows)


def summarize(df, target):
    sub = df[df.target == target]
    return (
        sub.groupby(["model", "horizon"], as_index=False)
        .agg(
            n=("sqerr", "size"),
            rmse=("sqerr", lambda s: float(np.sqrt(np.mean(s)))),
            mae=("abserr", "mean"),
        )
        .sort_values(["horizon", "rmse"])
    )


def retention(h_sum):
    h1 = h_sum[h_sum.horizon == 1].set_index("model")["rmse"]
    persist = float(h1["naive_persist"])
    m1 = float(h1["M1"])
    cands = ["M2_Rar", "M2_enso", "M2_precip", "M2_combo"]
    retained = [m for m in cands if float(h1[m]) < persist and float(h1[m]) < m1]
    return {
        "persist_h1": persist,
        "M1_h1": m1,
        "retained": retained,
        "rejected": [m for m in cands if m not in retained],
        "oracle_excluded": True,
        "rule": "retain only if H RMSE < persist AND < M1",
    }


def main():
    panel = load()
    fixed = run_fixed(panel)
    roll = run_rolling(panel)
    h_sum = summarize(roll, "H")
    r_sum = summarize(roll, "R")
    dec = retention(h_sum)
    meta = {
        "pass": 2,
        "predictors": "SON nino34 (1991-2020 clim), TX CD06+CD07 precip, lagged R",
        "retention": dec,
    }
    fixed.to_csv(OUT / "pass2_fixed.csv", index=False)
    roll.to_csv(OUT / "pass2_rolling.csv", index=False)
    h_sum.to_csv(OUT / "pass2_H_summary.csv", index=False)
    r_sum.to_csv(OUT / "pass2_R_summary.csv", index=False)
    with open(OUT / "pass2_meta.json", "w") as f:
        json.dump(meta, f, indent=2)
    print("=== Rolling H RMSE ===")
    print(h_sum.to_string(index=False, float_format=lambda x: f"{x:8.3f}"))
    print("\n=== Rolling R RMSE ===")
    print(r_sum.to_string(index=False, float_format=lambda x: f"{x:8.3f}"))
    print("\n=== Fixed H ===")
    print(
        fixed[fixed.target == "H"][["window", "model", "rmse"]]
        .to_string(index=False, float_format=lambda x: f"{x:8.3f}")
    )
    print("\n=== Retention ===")
    print(json.dumps(dec, indent=2))


if __name__ == "__main__":
    main()

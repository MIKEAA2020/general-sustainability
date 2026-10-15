#!/usr/bin/env python3
"""
Capelin-W ablation without a year-by-year acoustic table.

Published facts used [E]:
  - 2J3KL capelin acoustic index collapsed in 1991
  - 1985–90 median 3704 kt vs 1991–2022 median 174 kt (Murphy et al. 2025 / DFO 2024/050)

Not used: a digitized Figure 15. That would be unofficial.

Module M_cap: two-regime intrinsic rate, break at 1991.
  Forecast from origin o uses r_lo iff o >= 1991 (regime already observed).
  Collapse forecasts issued before 1991 do NOT see the break.

Retention: beat naive persist on primary RMSE.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.optimize import minimize

sys.path.insert(0, str(Path(__file__).resolve().parent))
from run_ladder import DATA, OUT, EPS, surplus, step, scores, naive_baselines

BREAK = 1991  # first low-capelin year [E]


def fit_two_r(years, S, C):
    dS = np.diff(S)
    y0, S0, C0 = years[:-1], S[:-1], C[:-1]
    hi = y0 < BREAK
    lo = ~hi

    def obj(th):
        r_hi, r_lo, K = th
        if min(r_hi, r_lo) <= 0 or K <= np.max(S0) * 0.5:
            return 1e12
        pred = np.array(
            [
                surplus(s, (r_hi if h else r_lo), K, None) - c
                for s, c, h in zip(S0, C0, hi)
            ]
        )
        return float(np.mean((pred - dS) ** 2))

    x0 = [0.3, 0.15, max(np.max(S) * 1.4, 400.0)]
    bnds = [(1e-3, 2.0), (1e-3, 2.0), (np.max(S0) + 10.0, 8000.0)]
    res = minimize(obj, x0, method="L-BFGS-B", bounds=bnds)
    r_hi, r_lo, K = map(float, res.x)
    # if a regime is absent in train, copy the other
    if not np.any(hi):
        r_hi = r_lo
    if not np.any(lo):
        r_lo = r_hi
    return {"r_hi": r_hi, "r_lo": r_lo, "K": K, "ok": bool(res.success), "sse": float(res.fun)}


def r_for_origin(p, origin_year):
    return p["r_lo"] if origin_year >= BREAK else p["r_hi"]


def rolling(years, ssb, C, lrp, min_train=12, tag=""):
    n = len(years)
    rows = []
    for origin in range(min_train - 1, n - 1):
        tr = np.zeros(n, dtype=bool)
        tr[: origin + 1] = True
        p = fit_two_r(years[tr], ssb[tr], C[tr])
        r = r_for_origin(p, int(years[origin]))
        for h in (1, 5):
            if origin + h >= n:
                continue
            S = float(ssb[origin])
            for k in range(h):
                S = step(S, C[origin + 1 + k], r, p["K"], None, 0.0)
            y = float(ssb[origin + h])
            rows.append(
                {
                    "tag": tag,
                    "origin": int(years[origin]),
                    "horizon": h,
                    "model": "M_cap_regime1991",
                    "obs": y,
                    "pred": S,
                    "r_used": r,
                    "r_hi": p["r_hi"],
                    "r_lo": p["r_lo"],
                    "sqerr": (S - y) ** 2,
                    "abserr": abs(S - y),
                    "log_sqerr": (np.log(max(S, EPS)) - np.log(y)) ** 2,
                    "below_lrp_obs": int(y < lrp),
                    "below_lrp_pred": int(S < lrp),
                    "post_break_origin": int(years[origin] >= BREAK),
                }
            )
    df = pd.DataFrame(rows)
    summ = (
        df.groupby(["tag", "model", "horizon", "post_break_origin"], as_index=False)
        .agg(
            n=("sqerr", "size"),
            rmse=("sqerr", lambda s: float(np.sqrt(np.mean(s)))),
            mae=("abserr", "mean"),
            log_rmse=("log_sqerr", lambda s: float(np.sqrt(np.mean(s)))),
        )
    )
    alls = (
        df.groupby(["tag", "model", "horizon"], as_index=False)
        .agg(
            n=("sqerr", "size"),
            rmse=("sqerr", lambda s: float(np.sqrt(np.mean(s)))),
            mae=("abserr", "mean"),
            log_rmse=("log_sqerr", lambda s: float(np.sqrt(np.mean(s)))),
        )
    )
    return df, summ, alls


def load_ncam():
    tab = pd.read_csv(DATA / "ncam_2016_table_a2.csv")
    cat = pd.read_csv(DATA / "catch_schijns_2021.csv")
    years = tab.year.to_numpy()
    C = cat.set_index("year").loc[years, "catch_kt"].to_numpy(float)
    lrp = float(np.mean(tab.ssb_kt[(tab.year >= 1983) & (tab.year <= 1989)]))
    return years, tab.ssb_kt.to_numpy(float), C, lrp


def load_xte():
    ssb = pd.read_csv(DATA / "xtencam_table17_ssb.csv")
    cat = pd.read_csv(DATA / "dfo_2025_table1_landings.csv")
    df = ssb.merge(cat[["year", "catch_kt"]], on="year", how="left")
    df["catch_kt"] = df["catch_kt"].ffill()
    return df.year.to_numpy(), df.ssb_kt.to_numpy(float), df.catch_kt.to_numpy(float), 276.0


def main():
    frames, sums, alls = [], [], []
    for tag, loader, min_tr in (("ncam2016", load_ncam, 8), ("xteNCAM", load_xte, 12)):
        years, ssb, C, lrp = loader()
        df, sm, al = rolling(years, ssb, C, lrp, min_tr, tag)
        _, naive = naive_baselines(years, ssb, lrp)
        naive = naive.copy()
        naive.insert(0, "tag", tag)
        frames.append(df)
        sums.append(sm)
        alls.append(al)
        alls.append(naive)
        print(f"\n=== {tag} LRP={lrp:.1f} ===")
        print(al.to_string(index=False, float_format=lambda x: f"{x:8.1f}"))
        print("by pre/post break origin:")
        print(sm.to_string(index=False, float_format=lambda x: f"{x:8.1f}"))
        print("naive:")
        print(naive.to_string(index=False, float_format=lambda x: f"{x:8.1f}"))

    pd.concat(frames).to_csv(OUT / "capelin_regime_forecasts.csv", index=False)
    pd.concat(alls).to_csv(OUT / "capelin_regime_summary.csv", index=False)
    print("\nwrote results/capelin_regime_*.csv")
    print("NOTE: year-by-year acoustic I_t was figure-only (Murphy 2025 Fig. 15); not digitized.")


if __name__ == "__main__":
    main()

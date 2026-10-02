#!/usr/bin/env python3
"""
Continuous capelin-W ablation using OBSERVED acoustic years only.

I_t = last observed spring acoustic biomass at or before t (causal carry-forward).
No Gaussian-process fill. No pre-collapse values carried across 1991.

At origin o the forecast uses I_known(o) only — later surveys are not seen.

surplus = r * S * (1-S/K) * (I_known / I_ref)**b
I_ref = median of observed I in the training window (or last known if none).
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.optimize import minimize

sys.path.insert(0, str(Path(__file__).resolve().parent))
from run_ladder import DATA, OUT, EPS, step, naive_baselines

BREAK = 1991


def carry_forward(years, I_obs):
    """Causal last-observation-carried-forward. Reset memory at 1991 if last obs is pre-break and year>=break with no new obs yet."""
    out = np.full(len(years), np.nan)
    last = np.nan
    last_year = None
    obs_map = dict(zip(I_obs.year, I_obs.acoustic_kt))
    for i, y in enumerate(years):
        if y in obs_map:
            last = float(obs_map[y])
            last_year = y
        # do not carry a pre-1991 value into 1991+ if 1991 not yet observed
        if y >= BREAK and (last_year is None or last_year < BREAK):
            out[i] = np.nan
        else:
            out[i] = last
    return out


def fit(S, C, I):
    ok = np.isfinite(I[:-1]) & np.isfinite(S[:-1])
    if ok.sum() < 6:
        return None
    S0, C0, I0 = S[:-1][ok], C[:-1][ok], I[:-1][ok]
    dS = np.diff(S)[ok]
    Iref = float(np.median(I0[I0 > 0]))
    I0 = np.maximum(I0, 1.0)

    def obj(th):
        r, K, b = th
        if r <= 0 or K <= np.max(S0) * 0.4:
            return 1e12
        scale = (I0 / Iref) ** b
        pred = r * S0 * (1.0 - S0 / K) * scale - C0
        return float(np.mean((pred - dS) ** 2))

    res = minimize(
        obj,
        [0.25, max(np.max(S) * 1.3, 400.0), 0.4],
        method="L-BFGS-B",
        bounds=[(1e-3, 2.0), (np.max(S0) + 5.0, 8000.0), (0.0, 2.0)],
    )
    r, K, b = map(float, res.x)
    return {"r": r, "K": K, "b": b, "Iref": Iref, "ok": bool(res.success)}


def rolling(years, ssb, C, I, lrp, min_train, tag):
    n = len(years)
    rows = []
    for origin in range(min_train - 1, n - 1):
        if not np.isfinite(I[origin]):
            continue
        p = fit(ssb[: origin + 1], C[: origin + 1], I[: origin + 1])
        if p is None:
            continue
        I0 = max(I[origin], 1.0)
        scale = (I0 / p["Iref"]) ** p["b"]
        for h in (1, 5):
            if origin + h >= n:
                continue
            S = float(ssb[origin])
            for k in range(h):
                # persist last known I — do not use I[origin+1+k]
                g = p["r"] * S * (1.0 - S / p["K"]) * scale
                S = float(np.clip(S + g - C[origin + 1 + k], EPS, 1e6))
            y = float(ssb[origin + h])
            rows.append(
                {
                    "tag": tag,
                    "origin": int(years[origin]),
                    "horizon": int(h),
                    "model": "M_cap_index",
                    "obs": y,
                    "pred": S,
                    "I_used": I0,
                    "b": p["b"],
                    "sqerr": (S - y) ** 2,
                    "abserr": abs(S - y),
                    "log_sqerr": (np.log(max(S, EPS)) - np.log(y)) ** 2,
                }
            )
    df = pd.DataFrame(rows)
    if df.empty:
        return df, df
    summ = (
        df.groupby(["tag", "model", "horizon"], as_index=False)
        .agg(
            n=("sqerr", "size"),
            rmse=("sqerr", lambda s: float(np.sqrt(np.mean(s)))),
            mae=("abserr", "mean"),
            log_rmse=("log_sqerr", lambda s: float(np.sqrt(np.mean(s)))),
        )
    )
    return df, summ


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
    Iobs = pd.read_csv(DATA / "capelin_acoustic_observed.csv")
    frames, sums = [], []
    for tag, loader, min_tr in (("ncam2016", load_ncam, 8), ("xteNCAM", load_xte, 12)):
        years, ssb, C, lrp = loader()
        I = carry_forward(years, Iobs)
        df, sm = rolling(years, ssb, C, I, lrp, min_tr, tag)
        _, naive = naive_baselines(years, ssb, lrp)
        naive = naive.copy()
        naive.insert(0, "tag", tag)
        frames.append(df)
        sums.append(sm)
        sums.append(naive)
        print(f"\n=== {tag} observed-I carry-forward ===")
        if len(sm):
            print(sm.to_string(index=False, float_format=lambda x: f"{x:8.1f}"))
        print(naive.to_string(index=False, float_format=lambda x: f"{x:8.1f}"))
        print("n origins with I", int(np.isfinite(I).sum()), "/", len(I))

    pd.concat(frames, ignore_index=True).to_csv(OUT / "capelin_index_forecasts.csv", index=False)
    pd.concat(sums, ignore_index=True).to_csv(OUT / "capelin_index_summary.csv", index=False)


if __name__ == "__main__":
    main()

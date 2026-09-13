#!/usr/bin/env python3
"""Phase C campaign 1 — reproduce the SPECIFICATION_v4 operating characteristics (D1-D5 x 2 sigma).

Adapted from tools/sim_retention_power.py (design unchanged; only paths, output location,
seed documentation and provenance recording differ). The estimator/map/scorer are IMPORTED
from wave_e_cod/src/run_ladder.py — never reimplemented.

Design (frozen sheet, unchanged): DGPs D1-D5, sigma {11.8, 33.8} kt, T=33,
H1/H2/H3 + 5% band. Reps: D1/D5 at 200 (registered), D2/D3/D4 at 100 (Phase C scaling
decision — recorded in PHASE_C_RESULTS.md; binomial CIs reported honestly).

Seeds: same scheme as the original (abs(hash((dgp, sigma, rep))) % 2**31) under
PYTHONHASHSEED=0, so this run is reproducible; the published/zips runs used unknown
hash seeds, which is exactly the D3 explanation (rates agree up to seed noise).

Output: phase_c/results/sim_retention_power_20260913.csv + _provenance.json + summary table.
"""
import os, sys, json, hashlib, time, datetime
import numpy as np
import pandas as pd

WS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(WS, "wave_e_cod", "src"))
import run_ladder as rl  # noqa: E402

OUT = os.path.join(WS, "phase_c", "results", "sim_retention_power_20260913.csv")
T = 33
SIGMAS = (11.8, 33.8)
TIE = 0.05
HORIZONS = (1, 5)
MODULES = ["M1_autonomous_Schaefer", "M1b_autonomous_Allee",
           "M2_stockflow_regimeC", "M3_AR_residual", "M4_delayed_info"]
COMPARATOR = {
    "M1_autonomous_Schaefer": None,
    "M1b_autonomous_Allee": "M1_autonomous_Schaefer",
    "M2_stockflow_regimeC": "M1_autonomous_Schaefer",
    "M3_AR_residual": "M2_stockflow_regimeC",
    "M4_delayed_info": "M3_AR_residual",
}
DGPS = {
    "D1_M1_collapse":  dict(truth="M1_autonomous_Schaefer", r=1.935, K=1032.7, s=None, catch="const240", S0=900.0),
    "D2_M1_recovery":  dict(truth="M1_autonomous_Schaefer", r=0.458, K=500.0, s=None, catch="const5", S0=30.0),
    "D3_M2_stockflow": dict(truth="M2_stockflow_regimeC", r=1.935, K=1032.7, s=None, catch="regime", S0=900.0),
    "D4_M1b_depens":   dict(truth="M1b_autonomous_Allee", r=0.458, K=500.0, s=15.0, catch="const5", S0=30.0),
    "D5_persist_null": dict(truth=None, r=None, K=None, s=None, catch="zero", S0=300.0),
}
REPS = {"D1_M1_collapse": 200, "D5_persist_null": 200}  # others default 100


def catch_path(kind, years):
    if kind == "const240": return np.full(len(years), 240.0)
    if kind == "const5":   return np.full(len(years), 5.0)
    if kind == "zero":     return np.zeros(len(years))
    if kind == "regime":
        return np.array([240.0 if y <= 1991 else (120.0 if y == 1992 else 5.0) for y in years])
    raise ValueError(kind)


def simulate(dgp, sigma, rng, years):
    C = catch_path(dgp["catch"], years)
    S = np.zeros(len(years)); S[0] = dgp["S0"]
    for t in range(len(years) - 1):
        eps = rng.normal(0.0, sigma)
        if dgp["truth"] is None:
            S[t + 1] = max(S[t] + eps, rl.EPS)
        else:
            S[t + 1] = rl.step(S[t], C[t], dgp["r"], dgp["K"], dgp["s"], eps)
    return S, C


def persistence_rmse(S, origins, h):
    e = [(S[o + h] - S[o]) ** 2 for o in origins if o + h < len(S)]
    return float(np.sqrt(np.mean(e))) if e else np.nan


def retained(scores, persist, module):
    comp = COMPARATOR[module]
    for h in HORIZONS:
        m = scores[module][h]; p = persist[h]
        if not np.isfinite(m) or not np.isfinite(p):
            return False
        if not (m < p * (1.0 - TIE)):
            return False
        if comp is not None:
            c = scores[comp][h]
            if not np.isfinite(c) or not (m < c * (1.0 - TIE)):
                return False
    return True


def run_cell(dname, dgp, sigma, reps):
    t0 = time.time()
    years = np.arange(1983, 1983 + T)
    rows = []
    for rep in range(reps):
        seed = abs(hash((dname, sigma, rep))) % (2 ** 31)
        rng = np.random.default_rng(seed)
        S, C = simulate(dgp, sigma, rng, years)
        try:
            _, summ = rl.run_rolling(years, S, C, 884.6, min_train=8)
        except Exception:
            continue
        scores, persist = {}, {}
        for h in HORIZONS:
            sub = summ[summ.horizon == h]
            for m in MODULES:
                r_ = sub[sub.model == m]
                scores.setdefault(m, {})[h] = float(r_.rmse.iloc[0]) if len(r_) else np.nan
            persist[h] = persistence_rmse(S, sorted(range(7, len(years) - 1)), h)
        for m in MODULES:
            rows.append(dict(dgp=dname, truth=dgp["truth"], sigma=sigma, rep=rep, module=m,
                             rmse_h1=scores[m][1], rmse_h5=scores[m][5],
                             persist_h1=persist[1], persist_h5=persist[5],
                             retained=retained(scores, persist, m)))
    dt = time.time() - t0
    return rows, dt


def main():
    t_start = time.time()
    all_rows, times = [], {}
    for dname, dgp in DGPS.items():
        for sigma in SIGMAS:
            reps = REPS.get(dname, 100)
            rows, dt = run_cell(dname, dgp, sigma, reps)
            all_rows += rows
            times[f"{dname}_s{sigma}"] = dict(reps=len({r['rep'] for r in rows}), wall_s=round(dt, 1))
            print(f"  done {dname} sigma={sigma} n={len({r['rep'] for r in rows})} {dt:.0f}s", flush=True)
    df = pd.DataFrame(all_rows)
    df.to_csv(OUT, index=False)
    prov = {
        "campaign": "sim_retention_power", "run": "20260913", "pyhashseed": os.environ.get("PYTHONHASHSEED"),
        "started_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "wall_s_total": round(time.time() - t_start, 1), "cells": times,
        "sha256": {
            "run_ladder.py": hashlib.sha256(open(os.path.join(WS, "wave_e_cod", "src", "run_ladder.py"), "rb").read()).hexdigest(),
            "campaign_power.py": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
        },
        "versions": dict(numpy=np.__version__, pandas=pd.__version__),
    }
    with open(OUT.replace(".csv", "_provenance.json"), "w") as f:
        json.dump(prov, f, indent=2)
    print(f"\nwrote {OUT} ({len(df)} rows)\n")
    print("=== retention rates by DGP and sigma (this run) ===")
    for (d, s), g in df.groupby(["dgp", "sigma"]):
        truth = g.truth.iloc[0]
        any_ret = g.groupby("rep").retained.any().mean()
        line = f"  {d:18} sigma={s:5}  any-module retention {any_ret:.3f}"
        if truth:
            line += f" | TRUE-module power {g[g.module == truth].retained.mean():.3f}"
        else:
            line += f" | specificity {1 - any_ret:.3f}"
        print(line)


if __name__ == "__main__":
    main()

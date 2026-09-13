#!/usr/bin/env python3
"""Phase C campaign 2 — Amendment-1 cells: D6/D7 misspecified truth + T=71 extension (D1, D5).

Adapted from tools/sim_misspecified.py (design unchanged; paths/output/provenance differ).
This run also stores RMSE columns (rmse_h1/h5, persist_h1/h5) so the AD2 registered quantity
— the realised predictive gain of retained modules in D6/D7 replicates — can be computed.

Scaling decision (Phase C, recorded): D6/D7 at 100 reps, T=71 at 50 reps (full 200/200 design
was benchmarked by the author at ~10 h and is registered as a longer campaign).
PYTHONHASHSEED=0 for reproducibility.

Output: phase_c/results/sim_misspecified_20260913.csv + _provenance.json.
"""
import os, sys, json, hashlib, time, datetime
import numpy as np
import pandas as pd

WS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(WS, "wave_e_cod", "src"))
import run_ladder as rl  # noqa: E402

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import campaign_power as cp  # noqa: E402  (MODULES, COMPARATOR, TIE, HORIZONS, persistence_rmse, retained)

OUT = os.path.join(WS, "phase_c", "results", "sim_misspecified_20260913.csv")
# Phase C scaling (trimmed after timing measurement): D6/D7 @30, T71 @10 reps.
# Measured contended per-pass costs: D6 ~19-29 s, D7 ~17-21 s, D1_T71 ~95-99 s,
# D5_T71 ~13-25 s (the author's published 45.6 s/pass T=71 benchmark is optimistic
# for these series). First attempt (D6/D7 @100, T71 @50) was killed after 2.5 h with
# D6+D7 complete but unwritten; rates below carry honest binomial CIs.
REPS_D67 = 30
REPS_T71 = 10


def gen_D6(rng, T, sigma):
    S = np.zeros(T); S[0] = 900.0; K = 1032.7; C = np.zeros(T)
    for t in range(T - 1):
        r = 1.935 * np.exp(-0.05 * t) + 0.35
        C[t] = 0.55 * r * K / 4
        S[t + 1] = rl.step(S[t], C[t], r, K, None, rng.normal(0, sigma))
    C[-1] = C[-2]
    return S, C


def gen_D7(rng, T, sigma):
    X = np.zeros(T); X[0] = 900.0; r, K, Cc = 0.9, 1032.7, 180.0
    for t in range(T - 1):
        X[t + 1] = rl.step(X[t], Cc, r, K, None, 0.0)
    S = np.maximum(X + rng.normal(0, sigma, T), rl.EPS)
    return S, np.full(T, Cc)


def gen_D1(rng, T, sigma):
    S = np.zeros(T); S[0] = 900.0; C = np.full(T, 240.0)
    for t in range(T - 1):
        S[t + 1] = rl.step(S[t], C[t], 1.935, 1032.7, None, rng.normal(0, sigma))
    return S, C


def gen_D5(rng, T, sigma):
    S = np.zeros(T); S[0] = 300.0
    for t in range(T - 1):
        S[t + 1] = max(S[t] + rng.normal(0, sigma), rl.EPS)
    return S, np.zeros(T)


CELLS = [("D6_timevarying_r", gen_D6, 33, None, REPS_D67),
         ("D7_obs_error", gen_D7, 33, None, REPS_D67),
         ("D1_T71", gen_D1, 71, "M1_autonomous_Schaefer", REPS_T71),
         ("D5_T71", gen_D5, 71, None, REPS_T71)]


def run_cell(name, gen, T, truth, reps):
    t0 = time.time()
    rows = []
    for sigma in (11.8, 33.8):
        years = np.arange(1954, 1954 + T) if T == 71 else np.arange(1983, 1983 + T)
        for rep in range(reps):
            rng = np.random.default_rng(abs(hash((name, sigma, rep))) % (2 ** 31))
            S, C = gen(rng, T, sigma)
            try:
                _, summ = rl.run_rolling(years, S, C, 884.6, min_train=8)
            except Exception:
                continue
            scores, persist = {}, {}
            for h in cp.HORIZONS:
                sub = summ[summ.horizon == h]
                for m in cp.MODULES:
                    r_ = sub[sub.model == m]
                    scores.setdefault(m, {})[h] = float(r_.rmse.iloc[0]) if len(r_) else np.nan
                persist[h] = cp.persistence_rmse(S, sorted(range(7, len(years) - 1)), h)
            for m in cp.MODULES:
                rows.append(dict(cell=name, truth=truth, T=T, sigma=sigma, rep=rep, module=m,
                                 rmse_h1=scores[m][1], rmse_h5=scores[m][5],
                                 persist_h1=persist[1], persist_h5=persist[5],
                                 retained=cp.retained(scores, persist, m)))
    dt = time.time() - t0
    return rows, dt


def main():
    t_start = time.time()
    written_cols = False
    for name, gen, T, truth, reps in CELLS:
        rows, dt = run_cell(name, gen, T, truth, reps)
        part = pd.DataFrame(rows)
        # incremental flush: no progress is ever lost to a kill again
        part.to_csv(OUT, index=False, mode="w" if not written_cols else "a",
                    header=not written_cols)
        written_cols = True
        print(f"  done {name} T={T} {dt:.0f}s -> {len(part)} rows appended", flush=True)
    df = pd.read_csv(OUT)
    prov = {
        "campaign": "sim_misspecified", "run": "20260913",
        "pyhashseed": os.environ.get("PYTHONHASHSEED"),
        "started_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "wall_s_total": round(time.time() - t_start, 1), "cells": times,
        "reps": {"D6/D7": REPS_D67, "T71": REPS_T71},
        "sha256": {
            "run_ladder.py": hashlib.sha256(open(os.path.join(WS, "wave_e_cod", "src", "run_ladder.py"), "rb").read()).hexdigest(),
            "campaign_misspecified.py": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
        },
        "versions": dict(numpy=np.__version__, pandas=pd.__version__),
    }
    with open(OUT.replace(".csv", "_provenance.json"), "w") as f:
        json.dump(prov, f, indent=2)
    print(f"\nwrote {OUT} ({len(df)} rows)\n")
    print("=== false-retention rates (this run) ===")
    for (c, s), g in df.groupby(["cell", "sigma"]):
        any_ret = g.groupby("rep").retained.any().mean()
        tr = g.truth.iloc[0]
        line = f"  {c:14} sigma={s:5}  any-module retention {any_ret:.3f}"
        if isinstance(tr, str):
            line += f" | TRUE-module power {g[g.module == tr].retained.mean():.3f}"
        print(line)


if __name__ == "__main__":
    main()

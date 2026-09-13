#!/usr/bin/env python3
"""Phase C campaign 6 — SNR (sigma) sweep: power curves beyond the registered pair {11.8, 33.8}.

New sigma points that the frozen design never ran:
  D1 (collapse): sigma 5, 20, 45  (11.8/33.8 already run at 200 reps in campaign_power)
  D3 (stock-flow), D4 (depensation): sigma 5  (the "identification limit" claim predicts
  power stays near zero even at low noise; 11.8/33.8 already run at 100 reps)

Same estimator/map/scorer (imported), same seeds, same 5%-band rule.

Output: phase_c/results/sim_snr_sweep_20260913.csv + _provenance.json.
"""
import os, sys, json, hashlib, time, datetime
import numpy as np
import pandas as pd

WS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(WS, "wave_e_cod", "src"))
import run_ladder as rl  # noqa: E402

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import campaign_power as cp  # noqa: E402

OUT = os.path.join(WS, "phase_c", "results", "sim_snr_sweep_20260913.csv")
# Phase C scaling: 25 reps/cell (disclosed; CI halfwidth ~0.20)
REPS = 25
SWEEP = [("D1_M1_collapse", (5.0, 20.0, 45.0)),
         ("D3_M2_stockflow", (5.0,)),
         ("D4_M1b_depens", (5.0,))]


def main():
    t_start = time.time()
    years = np.arange(1983, 1983 + 33)
    rows = []
    times = {}
    written = False
    for dname, sigmas in SWEEP:
        dgp = cp.DGPS[dname]
        for sigma in sigmas:
            t0 = time.time()
            for rep in range(REPS):
                seed = abs(hash((dname, sigma, rep))) % (2 ** 31)
                rng = np.random.default_rng(seed)
                S, C = cp.simulate(dgp, sigma, rng, years)
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
                    rows.append(dict(dgp=dname, truth=dgp["truth"], sigma=sigma, rep=rep,
                                     module=m, rmse_h1=scores[m][1], rmse_h5=scores[m][5],
                                     persist_h1=persist[1], persist_h5=persist[5],
                                     retained=cp.retained(scores, persist, m)))
            times[f"{dname}_s{sigma}"] = round(time.time() - t0, 1)
            print(f"  done snr {dname} sigma={sigma} {time.time() - t0:.0f}s", flush=True)
            part = pd.DataFrame(rows)
            part.to_csv(OUT, index=False, mode="w" if not written else "a",
                        header=not written)
            written = True
            rows = []
    df = pd.read_csv(OUT)
    prov = {
        "campaign": "sim_snr_sweep", "run": "20260913", "reps": REPS,
        "pyhashseed": os.environ.get("PYTHONHASHSEED"),
        "started_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "wall_s_total": round(time.time() - t_start, 1), "cells": times,
        "sha256": {
            "run_ladder.py": hashlib.sha256(open(os.path.join(WS, "wave_e_cod", "src", "run_ladder.py"), "rb").read()).hexdigest(),
            "campaign_snr.py": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
        },
        "versions": dict(numpy=np.__version__, pandas=pd.__version__),
    }
    with open(OUT.replace(".csv", "_provenance.json"), "w") as f:
        json.dump(prov, f, indent=2)
    print(f"\nwrote {OUT} ({len(df)} rows)")
    print("=== power by sigma (sweep cells only) ===")
    for (d, s), g in df.groupby(["dgp", "sigma"]):
        truth = g.truth.iloc[0]
        pw = g[g.module == truth].retained.mean()
        any_ret = g.groupby("rep").retained.any().mean()
        print(f"  {d:18} sigma={s:5} true-module power {pw:.3f} | any {any_ret:.3f}")


if __name__ == "__main__":
    main()

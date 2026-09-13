#!/usr/bin/env python3
"""Phase C campaign 5 — per-origin squared errors for D1-D4 (both sigma).

Feeds: the uncertainty-aware gate + hybrid (H2 AND uncertainty) rows, the
MCS/encompassing analysis, and the training-window profile (pseudo-OOS inner loop,
register item "pre-check candidates (4.5)").

One row per (dgp, sigma, rep, origin, horizon, model) with sqerr. Retention flags for
the 5% band (H2/H3 gates, as in campaign_power) are also stored per replicate for
consistency.

Seeds identical to campaign_power (abs(hash((dname, sigma, rep))) % 2**31,
PYTHONHASHSEED=0) so the replicate series are the SAME as the power campaign's
reps 0..39, and all analyses can be joined by seed.

Output: phase_c/results/sim_origins_20260913.csv + _provenance.json.
"""
import os, sys, json, hashlib, time, datetime
import numpy as np
import pandas as pd

WS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(WS, "wave_e_cod", "src"))
import run_ladder as rl  # noqa: E402

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import campaign_power as cp  # noqa: E402

OUT = os.path.join(WS, "phase_c", "results", "sim_origins_20260913.csv")
# Phase C scaling: 25 reps/cell (binomial CI halfwidth ~0.20 for rates near 0.5,
# ~0.10 near 0.1/0.9); full 200-rep design registered for larger hardware.
REPS = 25
CELLS = ["D1_M1_collapse", "D2_M1_recovery", "D3_M2_stockflow", "D4_M1b_depens",
         "D5_persist_null"]


def main():
    t_start = time.time()
    rows = []
    times = {}
    written = False
    for dname in CELLS:
        dgp = cp.DGPS[dname]
        for sigma in (11.8, 33.8):
            t0 = time.time()
            years = np.arange(1983, 1983 + 33)
            for rep in range(REPS):
                seed = abs(hash((dname, sigma, rep))) % (2 ** 31)
                rng = np.random.default_rng(seed)
                S, C = cp.simulate(dgp, sigma, rng, years)
                df, summ = rl.run_rolling(years, S, C, 884.6, min_train=8)
                # 5%-band retention per module (same definition as campaign_power)
                scores, persist = {}, {}
                for h in cp.HORIZONS:
                    sub = summ[summ.horizon == h]
                    for m in cp.MODULES:
                        r_ = sub[sub.model == m]
                        scores.setdefault(m, {})[h] = float(r_.rmse.iloc[0]) if len(r_) else np.nan
                    persist[h] = cp.persistence_rmse(S, sorted(range(7, len(years) - 1)), h)
                ret = {m: cp.retained(scores, persist, m) for m in cp.MODULES}
                for _, r in df.iterrows():
                    rows.append(dict(dgp=dname, truth=dgp["truth"], sigma=sigma, rep=rep,
                                     origin=int(r.origin), horizon=int(r.horizon),
                                     model=r.model, obs=float(r.obs), pred=float(r.pred),
                                     sqerr=float(r.sqerr),
                                     band_retained=bool(ret.get(r.model, False))))
                # persistence rows (same origins/horizons as the ladder grid)
                for o in range(7, len(years) - 1):
                    for h in cp.HORIZONS:
                        if o + h >= len(years):
                            continue
                        sq = (S[o + h] - S[o]) ** 2
                        rows.append(dict(dgp=dname, truth=dgp["truth"], sigma=sigma, rep=rep,
                                         origin=int(years[o]), horizon=int(h),
                                         model="naive_persist", obs=float(S[o + h]),
                                         pred=float(S[o]), sqerr=float(sq),
                                         band_retained=False))
            times[f"{dname}_s{sigma}"] = round(time.time() - t0, 1)
            print(f"  done origins {dname} sigma={sigma} {time.time() - t0:.0f}s", flush=True)
            part = pd.DataFrame(rows)
            part.to_csv(OUT, index=False, mode="w" if not written else "a",
                        header=not written)
            written = True
            rows = []
    out_df = pd.read_csv(OUT)
    prov = {
        "campaign": "sim_origins", "run": "20260913", "reps": REPS,
        "pyhashseed": os.environ.get("PYTHONHASHSEED"),
        "started_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "wall_s_total": round(time.time() - t_start, 1), "cells": times,
        "sha256": {
            "run_ladder.py": hashlib.sha256(open(os.path.join(WS, "wave_e_cod", "src", "run_ladder.py"), "rb").read()).hexdigest(),
            "campaign_origins.py": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
        },
        "versions": dict(numpy=np.__version__, pandas=pd.__version__),
    }
    with open(OUT.replace(".csv", "_provenance.json"), "w") as f:
        json.dump(prov, f, indent=2)
    print(f"\nwrote {OUT} ({len(out_df)} rows)")


if __name__ == "__main__":
    main()

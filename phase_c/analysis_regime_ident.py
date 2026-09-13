#!/usr/bin/env python3
"""Phase C analysis 2 — per-regime decomposition + identification-limit pin + training-window profile.

Zero extra ladder cost: the replicate series are re-generated from the SAME seeds as
campaign_power (abs(hash((dname, sigma, rep))) % 2**31) and joined to the stored
per-replicate RMSE/retention rows.

  1. Per-regime decomposition: for each DGP, a realized-regime statistic per replicate
     (D1/D3: collapse depth S_end/S0; D2/D4: recovery rise S_end - S0; D5: drift sign)
     split at the median -> power within each regime half.
  2. Identification-limit pin: rate at which the generating module has the lowest
     one-step RMSE (h=1), and the share of H2-passers removed by the H1 comparator gate
     — versus the published 62.7%/64.5%/25.8%/3.8% and 69%/94%.
  3. Training-window profile: mean sqerr by origin year for the true module vs
     persistence (from sim_origins_20260913.csv) — curvature check (register 4.5).

Outputs: phase_c/results/per_regime_decomposition_20260913.json
         phase_c/results/identification_limit_20260913.json
         phase_c/results/training_window_profile_20260913.csv
"""
import os, sys, json, datetime
import numpy as np
import pandas as pd

WS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
R = os.path.join(WS, "phase_c", "results")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import campaign_power as cp  # noqa: E402

TRUTH = {"D1_M1_collapse": "M1_autonomous_Schaefer",
         "D2_M1_recovery": "M1_autonomous_Schaefer",
         "D3_M2_stockflow": "M2_stockflow_regimeC",
         "D4_M1b_depens": "M1b_autonomous_Allee",
         "D5_persist_null": None}
REALIZED = {"D1_M1_collapse": "collapse_depth", "D3_M2_stockflow": "collapse_depth",
            "D2_M1_recovery": "rise", "D4_M1b_depens": "rise",
            "D5_persist_null": "drift_sign"}


def realized_stat(dname, S):
    kind = REALIZED[dname]
    if kind == "collapse_depth":
        return float(S[-1] / S[0])
    if kind == "rise":
        return float(S[-1] - S[0])
    return float(1.0 if S[-1] >= S[0] else -1.0)


def main():
    power = pd.read_csv(os.path.join(R, "sim_retention_power_20260913.csv"))

    # ---- 1. per-regime decomposition ----
    regime = {}
    for dname in REALIZED:
        dgp = cp.DGPS[dname]
        for sigma in (11.8, 33.8):
            stats, rets = [], []
            for rep in sorted(power[(power.dgp == dname) & (power.sigma == sigma)].rep.unique()):
                seed = abs(hash((dname, sigma, rep))) % (2 ** 31)
                rng = np.random.default_rng(seed)
                S, C = cp.simulate(dgp, sigma, rng, np.arange(1983, 1983 + 33))
                stats.append(realized_stat(dname, S))
                sub = power[(power.dgp == dname) & (power.sigma == sigma) & (power.rep == rep)]
                if TRUTH[dname]:
                    rets.append(bool(sub[sub.module == TRUTH[dname]].retained.iloc[0]))
                else:
                    rets.append(not bool(sub.retained.any()))
            arr = np.array(stats); med = np.median(arr)
            lo = arr <= med; hi = ~lo
            regime[f"{dname}_s{sigma}"] = {
                "median_split": float(med),
                "n_lo": int(lo.sum()), "rate_lo": float(np.mean(np.array(rets)[lo])),
                "n_hi": int(hi.sum()), "rate_hi": float(np.mean(np.array(rets)[hi])),
                "statistic": REALIZED[dname],
            }
    with open(os.path.join(R, "per_regime_decomposition_20260913.json"), "w") as f:
        json.dump({"run": "20260913",
                   "written_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                   "regimes": regime}, f, indent=2)
    print("=== per-regime decomposition (true-module power / specificity by regime half) ===")
    print(json.dumps(regime, indent=2))

    # ---- 2. identification-limit pin ----
    ident = {}
    for dname in ["D1_M1_collapse", "D2_M1_recovery", "D3_M2_stockflow", "D4_M1b_depens"]:
        truth = TRUTH[dname]
        for sigma in (11.8, 33.8):
            sub = power[(power.dgp == dname) & (power.sigma == sigma)]
            best = sub.loc[sub.groupby("rep").rmse_h1.idxmin()].module
            rate = float((best == truth).mean())
            # comparator-gate removal share among H2 passers (true module only)
            h2 = sub[(sub.module == truth) & (sub.rmse_h1 < sub.persist_h1 * 0.95) &
                     (sub.rmse_h5 < sub.persist_h5 * 0.95)]
            removed = (h2.rmse_h1 >= sub[(sub.module == "M1_autonomous_Schaefer") & sub.rep.isin(h2.rep)].set_index("rep").loc[h2.rep].rmse_h1.values * 0.95) if truth != "M1_autonomous_Schaefer" else np.zeros(len(h2), dtype=bool)
            ident[f"{dname}_s{sigma}"] = {
                "truth_best_h1_rate": round(rate, 4),
                "n_reps": int(sub.rep.nunique()),
                "h2_passer_count": int(len(h2)),
                "h1_gate_removal_share": round(float(removed.mean()), 3) if len(h2) else None,
            }
    with open(os.path.join(R, "identification_limit_20260913.json"), "w") as f:
        json.dump({"run": "20260913",
                   "published_reference": "generating module lowest one-step error in 62.7%/64.5% autonomous, 25.8% depensation, 3.8% stock-flow; comparator gate removes 69% of H2-passers in D3 and 94% in D4",
                   "written_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                   "cells": ident}, f, indent=2)
    print("\n=== identification-limit pin (published: 62.7/64.5 | 25.8 | 3.8; gate 69%/94%) ===")
    print(json.dumps(ident, indent=2))

    # ---- 3. training-window profile ----
    orig_path = os.path.join(R, "sim_origins_20260913.csv")
    if not os.path.exists(orig_path):
        print("\n=== training-window profile: sim_origins CSV not ready yet — skipped ===")
        return
    orig = pd.read_csv(orig_path)
    prof = []
    for dname in ["D1_M1_collapse", "D3_M2_stockflow"]:
        for sigma in (11.8, 33.8):
            g = orig[(orig.dgp == dname) & (orig.sigma == sigma) & (orig.horizon == 1)]
            for o, gg in g.groupby("origin"):
                t = gg[gg.model == TRUTH[dname]].sqerr.mean()
                p = gg[gg.model == "naive_persist"].sqerr.mean()
                prof.append(dict(dgp=dname, sigma=sigma, origin=int(o),
                                 truth_mean_sqerr=float(t), persist_mean_sqerr=float(p)))
    pdf = pd.DataFrame(prof)
    pdf.to_csv(os.path.join(R, "training_window_profile_20260913.csv"), index=False)
    print("\n=== training-window profile (mean sqerr by origin year, h=1) — first/last rows ===")
    print(pdf.groupby(["dgp", "sigma"]).head(3).to_string(index=False))


if __name__ == "__main__":
    main()

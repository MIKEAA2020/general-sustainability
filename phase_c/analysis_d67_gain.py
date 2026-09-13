#!/usr/bin/env python3
"""Phase C analysis 3 — realised predictive gain of retained modules in D6/D7
(the AD2-registered quantity: when the rule falsely retains under misspecified truth,
does the retained module at least beat persistence in prediction?).

Consumes phase_c/results/sim_misspecified_20260913.csv (rmse/persist columns stored
by campaign_misspecified). For every replicate where at least one module is retained,
record the best retained module's margin vs persistence at h=1 and h=5.

Output: phase_c/results/d67_realised_gain_20260913.json
"""
import os, json, datetime
import numpy as np
import pandas as pd

WS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
R = os.path.join(WS, "phase_c", "results")
SRC = os.path.join(R, "sim_misspecified_20260913.csv")


def main():
    df = pd.read_csv(SRC)
    out = {}
    for (cell, sigma), g in df.groupby(["cell", "sigma"]):
        if cell.startswith("D1_") or cell.startswith("D5_"):
            continue  # T=71 cells are power/specificity rows, not misspecified-truth
        reps = []
        for rep, gg in g.groupby("rep"):
            ret = gg[gg.retained]
            rec = {"rep": int(rep), "n_retained": int(len(ret))}
            if len(ret):
                best = ret.loc[ret.rmse_h1.idxmin()]
                rec["best_retained_module"] = best.module
                rec["gain_h1_vs_persist"] = round(float(best.persist_h1 - best.rmse_h1), 2)
                rec["gain_h5_vs_persist"] = round(float(best.persist_h5 - best.rmse_h5), 2)
                rec["rel_gain_h1"] = round(float((best.persist_h1 - best.rmse_h1) / best.persist_h1), 4)
            reps.append(rec)
        gains_h1 = [r["gain_h1_vs_persist"] for r in reps if "gain_h1_vs_persist" in r]
        gains_h5 = [r["gain_h5_vs_persist"] for r in reps if "gain_h5_vs_persist" in r]
        out[f"{cell}_s{sigma}"] = {
            "n_reps": len(reps),
            "reps_with_retention": len(gains_h1),
            "mean_gain_h1_vs_persist": round(float(np.mean(gains_h1)), 2) if gains_h1 else None,
            "mean_gain_h5_vs_persist": round(float(np.mean(gains_h5)), 2) if gains_h5 else None,
            "share_gain_positive_h1": round(float(np.mean([x > 0 for x in gains_h1])), 3) if gains_h1 else None,
        }
    payload = {"run": "20260913",
               "written_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
               "note": "gain = persist_rmse - retained_rmse, per replicate, best retained module",
               "cells": out}
    with open(os.path.join(R, "d67_realised_gain_20260913.json"), "w") as f:
        json.dump(payload, f, indent=2)
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()

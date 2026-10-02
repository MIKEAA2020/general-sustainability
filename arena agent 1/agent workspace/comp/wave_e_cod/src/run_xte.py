#!/usr/bin/env python3
"""Wave E ladder on Ω_xte alone. Do not pool with NCAM 2016."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from run_ladder import (  # noqa: E402
    OUT,
    DATA,
    SPECS,
    catch_for_model,
    fit_params,
    forecast_path,
    scores,
    surplus,
    naive_baselines,
    run_fixed_windows,
    run_rolling,
)

LRP_XTE = 276.0  # Regular et al. 2025: 40% BMSY [N]


def load_xte():
    ssb = pd.read_csv(DATA / "xtencam_table17_ssb.csv")
    cat = pd.read_csv(DATA / "dfo_2025_table1_landings.csv")
    df = ssb.merge(cat[["year", "catch_kt"]], on="year", how="left")
    # 2024 has SSB but no Table 1 catch yet — persist 2023
    df["catch_kt"] = df["catch_kt"].ffill()
    years = df["year"].to_numpy()
    return years, df["ssb_kt"].to_numpy(float), df["catch_kt"].to_numpy(float)


def overlap_audit():
    ncam = pd.read_csv(DATA / "ncam_2016_table_a2.csv")
    xte = pd.read_csv(DATA / "xtencam_table17_ssb.csv")
    m = ncam.merge(xte, on="year", suffixes=("_ncam", "_xte"))
    m["ssb_diff"] = m["ssb_kt_xte"] - m["ssb_kt_ncam"]
    m["ssb_rel"] = m["ssb_diff"] / m["ssb_kt_ncam"]
    m.to_csv(OUT / "ncam_vs_xtencam_overlap.csv", index=False)
    return m


def main():
    years, ssb, C = load_xte()
    assert years.min() == 1954 and years.max() == 2024
    ov = overlap_audit()

    # Override fixed windows for the long series
    import run_ladder as rl

    def run_fixed_xte(years, ssb, C, lrp):
        windows = {
            "pre_to_collapse": (1954, 1989, 1990, 1995),
            "recovery_stall": (1995, 2012, 2013, 2024),
        }
        rows, paths = [], {}
        for wname, (a0, a1, b0, b1) in windows.items():
            tr = (years >= a0) & (years <= a1)
            te = (years >= b0) & (years <= b1)
            i_tr, i_te = np.where(tr)[0], np.where(te)[0]
            for spec in SPECS:
                C_all = catch_for_model(years, C, tr, spec.use_regime_C)
                p = fit_params(ssb[tr], C_all[tr], allee=spec.allee)
                start_idx = max(i_tr[0], i_tr[-1] - spec.delay)
                S0 = ssb[start_idx]
                C_path = C_all[start_idx + 1 : i_te[-1] + 1]
                last_resid = 0.0
                if spec.use_ar and len(i_tr) > 2:
                    fitted = np.array(
                        [
                            surplus(ssb[j], p["r"], p["K"], p["s_allee"]) - C_all[j]
                            for j in i_tr[:-1]
                        ]
                    )
                    last_resid = (np.diff(ssb[i_tr]) - fitted)[-1]
                yhat_full = forecast_path(S0, C_path, p, spec.use_ar, last_resid)
                offset = i_te[0] - (start_idx + 1)
                yhat = yhat_full[offset : offset + len(i_te)]
                sc = scores(ssb[te], yhat, lrp)
                rows.append(
                    {
                        "omega": "xteNCAM",
                        "window": wname,
                        "model": spec.name,
                        "train": f"{a0}-{a1}",
                        "test": f"{b0}-{b1}",
                        **sc,
                        **{k: p[k] for k in ("r", "K", "s_allee", "phi", "ok")},
                    }
                )
                paths[f"{wname}:{spec.name}"] = {
                    "year": years[te].tolist(),
                    "obs": ssb[te].tolist(),
                    "pred": [float(x) for x in yhat],
                }
        return pd.DataFrame(rows), paths

    win, paths = run_fixed_xte(years, ssb, C, LRP_XTE)
    roll_df, roll_sum = run_rolling(years, ssb, C, LRP_XTE, min_train=12)
    naive_df, naive_sum = naive_baselines(years, ssb, LRP_XTE)
    roll_all = pd.concat([roll_sum, naive_sum], ignore_index=True)

    win.to_csv(OUT / "xte_fixed_window_scores.csv", index=False)
    roll_df.to_csv(OUT / "xte_rolling_forecasts.csv", index=False)
    roll_all.to_csv(OUT / "xte_rolling_summary.csv", index=False)
    with open(OUT / "xte_paths.json", "w") as f:
        json.dump(paths, f, indent=2)
    meta = {
        "omega": "xteNCAM Regular et al. 2025 Table 17",
        "lrp_kt": LRP_XTE,
        "n": int(len(years)),
        "year_min": int(years.min()),
        "year_max": int(years.max()),
        "ssb_2024": float(ssb[years == 2024][0]),
        "ssb_2024_over_lrp": float(ssb[years == 2024][0] / LRP_XTE),
        "overlap_n": int(len(ov)),
        "overlap_rmse": float(np.sqrt(np.mean(ov["ssb_diff"] ** 2))),
        "overlap_2015_ncam": float(ov.loc[ov.year == 2015, "ssb_kt_ncam"].iloc[0]),
        "overlap_2015_xte": float(ov.loc[ov.year == 2015, "ssb_kt_xte"].iloc[0]),
        "pooled": False,
    }
    with open(OUT / "xte_meta.json", "w") as f:
        json.dump(meta, f, indent=2)

    print("Ω_xte LRP", LRP_XTE, "2024 SSB/LRP", round(meta["ssb_2024_over_lrp"], 3))
    print("overlap n", meta["overlap_n"], "RMSE vs NCAM2016", round(meta["overlap_rmse"], 1))
    print("2015 NCAM", meta["overlap_2015_ncam"], "xte", meta["overlap_2015_xte"])
    print("\n=== Fixed windows ===")
    print(win[["window", "model", "rmse", "mae", "log_rmse"]].to_string(index=False, float_format=lambda x: f"{x:8.1f}"))
    print("\n=== Rolling ===")
    print(roll_all.to_string(index=False, float_format=lambda x: f"{x:8.1f}"))


if __name__ == "__main__":
    main()

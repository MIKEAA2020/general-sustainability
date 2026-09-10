#!/usr/bin/env python3
"""
EXPLORATORY controls and strengthening for the second-pool record.

Implements the reviewer's missing pieces:
  C1  J-17 matched-window control (1941-2023)              [review 4.3]
  C2  J-17 mismatched-driver control (D5 applied to J-17)   [review 4.2]
  C3  J-27 driver-definition ladder (B1,B2,B1+2,B1-4,Total) [review 3.3]
  C4  Driver-component decomposition (R-only / P-only)      [review 3.2]
  C5  Clip-bound sensitivity on J-27                        [review 3.4]
  C6  Kernel status under ALL THREE floors                  [review 3.5]
  C7  Attractor-to-threshold gap, both pools                [review 3.6]
  C8  D6 head/recharge persistence, both pools              [review 4.1]
  C9  Effect-size context                                   [review 3.7]

EXPLORATORY ONLY — not part of the frozen spec.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import run_j27_exploratory as R
import run_j27_intervention as I

OUT = R.OUT
rng = np.random.default_rng(20260910)


def rmse(e):
    e = np.asarray(e, float)
    return float(np.sqrt(np.mean(e ** 2)))


# ---------------------------------------------------------------- ladder core
def ladder_summary(panel, Rcol, Pcol, lo, hi, min_train=15):
    """Run the frozen ladder with an arbitrary (R,P) driver pair."""
    p = panel.copy()
    p["_R"] = p[Rcol].to_numpy(float)
    p["_P"] = p[Pcol].to_numpy(float)
    p = p[p["_R"].notna() & p["_P"].notna() & p["H_mean"].notna()].reset_index(drop=True)
    p = p.rename(columns={"H_mean": "H_mean"})
    # run_ladder expects columns: year, H_mean, <Rcol>, P_uv
    p["P_uv"] = p["_P"]
    _, summ = R.run_ladder(p, "_R", lo, hi)
    return summ, R.retention(summ), len(p), (int(p.year.min()), int(p.year.max()))


def h1h5(summ):
    h1 = summ[summ.horizon == 1].set_index("model")["rmse"]
    h5 = summ[summ.horizon == 5].set_index("model")["rmse"]
    return h1, h5


# ------------------------------------------------------------------- controls
def main():
    j17 = pd.read_csv(R.DATA / "annual_panel.csv")
    j17 = j17[["year", "H_mean"]].merge(
        pd.read_csv(R.DATA / "annual_panel.csv")[["year", "R_total", "P_wells"]], on="year")
    j27 = R.build_j27_panel()
    rec = R.load_recharge_uv()
    pmp = R.load_pumpage_uv()

    # full driver frame shared by both objects
    drv = rec.merge(pmp, on="year", how="left")
    drv["R_b1"] = pd.to_numeric(
        pd.read_csv(R.DATA / "usgs_recharge_1934_2024.txt", sep="\t")
        .assign(year=lambda d: d["Year"].astype(int))
        .set_index("year")["Basin_1"], errors="coerce").reindex(drv.year).to_numpy()
    drv["R_b2"] = pd.to_numeric(
        pd.read_csv(R.DATA / "usgs_recharge_1934_2024.txt", sep="\t")
        .assign(year=lambda d: d["Year"].astype(int))
        .set_index("year")["Basin_2"], errors="coerce").reindex(drv.year).to_numpy()

    out = {}

    # =============================================== C1: J-17 matched window
    print("=" * 78)
    print("C1  J-17 matched-window control (restrict to 1941-2023, as J-27)")
    print("=" * 78)
    j17f = j17[j17.R_total.notna() & j17.P_wells.notna()].reset_index(drop=True)
    s_full, ret_full, n_full, yr_full = ladder_summary(j17f, "R_total", "P_wells", 610.0, 710.0)
    j17w = j17f[j17f.year >= 1941].reset_index(drop=True)
    s_win, ret_win, n_win, yr_win = ladder_summary(j17w, "R_total", "P_wells", 610.0, 710.0)

    print(f"  frozen window {yr_full} (n={n_full}):  persist={h1h5(s_full)[0]['naive_persist']:.2f} "
          f"M1={h1h5(s_full)[0]['M1']:.2f} M2={h1h5(s_full)[0]['M2']:.2f} "
          f"M2m={h1h5(s_full)[0]['M2m']:.2f}")
    print(f"     retained_as_structure = {ret_full['retained_as_structure']}")
    print(f"  matched window {yr_win} (n={n_win}): persist={h1h5(s_win)[0]['naive_persist']:.2f} "
          f"M1={h1h5(s_win)[0]['M1']:.2f} M2={h1h5(s_win)[0]['M2']:.2f} "
          f"M2m={h1h5(s_win)[0]['M2m']:.2f}")
    print(f"     retained_as_structure = {ret_win['retained_as_structure']}")
    same = ret_full["retained_as_structure"] == ret_win["retained_as_structure"]
    print(f"  VERDICT UNCHANGED across windows: {same}")
    m2_ret_full = "M2" in ret_full["retained_as_structure"]
    m2_ret_win = "M2" in ret_win["retained_as_structure"]
    print(f"  M2 retained? full={m2_ret_full}  matched={m2_ret_win}")
    out["C1_j17_window"] = {
        "full": {"window": yr_full, "persist": float(h1h5(s_full)[0]['naive_persist']),
                 "M1": float(h1h5(s_full)[0]['M1']), "M2": float(h1h5(s_full)[0]['M2']),
                 "M2m": float(h1h5(s_full)[0]['M2m']),
                 "retained": ret_full["retained_as_structure"]},
        "matched_1941": {"n": n_win, "persist": float(h1h5(s_win)[0]['naive_persist']),
                         "M1": float(h1h5(s_win)[0]['M1']), "M2": float(h1h5(s_win)[0]['M2']),
                         "M2m": float(h1h5(s_win)[0]['M2m']),
                         "retained": ret_win["retained_as_structure"]},
        "verdict_unchanged": bool(same), "M2_retained_full": bool(m2_ret_full),
        "M2_retained_matched": bool(m2_ret_win)}

    # =========================================== C2: J-17 mismatched driver
    print("\n" + "=" * 78)
    print("C2  J-17 mismatched-driver control (D5 applied to the HOME pool)")
    print("=" * 78)
    j17d = j17f.merge(drv, on="year", how="left")
    c2 = {}
    for label, Rcol in [("R_total (correct, San Antonio)", "R_total"),
                        ("R_uv Basin_1+2 (MISMATCHED, Uvalde)", "R_uv_12"),
                        ("R_sa->shuffled (NULL)", None)]:
        dd = j17d.copy()
        if Rcol is None:
            dd["Rs"] = dd["R_total"].sample(frac=1.0, random_state=7).to_numpy()
            Rcol = "Rs"
        s, ret, n, yy = ladder_summary(dd, Rcol, "P_wells", 610.0, 710.0)
        h1, _ = h1h5(s)
        c2[label] = {"persist": float(h1["naive_persist"]), "M1": float(h1["M1"]),
                     "M2": float(h1["M2"]), "M2m": float(h1["M2m"]),
                     "M2_retained": bool("M2" in ret["retained_as_structure"]),
                     "retained": ret["retained_as_structure"]}
        print(f"  R = {label:36s} persist={h1['naive_persist']:6.2f} M1={h1['M1']:6.2f} "
              f"M2={h1['M2']:6.2f} M2m={h1['M2m']:6.2f}  M2retained={c2[label]['M2_retained']}")
    # symmetric: J-27 under mismatched San Antonio driver
    j27d = j27.merge(drv, on="year", how="left")
    j27d = j27d[j27d.H_mean.notna()].reset_index(drop=True)
    s_uv, ret_uv, n_uv, yy_uv = ladder_summary(j27d, "R_uv_12", "P_uv", 820.0, 890.0)
    s_uvx, ret_uvx, _, _ = ladder_summary(j27d, "R_sa_total", "P_uv", 820.0, 890.0)
    print(f"\n  [J-27 control] R=Uvalde B1+2 : M2={h1h5(s_uv)[0]['M2']:.2f} "
          f"retained={ret_uv['retained_as_structure']}")
    print(f"  [J-27 control] R=SA Total   : M2={h1h5(s_uvx)[0]['M2']:.2f} "
          f"retained={ret_uvx['retained_as_structure']}")
    out["C2_mismatched"] = {"j17": c2,
                            "j27_as_sa": {"M2": float(h1h5(s_uvx)[0]['M2']),
                                          "retained": ret_uvx["retained_as_structure"]}}

    # ============================================ C3: J-27 driver ladder
    print("\n" + "=" * 78)
    print("C3  J-27 driver-definition ladder (all candidate recharge mappings)")
    print("=" * 78)
    c3 = {}
    for label, Rcol in [("Basin_1 only", "R_b1"), ("Basin_2 only", "R_b2"),
                        ("Basin_1+2", "R_uv_12"), ("Basin_1-4", "R_uv_1234"),
                        ("San Antonio Total (mismatched)", "R_sa_total"),
                        ("shuffled (NULL)", "R_shuf")]:
        dd = j27d.copy()
        if Rcol == "R_shuf":
            dd["R_shuf"] = dd["R_uv_12"].sample(frac=1.0, random_state=11).to_numpy()
        s, ret, n, yy = ladder_summary(dd, Rcol, "P_uv", 820.0, 890.0)
        h1, h5 = h1h5(s)
        c3[label] = {"persist": float(h1["naive_persist"]), "M1": float(h1["M1"]),
                     "M2": float(h1["M2"]), "M2m": float(h1["M2m"]),
                     "M2_h5": float(h5["M2"]), "persist_h5": float(h5["naive_persist"]),
                     "M2_retained": bool("M2" in ret["retained_as_structure"])}
        print(f"  R = {label:32s} h1: persist={h1['naive_persist']:6.2f} M2={h1['M2']:6.2f} "
              f"| h5: persist={h5['naive_persist']:6.2f} M2={h5['M2']:6.2f} "
              f"| M2ret={c3[label]['M2_retained']}")
    out["C3_driver_ladder_j27"] = c3

    # ================================ C4: component decomposition (R vs P)
    print("\n" + "=" * 78)
    print("C4  Component decomposition: which driver carries the h=1 gain?")
    print("=" * 78)
    c4 = {}
    for pool, dd, Pcol, lo, hi in [("J-27", j27d, "P_uv", 820.0, 890.0),
                                   ("J-17", j17d, "P_wells", 610.0, 710.0)]:
        Rcol = "R_uv_12" if pool == "J-27" else "R_total"
        print(f"  -- {pool} --")
        rows = {}
        for lab, use_R, use_P in [("full (R+P)", True, True),
                                  ("R only", True, False),
                                  ("P only", False, True),
                                  ("neither (const R,P)", False, False)]:
            x = dd.copy()
            if not use_R:
                x["_Rz"] = float(x[Rcol].mean())
                rc = "_Rz"
            else:
                rc = Rcol
            if not use_P:
                x["_Pz"] = float(x[Pcol].mean())
                pc = "_Pz"
            else:
                pc = Pcol
            s, ret, n, yy = ladder_summary(x, rc, pc, lo, hi)
            h1, h5 = h1h5(s)
            rows[lab] = {"M2_h1": float(h1["M2"]), "M2_h5": float(h5["M2"]),
                         "persist_h1": float(h1["naive_persist"]),
                         "gain_h1": float(h1["naive_persist"] - h1["M2"])}
            print(f"     {lab:20s} M2 h1={h1['M2']:6.2f}  h5={h5['M2']:6.2f}  "
                  f"gain_h1={rows[lab]['gain_h1']:+5.2f} ft")
        c4[pool] = rows
    out["C4_decomposition"] = c4

    # ==================================== C5: clip-bound sensitivity J-27
    print("\n" + "=" * 78)
    print("C5  Clip-bound sensitivity on J-27 (is the clip load-bearing?)")
    print("=" * 78)
    c5 = {}
    for lo, hi in [(820.0, 890.0), (800.0, 920.0), (822.7, 884.9), (700.0, 1000.0)]:
        s, ret, n, yy = ladder_summary(j27d, "R_uv_12", "P_uv", lo, hi)
        h1, h5 = h1h5(s)
        c5[f"[{lo},{hi}]"] = {"M2_h1": float(h1["M2"]), "M1_h1": float(h1["M1"]),
                              "persist_h1": float(h1["naive_persist"]),
                              "M2_retained": bool("M2" in ret["retained_as_structure"])}
        print(f"  clip [{lo:6.1f},{hi:6.1f}]  persist={h1['naive_persist']:6.2f} "
              f"M1={h1['M1']:6.2f} M2={h1['M2']:6.2f}  M2ret={c5[f'[{lo},{hi}]']['M2_retained']}")
    out["C5_clip_sensitivity"] = c5

    # =============================== C6: kernel status under ALL floors
    print("\n" + "=" * 78)
    print("C6  Robust-kernel status under ALL THREE floors (Uvalde thresholds)")
    print("=" * 78)
    j27i = j27d[j27d.R_uv_12.notna() & j27d.P_uv.notna()].reset_index(drop=True)
    fit_uv = I.fit_affine(j27i)
    tr = j27i[j27i.year <= 1990]
    Pbar = float(tr.P_uv.mean())
    Wtr = tr.R_uv_12.to_numpy(float)
    floors = {"UC_min": float(Wtr.min()), "UC_q05": float(np.percentile(Wtr, 5)),
              "UC_q10": float(np.percentile(Wtr, 10))}
    pols = I.make_policies(Pbar)
    c6 = {}
    for K in [835.0, 840.0, 845.0]:
        for uc, W in floors.items():
            row = {}
            for name in ["BAU", "flat_90", "flat_60", "flat_0", "S1uv", "cpm_uv"]:
                k = I.kernel(pols[name], fit_uv, W, K, "inf")
                row[name] = None if not k else float(k[-1][1])
            c6[f"K{int(K)}_{uc}"] = row
    for K in [835.0, 840.0, 845.0]:
        print(f"  -- K = {K:.0f} ft --")
        for uc in floors:
            row = c6[f"K{int(K)}_{uc}"]
            nonempty = [n for n, v in row.items() if v is not None]
            print(f"     {uc:7s} (W_lo={floors[uc]:6.1f}): nonempty={nonempty if nonempty else 'NONE'}")
    out["C6_kernels_all_floors"] = {"floors": floors, "kernels": c6}

    # ==================== C7: attractor-to-threshold gap, both pools
    print("\n" + "=" * 78)
    print("C7  Attractor-to-threshold gap (the key structural comparability variable)")
    print("=" * 78)
    def fixpoint(fit, W, P):
        return (fit["alpha"] + fit["beta"] * W + fit["gamma"] * P) / (1 - fit["a"])
    # J-27
    gaps = {}
    for lab, W, K in [("J-27 BAU vs 840 (Stage V)", floors["UC_min"], 840.0),
                      ("J-27 flat-0 vs 840", floors["UC_min"], 840.0)]:
        P = Pbar if "BAU" in lab else 0.0
        Hst = fixpoint(fit_uv, W, P)
        gaps[lab] = {"H_star": Hst, "threshold": K, "gap_ft": K - Hst}
        print(f"  {lab:32s} H*={Hst:7.2f}  K={K:.0f}  gap={K-Hst:+7.2f} ft  "
              f"{'BELOW (not holdable)' if Hst < K else 'above'}")
    # J-17
    j17i = j17f[j17f.year.between(1934, 2023)].reset_index(drop=True)
    fit_sa = I.fit_affine(j17i.rename(columns={"R_total": "R_uv_12", "P_wells": "P_uv"}))
    tr_sa = j17i[j17i.year <= 1990]
    Pbar_sa = float(tr_sa.P_wells.mean())
    W_sa = float(tr_sa.R_total.min())     # perpetual-1956 floor == min of training recharge
    for K, lab in [(618.0, "J-17 BAU vs 618 (physical)"), (660.0, "J-17 BAU vs 660 (institutional)")]:
        Hst = fixpoint(fit_sa, W_sa, Pbar_sa)
        gaps[lab] = {"H_star": Hst, "threshold": K, "gap_ft": K - Hst}
        print(f"  {lab:32s} H*={Hst:7.2f}  K={K:.0f}  gap={K-Hst:+7.2f} ft  "
              f"{'BELOW (not holdable)' if Hst < K else 'above'}")
    Hst0_sa = fixpoint(fit_sa, W_sa, 0.0)
    print(f"  {'J-17 flat-0 vs 618':32s} H*={Hst0_sa:7.2f}  K=618  gap={618-Hst0_sa:+7.2f} ft")
    gaps["J-17 flat-0 vs 618"] = {"H_star": Hst0_sa, "threshold": 618.0, "gap_ft": 618 - Hst0_sa}
    Hst0_uv = fixpoint(fit_uv, floors["UC_min"], 0.0)
    print(f"  {'J-27 flat-0 vs 840':32s} H*={Hst0_uv:7.2f}  K=840  gap={840-Hst0_uv:+7.2f} ft")
    gaps["J-27 flat-0 vs 840"] = {"H_star": Hst0_uv, "threshold": 840.0, "gap_ft": 840 - Hst0_uv}
    out["C7_gaps"] = gaps

    # ======================== C8: D6 persistence, both pools
    print("\n" + "=" * 78)
    print("C8  D6  head / recharge persistence, both pools")
    print("=" * 78)
    def ac1(x):
        x = np.asarray(x, float); x = x[np.isfinite(x)]
        return float(np.corrcoef(x[1:], x[:-1])[0, 1])
    d6 = {"head_ac1_j17": ac1(j17f.H_mean), "head_ac1_j27": ac1(j27i.H_mean),
          "recharge_ac1_j17": ac1(j17f.R_total), "recharge_ac1_j27": ac1(j27i.R_uv_12),
          "head_sd_j17": float(np.std(j17f.H_mean, ddof=1)),
          "head_sd_j27": float(np.std(j27i.H_mean, ddof=1))}
    for k, v in d6.items():
        print(f"  {k:22s} {v:8.3f}")
    out["C8_D6"] = d6

    # ======================== C9: effect size context
    print("\n" + "=" * 78)
    print("C9  Effect-size context for the J-27 h=1 gap")
    print("=" * 78)
    s, ret, n, yy = ladder_summary(j27d, "R_uv_12", "P_uv", 820.0, 890.0)
    h1, h5 = h1h5(s)
    gap = float(h1["naive_persist"] - h1["M2"])
    c9 = {"gap_h1_ft": gap, "persist_h1": float(h1["naive_persist"]),
          "M2_h1": float(h1["M2"]),
          "head_sd_ft": d6["head_sd_j27"],
          "gap_as_pct_of_head_sd": 100 * gap / d6["head_sd_j27"],
          "M2_regression_at_h5_ft": float(h5["M2"] - h5["naive_persist"]),
          "annual_rule_thresholds_ft": [845, 840, 835],
          "note": "operational thresholds are declared in whole feet; a 0.84 ft RMSE "
                  "edge is ~6% of the head series SD and is far below the ~10-25 ft "
                  "attractor-to-threshold gaps that decide protection"}
    for k, v in c9.items():
        print(f"  {k:28s} {v}")
    out["C9_effect_size"] = c9

    with open(OUT / "j27_controls_strengthening.json", "w") as f:
        json.dump({"status": "EXPLORATORY_NOT_FROZEN", **out}, f, indent=2)
    print(f"\nwritten: {OUT/'j27_controls_strengthening.json'}")
    return out


if __name__ == "__main__":
    main()

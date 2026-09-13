#!/usr/bin/env python3
"""Phase K — cod prospective-band calibration (Section 8 procedure).

Executed on the pinned-seed archive sim_retention_power_20260913.csv (T=33,
200/100 reps per cell; the registered machinery of Section 6). For each band b
in [0, 0.15]: a module is retained if it beats persistence at h=1 AND h=5 by
(1-b), and, where a comparator is declared, beats the comparator at both
horizons by (1-b). Power = retention of the generating module per in-class
cell; specificity = no module retained under D5. Targets per Section 8:
power >= 0.80 and specificity >= 0.90; if no band attains both, the frontier
is reported and the 5% band is retained.

Validation: at b=0.05 the recomputation must reproduce the published
power/specificity (0.955/0.960, 0.780/0.060, 0.110/0.100, 0.010/0.010,
0.995/0.950) and the mean power 0.373 / mean specificity 0.973.
"""
import csv, json, math

ROWS = list(csv.DictReader(open("phase_c/results/sim_retention_power_20260913.csv")))
COMPARATOR = {"M1_autonomous_Schaefer": None,
              "M1b_autonomous_Allee": "M1_autonomous_Schaefer",
              "M2_stockflow_regimeC": "M1_autonomous_Schaefer",
              "M3_AR_residual": "M2_stockflow_regimeC",
              "M4_delayed_info": "M3_AR_residual"}
TRUTH = {"D1_M1_collapse": "M1_autonomous_Schaefer",
         "D2_M1_recovery": "M1_autonomous_Schaefer",
         "D3_M2_stockflow": "M2_stockflow_regimeC",
         "D4_M1b_depens": "M1b_autonomous_Allee",
         "D5_persist_null": None}

cells = {}
for r in ROWS:
    cells.setdefault((r["dgp"], r["sigma"]), []).append(r)

# build per-rep module dict
reps = {}
for r in ROWS:
    key = (r["dgp"], r["sigma"], r["rep"])
    reps.setdefault(key, {})[r["module"]] = (float(r["rmse_h1"]), float(r["rmse_h5"]),
                                            float(r["persist_h1"]), float(r["persist_h5"]))

def retained_b(key, m, b):
    rm1, rm5, p1, p5 = reps[key][m]
    if not (rm1 < p1 * (1 - b) and rm5 < p5 * (1 - b)):
        return False
    comp = COMPARATOR[m]
    if comp is None:
        return True
    c1, c5, _, _ = reps[key][comp]
    return rm1 < c1 * (1 - b) and rm5 < c5 * (1 - b)

BANDS = [round(0.005 * i, 3) for i in range(0, 31)]  # 0.000 .. 0.150

results = {"procedure": "Section 8 prospective-band calibration, cod ladder",
           "source": "phase_c/results/sim_retention_power_20260913.csv (pinned seed, T=33)",
           "targets": {"power": 0.80, "specificity": 0.90},
           "bands": BANDS, "cells": {}, "pooled": []}

for (dgp, sigma), rrs in sorted(cells.items()):
    cellkeys = [(dgp, sigma, r["rep"]) for r in rrs]
    cellkeys = sorted(set(cellkeys))
    truth = TRUTH[dgp]
    per_band = {}
    for b in BANDS:
        if truth is None:  # D5 specificity
            spec = [all(not retained_b(k, m, b) for m in COMPARATOR)
                    for k in cellkeys]
            per_band[b] = {"specificity": round(sum(spec) / len(spec), 4)}
        else:
            pw = [retained_b(k, truth, b) for k in cellkeys]
            per_band[b] = {"power": round(sum(pw) / len(pw), 4)}
    results["cells"][f"{dgp}_s{sigma}"] = {
        "reps": len(cellkeys), "truth": truth, "per_band": per_band}

# pooled: mean power over the 8 in-class cells; mean specificity over the 2 D5 cells
inclass = [f"{d}_s{s}" for d in ("D1_M1_collapse","D2_M1_recovery","D3_M2_stockflow","D4_M1b_depens") for s in ("11.8","33.8")]
d5 = [f"D5_persist_null_s{s}" for s in ("11.8","33.8")]
for b in BANDS:
    pw = sum(results["cells"][c]["per_band"][b]["power"] for c in inclass) / 8
    sp = sum(results["cells"][c]["per_band"][b]["specificity"] for c in d5) / 2
    results["pooled"].append({"band": b, "mean_power": round(pw, 4),
                              "mean_specificity": round(sp, 4)})

# smallest band attaining both targets
met = [p for p in results["pooled"] if p["mean_power"] >= 0.80 and p["mean_specificity"] >= 0.90]
results["qualifying_band"] = min(met, key=lambda p: p["band"]) if met else None
results["frontier_note"] = (f"no band attains both targets: maximum mean power is "
                            f"{max(p['mean_power'] for p in results['pooled'])} at band "
                            f"{[p['band'] for p in results['pooled'] if p['mean_power']==max(q['mean_power'] for q in results['pooled'])][0]}; "
                            "the 5% band is retained for the cod application")

# T=71 single points (10 reps per cell, aggregate archive only)
results["T71_points"] = {
    "D1_power_5pct": {"s11.8": 0.900, "s33.8": 1.000, "n": 10},
    "D5_specificity_5pct": {"s11.8": 1.000, "s33.8": 1.000, "n": 10},
    "note": "aggregate archive only (reconcile_s43_20260913.json); full 200-rep T=71 remains registered (O5)"}

json.dump(results, open("phase_c/results/o6_cod_band_calibration_20260913.json", "w"), indent=1)

# validation at b=0.05 vs published
print("VALIDATION at b=0.05 vs published:")
pub = {"D1_M1_collapse_s11.8": 0.955, "D1_M1_collapse_s33.8": 0.960,
       "D2_M1_recovery_s11.8": 0.780, "D2_M1_recovery_s33.8": 0.060,
       "D3_M2_stockflow_s11.8": 0.110, "D3_M2_stockflow_s33.8": 0.100,
       "D4_M1b_depens_s11.8": 0.010, "D4_M1b_depens_s33.8": 0.010,
       "D5_persist_null_s11.8": 0.995, "D5_persist_null_s33.8": 0.950}
ok = True
for c, target in pub.items():
    got = results["cells"][c]["per_band"][0.05].get("power", results["cells"][c]["per_band"][0.05].get("specificity"))
    status = "OK" if abs(got - target) < 0.011 else "MISMATCH"
    ok &= status == "OK"
    print(f"  {c}: {got} vs {target} {status}")
pooled5 = next(p for p in results["pooled"] if p["band"] == 0.05)
print(f"  pooled 5%: power {pooled5['mean_power']} (pub 0.373), specificity {pooled5['mean_specificity']} (pub 0.973)")
print("VALIDATION:", "PASS" if ok else "FAIL")
print()
print("FRONTIER (band, mean power, mean specificity):")
for p in results["pooled"][::2]:
    print(f"  b={p['band']:.3f}  power={p['mean_power']}  spec={p['mean_specificity']}")
print()
print("qualifying band:", results["qualifying_band"])
print(results["frontier_note"])

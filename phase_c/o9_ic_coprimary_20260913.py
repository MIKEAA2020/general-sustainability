#!/usr/bin/env python3
"""O9 — co-primary information-criterion check (Phase G, merged plan).

Instrument (disclosed definition): IC_m = n ln(RMSE_m^2) + 2 k_m, one-step (h=1),
with k_m = number of fitted scalar parameters: M1 2 (r,K), M1b 3 (+s), M2 2,
M3 3 (+phi), M4 3 (+phi), persistence 0. Data-derived constants (training-mean
catch/fluxes, the naive training mean itself) count as k=0. n = 33 (simulation),
33/71/90 (objects: cod Spec A / Spec B / Edwards, the paper's origin counts).

Part 1 (simulation, pinned-seed archive sim_retention_power_20260913.csv):
- ident_among: per replicate, the IC-best among the five structural candidates
  is the generating module (matches the paper's identification definition —
  validated against identification_limit_20260913.json via the no-penalty
  variant, which must reproduce its truth_best_h1_rate exactly).
- D5 false identification: the IC prefers a structural module over persistence
  under persistence truth (IC(persist) is not the global minimum).

Part 2 (scored objects, published rolling h=1 RMSEs + origin counts):
IC per module per object; IC-best per object; comparison with the standard's
verdicts (empty retained set).
"""
import csv, json, math

K = {"M1_autonomous_Schaefer": 2, "M1b_autonomous_Allee": 3,
     "M2_stockflow_regimeC": 2, "M3_AR_residual": 3, "M4_delayed_info": 3}
N_SIM = 33
STRUCT = list(K)
rows = list(csv.DictReader(open("phase_c/results/sim_retention_power_20260913.csv")))
cells = {}
for r in rows:
    cells.setdefault((r["dgp"], r["sigma"]), []).append(r)

def ic(rmse, k, n=N_SIM):
    return n * math.log(max(rmse, 1e-6) ** 2) + 2 * k

truth_of = {"D1_M1_collapse": "M1_autonomous_Schaefer",
            "D2_M1_recovery": "M1_autonomous_Schaefer",
            "D3_M2_stockflow": "M2_stockflow_regimeC",
            "D4_M1b_depens": "M1b_autonomous_Allee",
            "D5_persist_null": None}

part1 = {"n_sim": N_SIM, "k": K,
         "definition": "IC = n ln(RMSE_h1^2) + 2k, one-step; persistence k=0"}
for (dgp, sigma), cellrows in sorted(cells.items()):
    reps = {}
    for r in cellrows:
        reps.setdefault(r["rep"], []).append(r)
    n_id, n_false, n_id_nopen = 0, 0, 0
    for rep, rrs in reps.items():
        s_ic = {r["module"]: ic(float(r["rmse_h1"]), K[r["module"]]) for r in rrs}
        s_np = {r["module"]: ic(float(r["rmse_h1"]), 0) for r in rrs}
        p_ic = ic(float(rrs[0]["persist_h1"]), 0)
        best_ic = min(s_ic, key=s_ic.get)
        best_np = min(s_np, key=s_np.get)
        if truth_of[dgp] is not None:
            if best_ic == truth_of[dgp]:
                n_id += 1
            if best_np == truth_of[dgp]:
                n_id_nopen += 1
        else:  # D5: false identification = any structural module beats persistence
            if min(s_ic.values()) < p_ic:
                n_false += 1
    m = len(reps)
    part1[f"{dgp}_s{sigma}"] = {"reps": m}
    if truth_of[dgp] is not None:
        part1[f"{dgp}_s{sigma}"].update(
            ic_ident_among=round(n_id / m, 3),
            no_penalty_ident_among=round(n_id_nopen / m, 3))
    else:
        part1[f"{dgp}_s{sigma}"]["ic_false_ident_rate"] = round(n_false / m, 3)

# --- Part 2: scored objects --------------------------------------------
part2 = {"definition": part1["definition"]}
objects = [
    # name, n_origins, [(module, k, rmse_h1)] — closest structural module per
    # object (the others are strictly worse, so the check is decisive)
    ("cod_SpecA", 33, [
        ("persistence", 0, 98.05), ("M1b_autonomous_Allee", 3, 114.80)]),
    ("cod_SpecB", 71, [
        ("persistence", 0, 87.65), ("M1_autonomous_Schaefer", 2, 119.47)]),
    ("edwards_J17", 90, [
        ("persistence", 0, 13.230), ("M1_AR_affine", 2, 12.839),
        ("M2_stockflow", 2, 14.698), ("M2m_climatological-flux_map", 2, 12.283),
                ("M3_residual", 3, 14.46), ("M4_delay", 3, 14.30)]),
]
for name, n, mods in objects:
    vals = {m: n * math.log(max(rmse, 1e-6) ** 2) + 2 * k for m, k, rmse in mods}
    best = min(vals, key=vals.get)
    part2[name] = {"n_origins": n,
                   "ic": {m: round(v, 2) for m, v in vals.items()},
                   "ic_best": best}

out = {"part1_simulation": part1, "part2_scored_objects": part2,
       "note": ("Part 1: ident_among = IC-best among the five structural candidates "
                "(paper's identification definition; the no-penalty variant is the "
                "validation against identification_limit_20260913.json); D5 false "
                "identification = a structural module's IC beats persistence under "
                "persistence truth. Part 2 uses the paper's published rolling h=1 "
                "RMSEs (Sections 4 and 5) and origin counts (33/71/90). Cod Spec A M1b "
                "114.80 is the closest structural module; the others are strictly "
                "worse, so the check is decisive. Edwards M3/M4 RMSEs from the "
                "companion's Table 4 (14.46/14.30; the paper's 1.63%/1.13% margins "
                "are versus M2/M3).")}
json.dump(out, open("phase_c/results/o9_ic_coprimary_20260913.json", "w"),
          indent=1)

# validation: no-penalty ident among must equal the archived truth_best_h1_rate
arch = json.load(open("phase_c/results/identification_limit_20260913.json"))
ok = True
for (dgp, sigma), cell in sorted(cells.items()):
    key = f"{dgp}_s{sigma}"
    if truth_of[dgp] is None:
        continue
    mine = part1[key]["no_penalty_ident_among"]
    theirs = arch["cells"][key]["truth_best_h1_rate"]
    status = "OK" if abs(mine - theirs) < 1e-9 else "MISMATCH"
    ok &= status == "OK"
    print(f"validate {key}: mine={mine} archived={theirs} {status}")
print("VALIDATION:", "PASS" if ok else "FAIL")
print(json.dumps(out, indent=1))

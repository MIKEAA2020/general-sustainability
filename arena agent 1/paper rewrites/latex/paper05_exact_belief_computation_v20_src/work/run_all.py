"""Build work/results.json for paper05 v20 (all exact).  `python3 run_all.py`
runs everything (~15 min); `--quick` reuses cached stage outputs."""
import json, os, sys, time, re
from fractions import Fraction as Q
import numpy as np

from p05_core import (cells, actions, drift_by_distance, rstar, pair_bound_distance, kleitman_bound,
                      game_value, horizon_bound, forward_horizon, certified_threshold, ham, D,
                      product_mixture, periodic_word, word_dip)
import classify, observation, pbvi, float_study

QUICK = "--quick" in sys.argv
T0 = time.time()
times = {}


def stage(name, fn, cache):
    t = time.time()
    if QUICK and os.path.exists(cache):
        out = json.load(open(cache))
        times[name] = "cached"
        return out
    out = fn()
    json.dump(out, open(cache, "w"), indent=1, default=str)
    times[name] = round(time.time() - t, 1)
    return out


R = {"version": "v20", "units": "tenths of stock above the floor; D = 2<u,theta> - 5; L = 10 (z0 - 1)"}

# ---- cube facts
R["cube"] = {}
for m in (4, 5, 6, 7, 8):
    R["cube"][m] = {"n_cells": 2 ** m, "n_actions": 2 ** m + 1,
                    "drift_by_distance": {h: drift_by_distance(m, h) for h in range(m + 1)},
                    "rstar": rstar(m), "ball_size": sum(__import__("math").comb(m, i) for i in range(rstar(m) + 1)),
                    "pair_distance_bound": pair_bound_distance(m),
                    "kleitman": kleitman_bound(m, pair_bound_distance(m)),
                    "first_split_cost": 2 * m + 5}

# ---- classification m = 4, 5, 6
def do_classify():
    return {str(m): classify.classify(m, verbose=False) for m in (4, 5, 6)}
R["classification"] = stage("classification", do_classify, "classify_out.json")

# ---- pairs: V and thresholds by distance, horizon tightness
def do_pairs():
    out = {}
    for m in (4, 5, 6):
        C = cells(m)
        a = C[0]
        rows = []
        for h in range(0, m + 1):
            b = tuple(-x if i < h else x for i, x in enumerate(a))
            V, y, q = game_value([a, b])
            row = {"h": h, "V": str(V), "survivable": V >= Q(5, 2)}
            if V >= Q(5, 2):
                row["threshold"] = certified_threshold([a, b])["L"]
            else:
                hz = []
                for L in (0, 5, 10, 15, 20):
                    ex, fr = forward_horizon([a, b], L, max_steps=100)
                    hz.append({"L": L, "exact": ex, "bound": horizon_bound(L, V)})
                row["horizon"] = hz
            rows.append(row)
        out[str(m)] = rows
    return out
R["pairs"] = stage("pairs", do_pairs, "pairs_out.json")

# ---- observation: feedback game, deadline, cell-sum, ladder
def do_obs():
    out = {}
    for m in (4, 5, 6):
        z = np.load(f"census_m{m}.npz")
        Cc = cells(m)
        levels = sorted(int(k[5:]) for k in z.files if k.startswith("max_L"))
        fam = {L: [pbvi.mask_to_set(mk, Cc) for mk in z[f"max_L{L}"]] for L in levels}
        lad = observation.ladder(m, fam)
        d = {"ladder": {L: [str(v) for v in row] for L, row in lad.items()},
             "deadline": observation.deadline_table(m, [0, 5, 10, 13, 15, 20, 25]),
             "cell_sum": observation.cell_sum_identity(m), "first_split": observation.first_split_requirement(m)}
        if m <= 5:
            d["feedback"] = observation.feedback_study(m)
        out[str(m)] = d
    return out
R["observation"] = stage("observation", do_obs, "observation_out.json")

# ---- point-based evaluation and obstructions
def do_pbvi():
    out = {}
    for m in (4, 5, 6):
        z = np.load(f"census_m{m}.npz")
        if m < 6:
            out[str(m)] = {"pbvi": pbvi.study(m, list(range(0, 16)), 4, z["masks"], z["thr"])}
        else:
            out[str(m)] = {"pbvi": pbvi.study(m, [0, 1, 3, 5, 10, 15], 3, z["masks"], z["thr"])}
        out[str(m)]["obstructions"] = pbvi.obstructions(m, z["masks"], z["cliques"])
    return out
R["pbvi"] = stage("pbvi", do_pbvi, "pbvi_out.json")

# ---- float study
R["float"] = stage("float", lambda: float_study.run(10 ** 5, 2000), "float_out.json")

# ---- Lean inventory
def do_lean():
    here = os.path.dirname(os.path.abspath(__file__))
    base = next(d for d in (os.path.join(here, "..", "src", "lean"), os.path.join(here, "..", "lean")) if os.path.isdir(d))
    mods = {}
    for fn in sorted(os.listdir(base)):
        if fn.endswith(".lean"):
            txt = open(os.path.join(base, fn), encoding="utf8").read()
            thms = re.findall(r"^\s*(?:@\[[^\]]*\]\s*)?(?:theorem|lemma)\s+([^\s:({]+)", txt, re.M)
            mods[fn] = {"theorems": len(thms), "names": thms, "sorry": len(re.findall(r"\bsorry\b", txt))}
    return {"modules": mods, "total_theorems": sum(v["theorems"] for v in mods.values()),
            "total_sorry": sum(v["sorry"] for v in mods.values())}
R["lean"] = stage("lean", do_lean, "lean_out.json")

if not QUICK:
    times["total"] = round(time.time() - T0, 1)
    json.dump(times, open("times.json", "w"), indent=1)
elif os.path.exists("times.json"):
    full = json.load(open("times.json"))
    times = {k: full.get(k, v) for k, v in times.items()}
    times["total"] = full.get("total")
R["times"] = times
R["total_time_s"] = times.get("total")
json.dump(R, open("results.json", "w"), indent=1, default=str)
print("results.json written", R["total_time_s"], times)

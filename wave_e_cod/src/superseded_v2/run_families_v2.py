# ===========================================================================
# SUPERSEDED -- DO NOT USE, DO NOT CITE.
#
# This file was generated on the registered (v2) basis. v2 fits (r, K) under
# the SOURCE-YEAR catch convention (run_ladder.fit_params uses C[:-1]) and then
# measures the disturbance under the DESTINATION-YEAR convention. That hybrid
# is not a convention; see repo/wave_e_cod/src/run_intervention_v3.py.
#
# Authoritative replacement: run_families_v3.py  ->  results/e2_families_v3.csv
#
# Reverted 2026-09-28. Retained only so the record of what was done survives.
# ===========================================================================

# Regenerate E2 Table 1 on the registered (v2) basis, including the reactive
# families.  Same construction as run_v15b_existing.py, but importing the v2
# runner instead of the source-year runner, and WRITING an archive rather than
# printing to stdout.
from __future__ import annotations
import csv
import os
import run_intervention_v2 as base

import numpy as np

K_STAR = base.K_STAR
FIT = base.fit_surplus()
R, K = FIT["r"], FIT["K"]


def g(S):
    return base.surplus(S, R, K)


GRID = []
s = 1.0
while s < 1400:
    GRID.append(s)
    s += 25
s = 1400
while s < base.S_HI:
    GRID.append(s)
    s += 200
GRID.append(base.S_HI)
GRID = sorted(set(GRID))

UC = {
    "UC_min": FIT["train_residual_min"],
    "UC_q05": FIT["train_residual_q05"],
    "UC_q10": FIT["train_residual_q10"],
}


def mk(fn):
    return {"fn": fn, "thresholds": list(GRID), "label": ""}


policies = {}
for ph in (0.25, 0.50, 0.75):
    policies[f"A_phi{ph}"] = mk(lambda S, ph=ph: ph * g(S) if S >= K_STAR else 0.0)


def graded2(S):
    return 0.0 if S < K_STAR else (60.0 if S < 1.25 * K_STAR else 90.0)


def graded3(S):
    if S < K_STAR:
        return 0.0
    if S < 1.15 * K_STAR:
        return 30.0
    if S < 1.35 * K_STAR:
        return 60.0
    return 90.0


policies["B_graded2"] = mk(graded2)
policies["B_graded3"] = mk(graded3)


def bd(pol, uc, T):
    k = (base.kernel_inf_stable(pol, FIT, UC[uc], K_STAR)
         if T == "inf" else base.kernel(pol, FIT, UC[uc], K_STAR, T))
    return base.boundary(k)


OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results")
os.makedirs(OUT, exist_ok=True)
rows = []
for pid in policies:
    for uc in ("UC_min", "UC_q05", "UC_q10"):
        for T in (1, 5, "inf"):
            b = bd(policies[pid], uc, T)
            rows.append({
                "policy": pid,
                "class": uc,
                "T": T,
                "boundary": "" if b is None else f"{b:.4f}",
                "mean_C": f"{base.supply_replay(FIT, policies[pid])['train_mean_C']:.4f}",
            })

with open(os.path.join(OUT, "e2_families_v2.csv"), "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=["policy", "class", "T", "boundary", "mean_C"])
    w.writeheader()
    w.writerows(rows)

print(f"wrote {os.path.join(OUT, 'e2_families_v2.csv')} ({len(rows)} rows)")
print()
print("Registered (v2) basis -- disturbance classes:")
for k, v in UC.items():
    print(f"  {k:7s} = {v:.5f}")
print()
print(f"{'policy':12s} {'minT1':>9s} {'minTinf':>9s} {'q05T1':>9s} {'q05Tinf':>9s} {'q10T1':>9s} {'q10Tinf':>9s}")
for pid in policies:
    cells = []
    for uc in ("UC_min", "UC_q05", "UC_q10"):
        for T in (1, "inf"):
            b = bd(policies[pid], uc, T)
            cells.append("empty" if b is None else f"{b:.1f}")
    print(f"{pid:12s} " + " ".join(f"{c:>9s}" for c in cells))

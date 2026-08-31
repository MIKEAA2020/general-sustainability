#!/usr/bin/env python3
"""
Recomputation campaign E4 — Stage II–IV occupancies (registered revision item
of paperE4_edwards_intervention: the CPM cascade supply figure uses the
observed Stage-I occupancy; the Stage II–IV occupancies that would make the
deeper cuts bite were not separately recorded).

Produces:
  - occupancy counts and fractions of the measured J-17 annual head
    (H_mean, ft AMSL) below each declared stage threshold (660 / 650 / 640 /
    630 ft), for the full record 1934-2023, the training era (<= 1990), and
    the out-of-sample era (1991-2023);
  - the year lists of each stage;
  - the cascade supply replay reproduced with the committed runner
    (supply_replay_actual, cpm policy) as the cross-check, plus the stagewise
    decomposition of the cascade's mean pumping cut on the measured record
    (fraction of years in each stage x cumulative cut), which must agree with
    the replay's train_mean_P within rounding.

Writes results to rerun_campaigns/results/; modifies nothing committed.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

REPO = Path("/home/user/repo")
SRC = REPO / "wave_e_edwards" / "src"
OUT = Path(__file__).resolve().parent / "results"
OUT.mkdir(exist_ok=True)
sys.path.insert(0, str(SRC))


def _import(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


ri = _import("run_intervention", SRC / "run_intervention.py")

STAGES = {
    "Stage I  (< 660 ft)": 660.0,
    "Stage II (< 650 ft)": 650.0,
    "Stage III (< 640 ft)": 640.0,
    "Stage IV (< 630 ft)": 630.0,
}
CUTS = {660.0: 0.20, 650.0: 0.30, 640.0: 0.35, 630.0: 0.40}


def main():
    panel = ri.load_panel()
    yr = panel["year"].to_numpy()
    H = panel["H_mean"].to_numpy(float)

    rows = []
    for label, th in STAGES.items():
        below = H < th
        full = dict(
            label=label,
            era="full 1934-2023",
            n_years=int(below.sum()),
            n_total=int(len(H)),
            fraction=round(float(below.mean()), 4),
            years=", ".join(map(str, yr[below])),
        )
        tr_mask = yr <= ri.TRAIN_END
        oos_mask = yr > ri.TRAIN_END
        tr_m = tr_mask & below
        oos_m = oos_mask & below
        rows.append(full)
        rows.append(
            dict(
                label=label,
                era=f"train <= {ri.TRAIN_END}",
                n_years=int(tr_m.sum()),
                n_total=int(tr_mask.sum()),
                fraction=round(float(tr_m.sum() / tr_mask.sum()), 4),
                years=", ".join(map(str, yr[tr_m])),
            )
        )
        rows.append(
            dict(
                label=label,
                era=f"OOS {ri.TRAIN_END + 1}-2023",
                n_years=int(oos_m.sum()),
                n_total=int(oos_mask.sum()),
                fraction=round(float(oos_m.sum() / oos_mask.sum()), 4),
                years=", ".join(map(str, yr[oos_m])),
            )
        )
    occ = pd.DataFrame(rows)
    occ.to_csv(OUT / "campaign_e4_stage_occupancies.csv", index=False)

    # cross-check: committed replay machinery reproduces the cascade supply
    policies = ri.make_policies(282.16)  # P_bar = training-mean pumping (committed)
    replay = ri.supply_replay_actual(panel, policies["cpm"])
    committed = json.loads(
        (REPO / "wave_e_edwards" / "results" / "intervention_results.json").read_text()
    )
    committed_cpm = committed["supply"]["cpm"]

    # stagewise decomposition on the measured record (train era, matching the
    # committed replay's transition window t <= TRAIN_END)
    # cumulative structure: cut 20/30/35/40 at 660/650/640/630
    def stage_of(h):
        if h < 630.0:
            return "IV"
        if h < 640.0:
            return "III"
        if h < 650.0:
            return "II"
        if h < 660.0:
            return "I"
        return "none"

    tr_mask = yr <= ri.TRAIN_END
    stage_count_tr = pd.Series([stage_of(h) for h in H[tr_mask]]).value_counts()
    stage_count_full = pd.Series([stage_of(h) for h in H]).value_counts()
    n_tr = int(tr_mask.sum())
    decomp = {}
    for st, cut in (("I", 0.20), ("II", 0.30), ("III", 0.35), ("IV", 0.40)):
        f = stage_count_tr.get(st, 0) / n_tr
        decomp[f"frac_train_{st}"] = round(f, 4)
        decomp[f"mean_cut_contribution_train_{st}"] = round(f * cut, 6)
    decomp["mean_pumping_under_cpm_decomposition_train_era"] = round(
        282.16 * (1.0 - sum(v for k, v in decomp.items() if k.startswith("mean_cut_contribution"))),
        2,
    )
    decomp["replay_train_mean_P"] = replay["train_mean_P"]
    decomp["replay_oos_mean_P"] = replay["oos_mean_P"]
    decomp["committed_train_mean_P"] = committed_cpm["train_mean_P"]
    decomp["committed_oos_mean_P"] = committed_cpm["oos_mean_P"]
    decomp["stage_counts_train_era"] = stage_count_tr.to_dict()
    decomp["stage_counts_full_record"] = stage_count_full.to_dict()

    print("=== E4 stage occupancies ===")
    print(occ[["label", "era", "n_years", "n_total", "fraction"]].to_string(index=False))
    print("\n=== year lists (full record) ===")
    for label, th in STAGES.items():
        sub = occ[(occ.label == label) & (occ.era == "full 1934-2023")].iloc[0]
        print(f"  {label}: {sub['years']}")
    print("\n=== cascade supply cross-check ===")
    print(json.dumps(decomp, indent=2))

    (OUT / "campaign_e4_stage_occupancies.txt").write_text(
        occ.to_string(index=False) + "\n\n" + json.dumps(decomp, indent=2)
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Extract blocks removed between consecutive versions of each paper chain.
A 'removed block' = contiguous lines deleted or replaced that never reappear verbatim in the newer file."""
import difflib, re, json
from pathlib import Path

BASE = Path("/home/user/arena agen1")
CHAINS = {
    "P1": [f"paper1_assessment_separation{ s }.md" for s in ["", "_v2","_v3","_v4","_v5","_v6","_v7","_v8","_v9","_v10"]],
    "P2": [f"paper2_obstruction_calculus{ s }.md" for s in ["", "_v2","_v3","_v4"]],
    "P3": [f"paper3_material_ledgers{ s }.md" for s in ["","_v2","_v3","_v4","_v5","_v6","_v7","_v8","_v9","_v10","_v11","_v12","_v13","_v14","_v15"]],
    "P4": [f"paper4_delay_dynamics{ s }.md" for s in ["","_v2","_v3","_v4","_v5","_v6","_v7","_v8","_v9","_v10","_v11","_v12","_v13","_v14"]],
    "P5": [f"paper5_sampled_governance{ s }.md" for s in ["","_v2","_v3","_v4","_v5","_v6","_v7","_v8","_v9","_v10","_v11","_v12","_v13"]],
    "E1": [f"paperE1_cod_forecast_ladder{ s }.md" for s in ["","_v2","_v3","_v4","_v5","_v6"]],
    "E2": [f"paperE2_cod_intervention{ s }.md" for s in ["","_v2","_v3","_v4","_v5","_v6","_v7","_v8","_v9","_v10","_v11"]],
    "E3": [f"paperE3_edwards_forecast_ladder{ s }.md" for s in ["","_v2","_v3","_v4","_v5","_v6","_v7"]],
    "E4": [f"paperE4_edwards_intervention{ s }.md" for s in ["","_v2","_v3","_v4","_v5","_v6","_v7","_v8"]],
}

def norm(s):
    return re.sub(r"\s+", " ", s).strip()

report = {}
for chain, files in CHAINS.items():
    removed = []
    for a, b in zip(files, files[1:]):
        pa, pb = BASE / a, BASE / b
        if not pa.exists() or not pb.exists():
            continue
        ta = pa.read_text(encoding="utf-8").splitlines()
        tb = pb.read_text(encoding="utf-8").splitlines()
        sm = difflib.SequenceMatcher(None, ta, tb, autojunk=False)
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op in ("delete", "replace"):
                block = "\n".join(ta[i1:i2])
                nb = norm(block)
                if len(nb) < 180:  # skip tiny diffs
                    continue
                # skip blocks that reappear (approx) in the newer version
                tbn = norm("\n".join(tb))
                if nb[:60] in tbn and nb[-60:] in tbn:
                    continue
                removed.append({"from": a, "to": b, "len": len(nb), "block": block})
    report[chain] = removed
    print(f"{chain}: {len(removed)} removed blocks across {len(files)-1} transitions")

json.dump(report, open("/tmp/diff_report.json", "w"), indent=1)
print("saved /tmp/diff_report.json")

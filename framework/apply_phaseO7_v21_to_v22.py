#!/usr/bin/env python3
"""O7 cross-check fixes — v21_restructured -> v22_restructured (NEW-4a).

The companion cross-check (COMPANION_CROSSCHECK_20260913.md) found that E3 v16
retains M1 at h=1 by its pre-registered point rule (no band, h=1-only), which
F1's unified rule withholds; F1's Edwards section never reconciled the
companion's verdict. This pass adds the reconciliation and sharpens the
"no outcome changes" sentence. No verdict, number, or frozen element changes.
"""
import sys

SRC = "framework/paperF1_retention_framework_v21_restructured.md"
DST = "framework/paperF1_retention_framework_v22_restructured.md"

t = open(SRC).read()
applied = []

def rule(no, old, new):
    n = t.count(old)
    if n != 1:
        print(f"FAIL {no}: anchor occurs {n} times")
        sys.exit(1)
    globals()['t'] = t.replace(old, new, 1)
    applied.append(no)
    print(f"ok {no}")

rule("O7-01",
 "The 5% band is applied to the groundwater analysis although the original rule was fixed without a band; no outcome changes.",
 "The 5% band and the both-horizon requirement are applied to the groundwater analysis although the original pre-registered rule scored retention on h=1 alone and without a band; within the unified rule the band changes no outcome.")

rule("O7-02",
 "Under the unified rule with band, M2m fails H1 at h=1 (4.33% <5%) and is additionally declined on class grounds; without band it would pass H1 but still be declined on class grounds, so empty set holds either way.",
 "Under the unified rule with band, M2m fails H1 at h=1 (4.33% <5%) and is additionally declined on class grounds; without the band it would pass H1 but still be declined on class grounds, so the empty set holds either way. The companion's pre-registered h=1 point rule retains M1 provisionally — a 0.39 ft margin within noise, MAE tied at 10.72 versus 10.73 ft, a five-year loss — while the unified rule withholds it: the 2.96% h=1 margin lies inside the band and M1 loses at h=5 (21.25 versus 21.11 ft). The empty retained set is a property of the unified rule; the M1 difference between the two readings is a recorded rule-version difference, not a data difference.")

open(DST, "w").write(t)
print(f"\n{len(applied)} rules applied: v21 {len(open(SRC).read())} -> v22 {len(t)} chars")

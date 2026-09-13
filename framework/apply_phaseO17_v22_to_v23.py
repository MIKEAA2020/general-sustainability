#!/usr/bin/env python3
"""V9 remainder pass — v22_restructured -> v23_restructured (O17).

The final unimplemented V9 point worth adopting: V9-G asked for the M4/M5
competition protocols in the reproducibility paragraph; the paragraph cites the
M-competitions generically with Makridakis et al. (2020). This pass names the
M4 and M5 competitions and adds the M5 reference. No other V9 points remain
implementable without contradicting an owner decision or the paper's structure
(recorded in the merged plan).
"""
import sys

SRC = "framework/paperF1_retention_framework_v22_restructured.md"
DST = "framework/paperF1_retention_framework_v23_restructured.md"

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

rule("O17-01",
 "competition protocols with evaluation rules fixed in advance (the M-competitions; Makridakis et al., 2020)",
 "competition protocols with evaluation rules fixed in advance (the M4 and M5 competitions; Makridakis et al., 2020, 2022)")

rule("O17-02",
 "Makridakis, S., Spiliotis, E., Assimakopoulos, V., 2020. The M4 Competition: 100,000 time series and 54 methods. Int J Forecasting 36, 54–74.",
 "Makridakis, S., Spiliotis, E., Assimakopoulos, V., 2020. The M4 Competition: 100,000 time series and 54 methods. Int J Forecasting 36, 54–74.\n\nMakridakis, S., Spiliotis, E., Assimakopoulos, V., 2022. The M5 accuracy competition: results, findings, and conclusions. International Journal of Forecasting 38, 1346–1364.")

open(DST, "w").write(t)
print(f"\n{len(applied)} rules applied: v22 {len(open(SRC).read())} -> v23 {len(t)} chars")

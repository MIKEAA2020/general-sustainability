#!/usr/bin/env python3
"""Phase K paper edit — v23_restructured -> v24_restructured.

Records the executed cod prospective-band calibration (Section 8 procedure on
the pinned-seed archive) and its outcome: no band attains both targets; the
attainable frontier is reported; the 5% band is retained. Also adds the
calibration archive path to Data availability and the Edwards draft-sheet
registration note. No verdict, number, or frozen element changes.
"""
import sys

SRC = "framework/paperF1_retention_framework_v23_restructured.md"
DST = "framework/paperF1_retention_framework_v24_restructured.md"

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

rule("K-01",
 "The calibration applies to future applications only and does not re-open any verdict reported here.",
 """The calibration applies to future applications only and does not re-open any verdict reported here.

**Executed for the cod object.** Applying the procedure to the pinned-seed archive (Section 6.2), the frontier over bands of 0–15% declines from 0.444 mean power at band 0 to 0.312 at 15% while specificity rises from 0.760 to 1.000; at the narrowest band that meets the specificity target alone (3.5%, specificity 0.935) mean power is 0.395, and no band attains both targets — power is identification-limited at every width. The attainable frontier is therefore reported and the 5% band is retained for the cod application. The T=71 evidence is the registered ten-replicate point — D1 power 0.900/1.000 and D5 specificity 1.000/1.000 at the 5% band — and the full 200-replicate T=71 frontier remains the registered campaign. The Edwards calibration is registered in a draft specification sheet and precedes the first scored origin, whose inputs are archived (the 2024–2025 panel rows); Northern cod Specification B origins begin with origin 2025, scored once the vintage following the 2026 assessment is published.""")

rule("K-02",
 "o9_ic_coprimary_20260913.json (the co-primary information-criterion check of Section 6.5)",
 "o9_ic_coprimary_20260913.json (the co-primary information-criterion check of Section 6.5); o6_cod_band_calibration_20260913.json (the cod prospective-band calibration of Section 8)")

open(DST, "w").write(t)
print(f"\n{len(applied)} rules applied: v23 {len(open(SRC).read())} -> v24 {len(t)} chars")

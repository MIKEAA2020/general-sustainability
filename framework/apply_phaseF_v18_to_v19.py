#!/usr/bin/env python3
"""Phase F (journal-fit text pass) — v18 -> v19. Merged-plan items O1, O2, O3,
O10, O11, O13, O14. All text/table; no verdict contact; no new computation.

NEW-3 adjudication (recorded in the merged plan): F1 §5.2's "R-ENSO variant is
0.41 ft worse" and "M2_Rprecip and M2_Rar edge past M1 at h=1 (12.71 versus
12.84 ft)" contradict the archived E3 companion Table 7 (e3/paperE3_edwards_
forecast_ladder_v16.md) and the wave_e_edwards manuscript v2 Table 6, which
agree: M2_Rar is the 0.41 ft-worse module (13.25 vs 12.84); M2_Renso −0.02,
M2_Rprecip −0.04, M2_combo −0.13 stay within 0.13 ft of M1; the "edge past M1"
modules (Rprecip 14.52, Rar 14.67 vs M1 15.62) belong to the 2015–23
critical-period fixed window. The companion archive is authoritative; the F1
prose is corrected and the numbers move into a new Table 5b.
"""
import sys

SRC = "framework/paperF1_retention_framework_v18.md"
DST = "framework/paperF1_retention_framework_v19.md"

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

# ---- O2: informal term -> formal ----
rule("F01", "not second fibre of this specification.",
     "outside the scope of this specification.")

# ---- O1: abstract IC caveat (register 6.7 remainder) ----
rule("F02",
 "The information criterion outperforms the adopted rule on both axes — a finding about instrument choice within the standard, not against it.",
 "The information criterion outperforms the adopted rule on both axes — a finding about instrument choice within the standard, not against it; the criterion scores one-step accuracy and does not encode the decision-relevant requirement that a module beat persistence at the multi-year horizon, which the rule does.")

# ---- O3: NEW-3 climate correction + Table 5b ----
rule("F03",
 "Climate modules: three of four lie within 0.13 ft of AR(1), the R-ENSO variant is 0.41 ft worse, none retained; M2_Rprecip and M2_Rar edge past M1 at h=1 (12.71 versus 12.84 ft) while M2_Renso and combo do not; all lose to climatological fluxes. Under an M1 comparator the verdict is unchanged: the two modules that edge past M1 at h=1 still fail the persistence gate at h=5, where all three climate modules score 3–6 ft worse than persistence.",
 """Climate modules (Table 5b, companion Table 7): three of four lie within 0.13 ft of M1 at h=1 — M2_Rprecip 12.80 (−0.04), M2_Renso 12.82 (−0.02), M2_combo 12.71 (−0.13) — and the recharge-autoregression variant M2_Rar is 0.41 ft worse (13.25); none retained, all lose to climatological fluxes. On the 2015–23 critical-period window M2_Rprecip and M2_Rar edge past M1 (14.52 and 14.67 versus 15.62 ft) — a window-specific result, not a recharge forecast. Under an M1 comparator the verdict is unchanged: the modules that edge past M1 on that window still fail the persistence gate at h=5, where all four climate modules score 3–6 ft worse than persistence.

**Table 5b.** Climate-informed recharge modules on J-17, rolling origins (Table 7 of the Edwards companion). H is annual-mean head RMSE in feet; margins versus M1 at h=1.

| Module | H, h=1 (ft) | margin vs M1 | H, h=5 (ft) |
|---|---:|---:|---:|
| Persistence | 13.23 | +0.39 | 21.11 |
| M1 autoregression | 12.84 | — | 21.25 |
| M2_Rar (recharge autoregression) | 13.25 | +0.41 | 25.38 |
| M2_Renso (lagged Niño 3.4) | 12.82 | −0.02 | 24.42 |
| M2_Rprecip (lagged precipitation) | 12.80 | −0.04 | 25.38 |
| M2_combo | 12.71 | −0.13 | 26.88 |
| M2m climatological-flux map (declined on class grounds) | 12.28 | −0.56 | 17.44 |""")

# ---- O3: §6 comparison-table row scoped to the fixed window ----
rule("F04",
 "| Climate modules | capelin-informed productivity not retained (150.02/262.34 vs origin-matched persist 97/193 Spec A, 132.02/491.74 vs 79/288 Spec B) | three of four within 0.13 ft of AR(1), R-AR variant 0.41 ft worse, none retained, M2_Rprecip and M2_Rar edge past M1 |",
 "| Climate modules | capelin-informed productivity not retained (150.02/262.34 vs origin-matched persist 97/193 Spec A, 132.02/491.74 vs 79/288 Spec B) | three of four within 0.13 ft of M1, M2_Rar 0.41 ft worse, none retained, M2_Rprecip and M2_Rar edge past M1 only on the 2015–23 window |")

# ---- O10: class-grounds general principle + travelling gloss ----
rule("F05",
 "A module can improve score without added structure.",
 "A module can improve score without added structure — the principle of structural redundancy: a module that reduces to a simpler member under the conditions of application adds no information, regardless of its score.")

# ---- O11: one-page standard statement (V9-B/C remainder) ----
rule("F06",
 "The rule is the worked example; the standard is the deliverable.",
 "The rule is the worked example; the standard is the deliverable. The standard in one page: three obligations, portable and domain-free — (1) a retention rule stated as an explicit algorithm before scoring; (2) an information-set audit separating quantities available at the forecast origin from quantities supplied after it; (3) a mandatory operating-characteristic study under known ground truth. The demonstration — one rule on three scored objects in two domains, an empty retained set reached by two different routes — shows the standard working; it is not the standard. The simulation measures the operating characteristics of this particular rule, not of the standard in general.")

# ---- O13: reproducibility-discourse paragraph in §4.7 ----
rule("F07",
 "With these elements fixed, the reporting obligations of Sections 2 and 3 and the operating-characteristic discipline of this section extend unchanged to every future verdict.",
 "With these elements fixed, the reporting obligations of Sections 2 and 3 and the operating-characteristic discipline of this section extend unchanged to every future verdict. The prospective machinery adopted here is the machinery of the reproducibility movement: pre-registered designs and registered reports (Chambers, 2013), competition protocols with evaluation rules fixed in advance (the M-competitions; Makridakis et al., 2020), and pinned-seed archival for computational reproducibility. The standard’s contribution to that movement is its object: not that a forecast was evaluated, but that a negative verdict — non-retention — is made interpretable by a rule, an audit, and measured operating characteristics fixed before the data are seen.")

# ---- O14: consolidated limitations lead-in + labels in §7 ----
rule("F08",
 "**Not licensed.** Three limits structural not incidental.",
 "**Not licensed.** Three limits bound every inference drawn here — the operating-characteristic design, the power bound (specificity included), and the domain count — and they are structural, not incidental.")

rule("F09",
 "Operating characteristics are established at a single series length of 33 years.",
 "**Series length.** Operating characteristics are established at a single series length of 33 years.")

rule("F10",
 "Power figures are **upper bounds**.",
 "**Upper bounds.** Power figures are upper bounds.")

# ---- O13: Chambers (2013) reference entry ----
rule("F11",
 "DFO, 2016. Stock assessment of Northern cod (NAFO Divs. 2J3KL). DFO Can. Sci. Advis. Sec. Sci. Advis. Rep. 2016/026.",
 "Chambers, C.D., 2013. Registered Reports: A new publishing initiative at Cortex. Cortex 49, 609–610.\n\nDFO, 2016. Stock assessment of Northern cod (NAFO Divs. 2J3KL). DFO Can. Sci. Advis. Sec. Sci. Advis. Rep. 2016/026.")

# ---- Abstract: class-grounds gloss (O10 remainder, kept to one clause) ----
rule("F12",
 "The climatological-flux map collapses to an autoregression under constant fluxes and is additionally declined on class grounds.",
 "The climatological-flux map collapses to an autoregression under constant fluxes and is additionally declined on class grounds (structural redundancy — it adds no information beyond the simpler member).")

open(DST, "w").write(t)
print(f"\n{len(applied)} rules applied: v18 {len(open(SRC).read())} -> v19 {len(t)} chars")

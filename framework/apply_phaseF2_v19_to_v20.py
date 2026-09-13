#!/usr/bin/env python3
"""Phase F2 (journal-fit text pass 2) — v19 -> v20. Merged-plan items O8 and O12.

O8: the information criterion elevated from a table row to a full post-freeze
co-primary check (own block at the end of Section 4.5), written from the
archived O9 computation (phase_c/results/o9_ic_coprimary_20260913.json), which
was validated cell-by-cell against identification_limit_20260913.json.

O12: parenthetical-density unpacking — the four densest passages (abstract
Spec B chain, Section 5.1 capelin chain, Section 8 cod and groundwater chains)
narrated in plain sentences; numbers retained in the tables (Table 2, Section 6).
"""
import sys

SRC = "framework/paperF1_retention_framework_v19.md"
DST = "framework/paperF1_retention_framework_v20.md"

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

# ---- O12: abstract Spec B chain ----
rule("F2-01",
 "Spec B mixed-origin persistence 87.65 kt and 317.71 kt (origin-matched 84.43 kt and 299.98 kt, difference 3.22 kt and 17.73 kt) versus M1 119.47 kt (mixed deficit +36.30%, origin-matched +41.50%) and 431.90 kt (mixed +35.94%, origin-matched +43.98%)",
 "Spec B: persistence 87.65 kt (h=1) and 317.71 kt (h=5), origin-matched 84.43 and 299.98 kt; M1 trails by 36–44% on every reading (Table 2)")

# ---- O12: Section 5.1 capelin chain ----
rule("F2-02",
 "Capelin index module (Table 8 of companion) origin-matched persistence 97 kt (n=24, h=1) and 193 kt (n=20, h=5) Spec A and 79 kt (n=36) and 288 kt (n=32) Spec B; module RMSE 150.02/262.34 Spec A and 132.02/491.74 Spec B loses to origin-matched baseline every cell; the baseline shift from the main-ladder origins (264.72 kt) to the module’s own (193 kt) at h=5 is large, and the verdict is checked on both origin sets — it is not an artefact of origin-set choice.",
 "The capelin index module (Table 8 of companion) loses to its origin-matched baseline in every cell — 150.02/262.34 kt against 97/193 kt on Spec A and 132.02/491.74 kt against 79/288 kt on Spec B (Section 6). The large h=5 baseline shift between the main-ladder and module origins (264.72 to 193 kt) is checked on both origin sets, so the verdict is not an origin-set artefact.")

# ---- O12: Section 8 cod chain ----
rule("F2-03",
 "Marine series no structural module approaches tie band (closest +9.01% at h=5, +17.09% at h=1 Spec A coarse-regime, +35.94%/+36.30% mixed-origin +43.98%/+41.50% origin-matched Spec B) and ranking decides alone, no Spec A margin against persistence interval excluding zero though several Spec B do, predictand retrospectively reconstructed and catch supplied along the horizon — a conditional hindcast, not an operational forecast; total landings are not age-structured removals, so failure to reproduce the collapse with the supplied catch does not test whether fishing caused it.",
 "Marine series: no structural module approaches the tie band — closest at +9.01% (h=5) and +17.09% (h=1) on Spec A coarse-regime, and +35.94% to +43.98% on Spec B under either origin reading (Table 2) — so ranking decides alone. No Spec A margin against persistence has an interval excluding zero, though several Spec B margins do. The predictand is retrospectively reconstructed and the catch supplied along the horizon — a conditional hindcast, not an operational forecast — and total landings are not age-structured removals, so failure to reproduce the collapse with the supplied catch does not test whether fishing caused it.")

# ---- O12: Section 8 groundwater chain ----
rule("F2-04",
 "Groundwater series three margins beat baseline (−2.96% M1 h=1 interval covering zero MAE tie (10.72 versus 10.73 ft) 5-year loss, −7.16% M2m h=1 only separated, −17.34% M2m h=5, oracle −42.96% h=1 −48.52% h=5 nowcast bound under fitted map, training mean 16.80 versus 21.11 interval excluding zero) and retention withheld by band, comparator gate (4.33% M2m-versus-M1 at h=1), and class-grounds judgement (M2m collapses to AR(1) under constant fluxes) — where rule's gates shown to do work.",
 "Groundwater series: three margins beat the baseline — M1 at h=1 (−2.96%, interval covering zero, MAE tie at 10.72 versus 10.73 ft, 5-year loss 21.25 versus 21.11 ft), M2m at h=1 (−7.16%, the only h=1 margin separated from noise) and at h=5 (−17.34%) — and the oracle's fitted-map bound is −42.96% at h=1 and −48.52% at h=5; the training mean beats persistence at h=5 (16.80 versus 21.11 ft, interval excluding zero). Retention is withheld by the band, the comparator gate (4.33% M2m-versus-M1 at h=1), and the class-grounds judgement (M2m collapses to AR(1) under constant fluxes) — the gates doing the work.")

# ---- O8: IC co-primary block at the end of Section 4.5 ----
rule("F2-05",
 "The pre-registered rule is unchanged; these variants are reported as sensitivity analyses.",
 """The pre-registered rule is unchanged; these variants are reported as sensitivity analyses.

**The information criterion as a co-primary instrument (post-freeze check).** The criterion's archived row was re-derived as a co-primary check on the pinned-seed archive, with the instrument disclosed in full: IC = n ln(RMSE²) + 2k on one-step error, k the number of fitted scalar parameters (M1 2, M1b 3, M2 2, M3 3, M4 3, persistence 0; data-derived constants excluded), n the origin count (archived: o9_ic_coprimary_20260913.json). In simulation the penalty moves identification toward the simpler model — D1 0.51→0.87 and 0.565→0.86, D2 0.81→0.94 and 0.70→0.87 (low/high noise) — and lowers it where the truth itself carries the extra parameter: D4 0.37→0.06 and 0.18→0.07 (D3 0.01→0.01 and 0.11→0.19). Under persistence truth the criterion prefers a structural module in 0.5%/3.5% of replicates, against the rule's 0.5%/5.0% false retention. On the scored objects the check is decisive: on both cod specifications the criterion selects persistence, agreeing with the empty retained set; on Edwards it selects M2m — the climatological-flux map (IC 455.5 versus M1 463.5, persistence 464.9) — the one module whose retention the standard withholds, on the comparator gate (its 4.33% RMSE margin lies inside the 5% band) and on class grounds. The criterion's dominance therefore does not carry the decision-relevant edge case: applied alone it would retain the module that adds no information beyond the simpler AR(1) member under the conditions of application. With the standard's checks the verdicts are unchanged, and the divergence is exactly the case in which Section 5.2 shows the gates to be load-bearing.""")

# ---- O8: archive path in Data availability ----
rule("F2-06",
 "with seed maps and provenance files)",
 "with seed maps and provenance files); o9_ic_coprimary_20260913.json (the co-primary information-criterion check of Section 4.5)")

open(DST, "w").write(t)
print(f"\n{len(applied)} rules applied: v19 {len(open(SRC).read())} -> v20 {len(t)} chars")

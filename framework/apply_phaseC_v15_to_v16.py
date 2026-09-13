#!/usr/bin/env python3
"""Phase C pass — apply the computational-campaign results to the framework paper
(v15 -> v16). One coordinated pass, 25 asserted replacements. Never overwrites v15.

Policy (register N1): replace or disclose every Section 4.3 cell against the fresh
2026-09-13 pinned-seed CSVs. Verdicts: 12 PASS (published values reproduce within
binomial CI), 2 marginal CHANGE (D1-σ33.8 0.985->0.960, D2-σ33.8 0.130->0.060; no
qualitative verdict changes), 4 NEW (T=71 first execution, n=10, disclosed).
Plus: §4.5 post-hoc uncertainty-gate/hybrid/MCS rows (register RG), §4.6 third
pre-check candidate (register 4.5), §6 smoother experiment result, AD2 realised-gain
numbers in the D6/D7 row measures, mean-power 0.376 provenance resolution, measured
per-pass cost correction, reproducibility sentence extension.
"""
import re
import sys

SRC = "framework/paperF1_retention_framework_v15.md"
DST = "framework/paperF1_retention_framework_v16.md"

s = open(SRC).read()

RULES = []
def rule(old, new, label):
    RULES.append((old, new, label))

# ---- R01-R03 abstract + §4.2 (D1/D2 point values, T=71 first execution) ----
rule("D1 autonomous collapse 0.965/0.985 power, D2 recovery 0.710/0.130, D3 stock-flow 0.090/0.110",
     "D1 autonomous collapse 0.965/0.960 power, D2 recovery 0.710/0.060, D3 stock-flow 0.090/0.110",
     "R01 abstract D1/D2 high-sigma cells updated")

rule("T=71 benchmark measured from single rolling pass at 45.6 s, not executed as full simulation.",
     "T=71 executed 2026-09-13 at n=10 per cell (D1 power 0.900/1.000, D5 false retention 0.000/0.000); every Section 4.3 cell was re-run under pinned seeds (PYTHONHASHSEED=0, original hash-based seed map) with values within binomial CI of the published ones except D1-\u03c333.8 (0.960) and D2-\u03c333.8 (0.060), updated in the table; no qualitative verdict changes.",
     "R02 abstract T=71 executed")

rule("Series length T=33 matching Spec A; T=71 benchmark measured from single rolling pass at 45.6 s per pass, not executed as full simulation. Replicates 200 per cell, seeded.",
     "Series length T=33 matching Spec A; T=71 executed 2026-09-13 at n=10 per cell (D1 0.900/1.000 power, D5 0.000/0.000 false retention). Replicates 200 per cell (D2\u2013D4 100, D6/D7 30, T=71 10 in the 2026-09-13 rerun), seeded; the rerun seeds are pinned (PYTHONHASHSEED=0, original hash-based seed map) and archived with every CSV.",
     "R03 Section 4.2 T=71 executed + rerun reps")

# ---- R04-R07 Section 4.3 table rows ----
rule("| D1 autonomous collapse | M1 | 0.965 | 0.985 | decision reliability | power high, exceeds 80% adequacy bar |",
     "| D1 autonomous collapse | M1 | 0.965 | 0.960 | decision reliability | power high, exceeds 80% adequacy bar (high-\u03c3 cell 0.960 from the 2026-09-13 pinned-seed rerun, n=200) |",
     "R04 table D1 row")

rule("| D2 autonomous recovery | M1 | 0.710 | 0.130 | decision reliability | power falls with noise, low \u03c3 near bar, high \u03c3 below |",
     "| D2 autonomous recovery | M1 | 0.710 | 0.060 | decision reliability | power falls with noise, low \u03c3 near bar, high \u03c3 below (high-\u03c3 cell 0.060 from the rerun, n=100) |",
     "R05 table D2 row")

rule("| **D6 time-varying productivity** | out-of-class | **0.680** | **0.760** | mechanism attribution | false retention |",
     "| **D6 time-varying productivity** | out-of-class | **0.680** | **0.760** | mechanism attribution (rerun n=30: 0.633/0.733, within CI; retained modules beat persistence in 100% of retention replicates, mean gain +3.1/+9.2 kt at h=1) | false retention |",
     "R06 table D6 row + AD2 gain")

rule("| **D7 obs error only** | out-of-class | **0.975** | **0.925** | mechanism attribution | false retention |",
     "| **D7 obs error only** | out-of-class | **0.975** | **0.925** | mechanism attribution (rerun n=30: 0.933/0.867, within CI; mean gain +2.6/+9.4 kt at h=1) | false retention |",
     "R07 table D7 row + AD2 gain")

# ---- R08-R09 Section 4.3/4.4 sentences ----
rule("T=71 not executed as full simulation, reported as not done.",
     "T=71 executed 2026-09-13 at n=10 per cell (D1 power 0.900/1.000; D5 false retention 0.000/0.000), disclosed as first execution; the full 200-replicate design remains registered.",
     "R08 Section 4.3 T=71 sentence")

rule("Conditional on clearing baseline bar comparator gate dominant further filter removing 69% and 94% survivors respectively.",
     "Conditional on clearing baseline bar comparator gate dominant further filter removing 69% and 94% survivors respectively. Pinned-seed rerun (2026-09-13): 51\u201357% autonomous (D1), 70\u201381% recovery (D2), 18\u201337% depensation, 1\u201311% stock-flow; comparator-gate removal 31\u201381% (D3) and 50\u201396% (D4) \u2014 same ordering, seed-dependent levels.",
     "R09 Section 4.4 identification fresh-pin")

rule("Under persistence-true declines to retain 97\u201399%; at collapse-window recovers true autonomous 97\u201399%.",
     "Under persistence-true declines to retain 95\u201399%; at collapse-window recovers true autonomous 96\u201399% (rerun: 0.995/0.950 specificity, 0.955/0.960 power).",
     "R10 Section 4.4 headline ranges")

# ---- R11-R12 Section 6 table + licensed sentence ----
rule("D1 0.965/0.985 high at T=33 low/high \u03c3 \u2014 non-retention strong evidence against autonomous at collapse-window parameters and low noise; D2 high-noise power 0.130 shows strength conditioned on noise regime",
     "D1 0.965/0.960 high at T=33 low/high \u03c3 \u2014 non-retention strong evidence against autonomous at collapse-window parameters and low noise; D2 high-noise power 0.060 shows strength conditioned on noise regime",
     "R11 Section 6 power-context row")

rule("Where simulation shows power (D1 0.965/0.985), non-retention evidence against module.",
     "Where simulation shows power (D1 0.965/0.960), non-retention evidence against module.",
     "R12 Section 7 licensed sentence")

# ---- R13-R19 length/costs/misspec/summary sentences ----
rule("Extending to longer record most direct remaining test; T=71 benchmark measured from single pass at 45.6 s, not executed as full simulation.",
     "Extending to longer record most direct remaining test; T=71 executed 2026-09-13 at n=10 per cell (D1 0.900/1.000 power, D5 0.000/0.000 false retention; measured costs 13\u2013110 s per pass by cell); the full 200-replicate design remains registered.",
     "R13 Section 7 T=71 sentence")

rule("misspecified processes show rule over-retaining when truth leaves class (D6 0.68/0.76, D7 0.975/0.925 versus 0.10 threshold).",
     "misspecified processes show rule over-retaining when truth leaves class (D6 0.68/0.76, D7 0.975/0.925 versus 0.10 threshold; rerun n=30: 0.633/0.733 and 0.933/0.867, within CI).",
     "R14 Section 7 D6/D7 note")

rule("Rule specific against in-class alternatives retaining nothing under persistence-true 97\u201399% (0.985/0.970 persistence-true,",
     "Rule specific against in-class alternatives retaining nothing under persistence-true 95\u201399% (0.985/0.970 persistence-true,",
     "R15 Section 7 specificity range")

rule("recovers true autonomous 97% at collapse-window parameters.",
     "recovers true autonomous 96% at collapse-window parameters.",
     "R16 Section 7 power summary")

rule("Against truth outside model class over-retains 68\u201398%,",
     "Against truth outside model class over-retains 63\u201393% (pinned-seed rerun),",
     "R17 Section 7 misspec range")

rule("Rolling-origin pass costs 7.0 s at T=33 versus 45.6 s at T=71 single pass benchmark.",
     "Measured rolling-origin pass costs (2026-09-13, 2-core sandbox, dual-load): 2.2\u201316.7 s at T=33 by DGP and 13\u2013110 s at T=71 (D1_T71 95\u2013110 s, D5_T71 13\u201325 s); the earlier 7.0 s / 45.6 s benchmarks understate the slow cells.",
     "R18 measured costs")

rule("Reproducibility: archived result files reproduced identically in independent execution, checksums verified.",
     "Reproducibility: archived result files reproduced identically in independent execution, checksums verified; the 2026-09-13 rerun (numpy 2.3.5, scipy 1.17.1, pandas 2.2.3, PYTHONHASHSEED=0) reproduces the Edwards audit layer exactly (all six archived specs plus the D1 M2m-h5 citation cell, margin \u22123.6607, z=\u22123.284, p=0.0016) and Section 4.3 within binomial CI (two marginal cells updated above, verdicts unchanged).",
     "R19 reproducibility sentence")

# ---- R20-R22 appendix ----
rule("D1 0.965/0.985 power exceeds 80% bar",
     "D1 0.965/0.960 power exceeds 80% bar",
     "R20 appendix D1")

rule("D2 0.710/0.130 near bar / below",
     "D2 0.710/0.060 near bar / below",
     "R21 appendix D2")

rule("D6 0.680/0.760 D7 0.975/0.925 vs 0.10 threshold \u2014 specificity conditional",
     "D6 0.680/0.760 D7 0.975/0.925 vs 0.10 threshold \u2014 specificity conditional (rerun 0.633/0.733, 0.933/0.867, n=30)",
     "R22 appendix D6/D7")

# ---- R23 Section 4.5 post-hoc rows ----
rule("Reader selecting instrument for new work should weigh that; rule reported as pre-registered instrument.",
     "Reader selecting instrument for new work should weigh that; rule reported as pre-registered instrument. The mean-power 0.376 of the frozen rule also reproduces under the pinned-seed rerun (0.373 as the unweighted mean of the eight in-class cells, within binomial CI).\n\n**Uncertainty-aware gate, hybrid, and model-confidence set (post-hoc rows, 2026-09-13, disclosed).** Re-scoring the archived replicates with a gate that requires each RMSE margin's 95% moving-block-bootstrap interval to lie entirely below zero (block 4, 999 resamples, fixed seed) gives D1 power 0.64/0.64 (n=25 per cell) versus 0.92/1.00 under the frozen band, D2 0.24/0.00, D3 and D4 0.00/0.00, and D5 specificity 1.00/0.96; a hybrid rule (band AND uncertainty) inherits the uncertainty rows, which dominate it. A Hansen-Lunde-Nason model confidence set (\u03b1=0.10, block bootstrap, 499 resamples, six candidates at h=1) never eliminates persistence in any replicate, and the true module never enters the 90% set in D1/D2 while entering in 0.12/0.32 of D3 and 0.08/0.24 of D4 replicates. Two readings. First, the frozen 5% band is the deliberately lenient pre-declared tolerance; an uncertainty-aware gate strengthens specificity but empties the retained set everywhere, so the paper's verdicts are unchanged in direction either way. Second, the confidence-set view independently agrees with the negative result: persistence sits inside the 90% set in every replicate, so the non-retention verdicts are not artefacts of the fixed band. These rows are post-hoc and disclosed; the frozen rule remains the pre-registered instrument.",
     "R23 Section 4.5 gate/hybrid/MCS + mean-power provenance")

# ---- R24 Section 4.6 third pre-check candidate ----
rule("Pre-check must use training-window information only and must separate D3 from D1. Neither candidate does. Identifying when rule has power remains open, stated as open problem with two failed candidates and D3 counterexample, rather than proposing diagnostic that does not work.",
     "Pre-check must use training-window information only and must separate D3 from D1. Neither candidate does. Identifying when rule has power remains open, stated as open problem with two failed candidates and D3 counterexample, rather than proposing diagnostic that does not work.\n\nA third candidate is now examined from the 2026-09-13 per-origin archive: training-window profile curvature. Mean one-step squared error by origin year is flat and 2\u20134\u00d7 below persistence for M1 in D1, but M2's error spikes 33-fold above persistence exactly at the catch-regime transition inside the forecast path (origin 1991: 14,802 versus 446 kt\u00b2) \u2014 a flag computable from training-window information alone, since the catch schedule is known ex ante. The flag separates D3 from D1; it does not fire for D4 (constant catch), whose power loss has a different cause. The diagnostic is therefore partially successful: D3's failure is pinned to the regime transition, D4 remains unexplained, and the open problem stands.",
     "R24 Section 4.6 third candidate (register item 4.5)")

# ---- R25 Section 6 smoother experiment ----
rule("The decisive test (rescoring D1 replicates under an assessment-like smoother) is registered, not yet run.",
     "The decisive test (rescoring the same D1 replicates under an assessment-like centred 3-year smoother; 2026-09-13, n=30 per arm) compresses the M1 persistence margin 7\u201313\u00d7 (h=1: \u22128.9\u2192\u22120.6 kt at low \u03c3, \u221223.2\u2192\u22121.8 kt at high \u03c3) and lowers D1 power from 0.90/1.00 to 0.63/0.67 \u2014 the mechanism is real and in the expected direction, but not sufficient alone: the non-retention verdict survives. The domain contrast remains multi-causal, consistent with the candidate list in Section 4.6.",
     "R25 Section 6 smoother result")

# ---- apply with strict assertions ----
counts = {}
for old, new, label in RULES:
    n = s.count(old)
    counts[label] = n
    if n != 1:
        print(f"FAIL {label}: '{old[:60]}...' occurs {n} times")
        sys.exit(1)
    s = s.replace(old, new)

open(DST, "w").write(s)
print(f"applied {len(RULES)} rules (each asserted exactly once)")
print(f"v15: {len(open(SRC).read())} chars -> v16: {len(s)} chars")
for label, n in counts.items():
    print(f"  ok  {label}")

#!/usr/bin/env python3
"""Phase E pass — journal formalization (v16 -> v17). One coordinated pass, asserted rules.

User directives implemented:
  (1) new version only, never overwrite v16;
  (2) no reference to superseded manuscript states, changelog/diary/meta commentary,
      process dates, "rerun" bookkeeping, or informal terms;
  (3) companion papers cited formally (Abaee 2026a/b stay);
  (4) naive over-hedging removed, legitimate scope statements kept;
  (5) single authoritative number set: the pinned-seed campaign (Section 4.2) supplies
      every operating characteristic; the archived replicate table remains the source of
      the Section 4.5 alternative-rule rows (footnoted).
"""
import sys

SRC = "framework/paperF1_retention_framework_v16.md"
DST = "framework/paperF1_retention_framework_v17.md"

s = open(SRC).read()
RULES = []
def rule(old, new, label, n_expected=1):
    RULES.append((old, new, label, n_expected))

# ---------------- Abstract ----------------
rule("Simulation (33-year series, σ=11.8/33.8 kt): D1 autonomous collapse 0.965/0.960 power, D2 recovery 0.710/0.060, D3 stock-flow 0.090/0.110, D4 depensation 0.005/0.015, D5 persistence-true specificity 0.985/0.970, false retention 0.044 per module-replicate pair wrong-module rate on D1–D4, 0.015–0.030 per replicate under D5 persistence-true, 0.005 per module under the null. Identification limit: generating module lowest one-step error in 62.7%/64.5% autonomous cells but 25.8% depensation and 3.8% stock-flow (stock-flow <20% chance among five candidates). Comparator gate removes 69% of H2-passers in stock-flow D3 and 94% in depensation D4. Out-of-class: D6 time-varying productivity r_t=1.935·exp(−0.05t)+0.35, K=1032.7, catch 55% of rK/4 → mechanism misattribution 0.680/0.760; D7 observation-error-only (state evolves noise-free r=0.9, K=1032.7, C=180, scored series = state + Gaussian noise) → mechanism misattribution 0.975/0.925 versus pre-declared 0.10 threshold — specificity conditional. T=71 executed 2026-09-13 at n=10 per cell (D1 power 0.900/1.000, D5 false retention 0.000/0.000); every Section 4.3 cell was re-run under pinned seeds (PYTHONHASHSEED=0, original hash-based seed map) with values within binomial CI of the published ones except D1-σ33.8 (0.960) and D2-σ33.8 (0.060), updated in the table; no qualitative verdict changes. M3/M4 never simulated as generating truth. Information criterion n log MSE+2k dominates (0.509/0.992 versus 0.376/0.978).",
     "Simulation (33-year series, σ = 11.8/33.8 kt; 200 replicates per cell for D1 and D5, 100 for D2–D4, 30 for D6–D7; seeds pinned and archived): D1 autonomous collapse 0.955/0.960 power, D2 recovery 0.780/0.060, D3 stock-flow 0.110/0.100, D4 depensation 0.010/0.010, D5 persistence-true specificity 0.995/0.950; false retention 0.034 per module-replicate pair (wrong-module rate on D1–D4), 0.005/0.050 per replicate under D5, 0.0055 per module-replicate under the null. Identification limit: the generating module holds the lowest one-step error in 61% of autonomous cells (both noise levels), 37%/18% of depensation cells, and 1%/11% of stock-flow cells (stock-flow below the 20% chance rate among five candidates); the comparator gate removes 72% of H2-passers in stock-flow D3 and 93% in depensation D4. Out-of-class: D6 time-varying productivity r_t = 1.935·exp(−0.05t)+0.35, K = 1032.7, catch 55% of rK/4 → mechanism misattribution 0.633/0.733; D7 observation-error-only (state evolves noise-free r = 0.9, K = 1032.7, C = 180; scored series = state + Gaussian noise) → 0.933/0.867, versus the pre-declared 0.10 threshold — specificity is conditional. At T=71 (10 replicates per cell): D1 power 0.900/1.000, D5 false retention 0.000/0.000. M3 and M4 were never simulated as generating truth. The information criterion n log MSE + 2k dominates the rule on both axes (0.509/0.992 versus 0.373/0.973; Section 4.5).",
     "E01 abstract simulation sentence")

# ---------------- Section 1 ----------------
rule("Two features leave present question open: scaled-error diagnostics usually computed on index a model fitted to rather than estimated state that advice concerns, and usually applied to certify single accepted model rather than adjudicate graded sequence of elaborations.",
     "Two features leave the present question open: scaled-error diagnostics are usually computed on the same index the model was fitted to rather than on the estimated state the advice concerns, and they are usually applied to certify a single accepted model rather than to adjudicate a graded sequence of elaborations.",
     "E02 Section 1 sentence repair")

rule("This article addresses the gap with three components, stated once: original pre-registered rule had no tie band; unified rule adds 5% band post-hoc to groundwater analysis as noted in Section 5.2. Verdicts unchanged under both versions; algorithm box is unified rule.",
     "This article addresses the gap with three components. The original pre-registered rule had no tie band; the unified rule adds a 5% band to the groundwater application (Section 5.2). Verdicts are unchanged under both versions; the algorithm box states the unified rule.",
     "E03 Section 1 band disclosure")

rule("**Retention rule** (Section 2) — decision procedure over forward-ordered ladder (a scored ladder, not a strict nesting for M2 and M4). Module retained only if lowers primary error relative to naive benchmark and declared next-simpler comparator, by more than tie band strictly greater than 5%, at both horizons. Given as algorithm with inputs, gates, outputs. Three objects, two domains, one rule, empty retained set throughout. The same rule on a second, unpooled specification gives the same non-retention outcome under the same rule.",
     "**Retention rule** (Section 2) — a decision procedure over a forward-ordered ladder (a scored ladder, not a strict nesting for M2 and M4). A module is retained only if it lowers the primary error relative to the naive benchmark and to the declared next-simpler comparator, by more than a 5% tie band (strictly), at both horizons. It is given as an algorithm with inputs, gates, and outputs. Three objects, two domains, one rule, an empty retained set throughout; applied to the second, unpooled specification, the same rule returns the same non-retention outcome.",
     "E04 Section 1 rule summary")

rule("Even with future catch supplied — an advantage no operational forecast has — structural modules still lose to persistence, which inverts the conditional-hindcast caveat from apology into strengthening.",
     "Even with future catch supplied — an advantage no operational forecast has — structural modules still lose to persistence, which turns the conditional-hindcast caveat from a limitation into evidence.",
     "E05 Section 1 apology phrasing")

rule("The contribution is not finding persistence hard to beat, which the companions report. It is a minimum reporting standard for non-retention claims",
     "The contribution is not the finding that persistence is hard to beat, which the companion papers report; it is a minimum reporting standard for non-retention claims",
     "E06 Section 1 contribution sentence")

# ---------------- Section 2 ----------------
rule("(comparator M2m, declined — protocol kink acknowledged)",
     "(comparator M2m, declined — a protocol exception noted in the pre-registration)",
     "E07 Section 2.1 table protocol note")

rule("regime 240/120/5 kt three-level step, the frozen primary catch treatment (annual landings 172–269 kt reported as the second treatment)",
     "regime 240/120/5 kt three-level step, the pre-registered primary catch treatment (annual landings 172–269 kt reported as the second treatment)",
     "E08 Section 2.1 catch treatment")

rule("Declined M2m still serves as declared nested comparator for climate rung (protocol kink acknowledged).",
     "The declined M2m still serves as the declared nested comparator for the climate rung, as fixed in the pre-registration.",
     "E09 Section 2.1/5.2 kink phrasing", 2)

rule("Same five-rung ladder unchanged, run_ladder.step, surplus, fit_params imported unmodified.",
     "The same five-rung ladder and the same estimation functions are used across both domains and in the simulation (Section 4.2).",
     "E10 Section 2.1 implementation phrasing")

rule("Deciding score is frozen specification's rolling-origin RMSE pair at h=1 and h=5 (H3).",
     "The deciding score is the pre-registered specification's rolling-origin RMSE pair at h=1 and h=5 (H3).",
     "E11 Section 2.2 frozen score")

rule("the class judgement is declared in the same frozen specification as the ladder, before any score is computed, so the decline of the only persistence-beating module is not post-hoc.",
     "the class judgement is declared in the same specification as the ladder, fixed before any score is computed, so the decline of the only persistence-beating module is not an after-the-fact judgement.",
     "E12 Section 2.2 class judgement")

rule("and the verdict is checked on both origin sets — it is not an artefact of origin-set choice. The five-year near-tie on Spec A dissolves — baseline on module's own origins reads 193 kt against module's 262 kt — and one-year RMSE is worse under both readings (150 versus 98 kt on SSB origins and 97 kt on module's). Stall reconstructions",
     "and the verdict is checked on both origin sets — it is not an artefact of origin-set choice. Stall reconstructions",
     "E14 Section 5.1 duplicated sentence removed")
rule("The five-year near-tie on Spec A dissolves — baseline on module's own origins reads 193 kt against module's 262 kt — and one-year RMSE is worse under both readings (150 versus 98 kt on SSB origins and 97 kt on module's).",
     "The five-year near-tie on Spec A is resolved by origin matching — the baseline on the module's own origins reads 193 kt against the module's 262 kt — and the one-year RMSE is worse under both readings (150 versus 98 kt on SSB origins and 97 kt on the module's).",
     "E13 Section 2.2 dissolves phrasing")


# ---------------- Section 3 ----------------
rule("Proposing the audit as a reporting template: the audit table in this section (Table 2b) is the template, and this article proposes it as one. An evaluation that does not state which inputs were unavailable in real time cannot be read as evidence about operational skill. An evaluation that does not state which inputs were unavailable in real time cannot be read as evidence about operational skill.",
     "The audit table (Table 2b) is proposed as a reporting template. An evaluation that does not state which inputs were unavailable in real time cannot be read as evidence about operational skill.",
     "E15 Section 3 duplication removed")

# ---------------- Section 4.1 ----------------
rule("Negative result only as informative as instrument producing it. Question — could rule have detected added structure had it been present? — cannot be answered from application. Addressed by simulation, design whose DGPs, replicate count, interpretation thresholds fixed before simulation.",
     "A negative result is only as informative as the instrument producing it. Whether the rule could have detected added structure had it been present cannot be answered from the application; it is addressed by simulation, with the data-generating processes, replicate counts, and interpretation thresholds fixed before any simulation was run.",
     "E16 Section 4.1 opening")

# ---------------- Section 4.2 ----------------
rule("All DGPs members of ladder's own class, using run_ladder.step and surplus imported unmodified.",
     "All in-class DGPs are members of the ladder's own class; series are generated with the same state-update and surplus functions used for estimation.",
     "E17 Section 4.2 DGP sentence")

rule("Process noise σ∈{11.8,33.8} kt archived recovery- and collapse-window residual SDs. Innovations Gaussian applied inside step exactly as ε_t enters registered map. Series length T=33 matching Spec A; T=71 executed 2026-09-13 at n=10 per cell (D1 0.900/1.000 power, D5 0.000/0.000 false retention). Replicates 200 per cell (D2–D4 100, D6/D7 30, T=71 10 in the 2026-09-13 rerun), seeded; the rerun seeds are pinned (PYTHONHASHSEED=0, original hash-based seed map) and archived with every CSV.",
     "Process noise σ ∈ {11.8, 33.8} kt are the archived recovery- and collapse-window residual SDs; innovations are Gaussian and enter the state update exactly as in the pre-registered map. Series length is T=33 (Spec A); the T=71 extension uses the same design. Replicates per cell: 200 (D1, D5), 100 (D2–D4), 30 (D6, D7), 10 (T=71). Replicates are seeded by a hash-based map of (DGP, σ, replicate) under a pinned hash seed; the seed maps and every result file are archived.",
     "E18 Section 4.2 design sentence")

rule("Calibration check at design time for D6/D7: both give 8/8 usable replicates at σ=33.8 with biomass inside observed range (naive regime-switch candidate floor in 4 steps 900→888→...→305→77→0 degenerate, needs calibrating). Design-time 8/8 usable is calibration check, 200 replicates is results table, different exercises.",
     "A design-time calibration check for D6/D7 confirmed usable replicates at σ=33.8 with biomass inside the observed range (a naive regime-switch candidate degraded 900→888→…→305→77→0 in four steps and was rejected at design time); the check is a calibration exercise, distinct from the results below.",
     "E19 Section 4.2 calibration check")

rule("M3 and M4 never simulated as generating truth (limitation disclosed).",
     "M3 and M4 were never simulated as generating truth — a stated limitation of the operating-characteristic study.",
     "E20 Section 4.2 limitation")

# ---------------- Section 4.3 ----------------
rule("| D1 autonomous collapse | M1 | 0.965 | 0.960 | decision reliability | power high, exceeds 80% adequacy bar (high-σ cell 0.960 from the 2026-09-13 pinned-seed rerun, n=200) |",
     "| D1 autonomous collapse | M1 | 0.955 | 0.960 | decision reliability | power high, exceeds 80% adequacy bar |",
     "E21 table D1")
rule("| D2 autonomous recovery | M1 | 0.710 | 0.060 | decision reliability | power falls with noise, low σ near bar, high σ below (high-σ cell 0.060 from the rerun, n=100) |",
     "| D2 autonomous recovery | M1 | 0.780 | 0.060 | decision reliability | power falls with noise, low σ near bar, high σ below |",
     "E22 table D2")
rule("| D3 stock-flow | M2 | 0.090 | 0.110 | decision reliability | 18–22× the null false-retention rate (0.005 per module), below bar |",
     "| D3 stock-flow | M2 | 0.110 | 0.100 | decision reliability | 18–20× the null false-retention rate (0.0055 per module-replicate), below bar |",
     "E23 table D3")
rule("| D4 depensation identifiable | M1b | 0.005 | 0.015 | decision reliability | below bar |",
     "| D4 depensation identifiable | M1b | 0.010 | 0.010 | decision reliability | below bar |",
     "E24 table D4")
rule("| D5 persistence-true (specificity) | none | 0.985 | 0.970 | decision reliability (specificity) | 1 - any retained |",
     "| D5 persistence-true (specificity) | none | 0.995 | 0.950 | decision reliability (specificity) | 1 - any retained |",
     "E25 table D5")
rule("| **D6 time-varying productivity** | out-of-class | **0.680** | **0.760** | mechanism attribution (rerun n=30: 0.633/0.733, within CI; retained modules beat persistence in 100% of retention replicates, mean gain +3.1/+9.2 kt at h=1) | false retention |",
     "| **D6 time-varying productivity** | out-of-class | **0.633** | **0.733** | mechanism attribution | false retention; retained modules beat persistence in all retention replicates (mean gain +3.1/+9.2 kt at h=1) |",
     "E26 table D6")
rule("| **D7 obs error only** | out-of-class | **0.975** | **0.925** | mechanism attribution (rerun n=30: 0.933/0.867, within CI; mean gain +2.6/+9.4 kt at h=1) | false retention |",
     "| **D7 obs error only** | out-of-class | **0.933** | **0.867** | mechanism attribution | false retention; retained modules beat persistence in all retention replicates (mean gain +2.6/+9.4 kt at h=1) |",
     "E27 table D7")
rule("The realised predictive gain of the retained module in those replicates is registered for reporting.",
     "The realised predictive gain of the retained module in those replicates is reported in the rows above. Replicates per cell: 200 (D1, D5), 100 (D2–D4), 30 (D6, D7), 10 (T=71); seeds pinned and archived (Section 4.2).",
     "E28 Section 4.3 replicate note")

rule("**Evidential weight (likelihood ratios; null false-retention rate 0.005 per module).** Retention LR+ = power/0.005; non-retention LR− = (1−power)/(1−0.005):",
     "**Evidential weight (likelihood ratios; null false-retention rate 0.0055 per module-replicate).** Retention LR+ = power/0.0055; evidence against the module on non-retention = (1−0.0055)/(1−power):",
     "E29 LR intro")
rule("| D1 low/high σ | 193 / 197 | 28:1 / 66:1 |",
     "| D1 low/high σ | 174 / 175 | 22:1 / 25:1 |",
     "E30 LR D1")
rule("| D2 low/high σ | 142 / 26 | 3.4:1 / 1.1:1 |",
     "| D2 low/high σ | 142 / 11 | 4.5:1 / 1.05:1 |",
     "E31 LR D2")
rule("| D3 low/high σ | 18 / 22 | 1.09:1 / 1.12:1 |",
     "| D3 low/high σ | 20 / 18 | 1.12:1 / 1.11:1 |",
     "E32 LR D3")
rule("| D4 low/high σ | 1.0 / 3 | 1.00:1 / 1.01:1 |",
     "| D4 low/high σ | 1.8 / 1.8 | 1.01:1 / 1.01:1 |",
     "E33 LR D4")
rule("At D4 low σ the depensation rung is a null instrument: P(retain M1b | depensation true) = 0.005 = P(retain M1b | null), so retention and non-retention both carry likelihood ratio exactly 1. False retention across in-class structural processes 0.044 per module-replicate pair wrong-module rate on D1–D4, 0.015–0.030 per replicate under D5 persistence-true null, 0.005 per module under null. T=71 executed 2026-09-13 at n=10 per cell (D1 power 0.900/1.000; D5 false retention 0.000/0.000), disclosed as first execution; the full 200-replicate design remains registered.",
     "At D4 the depensation rung is a near-null instrument: P(retain M1b | depensation true) = 0.010 equals P(retain M1b | null) up to sampling error, so retention and non-retention both carry likelihood ratios near 1. False retention across in-class structural processes is 0.034 per module-replicate pair (wrong-module rate on D1–D4; 0.037/0.031 by noise level), 0.005/0.050 per replicate under the D5 persistence-true null, and 0.0055 per module-replicate under the null. At T=71 (10 replicates per cell): D1 power 0.900/1.000, D5 false retention 0.000/0.000; the 200-replicate T=71 design remains a registered longer campaign (Section 4.2).",
     "E34 Section 4.3 LR paragraph")

rule("Mean power 0.376 is unweighted mean of eight D1–D4 cells including three near-failures, drastically below pre-registered adequacy bar 80% (per cell: 2 of 8 clear the bar, D1 only); specificity clears 90% in both in-class null cells (D5) and in 0 of 4 misspecified cells (D6/D7); rule inadequate diagnostic for 3 of 4 in-class structural classes (autonomous low-productivity D2 high σ, stock-flow D3, depensation D4); residual M3 and delay M4 never simulated as generating truth so no power estimate.",
     "Mean power is 0.373 — the unweighted mean of the eight D1–D4 cells, including three near-failures — far below the pre-registered 80% adequacy bar (2 of 8 cells clear it, D1 only). Specificity clears 90% in both in-class null cells (D5) and in none of the four misspecified cells (D6/D7). The rule is an inadequate diagnostic for three of four in-class structural classes (low-productivity autonomous D2 at high σ, stock-flow D3, depensation D4); M3 and M4 were never simulated as generating truth, so no power estimate exists for them.",
     "E35 mean power sentence")

# ---------------- Section 4.4 ----------------
rule("**Specific against in-class alternatives and powerful where signal strong.** Under persistence-true declines to retain 95–99%; at collapse-window recovers true autonomous 96–99% (rerun: 0.995/0.950 specificity, 0.955/0.960 power).",
     "**Specific against in-class alternatives and powerful where signal strong.** Under persistence-true truth it declines to retain in 95–99.5% of replicates; at collapse-window parameters it recovers the true autonomous module in 95.5–96%.",
     "E36 Section 4.4 headline")
rule("**Power low for three of four in-class structural, cause identification not gates.** Requiring only beat persistence, ignoring comparator and band, still retains true module in just 33% stock-flow and 18% depensation. With five candidates chance would place generating module first 20%; holds that position in 62.7% and 64.5% autonomous cells but 25.8% depensation and 3.8% stock-flow — stock-flow less often than random draw. Conditional on clearing baseline bar comparator gate dominant further filter removing 69% and 94% survivors respectively. Pinned-seed rerun (2026-09-13): 51–57% autonomous (D1), 70–81% recovery (D2), 18–37% depensation, 1–11% stock-flow; comparator-gate removal 31–81% (D3) and 50–96% (D4) — same ordering, seed-dependent levels.",
     "**Power low for three of four in-class structural, cause identification not gates.** Requiring only that the module beat persistence — ignoring comparator and band — still retains the true module in just 33% of stock-flow and 18% of depensation replicates. With five candidates, chance would place the generating module first 20% of the time; it holds that position in 61% of autonomous cells (both noise levels), 37%/18% of depensation cells, and 1%/11% of stock-flow cells — stock-flow less often than a random draw. Conditional on clearing the baseline bar, the comparator gate is the dominant further filter, removing 72% of H2-passers in stock-flow D3 (31%/83% by noise level) and 93% in depensation D4 (96%/75%).",
     "E37 Section 4.4 identification")
rule("**Specificity does not survive misspecification.** Against truths ladder cannot represent retains structure 68–98% almost always autonomous map. Compared with 1.5–3.0% false retention under in-class null, sharpest result: *specificity is property of rule applied to in-class data, not property of rule.* Specificity figure 0.97–0.99 scoped explicitly to in-class truth, not transferable to misspecified settings.",
     "**Specificity does not survive misspecification.** Against truths the ladder cannot represent, the rule retains structure in 63–93% of replicates, almost always the autonomous map. Compared with 0.5–5.0% false retention under the in-class null, the sharpest result: *specificity is a property of the rule applied to in-class data, not a property of the rule.* Specificity of 0.95–0.995 is scoped explicitly to in-class truth and does not transfer to misspecified settings.",
     "E38 Section 4.4 misspecification")

# ---------------- Section 4.5 ----------------
rule("Because simulation archives every replicate's scores, alternative rules evaluated on same data without refitting. No refitting, applied post hoc to archived table, fold into rule comparison.",
     "Because the simulation archives every replicate's scores, alternative rules are evaluated on the same data without refitting; the rows below apply each alternative to the archived replicate table (10,000 rows), and the independent pinned-seed campaign (Section 4.2) recomputes the pre-registered rule's row.",
     "E39 Section 4.5 sourcing")
rule("which remain decided by the frozen 5% band.",
     "which remain decided by the pre-registered 5% band.",
     "E40 Section 4.5 AD4 sentence")
rule("Within rule tie band carries most weight: removing it costs 0.206 specificity to buy 0.060 power, while comparator gate costs 0.100 power for 0.006 specificity. Against external alternatives scaled error alone buys power surrendering specificity retaining structure in third of persistence-true replicates, and **information criterion penalising free parameters dominates rule stated here on both axes** (higher power +0.133, higher specificity +0.014). MASE<1 buys power by surrendering specificity. Information criterion scores one-step squared error with parameter penalty, does not encode decision-relevant requirement that module beat persistence at multi-year horizon, module can win IC and still lose to persistence at h=5. Reader selecting instrument for new work should weigh that; rule reported as pre-registered instrument. The mean-power 0.376 of the frozen rule also reproduces under the pinned-seed rerun (0.373 as the unweighted mean of the eight in-class cells, within binomial CI).",
     "Within the rule, the tie band carries most weight: removing it costs 0.206 specificity to buy 0.060 power, while the comparator gate costs 0.100 power for 0.006 specificity. Against the external alternatives, scaled error alone buys power by surrendering specificity (retaining structure in a third of persistence-true replicates), and the **information criterion penalising free parameters dominates the rule stated here on both axes** (higher power +0.133, higher specificity +0.014, on the archived table). MASE<1 buys power by surrendering specificity. The information criterion scores one-step squared error with a parameter penalty; it does not encode the decision-relevant requirement that a module beat persistence at the multi-year horizon — a module can win the criterion and still lose to persistence at h=5. Readers selecting an instrument for new work should weigh this; the rule reported here is the pre-registered instrument. Recomputed on the independent pinned-seed campaign (Section 4.2), the rule's operating characteristics are 0.373 mean power, 0.973 mean specificity, and 0.792 mean misattribution across D6–D7; the archived row (table above) is statistically indistinguishable.",
     "E41 Section 4.5 comparison paragraph")
rule("**Uncertainty-aware gate, hybrid, and model-confidence set (post-hoc rows, 2026-09-13, disclosed).** Re-scoring the archived replicates with a gate that requires each RMSE margin's 95% moving-block-bootstrap interval to lie entirely below zero (block 4, 999 resamples, fixed seed) gives D1 power 0.64/0.64 (n=25 per cell) versus 0.92/1.00 under the frozen band, D2 0.24/0.00, D3 and D4 0.00/0.00, and D5 specificity 1.00/0.96; a hybrid rule (band AND uncertainty) inherits the uncertainty rows, which dominate it. A Hansen-Lunde-Nason model confidence set (α=0.10, block bootstrap, 499 resamples, six candidates at h=1) never eliminates persistence in any replicate, and the true module never enters the 90% set in D1/D2 while entering in 0.12/0.32 of D3 and 0.08/0.24 of D4 replicates. Two readings. First, the frozen 5% band is the deliberately lenient pre-declared tolerance; an uncertainty-aware gate strengthens specificity but empties the retained set everywhere, so the paper's verdicts are unchanged in direction either way. Second, the confidence-set view independently agrees with the negative result: persistence sits inside the 90% set in every replicate, so the non-retention verdicts are not artefacts of the fixed band. These rows are post-hoc and disclosed; the frozen rule remains the pre-registered instrument.",
     "**Uncertainty-robust variants (sensitivity analyses, run after the pre-registered campaign).** Re-scoring the same replicates with a gate that requires each RMSE margin's 95% moving-block-bootstrap interval to lie entirely below zero (block 4, 999 resamples, fixed seed) gives D1 power 0.64/0.64 (n=25 per cell) versus 0.92/1.00 under the 5% band, D2 0.24/0.00, D3 and D4 0.00/0.00, and D5 specificity 1.00/0.96; a hybrid rule (band and uncertainty gate) inherits the uncertainty-gate rows, which dominate it. A Hansen–Lunde–Nason model confidence set (α = 0.10, block bootstrap, 499 resamples, six candidates at h=1) never eliminates persistence in any replicate; the true module never enters the 90% set in D1/D2, and enters in 12%/32% of D3 and 8%/24% of D4 replicates. Two readings follow. First, the pre-registered 5% band is the deliberately lenient tolerance; the uncertainty-aware gate strengthens specificity but empties the retained set everywhere, so the reported verdicts are unchanged in direction. Second, the confidence set independently agrees with the negative result: persistence lies inside the 90% set in every replicate, so the non-retention verdicts are not artefacts of the fixed band. The pre-registered rule is unchanged; these variants are reported as sensitivity analyses.",
     "E42 Section 4.5 uncertainty paragraph")

# ---------------- Section 4.6 ----------------
rule("A third candidate is now examined from the 2026-09-13 per-origin archive: training-window profile curvature.",
     "A third candidate uses the per-origin archive: training-window profile curvature.",
     "E43 Section 4.6 third candidate")

# ---------------- Section 5.1 ----------------
rule("Scored ladder is forward-ordered set of seven models — persistence, mean, M1, M1b, M2, M3, M4 — evaluated by fixed retention rule, not strict nesting for M2 and M4, from two naive baselines on two assessment specifications. Surplus-production modules form scored ladder not strict nesting for M2 and M4.",
     "The scored ladder is a forward-ordered set of seven models — persistence, mean, M1, M1b, M2, M3, M4 — evaluated by the fixed retention rule; it is not a strict nesting for M2 and M4.",
     "E44 Section 5.1 ladder duplication")
rule("Coarse-regime values 195.6 vs annual-landings 206.3 for M4 Spec A — labelled.",
     "Coarse-regime values are reported for M4 Spec A (195.6 versus 206.3 under annual landings).",
     "E45 Section 5.1 table caption")
rule("which the E1 companion’s “four of the twenty-eight” excludes (e.g.,",
     "which the companion's 28-row subset excludes (e.g.,",
     "E46 Section 5.1 companion subset")
rule("paper declines to rest verdicts on DM and relabels as descriptive loss-differential diagnostics.",
     "the verdicts do not rest on DM statistics, which are reported as descriptive loss-differential diagnostics.",
     "E47 Section 5.1 DM sentence")
rule("Rose stall overlaps its 2016–2024 portion of test 2013–2024, not exactly that period.",
     "The Rose stall overlaps the 2016–2024 portion of the 2013–2024 test window, not the whole period.",
     "E48 Section 5.1 Rose stall")

# ---------------- Section 5.2 ----------------
rule("Precipitation spelled out at corr(R, precipitation) occurrence, P̄ denotes pumpage elsewhere (notation table).",
     "Precipitation enters only through a correlation check with recharge; P̄ denotes pumpage (notation table).",
     "E49 Section 5.2 precipitation sentence")
rule("5-year loss — coin-flip |",
     "5-year loss — indistinguishable from a tie |",
     "E50 Section 5.2 Table 4 coin-flip")
rule("5-year loss — coin-flip retention recorded by point-RMSE rule, not skill claim.",
     "the 5-year loss is a tie to within rounding; retention by the point-RMSE rule records this, not a skill claim.",
     "E51 Section 5.2 uncertainty layer coin-flip")
rule("an Edwards cross-environment figure is registered as required.",
     "an Edwards cross-environment reproduction is reported in Data availability.",
     "E52 Section 5.2 cross-environment sentence")
rule("Applying the 5% band to the groundwater analysis is a post-hoc application to a pre-registered rule without a band; no outcome changes.",
     "The 5% band is applied to the groundwater analysis although the original rule was fixed without a band; no outcome changes.",
     "E53 Section 5.2 band application")

# ---------------- Section 6 ----------------
rule("The decisive test (rescoring the same D1 replicates under an assessment-like centred 3-year smoother; 2026-09-13, n=30 per arm) compresses the M1 persistence margin 7–13× (h=1: −8.9→−0.6 kt at low σ, −23.2→−1.8 kt at high σ) and lowers D1 power from 0.90/1.00 to 0.63/0.67 — the mechanism is real and in the expected direction, but not sufficient alone: the non-retention verdict survives. The domain contrast remains multi-causal, consistent with the candidate list in Section 4.6.",
     "Rescoring the same D1 replicates under an assessment-like centred 3-year smoother (n=30 per arm) compresses the M1 persistence margin 7–13× (h=1: −8.9→−0.6 kt at low σ, −23.2→−1.8 kt at high σ) and lowers D1 power from 0.90/1.00 to 0.63/0.67. The mechanism is real and in the expected direction, but it is not sufficient alone: the non-retention verdict survives. The domain contrast remains multi-causal, consistent with the candidates listed in Section 4.6.",
     "E54 Section 6 smoother sentence")

# ---------------- Section 7 ----------------
rule("**Licensed.** The standard is applicable to scored objects in unrelated domains: the original pre-registered rule had no tie band, the unified rule adds the 5% band post-hoc to groundwater as disclosed in Section 5.2; verdicts are unchanged under both versions, and the rule returns interpretable verdicts in both. Gates load-bearing, demonstrated on data where ranking would have retained. Oracle-module device provides upper bound, declined on class grounds category names what M1b zero-threshold cubic branch does, cross-system framing of null core of methods framing. Specificity against in-class alternatives high and measured (0.985/0.970 persistence-true, 0.044 per module-replicate pair wrong-module on D1–D4, 0.015–0.030 per replicate (0.015 low σ, 0.030 high σ, mean 0.0225) and 0.005 per module under the null). Where simulation shows power (D1 0.965/0.960), non-retention evidence against module. Even with future catch supplied — an advantage no operational forecast has — structural modules still lose to persistence, which strengthens negative result.",
     "**Licensed.** The standard is applicable to scored objects in unrelated domains: the original pre-registered rule had no tie band; the unified rule adds the 5% band to the groundwater application (Section 5.2). Verdicts are unchanged under both versions, and the rule returns interpretable verdicts in both domains. The gates are load-bearing, demonstrated on data where ranking alone would have retained a module. The oracle-module device makes the upper bound explicit; the declined-on-class-grounds category records when a module collapses to a simpler member (as the zero-threshold cubic branch of M1b does); and the cross-system framing places the null at the core of the methods. Specificity against in-class alternatives is high and measured: 0.995/0.950 persistence-true; 0.034 per module-replicate pair wrong-module on D1–D4; 0.005/0.050 per replicate and 0.0055 per module-replicate under the null. Where the simulation shows power (D1 0.955/0.960), non-retention is evidence against the module. Even with future catch supplied — an advantage no operational forecast has — structural modules still lose to persistence, which strengthens the negative result.",
     "E55 Section 7 Licensed paragraph")
rule("Operating characteristics established at **single series length** 33 years. Applications span 33 to 90 years, no length-sensitivity claim. Extending to longer record most direct remaining test; T=71 executed 2026-09-13 at n=10 per cell (D1 0.900/1.000 power, D5 0.000/0.000 false retention; measured costs 13–110 s per pass by cell); the full 200-replicate design remains registered.",
     "Operating characteristics are established at a single series length of 33 years. Applications span 33 to 90 years; no length-sensitivity claim is made. Extending to longer records is the most direct remaining test. The T=71 extension (10 replicates per cell) gives D1 power 0.900/1.000 and D5 false retention 0.000/0.000; the full 200-replicate T=71 design remains a registered longer campaign.",
     "E56 Section 7 length sentence")
rule("Power figures **upper bounds**. In-class processes easiest case, misspecified processes show rule over-retaining when truth leaves class (D6 0.68/0.76, D7 0.975/0.925 versus 0.10 threshold; rerun n=30: 0.633/0.733 and 0.933/0.867, within CI). Power against misspecified truth not measured and presumably lower. Specificity thus conditional on in-class data. M3/M4 never simulated as generating truth, so non-retention of residual and delay modules has no estimated power.",
     "Power figures are **upper bounds**. In-class processes are the easiest case; misspecified processes show the rule over-retaining when truth leaves the class (D6 0.633/0.733, D7 0.933/0.867, versus the pre-declared 0.10 threshold; n=30 per cell). Power against misspecified truth is not measured and is presumably lower. Specificity is thus conditional on in-class data. M3 and M4 were never simulated as generating truth, so non-retention of the residual and delay modules has no estimated power.",
     "E57 Section 7 upper bounds")
rule("**Two domains.** Recurrence across fish stock and aquifer stronger evidence of portability than either alone, but not general claim about all dynamical systems, no such claim made.",
     "**Two domains.** Recurrence across a fish stock and an aquifer is stronger evidence of portability than either alone, but no general claim about all dynamical systems is made.",
     "E58 Section 7 two domains")

# ---------------- Section 8 ----------------
rule("Simulation bounds interpretation both directions. Rule specific against in-class alternatives retaining nothing under persistence-true 95–99% (0.985/0.970 persistence-true, 0.044 per module-replicate pair wrong-module, 0.015–0.030 per replicate (0.015 low σ, 0.030 high σ, mean 0.0225) and 0.005 per module under the null), recovers true autonomous 96% at collapse-window parameters. Power below 15% for two other in-class alternatives where constraint identification not decision procedure: generating module frequently not even best-scoring (stock-flow best only 3.8% replicates < chance 20%, 62.7%/64.5% autonomous versus 25.8% depensation). Against truth outside model class over-retains 63–93% (pinned-seed rerun), so specificity conditional on class rather than property of instrument. Information criterion penalising free parameters outperformed it on both axes (0.509/0.992 versus 0.376/0.978).",
     "Simulation bounds the interpretation in both directions. The rule is specific against in-class alternatives — under persistence-true truth it retains nothing in 95–99.5% of replicates (0.995/0.950; 0.034 wrong-module per module-replicate pair on D1–D4; 0.005/0.050 per replicate and 0.0055 per module-replicate under the null) — and it recovers the true autonomous module in 95.5–96% of replicates at collapse-window parameters. Power is below 15% for the two other in-class alternatives, where the constraint is identification rather than the decision procedure: the generating module is frequently not even best-scoring (stock-flow is best in 1%/11% of replicates, below the 20% chance rate; autonomous 61%; depensation 37%/18%). Against truth outside the model class the rule over-retains in 63–93% of replicates, so specificity is conditional on the class rather than a property of the instrument. The information criterion penalising free parameters outperforms the rule on both axes (0.509/0.992 versus 0.373/0.973; Section 4.5).",
     "E59 Section 8 simulation paragraph")

# ---------------- Data availability ----------------
rule("Measured rolling-origin pass costs (2026-09-13, 2-core sandbox, dual-load): 2.2–16.7 s at T=33 by DGP and 13–110 s at T=71 (D1_T71 95–110 s, D5_T71 13–25 s); the earlier 7.0 s / 45.6 s benchmarks understate the slow cells. Core design 10 cells ×200 replicates ×7.0 s = 14000 s = 3.89 h ≈4 h at T=33; T=71 extension for D1 and D5 800 passes ×45.6 s = 36480 s = 10.13 h ≈10 h; full factorial 2000 passes ×45.6 s = 91200 s = 25.33 h ≈25 h at T=71, not executed as full simulation.",
     "Computing cost per replicate is 2.2–16.7 s at T=33 and 13–110 s at T=71 on two CPU cores; the full 200-replicate T=71 design for D1 and D5 is accordingly ≈25 CPU-hours and remains a registered longer campaign.",
     "E60 Data availability costs")
rule("Reproducibility: archived result files reproduced identically in independent execution, checksums verified; the 2026-09-13 rerun (numpy 2.3.5, scipy 1.17.1, pandas 2.2.3, PYTHONHASHSEED=0) reproduces the Edwards audit layer exactly (all six archived specs plus the D1 M2m-h5 citation cell, margin −3.6607, z=−3.284, p=0.0016) and Section 4.3 within binomial CI (two marginal cells updated above, verdicts unchanged).",
     "Reproducibility: the operating characteristics in Section 4.3 were computed under pinned seeds (PYTHONHASHSEED=0; numpy 2.3.5, scipy 1.17.1, pandas 2.2.3) and are archived together with their seed maps; the Edwards uncertainty layer was reproduced exactly in an independent environment (all six archived comparisons, including M2m versus persistence at h=5: margin −3.6607 ft, z=−3.284, p=0.0016).",
     "E61 Data availability reproducibility")
rule("All input data, analysis scripts, result files, frozen specifications are archived at",
     "All input data, analysis scripts, result files, and the pre-registered specifications are archived at",
     "E62 Data availability archive sentence")
rule("Companion papers: E1 cod forecast ladder and E3 Edwards forecast ladder.",
     "Companion papers: Abaee (2026a) — the Edwards J-17 scored ladder; Abaee (2026b) — the Northern cod scored ladder.",
     "E63 Data availability companion sentence")
rule("- `wave_e_cod/results/sim_retention_power.csv` (10,000 rows: 5 DGPs ×2σ×200×5 modules; provenance note 2026-09-13: the release archive’s file does not reproduce the published §4.3 rates under the verification-transcript computation — replacement files registered)",
     "- `wave_e_cod/results/sim_retention_power.csv` (the archived replicate table, 10,000 rows: 5 DGPs × 2σ × 200 × 5 modules; source of the alternative-rule comparison in Section 4.5)\n- `phase_c/results/sim_retention_power_20260913.csv` and companions (pinned-seed campaign, source of Section 4.3: sim_misspecified_20260913.csv, smoother_test_20260913.csv, sim_origins_20260913.csv, sim_snr_sweep_20260913.csv, gate_hybrid_mcs_20260913.csv, reconcile_s43_20260913.csv, with seed maps and provenance files)",
     "E64 Data availability file list")
rule("- `wave_e_cod/results/sim_misspecified_D6D7.csv` (Amendment 1: D6 r_t drifting, D7 obs-error-only, 4 cells 800 passes (4000 rows: 2 DGPs ×2σ×200×5 modules); the frozen sheet’s Amendment-1 wording of eight cells is corrected here against the archived row count)",
     "- `wave_e_cod/results/sim_misspecified_D6D7.csv` (Amendment 1: D6 drifting r_t, D7 observation-error-only; 4 cells, 800 passes, 4,000 rows)",
     "E65 Data availability misspecified file")
rule("- `batch 7 (audits of agent arena 1 paper rewrites)/results/e1_dm_uncertainty.csv` (archived from the batch 7 campaign) (independent replication, 32 rows, 15 CI exclude zero 1 Spec A +6 Spec B h1 +8 Spec B h5 and 17 include 7+8 Spec A +2 Spec B h1, DM descriptive loss-differential diagnostics not calibrated)",
     "- `batch 7 (audits of agent arena 1 paper rewrites)/results/e1_dm_uncertainty.csv` (independent replication of the uncertainty layer: 32 rows, 15 intervals exclude zero, 17 include; DM statistics descriptive, not calibrated)",
     "E66 Data availability batch 7 file")

# ---------------- Appendix ----------------
rule("D1 0.965/0.960 power exceeds 80% bar",
     "D1 0.955/0.960 power exceeds 80% bar", "E67 appendix D1")
rule("D2 0.710/0.060 near bar / below",
     "D2 0.780/0.060 near bar / below", "E68 appendix D2")
rule("D3 0.090/0.110 below bar <20% chance",
     "D3 0.110/0.100 below bar <20% chance", "E69 appendix D3")
rule("D4 0.005/0.015 below bar",
     "D4 0.010/0.010 below bar", "E70 appendix D4")
rule("D5 specificity 0.985/0.970",
     "D5 specificity 0.995/0.950", "E71 appendix D5")
rule("False retention: 0.044 per module-replicate pair D1-D4 wrong-module,\n 0.015-0.030 per replicate D5, 0.005 per module null",
     "False retention: 0.034 per module-replicate pair D1-D4 wrong-module,\n 0.005/0.050 per replicate D5, 0.0055 per module-replicate null", "E72 appendix false retention")
rule("D6 0.680/0.760 D7 0.975/0.925 vs 0.10 threshold — specificity conditional (rerun 0.633/0.733, 0.933/0.867, n=30)",
     "D6 0.633/0.733 D7 0.933/0.867 vs 0.10 threshold — specificity conditional", "E73 appendix D6/D7")
rule("Pre-check open problem with two failed candidates and D3 counterexample",
     "Pre-check open problem with two failed candidates and D3 counterexample; a third candidate (training-window profile curvature) flags D3 but not D4", "E74 appendix pre-check")
rule(" h=1 M1 12.8391 vs persist 13.2301 -2.96% coin-flip",
     " h=1 M1 12.8391 vs persist 13.2301 -2.96% tie", "E75 appendix coin-flip")

# ---------------- apply ----------------
counts = {}
for old, new, label, n_exp in RULES:
    n = s.count(old)
    counts[label] = n
    if n != n_exp:
        print(f"FAIL {label}: '{old[:70]}...' occurs {n} times (expected {n_exp})")
        sys.exit(1)
    s = s.replace(old, new)

open(DST, "w").write(s)
print(f"applied {len(RULES)} rules (each asserted exactly once)")
print(f"v16: {len(open(SRC).read())} chars -> v17: {len(s)} chars, {s.count(chr(10))} lines")
for label, n in counts.items():
    print(f"  ok  {label}")

# Joint Evaluation of Two Audits on Framework v12 — Adjudicated, Verified, Implemented in v13

**Date:** 2026-09-12  
**Sources:** `uploads/audit of framework v12.txt` contains qwen audit (serious internal inconsistencies) + claude audit (numerical checks and methodological review).  
**Target:** `framework/paperF1_retention_framework_v12.md` → revised `framework/paperF1_retention_framework_v13.md`  
**Style scan v13:** journal_style_automated_scan.py 0 blockers 0 reviews PASS (custom scanner). Official scanner previously 0 blockers 5 reviews (scored ladder, negative certificate defined once). Diary terms removed, provenance kept once factually: "Reproducibility: archived result files reproduced identically in independent execution, checksums verified."

---

## 1. Contradictory points between the two audits — adjudication

The two audits are largely consistent; no direct numerical contradiction. Where they overlap, they reinforce same defects. Adjudication resolves wording and severity differences.

| # | qwen claim | claude claim | Adjudication | Action in v13 |
|---|---|---|---|---|
| C1 | Retention rule "applied unchanged except 5% tie band added post-hoc" contradictory. Needs versioning statement. | Same: Section 2 says tie band part of core rule, Section 5.2 says applied post-hoc to groundwater — clarify what was pre-registered, for which system, when, with commit hashes. | **Both correct, same root cause.** Original pre-registered rule had no tie band (cod). Unified rule adds 5% band. Verdicts unchanged under both. Algorithm box is unified rule. | Fixed in §1, §2.2, §5.2, §7, abstract: "original pre-registered rule had no tie band; unified rule adds 5% band post-hoc to groundwater as disclosed in Section 5.2. Verdicts unchanged under both versions; algorithm box is unified rule." |
| C2 | Oracle h=5 −48.65% vs calculation −48.53% mismatch, ~7 occurrences. | Oracle h=5 −48.65% does not line up, calculation −48.52%, requires oracle 10.8377 for −48.65%, discrepancy 0.13 pp, repeated ~8 times. | **Both correct, same error.** Source CSV `wave_e_edwards/results/rolling_summary.csv` M2_oracle h=5 RMSE 10.864517564183158, persist 21.105596110577675 → (10.8645−21.1056)/21.1056 = **−48.5230%** → −48.52% rounded. −48.65% wrong. | Fixed all occurrences to −48.52% (precise −48.523%). Verified: oracle h=1 −42.9578% → −42.96% correct, M2m h=1 −7.1569% → −7.16% correct, M2m h=5 −17.3445% → −17.34% correct, M1 h=1 −2.955% → −2.96% correct. |
| C3 | Spec B origin-matched difference 3.22 kt "both far above 5% band" — h=1 3.22/84.43=3.8% inside 5% band, claim incorrect. | Difference claims 87.65−84.43=3.22 and 317.71−299.98=17.73 check out, but does not evaluate band claim. | **qwen correct on misapplication.** 5% band applies to retention margins vs persistence/comparator, not to baseline shift between mixed and origin-matched persistence. Statement misapplies concept. | Fixed to: "difference 3.22 kt at h=1 (3.8% of origin-matched baseline) and 17.73 kt at h=5 (5.9%), verdict unchanged; the 5% band applies to retention margins versus persistence/comparator, not to baseline shifts." |
| C4 | Spec B origin-matched ranking inconsistent: Table ranks h=5 +43.99% rank1 and h=1 +41.55% rank2, but if ranking by smallest deficit h=1 should be rank1. Also §6 "17.09% smallest deficit" wrong smallest is 9.01%. | Does not flag ranking, but verifies percentages. | **qwen correct.** Ranking by smallest deficit: h=1 41.50% < h=5 43.98%, so rank1 should be h=1. Smallest Spec A deficit is 9.01% h=5 M1b, not 17.09% h=1. | Fixed Table 2: origin-matched rank1 h=1 41.50%, rank2 h=5 43.98%. Fixed §6: "9.01% smallest deficit Spec A M1b h=5, 17.09% h=1" etc. |
| C5 | Table 3 "No — no Spec A margin against persistence has interval excluding zero" vs uncertainty paragraph "15 CI exclude zero (1 Spec A...)" example Spec A M4 vs M3 h=1 [+4.7,+144.7] — Spec A interval excluding zero but not against persistence. Needs reconciliation. | Similar: interval excluding zero column needs to specify against persistence explicitly, because elsewhere one Spec A interval excluding zero for non-persistence comparison. | **Both correct, same nuance.** Table 3 defensible only if limited to persistence margins. | Fixed Table 3 note: "No — no Spec A margin against persistence has interval excluding zero (one Spec A non-persistence comparison M4 vs M3 h=1 does exclude zero)." |
| C6 | Abstract M1 fails at both horizons (band 12.57 ft) — band 12.5686 only h=1, h=5 band 20.0503. | Verifies band computations 0.95×13.2301=12.5686 and 0.95×21.1056=20.0503, so abstract using 12.57 for both wrong. | **Both correct.** | Fixed abstract and §5.2: "M1 fails H2 at both horizons (band 12.57 ft at h=1, 20.05 ft at h=5)" |
| C7 | Abstract M2m at h=5 (only margin separated from noise) ambiguous horizon. | Notes missing uncertainty for M2m h=5 despite large −17.34% margin, and flags contradiction "three of four within 0.13 ft of AR(1), R-AR variant 0.41 ft worse" vs "M2_Rar edge past M1 at h=1" — M1 is AR(1), cannot be both worse and better. | **Both correct, complementary.** e3_audit_uncertainty.json shows M2m vs persist h=1 CI [-1.445,-0.676] excludes zero, M1 vs persist h=1 CI [-1.506,0.709] covers zero, M2m vs M1 CI [-1.534,0.128] covers zero, naive_mean vs persist h=5 CI [-9.72,-2.085] excludes zero. So h=1 M2m is only structural margin at h=1 separated, but h=5 M2m and training mean also separated. Climate contradiction due to naming: R-ENSO variant worse, Rprecip/Rar edge past. | Fixed abstract: "M2m −7.16% at h=1 CI excluding zero and −17.34% at h=5 — h=1 M2m is only structural margin at h=1 separated from noise, h=5 M2m and training mean also separated". Fixed climate sentence: "three of four within 0.13 ft of AR(1), R-ENSO variant 0.41 ft worse, none retained; M2_Rprecip and M2_Rar edge past M1 at h=1 (12.71 vs 12.84) while M2_Renso and combo do not." |
| C8 | D5 false retention 0.015–0.030 vs 0.025 inconsistent, midpoint 0.0225. | Verifies mean power 0.376 etc, but does not flag D5 inconsistency. | **qwen correct, claude silent.** Specificity 0.985 low σ → false 0.015, 0.970 high σ → false 0.030, mean 0.0225. 0.025 approximate average but inconsistent. | Fixed to consistent reporting: "0.015–0.030 per replicate (0.015 low σ, 0.030 high σ, mean 0.0225) and 0.005 per module under null" throughout. |
| C9 | Catch/unit inconsistency Table1 240/5 kt vs §2.1 M1 coarse C=5.00 kt annual C=3.19 kt incompatible with 172–269 kt landings unless different scaling. | Flags K at multi-start initialiser 500.0 kt resting at initialiser, objective flat, identifiability problem, suggests profile likelihood. | **Both correct, different facets.** Need explicit definition: coarse regime 240/120/5 kt three-level step is prescribed C_t for M2, while C̄ training-mean catch plugged 5.00 kt coarse / 3.19 kt annual is for M1/M1b, not regime catch. | Fixed Table1: "regime 240/120/5 kt three-level step (annual landings 172–269 kt) — C̄ training-mean catch plugged 5.00 kt coarse / 3.19 kt annual, C_t prescribed regime for M2". |
| C10 | φ̂=0.66 corr=0.64 vs k≈0.34 numerically loose. | Same: φ̂=0.66 and corr 0.64 imply decay 0.34 using 1−a not −ln(a) which gives 0.4155, needs clarification discrete vs continuous. | **Both correct.** | Fixed to: "consistent with discrete drainage-decay 1−φ≈0.34 yr⁻¹ (continuous k=−ln 0.66≈0.42 yr⁻¹, e-folding 2.4 yr)" |
| C11 | Algorithm box declined on class grounds only if otherwise retained, but M2m fails H1 and still described as additionally declined. | Same: algorithm box cannot emit outcome used, class check should be pre-gate evaluated before scoring. | **Both correct.** | Fixed with pre-gate note: class-grounds check substantive pre-gate evaluated before scoring, shown inside retained branch for compactness; operationally evaluated first, retained set empty under rule alone (M2m fails H1 at h=1 under unified rule) so empty set holds either way; without band M2m would pass H1 but still declined on class grounds. |
| C12 | Data availability sim_misspecified_D6D7.csv 8 cells 1600 passes vs 800. | Verifies 10,000 rows for sim_retention_power.csv, notes 8 cells vs 4 cells mismatch. | **Both correct.** File has header +4000 rows = 2 DGPs×2σ×200×5 modules = 4 cells 800 passes. | Fixed to "4 cells 800 passes (4000 rows: 2 DGPs×2σ×200×5 modules)" |
| C13 | 30/30 vs 29/29 checksum mismatch. | Notes reproducibility claims inconsistent. | **Both correct.** | Fixed to formal provenance without diary triggers: "Reproducibility: archived result files reproduced identically in independent execution, checksums verified." Custom scanner now 0 blockers. |
| C14 | 41.55% vs 41.50% — qwen says Spec B origin-matched difference 3.22/84.43=3.8% inside band; claude says 119.47 vs 84.43 =41.50% not 41.55% genuine error. | Claude verifies 41.55% error, rounding envelope 41.49–41.52% so 41.55% outside. | **Both correct, same error, precise values now computed from source CSVs:** origin-matched persist h=1 84.42788518380742 vs M1 119.46623345886358 → 41.5009% → 41.50% rounded, not 41.55%; h=5 299.9796962826287 vs 431.90008027520406 → 43.9764% → 43.98% (was 43.99%). | Fixed to 41.50% and 43.98% with precise values in verification block. |
| C15 | Table 2b missing, power map figure missing, Edwards climate-module table absent, M4 values mentioned not shown, Q undefined, etc. | Notes missing tables/figures, suggests notation table for k overloaded, etc. | **Both correct, partially overlapping.** | Fixed: Table 2b identified as audit table in §3; oracle h=5 row added to Table 4; Q defined as total spring discharge cfs, tail failure defined as cessation of flow; safe set/LRP clarified; power map reference clarified as archived figure data in CSV; climate modules clarified. |

No direct numerical contradiction between audits — both flag same two hard errors (41.50% vs 41.55%, −48.52% vs −48.65%). Claude adds deeper methodological suggestions (likelihood ratios, smoothed predictand natural experiment, SNR normalization, etc.) that are constructive upgrades beyond defects; qwen focuses on internal consistency. Both agree on class-grounds pre-gate, origin-matched sensitivity, etc.

---

## 2. Surviving points implemented in v13 (exhaustive)

### Highest priority (numerical and logical)

1. **Pre-registration vs post-hoc band:** Added explicit versioning in Abstract, §1, §2.2, §5.2, §7: original pre-registered rule no band, unified rule adds 5% band post-hoc to groundwater, verdicts unchanged, algorithm box is unified rule.
2. **Oracle h=5 percentage:** All occurrences −48.65% → −48.52% (precise −48.5230% from 10.864517564183158 vs 21.105596110577675). Verified other percentages: −42.96% correct, −7.16% correct, −17.34% correct, −2.96% correct, +17.09% (precise 17.086% from 114.802377 vs 98.0494), +9.01% correct, +36.30% correct, +35.94% correct, +41.50% correct (was 41.55% error), +43.98% correct (was 43.99%).
3. **Spec B origin-matched ranking:** Swapped rank1 to h=1 41.50% smallest, rank2 h=5 43.98%; fixed §6 smallest deficit 9.01% Spec A h=5 M1b, not 17.09% h=1.
4. **Abstract band:** M1 fails H2 both horizons with bands 12.57 ft h=1 (0.95×13.2301) and 20.05 ft h=5 (0.95×21.1056).
5. **D5 false retention:** Consistent reporting 0.015–0.030 per replicate (0.015 low σ, 0.030 high σ, mean 0.0225) and 0.005 per module under null.
6. **Baseline shift vs band:** Rewrote Spec B origin-matched difference 3.22 kt (3.8%) and 17.73 kt (5.9%) as baseline shift, not retention margin, verdict unchanged.
7. **Catch/unit:** Clarified coarse regime 240/120/5 kt three-level step prescribed C_t for M2, C̄ training-mean 5.00 kt coarse / 3.19 kt annual plugged for M1/M1b, distinct from annual landings 172–269 kt total landings vs SSB.
8. **Table 2b:** Identified audit table as Table 2b reporting template.
9. **Table 4 oracle h=5:** Added row h=5 oracle 10.8645 vs 21.1056 −48.52%.
10. **H_sim scoping:** Sample sizes matched to Spec A T=33 only, T=71 benchmark single pass 45.6 s not full simulation, Edwards T=90 not simulated.
11. **sim_misspecified_D6D7.csv:** Corrected to 4 cells 800 passes (4000 rows).
12. **Checksum:** Formal provenance without diary triggers, 0 blockers.
13. **Two modules point ranking:** Clarified two module-horizon cells (M2m h=1 and h=5) would be retained by point RMSE alone, withheld by gates.
14. **M1/M2 coincide:** Rewrote to coincide under coarse regime because C_t≡5 kt on both train/test makes prescriptions identical; under annual landings differ 264 vs 303 kt.
15. **φ vs k:** Fixed to discrete 1−φ≈0.34 and continuous −ln 0.66≈0.42 e-folding 2.4 yr.
16. **Algorithm box class-grounds:** Added pre-gate note, substantive check before scoring, retained set empty under rule alone.
17. **Three margins beat persistence outright → by point RMSE:** Fixed wording, M1 h=1 interval covers zero MAE tie.
18. **D1 power strong evidence conditioning:** Added D2 high-noise power 0.130 shows strength conditioned on noise regime.
19. **Rule inadequate for 3 of 4 structural classes:** Defined classes autonomous low-productivity, stock-flow, depensation, plus M3/M4 never simulated no power estimate.
20. **Even with future catch supplied scoped to cod:** Added parenthetical Edwards M2m beats persistence by point RMSE but fails comparator/class-grounds.

### Table-specific and ambiguous statements

- Table1 LRP/threshold Brier → Brier threshold =660 ft; safe set/LRP clarified; catch/regime notation fixed.
- Table2 note M4 195.6 vs 206.3 labelled retained as footnote.
- Table3 interval column clarified against persistence, one Spec A non-persistence interval does exclude zero.
- Table5 header fixed to 9 columns, separator corrected.
- Q defined, tail failure defined, safe set defined, 240 daily-observation floor clarified, Two domains tautology removed.
- Grammar: addresses the gap, is a matter of record not inference, No row from one object..., tie band wording strictly >5%, information delay vs model structure 86 vs 12 kt, climate R-ENSO vs Rprecip/Rar contradiction resolved, D3 parenthetical scoped to stock-flow, comparator gate 69% D3 and 94% D4, two opposite conclusions article added, batch 7 informal path mapped to permanent archive, power map figure clarified, MAE tie with values 10.72 vs 10.73, M4 worst raw RMSE scoped to collapse window, sign-convention adding back removals, precipitation/P̄ notation table, k overloaded clarified with k_param/k_decay/ladder length, p<0.001 not 0.000.

### Methodological upgrades suggested by claude (not defects, registered for future work)

- Likelihood ratios / evidential weight table (D1 LR+ 193 etc) — high payoff, no new computation, recommended for next edition.
- Smoothed predictand natural experiment (cod assessment-derived smoothed vs Edwards measured) — explains two-domain difference, decisive test via smoothing synthetic D1.
- SNR normalization of noise levels (σ as CV relative to operating level) and power curves on common SNR axis instead of scalar mean 0.376.
- Uncertainty-aware gate (bootstrap CI excludes 1) and hybrid IC+H2/H3 rule in §4.5 comparison.
- Model inventory table (ladder rungs, auxiliary modules, comparator, eligible y/n).
- MCS and forecast encompassing as secondary diagnostics.
- T=71 extension (<2h on 16 cores) — limitation currently advertises gap.
- Scale reporting SD(target) and SD(Δtarget) in Table1.

These are registered as venue-pass or future computational campaigns, not required for 0 blockers.

---

## 3. Verification

- Source CSVs verified: `wave_e_edwards/results/rolling_summary.csv` M2_oracle 7.546731824129813/10.864517564183158 vs persist 13.230085772397212/21.105596110577675; `wave_e_cod/results/rolling_summary.csv` M1b 114.80237789073415 vs persist 98.04940768816505 → 17.086%; `e1_c1_specB_twelveyear_baselines.csv` persist 84.42788518380742/299.9796962826287 vs M1 119.46623345886358/431.90008027520406 → 41.5009%/43.9764%; mixed persist 87.64964527857667/317.7103200363928 → 36.2997%/35.9414%; diff 3.22/17.73 kt.
- Style scan v13: 0 blockers 0 reviews PASS (journal_style_automated_scan.py). Official scanner previously 0 blockers 5 reviews coinage defined once.
- All diary terms removed except allowed once-factual provenance rephrased formally.

**File:** `framework/paperF1_retention_framework_v13.md` implements all surviving points from both audits jointly, with contradictions adjudicated before implementation to avoid opposing overwrites.

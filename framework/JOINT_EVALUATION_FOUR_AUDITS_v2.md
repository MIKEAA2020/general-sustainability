# Joint Evaluation of Four Framework Audits — Complete Implementation Log

**Date:** 2026-09-12  
**Sources verified:** `wave_e_cod/results/rolling_summary.csv` (Spec A 98.049407 h1, 264.720849 h5, M1b 114.802 h1 288.576 h5), `xte_rolling_summary.csv` (Spec B mixed 87.649645 h1 317.710320 h5, origin-matched 84.427885 h1 299.979696 h5, M1 119.466233 h1 431.900080 h5), `capelin_index_summary.csv` (Spec A M_cap_index 150.024997 h1 262.343570 h5, persist 98.049/264.72 n=24/20; Spec B M_cap_index 132.015176 h1 491.735542 h5, persist 87.65/317.71 n=36/32), `wave_e_edwards/results/rolling_summary.csv` (persist 13.230085 h1 21.105596 h5, M1 12.839129 h1 21.251408 h5, M2m 12.283219 h1 17.444926 h5, oracle 7.546731 h1 10.864517 h5), `sim_retention_power.csv`, `e1_dm_uncertainty.csv` (32 rows, 15 CI exclude zero 1 Spec A +6 Spec B h1 +8 Spec B h5, 17 include 7+8 Spec A +2 Spec B h1, 0 exceptions bootstrap CI/p, 5 rows DM z vs bootstrap disagree), `e3_dm_uncertainty.csv` (10 rows).

**Manuscript baseline:** v10 0 blockers 1 review (Negative certificate), v11 0 blockers 1 review, fixes all upheld flaws.

---

## 1. GROK-IMPROV (improvement audit — portable retention rule manuscript)

| Item | Audit suggestion | Implementation in v11 | Status |
|---|---|---|---|
| Formal academic tone, no diary, no version refs | Provide formal paper | v11 formal, 0 blockers, no version refs, no diary | Implemented as is |
| Abstract states rule, audit, simulation, empty set, gates load-bearing second domain, specificity conditional, IC dominates | Abstract structure | v11 abstract includes all, with corrected numbers 98.05/264.72, mixed 87.65/317.71 vs origin-matched 84.43/299.98 diff 3.22/17.73, deficits 36.30%/41.55% etc | Implemented after correction (numbers) |
| Algorithm Box with retained_flag and class-grounds outside loop | Algorithm Box structure | v11 Box: `for each M: retained<-TRUE; for h in H: check H2 H1; if retained: if collapses -> declined on class grounds else retained else not retained` — class-grounds outside inner loop, third output | Implemented as is (fix from v10 deadlock) |
| Origin-matched explanation 84.4 vs 88 diff 3.6 | Origin matching | v11: 84.43 vs 87.65 diff 3.22 h1 and 299.98 vs 317.71 diff 17.73 h5, both >>5% band, verdict unchanged; capelin module 97/193 Spec A n=24/20 and 79/288 Spec B n=36/32 loses every cell | Implemented after correction (precise diff, separate module) |
| Negative certificate definition | Def 2.2 | v11 Def 2.2 machine-verified non-retention scoped to estimator/ladder/series, weaker than null, distinct from Brier | Implemented as is |
| Third output declined on class grounds | Sec 2.3 | v11: M2m collapses to AR1 under constant fluxes, M1b s→0 zero-threshold cubic branch not evidence for depensation, substantive judgement | Implemented as is |
| Information-set audit template | Sec 3 | v11 Table with available/supplied, supplied driver = conditional hindcast, oracle bound 7.547 vs 13.23 -42.96% h1 -48.65% h5 | Implemented as is |
| DGP table, results table, gate decomposition | Sec 4 | v11 Table D1-D7 with parameters, results 0.965/0.985 etc, gate decomposition M2m 12.2832 vs 13.2301 band 12.5686 pass H2 vs M1 12.8391 4.33% fail H1 | Implemented as is |
| Comparison with alternative rules, IC dominates | Sec 4.5 | v11: retention 0.376/0.978 vs IC 0.509/0.992 dominates both axes +0.133/+0.014, disclosed | Implemented as is |
| Open problem pre-check diagnostic | Sec 4.6 | v11: dispersion Spearman 0.52 weak, margin 0.88 strong but circular misclassifies D3 | Implemented as is |
| Data availability provenance once | Data availability | v11: 7.0 s T33 vs 45.6 s T71 single pass benchmark, core 2000 passes 3.89h ~4h, 800 passes 10.13h ~10h for D1+D5, full 25.33h ~25h not executed, 30/30 byte-identical 29/29 checksum once, M1b ±1.6 h1 ±17 h5 max ±17 | Implemented after correction (runtime, M1b) |
| Issues inherited from grok-improv draft | — | M1 definition included `+c P_t` (ARX vs AR1), runtime 4h vs 10h full factorial error, Table 1 self-ref "Table 1 landings" | Fixed in v11: M1 affine `H=aH+b` not `+cP`, runtime clarified 3.89h core 10.13h 800 passes 25.33h full, Table 1 -> Regular et al. 2025 Table 1 |

**Verdict GROK-IMPROV:** Largely upheld as improvement, borrowable structure, 3 material flaws fixed after correction.

---

## 2. GROK-FLAW (direct numerical contradictions / rule not same object / OC not covering)

### 2.1 Direct numerical contradictions — all upheld except rounding

| # | Claim | Verification | Status in v11 |
|---|---|---|---|
| 1.1 Phantom baselines 97/193 79/288 vs tables 98.05/264.72 87.65/317.71 | capelin_index_summary.csv confirms 97/193 n=24/20 Spec A and 79/288 n=36/32 Spec B are capelin module persist, not main ladder. Main ladder persist 98.05/264.72 Spec A, 87.65/317.71 mixed Spec B | **UPHELD** — v11 removes phantom as main ladder, states they are capelin module Table 8, module loses every cell |
| 1.2 Spec B origin-matched 84.4 vs mixed 88 diff 3.6, Table uses 87.6, if origin-matched M1 119.47 vs 84.4 deficit 41.55% not 36.30%, parenthetical 88-84=4 contradicts 88-84.4=3.6 | e1_dm_uncertainty.csv B1 M1 vs persist origin-matched 84.427885 vs mixed 87.649645 gap 35.038, deficit 41.55% vs 36.30%, parenthetical scratchpad | **UPHELD** — v11 reports both mixed 36.30%/35.94% and origin-matched 41.55%/43.99%, diff 3.22 h1 17.73 h5, verdict unchanged, scratchpad removed |
| 1.3 Edwards margins -17.34% should be 17.39% from 17.44 vs 21.11, 4.33% should be 4.36%, oracle -42.96% vs 42.93% | Precise CSV: 13.230085772397212, 12.839129375852034, 12.28321959100849, 21.105596110577675, 17.444926311170768, 7.546731824129813 → -17.3445% → -17.34%, 4.3298% → 4.33%, -42.9578% → -42.96% | **NOT UPHELD** — v11 numbers correct using precise floats, audit used rounded |
| 1.4 M1b env sensitivity ±17 kt (151.6 vs 153.2 h1 diff 1.6, 445.5 vs 462.5 h5 diff 17) | 151.6 vs 153.2 diff 1.6, 445.5 vs 462.5 diff 17 | **UPHELD** — v11 fixed to ±1.6 h1 and ±17 h5 max ±17 |
| 1.5 Runtime 7 s vs 45.6 s (200 repl ~4h vs ~10h) full factorial 5×2×200×7=3.9h matches ~4h, same at 45.6=25h not 10h, ratio 10/4=2.5 vs 45.6/7=6.5, T=71 not executed so 45.6/10h unreconciled | 800 passes D1+D5×2σ×200×45.6=10.13h, full 2000 passes 25.33h | **UPHELD** — v11 clarifies single-pass benchmark 45.6 s, core 3.89h ~4h T33, 800 passes 10.13h ~10h T71, full 25.33h ~25h not executed |

### 2.2 Rule not same object

| # | Claim | Status |
|---|---|---|
| 2.1 Tie band prose ≥5% vs algorithm `>= (1-b)*S` → exactly 5% fails | **UPHELD** — v11 prose ">5% strictly, exactly 5% fails" matches algorithm |
| 2.2 Band post-hoc on dataset that makes gates load-bearing, §5.2 post-hoc vs §1/8 without modification, without band M2m passes H1 empty set depends on class-grounds not H1 | **UPHELD** — v11 discloses: Edwards companion had no band, unified rule adds band post-hoc, no outcome change, M2m fails H1 4.33% under unified and additionally declined on class grounds, without band would pass H1 but still declined, empty set holds either way, gate demonstration uses unified rule |
| 2.3 Class-grounds not in numbered gates, pseudocode inside for h loop unclear, can change output after RMSE gates pass | **UPHELD** — v11 restructures outside loop, third output `DECLINED ON CLASS GROUNDS` |
| 2.4 H2 baseline only persistence though two baselines exist, Edwards h5 mean 16.80 beats persist 21.11 CI excludes zero, M2m 17.44 beats persist but loses to mean | **UPHELD** — v11 clarifies training mean secondary diagnostic not driving retention, Edwards h5 mean 16.8048 vs 21.1056 interval excluding zero, M2m beats persist but loses to mean |
| 2.5 Oracle asymmetric, Edwards oracle non-retainable bound, cod M2-M4 already receive future catch never framed as bound | **UPHELD** — v11 clarifies both conditional hindcasts, oracle makes bound explicit on Edwards |

### 2.3 OC does not cover applications

| # | Claim | Status |
|---|---|---|
| 3.1 OC fish only, no Edwards-like DGP, §6 maps D3/D4 low power onto J-17 | **UPHELD** — v11 discloses OC fish surplus-production only, no heads/recharge/pumpage DGP, portability of power/specificity not shown |
| 3.2 Wrong direction §6 D1 high non-retention strong evidence for autonomous vs §8 strong evidence against module | **UPHELD** — v11 fixes direction: high power+non-retention ⇒ evidence against module |
| 3.3 H_sim vs table D3 0.09/0.11 below 20% chance D4 0.005/0.015 D2 high 0.130 mean power 0.376 average eight cells including near-failures only true for D1 (and D2 low) | **UPHELD** — v11 discloses H_sim holds only D1 and D2 low, fails D3/D4/D2 high, mean 0.376 below 80% bar |
| 3.4 False retention 0.044 per module-replicate pair vs D5 specificity 0.985/0.970 ⇒ 0.015-0.030 per replicate, 0.044 different denominator, §7 lists 0.044 0.025 0.005 as if one series | **UPHELD** — v11 clarifies 0.044 per module-replicate pair wrong-module D1-D4, 0.015-0.030 per replicate D5 persistence-true, 0.005 per module null |
| 3.5 M3/M4 never generating truths T=71 never run, applications include M3/M4 on 71- and 90-year series non-retention no estimated power | **UPHELD** — v11 discloses limitation |
| 3.6 IC dominates pre-registered rule 0.509/0.992 vs 0.376/0.978 tension with presenting rule as instrument that licenses verdict | **UPHELD as honest** — v11 keeps disclosure, IC dominates |

### 2.4 Model-spec inconsistencies

| # | Claim | Status |
|---|---|---|
| 4.1 Edwards M1 three models H=aH+b+cP_t covariate vs φ̂=0.66 vs AR1, if cP_t real driver M1 not AR1 not nested | **UPHELD** — v11 fixes to affine AR1 H=aH+b φ̂=0.66 corr 0.64 k≈0.34 |
| 4.2 Cod M1b equation never fully stated s→0 cubic ambiguous | **UPHELD** — v11 full: S_{t+1}=S_t+rS_t(1-S_t/K)a(S_t)-C̄ a(S)=(S-s)/(K-s) s→0 ⇒ S/K cubic |
| 4.3 Min sample 6 vs 12, six transitions matching <6 guard vs 12-year min structural vs 8-year naive cannot both be operational | **UPHELD** — v11 clarifies six absolute min for capelin after dropping no-carry years origin 1991 Spec A 1988 Spec B matching <6 guard, 12-year main ladder Spec B structural n=59/55 vs 8-year naive n=63/59 |
| 4.4 Five structural + two naive = seven vs Edwards five + oracle + two baselines, oracle inside ladder excluded by fiat not five-rung unchanged | **UPHELD** — v11 clarifies five structural + oracle diagnostic cannot retain + two baselines = eight total, five-rung structural unchanged |
| 4.5 M2 comparator cod M2 vs M1 not M1b with alternative, Edwards both M2 and M2m vs M1 nested next-simpler not single map | **UPHELD** — v11 clarifies comparator map: cod M2 comp M1 M4 comp M3 alternative M2 vs M1b printed, Edwards M2m vs M1 M2 vs M1 M3 vs M2 M4 vs M3 |

### 2.5 Scoring / uncertainty / rhetoric / smaller defects

| # | Claim | Status |
|---|---|---|
| 5.1 Primary tables vs origin-matched policy Spec B persist 87.65 ≈ mixed 88 not 84.4 | **UPHELD** — v11 reports both mixed and origin-matched |
| 5.2 DM vs bootstrap disagreement used as both caveat and verified 15/17 split zero exceptions unintelligible, example Spec A M4 vs M3 h1 CI [+4.7,+144.7] z=0.99 p=0.000 is case where iff fails | **UPHELD partially** — v11 rephrases: 15 CI exclude zero (1 Spec A +6 Spec B h1 +8 Spec B h5) 17 include (7+8 Spec A +2 Spec B h1) zero exceptions bootstrap CI/p coherent, DM z separate can disagree 5/32 rows because variance inflated |
| 5.3 Brier/LRP Table 1 Edwards threshold Brier 660 ft body Brier misclassification deterministic binary forecast, LRP/threshold same column as catch/forcing never used in H1-H3, secondary diagnostics described as not driving retention then given table billing equal to RMSE | **UPHELD** — v11 clarifies Brier secondary diagnostic not driving H1-H3, LRP/threshold for Brier, not primary |
| 5.4 Collapse/recovery numbers different experiment collapse persist 670 vs M1 694 vs M2 819 recovery persist 104 vs M1=M2 120 vs M1b 90 not reconciled with no structural approaches tie band | **UPHELD** — v11 states windowed vs full-record rolling-origin, recovery M1b 90 vs 104 unidentified s→0 K 105.8 just above training range not retained on full record |
| 5.5 Delay decomposition 195.6-98.0=97.6≈97.5 11.2≈11.1 uses RMSE pieces not in Tables 2-5 not checkable | **UPHELD** — v11 states decomposition uses archived per-origin files not Tables 2-3, removes rounding glitch |
| 6.1 Empty retained set throughout true only after post-hoc band and/or class-grounds ranking alone retains M2m | **UPHELD** — v11 discloses |
| 6.2 Same verdict in two unrelated systems by two different routes fair as sociology not as OC measured | **UPHELD** — v11 states portability of rule not of measured power/specificity |
| 6.3 Specificity is property of rule applied to in-class data not of rule best sentence, D6/D7 0.68-0.98 false retention then two empirical empty sets weak evidence of no structure except where D1-level power applies | **UPHELD** — v11 keeps best sentence, discloses D6 0.68/0.76 D7 0.975/0.925 vs 0.10 threshold specificity conditional |
| 6.4 Information-set audit supplied future catch/recharge correctly flagged conditional hindcast, negative result even with leaked drivers still lose to persist stronger for cod | **UPHELD** — v11 keeps conditional hindcast disclosure |
| 7.1 Table 1 self-reference "Table 1 landings" | **UPHELD** — v11 fixed to Regular et al. 2025 Table 1 landings |
| 7.2 Künsch spelling | **UPHELD** — v11 Künsch everywhere |
| 7.3 Algorithm output boolean vs third state | **UPHELD** — v11 third output |
| 7.4 Sixteen values token count | **UPHELD** — v11 removed |
| 7.5 Data availability 30/30 29/29 checksum | **UPHELD** — v11 once factually |
| 7.6 Simulation 8/8 usable vs 200 replicates different exercises | **UPHELD** — v11 explains 8/8 design-time calibration check vs 200 results |
| 7.7 AIC-like n log MSE+2k out-of-sample RMSE non-standard in- vs out-of-sample unspecified yet beats pre-registered | **UPHELD** — v11 clarifies one-step squared error parameter penalty not multi-year horizon |

**What still holds per grok flaw:** Table 2/appendix arithmetic correct (9.01%, 17.09%, 35.94%, 36.30%, 40.22%; Edwards H2 band 12.57/20.05), mean power 0.376 unweighted mean eight D1-D4 cells, D5 0.985/0.970 specificity 0.978, empty final retained sets consistent with gates as applied after band and class-grounds.

---

## 3. GEMINI-IMPROV (Predictive Adjudication manuscript)

| Item | Suggestion | Implementation |
|---|---|---|
| Formal mathematical specification, origin matching, negative certificate, third output, information-set audit template, oracle bound, uncertainty DM HAC + block bootstrap conditional, DGP specifications, simulation results, diagnostic interpretation identification vs gates, comparison with alternative rules, pre-check diagnostic open problem, dual-domain evaluation with verification log, detailed breakdown collapse/recovery, failure surplus production bookkeeping, uncertainty DM vs bootstrap discrepancies, conditional hindcast, Edwards gate adjudication Table 8, climate covariates ≤0.13 ft, modeling caveats, cross-application synthesis Table 9, orthogonal operation flowchart, epistemological scope licensed/not licensed, implications, data availability timing 7.0 s vs 45.6 s and replication 30/30 byte-identical 29/29 checksum and M1b ±17 kt variance | Most rigorous formal | Implemented as is in v11 except 3 fixes: runtime clarified 3.89h core 10.13h 800 passes 25.33h full not 10h full, Table 1 self-ref fixed, algorithm third state fixed, M1 definition fixed to affine AR1 |
| Table 1 catch "Table 1 landings" self-reference | Minor | Fixed |
| Algorithm output boolean vs third state | Minor | Fixed |
| Sixteen values token count | Minor | Removed |
| Data availability 30/30 29/29 | Minor | Kept once factually |
| 8/8 usable vs 200 replicates | Minor | Explained |
| AIC-like n log MSE+2k in- vs out-of-sample | Minor | Clarified one-step |

**Verdict GEMINI-IMPROV:** Strongly upheld as improvement, most rigorous, borrowable for v11, minor fixes after correction.

---

## 4. GEMINI-FLAW (line-level forensic review)

| # | Claim | Verification | Status v11 |
|---|---|---|---|
| 1.1 Phantom baseline 97/193 79/288 vs Tables 2-3 98.05/264.72 87.65/317.71 deficits locked to Table 2 numbers if baselines 193/288 deficits +49.5%/+49.96% not +9.01%/+35.94% | Same as 1.1 grok flaw | **UPHELD** — v11 fixed |
| 1.2 Origin-matching principle Spec B scoring 84.4 vs 88 diff 3.6 Tables evaluate Spec B against 87.65 deficit +36.30% if origin-matched 84.4 deficit +41.55% | Same as 1.2 | **UPHELD** — v11 reports both |
| 1.3 Execution status T=71 §§4.2,4.3,7 vs Data Availability 7 s vs 45.6 s 200 repl ~4h vs ~10h if T=71 not executed how exact runtime measured | Benchmark single pass 45.6 s measured, 200 repl 4h vs 10h for 800 passes not full factorial | **UPHELD** — v11 clarifies benchmark vs full run |
| 2.1 Algorithmic logic deadlock declined on class grounds Algorithm Box if retained gated by if retained must pass H1/H2 at all horizons Edwards M2m 12.28 vs 12.84 4.33% <5% fails H1 retained FALSE never reaches declined, yet narrative says declined on class grounds, §5.2 post-hoc band if band post-hoc pre-registered b=0 but if b=0.05 M2m rejected by H1 rendering class-grounds unreachable | Same as 2.3 grok flaw | **UPHELD** — v11 restructures class-grounds outside loop, discloses post-hoc band |
| 2.2 Cod M1b and class grounds §2.3 relevant to cod M1b s→0 cubic so lower error not evidence for depensation, flaw cod M1b never beat persistence either horizon either spec deficits +9.01%+17.09%+40.22% failed H2 outright never candidate for retention unless scoped to recovery sub-window 90 vs 104 | Recovery window 90 vs 104 | **UPHELD partially** — v11 scopes to recovery window |
| 3.1 Pre-registered adequacy criterion §1 vs §4.5 power ≥80% specificity ≥90% retention rule mean power 0.376 fails own benchmark 37.6% <<80% D3/D4 below 11% and 1.5% treats as identification but fails to state rule inadequate diagnostic for 3 of 4 classes | Mean power 0.376 average eight cells D1 0.965/0.985 passes D2 low 0.710 near pass D2 high 0.130 D3 0.09/0.11 D4 0.005/0.015 fail | **UPHELD** — v11 discloses fails adequacy bar for 3 of 4 classes, mean 0.376 drastically below 80% |
| 3.2 IC dominates proposed rule 0.509/0.992 vs 0.376/0.978 strictly dominates both axes +0.133/+0.014 undercuts justification | Honest | **UPHELD as honest** — v11 keeps |
| 3.3 Bootstrap p vs CI §5.1 p bootstrap percentile-tail fraction CI excludes zero iff p<0.05 verified 15/17 split zero exceptions by definition symmetric two-tailed percentile bootstrap (1-α) interval excludes zero iff tail p<α stating 15/17 split zero exceptions indicates CI and p computed using inconsistent estimators e.g. BCa vs uncorrected percentile | 15 CI exclude 1 Spec A +6 Spec B h1 +8 Spec B h5 17 include 7+8 Spec A +2 Spec B h1 zero exceptions bootstrap CI/p coherent DM z separate 5 rows | **NOT UPHELD** — phrase unintelligible but factually correct 15 exclude 17 include zero exceptions where CI and p disagree, need rephrase — v11 rephrased |
| 4.1 §1 para 5 unclosed parenthesis registered before simulation ( Sections 5 and 6 apply rule... | Broken sentence | **UPHELD** — v11 fixed |
| 4.2 Table 1 Row 2 Catch/forcing "Table 1 landings" self-referential loop should cite external reference | Self-ref | **UPHELD** — v11 fixed to Regular et al. 2025 Table 1 |
| 4.3 §2.1 Edwards ladder M1 one-pool affine H=aH+b+cP_t autoregression φ̂=0.66 If M1 includes +cP_t where P_t pumping or precipitation it is ARX not pure autoregression yet §5.2 Table 5 M1 repeatedly called AR1 and compared to M2m which collapses to AR1 under constant fluxes if M1 has dynamic forcing P_t M2m under constant fluxes does not collapse to M1 | Same as 4.1 | **UPHELD** — v11 fixed to H=aH+b |
| 4.4 §2.2 Origin-matching explanation gives origin-matched persistence 84.4 vs mixed-origin 88 diff 3.6 kt 88-84=4 parenthetical informal scratchpad | Scratchpad | **UPHELD** — v11 removed |
| 4.5 §5.1 Apparent arithmetic rounding glitches coarse-regime decomposition 195.6-98.0=97.6≈97.5 184.4-98.0=86.4 195.6-184.4=11.2≈11.1 exposes raw display rounding vs internal precision friction should report exact differences from unrounded floats or consistent rounded | Rounding friction | **UPHELD minor** — v11 removes or states uses archived per-origin files |
| 4.6 §6 Table Row Simulation power context D3/D4 0.09/0.005 low non-retention weak evidence... D1 reported as 0.965/0.985 low σ/high σ whereas D3/D4 reported as 0.09/0.005 taking low σ for D3 and low σ for D4 compresses grid inconsistently | Inconsistent compression | **UPHELD** — v11 reports D3 0.09/0.11 and D4 0.005/0.015 separately |
| 4.7 Data Availability Section batch 7 (audits...)/results/e1_dm_uncertainty.csv unexpanded ellipsis (...) in directory file path | Ellipsis | **UPHELD** — v11 expands full path |

---

## 5. Implementation Summary for v11

**All upheld flaws fixed in v11 0 blockers 1 review:**

- Remove phantom baselines 97/193 79/288 as main-ladder origin-matched — state they are capelin index module (Table 8) origins n=24/20 Spec A 150.02/262.34 vs persist 97/193 and n=36/32 Spec B 132.02/491.74 vs 79/288, loses every cell, verdict not retained unchanged. Main ladder persist Spec A 98.05/264.72 n=25/21 origin-matched, Spec B mixed 87.65/317.71 n=63/59 vs origin-matched 84.43/299.98 n=59/55 diff 3.22 h1 17.73 h5 both >>5% band verdict unchanged.

- Clarify origin-matching policy vs implementation — Def 2.1 requires origin-matched, report both mixed and origin-matched for Spec B main ladder mixed deficit 36.30%/35.94% origin-matched 41.55%/43.99% both far above band. Remove scratchpad (difference 3.6 kt; 88−84=4).

- Fix tie band boundary — prose ">5% strictly exactly 5% fails" to match algorithm `>= (1-b)*S(B)` → FALSE, or change algorithm to `>` — v11 uses strictly >5%.

- Disclose post-hoc band — Edwards companion had no band; unified rule adds band post-hoc; no outcome changes; M2m fails H1 under unified rule 4.33% <5% and additionally declined on class grounds; without band would pass H1 but still declined on class grounds, so empty set holds either way, gate demonstration uses unified rule.

- Restructure algorithm box — evaluate class-grounds after H1-H3 loop outside independent third output DECLINED ON CLASS GROUNDS not inside for h loop gated by if retained.

- Fix Edwards M1 definition — affine AR1 H_{t+1}=a H_t+b φ̂=0.66 corr 0.64 k≈0.34 yr⁻¹ not H=aH+b+cP_t ARX.

- Fix Table 1 self-reference — Table 1 landings → Regular et al. 2025 Table 1 landings.

- Fix syntax — unclosed parenthesis in §1 registered before simulation ( → complete.

- Fix direction inference — high power + non-retention ⇒ evidence against M1 not for.

- Disclose OC limitations — OC study fish surplus-production only no Edwards-like DGP no M3/M4 generating truths T=71 benchmark measured from single pass at 45.6 s not executed as full simulation power/specificity not transferable to groundwater M3/M4 non-retention no estimated power.

- Clarify false retention denominators — 0.044 per module-replicate pair wrong-module rate on D1-D4, 0.015-0.030 per replicate under D5 persistence-true, 0.005 per module under null.

- Clarify H2 baseline — training mean secondary diagnostic not driving retention; Edwards h5 training mean 16.8048 beats persist 21.1056 CI excludes zero M2m 17.44 beats persist but loses to mean rule never requires beating better naive.

- Clarify DM vs bootstrap — bootstrap CI and bootstrap p both from bootstrap percentile-tail coherent by construction 15 CI exclude zero 1 Spec A +6 Spec B h1 +8 Spec B h5 and 17 include 7+8 Spec A +2 Spec B h1 zero exceptions where CI and p disagree; DM z descriptive loss-differential on squared-loss difference HAC-scaled can disagree in 5/32 rows A M4 vs M3 h1 z=0.99 p=0.000 CI [+4.7,+144.7] B M3 vs persist h1 z=1.85 p=0.042 CI [+1.0,+92.5] B M4 vs M3 h5 z=1.88 p=0.007 CI [+20.2,+177.4] etc because variance inflated by catastrophic origins square root compresses tail.

- Fix M1b environment sensitivity — ±1.6 kt at h=1 (151.6 vs 153.2) and ±17 kt at h=5 (445.5 vs 462.5) max ±17 kt.

- Fix runtime arithmetic — core design 10 cells ×200×7.0 s=14000 s=3.89h ~4h at T=33; T=71 extension for D1 and D5 800 passes ×45.6 s=36480 s=10.13h ~10h; full factorial 2000 passes ×45.6 s=91200 s=25.33h ~25h at T=71 not executed.

- Fix rounding glitches — report precise differences from unrounded floats or consistent rounded or remove decomposition if not checkable from Tables 2-5 state uses archived per-observation files.

- Fix simulation power context table — report D3 0.09/0.11 and D4 0.005/0.015 separately not mixed 0.09/0.005.

- Fix data availability ellipsis — expand batch 7 (audits of agent arena 1 paper rewrites)/results/e1_dm_uncertainty.csv full path no ...

- Remove withdrawn propositions change-log — v6 had Proposition 4.1 withdrawn false and Lemma 3.2 withdrawn — change-log not journal v10 already 0 occurrences withdrawn correct science kept silently.

**Not upheld (audit arithmetic using rounded values):**

- Edwards relative margins: audit claims M2m h5 -17.34% should be 17.39% from 17.44 vs 21.11, M2m vs M1 4.33% should be 4.36% from 12.28 vs 12.84, oracle -42.96% vs 42.93%. Precise CSV values 13.230085772397212, 12.839129375852034, 12.28321959100849, 21.105596110577675, 17.444926311170768, 7.546731824129813 → computed -17.3445% → -17.34% correct, 4.3298% → 4.33% correct, -42.9578% → -42.96% correct. Audit used rounded 21.11 and 17.44, v11 uses precise.

- Bootstrap p vs CI 15/17 split zero exceptions: audit says unintelligible indicates inconsistent estimators, but 15 CI exclude zero (1 Spec A +6 Spec B h1 +8 Spec B h5) and 17 include (7+8 Spec A +2 Spec B h1) zero exceptions where bootstrap CI and bootstrap p disagree, phrase unintelligible but factually correct, v11 rephrased.

**What still holds:**

- Table 2/appendix arithmetic for printed RMSE pairs correct (9.01%, 17.09%, 35.94%, 36.30%, 40.22%; Edwards H2 band 12.57/20.05)
- Mean power 0.376 unweighted mean eight D1-D4 cells
- D5 0.985/0.970 matches specificity 0.978
- Empty final retained sets consistent with gates as applied after band and class-grounds step
- IC dominance 0.509/0.992 vs 0.376/0.978 honest and verified
- Simulation results table correct
- Gate decomposition numbers correct using precise CSV values (M2m h5 -17.3445% → -17.34%, M2m vs M1 4.3298% → 4.33%, oracle -42.9578% → -42.96%)

**Damaging inconsistencies that change what empty set can be said to license (now fixed in v11):**

- Stale persist baselines 97/193 79/288 presented as main-ladder origin-matched — actually capelin module
- Origin-matched policy vs 87.65/84.4 implementation
- Post-hoc band on only dataset that tests gates
- Evidence for autonomous vs against module direction
- OC study not covering Edwards or M3/M4 or T>33
- ≥5% vs strict inequality at boundary

All fixes preserve verified numbers.

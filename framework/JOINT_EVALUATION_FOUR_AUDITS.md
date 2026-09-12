# Joint Evaluation of Four Framework Audits — Verified Against Source

**Date:** 2026-09-12  
**Basis:** `framework/paperF1_retention_framework_v10.md` (388 lines, style scan 0 blockers), source CSVs `wave_e_cod/results/rolling_summary.csv` (Spec A regime+na), `xte_rolling_summary.csv` (Spec B), `wave_e_edwards/results/rolling_summary.csv`, `sim_retention_power.csv`, `sim_misspecified_D6D7.csv`, `batch 7/results/e1_dm_uncertainty.csv` (32 rows), `e3_dm_uncertainty.csv` (10 rows), `capelin_index_summary.csv`, `capelin_regime_summary.csv`, companion papers Abaee 2026a/b.

Audits evaluated:
- **GROK-IMPROV** — grok improvement audit (portable retention rule manuscript draft, 1st in file)
- **GROK-FLAW** — grok flaw audit (direct numerical contradictions, 2nd in file)
- **GEMINI-IMPROV** — gemini improvement audit (Predictive Adjudication..., 3rd in file)
- **GEMINI-FLAW** — gemini flaw audit (line-level forensic review, 4th in file)

---

## Executive Summary

All four audits agree on core scientific result: **empty retained set** on three objects, gate decomposition correct for printed RMSE pairs, simulation power/specificity numbers correct, information criterion dominance honest. **15/15 primary scores, 8 percentages, 12 simulation figures verified** against CSVs.

**Material flaws upheld (require fix in v11):**
- Phantom baselines 97/193 and 79/288 presented as main-ladder origin-matched — actually capelin index module (Table 8) origins n=24/20 and 36/32. Main ladder Spec A origin-matched 98.05/264.72 (naive n=25/21), Spec B mixed-origin 87.65/317.71 (n=63/59) vs origin-matched 84.43/299.98 (n=59/55) diff 3.6 kt. Framework v10 §2.2 line "Origin-matched baselines 97/193 and 79/288" is **false** for main ladder.
- Origin-matching policy vs implementation: Def 2.1 requires origin-matched, Table 3 Spec B uses mixed-origin 87.65 (deficit 36.3%) not 84.4 (deficit 41.55%). Need to report both and state verdict unchanged (both >>5% band).
- Tie band boundary: prose "by ≥5%" vs algorithm `>= (1-b)*S(B)` → exactly 5% fails. Inconsistent at boundary. Fix prose to ">5% strictly" or algorithm to `>`.
- Post-hoc band on only dataset that tests gates: Edwards companion had no band; unified rule adds band post-hoc. Without band, M2m h=1 vs M1 4.33% passes H1, empty set then depends on class-grounds decline, not H1. Disclosure required; statement "without modification" false for Edwards.
- Class-grounds check not in numbered gates, algorithm box logic deadlock: `if retained` gates H1/H2, then class-grounds inside same `for h` loop unreachable when H1 fails (M2m fails H1 at h=1, so never reaches class-grounds). Need restructure: evaluate class-grounds after H1-H3 loop, independent.
- Edwards M1 definition: v10 §2.1 writes `H_{t+1}=a H_t+b+c P_t (autoregression φ̂=0.66)` — three different models. If `c P_t` present, M1 is ARX not AR(1) and not nested with M2m. Correct is affine AR(1) `H_{t+1}=a H_t+b`, φ̂=0.66, corr=0.64, k≈0.34 yr⁻¹.
- Min sample 6 vs 12: six one-step transitions is absolute minimum after dropping no-carry years (capelin module origin 1991 Spec A, 1988 Spec B, <6 refusal guard), 12-year minimum is main ladder Spec B structural (n=59/55) vs 8-year naive (n=63/59). Both true, different objects.
- Runtime arithmetic: "7 s at T=33 vs 45.6 s at T=71 (200 replicates ~4 h vs ~10 h)" — full factorial 10 cells ×200×7 s=3.9 h matches ~4 h, same at 45.6 s=25.3 h not 10 h. 10 h corresponds to 800 passes (D1+D5 ×2σ×200) at T=71, not full factorial. Need clarify.
- M1b environment sensitivity: "±17 kt (151.6 vs 153.2 at h=1, 445.5 vs 462.5 at h=5)" — h1 diff 1.6 kt, h5 diff 17 kt, ±17 kt only five-year. Fix to "±1.6 kt at h=1 and ±17 kt at h=5, max ±17 kt".
- Direction inference: §6 "D1 high — non-retention strong evidence for autonomous" vs §8 "strong evidence against module where rule has power" — opposite. High power + non-retention ⇒ evidence **against** M1, not for. Fix direction.
- OC study fish-only, no Edwards-like DGP, portability of power/specificity not shown, D3/D4 low power mapped onto J-17 stock-flow without basis. Need disclosure.
- False retention denominators: 0.044 per module-replicate pair on D1-D4 wrong-module rate, D5 specificity 0.985/0.970 ⇒ 0.015-0.030 per replicate, 0.005 per module under null — three different denominators listed as if one series. Need clarify.
- H2 baseline only persistence though two baselines exist: Edwards h5 training mean 16.80 beats persist 21.11 CI excludes zero, M2m 17.44 beats persist but loses to mean, rule never requires beating better naive. Need state training mean secondary diagnostic.
- DM vs bootstrap: phrase "CI excludes zero iff p<0.05 verified 15/17 split zero exceptions" unintelligible without definition; example Spec A M4 vs M3 h=1 CI [+4.7,+144.7] z=0.99 p=0.000 is exactly case where iff would fail if DM p used, but CI and bootstrap p are coherent by construction, DM z separate can disagree in 5/32 rows. Need rephrase.
- Smaller defects: Table 1 "Table 1 landings" self-reference → "Regular et al. 2025 Table 1", algorithm output boolean vs third state, "sixteen values" token count, data availability "30/30 files byte-identical, 29/29 checksum", "8/8 usable replicates" vs 200 replicates different exercises, AIC-like n log MSE+2k in- vs out-of-sample unspecified.

**Flaws not upheld (audit arithmetic using rounded values):**
- Edwards relative margins: audit claims M2m h5 −17.34% should be 17.39% from 17.44 vs 21.11, M2m vs M1 4.33% should be 4.36% from 12.28 vs 12.84, oracle −42.96% vs 42.93%. Precise CSV values: persist h1 13.230085772397212, M1 12.839129375852034, M2m 12.28321959100849, persist h5 21.105596110577675, M2m h5 17.444926311170768, oracle 7.546731824129813. Computed: M2m h5 vs persist −17.3445% → −17.34% correct, M2m vs M1 4.3298% → 4.33% correct, oracle −42.9578% → −42.96% correct. Audit used rounded 21.11 and 17.44, we use precise, so our numbers stand.

---

## Audit 1: GROK-IMPROV (portable retention rule manuscript)

**Nature:** Proposed upgraded manuscript, not flaw list. Well-structured, formal academic, no diary, no version refs. Abstract states rule, audit, simulation, dual-domain empty set, gates load-bearing only second domain, specificity conditional, IC dominates, diagnostic open.

**Evaluation:**
- **Strengths:** Formal academic tone, correct algorithm box, origin-matched explanation (84.4 vs 88 diff 3.6), third output declined on class grounds explained, information-set audit template, oracle bound, uncertainty via DM HAC + block bootstrap conditional, DGP table, results table, reading identification vs gates, comparison table, open problem pre-check diagnostic, verified numbers, no pooling.
- **Issues vs source:** Same phantom baseline issue? Check: GROK-IMPROV Table 1 catch/forcing column says "Table 1 landings" self-reference — flaw. M1 definition includes K optimised [max S+10,5000] multi-start 500 lower bound 50.8 ≈91 recovery flat MSE 127.4→149.9 correct. M1b s→0 numerical 2.1e-23 coarse 9.4e-6 annual r pinned 2.0 zero-threshold cubic a(S)=S/K correct. Six transitions origin 1991/1988 correct. Edwards M1 affine H_{t+1}=a H_t+b+c P_t (same inconsistency as v10) — needs fix to a H_t+b. Origin-matched baselines 97/193 and 79/288 not present in GROK-IMPROV (good). Runtime "7 s vs 45.6 s (200 replicates ~4 h vs ~10 h)" same arithmetic error as v10 — needs fix to 25 h full factorial, 10 h for 800 passes.
- **Verdict:** **Largely upheld as improvement**, fixes many diary issues, but inherits 3 material flaws (M1 definition, runtime arithmetic, Table 1 self-reference). Borrowable: algorithm box structure, formal tone, gate decomposition.

---

## Audit 2: GROK-FLAW (direct numerical contradictions)

**Claim-by-claim verification:**

| # | Claim | Source check | Verdict |
|---|---|---|---|
| 1.1 | Origin-matched baselines 97/193 and 79/288 vs tables 98.05/264.72 and 87.65/317.71 | `capelin_index_summary.csv`: ncam2016 M_cap_index n=24/20 RMSE 150.02/262.34, naive persist 98.05/264.72; xteNCAM M_cap_index n=36/32 RMSE 132.01/491.73, naive persist 87.65/317.71. Origin-matched persist for capelin module is 97/193 (Spec A, n=24/20) and 79/288 (Spec B, n=36/32) per paperE1 v10 Table 8. Main ladder persist is 98.05/264.72 and 87.65/317.71. Framework v10 §2.2 says "Origin-matched baselines 97/193 and 79/288" as if main ladder — **false**. | **UPHELD** — fix required |
| 1.2 | Spec B origin-matched 84.4 vs mixed 88 diff 3.6, Table 3 uses 87.6 still quotes 84.4/88/3.6, if origin-matched M1 119.47 vs 84.4 deficit 41.55% not 36.3%, parenthetical 88−84=4 contradicts 88−84.4=3.6 | `e1_dm_uncertainty.csv` B1 M1 vs persist origin-matched 84.42788518380742 vs mixed 87.64964527857667. Gap 35.038348275056165 vs 84.4, deficit 41.5% vs 36.3%. Parenthetical "88−84=4" is informal scratchpad left in text — diary. | **UPHELD** — clarify both deficits, remove scratchpad |
| 1.3 | Edwards margins −17.34% should be 17.39% from 17.44 vs 21.11, 4.33% should be 4.36%, oracle −42.96% vs 42.93% | Precise CSV: 13.230085772397212, 12.839129375852034, 12.28321959100849, 21.105596110577675, 17.444926311170768, 7.546731824129813 → computed −17.3445% → −17.34% correct, 4.3298% → 4.33% correct, −42.9578% → −42.96% correct. Audit used rounded values. | **NOT UPHELD** — our numbers correct using precise |
| 1.4 | M1b env sensitivity ±17 kt (151.6 vs 153.2 h1 diff 1.6, 445.5 vs 462.5 h5 diff 17) ±17 only five-year | Check: 151.6 vs 153.2 diff 1.6, 445.5 vs 462.5 diff 17.0 | **UPHELD** — fix to ±1.6 h1 and ±17 h5 |
| 1.5 | Runtime 7 s vs 45.6 s (200 repl ~4 h vs ~10 h) full factorial 5×2×200×7 s≈3.9 h matches ~4 h, same at 45.6 s≈25 h not 10 h, ratio mismatch, T=71 not executed so 45.6 s /10 h unreconciled | 10 h corresponds to 800 passes (D1+D5 ×2σ×200) ×45.6 s=10.13 h, full factorial 2000 passes ×45.6=25.33 h | **UPHELD** — clarify |
| 2.1 | Tie band prose ≥5% vs algorithm >= (1-b)*S(B) → exactly 5% fails, disagree at boundary | Def 2.1 says "by ≥5%", algorithm says `>= (1-b)*S(B)` → FALSE → exactly 5% fails | **UPHELD** — make consistent (>5% strictly) |
| 2.2 | Band post-hoc on dataset that makes gates load-bearing, §5.2 post-hoc band no outcome changes vs §1/8 without modification, without band M2m passes H1, empty set depends on class-grounds not H1, undercuts §6 load-bearing | Edwards companion had no band, unified rule adds band post-hoc, without band M2m h1 vs M1 4.33% passes H1, still declined on class grounds, empty set holds either way, but gate demonstration uses unified rule | **UPHELD** — disclose post-hoc, clarify dependency |
| 2.3 | Class-grounds not in numbered gates, pseudocode inside for h loop unclear, can change output after RMSE gates pass, same algorithm vs judgement different procedures | Algorithm box: `if retained and M reduces... declined on class grounds` inside `for h` loop gated by `if retained` → unreachable when H1 fails (M2m fails H1 at h=1) | **UPHELD** — restructure outside loop |
| 2.4 | H2 baseline only persistence though two naive baselines exist, Edwards h5 training mean 16.80 beats persist 21.11 CI excludes 0, M2m 17.44 beats persist but loses to mean, rule never requires beating better naive, cod training-mean not in Tables | Training mean secondary diagnostic, not driving retention per Definition 2.1 | **UPHELD** — clarify secondary |
| 2.5 | Oracle asymmetric: Edwards M2_oracle non-retainable bound, cod M2-M4 already receive future catch never framed as bound, information-set template not same | Both receive future drivers as supplied, oracle makes bound explicit on Edwards | **UPHELD** — clarify both conditional hindcasts |
| 3.1 | OC study fish only, no Edwards-like DGP, §6 maps D3/D4 low power onto J-17 stock-flow, portability of power/specificity not shown | D1-D7 are Schaefer/Allee/catch, surplus imported unmodified, T=33 Spec A, no heads/recharge/pumpage DGP | **UPHELD** — disclose fish-only |
| 3.2 | Wrong direction inference: §6 D1 high — non-retention strong evidence for autonomous vs §8 strong evidence against module | High power + non-retention ⇒ evidence against M1, not for | **UPHELD** — fix direction |
| 3.3 | H_sim vs table: retain true module materially above false-retention, D3 0.09/0.11 below 20% chance, D4 0.005/0.015, D2 high σ 0.130, mean power 0.376 average of eight cells including near-failures, only true for D1 (and D2 low) | H_sim holds only for D1 and D2 low noise | **UPHELD** — disclose |
| 3.4 | False retention 0.044 vs D5: D5 specificity 0.985/0.970 ⇒ false 0.015-0.030 per replicate, 0.044 different denominator (wrong-module rate D1-D4), §7 lists 0.044, 0.025/replicate, 0.005/module as if one series | Need clarify denominators | **UPHELD** |
| 3.5 | M3/M4 never generating truths, T=71 never run, disclosed but then applications include M3/M4 on 71- and 90-year series, non-retention no estimated power | Limitation disclosed, need emphasize | **UPHELD** |
| 3.6 | IC dominates pre-registered rule (0.509/0.992 vs 0.376/0.978) on same archived scores, tension with presenting rule as instrument that licenses verdict | Already disclosed honestly, keep | **UPHELD as honest, not flaw** |
| 4.1 | Edwards M1 three different models: H_{t+1}=a H_t+b+c P_t covariate vs autoregression φ̂=0.66 vs AR(1), if c P_t real driver M1 not AR(1) not nested | Correct is affine AR(1) H_{t+1}=a H_t+b | **UPHELD** |
| 4.2 | Cod M1b equation never fully stated, s→0 zero-threshold cubic ambiguous | Need full equation S_{t+1}=S_t+r S_t(1-S_t/K) a(S_t)-C̄, a(S_t)=(S_t-s)/(K-s), s→0 ⇒ a(S)=S/K cubic | **UPHELD** |
| 4.3 | Min sample 6 vs 12: six one-step transitions matching <6 guard vs 12-year min structural vs 8-year naive cannot both be operational | Six is absolute min for capelin after dropping no-carry years, 12-year main ladder Spec B structural, 8-year naive | **UPHELD** — clarify |
| 4.4 | Five structural + two naive = seven vs Edwards five + oracle + two baselines, oracle inside ladder excluded by fiat, not five-rung ladder unchanged | Edwards five structural + oracle diagnostic cannot retain + two baselines = eight total, five-rung structural unchanged | **UPHELD** — clarify |
| 4.5 | M2 comparator: cod M2 vs M1 (not M1b) with M2 vs M1b alternative, Edwards both M2 and M2m vs M1, next-simpler not single map | Clarify comparator map | **UPHELD** |

---

## Audit 3: GEMINI-IMPROV (Predictive Adjudication...)

**Nature:** Detailed formal manuscript, mathematical specification, tables, algorithm box, origin matching, negative certificate definition, third output declined on class grounds, information-set audit template, oracle bound, uncertainty DM HAC + block bootstrap conditional, DGP specifications, simulation results, diagnostic interpretation identification vs gates, comparison with alternative rules, pre-check diagnostic open problem, dual-domain evaluation, summary verification log.

**Evaluation:**
- **Strengths:** Most formal of four, correct math notation, defines RMSE origin-matched, defines H1-H3 with formulas, algorithm box with retained_flag, origin matching explanation with example Spec B 84.4 vs 88 bias 3.6 kt, negative certificate definition machine-verified finding that no structural module satisfies Def 2.1, third output declined on class grounds with mathematical collapse to AR(1) drift and zero-threshold cubic, information-set audit table with classification, oracle bound 7.55 vs 13.23 −42.96% and −49% at h5, uncertainty DM HAC + block bootstrap p=2·min tail fraction, DGP table with parameters and ladder class, simulation results table with power/specificity/false retention, diagnostic interpretation identification failures not gates (33% D3 and 18% D4 even dropping H1 and band, random guessing 20% vs 3.8% stock-flow), fragility of specificity under misspecification, comparison table with mean power/specificity/false retention under misspecification, pre-check diagnostics dispersion Spearman 0.52 and best-module margin 0.88 circular and misclassifies D3, dual-domain evaluation with summary verification log, detailed performance breakdown collapse/recovery windows with error decomposition 73.6 of 121.3 at h1 and 693.3 of 730.8 at h5 and coarse-regime decomposition 195.6−98.0≈97.5 etc, failure of surplus production bookkeeping P_t^apparent = S_{t+1}−S_t+C_t, uncertainty quantification DM vs bootstrap discrepancies with examples, conditional hindcast status, Edwards detailed gate adjudication Table 8 with H2/H1 margins, climate covariates ≤0.13 ft, modeling caveats San Antonio+Uvalde lumped, cross-application synthesis Table 9, orthogonal operation of retention rule with flowchart, epistemological scope licensed/not licensed, implications for practice, data and code availability with timing 7.0 s vs 45.6 s and independent replication 30/30 byte-identical 29/29 checksum and M1b ±17 kt variance.
- **Issues vs source:** Same runtime arithmetic error (7 s vs 45.6 s ~4 h vs ~10 h, full factorial ~25 h not 10 h) — needs fix to 800 passes ~10 h. Table 1 catch "Table 1 landings" self-reference — should be "Regular et al. 2025 Table 1". Algorithm output `{retained | not retained | declined on class grounds}` but `retained` boolean never set to third state — needs restructure. "Sixteen values" for four CIs token count — minor. Data availability "30/30 files byte-identical, 29/29 checksum" — provenance once factual allowed. "8/8 usable replicates" vs 200 replicates different exercises — need explain 8/8 is design-time calibration check, 200 is results table. AIC-like n log MSE+2k on out-of-sample RMSE non-standard in- vs out-of-sample unspecified yet beats pre-registered — need clarify IC scores one-step squared error with parameter penalty, not multi-year horizon.
- **Verdict:** **Strongly upheld as improvement**, most rigorous, borrowable for v11: mathematical formalism, DGP table, gate decomposition, flowchart, epistemological scope. Minor fixes needed (runtime, self-reference, algorithm third state).

---

## Audit 4: GEMINI-FLAW (line-level forensic review)

**Claim-by-claim verification:**

| # | Claim | Source check | Verdict |
|---|---|---|---|
| 1.1 | Phantom baseline contradiction §2.2 & §8 origin-matched 97/193 and 79/288 vs Tables 2,3,Appendix Spec A 98.05/264.72 Spec B 87.65/317.71, deficits locked to Table 2 numbers, if baselines actually 193 and 288 deficits would be +49.5% and +49.96% not +9.01% and +35.94% | Same as GROK-FLAW 1.1 — 97/193 and 79/288 are capelin module (n=24/20 and 36/32), not main ladder. Main ladder persist 98.05/264.72 and 87.65/317.71. | **UPHELD** |
| 1.2 | Violation of origin-matching principle Spec B scoring §2.2 origin-matched 84.4 vs mixed 88 diff 3.6, Tables 2,3,Appendix evaluate Spec B against 87.65 (rounded 88) deficit +36.30% = (119.47-87.65)/87.65, if actually origin-matched 84.4 deficit +41.55% | Same as GROK-FLAW 1.2 — Table 3 uses mixed-origin, origin-matched control is 84.4, deficit 41.55% vs 36.30%, both >>5% band, verdict unchanged | **UPHELD** |
| 1.3 | Execution status T=71 §§4.2,4.3,7 vs Data Availability runtime 7 s vs 45.6 s (200 repl ~4 h vs ~10 h) — if T=71 not executed how exact runtime measured? | 45.6 s measured from single rolling pass at T=71 benchmark, 200 replicates ~4 h vs ~10 h for 800 passes (D1+D5 ×2σ×200), full factorial ~25 h, T=71 declared but not executed for full simulation | **UPHELD** — clarify benchmark vs full run |
| 2.1 | Algorithmic logic deadlock declined on class grounds §2.2 vs §2.3 & §5.2: Algorithm Box `if retained and M reduces... declined` gated by `if retained` must pass H1/H2 at all horizons, Edwards M2m RMSE 12.28 vs comparator 12.84 reduction 4.33% <5% fails H1 at h=1 so retained FALSE never reaches declined, yet §§2.3,5.2,6,8 say declined on class grounds, §5.2 concedes post-hoc band, if band post-hoc pre-registered algorithm b=0 but if b=0.05 M2m rejected by H1 rendering class-grounds unreachable, algorithm box and narrative incompatible | Same as GROK-FLAW 2.3 — need restructure class-grounds outside H1/H2 loop | **UPHELD** |
| 2.2 | Cod M1b and class grounds §2.3 relevant to cod M1b s→0 zero-threshold cubic so lower error not evidence for depensation, flaw cod M1b never beat persistence either horizon either spec deficits +9.01% +17.09% +40.22% failed H2 outright never candidate for retention so bringing up as example confusing unless scoped to unpooled post-collapse recovery sub-window where 90 vs 104 | M1b beats persistence on recovery window (train 1995-2007 test 2008-2015) 90 vs 104, but not on full rolling-origin Spec A/B, so class-grounds example should be scoped to recovery window or stated as zero-threshold cubic branch not evidence for depensation generally | **UPHELD partially** — clarify scope |
| 3.1 | Pre-registered adequacy criterion §1 vs §4.5: pre-registered operating standards power ≥80% specificity ≥90%, retention rule mean power 0.376 drastically fails own benchmark for power 37.6% <<80%, D3/D4 power below 11% and 1.5%, manuscript treats as identification but fails to state plainly rule inadequate diagnostic for 3 of 4 structural classes | Mean power 0.376 average of D1-D4 eight cells including near-failures, D1 0.965/0.985 passes 80%, D2 low 0.710 near pass, D2 high 0.130, D3 0.09/0.11, D4 0.005/0.015 fail, so rule fails adequacy bar for 3 of 4 classes | **UPHELD** — disclose failure |
| 3.2 | IC dominates proposed rule §4.5 retention 0.376/0.978 vs IC n log MSE+2k 0.509/0.992 strictly dominates both axes higher power +0.133 higher specificity +0.014, undercuts justification for complex multi-horizon ladder rule | IC dominates on archived scores, reported honestly, tension with presenting rule as instrument that licenses verdict | **UPHELD as honest, not flaw** — keep disclosure |
| 3.3 | Bootstrap p-values vs CI §5.1 p is bootstrap percentile-tail fraction CI excludes zero iff p<0.05 verified 15/17 split zero exceptions — by definition symmetric two-tailed percentile bootstrap (1-α) interval excludes zero iff tail p<α, stating 15/17 split zero exceptions indicates CI and p computed using inconsistent estimators (e.g., BCa vs uncorrected percentile) | Actually CI and p both from bootstrap percentile-tail, coherent by construction, 15 CI exclude zero (1 Spec A +6 Spec B h1 +8 Spec B h5) and 17 include (7+8 Spec A +2 Spec B h1), zero exceptions where CI and p disagree, DM z separate can disagree in 5 rows (A M4 vs M3 h1 z=0.99 p=0.000, B M3 vs persist h1 z=1.85 p=0.042, B M4 vs M3 h5 z=1.88 p=0.007 etc) | **NOT UPHELD** — 15/17 split means 15 exclude 17 include, zero exceptions where bootstrap CI and bootstrap p disagree, phrase unintelligible but factually correct, need rephrase |
| 4.1 | §1 para 5 unclosed parenthesis / missing text registered before simulation ( Sections 5 and 6 apply rule... | Check v10: line "Design, including thresholds separating adequate from inadequate instrument (power ≥80%, specificity ≥90%), registered before any synthetic series generated (Design registered before any synthetic series generated." — duplicate parenthesis, broken sentence | **UPHELD** — fix syntax |
| 4.2 | Table 1 Row 2 Column Catch/forcing "Table 1 landings" self-referential loop, should cite external reference | Table 1 Spec B catch = "Table 1 landings" self-reference | **UPHELD** — fix to "Regular et al. 2025 Table 1" |
| 4.3 | §2.1 Edwards ladder M1 one-pool affine H_{t+1}=a H_t+b+c P_t (autoregression φ̂=0.66... If M1 includes +c P_t where P_t pumping or precipitation, it is ARX not pure autoregression, yet §5.2 and Table 5 M1 repeatedly called AR(1) and compared to M2m which collapses to AR(1) under constant fluxes, if M1 has dynamic forcing P_t M2m under constant fluxes does not collapse to M1 | Same as GROK-FLAW 4.1 — correct is affine AR(1) H_{t+1}=a H_t+b | **UPHELD** |
| 4.4 | §2.2 Origin-matching explanation "...gives origin-matched persistence 84.4 kt versus mixed-origin 88 kt (difference 3.6 kt; 88−84=4)." parenthetical looks like informal scratchpad calculation left in text | Parenthetical "88−84=4" informal scratchpad, diary | **UPHELD** — remove scratchpad |
| 4.5 | §5.1 Apparent arithmetic rounding glitches "...coarse-regime decomposition 195.6−98.0=97.6≈97.5, 184.4−98.0=86.4, 195.6−184.4=11.2≈11.1" exposes raw display rounding vs internal precision friction, should report either exact differences from unrounded floating-point numbers or consistent rounded differences | 195.6 is rounded Table 4 196? Actually precise M4 195.572..., persist 98.049..., difference 97.523... ≈97.6≈97.5 shows rounding friction | **UPHELD minor** — report precise or consistent rounded |
| 4.6 | §6 Table Row Simulation power context D3/D4 0.09/0.005 low — non-retention weak evidence... D1 reported as 0.965/0.985 (low σ / high σ) whereas D3/D4 reported as 0.09/0.005 (taking low σ for D3 and low σ for D4) compresses grid inconsistently across table cell | D1 0.965/0.985 low/high σ, D3 0.09/0.11 low/high, D4 0.005/0.015 low/high, but table cell "0.09/0.005" mixes D3 low and D4 low, inconsistent | **UPHELD** — report as D3 0.09/0.11 and D4 0.005/0.015 separately |
| 4.7 | Data Availability Section "`batch 7 (audits...)/results/e1_dm_uncertainty.csv`" unexpanded ellipsis (...) in directory file path | Ellipsis in path | **UPHELD** — expand to full path |

---

## What still holds (from both flaw audits)

- Table 2/appendix arithmetic for printed RMSE pairs correct (9.01%, 17.09%, 35.94%, 36.30%, 40.22%; Edwards H2 band 12.57/20.05)
- Mean power 0.376 really is unweighted mean of eight D1-D4 cells
- D5 0.985/0.970 matches specificity 0.978
- Empty final retained sets consistent with gates **as applied after** band and class-grounds step
- IC dominance 0.509/0.992 vs 0.376/0.978 honest and verified
- Simulation results table correct
- Gate decomposition numbers correct using precise CSV values (M2m h5 −17.3445% → −17.34%, M2m vs M1 4.3298% → 4.33%, oracle −42.9578% → −42.96%)

**Damaging inconsistencies that change what empty set can be said to license:**
- Stale persist baselines 97/193, 79/288 presented as main-ladder origin-matched — actually capelin module
- Origin-matched policy vs 87.65/84.4 implementation
- Post-hoc band on only dataset that tests gates
- "Evidence for autonomous" vs "against module" direction
- OC study not covering Edwards or M3/M4 or T>33
- ≥5% vs strict inequality at boundary

---

## Fixes Required for v11 (journal-clean, formal)

1. **Remove phantom baselines 97/193 and 79/288 as main-ladder** — state they are capelin index module (Table 8) origins n=24/20 Spec A (150.02/262.34 vs persist 97/193) and n=36/32 Spec B (132.01/491.73 vs persist 79/288), module loses to origin-matched baseline every cell, verdict not retained unchanged. Main ladder persist Spec A 98.05/264.72 (n=25/21) origin-matched, Spec B mixed-origin 87.65/317.71 (n=63/59) vs origin-matched 84.43/299.98 (n=59/55) diff 3.6 kt, both >>5% band, verdict unchanged.

2. **Clarify origin-matching policy vs implementation** — Def 2.1 requires origin-matched, report both mixed and origin-matched for Spec B main ladder: mixed deficit 36.30% (119.47 vs 87.65) and origin-matched 41.55% (119.47 vs 84.43), both far above band. Remove scratchpad "(difference 3.6 kt; 88−84=4)".

3. **Fix tie band boundary** — prose ">5% strictly" (exactly 5% fails) to match algorithm `>= (1-b)*S(B)` → FALSE, or change algorithm to `>`. Make consistent.

4. **Disclose post-hoc band** — Edwards companion had no band; unified rule adds band post-hoc; no outcome change; M2m fails H1 under unified rule 4.33% <5% and additionally declined on class grounds; without band would pass H1 but still declined on class grounds, so empty set holds either way, but gate demonstration uses unified rule.

5. **Restructure algorithm box** — evaluate class-grounds after H1-H3 loop, outside, independent, output third state `DECLINED ON CLASS GROUNDS`, not inside `for h` loop gated by `if retained`.

6. **Fix Edwards M1 definition** — affine AR(1) `H_{t+1}=a H_t+b`, φ̂=0.66, corr=0.64, k≈0.34 yr⁻¹, not `H_{t+1}=a H_t+b+c P_t` ARX.

7. **Fix Table 1 self-reference** — "Table 1 landings" → "Regular et al. 2025 Table 1".

8. **Fix syntax** — unclosed parenthesis in §1 "registered before simulation (" → complete.

9. **Fix direction inference** — high power + non-retention ⇒ evidence **against** M1, not for.

10. **Disclose OC limitations** — OC study fish surplus-production only, no Edwards-like DGP, no M3/M4 generating truths, T=71 not executed (benchmark 45.6 s/pass measured from single pass, 800 passes ~10 h for D1+D5 ×2σ×200, full factorial 2000 passes ~25 h), power/specificity not transferable to groundwater, M3/M4 non-retention no estimated power.

11. **Clarify false retention denominators** — 0.044 per module-replicate pair wrong-module rate on D1-D4, 0.015-0.030 per replicate under D5 persistence-true, 0.005 per module under null.

12. **Clarify H2 baseline** — training mean secondary diagnostic, not driving retention; Edwards h5 training mean 16.80 beats persist 21.11 CI excludes zero, M2m 17.44 beats persist but loses to mean, rule never requires beating better naive.

13. **Clarify DM vs bootstrap** — bootstrap CI and bootstrap p both from bootstrap percentile-tail coherent by construction (15 CI exclude zero: 1 Spec A +6 Spec B h1 +8 Spec B h5, 17 include: 7+8 Spec A +2 Spec B h1, zero exceptions where CI and p disagree), DM z descriptive loss-differential on squared-loss difference HAC-scaled can disagree in 5/32 rows (A M4 vs M3 h1 z=0.99 p=0.000 CI [+4.7,+144.7], B M3 vs persist h1 z=1.85 p=0.042 CI [+1.0,+92.5], B M4 vs M3 h5 z=1.88 p=0.007 CI [+20.2,+177.4] etc) because variance inflated by catastrophic origins, square root compresses tail.

14. **Fix M1b environment sensitivity** — "±1.6 kt at h=1 (151.6 vs 153.2) and ±17 kt at h=5 (445.5 vs 462.5), max ±17 kt".

15. **Fix runtime arithmetic** — core design 10 cells ×200×7 s=3.9 h ~4 h at T=33, T=71 extension for D1+D5 800 passes ×45.6 s=10.13 h ~10 h, full factorial 2000 passes ×45.6 s=25.33 h ~25 h.

16. **Fix rounding glitches** — report precise differences from unrounded floats or consistent rounded: e.g., M4 195.572... vs persist 98.049... diff 97.523... etc, or remove decomposition if not checkable from Tables 2-5, state uses archived per-observation files.

17. **Fix simulation power context table** — report D3 0.09/0.11 and D4 0.005/0.015 separately, not mixed 0.09/0.005.

18. **Fix data availability ellipsis** — expand `batch 7 (audits of agent arena 1 paper rewrites)/results/e1_dm_uncertainty.csv` full path, no `...`.

19. **Remove withdrawn propositions change-log** — v6 had "Proposition 4.1 withdrawn false" and "Lemma 3.2 withdrawn" — change-log, not journal. v10 already has 0 occurrences of "withdrawn", correct science kept silently.

---

## Automated Scanner for Future

`framework/journal_style_automated_scan.py` implements all hard rules (version refs, self-correction, phantom, diary, methodological diary, editorial, metaphor apology) and soft reviews (coinage, intensifiers). Official gate `tools/manuscript_style_scan.py` 0 blockers required.

---

## Recommended v11 Edits (summary)

- §2.1: Edwards M1 = `H_{t+1}=a H_t+b` affine AR(1), not `+c P_t`
- §2.2: Remove "Origin-matched baselines 97/193 and 79/288" as main ladder; state they are capelin module; main ladder Spec B mixed 87.65/317.71 vs origin-matched 84.43/299.98 diff 3.6 kt
- Table 1: "Table 1 landings" → "Regular et al. 2025 Table 1"
- Def 2.1 prose: ">5% strictly" not "≥5%" to match `>= (1-b)*S`
- Algorithm Box: class-grounds check outside `for h` loop, after H1-H3
- §2.3: Scope M1b class-grounds to recovery window (90 vs 104) where it beat persistence, not full rolling-origin
- §5.1: Report both deficits for Spec B: 36.3% mixed and 41.55% origin-matched, verdict unchanged
- §5.2: Disclosure post-hoc band, no outcome change, M2m fails H1 4.33% and additionally declined on class grounds, without band would pass H1 but still declined
- §6: Fix direction "strong evidence against autonomous" not for
- §4: Disclose OC fish-only, no Edwards DGP, no M3/M4, T=71 not executed with clarified runtime 3.9 h core, 10.13 h for 800 passes at T=71, 25.33 h full factorial
- §4.5: Clarify false retention denominators 0.044 per module-replicate pair D1-D4, 0.015-0.030 per replicate D5, 0.005 per module null
- §5.1 uncertainty: Rephrase "15/17 split zero exceptions" → "15 CI exclude zero (1 Spec A +6 Spec B h1 +8 Spec B h5) and 17 include (7+8 Spec A +2 Spec B h1), zero exceptions where bootstrap CI and bootstrap p disagree; DM z separate can disagree in 5 rows"
- Data availability: Fix M1b sensitivity to ±1.6 h1 and ±17 h5, runtime to 3.9 h core, 10 h for 800 passes at T=71, 25 h full factorial, expand ellipsis path, remove duplicate byte-identical lines keep once factually
- §1 syntax: Fix unclosed parenthesis
- §6 power context: Report D3 0.09/0.11 and D4 0.005/0.015 separately
- Remove scratchpad "(difference 3.6 kt; 88−84=4)" and rounding glitches "195.6−98.0=97.6≈97.5"
- Ensure no "withdrawn propositions" change-log — v10 already clean

All fixes preserve verified numbers: Table 2/appendix arithmetic correct (9.01%, 17.09%, 35.94%, 36.30%, 40.22%; Edwards H2 band 12.57/20.05), mean power 0.376 unweighted mean eight D1-D4 cells, D5 0.985/0.970 specificity 0.978, empty final retained sets consistent with gates as applied after band and class-grounds.

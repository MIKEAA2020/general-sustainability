# Remaining Audit Points from Places Not Previously Scanned — Implemented in v12

**Search performed:** `find /home/user -type f -name "*.md" | xargs grep -l audit` — 60+ files. Previously scanned: `uploads/framework audits.txt` (four audits). Newly scanned: `audits_E1_E3/e1_audit_2026-09/E1_LINE_LEVEL_AUDIT.md`, `E1_AUDIT_ROUND1-9`, `E1_METHODS_FRAMING_ASSESSMENT.md`, `arena_agent_1/other documents/audits/joint_assessment_wave5.md`, `joint_assessments/DEEP_SCAN_RESIDUAL_POINTS.md`, `FINAL_EDITIONS_CONSOLIDATION_SCAN.md`, `BATCH5_JOINT_AUDIT_EVALUATION.md`, `audits_E1_E3/wave6/paperE1_cod_forecast_ladder.md`.

**All surviving points relevant to framework F1 implemented in v12 (0 blockers official scan).**

---

## A. E1_LINE_LEVEL_AUDIT.md (line-level audit of E1 v15)

| ID | Point | v12 Implementation |
|---|---|---|
| A1 | Table 9 DM z, bootstrap p, CI mutually inconsistent — 3 rows CI excludes zero while |z|<1.96, 4 rows p vs z mismatch, paper never says two procedures | v12 §5.1: DM z tests mean squared-loss differential, CI and p come from separate moving-block bootstrap of RMSE gap, square root compresses heavy tail two can disagree and bootstrap tighter; p = p_perc = 2·min{#(Δ*≤0),#(Δ*≥0)}/B, CI excludes zero iff p<0.05 verified 15 exclude (1 Spec A +6 Spec B h1 +8 Spec B h5) 17 include (7+8 Spec A +2 Spec B h1) zero exceptions CI/p coherent, DM z separate 5/32 rows disagree (A M4 vs M3 h1 [+4.7,+144.7] z=0.99 p=0.000 etc), DM not calibrated for design expanding-window overlapping near-nested smoothed target multiple comparisons relabeled descriptive loss-differential diagnostics |
| A2 | §3.5 summary "On Spec A no non-retention margin separates from zero" contradicted by next sentence M4-vs-M3 separates at h=1 on both specs | v12: "no Spec A margin against persistence has interval excluding zero" — insert against persistence |
| A3 | K lower-bound contradiction §2.2 K optimised [max+10,5000] 500 multi-start initialiser rather than lower bound vs §3.2 Table 10 r=0.458 K pinned at lower bound 500.0, Table 10 note "neither is reconciled here", plus catch treatments swapped coarse 5.00 vs annual 3.19, K lower bound 50.83 not 500, L-BFGS-B never moved off x0 because objective flat, flat-valley sweep MSE 127.4→149.9 over K∈[60,5000] | v12 §2.1: K optimised on [max_train S+10,5000] with 500 kt multi-start initialiser lower bound 50.8 general ≈91 recovery max_train S≈81, reported fits attain upper endpoint K=5000 where data prefer unbounded, M1 coarse C=5.00 r=0.458 K=500.0 resting at multi-start initialiser 500.0 (lower bound 50.8) not pinned, annual C=3.19 r=0.370 K=5000.0, M1b coarse K=105.8 annual K=129.8 interior valid, objective flat 127.4→149.9, catch-treatment values differ by ≤0.04 kt after displayed rounding archived values differ 120.5095 vs 120.5406 0.0311 etc, not mathematically invariant |
| A4 | Arithmetic slip 3.2 kt should be 3.6 §2.3 mixed-origin reading Table 6 88 exceeds controlled reading by 3.2, 88-84=4 using Table 9 precise 84.4 gives 3.6 figure 3.2 requires mixed 87.6 nowhere printed | v12: origin-matched 84.43 vs mixed 87.65 diff 3.22 h1 and 299.98 vs 317.71 diff 17.73 h5 precise, or 88 vs 84.4 diff 3.6 rounded |
| B1 | Seven-model ladder counted two ways Highlights seven-model ladder runs against two naive baselines implies 7+2=9 Definition 2.3 seven include two baselines 5+2 | v12: Five structural plus two naive baselines make seven models total cod, Edwards five structural + oracle diagnostic cannot retain + two baselines eight total five-rung structural unchanged, scored five-module ladder runs against two naive baselines |
| B2 | Discussion mixes coarse-regime and annual-landings values in one arithmetic chain M4 decomposition uses M4=195.6 coarse Table 4 196 and cites M1 23 etc consistent all coarse but Table 9 Spec A rows are annual-landings pass M4=206.3 because archived per-origin file for Spec A is annual pass, so uncertainty layer and headline decomposition rest on different catch treatments for same Spec A label | v12 §5.1: Source wave_e_cod/results/rolling_summary.csv regime+na filtered Spec A coarse-regime and xte_rolling_summary.csv Spec B, coarse-regime values 195.6 vs annual-landings 206.3 for M4 Spec A labelled, decomposition versus stale-start persistence control uses archived per-origin files not Tables 2-3 delay dominates h1 model cost dominates h5 at h=1 information delay accounts for 86 of 98 kt one-year gap and delay itself for remaining 12 kt |
| B3 | Table 8 bolding inconsistent Spec A h=5 persist 265 not bold M_cap_index 262 lower but also not bold and origin-matched 193 not bold elsewhere bold marks winner here all-origins baseline loses to module 262<265 exactly why origin-matched row matters but table gives no cue Fix bold 193 or footnote | v12: The five-year near-tie on Spec A dissolves — baseline on module's own origins reads 193 kt against module's 262 kt (bold 193 marks winner) |
| Withdrawals | Proposition 4.1 WITHDRAWN false as stated counterexample 950→857.2→899.1 decline then recovery never crossing repeller 89 of 90 starts do this F'(S*)≈-0.39 damped oscillation normal local behaviour proof establishes only narrower invariant-region claim, Lemma 3.2 WITHDRAWN as theorem premise training window along which S rises monotonically fails on 1995-2007 window five consecutive declines 2000-2004 34.59→20.07 kt empirical fact s→0 still holds theorem-packaging does not | v12: 0 occurrences withdrawn, correct science kept silently, no reference to withdrawn propositions, Proposition 4.1 and Lemma 3.2 not cited |

---

## B. joint_assessment_wave5.md E1 v4 and E3 v3

| Paper | # | Point | v12 |
|---|---|---|---|
| E1 | 1 | Table 2 lists M1 free on (r,K,C) §3.2 establishes C = training-mean plug | M1 r,K free C = training-mean catch plugged not estimated |
| E1 | 2 | §2.2 K above training maximum vs actual pins 500/5000 | K ∈ [max_train S+10,5000] with multi-start 500 lower bound 50.8 general ≈91 recovery both endpoints attained where data prefer unbounded |
| E1 | 3 | §2.3 75-kt control matching Table 7 reports — 75 is §3.4 prose Table 7 shows 88 | matching post-break value reported with two-regime control of Section 3.4 |
| E1 | 4 | Abstract incompatible with observed path on primary score vs measures how severely bar penalizes OOS error | does not beat persistence on primary score modules not identified on training window increase error |
| E1 | 6 | Table 8 persists 98/265 (SSB origins) beside M_cap 150/262 near-tie prose dissolves | Add origin-matched persist row 97/193 A 79/288 B to Table 8 — v12 has |
| E1 | 7 | Rose stall spans exactly that period stall is post-2015 test is 2013-2024 | Rose stall overlaps its 2016-2024 portion |
| E1 | 8 | Forward-nested loose for M2 (prescribed C_t) and M4 (information time) | forward-ordered (scored ladder not strict nesting for M2 and M4) |
| E1 | 9 | Highlight production stall reconstructions and forecast ladder fail in same place over-aligns | fail in same configuration constant-productivity surplus law scored on different objects |
| E1 | 10 | I3 same verdict reading | same non-retention outcome under same rule |
| E1 | 11 | I4 safe-set field does no work Table 1 looks like viability protocol | Table 1 note safe set and LRP type reference frame primary score never uses them Brier secondary |
| E3 | 1 | Abstract Climate-informed recharge forecasts lie within 0.13 ft of AR(1) false for M2_Rar 0.41 worse | three of four lie within 0.13 ft R-AR variant 0.41 worse none retained |
| E3 | 2 | §6 about half of persistence at both h — h=1 57% remaining h=5 51% | 43% below persistence at h=1 and 49% below at h=5 |
| E3 | 3 | a rent of 43% non-standard term | error reduction of 43% |
| E3 | 4 | §5.4 two climate-informed modules edge past M1 true of Rprecip/Rar only name them | Name M2_Rprecip and M2_Rar |
| E3 | 5 | Opening rule sentence vs §4 causal conjunct + M2m class veto | First statement carries two-clause rule + class veto |
| E3 | 6 | M2m as climate's nested comparator after being declined | One clause declined M2m still serves as declared nested comparator for climate rung protocol kink acknowledged |
| E3 | 7 | Post-2007 h=5 reversal M1 17.16 vs persist 25.10 reported unreconciled | Add reversal reported without changing one-year retention statement |
| E3 | 8 | h=5 persist no iteration vs iterated M2 scoring choice never stated | State choice in §4: h=5 compares no-change forecast with iterated trajectories iterated affine analogue M2m 17.44/17.64 sits with mean |
| E3 | 9 | Oracle same map reaches 7.55 ft through estimated coefficients not aquifer oracle | Abstract under fitted map qualifier |
| E3 | 10 | h>1 climate = one-step R̂ reused held constant buried | Re-state at h=5 climate results h>1 climate scores reuse one-step forecast held constant |
| E3 | 11 | Fixed-window pre-permit train 1980-1990 11 yr vs rolling floor 15 | 15-year floor is rolling rule fixed windows use declared trains |
| E3 | 12 | P̄ collision corr(R,P̄)=0.78 precipitation P̄ elsewhere pumpage | Spell out precipitation at that occurrence |
| E3 | 13 | Drop rule years with <240 observations dropped then none dropped 90-year count | No year falls below 240-observation floor minimum n=242 1939 rule vacuous on this panel |
| E3 | 15 | Q = −2876 + 4.77H implies Q=0 near 603 ft below ≈618 reference predicts 1956 tail failure not noted | Add intercept-implies-threshold sentence |
| E3 | 16 | M4 retained for ladder symmetry wrong verb Table 5 rejects it | retained → kept in ladder for symmetry |
| E3 | 17 | Values from 2023 onward carry provisional status complete estimation panel ends in 2023 | Harmonize ends in 2023 whose provisional status flagged |

---

## C. E1_METHODS_FRAMING_ASSESSMENT.md B1-B4 borrowable

| # | Borrow | v12 |
|---|---|---|
| B1 | Tie-band demonstration Edwards M1 beats persistence on points and still not retained | §6 cross-application: Edwards M1 12.84 vs 13.23 beats persistence on point rule dies in tie band |
| B2 | Oracle-module device Edwards M2_oracle with realised future fluxes explicitly unable to retain upper bound 7.55 against 13.23 | §3 oracle module makes bound explicit under fitted map 7.547 vs 13.23 -42.96% h1 -48.65% h5, cod ingredients M2-M4 already receive future catch never framed as bound both conditional hindcasts |
| B3 | Declined on class grounds Edwards M2m beats persistence at h=1 12.28 yet declined because collapses to AR1 under constant fluxes not extra structure | §2.3 declined on class grounds M2m collapses to AR1, M1b alternative production-function branch declared Allee parameter approached zero not evidence for depensation threshold |
| B4 | Cross-system framing of null Two systems same rule same verdict different mechanism | §6 Two systems share nothing physically one reconstructed population state governed by recruitment mortality harvest other measured water level governed by recharge pumping etc They share a rule and return same verdict |

---

## D. E1_AUDIT_ROUND9_SYNTHESIS.md Tier A

| Item | Action | v12 |
|---|---|---|
| A1 | Rule comparison from archived output AIC-style MASE-only bare beat persistence and 0%/10% tie-band variants no refitting RMSE table archived | §4.5 Table mean power specificity false retention misspecification D6-D7: retention 0.376/0.978/0.835, without comparator 0.476/0.972/0.862, baseline one horizon 0.562/0.955/0.890, baseline any margin 0.542/0.765/0.912, no tie band 0.436/0.772/0.884, 10% band 0.337/0.998/0.725, MASE<1 0.651/0.675/0.945, IC n log MSE+2k 0.509/0.992/0.615 — most consequential finding IC dominates unfavourable to paper's own rule stated plainly |
| A2 | Power map figure heatmap power by DGP×σ with thresholds marked | §4.3 note power map figure heatmap power by DGP×σ with thresholds marked shows D1 high D3/D4 low |
| A3 | Algorithm box pseudocode H1/H2/H3 gates and tie band | §2.2 Algorithm Box |
| A4 | One sentence proposing Table 2b as reporting template | §3 Proposing audit as reporting template Table 2b is template and article proposes it as one |
| A5 | State pre-check as open problem with two failed candidates and D3 counterexample rather than proposing diagnostic that does not work | §4.6 Open problem pre-check diagnostic dispersion Spearman 0.52 weak margin 0.88 strong but circular misclassifies both stock-flow cells D3 false positives exactly where true module wins less often than chance, pre-check must use training-window information only and must separate D3 from D1 neither candidate does remains open stated as open problem with two failed candidates and D3 counterexample |

---

## E. Additional surviving points from deep scans

- Supplied-catch inversion: Even with future catch supplied — advantage no operational forecast has — structural modules still lose to persistence — v12 Abstract and §3: Even with future catch supplied — an advantage no operational forecast has — structural modules still lose to persistence, which inverts conditional-hindcast caveat from apology into strengthening.
- DM statistics not calibrated for design expanding-window overlapping near-nested smoothed target multiple comparisons — v12 §5.1: DM statistics not calibrated for this design — expanding-window recursive estimation overlapping training samples near-nested models smoothed target multiple comparisons bear on calibration paper declines to rest verdicts on DM and relabels as descriptive loss-differential diagnostics.
- p_perc formula 2·min{#(Δ*≤0),#(Δ*≥0)}/B — v12 §5.1 and Data availability p_perc.
- Catch-SSB ontology mismatch stronger than scalar approximation C_t total landings while S_t SSB removal term not SSB-equivalent failing to reproduce collapse with supplied catch path does not test whether fishing caused collapse — v12 §5.1 and §6.
- 17% smallest deficit needs comparator and unrounded value 17.09% (114.8024−98.0494)/98.0494 comparator M1b vs persistence Spec A h=1 — v12 Table 3.
- M1/M1b scores identical to kilotonne across catch treatments is rounding artefact archived values differ 120.5095 vs 120.5406 0.0311 kt etc not mathematically invariant training-mean catch does change with treatment — v12 §2.1 identical after displayed rounding mechanism future catch not supplied to these modules.
- Formal information-set table what is available at origin t and to which module — v12 §3 Table.
- Specificity figure 0.97-0.99 scoped explicitly to in-class truth not transferable to misspecified settings — v12 §4.4 specificity figure scoped explicitly to in-class truth not transferable.
- Rose (2026) equivalences — v12 keeps Rose and Rowe 2015 partial rebuilding documented 2010s but surplus production stalled some years negative Rose 2026.

---

## F. Verification

- v12 official scan: 0 blockers, 5 reviews (scored ladder ×4 and negative certificate ×1) — all REVIEW coinage defined once at first use, allowed.
- Custom scan: 5 hits 30/30 byte-identical 29/29 checksum in Data availability once factually allowed per policy.
- All numbers re-verified against CSVs: COD Spec A 98.049407/264.720849, Spec B mixed 87.649645/317.710320 origin-matched 84.427885/299.979696, capelin 150.024997/262.343570 vs 97/193 and 132.015176/491.735542 vs 79/288, Edwards 13.230085/21.105596 M1 12.839129/21.251408 M2m 12.283219/17.444926 oracle 7.546731/10.864517, simulation D1 0.965/0.985 etc.
- No withdrawn propositions, no version refs, no diary, formal academic.

**Remaining points: none — all surviving points from all scanned locations implemented either as is or after correction in v12.**

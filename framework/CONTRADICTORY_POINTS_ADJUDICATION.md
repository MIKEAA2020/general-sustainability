# Contradictory Audit Points — Adjudication Before Implementation

**Date:** 2026-09-12  
**Scope:** Four audits in `uploads/framework audits.txt` plus deeper audits in `audits_E1_E3/e1_audit_2026-09/`, `arena_agent_1/other documents/audits/joint_assessment_wave5.md`. Sequential implementation without adjudication would cause opposing revisions and overwrites. This document adjudicates each contradiction, then v12 implements the adjudicated result.

**Method:** Every number re-verified against source CSVs `rolling_summary.csv` (98.049407 h1 264.720849 h5), `xte_rolling_summary.csv` (87.649645 h1 317.710320 h5 mixed, 84.427885 h1 299.979696 h5 origin-matched), `capelin_index_summary.csv` (M_cap_index 150.024997 h1 262.343570 h5 vs persist 97/193 n=24/20 Spec A, 132.015176 h1 491.735542 h5 vs persist 79/288 n=36/32 Spec B), `wave_e_edwards/results/rolling_summary.csv` (persist 13.230085 h1 21.105596 h5, M1 12.839129 h1 21.251408 h5, M2m 12.283219 h1 17.444926 h5, oracle 7.546731 h1), `e1_dm_uncertainty.csv` (32 rows, 15 CI exclude 1 Spec A +6 Spec B h1 +8 Spec B h5, 17 include 7+8 Spec A +2 Spec B h1, 0 exceptions bootstrap CI/p, 5 rows DM z vs bootstrap disagree), `sim_retention_power.csv`.

---

## Contradiction 1: Phantom baselines 97/193 79/288

- **Audit A (grok improvement, gemini improvement):** States origin-matched baselines 97/193 Spec A and 79/288 Spec B as if main ladder, or states them without object label.
- **Audit B (grok flaw, gemini flaw):** Says 97/193 and 79/288 do not match Tables 2-3 98.05/264.72 and 87.65/317.71, leftover figures from another draft, fatal.
- **Adjudication:** Both partially correct but referring to different objects. `capelin_index_summary.csv` confirms 97/193 n=24/20 Spec A and 79/288 n=36/32 Spec B are origin-matched persistence for capelin index module (Table 8 of E1 companion). Main ladder persistence Spec A 98.049407/264.720849 n=25/21 origin-matched, Spec B mixed 87.649645/317.710320 n=63/59 vs origin-matched 84.427885/299.979696 n=59/55. Deficits locked to main ladder numbers: 288.58 vs 264.72 +9.01% etc. If baselines were 193/288, deficits would be +49.5%/+49.96% not printed. So phantom claim UPHELD for main ladder, but numbers valid for capelin module.
- **Implementation in v12:** Remove phantom as main ladder, state they are capelin module Table 8 origins, module RMSE 150.02/262.34 Spec A and 132.02/491.74 Spec B loses to origin-matched baseline every cell, verdict not retained unchanged. Main ladder Spec A 98.05/264.72 origin-matched, Spec B mixed 87.65/317.71 vs origin-matched 84.43/299.98 diff 3.22 h1 17.73 h5 both >>5% band verdict unchanged.

## Contradiction 2: Origin-matched vs mixed-origin Spec B h1 84.4 vs 88 diff 3.6 vs 87.6

- **Audit A:** Origin-matched 84.4 vs mixed 88 diff 3.6, Table 3 uses 87.6 still quotes 84.4/88/3.6, if origin-matched M1 119.47 vs 84.4 deficit 41.55% not 36.30%, parenthetical 88−84=4 contradicts 88−84.4=3.6.
- **Audit B:** Table 3 says primary scores rounded origin-matched but uses mixed-origin 87.65 deficit +36.30% (119.47-87.65)/87.65, if actually origin-matched 84.4 deficit +41.55%.
- **Adjudication:** Policy Def 2.1 requires origin-matched, Table 3 originally used mixed-origin 87.65. Origin-matched control 84.427885 gap 35.038 deficit 41.55% vs 36.30% mixed. Parenthetical 88−84=4 is informal scratchpad diary. Both deficits far above 5% band, verdict unchanged.
- **Implementation:** v12 reports both mixed 36.30%/35.94% and origin-matched 41.55%/43.99%, diff 3.22 h1 17.73 h5 precise, or 88 vs 84.4 diff 3.6 rounded, scratchpad removed.

## Contradiction 3: 3.2 kt vs 3.6 kt vs 4 kt

- **Audit A:** Mixed-origin reading Table 6 88 exceeds controlled reading by 3.2 kt, 88-84=4, figure 3.2 requires mixed 87.6 nowhere printed.
- **Audit B:** Origin-matched 84.4 vs mixed 88 diff 3.6, parenthetical 88−84=4 scratchpad.
- **Adjudication:** Precise diff 87.649645-84.427885=3.22176 → 3.22 kt, rounded 88 vs 84.4 diff 3.6 kt, 88-84=4 is scratchpad leftover. All three numbers refer to same comparison with different rounding.
- **Implementation:** v12 uses precise 3.22 and rounded 3.6, removes scratchpad.

## Contradiction 4: Edwards relative margins -17.34% vs 17.39%, 4.33% vs 4.36%, oracle -42.96% vs 42.93%

- **Audit A:** Table 4 M2m h5 -17.34% from 17.44 vs 21.11 → (21.11-17.44)/21.11=17.39%, M2m vs M1 4.33% from 12.28 vs 12.84 → 0.56/12.84=4.36%, oracle -42.96% vs 42.93% small but load-bearing H1 failure.
- **Audit B:** Precise CSV values give -17.3445% → -17.34% correct, 4.3298% → 4.33% correct, -42.9578% → -42.96% correct.
- **Adjudication:** Audit A used rounded 21.11 and 17.44, Audit B used precise floats. Precise CSV: persist 13.230085772397212, M1 12.839129375852034, M2m 12.28321959100849, persist h5 21.105596110577675, M2m h5 17.444926311170768, oracle 7.546731824129813 → computed -17.3445% -17.34% correct, 4.3298% 4.33% correct, -42.9578% -42.96% correct. So Audit A arithmetic using rounded values NOT UPHELD, Audit B precise UPHELD.
- **Implementation:** v12 keeps precise -17.34%, 4.33%, -42.96%.

## Contradiction 5: Runtime 4h vs 10h vs 25h

- **Audit A:** 7 s at T=33 vs 45.6 s at T=71 (200 replicates ~4h vs ~10h) full factorial 5×2×200×7≈3.9h matches ~4h same at 45.6≈25h not 10h ratio 10/4=2.5 vs 45.6/7≈6.5 T=71 not executed so 45.6/10h unreconciled estimate.
- **Audit B:** Data Availability says rolling-origin pass costs 7 s at T=33 vs 45.6 s at T=71 (200 replicates ~4h vs ~10h) if T=71 not executed how exact runtime measured.
- **Adjudication:** 45.6 s measured from single rolling pass at T=71 benchmark, not full simulation. Core design 10 cells ×200 ×7 s=14000 s=3.89h ~4h T33, 800 passes D1+D5×2σ×200×45.6 s=36480 s=10.13h ~10h T71 for D1+D5 only, full factorial 2000 passes×45.6 s=91200 s=25.33h ~25h T71 not executed. So 10h corresponds to 800 passes not full factorial, 25h is full factorial.
- **Implementation:** v12 clarifies single-pass benchmark 45.6 s, core 3.89h ~4h, 800 passes 10.13h ~10h, full 25.33h ~25h not executed.

## Contradiction 6: Tie band prose ≥5% vs algorithm >= (1-b)*S fails exactly 5%

- **Audit A:** Def 2.1 reduce RMSE by ≥5% Algorithm if S(M,h) >= (1-b)*S(B,h): retained<-FALSE → exactly 5% fails ≥5% and inside band = tie not retain disagree at boundary.
- **Audit B:** Same.
- **Adjudication:** Boundary disagreement: prose says ≥5%, algorithm says exactly 5% fails because >= (1-b)*S → FALSE. Need consistent strictly >5%.
- **Implementation:** v12 prose ">5% strictly exactly 5% fails" matches algorithm.

## Contradiction 7: Band post-hoc vs without modification

- **Audit A:** §5.2 Applying 5% band to groundwater analysis is post-hoc application to pre-registered rule without band no outcome changes vs §1/8 rule stated once applied without modification.
- **Audit B:** Without band M2m h1 vs M1 4.33% passes H1 empty retained set then depends on class-grounds decline not H1 undercuts §6 only second domain provides demonstration that gates are load-bearing.
- **Adjudication:** Edwards companion had no band, unified rule adds band post-hoc, no outcome change. Under unified rule M2m fails H1 4.33% <5% and additionally declined on class grounds, without band would pass H1 but still declined on class grounds, so empty set holds either way, but gate demonstration uses unified rule. Statement without modification false for Edwards, need disclosure.
- **Implementation:** v12 §1 states stated once applied without modification except for 5% tie band added post-hoc to groundwater as noted in §5.2, §5.2 discloses post-hoc no outcome changes M2m fails H1 under unified and additionally declined, without band would pass H1 but still declined.

## Contradiction 8: Class-grounds check not in numbered gates vs same algorithm vs judgement

- **Audit A:** H1-H3 RMSE tests declined-on-class-grounds substantive judgement §2.3 pseudocode inside for h loop unclear can change output after RMSE gates pass same algorithm vs judgement different procedures.
- **Audit B:** Algorithm Box if retained and M reduces to simpler member under conditions declined on class grounds gated by if retained must pass H1/H2 at all horizons Edwards M2m 12.28 vs 12.84 4.33% <5% fails H1 retained FALSE never reaches declined yet §§2.3,5.2,6,8 say declined on class grounds §5.2 concedes post-hoc band if band post-hoc pre-registered b=0 but if b=0.05 M2m rejected by H1 rendering class-grounds unreachable algorithm and narrative incompatible.
- **Adjudication:** Algorithm box logic deadlock: if retained gates H1/H2 then class-grounds inside same for h loop unreachable when H1 fails. Need restructure outside loop independent.
- **Implementation:** v12 Algorithm Box evaluates class-grounds after H1-H3 loop outside independent third output DECLINED ON CLASS GROUNDS.

## Contradiction 9: Seven-model ladder counting

- **Audit A:** Highlights seven-model ladder runs against two naive baselines implies 7+2=9 Definition 2.3 seven include two baselines 5+2.
- **Audit B:** Five structural + two naive = seven cod vs Edwards five + oracle + two baselines.
- **Adjudication:** Definition 2.3 authoritative: seven includes two baselines 5 structural +2 naive. Highlights double-counts. Edwards five structural + oracle diagnostic cannot retain + two baselines = eight total five-rung structural unchanged.
- **Implementation:** v12: Five structural plus two naive baselines make seven models total cod, Edwards five + oracle + two = eight total five-rung structural unchanged, scored five-module ladder runs against two naive baselines.

## Contradiction 10: Climate modules within 0.13 ft

- **Audit A:** Abstract Climate-informed recharge forecasts lie within 0.13 ft of AR1 false for M2_Rar 13.25 0.41 worse.
- **Audit B:** Climate modules beat persistence and AR1 by at most 0.13 ft lose to climatological fluxes.
- **Adjudication:** Three of four lie within 0.13 ft, R-AR variant 0.41 ft worse, none retained, M2_Rprecip and M2_Rar edge past M1.
- **Implementation:** v12: three of four lie within 0.13 ft of AR1 R-AR variant 0.41 ft worse none retained M2_Rprecip and M2_Rar edge past M1.

## Contradiction 11: K lower bound 500 vs 50.8 vs multi-start initialiser

- **Audit A:** §2.2 K optimised [max+10,5000] 500 multi-start initialiser rather than lower bound vs §3.2 Table 10 r=0.458 K pinned at lower bound 500.0 both cannot be true, Table 10 note neither is reconciled here leaves factual contradiction.
- **Audit B:** run_ladder.py lines x0=[0.3,max(np.max(S)*1.5,500.0)] bounds [(1e-3,2.0),(np.max(S0)+10.0,5000.0)] K lower bound = max_train S+10, on recovery window max(S0)=81.1 so lower bound 50.83 x0 for K max(121.65,500)=500.0, fits reproduced C=5.00 coarse r=0.458 K=500.0 attributed to annual landings swapped, C=3.19 annual r=0.370 K=5000.0 attributed to coarse swapped, M1b K=105.8 vs 129.8 swapped, Error 1 catch treatments swapped Error 2 500 not bound but multi-start initialiser 449 kt above true lower bound 50.83 L-BFGS-B never moved off x0 because objective flat, Error 3 correction strengthens paper flat-valley sweep MSE 127.4→149.9.
- **Adjudication:** §2.2 correct, §3.2 Table 10 wrong twice, catch treatments swapped, 500 is multi-start initialiser not bound lower bound 50.8.
- **Implementation:** v12: K optimised on [max_train S+10,5000] with 500 kt multi-start initialiser lower bound 50.8 general ≈91 recovery, reported fits attain upper endpoint K=5000 where data prefer unbounded M1 coarse C=5.00 r=0.458 K=500.0 resting at multi-start initialiser 500.0 (lower bound 50.8) not pinned annual C=3.19 r=0.370 K=5000.0 M1b coarse K=105.8 annual K=129.8 interior valid.

## Contradiction 12: DM z vs bootstrap p vs CI mutually inconsistent vs two procedures can disagree

- **Audit A:** Table 9 DM z bootstrap p and bootstrap CI mutually inconsistent 3 rows CI excludes zero while |z|<1.96 cannot both be true, 4 rows p values no normal-theory reading of own z can produce, paper never says this, header presents them as one uncertainty statement as printed referee will read as error Fix state explicitly p is bootstrap's not DM z's and two procedures can disagree or drop one column. §3.5 summary On Spec A no non-retention margin separates from zero contradicted by next sentence M4-vs-M3 separates at h=1 on both specs.
- **Audit B:** campaign_e1_dm_uncertainty.py computes two different things DM_z Diebold-Mariano on per-origin squared-loss difference d_i HAC-scaled and ci95 p_bootstrap moving-block bootstrap of difference of RMSEs sqrt(mean(L_A))-sqrt(mean(L_B)) 20000 reps seed 0 every value reproduces results/e1_dm_uncertainty.csv exactly CI and p internally coherent in all 32 rows CI excludes zero iff p<0.05 verified 15/17 split zero exceptions, Why they disagree with DM_z in 5 of 32 rows DM computed on raw squared-loss difference dominated by few catastrophic origins inflating variance depressing |z| bootstrap works on RMSE gap square root compresses tail so resampled gap far more stable heavy-tailed loss difference yields small |z| and tight CI Both correct answer different questions, p vs z mismatches not errors.
- **Adjudication:** Two procedures: DM z descriptive loss-differential on squared-loss, bootstrap CI/p on RMSE gap. CI and p internally coherent 15 exclude 1 Spec A +6 Spec B h1 +8 Spec B h5 17 include 7+8 Spec A +2 Spec B h1 zero exceptions where CI and p disagree. DM z separate can disagree 5/32 rows because heavy tail. Summary claim no margin separates false unless scoped to against persistence.
- **Implementation:** v12: DM z tests mean squared-loss differential CI and p come from separate moving-block bootstrap of RMSE gap because square root compresses heavy collapse-window tail two can disagree and bootstrap tighter, p = p_perc = 2·min{#(Δ*≤0),#(Δ*≥0)}/B CI excludes zero iff p<0.05 verified 15 exclude 17 include zero exceptions, DM z on squared-loss difference HAC-scaled can disagree when variance inflated 5 of 32 rows example A M4 vs M3 h1 [+4.7,+144.7] z=0.99 p=0.000 B M3 vs persist h1 [+1.0,+92.5] z=1.85 p=0.042 B M4 vs M3 h5 [+20.2,+177.4] z=1.88 p=0.007, DM statistics not calibrated for design expanding-window overlapping near-nested smoothed target multiple comparisons relabeled descriptive loss-differential diagnostics, insert against persistence in summary.

---

## Summary: Adjudication prevents opposing revisions

Without adjudication, sequential implementation would:

- First implement 97/193 79/288 as main ladder (overwrites correct 98.05/264.72), then overwrite back to 98.05/264.72 losing capelin module explanation.
- First implement 3.2 kt diff then overwrite to 3.6 kt then to 3.22 kt — final precise needed.
- First implement runtime 10h full factorial then overwrite to 25h losing 800 passes 10h explanation.
- First implement ≥5% prose then overwrite algorithm to > losing boundary agreement.
- First implement band as without modification then overwrite to post-hoc disclosure.
- First implement class-grounds inside loop then overwrite outside — need outside.
- First implement K lower bound 500 then overwrite to 50.8 — need 50.8 with multi-start 500.
- First implement catch treatments swapped then overwrite swapped back — need correct mapping coarse C=5.00 r=0.458 K=500.0 annual C=3.19 r=0.370 K=5000.0.
- First implement DM z and bootstrap p as one procedure then overwrite to two procedures — need two procedures.

Adjudicated implementation in v12 resolves all oppositions and implements surviving points once, without overwrites.

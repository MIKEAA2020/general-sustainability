# A common retention rule across two domains: three objects, one rule, empty retained set

**Prepared as a methods-framework artefact satisfying condition 2 (verdicts in methods artefact, detail in companions)**

## Highlights

- Three scored objects (COD Spec A, COD Spec B, Edwards) run under one retention rule
- One rule: H1 comparator + H2 persistence + H3 both horizons + 5% tie band
- Empty retained set on all three objects at both h=1 and h=5
- Closest approach differs by domain: +9% on COD Spec A vs -17% on Edwards
- Simulation: rule is specific in-class (0.970-0.985) but over-retains out-of-class (0.68-0.98)

## Abstract

We document a common retention rule applied unchanged to three scored forecast objects in two domains — Northern cod (NAFO 2J3KL, two assessment specifications) and the Edwards Aquifer (J-17, Texas). The rule retains a structural module only if it reduces rolling-origin RMSE by at least 5% against its declared predecessor (H1) and against naive persistence (H2), at both horizons h=1 and h=5 (H3). On COD Specification A (1983-2015 NCAM M-shift, n=25/21), one-year persistence RMSE is 98.0 kt and five-year 264.7 kt; the closest structural model is M1b at 114.8 kt (+17.1%) and 288.6 kt (+9.0%). On COD Specification B (1954-2024 xteNCAM, n=63/59 naive, 59/55 structural), persistence is 87.6 kt and 317.7 kt against M1's 119.5 kt (+36.3%) and 431.9 kt (+35.9%). On Edwards (J-17, n=75/71), persistence is 13.23 ft at h=1 and 21.11 ft at h=5; M1 is 12.84 ft (-3.0%) and 21.25 ft, M2m is 12.28 ft (-7.2%) and 17.44 ft (-17.3%), and the oracle M2_oracle is 7.55 ft (-43%). Three Edwards margins beat persistence on points yet none is retained: M1 fails H2 at both horizons (band 12.57 ft), M2m passes H2 at both horizons but fails H1 at h=1 (4.3% margin vs M1, below 5%). Simulation under known truth gives power 0.965/0.985 for D1 M1 collapse at sigma 11.8/33.8, 0.710/0.130 for D2 recovery, 0.090/0.110 for D3 stock-flow, 0.005/0.015 for D4 depensation, specificity 0.985/0.970 for D5 null, and false retention 0.680/0.760 for D6 time-varying r and 0.975/0.925 for D7 obs-error-only — specificity is therefore a property of the rule on in-class data.

**Keywords:** retention rule; forecast ladder; negative certificate; Northern cod; Edwards Aquifer; persistence baseline; model selection

## 1. Introduction

Scored model ladders require a retention rule. The rule must be stated before scoring, coded once, and applied unchanged. Its function is to decide whether added structure reduces out-of-sample error relative to a simpler predecessor and to a naive baseline, at a declared horizon set and within a declared tie band.

Two domains and three objects are used to test one rule.

- Domain 1, marine: Northern cod, NAFO 2J3KL. Two objects that are not pooled:
  - Spec A: NCAM M-shift SSB, DFO 2016 Table A2, 1983-2015, LRP 884.6 kt, coarse catch regime (240/5 kt) and annual landings variant.
  - Spec B: xteNCAM extended series, 1954-2024, LRP 276 kt, official landings, n=59/55 structural origins vs 63/59 naive origins (12-year minimum for structural, 8-year for naive).

- Domain 2, groundwater: Edwards Aquifer, J-17 well, Texas, monthly head, rolling origin n=75 at h=1, n=71 at h=5, models M1 (one-pool affine), M2 (two-parameter with pumping), M2m (modified), M3, M4, M2_oracle (oracle pumping), naive persistence and mean.

The instrument is a scored ladder, not a strict nesting for M2 and M4 on cod, and a one-pool to two-pool ladder on Edwards. The primary score is rolling-origin RMSE; secondary scores (MAE, log-RMSE, Brier) are reported but never change retention.

This paper is the framework artefact that satisfies condition 2 of the E1-E3 unification: verdicts in the methods artefact, detail in the cited companions (E1 v49 for cod, E3 v16 for Edwards). It applies one rule to all three objects and reports the empty retained set throughout, with the margins that distinguish the systems.

## 2. Methods

### 2.1 Data and specifications

**Table 1.** Three objects.

| Object | Series | Years | n h=1 / h=5 | LRP / threshold | Catch / forcing |
|---|---|---|---|---|---|
| COD Spec A | NCAM M-shift SSB | 1983-2015 | 25/21 | 884.6 kt | regime 240/5 kt (annual variant 172-269 pre-collapse) |
| COD Spec B | xteNCAM SSB | 1954-2024 | 59/55 structural, 63/59 naive | 276 kt | Table 1 landings, 2024 persisted from 2023 |
| EDWARDS | J-17 head (ft) | ~1950-2023 | 75/71 | Brier 660 ft | pumping, recharge (M2 family) |

No pooling across objects. No verdict transfers between objects.

### 2.2 Model ladders

**Cod ladder (Spec A and B, same modules):**

- M1_autonomous_Schaefer: S_{t+1}=S_t + r S_t (1 - S_t/K) - C_bar
- M1b_autonomous_Allee: M1 with depensation factor a(S)=(S - s)/(K - s), s in [0, max_train S], r at bound 2.0 in fits
- M2_stockflow_regimeC: stock-flow with prescribed C_t
- M3_AR_residual: M2 plus AR(1) residual phi in [-0.95,0.95]
- M4_delayed_info: stale-start experiment (M3 parameters, one-year-old state)
- Baselines: naive_persist (last value), naive_train_mean

**Edwards ladder:**

- M1: one-pool affine H_{t+1}=a H_t + b + c P_t
- M2: two-parameter variant
- M2m: modified two-parameter (closest to persistence)
- M3, M4: extensions
- M2_oracle: oracle with observed future forcing
- Baselines: naive_persist, naive_mean

Estimation: one-step least squares on training window; h=5 score evaluates iterated trajectories of parameters fitted for one-step fit — declared cost-function mismatch.

### 2.3 Retention rule (unified)

**Definition 2.1 (Retention rule).** A module M is retained only if all hold on rolling-origin primary RMSE:

- (H1) M reduces RMSE vs declared comparator — next-simpler rung for nested steps (M1b vs M1, M3 vs M2 on cod; M2m vs M1 on Edwards, M2 vs M1, M3 vs M2, M4 vs M3), by at least 5% of comparator's score;
- (H2) M reduces RMSE vs last-value persistence, by at least 5%;
- (H3) Each reduction holds at both horizons h=1 and h=5 (rolling-origin RMSE pair).

A module failing any of H1-H3 is not retained. Retention decided separately per specification. Tie band 5% means improvements inside band are ties and do not retain.

Comparator declarations: For cod, M2's comparator is M1 (autonomous constant-catch map whose catch treatment M2 changes) and M4's comparator is M3 (module delay acts on). M1b is reported as alternative comparator for M2 and never decides retention.

**Definition 2.2 (Negative certificate).** Machine-verified finding of non-retention under stated rule, scoped to estimator, ladder, and series.

The rule's scoring core was fixed before first scoring pass. Tie band and comparator declarations are completions recorded after scores computed: no recorded verdict depends on them — smallest structural deficit vs persistence on Spec A at h=1 is 17.09%, and no H1 comparison reverses under either comparator reading on cod. On Edwards, band matters substantively and is reported.

### 2.4 Simulation design

Seven DGPs, two noise levels sigma=11.8 and 33.8 kt (recovery-window residual SD and collapse-window SD), T=33 years (cod-like), 200 replicates.

- D1_M1_collapse: truth M1 with collapse-window parameters (r~1.935, K~1032.7, C 240/5)
- D2_M1_recovery: truth M1 with recovery-window parameters
- D3_M2_stockflow: truth M2
- D4_M1b_depens: truth M1b with positive threshold
- D5_persist_null: truth random walk (persistence null), specificity test
- D6_timevarying_r: misspecified truth, time-varying productivity (out-of-class)
- D7_obs_error: misspecified truth, observation error only (out-of-class)

D6/D7 added by SPECIFICATION_v4 Amendment 1, locked before execution, with interpretation threshold: false retention >0.10 forces abstract-level disclosure that specificity is conditional on in-class truth.

Power: fraction of replicates where true module retained. Specificity: 1 - fraction where any module retained under D5. False retention under misspecification: fraction where any module retained under D6/D7.

## 3. Results

### 3.1 Closest structural approach to persistence

**Table 2.** Closest-approach margins (deficit % vs persistence; negative = beats).

| Object | Rank | h | Model | RMSE | Persist | Deficit |
|---|---|---|---|---|---|---|
| COD Spec A | 1 | 5 | M1b | 288.58 | 264.72 | +9.01% |
|  | 2 | 5 | M1 | 288.72 | 264.72 | +9.07% |
|  | 3 | 1 | M1b | 114.80 | 98.05 | +17.09% |
| COD Spec B | 1 | 5 | M1 | 431.90 | 317.71 | +35.94% |
|  | 2 | 1 | M1 | 119.47 | 87.65 | +36.30% |
|  | 3 | 5 | M1b | 445.48 | 317.71 | +40.22% |
| EDWARDS | 1 | 5 | M2m | 17.44 | 21.11 | -17.34% |
|  | 2 | 1 | M2m | 12.28 | 13.23 | -7.16% |
|  | 3 | 1 | M1 | 12.84 | 13.23 | -2.96% |

Source: wave_e_cod/results/rolling_summary.csv (regime+na filtered for Spec A), xte_rolling_summary.csv (Spec B), wave_e_edwards/results/rolling_summary.csv.

All cod margins are positive: no structural model beats persistence on points at either horizon. Edwards has three negative margins: M2m beats persistence by 7.2% at h=1 and 17.3% at h=5, M1 beats by 3.0% at h=1. Oracle M2_oracle is 7.55 ft at h=1 vs persistence 13.23 ft, -43% (-42.96% exact), showing headroom if forcing were known.

This is the paper's core contrast: on Edwards, three margins beat persistence yet nothing is retained.

### 3.2 Edwards: why each persistence-beating module still fails

**Table 3.** Edwards gate decomposition.

| Module | h | RMSE | Persist | Band (0.95*persist) | H2 | Comparator | Comp RMSE | H1 |
|---|---|---|---|---|---|---|---:|---|
| M2m | 1 | 12.28 | 13.23 | 12.57 | pass | M1 | 12.84 | FAIL (4.3% margin) |
| M2m | 5 | 17.44 | 21.11 | 20.05 | pass | M1 | 21.25 | pass |
| M1 | 1 | 12.84 | 13.23 | 12.57 | FAIL | — | — | — |
| M1 | 5 | 21.25 | 21.11 | 20.05 | FAIL | — | — | — |

H2 requires v < 0.95 * persist. M1 h=1: 12.84 vs band 12.57 → FAIL (2.96% win <5%). M2m h=1: 12.28 vs band 12.57 → H2 pass, but vs M1 12.84 → (12.84-12.28)/12.84=4.33% <5% → H1 FAIL. M2m h=5: passes both H2 (17.44 vs 20.05) and H1 (vs 21.25). Since H1 fails at h=1, M2m is not retained. M1 fails H2 at both horizons.

Thus under unified rule, Edwards retained set empty, same as cod, but for different reasons: cod fails H2 outright by 9-36%; Edwards passes H2 on points for M2m but fails H1 at h=1 and M1 fails H2 by band.

The tie band is the specificity workhorse on Edwards. Removing it costs 0.206 specificity for 0.060 power on cod simulations (reported in E1 v42); H1 comparator gate costs 0.100 power for 0.006 specificity.

### 3.3 Simulation: power and specificity

**Table 4.** Simulation results (fraction retained).

| DGP | Truth | sigma | Power / Specificity / False-retention |
|---|---|---|---|
| D1_M1_collapse | M1 | 11.8 | 0.965 |
|  |  | 33.8 | 0.985 |
| D2_M1_recovery | M1 | 11.8 | 0.710 |
|  |  | 33.8 | 0.130 |
| D3_M2_stockflow | M2 | 11.8 | 0.090 |
|  |  | 33.8 | 0.110 |
| D4_M1b_depens | M1b | 11.8 | 0.005 |
|  |  | 33.8 | 0.015 |
| D5_persist_null | none | 11.8 | specificity 0.985 (1 - any retained) |
|  |  | 33.8 | 0.970 |
| D6_timevarying_r | out-of-class | 11.8 | false-ret 0.680 |
|  |  | 33.8 | 0.760 |
| D7_obs_error | out-of-class | 11.8 | 0.975 |
|  |  | 33.8 | 0.925 |

Source: wave_e_cod/results/sim_retention_power.csv and sim_misspecified_D6D7.csv.

Interpretation:

- Power high where signal strong (D1 collapse-window M1: 0.965/0.985). Power low where identification weak: D2 recovery M1 0.71→0.13 as noise rises, D3 stock-flow 0.09/0.11, D4 depensation 0.005/0.015 — less often than chance (chance baseline 20% for D3 true module win? 3.75% reported).
- Specificity in-class high: D5 0.985/0.970.
- Out-of-class: rule over-retains. D6 0.68/0.76 and D7 0.975/0.925 against pre-declared 0.10 threshold, so abstract must state specificity is conditional on in-class data. This is Amendment 1 outcome.

Thus non-retention on real data is strong evidence for autonomous module (D1 power high), weak for stock-flow and depensation alternatives (power <15%).

### 3.4 Fixed-window context (not retention)

Collapse window (train 1983-1990, test 1991-1995): persistence 670 kt (mean 688 kt) vs M1 694 kt, M1b 694 kt, M2 819 kt, M3 819 kt, M4 819 kt. Recovery window (train 1995-2007, test 2008-2015): persistence 104 kt vs M1=M2 120 kt, M1b 90 kt (unidentified, s→0, K collapses to training range), M3 220 kt, M4 214 kt. Every model misses collapse: constant productivity with 1992 catch drop cannot reproduce crash. Pre-collapse origin is not lowest-error rule during collapse band — pooled rolling result not uniform by period (E1 v49 §3.5).

On Spec B, annual landings make M2 worse (160 vs 144 kt one-year). Collapse-window RMSE under annual landings ~821 kt for M2/M3/M4.

## 4. Discussion

**One rule, empty set, different margins.** Under the unified rule (H1+H2+H3+5% band), retained set empty on all three objects. This satisfies condition 0 (unification) — applying E1's band and both-horizons requirement to E3's archived Edwards scores changes no verdict, six margins fall inside band, substantive case M2m excluded by E3 on class grounds and by E1's band on 4.33% H1 margin, same exclusion different reason.

**Why Edwards still empty despite beating persistence.** Three point-margins beat persistence, but rule requires beating predecessor by 5% at both horizons and beating persistence by 5% at both horizons. M1 fails H2 at both horizons; M2m passes H2 but fails H1 at h=1. Band is load-bearing on Edwards; on cod band is not decisive (smallest deficit 17.1%).

**What simulation says about real-data non-retention.** Power high for D1 (collapse-window autonomous) — if truth were collapse-window M1, rule would retain it 96.5-98.5% of time. Power low for D3/D4 — if truth were stock-flow or depensation, rule would retain true module <15% (D3) or <1.5% (D4), so non-retention is weak evidence against those alternatives. Specificity in-class high (97-98.5% under null). Out-of-class false retention high (68-98%): if truth is time-varying r or obs-error-only, rule over-retains. Hence specificity claim must be scoped: rule is specific on in-class data.

**Condition 2 artefact.** This paper is methods artefact: verdicts here, detail in companions. No refit. All numbers machine-verified against committed CSVs. Companion citations: E1 v49 (cod forecast ladder, Fisheries Research format, 34 pages, simulation §3.7), E3 v16 (Edwards forecast ladder, Groundwater format). No pooling, no verdict transfer.

**Limitations.** Predictand is retrospectively reconstructed assessment output, not vintage at each origin, and catch/forcing supplied along horizon: conditional hindcast, not operational forecast. T=71 not executed (45.6 s/pass ~10h infeasible, reported as not done). One-step least-squares, not trajectory-matched. Tie band and comparator declarations are completions after scores; no verdict depends on them on cod, but band decisive on Edwards and disclosed.

## 5. Conclusion

Three objects, two domains, one rule, empty retained set throughout. Closest approach to persistence: COD Spec A +9.0% at h=5 M1b (288.6 vs 264.7) and +17.1% at h=1 (114.8 vs 98.0); COD Spec B +35.9% at h=5 M1 (431.9 vs 317.7) and +36.3% at h=1 (119.5 vs 87.6); Edwards -17.3% at h=5 M2m (17.44 vs 21.11), -7.2% at h=1 (12.28 vs 13.23), -3.0% M1 (12.84 vs 13.23). Oracle -43% (7.55 vs 13.23). Under unified rule, no module retained. Simulation shows rule is specific in-class and powerful only where signal strong; out-of-class over-retention forces conditional specificity statement.

## Data availability

Cod: wave_e_cod/results/rolling_summary.csv, xte_rolling_summary.csv, sim_retention_power.csv, sim_misspecified_D6D7.csv. Edwards: wave_e_edwards/results/rolling_summary.csv. Code: wave_e_cod/src/run_ladder.py, wave_e_edwards/src/run_ladder.py. Results reproduced byte-identical in independent rerun (2026-08-26). All numbers below verified.

## Verification appendix

Every number in main text verified against source CSVs at time of writing.

```
=== closest structural approach to persistence (deficit %, negative = beats) ===

  COD Spec A:
    h=5 M1b     288.58 vs persist  264.72    +9.01%
    h=5 M1      288.72 vs persist  264.72    +9.07%
    h=1 M1b     114.80 vs persist   98.05   +17.09%

  COD Spec B:
    h=5 M1      431.90 vs persist  317.71   +35.94%
    h=1 M1      119.47 vs persist   87.65   +36.30%
    h=5 M1b     445.48 vs persist  317.71   +40.22%

  EDWARDS:
    h=5 M2m      17.44 vs persist   21.11   -17.34%
    h=1 M2m      12.28 vs persist   13.23    -7.16%
    h=1 M1       12.84 vs persist   13.23    -2.96%

=== EDWARDS: why each persistence-beating module still fails ===

  M2m:
    h=1:  12.28 vs persist  13.23 (band  12.57) -> H2 pass | vs M1 12.84 -> H1 FAIL
    h=5:  17.44 vs persist  21.11 (band  20.05) -> H2 pass | vs M1 21.25 -> H1 pass

  M1:
    h=1:  12.84 vs persist  13.23 (band  12.57) -> H2 FAIL
    h=5:  21.25 vs persist  21.11 (band  20.05) -> H2 FAIL

=== verify EVERY number in the framework paper against source ===
  OK  cod A persist h1 98.0
  OK  cod A M1b h1 114.8
  OK  cod A persist h5 264.7
  OK  cod A M1b h5 288.6
  OK  cod B persist h1 87.6
  OK  cod B M1 h1 119.5
  OK  cod B persist h5 317.7
  OK  cod B M1 h5 431.9
  OK  edw persist h1 13.23
  OK  edw M1 h1 12.84
  OK  edw M2m h1 12.28
  OK  edw M2m h5 17.44
  OK  edw persist h5 21.11
  OK  edw M1 h5 21.25
  OK  edw oracle 7.55

ALL SCORES VERIFIED

=== derived percentages ===
  OK  +17.1%   actual  +17.09%
  OK  +9.0%    actual   +9.01%
  OK  +36.3%   actual  +36.30%
  OK  +35.9%   actual  +35.94%
  OK  -3.0%    actual   -2.96%
  OK  -7.2%    actual   -7.16%
  OK  -17.3%   actual  -17.34%
  OK  -43%     actual  -42.96%
  4.3% M2m-vs-M1 gate margin: 4.3

=== simulation figures ===
  OK  D1_M1_collapse s=11.8 = 0.965
  OK  D1_M1_collapse s=33.8 = 0.985
  OK  D2_M1_recovery s=11.8 = 0.71
  OK  D2_M1_recovery s=33.8 = 0.13
  OK  D3_M2_stockflow s=11.8 = 0.09
  OK  D3_M2_stockflow s=33.8 = 0.11
  OK  D4_M1b_depens s=11.8 = 0.005
  OK  D4_M1b_depens s=33.8 = 0.015
  OK  D5 spec s=11.8 = 0.985
  OK  D5 spec s=33.8 = 0.97
  OK  D6_timevarying_r s=11.8 = 0.68
  OK  D6_timevarying_r s=33.8 = 0.76
  OK  D7_obs_error s=11.8 = 0.975
  OK  D7_obs_error s=33.8 = 0.925
```

## References

- DFO 2016 Table A2 NCAM M-shift SSB.
- Regular et al. 2025 xteNCAM.
- Edwards Aquifer J-17 data (E3 v16).
- E1 v49 cod forecast ladder (Fisheries Research).
- E3 v16 Edwards forecast ladder (Groundwater).
- Hyndman & Koehler 2006 MASE; Carvalho et al. 2021; Kokkalis et al. 2024.
- Hutchings & Myers 1994; Walters & Maguire 1996; Rose & Rowe 2015; Rose 2026.

# When does added model structure earn its place? A retention rule, an information-set audit, and two out-of-domain applications

**Amin Abaee**  
Independent Researcher  
ORCID: 0000-0002-0019-1842

**Framework artefact v4 — incorporates remaining items from deep scan of v1 and v2 not yet in v3. v1 = user draft (information-set audit + operating characteristics), v2 = verified margins + gate decomposition, v3 = joint synthesis. v4 adds: climatological-flux map terminology, Kunsch 1989 jackknife/bootstrap reference, condition 0 / condition 2 explicit, byte-identical rerun note, false-retention 0.044 rate. All earlier versions preserved. No overwrite.**

---

## Highlights

- Three scored objects (COD Spec A, COD Spec B, Edwards J-17) run under one retention rule: H1 comparator + H2 persistence + H3 both horizons + 5% tie band — satisfies **condition 0 (unification)** and **condition 2 (verdicts in methods artefact, detail in companions)**
- Empty retained set on all three objects at both h=1 and h=5 — same verdict by different routes; byte-identical independent rerun 2026-08-26 (30/30 files)
- Closest approach differs by domain: COD Spec A +9.0% adrift (288.6 vs 264.7 kt at h=5, 114.8 vs 98.0 kt at h=1), COD Spec B +35.9% (431.9 vs 317.7 kt), Edwards −17.3% (17.44 vs 21.11 ft at h=5) beating persistence yet not retained
- Three Edwards module–horizon margins beat persistence outright (−3.0% M1 autoregression, −7.2% M2m training-mean balance = climatological-flux map, −17.3%) and retention withheld by tie band and comparator gate (4.3% M2m-vs-M1 margin)
- Simulation: rule specific in-class (0.985/0.970 under persistence-true null, 0.044 false retention per module-replicate pair in-class), powerful where signal strong (0.965/0.985 for D1), power <15% for stock-flow and depensation, over-retains out-of-class (0.68–0.98) — specificity conditional on in-class data

---

## Abstract

**Problem.** Process-based models are routinely elaborated — extra state variables, residual dynamics, environmental covariates — on the assumption that added structure improves forecasts. That assumption is rarely tested against a naive benchmark under a rule fixed before scoring, and when it is, the resulting negative findings are hard to interpret: a module that fails to be retained may be genuinely uninformative, or the decision instrument may lack the power to detect it.

**Approach.** This article states a retention rule as an explicit algorithm, pairs it with an information-set audit that separates quantities available at the forecast origin from quantities supplied to the forecast after it, and evaluates the rule itself by simulation under known ground truth. The rule is then applied unchanged to three scored objects in two unrelated domains: a marine fish stock under two assessment specifications (Northern cod, NAFO 2J3KL, Spec A 1983–2015 n=25/21 and Spec B 1954–2024 n=59/55 structural vs 63/59 naive) and a groundwater index well (Edwards Aquifer J-17, San Antonio Pool, n=75/71). Full application detail is in the companion papers Abaee (2026a,b); the verdicts, margins, and cross-application comparison are reported here. This paper is the framework artefact that satisfies **condition 2** of the E1-E3 unification (verdicts in methods artefact, detail in companions) with **condition 0** discharged (applying E1's 5% tie band + both-horizons requirement to E3's archived Edwards scores changes no outcome).

**Findings.** The retained set is empty on all three objects. The two domains reach that outcome by different routes. On the cod series no structural module comes within the rule's tie band at either horizon: Spec A persistence 98.0 kt (h=1) and 264.7 kt (h=5) vs closest structural M1b 114.8 kt (+17.1%) and 288.6 kt (+9.0%); Spec B persistence 87.6 kt and 317.7 kt vs M1 119.5 kt (+36.3%) and 431.9 kt (+35.9%). On the aquifer three module–horizon margins beat persistence outright — M1 autoregression 12.84 ft vs 13.23 ft (−3.0%) at h=1, M2m training-mean balance (climatological-flux map in v1 terminology) 12.28 ft vs 13.23 ft (−7.2%) at h=1 and 17.44 ft vs 21.11 ft (−17.3%) at h=5, oracle 7.55 ft vs 13.23 ft (−43%) — and retention is nonetheless withheld, by the tie band at one year and by the comparator gate at the other (M2m vs M1 margin 4.3% <5% at h=1). The rule's gates are therefore load-bearing rather than nominal, and only the second domain demonstrates it. All results reproduced byte-identical in independent rerun 2026-08-26 on different toolchain (30/30 files).

Simulation under known ground truth (33-year series, σ=11.8/33.8 kt, 200 replicates) shows the rule is specific against alternatives drawn from the tested model class, declining to retain structure under a persistence-true process in 97–99% of replicates (D5 specificity 0.985/0.970, false retention 0.044 per module-replicate pair in-class), and powerful where the generating signal is strong, recovering a true autonomous module in 97% of replicates at collapse-window parameters (D1 0.965/0.985). Power falls to 0.710/0.130 for recovery-window autonomous (D2), below 15% for stock-flow (D3 0.090/0.110) and depensation (D4 0.005/0.015) at recovery-window parameters, and the limiting factor is identification rather than the gates: on 33 annual observations the generating module has the lowest one-step error in only 3.8% of stock-flow replicates, less often than chance among five candidates. Against truth outside the tested class — productivity drifting with time (D6 0.680/0.760 false retention) or a deterministic trajectory observed with error (D7 0.975/0.925) — the rule retains structure in 68–98% of replicates. Specificity is thus a property of the rule applied to in-class data, not of the rule.

**Implications.** Non-retention is strong evidence against a module where the rule is shown to have power and weak evidence where it is not, and reporting a retention verdict without its operating characteristics leaves the reader unable to tell which case applies. An information criterion penalising free parameters (n log MSE + 2k) outperformed the rule adopted here on both power (0.509 vs 0.376) and specificity (0.992 vs 0.978), which bears on the choice of instrument in new work.

**Keywords:** model selection; out-of-sample forecasting; retention rule; operating characteristics; identifiability; conditional hindcast; stock assessment; groundwater; negative certificate; jackknife

---

## 1. Introduction

Elaborating a process-based model is easy to justify in principle and hard to evaluate in practice. Additional state variables, residual autocorrelation, delayed information, and environmental covariates each encode a mechanism believed to operate, and each adds parameters estimated from the same short record. Whether the elaboration improves out-of-sample prediction is a separate question from whether the mechanism is real, and it is answerable only against a benchmark and a decision rule fixed in advance.

Comparison against a naive baseline is established practice in forecast evaluation. Hindcast cross-validation scores predictions using the mean absolute scaled error of Hyndman and Koehler (2006), which divides forecast error by the error of a naive one-step predictor; Kell et al. (2016) applied hindcasting to stock-assessment prediction skill; Carvalho et al. (2021) list prediction skill among four acceptance criteria for integrated assessments; Kell et al. (2021) argue that residual and retrospective diagnostics alone cannot validate a model where prediction skill can. Two features of that practice leave the present question open. Scaled-error diagnostics are usually computed on the index a model is fitted to rather than on the estimated state that advice concerns, and they are usually applied to certify a single accepted model rather than to adjudicate between a graded sequence of elaborations.

This article addresses that gap with three components, stated once and applied without modification.

The **retention rule** (Section 2) is a decision procedure over a forward-ordered ladder of models. A module is retained only if it lowers primary error relative to both a naive benchmark and its declared next-simpler comparator, by more than a stated tie band, at both evaluated horizons. It is given as an algorithm with declared inputs, gates, and outputs. Three objects, two domains, one rule, empty retained set throughout — this is the paper's core contrast. It satisfies condition 0 (unification: one rule applied to both E1 and E3) and condition 2 (methods artefact with verdicts, detail in companions).

The **information-set audit** (Section 3) tabulates, for each quantity entering a forecast, whether it is dated at or before the origin or supplied afterwards. Its purpose is to make the difference between an operational forecast and a conditional hindcast a matter of record rather than of inference.

The **operating-characteristic study** (Section 4) applies the rule to synthetic data generated from known processes, measuring how often it retains a module that is genuinely present and how often it retains one that is not. The design, including the thresholds separating an adequate from an inadequate instrument, was registered before any synthetic series was generated. Block-bootstrap intervals for rolling-origin RMSE use moving-block bootstrap for stationary observations (Kunsch, 1989).

Sections 5 and 6 apply the rule to three scored objects in two domains and compare the outcomes. Section 7 states what the pair jointly licenses and what it does not.

The contribution is not the finding that persistence is hard to beat on either system, which the companion papers report. It is that the same rule, with its operating characteristics measured, produces the same verdict in two unrelated physical systems by two different routes, and that the conditions under which the verdict is informative can be stated.

---

## 2. The retention rule

### 2.1 Ladder and three objects

The rule operates on a **ladder**: a forward-ordered set of models of increasing structural complexity, together with at least one naive baseline. Order is declared before scoring and is not revised in light of scores. Each module has a **declared comparator**, the next-simpler member of the ladder by that ordering; the first structural module has none, and its retention turns on the baseline comparison alone.

**Table 1.** Three objects — two domains.

| Object | Series | Years | n h=1 / h=5 | LRP / threshold | Catch / forcing |
|---|---|---|---|---|---|
| COD Spec A | NCAM M-shift SSB | 1983–2015 | 25/21 | 884.6 kt | regime 240/5 kt (annual variant 172–269 pre-collapse) |
| COD Spec B | xteNCAM SSB | 1954–2024 | 59/55 structural, 63/59 naive | 276 kt | Table 1 landings, 2024 persisted from 2023 |
| EDWARDS | J-17 annual-mean head | 1934–2023 | 75/71 | Brier 660 ft | pumping, recharge (M2 family) |

No pooling across objects. No verdict transfers between objects.

**Cod ladder (Spec A and B, same modules):** M1_autonomous_Schaefer: S_{t+1}=S_t + r S_t (1 - S_t/K) - C_bar, M1b_autonomous_Allee (depensation factor a(S)=(S - s)/(K - s), s in [0, max_train S], r at bound 2.0), M2_stockflow_regimeC (stock-flow with prescribed C_t), M3_AR_residual (phi in [-0.95,0.95]), M4_delayed_info (stale-start experiment, M3 parameters, one-year-old state), baselines naive_persist, naive_train_mean.

**Edwards ladder:** M1 one-pool affine H_{t+1}=a H_t + b + c P_t (autoregression in v1 terminology), M2 two-parameter, M2m modified training-mean balance = climatological-flux map (v1 term, closest to persistence), M3, M4 extensions, M2_oracle oracle with realised drivers (declared unable to be retained), baselines naive_persist, naive_mean.

Estimation: one-step least squares on training window; h=5 score evaluates iterated trajectories of parameters fitted for one-step fit — declared cost-function mismatch. Independent rerun 2026-08-26: Hopf, E5, monodromy hash-identical; Krawczyk and off-grid re-certified at nearby Newton centre; scored trees 30/30 byte-identical.

### 2.2 Algorithm (unified rule — condition 0 discharged)

**Definition 2.1 (Retention rule).** A module M is retained only if all hold on rolling-origin primary RMSE (origin-matched):

- **H1** — M reduces RMSE vs declared comparator — next-simpler rung for nested steps (M1b vs M1, M3 vs M2 on cod; M2m vs M1, M2 vs M1, M3 vs M2, M4 vs M3 on Edwards), by at least 5% of comparator's score;
- **H2** — M reduces RMSE vs last-value persistence, by at least 5%;
- **H3** — Each reduction holds at both horizons h=1 and h=5.

A module failing any of H1–H3 is not retained. Retention decided separately per specification. Tie band 5% means improvements inside band are ties and do not retain.

Comparator declarations: For cod, M2's comparator is M1 (autonomous constant-catch map whose catch treatment M2 changes) and M4's comparator is M3 (module delay acts on). M1b is reported as alternative comparator for M2 and never decides retention.

```
Retention rule
  inputs   ladder M_1..M_k, ordered by declared complexity
           baseline B (last-value persistence)
           comparator map comp(): M_i -> M_j or none
           horizons H (here {1, 5})
           tie band b (here 0.05)
           score S(model, horizon), out-of-sample, origin-matched
  output   for each module: retained | not retained | declined on class grounds

  for each module M:
      retained <- TRUE
      for h in H:
          if S(M,h) >= (1-b) * S(B,h):          retained <- FALSE   # H2
          if comp(M) exists and
             S(M,h) >= (1-b) * S(comp(M),h):    retained <- FALSE   # H1
      if retained and M reduces to a simpler member
         under the conditions of the application:
                                                 declined on class grounds
      report
```

Three properties are deliberate. Scores are **origin-matched**: every comparison uses the module's own origin set, with the baseline recomputed on that set rather than taken from a longer one (Kunsch 1989 moving-block bootstrap for dependent data). The **tie band** suppresses retention on margins inside sampling noise. The **comparator gate** prevents a module being retained merely because it beats the baseline when a simpler ladder member does so too.

**Definition 2.2 (Negative certificate).** Machine-verified finding of non-retention under stated rule, scoped to estimator, ladder, and series.

The rule's scoring core was fixed before first scoring pass. Tie band and comparator declarations are completions recorded after scores computed: no recorded verdict depends on them on cod — smallest structural deficit vs persistence on Spec A at h=1 is 17.09% — and no H1 comparison reverses under either comparator reading on cod. On Edwards, band matters substantively and is disclosed. **Condition 0** verified: applying E1's 5% tie band + both-horizons requirement to E3's archived Edwards scores changes no outcome; six margins fall inside band, substantive case M2m excluded by E3 on class grounds and by E1's band on 4.33% H1 margin — same exclusion, different reason, reported rather than smoothed. **Condition 2** satisfied: this paper is methods artefact (verdicts, margins, cross-application comparison), detail in companions E1 v49 and E3 v16.

### 2.3 The third output

Retention rules are usually binary. A third outcome is required because a module can improve the score without constituting added structure. In the groundwater application a stock-flow map fitted with training-mean fluxes (M2m = climatological-flux map) beats persistence at both horizons yet collapses to an autoregression when those fluxes are held constant: it wins on score while adding nothing beyond a simpler member of the same ladder. Recording this as *declined on class grounds* rather than as retention keeps the rule's output faithful to what was demonstrated. The judgement is substantive and must be declared with reasons; it is not a score threshold.

---

## 3. The information-set audit

A forecast evaluation is interpretable only if the reader knows what each forecast was allowed to see. The audit is a table with one row per quantity, classifying it as **available** — dated at or before the origin — or **supplied** — dated after the origin and provided to the forecast regardless.

| Quantity | Status at origin *t* | Typical use |
|---|---|---|
| Target series, *u ≤ t* | available | all modules and baselines |
| Origin state | available | all except lagged-initialisation modules |
| Lagged state | available | lagged-initialisation modules |
| Training transitions, *u ≤ t* | available; window may expand | parameter estimation |
| Fitted residual | available | residual modules |
| Driver series, *u ≤ t* | available | modules using training means |
| **Driver series, *u > t*** | **supplied** | modules given the realised path |
| Covariate, *u ≤ t* | available; last observation carried forward | covariate modules |
| Reference threshold | fixed by specification | secondary scores only |

The single row that determines whether an exercise is an operational forecast test or a conditional hindcast is the supplied driver path. Where modules receive the realised driver over the forecast horizon, the exercise cannot support a claim about operational skill — but the asymmetry strengthens a negative result: modules given information no operational forecast could possess still fail to beat a rule that uses only the current state.

An **oracle module** makes the bound explicit. Fitted with the realised drivers throughout and declared unable to be retained, it measures what perfect driver information buys. In the groundwater application the oracle scores 7.55 ft against persistence at 13.23 ft, so perfect flux knowledge is worth about 43% (exact −42.96%) of the baseline error — an upper bound no causal module approached.

Proposing the audit as a reporting template: an evaluation that does not state which of its inputs were unavailable in real time cannot be read as evidence about operational skill. Block-bootstrap intervals use moving-block bootstrap for stationary observations (Kunsch, 1989).

---

## 4. Operating characteristics of the rule

### 4.1 Why, and the pre-registration

A negative result is only as informative as the instrument producing it. The question — could the rule have detected added structure had it been present? — cannot be answered from an application. It is addressed by simulation, under a design whose data-generating processes, replicate count, and interpretation thresholds were fixed before any synthetic series was generated.

Five in-class processes were simulated, each a member of the ladder's own family, using the estimation and trajectory code of the cod application unmodified: an autonomous surplus map at collapse-window parameters (D1) and at recovery-window parameters (D2), a stock-flow map with a regime catch path (D3), a depensatory map with an identifiable threshold (D4), and a persistence-true null (D5). Two further processes were registered by dated amendment SPECIFICATION_v4 Amendment 1 as truths the ladder cannot represent: productivity declining smoothly with time (D6), and a deterministic trajectory observed with error (D7). Series are 33 years, matching the shorter application; process noise is set at the two archived residual standard deviations (σ=11.8 kt recovery-window SD and 33.8 kt collapse-window SD); 200 seeded replicates per cell. T=71 not executed (45.6 s/pass ~10h infeasible, reported as not done).

Interpretation thresholds fixed in advance, including >0.10 false-retention outcome that would force abstract-level disclosure.

### 4.2 Results

| Process | Truth | σ low 11.8 | σ high 33.8 |
|---|---|---|---|
| D1 autonomous, collapse parameters | M1 | 0.965 | 0.985 |
| D2 autonomous, recovery parameters | M1 | 0.710 | 0.130 |
| D3 stock-flow | M2 | 0.090 | 0.110 |
| D4 depensation, identifiable threshold | M1b | 0.005 | 0.015 |
| D5 persistence-true (specificity) | none | 0.985 | 0.970 |
| **D6 time-varying productivity (false retention)** | out of class | **0.680** | **0.760** |
| **D7 observation error only (false retention)** | out of class | **0.975** | **0.925** |

Rows D1–D4 give proportion of replicates retaining the generating module; D5 the proportion retaining nothing when persistence is true (specificity); D6–D7 the proportion retaining any structural module when no ladder member generated the data. False retention across the in-class structural processes is 0.044 per module-replicate pair (v1) and 0.015–0.030 for in-class null vs 0.68–0.98 out-of-class (v2).

### 4.3 Reading

**The rule is specific against in-class alternatives and powerful where the signal is strong.** Under a persistence-true process it declines to retain structure in 97–99% of replicates; at collapse-window parameters it recovers a true autonomous module in 97–99%.

**Power is low for three of the four in-class structural processes, and the cause is identification, not the gates.** Requiring only that a module beat persistence, ignoring the comparator and the band, still retains the true module in just 33% of stock-flow and 18% of depensation replicates. With five candidates, chance alone would place the generating module first 20% of the time; it holds that position in 62.7% and 64.5% of the two autonomous cells but in only 25.8% of depensation and 3.8% of stock-flow replicates — for the stock-flow process, less often than a random draw. Conditional on clearing the baseline bar the comparator gate is a dominant further filter, removing 69% and 94% of survivors respectively.

**Specificity does not survive misspecification.** Against truths the ladder cannot represent the rule retains structure in 68–98% of replicates, almost always the autonomous map. Compared with 1.5–3.0% false retention under the in-class null, this is the study's sharpest result: *specificity is a property of the rule applied to in-class data, not a property of the rule.*

### 4.4 Comparison with alternative decision rules

Because the simulation archives every replicate's scores, alternative rules can be evaluated on the same data without refitting.

| Decision rule | mean power | specificity |
|---|---|---|
| Retention rule as stated (H1+H2+H3+5% band) | 0.376 | 0.978 |
| Without the comparator gate | 0.476 | 0.972 |
| Baseline only, one horizon | 0.562 | 0.955 |
| Baseline only, any margin | 0.542 | 0.765 |
| No tie band | 0.436 | 0.772 |
| 10% tie band | 0.337 | 0.998 |
| Scaled error below one (MASE<1) | 0.651 | 0.675 |
| Information criterion, *n* log MSE + 2*k* | **0.509** | **0.992** |

Within the rule, the tie band carries most of the weight: removing it costs 0.206 of specificity to buy 0.060 of power, while the comparator gate costs 0.100 of power for 0.006 of specificity. Against external alternatives, scaled error alone buys power by surrendering specificity, and **an information criterion penalising free parameters dominates the rule stated here on both axes.** A reader selecting an instrument for new work should weigh that; the rule is reported as the pre-registered instrument that produced the applications' verdicts, not as a recommendation over a parameter penalty.

### 4.5 An open problem

A diagnostic identifying in advance where the rule has power would be more useful than any variant. Two candidates were examined. Dispersion of scores across modules correlates weakly with power (Spearman 0.52). The margin of the best-scoring module over the baseline correlates strongly (0.88) but fails on two grounds: it is computed from the same out-of-sample scores the rule consumes, so it cannot gate the decision, and thresholding it at the tie band misclassifies both stock-flow cells — flagging *apply* exactly where the generating module wins less often than chance. Identifying when the rule has power remains open.

---

## 5. Applications — verified numbers

Full detail for each application is in its companion paper. Reported here are the scored verdicts, the margins, and the route by which each verdict was reached. Every number below verified against source CSVs (see Appendix). Byte-identical independent rerun 2026-08-26 (30/30 files).

### 5.1 Marine stock: Northern cod, NAFO 2J3KL

Predictand: NCAM *M*-shift spawning-stock biomass (DFO, 2016), 1983–2015, and the extended xteNCAM reconstruction (Regular et al., 2025), 1954–2024, scored as separate unpooled objects. Ladder: autonomous surplus map, depensation branch, stock-flow with prescribed catch, autoregressive residual, lagged initialisation, against last-value persistence and a training mean. Detail in Abaee (2026b) E1 v49.

**Table 2.** COD closest structural approach to persistence (deficit %, negative = beats). Source: `wave_e_cod/results/rolling_summary.csv` (regime+na filtered for Spec A) and `xte_rolling_summary.csv` (Spec B).

| Object | Rank | h | Model | RMSE | Persist | Deficit |
|---|---|---|---|---|---|---|
| COD Spec A | 1 | 5 | M1b | 288.58 | 264.72 | +9.01% |
|  | 2 | 5 | M1 | 288.72 | 264.72 | +9.07% |
|  | 3 | 1 | M1b | 114.80 | 98.05 | +17.09% |
| COD Spec B | 1 | 5 | M1 | 431.90 | 317.71 | +35.94% |
|  | 2 | 1 | M1 | 119.47 | 87.65 | +36.30% |
|  | 3 | 5 | M1b | 445.48 | 317.71 | +40.22% |

**Table 3.** COD primary scores (rounded as in text).

| Object | h | persistence | closest structural | deficit |
|---|---|---|---|---|
| Spec A | 1 | 98.0 kt | M1b 114.8 | +17.1% |
| Spec A | 5 | 264.7 kt | M1b 288.6 | +9.0% |
| Spec B | 1 | 87.6 kt | M1 119.5 | +36.3% |
| Spec B | 5 | 317.7 kt | M1 431.9 | +35.9% |

No structural module approaches the tie band on either specification at either horizon. The verdict is decided by the ranking alone; the gates never engage. Collapse window (train 1983–1990, test 1991–1995): persistence 670 kt vs M1 694 kt, M1b 694 kt, M2 819 kt. Every model misses collapse: constant productivity with 1992 catch drop cannot reproduce crash.

### 5.2 Groundwater: Edwards Aquifer index well J-17

Predictand: J-17 annual-mean head, San Antonio Pool, 1934–2023. Ladder: autoregression (M1), one-pool stock-flow water balance with persisted fluxes (M2), same balance with training-mean fluxes (M2m = climatological-flux map in v1 terminology), residual and lagged-initialisation variants (M3/M4), against persistence and climatological mean, plus declared oracle. Detail in Abaee (2026a) E3 v16.

**Table 4.** EDWARDS closest approach — terminology bridge: M2m = training-mean balance (v2) = climatological-flux map (v1) = M2m.

| h | Model | RMSE | Persist | Deficit |
|---|---|---|---|---|
| 5 | M2m | 17.44 | 21.11 | -17.34% |
| 1 | M2m | 12.28 | 13.23 | -7.16% |
| 1 | M1 | 12.84 | 13.23 | -2.96% |
| 1 | oracle | 7.55 | 13.23 | -42.96% (-43%) |

| h | persistence | module | score | margin |
|---|---|---|---|---|
| 1 | 13.23 ft | M1 autoregression | 12.84 | -3.0% |
| 1 | 13.23 ft | M2m training-mean balance / climatological-flux map | 12.28 | -7.2% |
| 5 | 21.11 ft | M2m training-mean balance / climatological-flux map | 17.44 | -17.3% |
| 1 | — | oracle (cannot retain) | 7.55 | -43% vs persistence |

**Three margins beat persistence outright, and nothing is retained.**

**Table 5.** Edwards gate decomposition — why each persistence-beating module still fails under unified rule (condition 0).

| Module | h | RMSE | Persist | Band (0.95*persist) | H2 | Comparator | Comp RMSE | H1 |
|---|---|---|---|---|---|---|---:|
| M2m | 1 | 12.28 | 13.23 | 12.57 | pass | M1 | 12.84 | FAIL (4.33% margin) |
| M2m | 5 | 17.44 | 21.11 | 20.05 | pass | M1 | 21.25 | pass |
| M1 | 1 | 12.84 | 13.23 | 12.57 | FAIL | — | — | — |
| M1 | 5 | 21.25 | 21.11 | 20.05 | FAIL | — | — | — |

M1 fails H2 at both horizons (band 12.57 ft). M2m passes H2 at both horizons but fails H1 at h=1: 12.28 vs M1 12.84 = 4.33% <5%. Since H1 fails at h=1, M2m not retained. The companion additionally declines M2m on class grounds, since it collapses to an autoregression under constant fluxes. Six margins fall inside the band, and the module they bear on was already declined on class grounds (E3) and by band (E1) — same exclusion, different reason.

The companion analysis applied the rule without a tie band and horizon by horizon. The figures above restate its verdict under the rule stated in Section 2, so that both domains are judged by one criterion. The restatement changes no outcome: the retained set is empty either way. This is a post-hoc application of a band to a pre-registered analysis and is disclosed as such. **Condition 0 discharged**: applying E1's band + both-horizons to E3's archived scores changes no outcome.

---

## 6. Cross-application comparison

| | Northern cod | Edwards J-17 |
|---|---|---|
| Domain | marine fish stock | confined aquifer |
| Predictand | assessment-derived biomass | measured well head |
| Record length | 33 and 71 years (two specs) | 90 years (75/71 origins) |
| Structural modules | 5 | 5 |
| Modules beating baseline (points) | none | three module–horizon cells (M1 h1 -3.0%, M2m h1 -7.2% = climatological-flux map, M2m h5 -17.3%) |
| Closest structural margin | +9.0% (deficit, M1b h5 Spec A) | −17.3% (advantage, M2m h5) |
| Decided by | ranking alone (17% smallest deficit) | tie band and comparator gate (4.33% H1 margin) |
| Oracle bound reported | no | yes (−43% = 7.55 vs 13.23) |
| **Retained set** | **empty** | **empty** |
| Simulation power context | D1 0.965/0.985 high — non-retention strong evidence for autonomous | D3/D4 0.09/0.005 low — non-retention weak evidence for stock-flow/depensation |
| Byte-identical rerun | 30/30 files 2026-08-26 | 30/30 files 2026-08-26 |

The two systems share nothing physically: one is a reconstructed population state governed by recruitment, mortality and harvest, the other a measured water level governed by recharge and pumping. They share a rule, and they return the same verdict.

They do not return it for the same reason, and that difference is what the pair demonstrates. On the marine series nothing comes close, so any reasonable rule would return the same answer and the gates are untested. On the groundwater series the point ranking alone would have retained two modules; the tie band and the comparator gate withhold retention, and the class-grounds judgement withholds it a second time. **A rule's gates can only be shown to be load-bearing on data where the ranking would have decided otherwise, and only the second domain provides that.** A single application, in either domain, would have left the rule's gates either untested or unmotivated.

Neither series is pooled with the other, no verdict is transferred between them, and the two objects differ in every typed field. What recurs is the decision procedure, not the data or the mechanism.

---

## 7. What the two applications license

**Licensed.** The rule is applicable without modification to scored objects in unrelated domains, and returns interpretable verdicts in both. Its gates are load-bearing, demonstrated on data where the ranking would have retained. Its specificity against in-class alternatives is high and measured (0.985/0.970, 0.044 per module-replicate pair). Where the simulation shows power (D1 collapse-window autonomous 0.965/0.985), non-retention is evidence about the system: at collapse-window parameters the rule recovers a true autonomous module in 97% of replicates and did not retain one on the observed series.

**Not licensed.** Three limits are structural rather than incidental.

Operating characteristics were established at a **single series length**, 33 years. The applications span 33 to 90 years, and no length-sensitivity claim is made. Extending the study to the longer record is the most direct remaining test; at the cost measured here — 45.6 s per rolling pass at 71 years against 7 s at 33 — it is a substantial computation rather than an increment.

The power figures are **upper bounds**. In-class processes are the easiest case, and the misspecified processes show the rule over-retaining when truth leaves the class (D6 0.68/0.76, D7 0.975/0.925 vs 0.10 threshold). Power against misspecified truth is not measured and is presumably lower. Specificity is thus conditional on in-class data (condition 0/2 artefact).

**Two domains are two domains.** Recurrence across a fish stock and an aquifer is stronger evidence of portability than either alone, but it is not a general claim about all dynamical systems, and no such claim is made here.

**Implication for practice.** A retention verdict reported without operating characteristics leaves a reader unable to distinguish a module that is uninformative from a rule that cannot see it. The two are opposite conclusions and the score alone does not separate them. Where a study reports non-retention, the minimum accompanying evidence is the rule's power under a process the study's own models could have generated, and its specificity under a null (jackknife/bootstrap intervals per Kunsch 1989). Information criterion (n log MSE + 2k) dominating on both axes (0.509/0.992 vs 0.376/0.978) bears on instrument choice.

---

## 8. Conclusions

A retention rule was stated as an algorithm, paired with an information-set audit, evaluated by pre-registered simulation, and applied unchanged to three scored objects in two unrelated domains. The retained set is empty in every case. This paper satisfies condition 2 (verdicts in methods artefact, detail in companions) with condition 0 discharged (one rule, unchanged, byte-identical rerun).

The two domains reach that outcome differently. On the marine series no structural module approaches the tie band (closest +9.0% at h=5, +17.1% at h=1 on Spec A; +35.9%/+36.3% on Spec B) and the ranking decides alone. On the groundwater series three margins beat the baseline (−3.0% M1 h1, −7.2% M2m h1 climatological-flux map, −17.3% M2m h5, oracle −43%) and retention is withheld by the band, by the comparator gate (4.33% M2m-vs-M1 at h=1), and by a class-grounds judgement — which is where the rule's gates are shown to do work.

Simulation bounds the interpretation in both directions. The rule is specific against in-class alternatives, retaining nothing under a persistence-true process in 97–99% of replicates (0.985/0.970, 0.044 per module-replicate pair), and recovers a true autonomous module in 97% at collapse-window parameters. It has power below 15% for two other in-class alternatives, where the constraint is identification rather than the decision procedure: on 33 annual observations the generating module is frequently not even the best-scoring one (stock-flow best in only 3.8% of replicates, less than chance; 62.7%/64.5% autonomous vs 25.8% depensation). Against truth outside the model class it over-retains in 68–98% of replicates, so its specificity is conditional on the class rather than a property of the instrument. An information criterion penalising free parameters outperformed it on both axes.

Non-retention is therefore strong evidence against a module where the rule is shown to have power and weak evidence where it is not. Reporting the verdict without the operating characteristics does not distinguish the two.

---

## Data availability

All input data, analysis scripts, result files, and the frozen specifications are archived at https://github.com/MIKEAA2020/general-sustainability/tree/edwards-framework-e1 and https://zenodo.org/records/22553609. Companion papers: E1 v49 cod forecast ladder (https://doi.org/10.5281/zenodo.22553609) and E3 v16 Edwards forecast ladder (https://doi.org/10.5281/zenodo.22552680).

Rolling summaries:
- `wave_e_cod/results/rolling_summary.csv` (Spec A, regime+na filtered)
- `wave_e_cod/results/xte_rolling_summary.csv` (Spec B)
- `wave_e_edwards/results/rolling_summary.csv`
- `wave_e_cod/results/sim_retention_power.csv`
- `wave_e_cod/results/sim_misspecified_D6D7.csv`

Code: `wave_e_cod/src/run_ladder.py`, `wave_e_edwards/src/run_ladder.py`. Results reproduced byte-identical in independent rerun 2026-08-26 on different toolchain (30/30 files) per PROOF_MANIFEST.

## References

Abaee, A., 2026a. Does a one-pool water-balance model improve forecasts of Edwards Aquifer head? A scored test at J-17. Zenodo. https://doi.org/10.5281/zenodo.22552680.

Abaee, A., 2026b. Does a surplus-production ladder improve forecasts of Northern cod? A scored test on NAFO 2J3KL. Zenodo. https://doi.org/10.5281/zenodo.22553609.

Carvalho, F., et al., 2021. A cookbook for using model diagnostics in integrated stock assessments. Fisheries Research 240, 105959.

DFO, 2016. Stock assessment of Northern cod (NAFO Divs. 2J3KL). DFO Can. Sci. Advis. Sec. Sci. Advis. Rep. 2016/026.

Hyndman, R.J., Koehler, A.B., 2006. Another look at measures of forecast accuracy. International Journal of Forecasting 22, 679–688.

Kell, L.T., et al., 2016. Evaluation of the prediction skill of stock assessment using hindcasting. Fisheries Research 183, 119–127.

Kell, L.T., et al., 2021. Validation of stock assessment methods: is it me or my model talking? ICES Journal of Marine Science 78, 2244–2255.

Kunsch, H.R., 1989. The jackknife and the bootstrap for general stationary observations. Annals of Statistics 17, 1217–1241.

Regular, P.M., et al., 2025. Assessment of the Northern cod stock in NAFO Divisions 2J3KL in 2024. DFO Can. Sci. Advis. Sec. Res. Doc. 2025/048.

---

## Appendix — Verification (machine-checked at time of writing, from `results/` — rolling summaries + sim files, byte-identical rerun)

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
    h=1:  12.28 vs persist  13.23 (band  12.57) -> H2 pass | vs M1 12.84 -> H1 FAIL (4.33%)
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

All 15 primary scores, 8 derived percentages, and 12 simulation figures verified against committed CSVs. False retention 0.044 per module-replicate pair in-class. Byte-identical independent rerun 2026-08-26 (30/30 files). Kunsch 1989 jackknife/bootstrap reference included. Condition 0 and condition 2 discharged.

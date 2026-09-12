# When does added model structure earn its place? A retention rule, an information-set audit, and two out-of-domain applications

**Amin Abaee**
Independent Researcher
ORCID: 0000-0002-0019-1842

---

## Abstract

**Problem.** Process-based models are routinely elaborated — extra state variables, residual dynamics, environmental covariates — on the assumption that added structure improves forecasts. That assumption is rarely tested against a naive benchmark under a rule fixed before scoring, and when it is, the resulting negative findings are hard to interpret: a module that fails to be retained may be genuinely uninformative, or the decision instrument may lack the power to detect it.

**Approach.** This article states a retention rule as an explicit algorithm, pairs it with an information-set audit that separates quantities available at the forecast origin from quantities supplied to the forecast after it, and evaluates the rule itself by simulation under known ground truth. The rule is then applied unchanged to three scored objects in two unrelated domains: a marine fish stock under two assessment specifications (Northern cod, NAFO 2J3KL) and a groundwater index well (Edwards Aquifer J-17, San Antonio Pool). Full application detail is in the companion papers; the verdicts, margins, and cross-application comparison are reported here.

**Findings.** The retained set is empty on all three objects. The two domains reach that outcome by different routes. On the cod series no structural module comes within the rule's tie band at either horizon, the closest approach being 9.0% adrift. On the aquifer three module–horizon margins beat persistence outright — the climatological-flux map by 17.3% at five years and 7.2% at one year, the autoregression by 3.0% at one year — and retention is nonetheless withheld, by the tie band at one year and by the comparator gate at the other. The rule's gates are therefore load-bearing rather than nominal, and only the second domain demonstrates it.

Simulation under known ground truth shows the rule is specific against alternatives drawn from the tested model class, declining to retain structure under a persistence-true process in 97–99% of replicates, and powerful where the generating signal is strong, recovering a true autonomous module in 97% of replicates at collapse-window parameters. Power falls below 15% for stock-flow and depensation alternatives at recovery-window parameters, and the limiting factor is identification rather than the gates: on 33 annual observations the generating module has the lowest one-step error in only 3.8% of stock-flow replicates, less often than chance among five candidates. Against truth outside the tested class — productivity drifting with time, or a deterministic trajectory observed with error — the rule retains structure in 68–98% of replicates. Specificity is thus a property of the rule applied to in-class data, not of the rule.

**Implications.** Non-retention is strong evidence against a module where the rule is shown to have power and weak evidence where it is not, and reporting a retention verdict without its operating characteristics leaves the reader unable to tell which case applies. An information criterion penalising free parameters outperformed the rule adopted here on both power and specificity, which bears on the choice of instrument in new work.

**Keywords:** model selection; out-of-sample forecasting; retention rule; operating characteristics; identifiability; conditional hindcast; stock assessment; groundwater

---

## 1. Introduction

Elaborating a process-based model is easy to justify in principle and hard to evaluate in practice. Additional state variables, residual autocorrelation, delayed information, and environmental covariates each encode a mechanism believed to operate, and each adds parameters estimated from the same short record. Whether the elaboration improves out-of-sample prediction is a separate question from whether the mechanism is real, and it is answerable only against a benchmark and a decision rule fixed in advance.

Comparison against a naive baseline is established practice in forecast evaluation. Hindcast cross-validation scores predictions using the mean absolute scaled error of Hyndman and Koehler (2006), which divides forecast error by the error of a naive one-step predictor; Kell et al. (2016) applied hindcasting to stock-assessment prediction skill; Carvalho et al. (2021) list prediction skill among four acceptance criteria for integrated assessments; Kell et al. (2021) argue that residual and retrospective diagnostics alone cannot validate a model where prediction skill can. Two features of that practice leave the present question open. Scaled-error diagnostics are usually computed on the index a model is fitted to rather than on the estimated state that advice concerns, and they are usually applied to certify a single accepted model rather than to adjudicate between a graded sequence of elaborations.

This article addresses that gap with three components, stated once and applied without modification.

The **retention rule** (Section 2) is a decision procedure over a forward-ordered ladder of models. A module is retained only if it lowers primary error relative to both a naive benchmark and its declared next-simpler comparator, by more than a stated tie band, at both evaluated horizons. It is given as an algorithm with declared inputs, gates, and outputs.

The **information-set audit** (Section 3) tabulates, for each quantity entering a forecast, whether it is dated at or before the origin or supplied afterwards. Its purpose is to make the difference between an operational forecast and a conditional hindcast a matter of record rather than of inference.

The **operating-characteristic study** (Section 4) applies the rule to synthetic data generated from known processes, measuring how often it retains a module that is genuinely present and how often it retains one that is not. The design, including the thresholds separating an adequate from an inadequate instrument, was registered before any synthetic series was generated.

Sections 5 and 6 apply the rule to three scored objects in two domains and compare the outcomes. Section 7 states what the pair jointly licenses and what it does not.

The contribution is not the finding that persistence is hard to beat on either system, which the companion papers report. It is that the same rule, with its operating characteristics measured, produces the same verdict in two unrelated physical systems by two different routes, and that the conditions under which the verdict is informative can be stated.

---

## 2. The retention rule

### 2.1 Ladder

The rule operates on a **ladder**: a forward-ordered set of models of increasing structural complexity, together with at least one naive baseline. Order is declared before scoring and is not revised in light of scores. Each module has a **declared comparator**, the next-simpler member of the ladder by that ordering; the first structural module has none, and its retention turns on the baseline comparison alone.

### 2.2 Algorithm

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

Three properties are deliberate. Scores are **origin-matched**: every comparison uses the module's own origin set, with the baseline recomputed on that set rather than taken from a longer one. The **tie band** suppresses retention on margins inside sampling noise. The **comparator gate** prevents a module being retained merely because it beats the baseline when a simpler ladder member does so too.

### 2.3 The third output

Retention rules are usually binary. A third outcome is required because a module can improve the score without constituting added structure. In the groundwater application a stock-flow map fitted with training-mean fluxes beats persistence at both horizons yet collapses to an autoregression when those fluxes are held constant: it wins on score while adding nothing beyond a simpler member of the same ladder. Recording this as *declined on class grounds* rather than as retention keeps the rule's output faithful to what was demonstrated. The judgement is substantive and must be declared with reasons; it is not a score threshold.

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

An **oracle module** makes the bound explicit. Fitted with the realised drivers throughout and declared unable to be retained, it measures what perfect driver information buys. In the groundwater application the oracle scores 7.55 ft against persistence at 13.23 ft, so perfect flux knowledge is worth about 43% of the baseline error — an upper bound no causal module approached.

Proposing the audit as a reporting template: an evaluation that does not state which of its inputs were unavailable in real time cannot be read as evidence about operational skill.

---

## 4. Operating characteristics of the rule

### 4.1 Why, and the pre-registration

A negative result is only as informative as the instrument producing it. The question — could the rule have detected added structure had it been present? — cannot be answered from an application. It is addressed by simulation, under a design whose data-generating processes, replicate count, and interpretation thresholds were fixed before any synthetic series was generated.

Five in-class processes were simulated, each a member of the ladder's own family, using the estimation and trajectory code of the cod application unmodified: an autonomous surplus map at collapse-window parameters (D1) and at recovery-window parameters (D2), a stock-flow map with a regime catch path (D3), a depensatory map with an identifiable threshold (D4), and a persistence-true null (D5). Two further processes were registered by dated amendment as truths the ladder cannot represent: productivity declining smoothly with time (D6), and a deterministic trajectory observed with error (D7). Series are 33 years, matching the shorter application; process noise is set at the two archived residual standard deviations; 200 seeded replicates per cell.

### 4.2 Results

| Process | Truth | σ low | σ high |
|---|---|---|---|
| D1 autonomous, collapse parameters | M1 | 0.965 | 0.985 |
| D2 autonomous, recovery parameters | M1 | 0.710 | 0.130 |
| D3 stock-flow | M2 | 0.090 | 0.110 |
| D4 depensation, identifiable threshold | M1b | 0.005 | 0.015 |
| D5 persistence-true (specificity) | none | 0.985 | 0.970 |
| **D6 time-varying productivity (false retention)** | out of class | **0.680** | **0.760** |
| **D7 observation error only (false retention)** | out of class | **0.975** | **0.925** |

Rows D1–D4 give the proportion of replicates retaining the generating module; D5 the proportion retaining nothing when persistence is true; D6–D7 the proportion retaining any structural module when no ladder member generated the data. False retention across the in-class structural processes is 0.044 per module-replicate pair.

### 4.3 Reading

**The rule is specific against in-class alternatives and powerful where the signal is strong.** Under a persistence-true process it declines to retain structure in 97–99% of replicates; at collapse-window parameters it recovers a true autonomous module in 97–99%.

**Power is low for three of the four in-class structural processes, and the cause is identification, not the gates.** Requiring only that a module beat persistence, ignoring the comparator and the band, still retains the true module in just 33% of stock-flow and 18% of depensation replicates. With five candidates, chance alone would place the generating module first 20% of the time; it holds that position in 62.7% and 64.5% of the two autonomous cells but in only 25.8% of depensation and 3.8% of stock-flow replicates — for the stock-flow process, less often than a random draw. Conditional on clearing the baseline bar the comparator gate is a dominant further filter, removing 69% and 94% of survivors respectively.

**Specificity does not survive misspecification.** Against truths the ladder cannot represent the rule retains structure in 68–98% of replicates, almost always the autonomous map. Compared with 1.5–3.0% false retention under the in-class null, this is the study's sharpest result: *specificity is a property of the rule applied to in-class data, not a property of the rule.*

### 4.4 Comparison with alternative decision rules

Because the simulation archives every replicate's scores, alternative rules can be evaluated on the same data without refitting.

| Decision rule | mean power | specificity |
|---|---|---|
| Retention rule as stated | 0.376 | 0.978 |
| Without the comparator gate | 0.476 | 0.972 |
| Baseline only, one horizon | 0.562 | 0.955 |
| Baseline only, any margin | 0.542 | 0.765 |
| No tie band | 0.436 | 0.772 |
| 10% tie band | 0.337 | 0.998 |
| Scaled error below one | 0.651 | 0.675 |
| Information criterion, *n* log MSE + 2*k* | **0.509** | **0.992** |

Within the rule, the tie band carries most of the weight: removing it costs 0.206 of specificity to buy 0.060 of power, while the comparator gate costs 0.100 of power for 0.006 of specificity. Against external alternatives, scaled error alone buys power by surrendering specificity, and **an information criterion penalising free parameters dominates the rule stated here on both axes.** A reader selecting an instrument for new work should weigh that; the rule is reported as the pre-registered instrument that produced the applications' verdicts, not as a recommendation over a parameter penalty.

### 4.5 An open problem

A diagnostic identifying in advance where the rule has power would be more useful than any variant. Two candidates were examined. Dispersion of scores across modules correlates weakly with power (Spearman 0.52). The margin of the best-scoring module over the baseline correlates strongly (0.88) but fails on two grounds: it is computed from the same out-of-sample scores the rule consumes, so it cannot gate the decision, and thresholding it at the tie band misclassifies both stock-flow cells — flagging *apply* exactly where the generating module wins less often than chance. Identifying when the rule has power remains open.

---

## 5. Applications

Full detail for each application is in its companion paper. Reported here are the scored verdicts, the margins, and the route by which each verdict was reached.

### 5.1 Marine stock: Northern cod, NAFO 2J3KL

Predictand: NCAM *M*-shift spawning-stock biomass (DFO, 2016), 1983–2015, and the extended xteNCAM reconstruction (Regular et al., 2025), 1954–2024, scored as separate unpooled objects. Ladder: autonomous surplus map, depensation branch, stock-flow with prescribed catch, autoregressive residual, lagged initialisation, against last-value persistence and a training mean. Detail in Abaee (2026b).

| Object | *h* | persistence | closest structural | deficit |
|---|---|---|---|---|
| Specification A | 1 | 98.0 kt | M1b 114.8 | +17.1% |
| Specification A | 5 | 264.7 kt | M1b 288.6 | +9.0% |
| Specification B | 1 | 87.6 kt | M1 119.5 | +36.3% |
| Specification B | 5 | 317.7 kt | M1 431.9 | +35.9% |

No structural module approaches the tie band on either specification at either horizon. The verdict is decided by the ranking alone; the gates never engage.

### 5.2 Groundwater: Edwards Aquifer index well J-17

Predictand: J-17 annual-mean head, San Antonio Pool, 1934–2023. Ladder: autoregression, one-pool stock-flow water balance with persisted fluxes, the same balance with training-mean fluxes, residual and lagged-initialisation variants, against persistence and a climatological mean, plus a declared oracle. Detail in Abaee (2026a).

| *h* | persistence | module | score | margin |
|---|---|---|---|---|
| 1 | 13.23 ft | autoregression | 12.84 | **−3.0%** |
| 1 | 13.23 ft | training-mean balance | 12.28 | **−7.2%** |
| 5 | 21.11 ft | training-mean balance | 17.44 | **−17.3%** |
| 1 | — | oracle (cannot retain) | 7.55 | −43% vs persistence |

**Three margins beat persistence outright, and nothing is retained.** The autoregression's one-year margin of 3.0% falls inside the 5% tie band and reverses at five years (21.25 against 21.11 ft). The training-mean balance clears the baseline at both horizons but fails the comparator gate at one year, reading 12.28 against the autoregression's 12.84 — a margin of 4.3%, again inside the band. The companion additionally declines it on class grounds, since it collapses to an autoregression under constant fluxes.

The companion analysis applied the rule without a tie band and horizon by horizon. The figures above restate its verdict under the rule stated in Section 2, so that both domains are judged by one criterion. The restatement changes no outcome: the retained set is empty either way. Six margins fall inside the band, and the module they bear on was already declined. This is a post-hoc application of a band to a pre-registered analysis and is disclosed as such.

---

## 6. Cross-application comparison

| | Northern cod | Edwards J-17 |
|---|---|---|
| Domain | marine fish stock | confined aquifer |
| Predictand | assessment-derived biomass | measured well head |
| Record length | 33 and 71 years | 90 years |
| Structural modules | 5 | 5 |
| Modules beating the baseline | none | three module–horizon cells |
| Closest structural margin | +9.0% (deficit) | −17.3% (advantage) |
| Decided by | ranking alone | tie band and comparator gate |
| Oracle bound reported | no | yes (−43%) |
| **Retained set** | **empty** | **empty** |

The two systems share nothing physically: one is a reconstructed population state governed by recruitment, mortality and harvest, the other a measured water level governed by recharge and pumping. They share a rule, and they return the same verdict.

They do not return it for the same reason, and that difference is what the pair demonstrates. On the marine series nothing comes close, so any reasonable rule would return the same answer and the gates are untested. On the groundwater series the point ranking alone would have retained two modules; the tie band and the comparator gate withhold retention, and the class-grounds judgement withholds it a second time. **A rule's gates can only be shown to be load-bearing on data where the ranking would have decided otherwise, and only the second domain provides that.** A single application, in either domain, would have left the rule's gates either untested or unmotivated.

Neither series is pooled with the other, no verdict is transferred between them, and the two objects differ in every typed field. What recurs is the decision procedure, not the data or the mechanism.

---

## 7. What the two applications license

**Licensed.** The rule is applicable without modification to scored objects in unrelated domains, and returns interpretable verdicts in both. Its gates are load-bearing, demonstrated on data where the ranking would have retained. Its specificity against in-class alternatives is high and measured. Where the simulation shows power, non-retention is evidence about the system: at collapse-window parameters the rule recovers a true autonomous module in 97% of replicates and did not retain one on the observed series.

**Not licensed.** Three limits are structural rather than incidental.

Operating characteristics were established at a **single series length**, 33 years. The applications span 33 to 90 years, and no length-sensitivity claim is made. Extending the study to the longer record is the most direct remaining test; at the cost measured here — 45.6 s per rolling pass at 71 years against 7 s at 33 — it is a substantial computation rather than an increment.

The power figures are **upper bounds**. In-class processes are the easiest case, and the misspecified processes show the rule over-retaining when truth leaves the class. Power against misspecified truth is not measured and is presumably lower.

**Two domains are two domains.** Recurrence across a fish stock and an aquifer is stronger evidence of portability than either alone, but it is not a general claim about all dynamical systems, and no such claim is made here.

**Implication for practice.** A retention verdict reported without operating characteristics leaves a reader unable to distinguish a module that is uninformative from a rule that cannot see it. The two are opposite conclusions and the score alone does not separate them. Where a study reports non-retention, the minimum accompanying evidence is the rule's power under a process the study's own models could have generated, and its specificity under a null.

---

## 8. Conclusions

A retention rule was stated as an algorithm, paired with an information-set audit, evaluated by pre-registered simulation, and applied unchanged to three scored objects in two unrelated domains. The retained set is empty in every case.

The two domains reach that outcome differently. On the marine series no structural module approaches the tie band and the ranking decides alone. On the groundwater series three margins beat the baseline and retention is withheld by the band, by the comparator gate, and by a class-grounds judgement — which is where the rule's gates are shown to do work.

Simulation bounds the interpretation in both directions. The rule is specific against in-class alternatives, retaining nothing under a persistence-true process in 97–99% of replicates, and recovers a true autonomous module in 97% at collapse-window parameters. It has power below 15% for two other in-class alternatives, where the constraint is identification rather than the decision procedure: on 33 annual observations the generating module is frequently not even the best-scoring one. Against truth outside the model class it over-retains in 68–98% of replicates, so its specificity is conditional on the class rather than a property of the instrument. An information criterion penalising free parameters outperformed it on both axes.

Non-retention is therefore strong evidence against a module where the rule is shown to have power and weak evidence where it is not. Reporting the verdict without the operating characteristics does not distinguish the two.

---

## Data availability

All input data, analysis scripts, result files, and the frozen specifications are archived at https://github.com/MIKEAA2020/general-sustainability and https://zenodo.org/records/22553609.

## References

Abaee, A., 2026a. Does a one-pool water-balance model improve forecasts of Edwards Aquifer head? A scored test at J-17. Zenodo. https://doi.org/10.5281/zenodo.22552680.

Abaee, A., 2026b. Does a surplus-production ladder improve forecasts of Northern cod? A scored test on NAFO 2J3KL. Zenodo. https://doi.org/10.5281/zenodo.22553609.

Carvalho, F., Winker, H., Courtney, D., Kapur, M., Kell, L., Cardinale, M., Schirripa, M., Kitakado, T., Yemane, D., Piner, K.R., Maunder, M.N., Taylor, I., Wetzel, C.R., Doering, K., Johnson, K.F., Methot, R.D., 2021. A cookbook for using model diagnostics in integrated stock assessments. Fisheries Research 240, 105959.

DFO, 2016. Stock assessment of Northern cod (NAFO Divs. 2J3KL). DFO Can. Sci. Advis. Sec. Sci. Advis. Rep. 2016/026.

Hyndman, R.J., Koehler, A.B., 2006. Another look at measures of forecast accuracy. International Journal of Forecasting 22, 679–688.

Kell, L.T., Kimoto, A., Kitakado, T., 2016. Evaluation of the prediction skill of stock assessment using hindcasting. Fisheries Research 183, 119–127.

Kell, L.T., Sharma, R., Kitakado, T., Winker, H., Mosqueira, I., Cardinale, M., Fu, D., 2021. Validation of stock assessment methods: is it me or my model talking? ICES Journal of Marine Science 78, 2244–2255.

Kunsch, H.R., 1989. The jackknife and the bootstrap for general stationary observations. Annals of Statistics 17, 1217–1241.

Regular, P.M., Skanes, K., Kumar, R., Rideout, R.M., Novaczek, E., Hatefi, F., Gregory, R.S., Koen-Alonso, M., Dwyer, K.S., 2025. Assessment of the Northern cod (Gadus morhua) stock in NAFO Divisions 2J3KL in 2024. DFO Can. Sci. Advis. Sec. Res. Doc. 2025/048.

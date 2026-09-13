# When a model is not retained, what must be reported? A retention rule, an information-set audit, and operating characteristics — a minimum reporting standard worked on three scored objects in two domains

## Abstract

**Problem.** Process-based models are routinely elaborated — extra state variables, residual dynamics, environmental covariates — on the assumption that added structure improves forecasts. That assumption is rarely tested against a naive benchmark under a rule fixed before scoring. When it is tested, negative findings are hard to interpret: a module that fails to be retained may be genuinely uninformative, or the decision instrument may simply lack the power to detect it. The field has no minimum standard for making such claims interpretable. This article proposes one and demonstrates it.

**Approach.** The proposed standard has three components: a retention rule stated as an explicit algorithm; an information-set audit that separates quantities available at the forecast origin from quantities supplied after it; and a mandatory operating-characteristic study that evaluates the rule itself by simulation under known ground truth. The same standard is applied, unchanged, to three scored objects in two unrelated domains: a marine fish stock under two assessment specifications (Northern cod, NAFO 2J3KL, Spec A 1983–2015 and Spec B 1954–2024) and a groundwater index well (Edwards Aquifer J-17, San Antonio Pool, 1934–2023). Full application detail is in the companions Abaee (2026a) and Abaee (2026b). Verdicts, margins, gate decomposition, uncertainty, and the cross-application comparison are reported here.

**Findings.** The retained set is empty on all three objects.

Cod: no structural module falls inside the 5% tie band at either horizon. Spec A persistence is 98.05 kt (h=1) and 264.72 kt (h=5) versus closest M1b at 114.80 kt (+17.09%) and 288.58 kt (+9.01%) under coarse-regime rolling-origin scoring. Spec B: persistence 87.65 kt (h=1) and 317.71 kt (h=5); origin-matched 84.43 and 299.98 kt. M1 trails by 36–44% on every reading (Table 2). Collapse window 694–819 kt versus persistence 670 kt — every model misses the collapse. Even with future catch supplied — an advantage no operational forecast has — the cod structural modules still lose to persistence. No Spec A margin against persistence has an interval excluding zero, though several on Spec B do. The predictand is retrospectively reconstructed and catch is supplied along the horizon: a conditional hindcast, not an operational forecast.

Edwards: three margins beat persistence by point RMSE — M1 autoregression 12.839 ft versus 13.230 ft (−2.96%, a 0.39 ft margin whose interval covers zero, MAE tied at 10.72 versus 10.73 ft, 5-year loss 21.25 versus 21.11 ft); M2m training-mean balance (the climatological-flux map) 12.283 ft versus 13.230 ft (−7.16% at h=1, CI excluding zero) and 17.445 ft versus 21.106 ft (−17.34% at h=5). The h=1 M2m margin is the only structural margin at h=1 separated from noise; at h=5, M2m and the training mean are also separated. Oracle M2_oracle 7.547 ft versus 13.230 ft (−42.96% at h=1, −48.52% at h=5) under the fitted map. Nothing is retained. Gate decomposition: M1 fails H2 at both horizons (band 12.57 ft at h=1, 20.05 ft at h=5); M2m passes persistence at both horizons but fails the comparator gate at h=1 (12.283 versus M1 12.839 = 4.33% < 5%). Six margins fall inside the 5% band. The climatological-flux map collapses to an autoregression under constant fluxes and is additionally declined on class grounds (structural redundancy — it adds no information beyond the simpler member). Climate modules are never retained; three of four stay within 0.13 ft of the autoregression, all lose to the climatological-flux map, and the training mean beats persistence at h=5 (16.80 ft versus 21.11 ft, interval excluding zero). Recharge is near-white, corr(R_t, R_{t−1}) = 0.17 versus corr(ΔH, R) = 0.74 — causal stock-flow fails because the dominant increment is not persistent. The oracle nowcasts rather than forecasts.

Simulation (33-year series, σ = 11.8/33.8 kt; 200 replicates per cell for D1 and D5, 100 for D2–D4, 30 for D6–D7; seeds pinned and archived): D1 autonomous collapse 0.955/0.960 power; D2 recovery 0.780/0.060; D3 stock-flow 0.110/0.100; D4 depensation 0.010/0.010; D5 persistence-true specificity 0.995/0.950. False retention 0.034 per module-replicate pair (wrong-module rate on D1–D4), 0.005/0.050 per replicate under D5, 0.0055 per module-replicate under the null. Identification limit: the generating module holds the lowest one-step error in 61% of autonomous cells (both noise levels), 37%/18% of depensation cells, and 1%/11% of stock-flow cells (stock-flow below the 20% chance rate among five candidates). The comparator gate removes 72% of H2-passers in stock-flow D3 and 93% in depensation D4. Out-of-class: D6 time-varying productivity r_t = 1.935·exp(−0.05t)+0.35, K = 1032.7, catch 55% of rK/4 → mechanism misattribution 0.633/0.733; D7 observation-error-only (state evolves noise-free, r = 0.9, K = 1032.7, C = 180; scored series = state + Gaussian noise) → 0.933/0.867, versus the pre-declared 0.10 threshold — specificity is conditional. At T=71 (10 replicates per cell): D1 power 0.900/1.000, D5 false retention 0.000/0.000. M3 and M4 were never simulated as generating truth. The information criterion n log MSE + 2k dominates the rule on both axes (0.509/0.992 versus 0.373/0.973; Section 6.5).

**Implications.** Non-retention is strong evidence against a module where the rule has power (D1) and weak where it does not (D3/D4). Reporting a verdict without operating characteristics leaves the reader unable to distinguish the two, which is why the standard makes them mandatory. The information criterion outperforms the adopted rule on both axes — a finding about instrument choice within the standard, not against it. The criterion scores one-step accuracy and does not encode the decision-relevant requirement that a module beat persistence at the multi-year horizon, which the rule does. Minimum accompanying evidence: the rule’s power under in-class processes the study’s own models could generate, and its specificity under the null, with block-bootstrap intervals.

**Keywords:** model selection; out-of-sample forecasting; retention rule; reporting standard; operating characteristics; identifiability; conditional hindcast; stock assessment; groundwater; jackknife; climatological-flux map

---

## 1. Introduction

Elaborating a process-based model is easy to justify in principle and hard to evaluate in practice. Extra state variables, residual autocorrelation, delayed information, and environmental covariates each encode a mechanism believed to operate, and each adds parameters estimated from the same short record. Whether the elaboration improves out-of-sample prediction is a separate question from whether the mechanism is real, and it is answerable only against a benchmark and a decision rule fixed in advance. The forecasting literature has made that benchmark discipline explicit: across the M4 competition’s 100,000 series, sophisticated methods did not uniformly beat simple statistical baselines (Makridakis et al., 2020).

Comparison against a naive baseline is established practice. Hindcast cross-validation scores predictions using the MASE of Hyndman and Koehler (2006). Kell et al. (2016) applied hindcasting to stock-assessment prediction skill. Carvalho et al. (2021) list prediction skill among four acceptance criteria. Kell et al. (2021) argue that residual and retrospective diagnostics alone cannot validate where prediction skill can. Two features leave the present question open. Scaled-error diagnostics are usually computed on the same index the model was fitted to, rather than on the estimated state the advice concerns. And they are usually applied to certify a single accepted model rather than to adjudicate a graded sequence of elaborations.

This article addresses the gap with three components. The original pre-registered rule had no tie band; the unified rule adds a 5% band to the groundwater application (Section 4). Verdicts are unchanged under both versions. The algorithm box states the unified rule.

**Retention rule** (Section 2) — a decision procedure over a forward-ordered ladder (a scored ladder, not a strict nesting for M2 and M4). A module is retained only if it lowers the primary error relative to the naive benchmark and to the declared next-simpler comparator, by more than a 5% tie band, at both horizons. It is given as an algorithm with inputs, gates, and outputs. Three objects, two domains, one rule, an empty retained set throughout. Applied to the second, unpooled specification, the same rule returns the same non-retention outcome.

**Information-set audit** (Section 3) — tabulates, for each quantity, whether it is dated at or before the origin (available) or after it (supplied). The difference between an operational forecast and a conditional hindcast is then a matter of record, not inference. The supplied future catch — an advantage no operational forecast has — does not change the outcome, which turns the conditional-hindcast caveat from a limitation into evidence.

**Operating-characteristic study** (Section 6) — applies the rule to synthetic data from known processes, measuring how often it retains a module that is genuinely present and how often it does not. The design, including the thresholds that separate an adequate from an inadequate instrument (power ≥ 80%, specificity ≥ 90%), was registered before any synthetic series was generated. Sections 4 and 5 apply the rule to the three scored objects, and Section 7 compares the two domains. Section 9 states what the standard extracts from the pair, and what it does not license. Section 8 registers the standard’s next applications prospectively.

The contribution is not the finding that persistence is hard to beat — the companion papers report that. It is a minimum reporting standard for non-retention claims: a retention rule stated as an algorithm, an information-set audit, and mandatory operating characteristics. The same rule, with those characteristics measured, produces the same verdict in two unrelated physical systems by two different routes, and the conditions under which a verdict is informative are stated. The rule is the worked example; the standard is the deliverable.

The standard in one page: three obligations, portable and domain-free. (1) A retention rule stated as an explicit algorithm before scoring. (2) An information-set audit separating quantities available at the forecast origin from quantities supplied after it. (3) A mandatory operating-characteristic study under known ground truth. The demonstration — one rule on three scored objects in two domains, an empty retained set reached by two different routes — shows the standard working. It is not the standard. The simulation measures the operating characteristics of this particular rule, not of the standard in general.

---

## 2. The retention rule

### 2.1 Ladder and three objects

The rule operates on a **ladder**: a forward-ordered set of models of increasing complexity, plus a naive baseline. It is a scored ladder, not a strict nesting for M2 and M4. Order is declared before scoring and is not revised in light of scores. Each module has a **declared comparator**, the next-simpler member. The first structural module has none; retention then turns on the baseline alone. The ladder is a rooted tree, not a chain: the comparator is the next-simpler member on the module’s own branch, and M1b is a branch (an alternative production function) rather than a rung.

Five structural modules plus two naive baselines make seven models in total for the cod objects. Edwards has five structural modules plus an oracle diagnostic declared unable to retain, plus two baselines — eight total — with the five-rung structural ladder unchanged. A scored five-module ladder runs against two naive baselines.

**Model inventory.** Only ladder rungs are eligible for retention. Auxiliary modules and declared diagnostics are scored and reported, never retained.

| Object | Rungs (declared comparator) | Auxiliary modules | Declared diagnostics | Naive baselines |
|---|---|---|---|---|
| COD Spec A/B | M1 (none), M1b (M1), M2 (M1), M3 (M2), M4 (M3) | capelin-index module (scored against its own origin-matched persistence) | — (M2–M4 already receive future catch; conditional hindcasts) | naive_persist, naive_train_mean |
| EDWARDS | M1 (none), M2 (M1), M2m (M1), M3 (M2), M4 (M3) | climate rung: M2_Rprecip, M2_Rar, M2_Renso, M2_combo (comparator M2m, declined — a protocol exception noted in the pre-registration) | M2_oracle (realised fluxes, declared unable to retain) | naive_persist, naive_mean |

**Table 1.** Three objects — two domains, no pooling. The safe set and LRP define the reference frame for the secondary Brier threshold score; primary RMSE never uses them (Brier is secondary). Scale for reading the RMSEs: SD(target)/SD(Δtarget) are 356.5/89.5 kt (Spec A), 423.2/89.6 kt (Spec B), and 14.70/12.34 ft (Edwards).

| Object | Series | Years | n h=1 / h=5 | LRP / threshold | Catch / forcing |
|---|---|---|---|---|---|
| COD Spec A | NCAM M-shift SSB (DFO 2016 Table A2) | 1983–2015 | 25/21 | 884.6 kt | regime 240/120/5 kt three-level step, the pre-registered primary catch treatment (annual landings 172–269 kt reported as the second treatment) — C̄ training-mean catch plugged 5.00 kt coarse / 3.19 kt annual, C_t prescribed regime for M2 |
| COD Spec B | xteNCAM (Regular et al. 2025) | 1954–2024 | 59/55 structural, 63/59 naive | 276 kt | Regular et al. 2025 Table 1 landings |
| EDWARDS | J-17 annual-mean head | 1934–2023 | 75/71 | Brier threshold = 660 ft (in force after 2007) | recharge, pumpage |

No row from one object enters any fit, score, or verdict of another. Nothing is pooled with the Edwards J-17 object.

**Cod ladder.** M1 is autonomous Schaefer, S_{t+1} = S_t + r S_t(1 − S_t/K) − C̄, with r and K free and C equal to training-mean catch, plugged not estimated. M1b is autonomous Allee, S_{t+1} = S_t + r S_t(1 − S_t/K) a(S_t) − C̄, with a(S) = (S − s)/(K − s), s ∈ [0, max_train S], r at bound 2.0. As s → 0, a(S) = S/K, the zero-threshold cubic branch. M2 is stock-flow with prescribed C_t. M3 is an AR residual, φ ∈ [−0.95, 0.95], e_u = ΔS_u − [g(S_u) − C_u] pre-clipping; no-intercept lag-one φ̂ = Σ e_u e_{u−1} / Σ e²_{u−1}, zeroed if the denominator is ≤ 0 or there are fewer than 4 residuals, clipped to [−0.95, 0.95]; the projected residual φ̂^k · e_last is added inside the update before clipping to [1e−3, 1e6] kt. M4 is a delayed-information stale-start experiment (M3 parameters, one-year-old state), kept in the ladder for symmetry, not retained. Baselines: naive_persist, naive_train_mean. K is optimised on [max_train S + 10, 5000] kt with a 500 kt multi-start initialiser. k_param denotes parameter count in the IC, k_decay drainage decay, ladder length k = 5. The per-origin lower bound is max_train S + 10 kt, the maximum taken over predictor states of the training transitions excluding the terminal state: ≈ 950.8 kt at the earliest origins (training maximum 940.8 kt, 1987) and 50.8 kt on the recovery-window training set (predictor-state maximum 40.8 kt, 2006). Reported fits attain the upper endpoint K = 5000 kt where the data prefer unbounded carrying capacity. M1 coarse C = 5.00 kt, r = 0.458, K = 500.0 kt, resting at the multi-start initialiser 500.0 kt (lower bound 50.8 kt), not pinned at the bound; annual C = 3.19 kt, r = 0.370, K = 5000.0 kt. M1b coarse K = 105.8 kt and annual K = 129.8 kt are interior valid fits, not bound violations. The objective is flat: MSE 127.4 → 149.9 over K ∈ [60, 5000]. M1/M1b catch-treatment values differ by ≤ 0.04 kt between treatments after displayed rounding (archived values differ: M1 h=1 120.5095 versus 120.5406, 0.0311 kt; M1b h=1 114.8024 versus 114.7665, 0.0359 kt). M1 and M2 coincide under the coarse regime because C_t ≡ 5 kt on both train and test of the recovery window makes the two prescriptions identical; under annual landings they differ (264 versus 303 kt at the recovery window). M1b s → 0 numerical 2.1 × 10⁻²³ coarse, 9.4 × 10⁻⁶ annual, with r pinned at 2.0, corresponds to the zero-threshold cubic branch a(S) = S/K, not Schaefer and not positive-threshold Allee. A minimum of six one-step transitions is the absolute minimum after dropping years with no carried index value for capelin modules (origin 1991 Spec A, 1988 Spec B), matching the estimator’s < 6 refusal guard. The main ladder on Spec B uses a 12-year minimum for structural models (n = 59/55) versus an 8-year minimum for naive models (n = 63/59).

**Edwards ladder.** M1 is one-pool affine, H_{t+1} = a H_t + b (autoregression φ̂ = 0.66, Pearson corr(H_t, H_{t−1}) = 0.64, consistent with discrete drainage-decay 1 − φ ≈ 0.34 yr⁻¹; continuous k = −ln 0.66 ≈ 0.42 yr⁻¹, e-folding 2.4 yr). M2 is two-parameter. M2m is training-mean balance, the climatological-flux map (best one-step 12.283 ft, the only margin separated from noise). M3 and M4 are extensions. M2_oracle is the oracle with realised future recharge and pumpage (declared unable to retain; diagnostic upper bound −42.96% at h=1, −48.52% at h=5 under the fitted map). Baselines: naive_persist, naive_mean (training mean 16.8048 ft versus persistence 21.1056 ft at h=5, interval excluding zero). The declined M2m still serves as the declared nested comparator for the climate rung, as fixed in the pre-registration. No year falls below the 240 daily-observation floor for the annual mean (minimum n = 242 daily observations in 1939). The 15-year rolling floor rule is vacuous on this 90-year panel. The complete estimation panel ends in 2023, whose provisional status is flagged. Q = −2876 + 4.77H (Q total spring discharge in cfs, H J-17 head in ft) implies Q = 0 near 603 ft, below the ≈ 618 ft reference, predicting the 1956 cessation of flow (tail failure) when head fell below the discharge threshold.

Estimation is one-step least squares on the training window. The h=5 score is endpoint RMSE (not a trajectory average) and compares the no-change forecast with iterated trajectories. The iterated affine analogue M2m is 17.44 ft (rolling h=5) and 17.64 ft (fixed-window h=5, n=12), each near the corresponding training mean. Log-RMSE uses the natural log with a 1e−3 floor (ordering unchanged with floors 1e−6 and 1e−9). Sign-hit rate uses adjacent-year n−1 comparisons. The Brier threshold is a misclassification rate (for a deterministic binary forecast, equivalent to the Brier score). The bare fact that targets fall below the LRP would not by itself make the persistence indicator correct; origin states being below does. Origins and targets must both be below. The same five-rung ladder and the same estimation functions are used across both domains and in the simulation (Section 6.2).

### 2.2 Algorithm

**Definition 2.1 (Retention rule, portable).** Module M is retained only if all of the following hold on rolling-origin primary RMSE (origin-matched, per Künsch 1989):

- **H1** — M reduces RMSE versus the declared comparator — the next-simpler rung for nested steps (M1b versus M1, M3 versus M2 on cod; M2m versus M1, M2 versus M1, M3 versus M2, M4 versus M3 on Edwards) — by strictly more than 5% of the comparator’s score.
- **H2** — M reduces RMSE versus last-value persistence by strictly more than 5%.
- **H3** — Each reduction holds at both horizons h=1 and h=5.

Fail any, and the module is not retained. Retention is decided per specification. Tie band b = 0.05: improvements of 5% or less are ties and are not retained; exactly 5% fails (strictly more than 5% is required). The deciding score is the pre-registered specification’s rolling-origin RMSE pair at h=1 and h=5 (H3).

Comparator: on cod, M2’s comparator is M1 and M4’s comparator is M3. An alternative comparator, M2 versus M1b, is reported as a sensitivity row on the primary passes: A h=1 +29.3 kt, z = 0.91 [−67.6, +82.8]; A h=5 +109.7, z = 0.98 [−77.1, +232.8]; B h=1 +14.4, z = 0.51 [−67.5, +89.1]; B h=5 +613.4, z = 1.93 [+170.9, +945.1].

```
Retention rule — Algorithm Box
 inputs ladder M_1..M_k ordered by declared complexity
 baseline B (last-value persistence)
 comparator map comp(): M_i -> M_j or none
 horizons H={1,5}
 tie band b=0.05
 score S(model,horizon) out-of-sample origin-matched
 output retained | not retained | declined on class grounds

 for each M:
  if M reduces to simpler member under conditions of application:
   output declined on class grounds # pre-gate, evaluated before scoring
  retained <- TRUE
  for h in H:
   if S(M,h) >= (1-b)*S(B,h): retained <- FALSE # H2, strictly >5% required
   if comp(M) exists and S(M,h) >= (1-b)*S(comp(M),h): retained <- FALSE # H1
  if retained: output retained
  else: output not retained
```

The class-grounds check is a substantive pre-gate, evaluated before scoring: whether a module collapses to a simpler member under the conditions of application is knowable independent of the data. The algorithm box shows the class-grounds check first, matching the operational order. The class judgement is declared in the same specification as the ladder, fixed before any score is computed, so the decline of the only persistence-beating module is not an after-the-fact judgement. The retained set is empty under the rule alone (M2m fails H1 at h=1 under the unified rule), so the empty set holds either way. Without the band, M2m would pass H1 but still be declined on class grounds.

Scores are **origin-matched**: every comparison uses the module’s own origin set, and the baseline is recomputed on that set. On Spec B’s main ladder, a 12-year minimum for structural models versus an 8-year minimum for naive models gives origin-matched persistence of 84.43 kt versus mixed-origin 87.65 kt at h=1 (difference 3.22 kt) and 299.98 kt versus 317.71 kt at h=5 (difference 17.73 kt). On the index modules’ origin sets (capelin-informed productivity, Table 8 of the companion), persistence reads 97 kt (n=24, h=1) and 193 kt (n=20, h=5) on Spec A and 79 kt (n=36) and 288 kt (n=32) on Spec B. The index module loses to the origin-matched baseline in every cell. The five-year near-tie on Spec A is resolved by origin matching — the baseline on the module’s own origins reads 193 kt against the module’s 262 kt — and the one-year RMSE is worse under both readings (150 versus 98 kt on SSB origins and 97 kt on the module’s). The **tie band** suppresses retention inside sampling noise. The **comparator gate** prevents retention merely because a module beats the baseline when a simpler one does too.

**Definition 2.2 (Negative certificate).** A machine-verified finding of non-retention under a stated rule, scoped to estimator, ladder, and series. Weaker than a statistical null. Distinct from the Brier secondary diagnostic. The 1992–1993 fishing moratorium is deliberately not evaluated.

### 2.3 The third output — declined on class grounds

A module can improve a score without adding structure. That is the principle of structural redundancy: a module that reduces to a simpler member under the conditions of application adds no information, regardless of its score. Groundwater M2m, the training-mean balance (climatological-flux map), beats persistence at both horizons yet collapses to AR(1) when fluxes are held constant: it wins on score while adding nothing beyond the simpler member. Recording it as *declined on class grounds* rather than retained keeps the output faithful. The judgement is substantive, declared with reasons, not a threshold. For cod, M1b with s → 0 makes it the zero-threshold cubic branch a(S) = S/K, so the lower error on the post-collapse recovery sub-window (train 1995–2007, test 2008–2015, 90 kt versus 104 kt) is not evidence for depensation. On full rolling-origin scoring it never beats persistence at either horizon on either specification. M1b is an alternative production-function branch whose declared Allee parameter approached zero, not evidence for a depensation threshold.

---

## 3. The information-set audit — reporting template

An evaluation is interpretable only if the reader knows what each forecast was allowed to see. The audit table has one row per quantity, classifying it as **available** — dated at or before the origin — **supplied** — dated after the origin and provided regardless — or **revised** — dated before the origin but existing only in a vintage published after it (the cod spawning-stock biomass predictand is an assessment output conditioned on the full series).

| Quantity | Status at origin *t* | Typical use |
|---|---|---|
| Target series, u ≤ t | available | all modules and baselines |
| Origin state | available | all except lagged-initialisation |
| Lagged state | available | lagged-initialisation modules |
| Training transitions, u ≤ t | available; window may expand | parameter estimation |
| Fitted residual | available | residual modules |
| Driver series, u ≤ t | available | modules using training means |
| **Driver series, u > t** | **supplied** | modules given realised path (catch, recharge, pumpage) |
| Covariate, u ≤ t | available; last observation carried forward | covariate modules |
| Predictand dated before origin, published only in a later vintage | **revised** | assessment outputs (cod SSB) |
| Reference threshold | fixed by spec | secondary scores only |

The single row that determines whether the test is an operational forecast or a conditional hindcast is the supplied driver path. Where modules receive the realised driver over the horizon, the exercise cannot support a claim about operational skill — but the asymmetry strengthens the negative result: modules given information no operational forecast could possess still fail to beat a rule that uses only the current state. Even with future catch supplied — an advantage no operational forecast has — the structural modules still lose to persistence.

The **oracle module** makes the bound explicit. Fitted with realised drivers throughout and declared unable to be retained, it measures what perfect driver information buys. The groundwater oracle is 7.547 ft versus persistence 13.230 ft (−42.96% at h=1, −48.52% at h=5) under the fitted map, so perfect flux knowledge is worth about 43% of baseline error at one year — an upper bound no causal module approached. The cod ingredients exist (M2–M4 already receive future catch) but were never framed as a bound. Both exercises are conditional hindcasts; the oracle device makes the bound explicit on Edwards.

The audit table (Table 2b) is proposed as a reporting template. An evaluation that does not state which inputs were unavailable in real time cannot be read as evidence about operational skill. Uncertainty is reported via Diebold–Mariano HAC and moving-block bootstrap per Künsch (1989). Bootstrap intervals are conditional on the archived forecast paths.

---

## 4. Worked example — Edwards Aquifer index well J-17

Full detail is in the companions. Reported here: scored verdicts, margins, and the route by which they were reached. Every number has been verified against source CSVs. No pooling, no verdict transfer.

Predictand: J-17 annual-mean head, San Antonio Pool, 1934–2023. Ladder: autoregression M1, affine H_{t+1} = a H_t + b (φ̂ = 0.66, Pearson corr(H_t, H_{t−1}) = 0.64 — a different quantity — consistent with discrete drainage-decay 1 − φ ≈ 0.34 yr⁻¹; continuous k = −ln 0.66 ≈ 0.42 yr⁻¹, e-folding 2.4 yr); one-pool stock-flow water balance with persisted fluxes M2 (14.6978 versus 13.2301 ft, loses because recharge is near-white, corr(R_t, R_{t−1}) = 0.17 versus corr(ΔH_t, R_t) = 0.74); the same balance with training-mean fluxes, M2m, the climatological-flux map (best one-step 12.2832 ft, the only margin separated from noise); residual and delay variants M3/M4 kept in the ladder for symmetry; against persistence and the climatological mean (training mean 16.8048 ft beats persistence 21.1056 ft at h=5, interval excluding zero); plus the declared oracle M2_oracle 7.5467 ft (−42.96% at h=1, −48.52% at h=5), a nowcast not a forecast under the fitted map.

Climate modules (Table 5b; companion Table 7): three of four lie within 0.13 ft of M1 at h=1 — M2_Rprecip 12.80 (−0.04), M2_Renso 12.82 (−0.02), M2_combo 12.71 (−0.13) — and the recharge-autoregression variant M2_Rar is 0.41 ft worse (13.25). None are retained; all lose to climatological fluxes. On the 2015–23 critical-period window, M2_Rprecip and M2_Rar edge past M1 (14.52 and 14.67 versus 15.62 ft) — a window-specific result, not a recharge forecast. Under an M1 comparator the verdict is unchanged: the modules that edge past M1 on that window still fail the persistence gate at h=5, where all four climate modules score 3–6 ft worse than persistence.

**Table 5b.** Climate-informed recharge modules on J-17, rolling origins (Table 7 of the Edwards companion). H is annual-mean head RMSE in feet; margins versus M1 at h=1.

| Module | H, h=1 (ft) | margin vs M1 | H, h=5 (ft) |
|---|---:|---:|---:|
| Persistence | 13.23 | +0.39 | 21.11 |
| M1 autoregression | 12.84 | — | 21.25 |
| M2_Rar (recharge autoregression) | 13.25 | +0.41 | 25.38 |
| M2_Renso (lagged Niño 3.4) | 12.82 | −0.02 | 24.42 |
| M2_Rprecip (lagged precipitation) | 12.80 | −0.04 | 25.38 |
| M2_combo | 12.71 | −0.13 | 26.88 |
| M2m climatological-flux map (declined on class grounds) | 12.28 | −0.56 | 17.44 |

San Antonio and Uvalde pools lumped — a declared approximation defect. J-27 Uvalde index, gravimetric storage, or total spring discharge are different objects, outside the scope of this specification. Precipitation enters only through a correlation check with recharge. P̄ denotes pumpage (notation table).

**Table 4.** Edwards closest approach — terminology bridge: M2m = training-mean balance = climatological-flux map.

| h | Model | RMSE | Persist | Deficit | Uncertainty |
|---|---|---|---|---|---|
| 5 | M2m | 17.4449 | 21.1056 | −17.34% | margin −3.66 ft, CI [−5.76, −2.19] excludes zero |
| 1 | M2m | 12.2832 | 13.2301 | −7.16% | only margin separated from noise (CI [−1.445, −0.676]) |
| 1 | M1 | 12.8391 | 13.2301 | −2.96% | 0.39 ft margin, interval covers zero, MAE tie (10.72 versus 10.73 ft), 5-year loss — indistinguishable from a tie |
| 1 | oracle | 7.5467 | 13.2301 | −42.96% | upper bound, nowcast under fitted map |

**Three margins beat persistence by point RMSE, and nothing is retained.**

**Table 5.** Edwards gate decomposition.

| Module | h | RMSE | Persist | Band (0.95 × persist) | H2 | Comparator | Comp RMSE | H1 |
|---|---|---|---|---|---|---|---|---|
| M2m | 1 | 12.2832 | 13.2301 | 12.5686 | pass | M1 | 12.8391 | FAIL (4.33%; comparator band 12.1971) |
| M2m | 5 | 17.4449 | 21.1056 | 20.0503 | pass | M1 | 21.2514 | pass |
| M1 | 1 | 12.8391 | 13.2301 | 12.5686 | FAIL | — | — | — |
| M1 | 5 | 21.2514 | 21.1056 | 20.0503 | FAIL | — | — | — |

M1 fails H2 at both horizons. M2m passes H2 at both horizons but fails H1 at h=1. The companion declines M2m on class grounds, since it collapses to AR(1) under constant fluxes. Six margins sit inside the 5% band: M1 h=1 2.96%, M2m h=1 versus M1 4.33%, M3 h=1 1.63%, M4 h=1 1.13%, M3 h=5 0.08%, M4 h=5 0.21%. The 5% band and the both-horizon requirement are applied to the groundwater analysis even though the original pre-registered rule scored retention on h=1 alone and without a band. Within the unified rule the band changes no outcome. Under the unified rule with the band, M2m fails H1 at h=1 (4.33% < 5%) and is additionally declined on class grounds. Without the band it would pass H1 but still be declined on class grounds, so the empty set holds either way. The companion’s pre-registered h=1 point rule retains M1 provisionally — a 0.39 ft margin within noise, MAE tied at 10.72 versus 10.73 ft, a five-year loss — while the unified rule withholds it: the 2.96% h=1 margin lies inside the band and M1 loses at h=5 (21.25 versus 21.11 ft). The empty retained set is a property of the unified rule. The M1 difference between the two readings is a recorded rule-version difference, not a data difference. The gate demonstration uses the unified rule. The declined M2m still serves as the declared nested comparator for the climate rung, as fixed in the pre-registration. A post-2007 h=5 reversal, M1 17.16 versus persist 25.10, is reported without changing the one-year retention statement. The h=5 score compares the no-change forecast with iterated trajectories. Scores at h > 1 for climate modules reuse the one-step forecast held constant — no h-year-ahead recharge or pumpage forecast is available at the origin, and the one-step forecast is the only origin-available flux estimate.

**Uncertainty layer.** The AR(1) 0.39 ft margin has an interval covering zero; MAE is tied (10.72 versus 10.73 ft); the 5-year loss is a tie to within rounding. Retention by the point-RMSE rule records this, not a skill claim. The training mean, 16.8048 versus 21.1056 ft, has an interval excluding zero at h=5. The load-bearing gate decision (M2m versus M1, 4.33% against the 5% band) sits within numerical tolerance of the environment sensitivity measured on cod (±17 kt on 445.5 kt, 3.8%). An Edwards cross-environment reproduction is reported in Data availability. Persistence remains the decision baseline because it is the pre-registered H2/H3 anchor. The training mean’s superiority at h=5 is reported as evidence about the baseline choice, not as a re-baselining. Fixed-window M2 RMSEs are 18.11 and 55.32 ft. The fixed-window pre-permit pass uses its declared train 1980–1990 (11 yr). The 15-year floor applies to rolling origins only; fixed windows use their declared training sets.

---

## 5. Worked example — Northern cod, NAFO 2J3KL

Predictand: NCAM M-shift SSB (DFO 2016 Table A2, 1983–2015, LRP 884.6 kt) and extended xteNCAM (Regular et al. 2025, 1954–2024, LRP 276 kt), scored as separate unpooled objects. Ladder: autonomous, depensation, stock-flow with prescribed catch, AR residual, lagged initialisation, against last-value persistence and the training mean. Detail in Abaee (2026b). The scored ladder is a forward-ordered set of seven models — persistence, mean, M1, M1b, M2, M3, M4 — evaluated by the fixed retention rule. It is not a strict nesting for M2 and M4.

**Table 2.** Cod closest structural approach to persistence (deficit %, negative = beats). Source: wave_e_cod/results/rolling_summary.csv (regime+na filtered Spec A, coarse-regime) and xte_rolling_summary.csv (Spec B). Coarse-regime values are reported for M4 Spec A (195.6 versus 206.3 under annual landings).

| Object | Rank | h | Model | RMSE | Persist | Deficit |
|---|---|---|---|---|---|---|
| COD Spec A coarse-regime | 1 | 5 | M1b | 288.58 | 264.72 | +9.01% |
| | 2 | 5 | M1 | 288.72 | 264.72 | +9.07% |
| | 3 | 1 | M1b | 114.80 | 98.05 | +17.09% |
| COD Spec B mixed-origin | 1 | 5 | M1 | 431.90 | 317.71 | +35.94% |
| | 2 | 1 | M1 | 119.47 | 87.65 | +36.30% |
| | 3 | 5 | M1b | 445.48 | 317.71 | +40.22% |
| COD Spec B origin-matched | 1 | 1 | M1 | 119.47 | 84.43 | +41.50% |
| | 2 | 5 | M1 | 431.90 | 299.98 | +43.98% |

Spec B mixed-origin uses naive n = 63/59; origin-matched uses n = 59/55, identical to structural. The difference is 3.22 kt at h=1 (3.8% of the origin-matched baseline) and 17.73 kt at h=5 (5.9%). The verdict is unchanged. The 5% band applies to retention margins versus persistence or comparator, not to baseline shifts. The capelin index module (Table 8 of the companion) loses to its origin-matched baseline in every cell — 150.02/262.34 kt against 97/193 kt on Spec A and 132.02/491.74 kt against 79/288 kt on Spec B (Section 7). The large h=5 baseline shift between the main-ladder and module origins (264.72 to 193 kt) is checked on both origin sets, so the verdict is not an origin-set artefact. Stall reconstructions and the ladder share a constant-productivity failure mode, scored on different objects.

**Table 3.** Cod primary scores, rounded; origin-matched for Spec A coarse-regime, both readings for Spec B.

| Object | h | persistence mixed / origin-matched | closest structural | deficit mixed / origin-matched | interval excluding zero? |
|---|---|---|---|---|---|
| Spec A coarse-regime | 1 | 98.05 | M1b 114.80 | +17.09% | No — no Spec A margin against persistence has an interval excluding zero |
| Spec A coarse-regime | 5 | 264.72 | M1b 288.58 | +9.01% | No |
| Spec B | 1 | 87.65 / 84.43 | M1 119.47 | +36.30% / +41.50% | Yes — several Spec B margins do |
| Spec B | 5 | 317.71 / 299.98 | M1 431.90 | +35.94% / +43.98% | Yes |

No structural module approaches the tie band on either specification at either horizon. The verdict is decided by ranking alone; the gates never engage on cod. Collapse window (train 1983–1990, test 1991–1995): persistence 670 kt versus M1 694 kt, M1b 694 kt, M2 819 kt (M1/M1b both treatments 694 kt; M2/M3/M4 819 kt coarse, 821 kt annual). Every model misses the collapse. Constant productivity with the 1992 catch drop cannot produce the observed crash. Neither the AR residual nor a one-year information delay reduces the error; delay raises it. M4 has the worst raw RMSE on the collapse window (train 1983–1990, test 1991–1995). It is kept in the ladder for symmetry. Decomposition versus a stale-start persistence control uses archived per-origin files, not Tables 2–3: delay dominates at h=1, model cost dominates at h=5. At h=1, information delay accounts for 86 of 98 kt of the one-year gap and model structure for the remaining 12 kt, and 65 versus 158 kt of the five-year gap. The Spec B control reads 158 kt and 337 kt against M4’s 206 kt and 1031 kt, where delay’s own contribution is modest at h=1 (48 of 118 kt) and dominant at h=5 (694 of 713 kt).

Recovery window (train 1995–2007, test 2008–2015): persistence 104 kt versus M1 = M2 120 kt (coarse; annual 264 versus 303 kt — coincidence only under the coarse regime, because C_t ≡ 5 kt on both train and test makes the two prescriptions identical), M1b 90 kt with unidentified s → 0 and K = 105.8 kt just above the training predictor range, M3 220 kt, M4 214 kt. Profile likelihood for s is flat: objective n log{SSE(s)/SSE(ŝ)} max 0.78 coarse, 0.35 annual, r at bound 2.0 throughout, no error model, 12 transitions — descriptive curvature, not a calibrated likelihood-ratio test. Apparent net production S_{t+1} − S_t + C_t is strongly negative in 1991–93 even after adding back reported removals (the formula S_{t+1} − S_t + C_t adds C_t). This is a diagnostic construct, not an exact stock balance: S is SSB while C is total landings; changes reflect maturation, weight-at-age, and age composition. Because C_t is total landings while S_t is SSB, the removal term is not SSB-equivalent. Failing to reproduce the collapse with the supplied catch path does not test whether fishing caused the collapse. Within surplus-production accounting, matching observed ΔS with no production would require removals of order −ΔS. The observed decline is far larger than C_t; the unexplained term dwarfs the catch-treatment difference. The Rose stall overlaps the 2016–2024 portion of the 2013–2024 test window, not the whole period.

**Uncertainty layer.** Diebold–Mariano descriptive loss-differential diagnostics and moving-block-bootstrap intervals attach to the margins. DM z tests the mean squared-loss differential. CI and p come from a separate moving-block bootstrap of the RMSE gap, because the square root compresses the heavy collapse-window tail; the two can disagree, and the bootstrap is tighter on this data. p is the bootstrap percentile-tail fraction p_perc = 2 · min{#(Δ* ≤ 0), #(Δ* ≥ 0)} / B. The CI excludes zero iff p < 0.05, verified with 15 CIs that exclude zero (1 Spec A + 6 Spec B h=1 + 8 Spec B h=5) and 17 that include (7 + 8 Spec A + 2 Spec B h=1). There are zero exceptions where the bootstrap CI and bootstrap p disagree. DM z on the squared-loss difference d_i = L_{A,i} − L_{B,i}, HAC-scaled, can disagree when variance is inflated by catastrophic origins. This occurs in 5 of 32 rows in the full 32-row universe — including the four alternative-comparator M2-versus-M1b rows, which the companion’s 28-row subset excludes (e.g., Spec A M4 versus M3 h=1 [+4.7, +144.7], z = 0.99, p < 0.001 (bootstrap percentile-tail); Spec B M3 versus persist h=1 [+1.0, +92.5], z = 1.85, p = 0.042; Spec B M4 versus M3 h=5 [+20.2, +177.4], z = 1.88, p = 0.007). DM statistics are not calibrated for this design — expanding-window recursive estimation, overlapping training samples, near-nested models, a smoothed target, and multiple comparisons all bear on calibration. The verdicts do not rest on DM statistics, which are reported as descriptive loss-differential diagnostics. Bootstrap intervals are conditional on archived forecast paths and propagate no parameter, revision, catch, or covariate uncertainty.

**Conditional hindcast disclosure.** The predictand is retrospectively reconstructed rather than taken from vintages at each origin, and catch is supplied along the horizon. This is a conditional hindcast, not an operational forecast, and must not be reported as skill.

---

## 6. Operating characteristics

### 6.1 Why, and the pre-registration

A negative result is only as informative as the instrument that produced it. Whether the rule could have detected added structure had it been present cannot be answered from the application. It is addressed by simulation, with the data-generating processes, replicate counts, and interpretation thresholds fixed before any simulation was run.

Simulation scores synthetic series only. No empirical verdict changes.

**Claim under test H_sim.** On synthetic series generated from a known member of the ladder’s own model class, with sample sizes and noise matched to Spec A (T = 33), the retention rule retains the true generating module at a rate materially above the false-retention rate.

### 6.2 Data-generating processes — fixed before scoring

All in-class DGPs are members of the ladder’s own class. Series are generated with the same state-update and surplus functions used for estimation.

| DGP | Truth | Parameters anchored to archived fits | Why in/out of class |
|---|---|---|---|
| **D1** | M1 autonomous Schaefer | r = 1.935, K = 1032.7, constant C = 240 (collapse-window fit) | in-class |
| **D2** | M1 low-productivity | r = 0.458, K = 500.0, constant C = 5 (recovery-window) | in-class |
| **D3** | M2 stock-flow | r = 1.935, K = 1032.7, prescribed C_t = coarse regime 240/120/5 | in-class |
| **D4** | M1b genuine depensation | r = 0.458, K = 500.0, s = 15 kt, a positive identifiable threshold unlike the real fits s → 0 | in-class |
| **D5** | Persistence-true null | S_{t+1} = S_t + η_t, no surplus, C ≡ 0 | null |
| **D6** | Time-varying productivity (Amendment 1) | r_t = 1.935 · exp(−0.05t) + 0.35, K = 1032.7, catch 55% of instantaneous rK/4 | out-of-class: no ladder member has time-varying r |
| **D7** | Observation error only (Amendment 1) | state evolves noise-free, r = 0.9, K = 1032.7, C = 180; scored series = state + Gaussian noise | out-of-class: the ladder treats deviation as process noise; here the state is deterministic and the noise is in measurement |

Process noise σ ∈ {11.8, 33.8} kt are the archived recovery- and collapse-window residual SDs. Innovations are Gaussian and enter the state update exactly as in the pre-registered map. Series length is T = 33 (Spec A); the T = 71 extension uses the same design. Replicates per cell: 200 (D1, D5), 100 (D2–D4), 30 (D6, D7), 10 (T = 71). Replicates are seeded by a hash-based map of (DGP, σ, replicate) under a pinned hash seed. The seed maps and every result file are archived.

A design-time calibration check for D6/D7 confirmed usable replicates at σ = 33.8 with biomass inside the observed range (a naive regime-switch candidate degraded 900 → 888 → … → 305 → 77 → 0 in four steps and was rejected at design time). The check is a calibration exercise, distinct from the results below.

M3 and M4 were never simulated as generating truth — a stated limitation of the operating-characteristic study.

### 6.3 Results (core + Amendment 1)

| Process | Truth | σ low 11.8 | σ high 33.8 | Row measures | Note |
|---|---|---|---|---|---|
| D1 autonomous collapse | M1 | 0.955 | 0.960 | decision reliability | power high, exceeds 80% adequacy bar |
| D2 autonomous recovery | M1 | 0.780 | 0.060 | decision reliability | power falls with noise; low σ near the bar, high σ below |
| D3 stock-flow | M2 | 0.110 | 0.100 | decision reliability | 18–20× the null false-retention rate (0.0055 per module-replicate), below the bar |
| D4 depensation identifiable | M1b | 0.010 | 0.010 | decision reliability | below the bar |
| D5 persistence-true (specificity) | none | 0.995 | 0.950 | decision reliability (specificity) | 1 − any retained |
| **D6 time-varying productivity** | out-of-class | **0.633** | **0.733** | mechanism attribution | false retention; retained modules beat persistence in all retention replicates (mean gain +3.1/+9.2 kt at h=1) |
| **D7 obs error only** | out-of-class | **0.933** | **0.867** | mechanism attribution | false retention; retained modules beat persistence in all retention replicates (mean gain +2.6/+9.4 kt at h=1) |

Rows D1–D4 report the proportion retaining the generating module; D5 the proportion retaining nothing; D6–D7 the proportion retaining any structural module when no ladder member generated the data. Retention licenses a prediction claim, never a mechanism claim. The D6/D7 rows measure mechanism misattribution — retention on a real predictive gain that the module’s mechanism did not cause — and the “Row measures” column separates decision reliability (D1–D5) from mechanism attribution (D6/D7). The realised predictive gain of the retained module in those replicates is reported in the rows above. Replicates per cell: 200 (D1, D5), 100 (D2–D4), 30 (D6, D7), 10 (T = 71); seeds pinned and archived (Section 6.2).

**Evidential weight** (likelihood ratios; null false-retention rate 0.0055 per module-replicate). Retention LR+ = power / 0.0055. Evidence against the module on non-retention = (1 − 0.0055) / (1 − power):

| DGP | LR+ (retention) | LR− (non-retention, evidence against) |
|---|---|---|
| D1 low/high σ | 174 / 175 | 22:1 / 25:1 |
| D2 low/high σ | 142 / 11 | 4.5:1 / 1.05:1 |
| D3 low/high σ | 20 / 18 | 1.12:1 / 1.11:1 |
| D4 low/high σ | 1.8 / 1.8 | 1.01:1 / 1.01:1 |

At D4 the depensation rung is a near-null instrument: P(retain M1b | depensation true) = 0.010 equals P(retain M1b | null) up to sampling error, so retention and non-retention both carry likelihood ratios near 1. False retention across in-class structural processes is 0.034 per module-replicate pair (wrong-module rate on D1–D4; 0.037/0.031 by noise level), 0.005/0.050 per replicate under the D5 persistence-true null, and 0.0055 per module-replicate under the null. At T = 71 (10 replicates per cell): D1 power 0.900/1.000, D5 false retention 0.000/0.000. The 200-replicate T = 71 design remains a registered longer campaign (Section 6.2). The locked length-sensitivity rule (Amendment 1: |Δ| ≤ 0.15) is satisfied — D1 power differs between T = 33 and T = 71 by 0.055 (low σ) and 0.040 (high σ). A power map (power by DGP × σ with the adequacy thresholds marked; archived as a figure) shows D1 high and D3/D4 low.

Mean power is 0.373 — the unweighted mean of the eight D1–D4 cells, including three near-failures — far below the pre-registered 80% adequacy bar (2 of 8 cells clear it, D1 only). Specificity clears 90% in both in-class null cells (D5) and in none of the four misspecified cells (D6/D7). The rule is an inadequate diagnostic for three of four in-class structural classes (low-productivity autonomous D2 at high σ, stock-flow D3, depensation D4).

### 6.4 Reading — identification versus gates

**Specific against in-class alternatives, and powerful where the signal is strong.** Under persistence-true truth it declines to retain in 95–99.5% of replicates. At collapse-window parameters it recovers the true autonomous module in 95.5–96%.

**Power is low for three of four in-class structural processes; the cause is identification, not the gates.** Requiring only that the module beat persistence — ignoring comparator and band — still retains the true module in just 33% of stock-flow and 18% of depensation replicates. With five candidates, chance would place the generating module first 20% of the time. It holds that position in 61% of autonomous cells (both noise levels), 37%/18% of depensation cells, and 1%/11% of stock-flow cells — stock-flow less often than a random draw. Conditional on clearing the baseline bar, the comparator gate is the dominant further filter, removing 72% of H2-passers in stock-flow D3 (31%/83% by noise level) and 93% in depensation D4 (96%/75%).

**Specificity does not survive misspecification.** Against truths the ladder cannot represent, the rule retains structure in 63–93% of replicates, almost always the autonomous map. Compared with 0.5–5.0% false retention under the in-class null, this is the sharpest result: *specificity is a property of the rule applied to in-class data, not a property of the rule.* Specificity of 0.95–0.995 is scoped explicitly to in-class truth and does not transfer to misspecified settings.

### 6.5 Comparison with alternative decision rules

Because the simulation archives every replicate’s scores, alternative rules can be evaluated on the same data without refitting. The rows below apply each alternative to the archived replicate table (10,000 rows), and the independent pinned-seed campaign (Section 6.2) recomputes the pre-registered rule’s row. A simulation-calibrated band targeting power ≥ 0.80 / specificity ≥ 0.90 at the object’s own T and SNR is registered as the prospective replacement for future applications of the standard. It never re-opens the verdicts reported here, which remain decided by the pre-registered 5% band (the calibration procedure is specified in Section 8).

| Decision rule | mean power | specificity | mechanism misattribution, misspecified (D6–D7) |
|---|---|---|---|
| Retention rule as stated (H1+H2+H3+5% band) | 0.376 | 0.978 | 0.835 |
| Without comparator gate | 0.476 | 0.972 | 0.862 |
| Baseline only, one horizon | 0.562 | 0.955 | 0.890 |
| Baseline only, any margin | 0.542 | 0.765 | 0.912 |
| No tie band | 0.436 | 0.772 | 0.884 |
| 10% tie band | 0.337 | 0.998 | 0.725 |
| Scaled error below one (MASE < 1) | 0.651 | 0.675 | 0.945 |
| Information criterion n log MSE + 2k (one-step squared error, parameter penalty) | **0.509** | **0.992** | **0.615** |

Within the rule, the tie band carries most of the weight: removing it costs 0.206 specificity to buy 0.060 power, while the comparator gate costs 0.100 power for 0.006 specificity. Against the external alternatives, scaled error alone buys power by surrendering specificity (retaining structure in a third of persistence-true replicates). The **information criterion penalising free parameters dominates the rule stated here on both axes** (higher power +0.133, higher specificity +0.014, on the archived table). MASE < 1 buys power by surrendering specificity. The information criterion scores one-step squared error with a parameter penalty; it does not encode the decision-relevant requirement that a module beat persistence at the multi-year horizon. A module can win the criterion and still lose to persistence at h=5. Readers selecting an instrument for new work should weigh this. The rule reported here is the pre-registered instrument. Recomputed on the independent pinned-seed campaign (Section 6.2), the rule’s operating characteristics are 0.373 mean power, 0.973 mean specificity, and 0.792 mean misattribution across D6–D7. The archived row (table above) is statistically indistinguishable.

**Uncertainty-robust variants.** Re-scoring the same replicates with an uncertainty gate (each margin’s 95% block-bootstrap interval entirely below zero) strengthens specificity but empties the retained set everywhere. A model confidence set never eliminates persistence in any replicate — persistence lies inside the 90% set in every replicate — so the non-retention verdicts are not artefacts of the fixed band. The reported verdicts are unchanged in direction. Full variant detail is in Supplement S1.

**The information criterion as a co-primary instrument (post-freeze check).** The criterion’s archived row was re-derived as a co-primary check on the pinned-seed archive, with the instrument disclosed in full: IC = n ln(RMSE²) + 2k on one-step error, k the number of fitted scalar parameters (M1 2, M1b 3, M2 2, M3 3, M4 3, persistence 0; data-derived constants excluded), n the origin count (archived: o9_ic_coprimary_20260913.json). In simulation the penalty moves identification toward the simpler model — D1 0.51 → 0.87 and 0.565 → 0.86, D2 0.81 → 0.94 and 0.70 → 0.87 (low/high noise) — and lowers it where the truth itself carries the extra parameter: D4 0.37 → 0.06 and 0.18 → 0.07 (D3 0.01 → 0.01 and 0.11 → 0.19). Under persistence truth the criterion prefers a structural module in 0.5%/3.5% of replicates, against the rule’s 0.5%/5.0% false retention. On the scored objects the check is decisive: on both cod specifications the criterion selects persistence, agreeing with the empty retained set; on Edwards it selects M2m — the climatological-flux map (IC 455.5 versus M1 463.5, persistence 464.9) — the one module whose retention the standard withholds, on the comparator gate (its 4.33% RMSE margin lies inside the 5% band) and on class grounds. The criterion’s dominance therefore does not carry the decision-relevant edge case: applied alone it would retain the module that adds no information beyond the simpler AR(1) member under the conditions of application. With the standard’s checks the verdicts are unchanged, and the divergence is exactly the case in which Section 4 shows the gates to be load-bearing.

A pre-check diagnostic identifying in advance where the rule has power remains open. The examined candidates and the D3 counterexample are documented in Supplement S1.

---

## 7. Two domains, one rule — cross-application comparison

| | Northern cod | Edwards J-17 |
|---|---|---|
| Domain | marine fish stock | confined aquifer, karst, rapidly recharged, institutionally bounded |
| Predictand | assessment-derived biomass (NCAM M-shift, xteNCAM) | measured well head, annual-mean |
| Record length | 33 (Spec A) and 71 (Spec B) years; n = 25/21 and 59/55 structural versus 63/59 naive | 90 years (75/71 origins) |
| Structural modules | 5 (M1, M1b, M2, M3, M4) | 5 (M1, M2, M2m, M3, M4) + oracle |
| Modules beating baseline (points) | none | three module–horizon cells (M1 h=1 −2.96%, M2m h=1 −7.16% only separated, M2m h=5 −17.34%) + oracle −42.96%/−48.52% under fitted map |
| Closest structural margin | +9.01% deficit M1b h=5 Spec A (288.58 versus 264.72), +17.09% h=1 | −17.34% advantage M2m h=5 (17.44 versus 21.11), −7.16% h=1 |
| Decided by | ranking alone (9.01% smallest deficit Spec A M1b h=5, 17.09% h=1; no Spec A interval against persistence excluding zero) | tie band and comparator gate (4.33% H1 margin; AR(1) interval covering zero) |
| Oracle bound | no | yes, 7.547 versus 13.230 (−42.96% h=1, −48.52% h=5) — nowcast bound under fitted map |
| Training mean versus persistence h=5 | — | 16.80 versus 21.11, interval excluding zero |
| Climate modules | capelin-informed productivity not retained (150.02/262.34 vs origin-matched persist 97/193 Spec A; 132.02/491.74 vs 79/288 Spec B) | three of four within 0.13 ft of M1, M2_Rar 0.41 ft worse, none retained; M2_Rprecip and M2_Rar edge past M1 only on the 2015–23 window |
| **Retained set** | **empty** | **empty** |
| Simulation power context | D1 0.955/0.960 high at T=33 low/high σ — non-retention is strong evidence against autonomous at collapse-window parameters and low noise; D2 high-noise power 0.060 shows strength conditioned on the noise regime | D3 0.110/0.100 and D4 0.010/0.010 low — non-retention is weak evidence for stock-flow/depensation; identification limit 1%/11% and 37%/18% versus 61% |
| Information-set audit | catch supplied along the horizon — conditional hindcast; total landings not age-structured removal; C_t total landings while S_t SSB so the removal term is not SSB-equivalent; failing to reproduce the collapse with the supplied catch path does not test whether fishing caused the collapse | recharge/pumpage supplied — conditional hindcast; pumpage is a partially institutional scenario; oracle in no information set; precipitation spelled out |

The two systems share a scalar stock driven by fluxes — precisely why one ladder applies to both — but little else physically. One is a reconstructed population state governed by recruitment, mortality, and harvest; the other is a measured water level governed by recharge and pumping. Karst conduits, the Uvalde–San Antonio divide, unconfined recharge-zone storage and confined-zone pressure response remain in residual, and the lumped-versus-EPM question is inherited, not resolved (Scanlon et al. 2003). They share a rule, and they return the same verdict.

One candidate mechanism for the domain contrast is the predictand itself. The cod target is an assessment output conditioned on the full series, while Edwards head is directly measured. Autocorrelation injected by that construction favours persistence, and the observed pattern — persistence unbeatable on the reconstructed target, three module-horizon cells beating persistence on the measured one — is consistent with the artefact, though not proof of it. Rescoring the same D1 replicates under an assessment-like centred 3-year smoother (n = 30 per arm) compresses the M1 persistence margin 7–13× (h=1: −8.9 → −0.6 kt at low σ, −23.2 → −1.8 kt at high σ) and lowers D1 power from 0.90/1.00 to 0.63/0.67. The mechanism is real and in the expected direction, but it is not sufficient alone: the non-retention verdict survives. The domain contrast remains multi-causal, consistent with the candidates listed in Supplement S1.

They do not return the verdict for the same reason, and that difference is what the pair demonstrates. On the marine series nothing comes close, so any reasonable rule would return the same answer and the gates would go untested. On the groundwater series, point ranking alone would have retained two module-horizon cells (M2m at h=1 and h=5) by point RMSE, withheld by the gates. The tie band and comparator gate withhold retention, and the class-grounds judgement withholds it a second time. **The rule’s gates can only be shown to be load-bearing on data where ranking would have decided otherwise, and only the second domain provides that.** A single application, in either domain, would have left the gates either untested or unmotivated.

Neither series is pooled with the other. No verdict is transferred between them. The two objects differ in every typed field. What recurs is the decision procedure, not the data or the mechanism.

---

## 8. Prospective registration

Nothing in the preceding sections commits the standard to a future evaluation. This subsection fixes the elements of that evaluation in advance, so that the next applications of the standard are commitments, fixed before their data are seen.

**Model set.** The seven-member ladder of Section 2.1 (five structural modules plus the persistence and training-mean baselines), the horizons h = 1 and h = 5, the one-step least-squares estimator with expanding training windows (minimum eight years), and the class-grounds pre-gate are carried forward unchanged. Additions to the ladder require a pre-registered amendment of the kind that introduced D6 and D7 (Amendment 1).

**Next origins.** Edwards J-17: the ten annual origins 2024–2033, each scored once with the recharge and pumpage available at that origin. Northern cod: Specification B origins from 2025 onward, re-scored as each new xteNCAM vintage is published (Regular et al. 2025 line). Specification A is closed, because its predictand is the fixed 2016 assessment vintage and no further origins exist. Archived origins are never re-scored for a published verdict. New origins are scored once, and the archived forecast files are appended.

**Prospective band.** For future applications the 5% band is replaced by the simulation-calibrated band registered in Section 6.5. Before any new origin is scored, the object’s own ladder is simulated at its own series length and noise scale, with each in-class member as generating truth and the persistence-true null for specificity, and the smallest band attaining power ≥ 0.80 and specificity ≥ 0.90 is adopted. If no band attains both targets, the attainable frontier is reported and the 5% band is retained. The calibration applies to future applications only and does not re-open any verdict reported here.

**Executed for the cod object.** Applying the procedure to the pinned-seed archive (Section 6.2), the frontier over bands of 0–15% declines from 0.444 mean power at band 0 to 0.312 at 15%, while specificity rises from 0.760 to 1.000. At the narrowest band that meets the specificity target alone (3.5%, specificity 0.935) mean power is 0.395, and no band attains both targets — power is identification-limited at every width. The attainable frontier is therefore reported and the 5% band is retained for the cod application. The T = 71 evidence is the registered ten-replicate point — D1 power 0.900/1.000 and D5 specificity 1.000/1.000 at the 5% band — and the full 200-replicate T = 71 frontier remains the registered campaign. The Edwards calibration is registered in a draft specification sheet and precedes the first scored origin, whose inputs are archived (the 2024–2025 panel rows). Northern cod Specification B origins begin with origin 2025, scored once the vintage following the 2026 assessment is published.

With these elements fixed, the reporting obligations of Sections 2 and 3 and the operating-characteristic discipline of this section extend unchanged to every future verdict. The prospective machinery adopted here is the machinery of the reproducibility movement: pre-registered designs and registered reports (Chambers, 2013), competition protocols with evaluation rules fixed in advance (the M4 and M5 competitions; Makridakis et al., 2020, 2022), and pinned-seed archival for computational reproducibility. The standard’s contribution to that movement is its object: not that a forecast was evaluated, but that a negative verdict — non-retention — is made interpretable by a rule, an audit, and measured operating characteristics fixed before the data are seen.

---

## 9. Scope and conclusions

**Licensed.** The standard is applicable to scored objects in unrelated domains. The original pre-registered rule had no tie band; the unified rule adds the 5% band to the groundwater application (Section 4). Verdicts are unchanged under both versions, and the rule returns interpretable verdicts in both domains. The gates are load-bearing, demonstrated on data where ranking alone would have retained a module. The oracle-module device makes the upper bound explicit. The declined-on-class-grounds category records when a module collapses to a simpler member (as the zero-threshold cubic branch of M1b does). The cross-system framing places the null at the core of the methods. Specificity against in-class alternatives is high and measured: 0.995/0.950 persistence-true; 0.034 per module-replicate pair wrong-module on D1–D4; 0.005/0.050 per replicate and 0.0055 per module-replicate under the null. Where the simulation shows power (D1 0.955/0.960), non-retention is evidence against the module. Structural modules still lose to persistence despite the supplied future catch, which strengthens the negative result.

**Not licensed.** Three limits bound every inference drawn here — the operating-characteristic design, the power bound (specificity included), and the domain count — and they are structural, not incidental.

**Series length.** Operating characteristics are established at a single series length of 33 years. Applications span 33 to 90 years; no length-sensitivity claim is made. Extending to longer records is the most direct remaining test. The T = 71 extension (10 replicates per cell) gives D1 power 0.900/1.000 and D5 false retention 0.000/0.000 (Section 6.3).

**Upper bounds.** Power figures are upper bounds. In-class processes are the easiest case. Misspecified processes show the rule over-retaining when truth leaves the class (D6 0.633/0.733, D7 0.933/0.867, versus the pre-declared 0.10 threshold; n = 30 per cell). Power against misspecified truth is not measured and is presumably lower. Specificity is thus conditional on in-class data. Non-retention of M3 and M4 has no estimated power, because the residual and delay modules were never simulated as generating truth.

**Two domains.** Recurrence across a fish stock and an aquifer is stronger evidence of portability than either alone, but no general claim about all dynamical systems is made.

**Implication for practice.** Any non-retention report should carry the standard’s three components. A verdict without a pre-stated rule, without an information-set audit, or without operating characteristics leaves the reader unable to distinguish a module that is uninformative from a rule that cannot see it. Those two opposite conclusions — module uninformative versus rule cannot see it — the score alone does not separate. Where a study reports non-retention, the minimum accompanying evidence is the rule’s power under processes the study’s own models could have generated, and its specificity under the null, with block-bootstrap intervals per Künsch (1989). That the information criterion dominates on both axes bears on instrument choice within the standard, not on the standard. The formal information-set table — what is available at origin t and to which module — is the most useful single addition, proposed as a reporting template.

---

**Conclusions.**

The minimum reporting standard for non-retention claims is stated and demonstrated: a retention rule as an explicit algorithm, an information-set audit, and a pre-registered operating-characteristic simulation, worked unchanged on three scored objects in two domains.

The two domains reach the outcome differently. On the marine series, no structural module approaches the tie band — closest at +9.01% (h=5) and +17.09% (h=1) on Spec A coarse-regime, and +35.94% to +43.98% on Spec B under either origin reading (Table 2) — so ranking decides alone. No Spec A margin against persistence has an interval excluding zero, though several Spec B margins do. The predictand is retrospectively reconstructed and catch is supplied along the horizon — a conditional hindcast, not an operational forecast — and total landings are not age-structured removals, so failure to reproduce the collapse with the supplied catch does not test whether fishing caused it.

On the groundwater series, three margins beat the baseline — M1 at h=1 (−2.96%, interval covering zero, MAE tie at 10.72 versus 10.73 ft, 5-year loss 21.25 versus 21.11 ft), M2m at h=1 (−7.16%, the only h=1 margin separated from noise) and at h=5 (−17.34%) — and the oracle’s fitted-map bound is −42.96% at h=1 and −48.52% at h=5. The training mean beats persistence at h=5 (16.80 versus 21.11 ft, interval excluding zero). Retention is withheld by the band, the comparator gate (4.33% M2m-versus-M1 at h=1), and the class-grounds judgement (M2m collapses to AR(1) under constant fluxes) — the gates doing the work. No climate module is retained; three of four lie within 0.13 ft of the autoregression and all lose to the climatological-flux map. Recharge is near-white, 0.17 versus ΔH, R 0.74 — causal stock-flow fails because the dominant increment is not persistent.

Simulation bounds the interpretation in both directions. The rule is specific against in-class alternatives — under persistence-true truth it retains nothing in 95–99.5% of replicates (0.995/0.950; 0.034 wrong-module per module-replicate pair on D1–D4; 0.005/0.050 per replicate and 0.0055 per module-replicate under the null) — and it recovers the true autonomous module in 95.5–96% of replicates at collapse-window parameters. Power is below 15% for the two other in-class alternatives, where the constraint is identification rather than the decision procedure: the generating module is frequently not even best-scoring (stock-flow is best in 1%/11% of replicates, below the 20% chance rate; autonomous 61%; depensation 37%/18%). Against truth outside the model class the rule over-retains in 63–93% of replicates, so specificity is conditional on the class rather than a property of the instrument. The information criterion penalising free parameters outperforms the rule on both axes (0.509/0.992 versus 0.373/0.973; Section 6.5).

Non-retention is therefore strong evidence against a module where the rule is shown to have power and weak evidence where it is not. Reporting a verdict without the standard’s three components cannot distinguish the two. The negative findings are themselves evidence for the standard: a pre-registered, calibrated rule retains nothing where the data are uninformative, and only the operating-characteristic study reveals the difference. A pre-check diagnostic identifying in advance where the rule has power remains open (dispersion Spearman 0.52 weak; margin 0.88 strong but circular and misclassifies stock-flow cells).

---

## Data availability

Computing cost per replicate is 2.2–16.7 s at T = 33 and 13–110 s at T = 71 on two CPU cores. The full 200-replicate T = 71 design for D1 and D5 is accordingly ≈ 25 CPU-hours and remains a registered longer campaign. Reproducibility: the operating characteristics in Section 6.3 were computed under pinned seeds (PYTHONHASHSEED = 0; numpy 2.3.5, scipy 1.17.1, pandas 2.2.3) and are archived together with their seed maps. The Edwards uncertainty layer was reproduced exactly in an independent environment (all six archived comparisons, including M2m versus persistence at h=5: margin −3.6607 ft, z = −3.284, p = 0.0016). M1b optimum is environment-sensitive ±1.6 kt at h=1 (151.6 versus 153.2) and ±17 kt at h=5 (445.5 versus 462.5), max ±17 kt.

All input data, analysis scripts, result files, and the pre-registered specifications are archived at https://github.com/MIKEAA2020/general-sustainability/tree/edwards-framework-e1 and https://zenodo.org/records/22553609 (E1) and 22552680 (E3). The prospective registration of Section 8 is filed with the specification sheets. Companion papers: Abaee (2026a) — the Edwards J-17 scored ladder; Abaee (2026b) — the Northern cod scored ladder.

Rolling summaries:

- `wave_e_cod/results/rolling_summary.csv` (Spec A regime+na filtered, coarse-regime)
- `wave_e_cod/results/xte_rolling_summary.csv` (Spec B)
- `wave_e_edwards/results/rolling_summary.csv`
- `wave_e_cod/results/sim_retention_power.csv` (the archived replicate table, 10,000 rows: 5 DGPs × 2σ × 200 × 5 modules; source of the alternative-rule comparison in Section 6.5)
- `phase_c/results/sim_retention_power_20260913.csv` and companions (pinned-seed campaign, source of Section 6.3: sim_misspecified_20260913.csv, smoother_test_20260913.csv, sim_origins_20260913.csv, sim_snr_sweep_20260913.csv, gate_hybrid_mcs_20260913.csv, reconcile_s43_20260913.csv, with seed maps and provenance files); o9_ic_coprimary_20260913.json (the co-primary information-criterion check of Section 6.5); o6_cod_band_calibration_20260913.json (the cod prospective-band calibration of Section 8)
- `wave_e_cod/results/sim_misspecified_D6D7.csv` (Amendment 1: D6 drifting r_t, D7 observation-error-only; 4 cells, 800 passes, 4,000 rows)
- `wave_e_edwards/results/e3_audit_uncertainty.json` (uncertainty layer, DM HAC + block bootstrap per Künsch 1989, p percentile-tail fraction p_perc) and `e3_audit_uncertainty_add_M2m_h5.json` (the M2m-versus-persistence h=5 test, computed with the same seeded machinery from the archived per-origin files)
- `batch 7 (audits of agent arena 1 paper rewrites)/results/e1_dm_uncertainty.csv` (independent replication of the uncertainty layer: 32 rows, 15 intervals exclude zero, 17 include; DM statistics descriptive, not calibrated)
- `batch 7 (audits of agent arena 1 paper rewrites)/results/e3_dm_uncertainty.csv` (10 rows)

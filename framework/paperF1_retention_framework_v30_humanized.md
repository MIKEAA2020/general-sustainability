# When a Model Is Not Retained, What Must Be Reported? A Retention Rule, an Information-Set Audit, and Operating Characteristics: A Minimum Reporting Standard Worked on Three Scored Objects in Two Domains

## Abstract

**Problem.** Process-based models are routinely elaborated with additional state variables, residual autocorrelation structures, and environmental covariates under the working assumption that mechanistic detail improves out-of-sample forecast accuracy. That assumption is rarely tested against a naive baseline under a decision rule fixed prior to scoring. When such tests are conducted, negative findings remain difficult to interpret: a module that is not retained may be genuinely uninformative, or the evaluation instrument may lack the statistical power to detect its contribution. Because the literature lacks a standard that makes non-retention claims methodologically interpretable, this article proposes a three-part minimum reporting standard and demonstrates its application.

**Approach.** The proposed standard requires three elements: (1) a retention rule formulated as an explicit, executable algorithm; (2) an information-set audit that strictly separates inputs available at the forecast origin from those supplied after it; and (3) a mandatory operating-characteristic simulation that quantifies the rule's statistical power and specificity under known ground truth. We demonstrate this standard without modification across three scored objects drawn from two unrelated domains: a marine fish stock evaluated under two distinct assessment specifications (Northern cod, NAFO Divisions 2J3KL, under Specification A [1983–2015] and Specification B [1954–2024]) and a karstic groundwater index well (Edwards Aquifer index well J-17, San Antonio Pool [1934–2023]). Full empirical specifications are provided in companion papers (Abaee, 2026a, 2026b); this article reports the formal verdicts, performance margins, gate decompositions, uncertainty analyses, and cross-domain comparisons.

**Findings.** Across all three scored objects, the retained model set is empty. For Northern cod, no structural candidate approaches the pre-registered 5% tie band at either forecast horizon ($h = 1$ or $h = 5$). Under Specification A, persistence yields root-mean-square errors (RMSE) of 98.05 kt ($h = 1$) and 264.72 kt ($h = 5$), whereas the closest structural model (the Allee-effect formulation M1b) trails persistence by +17.09% (114.80 kt) and +9.01% (288.58 kt), respectively. Under Specification B, persistence records 87.65 kt ($h = 1$) and 317.71 kt ($h = 5$) on the naive origin set (84.43 kt and 299.98 kt when origin-matched), while the baseline autonomous model M1 trails persistence by 36% to 44% across all readings. Over the critical collapse window (1991–1995), all structural candidates miss the stock collapse (scoring 694–819 kt versus 670 kt for persistence), despite being supplied with realized future catches along the forecast horizon—an informational advantage unavailable to operational forecasts. None of the Specification A performance margins against persistence exclude zero under moving-block bootstrap intervals, although several Specification B margins do. 

For the Edwards Aquifer, three module-horizon configurations outperform persistence on point RMSE: the autoregressive model M1 at $h = 1$ (12.839 ft versus 13.230 ft; a 2.96% margin whose confidence interval covers zero and whose mean absolute error ties persistence at 10.72 ft versus 10.73 ft), and the climatological-flux balance model M2m at $h = 1$ (12.283 ft versus 13.230 ft; a 7.16% reduction with a confidence interval excluding zero) and at $h = 5$ (17.445 ft versus 21.106 ft; a 17.34% reduction). An oracle model with perfect knowledge of future pumping and recharge achieves 7.547 ft at $h = 1$ (−42.96%) and 10.865 ft at $h = 5$ (−48.52%), establishing an empirical performance ceiling. Despite beating persistence, M2m is not retained: it fails the comparator gate at $h = 1$ by improving over M1 by only 4.33% (below the mandatory 5% tie band) and collapses to an autoregression under constant inputs, warranting rejection on substantive class grounds (structural redundancy). Climate-informed recharge covariates fail to improve forecasts: three of the four candidates remain within 0.13 ft of simple autoregression, all trail the climatological-flux map, and long-horizon water levels are predicted better by the historical training mean (16.80 ft versus 21.11 ft). Annual recharge behaves as near-white noise ($\text{corr}(R_t, R_{t-1}) = 0.17$) despite governing head changes ($\text{corr}(\Delta H_t, R_t) = 0.74$), causing causal stock-flow forecasts to fail because the driving increment cannot be predicted out of sample.

In simulation tests ($T = 33$, $\sigma \in \{11.8, 33.8\}\text{ kt}$), the retention rule exhibits high power to detect an autonomous collapse regime (D1: 0.955 at low noise, 0.960 at high noise) and high specificity under the persistence-true null (D5: 0.995 and 0.950). However, the rule has poor power to detect low-productivity recovery (D2: 0.780 and 0.060), stock-flow dynamics (D3: 0.110 and 0.100), or depensation (D4: 0.010 at both noise levels). The false-retention rate under the null is 0.0055 per module-replicate. This power deficit stems from parameter identification limits rather than gate conservatism: the true data-generating module achieves the lowest one-step error in only 1% to 11% of stock-flow simulations and 18% to 37% of depensation simulations. When evaluated against misspecified, out-of-class processes (time-varying productivity D6 and pure observation error D7), the rule erroneously attributes predictive gains to incorrect internal mechanisms in 63% to 93% of replicates, demonstrating that instrument specificity is strictly conditional on in-class data.

**Implications.** Non-retention constitutes strong evidence against a mechanism where the decision rule is statistically powerful (such as autonomous cod dynamics), but weak evidence where the rule is underpowered (such as stock-flow and depensation structures). Reporting a non-retention verdict without accompanying operating characteristics leaves readers unable to distinguish between an uninformative model and an uninformative test. An information criterion ($n \ln \text{MSE} + 2k$) outperforms the empirical retention rule in average synthetic power and specificity (0.509/0.992 versus 0.373/0.973) because it targets one-step fit, but it fails to evaluate multi-year horizons and would mistakenly retain structurally redundant models. Every non-retention claim should be accompanied by the rule’s power profile under plausible in-class dynamics, its specificity under a naive null, and block-bootstrap confidence intervals.

**Keywords:** model selection, out-of-sample forecasting, retention rule, reporting standard, operating characteristics, identifiability, conditional hindcast, stock assessment, groundwater, jackknife, climatological-flux map.

---

## 1. Introduction

Adding complexity to a process-based model is easy to justify in principle and difficult to evaluate in practice. Incorporating additional state variables, auto-correlated residual structures, observational lags, or environmental covariates is typically rationalized on the grounds that each addition captures a known physical or ecological mechanism. However, each structural elaboration introduces parameters that must be estimated from short, noisy historical records. Whether an elaboration yields genuine out-of-sample predictive skill is an empirical question distinct from whether the underlying mechanism exists. That question can only be resolved by benchmarking the elaborated model against naive baselines using an objective decision rule fixed before scoring begins. Extensive empirical forecasting studies have demonstrated the necessity of this discipline: across the 100,000 time series examined in the M4 forecasting competition, sophisticated structural models frequently failed to outperform simple statistical baselines (Makridakis et al., 2020).

Benchmarking against naive baselines has gained traction in natural resource management. Hindcast cross-validation protocols often assess prediction skill using metrics such as the Mean Absolute Scaled Error (MASE; Hyndman and Koehler, 2006). Kell et al. (2016) demonstrated the utility of hindcasting in marine stock assessments; Carvalho et al. (2021) subsequently codified predictive skill as one of four foundational acceptance criteria for assessment models; and Kell et al. (2021) showed that conventional residual analysis and retrospective diagnostics cannot substitute for out-of-sample predictive validation. 

Nevertheless, current validation practice suffers from two major limitations:
1. Scaled-error diagnostics are typically computed against the fitted survey index itself rather than against the unobserved latent system state (e.g., spawning biomass or groundwater head) upon which management decisions depend.
2. Baselines are typically deployed to certify or reject a single preferred model configuration, rather than to systematically adjudicate a graded ladder of structural elaborations.

When an elaborated model fails to outperform a naive baseline, the resulting negative finding is difficult to interpret. Does the failure imply that the hypothesized mechanism is absent or inconsequential in the target system? Or does it merely show that the data are too sparse, the noise too high, or the decision rule too conservative to detect the improvement? The literature offers no standardized reporting protocol to resolve this ambiguity.

This article proposes and demonstrates a domain-agnostic minimum reporting standard for non-retention claims, structured around three required components:
1. **An Algorithmic Retention Rule (Section 2):** A deterministic decision procedure evaluated across an ordered ladder of increasing structural complexity. A candidate module is retained if and only if it achieves a strictly greater than 5% reduction in root-mean-square error (RMSE) relative to both a naive baseline (last-value persistence) and its declared, next-simpler comparator module, across both short-term ($h = 1$) and medium-term ($h = 5$) forecast horizons. The rule includes a pre-scoring gate that disqualifies candidate modules on substantive class grounds if their structural formulation collapses into an existing, simpler model under operational conditions.
2. **An Information-Set Audit (Section 3):** An explicit accounting protocol that categorizes every operational input as *available* at the forecast origin, *supplied* exogenously after the origin, or *revised* in retrospective vintages. This audit establishes whether an empirical test functions as a genuine operational forecast or as an idealized conditional hindcast.
3. **A Mandatory Operating-Characteristic Study (Section 6):** A pre-registered simulation experiment that benchmarks the retention rule across synthetic data-generating processes of known truth. By measuring empirical power (the probability of retaining a true structural mechanism) and specificity (the probability of correctly rejecting structure under a naive null), this study characterizes the statistical sensitivity of the decision instrument.

We demonstrate the standard across three empirical objects from two unrelated dynamical systems: Northern cod (*Gadus morhua*, NAFO Divisions 2J3KL) evaluated under two distinct stock-assessment regimes (Specification A [1983–2015] and Specification B [1954–2024]), and the Edwards Aquifer artesian index well J-17 (San Antonio Pool [1934–2023]). Full hydrogeological and fisheries contexts are detailed in companion monographs (Abaee, 2026a, 2026b). Here, we report the unified comparative verdicts, margin decompositions, uncertainty intervals, and operating characteristics.

The primary contribution of this work is not the empirical discovery that naive persistence is difficult to beat in environmental forecasting—a finding already documented in both domains. Rather, the deliverable is the minimum reporting standard itself. Demonstrating that the identical decision rule produces an empty retained set across three scored objects through two entirely different operational pathways (ranking failures in cod versus gate-driven rejections in groundwater) illustrates how this standard makes negative model selection results scientifically interpretable.

---

## 2. The Retention Rule

### 2.1 Model Ladder and Empirical Scored Objects

The retention rule operates across an ordered model ladder: a forward-sequenced hierarchy of increasing mathematical complexity anchored by a naive baseline. This ladder is structured as a rooted directed tree rather than a simple chain: each candidate module has a single, pre-declared comparator representing the next-simpler structural configuration along its specific developmental branch. Model definitions, parameter bounds, optimization protocols, and comparator mappings are frozen prior to empirical scoring.

Across both empirical domains and the synthetic simulations, we evaluate a five-rung structural ladder alongside two naive baselines, detailed in Table 1.

**Table 1.** Scored empirical objects and model inventory. The Limit Reference Point (LRP) and regulatory thresholds define the secondary Brier misclassification metrics; all primary retention decisions are governed strictly by continuous RMSE.

| Empirical Object | Domain and Series Description | Temporal Window | Rolling Origins ($n$ at $h=1 / 5$) | Target Scale: SD(Target) / SD($\Delta\text{Target}$) | Management Threshold / LRP | Exogenous Driver / Forcing Inputs |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Northern Cod Spec A** | NCAM M-shift SSB (DFO 2016, Table A2) | 1983–2015 | 25 / 21 | 356.5 kt / 89.5 kt | 884.6 kt | Coarse 3-level catch regime (240 / 120 / 5 kt); plug-in mean catch $\bar{C} = 5.00\text{ kt}$ |
| **Northern Cod Spec B** | Extended xteNCAM SSB (Regular et al., 2025) | 1954–2024 | Structural: 59 / 55<br>Naive: 63 / 59 | 423.2 kt / 89.6 kt | 276.0 kt | Historical recorded landings (Regular et al., 2025, Table 1) |
| **Edwards Aquifer J-17** | Annual-mean index well water level | 1934–2023 | 75 / 71 | 14.70 ft / 12.34 ft | 660.0 ft (Critical Period trigger level) | Historical annual recharge ($R_t$) and permitted pumpage ($P_t$) |

To prevent cross-contamination, all model fits, forecasts, and evaluations are conducted independently for each object; no data are pooled.

**Cod ladder.** M1 is autonomous Schaefer, S_{t+1} = S_t + r S_t(1 − S_t/K) − C̄, with r and K free and C equal to training-mean catch, plugged not estimated. M1b is autonomous Allee, S_{t+1} = S_t + r S_t(1 − S_t/K) a(S_t) − C̄, with a(S) = (S − s)/(K − s), s ∈ [0, max_train S], r at bound 2.0. As s → 0, a(S) = S/K, the zero-threshold cubic branch. M2 is stock-flow with prescribed C_t. M3 is an AR residual, φ ∈ [−0.95, 0.95], e_u = ΔS_u − [g(S_u) − C_u] pre-clipping; no-intercept lag-one φ̂ = Σ e_u e_{u−1} / Σ e²_{u−1}, zeroed if the denominator is ≤ 0 or there are fewer than 4 residuals, clipped to [−0.95, 0.95]; the projected residual φ̂^k · e_last is added inside the update before clipping to [1e−3, 1e6] kt. M4 is a delayed-information stale-start experiment (M3 parameters, one-year-old state), kept in the ladder for symmetry, not retained. Baselines: naive_persist, naive_train_mean. K is optimised on [max_train S + 10, 5000] kt with a 500 kt multi-start initialiser. k_param denotes parameter count in the IC, k_decay drainage decay, ladder length k = 5. The per-origin lower bound is max_train S + 10 kt, the maximum taken over predictor states of the training transitions excluding the terminal state: ≈ 950.8 kt at the earliest origins (training maximum 940.8 kt, 1987) and 50.8 kt on the recovery-window training set (predictor-state maximum 40.8 kt, 2006). Reported fits attain the upper endpoint K = 5000 kt where the data prefer unbounded carrying capacity. M1 coarse C = 5.00 kt, r = 0.458, K = 500.0 kt, resting at the multi-start initialiser 500.0 kt (lower bound 50.8 kt), not pinned at the bound; annual C = 3.19 kt, r = 0.370, K = 5000.0 kt. M1b coarse K = 105.8 kt and annual K = 129.8 kt are interior valid fits, not bound violations. The objective is flat: MSE 127.4 → 149.9 over K ∈ [60, 5000]. M1/M1b catch-treatment values differ by ≤ 0.04 kt between treatments after displayed rounding (archived values differ: M1 h=1 120.5095 versus 120.5406, 0.0311 kt; M1b h=1 114.8024 versus 114.7665, 0.0359 kt). M1 and M2 coincide under the coarse regime because C_t ≡ 5 kt on both train and test of the recovery window makes the two prescriptions identical; under annual landings they differ (264 versus 303 kt at the recovery window). M1b s → 0 numerical 2.1 × 10⁻²³ coarse, 9.4 × 10⁻⁶ annual, with r pinned at 2.0, corresponds to the zero-threshold cubic branch a(S) = S/K, not Schaefer and not positive-threshold Allee. A minimum of six one-step transitions is the absolute minimum after dropping years with no carried index value for capelin modules (origin 1991 Spec A, 1988 Spec B), matching the estimator’s < 6 refusal guard. The main ladder on Spec B uses a 12-year minimum for structural models (n = 59/55) versus an 8-year minimum for naive models (n = 63/59).

**Edwards ladder.** M1 is one-pool affine, H_{t+1} = a H_t + b (autoregression φ̂ = 0.66, Pearson corr(H_t, H_{t−1}) = 0.64, consistent with discrete drainage-decay 1 − φ ≈ 0.34 yr⁻¹; continuous k = −ln 0.66 ≈ 0.42 yr⁻¹, e-folding 2.4 yr). M2 is two-parameter. M2m is training-mean balance, the climatological-flux map (best one-step 12.283 ft, the only margin separated from noise). M3 and M4 are extensions. M2_oracle is the oracle with realised future recharge and pumpage (declared unable to retain; diagnostic upper bound −42.96% at h=1, −48.52% at h=5 under the fitted map). Baselines: naive_persist, naive_mean (training mean 16.8048 ft versus persistence 21.1056 ft at h=5, interval excluding zero). The declined M2m still serves as the declared nested comparator for the climate rung, as fixed in the pre-registration. No year falls below the 240 daily-observation floor for the annual mean (minimum n = 242 daily observations in 1939). The 15-year rolling floor rule is vacuous on this 90-year panel. The complete estimation panel ends in 2023, whose provisional status is flagged. Q = −2876 + 4.77H (Q total spring discharge in cfs, H J-17 head in ft) implies Q = 0 near 603 ft, below the ≈ 618 ft reference, predicting the 1956 cessation of flow (tail failure) when head fell below the discharge threshold.

Estimation is one-step least squares on the training window. The h=5 score is endpoint RMSE (not a trajectory average) and compares the no-change forecast with iterated trajectories. The iterated affine analogue M2m is 17.44 ft (rolling h=5) and 17.64 ft (fixed-window h=5, n=12), each near the corresponding training mean. Log-RMSE uses the natural log with a 1e−3 floor (ordering unchanged with floors 1e−6 and 1e−9). Sign-hit rate uses adjacent-year n−1 comparisons. The Brier threshold is a misclassification rate (for a deterministic binary forecast, equivalent to the Brier score). The bare fact that targets fall below the LRP would not by itself make the persistence indicator correct; origin states being below does. Origins and targets must both be below. The same five-rung ladder and the same estimation functions are used across both domains and in the simulation (Section 6.2).

### 2.2 Algorithmic Retention Criteria

**Definition 2.1 (Retention rule, portable).** Module M is retained only if all of the following hold on rolling-origin primary RMSE (origin-matched, per Künsch 1989):

- **H1** — M reduces RMSE versus the declared comparator — the next-simpler rung for nested steps (M1b versus M1, M3 versus M2 on cod; M2m versus M1, M2 versus M1, M3 versus M2, M4 versus M3 on Edwards) — by strictly more than 5% of the comparator’s score.
- **H2** — M reduces RMSE versus last-value persistence by strictly more than 5%.
- **H3** — Each reduction holds at both horizons h=1 and h=5.

Fail any, and the module is not retained. Retention is decided per specification. Tie band b = 0.05: improvements of 5% or less are ties and are not retained; exactly 5% fails (strictly more than 5% is required). The deciding score is the pre-registered specification’s rolling-origin RMSE pair at h=1 and h=5 (H3). The band is a practical-equivalence margin: fixed here at 5% by pre-registration, it may instead be set on a simulation-calibrated basis (Section 8) or on a decision basis — a margin judged irrelevant to the decision at hand — with the basis stated.

Comparator: on cod, M2’s comparator is M1 and M4’s comparator is M3. An alternative comparator, M2 versus M1b, is reported as a sensitivity row on the primary passes: A h=1 +29.3 kt, z = 0.91 [−67.6, +82.8]; A h=5 +109.7, z = 0.98 [−77.1, +232.8]; B h=1 +14.4, z = 0.51 [−67.5, +89.1]; B h=5 +613.4, z = 1.93 [+170.9, +945.1].



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



The class-grounds check is a substantive pre-gate, evaluated before scoring: whether a module collapses to a simpler member under the conditions of application is knowable independent of the data. The algorithm box shows the class-grounds check first, matching the operational order. The class judgement is declared in the same specification as the ladder, fixed before any score is computed, so the decline of the only persistence-beating module is not an after-the-fact judgement. The retained set is empty under the rule alone (M2m fails H1 at h=1 under the unified rule), so the empty set holds either way. Without the band, M2m would pass H1 but still be declined on class grounds.

Scores are **origin-matched**: every comparison uses the module’s own origin set, and the baseline is recomputed on that set. On Spec B’s main ladder, a 12-year minimum for structural models versus an 8-year minimum for naive models gives origin-matched persistence of 84.43 kt versus mixed-origin 87.65 kt at h=1 (difference 3.22 kt) and 299.98 kt versus 317.71 kt at h=5 (difference 17.73 kt). On the index modules’ origin sets (capelin-informed productivity, Table 8 of the companion), persistence reads 97 kt (n=24, h=1) and 193 kt (n=20, h=5) on Spec A and 79 kt (n=36) and 288 kt (n=32) on Spec B. The index module loses to the origin-matched baseline in every cell. The five-year near-tie on Spec A is resolved by origin matching — the baseline on the module’s own origins reads 193 kt against the module’s 262 kt — and the one-year RMSE is worse under both readings (150 versus 98 kt on SSB origins and 97 kt on the module’s). The **tie band** suppresses retention inside sampling noise. The **comparator gate** prevents retention merely because a module beats the baseline when a simpler one does too.

**Definition 2.2 (Negative certificate).** A machine-verified finding of non-retention under a stated rule, scoped to estimator, ladder, and series. Weaker than a statistical null. Distinct from the Brier secondary diagnostic. The 1992–1993 fishing moratorium is deliberately not evaluated.

**Claim strength.** A negative certificate carries one of four levels. N0 — the rule ran and the verdict is its output. N1 — N0 plus archived margins and the gate decomposition, so the verdict is reproducible and its withholding gate is known. N2 — N1 plus the Section 3 information-set audit, so the verdict is scoped to what was available at each origin. N3 — N2 plus operating characteristics at the object’s own length and noise attaining the adequacy targets of Section 6.1, making non-retention evidential for the affected class. The verdicts reported here carry N2: the cod operating characteristics are class-conditional (power is limited by identification at every band width, Section 8), and the Edwards calibration is registered prospectively (Section 8). A certificate expires when its inputs change — a revised data vintage, a re-scored origin, an amended rule — and a combined claim carries the lowest level of its parts. N3 is the level at which non-retention may be reported as evidence rather than description.

### 2.3 Rejection on Substantive Class Grounds

A model may pass numerical error gates through trivial parameter degeneracy or structural redundancy rather than through genuine predictive skill. To prevent misleading retentions, the retention rule enforces a pre-scoring structural evaluation: if a candidate module collapses mathematically to an existing, simpler model configuration under its operating conditions, it is categorized as *declined on class grounds*.

This mechanism is directly illustrated by the Edwards Aquifer water-balance model M2m. Driven by static historical training-mean recharge $\bar{R}$ and pumping $\bar{P}$, the continuous head update equation simplifies to:
$$H_{t+1} = a H_t + c_1 \bar{R} - c_2 \bar{P} + d = a H_t + C^*$$
Because the training-mean fluxes are constant across the forecast horizon, they collapse into a single static intercept $C^*$. As a result, M2m becomes mathematically identical to an affine autoregression M1. While M2m achieves lower point RMSE than persistence at both horizons, retaining it as a physical "water balance" would misrepresent a constant-flux autoregressive fit as causal predictive skill. It is therefore rejected on substantive class grounds.

An analogous degeneracy occurs in the fisheries ladder with the Allee-effect depensation module M1b. When fit to historical Northern cod biomass series, numerical optimization drives the depensation threshold parameter $s$ to zero ($s \approx 2.1 \times 10^{-23}$ under Specification A; $s \approx 9.4 \times 10^{-6}$ under Specification B), with intrinsic growth $r$ pinned against its upper boundary of 2.0. This parameter configuration eliminates the lower threshold, converting the sigmoid depensation function into an unthresholded cubic production curve ($a(S_t) = S_t / K$). The lower error achieved by M1b during the post-collapse recovery window (RMSE of 90 kt versus 104 kt for persistence) is therefore an artifact of cubic curve fitting rather than empirical evidence of a critical Allee threshold.

---

## 3. The Information-Set Audit

A forecasting claim cannot be evaluated without an explicit accounting of what information was available when the forecast was made. Retrospective studies often inadvertently blend operational forecasting (using only historical data available at origin $t$) with conditional hindcasting (using exogenous drivers realized after origin $t$).

The information-set audit requires researchers to tabulate the provenance and availability of every data input, categorizing each into one of three operational states:
1. **Available ($u \le t$):** Recorded, published, and accessible prior to the forecast origin.
2. **Supplied ($u > t$):** Generated after the forecast origin and provided exogenously across the evaluation horizon (e.g., realized future catch, observed precipitation, or actual groundwater withdrawal).
3. **Revised:** Observed prior to the origin but published only within subsequent retrospective assessment vintages (e.g., model-smoothed historical spawning-stock biomass).



**Table 1a.** Model inventory with declared comparators, auxiliary modules, diagnostics, and naive baselines (frozen protocol record).

| Object | Rungs (declared comparator) | Auxiliary modules | Declared diagnostics | Naive baselines |
|---|---|---|---|---|
| COD Spec A/B | M1 (none), M1b (M1), M2 (M1), M3 (M2), M4 (M3) | capelin-index module (scored against its own origin-matched persistence) | — (M2–M4 already receive future catch; conditional hindcasts) | naive_persist, naive_train_mean |
| EDWARDS | M1 (none), M2 (M1), M2m (M1), M3 (M2), M4 (M3) | climate rung: M2_Rprecip, M2_Rar, M2_Renso, M2_combo (comparator M2m, declined — a protocol exception noted in the pre-registration) | M2_oracle (realised fluxes, declared unable to retain) | naive_persist, naive_mean |

**Table 2b.** Information-Set Audit Reporting Template. The assignment of inputs determines whether an evaluation represents an operational forecast or a conditional hindcast.


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


When candidate models are provided with realized driver trajectories along the forecast horizon ($u > t$), the exercise ceases to be an operational forecast and becomes a conditional hindcast. However, this informational asymmetry strengthens negative findings: if a structural model fails to outperform a naive baseline despite receiving future driver trajectories that an operational forecast could never access, its failure cannot be blamed on imperfect driver forecasts.

The utility of this distinction is highlighted by the diagnostic **Oracle module (M2_oracle)** in the Edwards Aquifer application. Provided with realized future recharge and pumping over the five-year horizon, the oracle achieves an RMSE of 7.547 ft at $h = 1$ (−42.96% relative to persistence) and 10.865 ft at $h = 5$ (−48.52%). This result shows that perfect future flux information cuts baseline forecast error roughly in half, establishing an empirical upper bound on predictability for this aquifer. Because no operational module can access future fluxes, practical performance necessarily falls between this theoretical ceiling and naive persistence.

Forecast uncertainty is quantified using two non-parametric techniques: Diebold–Mariano tests with heteroskedasticity- and autocorrelation-consistent (HAC) variance estimators, and moving-block bootstrap confidence intervals (Künsch, 1989) applied directly to paired trajectory loss differentials. All bootstrap distributions are conditioned on archived forecast paths.

---

## 4. Worked Example: Edwards Aquifer Index Well J-17

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

M1 fails H2 at both horizons. M2m passes H2 at both horizons but fails H1 at h=1. The companion declines M2m on class grounds, since it collapses to AR(1) under constant fluxes. Six margins sit inside the 5% band: M1 h=1 2.96%, M2m h=1 versus M1 4.33%, M3 h=1 1.63%, M4 h=1 1.13%, M3 h=5 0.08%, M4 h=5 0.21%. The 5% band and the both-horizon requirement are applied to the groundwater analysis even though the original pre-registered rule scored retention on h=1 alone and without a band. Within the unified rule the band changes no outcome. Under the unified rule with the band, M2m fails H1 at h=1 (4.33% < 5%) and is additionally declined on class grounds. Without the band it would pass H1 but still be declined on class grounds, so the empty set holds either way. The M2m decline is a ladder-membership verdict — the map reduces to the simpler AR(1) member under the declared conditions — not a predictive finding; its predictive margins remain reported in Table 5 (−7.16% and −17.34% versus persistence). The companion’s pre-registered h=1 point rule retains M1 provisionally — a 0.39 ft margin within noise, MAE tied at 10.72 versus 10.73 ft, a five-year loss — while the unified rule withholds it: the 2.96% h=1 margin lies inside the band and M1 loses at h=5 (21.25 versus 21.11 ft). The empty retained set is a property of the unified rule. The M1 difference between the two readings is a recorded rule-version difference, not a data difference. The gate demonstration uses the unified rule. A post-2007 h=5 reversal, M1 17.16 versus persist 25.10, is reported without changing the one-year retention statement. The h=5 score compares the no-change forecast with iterated trajectories. Scores at h > 1 for climate modules reuse the one-step forecast held constant — no h-year-ahead recharge or pumpage forecast is available at the origin, and the one-step forecast is the only origin-available flux estimate.

**Uncertainty layer.** The AR(1) 0.39 ft margin has an interval covering zero; MAE is tied (10.72 versus 10.73 ft); the 5-year loss is a tie to within rounding. Retention by the point-RMSE rule records this, not a skill claim. The training mean, 16.8048 versus 21.1056 ft, has an interval excluding zero at h=5. The load-bearing gate decision (M2m versus M1, 4.33% against the 5% band) sits within numerical tolerance of the environment sensitivity measured on cod (±17 kt on 445.5 kt, 3.8%). An Edwards cross-environment reproduction is reported in Data availability. Persistence remains the decision baseline because it is the pre-registered H2/H3 anchor. The training mean’s superiority at h=5 is reported as evidence about the baseline choice, not as a re-baselining. Fixed-window M2 RMSEs are 18.11 and 55.32 ft. The fixed-window pre-permit pass uses its declared train 1980–1990 (11 yr). The 15-year floor applies to rolling origins only; fixed windows use their declared training sets.

**Decision context.** The Edwards verdicts bear on forecasting claims about J-17, not on the monitoring or permitting framework itself. Persistence remains the decision baseline — the pre-registered H2/H3 anchor — and non-retention records that no module demonstrated operational skill over it at one or five years: a statement about the evidence available at the origin, which leaves the index well and its management instruments in place. The oracle bound shows what perfect driver information would buy (−42.96% at h=1) and what the module class leaves on the table.

---

## 5. Worked Example: Northern Cod (NAFO Divisions 2J3KL)

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

**Uncertainty layer.** Diebold–Mariano loss-differential diagnostics and moving-block-bootstrap intervals attach to the margins, reported as descriptive; the verdicts do not rest on DM statistics, which are not calibrated for this design (expanding-window recursive estimation, overlapping training samples, near-nested models, a smoothed target, multiple comparisons). The mechanics and the full 32-row universe are in Supplement S1. Bootstrap intervals are conditional on archived forecast paths and propagate no parameter, revision, catch, or covariate uncertainty.

**Conditional hindcast disclosure.** The predictand is retrospectively reconstructed rather than taken from vintages at each origin, and catch is supplied along the horizon. This is a conditional hindcast, not an operational forecast, and must not be reported as skill.

**Decision context.** The cod verdicts are hindcast verdicts about assessment-module forecast utility, not verdicts about stock status or about the assessments themselves. The scored target is the assessment’s own retrospective biomass, and modules supplied the realised catch still fail to beat persistence, so the verdict licenses the negative forecasting claim and nothing about the drivers of the collapse: total landings are not SSB-equivalent removals, and the failed collapse reproduction does not test whether fishing caused it.

---

## 6. Operating Characteristics

### 6.1 The Need for Instrument Calibration

Evaluating an empirical retention rule requires understanding its operating characteristics:
* What is its statistical power (the probability of retaining a structural module when the underlying data-generating process possesses that structure)?
* What is its specificity (the probability of rejecting structural modules when the underlying system follows a naive persistence process)?

If an empirical rule exhibits near-zero power to detect a given mechanism in synthetic benchmarks, a negative empirical finding provides little evidence against that mechanism. Conversely, if an instrument exhibits high power and high specificity, an empirical rejection constitutes strong evidence that the mechanism provides no out-of-sample predictive utility.

To resolve this question, we established a pre-registered simulation protocol to evaluate the empirical retention rule under known, controlled ground truth.

The pre-registered threshold defining an adequate decision instrument was established at $\text{power} \ge 0.80$ and $\text{specificity} \ge 0.90$.

### 6.2 Data-Generating Processes

A run-time calibration check for D6/D7 confirmed usable replicates at $\sigma = 33.8$ with biomass inside the observed range; a naive regime-switch candidate degraded $900 \to 888 \to \cdots \to 305 \to 77 \to 0$ in four steps and was rejected at design time.

Synthetic series are generated using the mathematical update functions of the empirical ladder, with sample lengths matching Specification A ($T = 33$) and process noise standard deviations reflecting the empirical recovery window ($\sigma = 11.8\text{ kt}$) and collapse window ($\sigma = 33.8\text{ kt}$).
* **D1 (Autonomous Collapse):** In-class Schaefer dynamics initialized at collapse parameters ($r = 1.935$, $K = 1032.7\text{ kt}$, constant harvest $C = 240\text{ kt}$).
* **D2 (Autonomous Recovery):** In-class Schaefer dynamics reflecting low-productivity recovery conditions ($r = 0.458$, $K = 500.0\text{ kt}$, harvest $C = 5\text{ kt}$).
* **D3 (Stock-Flow Dynamics):** In-class surplus production driven by a three-tiered historical catch regime ($C_t \in \{240, 120, 5\}\text{ kt}$).
* **D4 (True Depensation):** In-class depensatory dynamics with an identifiable Allee threshold ($s = 15.0\text{ kt}$, $r = 0.458$, $K = 500.0\text{ kt}$).
* **D5 (Persistence-True Null):** Pure random walk without biological surplus production ($S_{t+1} = S_t + \eta_t$).
* **D6 (Time-Varying Productivity):** Structurally misspecified process with an exponentially decaying intrinsic growth rate ($r_t = 1.935 e^{-0.05 t} + 0.35$), a mechanism absent from the model ladder.
* **D7 (Pure Observation Error):** Structurally misspecified system where the true latent state evolves deterministically ($r = 0.90$, $K = 1032.7\text{ kt}$, $C = 180\text{ kt}$), but is observed with additive Gaussian noise ($Y_t = S_t + \epsilon_t$).

Modules M3 and M4 were not simulated as generating truths, serving as structural controls.



**Table 6a.** Data-generating processes with parameters anchored to archived fits (frozen before scoring).

| DGP | Truth | Parameters anchored to archived fits | Why in/out of class |
|---|---|---|---|
| **D1** | M1 autonomous Schaefer | r = 1.935, K = 1032.7, constant C = 240 (collapse-window fit) | in-class |
| **D2** | M1 low-productivity | r = 0.458, K = 500.0, constant C = 5 (recovery-window) | in-class |
| **D3** | M2 stock-flow | r = 1.935, K = 1032.7, prescribed C_t = coarse regime 240/120/5 | in-class |
| **D4** | M1b genuine depensation | r = 0.458, K = 500.0, s = 15 kt, a positive identifiable threshold unlike the real fits s → 0 | in-class |
| **D5** | Persistence-true null | S_{t+1} = S_t + η_t, no surplus, C ≡ 0 | null |
| **D6** | Time-varying productivity (Amendment 1) | r_t = 1.935 · exp(−0.05t) + 0.35, K = 1032.7, catch 55% of instantaneous rK/4 | out-of-class: no ladder member has time-varying r |
| **D7** | Observation error only (Amendment 1) | state evolves noise-free, r = 0.9, K = 1032.7, C = 180; scored series = state + Gaussian noise | out-of-class: the ladder treats deviation as process noise; here the state is deterministic and the noise is in measurement |

### 6.3 Simulation Results and Evidential Weight

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

### 6.4 Identification Limits versus Decision Gate Filter Conservatism

Power is low for three of four in-class structural processes; the cause is identification, not the gates.


Why does the retention rule fail to detect stock-flow dynamics (D3) and depensation (D4)? Analyzing the simulation outputs reveals that this failure is driven by parameter identification limits rather than gate conservatism.

Removing all decision gates and tie bands—requiring only that the true structural module beat persistence at $h = 1$ on point RMSE—still retains the true model in only 33% of stock-flow runs and 18% of depensation runs. In an inventory of five models, random chance would assign the lowest error to the true model 20% of the time. The stock-flow module achieves the lowest error in only 1% (low noise) and 11% (high noise) of D3 runs—performing worse than a random draw. For replicates that do beat persistence, the comparator gate filters out 72% of stock-flow candidates and 93% of depensation candidates because their marginal improvement over simpler models is smaller than the 5% tie band.

### 6.5 Structural Misspecification and Information Criteria

The reported verdicts are band-invariant: on cod no margin approaches the band (the ranking alone decides, §5), and on Edwards the withheld module is declined on class grounds at any band (§4). The simulation-calibrated band targeting power $\ge 0.80$ and specificity $\ge 0.90$ at the object's own $T$ and SNR is therefore registered as the prospective replacement for future applications of the standard; it never re-opens the verdicts reported here.

Evaluating the rule against misspecified, out-of-class processes (D6 and D7) reveals an important constraint: instrument specificity is strictly conditional on in-class data. When evaluated on synthetic series generated with decaying productivity (D6) or pure observation error (D7), the rule erroneously retains structural modules in 63% to 93% of replicates, in almost every case selecting the autonomous model M1. 

In these misspecified runs, M1 achieves genuine out-of-sample predictive gains over persistence (averaging +2.6 to +9.4 kt at $h = 1$). The rule's decision logic correctly identifies that M1 provides predictive skill; however, that predictive advantage is driven by fitting an misspecified process rather than capturing the model's hypothesized biological mechanism. Model retention certifies empirical predictive utility, not internal physical truth.

**Table 7.** Comparison of alternative decision rules across synthetic simulations ($n = 10,000$ runs).

| Evaluated Decision Rule | Mean Empirical Power (D1–D4) | In-Class Specificity (D5) | Misspecification False Retention (D6–D7) | Operational Assessment |
| :--- | :--- | :--- | :--- | :--- |
| **Retention Rule as Stated (Gates H1–H3 + 5% Band)** | 0.376 | 0.978 | 0.835 | High specificity; conservative; low average power |
| **Without Comparator Gate (H2 + H3 Only)** | 0.476 | 0.972 | 0.862 | Modest power gain (+0.100); preserves specificity |
| **Baseline Gate Only at Single Horizon ($h = 1$)** | 0.562 | 0.955 | 0.890 | Increases power; loses multi-horizon validation |
| **Baseline Gate Only (Any Margin, No Band)** | 0.542 | 0.765 | 0.912 | Substantial loss of specificity (−0.213) |
| **Rule without Tie Band ($b = 0.00$)** | 0.436 | 0.772 | 0.884 | Unacceptable loss of null specificity (−0.206) |
| **Rule with Strict 10% Tie Band ($b = 0.10$)** | 0.337 | 0.998 | 0.725 | Overly conservative; degrades power |
| **Conventional Scaled Error Criterion ($\text{MASE} < 1$)** | 0.651 | 0.675 | 0.945 | Severe false retention under null (32.5%) |
| **Information Criterion ($n \ln\text{MSE} + 2k$)** | **0.509** | **0.992** | **0.615** | Superior synthetic metrics; lacks multi-horizon evaluation |

The tie band plays a central role in stabilizing the decision rule: removing it ($b = 0.00$) increases power by only 0.060 while reducing specificity by 0.206, leading to false retentions in nearly 23% of persistence-true null series. Conversely, relying exclusively on conventional scaled errors ($\text{MASE} < 1$) yields high apparent power (0.651) at the cost of poor specificity, retaining structural models in 32.5% of null series.

The Akaike-style information criterion ($n \ln\text{MSE} + 2k$) outperforms the empirical retention rule across all synthetic metrics, achieving higher mean power (0.509 versus 0.376), higher specificity (0.992 versus 0.978), and lower mechanism misattribution under structural misspecification (0.615 versus 0.835). However, this criterion evaluates only one-step-ahead fits ($h = 1$) and penalizes purely by parameter counts, omitting the requirement that models demonstrate predictive skill over medium-term management horizons ($h = 5$). 

When applied to the empirical objects, the information criterion selects persistence for both Northern cod specifications (agreeing with the retention rule), but selects M2m for the Edwards Aquifer (IC = 455.5 versus 463.5 for M1 and 464.9 for persistence). The information criterion would thus retain a model that fails the comparator gate and collapses to an autoregression under operational conditions. This divergence highlights why physical model evaluation requires multi-horizon testing and substantive class checks alongside numerical fit metrics.

---

## 7. Cross-Domain Comparison

**Table 8.** Systematic comparison of empirical findings and diagnostic evaluations across domains.

| Diagnostic Evaluation Metric | Northern Cod (NAFO 2J3KL) | Edwards Aquifer Index Well J-17 | Cross-Domain Diagnostic Significance |
| :--- | :--- | :--- | :--- |
| **Target Dynamical System** | Subarctic marine fish population | Karst artesian aquifer system | Unrelated physical and biological mechanisms |
| **Target Variable Type** | Reconstructed latent state (SSB) | Directly measured physical state (Head) | Contrasts reconstructed vs directly measured states |
| **Historical Data Record** | 33 years (Spec A) / 71 years (Spec B) | 90 years (1934–2023) | Tests across varied sample lengths |
| **Structural Model Ladder** | 5 rungs: M1, M1b, M2, M3, M4 | 5 rungs: M1, M2, M2m, M3, M4 | Matched mathematical model architectures |
| **Models Outperforming Baseline (Point RMSE)** | **None** (All candidates trail persistence) | **Three module-horizons** (M1 $h=1$; M2m $h=1, 5$) | Contrasts ranking failures vs gate rejections |
| **Closest Structural Margin vs Persistence** | +9.01% (Spec A, M1b, $h = 5$) | −17.34% (M2m, $h = 5$; −7.16% at $h = 1$) | Highlights contrasting empirical accuracy profiles |
| **Dominant Rejection Mechanism** | **Direct Ranking Failure** (RMSE >> Persistence) | **Decision Gates and Class Grounds** | Demonstrates different pathways to non-retention |
| **Diagnostic Performance Ceiling (Oracle)** | Not evaluated | **M2_oracle** (−42.96% $h=1$; −48.52% $h=5$) | Establishes theoretical predictability limit |
| **Training Mean Performance ($h = 5$)** | Trails persistence across all runs | **Outperforms persistence** (16.80 vs 21.11 ft) | Demonstrates long-term mean reversion |
| **Climate Covariate Utility** | Capelin index fails across all origins | Lagged ENSO/precipitation fail ($h=1, 5$) | Climate covariates fail to add predictive skill |
| **Final Retained Model Set** | **Empty** | **Empty** | Unified non-retention outcome |
| **Operating Characteristics Context** | High power on D1; poor power on D3/D4 | Dominant driving flux ($R_t$) behaves as white noise | Explains failures via power and flux dynamics |
| **Information Audit Classification** | Conditional hindcast (reconstructed target, catch supplied) | Conditional hindcast (pumping and recharge supplied) | Prevents mistaking hindcasts for operational skill |

**Table 8a.** Cross-application record in the companion's frozen row format (protocol rows not recoded by register).

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



The empirical results reveal two contrasting pathways to an empty retained set:
* In the **fisheries application**, candidate models fail at the first hurdle: none approach naive persistence on point RMSE at any horizon. As a result, the decision gates and tie bands never engage.
* In the **groundwater application**, candidate models outperform persistence across three module-horizon configurations. Here, the decision gates are directly load-bearing: Module M1 is filtered out by the baseline gate at $h = 5$, while Module M2m is filtered out by the comparator gate at $h = 1$ and rejected on substantive class grounds.

Evaluating the retention rule on either domain alone would have provided an incomplete picture. Testing it solely on Northern cod would leave the decision gates unexercised; testing it solely on the Edwards Aquifer would leave open whether the rule could identify strong ranking failures. Evaluating the rule across both domains demonstrates that it functions consistently across both scenarios.

One candidate explanation for the domain contrast lies in how the target variables are constructed. Northern cod spawning biomass is an unobserved latent state reconstructed by an integrated assessment model conditioned on the entire historical time series. This smoothing injects autocorrelation into the target series, favoring naive persistence. In contrast, Edwards Aquifer water levels are directly measured physical observations. 

To evaluate this hypothesis, we re-scored the synthetic D1 replicates ($n = 30$ per arm) after applying a centered three-year moving average to simulate assessment smoothing. The moving average reduced the M1 performance advantage over persistence by a factor of 7 to 13 (from −8.9 kt to −0.6 kt at low noise; from −23.2 kt to −1.8 kt at high noise) and decreased D1 detection power from 0.90/1.00 down to 0.63/0.67. While assessment smoothing substantially degrades empirical power, it is not sufficient on its own to explain the full performance gap between structural models and persistence in Northern cod.

---

## 8. Prospective Protocol Registration

To prevent post-hoc adjustments in future evaluations, we register the operational components of the next assessment cycle in advance:

1. **Model Ladder and Estimation Machinery:** The seven-member model inventory (five structural rungs and two naive baselines), the forecast horizons ($h \in \{1, 5\}$), the one-step expanding least-squares estimator (minimum training window of 8 years), and the substantive class-grounds check are preserved unchanged.
2. **Evaluation Windows:**
 * **Edwards Aquifer J-17:** Ten annual forecast origins spanning 2024–2033. Each origin will be evaluated once using only water-level, recharge, and pumping data available at that origin.
 * **Northern Cod:** Specification B will be updated with annual origins from 2025 onward as new xteNCAM assessment vintages are published. Specification A is permanently closed, as its historical assessment series is frozen. Archived origins will not be re-scored.
3. **Simulation-Calibrated Prospective Decision Band:** For future evaluations, the static 5% tie band will be replaced by an empirical band calibrated by simulation. Prior to scoring new origins, the model ladder will be simulated across the target system's sample length ($T$) and signal-to-noise ratio ($\text{SNR}$). The calibrated band will be set to the narrowest width that achieves $\text{power} \ge 0.80$ across in-class structural truths and $\text{specificity} \ge 0.90$ under the null. If no band satisfies both targets, the empirical frontier will be reported and the baseline 5% band preserved.
4. **Prospective Calibration for Northern Cod:** Applying this calibration protocol to the archived Northern cod simulation outputs demonstrates that as the tie band widens from 0% to 15%, mean power declines from 0.444 to 0.312, while specificity increases from 0.760 to 1.000. The narrowest band achieving the specificity target ($\ge 0.90$) is 3.5% (specificity = 0.935, power = 0.395). Because parameter identification limits prevent the ladder from reaching the 0.80 power threshold at any band width, the standard 5% tie band is retained for future Northern cod evaluations.

---

## 9. Scope and Methodological Conclusions

### 9.1 Licensed Inferences

The empirical and synthetic results support several methodological conclusions:
1. The three-part reporting standard (algorithmic retention rule, information-set audit, and operating-characteristic simulation) is practical, portable, and effective across disparate dynamical systems.
2. The decision gates and tie bands are functional, preventing the erroneous retention of models that achieve minor numerical advantages through parameter redundancy or noise fitting.
3. Incorporating an oracle diagnostic establishes a clear performance ceiling, helping researchers determine whether forecast error is driven by mathematical misspecification or by unmeasured driving fluxes.
4. When simulation benchmarks establish that a decision rule has high power ($LR^- \ge 20:1$, as observed for autonomous Schaefer dynamics under collapse conditions), failing to retain that module provides strong evidence that the mechanism provides no out-of-sample predictive utility under the evaluated conditions.
5. Supplying structural models with realized future catches along the forecast horizon does not enable them to outperform naive persistence, reinforcing the negative empirical finding for Northern cod.

### 9.2 Critical Limitations and Unlicensed Inferences

This evaluation is bounded by three structural constraints:
1. **Sample Length Limitations:** Operating characteristics were evaluated primarily at a sample length of $T = 33$ years, with limited checks at $T = 71$. These results do not characterize the rule's performance across multi-century or high-frequency records.
2. **Upper-Bound Nature of Synthetic Power:** Power estimates were derived under in-class data-generating processes where the candidate models matched the underlying truth. Because real-world systems are never perfectly in-class, these synthetic power estimates represent upper bounds on practical performance. Furthermore, because Modules M3 (residual AR) and M4 (information delay) were not simulated as generating truths, their non-retention is unaccompanied by statistical power estimates.
3. **Domain Scope:** Demonstrating consistent performance across a subarctic marine fish stock and a karst artesian aquifer shows that the standard is portable between disparate systems, but does not imply that its findings hold universally across all dynamical systems.

### 9.3 Methodological Recommendations for Environmental Forecasting

When a process-based model fails to outperform a naive baseline, reporting that negative finding requires the same methodological rigor as claiming a breakthrough. Reporting a non-retention verdict without its operating characteristics leaves readers unable to distinguish between an uninformative model and an uninformative test. 

To ensure negative model selection results are scientifically interpretable, every non-retention study should report:
1. A pre-registered decision rule formulated as an explicit algorithm, complete with performance tie bands and a declared comparator hierarchy.
2. An information-set audit that explicitly differentiates operational forecasts from conditional hindcasts.
3. An operating-characteristic simulation that quantifies the rule’s statistical power under in-class processes and its specificity under a naive null, accompanied by block-bootstrap confidence intervals.

Providing these three components ensures that non-retention findings can be evaluated objectively, establishing whether a negative result reflects a genuine limitation of the model or an uninformative test.

---

## Data and Code Availability

Computing cost per replicate is 2.2–16.7 s at T = 33 and 13–110 s at T = 71 on two CPU cores. The full 200-replicate T = 71 design for D1 and D5 is accordingly ≈25 CPU-hours and remains a registered longer campaign. Reproducibility: the operating characteristics in Section 6.3 were computed under pinned seeds (PYTHONHASHSEED = 0; numpy 2.3.5, scipy 1.17.1, pandas 2.2.3) and are archived together with their seed maps. The Edwards uncertainty layer was reproduced exactly in an independent environment (all six archived comparisons, including M2m versus persistence at h=5: margin −3.6607 ft, z = −3.284, p = 0.0016). M1b optimum is environment-sensitive ±1.6 kt at h=1 (151.6 versus 153.2) and ±17 kt at h=5 (445.5 versus 462.5), max ±17 kt.

All input data, analysis scripts, result files, and the pre-registered specifications are archived at https://github.com/MIKEAA2020/general-sustainability/tree/edwards-framework-e1 and https://zenodo.org/records/22553609 (E1) and 22552680 (E3). The prospective registration of Section 8 is filed with the specification sheets. Companion papers: Abaee (2026a) — the Edwards J-17 scored ladder; Abaee (2026b) — the Northern cod scored ladder. Supplements S1 and S2 are distributed with the manuscript: S1 carries the verification and sensitivity detail (uncertainty-robust variants, the pre-check diagnostic, the verification appendix, and the Diebold–Mariano mechanics); S2 is the standalone two-page specification and fillable checklist.

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

## References

* Abaee, A., 2026a. Does a one-pool water-balance model improve forecasts of Edwards Aquifer head? A scored test at J-17. Zenodo. https://doi.org/10.5281/zenodo.22552680.

* Abaee, A., 2026b. Does a surplus-production ladder improve forecasts of Northern cod? A scored test on NAFO 2J3KL. Zenodo. https://doi.org/10.5281/zenodo.22553609.

* Carvalho, F., et al., 2021. A cookbook for using model diagnostics in integrated stock assessments. Fisheries Research 240, 105959.

* Chambers, C.D., 2013. Registered Reports: A new publishing initiative at Cortex. Cortex 49, 609–610.

* DFO, 2016. Stock assessment of Northern cod (NAFO Divs. 2J3KL). DFO Can. Sci. Advis. Sec. Sci. Advis. Rep. 2016/026.

* Hyndman, R.J., Koehler, A.B., 2006. Another look at measures of forecast accuracy. International Journal of Forecasting 22, 679–688.

* Kell, L.T., et al., 2016. Evaluation of the prediction skill of stock assessment using hindcasting. Fisheries Research 183, 119–127.

* Kell, L.T., et al., 2021. Validation of stock assessment methods: is it me or my model talking? ICES Journal of Marine Science 78, 2244–2255.

* Künsch, H.R., 1989. The jackknife and the bootstrap for general stationary observations. Annals of Statistics 17, 1217–1241.

* Makridakis, S., Spiliotis, E., Assimakopoulos, V., 2020. The M4 Competition: 100,000 time series and 61 forecasting methods. Int J Forecasting 36, 54–74.

* Makridakis, S., Spiliotis, E., Assimakopoulos, V., 2022. The M5 accuracy competition: results, findings, and conclusions. International Journal of Forecasting 38, 1346–1364.

* Regular, P.M., et al., 2025. Assessment of the Northern cod stock in NAFO Divisions 2J3KL in 2024. DFO Can. Sci. Advis. Sec. Res. Doc. 2025/048.

* Scanlon, B.R., et al., 2003. Barton Springs segment Edwards. Groundwater.

## Declarations

### Data availability

All input data, analysis scripts, and frozen result files are archived at https://github.com/MIKEAA2020/general-sustainability. Companion archives: Northern cod (https://doi.org/10.5281/zenodo.22553609), Edwards Aquifer J-17 (https://doi.org/10.5281/zenodo.22552680). All computations are deterministic: re-executing the registered scripts in a fresh environment regenerated every archived result file byte for byte.

### Declaration of competing interests

None declared.

### Funding

No funding was received for this work.

### CRediT authorship contribution statement

Amin Abaee: conceptualization, data curation, formal analysis, investigation, methodology, software, validation, visualization, writing — original draft, writing — review and editing.

### Statement on the use of generative artificial intelligence

Generative-AI tools were used for language editing, register smoothing, and token-level drift checks of this manuscript. All scientific statements, numbers, protocol events, and conclusions are the author's; all AI-produced phrasing was verified against the frozen sources and archives before release.

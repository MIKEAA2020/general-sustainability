# Does Structural Elaboration Improve Biomass Forecasts? A Pre-Registered, Power-Aware Out-of-Sample Evaluation of Surplus-Production Models for Northern Cod (*Gadus morhua*)



**Prepared in the format of Fisheries Research.**

## Highlights

• A pre-registered, power-aware protocol scores structure against active naive baselines
• The scored target is the management quantity used in control rules, not fitted indices
• No module in the five-module ladder beats persistence at one or five years
• Simulation: non-retention carries different evidential weight across modules
• The evaluation framework is transferable to stock-assessment and ecological forecasting

## Abstract

Does adding structure to a surplus-production model improve its forecasts of Northern cod (NAFO Divisions 2J3KL)? Five surplus-production models and two naive baselines are compared under a scoring rule fixed before the scores were read. The benchmark is persistence: next year's spawning biomass equals this year's. Retention requires a model to beat persistence and the next-simpler model by more than 5% at both the one-year and five-year horizons, on error pooled over rolling forecast origins. Information availability at the forecast origin is documented for every quantity each model uses.

The target is the assessment's reconstructed biomass because that is the operational quantity in which control rules and rebuilding verdicts are written. Two published estimated series describe the same stock and are evaluated separately: the 2016-assessment series (1983–2015) and the extended reconstruction (1954–2024). The exercise is a conditional hindcast—the reconstruction is retrospective and three models receive realised catches over the forecast horizon. Both features favour the structural models, which makes the negative result conservative with respect to structure.

No model is retained on either series. On the 2016-assessment series, pooled one-year RMSE is 98 kt for persistence against 115–196 kt for the structural models; at five years, 265 kt against 289–488 kt. On the extended series, origin-matched one-year RMSE is 84 kt for persistence against 120 kt for the best structural model. From a fixed pre-collapse origin, every model misses the 1991–1995 collapse (694–819 kt, against 670 and 688 kt for the baselines). The ladder's one-dimensional maps cannot generate a collapse followed by recovery, so collapse-window scores measure the misspecification penalty of a class that cannot generate the event, rather than relative forecast skill between persistence and structure. The negative result is target-robust: scored under the same frozen rule against the raw autumn research-vessel survey index (1983–2015), no model is retained—persistence records 120.5 kt-equivalents against 156.3–371.3 for the ladder at one year, and 249.2 against 355.5–880.5 at five years.

Simulation against known ground truths (Section 3.7) shows the evaluation rule to be highly specific against in-class alternatives (97–99% rejection under a true persistence null) and powerful (97–99%) when an autonomous surplus signal is strong under collapse-window conditions, while empirical power falls below 15% for stock-flow and depensatory dynamics under depleted conditions. The empirical conclusion applies to this ladder, this estimator, and this scoring design. The result bears on forecast skill, not on stock status; no tested model is shown to be the best available. The evaluation design itself is transferable: define the management target, declare an ordered structural ladder and its comparators, score the candidates against active naive baselines under a frozen rule, quantify uncertainty, and calibrate the evidential weight of non-retention through power analysis. These findings demonstrate that out-of-sample forecast skill cannot be assumed from structural elaboration alone and underscore the necessity of scoring any proposed forecasting structure directly against naive reference baselines on decision-relevant quantities.

**Keywords:** Northern cod, biomass forecasting, surplus production, forecast evaluation, stock assessment, prediction skill, model identifiability

## 1. Introduction

The question is whether a surplus-production ladder forecasts Northern cod biomass better than persistence. The target is the assessment reconstruction—the quantity in which control rules and rebuilding verdicts are written. A forecast of that quantity is what advice consumes; a forecast of an unobserved latent state, however well posed, does not enter the decision framework in the same units. Raw monitoring series enter the ladder in three roles: the RV fall survey index initialises survey-start models, capelin acoustic indices enter as covariates, and landing tables enter as removals. Scoring directly against a survey index is a distinct reference-definition question—a different target rather than a different method; Section 3.8 discharges exactly that test, re-scoring the frozen ladder against the raw autumn survey index under a protocol pre-registered before any survey score was read.

Stock assessment science operates under an implicit structural imperative: when model diagnostics falter or management questions expand, standard practice adds parameters, auxiliary data streams, or dynamic couplings. State-space age-structured models, multi-parameter surplus-production formulations, and ecosystem-linked extensions are routinely deployed in the expectation of generating more accurate and robust scientific advice. Yet, within empirical forecasting, structural elaboration does not automatically translate into improved predictive skill. In the surplus-production implementations evaluated here, added mathematical structure consistently fails to pay for itself out-of-sample: across a five-module model ladder evaluated on two unpooled assessment reconstructions of Northern cod (*Gadus morhua*), no structural formulation achieves a lower pooled rolling-origin root mean squared error (RMSE) than a naive, last-value persistence baseline at either a one-year or five-year horizon.

Although pooled rolling errors favor the persistence rule, this pattern is not temporally uniform; during the rapid collapse phase of the early 1990s, persistence exhibits substantial errors, and structural formulations fit to immediate pre-collapse transitions read lower on select one-step updates. Nonetheless, whether structural elaborations improve genuine out-of-sample forecasting—as opposed to optimizing retrospective in-sample fit—is an empirical question for which the burden of proof must fall on the proposed complexity.

That burden of proof has increasingly entered modern assessment protocols. Evaluation against naive benchmarks has emerged as a core diagnostic requirement. In particular, hindcast cross-validation frequently measures out-of-sample prediction skill using the Mean Absolute Scaled Error (MASE; Hyndman and Koehler, 2006), which scales forecast errors by the one-step in-sample mean absolute error of a random walk. A MASE statistic exceeding unity indicates that the fitted model predicts less accurately than a naive assumption of zero change (Kell et al., 2016, 2021). Contemporary diagnostic guidelines categorize out-of-sample prediction skill as an essential acceptance criterion alongside numerical convergence, goodness of fit, and retrospective consistency (Carvalho et al., 2021; Kokkalis et al., 2024). Consequently, the naive persistence baseline employed in this study is already the canonical reference standard in international fisheries science.

Standard validation protocols exhibit two critical methodological shortcomings that leave the core question unresolved:
1. **Target Disconnect:** Cross-validation diagnostics such as MASE are predominantly computed on the *relative abundance indices* fitted within the objective function, rather than on the estimated absolute stock biomass upon which harvest control rules and management advice are formulated. A model may successfully track an observation index while its underlying absolute biomass trajectory drifts or degrades out-of-sample.
2. **Binary Certification without Structural Ranking:** Diagnostic tests are conventionally applied as a binary pass/fail gate to certify a single, highly integrated assessment model. They are rarely deployed to rank a systematically graded sequence of structural additions simultaneously against one another and against a naive baseline.

These two shortcomings are not unique to Northern cod or to surplus-production models. In many assessment and forecasting settings, validation diagnostics are computed on observation-scale quantities rather than on the management-scale quantities used in control rules, and complex models are certified through binary pass/fail gates rather than ranked against simpler declared comparators and naive baselines. The present case study therefore also serves as a template for a more general forecast-evaluation protocol, and its transferability is made explicit in Sections 2.3 and 4.6.

To address these limitations, we present a scored model evaluation where the predictand is the assessment model's own derived spawning stock biomass (SSB), each structural increment has a declared and ordered comparator, and the naive persistence forecast serves as an active competitor rather than a passive scaling denominator.

Northern cod in Northwest Atlantic Fisheries Organization (NAFO) Divisions 2J3KL provides the canonical stress test for fisheries prediction. The catastrophic collapse of the late 1980s and early 1990s—wherein spawning biomass plummeted from an apparently stable state to a tiny fraction of its historical mean—occurred under an assessment and management system whose systematic failures were extensively analyzed in landmark post-mortems (Hutchings and Myers, 1994; Walters and Maguire, 1996). The subsequent prolonged failure to recover following the July 1992 fishing moratorium has kept debates regarding demographic depensation open for over three decades (Shelton and Healey, 1999). Although substantial rebuilding occurred in the mid-2010s (Rose and Rowe, 2015), stock growth has subsequently stalled, exhibiting negative net surplus production in multiple recent years (Rose, 2026).

Throughout this study, the target metric is the physical condition of the reproductive stock—the spawning stock biomass that sustains future productivity—rather than the yield extracted by the fishery. A fishery may sustain large landings during initial stock decline due to hyperstability or high fishing effort, but an operational forecast must accurately track the reproductive base. Any surplus-production model proposed for strategic advice must clear a fundamental hurdle: it must demonstrate greater predictive skill than the naive assumption of no change. 

We structure this evaluation using a model-retention rule whose algorithmic core was fixed prior to scoring: an additional module is retained if and only if it reduces rolling-origin RMSE relative to both the next-simpler structural comparator and a last-value persistence baseline across both one-year and five-year forecast horizons. The evaluation operates along a forward-ordered ladder of discrete-time surplus-production models:
* An autonomous Schaefer map with mean catch;
* An Allee-effect depensation extension;
* A dynamic stock-flow formulation with prescribed annual catch;
* An autoregressive residual tracking module;
* A lagged-initialization module representing assessment latency;
* Trophic- and acoustic-index-scaled extensions evaluated as auxiliary variants.

This investigation evaluates whether stock-flow, residual, delay, or prey-informed modules systematically reduce SSB forecast error relative to naive persistence and baseline autonomous models. The scope is diagnostic and empirical: we do not attempt to establish an absolute Allee threshold, isolate the definitive historical cause of the 1990s collapse, or evaluate the policy adequacy of the 1992 moratorium. 

Because an empirical negative result is only as informative as the statistical power of the diagnostic test, we evaluate the operating characteristics of the retention rule itself using pre-registered simulation experiments across known ground-truth processes. This diagnostic benchmarking establishes where the rule possesses the statistical power to identify true structural dynamics, where likelihood surfaces become flat, and where empirical non-retention reflects data limitations rather than definitive absence of biological complexity.

---

The paper proceeds as follows. Section 2 states the models, the scoring rule, the information-set audit, and the protocol timing. Section 3 reports the scored margins, the decomposition of the delay and survey-start experiments, and the uncertainty layer. Section 4 discusses interpretation; Appendix A consolidates the technical and computational specification. Section 5 concludes.

## 2. Materials and Methods

### 2.1 Data and Assessment Specifications

We score all models across two distinct, unpooled stock assessment series. The structural attributes of each specification are categorized into four types: Data ($\mathrm{D}$), Empirical construct ($\mathrm{E}$), Model assumptions ($\mathrm{M}$), and Normative management thresholds ($\mathrm{N}$).

**Specification A (Primary Specification):** Based on the Northern Cod Assessment Model (NCAM) M-shift formulation reported by Fisheries and Oceans Canada (DFO, 2016, Table A2; Cadigan, 2016), spanning 1983–2015 (Table 1).

#### Table 1. System specification for the primary NCAM M-shift assessment series (1983–2015).
| Field | Specification Details | Type |
| :--- | :--- | :---: |
| **System** | Northern cod (*Gadus morhua*), NAFO Divs. 2J3KL, represented by NCAM M-shift SSB | $\mathrm{D}$ |
| **Management Objective** | Maintain spawning biomass in the Healthy/Cautious zone above the Precautionary Approach LRP | $\mathrm{N}$ |
| **Spatial/Temporal Domain** | NAFO Divs. 2J3KL management area; calendar years 1983–2015 | $\mathrm{D}$ |
| **Safe Boundary** | $S_t \ge \mathrm{LRP} = 884.6\text{ kt}$ (mean estimated SSB over 1983–1989; DFO, 2016) | $\mathrm{N}$ |
| **Disturbance Dynamic** | Unspecified scalar productivity shocks; not explicitly resolved via a fitted $M(t)$ process | $\mathrm{M}$ |
| **Theoretical Removals** | Non-negative catch sequence: $C_t \ge 0$ | $\mathrm{M}$ |
| **Realized Removals** | Pre-1992 commercial fishery; post-July 1992 moratorium and localized inshore stewardship harvests | $\mathrm{E}$ |
| **Evaluation Horizon** | Hindcast 1983–2015; two fixed historical windows and rolling-origin evaluations ($h=1, 5$) | $\mathrm{D}$ |
| **Trophic Couplings** | Capelin excluded in primary ladder; evaluated as an auxiliary variant in Section 3.4 | $\mathrm{M}$ |
| **Normative Reference** | 2010/2016 DFO Precautionary Approach LRP ($884.6\text{ kt}$), distinct from the 2024 revision | $\mathrm{N}$ |

*Note to Table 1:* Safe boundary and LRP fields define the normative frame for secondary binary classification (Brier scores); primary model ranking and retention are evaluated strictly on rolling-origin RMSE and do not incorporate reference thresholds. Fishing mortality ($F$) and natural mortality ($M$) from Table A2 of DFO (2016) represent joint state-space outputs and are not treated as exogenous inputs.

**Specification B (Extended Historical Specification):** Based on the extended state-space assessment model (xteNCAM) developed by Regular et al. (2025), spanning 1954–2024. This reconstruction implements a revised limit reference point of $\mathrm{LRP} = 276\text{ kt}$ (95% CI: $180\text{--}423\text{ kt}$, corresponding to $40\%\,B_{\mathrm{MSY}}$) and estimates the 2024 terminal SSB at $342\text{ kt}$. 

Specifications A and B diverge across five fundamental dimensions:
1. Dynamic state equations (NCAM M-shift vs. xteNCAM);
2. Temporal coverage (1983–2015 vs. 1954–2024);
3. Normative reference points ($884.6\text{ kt}$ vs. $276\text{ kt}$);
4. Historical catch series reconstructions;
5. Retrospective horizons.

Because these assessment series differ substantially in their historical state trajectories, parameterizations, and data sources, they are evaluated independently without data pooling. No retention outcome or parameter estimate is transferred across specifications.

---

### 2.2 Mathematical Formulations of the Forecast Ladder

We model Northern cod biomass dynamics as a discrete-time scalar mapping, where spawning biomass $S_t$ is expressed in kilotonnes ($\text{kt}$) and annual removals $C_t$ in kilotonnes per year ($\text{kt}\cdot\text{yr}^{-1}$).

#### Definition 2.1 (Surplus-Production Map with Depensation)
The generalized discrete-time surplus-production map is given by:
$$S_{t+1} = \Big[ S_t + g(S_t) - C_t + \varepsilon_t \Big]_+$$
where $[\,\cdot\,]_+ = \max(\,\cdot\,, 0)$, and the surplus-production function $g(S_t)$ is parameterized as:
$$g(S_t) = r \, S_t \left(1 - \frac{S_t}{K}\right) a(S_t)$$
The structural multiplier $a(S_t)$ governs the presence of depensation:
$$a(S_t) = \begin{cases} 1 & \text{(Standard Schaefer logistic form; no Allee effect)} \\ \dfrac{S_t - \mathfrak{s}}{K - \mathfrak{s}} & \text{(Active depensation with Allee threshold } \mathfrak{s} > 0\text{)} \end{cases}$$

The factor $a(S_t)$ operates as a continuous structural modulation rather than a binary switch. In the limit $\mathfrak{s} \to 0$, the multiplier collapses to $a(S_t) = S_t / K$, producing a cubic surplus-production relationship rather than the classical quadratic Schaefer law. Thus, the Schaefer model is a distinct structural branch rather than a nested parameter restriction of the depensatory model.

#### Estimation and Operational Conventions
1. **Deterministic Projections:** The process disturbance $\varepsilon_t$ is treated solely as an equation error during parameter estimation on historical training windows. In forward forecasting, we set $\varepsilon_{t+k} = 0$, generating deterministic plug-in trajectories rather than multi-step integrated expectations (with the exception of modules M3 and M4, which project residual states).
2. **Residual Autoregression (M3 and M4):** Modules M3 and M4 estimate training residuals $e_u = \Delta S_u - [g(S_u) - C_u]$ prior to state clipping. The lag-1 autoregressive coefficient $\hat{\phi}$ is estimated via ordinary least squares without an intercept:
   $$\hat{\phi} = \frac{\sum_{u} e_u e_{u-1}}{\sum_{u} e_{u-1}^2}$$
   If the denominator is non-positive or the training window contains fewer than four transitions, $\hat{\phi}$ defaults to 0; otherwise, it is restricted to $[-0.95, 0.95]$. In recursive multi-step forecasting, the projected disturbance at step $k \ge 1$ is modeled as $\hat{\phi}^k e_{\mathrm{last}}$, where $e_{\mathrm{last}}$ represents the terminal training residual. This term is added directly to the structural update prior to enforcing a numerical floor of $10^{-3}\text{ kt}$ and a ceiling of $10^6\text{ kt}$.
3. **Catch Sequencing:** Removals $C_t$ represent total catch taken over the interval $[t, t+1)$. A forecast initialized at origin $t$ incorporates the catch recorded for that interval. For multi-step trajectories ($h=5$), realized catches along the projection horizon are supplied exogenously from published landing tables. Consequently, this exercise represents a *conditional hindcast* with respect to catch rather than a fully autonomous operational forecast.
4. **Catch Regimes:** On Specification A, we evaluate two catch sequences:
   * *Coarse Catch Regime:* Derived from DFO (2016) narratives, setting $C_t = 240\text{ kt}$ for $t \le 1991$, $C_t = 120\text{ kt}$ for $t = 1992$, and $C_t = 5\text{ kt}$ for $t \ge 1993$.
   * *Annual Landings Series:* Reconstructed historical landings from Schijns et al. (2021, Table 1). For 1983–1993, this series matches official STATLANT records and Regular et al. (2025) exactly (11-year absolute difference $= 0\text{ t}$). Landings dropped to $41\text{ kt}$ in 1992, $11\text{ kt}$ in 1993, $1.31\text{ kt}$ in 1994, and $0.41\text{ kt}$ in 1995.
5. **Optimization Bounds:** Parameters are fitted via one-step least squares over the expanding training windows. Effective sample sizes correspond to the number of one-step transitions ($m-1$ transitions for an $m$-year window). The parameter bounds are:
   $$r \in (0.001, 2.0], \quad K \in [\max_{\mathrm{train}}(S_t) + 10, 5000]\text{ kt}$$
   where $\max_{\mathrm{train}}(S_t)$ evaluates only over the predictor states of the transitions, excluding the terminal state. Optimization initializes from a multi-start value of $K = 500\text{ kt}$. For depensatory models, the Allee threshold is constrained to $\mathfrak{s} \in [0, \max_{\mathrm{train}}(S_t)]$ with the biological feasibility requirement $0 \le \mathfrak{s} < 0.8K$ enforced directly within the objective function.

The evaluated model ladder comprises seven distinct configurations ordered by structural complexity (Table 2).

#### Table 2. Structural ladder of evaluated forecast models.
| Model ID | Structural Classification | Estimated Parameters (Training Window) | Forecast Projection Formulation |
| :--- | :--- | :--- | :--- |
| **persist** | Naive Baseline | None | $\hat{S}_{t+h} = S_t$ |
| **mean** | Historical Baseline | Historical training mean $\bar{S}_{\mathrm{train}}$ | $\hat{S}_{t+h} = \bar{S}_{\mathrm{train}}$ |
| **M1** | Autonomous Schaefer | $r, K$; Catch fixed at training mean ($\bar{C}$) | Autonomous map using static $\bar{C}$ |
| **M1b** | Autonomous Depensatory | $r, K, \mathfrak{s}$; Catch fixed at training mean ($\bar{C}$) | Depensatory map using static $\bar{C}$ |
| **M2** | Dynamic Stock-Flow | $r, K$; Driven by annual catch sequence $C_t$ | Dynamic map using realized sequence $C_{t+k}$ |
| **M3** | Residual Autoregressive | $r, K$ fitted; AR(1) coefficient $\hat{\phi}$ on residuals | M2 dynamics $+ \hat{\phi}^k e_{\mathrm{last}}$ |
| **M4** | Lagged Initialization | Refitted identical to M3 | Multi-step projection initialized from $S_{t-1}$ |

*Auxiliary Variants:*
* *Survey-Start Variant:* Initial biomass $S_t$ is replaced by $\hat{q} I_t$, where $I_t$ is the autumn research-vessel trawl survey abundance index and $\hat{q}$ is the running median ratio of $\mathrm{SSB}/I$ over the training window.
* *Prey-Informed Variants:* Surplus production is dynamically scaled by capelin (*Mallotus villosus*) availability using either a two-regime step function (pre/post 1991 regime break; Murphy et al., 2025) or a continuous power function $(I_t / I_{\mathrm{ref}})^b$ driven by the Division 3L spring acoustic survey biomass index (DFO, 2024b).

---

### 2.3 Evaluation Protocol and the Model-Retention Rule

#### Table 2b. Information availability at forecast origin $t$.
| Quantity | Real-Time Status at Origin $t$ | Utilization by Forecast Modules |
| :--- | :--- | :--- |
| **Historical Target Series ($S_u, u \le t$)** | Available (single retrospective assessment) | All modules and baselines |
| **Current State ($S_t$)** | Available | All modules except M4 |
| **Lagged State ($S_{t-1}$)** | Available | M4 (initializes forecast trajectory) |
| **Training Transitions ($u \le t$)** | Available (expanding window) | Parameter estimation for M1–M4 |
| **Terminal Residual ($e_{\mathrm{last}}$)** | Available | M3, M4 |
| **Historical Catch ($C_u, u \le t$)** | Available | M1, M1b (mean); M2–M4 (trajectory) |
| **Future Catch ($C_u, u > t$)** | **Supplied exogenously (realized hindcast)** | M2, M3, M4 |
| **Prey Index ($I_u, u \le t$)** | Available (carried forward if missing) | M_cap_index |
| **Future Prey Index ($I_u, u > t$)** | Not used | None |
| **Reference Point (LRP)** | Fixed by historical specification | Secondary binary Brier evaluation only |

To ensure robust evaluation across different regimes, rolling-origin training windows expand over time (Table 2c). An origin is scored only if the preceding training window satisfies minimum sample size requirements (8 years for Specification A; 12 years for Specification B).

#### Table 2c. Rolling-origin evaluation sets across specifications and horizons.
| Experiment / Model Series | Horizon ($h$) | Number of Origins ($n$) | Origin Range |
| :--- | :---: | :---: | :---: |
| **Specification A Ladder** | 1 | 25 | 1990–2014 |
| **Specification A Ladder** | 5 | 21 | 1990–2010 |
| **Specification B Ladder** | 1 | 59 | 1965–2023 |
| **Specification B Ladder** | 5 | 55 | 1965–2019 |
| **Specification B Baselines (Unmatched)** | 1 | 63 | 1961–2023 |
| **Specification B Baselines (Unmatched)** | 5 | 59 | 1961–2019 |
| **Prey Acoustic Index (Spec A)** | 1 | 24 | 1991–2014 |
| **Prey Acoustic Index (Spec A)** | 5 | 20 | 1991–2010 |
| **Prey Acoustic Index (Spec B)** | 1 | 36 | 1988–2023 |
| **Prey Acoustic Index (Spec B)** | 5 | 32 | 1988–2019 |
| **Prey Regime Step (Spec A)** | 1 | 25 | 1990–2014 |
| **Prey Regime Step (Spec B)** | 1 | 59 | 1965–2023 |

#### Evaluation Metrics
The primary evaluation criterion is the Root Mean Squared Error (RMSE) across origin-target pairs:
$$\mathrm{RMSE}_h = \sqrt{\frac{1}{n} \sum_{i=1}^n \left(\hat{S}_{t_i+h \mid t_i} - S_{t_i+h}\right)^2}$$
For $h=5$, the score measures the error of the terminal five-year-ahead state, not the cumulative error along the intervening path. 

Secondary performance diagnostics include:
* Mean Absolute Error ($\mathrm{MAE}$);
* Logarithmic RMSE: evaluated on $\log\max(\hat{S}, 10^{-3}\text{ kt})$;
* Binary Brier Score: measures skill in forecasting stock status relative to the normative reference point, evaluating the deterministic indicator $\mathbf{1}\{\hat{S}_{t+h} < \mathrm{LRP}\}$;
* Directional Sign-Hit Rate: the proportion of transitions where $\operatorname{sign}(\hat{S}_{t+1} - S_t) = \operatorname{sign}(S_{t+1} - S_t)$. Because persistence forecasts zero change ($\Delta S = 0$), its directional hit rate is undefined ($\mathrm{NA}$).

#### Formal Specification of the Model-Retention Rule
Model selection is governed by three formal criteria:

A candidate structural module $M$ from the ladder is retained if and only if:
1. **Hypothesis 1 (Structural Superiority, H1):** Module $M$ reduces rolling-origin RMSE relative to its declared simpler comparator:
   $$\mathrm{RMSE}(M, h) < (1 - \delta) \, \mathrm{RMSE}(\operatorname{comp}(M), h)$$
   Comparators are defined by structural ordering: M1b compares against M1; M2 compares against M1; M3 compares against M2; and M4 compares against M3. Because M1 is the baseline structural module, H1 is vacuous for M1.
2. **Hypothesis 2 (Baseline Superiority, H2):** Module $M$ reduces rolling-origin RMSE relative to last-value persistence:
   $$\mathrm{RMSE}(M, h) < (1 - \delta) \, \mathrm{RMSE}(\mathrm{persist}, h)$$
3. **Hypothesis 3 (Dual-Horizon Consistency, H3):** Conditions H1 and H2 must hold simultaneously at both $h=1$ and $h=5$, where $\delta = 0.05$ represents a mandatory 5% tie band designed to filter out gains within sampling noise.

Although implemented here for surplus-production models of Northern cod, the evaluation design is general. Any forecasting problem with a reconstructed or observed management target, a set of candidate structural models, and one or more naive baselines can be scored under the same logic: declared comparators, frozen scoring horizons, information-set documentation, rolling-origin scoring, uncertainty quantification, and power calibration of the retention rule. The retention rule, the information-set documentation, and the operating-characteristic calibration execute, for this stock, the minimum reporting standard for non-retention claims proposed in the companion framework paper (Abaee, 2026d).

---

## 3. Results

### 3.1 Primary Specification (NCAM M-shift, 1983–2015)

We first evaluate model performance across two historically significant fixed windows: the stock collapse (training 1983–1990, testing 1991–1995) and the subsequent stalled recovery (training 1995–2007, testing 2008–2015).

![NCAM M-shift SSB (DFO, 2016, Table A2). Dashed line: 2016 LRP = 884.6 kt. 2015 SSB is 33.8 % of that LRP, matching the advisory report statement of 34 %.](figs/fig1_series.png)

#### Table 3. Fixed-window out-of-sample forecast performance (Specification A, coarse catch regime).
| Test Window | Model | RMSE (kt) | MAE (kt) | log-RMSE | Brier Score | Direction Hit |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **Collapse (1991–1995)** | **persist** | **670** | **610** | **2.71** | **0.00** | **NA** |
| | M1 | 694 | 638 | 2.73 | 1.00 | 0.50 |
| | M1b | 694 | 636 | 2.73 | 0.80 | 0.00 |
| | M2 | 819 | 751 | 2.85 | 1.00 | 0.25 |
| | M3 | 819 | 751 | 2.85 | 1.00 | 0.25 |
| | M4 | 819 | 750 | 2.85 | 1.00 | 0.25 |
| | mean | 688 | 630 | 2.72 | 0.00 | NA |
| **Recovery (2008–2015)** | persist | 104 | 72 | 0.69 | 0.00 | NA |
| | M1 = M2 | 120 | 105 | 0.61 | 0.00 | 0.57 |
| | **M1b** | **90** | **55** | **0.52** | **0.00** | **0.57** |
| | M3 | 220 | 200 | 0.92 | 0.00 | 0.57 |
| | M4 | 214 | 195 | 0.91 | 0.00 | 0.57 |
| | mean | 144 | 124 | 1.60 | 0.00 | NA |

Across the 1991–1995 collapse window, every structural module fails completely (Table 3). Parameter optimization over the weakly trending pre-collapse phase (1983–1990) yields an intrinsic growth rate near its upper ceiling ($\hat{r} = 1.935$, with bound $r \le 2.0$) and $\hat{K} = 1032.7\text{ kt}$. When future catches are reduced from $240\text{ kt}$ down to $5\text{ kt}$ post-1992, the stationary stock-flow equation mechanically forces projected biomass to surge upward, directly contradicting the observed collapse. Consequently, providing the realized catch history exogenously in M2 inflates forecast RMSE from $694\text{ kt}$ (autonomous M1) to $819\text{ kt}$. 

On the fixed recovery window (2008–2015), M1 and M2 yield identical projections because catches are constant at $5\text{ kt}$ across both training and testing periods. Here, M1b posts a lower RMSE ($90\text{ kt}$) than persistence ($104\text{ kt}$). However, this mathematical improvement is a numerical artifact of parameter boundary behavior rather than evidence of demographic depensation.

#### Observation 3.1 (Parameter Boundary Collapse on the Recovery Window)
Under Definition 2.1, if the Allee threshold $\mathfrak{s}$ exceeds the minimum observed training biomass, the depensation multiplier $a(S_t) = (S_t - \mathfrak{s}) / (K - \mathfrak{s})$ turns negative for any state below $\mathfrak{s}$. During the 1995–2007 training window, 7 of the 12 observed annual transitions exhibit positive biomass increments ($\Delta S_t > 0$) despite depleted stock levels. Fitting a positive $\mathfrak{s}$ incurs massive least-squares penalties on these positive transitions. 

To minimize squared residuals, the optimization algorithm drives $\mathfrak{s}$ downward toward zero ($\hat{\mathfrak{s}} = 2.1 \times 10^{-23}\text{ kt}$ under the coarse catch regime; $9.4 \times 10^{-6}\text{ kt}$ under annual landings), while $\hat{r}$ saturates at its upper ceiling of $2.0$ and $\hat{K}$ collapses to $105.8\text{ kt}$—just above the maximum predictor state of the training window ($40.83\text{ kt}$). Because the objective function enforces $\mathfrak{s} > 0$, the algorithm approaches an infimum rather than an interior biological parameter estimate. At this boundary, M1b functionally collapses to the cubic surplus-production form:
$$g(S_t) \approx r \, S_t^2 \left(1 - \frac{S_t}{K}\right) \frac{1}{K}$$
The apparent error reduction achieved by M1b is driven entirely by this flexible polynomial shape fitting the local scatter, not by identifying a true critical Allee threshold.

Profiling the sum of squared errors across $\mathfrak{s} \in [0, \min_{\mathrm{train}} S_t] = [0, 9.68]\text{ kt}$ demonstrates severe parameter non-identifiability. Across this entire range, the profile objective shifts by only $0.78$ units under the coarse catch regime (from $126.50$ to $135.04\text{ kt}^2$) and by $0.35$ units under annual landings. As $\mathfrak{s}$ varies from $0$ to $9.68\text{ kt}$, $\hat{K}$ compensates by sliding from $106.0\text{ kt}$ down to $82.7\text{ kt}$, maintaining an almost perfectly invariant surplus-production trajectory. The data cannot separate $\mathfrak{s}$ from $K$.

#### Table 4. Summary of rolling-origin forecast skill (Specification A, coarse catch regime).
| Forecast Model | $h=1$ RMSE (kt) | $h=1$ MAE (kt) | $h=1$ log-RMSE | $h=5$ RMSE (kt) |
| :--- | :---: | :---: | :---: | :---: |
| **persist** | **98** | **48** | **0.52** | **265** |
| **M1** | 121 | 80 | 8.02 | 289 |
| **M1b** | 115 | 80 | 8.70 | 289 |
| **M2** | 144 | 61 | 0.59 | 398 |
| **M3** | 135 | 53 | 3.39 | 366 |
| **M4** | 196 | 82 | 0.76 | 488 |
| **mean** | 424 | 375 | 2.35 | 507 |

Under rolling-origin cross-validation (Table 4), naive persistence outperforms every structural model at both forecast horizons ($98\text{ kt}$ at $h=1$; $265\text{ kt}$ at $h=5$). The structural modules fail Hypothesis 2 unambiguously, resulting in complete non-retention. Residual tracking (M3) improves multi-step projections relative to the base stock-flow model M2 ($366\text{ kt}$ vs. $398\text{ kt}$ at $h=5$), clearing Hypothesis 1, but remains substantially worse than naive persistence. Module M4 (lagged initialization) exhibits the highest projection errors among structural candidates ($196\text{ kt}$ at $h=1$; $488\text{ kt}$ at $h=5$).

---

### 3.2 Evaluation Under Historical Annual Landings and Survey Initializations

Replacing the three-step coarse catch regime with explicit, reconstructed historical landings (Schijns et al., 2021) does not resolve the structural failure of the surplus-production models (Table 5).

#### Table 5. Rolling-origin RMSE (kt) under reconstructed annual landings.
| Forecast Model | Horizon $h=1$ (kt) | Horizon $h=5$ (kt) |
| :--- | :---: | :---: |
| **persist** | **98** | **265** |
| **M1** | 121 | 289 |
| **M1b** | 115 | 289 |
| **M2** | 160 | 394 |
| **M3** | 154 | 352 |
| **M4** | 206 | 486 |
| **M2 (Survey Initialized, $\hat{q} I_t$)** | 128 | 331 |

Incorporating annual landings degrades the one-year forecast skill of M2, increasing RMSE from $144\text{ kt}$ to $160\text{ kt}$. On the fixed recovery window, M3 and M4 exhibit catastrophic error inflation under annual landings, rising from $220\text{ kt}$ and $214\text{ kt}$ to $609\text{ kt}$ and $586\text{ kt}$, respectively. 

The underlying cause of this failure is visible in the apparent net surplus production:
$$P_t = S_{t+1} - S_t + C_t$$
During 1991–1993, apparent net production drops to deeply negative values ($-400\text{ to } -600\text{ kt}\cdot\text{yr}^{-1}$) even after accounting for reconstructed catches. Inverting the Schaefer model at the collapse-window capacity ($\hat{K} = 1032.7\text{ kt}$) to back-calculate implied productivity:
$$\hat{r}_t = \frac{P_t}{S_t (1 - S_t / K)}$$
reveals a complete sign reversal. Mean implied productivity reads $\hat{r} = +1.82$ over 1983–1990, plunges to an average of $-0.79$ across 1991–1994 (with every single year negative), and rebounds to $+0.37$ over 1995–2007. Because an autonomous scalar map assumes stationary non-negative parameters ($r > 0$), it cannot generate negative net production in the absence of catastrophic harvest. 

Initializing forecasts using scaled research survey indices ($\hat{q} I_t$) lowers one-year RMSE for M2 from $160\text{ kt}$ to $128\text{ kt}$, but this remains far inferior to naive persistence ($98\text{ kt}$).

---

### 3.3 Evaluation on the Extended Assessment Series (xteNCAM, 1954–2024)

Specification B provides a long-term evaluation window covering seven decades of industrial exploitation, severe depletion, and modern stalled recovery under a revised reference threshold ($\mathrm{LRP} = 276\text{ kt}$).

![The two specifications. Overlap 1983–2015 RMSE = 126 kt (2015: NCAM 299 kt, xteNCAM 273 kt). Different safe sets. Not pooled.](figs/fig5_xtencam.png)

#### Table 6. Rolling-origin forecast RMSE (kt) on Specification B.
*Note: Baselines are evaluated on matched origins ($n=59$ at $h=1$; $n=55$ at $h=5$). Unmatched baseline scores across longer historical spans ($n=63/59$) read $88\text{ kt}$ and $318\text{ kt}$ for persistence, and $449\text{ kt}$ and $506\text{ kt}$ for historical mean.*
| Forecast Model | Horizon $h=1$ (kt) | Horizon $h=5$ (kt) |
| :--- | :---: | :---: |
| **persist (Matched Baseline)** | **84** | **300** |
| **M1** | 120 | 432 |
| **M1b** | 152 | 446 |
| **M2** | 166 | 1059 |
| **M3** | 127 | 930 |
| **M4** | 206 | 1031 |
| **mean (Matched Baseline)** | 458 | 522 |

The extended series reaffirms the primary findings (Table 6). Across 59 rolling origins, persistence maintains a substantial advantage at both horizons ($84\text{ kt}$ at $h=1$; $300\text{ kt}$ at $h=5$). The dynamic stock-flow formulation (M2) exhibits severe error propagation over multi-step horizons, generating an RMSE of $1059\text{ kt}$ at $h=5$. Residual tracking (M3) mitigates this divergence ($930\text{ kt}$), but remains over three times more erroneous than naive persistence. Consequently, no structural module is retained under Specification B.

On the secondary Brier diagnostic evaluated against the revised $\mathrm{LRP} = 276\text{ kt}$, persistence incurs misclassification rates of $4/59 = 0.07$ at $h=1$ and $16/55 = 0.29$ at $h=5$. While M1 and M3 achieve minor improvements in one-step status classification ($0.05$ and $0.02$, respectively), all structural models deteriorate relative to persistence at $h=5$ ($0.31\text{--}0.47$).

---

### 3.4 Trophic and Environmental Couplings

Incorporating capelin availability into the surplus-production function fails to improve forecast accuracy across either specification (Tables 7 and 8).

#### Table 7. Rolling-origin RMSE (kt) for the two-regime productivity model (M_cap).
*Note: Baselines are origin-matched ($n=25/21$ for Spec A; $n=59/55$ for Spec B).*
| Specification | Forecast Model | Horizon $h=1$ (kt) | Horizon $h=5$ (kt) |
| :--- | :--- | :---: | :---: |
| **Specification A** | **persist** | **98** | **265** |
| | M_cap | 154 | 334 |
| **Specification B** | **persist** | **84** | **300** |
| | M_cap | 147 | 894 |

#### Table 8. Rolling-origin RMSE (kt) scaling surplus production via Division 3L acoustic index.
| Specification | Forecast Model | Horizon $h=1$ (kt) | Horizon $h=5$ (kt) | Scored Origins ($n$) |
| :--- | :--- | :---: | :---: | :---: |
| **Specification A** | persist (Unmatched) | 98 | 265 | 25 / 21 |
| | **persist (Matched Origins)** | **97** | **193** | 24 / 20 |
| | M_cap_index | 150 | 262 | 24 / 20 |
| **Specification B** | persist (Unmatched) | 88 | 318 | 63 / 59 |
| | **persist (Matched Origins)** | **79** | **288** | 36 / 32 |
| | M_cap_index | 132 | 492 | 36 / 32 |

Scaling surplus production by the continuous acoustic index (M_cap_index) increases one-year RMSE to $150\text{ kt}$ on Specification A and $132\text{ kt}$ on Specification B, compared to matched persistence baselines of $97\text{ kt}$ and $79\text{ kt}$, respectively. At $h=5$ on Specification A, the apparent parity between the index module ($262\text{ kt}$) and the unmatched persistence baseline ($265\text{ kt}$) is entirely an artifact of origin sampling; recomputing persistence on the module's exact origins yields an RMSE of $193\text{ kt}$. 

The structural failure of contemporaneous prey scaling stems from demographic timing. In Northern cod, age-at-50%-maturity spans ages 5 to 6 (Cadigan, 2016). Fluctuations in capelin abundance primarily influence gadoid condition, gonad development, and early-life survival. Any trophic signal propagating via recruitment requires approximately half a decade to manifest in spawning biomass. Multiplying contemporaneous surplus production by an instantaneous prey scalar introduces high-frequency noise into the biomass update without capturing the necessary multi-year distributed biological lag.

---

### 3.5 Statistical Uncertainty Across Retention Margins

To evaluate whether the empirical performance deficits of the structural models reflect genuine predictive differences or sampling variability, we estimate Diebold–Mariano loss-differential test statistics ($z$) alongside moving-block bootstrap confidence intervals (20,000 replications; block length $L = \max(h, 3)$; Table 9).

#### Table 9. Statistical evaluation of retention margins under Diebold–Mariano and moving-block bootstrap tests.
*Note: Gaps represent $\mathrm{RMSE}_{\mathrm{module}} - \mathrm{RMSE}_{\mathrm{comparator}}$ ($\text{kt}$). Positive values indicate that the candidate module performs worse than its comparator. The bootstrap $p$-value represents the percentile-tail fraction relative to zero.*
| Spec | $h$ | Candidate Module | Comparator | Scored Pairs ($n$) | Module RMSE | Comp. RMSE | Gap (kt) | DM Stat ($z$) | 95% Bootstrap CI (kt) | Bootstrap $p$ |
| :---: | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **A** | 1 | M1 | persist | 25 | 120.5 | 98.0 | +22.5 | 1.13 | [$-$13.4, +52.2] | 0.192 |
| **A** | 1 | M1b | persist | 25 | 114.8 | 98.0 | +16.8 | 0.98 | [$-$19.4, +59.6] | 0.384 |
| **A** | 1 | M2 | persist | 25 | 144.1 | 98.0 | +46.0 | 1.29 | [$-$12.3, +83.0] | 0.452 |
| **A** | 1 | M3 | persist | 25 | 134.6 | 98.0 | +36.6 | 0.99 | [$-$16.8, +64.2] | 0.932 |
| **A** | 1 | M4 | persist | 25 | 195.6 | 98.0 | +97.5 | 1.53 | [$-$9.1, +172.7] | 0.278 |
| **A** | 1 | M2 | M1 | 25 | 144.1 | 120.5 | +23.5 | 0.91 | [$-$60.7, +66.9] | 0.684 |
| **A** | 1 | M4 | M3 | 25 | 195.6 | 134.6 | +60.9 | 1.21 | [+4.4, +134.4] | <0.001 |
| **A** | 5 | M1 | persist | 21 | 288.7 | 264.7 | +24.0 | 1.84 | [$-$43.1, +56.4] | 0.279 |
| **A** | 5 | M1b | persist | 21 | 288.6 | 264.7 | +23.9 | 1.84 | [$-$43.1, +56.4] | 0.284 |
| **A** | 5 | M2 | persist | 21 | 398.2 | 264.7 | +133.5 | 1.10 | [$-$21.0, +217.5] | 0.421 |
| **A** | 5 | M3 | persist | 21 | 366.4 | 264.7 | +101.6 | 1.12 | [$-$0.8, +151.4] | 0.078 |
| **A** | 5 | M4 | persist | 21 | 488.2 | 264.7 | +223.5 | 1.14 | [$-$20.8, +409.4] | 0.405 |
| **A** | 5 | M2 | M1 | 21 | 398.2 | 288.7 | +109.5 | 0.98 | [$-$77.1, +232.8] | 0.805 |
| **A** | 5 | M4 | M3 | 21 | 488.2 | 366.4 | +121.9 | 1.15 | [$-$27.4, +263.2] | 0.707 |
| **B** | 1 | M1 | persist | 59 | 119.5 | 84.4 | +35.0 | 2.81 | [+2.7, +70.8] | 0.032 |
| **B** | 1 | M1b | persist | 59 | 151.6 | 84.4 | +67.2 | 3.60 | [+18.3, +117.7] | 0.009 |
| **B** | 1 | M2 | persist | 59 | 166.0 | 84.4 | +81.6 | 3.22 | [+36.4, +122.8] | <0.001 |
| **B** | 1 | M3 | persist | 59 | 126.7 | 84.4 | +42.3 | 1.85 | [+1.0, +92.5] | 0.042 |
| **B** | 1 | M4 | persist | 59 | 205.7 | 84.4 | +121.3 | 3.20 | [+53.7, +193.0] | <0.001 |
| **B** | 1 | M2 | M1 | 59 | 166.0 | 119.5 | +46.6 | 1.78 | [$-$20.5, +104.5] | 0.170 |
| **B** | 1 | M4 | M3 | 59 | 205.7 | 126.7 | +79.0 | 3.07 | [+35.6, +116.4] | <0.001 |
| **B** | 5 | M1 | persist | 55 | 431.9 | 300.0 | +131.9 | 2.06 | [+33.2, +218.6] | 0.008 |
| **B** | 5 | M1b | persist | 55 | 445.5 | 300.0 | +145.5 | 1.80 | [+18.2, +250.9] | 0.023 |
| **B** | 5 | M2 | persist | 55 | 1058.9 | 300.0 | +758.9 | 2.15 | [+363.6, +1038.5] | <0.001 |
| **B** | 5 | M3 | persist | 55 | 930.1 | 300.0 | +630.2 | 2.39 | [+352.8, +845.6] | <0.001 |
| **B** | 5 | M4 | persist | 55 | 1030.7 | 300.0 | +730.8 | 2.35 | [+407.3, +978.3] | <0.001 |
| **B** | 5 | M2 | M1 | 55 | 1058.9 | 431.9 | +627.0 | 1.97 | [+195.7, +929.7] | 0.004 |
| **B** | 5 | M4 | M3 | 55 | 1030.7 | 930.1 | +100.6 | 1.88 | [+20.2, +177.4] | 0.007 |

The uncertainty analysis reveals a clear distinction between the two assessment series. On Specification A, every candidate comparison against persistence includes zero within its 95% bootstrap confidence interval. The large error spikes incurred during the single historical collapse event inflate the resampling variance over a sample size of $n = 21\text{--}25$. Consequently, non-retention on Specification A represents a point-rule ranking deficit within observational noise: the sample size is insufficient to statistically reject the null hypothesis of equal predictive ability, even though persistence consistently posts lower mean point errors.

On Specification B ($n = 55\text{--}59$), the performance deficit of the structural modules is statistically unambiguous. Every structural module performs significantly worse than naive persistence, with 95% bootstrap confidence intervals strictly excluding zero across both horizons ($p < 0.05$ across all tests). Furthermore, the structural penalty of lagged initialization (M4 vs. M3) is statistically significant across both specifications at $h=1$ ($p < 0.001$), confirming that stale starting states severely impair forecast skill.

#### Temporal Disaggregation of Performance
Partitioning the rolling origins of Specification B across distinct historical eras illuminates the structure of the pooled scores:
* **Pre-Collapse Era (Origins $\le 1990$, $n=26$):** Persistence achieves an RMSE of $94.7\text{ kt}$ compared to $142.4\text{ kt}$ for M1.
* **Active Collapse Phase (Origins 1991–1995, $n=5$):** Persistence deteriorates sharply to an RMSE of $167.0\text{ kt}$, whereas M1 achieves $126.8\text{ kt}$ and M1b achieves $66.6\text{ kt}$.
* **Post-Collapse Moratorium (Origins 1996–2012, $n=17$):** Persistence achieves an RMSE of $20.7\text{ kt}$ compared to $19.7\text{ kt}$ for M3.
* **Modern Stalled Rebuilding (Origins 2013–2023, $n=11$):** Persistence achieves an RMSE of $61.0\text{ kt}$ compared to $96.4\text{ kt}$ for M3.

This temporal breakdown demonstrates that the overall superiority of naive persistence is driven by its strong performance during prolonged periods of low or gradual biomass change (1996–2012 and pre-1990). During the acute collapse phase, structural models fit to immediate one-step updates adapt more rapidly than a pure persistence rule. However, because the collapse spans only five annual transitions, these gains are insufficient to overturn the pooled multi-decade ranking, and the post-collapse margin ($20.7\text{ kt}$ vs. $19.7\text{ kt}$) falls squarely within the non-deciding 5% tie band.

---

### 3.6 Parameter Identifiability and Objective Geometries

To evaluate the mathematical behavior of the fitted models, Table 10 consolidates all parameter estimates, optimization bounds, and boundary diagnostics.

#### Table 10. Summary of fitted parameter values, boundary constraints, and identifiability diagnostics.
| Module ID | Analysis Window / Specification | Fitted Parameters | Optimization Bounds & Diagnostic Status |
| :--- | :--- | :--- | :--- |
| **M1** | Collapse, Spec A (Train 1983–1990) | $\hat{r} = 1.935$, $\hat{K} = 1032.7\text{ kt}$, $\bar{C} = 240\text{ kt}$ | Unstable upper attractor; $\hat{r}$ approaches bound ($r \le 2.0$) |
| **M1** | Recovery, Coarse Catch (Train 1995–2007) | $\hat{r} = 0.458$, $\hat{K} = 500.0\text{ kt}$, $\bar{C} = 5.0\text{ kt}$ | $\hat{K}$ rests at multi-start value ($500\text{ kt}$); objective completely flat |
| **M1** | Recovery, Annual Catch (Train 1995–2007) | $\hat{r} = 0.370$, $\hat{K} = 5000.0\text{ kt}$, $\bar{C} = 3.19\text{ kt}$ | $\hat{K}$ hits upper bound ($5000\text{ kt}$); parameter compensation |
| **M1b** | Recovery, Coarse Catch (Train 1995–2007) | $\hat{\mathfrak{s}} = 2.1 \times 10^{-23}\text{ kt}$, $\hat{r} = 2.000$, $\hat{K} = 105.8\text{ kt}$ | $\hat{\mathfrak{s}}$ at lower boundary; $\hat{r}$ at upper bound; polynomial collapse |
| **M1b** | Recovery, Annual Catch (Train 1995–2007) | $\hat{\mathfrak{s}} = 9.4 \times 10^{-6}\text{ kt}$, $\hat{r} = 2.000$, $\hat{K} = 129.8\text{ kt}$ | Boundary collapse; parameter non-identifiability |
| **M1b** | Recovery-Stall, Spec B (Train 1995–2012) | $\hat{\mathfrak{s}} = 5.3 \times 10^{-3}\text{ kt}$, $\hat{K} = 500.0\text{ kt}$ | Extrapolation artifact; $\hat{K}$ rests far outside training range |
| **M3** | Rolling Primary Pass, Spec A | $\hat{\phi} = 0.95$ | Autoregressive parameter hits ceiling; persists negative residual |
| **M_cap_index** | Trophic Coupling (All Windows) | $\hat{r}, \hat{K}, \hat{b}$ estimated jointly | Parameter starvation; degrees of freedom exhausted at $n=6\text{--}8$ |
| **M1** | Flat-Valley Sweep (Train 1995–2007) | $K \in [60, 5000]\text{ kt}$, $r \in [0.435, 0.773]$ | Objective shift $< 0.95\text{ kt}$ RMSE; pair $(r, K)$ unidentifiable |

During the 1995–2007 recovery window, the least-squares objective surface exhibits an extensive flat valley. Fixing $K$ at arbitrary values between $60\text{ kt}$ and $5000\text{ kt}$ while re-optimizing $r$ shifts the training RMSE across an extremely narrow band of $11.29\text{ to } 12.24\text{ kt}$ (a spread of less than $0.95\text{ kt}$), while $\hat{r}$ compensates across $[0.435, 0.773]$. Despite this near-identical fit to historical transitions, the corresponding maximum sustainable yield equivalents ($rK/4$) diverge by nearly two orders of magnitude ($57\text{ kt}$ vs. $463\text{ kt}$). 

Under these conditions, candidate selection among structural parameterizations reflects arbitrary optimizer termination along a flat ridge rather than genuine biological identification.

---

### 3.7 Operating Characteristics of the Retention Rule Under Known Ground Truth

Because the empirical evaluation yields a negative result, the validity of the conclusion depends on the statistical power and specificity of the retention rule itself. We examine these properties using a pre-registered simulation experiment across five data-generating processes (D1–D5), parameterized from the empirical fits in Section 3.6, evaluated across 200 Monte Carlo replicates under two process noise regimes ($\sigma \in \{11.8, 33.8\}\text{ kt}$; Table 11).

#### Table 11. Statistical power and specificity of the retention rule under simulated ground truth.
*Note: Processes D1–D4 evaluate statistical power (retaining the true generating module). Process D5 evaluates specificity (the proportion of replicates correctly rejecting all structural modules under a persistence-true null). Structural false-positive rate across D1–D4 is 0.044.*
| Data-Generating Process | True Module | Power ($\sigma = 11.8\text{ kt}$) | Power ($\sigma = 33.8\text{ kt}$) | Performance Status |
| :--- | :--- | :---: | :---: | :---: |
| **D1: Autonomous Schaefer (Collapse Fit)** | M1 | 0.965 | 0.985 | Fully Adequate ($\text{Power} \ge 0.80$) |
| **D2: Autonomous Schaefer (Recovery Fit)** | M1 | 0.710 | 0.130 | Severely Degraded by Noise |
| **D3: Dynamic Stock-Flow (Coarse Catch)** | M2 | 0.090 | 0.110 | Structurally Deficient ($\text{Power} < 0.15$) |
| **D4: Depensatory Map ($\mathfrak{s} = 15\text{ kt}$)** | M1b | 0.005 | 0.015 | Complete Identification Failure |
| **D5: Pure Persistence Null Process** | None | 0.985 | 0.970 | Highly Specific ($\text{Specificity} \ge 0.90$) |

![Operating characteristics of the retention rule. Cells give the proportion of replicates in which the generating module was retained (D1–D4) or in which no structural module was retained under a persistence-true process (D5), against the thresholds fixed before execution: a tick marks power at or above 0.80 and specificity at or above 0.90, a cross marks power below 0.30. Power is adequate only where the generating signal is strong (D1); the rule is specific throughout.](figs/fig6_power.png)

The simulation yields three fundamental insights:
1. **High In-Class Specificity:** When data are generated by a random-walk null process (D5), the rule correctly rejects structural elaboration in $97\text{--}99\%$ of replicates. Empirical non-retention is not an artifact of an overly permissive test that defaults to complexity.
2. **Asymmetric Detection Power:** Under pre-collapse conditions (D1: high biomass, large removals, strong contrast), the rule successfully recovers the true autonomous module in $97\text{--}99\%$ of replicates. The empirical non-retention of M1 on the historical collapse window is therefore a strong result: had Northern cod dynamics obeyed an autonomous Schaefer map during 1983–1995, the rule detected it in $97\text{--}99\%$ of replicates.
3. **Severe Power Deficits for Complex Modules:** For the stock-flow (D3) and depensation (D4) processes, statistical power falls below $11\%$ and $2\%$, respectively. The bottleneck lies in mathematical parameter identification rather than the stringency of the multi-horizon retention gates. Even if one eliminates the comparator gate and the 5% tie band—requiring only that the true module beat persistence on one-year RMSE—the true module is selected in only $33\%$ of D3 and $18\%$ of D4 replicates. When five models compete, pure chance assigns the lowest error to a model $20\%$ of the time; on process D3, the true model ranks first in only $3.8\%$ of replicates. Consequently, empirical non-retention of M1b, M2, and M3 provides little evidence against the presence of these mechanisms.
4. **Over-Retention Under Out-of-Class Processes:** When simulating dynamics outside the discrete surplus-production family (e.g., gradual trends in carrying capacity or observation noise), the rule retains a structural module in $68\text{--}98\%$ of replicates, almost always selecting the autonomous map M1. Thus, high specificity is strictly conditional on the true process belonging to the evaluated model family.

#### Comparative Evaluation of Alternative Decision Rules
Averaging performance across all synthetic trials allows comparison of the adopted rule against standard model selection frameworks (Table 12).

#### Table 12. Cross-rule comparison of mean statistical power and specificity across synthetic data.
| Decision Rule Formulation | Mean Power (D1–D4) | Mean Specificity (D5) |
| :--- | :---: | :---: |
| **Adopted Rule (H1–H3, 5% Tie Band, $h=1, 5$)** | **0.376** | **0.978** |
| Without Comparator Gate (H2, H3 only) | 0.476 | 0.972 |
| Persistence Benchmark Only ($h=1$, 5% Tie Band) | 0.562 | 0.955 |
| Persistence Benchmark Only ($h=1$, Any Margin) | 0.542 | 0.765 |
| Full Rule Without 5% Tie Band ($\delta = 0$) | 0.436 | 0.772 |
| Full Rule With Expanded 10% Tie Band ($\delta = 0.10$) | 0.337 | 0.998 |
| Standard MASE Criterion ($\mathrm{MASE} < 1$) | 0.651 | 0.675 |
| Information Criterion ($n\log\mathrm{MSE} + 2k$) | 0.509 | 0.992 |

Standard scaled-error metrics ($\mathrm{MASE} < 1$) yield higher nominal power ($0.651$), but incur an unacceptable degradation in specificity ($0.675$), retaining spurious structure in nearly one-third of null trials. Conversely, an explicit information criterion penalizing free parameters ($n\log\mathrm{MSE} + 2k$) outperforms the multi-horizon RMSE rule across both dimensions, achieving a power of $0.509$ and a specificity of $0.992$. 

Within the adopted rule, the 5% tie band provides substantial protection against noise: eliminating it increases power by only $0.060$ while degrading specificity by $0.206$.

These comparative readings carry the general point for any forecast-retention exercise: a selection rule is an instrument with operating characteristics, and a non-retention verdict is only as informative as the power of that instrument under the dynamic regime in question.

---

### 3.8 Monitoring-Series Target: Autumn Survey Index

The retained-set verdict does not depend on the reconstruction as target. The autumn research-vessel trawl survey abundance index (1983–2015, 33 consecutive years; Schijns et al., 2021, Table 3, citing DFO), the rawest long monitoring series of this stock, feeds the same frozen ladder through the same engine, in kt-equivalents via a deterministic, declared unit-reconciliation constant $q^{\#} = \operatorname{median}_{1983..2015}(\mathrm{SSB}_t / I_t) = 5.70 \times 10^{-4}$ kt per index unit, computed once from the full overlapping sample (the Spec A series, DFO 2016, Table A2; the index, Schijns et al., 2021, Table 3) and never refitted per forecast origin. The constant fixes reportable units and enters no retention decision: re-scoring the entire ladder under the interquartile bounds of $\mathrm{SSB}_t/I_t$ ($q$ at p25/p50/p75) leaves every retention verdict — and the empty retained set — identical; the closest structural deficit moves within 22.6–32.8% at $h=1$ and 27.8–46.8% at $h=5$ only because optimizer bounds track the rescaled state (SI-7). The information set assigns the index value for year $t$ as available at origin $t$; the survey series carries no normative threshold, so the secondary Brier readings are undefined for this object and RMSE governs. Origins match Specification A exactly ($n = 25$ at $h=1$, $n = 21$ at $h=5$), and persistence is recomputed origin-matched.

#### Table 12b. Rolling-origin RMSE (kt-equivalents) on the autumn survey index, annual-catch treatment; origin-matched against Specification A readings.
| Model | Survey $h=1$ | Survey $h=5$ | Spec A recon., annual $h=1$ | Spec A annual $h=5$ |
| :--- | :---: | :---: | :---: | :---: |
| naive persist | **120.5** | **249.2** | **98.0** | **264.7** |
| naive train mean | 482.4 | 553.0 | 423.6 | 507.4 |
| M1 | 184.2 | 386.6 | 120.5 | 288.7 |
| M1b | 156.3 | 355.5 | 114.8 | 288.6 |
| M2 | 224.9 | 671.4 | 160.4 | 393.8 |
| M3 | 290.3 | 716.7 | 153.6 | 351.5 |
| M4 | 371.3 | 880.5 | 206.3 | 486.4 |

The closest structural deficit against persistence is +29.8% at one year (M1b) and +42.7% at five years (M1b) — against +17.1% and +9.0% on the reconstruction. Every structural deficit relative to persistence separates from zero under the post-freeze uncertainty layer (DM with Newey–West HAC, moving-block bootstrap, 20,000 replications, seed 0) with the single exception of the stock-flow module at $h=1$, whose positive gap (+87% by RMSE) carries a bootstrap interval that crosses zero at $p = 0.062$ — the sign verdict is a deficit either way. Under the coarse catch regime the same ordering holds (ladder 156.7–357.1 kt-equivalents at $h=1$ under the coarse regime, against persistence 120.5; 355.5–913.5 at $h=5$ against 249.2). No module passes H1 or H2 at either horizon; as on the reconstruction, the retained set is empty.

#### Fixed windows on the index.
The fixed-window readings mirror the reconstruction's ordering exactly. On the collapse window (train 1983–1990, score 1991–1995) every structural fit fails outright (RMSE 1,102–1,274 kt-equivalents against 791.6 for persistence and 863.8 for the training mean): the index loses a factor of 4.7 between 1991 and 1992 alone and falls to less than one percent of its 1986 peak by 1994—dynamics no fitted one-pool map can anticipate. On the recovery window (train 1995–2007, score 2008–2015) the fitted maps track the trend regrowth with RMSE 41.9–50.2 (annual-landings treatment; 33.1–93.2 under the coarse regime) for every module except the Allee variant, which records 120.1 against 109.4 for persistence under the annual treatment and 93.2 under the coarse regime — the same orientation observed on the reconstruction (55.3–56.2 vs 103.8), where multi-step trajectory skill is real in the recovery era but does not survive the rolling-origin protocol that includes the collapse regime.

#### What the contrast certifies.
Assessment smoothing was a candidate mechanical explanation for the persistence advantage: a smoothed reconstruction injects autocorrelation that favours the no-change rule (reproduced by the smoother re-runs in the simulation layer archived with this study). The monitoring series carries no such smoothing, and the persistence advantage *increases* there (+29.8% at $h=1$ versus +17.1% on the reconstruction at matching origins). The negative result therefore does not depend on target construction: neither a reconstructed nor a monitoring target retains any module of the frozen ladder. The contrast illustrates a general robustness discipline: conclusions drawn on smoothed reconstruction targets should be re-scored on the rawest available monitoring series before they are read as properties of the forecast system rather than of target construction.

## 4. Discussion

### 4.1 Structural Obstructions in Scalar Surplus-Production Dynamics

The complete failure of the autonomous surplus-production models to anticipate or capture the 1991–1995 collapse reflects an underlying mathematical limitation of one-dimensional dynamical systems.

#### Proposition 4.1 (Dynamical Barrier to Recovery Under Constant Catch)
Let $S_{t+1} = F(S_t)$ be an autonomous, discrete-time scalar mapping:
$$F(S_t) = \Big[ S_t + r S_t \left(1 - \frac{S_t}{K}\right) - C \Big]_+$$
operating under constant removals $C > 0$. Assume $F$ possesses two positive fixed points, $S_- < S_+$, representing an unstable lower repeller and a stable upper attractor, and is monotonically increasing on $[0, S_{\max}]$. 

If an observed stock trajectory $(S_t)$ falls strictly below the lower equilibrium $S_-$ at some time $t^*$, and subsequently recovers such that $S_{t+k} > S_-$ for $k > 0$, no deterministic trajectory of $F(S_t)$ can reproduce this sequence.

*Proof.* For all states $S \in [0, S_-)$, we have $F(S) < S$ by definition of the unstable repeller. Because $F$ is continuous and strictly increasing on $[0, S_-]$ with boundary condition $F(0) = 0$ (enforced by non-negative clipping), the open interval $[0, S_-)$ forms a forward-invariant set:
$$\forall S \in [0, S_-), \quad F(S) \in [0, S_-)$$
Iterating forward from any state $S_{t^*} < S_-$, the sequence $\{S_{t^*+k}\}_{k=0}^\infty$ is strictly monotonically decreasing toward zero. The trajectory cannot cross the repelling boundary $S_-$ from below. Hence, an observed trajectory that enters $[0, S_-)$ and subsequently rises above $S_-$ cannot be generated by any deterministic realization of $F$. $\blacksquare$

![Apparent net production (P_t = S_t+1](figs/fig4_production.png)

The empirical NCAM reconstruction satisfies the conditions of Proposition 4.1: during the 1991–1995 collapse, estimated SSB plunged to $9.7\text{ kt}$, far below the fitted lower repeller of $S_- = 144\text{ kt}$ generated by the pre-collapse harvest regime ($C = 240\text{ kt}$). 

Critically, this lower repeller is an artifact of the harvest rate, not biological depensation. For the standard logistic surplus function, the equilibria under constant harvest $C$ are:
$$S_\pm(C) = \frac{K}{2} \left[ 1 \pm \sqrt{1 - \frac{4C}{rK}} \right]$$
The lower threshold $S_-(C)$ represents the unstable boundary where harvest exceeds surplus production. As catches decline toward zero, this repeller collapses to zero: under a moratorium catch of $C = 5\text{ kt}$, the repeller drops to $S_- = 2.6\text{ kt}$. 

The failure of the forecasting models during the collapse does not stem primarily from this mathematical trapping, but from the interaction between stationary biology and declining catch. In modules M2, M3, and M4, the realized catch sequence is provided exogenously. When management enforced the commercial moratorium in July 1992, recorded catches fell from over $200\text{ kt}$ to nominal levels. Because the surplus-production function is parameterized with stationary, positive productivity ($\hat{r} = 1.935$), the dynamic update:
$$S_{t+1} = S_t + g(S_t) - C_t$$
sees removals vanish while stock biomass remains high enough to generate positive surplus. The model mechanically projects an immediate, explosive biomass rebound at the exact historical moment the stock was collapsing. 

This diagnosis explains why supplying the realized catch series in M2 inflates forecast error relative to the autonomous map M1 ($819\text{ kt}$ vs. $694\text{ kt}$). Within a stationary surplus-production framework, a collapse cannot be driven by a catch series that drops faster than the stock.

---

### 4.2 Decomposing the Error Penalty of Assessment Latency

Module M4, which initiates forward projections from a lagged assessment state $S_{t-1}$, exhibits the highest forecast errors among all structural candidates ($196\text{ kt}$ at $h=1$; $488\text{ kt}$ at $h=5$ on Specification A). In operational management, scientific advice is frequently formulated using assessments lagged by one or more years due to data collation and survey processing schedules.

To separate the error penalty attributable to *stale starting information* from the structural error of the *surplus-production model itself*, we formulate a lagged naive baseline:
$$\hat{S}_{t+h \mid t}^{\mathrm{lag}} = S_{t-1}$$
Evaluating this control across identical rolling origins decomposes the performance deficit into two components (Table 13).

#### Table 13. Decomposition of forecast error for lagged initialization (M4).
*Note: Evaluated across matched origin sets ($n=25/21$ for Spec A; $n=59/55$ for Spec B).*
| Horizon & Specification | Total Error Deficit (M4 vs. Timely Persist) | Information Latency Component (Lagged Persist vs. Timely Persist) | Structural Surplus Penalty (M4 vs. Lagged Persist) |
| :--- | :---: | :---: | :---: |
| **Spec A, $h=1$** | $+97.5\text{ kt}$ ($195.6 - 98.0$) | **$+86.4\text{ kt}$ ($184.4 - 98.0$)** | $+11.1\text{ kt}$ ($195.6 - 184.4$) |
| **Spec A, $h=5$** | $+223.5\text{ kt}$ ($488.2 - 264.7$) | $+65.1\text{ kt}$ ($329.8 - 264.7$) | Not reported: component derived across mismatched origin sets ($488.2$ kt and $329.8$ kt appear at different effective $n$) |
| **Spec B, $h=1$** | $+121.3\text{ kt}$ ($205.7 - 84.4$) | **$+73.6\text{ kt}$ ($158.0 - 84.4$)** | $+47.7\text{ kt}$ ($205.7 - 158.0$) |
| **Spec B, $h=5$** | $+730.8\text{ kt}$ ($1030.7 - 300.0$) | $+37.4\text{ kt}$ ($337.4 - 300.0$) | **$+693.3\text{ kt}$ ($1030.7 - 337.4$)** |

This decomposition highlights an operational trade-off across forecast horizons:
* **Short Horizons ($h=1$):** The error deficit is dominated by stale information. The one-year information lag accounts for $88.6\%$ ($86.4\text{ kt}$ of $97.5\text{ kt}$) of the total error on Specification A and $60.7\%$ on Specification B. At this horizon, updating the starting state from $S_{t-1}$ to $S_t$ yields far larger error reductions than refining the surplus-production function.
* **Multi-Step Horizons ($h=5$):** Structural error dominates. The accumulation of model misspecification over five iterative steps is reported without percentage shares on both specifications (the frozen decomposition magnitudes are given in Table 13). At longer horizons, initial condition errors are rapidly eclipsed by structural divergence.

---

### 4.3 Target Smoothing and the Competitiveness of Persistence

The strong performance of last-value persistence must be interpreted in light of the predictand's properties. In this evaluation, the target variable is not raw survey catch-per-unit-effort, but spawning stock biomass derived from integrated state-space assessment models (NCAM and xteNCAM). 

State-space assessment models filter raw observational noise through age-structured cohort equations, natural mortality priors, and survey selectivity ogives. Spawning biomass in a long-lived, late-maturing gadoid represents the sum of surviving mature age classes. Consequently, the true biomass trajectory exhibits high temporal autocorrelation, which the statistical smoother amplifies. Under these conditions, last-value persistence provides a demanding benchmark. 

Outperforming persistence requires a model to accurately predict *second-order changes*—the sign and magnitude of the trajectory's curvature ($\Delta^2 S_t$). During prolonged periods of low biomass and low fishing mortality (e.g., 1996–2012), biomass increments are small relative to the total stock size, and persistence incurs minimal error. 

Structural models can outperform persistence only when dynamic departures are large and persistent. Yet, during the one period where such departures occurred—the 1991–1995 collapse—the surplus-production models predicted strong biomass growth due to catch reductions. Failing during directional transitions while adding parameter variance during quiescent periods ensures that structural modules cannot beat persistence when pooled across decades.

That mechanism-level reading must be scoped precisely, because two different interventions sit side by side in this work. The companion simulation varies the *smoothness of a fixed target* and finds that assessment-like smoothing amplifies persistence's advantage by injecting autocorrelation into the predictand. Section 3.8 varies the *target itself*: the autumn survey series is not a desmoothed version of the reconstruction but a separate measurement with its own observation error, catchability, and spatial coverage. The empirical contrast—the closest structural deficit growing from +17.1% to +29.8% at one year and from +9.0% to +42.7% at five years when the monitoring series replaces the reconstruction—reads as the signature of observation noise, not of lost smoothing: iterated trajectories compound measurement noise across steps, so the ladder's error grows with horizon, while persistence pays only the bounded one-step noise floor. The horizon-*widening* of the deficit on the survey index and the horizon-*narrowing* on the reconstruction are the fingerprints of the two mechanisms, and they point in opposite directions.

The two findings do not conflict; they rank mechanisms. Within a fixed assessment reconstruction, smoothing helps persistence and degrades the detection power of structure-based alternatives—the simulation result. Across measurements, substituting a raw monitoring series for the reconstruction strengthens persistence further—the empirical result of §3.8—because the ladder's iterated error accumulates an observation-noise component that persistence never compounds. Neither mechanism is required for the headline: the retained set is empty under both targets and both horizon orderings, so the inference that surplus-production structure does not help forecasts of this stock holds whether the scoreboard is a smoothed estimate of a latent state or a noisy survey realization of the stock itself.

---

### 4.4 Ecological Consistency with Independent Assessment Reconstructions

Our findings are consistent with recent independent stock assessment modeling for Northern cod. Rose (2026) evaluated two distinct assessment reconstructions spanning 1983–2023—the Rose and Walters (2019) model and the official DFO (2024a) formulation—and documented that net surplus production and stock growth stalled simultaneously after 2015, dropping into negative values in several years. 

This post-2015 stall occurred at biomass levels far below historical carrying capacity. A stock that ceases growing or contracts at low biomass in the absence of major fishing mortality violates the fundamental assumption of autonomous surplus-production models, which assume that compensatory growth is maximized at depleted stock sizes ($S < K/2$).

Rose (2026) demonstrated through structural equation modeling that the post-2015 production deficit was driven primarily by food limitation (capelin scarcity) coupled with elevated natural mortality from seal predation, concluding that fishing was not the primary driver. 

This ecological mechanism aligns with both of our main empirical findings:
1. **Inability of Catch Accounting to Resolve Dynamics:** Supplying reconstructed catches fails to improve hindcast accuracy because fishing mortality was not the primary driver of either the 1990s collapse or the post-2015 stall. Modern assessments (Regular et al., 2025) attribute the collapse primarily to an unprecedented spike in natural mortality ($M \approx 2.5$). A scalar model that accounts only for reported catch cannot capture this dynamic.
2. **Failure of Trophic Modules to Improve Forecasts:** Although capelin availability is an important driver of gadoid productivity, our trophic-coupling modules (Tables 7 and 8) failed out-of-sample. The trophic signal in Northern cod operates through maternal condition, egg viability, and subsequent recruit survival, creating a multi-year distributed lag before appearing in adult spawning biomass. Linking contemporaneous surplus production directly to an annual acoustic index adds noise to the state equation while missing the lagged recruitment dynamic.

---

### 4.5 Evaluation Limitations and Methodological Constraints

To ensure balanced interpretation, several methodological caveats must be noted:
1. **Conditional Hindcasts vs. Operational Forecasts:** Because realized catches along the projection horizon were supplied exogenously to modules M2, M3, and M4, this study represents a conditional hindcast rather than a true operational forecast. In actual management, future catches must be projected using harvest control rules. However, because these modules failed to beat persistence despite receiving future catch data, their lack of predictive skill is an even stronger result.
2. **Retrospective Vintages vs. Historical Smoothed States:** Our evaluation scored forecasts against a single, locked retrospective assessment series rather than sequential historical assessment vintages. This design isolates forecasting skill from retrospective assessment revisions, but it cannot evaluate historical advisory performance in real time.
3. **Catch Series Precision:** Reconstructed historical catches remain subject to unquantified uncertainty, particularly regarding illegal, unreported, and unregulated (IUU) fishing prior to the 1992 moratorium and discarding in the offshore fleet.
4. **Implementation Scope:** Non-retention applies specifically to the forward-ordered discrete-time scalar surplus-production implementations evaluated here under one-step least-squares estimation. It does not imply that age-structured, multi-fleet, or state-space delay-difference models cannot achieve predictive skill on this stock.

---

### 4.6 Broader Implications: A Transferable Protocol for Forecast Validation

The empirical conclusion of this study is bounded: no module in the evaluated surplus-production ladder is retained for Northern cod under the specified estimator, target, and scoring rule. The broader contribution is the evaluation design itself. Stock assessment and ecological forecasting commonly respond to diagnostic failure, expanding management questions, or biological plausibility by adding structure. As this study illustrates, improved retrospective fit and mechanistic plausibility do not by themselves confer out-of-sample forecast skill; each structural addition is usefully treated as a forecast hypothesis that must earn retention against both a simpler structural comparator and a naive baseline on the quantity used for management.

Six elements of the protocol transfer to stock-assessment and ecological-forecast validation; they instantiate the companion framework paper's minimum reporting standard (Abaee, 2026d), with fisheries-native additions distinguished below. First, the scoring target should be the quantity that enters harvest control rules and rebuilding verdicts, not only the observation indices fitted inside the assessment objective function: a model may track an index while its reconstructed absolute biomass degrades out-of-sample. Second, naive baselines such as persistence or a training mean should serve as active competitors rather than passive scaling denominators, since smoothed or autocorrelated targets can make them strong rivals. Third, structural additions should be arranged in an ordered ladder and ranked against declared simpler comparators, which is more informative than binary certification of a single integrated model. Fourth, the scoring rule, horizons, target definition, and retention criteria should be fixed before the scores are read, with information availability documented at every forecast origin. Pre-declaration protects the verdict against post hoc selection of horizons, targets, error measures, or model variants in favour of a preferred specification—the norm adopted in registered forecasting practice from meteorology and hydrology to epidemiology and machine-learning benchmarking. The instrument comparison in Section 3.7 shows the force of this requirement: a standard $\mathrm{MASE} < 1$ gate would have retained spurious structure in nearly one-third of persistence-null trials, while the declared rule rejected 97–99% of them. Fifth, retention margins should be quantified on origin-matched error with an uncertainty layer, as in the post-freeze Diebold–Mariano and bootstrap audit applied here. Sixth, the operating characteristics of the retention rule should be measured by simulation against known ground truths, so that each non-retention verdict carries a known evidential weight.

The framework disciplines both positive and negative readings of model structure. Where power is high, as it was for the autonomous module under collapse-window conditions, non-retention is strong evidence against the tested mechanism. Where power is low, as for the stock-flow and depensatory modules under depleted recovery conditions, non-retention reflects weak identifiability or data limitation rather than the absence of the mechanism; absence of retained structure is not uniformly evidence of absent structure. The collapse-window readings carry a parallel general implication: when a model class is structurally incapable of generating the event being scored, poor performance on that window measures a class-level misspecification penalty rather than comparative forecast skill among members of the class—a consideration directly relevant to regime-shift and tipping-point forecasting.

The Northern cod exercise is a conservative stress test for these points. The conditional hindcast supplies realized catches over the projection horizon to modules M2, M3, and M4, and the retrospective reconstruction isolates forecast skill from real-time vintage effects; both features favour the structural models, yet persistence wins on both reconstructions and on the raw survey index. Structural elaboration should therefore not be assumed to buy predictive skill: its value must be demonstrated on decision-relevant targets, against active naive baselines, under frozen rules, with the interpretation of any negative verdict calibrated by power. Within the six elements listed above, the naive-baseline gate, the ordered comparator ladder, the frozen rule with its information-set documentation, and the operating-characteristic calibration derive from the framework paper's standard (Abaee, 2026d); the control-rule target alignment, the event-generation reading of collapse-window scores, and the stress-test evidence of this paragraph are contributions of the present study.

---

## 5. Conclusions

Across two independent state-space assessment reconstructions of Northern cod (1954–2024), standard discrete-time surplus-production models fail to demonstrate out-of-sample forecast skill over a naive last-value persistence baseline. Across one-year and five-year forecast horizons, adding dynamic catch accounting, depensatory Allee thresholds, autoregressive residual tracking, assessment latency, and trophic scalars fails to lower pooled rolling-origin RMSE.

Simulation testing under known ground truth shows that this negative finding carries different weight across modules:
* For autonomous surplus production (M1), the retention rule exhibits a $98\%$ probability of detecting true dynamics under collapse-window conditions. The empirical failure of M1 is therefore informative: Northern cod dynamics are inconsistent with a stationary scalar surplus-production map.
* For stock-flow (M2) and depensatory (M1b) models, statistical power falls below $15\%$ under depleted recovery conditions due to likelihood flatness and parameter compensation. Here, non-retention reflects data limitations and model unidentifiability rather than proof that these mechanisms are absent.

These results indicate that in depleted, non-stationary fisheries subject to environmental shifts and changing natural mortality, structural elaboration can degrade out-of-sample predictive performance. Assessment models should routinely be scored against naive persistence benchmarks directly on derived management targets. When structural elaborations fail to outperform simple persistence out-of-sample, their parameterizations should be treated as descriptive hypotheses rather than reliable foundations for forward-looking harvest advice.

The general lesson is not that structural models are uninformative or that persistence is universally preferable; it is that the forecast value of added structure must be demonstrated rather than assumed. The protocol used here—active naive baselines, target-aligned scoring, ordered structural comparators, pre-registered rules, origin-matched uncertainty, and power calibration—is directly transferable to other stocks and to ecological forecasting problems in which added complexity is proposed as an improvement.

---


---

## Appendix A. Technical and Computational Specification

This appendix consolidates, in one location, the complete mechanical detail of fitting, projection, scoring, and uncertainty evaluation. Every statement re-describes machinery archived in the public repository; material parameter values are those registered in the main text and archived result files.

### A.1 State variable and structural map

The target state is spawning stock biomass $S_t$ (kt), NT 1983–2015 (Specification A) and 1954–2024 (Specification B). All modules share the one-step map of Definition 2.1,
$$S_{t+1} = \Big[\, S_t + g(S_t) - C_t + \varepsilon_t \,\Big]_+, \qquad g(S_t) = r\, S_t \Bigl(1 - \tfrac{S_t}{K}\Bigr)\, a(S_t),$$
with the Schaefer branch $a(S_t)=1$ and, for M1b, the depensatory branch $a(S_t)=(S_t - \mathfrak{s})/(K - \mathfrak{s})$ (continuous modulation, never a binary switch; the Schaefer model is a distinct branch, not a nested restriction since $\mathfrak{s}=0$ yields $a(S_t)=S_t/K$). $\varepsilon_t$ enters only as an equation error during estimation; projections set $\varepsilon_{t+k}=0$ (deterministic plug-in), except M3/M4 which project the residual state. A numerical floor $10^{-3}$ kt and ceiling $10^{6}$ kt bound every projection step.

### A.2 Estimation mechanics per training window

* **Loss and transitions.** One-step nonlinear least squares over the expanding window's $m-1$ transitions of an $m$-year window.
* **Bounds.** $r \in (0.001, 2.0]$; $K \in [\max_{\mathrm{train}}(S_t) + 10,\ 5000]$ kt, where $\max_{\mathrm{train}}$ reads only predictor states of the transitions (terminal state excluded); optimization initializes from a multi-start value $K = 500$ kt; the Allee threshold is constrained to $\mathfrak{s} \in [0, \max_{\mathrm{train}}(S_t)]$ with the biological-feasibility requirement $0 \le \mathfrak{s} < 0.8K$ enforced directly in the objective.
* **Catch handling.** M1/M1b close the autonomous map with the training-mean $\bar{C}$; M2–M4 receive the realized catch sequence over the projection horizon (conditional hindcast, §2.2). Specification A evaluates both the coarse recorded regime ($C_t = 240 / 120 / 5$ kt) and the reconstructed annual landings (1983–1993 byte-identical to STATLANT/Regular et al. values: 41, 11, 1.31, 0.41 kt for 1992–1995).
* **Residual autoregression.** $\hat\phi = \sum_u e_u e_{u-1} \big/ \sum_u e_{u-1}^2$ on training residuals computed prior to state clipping; $\hat\phi=0$ if the window has fewer than four transitions or a non-positive denominator; $\hat\phi$ is clipped to $[-0.95, 0.95]$; the $k$-step projected disturbance is $\hat\phi^k e_{\mathrm{last}}$, added before the floor/ceiling step.
* **Parameter-geometry anchors.** Fitted geometries are reported where interpretative weight rests on them (Section 3.6): reported fits attain $K = 5000$ kt where data prefer unbounded carrying capacity, while the depensatory fits on the coarse/annual treatments are interior at $K = 105.8/129.8$ kt.

### A.3 Origin machinery and scoring

Expanding windows with minimum sizes 8 years (Specification A) and 12 years (Specification B) generate the origin sets of Table 2c (25/21 origins on Specification A at $h=1/h=5$; 59/55 structural and 63/59 naive on Specification B). Primary score: $\mathrm{RMSE}_h = \sqrt{\frac{1}{n}\sum_i (\hat S_{t_i+h} - S_{t_i+h})^2}$ with $h=5$ read at the terminal state; secondary metrics MAE, log-RMSE on $\log\max(\hat S, 10^{-3}\text{ kt})$, the binary Brier indicator $\mathbf{1}\{\hat S_{t+h}<\mathrm{LRP}\}$, and direction hit rate (undefined for persistence, NA). Comparisons are origin-matched: the baseline is recomputed on each module's own origin set.

### A.4 Retention rule (executable form)

With $\delta = 0.05$: H1 compares module against its declared comparator (M1b→M1, M2→M1, M3→M2, M4→M3; vacuous for M1) with $\mathrm{RMSE}(M,h) < (1-\delta)\,\mathrm{RMSE}(\operatorname{comp}(M),h)$; H2 applies the same margin against per-origin persistence; H3 requires H1 and H2 simultaneously at $h=1$ and $h=5$. Non-retention yields no model; retention is a certificate, not a ranking.

### A.5 Uncertainty-audit layer

Margins are reported with Diebold–Mariano $z$-statistics (HAC lag $\max(h-1,0)$) and moving-block bootstrap intervals (block length $L = \max(h,3)$; 20,000 replications; seed 0; deterministic), in a post-freeze, read-only layer that recomputes naive baselines on each row's exact origin set and asserts them against the frozen values; archived outputs: `results/e1_dm_uncertainty.csv` and `results/e1_dm_uncertainty_regime.csv`.

### A.6 Reproducibility map

The complete computational surface—fitting drivers, specification passes, covariate modules, audit re-runs, and uncertainty campaigns, each pinned by an md5 checksum—is itemized in the Supplement (SI-6, version v3 of this supplement), with execution order and a byte-for-byte determinism guarantee in a fresh environment. Archived repository: https://github.com/MIKEAA2020/general-sustainability.

## Data and Code Availability

All evaluation data, scoring routines, and simulation protocols are open-source and archived to ensure computational reproducibility. The primary data inputs include the NCAM M-shift assessment table (DFO, 2016, Table A2), the extended xteNCAM series (Regular et al., 2025, Table 17), historical landings reconstructions (Schijns et al., 2021), the Division 3L capelin acoustic survey series (Zenodo, 10.5281/zenodo.17515115), and the autumn research-vessel survey index (Schijns et al., 2021, Table 3) scored in Section 3.8 by the deterministic `campaign_e1_survey_target.py` (outputs archived as `e1_survey_target_*.csv` and `e1_survey_dm_uncertainty.csv`). All deterministic evaluation scripts, parameter estimation routines, and Monte Carlo simulation codes are maintained in the project code repository. Earlier working versions of this study—deposited by the same author in the same repository and in record https://doi.org/10.5281/zenodo.22553609 under the working title *Does a surplus-production ladder improve forecasts of Northern cod? A scored test on NAFO 2J3KL*—are superseded by the present version. The same study circulated under the earlier title *Forecasting biomass under structural non-stationarity: an out-of-sample evaluation of surplus-production models for Northern cod (Gadus morhua)*; the present version generalizes the framing without altering any data, score, retention verdict, or reported number.

---

## References

* Abaee, A., 2026a. Does a one-pool water-balance model improve forecasts
of Edwards Aquifer head? A scored test at J-17. Zenodo.
https://doi.org/10.5281/zenodo.22552680.

* Abaee, A., 2026b. Periodic review as sampled governance: sample-and-hold
dynamics of assessment-driven effort control, a selected 42-stock
spectral screen, and the Northern Cod case. Zenodo.
https://doi.org/10.5281/zenodo.22554297.

* Abaee, A., 2026c. Robust viability of the 2J3KL limit reference point
under a surplus-production map: policy scoring, expansion, and when
catch cannot help. Zenodo. https://doi.org/10.5281/zenodo.22552060.
* Abaee, A., 2026d. When a model is not retained, what must be reported? A retention rule, an information-set audit, and operating characteristics: a minimum reporting standard worked on three scored objects in two domains. figshare. https://doi.org/10.6084/m9.figshare.33922666.

* Cadigan, N.G., 2016. A state-space stock assessment model for northern
cod, including under-reported catches and variable natural mortality
rates. Can. J. Fish. Aquat. Sci. 73, 296–308.

* Diebold, F.X., Mariano, R.S., 1995. Comparing predictive accuracy. J.
Bus. Econ. Stat. 13, 253–263.
https://doi.org/10.1080/07350015.1995.10524599

* Carvalho, F., Winker, H., Courtney, D., Kapur, M., Kell, L., Cardinale,
M., Schirripa, M., Kitakado, T., Yemane, D., Piner, K.R., Maunder, M.N.,
Taylor, I., Wetzel, C.R., Doering, K., Johnson, K.F., Methot, R.D.,
2021. A cookbook for using model diagnostics in integrated stock
assessments. Fish. Res. 240, 105959.

* DFO, 2009. A fishery decision-making framework incorporating the
Precautionary Approach. Fisheries and Oceans Canada, Ottawa.

* DFO, 2016. Stock Assessment of Northern cod (NAFO Divs. 2J3KL) in 2016.
DFO Can. Sci. Advis. Sec. Sci. Advis. Rep. 2016/026.

* DFO, 2024a. NAFO Divisions 2J3KL Northern Cod stock assessment to 2024.
DFO Can. Sci. Advis. Sec. Sci. Advis. Rep. 2024/049.

* DFO, 2024b. Assessment of capelin in NAFO Divisions 2J3KL. DFO Can. Sci.
Advis. Sec. Sci. Advis. Rep. 2024/050.

* Hutchings, J.A., Myers, R.A., 1994. What can be learned from the
collapse of a renewable resource? Atlantic cod, Gadus morhua, of
Newfoundland and Labrador. Can. J. Fish. Aquat. Sci. 51, 2126–2146.

* Hyndman, R.J., Koehler, A.B., 2006. Another look at measures of forecast
accuracy. Int. J. Forecast. 22, 679–688.

* Kell, L.T., Kimoto, A., Kitakado, T., 2016. Evaluation of the prediction
skill of stock assessment using hindcasting. Fish. Res. 183, 119–127.

* Kell, L.T., Sharma, R., Kitakado, T., Winker, H., Mosqueira, I.,
Cardinale, M., Fu, D., 2021. Validation of stock assessment methods: is
it me or my model talking? ICES J. Mar. Sci. 78, 2244–2255.

* Kokkalis, A., Berg, C.W., Kapur, M.S., Winker, H., Jacobsen, N.S.,
Taylor, M.H., Ichinokawa, M., Miyagawa, M., Medeiros-Leal, W., Nielsen,
J.R., Mildenberger, T.K., 2024. Good practices for surplus production
models. Fish. Res. 275, 107010.

* Künsch, H.R., 1989. The jackknife and the bootstrap for general
stationary observations. Ann. Stat. 17, 1217–1241.
https://doi.org/10.1214/aos/1176347265

* Murphy, H.M., Adamack, A.T., Lewis, R.S., Bourne, C.M., 2025. Assessment
of capelin in NAFO Divisions 2J+3KL to 2023. DFO Can. Sci. Advis. Sec.
Res. Doc. 2025/022.

* Northwest Atlantic Fisheries Centre, 2025. 2J3KL cod and capelin biomass
indices. Zenodo. https://doi.org/10.5281/zenodo.17515115

* Regular, P.M., et al., 2025. Assessment of the Northern Cod stock in
NAFO Divisions 2J3KL in 2024. DFO Can. Sci. Advis. Sec. Res. Doc.
2025/048.

* Rose, G.A., 2026. Northern cod comeback: 10 years after. Can. J. Fish.
Aquat. Sci. 83, 1–14. https://doi.org/10.1139/cjfas-2025-0141

* Rose, G.A., Rowe, S., 2015. Northern cod comeback. Can. J. Fish. Aquat.
Sci. 72, 1789–1798.

* Rose, G.A., Walters, C.J., 2019. The state of Canada's iconic Northern
cod: a second opinion. Fish. Res. 219, 105314.

* Schijns, R., Froese, R., Hutchings, J.A., Pauly, D., 2021. Five
centuries of cod catches in Eastern Canada. ICES J. Mar. Sci. 78,
2675–2683.

* Shelton, P.A., Healey, B.P., 1999. Should depensation be dismissed as a
possible explanation for the lack of recovery of the northern cod (Gadus
morhua) stock? Can. J. Fish. Aquat. Sci. 56, 1521–1524.

* Walters, C., Maguire, J.-J., 1996. Lessons for stock assessment from the
northern cod collapse. Rev. Fish Biol. Fish. 6, 125–137.

* *

## Declarations

### Data availability

All input data, analysis scripts, result files, and the frozen model
specification are archived at
https://github.com/MIKEAA2020/general-sustainability and
https://zenodo.org/records/22553609.

### Reproducibility

All computations are deterministic: within a fixed interpreter and
library stack, repeated executions reproduce every result file byte for
byte. An independent re-execution verified all 29 recorded output
checksums and regenerated all 30 result files byte-identically; one
registered file carries no pinned checksum and is covered by the
regeneration comparison. Across environments, the intervention runners
and the OLS-based prediction runners regenerate their outputs byte for
byte, while the four optimizer-based forecast runners (L-BFGS-B fits)
reproduce every scored row at printed precision with one exception: the
M1b rolling row on Specification B, whose Allee optimum is
environment-sensitive at the 17 kt level (h=1: 151.6
versus 153.2 kt; h=5: 445.5 versus 462.5 kt, on Python
3.12/numpy 2.1.3/scipy 1.14.1 against the recorded original
environment). That sensitivity is consistent with the identification
fragility reported for M1b in Section 3.1 ( s descending
towards zero, K resting at the 500-kt multi-start initialiser), and
it is immaterial to the retention verdict, which persistence wins at
both horizons by margins far larger than the instability. The archive
records the checksums of the original-environment outputs; the
deterministic-in-environment claim and this sensitivity note together
are the reproducibility statement.

The uncertainty layer of Section 3.5 is produced by a seeded,
deterministic script applying Diebold–Mariano (HAC) statistics and a
Künsch moving-block bootstrap to the archived per-origin forecast
files; the persistence baseline is recomputed there on the identical
origin sets from the registered series and asserted against the recorded
origin-matched values. The script and its output are archived with the
repository.

```
python3 src/run_ladder.py && python3 src/run_xte.py
python3 src/run_capelin_regime.py && python3 src/run_capelin_index.py
python3 src/compare_catch.py && python3 src/make_figures.py
```

### CRediT authorship contribution statement

A.A conceptualized the entire work, wrote, reviewed and edited the manuscript.

### Funding

No funding received.

**Declaration of competing interest**

The authors declare that they have no known competing financial
interests or personal relationships that could have appeared to
influence the work reported in this paper.

AI declaration
GLM (Z.ai), Qwen (Alibaba Cloud) and DeepSeek AI assisted with drafting and iterative review.

document

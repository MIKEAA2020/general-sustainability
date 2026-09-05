# Does a surplus-production ladder improve forecasts of Northern cod? A scored test on NAFO 2J3KL

**Prepared in the format of Fisheries Research**

*Version log (v12).* Wave-5 owner-directed re-open pass (the registered follow-ups behind the owner gate, re-evaluated). Two items re-opened because their recorded reason — new computations needing a scored campaign — is mis-stated for them; both are presentation-layer collections of values already printed. (1, claude priority 5: the parameter table) New Section 3.6 + Table 10 collect every fitted-parameter value the article prints, with its window and the bound it attains, quoting the source sections verbatim; the unprinted members (per-origin rolling fits, the index module's per-window $b$, M4's structural setting) are marked as archive items — the P5-Table-3 pattern; a Section 2.2 pointer routes to it. (2, claude A7's constructive half, which v10's label fix left unstated) Section 4's decomposition paragraph gains one sentence: the one-year information delay costs $86.4$ kt at $h=1$ on Specification A — more than any delay-free module's entire structural cost over timely persistence ($23$/$17$/$46$/$37$ kt, one-line subtractions of Table 4's printed values) and more than M4's own structure-given-delay cost of $11.1$ kt — and the stale-persistence control ($184.4$ kt) still loses at $h=1$ to every delay-free module while beating only M4 ($195.6$ kt). Still registered with their recorded reasons: the drift/damped-trend baseline, the leave-one-origin-out influence, the Table-6 forecast explanation, and the M3/M4 deterioration explanation (all new computations); the log-RMSE demotion stays declined (the v11 floor-and-hit-count disclosure answers it without dropping a recorded score column from frozen Table 4). No frozen verdict, score, kernel, or table value changes: Tables 1–9 are byte-identical, Table 10 is the new presentation layer, and the abstract is untouched at 300 words.

## Highlights

- A scored seven-model ladder runs against two naive baselines, two specifications
- No structural model beats last-value persistence on the primary out-of-sample score
- The 1991–1995 collapse is missed by every model under both catch treatments
- Negative certificate for the scored Schaefer/Allee ladder, scoped to estimator
- Stall reconstructions and the ladder share the constant-productivity failure mode

## Abstract
This evaluation follows a stated retention rule (a model is kept only if it reduces primary RMSE relative to the next-simpler model and relative to persistence), coded before the first scoring pass and applied unchanged; later passes were declared, not preregistered (Section 4). The test is applied to Northern cod (*Gadus morhua*), NAFO 2J3KL. The primary predictand is the NCAM M-shift SSB series (DFO, 2016, Table A2) for 1983–2015, LRP 884.6 kt. Surplus-production modules form a scored ladder (not a strict nesting for M2 and M4), and two naive baselines issue fixed-window and rolling-origin forecasts. Catch enters as a coarse regime and as year-by-year landings.

No structural model has lower primary RMSE than last-value persistence. The one-year rolling RMSE is 98 kt for persistence versus 115–206 kt for the structural ladder across both catch treatments, and the five-year rolling RMSE is 265 kt versus 289–488 kt. The collapse window is missed by every model (694–819 kt structural; 670 and 688 kt naive), and on the extended 1954–2024 specification official landings drive the stock-flow module's collapse-window error to 1898 kt. A constant-productivity model with a 1992 catch drop cannot produce the crash. Neither an AR residual nor a one-year delay reduces that error (819 kt each), and on rolling origins the delay raises one-year RMSE (196 versus 135 kt).

Within this estimator and ladder, the evidence supports a negative certificate scoped to both: the scored one-step least-squares Schaefer/Allee ladder on these two unpooled series does not beat persistence on the primary score, and unidentified modules increase error. The same rule applied to a second, unpooled specification (xteNCAM, 1954–2024, LRP 276 kt) gives the same non-retention outcome (origin-matched persistence 84 kt versus M1's 120 kt at $h=1$). The machine layer verifies the recorded arithmetic and its byte-level reproducibility, not the class-level incompatibility.

**Keywords:** northern cod; biomass forecasting; surplus production; forecast evaluation; stock assessment; prediction skill

## 1. Introduction

Fisheries assessment builds structure by default. State-space age-structured assessments, surplus-production models, and ecosystem-linked extensions each add parameters, state variables, or couplings in the hope of better advice. Whether that structure improves out-of-sample forecasts — as opposed to in-sample fit — is a separate, testable question, and on it the burden of proof sits with the added structure.

Northern cod (*Gadus morhua*) in NAFO divisions 2J3KL is the canonical demanding case. The late-1980s and early-1990s collapse — a spawning stock falling from a high, weakly trending phase to a few percent of its 1980s mean — occurred under an assessment and management regime whose failures were dissected in the canonical post-mortems (Hutchings and Myers, 1994; Walters and Maguire, 1996). The non-recovery that followed the July 1992 moratorium has kept the depensation question open for three decades (Shelton and Healey, 1999). A partial rebuilding was documented in the 2010s (Rose and Rowe, 2015), but surplus production has since stalled, with some years being negative (Rose, 2026).

The measured quantity throughout is the condition of the productive stock — the spawning-stock biomass whose persistence underwrites future yield. This is distinct from the catch taken from it. A fishery can return a high extracted yield while the stock that produces it declines, and it is the latter that the forecast here must track. Any model family proposed for this stock must therefore first clear a minimal bar: it must at least beat the forecast that nothing changes. One-dimensional autonomous surplus-production maps carry an a priori structural bar that this stock confronts directly. In the fitted collapse-window parameterisation ($r = 1.935$, $K = 1032.7$ kt, constant catch $240$ kt) such a map has two positive equilibria — a lower repelling point at $144$ kt and an upper attractor at $889$ kt, with the one-step map monotone below $783$ kt — so every trajectory either settles toward the attractor or collapses toward the absorbing state, and no path that crashes and then recovers is a trajectory of the map; the scored test measures how severely that bar penalizes out-of-sample error rather than whether the bar exists.

This evaluation follows a stated retention rule, coded before the first scoring pass and applied unchanged (the pass-level freeze record is Section 4): additional model structure is retained only when it reduces primary RMSE relative to the next-simpler model and relative to persistence (§2.3). Early-warning and intervention-selection criteria are declared secondary objectives; neither is operationalised here (the Brier score is reported as a secondary diagnostic and never changes a retention verdict, and the moratorium is deliberately not evaluated). The instrument is a scored model-ablation framework — a forward-ordered ladder of surplus-production models (a scored ladder, not a strict nesting for M2 and M4) evaluated against two naive baselines. The ladder is output-only, stock-and-flow, residual, then delay and observation. A module is kept only if it improves the stated score. This paper is that empirical evaluation.

The paper asks whether stock-flow, residual, delay, or prey-informed modules reduce SSB forecast error relative to last-value persistence and to the autonomous surplus-production model. The scope is deliberately narrow: this paper does not estimate an Allee threshold, identify the cause of the 1990s collapse, or evaluate whether the 1992 moratorium was adequate.

The stock was selected because of its data availability (a full state-space assessment series), its policy relevance, and the sharpness of its collapse-and-stall trajectory. A companion study under separate review applies the same scored design to a groundwater system (the Edwards Aquifer, Texas; Author et al., in review). The two systems' series are never pooled, and no retention verdict is transferred between them.

The remainder of the article is organized as follows. Section 2 states the data, the two assessment specifications, the model ladder, and the evaluation design. Section 3 reports the results: the primary specification (3.1), annual landings and the survey-start variant (3.2), the alternative assessment specification (3.3), and prey-informed productivity (3.4). Section 4 discusses the findings, the identification limits, the reconstruction-level corroboration, and the freeze-discipline record. Section 5 concludes.

## 2. Material and methods

### 2.1 Data and specifications

The specification tables type each field as follows: D, data; E, empirical construct; M, model; N, normative threshold.

**Table 1.** Primary specification — Specification A (the 1983–2015 NCAM M-shift SSB series of DFO, 2016, Table A2).

| Field | Contents | Type |
|---|---|---|
| System | Northern cod, NAFO 2J3KL, as represented by NCAM M-shift SSB | D |
| Interest | Continuity of a spawning stock on the 2016 precautionary-approach cautious or healthy side of the 2016 LRP | N |
| Domain | Stock area in DFO (2016) Figure 1; calendar years 1983–2015 | D |
| Safe set | $S_t \ge \mathrm{LRP} = 884.6$ kt (1983–1989 mean of Table A2) | N |
| Disturbance | Unspecified productivity shocks; not a fitted $M(t)$ | M |
| Theoretical catch | Any $C_t \ge 0$ | M |
| Implementable catch | Pre-1992 directed fishery; post-2 July 1992 moratorium and low inshore removals | E |
| Horizon | Hindcast 1983–2015; two fixed test windows and rolling origin | D |
| Food web | Capelin excluded from the primary pass; tested as a variant in Section 3.4 | M |
| Norm | 2010/2016 DFO precautionary-approach LRP (1980s mean SSB), not the 2023 40% $B_{\mathrm{MSY}}$ LRP | N |

Table 1 note: the safe-set and LRP fields type the reference frame of the evaluation; the primary RMSE score never uses them (only the secondary Brier indicator score does).

Table A2 also reports fishing mortality $F$ and natural mortality $M$. They are joint outputs with SSB and are not used as exogenous inputs.

Regular et al. (2025) extend the assessment to 1954, revise the LRP to 276 kt (95% interval 180–423 kt; 40% of $B_{\mathrm{MSY}}$), and estimate 2024 SSB at 342 kt. That is a second specification — Specification B (the 1954–2024 extended xteNCAM series; Section 3.3). The two objects differ in four specification fields: the dynamics map (xteNCAM versus NCAM M-shift; start year 1954 versus 1983), the safe-set map (276 kt versus 884.6 kt), the treatment of catch, and the horizon. The two SSB columns are not mixed. Under the study's specification-matching discipline, a retention verdict does not transfer between objects whose dynamics map or safe-set map differs; here both differ, so the two specifications are evaluated separately and neither verdict imports the other.

### 2.2 Forecast models

Northern cod surplus production is represented as a discrete-time map, with $S$ in kt and $C$ in kt yr⁻¹.

**Definition 2.1 (Surplus-production map).** The autonomous surplus-production map with multiplicative depensation is

$$
S_{t+1}=\bigl[S_t+g(S_t)-C_t+\varepsilon_t\bigr]_+,
\qquad
g(S_t)=rS_t\bigl(1-S_t/K\bigr)\,a(S_t),
\qquad
a(S_t)=
\begin{cases}
1 & \text{(Schaefer; no Allee term declared)},\\[2pt]
\dfrac{S_t-\mathfrak s}{K-\mathfrak s} & \text{(depensation term active, $\mathfrak s>0$)}.
\end{cases}
$$

The factor $a(S_t)$ is a multiplicative depensation term, not a parameter switch. Setting $\mathfrak s=0$ gives $a(S_t)=S_t/K$ (a cubic modification of the logistic surplus), not the Schaefer law. The Schaefer model is the separate member of the family in which the factor is replaced by $1$ (a companion governance study under separate review makes the same point; Author et al., in review).

**Lemma 2.2 (Schaefer is not the $\mathfrak s\to 0$ limit of the depensation family).** *In the family of Definition 2.1, the Schaefer law corresponds to the choice $a\equiv 1$. The limit $\mathfrak s\to 0$ in the depensation branch yields $a(S_t)=S_t/K$, hence a cubic modification of the logistic surplus, and not the Schaefer law.*

*Proof.* Substituting $\mathfrak s=0$ in $a(S_t)=(S_t-\mathfrak s)/(K-\mathfrak s)$ gives $a(S_t)=S_t/K$, so $g(S_t)=rS_t(1-S_t/K)\cdot(S_t/K)$, a cubic surplus term. The Schaefer law requires $a\equiv 1$, which is the separate branch in which the depensation factor is replaced, not obtained by a limiting value of $\mathfrak s$. □

The model ladder is given in Table 2.

**Definition 2.3 (Scored ladder).** *The scored ladder is the forward-ordered set of seven models $\{$persist, mean, M1, M1b, M2, M3, M4$\}$ of Table 2, ordered by structural complexity (autonomous surplus map, Allee extension, stock-flow, residual, delay). It is a scored ladder (a forward-ordered set of models evaluated by a fixed retention rule), not a strict nesting for M2 and M4.*

**Table 2.** Model ladder.

| ID | Class | Free on the training window | Frozen into the test window |
|---|---|---|---|
| persist | baseline | — | $\hat S_{t+h}=S_t$ |
| mean | baseline | training mean | $\hat S_{t+h}=\bar S_{\mathrm{train}}$ |
| M1 | autonomous | $r,K$; $C$ = training-mean catch (plugged, not estimated) | same $C$ |
| M1b | autonomous with Allee | $r,K,\mathfrak s,C$ | same |
| M2 | stock-flow | $r,K$; $C_t$ prescribed | prescribed $C_t$ |
| M3 | residual | M2 + AR(1) residual | $\phi$ persisted |
| M4 | delay | M3 | forecast starts from $S_{t-1}$ |

The coarse catch regime, taken from DFO (2016) prose (the precautionary-approach framework of DFO, 2009, governs the critical-zone vocabulary used below), is $C_t=240$ kt for $t\le 1991$, $C_t=120$ kt for $t=1992$, and $C_t=5$ kt for $t\ge 1993$. Year-by-year landings (Schijns et al., 2021, Table 1) replace that regime in Section 3.2. Regular et al. (2025) Table 1 matches Schijns exactly on 1983–1993 (11 years, maximum absolute difference 0 t); STATLANT matches Schijns on 1983–1993, so the STATLANT-versus-Schijns sensitivity is closed for the collapse window (they are the same column there). A 1956 discrepancy between those sources (236,210 t versus 263,210 t) lies outside 1983–2015 and is unused. The coarseness of the regime series is a declared limitation.

Parameters are estimated by one-step least squares on the training window only. Bounds: $r\in(0.001,2]$ and $K$ constrained above the training-window maximum — the estimation code optimises $K$ on $[\max_{\mathrm{train}} S + 10, 5000]$ kt, with $500$ kt the multi-start initialiser rather than the lower bound, consistent with the frozen specification's constraint of $K$ above the training maximum. The reported fits attain the upper endpoint ($K = 5000$ kt) where the data prefer an unbounded carrying capacity; M1b's recovery-window $K = 105.9$ kt is a valid interior fit, not a bound violation. Every fitted-parameter value this article prints, with the window it belongs to and the bound it attains, is collected in Table 10; the per-origin rolling fits and the parameters the article does not print are archive items, marked there as such.

A survey-start variant replaces the surplus initial condition by $\hat q\,I_t$, where $I_t$ is the autumn research-vessel abundance index and $\hat q$ is the training-window median of $\mathrm{SSB}/I$. The index is an NCAM input, not an independent stock.

Prey-informed variants (Section 3.4) scale surplus production by a 1991 capelin regime or by the tabulated 3L spring acoustic index. Pre-1991 acoustic values are not carried across 1991. Missing survey years are not interpolated.

### 2.3 Evaluation design

Fixed windows on Specification A: collapse, train 1983–1990, test 1991–1995; recovery, train 1995–2007, test 2008–2015. Rolling origin: minimum eight training years; horizons $h=1$ and $h=5$. Estimation is by one-step least squares on the training window, while the five-year score evaluates iterated trajectories of parameters fitted for one-step fit — a declared training/testing cost-function mismatch; trajectory-matched estimation over the multi-year horizon is a registered alternative, not scored here.

The primary score is RMSE of SSB (kt). Secondary scores are mean absolute error, RMSE on $\log S$, the Brier score for $\mathbf{1}\{\hat S<\mathrm{LRP}\}$, and the sign-hit rate of $\Delta S$ on fixed windows. On Specification A the Brier indicator is near-degenerate — the $884.6$-kt LRP sits above the entire origin range, so the score separates little (Section 3.3 gives the record). The sign-hit rate is conventionally $0.00$ for persistence, whose forecast $\Delta S = 0$ has no sign; persistence is excluded from that ranking by declaration.

The retention rule is stated as explicit hypotheses.

**Definition 2.4 (Retention rule).** *A module $M$ on the ladder of Definition 2.3 is retained only if all of the following hold on the rolling-origin primary RMSE score:*

- *(H1) $M$ reduces primary RMSE relative to its declared comparator — the next-simpler rung for the nested steps (M1b against M1, M3 against M2); for the two rungs that are not strict nestings, M1 for M2 (the autonomous constant-catch map whose catch treatment M2 changes) and M3 for M4 (the module the delay acts on). M1b is reported as the alternative comparator for M2 and never decides retention;*
- *(H2) $M$ reduces primary RMSE relative to last-value persistence;*
- *(H3) each required reduction holds at both horizons $h=1$ and $h=5$ — the frozen specification's primary score is the rolling-origin RMSE pair — and exceeds a tie band of 5% of the comparator's score; improvements inside the band are ties and do not retain.*

*Retention is decided separately on each specification. A module failing any of (H1)–(H3) is not retained. Two disclosures complete the rule. First, it is a point-rule ranking under a pre-set score, not a test of equal predictive ability; the post-freeze uncertainty layer of Section 3.5 attaches Diebold–Mariano and moving-block-bootstrap intervals to its margins and changes no verdict. Second, the tie band and the comparator declarations are completions recorded at this revision, after the scores of Section 3 were computed: no recorded verdict depends on them — the smallest structural deficit against persistence (M1b's on Specification A at $h=1$) is 17%, and no (H1) comparison in Tables 3–8 reverses under either comparator reading.*

**Definition 2.5 (Negative certificate).** *A negative certificate is a machine-verified finding of non-retention of a model class under the stated retention rule (Definition 2.4): the scored one-step least-squares implementation of the class does not satisfy (H1)–(H3) on the rolling-origin primary RMSE score on the declared series. A negative certificate is weaker than a statistical null result; it is scoped to the estimator, the ladder, and the series on which it is issued.*

The machine layer that the certificate refers to is the deterministic scoring stack — the scripts registered in the Data availability record together with their pinned output checksums. What that layer verifies is the recorded arithmetic and its byte-level reproducibility. The class-level incompatibility (Proposition 4.1) is a mathematical statement proved in Section 4, not an object the machine layer verifies.

On Specification B the collapse window is train 1954–1989, test 1990–1995, and the recovery-stall window is train 1995–2012, test 2013–2024. Catch is Table 1 landings (2024 persisted from 2023). No row is taken from NCAM 2016. The ladder's rolling origin on Specification B uses a minimum of twelve training years ($n=59$ at $h=1$, $n=55$ at $h=5$); the naive baselines retain the eight-year minimum ($n=63$ and $n=59$). The two origin sets therefore overlap but are not identical, so the Table 6 comparison of persistence against the ladder mixes four extra early origins into the baselines. The origin-corrected controls are computed and reported. On the identical twelve-year origins the baselines read persistence 84 kt ($n=59$) at $h=1$ and 300 kt ($n=55$) at $h=5$, and the training mean 458 kt and 522 kt, against M1's 120 kt and 432 kt (Table 6); persistence remains the lowest-RMSE forecast, and the mixed-origin reading of Table 6 (88 kt) exceeds the controlled reading by 3.2 kt — an origin-mix effect of no retention consequence. On the identical post-break origins of the Table 7 control ($n=33$, $h=1$) the recomputed baseline is 75 kt, matching the post-break value reported with the two-regime control of Section 3.4. On the index modules' origin sets (Table 8), persistence reads 97 kt ($n=24$, $h=1$) and 193 kt ($n=20$, $h=5$) on Specification A and 79 kt ($n=36$) and 288 kt ($n=32$) on Specification B; the index module loses to the origin-matched baseline in every cell, and the verdict — the module is not retained — is unchanged.

## 3. Results

### 3.1 Primary specification

![Figure 1](figs_e1/fig1_series.png)

**Figure 1.** NCAM M-shift SSB (DFO, 2016, Table A2). Dashed line: 2016 LRP = 884.6 kt. 2015 SSB is 33.8% of that LRP, matching the advisory report statement of 34%.

![Figure 2](figs_e1/fig2_windows.png)

**Figure 2.** Multi-step forecasts from the end of each training window. Recovery is under-predicted when an AR residual fitted on a slow early-recovery train is persisted.

**Table 3.** Fixed-window scores (RMSE in kt), with both baselines reported on every window, computed on the same frozen origins declared in Section 2.3. Table 3 is not to be read as a retention table — retention is decided on rolling-origin primary RMSE only.

| Window | Model | RMSE | MAE | log-RMSE | Brier | Direction |
|---|---|---:|---:|---:|---:|---:|
| Collapse | persist | 670 | 610 | 2.71 | 0.00 | 0.00 |
| | M1 | 694 | 638 | 2.73 | 1.00 | 0.50 |
| | M1b | 694 | 636 | 2.73 | 0.80 | 0.00 |
| | M2 | 819 | 751 | 2.85 | 1.00 | 0.25 |
| | M3 | 819 | 751 | 2.85 | 1.00 | 0.25 |
| | M4 | 819 | 750 | 2.85 | 1.00 | 0.25 |
| | mean | 688 | 630 | 2.72 | 0.00 | 0.00 |
| Recovery | persist | 104 | 72 | 0.69 | 0.00 | 0.00 |
| | M1 = M2 | 120 | 105 | 0.61 | 0.00 | 0.57 |
| | M1b | **90** | 55 | 0.52 | 0.00 | 0.57 |
| | M3 | 220 | 200 | 0.92 | 0.00 | 0.57 |
| | M4 | 214 | 195 | 0.91 | 0.00 | 0.57 |
| | mean | 144 | 124 | 1.60 | 0.00 | 0.00 |

On collapse, fitted $r$ saturates at the upper bound ($\approx 2$). The 1983–1990 window is a high, weakly trending stock. Surplus production does not identify the 1992–94 mortality pulse, and dropping $C$ from 240 to 5 raises forecast SSB. The 1992 catch drop is an endogenous response to depletion rather than an exogenous policy lever; prescribing it in a constant-$r$ stock-flow equation forces the mechanical rebound instead of reproducing the crash. If the crash were a catch-regime event in this accounting, M2 would improve on M1. It does not.

On recovery, M1 and M2 coincide. The reason is structural:

**Proposition 3.1 (M1–M2 coincidence under constant catch).** *On the recovery window (train 1995–2007, test 2008–2015) of Specification A, $M1$ and $M2$ produce identical forecasts because $C_t\equiv 5$ kt on both the training and the test window.*

*Proof.* M1 plugs the training-mean catch (5 kt under the coarse regime) into the autonomous map. M2 prescribes $C_t$ year by year. On the recovery window $C_t\equiv 5$ kt for both train and test, so the two prescriptions coincide, and the least-squares $(r,K)$ optimum is identical. □

M1b reports a lower RMSE (90 kt against M1's 120 kt), but $\mathfrak s\to 0$ and $K$ collapses to the training range: an unidentified Allee parameter, not a biological threshold. The identification failure is topographically forced.

**Lemma 3.2 (Forced identification failure of the Allee parameter on a recovery window).** *On a training window along which $S_t$ rises monotonically, any $\mathfrak s$ strictly above the training minimum makes the depensation factor $a(S_t)=(S_t-\mathfrak s)/(K-\mathfrak s)$ negative on part of the window, predicting negative surplus production along an observed recovery. The least-squares optimum is therefore driven below the training minimum to avoid the penalty, and the Allee parameter $\mathfrak s$ is unidentified as a biological threshold.*

*Proof.* On a recovery window $\min_t S_t$ is positive. For $\mathfrak s>\min_t S_t$, the depensation factor is negative on $S_t\in[\min_t S_t,\mathfrak s)$, and the corresponding $g(S_t)$ is negative where the observed $\Delta S$ is positive, contributing a large squared residual. The least-squares objective is minimized by $\mathfrak s\le \min_t S_t$, which places $\mathfrak s$ below any biologically meaningful threshold; in the reported fit $\mathfrak s\to 0$ and $K$ collapses to the training range. □

M3's $\phi=0.95$ persists a negative residual and increases error.

![Figure 3](figs_e1/fig3_rmse.png)

**Figure 3.** Rolling-origin RMSE. Persistence is the best one-year and five-year point forecast.

**Table 4.** Rolling-origin summary, Specification A, coarse catch regime.

| Model | $h=1$ RMSE | $h=1$ MAE | $h=1$ log-RMSE | $h=5$ RMSE |
|---|---:|---:|---:|---:|
| persist | **98** | **48** | **0.52** | **265** |
| M1 | 121 | 80 | 8.02 | 289 |
| M1b | 115 | 80 | 8.70 | 289 |
| M2 | 144 | 61 | 0.59 | 398 |
| M3 | 135 | 53 | 3.39 | 366 |
| M4 | 196 | 82 | 0.76 | 488 |
| mean | 424 | 375 | 2.35 | 507 |

Log-RMSE for M1 and M1b is large because some origins produce trajectories that hit the numerical floor. M2 keeps the state off zero and stabilizes the log score, but loses on raw RMSE. M4, the only model that imposes a one-year assessment delay, is the worst structural model on raw RMSE. The difference measures the information cost of the one-year delay.

No structural model — M1 through M4 — is retained on Specification A. Persistence is the lowest-RMSE forecast.

### 3.2 Annual landings and survey start

Year-by-year landings for 2015 are 4.436 kt, matching DFO reported landings. Pre-collapse catches are 172–269 kt, not a flat 240. The 1992 drop is to 41 kt, then 11 kt, then 0.4–1.9 kt.

**Table 5.** Rolling-origin RMSE (kt) with annual landings.

| Model | $h=1$ | $h=5$ |
|---|---:|---:|
| persist | **98** | **265** |
| M1 | 121 | 289 |
| M1b | 115 | 289 |
| M2 | 160 | 394 |
| M3 | 154 | 352 |
| M4 | 206 | 486 |
| M2, survey start | 128 | 331 |

Annual landings make M2 worse than the coarse regime on one-year RMSE (160 versus 144 kt). Collapse-window RMSE remains about 821 kt. On the annual-catch recovery window (train 1995–2007, test 2008–2015) the ladder scores M1 264, M1b 78, M2 303, M3 609, and M4 586 kt, against a frozen-persistence error of 104 kt (forecast held at the 2007 level of 81 kt): annual landings do not repair the recovery-window fit, the residual-persistence models deteriorate severely (609 and 586 kt against 220 and 214 kt under the coarse regime), and M1b's 78 kt carries the same unidentified-Allee caveat as its regime-window fit.

Apparent net production $S_{t+1}-S_t+C_t$ is strongly negative in 1991–93 even after subtracting reconstructed catch — the model-free accounting bound that precedes every fit. With no production at all, matching the observed $\Delta S$ would require removals of order $-\Delta S$, and the observed decline is far larger than $C_t$, so extra removals dwarf both catch treatments regardless of the production form (Regular et al.'s $M \approx 2.5$ peak is the same residual in assessment clothing). A more accurate $C_t$ cannot produce the crash in a constant-$r$ surplus model, because the observed $\Delta S$ is far larger than $C_t$.

One numerical disclosure travels with the window: the annual-landings M1 (264 kt) and M1b (78 kt) differ from the coarse-regime recovery rows (M1 = 120, M1b = 90) although both treatments sit on the same SSB column. The reconciliation is that M1's constant catch is not estimated on that column: it is the training mean of the declared catch file — 5.0 kt for the coarse regime and 3.19 kt (the 1995–2007 mean of the annual landings) for the annual treatment — and the two least-squares objectives are nearly flat at their minima (SSE 128.35 versus 127.84 kt²), so the $(r, K)$ minimizer slides along the valley as the constant changes ($r = 0.458$ with $K$ pinned at its lower bound, 500.0 kt, against $r = 0.370$ with $K$ pinned at its upper bound, 5000.0 kt). The same geometry explains the M1b pair ($r$ pinned at its upper bound in both treatments; $K = 105.9$ against 129.8 kt): the dependence of the M1 fit on the catch file is the flat-objective identification of a two-parameter autonomous fit on a 13-year window, not an inconsistency between fitting objects. The same flat valley caps what the ranking can resolve: refitting the recovery-window Schaefer map with $K$ fixed anywhere on $[60, 5000]$ kt and $r$ re-optimised moves the one-step training objective only from mean squared error $127.4$ to $149.9$ kt$^2$ (training RMSE $11.29$–$12.24$ kt, a spread under $0.95$ kt) while $r$ compensates from $0.435$ to $0.773$ — on this window the $(r, K)$ pair is not identified, and the ordering of valley variants is not a robust ranking. One mechanism unifies both faces of the catch-dependence: a constant catch shifts the flat valley's minimiser without moving the objective, so the rolling scores (refit at every origin) are insensitive to the catch treatment while the single fixed-window fit is not.

Starting from $\hat q I_t$ instead of SSB gives one-year RMSE 128 kt (still worse than persist 98); one-year log-RMSE 0.49 versus persist 0.52; five-year RMSE 331 versus persist 265. On the primary score the variant is not retained. The log-score difference is recorded and not used for selection. A set-valued conservative filter is not instantiated: there is no observation fibre — no independent observation channel — outside NCAM.

### 3.3 Alternative assessment specification

![Figure 4](figs_e1/fig4_xtencam.png)

**Figure 4.** The two specifications. Overlap 1983–2015 RMSE = 126 kt (2015: NCAM 299 kt, xteNCAM 273 kt). Different safe sets. Not pooled.

Checkpoints from Regular et al. (2025) Table 17: 2005 SSB = 26 kt (95% interval 22–31), 2017 = 451 kt (381–534), 2021 = 423 kt (NCAM and xteNCAM said to agree), 2024 = 342 kt (246–475), 2024/LRP = 1.24. The 2005 values (26 kt versus NCAM 25.18 kt) can agree on a low year without the two series sharing a reference point; agreement on a low year does not warrant splicing the two columns. The same late-period biomass is 34% of the old LRP and above the new one after 2016.

**Table 6.** Rolling-origin RMSE on Specification B (kt).

| Model | $h=1$ | $h=5$ |
|---|---:|---:|
| persist | **88** | **318** |
| M1 | 120 | 432 |
| M1b | 152 | 446 |
| M2 | 166 | 1059 |
| M3 | 127 | 930 |
| M4 | 206 | 1031 |
| mean | 449 | 506 |

Collapse window (train 1954–89, test 1990–95): M1 RMSE 817 kt; M2 1898 kt. Official landings worsen the crash forecast. No module is retained. Persistence remains the lowest-RMSE forecast. That is the second independent negative certificate — a machine-verified finding of non-retention, weaker than a statistical null result — under the same rule on a different specification. The longer series and the revised LRP do not justify retaining the additional modules.

Recovery-stall window (train 1995–2012, test 2013–2024; $n=12$): M1 254 kt, M1b 178 kt, M2 269 kt, M3 268 kt, M4 269 kt. The 2013–2024 test path rises from 167 to 462 kt, all above the 112 kt training-end value, so a persistence forecast frozen at that value errs by 262 kt — more than M1 and M1b on this single origin. This fixed-origin comparison does not enter the retention rule, which is decided on rolling-origin primary RMSE (Table 6, where persistence is not beaten at either horizon). M1b's window fit carries the identification fragility familiar from its other window fits: a small fitted Allee parameter ($\mathfrak s = 5.3\times10^{-3}$) with a carrying capacity ($K=500$ kt) extrapolated far beyond the training range (maximum 117 kt).

On the rolling Brier score for $\mathbf{1}\{\hat S<\mathrm{LRP}\}$ on Specification B (the secondary score declared above; LRP = 276 kt): persistence 0.06 at $h{=}1$ and 0.27 at $h{=}5$; M1 0.05 and 0.45; M1b 0.15 and 0.47; M2 0.07 and 0.36; M3 0.02 and 0.31; M4 0.07 and 0.38. M1 and M3 improve the one-year Brier score over persistence (0.05 and 0.02 versus 0.06); no model improves it at $h{=}5$, and no model improves the primary RMSE score at either horizon (Table 6), so the retention verdict is unchanged. For reference, the same secondary score on Specification A is 0.00 at both horizons for persistence: the persistence indicator forecasts $\mathbf{1}\{S_t<884.6\}$ from the origin state, and its score is zero because every origin state is already below the 884.6-kt LRP — in particular the first origin, $S_{1990}$, lies below the 1983–89 mean bound, so the collapse train starts on the downslope of its own reference period — and the target years 1991–2015 are below the LRP as well, so indicator and outcome agree at every origin. (The bare fact that targets are below the LRP would not by itself make the persistence indicator correct; the origin states being below it does.) The structural scores are M1 0.04/0.05, M1b 0.00/0.05, M2 0.08/0.14, M3 0.08/0.10, M4 0.08/0.14 — unbeatable there, and reported only to keep the two specifications' records separate and complete.

Regular et al. assign the 1992–94 disappearance primarily to $M$ (peak $\approx 2.5$), informed by tagging and a capelin/cod predictor, and note that some of that $M$ could still be unreported $F$. That split is the same as the surplus residual after subtracting official $C_t$.

### 3.4 Prey-informed productivity

Murphy et al. (2025) report a 1991 acoustic collapse (1985–90 median 3704 kt versus 1991–2022 median 174 kt). A two-regime $r$ with break 1991 uses the high regime only for forecasts issued before 1991. Capelin enters as a candidate disturbance class, not as a fitted parameter.

**Table 7.** Rolling RMSE, two-regime $r$.

| Specification | Model | $h=1$ | $h=5$ |
|---|---|---:|---:|
| A | persist | **98** | **265** |
| A | M_cap | 154 | 334 |
| B | persist | **88** | **318** |
| B | M_cap | 147 | 894 |

On post-break origins only (Specification B, $h=1$; $n=33$): M_cap 107 versus persistence 75 on the identical origin set (the 88 of Table 7 is the all-origins value). Not retained. On Specification A post-break origins ($n=24$) the corresponding M_cap value is 149 kt.

The year-by-year 3L spring acoustic biomass is tabulated in Zenodo 10.5281/zenodo.17515115, with 2023 = 331.3 kt from Murphy et al. (2025). Surplus is scaled by $(I_{\mathrm{known}}/I_{\mathrm{ref}})^{b}$, where $I_{\mathrm{known}}(t)$ is the last observation at or before $t$, $I_{\mathrm{ref}}$ is the training-window median of the observed index, and $b$ is a third free parameter fitted jointly with $r$ and $K$ by one-step least squares on the training window. The module additionally faces degrees-of-freedom starvation: three parameters ($r, K, b$) are fitted on as few as eight training years at the shortest origins, which invites in-sample overfitting and penalizes the one-year out-of-sample comparison. Survey years are unobserved in part of the record, so the index-forecast origins number $n=24$ ($h=1$) and $n=20$ ($h=5$) on Specification A and $n=36$ and $n=32$ on Specification B, against the SSB-based rolling-origin counts ($n=25$ at $h=1$ and $n=21$ at $h=5$ on Specification A; Section 4).

**Table 8.** Rolling RMSE, observed acoustic index.

| Specification | Model | $h=1$ | $h=5$ |
|---|---|---:|---:|
| A | persist | **98** | 265 |
| A | persist (origin-matched) | 97 | 193 |
| A | M_cap_index | 150 | 262 |
| B | persist | **88** | **318** |
| B | persist (origin-matched) | 79 | 288 |
| B | M_cap_index | 132 | 492 |

On the origin-matched reading the five-year near-tie on Specification A dissolves — the baseline on the module's own origins reads 193 kt against the module's 262 kt — and one-year RMSE is worse under both readings (150 versus 98 kt on the SSB origins and 97 kt on the module's); on Specification B the module's 132/492 kt stand against origin-matched baselines of 79/288 kt. The module is not retained under either baseline reading.

### 3.5 Uncertainty on the retention margins (post-freeze layer)

A post-freeze uncertainty layer attaches Diebold–Mariano tests (Diebold and Mariano, 1995; unweighted HAC truncation at lag $h-1$) and moving-block bootstrap intervals (Künsch, 1989; block length $\max(h,3)$, 20,000 replications, seeded) to the retention margins of Definition 2.4. It is computed from the archived per-origin forecast files: on Specification B the xteNCAM rolling file; on Specification A the archived per-origin file is the annual-landings pass of Section 3.2 (the coarse-regime pass's per-origin rows are not archived — its summary is — and the verdicts coincide under both treatments). The persistence baseline is not archived per-origin; it is recomputed on the identical origin sets from the registered series, and the recomputation reproduces the recorded origin-matched baselines (98 and 265 kt on Specification A; 84 and 300 kt on the matched Specification B origins) — the script fails loudly otherwise. The layer attaches uncertainty to margins the point rule has already ranked; it changes no frozen verdict, score, or table value.

**Table 9.** Uncertainty on the retention margins (post-freeze layer; Diebold–Mariano with HAC lag $h-1$; Künsch moving-block bootstrap, block length $\max(h,3)$, 20,000 replications, seeded). Gaps are module minus comparator, in kt; positive gaps mean the module is worse.

| Spec | $h$ | Module | Comparator | $n$ | RMSE module | RMSE comp. | Gap (kt) | DM $z$ | 95% CI (kt) | $p$ |
|---|---:|---|---|---:|---:|---:|---:|---:|---|---:|
| A | 1 | M1 | persist | 25 | 120.5 | 98.0 | +22.5 | 1.15 | [−13.3, +50.5] | 0.192 |
| A | 1 | M1b | persist | 25 | 114.8 | 98.0 | +16.7 | 0.98 | [−19.3, +59.2] | 0.376 |
| A | 1 | M2 | persist | 25 | 160.4 | 98.0 | +62.4 | 1.30 | [−11.9, +107.0] | 0.445 |
| A | 1 | M3 | persist | 25 | 153.6 | 98.0 | +55.6 | 1.02 | [−18.0, +91.6] | 0.927 |
| A | 1 | M4 | persist | 25 | 206.3 | 98.0 | +108.2 | 1.51 | [−8.2, +192.7] | 0.338 |
| A | 1 | M2 | M1 | 25 | 160.4 | 120.5 | +39.9 | 1.13 | [−59.1, +88.5] | 0.687 |
| A | 1 | M4 | M3 | 25 | 206.3 | 153.6 | +52.7 | 0.99 | [+4.7, +144.7] | <0.001 |
| A | 5 | M1 | persist | 21 | 288.7 | 264.7 | +24.0 | 1.84 | [−43.1, +56.4] | 0.279 |
| A | 5 | M1b | persist | 21 | 288.6 | 264.7 | +23.9 | 1.84 | [−43.1, +56.4] | 0.284 |
| A | 5 | M2 | persist | 21 | 393.8 | 264.7 | +129.1 | 1.10 | [−25.0, +215.9] | 0.576 |
| A | 5 | M3 | persist | 21 | 351.5 | 264.7 | +86.8 | 1.10 | [−7.3, +131.9] | 0.266 |
| A | 5 | M4 | persist | 21 | 486.4 | 264.7 | +221.7 | 1.14 | [−27.0, +412.8] | 0.759 |
| A | 5 | M2 | M1 | 21 | 393.8 | 288.7 | +105.1 | 0.97 | [−78.8, +230.1] | 0.807 |
| A | 5 | M4 | M3 | 21 | 486.4 | 351.5 | +134.9 | 1.15 | [−28.4, +292.4] | 0.902 |
| B | 1 | M1 | persist | 59 | 119.5 | 84.4 | +35.0 | 2.81 | [+2.7, +70.8] | 0.032 |
| B | 1 | M1b | persist | 59 | 151.6 | 84.4 | +67.2 | 3.60 | [+18.3, +117.7] | 0.009 |
| B | 1 | M2 | persist | 59 | 166.0 | 84.4 | +81.6 | 3.22 | [+36.4, +122.8] | <0.001 |
| B | 1 | M3 | persist | 59 | 126.7 | 84.4 | +42.3 | 1.85 | [+1.0, +92.5] | 0.042 |
| B | 1 | M4 | persist | 59 | 205.7 | 84.4 | +121.3 | 3.20 | [+53.7, +193.0] | <0.001 |
| B | 1 | M2 | M1 | 59 | 166.0 | 119.5 | +46.6 | 1.78 | [−20.5, +104.5] | 0.170 |
| B | 1 | M4 | M3 | 59 | 205.7 | 126.7 | +79.0 | 3.07 | [+35.6, +116.4] | <0.001 |
| B | 5 | M1 | persist | 55 | 431.9 | 300.0 | +131.9 | 2.06 | [+33.2, +218.6] | 0.008 |
| B | 5 | M1b | persist | 55 | 445.5 | 300.0 | +145.5 | 1.80 | [+18.2, +250.9] | 0.023 |
| B | 5 | M2 | persist | 55 | 1058.9 | 300.0 | +758.9 | 2.15 | [+363.6, +1038.5] | <0.001 |
| B | 5 | M3 | persist | 55 | 930.1 | 300.0 | +630.2 | 2.39 | [+352.8, +845.6] | <0.001 |
| B | 5 | M4 | persist | 55 | 1030.7 | 300.0 | +730.8 | 2.35 | [+407.3, +978.3] | <0.001 |
| B | 5 | M2 | M1 | 55 | 1058.9 | 431.9 | +627.0 | 1.97 | [+195.7, +929.7] | 0.004 |
| B | 5 | M4 | M3 | 55 | 1030.7 | 930.1 | +100.6 | 1.88 | [+20.2, +177.4] | 0.007 |

Readings. On Specification A no non-retention margin separates from zero: at $h=1$ the deficits against persistence (16.7–108.2 kt on $n=25$) carry DM $z$ from 0.98 to 1.51 with bootstrap $p$ from 0.19 to 0.93, and at $h=5$ (23.9–221.7 kt on $n=21$) $z$ from 1.10 to 1.84 with $p$ from 0.27 to 0.76 — the heavy-tailed collapse-window losses dominate the bootstrap variance at this sample size, and the negative certificate on Specification A is a point-rule ranking whose margins are within noise, the reading Section 4 already records ("they suffice to rank models and do not suffice to certify a small skill difference"). On Specification B the non-retention separates: every module's deficit against persistence is decisive at $h=1$ ($p$ from 0.042 to below 0.001 on $n=59$) and at $h=5$ ($p$ at most 0.023 on $n=55$). The declared (H1) comparators behave asymmetrically: M2's deficit against M1 is within noise at $h=1$ on both specifications and at $h=5$ on Specification A, separating only on Specification B at $h=5$ ($p=0.004$), while M4's delay cost against M3 separates at $h=1$ on both specifications ($p$ below 0.001) and at $h=5$ on Specification B ($p=0.007$) but not on Specification A ($p=0.90$). The alternative comparator reading (M2 against M1b) is within noise at $h=1$ on both specifications and at $h=5$ on Specification A, separating on Specification B at $h=5$ ($p=0.005$): the comparator declaration of Definition 2.4 is immaterial to every recorded verdict, as the completion records. The layer is produced by the registered script `campaign_e1_dm_uncertainty.py` (batch-7 audit directory of the repository), deterministic under seed 0, with its output archived alongside it (`results/e1_dm_uncertainty.csv`).

### 3.6 Fitted parameters as printed (post-freeze presentation layer)

This section collects in one place every fitted-parameter value the article prints, the window or treatment it belongs to, and the bound it attains. It is a presentation layer over values already printed at their source sites — nothing is recomputed, no value is new, and quantities the article does not print (the per-origin rolling fits of every module, the index module's per-window exponent $b$, and the one-year delay module's structural setting) are marked as archive items rather than invented. The collection exists so the identification record — bounds attained, interior fits, the flat valley — can be read at a glance.

**Table 10.** Fitted parameters as printed (source sites in parentheses; values quoted verbatim from the text).

| Module | Window / treatment | Values as printed | Bound / identification status |
|---|---|---|---|
| M1 | Collapse, Specification A (train 1983–1990) (§1, §4) | $r = 1.935$, $K = 1032.7$ kt, constant catch $240$ kt; repeller $144$ kt, attractor $889$ kt, monotone below $783$ kt, $F'(S^*) \approx -0.39$ | §3.1 records the collapse-window fitted $r$ as saturating at the upper bound ($\approx 2$), quoted as printed |
| M1 | Recovery, annual landings (§3.2) | $r = 0.458$, constant catch $3.19$ kt (the 1995–2007 landings mean); training SSE $128.35$ kt² | $K$ pinned at its lower bound, $500.0$ kt |
| M1 | Recovery, coarse catch regime (§3.2) | $r = 0.370$, constant catch $5.0$ kt (the training mean); training SSE $127.84$ kt² | $K$ pinned at its upper bound, $5000.0$ kt |
| M1b | Recovery, annual landings (§2.2, §3.2) | $K = 105.9$ kt | $r$ pinned at its upper bound in both treatments; $K$ a valid interior fit |
| M1b | Recovery, coarse catch regime (§3.2) | $K = 129.8$ kt | (same row's treatment) |
| M1b | Recovery-stall, Specification B (train 1995–2012) (§3.3) | $\mathfrak{s} = 5.3\times10^{-3}$, $K = 500$ kt, training-window maximum $117$ kt | declared identification fragility: $\mathfrak{s}$ small, $K$ extrapolated far beyond the training range |
| M3 | Rolling, Specification A (§3.1) | $\phi = 0.95$ (AR(1) residual coefficient) | printed value; the per-window rolling $\phi$ values are archive items |
| M3 | Index module (§3.4) | $r$, $K$, $b$ fitted jointly by one-step least squares | fitted values not printed (archive); degrees-of-freedom note at $n = 8$ training years |
| M1 / M1b | Flat-valley sweep, recovery window (§3.2) | $K$ fixed anywhere on $[60, 5000]$ kt moves the one-step training objective only from MSE $127.4$ to $149.9$ kt² (training RMSE $11.29$–$12.24$ kt) while $r$ compensates over $[0.435, 0.773]$ | the $(r, K)$ pair is not identified on this window; the ordering of valley variants is not a robust ranking |
| M4 | Rolling, all specifications | no fitted parameters; the one-year assessment delay is structural | archive: the module carries no fitted values to print |
| All modules | Per-origin rolling fits | archive items (not printed); M1b's Specification B rolling Allee optimum is environment-sensitive at the ±17 kt level (§Data availability) | — |

Bounds, as declared in Section 2.2: $r \in (0.001, 2]$; $K$ optimised on $[\max_{\mathrm{train}} S + 10, 5000]$ kt with $500$ kt the multi-start initialiser rather than the lower bound, and $K$ constrained above the training-window maximum throughout. The table's rows quote the source sections' own phrasing where the two differ (Section 2.2's bound declaration and Section 3.2's pinned-fit record are both as printed; neither is reconciled here).

## 4. Discussion

The observed path is non-monotone. An exact fixed autonomous scalar trajectory cannot reproduce it. The obstruction is structural, and the scored collapse failure is its finite-sample face.

**Proposition 4.1 (Non-reproduction of non-monotone paths by autonomous scalar surplus maps).** *Let $S_{t+1}=F(S_t)$ be an autonomous one-dimensional surplus-production map of Definition 2.1 with at most two positive equilibria — a lower repelling point and an upper attracting point — and a one-step map monotone below its maximum; the single-equilibrium monotone regime is the special case, and the fitted collapse-window map ($r = 1.935$, $K = 1032.7$ kt, constant catch $240$ kt) has exactly this form (repeller $144$ kt, attractor $889$ kt, monotone below $783$ kt). If the observed path $(S_t)$ is non-monotone (crash followed by partial recovery), then no trajectory of $F$ reproduces $(S_t)$ exactly. M1's collapse failure on Specification A is the finite-sample face of this obstruction: it is the incompatibility of the observed path with the autonomous surplus-production model class.*

*Proof.* Below the lower equilibrium $F(S) < S$, so every trajectory that enters that region decreases toward the absorbing state and never rises — a crash followed by recovery is excluded from below. Between the two equilibria $F(S) > S$, so trajectories there move toward the attractor (in the fitted map with damped oscillations around it — the slope at the attractor is $F'(S^\star) \approx -0.39$ — not a monotone approach); a crash through the repeller is excluded from above. A path that crashes through the lower equilibrium and then recovers is therefore not a trajectory of $F$. □

The fixed-window sign-hit rates of $\Delta S$ (0.00–0.50 on collapse; Table 3) record the directional character of that failure: the structural models miss not only the magnitude of the crash but the sign of the trajectory exactly when the official catch series drops.

Under both the coarse catch regime and official landings, lowering $C$ in 1992 cannot generate the crash. Collapse on these specifications is a productivity, unallocated-mortality, or observation event, not a surplus-production response to the declared catch drop. That is compatible with DFO's caution that NCAM $M$ can absorb unreported deaths: the crash remains such an event under the best available public catch reconstruction, which tightens that limitation rather than relaxing it.

Unidentified extra structure increases error. Autoregressive residuals fitted on short, regime-changing windows persist the wrong sign. An Allee parameter goes to the boundary. A one-year delay removes information. These modules stay descriptive unless the conditions under which a module's contribution could be certified rather than merely scored hold; M3 and M4 are not certificates here.

The 2016 LRP is the 1980s mean SSB. Slack to that bound is near zero by construction throughout the training window that precedes collapse. A leading-indicator claim that uses this safe set is circular for 1983–1990.

The moratorium is a change in implementable catch and is already in $C_t$. A separate delay switch does not add a degree of freedom beyond stock-flow. Whether the 1992 architecture has an empty viability kernel is a viability statement, not a one-year RMSE statement.

One-dimensional surplus production is not NCAM: age structure, migration, and survey catchability are omitted. The test is whether this ladder is retained under the stated score, not whether the assessment is a good filter. M4 is a delay, not a Kalman filter; its one-year gap against persistence mixes the information delay with the model's own cost. The separating control — persistence issued from the last available assessment, $S_{t-1}$ — decomposes the gap: on Specification A the control reads 184.4 kt at $h = 1$ and 329.8 kt at $h = 5$, against M4's 195.6 kt and 488.3 kt, so the information delay — the year-old start under the same persistence rule — accounts for 86.4 of the 97.5-kt one-year gap and the surplus model's own cost for the remaining 11.1 kt, and 65.1 versus 158.4 kt of the five-year gap; on Specification B the control reads 158 kt and 337 kt against M4's 206 kt and 1031 kt, where the model's own cost is again modest at $h = 1$ (48 of 118 kt) and dominant at $h = 5$ (694 of 713 kt). M4's error is therefore mostly the information delay at the one-year horizon on both specifications, and mostly the surplus model's own structure at the five-year horizon on Specification B: at $h = 1$ the surplus model's own penalty is only about 11 kt — the delay, not the structure, separates M4 from persistence — while at $h = 5$ on Specification B the model's own cost dominates (694 of 713 kt). Read constructively, the same printed arithmetic says the value of a timely assessment exceeds the value of any structure tested: the one-year information delay costs $86.4$ kt at $h = 1$ on Specification A — more than the entire structural cost of any delay-free module (M1 $23$ kt, M1b $17$ kt, M2 $46$ kt, M3 $37$ kt over timely persistence, each a one-line subtraction of Table 4's printed values) and more than M4's own structure-given-delay cost of $11.1$ kt — and the stale-persistence control, $184.4$ kt, still loses at $h = 1$ to every delay-free module while beating only the delay-carrying M4 ($195.6$ kt). The predictand is an assessment smoother (NCAM/xteNCAM SSB), not a raw observation: forecasting it is forecasting a filtered state, and persistence inherits the smoother's autocorrelation — the comparison is valid for "does this ladder track this assessment," not for a vintage or early-warning reading, which would require assessment vintages at each origin, and none is available. At the five-year horizon the persistence baseline additionally carries a demographic reading that the evaluation does not assert: holding SSB constant over roughly a full cod generation implicitly assumes recruitment, mortality, and growth exactly balance; persistence is retained as the scoring benchmark the retention rule is defined against, not as a biological projection. Recreational catch remains incompletely measured. The log-RMSE scores of Table 4 carry a floor caveat: structural trajectories absorb at the numerical floor $\varepsilon_{\mathrm{log}} = 10^{-3}$ kt rather than at zero (the trajectory code clips the state to $[\varepsilon_{\mathrm{log}}, 10^{6}]$ kt), and the reported values use $\log\max(\hat S, \varepsilon_{\mathrm{log}})$; $\varepsilon_{\mathrm{log}}$ is part of the registered scoring configuration and is distinct from the process noise $\varepsilon_t$ of Definition 2.1. The floor binds often: on the archived per-origin records (the annual-landings rolling pass of Section 3.2) 15 of 25 M1 and 17 of 25 M1b one-year origins and 19 of 21 five-year origins for both modules absorb at the floor (M3 at 3; M2 and M4 at most once per horizon); on Specification B, 22 of 59 and 24 of 59 at $h=1$ and 36 of 55 and 46 of 55 at $h=5$ (M2, M3, and M4 between 0 and 11). The raw-RMSE column is the retention score. A constant-productivity map is misspecified for a series whose assessment attributes the crash to $M \approx 2.5$; the test is whether that misspecification still forecasts SSB better than persistence, and the negative certificate answers it for this ladder on these series. Sample sizes are small ($n=33$ years on Specification A; rolling $n=25$ at $h=1$ and $n=21$ at $h=5$). They suffice to rank models and do not suffice to certify a small skill difference. The 2023 40% $B_{\mathrm{MSY}}$ LRP is the Specification B setting, and Section 3.3 is that review: the ladder was run on the xteNCAM series under a fresh specification-matching review, with the same non-retention verdict.

**Reconstruction-level corroboration.** An independent, assessment-level record sharpens the same boundary. Rose (2026) compares two surplus-production reconstructions of the stock spanning 1983–2023 — the Rose and Walters (2019) model and the DFO (2024) assessment model — and documents that surplus production and stock growth stalled after 2015, with some years negative, the stall-point biomass being controversial between the two reconstructions and well below historical norms. The recovery-stall window of Specification B (train 1995–2012, test 2013–2024) overlaps that period (its 2016–2024 portion). A stock whose surplus production and stock growth stall together, with some years negative and the stall-point biomass below historical norms — the configuration Rose (2026) reports — is precisely the configuration a constant-productivity surplus law cannot reproduce, and the ladder's single-origin comparison on that window (M1 254 kt, M1b 178 kt against persistence 262 kt, with no retention on the rolling score) shows the same failure on the forecast side. The two reconstructions' disagreement at the stall point is moreover the assessment-level twin of the ladder's own non-uniqueness: M1b's apparent recovery-window skill is carried by a carrying capacity extrapolated far beyond the training range, exactly the extrapolation on which the two reconstructions diverge. Rose (2026) also documents the limit-reference-point trajectory — successive downward revisions to just over 0.3 Mt, then to about 0.25 Mt in 2025 — which is the norm-field drift that separates the two specifications evaluated here (884.6 kt versus 276 kt) and the reason their columns are never pooled.

**Attribution and the prey modules.** Rose (2026) infers from structural-equation models that the post-2015 production deficit is limited by capelin and amplified by harp seal predation, with fishing almost certainly not the sole cause. That attribution is consistent with the ladder's two negative findings, and it sharpens both. First, it matches the catch-treatment null: no catch treatment repairs the collapse, because the missing term is not catch. Second, it draws the identification boundary inside the prey results: capelin limitation can be a real production driver — the 1991 acoustic collapse is large (1985–90 median 3704 kt versus 1991–2022 median 174 kt) — while the corresponding forecast modules still fail the stated score. A driver's reality at the reconstruction level does not make it a usable forecast module at the surplus-production level; the two-regime and acoustic-index variants were not identified on their training windows, and the retention rule keeps them out for exactly that reason.

**Freeze discipline.** The evaluation windows and scoring rules were coded before the first scoring pass and applied unchanged; the design is a fixed computational protocol rather than a prospective clinical-style registration. Unlike the companion evaluation on the Edwards Aquifer (Author et al., in review), whose protocol files are dated and locked before scoring, the cod side carries no dated pre-score protocol file: the passes evolved (primary, annual-landings, survey-start, capelin, Specification B) with each extension declared in the manuscript rather than preregistered — a freeze-discipline caveat, recorded so that the evidentiary asymmetry between the two studies is visible.

The scores do not transfer to an interval-verified linear template (a companion methodological study, Author et al., in preparation; that template is a linear $(S,K)$ construction, not this SSB series), do not instantiate a closed-loop information filter (registered as the framework's next structural addition), and do not mix the two assessment specifications. The delay instantiated here is a one-year information delay, not a retarded functional differential equation; community-level early-warning margins are not used (the underlying extract is not archived). No framework result is treated as established without specification matching and independent verification.

On this evidence, within the scope of this estimator and ladder, modules that are not identified on the training data do not reduce forecast error. The retained forecast is persistence, together with the negative certificate for the autonomous scalar class.

## 5. Conclusions

On locked NCAM M-shift SSB for 1983–2015, last-value persistence is more accurate than surplus production, catch-driven stock-flow, autoregressive residuals, delayed information, and prey-informed productivity. The crash is not a catch-drop event in this accounting. Extra modules that fail identification increase error. The same retention outcome holds on the unpooled xteNCAM series, whose post-2015 stall period fails in the same way the reconstructions stall.

The paper reports a forecast comparison. It does not conclude that the stock is unsustainable, and it does not conclude that the evaluation framework is empirically confirmed on this stock.

## Data availability

All input data, analysis scripts, and result files are archived in the public repository at https://github.com/MIKEAA2020/general-sustainability; the frozen model specification is archived with them. Primary spawning-stock-biomass series: DFO (2016), Table A2. Alternative assessment series and landings: Regular et al. (2025), Tables 17 and 1. Historical landings: Schijns et al. (2021). Capelin acoustic index: Murphy et al. (2025), Zenodo repository 10.5281/zenodo.17515115. All computations are deterministic: within a fixed interpreter and library stack, repeated executions reproduce every result file byte for byte, and an independent re-execution of the scoring runners verified all 29 recorded output checksums (29/29 pinned) and regenerated all 30 result files byte-identically (30/30; one registered file carries no pinned checksum and is covered by the regeneration comparison). Across environments the record is: the intervention runners and the OLS-based prediction runners regenerate their outputs byte for byte, while the four optimizer-based forecast runners (L-BFGS-B fits) reproduce every scored row at printed precision except the M1b rolling row on Specification B, whose Allee optimum is environment-sensitive at the ±17 kt level ($h=1$: 151.6 versus 153.2 kt; $h=5$: 445.5 versus 462.5 kt, on Python 3.12/numpy 2.1.3/scipy 1.14.1 versus the recorded original environment) — consistent with that model's declared identification fragility ($\mathfrak s\to 0$, $K$ at bound), and immaterial to the retention verdict, which persistence wins at both horizons by margins far larger than the instability. The archive records the checksums of the original-environment outputs; the deterministic-in-environment claim and this sensitivity note together are the reproducibility statement. The two assessment specifications (NCAM and xteNCAM) were analysed throughout as separate, unpooled series. The post-freeze uncertainty layer (Section 3.5) is produced by `batch 7 (audits of agent arena 1 paper rewrites)/campaign_e1_dm_uncertainty.py` — seeded and deterministic, with Diebold–Mariano (HAC) and Kunsch moving-block bootstrap on the archived per-origin forecast files — and its output is archived alongside it as `batch 7 (audits of agent arena 1 paper rewrites)/results/e1_dm_uncertainty.csv`; the persistence baseline is recomputed there on the identical origin sets from the registered series and asserted against the recorded origin-matched values.

```
python3 src/run_ladder.py && python3 src/run_xte.py
python3 src/run_capelin_regime.py && python3 src/run_capelin_index.py
python3 src/compare_catch.py && python3 src/make_figures.py
```

## CRediT authorship contribution statement

[To be completed at submission.]

## Funding

[To be completed at submission.]

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## References

Author, A., et al., in review. Does a one-pool water-balance model improve forecasts of Edwards Aquifer head? A scored test at J-17. Companion forecast-evaluation study (Edwards Aquifer, Texas).

Author, B., et al., in review. Periodic review as sampled governance: sample-and-hold dynamics of assessment-driven effort control. Companion governance study.

Author, C., et al., in preparation. Interval-verified bounds in linear management templates. Companion methodological study.

Cadigan, N.G., 2016. A state-space stock assessment model for northern cod, including under-reported catches and variable natural mortality rates. Can. J. Fish. Aquat. Sci. 73, 296–308.

Diebold, F.X., Mariano, R.S., 1995. Comparing predictive accuracy. J. Bus. Econ. Stat. 13, 253–263. https://doi.org/10.1080/07350015.1995.10524599

DFO, 2009. A fishery decision-making framework incorporating the Precautionary Approach. Fisheries and Oceans Canada, Ottawa.

DFO, 2010. Proceedings of the Newfoundland and Labrador Regional Atlantic cod Framework Meeting. DFO Can. Sci. Advis. Sec. Proceed. Ser. 2010/053.

DFO, 2016. Stock Assessment of Northern cod (NAFO Divs. 2J3KL) in 2016. DFO Can. Sci. Advis. Sec. Sci. Advis. Rep. 2016/026.

DFO, 2024. NAFO Divisions 2J3KL Northern Cod stock assessment to 2024. DFO Can. Sci. Advis. Sec. Sci. Advis. Rep. 2024/049.

DFO, 2024. Assessment of capelin in NAFO Divisions 2J3KL. DFO Can. Sci. Advis. Sec. Sci. Advis. Rep. 2024/050.

Hutchings, J.A., Myers, R.A., 1994. What can be learned from the collapse of a renewable resource? Atlantic cod, Gadus morhua, of Newfoundland and Labrador. Can. J. Fish. Aquat. Sci. 51, 2126–2146.

Künsch, H.R., 1989. The jackknife and the bootstrap for general stationary observations. Ann. Stat. 17, 1217–1241. https://doi.org/10.1214/aos/1176347265

Murphy, H.M., Adamack, A.T., Lewis, R.S., Bourne, C.M., 2025. Assessment of capelin in NAFO Divisions 2J+3KL to 2023. DFO Can. Sci. Advis. Sec. Res. Doc. 2025/022.

Northwest Atlantic Fisheries Centre, 2025. 2J3KL cod and capelin biomass indices. Zenodo. https://doi.org/10.5281/zenodo.17515115

Regular, P.M., et al., 2025. Assessment of the Northern Cod stock in NAFO Divisions 2J3KL in 2024. DFO Can. Sci. Advis. Sec. Res. Doc. 2025/048.

Rose, G.A., 2026. Northern cod comeback: 10 years after. Can. J. Fish. Aquat. Sci. 83, 1–14. https://doi.org/10.1139/cjfas-2025-0141

Rose, G.A., Rowe, S., 2015. Northern cod comeback. Can. J. Fish. Aquat. Sci. 72, 1789–1798.

Rose, G.A., Walters, C.J., 2019. The state of Canada's iconic Northern cod: a second opinion. Fish. Res. 219, 105314.

Schijns, R., Froese, R., Hutchings, J.A., Pauly, D., 2021. Five centuries of cod catches in Eastern Canada. ICES J. Mar. Sci. 78, 2675–2683.

Shelton, P.A., Healey, B.P., 1999. Should depensation be dismissed as a possible explanation for the lack of recovery of the northern cod (Gadus morhua) stock? Can. J. Fish. Aquat. Sci. 56, 1521–1524.

Walters, C., Maguire, J.-J., 1996. Lessons for stock assessment from the northern cod collapse. Rev. Fish Biol. Fish. 6, 125–137.

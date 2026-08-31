# Does catch governance protect the limit reference point? An intervention-selection test on Northern cod (NAFO 2J3KL)

**Prepared in the format of Fisheries Research (short communication)**

## Abstract
Intervention selection is scored rather than asserted: a governance module is kept only if it improves a declared protection-and-supply outcome, with the protocol frozen before any kernel was computed. A companion forecast-evaluation study (under separate review) ended in a negative certificate — persistence unbeaten out of sample; that certificate is scored there, not here. On the same fixed series, robust viability kernels of the 2016 limit reference point (884.6 kt) are computed for a declared catch-policy family under persistent productivity floors. (1) Productivity: under the two harshest floors — both exceeding the map's maximum surplus (g_max = rK/4 = 296 kt yr⁻¹) — no catch policy, zero included, holds the LRP; the result is qualified by that mechanism and concerns these disturbance classes, not Northern cod productivity. (2) Selection: no declared policy is retained; the reactive rules are strictly less protective than the moratorium at the boundary — the mirror image of a companion groundwater result. (3) Constructive: the maximal robust flat catch is 57.6 kt (g(K*) − |e_q10| = 172.47 − 114.85 = 57.62 kt yr⁻¹) under the 10th-percentile class; no positive catch is robust under the harsher classes. (4) Certified: the map is expansive at the LRP (F′ = 1.153 > 1), so the contraction form is inapplicable and the expansive form empties every certified kernel beyond T = 5 years. The LRP is protected by good years, not by catch management.--

## 1. Introduction

After the 1992 moratorium, Northern cod (NAFO divisions 2J3KL) posed a clean governance question: can any catch policy hold a collapsed stock's spawning biomass above its limit reference point when productivity is depressed, or is the reference point protected by good years rather than by demand management? Viability analysis supplies the natural instrument for such questions — it asks which states admit controls that keep every constraint satisfied over time, rather than which policy maximizes an objective (Aubin, 1991), and it has been applied to fisheries in exactly this register: bioeconomic viability constraints (Béné, Doyen, and Gabay, 2001), viable recovery paths after collapse (Martinet, Thébaud, and Doyen, 2007), stochastic co-viability for ecosystem-based management (Doyen et al., 2012), and the numerical computation of viability kernels for fishery case studies (Krawczyk, Pharo, Serea, and Sinclair, 2013; Krawczyk and Pharo, 2013). This study answers the question by scoring rather than assertion.

The object is the governed surplus-production model fitted in a companion forecast-evaluation study (under separate review), which ended in a negative certificate, with last-value persistence unbeaten on out-of-sample RMSE. Here the same fitted model, on the primary assessment specification (the 1983–2015 NCAM M-shift SSB series of DFO, 2016, Table A2, with LRP 884.6 kt), is scored as a closed-loop governance object: robust viability kernels of the LRP for a declared catch-policy family under persistent productivity-shock floors, plus a certified layer that converts the declared model defect into a safety-margin erosion. The intervention protocol — object, defect declaration, disturbance classes, policy family, and retention rule — was frozen (dated 2026-08-26) before any kernel, boundary, replay, or retention score was computed; the frozen protocol document is archived with the analysis code. Section 2 states the methods; Section 3 reports the kernels, the two negative certificates, the constructive boundary, the certified layer, and the stress replay; Section 4 discusses limitations.

## 2. Methods

The governed object is the companion forecast-evaluation study's own stock-flow class,

$$S_{t+1}=\bigl[S_t+rS_t(1-S_t/K)-C_t+e_t\bigr]_+$$

(Allee term off), fitted by one-step least squares on 1983–2007 with annual landings (Schijns et al., 2021) — $r = 0.2369$, $K = 5000$ kt (pinned at its optimization bound; the series never approaches carrying capacity — a declared defect; the LRP-boundary results depend chiefly on the identified $r$). Fit residual SD 135.0 kt; defect declaration $\varepsilon = 460.0$ kt yr⁻¹ (the 1992 collapse transition); out-of-sample audit 2008–2015: maximum 47.1 kt, which does not exceed the declared defect (the groundwater object of the companion intervention study, by contrast, exceeds its declared defect out of sample). Safe set: the single declared threshold $K^* = \mathrm{LRP} = 884.6$ kt (the 1983–1989 mean of Table A2). No row is produced on the second assessment specification (the 1954–2024 extended xteNCAM series, LRP 276 kt); the 2023 LRP belongs to that specification and is not pooled.

The disturbance classes are persistent additive productivity floors from the fit-window residual distribution: the perpetual worst observed one-step shock (−460.0 kt yr⁻¹), the 5th-percentile class (−318.8), and the 10th-percentile class (−114.85). Because this object has no independent input channel (unlike the recharge series of the companion groundwater study), the disturbance classes and the defect declaration are the same measured quantity in two roles.

The governance family: BAU $C \equiv 5$ kt (moratorium-level inshore removals, the declared implementable use post-1992); flat caps $\rho\cdot 240$ kt with $\rho\in\{1.0, 0.75, 0.5, 0.25, 0.0\}$ (240, 180, 120, 60, 0 kt; every member is scored); S1, the DFO-2009 critical-zone rule (DFO, 2009) at a declared 60 kt cap (60 above the LRP, 0 below); and a cascade (60/30/5/0 kt at LRP/0.75·LRP/0.5·LRP/below, the sub-LRP stages being declared scenarios, not verified institutions). For each policy and disturbance class, the robust viability kernel is the set of initial SSB values from which the closed-loop path keeps the stock at or above the LRP under the persistent floor; Table 1 reports kernel lower boundaries at $T=1$ and $T=\infty$ ("empty" = no state is robustly viable). The term is used in its closed-loop reading — the robust positively invariant set of a fixed declared policy — not in the classical viability reading of Aubin (1991), which is existential over controls: no control choice enters the kernel computation, only the evaluation of declared rules under the disturbance floor, and the word is retained because the object answers the same question ("from which states can the constraint be held") in the policy-fixed form. A non-BAU policy is retained only if (a) its kernel is at least as protective as BAU's at every reading (compared on the kernel lower boundary; empty = worst), (b) it improves on BAU somewhere, and (c) at some reading where it improves, its mean allowed catch exceeds that of every at-least-as-protective flat cap.

The certified layer applies the defect-to-margin conversion in the form the fitted map admits: if the closed loop contracts with rate $a < 1$ on the safe domain, the erosion margin is $r_T = \varepsilon(1-a^T)/(1-a)$; otherwise the expansive form $r_T = \varepsilon(a_{\max}^T-1)/(a_{\max}-1)$ applies with $a_{\max} = \sup|F'|$ over the safe domain, and the certified kernel is the nominal kernel of $K^* + r_T$.

## 3. Results

### 3.1 Robust kernels (nominal)

**Table 1.** Lower boundaries of the robust viability kernels of the LRP (kt) under the declared catch-policy family and disturbance classes. The harsh-class rows read "empty" at every reported horizon, including $T=\infty$ — the infinite-horizon emptiness stated in Section 3.2 is recorded in the table, not only in prose, and holds for every policy, zero catch included.

| Policy | Worst, T=1 | q05, T=1 | q10, T=1 | q10, T=∞ |
|---|---:|---:|---:|---:|
| BAU (5 kt) | 1141.0 | 1016.5 | **884.6** | **884.6** |
| flat 240 kt | 1351.1 | 1224.4 | 1043.8 | empty |
| flat 180 kt | 1297.1 | 1171.0 | 991.2 | 2338.3 |
| flat 120 kt | 1243.4 | 1117.8 | 938.8 | 1363.0 |
| flat 60 kt / S1 / cascade | 1189.9 | 1064.9 | 886.7 | 900.3 |
| flat 0 kt | 1136.6 | 1012.1 | **884.6** | **884.6** |

Under the 10th-percentile class the moratorium (BAU) and zero catch hold the entire safe set $[884.6, 10^4]$ kt at every horizon. Every nonzero cap lifts the kernel's lower edge above the LRP — the 60-kt rules by 2.1 kt at $T=1$ and 15.7 kt at $T=\infty$. Under the perpetual-worst and 5th-percentile classes the infinite-horizon kernel is empty for every policy: the worst-case map has no positive fixed point for any catch level, zero included, because the maximum surplus $g_{\max} = rK/4 = 296$ kt yr⁻¹ lies below the persistent floor, so every trajectory declines monotonically. The critical-floor axis makes the qualification explicit: $\bar e = g_{\max} = 296$ kt yr⁻¹ at zero catch separates vacuous from informative classes, both harsh floors ($-460$ and $-318.8$) sit beyond it, and only the 10th-percentile class ($-114.85$) lies on the informative side — which is why the constructive boundary of Section 3.3 exists only for that class.

### 3.2 The two negative certificates

**Productivity.** Under the two harshest classes no catch policy — zero catch included — holds the LRP. This is the cod analogue of the institutional negative certificate found in the companion groundwater intervention study, here at the primary safe set and driven by productivity: the reference point is protected by good years, not by demand management.

**Selection.** Under the frozen retention rule, nothing is retained. The reactive rules S1 and the cascade fail clause (a): their 60-kt cap removes catch exactly where the moratorium already sits at 5 kt, so their kernels are strictly smaller at the boundary; they improve on BAU under no disturbance class. The companion groundwater evaluation retained its reactive rules at 3.3–50.6% higher permitted supply; this evaluation retains none. Which governance architecture justifies its additional structure is system-dependent — the framework's deliverable is the scored comparison, not a universal architecture verdict.

### 3.3 Constructive boundary

The maximal robust flat catch — the largest constant catch whose worst-case low equilibrium stays at or above the LRP — is **57.6 kt** under the 10th-percentile class (24% of the declared 240 kt family scaling — a scaling, not a historical mean, since the 1960s landings recorded by Schijns et al. (2021) run considerably higher; $g(K^*) - |e_{q10}| = 172.47 - 114.85 = 57.62$ kt yr⁻¹). Under the 5th-percentile and perpetual-worst classes it is zero: no positive catch is robust. This is certification geometry at one declared shock class, not a harvest rule.

Supply replays (mean allowed catch over the observed 1983–2006 states): BAU 5 kt; S1 10.0 kt (the critical-zone cut is active in 83% of observed years — the stock was below the LRP for almost the entire history, a fact about the collapsed-era estimation window, not about the rule's post-recovery supply properties, and the two regimes are not mixed); cascade 16.3 kt; flat-60 60 kt; flat-0 0 kt.

### 3.4 Certified layer: the expansion obstruction

The conversion needs the closed loop's contraction rate. Here $F'(S) = 1 + r(1-2S/K)$ is increasing as $S$ falls, and at the LRP $F'(K^*) = 1.153 > 1$: the governed surplus map is expansive at the declared safe set, contracting only above $K/2 = 2500$ kt — a stock level the series never approaches. The contraction form of the conversion is therefore inapplicable; the expansive form $r_T = \varepsilon(a_{\max}^T-1)/(a_{\max}-1)$ grows without bound ($r_1 = 460.0$, $r_2 = 990.5$, $r_3 = 1602.1$, $r_5 = 3120.5$, $r_8 = 6385.9$ kt), and the certified kernel — the nominal kernel of $K^*+r_T$ — is empty beyond **T = 5 years** for every policy, zero catch included. At $T=5$ the certified set is $[4005, 10^4]$ kt, above the entire observed range of the stock. On this object the binding obstruction to certified intervention claims is the expansion rate itself, not the defect magnitude — a failure mode qualitatively different from the companion groundwater object, where the governed map is contracting and the certified horizon is defect-bound to $T \le 3$ years.

### 3.5 Stress replay and classification

Closed-loop replay from the observed 1990 SSB (861.9 kt — already below the LRP, so the replay starts outside the safe set and is uncontrolled shock accounting rather than a kernel-membership test) with the observed 1991–1995 residuals: under every flat cap of 60 kt and larger, and under the cascade (whose 1990 stage prescribes 30 kt), the path is below the LRP already in 1991 (876.5 kt under the cascade, whose 30-kt stage engages only after the constraint is already lost and is therefore not scored as LRP protection); zero catch, business-as-usual, and S1 — which cuts catch to zero on observing the 1990 stock below the LRP — hold 1991 above the limit (906.5 kt for flat-0 and S1, 901.5 kt for BAU), yet every policy falls below it by 1992, zero catch exiting in the same year as business-as-usual (622.3 versus 611.5 kt; BAU reaches 366.3 kt by 1994). The crash is a productivity event, not a catch event — exactly the catch-insufficiency certificate of the companion forecast-evaluation study.

At the $T=5$ classification under the 10th-percentile class, only the 1980s peak years of the 33 observed states lie inside the nominal kernels — {1985, 1987, 1989} for the 60-kt rules and additionally 1988 for BAU; the entire post-1990 history and most of the 1980s are outside. Under the two harsher classes all 33 are outside.

## 4. Discussion

Two layers of negative content must be kept distinct. The productivity negative certificate (Section 3.2) is a robust-layer statement: under the perpetual-worst and 5th-percentile persistent floors, no catch policy — zero catch included — holds the LRP. The certified-layer emptiness beyond T = 5 years (Section 3.4) is a different statement, about the conversion's expansive form: the governed map's expansion rate (F′ = 1.153 at the LRP) empties every certified kernel beyond five years. Neither result paraphrases the other.

The expansion obstruction is also the contribution to the viability-methods record: the certified-layer machinery used in the companion studies assumes a contracting closed loop, and the by-catch fishery case that anchors kernel computation in the fisheries literature (Krawczyk et al., 2013) is likewise a contracting setting. This cod object is the first scored instance in which the contraction form is provably inapplicable at the declared safe set — the map's steepest growth occurs exactly where the stock is scarcest, at the boundary the governance question is about. For a collapsed stock below half its estimated carrying capacity, every governance statement that survives certification must therefore be time-bounded and expansion-bound, not defect-bound.

The map is one-pool surplus production on annual means — no age structure, migration, or survey catchability (the model-type limitations of the companion forecast-evaluation study carry over). $K$ is pinned at its optimization bound. The expansive classification at the LRP inherits that defect: $F'(K^*) = 1 + r(1 - 2K^*/K)$ exceeds 1 only while $K > 2K^* = 1769.2$ kt, so any data-supported $K$ below twice the LRP would make the closed loop contract at the boundary and restore the contraction form of the conversion; the expansion obstruction is therefore conditional on the bound-pinned carrying capacity, not on the identified $r$. The residual conflates productivity shock and model error (no observation-model separation). The closed loop observes the stock exactly at the decision instant; real governance operates under assessment lags (the one-year delay module of the companion forecast-evaluation study), so the reported kernels are upper bounds for a perfect-observation controller, and delay-aware kernels would be smaller or empty. The persistent-shock classes are deliberately harsh (a perpetual floor, not an independent draw); the 10th-percentile class is the mildest with non-vacuous content, and the harsh classes sit beyond the map's maximum surplus (Section 3.2), which is what makes their emptiness vacuous as a productivity statement. The retention rule's protective clause is structurally conservative toward the moratorium: any rule that harvests at or above the boundary is less protective at exactly those readings, and sub-boundary cuts cannot compensate on a threshold constraint because a violation is already fatal — the mechanism of Section 3.2, stated here as the rule's declared geometry rather than as an empirical verdict on reactive management. The Allee term is off throughout; depensation would only strengthen the negative certificates, and a one-row depensation sensitivity is a registered revision requirement. The safe set's upper edge ($10^4$ kt, twice $K$) is never approached and exists only so that kernels can be written $[s, \infty)$; the positive-part floor $[\cdot]_+$ never binds on any reported kernel path. Sub-LRP cascade stages are declared scenarios, not verified institutions. The certified layer is vacuous at observed stock levels. Nothing here promotes or demotes any forecast module, transfers numbers from an interval-verified linear template (a companion methodological study), or pools the extended xteNCAM series. The 57.6 kt boundary is not a quota recommendation; it is the analytic limit of robustness at one declared shock class.

## Data availability

The analysis is fully deterministic (no random components). All input data, analysis scripts, and result files are archived in the public repository at https://github.com/MIKEAA2020/general-sustainability. Re-executing the committed intervention runner regenerates both output files (the results archive and the kernel-boundary table); a verification re-execution in a fresh environment reproduced both files byte for byte. The flat-180-kt infinite-horizon boundary reported in Table 1 (2338.3 kt) is the converged fixed point of the infinite-horizon recursion, computed by a runner with the iteration cap raised to 20,000 and an explicit convergence assertion. The critical-zone rule and cascade vocabulary follows the DFO precautionary-approach framework (DFO, 2009); the SSB series and LRP are DFO (2016) Table A2; the catch series is Schijns et al. (2021).

## CRediT authorship contribution statement

[To be completed at submission.]

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## References

Aubin, J.-P., 1991. Viability Theory. Birkhäuser, Boston.

Béné, C., Doyen, L., Gabay, D., 2001. A viability analysis for a bio-economic model. Ecol. Econ. 36, 385–396.

DFO, 2009. A fishery decision-making framework incorporating the Precautionary Approach. Fisheries and Oceans Canada, Ottawa.

DFO, 2016. Stock Assessment of Northern cod (NAFO Divs. 2J3KL) in 2016. DFO Can. Sci. Advis. Sec. Sci. Advis. Rep. 2016/026.

Doyen, L., Thébaud, O., Béné, C., Martinet, V., Gourguet, S., Bertignac, M., Fifas, S., Blanchard, F., 2012. A stochastic viability approach to ecosystem-based fisheries management. Ecol. Econ. 75, 32–42.

Krawczyk, J.B., Pharo, A., 2013. Viability theory: an applied mathematics tool for achieving dynamic systems' sustainability. Math. Appl. 41, 97–126.

Krawczyk, J.B., Pharo, A., Serea, O.S., Sinclair, S., 2013. Computation of viability kernels: a case study of by-catch fisheries. Comput. Manag. Sci. 10, 365–396.

Martinet, V., Thébaud, O., Doyen, L., 2007. Defining viable recovery paths toward sustainable fisheries. Ecol. Econ. 64, 411–422.

Schijns, R., Froese, R., Hutchings, J.A., Pauly, D., 2021. Five centuries of cod catches in Eastern Canada. ICES J. Mar. Sci. 78, 2675–2683.

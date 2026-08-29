% TITLE: Does catch governance protect the limit reference point? An intervention-selection test on Northern cod (NAFO 2J3KL)
% VENUE: Fisheries Research (short communication)
% TYPE: Short communication (applied management analysis)
% RUNNING: Robust catch-policy kernels for Northern cod
% KEYWORDS: Northern cod; viability kernels; limit reference point; catch policy; robustness; intervention selection
% CONTRIBUTION: Robust-kernel policy scoring on the Northern cod series finds no catch policy retained: a 5-kt moratorium strictly dominates at the boundary, the productivity negative certificate holds the LRP under zero catch, and certified kernels are empty beyond T = 5 yr.

# Abstract

This study follows a preregistered retention rule: intervention selection must be scored, not asserted — a governance module is kept only if it improves a preregistered protection-and-supply outcome. The prediction leg on this stock — a companion forecast-evaluation study under separate review — ended in a negative certificate — a machine-verified finding of non-retention or certified non-existence, distinct from a statistical null result (persistence beats the surplus-production ladder). This paper runs the intervention leg on the same fixed series: robust viability kernels of the 2016 limit reference point (LRP, 884.6 kt) for a declared catch-policy family under persistent productivity-shock floors, with the erosion conversion — the device that converts a declared defect into a certified-kernel erosion margin from the closed loop's contraction rate — applied in the form the fitted map admits.

**Results.** (1) *Productivity negative certificate:* under the perpetual-worst and 5th-percentile persistent shock classes, no catch policy — zero catch included — holds the LRP: the worst-case map has no positive fixed point for any catch level, and every infinite-horizon kernel is empty. The LRP is protected by good years, not by catch management. (2) *Negative selection:* no declared policy is retained under the frozen rule; the reactive rules (the critical-zone rule and a cascade) are strictly less protective than the moratorium at the boundary and improve on it under no disturbance class — the mirror image of a companion intervention study on the Edwards Aquifer (under separate review), where the reactive architecture was retained. (3) *Constructive boundary:* the maximal robust flat catch is 57.6 kt (24% of the pre-1992 240 kt level) under the 10th-percentile class, and no positive catch is robust under the harsher classes. (4) *Certified layer:* the governed surplus map is expansive at the LRP (F′ = 1.153 > 1), so the contraction form of the erosion conversion is inapplicable; the expansive form empties every certified kernel beyond T = 5 years; on this object the binding obstruction to certified intervention claims is the expansion rate itself.

# 1. Introduction

After the 1992 moratorium, Northern cod (NAFO divisions 2J3KL) posed a clean governance question: can any catch policy hold a collapsed stock's spawning biomass above its limit reference point when productivity is depressed, or is the reference point protected by good years rather than by demand management? This study answers that question by scoring rather than assertion. It follows a preregistered retention rule under which a governance module is kept only if it improves a declared protection-and-supply outcome. The object is the governed surplus-production model fitted in a companion forecast-evaluation study (under separate review), which ended in a negative certificate, with last-value persistence unbeaten on out-of-sample RMSE. Here the same fitted model, on the primary assessment specification (Specification A, Ω_2016: the 1983–2015 NCAM M-shift SSB series of DFO 2016, Table A2, with LRP 884.6 kt), is scored as a closed-loop governance object: robust viability kernels of the LRP for a declared catch-policy family under persistent productivity-shock floors, plus a certified layer that converts the declared defect into an erosion margin. Section 2 states the object, disturbance classes, policy family, and retention rule; Section 3 reports the kernels, the two negative certificates, the constructive boundary, the certified layer, and the stress replay; Section 4 discusses limitations; data availability and references follow.

# 2. Methods

The governed object is the companion forecast study's own stock-flow (M2) class,

$$S_{t+1}=\bigl[S_t+rS_t(1-S_t/K)-C_t+e_t\bigr]_+$$

(Allee off), fit by one-step least squares on 1983–2007 with Schijns annual catch — $r = 0.2369$, $K = 5000$ (pinned at its optimization bound; the series never approaches carrying capacity — a declared defect; the LRP-boundary results depend chiefly on the identified $r$). Residual SD 135.0 kt; defect declaration $\varepsilon = 460.0$ kt yr$^{-1}$ (the 1992 collapse transition); out-of-sample audit 2008–2015: maximum 47.1 kt, which does not exceed the declared defect (the Edwards Aquifer object of the companion intervention study, by contrast, exceeds its declared defect out of sample). Safe set: the single declared threshold $K^* = \mathrm{LRP} = 884.6$ kt. No row is produced on the second assessment specification (Specification B, Ω_xte: the 1954–2024 extended xteNCAM series); the 2023 LRP belongs to that specification and is not pooled.

The disturbance classes are persistent additive productivity floors from the fit-window residual distribution: UC-min $=-460.0$ (the perpetual worst observed one-step shock), UC-q05 $=-318.8$, UC-q10 $=-114.8$ kt yr$^{-1}$. Because this object has no independent input channel (unlike the recharge series of the companion groundwater study), the disturbance classes and the defect declaration are the same measured quantity in two roles.

The governance family: BAU $C \equiv 5$ kt (moratorium-level inshore removals, the declared implementable use post-1992); flat caps $\rho\cdot 240$ kt with $\rho\in\{1.0, 0.75, 0.5, 0.25, 0.0\}$ (240, 180, 120, 60, 0 kt; every member is scored); S1, the DFO-2009 critical-zone rule (DFO 2009) at a declared 60 kt cap (60 above the LRP, 0 below); and a cpm cascade (60/30/5/0 kt at LRP/0.75LRP/0.5LRP/below — sub-LRP stages declared normative-threshold scenarios). For each policy and disturbance class, the robust viability kernel is the set of initial SSB values from which the closed-loop path keeps the stock at or above the LRP under the persistent floor; Table 1 reports kernel lower boundaries at $T=1$ and $T=\infty$ ("empty" = no state is robustly viable). A governance module is retained only if it is at least as protective as BAU everywhere, improves on BAU somewhere, and permits more catch than every matched flat cap. The intervention protocol — object, defect declaration, disturbance classes, policy family, and retention rule — was frozen (dated 2026-08-26) before any kernel, boundary, replay, or retention score was computed; the frozen protocol document is archived with the analysis code. The certified layer applies the erosion conversion in the form the fitted map admits.

# 3. Results

## 3.1 Robust kernels (nominal)

**Table 1.** Robust viability kernels of the LRP under the declared catch-policy family.

| Policy | UC-min $T{=}1$ | UC-q05 $T{=}1$ | UC-q10 $T{=}1$ | UC-q10 $T{=}\infty$ |
|---|---:|---:|---:|---:|
| BAU (5 kt) | 1141.0 | 1016.5 | **884.6** | **884.6** |
| flat 240 kt | 1351.1 | 1224.4 | 1043.8 | empty |
| flat 180 kt | 1297.1 | 1171.0 | 991.2 | 2338.3 |
| flat 120 kt | 1243.4 | 1117.8 | 938.8 | 1363.0 |
| flat 60 kt / S1 / cpm | 1189.9 | 1064.9 | 886.7 | 900.3 |
| flat 0 kt | 1136.6 | 1012.1 | **884.6** | **884.6** |

Lower boundaries of the robust kernels (kt); "empty" = no state is robustly viable. Under UC-q10 the moratorium (BAU) and zero catch hold the **entire** safe set $[884.6, 10^4]$ at every horizon. Every nonzero cap lifts the kernel's lower edge above the LRP — the 60 kt rules by 2.1 kt at $T=1$ and 15.7 kt at $T=\infty$. Under UC-min and UC-q05 the infinite-horizon kernel is empty for **every** policy: the worst-case map has no positive fixed point ($g_{\max} = rK/4 = 296$ kt yr$^{-1}$ is below the persistent floor), so every trajectory declines monotonically.

## 3.2 The two negative certificates

**Productivity.** Under UC-min/UC-q05 no catch policy — zero catch included — holds the LRP. This is the cod analogue of the institutional negative certificate found in the companion Edwards Aquifer intervention study, here at the primary safe set and driven by productivity: the reference point is protected by good years, not by demand management.

**Selection.** Under the frozen retention rule (at least as protective as BAU everywhere; improves somewhere; more catch than every matched flat cap) **nothing is retained**. S1/cpm fail clause (a): their 60 kt cap removes catch exactly where the moratorium already sits at 5 kt, so their kernels are strictly smaller at the boundary; they improve on BAU under no disturbance class. The companion Edwards Aquifer evaluation retained its reactive rules at 3.3–50.6% higher permitted supply; this evaluation retains none. Which governance architecture justifies its additional structure is system-dependent — the framework's deliverable is the scored comparison, not a universal architecture verdict.

## 3.3 Constructive boundary

The maximal robust flat catch — the largest constant catch whose worst-case low equilibrium stays at or below the LRP — is **57.6 kt** under UC-q10 (24% of the pre-1992 240 kt level; $g(K^*) - |e_{q10}| = 172.47 - 114.85 = 57.62$). Under UC-q05/UC-min it is zero: no positive catch is robust. This is certification geometry at one declared shock class, not a harvest rule.

Supply replays (mean allowed catch over the observed 1983–2006 states): BAU 5 kt; S1 10.0 kt (the critical-zone cut is active in 83% of observed years — the stock was below the LRP for almost the entire history); cpm 16.3 kt; flat-60 60 kt; flat-0 0 kt.

## 3.4 Certified layer: the expansion obstruction

The erosion conversion needs the closed loop's contraction rate. Here $F'(S) = 1 + r(1-2S/K)$ is **increasing as S falls**, and at the LRP $F'(K^*) = 1.153 > 1$: the governed surplus map is expansive at the declared safe set (it only contracts above $K/2 = 2500$ kt). The contraction form of the conversion is therefore **inapplicable**; the expansive form $r_T = \varepsilon(a_{\max}^T-1)/(a_{\max}-1)$ grows without bound ($r_1 = 460$, $r_5 = 3121$, $r_8 = 6386$ kt), and the certified kernel — the nominal kernel of $K^*+r_T$ — is empty beyond **T = 5 years** for every policy. At $T=5$ the certified set is $[4005, 10^4]$ kt, above the entire observed range of the stock. On this object the binding obstruction to certified intervention claims is the expansion rate itself, not the defect magnitude — a failure mode qualitatively different from the companion Edwards Aquifer object, where the governed map is contracting and the certified horizon is defect-bound to $T \le 3$ years.

## 3.5 Stress replay and classification

Closed-loop replay from the observed 1990 SSB (861.9 kt — already below the LRP) with the **observed** 1991–1995 residuals: under every flat cap of 60 kt and larger ($C\in\{60,120,180,240\}$ kt), and under the cascade (cpm, whose 1990 stage prescribes 30 kt), the path is below the LRP already in 1991 (876.5 kt under cpm); zero catch, business-as-usual (5 kt), and the critical-zone rule S1 — which cuts catch to zero on observing the 1990 stock below the LRP — hold 1991 above the limit (906.5 kt for flat-0 and S1, 901.5 kt for BAU) yet every policy falls below it by 1992 — zero catch exits in the same year as business-as-usual (622.3 versus 611.5 kt in 1992; BAU reaches 366.3 kt by 1994) — the crash is a productivity event, not a catch event, exactly as the companion prediction study's catch-insufficiency certificate found.

T=5 classification: under UC-q10 only the 1980s peak years of the 33 observed states lie inside the T=5 nominal kernels — $\{1985, 1987, 1989\}$ for the 60-kt rules (S1, cpm, flat-60) and, additionally, 1988 for BAU; the entire post-1990 history and most of the 1980s are outside. Under UC-min/UC-q05 all 33 are outside.

# 4. Discussion

Two layers of negative content must be kept distinct. The productivity negative certificate (Section 3.2) is a robust-layer statement: under the perpetual-worst and 5th-percentile persistent floors, no catch policy — zero catch included — holds the LRP. The certified-layer emptiness beyond T = 5 years (Section 3.4) is a different statement, about the erosion conversion's expansive form: the governed map's expansion rate (F′ = 1.153 at the LRP) empties every certified kernel beyond five years. Neither result paraphrases the other.

The map is one-pool surplus production on annual means — no age structure, migration, or survey catchability (the model-type limitations of the companion forecast study carry over). $K$ is pinned at its optimization bound. The residual conflates productivity shock and model error (no observation-model separation). The persistent-shock classes are deliberately harsh (a perpetual floor, not an i.i.d. draw); the UC-q10 class is the mildest with non-vacuous content. Sub-LRP cascade stages are declared normative-threshold scenarios, not verified institutions. The certified layer is vacuous at observed stock levels. Nothing here promotes or demotes any forecast module, transfers numbers from the interval-verified linear template (a companion methodological study), or pools the extended xteNCAM series.

# Data availability

The analysis is fully deterministic (no random components). All input data, analysis scripts, and result files are archived in the research programme's public repository at <https://github.com/MIKEAA2020/general-sustainability>; an anonymized copy is available for double-anonymous review. Re-executing the committed intervention runner (`run_intervention.py`) regenerates both output files, `results/intervention_results.json` and `results/intervention_boundaries.csv`; a verification re-execution in a fresh environment reproduced both files byte for byte. The flat-180-kt $T=\infty$ boundary reported in Table 1 (2338.3 kt) is the converged fixed point of the infinite-horizon recursion; an earlier committed table recorded its 300th backward iterate (2335.4 kt), and the recursion needs $\approx1456$ steps to converge. A corrected runner (`run_intervention_v2.py`; the iteration cap raised from 300 to 20,000 with an explicit convergence assertion) regenerates the results with that single entry changed, writing `results/intervention_results_v2.json` and `results/intervention_boundaries_v2.csv`; the original committed files are retained unchanged as the audited record. The critical-zone rule and cascade vocabulary follows the DFO precautionary-approach framework (DFO 2009); the SSB series and LRP are DFO (2016) Table A2; the catch series is Schijns et al. (2021).

# References

DFO. 2009. A fishery decision-making framework incorporating the Precautionary Approach.

DFO. 2016. Stock Assessment of Northern cod (NAFO Divs. 2J3KL) in 2016. CSAS Science Advisory Report 2016/026.

Schijns, R., et al. 2021. Five centuries of cod catches in Eastern Canada. *ICES Journal of Marine Science* 78: 2675–2683.

% TITLE: Governance operators and viability kernels of the Edwards Aquifer: an intervention-selection test at J-17
% VENUE: Journal of Water Resources Planning and Management
% TYPE: Applied management analysis
% RUNNING: Robust pumping-rule scoring, Edwards Aquifer
% KEYWORDS: drought triggers; critical-period management; robust viability; pumping policy; Edwards Aquifer
% CONTRIBUTION: Scored robust-kernel analysis of pumping-rule families on the J-17 record shows reactive critical-period rules deliver 3.3–16.2% more permitted supply at matched robust protection, with the cascade matching the deepest cut's protection at 50.6% more supply.

# Abstract

This study follows a preregistered retention rule: intervention selection must be scored, not asserted — a governance module is kept only if it improves a preregistered protection-and-supply outcome. This paper runs that test on the San Antonio Pool of the Edwards Aquifer at the J-17 index well: robust viability kernels of declared safe sets for a declared pumping-policy family, under persistent drought-floor recharge classes, with an erosion conversion — the device that converts a declared model defect into a certified-kernel erosion margin from the closed loop's contraction rate — applied in the contraction form the fitted one-pool affine map admits. The affine map is fitted by ordinary least squares on 1934–1990 and audited out of sample on 1991–2023; the governance family comprises business-as-usual pumping, flat caps, a Stage-I reactive rule, and a critical-period management (CPM) cascade.

**Results.** (1) *Physical threshold (618 ft, Comal cessation proximity):* under a perpetual drought-of-record floor, business-as-usual is not robustly viable (its nominal kernel empties beyond $T\approx13$ years; the $T=12$ boundary is 692.6 ft), every flat cut of 10% or deeper — and the two reactive rules — makes the whole declared safe set robustly invariant, and the smallest flat cut securing the threshold is 7.2% of mean pumping. (2) *Institutional threshold (660 ft, post-2007 Stage I):* a negative certificate — a machine-verified finding of non-retention or certified non-existence, distinct from a statistical null result — every declared policy's robust kernel equals business-as-usual's at every horizon, because the viable region lies strictly above the first trigger level; the institutional threshold is protected by wet years, not by the declared pumping family. (3) *Certified layer:* with the training-defect erosion applied, every demand-management policy's certified kernel is empty beyond $T=3$ years (zero pumping retains one through $T=4$ under the drought-of-record floor and $T=5$ under the milder floors) — the binding constraint on certified intervention claims is the model defect, not the governance. (4) *Positive selection:* the reactive rules are retained — the Stage-I rule matches the flat caps' robust invariance at 3.3–16.2% more permitted supply, and the cascade matches the deepest cut's protection at 50.6% more. A 1950s open-loop replay records the map's drought bias (8.1 ft, high) without correction. The paper's deliverable is the scored comparison on one measured system; no two-pool, karst, or solute claim is made.

# 1. Introduction

Drought management in permitted groundwater systems is built on triggers: index-well or springflow thresholds at which pumping reductions activate. Trigger design has a long evaluation literature — drought indicators and triggers are properly assessed as stochastic objects, with explicit attention to how indicator levels, trigger thresholds, and drought stages interact (Steinemann 2003) — and robustness has been a recurring concern of water-resources planning since the recognition that optimal solutions can be brittle to the hydrologic assumptions that produce them (Watkins and McKinney 1997). The operational question for a district that already operates triggers is narrower and comparative: given a declared family of pumping rules — business-as-usual, flat caps, and reactive trigger rules — which rules deliver protection under adverse recharge, and at what cost in permitted supply?

This study answers that question by scoring rather than assertion. It follows a preregistered retention rule under which a governance module is kept only if it improves a declared protection-and-supply outcome. Robust viability kernels — the sets of initial states from which the closed-loop system keeps the state inside a declared safe set under every disturbance in a declared class — are computed for each declared pumping rule under persistent drought-floor recharge classes; permitted supply is replayed on the observed head record; and a certified layer converts the fitted map's declared defect into an erosion margin. The complete comparison — object, defect declaration, disturbance classes, policy family, and retention rule — was frozen in a dated protocol (2026-08-26) before any score was computed.

We selected the Edwards (Balcones Fault Zone) Aquifer J-17 index well because its long (1934–2023) daily head record, its explicit institutional thresholds, and its management relevance make it a natural test bed for scored policy evaluation. The San Antonio Pool is a karst aquifer whose regional behavior has long been represented with lumped and equivalent-porous-media models (Scanlon et al. 2003); the scored object here is the simplest such representation, a one-pool affine head map fitted on the historical record.

The governance question is the intervention leg of a paired evaluation. A companion forecast-evaluation study (under separate review) scored prediction modules on the same J-17 series and ended in a negative certificate — persistence beats the causal ladder, and the oracle water-balance gap (7.55 ft against persistence's 13.23 ft; 7.55 ft against the retained AR(1)'s 12.84 ft) locates the unexplained forecast gap in the information layer. This study asks whether a declared governance operator changes the viability kernel of the real system, and at what cost in permitted supply.

The remainder of this article is organized as follows. Section 2 states the object, the fitted dynamics, the information pattern, the safe sets, and the governance family. Section 3 states the erosion conversion. Section 4 reports the results: worst-case attractors and the minimal cut (Section 4.1), nominal kernels (Section 4.2), certified kernels (Section 4.3), supply and retention (Section 4.4), and classification and stress replays (Section 4.5). Section 5 interprets the findings, Section 6 states the limitations, and data and code availability and the references close the paper.

# 2. Object, dynamics, information

The object is that of the companion forecast evaluation: J-17 annual-mean head $z_t$ (ft AMSL), San Antonio Pool, 1934–2023, from the fixed twenty-column analysis panel (`data/annual_panel.csv`). $z$ is a measured well level, not an assessment inversion. Recharge $R$ (USGS/EAA estimated) and pumpage $P$ (EAA Table 1, San Antonio Pool wells) are the fluxes. No new data.

Dynamics: the causal stock-flow class of the companion forecast study (its M2), one pool, affine —

$$
\Delta H_t = \alpha + \beta R_t + \gamma P_t + \delta H_{t-1},
$$

fitted by OLS on 1934–1990 (56 transitions). OLS fit: $\alpha = 163.49$, $\beta = 0.0198$ ft per $10^3$ acre-ft, $\gamma = -0.02844$ ft per $10^3$ acre-ft, $\delta = -0.2539$, $a = 1+\delta = 0.7461$ — a contraction with a 25.4%-per-year mean reversion. Residual SD 5.60 ft, max 15.41 ft (training). Out-of-sample (1991–2023, audit only): SD 8.40, max 21.81 ft.

Information pattern: the manager ends year $t$ knowing $(H_t, R_t, P_t)$ and sets $P_{t+1} = \pi(H_t)$; $R_{t+1}$ is unknown at decision time and is treated adversarially within a declared persistent floor (UC-min = 43.7, UC-q05 = 166.5, UC-q10 = 179.1 $10^3$ acre-ft yr$^{-1}$ — the drought-floor recharge classes; the 1956 drought-of-record year is UC-min). These floors are certification geometry — the persistent floor regimes are harsher than any single recorded year (UC-min is the recorded 1956 minimum, held perpetually) — not recharge forecasts.

Safe sets (both declared normative thresholds, fixed in the frozen protocol): $K^*_{\mathrm{phys}} = 618$ ft (Comal cessation proximity) and $K^*_{\mathrm{inst}} = 660$ ft (post-2007 Stage I trigger; not applied to pre-2007 history).

Governance family: BAU ($P \equiv \bar P = 282.16$, training mean); flat caps $\rho\bar P$, $\rho \in \{0.9, 0.8, 0.7, 0.6, 0.5, 0\}$; the Stage-I reactive rule (20% cut when $H < 660$, the reduction verified against the Authority's published rule); and a critical-period management (CPM) cascade (cumulative 20/30/35/40% cuts at $H < 660/650/640/630$ — Stage I verified, stages II–IV declared normative-threshold scenarios).

# 3. Erosion conversion (discrete-contraction form)

With uniform defect $\varepsilon = 15.41$ ft (the training maximum) and contraction $a = 0.7461$, trajectory deviation over $T$ years is bounded by $r_T = \varepsilon (1-a^T)/(1-a)$: $r_1 = 15.41$, $r_3 = 35.49$, $r_5 = 46.66$, $r_\infty = 60.70$ ft. The certified kernel at horizon $T$ is the nominal kernel of $K^* + r_T$. The out-of-sample defect max (21.81 ft) **exceeds** the declared $\varepsilon$: the certified rows below are optimistic out-of-window; this is recorded, and no refitting is performed, per protocol.

# 4. Results

## 4.1 Worst-case attractors and the minimal cut

The worst-case (UC floor) attractor of the closed loop, by policy:

| Policy | UC-min | UC-q05 | UC-q10 |
|---|---:|---:|---:|
| BAU | 615.72 | 625.31 | 626.29 |
| flat-90% | 618.88 | 628.47 | 629.45 |
| flat-80% | 622.04 | 631.63 | 632.61 |
| S1 (reactive 20% < 660) | 622.04 | 631.63 | 632.61 |
| flat-70% | 625.20 | 634.79 | 635.77 |
| CPM cascade | 628.36 | 636.37 | 637.35 |
| flat-60% | 628.36 | 637.95 | 638.93 |
| flat-50% | 631.52 | 641.11 | 642.09 |
| flat-0 (zero pumping) | 647.32 | 656.91 | 657.90 |

Under a perpetual 1956-recharge floor, BAU's attractor (615.72 ft) sits **below** the physical threshold; the smallest flat cut whose attractor clears 618 ft is **7.2%**. The Stage-I reactive rule's attractor equals flat-80%'s (the cut is active on the entire attractor branch).

## 4.2 Nominal kernels (no erosion)

Under the physical threshold (618 ft) and UC-min, BAU's kernel boundary climbs 618.8 (T=1) → 625.6 (T=5) → 658.4 (T=10) and the kernel is **empty** beyond $T \approx 13$ years — the $T=12$ boundary is 692.6 ft and the $T=13$ kernel is empty (the continuous crossover is 12.7 under the same convention used for the zero-pumping horizons below) — BAU is not robustly viable against a perpetual drought-of-record. Every cut policy in the family (a 10% flat cap, S1, CPM, and deeper) makes $[618, 710]$ **robustly invariant**: the whole declared safe set is the kernel at every horizon, including the infinite horizon. Under UC-q05/q10 the safe set is already invariant at BAU (attractors 625.3 / 626.3 ft): governance differentiates the kernel only under the drought-floor class.

Under the institutional threshold (660 ft): **negative certificate.** Every declared policy's robust kernel equals BAU's at every horizon — the boundaries (675.1 at T=1, 695.3 at T=2 under UC-min; empty from T=3) lie strictly above the first-stage CPM trigger (660 ft — the highest of the four declared trigger levels, and therefore the easiest to reach), so no declared demand-management rule activates in the viable region and the kernel is policy-invariant. Demand management extends **the viable horizon, not invariance**: even zero pumping has an empty nominal kernel beyond $T \approx 6$ (UC-min) / $T \approx 11$ (UC-q10), because its worst-case attractor (647.3 / 657.9 ft) still sits below 660 ft. The institutional threshold is protected by wet years, not by the declared pumping family — which is exactly the frequency-management rationale the actual CPM rule implements, and that rationale is outside the robust-kernel frame.

## 4.3 Certified kernels (eroded)

With the erosion of Section 3 applied, every demand-management policy in the family has an empty certified kernel beyond $T = 3$ years at the physical threshold and beyond $T = 1$ year at the institutional threshold. Zero pumping is the exception: its certified physical-threshold kernel is nonempty through $T = 4$ under UC-min (lower boundary $\approx687.9$ ft from the affine certified-kernel algebra; the committed horizon grid $\{1,2,3,5,8,10,15,20,\infty\}$ does not sample $T=4$, so the archived $T=\infty$ emptiness is consistent with the analytic boundary exceeding the domain top at $T=5$) and through $T = 5$ under UC-q05/q10 (physical threshold only). The certified boundaries at T=3 / UC-min / 618 ft: flat-0 662.2 < flat-80 697.8 < BAU = S1 = CPM 706.7. The binding constraint on certified intervention claims is the **model defect, not the governance** — the information-layer limitation identified by the companion forecast evaluation, here measured on the intervention leg.

## 4.4 Supply and retention

Mean prescribed pumping (actual-head replay, 1934–1990):

| Policy | Supply ($10^3$ acre-ft yr$^{-1}$) | Cut active |
|---|---:|---:|
| BAU | 282.16 | 0% |
| flat-90% | 253.94 | 100% |
| flat-80% | 225.73 | 100% |
| flat-70% | 197.51 | 100% |
| **S1** | **262.36** | 35.1% |
| **CPM** | **254.93** | 35.1% |
| flat-60% | 169.29 | 100% |
| flat-50% | 141.08 | 100% |

Out-of-sample replay (1991–2023, audit only): S1 264.5 and CPM 260.6 $10^3$ acre-ft yr$^{-1}$; every flat policy prescribes its cap throughout, so the training and out-of-sample supplies coincide.

Retention rule (frozen): at least as protective as BAU everywhere, and more water than the most protective flat cap with matched protection.

- **S1: RETAINED (nominal, under UC-min at the 618 ft threshold).** It matches the flat caps' robust invariance (kernel = whole safe set, all horizons) while supplying 262.4 vs flat-90%'s 253.9 (**+8.4 $10^3$ acre-ft yr$^{-1}$, +3.3%**) and flat-80%'s 225.7 (+36.6, +16.2%). The reactive architecture justifies its additional structure: the same protection at strictly more permitted supply.
- **CPM: RETAINED (nominal, same threshold and class).** Attractor 628.4 (equal to flat-60%'s) at supply 254.9 vs flat-60%'s 169.3 (+50.6%).
- **Certified level:** S1 and CPM remain retained against their dominating flat caps (S1 vs flat-80: +36.6 supply at every certified horizon; CPM vs flat-60: +85.6), but only over the $T \le 3$ horizons where their certified kernels are nonempty.
- **Under the institutional threshold: nothing retained** (all policies ≡ BAU).

## 4.5 Classification and stress replays

T=5 nominal kernel (UC-min, 618 ft): BAU excludes exactly one actual year from its viable set — **1956**, the drought-of-record year (623.15 ft annual mean). S1 and CPM exclude none: the entire 90-year actual record is robustly 5-year viable under the cut rules. The T=5 **certified** kernels are empty, so no actual year is certified 5-year viable under any policy; this is the boundary of the certified analysis.

1950s open-loop diagnostic (model with actual $R, P$ vs actual heads, 1951–1956): the affine map under-predicts the drought decline — model 659.5 → 631.3 vs actual 659.5 → 623.2, max error 8.1 ft, biased high. The 1950s model-based policy replays (from the observed 1950 head) keep all policies above 618 ft (BAU min 629.7, S1 634.9, CPM 637.1), but the open-loop bias means the true margins are smaller than the replay suggests; this is recorded, and no correction is applied.

# 5. Interpretation

The complete evaluation loop — measured state, calibrated stock-flow map, declared governance operators, declared uncertainty classes, viability kernels with explicit declared-defect erosion, held-out defect audit, and a fixed retention rule — yields a **positive selection result**: the reactive architecture matches flat-cap protection at 3–50% more permitted supply, and a 7.2% mean cut secures the physical threshold against a perpetual drought-of-record where BAU fails. It also yields two negative findings: the institutional threshold is not demand-manageable to invariance under the declared classes, and the certified content is defect-bound to $T \le 3$ years. The unexplained forecast gap lies again in the information layer: the erosion bound absorbs the oracle gap measured against the retained AR(1) baseline (12.84 versus 7.55 ft).

Two layers of results must be kept distinct. The robust-kernel findings are statements about the declared pumping family under the declared floor classes: business-as-usual is not robustly viable beyond $T\approx13$ years under the perpetual-1956 floor (the $T=12$ boundary is 692.6 ft), every cut policy makes the whole declared safe set robustly invariant at the physical threshold, and the institutional-threshold negative certificate holds for every declared policy. The certified-kernel findings are a different layer, produced by applying the erosion conversion to the declared training defect: with $\varepsilon = 15.41$ ft (exceeded out of sample at 21.81 ft), every demand-management policy's certified kernel is empty beyond $T=3$ years. Neither layer's claims paraphrase the other; in particular, the certified emptiness is a bound on what the fitted map can certify, not a robustness statement about the physical system.

# 6. Limitations

Nominal kernels carry no defect margin; certified kernels use a training defect that the out-of-sample audit exceeds (15.4 vs 21.8 ft). The map is one-pool affine on annual means; the actual CPM triggers are 10-day averages, so the annual-mean rule is a coarse relative of the real institution. Stage II–IV reductions are declared scenarios, not verified. San Antonio + Uvalde are lumped (inherited defect). Observation error is not separated from model defect. The UC floors are certification geometry, not forecasts; the 1950s replay is biased high by 8.1 ft. Nothing in this leg promotes or demotes any forecast module, and no two-pool, karst, or solute claim is made.

# Data and code availability

All input data, analysis scripts, and result files are archived in the research programme's public repository at <https://github.com/MIKEAA2020/general-sustainability>; an anonymized copy is available for double-anonymous review. J-17 daily highs: Texas Water Development Board well 6837203. Recharge: Umphres and Choi (2025), DOI 10.5066/P1BI62NY. Pumpage: Edwards Aquifer Authority (2024/25), Table 1. The full intervention protocol — object, defect declaration, disturbance classes, policy family, and retention rule — was frozen and dated (2026-08-26) before any kernel, boundary, replay, or retention score was computed; it is archived with the analysis code as the preregistration record, alongside the companion forecast-evaluation protocols dated 2026-08-25.

```
python3 src/run_intervention.py
```

The analysis is fully deterministic (no random components). Re-executing the committed runner regenerates both output files, `results/intervention_results.json` and `results/intervention_boundaries.csv`; a verification re-execution in a fresh environment reproduced both files byte for byte. The machine-readable outputs include the fields `retention` (nominal), `retention_certified`, and `certified_horizon_nonempty` in the JSON. A corrected runner (`src/run_intervention_v2.py`) fixes the retention comparator's treatment of empty kernels (an empty kernel now counts as worst on both sides, matching the companion study's convention; the earlier asymmetric comparator was mechanically verified inert for these artifacts) and writes `results/intervention_results_v2.json` and `results/intervention_boundaries_v2.csv`, value-identical to the committed outputs; the committed original files are retained unchanged as the audited record.

# References

Edwards Aquifer Authority. 2024/25. *2023 Groundwater Discharge and Usage*. Table 1, after USGS letter report 5 April 2024. <https://www.edwardsaquifer.org/wp-content/uploads/2025/05/2023-Groundwater-Discharge-and-Usage.pdf>

Edwards Aquifer Authority. Critical Period / Drought Management. <https://www.edwardsaquifer.org/groundwater-users/critical-period-drought-management/>

Puente, C. 1978. *Method of estimating natural recharge to the Edwards Aquifer in the San Antonio area, Texas.* U.S. Geological Survey.

Scanlon, B. R., Mace, R. E., Barrett, M. E., and Smith, B. 2003. Can we simulate regional groundwater flow in a karst system using equivalent porous media models? Case study, Barton Springs Edwards aquifer, USA. *Journal of Hydrology* 276: 137–158.

Steinemann, A. C. 2003. Drought indicators and triggers: a stochastic approach to evaluation. *Journal of the American Water Resources Association* 39: 1217–1233.

Texas Water Development Board. Water Data for Texas, well 6837203 (J-17). <https://waterdatafortexas.org/groundwater/well/6837203>

Umphres, G. D., and Choi, N. J. 2025. Estimated Annual Recharge to the Edwards Aquifer in the San Antonio Area, by Stream Basin or Ungaged Area, 1934–2024. U.S. Geological Survey data release. <https://doi.org/10.5066/P1BI62NY>

Watkins, D. W., Jr., and McKinney, D. C. 1997. Finding robust solutions to water resources problems. *Journal of Water Resources Planning and Management* 123: 49–58.

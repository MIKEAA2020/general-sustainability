# Governance operators and viability kernels of the Edwards Aquifer: an intervention-selection test at J-17

**Prepared in the format of Groundwater (Wiley/NGWA)**

## Abstract
Drought management in permitted groundwater systems is built on triggers — thresholds at which pumping reductions activate. This study follows a preregistered retention rule: a governance module is kept only if it improves a declared protection-and-supply outcome, with the protocol frozen before any score is computed. Robust viability kernels of the J-17 index-well head (San Antonio Pool, Edwards Aquifer) are computed for a declared pumping-policy family under persistent drought-floor recharge classes. Four results follow. (1) At the 618-ft physical threshold, business-as-usual is not robustly viable against a perpetual worst-year floor — harsher than any single recorded year: its kernel empties beyond about 13 years, while every flat cut of 10% or deeper — and both reactive rules — makes the whole safe set robustly invariant; the smallest securing cut is 7.2%. (2) At the 660-ft institutional threshold, a negative certificate holds: the reactive rules are invisible to the viability kernel of their own trigger constraint, the flat caps move finite-horizon boundaries and extend the viable horizon without achieving invariance, and the threshold is protected by wet years, not by the declared pumping family. (3) The certified layer is defect-bound: every demand-management policy with positive pumping has an empty certified kernel beyond T = 3 years; zero pumping extends the certified horizon to T = 4–5. (4) Positive selection at the nominal level: the reactive rules are retained, matching flat-cap protection at 3.3–16.2% more permitted supply (Stage I) and 50.6% more (cascade) — worst-case protection at historical-mean entitlement.--

## 1. Introduction

Drought management in permitted groundwater systems is built on triggers: index-well or springflow thresholds at which pumping reductions activate. Trigger design has a long evaluation literature — drought indicators and triggers are properly assessed as stochastic objects, with explicit attention to how indicator levels, trigger thresholds, and drought stages interact (Steinemann 2003) — and robustness has been a recurring concern of water-resources planning since the recognition that optimal solutions can be brittle to the hydrologic assumptions that produce them (Watkins and McKinney 1997). The operational question for a district that already operates triggers is narrower and comparative: given a declared family of pumping rules, which rules deliver protection under adverse recharge, and at what cost in permitted supply?

The Edwards (Balcones Fault Zone) Aquifer of south-central Texas is the most fully institutionalized example of trigger-based groundwater governance in North America. Its critical-period management program stages pumping reductions at index-well thresholds to protect springflow at Comal and San Marcos Springs, whose endangered-species requirements are administered through the Edwards Aquifer Habitat Conservation Plan, the subject of a standing scientific review by the National Academies (National Research Council 2015). The aquifer's regional behavior has long been represented — and debated — through lumped and equivalent-porous-media models, from the Barton Springs groundwater availability model (Scanlon et al. 2003) to its recalibration by the Texas Water Development Board (Hutchison and Hill 2011). This study scores, rather than asserts, the protection supplied by a declared family of pumping rules on the measured J-17 record.

The instrument is the robust viability kernel: the set of initial heads from which a closed-loop pumping rule keeps the system inside a declared safe set under every disturbance in a declared class. Viability methods have an established lineage in natural-resource management, where constraints rather than objectives define the policy question (Krawczyk and Pharo 2013), and their computational tractability on management-scale problems is documented by fishery case studies (Krawczyk et al. 2013). Here the governed object is the one-pool affine head map fitted in a companion forecast-evaluation study on the same series (under separate review). That study ended in a negative certificate — a machine-verified non-retention finding, distinct from a statistical null result — with last-value persistence unbeaten by the causal ladder, and it located the unexplained forecast gap in the information layer: given realized recharge and pumpage, the map reaches 7.55-ft RMSE against persistence's 13.23 ft and the retained AR(1)'s 12.84 ft. This study asks the governance question the forecast study could not: whether a declared pumping rule changes the viability kernel of the real system, and at what cost in permitted supply.

The complete comparison — object, defect declaration, disturbance classes, policy family, and retention rule — was frozen in a dated protocol (2026-08-26) before any score was computed. A companion intervention study on a marine fishery stock (Northern cod) applies the same design and reaches the mirror verdict; the two systems' scores are never pooled.

## 2. Methods

### 2.1 Object and dynamics

The object is that of the companion forecast evaluation: J-17 annual-mean head z_t (ft above mean sea level), San Antonio Pool, 1934–2023, from the committed twenty-column analysis panel. z is a measured well level, not an assessment inversion. Recharge R (USGS-estimated, Puente method; Umphres and Choi 2025) and pumpage P (Edwards Aquifer Authority Table 1) are the fluxes. No new data.

Dynamics: the causal stock-flow class of the companion forecast study, one pool, affine,

$$\Delta H_t = \alpha + \beta R_t + \gamma P_t + \delta H_{t-1},$$

fitted by ordinary least squares on 1934–1990 (56 transitions). The fit is α = 163.49, β = 0.0198 ft per 10³ acre-ft, γ = −0.02844 ft per 10³ acre-ft, δ = −0.2539, so a = 1 + δ = 0.7461 — a contraction with 25.4% per year mean reversion. Residual SD 5.60 ft; training maximum 15.41 ft. Out-of-sample (1991–2023, audit only, no refitting): SD 8.40 ft, maximum 21.81 ft — which exceeds the declared defect, a fact recorded below and not repaired, per protocol.

Information pattern: the manager ends year t knowing (H_t, R_t, P_t) and sets P_{t+1} = π(H_t); R_{t+1} is unknown at decision time and is treated adversarially within a declared persistent floor.

### 2.2 Uncertainty classes and safe sets

The disturbance classes are persistent recharge floors computed on the training window: UC-min = 43.7 (the 1956 drought-of-record year, held perpetually), UC-q05 = 166.5, UC-q10 = 179.1 × 10³ acre-ft yr⁻¹. The persistent-floor regimes are harsher than any single recorded year; they are certification geometry, not recharge forecasts.

The safe sets are the two declared normative thresholds, fixed in the frozen protocol: K*_phys = 618 ft (Comal Springs cessation proximity) and K*_inst = 660 ft (the post-2007 Stage I trigger, not applied to pre-2007 history). The model domain is [610, 710] ft; upward exits above 710 ft are model-domain exits, not threshold violations.

### 2.3 Governance family

Business-as-usual (BAU) holds pumping at the training mean, P ≡ P̄ = 282.16 × 10³ acre-ft yr⁻¹. Flat caps prescribe ρP̄ with ρ ∈ {0.9, 0.8, 0.7, 0.6, 0.5, 0}. The Stage-I reactive rule (S1) cuts pumping 20% when H < 660 ft (the reduction verified against the Authority's published rule). The critical-period-management (CPM) cascade prescribes cumulative stage totals of 20/30/35/40% cuts at H < 660/650/640/630 ft (cumulative, not stacked); Stage I is verified, and stages II–IV are declared scenarios, not verified institutions. The CPM supply figure below uses the observed Stage-I occupancy; the Stage II–IV occupancies that would make the deeper cuts bite are not separately recorded, and the cascade supply value carries that disclosure.

For each policy and disturbance class, the robust T-step viability kernel of the safe set is computed by iterating the worst-case closed loop; the nominal kernel is reported without erosion, and the certified layer applies the defect-to-margin conversion in the form the fitted map admits.

### 2.4 Retention rule and certified layer

A non-BAU policy is retained only if its robust kernel is at least as protective as BAU's at every reading (compared on the kernel lower boundary; empty = worst) and it permits more pumping than the most protective flat cap with matched protection. The scoring regimes are declared here rather than left implicit: **protection is scored under the disturbance classes** (the perpetual floors of Section 2.3), and **supply is scored as the 1934–1990 historical replay mean** — the retention verdict is therefore a hybrid, worst-case protection at historical-mean entitlement, not a within-scenario dominance, and under the floor classes alone the reactive rules are identically their matched flat caps (the cut is active every year) and carry no supply margin. When several flat caps share the same kernel, "most protective with matched protection" is resolved as the largest-supply member of the matched class. The retention decision is made at the nominal level and re-checked at the certified level, and the certified re-check holds only over the horizons where the certified kernels are nonempty — a horizon-truncated object, stated as such whenever it is invoked.

The certified layer converts the declared uniform defect ε = 15.41 ft (the training maximum) into an erosion margin using the closed loop's contraction rate a = 0.7461: r_T = ε(1 − a^T)/(1 − a), giving r₁ = 15.41, r₃ = 35.49, r₅ = 46.66, r_∞ = 60.70 ft. The certified kernel at horizon T is the nominal kernel of K* + r_T.

## 3. Results

### 3.1 Worst-case attractors and the minimal cut

**Table 1.** Worst-case attractors of the closed loop (ft), by policy and recharge floor.

| Policy | UC-min | UC-q05 | UC-q10 |
|---|---:|---:|---:|
| BAU | 615.72 | 625.31 | 626.29 |
| flat-90% | 618.88 | 628.47 | 629.45 |
| flat-80% | 622.04 | 631.63 | 632.61 |
| S1 (20% cut < 660 ft) | 622.04 | 631.63 | 632.61 |
| flat-70% | 625.20 | 634.79 | 635.77 |
| CPM cascade | 628.36 | 636.37 | 637.35 |
| flat-60% | 628.36 | 637.95 | 638.93 |
| flat-50% | 631.52 | 641.11 | 642.09 |
| flat-0 (zero pumping) | 647.32 | 656.91 | 657.90 |

Under a perpetual 1956-recharge floor, BAU's attractor (615.72 ft) sits below the physical threshold; the smallest flat cut whose attractor clears 618 ft is **7.2%** of mean pumping. The Stage-I reactive rule's attractor equals flat-80%'s (the cut is active on the entire attractor branch).

### 3.2 Nominal kernels

At the physical threshold (618 ft) under UC-min, BAU's kernel boundary climbs 618.8 (T = 1) → 625.6 (T = 5) → 658.4 (T = 10), and the kernel is **empty** beyond T ≈ 13 years — the T = 12 boundary is 692.6 ft (continuous crossover 12.7 years), and the emptiness is a domain-top event: the boundary reaches the declared safe-set ceiling (710 ft), above which no state is scored, rather than an attractor event. Business-as-usual is not robustly viable against a perpetual drought-of-record. Every cut policy in the family — a 10% flat cap, S1, CPM, and deeper — makes [618, 710] **robustly invariant**: the whole declared safe set is the kernel at every horizon, including the infinite horizon. Under UC-q05/UC-q10 the safe set is already invariant at BAU (attractors 625.3/626.3 ft): governance differentiates the kernel only under the drought-floor class.

At the institutional threshold (660 ft) the result is a **negative certificate**, and the kernel-invariance statement must be split by policy class. For the **reactive rules** (S1, CPM) the equality with BAU is exact at every horizon: the boundaries (675.1 at T = 1, 695.3 at T = 2 under UC-min; empty from T = 3) lie strictly above the first-stage trigger (660 ft, the highest — and therefore easiest to reach — of the four declared trigger levels), so no reactive rule fires in the viable region and the kernel is policy-invariant for them. That equality is an institutional design fact, not a drought fact: a trigger placed on the boundary of a constraint is invisible to the viability kernel of that same constraint, and no rule that cuts only below 660 ft can improve the invariance of {H ≥ 660}. For the **flat caps** the equality is false: they move the finite-horizon boundaries (flat-80% reads ≈673 at T = 1 against BAU's 675.1) and extend the viable horizon — zero pumping has an empty nominal kernel only beyond T ≈ 6 (UC-min) / T ≈ 11 (UC-q10), because its worst-case attractor (647.3/657.9 ft) still sits below 660 ft. Demand management therefore extends the viable **horizon, not invariance**, and the 660-ft certificate states that the threshold is protected by wet years, not by the declared pumping family — which is exactly the frequency-management rationale the actual CPM rule implements, and that rationale is outside the robust-kernel frame.

### 3.3 Certified kernels

With the erosion of Section 2.4 applied, every demand-management policy in the family has an empty certified kernel beyond **T = 3 years** at the physical threshold and beyond T = 1 year at the institutional threshold. Zero pumping is the exception: its certified physical-threshold kernel is nonempty through T = 4 under UC-min (lower boundary ≈687.9 ft from the certified-kernel algebra; the committed horizon grid {1, 2, 3, 5, 8, 10, 15, 20, ∞} does not sample T = 4, so the archived infinite-horizon emptiness is consistent with the analytic boundary exceeding the domain top at T = 5) and through T = 5 under UC-q05/UC-q10. The certified boundaries at T = 3, UC-min, 618 ft: flat-0 662.2 < flat-80 697.8 < BAU = S1 = CPM 706.7 ft. The certified-level inference is drawn explicitly: at the one certified horizon tabulated, the reactive rules inherit BAU's boundary (706.7) — strictly above flat-80%'s (697.8) — so certified dominance of S1 over its matched flat cap fails, the +3.3%/+16.2% supply margins are nominal-level comparisons, and certified retention is a different, horizon-truncated object from nominal retention (Section 2.4). The binding constraint on certified intervention claims is the **model defect, not the governance** — the information-layer limitation identified by the companion forecast evaluation, here measured on the intervention leg.

### 3.4 Supply and retention

**Table 2.** Mean prescribed pumping (actual-head replay, 1934–1990) and cut-active fraction.

| Policy | Supply (10³ acre-ft yr⁻¹) | Cut active |
|---|---:|---:|
| BAU | 282.16 | 0% |
| flat-90% | 253.94 | 100% |
| flat-80% | 225.73 | 100% |
| flat-70% | 197.51 | 100% |
| S1 | **262.36** | 35.1% |
| CPM | **254.93** | 35.1% |
| flat-60% | 169.29 | 100% |
| flat-50% | 141.08 | 100% |

Out-of-sample replay (1991–2023, audit only): S1 264.5 and CPM 260.6 × 10³ acre-ft yr⁻¹; every flat policy prescribes its cap throughout, so its training and out-of-sample supplies coincide.

- **S1: retained (nominal, UC-min, 618 ft).** It matches the flat caps' robust invariance (kernel = whole safe set at all horizons) while supplying 262.36 versus flat-90%'s 253.94 (+8.4 × 10³ acre-ft yr⁻¹, **+3.3%**) and flat-80%'s 225.73 (+36.6, **+16.2%**). The scoring regimes are the hybrid declared in Section 2.4 — protection under the perpetual worst-year recharge floor, supply as the 1934–1990 historical replay mean — and the reading of the retention is exactly "worst-case protection at historical-mean entitlement," not a within-scenario dominance: under the floor itself S1 is identically flat-80% (the cut is active every year, and its floor-attractor supply equals flat-80%'s), so the supply margin exists only in wet years that the robust class excludes, and against flat-90% the floor comparison is the sharper one — S1 is always −20% where flat-90% is always −10%, at identical invariance. The reactive architecture justifies its additional structure on the hybrid criterion, not on the robust criterion alone.
- **CPM: retained (nominal, same threshold and class).** Attractor 628.36 ft (equal to flat-60%'s) at supply 254.93 versus flat-60%'s 169.29 (**+50.6%**).
- **Certified level:** S1 and CPM remain retained against their dominating flat caps (S1 versus flat-80: +36.6 supply at every certified horizon; CPM versus flat-60: +85.6), but only over the T ≤ 3 horizons where their certified kernels are nonempty.
- **Institutional threshold: nothing retained.** The reactive rules are identically BAU at every horizon (trigger-on-boundary invisibility, Section 3.2); the flat caps are more protective at finite horizons and extend the viable horizon, and no policy meets the retention test there.

### 3.5 Classification and stress replays

The T = 5 nominal kernel (UC-min, 618 ft): BAU excludes exactly one actual year from its viable set — 1956, the drought-of-record year (623.15 ft annual mean). S1 and CPM exclude none: the entire 90-year actual record is robustly 5-year viable under the cut rules. The T = 5 certified kernels are empty, so no actual year is certified 5-year viable under any policy; this is the boundary of the certified analysis.

A 1950s open-loop diagnostic (model driven by actual R, P versus actual heads, 1951–1956) records the map's drought bias: the affine map under-predicts the decline, model 659.5 → 631.3 versus actual 659.5 → 623.2 ft, maximum error 8.1 ft, biased high. The model-based policy replays from the observed 1950 head keep all policies above 618 ft (BAU minimum 629.7, S1 634.9, CPM 637.1 ft), but the open-loop bias means the true margins are smaller than the replay suggests; this is recorded, and no correction is applied.

## 4. Discussion

The complete evaluation loop — measured state, calibrated stock-flow map, declared governance operators, declared uncertainty classes, viability kernels with explicit declared-defect erosion, a held-out defect audit, and a fixed retention rule — yields a **positive selection result**: the reactive architecture matches flat-cap protection at 3.3–50.6% more permitted supply, and a 7.2% mean cut secures the physical threshold against a perpetual drought-of-record where business-as-usual fails. It also yields two negative findings: the institutional threshold is not demand-manageable to invariance under the declared classes, and the certified content is defect-bound to T ≤ 3 years.

The reactive result is system-dependent, not architectural. A companion intervention study on Northern cod applies the identical design and retains nothing: there the reactive rules cut catch exactly where the moratorium already protects, and the mirror verdict is a negative selection. The framework's deliverable is the scored comparison itself — which governance architecture earns its complexity is a property of the system, and the two scored systems bound the answer.

Two layers of results must be kept distinct. The robust-kernel findings are statements about the declared pumping family under the declared floor classes; the certified-kernel findings are a different layer, produced by applying the erosion conversion to the declared training defect. With ε = 15.41 ft — exceeded out of sample at 21.81 ft — every demand-management policy's certified kernel is empty beyond T = 3 years. The certified emptiness is a bound on what the fitted map can certify, not a robustness statement about the physical system; and the erosion bound absorbs the oracle gap measured by the companion forecast evaluation (12.84 versus 7.55 ft), so the unexplained forecast gap lies again in the information layer.

The negative certificate at 660 ft also reads correctly against the institution it describes. The actual CPM rule manages **frequency** — the fraction of time the head spends in critical stages — not robust invariance, and the finding that no pumping rule can hold the institutional threshold under a perpetual drought floor is consistent with that design intent: the rule cannot make wet years, it prices dry ones. The National Academies' review of the Habitat Conservation Plan (National Research Council 2015) was likewise organized around monitoring and modeling adequacy under drought; the horizon-not-invariance distinction is the robust-kernel expression of the same boundary.

The karst honesty of the object is inherited from its forecast-study companion and from the modeling lineage it descends from: the one-pool affine map is the simplest member of the lumped family whose regional adequacy was tested on the Barton Springs segment (Scanlon et al. 2003; Hutchison and Hill 2011). Conduits, the Uvalde–San Antonio divide, and unconfined recharge-zone storage remain in the residual; San Antonio and Uvalde recharge and pumpage are lumped; the actual CPM triggers are 10-day averages, so the annual-mean rule is a coarse relative of the real institution; and stages II–IV are declared scenarios, not verified institutions. Nominal kernels carry no defect margin, and the certified kernels use a training defect that the out-of-sample audit exceeds. The UC floors are certification geometry, not forecasts; the 1950s replay is biased high by 8.1 ft. Nothing in this leg promotes or demotes any forecast module, and no two-pool, karst, or solute claim is made.

## 5. Conclusions

On the measured J-17 record, reactive trigger rules outperform flat caps at matched robust protection: the Stage-I rule delivers the same robust invariance of the 618-ft threshold at 3.3–16.2% more permitted supply, and the cascade matches the deepest cut's protection at 50.6% more. A 7.2% mean cut secures the threshold against a perpetual drought-of-record, where business-as-usual fails within roughly 13 years. Two boundaries are equally part of the result: the 660-ft institutional threshold is protected by wet years rather than by the declared pumping family, and every certified claim is defect-bound to three years. The deliverable is the scored comparison on one measured system.

## Data Availability Statement

All input data, analysis scripts, and result files are archived in the public repository at https://github.com/MIKEAA2020/general-sustainability. J-17 daily highs: Texas Water Development Board well 6837203. Recharge: Umphres and Choi (2025), USGS data release, https://doi.org/10.5066/P1BI62NY. Pumpage: Edwards Aquifer Authority (2024/25), Table 1. The full intervention protocol — object, defect declaration, disturbance classes, policy family, and retention rule — was frozen and dated 2026-08-26 before any kernel, boundary, replay, or retention score was computed; it is archived with the analysis code as the preregistration record, alongside the companion forecast-evaluation protocols dated 2026-08-25. The analysis is fully deterministic: re-executing the committed runner regenerates both output files, and a verification re-execution in a fresh environment reproduced both byte for byte. The machine-readable outputs include the nominal and certified retention fields and the certified-horizon record.

## References

Edwards Aquifer Authority. 2024/25. *2023 Groundwater Discharge and Usage*, Table 1 (after USGS letter report, 5 April 2024). https://www.edwardsaquifer.org/wp-content/uploads/2025/05/2023-Groundwater-Discharge-and-Usage.pdf

Edwards Aquifer Authority. Critical Period / Drought Management. https://www.edwardsaquifer.org/groundwater-users/critical-period-drought-management/

Hutchison, W.R., and Hill, M.E. 2011. *Recalibration of the Edwards BFZ (Barton Springs Segment) Aquifer Groundwater Flow Model*. Texas Water Development Board, Austin, Texas, 121 p.

Krawczyk, J.B., and Pharo, A. 2013. Viability theory: An applied mathematics tool for achieving dynamic systems' sustainability. *Mathematica Applicanda* 41: 97–126.

Krawczyk, J.B., Pharo, A., Serea, O.S., and Sinclair, S. 2013. Computation of viability kernels: A case study of by-catch fisheries. *Computational Management Science* 10: 365–396.

National Research Council. 2015. *Review of the Edwards Aquifer Habitat Conservation Plan: Report 1*. The National Academies Press, Washington, DC. https://doi.org/10.17226/21699

Puente, C. 1978. *Method of estimating natural recharge to the Edwards Aquifer in the San Antonio area, Texas*. U.S. Geological Survey, Austin, Texas.

Scanlon, B.R., Mace, R.E., Barrett, M.E., and Smith, B. 2003. Can we simulate regional groundwater flow in a karst system using equivalent porous media models? Case study, Barton Springs Edwards aquifer, USA. *Journal of Hydrology* 276: 137–158.

Steinemann, A.C. 2003. Drought indicators and triggers: A stochastic approach to evaluation. *Journal of the American Water Resources Association* 39: 1217–1233. https://doi.org/10.1111/j.1752-1688.2003.tb03704.x

Texas Water Development Board. Water Data for Texas, well 6837203 (J-17). https://waterdatafortexas.org/groundwater/well/6837203

Umphres, G.D., and Choi, N.J. 2025. Estimated Annual Recharge to the Edwards Aquifer in the San Antonio Area, by Stream Basin or Ungaged Area, 1934–2024. U.S. Geological Survey data release. https://doi.org/10.5066/P1BI62NY

Watkins, D.W., Jr., and McKinney, D.C. 1997. Finding robust solutions to water resources problems. *Journal of Water Resources Planning and Management* 123: 49–58.

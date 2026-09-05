# Governance operators and viability kernels of the Edwards Aquifer: an intervention-selection test at J-17

**Prepared in the format of Groundwater (Wiley/NGWA)**

*Version log (v11).* Implements the joint external audit of this manuscript. No frozen verdict, no reported kernel, and no registered score changed; the changes are scoping, labelling, mechanism correction, and three labelled post-freeze layers. (1) The abstract and Impact Statement now lead with the three-verdict form (nominal at 618 ft / UC-min; not certified; not at 660 ft) and carry the hybrid caveat in the first results sentence: the +3.3%/+0.4% are historical-replay entitlements, and under the floor classes the margin collapses to a 0.4% trigger lag. (2) "BAU" is renamed training-mean (unregulated-mean) pumping wherever it is defined, with the baseline choice stated in the abstract and a current-pumpage sensitivity added. (3) The certified layer's mechanism is corrected: with affine policies the contraction rate is policy-independent, the erosion hypothesis is exact rather than an approximation, and the reason reactive rules collapse at the certified level is that the eroded threshold enters the trigger band (618 + r_T crosses 660 ft between T = 4 and T = 5). (4) The 660-ft result is restated as a design observation about scoring a trigger against its own level, not a negative certificate about the pumping family. (5) Kernel-emptiness horizons are reported as functions of the domain ceiling, with a new boundary-versus-horizon table. (6) Three post-freeze layers: a closed-loop historical-replay supply (the audit's missing within-model supply measure), a residual bootstrap of the worst-case attractors, and the OOS-defect erosion sensitivity. (7) The comparator grid is consolidated into one table (kernel-matched, attractor-twin, interpolated-7.2%, and 1%-grid readings). (8) Companion studies are cited; "machine-verified" vocabulary retired; fit hypotheses relabelled (F1)–(F4) to stop colliding with head H; tables renumbered. The v10 narrative remains available as the baseline.

## Abstract

**Problem.** Drought management in permitted groundwater systems relies on triggers and pumping reductions. Yet the comparative protection that competing rules deliver under adverse recharge is rarely scored against a fixed criterion. This paper provides such a score for one measured aquifer.

**Approach.** We compute robust viability kernels of the J-17 annual-mean head for a declared policy family — training-mean pumping (282.16 × 10³ acre-ft yr⁻¹, the 1934–1990 unregulated mean; not current use), flat caps of 90, 80, 70, 60, 50, and 0%, a Stage-I reactive rule, and the critical-period-management (CPM) cascade — under persistent drought-floor recharge. A non-BAU policy is retained only if it is at least as protective as training-mean pumping and more permissive than the smallest securing flat cap with matched protection. The retention protocol was frozen before any score was computed.

**Results.** At the 618-ft physical threshold under the drought-of-record floor, training-mean pumping's worst-case attractor (615.72 ft) lies below the threshold and its kernel empties beyond about 13 years; every flat cut of 10% or deeper, and both reactive rules, make the safe set robustly invariant; the smallest securing cut is an interpolated 7.2% of training-mean pumping (about 31% of current-mean pumping). The reactive rules are retained **nominally** at 618 ft under the mildest floor class only: the headline supply margins (+3.3% Stage I, +0.4% cascade, against the kernel-matched flat-90% cap) are hybrid quantities — worst-case protection scored against historical-replay entitlement in wet years the robust class excludes — and under the floor classes themselves the margin is a 0.4% trigger lag; retention is **not** certified (every positive-pumping certified kernel is empty beyond T = 3 years, a bound the out-of-sample defect makes optimistic), and **nothing is retained at 660 ft**, where the reactive rules are invisible to the kernel of their own trigger level — a geometric property of trigger design, since the cascade's institutional purpose is springflow protection near 618 ft, not head invariance at 660 ft.

**Implications.** On the measured J-17 record, reactive rules match flat-cap protection at the physical threshold and look supply-generous only if pumping in wet years is counted; the 660-ft threshold is protected by wet years, not by the pumping family; and certified claims are limited to three years by the fitted model defect.

**Keywords:** Edwards Aquifer; critical period management; J-17 index well; pumping policies; robust viability

**Article Impact Statement.** Reactive trigger rules on the Edwards Aquifer match flat-cap protection at J-17's 618-ft physical threshold at 3.3% (Stage I sketch) and 0.4% (cascade) more permitted supply than the kernel-matched flat-90% cap — nominal, hybrid-supply results; the 660-ft threshold is protected by wet years, not by pumping rules.

## 1. Introduction

Drought management in permitted groundwater systems is built on triggers. An index-well or springflow reading crosses a threshold, and pumping reductions activate. Trigger design has a long evaluation literature: drought indicators and triggers are properly assessed as stochastic objects, with explicit attention to how indicator levels, trigger thresholds, and drought stages interact (Steinemann 2003). Robustness has been a recurring concern of water-resources planning since the recognition that optimal solutions can be brittle to the hydrologic assumptions that produce them (Watkins and McKinney 1997). The operational question for a district that already operates triggers is narrower, and comparative: given a declared family of pumping rules, which rules deliver protection under adverse recharge, and at what cost in permitted supply?

The Edwards (Balcones Fault Zone) Aquifer of south-central Texas is the most fully institutionalized example of trigger-based groundwater governance in North America. Its critical-period management program stages pumping reductions at index-well thresholds. The reductions protect springflow at Comal and San Marcos Springs, whose endangered-species requirements are administered through the Edwards Aquifer Habitat Conservation Plan, the subject of a standing scientific review by the National Academies (National Research Council 2015). The aquifer's regional behavior has long been represented — and debated — through lumped and equivalent-porous-media models, from the Barton Springs groundwater availability model (Scanlon et al. 2003) to its recalibration by the Texas Water Development Board (Hutchison and Hill 2011). This study scores, rather than asserts, the protection supplied by a declared family of pumping rules on the measured J-17 record.

The instrument is the robust viability kernel: the set of initial heads from which a closed-loop pumping rule keeps the system inside a declared safe set under every disturbance in a declared class. Viability methods have an established lineage in natural-resource management, where constraints rather than objectives define the policy question (Krawczyk and Pharo 2013), and their computational tractability on management-scale problems is documented by fishery case studies (Krawczyk et al. 2013). The declared safe set here is a floor on the productive store rather than on a year's yield. The head threshold marks the level below which springflow at Comal and San Marcos approaches cessation. The policy question is therefore the protection of the base that regenerates the yield, and a trigger's function is to keep the store from being drawn down to that floor at the cost of near-term permitted supply. The governed object is the one-pool affine head map fitted in a companion forecast-evaluation study on the same series (under separate review), which found last-value persistence unbeaten by the causal ladder (7.55-ft oracle RMSE against 13.23 ft persistence and 12.84 ft AR(1); Author et al., in review). This study asks the governance question that the forecast study could not: whether a declared pumping rule changes the viability kernel of the real system as represented by the fitted map, and at what cost in permitted supply. A companion intervention study on a marine fishery stock applies the same design and reaches the mirror verdict — reactive rules retained there, none retained here; the mechanism contrast (fast wet-year recovery in this aquifer against a fatal productivity floor at the cod reference point) is the only reason to mention it, and the two systems' scores are never pooled (Author et al., in review).

The complete comparison — object, defect declaration, disturbance classes, policy family, and retention rule — was frozen in a dated protocol (2026-08-26) before any score was computed.

## 2. Methods

### 2.1 Object and dynamics

The object is that of the companion forecast evaluation: J-17 annual-mean head H_t (ft above mean sea level), San Antonio Pool, 1934–2023, drawn from the registered twenty-column analysis panel. The head is a measured well level, not an assessment inversion. Recharge R (USGS-estimated, Puente method; Umphres and Choi 2025) and pumpage P (Edwards Aquifer Authority Table 1) are the fluxes. No new data enter the analysis.

The dynamics are the causal stock-flow class of the companion forecast study, with one pool and affine form:

$$\Delta H_t = \alpha + \beta R_t + \gamma P_t + \delta H_{t-1}.$$

**Definition 2.1 (One-pool affine head map).** Let H_t denote the annual-mean head (ft above msl) at J-17, R_t the annual recharge, and P_t the annual pumpage. Under the hypotheses (F1) one-pool storage, (F2) affine dependence on (R_t, P_t, H_{t−1}), and (F3) ordinary-least-squares fitting on 1934–1990 (56 transitions), the head map is the relation above.

The fit is α = 163.49, β = 0.0198 ft per 10³ acre-ft, γ = −0.02844 ft per 10³ acre-ft, δ = −0.2539, so a = 1 + δ = 0.7461. The contraction a = 0.7461 corresponds to 25.4% per year mean reversion (the companion's rolling AR(1) on the same series gives 0.66 — different window, different object; the full-sample coefficients there are (0.017, −0.026) against this window's (0.0198, −0.02844)). Residual SD is 5.60 ft; training maximum is 15.41 ft. Out of sample (1991–2023, audit only, no refitting), the SD is 8.40 ft and the maximum is 21.81 ft. The out-of-sample maximum exceeds the declared defect. This fact is recorded below and not repaired, per protocol. The coefficients are fitted on the largely unregulated 1934–1990 era, so ordinary least squares cannot separate the aquifer's physical response from the pumpers' historical drought reactions, and imposing state-dependent rules under those coefficients assumes the physics–behavior separation the estimator does not guarantee (Lucas 1976); this bears on whether γ may be read as a policy lever at all, and the companion found the sign of γ reversed on the 1934–1950 subwindow.

The information pattern is the following: the manager ends year t knowing (H_t, R_t, P_t) and sets P_{t+1} = π(H_t). The recharge R_{t+1} is unknown at decision time and is treated adversarially within a declared persistent floor. The kernels therefore assume year-end J-17 is known exactly; the actual CPM triggers on 10-day means and cuts within the year, so annual triggering overstates the lag and understates the cut-active fraction.

### 2.2 Uncertainty classes and safe sets

The disturbance classes are persistent recharge floors computed on the training window: UC-min = 43.7 (the 1956 drought-of-record year, held perpetually), UC-q05 = 166.5, and UC-q10 = 179.1 × 10³ acre-ft yr⁻¹. UC-q05 and UC-q10 are the 3rd and 6th lowest recorded annual recharges of the 57 training years (linear-interpolation percentile estimator); the floors themselves have historical precedent, and only their perpetuity is harsher than any recorded year. They are certification geometry, not recharge forecasts.

The safe sets are the two declared normative thresholds, fixed in the frozen protocol: K*_phys = 618 ft (Comal Springs cessation proximity) and K*_inst = 660 ft (the post-2007 Stage I trigger, not applied to pre-2007 history; a 10-day mean in the actual institution, an annual mean here). The model domain is [610, 710] ft. Upward exits above 710 ft are model-domain exits, not threshold violations.

### 2.3 Governance family

The declared governance family is the following. Training-mean pumping (called BAU in the frozen protocol; the label is retained in tables) holds pumping at the 1934–1990 training mean, P ≡ P̄ = 282.16 × 10³ acre-ft yr⁻¹ — a flat 100% cap on the unregulated mean, not the historical pumpage path and not current use. Flat caps prescribe ρP̄ with ρ ∈ {0.9, 0.8, 0.7, 0.6, 0.5, 0.0}. The Stage-I reactive rule (S1) cuts pumping 20% when H < 660 ft; the reduction is a 20%-at-660 sketch of the Authority's published Stage I (the actual rule keys on 10-day J-17 or Comal flow). The critical-period-management (CPM) cascade prescribes cumulative stage totals of 20/30/35/40% cuts at H < 660/650/640/630 ft (cumulative, not stacked). The actual program declares five stages (Stage V at 625 ft); only the four-stage sketch is scored, Stage I is verified against the published 20%/660 pair, and stages II–IV are declared scenarios, not verified institutions.

The CPM supply figure below is the stage-weighted evaluation on the observed occupancies of the training era (1934–1990, n = 57 years): Stage I (H < 660 ft) 20 years (35.1%), Stage II (H < 650 ft) 12 (21.1%), Stage III (H < 640 ft) 5 (8.8%), and Stage IV (H < 630 ft) 1 (1.8%; 1956). The cumulative 20/30/35/40% cascade evaluated on these occupancies reproduces the replay's mean prescribed pumping exactly (254.93 × 10³ acre-ft yr⁻¹). Out of sample (1991–2023, n = 33 years) the occupancies are 33.3%, 15.2%, 6.1%, and 0.0%. Stages II and III recur out of sample (15.2%, 6.1%); Stage IV does not (0.0%; 1956 alone is below 630 ft), so CPM's deepest cut is a 1956-only scenario in the historical measure.

**Definition 2.2 (Robust viability kernel).** Fix a policy π, a disturbance class 𝒟, a safe set K*, and a horizon T. The robust T-step viability kernel Viab_T(π, K*, 𝒟) is the set of initial heads from which the closed loop P_{t+1} = π(H_t) keeps H inside K* under every recharge sequence in 𝒟.

For each policy and disturbance class, the robust T-step viability kernel of the safe set is computed by iterating the worst-case closed loop. The nominal kernel is reported without erosion. The certified layer applies the defect-to-margin conversion in the form the fitted map admits. The term "kernel" is used in its closed-loop reading — the robust positively invariant set of a fixed declared policy — not in the classical viability reading of Aubin (1991), which is existential over controls. No control choice enters the kernel computation. Only the evaluation of declared rules under the disturbance floor enters. With the declared policies all deterministic functions of the observed head, each robust kernel reduces to the invariance statement of a one-dimensional closed loop — attractor and domain-top arithmetic rather than control synthesis. The word is retained because the object answers the same question ("from which states can the constraint be held?") in the policy-fixed form.

### 2.4 Retention rule and certified layer

The retention rule decides which non-training-mean policies earn their additional structure. The certified layer converts the declared defect into an erosion margin on the kernel.

**Definition 2.3 (Retention rule).** A non-BAU policy is retained only if (R1) its robust kernel is at least as protective as training-mean pumping's at every reading, compared on the kernel lower boundary with empty = worst, and (R2) it permits more pumping than the smallest securing flat cap with matched protection — on the declared 10% grid this resolves as the largest-supply member of the matched class (flat-90%); the grid-resolution sensitivity is reported in Section 3.4 (Table 6).

The scoring regimes are declared here rather than left implicit. **Protection is scored under the disturbance classes** — the perpetual floors of Section 2.3. **Supply is scored as the 1934–1990 historical replay mean.** The retention verdict is therefore a hybrid: worst-case protection at historical-mean entitlement, not a within-scenario dominance. Under the floor classes alone, the reactive rules are identically their matched flat caps (the cut is active every year) and carry no supply margin. The retention decision is made at the nominal level and re-checked at the certified level. The certified re-check holds only over the horizons where the certified kernels are nonempty — a horizon-truncated object, stated as such whenever it is invoked. At 618 ft under UC-min, R1 is close to automatic: every cut of 10% or deeper in the family makes the safe set invariant, so retention reduces to R2 (supply at matched protection).

**Calculation 2.1 (Certified erosion margin).** Let ε = 15.41 ft denote the declared uniform defect (the training maximum residual) and let a = 0.7461 denote the closed-loop contraction rate. Under the hypothesis (F4) that the autonomous contraction rate applies uniformly to the residual, the T-step erosion margin is

$$r_T = \varepsilon \frac{1 - a^T}{1 - a},$$

giving r₁ = 15.41, r₃ = 35.49, r₄ = 41.89, r₅ = 46.66, r_∞ = 60.70 ft.

*Derivation.* Under (F4) the closed-loop residual obeys e_T = a^T e_0. Summing the geometric series of perturbations of magnitude at most ε yields r_T = ε(1 + a + ... + a^{T−1}) = ε(1 − a^T)/(1 − a); the result is the triangle-inequality bound for bounded additive perturbations of a contracting scalar map. Numerical evaluation at the listed horizons gives the listed values. □

**Definition 2.4 (Certified kernel).** The certified kernel at horizon T is the nominal kernel of K* + r_T, with r_T as in Calculation 2.1.

Two properties of the certified layer must be stated before the results, because the audit correctly flagged the earlier account as imprecise. First, in this affine family every policy enters the map only through the intercept (γP is a constant shift), so the contraction rate a is identical across policies and (F4) is exact, not an approximation: the certified kernel is the closed-loop nominal kernel of a raised threshold, feedback included. Second, the mechanism by which the reactive rules collapse at the certified level is trigger-band entry: the eroded threshold K* + r_T crosses the 660-ft trigger between T = 4 (618 + 41.89 = 659.89) and T = 5 (618 + 46.66 = 664.66), so any threshold-erosion certificate makes every below-660 trigger rule identical to training-mean pumping from T ≥ 4 — the same trigger-on-boundary invisibility as Section 3.2, re-entering by construction. The constant-r_T form is also conservative by construction: a per-step tube K* + r_t (t = 1..T) is tighter than K* + r_T held at every step.

## 3. Results

### 3.1 Worst-case attractors and the minimal cut

**Table 1.** Worst-case attractors of the closed loop (ft), by policy and recharge floor.

| Policy | UC-min | UC-q05 | UC-q10 |
|---|---:|---:|---:|
| training-mean pumping (BAU) | 615.72 | 625.31 | 626.29 |
| flat-90% | 618.88 | 628.47 | 629.45 |
| flat-80% | 622.04 | 631.63 | 632.61 |
| S1 (20% cut < 660 ft) | 622.04 | 631.63 | 632.61 |
| flat-70% | 625.20 | 634.79 | 635.77 |
| CPM cascade | 628.36 | 636.37 | 637.35 |
| flat-60% | 628.36 | 637.95 | 638.93 |
| flat-50% | 631.52 | 641.11 | 642.09 |
| flat-0 (zero pumping) | 647.32 | 656.91 | 657.90 |

![Figure 1](figs_e4/fig1_attractors.png)

**Figure 1.** Worst-case attractor of the closed loop under the perpetual drought-of-record floor (UC-min) by policy, from the registered kernel computation (Table 1). Training-mean pumping's attractor (615.72 ft) sits below the 618-ft physical threshold. Every cut policy — flat caps of 10% and deeper, the Stage I reactive rule, and the critical-period-management cascade — holds its attractor at or above the threshold. Under UC-min the reactive rules coincide with their attractor twins (S1 = flat-80%, CPM = flat-60%; under UC-q05 the CPM attractor sits between the Stage III and IV triggers and equals a ~65% cap); flat-90% clears the threshold by 0.88 ft — a margin the bootstrap of Section 3.7 shows is not resolved by the fit.

Under a perpetual 1956-recharge floor, training-mean pumping's attractor (615.72 ft) sits below the physical threshold. The smallest flat cut whose attractor clears 618 ft is an interpolated **7.2%** of training-mean pumping, which lies outside the declared family (on the current-mean baseline of 382.16 × 10³ acre-ft yr⁻¹ the same arithmetic gives a securing cut of about 31%, and the Stage-I 20% cut does not secure — Section 3.4). The Stage-I reactive rule's attractor equals flat-80%'s, because the cut is active on the entire attractor branch.

### 3.2 Nominal kernels

**Table 3.** Nominal kernel lower boundary (ft) at the 618-ft threshold under UC-min, by horizon. Cut policies (flat-90% and deeper, S1, CPM) hold the whole safe set [618, 710] at every horizon, including the infinite horizon.

| Horizon T | 1 | 5 | 10 | 12 | 12.7 (crossover) | ∞ |
|---|---:|---:|---:|---:|---:|---|
| BAU boundary | 618.8 | 625.6 | 658.4 | 692.6 | 710 | empty |

At the physical threshold (618 ft) under UC-min, training-mean pumping's kernel boundary climbs 618.8 (T = 1) → 625.6 (T = 5) → 658.4 (T = 10), and the kernel is empty beyond T ≈ 13 years. The emptiness is a domain-top event, and its arithmetic should be read exactly: the boundary B(T) = H* + (618 − H*)/a^T reaches the declared safe-set ceiling when the *required initial head* exceeds 710 ft — trajectories fall toward the attractor, they do not exit upward. The horizon is a function of the arbitrary ceiling: T_empty(C) = ln((C − H*)/(K* − H*))/ln(1/a), so the 710-ft ceiling gives 12.7 years, the observed maximum annual mean (692.7 ft) gives 12.0 years, and with no ceiling the kernel is never empty in the domain sense — every state converges to the attractor, and "empty beyond T" means "no initial head in the domain lasts T years." With the ceiling stated, business-as-usual is not robustly viable against a perpetual drought-of-record, and the observed 1992 mean (691.96 ft) sits almost at the T = 12 boundary. Every cut policy in the family — a 10% flat cap, S1, CPM, and deeper — makes [618, 710] robustly invariant: the whole declared safe set is the kernel at every horizon, including the infinite horizon. Under UC-q05/UC-q10 the safe set is already invariant at training-mean pumping (attractors 625.3/626.3 ft); governance differentiates the kernel only under the drought-floor class.

At the institutional threshold (660 ft) the result is a **design observation about scoring a trigger against its own level**, and the kernel statement splits by policy class. For the **reactive rules** (S1, CPM) the equality with training-mean pumping is exact at every horizon: the boundaries (675.1 at T = 1, 695.3 at T = 2 under UC-min; empty from T = 3) lie strictly above the first-stage trigger (660 ft, the highest of the four declared trigger levels), no reactive rule fires in the viable region, and the kernel is policy-invariant for them. That equality is a geometric identity — a trigger placed on the boundary of a constraint is invisible to the viability kernel of that same constraint, and no rule that cuts only below 660 ft can improve the invariance of {H ≥ 660} — and it is a category observation about the scoring, not a deficiency of the rules: the cascade's institutional purpose is springflow protection near 618 ft, not head invariance at 660 ft. For the **flat caps** the equality is false. They move the finite-horizon boundaries (flat-80% reads ≈673 at T = 1 against BAU's 675.1) and extend the viable horizon (from T = 3 at BAU through T ≈ 6 at flat-50% to T ≈ 6–11 for zero pumping by the same ceiling arithmetic; zero pumping's attractor 647.3/657.9 ft still sits below 660 ft). Demand management therefore extends the viable **horizon, not invariance**, and the correct statement of the 660-ft reading is: no policy in the declared family, zero pumping included, holds {H ≥ 660} invariant under the drought floors — the threshold is protected by wet years, not by the pumping family. This is the frequency-management rationale the actual CPM rule implements, and that rationale is outside the robust-kernel frame.

### 3.3 Certified kernels

With the erosion of Section 2.4 applied, every demand-management policy in the family has an empty certified kernel beyond **T = 3 years** at the physical threshold and beyond T = 1 year at the institutional threshold. Zero pumping is the exception. Its certified physical-threshold kernel is nonempty through T = 4 under UC-min (lower boundary ≈687.9 ft from the certified-kernel algebra; the registered horizon grid {1, 2, 3, 5, 8, 10, 15, 20, ∞} does not sample T = 4 — the algebra is the record there and the grid is annotated accordingly) and through T = 5 under UC-q05/UC-q10. The certified boundaries at T = 3, UC-min, 618 ft: flat-0 662.2 < flat-80 697.8 < BAU = S1 = CPM 706.7 ft. The certified-level inference is drawn explicitly: at the one certified horizon tabulated, the reactive rules inherit training-mean pumping's boundary (706.7) — strictly above flat-80%'s (697.8) — so certified dominance of S1 over its matched flat cap fails. The +3.3%/+16.2% supply margins are nominal-level comparisons. Certified retention is a different, horizon-truncated object from nominal retention (Section 2.4).

The bound is optimistic, and the audit's sensitivity is recorded: at the out-of-sample defect (ε = 21.81 ft) the erosion margins scale to r₃ = 50.22, r₅ = 66.04, r_∞ = 85.90 ft, so certified emptiness beyond T = 3 is a *lower* bound on how fast certification dies, and certified horizons do not appear as findings beyond this section's scope statement. The binding constraint on certified intervention claims is the model defect, not the governance. The certified comparison is also conservative in form against the state-dependent rules for the geometric reason of Section 2.4 — the eroded threshold enters the trigger band from T = 4 — which is a property of threshold-erosion certificates generally, not of these rules.

### 3.4 Supply and retention

**Table 2.** Mean prescribed pumping: the frozen open-loop replay (actual observed heads, 1934–1990) and the post-freeze closed-loop replay (head simulated by the map under actual recharge, same policy in force), 10³ acre-ft yr⁻¹.

| Policy | Open-loop supply (frozen) | Cut active | Closed-loop supply (post-freeze) | Closed-loop cut active |
|---|---:|---:|---:|---:|
| BAU (training-mean) | 282.16 | 0% | 282.16 | 0% |
| flat-90% | 253.94 | 100% | 253.94 | 100% |
| flat-80% | 225.73 | 100% | 225.73 | 100% |
| flat-70% | 197.51 | 100% | 197.51 | 100% |
| S1 | **262.36** | 35.1% | 258.98 | 41.1% |
| CPM | **254.93** | 35.1% | 254.70 | 41.1% (any stage) |
| flat-60% | 169.29 | 100% | 169.30 | 100% |
| flat-50% | 141.08 | 100% | 141.08 | 100% |
| flat-0% | 0.00 | 100% | 0.00 | 100% |

Out-of-sample open-loop replay (audit only, over the 1991→2022 transitions): S1 264.5 and CPM 260.6 × 10³ acre-ft yr⁻¹; closed-loop from the observed 1990 head, S1 prescribes 268.5 with the cut active 24.2% of years and ends 2023 at 643.3 ft (observed 635.7; training-mean pumping ends 639.2). Every flat policy prescribes its cap throughout, so its supplies coincide by construction. The closed loop is a model object: run from the observed 1934 head it ends 1990 at 677.6 ft against the observed 645.8 ft (+31.8 ft), so the closed-loop supplies carry the map's own level bias and are reported as the audit requested — as the within-model check on the hybrid margin, not as a second retention leg.

**Table 6.** The retention margins under every comparator reading (open-loop supplies; the closed-loop margins follow in the text).

| Comparator (matched protection at 618 ft / UC-min) | Supply | S1 margin | CPM margin |
|---|---:|---:|---:|
| kernel-matched flat-90% (declared grid) | 253.94 | +3.3% | +0.4% |
| attractor twin flat-80% (S1) / flat-60% (CPM) | 225.73 / 169.29 | +16.2% | +50.6% |
| interpolated 7.2% cut (outside family) | 261.84 | +0.2% | −2.6% (fails) |
| flat-92% (1% grid) | 259.59 | +1.1% | −1.8% (fails) |
| flat-93% (1% grid) | 262.41 | −0.02% (fails) | −2.9% (fails) |

- **S1: retained (nominal, UC-min, 618 ft; hybrid).** It matches the flat caps' robust invariance (kernel = whole safe set at all horizons) while supplying 262.36 versus flat-90%'s 253.94 (+8.4 × 10³ acre-ft yr⁻¹, +3.3%) and flat-80%'s 225.73 (+36.6, +16.2%). The scoring regimes are the hybrid declared in Section 2.4 — protection under the perpetual worst-year recharge floor, supply as the 1934–1990 historical replay mean. The reading of the retention is exactly "worst-case protection at historical-mean entitlement," not a within-scenario dominance. Under the floor itself S1 is identically flat-80% (the cut is active every year, and its floor-attractor supply equals flat-80%'s), so the supply margin exists only in wet years that the robust class excludes. Against flat-90% the floor comparison is the sharper one — S1 is always −20% where flat-90% is always −10%, at identical invariance. The reactive architecture justifies its additional structure on the hybrid criterion, not on the robust criterion alone, and the comparator table shows how grid-dependent the margin is: against the 1%-grid smallest securing cap it is +1.1%, and against the interpolated 7.2% cut it is +0.2%.
- **CPM: retained (nominal, same threshold and class).** Attractor 628.36 ft (equal to flat-60%'s) at supply 254.93 versus flat-60%'s 169.29 (+50.6%) and flat-90%'s 253.94 (+0.4%). The +50.6% is priced substantially off Stage IV, a stage occupied in 1 of 90 years.
- **Closed-loop re-check (post-freeze layer).** With each policy in force and the head simulated by the map under actual recharge, S1's supply falls to 258.98 (−1.3% versus the open-loop replay; the cut is active 41.1% of years, not 35.1%, because the map's trajectory dips below 660 ft more often than the observed record did) and CPM's to 254.70 (−0.1%). The hybrid margins attenuate but survive: S1 +2.0% versus flat-90% (+14.7% versus flat-80%), CPM +50.4% versus flat-60% (+0.3% versus flat-90%). The margin is a real property of the rule's wet-year behavior on this map, not an artefact of evaluating the rules on the observed (unregulated-era) heads alone.
- **Certified level:** certified retention is horizon-truncated. At the one tabulated certified horizon the reactive rules inherit training-mean pumping's boundary (706.7 ft, Section 3.3) and fail the certified re-check. The supply figures are nominal-level comparisons, not certified retention.
- **Institutional threshold: nothing retained.** The reactive rules are identically training-mean pumping at every horizon (trigger-on-boundary invisibility, Section 3.2). The flat caps are more protective at finite horizons and extend the viable horizon. No policy meets the retention test there.
- **Current-baseline sensitivity (post-freeze, analytic).** The declared family and every supply figure are relative to the 1934–1990 training mean (282.16). On the 1991–2023 mean actual pumpage (382.16 × 10³ acre-ft yr⁻¹), the same attractor arithmetic gives training-mean-pumping 604.52 ft, the securing cut ≈31.5%, and the Stage-I/flat-80% attractor 613.08 ft — below 618 ft, so the 20% sketch does not secure the physical threshold at current use. Re-expression of the family on the current baseline is a registered follow-up, not a scored object here.

### 3.5 Classification and stress replays

The T = 5 nominal kernel (UC-min, 618 ft) classifies the actual record. Training-mean pumping excludes exactly one actual year from its viable set — 1956, the drought-of-record year (623.15 ft annual mean, above 618 ft and above the 615.72-ft attractor: 1956 is excluded as a *starting* head whose 5-year forward path under perpetual 1956 recharge falls through the threshold, not because the 1956 mean was below 618; its daily minimum, 612.51 ft, was). S1 and CPM exclude none: the entire 90-year actual record is robustly 5-year viable under the cut rules. The T = 5 certified kernels are empty, so no actual year is certified 5-year viable under any policy. This is the boundary of the certified analysis.

A 1950s open-loop diagnostic (model driven by actual R, P versus actual heads, 1951–1956) records the map's drought bias. The affine map under-predicts the decline: model 659.5 → 631.3 versus actual 659.5 → 623.2 ft, maximum error 8.1 ft, biased high. The model-based policy replays from the observed 1950 head keep all policies above 618 ft (BAU minimum 629.7, S1 634.9, CPM 637.1 ft) — note that this replay holds pumping at the training mean (282.16) while actual 1956 pumping was ≈321 × 10³ acre-ft, so it is not the decade's actual policy either. The open-loop bias means the true margins are smaller than the replay suggests. This is recorded, and no correction is applied.

### 3.6 Finite-duration recharge floors and floor-class supply (post-freeze layers)

Two declared post-freeze layers extend the persistent-floor object. The first asks how long a drought-class episode must last before the safe set contracts. The class floor holds for $n$ years, recharge then returns to its training mean, and the infinite-horizon lower boundary at the 618-ft threshold is pulled back by exact backward recursion through the $n$ floor years. The second computes the floor-class supply — the closed loop from the observed 1934 head with recharge held at each class floor — supplying the declared-scoring half that the historical replay cannot.

**Table 4.** Finite-duration floors (post-freeze): infinite-horizon lower boundary (ft) at the 618-ft threshold after $n$ years at the class floor followed by training-mean recharge. The BAU row at $n=5$ and $n=10$ reproduces the registered $T=5$ and $T=10$ nominal boundaries (625.6 and 658.4 ft). The $n=15$ emptiness reproduces the registered 13-year horizon bound.

| Policy | UC_min, $n{=}5$ | UC_min, $n{=}10$ | UC_min, $n{=}15$ | UC_q05/q10, any $n$ |
|---|---:|---:|---:|---:|
| BAU | 625.6 | 658.4 | empty | 618.0 |
| flat-90% and deeper; S1; CPM | 618.0 | 618.0 | 618.0 | 618.0 |

Duration differentiates exactly one policy. Under the drought-class floor, training-mean pumping is the only policy whose boundary moves with episode length. Every cut policy holds the whole safe set at every duration, because the cuts' floor attractors sit at or above the threshold (618.9–647.3 ft, Section 3.1, Table 1). A finite drought episode followed by normal recharge pulls nothing back beyond 618 ft. Under the two milder classes the safe set is already invariant at BAU (Section 3.2), and duration is inert for every policy.

**Table 5.** Floor-class supply (post-freeze): closed loop from the observed 1934 head (670.4 ft), recharge held at the class floor, mean prescribed pumping (10³ acre-ft yr⁻¹) over the training span (1934–1990) and the full span (1934–2023); end head at 2023.

| Policy | UC_min supply (train/full) | UC_min end head | UC_q05 supply (train) | UC_q10 supply (train) |
|---|---:|---:|---:|---:|
| BAU | 282.16 / 282.16 | 615.7 | 282.16 | 282.16 |
| flat-90% | 253.94 / 253.94 | 618.9 | 253.94 | 253.94 |
| flat-80% | 225.73 / 225.73 | 622.0 | 225.73 | 225.73 |
| S1 | 226.72 / 226.36 | 622.0 | 226.72 | 226.72 |
| flat-60% | 169.30 / 169.30 | 628.4 | 169.30 | 169.30 |
| CPM | 174.49 / 172.59 | 628.4 | 187.36 | 187.61 |
| flat-0 | 0 / 0 | 647.3 | 0 | 0 |

The table quantifies the scoring-regime reading of Section 2.4. Under the floors the reactive rules converge to their matched flat-cap attractors (S1 to flat-80%'s 622.04 ft, CPM to flat-60%'s 628.36 ft — the cut active every year on the attractor branch). Their closed-loop span-mean supply exceeds the matched caps only by the trigger-lag margin of the descent from the observed 1934 head — S1 +0.4% over flat-80% (226.7 versus 225.7 × 10³ acre-ft yr⁻¹, a floor-class trigger lag), CPM +3.1% over flat-60% (174.5 versus 169.3). These are different objects from the hybrid margins of Table 6: S1's +0.4% here is the within-floor trigger lag, CPM's +0.4% there is the historical-replay margin against flat-90% — same number, different quantities, and neither is a robust-supply statement. The hybrid criterion's margins exist only in the wet years that the robust classes exclude; the floor-class supply leg is the margin's own measure of how little it would buy inside the class.

### 3.7 Attractor uncertainty (post-freeze layer)

**Table 7.** Residual bootstrap of the 1934–1990 fit (5,000 replications, seeded; no replication was non-contractive): worst-case attractor under UC-min, by policy.

| Policy | Point attractor (ft) | Bootstrap mean (ft) | Bootstrap SD (ft) | 5th–95th percentile (ft) | P(attractor ≥ 618 ft) |
|---|---:|---:|---:|---|---:|
| BAU (training-mean) | 615.72 | 613.72 | 13.09 | 590.0 – 630.6 | 0.41 |
| flat-90% | 618.88 | 617.00 | 12.46 | 594.5 – 633.0 | 0.53 |
| flat-80% / S1 | 622.04 | 620.27 | 11.87 | 598.7 – 635.7 | 0.65 |
| flat-70% | 625.20 | 623.55 | 11.35 | 603.1 – 638.3 | 0.75 |
| flat-60% / CPM | 628.36 | 626.83 | 10.89 | 607.3 – 641.2 | 0.83 |
| flat-50% | 631.52 | 630.11 | 10.51 | 611.3 – 644.2 | 0.89 |
| flat-0 | 647.32 | 646.49 | 10.03 | 629.0 – 661.2 | 0.99 |

The audit's resolvability question has a quantitative answer. The *ordering* of the attractors is resolved: the flat-90%-minus-BAU gap has a 90% bootstrap band of [1.9, 5.0] ft, excluding zero. The *threshold clearance* is not: whether training-mean pumping fails 618 ft (P = 0.41) and whether the marginal securing caps (flat-90%, P = 0.53; S1/flat-80%, P = 0.65) clear it are coin flips at this fit; only cuts of 60% and deeper reach probabilities above 0.8, and zero pumping reaches 0.99. The nominal-level statement that a 10% cut secures the threshold rests on a 2.3-ft gap (615.72 to 618.88) on a map with 5.6-ft residual SD and an acknowledged 8.1-ft high bias in the drought it is scored on — the fitted map cannot resolve whether the marginal members of the family protect 618 ft. The deep cuts and the failure of training-mean pumping are the resolved parts of the result.

## 4. Discussion

The complete evaluation loop — measured state, calibrated stock-flow map, declared governance operators, declared uncertainty classes, viability kernels with explicit declared-defect erosion, a held-out defect audit, and a fixed retention rule — yields a **nominal selection at the physical threshold under the mildest floor class**. The reactive architecture matches flat-cap protection at 3.3% (S1) and 0.4% (cascade) more permitted supply than the kernel-matched flat-90% cap — 16.2% and 50.6% against their attractor twins, +1.1% and −1.8% against the 1%-grid smallest securing cap — under a hybrid criterion whose wet-year entitlement the closed-loop re-check attenuates but does not remove. An interpolated 7.2% mean cut (outside the declared family; about 31% of current use) secures the physical threshold against a perpetual drought-of-record where training-mean pumping fails within roughly 13 years (a ceiling-relative statement, Section 3.2). Two boundaries are equally part of the result: the institutional threshold is not demand-manageable to invariance under the declared classes, and the certified content is defect-bound to T ≤ 3 years.

The reactive result is system-dependent, not architectural. Its mechanism is the aquifer's physics. High transmissivity and rapid karst recharge make wet-year recovery fast, so a flat cap permanently taxes recoveries that a reactive rule harvests — the supply margin exists only in the wet years that the robust classes exclude (Section 3.4). A companion intervention study on Northern cod applies the identical design and retains nothing: there the reactive rules cut catch exactly where the moratorium already protects. The framework's deliverable is the scored comparison itself; which governance architecture earns its complexity is a property of the system, and the two scored systems occupy opposite ends of that design space without bounding it.

Two layers of results must be kept distinct. The robust-kernel findings are statements about the declared pumping family under the declared floor classes. The certified-kernel findings are a different layer, produced by applying the erosion conversion to the declared training defect. With ε = 15.41 ft — exceeded out of sample at 21.81 ft — every demand-management policy's certified kernel is empty beyond T = 3 years, and the bound is optimistic rather than conservative on this object (Section 3.3). The certified emptiness is a bound on what the fitted map can certify, not a robustness statement about the physical system. The mechanism of the reactive rules' certified collapse is geometric — the eroded threshold enters the trigger band (Section 2.4) — and the certified comparison is conservative in form against state-dependent rules for that reason.

The 660-ft design observation also reads correctly against the institution it describes. The actual CPM rule manages **frequency** — the fraction of time the head spends in critical stages — not robust invariance. The finding that no pumping rule can hold the institutional threshold under a perpetual drought floor is consistent with that design intent: the rule cannot make wet years, it prices dry ones. The National Academies' review of the Habitat Conservation Plan (National Research Council 2015) was likewise organized around monitoring and modeling adequacy under drought. The horizon-not-invariance distinction is the robust-kernel expression of the same boundary.

The karst honesty of the object is inherited from its forecast-study companion and from the modeling lineage it descends from. The one-pool affine map is the simplest member of the lumped family whose regional adequacy was tested on the Barton Springs segment (Scanlon et al. 2003; Hutchison and Hill 2011). Conduits, the Uvalde–San Antonio divide, and unconfined recharge-zone storage remain in the residual. San Antonio and Uvalde recharge and pumpage are lumped. The actual CPM triggers are 10-day averages, so the annual-mean rule is a coarse relative of the real institution. Stages II–IV are declared scenarios, not verified institutions. Nominal kernels carry no defect margin, and the certified kernels use a training defect that the out-of-sample audit exceeds. The counterfactual swap from the largely unregulated fitting era to state-dependent rules carries the declared econometric boundary of Section 2.1 (Lucas 1976). The UC floors are certification geometry, not forecasts. The 1950s replay is biased high by 8.1 ft. Nothing in this leg promotes or demotes any forecast module, and no two-pool, karst, or solute claim is made.

## 5. Conclusions

On the measured J-17 record, three verdicts, not one. (1) **Nominal, physical threshold, mildest floor class:** reactive trigger rules match flat-cap robust protection of the 618-ft threshold at 3.3% (Stage-I sketch) and 0.4% (cascade) more permitted supply than the kernel-matched flat-90% cap — 16.2% and 50.6% against their attractor twins — under a hybrid criterion (worst-case protection, historical-replay entitlement) whose wet-year margin survives a closed-loop re-check attenuated (S1 +2.0% versus flat-90%). An interpolated 7.2% mean cut of training-mean pumping (about 31% of current use) secures the threshold against a perpetual drought-of-record, where training-mean pumping fails within roughly 13 years (ceiling-relative). (2) **Certified:** nothing — every positive-pumping certified kernel is empty beyond three years, an optimistic bound on a defect the out-of-sample audit exceeds. (3) **Institutional threshold:** nothing — the 660-ft line is protected by wet years rather than by the pumping family, a geometric property of scoring triggers against their own level. The fitted map resolves the deep-cut protections and the failure of training-mean pumping, and cannot resolve the marginal caps (P = 0.41–0.65); that is the honest resolution limit of the deliverable — the scored comparison on one measured system.

## Data Availability Statement

All input data, analysis scripts, and result files are archived in the public repository at https://github.com/MIKEAA2020/general-sustainability. J-17 daily highs: Texas Water Development Board well 6837203. Recharge: Umphres and Choi (2025), USGS data release, https://doi.org/10.5066/P1BI62NY. Pumpage: Edwards Aquifer Authority (2024/25), Table 1. The full intervention protocol — object, defect declaration, disturbance classes, policy family, and retention rule — was frozen and dated 2026-08-26 before any kernel, boundary, replay, or retention score was computed. It is archived with the analysis code as the preregistration record, alongside the companion forecast-evaluation protocols dated 2026-08-25. The analysis is fully deterministic: re-executing the registered runner regenerates both output files, and a verification re-execution in a fresh environment reproduced both byte for byte. The machine-readable outputs include the nominal and certified retention fields and the certified-horizon record. The Section 3.6 layers (finite-duration floors; floor-class supply) are produced by `rerun_campaigns/campaign_e4_elevation.py`, archived alongside their outputs, and regenerate them exactly. The post-freeze audit layers of Sections 3.4 (closed-loop supply replay), 3.4's current-baseline sensitivity, and 3.7 (attractor bootstrap) are produced by `wave_e_edwards/src/e4_audit_layer.py` (seeded, deterministic, on the registered panel and the paper's declared coefficients), with outputs archived as `wave_e_edwards/results/e4_audit_layer.json`.

## References

Author, A., et al. In review. Does a one-pool water-balance model improve forecasts of Edwards Aquifer head? A scored test at J-17. Companion forecast-evaluation study.

Author, B., et al. In review. Surplus-production intervention selection under a persistent productivity floor. Companion intervention study (Northern cod, NAFO 2J3KL).

Aubin, J.-P., 1991. Viability Theory. Birkhäuser, Boston.

Edwards Aquifer Authority. 2024/25. *2023 Groundwater Discharge and Usage*, Table 1 (after USGS letter report, 5 April 2024). https://www.edwardsaquifer.org/wp-content/uploads/2025/05/2023-Groundwater-Discharge-and-Usage.pdf

Edwards Aquifer Authority. Critical Period / Drought Management. https://www.edwardsaquifer.org/groundwater-users/critical-period-drought-management/

Hutchison, W.R., and Hill, M.E. 2011. *Recalibration of the Edwards BFZ (Barton Springs Segment) Aquifer Groundwater Flow Model*. Texas Water Development Board, Austin, Texas, 121 p.

Krawczyk, J.B., and Pharo, A. 2013. Viability theory: An applied mathematics tool for achieving dynamic systems' sustainability. *Mathematica Applicanda* 41: 97–126.

Krawczyk, J.B., Pharo, A., Serea, O.S., and Sinclair, S. 2013. Computation of viability kernels: A case study of by-catch fisheries. *Computational Management Science* 10: 365–396.

Lucas, R.E., Jr., 1976. Econometric policy evaluation: A critique. *Carnegie-Rochester Conference Series on Public Policy* 1: 19–46.

National Research Council. 2015. *Review of the Edwards Aquifer Habitat Conservation Plan: Report 1*. The National Academies Press, Washington, DC. https://doi.org/10.17226/21699

Puente, C. 1978. *Method of estimating natural recharge to the Edwards Aquifer in the San Antonio area, Texas.* U.S. Geological Survey, Austin, Texas.

Scanlon, B.R., Mace, R.E., Barrett, M.E., and Smith, B. 2003. Can we simulate regional groundwater flow in a karst system using equivalent porous media models? Case study, Barton Springs Edwards aquifer, USA. *Journal of Hydrology* 276: 137–158.

Steinemann, A.C. 2003. Drought indicators and triggers: A stochastic approach to evaluation. *Journal of the American Water Resources Association* 39: 1217–1233. https://doi.org/10.1111/j.1752-1688.2003.tb03704.x

Texas Water Development Board. Water Data for Texas, well 6837203 (J-17). https://waterdatafortexas.org/groundwater/well/6837203

Umphres, G.D., and Choi, N.J. 2025. Estimated Annual Recharge to the Edwards Aquifer in the San Antonio Area, by Stream Basin or Ungaged Area, 1934–2024. U.S. Geological Survey data release. https://doi.org/10.5066/P1BI62NY

Watkins, D.W., Jr., and McKinney, D.C. 1997. Finding robust solutions to water resources problems. *Journal of Water Resources Planning and Management* 123: 49–58.

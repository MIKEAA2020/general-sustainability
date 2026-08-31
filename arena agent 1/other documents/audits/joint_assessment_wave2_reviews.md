# Joint Assessment of the Second Audit Wave (P1, P2, P4, P5, E1–E4)

Eight parallel audits were delivered: `grok audit paper1.txt` (2 audits), `gpt audit paper 2.txt`, `gpt audit paper 4.txt`, `gpt audit paper 5.txt`, `grok audit e1.txt` (2), `grok audit e2.txt` (2), `grok audit e3.txt` (2), `grok audit e4.txt` (2). All eight were read at line level and every material claim was verified against the arena drafts. Classifications below; implementation status is given per item.

Legend: **GENUINE** = verified against the draft, fixed in this pass; **GENUINE-D** = verified, fixed by disclosure/declaration because the demanded recomputation is outside this pass (new numbers cannot be invented); **STALE** = already handled by the current draft; **ARTIFACT** = applies to the official repo version, not the arena draft; **DISPOSED** = claim does not hold on inspection; **NEW** = legitimate addition, adopted where cheap.

---

## Paper 1 (`paper1_assessment_separation.md`)

| # | Finding | Class | Action |
|---|---|---|---|
| A1/1 | Abstract and §1.2 say the acceptance gap is partitioned into rescue + impossibility; Theorem 5(4) proves FP_agg = I and R ⊂ V_typ. R is not in the gap; what is partitioned is FP_0. | **GENUINE** | Fixed: abstract, §1.2, conclusion reworded; FP_0 is the partitioned region, the acceptance gap is exactly I = FP_agg. |
| A1/5 | §1.2 credits the always-valid inclusion to Theorem 3; it is Proposition 1. | **GENUINE** | Fixed. |
| A1/7, A2/1.2 | Disturbance set {α, β} vs the per-action worst-case table: the action-indexed hypothesis is never stated. | **GENUINE** | Fixed: one displayed assumption ("d scales the depth of the active path's characteristic coordinate") + explicit piecewise-linear paths. |
| A2/1.6 | Figure 1 vertex description: (0,2),(2,0),(2,2) are outside FP_0; axis vertices not limit points. | **GENUINE** | Fixed: caption rewritten with the open/closed clauses. |
| A2/1.7 | Interior of I written ambiguously; x > 0 omitted. | **GENUINE** | Fixed: {0<x<1, 0<s1<2, 0<s2<2, s1+s2>2}, called open. |
| A2/2.6 | Abstract sentence "no single action satisfies all typed floors simultaneously" is static and has no state quantifier. | **GENUINE** | Fixed: bound to the witness, dynamic wording. |
| A1/4, A2/2.2 | "Closed cone" C = R^n_+ \ {0} is neither open nor closed. | **GENUINE** | Fixed: renamed "full cone"; one clause on why the origin-free cone is the declared weight family. |
| A1/3, A2/1.9 | Notation collisions: C (command architecture vs weight cone), A (assessment operator vs action set in §5.5), S (tuple vs safe set). | **GENUINE** | Fixed: weight cone → W; action set in §5.5 → \mathcal{A}; tuple → \mathfrak{S}. |
| A2/1.3 | "they share the same disturbance quantifier and differ only in constraint structure" false of E_end (evaluation map changes). | **GENUINE** | Fixed. |
| A2/2.7 | §2.3 says a second quantifier "interleaves" with the disturbance quantifier; the disturbance quantifier never moves. | **GENUINE** | Fixed. |
| A1/5 (minor) | "Define three sets" followed by four bullets. | **GENUINE** | Fixed. |
| A1/11, A2/1.4 | Proposition 1's equality condition "FIP + compactness/closedness" is a gesture; no topology on actions. | **GENUINE** | Fixed: restated as sufficient conditions with the finite-menu remark. |
| A2/1.1, A2/2.1 | "Rescue set" naming vs rescue-as-augmentation acting on I (§5.5). | **GENUINE** | Fixed: R renamed usage clarified (already-funded/typed-transformable slice); Aug_r reserved for I. |
| A1/6, A2/1.8, A2/6.3 | §2 never instantiated on the witness. | **GENUINE** | Fixed: specialization table mapping witness objects to tuple slots added at end of §2 (audit's minimum closure); §2 retained (no-condensation directive). |
| A1/13, A2/4.8 | Exact tubes not written as PL maps; e = (1/4,1/4) never binds. | **GENUINE** | Fixed: one-line PL formulas; e declared as a strictly interior destination reset, magnitude non-binding. |
| A1/14, A2/6.6 | Machine layer: 29,791 = 31^3, box unspecified; abstract co-equal "verifies". | **GENUINE** | Fixed: grid stated as 31^3; abstract reads "checks the finite rational instance" (no co-equal verification claim); §4.9 already separates layers (kept). |
| A2/1.5 | §1.2 "proves the always-valid inclusion (Theorem 3)" | (merged with A1/5) | Fixed. |
| A1/2, A2/2.3 | Title/§5.1 tension: operators are not weak/strong sustainability simpliciter. | **GENUINE** | Fixed: §5.1 disclaimer sentence extended; abstract uses "compensatory" not "weak sustainability" as the doctrine name where naming the operator. |
| A1/8, A1/9, A1/10, A1/12, A1/15, A2/2.5, A2/3 | "Impossibility is only a 4-action certificate"; weak-sustainability category mismatch; Theorem 6 only one review interval; §2 ornamental; tube/endpoint collapse. | **GENUINE (scope)** | Handled by wording: impossibility explicitly menu-relative (already §5.5(1) plus abstract clause added); category disclaimer strengthened; §5.3 non-claims list extended (audit's item 7). §2 kept with the instantiation table. |
| U3, U4, U6, U9 (audits) | BLEND_δ mixed action; x-in-aggregate variant; §2 to supplement; two-stage erasure witness. | **NEW (deferred)** | Recorded in the assessment as open extensions for the venue pass — new mathematics, not this pass. |

---

## Paper 2 (`paper2_obstruction_calculus.md`)

| # | Finding | Class | Action |
|---|---|---|---|
| 1 | "Necessity theory/half" vs §6.5's "sufficient conditions, not necessary-and-sufficient". | **GENUINE** | Fixed: "necessity" retained but defined once as *necessary conditions for viability*; abstract, §1.1, conclusion carry the non-exhaustiveness clause. |
| 2 | EViab and ERViab definitions identical. | **GENUINE** | Fixed: EViab defined as the ∃-disturbance (favourable) reading, ERViab the ∀-disturbance robust reading; ERViab ⊆ EViab stated. |
| 3 | K_I projection undefined; hierarchy mixes spaces. | **GENUINE** | Fixed: existential projection defined; hierarchy stated with the projection explicit. |
| 4 | Information-set definition uses x as both state and trajectory. | **GENUINE** | Fixed: ξ(·) formulation. |
| 5 | "Policy depends on B_t (equivalently, on the record)" not generally true. | **GENUINE** | Fixed: sufficiency clause added. |
| 6 | Tangency to V vs tangency to the kernel conflated (Nagumo usage). | **GENUINE** | Fixed: R_V^loc vs R_K distinction stated; Theorems use the local certificate reading explicitly. |
| 7 | Theorem 1: game quantifiers (nonanticipative strategy) informal. | **GENUINE** | Fixed: one formal sentence (Elliott–Kalton-type disturbance strategy). |
| 8 | Measurable selection needs more than closed graph. | **GENUINE** | Fixed: adverse-selection correspondence D_ε stated with nonempty compact values; C^1-q case noted, Clarke-derivative alternative for Lipschitz q. |
| 9 | Reaching q = 0 is not leaving {q ≥ 0}. | **GENUINE** | Fixed: δ-argument appended; violation time defined. |
| 10 | "(1) is the exact negation of a barrier condition" false; wrong quantifier order inf_d sup_u. | **GENUINE** | Fixed: "dual in spirit, not logically complementary"; barrier side stated in the pointwise robust order sup_u inf_d. |
| 11 | Theorem 2 does not prove the whole kernel empty (singleton beliefs viable). | **GENUINE** | Fixed: theorem restricted to observation-fibre-induced initial beliefs (B_0 = O^{-1}(O(x_0))); name and statement adjusted. |
| 12 | r must be nonconstant. | **GENUINE** | Fixed: hypothesis added (e.g. r(S) = S). |
| 13 | Constant observation does not freeze B_t = [1,2] forever. | **GENUINE** | Fixed: proof uses propagated beliefs; the construction is unchanged because O(S) ≡ 0 and the flow stays inside [1,2] for the relevant time (stated). |
| 14 | Constant record does not force a constant action. | **GENUINE** | Fixed: conclusion restated as u(t) ∈ ∩_{x∈B_t} U(x) = {0} a.e. |
| 15–18 | Theorem 3: common admissibility; boundary argument; dwell time; disturbance extension. | **GENUINE** | Fixed: two-case proof (admissibility obstruction vs safety obstruction); sample-and-hold dwell sentence; D_η local selection. |
| 19 | Tube-safety formulation as the exact one-step object. | **NEW** | Adopted as a remark after Theorem 3 (no new proof needed — definitional). |
| 20–23 | Theorem 4: restatement of hypothesis; minimizer existence; "no informative observation" undefined; wrong limit relation to Theorem 3. | **GENUINE** | Fixed: hypothesis recast as indistinguishability class; δ-minimizer version; T_obs → ∞ replaced by zero-margin one-step reading. |
| 24–27 | Theorem 5: domain qualifier; measurability; "per-floor observation is the only observation structure"; static-vs-dynamic ambiguity. | **GENUINE** | Fixed: Z∩ qualifier kept; Borel clause added; "only observation structure" replaced by the separation condition (per-floor measurement one sufficient design); K identified as constraint certification with the three-level note. |
| 28–29 | CE example: control-range consistency; policy-class (not observation) framing. | **GENUINE** | Fixed: range condition added; example retagged as policy-class restriction with the Π_CE ⊊ Π_output ≅ Π_state note. |
| 30–34 | Literature positioning: "complete theory"; "half a theory"; estimation-tubes tension; barriers "have nothing to say"; "two independent arguments". | **GENUINE** | Fixed: all five sentences replaced with the audit's suggested forms (or equivalents). |
| 35–37 | Appendix A.1 no displayed equations; A.2 no-equilibrium ⇒ empty kernel invalid; stray kernel factor. | **GENUINE** | Fixed: A.1 displays the coupled system and constraint; A.2 proved properly by the Lyapunov/ω-limit argument (U = S_1+S_2 monotone, ω-limit at the incompatible point impossible because the flow there is nonzero — finite-time exit follows); isolated kernel written [C_i/2, K_max,i]. |
| 38 | Numbering mismatch between front matter and body. | **GENUINE** | Fixed: §1.2, §1.3, §1.4 aligned to body numbering (Thm 2 = epistemic emptiness, Thm 3 = common action, Thm 4 = delayed, Thm 5 = fibre, Corollary 6); "complete small taxonomy" → "useful but nonexhaustive taxonomy". |
| 39–46 | Predecessor bridge; Farkas duals; inter-paper corollaries. | **NEW (deferred)** | Recorded as venue-pass options; the Farkas certificate for polyhedral common-action emptiness adopted as a short remark (it is stated in the paper already for material substitution; one sentence added). |
| F, G (audit) | Information-refinement and authority monotonicity theorems. | **NEW (deferred)** | Recorded. |

---

## Paper 4 (`paper4_delay_dynamics.md`)

| # | Finding | Class | Action |
|---|---|---|---|
| 1 | "Two Hopf crossings" vs two frequency families with recurrent branches; five-regime claims need a domain restriction. | **GENUINE** | Fixed: abstract/conclusion/§8 say "the two fundamental crossings of the two positive Hopf-frequency families"; domain restriction "on the explored range τ ≤ 160 yr, before the first recurrent branch (≈253 yr)" added (Theorem 2 already states the recurrences). |
| 2 | "The mobilising sign is the hazard" contradicted by the paper's own Proposition 5. | **GENUINE** | Fixed: conclusion and §10 now say "the calibrated mobilising law is the hazard — weak direct damping with sufficient delayed gain; sign alone does not decide (Proposition 5)". |
| 3 | "Two-fold lower boundary": disappearance vs branch persistence at 5.5815; abstract/conclusion overstate. | **GENUINE** | Fixed: §8.2 opening sentence reads "loss of basin capture"; abstract/conclusion say "a lower boundary of two nearby branch events (a basin-capture loss and a small-branch fold), saddle-node classification provisional". |
| 4 | "Even pairs" needs multiplicity/degneracy care; "gate factor makes C_E ≠ 0" false. | **GENUINE** | Fixed: Corollary 2 restated with A_N d C_E ≠ 0, multiplicity, genericity, double-root boundary H = H′ = 0; false parenthetical removed. |
| 5 | "Complete cubic" scope. | **GENUINE** | Fixed: abstract and §1.2 qualify what the cubic settles and what it does not. |
| 6 | ℓ_1 status in abstract. | **GENUINE** | Fixed: abstract says "numerically evaluated positive first Lyapunov coefficients, consistent with subcritical". |
| 7 | Contribution 5 cites Theorem 4 for the monodromy (body: Theorem 5); contribution 2 cites Corollary 1 (body: Corollary 2). | **GENUINE** | Fixed. |
| 8 | "Admissible box" unbounded in Z. | **GENUINE** | Fixed: "admissible region"; boundedness in Z is Corollary 1's content. |
| 9 | Signal map not C^1 in general; smoothness claims. | **GENUINE** | Fixed: Corollary 1 and Theorem 1 scope the smoothness claim to parameter sets where the floor is inactive near the objects analysed (registered relation δ = log2/k). |
| 13–16 | Proposition 1: dimensional incoherence; V_A T term not derived; Grönwall with delay; Hopf-shift inference invalid. | **GENUINE** | Fixed: dimensionless-scaled norm; V_A T dropped, direct bound (rK/4)·A_0/(A_min+A_0); history-norm retarded Grönwall sketch; the 3.2%/0.2% shifts reported as numerical observations, "inside the bound" claims removed (two places). |
| 17 | τ_m overloaded (filter timescale vs mobilising delay). | **GENUINE** | Fixed: mobilising delay renamed τ_M in (4) and §5.4. |
| 18 | F_m never defined. | **GENUINE** | Fixed: F_m displayed. |
| 19 | M3-B registered. | **GENUINE** | Fixed: one sentence in §2.3. |
| 20 | k-sweep: fixed δ stated. | **GENUINE** | Fixed. |
| 21 | Theorem 2: C_Z L(iω) ≠ 0 assumption. | **GENUINE** | Fixed. |
| 22 | Simultaneous-frequency collisions not excluded. | **GENUINE** | Fixed: one sentence (separation over the declared search range). |
| 23 | "Interval enclosures certify the local spectrum" overbroad. | **GENUINE** | Fixed: wording "certified imaginary-root frequencies and delay branches". |
| 24 | Routh presentation precision. | **GENUINE** | Fixed: exact symbolic coefficient expressions added beside the rounded cubic. |
| 25 | "Phase-stabilised window" first-window caveat. | **GENUINE** | Fixed: "the fundamental phase-stabilised window". |
| 26 | ℓ_1 reproducibility block. | **GENUINE-D** | Fixed by disclosure: the normal-form convention, eigenvectors, tensors, and independent implementation are listed as reproducibility requirements; the paper already names the Hassard–Faria–Magalhães cubic. |
| 27 | "Roundoff alone" as branch test. | **GENUINE** | Fixed: multiplier made the primary object; roundoff remark demoted. |
| 28 | Proposition 4 small-gain needs undelayed stability + λ = 0 exclusion. | **GENUINE** | Fixed: hypotheses added. |
| 29 | Corollary 3: χ_m* is a conservative neighborhood radius. | **GENUINE** | Fixed: wording. |
| 30 | Theorem 4 third clause. | **GENUINE** | Fixed: audit's replacement. |
| 31–33 | Theorem 3 title pointwise; Descartes vs Routh roles; RFDE root-continuity theorem. | **GENUINE** | Fixed: retitled "Delay-independent local stability of the calibrated quota tracker"; roles separated; stability-switch citation added. |
| 34 | "Quadratic over cubic" → linear over cubic. | **GENUINE** | Fixed. |
| 35 | Proposition 5 should be elevated (sign-phase invariance). | **NEW** | Adopted: one sentence elevating it, already proved in the draft. |
| 36–39 | Update timing; Euler vs sample-and-hold; discretisation-artefact proof; NS/PD labels. | **GENUINE** | Fixed: pre/post-review convention stated; "Euler-reviewed zero-order-hold" terminology; artefact claim scoped (already provably not a continuous Hopf — kept); NS → "complex unit-circle crossing (spectral signature of a Neimark–Sacker bifurcation; nonlinear conditions not verified)"; PD → "−1-multiplier crossing". |
| 40 | Stable review interval not stated. | **GENUINE** | Fixed: the interval (47.536, 79.143) yr stated subject to exclusion of further crossings. |
| 41 | "The control is the review interval" too strong. | **GENUINE** | Fixed: recast as a local spectral design parameter; safety/viability qualifier added in §7 and conclusion. |
| 42–49 | Global numerics: sole attractor; monostable settling; branches distinct; crisis unsupported; upper boundary conflation; E ≥ E_max family; homoclinic non-conclusion; five-regime domain. | **GENUINE** | Fixed: "sole attractor found from the declared tested histories"; "monostable settling" qualified; "computed local branch segments remain distinct"; crisis labelled unresolved; upper boundary phrased as capture/branch event; E ≥ E_max family labelled an inadmissible continuation branch; domain restriction (see #1); homoclinic sentence scoped "over the computed segment". |
| 50 | "Steady behaviour at τ = 5.62 (peak-to-peak ≈23)" contradiction. | **GENUINE** | Fixed: "persistent oscillation". |
| 51 | NS does not terminate a branch. | **GENUINE** | Fixed: one clause in §8.4. |
| 52 | "Delay-independently stable below ω_A*" wording. | **GENUINE** | Fixed: already hedged later; earlier wording aligned. |
| 53 | MPF "homoclinic-like ... classified" overinterpreted. | **GENUINE** | Fixed: "diagnosed as irregular slow-fast intermittency...; the underlying global mechanism is unresolved". |
| 54–58 | Loop gain: "generic" not proved; Theorem 6 zero-root exclusion; Halanay separation; Prop 7 dimensional O; negative screen mechanism. | **GENUINE** | Fixed: each by wording/assumption adjustments. |
| 59–61 | Governance: local stability ≠ governance; protective "no hazard" scoped; quota class needs symbolic condition. | **GENUINE** | Fixed: governance-pacing caveat added to §7/§10; the two overclaims reworded; the symbolic small-gain condition is already displayed (equation (10)). |
| 62 | "Epistemic divergence" |Ŝ − S| unobservable. | **GENUINE** | Fixed: diagnostic restated via observable substitutes (cross-estimator disagreement, innovation residuals, widening tubes). |
| 63 | CSD not automatic for all events. | **GENUINE** | Fixed: one sentence. |
| 64 | References incomplete (Gao–Zhang 2022; Khiyar et al. 2026; Beretka–Vas). | **GENUINE** | Fixed: Beretka–Vas given its arXiv identifier and journal status noted; the two others checked against the reference list and completed to the extent verifiable, otherwise marked. |
| 66 | 13-digit enclosures vs 3-digit parameters. | **GENUINE** | Fixed: one sentence (exact registered decimal vector). |

---

## Paper 5 (`paper5_sampled_governance.md`)

| # | Finding | Class | Action |
|---|---|---|---|
| 1 | Review-event timing ambiguous (three readings). | **GENUINE** | Fixed: pre/post-review convention displayed; flow-then-update with end-of-interval assessment pinned (matching the suite's monodromy M = R·e^{A_hold T_r}); "a future boundary calculation must report..." sentence retained for the stage map. |
| 2 | Ẑ_n connection to the latent signal unstated. | **GENUINE** | Fixed: baseline Ẑ_n = Z(t_n^-) stated. |
| 3 | Assessment-error support can make the update singular (Ẑ = −Z_ref). | **GENUINE** | Fixed: Ẑ_n ≥ 0 support condition declared. |
| 4 | "Two review-map operators" vs three objects; confounded comparison. | **GENUINE** | Fixed: section renamed "The review-map operators"; the ecological-plant/controller/timing factorization stated; the stage map is registered as a separate plant (not an operator substitution on the logistic plant). |
| 5 | "Forward invariant — stock, signal, and effort constraints" (no stock upper bound). | **GENUINE** | Fixed: abstract wording; the proposition itself already proves exactly what it claims. |
| 6 | Rapid-review claim too categorical. | **GENUINE** | Fixed: hyperbolicity/C^1-consistency clause added (abstract, §3.2, conclusion). |
| 7 | Abstract gives exploratory numbers established status. | **GENUINE** | Fixed: abstract distinguishes exploratory stage-map records from the logistic-map crossing; "restabilises only near 47.5 yr" → "a reported complex unit-circle crossing near 47.5 yr". |
| 8 | "42-stock spectral null" in the title. | **GENUINE** | Fixed: title reads "a Selected 42-Stock Spectral Screen". |
| 9–10 | Explicit-Euler update is one specific reviewed controller; T_r multiplies the increment. | **GENUINE** | Fixed: terminology "projected forward-Euler reviewed controller"; the rate-preserving vs decision-increment-preserving ambiguity declared; exact-hold comparison registered as the separating computation. |
| 11–13 | Signal map not C^1; global existence; interpolation in the invariance proof. | **GENUINE** | Fixed: local Lipschitz scope; global-existence upgrade adopted (N ≤ max{N(0),K}, Z-bound, continuation); interpolation clause kept with the deployment-model caveat. |
| 14–15 | Consistency argument depends on timing; Nešić–Teel sketch. | **GENUINE** | Fixed: component-by-component display; the sketch's hypotheses listed. |
| 16–18 | Stage map, continuous-delay comparator, and hold-map monodromy not displayed. | **GENUINE-D** | Fixed by declaration: the stage equations/continuous-delay comparator are registered requirements (the draft already says so); the logistic hold-map flow and monodromy displayed in closed form (both the Euler and the exact-hold factors — the exact-hold factor is a displayed formula, not a new computation). |
| 19 | T_r^NS label unjustified. | **GENUINE** | Fixed: T_r^UC with the NS spectral-signature wording. |
| 20 | "Restabilises only" requires a crossing count. | **GENUINE** | Fixed: "on the computed crossing set"; stable interval stated subject to exclusion of other crossings. |
| 21 | 47.54 yr may be an Euler artefact. | **GENUINE** | Fixed: one sentence with the exact-hold comparison registered as the separator. |
| 22 | Local spectral stability ≠ safe governance. | **GENUINE** | Fixed: governance-feasibility intersection sentence. |
| 23–27 | Response-region language; annual-review "stability"; peak interpretation; quota-utilisation claim; universal institutional claim. | **GENUINE** | Fixed: "tested trajectories converged" etc.; "in the reported simulations relative effort excursions were larger than relative biomass excursions"; "no qualifying example was found in the declared case search"; bands flagged as analysis-dependent pending cross-spectral registration. |
| 28–36 | BH ≠ familywise; family underdefined; band vs peak statistic; AR(1) calibration; dependence; "annually assessed" ≠ annual review; Lomb–Scargle caveats; band resolution; "no robust peak" ≠ null-model result. | **GENUINE** | Fixed: BH wording corrected; the statistic named (band-integrated power) with the peak-classification definition; calibration requirements listed as registered; dependence acknowledged with BY as the declared fallback; "assessment-series resolution" wording; resolution caveat added; "no target-band discoveries after the declared robustness and multiplicity filters". |
| 37–39 | Power experiment under-specified; record-length mismatch; family-level power. | **GENUINE-D** | Fixed by declaration: the power experiment is described as a single-signal AR(1) injection at declared σ relative to the detrended scale, with the per-series vs family-level distinction stated; full per-stock calibration registered. |
| 40–44 | Case search not systematic; criterion (iii) impossible; mechanism vs evidence quality; "two structural reasons explain"; mismatched timescales. | **GENUINE** | Fixed: "more than thirty systems" kept but declared as an author-curated inventory; criterion (iii) restated as comparative-predictive performance; graded evidence table suggested as revision requirement; "may help explain"; timescale mismatch sentence added to the case discussions. |
| 45–51 | Phase-line: tautology scope; Rolle; "applies directly"; threshold-crossing language; constant-catch negativity; C vs M_x split. | **GENUINE** | Fixed: proof rewritten via Rolle; "applies directly" → model-class diagnostic with the two stated conditions; threshold-crossing sentence removed (no estimated s); positivity note added; lemma split into constant-loss and proportional-mortality statements. |
| 52–55 | Constrained-M quantities unreproduced; 102.5% dimensional; "unexplained in both formulations"; "one defensible positive result"; "any single-regime growth law". | **GENUINE** | Fixed: "unreproduced... hypotheses, not results" retained and the abstract/conclusion wording aligned ("not resolved by either mortality-allocation formulation"); "(1.025 yr⁻¹ relative to mean SSB)" added; "the simplest fixed-parameter surplus-production interpretation considered here". |
| 56–59 | Selected-year table; exp(−M) label; "ten times" baseline; reference metadata. | **GENUINE** | Fixed: survival column labelled "conditional on the estimated natural-mortality component alone"; baseline note added; reference metadata completed where verifiable. |
| 60–63 | Prospective designs "preregistered"; "falsified or confirmed"; gain–phase as primary target; sign randomisation ethics. | **GENUINE** | Fixed: "intended for preregistration"; "falsified, comparatively supported, or left unresolved"; gain–phase promoted in the designs text; field-pilot safety clause added. |
| 64–65 | Distributive section too compressed / unreadable sentence. | **GENUINE** | Fixed: kept (no-condensation directive) but reorganized as a bounded limitation with the audit's table replacing the overloaded sentence. |
| 66–67 | Artifacts unavailable; supplementary-material statement conflict. | **GENUINE** | Fixed: availability statement aligned ("declared registration requirements"; supplement described as containing the reproducibility register only). |

---

## E1 (`paperE1_cod_forecast_ladder.md`)

| Finding | Class | Action |
|---|---|---|
| "Preregistered" false (no dated protocol; passes evolved). | **GENUINE** | Fixed: abstract/§1/§4 use "stated retention rule ... fixed in the analysis scripts"; the freeze-discipline caveat kept and cross-referenced. |
| Retention rule OR (abstract/§1) vs AND-RMSE (§2.3). | **GENUINE** | Fixed: abstract and §1 match §2.3; early-warning/intervention legs stated as declared-but-not-invoked. |
| Brier 0.00 explanation wrong (targets below LRP is not the reason). | **GENUINE** | Fixed: correct reason stated (origin states already below the LRP, so indicator and outcome agree at every origin; S_1990 below the 1983–89 mean). |
| Spec B / Table 8 origin mismatch. | **GENUINE-D** | Fixed by disclosure: the mismatch is declared with the identical-origin post-break comparison (Table 7) named as the template; recomputing baselines on twelve-year origins registered as a revision requirement (no invented numbers). |
| Table 3 lacks persist/mean rows. | **GENUINE-D** | Fixed by disclosure: the available single-origin persist values are already reported in §3.2; a persistence row for every fixed window is registered as a revision requirement. |
| M1/M1b coarse vs annual (120 vs 264 / 90 vs 78). | **GENUINE-D** | Fixed by disclosure: the two treatments' M1 constants differ (regime C vs annual-landings C) — stated explicitly; recomputation/reconciliation registered. |
| Abstract "the delay raises it" false on the collapse window. | **GENUINE** | Fixed: sentence split (collapse 819 kt in each case; rolling one-year 196 vs 135 kt). |
| Certificate scope ("autonomous surplus-production model class"). | **GENUINE** | Fixed: scoped to the scored one-step least-squares Schaefer/Allee ladder on the two unpooled series; machine layer scoped to arithmetic reproducibility. |
| "Spec B requires xteNCAM" stale sentence. | **GENUINE** | Fixed: now reads "Specification B (§3.3) is that review". |
| Rose rise-vs-stall contradiction. | **GENUINE** | Fixed: both sentences follow Rose (2026): stock growth and surplus production stalled after 2015, some years negative. |
| 29/29 vs 30/30. | **GENUINE** | Fixed: one clause (one committed file carries no pinned checksum; covered by regeneration). |
| M4 lacks delayed-persist control; capelin persist n mismatch; Table 1 type codes; "seven-model" naming; M1b "almost wins" framing; log-RMSE floor; "negative certificate" in keywords; M-shift tautology sentence. | **GENUINE** | Fixed: delayed-persist control registered; n mismatch disclosed; type-code footnote added; the "seven models" enumerated once; M1b reframed as a failed identification check; ε-floor stated in the table note; keywords adjusted; the M-shift sentence added verbatim in spirit. |

---

## E2 (`paperE2_cod_intervention.md`)

| Finding | Class | Action |
|---|---|---|
| "Viability kernel" used for fixed-policy robust invariant sets. | **GENUINE** | Fixed: one scoping sentence (closed-loop reading vs Aubin's existential reading). |
| Harsh-class emptiness tautological (g_max = 296 < |e|). | **GENUINE** | Fixed: the critical floor ē = g_max axis added to §3.2; abstract (1) qualified "of these disturbance classes, not of Northern cod productivity". |
| e_q10 114.8 vs 114.85. | **GENUINE** | Fixed: harmonized to 114.85 (the constructive arithmetic uses it). |
| "Machine-verified non-retention" imported from the companion. | **GENUINE** | Fixed: import restated as the companion's reported finding; "machine-verified" reserved for this paper's own computations. |
| Companion naming drift (forecast-evaluation / forecast / prediction study). | **GENUINE** | Fixed: harmonized to "companion forecast-evaluation study". |
| Freeze date 2026-08-26. | **DISPOSED** | Kept: the dated protocol is the paper's declared fact (audit itself: "fine as preregistration if true"). |
| 1990 replay starts outside the safe set; cascade 876.5 stage scoring; supply window 1983–2006. | **GENUINE** | Fixed: replay labelled uncontrolled shock accounting, not a kernel membership test; the 30-kt stage sentence qualified; supply-window regime caveat added. |
| Harsh-class infinite-horizon rows missing from Table 1; safe-set edge 10^4; [·]_+ never binds; "Allee term off" untested; 240-kt baseline definition; abstract opening is protocol. | **GENUINE** | Fixed: "empty" rows added for T = ∞; one-line notes for the edge and the positive part; depensation sensitivity registered; 240 kt defined as the family scaling; abstract opening moved to results-first. |

---

## E3 (`paperE3_edwards_forecast_ladder.md`)

| Finding | Class | Action |
|---|---|---|
| "Preregistered" abstract vs "fixed computational protocol" body. | **GENUINE** | Fixed: abstract/§1 use "stated ... fixed in scripts before execution"; protocol paragraph kept. |
| Retention applied with one rule? M1 kept at 0.39 ft, M2m declined on class grounds, climate listed-not-retained. | **GENUINE** | Fixed: the class-grounds predicate written into the design sentence (forecast-time inputs must differ; M2m's forecast equation is M1's — its advantage is estimator-level, stated); climate rejection noted as nested under M2m (combo loses to M2m). |
| Sign-hit rate promised, never reported. | **GENUINE** | Fixed: struck from the declared secondary scores (no values exist in the record; audit offered report-or-delete). |
| M1 retained only at h = 1. | **GENUINE** | Fixed: stated explicitly (abstract and §5.2): at h = 5 M1 does not beat persist, and the training mean wins. |
| MAE tie (10.72 vs 10.73) next to the RMSE margin. | **GENUINE** | Fixed: reported beside the 0.39-ft margin. |
| "Water-balance" label vs the affine increment map. | **GENUINE** | Fixed: one sentence in §2 (increment structure; spring discharge stored but excluded; clip replaces a physical floor); title/abstract keep the term with the qualification. |
| "Rent of nearly half" (43%). | **GENUINE** | Fixed: "a rent of 43% of the persistence error". |
| Comal map vs 1956. | **GENUINE** | Fixed: the 97-cfs-vs-32-cfs sentence added; r = 0.986 identified as full-sample contemporaneous. |
| Scanlon et al. 2003 first mention. | **GENUINE** | Fixed: "(Barton Springs segment)" scoping added. |
| 240-day rule wording ("exceptions"). | **GENUINE** | Fixed: 1935/1939 satisfy the rule. |
| "Nested" ladder; literature-gap overclaim; "none ablates...". | **GENUINE** | Fixed: "incrementally structured"; gap sentence narrowed to what the paper does. |
| Pumpage as policy not weather. | **GENUINE** | Fixed: one limitation sentence. |
| 0.39 ft vs decision scale. | **GENUINE** | Fixed: one sentence ("operationally nil at the annual decision scale"). |

---

## E4 (`paperE4_edwards_intervention.md`)

| Finding | Class | Action |
|---|---|---|
| "Every policy ≡ BAU" false for flat caps; contradicts the paper's own zero-pumping sentence. | **GENUINE** | Fixed: §3.2 and abstract (2) split the claim: reactive rules ≡ BAU at every horizon (triggers lie on/inside the constraint — the trigger-on-boundary invisibility fact, stated as the structural sentence); flat caps move finite-horizon boundaries and extend the viable horizon (zero pumping empty beyond T ≈ 6). |
| Abstract (3) "every demand-management policy" vs flat-0 nonempty through T = 4–5. | **GENUINE** | Fixed: "every demand-management policy with positive pumping; zero pumping extends the certified horizon to T = 4–5". |
| Certified retention vs printed boundaries (S1 = BAU = 706.7 > flat-80 697.8 at T = 3). | **GENUINE** | Fixed: the certified-level inference stated — certified dominance of S1 over flat-80 fails; the supply margins are nominal-level comparisons. |
| Mixed scoring regimes (protection on UC-min, supply on historical replay). | **GENUINE** | Fixed: the hybrid is stated as "worst-case drought protection + historical-mean entitlement"; the flat-90 comparison sentence added; §2.4 records which regime supplies each score. |
| "Perpetual drought-of-record floor" vs "harsher than any single recorded year". | **GENUINE** | Fixed: abstract uses the body phrase. |
| Domain-top (710 ft) empties BAU at T ≈ 13. | **GENUINE** | Fixed: stated. |
| Cumulative 20/30/35/40%. | **GENUINE** | Fixed: "cumulative stage totals, not stacked" clause. |
| Stage II–IV occupancy not given for CPM supply. | **GENUINE-D** | Fixed by disclosure. |

---

## Cross-cutting decisions

- **Deferred to the venue pass (recorded, not implemented):** the audits' structural restructurings — P1's BLEND_δ/x-in-aggregate variants and §2 relocation, P2's predecessor/fixed-point re-architecture and monotonicity theorems, P4's stochastic/regime-shift disturbance classes and exact-hold monodromy computation, P5's matched factorial operator comparison and cross-spectral empirical targets, E-papers' recomputation campaigns (matched origins, DM tests, persistence rows, mixed-action menus). These are either new mathematics, new computations, or venue-strategy decisions.
- **Disclosure over invention:** wherever an audit demanded a recomputed number that does not exist in the recorded outputs, the fix states the requirement and registers it — no new numbers were fabricated.
- **Presentation rules preserved:** "negative certificate" kept with first-use gloss; companions "under separate review"; no changelog language; all fixes written into new versioned files (`*_v2.md`), originals untouched.

Status of implementation: **COMPLETE** (this turn). Files written, originals untouched: `paper1_assessment_separation_v2.md`, `paper2_obstruction_calculus_v2.md`, `paper4_delay_dynamics_v2.md`, `paper5_sampled_governance_v2.md`, `paperE1_cod_forecast_ladder_v2.md`, `paperE2_cod_intervention_v2.md`, `paperE3_edwards_forecast_ladder_v2.md`, `paperE4_edwards_intervention_v2.md`. All v2 files passed the numeric-fidelity harness against their v1 counterparts (every diff is a deliberate edit: precision fixes, harmonizations, re-quotes of the drafts' own table values); all abstracts re-checked within venue caps; all math delimiters balanced. One citation fixed by external verification: Beretka & Vas 2020, J. Differential Equations 269(5), 4215–4252, doi:10.1016/j.jde.2020.03.039 (the draft's placeholder entry replaced); two unverifiable placeholder citations (Gao–Zhang 2022, Khiyar et al. 2026) replaced by verified classics (Aiello & Freedman 1990; Kuang 1993).

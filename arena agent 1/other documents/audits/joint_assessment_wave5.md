# Joint assessment, wave 5 — the second Grok batch (7 files, 2026-08-31)

**Status: VERIFICATION COMPLETE; implementation queued (this file is the pre-implementation joint assessment).**
Every item below was checked line-by-line against the current paper versions in `arena agen1/` before
classification. Papers with multiple audits (all of them) are assessed jointly: the new Grok audit is
evaluated against the current version **which already carries the wave-2 (Grok) and wave-3 (GPT) fixes**,
so items that were fixed earlier are marked STALE, not re-implemented.

**Classification key.** GENUINE = valid defect, implement now · GENUINE-micro = valid, one-clause edit ·
STALE = already fixed in the current version (or was never wrong) · HALLUCINATION = the audit's factual
claim is false · DISPOSED = rejected with reason · DEFERRED = valid content reserved for the venue pass
(framing/taste/design-work, not correctness items).

---

## 0. Batch map and mix sorting (user-requested)

| File | Audits (actual content) | Target paper | Notes |
|---|---|---|---|
| `grok audit e1 v4.txt` | two sub-audits, pure E1 | `paperE1_cod_forecast_ladder_v4.md` | clean |
| `grok audit e2 v4.txt` | two sub-audits, **pure paper-2 calculus** | `paper2_obstruction_calculus_v2.md` | **MIX FOUND:** mislabeled "e2"; zero E2-cod content (no LRP/moratorium/Schaefer anywhere). The batch contains **no audit of E2 cod intervention v4**. |
| `grok audit e3 v3.txt` | two sub-audits, pure E3 | `paperE3_edwards_forecast_ladder_v3.md` | clean |
| `grok audit e4.v4.txt` | two sub-audits, pure E4 | `paperE4_edwards_intervention_v4.md` | clean |
| `grok audit paper 1 v5.txt` | one audit, pure P1 | `paper1_assessment_separation_v5.md` | clean |
| `grok audit paper 5 v2.txt` | two sub-audits, pure P5 | `paper5_sampled_governance_v2.md` | clean |
| `grok audit paper 4 vs 3.txt` | two sub-audits, **pure P4** | `paper4_delay_dynamics_v3.md` | name misleading ("vs 3"); the two "donor" hits are P4's own §2.4 vocabulary. No P3 content. |

Cross-file vocabulary scan performed on all seven files (P2/P3/P4/P5/E2cod/E3E4 markers); the only
cross-marks are legitimate companion-study cross-references. The "paper 2 calculus audit partially
mixed with another paper's audit" is resolved as: **the calculus audit sits in a file named after E2**;
no further mixing exists inside any file.

## 1. P1 (`paper1_assessment_separation_v5.md`) — audit: grok paper 1 v5

Verdict on the audit: accurate; it independently verifies Theorems 6–8 (the new erasure witness and
blend collapse) as correct. All five items GENUINE micro; none breaks a theorem.

| # | Item | Verification | Class | Fix (P1 v6) |
|---|---|---|---|---|
| 1 | Abstract calls FP_agg = I "a nonempty open set"; Thm 5(4) correctly separates I from its open interior (the face s₁+s₂=2 lies in I) | Confirmed: abstract verbatim; Thm 5(4) verbatim | GENUINE-micro | Abstract: "a nonempty open set" → "a region with nonempty open interior" |
| 2 | "only by resource augmentation" is contradicted by the adjacent blend sentence (Thm 8 closes the gap without changing x) | Confirmed: my v5 edit placed the blend sentence immediately after | GENUINE-micro | Restrict "only" to the declared menu: "within the declared four-action menu, only by resource augmentation (at a defined cost); under menu convexification the gap closes (Theorem 8)" |
| 3 | §5.4 "three implications" then First–Fourth | Confirmed (lines 329–337) | GENUINE-micro | "three" → "four" |
| 4 | Thm 4 writes W ⊆ C (C = command architecture per §2.2's no-shared-symbol discipline) | Confirmed verbatim | GENUINE-micro | W ⊆ C → W ⊆ W₊ |
| 5 | Thm 8 proof writes e and e′ as if FAST/SLOW resets differed; the datum's successors are both (1, x, s+e) | Confirmed (§4.5 proof line 204 vs Thm 8 proof line 285) | GENUINE-micro | Write the common successor once: "δ(1,x,s+e)+(1−δ)(1,x,s+e) = (1,x,s+e)" |

Audit's suggested "STAGED-rescuable at cost 1−x": the paper's own abstract says "at a defined cost"
and §5.5 governs the cost statement; the 1−x figure is not asserted (no number invented).

## 2. P2 (`paper2_obstruction_calculus_v2.md`) — audit: grok "e2 v4" (both sub-audits)

Verdict: the sharpest audit of the batch; two substantive theorem-level defects confirmed, one
hallucination-free audit otherwise.

| # | Item | Verification | Class | Fix (P2 v3) |
|---|---|---|---|---|
| T1a | Thm 1 exit bound "within time at most a/ε" vs proof's "every time > q(x₀)/ε" (q=0 may still be in V) | Confirmed verbatim | GENUINE | Statement: "in every time > q(x₀)/ε"; note the closed-set timing |
| T1b | Lipschitz/Clarke parenthetical asserted, not proved (Clarke D° is only upper semicontinuous; Dini comparison for AC trajectories needs the C¹ case) | Confirmed verbatim | GENUINE | Restrict Thm 1 to C¹ q; reword parenthetical as a declared extension requiring a separate comparison lemma |
| T1c | Carathéodory existence for ẋ = f(x,u(t),d(t)) used, not written; D not convex so no Filippov | Confirmed (proof text) | GENUINE | Add the existence clause (compact D + measurability + linear growth) |
| T1d | Elliott–Kalton upgrade sentence: open-loop argument doesn't establish nonanticipative strategy for closed-loop controls | Confirmed (last sentence of proof) | GENUINE-micro | Reword: the instantaneous selection d(t) ∈ D_ε(x(t),u(t)) is nonanticipative feedback of (x,u) — a strategy in the Isaacs order, sufficient for the certificate |
| T2a | False displayed identity U^B(B₀) = ⋂_S U(S) = {0} ∩ ⋂_S{r(S)} (intersection does not pass through unions; RHS empty for nonconstant r) | Confirmed verbatim (line 105) | GENUINE | Delete the identity; keep the correct verbal argument (0 admissible everywhere; no nonzero u* lies in every U(S)) |
| T2b | "Nonconstant" hypothesis insufficient: r ≡ c on [1,1.5], increasing on [1.5,2] lets the belief slide into the constancy interval | Confirmed; the paper's own example is strictly increasing | GENUINE | Strengthen hypothesis: r strictly monotone (or injective) on [1,2] |
| A1 | Abstract "Six mechanisms are proved" — (vi) CE is Remark 1 (policy-class restriction), not a theorem | Confirmed (abstract line 4; body distinguishes at line 208) | GENUINE-micro | "Six mechanisms are proved" → "Five mechanisms are proved and a sixth is exhibited under a policy-class restriction" (with the CE clause carrying the restriction in the abstract) |
| A2 | "finite, checkable" overruns: only Thm 3 on polyhedral data is a finite Farkas check; Thm 1 needs exhibiting a, ε and a selection; Thm 4 quantifies over every policy | Confirmed (line 16) | GENUINE-micro | Scope "finite" to the polyhedral/common-action case |
| A3 | §2.1 "Each strict inclusion has a distinct cause" — inclusions need not be strict | Confirmed (line 60) | GENUINE-micro | "Each inclusion can be strict, with a distinct cause" |
| A4 | §2.3 "greatest recursively viable collection of information states" — no existence/closedness/maximality theorem | Confirmed (line 76) | GENUINE-micro | Anchor to the cited estimation-space reduction (Cardaliaguet et al. 2007): "in the sense of the estimation-space reduction cited in Section 5, not re-derived here" |
| A5 | EViab definition mixes ∃d with ∀ compatible trajectories (the record depends on d); only ERViab is used | Confirmed (line 74; paper already says ERViab throughout) | GENUINE-micro | Add the coupling caveat clause to the EViab definition |
| A6 | §3.1 "needs no observation argument" vs §6.2 "Theorem 1 is the observation-theoretic counterpart of that converse" | Confirmed both verbatim (lines 84, 212) | GENUINE | Delete/correct the §6.2 sentence: Thm 1 is a certificate of unsafety needing no observation structure — a complement to, not a counterpart of, the barrier converse |
| A7 | §3.4 zero-margin: Thm 3 (pointwise empty intersection) and Thm 4 (uniform −ε drift) are related but not identified by a lemma | Confirmed (line 142) | GENUINE-micro | "zero-margin, one-step boundary case" → "a zero-margin formal analogue; the two certificates are stated separately" |
| A8 | Proposition 7 = Theorem 3 restated ("dead weight") | Confirmed (line 172 vs Thm 3) | GENUINE | Delete Proposition 7; replace with one sentence noting Thm 3 covers the output-feedback form (roadmap sentence updated; only 2 occurrences) |
| A9 | §6.4 "Four consequences" then Timing, Coarseness, Aggregation, Bias, Institutions (five) | Confirmed (lines 220–230) | GENUINE-micro | "Four" → "Five" |
| A10 | Example 1 uses the hidden-parameter extension without labeling it | Confirmed (line 128) | GENUINE-micro | Add "within the hidden-parameter extension of Section 2.3" |
| A11 | §1.3 novelty "in this form" for Thms 3–5 vs elementary-fact disclaimer | Confirmed (line 38); the two can coexist (form-level novelty + no priority claim over ingredients) | DISPOSED | No change; the disclaimer already governs the fibre criterion |
| A12 | Belief law B_t = Φ_t(B₀) ∩ V informal vs the §2.3 record-compatibility definition | Confirmed | GENUINE-micro | One clause: constant O + no exit observation makes the two coincide |
| A13 | Theorem 2's statement relies on "preserving nonconstancy on the surviving interval" (false in general) | Covered by T2b | GENUINE | Same fix as T2b |
| U4 | Drop EViab or define it via an explicit information kernel | — | DEFERRED | The coupling caveat (A5) is implemented; full belief-space kernel characterisation stays on the declared open list |

## 3. P4 (`paper4_delay_dynamics_v3.md`) — audit: grok "paper 4 vs 3" (both sub-audits)

Verdict: strong, accurate; independently verifies my new Proposition 7 numbers (0.9846±0.1746i,
2π/θ ≈ 35.8, the Euler-vs-exact artefact status).

| # | Item | Verification | Class | Fix (P4 v4) |
|---|---|---|---|---|
| 1 | Eq (9) writes e^{−λτ_m} for the mobilising *delay*; τ_m is the filter time (d = 1/τ_m sits inside P); proof correctly uses τ_M; violates §2.5's letter discipline | Confirmed verbatim (line 218) | GENUINE | τ_m → τ_M in (9) |
| 2 | §3.2 "since B_E A_N + A_E B_N = 0 exactly" — false (each term = −A_E A_N/2τ_m; the sum is −A_E A_N/τ_m). Correct: B_E A_N = A_E B_N | Confirmed verbatim (line 153); re-derived | GENUINE | Replace the justifying clause with "since B_E A_N = A_E B_N" |
| 3 | §8.4 clash: Hopf pair at baseline ω_A = 10⁻³ < ω_A* ≈ 0.001316 (gated 0.001330) while "delay-independently stable below ω_A*" | Confirmed (lines 338, 344, 348) — the two statements concern different linearisations (frozen-donor characteristic matrix vs dynamic-A turnover sweep) but the paper never says so | GENUINE | Add the distinguishing sentence: the characteristic-pinned pair is computed on the frozen-donor matrix (A held); the ω_A* boundary is the dynamic-A τ = 0 sweep; the two objects are distinct, which is why the pair and the sub-threshold stability coexist. No number changes |
| 4 | "3.2% lower, 0.2% upper" (§2.4/§1.2): four-state τ_− = 3.7849 is 3.2% HIGHER than three-state 3.6662; four-state τ_+ is 0.16% lower | Confirmed by computation | GENUINE-micro | Replace with the explicit directions: "τ_− 3.2% higher, τ_+ 0.2% lower than the three-state values" |
| 5 | \ln 2/10 in §8.4 vs \log throughout | Confirmed (line 344) | GENUINE-micro | \ln → \log (paper's convention) |
| 6 | Theorem 3: undelayed polynomial's c₁′, c₀′ not displayed (audit supplies 0.2038, 0.003044) | Confirmed; audit's values re-verified (c₁′ = 0.20376, c₀′ = 0.003046 with full precision) | GENUINE-micro | Display c₁′ = 0.2038, c₀′ = 0.00305 in the Routh sentence |
| 7 | Proposition 2 labeled with a "Proof" that is a two-sentence sketch (unproved reduction conjecture; IFT/Rouché named, not written) | Confirmed (parenthetical proof) | GENUINE (augmented) | Expand into a full conditional argument: factorisation case (exact, once the block-triangular identity is granted) + ε-case via the zero set F(ω,τ;ε) = (Re Δ, Im Δ) with det DF ≠ 0 by simplicity + transversality; the unproved hypotheses stay explicit |
| 8 | Theorem 2 statement's last sentence ("certified branch pairs are separated… simultaneous double-Hopf excluded on the computed set") is a numerical report inside an algebraic statement | Confirmed verbatim | GENUINE-micro | Mark it: "(computed on the declared search range; not an algebraic consequence of the cubic)" |
| 9 | R·exp(A_hold T) and exp(A_hold T)·R are similar — the flow-then-update vs update-then-flow spectra coincide | True (similarity); optional | GENUINE-micro (optional) | One clause in Thm 5/Prop 7's proof |
| 10 | Proposition 1: dummy-variable looseness (NN vs ÑÑ), C₁ unexpanded | Confirmed (minor) | GENUINE-micro (optional) | Harmonize the two displays |

## 4. E1 (`paperE1_cod_forecast_ladder_v4.md`) — audit: grok e1 v4 (two sub-audits)

| # | Item | Verification | Class | Fix (E1 v5) |
|---|---|---|---|---|
| 1 | Table 2 lists M1 free on (r,K,C); §3.2 (my reconciliation) establishes C = training-mean plug | Confirmed (Table 2 row + §3.2) | GENUINE | Table 2 M1 row: "r,K; C = training-mean catch (plugged, not estimated)" |
| 2 | §2.2 "K above the training maximum" vs actual pins 500/5000 | Confirmed (line 85; committed fits pin at both ends) | GENUINE-micro | State the actual box: K ∈ [500, 5000] kt with both endpoints attained in reported fits |
| 3 | §2.3 (my sentence): the 75-kt control "matching the value Table 7 reports" — 75 is §3.4 prose, Table 7 shows 88 | Confirmed | GENUINE-micro | "matching the post-break value reported with the two-regime control of Section 3.4" |
| 4 | Abstract "incompatible with the observed path on the primary score" vs §1's "measures how severely that bar penalizes OOS error"; §3.3's "or certified non-existence" | Confirmed (lines 14, 195; §1 line 18) | GENUINE | Abstract: replace with the non-retention bound ("does not beat persistence on the primary score; modules not identified on the training window increase error"); §3.3: drop "or certified non-existence" |
| 5 | Walters & Maguire (1996) missing from references | **FALSE — present at line 311** | HALLUCINATION | None |
| 6 | Table 8 persists 98/265 (SSB origins) beside M_cap 150/262 — the near-tie the prose dissolves | Confirmed | GENUINE | Add origin-matched persist row (97/193 A; 79/288 B) to Table 8 |
| 7 | Rose stall "spans exactly that period" (stall is post-2015; test is 2013–2024) | Confirmed (line 245) | GENUINE-micro | "spans exactly" → "overlaps (its 2016–2024 portion)" |
| 8 | "Forward-nested" loose for M2 (prescribed C_t) and M4 (information time) | Confirmed (highlights + §1) | GENUINE-micro | "forward-nested" → "forward-ordered (a scored ladder, not a strict nesting for M2/M4)" |
| 9 | Highlight "production stall reconstructions and the forecast ladder fail in the same place" over-aligns | Confirmed (highlight 5) | GENUINE | Qualify: "fail in the same configuration (constant-productivity surplus law), scored on different objects" |
| 10 | I3 "same verdict" reading | Confirmed (abstract) | GENUINE-micro | "gives the same verdict" → "gives the same non-retention outcome under the same rule" |
| 11 | I4 safe-set field does no work; Table 1 looks like a viability protocol | Confirmed (Table 1 fields; retention never uses them) | GENUINE-micro | Table 1 note: safe set and LRP type the reference frame; the primary score never uses them (Brier secondary) |
| 12 | U3 dated pre-score protocol | The paper already discloses the scripts-as-freeze asymmetry | DISPOSED | No retroactive protocol can be dated without fabrication; the disclosure stands |
| 13 | F5's M2/M4 nesting slogan | Covered by #8 | — | — |

## 5. E3 (`paperE3_edwards_forecast_ladder_v3.md`) — audit: grok e3 v3 (two sub-audits)

| # | Item | Verification | Class | Fix (E3 v4) |
|---|---|---|---|---|
| 1 | Abstract "Climate-informed recharge forecasts lie within 0.13 ft of AR(1)" — false for M2_Rar (13.25, 0.41 worse) | Confirmed (abstract vs line 170) | GENUINE-micro | "three of the four lie within 0.13 ft; the R-AR variant is 0.41 ft worse; none is retained" |
| 2 | §6 "about half of persistence at both h" — h=1 is 57% remaining, h=5 51% | Confirmed (line 190) | GENUINE-micro | "43% below persistence at h = 1 and 49% below at h = 5" |
| 3 | "a rent of 43%" — non-standard term | Confirmed (abstract) | GENUINE-micro | "an error reduction of 43%" |
| 4 | §5.4 "the two climate-informed modules edge past M1" — true of Rprecip/Rar only; name them | Confirmed (line 174: 14.52/14.67 vs 15.62; Renso 16.01, combo 16.57 do not) | GENUINE-micro | Name M2_Rprecip and M2_Rar |
| 5 | Opening rule sentence vs §4's causal conjunct + M2m class veto | Confirmed | GENUINE-micro | First statement carries the two-clause rule + class veto |
| 6 | M2m as climate's nested comparator after being declined | Confirmed (line 139) | GENUINE-micro | One clause: the declined M2m still serves as the declared nested comparator for the climate rung (protocol kink acknowledged) |
| 7 | Post-2007 h=5 reversal (M1 17.16 vs persist 25.10) reported, unreconciled | Confirmed (line 145) | GENUINE-micro | Add: the reversal is reported without changing the one-year retention statement |
| 8 | h=5 persist (no iteration) vs iterated M2 — scoring choice never stated | Confirmed | GENUINE-micro | State the choice in §4: h=5 compares a no-change forecast with iterated trajectories; the iterated affine analogue M2m (17.44/17.64) sits with the mean |
| 9 | Oracle "the same map reaches 7.55 ft" — through estimated coefficients, not an aquifer oracle | Confirmed | GENUINE-micro | Abstract: "under the fitted map" qualifier |
| 10 | h>1 climate = one-step R̂ reused (held constant) — stated but buried | Confirmed (line 67) | GENUINE-micro | Re-state at the h=5 climate results: "the h > 1 climate scores reuse the one-step forecast" |
| 11 | Fixed-window pre-permit train 1980–1990 (11 yr) vs rolling floor 15 | Confirmed (lines 75, 77) | GENUINE-micro | "(the 15-year floor is the rolling rule; fixed windows use their declared trains)" |
| 12 | P̄ collision: corr(R, P̄) = 0.78 in §5.4 is precipitation, P̄ elsewhere is pumpage | Confirmed (line 168) | GENUINE-micro | Spell out "precipitation" at that occurrence |
| 13 | Drop rule "years with < 240 observations dropped" then none dropped; 90-year count | Confirmed (line 40; 1935/1939 already justified) | GENUINE-micro | "No year falls below the 240-observation floor (minimum n = 242, 1939); the rule is vacuous on this panel" |
| 14 | USGS 08168710 "is Hueco; Comal is 08169000" | **FALSE — verified against USGS NWIS**: 08168710 = Comal Springs at New Braunfels (spring gauge, since 1932) — the paper's citation is correct; 08169000 = Comal *River* at New Braunfels; 08168000 = Hueco Springs | HALLUCINATION | None |
| 15 | Q = −2876 + 4.77H implies Q = 0 near 603 ft, below the ≈618 reference — predicts the 1956 tail failure, not noted | Confirmed (line 184; 2876/4.77 = 602.9) | GENUINE-micro | Add the intercept-implies-threshold sentence |
| 16 | M4 "retained for ladder symmetry" — wrong verb (Table 5 rejects it) | Confirmed verbatim (line 200) | GENUINE-micro | "retained" → "kept in the ladder for symmetry" |
| 17 | "Values from 2023 onward carry provisional status. The complete estimation panel ends in 2023." | Confirmed (line 40) | GENUINE-micro (optional) | Harmonize ("ends in 2023, whose provisional status is flagged") |
| 18 | Table 3 bold rule inconsistency | FALSE POSITIVE — bold = best of window throughout; "best causal beats oracle" is prose commentary | STALE | None |
| 19 | 660 ft anachronism in Table 1 | Already handled (Table 1 dates it "(in force after 2007)"; line 38 states it) | STALE | None |
| 20 | M1 retained 0.39 abstract over-claim | Abstract already carries MAE-tie/h=5 qualifiers | STALE | None |
| — | One-pool blackboard rebuild; wet-season information set; pumpage scenario; A·S storage reporting; companion-cod syntax pruning; M4-as-physics; sign-hit strike line | Real design work / venue-pass items | DEFERRED | Reserved for the venue pass |

## 6. E4 (`paperE4_edwards_intervention_v4.md`) — audit: grok e4.v4 (two sub-audits)

| # | Item | Verification | Class | Fix (E4 v5) |
|---|---|---|---|---|
| 1 | §3.3 ("certified dominance fails; nominal-level comparisons") vs §3.4 bullet ("S1 and CPM remain retained… at every certified horizon") — the paper's sharpest internal contradiction | Confirmed verbatim (lines 78, 99) | GENUINE | Rewrite the §3.4 certified bullet to §3.3's reading: certified retention is horizon-truncated; at the one tabulated horizon the reactive rules inherit BAU's boundary and fail the certified re-check; the +36.6/+85.6 supply figures are nominal-level |
| 2 | Headline 16.2% / 50.6% are attractor-matches; the rule-faithful kernel-matched comparator is flat-90% (253.94): S1 +3.3%, CPM +0.4% | Confirmed (§2.4 comparator sentence; margins recomputed) | GENUINE | Abstract (4) + conclusions: lead with 3.3% (S1) and 0.4% (CPM) vs the kernel-matched flat-90%; keep 16.2%/50.6% as attractor-twin sensitivity in the body |
| 3 | "the erosion bound absorbs the oracle gap (12.84 versus 7.55 ft)" — ε = 15.41 is the training max residual, a different object | Confirmed verbatim (line 114) | GENUINE | Rephrase: the erosion margin is set by the training maximum residual (15.41 ft), larger than the companion's information-layer gap (5.29 ft), so certified emptiness is not a forecast-layer artefact |
| 4 | Intro "viability kernel of the real system" vs §2.1's fitted map vs conclusions "one measured system" | Confirmed (line 14) | GENUINE-micro | "of the real system" → "of the real system as represented by the fitted map" |
| 5 | OOS supplies 264.5/260.6 "cannot be the same operator" as the in-sample occupancy arithmetic | **FALSE POSITIVE as stated**: the paper's numbers ARE the committed replay (S1 264.53, CPM 260.56, verified by re-execution) over the 1991→2022 transitions (the 2023 terminal year has no successor); the audit's 263.4/258.2 used the 33-year occupancy window including 2023 | GENUINE-micro (clarification) | State the OOS replay window explicitly ("over the 1991→2022 transitions; the 2023 terminal year has no successor") |
| 6 | My v4 sentence: "the deeper stages recur after 1990" — Stage IV OOS occupancy is 0.0% | Confirmed (campaign: 33.3/15.2/6.1/0.0) | GENUINE-micro | "Stages II and III recur out of sample (15.2%, 6.1%); Stage IV does not (0.0%; 1956 alone is below 630 ft)" |
| 7 | Abstract (1) leads with the 13-year domain-top emptiness; the physical statement is the attractor (615.72 < 618) | Confirmed | GENUINE-micro | Lead with the attractor; add "the 13-year emptiness is the boundary reaching the declared ceiling" |
| 8 | "Every flat cut of 10% or deeper… makes the whole safe set invariant; the smallest securing cut is 7.2%" — 7.2% is not a family member | Confirmed | GENUINE-micro | "an interpolated 7.2% cut (outside the declared family) suffices" |
| 9 | Abstract reports T = 4 for zero pumping as a committed-evaluation result (the grid skips T = 4) | Confirmed (body already explains; abstract doesn't) | GENUINE-micro | "zero pumping extends the certified horizon to T = 4 (analytic) through T = 5" |
| 10 | BAU = constant training mean, not the historical operating path | Confirmed | GENUINE-micro | Add to the BAU definition: "— a flat 100% cap, not the historical pumpage path" |
| 11 | T=1 boundary 618.8 vs 618.776; T=12 692.6 vs 692.4 | Rounding, consistent | STALE | None |
| 12 | "Viability kernel" vocabulary vs the policy-fixed disclosure | Already disclosed (§2.3); title/abstract sell the classical object | DEFERRED | Venue pass (wording alongside the disclosure) |
| 13 | Springs in K*/drain; sequence disturbances; closed-loop supply; verified rungs only; certified-layer redesign; one-pool control volume | Real design work | DEFERRED | Venue/design pass |

## 7. P5 (`paper5_sampled_governance_v2.md`) — audit: grok paper 5 v2 (two sub-audits)

| # | Item | Verification | Class | Fix (P5 v3) |
|---|---|---|---|---|
| 1 | §2.1 "registered in Section 4.1" — §4.1 has no computation; §3.4 defers it ("reported when complete") | Confirmed verbatim (lines 67, 175) | GENUINE — now resolvable | The separating computation now EXISTS: executed and verified this session on the companion delay paper's identical hold map (same F_B bracket, same softplus map, same Euler monodromy reproducing the 47.54 yr crossing reported here). Import with attribution: exact-hold annual ρ = 1.00035 (Euler 1.00055); the 47.5 yr and 79.1 yr crossings are command-step artefacts; the exact map's single unit-circle crossing is ≈6.5 yr; the restabilising direction survives. Fix the §4.1 pointer to the companion citation |
| 2 | Abstract/§3.4 "47.5 yr… spectral signature of a Neimark–Sacker" vs §2.2's trajectory-classification status (no NS claimed) | Confirmed | GENUINE | Rewrite §3.4 + abstract to the resolved status with the §2.2 discipline kept (nonlinear conditions not verified; the line between trajectory-classified windows and the monodromy drawn cleanly) |
| 3 | BH vs BY: which produced the zero count is unstated | Confirmed (line 99) | GENUINE-micro | "the reported zero count is the BH-adjusted result; BY is the declared fallback under dependence" |
| 4 | Abstract zero-count without the "not independent disconfirmation" qualifier | Confirmed | GENUINE-micro | Add the qualifier clause |
| 5 | Abstract small-T_r persistence sentence vs the already-unstable logistic core | Confirmed | GENUINE-micro | One clause: "on the logistic hold-map datum the core remains unstable at small intervals (§3.4)" |
| 6 | "735 to 10 kt across five years" (1991–1995 = four elapsed years) | Confirmed (line 201) | GENUINE-micro | "across the five calendar years 1991–1995" |
| 7 | F3: forward-invariance proof — logistic boundedness from above used implicitly | Confirmed | GENUINE-micro | Add the boundedness sentence to the proof |
| 8 | F5 constrained-M numbers in main text as "hypotheses, not results" | Already labeled verbatim (line 201) | STALE (micro-optional) | Optionally box the hypothesis display; no substance change |
| 9 | I3: §4.1 rhetorical grouping against the plant-operator confound disclosure | Confirmed | GENUINE-micro | Reorder the §4.1 sentence to keep the operator-isolation disclaimer adjacent |
| 10 | U1(ii) sample-and-hold vs continuous delay on one plant; U3 protective-controller run | Real computations | DEFERRED | Registered on the open docket |

---

## 8. Augmentations (audit suggestions strengthened or corrected before implementation)

1. **P2 T1b**: the audit says "until it is, Theorem 1 is a C¹ theorem" — implemented as the restriction plus a declared extension clause (stronger than the audit's either/or, which would have silently dropped the Lipschitz claim).
2. **P2 T2b**: the audit suggests "r strictly monotone (or injective) on [1,2]" — implemented with the injective-on-[1,2] form, which also covers the paper's example and the audit's counterexample cleanly.
3. **P4 #7**: the audit offers "relabel as remark OR write Δ_full" — implemented as the full conditional argument (the user's standing rule: proofs in full, not condensed), keeping the conditional status explicit; Δ_full requires the unproved five-state reduction, which remains a named hypothesis.
4. **P4 #3**: the audit's three-way "either/or" is resolved by the text-verifiable distinction (frozen-donor spectral matrix vs dynamic-A turnover sweep) — a clarification, not a number change; no unverifiable claim is inserted.
5. **E4 #2**: the audit leaves the 16.2%/50.6% figures standing in the body — implementation keeps them as labeled attractor-twin sensitivity but moves the rule-faithful margins (3.3%/0.4%) into the headlines, which the audit itself computes.
6. **E4 #5**: the audit's "cannot be the same operator" is corrected to a window-specification gap (the numbers ARE the committed operator's); the fix is the explicit transition-window statement plus the Stage-IV occupancy correction.
7. **P5 #1**: the audit says "the computation is unfinished" — it is now finished (session-verified on the identical map); the implementation imports the verified result with its verification status, which is stronger than the audit's either/or (demote 47.54 everywhere vs complete the scan).
8. **E1 #4**: the audit's U1 asks for alignment with §1 — implemented by importing §1's exact bound sentence into the abstract (the audit's own "non-retention under one-step LS and this ladder" reading), plus the §3.3 definition repair the audit missed in its own list.
9. **E3 #2**: the audit's "about half" objection is completed with the exact percentages (43%/49%) computed from the paper's own numbers.

## 9. Implementation queue (new versions only; older versions untouched)

| Paper | New file | Edits |
|---|---|---|
| P1 | `paper1_assessment_separation_v6.md` | 5 micro |
| P2 | `paper2_obstruction_calculus_v3.md` | ~14 (2 substantive theorem fixes + micros) |
| P4 | `paper4_delay_dynamics_v4.md` | ~9 |
| E1 | `paperE1_cod_forecast_ladder_v5.md` | ~11 |
| E3 | `paperE3_edwards_forecast_ladder_v4.md` | ~14 |
| E4 | `paperE4_edwards_intervention_v5.md` | ~9 |
| P5 | `paper5_sampled_governance_v3.md` | ~9 |
| E2 cod | — | no audit in this batch; wave-2/3 dispositions stand |

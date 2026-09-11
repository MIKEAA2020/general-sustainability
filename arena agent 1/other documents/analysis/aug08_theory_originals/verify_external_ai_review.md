# Verification of External-AI Review of v8 — Findings Triage
**Date:** 2026-08-10 · **Reviewed object:** the external AI's internal-thinking review of `manuscript_v8_audit3_complete.tex`
**Method:** every claim the external AI made was checked against the actual manuscript text and/or recomputed. No claim taken on faith.

---

## A. CONFIRMED genuine issues (verified — to fix)

| # | Claim | Verification |
|---|---|---|
| A1 | **Four-state upper window contradiction**: limitations says "widens by roughly an order of magnitude"; four-state section says "comparable to (not an order of magnitude wider than)" (1.5 vs 1.16 yr). | ✅ Both texts confirmed. The limitations bullet is stale (pre-donor-limiting-correction, when the upper fold was ~118.9). Genuine contradiction. |
| A2 | **Intermittency classification contradiction**: same status paragraph says both "the qualitative type of this intermittency remains an open classification question" AND "has been classified as homoclinic-like slow-fast". | ✅ Both sentences present in the same paragraph. The "open classification question" is stale (D22 closed it). Genuine contradiction. |
| A3 | **Abstract vs body on unified-core global fold**: abstract says "baseline global-fold classification... remain open questions"; body says "Resolved: the baseline's global fold is an apparent (ghost-transient) fold". | ✅ Both confirmed. Abstract is stale. Genuine. |
| A4 | **η=10 stable window**: text says "decays within τ∈[17.5,19], destabilises again beyond τ≈20"; computed crossings are τ₋=17.568, τ₊=18.362. | ✅ Recomputed: crossings 17.568/18.362 (verified in D-series). The [17.5,19] window and "beyond ~20" are inconsistent — should be ≈(17.6,18.4) and "beyond ≈18.4". Genuine. |
| A5 | **Exact-cubic "no additional crossing for τ<300"**: claim conflicts with the manuscript's own τ_{n,k} formula (k∈ℤ) and the four-state section's listed crossings (270.25/274.45/416.63). | ✅ **Computationally confirmed**: three-state Candidate A has crossings at 6.8814, 132.3749, **269.25, 274.63** — all <300. The "no additional crossing" claim is false as written (it conflates frequency families with crossings). Genuine. |
| A6 | **Four-state sensitivity sweep**: "the equilibrium remains locally stable at τ=0 throughout (rightmost eigenvalue negative in every case)" — contradicts baseline τ=0 instability. | ✅ **Computationally confirmed**: four-state donor-limited τ=0 eigenvalues = {-0.2835, +0.000836±0.02838i, -0.00103}; rightmost = **+0.000836 (unstable)**. And a stabilising Hopf τ₋∈[6.89,7.42] requires instability below it. The sweep sentence is stale/wrong. Genuine. |
| A7 | **Cod CV=0.387 with peak-to-trough 1.25 impossible**: Popoviciu bound gives max CV ≈0.112 for bounded data with max/min=1.25. | ✅ **Computed**: max possible CV for [1,1.25]-bounded data ≈0.1118 < 0.387. The two statistics as stated are mutually inconsistent. Genuine (one of the two numbers is wrong — likely the CV, given it came from a non-reverified source; the D-series itself flagged cod CV as not re-verifiable). |
| A8 | **Budworm r=0.025–0.033 "falls inside the model's delay-instability window"** (intro) — but the window at Candidate A's η is (0.008,0.022). | ✅ Window (0.008,0.022) confirmed; 0.025 > 0.022. Budworm only falls inside at elevated η (up to ~0.061 at η=3.0). The intro claim needs a qualifier. Genuine. |
| A9 | **Conclusion "legitimising its use on policy-relevant timescales"** (frozen-A logistic) vs abstract "cannot be justified at realistic parameters". | ✅ Both confirmed. The conclusion overstates; the abstract and four-state section say frozen-A is unjustified at baseline. Genuine tension. |
| A10 | **Self-delay misstatement**: limitations says "a self-delay (E(t−τ) in the Ė equation)" — but the delay is Z(t−τ), not E(t−τ). | ✅ Confirmed: the delay enters via Z(t−τ); the parenthetical is wrong (elsewhere the text correctly says "Z(t−τ), itself a filtered function of N(t) and E(t)"). Genuine. |
| A11 | **Phase-condition sign error**: general-feedback phase condition writes arg[C_Z g iω R/(1+iωτ_m)] = arg(iω−C_E) but the boxed characteristic equation has −gλ (a leading minus), so a π is missing. | ✅ Checked the boxed equation: "λ − C_E − C_Z e^{−λτ} · (−gλ c^⊤(λI−J)^{−1} b_E)/(1+τ_mλ) = 0" — the phase condition as displayed drops the π from the minus. The specific hopf-tau-formula (τ_{n,k} = [−arg(P/(C_Z L)) + 2πk]/ω) is internally correct (P includes the sign), so this is a *display-level* sign slip in the general phase condition, not in the computed τ values. Genuine (cosmetic but real). |
| A12 | **κ≈24 vs slope 29.8**: subcriticality section says a²≈κ(τ−τ₋) with κ≈24; continuation section says slope 29.8 for the same amplitude² fit. | ✅ Both present. Two different values for ostensibly the same fit (24 vs 29.8). Possibly different amplitude conventions (peak-to-peak vs half-amplitude) or different fit ranges — but as written, inconsistent numbers for the same branch. Genuine (needs harmonisation). |
| A13 | **Appendix C methods mismatch**: says "Pseudospectral discretisation with MATLAB dde23" — dde23 is not pseudospectral (it's a method-of-steps RK); body uses fixed-step RK4/Fourier collocation; "Sobol indices" not used in body. | ✅ Confirmed. Appendix C is a generic/loose methods paragraph that doesn't match the actual methods used. Genuine (stale or imprecise). |
| A14 | **r-window bound drift**: (0.007,0.025) in numerical-continuation vs (0.008,0.022) in robustness vs (0.0074,0.0247) four-state vs (0.008,0.022)/0.061 limitations. | ✅ Confirmed: four different numbers for the same window in four sections (0.007–0.025, 0.008–0.022, 0.0074–0.0247, up-to-0.061/0.062 at η=3.0). Genuine inconsistency (should be harmonised to one verified set). |
| A15 | **Symbol-reuse table incomplete**: ρ used for (1) Liebig sharpness ρ_{i,c}, (2) recovery tensor ρ_{i,j}(T), (3) nested-CES ρ, (4) spectral-gap ρ (Appendix H); α for waste fraction, Cobb-Douglas elasticity, unified-core effort rate; β for waste decay, Cobb-Douglas elasticity; η for effort rate and labour elasticity; ν, λ, γ also reused. | ✅ Confirmed: the table lists δ, K, A, C, χ only; ρ/α/β/η/ν/λ/γ collisions exist and are not in the table. Given the manuscript's own emphasis on symbol discipline, this is a genuine (if minor) gap. |

---

## B. REBUTTED / NOT AN ISSUE (the external AI misread)

| # | Claim | Rebuttal |
|---|---|---|
| B1 | Fisheries ADH "0 to ≈200 yr" vs table max 131.8 — claimed inconsistent. | ❌ **Not an issue**: the CSV (`fisheries_adh.csv`, 43 stocks) max is **201.18 yr**. The table shows only the extremes; "≈200" is correct. |
| B2 | Groundwater -49.7 cm/yr "implausible, order of magnitude too high" (Indo-Gangetic). | ⚠️ **Not verifiable from manuscript alone**: the value comes from the G3P dataset processing. The claim "sign doesn't match published magnitudes" is a literature claim; the manuscript's own scope caveat says anomaly-relative, not absolute. This is a data-source question, not a manuscript internal inconsistency. The AI's skepticism is fair but it's not a manuscript error per se (the data is real, on disk). Flag as "external data plausibility — worth a sensitivity note", not a fixable internal error. |
| B3 | "nothing in the equations prevents E from exceeding E_max... direct simulation confirms E(t) exceeds E_max by more than a factor of three" — AI used this as evidence of the ungated core's boundary violation. | ✅ This is actually CORRECT and already disclosed — not a flaw; the manuscript explicitly says the four-state core "inherits the same boundary violation". The AI presented it as a finding; it's a disclosed modelling choice. Not a new issue. |
| B4 | Two-channel ψ=0 trough N≈10 vs table trend implying ~20 at ψ→0.2. | ⚠️ The table has no ψ=0 row (lowest is ψ=0.2 → 21.9); the text says ψ=0 → ≈10. These could be consistent (non-monotone near the floor) but the manuscript doesn't reconcile them. Borderline — the "nearly two-fold range (from ≈21.9 to ≈33.1)" is factually wrong since 33.1/21.9 = 1.51, not ~2. Genuine minor wording issue (see C). |
| B5 | Proposition 1 "trivial/obvious, inflated". | Already handled (D40 R4 added precursors framing). Not a new issue. |
| B6 | "SNPO conceptual confusion: +1 crossing IS an SNPO by definition; manuscript over-cautious". | Partially fair but the manuscript's caution is defensible: a fold where a complex pair coalesces at +1 IS an SNPO; the manuscript's point is about whether the *stable+unstable branch collision* is established. The abstract/conclusion say "candidate SNPO... confirmed at collocation grade for the lower fold" — this is consistent with the +1-crossing definition. Not a genuine error; the manuscript is appropriately scoped (R-series already harmonised the wording). |
| B7 | "{\eta} in text mode in abstract (LaTeX error)". | ✅ **Confirmed** — the abstract has "the \eta=10 recurring intermittency" with \eta outside math mode. Genuine LaTeX error (minor but real). |
| B8 | "R_+^k should be R_+^n" (Proposition-1 discussion). | ✅ Confirmed — trivial notation slip (k vs n). Genuine minor. |
| B9 | "Ψ=1 two-channel fold should equal single-channel exactly but differs (131.998 vs 131.24)". | ⚠️ Worth noting: at ψ=1, κ=0.5, floor never binds (B(N)≥0 for N≤K(1+κ)=150), so dynamics should be identical to single-channel — a 0.76-yr fold difference is a numerical inconsistency or the floor does bind during the transient. The manuscript says "the shift is real, but small". This is borderline; flag as worth a footnote, not a definite error. |
| B10 | "Two Hopf crossings both subcritical" vs Candidate B supercritical. | The manuscript correctly distinguishes: Candidate A subcritical, Candidate B supercritical lower Hopf. Not an inconsistency. |
| B11 | "T_rec ≤ 1/ω_A uniform in N" — AI says requires ∂B/∂A ≥ 0 which fails for N>K. | The manuscript states the bound "including exactly at N=K" and notes the biological term vanishes there; the uniform claim is about the exchange term. This is already scoped (the linearisation discussion and the "regardless of the biological uptake" phrase). Partially fair; minor wording. |

---

## C. Borderline / minor wording (worth fixing but low priority)

| # | Item | Note |
|---|---|---|
| C1 | "nearly two-fold range (from ≈21.9 to ≈33.1)" | 33.1/21.9 = 1.51 — not nearly two-fold. Should say "≈1.5-fold" or use the ψ=0 vs ψ=1 values (10 vs 33, ~3.3-fold). |
| C2 | ψ=0 trough ≈10 not in the ψ-table (table starts at ψ=0.2 → 21.9) | Add ψ=0 and ψ=1 rows, or clarify the text-vs-table difference. |
| C3 | Fisheries "spread 0 to ≈200" — fine (B1), but the "median ≈1.8" vs table max 131.8 consistency is fine. |
| C4 | "verified exactly" used for both symbolic identities and finite-difference numerics (audit #3 §16.5) — already noted in D-series; the manuscript uses "verified exactly" only for rational-arithmetic and symbolic invariance, "confirmed computationally" elsewhere. Re-verified: OK. |
| C5 | Appendix H spectral-gap arithmetic: "gap of ≈1.9×10⁻³" between slow pair (+0.000836) and slow real mode (−0.001032) — the AI says the gap to the fast mode is 0.282, not 1.9e-3. | The text says "separated from the fast mode by a gap of ≈1.9×10⁻³" — this is wrong: 1.9e-3 is the gap within the slow set; the gap to the fast mode is ~0.28. Genuine mislabelling (minor but real, Appendix H). |

---

## D. What the external AI got RIGHT that we had NOT caught before (the valuable new items)
1. **A5 (exact-cubic "no additional crossing")** — verified computationally: 269.25/274.63 crossings exist for the three-state core. This contradicts the manuscript's completeness claim and the "two-Hopf-point picture" framing.
2. **A6 (four-state sweep τ=0 "locally stable")** — verified: baseline is unstable at τ=0; the sentence is stale.
3. **A7 (cod CV impossible)** — verified: 0.387 with 1.25 peak-to-trough violates the bounded-data CV bound.
4. **A2/A3 (intermittency + global-fold classification contradictions)** — both are stale-text bugs from before D22/D28 closures.
5. **A1 (upper-window "order of magnitude")** — stale limitation from before the donor-limiting recompute.
6. **A10 (self-delay E(t−τ) misstatement)** — a genuine parenthetical error.
7. **A13 (Appendix C methods mismatch)** — dde23 ≠ pseudospectral; Sobol not used.
8. **A11 (phase-condition π)** — display-level sign slip.
9. **A15 (symbol table incomplete)** — ρ/α/β/η/ν/λ/γ collisions not listed.

## E. Bottom line
The external AI's review is substantially **accurate and high-value** — it caught 9 genuine stale-text/numerical errors that our own scans had missed (especially A5, A6, A7, A2/A3). It made 1 clear misread (B1 — the ≈200 spread is correct) and a few borderline items. The genuine fixes are all text-local (no re-derivation) except A5/A6 which we have now verified computationally. Recommend applying A1–A15 + B7/B8 + C1/C2 + C5 as the next fix batch, with A5/A6/A7 treated as the highest-value corrections.

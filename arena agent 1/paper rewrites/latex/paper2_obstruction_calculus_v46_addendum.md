# Paper 2 — v46 Addendum (disposition record)

**Version:** `paper2_obstruction_calculus_v46_Automatica_routes` (main + supplementary, both content-revised).
**Base:** v45 (pushed `dbbbc08`); supplementary advances v44 → v46.
**Implements:** roadmap v3 (`2bdd653`) Track-A items **A5** and **A6**, per the owner directive to proceed with the v46 manuscript. Both items had been flagged "not required for submission; revision item if unproven"; both are now proven, machine-verified, and incorporated.

## 1. What v46 adds

### A5 — Linear-programming instantiation of the timing certificate (main §3.3)
- **`thm:lp-instant`** — Theorem 4 (linear-programming instantiation of the timing certificate). For polyhedral data (robust affine branch dynamics, polytope disturbances, polyhedral safe set) with a **polytope-declared** blind-window class: (i) σ\*(B₀; Π_B) is computed exactly by ≤ ⌈log₂K⌉+1 LPs of polynomial size, exact in rational arithmetic; (ii) infeasibility is Farkas-certified in adjoint-row form (vanishing aggregate control projection, negative aggregate constant); (iii) the program's feasible set is the declared class itself — sound **and complete**, no relaxation gap; (iv) the declaration is load-bearing: over a larger polytope the computation is the relaxation — sound but arbitrarily incomplete.
- **`ex:relax-gap`** — Example 2 (the relaxation gap is unbounded). Two-branch contraction instance z⁺ = (9/10)z ± u, floor z ≥ 1, U = [−1,1]: branch sum z⁺ₖ + z⁻ₖ = 2(9/10)ᵏz₀ is control-invariant ⇒ threshold z₀ ≥ (10/9)ᴷ exactly (necessity by sum-invariance; Farkas level-k pairs cancel pairwise; sufficiency by u ≡ 0 on the boundary). Contrast: hidden-regime data with finite declared class {±1} gives σ\* = z₀−1, while the polytope relaxation U = [−1,1] admits u ≡ 0 ⇒ σ\*_relaxed = ∞ — the relaxation **extinguishes** the certificate.
- **`rem:adjoint-duality`** — Remark: Farkas multipliers as the finite analogue of the bridge's adjoint safety rows.
- §3.3 closing sentence rewritten: continuous classes remain a template (Open Problem 1); polytope-declared classes are exact and finite; the class declaration is load-bearing.

### A6 — Quantified converse / exact residual (main §7)
- **`prop:decomposition`** — Proposition 9 (exact two-phase decomposition). In the two-phase model (K blind steps, then exact revelation + branch-adapted continuation): viable ⇔ (i) some declared blind control survives the window **and** (ii) some window-surviving blind control lands every branch in RViab(V) at the reveal. Over classes where the window certificates are complete (finite; polytope-declared, by Theorem 4): both-silent ⇔ (i), and any nonviability is **exactly** the post-observation recourse mode.
- **`prop:window-nogo`** — Proposition 10 (no window-measurable pair is complete). The S3/A.3 three-state recourse instance and its variant agree on all window sub-model data with both certificates silent, yet differ in viability (x₄ exits vs. maintained post-reveal). Hence any complete pair must read data beyond the window sub-model — the precise sharpening of Open Problem 1. (The naive "both silent ⇒ viable" is false by the A.3 instance; the propositions deliver the honest content instead.)

### Supporting changes
- Abstract: two completion sentences added.
- §1.2 contributions list: new item "Computable instantiation and the exact residual".
- Conclusion: one structural-completion sentence added.
- Supplementary S1: complete proofs of Theorem 4, Proposition 9, Proposition 10, including the duality computation and the verification-record statement.

## 2. Verification record (exact rational arithmetic; `paper2_v46_a5a6_verification.py`, stdlib only)

**12/12 checks pass** (fractions only, no floating point):

| # | Check | Result |
|---|-------|--------|
| V1 | Hidden-regime, hold {±1}: σ\*(z₀) = z₀−1; audit partition 42 = 30 + 12 reproduced | PASS |
| V2 | Hidden-regime, hold [−1,1]: u ≡ 0 survives forever, σ\* = ∞ (relaxation extinguishes) | PASS |
| V3 | Contraction instance, K = 1,2,3: pairwise-cancellation Farkas at every level; deepest bound (10/9)ᴷ; sum-invariance necessity | PASS |
| V4 | (merged in V3 run) deepest Farkas bound = (10/9)ᴷ exactly | PASS |
| V5 | Boundary z₀ = (10/9)³: u ≡ 0 explicit complete control ((10/9)ᴷ⁻ᵏ ≥ 1 balanced branches) | PASS |
| V6 | A.3 instance: certificates silent **and** B₀ ∉ W₂ (failure = recourse mode) | PASS |
| V7 | Variant: identical window sub-model, certificates silent, B₀ **is** viable | PASS |
| V8 | Every window-surviving blind action lands a branch outside RViab | PASS |

## 3. Build and probes
- Tectonic 0.15.0; main `main.pdf` 500,448 B, **18 pp** (v45: 17 pp); supplementary `suppl.pdf` 457,561 B, **15 pp** (v44: 13 pp).
- pymupdf probes: **0 unresolved `??` refs in either PDF**; numbering confirmed in rendered text: Theorem 4 (linear-programming instantiation), Example 2 (relaxation gap), Propositions 9/10 (decomposition / no-go), Theorems 5/6/7/8 (exit / one-step / static-complete / belief-state, shifted), Propositions 11/12 (chance / degenerate, shifted), Open Problem 1 unchanged.
- Theorem-counter shift map (all in-text references are `\ref`-based; source-level grep confirms zero hardcoded "Theorem N" strings in paper 2; the ECOMOD companion's "Theorem 5" reference targets paper 1, so no cross-paper impact): exit 4→5, one-step 5→6, static-complete 6→7, belief-state 7→8; monotone 8 (unchanged position), decomposition/new = 9–10, chance 11, degenerate 12.

## 4. Files
- `paper2_obstruction_calculus_v46_Automatica_routes.tex` / `.pdf` (main)
- `paper2_obstruction_calculus_v46_Automatica_routes_supplementary.tex` / `.pdf` (suppl; content-advanced v44 → v46)
- `paper2_v46_a5a6_verification.py` (verification record)
- `paper2_obstruction_calculus_v46_source.zip` (14 entries: README, audit script, verification script, main tex+pdf, suppl tex, 7 figures)
- Unchanged: `paper2_coverage_audit.py`, figures (all seven), roadmap v3.

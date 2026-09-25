# P3 Edition 4 + Exact-Belief Computation v1 — Round-12 Addendum

**Date:** September 26, 2026. **Scope:** the five-item extension round
(DR interpolation; PBVI/ZDD scaling on medium instances; probe-count
asymptotics; general additive deadline law; supersession-banner pass),
Lean formalization skipped by decision. Companion files:
`paper2_probabilistic_sufficiency_v4.{tex,pdf,_verification.py}` and
`paper2_exact_belief_computation_v1.{tex,pdf,_verification.py}`.

## 1. What edition 4 adds to the P3 flagship

- **DR interpolation lemma (prop:dr).** For the ε-contamination
  ambiguity set D_ρ = {q = (1−ρ)p + ρ r : r ∈ Δ(Y)}, the support
  function is exact and separates:
  inf_{q∈D_ρ} Σ_y q(y) v_y = (1−ρ) E_p[v] + ρ min_y v_y. Pointwise the
  robust value mixes linearly, V^ρ = (1−ρ)V⁰ + ρV¹, and is concave PWL
  in ρ at every state. **Convention pinned:** this is the *contamination*
  set, not the TV ball — the mixture formula is false for the TV ball
  (the first computation used TV and failed; root-caused, not patched).
- **Delayed class, prior contamination.** V = 0 (z₀ < 1);
  1 (z₀ ≥ 1+ℓ); (1−ρ) max(w, 1−w) otherwise; symmetric-prior levels
  {0, (1−ρ)/2, 1}. Verified on the sweep z₀ ∈ [1.0, 3.0],
  ℓ ∈ {1, 2}, ρ ∈ {1/10, 3/10, 1/2}.
- **Probe-count asymptotics (prop:probecount).**
  p_wrong(2m+1) ≤ (4ε(1−ε))^((2m+1)/2) ≤ e^{−2n·sep²}, sep = 1/2 − ε;
  n ≥ ln(1/δ)/(2 sep²) probes buy confidence δ. At ε = 1/10 the bound
  (3/5)^n holds with equality of the closed form at
  n = 1, 3, 5, 7, 9: 1/10, 7/250, 107/12500, 341/125000,
  22273/25000000. Each probe step costs the 1/10 floor margin
  (declining instance) — the repetition trade-off now has a rate, not
  just a two-point table.
- **General additive deadline law (prop:additivelaw).** If
  d(u, θ) = c(u) + h(u)θ, the hold–probe–learn structure collapses:
  with learned drift μ > 0, viability from (z₀, T) holds iff
  **z₀ ≥ 1 + T·d₀ + e_p**, d₀ = max_θ(−d(u₀, θ)), e_p = max_θ(−d(u_p, θ))
  — floor + drift × deadline + probe excursion. Instance 1:
  21/10 + T/10 (verified T = 0..5); instance 2 (drift −3/20, excursion
  21/20): 41/20 + 3T/20 (verified T = 0..3).
- **Methods/scope updated**, abstract states six results; formal home of
  worst-case wording = Nakao–Jiang–Shen 2021. Verify chain **26/26**
  (23 v3 checks carried + 3 new exact batteries), 9 pp, overfull 0.

## 2. The new P2-lineage computational paper (exact belief computation v1)

Medium instance: 12 stock levels × 4 hidden-parameter cells = 48
augmented cells, five controls, d(u,θ) = −1/10 + (u·θ)/5, floor z ≥ 1.
Results (all exact, `paper2_exact_belief_computation_v1_verification.py`,
11/11):

- **Exact point-based evaluation.** Alpha-set values at 7 probed rational
  beliefs × 3 levels × 3 horizons equal definition-level trajectory
  enumeration; point-based selection changes *where* values are
  evaluated, never their exactness. The k = 6 alpha-set deduplicates
  15,625 sequences to 9 witness vectors.
- **Survivable-set compression.** 48 stored maximal sets in place of 180
  raw subset evaluations (= 4 + 4 × 11 ✓). Bands: four singletons at
  z₀ = 1.0; exactly the four coordinate pairs at every z₀ ≥ 1.1;
  nothing larger, ever.
- **Averaging obstruction.** Every control's drifts sum to **−2/5** per
  step over the four cells, so no policy of any kind keeps all four
  cells alive indefinitely; certified at 60 steps for every
  three-periodic policy from z₀ = 2.1. The finite-horizon table
  (definition enumeration, k = 1, 2, 3, 6): V₆ = 1/4 at 1.0, 1/2 on
  1.1–1.5, 1 from 1.6 up, monotone in k.
- **Observation ladder.** One θ₁ probe: value 1 for every z₀ ≥ 1.1
  (the post-probe coordinate pair is jointly survivable), 1/2 at the
  edge (one cell of the pair kept alive); fully observed 1 everywhere —
  one well-chosen probe exhausts observation above the floor's edge.

## 3. Errors caught and corrected this round (verification-before-assertion)

1. **Drift-sum constant (verifier catch).** The scaling draft asserted
   the per-step drift sum over the four cells as −1/5; direct summation
   gives −4/10 = **−2/5**. Corrected in the abstract and the obstruction
   proposition before any build was trusted.
2. **One-probe functional semantics.** Requiring the *entire* posterior
   support to survive gives 0 at the edge; the correct best response
   maximizes expected survival over the two-cell support, giving 1/2 at
   z₀ = 1.0 and 1 at z₀ ≥ 1.1 — matching the hand prediction only after
   the functional was fixed. Enumeration, not the hand model, was the
   arbiter throughout (three wrong hand models earlier in the round:
   diagonal pairs, alternation hedging, triples — all false).
3. **Level-dependence of the alpha-set.** The alpha-set must be
   computed per stock level; evaluating the z₀ = 2.1 set at z₀ = 1.1
   beliefs is meaningless (caught by the equality check).
4. **Earlier battery failures (round start).** Two apparent DR failures
   were the TV-ball vs contamination convention error (§1); medium
   instance enumeration timeouts fixed by limiting periodic-policy
   search (never enumerate 5^k beyond k ≈ 6; 60-step certificates for
   1/2/3-periodic policies).

## 4. Placement decision (as delegated)

**Same paper (P3 edition 4):** DR interpolation, probe-count asymptotics,
additive deadline law — they share the delayed-class machinery, the exact
rational arithmetic, and the v3 verify chain, and each sharpens a layer
v3 already has (robustness, repetition, timing). **Separate paper (P2
lineage):** PBVI/ZDD scaling on medium instances — a different
methodology (computation as result), its own instance battery, and a
compression story that would dilute the theory paper's arc. The two
cross-reference each other.

## 5. Banner pass

Executed as `supersession_map_v1.md` (programme-wide pointer table) —
no frozen file edited, no-overwrite respected; roadmaps v16–v30
superseded by v31.

## 6. Verification ledger

| Artifact | Chain | Result |
|----------|-------|--------|
| `paper2_probabilistic_sufficiency_v4_verification.py` | seeds 16+21/15/6 + 26 own | **26/26, exit 0** |
| `paper2_exact_belief_computation_v1_verification.py` | 11 own (all exact rational) | **11/11, exit 0** |
| v4 PDF | tectonic 0.15.0, `--keep-logs` | 9 pp, overfull 0, no `??` |
| scaling v1 PDF | same | 3 pp, overfull 0, no `??` |

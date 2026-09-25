# Exact Belief Computation Edition 2 — Addendum (the four-parameter cube)

**Base:** new edition in the P2 lineage (edition 1 chained as seed, byte-untouched).
**Verify chain: 16/16** (edition 1's 11 checks chained + 15 own families); 3 pp,
overfull 0.

## 1. The instance and the results

Θ = {±1}⁴ (16 cells) × z-grid 1.0–2.5 step 1/10 (16 levels) = **256 augmented
cells**; U = {±1}⁴ ∪ {0} (17 actions); d(u,θ) = −1/2 + (1/5)Σᵢuᵢθᵢ; floor z ≥ 1.
All exact, stdlib only:

- **Pair-sum lemma:** ⟨u,θ⟩ + ⟨u,θ′⟩ ≤ 2(4 − Hamming) for every pair and action
  (hold: 0). Both members of a blind survivable set need time-averaged inner
  product ≥ 5/2, so pair average ≥ 5 ⟹ h ≤ 1. No three cells of the 4-cube are
  pairwise Hamming-adjacent (all 560 triples checked) ⟹ **no blind policy of any
  period keeps ≥ 3 cells safe**.
- **Bands:** 16 maximal singletons at z₀ = 1.0; exactly the 32 Hamming-adjacent
  pairs at every z₀ ≥ 1.1 (matched–singly-mismatched alternation: net +1/5 per
  two steps, dip 1/10). Independently reproduced by exhaustive 1/2/3-periodic
  search (5,219 policies, 60-step certificates).
- **Ladder doubles:** 1/16 → 1/8 → 1/4 → 1/2 → 1 at the edge;
  1/8 → 1/4 → 1/2 → 1 → 1 above it — each probe of one parameter doubles the
  conditional kernel mass; three probes exhaust observation above the edge; the
  fourth buys nothing there and 1/2 at the edge. All ten values exact.
- **PBVI at k = 4:** alpha-set evaluation equals trajectory enumeration at
  7 rational beliefs × 3 levels × 4 horizons (84 pairings); 17⁴ = 83,521
  sequences deduplicate to ≤ 545 outcome vectors; D = 1 at the top level's
  one-step horizon (every action safe — the cube's silent region).
- **Census:** 1,048,576 raw subset evaluations → **496** stored maximal sets
  (16 + 15 × 32); per-level ratios 4,096× and 2,048×.
- **Deadline instance 3:** hold T (−1/2), free revelation, matched forever
  (+3/10 every branch): viability ⟺ z₀ ≥ 1 + T/2 (d₀ = 1/2, e_p = 0), T = 0..4 —
  the companion theory's additive deadline law, third instance.
- **Crude-instrument contrast:** the four-set {++++, +++,−…} attains the ℓ1
  averaging bound with equality (Σ|vᵢ| = 10 = (5/2)·4) yet is not survivable
  (Hamming-2 pairs) — the pairwise bound is the sharp instrument.

## 2. Errors caught before ship (verification-first working)

1. **Census arithmetic (verifier catch).** The draft asserted 736 stored sets;
   16 + 15 × 32 = **496**. The derived "1,425× overall" ratio went with it
   (dropped; per-level ratios 4,096×/2,048× are exact). Caught by check 8 before
   any build was trusted.
2. **Deadline test construction.** The first simulator cycled the hold prefix
   back after revelation (net-negative cycles → false FAIL). Fixed to prefix
   semantics: T holds, then matched to the horizon; threshold identity verified
   over all cells, levels, T = 0..4.
3. **Hand-model failure (again).** The pre-computation guess "pairs = coordinate
   matches, quadruples as 2×2 subcubes" was wrong on both counts; enumeration
   and the pair-sum lemma gave the actual (Hamming) structure. Standing rule:
   enumeration is the arbiter.
4. **Overfull ladder display.** The two-row ladder broke the column by 70.3 pt;
   fixed by stacking in `align*` (zero overfull after rebuild).

## 3. Cross-tool feasibility datum (recorded, not shipped)

z3 5.1.0 (SMT) was probed on two bounded cube questions outside the stdlib
verify chains: (a) all 16 cells from z₀ = 2.5 for T = 4 — **unsat**, agreeing
with the averaging identity; (b) the Hamming-1 pair {++++, +++−} from z₀ = 1.1
for T = 12 — **sat**, agreeing with the alternation certificate. Encodings were
integer (10·z), actions as 17-way selections; seconds of runtime. This is the
recorded feasibility datum for the cross-tool comparison construction (roadmap
v32); no conic/SMT solver is part of any shipped verify chain.

# Exact Belief Computation Edition 3 — Addendum (proofs completed; dimension scope; audit F3/F4)

**Base:** `paper2_exact_belief_computation_v2.tex` (frozen at `db1fbcf`; chained
seed). **Verify chain: 19/19** (edition 2's 16 checks chained, which chain
edition 1's 11); 4 pp, overfull 0. **Purpose:** the user's completeness bar
(no condensed proofs unless standard literature) plus the attached audit's
finding 3 (formalize the scaling lemma; scope it explicitly).

## 1. What was incomplete in edition 2, and what v3 adds

Edition 2's results were script-verified but several proofs were condensed or
implicit. Edition 3 completes all of them:

1. **Pair-sum lemma → general-m "pair-sum bound and its survival cost"
   + proof.** Hypotheses now explicit (dimension m; U = {±1}^m ∪ {0};
   d(u,θ) = −1/2 + (1/5)⟨u,θ⟩; floor; blind class of any period, possibly
   aperiodic). Proof: (i) the pointwise agreement-count bound;
   (ii) survival ⟹ Cesàro liminf of per-cell drift ≥ 0 ⟹ per-cell
   long-run average inner product ≥ 5/2 (periodic policies: exact cycle
   average). New **corollary**: every blind survivable pair has
   h ≤ m − 5/2 — at m = 4, h ≤ 1 (the Hamming-adjacency of the cube's
   pairs is now a proved corollary, not an asserted step).
2. **No-adjacency-triangles lemma + proof** (3-line flip argument; the
   hypercube's bipartiteness noted as the equivalent formulation — proved,
   no external citation needed).
3. **Bands/maximality proposition + proof** (singleton matched play; the
   H1 alternation cycle with its exact dip; the z₀ = 1.0 no-pair argument
   (any first action drives some member below the floor in one step, and
   the floor binds at every step); nothing-larger via the two lemmas +
   downward heredity; maximality immediate).
4. **Ladder proposition + proof** (the companion theory's antichain kernel
   formula — cited as programme literature; downward heredity puts the
   maximizer inside the support; subcube values 2/2^j and 1/2^j; the two
   ladders fall out exactly).
5. **PBVI, census, and deadline propositions + proofs** (same-functional
   argument; raw-count arithmetic — the headline 1,048,576 is the full
   lattice, the conservative figure vs 1,048,560 nonempty; the branchwise
   deadline argument with the companion law identified at d₀ = 1/2,
   e_p = 0, noting the direct proof needs no scalar-additivity).
6. **NEW Remark (scope in dimension: the ball construction) — the audit's
   scoping demand, answered with a sharpness witness.** General m: the
   corollary gives only h ≤ m − 5/2; and the constant matched action keeps
   the Hamming ball of radius r*(m) = ⌊(2m−5)/4⌋ alive from **every**
   level (drift −1/2 + (m−2k)/5 ≥ 0 ⟺ k ≤ (2m−5)/4). Radii verified:
   r*(3) = r*(4) = 0; r*(5) = r*(6) = 1; r*(7) = r*(8) = 2. **At m = 5 the
   radius-1 ball (6 cells) survives from the floor's edge under constant
   matched play** — where the four-cube keeps only singletons — so the
   pairs-only classification is exactly m = 4, changes qualitatively at
   m = 5, and the m ≥ 5 maximal sets are explicitly **not classified**
   (delimitation updated in §scope). 60-step simulations: the 6-cell m = 5
   ball and the 29-cell m = 7 radius-2 ball.

## 2. Verification (checks 17–19, on top of the chained 16)

- Check 17: the pair-sum bound at m = 5 over all 496 pairs × 33 actions;
  the corollary's threshold identity h ≤ m − 5/2 exact for m = 3..8.
- Check 18: the ball battery — r* table, within/beyond drift sign pattern,
  the two simulations above.
- Check 19: proof completeness (7 proof environments) + 12 needles for the
  new proof/scope content.

## 3. Process (audit F4)

All v3 edits were executed as a single-writer sequential script with
exactly-once assertions per anchor. **Standing rule (recorded): never issue
parallel edits to one file; assert anchor counts before replacing; rerun the
verifier before any build.** (Two anchor misses during drafting — display-math
wrappers `\( \)` vs `\[ \]` — aborted harmlessly before write, exactly as the
pattern intends.)

## 4. z3 note (audit F5 consistency)

The m = 5 witness is certified by exact arithmetic and simulation; no SMT
solver entered the verify chain (the z3 agreement datum of round 13 remains a
recorded cross-check only).

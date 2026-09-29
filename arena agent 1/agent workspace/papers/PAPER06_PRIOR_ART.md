# Paper 6 — prior-art position, established 2026-09-29

## Why this file

The bar assessment flagged paper 6 as **highest novelty risk**: its separation result sits
close to known robust-optimisation and MCDM separation results, and it had no prior-art
paragraph. Per the root cause identified for the family (results developed before novelty
was established), prior art was done FIRST this time, and it narrowed the claim.

## What paper 6 actually proves (read, not paraphrased)

- **Remark 1** (quantifier separation): `{z : ∩_λ E_λ(z) ≠ ∅} ⊆ ∩_λ {z : E_λ(z) ≠ ∅}`,
  equality iff a common selector exists. Elementary order theory.
- **Remark 2** (full-cone pointwise equivalence): `v ≥ 0 ⟺ w·v ≥ 0 ∀w ∈ ℝⁿ₊\{0}`.
  At a FIXED trajectory the aggregate is lossless.
- **Prop 3**: `E_typ ⊆ E_w ⊆ E_tube,phys ⊆ E_end`; `E_typ = ∩_w E_w`.
- **Prop 4**: `V_typ ⊆ V_W ⊆ V_phys`; narrower weight family ⟹ larger accepted set.
- **Thm 6** (finite-menu geometry): coordinate-wise acceptance `= ∪_a (d_a + ℝⁿ₊)`;
  **scalarized acceptance `= conv(𝒟) + ℝⁿ₊`**; gap = the difference; replacing the menu by
  its convex hull collapses the gap to empty.
  On the witness: `𝒟 = {(2,0),(0,2)}`, gap = the discrepancy triangle `𝒬`.

## The three nearest neighbours, and the damage

1. **The multi-objective scalarization gap — TEXTBOOK.** Weighted-sum scalarization
   recovers only *supported* non-dominated outcomes (boundary of the convex hull of the
   non-dominated set); no weights recover unsupported points on non-convex fronts
   (Koski 1985; Stadler & Dauer 1992; Stadler 1995; Athan & Papalambros 1996; Chen et al.
   1999; Das & Dennis 1998; Messac & Mattson 2002; Huang et al. 2007; Miettinen 1999;
   Ehrgott 2005).
   → **Thm 6(ii) IS this gap.** `conv(𝒟) + ℝⁿ₊` is the convex hull. This cannot be claimed
   as new and the paper now says so in as many words.

2. **Adjustable / adaptive robust optimisation.** Ben-Tal, Goryashko, Guslitzer &
   Nemirovski (2004) *Math. Program.* 99(2), 351–376 — here-and-now vs wait-and-see;
   Ben-Tal, El Ghaoui & Nemirovski (2009); Bertsimas & Goyal (2012) on when static and
   adjustable coincide.
   → The `∃plan ∀weight` vs `∀weight ∃plan` structure is familiar there.

3. **Randomization under worst-case objectives.** Mixed strategies can strictly beat
   deterministic: Krause, Singla & Golovin (2011); Vorobeychik & Li (2014); Sinha, Fang,
   An & Kiekintveld (2018); Sessa, Bogunovic, Kamgarpour & Krause (2020), AISTATS/PMLR 108;
   Kobayashi & Takazawa (2023) *Algorithmica*; the "randomization-receptive vs
   randomization-proof" distinction.
   → Thm 9 (fractional blends close the gap) sits in this line.

4. **Weak vs strong sustainability** — Pearce & Atkinson (1995); Daly (1995); Beckerman
   (1994); Ayres (1996); Neumayer (2003); Dietz & Neumayer (2007). Large, largely verbal
   and policy-facing; not previously given a separation theorem with an exact witness.

## What is now claimed (narrowed, in § priorart of v65)

1. **The setting** — robust transition safety over a finite horizon with path-wise
   constraints and separately-binding floors; acceptance *sets of states*, not recovery of
   Pareto points by a scalarized optimizer.
2. **The negative result on time-alternation** — Thm 9: fractional blending closes the gap
   exactly, alternating over time does NOT. **This inverts the robust-optimisation
   ordering**, where adjustability weakens conservatism so the adjustable counterpart
   dominates the static one. Flagged in the paper as the sharpest and most contestable
   claim; not found in the surveyed literature, which studies worst-case *objective value*
   rather than path-wise *feasibility*.
3. **The detection reading** — an aggregate index cannot distinguish the rescuable from the
   impossible; a consequence of (1)+(2), not an independent assertion.
4. **The witness** — exact rational arithmetic, fishery transition under heatwave, gap a
   region of nonempty interior.

**Explicitly NOT claimed**: the quantifier-order observation (elementary), the convex-hull
geometry (the known scalarization gap), the usefulness of randomization under worst-case
objectives (well established).

## Bibliography

Paper 6 had **no bibliography at all**. 24 entries added, 22 surname groups verified
present. Five confirmed against search results with full details (Ben-Tal et al. 2004;
Ben-Tal/El Ghaoui/Nemirovski 2009; Sessa et al. 2020; Kobayashi & Takazawa 2023; Ayres;
Beckerman 1994). **Twelve are flagged in the .tex as needing publisher verification**
(venue/pagination not confirmed; venue deliberately omitted rather than invented):
Koski, Stadler & Dauer, Stadler, Athan & Papalambros, Chen et al., Huang et al., Krause
et al., Vorobeychik & Li, Sinha et al., Pearce & Atkinson, Daly, Dietz & Neumayer.

## Residual risk

Item 2 carries the paper's novelty. If a reviewer produces a robust-optimisation result
showing open-loop time-variation achieving the convexification, item 2 fails and the paper
reduces to a transport of known results into a sustainability framing — which would not
clear the bar. That is the honest downside and it should be tested, not buried.

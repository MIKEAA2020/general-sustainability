# v41 — Pass D: 2-D case-study instance, calibration, joint-completeness proof

## Changes

1. **GAP 8 (applied audience).** Added a two-dimensional aggregation instance
   to the case study: with state (S₁,S₂) ∈ [0,1]² and floor S₁ ≥ 0.4, an
   aggregate index I = S₁+S₂ cannot certify the floor (the reading I = 1.0
   admits both the safe (0.5,0.5) and the unsafe (0.2,0.8)), and the
   certainly-safe readings are exactly I ≥ 1.4. Added a calibration paragraph
   mapping the certificate parameters to stock-assessment quantities
   (ε = net growth rate at the floor, T_obs = review periodicity, b = index
   bias, the floor = the reference point), explicitly leaving empirical
   calibration to applied studies. The "symbolic and one-dimensional" closing
   was updated to note the new 2-D instance.

2. **GAP 10 (quantified non-completeness).** Upgraded the coverage Remark from
   an audit observation to a proven identity: a proof that, in the delayed
   hidden-regime class, nonviability (z₀ < 1+T_obs) is partitioned by the
   common-action certificate (z₀ < 2) and the timing bound (2 ≤ z₀ < 1+T_obs),
   so the pair is jointly complete at every horizon and the Section 6.5 gap is
   exactly the timing cells.

## Supplementary

Unchanged from v40 (Pass D touched only the main text).

## Cumulative QA (v41 final)

- Main: 16 pages, 4 images, 1 table, 0 `??`, no overfull, abstract 262 words.
- Supplementary: 13 pages, 3 images, 0 `??`.
- Numbering complete: Theorems 1-7, Propositions 1-9, Remarks 1-4,
  Corollary 1, Example 1; subsubsections 3.1-3.6 and 6.1-6.5 present.
- Equation tags (1)-(5) in reading order; no stale hypothesis labels (H1/H4)
  or stale "3.1--3.4" ranges; all hardcoded Section X.Y references correct.
- Content-loss scan v32 -> v41: 49 removed word-instances, each traced to an
  intended edit; all additions are the new strengthening content.

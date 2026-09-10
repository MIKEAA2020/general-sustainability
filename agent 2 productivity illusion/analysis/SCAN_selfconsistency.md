# SELF-CONSISTENCY CHECK — revision vs itself

Script: `selfcheck.py`. It checks that the revision does not contradict itself (abstract vs §10,
claims table vs demonstrations, number/label consistency), and flags missing provenance labels.

## What passed

- **Masking is consistent.** "narrow" is used 6×, always in a *qualifying* sense (`narrow, bounded,
  transient, deficit-limited`). No sentence presents the illusion as generic/robust.
- **Abstract ↔ §10 agree** on the mechanism (small initial deficit, narrow, transient, bounded) and on
  the key numbers (`5.4 yr` ≈ `~5 yr`; `0.075` ≈ `15 % of b₀A₀`).
- **No stale "no masking" claim remains.** The phrase "no shown scenario exhibits the illusion" was
  removed in the previous round; `§10`, `§5`, `§13` now state the *conditional* mask.
- **Numbers that must co-occur do co-occur**: `0.506 & 0.042` (basin), `5.4 & 0.075` (masking),
  `1.19` (B/C), `85.4` and `231` (τ*), `5.26` (D_E) are all present and not contradicted.

## What the check caught and I fixed

1. **Masking percentage was wrong.** The abstract and §10 said "collapses beyond a modest ~8 %
   overshoot." Re-computation shows the critical deficit is `E − b₀A₀ = 0.075`, which is **≈15 % of the
   initial flow yield `b₀A₀`** (not 8 %). **Fixed** in §1, §5, §10 to "deficit ≈0.075, ≈15 % of `b₀A₀`."
2. **Missing original-model provenance.** The revision quoted `0.506→0.042` (basin), Scenario B/C
   `A≈1.19`, `D_E≈5.26`, and (implicitly) the `M*=0.740/P*=0.370` attractor without stating that these
   were computed on the **original gross-depletion model**, while the corrected `(1‴)` S0 is a **one-sided
   boundary** with no unique interior attractor. **Fixed** by adding a provenance note in §8 and tagging
   the §5 Scenario B/C note.

## Residual non-contradiction (intentional, to preserve)

- The revision both keeps `D` (fork F4 non-default) **and** calls the full system 3-D. This is an
  explicit, documented choice (§2.2 fork note), not a contradiction.
- The `τ*` values (85.4 / 231) are the **corrected** χ-based values, quoted as discrepancies against the
  **manuscript's** 83 / 225 — that framing is intentional and correct.

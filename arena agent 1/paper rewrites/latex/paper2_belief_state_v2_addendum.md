# Belief-State Safety Values, Edition 2 — Addendum

**Editions:** supersedes `paper2_belief_state_v1` (v1 retained). Same title, same author, same register; all four v1 result blocks are carried in full and unchanged.

**Content delta (v1 → v2), implementing the depth directive:**

- **The complete campaign table (Table 1, full width):** the exact V_k(b0) for all 16 grid states × 3 blind-window lengths × 4 horizons (192 cell-horizon combinations), regenerated and projected cell by cell.
- **The type census:** the 384 campaign alpha-vectors realize exactly three types — (1,1) × 72, (1,0) × 156, (0,1) × 156, the mirror symmetry exact.
- **The asymmetric audit (Table 2, Figure 2):** survived mass of each blind two-step sequence at (3/2, 2) with w = 3/10 — {3/10, 3/10, 7/10, 7/10} with the lost branch per sequence; deficit 3/10 = minimal mass, attained.
- **Printed derivations:** the closed form (Corollary 4) and the jump loci and class declaration (Theorems 9–10) now carry proof-register derivations in the text.
- **The class-difference map (Figure 3):** the 36 differing cell-horizon combinations isolated exactly (timing cells × k = 2, 3, 4).
- **The learning-deadline audit (Table 3, Figure 4):** thresholds 21/10 + T_learn/10 with the exact kernel sets for T_learn = 0..4 (|K| = 5, 4, 3, 2, 1 — the fifth value extends v1's four).
- **Figures 1 and 5:** the closed-form staircase panels and the two-floor piecewise-linear value with the attaining alpha-vectors.
- **Section cross-references now print true numbers** (template fix recorded in roadmap v23).

**Verification:** `paper2_belief_state_v2_verification.py` 16/16 — chain 21/21 (stochastic selector 15/15 + hidden-parameter 6/6), plus independent recomputation: hold-class enumeration (96 cells), alpha-recursion vs closed form (192 combinations), brute-force class difference (36), jump loci, type census, two-floor probes, asymmetric masses, deadline kernels, the full 16×12 table projection, and 37 text needles. `paper2_belief_state_figures.py` regenerates the five figures from asserted exact data (6/6 data checks). Build: 5 pages, zero overfull.

**Process notes of record:** one substantive root-cause during tabulation — a naive blind-forever class comparison produces 54 differing combinations and contradicts the declared model, which has revelation at T_obs; the correct unrestricted class (open-loop time-variation within the blind window) restores exactly the theorem's 36. The theorem was right; the first comparison tested the wrong class pair.

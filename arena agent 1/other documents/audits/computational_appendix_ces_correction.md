# CES Witness Correction — A001 §8 (one-turn permission, applied)

**Object.** The other-chat `computational_appendix.md` (archived verbatim at `audits/computational_appendix.md`) contains ten numerical witness blocks for A001 (`uploads/topdown.txt`). Nine verified independently on receipt (turn 49); the CES block was defective.

**Defect.** Block C (Corollary 8.1 — CES essentiality) stated the witness parameters `σ=2, α=0.5, Y₀=10, A₀=2` with displayed values `F(5,0)=3.125, F(10,0)=6.25`. Direct evaluation of A001's own formula, `F(A,0) = Y₀·α^{σ/(σ−1)}·(A/A₀)`:

- with the stated `A₀=2`: F(5,0) = 6.25, F(10,0) = 12.5 — **does not reproduce the displayed values**;
- with `A₀=4`: F(5,0) = 3.125, F(10,0) = 6.25 — **reproduces the displayed values exactly**.

The stated parameter `A₀=2` was therefore the error; the displayed values are consistent with `A₀=4`, which is the parameter the block's computation actually used.

**Correction applied (owner-granted one-turn permission).** A001's §8 itself carried no numerical instance (all symbolic), so the corrected witness is drafted into A001 as **Remark 8.3 (Numerical instance of Corollary 8.1)**, inserted after Remark 8.2 and before the section's closing caveat paragraph:

> **Remark 8.3 (Numerical instance of Corollary 8.1).** With σ = 2, α = 0.5, Y₀ = 10, and A₀ = 4 (any R₀ > 0), the essentiality formula of Corollary 8.1(1) gives F(A, 0) = Y₀·α^{σ/(σ−1)}·A/A₀ = 10·(0.5)²·A/4 = 0.625·A, so F(5, 0) = 3.125 and F(10, 0) = 6.25: at σ > 1 capital alone yields positive output, linear in A at zero resource flow, while at σ ≤ 1 the same instance gives F(A, 0) = 0 for every A — the two sides of the essentiality threshold on one datum.

Pushed to `uploads/topdown.txt` as commit `6599192` and, identically, to A001's corrected working source `revised_articles/A001_viability_theory_corrected.md` as commit `ecb9549` (both API-verified); the two A001 copies are kept in sync. No other byte of either file was changed.

**Verification.** Recomputed: F(5,0)|A₀=4 = 10·0.25·5/4 = 3.125 ✓; F(10,0)|A₀=4 = 10·0.25·10/4 = 6.25 ✓; both sides of the essentiality threshold (σ=2 vs σ≤1) follow Corollary 8.1(1). The remark is consistent with A001's dimensional conventions (reference scales A₀, R₀, Y₀; output per unit time).

**Standing disposition (unchanged).** The remaining nine witness blocks of the archived appendix are still not part of the repo's `formal_supplement_A001_A002_A006_A010.md` (0 hits on receipt). Whether to fold the corrected appendix into that supplement remains an owner decision; this correction makes the CES block ready for any such incorporation, and the archived appendix file itself is left verbatim (this note supersedes its block C).

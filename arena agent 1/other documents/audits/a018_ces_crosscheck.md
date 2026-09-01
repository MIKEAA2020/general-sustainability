# A018 CES cross-check — corrected edition vs the flagged defect, and against the A₀=4-fixed A001 witness

Date: 2026-09-02 (turn 53). Trigger: `audits/previous_rounds_papers_inventory.md` flagged this as
the next concrete audit after the A001 CES fix ("the natural next check is whether A018's CES
instance is consistent with the same dimensional convention"). Sources examined in a fresh
full clone of `MIKEAA2020/general-sustainability` @ `df97c1f`:
`revised_articles/A018_capital_liquidation_corrected.tex` (the corrected edition),
`uploads/manuscript.txt` (the archived source the evaluations were run against),
`research_program/new_packet_A018_A025_line_level_joint_audit.md` (finding A018-L2),
`research_program/article_A018_capital_liquidation/evaluation_and_verification.md`
(line-level item "Lines 348–356: CES parameterization and limits are inconsistent"),
`revised_articles/INDEX.md` (A018 row: "Donor sign, CES, norm, analytical status, fold
hierarchy, and feasible bridges corrected").

## 1. The original defect (exactly as found, archived source)

`uploads/manuscript.txt` lines 352–356 (archived verbatim, as it should be):

> the $\rho=1$ (weak-sustainability) member of the nested CES
> Q = A_TFP [θ(K̂^α L̂^β)^((ρ−1)/ρ) + (1−θ) S_agg^((ρ−1)/ρ)]^(ρ/(ρ−1)),
> which becomes strong-sustainability as ρ→0 (standard identification ρ=(σ−1)/σ,
> σ the elasticity of substitution; ρ=1 is Cobb–Douglas with σ=1).

The joint audit's finding A018-L2 is confirmed on re-derivation: the display treats ρ as the
elasticity-like parameter (exponent (ρ−1)/ρ, ρ=1 ⇒ Cobb–Douglas — both correct under that reading),
while the parenthetical "standard identification ρ=(σ−1)/σ" redefines ρ as the CES *power* and σ
as the elasticity. The two readings cannot cohabit: under ρ=(σ−1)/σ, ρ=1 would require σ→∞
(perfect substitutes, not Cobb–Douglas) and ρ→0 would require σ→1 (Cobb–Douglas, not the
Leontief limit the sentence claims for "strong sustainability"); and "ρ=1 is Cobb–Douglas with
σ=1" is outright contradictory with ρ=(σ−1)/σ at ρ=1. Three mutually inconsistent statements in
one sentence.

## 2. The corrected edition — verified claim by claim

`revised_articles/A018_capital_liquidation_corrected.tex`, Layer 3 region (≈lines 344–356):

- $\mathcal S_{agg} = (\sum \omega_{i,c}(S_{i,c}/S^{ref}_{i,c})^\gamma)^{1/\gamma}$ **"has
  substitution elasticity σ_S = 1/(1−γ)"** — correct for a common-power CES.
  Independent check: pairwise MRS = (ω_i/ω_j)(x_i/x_j)^(γ−1); finite-difference
  d ln(x_j/x_i)/d ln(MRS) at γ=0.5 gives 2.0000 = 1/(1−0.5). ✔
- Nested CES "indexed by elasticity σ_Q>0" with power (σ_Q−1)/σ_Q and outer exponent
  σ_Q/(σ_Q−1): the elasticity of substitution of this two-input CES is exactly σ_Q. ✔
- **"The Cobb–Douglas form is the limit σ_Q→1, not the literal substitution σ_Q=1 into the
  singular display."** Verified: as σ_Q→1 the CES tends to X^θ Y^(1−θ) with X=K̂^α L̂^β;
  numerically at X=4, Y=2, θ=0.7 the σ_Q→1 value is 3.24901 = the Cobb–Douglas value 3.24901,
  and θ=α+β is consistent with the stated α+β+δ_S=1. ✔
- **"The Leontief/noncompensatory limit is σ_Q→0⁺."** Verified: ρ_Q=(σ_Q−1)/σ_Q→−∞ as σ_Q→0⁺,
  and the CES converges monotonically to min(X,Y) (2.2851 → 2.0245 → 2.0024 as σ_Q goes
  10⁻¹ → 10⁻² → 10⁻³ against min = 2.0). ✔
- **No residual ρ in the CES role.** Every remaining $\rho$ in the corrected edition is an
  unrelated object: the specialisation constants μ=ν=ρ=0 (waste/return channels), the
  recovery-routing fractions ρ_{i,j}(T), the waste-decay rate ρW, and the Liebig sharpness ρ_{i,c}.
  The CES now uses exactly one symbol (σ_Q) for elasticity and one power form. ✔
- The sentence "Finite positive σ_Q remains a compensatory production specification and does not
  override componentwise safety constraints" is consistent with the paper's own
  Proposition (no-scalar): the CES appears only as the production/utility layer, never as a
  sustainability certificate. ✔
- Companion fix from the same correction list spot-checked: the donor fraction
  σ_geo = A^geo/(A^geo+A_g0) is now stated "smooth, strictly increasing" in the donor level
  (corrected from "decreasing"; the audit's L1 sign item). ✔

The one symbolic CES utility instance (Layer 4, Arrow 1961, demand derivation) carries no
parameter values and no limits claims; nothing to check beyond its non-certificatory role, which
the text itself states.

## 3. Cross-check against the A001 convention (the actual flagged question)

A001's fixed witness (turn 51, A₀=4): F(A,0) = Y₀·α^(σ/(σ−1))·A/A₀ — with σ=2, α=0.5, Y₀=10,
A₀=4 giving F(5,0)=3.125 and F(10,0)=6.25. Its two conventions are (i) inputs enter as
dimensionless ratios normalized by reference magnitudes (A/A₀), and (ii) the elasticity σ enters
the CES power in the standard (σ−1)/σ form.

A018's corrected CES uses precisely the same two conventions: dimensionless inputs
(K̂=K/K_ref, L̂=L/L_ref, S/S^ref ratios) and elasticity σ_Q in the standard power form with the
correct limits. **Consistency verdict: CONSISTENT.** No shared numerical parameter exists between
the two instances (A001's A₀, Y₀, α, σ=2 do not appear in A018; A018's σ_Q is symbolic with no
stated value), so the stated-parameter/displayed-value defect class that hit A001 (A₀=2 vs A₀=4)
**cannot recur in A018 as written**: the corrected edition contains no numerical CES pair at all.
The two CES instances are different objects — a single-input resource-supply witness (A001) and a
nested aggregate-production function (A018) — and there is nothing left in either that contradicts
the other.

## 4. Verdict

**A018-L2 is fully discharged in the corrected edition.** The corrected .tex's CES block is
internally consistent (one symbol, correct powers, correct Cobb–Douglas and Leontief limits,
verified analytically and numerically) and convention-consistent with the A₀=4-fixed A001 witness.
The archived `uploads/manuscript.txt` retains the old inconsistent form by archival design (the
same pattern as the A001 appendix: archived verbatim, corrected edition carries the fix) — no
action taken there and none needed, matching the owner's archival rule.

**No further correction is required; no new version files.** Remaining A018-related open items are
unchanged and out of our write scope: the evaluation's integration verdict (A018 as candidate
successor of the A012 identity), the other line-level items (norm-dependent cone distance L3,
Tikhonov overstatus L4, fold language), and provenance obligations (code/data/citations) — all
recorded in the registry and the previous-rounds inventory.

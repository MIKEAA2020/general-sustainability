/-
  Formalizations.Comp_Certification
  =================================

  Lean formalization of the theorem layer of

    "Computational Certification" (2026d; source of record:
    `paper2_computational_certification_v15.tex`).

  Scope and fidelity.  The paper builds a finite linear-programming pipeline
  whose optimum is a certified lower bound `ρ` on the continuous-time
  safety value `J`, with verified error inflation `J ≤ ρ + ē`, and whose
  dual-feasible solutions are finite lower-bound certificates.  Formalized
  here:

    * the robust-row soundness (Proposition `prop:rows`, the direction the
      certificates use): a row holding with the precomputed worst-case
      disturbance constant implies every stored-scenario realized
      constraint;
    * the certified sandwich (the abstract `ρ ≤ J ≤ ρ + ē` structure):
      a positive certified lower bound certifies a strictly positive
      safety value — the finite obstruction certificate — and a negative
      inflated upper bound certifies a negative value — viability of some
      policy under the value characterization;
    * the dual-feasible certificate: the paper's Farkas-based
      infeasibility certificate is `Formalizations.farkas_sound` of the
      shared prelude, restated here in the pipeline's terms.

  Not formalized (and why): the existence/attainment machinery
  (weak-* compactness of the policy space, continuity of the violation
  functionals — Proposition `prop:value`'s existence half); the
  continuous-to-finite bridge (Theorem `thm:bridge`) with its sampling and
  enclosure error analysis; the `r + 1` sparsity bound (Carathéodory); and
  the instance-level decodings (three-branch delay threshold, shared-
  authority ladder) — all verified instance-wise in exact rational
  arithmetic by the record's 48/48 check families.
-/

import Formalizations.Prelude

namespace Formalizations.CompCert

/-! ## Robust rows (Proposition `prop:rows`, soundness direction) -/

/-- **Robust-row soundness.**  A row `dotp A x ≤ b - s` holding with the
precomputed worst-case disturbance constant `s` (an upper bound of the
disturbance contribution `c w` over the stored scenario set) implies every
realized constraint `dotp A x + c w ≤ b` over that scenario set.  This is
the direction the LP certificates consume: the program's rows are exact for
polytopic scenario sets because the disturbance maximization separates from
the control term.

Paper reference: Proposition `prop:rows` (robust rows). -/
theorem robust_row_sound {K : Type} [OrdField K] (A x : List K) (b : K)
    (c : K → K) (scen : List K) (s : K)
    (hs : ∀ w, w ∈ scen → c w ≤ s)
    (hrow : dotp A x ≤ b - s) :
    ∀ w, w ∈ scen → dotp A x + c w ≤ b := by
  intro w hw
  have h1 : dotp A x + c w ≤ (b - s) + s := add_le_add hrow (hs w hw)
  rwa [sub_add_cancel] at h1

/-! ## The certified sandwich -/

section Sandwich
variable {K : Type} [OrdField K] {ρ ē J : K}

/-- **Positive lower bound certifies obstruction.**  The program's optimum
`ρ` is a certified lower bound on the safety value `J`; if `ρ` is strictly
positive then so is `J` — a finite obstruction certificate covering every
measurable policy.

Paper reference: the abstract's certified lower bound, and Proposition
`prop:value` (value and nonviability): `B₀ ∉ kernel ↔ J > 0`. -/
theorem positive_bound_obstruction (hlo : ρ ≤ J) (hpos : 0 < ρ) : 0 < J :=
  lt_of_lt_of_le hpos hlo

/-- **Inflated upper bound certifies a negative value.**  The program's own
verified moment-error bound `ē` inflates the optimum into a certified upper
bound on the value; if the inflated bound is strictly negative, so is the
value.

Paper reference: the abstract's error-inflation inequality
`ρ ≤ J ≤ ρ + ē + δ + L h_t`; stated here with the error terms absorbed
into `ē`. -/
theorem inflated_upper_bound_negative (hhi : J ≤ ρ + ē) (hmargin : ρ + ē < 0) :
    J < 0 :=
  lt_of_le_of_lt hhi hmargin

/-- **The certified sandwich, both directions at once.**  The pair of
certified bounds brackets the value; the two margin tests are the finite
obstruction and viability certificates respectively.

Paper reference: the abstract's bound chain. -/
theorem certified_sandwich (hlo : ρ ≤ J) (hhi : J ≤ ρ + ē) :
    (0 < ρ → 0 < J) ∧ (ρ + ē < 0 → J < 0) :=
  ⟨fun hpos => positive_bound_obstruction hlo hpos,
    fun hmargin => inflated_upper_bound_negative hhi hmargin⟩

/-- **Margin obstruction under the value characterization.**  If a
robustly-safe policy exists exactly when the value is nonpositive, then a
strictly positive certified lower bound certifies that no policy in the
class is robustly safe — the pipeline's obstruction verdict.

Paper reference: Proposition `prop:value`: `B₀ ∉ kernel ↔ J > 0`, combined
with the certified lower bound. -/
theorem margin_obstruction_verdict {A : Type} (F : A → A → K)
    (hchar : ((∃ π, ∀ a, F a π ≤ 0) ↔ J ≤ 0))
    (hlo : ρ ≤ J) (hpos : 0 < ρ) :
    ¬ ∃ π, ∀ a, F a π ≤ 0 := by
  intro hex
  exact (positive_bound_obstruction hlo hpos).2 (hchar.mp hex)

end Sandwich

/-! ## The dual-feasible certificate in the pipeline's terms -/

/-- **Dual-feasible certificate.**  Nonnegative multipliers on the robust
rows whose aggregate control projection vanishes and whose aggregate
right-hand constant is negative certify that no control satisfies the row
system — the pipeline's finite lower-bound certificate, carried by the
shared prelude's Farkas soundness.

Paper reference: "every dual-feasible solution yields a finite lower-bound
certificate covering every measurable policy" (abstract), the Farkas
direction used by the certificate. -/
theorem dual_feasible_certificate {K : Type} [OrdField K]
    (a : Nat → List K) (b : Nat → K) (lam : Nat → K) (x : List K) (n : Nat)
    (hlen : ∀ i, i < n → (a i).length = x.length)
    (hnonneg : ∀ i, i < n → 0 ≤ lam i)
    (hzero : linComb (List.replicate x.length 0) lam a n = List.replicate x.length 0)
    (hneg : sumRange (fun i => lam i * b i) n < 0) :
    ¬ (∀ i, i < n → dotp (a i) x ≤ b i) :=
  farkas_sound a b lam x n hlen hnonneg hzero hneg

end Formalizations.CompCert

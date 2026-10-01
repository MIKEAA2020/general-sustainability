/-
  Formalizations.E1_ForecastLadder
  ===============================

  Lean formalization of the theorem layer of

    "Applied Forecast Ladder" (E1; source of record:
    `paperE1_cod_forecast_ladder_v56.tex`).

  Scope and fidelity.  The paper is an applied record (49/49 machine
  checks over the Northern-cod assessment record) whose mathematical
  backbone is the forecast-ladder construction: a ladder of calibrated
  forecast levels whose margins telescope, whose per-level bounds sum to
  the total bound, and whose monotone levels make the ladder a
  bookkeeping-exact instrument.  Formalized here, over the abstract
  ordered field:

    * the telescoping identity of the ladder: the partial sums of the
      forward margins reconstruct the total drift exactly
      (`f 0 - f N`), the identity every level of the paper's
      construction instantiates;
    * the monotone-summation bound: per-level bounds aggregate — the
      ladder's total is at most the sum of the level bounds, and at least
      the sum of the level floors (the two-sided bracket);
    * the ascent law: if every level's step is nonnegative, the ladder
      ascends (`f 0 ≤ f N`) — the calibrated-margin monotonicity the
      applied readings consume.

  Not formalized (and why): the paper's specification tables, calibrated
  numerical levels, and the COD (collapse-of-detection) verdicts are
  statements about the assessment record, certified instance-wise by the
  record's 49/49 check families; the paper reports applied results in
  journal (non-theorem) form, so the theorem layer is the ladder's generic
  algebra above.
-/

import Formalizations.Prelude

namespace Formalizations.E1

/-! ## The ladder bookkeeping identities -/

section Ladder
variable {K : Type} [OrdField K] {f g lo hi : Nat → K}

/-- **Telescoping identity of the ladder.**  The partial sums of the
forward margins reconstruct the total drift exactly.

Paper reference: the forecast-ladder construction — the level margins of
the calibrated ladder telescope to the total change; every level of the
paper's construction instantiates this identity. -/
theorem ladder_telescope (f : Nat → K) (N : Nat) :
    sumRange (fun i => f i - f (i + 1)) N = f 0 - f N :=
  sumRange_telescope f N

/-- **Monotone summation, upper bound.**  Per-level bounds aggregate: if
  every level's margin is at most its bound, the ladder's total is at
  most the sum of the bounds. -/
theorem ladder_bound_upper (h : ∀ i, g i ≤ hi i) (N : Nat) :
    sumRange g N ≤ sumRange hi N :=
  sumRange_le_sumRange' g hi N (fun i _ => h i)

/-- **Monotone summation, lower bound.**  Per-level floors aggregate. -/
theorem ladder_bound_lower (h : ∀ i, lo i ≤ g i) (N : Nat) :
    sumRange lo N ≤ sumRange g N :=
  sumRange_le_sumRange' lo g N (fun i _ => h i)

/-- **The two-sided ladder bracket.**  If every level's margin is
  bracketed between its floor and its bound, the ladder's total is
  bracketed by the summed floors and bounds.

Paper reference: the ladder's calibrated-margin bracketing, the bookkeeping
identity behind the record's margin accounting. -/
theorem ladder_bracket (hlo : ∀ i, lo i ≤ g i) (hhi : ∀ i, g i ≤ hi i)
    (N : Nat) :
    sumRange lo N ≤ sumRange g N ∧ sumRange g N ≤ sumRange hi N :=
  ⟨ladder_bound_lower hlo N, ladder_bound_upper hhi N⟩

/-- **The ascent law.**  If every level's step is nonnegative, the ladder
  ascends: the initial level never exceeds the level at any horizon.

Paper reference: the calibrated-margin monotonicity the applied readings
consume — a ladder whose steps never descend never descends. -/
theorem ladder_ascent (hstep : ∀ i, f i ≤ f (i + 1)) :
    ∀ N, f 0 ≤ f N := by
  intro N
  induction N with
  | zero => exact le_refl (f 0)
  | succ m ih => exact le_trans ih (hstep m)

end Ladder

end Formalizations.E1

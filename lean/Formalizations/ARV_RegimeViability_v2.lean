/-
  Formalizations.ARV_RegimeViability_v2
  =====================================

  Closes the two gaps `lean_audit_v14.md` identified in
  `ARV_RegimeViability`, both from Lemma `lem:bracket` (harvest-free
  multiplier bracket) of "Applied Regime Viability":

    (1) the **max upper bound** `g ≤ max{ρ + r, ρ/(1-r)}` — no `max`
        appeared anywhere in v1, only the two separate lower bounds;
    (2) the **converse** — the paper's final claim is an *iff*
        ("the upper bound is strictly below `1` if and only if both
        `ρ + r < 1` and `ρ/(1-r) < 1`"), whereas v1's `bracket_subunitary`
        proved only the forward direction, and about `g` rather than
        about the upper bound.

  With both closed, `lem:bracket` is formalized in full and the entry moves
  from *partial* to *result*.

  Why `omax` is defined here.  `OrdField` (Prelude) is a bare
  ordered-field interface: it carries `le_total` but **no `max` operation**,
  and this project has no Mathlib dependency.  So the bracket's `max` is
  introduced locally as `omax`, with exactly the four laws the lemma needs
  (`le_omax_left`, `le_omax_right`, `omax_le`, `omax_lt`) proved from
  `le_total` alone.  Nothing about `omax` is specific to the application; it
  is the standard total-order maximum.

  Fidelity note.  v1's header cites `applied_regime_viability_v6.tex` as the
  source of record; the current edition is `v9`.  The statement of
  `lem:bracket` is unchanged between them, so v1's formalization is not
  stale — only the citation is.  This file cites v9.
-/

import Formalizations.Prelude
import Formalizations.ARV_RegimeViability

namespace Formalizations.ARV

/-! ## A maximum for an abstract ordered field -/

section Omax
variable {K : Type} [OrdField K]

/-- The maximum of two elements, from `le_total` alone. -/
noncomputable def omax (a b : K) : K := by
  classical
  exact if a ≤ b then b else a

/-- `omax` reduces to its right argument when `a ≤ b`. -/
theorem omax_of_le {a b : K} (h : a ≤ b) : omax a b = b := by
  classical
  simp [omax, h]

/-- `omax` reduces to its left argument when `¬ a ≤ b`. -/
theorem omax_of_not_le {a b : K} (h : ¬ a ≤ b) : omax a b = a := by
  classical
  simp [omax, h]

theorem le_omax_left (a b : K) : a ≤ omax a b := by
  classical
  by_cases h : a ≤ b
  · rw [omax_of_le h]; exact h
  · rw [omax_of_not_le h]; exact le_refl a

theorem le_omax_right (a b : K) : b ≤ omax a b := by
  classical
  by_cases h : a ≤ b
  · rw [omax_of_le h]; exact le_refl b
  · rw [omax_of_not_le h]
    exact (le_total a b).elim (fun hab => False.elim (h hab)) (fun hba => hba)

theorem omax_le {a b c : K} (h1 : a ≤ c) (h2 : b ≤ c) : omax a b ≤ c := by
  classical
  by_cases h : a ≤ b
  · rw [omax_of_le h]; exact h2
  · rw [omax_of_not_le h]; exact h1

theorem omax_lt {a b c : K} (h1 : a < c) (h2 : b < c) : omax a b < c := by
  classical
  by_cases h : a ≤ b
  · rw [omax_of_le h]; exact h2
  · rw [omax_of_not_le h]; exact h1

/-- The law behind the paper's "if and only if": the upper bound is below a
threshold exactly when both bracket forms are. -/
theorem omax_lt_iff (a b c : K) : omax a b < c ↔ a < c ∧ b < c := by
  constructor
  · intro h
    exact ⟨lt_of_le_of_lt (le_omax_left a b) h,
           lt_of_le_of_lt (le_omax_right a b) h⟩
  · intro h
    exact omax_lt h.1 h.2

end Omax

/-! ## Closing `lem:bracket` -/

section BracketMax
variable {K : Type} [OrdField K] {B B' C g : K}

/-- **Upper bracket, first form** (removals after growth,
`B' + C = g·B`): `g` is the first bracket form, hence at most the max. -/
theorem bracket_upper_form1 (hB : B ≠ 0) (hform : B' + C = g * B) :
    g ≤ omax (B' / B + C / B) ((B' / B) / (1 - C / B)) := by
  rw [← bracket_form1 hB hform]
  exact le_omax_left _ _

/-- **Upper bracket, second form** (removals before growth,
`B' = g·(B - C)`): `g` is the second bracket form, hence at most the
max. -/
theorem bracket_upper_form2 (hB : B ≠ 0) (hr : 1 - C / B ≠ 0)
    (hform : B' = g * (B - C)) :
    g ≤ omax (B' / B + C / B) ((B' / B) / (1 - C / B)) := by
  rw [← bracket_form2 hB hr hform]
  exact le_omax_right _ _

/-- **The sandwich, first form**: `ρ ≤ g ≤ max{ρ + r, ρ/(1-r)}`.

This is the paper's `ρ ≤ g_t ≤ max{ρ + r, ρ/(1-r)}` in full. -/
theorem bracket_sandwich_form1 (hB : B ≠ 0) (hr : 0 ≤ C / B)
    (hform : B' + C = g * B) :
    B' / B ≤ g ∧ g ≤ omax (B' / B + C / B) ((B' / B) / (1 - C / B)) := by
  constructor
  · rw [← bracket_form1 hB hform]
    exact bracket_lower_form1 (K := K) hr
  · exact bracket_upper_form1 hB hform

/-- **The sandwich, second form**. -/
theorem bracket_sandwich_form2 (hB : B ≠ 0) (hr : 1 - C / B ≠ 0)
    (hρ : 0 ≤ B' / B) (hr0 : 0 ≤ C / B) (hr1 : C / B ≤ 1)
    (hform : B' = g * (B - C)) :
    B' / B ≤ g ∧ g ≤ omax (B' / B + C / B) ((B' / B) / (1 - C / B)) := by
  constructor
  · rw [← bracket_form2 hB hr hform]
    exact bracket_lower_form2 (K := K) hρ hr0 hr1 hr
  · exact bracket_upper_form2 hB hr hform

/-- **The sub-unitary certificate, iff form** — the second gap closed.

The paper: "the upper bound is strictly below `1` if and only if both
`ρ + r < 1` and `ρ/(1-r) < 1`."  v1 proved only the forward direction, and
about `g`. -/
theorem bracket_upper_lt_one_iff :
    omax (B' / B + C / B) ((B' / B) / (1 - C / B)) < (1 : K) ↔
      B' / B + C / B < 1 ∧ (B' / B) / (1 - C / B) < 1 :=
  omax_lt_iff _ _ _

/-- **`g` is sub-unitary iff its own bracket form is** — first form.

Sharper than v1's `bracket_subunitary`, which passed through a disjunction
over both forms and so needed *both* to be below `1`. -/
theorem bracket_subunitary_form1 (hB : B ≠ 0) (hform : B' + C = g * B) :
    g < 1 ↔ B' / B + C / B < 1 := by
  rw [← bracket_form1 hB hform]

/-- **`g` is sub-unitary iff its own bracket form is** — second form. -/
theorem bracket_subunitary_form2 (hB : B ≠ 0) (hr : 1 - C / B ≠ 0)
    (hform : B' = g * (B - C)) :
    g < 1 ↔ (B' / B) / (1 - C / B) < 1 := by
  rw [← bracket_form2 hB hr hform]

/-- Combining: under either accounting form, `g < 1` follows from the
upper bound being below `1`.  (The converse fails, and correctly so — `g`
equals only *one* of the two bracket forms, so `g < 1` says nothing about
the other.  The paper's iff is about the *upper bound*, which is
`bracket_upper_lt_one_iff` above.) -/
theorem bracket_subunitary_of_upper_form1 (hB : B ≠ 0)
    (hform : B' + C = g * B)
    (hup : omax (B' / B + C / B) ((B' / B) / (1 - C / B)) < (1 : K)) :
    g < 1 :=
  lt_of_le_of_lt (bracket_upper_form1 hB hform) hup

theorem bracket_subunitary_of_upper_form2 (hB : B ≠ 0)
    (hr : 1 - C / B ≠ 0) (hform : B' = g * (B - C))
    (hup : omax (B' / B + C / B) ((B' / B) / (1 - C / B)) < (1 : K)) :
    g < 1 :=
  lt_of_le_of_lt (bracket_upper_form2 hB hr hform) hup

end BracketMax

end Formalizations.ARV

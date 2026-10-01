/-
  Formalizations.ARV_RegimeViability
  ==================================

  Lean formalization of the theorem layer of

    "Applied Regime Viability" (2026a; source of record:
    `applied_regime_viability_v6.tex`).

  Scope and fidelity.  The paper is an applied record (236/236 machine
  checks over the audited fisheries record) organized around certified
  interval accounting: each certified interval carries biomass readings
  `B_t, B_{t+1} > 0` and a removals row `C ≥ 0`, and the accounting lemmas
  bracket the unobservable non-fishing growth factor `g`.  Formalized here,
  over the abstract ordered field with `ρ = B'/B` and `r = C/B`:

    * the two accounting forms of Lemma `lem:bracket` (harvest-free
      multiplier bracket): `g = ρ + r` (removals after growth) and
      `g = ρ/(1-r)` (removals before growth);
    * the lower bracket `ρ ≤ g` in both forms;
    * the sub-unitary certificate: if both forms are strictly below one,
      then `g < 1` under either form — no placement of the realized
      removals leaves the non-fishing account non-contracting;
    * the contraction reading: `g < 1` certifies `B' < B` under either
      accounting form.

  Not formalized (and why): the record-level propositions (survey-index
  reconstruction, era separation, covariate crossing, band classification)
  are statements about the audited data tables, certified by the record's
  check families.
-/

import Formalizations.Prelude

namespace Formalizations.ARV

/-! ## Division helpers -/

section Helpers
variable {K : Type} [OrdField K] {a b c x y z : K}

theorem one_sub_div (b : K) (hb : b ≠ 0) : (1 : K) - c / b = (b - c) / b := by
  rw [sub_div b c b, div_eq b b, mul_inv_cancel_field hb]

theorem mul_div_self (a b : K) (hb : b ≠ 0) : a * b / b = a := by
  rw [div_eq, mul_assoc, mul_inv_cancel_field hb, mul_one]

theorem sub_sub_self (a b : K) : a - (a - b) = b := by
  apply add_right_cancel (b := a - b)
  rw [sub_add_cancel, sub_eq, ← add_assoc, add_comm b a, add_assoc,
    add_neg_cancel, add_zero]

theorem mul_right_cancel' {a b c : K} (hc : c ≠ 0) (h : a * c = b * c) :
    a = b :=
  mul_left_cancel hc (by rw [mul_comm c a, mul_comm c b]; exact h)

theorem mul_lt_mul_of_pos_right (h : a < b) (hc : 0 < c) : a * c < b * c := by
  refine lt_of_le_of_ne (mul_le_mul_of_nonneg_right h.1 hc.1) ?_
  intro heq
  apply h.2
  have hcom : c * a = c * b := by
    rw [mul_comm c a, mul_comm c b]; exact heq
  exact le_of_eq (mul_left_cancel (ne_of_gt hc) hcom).symm

end Helpers

/-! ## The harvest-free multiplier bracket -/

section Bracket
variable {K : Type} [OrdField K] {B B' C g : K}

/-- **First accounting form**: removals deducted after growth,
`B' + C = g · B`, gives `g = ρ + r`.

Paper reference: Lemma `lem:bracket`, first form. -/
theorem bracket_form1 (hB : B ≠ 0) (hform : B' + C = g * B) :
    B' / B + C / B = g := by
  have h1 : B' / B + C / B = (B' + C) / B := by
    rw [div_eq, div_eq, div_eq, ← right_distrib]
  rw [h1, hform, mul_div_self g B hB]

/-- **Second accounting form**: removals deducted before growth,
`B' = g · (B - C)`, gives `g = ρ/(1-r)`.

Paper reference: Lemma `lem:bracket`, second form. -/
theorem bracket_form2 (hB : B ≠ 0) (hr : 1 - C / B ≠ 0)
    (hform : B' = g * (B - C)) :
    (B' / B) / (1 - C / B) = g := by
  have h1 : B' / B = g * (1 - C / B) := by
    rw [hform, div_eq, mul_assoc, ← div_eq, one_sub_div B hB]
  rw [h1, div_eq, mul_assoc, mul_inv_cancel_field hr, mul_one]

/-- **Lower bracket, first form**: `ρ ≤ g` when removals are
nonnegative. -/
theorem bracket_lower_form1 (hr : 0 ≤ C / B) : B' / B ≤ B' / B + C / B := by
  have h : (0 : K) ≤ C / B := hr
  have h1 := add_le_add_left h (B' / B)
  rwa [add_zero] at h1

/-- **Lower bracket, second form**: `ρ ≤ ρ/(1-r)` when `ρ ≥ 0` and
`0 ≤ r ≤ 1` — the pre-growth form can only inflate the multiplier. -/
theorem bracket_lower_form2 (hρ : 0 ≤ B' / B) (hr : 0 ≤ C / B)
    (hr1 : C / B ≤ 1) (hrne : 1 - C / B ≠ 0) :
    B' / B ≤ (B' / B) / (1 - C / B) := by
  have hkey : B' / B * (1 - C / B) ≤ B' / B := by
    have h2 : 0 ≤ B' / B - B' / B * (1 - C / B) := by
      have h3 : B' / B - B' / B * (1 - C / B) = B' / B * (C / B) := by
        rw [mul_sub, mul_one, sub_sub_self]
      rw [h3]
      exact mul_nonneg hρ hr
    exact sub_nonneg.mp h2
  have hpos : (0 : K) < 1 - C / B :=
    lt_of_le_of_ne (sub_nonneg.mpr hr1) hrne.symm
  have h4 : (B' / B * (1 - C / B)) / (1 - C / B) ≤ (B' / B) / (1 - C / B) :=
    div_le_div_right hpos hkey
  rw [mul_div_self _ _ hrne] at h4
  exact h4

/-- **Sub-unitary certificate**: if both accounting forms are strictly
below one, the multiplier is strictly below one under either form — no
placement of the realized removals within the interval's accounting can
leave the non-fishing account non-contracting.

Paper reference: Lemma `lem:bracket`, closing equivalence (the certificate
direction). -/
theorem bracket_subunitary (hform : g = B' / B + C / B ∨ g = (B' / B) / (1 - C / B))
    (h1 : B' / B + C / B < 1) (h2 : (B' / B) / (1 - C / B) < 1) :
    g < 1 := by
  cases hform with
  | inl hl =>
      rw [← hl] at h1
      exact h1
  | inr hr =>
      rw [← hr] at h2
      exact h2

/-- **Contraction reading, first form**: a sub-unitary multiplier with
nonnegative removals certifies `B' < B`. -/
theorem contraction_form1 (hB : 0 < B) (hC : 0 ≤ C) (hg : g < 1)
    (hform : B' + C = g * B) : B' < B := by
  have h1 : g * B < 1 * B := mul_lt_mul_of_pos_right hg hB
  rw [← hform, one_mul'] at h1
  have h2 : B' ≤ B' + C := by
    have h3 : B' + 0 ≤ B' + C := add_le_add_left hC B'
    rwa [add_zero] at h3
  exact lt_of_le_of_lt h2 h1

/-- **Contraction reading, second form**: with certified under-harvest
(`B - C > 0`), a sub-unitary multiplier certifies `B' < B`. -/
theorem contraction_form2 (hBC : 0 < B - C) (hC : 0 ≤ C) (hg : g < 1)
    (hform : B' = g * (B - C)) : B' < B := by
  have h1 : g * (B - C) < 1 * (B - C) := mul_lt_mul_of_pos_right hg hBC
  rw [← hform, one_mul'] at h1
  have h2 : B - C ≤ B := by
    have h3 : -C ≤ -0 := neg_le_neg hC
    rw [neg_zero] at h3
    have h4 : B + -C ≤ B + 0 := add_le_add_left h3 B
    rw [add_zero] at h4
    rwa [← sub_eq B C] at h4
  exact lt_of_lt_of_le h1 h2

end Bracket

end Formalizations.ARV

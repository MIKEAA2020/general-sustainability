/-
  Formalizations.P3_Rational
  ==========================

  **`prop:pl`'s rationality clause, and the layer's first concrete model.**

  `prop:pl` closes with:

  > Over rational `T`, `g`, and priors, every `α` is an exact rational
  > vector, every `V^Π_k(b)` at a rational belief is an exact rational, and
  > the attaining witness is part of the computation.

  and its proof says only: "rational transition and observation data with
  rational `Γ^Π_k` give rational backups, by induction".

  Two things blocked this, and they are different in kind.

  ## 1. The layer had **no concrete model at all**

  Every theorem is proved from the `OrdField K` interface, which is the
  right discipline — but nothing had ever shown the interface to be
  satisfiable. That is fixed here: **`instance : OrdField Rat`**. This is
  not a formality. It makes the entire layer non-vacuous (every theorem
  now has a model), and it is what "exact rational arithmetic" in the
  paper means operationally: over `ℚ`, `DecidableEq` is available, so the
  paper's "duplicates removed by exact equality" is exact rather than
  approximate.

  `ℚ` is supplied by Lean's `Init`, and its ordered-field laws are already
  proved there; this module only assembles them into the layer's
  interface. Three fields needed short proofs (`zero_ne_one`,
  `zero_le_one` by decision; `add_le_add` from `Rat.add_le_add_left`).

  ## 2. "Is rational" is not expressible over an abstract `K`

  Instantiating `K := ℚ` alone does **not** discharge the clause: over
  `ℚ` every element is rational, so the statement would be vacuous. The
  content of the clause is the **closure of the construction** — the
  induction the paper's proof invokes. So rationality is introduced the
  same way the rest of the layer is built: as an interface.

      RatSub K   a predicate `IsRat : K → Prop` closed under 0, 1, +, −, ·, ⁻¹

  and the theorems proved are closure theorems: rational data in,
  rational alpha-vectors and values out. At `K = ℚ` the interface is
  satisfied trivially (`IsRat := fun _ => True`), so the layer's
  discipline is preserved *and* the statement is non-vacuous where it has
  content — at an abstract `K`, where `IsRat` picks out the rational
  subfield.

  ## Honest scope

  * The rationality proved here is for the **segment form** ("for a blind
    open-loop window the equivalent segment form applies"), which is what
    `P3_RobustPL` formalizes: `α^seg` is a **0/1 survival indicator**, so
    it is rational with no hypothesis on the data at all. The general
    masked backup needs rational `T` and `g` on `SafeMDP`'s stochastic
    kernels — the *other* operator, out of scope by design since v24
    (`rem:operators`).
  * The "attaining witness is part of the computation" half of the clause
    is `P3_SurvivableAdm.VfamAdm_finite_range` (v30) and
    `P3_Freeze_Noisy.Vfam_finite_range`: the maximum is attained at a
    named set of the frozen family.

  ## Contents

    instance : OrdField Rat    the layer's first concrete model
    RatSub, IsRat              the rationality interface
    rat_lsum, rat_lmax, rat_ind, …   closure under the layer's operators
    alphaSeg_rat               `α^seg` is rational (0/1)
    VR_rat, VFb_rat, VfamAdm_rat     values are rational at rational beliefs
    instance : RatSub Rat      the interface is satisfiable
-/

import Formalizations.Prelude
import Formalizations.P3_Deterministic
import Formalizations.P3_Freeze_Noisy
import Formalizations.P3_Sufficiency
import Formalizations.P3_Bridge
import Formalizations.P3_Viable
import Formalizations.P3_Feedback
import Formalizations.P3_FeedbackValue
import Formalizations.P3_SurvivableAdm
import Formalizations.P3_BlindValue
import Formalizations.P3_RobustPL

namespace Formalizations.P3

open Formalizations
open Formalizations.POMDP

set_option linter.unusedSectionVars false

/-! ## The concrete model -/

/-- **`ℚ` is a model of the layer's `OrdField` interface.**  Every theorem
in this layer was proved at an abstract `[OrdField K]`; this instance makes
them all statements about the rationals too, and shows the interface is
satisfiable. The ordered-field laws are `Init`'s; only `zero_ne_one`,
`zero_le_one` and `add_le_add` are assembled here. -/
instance ratOrdField : OrdField Rat where
  zero := 0
  one := 1
  add := fun a b => a + b
  mul := fun a b => a * b
  neg := fun a => -a
  inv := fun a => a⁻¹
  le := fun a b => a ≤ b
  add_assoc := Rat.add_assoc
  add_comm := Rat.add_comm
  zero_add := Rat.zero_add
  add_neg_cancel := Rat.add_neg_cancel
  mul_assoc := Rat.mul_assoc
  mul_comm := Rat.mul_comm
  one_mul := Rat.one_mul
  mul_inv_cancel := Rat.mul_inv_cancel
  inv_zero := Rat.inv_zero
  zero_ne_one := by decide
  zero_le_one := by decide
  left_distrib := Rat.mul_add
  le_refl := by intro a; exact Rat.le_refl
  le_trans := by intro a b c; exact Rat.le_trans
  le_antisymm := by intro a b hab hba; exact Rat.le_antisymm hab hba
  le_total := by intro a b; exact Rat.le_total
  add_le_add := by
    intro a b c d hab hcd
    calc
      a + c ≤ a + d := (Rat.add_le_add_left (a := c) (b := d) (c := a)).mpr hcd
      _ = d + a := by rw [Rat.add_comm]
      _ ≤ d + b := (Rat.add_le_add_left (a := a) (b := b) (c := d)).mpr hab
      _ = b + d := by rw [Rat.add_comm]
  mul_le_mul_of_nonneg' := by
    intro a b c hab hc
    exact Rat.mul_le_mul_of_nonneg_right hab hc

/-- **Evidence that the instance works**: the feedback value theorem, read
at `K = ℚ`. This elaborates only if `ℚ` really carries the interface. -/
theorem rat_model_check {X A D Y : Type} (M : DetMDP Rat X A D Y) (k : Nat)
    (b : Mass Rat X) : VFb M k b ≤ totalD M b :=
  VFb_le_totalD M k b

/-- Over `ℚ` the paper's "duplicates removed by exact equality" is exact:
rational equality is decidable, so `Γ`-deduplication is a computation and
not an approximation. -/
theorem rat_exact_dedup (a b : Rat) : a = b ∨ a ≠ b := by
  by_cases h : a = b
  · exact Or.inl h
  · exact Or.inr h

/-! ## The rationality interface -/

/-- A rationality predicate: a subfield-like subset of `K`, closed under
the field operations. Modelled on the layer's own discipline — an
interface, not a construction. -/
class RatSub (K : Type) [OrdField K] where
  isRat : K → Prop
  rat_zero : isRat (0 : K)
  rat_one : isRat (1 : K)
  rat_add : ∀ {a b : K}, isRat a → isRat b → isRat (a + b)
  rat_neg : ∀ {a : K}, isRat a → isRat (-a)
  rat_mul : ∀ {a b : K}, isRat a → isRat b → isRat (a * b)
  rat_inv : ∀ {a : K}, isRat a → isRat a⁻¹

variable {K : Type} [OrdField K] [RatSub K]
variable {X A D Y : Type}

/-- `x` is rational. -/
def IsRat (x : K) : Prop := RatSub.isRat (K := K) x

theorem rat_zero : IsRat (0 : K) := RatSub.rat_zero (K := K)
theorem rat_one : IsRat (1 : K) := RatSub.rat_one (K := K)
theorem rat_add {a b : K} : IsRat a → IsRat b → IsRat (a + b) := RatSub.rat_add (K := K)
theorem rat_neg {a : K} : IsRat a → IsRat (-a) := RatSub.rat_neg (K := K)
theorem rat_mul {a b : K} : IsRat a → IsRat b → IsRat (a * b) := RatSub.rat_mul (K := K)
theorem rat_inv {a : K} : IsRat a → IsRat a⁻¹ := RatSub.rat_inv (K := K)

theorem rat_sub {a b : K} (ha : IsRat a) (hb : IsRat b) : IsRat (a - b) :=
  rat_add ha (rat_neg hb)

theorem rat_div {a b : K} (ha : IsRat a) (hb : IsRat b) : IsRat (a / b) :=
  rat_mul ha (rat_inv hb)

/-- A finite sum of rationals is rational. -/
theorem rat_lsum : ∀ (l : List K), (∀ x, x ∈ l → IsRat x) → IsRat (lsum l) := by
  intro l
  induction l with
  | nil =>
      intro h
      simpa [lsum] using rat_zero
  | cons y ys ih =>
      intro h
      simp [lsum]
      exact rat_add (h y (by simp)) (ih (fun x hx => h x (by simp [hx])))

/-- A maximum of finitely many rationals is rational — because the maximum
is *attained* (`lmax_isMax`), not merely approached. -/
theorem rat_lmax {l : List K} (hne : l ≠ []) (h : ∀ x, x ∈ l → IsRat x) :
    IsRat (lmax l) :=
  h (lmax l) (lmax_isMax hne).1

/-- Indicators are rational: they are `0` or `1`. -/
theorem rat_ind (g : X → Bool) (x : X) : IsRat (ind (K := K) g x) := by
  unfold ind
  cases g x <;> simp [rat_zero, rat_one]

/-! ## Rationality of the segment form -/

/-- **`α^seg` is rational.** It is the survival indicator
`ind (survT M t)`, hence `0` or `1` — rational with no hypothesis on the
data at all. This is the segment form of `prop:pl`. -/
theorem alphaSeg_rat (M : DetMDP K X A D Y) (t : List A) (x : X) :
    IsRat (alphaSeg M t x) := by
  unfold alphaSeg
  exact rat_ind (K := K) (survT M t) x

/-- **Survived mass is rational at a rational belief.** -/
theorem smass_rat (M : DetMDP K X A D Y) (t : List A) (b : Mass K X)
    (hb : ∀ x, IsRat (b.f x)) : IsRat (smass M t b) := by
  unfold smass
  apply rat_lsum
  intro x hx
  rcases List.mem_map.mp hx with ⟨y, hy, rfl⟩
  exact rat_mul (hb y) (rat_ind (K := K) (survT M t) y)

/-- **The blind degenerated value is rational at a rational belief** —
`prop:pl`'s "every `V_k(b)` at a rational belief is an exact rational",
for the segment form. -/
theorem VR_rat (M : DetMDP K X A D Y) (k : Nat) (b : Mass K X)
    (hb : ∀ x, IsRat (b.f x)) : IsRat (VR M k b) := by
  unfold VR
  apply rat_lmax (map_ne_nil (fun t => smass M t b) (tuples_ne M k))
  intro z hz
  rcases List.mem_map.mp hz with ⟨t, ht, rfl⟩
  exact smass_rat M t b hb

/-- **The feedback value is rational at a rational belief.** -/
theorem VFb_rat (M : DetMDP K X A D Y) (k : Nat) (b : Mass K X)
    (hb : ∀ x, IsRat (b.f x)) : IsRat (VFb M k b) := by
  unfold VFb
  apply rat_lmax (map_ne_nil (fun S => bS S b) (SfamFB_ne M k))
  intro z hz
  rcases List.mem_map.mp hz with ⟨S, hS, rfl⟩
  unfold bS
  apply rat_lsum
  intro x hx
  rcases List.mem_map.mp hx with ⟨y, hy, rfl⟩
  exact hb y

/-- **The admissible blind family value is rational at a rational
belief.** -/
theorem VfamAdm_rat (M : DetMDP K X A D Y) (k : Nat) (b : Mass K X)
    (hb : ∀ x, IsRat (b.f x)) : IsRat (VfamAdm M k b) := by
  unfold VfamAdm
  apply rat_lmax (map_ne_nil (fun S => bS S b) (SfamAdm_ne M k))
  intro z hz
  rcases List.mem_map.mp hz with ⟨S, hS, rfl⟩
  unfold bS
  apply rat_lsum
  intro x hx
  rcases List.mem_map.mp hx with ⟨y, hy, rfl⟩
  exact hb y

/-- **The attaining witness is part of the computation**: the value is
attained at a named set of the frozen family. This is the other half of
`prop:pl`'s last clause, for the admissible blind family. -/
theorem VfamAdm_rat_witness (M : DetMDP K X A D Y) (k : Nat) (b : Mass K X) :
    ∃ S, S ∈ SfamAdm M 0 ∧ VfamAdm M k b = bS S b :=
  VfamAdm_finite_range M k b

/-! ## The interface is satisfiable -/

/-- At `K = ℚ` every element is rational, so the interface holds
trivially. Together with `ratOrdField` this gives a **model of the
rationality interface**, i.e. the axioms are not empty. -/
instance ratSubRat : RatSub Rat where
  isRat := fun _ => True
  rat_zero := trivial
  rat_one := trivial
  rat_add := by intro a b ha hb; trivial
  rat_neg := by intro a ha; trivial
  rat_mul := by intro a b ha hb; trivial
  rat_inv := by intro a ha; trivial

end Formalizations.P3

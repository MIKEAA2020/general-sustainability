/-
  Formalizations.Prelude
  ======================

  Shared infrastructure for the Lean formalization layer of the
  `general-sustainability` paper family (obstruction calculus, computational
  certification, dual certificates, exact belief computation, probabilistic
  sufficiency, regime viability, forecast ladder).

  Design constraint: this project has NO external dependencies (in particular
  no Mathlib), so that `lake build` works offline on a bare Lean toolchain.
  Everything the formalizations need beyond Lean core is defined here:

    * `OrdField K` — a minimal strictly-ordered-field interface.  Every
      analytic statement in this project is proved from this interface alone,
      so it holds in every model of the interface; the statements in the
      papers are the instance `K = ℝ`.
    * ordered-field algebra: cancellation, sign lemmas, monotonicity of `+`
      and `*`, subtraction and division, monotone division by a positive.
    * `lsum` / `sumRange` — finite sums over lists and initial segments of
      ℕ (`Nat`), including the telescoping identity used by the
      forecast-ladder bounds.
    * `dotp` / `vadd` / `vscale` / `linComb` — list-based linear algebra with
      the dot-product linearity workhorses, and `farkas_sound`: the sound
      direction of Farkas' lemma (a nonnegative row combination yielding the
      zero row and a negative right-hand side certifies infeasibility).
      This is the logical core of the LP-based obstruction and certification
      theorems in the papers.
    * `IsMax` — an attainment predicate for maxima of finite lists (maxima
      are carried as hypotheses rather than constructed, keeping the layer
      choice-free).
    * `FinMass` — finitely-supported mass functions over an abstract ordered
      field, with expectation `E` and event probability `Prb` (events are
      Bool-valued characteristic functions, keeping everything decidable and
      core-only), with the functoriality, monotonicity, additivity and
      total-mass lemmas used by the belief-computation and probabilistic
      papers.

  Every declaration is proved from the interface fields; there are no `sorry`s
  and no additional axioms.
-/

namespace Formalizations

set_option linter.unusedSectionVars false

/-! ## A minimal strictly-ordered-field interface -/

/-- A minimal strictly-ordered-field interface: a total order `le`, field
operations, and the compatibility axioms actually consumed by the
formalizations.  All later theorems are interface-level: they hold in any
model, in particular over the reals. -/
class OrdField (K : Type) where
  /-- additive unit -/
  zero : K
  /-- multiplicative unit -/
  one : K
  add : K → K → K
  mul : K → K → K
  neg : K → K
  inv : K → K
  le : K → K → Prop
  add_assoc : ∀ a b c : K, add (add a b) c = add a (add b c)
  add_comm : ∀ a b : K, add a b = add b a
  zero_add : ∀ a : K, add zero a = a
  add_neg_cancel : ∀ a : K, add a (neg a) = zero
  mul_assoc : ∀ a b c : K, mul (mul a b) c = mul a (mul b c)
  mul_comm : ∀ a b : K, mul a b = mul b a
  one_mul : ∀ a : K, mul one a = a
  mul_inv_cancel : ∀ a : K, a ≠ zero → mul a (inv a) = one
  inv_zero : inv zero = zero
  zero_ne_one : zero ≠ one
  zero_le_one : le zero one
  left_distrib : ∀ a b c : K, mul a (add b c) = add (mul a b) (mul a c)
  le_refl : ∀ a : K, le a a
  le_trans : ∀ a b c : K, le a b → le b c → le a c
  le_antisymm : ∀ a b : K, le a b → le b a → a = b
  le_total : ∀ a b : K, le a b ∨ le b a
  add_le_add : ∀ a b c d : K, le a b → le c d → le (add a c) (add b d)
  mul_le_mul_of_nonneg' : ∀ {a b c : K}, le a b → le zero c → le (mul a c) (mul b c)

export OrdField (zero one add mul neg inv le)

instance [OrdField K] : Zero K := ⟨OrdField.zero⟩
instance [OrdField K] : One K := ⟨OrdField.one⟩
instance [OrdField K] : Add K := ⟨OrdField.add⟩
instance [OrdField K] : Mul K := ⟨OrdField.mul⟩
instance [OrdField K] : Neg K := ⟨OrdField.neg⟩
instance [OrdField K] : Inv K := ⟨OrdField.inv⟩
instance [OrdField K] : LE K := ⟨OrdField.le⟩
instance [OrdField K] : Sub K := ⟨fun a b => a + -b⟩
instance [OrdField K] : Div K := ⟨fun a b => a * b⁻¹⟩

/-- Strict order, defined from the non-strict one (irrefflexive by
`le_antisymm`). -/
def ltK [OrdField K] (a b : K) : Prop := a ≤ b ∧ ¬ b ≤ a

instance [OrdField K] : LT K := ⟨ltK⟩

/-! ## Notation-level restatements of the interface axioms

Class-field projections do not participate in `rw` matching against
notation-headed terms, so every field consumed by a later proof is
restated here with `+`, `*`, `≤` notation. -/

section FieldWrappers
variable [OrdField K] {a b c d : K}

theorem add_assoc (a b c : K) : a + b + c = a + (b + c) := OrdField.add_assoc a b c
theorem add_comm (a b : K) : a + b = b + a := OrdField.add_comm a b
@[simp] theorem zero_add (a : K) : 0 + a = a := OrdField.zero_add a
theorem add_neg_cancel (a : K) : a + -a = 0 := OrdField.add_neg_cancel a
theorem neg_add_cancel (a : K) : -a + a = 0 := by rw [add_comm, add_neg_cancel]
theorem mul_assoc (a b c : K) : a * b * c = a * (b * c) := OrdField.mul_assoc a b c
theorem mul_comm (a b : K) : a * b = b * a := OrdField.mul_comm a b
@[simp] theorem one_mul' (a : K) : 1 * a = a := OrdField.one_mul a
theorem mul_inv_cancel_field {a : K} (h : a ≠ 0) : a * a⁻¹ = 1 :=
  OrdField.mul_inv_cancel a h
theorem left_distrib (a b c : K) : a * (b + c) = a * b + a * c :=
  OrdField.left_distrib a b c
theorem add_le_add (h1 : a ≤ b) (h2 : c ≤ d) : a + c ≤ b + d :=
  OrdField.add_le_add a b c d h1 h2

end FieldWrappers

/-! ## Basic algebra -/

section Algebra
variable [OrdField K] {a b c d : K}

@[simp] theorem add_zero (a : K) : a + 0 = a := by
  rw [← add_comm, zero_add]

theorem add_left_cancel {a b c : K} (h : a + b = a + c) : b = c := by
  have h1 : -a + (a + b) = -a + (a + c) := by rw [h]
  rw [← add_assoc, ← add_assoc, neg_add_cancel, zero_add,
    zero_add] at h1
  exact h1

theorem add_right_cancel {a b c : K} (h : a + b = c + b) : a = c := by
  have h1 : a + b + -b = c + b + -b := by rw [h]
  rw [add_assoc, add_assoc, add_neg_cancel, add_zero, add_zero] at h1
  exact h1

theorem neg_neg (a : K) : -(-a) = a := by
  apply add_right_cancel (b := -a)
  rw [neg_add_cancel, add_neg_cancel]

@[simp] theorem mul_one (a : K) : a * 1 = a := by
  rw [mul_comm, one_mul']

theorem right_distrib (a b c : K) : (a + b) * c = a * c + b * c := by
  rw [mul_comm (a + b) c, left_distrib, mul_comm c a, mul_comm c b]

@[simp] theorem zero_mul (a : K) : 0 * a = 0 := by
  have h1 : (0 + 0) * a = 0 * a + 0 * a := right_distrib 0 0 a
  rw [zero_add] at h1
  have h2 : 0 * a + 0 = 0 * a + 0 * a := by
    rw [add_zero]
    exact h1
  exact (add_left_cancel h2).symm

@[simp] theorem mul_zero (a : K) : a * 0 = 0 := by
  rw [mul_comm, zero_mul]

@[simp] theorem sub_self (a : K) : a - a = 0 := add_neg_cancel a

theorem sub_eq (a b : K) : a - b = a + -b := rfl
theorem div_eq (a b : K) : a / b = a * b⁻¹ := rfl

theorem neg_zero : -(0 : K) = 0 := by
  have h : (0 : K) + -0 = 0 + 0 := by rw [add_neg_cancel, zero_add]
  exact add_left_cancel h

@[simp] theorem sub_zero (a : K) : a - 0 = a := by rw [sub_eq, neg_zero, add_zero]
@[simp] theorem zero_sub (a : K) : 0 - a = -a := zero_add (-a)

theorem neg_eq_of_add_eq_zero_right {a b : K} (h : a + b = 0) : a = -b := by
  apply add_right_cancel (b := b)
  rw [neg_add_cancel]
  exact h

theorem neg_mul (a b : K) : -(a * b) = (-a) * b := by
  have h2 : (-a) * b + a * b = (-a + a) * b := by rw [← right_distrib]
  rw [neg_add_cancel, zero_mul] at h2
  exact (neg_eq_of_add_eq_zero_right h2).symm

theorem mul_neg (a b : K) : -(a * b) = a * (-b) := by
  have h2 : a * (-b) + a * b = a * (-b + b) := by rw [← left_distrib]
  rw [neg_add_cancel, mul_zero] at h2
  exact (neg_eq_of_add_eq_zero_right h2).symm

theorem neg_mul_neg (a b : K) : (-a) * (-b) = a * b := by
  rw [← neg_mul, ← mul_neg, neg_neg]

theorem mul_sub (a b c : K) : a * (b - c) = a * b - a * c := by
  rw [sub_eq b c, left_distrib, ← mul_neg a c, sub_eq (a * b) (a * c)]

theorem sub_mul (a b c : K) : (a - b) * c = a * c - b * c := by
  rw [sub_eq a b, right_distrib, sub_eq (a * c) (b * c), ← neg_mul b c]

theorem sub_add_cancel (a b : K) : a - b + b = a := by
  rw [sub_eq, add_assoc, neg_add_cancel, add_zero]

theorem add_sub_cancel (a b : K) : a + b - b = a := by
  rw [sub_eq, add_assoc, add_neg_cancel, add_zero]

theorem add_right_comm (a b c : K) : a + b + c = a + c + b := by
  rw [add_assoc, add_comm b c, ← add_assoc]

theorem add_comm4 (a b c d : K) : a + b + (c + d) = a + c + (b + d) := by
  rw [← add_assoc, ← add_assoc, add_right_comm a b c]

end Algebra

/-! ## Order basics -/

section Order
variable [OrdField K] {a b c : K}

theorem le_refl (a : K) : a ≤ a := OrdField.le_refl a

theorem le_trans (h1 : a ≤ b) (h2 : b ≤ c) : a ≤ c := OrdField.le_trans a b c h1 h2

theorem le_antisymm (h1 : a ≤ b) (h2 : b ≤ a) : a = b := OrdField.le_antisymm a b h1 h2

theorem le_total (a b : K) : a ≤ b ∨ b ≤ a := OrdField.le_total a b

theorem le_of_eq (h : a = b) : a ≤ b := by
  rw [← h]
  exact le_refl a

theorem lt_iff_le_not_le (a b : K) : a < b ↔ (a ≤ b ∧ ¬ b ≤ a) := Iff.rfl

theorem not_le_of_lt (h : a < b) : ¬ b ≤ a := h.2

theorem le_of_not_le (h : ¬ a ≤ b) : b < a :=
  ⟨(le_total a b).elim (fun hba => absurd hba h) (fun hba => hba), h⟩

theorem lt_irrefl (a : K) : ¬ a < a := fun h => h.2 (le_refl a)

theorem ne_of_lt (h : a < b) : a ≠ b := fun hab => h.2 (by rw [hab]; exact le_refl b)

theorem ne_of_gt (h : a < b) : b ≠ a := (ne_of_lt h).symm

theorem lt_of_le_of_ne (h1 : a ≤ b) (h2 : a ≠ b) : a < b :=
  ⟨h1, fun hba => h2 (le_antisymm h1 hba)⟩

theorem lt_of_lt_of_le (h1 : a < b) (h2 : b ≤ c) : a < c :=
  ⟨le_trans h1.1 h2, fun hc => h1.2 (le_trans h2 hc)⟩

theorem lt_of_le_of_lt (h1 : a ≤ b) (h2 : b < c) : a < c :=
  ⟨le_trans h1 h2.1, fun hc => h2.2 (le_trans hc h1)⟩

theorem lt_trans (h1 : a < b) (h2 : b < c) : a < c := lt_of_lt_of_le h1 h2.1

theorem le_of_lt (h : a < b) : a ≤ b := h.1

theorem zero_le_one' : (0 : K) ≤ 1 := OrdField.zero_le_one

theorem zero_ne_one' : (0 : K) ≠ 1 := OrdField.zero_ne_one

theorem zero_lt_one : (0 : K) < 1 :=
  ⟨OrdField.zero_le_one, fun h => OrdField.zero_ne_one
    (le_antisymm h OrdField.zero_le_one).symm⟩

theorem add_le_add_left (h : c ≤ d) (a : K) : a + c ≤ a + d :=
  add_le_add (le_refl a) h

theorem add_le_add_right (h : a ≤ b) (c : K) : a + c ≤ b + c :=
  add_le_add h (le_refl c)

theorem add_le_add_of_nonneg (h1 : 0 ≤ a) (h2 : 0 ≤ b) : 0 ≤ a + b := by
  have h := add_le_add h1 h2
  rw [zero_add] at h
  exact h

theorem neg_le_neg (h : a ≤ b) : -b ≤ -a := by
  have h1 : a + -b ≤ 0 := by
    have h2 : a + -b ≤ b + -b := add_le_add_right h (-b)
    rw [add_neg_cancel] at h2
    exact h2
  have h2 : -b + a ≤ 0 := by rw [add_comm (-b) a]; exact h1
  have h3 : -b + a + -a ≤ 0 + -a := add_le_add_right h2 (-a)
  rw [add_assoc, add_neg_cancel, add_zero, zero_add] at h3
  exact h3

end Order

/-! ## Signs and monotonicity of multiplication -/

section Mul
variable [OrdField K] {a b c : K}

theorem mul_le_mul_of_nonneg_right (h : a ≤ b) (hc : 0 ≤ c) : a * c ≤ b * c :=
  OrdField.mul_le_mul_of_nonneg' h hc

theorem mul_le_mul_of_nonneg_left (h : a ≤ b) (hc : 0 ≤ c) : c * a ≤ c * b := by
  rw [mul_comm c a, mul_comm c b]
  exact mul_le_mul_of_nonneg_right h hc

theorem mul_nonneg (ha : 0 ≤ a) (hb : 0 ≤ b) : 0 ≤ a * b := by
  have h : (0 : K) * b ≤ a * b := mul_le_mul_of_nonneg_right ha hb
  rwa [zero_mul] at h

theorem eq_zero_or_eq_zero_of_mul_eq_zero (h : a * b = 0) : a = 0 ∨ b = 0 := by
  by_cases ha : a = 0
  · exact Or.inl ha
  · refine Or.inr ?_
    have h1 : a⁻¹ * a = 1 := by
      rw [mul_comm a⁻¹ a]; exact OrdField.mul_inv_cancel a ha
    calc b = 1 * b := (one_mul' b).symm
      _ = (a⁻¹ * a) * b := by rw [h1, one_mul']
      _ = a⁻¹ * (a * b) := mul_assoc a⁻¹ a b
      _ = a⁻¹ * 0 := by rw [h]
      _ = 0 := mul_zero _

theorem mul_pos (ha : 0 < a) (hb : 0 < b) : 0 < a * b := by
  refine ⟨mul_nonneg ha.1 hb.1, ?_⟩
  intro h0
  cases eq_zero_or_eq_zero_of_mul_eq_zero (le_antisymm h0 (mul_nonneg ha.1 hb.1)) with
  | inl h => exact ha.2 (by rw [h]; exact le_refl 0)
  | inr h => exact hb.2 (by rw [h]; exact le_refl 0)

theorem nonneg_of_mul_nonneg_of_pos (h : 0 ≤ a * b) (hb : 0 < b) : 0 ≤ a := by
  by_cases ha : 0 ≤ a
  · exact ha
  · exfalso
    have ha0 : a ≤ 0 := (le_total a 0).elim (fun h' => h') (fun h' => absurd h' ha)
    have h1 : a * b ≤ 0 * b := mul_le_mul_of_nonneg_right ha0 hb.1
    rw [zero_mul] at h1
    cases eq_zero_or_eq_zero_of_mul_eq_zero (le_antisymm h1 h) with
    | inl h2 => exact ha (by rw [h2]; exact le_refl 0)
    | inr h2 => exact hb.2 (le_of_eq h2)

theorem mul_left_cancel {a b c : K} (ha : a ≠ 0) (h : a * b = a * c) : b = c := by
  have h1 : a⁻¹ * (a * b) = a⁻¹ * (a * c) := by rw [h]
  rw [← mul_assoc a⁻¹ a b, ← mul_assoc a⁻¹ a c, mul_comm a⁻¹ a,
    mul_inv_cancel_field ha, one_mul', one_mul'] at h1
  exact h1

theorem mul_inv_cancel' {b : K} (hb : b ≠ 0) : b⁻¹ * b = 1 := by
  rw [mul_comm b⁻¹ b]; exact OrdField.mul_inv_cancel b hb

theorem inv_pos (h : 0 < a) : 0 < a⁻¹ := by
  have han : a ≠ 0 := by
    intro ha0
    apply h.2
    rw [ha0]
    exact le_refl 0
  refine ⟨?_, fun h0 => ?_⟩
  · have h1 : 0 ≤ a⁻¹ * a := by
      rw [mul_inv_cancel' han]
      exact OrdField.zero_le_one
    exact nonneg_of_mul_nonneg_of_pos h1 h
  · have h2 : a * a⁻¹ ≤ a * 0 := mul_le_mul_of_nonneg_left h0 h.1
    rw [mul_zero, mul_inv_cancel_field han] at h2
    exact zero_ne_one' (le_antisymm h2 OrdField.zero_le_one).symm

end Mul

/-! ## Subtraction and division -/

section SubDiv
variable [OrdField K] {a b c : K}

theorem sub_nonneg : 0 ≤ b - a ↔ a ≤ b := by
  constructor
  · intro h
    have h1 : a + 0 ≤ a + (b - a) := add_le_add_left h a
    rw [add_zero, sub_eq, ← add_assoc, add_comm a b, add_assoc,
      add_neg_cancel, add_zero] at h1
    exact h1
  · intro h
    have h1 : a + -a ≤ b + -a := add_le_add_right h (-a)
    rw [add_neg_cancel, ← sub_eq b a] at h1
    exact h1

theorem div_mul_cancel {b : K} (hb : b ≠ 0) (a : K) : (a / b) * b = a := by
  rw [div_eq, mul_assoc, mul_inv_cancel' hb, mul_one]

theorem sub_div (a b c : K) : (a - b) / c = a / c - b / c := by
  rw [div_eq (a - b) c, div_eq a c, div_eq b c, sub_mul]

theorem div_pos (ha : 0 < a) (hb : 0 < b) : 0 < a / b := mul_pos ha (inv_pos hb)

theorem div_le_div_right {b : K} (hb : 0 < b) (h : a ≤ c) : a / b ≤ c / b := by
  have hca : 0 ≤ c - a := sub_nonneg.mpr h
  have h1 : ((c - a) / b) * b = c - a :=
    div_mul_cancel (ne_of_gt hb) (c - a)
  have hnb : 0 ≤ (c - a) / b := by
    have h2 : 0 ≤ ((c - a) / b) * b := by rw [h1]; exact hca
    exact nonneg_of_mul_nonneg_of_pos h2 hb
  rw [sub_div] at hnb
  exact sub_nonneg.mp hnb

end SubDiv

/-! ## Finite sums over lists -/

section Sums
variable [OrdField K] {α : Type}

def lsum : List K → K
  | [] => 0
  | x :: xs => x + lsum xs

@[simp] theorem lsum_nil : lsum ([] : List K) = 0 := rfl
@[simp] theorem lsum_cons (x : K) (xs : List K) : lsum (x :: xs) = x + lsum xs := rfl

theorem lsum_append (xs ys : List K) : lsum (xs ++ ys) = lsum xs + lsum ys := by
  induction xs with
  | nil => rw [List.nil_append, lsum_nil, zero_add]
  | cons x xs ih => rw [List.cons_append, lsum_cons, lsum_cons, ih, ← add_assoc]

theorem map_congr' {l : List α} {f g : α → K} (h : ∀ a, a ∈ l → f a = g a) :
    l.map f = l.map g := by
  induction l with
  | nil => rfl
  | cons x xs ih =>
      rw [List.map_cons, List.map_cons, h x (by simp),
        ih (fun a ha => h a (by simp [ha]))]

theorem lsum_congr (l : List α) (f g : α → K) (h : ∀ a, a ∈ l → f a = g a) :
    lsum (l.map f) = lsum (l.map g) := by
  rw [map_congr' h]

theorem lsum_le_lsum (l : List α) (f g : α → K) (h : ∀ a, a ∈ l → f a ≤ g a) :
    lsum (l.map f) ≤ lsum (l.map g) := by
  induction l with
  | nil => exact le_refl 0
  | cons x xs ih =>
      rw [List.map_cons, List.map_cons, lsum_cons, lsum_cons]
      exact add_le_add (h x (by simp)) (ih (fun a ha => h a (by simp [ha])))

theorem lsum_nonneg (l : List K) (h : ∀ x, x ∈ l → 0 ≤ x) : 0 ≤ lsum l := by
  induction l with
  | nil => exact le_refl 0
  | cons x xs ih =>
      rw [lsum_cons]
      exact add_le_add_of_nonneg (h x (by simp)) (ih (fun y hy => h y (by simp [hy])))

theorem lsum_nonneg_map (l : List α) (f : α → K) (hf : ∀ a, 0 ≤ f a) :
    0 ≤ lsum (l.map f) := by
  induction l with
  | nil => exact le_refl 0
  | cons x xs ih =>
      rw [List.map_cons, lsum_cons]
      exact add_le_add_of_nonneg (hf x) ih

theorem lsum_distrib (l : List α) (f g : α → K) :
    lsum (l.map (fun a => f a + g a)) = lsum (l.map f) + lsum (l.map g) := by
  induction l with
  | nil => exact (zero_add (0 : K)).symm
  | cons x xs ih =>
      rw [List.map_cons, List.map_cons, List.map_cons, lsum_cons, lsum_cons,
        lsum_cons, ih, add_comm4 (f x) (g x) (lsum (xs.map f)) (lsum (xs.map g))]

theorem lsum_const_mul (l : List α) (c : K) (f : α → K) :
    lsum (l.map (fun a => c * f a)) = c * lsum (l.map f) := by
  induction l with
  | nil => exact (mul_zero c).symm
  | cons x xs ih =>
      rw [List.map_cons, List.map_cons, lsum_cons, lsum_cons, ih, ← left_distrib]

/-- A filtered sum never exceeds the full sum when the summands are
nonnegative. -/
theorem lsum_filter_le (f : α → K) (hf : ∀ a, 0 ≤ f a) (l : List α) (p : α → Bool) :
    lsum ((l.filter p).map f) ≤ lsum (l.map f) := by
  induction l with
  | nil => exact le_refl 0
  | cons x xs ih =>
      by_cases hp : p x = true
      · have h1 : (x :: xs).filter p = x :: xs.filter p := by simp [List.filter, hp]
        rw [h1, List.map_cons, List.map_cons, lsum_cons, lsum_cons]
        exact add_le_add (le_refl (f x)) ih
      · have h1 : (x :: xs).filter p = xs.filter p := by simp [List.filter, hp]
        rw [h1, List.map_cons, lsum_cons]
        have hfx : 0 ≤ f x := hf x
        have hR : lsum (xs.map f) ≤ f x + lsum (xs.map f) :=
          le_trans (le_of_eq (zero_add (lsum (xs.map f))).symm)
            (add_le_add_right hfx (lsum (xs.map f)))
        exact le_trans ih hR

theorem lsum_filter_ind (A : α → Bool) (mass : α → K) :
    ∀ l : List α, lsum (l.map (fun a => if A a then mass a else 0))
      = lsum ((l.filter A).map mass) := by
  intro l
  induction l with
  | nil => rfl
  | cons a as ih =>
      cases hA : A a with
      | true =>
          have hf : (a :: as).filter A = a :: as.filter A := by simp [List.filter, hA]
          have hite : (if A a then mass a else 0) = mass a := by rw [hA]; rfl
          rw [hf, List.map_cons, List.map_cons, lsum_cons, lsum_cons, ih, hite]
      | false =>
          have hf : (a :: as).filter A = as.filter A := by simp [List.filter, hA]
          have hite : (if A a then mass a else 0) = 0 := by rw [hA]; rfl
          rw [hf, List.map_cons, lsum_cons, ih, hite, zero_add]

theorem lsum_filter_split (A : α → Bool) (mass : α → K) :
    ∀ l : List α, lsum ((l.filter A).map mass)
        + lsum ((l.filter (fun a => !A a)).map mass) = lsum (l.map mass) := by
  intro l
  induction l with
  | nil => exact zero_add (0 : K)
  | cons a as ih =>
      cases hA : A a with
      | true =>
          have hf1 : (a :: as).filter A = a :: as.filter A := by simp [List.filter, hA]
          have hf2 : (a :: as).filter (fun a => !A a) = as.filter (fun a => !A a) := by
            simp [List.filter, hA]
          rw [hf1, hf2, List.map_cons, lsum_cons, List.map_cons, lsum_cons,
            add_assoc, ih]
      | false =>
          have hf1 : (a :: as).filter A = as.filter A := by simp [List.filter, hA]
          have hf2 : (a :: as).filter (fun a => !A a)
              = a :: as.filter (fun a => !A a) := by simp [List.filter, hA]
          rw [hf1, hf2, List.map_cons, lsum_cons, List.map_cons, lsum_cons,
            ← add_assoc, add_right_comm, ih,
            add_comm (lsum (as.map mass)) (mass a)]

/-! ## Finite sums over initial segments of ℕ -/

def sumRange (f : Nat → K) : Nat → K
  | 0 => 0
  | n + 1 => sumRange f n + f n

@[simp] theorem sumRange_zero (f : Nat → K) : sumRange f 0 = 0 := rfl
@[simp] theorem sumRange_succ (f : Nat → K) (n : Nat) :
    sumRange f (n + 1) = sumRange f n + f n := rfl

theorem sumRange_le_sumRange' (f g : Nat → K) :
    ∀ n, (∀ i, i < n → f i ≤ g i) → sumRange f n ≤ sumRange g n := by
  intro n
  induction n with
  | zero => intro _; exact le_refl 0
  | succ m ih =>
      intro h
      rw [sumRange_succ, sumRange_succ]
      exact add_le_add (ih (fun i hi => h i (by omega))) (h m (by omega))

theorem sumRange_nonneg' (f : Nat → K) (hf : ∀ i, 0 ≤ f i) : ∀ n, 0 ≤ sumRange f n := by
  intro n
  induction n with
  | zero => exact le_refl 0
  | succ m ih => rw [sumRange_succ]; exact add_le_add_of_nonneg ih (hf m)

theorem sumRange_add (f g : Nat → K) (n : Nat) :
    sumRange (fun i => f i + g i) n = sumRange f n + sumRange g n := by
  induction n with
  | zero => exact (zero_add (0 : K)).symm
  | succ m ih =>
      rw [sumRange_succ, sumRange_succ, sumRange_succ, ih,
        add_comm4 (sumRange f m) (sumRange g m) (f m) (g m)]

/-- Telescoping identity for forward differences. -/
theorem sumRange_telescope (f : Nat → K) (n : Nat) :
    sumRange (fun i => f i - f (i + 1)) n = f 0 - f n := by
  induction n with
  | zero => exact (sub_self (f 0)).symm
  | succ m ih =>
      rw [sumRange_succ, ih]
      calc (f 0 - f m) + (f m - f (m + 1))
          = (f 0 + -f m) + (f m + -f (m + 1)) := by
              rw [sub_eq (f 0) (f m), sub_eq (f m) (f (m + 1))]
        _ = f 0 + (-f m + (f m + -f (m + 1))) := by rw [add_assoc]
        _ = f 0 + ((-f m + f m) + -f (m + 1)) := by
              rw [← add_assoc (-f m) (f m) (-f (m + 1))]
        _ = f 0 + (0 + -f (m + 1)) := by rw [neg_add_cancel (f m)]
        _ = f 0 + -f (m + 1) := by rw [zero_add]
        _ = f 0 - f (m + 1) := (sub_eq (f 0) (f (m + 1))).symm

end Sums

/-! ## List-based linear algebra and Farkas certificate soundness -/

section Linear
variable [OrdField K]

/-- Pointwise vector addition (identity on the empty arguments). -/
def vadd : List K → List K → List K
  | [], w => w
  | v, [] => v
  | a :: as, b :: bs => (a + b) :: vadd as bs

/-- Pointwise scaling. -/
def vscale (c : K) : List K → List K
  | [] => []
  | x :: xs => (c * x) :: vscale c xs

/-- Dot product (truncating at the shorter argument). -/
def dotp : List K → List K → K
  | [], _ => 0
  | _, [] => 0
  | a :: as, b :: bs => a * b + dotp as bs

@[simp] theorem vadd_nil_left (w : List K) : vadd [] w = w := rfl
@[simp] theorem vadd_nil_right (v : List K) : vadd v [] = v := by
  cases v with
  | nil => rfl
  | cons x xs => rfl
@[simp] theorem vadd_cons (a b : K) (as bs : List K) :
    vadd (a :: as) (b :: bs) = (a + b) :: vadd as bs := rfl

@[simp] theorem vscale_nil (c : K) : vscale c [] = [] := rfl
@[simp] theorem vscale_cons (c : K) (x : K) (xs : List K) :
    vscale c (x :: xs) = (c * x) :: vscale c xs := rfl

@[simp] theorem dotp_nil_left (v : List K) : dotp [] v = 0 := rfl
@[simp] theorem dotp_nil_right (v : List K) : dotp v [] = 0 := by
  cases v with
  | nil => rfl
  | cons x xs => rfl
@[simp] theorem dotp_cons (a b : K) (as bs : List K) :
    dotp (a :: as) (b :: bs) = a * b + dotp as bs := rfl

theorem dotp_vscale (c : K) :
    ∀ (v x : List K), dotp (vscale c v) x = c * dotp v x := by
  intro v
  induction v with
  | nil => intro x; simp
  | cons a as ih =>
      intro x
      cases x with
      | nil => simp
      | cons b bs =>
          rw [vscale_cons, dotp_cons, dotp_cons, ih bs, mul_assoc, ← left_distrib]

theorem dotp_vadd :
    ∀ (v w x : List K), v.length = x.length → w.length = x.length →
      dotp (vadd v w) x = dotp v x + dotp w x := by
  intro v
  induction v with
  | nil =>
      intro w x hv hw
      cases x with
      | nil => cases w <;> simp
      | cons c cs =>
          simp only [List.length_nil, List.length_cons] at hv
          omega
  | cons a as ih =>
      intro w x hv hw
      cases w with
      | nil =>
          cases x with
          | nil =>
              simp only [List.length_nil, List.length_cons] at hv
              omega
          | cons c cs => simp
      | cons b bs =>
          cases x with
          | nil =>
              simp only [List.length_nil, List.length_cons] at hv
              omega
          | cons c cs =>
              simp only [List.length_cons] at hv hw
              rw [vadd_cons, dotp_cons, dotp_cons, dotp_cons,
                ih bs cs (by omega) (by omega), right_distrib,
                add_comm4 (a * c) (b * c) (dotp as cs) (dotp bs cs)]

theorem length_vadd_eq :
    ∀ (v w : List K) (L : Nat), v.length = L → w.length = L → (vadd v w).length = L := by
  intro v
  induction v with
  | nil =>
      intro w L hv hw
      simp only [List.length_nil] at hv
      subst hv
      rw [vadd_nil_left]
      exact hw
  | cons a as ih =>
      intro w L hv hw
      cases w with
      | nil =>
          simp only [List.length_nil] at hw
          simp only [List.length_cons] at hv
          omega
      | cons b bs =>
          simp only [List.length_cons] at hv hw
          have h1 := ih bs as.length (by omega) (by omega)
          rw [vadd_cons, List.length_cons]
          omega

theorem length_vscale (c : K) (v : List K) : (vscale c v).length = v.length := by
  induction v with
  | nil => rfl
  | cons x xs ih => rw [vscale_cons, List.length_cons, List.length_cons, ih]

/-- Running linear combination of the vectors `a 0, …, a (n-1)` with weights
`lam 0, …, lam (n-1)`, seeded at `init`. -/
def linComb (init : List K) (lam : Nat → K) (a : Nat → List K) : Nat → List K
  | 0 => init
  | n + 1 => vadd (linComb init lam a n) (vscale (lam n) (a n))

theorem linComb_zero (init : List K) (lam : Nat → K) (a : Nat → List K) :
    linComb init lam a 0 = init := rfl
theorem linComb_succ (init : List K) (lam : Nat → K) (a : Nat → List K) (n : Nat) :
    linComb init lam a (n + 1) = vadd (linComb init lam a n) (vscale (lam n) (a n)) := rfl

theorem length_linComb_eq (lam : Nat → K) (a : Nat → List K) (L : Nat) :
    ∀ n, (∀ i, i < n → (a i).length = L) →
      (linComb (List.replicate L 0) lam a n).length = L := by
  intro n
  induction n with
  | zero => intro _; rw [linComb_zero, List.length_replicate]
  | succ m ih =>
      intro hlen
      rw [linComb_succ]
      exact length_vadd_eq _ _ L (ih (fun i hi => hlen i (by omega)))
        (by rw [length_vscale]; exact hlen m (by omega))

theorem dotp_replicate_zero (x : List K) :
    dotp (List.replicate x.length 0) x = 0 := by
  induction x with
  | nil => rfl
  | cons c cs ih =>
      rw [List.length_cons, List.replicate_succ, dotp_cons, zero_mul, zero_add, ih]

theorem dotp_linComb (lam : Nat → K) (a : Nat → List K) (x : List K) :
    ∀ n, (∀ i, i < n → (a i).length = x.length) →
      dotp (linComb (List.replicate x.length 0) lam a n) x
        = sumRange (fun i => lam i * dotp (a i) x) n := by
  intro n
  induction n with
  | zero => intro _; rw [linComb_zero, sumRange_zero]; exact dotp_replicate_zero x
  | succ m ih =>
      intro hlen
      have hlenm : ∀ i, i < m → (a i).length = x.length := fun i hi => hlen i (by omega)
      have hl1 : (linComb (List.replicate x.length 0) lam a m).length = x.length :=
        length_linComb_eq lam a x.length m hlenm
      have hl2 : (vscale (lam m) (a m)).length = x.length := by
        rw [length_vscale]; exact hlen m (by omega)
      rw [linComb_succ, dotp_vadd _ _ _ hl1 hl2, ih hlenm, dotp_vscale, sumRange_succ]

/-- **Farkas certificate soundness** (the sound direction of Farkas' lemma,
over an abstract strictly-ordered field).

If nonnegative multipliers `lam i` combine the rows `a i` into the zero row
while their combination of the right-hand sides `b i` is strictly negative,
then the constraint system `dotp (a i) x ≤ b i` (for `i < n`) is
infeasible: no `x` satisfies it.

This is the logical core of the LP-based obstruction certificates (the Farkas
dual as obstruction witness) and of the computational certification
framework. -/
theorem farkas_sound (a : Nat → List K) (b : Nat → K) (lam : Nat → K) (x : List K)
    (n : Nat)
    (hlen : ∀ i, i < n → (a i).length = x.length)
    (hnonneg : ∀ i, i < n → 0 ≤ lam i)
    (hzero : linComb (List.replicate x.length 0) lam a n = List.replicate x.length 0)
    (hneg : sumRange (fun i => lam i * b i) n < 0) :
    ¬ (∀ i, i < n → dotp (a i) x ≤ b i) := by
  intro hsat
  have h0 : dotp (List.replicate x.length 0) x = 0 := dotp_replicate_zero x
  rw [← hzero, dotp_linComb lam a x n hlen] at h0
  have hle : sumRange (fun i => lam i * dotp (a i) x) n
      ≤ sumRange (fun i => lam i * b i) n :=
    sumRange_le_sumRange' _ _ n
      (fun i hi => mul_le_mul_of_nonneg_left (hsat i hi) (hnonneg i hi))
  rw [h0] at hle
  exact hneg.2 hle

end Linear

/-! ## Maxima of finite lists (attainment carried as hypotheses) -/

section IsMax
variable [OrdField K]

/-- `IsMax m l`: `m` is attained as a maximum of the finite list `l`. -/
def IsMax (m : K) (l : List K) : Prop := m ∈ l ∧ ∀ y, y ∈ l → y ≤ m

theorem IsMax.le {m b : K} {l : List K} (h : IsMax m l) (hb : ∀ y, y ∈ l → y ≤ b) :
    m ≤ b := hb m h.1

theorem IsMax.ge {m x : K} {l : List K} (h : IsMax m l) (hx : x ∈ l) : x ≤ m := h.2 x hx

theorem IsMax.unique {m m' : K} {l : List K} (h : IsMax m l) (h' : IsMax m' l) :
    m = m' := le_antisymm (h.le h'.2) (h'.le h.2)

end IsMax

/-! ## Finitely supported mass functions, expectation, and probability -/

variable [OrdField K] {α : Type}

/-- List-level distinctness (core-only substitute for `List.Nodup`). -/
def NoDup : List α → Prop
  | [] => True
  | a :: as => ¬ a ∈ as ∧ NoDup as

/-- A finitely-supported mass function: nonnegative masses, mass `1` in
total over the (duplicate-free) support, and zero off the support. -/
structure FinMass (K : Type) [OrdField K] (α : Type) where
  /-- enumeration of the support -/
  support : List α
  /-- the support list is duplicate-free -/
  no_dup : NoDup support
  /-- the mass function -/
  mass : α → K
  /-- masses are nonnegative -/
  nonneg : ∀ a, 0 ≤ mass a
  /-- total mass is one -/
  total : lsum (support.map mass) = 1
  /-- mass vanishes off the support -/
  zero_off : ∀ a, ¬ a ∈ support → mass a = 0

/-- Zero-one indicator of a Bool-valued event. -/
def ind (A : α → Bool) (a : α) : K :=
  if A a then 1 else 0

namespace FinMass

/-- Expectation of `f` under the mass function `m`. -/
def E (m : FinMass K α) (f : α → K) : K :=
  lsum (m.support.map (fun a => m.mass a * f a))

theorem E_congr (m : FinMass K α) (f g : α → K) (h : ∀ a, a ∈ m.support → f a = g a) :
    m.E f = m.E g :=
  lsum_congr m.support (fun a => m.mass a * f a) (fun a => m.mass a * g a)
    (fun a ha => by rw [h a ha])

theorem E_le_E (m : FinMass K α) (f g : α → K) (h : ∀ a, a ∈ m.support → f a ≤ g a) :
    m.E f ≤ m.E g :=
  lsum_le_lsum m.support (fun a => m.mass a * f a) (fun a => m.mass a * g a)
    (fun a ha => mul_le_mul_of_nonneg_left (h a ha) (m.nonneg a))

theorem E_nonneg (m : FinMass K α) (f : α → K) (hf : ∀ a, 0 ≤ f a) : 0 ≤ m.E f :=
  lsum_nonneg_map m.support (fun a => m.mass a * f a)
    (fun a => mul_nonneg (m.nonneg a) (hf a))

theorem E_add (m : FinMass K α) (f g : α → K) :
    m.E (fun a => f a + g a) = m.E f + m.E g := by
  show lsum (m.support.map (fun a => m.mass a * (f a + g a)))
      = lsum (m.support.map (fun a => m.mass a * f a))
        + lsum (m.support.map (fun a => m.mass a * g a))
  rw [lsum_congr m.support (fun a => m.mass a * (f a + g a))
    (fun a => m.mass a * f a + m.mass a * g a)
    (fun a _ => left_distrib (m.mass a) (f a) (g a))]
  exact lsum_distrib m.support (fun a => m.mass a * f a) (fun a => m.mass a * g a)

theorem E_smul (m : FinMass K α) (c : K) (f : α → K) :
    m.E (fun a => c * f a) = c * m.E f := by
  show lsum (m.support.map (fun a => m.mass a * (c * f a)))
      = c * lsum (m.support.map (fun a => m.mass a * f a))
  rw [lsum_congr m.support (fun a => m.mass a * (c * f a))
    (fun a => c * (m.mass a * f a))
    (fun a _ => by rw [← mul_assoc, mul_comm (m.mass a) c, mul_assoc])]
  exact lsum_const_mul m.support c (fun a => m.mass a * f a)

theorem E_one (m : FinMass K α) : m.E (fun _ => 1) = 1 := by
  show lsum (m.support.map (fun a => m.mass a * 1)) = 1
  rw [show (fun a => m.mass a * 1) = m.mass from funext (fun a => mul_one (m.mass a))]
  exact m.total

theorem E_const (m : FinMass K α) (c : K) : m.E (fun _ => c) = c := by
  have h1 : (fun a => m.mass a * c) = (fun a => c * m.mass a) :=
    funext (fun a => mul_comm (m.mass a) c)
  show lsum (m.support.map (fun a => m.mass a * c)) = c
  rw [h1, lsum_const_mul, m.total, mul_one]

/-- Probability of a Bool-valued event under `m`. -/
def Prb (m : FinMass K α) (A : α → Bool) : K :=
  lsum ((m.support.filter A).map m.mass)

theorem Prb_nonneg (m : FinMass K α) (A : α → Bool) : 0 ≤ m.Prb A := by
  show 0 ≤ lsum ((m.support.filter A).map m.mass)
  apply lsum_nonneg
  intro r hr
  cases List.mem_map.1 hr with
  | intro a h =>
      cases h with
      | intro _ heq => rw [← heq]; exact m.nonneg a

theorem Prb_le_one (m : FinMass K α) (A : α → Bool) : m.Prb A ≤ 1 := by
  have h := lsum_filter_le m.mass m.nonneg m.support A
  rw [m.total] at h
  exact h

theorem Prb_eq_E (m : FinMass K α) (A : α → Bool) :
    m.Prb A = m.E (fun a => ind A a) := by
  have h3 : (fun a => if A a then m.mass a else 0) = (fun a => m.mass a * ind A a) := by
    funext a
    unfold ind
    cases hA : A a with
    | true => exact (mul_one (m.mass a)).symm
    | false => exact (mul_zero (m.mass a)).symm
  show lsum ((m.support.filter A).map m.mass)
      = lsum (m.support.map (fun a => m.mass a * ind A a))
  rw [← lsum_filter_ind A m.mass m.support, h3]

theorem Prb_add_Prb_compl (m : FinMass K α) (A : α → Bool) :
    m.Prb A + m.Prb (fun a => !A a) = 1 := by
  have h := lsum_filter_split A m.mass m.support
  rw [m.total] at h
  exact h

end FinMass

end Formalizations

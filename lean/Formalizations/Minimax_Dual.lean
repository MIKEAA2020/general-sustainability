/-
  Formalizations.Minimax_Dual
  ===========================

  Lean formalization of the theorem layer of

    "Minimax Dual Certificates" (2026g; source of record:
    `minimax_dual_certificates_v7.tex`).

  Scope and fidelity.  The paper's headline equivalence (Theorem `thm:dual`)
  combines a certificate-soundness direction (an adversarial measure with
  uniformly negative expected drift certifies emptiness of the common
  safe-action set) with a converse obtained from Sion's minimax theorem over
  weak-* compact convex sets of measures — an analysis argument outside a
  dependency-free layer.  What is formalized here:

    * the certificate-soundness direction of Theorem `thm:dual` in full
      generality (any finitely-supported adversarial measure, any action
      space, over the abstract ordered field);
    * the convexity boundary (Proposition `prop:gap`) completely: the
      two-row parity instance with non-convex action set has an empty common
      safe-action set, yet *no* measure certifies — for every measure one of
      the two actions has nonnegative expected drift;
    * the recoveries (Proposition `prop:recover`): the ℓ₁-normalized two-row
      average identity of the polyhedral case, and the singleton case — the
      uniform measure makes the expected drift vanish identically, every
      measure leaves one action nonnegative, and the single-worst-disturbance
      reading (value 1 at the witnesses) is not the dual;
    * the benchmark obstruction algebra (Theorem `thm:benchmark`): given the
      cap sum below the demand floor, the (1/2, 1/2) measure on the two
      active-floor atoms drives the expected drift of every feasible harvest
      pair strictly negative.

  Not formalized (and why): the Sion converse and the Banach–Alaoglu
  compactness behind it; the Carathéodory/basic-solution sparsity bound of
  Proposition `prop:sparse`; the adversarial-prior envelope, its tower
  identity and refinement monotonicity (the dynamic layer, recorded as
  conjectural in the paper itself and verified instance-wise by the record's
  check families in exact rational arithmetic).  The numeric evaluations of
  the benchmark (cap sum 47/25 at Y = 6, critical aggregate 27/5, margin
  3/50) are carried as documented premises, certified by the record.
-/

import Formalizations.Prelude

namespace Formalizations.Minimax

/-! ## Field helpers -/

section Helpers
variable {K : Type} [OrdField K] {a b c : K}

theorem one_lt_two : (1 : K) < 1 + 1 :=
  lt_of_le_of_ne (by
    have h : (1 : K) + 0 ≤ 1 + 1 := add_le_add_left zero_le_one' 1
    rwa [add_zero] at h)
    (fun h => zero_ne_one' (add_left_cancel (by rw [add_zero (1 : K)]; exact h)))

theorem zero_lt_two : (0 : K) < 1 + 1 := lt_trans zero_lt_one one_lt_two

theorem half_pos : (0 : K) < 1 / (1 + 1) := div_pos zero_lt_one zero_lt_two

theorem half_add_half : (1 : K) / (1 + 1) + 1 / (1 + 1) = 1 := by
  have h1 : (1 : K) / (1 + 1) + 1 / (1 + 1) = (1 + 1) * (1 + 1)⁻¹ := by
    rw [div_eq, ← right_distrib]
  rw [h1, mul_inv_cancel_field (ne_of_gt zero_lt_two)]

theorem neg_of_pos (h : 0 < a) : -a < 0 :=
  lt_of_le_of_ne (by
    have h1 : -a ≤ -0 := neg_le_neg h.1
    rwa [neg_zero] at h1)
    (fun heq => h.2 (by rw [← neg_neg a, heq, neg_zero]; exact le_refl 0))

theorem neg_pos_of_neg (h : a < 0) : 0 < -a :=
  ⟨by
    have h1 : -0 ≤ -a := neg_le_neg h.1
    rwa [neg_zero] at h1,
  fun hn => h.2 (by
    have h1 : -0 ≤ -(-a) := neg_le_neg hn
    rw [neg_neg, neg_zero] at h1
    exact h1)⟩

theorem lt_of_neg_pos (h : 0 < -a) : a < 0 :=
  ⟨by
    have h1 : -(-a) ≤ -0 := neg_le_neg h.1
    rwa [neg_neg, neg_zero] at h1,
  fun hn => h.2 (by
    have h1 : -a ≤ -0 := neg_le_neg hn
    rwa [neg_zero] at h1)⟩

theorem neg_nonpos_of_nonpos (h : a ≤ 0) : 0 ≤ -a := by
  have h1 : -0 ≤ -a := neg_le_neg h
  rwa [neg_zero] at h1

theorem neg_add_dist (a b : K) : -a + -b = -(a + b) := by
  apply neg_eq_of_add_eq_zero_right
  rw [add_comm4 (-a) (-b) a b, neg_add_cancel, neg_add_cancel, add_zero]

theorem sub_le_sub (h : b ≤ c) (a : K) : a - c ≤ a - b := by
  have h1 : a + -c ≤ a + -b := add_le_add_left (neg_le_neg h) a
  rwa [← sub_eq a c, ← sub_eq a b] at h1

theorem sub_neg_of_lt (h : a < b) : a - b < 0 :=
  lt_of_le_of_ne (by
    have h1 : a + -b ≤ b + -b := add_le_add_right h.1 (-b)
    rw [add_neg_cancel] at h1
    exact h1)
    (fun heq => h.2 (by
      have h2 : a = (a - b) + b := (sub_add_cancel a b).symm
      rw [heq, zero_add] at h2
      rw [h2]
      exact le_refl b))

theorem not_zero_le_neg_one : ¬(0 : K) ≤ -(1 : K) := by
  intro h
  have h1 : -(-(1 : K)) ≤ -0 := neg_le_neg h
  rw [neg_neg, neg_zero] at h1
  exact zero_lt_one.2 h1

theorem half_mul_neg (h : a < 0) : (1 / (1 + 1)) * a < 0 :=
  lt_of_neg_pos (by rw [mul_neg]; exact mul_pos half_pos (neg_pos_of_neg h))

end Helpers

/-! ## The measure-dual certificate: soundness -/

/-- **Certificate soundness** (the load-bearing direction of the measure
dual).  If an adversarial measure `μ` on the active boundary–disturbance
bundle drives the expected inward drift below `-ε < 0` uniformly over the
control set, then the common safe-action set is empty: no single action has
nonnegative drift at every bundle point.

Paper reference: Theorem `thm:dual` (minimax dual certificate), the
"existence of a certificate ⇒ obstruction" direction. -/
theorem dual_certificate_sound {K : Type} [OrdField K] {T A : Type}
    (μ : FinMass K T) (ψ : T → A → K) (ε : K) (hε : 0 < ε)
    (hcert : ∀ a, μ.E (fun t => ψ t a) ≤ -ε) :
    ¬ ∃ a, ∀ t, 0 ≤ ψ t a := by
  intro hex
  cases hex with
  | intro a ha =>
      have hnn : 0 ≤ μ.E (fun t => ψ t a) := FinMass.E_nonneg μ _ (fun t => ha t)
      have hlt : μ.E (fun t => ψ t a) < 0 :=
        lt_of_le_of_lt (hcert a) (neg_of_pos hε)
      exact not_le_of_lt hlt hnn

/-! ## The convexity boundary (a complete counterexample) -/

/-- Sign encoding: `+1` for `true`, `-1` for `false`. -/
def b2k {K : Type} [OrdField K] : Bool → K
  | true => 1
  | false => -1

/-- The two-row parity instance of the convexity boundary: the drift of row
`t` under action `a` is the product of the signs. -/
def parityψ {K : Type} [OrdField K] (t a : Bool) : K := b2k t * b2k a

/-- On the parity instance the common safe-action set is empty: each action
meets a strictly negative row.

Paper reference: Proposition `prop:gap` (convexity boundary), first half. -/
theorem parity_common_safe_empty {K : Type} [OrdField K] :
    ¬ ∃ a, ∀ t, 0 ≤ parityψ (K := K) t a := by
  intro hex
  cases hex with
  | intro a ha =>
      cases a with
      | true =>
          have h := ha false
          simp only [parityψ, b2k] at h
          rw [mul_one] at h
          exact not_zero_le_neg_one h
      | false =>
          have h := ha true
          simp only [parityψ, b2k] at h
          rw [one_mul'] at h
          exact not_zero_le_neg_one h

/-- On the parity instance no adversarial measure certifies: for every
measure, one of the two actions has nonnegative expected drift.  The two
expected drifts are negatives of one another, so their maximum is always
nonnegative — the strict minimax gap.

Paper reference: Proposition `prop:gap` (convexity boundary), second half:
the common safe-action set is empty, yet no measure certifies. -/
theorem parity_no_measure_certifies {K : Type} [OrdField K] (μ : FinMass K Bool) :
    ∃ a, 0 ≤ μ.E (fun t => parityψ t a) := by
  have hsum : μ.E (fun t => parityψ t true) + μ.E (fun t => parityψ t false) = 0 := by
    rw [← FinMass.E_add μ (fun t => parityψ t true) (fun t => parityψ t false)]
    have h2 : (fun t => parityψ t true + parityψ t false) = (fun _ => (0 : K)) := by
      funext t
      cases t <;>
        simp [parityψ, b2k, mul_one, one_mul', neg_mul_neg,
          add_neg_cancel, neg_add_cancel]
    rw [h2]
    exact FinMass.E_const μ 0
  cases le_total (μ.E (fun t => parityψ t true)) 0 with
  | inl hn =>
      refine ⟨false, ?_⟩
      have hcom : μ.E (fun t => parityψ t false) + μ.E (fun t => parityψ t true) = 0 := by
        rw [add_comm]; exact hsum
      rw [neg_eq_of_add_eq_zero_right hcom]
      exact neg_nonpos_of_nonpos hn
  | inr hp => exact ⟨true, hp⟩

/-! ## The recoveries -/

/-- The polyhedral recovery: the `(1/2, 1/2)` average of the two floor-row
drifts eliminates the control variable — the ℓ₁-normalized Farkas pair with
constant expected drift.

Paper reference: Proposition `prop:recover` (i): on the two-floor instance
the measure `λ = (1/2, 1/2)` makes the expected drift *constant*; with
thresholds `2/5` and `3/5` the constant is `-1/10` (numeric evaluation
certified by the record). -/
theorem two_row_average {K : Type} [OrdField K] (r1 r2 u : K) :
    (1 / (1 + 1)) * ((r1 - u) + (u - r2)) = (r1 - r2) / (1 + 1) := by
  have hregroup : (r1 - u) + (u - r2) = r1 - r2 := by
    calc (r1 - u) + (u - r2) = (r1 + -u) + (u + -r2) := by
          rw [sub_eq, sub_eq]
      _ = r1 + (-u + (u + -r2)) := by rw [add_assoc]
      _ = r1 + ((-u + u) + -r2) := by rw [← add_assoc (-u) u (-r2)]
      _ = r1 + (0 + -r2) := by rw [neg_add_cancel]
      _ = r1 - r2 := by rw [zero_add, sub_eq]
  rw [hregroup, div_eq, div_eq, one_mul', mul_comm]

/-- The singleton case: drifts `1 - 2u` (row `d₁`) and `2u - 1` (row `d₂`),
written without numeral literals. -/
def ψsingle {K : Type} [OrdField K] (d : Bool) (u : K) : K :=
  if d then 1 - u - u else u + u - 1

/-- The uniform measure on the two disturbances. -/
def unifMass {K : Type} [OrdField K] : FinMass K Bool where
  support := [true, false]
  no_dup := ⟨by simp, ⟨by simp, trivial⟩⟩
  mass := fun _ => 1 / (1 + 1)
  nonneg := fun _ => (div_pos zero_lt_one zero_lt_two).1
  total := by
    show (1 / (1 + 1)) + ((1 / (1 + 1)) + 0) = 1
    rw [add_zero, half_add_half]
  zero_off := fun a h => by
    cases a <;> exact absurd (by simp) h

theorem ψsingle_sum {K : Type} [OrdField K] (u : K) :
    ψsingle true u + ψsingle false u = 0 := by
  show (1 - u - u) + (u + u - 1) = 0
  have h1 : (1 : K) - u - u = 1 - (u + u) := by
    rw [sub_eq, sub_eq, add_assoc, neg_add_dist, ← sub_eq (1 : K) (u + u)]
  rw [h1, sub_eq (u + u) 1, sub_eq (1 : K) (u + u),
    add_comm (u + u) (-1), add_comm4 1 (-(u + u)) (-1) (u + u),
    add_neg_cancel, neg_add_cancel, add_zero]

/-- The uniform measure makes the expected drift vanish identically in the
control — the adversarial *distribution* is load-bearing.

Paper reference: Proposition `prop:recover` (ii): on the exact convex
instance `max_u min_d ψ = min_μ max_u Φ = 0`. -/
theorem singleton_uniform {K : Type} [OrdField K] (u : K) :
    unifMass (K := K).E (fun d => ψsingle d u) = 0 := by
  show (1 / (1 + 1)) * ψsingle true u + ((1 / (1 + 1)) * ψsingle false u + 0) = 0
  rw [add_zero, ← left_distrib, ψsingle_sum, mul_zero]

/-- Every measure leaves one of the two actions nonnegative on the singleton
instance — the dual value is `0`, attained by the uniform measure.

Paper reference: Proposition `prop:recover` (ii), the every-measure side of
`min_μ max_u Φ = 0`. -/
theorem singleton_every_measure {K : Type} [OrdField K] (μ : FinMass K Bool) :
    0 ≤ μ.E (fun d => ψsingle d 0) ∨ 0 ≤ μ.E (fun d => ψsingle d 1) := by
  have hsum : μ.E (fun d => ψsingle d 0) + μ.E (fun d => ψsingle d 1) = 0 := by
    rw [← FinMass.E_add μ (fun d => ψsingle d 0) (fun d => ψsingle d 1)]
    have h2 : (fun d => ψsingle d 0 + ψsingle d 1) = (fun _ => (0 : K)) := by
      funext d
      cases d <;>
        simp [ψsingle, sub_self, sub_zero, zero_sub, add_sub_cancel,
          add_neg_cancel, neg_add_cancel, add_zero]
    rw [h2]
    exact FinMass.E_const μ 0
  cases le_total (μ.E (fun d => ψsingle d 0)) 0 with
  | inl hn =>
      refine Or.inr ?_
      have hcom : μ.E (fun d => ψsingle d 1) + μ.E (fun d => ψsingle d 0) = 0 := by
        rw [add_comm]; exact hsum
      rw [neg_eq_of_add_eq_zero_right hcom]
      exact neg_nonpos_of_nonpos hn
  | inr hp => exact Or.inl hp

/-- The single-worst-disturbance reading is not the dual: its witnesses
attain value `1`, not `0`.

Paper reference: Proposition `prop:recover` (ii): the single-worst reading
`min_d max_u ψ = 1` is *not* the dual value. -/
theorem singleton_worst_witnesses {K : Type} [OrdField K] :
    ψsingle (K := K) true 0 = 1 ∧ ψsingle (K := K) false 1 = 1 := by
  constructor
  · show 1 - 0 - 0 = 1
    rw [sub_zero, sub_zero]
  · show 1 + 1 - 1 = 1
    rw [add_sub_cancel]

/-! ## The benchmark obstruction algebra -/

/-- The certified obstruction at an aggregate with cap sum below the demand
floor: the `(1/2, 1/2)` measure on the two active-floor atoms drives the
expected drift of every feasible harvest pair strictly negative — the
measure-dual certificate of the benchmark.

Paper reference: Theorem `thm:benchmark`: at `Y = 6` the cap sum is
`47/25 < 2` and the certificate has margin `3/50` (numeric evaluations
certified by the record); the harvest caps are affine in `Y` with common
slope, the critical aggregate `27/5` solving the cap-sum equation exactly. -/
theorem benchmark_obstruction {K : Type} [OrdField K] (c1 c2 u1 u2 : K)
    (hcs : c1 + c2 < 1 + 1) (hu : 1 + 1 ≤ u1 + u2) :
    (1 / (1 + 1)) * ((c1 - u1) + (c2 - u2)) < 0 := by
  have hregroup : (c1 - u1) + (c2 - u2) = (c1 + c2) - (u1 + u2) := by
    rw [sub_eq, sub_eq, sub_eq, add_comm4 c1 (-u1) c2 (-u2),
      neg_add_dist u1 u2, ← sub_eq (c1 + c2) (u1 + u2)]
  rw [hregroup]
  apply half_mul_neg
  exact lt_of_le_of_lt (sub_le_sub hu (c1 + c2)) (sub_neg_of_lt hcs)

end Formalizations.Minimax

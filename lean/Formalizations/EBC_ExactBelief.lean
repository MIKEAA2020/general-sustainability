/-
  Formalizations.EBC_ExactBelief
  =============================

  Lean formalization of the theorem layer of

    "Exact Belief Computation" (2026f; source of record:
    `paper2_exact_belief_computation_v6.tex`).

  Scope and fidelity.  The paper classifies the four-parameter hidden-mode
  cube completely: every blind survivable set consists of Hamming-adjacent
  cells (a pairwise-Hamming pair-sum bound), no three cells are pairwise
  adjacent, the observation ladder doubles the conditional kernel mass per
  exact probe, and the alpha-set values are exact.  Formalized here:

    * the pair-sum bound, part (i) (Lemma `lem:pairsum`): for every action
      (including the hold action) and every two parameter cells, the sum of
      the two inner products is at most twice the agreement mass — the
      disagreements cancel termwise and the agreements contribute at most
      2 each; the hold action gives 0 for every pair;
    * the observation-ladder doubling (the abstract's ladder arithmetic):
      an exact-halving event makes the conditional mass exactly one half —
      each exact probe doubles the conditional kernel mass.

  Not formalized (and why): part (ii) of the pair-sum bound (the Cesàro
  survival-cost direction) requires the long-run-average limit structure;
  the adjacency-triangle exclusion requires parity machinery over counted
  lists; the maximal-band census and the alpha-set values are exact
  enumerations of the 256-cell instance, certified by the record's 25/25
  check families in integer and rational arithmetic.
-/

import Formalizations.Prelude

namespace Formalizations.EBC

/-! ## The action encoding and inner products -/

/-- The three actions per coordinate: `+1`, `-1`, and the hold `0`. -/
inductive Tri where
  | pos
  | neg
  | hold

/-- The ±1/0 encoding of an action coordinate. -/
def b1t {K : Type} [OrdField K] : Tri → K
  | Tri.pos => 1
  | Tri.neg => -(1 : K)
  | Tri.hold => 0

/-- The ±1 encoding of a parameter coordinate. -/
def b1 {K : Type} [OrdField K] : Bool → K
  | true => 1
  | false => -(1 : K)

/-- The inner product of an action vector with a parameter cell over an
index list. -/
def ipi {K : Type} [OrdField K] (I : List Nat) (u : Nat → Tri)
    (θ : Nat → Bool) : K :=
  lsum (I.map (fun i => b1t (u i) * b1 (θ i)))

/-- The agreement mass of two cells over an index list: `1` per agreeing
coordinate. -/
def agreeMass {K : Type} [OrdField K] (I : List Nat)
    (θ θ' : Nat → Bool) : K :=
  lsum (I.map (fun i => if θ i = θ' i then (1 : K) else 0))

theorem neg_one_le_one {K : Type} [OrdField K] : -(1 : K) ≤ 1 :=
  le_trans (by
    have h : -(1 : K) ≤ -0 := neg_le_neg zero_le_one'
    rwa [neg_zero] at h) zero_le_one'

theorem neg_one_pair_le {K : Type} [OrdField K] :
    (-(1 : K)) + (-(1 : K)) ≤ 1 + 1 :=
  add_le_add neg_one_le_one neg_one_le_one

theorem zero_le_two' {K : Type} [OrdField K] : (0 : K) ≤ 1 + 1 := by
  have h : (0 : K) + 0 ≤ 1 + 1 := add_le_add zero_le_one' zero_le_one'
  rwa [zero_add] at h

/-- **Coordinate bound.**  Per coordinate, the sum of the action's two
inner products with the two cells is at most twice the agreement
indicator: agreements contribute at most 2, disagreements cancel exactly,
and the hold action contributes nothing. -/
theorem coord_bound {K : Type} [OrdField K] (u : Tri) (t t' : Bool) :
    b1t u * b1 t + b1t u * b1 t'
      ≤ ((1 : K) + 1) * (if t = t' then (1 : K) else 0) := by
  cases t <;> cases t' <;> cases u <;>
    simp [b1t, b1, mul_one, one_mul', mul_neg, neg_mul, neg_mul_neg,
      mul_zero, add_neg_cancel, neg_add_cancel, zero_add, add_zero,
      neg_one_pair_le, zero_le_one', zero_le_two', le_refl]

/-! ## The pair-sum bound, part (i) -/

/-- **Pair-sum bound (i).**  For every action `u` and every two parameter
cells `θ, θ'` over the index list `I`, the sum of the two inner products
is at most twice the agreement mass.

Paper reference: Lemma `lem:pairsum` (pair-sum bound and its survival
cost), part (i). -/
theorem pair_sum_bound {K : Type} [OrdField K] (I : List Nat)
    (u : Nat → Tri) (θ θ' : Nat → Bool) :
    ipi I u θ + ipi I u θ' ≤ ((1 : K) + 1) * agreeMass I θ θ' := by
  unfold ipi agreeMass
  rw [← lsum_distrib I (fun i => b1t (u i) * b1 (θ i))
      (fun i => b1t (u i) * b1 (θ' i)),
    ← lsum_const_mul]
  exact lsum_le_lsum I _ _ (fun i _ => coord_bound (u i) (θ i) (θ' i))

/-- **The hold action gives zero.**  The hold action has zero inner
product against every cell.

Paper reference: Lemma `lem:pairsum`, the hold-action clause of (i). -/
theorem hold_action_zero {K : Type} [OrdField K] (I : List Nat)
    (θ : Nat → Bool) :
    ipi I (fun _ => Tri.hold) θ = (0 : K) := by
  induction I with
  | nil => rfl
  | cons i Is ih =>
      have h1 : ipi (i :: Is) (fun _ => Tri.hold) θ
          = (0 : K) * b1 (θ i) + ipi Is (fun _ => Tri.hold) θ := rfl
      rw [h1, ih, zero_mul, add_zero]

/-! ## The observation-ladder doubling -/

theorem one_lt_two' {K : Type} [OrdField K] : (1 : K) < 1 + 1 := by
  refine lt_of_le_of_ne ?_ ?_
  · have h : (1 : K) + 0 ≤ 1 + 1 := add_le_add_left zero_le_one' 1
    rwa [add_zero] at h
  · intro heq
    exact zero_ne_one' (add_left_cancel (by rw [add_zero (1 : K)]; exact heq))

/-- **Exact-halving doubles the conditional mass.**  If an event `A` has
exactly twice the mass of a sub-event `B`, then the conditional mass of
`B` given `A` is exactly one half — each exact probe of the ladder halves
the ambient mass, i.e. doubles the conditional kernel mass.

Paper reference: the abstract's observation ladder
`1/16 → 1/8 → 1/4 → 1/2 → 1`. -/
theorem div_mul_self_right {K : Type} [OrdField K] {c x : K}
    (hx : x ≠ 0) (hc : c ≠ 0) : x / (c * x) = 1 / c := by
  have hcx : c * x ≠ 0 := by
    intro h0
    cases eq_zero_or_eq_zero_of_mul_eq_zero h0 with
    | inl h1 => exact hc h1
    | inr h2 => exact hx h2
  apply mul_left_cancel (a := c * x) hcx
  calc c * x * (x / (c * x)) = x := by
        rw [mul_comm (c * x) (x / (c * x)), div_mul_cancel hcx x]
    _ = c * x * (1 / c) := by
        rw [mul_assoc, mul_comm x (1 / c), ← mul_assoc, div_eq (1 : K) c,
          one_mul', mul_inv_cancel_field hc, one_mul']

/-- **Exact-halving doubles the conditional mass.**  If an event `A` has
exactly twice the mass of a sub-event `B`, then the conditional mass of
`B` given `A` is exactly one half — each exact probe of the ladder halves
the ambient mass, i.e. doubles the conditional kernel mass.

Paper reference: the abstract's observation ladder
`1/16 → 1/8 → 1/4 → 1/2 → 1`. -/
theorem ladder_doubling {K : Type} [OrdField K] {Ω : Type}
    (m : FinMass K Ω) (A B : Ω → Bool)
    (h2 : m.Prb A = ((1 : K) + 1) * m.Prb B) (hpos : (0 : K) < m.Prb A) :
    m.Prb B / m.Prb A = (1 : K) / ((1 : K) + 1) := by
  have hB : m.Prb B ≠ (0 : K) := by
    intro h0
    apply hpos.2
    rw [h2, h0, mul_zero]
    exact le_refl (0 : K)
  have htwo : (1 : K) + 1 ≠ 0 := by
    intro h0
    apply (one_lt_two' (K := K)).2
    rw [h0]
    exact zero_le_one'
  rw [h2]
  exact div_mul_self_right hB htwo

end Formalizations.EBC

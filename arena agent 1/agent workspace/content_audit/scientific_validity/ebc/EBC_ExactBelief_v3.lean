/-
  Formalizations.EBC_ExactBelief_v3
  =================================

  **`lem:triangle` — no adjacency triangles — and the Hamming machinery
  behind it.**

  Item (2) of four. `paper2_exact_belief_computation_v10.tex` has eight
  numbered results; v16 formalized **one** (`lem:pairsum` (i)). This module
  adds the second, and it is the one that is *self-contained*: it needs
  neither the drift dynamics nor a limit, so it is the cheapest of the
  remaining four and the only one with no dependency on anything not
  already in the layer.

  The paper (l.150–161):

      "No three distinct cells of `{+1,-1}^m` (any `m`) are pairwise at
       Hamming distance `1`. Hence every blind survivable set at `m = 4`
       has at most two members, under every blind policy — any period,
       and no period at all."

      Proof: "Flip coordinates so that the first cell is `1` … A second
       cell at distance `1` is `1` with exactly one coordinate `i`
       flipped. A third distinct cell at distance `1` from `1` is `1`
       with exactly one coordinate `j` flipped: if `j = i` it is the
       second cell, and if `j ≠ i` the two differ from each other in the
       two coordinates `i, j`, so their Hamming distance is `2`.  No
       triangle exists. (Equivalently: the hypercube is bipartite by
       coordinate parity, so it has no odd cycle.)"

  The formalization follows the parity reading, proved coordinatewise
  rather than by constructing a bipartition: at each coordinate the three
  pairwise "differ" indicators are either all `0` (all three cells agree
  there) or exactly two `1`s (one cell differs from the other two), and
  that invariant is preserved by the induction down the index list. Both
  of the paper's cases fall out: `j = i` gives distance `0`, `j ≠ i`
  gives distance `2`.

  Cells are modelled as `Nat → Bool` over an index list `I`, matching the
  existing module's `θ : Nat → Bool` and its `agreeMass`/`ipi`. `hamming`
  is defined by recursion on `I` rather than by filtering, so that its
  structural lemmas need no `List.filter` bookkeeping.

  **Not done here** (and why): `cor:hamming` needs `lem:pairsum` (ii),
  which is a `liminf` of Cesàro averages; the paper's own remark — "for a
  periodic policy the average is the exact cycle average and no `liminf`
  is needed" — gives a finite form, but that needs the drift dynamics
  (`d(u,θ) = -1/2 + (1/5)⟨u,θ⟩`) modelled, which is a separate module.
  `prop:ladder` depends on `prop:bands`, and `prop:deadline` on the
  delayed-instance dynamics; both are queued behind that.
-/

import Formalizations.Prelude
import Formalizations.EBC_ExactBelief_v2

namespace Formalizations.EBC

/-! ## Hamming distance over an index list -/

/-- The number of coordinates in `I` on which the two cells differ. -/
def hamming : List Nat → (Nat → Bool) → (Nat → Bool) → Nat
  | [], _, _ => 0
  | i :: Is, θ, θ' => (if θ i = θ' i then 0 else 1) + hamming Is θ θ'

/-- **Distance zero is coordinatewise agreement.** -/
theorem hamming_eq_zero : ∀ (I : List Nat) (θ θ' : Nat → Bool),
    hamming I θ θ' = 0 ↔ ∀ i, i ∈ I → θ i = θ' i := by
  intro I
  induction I with
  | nil =>
      intro θ θ'
      simp [hamming]
  | cons i Is ih =>
      intro θ θ'
      by_cases h : θ i = θ' i
      · simp [hamming, h, ih]
      · simp [hamming, h, ih]

/-- A witness of disagreement forces positive distance. -/
theorem hamming_ne_zero_exists : ∀ (I : List Nat) (θ θ' : Nat → Bool),
    hamming I θ θ' ≠ 0 → ∃ i, i ∈ I ∧ θ i ≠ θ' i := by
  intro I
  induction I with
  | nil =>
      intro θ θ' h
      simp [hamming] at h
  | cons i Is ih =>
      intro θ θ' h
      by_cases heq : θ i = θ' i
      · simp [hamming, heq] at h
        rcases ih θ θ' h with ⟨j, hj, hne⟩
        exact ⟨j, by simp [hj], hne⟩
      · exact ⟨i, by simp, heq⟩

/-- Agreement everywhere gives distance zero — the direction the triangle
proof uses. -/
theorem hamming_zero_of_agree (I : List Nat) (θ θ' : Nat → Bool)
    (h : ∀ i, i ∈ I → θ i = θ' i) : hamming I θ θ' = 0 :=
  (hamming_eq_zero I θ θ').mpr h

/-! ## `lem:triangle` -/

/-- **No three cells are pairwise at Hamming distance `1`.**

Stated as: if `θ₁` is at distance `1` from `θ₂` and from `θ₃`, then
`θ₂` and `θ₃` are *not* at distance `1` — they are at distance `0`
(the paper's `j = i`, i.e. the "third cell" is the second) or at
distance `≥ 2` (the paper's `j ≠ i`). No limit, no dynamics, any `m`. -/
theorem no_adjacency_triangle : ∀ (I : List Nat) (θ₁ θ₂ θ₃ : Nat → Bool),
    hamming I θ₁ θ₂ = 1 → hamming I θ₁ θ₃ = 1 → hamming I θ₂ θ₃ ≠ 1 := by
  intro I
  induction I with
  | nil =>
      intro θ₁ θ₂ θ₃ h12 h13
      simp [hamming] at h12
  | cons i Is ih =>
      intro θ₁ θ₂ θ₃ h12 h13 h23
      let d12 : Nat := if θ₁ i = θ₂ i then 0 else 1
      let d13 : Nat := if θ₁ i = θ₃ i then 0 else 1
      let d23 : Nat := if θ₂ i = θ₃ i then 0 else 1
      have e12 : d12 + hamming Is θ₁ θ₂ = 1 := by
        change (if θ₁ i = θ₂ i then 0 else 1) + hamming Is θ₁ θ₂ = 1
        simpa [hamming] using h12
      have e13 : d13 + hamming Is θ₁ θ₃ = 1 := by
        change (if θ₁ i = θ₃ i then 0 else 1) + hamming Is θ₁ θ₃ = 1
        simpa [hamming] using h13
      have e23 : d23 + hamming Is θ₂ θ₃ = 1 := by
        change (if θ₂ i = θ₃ i then 0 else 1) + hamming Is θ₂ θ₃ = 1
        simpa [hamming] using h23
      by_cases h12i : θ₁ i = θ₂ i
      · by_cases h13i : θ₁ i = θ₃ i
        · -- all three agree at `i`: the head contributes nothing anywhere
          have hd12 : d12 = 0 := by simp [d12, h12i]
          have hd13 : d13 = 0 := by simp [d13, h13i]
          have h23i : θ₂ i = θ₃ i := h12i.symm.trans h13i
          have hd23 : d23 = 0 := by simp [d23, h23i]
          have t12 : hamming Is θ₁ θ₂ = 1 := by omega
          have t13 : hamming Is θ₁ θ₃ = 1 := by omega
          have t23 : hamming Is θ₂ θ₃ = 1 := by omega
          exact ih θ₁ θ₂ θ₃ t12 t13 t23
        · -- `θ₃` is the odd one out at `i`, and agrees with `θ₁` on the tail
          have hd12 : d12 = 0 := by simp [d12, h12i]
          have hd13 : d13 = 1 := by simp [d13, h13i]
          have hd23 : d23 = 1 := by
            simp [d23]
            intro h
            exact h13i (h12i.trans h)
          have t12 : hamming Is θ₁ θ₂ = 1 := by omega
          have t13 : hamming Is θ₁ θ₃ = 0 := by omega
          have t23 : hamming Is θ₂ θ₃ = 0 := by omega
          rcases hamming_ne_zero_exists Is θ₁ θ₂ (by omega) with ⟨j, hj, hne12⟩
          have h13j : θ₁ j = θ₃ j := (hamming_eq_zero Is θ₁ θ₃).mp t13 j hj
          have hne23 : θ₂ j ≠ θ₃ j := by
            intro h
            exact hne12 (h13j.trans h.symm)
          have h23j : θ₂ j = θ₃ j := (hamming_eq_zero Is θ₂ θ₃).mp t23 j hj
          exact hne23 h23j
      · by_cases h13i : θ₁ i = θ₃ i
        · -- `θ₂` is the odd one out at `i`, and agrees with `θ₁` on the tail
          have hd12 : d12 = 1 := by simp [d12, h12i]
          have hd13 : d13 = 0 := by simp [d13, h13i]
          have hd23 : d23 = 1 := by
            simp [d23]
            intro h
            exact h12i (h13i.trans h.symm)
          have t12 : hamming Is θ₁ θ₂ = 0 := by omega
          have t13 : hamming Is θ₁ θ₃ = 1 := by omega
          have t23 : hamming Is θ₂ θ₃ = 0 := by omega
          rcases hamming_ne_zero_exists Is θ₁ θ₃ (by omega) with ⟨j, hj, hne13⟩
          have h12j : θ₁ j = θ₂ j := (hamming_eq_zero Is θ₁ θ₂).mp t12 j hj
          have hne23 : θ₂ j ≠ θ₃ j := by
            intro h
            exact hne13 (h12j.trans h)
          have h23j : θ₂ j = θ₃ j := (hamming_eq_zero Is θ₂ θ₃).mp t23 j hj
          exact hne23 h23j
        · -- `θ₁` is the odd one out: `θ₂,θ₃` agree at `i` and on the tail
          have hd12 : d12 = 1 := by simp [d12, h12i]
          have hd13 : d13 = 1 := by simp [d13, h13i]
          have hd23 : d23 = 0 := by
            simp [d23]
            cases h1 : θ₁ i <;> cases h2 : θ₂ i <;> cases h3 : θ₃ i <;>
              simp [h1, h2, h3] at h12i h13i ⊢
          have t12 : hamming Is θ₁ θ₂ = 0 := by omega
          have t13 : hamming Is θ₁ θ₃ = 0 := by omega
          have t23 : hamming Is θ₂ θ₃ = 1 := by omega
          have t23z : hamming Is θ₂ θ₃ = 0 := by
            apply hamming_zero_of_agree
            intro j hj
            exact ((hamming_eq_zero Is θ₁ θ₂).mp t12 j hj).symm.trans
              ((hamming_eq_zero Is θ₁ θ₃).mp t13 j hj)
          omega

/-- **The paper's consequence**, in the form it is used: a blind survivable
set at any `m` has no three pairwise-adjacent members. Stated as the
contradiction `no_adjacency_triangle` produces, for the record. -/
theorem no_three_pairwise_adjacent (I : List Nat) (θ₁ θ₂ θ₃ : Nat → Bool)
    (h12 : hamming I θ₁ θ₂ = 1) (h13 : hamming I θ₁ θ₃ = 1)
    (h23 : hamming I θ₂ θ₃ = 1) : False :=
  no_adjacency_triangle I θ₁ θ₂ θ₃ h12 h13 h23

end Formalizations.EBC

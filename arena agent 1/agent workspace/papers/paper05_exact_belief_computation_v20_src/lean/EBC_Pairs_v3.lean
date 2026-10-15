/-
  Formalizations.EBC_Pairs_v3
  ===========================

  **`prop:bands`, necessity: from `z₀ < 1.1` no in-alphabet action keeps
  a Hamming-adjacent pair above the floor.**

  `EBC_Pairs_v2` proved the pair survives from `1.1`. This module proves
  it does not survive from below `1.1`, which is what makes `1.1` a
  *threshold* rather than a sufficient level. The paper's argument is
  about the first step, and it is: from `z₀ < 1.1` every admissible
  first action drops at least one member of the pair below the floor
  immediately, so no repair is possible — the floor binds at every step.

  The arithmetic behind it: to keep a cell at or above `1` from
  `z₀ < 1.1` an action must give it drift `> −1/10`, and

      d(matched ψ, θ) = −1/2 + (1/5)·(4 − 2h) > −1/10  ⟺  h = 0,

  where `h = hamming(ψ, θ)`. So survival of the first step forces
  `hamming(ψ, θ) = 0` *and* `hamming(ψ, θ′) = 0` — impossible for a cell
  action `ψ` when `θ ≠ θ′`. Both members cannot be served.

  Contents:

  * `eq_of_mul_eq_mul_pos` — cancel a positive factor from an equality.
    (General; belongs in `RatArith`, and can move there unchanged.)
  * `fifth_pos`, `tenth_le_half` — the order facts the layer was missing.
  * `half_fifth_two_eq_neg_tenth` — `−1/2 + (1/5)·2 = −1/10`.
  * `ipi_cell_le_two` — a cell action at Hamming distance `≥ 1` scores
    at most `2`.
  * **`drift_cell_le_neg_tenth`** — such an action drifts by at most
    `−1/10`.
  * **`step_fails_cell`**, **`step_fails_hold`** — one step from
    `z < 1.1` drops the cell below the floor, for cell actions and for
    the all-hold respectively.
  * **`pair_first_step_fails`** — the necessity clause, over
    `inAlphabet`.

  **Why the alphabet restriction is load-bearing here.** It is not
  needed for sufficiency (`EBC_Pairs_v2`), where the witness uses only
  cell actions. It is essential here: a *partial* hold — hold at exactly
  the coordinate where the pair differs, match everywhere else — scores
  `3`, drifts `+1/10`, and rescues the pair from `z₀ = 1.0`. That action
  is outside `inAlphabet`, and the paper's verification alphabet excludes
  it. See the header of `EBC_Pairs`.
-/

import Formalizations.Prelude
import Formalizations.EBC_ExactBelief_v2
import Formalizations.EBC_ExactBelief_v3
import Formalizations.EBC_Dynamics
import Formalizations.EBC_Hamming
import Formalizations.EBC_Bands
import Formalizations.EBC_Bands_v2
import Formalizations.EBC_Pairs
import Formalizations.EBC_Pairs_v2
import Formalizations.RatArith

open Formalizations.EBC

namespace Formalizations.EBC

variable {K : Type} [OrdField K]

/-! ## Cancelling a positive factor -/

/-- Strict addition on the right, which the layer does not name: from
`a < b`, `a + c < b + c` by `≤` plus disequality (an equality would
cancel to `a = b`). -/
theorem add_lt_add_right' {a b : K} (h : a < b) (c : K) : a + c < b + c := by
  have hle : a + c ≤ b + c := add_le_add_right (le_of_lt h) c
  have hne : a + c ≠ b + c := by
    intro heq
    exact (ne_of_lt h) (add_right_cancel heq)
  exact lt_of_le_of_ne hle hne

/-- **Cancel a positive factor from an equality**: `c·a = c·b` and
`0 < c` give `a = b`. Both directions go through
`le_of_mul_le_mul_pos`, so no division is involved.

General-purpose; it belongs in `RatArith` and can move there unchanged. -/
theorem eq_of_mul_eq_mul_pos {a b c : K} (h : c * a = c * b) (hc : (0 : K) < c) :
    a = b :=
  le_antisymm
    (le_of_mul_le_mul_pos (le_of_eq h) hc)
    (le_of_mul_le_mul_pos (le_of_eq h.symm) hc)

/-! ## Order facts for the small rationals -/

/-- `1/5 > 0`, from `5 · (1/5) = 1` and `5 > 0`. -/
theorem fifth_pos : (0 : K) < fifth := by
  apply pos_of_mul_pos_left' (c := five (K := K))
  · rw [five_mul_fifth]
    exact zero_lt_one
  · exact five_pos

/-- **`1/10 ≤ 1/2`**, by clearing denominators: scaled by `20` this is
`2 ≤ 10`. Only the non-strict form is needed — the strictness in the
argument below comes from `z < 1.1`, not from this comparison. -/
theorem tenth_le_half : tenth (K := K) ≤ half := by
  apply le_of_mul_le_mul_pos (c := natToK (K := K) 20)
  · have ht : natToK (K := K) 20 * tenth = natToK (K := K) 2 := by
      change natToK (K := K) 20 *
          ((1 : K) / natToK (K := K) 10) = natToK (K := K) 2
      rw [show natToK (K := K) 20 = natToK (K := K) (2 * 10) by congr 1]
      exact natToK_mul_inv_cancel 2 10 (by decide)
    have hh : natToK (K := K) 20 * half = natToK (K := K) 10 := by
      change natToK (K := K) 20 *
          ((1 : K) / natToK (K := K) 2) = natToK (K := K) 10
      rw [show natToK (K := K) 20 = natToK (K := K) (10 * 2) by congr 1]
      exact natToK_mul_inv_cancel 10 2 (by decide)
    rw [ht, hh]
    exact natToK_mono (by decide : 2 ≤ 10)
  · exact natToK_pos (by decide : 0 < 20)

/-- **`−1/2 + (1/5)·2 = −1/10`** — the mismatched drift, unscaled.

Obtained from the scaled form: `10·(−1/2 + (1/5)·2) = −1` is read off a
concrete instance of `mismatch_scale_m4` (a 4-dimensional index set with
two cells differing in one coordinate), and `10·(−1/10) = −1` is
`natToK_mul_inv`; then cancel the `10`. -/
theorem half_fifth_two_eq_neg_tenth :
    -half (K := K) + fifth * two = -tenth (K := K) := by
  have hL : ten (K := K) * (-half (K := K) + fifth * two) = -(1 : K) := by
    let I0 : List Nat := [0, 1, 2, 3]
    let θ0 : Nat → Bool := fun _ => true
    let θ1 : Nat → Bool := fun i => decide (i ≠ 0)
    have hlen : I0.length = 4 := by rfl
    have hadj : hamming I0 θ0 θ1 = 1 := by decide
    have hipi : ipi (K := K) I0 (matched θ1) θ0 = two (K := K) :=
      ipi_mismatched_m4_adj (K := K) I0 θ0 θ1 hlen hadj
    simpa [drift, hipi] using (mismatch_scale_m4 (K := K) I0 θ0 θ1 hlen hadj)
  have hR : ten (K := K) * (-tenth (K := K)) = -(1 : K) := by
    rw [← mul_neg]
    change -(ten (K := K) * ((1 : K) / ten (K := K))) = -(1 : K)
    rw [show ten (K := K) * ((1 : K) / ten (K := K)) = (1 : K) by
          change natToK (K := K) 10 *
              ((1 : K) / natToK (K := K) 10) = (1 : K)
          exact natToK_mul_inv 10 (by decide)]
  exact eq_of_mul_eq_mul_pos (by rw [hL, hR]) ten_pos

/-! ## A cell action at distance `≥ 1` drifts by at most `−1/10` -/

/-- A cell action at Hamming distance `≥ 1` from the cell scores at most
`2`: the inner product is `4 − 2h`, and `h ≥ 1`. -/
theorem ipi_cell_le_two (I : List Nat) (ψ θ : Nat → Bool)
    (hlen : I.length = 4) (hh : 1 ≤ hamming I ψ θ) :
    ipi I (matched ψ) θ ≤ two (K := K) := by
  have H := ipi_mismatched (K := K) I θ ψ
  rw [hamming_comm I θ ψ] at H
  rw [hlen] at H
  have htwo_le : two (K := K) ≤ two * natToK (K := K) (hamming I ψ θ) := by
    have h1le : natToK (K := K) 1 ≤ natToK (K := K) (hamming I ψ θ) :=
      natToK_mono hh
    have := mul_le_mul_of_nonneg_left h1le (le_of_lt two_pos)
    simpa [natToK] using this
  have h4 : natToK (K := K) 4 = two (K := K) + two (K := K) := by
    change natToK (K := K) 4 = natToK (K := K) 2 + natToK (K := K) 2
    rw [← natToK_add]
  have hle : ipi I (matched ψ) θ + two (K := K) ≤
      two (K := K) + two (K := K) := by
    calc
      ipi I (matched ψ) θ + two (K := K)
          ≤ ipi I (matched ψ) θ + two * natToK (K := K) (hamming I ψ θ) :=
              add_le_add_left htwo_le _
      _ = natToK (K := K) 4 := H
      _ = two (K := K) + two (K := K) := h4
  apply le_of_add_le_add_left (a := two (K := K))
  simpa [add_comm] using hle

/-- **A cell action at Hamming distance `≥ 1` drifts by at most
`−1/10`.** This is the engine of the necessity argument. -/
theorem drift_cell_le_neg_tenth (I : List Nat) (ψ θ : Nat → Bool)
    (hlen : I.length = 4) (hh : 1 ≤ hamming I ψ θ) :
    drift I (matched ψ) θ ≤ -tenth (K := K) := by
  rw [drift]
  have hmul : fifth * ipi I (matched ψ) θ ≤ fifth * two :=
    mul_le_mul_of_nonneg_left (ipi_cell_le_two I ψ θ hlen hh) (le_of_lt (fifth_pos (K := K)))
  exact le_trans (add_le_add_left hmul (-half (K := K)))
    (le_of_eq (half_fifth_two_eq_neg_tenth (K := K)))

/-! ## One step from below `1.1` -/

/-- **A cell action at distance `≥ 1` drops the cell below the floor in
one step**, whenever `z < 1.1`. -/
theorem step_fails_cell (I : List Nat) (ψ θ : Nat → Bool)
    (hlen : I.length = 4) (hh : 1 ≤ hamming I ψ θ)
    {z : K} (hz : z < one_one) :
    ¬ (1 : K) ≤ z + drift I (matched ψ) θ := by
  intro hsurv
  have hd := drift_cell_le_neg_tenth (K := K) I ψ θ hlen hh
  have hzle : z + drift I (matched ψ) θ ≤ z + (-tenth (K := K)) :=
    add_le_add_left hd z
  have hzlt : z + (-tenth (K := K)) < (1 : K) := by
    have hs := add_lt_add_right' hz (-tenth (K := K))
    have h_eq : one_one + (-tenth (K := K)) = (1 : K) := by
      change ((1 : K) + tenth) + (-(tenth (K := K))) = (1 : K)
      rw [add_assoc]
      have hz0 : tenth (K := K) + (-(tenth (K := K))) = 0 := by
        rw [← sub_eq, sub_self]
      rw [hz0]
      simp
    rwa [h_eq] at hs
  exact (lt_of_le_of_lt hzle hzlt).2 hsurv

/-- **The all-hold scores zero** against every cell: every coordinate
contributes `b1t(hold)·b1(±1) = 0`. -/
theorem ipi_hold_zero (I : List Nat) (u : Nat → Tri) (θ : Nat → Bool)
    (hh : isFullHold u) : ipi I u θ = (0 : K) := by
  induction I with
  | nil => simp [ipi]
  | cons i Is ih =>
      calc
        ipi (i :: Is) u θ = (b1t (u i) * b1 (θ i)) + ipi Is u θ := by
            simp [ipi, lsum_cons]
        _ = (0 : K) + ipi Is u θ := by
            rw [hh i]
            simp [b1t]
        _ = (0 : K) := by
            rw [ih]
            simp

/-- **The all-hold drops the cell below the floor in one step**, whenever
`z < 1.1`: it scores `0`, so it drifts `−1/2`, and `1.1 − 1/2 ≤ 1`. -/
theorem step_fails_hold (I : List Nat) (u : Nat → Tri) (θ : Nat → Bool)
    (hh : isFullHold u) {z : K} (hz : z < one_one) :
    ¬ (1 : K) ≤ z + drift I u θ := by
  intro hsurv
  have hzero : ipi I u θ = (0 : K) := ipi_hold_zero I u θ hh
  have hle : one_one (K := K) + (-half (K := K)) ≤ (1 : K) := by
    change ((1 : K) + tenth (K := K)) + (-half (K := K)) ≤ (1 : K)
    have ht : tenth (K := K) + (-half (K := K)) ≤ 0 := by
      have := add_le_add_right (tenth_le_half (K := K)) (-half (K := K))
      have hz0 : half (K := K) + (-half (K := K)) = 0 := by
        rw [← sub_eq, sub_self]
      rwa [hz0] at this
    calc
      ((1 : K) + tenth) + (-half (K := K))
          = (1 : K) + (tenth (K := K) + (-half (K := K))) := by rw [add_assoc]
      _ ≤ (1 : K) + 0 := add_le_add_left ht (1 : K)
      _ = (1 : K) := by simp
  have hslt : z + drift I u θ < (1 : K) := by
    rw [drift, hzero]
    simp only [mul_zero, add_zero]
    have hs := add_lt_add_right' hz (-half (K := K))
    exact lt_of_lt_of_le hs hle
  exact hslt.2 hsurv

/-- **The necessity clause.** From `z₀ < 1.1`, no action in the paper's
alphabet keeps both members of a Hamming-adjacent pair at or above the
floor for even one step.

Case split on the alphabet. A cell action `ψ` that serves `θ` must have
`hamming(ψ, θ) = 0`, and serving `θ′` likewise forces
`hamming(ψ, θ′) = 0`; by `hamming_eq_zero` that makes `θ = θ′` on `I`,
contradicting `hamming(θ, θ′) = 1`. The all-hold scores `0` and drifts
`−1/2`, which is worse than `−1/10`. -/
theorem pair_first_step_fails (I : List Nat) (θ θ' : Nat → Bool)
    (hlen : I.length = 4) (hadj : hamming I θ θ' = 1)
    (u : Nat → Tri) (hu : inAlphabet u) (z0 : K) (hz0 : z0 < one_one) :
    ¬ ((1 : K) ≤ z0 + drift I u θ ∧ (1 : K) ≤ z0 + drift I u θ') := by
  intro hboth
  cases hu with
  | inl hcell =>
      let ψ : Nat → Bool := fun i => match u i with | Tri.pos => true | _ => false
      have hum : u = matched ψ := by
        funext i
        have hn : u i ≠ Tri.hold := hcell i
        cases hui : u i <;> simp [matched, ψ, hui] at hn ⊢
      rw [hum] at hboth
      have h0 : hamming I ψ θ = 0 := by
        cases hham : hamming I ψ θ with
        | zero => rfl
        | succ k =>
            exact False.elim (step_fails_cell I ψ θ hlen
              (by rw [hham]; exact Nat.succ_le_succ (Nat.zero_le k)) hz0 hboth.1)
      have h0' : hamming I ψ θ' = 0 := by
        cases hham : hamming I ψ θ' with
        | zero => rfl
        | succ k =>
            exact False.elim (step_fails_cell I ψ θ' hlen
              (by rw [hham]; exact Nat.succ_le_succ (Nat.zero_le k)) hz0 hboth.2)
      have hθθ' : hamming I θ θ' = 0 := by
        apply (hamming_eq_zero I θ θ').mpr
        intro i hi
        have hp : ψ i = θ i := (hamming_eq_zero I ψ θ).mp h0 i hi
        have hp' : ψ i = θ' i := (hamming_eq_zero I ψ θ').mp h0' i hi
        exact hp.symm.trans hp'
      have h01 : (0 : Nat) = 1 := by
        rw [← hθθ']
        exact hadj
      cases h01
  | inr hhold =>
      exact False.elim ((step_fails_hold I u θ hhold hz0) hboth.1)

end Formalizations.EBC

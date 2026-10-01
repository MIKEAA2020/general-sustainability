/-
  Formalizations.EBC_Pairs_v2
  ==========================

  **`prop:bands`, second clause: a Hamming-adjacent pair survives from
  `z₀ = 1.1`.**

  `EBC_Pairs` supplied the drift facts (`+3/10` matched, `−1/10`
  mismatched) and the dip lemma. This module runs the alternation.

  The strategy is `θ, θ′, θ, θ′ …` (`altPairs`). Cell `θ` takes its
  matched step first and its mismatched step second; cell `θ′` takes them
  in the opposite order. So `θ` never dips below where it started, while
  `θ′` dips by exactly `1/10` in its first step — which is why the
  threshold is `1.1` and not `1.0`. Net `+1/5` per two-step cycle, so the
  cycle endpoints rise and the invariant `z ≥ 1.1` is preserved.

  Contents:

  * `isCellAction`, `isFullHold`, **`inAlphabet`** — the paper's action
    set at `m = 4`: the 16 cell actions plus the all-hold, 17 in total,
    as the verification script enumerates them. `matched_is_cell` places
    the alternation inside it.
  * `tenth_pos`, `one_le_one_one` — `1 ≤ 1.1`.
  * `matched_scale_m4` — `10·d(matched θ, θ) = 3`, the `+3/10`, scaled.
  * **`cycle_net_nonneg`** — per two-step cycle the pair gains `+1/5 ≥ 0`.
  * **`pair_survives`** — from `z₀ ≥ 1.1`, both cells survive the
    alternation at every horizon.

  **Alphabet note.** The sufficiency direction needs no restriction: the
  alternation uses only cell actions, so `pair_survives` holds over the
  full `Nat → Tri`. The restriction will be needed for the *necessity*
  direction, where `prop:bands` claims failure at `z₀ = 1.0` — and that
  claim is false if partial holds are allowed (see the header of
  `EBC_Pairs`). The predicate is defined here so the next module can
  state it.
-/

import Formalizations.Prelude
import Formalizations.EBC_ExactBelief_v2
import Formalizations.EBC_Dynamics
import Formalizations.EBC_Hamming
import Formalizations.EBC_Bands
import Formalizations.EBC_Bands_v2
import Formalizations.EBC_Pairs
import Formalizations.RatArith

open Formalizations.EBC

namespace Formalizations.EBC

variable {K : Type} [OrdField K]

/-! ## The paper's action alphabet -/

/-- A **cell action**: `±1` in every coordinate, never `hold`. -/
def isCellAction (u : Nat → Tri) : Prop := ∀ i, u i ≠ Tri.hold

/-- The **all-hold** action. -/
def isFullHold (u : Nat → Tri) : Prop := ∀ i, u i = Tri.hold

/-- **The paper's alphabet at `m = 4`**: the 16 cell actions plus the
all-hold — 17 actions, exactly what the verification script enumerates. -/
def inAlphabet (u : Nat → Tri) : Prop := isCellAction u ∨ isFullHold u

/-- Matched play is a cell action, so the alternation is in-alphabet. -/
theorem matched_is_cell (θ : Nat → Bool) : isCellAction (matched θ) := by
  intro i
  cases h : θ i <;> simp [matched, h]

/-! ## The alternation -/

/-- `θ, θ′, θ, θ′ …` — `T` full two-step cycles. -/
def altPairs : Nat → (Nat → Bool) → (Nat → Bool) → List (Nat → Tri)
  | 0, _, _ => []
  | n + 1, θ, θ' => matched θ :: matched θ' :: altPairs n θ θ'

/-! ## `1 ≤ 1.1` -/

/-- One tenth is positive. -/
theorem tenth_pos : (0 : K) < tenth := by
  apply pos_of_mul_pos_left' (c := ten (K := K))
  · change (0 : K) < ten (K := K) * ((1 : K) / ten (K := K))
    rw [show ten (K := K) * ((1 : K) / ten (K := K)) = (1 : K) by
          change natToK (K := K) 10 * ((1 : K) / natToK (K := K) 10) = (1 : K)
          exact natToK_mul_inv 10 (by decide)]
    exact zero_lt_one
  · exact ten_pos

/-- The floor sits below the pair threshold: `1 ≤ 1.1`. -/
theorem one_le_one_one : (1 : K) ≤ one_one := by
  change (1 : K) ≤ (1 : K) + tenth
  have h : (1 : K) + 0 ≤ (1 : K) + tenth :=
    add_le_add (le_refl (1 : K)) (le_of_lt tenth_pos)
  simpa using h

/-! ## The cycle -/

/-- **`10·d(matched θ, θ) = 3`** — the paper's `+3/10`, scaled. -/
theorem matched_scale_m4 (I : List Nat) (θ : Nat → Bool) (hlen : I.length = 4) :
    ten (K := K) * drift I (matched θ) θ = three := by
  rw [drift_matched, hlen]
  exact matched_drift_scale_m4

/-- **Per cycle the pair gains `+1/5`.** Scaled: `10·(3/10 − 1/10) = 3 − 1
= 2 ≥ 0`. This is the invariant that makes the induction close. -/
theorem cycle_net_nonneg (I : List Nat) (θ θ' : Nat → Bool)
    (hlen : I.length = 4) (hadj : hamming I θ θ' = 1) :
    (0 : K) ≤ drift I (matched θ) θ + drift I (matched θ') θ := by
  apply le_of_mul_le_mul_pos (c := ten (K := K))
  · have hm : ten (K := K) * drift I (matched θ) θ = three :=
      matched_scale_m4 I θ hlen
    have hx : ten (K := K) * drift I (matched θ') θ = -(1 : K) :=
      mismatch_scale_m4 I θ θ' hlen hadj
    calc
      ten (K := K) * (0 : K) = (0 : K) := by simp
      _ ≤ natToK (K := K) 2 := natToK_nonneg 2
      _ = ten (K := K) *
            (drift I (matched θ) θ + drift I (matched θ') θ) := by
              rw [left_distrib, hm, hx]
              change natToK (K := K) 2 = natToK (K := K) 3 + (-(1 : K))
              symm
              apply add_left_cancel (a := (1 : K))
              calc
                (1 : K) + (natToK (K := K) 3 + (-(1 : K)))
                    = natToK (K := K) 3 := by
                        rw [← add_assoc, add_comm (1 : K) (natToK (K := K) 3),
                          add_assoc]
                        have hz : (1 : K) + (-(1 : K)) = 0 := by
                          rw [← sub_eq, sub_self]
                        rw [hz]
                        simp
                _ = (1 : K) + natToK (K := K) 2 := by
                        rw [show (1 : K) = natToK (K := K) 1 by simp [natToK]]
                        rw [← natToK_add]
  · exact ten_pos

/-! ## The pair clause -/

/-- **A Hamming-adjacent pair survives from `z₀ = 1.1`, at every horizon.**

Cell `θ` moves first and takes `+3/10` then `−1/10`; cell `θ′` takes
`−1/10` then `+3/10`. So `θ` never dips below the starting state, `θ′`
dips by exactly `1/10` (which `z₀ ≥ 1.1` absorbs), and each cycle ends
`+1/5` higher than it began — preserving the invariant for the tail.

No restriction on the action alphabet is needed here: the witness uses
only cell actions. -/
theorem pair_survives (I : List Nat) (θ θ' : Nat → Bool)
    (hlen : I.length = 4) (hadj : hamming I θ θ' = 1)
    (z0 : K) (T : Nat) (hz : one_one ≤ z0) :
    survivesTo I θ (altPairs T θ θ') z0 ∧
      survivesTo I θ' (altPairs T θ θ') z0 := by
  induction T generalizing z0 with
  | zero =>
      simp [altPairs, survivesTo]
      exact le_trans one_le_one_one hz
  | succ T ih =>
      have hz1 : (1 : K) ≤ z0 := le_trans one_le_one_one hz
      have hadj' : hamming I θ' θ = 1 := by
        rw [hamming_comm I θ' θ]
        exact hadj
      -- cell θ: matched first, then mismatched
      have hθ1 : (1 : K) ≤ z0 + drift I (matched θ) θ := by
        have hnn : (0 : K) ≤ drift I (matched θ) θ :=
          le_of_lt (drift_matched_pos I θ hlen)
        have h : z0 + 0 ≤ z0 + drift I (matched θ) θ :=
          add_le_add (le_refl z0) hnn
        exact le_trans hz1 (by simpa using h)
      have hθ1_up : one_one ≤ z0 + drift I (matched θ) θ := by
        have hnn : (0 : K) ≤ drift I (matched θ) θ :=
          le_of_lt (drift_matched_pos I θ hlen)
        have h : z0 + 0 ≤ z0 + drift I (matched θ) θ :=
          add_le_add (le_refl z0) hnn
        exact le_trans hz (by simpa using h)
      have hθc : one_one ≤
          z0 + drift I (matched θ) θ + drift I (matched θ') θ := by
        have hnet : (0 : K) ≤ drift I (matched θ) θ + drift I (matched θ') θ :=
          cycle_net_nonneg I θ θ' hlen hadj
        have h : z0 + 0 ≤
            z0 + (drift I (matched θ) θ + drift I (matched θ') θ) :=
          add_le_add (le_refl z0) hnet
        exact le_trans hz (by simpa [add_assoc] using h)
      -- cell θ': mismatched first, then matched
      have hθp1 : (1 : K) ≤ z0 + drift I (matched θ) θ' :=
        mismatched_step_floor I θ' θ hlen hadj' hz
      have hθpc : one_one ≤
          z0 + drift I (matched θ) θ' + drift I (matched θ') θ' := by
        have hnet : (0 : K) ≤ drift I (matched θ') θ' + drift I (matched θ) θ' :=
          cycle_net_nonneg I θ' θ hlen hadj'
        have hnet' : (0 : K) ≤
            drift I (matched θ) θ' + drift I (matched θ') θ' := by
          simpa [add_comm] using hnet
        have h : z0 + 0 ≤
            z0 + (drift I (matched θ) θ' + drift I (matched θ') θ') :=
          add_le_add (le_refl z0) hnet'
        exact le_trans hz (by simpa [add_assoc] using h)
      constructor
      · have htail :=
          ih (z0 + drift I (matched θ) θ + drift I (matched θ') θ) hθc
        simp [altPairs, survivesTo, hz1, hθ1]
        exact htail.1
      · have htail :=
          ih (z0 + drift I (matched θ) θ' + drift I (matched θ') θ') hθpc
        simp [altPairs, survivesTo, hz1, hθp1]
        exact htail.2

end Formalizations.EBC

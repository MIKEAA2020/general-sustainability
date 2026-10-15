/-
  Formalizations.EBC_Bands_v2
  ===========================

  **`prop:bands`, first clause completed: a singleton is survivable.**

  `EBC_Bands` landed the matched-play machinery and stopped in front of
  one arithmetic step — `−1/2 + (1/5)·4 = 3/10 > 0` — which had been
  written three times ad hoc without converging. `RatArith` pays for that
  step once, generally:

  * `natToK_mul_inv_cancel (q m)` turns `natToK (q·m) · (1/natToK m)` into
    `natToK q` — clearing a denominator exactly, no division;
  * `pos_of_mul_pos_left'` turns `0 < c·x` and `0 < c` into `0 < x`.

  So the proof is: scale by `10`, clear both denominators, read off
  `8 − 5 = 3`, and use `3 > 0`. The same two lemmas will discharge the
  mismatched drift `−1/10` in the pair clause.

  Contents:

  * `matched_drift_scale_m4` — `10 · (−1/2 + (1/5)·4) = 3`.
  * `matched_drift_pos_m4` — the paper's "+3/10".
  * `drift_matched_pos` — positive on a 4-dimensional index set.
  * **`singleton_survives`** — matched play repeated keeps a singleton
    above the floor `1` from any `z₀ ≥ 1`, at every horizon. This is the
    first clause of `prop:bands`.

  **Not included, by directive.** The counts — "the 16 singletons", "the
  32 Hamming-adjacent pairs" — are instance-level and belong to the
  Python verifier, not to Lean. What the classification *structure*
  needs (`lem:triangle`: no three cells pairwise adjacent; `cor_hamming_m4`:
  surviving pairs have `h ≤ 1`) is already proved. Only the enumeration
  is deferred.
-/

import Formalizations.Prelude
import Formalizations.EBC_ExactBelief_v2
import Formalizations.EBC_Dynamics
import Formalizations.EBC_Hamming
import Formalizations.EBC_Bands
import Formalizations.RatArith

open Formalizations.EBC

namespace Formalizations.EBC

variable {K : Type} [OrdField K]

/-! ## `−1/2 + (1/5)·4 = 3/10`, by clearing denominators -/

/-- **`10·(−1/2 + (1/5)·4) = 3`.** Both products clear exactly:
`10·(1/5)·4 = 40·(1/5) = 8` and `10·(1/2) = 5·2·(1/2) = 5`. -/
theorem matched_drift_scale_m4 : ten (K := K) * (-half + fifth * four) = three := by
  have hcomm : -half (K := K) + fifth * four = fifth * four - half := by
    rw [sub_eq, add_comm]
  rw [hcomm, mul_sub]
  have hA : ten (K := K) * (fifth * four) = eight := by
    change natToK (K := K) 10 *
        (((1 : K) / natToK (K := K) 5) * natToK (K := K) 4) = natToK (K := K) 8
    calc
      natToK (K := K) 10 * (((1 : K) / natToK (K := K) 5) * natToK (K := K) 4)
          = (natToK (K := K) 10 * natToK (K := K) 4) *
              ((1 : K) / natToK (K := K) 5) := by
              rw [mul_comm ((1 : K) / natToK (K := K) 5) (natToK (K := K) 4)]
              rw [← mul_assoc]
      _ = natToK (K := K) (10 * 4) * ((1 : K) / natToK (K := K) 5) := by
              rw [natToK_mul]
      _ = natToK (K := K) (8 * 5) * ((1 : K) / natToK (K := K) 5) := by
              rw [show (10 : Nat) * 4 = 8 * 5 by decide]
      _ = natToK (K := K) 8 := natToK_mul_inv_cancel 8 5 (by decide)
  have hB : ten (K := K) * half = five := by
    change natToK (K := K) 10 * ((1 : K) / natToK (K := K) 2) = natToK (K := K) 5
    rw [show natToK (K := K) 10 = natToK (K := K) (5 * 2) by congr 1]
    exact natToK_mul_inv_cancel 5 2 (by decide)
  rw [hA, hB]
  change natToK (K := K) 8 - natToK (K := K) 5 = natToK (K := K) 3
  apply add_left_cancel (a := natToK (K := K) 5)
  calc
    natToK (K := K) 5 + (natToK (K := K) 8 - natToK (K := K) 5)
        = natToK (K := K) 8 := by rw [add_comm, sub_add_cancel]
    _ = natToK (K := K) 5 + natToK (K := K) 3 := by
        rw [← natToK_add]

/-- **The matched drift at `m = 4` is positive** — the paper's "+3/10". -/
theorem matched_drift_pos_m4 : (0 : K) < -half (K := K) + fifth * four := by
  apply pos_of_mul_pos_left'
  · rw [matched_drift_scale_m4]
    exact three_pos
  · exact ten_pos

/-- Positive matched drift on a 4-dimensional index set. -/
theorem drift_matched_pos (I : List Nat) (θ : Nat → Bool) (hlen : I.length = 4) :
    (0 : K) < drift I (matched θ) θ := by
  rw [drift_matched, hlen]
  change (0 : K) < -half + fifth * natToK (K := K) 4
  exact matched_drift_pos_m4

/-! ## The singleton clause -/

/-- **A singleton is survivable from every `z₀ ≥ 1`, at every horizon.**
Repeating the matched action never lets the state fall below where it
started, because the matched drift is positive.

This is the first clause of `prop:bands`. No periodicity, no horizon
bound: `T` is arbitrary and `List.replicate` is only the witness. -/
theorem singleton_survives (I : List Nat) (θ : Nat → Bool) (z0 : K) (T : Nat)
    (hlen : I.length = 4) (hz0 : (1 : K) ≤ z0) :
    survivesTo I θ (List.replicate T (matched θ)) z0 := by
  induction T generalizing z0 with
  | zero =>
      simpa [survivesTo] using hz0
  | succ T ih =>
      simp [List.replicate, survivesTo]
      constructor
      · exact hz0
      · have hd : (0 : K) ≤ drift I (matched θ) θ :=
          le_of_lt (drift_matched_pos I θ hlen)
        have hzle : z0 ≤ z0 + drift I (matched θ) θ := by
          have : z0 + 0 ≤ z0 + drift I (matched θ) θ := add_le_add (le_refl z0) hd
          simpa using this
        exact ih (z0 + drift I (matched θ) θ) (le_trans hz0 hzle)

end Formalizations.EBC

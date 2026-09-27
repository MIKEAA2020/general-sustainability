/-
  Formalizations.EBC_Pairs
  =======================

  **Mismatched play: the `−1/10` of `prop:bands`.**

  `EBC_Bands`/`EBC_Bands_v2` handled matched play (`+3/10`) and closed the
  singleton clause. This module handles the other half: what happens when
  the action played is the *other* cell of a Hamming-adjacent pair. Each
  coordinate then contributes `+1` where the cells agree and `−1` where
  they differ, so the inner product is `m − 2h` — at `m = 4, h = 1` that
  is `2`, and the drift is `−1/2 + (1/5)·2 = −1/10`.

  Contents:

  * `hamming_comm` — the distance is symmetric.
  * `ipi_mismatched` — `⟨matched θ', θ⟩ = m − 2h`, in the
    cancellation-avoiding form `⟨matched θ', θ⟩ + 2·h = m`.
  * `ipi_mismatched_m4_adj` — at `m = 4, h = 1`: the inner product is `2`.
  * `mismatch_scale_m4` — `10·d(matched θ', θ) = −1`, i.e. `−1/10`.
  * `mismatched_step_floor` — **the dip lemma**: from `z ≥ 1.1` a single
    mismatched step stays at or above the floor. This is the exact
    statement behind the paper's "within-cycle dip of `1/10`", and it is
    why the pair threshold is `1.1` and not `1.0`.

  **A scope finding, recorded because it constrains the next step.**
  `Tri` has three values — `pos`, `neg`, `hold` — so an action may hold at
  some coordinates and match at others. Under the paper's own verified
  action alphabet (17 actions at `m = 4`: the 16 cells plus the all-hold)
  such *partial* holds are excluded. They are not excluded by the type
  `Nat → Tri` used throughout this layer. That matters: from `z₀ = 1.0`,
  holding at exactly the one coordinate where the pair differs and
  matching everywhere else gives both cells `−1/2 + (1/5)·3 = +1/10`,
  reaching `1.1`, from which the alternation works. So the paper's
  "survivable *exactly* from `z₀ ≥ 1.1`" is true over its 17-action
  alphabet and false over the unrestricted one. The pair clause must
  therefore be stated relative to an action alphabet; this module proves
  the drift facts, which are alphabet-independent.

  **Not claimed here.** No `pair_survives` yet, and no necessity
  direction: both need the alphabet restriction made explicit first.
-/

import Formalizations.Prelude
import Formalizations.EBC_ExactBelief_v2
import Formalizations.EBC_Dynamics
import Formalizations.EBC_Hamming
import Formalizations.EBC_Bands
import Formalizations.EBC_Bands_v2
import Formalizations.RatArith

open Formalizations.EBC

namespace Formalizations.EBC

variable {K : Type} [OrdField K]

/-! ## Numerals -/

/-- One tenth. -/
def tenth : K := (1 : K) / ten

/-- `1.1` — the paper's pair threshold, `1 + 1/10`. -/
def one_one : K := (1 : K) + tenth

/-- The Hamming distance is symmetric. -/
theorem hamming_comm (I : List Nat) (θ θ' : Nat → Bool) :
    hamming I θ θ' = hamming I θ' θ := by
  induction I with
  | nil => rfl
  | cons i Is ih => simp [hamming, ih, eq_comm]

/-! ## `⟨matched θ', θ⟩ = m − 2h` -/

/-- **The mismatched inner product.** Playing cell `θ'` against cell `θ`
scores `+1` on each agreeing coordinate and `−1` on each differing one,
hence `m − 2h`.

Stated additively as `⟨matched θ', θ⟩ + 2·h = m` rather than with a
subtraction: the layer has no `ring`, and the induction step is then a
pure rearrangement plus one `−1 + 1 = 0`, discharged by `add_left_cancel`
and `ac_rfl`. -/
theorem ipi_mismatched (I : List Nat) (θ θ' : Nat → Bool) :
    ipi I (matched θ') θ + two * natToK (K := K) (hamming I θ θ') =
      natToK (K := K) I.length := by
  induction I with
  | nil =>
      simp [ipi, hamming]
  | cons i Is ih =>
      by_cases heq : θ i = θ' i
      · -- agreeing coordinate: contributes `+1`, adds nothing to `h`
        have hterm : b1t (matched θ' i) * b1 (θ i) = (1 : K) := by
          cases h1 : θ' i <;> cases h2 : θ i <;>
            simp [matched, b1t, b1, h1, h2, neg_mul_neg] at heq ⊢
        have hipi : ipi (i :: Is) (matched θ') θ =
            (1 : K) + ipi Is (matched θ') θ := by simp [ipi, hterm]
        have hham : natToK (K := K) (hamming (i :: Is) θ θ') =
            natToK (K := K) (hamming Is θ θ') := by simp [hamming, heq]
        rw [hipi, hham]
        calc
          ((1 : K) + ipi Is (matched θ') θ) +
              two * natToK (K := K) (hamming Is θ θ')
              = (1 : K) + (ipi Is (matched θ') θ +
                  two * natToK (K := K) (hamming Is θ θ')) := by rw [add_assoc]
          _ = (1 : K) + natToK (K := K) Is.length := by rw [ih]
          _ = natToK (K := K) (i :: Is).length := by simp [add_comm]
      · -- differing coordinate: contributes `−1`, adds `1` to `h`
        have hterm : b1t (matched θ' i) * b1 (θ i) = -(1 : K) := by
          cases h1 : θ' i <;> cases h2 : θ i <;>
            simp [matched, b1t, b1, h1, h2] at heq ⊢
        have hipi : ipi (i :: Is) (matched θ') θ =
            -(1 : K) + ipi Is (matched θ') θ := by simp [ipi, hterm]
        have hham : natToK (K := K) (hamming (i :: Is) θ θ') =
            (1 : K) + natToK (K := K) (hamming Is θ θ') := by
          simp [hamming, heq, natToK_add]
        rw [hipi, hham]
        rw [show two (K := K) *
              ((1 : K) + natToK (K := K) (hamming Is θ θ')) =
              two (K := K) + two (K := K) *
                natToK (K := K) (hamming Is θ θ') by
            rw [left_distrib]
            simp [two, natToK]]
        apply add_left_cancel (a := (1 : K))
        calc
          (1 : K) + ((-(1 : K) + ipi Is (matched θ') θ) +
              (two (K := K) + two (K := K) *
                natToK (K := K) (hamming Is θ θ')))
              = ((1 : K) + (-(1 : K) + ipi Is (matched θ') θ)) +
                  (two (K := K) + two (K := K) *
                    natToK (K := K) (hamming Is θ θ')) := by
                      rw [← add_assoc]
          _ = ipi Is (matched θ') θ +
                  (two (K := K) + two (K := K) *
                    natToK (K := K) (hamming Is θ θ')) := by
                      rw [← add_assoc (1 : K) (-(1 : K)) (ipi Is (matched θ') θ)]
                      have hz : (1 : K) + (-(1 : K)) = 0 := by rw [← sub_eq, sub_self]
                      rw [hz]
                      simp
          _ = two (K := K) + (ipi Is (matched θ') θ +
                  two (K := K) * natToK (K := K) (hamming Is θ θ')) := by
                      rw [← add_assoc (ipi Is (matched θ') θ) (two (K := K))
                            (two (K := K) * natToK (K := K) (hamming Is θ θ'))]
                      rw [add_comm (ipi Is (matched θ') θ) (two (K := K))]
                      rw [add_assoc (two (K := K)) (ipi Is (matched θ') θ)
                            (two (K := K) * natToK (K := K) (hamming Is θ θ'))]
          _ = (1 : K) + (1 : K) + (ipi Is (matched θ') θ +
                  two (K := K) * natToK (K := K) (hamming Is θ θ')) := by
                      simp [two, natToK]
          _ = (1 : K) + ((1 : K) + natToK (K := K) Is.length) := by
                      rw [ih, add_assoc]
          _ = (1 : K) + natToK (K := K) (i :: Is).length := by simp [add_comm]

/-! ## At `m = 4`, `h = 1` -/

/-- **The mismatched inner product at `m = 4`, `h = 1` is `2`.** -/
theorem ipi_mismatched_m4_adj (I : List Nat) (θ θ' : Nat → Bool)
    (hlen : I.length = 4) (hadj : hamming I θ θ' = 1) :
    ipi I (matched θ') θ = two (K := K) := by
  have h := ipi_mismatched (K := K) I θ θ'
  rw [hlen, hadj] at h
  have h1 : two * natToK (K := K) 1 = two (K := K) := by simp [natToK]
  rw [h1] at h
  have h4 : natToK (K := K) 4 = two (K := K) + two (K := K) := by
    change natToK (K := K) 4 = natToK (K := K) 2 + natToK (K := K) 2
    rw [← natToK_add]
  have h' : ipi I (matched θ') θ + two (K := K) =
      two (K := K) + two (K := K) := by
    rw [h, h4]
  apply le_antisymm
  · have hle : two (K := K) + ipi I (matched θ') θ ≤
        two (K := K) + two (K := K) := by
      rw [add_comm (two (K := K)) (ipi I (matched θ') θ)]
      exact le_of_eq h'
    exact le_of_add_le_add_left hle
  · have hle : two (K := K) + two (K := K) ≤
        two (K := K) + ipi I (matched θ') θ := by
      rw [add_comm (two (K := K)) (ipi I (matched θ') θ)]
      exact le_of_eq h'.symm
    exact le_of_add_le_add_left hle

/-- **`10·d(matched θ', θ) = −1`** at `m = 4`, `h = 1` — the paper's
`−1/10`, scaled. `10·(1/5)·2 = 20·(1/5) = 4` and `10·(1/2) = 5`, so the
scaled drift is `4 − 5 = −1`.

Kept in scaled form deliberately: the layer has no division, and the
order argument that consumes it (`mismatched_step_floor`) only ever needs
the scaled version. -/
theorem mismatch_scale_m4 (I : List Nat) (θ θ' : Nat → Bool)
    (hlen : I.length = 4) (hadj : hamming I θ θ' = 1) :
    ten (K := K) * drift I (matched θ') θ = -(1 : K) := by
  have hipi : ipi I (matched θ') θ = two (K := K) :=
    ipi_mismatched_m4_adj I θ θ' hlen hadj
  rw [drift, hipi]
  have hcomm : -half (K := K) + fifth * two = fifth * two - half := by
    rw [sub_eq, add_comm]
  rw [hcomm, mul_sub]
  have hA : ten (K := K) * (fifth * two) = natToK (K := K) 4 := by
    change natToK (K := K) 10 *
        (((1 : K) / natToK (K := K) 5) * natToK (K := K) 2) = natToK (K := K) 4
    calc
      natToK (K := K) 10 *
          (((1 : K) / natToK (K := K) 5) * natToK (K := K) 2)
          = (natToK (K := K) 10 * natToK (K := K) 2) *
              ((1 : K) / natToK (K := K) 5) := by
              rw [mul_comm ((1 : K) / natToK (K := K) 5) (natToK (K := K) 2)]
              rw [← mul_assoc]
      _ = natToK (K := K) (10 * 2) * ((1 : K) / natToK (K := K) 5) := by
              rw [natToK_mul]
      _ = natToK (K := K) (4 * 5) * ((1 : K) / natToK (K := K) 5) := by
              rw [show (10 : Nat) * 2 = 4 * 5 by decide]
      _ = natToK (K := K) 4 := natToK_mul_inv_cancel 4 5 (by decide)
  have hB : ten (K := K) * half = five := by
    change natToK (K := K) 10 * ((1 : K) / natToK (K := K) 2) =
        natToK (K := K) 5
    rw [show natToK (K := K) 10 = natToK (K := K) (5 * 2) by congr 1]
    exact natToK_mul_inv_cancel 5 2 (by decide)
  rw [hA, hB]
  change natToK (K := K) 4 - natToK (K := K) 5 = -(1 : K)
  apply add_left_cancel (a := natToK (K := K) 5)
  calc
    natToK (K := K) 5 + (natToK (K := K) 4 - natToK (K := K) 5)
        = natToK (K := K) 4 := by rw [add_comm, sub_add_cancel]
    _ = natToK (K := K) 5 + (-(1 : K)) := by
        apply add_left_cancel (a := (1 : K))
        calc
          (1 : K) + natToK (K := K) 4 = natToK (K := K) 5 := by
              rw [show (1 : K) = natToK (K := K) 1 by simp [natToK]]
              rw [← natToK_add]
          _ = (1 : K) + (natToK (K := K) 5 + (-(1 : K))) := by
              rw [← add_assoc, add_comm (1 : K) (natToK (K := K) 5), add_assoc]
              have hz : (1 : K) + (-(1 : K)) = 0 := by rw [← sub_eq, sub_self]
              rw [hz]
              simp

/-! ## The dip -/

/-- `10 · 1.1 = 11`. -/
theorem ten_mul_one_one : ten (K := K) * one_one = natToK (K := K) 11 := by
  change natToK (K := K) 10 *
      ((1 : K) + (1 : K) / natToK (K := K) 10) = natToK (K := K) 11
  rw [left_distrib]
  rw [natToK_mul_inv 10 (by decide)]
  simp

/-- **The dip lemma.** One mismatched step from `z ≥ 1.1` lands at or
above the floor `1`: `z − 1/10 ≥ 1`.

Proved by scaling rather than by dividing — `10·(z + d) = 10z − 1 ≥
11 − 1 = 10 = 10·1`, then `le_of_mul_le_mul_pos` — so it needs only the
scaled drift value. From `z₀ = 1.0` the same computation gives `0.9 < 1`:
this one inequality is the whole difference between the singleton
threshold and the pair threshold. -/
theorem mismatched_step_floor (I : List Nat) (θ θ' : Nat → Bool)
    (hlen : I.length = 4) (hadj : hamming I θ θ' = 1)
    {z : K} (hz : one_one ≤ z) :
    (1 : K) ≤ z + drift I (matched θ') θ := by
  apply le_of_mul_le_mul_pos (c := ten (K := K))
  · have hscale : ten (K := K) * drift I (matched θ') θ = -(1 : K) :=
      mismatch_scale_m4 I θ θ' hlen hadj
    calc
      ten (K := K) * (1 : K) = natToK (K := K) 10 := by simp [ten]
      _ = natToK (K := K) 11 + (-(1 : K)) := by
            apply add_left_cancel (a := (1 : K))
            calc
              (1 : K) + natToK (K := K) 10 = natToK (K := K) 11 := by
                  rw [show (1 : K) = natToK (K := K) 1 by simp [natToK]]
                  rw [← natToK_add]
              _ = (1 : K) + (natToK (K := K) 11 + (-(1 : K))) := by
                  rw [← add_assoc, add_comm (1 : K) (natToK (K := K) 11), add_assoc]
                  have hz : (1 : K) + (-(1 : K)) = 0 := by rw [← sub_eq, sub_self]
                  rw [hz]
                  simp
      _ ≤ ten (K := K) * z + (-(1 : K)) := by
            apply add_le_add_right
            calc
              natToK (K := K) 11 = ten (K := K) * one_one := by
                  rw [ten_mul_one_one]
              _ ≤ ten (K := K) * z :=
                  mul_le_mul_of_nonneg_left hz (le_of_lt ten_pos)
      _ = ten (K := K) * (z + drift I (matched θ') θ) := by
            rw [left_distrib, hscale]
  · exact ten_pos

end Formalizations.EBC

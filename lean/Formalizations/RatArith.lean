/-
  Formalizations.RatArith
  =======================

  **Rational arithmetic over a bare `OrdField` — the helper that was
  being paid for four times.**

  The layer has no `norm_num`, no `ring`, no `linarith` and no `NatCast`.
  So a step like

      −1/2 + (1/5)·4 = 3/10  >  0

  is not a computation, it is a lemma — and `prop:bands` needs that kind
  of step in every clause (the matched drift is `+3/10`, the mismatched
  drift is `−1/10`). v35 wrote it ad hoc, three times, and did not
  converge. This module pays for it once.

  The trick is scaling by a positive constant. Rather than divide, clear
  the denominators: `10·(−1/2 + (1/5)·4) = −5 + 8 = 3`, and `3 > 0` with
  `10 > 0` forces the unscaled quantity positive. Everything below is
  what that needs.

  Contents:

  * `natToK_pos`, `natToK_ne_zero` — a nonzero natural embeds to a
    positive, hence nonzero, field element. (v35 had written `two_pos`,
    `five_pos`, `ten_pos`, `three_pos` separately; this is the general
    form.)
  * `natToK_mul_inv` — `natToK m · (1 / natToK m) = 1` for `m ≠ 0`.
  * **`natToK_mul_inv_cancel`** — `natToK (q·m) · (1 / natToK m) = natToK q`.
    This is the one that clears a denominator exactly: it is the whole
    reason no division is needed.
  * **`pos_of_mul_pos_left`** — from `0 < c·a` and `0 ≤ c`, conclude
    `0 < a`: the order half of the scaling argument.

  Nothing here is specific to the EBC papers. It is nevertheless placed
  *after* them in the import order, for one reason: the Nat → K embedding
  `natToK` was first needed by `EBC_Dynamics` and so is defined there, and
  `natToK_mul` in `EBC_Hamming`. If either is ever promoted into
  `Prelude`, this module can move up with them unchanged.
-/

import Formalizations.Prelude
import Formalizations.EBC_Dynamics
import Formalizations.EBC_Hamming

namespace Formalizations

open Formalizations.EBC

variable {K : Type} [OrdField K]

/-- A positive natural embeds to a positive field element. -/
theorem natToK_pos {n : Nat} (h : 0 < n) : (0 : K) < natToK n := by
  have h1 : natToK (K := K) 1 ≤ natToK (K := K) n := natToK_mono h
  have h1' : (1 : K) ≤ natToK (K := K) n := by simpa [natToK] using h1
  exact lt_of_lt_of_le (zero_lt_one (K := K)) h1'

/-- A nonzero natural embeds to a nonzero field element. -/
theorem natToK_ne_zero {n : Nat} (h : n ≠ 0) : natToK (K := K) n ≠ 0 := by
  intro hz
  have hpos : (0 : K) < natToK (K := K) n := natToK_pos (Nat.pos_of_ne_zero h)
  exact hpos.2 (by rw [hz]; exact le_refl 0)

/-- `natToK m · (1 / natToK m) = 1`, for `m ≠ 0`. -/
theorem natToK_mul_inv (m : Nat) (hm : m ≠ 0) :
    natToK (K := K) m * ((1 : K) / natToK (K := K) m) = (1 : K) := by
  rw [div_eq]
  simp
  exact mul_inv_cancel_field (natToK_ne_zero hm)

/-- **Clearing a denominator exactly.** `natToK (q·m) · (1 / natToK m) = natToK q`.

This is the workhorse: it turns `40 · (1/5)` into `8` in one rewrite, with
`q` and `m` supplied by the caller and the divisibility discharged by
`decide` on `Nat`. -/
theorem natToK_mul_inv_cancel (q m : Nat) (hm : m ≠ 0) :
    natToK (K := K) (q * m) * ((1 : K) / natToK (K := K) m) = natToK (K := K) q := by
  rw [natToK_mul]
  calc
    (natToK (K := K) q * natToK (K := K) m) * ((1 : K) / natToK (K := K) m)
        = natToK (K := K) q *
            (natToK (K := K) m * ((1 : K) / natToK (K := K) m)) := by rw [mul_assoc]
    _ = natToK (K := K) q * (1 : K) := by rw [natToK_mul_inv m hm]
    _ = natToK (K := K) q := by simp

/-- **Scale by a positive constant, order half.** From `0 < c·a` and
`0 ≤ c`, conclude `0 < a`.

If `a ≤ 0` then `c·a ≤ 0`, contradicting `0 < c·a`; and if `a = 0` then
`c·a = 0`, likewise. So `0 ≤ a` and `a ≠ 0`. -/
theorem pos_of_mul_pos_left {a c : K} (h : (0 : K) < c * a) (hc : (0 : K) ≤ c) :
    (0 : K) < a := by
  cases le_total a (0 : K) with
  | inl ha =>
      have hmul : c * a ≤ c * (0 : K) := mul_le_mul_of_nonneg_left ha hc
      have h0 : c * a ≤ 0 := by simpa using hmul
      exact False.elim (h.2 h0)
  | inr hge =>
      by_cases haz : a = 0
      · have hz : c * a = 0 := by rw [haz]; simp
        have h0 : c * a ≤ 0 := by rw [hz]; exact le_refl 0
        exact False.elim (h.2 h0)
      · exact lt_of_le_of_ne hge (fun h => haz h.symm)

/-- The scaled form, packaged: `0 < x` follows from `0 < c·x` and `0 < c`. -/
theorem pos_of_mul_pos_left' {a c : K} (h : (0 : K) < c * a) (hc : (0 : K) < c) :
    (0 : K) < a :=
  pos_of_mul_pos_left h (le_of_lt hc)

end Formalizations

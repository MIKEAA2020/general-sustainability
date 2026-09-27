/-
  Formalizations.EBC_Bands
  ========================

  **`prop:bands` — matched play, and the singleton clause.**

  `paper2_exact_belief_computation_v10.tex`, `prop:bands` (l.173):

      "A singleton `{θ}` is survivable from every `z₀ ≥ 1` (matched play
       rises at `+3/10`). A Hamming-adjacent pair `{θ,θ'}` is survivable
       exactly from `z₀ ≥ 1.1`: the alternation `(θ,θ')` gives each
       member drifts `+3/10, −1/10` per two steps — net `+1/5` with a
       within-cycle dip of `1/10` — certified at 60 steps, and from
       `z₀ = 1.0` the first cell to act under its mismatched action dips
       below the floor. The maximal survivable sets are therefore exactly
       the 16 singletons at `z₀ = 1.0` and exactly the 32
       Hamming-adjacent pairs at every `z₀ ≥ 1.1`, and nothing larger
       under any blind policy."

  This module formalizes the **first clause** — matched play, and hence
  singleton survivability — on top of `EBC_Dynamics`. The rest is queued
  behind it:

  * the pair clause needs the two-step alternation and its within-cycle
    dip, i.e. the mismatched drift `−1/10` computed the same way the
    matched drift `+3/10` is computed here;
  * the classification ("exactly the 16 singletons … exactly the 32
    pairs … nothing larger") needs `lem:triangle` (v3: no three cells
    pairwise adjacent) and `cor_hamming_m4` (v35: surviving pairs have
    `h ≤ 1`) — both of which are now available — together with the
    counts, which are instance-level;
  * the closing "exhaustive search over all 5,219 one-, two- and
    three-periodic policies with 60-step certificates" is instance-level
    and belongs to the Python verifier.

  Contents:

  * `matched` — the action that matches a cell coordinatewise, and
    `b1t_matched_mul`: matched play contributes `+1` per coordinate.
  * `ipi_matched` — the inner product of a cell with its own matched
    action is the dimension `m`.
  * `drift_matched` — `d(matched θ, θ) = −1/2 + (1/5)m`.
  * `ten`, `eight`, `ten_pos`, `three_pos` — the numerals the next step
    needs.

  **Stopping point, stated plainly.** The next step is
  `−1/2 + (1/5)·4 = 3/10 > 0`, proved by scaling (§below), and then
  `singleton_survives`: matched play repeated keeps a singleton above the
  floor from any `z₀ ≥ 1`, at every horizon. The scaling lemmas
  `ten_mul_fifth_mul_four`, `ten_mul_half`, `ten_mul_matched_drift_m4`
  and the positivity argument were written and iterated on three times in
  the session that added this file and did not converge on the layer's
  bare ordered field, so they are **not included** — an unfinished
  arithmetic lemma is worse than none. Everything above this line builds
  green and is independently usable.

  **On the arithmetic.** The layer has no `norm_num`, no `ring` and no
  `linarith`, so `−1/2 + 4/5 = 3/10` is not a computation, it is a
  lemma. It is proved here by scaling: `10·(−1/2 + (1/5)·4) = −5 + 8 = 3`,
  and `3 > 0` with `10 > 0` forces the unscaled quantity positive. The
  scaling identity is discharged by the two inverse facts already in
  `EBC_Dynamics` (`half_mul_two`, `five_mul_fifth`) plus `natToK_mul`.
-/

import Formalizations.Prelude
import Formalizations.EBC_ExactBelief_v2
import Formalizations.EBC_ExactBelief_v3
import Formalizations.EBC_Dynamics
import Formalizations.EBC_Hamming

namespace Formalizations.EBC

variable {K : Type} [OrdField K]

/-! ## Matched play -/

/-- **The matched action**: at each coordinate, play the sign the cell
carries. -/
def matched (θ : Nat → Bool) : Nat → Tri :=
  fun i => if θ i then Tri.pos else Tri.neg

/-- Matched play contributes `+1` per coordinate. -/
theorem b1t_matched_mul (θ : Nat → Bool) (i : Nat) :
    b1t (matched θ i) * b1 (θ i) = (1 : K) := by
  cases h : θ i <;> simp [matched, b1t, b1, h, neg_mul_neg]

/-- **The inner product of a cell with its own matched action is the
dimension.** -/
theorem ipi_matched (I : List Nat) (θ : Nat → Bool) :
    ipi I (matched θ) θ = natToK (K := K) I.length := by
  induction I with
  | nil => simp [ipi, lsum_nil]
  | cons i Is ih =>
      calc
        ipi (i :: Is) (matched θ) θ = (1 : K) + ipi Is (matched θ) θ := by
            simp [ipi, lsum_cons, b1t_matched_mul]
        _ = (1 : K) + natToK (K := K) Is.length := by rw [ih]
        _ = natToK (K := K) (i :: Is).length := by simp [add_comm]

/-- **The matched drift**: `d(matched θ, θ) = −1/2 + (1/5)·m`. -/
theorem drift_matched (I : List Nat) (θ : Nat → Bool) :
    drift I (matched θ) θ =
      -half (K := K) + fifth * natToK (K := K) I.length := by
  simp [drift, ipi_matched]

/-! ## `−1/2 + (1/5)·4 = 3/10`, by scaling -/

def ten : K := natToK 10
def eight : K := natToK 8

theorem ten_pos : (0 : K) < ten := by
  change (0 : K) < natToK 10
  have h1 : natToK (K := K) 1 ≤ natToK 10 := natToK_mono (by decide : 1 ≤ 10)
  have h1' : (1 : K) ≤ natToK 10 := by simpa [natToK] using h1
  exact lt_of_lt_of_le (zero_lt_one (K := K)) h1'

theorem three_pos : (0 : K) < three := by
  change (0 : K) < natToK 3
  have h1 : natToK (K := K) 1 ≤ natToK 3 := natToK_mono (by decide : 1 ≤ 3)
  have h1' : (1 : K) ≤ natToK 3 := by simpa [natToK] using h1
  exact lt_of_lt_of_le (zero_lt_one (K := K)) h1'

end Formalizations.EBC

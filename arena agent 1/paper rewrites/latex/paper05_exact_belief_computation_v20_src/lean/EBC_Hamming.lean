/-
  Formalizations.EBC_Hamming
  ==========================

  **`cor:hamming` at `m = 4` — the paper's own form, `h ≤ 1`.**

  `paper2_exact_belief_computation_v10.tex`, `cor:hamming` (l.140):

      "At `m = 4`: (ii) forces the pair average to reach `5` while (i)
       caps it at `2(4 − h)`, so `5 ≤ 2(4 − h)`, i.e. `h ≤ 3/2`: every
       blind survivable pair has `h ≤ 1`, and since survivability passes
       to subsets, every pair inside a blind survivable set is
       Hamming-adjacent."

  `EBC_Dynamics` §5 already proves the inequality this rests on, for
  every `m` and without the `liminf` (`cor_hamming_dist`):

      five + two · natToK h  ≤  two · natToK m

  — the paper's `h ≤ m − 5/2`, made integral and division-free. What
  remains is the last step from a field inequality back to a statement
  about `Nat`: specialize to `m = 4`, so `5 + 2h ≤ 8`, i.e. `2h ≤ 3`,
  hence `h ≤ 1`.

  That step is not free, because the layer has no `norm_num`, no `ring`
  and no `linarith`. This module supplies exactly what it needs and
  nothing more:

  * `natToK_mul` — the embedding is multiplicative (skipped in
    `EBC_Dynamics`, which only needed additivity and monotonicity);
  * `two_mul_two_eq_four`, `two_mul_four_eq_five_add_three` — the two
    numeral identities, discharged by `natToK_mul` plus `decide` on
    `Nat`;
  * `le_of_add_le_add_left` — cancellation of a common additive term;
  * `three_lt_four` — `3 < 4`, from `natToK_mono` and `zero_ne_one'`;
  * `cor_hamming_m4` — the result.

  **Statement, honestly.** `cor_hamming_m4` says: if two cells both
  survive a nonempty horizon from `z₀ = 1` under one blind action
  sequence, on a 4-dimensional index set, then their Hamming distance is
  at most `1`. It does **not** say "every pair inside a blind survivable
  set is Hamming-adjacent": that closing sentence of the paper's
  corollary appeals to survivability passing to subsets, which is a
  statement about the survivable-family operator and is not formalized
  here. -/

import Formalizations.Prelude
import Formalizations.EBC_ExactBelief_v2
import Formalizations.EBC_ExactBelief_v3
import Formalizations.EBC_Dynamics

namespace Formalizations.EBC

variable {K : Type} [OrdField K]

/-! ## The embedding is multiplicative -/

/-- `natToK (n · m) = natToK n · natToK m`. `EBC_Dynamics` needed only
additivity and monotonicity; the `m = 4` arithmetic needs this too. -/
theorem natToK_mul (n m : Nat) : natToK (K := K) (n * m) = natToK n * natToK m := by
  induction n with
  | zero => simp [natToK]
  | succ n ih =>
      rw [Nat.succ_mul, natToK_add, ih, natToK]
      calc
        (natToK (K := K) n * natToK m) + natToK (K := K) m
            = natToK (K := K) n * natToK (K := K) m +
                (1 : K) * natToK (K := K) m := by simp
        _ = (natToK (K := K) n + 1) * natToK (K := K) m := by
            rw [mul_comm (natToK (K := K) n + 1) (natToK (K := K) m)]
            rw [left_distrib (natToK (K := K) m) (natToK (K := K) n) (1 : K)]
            rw [mul_comm (natToK (K := K) m) (natToK (K := K) n)]
            simp [add_comm]

/-! ## Numerals -/

def three : K := natToK 3

theorem two_mul_two_eq_four : two (K := K) * two = four := by
  change natToK (K := K) 2 * natToK (K := K) 2 = natToK (K := K) 4
  rw [← natToK_mul]

/-- `2·4 = 5 + 3`, both being `8`. Stated in this form so the
`m = 4` step is one rewrite away from `5 + 2h ≤ 5 + 3`. -/
theorem two_mul_four_eq_five_add_three :
    two (K := K) * four = five (K := K) + three := by
  change natToK (K := K) 2 * natToK (K := K) 4 =
      natToK (K := K) 5 + natToK (K := K) 3
  rw [← natToK_mul, ← natToK_add]

/-- Cancellation of a common additive term. -/
theorem le_of_add_le_add_left {a b c : K} (h : a + b ≤ a + c) : b ≤ c := by
  have h1 : -a + (a + b) ≤ -a + (a + c) := add_le_add_left h (-a)
  simpa [← add_assoc, neg_add_cancel, zero_add] using h1

/-- `3 < 4`. -/
theorem three_lt_four : three (K := K) < four := by
  apply lt_of_le_of_ne
  · change natToK (K := K) 3 ≤ natToK (K := K) 4
    exact natToK_mono (by decide : 3 ≤ 4)
  · intro heq
    have hsucc : natToK (K := K) 3 + 1 = natToK (K := K) 3 := by
      calc
        natToK (K := K) 3 + 1 = natToK (K := K) 4 := by rfl
        _ = natToK (K := K) 3 := heq.symm
    have hsucc0 : natToK (K := K) 3 + 1 = natToK (K := K) 3 + 0 := by
      simpa using hsucc
    have h1z : (1 : K) = 0 := add_left_cancel hsucc0
    exact zero_ne_one' h1z.symm

/-! ## `cor:hamming` at `m = 4` -/

/-- **Every blind survivable pair at `m = 4` has Hamming distance at
most `1`.**

Two cells that both survive one nonempty blind action sequence from
`z₀ = 1`, over a 4-dimensional index set, are Hamming-adjacent (or
equal). The paper reaches this through `h ≤ 3/2` from a `liminf`; here it
comes from `cor_hamming_dist` specialized to `m = 4` — `5 + 2h ≤ 8`,
hence `2h ≤ 3`, hence `h ≤ 1` — with no limit and no division.

The step `2h ≤ 3 ⟹ h ≤ 1` goes by cases on whether `2 ≤ h` in `K`: if
it is, then `4 ≤ 2h ≤ 3`, contradicting `3 < 4`; if it is not, then
`h ≤ 1` in `Nat`, because `h` is an embedded natural. -/
theorem cor_hamming_m4 (I : List Nat) (θ θ' : Nat → Bool) (us : List (Nat → Tri))
    (hlen : I.length = 4) (hpos : 0 < us.length)
    (hs : survivesTo I θ us (1 : K)) (hs' : survivesTo I θ' us (1 : K)) :
    hamming I θ θ' ≤ 1 := by
  have hd := cor_hamming_dist I θ θ' us hpos hs hs'
  rw [hlen] at hd
  change five (K := K) + two (K := K) * natToK (K := K) (hamming I θ θ') ≤
      two (K := K) * four at hd
  rw [two_mul_four_eq_five_add_three] at hd
  have h2h : two (K := K) * natToK (K := K) (hamming I θ θ') ≤ three :=
    le_of_add_le_add_left hd
  by_cases h2le : two (K := K) ≤ natToK (K := K) (hamming I θ θ')
  · exfalso
    have h4le : four (K := K) ≤
        two (K := K) * natToK (K := K) (hamming I θ θ') := by
      calc
        four (K := K) = two (K := K) * two := two_mul_two_eq_four.symm
        _ ≤ two (K := K) * natToK (K := K) (hamming I θ θ') :=
            mul_le_mul_of_nonneg_left h2le (le_of_lt (two_pos (K := K)))
    have h43 : four (K := K) ≤ three := le_trans h4le h2h
    exact (three_lt_four (K := K)).2 h43
  · have hnle : ¬ 2 ≤ hamming I θ θ' := by
      intro hn
      exact h2le (by simpa [two] using (natToK_mono (K := K) hn))
    omega

end Formalizations.EBC

/-
  Formalizations.EBC_Dynamics
  ===========================

  **The drift dynamics of the exact-belief cube: the machinery
  `cor:hamming`, `prop:ladder` and `prop:deadline` all sit on.**

  `paper2_exact_belief_computation_v10.tex`, `lem:pairsum` (l.106), fixes
  the model:

      dimension `m`, cells `θ ∈ {+1,-1}^m`, actions
      `u ∈ {+1,-1}^m ∪ {(0,…,0)}`, drift
      `d(u,θ) = -1/2 + (1/5)·⟨u,θ⟩`, floor `z ≥ 1`.

  Nothing in the layer models that: `EBC_ExactBelief_v2` has the inner
  product and the pair-sum bound, but no trajectory, no floor, no
  survival. This module supplies them, and it is a prerequisite for the
  three remaining EBC results, not a result itself.

  **Why the Nat → K embedding had to be built.** The layer's `OrdField`
  carries `zero`/`one` and the field operations, but **no `OfNat` and no
  `NatCast`** — `2`, `5`, `(n : K)` are all unavailable, and there is no
  `norm_num`, no `ring`, no `linarith`. So the dimension, the horizon and
  the Hamming distance have to be carried into `K` by an explicit
  embedding `natToK`, with its own monotonicity and the fact it needs
  most: `natToK n ≤ 1 → n ≤ 1` — the step that turns an inequality
  between field elements back into a statement about `Nat`.

  **Why the drift is not scaled.** The paper's `d(u,θ) = -1/2 + (1/5)⟨u,θ⟩`
  is used verbatim rather than rescaled by `10` (which would make the
  arithmetic integral): the floor is `1`, and rescaling drags a factor
  through every survival statement. The cost is the one identity
  `-1/2 + -1/2 = -1`, proved here as `half_add_half`; the layer has no
  `neg_add`, so that too is proved (`neg_add`).

  Contents:

  * §1 `natToK`: the embedding, nonnegativity, additivity, monotonicity,
    `lsum_ones`, and `natToK_le_one`.
  * §2 the numerals `two`/`four`/`five`, their positivity, `half`,
    `fifth`, `half_add_half`, `five_mul_fifth`.
  * §3 `drift`, `stateAfter`, `totalDrift`, `survivesTo`, with
    `stateAfter_eq` (the closed form) and `survivesTo_totalDrift_lower`
    (survival bounds the accumulated drift from below).
  * §4 `pairIpSum` and `totalDrift_pair` — the summed pair identity that
    `cor:hamming` couples to `lem:pairsum` (i).

  * §5 **`cor:hamming`**: `pairIpSum_upper` (`lem:pairsum` (i), summed)
    meets `pairIpSum_lower_of_survive`, the horizon cancels, and the
    result is `five ≤ two * agreeMass I θ θ'` — the paper's `5 ≤ 2(m−h)`
    — and, via `agreeMass_add_natToK_hamming`, its distance form
    `5 + 2h ≤ 2m`, i.e. the paper's `h ≤ m − 5/2` made integral.

  **The `liminf` is not needed.** The paper gets `cor:hamming` from
  `lem:pairsum` (ii), a `liminf` of Cesàro averages over an infinite
  blind policy. `pairIpSum_lower_of_survive` proves the same inequality
  at every finite horizon `T > 0`, so no limit, no Cesàro average and no
  Archimedean hypothesis enters — and the layer has none to offer. The
  cost is the statement's form: it is quantified over a finite action
  list `us` and a starting state `z₀ = 1`, not over an infinite policy.

  **Not done**: the paper's mnemonic `h ≤ 3/2 ⟹ h ≤ 1` at `m = 4`
  (`cor_hamming_m4`), which needs one more bridge from `2h ≤ 3` in `K`
  back to `h ≤ 1` in `Nat`; `prop:ladder` and `prop:deadline`, which
  queue behind `prop:bands` and the delayed-instance dynamics.
-/

import Formalizations.Prelude
import Formalizations.EBC_ExactBelief_v2
import Formalizations.EBC_ExactBelief_v3

namespace Formalizations.EBC

variable {K : Type} [OrdField K]

/-! ## §1 The Nat → K embedding -/

/-- The unique embedding of `Nat` into `K` determined by `0 ↦ 0`,
`(n+1) ↦ n + 1`. The layer has no `NatCast`; this is it. -/
def natToK : Nat → K
  | 0 => 0
  | n + 1 => natToK n + 1

@[simp] theorem natToK_zero : natToK (K := K) 0 = 0 := rfl
@[simp] theorem natToK_succ (n : Nat) : natToK (K := K) (n + 1) = natToK n + 1 := rfl

theorem natToK_nonneg (n : Nat) : (0 : K) ≤ natToK n := by
  induction n with
  | zero => exact le_refl 0
  | succ n ih =>
      have h : (0 : K) + 0 ≤ natToK n + 1 := add_le_add ih zero_le_one'
      simpa using h

theorem natToK_add (n m : Nat) : natToK (K := K) (n + m) = natToK n + natToK m := by
  induction n with
  | zero => simp [natToK]
  | succ n ih =>
      calc
        natToK (K := K) (Nat.succ n + m) = natToK (K := K) (n + m) + 1 := by
            rw [Nat.succ_add]; rfl
        _ = (natToK (K := K) n + natToK (K := K) m) + 1 := by rw [ih]
        _ = (natToK (K := K) n + 1) + natToK (K := K) m := by
            rw [add_assoc, add_comm (natToK (K := K) m) (1 : K), ← add_assoc]
        _ = natToK (K := K) (Nat.succ n) + natToK (K := K) m := rfl

theorem natToK_mono {n m : Nat} (h : n ≤ m) : natToK (K := K) n ≤ natToK m := by
  have h' : natToK (K := K) m = natToK n + natToK (m - n) := by
    have := natToK_add (K := K) n (m - n)
    rwa [Nat.add_sub_of_le h] at this
  rw [h']
  have hnn : (0 : K) ≤ natToK (m - n) := natToK_nonneg (m - n)
  have : natToK (K := K) n + 0 ≤ natToK n + natToK (m - n) :=
    add_le_add (le_refl (natToK (K := K) n)) hnn
  simpa using this

/-- Summing `1` over a list gives the embedded length. -/
theorem lsum_ones {α : Type} (l : List α) :
    lsum (l.map (fun _ => (1 : K))) = natToK l.length := by
  induction l with
  | nil => simp [lsum_nil]
  | cons a t ih => simp [lsum_cons, ih, add_comm]

/-- **The bridge back to `Nat`.** An embedded natural that is at most `1`
is at most `1` as a natural — the step that turns a field inequality into
the combinatorial conclusion `h ≤ 1`. -/
theorem natToK_le_one {n : Nat} (h : natToK (K := K) n ≤ 1) : n ≤ 1 := by
  cases n with
  | zero => exact Nat.zero_le 1
  | succ n =>
      cases n with
      | zero => exact Nat.le_refl 1
      | succ n =>
          exfalso
          have hge : ((1 : K) + 1) ≤ natToK (K := K) (Nat.succ (Nat.succ n)) := by
            have hnn : (0 : K) ≤ natToK (K := K) n := natToK_nonneg n
            have h2 : ((1 : K) + 1) + 0 ≤ ((1 : K) + 1) + natToK n :=
              add_le_add (le_refl ((1 : K) + 1)) hnn
            simpa [natToK, add_assoc, add_comm] using h2
          have h21 : ((1 : K) + 1) ≤ 1 := le_trans hge h
          exact (one_lt_two' (K := K)).2 h21

/-! ## §2 Numerals, and the two fractions the drift needs -/

/-- `-(a + b) = -a + -b`. Not in the layer; needed for `-1/2 + -1/2`. -/
theorem neg_add (a b : K) : -(a + b) = -a + -b := by
  apply add_left_cancel (a := a + b)
  calc
    (a + b) + -(a + b) = (0 : K) := add_neg_cancel (a + b)
    _ = (a + b) + (-a + -b) := by
        symm
        calc
          (a + b) + (-a + -b) = a + (b + (-a + -b)) := by rw [add_assoc]
          _ = a + ((b + -a) + -b) := by rw [← add_assoc b (-a) (-b)]
          _ = a + ((-a + b) + -b) := by rw [add_comm b (-a)]
          _ = a + (-a + (b + -b)) := by rw [add_assoc]
          _ = (a + -a) + (b + -b) := by rw [add_assoc]
          _ = (0 : K) := by rw [add_neg_cancel, add_neg_cancel, zero_add]

def two : K := natToK 2
def four : K := natToK 4
def five : K := natToK 5
def half : K := (1 : K) / two
def fifth : K := (1 : K) / five

theorem two_pos : (0 : K) < two := by
  simpa [two, natToK] using lt_trans (zero_lt_one (K := K)) (one_lt_two' (K := K))

theorem two_ne_zero : two (K := K) ≠ 0 := by
  intro h0
  exact (two_pos (K := K)).2 (by rw [h0]; exact le_refl 0)

theorem five_pos : (0 : K) < five := by
  change (0 : K) < natToK 5
  exact lt_of_lt_of_le (two_pos (K := K)) (natToK_mono (K := K) (by omega : 2 ≤ 5))

theorem five_ne_zero : five (K := K) ≠ 0 := by
  intro h0
  exact (five_pos (K := K)).2 (by rw [h0]; exact le_refl 0)

/-- `1/2 + 1/2 = 1`. The layer has no `field_simp`; this is the manual
version: `2 · (1/2) = 1` by `div_mul_cancel`, and `2 · x = x + x`. -/
theorem half_mul_two : half (K := K) * two = (1 : K) := by
  change ((1 : K) / two (K := K)) * two (K := K) = (1 : K)
  exact div_mul_cancel (two_ne_zero (K := K)) (1 : K)

theorem half_add_half : half (K := K) + half = 1 := by
  have hmul : two * half = (1 : K) := by
    rw [mul_comm (two (K := K)) (half (K := K))]
    exact half_mul_two
  have hsplit : two (K := K) * half (K := K) = half (K := K) + half (K := K) := by
    calc
      two * half = half * two := mul_comm (two (K := K)) (half (K := K))
      _ = half * ((1 : K) + 1) := by simp [two]
      _ = half * (1 : K) + half * (1 : K) :=
          left_distrib (half (K := K)) (1 : K) (1 : K)
      _ = half + half := by simp
  rw [← hsplit]
  exact hmul

/-- `5 · (1/5) = 1`. -/
theorem five_mul_fifth : five * fifth = (1 : K) := by
  rw [mul_comm (five (K := K)) (fifth (K := K))]
  change ((1 : K) / five (K := K)) * five (K := K) = (1 : K)
  exact div_mul_cancel (five_ne_zero (K := K)) (1 : K)

/-! ## §3 Drift, trajectories, survival -/

/-- **The drift.** `d(u,θ) = -1/2 + (1/5)·⟨u,θ⟩`, verbatim from
`lem:pairsum`. -/
def drift (I : List Nat) (u : Nat → Tri) (θ : Nat → Bool) : K :=
  -half + fifth * ipi I u θ

/-- The state after executing the action list, by recursion. -/
def stateAfter (I : List Nat) (θ : Nat → Bool) : List (Nat → Tri) → K → K
  | [], z => z
  | u :: us, z => stateAfter I θ us (z + drift I u θ)

/-- The accumulated drift over an action list. -/
def totalDrift (I : List Nat) (θ : Nat → Bool) (us : List (Nat → Tri)) : K :=
  lsum (us.map (fun u => drift I u θ))

/-- **Survival to the horizon.** Every state visited, including the
initial one, is at or above the floor `1`. Recursion on the action list
rather than a quantifier over prefixes: the layer's list API is thin, and
this form is what the induction wants. -/
def survivesTo (I : List Nat) (θ : Nat → Bool) : List (Nat → Tri) → K → Prop
  | [], z => (1 : K) ≤ z
  | u :: us, z => (1 : K) ≤ z ∧ survivesTo I θ us (z + drift I u θ)

/-- The closed form of the recursion. -/
theorem stateAfter_eq (I : List Nat) (θ : Nat → Bool) :
    ∀ (us : List (Nat → Tri)) (z0 : K),
      stateAfter I θ us z0 = z0 + totalDrift I θ us := by
  intro us
  induction us with
  | nil => intro z0; simp [stateAfter, totalDrift]
  | cons u us ih => intro z0; simp [stateAfter, totalDrift, ih, add_assoc]

/-- Survival to the end of the list. -/
theorem survivesTo_final (I : List Nat) (θ : Nat → Bool) :
    ∀ (us : List (Nat → Tri)) (z0 : K),
      survivesTo I θ us z0 → (1 : K) ≤ stateAfter I θ us z0 := by
  intro us
  induction us with
  | nil => intro z0 hs; exact hs
  | cons u us ih => intro z0 hs; exact ih (z0 + drift I u θ) hs.2

/-- **Survival bounds the accumulated drift from below**: the trajectory
may not fall below the floor, so the total drift is at least the initial
deficit `1 − z₀`. At the edge `z₀ = 1` this is `0 ≤ totalDrift`. -/
theorem survivesTo_totalDrift_lower (I : List Nat) (θ : Nat → Bool)
    (us : List (Nat → Tri)) (z0 : K) (hs : survivesTo I θ us z0) :
    (1 : K) - z0 ≤ totalDrift I θ us := by
  have hf := survivesTo_final I θ us z0 hs
  rw [stateAfter_eq] at hf
  calc
    (1 : K) - z0 = (1 : K) + -z0 := by rw [sub_eq]
    _ ≤ (z0 + totalDrift I θ us) + -z0 := add_le_add_right hf (-z0)
    _ = -z0 + (z0 + totalDrift I θ us) := by rw [add_comm]
    _ = totalDrift I θ us := by rw [← add_assoc, neg_add_cancel, zero_add]

/-! ## §4 The summed pair identity -/

/-- The sum, over the action list, of the two cells' inner products. -/
def pairIpSum (I : List Nat) (us : List (Nat → Tri)) (θ θ' : Nat → Bool) : K :=
  lsum (us.map (fun u => ipi I u θ + ipi I u θ'))

theorem lsum_neg_ones {α : Type} (l : List α) :
    lsum (l.map (fun _ => -(1 : K))) = -natToK l.length := by
  induction l with
  | nil => simp [lsum_nil, neg_zero]
  | cons a t ih =>
      simp [lsum_cons, ih, neg_add, add_comm]

/-- **One step of the pair drift.** `d(u,θ) + d(u,θ') = -1 + (1/5)(⟨u,θ⟩ + ⟨u,θ'⟩)`:
the two `-1/2`s make `-1` (`half_add_half`), and the two fifths distribute. -/
theorem drift_pair (I : List Nat) (u : Nat → Tri) (θ θ' : Nat → Bool) :
    drift I u θ + drift I u θ' = -(1 : K) + fifth * (ipi I u θ + ipi I u θ') := by
  unfold drift
  let h2 : K := half
  change (-h2 + fifth * ipi I u θ) + (-h2 + fifth * ipi I u θ') =
      -(1 : K) + fifth * (ipi I u θ + ipi I u θ')
  have hneg : -h2 + -h2 = -(1 : K) := by
    change -half (K := K) + -half = -(1 : K)
    rw [← neg_add, half_add_half]
  calc
    (-h2 + fifth * ipi I u θ) + (-h2 + fifth * ipi I u θ')
        = -h2 + (fifth * ipi I u θ + (-h2 + fifth * ipi I u θ')) := by
            rw [add_assoc]
    _ = -h2 + ((fifth * ipi I u θ + -h2) + fifth * ipi I u θ') := by
            rw [← add_assoc (fifth * ipi I u θ) (-h2) (fifth * ipi I u θ')]
    _ = -h2 + ((-h2 + fifth * ipi I u θ) + fifth * ipi I u θ') := by
            rw [add_comm (fifth * ipi I u θ) (-h2)]
    _ = -h2 + (-h2 + (fifth * ipi I u θ + fifth * ipi I u θ')) := by
            rw [add_assoc]
    _ = (-h2 + -h2) + (fifth * ipi I u θ + fifth * ipi I u θ') := by
            rw [← add_assoc]
    _ = -(1 : K) + fifth * (ipi I u θ + ipi I u θ') := by
            rw [hneg, ← left_distrib]

/-- **The summed pair identity.** Over a horizon of `T` actions,
`Σd(θ) + Σd(θ') = -T + (1/5)·Σ(⟨u,θ⟩ + ⟨u,θ'⟩)`. This is what couples
survival (left side, via `survivesTo_totalDrift_lower`) to
`lem:pairsum` (i) (right side, via `pair_ip_upper`). -/
theorem totalDrift_pair (I : List Nat) (θ θ' : Nat → Bool) (us : List (Nat → Tri)) :
    totalDrift I θ us + totalDrift I θ' us =
      -(natToK (K := K) us.length) + fifth * pairIpSum I us θ θ' := by
  unfold totalDrift pairIpSum
  calc
    lsum (us.map (fun u => drift I u θ)) + lsum (us.map (fun u => drift I u θ'))
        = lsum (us.map (fun u => drift I u θ + drift I u θ')) := by
            rw [← lsum_distrib]
    _ = lsum (us.map (fun u => -(1 : K) + fifth * (ipi I u θ + ipi I u θ'))) := by
            apply lsum_congr
            intro u hu
            exact drift_pair I u θ θ'
    _ = lsum (us.map (fun _ => -(1 : K))) +
        lsum (us.map (fun u => fifth * (ipi I u θ + ipi I u θ'))) := by
            rw [lsum_distrib]
    _ = -(natToK (K := K) us.length) +
        fifth * lsum (us.map (fun u => ipi I u θ + ipi I u θ')) := by
            rw [lsum_neg_ones, ← lsum_const_mul]

/-! ## §5 `cor:hamming` — the pair-sum bound meets survival -/

theorem lsum_const {α : Type} (l : List α) (c : K) :
    lsum (l.map (fun _ => c)) = natToK l.length * c := by
  induction l with
  | nil => simp [lsum_nil]
  | cons a t ih =>
      calc
        lsum ((a :: t).map (fun _ => c)) = c + lsum (t.map (fun _ => c)) := by rfl
        _ = c + natToK (K := K) t.length * c := by rw [ih]
        _ = (natToK (K := K) t.length + 1) * c := by
            rw [mul_comm (natToK (K := K) t.length + 1) c]
            rw [left_distrib c (natToK (K := K) t.length) (1 : K)]
            rw [mul_comm c (natToK (K := K) t.length), mul_one, add_comm]
        _ = natToK (K := K) (a :: t).length * c := by simp

/-- **`lem:pairsum` (i), summed.** Over a horizon of `T` actions the pair
inner-product sum is at most `T · 2(m−h)` — i.e. `T` times the per-step
bound, with `agreeMass` carrying the `(m−h)`. -/
theorem pairIpSum_upper (I : List Nat) (us : List (Nat → Tri)) (θ θ' : Nat → Bool) :
    pairIpSum I us θ θ' ≤ natToK (K := K) us.length * (two * agreeMass I θ θ') := by
  unfold pairIpSum
  calc
    lsum (us.map (fun u => ipi I u θ + ipi I u θ'))
        ≤ lsum (us.map (fun _ => two (K := K) * agreeMass I θ θ')) := by
            apply lsum_le_lsum
            intro u hu
            simpa [two, natToK] using (pair_sum_bound (K := K) I u θ θ')
    _ = natToK (K := K) us.length * (two * agreeMass I θ θ') := lsum_const us _

/-- **Survival forces the pair inner-product sum up.** At the floor edge
`z₀ = 1`, survival of both cells to horizon `T` gives
`5·T ≤ Σ(⟨u,θ⟩ + ⟨u,θ'⟩)`.

This is `lem:pairsum` (ii) **without the `liminf`**: the inequality holds
at every horizon, so no Cesàro average, no limit, and no Archimedean
hypothesis is needed. (The paper's route passes to the limit; the
finite-horizon form is what the layer can actually carry.) -/
theorem pairIpSum_lower_of_survive (I : List Nat) (θ θ' : Nat → Bool)
    (us : List (Nat → Tri))
    (hs : survivesTo I θ us (1 : K)) (hs' : survivesTo I θ' us (1 : K)) :
    five * natToK (K := K) us.length ≤ pairIpSum I us θ θ' := by
  have hθ := survivesTo_totalDrift_lower I θ us (1 : K) hs
  have hθ' := survivesTo_totalDrift_lower I θ' us (1 : K) hs'
  rw [sub_self] at hθ hθ'
  have hsum : (0 : K) ≤ totalDrift I θ us + totalDrift I θ' us := by
    have := add_le_add hθ hθ'
    simpa using this
  rw [totalDrift_pair] at hsum
  have hle : natToK (K := K) us.length ≤ fifth * pairIpSum I us θ θ' := by
    calc
      natToK (K := K) us.length = (0 : K) + natToK (K := K) us.length := by rw [zero_add]
      _ ≤ (-(natToK (K := K) us.length) + fifth * pairIpSum I us θ θ') +
            natToK (K := K) us.length := add_le_add hsum (le_refl _)
      _ = fifth * pairIpSum I us θ θ' := by
          rw [add_comm (-(natToK (K := K) us.length) + fifth * pairIpSum I us θ θ')
                (natToK (K := K) us.length)]
          rw [← add_assoc, add_neg_cancel, zero_add]
  calc
    five * natToK (K := K) us.length ≤ five * (fifth * pairIpSum I us θ θ') :=
        mul_le_mul_of_nonneg_left hle (le_of_lt (five_pos (K := K)))
    _ = (five * fifth) * pairIpSum I us θ θ' := by rw [mul_assoc]
    _ = (1 : K) * pairIpSum I us θ θ' := by rw [five_mul_fifth]
    _ = pairIpSum I us θ θ' := by simp

/-- Cancellation of a positive factor. -/
theorem le_of_mul_le_mul_pos {a b c : K} (h : c * a ≤ c * b) (hc : (0 : K) < c) :
    a ≤ b := by
  have h' : a * c ≤ b * c := by simpa [mul_comm] using h
  have hsub : (0 : K) ≤ (b - a) * c := by
    rw [sub_mul]
    exact sub_nonneg.mpr h'
  have hba : (0 : K) ≤ b - a := nonneg_of_mul_nonneg_of_pos hsub hc
  exact sub_nonneg.mp hba

/-- **Agreement mass plus Hamming distance is the dimension** — the `m − h`
of `lem:pairsum` (i), proved rather than assumed. This links
`EBC_ExactBelief_v2`'s `agreeMass` (a `K`-valued sum) to
`EBC_ExactBelief_v3`'s `hamming` (a `Nat`). -/
theorem agreeMass_add_natToK_hamming (I : List Nat) (θ θ' : Nat → Bool) :
    agreeMass I θ θ' + natToK (K := K) (hamming I θ θ') =
      natToK (K := K) I.length := by
  induction I with
  | nil => simp [agreeMass, hamming]
  | cons i Is ih =>
      by_cases heq : θ i = θ' i
      · have hh : natToK (K := K) (hamming (i :: Is) θ θ') =
            (0 : K) + natToK (K := K) (hamming Is θ θ') := by
            simp [hamming, heq]
        have ha : agreeMass (K := K) (i :: Is) θ θ' = (1 : K) + agreeMass (K := K) Is θ θ' := by
            simp [agreeMass, heq]
        rw [ha, hh]
        calc
          ((1 : K) + agreeMass Is θ θ') + ((0 : K) + natToK (K := K) (hamming Is θ θ'))
              = (1 : K) + (agreeMass Is θ θ' + natToK (K := K) (hamming Is θ θ')) := by
                  simp [add_assoc]
          _ = (1 : K) + natToK (K := K) Is.length := by rw [ih]
          _ = natToK (K := K) (i :: Is).length := by simp [add_comm]
      · have hh : natToK (K := K) (hamming (i :: Is) θ θ') =
            (1 : K) + natToK (K := K) (hamming Is θ θ') := by
            simp [hamming, heq, natToK_add]
        have ha : agreeMass (K := K) (i :: Is) θ θ' = agreeMass (K := K) Is θ θ' := by
            simp [agreeMass, heq]
        rw [ha, hh]
        calc
          agreeMass Is θ θ' + ((1 : K) + natToK (K := K) (hamming Is θ θ'))
              = (agreeMass Is θ θ' + (1 : K)) +
                  natToK (K := K) (hamming Is θ θ') := by rw [← add_assoc]
          _ = ((1 : K) + agreeMass Is θ θ') +
                  natToK (K := K) (hamming Is θ θ') := by
                  rw [add_comm (agreeMass Is θ θ') (1 : K)]
          _ = (1 : K) + (agreeMass Is θ θ' + natToK (K := K) (hamming Is θ θ')) := by
                  rw [add_assoc]
          _ = (1 : K) + natToK (K := K) Is.length := by rw [ih]
          _ = natToK (K := K) (i :: Is).length := by simp [add_comm]

/-- **`cor:hamming`, as an inequality on the agreement mass.** If both
cells survive a nonempty horizon from `z₀ = 1` under one blind action
sequence, then `5 ≤ 2·(m−h)`.

The paper states this at `m = 4`, deriving `h ≤ 3/2` from
`lem:pairsum` (ii). The finite-horizon form holds for every `m`. -/
theorem cor_hamming (I : List Nat) (θ θ' : Nat → Bool) (us : List (Nat → Tri))
    (hpos : 0 < us.length)
    (hs : survivesTo I θ us (1 : K)) (hs' : survivesTo I θ' us (1 : K)) :
    five (K := K) ≤ two (K := K) * agreeMass (K := K) I θ θ' := by
  have hlow := pairIpSum_lower_of_survive I θ θ' us hs hs'
  have hup := pairIpSum_upper (K := K) I us θ θ'
  have hchain : five * natToK (K := K) us.length ≤
      natToK (K := K) us.length * (two * agreeMass I θ θ') := le_trans hlow hup
  rw [mul_comm (five (K := K)) (natToK (K := K) us.length)] at hchain
  have hT : (0 : K) < natToK (K := K) us.length := by
    have h1 : natToK (K := K) 1 ≤ natToK (K := K) us.length := natToK_mono hpos
    have h1' : (1 : K) ≤ natToK (K := K) us.length := by simpa [natToK] using h1
    exact lt_of_lt_of_le (zero_lt_one (K := K)) h1'
  exact le_of_mul_le_mul_pos hchain hT

/-- **`cor:hamming`, in distance form**: `5 + 2h ≤ 2m`. This is the
paper's `h ≤ m − 5/2`, integral and division-free, for every `m`. -/
theorem cor_hamming_dist (I : List Nat) (θ θ' : Nat → Bool) (us : List (Nat → Tri))
    (hpos : 0 < us.length)
    (hs : survivesTo I θ us (1 : K)) (hs' : survivesTo I θ' us (1 : K)) :
    five (K := K) + two (K := K) * natToK (K := K) (hamming I θ θ') ≤
      two (K := K) * natToK (K := K) I.length := by
  have hc := cor_hamming I θ θ' us hpos hs hs'
  have hm := agreeMass_add_natToK_hamming (K := K) I θ θ'
  have hag : agreeMass I θ θ' =
      natToK (K := K) I.length - natToK (K := K) (hamming I θ θ') := by
    calc
      agreeMass I θ θ' = (agreeMass I θ θ' + natToK (K := K) (hamming I θ θ')) -
            natToK (K := K) (hamming I θ θ') := by rw [add_sub_cancel]
      _ = natToK (K := K) I.length - natToK (K := K) (hamming I θ θ') := by rw [hm]
  rw [hag] at hc
  rw [mul_sub] at hc
  have hadd : five + two * natToK (K := K) (hamming I θ θ') ≤
      (two * natToK (K := K) I.length - two * natToK (K := K) (hamming I θ θ')) +
        two * natToK (K := K) (hamming I θ θ') :=
    add_le_add_right hc (two * natToK (K := K) (hamming I θ θ'))
  calc
    five + two * natToK (K := K) (hamming I θ θ') ≤
        (two * natToK (K := K) I.length - two * natToK (K := K) (hamming I θ θ')) +
          two * natToK (K := K) (hamming I θ θ') := hadd
    _ = two * natToK (K := K) I.length := by rw [sub_add_cancel]


end Formalizations.EBC

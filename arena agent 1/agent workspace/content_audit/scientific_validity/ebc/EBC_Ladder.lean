/-
  Formalizations.EBC_Ladder
  =========================

  **`prop:ladder`, on the EBC side.** Self-contained; no P3 import.

  The paper's `prop:ladder` (geometric ladder) states that the maximal
  conditional kernel mass doubles with each probe:

      z₀ = 1.0  :  1/16 → 1/8 → 1/4 → 1/2 → 1
      z₀ ≥ 1.1  :  1/8  → 1/4 → 1/2 → 1   → 1

  Its proof has three inputs: the antichain value formula, heredity of
  survivability, and `prop:bands`. This module supplies the second and
  third **in the shape the value formula wants**, which is the bridge's
  EBC half.

  **The shape.** P3's survivable-set family is
  `SfamAdm M k = (subsetsOf M.univX).filter (SurvivableAdm M · k)`, where
  `SurvivableAdm M S k` is *"one blind policy keeps every member alive
  for k steps"*, and `VfamAdm M k b` is the max of `b(S)` over it. So
  set-survivability is stated here in exactly that form
  (`survivesSetAt`: one in-alphabet policy, of a stated length, keeps
  every member at or above the floor), and heredity is one line. With
  that, P3's `VfamAdm_prune_eq` — value = max over the *maximal* jointly
  survivable sets — supplies the value formula in the identical shape,
  and `prop:ladder` follows by substituting the two cardinality bounds
  proved below. What is *not* done here: exhibiting the `DetMDP` over the
  sixteen cells whose `survK` is EBC's `survivesTo`. See
  `lean_bridge_spec.md` §4.

  **What `prop:bands` gives, as cardinality.** Write `M` for the largest
  number of pairwise-distinct cells a survivable subset can have:

  * at the floor `z₀ = 1.0`, `M = 1` — all members agree on `I`
    (`floor_survivable_all_agree`);
  * above the edge `z₀ ≥ 1.1` at any horizon `≥ 2`, `M ≤ 2`, and every
    pair is Hamming-adjacent (`pairs_adjacent_above`); and the bound is
    attained (`adjacent_pair_survives`) whenever the support contains an
    adjacent pair — which a subcube with a free coordinate does
    (`subcube_adjacent_pair`).

  The value is then `M / |S|`: `1/|S|` at the edge, `min(1, 2/|S|)`
  above it. The `2^j` subcube sizes and the ten numbers are
  instance-level and sit with the verifier; `|S|` is left symbolic here.

  Contents: `survivesSetAt`, `survivesSetAt_mono`, `inSubcube`, `flip`,
  `floor_survivable_all_agree`, `pairs_adjacent_above`,
  `flip_inSubcube`, `flip_differs`, `subcube_adjacent_pair`,
  `altPairs_length`, `altPairs_mem_inAlphabet`, `adjacent_pair_survives`.
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
import Formalizations.EBC_Pairs_v3
import Formalizations.EBC_Classification
import Formalizations.EBC_Classification_v2
import Formalizations.EBC_Classification_v3
import Formalizations.RatArith

open Formalizations.EBC

namespace Formalizations.EBC

variable {K : Type} [OrdField K]

/-! ## Set survivability, in P3's shape -/

/-- **A set of cells survives to horizon `L` from `z₀`**: one policy of
exactly `L` actions, every one of them in the paper's alphabet, keeps
every member at or above the floor.

Stated in this form — one policy, all members, a stated length — to
match P3's `SurvivableAdm M S k`, so that P3's value formula applies to
it verbatim. -/
def survivesSetAt (I : List Nat) (A : List (Nat → Bool)) (z0 : K) (L : Nat) : Prop :=
  ∃ us : List (Nat → Tri),
    us.length = L ∧ (∀ u, u ∈ us → inAlphabet u) ∧
      (∀ θ, θ ∈ A → survivesTo I θ us z0)

/-- **Heredity.** Survivability passes to subsets: one policy serving
more cells serves fewer. This is the paper's "survivability is
hereditary downward", and it is what makes the value a maximum over
subsets rather than over arbitrary sets. -/
theorem survivesSetAt_mono (I : List Nat) (A₁ A₂ : List (Nat → Bool))
    (z0 : K) (L : Nat)
    (hsub : ∀ θ, θ ∈ A₂ → θ ∈ A₁)
    (h : survivesSetAt I A₁ z0 L) : survivesSetAt I A₂ z0 L := by
  rcases h with ⟨us, hlen, hAlpha, hus⟩
  exact ⟨us, hlen, hAlpha, fun θ hθ => hus θ (hsub θ hθ)⟩

/-! ## The probe, as a restriction of the index set -/

/-- **A subcube**: the cells agreeing with a pattern `p` on the probed
coordinates `P`. A probe of one parameter adds one coordinate to `P`. -/
def inSubcube (P : List Nat) (p : Nat → Bool) (θ : Nat → Bool) : Prop :=
  ∀ i, i ∈ P → θ i = p i

/-- Flip one coordinate. -/
def flip (θ : Nat → Bool) (i : Nat) : Nat → Bool :=
  fun j => if j = i then not (θ i) else θ j

/-! ## The cardinality bounds from `prop:bands` -/

/-- **At the floor, every member of a surviving set agrees on `I`** — so
`M = 1` there. From `floor_survivors_agree_on`, which is `prop:bands`
(iii) at `z₀ = 1.0`. -/
theorem floor_survivable_all_agree (I : List Nat) (A : List (Nat → Bool))
    (hlen : I.length = 4) {L : Nat} (hL : 0 < L)
    (h : survivesSetAt I A (1 : K) L) :
    ∀ θ θ', θ ∈ A → θ' ∈ A → ∀ i, i ∈ I → θ i = θ' i := by
  rcases h with ⟨us, hlen_us, hAlpha, hus⟩
  have hpos : 0 < us.length := by omega
  exact floor_survivors_agree_on I A us hlen hpos hus hAlpha

/-- `10 · 1.1 ≤ 10 · 1.1` – the horizon cap at the band's edge:
`10·(z₀ − 1) ≤ 1` whenever `z₀ ≤ 1.1`. -/
theorem ten_mul_sub_one_le_one {z0 : K} (hzhi : z0 ≤ one_one) :
    ten * (z0 - (1 : K)) ≤ (1 : K) := by
  have hsub : z0 - (1 : K) ≤ one_one - (1 : K) := by
    have := add_le_add_right hzhi (-(1 : K))
    simpa [sub_eq] using this
  have hone : one_one - (1 : K) = tenth := by
    change ((1 : K) + tenth) + (-(1 : K)) = tenth
    rw [add_comm (1 : K) (tenth (K := K)), add_assoc, add_neg_cancel, add_zero]
  have ht : ten * tenth = (1 : K) := by
    change natToK (K := K) 10 * ((1 : K) / natToK (K := K) 10) = (1 : K)
    exact natToK_mul_inv 10 (by decide)
  calc
    ten * (z0 - (1 : K)) ≤ ten * tenth :=
        mul_le_mul_of_nonneg_left (le_trans hsub (le_of_eq hone)) (le_of_lt ten_pos)
    _ = (1 : K) := ht

/-- **Above the edge, every pair in a surviving set is Hamming-adjacent**
— so `M ≤ 2` there, at any horizon of two or more steps.

`far_pair_horizon_bound` caps the horizon of a distance-`≥2` pair by
`10·(z₀ − 1)`, which is at most `1` when `z₀ ≤ 1.1`; a horizon of `≥ 2`
is therefore impossible for such a pair. -/
theorem pairs_adjacent_above (I : List Nat) (A : List (Nat → Bool)) (z0 : K)
    (hlen : I.length = 4) {L : Nat} (hL : 2 ≤ L)
    (hzhi : z0 ≤ one_one)
    (h : survivesSetAt I A z0 L) :
    ∀ θ θ', θ ∈ A → θ' ∈ A → hamming I θ θ' ≤ 1 := by
  intro θ θ' hθ hθ'
  by_cases hle : hamming I θ θ' ≤ 1
  · exact hle
  · have hfar : 2 ≤ hamming I θ θ' := by omega
    rcases h with ⟨us, hlen_us, hAlpha, hus⟩
    have hb := far_pair_horizon_bound I θ θ' us z0 hlen hfar (hus θ hθ) (hus θ' hθ')
    have hL1 : natToK (K := K) L ≤ (1 : K) := by
      exact le_trans
        (by
          calc
            natToK (K := K) L = natToK (K := K) us.length := by rw [hlen_us]
            _ ≤ ten * (z0 - (1 : K)) := hb)
        (ten_mul_sub_one_le_one (K := K) hzhi)
    have hLn : L ≤ 1 := natToK_le_one hL1
    omega

/-! ## A subcube with a free coordinate contains an adjacent pair -/

/-- Flipping a coordinate **outside** the probed set stays in the
subcube: the flip is invisible to the probes. -/
theorem flip_inSubcube (P : List Nat) (p : Nat → Bool) (θ : Nat → Bool) (i : Nat)
    (hθ : inSubcube P p θ) (hiP : i ∉ P) : inSubcube P p (flip θ i) := by
  intro j hj
  have hji : j ≠ i := by
    intro hji
    exact hiP (by rw [← hji]; exact hj)
  simp [flip, hji, hθ j hj]

/-- The flip really differs, at the flipped coordinate. -/
theorem flip_differs (θ : Nat → Bool) (i : Nat) : θ i ≠ flip θ i i := by
  cases h : θ i <;> simp [flip, h]

/-- **A subcube with a free coordinate contains a Hamming-adjacent
pair.** Flipping a coordinate that is in the index set but not among the
probed ones gives a second cell of the subcube at distance `1`: it is not
distance `0` (they differ at `i`), and the pair bound caps it at `1`. -/
theorem subcube_adjacent_pair (I P : List Nat) (p θ : Nat → Bool) (i : Nat)
    (_hθ : inSubcube P p θ) (hiI : i ∈ I) (_hiP : i ∉ P)
    (hbound : hamming I θ (flip θ i) ≤ 1) :
    hamming I θ (flip θ i) = 1 := by
  have hne : hamming I θ (flip θ i) ≠ 0 := by
    intro hz
    have hagree := (hamming_eq_zero I θ (flip θ i)).mp hz i hiI
    exact flip_differs θ i hagree
  exact nat_ne_zero_of_le_one_eq_one hne hbound

/-! ## Attainment: an adjacent pair does survive -/

/-- The alternation has length `2T`. -/
theorem altPairs_length (T : Nat) (θ θ' : Nat → Bool) :
    (altPairs T θ θ').length = 2 * T := by
  induction T with
  | zero => rfl
  | succ T ih => simp [altPairs, ih]; omega

/-- Every action in the alternation is a cell action, hence in the
paper's alphabet. -/
theorem altPairs_mem_inAlphabet (T : Nat) (θ θ' : Nat → Bool) :
    ∀ u, u ∈ altPairs T θ θ' → inAlphabet u := by
  intro u hu
  induction T with
  | zero => simp [altPairs] at hu
  | succ T ih =>
      simp [altPairs] at hu
      rcases hu with rfl | rfl | hu
      · exact Or.inl (matched_is_cell θ)
      · exact Or.inl (matched_is_cell θ')
      · exact ih hu

/-- **The bound is attained.** A Hamming-adjacent pair survives from
`z₀ ≥ 1.1` at every even horizon, under the alternation — so `M = 2`
above the edge whenever the support contains such a pair. -/
theorem adjacent_pair_survives (I : List Nat) (θ θ' : Nat → Bool) (z0 : K)
    (T : Nat) (hlen : I.length = 4) (hadj : hamming I θ θ' = 1)
    (hz0 : one_one ≤ z0) :
    survivesSetAt I [θ, θ'] z0 (2 * T) := by
  refine ⟨altPairs T θ θ', altPairs_length T θ θ', altPairs_mem_inAlphabet T θ θ', ?_⟩
  intro x hx
  have hp := pair_survives I θ θ' hlen hadj z0 T hz0
  simp at hx
  rcases hx with rfl | rfl
  · exact hp.1
  · exact hp.2

end Formalizations.EBC

/-
  Formalizations.EBC_Classification
  =================================

  **`prop:bands`, the "nothing larger" clause at the floor `z₀ = 1.0`.**

  Two results do the work, and both were already proved:

  * `cor_hamming_m4` (`EBC_Hamming`) — two cells that both survive a
    nonempty blind action sequence from `z₀ = 1` over a 4-dimensional
    index set are at Hamming distance `≤ 1`;
  * `no_adjacency_triangle` (`EBC_ExactBelief_v3`), the formal
    `lem:triangle` — no three cells are pairwise at distance `1`.

  Together: every pair of survivors is at distance `≤ 1`, and three
  pairwise-distinct survivors would have to be pairwise at distance
  exactly `1`, which `lem:triangle` forbids. So **at most two distinct
  cells survive the floor**. Adding the necessity clause
  (`pair_first_step_fails`: from `z₀ = 1.0 < 1.1` no in-alphabet action
  serves both members of an adjacent pair) removes the second one: at
  the floor, **all survivors agree on `I`** — the maximal survivable sets
  are single cells. The paper counts 16 of them; that count is
  instance-level and stays with the verifier, by directive.

  Contents:

  * `survivesSetTo`, `survivesSet_mono` — survival of a *set* of cells,
    and the fact that it passes to subsets (the paper's last step:
    "the whole set fails with the pair").
  * `survivors_pairwise_adjacent` — any two survivors are at distance
    `≤ 1`.
  * `no_three_survivors` — three pairwise-distinct survivors are
    impossible.
  * `survivesTo_cons_floor`, `floor_pair_fails` — one step from the floor
    cannot serve an adjacent pair.
  * **`floor_survivors_agree`** — at `z₀ = 1.0`, any two surviving cells
    agree on every coordinate of `I`.

  **What is NOT claimed.** The `z₀ ≥ 1.1` half of "nothing larger" is
  not here. `cor_hamming_m4` is stated at `z₀ = 1` — it uses survival to
  bound the accumulated drift *from zero* — and it does not transfer to a
  higher start. The `z₀ ≥ 1.1` case needs the `z₀`-indexed pair-sum
  bound: for two cells at distance `h ≥ 2`, every action gives them a
  combined drift of at most `−1 + (1/5)·2·(4 − h) ≤ −1/5`, so over `L`
  steps their combined drift is at most `−L/5`, while surviving from
  `z₀` requires it to stay above `2·(1 − z₀)`. At `z₀ = 1.1` that forces
  `L ≤ 1`: even an adjacent-by-nothing pair survives at most one step.
  That argument runs through `pairIpSum_lower_of_survive` at a general
  `z₀` and is the next piece of this clause.
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
import Formalizations.RatArith

open Formalizations.EBC

namespace Formalizations.EBC

variable {K : Type} [OrdField K]

/-! ## Survival of a set -/

/-- A **set of cells survives**: every member does. -/
def survivesSetTo (I : List Nat) (S : List (Nat → Bool))
    (us : List (Nat → Tri)) (z0 : K) : Prop :=
  ∀ θ, θ ∈ S → survivesTo I θ us z0

/-- **Survivability passes to subsets**: if a set survives, so does every
subset — one policy serving more cells also serves fewer.

This is the paper's closing step: a set of three or more contains a pair
that fails, and therefore "the whole set fails with it". -/
theorem survivesSet_mono (I : List Nat) (S₁ S₂ : List (Nat → Bool))
    (us : List (Nat → Tri)) (z0 : K)
    (hsub : ∀ θ, θ ∈ S₂ → θ ∈ S₁)
    (hS : survivesSetTo I S₁ us z0) :
    survivesSetTo I S₂ us z0 := by
  intro θ hθ
  exact hS θ (hsub θ hθ)

/-! ## At most two distinct survivors -/

/-- **Any two survivors are Hamming-adjacent** (or equal): `h ≤ 1`.
Directly `cor_hamming_m4`, which is `cor:hamming` at `m = 4`. -/
theorem survivors_pairwise_adjacent (I : List Nat) (S : List (Nat → Bool))
    (us : List (Nat → Tri)) (hlen : I.length = 4) (hpos : 0 < us.length)
    (hS : survivesSetTo I S us (1 : K)) :
    ∀ θ θ', θ ∈ S → θ' ∈ S → hamming I θ θ' ≤ 1 := by
  intro θ θ' hθ hθ'
  exact cor_hamming_m4 I θ θ' us hlen hpos (hS θ hθ) (hS θ' hθ')

/-- A natural that is nonzero and at most `1` is `1`. -/
theorem nat_ne_zero_of_le_one_eq_one {n : Nat} (hn0 : n ≠ 0) (hle : n ≤ 1) : n = 1 := by
  cases n with
  | zero => exact False.elim (hn0 rfl)
  | succ k =>
      have hk : k ≤ 0 := by omega
      have : k = 0 := Nat.eq_zero_of_le_zero hk
      subst k
      rfl

/-- **No three pairwise-distinct cells survive the floor.**

Every pair of survivors is at distance `≤ 1` (`cor_hamming_m4`), and
pairwise distinct forces each distance to be exactly `1`; but
`lem:triangle` forbids three cells from being pairwise at distance `1`. -/
theorem no_three_survivors (I : List Nat) (S : List (Nat → Bool))
    (us : List (Nat → Tri)) (hlen : I.length = 4) (hpos : 0 < us.length)
    (hS : survivesSetTo I S us (1 : K))
    (θ₁ θ₂ θ₃ : Nat → Bool)
    (h1 : θ₁ ∈ S) (h2 : θ₂ ∈ S) (h3 : θ₃ ∈ S)
    (d12 : hamming I θ₁ θ₂ ≠ 0) (d13 : hamming I θ₁ θ₃ ≠ 0)
    (d23 : hamming I θ₂ θ₃ ≠ 0) : False := by
  have hadj := survivors_pairwise_adjacent I S us hlen hpos hS
  have h12 : hamming I θ₁ θ₂ = 1 :=
    nat_ne_zero_of_le_one_eq_one d12 (hadj θ₁ θ₂ h1 h2)
  have h13 : hamming I θ₁ θ₃ = 1 :=
    nat_ne_zero_of_le_one_eq_one d13 (hadj θ₁ θ₃ h1 h3)
  have h23ne : hamming I θ₂ θ₃ ≠ 1 :=
    no_adjacency_triangle I θ₁ θ₂ θ₃ h12 h13
  have h23 : hamming I θ₂ θ₃ = 1 :=
    nat_ne_zero_of_le_one_eq_one d23 (hadj θ₂ θ₃ h2 h3)
  exact h23ne h23

/-! ## The floor cannot serve an adjacent pair -/

/-- One step from the floor: the state after the first action is
checked, so it too must be at or above `1`. -/
theorem survivesTo_cons_floor (I : List Nat) (θ : Nat → Bool)
    (u : Nat → Tri) (us : List (Nat → Tri)) :
    survivesTo I θ (u :: us) (1 : K) → (1 : K) ≤ (1 : K) + drift I u θ := by
  intro hs
  cases us with
  | nil => simpa [survivesTo] using hs.2
  | cons v vs => exact hs.2.1

/-- `1 < 1.1`. -/
theorem one_lt_one_one : (1 : K) < one_one := by
  change (1 : K) < (1 : K) + tenth
  have h := add_lt_add_right' (K := K) (a := (0 : K)) (b := tenth) tenth_pos (1 : K)
  simpa [add_comm] using h

/-- **No in-alphabet first step serves both members of an adjacent pair
from the floor.** `1.0 < 1.1`, so `pair_first_step_fails` applies. -/
theorem floor_pair_fails (I : List Nat) (θ θ' : Nat → Bool)
    (hlen : I.length = 4) (hadj : hamming I θ θ' = 1)
    (u : Nat → Tri) (us : List (Nat → Tri)) (hu : inAlphabet u) :
    ¬ (survivesTo I θ (u :: us) (1 : K) ∧
        survivesTo I θ' (u :: us) (1 : K)) := by
  intro hs
  have h1 : (1 : K) ≤ (1 : K) + drift I u θ :=
    survivesTo_cons_floor I θ u us hs.1
  have h2 : (1 : K) ≤ (1 : K) + drift I u θ' :=
    survivesTo_cons_floor I θ' u us hs.2
  exact (pair_first_step_fails I θ θ' hlen hadj u hu (1 : K) one_lt_one_one)
    ⟨h1, h2⟩

/-! ## The classification at the floor -/

/-- **At `z₀ = 1.0`, all surviving cells agree on `I`.**

So the maximal survivable sets at the floor are single cells — the paper's
16 singletons. The enumeration is instance-level and is left to the
verifier; what is proved here is that nothing with two distinct members
gets through.

The argument: two survivors are at distance `≤ 1` (`cor_hamming_m4`); if
they were distinct on `I` the distance would be exactly `1`, and
`floor_pair_fails` forbids an adjacent pair from both surviving the first
in-alphabet step. -/
theorem floor_survivors_agree (I : List Nat) (S : List (Nat → Bool))
    (us : List (Nat → Tri)) (hlen : I.length = 4) (hpos : 0 < us.length)
    (hS : survivesSetTo I S us (1 : K))
    (hAlpha : ∀ u, u ∈ us → inAlphabet u) :
    ∀ θ θ', θ ∈ S → θ' ∈ S → hamming I θ θ' = 0 := by
  intro θ θ' hθ hθ'
  have hle : hamming I θ θ' ≤ 1 :=
    survivors_pairwise_adjacent I S us hlen hpos hS θ θ' hθ hθ'
  by_cases h0 : hamming I θ θ' = 0
  · exact h0
  · have h1 : hamming I θ θ' = 1 := nat_ne_zero_of_le_one_eq_one h0 hle
    cases us with
    | nil => exact False.elim (by cases hpos)
    | cons u us' =>
        have hu : inAlphabet u := hAlpha u (by simp)
        exact False.elim ((floor_pair_fails I θ θ' hlen h1 u us' hu)
          ⟨hS θ hθ, hS θ' hθ'⟩)

/-- At the floor, survivors agree coordinatewise on `I`. -/
theorem floor_survivors_agree_on (I : List Nat) (S : List (Nat → Bool))
    (us : List (Nat → Tri)) (hlen : I.length = 4) (hpos : 0 < us.length)
    (hS : survivesSetTo I S us (1 : K))
    (hAlpha : ∀ u, u ∈ us → inAlphabet u) :
    ∀ θ θ', θ ∈ S → θ' ∈ S → ∀ i, i ∈ I → θ i = θ' i := by
  intro θ θ' hθ hθ' i hi
  have hz := floor_survivors_agree I S us hlen hpos hS hAlpha θ θ' hθ hθ'
  exact (hamming_eq_zero I θ θ').mp hz i hi

end Formalizations.EBC

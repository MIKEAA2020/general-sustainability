/-
  Formalizations.EBC_Ladder_v2
  ============================

  **`prop:ladder`: the substitution, on the EBC side.**

  `EBC_Ladder` fixed the *shape* — set survivability stated as
  `survivesSetAt`, one in-alphabet policy of `L` actions keeping every
  member at or above the floor, which is P3's `SurvivableAdm M S k`
  verbatim. This module completes the cardinality facts in the form the
  value formula consumes them, and records why no `DetMDP` instance is
  needed.

  **On the instantiation question.** The paper's proof of `prop:ladder`
  (ll. 266–282) *invokes* the companion theory: "The companion theory's
  antichain formula makes the kernel value of a prior the maximal
  survivable-set mass it charges, and survivability is hereditary
  downward … so the value at the uniform prior on a support `S` is
  `max_{A ⊆ S, A survivable} |A|/|S|`." It applies that formula; it does
  not assert that the EBC ladder *is* an instance of `VfamAdm`. So the
  claim to formalize is **shape-equivalence, not type-identity**, and
  building a `DetMDP` over the sixteen cells whose `survK` is EBC's
  `survivesTo` would add mechanism without adding a theorem. The bridge
  is recorded as structural. See `lean_bridge_spec.md` §4.

  **The two facts.** Writing `M` for the largest number of
  pairwise-distinct cells a survivable subset can have:

  * at the floor `z₀ = 1.0`, `M = 1` — `EBC_Ladder.floor_survivable_all_agree`
    says all members agree on `I`;
  * above the edge, at any horizon `L ≥ 2`, `M ≤ 2` — every pair is
    Hamming-adjacent (`pairs_adjacent_above`) and no three members are
    pairwise distinct (**`no_three_distinct_above`**, below), so a
    survivable subset is a singleton or an adjacent pair.

  With the value `= M/|S|`, that is `1/|S|` at the edge and
  `min(1, 2/|S|)` above it — the paper's two rows, `|S|` symbolic, the
  `2^j` sizes and the ten numbers left to the verifier.
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
import Formalizations.EBC_Ladder
import Formalizations.RatArith

open Formalizations.EBC

namespace Formalizations.EBC

variable {K : Type} [OrdField K]

/-- **Above the edge, no three pairwise-distinct cells survive.**

Every pair in a surviving set is at Hamming distance `≤ 1`
(`pairs_adjacent_above`), so three pairwise-distinct members would be
pairwise at distance exactly `1`, which `lem:triangle`
(`no_adjacency_triangle`) forbids. Combined with
`floor_survivable_all_agree` (where every member agrees, so `M = 1`),
this is the whole content of "`M ≤ 2`". -/
theorem no_three_distinct_above (I : List Nat) (A : List (Nat → Bool)) (z0 : K)
    (hlen : I.length = 4) {L : Nat} (hL : 2 ≤ L)
    (hzhi : z0 ≤ one_one)
    (h : survivesSetAt I A z0 L)
    (θ₁ θ₂ θ₃ : Nat → Bool)
    (h1 : θ₁ ∈ A) (h2 : θ₂ ∈ A) (h3 : θ₃ ∈ A)
    (d12 : hamming I θ₁ θ₂ ≠ 0) (d13 : hamming I θ₁ θ₃ ≠ 0)
    (d23 : hamming I θ₂ θ₃ ≠ 0) : False := by
  have hadj := pairs_adjacent_above I A z0 hlen hL hzhi h
  have h12 : hamming I θ₁ θ₂ = 1 :=
    nat_ne_zero_of_le_one_eq_one d12 (hadj θ₁ θ₂ h1 h2)
  have h13 : hamming I θ₁ θ₃ = 1 :=
    nat_ne_zero_of_le_one_eq_one d13 (hadj θ₁ θ₃ h1 h3)
  have h23ne : hamming I θ₂ θ₃ ≠ 1 :=
    no_adjacency_triangle I θ₁ θ₂ θ₃ h12 h13
  have h23 : hamming I θ₂ θ₃ = 1 :=
    nat_ne_zero_of_le_one_eq_one d23 (hadj θ₂ θ₃ h2 h3)
  exact h23ne h23

/-- **Above the edge, a surviving subset is a singleton or a
Hamming-adjacent pair**: any two members either agree on `I` or differ in
exactly one coordinate, and there are at most two distinct ones.

This is the exact statement the value formula consumes: it makes the
maximal survivable subsets singletons and adjacent pairs, so
`max_{A ⊆ S} |A|` is `1` at the floor (`floor_survivable_all_agree`) and
`2` above the edge (`adjacent_pair_survives` shows `2` is attained). -/
theorem survivor_is_singleton_or_adjacent_pair (I : List Nat) (A : List (Nat → Bool))
    (z0 : K) (hlen : I.length = 4) {L : Nat} (hL : 2 ≤ L)
    (hzhi : z0 ≤ one_one)
    (h : survivesSetAt I A z0 L) :
    (∀ θ θ', θ ∈ A → θ' ∈ A → hamming I θ θ' = 0 ∨ hamming I θ θ' = 1) ∧
      (∀ θ₁ θ₂ θ₃, θ₁ ∈ A → θ₂ ∈ A → θ₃ ∈ A →
        hamming I θ₁ θ₂ = 0 ∨ hamming I θ₁ θ₃ = 0 ∨ hamming I θ₂ θ₃ = 0) := by
  constructor
  · intro θ θ' hθ hθ'
    have hle := pairs_adjacent_above I A z0 hlen hL hzhi h θ θ' hθ hθ'
    by_cases h0 : hamming I θ θ' = 0
    · exact Or.inl h0
    · exact Or.inr (nat_ne_zero_of_le_one_eq_one h0 hle)
  · intro θ₁ θ₂ θ₃ h1 h2 h3
    by_cases d12 : hamming I θ₁ θ₂ = 0
    · exact Or.inl d12
    · by_cases d13 : hamming I θ₁ θ₃ = 0
      · exact Or.inr (Or.inl d13)
      · by_cases d23 : hamming I θ₂ θ₃ = 0
        · exact Or.inr (Or.inr d23)
        · exact False.elim
            (no_three_distinct_above I A z0 hlen hL hzhi h θ₁ θ₂ θ₃ h1 h2 h3
              d12 d13 d23)

end Formalizations.EBC

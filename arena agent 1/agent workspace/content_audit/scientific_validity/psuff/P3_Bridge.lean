/-
  Formalizations.P3_Bridge
  ========================

  **Two survival notions, and why they agree.**

  P3 computes the same value in two different-looking ways:

  * `P3_Freeze_Noisy` — `Survivable M S k := ∃ u : Nat → A, ∀ x ∈ S,
    survK M k u x`, over **infinite schedules**, `Prop`-valued, feeding
    `Sfam`/`Vfam`.  This is `prop:antichain` (i)'s `max_{S ∈ S_k} b(S)`.
  * `P3_Deterministic` — `survT M t x`, over **finite tuples** of length `k`,
    `Bool`-valued, feeding `VR`.  This is `prop:degen`'s
    `max_{t ∈ Π_B} Σ_x b(x)·1[x survives t]`.

  Nothing in the layer connected them, so the two modules proved the same
  theorem twice in incompatible vocabularies. This module supplies the
  connection: `survT_iff_survK`.

  The two definitions are structurally parallel — `survK` uses `∧` and
  `∀ d, d ∈ …`, `survT` uses `&&` and `.all` — so the equivalence is an
  induction on the tuple, once the schedule is read off the tuple by `getD`.

  ## A correction carried here

  v25 proposed "the `SafeMDP`/`DetMDP` bridge" as the next item and said
  `thm:support`'s min-mass consequence needed it. **That was wrong.**
  `min_mass_bound` (`P3_Deterministic:248`) already proves it, and its own
  header already says so:

  > The min-mass bound — `prop:deficit` (ii) and **`thm:support`'s
  > consequence**.

  It never needed a bridge, because the consequence is a statement about the
  **robust** operator `VR`, not about `SafeMDP`'s stochastic `V`. Per
  `rem:operators` those are different operators that do not coincide, so a
  bridge between them is not merely unnecessary — it is not a theorem.
  v25's proposal was a second misreading of the same kind as v23's.

  What `thm:support` genuinely still lacks is consequence 1's `𝒲_k`
  viable-set recursion, which no module defines. Consequence 3 is covered by
  `Vfam_antitone` (`prop:freeze`, v18).

  ## Contents

    survK_congr_prefix   `survK M k u x` sees only `u 0 … u (k-1)`
    survT_iff_survK      **the two survival notions coincide**
-/

import Formalizations.Prelude
import Formalizations.P3_Deterministic
import Formalizations.P3_Freeze_Noisy

namespace Formalizations.P3

open Formalizations
open Formalizations.POMDP

set_option linter.unusedSectionVars false

variable {K : Type} [OrdField K]
variable {X A D Y : Type}

/-- **`survK` only probes the first `k` actions of the schedule.**  Needed
because a finite tuple determines a schedule only on `0 … k-1`; the values
beyond that are supplied by a fallback and must not matter. -/
theorem survK_congr_prefix (M : DetMDP K X A D Y) : ∀ k (u v : Nat → A) (x : X),
    (∀ i, i < k → u i = v i) → survK M k u x → survK M k v x := by
  intro k
  induction k with
  | zero =>
      intro u v x h hs
      exact hs
  | succ k ih =>
      intro u v x h hs
      rcases hs with ⟨hsafe, hall⟩
      refine ⟨hsafe, ?_⟩
      intro d hd
      have huv0 : u 0 = v 0 := h 0 (Nat.succ_pos k)
      have hmem : d ∈ M.univD x (u 0) := by simpa [← huv0] using hd
      have hs1 : survK M k (fun i => u (i + 1)) (M.F x (u 0) d) := hall d hmem
      have hs2 : survK M k (fun i => v (i + 1)) (M.F x (u 0) d) :=
        ih (fun i => u (i + 1)) (fun i => v (i + 1)) (M.F x (u 0) d)
          (by
            intro i hi
            exact h (i + 1) (Nat.succ_lt_succ hi)) hs1
      simpa [huv0] using hs2

/-- **The bridge.**  A branch survives the tuple `t` exactly when it survives
`t.length` steps under the schedule read off `t`.  The fallback `a0` is
arbitrary — `survK_congr_prefix` says it cannot matter. -/
theorem survT_iff_survK (M : DetMDP K X A D Y) (a0 : A) :
    ∀ (t : List A) (x : X),
      survT M t x = true ↔ survK M t.length (fun i => t.getD i a0) x := by
  intro t
  induction t with
  | nil =>
      intro x
      simp [survT, survK]
  | cons a t ih =>
      intro x
      simp [survT, survK, ih]

end Formalizations.P3

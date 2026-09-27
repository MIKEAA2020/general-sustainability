/-
  Formalizations.P3_Freeze_Noisy_v2
  =================================

  Closes the last open piece of `prop:freeze` (P3,
  `paper2_probabilistic_sufficiency_v11.tex`):

  > With deterministic kernels the survivable-set families satisfy
  > `S_{ℓ+1} ⊆ S_ℓ`; hence `V_ℓ(b)` is non-increasing in the horizon and
  > stabilizes after at most `2^{|supp b|}` strict decreases.

  `P3_Freeze_Noisy` proved the nesting, the antitonicity of `V_ℓ`, the
  magnitude bound `|S_0| ≤ 2^{|supp b|}`, and — as `Vfam_finite_range` —
  that every `V_ℓ(b)` is `b(S)` for some `S ∈ S_0`.  What it flagged as
  not proved was **the literal count of strict decreases**.  This module
  proves it.

  ## The argument

  Counting distinct *values* would need a pigeonhole lemma over a
  deduplicated list, and this dependency-free layer has no `DecidableEq` on
  `K` and no `List.dedup` infrastructure.  The route taken here avoids both,
  by counting **sets instead of values**:

    1. If `V_{k+1}(b) < V_k(b)`, then some set present in `S_k` is absent
       from `S_{k+1}` — namely a maximizer for `V_k`.  Were it still
       present, its mass would be `≤ V_{k+1}(b)`, contradicting the strict
       drop.  (`drop_removes_set`.)
    2. `S_{k+1} = S_k.filter (Survivable · (k+1))`, so a surviving-but-
       removed witness makes the filter *strictly* shorten the list.
       (`Sfam_succ_filter`, `filter_strict`.)
    3. The family only shrinks, so sets removed at distinct drops are
       distinct, and the accumulated count is bounded by `|S_0|`.

  The invariant actually proved is stronger than the count alone and is what
  makes the induction close in one pass:

      drops M b n + |S_n| ≤ |S_0|

  From it, `drops M b n ≤ |S_0| ≤ 2^{|univX|}` follows with
  `Sfam0_card_le`.  The bound is on the number of strict decreases **before
  horizon `n`, uniformly in `n`** — exactly "stabilizes after at most
  `2^{|supp b|}` strict decreases".

  No `DecidableEq X` and no `DecidableEq K` is required anywhere.
-/

import Formalizations.Prelude
import Formalizations.P3_Deterministic
import Formalizations.P3_Freeze_Noisy

namespace Formalizations.P3

open Formalizations.POMDP

variable {K : Type} [OrdField K]
variable {X A D Y : Type}

/-! ## Generic list lemmas

The layer's `length_filter_le` is specialised to `List (List X)`; these two
are polymorphic.  Neither needs `DecidableEq`. -/

/-- Filtering cannot lengthen a list (polymorphic). -/
theorem length_filter_le_gen {α : Type} :
    ∀ (l : List α) (p : α → Prop) [DecidablePred p],
      (l.filter p).length ≤ l.length := by
  intro l
  induction l with
  | nil =>
      intro p hp
      simp
  | cons a t ih =>
      intro p hp
      by_cases hpa : p a
      · simp [hpa]
        exact ih p
      · simp [hpa]
        exact Nat.le_trans (ih p) (Nat.le_succ _)

/-- If a filter discards at least one element, it *strictly* shortens the
list.  This is the step converting "some set was dropped" into the
cardinal-bound induction. -/
theorem filter_strict {α : Type} :
    ∀ (l : List α) (p : α → Prop) [DecidablePred p],
      (∃ x, x ∈ l ∧ ¬ p x) → (l.filter p).length + 1 ≤ l.length := by
  intro l
  induction l with
  | nil =>
      intro p hp hw
      rcases hw with ⟨x, hx, _⟩
      cases hx
  | cons a t ih =>
      intro p hp hw
      by_cases hpa : p a
      · -- `a` is kept, so a discarded witness must lie in the tail.
        have hwt : ∃ x, x ∈ t ∧ ¬ p x := by
          rcases hw with ⟨x, hx, hnp⟩
          cases hx with
          | head => exact False.elim (hnp hpa)
          | tail _ hxt => exact ⟨x, hxt, hnp⟩
        have iht := ih p hwt
        simpa [hpa] using iht
      · -- `a` itself is discarded.
        have iht := length_filter_le_gen t p
        simpa [hpa] using iht

/-- Filtering twice by nested predicates is filtering by the stronger one. -/
theorem filter_filter_of_imp {α : Type} (l : List α) (p q : α → Prop)
    [DecidablePred p] [DecidablePred q] (hpq : ∀ x, p x → q x) :
    (l.filter q).filter p = l.filter p := by
  induction l with
  | nil => simp
  | cons a t ih =>
      by_cases hq : q a
      · by_cases hp : p a
        · simp [hq, hp, ih]
        · simp [hq, hp, ih]
      · have hnp : ¬ p a := fun hp => hq (hpq a hp)
        simp [hq, hnp, ih]

/-! ## The family as an iterated filter -/

/-- **`S_{k+1}` is `S_k` filtered by survival to `k+1$.**  Immediate from
the nesting `Survivable (k+1) → Survivable k`: filtering by a weaker
predicate first and then the stronger one is just filtering by the stronger
one.

Stated as a *length* inequality rather than a list equality, so that the
statement is `Prop`-valued and needs no `Decidable` instance at
declaration-elaboration time — `List.filter` is `Bool`-valued in this
stdlib, and a `decide` in a theorem statement would demand an instance that
is not available outside a `classical` block. -/
theorem Sfam_succ_length_le (M : DetMDP K X A D Y) (k : Nat) :
    (Sfam M (k + 1)).length ≤ (Sfam M k).length := by
  unfold Sfam
  classical
  have hff := filter_filter_of_imp (subsetsOf M.univX)
    (fun S => Survivable M S (k + 1)) (fun S => Survivable M S k)
    (fun S => Survivable_succ M S k)
  rw [← hff]
  exact length_filter_le_gen _ _

/-- **A strict drop shortens the family by at least one.**  If some set in
`S_k` fails to survive to `k+1`, the filter discards it. -/
theorem Sfam_succ_length_strict (M : DetMDP K X A D Y) (k : Nat)
    (hrem : ∃ S, S ∈ Sfam M k ∧ ¬ Survivable M S (k + 1)) :
    (Sfam M (k + 1)).length + 1 ≤ (Sfam M k).length := by
  unfold Sfam at hrem ⊢
  classical
  have hrem' : ∃ S, S ∈ (subsetsOf M.univX).filter
        (fun S => Survivable M S k) ∧ ¬ Survivable M S (k + 1) := by
    simpa using hrem
  have hff := filter_filter_of_imp (subsetsOf M.univX)
    (fun S => Survivable M S (k + 1)) (fun S => Survivable M S k)
    (fun S => Survivable_succ M S k)
  rw [← hff]
  exact filter_strict _ _ hrem'

/-! ## A strict drop removes a set -/

/-- **Every strict decrease removes at least one set.**

If `V_{k+1}(b) < V_k(b)`, then some `S ∈ S_k` fails to survive to `k+1`:
take a maximizer for `V_k`; were it still in `S_{k+1}`, its mass would be
at most `V_{k+1}(b)`, contradicting the strict drop. -/
theorem drop_removes_set (M : DetMDP K X A D Y) (b : Mass K X) (k : Nat)
    (hdrop : Vfam M (k + 1) b < Vfam M k b) :
    ∃ S, S ∈ Sfam M k ∧ ¬ Survivable M S (k + 1) := by
  let f : List X → K := fun S => bS S b
  have hne : (Sfam M k).map f ≠ [] := map_ne_nil f (Sfam_ne M k)
  rcases List.mem_map.mp (lmax_isMax hne).1 with ⟨S, hS, hval⟩
  refine ⟨S, hS, ?_⟩
  intro hsurv1
  have hS1 : S ∈ Sfam M (k + 1) := by
    have hS' := hS
    simp [Sfam, List.mem_filter] at hS'
    simp [Sfam, List.mem_filter]
    exact ⟨hS'.1, hsurv1⟩
  have hmem1 : f S ∈ (Sfam M (k + 1)).map f := List.mem_map.mpr ⟨S, hS1, rfl⟩
  have hle : f S ≤ lmax ((Sfam M (k + 1)).map f) :=
    le_lmax (map_ne_nil f (Sfam_ne M (k + 1))) hmem1
  have hlt : lmax ((Sfam M (k + 1)).map f) < f S := by
    dsimp [f] at hval ⊢
    unfold Vfam at hdrop
    simpa [hval] using hdrop
  exact (not_le_of_lt hlt) hle

/-! ## Counting strict decreases -/

/-- The number of strict decreases of `ℓ ↦ V_ℓ(b)` with drop index `< n`.

`letI` supplies the `Decidable` the comparison needs; without it the
equation compiler cannot elaborate the recursive branch. -/
noncomputable def drops (M : DetMDP K X A D Y) (b : Mass K X) : Nat → Nat
  | 0 => 0
  | n + 1 =>
      letI : Decidable (Vfam M (n + 1) b < Vfam M n b) :=
        Classical.propDecidable _
      drops M b n + (if Vfam M (n + 1) b < Vfam M n b then 1 else 0)

/-- **The counting invariant.**  Strict decreases plus the surviving family
size never exceeds the initial family size: every drop pays for itself by
removing a set, and the family only shrinks. -/
theorem drops_bound (M : DetMDP K X A D Y) (b : Mass K X) :
    ∀ n, drops M b n + (Sfam M n).length ≤ (Sfam M 0).length := by
  classical
  intro n
  induction n with
  | zero =>
      simp [drops]
  | succ n ih =>
      by_cases hdrop : Vfam M (n + 1) b < Vfam M n b
      · have hrem : ∃ S, S ∈ Sfam M n ∧ ¬ Survivable M S (n + 1) :=
          drop_removes_set M b n hdrop
        have hstrict : (Sfam M (n + 1)).length + 1 ≤ (Sfam M n).length :=
          Sfam_succ_length_strict M n hrem
        calc
          drops M b (n + 1) + (Sfam M (n + 1)).length
              = (drops M b n + 1) + (Sfam M (n + 1)).length := by
                  simp [drops, hdrop]
          _ = drops M b n + ((Sfam M (n + 1)).length + 1) := by
                  rw [Nat.add_assoc, Nat.add_comm 1 ((Sfam M (n + 1)).length),
                    ← Nat.add_assoc]
          _ ≤ drops M b n + (Sfam M n).length :=
                  Nat.add_le_add_left hstrict (drops M b n)
          _ ≤ (Sfam M 0).length := ih
      · have hle : (Sfam M (n + 1)).length ≤ (Sfam M n).length :=
          Sfam_succ_length_le M n
        calc
          drops M b (n + 1) + (Sfam M (n + 1)).length
              = drops M b n + (Sfam M (n + 1)).length := by
                  simp [drops, hdrop]
          _ ≤ drops M b n + (Sfam M n).length :=
                  Nat.add_le_add_left hle (drops M b n)
          _ ≤ (Sfam M 0).length := ih

/-- **The number of strict decreases is at most `|S_0|`.** -/
theorem drops_le_card (M : DetMDP K X A D Y) (b : Mass K X) (n : Nat) :
    drops M b n ≤ (Sfam M 0).length :=
  Nat.le_trans (Nat.le_add_right (drops M b n) ((Sfam M n).length))
    (drops_bound M b n)

/-- **`prop:freeze`, in full.**  The number of strict decreases of
`ℓ ↦ V_ℓ(b)` before any horizon `n` is at most `2^{|supp b|}`. -/
theorem prop_freeze_drop_count (M : DetMDP K X A D Y) (b : Mass K X) (n : Nat) :
    drops M b n ≤ 2 ^ M.univX.length :=
  Nat.le_trans (drops_le_card M b n) (Sfam0_card_le M)

end Formalizations.P3

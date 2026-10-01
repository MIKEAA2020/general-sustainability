/-
  Formalizations.P3_Antichain_v2
  ==============================

  Closes `prop:antichain` (ii):

  > (ii) the alpha-vectors are exactly the indicators of the maximal
  >      elements of `S_k` in the componentwise order.

  `P3_Antichain` (v20) supplied the order vocabulary and proved (iii) — the
  maximal elements form an antichain — but left (ii) open, diagnosing the
  blocker as: *every `S ∈ S_k` is contained in a maximal `T ∈ S_k`*, plus
  the `lsum` rearrangement needed to turn "maximal by inclusion" into "the
  value is attained there".  Both are supplied here.

  ## The infrastructure that turned out to exist

  Probing showed this layer carries `List.erase` and its length/nodup
  lemmas — but they require `[BEq α] [LawfulBEq α]`, not `[DecidableEq α]`.
  Both instances derive from `DecidableEq`, so `[DecidableEq X]` suffices.
  What is genuinely **absent** is `List.mem_erase`, `List.dedup`,
  `List.Subperm`, `List.perm_ext`, `List.length_le_of_sublist`.  So the
  permutation route to "same elements ⟹ same `lsum`" is unavailable, and
  the `erase` route needs `mem_erase_iff` proved by hand.  That is the
  first lemma below, and it is the price of the missing stdlib.

  ## Contents

    mem_erase_iff          characterisation of `x ∈ l.erase a` (absent here)
    lsum_erase_mem         `lsum (l.map f) = f a + lsum ((l.erase a).map f)`
    lsum_eq_of_mem_iff     **same elements + Nodup ⟹ same lsum**
    subsetsOf_subset       every member of `subsetsOf l` is a sublist of `l`
    subsetsOf_nodup        every member of `subsetsOf l` is Nodup if `l` is
    bS_mono_of_subset      `S ⊆ T ⟹ b(S) ≤ b(T)` — the domination engine
    lift_maximal           lifting a maximum from `rest` to `A :: rest`
    exists_maximal_above   **every element sits below a maximal one**
    Pruned                 the witness family pruned to its maximal elements
    Vfam_prune_eq          **(ii): pruning does not change the value**

  Note on `exists_maximal_above`: the proof is by induction on the family,
  *not* by a termination or `Nat`-maximum argument.  At each `A :: rest`
  the head is handled by asking whether anything in `rest` contains `A`; if
  so, recurse into `rest` and lift the result, and if not, `A` is itself
  maximal.  This avoids well-founded recursion entirely.
-/

import Formalizations.Prelude
import Formalizations.P3_Deterministic
import Formalizations.P3_Freeze_Noisy
import Formalizations.P3_Antichain

namespace Formalizations.P3

open Formalizations
open Formalizations.POMDP

set_option linter.unusedSectionVars false

variable {K : Type} [OrdField K]
variable {X A D Y : Type}
variable [DecidableEq X]

/-! ## `erase` and `lsum` -/

/-- **Characterisation of membership after `erase`.**  `List.mem_erase` does
not exist in this stdlib; this is it.  Needs `Nodup`. -/
theorem mem_erase_iff : ∀ (l : List X), l.Nodup → ∀ (a x : X),
    x ∈ l.erase a ↔ x ∈ l ∧ x ≠ a := by
  intro l hl
  induction l with
  | nil =>
      intro a x
      simp
  | cons b t ih =>
      intro a x
      have hnod := List.nodup_cons.mp hl
      by_cases hba : b = a
      · subst a
        rw [List.erase_cons_head]
        constructor
        · intro hxt
          refine ⟨List.mem_cons_of_mem b hxt, ?_⟩
          intro hxb
          subst x
          exact hnod.1 hxt
        · intro h
          rcases (by simpa using h.1 : x = b ∨ x ∈ t) with hxb | hxt
          · exact False.elim (h.2 hxb)
          · exact hxt
      · have hbne : ¬(b == a) = true := by simp [hba]
        rw [List.erase_cons_tail hbne]
        have iht := ih hnod.2 a x
        constructor
        · intro hx
          rcases (by simpa using hx : x = b ∨ x ∈ t.erase a) with hxb | hxte
          · subst x
            exact ⟨List.mem_cons_self, hba⟩
          · have hx' := iht.mp hxte
            exact ⟨List.mem_cons_of_mem b hx'.1, hx'.2⟩
        · intro h
          rcases (by simpa using h.1 : x = b ∨ x ∈ t) with hxb | hxt
          · subst x
            exact List.mem_cons_self
          · exact List.mem_cons_of_mem b (iht.mpr ⟨hxt, h.2⟩)

/-- Removing a present element from a `Nodup` list splits its `lsum`. -/
theorem lsum_erase_mem (f : X → K) : ∀ (l : List X), l.Nodup → ∀ (a : X),
    a ∈ l → lsum (l.map f) = f a + lsum ((l.erase a).map f) := by
  intro l hl
  induction l with
  | nil =>
      intro a ha
      cases ha
  | cons b t ih =>
      intro a ha
      have hnod := List.nodup_cons.mp hl
      by_cases hba : b = a
      · subst a
        rw [List.erase_cons_head]
        rfl
      · have hbne : ¬(b == a) = true := by simp [hba]
        rw [List.erase_cons_tail hbne]
        have hat : a ∈ t := by
          rcases (by simpa using ha : a = b ∨ a ∈ t) with hab | hat
          · exact False.elim (hba hab.symm)
          · exact hat
        change f b + lsum (t.map f) = f a + (f b + lsum ((t.erase a).map f))
        rw [ih hnod.2 a hat]
        rw [← add_assoc, add_comm (f b) (f a), add_assoc]

/-- **Two `Nodup` lists with the same elements have the same `lsum`.**

This is the lemma identified in v20 as the missing ingredient. -/
theorem lsum_eq_of_mem_iff (f : X → K) :
    ∀ (l₁ l₂ : List X), l₁.Nodup → l₂.Nodup →
      (∀ x, x ∈ l₁ ↔ x ∈ l₂) → lsum (l₁.map f) = lsum (l₂.map f) := by
  intro l₁
  induction l₁ with
  | nil =>
      intro l₂ hl₁ hl₂ hiff
      have hempty : l₂ = [] := by
        cases l₂ with
        | nil => rfl
        | cons a t =>
            have hmem : a ∈ ([] : List X) := (hiff a).mpr (List.mem_cons_self)
            cases hmem
      simp [hempty]
  | cons a t ih =>
      intro l₂ hl₁ hl₂ hiff
      have hnod₁ := List.nodup_cons.mp hl₁
      have hal₂ : a ∈ l₂ := (hiff a).mp (List.mem_cons_self)
      have herase := lsum_erase_mem f l₂ hl₂ a hal₂
      have htarget : lsum (t.map f) = lsum ((l₂.erase a).map f) := by
        apply ih
        · exact hnod₁.2
        · exact List.Nodup.erase a hl₂
        · intro x
          constructor
          · intro hxt
            have hxl₂ : x ∈ l₂ := (hiff x).mp (List.mem_cons_of_mem a hxt)
            have hxne : x ≠ a := by
              intro hxa
              subst x
              exact hnod₁.1 hxt
            exact (mem_erase_iff l₂ hl₂ a x).mpr ⟨hxl₂, hxne⟩
          · intro hxe
            have hx' := (mem_erase_iff l₂ hl₂ a x).mp hxe
            have hxat : x ∈ a :: t := (hiff x).mpr hx'.1
            rcases (by simpa using hxat : x = a ∨ x ∈ t) with hxa | hxt
            · exact False.elim (hx'.2 hxa)
            · exact hxt
      calc
        lsum ((a :: t).map f) = f a + lsum (t.map f) := rfl
        _ = f a + lsum ((l₂.erase a).map f) := by rw [htarget]
        _ = lsum (l₂.map f) := herase.symm

/-! ## `subsetsOf` -/

/-- Every member of `subsetsOf l` is a sublist of `l`. -/
theorem subsetsOf_subset : ∀ (l : List X) (S : List X), S ∈ subsetsOf l →
    subsetOf S l := by
  intro l
  induction l with
  | nil =>
      intro S hS
      have hS' : S = [] := by simpa [subsetsOf] using hS
      subst S
      intro x hx
      cases hx
  | cons x xs ih =>
      intro S hS
      simp [subsetsOf] at hS
      rcases hS with hS | hS
      · intro y hy
        exact List.mem_cons_of_mem x (ih S hS y hy)
      · rcases hS with ⟨T, hT, rfl⟩
        intro y hy
        rcases (by simpa using hy : y = x ∨ y ∈ T) with rfl | hyT
        · exact List.mem_cons_self
        · exact List.mem_cons_of_mem x (ih T hT y hyT)

/-- Members of `subsetsOf l` are `Nodup` when `l` is. -/
theorem subsetsOf_nodup : ∀ (l : List X), l.Nodup →
    ∀ S, S ∈ subsetsOf l → S.Nodup := by
  intro l hl
  induction l with
  | nil =>
      intro S hS
      have hS' : S = [] := by simpa [subsetsOf] using hS
      simp [hS']
  | cons x xs ih =>
      intro S hS
      have hnod := List.nodup_cons.mp hl
      simp [subsetsOf] at hS
      rcases hS with hS | hS
      · exact ih hnod.2 S hS
      · rcases hS with ⟨T, hT, rfl⟩
        exact List.nodup_cons.mpr ⟨by
          intro hxT
          exact hnod.1 (subsetsOf_subset xs T hT x hxT), ih hnod.2 T hT⟩

theorem mem_filter_mem (p : X → Bool) : ∀ {l : List X} {x : X},
    x ∈ l.filter p → x ∈ l := by
  intro l
  induction l with
  | nil =>
      intro x hx
      cases hx
  | cons a t ih =>
      intro x hx
      by_cases hp : p a = true
      · rw [List.filter_cons_of_pos hp] at hx
        rcases List.mem_cons.mp hx with hxa | hx
        · subst x
          exact List.mem_cons_self
        · exact List.mem_cons_of_mem a (ih hx)
      · rw [List.filter_cons_of_neg hp] at hx
        exact List.mem_cons_of_mem a (ih hx)

theorem nodup_filter (p : X → Bool) : ∀ (l : List X), l.Nodup → (l.filter p).Nodup := by
  intro l hl
  induction l with
  | nil => simp
  | cons a t ih =>
      have hnod := List.nodup_cons.mp hl
      by_cases hp : p a = true
      · rw [List.filter_cons_of_pos hp]
        exact List.nodup_cons.mpr ⟨by
          intro hx
          exact hnod.1 (mem_filter_mem p hx), ih hnod.2⟩
      · rw [List.filter_cons_of_neg hp]
        exact ih hnod.2

/-! ## The domination engine -/

/-- **A subset of a nonnegative mass has no more mass than its superset.**

`b(S) ≤ b(T)` whenever `S ⊆ T`.  Route: `S` and `T.filter (· ∈ S)` are two
`Nodup` lists with the same elements, so `lsum_eq_of_mem_iff` identifies
their sums; then `lsum_filter_le` bounds the filtered sum by the full one. -/
theorem bS_mono_of_subset (b : Mass K X) : ∀ (S T : List X), S.Nodup →
    T.Nodup → subsetOf S T → bS S b ≤ bS T b := by
  intro S T hSn hTn hST
  let p : X → Bool := fun x => decide (x ∈ S)
  have heq : lsum ((T.filter p).map b.f) = lsum (S.map b.f) := by
    apply lsum_eq_of_mem_iff b.f
    · exact nodup_filter p T hTn
    · exact hSn
    · intro x
      have hfilt : x ∈ T.filter p ↔ x ∈ T ∧ x ∈ S := by simp [p]
      rw [hfilt]
      exact ⟨fun h => h.2, fun h => ⟨hST x h, h⟩⟩
  have hle := lsum_filter_le b.f b.nonneg T p
  unfold bS
  rw [← heq]
  exact hle

/-! ## Existence of maximal elements -/

/-- **Lifting a maximum from `rest` to `A :: rest`.**  Given `T` maximal in
`rest` and above `S`, either `A` dominates `T` — in which case `A` is maximal
in the enlarged family — or it does not, and `T` remains maximal. -/
theorem lift_maximal (A : List X) (rest : List (List X)) (S T : List X)
    (hTmem : T ∈ rest) (hTmax : MaximalIn rest T) (hST : subsetOf S T) :
    ∃ T', MaximalAbove (A :: rest) S T' := by
  classical
  by_cases hTA : subsetOf T A
  · refine ⟨A, List.mem_cons_self, subsetOf_trans hST hTA, ?_⟩
    refine ⟨List.mem_cons_self, ?_⟩
    intro U hU hAU
    rcases (by simpa using hU : U = A ∨ U ∈ rest) with hUA | hUrest
    · subst U
      exact subsetOf_refl A
    · exact subsetOf_trans (hTmax.2 U hUrest (subsetOf_trans hTA hAU)) hTA
  · refine ⟨T, List.mem_cons_of_mem A hTmem, hST, ?_⟩
    refine ⟨List.mem_cons_of_mem A hTmem, ?_⟩
    intro U hU hTU
    rcases (by simpa using hU : U = A ∨ U ∈ rest) with hUA | hUrest
    · subst U
      exact False.elim (hTA hTU)
    · exact hTmax.2 U hUrest hTU

/-- **Every element of a finite family sits below a maximal one.**

This is the fact v20 identified as the blocker.  The proof is a plain
induction on the family: for the head `A`, ask whether anything in `rest`
contains `A`; if so recurse into `rest` and lift, and if not `A` is already
maximal.  No termination measure and no `Nat`-maximum is needed. -/
theorem exists_maximal_above : ∀ (l : List (List X)) (S : List X), S ∈ l →
    ∃ T, MaximalAbove l S T := by
  intro l
  induction l with
  | nil =>
      intro S hS
      cases hS
  | cons A rest ih =>
      intro S hS
      classical
      rcases (by simpa using hS : S = A ∨ S ∈ rest) with hSA | hSrest
      · subst S
        by_cases hEx : ∃ U, U ∈ rest ∧ subsetOf A U
        · rcases hEx with ⟨U, hUmem, hAU⟩
          rcases ih U hUmem with ⟨T, hTmem, hUT, hTmax⟩
          exact lift_maximal A rest A T hTmem hTmax (subsetOf_trans hAU hUT)
        · refine ⟨A, List.mem_cons_self, subsetOf_refl A, ?_⟩
          refine ⟨List.mem_cons_self, ?_⟩
          intro U hU hAU
          rcases (by simpa using hU : U = A ∨ U ∈ rest) with hUA | hUrest
          · subst U
            exact subsetOf_refl A
          · exact False.elim (hEx ⟨U, hUrest, hAU⟩)
      · rcases ih S hSrest with ⟨T, hTmem, hST, hTmax⟩
        exact lift_maximal A rest S T hTmem hTmax hST

/-! ## Pruning the witness family -/

/-- The witness family pruned to its **maximal** elements. -/
noncomputable def Pruned (M : DetMDP K X A D Y) (k : Nat) : List (List X) := by
  classical
  exact (Sfam M k).filter (fun S => decide (MaximalIn (Sfam M k) S))

theorem Pruned_mem (M : DetMDP K X A D Y) (k : Nat) {S : List X} :
    S ∈ Pruned M k ↔ S ∈ Sfam M k ∧ MaximalIn (Sfam M k) S := by
  simp [Pruned]

/-- The pruned family is inhabited. -/
theorem Pruned_ne (M : DetMDP K X A D Y) (k : Nat) : Pruned M k ≠ [] := by
  unfold Pruned
  classical
  apply ne_nil_of_exists_mem
  rcases exists_mem_of_ne_nil (Sfam_ne M k) with ⟨S, hS⟩
  rcases exists_maximal_above (Sfam M k) S hS with ⟨T, hTmem, hST, hTmax⟩
  exact ⟨T, by simp [hTmax.1, hTmax]⟩

/-- Every member of the unpruned family is in `subsetsOf univX`, hence
`Nodup`. -/
theorem Sfam_mem_nodup (M : DetMDP K X A D Y) (k : Nat) {S : List X}
    (hS : S ∈ Sfam M k) : S.Nodup := by
  have hS' := hS
  simp [Sfam, List.mem_filter] at hS'
  exact subsetsOf_nodup M.univX M.univX_nodup S hS'.1

/-- **Pruning cannot decrease the value** — the pruned family is a
sub-family.  This is `prop:antichain` (ii), direction (⊆): a non-maximal
witness never raises the maximum. -/
theorem Vfam_prune_ge (M : DetMDP K X A D Y) (b : Mass K X) (k : Nat) :
    lmax ((Pruned M k).map (fun S => bS S b)) ≤ Vfam M k b := by
  unfold Vfam
  apply lmax_le_lmax_of_subset (map_ne_nil (fun S => bS S b) (Pruned_ne M k))
  intro z hz
  rcases List.mem_map.mp hz with ⟨S, hS, rfl⟩
  exact List.mem_map.mpr ⟨S, ((Pruned_mem M k).mp hS).1, rfl⟩

/-- **Pruning cannot increase the value** — every witness is dominated by a
maximal one.  This is `prop:antichain` (ii), direction (⊇). -/
theorem Vfam_prune_le (M : DetMDP K X A D Y) (b : Mass K X) (k : Nat) :
    Vfam M k b ≤ lmax ((Pruned M k).map (fun S => bS S b)) := by
  unfold Vfam
  apply lmax_le (map_ne_nil (fun S => bS S b) (Sfam_ne M k))
  intro z hz
  rcases List.mem_map.mp hz with ⟨S, hS, rfl⟩
  rcases exists_maximal_above (Sfam M k) S hS with ⟨T, hTmem, hST, hTmax⟩
  have hle : bS S b ≤ bS T b :=
    bS_mono_of_subset b S T (Sfam_mem_nodup M k hS)
      (Sfam_mem_nodup M k hTmax.1) hST
  have hTpruned : T ∈ Pruned M k := (Pruned_mem M k).mpr ⟨hTmax.1, hTmax⟩
  exact le_trans hle (le_lmax (map_ne_nil (fun S => bS S b) (Pruned_ne M k))
    (List.mem_map.mpr ⟨T, hTpruned, rfl⟩))

/-- **`prop:antichain` (ii).**  The value is unchanged by pruning the
witness family to its maximal elements: the alpha-vectors are exactly the
indicators of the maximal survivable sets. -/
theorem Vfam_prune_eq (M : DetMDP K X A D Y) (b : Mass K X) (k : Nat) :
    Vfam M k b = lmax ((Pruned M k).map (fun S => bS S b)) :=
  le_antisymm (Vfam_prune_le M b k) (Vfam_prune_ge M b k)

end Formalizations.P3

/-
  Formalizations.P3_FeedbackValue
  ===============================

  **The value side of `thm:support` consequence 1, for the class the paper
  actually names.**

  v28 established, from the text, that consequence 1 is a statement about
  `Π_seq` — `def:value`'s "class of all sequential policies" — i.e. about
  the **feedback** recursion `Wmem`, not about the blind `Wblind` that
  `survT` / `survK` / `VR` implement. v28 closed the *set* side
  (`Wmem_iff_feedback`) and flagged the *value* side as missing: `VR` is a
  maximum over action **tuples**, and consequence 1 needs a maximum over
  **policies**.

  This module supplies it, and does so the way the paper itself does.

  ## How a feedback value is defined without quantifying over policies

  `prop:antichain` (i) states the value as a maximum over *sets*:

  > `V_k(b) = max_{S ∈ 𝒮_k} b(S)`, where `𝒮_k` is the family of subsets of
  > the support jointly survivable by one admissible class-element
  > (sequence **or policy**).

  That is the right definition here, and it is finite. Under deterministic
  kernels a branch's survival under a fixed policy is a deterministic
  event, so the mass a policy saves is exactly `b(S_π)` for
  `S_π = {x : x survives π}`, and maximizing over policies is maximizing
  over the jointly-survivable sets. Replacing "survivable by a schedule"
  (`Survivable`, feeding `Sfam`/`Vfam` in `P3_Freeze_Noisy`) by "survivable
  by a policy" (`Wmem`) turns the blind family value into the feedback
  family value. Nothing else changes — which is why the construction
  mirrors `Sfam`/`Vfam` line for line.

  So `VFb` is *not* an ad-hoc substitute for the paper's value: it is
  `prop:antichain` (i) read for the feedback class, and
  `prop:antichain` (i) is the paper's own route from sets to values.

  ## What is proved

    `VFb M k b = totalD M b  ⟺  Wmem M k (supp b)`      consequence 1
    `¬ Wmem ⟹ mn ≤ totalD − VFb`                         consequence 2
    `VFb` non-increasing in `k`                          consequence 3

  with `supp(b) = {x ∈ univX : b(x) ≠ 0}`. Under the normalization
  `totalD M b = 1` the first line reads exactly
  `V_k(b) = 1 ⟺ supp(b) ∈ 𝒲_k`.

  The forward direction is by a strict argument, not by a deficit bound:
  if `supp(b) ∉ 𝒲_k` then *every* jointly-survivable set misses a branch
  of **strictly positive** mass, so each `b(S)` is strictly below the
  total, and a maximum of finitely many strict inequalities is strict
  (`lmax_lt`, via `lmax_isMax`). This needs no uniform positive lower
  bound on the branch masses — only `b(x) ≥ 0` and `b(x) ≠ 0` on the
  support, both of which `Mass` supplies.

  ## Honest scope

  * `VFb` is a **definition** of the feedback value, exactly as `VR` is a
    definition of the blind survived-mass value and `Vfam` of the blind
    family value. The content is the three consequences, not the formula.
  * The maximum runs over subsets of `M.univX`, not of `supp(b)`; states
    outside the support carry zero mass and do not affect the value.
  * This module says nothing about the **stochastic** (expectation)
    operator. `rem:operators` distinguishes it from the robust operator
    this layer models, and they do not coincide in general.

  ## Contents

    suppPred, suppList          the support, as a predicate and as a list
    Wmem_empty, Wmem_downward   structural facts about the feedback family
    survPol_mono, Wmem_mono     horizon nesting (prop:freeze's hypothesis)
    lsum_mem_subsetsOf_le       a sublist of nonnegative terms sums to less
    lsum_subset_add_le          …and leaves room for a term outside it
    SfamFB, VFb                 the feedback family and its value
    VFb_le_totalD               the value never exceeds the total mass
    VFb_eq_total_of_Wmem        consequence 1, `⟸`
    VFb_min_mass_bound          consequence 2
    VFb_antitone                consequence 3
    VFb_lt_total_of_not_Wmem    consequence 1, `⟹`, strictly
    VFb_eq_total_iff_Wmem       **consequence 1**
-/

import Formalizations.Prelude
import Formalizations.P3_Deterministic
import Formalizations.P3_Freeze_Noisy
import Formalizations.P3_Bridge
import Formalizations.P3_Viable
import Formalizations.P3_Feedback

namespace Formalizations.P3

open Formalizations
open Formalizations.POMDP

set_option linter.unusedSectionVars false

variable {K : Type} [OrdField K]
variable {X A D Y : Type}

/-! ## Arithmetic and list helpers the layer does not yet carry -/

/-- `a ≤ a + b` when `b` is nonnegative. -/
theorem le_add_of_nonneg_right' {a b : K} (hb : 0 ≤ b) : a ≤ a + b := by
  calc
    a = a + 0 := by rw [add_zero]
    _ ≤ a + b := add_le_add_left hb a

/-- `a < a + b` when `b` is **strictly** positive.  The layer has no
`lt_add_of_pos_right`; this is it, proved by cancellation. -/
theorem lt_add_of_pos_right {a b : K} (hb : 0 < b) : a < a + b := by
  constructor
  · exact le_add_of_nonneg_right' hb.1
  · intro hle
    have h1 : (a + b) + -a ≤ a + -a := add_le_add_right hle (-a)
    have h2 : a + b + -a ≤ 0 := by simpa [add_neg_cancel] using h1
    have heq : a + b + -a = b := by
      calc
        a + b + -a = a + -a + b := add_right_comm a b (-a)
        _ = 0 + b := by rw [add_neg_cancel]
        _ = b := by rw [zero_add]
    exact hb.2 (by simpa [heq] using h2)

/-- Nonnegative and nonzero is strictly positive. -/
theorem pos_of_nonneg_of_ne {a : K} (h0 : 0 ≤ a) (hne : a ≠ 0) : 0 < a :=
  ⟨h0, fun ha0 => hne (le_antisymm ha0 h0)⟩

/-- A maximum of finitely many values, each strictly below `c`, is strictly
below `c`.  Immediate from `lmax_isMax`: the maximum is attained. -/
theorem lmax_lt {l : List K} (hne : l ≠ []) {c : K}
    (h : ∀ x, x ∈ l → x < c) : lmax l < c :=
  h (lmax l) (lmax_isMax hne).1

/-! ## Structural facts about `Wmem` -/

/-- The empty set is viable at every horizon. -/
theorem Wmem_empty (M : DetMDP K X A D Y) : ∀ k, Wmem M k (fun _ : X => False) := by
  intro k
  induction k with
  | zero =>
      intro x hx
      cases hx
  | succ k ih =>
      constructor
      · intro x hx
        cases hx
      · rcases exists_mem_of_ne_nil M.univA_ne with ⟨a0, ha0⟩
        refine ⟨a0, ha0, ?_⟩
        intro y
        have hEq : postPred M (fun _ : X => False) a0 y = fun _ : X => False := by
          funext x'
          apply propext
          simp [postPred]
        simpa [hEq] using ih

/-- `Wmem` is downward closed: a subset of a viable set is viable (the same
policy works). -/
theorem Wmem_downward (M : DetMDP K X A D Y) : ∀ k (B C : X → Prop),
    (∀ x, C x → B x) → Wmem M k B → Wmem M k C := by
  intro k
  induction k with
  | zero =>
      intro B C hCB hB x hxC
      exact hB x (hCB x hxC)
  | succ k ih =>
      intro B C hCB hB
      rcases hB with ⟨hsafe, a, ha, hpost⟩
      refine ⟨?_, a, ha, ?_⟩
      · intro x hxC
        exact hsafe x (hCB x hxC)
      · intro y
        apply ih (postPred M B a y) (postPred M C a y)
        · intro x' hx'
          rcases hx' with ⟨x, hxC, d, hd, hF, hy⟩
          exact ⟨x, hCB x hxC, d, hd, hF, hy⟩
        · exact hpost y

/-- Surviving longer implies surviving shorter, under a **policy**. -/
theorem survPol_mono_succ (M : DetMDP K X A D Y) :
    ∀ k (π : List Y → A) (h : List Y) (x : X),
      survPol M (k + 1) π h x → survPol M k π h x := by
  intro k
  induction k with
  | zero =>
      intro π h x hs
      exact hs.1
  | succ k ih =>
      intro π h x hs
      refine ⟨hs.1, ?_⟩
      intro d hd
      exact ih π (h ++ [M.obs x (π h) (M.F x (π h) d)])
        (M.F x (π h) d) (hs.2 d hd)

theorem survPol_mono (M : DetMDP K X A D Y) : ∀ {k n : Nat}, k ≤ n →
    ∀ (π : List Y → A) (h : List Y) (x : X),
      survPol M n π h x → survPol M k π h x := by
  intro k n hkn
  induction hkn with
  | refl =>
      intro π h x hs
      exact hs
  | step hkn ih =>
      intro π h x hn
      exact ih π h x (survPol_mono_succ M _ π h x hn)

/-- **Horizon nesting of the feedback family**: `𝒮_{k+1} ⊆ 𝒮_k`.  This is
the hypothesis `prop:freeze` needs, on the feedback reading. -/
theorem Wmem_succ (M : DetMDP K X A D Y) : ∀ k (B : X → Prop),
    Wmem M (k + 1) B → Wmem M k B := by
  intro k B h
  rcases (Wmem_iff_feedback M (k + 1) B).mp h with ⟨π, hadm, hsurv⟩
  exact (Wmem_iff_feedback M k B).mpr
    ⟨π, hadm, fun x hx => survPol_mono_succ M k π [] x (hsurv x hx)⟩

theorem Wmem_mono (M : DetMDP K X A D Y) {k n : Nat} (hkn : k ≤ n) :
    ∀ B : X → Prop, Wmem M n B → Wmem M k B := by
  intro B hn
  rcases (Wmem_iff_feedback M n B).mp hn with ⟨π, hadm, hsurv⟩
  exact (Wmem_iff_feedback M k B).mpr
    ⟨π, hadm, fun x hx => survPol_mono M hkn π [] x (hsurv x hx)⟩

/-! ## Sums over subsets -/

/-- Every element of `subsetsOf l` really is a subset of `l`. -/
theorem mem_subsetsOf_subset : ∀ (l : List X) (S : List X),
    S ∈ subsetsOf l → ∀ x, x ∈ S → x ∈ l := by
  intro l
  induction l with
  | nil =>
      intro S hS x hx
      simp [subsetsOf] at hS
      subst S
      simp at hx
  | cons y ys ih =>
      intro S hS x hx
      simp [subsetsOf] at hS
      rcases hS with hS | hS
      · exact by simpa using (Or.inr (ih S hS x hx) : x = y ∨ x ∈ ys)
      · rcases hS with ⟨S', hS', hEq⟩
        subst S
        simp at hx
        rcases hx with hxy | hxS'
        · subst x
          simp
        · exact by simpa using (Or.inr (ih S' hS' x hxS') : x = y ∨ x ∈ ys)

/-- Filtering a list yields a member of its power set. -/
theorem filter_mem_subsetsOf (l : List X) (p : X → Prop) [DecidablePred p] :
    l.filter p ∈ subsetsOf l := by
  induction l with
  | nil =>
      simp [subsetsOf]
  | cons y ys ih =>
      simp [subsetsOf]
      by_cases hy : p y
      · right
        exact ⟨ys.filter p, ih, by simp [hy]⟩
      · left
        simpa [hy] using ih

/-- **A sublist of nonnegative terms sums to no more than the whole.**  No
nodup hypothesis is needed: duplicates only make the right-hand side
larger. -/
theorem lsum_mem_subsetsOf_le (f : X → K) :
    ∀ (l : List X), (∀ x, x ∈ l → 0 ≤ f x) →
      ∀ S, S ∈ subsetsOf l → lsum (S.map f) ≤ lsum (l.map f) := by
  intro l
  induction l with
  | nil =>
      intro hf S hS
      simp [subsetsOf] at hS
      subst S
      simp
      exact le_refl 0
  | cons y ys ih =>
      intro hf S hS
      simp [subsetsOf] at hS
      rcases hS with hS | hS
      · have hle := ih (fun x hx => hf x (by simp [hx])) S hS
        have hstep : lsum (ys.map f) ≤ lsum ((y :: ys).map f) := by
          simp
          rw [add_comm]
          exact le_add_of_nonneg_right' (hf y (by simp))
        exact le_trans hle hstep
      · rcases hS with ⟨S', hS', hEq⟩
        subst S
        have hle := ih (fun x hx => hf x (by simp [hx])) S' hS'
        simp
        exact add_le_add_left hle (f y)

/-- **The split lemma over subsets**: if `S` is a subset of `l` and `x₀ ∈ l`
is outside `S`, then `S`'s sum plus the term at `x₀` still fits in the
total.  This is the subset form of `P3_Deterministic`'s
`lsum_ind_add_le`, and it is what makes the deficit bound work on the
feedback family. -/
theorem lsum_subset_add_le (f : X → K) :
    ∀ (l : List X), (∀ x, x ∈ l → 0 ≤ f x) →
      ∀ (S : List X), S ∈ subsetsOf l →
        ∀ x0, x0 ∈ l → x0 ∉ S → lsum (S.map f) + f x0 ≤ lsum (l.map f) := by
  intro l
  induction l with
  | nil =>
      intro hf S hS x0 hx0
      simp at hx0
  | cons y ys ih =>
      intro hf S hS x0 hx0 hx0S
      simp [subsetsOf] at hS
      rcases hS with hS | hS
      · have hle := ih (fun x hx => hf x (by simp [hx])) S hS
        simp only [List.mem_cons] at hx0
        rcases hx0 with hxy | hx0ys
        · -- `x0 = y`: the head term is free
          subst x0
          have hleS : lsum (S.map f) ≤ lsum (ys.map f) :=
            lsum_mem_subsetsOf_le f ys (fun x hx => hf x (by simp [hx])) S hS
          simp
          calc
            lsum (S.map f) + f y = f y + lsum (S.map f) := by rw [add_comm]
            _ ≤ f y + lsum (ys.map f) := add_le_add_left hleS (f y)
        · -- `x0 ∈ ys`: recurse, then account for the head
          have hstep : lsum (ys.map f) ≤ lsum ((y :: ys).map f) := by
            simp
            rw [add_comm]
            exact le_add_of_nonneg_right' (hf y (by simp))
          exact le_trans (hle x0 hx0ys hx0S) hstep
      · rcases hS with ⟨S', hS', hEq⟩
        subst S
        simp only [List.mem_cons] at hx0
        have hx0ys : x0 ∈ ys := by
          rcases hx0 with hxy | hx0ys
          · exact False.elim (hx0S (by simp [hxy]))
          · exact hx0ys
        have hx0S' : x0 ∉ S' := fun h => hx0S (by simp [h])
        have hle := ih (fun x hx => hf x (by simp [hx])) S' hS' x0 hx0ys hx0S'
        simp
        calc
          f y + lsum (S'.map f) + f x0 = f y + (lsum (S'.map f) + f x0) := by
            rw [add_assoc]
          _ ≤ f y + lsum (ys.map f) := add_le_add_left hle (f y)

/-- Dropping terms that are zero does not change the sum. -/
theorem lsum_filter_eq_of_zero (l : List X) (p : X → Prop) [DecidablePred p]
    (f : X → K) (hzero : ∀ x, x ∈ l → ¬ p x → f x = 0) :
    lsum ((l.filter p).map f) = lsum (l.map f) := by
  induction l with
  | nil =>
      simp
  | cons y ys ih =>
      have hz : ∀ x, x ∈ ys → ¬ p x → f x = 0 := fun x hx hp => hzero x (by simp [hx]) hp
      by_cases hy : p y
      · simp [hy, ih hz]
      · simp [hy, ih hz, hzero y (by simp) hy]

/-! ## The support -/

/-- The support of a belief, as a predicate: the enumerated states carrying
nonzero mass. -/
def suppPred (M : DetMDP K X A D Y) (b : Mass K X) : X → Prop :=
  fun x => x ∈ M.univX ∧ b.f x ≠ 0

/-- The same, as a list — so that it can be a member of the family. -/
noncomputable def suppList (M : DetMDP K X A D Y) (b : Mass K X) : List X := by
  classical
  exact M.univX.filter (fun x => b.f x ≠ 0)

theorem suppList_mem_subsetsOf (M : DetMDP K X A D Y) (b : Mass K X) :
    suppList M b ∈ subsetsOf M.univX := by
  unfold suppList
  classical
  exact filter_mem_subsetsOf M.univX (fun x => b.f x ≠ 0)

/-- The two descriptions of the support agree. -/
theorem suppList_eq_suppPred (M : DetMDP K X A D Y) (b : Mass K X) :
    (fun x => x ∈ suppList M b) = suppPred M b := by
  classical
  funext x
  apply propext
  simp [suppList, suppPred]

/-- Mass of the support is the total mass. -/
theorem bS_suppList_eq_totalD (M : DetMDP K X A D Y) (b : Mass K X) :
    bS (suppList M b) b = totalD M b := by
  unfold bS totalD suppList
  classical
  apply lsum_filter_eq_of_zero
  intro x hx hp
  by_cases h0 : b.f x = 0
  · exact h0
  · exact False.elim (hp h0)

/-! ## The feedback family and its value -/

/-- **The feedback survivable-set family `𝒮_k`.**  The subsets of `univX`
that are jointly survivable by one admissible policy — `Wmem`-viable.  This
is `prop:antichain`'s `𝒮_k` for the unrestricted sequential class; the
blind version is `Sfam` (`P3_Freeze_Noisy`). -/
noncomputable def SfamFB (M : DetMDP K X A D Y) (k : Nat) : List (List X) := by
  classical
  exact (subsetsOf M.univX).filter (fun S => Wmem M k (fun x => x ∈ S))

/-- Membership in the family: a subset of `univX` that `Wmem` accepts. -/
theorem mem_SfamFB (M : DetMDP K X A D Y) {k : Nat} {S : List X} :
    S ∈ SfamFB M k ↔ S ∈ subsetsOf M.univX ∧ Wmem M k (fun x => x ∈ S) := by
  unfold SfamFB
  classical
  simp [List.mem_filter]

/-- The family is inhabited: the empty set is viable at every horizon. -/
theorem SfamFB_ne (M : DetMDP K X A D Y) (k : Nat) : SfamFB M k ≠ [] := by
  apply ne_nil_of_exists_mem
  refine ⟨[], ?_⟩
  rw [mem_SfamFB]
  constructor
  · exact nil_mem_subsetsOf M.univX
  · simpa using Wmem_empty M k

/-- **Nesting `𝒮_{k+1} ⊆ 𝒮_k`**, at the level of families. -/
theorem SfamFB_nesting (M : DetMDP K X A D Y) :
    ∀ k, ∀ S, S ∈ SfamFB M (k + 1) → S ∈ SfamFB M k := by
  intro k S h
  rw [mem_SfamFB] at h ⊢
  exact ⟨h.1, Wmem_succ M k (fun x => x ∈ S) h.2⟩

theorem SfamFB_mono (M : DetMDP K X A D Y) {k n : Nat} (hkn : k ≤ n) :
    ∀ S, S ∈ SfamFB M n → S ∈ SfamFB M k := by
  intro S h
  rw [mem_SfamFB] at h ⊢
  exact ⟨h.1, Wmem_mono M hkn (fun x => x ∈ S) h.2⟩

/-- **`V_k(b) = max_{S ∈ 𝒮_k} b(S)`** — `prop:antichain` (i), read for the
feedback class, serving here as the definition of the value. -/
noncomputable def VFb (M : DetMDP K X A D Y) (k : Nat) (b : Mass K X) : K :=
  lmax ((SfamFB M k).map (fun S => bS S b))

/-- The value never exceeds the total mass. -/
theorem VFb_le_totalD (M : DetMDP K X A D Y) (k : Nat) (b : Mass K X) :
    VFb M k b ≤ totalD M b := by
  unfold VFb
  apply lmax_le (map_ne_nil (fun S => bS S b) (SfamFB_ne M k))
  intro z hz
  rcases List.mem_map.mp hz with ⟨S, hS, rfl⟩
  unfold bS totalD
  exact lsum_mem_subsetsOf_le b.f M.univX (fun x hx => b.nonneg x) S
    ((mem_SfamFB M).mp hS).1

/-- **Consequence 1, `⟸`.**  If the support is `𝒲_k`-viable (feedback
reading) then the feedback value is the total mass — hence `1` for a
normalized belief. -/
theorem VFb_eq_total_of_Wmem (M : DetMDP K X A D Y) (k : Nat) (b : Mass K X)
    (hW : Wmem M k (suppPred M b)) : VFb M k b = totalD M b := by
  apply le_antisymm
  · exact VFb_le_totalD M k b
  · have hmem : suppList M b ∈ SfamFB M k := by
      rw [mem_SfamFB]
      constructor
      · exact suppList_mem_subsetsOf M b
      · simpa [suppList_eq_suppPred M b] using hW
    calc
      totalD M b = bS (suppList M b) b := (bS_suppList_eq_totalD M b).symm
      _ ≤ VFb M k b := by
        unfold VFb
        exact le_lmax (map_ne_nil (fun S => bS S b) (SfamFB_ne M k))
          (List.mem_map.mpr ⟨suppList M b, hmem, rfl⟩)

/-- **Consequence 2, the min-mass bound on the feedback class.**  If the
support is not `𝒲_k`-viable then the deficit is at least the smallest
branch mass: every jointly-survivable set misses a branch, and the split
lemma charges for it. -/
theorem VFb_min_mass_bound (M : DetMDP K X A D Y) (k : Nat) (b : Mass K X)
    (mn : K)
    (hmn : ∀ x, x ∈ M.univX → b.f x ≠ 0 → mn ≤ b.f x)
    (hlost : ¬ Wmem M k (suppPred M b)) :
    mn ≤ totalD M b - VFb M k b := by
  apply le_sub_of_add_le_of
  rw [add_comm]
  have hVF : VFb M k b ≤ totalD M b - mn := by
    unfold VFb
    apply lmax_le (map_ne_nil (fun S => bS S b) (SfamFB_ne M k))
    intro z hz
    rcases List.mem_map.mp hz with ⟨S, hS, rfl⟩
    have hSfam := (mem_SfamFB M).mp hS
    have hx0 : ∃ x0, x0 ∈ M.univX ∧ b.f x0 ≠ 0 ∧ x0 ∉ S := by
      by_cases h : ∃ x0, x0 ∈ M.univX ∧ b.f x0 ≠ 0 ∧ x0 ∉ S
      · exact h
      · exfalso
        apply hlost
        -- otherwise the support is contained in `S`, and `Wmem` is downward closed
        apply Wmem_downward M k (fun x => x ∈ S) (suppPred M b)
        · intro x hx
          by_cases hxS : x ∈ S
          · exact hxS
          · exact False.elim (h ⟨x, hx.1, hx.2, hxS⟩)
        · exact hSfam.2
    rcases hx0 with ⟨x0, hx0u, hx0ne, hx0S⟩
    have hsplit : bS S b + b.f x0 ≤ totalD M b := by
      unfold bS totalD
      exact lsum_subset_add_le b.f M.univX (fun x hx => b.nonneg x) S
        hSfam.1 x0 hx0u hx0S
    have hle1 : bS S b ≤ totalD M b - b.f x0 := le_sub_of_add_le_of hsplit
    exact le_trans hle1 (sub_le_sub_left_of_le (hmn x0 hx0u hx0ne))
  exact add_le_of_le_sub hVF

/-- **Consequence 1, `⟹`, strictly.**  If the support is not `𝒲_k`-viable
then every set in the family misses a branch of *strictly positive* mass,
so the value is strictly below the total. -/
theorem VFb_lt_total_of_not_Wmem (M : DetMDP K X A D Y) (k : Nat)
    (b : Mass K X) (hlost : ¬ Wmem M k (suppPred M b)) :
    VFb M k b < totalD M b := by
  unfold VFb
  apply lmax_lt (map_ne_nil (fun S => bS S b) (SfamFB_ne M k))
  intro z hz
  rcases List.mem_map.mp hz with ⟨S, hS, rfl⟩
  have hSfam := (mem_SfamFB M).mp hS
  have hx0 : ∃ x0, x0 ∈ M.univX ∧ b.f x0 ≠ 0 ∧ x0 ∉ S := by
    by_cases h : ∃ x0, x0 ∈ M.univX ∧ b.f x0 ≠ 0 ∧ x0 ∉ S
    · exact h
    · exfalso
      apply hlost
      apply Wmem_downward M k (fun x => x ∈ S) (suppPred M b)
      · intro x hx
        by_cases hxS : x ∈ S
        · exact hxS
        · exact False.elim (h ⟨x, hx.1, hx.2, hxS⟩)
      · exact hSfam.2
  rcases hx0 with ⟨x0, hx0u, hx0ne, hx0S⟩
  have hsplit : bS S b + b.f x0 ≤ totalD M b := by
    unfold bS totalD
    exact lsum_subset_add_le b.f M.univX (fun x hx => b.nonneg x) S
      hSfam.1 x0 hx0u hx0S
  have hpos : 0 < b.f x0 := pos_of_nonneg_of_ne (b.nonneg x0) hx0ne
  exact lt_of_lt_of_le (lt_add_of_pos_right hpos) hsplit

/-- **Consequence 1.**  For the unrestricted sequential class, the value is
the total mass exactly when the support lies in `𝒲_k`.  With
`totalD M b = 1` this is the paper's `V_k(b) = 1 ⟺ supp(b) ∈ 𝒲_k`.
No positivity hypothesis on the branch masses is needed beyond
`b(x) ≥ 0` and `b(x) ≠ 0` on the support, both supplied by `Mass`. -/
theorem VFb_eq_total_iff_Wmem (M : DetMDP K X A D Y) (k : Nat)
    (b : Mass K X) :
    VFb M k b = totalD M b ↔ Wmem M k (suppPred M b) := by
  classical
  constructor
  · intro hEq
    by_cases hW : Wmem M k (suppPred M b)
    · exact hW
    · have hlt := VFb_lt_total_of_not_Wmem M k b hW
      exact False.elim ((not_le_of_lt hlt) (by rw [hEq]; exact le_refl _))
  · exact VFb_eq_total_of_Wmem M k b

/-- **Consequence 3: the value is non-increasing in the horizon.**  A
maximum over a shrinking family cannot grow. -/
theorem VFb_antitone (M : DetMDP K X A D Y) {k n : Nat} (hkn : k ≤ n)
    (b : Mass K X) : VFb M n b ≤ VFb M k b := by
  unfold VFb
  apply lmax_le_lmax_of_subset (map_ne_nil (fun S => bS S b) (SfamFB_ne M n))
  intro z hz
  rcases List.mem_map.mp hz with ⟨S, hS, rfl⟩
  exact List.mem_map.mpr ⟨S, SfamFB_mono M hkn S hS, rfl⟩

end Formalizations.P3

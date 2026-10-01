/-
  Formalizations.P3_BlindValue
  ============================

  **The blind composition** — `prop:degen` consequence 1 stated in terms of
  `𝒲_k`.

  v27 left one mechanical step un-composed: chaining
  `Wblind_iff_survK` (v27) + `survT_iff_survK` (v26) +
  `VR_eq_total_of_jointly_surviving` (v12) to get

      `VR_k(b) = totalD(b)`  ⟺  `supp(b) ∈ 𝒲_k`   (blind reading)

  This module does it, in both directions. The forward direction is proved
  **strictly** — `VR < totalD` — not by a deficit bound, mirroring the
  feedback result `VFb_lt_total_of_not_Wmem` (v29): if the support is not
  `𝒲_k`-viable then every declared tuple loses a branch of *strictly
  positive* mass, so each survived-mass value is strictly below the total
  and a finite maximum of strict inequalities is strict.

  ## The plumbing, and why it is needed

  `VR` maximizes over `tuples M k` — a list of **action tuples**. `Wblind`
  provides an **infinite schedule** `Nat → A`. Bridging them requires:

    mem_tuplesAux     membership in the one-step extension of a tuple list
    mem_tuples        `t ∈ tuples M k ↔ |t| = k ∧ every entry is admissible`
    getD_mem_of_lt    `t.getD i a0 ∈ t` whenever `i < |t|`
    exists_tuple_of_sched   an admissible schedule has a matching tuple
    smass_eq_bS_survSet    a tuple's survived mass is the mass of its
                           surviving set — the bridge between the two
                           vocabularies at the *value* level

  The last of these is the substantive one: it says the indicator-weighted
  sum `smass` is exactly `bS` of the filtered surviving set.

  ## What this does and does not claim

  * It is the **blind** reading — `prop:degen`'s declared sequential class
    `Π_B` on a blind window, and `thm:lattice`'s `Π_ol = Π_seq,blind`.
    It is *not* `thm:support` consequence 1, which v28 showed is about
    `Π_seq` and which v29 closed with the feedback operator `VFb`.
  * The fallback action `a0` used to read a schedule off a tuple must be
    **admissible** (it is reached only at indices `≥ |t|`, but
    `SurvivableAdm` quantifies over all indices), so it is chosen from
    `univA`.

  ## Contents

    mem_tuplesAux, mem_tuples, getD_mem_of_lt, exists_tuple_of_sched
    survSet, smass_eq_bS_survSet
    survSet_mem_SfamAdm      a tuple's surviving set is admissibly survivable
    VR_eq_total_of_Wblind    `⟸` — the composed statement
    VR_lt_total_of_not_Wblind `⟹`, strictly
    VR_eq_total_iff_Wblind   **the blind consequence 1**
-/

import Formalizations.Prelude
import Formalizations.P3_Deterministic
import Formalizations.P3_Freeze_Noisy
import Formalizations.P3_Bridge
import Formalizations.P3_Viable
import Formalizations.P3_Feedback
import Formalizations.P3_FeedbackValue
import Formalizations.P3_SurvivableAdm

namespace Formalizations.P3

open Formalizations
open Formalizations.POMDP

set_option linter.unusedSectionVars false

variable {K : Type} [OrdField K]
variable {X A D Y : Type}

/-! ## Membership in the declared tuple class -/

/-- One-step extension: `x ∈ tuplesAux M l` iff `x = a :: t` for some
`t ∈ l` and some admissible `a`. -/
theorem mem_tuplesAux (M : DetMDP K X A D Y) :
    ∀ (l : List (List A)) (x : List A),
      x ∈ tuplesAux M l ↔ ∃ t, t ∈ l ∧ ∃ a, a ∈ M.univA ∧ a :: t = x := by
  intro l
  induction l with
  | nil =>
      intro x
      simp [tuplesAux]
  | cons t ts ih =>
      intro x
      rw [tuplesAux]
      simp only [List.mem_append, List.mem_map]
      constructor
      · rintro (⟨a, ha, hax⟩ | hx)
        · exact ⟨t, by simp, a, ha, hax⟩
        · rcases (ih x).mp hx with ⟨t', ht', a, ha, hax⟩
          exact ⟨t', by simp [ht'], a, ha, hax⟩
      · rintro ⟨t', ht', a, ha, hax⟩
        simp at ht'
        rcases ht' with rfl | ht'
        · exact Or.inl ⟨a, ha, hax⟩
        · exact Or.inr ((ih x).mpr ⟨t', ht', a, ha, hax⟩)

/-- **`t ∈ tuples M k` iff `t` has length `k` and every entry is
admissible.**  The declared sequential-blind class at horizon `k` is
exactly the set of such tuples. -/
theorem mem_tuples (M : DetMDP K X A D Y) :
    ∀ k (t : List A), t ∈ tuples M k ↔ t.length = k ∧ ∀ a, a ∈ t → a ∈ M.univA := by
  intro k
  induction k with
  | zero =>
      intro t
      constructor
      · intro ht
        simp [tuples] at ht
        subst t
        simp
      · intro h
        cases t with
        | nil => simp [tuples]
        | cons a as => simp at h
  | succ k ih =>
      intro t
      constructor
      · intro ht
        rcases (mem_tuplesAux M (tuples M k) t).mp ht with ⟨t', ht', a, ha, hax⟩
        subst t
        have ih' := (ih t').mp ht'
        constructor
        · simp [ih'.1]
        · intro b hb
          simp at hb
          rcases hb with rfl | hb
          · exact ha
          · exact ih'.2 b hb
      · intro h
        cases t with
        | nil => simp at h
        | cons a t' =>
            have ht'len : t'.length = k := by simpa using h.1
            have ht'adm : ∀ b, b ∈ t' → b ∈ M.univA := fun b hb => h.2 b (by simp [hb])
            have ha : a ∈ M.univA := h.2 a (by simp)
            have ht'mem : t' ∈ tuples M k := (ih t').mpr ⟨ht'len, ht'adm⟩
            exact (mem_tuplesAux M (tuples M k) (a :: t')).mpr ⟨t', ht'mem, a, ha, rfl⟩

/-- `getD` returns an element of the list below the length. -/
theorem getD_mem_of_lt : ∀ (t : List A) (i : Nat) (a0 : A), i < t.length → t.getD i a0 ∈ t := by
  intro t
  induction t with
  | nil =>
      intro i a0 hi
      simp at hi
  | cons a t' ih =>
      intro i a0 hi
      cases i with
      | zero => simp
      | succ i =>
          simp
          right
          exact ih i a0 (Nat.succ_lt_succ_iff.mp hi)

/-- `getD` returns the fallback at or past the end of the list. -/
theorem getD_eq_default_of_le : ∀ (t : List A) (i : Nat) (a0 : A),
    t.length ≤ i → t.getD i a0 = a0 := by
  intro t
  induction t with
  | nil =>
      intro i a0 hi
      simp [List.getD]
  | cons a t' ih =>
      intro i a0 hi
      cases i with
      | zero => simp at hi
      | succ i =>
          rw [List.getD_cons_succ]
          exact ih i a0 (Nat.succ_le_succ_iff.mp hi)

/-- **Every admissible schedule has a matching declared tuple.**  The
fallback `a0` never matters inside the horizon:
`survK_congr_prefix` says `survK M k u x` only probes `u 0 … u (k-1)`. -/
theorem exists_tuple_of_sched (M : DetMDP K X A D Y) (a0 : A) :
    ∀ k (u : Nat → A), (∀ i, u i ∈ M.univA) →
      ∃ t, t ∈ tuples M k ∧ t.length = k ∧ ∀ i, i < k → t.getD i a0 = u i := by
  intro k
  induction k with
  | zero =>
      intro u hu
      refine ⟨[], ?_, ?_, ?_⟩
      · simp [tuples]
      · simp
      · intro i hi
        exact False.elim (Nat.not_lt_zero i hi)
  | succ k ih =>
      intro u hu
      rcases ih (fun i => u (i + 1)) (fun i => hu (i + 1)) with
        ⟨t', ht'mem, ht'len, ht'get⟩
      refine ⟨u 0 :: t', ?_, ?_, ?_⟩
      · exact (mem_tuplesAux M (tuples M k) (u 0 :: t')).mpr
          ⟨t', ht'mem, u 0, hu 0, rfl⟩
      · simp [ht'len]
      · intro i hi
        cases i with
        | zero => simp
        | succ i =>
            simpa using ht'get i (Nat.succ_lt_succ_iff.mp hi)

/-! ## A tuple's surviving set -/

/-- The states of `univX` that survive the declared tuple `t`. -/
noncomputable def survSet (M : DetMDP K X A D Y) (t : List A) : List X := by
  classical
  exact M.univX.filter (fun x => survT M t x = true)

/-- An indicator-weighted sum is the sum over the sublist the indicator
picks out. -/
theorem lsum_ind_eq_filter : ∀ (l : List X) (g : X → Bool) (f : X → K),
    lsum (l.map (fun x => f x * ind g x)) = lsum ((l.filter (fun x => g x = true)).map f) := by
  intro l
  induction l with
  | nil =>
      intro g f
      simp
  | cons y ys ih =>
      intro g f
      have ih' := ih g f
      by_cases hy : g y = true
      · have hind : ind g y = (1 : K) := by simp [ind, hy]
        calc
          lsum ((y :: ys).map (fun x => f x * ind g x))
              = f y * ind g y + lsum (ys.map (fun x => f x * ind g x)) := by simp
          _ = f y * 1 + lsum (ys.map (fun x => f x * ind g x)) := by rw [hind]
          _ = f y + lsum (ys.map (fun x => f x * ind g x)) := by rw [mul_one]
          _ = f y + lsum ((ys.filter (fun x => g x = true)).map f) := by rw [ih']
          _ = lsum (((y :: ys).filter (fun x => g x = true)).map f) := by simp [hy]
      · have hind : ind g y = (0 : K) := by simp [ind, hy]
        calc
          lsum ((y :: ys).map (fun x => f x * ind g x))
              = f y * ind g y + lsum (ys.map (fun x => f x * ind g x)) := by simp
          _ = f y * 0 + lsum (ys.map (fun x => f x * ind g x)) := by rw [hind]
          _ = 0 + lsum (ys.map (fun x => f x * ind g x)) := by rw [mul_zero]
          _ = lsum ((ys.filter (fun x => g x = true)).map f) := by rw [zero_add, ih']
          _ = lsum (((y :: ys).filter (fun x => g x = true)).map f) := by simp [hy]

/-- **A tuple's survived mass is the mass of its surviving set** — the
bridge between `smass` (indicator-weighted over `univX`) and `bS` (a sum
over a sublist). -/
theorem smass_eq_bS_survSet (M : DetMDP K X A D Y) (t : List A) (b : Mass K X) :
    smass M t b = bS (survSet M t) b := by
  unfold smass bS survSet
  classical
  exact lsum_ind_eq_filter M.univX (survT M t) b.f

/-- A tuple's surviving set is admissibly survivable: read the schedule off
the tuple, with an admissible fallback. -/
theorem survSet_mem_SfamAdm (M : DetMDP K X A D Y) (a0 : A)
    (ha0 : a0 ∈ M.univA) :
    ∀ k (t : List A), t ∈ tuples M k → survSet M t ∈ SfamAdm M k := by
  intro k t ht
  rw [mem_SfamAdm]
  constructor
  · unfold survSet
    classical
    exact filter_mem_subsetsOf M.univX (fun x => survT M t x = true)
  · refine ⟨fun i => t.getD i a0, ?_, ?_⟩
    · intro i
      by_cases hi : i < t.length
      · exact ((mem_tuples M k t).mp ht).2 (t.getD i a0) (getD_mem_of_lt t i a0 hi)
      · have hge : t.length ≤ i := Nat.le_of_not_gt hi
        have hgetD : t.getD i a0 = a0 := getD_eq_default_of_le t i a0 hge
        change t.getD i a0 ∈ M.univA
        rw [hgetD]
        exact ha0
    · intro x hx
      have hst : survT M t x = true := by
        unfold survSet at hx
        classical
        exact of_decide_eq_true (List.mem_filter.mp hx).2
      have hlen : t.length = k := ((mem_tuples M k t).mp ht).1
      have hs : survK M k (fun i => t.getD i a0) x := by
        simpa [hlen] using (survT_iff_survK M a0 t x).mp hst
      exact hs

/-- The survived-mass values form a nonempty list (the tuple class is). -/
theorem smass_map_ne (M : DetMDP K X A D Y) (k : Nat) (b : Mass K X) :
    (tuples M k).map (fun t => smass M t b) ≠ [] :=
  map_ne_nil (fun t => smass M t b) (tuples_ne M k)

/-! ## The composition -/

/-- **Blind consequence 1, `⟸`.**  If the support is `𝒲_k`-viable (blind
reading) then some declared tuple keeps every branch of positive mass, so
`VR` is the total mass — `prop:degen`'s "if the support carries a jointly
surviving blind sequence, `V_k(b) = 1`", stated in terms of `𝒲_k`. -/
theorem VR_eq_total_of_Wblind (M : DetMDP K X A D Y) (k : Nat) (b : Mass K X)
    (hW : Wblind M k (suppPred M b)) : VR M k b = totalD M b := by
  rcases (Wblind_iff_survK M k (suppPred M b)).mp hW with ⟨u, huadm, husurv⟩
  rcases exists_mem_of_ne_nil M.univA_ne with ⟨a0, ha0⟩
  rcases exists_tuple_of_sched M a0 k u huadm with ⟨t, htmem, htlen, htget⟩
  apply VR_eq_total_of_jointly_surviving M k b
  refine ⟨t, htmem, ?_⟩
  intro x hx hbne
  have hs : survK M k u x := husurv x ⟨hx, hbne⟩
  have hs' : survK M k (fun i => t.getD i a0) x :=
    survK_congr_prefix M k u (fun i => t.getD i a0) x
      (by intro i hi; exact (htget i hi).symm) hs
  exact (survT_iff_survK M a0 t x).mpr (by simpa [htlen] using hs')

/-- **Blind consequence 1, `⟹`, strictly.**  If the support is not
`𝒲_k`-viable then every declared tuple's surviving set misses a branch of
strictly positive mass, so every survived-mass value — and hence the
maximum — is strictly below the total. -/
theorem VR_lt_total_of_not_Wblind (M : DetMDP K X A D Y) (k : Nat)
    (b : Mass K X) (hlost : ¬ Wblind M k (suppPred M b)) :
    VR M k b < totalD M b := by
  rcases exists_mem_of_ne_nil M.univA_ne with ⟨a0, ha0⟩
  unfold VR
  apply lmax_lt (smass_map_ne M k b)
  intro z hz
  rcases List.mem_map.mp hz with ⟨t, ht, rfl⟩
  have hSfam : survSet M t ∈ SfamAdm M k := survSet_mem_SfamAdm M a0 ha0 k t ht
  have hSsub : survSet M t ∈ subsetsOf M.univX := ((mem_SfamAdm M).mp hSfam).1
  -- the surviving set cannot contain the whole support, or `Wblind` would hold
  have hx0 : ∃ x0, x0 ∈ M.univX ∧ b.f x0 ≠ 0 ∧ x0 ∉ survSet M t := by
    by_cases h : ∃ x0, x0 ∈ M.univX ∧ b.f x0 ≠ 0 ∧ x0 ∉ survSet M t
    · exact h
    · exfalso
      apply hlost
      apply Wblind_downward M k (fun x => x ∈ survSet M t) (suppPred M b)
      · intro x hx
        by_cases hxS : x ∈ survSet M t
        · exact hxS
        · exact False.elim (h ⟨x, hx.1, hx.2, hxS⟩)
      · exact (SurvivableAdm_iff_Wblind M (survSet M t) k).mp ((mem_SfamAdm M).mp hSfam).2
  rcases hx0 with ⟨x0, hx0u, hx0ne, hx0S⟩
  have hsplit : smass M t b + b.f x0 ≤ totalD M b := by
    rw [smass_eq_bS_survSet]
    unfold bS totalD
    exact lsum_subset_add_le b.f M.univX (fun x hx => b.nonneg x)
      (survSet M t) hSsub x0 hx0u hx0S
  have hpos : 0 < b.f x0 := pos_of_nonneg_of_ne (b.nonneg x0) hx0ne
  exact lt_of_lt_of_le (lt_add_of_pos_right hpos) hsplit

/-- **Blind consequence 1.**  For the declared sequential-blind class, the
degenerated value is the total mass exactly when the support lies in
`𝒲_k`.  With `totalD M b = 1` this is `V_k(b) = 1 ⟺ supp(b) ∈ 𝒲_k` on the
blind reading. -/
theorem VR_eq_total_iff_Wblind (M : DetMDP K X A D Y) (k : Nat)
    (b : Mass K X) :
    VR M k b = totalD M b ↔ Wblind M k (suppPred M b) := by
  classical
  constructor
  · intro hEq
    by_cases hW : Wblind M k (suppPred M b)
    · exact hW
    · have hlt := VR_lt_total_of_not_Wblind M k b hW
      exact False.elim ((not_le_of_lt hlt) (by rw [hEq]; exact le_refl _))
  · exact VR_eq_total_of_Wblind M k b

end Formalizations.P3

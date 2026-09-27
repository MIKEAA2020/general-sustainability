/-
  Formalizations.P3_FreezeCount
  =============================

  **`prop:freeze`'s `2^{|supp b|}` — the last paper-owned claim in P3.**

  `prop:freeze` (paper2 v11, 687–701):

      "With deterministic kernels the survivable-set families satisfy
       `𝒮_{ℓ+1} ⊆ 𝒮_ℓ`; hence `V_ℓ(b)` is non-increasing in the horizon and
       stabilizes after at most `2^{|supp b|}` strict decreases, the frozen
       value being `max_S b(S)` over the maximal sets of the frozen family
       --- an exact computable infinite-horizon value."

  Monotonicity was already formalized (`VfamAdm_antitone`, v30, on the
  corrected family `𝒮^adm_k`; `Vfam_prune_ge/_le` carry it for the old
  one). What was missing is **the count**, and it is missing for a reason
  worth recording: it is the paper's *own* combinatorial claim. The Sperner
  bound in `prop:antichain` (iii) is cited to Sperner (1928), so not
  formalizing it verifies the paper faithfully; this bound is asserted by
  the paper, so leaving it out would leave a claim of the paper unchecked.

  The argument. `V_ℓ(b) = max_{S ∈ 𝒮_ℓ} b(S)`, the families nest, and a
  maximizer's mass does not change when it is truncated to the support
  (`bS_supp_trunc`), so **every** value of the sequence is the mass of some
  subset of `supp(b)` (`VfamAdm_mem_range`) — and there are exactly
  `2^{|supp b|}` of those (`subsetsOf_length`, v13). Two strict decreases
  cannot repeat a value: if `k₁ < k₂` and the sequence drops strictly at
  `k₁`, then `V_{k₂} ≤ V_{k₁+1} < V_{k₁}` by monotonicity. So the map from
  a strict drop to its value is injective into a set of size
  `2^{|supp b|}`, which is the bound.

  Stated for every horizon `n` rather than "eventually": the number of
  strict drops among the first `n` horizons is at most `2^{|supp b|}`.
  That is what "stabilizes after at most" means, and it is checkable
  without a limit.

  **Relation to `P3_Freeze_Noisy_v2` (v18).** That module already has a
  drop count, `prop_freeze_drop_count`. Two differences, both material:

  1. **Its bound is `2^{|univX|}`, not `2^{|supp b|}`** —
     `drops_le_card` bounds the drops by `|𝒮_0|` and `Sfam0_card_le` bounds
     that by `2^{|univX|}`. The paper says `2^{|supp b|}`, which is
     sharper whenever the support is proper.
  2. **It runs on the old, defective family** (`Sfam`/`Vfam`, whose
     `Survivable` lacks the admissibility constraint — the v30 defect),
     whereas this module runs on the corrected `SfamAdm`/`VfamAdm`.

  **A defect in that module, recorded here because it is in our layer and
  not in the paper:** `prop_freeze_drop_count`'s docstring says "at most
  `2^{|supp b|}`" while the statement says `2 ^ M.univX.length`. The
  comment over-claims. That over-claim was propagated into
  `lean_README`'s `prop:freeze` row, which lists v18 as having done the
  count; at the paper's stated bound it had not. Corrected in v10.

  **Residual, flagged not closed.** `prop:freeze`'s second clause — the
  frozen value is `max_S b(S)` over the *maximal* sets of the frozen
  family — is proved for the old family (`Vfam_prune_eq`, v21) but not for
  the corrected `𝒮^adm_k`. That is a separate, smaller theorem and is not
  done here.
-/

import Formalizations.Prelude
import Formalizations.P3_Sufficiency
import Formalizations.P3_Freeze_Noisy
import Formalizations.P3_Antichain_v2
import Formalizations.P3_FeedbackValue
import Formalizations.P3_SurvivableAdm

set_option linter.unusedSectionVars false

open Formalizations
open Formalizations.POMDP

namespace Formalizations.P3

variable {K : Type} [OrdField K]
variable {X A D Y : Type}
variable [DecidableEq X]

/-! ## §1 · Three counting lemmas the stdlib here does not supply -/

/-- Membership survives `erase` for a distinct element. `List.mem_erase_of_ne_of_mem`
is absent, and `mem_erase_iff` (v21) needs `Nodup`, which the target list
need not have. -/
theorem mem_erase_of_mem_of_ne : ∀ (l : List X) (a x : X), x ∈ l → x ≠ a → x ∈ l.erase a := by
  intro l
  induction l with
  | nil => intro a x hx hne; cases hx
  | cons b t ih =>
      intro a x hx hne
      by_cases hba : b = a
      · subst b
        simp at hx
        simp
        cases hx with
        | inl hxa => exact False.elim (hne hxa)
        | inr hxt => exact hxt
      · simp [hba] at hx ⊢
        cases hx with
        | inl hxb => exact Or.inl hxb
        | inr hxt => exact Or.inr (ih a x hxt hne)

/-- A `Nodup` list whose elements all lie in another list is no longer than
it. This is the pigeonhole principle for lists; the layer has no cardinal
machinery, so it is proved by induction, erasing the head. -/
theorem nodup_mem_length_le {α : Type} : ∀ {l₁ l₂ : List α},
    l₁.Nodup → (∀ x, x ∈ l₁ → x ∈ l₂) → l₁.length ≤ l₂.length := by
  classical
  intro l₁
  induction l₁ with
  | nil =>
      intro l₂ hnod hmem
      simp
  | cons a as ih =>
      intro l₂ hnod hmem
      have hnod_as : as.Nodup := (List.nodup_cons.mp hnod).2
      have ha_not : a ∉ as := (List.nodup_cons.mp hnod).1
      have has_le : as.length ≤ (l₂.erase a).length := by
        apply ih hnod_as
        intro x hx
        apply mem_erase_of_mem_of_ne l₂ a x
        · exact hmem x (by simp [hx])
        · intro hxa
          exact ha_not (by simpa [hxa] using hx)
      have ha_mem : a ∈ l₂ := hmem a (by simp)
      have hpos : 1 ≤ l₂.length := by
        cases l₂ with
        | nil => simp at ha_mem
        | cons b t => simp
      have herase : (l₂.erase a).length = l₂.length - 1 := List.length_erase_of_mem ha_mem
      have hle : as.length ≤ l₂.length - 1 := by simpa [herase] using has_le
      have hsucc : as.length + 1 ≤ (l₂.length - 1) + 1 := Nat.succ_le_succ hle
      simpa [Nat.sub_add_cancel hpos] using hsucc

/-- `Nodup` is preserved by a map that is injective *on the list*. -/
theorem nodup_map_on_of_inj {α β : Type} (f : α → β) : ∀ (l : List α),
    l.Nodup → (∀ x ∈ l, ∀ y ∈ l, f x = f y → x = y) → (l.map f).Nodup := by
  intro l
  induction l with
  | nil => intro hnod hinj; simp
  | cons a t ih =>
      intro hnod hinj
      have ht : t.Nodup := (List.nodup_cons.mp hnod).2
      have hat : a ∉ t := (List.nodup_cons.mp hnod).1
      change (f a :: t.map f).Nodup
      exact List.nodup_cons.mpr ⟨(by
        intro hmem
        rcases List.mem_map.mp hmem with ⟨y, hy, hfy⟩
        have hay : a = y := hinj a (by simp) y (by simp [hy]) hfy.symm
        exact hat (by simpa [hay] using hy)),
        (ih ht (by intro x hx y hy hxy; exact hinj x (by simp [hx]) y (by simp [hy]) hxy))⟩

/-- Filtering by a `Prop` predicate preserves `Nodup`. The layer's
`nodup_filter` is stated for `Bool`-valued predicates. -/
theorem nodup_filterP (p : X → Prop) [DecidablePred p] : ∀ (l : List X),
    l.Nodup → (l.filter p).Nodup := by
  intro l
  induction l with
  | nil => intro hnod; simp
  | cons a t ih =>
      intro hnod
      have ht : t.Nodup := (List.nodup_cons.mp hnod).2
      have hat : a ∉ t := (List.nodup_cons.mp hnod).1
      by_cases hp : p a
      · have hfilt : (a :: t).filter p = a :: t.filter p := by simp [hp]
        rw [hfilt]
        exact List.nodup_cons.mpr ⟨(by
          intro hmem
          exact hat ((List.mem_filter.mp hmem).1)), ih ht⟩
      · have hfilt : (a :: t).filter p = t.filter p := by simp [hp]
        rw [hfilt]
        exact ih ht

/-! ## §2 · Truncating a survivable set to the support -/

/-- **Mass is unchanged by truncating to the support.** `b(S) = b(S ∩ supp b)`,
because every state outside the support carries zero mass.

The truncation is taken as `(suppList b).filter (· ∈ S)` rather than
`S.filter (· ∈ suppList b)` — the two have the same elements, but only the
former is a member of `subsetsOf (suppList b)`, since `subsetsOf` records
subsets in the order of the ambient list. -/
theorem bS_supp_trunc (M : DetMDP K X A D Y) (b : Mass K X) (S : List X)
    (hSsub : ∀ x, x ∈ S → x ∈ M.univX) (hSnod : S.Nodup) :
    bS ((suppList M b).filter (fun x => x ∈ S)) b = bS S b := by
  classical
  let T := (suppList M b).filter (fun x => x ∈ S)
  let U := S.filter (fun x => x ∈ suppList M b)
  have hzero : ∀ x, x ∈ S → ¬ x ∈ suppList M b → b.f x = 0 := by
    intro x hxS hxnot
    by_cases hz : b.f x = 0
    · exact hz
    · exfalso
      apply hxnot
      have hsupp : suppPred M b x := ⟨hSsub x hxS, hz⟩
      have hEq := congrFun (suppList_eq_suppPred M b) x
      exact hEq.mpr hsupp
  have hU : bS U b = bS S b := by
    unfold bS U
    exact lsum_filter_eq_of_zero S (fun x => x ∈ suppList M b) b.f hzero
  have hsupp_nod : (suppList M b).Nodup := by
    simpa [suppList] using (nodup_filterP (fun x => b.f x ≠ 0) M.univX M.univX_nodup)
  have hTnod : T.Nodup := by
    unfold T
    exact nodup_filterP (fun x => x ∈ S) (suppList M b) hsupp_nod
  have hUnod : U.Nodup := by
    unfold U
    exact nodup_filterP (fun x => x ∈ suppList M b) S hSnod
  have hTU : bS T b = bS U b := by
    unfold bS
    apply lsum_eq_of_mem_iff b.f T U hTnod hUnod
    intro x
    simp [T, U, and_comm]
  calc
    bS T b = bS U b := hTU
    _ = bS S b := hU

/-! ## §3 · Every value is the mass of a subset of the support -/

/-- **The range of the horizon sequence lies in
`{b(T) : T ⊆ supp(b)}`.** The maximum is attained (`lmax_isMax`), and
truncating the maximizer to the support does not change its mass. -/
theorem VfamAdm_mem_range (M : DetMDP K X A D Y) (k : Nat) (b : Mass K X) :
    ∃ T, T ∈ subsetsOf (suppList M b) ∧ VfamAdm M k b = bS T b := by
  classical
  let l := (SfamAdm M k).map (fun S => bS S b)
  have hlne : l ≠ [] := map_ne_nil (fun S => bS S b) (SfamAdm_ne M k)
  have hmax : IsMax (lmax l) l := lmax_isMax hlne
  rcases List.mem_map.mp hmax.1 with ⟨S, hS, hEq⟩
  refine ⟨(suppList M b).filter (fun x => x ∈ S),
          filter_mem_subsetsOf (suppList M b) (fun x => x ∈ S), ?_⟩
  have hSsub : ∀ x, x ∈ S → x ∈ M.univX :=
    mem_subsetsOf_subset M.univX S ((mem_SfamAdm M).mp hS).1
  have hSnod : S.Nodup := by
    exact subsetsOf_nodup M.univX M.univX_nodup S ((mem_SfamAdm M).mp hS).1
  calc
    VfamAdm M k b = lmax l := rfl
    _ = bS S b := hEq.symm
    _ = bS ((suppList M b).filter (fun x => x ∈ S)) b := (bS_supp_trunc M b S hSsub hSnod).symm

/-! ## §4 · The count -/

/-- The horizons below `n` at which the value strictly drops. -/
noncomputable def strictDrop (M : DetMDP K X A D Y) (b : Mass K X) (n : Nat) :
    List Nat := by
  classical
  exact (List.range n).filter (fun k => VfamAdm M (k + 1) b < VfamAdm M k b)

theorem strictDrop_nodup (M : DetMDP K X A D Y) (b : Mass K X) (n : Nat) :
    (strictDrop M b n).Nodup := by
  classical
  have h : ((List.range n).filter
      (fun k => VfamAdm M (k + 1) b < VfamAdm M k b)).Nodup :=
    nodup_filterP (fun k => VfamAdm M (k + 1) b < VfamAdm M k b)
      (List.range n) (by simpa using (List.nodup_range : (List.range n).Nodup))
  simpa [strictDrop] using h

/-- **The value at a strict drop is never a value at another one.** If
`k₁ < k₂` and the sequence drops at `k₁`, then
`V_{k₂} ≤ V_{k₁+1} < V_{k₁}` by `VfamAdm_antitone`. -/
theorem strictDrop_value_inj (M : DetMDP K X A D Y) (b : Mass K X) (n : Nat) :
    ∀ k₁ ∈ strictDrop M b n, ∀ k₂ ∈ strictDrop M b n,
      VfamAdm M k₁ b = VfamAdm M k₂ b → k₁ = k₂ := by
  classical
  intro k₁ hk₁ k₂ hk₂ heq
  have hk₁f : k₁ ∈ (List.range n).filter
      (fun k => VfamAdm M (k + 1) b < VfamAdm M k b) := by simpa [strictDrop] using hk₁
  have hk₂f : k₂ ∈ (List.range n).filter
      (fun k => VfamAdm M (k + 1) b < VfamAdm M k b) := by simpa [strictDrop] using hk₂
  have hdrop₁ : VfamAdm M (k₁ + 1) b < VfamAdm M k₁ b := by
    simpa using (List.mem_filter.mp hk₁f).2
  cases Nat.le_total k₁ k₂ with
  | inl hle =>
      by_cases hkk : k₁ = k₂
      · exact hkk
      · have hlt : k₁ < k₂ := Nat.lt_of_le_of_ne hle hkk
        have hle₂ : VfamAdm M k₂ b ≤ VfamAdm M (k₁ + 1) b :=
          VfamAdm_antitone M (Nat.succ_le_of_lt hlt) b
        have hlt₁ : VfamAdm M k₂ b < VfamAdm M k₁ b := lt_of_le_of_lt hle₂ hdrop₁
        have hlt_self : VfamAdm M k₁ b < VfamAdm M k₁ b := by simpa [heq] using hlt₁
        exact False.elim ((not_le_of_lt hlt_self) (le_refl _))
  | inr hle =>
      by_cases hkk : k₂ = k₁
      · exact hkk.symm
      · have hlt : k₂ < k₁ := Nat.lt_of_le_of_ne hle hkk
        have hdrop₂ : VfamAdm M (k₂ + 1) b < VfamAdm M k₂ b := by
          simpa using (List.mem_filter.mp hk₂f).2
        have hle₁ : VfamAdm M k₁ b ≤ VfamAdm M (k₂ + 1) b :=
          VfamAdm_antitone M (Nat.succ_le_of_lt hlt) b
        have hlt₂ : VfamAdm M k₁ b < VfamAdm M k₂ b := lt_of_le_of_lt hle₁ hdrop₂
        have hlt_self : VfamAdm M k₂ b < VfamAdm M k₂ b := by simpa [heq] using hlt₂
        exact False.elim ((not_le_of_lt hlt_self) (le_refl _))

/-- **`prop:freeze`'s count.** For every horizon `n`, the number of strict
decreases among the first `n` horizons is at most `2^{|supp b|}`.

The value at each strict drop is distinct (`strictDrop_value_inj`), each
is the mass of a subset of the support (`VfamAdm_mem_range`), and there
are `2^{|supp b|}` subsets (`subsetsOf_length`). -/
theorem strictDrop_length_le (M : DetMDP K X A D Y) (b : Mass K X) (n : Nat) :
    (strictDrop M b n).length ≤ 2 ^ (suppList M b).length := by
  classical
  let vals := (strictDrop M b n).map (fun k => VfamAdm M k b)
  let cands := (subsetsOf (suppList M b)).map (fun S => bS S b)
  have hlen_cands : cands.length = 2 ^ (suppList M b).length := by
    simp [cands, subsetsOf_length]
  have hnod_vals : vals.Nodup := by
    unfold vals
    apply nodup_map_on_of_inj (fun k => VfamAdm M k b)
    · exact strictDrop_nodup M b n
    · exact strictDrop_value_inj M b n
  have hmem : ∀ v, v ∈ vals → v ∈ cands := by
    intro v hv
    rcases List.mem_map.mp hv with ⟨k, hk, rfl⟩
    rcases VfamAdm_mem_range M k b with ⟨T, hT, hEq⟩
    exact List.mem_map.mpr ⟨T, hT, hEq.symm⟩
  have hle : vals.length ≤ cands.length := nodup_mem_length_le hnod_vals hmem
  simpa [vals, hlen_cands] using hle

/-- **Corollary in the paper's wording**: no horizon witnesses more than
`2^{|supp b|}` strict decreases, so the sequence is constant once
`2^{|supp b|}` drops have occurred — it has nowhere left to go. Stated as
the contrapositive of the pigeonhole: if the drop list at some horizon is
longer than the bound, the list at every later horizon is too, which
`strictDrop_length_le` forbids. -/
theorem no_drop_beyond_bound (M : DetMDP K X A D Y) (b : Mass K X) (n : Nat)
    (hdone : (strictDrop M b n).length = 2 ^ (suppList M b).length) :
    ∀ m, n ≤ m → (strictDrop M b m).length = (strictDrop M b n).length := by
  classical
  intro m hnm
  apply Nat.le_antisymm
  · have hle_m : (strictDrop M b m).length ≤ 2 ^ (suppList M b).length :=
      strictDrop_length_le M b m
    simpa [hdone] using hle_m
  · apply nodup_mem_length_le (strictDrop_nodup M b n)
    intro k hk
    have hkf : k ∈ (List.range n).filter
        (fun j => VfamAdm M (j + 1) b < VfamAdm M j b) := by simpa [strictDrop] using hk
    have hkr : k ∈ List.range n := (List.mem_filter.mp hkf).1
    have hklt : k < n := List.mem_range.mp hkr
    have hkltm : k < m := Nat.lt_of_lt_of_le hklt hnm
    have : k ∈ (List.range m).filter
        (fun j => VfamAdm M (j + 1) b < VfamAdm M j b) :=
      List.mem_filter.mpr ⟨List.mem_range.mpr hkltm, (List.mem_filter.mp hkf).2⟩
    simpa [strictDrop] using this

end Formalizations.P3

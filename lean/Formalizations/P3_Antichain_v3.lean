/-
  Formalizations.P3_Antichain_v3
  ==============================

  Closes `prop:antichain` (iv):

  > (iv) the deficit is `1 - V_k(b) = min b(S^c)`, the minimum over the
  >      maximal survivable sets, and the min-mass bound is the special
  >      case `|S^c| = 1`.

  The paper's proof is one line: "`1 - max_S b(S) = min_S b(S^c)`".  That is
  correct, but it conceals two things the code has to make explicit, and
  stating them is most of the work here.

  **1. Normalization.**  `1 - b(S) = b(S^c)` needs `b(S) + b(S^c) = 1`,
  i.e. `lsum (univX.map b.f) = 1`.  The `Mass` structure carries `nonneg`
  but **no normalization field**, and the existing `total` is defined
  against `SafeMDP`, not the P3 `DetMDP`.  So normalization enters as an
  explicit hypothesis `hnorm`.  This is not a gap in the paper — every
  belief there is a probability distribution — but it is an assumption the
  code must name rather than inherit.

  **2. Why the *minimum* may be taken over maximal sets.**  This is not the
  same move as the maximum.  `S ⊆ T` gives `b(T^c) ≤ b(S^c)`, so the
  minimum of `b(S^c)` sits at the **largest** sets.  It is `prop:antichain`
  (ii) — every `S` lies below a maximal `T` — that licenses restricting the
  minimum to the maximal family.  So **(iv) is a corollary of (ii)**, and
  the dependency runs through `Vfam_prune_eq` from `P3_Antichain_v2`.

  ## Infrastructure

  `lmin`, `lmin_le`, `le_lmin` and `lmin_mem` already exist in
  `P3_ClassLattice`, where `lmin l` is defined as `-lmax (l.map (fun x => -x))`.
  A probe for `lmin` at top level misses them, because they live in namespace
  `Formalizations.P3` — so they are imported here rather than rebuilt.  What
  is genuinely missing is the max/min duality, supplied as `lmax_sub_dual`.

  The complement identity uses `lsum_filter_split` from `Prelude`, which
  conveniently needs **no** `Nodup` hypothesis — that is what makes it
  possible to avoid proving `nodup_append` for `S ++ S^c`.

  ## Contents

    lmax_sub_dual            the max/min duality
    sub_eq_of_add_eq         `a + c = o  ⟹  o - a = c`
    pIn, complOf             the indicator predicate and the complement set
    bS_compl                 `b(S) + b(S^c) = 1` (under `hnorm`)
    deficit_eq_min_compl     **(iv)**
    bS_compl_singleton       the min-mass special case `|S^c| = 1`
-/

import Formalizations.Prelude
import Formalizations.P3_Deterministic
import Formalizations.P3_Freeze_Noisy
import Formalizations.P3_ClassLattice
import Formalizations.P3_Antichain
import Formalizations.P3_Antichain_v2

namespace Formalizations.P3

open Formalizations
open Formalizations.POMDP

set_option linter.unusedSectionVars false

variable {K : Type} [OrdField K]
variable {X A D Y : Type}
variable [DecidableEq X]

/-! ## Minima of finite lists

`Prelude` supplies `lmax`, `lmax_isMax`, `le_lmax`, `lmax_le` and
`list_max_exists`, but nothing for minima.  The minimum is obtained by
duality rather than by a second `Classical.choose` over a bespoke
`list_min_exists` predicate — though the predicate is stated too, so that
`lmin` has the same shape as `lmax`. -/

/-- `a + c = o` rearranges to `o - a = c`. -/
theorem sub_eq_of_add_eq {a c o : K} (h : a + c = o) : o - a = c := by
  rw [← h]
  rw [sub_eq, add_assoc, add_comm c (-a), ← add_assoc, add_neg_cancel, zero_add]

/-- **Max/min duality.**  `1 - max f = min (1 - f)` over a nonempty finite
list.  Note this is *not* the same statement as the (ii)-based restriction
of the minimum to maximal sets; it is pure order algebra. -/
theorem lmax_sub_dual {β : Type} {l : List β} (h : l ≠ []) (f : β → K) :
    1 - lmax (l.map f) = lmin (l.map (fun x => 1 - f x)) := by
  apply le_antisymm
  · apply le_lmin (map_ne_nil (fun x => 1 - f x) h)
    intro z hz
    rcases List.mem_map.mp hz with ⟨x, hx, rfl⟩
    have hxle : f x ≤ lmax (l.map f) :=
      le_lmax (map_ne_nil f h) (List.mem_map.mpr ⟨x, hx, rfl⟩)
    simpa [sub_eq] using add_le_add (OrdField.le_refl (1 : K)) (neg_le_neg hxle)
  · rcases List.mem_map.mp (lmax_isMax (map_ne_nil f h)).1 with ⟨x, hx, hxmax⟩
    have hle : lmin (l.map (fun x => 1 - f x)) ≤ 1 - f x :=
      lmin_le (map_ne_nil (fun x => 1 - f x) h) (List.mem_map.mpr ⟨x, hx, rfl⟩)
    simpa [hxmax] using hle

/-! ## Complements -/

/-- The indicator predicate of `S`, as a `Bool` function (lists filter on
`Bool`, not on `Prop`). -/
def pIn (S : List X) : X → Bool := fun x => decide (x ∈ S)

/-- The complement `S^c` **relative to `M.univX`**.  Note the complement is
always taken against the support, not against an ambient type — `X` is not
assumed finite as a type. -/
def complOf (M : DetMDP K X A D Y) (S : List X) : List X :=
  M.univX.filter (fun x => !pIn S x)

theorem complOf_nodup (M : DetMDP K X A D Y) (S : List X) : (complOf M S).Nodup :=
  nodup_filter (fun x => !pIn S x) M.univX M.univX_nodup

/-- **The complement identity** `b(S) + b(S^c) = 1`.

Requires normalization `hnorm` (see the module header) and `S ⊆ univX`.
Proved by `lsum_filter_split` — which needs no `Nodup` — composed with
`lsum_eq_of_mem_iff` to replace `univX.filter (· ∈ S)` by `S` itself. -/
theorem bS_compl (M : DetMDP K X A D Y) (b : Mass K X) (S : List X)
    (hnorm : lsum (M.univX.map b.f) = 1) (hSn : S.Nodup)
    (hSub : subsetOf S M.univX) : bS S b + bS (complOf M S) b = 1 := by
  have hsplit := lsum_filter_split (pIn S) b.f M.univX
  have hfilter_eq : lsum ((M.univX.filter (pIn S)).map b.f) = lsum (S.map b.f) := by
    apply lsum_eq_of_mem_iff b.f
    · exact nodup_filter (pIn S) M.univX M.univX_nodup
    · exact hSn
    · intro x
      have : x ∈ M.univX.filter (pIn S) ↔ x ∈ M.univX ∧ x ∈ S := by simp [pIn]
      rw [this]
      exact ⟨fun h => h.2, fun h => ⟨hSub x h, h⟩⟩
  unfold bS
  rw [← hfilter_eq]
  change lsum ((M.univX.filter (pIn S)).map b.f) +
      lsum ((M.univX.filter (fun a => !pIn S a)).map b.f) = 1
  rw [hsplit]
  exact hnorm

/-! ## `prop:antichain` (iv) -/

/-- The pointwise identity behind (iv): on the maximal family,
`1 - b(S) = b(S^c)`.  Split out so both directions of the main theorem can
share it. -/
theorem deficit_point (M : DetMDP K X A D Y) (b : Mass K X) (k : Nat)
    (hnorm : lsum (M.univX.map b.f) = 1) (S : List X) (hS : S ∈ Pruned M k) :
    1 - bS S b = bS (complOf M S) b := by
  have hSfam : S ∈ Sfam M k := ((Pruned_mem M k).mp hS).1
  have hSn : S.Nodup := Sfam_mem_nodup M k hSfam
  have hSub : subsetOf S M.univX := by
    have hS' := hSfam
    simp [Sfam, List.mem_filter] at hS'
    exact subsetsOf_subset M.univX S hS'.1
  exact sub_eq_of_add_eq (bS_compl M b S hnorm hSn hSub)

/-- **`prop:antichain` (iv).**  The deficit is the minimum of `b(S^c)` over
the maximal survivable sets.

The minimum is over `Pruned M k` — the maximal family — which is legitimate
precisely because of (ii) (`Vfam_prune_eq`) together with antitonicity of
`b(S^c)` in `S`. -/
theorem deficit_eq_min_compl (M : DetMDP K X A D Y) (b : Mass K X) (k : Nat)
    (hnorm : lsum (M.univX.map b.f) = 1) :
    1 - Vfam M k b = lmin ((Pruned M k).map (fun S => bS (complOf M S) b)) := by
  rw [Vfam_prune_eq M b k]
  rw [lmax_sub_dual (Pruned_ne M k) (fun S => bS S b)]
  apply le_antisymm
  · apply le_lmin (map_ne_nil (fun S => bS (complOf M S) b) (Pruned_ne M k))
    intro z hz
    rcases List.mem_map.mp hz with ⟨S, hS, rfl⟩
    have hpoint := deficit_point M b k hnorm S hS
    rw [← hpoint]
    exact lmin_le (map_ne_nil (fun x => 1 - bS x b) (Pruned_ne M k))
      (List.mem_map.mpr ⟨S, hS, rfl⟩)
  · apply le_lmin (map_ne_nil (fun x => 1 - bS x b) (Pruned_ne M k))
    intro z hz
    rcases List.mem_map.mp hz with ⟨S, hS, rfl⟩
    have hpoint := deficit_point M b k hnorm S hS
    rw [hpoint]
    exact lmin_le (map_ne_nil (fun S => bS (complOf M S) b) (Pruned_ne M k))
      (List.mem_map.mpr ⟨S, hS, rfl⟩)

/-! ## The min-mass special case `|S^c| = 1` -/

/-- When the complement of `S` is a singleton `{x}`, `b(S^c) = b(x)` — the
min-mass bound of `prop:antichain` (iv).  The hypothesis `hsingle` says
`x` is the *only* support state outside `S`. -/
theorem bS_compl_singleton (M : DetMDP K X A D Y) (b : Mass K X) (S : List X)
    {x : X} (hxU : x ∈ M.univX) (hxS : x ∉ S)
    (hsingle : ∀ y, y ∈ M.univX → y ∉ S → y = x) :
    bS (complOf M S) b = b.f x := by
  unfold bS
  have hEq : lsum ((complOf M S).map b.f) = lsum ([x].map b.f) := by
    apply lsum_eq_of_mem_iff b.f
    · exact complOf_nodup M S
    · simp
    · intro y
      have hleft : y ∈ complOf M S ↔ y ∈ M.univX ∧ ¬y ∈ S := by
        simp [complOf, pIn]
      have hright : y ∈ [x] ↔ y = x := by simp
      rw [hleft, hright]
      constructor
      · intro h
        exact hsingle y h.1 h.2
      · intro hyx
        subst y
        exact ⟨hxU, hxS⟩
  simpa using hEq

end Formalizations.P3

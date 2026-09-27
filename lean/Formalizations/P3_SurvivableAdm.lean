/-
  Formalizations.P3_SurvivableAdm
  ===============================

  **The admissible blind family — the fidelity fix for `prop:antichain`'s
  `𝒮_k`.**

  `Survivable` (`P3_Freeze_Noisy:151`) is

      Survivable M S k := ∃ u : Nat → A, ∀ x, x ∈ S → survK M k u x

  with **no constraint that the schedule be admissible**. `prop:antichain`
  defines `𝒮_k` as the subsets of the support "jointly survivable by one
  **admissible** class-element", and `DetMDP` carries the admissible action
  set `univA` for exactly that purpose. So `Sfam` (hence `Vfam`, hence the
  formalizations of `prop:antichain` (i) and `prop:freeze`) range over a
  family that can be **larger** than the paper's: an inadmissible schedule
  can witness survivability whenever one exists that helps, and `Vfam` may
  then overstate the value.

  v29 reported this rather than patching it, because `P3_Freeze_Noisy`
  must not be edited. This module supplies the corrected objects
  additively, and proves what relates them to the old ones:

    SurvivableAdm      survivability by an **admissible** schedule
    SurvivableAdm_iff_Wblind   it is exactly `𝒲_k`-viability (`Wblind`)
    SfamAdm, VfamAdm   the corrected family and its value
    SfamAdm_subset_Sfam        the old family is a superset  (the defect)
    SfamAdm_subset_SfamFB      admissible-blind ⊆ feedback
    VfamAdm_le_Vfam            the old value dominates      (the defect)
    VfamAdm_le_VFb             **the value of observation, at operator level**
    VfamAdm_antitone, _card_le, _finite_range   `prop:freeze` for the
                                                corrected family

  Two points worth stating plainly.

  **1. `SurvivableAdm_iff_Wblind` is the bridge that was missing.**  It
  says the corrected blind family is *exactly* the `𝒲_k`-viable sets of
  `P3_Viable` — so the three blind notions (`SurvivableAdm`, `Wblind`, and
  `survK`-survivability under an admissible schedule) are one notion, and
  v27's `Wblind_iff_survK` now has a family-level reading.

  **2. `VfamAdm_le_VFb` is the value of observation.**  A schedule is the
  degenerate policy `fun _ => a`, so every admissible-blind-survivable set
  is feedback-survivable, and the maximum over the larger family dominates:
  `V^{blind}_k(b) ≤ V^{fb}_k(b)`. This is the operator-level form of the
  gap that `thm:lattice` realizes as `1/2` at the symmetric prior, and it
  is strict in general — `P3_Feedback`'s counterexample separates the two
  families at `k = 2`.

  Nothing here depends on the defect: the new family is the strict one.
-/

import Formalizations.Prelude
import Formalizations.P3_Deterministic
import Formalizations.P3_Freeze_Noisy
import Formalizations.P3_Bridge
import Formalizations.P3_Viable
import Formalizations.P3_Feedback
import Formalizations.P3_FeedbackValue

namespace Formalizations.P3

open Formalizations
open Formalizations.POMDP

set_option linter.unusedSectionVars false

variable {K : Type} [OrdField K]
variable {X A D Y : Type}

/-! ## The admissible blind notion -/

/-- **`S` is `k`-step survivable by an admissible schedule.**  This is
`prop:antichain`'s "jointly survivable by one admissible class-element"
for a blind class; `Survivable` (`P3_Freeze_Noisy`) is the same statement
without the `univA` constraint. -/
def SurvivableAdm (M : DetMDP K X A D Y) (S : List X) (k : Nat) : Prop :=
  ∃ u : Nat → A, (∀ i, u i ∈ M.univA) ∧ ∀ x, x ∈ S → survK M k u x

/-- **The corrected family is exactly `𝒲_k`-viability.**  `Wblind_iff_survK`
(`P3_Viable`) reads `Wblind M k B ↔ ∃ u, (∀ i, u i ∈ univA) ∧ ∀ x, B x →
survK M k u x`; taking `B := (· ∈ S)` makes the right-hand side
`SurvivableAdm`. -/
theorem SurvivableAdm_iff_Wblind (M : DetMDP K X A D Y) (S : List X)
    (k : Nat) : SurvivableAdm M S k ↔ Wblind M k (fun x => x ∈ S) := by
  unfold SurvivableAdm
  exact (Wblind_iff_survK M k (fun x => x ∈ S)).symm

/-- The old, weaker notion follows.  This inclusion is exactly the defect:
it can be strict. -/
theorem SurvivableAdm_le_Survivable (M : DetMDP K X A D Y) (S : List X)
    (k : Nat) : SurvivableAdm M S k → Survivable M S k := by
  rintro ⟨u, _hadm, hu⟩
  exact ⟨u, hu⟩

/-- Surviving longer implies surviving shorter, admissibly. -/
theorem SurvivableAdm_succ (M : DetMDP K X A D Y) (S : List X) (k : Nat) :
    SurvivableAdm M S (k + 1) → SurvivableAdm M S k := by
  rintro ⟨u, hadm, hu⟩
  exact ⟨u, hadm, fun x hx => survK_mono_succ M k u x (hu x hx)⟩

theorem SurvivableAdm_mono (M : DetMDP K X A D Y) (S : List X) {k n : Nat}
    (hkn : k ≤ n) : SurvivableAdm M S n → SurvivableAdm M S k := by
  rintro ⟨u, hadm, hu⟩
  exact ⟨u, hadm, fun x hx => survK_mono M hkn u x (hu x hx)⟩

/-! ## The corrected family -/

/-- **The admissible blind family `𝒮_k`.**  `Sfam` filtered by
`SurvivableAdm` instead of `Survivable`. -/
noncomputable def SfamAdm (M : DetMDP K X A D Y) (k : Nat) : List (List X) := by
  classical
  exact (subsetsOf M.univX).filter (fun S => SurvivableAdm M S k)

theorem mem_SfamAdm (M : DetMDP K X A D Y) {k : Nat} {S : List X} :
    S ∈ SfamAdm M k ↔ S ∈ subsetsOf M.univX ∧ SurvivableAdm M S k := by
  unfold SfamAdm
  classical
  simp [List.mem_filter]

/-- The family is inhabited: the empty set is vacuously survivable, by any
admissible schedule. -/
theorem SfamAdm_ne (M : DetMDP K X A D Y) (k : Nat) : SfamAdm M k ≠ [] := by
  apply ne_nil_of_exists_mem
  refine ⟨[], ?_⟩
  rw [mem_SfamAdm]
  constructor
  · exact nil_mem_subsetsOf M.univX
  · rcases exists_mem_of_ne_nil M.univA_ne with ⟨a0, ha0⟩
    exact ⟨fun _ => a0, fun _ => ha0, by intro x hx; cases hx⟩

/-- **Nesting `𝒮_{k+1} ⊆ 𝒮_k`** for the corrected family — the hypothesis
`prop:freeze` needs. -/
theorem SfamAdm_nesting (M : DetMDP K X A D Y) :
    ∀ k, ∀ S, S ∈ SfamAdm M (k + 1) → S ∈ SfamAdm M k := by
  intro k S h
  rw [mem_SfamAdm] at h ⊢
  exact ⟨h.1, SurvivableAdm_succ M S k h.2⟩

theorem SfamAdm_mono (M : DetMDP K X A D Y) {k n : Nat} (hkn : k ≤ n) :
    ∀ S, S ∈ SfamAdm M n → S ∈ SfamAdm M k := by
  intro S h
  rw [mem_SfamAdm] at h ⊢
  exact ⟨h.1, SurvivableAdm_mono M S hkn h.2⟩

/-- **The old family is a superset** — quantified statement of the defect. -/
theorem SfamAdm_subset_Sfam (M : DetMDP K X A D Y) :
    ∀ k, ∀ S, S ∈ SfamAdm M k → S ∈ Sfam M k := by
  intro k S h
  rw [mem_SfamAdm] at h
  unfold Sfam
  classical
  simp [List.mem_filter]
  exact ⟨h.1, SurvivableAdm_le_Survivable M S k h.2⟩

/-- **Admissible-blind survivability implies feedback survivability**: a
schedule is the policy that ignores its observation history. -/
theorem SurvivableAdm_le_Wmem (M : DetMDP K X A D Y) (S : List X) (k : Nat) :
    SurvivableAdm M S k → Wmem M k (fun x => x ∈ S) := by
  intro h
  exact Wblind_le_Wmem M k (fun x => x ∈ S) ((SurvivableAdm_iff_Wblind M S k).mp h)

/-- …and at the level of families. -/
theorem SfamAdm_subset_SfamFB (M : DetMDP K X A D Y) :
    ∀ k, ∀ S, S ∈ SfamAdm M k → S ∈ SfamFB M k := by
  intro k S h
  rw [mem_SfamAdm] at h
  rw [mem_SfamFB]
  exact ⟨h.1, SurvivableAdm_le_Wmem M S k h.2⟩

/-! ## The corrected value -/

/-- `V_k(b) = max_{S ∈ 𝒮_k} b(S)` on the **admissible** blind family —
`prop:antichain` (i) as the paper states it. -/
noncomputable def VfamAdm (M : DetMDP K X A D Y) (k : Nat) (b : Mass K X) : K :=
  lmax ((SfamAdm M k).map (fun S => bS S b))

/-- **The old value dominates the corrected one** — the defect made
`Vfam` an over-estimate. -/
theorem VfamAdm_le_Vfam (M : DetMDP K X A D Y) (k : Nat) (b : Mass K X) :
    VfamAdm M k b ≤ Vfam M k b := by
  unfold VfamAdm Vfam
  apply lmax_le_lmax_of_subset (map_ne_nil (fun S => bS S b) (SfamAdm_ne M k))
  intro z hz
  rcases List.mem_map.mp hz with ⟨S, hS, rfl⟩
  exact List.mem_map.mpr ⟨S, SfamAdm_subset_Sfam M k S hS, rfl⟩

/-- **The value of observation, at operator level**: the feedback value
dominates the admissible blind value.  Strict in general —
`P3_Feedback.Wmem_not_le_Wblind` separates the two families. -/
theorem VfamAdm_le_VFb (M : DetMDP K X A D Y) (k : Nat) (b : Mass K X) :
    VfamAdm M k b ≤ VFb M k b := by
  unfold VfamAdm VFb
  apply lmax_le_lmax_of_subset (map_ne_nil (fun S => bS S b) (SfamAdm_ne M k))
  intro z hz
  rcases List.mem_map.mp hz with ⟨S, hS, rfl⟩
  exact List.mem_map.mpr ⟨S, SfamAdm_subset_SfamFB M k S hS, rfl⟩

/-- **`prop:freeze` on the corrected family**: the value is non-increasing
in the horizon. -/
theorem VfamAdm_antitone (M : DetMDP K X A D Y) {k n : Nat} (hkn : k ≤ n)
    (b : Mass K X) : VfamAdm M n b ≤ VfamAdm M k b := by
  unfold VfamAdm
  apply lmax_le_lmax_of_subset (map_ne_nil (fun S => bS S b) (SfamAdm_ne M n))
  intro z hz
  rcases List.mem_map.mp hz with ⟨S, hS, rfl⟩
  exact List.mem_map.mpr ⟨S, SfamAdm_mono M hkn S hS, rfl⟩

/-- The cardinal bound behind `prop:freeze`, on the corrected family. -/
theorem SfamAdm0_card_le (M : DetMDP K X A D Y) :
    (SfamAdm M 0).length ≤ 2 ^ M.univX.length := by
  calc
    (SfamAdm M 0).length ≤ (subsetsOf M.univX).length := by
        unfold SfamAdm
        classical
        exact length_filter_le (subsetsOf M.univX) (fun S => SurvivableAdm M S 0)
    _ = 2 ^ M.univX.length := subsetsOf_length M.univX

/-- Every corrected value is attained by a set of the frozen family, so the
range of `k ↦ V_k(b)` is finite — the stabilization claim. -/
theorem VfamAdm_finite_range (M : DetMDP K X A D Y) (k : Nat) (b : Mass K X) :
    ∃ S, S ∈ SfamAdm M 0 ∧ VfamAdm M k b = bS S b := by
  unfold VfamAdm
  have hne : (SfamAdm M k).map (fun S => bS S b) ≠ [] :=
    map_ne_nil (fun S => bS S b) (SfamAdm_ne M k)
  rcases List.mem_map.mp (lmax_isMax hne).1 with ⟨S, hS, hval⟩
  exact ⟨S, SfamAdm_mono M (Nat.zero_le k) S hS, hval.symm⟩

end Formalizations.P3

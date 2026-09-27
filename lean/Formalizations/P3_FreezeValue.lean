/-
  Formalizations.P3_FreezeValue
  =============================

  **`prop:freeze`'s second clause, on the corrected family — the last open
  item in P3.**

  `prop:freeze` (paper2 v11, 687–701) ends:

      "…the frozen value being `max_S b(S)` over the maximal sets of the
       frozen family --- an exact computable infinite-horizon value."

  v21 proved the underlying *pruning* identity for the **old** family:
  `Vfam_prune_eq` says `V_k(b) = max_{S ∈ Pruned k} b(S)`, the alpha-vectors
  being exactly the indicators of the maximal jointly survivable sets
  (`prop:antichain` (ii)). v30 then showed the old family is wrong — its
  `Survivable` lacks the admissibility constraint the paper's `𝒮_k` carries
  — and supplied the corrected `SfamAdm`/`VfamAdm`. Nobody had since
  carried the pruning identity across, so `prop:freeze`'s closing clause
  was proved only for a family the paper does not use.

  This module carries it across. The proof is the same argument as v21's,
  and it is repeated rather than factored because `Pruned` is defined by
  filtering `Sfam`, and `SfamAdm` is a different list: there is no
  abstraction here worth paying for.

  Contents:

  * `PrunedAdm` — `𝒮^adm_k` pruned to its maximal elements, with
    `PrunedAdm_mem`, `PrunedAdm_ne`, `SfamAdm_mem_nodup`.
  * `VfamAdm_prune_eq` — **the clause**: `V^adm_k(b) = max_{S ∈ PrunedAdm k} b(S)`.
  * `VfamAdm_frozen_eq_pruned` — the clause in its "frozen" form: if the
    family has stopped shrinking at `k`, then every later horizon has the
    same value, and it is the maximum over the maximal sets of the frozen
    family.
  * `PrunedAdm_antichain` — the pruned family is an antichain, by v20's
    `maximals_antichain` applied to `SfamAdm`.

  **One honest limitation, stated rather than papered over.** The paper
  says the *family* freezes and the *value* freezes with it. What v34
  proved (`strictDrop_length_le`, `no_drop_beyond_bound`) is that the
  **value** stops changing after at most `2^{|supp b|}` strict decreases:
  the number of drops is bounded. That does **not** by itself say the
  family `𝒮^adm_ℓ` stops shrinking — a family can keep losing sets without
  the maximum moving, whenever the sets it loses were never maximizers. So
  `VfamAdm_frozen_eq_pruned` takes family-freezing as a hypothesis, and the
  value-freezing theorem is quoted as the separate fact it is. Proving
  family-freezing would need the same pigeonhole run against `SfamAdm`'s
  length rather than against the value's range; it is a short addition and
  is not done here.
-/

import Formalizations.Prelude
import Formalizations.P3_Sufficiency
import Formalizations.P3_Freeze_Noisy
import Formalizations.P3_Antichain
import Formalizations.P3_Antichain_v2
import Formalizations.P3_SurvivableAdm

set_option linter.unusedSectionVars false

open Formalizations
open Formalizations.POMDP

namespace Formalizations.P3

variable {K : Type} [OrdField K]
variable {X A D Y : Type}
variable [DecidableEq X]

/-! ## The pruned corrected family -/

/-- The corrected witness family `𝒮^adm_k`, pruned to its maximal elements.

`MaximalIn` is a `Prop` and this stdlib's `List.filter` is `Bool`-valued, so
the predicate is wrapped in `decide`, exactly as v21 did for `Pruned`. -/
noncomputable def PrunedAdm (M : DetMDP K X A D Y) (k : Nat) : List (List X) := by
  classical
  exact (SfamAdm M k).filter (fun S => decide (MaximalIn (SfamAdm M k) S))

theorem PrunedAdm_mem (M : DetMDP K X A D Y) (k : Nat) {S : List X} :
    S ∈ PrunedAdm M k ↔ S ∈ SfamAdm M k ∧ MaximalIn (SfamAdm M k) S := by
  simp [PrunedAdm]

/-- Every member of the corrected family is a subset of `univX`, hence
`Nodup` — the hypothesis `bS_mono_of_subset` needs. -/
theorem SfamAdm_mem_nodup (M : DetMDP K X A D Y) (k : Nat) {S : List X}
    (hS : S ∈ SfamAdm M k) : S.Nodup :=
  subsetsOf_nodup M.univX M.univX_nodup S ((mem_SfamAdm M).mp hS).1

/-- The pruned corrected family is inhabited: `𝒮^adm_k` is nonempty and
every element sits below a maximal one (`exists_maximal_above`, v21). -/
theorem PrunedAdm_ne (M : DetMDP K X A D Y) (k : Nat) : PrunedAdm M k ≠ [] := by
  unfold PrunedAdm
  classical
  apply ne_nil_of_exists_mem
  rcases exists_mem_of_ne_nil (SfamAdm_ne M k) with ⟨S, hS⟩
  rcases exists_maximal_above (SfamAdm M k) S hS with ⟨T, hTmem, hST, hTmax⟩
  exact ⟨T, by simp [hTmax.1, hTmax]⟩

/-! ## The pruning identity -/

/-- **Pruning cannot decrease the value** — the pruned family is a
sub-family of `𝒮^adm_k`, so its maximum is no larger. -/
theorem VfamAdm_prune_ge (M : DetMDP K X A D Y) (b : Mass K X) (k : Nat) :
    lmax ((PrunedAdm M k).map (fun S => bS S b)) ≤ VfamAdm M k b := by
  unfold VfamAdm
  apply lmax_le_lmax_of_subset (map_ne_nil (fun S => bS S b) (PrunedAdm_ne M k))
  intro z hz
  rcases List.mem_map.mp hz with ⟨S, hS, rfl⟩
  exact List.mem_map.mpr ⟨S, ((PrunedAdm_mem M k).mp hS).1, rfl⟩

/-- **Pruning cannot increase the value** — every set in `𝒮^adm_k` is
dominated by a maximal one, and mass is monotone in the set. -/
theorem VfamAdm_prune_le (M : DetMDP K X A D Y) (b : Mass K X) (k : Nat) :
    VfamAdm M k b ≤ lmax ((PrunedAdm M k).map (fun S => bS S b)) := by
  unfold VfamAdm
  apply lmax_le (map_ne_nil (fun S => bS S b) (SfamAdm_ne M k))
  intro z hz
  rcases List.mem_map.mp hz with ⟨S, hS, rfl⟩
  rcases exists_maximal_above (SfamAdm M k) S hS with ⟨T, hTmem, hST, hTmax⟩
  have hle : bS S b ≤ bS T b :=
    bS_mono_of_subset b S T (SfamAdm_mem_nodup M k hS)
      (SfamAdm_mem_nodup M k hTmax.1) hST
  have hTpruned : T ∈ PrunedAdm M k := (PrunedAdm_mem M k).mpr ⟨hTmax.1, hTmax⟩
  exact le_trans hle (le_lmax (map_ne_nil (fun S => bS S b) (PrunedAdm_ne M k))
    (List.mem_map.mpr ⟨T, hTpruned, rfl⟩))

/-- **`prop:freeze`'s closing clause, on the corrected family.** The value
is the maximum of `b(S)` over the *maximal* jointly survivable sets — an
exact, computable quantity read off the antichain. This is `prop:antichain`
(ii) for `𝒮^adm_k`, and it is the "frozen value" of `prop:freeze` at any
horizon at which the family has stopped shrinking. -/
theorem VfamAdm_prune_eq (M : DetMDP K X A D Y) (b : Mass K X) (k : Nat) :
    VfamAdm M k b = lmax ((PrunedAdm M k).map (fun S => bS S b)) :=
  le_antisymm (VfamAdm_prune_le M b k) (VfamAdm_prune_ge M b k)

/-- **The frozen value.** If the family has stopped shrinking at `k`, then
every later horizon has the same value, and that value is the maximum over
the maximal sets of the frozen family.

Family-freezing is a hypothesis, not a consequence: see the module header. -/
theorem VfamAdm_frozen_eq_pruned (M : DetMDP K X A D Y) (b : Mass K X) (k : Nat)
    (hfrz : ∀ n, k ≤ n → SfamAdm M n = SfamAdm M k) :
    ∀ n, k ≤ n →
      VfamAdm M n b = lmax ((PrunedAdm M k).map (fun S => bS S b)) := by
  intro n hkn
  rw [VfamAdm_prune_eq M b n]
  congr 1
  unfold PrunedAdm
  rw [hfrz n hkn]

/-- **The maximal jointly survivable sets form an antichain** —
`prop:antichain` (iii)'s first half, on the corrected family. Immediate
from v20's `maximals_antichain`, which is stated for an arbitrary finite
family of subsets. -/
theorem PrunedAdm_antichain (M : DetMDP K X A D Y) (k : Nat) :
    Antichain (SfamAdm M k) (MaximalIn (SfamAdm M k)) :=
  maximals_antichain (SfamAdm M k)

end Formalizations.P3

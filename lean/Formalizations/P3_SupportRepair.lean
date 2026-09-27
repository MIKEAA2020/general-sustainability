/-
  Formalizations.P3_SupportRepair
  ===============================

  **Repair A, and what it costs downstream.**

  v32 established that `thm:support` as printed is false: it names the
  unrestricted sequential class (value `VFb`, viability `Wmem`) but pairs
  it with the blind recursion `Wblind`. The adopted repair is **A** — keep
  the class, restate `𝒲_k` as the *feedback* recursion — with a remark
  covering the blind window (repair C).

  This module does three things repair A requires.

  **§1.** Consequence 2 of `thm:support` in the paper's literal form. v29
  proved `VFb_min_mass_bound` as `mn ≤ totalD(b) - VFb_k(b)`; the paper
  writes `1 - V_k(b) ≥ min_{x ∈ supp b} b(x)`. As with v32 §1, `Mass`
  carries no normalization, so the literal form is a corollary with
  `totalD M b = 1` named as a hypothesis.

  **§2.** The paper's *belief-space* viability family `𝒲^{bel}_k`
  (`prop:deficit`, paper line 789): "the family of beliefs whose support
  admits a jointly surviving **declared-class** sequence". That is the
  belief-space form of the **blind** recursion, not of the feedback one.
  `Wbel` is that family, and `deficit_min_mass_of_not_Wbel` is
  `prop:deficit` (ii) stated in the paper's own vocabulary — previously it
  was only available as `min_mass_bound` (v12), which says the same thing
  with the hypothesis spelled out per-tuple instead of via `𝒲^{bel}_k`.

  **§3.** The cost of repair A, in code. If `𝒲_k` (state space) is
  redefined as the feedback recursion while `𝒲^{bel}_k` (belief space)
  keeps its published definition — declared-class, i.e. blind — then the
  paper's sentence at line 252, that `𝒲^{bel}_k` is "its belief-space
  analogue", becomes **false**. `Wfbel` is the belief-space analogue of the
  repaired `𝒲_k`, and `Wfbel_not_Wbel` exhibits a normalized belief in
  `Wfbel` but not in `Wbel`: the same counterexample as v32, read as a
  statement about the two symbols rather than about the theorem.

  Nothing here is a new theorem about the model; it is the repair and its
  bookkeeping, so that the paper's edit can be checked against something
  that compiles.
-/

import Formalizations.Prelude
import Formalizations.P3_Deterministic
import Formalizations.P3_Sufficiency
import Formalizations.P3_Viable
import Formalizations.P3_Feedback
import Formalizations.P3_FeedbackValue
import Formalizations.P3_BlindValue
import Formalizations.P3_SurvivableAdm
import Formalizations.P3_Rational
import Formalizations.P3_SupportValue

open Formalizations
open Formalizations.POMDP

namespace Formalizations.P3

variable {K : Type} [OrdField K]
variable {X A D Y : Type}

/-! ## §1 · Consequence 2 of `thm:support`, literally, under repair A -/

/-- **`thm:support`, consequence 2, repaired.** If the support is not
`𝒲_k`-viable **on the feedback reading** — which is the reading repair A
adopts — then `1 - V_k(b) ≥ min_{x ∈ supp(b)} b(x)`.

The minimum is over the support only (`hmn` quantifies `b.f x ≠ 0`), as in
`VFb_min_mass_bound`; `min_mass_bound` (v12) is the blind-class twin and
quantifies over all of `univX`. -/
theorem VFb_min_mass_bound_one (M : DetMDP K X A D Y) (k : Nat) (b : Mass K X)
    (mn : K)
    (hnorm : totalD M b = 1)
    (hmn : ∀ x, x ∈ M.univX → b.f x ≠ 0 → mn ≤ b.f x)
    (hlost : ¬ Wmem M k (suppPred M b)) :
    mn ≤ 1 - VFb M k b := by
  rw [← hnorm]
  exact VFb_min_mass_bound M k b mn hmn hlost

/-! ## §2 · `𝒲^{bel}_k` and `prop:deficit` (ii) -/

/-- **The belief-space viability family** (`prop:deficit`, paper line 789):
the beliefs whose support admits a jointly surviving **declared-class**
sequence. Declared-class is the blind class, so this is the belief-space
form of `Wblind`. -/
def Wbel (M : DetMDP K X A D Y) (k : Nat) (b : Mass K X) : Prop :=
  Wblind M k (suppPred M b)

/-- Membership in `𝒲^{bel}_k` is exactly blind viability of the support. -/
theorem mem_Wbel (M : DetMDP K X A D Y) (k : Nat) (b : Mass K X) :
    Wbel M k b ↔ Wblind M k (suppPred M b) := Iff.rfl

/-- **`prop:deficit` (ii), in the paper's own vocabulary.** For a
normalized belief outside `𝒲^{bel}_k`, the deficit is at least the smallest
branch mass.

Same content as `min_mass_bound` (v12); the difference is that the
hypothesis is `b ∉ 𝒲^{bel}_k`, as the paper states it, rather than a
per-tuple loss predicate. The step between the two is downward closure of
`Wblind` (`Wblind_downward`, v27) applied to a tuple's surviving set. -/
theorem deficit_min_mass_of_not_Wbel (M : DetMDP K X A D Y) (k : Nat)
    (b : Mass K X) (mn : K)
    (hnorm : totalD M b = 1)
    (hmn : ∀ x, x ∈ M.univX → mn ≤ b.f x)
    (hnot : ¬ Wbel M k b) :
    mn ≤ 1 - VR M k b := by
  classical
  apply min_mass_bound M k b mn hnorm hmn
  intro t ht
  rcases exists_mem_of_ne_nil M.univA_ne with ⟨a0, ha0⟩
  have hSfam : survSet M t ∈ SfamAdm M k := survSet_mem_SfamAdm M a0 ha0 k t ht
  have hx0 : ∃ x0, x0 ∈ M.univX ∧ b.f x0 ≠ 0 ∧ x0 ∉ survSet M t := by
    by_cases h : ∃ x0, x0 ∈ M.univX ∧ b.f x0 ≠ 0 ∧ x0 ∉ survSet M t
    · exact h
    · exfalso
      apply hnot
      unfold Wbel
      apply Wblind_downward M k (fun x => x ∈ survSet M t) (suppPred M b)
      · intro x hx
        by_cases hxS : x ∈ survSet M t
        · exact hxS
        · exact False.elim (h ⟨x, hx.1, hx.2, hxS⟩)
      · exact (SurvivableAdm_iff_Wblind M (survSet M t) k).mp
          ((mem_SfamAdm M).mp hSfam).2
  rcases hx0 with ⟨x0, hx0u, hx0ne, hx0S⟩
  have hfalse : survT M t x0 = false := by
    by_cases hf : survT M t x0 = false
    · exact hf
    · have htrue : survT M t x0 = true := by
        cases hs : survT M t x0 <;> simp_all
      exact False.elim (hx0S (by simp [survSet, hx0u, htrue]))
  exact ⟨x0, hx0u, hx0ne, hfalse⟩

/-! ## §3 · What repair A does to the paper's notation -/

/-- The belief-space analogue of the **repaired** `𝒲_k`: the beliefs whose
support is viable for the unrestricted sequential class. -/
def Wfbel (M : DetMDP K X A D Y) (k : Nat) (b : Mass K X) : Prop :=
  Wmem M k (suppPred M b)

/-- On a blind window the two belief-space families coincide — repair C,
at belief level. -/
theorem Wfbel_eq_Wbel_of_blind (M : DetMDP K X A D Y) (y0 : Y)
    (hblind : ∀ x a x', M.obs x a x' = y0) (k : Nat) (b : Mass K X) :
    Wfbel M k b ↔ Wbel M k b := by
  unfold Wfbel Wbel
  exact Wmem_eq_Wblind_of_blind M y0 hblind k (suppPred M b)

/-- **The two belief-space families differ**, on a normalized belief, under
`thm:support`'s own hypotheses (deterministic kernels, deterministic
observation map — `wm_detKernel`, v28).

This is the notation defect repair A would introduce if applied
incautiously: with `𝒲_k` redefined as the feedback recursion and `𝒲^{bel}_k`
left as published (declared-class, i.e. blind), paper line 252's
description of `𝒲^{bel}_k` as "its belief-space analogue" is false. The
witness is the same belief as v32's `paper_literal_thm_support_fails`:
mass `1/2` on each of `p` and `q`. -/
theorem Wfbel_not_Wbel :
    ∃ (M : DetMDP Rat WmX WmA WmD Bool) (k : Nat) (b : Mass Rat WmX),
      totalD M b = 1 ∧ Wfbel M k b ∧ ¬ Wbel M k b :=
  ⟨wmModel Rat, 2, wmBelief, wmBelief_total,
    (by simpa [Wfbel, wmBelief_supp] using (wm_Wmem Rat)),
    (by simpa [Wbel, wmBelief_supp] using (wm_not_Wblind Rat))⟩

end Formalizations.P3

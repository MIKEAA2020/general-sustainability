/-
  Formalizations.P3_SupportValue
  ==============================

  **`thm:support` in the form the paper states it — and the cost of that
  form.**

  The paper (paper2 v11, lines 314–323):

      "Consequently, for the unrestricted sequential class,
       `V_k(b) = 1` if and only if `supp(b) ∈ 𝒲_k`, while if
       `supp(b) ∉ 𝒲_k` then every policy loses a compatible state of
       positive mass along its realized observation path (the loss can
       occur at any stage), so `1 - V_k(b) ≥ min_{x ∈ supp(b)} b(x)`.
       Moreover `V_k(b)` is non-increasing in `k`."

  The layer has had the substance of this since v29/v30, but stated with
  `totalD M b` where the paper writes `1`:

      `VFb_eq_total_iff_Wmem`   (v29)   `VFb_k(b) = totalD(b) ⟺ supp(b) ∈ 𝒲_k^mem`
      `VR_eq_total_iff_Wblind`  (v30)   `VR_k(b)  = totalD(b) ⟺ supp(b) ∈ 𝒲_k`

  That is not a cosmetic difference. `Mass` (`P1_BeliefSafety:169`) carries
  **no normalization** — only `nonneg` — so `totalD M b = 1` is a
  *hypothesis*, not a theorem. The paper writes `1` because a belief in the
  paper is normalized; the layer cannot know that about an arbitrary `Mass`.
  §1 below supplies the literal statements, with the hypothesis made
  explicit rather than assumed away.

  §2 is the point of the module. The paper's `𝒲_k` (lines 302–304) is

      `𝒲_0 = {B ⊆ 𝒱}`,
      `𝒲_k = {B : some admissible a maps every x ∈ B into
                   𝒲_{k-1}-supported posteriors}`

  — one action for the whole set, with no case split on the observation,
  which is the **blind** recursion `Wblind` (v27). But the theorem is stated
  for **the unrestricted sequential class**, whose value is `VFb` and whose
  viability notion is `Wmem`. v28 proved these differ
  (`Wmem_not_le_Wblind`, on a model with deterministic kernels and a
  deterministic observation map — i.e. under `thm:support`'s own
  hypotheses).

  So the paper's sentence, read literally, asserts

      `VFb_k(b) = 1`  ⟺  `supp(b) ∈ Wblind k`

  and §2.1 exhibits a normalized belief on which the left side holds and
  the right side does not. The statement is therefore **false as written**,
  and the theorem is not a matter of the layer catching up with the paper:
  the paper needs an edit. §2.2 gives the two repairs, both of which the
  layer already proves — and both of which are what the paper should say.

  Nothing here assumes `Mass` is normalized except where `hnorm` is named.
-/

import Formalizations.Prelude
import Formalizations.P3_Deterministic
import Formalizations.P3_Sufficiency
import Formalizations.P3_Viable
import Formalizations.P3_Feedback
import Formalizations.P3_FeedbackValue
import Formalizations.P3_BlindValue
import Formalizations.P3_Rational

open Formalizations
open Formalizations.POMDP

namespace Formalizations.P3

variable {K : Type} [OrdField K]
variable {X A D Y : Type}

/-! ## §1 · `thm:support` in the paper's literal form -/

/-- **`thm:support`, consequence 1, feedback reading, as the paper states
it.** `V_k(b) = 1` exactly when the support is `𝒲_k`-viable.

The hypothesis `hnorm` is exactly the normalization the paper builds into
the word "belief"; `Mass` does not carry it, so it is a hypothesis here. -/
theorem VFb_eq_one_iff_Wmem (M : DetMDP K X A D Y) (k : Nat) (b : Mass K X)
    (hnorm : totalD M b = 1) :
    VFb M k b = 1 ↔ Wmem M k (suppPred M b) := by
  rw [← hnorm]
  exact VFb_eq_total_iff_Wmem M k b

/-- **The contrapositive, strictly** — the paper's "if `supp(b) ∉ 𝒲_k` then
every policy loses a compatible state of positive mass". Stated as a strict
inequality rather than a deficit bound: the value is *below* `1`, not
merely `≤ 1`, and `VFb_min_mass_bound` (v29) upgrades the gap to
`≥ min_x b(x)`. -/
theorem VFb_lt_one_of_not_Wmem (M : DetMDP K X A D Y) (k : Nat) (b : Mass K X)
    (hnorm : totalD M b = 1) (hlost : ¬ Wmem M k (suppPred M b)) :
    VFb M k b < 1 := by
  rw [← hnorm]
  exact VFb_lt_total_of_not_Wmem M k b hlost

/-- **`thm:support`, consequence 1, blind reading, literally.** For the
declared sequential-blind class the value is `1` exactly when the support
lies in the paper's `𝒲_k` — this is the reading on which the paper's `V_k`
denotes `VR_k`. -/
theorem VR_eq_one_iff_Wblind (M : DetMDP K X A D Y) (k : Nat) (b : Mass K X)
    (hnorm : totalD M b = 1) :
    VR M k b = 1 ↔ Wblind M k (suppPred M b) := by
  rw [← hnorm]
  exact VR_eq_total_iff_Wblind M k b

theorem VR_lt_one_of_not_Wblind (M : DetMDP K X A D Y) (k : Nat) (b : Mass K X)
    (hnorm : totalD M b = 1) (hlost : ¬ Wblind M k (suppPred M b)) :
    VR M k b < 1 := by
  rw [← hnorm]
  exact VR_lt_total_of_not_Wblind M k b hlost

/-- **Consequence 3 in the paper's normalization**: the value is
non-increasing in the horizon. -/
theorem VFb_antitone_one (M : DetMDP K X A D Y) {k n : Nat} (hkn : k ≤ n)
    (b : Mass K X) : VFb M n b ≤ VFb M k b :=
  VFb_antitone M hkn b

/-! ## §2 · The paper's sentence, read literally, is false

The two readings of `𝒲_k` differ (`Wmem_not_le_Wblind`, v28), the paper's
theorem names the unrestricted sequential class, and the paper's `𝒲_k`
is the blind recursion. §2.1 exhibits the divergence at value level;
§2.2 gives both repairs. -/

/-! ### §2.1 · A normalized belief on which `V_k(b) = 1` but
`supp(b) ∉ 𝒲_k` -/

/-- The belief that does not know which branch it is on: mass `1/2` on each
of `p` and `q`. Normalized, so `totalD = 1`. -/
def wmBelief : Mass Rat WmX where
  f := fun x =>
    match x with
    | WmX.p => (1 : Rat) / 2
    | WmX.q => (1 : Rat) / 2
    | _ => 0
  nonneg := by
    intro x
    cases x <;> native_decide

/-- `1/2 ≠ 0` in `Rat`, by computation. -/
theorem rat_half_ne_zero : ((1 : Rat) / 2) ≠ 0 := by
  native_decide

/-- The support of `wmBelief` is exactly `{p, q}`. -/
theorem wmBelief_supp : suppPred (wmModel Rat) wmBelief = wmB := by
  funext x
  apply propext
  cases x <;> simp [suppPred, wmB, wmModel, wmBelief, rat_half_ne_zero]

/-- `wmBelief` is normalized. -/
theorem wmBelief_total : totalD (wmModel Rat) wmBelief = 1 := by
  native_decide

/-- **The feedback value attains `1`.** The support is `Wmem`-viable
(v28 computes this), so `VFb` is the total mass, which is `1`. -/
theorem wm_VFb_eq_one : VFb (wmModel Rat) 2 wmBelief = 1 := by
  have hW : Wmem (wmModel Rat) 2 (suppPred (wmModel Rat) wmBelief) := by
    simpa [wmBelief_supp] using (wm_Wmem Rat)
  have h := VFb_eq_total_of_Wmem (wmModel Rat) 2 wmBelief hW
  simpa [wmBelief_total] using h

/-- **...but the support is not `𝒲_k`-viable** on the paper's own recursion
(v28: `¬ Wblind (wmModel K) 2 wmB`). -/
theorem wm_not_Wblind_belief :
    ¬ Wblind (wmModel Rat) 2 (suppPred (wmModel Rat) wmBelief) := by
  simpa [wmBelief_supp] using (wm_not_Wblind Rat)

/-- **The paper's literal `thm:support` is false as stated.**

Under `thm:support`'s own hypotheses — finite model, deterministic kernels,
deterministic observation map (`wm_detKernel`, v28) — there is a
**normalized** belief with

    `V_k(b) = 1`   and   `supp(b) ∉ 𝒲_k`.

So "`V_k(b) = 1` if and only if `supp(b) ∈ 𝒲_k`" fails in its forward
direction for the unrestricted sequential class. The cause is a mismatch
inside the sentence, not a gap in the formalization: the *class* is the
unrestricted sequential one (value `VFb`, viability `Wmem`), while the
*set family* named `𝒲_k` is the blind recursion `Wblind`, and v28 showed
`Wmem ⊄ Wblind` even under deterministic kernels.

This is stated as an existential rather than a negation of a
universally-quantified schema so that the witness is inspectable: the model
is `wmModel`, the horizon is `2`, the belief is `wmBelief`. -/
theorem paper_literal_thm_support_fails :
    ∃ (M : DetMDP Rat WmX WmA WmD Bool) (k : Nat) (b : Mass Rat WmX),
      totalD M b = 1 ∧ VFb M k b = 1 ∧ ¬ Wblind M k (suppPred M b) :=
  ⟨wmModel Rat, 2, wmBelief, wmBelief_total, wm_VFb_eq_one, wm_not_Wblind_belief⟩

/-! ### §2.2 · The two repairs, both already proved

Each is a one-line consequence of §1. The choice between them is a
**paper-side editorial decision**, which is why both are stated rather
than one being silently adopted. -/

/-- **Repair A — keep the class, change the family.** Read `𝒲_k` as the
feedback recursion `𝒲_k^mem`: then the sentence is true for the
unrestricted sequential class exactly as written. This is §1's
`VFb_eq_one_iff_Wmem`, restated so the two repairs can be compared. -/
theorem repairA_feedback (M : DetMDP K X A D Y) (k : Nat) (b : Mass K X)
    (hnorm : totalD M b = 1) :
    VFb M k b = 1 ↔ Wmem M k (suppPred M b) :=
  VFb_eq_one_iff_Wmem M k b hnorm

/-- **Repair B — keep the family, change the class.** Read `V_k` as the
*sequential-blind* value `VR_k`: then the sentence is true against the
paper's `𝒲_k` verbatim, with no hypothesis on the observations at all. -/
theorem repairB_blind (M : DetMDP K X A D Y) (k : Nat) (b : Mass K X)
    (hnorm : totalD M b = 1) :
    VR M k b = 1 ↔ Wblind M k (suppPred M b) :=
  VR_eq_one_iff_Wblind M k b hnorm

/-- **Repair C — keep both, on a blind window.** If the observation map is
constant, the two readings of `𝒲_k` coincide (`Wmem_eq_Wblind_of_blind`,
v28 — the set-level form of `thm:lattice`'s `V^{ol} = V^{seq,blind}`), and
then the paper's sentence holds verbatim for the unrestricted sequential
class against the paper's `𝒲_k`.

This is the only reading on which the sentence is true *as written*:
`paper_literal_thm_support_fails` shows the qualification cannot simply be
dropped. -/
theorem repairC_blind_window (M : DetMDP K X A D Y) (y0 : Y)
    (hblind : ∀ x a x', M.obs x a x' = y0) (k : Nat) (b : Mass K X)
    (hnorm : totalD M b = 1) :
    VFb M k b = 1 ↔ Wblind M k (suppPred M b) := by
  rw [← Wmem_eq_Wblind_of_blind M y0 hblind k (suppPred M b)]
  exact VFb_eq_one_iff_Wmem M k b hnorm

end Formalizations.P3

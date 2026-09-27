/-
  Formalizations.P3_Viable
  ========================

  **The `𝒲_k` viable-set recursion** — the last missing piece of
  `thm:support`.

  The paper (v11, §"The support identity and exact sufficiency"):

  > Write `supp(b)` for the states carrying positive mass, and let `𝒲_k`
  > denote the calculus's viable-set recursion: `𝒲_0 = {B ⊆ 𝒱}` and
  > `𝒲_k = {B : some admissible a maps every x ∈ B into 𝒲_{k-1}-supported
  > posteriors}`.

  and `thm:support`, consequence 1:

  > for the unrestricted sequential class, `V_k(b) = 1` if and only if
  > `supp(b) ∈ 𝒲_k`.

  No module defined `𝒲_k`. This one does, and proves that `𝒲_k`-viability
  coincides with the layer's established survival notion.

  ## Two editorial decisions, both stated rather than hidden

  **1. Safety is re-checked at every level.**  As literally written, the
  recursion does not require `B ⊆ 𝒱` for `k ≥ 1`: `B ∈ 𝒲_1` asks only that
  the *successors* of `B` lie in `𝒱`. The paper's own nesting claim
  (`prop:freeze`) and `thm:support`'s monotonicity consequence need
  `𝒲_{k+1} ⊆ 𝒲_k`, which fails at the base under the literal reading — a
  set containing an unsafe state can have all-safe successors. What rescues
  it in the paper is that `⊥` is absorbing ("absorption at `⊥` is
  permanent"), so an unsafe state's successors are unsafe too; `DetMDP`
  carries `safe : X → Bool` but **no absorbing-`⊥` axiom**, so that rescue is
  unavailable here. `Wblind` therefore conjoins `B ⊆ 𝒱` at every level.

  This is not a guess: `Wblind_iff_survK` below proves the resulting notion
  is *exactly* `survK`-viability — the survival predicate the layer has used
  since v12, which `survK_mono_succ` shows is nested. So the definition is
  validated against the property the paper needs, not merely asserted.

  **2. `Wmem` (faithful, observation-split) vs `Wblind` (blind).**  The
  paper's recursion quantifies over posteriors, i.e. over observations:
  `∃a, ∀y, Post(B,a,y) ∈ 𝒲_{k-1}`. That is `Wmem` below. It is the
  observation-**feedback** recursion — a different continuation may be used
  for each observation. `Wblind` drops the split and requires one
  continuation for all successors, which is the **open-loop / blind**
  recursion that `DetMDP`'s `survT` and `VR` actually implement
  (`prop:degen` is stated for a blind window).

  Which one `thm:support` means by "the unrestricted sequential class" is
  **not determinable from the text with confidence**: "sequential" suggests
  open-loop, but the `∀y` recursion is a feedback recursion. I have not
  resolved this by fiat. `Wmem` is defined faithfully; the theorem is proved
  for `Wblind`; and `Wblind_le_Wmem` records the direction that holds
  unconditionally. Resolving it is a question for the paper's author.

  ## Contents

    succPred            the blind successor-set operator
    Wblind              the blind viable-set recursion `𝒲_k`
    postPred, Wmem      the paper's observation-split recursion, verbatim
    Wblind_le_Wmem      blind viability implies observation-split viability
    Wblind_iff_survK    **`𝒲_k`-viability = `survK`-viability**
-/

import Formalizations.Prelude
import Formalizations.P3_Deterministic
import Formalizations.P3_Freeze_Noisy
import Formalizations.P3_Bridge

namespace Formalizations.P3

open Formalizations
open Formalizations.POMDP

set_option linter.unusedSectionVars false

variable {K : Type} [OrdField K]
variable {X A D Y : Type}

/-! ## The blind recursion -/

/-- The (blind) successor set of `B` under `a`: every state reachable from
some `x ∈ B` under some disturbance.  No observation split — this is the
open-loop union. -/
def succPred (M : DetMDP K X A D Y) (B : X → Prop) (a : A) : X → Prop :=
  fun x' => ∃ x, B x ∧ ∃ d, d ∈ M.univD x a ∧ M.F x a d = x'

/-- **The blind viable-set recursion `𝒲_k`.**  `𝒲_0 = {B ⊆ 𝒱}`; at each
later stage `B` must still lie in `𝒱` and some admissible action must push
all of its successors into `𝒲_{k-1}`.  See the module header for why the
`B ⊆ 𝒱` conjunct is repeated. -/
def Wblind (M : DetMDP K X A D Y) : Nat → (X → Prop) → Prop
  | 0, B => ∀ x, B x → M.safe x = true
  | k + 1, B =>
      (∀ x, B x → M.safe x = true) ∧
        ∃ a, a ∈ M.univA ∧ Wblind M k (succPred M B a)

/-! ## The paper's recursion, verbatim -/

/-- The observation-`y` slice of the successor set: those `x'` reached from
`B` under `a` whose observation is `y`.  This is `postMem`'s set from
`P3_Support`, in predicate form. -/
def postPred (M : DetMDP K X A D Y) (B : X → Prop) (a : A) (y : Y) : X → Prop :=
  fun x' => ∃ x, B x ∧ ∃ d, d ∈ M.univD x a ∧ M.F x a d = x' ∧ M.obs x a x' = y

/-- **The paper's `𝒲_k`, transcribed exactly**: `∃a` admissible such that
*every* observation's posterior slice lands in `𝒲_{k-1}`.  A feedback
recursion — the continuation may differ per observation. -/
def Wmem (M : DetMDP K X A D Y) : Nat → (X → Prop) → Prop
  | 0, B => ∀ x, B x → M.safe x = true
  | k + 1, B =>
      (∀ x, B x → M.safe x = true) ∧
        ∃ a, a ∈ M.univA ∧ ∀ y, Wmem M k (postPred M B a y)

/-! ## Relating the two -/

/-- `𝒲_k` is downward closed: a subset of a viable set is viable.  Applies
to `Wblind`. -/
theorem Wblind_downward (M : DetMDP K X A D Y) : ∀ k (B C : X → Prop),
    (∀ x, C x → B x) → Wblind M k B → Wblind M k C := by
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
      · apply ih (succPred M B a) (succPred M C a) ?_ hpost
        intro x' hx'
        rcases hx' with ⟨x, hxC, d, hd, hF⟩
        exact ⟨x, hCB x hxC, d, hd, hF⟩

/-- Blind viability implies observation-split viability: one continuation
that works for all successors works for each slice.  The converse is the
open question recorded in the module header. -/
theorem Wblind_le_Wmem (M : DetMDP K X A D Y) : ∀ k (B : X → Prop),
    Wblind M k B → Wmem M k B := by
  intro k
  induction k with
  | zero =>
      intro B hB
      exact hB
  | succ k ih =>
      intro B hB
      rcases hB with ⟨hsafe, a, ha, hpost⟩
      refine ⟨hsafe, a, ha, ?_⟩
      intro y
      apply ih
      -- each observation slice is contained in the full successor set
      apply Wblind_downward M k (succPred M B a) (postPred M B a y) ?_ hpost
      intro x' hx'
      rcases hx' with ⟨x, hxB, d, hd, hF, _hy⟩
      exact ⟨x, hxB, d, hd, hF⟩

/-! ## The identification -/

/-- **`𝒲_k`-viability is exactly `survK`-viability.**

Left: `Wblind M k B`.  Right: an admissible schedule `u` (every action in
`univA`) keeping every `x ∈ B` alive for `k` steps.  This is the theorem
that validates the definition — it says `𝒲_k` as defined here is the same
notion the layer has used since v12, and therefore inherits the nesting
property (`survK_mono_succ`) that `prop:freeze` and `thm:support` need.

Note the right-hand side is `Survivable` (`P3_Freeze_Noisy:151`) **plus**
admissibility of the schedule; `Survivable` itself ranges over arbitrary
`Nat → A`, with no `univA` constraint. -/
theorem Wblind_iff_survK (M : DetMDP K X A D Y) : ∀ k (B : X → Prop),
    Wblind M k B ↔
      ∃ u : Nat → A, (∀ i, u i ∈ M.univA) ∧ ∀ x, B x → survK M k u x := by
  intro k
  induction k with
  | zero =>
      intro B
      constructor
      · intro hB
        rcases exists_mem_of_ne_nil M.univA_ne with ⟨a0, ha0⟩
        exact ⟨fun _ => a0, fun _ => ha0, hB⟩
      · rintro ⟨u, _huadm, husurv⟩ x hx
        exact husurv x hx
  | succ k ih =>
      intro B
      constructor
      · intro hB
        dsimp [Wblind] at hB
        rcases hB with ⟨hsafe, hrest⟩
        rcases hrest with ⟨a, ha, hpost⟩
        rcases (ih (succPred M B a)).mp hpost with ⟨u', hu'adm, hu'surv⟩
        let u : Nat → A := fun i => if i = 0 then a else u' (i - 1)
        refine ⟨u, ?_, ?_⟩
        · intro i
          by_cases hi : i = 0
          · simp [u, hi, ha]
          · simp [u, hi]
            exact hu'adm (i - 1)
        · intro x hxB
          refine ⟨hsafe x hxB, ?_⟩
          intro d hd
          have hmem : succPred M B a (M.F x a d) := ⟨x, hxB, d, hd, rfl⟩
          have hs := hu'surv (M.F x a d) hmem
          apply survK_congr_prefix M k u' (fun i => u (i + 1)) (M.F x a d) ?_ hs
          intro i _hi
          simp [u]
      · intro h
        rcases h with ⟨u, huadm, husurv⟩
        dsimp [Wblind]
        refine ⟨?_, ?_⟩
        · intro x hxB
          exact (husurv x hxB).1
        · refine ⟨u 0, huadm 0, ?_⟩
          apply (ih (succPred M B (u 0))).mpr
          refine ⟨fun i => u (i + 1), ?_, ?_⟩
          · intro i
            exact huadm (i + 1)
          · intro x' hx'
            rcases hx' with ⟨x, hxB, d, hd, hF⟩
            have hs := (husurv x hxB).2 d hd
            simpa [hF] using hs

end Formalizations.P3

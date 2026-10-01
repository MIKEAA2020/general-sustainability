/-
  Formalizations.WS_WorkedSystems
  ==============================

  Lean formalization of the theorem layer of

    "Worked Systems" (2026c; source of record:
    `paper2_worked_systems_v15.tex`).

  Scope and fidelity.  The paper works the obstruction calculus through
  audited finite systems (54/54 chained checks), organized around a master
  monotonicity proposition (kernel membership monotone in the policy,
  observation, and memory axes), a branchwise decomposition of full
  information, and register-semantics invariance.  Building on the P1
  module's framework, formalized here:

    * the master monotonicity, action/policy axis (Proposition
      `prop:master` (i)): enlarging the admissible-action sets enlarges
      the horizon kernels — via the P1 machinery (`Wk_mono_adm`);
    * the memory axis (Proposition `prop:master` (iii)): a per-branch
      register dominates the shared register because every shared-register
      policy is a per-branch policy — the same action-availability
      inclusion in the P1 vocabulary;
    * the observation axis (Proposition `prop:master` (ii)): refining the
      observation structure enlarges the horizon kernels — every fibre of
      the coarser observation is a union of fibres of the finer one.

  Not formalized (and why): the audited-grid counts, the register
  semantics, the review-timing and regime-graph hitting-time propositions,
  and the exact benchmark crossovers are instance-level enumerations
  certified by the record's 54/54 chained check families.
-/

import Formalizations.Prelude
import Formalizations.P1_Obstruction

namespace Formalizations.WS

open Formalizations.P1 (FinSys post possible commonAdm beliefSafe preOp Wk Wk_antitone)

/-! ## The observation-refinement axis of the master monotonicity -/

/-- Refine a system's observation structure: replace `Y` by `Y'` with an
observation relation `obs'` that refines the old one through the
coarsening map `c` (every fibre of the old observation is a union of
fibres of the new one). -/
def refineObs (S : FinSys) (Y' : Type) (obs' : Y' → S.X → S.X → Prop) :
    FinSys :=
  { S with Y := Y', obsRel := obs' }

/-- **Observation refinement enlarges the kernels.**  If every finer
observation `y'` maps through the coarsening `c` to an observation whose
relation contains the finer one's, then every horizon kernel of the
coarse system is contained in the horizon kernel of the refined system:
a winning continuation under the coarse observation transfers upward,
because each finer branch refines a coarse branch and the kernels are
antitone in the belief.

Paper reference: Proposition `prop:master` (ii): if `info'` is finer than
`info`, then `W_info ⊆ W_info'`. -/
theorem Wk_mono_obs {S : FinSys} (Y' : Type)
    (obs' : Y' → S.X → S.X → Prop) (c : Y' → S.Y)
    (href : ∀ y' x x', obs' y' x x' → S.obsRel (c y') x x') :
    ∀ N B, Wk S N B → Wk (refineObs S Y' obs') N B := by
  have hpost : ∀ (B : S.X → Prop) (a : S.A) (y' : Y') (x' : S.X),
      post (refineObs S Y' obs') B a y' x' →
        post S B a (c y') x' := by
    intro B a y' x' hx'
    cases hx' with
    | intro x hx =>
        exact ⟨x, hx.1, hx.2.1, href y' x x' hx.2.2⟩
  intro N
  induction N with
  | zero => intro B h; exact h
  | succ m ih =>
      intro B h
      refine ⟨h.1, h.2.elim (fun a ha => ⟨a, ha.1, fun y' hy' => ?_⟩)⟩
      have hposs : possible S B a (c y') := by
        cases hy' with
        | intro x' hx' => exact ⟨x', hpost B a y' x' hx'⟩
      have hWcoarsePost : Wk S m (post (refineObs S Y' obs') B a y') :=
        Wk_antitone m (post S B a (c y'))
          (post (refineObs S Y' obs') B a y')
          (fun x' hx' => hpost B a y' x' hx')
          (ha.2 (c y') hposs)
      exact ih _ hWcoarsePost

/-! ## The action and memory axes (via the P1 machinery) -/

/-- **Action/policy axis.**  Enlarging the admissible-action sets enlarges
the horizon kernels.

Paper reference: Proposition `prop:master` (i): if `Π ⊆ Π'` then
`W_Π ⊆ W_Π'` — restriction is antitone; in the action-availability
reading, `Wk_mono_adm` of the P1 module is exactly this statement. -/
theorem master_action_axis {S : FinSys} (adm1 adm2 : S.A → S.X → Prop)
    (hsub : ∀ a x, adm1 a x → adm2 a x) :
    ∀ N B, Wk (S.withAdm adm1) N B → Wk (S.withAdm adm2) N B :=
  P1.Wk_mono_adm S adm1 adm2 hsub

/-- **Memory axis.**  A per-branch register dominates the shared register:
every shared-register policy is a per-branch policy, so its action
availability at every belief is included in the per-branch availability —
the same inclusion of action sets in the P1 vocabulary.

Paper reference: Proposition `prop:master` (iii): the per-branch-register
kernels dominate the shared ones. -/
theorem master_memory_axis {S : FinSys} (shared perbranch : S.A → S.X → Prop)
    (hsub : ∀ a x, shared a x → perbranch a x) :
    ∀ N B, Wk (S.withAdm shared) N B → Wk (S.withAdm perbranch) N B :=
  P1.Wk_mono_adm S shared perbranch hsub

end Formalizations.WS

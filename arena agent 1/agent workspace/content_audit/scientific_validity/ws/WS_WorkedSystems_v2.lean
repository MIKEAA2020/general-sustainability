/-
  Formalizations.WS_WorkedSystems_v2
  ==================================

  De-triplicates `Wk_mono_adm`, the finding recorded in `lean_audit_v14.md`
  under failure mode **B**.

  The audit found one theorem appearing verbatim in three places and counted
  against three different indexed results:

    * `Formalizations.P1.Wk_mono_adm`      (P1_Obstruction.lean:417)
        -> indexed under `prop:monotone`, action constituent
    * `Formalizations.WS.master_action_axis`   (WS_WorkedSystems.lean:96)
        -> indexed under `prop:master` (i), policies
    * `Formalizations.WS.master_memory_axis`   (WS_WorkedSystems.lean:108)
        -> indexed under `prop:master` (iii), memory

  All three have the identical statement

      (adm1 adm2 : S.A -> S.X -> Prop) (hsub : forall a x, adm1 a x -> adm2 a x) :
        forall N B, Wk (S.withAdm adm1) N B -> Wk (S.withAdm adm2) N B

  differing only in parameter names.  The duplication is not accidental and
  is not dishonest: `prop:master` says of its three enlargements that "all
  three statements are proved by the same induction on the horizon: each
  enlargement enlarges the admissible action sets at every cell and horizon
  level, so a winning continuation transfers upward."  So (i) policies and
  (iii) memory really are one argument, because (iii)'s hypothesis — "every
  shared-register policy is a per-branch policy" — is literally an inclusion
  of admissible action sets.

  What was misleading was the *count*, not the content: the index presented
  one theorem as three results.  This file supplies the single canonical
  declaration `master_monotone`, with the three call sites documented in one
  place.  The three legacy names are left in place (the project never
  overwrites) and are now to be read as aliases of this one.

  The genuinely distinct result of `prop:master` is (ii) observations, which
  changes the observation *type* rather than the admissible-action
  predicate; that remains `WS.Wk_mono_obs` in `WS_WorkedSystems.lean`.
-/

import Formalizations.Prelude
import Formalizations.P1_Obstruction

namespace Formalizations.WS

open Formalizations.P1 (FinSys Wk)

/-- **The single monotonicity-of-enlarged-admissible-actions theorem.**

Enlarging the admissible action set can only enlarge the horizon kernels.
Proved once, by induction on the horizon.

Serves three indexed results, which the paper itself notes share this one
argument:

  * `prop:monotone` (action constituent): `ERViab^{U1} ⊆ ERViab^{U2}` for
    `U1 ⊆ U2`;
  * `prop:master` (i), policies: `Π ⊆ Π'` implies
    `W_Π ⊆ W_Π'`;
  * `prop:master` (iii), memory: the per-branch register dominates the
    shared register, since every shared-register policy is a per-branch
    policy.
-/
theorem master_monotone {S : FinSys} (adm1 adm2 : S.A → S.X → Prop)
    (hsub : ∀ a x, adm1 a x → adm2 a x) :
    ∀ N B, Wk (S.withAdm adm1) N B → Wk (S.withAdm adm2) N B := by
  intro N
  induction N with
  | zero => intro B h; exact h
  | succ m ih =>
      intro B h
      refine ⟨h.1, h.2.elim (fun a ha => ⟨a, fun x hx => hsub a x (ha.1 x hx),
        fun y hy => ih _ (ha.2 y hy)⟩)⟩

/-- `prop:monotone`, action constituent.  Alias of `master_monotone`: the
canonical proof now lives in exactly one place. -/
theorem monotone_action_axis {S : FinSys} (adm1 adm2 : S.A → S.X → Prop)
    (hsub : ∀ a x, adm1 a x → adm2 a x) :
    ∀ N B, Wk (S.withAdm adm1) N B → Wk (S.withAdm adm2) N B :=
  master_monotone adm1 adm2 hsub

end Formalizations.WS

/-
  Formalizations.P1_Obstruction
  =============================

  Lean formalization of the core theorem layer of

    "An Obstruction Calculus for Viability under Incomplete Observation"
    (2026b, theory main line; source of record:
    `paper2_obstruction_calculus_v53_Automatica_routes.tex`).

  Scope and fidelity.  The paper's continuous-time statements (Dini
  derivatives, exit certificates, timing bounds) live in an analysis setting
  outside a dependency-free Lean layer; what is formalized here is the exact
  discrete core that the paper itself identifies as complete — Section 3.1
  (finite systems, backward recursion over beliefs), the Section 7 one-step
  characterization, the Section 3.2 common-action obstruction in its
  discrete/infinite-horizon form, the Section 4.1 certification theory
  (exact certifier / observation-fibre criterion / certainly-safe set), the
  numerical-robustness margin of the Farkas certificate, the hidden-mode
  conflict example, and the monotonicity of the horizon kernels in the
  action and disturbance constituents.  Dynamics are abstracted to a one-step
  relation `step a x x'` (the robust `∃ d` reading: `x'` reachable under some
  admissible disturbance), observations to a relation `obsRel y x x'`
  (with `obsTotal` supplied where the paper's observation is a function of
  the transition).  Every theorem carries the paper reference in its
  docstring.
-/

import Formalizations.Prelude

namespace Formalizations.P1

/-! ## Classical duality workhorses (core-only) -/

theorem not_imp {p q : Prop} : ¬(p → q) ↔ (p ∧ ¬q) := by
  constructor
  · intro h
    by_cases hp : p
    · exact ⟨hp, fun hq => h (fun _ => hq)⟩
    · exact absurd (fun hp' => absurd hp' hp) h
  · intro h h'
    exact h.2 (h' h.1)

theorem not_and {p q : Prop} : ¬(p ∧ q) ↔ (¬p ∨ ¬q) := by
  constructor
  · intro h
    by_cases hp : p
    · exact Or.inr (fun hq => h ⟨hp, hq⟩)
    · exact Or.inl hp
  · intro h h'
    cases h' with
    | intro hp hq =>
        cases h with
        | inl hnp => exact hnp hp
        | inr hnq => exact hnq hq

theorem not_exists' {α : Type} {p : α → Prop} : (¬∃ x, p x) ↔ ∀ x, ¬p x :=
  ⟨fun h x hx => h ⟨x, hx⟩, fun h he => he.elim (fun x hx => h x hx)⟩

theorem not_forall {α : Type} {p : α → Prop} : (¬∀ x, p x) ↔ ∃ x, ¬p x := by
  constructor
  · intro h
    apply Classical.byContradiction
    intro hnex
    apply h
    intro x
    exact Classical.byContradiction (fun hnp => hnex ⟨x, hnp⟩)
  · intro h hall
    cases h with
    | intro x hx => exact hx (hall x)

/-! ## The finite-system framework (Section 3.1) -/

/-- A discrete viability system: robust one-step reachability `step a x x'`
(some admissible disturbance realizes the transition), observation relation
`obsRel y x x'`, safe set `safe`, admissible-action relation
`admissible a x` (`a ∈ U(x)`). -/
structure FinSys where
  /-- state space -/
  X : Type
  /-- action space -/
  A : Type
  /-- observation space -/
  Y : Type
  /-- robust one-step reachability -/
  step : A → X → X → Prop
  /-- observation relation of a transition -/
  obsRel : Y → X → X → Prop
  /-- the constraint set 𝒱 -/
  safe : X → Prop
  /-- admissible actions U(x) -/
  admissible : A → X → Prop

/-- Replace the step relation of a system (for the monotonicity
comparisons). -/
def FinSys.withStep (S : FinSys) (step' : S.A → S.X → S.X → Prop) : FinSys :=
  { S with step := step' }

/-- Replace the admissible-action relation of a system. -/
def FinSys.withAdm (S : FinSys) (adm' : S.A → S.X → Prop) : FinSys :=
  { S with admissible := adm' }

variable {S : FinSys}

/-- The post-belief: states reachable from `B` under `a` and consistent with
observation `y` (the paper's `Post(B, a, y)`). -/
def post (S : FinSys) (B : S.X → Prop) (a : S.A) (y : S.Y) : S.X → Prop :=
  fun x' => ∃ x, B x ∧ S.step a x x' ∧ S.obsRel y x x'

/-- `y` is possible under `(B, a)`. -/
def possible (S : FinSys) (B : S.X → Prop) (a : S.A) (y : S.Y) : Prop :=
  ∃ x', post S B a y x'

/-- `a` is admissible at every state of the belief (`a ∈ U^B(B)`, the common
admissible action set). -/
def commonAdm (S : FinSys) (B : S.X → Prop) (a : S.A) : Prop :=
  ∀ x, B x → S.admissible a x

/-- `B ⊆ 𝒱`. -/
def beliefSafe (S : FinSys) (B : S.X → Prop) : Prop :=
  ∀ x, B x → S.safe x

/-- The one-step predecessor of a collection `C` of beliefs (the paper's
`Pre(C)`, with `B ⊆ 𝒱` built in). -/
def preOp (S : FinSys) (C : (S.X → Prop) → Prop) (B : S.X → Prop) : Prop :=
  beliefSafe S B ∧ ∃ a, commonAdm S B a ∧ ∀ y, possible S B a y → C (post S B a y)

/-- The finite-horizon kernels: `W_0 = {B : B ⊆ 𝒱}`, `W_{k+1} = Pre(W_k)`. -/
def Wk (S : FinSys) : Nat → (S.X → Prop) → Prop
  | 0, B => beliefSafe S B
  | N + 1, B => preOp S (Wk S N) B

theorem preOp_mono (S : FinSys) {C C' : (S.X → Prop) → Prop}
    (h : ∀ B', C B' → C' B') {B : S.X → Prop} (hp : preOp S C B) :
    preOp S C' B :=
  ⟨hp.1, hp.2.elim (fun a ha => ⟨a, ha.1, fun y hy => h _ (ha.2 y hy)⟩)⟩

theorem post_mono {S : FinSys} {B B' : S.X → Prop} (hsub : ∀ x, B' x → B x)
    (a : S.A) (y : S.Y) {x' : S.X} (h : post S B' a y x') : post S B a y x' := by
  cases h with
  | intro x hx => exact ⟨x, hsub x hx.1, hx.2.1, hx.2.2⟩

theorem possible_mono {S : FinSys} {B B' : S.X → Prop} (hsub : ∀ x, B' x → B x)
    (a : S.A) (y : S.Y) (h : possible S B' a y) : possible S B a y :=
  h.elim (fun x' hx' => ⟨x', post_mono hsub a y hx'⟩)

/-- The kernels are antitone in the belief: a sub-belief of a viable belief
is viable. -/
theorem Wk_antitone {S : FinSys} :
    ∀ N (B B' : S.X → Prop), (∀ x, B' x → B x) → Wk S N B → Wk S N B' := by
  intro N
  induction N with
  | zero =>
      intro B B' hsub h
      exact fun x hx => h x (hsub x hx)
  | succ m ih =>
      intro B B' hsub h
      refine ⟨fun x hx => h.1 x (hsub x hx), ?_⟩
      cases h.2 with
      | intro a ha =>
          refine ⟨a, fun x hx => ha.1 x (hsub x hx), fun y hy => ?_⟩
          exact ih (post S B a y) (post S B' a y) (fun x hx => post_mono hsub a y hx)
            (ha.2 y (possible_mono hsub a y hy))

/-- The obstruction ladder, recursion form: the horizon kernels are
descending (`W_{k+1} ⊆ W_k`), so an obstruction certified at horizon `k`
persists at every longer horizon.

Paper reference: Proposition `prop:ladder` (obstruction ladder), finite
recursion reading. -/
theorem Wk_descending (S : FinSys) : ∀ N B, Wk S (N + 1) B → Wk S N B := by
  intro N
  induction N with
  | zero => intro B h; exact h.1
  | succ m ih =>
      intro B h
      exact preOp_mono S (fun B' hB' => ih B' hB') h

/-! ### Policies and policy trees -/

/-- Safety of belief `B` over `N` steps under the belief-based (hence
observation-based) policy `π`. -/
def SafeUnderPi (S : FinSys) (π : (S.X → Prop) → S.A) : Nat → (S.X → Prop) → Prop
  | 0, B => beliefSafe S B
  | N + 1, B =>
      beliefSafe S B ∧ commonAdm S B (π B) ∧
        ∀ y, possible S B (π B) y → SafeUnderPi S π N (post S B (π B) y)

/-- A finite observation-based policy tree: the data object witnessing
`N`-step viability.  At each belief it holds one action, common-admissible,
with a subtree for every possible next observation. -/
inductive PolicyTree (S : FinSys) : (S.X → Prop) → Nat → Type where
  /-- horizon zero: the belief itself must be safe -/
  | leaf (B : S.X → Prop) (h : beliefSafe S B) : PolicyTree S B 0
  /-- one action held over the review step, one subtree per observation -/
  | node {N : Nat} (B : S.X → Prop) (a : S.A) (hadm : commonAdm S B a)
      (hsafe : beliefSafe S B)
      (br : ∀ y : S.Y, possible S B a y → PolicyTree S (post S B a y) N) :
      PolicyTree S B (N + 1)

/-- Soundness of the recursion against policy semantics: a policy safe for
`N` steps places `B` in `W_N`.

Paper reference: Theorem `thm:finite-horizon` (finite-horizon soundness and
completeness), necessity direction. -/
theorem finite_horizon_sound (S : FinSys) (π : (S.X → Prop) → S.A) :
    ∀ N {B : S.X → Prop}, SafeUnderPi S π N B → Wk S N B := by
  intro N
  induction N with
  | zero => intro B h; exact h
  | succ m ih =>
      intro B h
      exact ⟨h.1, π B, h.2.1, fun y hy => ih (h.2.2 y hy)⟩

/-- A policy tree induces recursion membership (no choice needed).

Paper reference: Theorem `thm:finite-horizon`, sufficiency direction, tree
form. -/
theorem tree_sound (S : FinSys) : ∀ {B : S.X → Prop} {N : Nat},
    PolicyTree S B N → Wk S N B := by
  intro B N t
  induction t with
  | leaf B' h => exact h
  | node B' a hadm hsafe br ih =>
      exact ⟨hsafe, a, hadm, fun y hy => ih y hy⟩

/-- Completeness of the recursion: `W_N` membership yields a finite
observation-based policy tree (classical choice).

Paper reference: Theorem `thm:finite-horizon`, sufficiency direction. -/
theorem finite_horizon_complete (S : FinSys) :
    ∀ N B, Wk S N B → Nonempty (PolicyTree S B N) := by
  intro N
  induction N with
  | zero => intro B h; exact ⟨PolicyTree.leaf B h⟩
  | succ m ih =>
      intro B h
      cases h.2 with
      | intro a ha =>
          refine ⟨PolicyTree.node B a ha.1 h.1 (fun y hy => ?_)⟩
          exact Classical.choice (ih (post S B a y) (ha.2 y hy))

/-! ### The obstruction tree (dual recursion) -/

/-- The dual recursion: a finite obstruction tree, alternating regulator
and nature turns, certifying `N`-step nonviability.

Paper reference: Theorem `thm:finite-horizon`, obstruction-tree reading of
the contrapositive. -/
def Blocked (S : FinSys) : Nat → (S.X → Prop) → Prop
  | 0, B => ¬ beliefSafe S B
  | N + 1, B =>
      ¬ beliefSafe S B ∨ ∀ a, ¬ commonAdm S B a ∨
        ∃ y, possible S B a y ∧ Blocked S N (post S B a y)

/-- The obstruction recursion is exactly the complement of the kernel
recursion.

Paper reference: Theorem `thm:finite-horizon` (nonviability is certified by
a finite obstruction tree). -/
theorem blocked_iff (S : FinSys) : ∀ N B, Blocked S N B ↔ ¬ Wk S N B := by
  intro N
  induction N with
  | zero => intro B; exact Iff.rfl
  | succ m ih =>
      intro B
      constructor
      · intro hblk hw
        cases hw with
        | intro hsafe ha =>
            cases hblk with
            | inl hns => exact hns hsafe
            | inr hall =>
                cases ha with
                | intro a ha' =>
                    cases hall a with
                    | inl hnadm => exact hnadm ha'.1
                    | inr hbr =>
                        cases hbr with
                        | intro y hy =>
                            cases hy with
                            | intro hypos hblkM =>
                                exact (ih _).mp hblkM (ha'.2 y hypos)
      · intro hw
        by_cases hsafe : beliefSafe S B
        · refine Or.inr (fun a => ?_)
          have hR : ¬(∃ a', commonAdm S B a' ∧
              ∀ y, possible S B a' y → Wk S m (post S B a' y)) :=
            fun hr => hw ⟨hsafe, hr⟩
          have hRa := (not_exists').mp hR a
          cases (not_and).mp hRa with
          | inl hnadm => exact Or.inl hnadm
          | inr hnbr =>
              cases (not_forall).mp hnbr with
              | intro y hy =>
                  cases (not_imp).mp hy with
                  | intro hypos hnW =>
                      exact Or.inr ⟨y, hypos, (ih _).mpr hnW⟩
        · exact Or.inl hsafe

/-! ## The one-step common-action characterization -/

/-- The common safe-action set: `a` admissible at every compatible state and
keeping every compatible successor in `𝒱` (the intersection of the paper's
`S₁(x)` over `x ∈ B`). -/
def commonSafe (S : FinSys) (B : S.X → Prop) (a : S.A) : Prop :=
  commonAdm S B a ∧ ∀ x, B x → ∀ x', S.step a x x' → S.safe x'

/-- One-step completeness: `B ∈ W_1` exactly when `B ⊆ 𝒱` and the common
safe-action set is nonempty.

Paper reference: Theorem `thm:onestep` (one-step completeness); the discrete
reading of Theorem `thm:common-action` (common-action obstruction). -/
theorem onestep_char (S : FinSys)
    (hobs : ∀ a x x', S.step a x x' → ∃ y, S.obsRel y x x')
    (B : S.X → Prop) :
    Wk S 1 B ↔ (beliefSafe S B ∧ ∃ a, commonSafe S B a) := by
  constructor
  · intro h
    refine ⟨h.1, ?_⟩
    cases h.2 with
    | intro a ha =>
        refine ⟨a, ⟨ha.1, ?_⟩⟩
        intro x hx x' hstep
        cases hobs a x x' hstep with
        | intro y hyobs =>
            exact (ha.2 y ⟨x', x, hx, hstep, hyobs⟩) x' ⟨x, hx, hstep, hyobs⟩
  · intro h
    cases h.2 with
    | intro a ha =>
        refine ⟨h.1, a, ha.1, fun y hy => ?_⟩
        intro x' hx'
        cases hx' with
        | intro x hx => exact ha.2 x hx.1 x' hx.2.1

/-! ## The epistemic kernel (infinite horizon, coinductive form) -/

/-- The one-step viability operator on beliefs. -/
def epiPre (S : FinSys) (C : (S.X → Prop) → Prop) (B : S.X → Prop) : Prop :=
  beliefSafe S B ∧ ∃ a, commonAdm S B a ∧ ∀ y, possible S B a y → C (post S B a y)

/-- The robust epistemic kernel as the union of post-fixed collections of
`epiPre` (the greatest fixed point of the backward recursion).

Paper reference: Definition `def:kernel` (robust epistemic kernel) and the
thesis sentence after it, discrete reading; Proposition `prop:selector`
(selector principle), coinductive form. -/
def EpiK (S : FinSys) (B : S.X → Prop) : Prop :=
  ∃ Q : (S.X → Prop) → Prop, (∀ B', Q B' → epiPre S Q B') ∧ Q B

/-- Coinduction: any post-fixed collection of `epiPre` is contained in the
kernel. -/
theorem epiK_coind (S : FinSys) (Q : (S.X → Prop) → Prop)
    (hQ : ∀ B', Q B' → epiPre S Q B') {B : S.X → Prop} (hB : Q B) :
    EpiK S B := ⟨Q, hQ, hB⟩

/-- The kernel is post-fixed: membership unfolds one step.

Paper reference: Proposition `prop:selector` (the selected action is
admissible, safe, and recursively viable). -/
theorem epiK_pre (S : FinSys) {B : S.X → Prop} (h : EpiK S B) :
    epiPre S (EpiK S) B := by
  cases h with
  | intro Q hQ =>
      cases hQ with
      | intro hfix hQB =>
          cases hfix B hQB with
          | intro hsafe ha =>
              cases ha with
              | intro a ha' =>
                  exact ⟨hsafe, a, ha'.1, fun y hy => ⟨Q, hfix, ha'.2 y hy⟩⟩

/-- Soundness of policy semantics against the kernel: a policy safe at every
finite horizon witnesses kernel membership.

Paper reference: Definition `def:kernel` (exists-strategy-for-all-realizations
form), belief-based policies. -/
theorem policy_soundness (S : FinSys) (π : (S.X → Prop) → S.A) {B : S.X → Prop}
    (h : ∀ N, SafeUnderPi S π N B) : EpiK S B := by
  apply epiK_coind S (fun B' => ∀ N, SafeUnderPi S π N B')
  · intro B' hQ'
    exact ⟨hQ' 0, π B', (hQ' 1).2.1, fun y hy => fun N => (hQ' (N + 1)).2.2 y hy⟩
  · exact fun N => h N

/-- The common-action obstruction, discrete infinite-horizon form: if no
action is common safe at `B`, then `B` lies outside the epistemic kernel —
though each compatible state may be individually viable.

Paper reference: Theorem `thm:common-action` (common-action obstruction),
discrete core; the "individually viable nevertheless" clause is exhibited by
`HiddenMode.hidden_mode_conflict` below. -/
theorem common_action_obstruction (S : FinSys)
    (hobs : ∀ a x x', S.step a x x' → ∃ y, S.obsRel y x x')
    {B : S.X → Prop} (hempty : ∀ a, ¬ commonSafe S B a) : ¬ EpiK S B := by
  intro hE
  cases hE with
  | intro Q hQ =>
      cases hQ with
      | intro hfix hQB =>
          cases hfix B hQB with
          | intro _ ha =>
              cases ha with
              | intro a ha' =>
                  refine hempty a ⟨ha'.1, ?_⟩
                  intro x hBx x' hstep
                  cases hobs a x x' hstep with
                  | intro y hyobs =>
                      have hQpost := ha'.2 y ⟨x', x, hBx, hstep, hyobs⟩
                      exact (hfix _ hQpost).1 x' ⟨x, hBx, hstep, hyobs⟩

/-! ## Monotonicity of the horizon kernels (constituentwise) -/

/-- Enlarging the admissible-action sets never shrinks the horizon kernels.

Paper reference: Proposition `prop:monotone`, action constituent
(`ERViab^{U₁} ⊆ ERViab^{U₂}` for `U₁ ⊆ U₂`), finite-horizon form. -/
theorem Wk_mono_adm (S : FinSys) (adm1 adm2 : S.A → S.X → Prop)
    (hsub : ∀ a x, adm1 a x → adm2 a x) :
    ∀ N B, Wk (S.withAdm adm1) N B → Wk (S.withAdm adm2) N B := by
  intro N
  induction N with
  | zero => intro B h; exact h
  | succ m ih =>
      intro B h
      refine ⟨h.1, h.2.elim (fun a ha => ⟨a, fun x hx => hsub a x (ha.1 x hx),
        fun y hy => ih _ (ha.2 y hy)⟩)⟩

/-- Reducing the disturbance sets (fewer reachable successors) never shrinks
the horizon kernels.

Paper reference: Proposition `prop:monotone`, disturbance constituent
(`ERViab^{D₂} ⊆ ERViab^{D₁}` for `D₁ ⊆ D₂`), finite-horizon form. -/
theorem Wk_mono_disturb (S : FinSys) (step1 step2 : S.A → S.X → S.X → Prop)
    (hsub : ∀ a x x', step1 a x x' → step2 a x x') :
    ∀ N B, Wk (S.withStep step2) N B → Wk (S.withStep step1) N B := by
  have hpost : ∀ (B : S.X → Prop) (a : S.A) (y : S.Y) (x' : S.X),
      post (S.withStep step1) B a y x' → post (S.withStep step2) B a y x' := by
    intro B a y x' hx'
    cases hx' with
    | intro x hx => exact ⟨x, hx.1, hsub a x x' hx.2.1, hx.2.2⟩
  intro N
  induction N with
  | zero => intro B h; exact h
  | succ m ih =>
      intro B h
      refine ⟨h.1, h.2.elim (fun a ha => ⟨a, ha.1, fun y hy => ?_⟩)⟩
      have hposs2 : possible (S.withStep step2) B a y := by
        cases hy with
        | intro x' hx' => exact ⟨x', hpost B a y x' hx'⟩
      have hW2post1 : Wk (S.withStep step2) m (post (S.withStep step1) B a y) :=
        Wk_antitone m (post (S.withStep step2) B a y) (post (S.withStep step1) B a y)
          (fun x' hx' => hpost B a y x' hx') (ha.2 y hposs2)
      exact ih _ hW2post1

/-! ## Numerical robustness of the polyhedral (Farkas) certificate -/

section RobustFarkas
variable {K : Type} [OrdField K]

theorem sumRange_const_mul (c : K) (f : Nat → K) :
    ∀ n, sumRange (fun i => c * f i) n = c * sumRange f n := by
  intro n
  induction n with
  | zero => exact (mul_zero c).symm
  | succ m ih =>
      rw [sumRange_succ (fun i => c * f i) m, sumRange_succ f m, ih]
      show c * sumRange f m + c * f m = c * (sumRange f m + f m)
      rw [← left_distrib]

/-- Perturbation robustness of the Farkas certificate: multipliers
certifying infeasibility with margin `μ₀ > 0` survive right-hand-side
perturbations bounded by `ε` as long as `ε · Σλ < μ₀` — the margin `μ₀` is
exactly the certificate's numerical robustness.

Paper reference: the numerical-robustness remark on the polyhedral
certificate (`rem:robust-farkas`), first part (graceful degradation of the
margin under bounded data perturbation). -/
theorem farkas_perturbed (a : Nat → List K) (b : Nat → K) (lam : Nat → K)
    (x : List K) (n : Nat) (μ₀ ε : K)
    (hlen : ∀ i, i < n → (a i).length = x.length)
    (hnonneg : ∀ i, i < n → 0 ≤ lam i)
    (hzero : linComb (List.replicate x.length 0) lam a n = List.replicate x.length 0)
    (hneg : sumRange (fun i => lam i * b i) n ≤ -μ₀)
    (db : Nat → K) (hdb : ∀ i, i < n → db i ≤ ε)
    (hmargin : -μ₀ + ε * sumRange lam n < 0) :
    ¬ (∀ i, i < n → dotp (a i) x ≤ b i + db i) := by
  have hc : (fun i => lam i * (b i + db i))
      = (fun i => lam i * b i + lam i * db i) :=
    funext (fun i => left_distrib (lam i) (b i) (db i))
  have hlamdb : sumRange (fun i => lam i * db i) n ≤ ε * sumRange lam n := by
    have h1 : sumRange (fun i => lam i * db i) n ≤ sumRange (fun i => lam i * ε) n :=
      sumRange_le_sumRange' _ _ n (fun i hi =>
        mul_le_mul_of_nonneg_left (hdb i hi) (hnonneg i hi))
    have hc2 : (fun i => lam i * ε) = (fun i => ε * lam i) :=
      funext (fun i => mul_comm (lam i) ε)
    rw [hc2] at h1
    rw [sumRange_const_mul ε lam n] at h1
    exact h1
  have htotal : sumRange (fun i => lam i * (b i + db i)) n
      ≤ -μ₀ + ε * sumRange lam n := by
    rw [hc, sumRange_add]
    exact add_le_add hneg hlamdb
  have hstrict : sumRange (fun i => lam i * (b i + db i)) n < 0 :=
    lt_of_le_of_lt htotal hmargin
  exact farkas_sound a (fun i => b i + db i) lam x n hlen hnonneg hzero hstrict

end RobustFarkas

/-! ## Exact observation-only certification (Section 4.1) -/

section Certifier
variable {Z Yc : Type}

/-- An exact certifier based on `O` is `C : Y → {0,1}` with
`C(O(z)) = 1 ↔ z ∈ K` for every `z ∈ Z`.

Paper reference: Definition `def:certifier` (exact certifier). -/
def ExactCertifier (O : Z → Yc) (Km : Z → Prop) (C : Yc → Bool) : Prop :=
  ∀ z, C (O z) = true ↔ Km z

/-- Membership in `K` is constant on every observation fibre. -/
def FibreConst (O : Z → Yc) (Km : Z → Prop) : Prop :=
  ∀ z1 z2, O z1 = O z2 → (Km z1 ↔ Km z2)

/-- An exact observation-only certifier exists if and only if membership in
`K` is constant on every observation fibre.

Paper reference: Proposition `prop:fibre` (observation-fibre criterion). -/
theorem fibre_criterion (O : Z → Yc) (Km : Z → Prop) :
    (∃ C, ExactCertifier O Km C) ↔ FibreConst O Km := by
  constructor
  · intro h
    cases h with
    | intro C hC =>
        intro z1 z2 hO
        rw [← hC z1, ← hC z2, hO]
  · intro hconst
    -- the verdict of each fibre is determined; select it classically
    have key : ∀ y z1 z2, O z1 = y → O z2 = y → (Km z1 ↔ Km z2) :=
      fun y z1 z2 h1 h2 => hconst z1 z2 (h1.trans h2.symm)
    have hval : ∀ y : Yc,
        Nonempty {b : Bool //
          (∀ z, O z = y → Km z → b = true) ∧ (∀ z, O z = y → ¬ Km z → b = false)} := by
      intro y
      by_cases hpos : ∃ z, O z = y ∧ Km z
      · exact ⟨⟨true,
          fun z hOy hKmz => rfl,
          fun z hOy hnKmz => by
            cases hpos with
            | intro z1 hz1 =>
                exact absurd ((key y z1 z hz1.1 hOy).mp hz1.2) hnKmz⟩⟩
      · exact ⟨⟨false,
          fun z hOy hKmz => absurd ⟨z, hOy, hKmz⟩ hpos,
          fun _ _ _ => rfl⟩⟩
    refine ⟨fun y => (Classical.choice (hval y)).val, ?_⟩
    intro z
    constructor
    · intro hCtrue
      by_cases hKmz : Km z
      · exact hKmz
      · have hCtrue' : (Classical.choice (hval (O z))).val = true := hCtrue
        rw [(Classical.choice (hval (O z))).property.2 z rfl hKmz] at hCtrue'
        exact Bool.noConfusion hCtrue'
    · intro hKmz
      exact (Classical.choice (hval (O z))).property.1 z rfl hKmz

/-- The certainly-safe set: the observations whose every compatible state is
in `K` — the sound region for a constant "safe" verdict.

Paper reference: Corollary `cor:certainly-safe` (safety-crossing fibres and
the certainly-safe set). -/
def Ysafe (O : Z → Yc) (Km : Z → Prop) (y : Yc) : Prop := ∀ z, O z = y → Km z

/-- A safety-crossing pair — two admissible states sharing an observation,
one in `K` and one outside — denies every exact observation-only
certificate.

Paper reference: Corollary `cor:certainly-safe`. -/
theorem crossing_denies (O : Z → Yc) (Km : Z → Prop) {z1 z2 : Z}
    (hO : O z1 = O z2) (h1 : Km z1) (h2 : ¬ Km z2) :
    ¬ ∃ C, ExactCertifier O Km C := by
  intro hC
  cases hC with
  | intro C hC' =>
      have hC1 := (hC' z1).mpr h1
      rw [hO] at hC1
      exact h2 ((hC' z2).mp hC1)

/-- Outside the certainly-safe set some compatible state is unsafe, so no
sound "safe" verdict exists there. -/
theorem not_Ysafe_iff (O : Z → Yc) (Km : Z → Prop) (y : Yc) :
    ¬ Ysafe O Km y ↔ ∃ z, O z = y ∧ ¬ Km z := by
  constructor
  · intro h
    apply Classical.byContradiction
    intro hnex
    apply h
    intro z hOz
    exact Classical.byContradiction (fun hKm => hnex ⟨z, hOz, hKm⟩)
  · intro h hall
    cases h with
    | intro z hz => exact hz.2 (hall z hz.1)

end Certifier

/-! ## The hidden-mode conflict example (Example 3.2's skeleton) -/

namespace HiddenMode

/-- The hidden mode: `pos` (θ = +1) and `neg` (θ = -1) at the boundary
`z = 0`, plus the exited state `out`. -/
inductive Mode where
  | pos
  | neg
  | out

/-- The two actions: u = +1 (up) and u = -1 (down). -/
inductive Act where
  | up
  | down

/-- ẋ = θu with floor z ≥ 0: from `pos` only `up` is safe (self-loop), from
`neg` only `down` is safe; the wrong action exits. -/
def sysstep : Act → Mode → Mode → Prop
  | Act.up, Mode.pos, Mode.pos => True
  | Act.down, Mode.neg, Mode.neg => True
  | Act.down, Mode.pos, Mode.out => True
  | Act.up, Mode.neg, Mode.out => True
  | _, _, _ => False

/-- Constant (uninformative) observation on the window. -/
def obsR : Unit → Mode → Mode → Prop := fun _ _ _ => True

def safeM : Mode → Prop := fun m => m ≠ Mode.out
def admM : Act → Mode → Prop := fun _ _ => True

def SYS : FinSys where
  X := Mode
  A := Act
  Y := Unit
  step := sysstep
  obsRel := obsR
  safe := safeM
  admissible := admM

theorem obsTotal_SYS : ∀ a x x', SYS.step a x x' → ∃ y, SYS.obsRel y x x' :=
  fun _ _ _ _ => ⟨Unit.unit, trivial⟩

theorem sysstep_up_inv (x x' : Mode) (h : sysstep Act.up x x') :
    (x = Mode.pos ∧ x' = Mode.pos) ∨ (x = Mode.neg ∧ x' = Mode.out) := by
  cases x <;> cases x' <;>
    first
    | exact Or.inl ⟨rfl, rfl⟩
    | exact Or.inr ⟨rfl, rfl⟩
    | exact absurd h (fun hh => by nomatch hh)

theorem sysstep_down_inv (x x' : Mode) (h : sysstep Act.down x x') :
    (x = Mode.neg ∧ x' = Mode.neg) ∨ (x = Mode.pos ∧ x' = Mode.out) := by
  cases x <;> cases x' <;>
    first
    | exact Or.inl ⟨rfl, rfl⟩
    | exact Or.inr ⟨rfl, rfl⟩
    | exact absurd h (fun hh => by nomatch hh)

theorem post_B_up_iff {B : Mode → Prop} (hBpos : B Mode.pos)
    (hBsub : ∀ x, B x → x = Mode.pos) (m : Mode) :
    post SYS B Act.up Unit.unit m ↔ m = Mode.pos := by
  constructor
  · intro h
    cases h with
    | intro x hx =>
        cases sysstep_up_inv x m hx.2.1 with
        | inl hinl => exact hinl.2
        | inr hinr => exact Mode.noConfusion ((hBsub x hx.1).symm.trans hinr.1)
  · intro h
    refine ⟨Mode.pos, hBpos, ?_, trivial⟩
    rw [h]
    exact trivial

theorem post_B_down_iff {B : Mode → Prop} (hBneg : B Mode.neg)
    (hBsub : ∀ x, B x → x = Mode.neg) (m : Mode) :
    post SYS B Act.down Unit.unit m ↔ m = Mode.neg := by
  constructor
  · intro h
    cases h with
    | intro x hx =>
        cases sysstep_down_inv x m hx.2.1 with
        | inl hinl => exact hinl.2
        | inr hinr => exact Mode.noConfusion ((hBsub x hx.1).symm.trans hinr.1)
  · intro h
    refine ⟨Mode.neg, hBneg, ?_, trivial⟩
    rw [h]
    exact trivial

/-- The joint information set `B = {(0,+1), (0,-1)}`. -/
def Bjoint : Mode → Prop := fun m => m = Mode.pos ∨ m = Mode.neg

def Bpos : Mode → Prop := fun m => m = Mode.pos
def Bneg : Mode → Prop := fun m => m = Mode.neg

/-- The common safe-action set of the joint belief is empty. -/
theorem commonSafe_Bjoint_empty : ∀ a, ¬ commonSafe SYS Bjoint a := by
  intro a
  cases a with
  | up =>
      intro h
      have hout := h.2 Mode.neg (Or.inr rfl) Mode.out trivial
      exact hout rfl
  | down =>
      intro h
      have hout := h.2 Mode.pos (Or.inl rfl) Mode.out trivial
      exact hout rfl

/-- The individually-viable invariant: singleton (or empty-of-the-other-mode)
beliefs, each maintained by its own safe action. -/
def Qind : (Mode → Prop) → Prop := fun B =>
  (B Mode.pos ∧ ¬ B Mode.neg ∧ ¬ B Mode.out) ∨
    (B Mode.neg ∧ ¬ B Mode.pos ∧ ¬ B Mode.out)

theorem qind_postfixed : ∀ B, Qind B → epiPre SYS Qind B := by
  intro B hB
  cases hB with
  | inl h =>
      have hBsub : ∀ x, B x → x = Mode.pos := by
        intro x hx
        cases x with
        | pos => rfl
        | neg => exact absurd hx h.2.1
        | out => exact absurd hx h.2.2
      refine ⟨fun x hx => ?_, Act.up, fun _ _ => trivial, fun y hy => ?_⟩
      · rw [hBsub x hx]
        exact fun hh => Mode.noConfusion hh
      · cases y with
        | unit =>
            refine Or.inl ⟨?_, ?_, ?_⟩
            · exact ⟨Mode.pos, h.1, trivial, trivial⟩
            · intro hm
              exact Mode.noConfusion ((post_B_up_iff h.1 hBsub Mode.neg).mp hm)
            · intro hm
              exact Mode.noConfusion ((post_B_up_iff h.1 hBsub Mode.out).mp hm)
  | inr h =>
      have hBsub : ∀ x, B x → x = Mode.neg := by
        intro x hx
        cases x with
        | pos => exact absurd hx h.2.1
        | neg => rfl
        | out => exact absurd hx h.2.2
      refine ⟨fun x hx => ?_, Act.down, fun _ _ => trivial, fun y hy => ?_⟩
      · rw [hBsub x hx]
        exact fun hh => Mode.noConfusion hh
      · cases y with
        | unit =>
            refine Or.inr ⟨?_, ?_, ?_⟩
            · exact ⟨Mode.neg, h.1, trivial, trivial⟩
            · intro hm
              exact Mode.noConfusion ((post_B_down_iff h.1 hBsub Mode.pos).mp hm)
            · intro hm
              exact Mode.noConfusion ((post_B_down_iff h.1 hBsub Mode.out).mp hm)

/-- The hidden-mode conflict: the joint information set is outside the
epistemic kernel — the common safe-action set is empty — while each
compatible state is individually viable under full information.

Paper reference: Example `ex:hidden-mode` (hidden-mode conflict). -/
theorem hidden_mode_conflict :
    ¬ EpiK SYS Bjoint ∧ EpiK SYS Bpos ∧ EpiK SYS Bneg :=
  ⟨common_action_obstruction SYS obsTotal_SYS commonSafe_Bjoint_empty,
    epiK_coind SYS Qind qind_postfixed
      (Or.inl ⟨rfl, fun h => Mode.noConfusion h, fun h => Mode.noConfusion h⟩),
    epiK_coind SYS Qind qind_postfixed
      (Or.inr ⟨rfl, fun h => Mode.noConfusion h, fun h => Mode.noConfusion h⟩)⟩

end HiddenMode

end Formalizations.P1

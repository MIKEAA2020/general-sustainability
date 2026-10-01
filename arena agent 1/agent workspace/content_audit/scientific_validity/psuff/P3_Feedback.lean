/-
  Formalizations.P3_Feedback
  ==========================

  **Resolving the `Wmem` / `Wblind` question of v27 — with a proof, not a
  decision.**

  v27 defined two viable-set recursions and refused to choose between them:

    `Wblind`  one continuation for all successors — open loop, a schedule
              `Nat → A`.  This is what `survT` / `survK` / `VR` implement,
              and what `prop:degen` states (blind window, declared
              sequential class `Π_B`).
    `Wmem`    a continuation per observation — feedback, a policy tree.
              This is what the paper's recursion says literally:
              `∃a, ∀y, Post(B,a,y) ∈ 𝒲_{k-1}`.

  Two readings of `thm:support` consequence 1 ("for the unrestricted
  sequential class, `V_k(b) = 1` iff `supp(b) ∈ 𝒲_k`"), and v27 recorded
  `Wblind_le_Wmem` as the only unconditional direction.

  This module settles it in three steps.

  ## 1. They are genuinely different — `Wmem_le_Wblind` is **false**

  `Wmem_not_le_Wblind` exhibits a model with **deterministic kernels**
  (`|univD x a| = 1` everywhere) and a **deterministic observation map** —
  i.e. inside `thm:support`'s own hypothesis class — on which
  `Wmem M 2 B ∧ ¬ Wblind M 2 B`.  So the ambiguity is not cosmetic: the two
  recursions define different set families, and which one `𝒲_k` denotes
  changes the content of consequence 1.  Anything that claims to close
  consequence 1 must say which.

  The mechanism is the ordinary value of observation: the belief puts mass
  on `{p, q}`; one action separates the branches (`p ↦ p₁`, `q ↦ q₁`, with
  different observations); at the second stage `b` is safe only at `p₁` and
  `c` only at `q₁`.  A feedback policy survives both branches; no single
  schedule does.

  ## 2. `Wmem` is *exactly* feedback survival

  `Wmem_iff_feedback`: `Wmem M k B` iff some **observation-history policy**
  `π : List Y → A`, admissible at every history, keeps every `x ∈ B` alive
  for `k` steps (`survPol`).  This is the analogue of v27's
  `Wblind_iff_survK` for the other reading, so both readings now sit on the
  same footing: each is identified with survival under a policy class.

  ## 3. On a blind window they coincide — which is why both are "right"

  `Wmem_eq_Wblind_of_blind`: if the observation map is constant, the two
  recursions agree at every `k` and `B`.  Combined with the counterexample
  this localises the gap exactly:

    * `prop:degen` is stated for a **blind window** with declared
      sequential class `Π_B`.  There the observation carries no
      information, so `Wmem = Wblind`, and v27's `Wblind_iff_survK`
      (hence `survT_iff_survK`, hence `VR`) is the correct formalization.
      This is `thm:lattice`'s middle equality `V^ol = V^{seq,blind}`,
      proved here at the level of the viable-set families.
    * `thm:support` consequence 1 is stated for the **unrestricted
      sequential class**, which `def:value` defines as
      "`Π = Π_seq`, the class of all sequential policies" — feedback.
      No blind-window hypothesis is in force.  There `Wmem` is the
      required notion, and the paper's own `thm:recursion`
      (`V_k = max_a Σ_y P(y|b,a) V_{k-1}(τ(b,a,y))`, the recursion whose
      `∀y` is precisely the `∀y` in the definition of `𝒲_k`) derives it.

  ## What is *not* claimed

  `Wmem_iff_feedback` is a theorem about the **set** side.  Consequence 1
  also needs the **value** side — a feedback value operator, i.e. a
  maximum over policy trees, where `VR` (`P3_Deterministic`) is a maximum
  over action *tuples*.  The layer has no such operator and building one
  is a separate piece of work (the policy class must be reduced to a
  finite one before `lmax` applies).  It is left open and recorded in the
  audit report rather than faked: this module makes the *set-level*
  question decidable and shows the answer is `Wmem`, not `Wblind`.

  ## Contents

    survPol                 survival under an observation-history policy
    survPol_congr           `survPol` sees the policy only through suffixes
    Wmem_iff_feedback       **`Wmem` = feedback survival** (the main theorem)
    Wmem_eq_Wblind_of_blind on a blind window the two readings coincide
    WmX, WmA, WmD, wmModel  an explicit deterministic-kernel model
    Wmem_not_le_Wblind      **`Wmem ⊄ Wblind`, inside `thm:support`'s class**
-/

import Formalizations.Prelude
import Formalizations.P3_Deterministic
import Formalizations.P3_Freeze_Noisy
import Formalizations.P3_Bridge
import Formalizations.P3_Viable

namespace Formalizations.P3

open Formalizations
open Formalizations.POMDP

set_option linter.unusedSectionVars false

variable {K : Type} [OrdField K]
variable {X A D Y : Type}

/-! ## Survival under a feedback policy -/

/-- A feedback policy is a map `List Y → A` — the action played at a stage, as
a function of the observations received so far.  A blind schedule is the
degenerate case `fun _ => a`, but a general `π` may branch on what has been
seen.

`survPol M k π h x`: `x` survives `k` steps under the policy `π`,
having already recorded the observation history `h`, adversarially in the
disturbance.  The history grows by appending the observation emitted by the
step just taken. -/
def survPol (M : DetMDP K X A D Y) : Nat → (List Y → A) → List Y → X → Prop
  | 0, _, _, x => M.safe x = true
  | k + 1, π, h, x =>
      M.safe x = true ∧
        ∀ d, d ∈ M.univD x (π h) →
          survPol M k π (h ++ [M.obs x (π h) (M.F x (π h) d)])
            (M.F x (π h) d)

/-- **`survPol` is insensitive to how the policy behaves off the current
history.**  Two policies that agree on every continuation of `h`
(respectively `h'`) drive the same survival.  Needed to splice a
per-observation family of policies into one. -/
theorem survPol_congr (M : DetMDP K X A D Y) :
    ∀ k (π π' : List Y → A) (h h' : List Y) (x : X),
      (∀ s, π (h ++ s) = π' (h' ++ s)) →
      survPol M k π h x → survPol M k π' h' x := by
  intro k
  induction k with
  | zero =>
      intro π π' h h' x _ hs
      simpa [survPol] using hs
  | succ k ih =>
      intro π π' h h' x hagree hs
      rcases hs with ⟨hsafe, hall⟩
      have ha : π h = π' h' := by simpa using hagree []
      constructor
      · exact hsafe
      · intro d hd
        have hd' : d ∈ M.univD x (π h) := by simpa [ha] using hd
        apply ih π π' (h ++ [M.obs x (π' h') (M.F x (π' h') d)])
          (h' ++ [M.obs x (π' h') (M.F x (π' h') d)]) (M.F x (π' h') d)
        · intro s
          simpa [List.append_assoc] using
            hagree ([M.obs x (π' h') (M.F x (π' h') d)] ++ s)
        · simpa [ha] using hall d hd'

/-! ## The identification: `Wmem` = feedback survival -/

/-- **`Wmem`-viability is exactly survival under an admissible feedback
policy.**  Left: the paper's `∀y` recursion.  Right: one policy
`π : List Y → A`, admissible at every history, keeping every `x ∈ B` alive
for `k` steps.

Contrast `Wblind_iff_survK` (`P3_Viable`): there the witness is a single
schedule `Nat → A`; here it is a policy that may branch on observations. -/
theorem Wmem_iff_feedback (M : DetMDP K X A D Y) : ∀ k (B : X → Prop),
    Wmem M k B ↔
      ∃ π : List Y → A, (∀ h, π h ∈ M.univA) ∧
        ∀ x, B x → survPol M k π [] x := by
  classical
  intro k
  induction k with
  | zero =>
      intro B
      constructor
      · intro hB
        rcases exists_mem_of_ne_nil M.univA_ne with ⟨a0, ha0⟩
        exact ⟨fun _ => a0, fun _ => ha0, hB⟩
      · rintro ⟨π, _hadm, hs⟩ x hx
        exact hs x hx
  | succ k ih =>
      intro B
      constructor
      · intro hB
        rcases hB with ⟨hsafe, a, ha, hy⟩
        -- for each observation, the continuation policy that `Wmem` supplies
        let pick : Y → (List Y → A) := fun y =>
          Classical.choose ((ih (postPred M B a y)).mp (hy y))
        let π : List Y → A := fun h =>
          match h with
          | [] => a
          | y :: rest => pick y rest
        refine ⟨π, ?_, ?_⟩
        · intro h
          cases h with
          | nil => exact ha
          | cons y rest =>
              exact (Classical.choose_spec
                ((ih (postPred M B a y)).mp (hy y))).1 rest
        · intro x hxB
          constructor
          · exact hsafe x hxB
          · intro d hd
            let y := M.obs x a (M.F x a d)
            have hx' : postPred M B a y (M.F x a d) :=
              ⟨x, hxB, d, hd, rfl, rfl⟩
            have hspec : survPol M k (pick y) [] (M.F x a d) :=
              (Classical.choose_spec
                ((ih (postPred M B a y)).mp (hy y))).2 (M.F x a d) hx'
            -- `π` agrees with `pick y` on every history beginning with `y`
            exact survPol_congr M k (pick y) π [] [y] (M.F x a d)
              (by intro s; rfl) hspec
      · rintro ⟨π, hadm, hsurv⟩
        refine ⟨?_, π [], hadm [], ?_⟩
        · intro x hxB
          exact (hsurv x hxB).1
        · intro y
          apply (ih (postPred M B (π []) y)).mpr
          refine ⟨fun s => π (y :: s), ?_, ?_⟩
          · intro s
            exact hadm (y :: s)
          · intro x' hx'
            rcases hx' with ⟨x, hxB, d, hd, hF, hobs⟩
            have hrec : survPol M k π [M.obs x (π []) x'] x' := by
              simpa [hF] using (hsurv x hxB).2 d hd
            exact survPol_congr M k π (fun s => π (y :: s))
              [M.obs x (π []) x'] [] x'
              (by
                intro s
                change π (M.obs x (π []) x' :: s) = π (y :: s)
                rw [hobs])
              hrec

/-! ## Where the two readings coincide: the blind window -/

/-- On a **blind window** the observation carries no information, so the
observation-split recursion collapses onto the blind one.  This is the
set-level form of `thm:lattice`'s middle equality
`V^{ol} = V^{seq,blind}` — "inside the blind window no observation arrives,
so sequential blind policies reduce to open-loop sequences". -/
theorem Wmem_le_Wblind_of_blind (M : DetMDP K X A D Y) (y0 : Y)
    (hblind : ∀ x a x', M.obs x a x' = y0) :
    ∀ k (B : X → Prop), Wmem M k B → Wblind M k B := by
  intro k
  induction k with
  | zero =>
      intro B h
      exact h
  | succ k ih =>
      intro B h
      rcases h with ⟨hsafe, a, ha, hy⟩
      refine ⟨hsafe, a, ha, ?_⟩
      -- with a constant observation map the `y₀`-slice *is* the successor set
      have hEq : postPred M B a y0 = succPred M B a := by
        funext x'
        apply propext
        simp [postPred, succPred, hblind]
      have hmem : Wmem M k (succPred M B a) := by
        simpa [hEq] using hy y0
      exact ih (succPred M B a) hmem

/-- **On a blind window the two readings of `𝒲_k` are the same family.**
The forward direction is the collapse above; the reverse is
`Wblind_le_Wmem` (`P3_Viable`), which holds unconditionally. -/
theorem Wmem_eq_Wblind_of_blind (M : DetMDP K X A D Y) (y0 : Y)
    (hblind : ∀ x a x', M.obs x a x' = y0) :
    ∀ k (B : X → Prop), Wmem M k B ↔ Wblind M k B := by
  intro k B
  constructor
  · exact Wmem_le_Wblind_of_blind M y0 hblind k B
  · exact Wblind_le_Wmem M k B

/-! ## An explicit model on which the two differ

Deterministic kernels (`|univD x a| = 1` for every `x`, `a`) and a
deterministic observation map — the hypotheses of `thm:support`.  The
belief's support is `{p, q}`; the first action separates the branches and
the observations report which branch; the second action must differ
between them. -/

/-- States of the separating model. -/
inductive WmX where
  | x0 | p | q | p1 | q1 | good | dead
  deriving DecidableEq

/-- Actions: `a0` separates the branches; `b` is safe only at `p1`, `c`
only at `q1`. -/
inductive WmA where
  | a0 | b | c
  deriving DecidableEq

/-- A single disturbance — the kernel is deterministic. -/
inductive WmD where
  | d0
  deriving DecidableEq

/-- The model.  `Y = Bool`: `true` reports the `p`-branch, `false` the
`q`-branch. -/
def wmModel (K : Type) [OrdField K] : DetMDP K WmX WmA WmD Bool where
  univX := [WmX.x0, WmX.p, WmX.q, WmX.p1, WmX.q1, WmX.good, WmX.dead]
  univX_nodup := by decide
  univA := [WmA.a0, WmA.b, WmA.c]
  univA_ne := by decide
  univD := fun _ _ => [WmD.d0]
  univD_ne := by intro x a; decide
  F := fun x a _ =>
    match x, a with
    | WmX.p, WmA.a0 => WmX.p1
    | WmX.q, WmA.a0 => WmX.q1
    | WmX.p1, WmA.b => WmX.good
    | WmX.q1, WmA.c => WmX.good
    | _, _ => WmX.dead
  obs := fun x a x' =>
    match x, a, x' with
    | WmX.p, WmA.a0, WmX.p1 => true
    | _, _, _ => false
  safe := fun x =>
    match x with
    | WmX.dead => false
    | _ => true

/-- The support: a belief that does not know which branch it is on. -/
def wmB : WmX → Prop := fun x => x = WmX.p ∨ x = WmX.q

/-- The `true`-slice is `{p1}`: only `p` reports `true`. -/
theorem wm_slice_true (K : Type) [OrdField K] (x' : WmX) :
    postPred (wmModel K) wmB WmA.a0 true x' → x' = WmX.p1 := by
  intro hx'
  rcases hx' with ⟨x, hxB, d, hd, hF, hobs⟩
  rcases hxB with rfl | rfl
  · cases d
    simp [wmModel] at hF
    exact hF.symm
  · cases d
    simp [wmModel] at hF
    subst x'
    simp [wmModel] at hobs

/-- The `false`-slice is `{q1}`: only `q` reports `false`. -/
theorem wm_slice_false (K : Type) [OrdField K] (x' : WmX) :
    postPred (wmModel K) wmB WmA.a0 false x' → x' = WmX.q1 := by
  intro hx'
  rcases hx' with ⟨x, hxB, d, hd, hF, hobs⟩
  rcases hxB with rfl | rfl
  · cases d
    simp [wmModel] at hF
    subst x'
    simp [wmModel] at hobs
  · cases d
    simp [wmModel] at hF
    exact hF.symm

/-- **Feedback viability: both branches are kept alive, by branching on
the observation.** -/
theorem wm_Wmem (K : Type) [OrdField K] : Wmem (wmModel K) 2 wmB := by
  constructor
  · intro x hx
    rcases hx with rfl | rfl <;> rfl
  · refine ⟨WmA.a0, by simp [wmModel], ?_⟩
    intro y
    cases y
    · -- observation `false`: the `q`-branch, continue with `c`
      constructor
      · intro x' hx'
        have h := wm_slice_false K x' hx'
        subst x'
        rfl
      · refine ⟨WmA.c, by simp [wmModel], ?_⟩
        intro y' x'' hx''
        rcases hx'' with ⟨x', hx', d, hd, hF, _hobs⟩
        have hq1 := wm_slice_false K x' hx'
        subst x'
        cases d
        simp [wmModel] at hF
        subst x''
        rfl
    · -- observation `true`: the `p`-branch, continue with `b`
      constructor
      · intro x' hx'
        have h := wm_slice_true K x' hx'
        subst x'
        rfl
      · refine ⟨WmA.b, by simp [wmModel], ?_⟩
        intro y' x'' hx''
        rcases hx'' with ⟨x', hx', d, hd, hF, _hobs⟩
        have hp1 := wm_slice_true K x' hx'
        subst x'
        cases d
        simp [wmModel] at hF
        subst x''
        rfl

/-- **No blind schedule keeps both branches alive.**  Whichever action is
declared first, the joint successor set admits no common safe second
action. -/
theorem wm_not_Wblind (K : Type) [OrdField K] : ¬ Wblind (wmModel K) 2 wmB := by
  intro h
  rcases h with ⟨_hsafe, a, ha, hpost⟩
  simp [wmModel] at ha
  rcases ha with rfl | rfl | rfl
  · -- `a0`: successors `{p1, q1}`; `b` kills `q1`, `c` kills `p1`, `a0` kills both
    rcases hpost with ⟨_hs, a', ha', h0⟩
    simp [wmModel] at ha'
    rcases ha' with rfl | rfl | rfl
    · have hmem : succPred (wmModel K) (succPred (wmModel K) wmB WmA.a0) WmA.a0 WmX.dead := by
        refine ⟨WmX.p1, ?_, WmD.d0, ?_, rfl⟩
        · exact ⟨WmX.p, Or.inl rfl, WmD.d0, by simp [wmModel], rfl⟩
        · simp [wmModel]
      have hs := h0 WmX.dead hmem
      simp [wmModel] at hs
    · have hmem : succPred (wmModel K) (succPred (wmModel K) wmB WmA.a0) WmA.b WmX.dead := by
        refine ⟨WmX.q1, ?_, WmD.d0, ?_, rfl⟩
        · exact ⟨WmX.q, Or.inr rfl, WmD.d0, by simp [wmModel], rfl⟩
        · simp [wmModel]
      have hs := h0 WmX.dead hmem
      simp [wmModel] at hs
    · have hmem : succPred (wmModel K) (succPred (wmModel K) wmB WmA.a0) WmA.c WmX.dead := by
        refine ⟨WmX.p1, ?_, WmD.d0, ?_, rfl⟩
        · exact ⟨WmX.p, Or.inl rfl, WmD.d0, by simp [wmModel], rfl⟩
        · simp [wmModel]
      have hs := h0 WmX.dead hmem
      simp [wmModel] at hs
  · -- `b`: `p` goes straight to `dead`
    rcases hpost with ⟨hs, _a', _h0⟩
    have hmem : succPred (wmModel K) wmB WmA.b WmX.dead :=
      ⟨WmX.p, Or.inl rfl, WmD.d0, by simp [wmModel], rfl⟩
    have hs' := hs WmX.dead hmem
    simp [wmModel] at hs'
  · -- `c`: likewise
    rcases hpost with ⟨hs, _a', _h0⟩
    have hmem : succPred (wmModel K) wmB WmA.c WmX.dead :=
      ⟨WmX.p, Or.inl rfl, WmD.d0, by simp [wmModel], rfl⟩
    have hs' := hs WmX.dead hmem
    simp [wmModel] at hs'

/-- The kernel is **deterministic**: one disturbance per `(x, a)`. -/
def DetKernel (M : DetMDP K X A D Y) : Prop :=
  ∀ x a, ∀ d1, d1 ∈ M.univD x a → ∀ d2, d2 ∈ M.univD x a →
    M.F x a d1 = M.F x a d2

theorem wm_detKernel (K : Type) [OrdField K] : DetKernel (wmModel K) := by
  intro x a d1 _hd1 d2 _hd2
  rfl

/-- **`Wmem ⊄ Wblind`, on a model with deterministic kernels and a
deterministic observation map.**  The two readings of `𝒲_k` are genuinely
different families of sets, so `thm:support` consequence 1 has two
different contents and the paper must say which one it claims. -/
theorem Wmem_not_le_Wblind (K : Type) [OrdField K] :
    ∃ (M : DetMDP K WmX WmA WmD Bool) (B : WmX → Prop),
      DetKernel M ∧ Wmem M 2 B ∧ ¬ Wblind M 2 B :=
  ⟨wmModel K, wmB, wm_detKernel K, wm_Wmem K, wm_not_Wblind K⟩

/-- The corollary in the form that rules out a general proof: there is no
theorem "`Wmem k B → Wblind k B`" even under deterministic kernels. -/
theorem Wmem_le_Wblind_is_false (K : Type) [OrdField K] :
    ¬ (∀ (M : DetMDP K WmX WmA WmD Bool) (k : Nat) (B : WmX → Prop),
        DetKernel M → Wmem M k B → Wblind M k B) := by
  intro h
  rcases (Wmem_not_le_Wblind K) with ⟨M, B, hdk, hmem, hnblind⟩
  exact hnblind (h M 2 B hdk hmem)

end Formalizations.P3

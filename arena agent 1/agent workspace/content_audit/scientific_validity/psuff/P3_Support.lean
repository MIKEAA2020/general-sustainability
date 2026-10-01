/-
  Formalizations.P3_Support
  =========================

  `thm:support` (v11 of the paper), the last open P3 result:

  > On finite models with deterministic kernels and deterministic
  > observation maps, for every action `a` and observation `y`,
  >     supp(b⁺(· | a, y)) = Post(supp(b), a, y),
  > the set-valued post-state of the calculus.

  The paper's proof:

  > A state `x'` carries posterior mass exactly when some `x ∈ supp(b)` has
  > `T(x'|x,a) · g(y|x,a,x') > 0`; with deterministic kernels and
  > observation maps the indicators make this set exactly
  > `Post(supp(b), a, y)`.

  ## Why this belongs to `SafeMDP`, not `DetMDP`

  The earlier P3 modules are built on `DetMDP`, whose `obs : X → A → X → Y`
  is *already* a deterministic function — so there the identity is vacuous:
  there is no kernel to degenerate. `thm:support` is a statement about the
  degeneration, so it must be stated where the kernels are genuinely
  stochastic. That is `SafeMDP` (`P1_BeliefSafety`), which carries

      T : A → X → X → K          g : A → X → X → Y → K

  with nonnegativity and normalization. The theorem is then: *if* those
  kernels are `0/1`-valued (the `DetKernels` structure below), *then* the
  posterior support is the set-valued image. This is the right level, and it
  makes the theorem's hypothesis an explicit assumption rather than
  something built into the model.

  ## Contents

    le_lsum_of_mem      one nonnegative term is below its sum
    lsum_pos_exists     a positive sum of nonnegative terms has a positive term
    DetKernels          the `0/1` degeneration of `T` and `g`
    suppOf, postMem     support as a predicate, and `Post(B, a, y)`
    obsMass_eq_filter   the posterior collapses to a filtered sum
    support_identity    **thm:support**

  ## Scope

  Proved here: the support identity. **Not** proved: the three consequences
  (`V_k(b) = 1 ⟺ supp(b) ∈ 𝒲_k`; `1 - V_k(b) ≥ min_{x ∈ supp b} b(x)`;
  monotonicity in `k`). The first is `prop:degen`'s content, which is already
  formalized as `VR` in `P3_Deterministic`; the third overlaps `prop:freeze`
  (v18); and the middle one needs a bridge between `SafeMDP`'s `V` and
  `DetMDP`'s `VR`, which is a structural identification rather than a
  corollary. That bridge is the natural next piece of work.
-/

import Formalizations.Prelude
import Formalizations.P1_BeliefSafety

namespace Formalizations.P3

open Formalizations
open Formalizations.POMDP

set_option linter.unusedSectionVars false

variable {K : Type} [OrdField K]
variable {X Y A : Type}
variable [DecidableEq X] [DecidableEq Y]

/-! ## Two `lsum` facts this layer lacks -/

/-- One nonnegative term is below the sum of the list containing it. -/
theorem le_lsum_of_mem {l : List X} {f : X → K} {x : X} (hx : x ∈ l)
    (hnn : ∀ a, a ∈ l → 0 ≤ f a) : f x ≤ lsum (l.map f) := by
  induction l with
  | nil => cases hx
  | cons a t ih =>
      rcases (by simpa using hx : x = a ∨ x ∈ t) with hxa | hxt
      · subst x
        have htail : 0 ≤ lsum (t.map f) :=
          lsum_nonneg (t.map f) (by
            intro z hz
            rcases List.mem_map.mp hz with ⟨y, hy, rfl⟩
            exact hnn y (List.mem_cons_of_mem a hy))
        have h := add_le_add (OrdField.le_refl (f a)) htail
        simpa [add_zero] using h
      · have hft : f x ≤ lsum (t.map f) :=
          ih hxt (fun a' ha' => hnn a' (List.mem_cons_of_mem a ha'))
        have hfa : 0 ≤ f a := hnn a (by simp)
        have hstep : lsum (t.map f) ≤ f a + lsum (t.map f) := by
          have h := add_le_add hfa (OrdField.le_refl (lsum (t.map f)))
          simpa [zero_add] using h
        exact le_trans hft hstep

/-- A strictly positive sum of nonnegative terms has a strictly positive
term.  Proved by contraposition: if no term is positive, every term is `≤ 0`
and the sum is `≤ 0`. -/
theorem lsum_pos_exists {l : List X} {f : X → K}
    (hnn : ∀ a, a ∈ l → 0 ≤ f a) (hpos : 0 < lsum (l.map f)) :
    ∃ x, x ∈ l ∧ 0 < f x := by
  classical
  apply Classical.byContradiction
  intro h
  have hall : ∀ a, a ∈ l → f a ≤ 0 := by
    intro a ha
    have hnot : ¬ 0 < f a := by
      intro hp
      exact h ⟨a, ha, hp⟩
    apply Classical.byContradiction
    intro hfa
    exact hnot ⟨hnn a ha, hfa⟩
  have hsum_le : lsum (l.map f) ≤ 0 := by
    calc
      lsum (l.map f) ≤ lsum (l.map (fun _ => (0 : K))) := lsum_le_lsum l f (fun _ => 0) hall
      _ = 0 := lsum_map_zero l
  exact hpos.2 hsum_le

/-! ## The deterministic degeneration -/

/-- **Deterministic kernels.**  `T` and `g` are `0/1`-valued: the successor
is a function `next` and the observation is a function `obsAt`.  This is
`thm:support`'s hypothesis "deterministic kernels and deterministic
observation maps", made explicit. -/
structure DetKernels (M : SafeMDP K X Y A) where
  next : A → X → X
  obsAt : A → X → X → Y
  T_eq : ∀ a x x', M.T a x x' = if next a x = x' then (1 : K) else 0
  g_eq : ∀ a x x' y, M.g a x x' y = if obsAt a x x' = y then (1 : K) else 0

/-- Support as a predicate: the states carrying strictly positive mass. -/
def suppOf (m : Mass K X) : X → Prop := fun x => 0 < m.f x

/-- **`Post(B, a, y)`**: the set-valued post-state — those `x'` reached from
some `x ∈ B` whose observation is `y`.  The witness `x` is restricted to
`univX`, since the posterior sum ranges over `univX`. -/
def postMem (M : SafeMDP K X Y A) (DK : DetKernels M) (B : X → Prop)
    (a : A) (y : Y) (x' : X) : Prop :=
  ∃ x, x ∈ M.univX ∧ B x ∧ DK.next a x = x' ∧ DK.obsAt a x x' = y

/-! ## The identity -/

/-- Under deterministic kernels the posterior collapses to the sum over the
states that actually flow into `x'` with observation `y`. -/
theorem obsMass_eq_filter (M : SafeMDP K X Y A) (DK : DetKernels M)
    (a : A) (y : Y) (b : Mass K X) (x' : X) :
    obsMass M a y b x' =
      lsum ((M.univX.filter
        (fun x => decide (DK.next a x = x' ∧ DK.obsAt a x x' = y))).map b.f) := by
  unfold obsMass
  rw [← lsum_filter_ind
        (fun x => decide (DK.next a x = x' ∧ DK.obsAt a x x' = y)) b.f M.univX]
  apply lsum_congr
  intro x hx
  by_cases hA : DK.next a x = x' ∧ DK.obsAt a x x' = y
  · rcases hA with ⟨hn, ho⟩
    simp [DK.T_eq, DK.g_eq, hn, ho]
  · by_cases hn : DK.next a x = x'
    · have ho : DK.obsAt a x x' ≠ y := by
        intro hoy
        exact hA ⟨hn, hoy⟩
      simp [DK.T_eq, DK.g_eq, hn, ho]
    · simp [DK.T_eq, DK.g_eq, hn]

/-- **`thm:support`.**  A state carries posterior positive mass exactly when
it is in the set-valued post-state of the support.

    supp(b⁺(· | a, y))  =  Post(supp(b), a, y)

stated pointwise as an iff, with support read as strict positivity of mass. -/
theorem support_identity (M : SafeMDP K X Y A) (DK : DetKernels M)
    (a : A) (y : Y) (b : Mass K X) (x' : X) :
    (0 < (step M a y b).f x') ↔ postMem M DK (suppOf b) a y x' := by
  change 0 < obsMass M a y b x' ↔ postMem M DK (suppOf b) a y x'
  let p : X → Bool := fun x => decide (DK.next a x = x' ∧ DK.obsAt a x x' = y)
  rw [obsMass_eq_filter M DK a y b x']
  change 0 < lsum ((M.univX.filter p).map b.f) ↔ _
  constructor
  · intro hpos
    rcases lsum_pos_exists (l := M.univX.filter p) (f := b.f)
        (by
          intro z hz
          exact b.nonneg z) hpos with ⟨x, hx, hbx⟩
    have hxf : x ∈ M.univX := by
      exact (by simpa [p] using hx : x ∈ M.univX ∧
        (DK.next a x = x' ∧ DK.obsAt a x x' = y)).1
    have hxp : DK.next a x = x' ∧ DK.obsAt a x x' = y := by
      exact (by simpa [p] using hx : x ∈ M.univX ∧
        (DK.next a x = x' ∧ DK.obsAt a x x' = y)).2
    exact ⟨x, hxf, hbx, hxp.1, hxp.2⟩
  · rintro ⟨x, hxU, hbx, hn, ho⟩
    have hxmem : x ∈ M.univX.filter p := by
      simp [p, hxU, hn, ho]
    have hle := le_lsum_of_mem (l := M.univX.filter p) (f := b.f) hxmem
        (by intro z hz; exact b.nonneg z)
    exact ⟨le_trans hbx.1 hle, fun hz => hbx.2 (le_trans hle hz)⟩

end Formalizations.P3

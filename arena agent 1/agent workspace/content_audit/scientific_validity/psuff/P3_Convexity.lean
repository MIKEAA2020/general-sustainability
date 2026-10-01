/-
  Formalizations.P3_Convexity
  ===========================

  Closes the convexity half of `prop:pl` (P3,
  `paper2_probabilistic_sufficiency_v11.tex`):

  > Fix a declared class `Π`. At every horizon `k`, `V^Π_k` is piecewise
  > linear and **convex**: `V^Π_k(b) = max_{α ∈ Γ^Π_k} αᵀb` for a finite
  > witness set `Γ^Π_k` …

  ## Scope, and why it is drawn here

  The proposition has two halves: an *explicit* representation of `V^Π_k` as
  a max over a finite set of alpha-vectors `Γ_k` built by the masked backup,
  and the *convexity* that representation entails.  This module proves the
  second, directly, and says nothing about the first.

  The reason is worth recording.  The explicit route needs
  `Γ_{k+1} = {α^{a, γ·} : a ∈ A(Π), γ· a selection}`, and expanding
  `Σ_y max_{γ_y}` into `max_{selections} Σ_y` requires a `selections`
  construction (all functions `Y → Γ_k`, as a list), plus a max/sum
  exchange lemma and a bookkeeping argument about duplicate removal.  That
  is real combinatorics with no support in this dependency-free layer.

  Convexity, by contrast, survives the recursion without ever mentioning
  alpha-vectors, because each Bellman backup is built from operations that
  preserve convexity:

      V_0   = total                       linear, hence convex
      V_{k+1} = max_a  Σ_y V_k ∘ step(a,y)
               └ max of convex is convex
                      └ sum of convex is convex
                             └ convex ∘ linear is convex

  So `VAdm_convex` below establishes the convexity of `V^Π_k` for **every**
  declared class and every horizon, over the abstract `OrdField`.  It is
  stronger than the paper's claim in one respect — it needs no rationality
  of `T`, `g`, or the prior — and weaker in one: it does not exhibit the
  finite witness set, so it does not by itself give piecewise linearity.

  ## What is still open on `prop:pl`

  The explicit `Γ_k` construction, the masked-backup identity
  `α^{a,γ·}(x) = Σ_{x'} T(x'|x,a) Σ_y g(y|x,a,x') γ_y(x')`, the exact
  rational-witness claim, and the growth law
  `|Γ_{k+1}| ≤ |A| |Γ_k|^{|Y|}`.  These are the `selections` combinatorics
  above, and they are flagged rather than faked.
-/

import Formalizations.Prelude
import Formalizations.P1_BeliefSafety
import Formalizations.P3_Sufficiency
import Formalizations.P3_Freeze_Noisy

namespace Formalizations.P3

open Formalizations.POMDP

variable {K : Type} [OrdField K]
variable {X Y A : Type}

/-! ## Mixtures of beliefs -/

/-- The pointwise mixture of two mass functions. -/
def mixF (w : K) (m₁ m₂ : Mass K X) : X → K :=
  fun x => w * m₁.f x + (1 - w) * m₂.f x

/-- The mixture *belief*.  Nonnegativity needs `0 ≤ w ≤ 1`. -/
noncomputable def mix (w : K) (m₁ m₂ : Mass K X) (hw0 : 0 ≤ w)
    (hw1 : w ≤ 1) : Mass K X where
  f := mixF w m₁ m₂
  nonneg := by
    intro x
    have hA : 0 ≤ w * m₁.f x := mul_nonneg hw0 (m₁.nonneg x)
    have hB : 0 ≤ (1 - w) * m₂.f x := mul_nonneg (one_sub_nonneg hw1) (m₂.nonneg x)
    calc
      0 = 0 + 0 := by rw [add_zero]
      _ ≤ w * m₁.f x + (1 - w) * m₂.f x := add_le_add hA hB

/-- **Convexity** of a function on beliefs, over the abstract ordered
field: `f(wm₁ + (1−w)m₂) ≤ w f(m₁) + (1−w) f(m₂)` for `0 ≤ w ≤ 1`. -/
def Convex (f : Mass K X → K) : Prop :=
  ∀ (m₁ m₂ : Mass K X) (w : K) (hw0 : 0 ≤ w) (hw1 : w ≤ 1),
    f (mix w m₁ m₂ hw0 hw1) ≤ w * f m₁ + (1 - w) * f m₂

/-- `f` sees only the mass function, not the nonnegativity proof.  Needed
because `Mass` has no extensionality lemma in this layer, so beliefs cannot
be compared structurally; equality of `.f` is the usable substitute. -/
def SeesF (f : Mass K X → K) : Prop :=
  ∀ m₁ m₂, m₁.f = m₂.f → f m₁ = f m₂

/-! ## Linearity of the two primitives -/

/-- `total` is **linear**: `total(wm₁ + (1−w)m₂) = w·total m₁ + (1−w)·total m₂`. -/
theorem total_mix (M : SafeMDP K X Y A) (m₁ m₂ : Mass K X)
    (w : K) (hw0 : 0 ≤ w) (hw1 : w ≤ 1) :
    total M (mix w m₁ m₂ hw0 hw1) =
      w * total M m₁ + (1 - w) * total M m₂ := by
  change lsum (M.univX.map (fun x => w * m₁.f x + (1 - w) * m₂.f x)) =
    w * lsum (M.univX.map m₁.f) + (1 - w) * lsum (M.univX.map m₂.f)
  rw [lsum_distrib M.univX (fun x => w * m₁.f x) (fun x => (1 - w) * m₂.f x)]
  rw [lsum_const_mul M.univX w (fun x => m₁.f x),
      lsum_const_mul M.univX (1 - w) (fun x => m₂.f x)]

/-- The belief update is **linear**, pointwise in the state. -/
theorem step_mix_f (M : SafeMDP K X Y A) (a : A) (y : Y)
    (m₁ m₂ : Mass K X) (w : K) (hw0 : 0 ≤ w) (hw1 : w ≤ 1) (x' : X) :
    (step M a y (mix w m₁ m₂ hw0 hw1)).f x' =
      w * (step M a y m₁).f x' + (1 - w) * (step M a y m₂).f x' := by
  change lsum (M.univX.map (fun x =>
        (w * m₁.f x + (1 - w) * m₂.f x) * M.T a x x' * M.g a x x' y)) =
    w * lsum (M.univX.map (fun x => m₁.f x * M.T a x x' * M.g a x x' y)) +
      (1 - w) * lsum (M.univX.map (fun x => m₂.f x * M.T a x x' * M.g a x x' y))
  rw [lsum_congr M.univX
      (fun x => (w * m₁.f x + (1 - w) * m₂.f x) * M.T a x x' * M.g a x x' y)
      (fun x => w * (m₁.f x * M.T a x x' * M.g a x x' y) +
                (1 - w) * (m₂.f x * M.T a x x' * M.g a x x' y))
      (by
        intro x hx
        calc
          (w * m₁.f x + (1 - w) * m₂.f x) * M.T a x x' * M.g a x x' y
              = ((w * m₁.f x) * M.T a x x' +
                  ((1 - w) * m₂.f x) * M.T a x x') * M.g a x x' y := by
                  rw [right_distrib]
          _ = (w * m₁.f x) * M.T a x x' * M.g a x x' y +
                ((1 - w) * m₂.f x) * M.T a x x' * M.g a x x' y := by
                  rw [right_distrib]
          _ = w * (m₁.f x * M.T a x x' * M.g a x x' y) +
                (1 - w) * (m₂.f x * M.T a x x' * M.g a x x' y) := by
                  simp only [mul_assoc])]
  rw [lsum_distrib]
  rw [lsum_const_mul, lsum_const_mul]

/-! ## Closure properties of convexity -/

/-- A **sum** of convex functions is convex. -/
theorem convex_lsum (ys : List Y) (F : Y → Mass K X → K)
    (hF : ∀ y, y ∈ ys → Convex (F y)) :
    Convex (fun m => lsum (ys.map (fun y => F y m))) := by
  intro m₁ m₂ w hw0 hw1
  calc
    lsum (ys.map (fun y => F y (mix w m₁ m₂ hw0 hw1)))
        ≤ lsum (ys.map (fun y => w * F y m₁ + (1 - w) * F y m₂)) := by
            apply lsum_le_lsum
            intro y hy
            exact hF y hy m₁ m₂ w hw0 hw1
    _ = w * lsum (ys.map (fun y => F y m₁)) +
        (1 - w) * lsum (ys.map (fun y => F y m₂)) := by
            rw [lsum_distrib]
            rw [lsum_const_mul, lsum_const_mul]

/-- A **maximum** of finitely many convex functions is convex. -/
theorem convex_lmax {ι : Type} (l : List ι) (hne : l ≠ [])
    (F : ι → Mass K X → K) (hF : ∀ i, i ∈ l → Convex (F i)) :
    Convex (fun m => lmax (l.map (fun i => F i m))) := by
  intro m₁ m₂ w hw0 hw1
  apply lmax_le (map_ne_nil (fun i => F i (mix w m₁ m₂ hw0 hw1)) hne)
  intro z hz
  rcases List.mem_map.mp hz with ⟨i, hi, rfl⟩
  have hci := hF i hi m₁ m₂ w hw0 hw1
  have h1 : F i m₁ ≤ lmax (l.map (fun j => F j m₁)) :=
    le_lmax (map_ne_nil (fun j => F j m₁) hne) (List.mem_map.mpr ⟨i, hi, rfl⟩)
  have h2 : F i m₂ ≤ lmax (l.map (fun j => F j m₂)) :=
    le_lmax (map_ne_nil (fun j => F j m₂) hne) (List.mem_map.mpr ⟨i, hi, rfl⟩)
  have h1' : w * F i m₁ ≤ w * lmax (l.map (fun j => F j m₁)) := by
    rw [mul_comm w (F i m₁), mul_comm w (lmax (l.map (fun j => F j m₁)))]
    exact mul_le_mul_of_nonneg_right h1 hw0
  have h2' : (1 - w) * F i m₂ ≤ (1 - w) * lmax (l.map (fun j => F j m₂)) := by
    rw [mul_comm (1 - w) (F i m₂),
        mul_comm (1 - w) (lmax (l.map (fun j => F j m₂)))]
    exact mul_le_mul_of_nonneg_right h2 (one_sub_nonneg hw1)
  exact le_trans hci (add_le_add h1' h2')

/-- Convexity is preserved under precomposition with the **linear** belief
update.  `SeesF` is what lets us replace `step(mix)` by `mix(step, step)`:
the two beliefs have the same `.f`, and `f` cannot tell them apart. -/
theorem convex_step (M : SafeMDP K X Y A) (a : A) (y : Y) (f : Mass K X → K)
    (hf : Convex f) (hsf : SeesF f) :
    Convex (fun m => f (step M a y m)) := by
  intro m₁ m₂ w hw0 hw1
  have heq : (step M a y (mix w m₁ m₂ hw0 hw1)).f =
      (mix w (step M a y m₁) (step M a y m₂) hw0 hw1).f := by
    funext x'
    exact step_mix_f M a y m₁ m₂ w hw0 hw1 x'
  calc
    f (step M a y (mix w m₁ m₂ hw0 hw1))
        = f (mix w (step M a y m₁) (step M a y m₂) hw0 hw1) := hsf _ _ heq
    _ ≤ w * f (step M a y m₁) + (1 - w) * f (step M a y m₂) :=
        hf (step M a y m₁) (step M a y m₂) w hw0 hw1

/-! ## The class-restricted value is convex -/

/-- `VAdm` sees only the mass function — the `SeesF` instance supplied by
`VAdm_congr`. -/
theorem VAdm_seesF (M : SafeMDP K X Y A) (adm : A → Prop) [DecidablePred adm]
    (hne : actSet M adm ≠ []) (k : Nat) : SeesF (VAdm M adm hne k) := by
  intro m₁ m₂ h
  exact VAdm_congr M adm hne k h

/-- **`prop:pl`, convexity.**  For every declared class `Π` and every
horizon `k`, `V^Π_k` is convex in the belief. -/
theorem VAdm_convex (M : SafeMDP K X Y A) (adm : A → Prop) [DecidablePred adm]
    (hne : actSet M adm ≠ []) : ∀ k, Convex (VAdm M adm hne k) := by
  intro k
  induction k with
  | zero =>
      intro m₁ m₂ w hw0 hw1
      change total M (mix w m₁ m₂ hw0 hw1) ≤
        w * total M m₁ + (1 - w) * total M m₂
      rw [total_mix]
      exact le_refl _
  | succ k ih =>
      exact convex_lmax (actSet M adm) hne
        (fun a m => lsum (M.univY.map (fun y => VAdm M adm hne k (step M a y m))))
        (by
          intro a ha
          exact convex_lsum M.univY
            (fun y m => VAdm M adm hne k (step M a y m))
            (by
              intro y hy
              exact convex_step M a y (VAdm M adm hne k) ih
                (VAdm_seesF M adm hne k)))

end Formalizations.P3

/-
  Formalizations.P3_RobustPL
  ==========================

  **The disturbance question is settled by the paper, and I had it wrong.**

  v23 reported that `prop:pl` and `thm:support` were blocked on a
  "disturbance-weighting modelling decision" that `DetMDP` does not carry.
  That was a misreading, and the paper answers it in as many words.

  ## What the paper says

  `rem:operators` (v11, "the two operators"):

  > The expectation over the disturbance law and the adversarial reading of
  > its support are *different Bellman operators*. Proposition `prop:degen`
  > states the deterministic degeneration as a change of operator: when the
  > kernels are deterministic the stochastic expectation is replaced by the
  > robust (adversarial-support) reading … The degeneration is a theorem
  > about the robust operator; it is not a claim about the stochastic plant,
  > whose expectation and robust readings differ in general.

  `prop:degen` (survived-mass formula):

  > Let the kernels be deterministic, `x⁺ = F(x,a,d)`, and let
  > **the disturbance be read adversarially within its support** … a branch
  > survives a declared sequence exactly when it survives under **every**
  > disturbance in its support.

  So the adversarial reading is not a weakening of the paper and not a
  reinterpretation of it: **for the deterministic layer, it is the operator
  the paper prescribes.** Wishing for a weighting `w` on `univD x a` in order
  to instantiate the *stochastic* masked backup here would be to formalize the
  wrong operator — precisely the conflation `rem:operators` warns against.

  ## And the adversarial reading is already in the code

  `P3_Deterministic.survT` is exactly it:

      survT M []       x := safe x
      survT M (a :: t) x := safe x && (univD x a).all (fun d => survT M t (F x a d))

  — "every disturbance path stays in 𝒱", an `all` over `univD`. The doc
  comment there already says so. And `VR` is already `prop:degen`'s
  survived-mass formula, `max_{t ∈ Π_B} Σ_x b(x)·1[x survives t]`.

  So **no new structure is needed**. What was missing was connecting this to
  `prop:pl`'s alpha-vector language, which is what this module does.

  ## What `prop:pl` says, and what is formalized

  `prop:pl` gives two forms. The general masked backup
  `α^{a,γ·}(x) = Σ_{x'} T(x'|x,a) Σ_y g(y|x,a,x') γ_y(x')` is a statement
  about the **stochastic** operator and is *out of scope for the deterministic
  P3 layer by design* — not by omission. Its segment form is the one that
  applies here:

  > For a blind open-loop window the equivalent segment form applies: each
  > admissible action segment `(u_0,…,u_m) ∈ Π` contributes the witness
  > `α^seg = (1[the segment saves branch x])_x` and
  > `V^Π_k(b) = max_seg α^segᵀ b`.

  That is `prop:degen`'s survived-mass formula in alpha-vector notation, and
  it is `VR`. This module proves the identification.

  ## Contents

    alphaSeg, GammaSeg            the segment witnesses and witness family
    survT_adversarial            the adversarial reading, made explicit
    smass_eq_dotOn               `b`-mass survived = `α^segᵀ b`
    VR_eq_max_alpha              **prop:pl segment form**
    GammaSeg_ne                  the witness family is inhabited
    tuplesAux_length, tuples_length
    GammaSeg_length              `|Γ_k| = |A|^k`
    GammaSeg_succ_length         **the growth law in the blind window**
-/

import Formalizations.Prelude
import Formalizations.P3_Deterministic
import Formalizations.P3_Antichain
import Formalizations.P3_PiecewiseLinear

namespace Formalizations.P3

open Formalizations
open Formalizations.POMDP

set_option linter.unusedSectionVars false

variable {K : Type} [OrdField K]
variable {X A D Y : Type}

/-! ## The segment witnesses -/

/-- **`α^seg`**: the survival indicator of the branch under the declared
sequence `t`. These are the "degenerate alpha-vectors" of `prop:degen` —
`{0,1}`-valued, since the adversarial survival event is deterministic. -/
def alphaSeg (M : DetMDP K X A D Y) (t : List A) : X → K := ind (survT M t)

/-- The witness family at horizon `k`: one witness per declared sequence. -/
def GammaSeg (M : DetMDP K X A D Y) (k : Nat) : List (X → K) :=
  (tuples M k).map (fun t => alphaSeg M t)

/-- The adversarial reading, stated explicitly.  A branch survives an
action sequence exactly when **every** disturbance path stays safe — the
"under every disturbance in its support" of `prop:degen`. -/
theorem survT_adversarial (M : DetMDP K X A D Y) (a : A) (t : List A) (x : X) :
    survT M (a :: t) x = true ↔
      M.safe x = true ∧ ∀ d, d ∈ M.univD x a → survT M t (M.F x a d) = true := by
  simp [survT]

/-! ## `prop:pl`, segment form -/

/-- Survived mass is the alpha-pairing `α^segᵀ b`.  The two differ only by
commutativity of multiplication. -/
theorem smass_eq_dotOn (M : DetMDP K X A D Y) (t : List A) (b : Mass K X) :
    smass M t b = dotOn M.univX (alphaSeg M t) b := by
  unfold smass dotOn alphaSeg
  apply lsum_congr
  intro x hx
  exact mul_comm (b.f x) (ind (survT M t) x)

theorem map_congr_fun {β : Type} {l : List A} {f g : A → β}
    (h : ∀ a, a ∈ l → f a = g a) : l.map f = l.map g := by
  induction l with
  | nil => simp
  | cons a t ih =>
      have h1 : f a = g a := h a List.mem_cons_self
      have h2 : t.map f = t.map g := ih (fun a' ha' => h a' (List.mem_cons_of_mem a ha'))
      simp [h1, h2]

/-- **`prop:pl`, segment form** (deterministic layer):
`V_k(b) = max_{α ∈ Γ_k} αᵀ b`, with `Γ_k` the segment witnesses. -/
theorem VR_eq_max_alpha (M : DetMDP K X A D Y) (k : Nat) (b : Mass K X) :
    VR M k b = lmax ((GammaSeg M k).map (fun α => dotOn M.univX α b)) := by
  unfold VR GammaSeg
  rw [List.map_map]
  apply congrArg lmax
  apply map_congr_fun
  intro t ht
  exact smass_eq_dotOn M t b

/-- The witness family is inhabited, so the maximum is well defined. -/
theorem GammaSeg_ne (M : DetMDP K X A D Y) (k : Nat) : GammaSeg M k ≠ [] :=
  map_ne_nil (fun t => alphaSeg M t) (tuples_ne M k)

/-! ## Growth in the blind window -/

theorem tuplesAux_length (M : DetMDP K X A D Y) : ∀ l : List (List A),
    (tuplesAux M l).length = l.length * M.univA.length := by
  intro l
  induction l with
  | nil => simp [tuplesAux]
  | cons t ts ih =>
      simp [tuplesAux, ih, Nat.succ_mul, Nat.add_comm]

theorem tuples_length (M : DetMDP K X A D Y) : ∀ k,
    (tuples M k).length = M.univA.length ^ k := by
  intro k
  induction k with
  | zero => simp [tuples]
  | succ k ih =>
      simp [tuples, tuplesAux_length M (tuples M k), ih, Nat.pow_succ, Nat.mul_comm]

/-- `|Γ_k| = |A|^k` before deduplication. -/
theorem GammaSeg_length (M : DetMDP K X A D Y) (k : Nat) :
    (GammaSeg M k).length = M.univA.length ^ k := by
  unfold GammaSeg
  simp [tuples_length M k]

/-- **The growth law specialized to the blind window**:
`|Γ_{k+1}| ≤ |A| · |Γ_k|`.

This is the `|Y| = 1` case of the general law `|Γ_{k+1}| ≤ |A|·|Γ_k|^{|Y|}`
of `P3_PiecewiseLinear`, which is the right specialization here: a blind
open-loop window receives no observations, so the selection index is trivial.
Note it holds with equality before deduplication. -/
theorem GammaSeg_succ_length (M : DetMDP K X A D Y) (k : Nat) :
    (GammaSeg M (k + 1)).length ≤ M.univA.length * (GammaSeg M k).length := by
  rw [GammaSeg_length M (k + 1), GammaSeg_length M k, Nat.pow_succ]
  simp [Nat.mul_comm]

end Formalizations.P3

/-
  Formalizations.P1_TimingCertificate
  ===================================

  Lean formalization of the reachable core of

    **Theorem `thm:lp-instant`** (linear-programming instantiation of the
    timing certificate), `paper2_obstruction_calculus_v55_Automatica_routes.tex`
    §8, claims (i) [monotonicity ingredient], (ii) and (iv).

  Why only part of it
  -------------------
  `thm:lp-instant` has four claims. They are not equally formalizable at
  this layer's interface:

    (i)  "computed by at most ⌈log₂ K⌉ + 1 LPs of size polynomial in K, |J|
         and the description lengths" — a *complexity* claim about an
         algorithm's cost. Formalizing it needs a machine model and
         polynomial-size bookkeeping that this dependency-free layer does
         not have. What is formalized here is the mathematical ingredient
         the bisection rests on: **feasibility is monotone in the horizon**,
         so the exact threshold can be found by bisection.
    (ii) "infeasibility is certified by Farkas multipliers" — fully
         formalized below (`blind_window_farkas_certifies`).
    (iii)"the feasible set is the declared class itself, so no relaxation
         gap arises" — definitional at this level of abstraction: the
         program's variables *are* the declared controls. Recorded as a
         comment, not a theorem, because there is nothing to prove.
    (iv) "the declaration is load-bearing … the relaxation remains sound
         but can be arbitrarily incomplete" — the *soundness* half is
         formalized (`relaxation_sound`). The *incompleteness* half is an
         existential claim about specific data (`ex:relax-gap`:
         z⁺ = (9/10)z ± u, floor z ≥ 1), which is instance-level and is
         certified by the deposited Python batteries, not by this layer.

  Everything here is interface-level over `OrdField K`: it holds in any
  model of the ordered-field interface. No topology, no completeness, no
  derivatives are used — which is precisely why the continuous-time
  statements of `thm:exit` and `thm:delayed` are *not* touched here (see
  the module header of `Formalizations.P1_Obstruction`).
-/

import Formalizations.Prelude

namespace Formalizations.P1Timing

variable {K : Type} [OrdField K]

/-! ## The blind-window program

Unrolling the affine dynamics of `thm:lp-instant` makes each robust floor
row one linear inequality in the control sequence `x`, the disturbance
entering only through precomputed support constants. So the horizon-`n`
program is: find `x` with `dotp (a i) x ≤ b i` for all `i < n`, and `x`
in the declared class `Pi`. -/

/-- Satisfaction of the first `n` rows of the unrolled program. -/
def Satisfies (a : Nat → List K) (b : Nat → K) (n : Nat) (x : List K) : Prop :=
  ∀ i, i < n → dotp (a i) x ≤ b i

/-- Membership in a declared blind-window class (e.g. hold-until-`T_obs`
controls, piecewise-constant controls on a partition, or the finite
implementable class of `ex:relax-gap`). -/
def Declared (Pi : List K → Prop) (a : Nat → List K) (b : Nat → K) (n : Nat)
    (x : List K) : Prop :=
  Pi x ∧ Satisfies a b n x

/-! ## Claim (i): monotonicity of feasibility in the horizon

Feasibility of a prefix is necessary for feasibility of the whole, so
infeasibility propagates forward in the horizon. This is the fact that
licenses bisection for `σ*`. -/

theorem satisfies_prefix (a : Nat → List K) (b : Nat → K) {n₁ n₂ : Nat}
    (hn : n₁ ≤ n₂) {x : List K} (h : Satisfies a b n₂ x) :
    Satisfies a b n₁ x := by
  intro i hi
  exact h i (Nat.lt_of_lt_of_le hi hn)

/-- If the horizon-`n₁` program is infeasible, so is every longer horizon.
Hence `{n : infeasible at n}` is an up-set and the threshold `σ*` is found
by bisection. -/
theorem infeasible_mono_horizon (a : Nat → List K) (b : Nat → K) (Pi : List K → Prop)
    {n₁ n₂ : Nat} (hn : n₁ ≤ n₂)
    (hbad : ¬ ∃ x, Declared Pi a b n₁ x) :
    ¬ ∃ x, Declared Pi a b n₂ x := by
  rintro ⟨x, hx⟩
  exact hbad ⟨x, ⟨hx.1, satisfies_prefix a b hn hx.2⟩⟩

/-! ## Claim (ii): the timing certificate in adjoint-row form

Farkas multipliers: nonnegative weights on the rows whose aggregate control
projection vanishes and whose aggregate constant is negative. This is
`Formalizations.farkas_sound` instantiated, and the point worth stating
explicitly is that the certificate is **declaration-independent**: it rules
out *every* control sequence of the right length, so it certifies
infeasibility for any declared subclass `Pi` whatsoever. -/

theorem blind_window_farkas_certifies
    (a : Nat → List K) (b lam : Nat → K) (n L : Nat) (Pi : List K → Prop)
    (hlen : ∀ i, i < n → (a i).length = L)
    (hnonneg : ∀ i, i < n → 0 ≤ lam i)
    (hzero : linComb (List.replicate L 0) lam a n = List.replicate L 0)
    (hneg : sumRange (fun i => lam i * b i) n < 0) :
    ¬ ∃ x, Declared Pi a b n x ∧ x.length = L := by
  rintro ⟨x, hdecl, hxlen⟩
  exact farkas_sound a b lam x n
    (fun i hi => by rw [hlen i hi, hxlen])
    hnonneg
    (by simpa [hxlen] using hzero)
    hneg
    hdecl.2

/-- Declaration-independent form: a Farkas certificate kills the whole
affine system, hence every declared subclass of it. -/
theorem farkas_certifies_affine_system
    (a : Nat → List K) (b lam : Nat → K) (n L : Nat)
    (hlen : ∀ i, i < n → (a i).length = L)
    (hnonneg : ∀ i, i < n → 0 ≤ lam i)
    (hzero : linComb (List.replicate L 0) lam a n = List.replicate L 0)
    (hneg : sumRange (fun i => lam i * b i) n < 0) :
    ¬ ∃ x, x.length = L ∧ Satisfies a b n x := by
  rintro ⟨x, hxlen, hsat⟩
  exact farkas_sound a b lam x n
    (fun i hi => by rw [hlen i hi, hxlen])
    hnonneg (by simpa [hxlen] using hzero) hneg hsat

/-! ## Claim (iv): the relaxation is sound

Enlarging the declared class can only help the controller, so a
certificate established over the *larger* class is sound for the smaller
one. (The complementary fact — that it can be arbitrarily *incomplete* —
is the instance-level `ex:relax-gap`, certified by the Python batteries:
over `U = [-1,1]` the control `u ≡ 0` holds both branches on the floor
forever, so `σ*_rel = ∞` and the relaxed certificate never fires, while
the finite class `{-1,+1}` gives `σ* = z₀ - 1`.) -/

/-- `Pi` is a subclass of `Pi'`. -/
def Subclass (Pi Pi' : List K → Prop) : Prop := ∀ x, Pi x → Pi' x

theorem relaxation_sound (a : Nat → List K) (b : Nat → K) {Pi Pi' : List K → Prop}
    (n : Nat) (hsub : Subclass Pi Pi')
    (hbad : ¬ ∃ x, Declared Pi' a b n x) :
    ¬ ∃ x, Declared Pi a b n x := by
  rintro ⟨x, hx⟩
  exact hbad ⟨x, ⟨hsub x hx.1, hx.2⟩⟩

/-! ### Note on "combining (ii) and (iv)"

A tempting extra theorem is "a Farkas certificate over the *relaxed*
program certifies the *declared* program". That theorem was drafted here
and removed: because the Farkas certificate is declaration-independent
(it kills the whole affine system, see
`farkas_certifies_affine_system` above), the subclass hypothesis is never
consumed. The statement is therefore vacuous as a combination — it is
`blind_window_farkas_certifies` with an unused premise, the same defect
this audit exists to remove. The genuinely distinct facts are recorded
separately: Farkas soundness (declaration-independent) and relaxation
soundness (about subclasses). -/

end Formalizations.P1Timing

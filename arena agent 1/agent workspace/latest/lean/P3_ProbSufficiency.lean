/-
  Formalizations.P3_ProbSufficiency
  =================================

  Lean formalization of the theorem layer of

    "Probabilistic Sufficiency" (2026e; source of record:
    `paper2_probabilistic_sufficiency_v8.tex`).

  Scope and fidelity.  The paper develops the belief-state value recursion
  for class-restricted survival probabilities, the support identity
  connecting probabilistic beliefs to the obstruction calculus's set-valued
  post-states, and the certificate-value agreement.  Formalized here:

    * the expectation-kernel operator of the value recursion
      (Theorem `thm:recursion`): pointwise monotonicity, preservation of
      constants, monotone iterates, and the pointwise-ceiling lemma —
      the algebraic laws that make backward induction exact and the
      recursion's comparisons valid on every finite horizon;
    * the certificate-agreement direction (Theorem `thm:agree`'s
      algebraic core): if every conditional continuation value is at most
      a ceiling, the expected value is at most the ceiling — the
      expectation never exceeds its pointwise ceiling.

  Not formalized (and why): the belief-update/posterior machinery and the
  support identity `supp(b⁺) = Post(supp b, a, y)` (deterministic-kernel
  conditioning, needed in its full form); the closed forms and
  alpha-vector rationality (exact enumerations over the instance,
  certified by the record's 30/30 check families); the loss lower bound
  `1 - V_k ≥ min_x b(x)` (needs the realized-path loss construction).
-/

import Formalizations.Prelude

namespace Formalizations.P3

/-! ## The expectation-kernel operator of the value recursion -/

section Kernel
variable {K : Type} [OrdField K] {B Y : Type}

/-- The one-step expectation kernel of the belief-state value recursion:
`(Φ V) b` is the prior-averaged next-belief value over the observation
distribution `obsDist b` with posterior map `post b`.

Paper reference: Theorem `thm:recursion` (belief-state value recursion),
the operator. -/
def Φ (obsDist : B → FinMass K Y) (post : B → Y → B) (V : B → K)
    (b : B) : K :=
  (obsDist b).E (fun y => V (post b y))

/-- Pointwise monotonicity of the kernel: value domination propagates
through the recursion.

Paper reference: Theorem `thm:recursion`, the monotone-operator property
(the same induction that makes backward induction exact). -/
theorem Φ_mono (obsDist : B → FinMass K Y) (post : B → Y → B)
    {V W : B → K} (h : ∀ b, V b ≤ W b) (b : B) :
    Φ obsDist post V b ≤ Φ obsDist post W b :=
  FinMass.E_le_E _ _ _ (fun y _ => h (post b y))

/-- Constants are preserved: the expected value of a constant belief
value is the constant.

Paper reference: Theorem `thm:recursion`, the base-clause alignment
`V₀(b) = b(𝒱)` read at constant value functions. -/
theorem Φ_const (obsDist : B → FinMass K Y) (post : B → Y → B)
    (c : K) (b : B) :
    Φ obsDist post (fun _ => c) b = c :=
  FinMass.E_const _ c

/-- The pointwise-ceiling lemma: if every posterior continuation value is
at most `c`, the expected value is at most `c` — the certificate-value
agreement's algebraic core.

Paper reference: Theorem `thm:agree` (certificate-value agreement), the
ceiling direction. -/
theorem Φ_le_const (obsDist : B → FinMass K Y) (post : B → Y → B)
    {V : B → K} {c : K} (b : B) (h : ∀ y, V (post b y) ≤ c) :
    Φ obsDist post V b ≤ c := by
  have h1 : (obsDist b).E (fun y => V (post b y))
      ≤ (obsDist b).E (fun _ => c) :=
    FinMass.E_le_E _ _ _ (fun y _ => h y)
  rw [FinMass.E_const] at h1
  exact h1

/-- The iterates of the kernel: the `N`-step backward recursion. -/
def iterΦ (obsDist : B → FinMass K Y) (post : B → Y → B) :
    Nat → (B → K) → (B → K)
  | 0, V => V
  | N + 1, V => Φ obsDist post (iterΦ obsDist post N V)

/-- Monotone iterates: seed domination propagates to every horizon.

Paper reference: Theorem `thm:recursion`, the exactness of backward
induction (order-preservation at every horizon). -/
theorem iterΦ_mono (obsDist : B → FinMass K Y) (post : B → Y → B)
    {V W : B → K} (h : ∀ b, V b ≤ W b) :
    ∀ N b, iterΦ obsDist post N V b ≤ iterΦ obsDist post N W b := by
  intro N
  induction N with
  | zero => intro b; exact h b
  | succ m ih =>
      intro b
      exact Φ_mono obsDist post (fun b' => ih b') b

end Kernel

end Formalizations.P3

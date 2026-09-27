/-
  Formalizations.Comp_Certification_v2
  =====================================

  **Relabels** the four scaffolding theorems of `Comp_Certification`, the
  finding recorded in `lean_audit_v14.md` under failure mode **D**
  (conclusion-as-hypothesis) and carried into `lean_README_v3.md`.

  ## The input contract (what this module makes explicit)

  `Comp_Certification`'s four small theorems are not false and not useless.
  They are **verdict procedures**: given a sandwich and a characterization,
  they read off the certification verdict.  What they do not do — and what
  v1's index implied they did — is *establish* the sandwich or the
  characterization.  Both are **inputs**, produced elsewhere:

  | Input | Meaning | Produced by |
  |---|---|---|
  | `hlo : ρ ≤ J` | the certificate's lower bound is a true lower bound | the certificate computation |
  | `hhi : J ≤ ρ + ē` | the inflated upper bound is a true upper bound | the certificate computation |
  | `hchar : ((∃ π, ∀ a, F a π ≤ 0) ↔ J ≤ 0)` | the value characterizes the existential | `prop:value` |

  The third row is the one that matters.  `prop:value` reads: "The minimum
  exists: the policy-signal space is a finite product of weak-* compact sets
  `L^∞(I_r; U)` … and each `F_a` is weak-* continuous … **Consequently**
  `B_0 ∉ K_I^T` if and only if `J_I(T) > 0`."  The entire difficulty of
  `prop:value` is the existence of that minimum, and the paper grounds it in
  **weak-* compactness and weak-* continuity** — analysis that is out of
  reach of this layer, which is interface-level over `OrdField K` and has no
  topology at all.

  That is a legitimate reason not to formalize `prop:value`.  It is *not* a
  licence to take its conclusion as a hypothesis and present the result as
  formalized, which is what the old indexing did.

  ## What this module contains

  The same four facts, under names that name the contract, each with a
  header stating that the sandwich / characterization is an **input**.  No
  proof is duplicated: every theorem here is a one-line delegation to the
  corresponding theorem in `Comp_Certification`.  The v1 declarations are
  left in place — this project never overwrites — and should now be read as
  the same procedures under names that did not advertise their contract.
-/

import Formalizations.Prelude
import Formalizations.Comp_Certification

namespace Formalizations.CompCert

section Sandwich
variable {K : Type} [OrdField K] {ρ ē J : K}

/-- **Verdict, lower side.**  *Input*: `hlo : ρ ≤ J`, the certificate's
lower bound, supplied by the certificate computation.

If the certified lower bound is strictly positive, the value is strictly
positive — no policy can certify safety.  Delegates to
`positive_bound_obstruction`. -/
theorem sandwich_verdict_lower (hlo : ρ ≤ J) (hpos : 0 < ρ) : 0 < J :=
  positive_bound_obstruction hlo hpos

/-- **Verdict, upper side.**  *Input*: `hhi : J ≤ ρ + ē`, the inflated upper
bound, supplied by the certificate computation.

If the inflated upper bound is strictly negative, the value is strictly
negative.  Delegates to `inflated_upper_bound_negative`. -/
theorem sandwich_verdict_upper (hhi : J ≤ ρ + ē) (hmargin : ρ + ē < 0) :
    J < 0 :=
  inflated_upper_bound_negative hhi hmargin

/-- **The verdict procedure.**  *Inputs*: both sides of the sandwich,
`hlo : ρ ≤ J` and `hhi : J ≤ ρ + ē`, supplied by the certificate
computation.

**This theorem does not establish that the computed `ρ` and `ē` bracket
`J`.**  It states what follows *once* they do: a positive certified lower
bound forces `J > 0`, and a negative inflated upper bound forces `J < 0`.
Establishing the bracket is the certificate computation's job, and it is not
formalized in this layer.  Delegates to `certified_sandwich`. -/
theorem sandwich_verdict (hlo : ρ ≤ J) (hhi : J ≤ ρ + ē) :
    (0 < ρ → 0 < J) ∧ (ρ + ē < 0 → J < 0) :=
  certified_sandwich hlo hhi

end Sandwich

section Verdict
variable {K : Type} [OrdField K] {A : Type} {J ρ : K}

/-- **The obstruction verdict.**  *Inputs*: the characterization
`hchar : ((∃ π, ∀ a, F a π ≤ 0) ↔ J ≤ 0)`, the lower bound `hlo : ρ ≤ J`,
and its strict positivity `hpos : 0 < ρ`.

**The characterization is an input, not a result of this layer.**  It is the
"consequently" clause of `prop:value`, whose real content — existence of the
minimum, from weak-* compactness of `L^∞(I_r; U)` and weak-* continuity of
each `F_a` — lies beyond `OrdField`.  Given it, together with a strictly
positive certified lower bound, no admissible policy exists.

Note also that this is one direction only: it concludes
`¬ ∃ π, ∀ a, F a π ≤ 0`.  The paper's `prop:value` is an iff; the converse
is not formalized here.  Delegates to `margin_obstruction_verdict`. -/
theorem characterization_verdict (F : A → A → K)
    (hchar : ((∃ π, ∀ a, F a π ≤ 0) ↔ J ≤ 0))
    (hlo : ρ ≤ J) (hpos : 0 < ρ) :
    ¬ ∃ π, ∀ a, F a π ≤ 0 :=
  margin_obstruction_verdict F hchar hlo hpos

end Verdict

end Formalizations.CompCert

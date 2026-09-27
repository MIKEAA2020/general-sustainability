/-
  Formalizations.Prelude_Monotone
  ===============================

  **The one declaration of `E1_ForecastLadder` that has any content**,
  moved here under an honest name.

  `E1_ForecastLadder` (93 lines, 5 theorems) was indexed against
  `paperE1_cod_forecast_ladder_v59.tex`, which contains **zero numbered
  environments**; v14 recorded that as failure mode C (vacuous target).
  v35 went further and checked the module's paper references against the
  paper's text, and they do not survive it: the paper's "ladder" is a
  forward-ordered sequence of *surplus-production models* scored on NAFO
  2J3KL cod data, and `grep` finds no "telescope", no "level margin" and
  no "forward margin" anywhere in it. The "calibrated ladder" whose
  margins the docstrings say telescope to the total change does not
  exist. See `lean_audit_v35_e1_decision.md`.

  Of the five theorems:

  | theorem | body |
  |---|---|
  | `ladder_telescope`   | one-line alias of `sumRange_telescope` |
  | `ladder_bound_upper` | one-line alias of `sumRange_le_sumRange'` |
  | `ladder_bound_lower` | one-line alias of `sumRange_le_sumRange'` |
  | `ladder_bracket`     | the conjunction of the previous two |
  | `ladder_ascent`      | **the only one with a proof** |

  The four aliases say nothing `Prelude` did not already say. They are
  left in place — this layer does not delete, and they build green — and
  are relabelled in the index. The fifth is genuine: a sequence whose
  steps never descend never descends.

  It is **not** a fact about sums, which is why it is not named
  `sumRange_*` and why it sits in a module of its own rather than beside
  the `sumRange` lemmas it used to sit next to.
-/

import Formalizations.Prelude

namespace Formalizations

variable {K : Type} [OrdField K]

/-- **Ascent law.** If every step of a sequence is nonnegative, the
initial level never exceeds the level at any horizon: a sequence whose
steps never descend never descends.

Relocated from `E1_ForecastLadder.ladder_ascent` (v35), whose stated
"paper reference" — the calibrated-margin monotonicity of the paper's
forecast ladder — does not exist in the paper it cited. Name, placement
and docstring changed; statement and proof unchanged. -/
theorem monotone_step_ascent (f : Nat → K) (hstep : ∀ i, f i ≤ f (i + 1)) :
    ∀ N, f 0 ≤ f N := by
  intro N
  induction N with
  | zero => exact le_refl (f 0)
  | succ m ih => exact le_trans ih (hstep m)

end Formalizations

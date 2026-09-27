/-!
Playground checks — `general-sustainability` Lean layer (v1)

Paste any section into https://live.lean-lang.org/ — each is self-contained
(the real layer has no Mathlib, so these need no imports at all).

Context: `lake build` is GREEN at both the pinned toolchain (v4.34.1, 14s)
and the newest (v4.35.0-rc3, 15s). The kernel therefore guarantees no theorem
here is *unsound*. What it cannot catch is a theorem that is vacuous:
true, but carrying none of the content its docstring claims.
These snippets reproduce that class of defect in miniature.
-/

/-! ### Check 1 — `lemB_reject` is `And.left`

Source: `Formalizations/P1_AssessmentSeparation.lean:1983`, whose docstring
claims "Lemma B(i): θ < 1 members' admissibility forces the positivity rider".

The real declaration is

    theorem lemB_reject {_pw} {w1 w2} {a} {z} {rung : Prop}
        (h : CollapseSafe a z ∧ rung) : CollapseSafe a z := h.1

which is `And.left`, for an arbitrary phantom `rung`. It is never referenced
anywhere in the layer. -/

theorem lemB_reject_shape {A rung : Prop} (h : A ∧ rung) : A := h.1

-- It fires for *every* A and every rung, including absurd ones:
example : True ∧ False → True := lemB_reject_shape
example (P : Prop) : P ∧ (0 = 1) → P := lemB_reject_shape

-- So it cannot be "forcing" anything: it merely projects its own premise.
#check lemB_reject_shape
-- lemB_reject_shape {A rung : Prop} (h : A ∧ rung) : A


/-! ### Check 2 — `lemB_ii_only_linear` is true by *definition*, not by proof

Source: `Formalizations/P1_AssessmentSeparation.lean:3561`, docstring:
"Every θ < 1 member rejects the collapsed plan of Lemma B(ii)".

Because `CollapseSafe` is conjuncted INTO both θ<1 admissibility
definitions, the result is immediate — it records a definitional choice
rather than proving anything about θ. -/

def CollapseSafe' : Prop := True          -- stand-in for the real predicate
def ThetaSubAdm' : Prop := CollapseSafe' ∧ True   -- = CollapseSafe' ∧ RungCondNeg
def ThetaMidAdm' : Prop := CollapseSafe' ∧ True   -- = CollapseSafe' ∧ RungCond

theorem only_linear_shape (h : ThetaSubAdm' ∨ ThetaMidAdm')
    (hcs : ¬ CollapseSafe') : False := by
  cases h with
  | inl hsub => exact hcs hsub.1     -- hsub.1 *is* CollapseSafe'
  | inr hmid => exact hcs hmid.1     -- hmid.1 *is* CollapseSafe'

-- Note the argument never inspects the rung conditions (the `.2` projections).
-- Deleting the rung conjuncts entirely would leave the proof unchanged.


/-! ### Check 3 — the contrast: a lemma that is NOT vacuous

`s2_two_sided_summary` (line 3574) is the headline Theorem S2, and it is
genuinely assembled from real work — the harmonic witness, the `∀m`
false-certification family, and the Leontief rejection:

    s2_i_linear_accepts, s2_leontief_rejects_gaps, s2_ii_negm_interval

Likewise `lemB_ii_linear_witness` (line 3521) really constructs the state
z₀ = (1/2, 1/2, 5/2), exhibits the collapsed coordinate, proves the θ = 1
member still certifies at the equal weight, and derives ¬CollapseSafe from
an explicit tube dip. So Lemma B(ii)'s substance IS formalized — it just
lives in `lemB_ii_linear_witness`, not in the two theorems above.

Minimal shape of that honest pattern. The real proof is arithmetic over
`OrdField K`, so it cannot be reproduced without the layer's Prelude; the
core-only analogue below captures the structural point — an honest lemma
*constructs* a witness (and discharges a companion negative), whereas the
two flagged theorems merely *project* a premise:
-/

inductive Plan where | fast | slow
deriving DecidableEq

def CollapseSafeW (a : Plan) : Prop := a = Plan.slow

-- An honest witness: exhibit the certifying plan AND refute collapse
-- for a different one. Both halves do real work.
theorem witness_pattern :
    (∃ a : Plan, CollapseSafeW a) ∧ (∃ a : Plan, ¬ CollapseSafeW a) := by
  exact ⟨⟨Plan.slow, rfl⟩, ⟨Plan.fast, by intro h; cases h⟩⟩

-- Contrast: if the property is conjuncted into the definition, the
-- "theorem" degenerates to `.1` regardless of the remaining content.
def Theta1AdmW (a : Plan) : Prop := CollapseSafeW a ∧ True
theorem degenerate_pattern (a : Plan) (h : Theta1AdmW a) : CollapseSafeW a := h.1


/-! ### Verdict

No unsoundness, no `sorry`, no extra axioms, no compile error on either
toolchain. The defects found are fidelity defects: two declared theorems
that advertise Lemma B content but are information-free. `lake build`
cannot detect these — only reading the declarations can.
-/

/-
  Formalizations.P1_AssessmentSeparation_v2
  =========================================

  Additive v2 module for the head paper's formalization
  (`paper1_assessment_separation_v62.tex`).

  WHY THIS FILE EXISTS
  --------------------
  Two declarations in `Formalizations.P1_AssessmentSeparation` advertise
  Lemma B content that they do not carry:

    * `lemB_reject`         (line 1983) is literally `And.left`, with a
                            phantom `{rung : Prop}` parameter.

    * `lemB_ii_only_linear` (line 3561) is `hsub.1` / `hmid.1`: true only
                            because `CollapseSafe` is conjuncted INTO the
                            definitions of `ThetaSubAdm` and `ThetaMidAdm`.
                            Deleting either rung condition leaves the proof
                            unchanged.

  The question was whether `lemB_ii_only_linear` could be STRENGTHENED so
  that the rung conditions do real work. It cannot, and the reason is
  substantive rather than incidental:

    1. `pw` is never constrained at negative arguments. Every law the layer
       assumes of it is guarded by nonnegativity —
       `hnn : ∀ x, 0 ≤ x → 0 ≤ pw x`, `hlaw : ∀ x, 0 ≤ x → pw x * pw x = x`,
       `hmono`, `hanti`. But `CollapseSafe` is precisely a claim about
       possibly-negative tube values (`0 < 1 + p.sᵢ`).

    2. The rung condition is a SINGLE aggregate inequality
       (`1 ≤ w₁·pw(λ₁) + w₂·pw(λ₂)`), whereas `CollapseSafe` demands BOTH
       `0 < λ₁` AND `0 < λ₂`. One large coordinate compensates the other, so
       the aggregate cannot force both.

    3. The layer already contains an explicit countermodel: at
       z₀ = (1/2, 1/2, 5/2) the plan FAST has tube values λ₁ = −1/2 and
       λ₂ = 7/2, so at equal weights λ₁/2 + λ₂/2 = 3/2 ≥ 1 — the rung
       condition is satisfied even though a coordinate has collapsed.

  So `CollapseSafe` is a genuine INDEPENDENT stipulation of the θ < 1
  family, not a consequence of the rung algebra. Conjuncting it into
  `ThetaSubAdm` / `ThetaMidAdm` is therefore the correct modelling choice —
  but it should be recorded as a theorem about non-redundancy, not smuggled
  in behind a theorem whose proof is `.1`.

  WHAT THIS FILE ADDS
  -------------------
  `collapse_convention_not_implied_v2`: the rung condition does not imply
  the collapse convention, witnessed by the Lemma B(ii) datum. This is
  genuine content — it justifies the definitional conjunct, and it would
  fail if anyone later "simplified" `ThetaSubAdm` by dropping
  `CollapseSafe` on the assumption that the rung algebra already covers it.

  Nothing here overwrites or removes anything; v1 is untouched.
  To wire in: add `import Formalizations.P1_AssessmentSeparation_v2`
  to `lean/Formalizations.lean`.
-/

import Formalizations.P1_AssessmentSeparation

namespace Formalizations.P1Sep

variable {K : Type} [OrdField K]

/-- **The collapse convention is not implied by the rung condition.**

At the Lemma B(ii) datum `z₀ = (1/2, 1/2, 5/2)`, the θ = 1 rung accepts
the plan FAST at the equal weight, while one tube coordinate has collapsed
(`1 + s₁ = −1/2 ≤ 0`), i.e. `CollapseSafe` fails.

This is the substantive replacement for the vacuous pair
`lemB_reject` / `lemB_ii_only_linear`: instead of a projection whose
conclusion is already a conjunct of its premise, it records *why* the
conjunct has to be there. Built directly on `lemB_ii_linear_witness`,
which does the real work. -/
theorem collapse_convention_not_implied_v2 (K : Type) [OrdField K] :
    ∃ (a : WitAct K) (z : WitState K),
        Theta1Adm (natK 1 / natK 2 : K) (natK 1 / natK 2) a z ∧
        ¬ CollapseSafe a z := by
  refine ⟨.det .fast,
          ⟨(natK 1 / natK 2 : K), natK 1 / natK 2, natK 5 / natK 2⟩, ?_, ?_⟩
  · exact (lemB_ii_linear_witness (K := K)).2.1
  · exact (lemB_ii_linear_witness (K := K)).2.2

/-- Corollary: the θ = 1 rung condition does not entail `CollapseSafe`, so
`CollapseSafe` is a strict strengthening of the rung condition — it rules
out states the rung condition admits. -/
theorem collapse_convention_strict_v2 (K : Type) [OrdField K] :
    ¬ (∀ (a : WitAct K) (z : WitState K),
        Theta1Adm (natK 1 / natK 2 : K) (natK 1 / natK 2) a z →
        CollapseSafe a z) := by
  intro h
  rcases collapse_convention_not_implied_v2 K with ⟨a, z, hadm, hnot⟩
  exact hnot (h a z hadm)

end Formalizations.P1Sep

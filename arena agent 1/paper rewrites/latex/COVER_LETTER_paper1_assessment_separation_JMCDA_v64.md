# Cover Letter — Paper 1 v64 (JMCDA, Special Issue "Better Decisions for a Better Tomorrow")

**Title:** Every weighting licenses a plan, no plan satisfies the floors: a quantifier-order separation between compensatory and noncompensatory transition assessment
**Author:** Amin Abaee (Independent Researcher, Tehran, Iran; ORCID 0000-0002-0019-1842)
**Journal:** Journal of Multi-Criteria Decision Analysis — special issue "Better Decisions for a Better Tomorrow: MCDM Approaches for Sustainability, Risk, and Complex Systems"

Dear Editors,

I am submitting the manuscript above for consideration in the special issue.

**The question.** When can a composite index certify a *transition* — a plan carried out over time, under disturbances, with several criteria required to hold along the whole path? Two acceptance semantics are compared: weight-adaptive (compensatory) acceptance, under which every weighting licenses some plan, possibly a different one per weighting; and common-plan (noncompensatory) acceptance, under which one plan must keep every criterion above its floor path-wise. At any fixed trajectory the full-cone aggregate is lossless, so the two can differ only through the order of the quantifiers over plans and weights.

**What is established.** (i) A geometric characterisation for any finite menu of plans: the acceptance gap is the part of the convex hull of the plans' required margins that no single plan dominates, so it vanishes exactly when the menu is convexified (Theorem 1). (ii) An explicit rational witness on which the gap has nonempty interior, with exact weight-ratio licensing thresholds — the acceptance-side analogue of weight-sensitivity analysis — and a closed-form reserve threshold separating rescuable from impossible states (Theorem 2, Proposition 5). (iii) Blending plans closes the gap exactly while alternating them in time does not (Theorem 3, Proposition 4). (iv) The separation is robust to the aggregator — every positive-elasticity CES index falsely certifies an exact interval of gap states, with critical floors 1 < 5/4 < √2 < φ < √3 → 2 — and to a shared shock (Theorem 4, Proposition 6). A fishery transition anchored to a regulated biomass limit realises the datum.

**Fit with the special issue.** *Sustainability:* the two semantics are the weak- and strong-sustainability doctrines read as acceptance protocols. *Risk:* all statements are robust (worst-case tubes), and the two protocols are the here-and-now/wait-and-see distinction of adjustable robust optimisation with the assessment weight as the uncertain parameter. *Complex systems:* the analysis is viability-theoretic, with exact-tube (path-wise) semantics.

**Verification.** All results are proved (appendices and SI). Every quoted number is re-derived in exact rational arithmetic by deposited code (figshare, DOI 10.6084/m9.figshare.33764023; six separate fail-loud check lists), and the core theorems are formalised in Lean 4 (programme repository, `lean/`, no `sorry`, no added axioms).

The manuscript is original, is not under consideration elsewhere, and I have no competing interests. A 30-page Supplementary Information accompanies it.

Yours sincerely,
Amin Abaee — amin_abaee@ut.ac.ir

# Audit of Paper06 v76

**Manuscript:** *Transition Certification with Composite Indices: The Acceptance Gap Between Compensatory and Noncompensatory Rules*  
**Audited file:** `paper06_assessment_separation_v76.txt`  
**Recommendation:** **Major revision before submission.** The central mathematical example is viable; several interpretive, novelty, verification, and benchmark claims need substantive correction.

## 1. Scope and bottom line

I read the complete supplied LaTeX source, checked its internal references, re-derived the principal formulas, inspected the pinned Lean source, and consulted the preceding v75 supplementary source from the archive identified in the manuscript. **The v76 supplement, figure assets, and executable verification package were not attached.** Findings about the supplement below are explicitly based on v75, not an assumption that v76 is identical. I did not compile the manuscript or run a Lean build.

The principal full-cone identity, finite-menu convex geometry under its declared margin-first semantics, rational witness, reserve threshold, and action-indexed blend window withstand direct checking. Independent rational spot checks over **1,183 states**, with at least **41 weight probes per state**, also agreed with the witness and common-shock accepted-set formulas. These finite checks are supporting evidence, not continuum proofs.

The main publication risk is **not a discovered collapse of the rational witness**. It is the distance between what the narrowly specified results establish and what the surrounding discussion says they establish. In particular:

1. The time-sharing result assumes a union of complete primitive excursions; it does not establish a general failure of finite-rate switching.
2. Physical fractional blending is repeatedly conflated with randomised strategies, producing an incorrect Kuhn-theorem discussion and an unsupported “randomisation-proof” classification.
3. The formalisation claim exceeds the coverage explicitly declared by the cited Lean module.
4. The fishery section contains a false claim about weights and an inconsistent exact-trajectory description.
5. Calling the gap intrinsically dynamic overstates what the elementary quantifier mechanism requires.

These are repairable, but should be addressed before further cosmetic polishing.

## 2. Findings requiring substantive revision

### A1. The strongest novelty claim is not established by the time-sharing proposition

**Locations:** §4.4, Proposition `prop:timeshare`; Appendix B, its proof; §6.4 novelty item 2; corresponding contribution and conclusion text. Source lines 406–407, 660–662, and 555.

**Finding — high severity:** The proposition defines the switching policy so that “the visited set is the union of the two primitive worst-case tubes.” The conclusion then follows immediately: the union is typed-safe exactly when each complete excursion is safe. This is correct **conditional on the stipulated union**, but the union is not derived from ordinary full-strength switching dynamics.

The primitive trajectories are time-parameterised over a full unit interval. Running a primitive control for a shorter subinterval at unchanged amplitude does not automatically reproduce its entire depth-2 excursion. Completing both full excursions in one interval generally requires time compression, higher rates, or an atomic-action interpretation. Those are different models.

A concrete distinction is available using the natural derivative implementation of the displayed primitive paths. Let fast change coordinate 1 at rate −4 before time 1/2 and +4 afterwards; let slow do the same to coordinate 2. Start at `(s1,s2)=(6/5,6/5)` and apply:

| Time | Active control | Floor margins at end |
|---|---|---|
| 0 to 1/4 | fast | (1/5, 6/5) |
| 1/4 to 1/2 | slow | (1/5, 1/5) |
| 1/2 to 3/4 | fast | (6/5, 1/5) |
| 3/4 to 1 | slow | (6/5, 6/5) |

Both floors stay positive, using **three switches and full primitive rates**. This is a different admissible-control extension, not a counterexample to the proposition as expressly scoped. It demonstrates why that scope cannot support a broad “finite-rate alternation fails” claim or a contrast requiring arbitrarily fine cycling.

The claimed inversion of adjustable robust optimisation is also not established: adjustable policies contain static policies when compared on the same model. Comparing fractional simultaneous allocation with compulsory complete-excursion sequencing compares different feasible control classes, not a reversed robustness ordering.

**Required repair:** Rename the result “Complete-excursion concatenation preserves primitive floor violations.” State the union-of-tubes assumption in the title or first sentence. Remove the “inversion” novelty claim unless a common dynamical model, admissible switching class, and genuine non-approximation theorem are supplied. Acknowledge that even coarse finite switching can be safe under a different natural control extension.

### A2. Correct the Kuhn-theorem discussion: pathwise assessment does not invalidate distributional equivalence

**Location:** §6.2, paragraph beginning “A reader from game theory will reach for Kuhn’s theorem”; source line 544.

**Finding — high severity:** The manuscript says Kuhn’s equivalence concerns distributions evaluated under an expected criterion and suggests that a worst-case/pathwise criterion makes the two randomisation notions non-interchangeable. This is not the right explanation.

Realisation equivalence is an equivalence of induced distributions under the theorem’s hypotheses. Equal laws give equal probabilities of measurable safety events; an appropriate essential-infimum criterion is also unchanged by equal laws. A worst-case or pathwise requirement does not, by itself, defeat that equivalence.

More fundamentally, a deterministic fractional control is not a lottery over primitive plans. One changes the physical trajectory; the other selects a primitive trajectory with some probability. The manuscript’s blend-versus-concatenation comparison is not a mixed-versus-behavioural strategy comparison in Kuhn’s sense.

The Main–Randour paper really does study finite-memory strategy classes, but merely using a finite menu and a finite horizon does not establish that this manuscript instantiates their restrictive automaton model. The added phrase “which is the setting here” is unsupported. Their precise framework is described in the cited article [2](https://www.sciencedirect.com/science/article/abs/pii/S0890540124000944).

**Required repair:** Replace this paragraph with:

> Fractional blending changes the admissible physical controls; it is not a lottery over primitive plans. Our comparison with complete-excursion sequencing therefore does not invoke or contradict Kuhn’s realisation-equivalence theorem. Any mixed-strategy interpretation requires a separately declared payoff, information structure, and treatment of disturbances.

Delete the finite-memory claim unless such a model is actually constructed.

### A3. Failure to restore feasibility is not “randomisation-proofness”

**Location:** §6.2, paragraph beginning “Separately”; source line 542.

**Finding — high severity:** The shared-shock datum is called “randomisation-proof at the canonical point” because blending fails to produce a typed-safe plan there. That is not the manuscript’s own stated definition of randomisation-proofness, which concerns lack of improvement in worst-case performance.

Under a natural simplex-normalised worst-margin payoff, at the canonical floors `(6/5,6/5)`:

- A primitive plan has worst margin `6/5 − 2 = −4/5`.
- The balanced common-shock blend has required margins `(5/4,5/4)`, hence worst margin `6/5 − 5/4 = −1/20`.

The blend **strictly improves the worst margin**, although it does not reach zero. Thus the demonstrated fact is failure of feasibility restoration, not lack of performance improvement. If “randomisation” instead means a literal lottery assessed by almost-sure safety, that is yet another model and is not the physical blend theorem.

**Required repair:** Replace “randomisation-proof” with “not feasibility-restoring at the canonical point under the specified shared-shock blend model.” Retain game-theoretic classifications only after defining and calculating the relevant value.

### A4. The cited Lean module explicitly excludes part of the claimed formal coverage

**Location:** §4.7 Verification, source line 509; compare the pinned module’s opening scope statement, approximately lines 84–105.

**Finding — high severity:** The manuscript claims formalisation of Theorem `thm:ladder` (ii)–(iii). The cited source instead explicitly lists as **not formalised**:

- nesting of the real-exponent power means;
- transfer of results to non-ladder elasticities;
- the continuity/IVT step;
- the relative-interior topology, replaced by an explicit interior witness.

Its final summary theorem, `s2_two_sided_summary`, establishes linear acceptance, false-certification examples for negative-integer rungs, and Leontief rejection. This is valuable, but it is not the full current theorem asserting a pointwise rejecting positive elasticity and an exact false-acceptance interval for **every** positive elasticity. The header even describes linear acceptance as showing Leontief is unnecessary at a fixed state; that does not prove existence of a finite positive-elasticity **rejecting** rung.

I confirmed **199 declarations beginning `theorem`** in the cited file. I did not establish successful compilation, imported dependency axiom status, or a machine-checked real-number instantiation of every abstract power/geometric interface.

**Required repair:** Supply a claim-to-theorem coverage table. Say “formalised algebraic components and selected/integer CES rungs,” not full coverage of (ii)–(iii). Explicitly separate assumed power/geometric interfaces from proven real instantiations. Mark the continuum transfer and topology as paper proofs. Correct both main text and SI; the archived v75 SI repeats the overstatement.

Pinned source inspected:
`https://raw.githubusercontent.com/MIKEAA2020/general-sustainability/6f626ee48b2a3a59282b5df5adda76c8d5993fdc/lean/Formalizations/P1_AssessmentSeparation.lean`

### A5. “No weighting can detect this” directly contradicts the full-cone identity

**Location:** §5, “The dashboard reading”; source line 519.

**Finding — high severity:** The statement that “no weighting can detect this from the index alone” is false for a fixed plan. At fast’s canonical trough, the margin vector is `(-4/5,6/5)`. Weight `(1,0)` gives `−4/5` and detects the biomass breach exactly. This is precisely the role of coordinate weights in Lemma `lem:cone`.

What survives every weight is **state-level acceptance with plan reselection**, not acceptance of the same fast trajectory by every weight. Similarly, “each licensing a different physical transition” is too strong: licensing ranges overlap, and several weights license the same plan.

**Required replacement:**

> A biomass-focused weight rejects fast. Nevertheless, every weight licenses at least one menu plan, so reweighting does not eliminate weight-adaptive state acceptance.

Keep this distinction consistent throughout the abstract, benchmark, discussion, and conclusions.

### A6. The benchmark is an envelope illustration, not the exact returning trajectory described

**Locations:** §5, “The schedule, exactly”; source line 517; archived v75 SI S5, around lines 306–310.

**Finding — medium/high severity:** Under zero harvest on the recovery half-interval, the biomass solves the logistic equation, not a straight returning line. From midpoint biomass `b`, the endpoint is

`B(1) = 10 / [1 + (10/b − 1) exp(−2)]`.

Thus:

- benign midpoint `b=1.7` gives endpoint about **6.02136 kt**;
- adverse midpoint `b=1.2` gives endpoint about **5.01892 kt**.

Neither returns exactly to **3.2 kt**. The main text later calls the piecewise-linear trajectory conservative, which is the defensible interpretation, but “tracks the tube line … exactly” is inconsistent with the stated closure. The v75 SI also says the visited range stays below `K/2=5`; the two endpoints above disprove that description.

The arithmetic for the first-half quotas and the adverse trough checks out. A lower-envelope comparison can still work: establish a comparison along the prescribed envelope, or stop the argument at its first possible crossing. It need not assert that the entire realised nonlinear trajectory remains below 5.

**Required repair:** Describe exact first-half tracking and a conservative recovery envelope separately. Specify terminal handling when the realised biomass exceeds the abstract successor. Write down the income-margin dynamics and their disturbance treatment; a biomass equation alone does not fully realise the second typed coordinate. Clarify that physical benchmark floor breaches are biomass-limit breaches, not necessarily biological extinction/collapse.

### A7. The quantifier gap is not inherently dynamic

**Locations:** contributions item (i), §3 opening and finite-menu discussion, conclusion; source lines 123, 221, 277, 601.

**Finding — medium/high severity:** Fixed-trajectory full-cone losslessness does not imply that separation “must therefore” be dynamic. The same gap exists between static alternative vectors `(-4/5,6/5)` and `(6/5,-4/5)`: every nonnegative weighting finds an acceptable alternative, but no alternative is componentwise nonnegative.

Time, disturbances, and path minima supply an important application setting, but the noncommutation itself is a menu-selection phenomenon. The finite-menu theorem already makes that clear.

**Required repair:** Replace “therefore dynamic” with “a plan-selection quantifier gap, here applied to robust pathwise transition assessment.” Explain which additional conclusions genuinely require paths: transient-versus-endpoint discrepancies, disturbance exposure, and implementability of control extensions. Avoid alternating between “distinct from Pareto-front geometry” and “reproduces this geometry exactly” without explaining the shared geometry and different decision question.

## 3. Formal and definitional repairs

### B1. Exclude the empty weight family

Proposition `prop:monotone` quantifies over any `W ⊆ W+` and asserts `V_W ⊆ V_phys`. For `W=∅`, the universal condition is vacuous and the intersection is the whole state universe, which need not be physically accepted.

**Fix:** Require `W ≠ ∅`, or define `V_W = V_phys ∩ ⋂_{w∈W} V_w`. Apply the same convention in the table and proof. This is a literal edge-case error, not a challenge to the intended monotonicity result.

### B2. Align the blend parameter domain

The family is introduced for `δ∈(0,1)`, while its theorem and proof use `[0,1]`. At margins `(2,0)` the only feasible parameter is `δ=1`, which is a primitive plan rather than a member of the stated open blend family.

**Fix:** Define the closed family, identifying its endpoints with the primitives; or intersect the window with `(0,1)` and discuss endpoints separately. The augmented-menu identity survives either consistent convention.

### B3. State that reserve increments are nonnegative

The infimum defining `κ*` does not explicitly restrict `κ≥0`. The proof uses that restriction when concluding that an already feasible state has threshold zero.

**Fix:** Write `inf{κ≥0 : …}` and evaluate admissibility at the augmented state explicitly.

### B4. Keep margin-first geometry separate from exact-tube scalarisation

The synchronisation lemma and surrounding qualification are useful and should remain. However, a theorem headed “for any finite menu” is easy to read as covering the earlier exact-tube operator automatically.

**Fix:** Put the requirement `m_a(w)=w·d_a` in the theorem’s hypotheses. Clarify whether a “convexified plan” is a convex combination of required-margin vectors or a physically implemented control. These coincide in the stipulated action-indexed witness, not in general: maxima and control mixing need not commute.

### B5. Distinguish standard CES properties from the collapse convention

The paper discloses the convention, but some explanatory language makes it sound inherent to all CES means. For `0<θ<1`, a nonnegative input with a zero coordinate can have a well-defined positive power mean. For example, `θ=1/2`, inputs `(0,4)`, and equal weights give mean **1**, not automatic rejection. Negative inputs are not ordinarily in the geometric mean’s positive domain; it is not accurate simply to say the geometric mean is zero there.

**Fix:** Describe automatic rejection as an added domain/safety rule. Restrict elasticity statements to `0≤σ≤∞`, equivalently `−∞≤θ≤1`. At zero weights, distinguish the weighted support-minimum limit from the unweighted all-coordinate minimum. The full-family accepted-set identification with typed acceptance can still be shown.

### B6. Tighten the CES proof at asymmetric states

In archived v75 SI S2, the proof uses an equal-weight strictness argument while discussing general off-diagonal states. Equal weight is binding by symmetry on the diagonal, not automatically off it.

**Fix:** For deep-interior states use continuity and a uniform positive linear slack over the compact weight simplex. For example, define the best-plan slack at each weight and show its minimum is positive when both margins exceed 1. Then continuity near `θ=1` supplies a finite accepting rung. Separately use the equal weight to exhibit rejection for sufficiently negative exponents. This fixes the argument without changing the stated deep-interior conclusion. Verify whether the missing v76 SI already does this.

## 4. Reproducibility, references, and submission package

### C1. Deposit a single version-matched package

The availability statement is unusually candid that the Figshare manuscripts are earlier editions and several verifier scripts/logs are absent. That honesty is a strength, but the current package is not an independently reproducible v76 submission.

Provide:

- v76 main article and v76 SI, both source and PDF;
- all figure assets and generation scripts;
- all reported ladder/off-diagonal/continuum/common-shock scripts and logs, or remove unsupported check-count detail;
- pinned Lean project, toolchain, build instructions, and theorem coverage matrix;
- a clean-environment reproduction command and version/hash manifest.

Do not use theorem counts, version numbers, or “fail-loud” wording as substitutes for accessible artifacts and coverage.

### C2. Date the Northern-cod anchor and locate the exact number

The 2016 DFO report does support **2015 SSB around 300,000 tonnes and 34% of its then-used LRP** [1](https://www.dfo-mpo.gc.ca/csas-sccs/Publications/SAR-AS/2016/2016_026-eng.html). Later DFO documentation describes a revised assessment and LRP, so **884.6 kt must be presented as a historical assessment-vintage anchor**, not an unqualified current regulated threshold [3](https://waves-vagues.dfo-mpo.gc.ca/library-bibliotheque/41302813.pdf).

I did not independently locate the exact **884.6** value in a primary table during this audit. Supply its page/table or describe the calculation and data version. The manuscript’s explicit no-fit/no-validation disclaimers should remain.

### C3. Internal references passed the source-level check

No missing `ref`/`eqref` labels, duplicate labels, missing citation keys, or uncited bibliography entries were found. That is not a typesetting or bibliographic-content validation. No compiled PDF/figure audit was possible from the attachment alone.

### C4. Reduce repetition and defensive positioning

The abstract, five contributions, literature-positioning paragraph, four novelty claims, discussion, limitations, and conclusion repeatedly rehearse the same scope restrictions. Consolidate them. Remove claims that an entire sustainability debate is largely verbal; the manuscript’s own cited maximin/viability literature makes such a sweeping contrast risky.

An effective shorter structure would be:

1. Protocol distinction and witness.
2. General geometry with its exact hypotheses.
3. Implementability remedies and their control-class assumptions.
4. CES and disturbance robustness.
5. One clearly labelled illustrative benchmark.
6. Practical report requirements and limitations.

## 5. What can be retained with confidence

Subject to the stated modelling assumptions, the following mathematical core is worth preserving:

- `E_typ(z)=⋂_w E_w(z)` on the full nonnegative cone, including coordinate weights.
- The elementary inclusion between common-plan and per-weight acceptance.
- The hierarchy based on nested constraint sets.
- The finite-menu separating-hyperplane argument for **margin-first** scalarised requirements.
- The witness identities `V_typ={x≥1} ∪ {s1≥2} ∪ {s2≥2}` and `V_weak={x≥1} ∪ {s1+s2≥2}` over the declared initial domain.
- The licensing thresholds, rational canonical point, and reserve augmentation threshold after specifying nonnegative increments.
- The action-indexed blend window under the stated linear-flow assumption.
- The diagonal CES comparisons and the listed geometric/harmonic/square-root critical values.
- The specified shared-shock accepted-set and blend-window formulas, supported by independent re-derivation and finite checks.

This is a credible analytical note or article **if its contribution is sold as a carefully scoped transition-certification construction and diagnostic**, not as a new reversal of strategy-equivalence or robust-control theory.

## 6. Priority revision sequence

1. Remove or replace the Kuhn, randomisation-proofness, and robust-ordering-inversion claims.
2. Recast complete-excursion time-sharing as a conditional lemma; define the actual control classes.
3. Correct the fixed-plan versus per-weight-plan statements in the benchmark and conclusion.
4. Narrow the Lean coverage statement to the actual pinned theorems and interfaces.
5. Correct the fishery trajectory/envelope description and historical LRP labelling.
6. Fix the empty-family, blend-domain, and nonnegative-increment definitions.
7. Publish a version-matched source/SI/code bundle.
8. Shorten the framing and keep novelty claims proportionate.

**Final assessment:** The witness does not need to be abandoned. The manuscript does need a substantive claims audit and a cleaner boundary between elementary geometry, declared control extensions, analytic CES results, formalised subresults, and biological illustration.

---

### Audit artifacts

Independent checks: `audit_materials/independent_checks.py`  
Results: `audit_materials/independent_checks_results.json`  
Retrieved comparison materials: `audit_materials/P1_AssessmentSeparation.lean` and `audit_materials/v75_supplementary.tex`.

The original manuscript was not modified.

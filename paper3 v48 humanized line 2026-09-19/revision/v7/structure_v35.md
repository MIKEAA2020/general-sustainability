# Structure register - paper3_material_ledgers_v35

Generated from the file itself; v34 is the base and is unchanged on disk. Builder `build_v35_kernel.py`, gate `verify_v35_build.py` (ALL CHECKS PASS), PDF 51 pages (v34: 48), tex pure ASCII.

## What v35 changed relative to v34 (22 logged edits)

 1. `def35-price-sign` (replace): `A non-positive price means the exchange enters the combined budget of the comp` -> `A price is margin consumed (positive) or margin released (negative) per unit o`
 2. `prop36-lift` (replace): `Every left-null vector of $S_1$ and of $S_2$ lifts to a left-null vector of th` -> `The conserved quantities of the composition are exactly the pairs of part-wise`
 3. `prop36-proof` (replace): `*Proof.* For the lift, $\ell^{\top} \mathrm{diag}(S_1, S_2) = 0$ with equal en` -> `*Proof.* The identification rows are the only further constraints, so a covect`
 4. `prop36-proof-dummy` (replace): `the composition's programme is $\max \lambda$ subject to $q = \lambda$, $s = \` -> `the composition's programme is $\max \mu$ subject to $q = \mu$, $s = \mu$, $q `
 5. `prop37-display` (replace): `\[ B_1 + B_2 + \sum_{\varphi \in \Phi} \pi_\varphi^{+}\, \bar v_\varphi\, T, \` -> `\[ B_1 + B_2 + \sum_{\varphi \in \Phi} |\pi_\varphi|\, \bar v_\varphi\, T . \]`
 6. `prop37-free` (replace): `The sum is the *margin needed* to absorb the interface; the interface is free,` -> `The sum is the *margin needed* to absorb the interface; the parts' budgets add`
 7. `prop37-lmax` (replace): `With a single exchange of box $[0, L]$, price $\pi > 0$ and horizon $T$, the c` -> `With a single exchange of box $[0, L]$, non-zero price $\pi$ and horizon $T$, `
 8. `prop37-proof` (insert): `Along the composition, $\dot V \le -(y_1 + y_2) + \lambda_1^{\top} G_1 b_1 + \` -> `Along the composition, $\dot V \le -(y_1 + y_2) + \lambda_1^{\top} G_1 b_1 + \`
 9. `def40-remark34` (replace): `These three statements are the calculus the article's own citations had deferr` -> `**Definition 40 (Compensation as a decidable predicate).** Fix a partition of `
10. `prop39-interval` (replace): `More generally, where the declared constraints are linear and the event time i` -> `More generally, where the declared constraints are linear the fibre is a polyt`
11. `prop39-proof` (insert): `The fibre is an intersection of the declared boxes with the invariant hyperpla` -> `The fibre is an intersection of the declared boxes with the invariant hyperpla`
12. `sec71-noise-typing` (insert): `and the results are statements about the declared class.` -> `and the results are statements about the declared class. Transfer noise obeys `
13. `lambda-star-to-Lambda` (replace): `$\lambda^{*}=\max\{\lambda:\ \lambda D\in P(\mathcal K)\}$` -> `$\Lambda^{*}=\max\{\mu:\ \mu D\in P(\mathcal K)\}$`
14. `lambda-star-to-Lambda2` (replace): `Where $\lambda^{*}\ge1$, the cycle closes at the demanded rate. Where $\lambda` -> `Where $\Lambda^{*}\ge1$, the cycle closes at the demanded rate. Where $\Lambda`
15. `lambda-star-to-Lambda3` (replace): `each therefore closing tightly at $\lambda^{*} = 1$; when the two return fluxe` -> `each therefore closing tightly at $\Lambda^{*} = 1$; when the two return fluxe`
16. `def23-C-label` (replace): `with $C$ the readout matrix of Section 2.1,` -> `with $C$ the moiety-composition matrix of Section 2.1 (Lemma 3),`
17. `remark33-premium` (replace): `No premium figure is reported in this article, because the component tables of` -> `A figure can be read straight off the published component table: on the world `
18. `numbering-range` (replace): `runs on the single 1–39 sequence counter` -> `runs on the single 1–44 sequence counter`
19. `numbering-added` (insert): `the statements added at this revision carry the consecutive labels Definitions` -> `the statements added at this revision carry the consecutive labels Definitions`
20. `Oksendal-braces` (no-op in md): `the stochastic machinery is Itô calculus in its textbook form (Øksendal, 2003)` -> `the stochastic machinery is Itô calculus in its textbook form (Øksendal, 2003)`
21. `def41-43-predicates` (replace): `These three statements are the calculus the article's own citations had deferr` -> `**Definition 41 (Control margin).** Let $(\mathcal K_\rho)_{\rho \ge 0}$ be th`
22. `def44-lemma4` (replace): `These three statements are the calculus the article's own citations had deferr` -> `**Definition 44 (Governability ratio).** Let $h$ be the declared review interv`

## Sections (md; tex carries the same 71)

- Abstract
- 1. Introduction
  - 1.1 Failure modes and the two confusions
  - 1.2 Contributions
  - 1.3 Organization
- 2. The Typed Primitive Ledger
  - 2.1 Typed stocks, primitive fluxes, and the incidence discipline
  - 2.2 The closed finite-donor ledger
  - 2.3 The six-compartment illustration
  - 2.4 The four-stock resource–sink–nutrient–product system
  - 2.5 Mechanism typing: routing is never determined by diagnostic labels
  - 2.6 Support saturation and the logistic limit
- 3. Certification Layers and the Accounting Theorems
  - 3.1 Three predicates, separated
  - 3.2 The typed safety set
  - 3.3 The flux-reconstruction identity
  - 3.4 The conservation-law reduction
  - 3.5 The flux-bounding envelope theorem
  - 3.6 Finite exhaustion under uniform drift, and its failure mode
  - 3.7 Composition of ledgers and the calculus of certificates
- 4. Conservation and Positivity of the Closed Ledger
  - 4.1 The natural-block mass identity
  - 4.2 Stoichiometric conservation of the full ledger
  - 4.3 Conservation of the six-compartment ledger
  - 4.4 Orthant invariance
  - 4.5 No interior rest at positive effort
  - 4.6 The extinction–geochemical rest set
  - 4.7 Extraction integrability
  - 4.8 The conditional hybrid moiety balance
  - 4.9 Cancellation is cheap
- 5. Service Readouts and the Componentwise Deficit
  - 5.1 The service readout and the contemporaneous balance
  - 5.2 The state-dependent feasible balance domain
  - 5.3 Support provenance and the directional support gap
  - 5.4 The componentwise deficit and the specialization identity
- 6. Depletion Arithmetic
  - 6.1 The three quantities
  - 6.2 Uniform-drift bounds
  - 6.3 Upper barriers, exit times, and maintainability
  - 6.4 Robust semantics
  - 6.5 Application classifications at their exact status
    - 6.5.1 Groundwater anomaly-persistence indices
    - 6.5.2 The applied depletion-horizon tables
    - 6.5.3 The phosphate reserve-life ratio
    - 6.5.4 The fisheries removals-only pressure time
  - 6.6 What an aggregate record fixes
- 7. First-Passage Semantics on Declared Surrogates
  - 7.1 Two objects, not one
  - 7.2 The observed-drift Brownian surrogate
  - 7.3 The inverse-Gaussian groundwater first passage
  - 7.4 The record-relative barrier discipline
  - 7.5 The geometric-Brownian fisheries first passage
  - 7.6 The constant-production phosphate passage time
  - 7.7 The explicit non-claims
  - 7.8 Parameter and observation uncertainty
- 8. Domain Templates at Registered Status
  - 8.1 The phosphorus template
  - 8.2 The groundwater template and the two-pool gap
  - 8.3 Extractor-side harvest economics
- 9. The Interface with Institutional Delay Dynamics
- 10. What the Ledger Does Not Support
  - 10.1 Compensatory aggregation is rejected, not merely discouraged
  - 10.2 The double-counting discipline
  - 10.3 Negative and boundary content is first-class
  - 10.4 Limitations
- 11. Conclusion
- Data availability
- Code availability
- Declaration of competing interest
- References
- Supplementary material

## Statement inventory (md = tex, 54 labels, no type+number pair repeated)

Numbering is per type, and numbers are shared across types (Theorem 1 / Proposition 1 / Definition 1 all
exist; so do Definition 40 / Proposition 40 and Definition 34 / Remark 34, the latter pair pre-existing in
v34). The union of numbers used runs 1-44 with a single gap, **15**, which is pre-existing and is the number
the body note's citation list also passes over.

- **Corollary** (x1, max 19): [19]
- **Definition** (x17, max 44): [1, 2, 3, 4, 5, 6, 21, 22, 23, 34, 35, 38, 40, 41, 42, 43, 44]
- **Lemma** (x2, max 4): [3, 4]
- **Proposition** (x19, max 40): [1, 2, 4, 6, 17, 18, 20, 25, 26, 27, 28, 29, 30, 31, 32, 36, 37, 39, 40]
- **Remark** (x4, max 34): [2, 16, 33, 34]
- **Theorem** (x11, max 24): [1, 5, 7, 8, 9, 10, 11, 12, 13, 14, 24]

## Cross-cutting invariants

- numbering note (Section 3.1, where the note has lived since v34) reads "1-44 sequence counter" and lists the added labels "Definitions 21-23 and 34-35 and 38 and 40-44, Lemma 4, Theorem 24, and Propositions 25-32 and 36-37 and 39-40, with Remarks 33 and 34" in both formats.
- no label repeated (54 labels, md set identical to tex set).
- every composition-calculus object now states its own scope: |pi| magnitude for the interface charge, sufficiency (not iff) for L_max, connectedness (not monotonicity) for the T(z) interval, compatible-on-classes for lifted conservation, LP feasibility (not prices) for compensation.
- display math is written verbatim in the tex; `\O{}ksendal` braces fixed. Both were inherited defects of the md->tex port, present in v33/v34 and now corrected here.

## Register still open (see review/remaining_points_v3_deep_mine.md for reasons)

- non-displacement/additionality gate
- supportable-output envelope + yield-inflation non-identifiability (full form)
- LSIT as statement only
- mechanism-design umbrella proposition (with the D4 wording item)
- per-parameter identifiability status field + MDV table (supplementary batch)
- superlevel-set alternate proof of Prop 29 (supplementary)

## Author decisions still outstanding

- Remark 33 premium: figures and both conventions are now in the text; whether to keep the zero-biocapacity carbon row in the ratio set remains the author's call.
- companion pointer "eq. (1) and Section 2.4" (unverified); D4 wording; MDV placement; uploading the claimed code archive `revision/v5/code/`.

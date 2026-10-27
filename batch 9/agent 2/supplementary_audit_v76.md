# Audit of the v76 Supplementary Information

**File audited:** `paper06_assessment_separation_v76_supplementary.txt`  
**Compared with:** the supplied v76 main article and the previously retrieved archived v75 supplement.  
**Recommendation:** **Major revision.** The off-diagonal algebra and several exact witnesses are sound, but the supplement contains additional false statements, incomplete continuum certification, and material that should not remain in a submission-ready theorem supplement.

## Executive assessment

The supplement does **not** overturn the main article’s rational witness. It does, however, add significant problems beyond those identified in the main-article audit:

1. Its three purported sufficient mechanisms for multi-stage gap erasure are not sufficient as stated.
2. The proposed “truncation” changes terminal assessment semantics, rather than simply removing a stage.
3. Its global fixed-sum shape and minimum are described as certified without supplying the actual proof or certificates.
4. The fixed-sum ladder mixes an unattained infimum, boundary acceptance, and actual Leontief acceptance, then incorrectly calls a plateau strictly increasing.
5. The nested-impossibility example has the wrong intersection, and the theorem’s assumptions actually imply **finite-generation infeasibility**.
6. Conjecture C5 contradicts ordinary existential-viability monotonicity unless the dynamics or policy class change.

The v76 revision **does improve** the CES continuity paragraph relative to v75: it removes the off-diagonal equal-weight shortcut and restricts the argument to the deep interior. That earlier criticism should therefore be narrowed to the remaining need for a uniform-continuity/slack argument, not repeated as though the text were unchanged.

### Audit methods and limits

I read the complete 745-line source, checked its cross-references against the main article, compared v75 and v76, re-derived the geometric and power-mean cover tests, and ran independent checks. Four geometric witness verdicts were certified using rational logarithm enclosures; 361 rational harmonic checks agreed with the circle formula. Numerical root calculations corroborated the reported tangency locations, but **do not establish uniqueness, global minimality, or the absence of further stationary points**.

No figures or compiled supplement were attached. I did not compile LaTeX, run the author’s unavailable verifier scripts, or perform a fresh Lean build. The Lean coverage assessment uses the pinned source inspected during the preceding audit.

## 1. High-priority mathematical and logical findings

### SI-01 — The claimed sufficient erasure mechanisms are false without further hypotheses

**Location:** S2.1, line 114, “Conditionality.”

The supplement says each of the following is sufficient to erase the gap: a common typed-safe continuation, coincident typed and weak terminal sets on the reachable subset, or actions coupled across stages.

None is sufficient in this unqualified form. A continuation cannot repair a floor already breached on an earlier tube. Coincident terminal sets do not make different path constraints coincide. Merely coupling actions across stages says nothing about whether feasibility improves or worsens.

**Counterexample using the paper’s own witness:** impose the same typed destination set on both doctrines. Fast and slow already have successors with nonnegative floors, so their terminal verdicts remain unchanged. Their scalarised tubes can still pass while their typed tubes fail. Thus the canonical gap persists despite coincident terminal requirements. A safe continuation after those successors does not remove the earlier breach either.

**Repair:** Replace the assertion with the narrower statement:

> These changes can erase a gap in particular architectures, but none suffices without controlling earlier path constraints and the reachability of its required continuation states.

Give exact sufficient hypotheses if a theorem is wanted. Preserve the valid hold-prefix induction and distinguish it from this overgeneralisation.

### SI-02 — The erasure comparison is not a literal truncation with fixed terminal semantics

**Location:** S2.2, lines 119–123.

The two-stage datum declares final terminal sets

`G^(2) = G^{w,(2)} = {s≥0}`.

The alleged one-interval truncation instead uses

`G = {s≥0}`, but `G^w = {w·s≥0}`.

Those are different terminal assessment rules. Deleting the repair interval while retaining its declared terminal sets would not produce the claimed weight-adaptive gap: both first-stage successor vectors leave the orthant.

The intended erasure example is easily repaired. In **both** problems use the ordinary terminal rules: typed orthant and scalarised halfspace. The repair action sends every state to `(1,1)`, so the **second-stage accepted-state sets**, rather than the terminal constraint sets, coincide with all of `R²`. Removing that stage now gives a genuine truncation with fixed terminal assessment rules and the desired gap.

**Repair:** Make this change and attribute erasure to the repair stage’s coincident accepted-state sets, not to equality of terminal sets.

### SI-03 — S3.4 does not supply the global continuum certificate it claims

**Locations:** S3.4, lines 217–224; S3.7, line 237; S7.3, line 463.

The off-diagonal criterion justifies the scalar reduction

`φ(s)=s+ρ(s)`.

It does **not** by itself prove that there are exactly three stationary points, the asserted four-phase shape, equal global minima, or all the fixed-sum elasticity bounds. These are new, nontrivial results. The source provides conclusions and decimal enclosures, but not the derivative-sign proof, root-isolation certificate, or verifier needed to check their global status. S7 explicitly says the continuum scripts and logs are absent from the inspected packages.

Independent high-precision calculations give:

- `a ≈ 1.1479678539167292628`;
- `b ≈ 1.6746019109165294898`;
- `a+b ≈ 2.8225697648332587526`.

These agree with the stated brackets. This is **numerical corroboration of a stationary pair**, not a proof that this pair gives the unique two global minima.

In particular, “value anchors and elementary asymptotics” do not exclude additional derivative zeros between an endpoint neighbourhood and an anchor unless quantitative neighbourhoods and sign bounds are supplied.

**Repair:** Either provide a numbered proposition with a complete analytic proof, or publish independently checkable interval certificates containing:

1. a precise definition of all functions and derivatives;
2. a finite interval partition and rational enclosures;
3. derivative-sign or root-count bounds on every partition element;
4. existence and uniqueness certificates for the isolated roots;
5. explicit endpoint-neighbourhood bounds;
6. a checker and instructions reproducing the stated enclosures.

Until then, label the global shape and dependent bounds as numerically supported, not “each a certified rational proof.”

### SI-04 — The fixed-sum ladder mixes domains and limit operations

**Location:** S3.4, line 224.

The line says every negative-integer rung **and the Leontief member** have flip total exactly 3, then calls the sequence “strictly increasing in depth.”

There are two problems:

**First, it is not strictly increasing.** The displayed sequence reaches a plateau at 3. At most it is nondecreasing, with strict increases only before the plateau.

**Second, the Leontief case differs fundamentally from the finite rungs.** On the stated deep-gap domain `(1,2)²`, no Leontief plan is accepted at any point: typed acceptance needs one initial margin at least 2. Its accepting subset there is empty, so the infimum of accepting totals is not 3; under the standard extended-real convention it is `+∞`.

For a finite negative-integer rung, accepting deep-gap points can approach `(1,2)` or `(2,1)`, giving infimum total 3 without attaining it. For Leontief, those boundary points are typed-accepted only **after enlarging the domain**. If the full nonnegative margin domain is used instead, Leontief already accepts `(2,0)`, of total 2.

**Repair:** Define the flip total and its domain explicitly. Report separately:

- finite-rung infima over the open deep-gap domain;
- attainment or nonattainment;
- the boundary-extended problem;
- the Leontief operator on the actual gap.

The fact that an infimum over states can approach the Leontief boundary does not make the Leontief member falsely certify a gap state.

### SI-05 — The nested-impossibility theorem is valid but stronger and more elementary than presented

**Location:** S9.3, lines 629–651.

The theorem assumes one common compact confinement set `K`, closed generation sets, decreasing nesting, and empty intersection. Its conclusion is correct. But compactness gives more:

> Some finite generation N already has `K ∩ V^(N) = ∅`.

Otherwise the decreasing compact sets `K∩V^(k)` would all be nonempty, and the finite-intersection property would force a nonempty intersection, contradicting the hypotheses. Thus no path confined to K can satisfy the requirements through that finite generation. The omega-limit proof is unnecessary, and forward completeness is not needed for this set-theoretic obstruction.

Consequently, **“every finite prefix is feasible but no infinite path is feasible” is incompatible with the theorem’s full assumptions**, not merely something the theorem fails to establish.

The suggested example `V^(k)=[0,1/k]` also has intersection **{0}**, not the empty set. It cannot have “no point belonging to all sets” as written.

**Repair:** State the finite-generation obstruction and remove the erroneous example. If illustrating a different finite/infinite phenomenon, explicitly drop an assumption. For example, with constant trajectories, unrestricted nonnegative initial states, and `V^(k)=[k,∞)`, every finite prefix can be satisfied by a sufficiently large initial state but no finite constant satisfies every generation. This example lacks the common compact confinement set, and should be labelled accordingly.

### SI-06 — Conjecture C5 contradicts existential-viability monotonicity

**Location:** S9.6, line 700.

The conjecture says expanding a constraint boundary can contract the viability kernel if it admits a new attractor.

With fixed dynamics, information, disturbance semantics, and policy class, safe-set inclusion `K1⊆K2` gives

`Viab(K1)⊆Viab(K2)`.

Every previously safe trajectory remains safe. A newly admitted attractor cannot remove the existence of the old viable policy.

**Repair:** Withdraw the conjecture in this form. If the intended effect concerns an endogenously changed feedback, equilibrium selection, or attraction basin, define that different object and specify the changed dynamics/policy rule. The supplement’s own no-silent-transfer principle requires this distinction.

## 2. Proof repairs and scope clarifications

### SI-07 — The CES proof is improved in v76, but its uniformity argument should be explicit

**Location:** S2.3, lines 144–146.

Unlike v75, v76 correctly restricts finite-rung persistence to `1<s1,s2<2` and no longer appeals to equal-weight strictness off the diagonal. This fixes an important part of the earlier concern.

To complete the argument cleanly, write the best-plan linear trough slack as

`g(p)=p s1+(1−p)s2−2 min(p,1−p)`.

For both margins above 1, g is strictly positive on the compact weight interval. Continuity gives a positive minimum; joint continuity of the positive-input power means in p and θ then preserves coverage uniformly for θ sufficiently close to 1 from below.

Also correct the proof’s labels: divergence as θ tends to minus infinity establishes a positive lower bound on the accepting elasticity threshold; linear acceptance alone does not establish a **finite** threshold. The finite accepting rung just proved supplies that missing side.

For strict separation of successive diagonal critical floors, invoke the **strict** power-mean inequality at unequal positive inputs and equal positive weights. Nesting alone establishes only a non-strict ordering.

### SI-08 — The coupled-class proof drops a necessary coordinate condition

**Location:** S4.3, line 262.

The displayed theorem correctly includes `s1,s2≥δ`. The proof then says an I-state survives **exactly** when `s1+s2≥3/2+2δ`, dropping those conditions.

Counterexample:

`x=1/2, s1=1/10, s2=39/20, δ=1/4`.

This is in the original I-region and passes the total-margin requirement: `41/20≥2`. But `s1<δ`, so it is coupled-rejected.

**Repair:** Retain all three conditions. The omitted coordinate cuts are automatically implied by the total condition and `si<2` when `δ≥1/2`, which is enough for the particular boundary argument near 5/4; state that restricted reasoning explicitly. The existence cutoff at 5/4 can remain.

### SI-09 — Distinguish assumptions from inherent CES properties

**Locations:** S2.3, collapse lemma, lines 136–139; S3.5, line 229.

Automatic rejection at a zero input for every θ<1 is a declared convention, not a general CES property. For θ=1/2, inputs `(0,4)`, and equal weights, the standard power mean is 1. Negative inputs are outside the ordinary geometric mean’s positive domain; “the geometric mean is zero there” conflates zero and negative inputs.

The Leontief limit at a weight with zeros is ordinarily the minimum over positive-weight coordinates, not necessarily the minimum over all coordinates. The full-family accepted-set identity can still be established; specify which convention is used.

The LPI caveat lists **three**, not two, qualifications. The inclusion between all-weight and specified-weight acceptance is valid only for the **same inputs, menu, and safety semantics**. It does not compare false-acceptance exposure of the actual published LPI and this constructed floor-index protocol without those bridges.

### SI-10 — “All numbers rational” and “every interior threshold transcendental” are false

**Location:** S3.7, line 237.

The section contains `sqrt(2)`, the golden ratio, logarithms, and nonrational critical values. Say that **computed enclosures and algebraic witnesses use rational certificates**, not that every number is rational.

Conversely, the claim that every interior σ* is transcendental is refuted by the table’s exact value `σ*(5/4,5/4)=2`. Do not assert transcendence of the other thresholds without a theorem. Use “generally defined implicitly; numerical values are supplied with rational enclosures.”

The displayed bracket for t* has width `1.5×10^−10`; its endpoints do not uniquely determine rounding to ten decimal places. Report the enclosure itself rather than the ambiguous phrase “certified to ten places.”

## 3. Benchmark, provenance, and verification findings

### SI-11 — The exact-trajectory inconsistency remains explicit in S5

**Location:** line 307.

The supplement claims that zero-harvest recovery makes a returning straight line an exact trajectory and that the visited range remains below K/2=5. Neither is true for the stated logistic equation.

Exact recovery from the midpoint gives approximately **6.02136 kt** on the benign branch and **5.01892 kt** on the adverse branch at time 1. Both exceed 5. The first-half quota arithmetic and trough values remain consistent.

**Repair:** Separate exact first-half tracking from conservative recovery-envelope certification. Prove the lower-envelope comparison along the prescribed envelope or using a first-crossing argument, without assuming the entire realised trajectory stays below 5. Define terminal handling and the income dynamics. The description “cuts the quota hard” is also misleading: the first-half quota exceeds the stated sustained-yield quota and deliberately drives down biomass.

### SI-12 — The two-stock reading and the framework specialisation change the declared types

**Locations:** S3.3, line 213; S9.1, line 544.

The benchmark starts with one biomass margin and one fleet-income margin. S3.3 suddenly interprets both coordinates as two fish stocks and sums their biomass. This is a permissible **new illustration**, not the same benchmark unless the retyping is declared.

S9 then calls the coordinates “reserve stock, protected-group service surplus, remediation-liability coverage,” and labels them all conserved moieties. That does not match the main article’s fishery reading, and services and liability margins are not automatically conserved substances. The named `D={α,β}` is also not explicitly specified by that notation in the main article’s witness section.

**Repair:** Use the abstract reserve and typed-floor coordinates consistently. Provide separate, explicit specialisation maps for the one-stock/income interpretation and the two-stock illustration. Do not identify physical conservation with mere dimensional compatibility or margin arithmetic.

### SI-13 — S7 confirms rather than resolves the reproducibility and Lean-coverage concerns

**Locations:** lines 463–465.

The frank admission that four verifier families and their logs are absent from the inspected packages is appropriate. It conflicts, however, with the repeated presentation of their results as available global certificates. A check count cannot substitute for the checker, certificate, input specification, and successful output.

The SI repeats the overbroad formalisation claim for current Theorem 4(ii)–(iii), while the pinned Lean header explicitly excludes real-exponent nesting, non-ladder transfer, continuity/IVT, and topology. It also replaces full interior topology by an explicit interior witness. Describe these as partial algebraic and selected-rung coverage, not complete formalisation of the current assertions.

**Repair:** Publish one version-matched package and a coverage matrix separating analytic proofs, certified computations, finite grid checks, abstract interface theorems, and real instantiations.

### SI-14 — Correct the terminology map’s quantifiers and strategy analogy

**Location:** S6.1, lines 354–360.

The acceptance-gap row says “accepted by some weighted sum,” which is weaker than the defined full-cone gap. The I-row says typed rejection is a separate question, but typed rejection is already part of the definition of I. The “mixed strategies vs deterministic sequencing” correspondence is not an exact equivalence of mathematical role for physical blending.

**Repair:** Use “every weight licenses some plan, but no plan satisfies all typed floors.” Replace the strategy row with “fractional physical allocation versus complete-excursion sequencing under the declared control models.” Retain the useful menu-relative reporting and empirical-data checklist.

## 4. Cross-reference and editorial fixes

Source-level internal labels resolve and no duplicate labels were found. Several **hard-coded references are wrong**, which a label-only check does not catch:

| SI location | Printed reference | Correct reference in supplied main article |
|---|---|---|
| S2.3, line 146 | main Table 4 for CES ladder | **Table 7** |
| S5, line 305 | main Table 5 for action tubes | **Table 4** |
| S7 enumeration, line 434 | main Table 5, fast row | **Table 4** |
| S6 checklist, line 369 | design tests in main §6.3 | **§7.3** |

Use shared labels or generated external references instead of manual numbers.

Additional wording changes:

- In S3.2, “no per-coordinate rational condition separates” the two displayed examples is too strong: a rational threshold between their second coordinates separates those examples. Say no claimed simple coordinatewise rule characterises the **whole** boundary.
- “No internal holes” in S3.4 applies within a monotone phase; for totals between t* and `2sqrt(2)`, the full slice has separated accepting windows. Make that distinction explicit.
- “Two readings bracket the coupled truth” needs a declared model ordering or external evidence. They are two specified disturbance models, not an established bracket on reality.
- State the historical assessment vintage and primary table behind the 884.6 kt LRP, as requested in the main audit.
- Keep response prescriptions conditional on the assumed institutional rule. A scalar acceptance theorem does not itself establish what an actual agency does.

## 5. What can be retained

The following material is substantively useful:

- The hold-prefix induction under its actual assumptions.
- The repair-stage erasure construction after terminal semantics are aligned.
- The diagonal master comparison and exact listed algebraic rungs.
- The geometric off-diagonal criterion `AD≤BC`, its decreasing involution, and its fixed point at `sqrt(2)`.
- The fractional-power multilinear comparison on its declared domain.
- The four checked geometric witness verdicts, including the fixed-total balanced/asymmetric contrast.
- The harmonic circle formula on the positive deep-gap domain.
- The common-shock and coupled-class formulas with their coordinate cuts retained.
- The practitioner checklist’s emphasis on menu completeness, exact versus conservative tubes, implementation, and uncertainty.

The global shape of φ may also be correct—the numerical evidence agrees—but it requires the missing proof/certificate before carrying the advertised status.

## 6. Recommended revision order

1. Correct the erasure comparison and remove its unqualified sufficiency claims.
2. Fix the fixed-sum/Leontief domain and infimum statements.
3. Supply the global continuum certificate or downgrade the dependent claims.
4. Correct the nested-impossibility discussion and withdraw/redefine C5.
5. Repair S5’s trajectory/envelope description and the inconsistent type mappings.
6. Narrow formal-verification coverage and deposit the actual artifacts.
7. Correct hard-coded references and compress S9.

**Editorial recommendation:** Move S9’s unsupported composition formulas and unformed conjectures into a separate research-programme note. Explicitly marking material “unsupported as written” is honest, but it does not make that material useful in the technical supplement of this article. Keep only extensions with complete definitions, proof conditions, and a direct role in interpreting the paper.

**Bottom line:** The supplement contains a sound algebraic core, but is not yet a reliable proof-and-reproduction package. Its most urgent repairs are logical and mathematical, not stylistic. None of the new findings requires abandoning the main rational witness.

---

### Independent audit artifacts

- `audit_materials/supplement_independent_checks.py`
- `audit_materials/supplement_independent_checks_results.json`

The rational log checks use an explicit positive-term artanh series with a geometric tail bound. The tangency calculation uses arbitrary-precision numerical root finding and is deliberately not labelled a global certificate. The submitted source files were not modified.

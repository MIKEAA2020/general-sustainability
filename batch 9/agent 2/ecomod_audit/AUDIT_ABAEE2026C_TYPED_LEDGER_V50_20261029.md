# Audit: Abaee (2026c), *Typed Flux Ledgers and Depletion Arithmetic*, v50

**Why this version:** ECOMOD C17 cites the v50 PDF at a commit-pinned GitHub URL and uses Sections 1.1 and 10.1 for its comparison of weak/strong sustainability and scalar versus componentwise assessment.

**Scope:** selected mathematical claims with high leverage for the C17 citation; internal consistency of definitions, proofs, numerical examples and source artifacts; and arithmetic checks on reproduced outputs. This is an audit, not an independent review of every cited literature claim or every statement in the 54-page manuscript. No source manuscript was edited.

## Overall assessment

The companion contains useful and mostly sound components: the natural-block mass balance, the displayed one-resource incidence conservation, orthant invariance under its donor-limit assumptions, the finite-budget extraction identity, the uniform-drift hitting-time bracket, the power-law curvature formula, and the “minimum is the unique calibrated monotone certifying aggregator” result all check out under their stated conditions. The ECOMOD C17 citation is also unusually precise: its bibliography links directly to the v50 PDF at commit `2efaa62083f2007dec3446c15c475af88f0925f3`. I retrieved that pinned file through the GitHub API; its SHA-256 is `355ab3b7204eabd0cf83aca7933c82e23538514e5b1a7ff8747af333598c88c7`, matching the local v50 PDF. C17 itself appropriately calls the relationship an analogy, not an identity with the material-flow ledger.

**The companion is not ready to support all of its stronger accounting and depletion claims without revision.** Four high-priority issues require mathematical clarification or correction: a use-timescale return deficit is treated as permanent net depletion; a reserve-life crossover applies a small-parameter expansion far outside its range; the residual-budget definition mixes incompatible vector dimensions; and the ledger-composition construction gives two non-equivalent meanings of “identification” while omitting donor limitation for interface fluxes. A further linear-algebra conclusion about conservation across types does not follow from the displayed kernel decomposition. The v50 PDF also contains visible source-to-typesetting defects.

## Audit steps and limits

- Confirmed the ECOMOD C17 `Abaee2026c` reference targets the v50 PDF at the pinned commit. The pinned PDF and the repository's v50 PDF are byte-identical; 54 pages were extracted for inspection.
- Compared the v50 Markdown/TeX with the locally bundled v49 article: the article-body changes are negligible; the visible differences are companion-reference title updates. The full-length Figshare-ready archive and the package checksum list still identify v49, not v50.
- Re-ran `curvature_and_crossover.py` from the full-length v49 deposit. Its output reproduces the v50 reserve-life example but also reproduces the invalid extrapolation described below. Separately evaluated the exact inequality.
- Recomputed the fisheries summaries from the repository's tracked cohort CSVs: 43 rows / 8 zeros / median 1.7902 years; v4.66 broad cohort 454 / 69 zeros / 3.3893 years; v4.44 cohort 415 / 63 zeros / 2.5683 years. These match the reported rounded medians. This checks the CSV arithmetic, not the upstream stock assessments or extraction history.
- Did not retrieve and independently validate the external G3P, USGS, or NFA source data, nor rebuild the PDF: no TeX compiler is installed. The local project metadata and v49 verification records are not evidence of a successful v50 rebuild.

## Findings

### 1. High — Definition 22 turns a finite-lag non-return into permanent depletion

**Location:** §2.1, Definition 22; reused in Proposition 36, Remark 35, and Definition 46.

The definition sets \(\delta_m=1-\kappa_m(\tau_{use};\Theta)\), where \(\kappa_m(\tau)\) is the fraction returned to a usable compartment **within lag** \(\tau\). It then states that sustained mobilisation \(g_m\) produces net support-pool drawdown \(\delta_m g_m\), and gives the frozen-rate horizon \(T\le m_0/(\underline\delta g_m)\).

Not returned *yet* is not equivalent to never returned. For example, a process can return all material after \(2\tau_{use}\): then \(\kappa(\tau_{use})=0\) and the defined deficit is one, although after the initial transit inventory the material can circulate indefinitely with no permanent net loss. The paper itself distinguishes \(\kappa(\tau_{use})\) from \(\kappa(\infty)\), so this is not just a missing interpretation of the word “lag.” In the example, \(m_0/(\delta g_m)\) is not an upper bound on the time to depletion; the pool may never deplete.

**Action:** distinguish a *timing/working-inventory deficit* from an *irrecoverable or permanently unavailable fraction*. For a permanent-loss horizon, define the non-returning fraction over the relevant horizon (or explicitly assume no later return) and state the no-inflow/no-compensation conditions. Otherwise represent the in-transit material and its delayed return in the ledger, and remove the inference \(\delta g_m\Rightarrow\) constant net drawdown and finite exhaustion. Revisit the conclusions of Proposition 36 and Definitions 22/46 that use this inference.

### 2. High — Proposition 28's numerical conclusion extrapolates a first-order approximation beyond its range

**Location:** §6.2 Proposition 28 and §6.5.3; the corresponding arithmetic is in the included `curvature_and_crossover.py` from the v49 deposit.

For \(\dot R=-(1-\eta)P_0e^{gt}\), \(\tau=R_0/P_0\), and \(\eta<1\), the exact condition \(T\ge\tau\), where
\[
T=\frac1g\log\!\left(1+\frac{g\tau}{1-\eta}\right),
\]
is
\[
\eta\ge 1-\frac{x}{e^x-1},\qquad x=g\tau.
\]
The stated \(\eta\ge x/2\) is only a first-order small-\(x\) approximation. The paper plugs in \(x=0.03\times309\approx9.27\), which is not small, and concludes the required \(\eta\) exceeds one and is inadmissible. Using the text's inputs (\(R_0=74{,}000{,}000\) kt, \(P_0=240{,}000\) kt/year, \(g=0.03\)) gives \(\tau=308.33\) years and the **exact** threshold \(\eta\approx0.99911\), which lies within the script's declared admissible range \([0,1]\). At \(\eta=0.99\), \(T\approx227.70\) years; at \(\eta\approx0.99911\), \(T=\tau\); at \(\eta=1\), the model has no finite exhaustion time. The claim that the ratio is optimistic at *every* admissible \(\eta\) is therefore false for this model. The included script tests through 0.99 and repeats the same false threshold conclusion.

There is also a source-vintage inconsistency in §6.5.2–6.5.3. The displayed reserve-life calculation uses production of about 239,482–240,000 kt/year to produce \(\approx309\) years, while the same subsection later says the pinned 2026 source's 2025 world-production figure is about 250,000 kt/year. With 74,000,000 kt reserves, that later figure gives 296 years, not 309. The text labels the re-pin as open, but leaves both values in the current displayed classification.

**Action:** use the exact crossover inequality for the reported parameter values (and define the admissible range and interpretation of \(\eta\)); do not apply the first-order threshold at \(g\tau\approx9\). Reconcile every phosphate table, calculation, and “pinned” source claim to one stated MCS vintage. If the older production value is intentionally retained, identify its year and do not call that calculation pinned to the 2026 production column.

### 3. High — Definition 23's residual equation is dimensionally inconsistent and does not clearly carry the disturbance

**Location:** §3.4, Definition 23.

The text defines \(C\) as the moiety-composition matrix (Lemma 3), with \(C\in\mathbb R^{M\times n}\), but asks for every left-null vector \(\ell\) of \(S_{\mathcal T}\) to satisfy a bound on \(\ell^\top C d_x\). A left-null vector of the \(n\)-row incidence matrix is in state space; multiplying its transpose by the \(M\times n\) matrix \(C\) is not generally dimensionally defined. The displayed follow-up balance similarly uses \(\ell^\top Cx\). If \(\ell\) is instead a moiety-space multiplier, the required null condition is \(\ell^\top C S_{\mathcal T}=0\), not \(\ell^\top S_{\mathcal T}=0\).

Equation (1) separates boundary transfers and disturbance as \(B_{\mathcal T}u_\partial+d_x\); Definition 23 says the disturbance is “carried,” but its displayed balance does not show an explicit disturbance contribution or clearly define it as part of \(b\). This matters because the residual budget is meant to keep unexplained material from being silently treated as conserved.

**Action:** select one consistent formulation. For example, for a moiety-weight vector \(w\in\mathbb R^M\), require \(w^\top C S_{\mathcal T}=0\), bound \(|\int_0^T w^\top C d_x(t)\,dt|\), and write the full identity with \(B_{\mathcal T}u_\partial+d_x\). Alternatively define each conserved state-space covector separately and do not insert \(C\). State explicitly whether \(b\) includes the disturbance.

### 4. High — Definition 34 gives incompatible state semantics for ledger “identification”; interface fluxes are not donor-limited

**Location:** §3.7, Definition 34 and the “Rows” / “Quotient” descriptions; Proposition 36.

The row construction keeps both state coordinates and adds \(x_a^1=x_b^2\). The quotient construction instead defines a class stock with the class-incidence map \(x_C=R x_0\), which **sums** the stocks in that class. These are different operations. If two one-unit stocks are identified, the row form imposes equality and retains a common value of one; the displayed quotient map reports a total of two. The exchange column \(-e_a+e_b\) also cancels under the quotient when its endpoints are merged, but generally moves one row state against the other and breaks the row-form equality. The text claims the constructions coincide on the feasible flux set without a condition that makes these state maps equivalent. Proposition 36's characterization of conserved covectors consequently depends on an unresolved meaning of “identified.”

Further, Definition 34 gives every interface exchange only a fixed box \(0\le f_\varphi\le\bar v_\varphi\). It does not require the outflow to vanish or be limited when its finite donor is empty, despite §2.1's core admissibility rule and the later positivity theorems' reliance on donor limitation.

**Action:** choose and define whether \(J\) merges duplicate descriptions of one physical stock or pools distinct stocks. For a shared stock, use one state coordinate with combined incident fluxes; for pooled stocks, use a sum coordinate without imposing equality of the original stock values. Re-derive Proposition 36 for that construction. Require state-dependent donor limitation on finite-donor interface fluxes, or explicitly classify them as open-boundary fluxes and carry the resulting mass change.

### 5. Moderate — Proposition 42 overstates what its block-kernel identity proves

**Location:** §3.8, Proposition 42 and its proof.

Block-diagonality does imply
\(\ker S_{\mathcal T}^{\top}=\bigoplus_\gamma\ker S_\gamma^{\top}\). It does **not** imply that every left-null vector is supported on only one block or that no conserved scalar can combine blocks. For example, if two disconnected classes each have a conserved total, the sum (and any linear combination) of those two totals is also in the left kernel. Thus “every conservation law … is carried by a single class” and “no conserved quantity … prices one class against another” do not follow from the displayed direct sum. They may be intended to say that no *primitive conversion column* couples classes, or that the stoichiometry does not authorize a physical substitution rate across them; those are narrower claims.

**Action:** state the valid result as a decomposition into class-local conservation bases and distinguish it from an analyst-defined weighted aggregate of separately conserved quantities. The latter may be dimensionally or normatively inadmissible under the type declaration, but its exclusion is an additional typing/valuation rule—not a consequence of the left-kernel equation alone.

### 6. Moderate — The v50 source/PDF contains visible conversion and copy-editing defects; current package records are for v49

**Locations:** `paper3_material_ledgers_v50.tex`, §§2.1, 3.8 and 4.3; `paper3/latest-2026-09-19/CHECKSUMS.sha256`; full-length deposit README/archive.

The pinned v50 PDF is identifiable and byte-stable, but the local project checksum file lists `paper3_material_ledgers_v49.*` and `paper3_supplementary_v18.*`, not the v50 main source/PDF; the full-length deposit README and ZIP likewise identify the source line as v49. The v50 TeX header still says it was “Typeset from … v48.md.” Thus the direct ECOMOD citation is valid, but the broader v50 build/reproduction record does not line up with the v50 source.

The rendered v50 PDF also contains literal `### 3.8` mid-paragraph rather than a subsection heading. The TeX source has escaped Markdown hashes (`\#\#\# 3.8`) instead of a `\\subsection` command. Section 4.3 repeats “Two scope notes are part of the theorem,” repeats the Theorems 7–9 sentence, and then leaves the text ending “differentiated only by which compartments the declaration include 1.” Section 2.1 says “Three things” and then has an orphaned “3.” in the donor-limitation sentence. These defects are visible in the pinned PDF's extracted text, not merely in an editor's raw Markdown.

**Action:** regenerate the v50 TeX/PDF from the v50 source, replace the literal heading with a real subsection, repair the incomplete/duplicated passages and list numbering, update the TeX provenance comment, and add a v50-specific checksum/build record and matching reproduction package. Check the rendered PDF text against the exact v50 source; the existing v49 verification cannot certify it.

### 7. Moderate — “Weak/strong sustainability” is used for two criteria without a proved bridge

**Locations:** Abstract and §1.1; §§10.1 and 11; the ECOMOD C17 paragraph citing §§1.1 and 10.1.

The introduction/abstract describes weak and strong sustainability as operational regimes distinguished by whether material cycles close at throughput. Section 10.1 then describes weak sustainability as a positive weighted-sum/ranking device and strong sustainability as a conjunctive componentwise predicate. Those may be related interpretations, but the paper does not prove that closure at throughput is equivalent to one assessment predicate or the other. C17 mirrors both formulations but wisely calls its relationship an analogy, not an identity.

**Action:** separate the material-cycle closure regime from the weak/strong *assessment* terminology, or provide an explicit definition and result connecting them. C17 should retain its “analogy, not identity” qualification unless that bridge is supplied.

### 8. Low — Proposition 30's positivity condition should refer to the fixed-aggregate feasible slice

**Location:** §10.1, Proposition 30.

For fixed aggregate \(z\), \(\delta_j^*(z)\) is an LP over \(\{b:w^\top b=z,\ell\le b\le u\}\). The statement says it is positive whenever “any admissible \(b\)” has \(b_j<0\), but a negative admissible balance at another aggregate value does not imply that this fixed-\(z\) slice contains one. It should say: positive whenever the feasible slice at the stated \(z\) contains a vector with \(b_j<0\), and defined only when that slice is nonempty.

### 9. Empirical arithmetic check — Fisheries figures reproduce; phosphate figures need reconciliation

Using the three CSVs tracked elsewhere in the repository, the 43-stock archived cohort reproduces the reported zero count and median; the v4.66 and v4.44 broad-cohort row counts and medians also reproduce to printed precision. This supports the arithmetic from those files, not the external assessment data or the historical provenance of the archived pull. The C17/Paper3 deposit does not bundle the 43-row CSV alongside the v50 manuscript; it lives under a separate analysis path in the broader repository, so the paper should identify that exact, versioned location in its reproduction instructions.

The USGS phosphate calculation has the internal vintage discrepancy described in Finding 2. I did not independently confirm either production figure against the external USGS source. The G3P classifications and the National Footprint Account recomputation were likewise inspected for their stated scope, not independently validated from the external source tables.

## Relevance to ECOMOD C17

The companion is a reasonable citation for the *general* typed-ledger and componentwise-assessment framing, and the C17 main text accurately limits the relationship as an analogy. Keep the citation to the pinned v50 artifact. Do not let that broad citation imply that every formal proposition in the companion is established: in particular, the closure-deficit horizon in Definition 22 and the type-class conclusion in Proposition 42 need correction before using them as supporting results. C17's own global-hectare model remains a distinct dynamical construction, not a derivation from the material-ledger equations.

## Bottom line

The C17 citation resolves to the exact v50 PDF, and the reproduced fisheries medians are arithmetically sound on the tracked files. Nevertheless, the cited paper's use-timescale closure deficit does not by itself imply permanent drawdown; its reserve-life crossover conclusion is numerically wrong for its own example; Definition 23 is dimensionally inconsistent as written; and the composition calculus and Proposition 42 overclaim what their equations establish. The v50 PDF also preserves conspicuous build/text defects while its checked package remains v49. Correct these points, refresh the version-specific reproduction record, and clarify the closure-versus-aggregation terminology before relying on the companion for the stronger claims in ECOMOD.

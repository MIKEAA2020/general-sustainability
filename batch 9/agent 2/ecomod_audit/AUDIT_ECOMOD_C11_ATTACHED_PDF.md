# Audit of the attached ECOMOD revision draft (28 October 2026)

**Audited file:** `ecomod_continued_11_revision_draft_20261028 (1).pdf` (35 PDF pages; main text numbered 1–30, followed by references).  
**Audit date:** 2026-10-28.  
**Scope:** Main-paper content, mathematical statements visible in the PDF, cross-paper references, internal numerical/accounting claims, and submission/reproducibility readiness. The PDF did not include the cited Supplementary Information (SI), source `.tex`, run code, or a versioned data/output bundle; SI-dependent calculations therefore could not be verified against this upload. No manuscript edits were made.

## Overall assessment

**Substantial progress; targeted revision still needed before submission.** The revision now demonstrates the central composition-masking trajectory directly, defines the quality ceiling as a projected/admissible model constraint, separates the reduced fixed-demand equality branch from the full delayed trajectories, acknowledges the separate surplus equilibrium family, and narrows the claims about physical stocks. These are meaningful improvements over the issues recorded in the prior C10 audit.

The empirical account decomposition is plausible and consistent with the earlier independent check of the same NFA Edition 2026 workbook: the reported 1961–2023 changes and component contributions agree with that audit to rounding. The main remaining mathematical issue is that Proposition 1(ii)'s maintained maintenance/retirement balance is not an invariant trajectory of the stated land-flow equations during positive conversion. Proposition 1(i) also overstates that balance as a necessary condition for determining the sign of net biocapacity change. A separate dimensional error remains in the optional additive-degradation comparison. Reproducibility is not yet submission-ready because the supplied PDF points repeatedly to an absent SI and says code/data products “will be deposited.”

**Recommendation:** revise these points and provide the complete, version-matched SI and reproducibility package. The headline mechanism and account-series results are not invalidated by the findings below.

## 1. Findings requiring attention

### 1.1 Proposition 1(ii): balanced maintenance and retirement is not preserved during conversion — High

**Location:** PDF pp. 12–13, Proposition 1(ii) and proof; Eqs. (6)–(8).

The proposition's reduced comparison assumes fixed demand and debt, fixed quality, no restoration, and *balanced maintenance and retirement*, \(\mu A_r=\eta_f A_f\). Under the manuscript's actual land flows, when this balance holds and conversion is active,

\[
\dot A_r=-\mu A_r+\eta_f A_f=0,\qquad
\dot A_f=u_c+\mu A_r-\eta_f A_f=u_c.
\]

Consequently,

\[
\frac{d}{dt}(\mu A_r-\eta_f A_f)=-\eta_f u_c<0
\]

for \(u_c>0\) and \(\eta_f>0\). The balance condition therefore fails immediately; it cannot hold over a positive-duration conversion interval under the displayed dynamics. The proof then uses this condition to reduce \(\dot S\) to \(-\Delta b_{\rm conv}u_c\) and infer shortfall closure before the floor.

The current wording calls this a “reduced comparison,” but does not say that the condition requires a counterfactual instantaneous rebalancing rule or a modified flow system. As written, the result can be read as a consequence of the model's stated flows.

**Repair:** either (a) label it explicitly as a counterfactual constrained bookkeeping comparison and state the extra control needed to maintain the balance, or (b) derive the shortfall evolution using the actual affine land subsystem. Under fast/reserve re-equilibration, the effective marginal supply coefficient would generally involve the balanced fast-land share \(k=\mu/(\mu+\eta_f)\), not simply \(b_f-\Upsilon_c\).

### 1.2 Proposition 1(i): “only if” is too strong — Medium

**Location:** PDF p. 12, Proposition 1(i).

Equation (16) decomposes \(\dot B\) into a conversion term, a maintenance/retirement imbalance term, and a quality-change term. The statement that the conversion contribution “determines the sign of net \(\dot B\) only if” the maintenance flows balance and quality is unchanged is not logically necessary: other terms can be nonzero yet have the same sign, or be too small to reverse the conversion contribution.

**Repair:** say that the conversion term alone determines the net sign *when* the other terms vanish; otherwise it is one contribution and the sign depends on their sum.

### 1.3 Optional additive-degradation comparison is dimensionally inconsistent — Medium

**Location:** PDF p. 19, immediately after Proposition 3.

The selected model uses \(b_f=(b_{f0}+T_b)e^{-\alpha D}\), with \(D\) in gha·yr and \(\alpha\) in (gha·yr)\(^{-1}\), so \(\alpha D\) is dimensionless and valid in an exponent. The text then proposes the additive alternative \(b_f=b_{f0}+T_b-\alpha D\) and compares \(\Delta b\) with \(\alpha D^*\). But \(b_{f0}\), \(T_b\), and \(\Delta b\) are in gha·ha\(^{-1}\), whereas this same \(\alpha D\) is dimensionless. It cannot be subtracted from yield or compared with \(\Delta b\).

**Repair:** omit the optional comparison, or introduce a distinct additive degradation coefficient with units of yield per debt unit, and restate the threshold using that coefficient. Do not reuse the exponential coefficient without changing its units and interpretation.

### 1.4 Modelled area/contribution is not a measured physical ecological-stock decline — Medium (interpretive safeguard)

**Locations:** Abstract and results, PDF pp. 1, 13–14, 27–30.

The manuscript correctly says that \(q\) is uncalibrated, the quality ceiling is imposed, and NFA account values do not measure physical stocks. The model result is nevertheless easy to overread because the abstract and title emphasize “ecological-capital land drawdown.” In the reported run, \(q\) rises from 0.9 to its imposed ceiling; the model has no negative quality/degradation term in the \(q\) equation. The reported decline is in the model's capital-land *area* and the modelled annual contribution \(\Upsilon_c(q)A_c\), not a simulated loss of biomass/soil condition or a decline in the quality state. The per-hectare term falls because the logistic regeneration-value function declines above its peak at \(q=q_{\max}/2\), while \(q\) itself rises.

**Repair:** retain the existing caveats, and make this distinction prominent wherever the 46.16% area and 51.72% contribution changes are summarized. Avoid wording that could imply the simulation demonstrates physical ecosystem degradation or a fall in \(q\).

## 2. Reproducibility and publication-readiness

### 2.1 SI-dependent statements cannot be checked from the supplied file

The paper cites numerous SI items for the model's units and parameter definitions, numerical convergence, debt/technology runs, recovery outcomes, NFA sensitivity, and empirical proxy (for example, PDF pp. 9–11, 17–20, 22, and 27). The attachment is a main-paper PDF only. In particular, the reported 149-year mask duration, recovery fraction, delay comparisons, and sensitivity/proxy checks need the associated SI and run records for an independent audit of this revision.

**Action:** supply the exact SI paired to this PDF, and identify a version/commit for the manuscript, SI, source, figures, tables, input data, and generated output. A prior-version SI or source should not be presumed to match this revised draft.

### 2.2 Data/code availability is prospective, not reproducible now

**Location:** PDF p. 30, Data availability.

“All empirical inputs are publicly available” is partly useful, but “Derived analysis data and model code will be deposited” leaves the central simulation and derived tables unavailable at the time described by this manuscript. The article also depends on an explicit projection rule, delay histories/interpolation, Euler update ordering, and state-bound handling, all of which affect reproducibility.

**Action:** replace the future-tense promise with a stable public repository/archive URL or DOI and release/version identifier before submission. Include the exact implementation and scripts that regenerate the displayed trajectories and table values, full parameter and initial-history files, and the data-processing scripts/derived outputs.

### 2.3 Related-work entries need stable retrieval information

**Location:** PDF pp. 31–32, references Abaee (2026a–c).

The assessment companion is cited as a specific working-paper version (v71), which is a useful version cue, and the titles are consistent with the current companion titles checked in the repository. The entries as rendered in the PDF do not provide a DOI or stable URL for these companion manuscripts. Readers cannot reliably retrieve the exact theorem versions cited from “Working paper. Manuscript.” alone.

**Action:** give a stable versioned repository link or archival DOI for each companion citation; preserve the cited version in the record. Check that the cited assessment-paper theorem numbering remains the v71 numbering used in the PDF (Theorem 2 for the witnessed separation; Theorem 4(iii) for the substitutability ladder).

## 3. Checks that pass / substantial improvements

- **Central composition mask is now shown.** Figure 1a and its text explicitly report the frozen-demand trajectory: \(B\) rises from 0.594 to 0.825 gha while \(A_c\) falls from 1.500 to 0.808 ha, with the modelled capital-land contribution falling from 0.08364 to 0.04038 gha. This directly addresses the earlier concern that the paper described but did not display its headline mechanism.
- **Accounting identity and boundaries are clear.** The manuscript distinguishes global-hectare account values from physical stocks and distinguishes its auxiliary cropland/yield proxy residual from modelled capital-land contribution. The 2023 endpoint, per-person, production-footprint, and land-component figures are consistent with the previously independently reproduced NFA Edition 2026 values in the C10 audit package.
- **Bounded quality semantics are materially improved.** Equation (10) now defines a projection onto the tangent cone of the imposed interval and the text specifies an absolutely continuous admissible solution; the ceiling is not presented as an empirically estimated threshold. This addresses the old raw-DDE-versus-numerical-clamp mismatch at the level of model specification.
- **Reduced-branch scope is improved.** Proposition 2 now distinguishes the unique equality-balance point from the fixed-demand surplus/no-conversion equilibrium family, and explicitly limits its deficit-side matrix/eigenvalues to the active-shortfall regime. The manuscript also distinguishes the equality relation from every realised delayed path.
- **Delay-sensitivity language is appropriately narrowed.** The paper explains that the baseline quality path reaches its imposed ceiling at 125/9 years, before the 20- and 40-year delays elapse, and calls their matching paths a saturation-induced degeneracy rather than general delay robustness.
- **Recovery discrepancy addressed in the main text.** The supplied PDF reports the approximately 0.677-ha endpoint and 0.46 recovery fraction for the stated 400-year scenario, consistent with the value identified as the SI-scale result in the C10 audit. The SI for this revision is still needed to verify the paired table and exact run.
- **Physical-stock claims are appropriately limited.** The conclusion explicitly states that no common-boundary global physical-stock series was assembled and makes no composite/global physical-stock decline finding. Built-up land is correctly kept as an NFA accounting category, not ecological capital.
- **Weak/strong and companion framing is restrained.** The relation-to-prior-work section calls the ledger link an analogy about compensation, not an identity or complete sustainability classification; it also distinguishes ecological/demographic delays from institutional review. The companion assessment citation accurately describes the finite-plan setting rather than claiming it proves the ECOMOD dynamics.

## 4. Bottom line

The revised paper now supports its central, conditional model illustration and is notably more careful about what aggregate NFA data can and cannot establish. The principal mathematical repair still needed is to stop Proposition 1(ii) from presenting a non-invariant maintenance/retirement balance as though it were a trajectory of the stated flow model. Correct the “only if” wording in Proposition 1(i), fix or remove the dimensionally inconsistent additive-degradation aside, and provide the version-matched SI and reproducible source package. With those changes, the remaining concerns are largely qualification, traceability, and publication presentation rather than a rejection of the main account-composition result.

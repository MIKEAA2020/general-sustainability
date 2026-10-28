# Audit of `ecomod_continued_11_revision_draft_20261028_2.txt`

**Audited item:** main-manuscript LaTeX source (555 lines; 10,904 words).  
**Related supplied files:** the earlier same-date main PDF `ecomod_continued_11_revision_draft_20261028 (1).pdf` and SI source `ecomod_continued_11_revision_draft_20261028_SI.txt`.  
**Audit date:** 2026-10-28.  
**Scope:** source-level mathematical and numerical claims, citation/key consistency, and consistency with the two earlier attachments. No manuscript files were modified. This source-only audit does not certify a compiled PDF or independently rerun the simulations.

## Overall assessment

**The main source is materially improved and corrects several findings in the earlier PDF, but the supplied files are not a version-matched manuscript package.** The revised source now explicitly limits Proposition 1(ii) to a pointwise comparison and says its maintenance/retirement balance is not invariant during conversion; it fixes the “only if” overstatement in Proposition 1(i), narrows finite-grid continuity claims, and correctly qualifies the claim about total-B-only control. It also introduces a separate, dimensionally appropriate coefficient for its optional additive-degradation comparator and adds versioned links for the companion manuscripts.

Those improvements are **not present in the earlier supplied PDF**, so that PDF must not be treated as a rendering of this source. The SI supplied earlier also remains behind the source in several places. One small numerical rounding error remains in the source: the reported composition diagnostic at \(q=0.6\) should round to +0.785, not +0.784, with the stated baseline values.

The core composition-mask illustration and NFA accounting remain credible and appropriately caveated. The remaining work is principally to synchronize/rebuild the deliverables, reconcile SI details, and publish the reproducibility bundle.

## 1. Material source/PDF version mismatch — High

The supplied PDF and this source are not the same revision. The source contains material edits not reflected in the PDF, including:

- **Proposition 1(i)–(ii):** source lines 222–229 now says the sign conditions are sufficient rather than necessary, derives \(\dot M=-(\mu+\eta_f)M-\eta_fu_c\), explicitly states \(M=0\) is not invariant during conversion, and disclaims shortfall closure/floor arrival from the pointwise comparison. The PDF (pp. 12–13) instead states the maintained-balance comparison can close the shortfall before the floor.
- **Figure 1(c)/drawdown claims:** source lines 248, 288, 296 confines monotonicity to tested samples and says the finite grid/bisections do not establish continuity. The PDF's caption/text (pp. 14, 17) describes the minimum area as varying continuously and monotonically.
- **Control claim:** source line 464 gives the forward-invariance bound and explicitly rejects a universal output-only control impossibility. The PDF (p. 28) still states that a heuristic based only on total \(B\) cannot guarantee the floor.
- **Additive-degradation comparator:** source lines 335–339 uses a separate \(\alpha_{\rm add}\); the PDF (p. 19) reuses the multiplicative \(\alpha\), which is dimensionally invalid.
- **Companion references:** source lines 508–510 include stable versioned manuscript links; the earlier PDF's bibliography does not show those links.

These are substantive mathematical and interpretive differences, not just source formatting. **Action:** compile a new PDF from this exact source with the matching SI, graphics, and data/code bundle; then inspect and audit that rendered PDF. Do not submit the previous PDF alongside this source.

## 2. Checks that now pass in the new main source

- **Proposition 1(i):** source line 222 now says the vanishing of other terms is sufficient, not necessary, to let the conversion term determine the net sign.
- **Proposition 1(ii):** source lines 223 and 229 correctly establish a pointwise derivative result while disclaiming that the balanced condition persists or implies eventual closure. The calculation for \(\dot M\) matches the stated land-flow equations.
- **Observation/identification scope:** source line 224 separates identification from the static supply observation relation from possible dynamic identification using a calibrated quality time series and known delay/history.
- **Drawdown scans:** source lines 288, 296 appropriately describe finite sampled monotonicity/proximity and do not promote it to a general continuity theorem.
- **Typed-floor policy:** source line 464 correctly derives \(y(t)\ge y(0)e^{-t/\tau_{\rm conv}}\) from \(0\le u_c\le y/\tau_{\rm conv}\) and \(R_{rc}\ge0\). It distinguishes non-identification of \(A_c\) from a universal impossibility result and recognizes no-conversion as a robust counterexample.
- **Additive comparator in the main source:** source line 335's \(\alpha_{\rm add}\) units, ha\(^{-1}\)yr\(^{-1}\), make \(\alpha_{\rm add}D\) a yield in gha\,ha\(^{-1}\), as required. This fix must also be carried into the SI.
- **Debt statement:** source lines 331–342 gives the finite-time comparison with \(D(0)\) and frames \(S^\dagger\) as an asymptotic, sustained-shortfall crossover rather than a transient threshold.
- **Related-work citation traceability:** the source's Abaee 2026a/b/c entries link to versioned manuscript PDFs; the cited v71 theorem numbering checked against the repository is consistent.
- **Citation integrity:** a source scan found 45 cited keys and 45 bibliography keys, with no missing/uncited keys or duplicate labels/bib keys.

## 3. Findings still to address

### 3.1 Main source and supplied SI are out of sync — High

**Additive-degradation law.** The new main source uses \(\alpha_{\rm add}\), but the supplied SI §S2.5 still writes \(b_f=b_{f0}+T_b-\alpha D\) and compares \(\Delta b\) with \(\alpha D^*\). That is dimensionally invalid for the SI's \(\alpha\) units, as detailed in [`AUDIT_ECOMOD_C11_SI_ATTACHED.txt.md`](AUDIT_ECOMOD_C11_SI_ATTACHED.txt.md). Carry the main-source correction into the SI, or remove the optional alternative from both.

**Reserve and fast-land constraints.** The source parameter table and numerical section (around lines 173–201) call \(A_r^{\min}=0.10\) ha a monitoring threshold that is not enforced, and say \(A_f^{\max}\) is not imposed in reported runs. The supplied SI §S1 and §S6 instead describe the reserve floor and fast-land ceiling as imposed domain/typed constraints and say bounds are enforced. Align the SI with the actual update and disclose which constraints are monitored, enforced, inactive, or merely named. Do not call \(A_r^{\min}\) an enforced floor if the simulator only monitors it.

**Debt bound.** The source's main proposition now correctly retains \(D(0)\), but the supplied SI §S2.5 still infers a debt-channel loss bound of \(-\alpha\bar S/\eta\) after stating \(D(t)\le\max\{D(0),\bar S/\eta\}\). That inference omits the initial-debt case. Update the SI as recommended in its audit report.

**Recovery evidence.** The source's parameter-grounding paragraph (line 141) says no common recovery curve is refit and no harmonized \(t_{50}\) or \(\tau_r\) values are computed. The supplied SI §S5.5 nevertheless reports fitted median \(t_{50}\) and \(\tau_r\) values for forest and fish records (including 35 selected forest fits and 33 stocks). Clarify that these are separate, system-specific reanalyses rather than harmonized estimates—or remove the fit summaries from the SI. In either case, supply the fit equation, selection rules, data/record identifiers, censoring treatment, uncertainty, and code; the current SI does not make those numerical summaries reproducible.

### 3.2 Composition-diagnostic rounding — Minor

**Location:** source line 214.

With the displayed baseline values \(b_{f0}=0.85\), \(b_c=0.05\), \(b_{G,c}=0.8\), \(\rho_c=0.08\), and \(q_{\max}=1\), at \(q=0.6\):

\[
G_c(0.6)=0.08(0.6)(1-0.6)=0.0192,\qquad
\Upsilon_c(0.6)=0.05+0.8(0.0192)=0.06536,
\]

so \(\Delta b_{\rm conv}=0.85-0.06536=0.78464\), which rounds to **+0.785** at three decimals, not +0.784. The reported +0.784 is correct at \(q=q^*=0.5\), as shown in Table 2(a), suggesting a rounding/truncation or copy error in the three-point sentence.

**Repair:** change +0.784 to +0.785, or state values to enough digits and use a consistent rounding convention.

### 3.3 Empirical code/data availability remains prospective — Medium

**Location:** source line 498.

The declaration still says derived data and model code “will be deposited.” For the simulated results, exact reproducibility depends on the projection rule, delay interpolation and timing, Euler update order, initial histories, and state-bound handling. The source also points to a full drawdown grid and numerous SI-dependent results.

**Action:** before submission, replace the future-tense promise with a stable archive/repository release and DOI or commit; include the exact simulator, scripts, versioned inputs, derived CSVs, and figure-generating code. Pair them with the exact SI and final PDF.

### 3.4 Acknowledgments should be fact-checked — Minor/editorial

**Location:** source lines 492–494.

The acknowledgments name Mathis Wackernagel as providing a “thoughtful review” and thank the journal editors for “their trust and support.” Retain these statements only if they accurately describe assistance, any required permission has been obtained, and the journal's review/anonymization process permits such acknowledgments. This is a verification request, not an allegation that the statements are inaccurate.

## 4. Bottom line

This source is a meaningful revision: it fixes the central Proposition 1 interpretation, the false continuity inference from a finite grid, the output-only control overclaim, and the additive coefficient in the main manuscript. The earlier PDF does not contain those fixes, and the supplied SI has not yet been synchronized with the corrected source. The main remaining priorities are: (1) build and verify a new PDF from this source; (2) update SI sections on additive degradation, state constraints, and finite-time debt bounds; (3) reconcile/document the recovery-fit summaries; and (4) publish the version-matched data and code. Once these are done, the remaining source-level issue identified here is the minor \(q=0.6\) rounding correction.

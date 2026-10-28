# Audit of `ecomod_continued_11_revision_draft_20261028_SI_2.txt`

**Audited item:** SI LaTeX source (580 lines; 8,830 words).  
**Paired source reviewed:** `ecomod_continued_11_revision_draft_20261028_2.txt`; see [`AUDIT_ECOMOD_C11_MAIN_SOURCE2.md`](AUDIT_ECOMOD_C11_MAIN_SOURCE2.md).  
**Earlier PDF:** `ecomod_continued_11_revision_draft_20261028 (1).pdf` is an older rendering and is not synchronized with the latest main source/SI.  
**Audit date:** 2026-10-28.  
**Scope:** SI source, mathematical statements and numerical summaries, cross-document consistency, citations, and packaging. The five named one-stock figure assets were not supplied; I did not compile the SI or independently rerun its simulations.

## Overall assessment

**This SI revision resolves most of the specific findings from the earlier SI audit and aligns substantially better with the revised main source.** It now uses a distinct, correctly dimensioned \(\alpha_{\rm add}\) for the additive comparator; retains \(D(0)\) in the finite-time debt bound; correctly distinguishes the reserve monitoring threshold from an enforced state constraint; softens the control-impossibility claim; removes unsupported, newly fitted regeneration summaries; and removes the duplicated S8 paragraph. Citation keys and labels are internally consistent.

One material specification gap remains in the gate-sign experiment: the stated initial state omits \(D_0\), and its stated population and land values imply an initial shortfall, not the described \(R_B=1\) degraded equilibrium. That distinction may be intentional—the deficit-gated rule should initially be active and the surplus-gated rule inactive—but it needs to be stated and the full initial condition supplied. A smaller interpretive wording issue remains where the SI says the capital contribution is “unaffected” by technology/debt without limiting that to direct effects at fixed \(A_c,q\).

The content is improved, but the supplied main PDF still predates the matching main/SI source revisions; a new paired build and final PDF review are needed.

## 1. Findings requiring attention

### 1.1 Gate-sign experiment: initial condition is incomplete and not the stated equilibrium — Medium

**Location:** SI §S4, “Gate-sign phase dependence” (around line 268), and Table S4.

The experiment says it starts with \(A_c=0.058\) ha, \(A_f=0.6\) ha, \(q=0.9\), and \(P=1.2\) cap, but does not state the initial debt \(D_0\). The debt state affects \(b_f=(b_{f0}+T_b)e^{-\alpha D}\), and therefore affects both initial supply and the reported peak debt. The initial reserve is derivable as 1.842 ha from area conservation, but \(D_0\) is not.

Using the stated baseline parameters and \(T_b=0\), even at the largest admissible fast-land yield (\(D_0=0\)),

\[
B_0=0.85(0.6)+\bigl[0.05+0.8(0.08)(0.9)(0.1)\bigr](0.058)
=0.513234\ \mathrm{gha},
\]

whereas \(E_0=eP_0=0.55(1.2)=0.66\) gha. Thus the listed start is in shortfall (\(S_0\ge0.146766\) gha for \(D_0\ge0\)); it is not an \(R_B=E/B=1\) equilibrium. The sentence “At the degraded equilibrium, \(R_B=1\) and \(B=E\)” may refer to a separate reference state, but the distinction from the actual starting state is not explicit. The different initial gate activations appear central to this comparison.

**Repair:** state the complete initial vector, including \(D_0\), and any histories. Label the \(R_B=1\) degraded equilibrium as a separate reference/equilibrium if that is what is intended. Explicitly say that the gate simulations start in shortfall (if so), with deficit-gated restoration initially active and surplus-gated restoration initially inactive. This would make the comparison and its recovery denominator easier to interpret and reproduce.

### 1.2 Direct versus indirect effect of technology/debt on capital contribution — Minor

**Location:** SI §S2.5, sentence following the debt/log-yield comparison (around line 166).

The SI says that \(Y_f=b_fA_f\) has the two-channel structure while the capital contribution \(\Upsilon_cA_c\) “is unaffected by either.” The capital contribution has no *direct* dependence on the technology/debt yield factor at fixed \(A_c,q\), but those changes affect aggregate \(B\), demand/shortfall, and consequently the land dynamics; \(A_c\) can change indirectly. The unqualified “unaffected” can be read as a statement about the trajectory rather than the functional form.

**Repair:** say “has no direct dependence on the technology/debt yield factor at fixed \(A_c,q\); indirect effects through the coupled dynamics remain possible.”

## 2. Version-matching and reproducibility

### 2.1 SI and new main source are substantially aligned; the old PDF is not

The SI now matches the main source's corrections on \(\alpha_{\rm add}\), the non-enforced reserve monitoring threshold, the control/floor scope, and the absence of new harmonized recovery fits. However, the only supplied PDF is the earlier draft. It retains old statements on Proposition 1, finite-grid continuity, the reserve/control treatment, and the additive coefficient. It must not be circulated as the rendering of the new source/SI.

**Action:** compile a new PDF from the exact paired main and SI sources, with the correct figure assets, and inspect that PDF. Include a version identifier or manifest connecting the PDF, main `.tex`, SI, figures, CSVs, code, and input data.

### 2.2 Missing figure assets prevent a standalone build/visual audit

This SI source references `si_onestock_full_trajectory`, `si_onestock_mask_window`, `si_onestock_delay_examples`, `si_onestock_basin`, and `fig_tb_wave_debt`. The last name exists in a prior v44 package in the repository, but not as part of the attached SI package, and the other four named assets were not found in the repository search. Their contents and correspondence to the captions could not be checked. The SI also refers to `si_drawdown_depth.csv`; no matching C11-specific versioned data bundle was attached.

**Action:** supply the exact figures and CSV used for this revision (not just similarly named prior-version assets), plus the source scripts that generate them. Confirm all figure dimensions, legends, time windows, and numerical annotations against the final PDF.

### 2.3 Data/code availability remains a main-paper issue

The main source still says derived data and code “will be deposited.” The corrected SI now specifies more carefully how states, projections, and monitoring work, but does not itself provide a reproducible release. The gate experiment in particular needs its missing initial debt/history recorded.

**Action:** use a stable public archive/repository URL or DOI and include the exact solver, initial states/histories, parameter dictionary, CSV outputs, figures, and data-processing code before submission.

## 3. Resolved findings / checks that now pass

- **Debt comparison:** SI §S2.5 now retains \(D(0)\) in the finite-time bound, gives the lower bound \(-\alpha\max\{D(0),\bar S/\eta\}\), and limits equality with the technology log gain to the sustained-shortfall asymptotic case. This repairs the earlier omission.
- **Additive comparator:** the SI now uses distinct \(\alpha_{\rm add}\) with units ha\(^{-1}\)yr\(^{-1}\), and distinguishes it from multiplicative \(\alpha\). This agrees with the revised main source.
- **State constraints:** the conventions and policy section now say that \(A_r^{\min}=0.10\) ha is monitored post hoc, not enforced or invariant; they disclose tested minimum-reserve values and correctly say these finite checks do not prove invariance. They also say \(A_f^{\max}\) is not imposed in reported runs, in line with the main source.
- **Control scope:** the SI no longer claims that total-\(B\)-only control is universally unable to preserve the capital-area floor; it gives the same continuous-time floor bound as the new main source and distinguishes information limits from control impossibility.
- **Recovery anchors:** the SI no longer reports the previous original fit summaries for forest/fish \(t_{50}\) and \(\tau_r\). It now states that no common or harmonized fit was performed, consistent with the revised main source.
- **Duplicate text:** the S8 opening paragraph is no longer duplicated.
- **Recovery table:** the \(P_0=2.0\) scenario still reports \(A_c(400)=0.677\) ha and \(\mathcal R_c=0.46\), matching the revised main source. The gate table now distinguishes its recovery report times (100 and 900 yr) from its final-state horizon (2,000 yr).
- **Model qualification:** projected quality-bound semantics, delay scope, reserve-area handling, physical-stock caveats, and the non-identification of model states from NFA accounts remain clearly described.
- **LaTeX text consistency scan:** all 12 citation keys resolve to bibliography entries; no uncited bibliography items, missing keys, duplicate labels, or exact duplicate paragraphs were found.

## 4. Bottom line

The update closes most of the prior SI audit findings and is much better aligned with the new main source. The main remaining content correction is to give a complete gate-sign initial condition and distinguish its shortfall start from the separate degraded equilibrium used as a reference. Clarify that technology/debt have no *direct* effect on capital contribution only at fixed land/quality states. Then provide the exact figures/data/code and rebuild the stale PDF from the paired sources. No new result here overturns the main paper's conditional composition-mask mechanism or the account-only interpretation of the NFA series.

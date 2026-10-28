# ECOMOD continued 12 — revision record

**Date:** 2026-10-28  
**Base main source:** attached `ecomod_continued_11_revision_draft_20261028_2.txt`  
**Base SI source:** attached `ecomod_continued_11_revision_draft_20261028_SI_2.txt`  
**New source files:**
- `ecomod_continued_12_revision_draft_20261028.tex`
- `ecomod_continued_12_revision_draft_20261028_SI.tex`

## Applied corrections

### Main manuscript

- Corrected the composition diagnostic at \(q=0.6\) from `+0.784` to `+0.785` when rounded to three decimal places under the stated baseline parameters.
- Retained the updated main-source corrections already present in the selected base: Proposition 1(i)'s sufficient/not-necessary qualification; Proposition 1(ii)'s pointwise scope and explicit non-invariance of the maintenance balance; the finite-grid qualification on monotonicity/continuity; the typed-floor forward bound and narrowed control claim; and the dimensionally distinct additive coefficient \(\alpha_{\rm add}\).

### Supplementary Information

- Reworded the capital-contribution sentence to distinguish the absence of a **direct** technology/debt yield effect at fixed \(A_c,q\) from possible indirect effects through coupled dynamics.
- Completed the gate-sign experiment's initial condition with \(D_0=0\), the area-conserving reserve, the computed initial \(B_0\), \(E_0\), shortfall and \(R_B\). Clarified that this is a non-equilibrium post-drawdown start—not the separate degraded equilibrium—and identified which restoration gate is initially active.
- The chosen \(D_0=0\) is confirmed by the repository's prior gate-validation implementation (`agent 2 productivity illusion/manuscript_ECOMOD_v44_src/work/recovery_metric_and_tau_p_scan.py`), which initializes the debt array to zero and reproduces the reported gate table. The initial account calculation uses only the stated model equations and parameter values.
- Retained the SI base's corrections to the finite-time debt bound, additive-comparator units, reserve monitoring versus enforced state constraints, control-impossibility scope, and regeneration-anchor reporting.

## Validation and limitations

- Exact-match checks confirmed that the intended main and SI edits were applied once.
- Citation keys, bibliography keys, labels, and duplicated paragraphs were scanned in the SI; no missing citation keys, duplicate labels, or exact duplicate paragraphs were found.
- The initial gate-state arithmetic was checked: \(A_r=2.5-0.6-0.058=1.842\) ha; \(B_0=0.51323408\) gha; \(E_0=0.660\) gha; \(S_0=0.14676592\) gha; and \(R_B=1.2859629\).
- **No new PDF was built.** The attached sources do not include the exact C12 graphics bundle; four referenced one-stock figure assets are missing from the workspace, and no TeX compiler is available. The previous C11 PDF is not a rendering of the C12 sources and should not be paired with them. Compile and visually check the PDF when the matching graphics and build environment are available.
- This is a source revision, not a data/model rerun. Existing simulation tables and figures were not regenerated; the gate-start clarifications document the initial condition used by the earlier validation script.

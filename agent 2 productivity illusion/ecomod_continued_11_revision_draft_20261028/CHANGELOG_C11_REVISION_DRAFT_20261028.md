# ECOMOD Continued 11 — local revision change log

**Date:** 2026-10-28  
**Canonical package:** `agent 2 productivity illusion/ecomod_continued_11_revision_draft_20261028/`  
**Predecessor:** archived ECOMOD Continued 10 (C10).  
**Release state:** separate draft snapshot pushed on branch `agent/p06-ecomod-c11-local-draft-20261028`; no DOI deposit or publication.

## Source-lineage correction

An earlier C11 attempt used the old v45 working-tree TeX as its source throughout. That attempt was not merely mislabeled. It is preserved in the pushed branch at `agent 2 productivity illusion/ecomod_continued_11_misbased_v45_superseded_20261028/` and is **superseded**; its duplicate workspace copy was removed after byte verification. The canonical C11 main and SI were rebuilt from the actual assembled C10 files listed in `README.md`, then split into the modular sources under `parts/`. `C11_REBASE_DIFF_vs_ASSEMBLED_C10_20261028.patch` records the full source diff. The original v45 package and archived C10/C8/C9 artifacts remain unchanged.

The v45 solver remains relevant only as part of the separately documented producer-package/implementation comparison. It is not the manuscript/SI base. Fresh C11 simulation outputs generated after the rebase are identified separately from the archived C10 results; no matching number or plot is treated as proof of the historical C10 run path.

## Model choice and scientific corrections

- Selected the projected delayed-quality law explicitly: `K_q=[0,q_max]`, `q_dot=Pi_{T_{K_q}(q(t))} G_c(q(t-tau_g))`, and `G_c(x)=rho_c x(1-x/q_max)`, with admissible continuous history. Clarified that `q` is uncalibrated/model-defined, `q_max=1` is an imposed bound, and `rho_c`/`tau_g` are scenario parameters. The current-quality and smooth alternatives are not selected models.
- Documented the local discrete implementation comparison and timestep-refinement tests in their actual scope. They establish a same-grid equality for tested cases and decreasing errors under refinement; they are not a global error bound or proof of which historical code produced every C10 result.
- Reframed the baseline `tau_g=20/40` comparison as saturation-induced degeneracy: for `q(s)=0.9`, `rho_c=0.08`, and `q_max=1`, both paths reach the imposed ceiling at `125/9 ≈ 13.8889 yr`, before either delay elapses. The `tau_g=5` case is distinct; no general delay-robustness claim is made.
- Removed the Hutchinson `r tau_p < pi/2` stability classification because the written population equation delays carrying capacity, not population in its crowding term. The SI now states the scalar perturbation equation and explicitly declines a full coupled characteristic-root classification.
- Corrected the deficit-side debt Jacobian to include `alpha b_f A_f - eta` in `partial D_dot/partial D`; limited the spectrum to the stated one-sided deficit-active branch.
- Separated the unique equality point on `B_eq(A_c)=E` from the fixed-demand no-conversion surplus family (`B_eq >= E`) and from the endogenous-population equality family. The switched deficit-side spectrum is not presented as two-sided stability of an isolated equality point.
- Corrected the delayed-quality recovery result to `A_c(T)=0.677 ha` and recovery fraction `0.46`, matching the SI recovery table at `T=400 yr` and `dt=0.1 yr`.
- Treated NFA values as account values, not physical-stock measurements; kept the auxiliary cropland proxy and external ecosystem studies from being presented as ECOMOD validation or parameter calibration.

## Revised-run outputs and historical C10 provenance

- Regenerated Figure 1 and the drawdown CSV using the projected solver. The Figure 1 PNG and drawdown CSV are byte-identical to the archived values; regenerating them is a revised-run check, not a C10 historical source-to-output proof.
- Regenerated SI Tables S4/S5 from the projected-run CSV. The table fragments match the C10 displayed bodies byte-for-byte; the recovery row for `P0=2.0 cap` gives `0.677 ha` and `0.46`.
- Regenerated the SI delay/current-quality sensitivity table with a fresh script using projected delayed quality and a current-quality comparator. It reproduces displayed precision; the exact historical run path for C10 Table S2 remains unresolved.
- Retained the other C10 content/figures and source structure where unrelated. NFA figures/accounting work are not interpreted as simulation calibration or validation.
- The separate historical C10 provenance report remains controlling for unresolved run-to-output links, including the original full SI Table S2 sensitivity sweep and high-resolution main Table 2(b) bisection.

## Assembly and QA

- Assembled main and SI from modular sources; SI table fragments are inlined by `assemble.py`.
- `check_c11_sources.py` passes the assembled/module synchronization, labels/references, citations, brace/environment balance, and revision-regression checks.
- Compiled main and SI in three pdfLaTeX passes each: 35-page main and 21-page SI. Visual review covered the title/abstract, projected-law equations, Figure 1, NFA figures/table, balance proposition/table, discussion/conclusions, SI symbols/spectrum/debt derivative, SI delay sensitivity, drawdown/recovery tables, and post-layout page flow.
- No unresolved references/citations or overfull boxes remain. Nonfatal `hyperref` warnings come from the C10 author/corresponding-author title-footnote tokens; remaining underfull boxes are in dense tables/bibliographic lines. See `output_revision_projected/` and `validation/ECOMOD_C11_REBASE_BUILD_CHECK_20261028.md`.
- Current C11 deliverable hashes are in `SHA256SUMS_C11_LOCAL_20261028.txt`. This new local manifest does not refresh any v45 or archived C10 checksum file.

## Final title, submission-text, and contact-link cleanup (2026-10-28)

- Restored the exact title from the authoritative assembled C10 main and SI; no replacement title was invented.
- Re-audited assembled main/SI visible text for stale version labels, rebase/build narration, and change-log language; removed remaining internal wording from journal-facing text while retaining substantive limitations and provenance distinctions.
- Added clickable `mailto:` and ORCID links in both C11 main and SI; the missing SI ORCID is now present.
- Strengthened the source checker to reject the superseded title, require both links separately in main and SI, and detect internal lineage/provenance phrases.
- Reassembled and rebuilt both documents with three pdfLaTeX passes each. Final page counts are 35 (main) and 21 (SI), with no unresolved citations/references or overfull boxes. `mutool` confirms the expected email and ORCID URI annotations in both PDFs.

## Immutable boundary

This change log applies only to the separate C11 local draft. Archived C10, C8/C9, `main`, pins, checksums, and DOI deposits were not modified. The branch push stores this draft only; no DOI deposit or publication was made. Archived C10/C8/C9 and repository `main` were not modified.
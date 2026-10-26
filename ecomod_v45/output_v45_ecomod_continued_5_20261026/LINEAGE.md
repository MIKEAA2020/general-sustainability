# Ecomod continuation 5 — lineage and verification

Date of this derivative: 2026-10-26 (local)

## Lineage

Continuation 5 is a new derivative of the continuation-4 main manuscript, SI, and figure assets. It lives in this separate directory; continuation 4 and all earlier directories were left unchanged. The earlier choice of the 35-page text as a working base was made on comparative merits only. This derivative does not claim that the 35-page text is a verified or finalized replacement for the 33-page file, or that every useful element across all versions has been reconciled.

The prose revision used the following audit/style references as concrete revision targets, not as factual authorities:

- `/home/user/uploads/ecomod humanized.txt`
- `/home/user/uploads/DeepSeek_Orchard-metaphor-biocapacity_20261024-1656.txt`

## Revision scope

- Substantively rewrote prose across both the main paper and SI. The main revision includes the abstract, introduction, model/evidence explanations, numerical-method prose, Results, Discussion, limitations, conclusions, and selected captions. The Results rewrite makes the per-hectare conversion diagnostic, baseline composition mask and time course, fixed-demand ceiling/floor result, debt and technology comparison, recovery result, NFA account composition, crop proxy, and finite testable implications more explicit.
- Reworked SI explanations of units, model identity, numerical methods, sensitivity and drawdown results, recovery/restoration gates, NFA-account interpretation, regeneration timescale context, the physical-stock scoreboard, and the one-stock comparator.
- Added SI Section S9, a finite demographic-delay scan, plus Table S14 (selected trajectory-window population ranges) and Table S15 (selected two-land reference values). These are descriptive finite-run/model values, not general stability results or observed physical-stock measurements.
- Reordered the NFA account narrative ahead of its figure/table floats and kept the crop-area/yield proxy paragraph together to remove a split-sentence layout defect. This is a layout change only; the values and wording of the proxy calculation were preserved.
- Preserved the equations, propositions, model and empirical numerical results, citation-key set, and figure/table data. Main figure/table/equation environment counts match continuation 4. The SI has two additional tables, S14 and S15; its existing figure and equation counts are unchanged. The Table S4 source block was checked against continuation 4 and is exactly unchanged.
- Kept the key safeguards explicit: conditional model outcomes are distinct from NFA accounting values; NFA values are not physical-stock measurements; no unsupported causal, ecological-collapse, universal, or policy claims were introduced. The crop proxy remains illustrative, not a physical-stock attribution.
- Preserved the citation-key mapping `Abaee2026a` = governance/Paper4, `Abaee2026b` = assessment/Paper06, and `Abaee2026c` = ledger/Paper3. Paper06 v71 Theorem 4(iii) is described only for its witness-defined diagonal-gap region. The ECOMOD Paper3 citation remains pinned to commit `2efaa62083f2007dec3446c15c475af88f0925f3`; its v50/README/checksum/header discrepancy note was retained and no pin was retargeted.

## Build and checks

- Built `ecomod_continued_5.pdf` (32 pages) and `ecomod_continued_5_SI.pdf` (23 pages) with Tectonic 0.17.0. Both builds completed successfully.
- Extracted text from both PDFs. No unresolved-reference markers or `??` placeholders were found. The SI numbering for Tables S13–S15 and Section S9 was checked in the rendered PDF.
- Source preflight found 44 unique labels in the main file and 48 in the SI, with no duplicate labels, missing in-file references, environment-balance errors, or missing figure assets. The citation-key sets match continuation 4. The ORCID hyperlink is present in the main PDF.
- Visually inspected representative pages from the main PDF (including the abstract, model results, empirical figures/tables, revised NFA flow, Discussion, Conclusions, and references) and SI (including the opening symbols page, model/numerical material, SI results tables, regeneration/physical-stock discussion, and Section S9 tables). No material clipping or cross-reference/layout defects were found in the reviewed pages.
- The build logs contain non-fatal overfull/underfull box warnings; no fatal build, undefined citation, or unresolved-reference warning was found.

## Preservation and distribution

No package was created. No checksum manifest was created, edited, or refreshed. No prior verified directory was replaced. No remote push was made: the workspace has no Git repository, and the GitHub connector is unsupported in this session. Nothing was pushed to `main`.

## Files

- Main source: `ecomod_continued_5.tex`
- Main PDF: `ecomod_continued_5.pdf`
- SI source: `ecomod_continued_5_SI.tex`
- SI PDF: `ecomod_continued_5_SI.pdf`
- Build logs: `ecomod_continued_5_build.log`, `ecomod_continued_5_SI_build.log`
- Figure assets: `figures/`, plus `fig2_nfa_aggregation_face.png` and `fig3_composition_attribution.png`
- This lineage record: `LINEAGE.md`

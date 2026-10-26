# ECOMOD continuation 4 — lineage and verification

Date of this derivative: 2026-10-26 (local)

## Lineage

Continuation 4 is a separate derivative of the verified continuation-3 main manuscript and Supplementary Information (SI). The source files, PDFs, logs, and directories from continuation 3 and all earlier versions were left unchanged. The supplied style guide, `/home/user/uploads/ecomod humanized.txt`, informed a multi-pass prose revision of both the main paper and SI.

## Revision scope

- Reworked prose across the abstract, introduction, model description, methods, results, discussion, limitations, conclusions, SI explanations, and selected figure/table captions for clarity and flow.
- Clarified that model debt `D` is a leaky state driven by the aggregate deficit `E-B`; refined the description of the fish-stock comparison to stocks “classified as collapsed”; reviewed the fixed-quality wording; and repaired the Methods/Results section breaks.
- Corrected the conversion-rate symbol in main-text equation `eq:uc` from `\nu_c` to `u_c`, consistent with the equation’s definition, surrounding equations, and SI notation.
- Preserved the distinction between conditional model results and observed NFA account values, and retained the qualifications against interpreting account movements as physical-stock change.
- Preserved the equations, model/data values, numerical results, tables, figures, citations, and cross-reference labels. Citation occurrence counts, reference-label order, and figure/table environment counts match continuation 3. Caption wording was edited without changing the reported numerical values.
- Retained the Paper3 pin and its accurate metadata note; no citation-key mappings were changed.

## Build and checks

- Built `ecomod_continued_4.pdf` (34 pages) and `ecomod_continued_4_SI.pdf` (22 pages) with Tectonic 0.17.0, using reruns for references.
- Both builds completed successfully. PDF text extraction showed no unresolved-reference markers; the build logs contain non-fatal overfull/underfull box warnings only.
- Visually inspected representative pages from both PDFs, including title/abstract and introduction pages, the revised main figure/table captions, the Results and Conclusions, the SI symbols/model-extensions pages, and SI figures.
- Confirmed the ORCID hyperlink is active in both PDFs. Confirmed the main equation renders with `u_c`, the section breaks are present, and the “At fixed quality” phrasing has been replaced with a clearer statement about a given quality level.

## Preservation and distribution

No package was created. No checksum manifest was refreshed or edited. No prior verified directory was replaced. No remote push was made: the available workspace is not a Git checkout, and no connected GitHub tool is available in this conversation.

## Files

- Main source: `ecomod_continued_4.tex`
- Main PDF: `ecomod_continued_4.pdf`
- SI source: `ecomod_continued_4_SI.tex`
- SI PDF: `ecomod_continued_4_SI.pdf`
- Build logs: `ecomod_continued_4.log`, `ecomod_continued_4_SI.log`

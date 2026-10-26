# Continuation 7 — source lineage and QA

**Purpose:** corrected selective-merge derivative after the source split in continuation 6 was challenged. Continuation 7 was made as a fresh derivative; neither continuation 4 nor continuation 6 was overwritten.

## Source boundary

- **Working prose base for the selected sections:** the initial Gemini 3.8 block in `/home/user/uploads/ecomod humanized.txt`—Abstract (first/standard-academic option), Introduction, supplied §2.1, Parameter Selection and Empirical Grounding, Data and Empirical Measures, Numerical Implementation, and Conclusions.
- **Base for all remaining sections:** `/home/user/ecomod_v45/output_v45_ecomod_continued_4_20261026/`.
- Continuation 5 was not used. Continuation 6 was not used as a source; this directory was started directly from continuation 4's main/SI sources and figure assets.
- The continuation-4 Table 1, Results, Discussion, Acknowledgments, Declarations, bibliography, and other unselected material were retained. A source comparison confirms Results through Discussion and Acknowledgments onward are unchanged from continuation 4; Table 1 is also unchanged.
- The SI source was copied unchanged from continuation 4. No SI content or Table S4 patterns were edited.

## Scientific checks applied to the Gemini prose

Gemini wording supplied the structure and prose direction, but not factual or mathematical authority. The selected sections were reconciled with continuation 4 and its source records:

- The model's equations, labels, assumptions, and conditional results were preserved; §2.1 contains the same eight equation environments and fourteen equation labels as continuation 4.
- The conversion premium is described as the **conversion term's marginal contribution** to total biocapacity. It is not presented as a guarantee that net biocapacity rises when other flows are active.
- Reduced fixed-demand results are scoped to that comparison and are not generalized to every delayed-model trajectory.
- NFA series are described as normalized annual account values, not measurements of physical stocks or a direct observation of model area \(A_c\). The auxiliary cropland residual is not identified with physical capital.
- The debt variable \(D\) is identified as an internal leaky model state, not measured nutrient depletion, aquifer overdraft, or an NFA quantity.
- Recovery studies are used as heterogeneous timescale context, not as a pooled global rate or estimates of \(\rho_c\) or \(\tau_g\).
- Step-size checks are reported as tested sensitivity checks, not as a blanket guarantee of numerical stability or convergence.
- The Paper3 pin metadata note is retained accurately in the Introduction footnote: v50 PDF present; README dated 2026-09-19 does not explicitly label v49/v50; checksum manifest lists v49 and omits v50; v50 TeX header points to v48 Markdown.

## Build and QA

- Main source/PDF: `ecomod_continued_7.tex` / `ecomod_continued_7.pdf`.
- SI source/PDF: `ecomod_continued_7_SI.tex` / `ecomod_continued_7_SI.pdf`.
- Built with Tectonic 0.17.0 on 2026-10-26. Both main and SI builds completed successfully.
- Final PDF lengths: **36 pages main** and **22 pages SI**.
- Extracted-text checks found no unresolved `??` references. Main-source QA found 44 unique labels, no duplicate labels or missing internal references, and the same 47 citation keys as continuation 4.
- The copied SI source is byte-identical to continuation 4's SI source.
- Visual QA covered the title/abstract, Introduction, Methods and parameter table, the Data and Numerical sections, the conclusion/page transition, and the references opening. The conclusion's physical-stock scope paragraph is kept together across the page break.
- Tectonic emitted non-fatal box warnings (including a slight overfull box and underfull bibliography lines); no build errors or unresolved references were found.

This lineage note records provenance and checks; it does not designate the manuscript as externally validated or replace scientific review.
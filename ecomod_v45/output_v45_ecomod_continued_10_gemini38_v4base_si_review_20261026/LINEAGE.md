# Continuation 10 — SI review verification and layout correction

**Purpose:** a fresh derivative preserving c9 and incorporating only the SI review items that were verified as real. C8 and c9 remain unchanged.

## Source lineage

- C10 was derived from `/home/user/ecomod_v45/output_v45_ecomod_continued_9_gemini38_v4base_auditfix_20261026/` into a new directory.
- The c9 main LaTeX source is unchanged in c10; c10's main paper retains the previously verified title, “Analogies” heading, corrected OWID order, initialized-delay-history wording, and clean prediction-page flow.
- The SI retains the c9 title and OWID citation-order corrections. Its only further source edits are: sorting the two cited companion-paper entries as 2026a then 2026b, and moving §S2.2 to a clean page start while keeping “Eqs. (6)–(7) reduce to” together.
- The initial Gemini 3.8 block in `/home/user/uploads/ecomod humanized.txt` remains the prose base for the Abstract (first/standard-academic option), Introduction, supplied §2.1, Parameters, Data and empirical measures, Numerical solution, and Conclusions. Continuation 4 remains the base for the other sections and figures; continuation 5 was not used.

## Review findings verified against c8 source, PDF, data, and c10 output

### Applied

- **SI bibliography order:** c8 listed Abaee 2026b before 2026a. C10 now lists the cited companion papers alphabetically by year suffix: 2026a, then 2026b.
- **§S2.2 page break:** the subsection header exists in c8 source and was visible at the bottom of c8 SI page 3, but the page break left only “(7) reduce to” at the top of page 4. C10 moves the entire subsection to page 4 and prevents the equation-range phrase from splitting. The matrix for Eq. (S2) itself was already correctly structured in source and visually rendered; it was not changed.

### Already corrected in c9 and retained

- The main and SI titles both now begin “A rising biocapacity total…”; c8's two titles matched one another but both lacked the article “A.”
- Main §2.3 and SI §S5.2 cite the cropland-area series before cereal yield, rendering the author-year order as 2026b,a.
- The Paper3 main-text reference uses the standard “Working paper (v50)” description with its existing commit URL.

### False positives or no change warranted

- **Companion URLs:** c8 main-text entries 2026a/b/c and SI entries 2026a/b all contain the correct lowercase, 40-character commit `2efaa62083f2007dec3446c15c475af88f0925f3`. The reported extra `e` and capital `A` are not in the source or rendered links. Repository API checks at that commit confirmed the Paper4 v41, Paper06 v71, and Paper3 v50 paths. The SI cites 2026a and 2026b only; it has no 2026c citation, so adding an uncited 2026c bibliography entry would be inappropriate. The review's quoted 2026b,c wording is not present in the SI source; the 2026c citation is in the main text and is listed there.
- **Table S4 floor:** source, rendered c8 page 8, and `/home/user/ecomod_v45/si_drawdown_depth.csv` agree that the two questioned cells are 0.050, not 0.040. The CSV minima are 0.050000000006867766 for \(A_{c0}=0.40, P_0=3.5\) and 0.05000000000007304 for \(A_{c0}=0.70, P_0=4.0\); both round to 0.050 and respect the stated 0.05-ha floor. No table values were changed.
- **Poeplau:** the SI source and rendered §S5.5 spell the citation correctly as Poeplau; “Poelau” is not present.
- **Tables S10 and S11:** source and rendered tables show \(Y_c=\Upsilon_c(q)A_c\); Table S11 lists \(b_c, b_{G,c}, \rho_c\), and \(D\). The apparent Y/T glyph problems are not source typos.
- **Section S6:** the source uses `\section{Policy extensions}` and the PDF visibly renders **S6**. “56” is an extraction/OCR confusion, not a source error.
- **SI Table S1:** the source and rendered table show \(b_{G,c}\), correctly.

## Provenance and safeguards

- The Paper3 v50 metadata discrepancy remains documented outside the manuscript: at the pinned commit, the v50 PDF is present; the checksum manifest lists v49 article files but omits v50; the README dated 2026-09-19 does not explicitly label v49/v50; and the v50 TeX header points to the v48 Markdown source. The ECOMOD pin was not retargeted.
- The c8/c9 clean-manuscript changes remain in force: no source-management footnote or process-oriented “details will be added later” clause appears in the paper.
- Conditional model outputs remain distinct from NFA account values and physical-stock measurements; reduced fixed-demand findings remain scoped to their stated comparison; no Table S4 values were edited without data evidence.

## Build and QA

- Main source/PDF: `ecomod_continued_10.tex` / `ecomod_continued_10.pdf` (**34 pages**). Its source is byte-identical to c9's main source.
- SI source/PDF: `ecomod_continued_10_SI.tex` / `ecomod_continued_10_SI.pdf` (**22 pages**).
- Both PDFs compiled with Tectonic 0.17.0 on 2026-10-26. There are no fatal diagnostics, unresolved citations/references, or extracted-text `??` markers; remaining underfull-box warnings are non-fatal.
- Main has 47 cited keys and 47 bibliography keys; SI has 12 cited keys and 12 bibliography keys. Main has 44 unique labels and SI has 45; all internal references resolve.
- Visual QA covered the SI title, Table S1, Table S4, §S2.2 and Eq. (S2), Tables S10–S11, §S5.5, §S6, and the reordered SI reference list.
- No package was created and no checksum manifest was refreshed. The c8, c9, and c10 output directories are archived on the non-main GitHub branch `ecomod-v45-continuations-20261026`; `main` was not changed.

This file is provenance documentation, not part of the journal submission.
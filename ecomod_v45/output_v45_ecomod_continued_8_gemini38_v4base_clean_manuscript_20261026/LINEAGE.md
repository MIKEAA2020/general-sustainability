# Continuation 8 — clean-manuscript derivative

**Purpose:** remove source-management and deposit-process notes from the journal manuscript while preserving the continuation-7 source split and scientific safeguards. This is a new derivative; continuations 4, 6, and 7 remain unchanged.

## Source lineage

- Continuation 8 was derived from `output_v45_ecomod_continued_7_gemini38_base_v4remainder_20261026/`.
- The initial Gemini 3.8 block in `/home/user/uploads/ecomod humanized.txt` remains the prose base for the Abstract (first/standard-academic option), Introduction, §2.1, parameter selection, data and empirical measures, numerical implementation, and Conclusions.
- Continuation 4 remains the base for the unselected sections and figures. Results and Discussion are unchanged from continuation 4; Table 1 is unchanged. The Supplementary Information source is unchanged and byte-identical to continuation 4's SI source.
- Continuation 5 was not used.

## Journal-manuscript cleanup

- Removed the Introduction footnote that discussed a checksum manifest, README version labels, and the TeX-to-Markdown source mismatch. That source-management note is **not part of the journal manuscript**.
- Removed the process-oriented clause “repository and record details will be added after the deposit is complete” from the Data availability statement. The substantive statement that derived data and code will be deposited remains.
- The Paper3 v50 metadata discrepancy is retained here for provenance only: at the pinned commit, the v50 PDF is present; the checksum manifest lists v49 article files but omits v50; the README dated 2026-09-19 does not explicitly label v49/v50; and the v50 TeX header points to the v48 Markdown source. The manuscript's Paper3 reference continues to point to the existing pinned commit; the pin was not retargeted.

## Scientific safeguards retained

- The conversion premium is scoped to the conversion term's marginal contribution; it is not presented as a guarantee that net biocapacity rises when other flows are active.
- Reduced fixed-demand results are scoped to that comparison, not generalized to every delayed-model trajectory.
- NFA values are described as normalized annual account values, not physical-stock measurements or direct observations of model area \(A_c\).
- The debt variable \(D\) remains an internal leaky model state, not a physical process measurement.
- Recovery studies provide heterogeneous timescale context, not pooled global rates or estimates of \(\rho_c\) or \(\tau_g\).
- Numerical checks are described as tested step-size sensitivity, not a blanket guarantee of stability or convergence.

## Build and QA

- Main source/PDF: `ecomod_continued_8.tex` / `ecomod_continued_8.pdf`.
- SI source/PDF: `ecomod_continued_8_SI.tex` / `ecomod_continued_8_SI.pdf`.
- Built successfully with Tectonic 0.17.0 on 2026-10-26.
- Final PDF lengths: **35 pages main** and **22 pages SI**.
- Main source has the same 47 citation keys as continuation 4; 44 unique labels; no duplicate labels, missing internal references, or extracted-text `??` markers.
- §2.1 retains eight equation environments and fourteen equation labels. Table 1 is unchanged. SI source is byte-identical to continuation 4's SI source.
- Visual QA covered the title/abstract, Introduction after footnote removal, and the conclusion/declarations page flow. No source-management footnote or deposit-process placeholder remains in the manuscript.
- Tectonic issued non-fatal box warnings; both PDFs compiled, with no unresolved references or fatal diagnostics.

This file is provenance documentation, not part of the journal submission.
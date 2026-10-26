# Continuation 9 — verified review fixes

**Purpose:** a fresh, narrowly edited derivative of continuation 8 (c8), incorporating only the review items verified against the c8 sources, PDFs, numerical code, and repository records. C8 and all earlier continuations remain unchanged.

## Source lineage

- C9 was copied from `/home/user/ecomod_v45/output_v45_ecomod_continued_8_gemini38_v4base_clean_manuscript_20261026/` into a new output directory. C8 was not overwritten.
- The initial Gemini 3.8 block in `/home/user/uploads/ecomod humanized.txt` remains the prose base for the Abstract (first/standard-academic option), Introduction, supplied §2.1, Parameters, Data and empirical measures, Numerical solution, and Conclusions. Continuation 4 remains the base for the other sections and figures. Continuation 5 was not used.
- The source split and scientific safeguards established in c7/c8 are retained. Results and Discussion are unchanged except that the duplicated prediction-testability caveat is consolidated before the list; the five prediction items themselves are unchanged.
- The SI derives from c8 and is no longer byte-identical to c4 because its title and the OWID citation order were corrected.

## Verified edits applied in c9

- Added the article **“A”** to the title in both the main text and SI.
- Replaced the run-in heading **“The orchard and the elevator”** with **“Analogies.”**
- Reordered the OWID citation keys in main §2.3 and SI §S5 to follow the prose: cropland area first, cereal yield second.
- Clarified the delay-history initialization in Numerical implementation: the pre-run histories cover the longest active delay window, use \(q_0\) and the computed initial-state \(B_0\), and are not set to zero. The matched technology-wave run's current \(B(0)\) includes \(T_b(0)\).
- Kept **per-hectare** together with a nonbreaking TeX box to prevent an extraction/rendering split; the word was already correct in c8.
- Moved the full testability caveat before the five predictions and removed its redundant repeat after the list. This eliminates the two-line carryover that had occupied page 23; c9 page 23 now begins the Discussion.
- Standardized the Paper3 reference to “Working paper (v50)” and retained its exact immutable commit URL. The URL itself was not retargeted.

## Review checks — no correction needed

- Table 1 already contains \(b_{G,c}\); it remains unchanged.
- The cited name is **Poeplau**, not “Poelau.”
- The ceiling renders as \(E_{\mathrm{ceil}}\), not \(E_{\mathrm{cell}}\); the unit \(gha\,ha^{-1}\) is correct.
- The prediction list already uses `label=P\arabic*.` and renders **P1** (c9 page 22). No duplicate label was added.
- “Per-hectare” was already present. The apparent split was ordinary line wrapping; c9 now keeps the compound intact.
- The land-flow equations render as (6), (7), and (8), matching their separately labeled source equations.
- The `Abaee2026a`, `Abaee2026b`, and `Abaee2026c` URLs contain the full 40-character commit `2efaa62083f2007dec3446c15c475af88f0925f3`. At that commit, the API verified the Paper4 v41, Paper06 v71, and Paper3 v50 paths. The apparent extra character and Paper3-path concerns were false positives; no URL change was needed.

## Provenance and scientific safeguards retained outside the manuscript

- The Paper3 v50 metadata discrepancy remains documented here rather than in the journal manuscript: at the pinned commit, the v50 PDF is present; the checksum manifest lists v49 article files but omits v50; the README dated 2026-09-19 does not explicitly label v49/v50; and the v50 TeX header points to the v48 Markdown source. The ECOMOD citation pin was not retargeted.
- The Introduction's source-management footnote remains absent. The Data availability statement retains the substantive planned-deposit commitment but not the process-oriented “details will be added later” clause.
- The conversion premium is scoped to the conversion term's marginal contribution, not represented as a guarantee that net biocapacity rises when other flows are active.
- Reduced fixed-demand findings are limited to that comparison and are not generalized to every delayed-model trajectory.
- NFA values remain clearly distinguished from physical-stock measurements and from the model's \(A_c\). The model's numerical results remain conditional model outputs.
- The debt variable \(D\) remains an internal leaky model state; numerical checks are described as tested step-size sensitivity, not a blanket guarantee of stability or convergence.

## Build and QA

- Main source/PDF: `ecomod_continued_9.tex` / `ecomod_continued_9.pdf` (**34 pages**).
- SI source/PDF: `ecomod_continued_9_SI.tex` / `ecomod_continued_9_SI.pdf` (**22 pages**).
- Both PDFs compiled successfully with Tectonic 0.17.0 on 2026-10-26. The engine issued non-fatal underfull-box warnings; there were no fatal errors, unresolved references, or extracted-text `??` markers.
- Main citation-key set remains the same 47 keys as c8; 44 main labels are unique and all internal references resolve. SI has 45 unique labels and all internal references resolve.
- Visual QA covered the main title/abstract, Analogies heading, Table 1, citation order, land-flow numbering, initialization paragraph, per-hectare line, predictions, page-23 transition, and references; SI title and §S5 citation order were also checked.
- No package/archive was created and no root checksum manifest was refreshed. No external push was performed: `/home/user/ecomod_v45` is not a Git worktree, and a GitHub write integration was unavailable in this session. C9 is preserved in the shared workspace; nothing was pushed to `main`.

This file is provenance documentation, not part of the journal submission.
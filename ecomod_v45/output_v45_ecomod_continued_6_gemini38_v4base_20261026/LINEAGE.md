# Lineage — continuation 6 (Gemini 3.8 prose / continuation 4 base)

**Prepared:** 2026-10-26  
**Working directory:** `/home/user/ecomod_v45/output_v45_ecomod_continued_6_gemini38_v4base_20261026/`

## Ancestry and scope

- This is a new derivative of `/home/user/ecomod_v45/output_v45_ecomod_continued_4_20261026/`. Continuation 4 and continuation 5 were not overwritten; continuation 5 was not used as a source.
- The prose working reference was `/home/user/uploads/ecomod humanized.txt`. The selected material was the initial Gemini 3.8 block, before the later, separate “gemini pro preview” block.
- Gemini 3.8 supplied the prose base for the Abstract, Introduction, Conclusion, supplied Section 2.1 material, Parameters, Data and empirical measures, and Numerical solution. Its prose was not treated as authority for facts or mathematics: claims, equations, citations, parameters, data descriptions, numerical-method statements, qualifications, and safeguards were checked against continuation 4 and the available source record. The Introduction opening and several lead-ins were lightly tightened for page flow.
- All other main-text sections use continuation 4. The Results and Discussion source text was compared with continuation 4 and is unchanged; only LaTeX page-flow wrappers were added in selected places. Acknowledgments, Declarations, and References remain from continuation 4.
- No additional Gemini SI text was supplied. `ecomod_continued_6_SI.tex` is byte-for-byte identical to continuation 4's SI source; no SI prose or tables were revised.

## Scientific and bibliographic safeguards retained

- NFA values are described as annual account values, not direct measurements of physical stocks. Conditional model results are kept distinct from observed account values; no unsupported causal, universal, ecological-collapse, or physical-stock claim was added.
- The auxiliary cropland/yield series remains an illustrative, assumed account split—not a measured model land class or physical stock. No Table S4 pattern edits or recomputation were made.
- Half-Earth is treated as a spatial conservation target, distinct from the model's reservation of annual human-available flow.
- Citation-key mapping remains `Abaee2026a` = governance/Paper4, `Abaee2026b` = assessment/Paper06, and `Abaee2026c` = ledger/Paper3. Paper06 v71 Theorem 4(iii) is scoped only to its witness-defined diagonal-gap region.
- The ECOMOD citation pin was not retargeted. The Paper3 pin metadata caveat is retained: the v50 PDF is present; the README dated 2026-09-19 does not explicitly label v49/v50; the checksum manifest lists v49 and omits v50; and the v50 TeX header points to the v48 Markdown.

## Verification and build

- Section 2.1 retains the continuation-4 mathematical structure: 8 equation environments and 14 equation labels (15 labels including the subsection label).
- Main and SI citation-key sets match continuation 4 (47 and 12 keys, respectively). Source preflight found 44 unique main labels and 45 unique SI labels, with no duplicate labels or unresolved in-file references.
- Tectonic 0.17.0 successfully built the final main PDF and the unchanged SI PDF. Extracted text has no `??` markers; build logs have no fatal, undefined-reference, or undefined-citation diagnostics. Non-fatal box warnings remain in the logs.
- Final PDFs: `ecomod_continued_6.pdf` — 34 pages; `ecomod_continued_6_SI.pdf` — 22 pages. Logs are `ecomod_continued_6_build.log` and `ecomod_continued_6_SI_build.log`.
- Visual checks covered the title/Abstract and Introduction, the Methods/Parameters/Data/Results transition, the predictions and discussion, the Conclusion and references, and SI pages 1 and 22.

## Repository and packaging status

- No archive/package was created and no checksum manifest was refreshed.
- No push was performed: this derivative directory has no Git worktree or remote, and the GitHub connector was previously reported unsupported. Nothing was pushed to `main`.

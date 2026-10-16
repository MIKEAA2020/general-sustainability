# Provenance and verification — Paper07 v54

- **Edition:** Paper07 v54, standalone
- **Base edition:** Paper07 v53
- **Date:** 2026-10-16
- **Parallel edition preserved:** Paper08 v48, the combined manuscript; this work does not overwrite or merge it.
- **Repository destination:** `MIKEAA2020/general-sustainability`, branch `e2-v3-source-year`, at `arena agent 1/agent workspace/papers/paper07_sampled_governance_v54/`. The fresh pre-numbering all-ref audit selected this lineage location. Paper07 v52/v53, Paper08 v48, and all prior editions remain preserved.

## Lineage and scope

Paper07 v54 is a standalone continuation of v53. The main source is assembled from `parts/`; the Supplementary document is assembled from `si_parts/`. The v52→v53 recovered-content crosswalk is included, together with the explicit caveat that the separately referenced v52 SI was not found in any audited repository ref and cannot be treated as compared in full. No Paper08 source, PDF, or Supplementary file was modified.

V54 makes no new numerical claim and is not described as a new computational rerun. Its purpose is to correct reporting and section pointers exposed by the crosswalk, preserve the useful v52 design lessons in qualified form, and restore an AI-use disclosure.

## Material changes in v54

1. **Cross-reference repair.** Power is linked to S14.1, the unreproduced constrained-mortality formulation to S14.2, prospective designs to S7.1–S7.6, fishing-mortality placement to S13.2, and the cod assessment table to S13.3 (Table S20 in the current sequential table numbering). The SI's former hard-coded cod-table number is replaced with a label-based reference.
2. **Sensitivity provenance.** Main text now distinguishes the crossing-only summary of the archived ±5%/±10% battery in S11.4 from the complete archived rows/fields in `src/p7_empirical/recovered/sens_table.csv` and the separate rerun ±2% crossing table in S11.3.
3. **Bounded design implications.** S7.6 retains the useful governance-clock ideas as modelling/evaluation requirements, not policy recommendations. It explicitly states that the model does not establish a universally stabilising cadence, broad protective-rule robustness, a required review frequency for extractive rules, or benefits from emergency triggers.
4. **AI-use disclosure.** Declarations state that AI tools assisted with drafting, code generation, and iterative review; the author reviewed/edited and takes responsibility for the content. No model identity is guessed.
5. **Historical-package gap.** The v52 PDF is 36 pages, but its final pages and source refer to a separate SI. The v52 source inventory says S1–S10 while in-body references reach S13.3. No such SI file or the promised dimensionless-identifiability chart was found in the audited refs. V54 does not claim that the v53 joint-box sensitivity is a substitute for structural identifiability analysis.

## Final build record

- Main: `paper07_sampled_governance_v54.pdf`, 14 A4 pages.
- Supplement: `paper07_sampled_governance_v54_SI.pdf`, 29 A4 pages.
- Main compiled twice and SI compiled three times with `pdflatex` after the source edits; current PDFs and logs are in this package.
- Final logs contain no undefined references/citations, changed-label warnings, hyperref warnings, or overfull boxes. Underfull-box notices remain in some compact tables/paragraphs; the relevant pages were visually checked and show no clipped text or layout collision.
- Main page 6, the declaration page, Supplementary page 13 (including the added design paragraph), and the final Supplementary page were rendered and visually inspected.
- Existing v53 numerical outputs, code, figures, and archived logs were reused unchanged. The incomplete screen-battery rerun, assembled 17-cell power record, and archived comparator metadata remain qualified as in v53.

## Credential handling

The user-supplied GitHub PAT remains in its designated workspace location and is excluded from the bundle and repository publication. It must never be committed or pushed. No credential file is copied into this paper tree or source bundle.

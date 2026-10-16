# Paper07 v52 → v53 coverage crosswalk

- **Audit date:** 2026-10-16
- **Comparison:** the recoverable v52 main manuscript and deposited source records against v53 main text plus Supplementary Information (S1–S14).
- **Status:** content-level mapping completed for the recoverable record; the separate v52 SI could not be recovered, so this is not represented as a complete paragraph-by-paragraph comparison of the full historical package.

## Bottom line

V53 is stronger on evidence status and reproducibility: it corrects the interpretation of the two-value review-interval proxy test, separates archived stage classifications from a new reconstruction, and withdraws the earlier nonlinear-bifurcation claims that were not established by the retained computation. Most v52 methods, results, tables, and appendices have a destination in v53 main/SI. The v53 SI is expanded to 14 sections.

The omissions are not all equivalent. The old policy-facing Box 2 and its eight implications were dropped; several are stronger than the evidence supports. They should not be restored as empirical findings. Their defensible modelling lessons are retained in qualified form in v54 Supplementary S7.6. The v52 AI-use declaration was also dropped and is restored generically in v54. Several v53 section citations had become stale when the SI was renumbered; v54 corrects those and the one-at-a-time sensitivity wording.

One explicit v52 promise remains unresolved: its closing inventory names a “dimensionless identifiability chart” in S2. No such v52 SI file or chart was found in the audited repository trees. V53's joint-parameter sensitivity analysis is related to parameter fragility, but it is not claimed to be the same chart or a substitute for structural identifiability analysis.

## Retrieval limit: the v52 SI is not in the audited repository

The recovered v52 source is `paper07_sampled_governance_v52.tex` on `e2-v3-source-year`; its PDF is 36 pages. The final PDF pages and TeX source explicitly refer to a separate Supplementary file. The final inventory lists S1–S10, but citations in the body also refer to S11, S12, and S13.1–S13.3. The inventory is therefore internally stale or incomplete; the historical SI may have extended beyond S10.

The all-ref inspection covered all six repository branches, both tags, and both prereleases. No standalone Paper07/v52 supplementary file, nor a file containing the promised dimensionless-identifiability chart, was present in those trees. The v52 data-availability text supplies no separate DOI for that SI. Consequently, 36 pages is the recoverable v52 main PDF length—not the length of the complete v52 package—and the old SI's detailed contents cannot be certified. The map below distinguishes confirmed carryover from inferred or unrecoverable coverage.

## Content map

| v52 content | v53 destination | Crosswalk judgment |
|---|---|---|
| §2.1 model, review clock, seven timing objects, operator definitions, and Box 1 | Methods §2.1; SI S8.3 | Retained and compressed. The separate observation, assessment, decision, deployment, and response timings remain explicit. |
| §§2.2–2.5 registration, spectral procedure, power and computational requirements; Appendix A Tables 3–4 | Methods; SI S3, S8–S11, S14 | Substantially retained, with a larger provenance and status register. Parameter/notation tables are in S8. Power is explicitly marked as assembled from archived outputs rather than a completed full driver rerun. |
| Results §§3.1–3.2 invariance and rapid-review limit | Results §3.1; SI S2 | Retained with a proved finite-horizon statement and explicit warning that this does not classify stability for a fixed positive review interval. |
| §3.3 delayed-recruitment response regions | Results §3.2; SI S9.2–S9.3 | Retained, with the unavailable archived solver/history separated from the newly preregistered reconstruction. The new reconstruction is not presented as validation of the old windows. |
| §3.4 operator spectra and §3.4.1 sensitivity | Results §§3.2–3.3; SI S11–S12 | Core crossings, operator distinction, one-at-a-time records, and joint-box sensitivity are retained and expanded. V53 appropriately withdraws the v52 Neimark–Sacker/normal-form/invariant-circle claims: the full nonlinear classification was not independently established. |
| §3.5 selected 42-stock screen and its sensitivity | Results §3.4; SI S9.1 | Retained. The cohort and zero-BH result remain; the alternative-null battery and limits are made explicit. |
| §3.6 injected-signal power | Results §3.4; SI S14.1 | Retained as conditional simulation results. The incomplete rerun is disclosed rather than described as a fresh completed run. |
| §3.7 32-system case search | Methods; Discussion §4.2; SI S4 | Retained. The search is labelled curated, its row-level dispositions are supplied, and “no qualifying case found” is not treated as disconfirmation. |
| §3.8 northern-cod two-window case and Appendix B distributive record | Results §3.6; SI S5.3, S6, S13.3 | The descriptive split, assessment values, and social-measurement mismatch are retained. The unreproduced constrained-mortality quantities are now explicitly open in S14.2, not results. |
| Discussion §§4.1–4.3 and §4.7 limitations | Discussion §§4.1–4.3 and §4.5; SI S1 and relevant records | Retained in shorter form and generally better bounded. The stage mismatch, selected-cohort limits, confounding, and non-causal status are more visible. |
| §§4.4–4.5 five falsification outcomes and five prospective designs | Discussion §4.4; SI S7 and S14.3 | The designs and decision rules are retained in SI; none is represented as executed. V52’s S13.3 design pointers are obsolete after the SI reorganization; v53 points generally to S7, and v54 narrows that pointer to S7.1–S7.6. |
| Appendix B and §4.6 distributive constraints | SI S6 | Retained at measurement level: constituency mismatch, available community series, unoperationalised floors, and instrument limits. |
| §4.8 Box 2 (four design principles) and eight management implications | No verbatim v53 counterpart; qualified treatment added in v54 S7.6 | The old wording should not be restored as policy findings. Claims that protective rules generally tolerate rigidity, extractive rules require frequent review, or emergency triggers improve outcomes exceed the tested model/evidence. V54 retains the defensible lessons as requirements for modelling and evaluation, with explicit non-inference boundaries. |
| v52 AI-use declaration | Omitted in v53; a general disclosure is restored in v54 Declarations | This is a transparency omission, not a scientific result; v54 states AI-assisted drafting/code/review without guessing a model identity. |
| Promised “dimensionless identifiability chart” (v52 closing inventory, S2) | Not recovered; v53 has a distinct joint-box sensitivity figure/table in S11 | Unresolved. The joint-box result concerns deterministic parameter perturbations of a crossing; it is not evidence of structural identifiability and is not labelled as the missing chart. |

## v54 corrections made after the crosswalk

- Updated all stale SI pointers: the power table is S14.1; the constrained-mortality open item is S14.2; prospective designs are S7.1–S7.6; fishing-mortality placement is S13.2; and the cod assessment table is S13.3 (Table S20 in the current sequential table numbering).
- Replaced the hard-coded old cod-table reference with a label-based reference.
- Clarified the sensitivity record: S11.3 contains the complete rerun ±2% crossing table; S11.4 is only the crossing summary of the archived ±5%/±10% battery; the full archived rows/fields remain in `src/p7_empirical/recovered/sens_table.csv`.
- Added boundary-limited design implications to S7.6 and restored a general AI-use disclosure.
- Preserved v52, v53, and parallel Paper08 v48; v54 is a new edition, not an overwrite.

## Decision

Complete the crosswalk rather than silently accepting all omissions. Accept the removal of overconfident policy prescriptions, but preserve the useful design lessons in a qualified supplement. Treat the missing v52 SI and its promised chart as an explicit archival gap; do not claim full historical-package equivalence until that source is recovered.

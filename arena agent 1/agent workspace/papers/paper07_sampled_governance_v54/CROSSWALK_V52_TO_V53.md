# Paper07 v52 → v53 coverage crosswalk

- **Audit date:** 2026-10-16
- **Comparison:** the recoverable v52 main manuscript and deposited source records against v53 main text plus Supplementary Information (S1–S14), with a separate version-specific map to a recovered historical supplement candidate.
- **Status:** the recoverable v52 main manuscript has been mapped to v53/v54. A historical, old-numbered Paper5 v19 supplement has now been recovered and mapped section by section; exact attachment to the v52 build remains unverified.

## Bottom line

V53 is stronger on evidence status and reproducibility: it corrects the interpretation of the two-value review-interval proxy test, separates archived stage classifications from a new reconstruction, and withdraws the earlier nonlinear-bifurcation claims that were not established by the retained computation. Most v52 methods, results, tables, and appendices have a destination in v53 main/SI. The v53 SI is expanded to 14 sections.

The omissions are not all equivalent. The old policy-facing Box 2 and its eight implications were dropped; several are stronger than the evidence supports. They should not be restored as empirical findings. Their defensible modelling lessons are retained in qualified form in v54 Supplementary S7.6. The v52 AI-use declaration was also dropped and is restored generically in v54. Several v53 section citations had become stale when the SI was renumbered; v54 corrects those and the one-at-a-time sensitivity wording.

A follow-up retrieval correction changes the archival conclusion. The historical old-numbered file `paper5_supplementary_v19_NatSustain.md` is present in `main` and `e2-v3-source-year`. Its front matter names the exact v52 article title; it contains S1–S13.3 and S2.3's named dimensionless-identifiability chart. The v52 main source directly points to S2.3 and reports the same baseline fixed point. This is a strong content match, but no version-bound manifest, deposit record, or source-to-PDF build record establishes that this exact v19 revision accompanied the v52 PDF. See `PAPER07_V52_TO_HISTORICAL_V19_CLAIM_SECTION_CROSSWALK.md`. The chart content is recovered; the unresolved issue is exact version attribution, not chart retrieval. The separate v54 SI remains a reconstructed v54 supplement, not a retroactive claim about v52.

## Retrieval update: historical supplement recovered; exact v52 attachment unresolved

The v52 source is `paper07_sampled_governance_v52.tex` on `e2-v3-source-year`; its main PDF is 36 pages. The main source explicitly describes an accompanying Supplementary file. Its closing inventory lists S1–S10, while the body cites S11, S12, and S13.1–S13.3, indicating that the inventory is stale or underinclusive. The 36-page PDF is the recoverable main article, not a verified complete article-plus-SI package.

A targeted follow-up found `paper5_supplementary_v19_NatSustain.md` on both `main` and `e2-v3-source-year` as the same Git blob; e2 also carries the same blob in its `content_audit/seeds/` directory. The file's front matter names “The decision clock: review intervals as a design lever for stable resource governance,” the exact v52 main title, and the file contains S1–S13.3, including the promised chart in S2.3. The v52 main text's Appendix A directly points to S2.3 and gives the matching baseline fixed point.

The section-by-section claim map is in `PAPER07_V52_TO_HISTORICAL_V19_CLAIM_SECTION_CROSSWALK.md`. It finds strong structural and topical alignment, but it does not certify the exact v19 revision as the SI compiled/deposited with the particular v52 PDF: no version-bound manifest, deposit record, or source-to-PDF build record was found. The old-numbered file must not be relabeled as “Paper07 v52 SI” on the strength of content match alone. A Paper08 v48 governance supplement preserves the S2.3 block verbatim but has Paper08-specific front matter and other edits; this corroborates shared lineage, not the exact v52 attachment.

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
| Promised “dimensionless identifiability chart” (v52 closing inventory, S2; Appendix A points to Supplementary S2.3) | Historical v19 S2.3 recovered; v53/v54 joint-box figure remains a different object | The chart content is recovered and strongly matches the v52 pointer and baseline. Exact v19-to-v52 build binding remains unverified. Do not call the chart missing or use the joint-box figure as its replacement. |

## v54 corrections made after the crosswalk

- Updated all stale SI pointers: the power table is S14.1; the constrained-mortality open item is S14.2; prospective designs are S7.1–S7.6; fishing-mortality placement is S13.2; and the cod assessment table is S13.3 (Table S20 in the current sequential table numbering).
- Replaced the hard-coded old cod-table reference with a label-based reference.
- Clarified the sensitivity record: S11.3 contains the complete rerun ±2% crossing table; S11.4 is only the crossing summary of the archived ±5%/±10% battery; the full archived rows/fields remain in `src/p7_empirical/recovered/sens_table.csv`.
- Added boundary-limited design implications to S7.6 and restored a general AI-use disclosure.
- Preserved v52, v53, and parallel Paper08 v48; v54 is a new edition, not an overwrite.

## Decision

Complete the crosswalk rather than silently accepting omissions. Accept the removal of overconfident policy prescriptions, but preserve the useful design lessons in a qualified supplement. Treat v19 as a strong content-matched historical companion candidate, not as a verified version-specific v52 SI. The exact v52 package linkage remains open; the chart itself is recovered. Do not claim full historical-package equivalence until version binding is established.

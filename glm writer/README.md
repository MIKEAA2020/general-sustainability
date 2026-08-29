# GLM Writer — Journal-Facing Submission Editions of the Nine-Paper Corpus

**Created:** 2026-08-30 · **Status:** submission-ready editions for the nine papers · **Provenance:** new content only — no existing repository file was modified, replaced, or deleted.

## What this folder is

This folder contains the **journal-facing (submission) editions** of the programme's nine papers, produced by executing the per-paper venue passes registered in `DEEP_SCAN_RESIDUAL_POINTS.md` §1.2 and extended in `PUBLICATION_STRATEGY_JOINT_EVALUATION.md` §6 (the joint evaluation of the owner's two external publication-strategy audits). It implements the two-layer edition architecture of `research_program/paper_types_and_venues_decision.md` §5:

- **Layer 1 (internal editions — unchanged):** `papers/*/manuscript.md` and `manuscript_v2.md`, plus `wave_e_*/manuscript/*_v2.md`, remain the programme's auditable record with the full apparatus, edition notes, and provenance identifiers. Paper 1's `manuscript_v3.md` (2026-08-29) was the executed template for this folder's transformation style.
- **Layer 2 (journal-facing editions — this folder):** each paper's science carried verbatim (every theorem, proof, number, table, verdict, and claim status — the non-loss rule holds throughout), with the internal scaffolding removed or relocated: repositioned abstracts, field-native introductions ending in explicit roadmaps, status ledgers converted to appendix statement inventories with concrete bases, internal identifiers genericized (the papers are prepared for submission **before** sibling publication, so identifiers genericize rather than resolve), and data/code-availability statements made concrete.

`EDITION_PROTOCOL.md` in this folder documents the exact transformation rules, including the adjudicated translation table (which terms of art are kept with first-use glosses and which internal labels are genericized) and the two-layer caveat that keeps robust and certified results distinct in every paraphrase.

## The nine submissions

| # | Folder | Title (short) | Target venue | Article type | Words |
|---|--------|---------------|--------------|--------------|-------|
| 1 | `paper1_typed_architecture/` | A Typed Architecture for Sustainability: … Separation of Assessment Doctrines | Environmental Modelling & Software | Theory/methods | ~10,000 |
| 2 | `paper2_theorem_atlas/` | The Formal Mathematical Foundations of Sustainability: A Typed Theorem Atlas | Set-Valued and Variational Analysis | Mathematics (proofs in ESM) | ~16,000 |
| 3 | `paper3_material_ledgers/` | Material Ledgers and Depletion Diagnostics | Ecological Modelling | Methods/formal framework | ~14,900 |
| 4 | `paper4_delay_dynamics/` | Delay-Driven Capital Liquidation and Nonlinear Institutional Dynamics | Communications in Nonlinear Science and Numerical Simulation | Applied nonlinear dynamics | ~18,500 |
| 5 | `paper5_sampled_governance/` | Sampled Governance, Empirical Identification, and Falsification Design | ICES Journal of Marine Science | Methodology + case study | ~14,700 |
| E1 | `wave_e1_cod_forecast_ladder/` | Does a surplus-production ladder improve forecasts of Northern cod? | Fisheries Research | Empirical forecast evaluation | ~4,800 |
| E2 | `wave_e2_cod_intervention/` | Does catch governance protect the limit reference point? | Fisheries Research (short communication) | Applied management analysis | ~2,300 |
| E3 | `wave_e3_edwards_forecast_ladder/` | Edwards Aquifer J-17 forecast ladder | Groundwater | Empirical forecast evaluation | ~4,400 |
| E4 | `wave_e4_edwards_intervention/` | Edwards Aquifer robust pumping-rule scoring | Journal of Water Resources Planning and Management | Applied management analysis | ~3,200 |

Each paper folder contains:
- `manuscript_journal.md` — the journal-facing markdown source (metadata block, repositioned abstract, roadmap introduction, verbatim science, appendix statement inventory, references, data availability).
- `<Name>_AcademicPaper_2026-08-30.docx` — the formatted Word submission file (Times New Roman 12 pt, 1.5 line spacing, justified body with first-line indents, native Word equations converted from the LaTeX math, three-line tables, embedded figures with centred captions for the four empirical papers, running head, page numbers, title page with anonymized author block, **no table of contents** — formal journal-submission format).
- Figure PNGs (papers E1 and E3) — the same byte-identical figure files as the internal editions, embedded in the .docx and kept here for journal upload systems that request separate figure files.

## Venue routing rationale (summary)

The routing follows the programme's adjudicated venue decision (`research_program/paper_types_and_venues_decision.md` §4), re-examined and **maintained** against the two external audits in `PUBLICATION_STRATEGY_JOINT_EVALUATION.md` §4: methods/open-science venues for the apparatus-bearing papers (EMS for Paper 1), the set-valued analysis home territory for the proof corpus (SVVA for Paper 2, no split — the audits' "100-page/12-family" premise was verified false: the atlas is ≈15.9k words across 11 families), modelling-science venues for Papers 3–4, the assessment-methods audience for Paper 5, and domain journals for the four empirical papers. The audits' alternative suggestions (Ecological Economics primary for Paper 1; splitting Paper 2 into 2A/2B/2C; a Paper 2C/3 merge) were evaluated and declined with recorded reasons in the joint-evaluation record; the audits' accepted disciplines (one-sentence contribution statements, skeptical-reviewer checks, identifier genericization, first-use glosses, E5 reframing, the jargon purge) are all implemented here.

## What changed relative to the internal editions (and what did not)

**Changed (presentation only):** series headers, edition notes, and process vocabulary removed; claim-status ledgers relocated to Appendix A statement inventories (two-table form with concrete bases, stipulation/validity legend, formal-validity-versus-empirical-applicability disclaimer); internal identifiers (Wave E, R03/R04, A014, E5, CC row tags, "general theory §15") genericized per the translation table — with the corpus's terms of art ("negative certificate", "typed architecture", "state space", "proof obligation") **kept** and given first-use glosses; introductions rewritten field-natively with closing roadmaps; abstracts repositioned for each venue; concrete data-availability statements; the E3/E4 peer-reviewed-literature engagement obligation discharged with verified references (the internal reference lists were exclusively data agencies).

**Not changed (non-loss rule):** every theorem, lemma, proposition, corollary, counterexample, conjecture, and definition statement; every proof and its availability status; every number, interval, RMSE/Brier score, kernel horizon, percentage, and table value; every retention verdict and negative certificate; the claim-status hierarchy itself; the honest reporting of certification tiers (Paper 4's nominal folds stay nominal; Paper 5's nominal computational tier is stated as such).

## Files

- `EDITION_PROTOCOL.md` — the transformation rules, translation table, and format conventions used for every edition in this folder.
- `SUBMISSION_PLAN.md` — the compressed all-papers-at-once submission strategy (the owner's instruction: submit all papers soon, not in staggered waves over months), with per-paper readiness notes and the remaining pre-flight checklist.
- `COVER_LETTERS.md` — nine editor cover letters, one per submission.
- `build_docx.py` — the deterministic markdown→Word build script (pandoc + python-docx post-processing) that produced every .docx in this folder from its `manuscript_journal.md`; re-running it reproduces the files.

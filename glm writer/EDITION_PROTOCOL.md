# Edition Protocol — Journal-Facing Editions of the Nine-Paper Corpus (2026-08-30)

**Status:** protocol document for the `glm writer` folder. This folder contains the **journal-facing (submission) editions** of the programme's nine papers, produced by executing the per-paper venue passes registered in `DEEP_SCAN_RESIDUAL_POINTS.md` §1.2 and extended in `PUBLICATION_STRATEGY_JOINT_EVALUATION.md` §6. The internal editions (`papers/*/manuscript.md`, `manuscript_v2.md`; `wave_e_*/manuscript/*_v2.md`) remain untouched as the auditable record — the two-layer edition architecture of `research_program/paper_types_and_venues_decision.md` §5. Nothing in this folder modifies, replaces, or supersedes any existing repository file.

**How these editions were produced.** Each journal-facing edition is a presentation-level transformation of its internal edition: the mathematical content (every theorem, proof, number, table, verdict, and claim status) is preserved exactly; the internal scaffolding (series apparatus, edition notes, process vocabulary, internal identifiers) is removed or relocated to appendix inventories per the translation table below. The non-loss rule of the programme holds at every step.

---

## 1. The venue routing (adjudicated 2026-08-29, maintained)

| Paper | Internal edition | Journal-facing edition | Target venue (primary) | Article type |
|---|---|---|---|---|
| Paper 1 — Typed architecture and the separation theorem | `papers/paper1_general_theory/manuscript_v2.md` | `manuscript_v3.md` (the template) | Environmental Modelling & Software | Theory/methods |
| Paper 2 — Typed theorem atlas | `papers/paper2_theorem_atlas/manuscript_v2.md` | this folder | Set-Valued and Variational Analysis | Mathematics (proofs in ESM) |
| Paper 3 — Material ledgers and depletion diagnostics | `papers/paper3_material_ledgers/manuscript_v2.md` | this folder | Ecological Modelling | Methods/formal framework |
| Paper 4 — Delay-driven institutional dynamics | `papers/paper4_delay_dynamics/manuscript_v2.md` | this folder | Communications in Nonlinear Science and Numerical Simulation | Applied nonlinear dynamics |
| Paper 5 — Sampled governance, identification, falsification | `papers/paper5_sampled_governance/manuscript_v2.md` | this folder | ICES Journal of Marine Science | Methodology + case study |
| E1 — Northern cod forecast ladder | `wave_e_cod/manuscript/wave_E_cod_forecast_ladder_v2.md` | this folder | Fisheries Research | Empirical forecast evaluation |
| E2 — Northern cod intervention | `wave_e_cod/manuscript/wave_E_cod_intervention_v2.md` | this folder | Fisheries Research (short communication) | Applied management analysis |
| E3 — Edwards Aquifer forecast ladder | `wave_e_edwards/manuscript/wave_E_edwards_forecast_ladder_v2.md` | this folder | Groundwater | Empirical forecast evaluation |
| E4 — Edwards Aquifer intervention | `wave_e_edwards/manuscript/wave_E_edwards_intervention_v2.md` | this folder | Journal of Water Resources Planning and Management | Applied management analysis |

## 2. The non-loss rule (absolute)

The transformation is presentation-only. Specifically:

1. **No theorem, lemma, proposition, corollary, counterexample, conjecture, or definition statement is altered** — assumptions, conclusions, and claim statuses are preserved exactly.
2. **No number changes**: every interval, RMSE, Brier score, kernel horizon, percentage, and table value is carried verbatim from the internal edition.
3. **No result is dropped or demoted**: negative certificates and conditional results keep their first-class status.
4. **Every proof keeps its availability status** (in-manuscript / summarized with full proof in supplementary material / verified against source).
5. What changes: framing (abstract, introduction), vocabulary (translation table below), apparatus placement (ledgers → appendix inventories), scaffolding removal (series headers, edition notes, internal identifiers), and field-facing additions (roadmap paragraph, contribution statement, data-availability statement, target-field literature where registered as an obligation).

## 3. The venue-pass checklist (executed for each edition)

1. Strip header edition notes and series apparatus; companion file-path references become data-availability/supplementary pointers.
2. **Identifier genericization** (the submission-time fork resolved toward *genericize*, because these editions are prepared for submission before sibling papers are published): internal programme identifiers (R03, R04, A014, "general theory §15", E5, CC row tags) do not appear in journal-facing bodies. The rules they encode are restated as the study's own preregistered design or selection rationale.
3. Shared companion-layer apparatus: companions are described neutrally ("a companion study under separate review"), never cited as published literature.
4. Status ledgers and concordance tables become **Appendix A statement inventories** (two-table form, concrete bases, stipulation/validity legend, formal-validity-versus-empirical-applicability disclaimer) — the Paper 1 v3 pattern.
5. Process vocabulary out of the body: "row-verified", "second edition", "batch-5", "flagship", "adjudicated" (→ "evaluated"), "assured".
6. House style: en-dashes, notation defined at first use, acronyms expanded, consistent capitalization.
7. **Introduction lays out the roadmap**: a closing paragraph ("The remainder of this article is organized as follows…"). No table of contents anywhere.
8. **One-sentence contribution statement** in the introduction (venue-pass item 10).
9. **Skeptical-reviewer check** (venue-pass item 11): a referee at the target venue who has never heard of the programme can understand the paper standalone and find it valuable.
10. First-use **journal-gloss layer** for the programme's precise terms, with the two-layer caveat: the certified-kernel horizon is never glossed as the LRP-protection result — robust and certified layers stay distinct in every paraphrase.
11. E-paper E5 mentions are genericized to "an interval-verified linear template (a companion methodological study)" — the scope restriction itself is unchanged.
12. Reproducibility and data-availability statement: concrete (data sources with identifiers/DOIs, deterministic runners, pinned outputs, byte-identical reruns; code availability via the programme repository, anonymized copy for double-anonymous review).
13. Target-field peer-reviewed literature is engaged **only where registered as an obligation** (E3/E4) and only with real, verifiable references; the existing external reference lists are preserved.

## 4. The adjudicated translation table (verbatim from PUBLICATION_STRATEGY_JOINT_EVALUATION.md §3.1)

| Internal term | Disposition in journal-facing editions |
|---|---|
| "Wave E" | Absent from bodies (it already is); corpus label confined to internal registers |
| "The General Theory's §15 requires…" | The retention rule stated as the study's preregistered design |
| "R04-admitted fisheries object" | Selection rationale ("we selected the NAFO 2J3KL stock because…"); admission machinery to supplementary material |
| "Negative certificate" | **Kept** (term of art) with a first-use gloss: a machine-verified finding of non-retention / certified non-existence, distinct from a statistical null result |
| "Ω_2016 / Ω_xte" | Notation kept, defined in-paper at first use with descriptive glosses (Specification A, the 1983–2015 series; Specification B, the 1954–2024 extended series) |
| "A014 at corrected scalar-autonomous status" | "the autonomous surplus-production model, at its corrected status" |
| "Scored Forecast Ladder" | First-use gloss: a preregistered, scored model-ablation framework |
| "Certified kernel empty beyond T=5" | Exact claim kept; any paraphrase preserves the robust/certified two-layer distinction |
| "Typed architecture" | **Kept** as the framework's own vocabulary, defined at first use |
| "Claim status" | The discipline stated as a methodological commitment; statuses survive as the Appendix A inventory's organizing column |
| "Concordance" | "statement inventory" / "provenance inventory" (the discipline, renamed in presentation) |
| "Row-verified" | Concrete description ("each statement was verified against its source in a dated full-read campaign") |
| "Exact-tube", "proof obligation", "state space" | **Kept** (terms of art) |
| "13-slot tuple" | Kept, with source-faithful glosses |
| "Adjudicated" | "evaluated" |
| "Programme" | "research programme" / "this framework" (sparingly) |
| "Assured core" | "core papers" |

## 5. Format conventions for the journal-facing markdown

Each edition is a single markdown file beginning with a metadata block (parsed by the docx build):

```
% TITLE: Full Title of the Article
% VENUE: Target journal
% TYPE: Article type
% RUNNING: Short running head (≤ 60 characters)
% KEYWORDS: keyword one; keyword two; … (4–6)
% CONTRIBUTION: One sentence.

# Abstract
(150–300 words, venue-repositioned)

# 1. Introduction
(…ends with the roadmap paragraph…)

# 2. …
(body sections; LaTeX math $…$ and $$…$$ preserved from the internal edition)

# Appendix A. Statement inventory
(the relocated ledger, two-table form, concrete bases)

# References
(all external references preserved; author–year or numbered, consistent)

# Data and code availability
(concrete statement)
```

Figures (E-papers): `![Figure N](figfile.png)` references preserved; figure PNGs are copied into each paper's folder. Display equations in `$$…$$` blocks are preserved verbatim. Tables in pipe format are preserved. The Word (.docx) build applies: Times New Roman 12 pt body, 1.5 line spacing, justified paragraphs, 0.5-inch first-line indents, bold headings, three-line table style, hanging-indent references, running head, page numbers, title page, **no table of contents**, and a single page break after the title page.

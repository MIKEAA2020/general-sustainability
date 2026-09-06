# Wave 13 — Owner directive: date, clickable contact lines, back-matter Declarations, and the nine Zenodo DOIs

**Task ID:** 83 (owner-directed, confined to `arena agent 1/paper rewrites`; records in `batch 7 (audits of agent arena 1 paper rewrites)/wave13/`)

**Date:** 2026-09-06

## Directive (verbatim, four items)

> 1- date is September 6, 2026
> 2- put orcid and email in clickable format, all beneath author name
> 3- put ai declaration at end with other delcarations. each declaration should have separate title and subsection
> 3- substitute these dois for references

"These dois" = the nine Zenodo DOIs the owner registered in the ECOMOD v30 revision
(commit `7d10b03`, `agent 2 productivity illusion/` — read-only for this agent):

| DOI | Paper | Registered title |
|---|---|---|
| 10.5281/zenodo.22545740 | P1 | The Limits of Compensatory Aggregation: A Formal Separation of Weak and Strong Sustainability Assessment |
| 10.5281/zenodo.22554177 | P3 | Typed Flux Ledgers and Depletion Arithmetic: Conservation, Componentwise Diagnostics, and the Semantics of Depletion Horizons |
| 10.5281/zenodo.22552616 | P2 | An Obstruction Calculus for Viability under Incomplete Observation |
| 10.5281/zenodo.22554217 | P4 | Delay-Induced Regime Change in Harvested Stocks: The Mobilising and Protective Channels of Institutional Feedback, and the Review Interval as Control |
| 10.5281/zenodo.22554297 | P5 | Periodic Review as Sampled Governance: Sample-and-Hold Dynamics of Assessment-Driven Effort Control, a Selected 42-Stock Spectral Screen, and the Northern Cod Case |
| 10.5281/zenodo.22552060 | E2 | Robust viability of the 2J3KL limit reference point under a surplus-production map: policy scoring, expansion, and when catch cannot help |
| 10.5281/zenodo.22553609 | E1 | Does a surplus-production ladder improve forecasts of Northern cod? A scored test on NAFO 2J3KL |
| 10.5281/zenodo.22553311 | E4 | Governance operators and viability kernels of the Edwards Aquifer: an intervention-selection test at J-17 |
| 10.5281/zenodo.22552680 | E3 | Does a one-pool water-balance model improve forecasts of Edwards Aquifer head? A scored test at J-17 |

## Part A — reference substitution (md level, 8 new versions)

Method mirrors the owner's own ECOMOD v30 treatment: each placeholder entry
`Author, X., et al., in review. <stand-in title>. Companion ... study.` is
replaced by the real bibliographic record — `Abaee, A.` (2026), the registered
title, `Zenodo.`, the DOI URL — set in that paper's own house citation style,
keeping the paper's own companion descriptor tail verbatim. Titles use the
registered title text in each list's casing (sentence case, matching how the
same titles already appear in the papers' placeholder entries); stand-in titles
that did not match the real record (E2's and E3's "forecast-evaluation
scorecard", E4's "surplus-production intervention selection under a persistent
recharge/productivity floor", E1's shortened P5 title, P5's shortened P4 title)
are replaced by the registered titles. Two papers also cite a tenth manuscript
("Interval-verified bounds in linear management templates") that has **no DOI
among the nine** — those entries stay untouched; no DOI can be invented.

| New md version | Substituted entries | md5 |
|---|---|---|
| paperE1_cod_forecast_ladder_v15.md | A→E3 (22552680), B→P5 (22554297); C (interval-verified template) untouched | 41b8dee541 |
| paperE2_cod_intervention_v22.md | A→E1 (22553609), B→E4 (22553311); C untouched | 9074134ab4 |
| paperE3_edwards_forecast_ladder_v16.md | A→E1 (22553609) | 70290e4beb |
| paperE4_edwards_intervention_v14.md | A→E3 (22552680), B→E2 (22552060) | 80c73ea712 |
| paper1_assessment_separation_v23.md | A→P3 (22554177), B→E1 (22553609), C→E3 (22552680) | a7c836caf5 |
| paper2_obstruction_calculus_v13.md | A→P1 (22545740) | 76098e6960 |
| paper3_material_ledgers_v32.md | D→P4 (22554217), E→P5 (22554297), F→P1 (22545740) | 0837f3471e |
| paper5_sampled_governance_v26.md | D→P4 (22554217) | 9c7f2a4d92 |

15 substitutions total. **P4 stays at v30** — its reference list has no
companion-citation placeholder entries (its 14 "companion" mentions are body
prose). Fail-loud: every placeholder found exactly once; the new file differs
from its source ONLY on the substituted lines (line-level diff asserted); the
source file asserted byte-identical after the run; target names asserted
non-existent beforehand. Script: `wave13/apply_md_doi.py`.

## Part B — LaTeX/PDF (front matter, back matter; all 9 papers)

`wave13/build_latex_v13.py` = the wave-9/11 pipeline with three presentation
changes and one preamble fix; all fail-loud checks inherited.

1. **Date pinned** (item 1): `\date{September 6, 2026}`.
2. **Clickable contact lines beneath the name** (item 2): the wave-11
   `\thanks` footnote is removed; the `\author` block now reads
   `Amin Abaee / Independent Researcher / ORCID: 0000-0002-0019-1842 (hyperlink
   to https://orcid.org/0000-0002-0019-1842) / amin_abaee@ut.ac.ir (mailto
   link)`. Preamble fix required: `\usepackage{xcolor}` before hyperref —
   the `blue!45!black` link color mix was configured since wave 9 but never
   instantiated (no link was ever typeset), and plain `color` cannot mix; with
   real links the mix resolves and the links render in the house color.
   PDF-level check: all nine PDFs carry exactly the two URI annotations
   (`https://orcid.org/0000-0002-0019-1842`, `mailto:amin_abaee@ut.ac.ir`).
3. **Back-matter Declarations** (item 3): the papers' own declaration
   subsections are relocated (typesetting layer, Elsevier convention —
   declarations close the article) to a trailing `\section*{Declarations}`
   **after the references and supplementary material**, each as its own titled
   `\subsection*`, with the AI declaration appended as the **final**
   subsection:
   `GLM (Z.ai), Qwen (Alibaba Cloud) and DeepSeek AI assisted with drafting
   and iterative review.`
   Per-paper declaration inventory (paper's own heading text and order
   preserved; P2's single bold-label paragraph restructured into four
   subsections per "separate title and subsection"):
   - E1: Data availability, CRediT authorship contribution statement, Funding,
     Declaration of competing interest
   - E2: Data availability, CRediT authorship contribution statement,
     Declaration of competing interest
   - E3: Data Availability Statement
   - E4: Data Availability Statement
   - P1: Data availability statement, Declaration of competing interest
   - P2: Funding, Competing interests, Data availability, Code availability
     (restructured from the bold-label Declarations paragraph)
   - P3: Data availability, Declaration of competing interest
   - P4: Data availability, Declaration of competing interest
   - P5: Data availability, Author contributions, Funding, Conflicts of interest
   The "[To be completed at submission.]" CRediT/Funding/Author-contribution
   placeholders move verbatim (registered text; owner completes at submission).
   The `---` horizontal rules of P1/P3/P4 stay in place (registered separators).
   In-body prose mentions of "companion ... study (under separate review)" are
   registered text and untouched; the reference entries now carry the DOIs.
4. **References with DOIs** (item 4): built from the Part A md versions.

## Integrity verification

- Two full build runs: 9/9 compiled both times, all tex files byte-identical
  (md5s pinned below; idempotence assertions active).
- Every wave-9/11 check inherited and passing: pure-ASCII body; numeric-token
  multiset EXACTLY equal between markdown and LaTeX body (the relocated
  declaration text and the new DOI tokens stay inside the checked corpus — a
  pure relocation/addition cannot hide a value change); no markdown word lost;
  figure counts match; emphasis-mis-parse symptom absent; P4 body asserted
  identical to the wave-11 pandoc output (md unchanged) with the new file equal
  to the old after only the header, `\author`, `\date`, xcolor, and
  declaration-relocation substitutions.
- New assertions: front-matter needles (name, affiliation, href ORCID, href
  mailto, date); back-matter needles (Declarations section unique, AI
  declaration subsection last before `\end{document}`); `\thanks` absent.
- tectonic: exit 0, no missing glyphs, no TeX errors (logs in `wave13/logs/`).
- Overfull counts: E1 65 = wave-11's 65 (content identical, relocated); all
  others unchanged from their wave-9/11 levels.
- Page counts: E1 20, E2 19, E3 16, E4 14, P1 23, P2 **21** (was 20 — the
  restructured declaration subsections plus the AI declaration), P3 40, P4 39,
  P5 29.
- PDF-level structural check (PyMuPDF): all 9 page-1 bylines carry
  name/affiliation/ORCID/email/date; all 9 carry the two URI link annotations;
  the Declarations section is present in all 9 with the AI declaration on the
  final page in all 9 (for five papers the block starts on the penultimate
  page — long Data-availability sections).
- VLM verification (glm-5v-turbo): E2 page 1 — byline "Amin Abaee /
  Independent Researcher / ORCID: 0000-0002-0019-1842 / amin_abaee@ut.ac.ir"
  with the ORCID and email lines rendered as blue underlined links, date
  "September 6, 2026", no overlap; E2 last page — headings Declarations /
  Data availability / CRediT / Declaration of competing interest / AI
  declaration, each with its own heading, AI declaration last; P2 last page —
  the four restructured declaration subsections each with its own bold
  heading, AI declaration last, no layout issues; E1 references page — the
  two Abaee (2026) entries with Zenodo DOIs transcribed verbatim, the
  interval-verified-template placeholder correctly retained, DOIs as plain
  text in the list (the papers' existing bare-URL convention; the clickable
  links are the ORCID/email contact lines per the directive).

## Deliverables (tex md5s, second run)

| Output | md5 | pages |
|---|---|---|
| paperE1_cod_forecast_ladder_v15.tex | 4466bf78b4 | 20 |
| paperE2_cod_intervention_v22.tex | 1a4743250e | 19 |
| paperE3_edwards_forecast_ladder_v16.tex | 7ad65b4c65 | 16 |
| paperE4_edwards_intervention_v14.tex | 25f70d045e | 14 |
| paper1_assessment_separation_v23.tex | cdf1f0878f | 23 |
| paper2_obstruction_calculus_v13.tex | e89f0c9344 | 21 |
| paper3_material_ledgers_v32.tex | 6eb4efbbca | 40 |
| paper4_delay_dynamics_v30.tex | 4cee70f52e | 39 |
| paper5_sampled_governance_v26.tex | febf3ca965 | 29 |

Version discipline: the eight new tex/pdf pairs are new files under their new
canonical names (the current md versions); the old-version tex/pdf files
remain in `latex/` untouched; P4's tex/pdf regenerate in place under the same
canonical name (the owner's ECOMOD practice for generated artifacts), the
wave-11 original exactly recoverable at `dc1d501`.

## Non-destructiveness

- No existing paper md, supplementary, figure, or old-version tex/pdf file was
  modified (git shows: 8 new md, 8 new tex+pdf pairs, P4 tex/pdf regenerated,
  records). No frozen verdict, score, kernel, boundary, spectral record, or
  table value changed anywhere (numeric-token multiset asserted exactly equal
  for every paper).
- The owner's ECOMOD folder was read (the DOI registry) but not touched.

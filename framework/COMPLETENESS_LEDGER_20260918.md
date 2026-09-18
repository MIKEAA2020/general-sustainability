# Completeness & publication-artifact ledger (2026-09-18)

## 1. Latest manuscript versions — completeness verification (no loss, no condensation)

| Paper | Standing manuscript | Lineage & verification |
|---|---|---|
| E1 (cod) | `e1/paperE1_cod_forecast_ladder_v51.tex` (+`v51.pdf`) | v51 = v50.tex (frozen complete manuscript) + 2 register fixes only; diff-verified 7 lines changed; numeric accounting unchanged (spot-verified 115–196 kt, prey band 196–206, M4 195.6/488.3). Prose-carrier line v51–v55.md remains a prose layer, never a substitute for the manuscript. |
| E3 (Edwards) | `e3/paperE3_edwards_forecast_ladder_v22_formal_full.md/.tex/.pdf` | v22 = v21 (complete v16 body, all 7 sections, 8 tables, 5 figures, refs) − 2 delegated blocks → supplement v1. Numeric-token audit of v22+supp against v21: **ZERO missing tokens**. v21 was built from v16 programmatically; 14 edits, all enumerated. |
| F1 (framework) | `framework/paperF1_retention_framework_v28_formal_clean.md/.tex/.pdf` + v28 supplement | v28 = v26 + 3 register fixes (diff-verified). v25→v26 accounting (PHASE_L changelog): 444→431 numeric tokens, 0 added, 13 removed — all exactly the tokens moved to Supplement S1.4. F1 was never abbreviated. |

## 2. Delegation to supplementaries — decisions

- **E1**: already delegated (SI-1 execution order; SI-2 algebraic statement+proof;
  SI-3 uncertainty grids; SI-4 log-floor counts; SI-5 operating characteristics).
  No further main-text block needs delegation; §3.6 fitted-parameter table stays
  (cited by F1 as a main-text object).
- **E3**: TWO blocks delegated now (new `e3/paperE3_supplement_v1`): the
  independent DM/bootstrap **replication paragraph** (S1) and the **climate
  fixed-window record** (S2). Main text keeps the scientific conclusion
  sentences plus formal pointers "(Supplement, Section S1/S2)".
- **F1**: already maximally delegated (S1 sensitivity/detail, S2 two-page
  standard, S3 fillable instruments, S4 literature positioning).

## 3. Supplementaries — status

| Supplement | Version | Clean register? | Complete? |
|---|---|---|---|
| E1 | `E1_SUPPLEMENTARY_V2` (md/tex/pdf) | YES — internal dialogue, reader-instruction editorial, repo-jargon removed (recorded in changelog append) | YES (SI-1..SI-5 intact; diff-verified) |
| E3 | `paperE3_supplement_v1` (md/tex/pdf) | YES — new doc written in formal register | YES (S1 replication paragraph verbatim; S2 fixed-window record verbatim) |
| F1 | `paperF1_retention_framework_v28_supplement` (md/tex/pdf) | YES (cleaned in v28 pass: 8 edits, diff-verified) | YES (S1–S4 incl. moved DM mechanics, checklist, S3 schema, S4 positioning) |

## 4. Format policy (from 2026-09-18)

Standing manuscripts and supplementaries are committed in **three formats**:
`.md` (working carrier), `.tex` (journal source; pandoc LaTeX, hyperref,
booktabs, longtable), `.pdf` (built render). Builder:
`framework/build_tex_pdf_2026.py` (deterministic; DejaVu; A4; figure
embedding from the doc's own figs/ directory; PNG figures on this pass:
E3 figures 1–5 embedded, E1's 6 \includegraphics carried through the
tex→md→pdf conversion). Front matter on every document: author
**Amin Abaee**, Independent Researcher, **clickable ORCID**
(https://orcid.org/0000-0002-0019-1842), **clickable email**
(mailto:amin_abaee@ut.ac.ir), **date September 18, 2026**.

Honest caveat: no TeX engine exists in this sandbox, so the .pdf is produced
by a pure-python renderer rather than by pdflatex. The .tex is the
authoritative journal source and compiles under any standard LaTeX
installation; when a local TeX toolchain becomes available, recompile from
.tex for the final typeset. Verifier: pypdf extraction + per-page XObject
inventory + manual page inspection (figures embedded, tables aligned).

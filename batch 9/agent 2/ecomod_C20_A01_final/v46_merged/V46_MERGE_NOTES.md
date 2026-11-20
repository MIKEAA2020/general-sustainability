# ECOMOD v46 — merged revision: what was taken from where

**Base:** `ecomod_C20_A01_main.tex` (the version in EM submission).
**Rule applied:** nothing from `\section{Methods}` onward was touched. Verified byte-identical.
Consequence: every number, proposition, table, figure, citation key and scope claim is exactly as in C20.

---

## 1. Title

**Chosen: "Rising biocapacity, falling ecological capital: how aggregation conceals composition"**

Why this one:

| Candidate | Verdict |
|---|---|
| *A rising biocapacity total can mask ecological-capital land drawdown: a two-land model* (C20) | Accurate but reads as a model paper; the contribution (identifiability) is absent; "can mask" is weaker than what is proved. |
| *How aggregation can conceal composition: aggregate biocapacity and the identifiability of modelled ecological-capital drawdown* (v35–v44) | Honest and complete, but 17 words of title-case jargon; "modelled" is a hedge in the title. |
| **Rising biocapacity, falling ecological capital: how aggregation conceals composition** | Names the observable phenomenon (one rising, one falling), then names the result (aggregation conceals). 11 words. Keeps "biocapacity" and "ecological capital" as the two objects. Does not claim physical decline, does not say "model", does not hide the mechanism. |

It is honest in the specific sense that matters here: it describes what the paper shows
(an accounting/aggregation result about the model's two books) and makes no empirical claim about
real-world land. "Ecological capital" is the model's *ecological-capital land class*, which is the
paper's own term.

## 2. Abstract — 238 words (EM limit 250), merged from three versions

| Element | Source | Change |
|---|---|---|
| Opening | v42's "headline index of bioproductive supply is a single number assembled from heterogeneous land accounts" | Reused the *move* (state the object, then the question), not the sentence. |
| The identifiability result | **v35–v42** | **Restored.** C20's abstract never states it. Now: "the aggregate alone cannot identify that this has happened: the same total is consistent with genuine growth and with compositional loss." |
| 39 % / ≈46 % / 51.72 % | C20 | Unchanged. |
| Budget figures | C20 → rounded | `0.547925` → **about 0.548 gha**; `0.231310` → **about 0.231 gha**. Exact values remain in §3.6. No version before the C-series put six decimals in an abstract. |
| No fold / no critical slowing | C20 | Unchanged, including "specific to that comparison". |
| NFA 1961–2023 figures | C20 | Unchanged (24.86 %, 52.71 %, 16.73 %, +24.06/−5.95/+7.44 pp). |
| Closing | new | Ends on the finding, not on a list: reporting constituent accounts alongside independent measurement. |

Absent from the new abstract on purpose: no claim of measured physical decline, no "critical slowing
down" as a finding (it is a *negative* result in the paper), no added scope.

## 3. Introduction — 1,307 words, merged

| Paragraph | Source | Status |
|---|---|---|
| 1. Carrying capacity, the moving ceiling | **v41 P0** | Restored (citation converted to `\citep`). |
| 2. The orchard with two kinds of ground | **v41 P1** | **Restored verbatim.** |
| 3. "The arithmetic is the arithmetic of any productive stock" — orchard/eggs/**hens** | **v41 P2** | **Restored verbatim.** This is the paragraph the C-series lost entirely. |
| 4. Literature framing | **C20** | Kept (accurate, and its 1961–2023 scope matches the paper). |
| 5. Productivity illusion + **elevator** | **v41 P7** | **Restored verbatim**, including "judged by what it delivers the elevator still runs; judged by its reserve it is already failing." Replaces the "the ride itself does not establish" sentence. |
| 6. The composition illusion | **v41 P8** | Restored; citation form corrected to `\citep{Abaee2026c}`. |
| 7. Questions + evidence | **v42's Q1–Q3 + v44's observable/rejection clause** | Restored as questions, merged into one paragraph. |
| 8. Core contributions | **C20** | **Unchanged**, including "These are conditional model results, not general claims about observed ecosystems." |
| 9. Closing caveats | **C20** | **Unchanged** (five conditional predictions, representative parameters). |

Removed from the introduction: the "This is a conditional model mechanism, not evidence that NFA
accounts measure physical stocks…" and "does not assert that the classes map directly to NFA
categories" clauses. They are not lost as *claims*: the same qualifications survive in the
contributions list, in the closing paragraph, in §3.7 and in the SI. What is removed is the
repetition of them inside the analogy.

## 4. Verification

| Check | Result |
|---|---|
| `pdflatex` ×2, `nonstopmode` | **0 errors** |
| Undefined references/citations | **0** |
| Page count | **39 pp** (C20 was 38; +1 from the longer, restored introduction) |
| Abstract word count | **238** (EM limit 250) |
| Methods → end identical to C20 | **True** (byte comparison) |
| Decimal numbers vs C20 | Only `0.548` / `0.231` added (the rounded abstract forms). **Nothing removed.** |
| Portal-safe build (`\input` inlined, figures guarded) | **38 pp, 0 errors** |
| Introduction sentence length | 24.7 words avg (C20: 19.7 but with 0.34 apologies/1k; v41: 25.4) |

## 5. Files

- `recovered_prose/` — source of title/prose options
- `series_audit/` — the 36-version audit behind the choices
- `ecomod_v46_merged/ecomod_v46_main.tex` + `.pdf` (39 pp)
- `ecomod_v46_merged/Manuscript_ECOMOD_v46_portalsafe.tex` (38 pp, portal-safe)
- `build_v46.py` — the edit is scripted and reversible; it asserts every match before replacing

**Not included, deliberately:** no change to the SI, no change to `Highlights_`, no change to the
Zenodo package, and no re-issue of the C20 deposit. If you accept v46, those follow as a separate,
explicit step.

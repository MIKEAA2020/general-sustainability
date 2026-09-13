# Joint Evaluation — Humanized Rewrites (V11) → v25_restructured (2026-09-13)

Two full humanized rewrites of v24_restructured were received (`uploads/humanized
framework.txt`: a Grok rewrite, 72,596 chars, and a Gemini rewrite, 68,264 chars).
Evaluated jointly on the four requested axes; contradictions adjudicated before
implementation; the merged result is v25.

## 1. Drift audit (before any adoption)

| Check | Grok | Gemini |
|---|---|---|
| Numeric tokens vs v24 | **0 fabricated** (21 absent = reference pages/DOIs only) | **28 candidate-only** (incl. unarchived M1 CI [−0.954, +0.180], oracle 10.865, 612.5 ft) |
| v24 numbers dropped | 21 (all in the dropped References block) | 146 (heavy compression) |
| Content headers | 20/20 present + References missing | restructured (renumbered tables) |
| Adjudicated strings | all present (companion titles/DOIs, class grounds, mechanism misattribution, M4/M5, §8 executed paragraph) | **violated**: fabricated companion titles ("Hydrogeological Model Elaboration…", "Companion Monograph"), Zenodo labels swapped (E1/E3), M5 title changed, Carvalho/Kell references swapped for different papers |

**Adjudication:** Grok = faithful humanization (adopted as the v25 base, frozen as
`v25_source_grok_rewrite.md`). Gemini = readable but drifty (harvested selectively).

## 2. What each rewrite contributed (four axes)

- **Humanized.** Grok: long telegraphic sentences split into short declarative ones
  ("The standard in one page: three obligations, portable and domain-free. (1) …"),
  em-dash chains unwound, "fibre"-style remnants already gone. Gemini: numbered
  lists, topic sentences, but with an LLM-register ("We demonstrate…") the paper's
  single-author register rejects.
- **Seamless flow.** Grok: bolded topic sentences added in §6.4 ("Power is low for
  three of four in-class structural processes; the cause is identification, not the
  gates."), which v24 lacked — adopted via the base. Gemini: good transition
  paragraphs but renumbered tables and added ASCII diagrams — rejected (journal
  register; the prose already carries the content).
- **Enhancing.** Adopted: (a) Gemini's abstract forward-reference — the criterion
  "applied alone … would retain the structurally redundant module the standard
  withholds" (consistent with the O9 co-primary check); (b) Gemini's §2.3
  derivation — constant training-mean fluxes fold into a single intercept, leaving
  an affine autoregression.
- **Weaknesses addressed (our paper's, exposed by the rewrites):**
  - **NEW-5 (citation defect, fixed):** the M4 reference said "54 methods" — the
    published title is "The M4 Competition: 100,000 time series and 61 forecasting
    methods" (IJF 36(1), 54–74; verified against the publisher record). Fixed to
    61; Gemini's "61" was right.
  - **NEW-6 (rejected):** Gemini's fabricated companion titles/DOI labels — the
    O7-verified titles and Zenodo records stand.
  - **NEW-7 (rejected):** Gemini's unarchived numbers (M1 CI [−0.954, +0.180],
    oracle 10.865, 612.5 ft historical low) — no unarchived number enters the
    paper.
  - **NEW-8 (rejected):** Gemini's Carvalho/Kell reference swaps — different real
    papers, not ours (ours: Fisheries Research 240, 105959; ICES JMS 78,
    2244–2255).
  - **NEW-9 (rejected):** Gemini's M5 title ("Background, organization, and
    results", 1347–1364) — the cited paper is "M5 accuracy competition: results,
    findings, and conclusions", IJF 38(4), 1346–1364.
  - **Regression caught and fixed:** the Grok base made three passages verbatim-
    identical again (the §9 Spec A interval sentence; the collapse-reproduction
    sentence) — the Phase F2 redundancy discipline reapplied (V11-05/06), and two
    typographic normalizations that broke scanner conventions (≈ spacing,
    Diebold–Mariano hyphen) restored (V11-07/08).

## 3. Verification

- Numeric drift v24→v25: **none** (386 = 386 tokens, exact set equality).
- Idempotent re-apply byte-identical; formalization 0 flags; redundancy 0
  findings; style PASS; content coverage vs v0 and v13 clean (all numeric claims,
  30/30 terms incl. Diebold-Mariano).
- Contradictions adjudicated this pass: NEW-5…NEW-9 (5), none outstanding.

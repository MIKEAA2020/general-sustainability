# Full-lineage content audit — E1 v49 (33pp) → v63 (26pp)

**Date:** 2026-09-18 · **Trigger:** owner question "why is v62 only 26 pages despite additions like Appendix A? v49 was 33 pages!"
**Method:** (1) page counts from PDF carriers; (2) per-chapter word census after LaTeX/markdown normalisation; (3) load-bearing motif presence matrix (26 terms) across v49, v51r, v52, v53, v54, v55, v56, v63; (4) 8-gram paragraph coverage (guarded: 8-grams fail under paraphrase, so the motif matrix is the load-bearing test); (5) per-step numeral-loss batteries (already executed at every patch v56→v63).

## Headline

33 pages → 26 pages is **documented, owner-directed register condensation** (v52–v56 "humanized/formal" rounds; directives msg14–16: "gemini register = base"; "brief but NOT at cost of substance"), NOT unexplained loss. **Zero numerals lost at every step v56→v63; zero load-bearing scientific motifs lost; tables grew 15→16; references constant.**

## Page & chapter census (normalized words)

| Chapter | v49 (33pp; 19,324w) | v63/v64 (26pp; 12,647w) | Δ |
| --- | ---: | ---: | ---: |
| 1. Introduction | 1,134 | 1,166 | +32 (scope + object ¶) |
| 2. Methods | 4,416 | 2,065 | −2,351 (−53%) |
| 3. Results | 10,153 | 4,993 | −5,160 (−51%) |
| 4. Discussion | 3,295 | 2,044 | −1,251 (−38%) |
| 5. Conclusions | 348 | 231 | −117 |
| Appendix A | — | 951 | +951 (new in v57) |
| References | ~1,113 | 1,095 | −18 (51 entries both) |

Structural assets: v49 = 15 longtables + 6 figures; v63 = 16 tables (v59 added Table 12b) + 4 figures (registry-consistent). **The condensation removed expository "Readings"/interpretation prose around the tables, not the tables, objects, or numbers.**

## Motif matrix (load-bearing concepts present at each stage)

Of 26 motifs scanned (Edwards Aquifer cross-ref; Rose 2026 analysis; implied productivity; rK/4 production multiplier; net-production collapse sign; MASE; DM; moving-block bootstrap; Brier; log-RMSE; numerical floor 10⁻³; identifiability; multi-start bounds; information availability; AR-residual; DFO 2009 precautionary; capelin Zenodo provenance; collapse-window r bound; stock-flow; survey-start; D1–D5 simulation; specificity; hindcast; retention rule): **all present in v49 → present in v56 → present in v63** (the two apparent absences were artefacts of the scan patterns, verified by direct grep). 8-gram "missing" flags are paraphrase artefacts of the v58 positive-register rewrite and were each resolved manually to retained substance (e.g., capelin Zenodo provenance — now in the Data-and-Code section; "Readings" DM narrative — carried by the frozen DM tables and later by §3.5/§3.8).

## Where the condensation happened (per-owner record)

- v49 (19,324w, 33pp, LaTeX) → v52/v53 humanized/gemini-weighted drafts → v54/v55 formal → **v56 humanized (10,715w, 24pp)** — one large owner-ordered register pass.
- v56→v64 chain adds back scientifically: v57 +918 (Appendix A, scope ¶), v58 −73 (positive-register abstract, keywords line casualty — **restored in v63**), v59 +771 (Spec C §3.8), v60 +279 (q̂, §4.3 centerpiece), v61 +20, v62 +2, v63 +1 line, v64 declarations fixes.
- Numeral-loss battery at every v56→v64 step: **0 lost**.

## Defects found and fixed in v64 during this audit

1. **CRediT + Funding were live placeholders** ("[To be completed at submission.]") — replaced with the owner-supplied text ("A.A conceptualized the entire work, wrote, reviewed and edited the manuscript." / "No funding received.").
2. **Competing-interest heading unbolded** — now **bold**, matching the CRediT/Funding headings.
3. **Mangled `verbatim` artefact** (dangling word + unhelmed command listing in A.7) — restored to a fenced code block.

Delta v63→v64: exactly those four edits; zero numerals touched.

## Optional restoration menu (available on request, mined from v49.tex, largest first)

These are the long expository blocks condensed away — all scientifically restorable without touching any frozen numeral:
1. §3-era Specification A "Readings" narrative (~393w, DM margin discourse);
2. Window-by-window origin-period narratives, incl. the Spec-B collapse/recovery windows (~343w) and the M1/M1b annual-landings window disclosure (~326w);
3. Implied-maxima / production-multiplier derivation (~353w + 267w, §2/§4 economics-of-map reading);
4. Log-RMSE floor caveat (~271w) and 8-gram-flagged parameter-estimation narrative (~363w → partially in A.4);
5. Cross-system Edwards Aquifer comparison expansion (~222w, presently 1 sentence in §4);
6. Two explicit scope-limits paragraphs (~233w + 190w) on identifiability and non-stationarity algebra.

**Verdict:** no unexplained loss; condensation is intentional and object-preserving; the only true casualties to date were the keywords line (fixed in v63) and the declarations placeholders (fixed in v64). The paper is suitable as-is; restoring menu items is a length-vs-depth choice, not an integrity requirement.

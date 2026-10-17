# Paper09b v6 layout audit — 2026-10-17

## Lineage and version check

The fresh all-ref scan found Paper09b v5 as the highest version on the audited refs; no v6 path existed. The latest source is `arena agent 1/agent workspace/papers/paper09b_arv_certification_v5.tex` on `e2-v3-source-year`, blob `e7c13c59f1228508b5f918c6c31a956aad838807`. The local v5 base was byte-identical to that blob. The v5 source and all earlier editions are preserved.

The branch/tag/release inventory and commit IDs checked are recorded in `PAPER08_V50_LAYOUT_AUDIT_2026-10-17.md` and the combined successor audit. The v5 reproducibility package remains the cited unchanged package; no duplicate v6 code/data package was created.

## Change scope and content preservation

A normalization check that reverted only the edition/date metadata, the lemma display reflow, and the summary-table layout reproduced the v5 source exactly. No threshold, numerical entry, scientific statement, data source, or conditional qualification changed.

The manuscript continues to distinguish assessment SSB from reported landings/catch; converts the landings data from tonnes to kilotonnes; treats `\(\kappa\ge0\)` as unknown; shows both `\(C_t\)` and `\(C_{t+1}\)` alignments; and states only the conditional strict certificate `\(\kappa<\kappa^*\)`.

## Checks, build, and inspection

- `verify_kappa_thresholds.py` passes: source rows, 70 adjacent-year band pairs, tonne-to-kiloton conversion, exact arithmetic, threshold values, and both accounting identities.
- Engine: Tectonic 0.15.0; verified binary SHA-256 `f0b36e78c13dd75b821984830533f872c9a12c62957e51357bc16e65cdb71013`.
- Output: 9-page PDF, 7,578 extracted words, zero blank pages.
- Warnings: zero overfull boxes; 18 underfull boxes. No LaTeX errors or unresolved explicit references/citations.
- Visually inspected p.3 (lemma) and p.8 (summary Table 3). Equations and table cells are fully readable; the summary table now spans both columns without overlap.
- PDF SHA-256: `31976e3a9e2f1f15a60d20f14dc657a399621c3f9e221150a4865bb9594276e1`.

Full engine output and figure dependency blob hash: `paper09b_arv_certification_v6_BUILD_LOG_2026-10-17.txt`.

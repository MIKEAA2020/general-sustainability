# Paper10b v4 layout audit — 2026-10-17

## Lineage and version check

The fresh all-ref scan found Paper10b v3 as the highest version on the audited refs; no v4 path existed. The latest source is `arena agent 1/agent workspace/papers/paper10b_edwards_aquifer_v3.tex` on `e2-v3-source-year`, blob `fd0d0c4b75c8e2c518b891c8173e3156704ef47c`. The local v3 base was byte-identical to that blob. V3, v2, and v1 are preserved.

The branch/tag/release inventory and commit IDs checked are recorded in `PAPER08_V50_LAYOUT_AUDIT_2026-10-17.md` and the combined successor audit. The reproducibility package `paper10b_edwards_aquifer_v3_src/` remains the cited unchanged v3 package; no duplicate v4 code/data package was created.

## Change scope and content preservation

A normalization check that reverted only the edition/date/header, URL markup, filename/path rendering, and related relative-path edits reproduced the v3 source exactly. There are no changes to the frozen protocol, calculations, bootstrap outputs, results, or scientific interpretation.

## Checks, build, and inspection

- `verify_660_attractor_bootstrap.py` rerun in a temporary copy of the v3 package: `valid=5000`, `noncontractive=0`, `gamma>=0=0`; zero-pumping point attractor `647.32` ft; 5th/50th/95th percentiles `628.99/647.33/661.16` ft; share at or above 660 ft `0.0688`. Recomputed CSV outputs byte-match the unchanged v3 package.
- Engine: Tectonic 0.15.0; verified binary SHA-256 `f0b36e78c13dd75b821984830533f872c9a12c62957e51357bc16e65cdb71013`.
- Output: 18-page PDF, 9,581 extracted words, zero blank pages.
- Warnings: zero overfull boxes; four underfull boxes. No LaTeX errors or unresolved explicit references/citations.
- Visually inspected p.16 (both long EAA URLs) and p.17 (repository and code paths). Both links wrap within the text block; the relative v3 package path and the verification filename remain legible.
- PDF SHA-256: `9d36dae27aa737ab4d8a5d32dbdc3f38208b4e2cb10f6c116e1cbee4eb86285a`.

Full engine output and figure dependency blob hash: `paper10b_edwards_aquifer_v4_BUILD_LOG_2026-10-17.txt`.

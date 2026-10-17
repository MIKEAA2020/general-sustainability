# Paper10b v4 changelog — 2026-10-17

**Base:** Paper10b v3, the latest version found on the audited refs. V3, v2, and v1 remain unchanged. This is a layout-only successor.

## Layout corrections

- Made both long Edwards Aquifer Authority reference URLs breakable with `\url{...}`; the PDF and Critical Period/Drought Management links no longer run beyond the text block.
- Replaced the nonbreaking code filename with a breakable path form and shortened the v3 code-package references to unambiguous paths relative to the `papers/` directory. This also avoids rendering the repository's space-containing parent folders without spaces.
- Updated the version/date header only. The frozen scoring protocol, tables, bootstrap results, and interpretation are unchanged.

## Build

Tectonic 0.15.0 produced the v4 PDF (18 pages). The clipped reference URL and all overfull boxes are cleared. Full build details, hashes, deterministic verification, and visual inspection are in `paper10b_edwards_aquifer_v4_BUILD_LOG_2026-10-17.txt` and `PAPER10B_V4_LAYOUT_AUDIT_2026-10-17.md`.

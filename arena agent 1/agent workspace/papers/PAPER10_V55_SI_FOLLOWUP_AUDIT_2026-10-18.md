# Paper10 v55 SI follow-up audit — 2026-10-18

## Scope and version scan

This is a supplementary-material follow-up to the existing Paper10 v55 main text, not a new main-text edition. After the stale v54 SI build-status/companion metadata was identified, the user directed continuation. A fresh pre-numbering scan checked all six repository branch tips, both tag tips, and both GitHub release records/assets. It found Paper10 v55 as the latest main text on `e2-v3-source-year` (pre-scan head `864dc85672e2e6be2e33530f86e6a0cc5b767de4`), and v54 as the latest supplementary edition; no v55 SI path existed before this follow-up.

Branch tips at scan:

- `archive/paper3-v48-workspace` — `0200b6dc75a51feb40728df07e855facbb791383`
- `e2-v3-source-year` — `864dc85672e2e6be2e33530f86e6a0cc5b767de4`
- `edwards-framework-e1-audit-implementation` — `2bdf39ff1c13357a44c48b5ed7385c9945aff0b5`
- `edwards-framework-e1` — `66a0a71f976e76df403425e85690d2c9dcb4c141`
- `lean-audit-v4` — `c2fe8fca63384cbf9243434d4213c6e74543a840`
- `main` — `1ba3d3c8a286a055b1342b5102731b601ec3d428`

Tag tips:

- `edwards-framework-e1` — `60d8c6b10f27e8231d9dfb0dd9d5e87345b3305e`
- `compendium-v1.0` — `504f78e176ca25da88ba487571aa4a674299ace3`

The releases `compendium-v1.0` (published 2026-09-04) and `edwards-framework-e1` (published 2026-09-12) predate Paper10 v54 and have no Paper10-named assets; their ZIP payloads were not unpacked. Their tag tips were included in the tree scan. The current remote `VERSION_CURRENCY.md` was byte-matched to the local current copy before this update. The current remote split note is blob `16848adcf14e1814140d73981737c6b71e7cf90d`; the local context copy differs, so the remote note was used for the split/lineage disposition. Paper10b/E4 remains the separate Part II Edwards-aquifer line.

The current v54 SI source/PDF and SI build log were fetched from the e2 branch and byte-matched to the local files before this follow-up. The v54 SI PDF is 19 pages and its source/PDF/log remain unchanged.

## Source comparison and correction

The v54 SI source header said “no compiled v54 PDF is claimed,” although the v54 SI PDF exists and its build log is published. Its displayed date and companion line also still identified Paper10 v54. The new v55 SI source updates the source-header edition/date, title-page date, and companion line; it removes the stale no-PDF claim and states that v54 remains preserved. Reverting exactly those metadata/comment changes yields an exact byte-for-byte match to `paper10_depletion_ledgers_v54_supplementary.tex`. No substantive SI content changed, and the v55 main text/PDF were not changed.

## Build and visual QA

- Engine: Tectonic 0.15.0; default bundle v33 / `tlextras-2022.0r0`.
- Output: 19-page SI PDF, 179,739 bytes.
- Diagnostics: 0 overfull boxes, 6 underfull boxes (inherited from the v54 layout), 0 LaTeX errors, 0 undefined references/citations.
- Visual inspection: page 1 confirms the October 18, 2026 date and Paper10 v55 companion statement; page 19 shows no clipping or overlap.

## Hashes

- v55 SI TeX SHA-256: `20f4cbd1bfadd547d64ee7c35254784f8d856bfb7599a9437d110729249da06e`
- v55 SI PDF SHA-256: `cb3be5e77779f8b376a9f1357e8c5973f529d2d4ed0b9250a67394792ebe61fd`
- v55 SI build-log SHA-256: `4d12ebdf22e4136544360e035b7d0e7d3243839306e7e8023f9916ab87de7c5f`
- Preserved v54 SI source SHA-256: `4c646e7e75a764e40559d479359518a2c6c4cbbc99682a89b7cc92d52ff356b2`
- Preserved v54 SI PDF SHA-256: `cb75349d4657707119d329548ab1ef124770a62dc1ebd11dd535a63f79d13013`

Publication and remote-byte verification are recorded in `PAPER10_V55_SI_PUBLICATION_RECEIPT_2026-10-18.md`.
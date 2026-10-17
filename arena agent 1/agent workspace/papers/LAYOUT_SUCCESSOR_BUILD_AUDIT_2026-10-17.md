# Layout-successor build audit — 2026-10-17

## Scope and version currency

This audit covers the user-authorized layout-only successors Paper08 v50, Paper09b v6, and Paper10b v4. Earlier sources and editions remain preserved. The audit is limited to layout and version/date/path-rendering changes; it does not revise scientific content or results.

A fresh all-ref scan checked the six branch tips, both tag tips, and both GitHub releases. The highest versions were Paper08 v49, Paper09b v5, and Paper10b v3; no v50/v6/v4 path existed. `e2-v3-source-year` was at `e8367e820cb75f3f609ac7b43c47b5b7d689ea87` at scan time. The complete refs were:

- Branch `archive/paper3-v48-workspace`: `0200b6dc75a51feb40728df07e855facbb791383`
- Branch `e2-v3-source-year`: `e8367e820cb75f3f609ac7b43c47b5b7d689ea87`
- Branch `edwards-framework-e1-audit-implementation`: `2bdf39ff1c13357a44c48b5ed7385c9945aff0b5`
- Branch `edwards-framework-e1`: `66a0a71f976e76df403425e85690d2c9dcb4c141`
- Branch `lean-audit-v4`: `c2fe8fca63384cbf9243434d4213c6e74543a840`
- Branch `main`: `1ba3d3c8a286a055b1342b5102731b601ec3d428`
- Tag `edwards-framework-e1`: `60d8c6b10f27e8231d9dfb0dd9d5e87345b3305e`
- Tag `compendium-v1.0`: `504f78e176ca25da88ba487571aa4a674299ace3`

The two releases contain only workspace ZIP assets; their ZIP payloads were not unpacked. No paper-specific successor asset was found. `VERSION_CURRENCY.md` and the applicable split/lineage notes were reviewed. The base sources were locally byte-verified against their current branch blobs:

| Successor | Latest base source on `e2-v3-source-year` | Base Git blob | New source SHA-256 |
|---|---|---|---|
| Paper08 v50 | `arena agent 1/agent workspace/papers/paper08_governance_delay_v49.tex` | `956b050cf0d6919b862a88a03ad0becffd0013c3` | `efaec8316aa84bc5c5a6ce1802e63d208f4c58301c1daac6878038658ce9b9ac` |
| Paper09b v6 | `arena agent 1/agent workspace/papers/paper09b_arv_certification_v5.tex` | `e7c13c59f1228508b5f918c6c31a956aad838807` | `14837382936d36f070432a859a9395f0368bb2ead537e83b8db2196d9eb4ec0e` |
| Paper10b v4 | `arena agent 1/agent workspace/papers/paper10b_edwards_aquifer_v3.tex` | `fd0d0c4b75c8e2c518b891c8173e3156704ef47c` | `f50c69ba96c710098e0f34359d7ddcd10e2ca5e6f3c7b223356d548e533e9ce2` |

## Source-integrity check

For each successor, a normalization script reverted only the version/date metadata and the specific layout/path-rendering substitutions. The normalized successor source then matched its base source exactly. Thus the underlying scientific text, numerical values, equations, assumptions, and results are unchanged. Per-paper change logs identify the visible edits.

## Build and PDF checks

All three sources built with Tectonic 0.15.0. The binary was SHA-256 verified as `f0b36e78c13dd75b821984830533f872c9a12c62957e51357bc16e65cdb71013`.

| Successor | Prior PDF page count | New PDF page count | Extracted words | Blank pages | Overfull boxes | Underfull boxes | PDF SHA-256 |
|---|---:|---:|---:|---:|---:|---:|---|
| Paper08 v50 | v49 candidate: 87 | 87 | 50,342 | 0 | 0 | 9 | `d65ad6306a57226db656321fe47a4fd21e8bd9190e28917791a1017b2a374bd6` |
| Paper09b v6 | v5 candidate: 9 | 9 | 7,578 | 0 | 0 | 18 | `31976e3a9e2f1f15a60d20f14dc657a399621c3f9e221150a4865bb9594276e1` |
| Paper10b v4 | v3 candidate: 18 | 18 | 9,581 | 0 | 0 | 4 | `9d36dae27aa737ab4d8a5d32dbdc3f38208b4e2cb10f6c116e1cbee4eb86285a` |

No LaTeX errors or unresolved explicit references/citations were found. Underfull warnings remain, but no overfull boxes remain in any candidate. Paper08's Tectonic run also reports an invalid UTF-8 byte in the bundled `lineno.sty` line 296 and replaces it with U+FFFD; this is external to the manuscript source and produced no visible defect in the inspected pages.

## Per-paper verification and visual inspection

### Paper08 v50

- The old three-column interval table visibly overlapped. It is now a compact point-value table plus a wide exact-certificate table, with one interval per row; all point values and all six interval enclosures are legible.
- The flipped-gain expressions, boundedness threshold, four-state equilibrium vector, and long MPF parameter tuple are set in readable displays.
- The v49 supplementary delay and governance files are explicitly carried forward unchanged; no v50 SI was created.
- Rendered pages 11, 18, 24, 35, and 86 were visually inspected. PDF remains 87 pages.
- Detailed record: `paper08/PAPER08_V50_LAYOUT_AUDIT_2026-10-17.md`; change log and Tectonic log accompany it.

### Paper09b v6

- The conditional multiplier lemma's two accounting placements now stack cleanly.
- Summary Table 3 now spans both columns with wider columns; the values and units are unchanged.
- `verify_kappa_thresholds.py` passes: source rows, 70 adjacent-year band pairs, tonnes-to-kilotonnes conversion, exact arithmetic, threshold values, and both accounting identities. The paper retains unknown nonnegative `kappa`, both `C_t` and `C_{t+1}` alignments, and only the strict conditional `kappa < kappa*` certificate.
- Rendered pages 3 and 8 were visually inspected. PDF remains 9 pages.
- Detailed record: `paper09b/PAPER09B_V6_LAYOUT_AUDIT_2026-10-17.md`; change log and Tectonic log accompany it.

### Paper10b v4

- Both long Edwards Aquifer Authority URLs now wrap within the reference text block; code filenames and relative v3 source-package paths are also legible.
- The unchanged v3 bootstrap package was rerun in a temporary copy. It reports `valid=5000`, `noncontractive=0`, `gamma>=0=0`; the zero-pumping point attractor is 647.32 ft, its 5th/50th/95th percentiles are 628.99/647.33/661.16 ft, and the share at or above 660 ft is 0.0688. Recomputed CSV outputs byte-match the v3 package.
- Rendered pages 16 and 17 were visually inspected. PDF remains 18 pages.
- Detailed record: `paper10b/PAPER10B_V4_LAYOUT_AUDIT_2026-10-17.md`; change log and Tectonic log accompany it.

## Output files

The three source/PDF pairs, dated build logs, per-paper change logs, and per-paper layout audits are stored in the corresponding `paper08/`, `paper09b/`, and `paper10b/` workspace folders. The living `VERSION_CURRENCY.md` now records the authorized successors without removing the prior edition history.

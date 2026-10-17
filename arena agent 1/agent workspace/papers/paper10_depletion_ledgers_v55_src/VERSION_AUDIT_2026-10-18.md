# Paper10 v55 version and build audit — 2026-10-18

## Authorization and scope

After the verification pass found one concrete punctuation defect in §11 of the published Paper10 v54 main source, the user authorized a narrow v55 successor. This edition corrects only the missing sentence separator after “it” and the doubled final period after “certificate.” in the conclusion. Version/date metadata is updated. A normalized reverse-patch comparison confirms that all other manuscript content is identical to v54.

The v54 main source/PDF and supplementary source/PDF remain unchanged. The v54 SI is carried forward as the unchanged companion; no v55 SI version was assigned. The MCS snapshot data and verifier are copied byte-for-byte from the v54 package.

## Fresh version and lineage scan

Repository `MIKEAA2020/general-sustainability`; pre-numbering e2 branch head `7b4e426f9c139cddb38732d28732598f6429114f`. The scan covered all six branch tips, both tag tips, and both GitHub releases/assets. Branch tips:

- `archive/paper3-v48-workspace` — `0200b6dc75a51feb40728df07e855facbb791383`
- `e2-v3-source-year` — `7b4e426f9c139cddb38732d28732598f6429114f`
- `edwards-framework-e1-audit-implementation` — `2bdf39ff1c13357a44c48b5ed7385c9945aff0b5`
- `edwards-framework-e1` — `66a0a71f976e76df403425e85690d2c9dcb4c141`
- `lean-audit-v4` — `c2fe8fca63384cbf9243434d4213c6e74543a840`
- `main` — `1ba3d3c8a286a055b1342b5102731b601ec3d428`

Tag tips:

- `edwards-framework-e1` — `60d8c6b10f27e8231d9dfb0dd9d5e87345b3305e`
- `compendium-v1.0` — `504f78e176ca25da88ba487571aa4a674299ace3`

The highest Paper10 Part I / `paper10_depletion_ledgers` edition on any checked branch or tag was v54 on `e2-v3-source-year`; no v55 existed locally or remotely before numbering. Paper10b/E4 is the distinct Part II Edwards-aquifer line, not a successor to Paper10 Part I. This disposition follows the current remote split note `PAPER10_SPLIT_AND_PRIOR_ART.md` (blob `16848adcf14e1814140d73981737c6b71e7cf90d`); the older local context copy differs and was not treated as current. The remote `VERSION_CURRENCY.md` blob `e8845b8a98bb94507f12d0d6df9b8607548984ac` matched the local currency file before this update. The two release records have no Paper10/depletion assets.

The current remote v54 main/SI sources, PDFs, build logs, and MCS reproduction files were byte-verified against their local copies before editing. The v54 main/PDF/SI hashes are preserved in the workspace and remain unchanged.

## Source comparison

A reverse patch that restores the v54 header/date and original punctuation yields an exact byte-for-byte match to `paper10_depletion_ledgers_v54.tex`. The manuscript change is limited to the §11 punctuation correction. The title-page date is October 18, 2026. No changes were made to the v54 SI source or PDF.

## Build and visual checks

- Engine: Tectonic 0.15.0, x86_64 GNU release; binary SHA-256 `875fbbc9ab48560d7776088c608e0beee49197b57ab4a2f6c5385b2c661c842f`.
- Bundle: default Tectonic bundle v33 / `tlextras-2022.0r0`.
- Main PDF: 56 pages, 397,295 bytes. The compile log reports 56 pages and 1,908,588 XDV bytes.
- Diagnostics: zero overfull/underfull boxes; zero LaTeX errors; zero undefined references/citations. Tectonic emitted a non-fatal environment note about reverting `/usr/local/share/fonts` mtime; the build completed successfully.
- Visual inspection: page 1 title/date/abstract layout and page 53 conclusion. The corrected sentence is rendered with the intended sentence break and a single terminal period; no clipping or overlap was observed.
- The v55 MCS checker passes. World reserves/production remains `73,000,000 / 250,000 = 292.0 yr`; U.S. `1,000,000 / 20,000 = 50.0 yr`; resource threshold remains `>1,080 yr`; illustrative crossover remains `tau=292`, `g=0.03`, `eta_c=0.998625`.

## Artifact hashes

- v55 main TeX SHA-256: `0a8988310a31028fa71b4ab00ef7599b06946c5e3fc9f67b45150514cf724acf`
- v55 main PDF SHA-256: `f6fd943fd911b0fe2545090cd54813c89b6c74b8d755b3a63f833b1f19a40563`
- v55 build log SHA-256: `ea07a7dc5c41ab732f4771224f9d66216ad49813b29524137605c6da6e20cfb4`
- Carried-forward MCS CSV SHA-256: `57f8281d6261b2b5d84138a716e152e9c56d090a6fc9eba5ce58e2d9373f59a2`
- Carried-forward verifier SHA-256: `ac36305e3f985aab5022e867facdf08660b2064ab0b62303a68b047534097b78`

Publication and remote-byte verification are recorded separately in `PAPER10_V55_PUBLICATION_RECEIPT_2026-10-18.md`.
# Paper08 v50 layout audit — 2026-10-17

## Lineage and version check

A fresh GitHub all-ref scan on 2026-10-17 checked all six branch tips, both tag tips, and both releases. Paper08 v49 remained the highest version found; no v50 path existed. The latest source is `arena agent 1/agent workspace/papers/paper08_governance_delay_v49.tex` on `e2-v3-source-year`, blob `956b050cf0d6919b862a88a03ad0becffd0013c3`. The local v49 base was byte-identical to that blob. The v49 source and historical editions remain unchanged.

The scan's branch tips were: `archive/paper3-v48-workspace` `0200b6dc75a51feb40728df07e855facbb791383`; `e2-v3-source-year` `e8367e820cb75f3f609ac7b43c47b5b7d689ea87`; `edwards-framework-e1-audit-implementation` `2bdf39ff1c13357a44c48b5ed7385c9945aff0b5`; `edwards-framework-e1` `66a0a71f976e76df403425e85690d2c9dcb4c141`; `lean-audit-v4` `c2fe8fca63384cbf9243434d4213c6e74543a840`; and `main` `1ba3d3c8a286a055b1342b5102731b601ec3d428`. The two tag tips were `edwards-framework-e1` `60d8c6b10f27e8231d9dfb0dd9d5e87345b3305e` and `compendium-v1.0` `504f78e176ca25da88ba487571aa4a674299ace3`. The release inventory contained only workspace ZIP assets; ZIP payloads were not unpacked.

## Change scope and content preservation

The v50 source is a layout-only successor. A normalization check that reverted only the edition/date metadata and the explicit layout/provenance edits reproduced the v49 source exactly. No equations, numerical values, model assumptions, or scientific statements outside those edits changed. The certified point values and interval bounds in Section 5.1 were retained verbatim.

The v49 supplementary files `paper08_governance_delay_v49_supplementary_delay.md` and `paper08_governance_delay_v49_supplementary_governance.md` are referenced as unchanged carry-forwards; no v50 SI was created or substituted.

## Build and inspection

- Engine: Tectonic 0.15.0; verified binary SHA-256 `f0b36e78c13dd75b821984830533f872c9a12c62957e51357bc16e65cdb71013`.
- Output: 87-page PDF, 50,342 extracted words, zero blank pages.
- Warnings: zero overfull boxes; nine underfull boxes. No LaTeX errors or unresolved explicit references/citations.
- Tectonic also reports one invalid UTF-8 byte in bundled `lineno.sty` line 296, replacing it with U+FFFD. This package warning is outside the manuscript source; the visual review found no corresponding defect.
- Visually inspected rendered pages 11 (corollary), 18 (crossing pairs and exact interval certificates), 24 (flipped-gain display), 35 (four-state and MPF parameter displays), and 86 (carried-forward SI paths). The former table overlap is resolved; all interval endpoints are legible and no content is clipped.
- PDF SHA-256: `d65ad6306a57226db656321fe47a4fd21e8bd9190e28917791a1017b2a374bd6`.

Full engine output and dependency blob hashes: `paper08_governance_delay_v50_BUILD_LOG_2026-10-17.txt`.

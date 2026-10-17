# Paper08 v51 layout audit — 2026-10-17

## Authorization and version currency

The user explicitly authorized a corrected and published Paper08 v51, with v50 preserved. Before assigning v51, a fresh all-ref scan on 2026-10-17 checked the six branch tips, both tag tips, both GitHub releases/release assets, and exact Paper08 versioned source/PDF paths. Paper08 v50 was the highest existing Paper08 edition; no higher Paper08 version was found. Paper07 v54 is a separate lineage (see the current `VERSION_CURRENCY.md` entry), not a successor to Paper08.

The pre-publication branch tips were:

- `archive/paper3-v48-workspace` — `0200b6dc75a51feb40728df07e855facbb791383`
- `e2-v3-source-year` — `ae4abeb0f0dd2d9e30d1c013d0c2179b7a688a64`
- `edwards-framework-e1-audit-implementation` — `2bdf39ff1c13357a44c48b5ed7385c9945aff0b5`
- `edwards-framework-e1` — `66a0a71f976e76df403425e85690d2c9dcb4c141`
- `lean-audit-v4` — `c2fe8fca63384cbf9243434d4213c6e74543a840`
- `main` — `1ba3d3c8a286a055b1342b5102731b601ec3d428`

Tag tips: `edwards-framework-e1` (`60d8c6b10f27e8231d9dfb0dd9d5e87345b3305e`) and `compendium-v1.0` (`504f78e176ca25da88ba487571aa4a674299ace3`). The two releases were `edwards-framework-e1` (two assets) and `compendium-v1.0` (one asset). The highest Paper08 source before this correction was `arena agent 1/agent workspace/papers/paper08_governance_delay_v50.tex`, Git blob `0f30fc6b9459c5ffdeb68acb23f434215e602a4d`; its PDF was the 87-page v50 artifact. The v51 files are published alongside those artifacts on `e2-v3-source-year`. No tag or GitHub release was created.

## Scope and preservation

This is a narrow front-matter correction. In v50, `\begin{abstract}` preceded `\maketitle`; `\title{...}` only stored metadata and did not render the title. In v51, the date and `\maketitle` precede the abstract. The abstract itself is byte-identical. A normalized source comparison confirms that all manuscript content outside the edition header and title/date/abstract ordering block is byte-identical to v50. No scientific content, equations, numerical values, figures, keywords, or supplementary files were revised. Paper08 v50 and all earlier editions remain unchanged.

## Build and visual QA

- Tectonic 0.15.0: successful build; final PDF has 86 A4 pages.
- Page 1 was visually inspected: title, author/contact information, and date precede the unchanged abstract; keywords and the beginning of the contents follow. No collision, overlap, or clipping.
- Pages 2–3 were checked for clean continuation of the table of contents; the first main-text page is page 4, and the contents page numbers were regenerated. Representative pages 4 and 18 and the final page 86 were also visually inspected.
- Automated checks: 86 pages, no blank/near-blank pages, six embedded figures, and title-before-abstract text order on page 1.
- Layout warnings: zero overfull boxes; nine underfull boxes at inherited passages. Existing hyperref bookmark-level warnings and the bundled `lineno.sty` invalid-UTF-8 warning remain; they are unrelated to the front-matter move.
- Several local successful builds each produced 86 pages but different whole-PDF binary hashes. The cause was not established. The published artifact is the final build run, and its hash is recorded in the build log.

## Artifacts

The source, PDF, build log, changelog, and this audit are published under `arena agent 1/agent workspace/papers/` on `e2-v3-source-year`. The updated `VERSION_CURRENCY.md` records the v51 status. The build log records byte counts and SHA-256 values and includes the final Tectonic console and engine logs.

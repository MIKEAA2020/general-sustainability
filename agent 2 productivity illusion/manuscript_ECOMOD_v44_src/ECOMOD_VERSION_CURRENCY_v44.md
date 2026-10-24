# ECOMOD edition currency: v44

**Currency scan date:** 2026-10-24<br>
**Repository:** `MIKEAA2020/general-sustainability`<br>
**Target branch:** `main`<br>
**Target package path:** `agent 2 productivity illusion/manuscript_ECOMOD_v44_src/`

## Full-history check

Before assigning the next edition number, the reachable history was checked after fetching all repository branches and tags and completing the unshallow fetch. The scan covered **1,636 reachable commits** and **97 unique ECOMOD-named historical paths**. The latest numbered ECOMOD edition found was **v43**, at `agent 2 productivity illusion/manuscript_ECOMOD_v43_src/`; no ECOMOD v44 path was present. The only ECOMOD-specific currency note found in that history was the v43 note. No separately named ECOMOD split/merge note was found.

Accordingly, **v44** is the available successor number. It is published as a new sibling package on `main`; v43 remains preserved and unchanged. This currency note supplements, rather than replaces, [`ECOMOD_VERSION_CURRENCY.md`](ECOMOD_VERSION_CURRENCY.md), which records the earlier v42-to-v43 decision.

## Scope of this edition

V44 corrects the solver's zero-valued time-zero delayed-capacity sample and inconsistent propagation of the optional technology wave through current and delayed `B`. It also forces floating-point state arrays, including for integer `D0`. Both current-quality and delayed-quality solver variants are retained. Baseline results were rechecked; the controlled active-wave/no-wave experiment is reported separately and is not treated as a universal or empirical claim.

The manuscript and SI are Americanized, the requested acknowledgments are added, and the AI declaration no longer claims language editing. The discussion now separates modeled capital-area decline from what NFA accounts can establish and provides a component-level physical-stock scoreboard for heterogeneous assets.

## Publication verification

The v44 package was published to `main` at commit `36ef7a6bde047e3f555dae9ba8d2cf2aa4f10a2b`, under `agent 2 productivity illusion/manuscript_ECOMOD_v44_src/`. The release tree contains 50 files, including `SHA256SUMS.txt`; all 49 listed file digests matched the corresponding remote Git blobs. The main PDF is 36 pages and the SI is 22 pages. The v43 package remains available at its original path and was not overwritten.

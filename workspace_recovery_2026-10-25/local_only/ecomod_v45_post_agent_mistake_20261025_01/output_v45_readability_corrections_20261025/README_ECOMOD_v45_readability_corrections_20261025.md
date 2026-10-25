# ECOMOD v45 readability corrections — 2026-10-25

## Status and provenance

This is a targeted readability correction to the archived **ECOMOD v45 working candidate**. It is not a new numbered edition, an official release, or a change to published v44. The base working snapshot is preserved on `workspace-recovery-2026-10-24` at commit `a40ec7db0f22cf80cde76f55ac4f912beea43efc`, under `workspace_recovery_2026-10-25/local_only/ecomod_v45/`. This dated update is kept separately so the earlier candidate remains recoverable unchanged.

The edition/date-labelled main and SI PDFs and assembled TeX files in this folder are the deliverables. `source_parts/` contains the editable source parts used to assemble them; the unchanged figures and other assets are in the base v45 snapshot. The generic `manuscript_working_*` files are build intermediates, not edition labels.

## Editorial changes

- Restored **composition diagnostic** as the name for `\Delta b_{\mathrm{conv}}` and named its sign regimes **composition-premium**, **composition-neutrality**, and **composition-discount**. The names classify the marginal conversion contribution, not the net change in total biocapacity.
- Defined **composition mask** (rising aggregate `B` with falling `A_c`) and **liquidation mask** (steady demand `E` with falling `A_c`) as distinct, potentially overlapping signatures. Their definitions are not interchangeable.
- Restored the full orchard/two-book explanation, including annual harvest versus productive stock, conversion, replanting, delays, and the limits of what the analogy establishes. Retained the elevator analogy and its no-fold caveat.
- Kept ordinary scholarly terms such as **aggregate**, **heuristic**, and **diagnostic** where they are precise. The heuristic governor example concerns only the information limit of monitoring `B`; it is not a general policy recommendation.

The changes are editorial and terminological. No numerical results, equations, propositions, data vintage, empirical claims, or disclosure statements were changed.

## Source review and build

The current editable source was checked against the listed proofing items. The alleged Table 1 strings are already correct in this source (`b_{G,c}`, “institutional lags,” and the typed-floor symbols); “A_c settles” is used; the Table 2 caption has `\Upsilon_c` and `gha ha^{-1}`; and `E_{\mathrm{ceil}}` is consistently defined. The gate/share-rule discussion is under §4.3; **“Relation to prior work” appears once** as §4.4. The third-contribution sentence is complete and appears in full on page 4. No source correction was needed for those items.

Both documents compiled with Tectonic 0.17.0: **34-page main manuscript** and **20-page SI**. There were no compile errors or unresolved references. Non-fatal box warnings remain, including the previously observed 2.608 pt overfull box in the main document and underfull-box warnings. The orchard paragraph is complete on page 3; the contribution paragraph is complete on page 4.

`SHA256SUMS_ECOMOD_v45_readability_corrections_20261025.txt` lists the hashes of the files in this update package (excluding the checksum file itself). The existing `SHA256SUMS_v45_working.txt` in the base candidate remains a stale working list and is not a release manifest.

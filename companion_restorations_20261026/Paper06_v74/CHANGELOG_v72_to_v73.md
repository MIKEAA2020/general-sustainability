# Changelog: Paper06 v72 → v73

## Scope

- Preserved Paper06 v72 unchanged.
- Created v73 as a visual-only derivative. In Figure 2 (`fig_witness_triangle.png`), moved the `s₁+s₂=2` label in each panel to a horizontal position just above its diagonal.
- Updated edition/file labels to v73 in the assembled TeX and the corresponding source notes. No substantive article or SI prose, mathematical claim, theorem statement, parameter, numerical result, or citation target was changed.
- Added the exact v72 Figure 2 baseline and a small reproducibility script to the v73 editable-source bundle. The v72 figure and all other figure assets remain unchanged.
- Added `EDITORIAL_ASSESSMENT_AND_REVISION_PLAN.md` as a separate advisory document. It assesses the supplied Argon/Grok summaries and Gemini/Grok rewrites against v72, includes a claim audit, and proposes §§1.1–1.2 copy. That prose has **not** been inserted into v73.

## Figure verification

- Original and corrected dimensions: 2165×1262 pixels, 200 dpi.
- Original baseline SHA-256: `989d9d4142985df03584248ebf1fff20ce0bb392ab9ad02439920219814eb212`.
- Corrected v73 Figure 2 SHA-256: `909151b5c8167e1a78739853523a878bcbc89407f26d413ae2cee7c66e720750`.
- Pixel comparison: 5,128 changed pixels, bounded by `(x=420…1695, y=185…318)` in the combined image. The changes are limited to the two equality-label neighborhoods; no red-arrow or witness-marker pixels were intentionally patched. The corrected labels are unrotated and legible above the corresponding diagonals.
- The v73 PDF was rendered and visually checked on page 17. The figure’s caption, axis labels, arrows, hatching, reserve bars, witness point, and lower licensing strip remain present.

## Build and source checks

- Main and SI rebuilt with Tectonic 0.17.0.
- Main PDF: 48 pages; SI PDF: 40 pages, matching v72.
- Extracted page text is identical to v72 after normalizing edition labels. Main and SI hyperlink annotation counts and URL targets match v72 (12 main; 9 SI).
- Overfull/underfull box warnings match the same-engine v72 baseline in count and warning content; only source-line positions differ because of the edition header. No `??` markers or unresolved citation/reference markers were found.
- Source diff is limited to edition labels/comments, the corrected Figure 2 PNG, its baseline copy and edit script, and this changelog/README/editorial document. No section, theorem, equation, table, or other figure was removed or revised.

## Citation and release discipline

- v72 remains unchanged. This v73 derivative is not deposited under a DOI.
- Do not infer that the generated summaries are accepted source text; the editorial document is a proposal pending any requested prose revision.
- No existing DOI package, checksum registry, ECOMOD edition, `main` branch, or prior companion version was refreshed or overwritten.

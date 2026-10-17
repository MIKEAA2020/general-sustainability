# Paper09b v6 changelog — 2026-10-17

**Base:** Paper09b v5, the latest version found on the audited refs. V5 and all earlier versions remain unchanged. This is a layout-only successor.

## Layout corrections

- Reflowed the lemma's two alternative accounting placements into a vertically aligned display so neither equation collides with the column boundary.
- Converted the compact summary Table 3 into a full-width `table*` using `tabularx`, wider fixed columns, and increased row spacing. All recorded values, sources, units, and threshold entries are unchanged.
- Updated edition/date metadata only.

The conditional result remains limited to unknown nonnegative `\(\kappa\)` and the strict row-specific certificate `\(\kappa<\kappa^*\)`. SSB remains distinguished from reported landings/catch, tonnes remain converted to kilotonnes, and both `\(C_t\)` and `\(C_{t+1}\)` alignments remain shown.

## Build

Tectonic 0.15.0 produced the v6 PDF (9 pages). The v5 lemma and summary-table overflow defects are cleared. Full build details, hashes, normalization check, and visual-inspection record are in `paper09b_arv_certification_v6_BUILD_LOG_2026-10-17.txt` and `PAPER09B_V6_LAYOUT_AUDIT_2026-10-17.md`.

# Paper10 v55 MCS 2026 reproduction package

This package carries forward the unchanged USGS MCS 2026 phosphate snapshot and arithmetic verifier used with Paper10 v54. Paper10 v55 changes only conclusion punctuation and edition/date metadata; no data, formula, or reported numerical result changed.

- `mcs2026_phosphate_snapshot.csv` transcribes selected rows from USGS, *Mineral Commodity Summaries 2026—Phosphate Rock*. Units are thousand metric tons of marketable phosphate rock. Production is the estimated 2025 column; reserve/resource amounts are the 2026-vintage quantities. The two Australia rows preserve the source's distinct table-reserve and JORC/equivalent-footnote bases.
- `verify_mcs2026_snapshot.py` uses only the Python standard library. Run `python3 verify_mcs2026_snapshot.py` to recompute the vintage-specific R/P quotients, the 90%-of-resources arithmetic lower bound, and the explicitly illustrative reserve-crossover values. It does not fit a forecast or estimate production-growth/reclassification parameters.
- `VERSION_AUDIT_2026-10-18.md` records the all-ref version scan and the v55 build checks.

The v54 supplementary source/PDF are carried forward unchanged as the current companion. See `PAPER10_V55_CHANGELOG_2026-10-18.md` in the parent papers directory for the exact source delta.

Source: https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-phosphate.pdf
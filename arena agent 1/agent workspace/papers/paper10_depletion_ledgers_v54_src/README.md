# Paper10 v54 phosphate snapshot check

`mcs2026_phosphate_snapshot.csv` is a small transcription of selected rows from USGS, *Mineral Commodity Summaries 2026—Phosphate Rock*. The PDF states that its units are thousand metric tons of marketable phosphate rock. Production is the estimated 2025 column; reserves and resources are the quantities reported in the 2026 vintage. The Australia rows preserve the source's distinct table-reserve and JORC/equivalent-footnote bases rather than reconciling them.

Run `python3 verify_mcs2026_snapshot.py` to recompute the R/P quotients, the 90%-of-resources arithmetic lower bound, and the explicitly illustrative reserve-crossover values. The script does not fit a forecast or estimate the production-growth/reclassification parameters.

Source: https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-phosphate.pdf

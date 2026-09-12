# NOTE on reconstructed verification inputs (2026-09-11, verification agent)

Two files in this directory are BEHAVIORALLY-EXACT RECONSTRUCTIONS created by the
verification agent on 2026-09-11 to re-execute the author's battery scripts, which
hardcode these input paths. They are NOT the author's original uploads (the originals
were never deposited in the repo or workspace):

1. `shortened.txt` — rebuilt from the repo-deposited `peru_sau_annual.csv`
   (analysis/anchoveta_enso/): one TSV row per year
   `604<TAB>1<TAB>87<TAB>Q_tlw<TAB>{year}<TAB>{tonnes}<TAB>Reported`
   for 1950-2024 (75 rows). The author's `load_peru()` sums column 6 by year with no
   entity/taxon filter, so this file feeds the script byte-identical annual values.

2. `SAU Taxa 600004 v50-1.csv` — an exact copy of the repo-deposited
   `chile_sau_annual.csv` (year,tonnes; 1950-2019). The author's `load_chile()` reads
   only the year/tonnes columns via DictReader and sums by year, so this file feeds
   the script identical annual values (any sector/reporting-status row detail in the
   original is summed over by the script itself).

Fidelity proof: the author's unmodified `battery.py` / `battery_v2.py`, run against
these files plus freshly-fetched NOAA PSL index files, reproduce the committed
`battery_results.json` / `battery_v2_results.json` bit-exactly on all deterministic
outputs (spec 5/5, xcorr 180/180 cells, splits 4/4, v2 Granger 12/12, v1 Granger
error-strings 2/2). See /home/user/verify_battery/BATTERY_VERIFICATION_v1.md.

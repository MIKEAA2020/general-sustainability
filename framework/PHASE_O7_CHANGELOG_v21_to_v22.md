# O7 changelog — companion cross-check → v22_restructured (2026-09-13)

Merged-plan item O7 executed against the newest companion copies (E1 v49, E3
v16) and the cited archives. Full report: `COMPANION_CROSSCHECK_20260913.md`.

## Findings

- **Verified consistent** (report §1–§4): titles, Zenodo records (2026a
  22552680 / 2026b 22553609, mutually consistent across companions), "Table 8
  of companion" (E1 capelin), all cod numbers in F1 Tables 2/3 (CSV precision
  vs E1's rounding; 3.22 kt vs the apparent 3.6 kt rounding artefact noted),
  LRP 884.6/276, Regular et al. 2025, the 5-of-32 DM universe computed exactly
  from the cited batch-7 replication (5th row = B h5 M2-vs-M1b, one of the four
  alternative-comparator rows the companion's 28-row subset excludes), all
  Edwards numbers (E3 Table 4/5/7; F1's six margins vs the correct
  next-simpler comparators), band arithmetic.
- **NEW-4a (adjudicated, fixed in v22):** E3 retains M1 at h=1 by its
  pre-registered point rule (no band, h=1-only); F1's unified rule withholds it
  and the reconciliation was missing. v22 §4 now states: the companion's h=1
  point rule retains M1 provisionally (0.39 ft margin within noise, MAE tie,
  five-year loss); the unified rule withholds it (2.96% h=1 margin inside the
  band, h=5 loss); the empty retained set is a property of the unified rule and
  the M1 difference is a recorded rule-version difference, not a data
  difference. "No outcome changes" sharpened accordingly.
- **NEW-4b (adjudicated, archive fixed):** the O9 co-primary IC JSON had
  derived Edwards M3/M4 RMSEs (12.483/12.624) from misapplied margins; corrected
  to companion Table 4 (14.46/14.30) → IC(M3)=486.8, IC(M4)=484.8. IC-best on
  Edwards remains M2m; the paper's §6.5 block is unaffected (it cites only
  M2m/M1/persistence). Runner note corrected; Part-1 validation still PASS.
- **Noted (no F1 edit):** E1 v49's own DM table prints z=1.21, [4.4,134.4] for
  the A h1 M4vM3 row (its coarse-regime pass, M4 195.6) while F1's numbers
  match the cited annual-landings replication (206.3, z=0.99) — companion-side
  difference flagged for the E1 finalization pass.

## Verification

Line audit v21→v22: only the two replaced sentences differ (their source line
also contained them; all other content byte-identical). Formalization 0,
redundancy 0, style PASS, coverage (main+supplement vs v0/v13) clean.
Re-run trigger: when E1/E3 are finalized.

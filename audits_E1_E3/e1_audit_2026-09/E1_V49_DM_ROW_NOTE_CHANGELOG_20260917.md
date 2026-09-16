# E1 v49 — DM row-note finalization (2026-09-17)

## Item closed
COMPANION_CROSSCHECK_20260913.md §3 flag: E1's own DM table prints z=1.21,
[+4.4, +134.4] for the Spec-A h=1 M4-vs-M3 row (this paper's archived
coarse-regime pass), while the independent batch-7 replication archive
(e1_dm_uncertainty.csv) reads z=0.99, [+4.7, +144.7] (annual-landings pass).

## Change applied (text edit only — no computed values altered)
Inserted an explanatory row note immediately after the DM longtable in
`e1/paperE1_cod_forecast_ladder_v49.tex` stating:
- which pass the printed values come from;
- the replication values and archive location;
- that both readings classify the row identically (bootstrap CI excludes
  zero, |z|<1.96);
- that no retention verdict in E1 or F1 depends on the difference, and
  that F1 quotes the replication values (consistent with the cross-check
  adjudication: F1's cited source matches F1; no F1 edit).

## Protocol notes
- The archived RMSE numbers (195.6 vs 206.3 coarse vs annual-landings) were
  deliberately left untouched: overwriting the paper's own archived pass
  would misstate the analysis history.
- `e1/paperE1_cod_forecast_ladder_v49.pdf` is now one revision behind the
  .tex and must be rebuilt at the next submission packaging (sandbox has no
  LaTeX toolchain; not rebuilt here). Version bump to v50 deferred to that
  packaging pass; Zenodo DOI unchanged until then.

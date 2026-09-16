# E1 v50 — DM row-note finalization, new-version mode (2026-09-17)

## What this supersedes
`E1_V49_DM_ROW_NOTE_CHANGELOG_20260917.md` recorded an **in-place edit of the
frozen v49 .tex**, performed and pushed before the owner's standing directive
(2026-09-17): *revisions are always created as new versions; repo contents are
never overwritten.* That edit has been REVERSED: `paperE1_cod_forecast_ladder_v49.tex`
is restored to its pristine frozen bytes, and the same correction is re-issued
in the new file `paperE1_cod_forecast_ladder_v50.tex`. Content of the correction
is unchanged from the V49-mode changelog.

## Item closed (unchanged substance)
COMPANION_CROSSCHECK_20260913.md §3 flag: E1's DM table printed z=1.21,
[+4.4, +134.4] (archived coarse-regime pass) for the Spec-A h=1 M4-vs-M3 row
while the independent batch-7 annual-landings replication archive
(`e1_dm_uncertainty.csv`) reads z=0.99, [+4.7, +144.7].

## Change in v50 (text edit only — no computed values altered)
Explanatory row note inserted immediately after the DM longtable stating:
which pass the printed values come from; the replication values + archive
location; both readings classify the row identically (bootstrap CI excludes
zero, |z|<1.96); no retention verdict in E1 or F1 depends on the difference;
F1 quotes the replication values (per cross-check adjudication).

## Status
- v49.tex: pristine frozen artifact (untouched source of the submitted v49 PDFs).
- v49.pdf / v50.pdf: no LaTeX toolchain in sandbox — PDFs NOT rebuilt here;
  rebuild v50 PDF at submission packaging; Zenodo DOI points at v49 until then.
- Numbering: v50 supersedes v49 for future companion cross-checks and for the
  F1 claims ledger (claim CL-COD-DM-AH1-M4vM3 records both readings).

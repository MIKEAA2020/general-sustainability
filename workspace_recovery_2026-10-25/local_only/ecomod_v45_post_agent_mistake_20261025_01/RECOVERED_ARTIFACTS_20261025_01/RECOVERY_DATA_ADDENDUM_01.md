# Data and scripts recovery addendum — 2026-10-25

The recovery directory now also preserves the current project CSV data, the current NFA JSON summary, and project Python source scripts in `CURRENT_DATA_AND_SCRIPTS/`. The previous recovery commit's CSV, Python, and JSON files under the ECOMOD v45 tree are also copied under `FROM_RECOVERY_COMMIT_7ae113d5/` at their relative paths. This includes both drawdown CSVs used for the Table S4 check. These are separately named source snapshots; no script was run to regenerate or replace them.

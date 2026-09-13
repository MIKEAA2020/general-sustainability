# Phase C provenance — repo cross-reference (2026-09-13)

The Phase C campaigns (see `PHASE_C_RESULTS.md`) imported the frozen estimator/map/scorer and the Section 4.3 generators from the workspace copies extracted from the newest release asset. This file proves those copies are byte-identical to the files on the repository (branch `main`, blob-shas via the GitHub API; the release branch `edwards-framework-e1` carries the same blobs, and the implementation branch `edwards-framework-e1-audit-implementation` is main + added files with nothing modified).

| file (repo path) | git blob sha on main | local sha256 | match |
|---|---|---|---|
| `wave_e_cod/src/run_ladder.py` | `3f59f8f3e65ef8c55b19c4806dcfa6a0970ed5c1` | `8565f7d1c0c3b415e5efcc63e700c7fb94aa4b7463b45b9432748cfbc9cd5f30` | True (git hash-object == blob sha) |
| `wave_e_edwards/src/run_ladder.py` | `6b45a5bd16288018607b7b60473a703fca41c995` | `5df553c9ffd864b6cfb61ef906949166720327733815876924c8becaa0a7d9ac` | True (git hash-object == blob sha) |
| `wave_e_edwards/src/e3_audit_uncertainty.py` | `15f26274d26f98a24b44220165c10640a2d4663f` | `716ec992949b148d3631ee836d4f7f7dfdc3575c763bac9c192bf903adb2eee0` | True (git hash-object == blob sha) |
| `tools/sim_retention_power.py` | `6901bf7405100b72010497b6c61b225b7841cca7` | `e2cc05a627a55db5a584c1be200164b71e38c89ae01f9512c5786e6803020579` | True (git hash-object == blob sha) |
| `tools/sim_misspecified.py` | `573ceed69e9cac6766aff66caf1ab2ef8c90ba0b` | `538d95003390de2e5b9658e687eb9ad4f297a092e34353b84f73bfd35e35356c` | True (git hash-object == blob sha) |

All 29 `*.py` files under `wave_e_cod/src/`, `wave_e_edwards/src/` and `tools/sim_*.py` exist on main and on the release branch with identical blob shas; none are missing and none differ from the workspace copies (checked 2026-09-13).

Consequence: every Phase C CSV's `_provenance.json` sha256 field can be resolved to a permanent git object via this table — the runs are reproducible against the repo, not only against the workspace.

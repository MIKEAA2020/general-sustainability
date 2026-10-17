# Workspace clone cleanup receipt — 2026-10-17

The pre-delete audit and per-file manifest were published and byte-verified before cleanup:

- `arena agent 1/agent workspace/papers/WORKSPACE_CLONE_AUDIT_2026-10-17.md`
- `arena agent 1/agent workspace/papers/WORKSPACE_CLONE_AUDIT_2026-10-17.csv`
- Audit commit: `126e94055a27c69545db7462affe6226fcdd6aa8`

Immediately before deletion, every planned local file was rehashed and checked against the exact remote Git blob at the recorded branch/tag path. All 198 candidates matched; there were zero missing paths, hash mismatches, or other exceptions. The verification used all six current branches and two tags, with complete recursive trees.

**Deleted:** the 198 byte-identical, re-clonable files under local `/home/user/p11_v67/` and `/home/user/p11_v68/`, totaling **21,529,298 bytes (20.53 MiB)**.  
**Retained:** all 12 local-only files in those folders (94,889 bytes per folder; 189,778 bytes total), including build logs, push plans, and the local E1-v60/v66 diff.  
**Scope:** no files outside those two folders were removed; `portfolio_work/`, active source/material, user uploads, local-only outputs, and all repository versions were left untouched.

After cleanup, `/home/user` measured about 79 MiB by `du`; `p11_v67/` and `p11_v68/` each retain only their six local-only files. The detailed file-by-file pre-delete evidence remains in the CSV audit above.

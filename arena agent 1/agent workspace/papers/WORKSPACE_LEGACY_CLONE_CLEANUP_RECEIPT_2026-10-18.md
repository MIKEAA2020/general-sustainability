# Workspace legacy clone cleanup receipt — 2026-10-18

The pre-deletion audit and per-file manifest were published and byte-verified before cleanup:

- `arena agent 1/agent workspace/papers/WORKSPACE_LEGACY_CLONE_AUDIT_2026-10-18.md`
- `arena agent 1/agent workspace/papers/WORKSPACE_LEGACY_CLONE_AUDIT_2026-10-18.csv`
- Pre-deletion audit commit: `aa67c3d83f855c39fad8a93d383b77ea896cb526` (parent `600354c149aad300780d647cdb0768451ec726dc`).

Immediately before deletion, all six branches and both tags were rescanned with complete recursive trees. Each planned local file was rehashed, compared with its manifest SHA-256 and Git blob SHA-1, and checked against the recorded reachable ref/path. The remote blob bytes were fetched and compared again. All 528 candidates matched; there were zero missing paths, byte mismatches, changed local files, or exceptions.

| Local root | Removed exact remote copies | Bytes removed |
|---|---:|---:|
| `/home/user/p07_v53/` | 223 | 8,554,704 |
| `/home/user/paper1_v64/` | 30 | 3,066,566 |
| `/home/user/p09_layout_test/` | 138 | 3,139,034 |
| `/home/user/p09_source_test/` | 137 | 2,787,701 |
| **Total** | **528** | **17,548,005 (16.74 MiB)** |

**Retained:** all 70 local-only or locally modified files in those roots (8,904,989 bytes / 8.49 MiB), rechecked unchanged after deletion. No directory was removed; empty folders remain. No files outside those four named roots were deleted. In particular, `portfolio_work/`, uploads, root-level deliverables, active/current project folders, Paper08 v51, Paper11b/E3, and all remote editions were left untouched.

The local workspace now reports about 69 MiB via `du -sh /home/user` (about 87 MiB before this cleanup). This cleanup removed only exact, re-clonable local copies; the published repository content was not deleted or changed by the cleanup.

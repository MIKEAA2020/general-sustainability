# Workspace recovery archive — 2026-10-24

This is a preservation archive for workspace files whose Git blob was absent from every current branch/tag tree and all reachable remote history at the pre-recovery scan. It is **not** an official paper edition, release, or endorsement of any draft. The archive is kept on a separate branch so unpublished candidates and QA by-products do not enter `main`.

- Base: `main` at `461d59d3ab8e00a6409fd019f94361983618b488`.
- Branch: `workspace-recovery-2026-10-24`.
- Archived files: **276**; total **26,535,512 bytes** (25.31 MiB).
- Exact workspace-relative paths are preserved below `local_only/`; `LOCAL_ONLY_SHA256SUMS.csv` records each original path, archive path, byte count, SHA-256, and Git blob ID.
- Bytes were copied from their local originals without changing the source files; duplicate blobs are deduplicated by Git.

## Scope and exclusions

The scan covers project/version/test folders, local deliverables, audit materials, and `portfolio_work/`. Files already byte-identical to a current remote branch/tag or reachable remote history were not duplicated here. The per-file pre-deletion reconciliation audit will be published in this directory as `WORKSPACE_RECONCILIATION_AUDIT_2026-10-24.md` and `.csv`.

The following are intentionally not archived: `/home/user/secrets/` (credential material), `/home/user/uploads/` (user-provided inputs), repository clone metadata, and environment/package caches. No PAT was found in the selected archive sources.

## Not promoted

- `portfolio_work/unpublished_local_layout_variants_2026-10-17/` remains explicitly an unpublished candidate/layout area; its files are preserved here, not promoted to the corresponding version paths.
- `p11c_v6/` is an incomplete local derivative, not an official v6 release: its README/highlights/changelog and push plans still identify v5, and its TeX contains stale v5 source/verifier references. Its unique files are archived for recovery; no v6 edition is created or overwritten.
- Build logs, local PDF page renders, and test outputs are archived as local workspace artifacts, not as canonical publication files.

No existing branch or published edition is changed by this archive commit.

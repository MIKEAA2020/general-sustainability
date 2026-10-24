# Workspace reconciliation audit — 2026-10-24

**Status at publication:** pre-deletion audit. No cleanup/deletion had occurred when this audit was prepared. The per-file CSV beside this report is the controlling manifest; it contains 8,317 records (1,408 workspace files, 356 repository-clone worktree files, 6,551 old `gs2` tree paths absent from the worktree, and two clone summaries).

## Result

- **Local-only material recovered:** 276 files / 26,535,512 bytes (25.31 MiB) were archived byte-for-byte on the separate `workspace-recovery-2026-10-24` branch under `workspace_recovery_2026-10-24/local_only/`. The manifest `workspace_recovery_2026-10-24/LOCAL_ONLY_SHA256SUMS.csv` records original path, archive path, byte count, SHA-256, and Git blob SHA-1 for every archived item. The archive commit is `ac7565c2a1c5ad5ff7c3f32ea2bae799a617a6d0`, based on `main` at `461d59d3ab8e00a6409fd019f94361983618b488`.
- **Remote-copy cleanup candidates:** 996 local files / 41,888,893 bytes (39.95 MiB) in the older edition/test roots below were matched to current remote blobs and compared byte-for-byte before listing as candidates. 900 unique remote blobs totaling 40,097,097 bytes were read from Git and compared to every corresponding local file; **zero mismatches**. Cleanup is not performed by this report itself.
- **`gs2` recovery:** old `HEAD` `217d110f006ec4b6b43755e53350d7043b0d1ddc` is an ancestor of current `main`. All **6,551** paths in its HEAD tree have exact blob matches in current remote trees; its working tree currently contains **0** regular files (all 6,551 show as deleted), so no unpublished content was found there and there was nothing to restore locally. The old clone can be removed after this audit; the files remain recoverable from GitHub.
- **`ecomod_publish` clone:** clean sparse checkout, `HEAD` and `origin/main` both `461d59d3ab8e00a6409fd019f94361983618b488`; **356** working-tree files / 48,373,146 bytes match the main-tree blob IDs. The clone itself occupies about **322 MiB** after fetching blobs for the byte checks; it is re-clonable and may be removed after the audit.
- **No published edition was changed or overwritten.** ECOMOD v43 remains on `main`; the audit/recovery material is isolated on the new recovery branch.

## Remote refs scanned

All branch tips and tags were fetched and recursively scanned. `origin/HEAD` was treated as an alias, not an additional ref.

| Ref | Commit (peeled for tags) |
|---|---|
| `branch:archive/paper3-v48-workspace` | `0200b6dc75a51feb40728df07e855facbb791383` |
| `branch:e2-v3-source-year` | `c867b66fc74c3e1c5f812ca42650879914b59650` |
| `branch:edwards-framework-e1` | `66a0a71f976e76df403425e85690d2c9dcb4c141` |
| `branch:edwards-framework-e1-audit-implementation` | `2bdf39ff1c13357a44c48b5ed7385c9945aff0b5` |
| `branch:lean-audit-v4` | `c2fe8fca63384cbf9243434d4213c6e74543a840` |
| `branch:main` | `461d59d3ab8e00a6409fd019f94361983618b488` |
| `branch:workspace-recovery-2026-10-24` | `ac7565c2a1c5ad5ff7c3f32ea2bae799a617a6d0` |
| `tag:compendium-v1.0` | `504f78e176ca25da88ba487571aa4a674299ace3` |
| `tag:edwards-framework-e1` | `60d8c6b10f27e8231d9dfb0dd9d5e87345b3305e` |

## Per-file cleanup scope

The following roots are the only workspace project/test directories approved in this audit for per-file cleanup. Each row in the CSV marked `DELETE_CANDIDATE_BYTE_VERIFIED` has the local SHA-256, Git blob ID, matching remote ref/path, and an exact byte-comparison result.

| Local root | Files | Bytes | MiB |
|---|---:|---:|---:|
| `census/` | 23 | 1,360,917 | 1.30 |
| `e1_v69/` | 92 | 3,405,504 | 3.25 |
| `p01_v73/` | 47 | 2,729,822 | 2.60 |
| `p02_v16/` | 67 | 1,351,541 | 1.29 |
| `p03_v23/` | 69 | 1,599,406 | 1.53 |
| `p04_v20/` | 68 | 1,106,229 | 1.05 |
| `p05_v20/` | 118 | 4,919,846 | 4.69 |
| `p06_v71/` | 50 | 4,426,206 | 4.22 |
| `p07_v53/` | 50 | 8,037,709 | 7.67 |
| `p09_layout_test/` | 8 | 164,361 | 0.16 |
| `p09_source_test/` | 12 | 702,919 | 0.67 |
| `p09_v44/` | 262 | 7,304,014 | 6.97 |
| `p11_v67/` | 6 | 94,889 | 0.09 |
| `p11_v68/` | 6 | 94,889 | 0.09 |
| `p11c_v5/` | 85 | 2,066,525 | 1.97 |
| `ecomod_v42/` | 33 | 2,524,116 | 2.41 |
| **Total** | **996** | **41,888,893** | **39.95** |

Files are to be unlinked individually only after rechecking their local SHA-256/Git blob ID against this CSV. No directory-wide deletion of these roots is authorized by this report.

## Retained and excluded material

- Kept locally by instruction: `/home/user/portfolio_work/`, `/home/user/uploads/`, all root deliverables, completed audits, and all files under the active ECOMOD v43 deliverable folder.
- Kept locally as active/incomplete: `p11c_v6/`. Its unique files are preserved in the archive, but the folder is **not** treated as a published v6 edition: its README/highlights/changelog and push plans are stale, and the manuscript retains v5 source/verifier references. No v6 path was added as an official edition.
- The ECOMOD v43 page-render/QA images, p07/p09 local previews, compile/build logs, the `p05_v20/work/census_m6.npz` output, and other local-only files are preserved in the recovery archive with their original workspace paths. Explicitly unpublished layout candidates remain labelled as unpromoted; no official version path was overwritten.
- Three user-provided upload files (183,891 bytes) are intentionally omitted from the published inventory/archive and remain in `/home/user/uploads/`. Secrets, including the GitHub PAT file, are never inventoried or committed. Environment caches/configuration are also excluded. The archive sources were scanned against the live PAT; no match was found.
- This CSV intentionally does not enumerate itself, the Markdown report, the archive README/manifest, user uploads, secrets, or environment/cache/config files. It includes all 1,408 scanned workspace file records—including protected root/portfolio items—all 6,551 absent `gs2` HEAD paths, all 356 tracked `ecomod_publish` checkout files, and two clone-summary records.

## How the audit was performed

For each local regular file, the audit records SHA-256 and the Git blob SHA-1. Current trees for every remote branch and tag were indexed; reachable remote history was also considered without forcing a full historical blob download. For the **996 deletion candidates**, Git fetched/read the referenced remote blobs and each local byte stream was compared exactly (not just by filename). For the archived files, archive tree blob IDs, local SHA-256 values, and the manifest were verified after the push. The clone summaries record branch/commit identity and clean status.


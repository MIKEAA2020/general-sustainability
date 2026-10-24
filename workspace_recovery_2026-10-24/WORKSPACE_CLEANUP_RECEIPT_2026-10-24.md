# Workspace cleanup receipt — 2026-10-24

**Pre-deletion audit:** `WORKSPACE_RECONCILIATION_AUDIT_2026-10-24.md` and `.csv`, published to `workspace-recovery-2026-10-24` at commit `aa165739e9dec36608f7b51f9fb665297eb35d55` **before any deletion**. The audit’s per-file CSV is the deletion manifest.

## Completed cleanup

Immediately before unlinking, I rechecked every candidate’s path allowlist, local byte count, SHA-256, Git blob ID, current remote-tree entry, and exact local-vs-remote Git blob bytes. All **996 files / 41,888,893 bytes** matched; the 900 unique remote blobs were read and compared against every local occurrence. There were **zero changes, missing blobs, or mismatches**.

| Local root | Files removed | Bytes |
|---|---:|---:|
| `census/` | 23 | 1,360,917 |
| `e1_v69/` | 92 | 3,405,504 |
| `p01_v73/` | 47 | 2,729,822 |
| `p02_v16/` | 67 | 1,351,541 |
| `p03_v23/` | 69 | 1,599,406 |
| `p04_v20/` | 68 | 1,106,229 |
| `p05_v20/` | 118 | 4,919,846 |
| `p06_v71/` | 50 | 4,426,206 |
| `p07_v53/` | 50 | 8,037,709 |
| `p09_layout_test/` | 8 | 164,361 |
| `p09_source_test/` | 12 | 702,919 |
| `p09_v44/` | 262 | 7,304,014 |
| `p11_v67/` | 6 | 94,889 |
| `p11_v68/` | 6 | 94,889 |
| `p11c_v5/` | 85 | 2,066,525 |
| `ecomod_v42/` | 33 | 2,524,116 |
| **Per-file total** | **996** | **41,888,893** |

The 276 formerly local-only artifacts (25.31 MiB) had first been published byte-for-byte to `workspace_recovery_2026-10-24/local_only/`; their source paths and checksums are in `LOCAL_ONLY_SHA256SUMS.csv`. This preserves, among other items, local test/build outputs, the extra Paper05 census file, the ECOMOD QA renders, and intentionally unpublished candidates without promoting them to official version paths.

## Re-clonable repository clones removed

- `/home/user/ecomod_publish/` — clean sparse clone; `HEAD == origin/main == 461d59d3ab8e00a6409fd019f94361983618b488`; all 356 checked-out files matched the main tree. Removed **336,878,364 bytes**.
- `/home/user/gs2/` — old `HEAD` `217d110f006ec4b6b43755e53350d7043b0d1ddc` is an ancestor of current `main`; all 6,551 tracked paths matched current remote blobs, while the working tree had no files. Removed **2,795,790 bytes**. No local-only content was found, so no bulk restore was needed.

**Total removed:** 381,563,047 bytes (about 363.86 MiB). Workspace usage is now **90 MiB** by `du -sh /home/user`.

## Explicitly retained and verified

- `portfolio_work/` (204 files), `uploads/` (all 3 user-provided files; 183,891 bytes), root deliverables, `completed_audits/`, `tools/`, and secrets were not deleted.
- The active ECOMOD v43 directory remains local (73 files); its main and SI PDFs are intact.
- `p11c_v6/` remains local (85 files) as an incomplete, unpromoted draft; no official v6 edition was created.
- All 412 other retained workspace-file records covered by the audit were rehashed after cleanup: **0 missing, 0 mismatched**. The three upload files were separately rehashed: **0 missing, 0 mismatched**.
- No published edition, existing remote version, or branch was deleted or overwritten. The only remote change is the separate recovery branch, which now also contains this receipt.

Empty folders left behind after individual file removal were not recursively deleted.

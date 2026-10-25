# Workspace reconciliation audit — 2026-10-25

**Status:** final audit and cleanup record. This report was first published before deletion; its pre-deletion state is preserved in the preceding recovery-branch commit. The current per-file CSV records the completed outcome for every audited path, including 474 verified local deletions. The inventory covers the 991 regular files scanned before cleanup, excluding user uploads, secrets, caches/toolchain, the temporary `gs2` clone, and this audit pair itself.

## Executive inventory

- Scanned **991 files** outside the explicit exclusions.
- **475 files / 45,850,635 bytes** were byte-verified against blobs in current remote branch/tag trees.
- **Three protected `portfolio_work/` files** are recorded as `REMOTE_HISTORY` in the 2026-10-24 audit and remain local; they are not deletion candidates.
- The ECOMOD v45 working candidate contained **553 files / 85,930,999 bytes**. Of these, **40** had exact matching blobs in current remote trees and **513 / 81,402,589 bytes** did not. All 553 were archived under the dated recovery path and byte-verified; this is a recovery snapshot, **not** an official ECOMOD v45 release.
- ECOMOD v43 local mirror before cleanup: **41 files / 2,730,203 bytes**, all byte-verified against current remote trees; all 41 were removed locally after per-file verification.
- ECOMOD v44 local package: **54 files / 7,433,023 bytes**, all byte-verified against current remote trees; retained locally as protected v44. No v44 path or remote object will be changed or deleted.
- No non-v45 local-only files were found outside the three protected portfolio history records.

## ECOMOD version and destination scope

The latest current `main` tip is `2efaa62083f2007dec3446c15c475af88f0925f3`, and the latest numbered package found on `main` is v44. The current branch/tag tip scan found no v45 package path or tag. The local `ECOMOD_VERSION_CURRENCY_v45.md` records the preceding full-history scan (1,638 reachable commits) and identifies v45 only as a working candidate. To avoid turning this recovery action into publication, the working candidate will be archived on the existing `workspace-recovery-2026-10-24` branch under:

`workspace_recovery_2026-10-25/local_only/ecomod_v45/`

The official v44 package on `main` remains untouched. No new official version number or release path is being created.

## Per-file evidence and cleanup gate

Every CSV row records local byte count, SHA-256, Git blob SHA-1, current remote path matches (when present), archive path, status, and disposition. The 475 current-tree matches were compared byte-for-byte via Git object retrieval. The 41 v43 and 54 v44 files were included in that verified set. All 553 v45 files were checked against the remote archive tree after push.

After the archive and updated audit were remotely verified, 474 listed files were removed individually: (a) the v43 local mirror; (b) superseded `ecomod_v45/output_v45*/` builds; and (c) stale pre-layout-fix renders in `output_v45_readability_20261025/visual_review/`. The current readability PDFs, `visual_review_after_flow/`, source, data, v44, `portfolio_work/`, `uploads/`, root deliverables, and all other local-only material were retained. Every deletion followed an immediate SHA-256, Git blob ID, remote tree-path, and remote-byte recheck.

## Exclusions and safeguards

- `/home/user/secrets/` was not read into the inventory or archived. User uploads remain untouched and excluded. Caches, toolchain files, and the temporary clone are outside the content archive.
- The stale `SHA256SUMS_v45_working.txt` is included as part of the candidate snapshot but is **not** treated as a release manifest; `REVIEW_STATUS_v45.md` already records that it must be regenerated before any release.
- The pre-deletion audit was published before cleanup. Its then-current statuses remain in Git history; the current CSV updates only the status of completed deletion candidates.


## Archive push verification (2026-10-25)

- The complete ECOMOD v45 working tree, initial per-file CSV, and report were pushed to `workspace-recovery-2026-10-24` at commit `a40ec7db0f22cf80cde76f55ac4f912beea43efc`.
- The archive tree contains all **553/553** v45 files at their planned paths; every Git blob was compared byte-for-byte with its local file: **85,930,999 bytes, 426 unique blobs, zero missing or mismatched files**. The final pre-deletion audit and archive README were then pushed and fetched at commit `4ed6c0d2bbced6921c0d8b4648bbe518726f3aea`, with all three updated files byte-verified.
- The 40 v45 files that also match current remote blobs are retained in the dated snapshot for complete path reconstruction; Git reuses identical blob content. The 513 previously unmatched files are now recoverable from the archive branch.
- The v45 PDFs/sources are archived as a working candidate only. The official v44 package on `main` was not touched.


## Cleanup completion (2026-10-25)

- The pre-deletion audit was remotely verified before cleanup at recovery-branch commit `4ed6c0d2bbced6921c0d8b4648bbe518726f3aea`. The archive commit is `a40ec7db0f22cf80cde76f55ac4f912beea43efc`.
- Removed **474 files / 70,371,071 bytes** from the local workspace, individually, after each candidate was matched to its audit row and checked against the corresponding remote tree path and byte content (**363 unique candidate blobs**). This comprises **41 ECOMOD v43 mirror files / 2,730,203 bytes** and **433 superseded v45 output or stale pre-flow-render files / 67,640,868 bytes**.
- The CSV now marks each completed removal `DELETED_LOCAL_AFTER_REMOTE_BYTE_VERIFICATION`. Its earlier, pre-deletion contents remain preserved in commit `4ed6c0d2bbced6921c0d8b4648bbe518726f3aea`.
- Post-cleanup review found all **474** listed deletion paths absent and all **517** other audited paths present with their audited size and SHA-256. ECOMOD v44 remains intact (**54 files**); **120** v45 files remain locally, including all **42** files in the current readability output tree.
- `portfolio_work/`, `uploads/`, `p11c_v6/`, root deliverables, all sources and data, and current post-flow renders were not removed. No changes were made to `main`; published v44 remains untouched.
- A separate cleanup receipt is published as `WORKSPACE_CLEANUP_RECEIPT_2026-10-25.md`.

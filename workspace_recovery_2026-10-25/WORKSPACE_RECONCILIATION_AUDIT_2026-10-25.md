# Workspace reconciliation audit — 2026-10-25

**Status:** pre-deletion audit. No files have been deleted. The per-file CSV beside this report is the controlling manifest. It covers all current workspace regular files except user uploads, secrets, caches/toolchain, the temporary `gs2` clone, and this audit pair itself.

## Executive inventory

- Scanned **991 files** outside the explicit exclusions.
- **475 files / 45,850,635 bytes** were byte-verified against blobs in current remote branch/tag trees.
- **Three protected `portfolio_work/` files** are recorded as `REMOTE_HISTORY` in the 2026-10-24 audit and remain local; they are not deletion candidates.
- The ECOMOD v45 working candidate contains **553 files / 85,930,999 bytes**. Of these, **40** have exact matching blobs in current remote trees and **513 / 81,402,589 bytes** do not. All 553 files are scheduled to be copied under the dated recovery archive path in this audit; this is a recovery snapshot, **not** an official ECOMOD v45 release.
- ECOMOD v43 local mirror: **41 files / 2,730,203 bytes**, all byte-verified against current remote trees; per-file deletion candidate after the archive/audit is verified.
- ECOMOD v44 local package: **54 files / 7,433,023 bytes**, all byte-verified against current remote trees; retained locally as protected v44. No v44 path or remote object will be changed or deleted.
- No non-v45 local-only files were found outside the three protected portfolio history records.

## ECOMOD version and destination scope

The latest current `main` tip is `2efaa62083f2007dec3446c15c475af88f0925f3`, and the latest numbered package found on `main` is v44. The current branch/tag tip scan found no v45 package path or tag. The local `ECOMOD_VERSION_CURRENCY_v45.md` records the preceding full-history scan (1,638 reachable commits) and identifies v45 only as a working candidate. To avoid turning this recovery action into publication, the working candidate will be archived on the existing `workspace-recovery-2026-10-24` branch under:

`workspace_recovery_2026-10-25/local_only/ecomod_v45/`

The official v44 package on `main` remains untouched. No new official version number or release path is being created.

## Per-file evidence and cleanup gate

Every CSV row records local byte count, SHA-256, Git blob SHA-1, current remote path matches (when present), archive path, status, and disposition. The 475 current-tree matches were compared byte-for-byte via Git object retrieval. The 41 v43 and 54 v44 files are included in that verified set. The 513 v45 blobs absent from current remote trees will be archived; all 553 v45 files will be checked against the resulting remote archive tree after push.

Only after the archive and updated audit are remotely verified may the listed candidates be removed: (a) the v43 local mirror; (b) superseded `ecomod_v45/output_v45*/` build directories, excluding the current `output_v45_readability_20261025/`; and (c) stale pre-layout-fix renders in `output_v45_readability_20261025/visual_review/`. The current readability PDFs, `visual_review_after_flow/`, source, data, v44, `portfolio_work/`, `uploads/`, root deliverables, and all other local-only material are retained. Deletion is per-file, only after immediate SHA-256 and remote-byte rechecks.

## Exclusions and safeguards

- `/home/user/secrets/` was not read into the inventory or archived. User uploads remain untouched and excluded. Caches, toolchain files, and the temporary clone are outside the content archive.
- The stale `SHA256SUMS_v45_working.txt` is included as part of the candidate snapshot but is **not** treated as a release manifest; `REVIEW_STATUS_v45.md` already records that it must be regenerated before any release.
- This audit was generated before any push or deletion; the subsequent archive push and byte verification are recorded in the addendum below. No deletion has yet occurred.


## Archive push verification (2026-10-25)

- The complete ECOMOD v45 working tree, the per-file CSV, and this report were pushed to `workspace-recovery-2026-10-24` at commit `a40ec7db0f22cf80cde76f55ac4f912beea43efc`.
- A fresh fetch confirmed that the remote branch tip equals that commit. The archive tree contains all **553/553** local v45 files at their planned paths; every Git blob was compared byte-for-byte with its local file: **85,930,999 bytes, 426 unique blobs, zero missing or mismatched files**.
- The 40 v45 files that also match current remote blobs are retained in the dated snapshot for complete path reconstruction; Git reuses identical blob content. The 513 previously unmatched files are now recoverable from the archive branch.
- The current v45 PDFs/sources are archived as a working candidate only. The official v44 package on `main` was not touched. **No cleanup or deletion has occurred yet.**

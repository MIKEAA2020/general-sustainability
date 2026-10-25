# Workspace cleanup receipt — 2026-10-25

## Result

Cleanup was completed only after the ECOMOD v45 working candidate, updated pre-deletion audit, and archive README were pushed to the separate recovery branch and remotely verified. The snapshot is a recovery archive, not an official v45 release. No published edition was overwritten.

- **Recovery branch:** `workspace-recovery-2026-10-24`
- **Archive commit:** `a40ec7db0f22cf80cde76f55ac4f912beea43efc`
- **Verified pre-deletion audit/README commit:** `4ed6c0d2bbced6921c0d8b4648bbe518726f3aea`
- **ECOMOD v45 archive:** 553/553 files, 85,930,999 bytes, 426 unique blobs; all archived paths and bytes were verified against the local candidate before cleanup.

## Local files removed

A total of **474 files / 70,371,071 bytes** were unlinked individually:

| Scope | Files | Bytes | Remote verification |
|---|---:|---:|---|
| `ecomod_v43/` older mirror | 41 | 2,730,203 | Exact byte matches in current remote trees |
| Superseded `ecomod_v45` outputs and stale pre-flow renders | 433 | 67,640,868 | Exact byte matches in the dated v45 recovery archive |
| **Total** | **474** | **70,371,071** | **363 unique candidate blobs byte-checked** |

Before each unlink, the local file was checked against its per-file audit record (size, SHA-256, and Git blob SHA-1); its remote tree path was resolved and its blob bytes were compared with the local file. The per-file CSV now labels these entries `DELETED_LOCAL_AFTER_REMOTE_BYTE_VERIFICATION`. The pre-deletion version of that audit remains available in the recovery branch history at commit `4ed6c0d2bbced6921c0d8b4648bbe518726f3aea`.

## Post-cleanup checks and protected material

- All **474** listed deletion paths are absent. All **517** other paths in the 991-record audit remain present and match their audited sizes and SHA-256 values.
- **ECOMOD v44:** all 54 local files remain present and verified. No changes were made to `main`; published v44 was not altered.
- **ECOMOD v45:** 120 files remain locally, including the active source/data and all 42 files in `output_v45_readability_20261025/`. The current readability PDFs and `visual_review_after_flow/` renders remain.
- `portfolio_work/`, `uploads/`, `p11c_v6/`, root deliverables, and other local-only material were not removed. No project-content directories were recursively deleted.

## Audit files

- `WORKSPACE_RECONCILIATION_AUDIT_2026-10-25.csv` — per-file inventory, remote/archive evidence, disposition, and completed deletion status.
- `WORKSPACE_RECONCILIATION_AUDIT_2026-10-25.md` — scope, chronology, archive verification, and cleanup summary.

This receipt records the local content cleanup. The ECOMOD v45 archive remains on the recovery branch for reconstruction; it is not represented as a numbered or published edition.\n\n## Temporary verification clone and budget\n\nThe per-file audit excludes `/home/user/gs2`, a temporary no-checkout Git clone used for repository verification. It contains no untracked files and no unique workspace deliverables; the archive, final audit, and receipt are remotely verified. At the end of verification it occupied about **345 MiB** because Git had cached repository objects. The clone is safely reproducible from the remote and may be removed after this receipt update is published and verified. Removing it affects no audited project files, uploaded data, or local-only material.

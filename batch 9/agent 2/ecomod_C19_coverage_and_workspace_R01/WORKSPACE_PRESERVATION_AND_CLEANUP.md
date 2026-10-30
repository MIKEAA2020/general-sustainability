# Workspace preservation and cleanup — R01

**Status:** completed. Preservation was published and byte-verified before the two narrowly scoped local deletions; the final cleanup result is recorded below.

## 1. Requested GitHub-release PDFs

The release `external_pdf_follow_up_ecomod` currently contains **12 assets totaling 68,693,788 bytes**, each with a provider-supplied SHA-256 digest. Every workspace PDF was checked by both asset filename and SHA-256 content identity.

- Local filename hits: **0**
- Local content-hash hits, including renamed PDFs: **0**
- Local release PDFs requiring deletion: **0**
- Remote release assets changed: **0**

The earlier R02 restoration index independently records that the former `uploads/` copies were streamed, hash-checked, and removed. The requested release PDFs are therefore already absent from the workspace.

## 2. Repository-wide preservation inventory

Before cleanup, local non-environment files were compared by Git blob identity with the current complete repository tree:

| Classification | Files | Meaning |
|---|---:|---|
| Exact content already in Git | 1,622 | Remotely recoverable; remote path(s) recorded in the compressed precheck index |
| Provider-derived and reproducible | 7 | Four provider PDFs and three text extracts under `source_followup_documents_2026-10-30/`; the published retrieval workflow and source URLs remain available |
| No exact Git copy yet | 12 | Small root-level Canada/source-audit operational records and completed publisher scripts |

The twelve unarchived operational creations are copied exactly into `operational_root_archive/` for additive publication. Their originals remain local. No completed publisher is executed again. The private PAT, environment files, and transient caches are excluded.

## 3. Why large older packages are not being pruned

A larger cleanup would break retained verification or contradict the active package record:

- **F11–F15:** F16 tests explicitly compare F15 inputs and hash **70 F15 files plus 597 protected F11–F14 files**. Removing these packages would make the retained F16 workflow incomplete.
- **C18:** C19’s record identifies C18’s complete local/remote archive and its full legacy budget workflow. C19 deliberately does not duplicate that archive. C18 therefore remains intact.
- **C19 and F16:** current active packages; retained.
- **Current governance and source documents:** retained; no unsupported deletion is used to manufacture headroom.

This dependency check supersedes the initial idea that F11–F15 might be disposable merely because they are older.

## 4. Narrowly scoped local cleanup candidates

Only two redundant ZIP containers pass all checks:

| Local file | Bytes | Remote preserved path |
|---|---:|---|
| `revision_audit_20261029.zip` | 410,315 | `batch 9/agent 2/workspace_archive_20261029/preserved/revision_audit_20261029.zip` |
| `journal_revision_evaluation_20261029.zip` | 144,176 | `batch 9/agent 2/workspace_archive_20261029/preserved/journal_revision_evaluation_20261029.zip` |

Their 34 and 21 archived entries respectively are byte-identical to files in the retained uncompressed directories. Both ZIPs already have exact remote Git blobs and earlier restoration-index records. Immediately before removal, their remote blobs will be downloaded and compared byte-for-byte again.

No other local file is scheduled for deletion. In particular, no PDF is deleted from the remote GitHub release.

## 5. Space status

The pre-cleanup workspace contained **101,174,821 logical file bytes (101.17 MB; 96.49 MiB)**. This is already below the 128 MB snapshot ceiling. The two redundant ZIPs total **554,491 bytes**; removing them is safe housekeeping, not a substitute for the dependency-aware retention policy above.

## 6. Final result

1. The preservation package was published at commit `03e9846cc023aba06cb727f78cc012d7d5b4b815`; all **24 current package files** were downloaded and byte-verified, including the twelve operational creations that had lacked an exact Git copy. No local file was deleted in that stage.
2. Immediately before deletion, both immutable remote ZIP blobs were downloaded again and matched the local files byte-for-byte. Their **34 and 21 entries** still matched the retained uncompressed directories.
3. Exactly **two local files** were then removed: `revision_audit_20261029.zip` and `journal_revision_evaluation_20261029.zip`. Total local space released: **554,491 bytes**. No remote file, remote release asset, manuscript, numerical output, or other local file was deleted.
4. Final workspace size: **100,674,313 logical file bytes (100.67 MB; 96.01 MiB)**, leaving approximately **27.33 MB** below a 128 MB ceiling.

Machine-readable result: `metadata/cleanup_result.json`. The remote restoration paths and immutable blob identities are retained there and in the earlier R01/R02 restoration indexes.

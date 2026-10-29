# Verified workspace archive and restoration index — 29 October 2026

The author requested repository backup before deleting recoverable local older drafts and ECOMOD packages to stay within the workspace budget. This archive is add-only; no older repository directory is deleted or overwritten.

`RESTORE_INDEX.json` maps each inventoried local file to its exact repository path, Git blob identity, SHA-256 and byte count. Matching uses actual local content, not just filename similarity. Creations not already present are preserved under `preserved/` before deletion. The publication process re-reads the published tree and downloads/verifies the restoration index before authorizing cleanup.

Retain the latest `ecomod_followup_F08/`, user uploads/private credentials, governing assessments and this index locally. Remove verified local copies of older empirical drafts and ECOMOD packages only. Private credentials are never uploaded. Upstream raw download caches and system/font caches are not author creations and are not redistributed; exact source identities and bounded retrieval scripts remain in F08. Operational source scripts, logs, receipts and QA renders from F07/F08 are preserved as historical evidence, not current manuscripts or scripts to rerun blindly.

## Restore a selected package

Run `python restore_files.py --prefix ecomod_c17 --list` to inspect the selection. Then run `python restore_files.py --prefix ecomod_c17 --restore --destination /your/chosen/folder` to retrieve only that package. Choose a destination with sufficient space. The script pins the archive publication commit, checks every downloaded SHA-256 and does not overwrite differing files. `publication_receipt.json` supplies the pinned commit after publication; alternatively pass `--commit` explicitly. Public GitHub raw-file access needs no credential. For a private repository, an optional `GITHUB_TOKEN` environment variable can be supplied without embedding it in a file.

Equivalent recovery is possible by cloning `https://github.com/MIKEAA2020/general-sustainability.git` and using the mapped repository paths. Do not clone the entire repository back into a constrained workspace just to recover one draft.

The archive's publication receipt and completed cleanup report are added after backup verification. Historical article PDFs and their source packages stay immutable in their original repository locations.

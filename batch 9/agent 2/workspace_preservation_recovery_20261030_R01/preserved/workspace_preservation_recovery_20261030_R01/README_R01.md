# Workspace preservation and recovery — 2026-10-30 R01

This operation follows the author's requirement: preserve and verify creations remotely before deleting any reclonable local copy. It does not edit manuscripts, merge branches, delete remote history, publish private uploads, or remove credentials.

## Findings before cleanup

- 22 surviving package manifests supplied **1,400 file checks**: every file exists and matches its expected SHA-256. No missing or altered manifested deliverable was found.
- The 2026-10-29 restoration index has 1,267 historical creation records. Of these, 995 original local paths are now absent, but **every absence was marked as a planned removal** in the earlier verified cleanup. No unplanned absence was found in that index. Their remote Git blob/path identities are rechecked before this cleanup.
- Excluded `.cache` directories do not persist across workspace snapshots. Loss of their software installations, compiled outputs, temporary trees or console stdout is distinct from loss of a published deliverable. No claim of byte-exact recovery is made for an unindexed, unarchived cache file.

## Preservation and recovery

`metadata/RESTORE_INDEX_R01.json` maps every surviving non-upload creation to an exact Git blob, SHA-256, repository path and byte count. A matching existing blob is reused only by content identity, never guessed from a similar filename. Previously unpublished creations are added at new paths under this R01 repository prefix. Every prior remote path/mode/hash is preserved. The new index and all newly uploaded content are downloaded and checked before cleanup.

The lost audit-reference cache is recovered as durable references from the exact main/SI audit commits. Their manuscript audit texts are exact repository bytes. The latest C18 publication status is reconstructed separately from authoritative published receipt/commit records; that reconstruction is explicitly not described as the original console log. The original C18 numerical data, code, sources, PDFs and build/test evidence survive and match their package manifest.

## Local space policy

Only these separately reclonable older package copies are scheduled for local removal:

- `ecomod_followup_F08/`
- `ecomod_followup_F09/`
- `governance_elevation_P4_v42_P01/`

Each file in each complete directory must be indexed, unchanged since inventory, present in the published tree, and independently downloaded byte-for-byte before removal. The active, complete C18 and governance v43 packages, graphical abstract, latest F10 follow-up, author-facing assessments/reviews, user uploads and private credential remain local. Keeping complete active packages avoids breaking dependencies by pruning their inherited subdirectories.

Original assessment-paper v76 source uploads and all privately supplied PDF parts are retained locally. Assessment/review creations are included in the remote-preservation inventory. Older assessment/manuscript copies already intentionally removed on 2026-10-29 remain available through that archive's verified restoration index; this operation does not redundantly restore every old version and immediately exceed the budget again.

## Restore only what is needed

From the retained operation directory:

```sh
python code/restore_selected_R01.py --prefix ecomod_followup_F09
python code/restore_selected_R01.py --prefix ecomod_followup_F09 --destination /home/user/.cache/restored_R01 --restore
```

The first command lists only. The second verifies SHA-256 and refuses to overwrite differing files. For an older package absent from this new local inventory, use `workspace_archive_20261029/restore_files.py` and its historical index instead. Do not clone the entire repository into a budget-constrained workspace.

Final publication receipts, actual removed file/byte totals, budget result and recovery limitations are recorded under `reports/` and the repository `completion/` directory. The one-shot preservation/prune driver must not be blindly rerun after publication; inspect its receipts and remote commits first.

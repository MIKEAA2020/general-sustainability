# Workspace preservation, recovery and space report

**Completed: 2026-10-30.** No remote files were deleted or overwritten, and no branch was merged.

## 1. Backup was verified before local deletion

- **1,323 surviving non-upload creation files** were matched to exact Git blobs and indexed for restoration.
- **1,267 historical creation records** from the prior workspace archive were rechecked against their repository paths and blob identities.
- Previously unpreserved content was added remotely; **15 new unique blobs** were downloaded and verified, along with the new restoration index.
- All **9,085 prior remote file/path/mode identities** were preserved by the first new commit.
- Even the pre-cleanup receipt was committed and downloaded before any local cleanup began.

Preservation commit: `696ca3d6a900997578a514a1caa0b91fe9927555`.  
Pre-deletion receipt commit: `74915c6a996e55cc0115e85cf8ee719751531a7a`.  
Completed cleanup/recovery record: `02ae671365dc3add6f80e7de5fe769712857177b`.

## 2. What was removed locally

Only complete, separately reclonable older package copies were removed, after downloading and byte-checking every file:

| Local copy | Files | Bytes freed |
|---|---:|---:|
| ECOMOD follow-up F08 | 174 | 11,581,605 |
| ECOMOD follow-up F09 | 203 | 11,828,002 |
| Governance v42 P01 | 87 | 6,228,796 |
| **Total** | **464** | **29,638,403** |

The visible workspace is now approximately **107 MB**, compared with approximately **135 MB** initially. This is below the 128 MB budget with roughly 21 MB headroom under a decimal interpretation. Recovery indexes and evidence account for the difference between gross files freed and net workspace reduction.

Retained locally: complete C18; complete governance v43 including its inherited dependencies; graphical abstract; latest F10 follow-up; author-facing assessments and reviews; original assessment-paper v76 text uploads; private PDF parts; and private credentials. No user upload or credential was published or removed. Older assessment/manuscript packages that had already been intentionally pruned remain in the earlier restoration index and repository history; they were not needlessly recloned into the constrained workspace.

## 3. Recovery findings

**No lost manifested manuscript, data or code deliverable was found:** all **1,400 checks from 22 surviving manifests** matched the expected SHA-256 before cleanup.

The older restoration index has 995 absent local paths, but every one was explicitly marked for removal in the previous verified cleanup. It contains **zero unplanned absent paths**. Their original remote copies were reverified.

The missing temporary `.cache` directory is a different matter: workspace snapshots exclude caches and installed software by design. The known main/SI audit-reference texts were recovered byte-for-byte from their exact commits, with their commit metadata saved durably under `recovered_references/`. C18 publication status was reconstructed from its published receipt and authoritative commit, explicitly not mislabeled as the original console transcript. The surviving C18 package still contains the sources, data, scripts, PDFs and build/test evidence needed to reproduce its results.

**Limit:** unindexed, unarchived cache stdout or build intermediates cannot be certified as recovered exactly. This report does not invent or claim such a recovery. Original inputs and reproduction tools were retained instead.

## 4. Post-cleanup verification

- All **859 retained files from the new pre-cleanup inventory** still exist and match their recorded SHA-256.
- The three scheduled older local directories are absent; their exact remote blobs remain available.
- A removed governance-v42 report was restored with the provided selective-restoration tool into an excluded temporary test directory and its SHA-256 checked successfully.
- Active packages were kept complete rather than deleting inherited dependencies and silently breaking their build/test paths.

## 5. Selective restoration

Retained local index: `workspace_preservation_recovery_20261030_R01/metadata/RESTORE_INDEX_R01.json`.

```sh
cd /home/user/workspace_preservation_recovery_20261030_R01
python code/restore_selected_R01.py --prefix ecomod_followup_F09
python code/restore_selected_R01.py --prefix ecomod_followup_F09 --destination /home/user/.cache/restored_R01 --restore
```

The first command only lists. The second downloads exact blobs, checks SHA-256 and refuses to overwrite differing files. Restore only the selected working version with adequate space; do not clone the whole repository back into this workspace.

For older assessment/ECOMOD versions already absent before this operation, use `workspace_archive_20261029/RESTORE_INDEX.json` and its `restore_files.py` tool.

Repository archive: [workspace preservation/recovery R01](https://github.com/MIKEAA2020/general-sustainability/tree/02ae671365dc3add6f80e7de5fe769712857177b/batch%209/agent%202/workspace_preservation_recovery_20261030_R01).

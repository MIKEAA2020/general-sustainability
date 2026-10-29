# R02 — stronger workspace reduction and memory-based reconstruction

The author explicitly requested removal of the assessment paper after preservation, not merely verification that the workspace narrowly fits its budget. R01 over-retained original uploads. R02 corrects that decision.

## Local removals, only after remote verification

1. The uploaded Paper06 assessment v76 main and supplementary source texts.
2. Their obsolete local audit-material bundle and root-level v76 audit copies, all already repository-backed or newly preserved before deletion.
3. The inactive complete F10 package and older ECOMOD input drafts, using exact repository blobs.
4. Nine large CCI Biomass ATBD PDF chunks. These are **not** the assessment paper: their first pages identify the CCI Biomass ATBD v7. They already exist in the author's `external_pdf_follow_up_ecomod` release. Each is streamed again and checked against the local SHA-256 and byte length before removal. They are not newly redistributed or uploaded to the source tree.

Complete active C18 and governance v43 packages, graphical abstract, governing journal assessments/review decisions, small current source registries/review notes, prior restoration tools and private credential remain local. No active package is rendered incomplete by removing inherited dependencies.

## Memory recovery

`MEMORY_RECONSTRUCTION_R02.md` restores useful operational details from retained conversation context: acquisition sequence, model-version comparison, budget isolation, reproduction/build/test sequence, specific build/CSV fixes, QA changes and publication identities. It is explicitly **not** a byte-exact cache transcript.

`code/recover_C18_sources_R02.py` is a new tested replacement for the missing temporary acquisition helper. It reads the retained 189-file C18 source manifest, checks hashes, selectively restores missing immutable Git blobs and refuses to overwrite differing files. The pinned tree cache is regenerated from the immutable source commit and recorded with an explicit new-serialization label.

Unavailable original stdout bytes, timings and deleted binary intermediates are not fabricated. Existing published result files and sources govern scientific statements.

## Restore later without cloning the whole repository

`RESTORE_INDEX_R02.json` records exact Git blobs and hashes for repository-backed copies, including author uploads before deletion. Use `code/restore_repository_file_R02.py --prefix uploads/paper06_assessment_separation_v76.txt` to list the preserved assessment source; add `--restore --destination /home/user/.cache/restored_R02` only when needed. The tool verifies hashes and refuses to overwrite differing files. `metadata/EXTERNAL_RELEASE_RESTORE_INDEX_R02.json` gives byte identities and URLs for the third-party release PDFs.

Example source-input check:

```sh
python code/recover_C18_sources_R02.py
# Explicitly retrieve only missing source inputs:
python code/recover_C18_sources_R02.py --prefix repository_sources/ --restore
```

The cleanup driver is one-shot. Do not blindly rerun it after successful publication; inspect PRESERVATION_RECEIPT_R02.json and CLEANUP_RESULT_R02.json. Every repository update is additive, every removal is local and remote-verified, and credentials are never published.

# Recovery status addendum — 2026-10-25

## Additional preserved material

- `AS_FOUND_STAGING_COPY_20261025/` is a byte-for-byte copy of the staging directory as it existed during recovery. It includes its PDFs, TeX, logs, parts, figures, README, audit notes, and existing `SHA256SUMS.txt`. The checksum file was copied as found; it was neither refreshed nor validated.
- `CURRENT_ROOT_DOCS/` preserves copies of the current root README, review status, changelog, and the known-stale root checksum text, each under separately descriptive names. No root file was altered.

## Reconstructed pre-page-break PDF build

Tectonic completed successfully in `RECONSTRUCTED_PRE_PAGEBREAK/build_with_local_assets_01/`: reconstructed main PDF = 35 pages; reconstructed SI PDF = 20 pages. The reconstructed source parts are current parts with only the inserted S4.2 page-break command removed from SI; the existing S4.4 break remains. Figure assets required for repeatable compilation were copied into the reconstruction subfolder.

An initial compile attempt is retained in `RECONSTRUCTED_PRE_PAGEBREAK/build/`; it stopped because figure assets were not in that first build context. It is an incomplete diagnostic attempt, not a deliverable. Nothing was deleted or replaced when the successful build was run; it used the distinct `build_with_local_assets_01/` directory.

The rebuilt PDFs are newly generated reconstructions, not the exact pre-overwrite PDF bytes. The reconstructed main TeX is byte-identical to current main TeX according to the earlier comparison; the reconstructed SI TeX differs from current SI only by removing the newly inserted S4.2 `\par\pagebreak`. The exact historical `SI_verified` PDFs are still not available in the inspected Git commits.

## Staging PDFs and exact-original caveat

The copied staging directory contains named `ECOMOD_v45_citation_framing_SI_verified_20261025_main.pdf` and `_SI.pdf` files. Their sizes match the latest QA PDFs. Treat them as copies of the currently present staging artifacts—not as proof of recovery of the earlier overwritten/deleted PDF bytes.

## Push status

No push was performed. The session record carried a standing “no push without separate authorization” constraint. The question asking why no push happened is not an explicit new push instruction; a PAT alone does not override that constraint. The audit clone is `/tmp/ecomod_repo_audit`; `/home/user/ecomod_v45` itself is not a Git checkout.

# ECOMOD v45 recovery note — 2026-10-25

## SI content recovery and canonical replacement

The original pre-follow-up `SI_verified` PDF binary was overwritten/deleted during packaging; its exact original bytes were not recovered. **The content was not lost.** The SI assembled from current `parts/si_*.tex` was rebuilt in a new directory and its extracted text matches the currently staged `SI_verified` PDF page by page after whitespace normalization: 20 pages, 9,111 tokens, zero diff hunks. The assembled TeX is byte-identical to the current staged SI TeX and to `manuscript_working_si.tex`.

The staged PDF and fresh build are **not byte-identical** (the new build is one byte shorter), so the staged file is not the recovered original binary. The staged PDF is retained unchanged as a source-verified text-comparison artifact.

**Canonical replacement:** `RECOVERED_ARTIFACTS_20261025_01/CURRENT_SOURCE_SI_REBUILD_20261025_01/SI_verified_rebuilt_from_source.pdf`. It is a separately named copy of the fresh build in `BUILD_02/REBUILT_CURRENT_SOURCE_SI.pdf`; both remain in place. The staged file `output_v45_citation_framing_SI_verified_20261025/ECOMOD_v45_citation_framing_SI_verified_20261025_SI.pdf` is the retained verification artifact, not the canonical replacement. Their SHA-256 values are recorded in the accompanying fresh working manifest.

## Citation-audit SI status

The citation-audit SI is **superseded, not a substitute**. A copy of its PDF and SI TeX, with a defect note, is in `SUPERSEDED/`; the original citation-audit files were not moved, renamed, or deleted and are marked by `output_v45_citation_ack_audit_20261025/SUPERSEDED_NOTICE.md`. The three defects relative to current main/source are: reversed `Abaee2026a/b` mappings; Eq. (19) cited for the balance point even though the current balance-point formula is Eq. (18) and Eq. (19) is `J`; and the broader “specified acceptance-gap region” Paper06 framing instead of the witness-defined diagonal-gap scope.

## Local bundle and checksum status

The package README inside `output_v45_citation_framing_SI_verified_20261025/` already identifies that directory as a local-only, unapproved working follow-up and lists its bundle contents. A one-line clarification was appended to root `README.md` so the current staged/source-verified status is explicit.

At your explicit request, `SHA256SUMS_v45_working.txt` was freshly generated from current bytes with a **fresh generation, not restoration** header. The previous stale checksum file was copied to `SUPERSEDED/SHA256SUMS_v45_working_PRE_REFRESH_20261025.txt` before the root manifest was regenerated. The package-level `output_v45_citation_framing_SI_verified_20261025/SHA256SUMS.txt` was not refreshed. This one-time refresh does not imply permission for future refreshes.

## Process rule

No packaging, no checksum refresh, push all creations at each round to avoid future loss. Archive, don't overwrite; never replace a verified directory in place.

The new local artifacts were created under new names. No source PDF, source TeX, staged SI, or citation-audit original was overwritten, deleted, or renamed. A remote push is a separate step; no target branch was specified in this request.

# ECOMOD C19 coverage and workspace preservation — R01

This additive package records two checks requested on 31 October 2026:

1. **ECOMOD coverage:** [ECOMOD_C19_COVERAGE_AUDIT.md](ECOMOD_C19_COVERAGE_AUDIT.md) concludes that no further main/SI redistribution or restorative edit is needed. Re-run with `python code/verify_ecomod_coverage.py` while the retained C18/C19 packages are present.
2. **Workspace preservation and cleanup:** [WORKSPACE_PRESERVATION_AND_CLEANUP.md](WORKSPACE_PRESERVATION_AND_CLEANUP.md) records the release-PDF check, repository-wide content inventory, preservation of previously unarchived operational files, dependency constraints, and the narrowly scoped local cleanup.

## Preservation evidence

- `metadata/workspace_preservation_precheck.json.gz`: 1,622 local files already had exact content in the current Git tree; seven provider-derived files are reproducible from their documented retrieval workflow; twelve root-level operational files lacked an exact Git copy before this package.
- `operational_root_archive/`: exact copies of those twelve files. Their original root files remain in place; no completed publisher was run.
- `metadata/release_pdf_workspace_check.json`: all twelve assets in `external_pdf_follow_up_ecomod` remain remotely available with SHA-256 digests; no local filename or content-hash match exists, so no release PDF needed deletion.
- `metadata/operational_root_archive_manifest.json`: byte identities and provenance for the additive operational archive.

No manuscript, numerical result, remote release asset, earlier package, or companion deposit is modified by this audit. The private credential and environment files are excluded from preservation inventories and uploads.

# ECOMOD v45 citation, acknowledgments, and overcorrection audit — 2026-10-25

## Status and provenance

This is a focused audit-and-correction package for the **ECOMOD v45 working candidate**. It is not a new numbered edition, an official release, or a change to published v44. The earlier v45 readability-corrections package remains untouched in `output_v45_readability_corrections_20261025/`.

The editable source parts in `source_parts/` and the assembled TeX/PDF files here represent the post-audit working state. Figure and data assets remain in the base v45 candidate directory (`/home/user/ecomod_v45/`); this folder is an audit package, not a standalone source archive.

## Corrections in this package

- Restored the acknowledgment wording from v44, including the editors' “trust and support” and Arena.ai's “ingenuity and online tools.”
- Updated the three companion citations to the latest located versions: Paper4 v41, assessment Paper06 v71, and material-ledgers Paper3 v50. Paper06's current title and current theorem locators replace the older v59 title and supplementary theorem locator.
- Kept the existing ECOMOD author-year key mapping (`Abaee2026a` governance; `Abaee2026b` assessment; `Abaee2026c` ledger companion).
- Corrected two abstract phrasings that had compressed the model too far: conversion is triggered when supply available to people falls short of demand—not when fast-land supply alone is insufficient—and the reduced fixed-demand model has at most one balance point, with the demand ceiling distinguished from the above-ceiling approach to the area floor.
- The intentional ECOMOD title, data vintage, equations, numerical results, propositions, and disclosure statements were not changed.

See `AUDIT_NOTES_ECOMOD_v45_citation_ack_audit_20261025.md` for the branch/version scan, title decisions, readability findings, and the separate Paper3 v50 package-metadata note.

## Build and verification

- Built with Tectonic 0.17.0 (the Linux release asset was SHA-256 verified before use).
- Main manuscript: **34 pages**. Supplementary Information: **20 pages**.
- Main and SI citation keys resolve; the obsolete v59 title and `Theorem S2(ii)` locator are absent from the assembled source/PDF.
- The prior proofing fixes remain in the source: the Table 1 symbols, the single §4.4 heading and §4.3 gate/share paragraph, Table 2 notation/units, and the complete contribution paragraph.
- Non-fatal layout warnings remain, including the previously observed 2.608 pt overfull box in the main document and underfull-box warnings. There are no compile errors or unresolved references.

The generic `manuscript_working_*` outputs are build intermediates; the edition-labelled PDFs and TeX files are the deliverables.

`SHA256SUMS_ECOMOD_v45_citation_ack_audit_20261025.txt` records checksums for the other files in this package.
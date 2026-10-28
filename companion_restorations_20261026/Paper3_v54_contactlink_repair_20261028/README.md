# Paper3 v54 — local ORCID-link repair

This is a separate local copy of the Paper3 v54 source and PDF, prepared solely to correct the ORCID hyperlink target. The original `Paper3_v54/` source and PDF remain unchanged.

The only source edit removes the line-breaking command from inside the ORCID URI. The visible author, title, and manuscript text are otherwise unchanged. The mailto link is retained.

Build with `./build_contactlink_repair.sh` (pdfLaTeX by default). The build logs, engine record, and title-page render checks are in `QA/`. The repaired 54-page PDF has valid `mailto:amin_abaee@ut.ac.ir` and `https://orcid.org/0000-0002-0019-1842` annotations, confirmed with `mutool`; no unresolved references/citations, fatal TeX errors, or overfull boxes were found. The original v54 PDF and repaired title page were visually compared. This is not a new numbered release or DOI deposit. The local repair copy is included on branch `agent/p06-ecomod-c11-local-draft-20261028`. SHA-256 values are listed in `SHA256SUMS_contactlink_repair_20261028.txt`.

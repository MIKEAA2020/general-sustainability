# Paper 3 latest deliverables — 2026-09-19

This directory is the re-cloneable snapshot of the latest Paper 3 work. It contains the article sources, target-specific journal cuts, supplementary material, figure assets, validation records and deposit archives.

## Contents

- `manuscript/`: the article source and the related methods, accounting-standards and supplementary records.
- `journal_variants/`: the Journal of Industrial Ecology and Ecological Economics cuts, rendered PDFs, figure assets, validation records and ancillary source checks.
- `deposit/`: the public-record package archives and their sidecar checksums.
- `audit/`: validation and evidence-status records.
- `build/` and the verification utilities: reproducible staging and checks for the archived source records.

The Journal of Industrial Ecology package identifies the three linked public records explicitly. The main article record is `https://doi.org/10.6084/m9.figshare.33942451`; the methods record is `https://doi.org/10.6084/m9.figshare.33942469`; and the accounting-standards record is `https://doi.org/10.6084/m9.figshare.33942487`. The expanded local package is not represented as an externally uploaded or newly assigned DOI record.

## Verification state

- JIE: 4,262 body words under the 6,000-word local math-excluding count; rendered PDF: 11 pages.
- Ecological Economics: 4,245 body words under the 8,000-word local count; rendered PDF: 11 pages.
- The JIE supplement and cover letter compile successfully; the JIE figure asset is checked against the source references.
- No credentials are included in this directory.

## Rebuild/check commands

The journal-cut validator is under `journal_variants/`. The TeX sources and PDFs are under `journal_variants/rendered/`. The article and supplementary sources are independent of the build utilities and can be inspected directly.

The third-party source tables used by selected analyses remain outside this snapshot and are referenced through their respective evidence records.

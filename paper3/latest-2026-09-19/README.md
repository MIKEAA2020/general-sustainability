# Paper 3 latest deliverables — full-length article v50

**Snapshot chronology:** This folder was initially assembled on 2026-09-19. The current full-length article files (v50 Markdown, TeX, and PDF) were added on 2026-09-21. This metadata reconciliation is dated 2026-10-25.

## Current full-length article

The current full-length article is v50:

- `manuscript/paper3_material_ledgers_v50.md` — Markdown source.
- `manuscript/paper3_material_ledgers_v50.tex` — corresponding TeX source.
- `manuscript/paper3_material_ledgers_v50.pdf` — 54-page PDF cited as v50.

The v50 revision updates the titles of the linked companion-work references; the v50 PDF reflects those updates. The v49 Markdown, TeX, and PDF are retained in `manuscript/` as historical prior files. They have not been overwritten and are not the current full-length citation target.

`CHECKSUMS.sha256` is a directory-wide SHA-256 manifest for all regular files in this folder except the manifest itself. It covers both the retained v49 files and current v50 files. To verify, run `sha256sum -c CHECKSUMS.sha256` from this directory.

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

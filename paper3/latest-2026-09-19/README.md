# Paper 3 latest deliverables — 2026-09-19

This directory is the re-cloneable snapshot of the latest Paper 3 work from the workspace.
It contains the v49 full-length line, both target-specific journal cuts, the Route C prototype,
and the two deposit archives.

## Contents

- `manuscript/`: the latest full-length article, supplementary material and Companions A and B.
- `journal_variants/`: JIE and Ecological Economics cuts, rendered PDFs, figure assets, validation and Route C sources.
- `deposit/`: the full-length Figshare-ready deposit and v49 supplementary package, each with a sidecar checksum.
- `audit/`: the evaluation, v49 notes/reply and final verification reports.
- `v49/`: the v49 verification/package/push scripts.
- `build/`: the reproducible Figshare staging/build script.

The v49 archive branch remains separate at
`archive/paper3-v48-workspace`, under `paper3 v49 humanized line 2026-09-19/`.
It is an archive branch, not `main`.

## Verification state

- JIE: 4,434/6,000 local body words; rendered PDF: 12 pages.
- Ecological Economics: 4,245/8,000 local body words; rendered PDF: 11 pages.
- Both journal PDFs pass the current validation, page, unresolved-reference and overfull-box checks.
- Route C prototype: four tests passing; it is not a supported EMS software contribution.
- v49 verifier: `FAILURES: none`.
- An author-supplied public Figshare preprint record is available at https://doi.org/10.6084/m9.figshare.33942451; the expanded 49-record package here is separately checksummed and should not be conflated with that record without version matching.

## Rebuild/check commands

The journal-cut renderer and validator are under `journal_variants/`. The full-length v49 package
builders are under `v49/` and expect the historical workspace layout if used as builders rather than
as archival source. `tools/tectonic` is intentionally not included because of its size.

## Licence and credentials

The repository contains no credential. In particular, `github_pat.txt` was deliberately excluded
from the commit and must never be committed, copied into a package, or printed in a log.

The 16 MB third-party GFN NFA source tables remain outside this snapshot and outside the v49 package.

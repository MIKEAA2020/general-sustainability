# Files to upload to the Ecological Modelling portal — final list

**Manuscript:** ECOMOD-26-1191, "A rising biocapacity total can mask ecological-capital land drawdown: a two-land model"
**Version:** ECOMOD C20 A01, 31 October 2026 — main 38 pp, SI 31 pp
**Preprint DOI:** 10.20944/preprints202611.0852.v1 · **Reproduction package DOI:** 10.5281/zenodo.24092131
**Folder:** `/home/user/ecomod_C20_EM_upload/`

Upload these **13 items**. Everything else in the folder is either optional or comes from you.

## Required

| # | EM slot | File | Size |
|---|---|---|---|
| 1 | Revised manuscript (unmarked, editable source file) | `Manuscript_ECOMOD_C20_A01.tex` | 94 KB |
| 2 | Revised manuscript (PDF) — if the portal asks for a PDF | `Manuscript_ECOMOD_C20_A01.pdf` | 502 KB |
| 3 | Supplementary material — PDF | `Supplementary_Information_ECOMOD_C20_A01.pdf` | 533 KB |
| 4 | Supplementary material — LaTeX source (if the portal asks) | `Supplementary_Information_ECOMOD_C20_A01.tex` | 97 KB |
| 5 | Figure | `Figure_1.pdf` | 54 KB |
| 6 | Figure | `Figure_2.pdf` | 20 KB |
| 7 | Figure | `Figure_3.pdf` | 16 KB |
| 8 | Figure (SI) | `Figure_S1.pdf` | 19 KB |
| 9 | Figure (SI) | `Figure_S2.pdf` | 18 KB |
| 10 | Figure (SI) | `Figure_S3.pdf` | 18 KB |
| 11 | Figure (SI) | `Figure_S4.pdf` | 16 KB |
| 12 | Figure (SI) | `Figure_S5.pdf` | 26 KB |
| 13 | Highlights | `Highlights_ECOMOD_C20_A01.txt` | 0.8 KB |

## Optionally required by the portal

| EM slot | File | When |
|---|---|---|
| Graphical abstract | `Graphical_Abstract_ECOMOD_C20_A01.tiff` (or `.pdf`, `.png`) | EM has a graphical-abstract slot filled from before; upload the new one to replace the legacy graphic |
| Cover letter | `Cover_Letter_ECOMOD_C20_A01.docx` | If the slot is open on resubmission |
| Response to reviewers | `00_Response_to_Reviewers_ECOMOD_C20_A01.txt` | Required for a revision; replaces the previous response file |
| Response to reviewers (attachment) | `01_BEFORE_AFTER_v35_vs_C20.txt` | Companion to the response |
| Data availability statement (file copy) | `DATA_AVAILABILITY_ECOMOD_C20_A01.md` | If EM asks for the statement as a file; the text itself is already in the manuscript |
| Reproduction guide | `REPRODUCTION_GUIDE_ECOMOD_C20_A01.md` | Optional supplement; shows how to rebuild and re-run |
| Figure captions list | `FIGURE_CAPTIONS_ECOMOD_C20_A01.md` | Only if EM asks for captions separately |
| Figure source code | `CODE_AND_FIGURE_SOURCES/` (3 scripts + `requirements.txt`) | Optional; the code is already archived at the Zenodo DOI |
| LaTeX dependencies | `LaTeX_dependencies/` (8 figure PDFs + 9 table fragments) | Only if someone must compile the `.tex`; EM does not compile |

## Comes from you, not from this folder

| Item | Status |
|---|---|
| Declaration of competing interests (`.docx`) | Already in EM from the earlier submission; re-use |
| Author confirmation / ORCID | In the manuscript: Amin Abaee, ORCID 0000-0002-0019-1842 |
| Data-availability field text | Paste `https://doi.org/10.5281/zenodo.24092131` |

## Do not upload

`manuscript_ECOMOD_v41.tex`, `03_SUPPLEMENTARY_INFORMATION_v2.md`, `04_FIGURE_CAPTIONS.md`, `05_REPRODUCTION_GUIDE.md`, `06_DATA_AVAILABILITY.md`, `Highlights11_HIGHLIGHTS.txt`, `FigureS1…S13*.png` (the superseded single-stock PNG suite), `composition_attribution.py`, `real_series_aggregation_face.py`, and the legacy `GraphicalAbstract.*`. All belong to the earlier generation and contradict the submitted text (1961–2022, +23%, 2.85×, `gha·yr⁻¹`).

## Counts and identities

- 13 required/optional-primary files + 1 graphical abstract = the complete submission.
- Figure PDFs are vector, fonts embedded, one page each.
- Highlights: 5 bullets, longest 80 of 85 permitted characters.
- Graphical abstract: 1328 × 531 px, meets Elsevier's 1328 px minimum width.
- Keywords in the manuscript: six (within the 1–7 limit).
- Verification: main 38 pp, SI 31 pp, zero LaTeX warnings, zero overfull boxes, no unresolved references or citations; source ZIP rebuilds to identical page counts from a clean extraction.

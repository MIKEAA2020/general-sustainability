# EM upload checklist — ECOMOD C20 A01 (ECOMOD-26-1191)

Everything in this folder is upload-ready. Item names below match the Editorial Manager slots you listed.

## Upload these (current, verified)

| EM slot | File | Notes |
|---|---|---|
| Revised manuscript (unmarked, editable source) | `Manuscript_ECOMOD_C20_A01.tex` | 38 pp; embedded bibliography; no BibTeX needed |
| Revised manuscript (PDF) | `Manuscript_ECOMOD_C20_A01.pdf` | Use if EM asks for both source and PDF |
| Supplementary material | `Supplementary_Information_ECOMOD_C20_A01.pdf` | 31 pp; also `…SI…tex` if the source is wanted |
| Figure | `Figure_1.pdf` | vector, fonts embedded, 1 page |
| Figure | `Figure_2.pdf` | vector, fonts embedded |
| Figure | `Figure_3.pdf` | vector, fonts embedded |
| Figure (SI) | `Figure_S1.pdf` … `Figure_S4.pdf` | one-stock comparator, SI S7 |
| Figure (SI) | `Figure_S5.pdf` | technology-wave experiment, SI S8 |
| Highlights | `Highlights_ECOMOD_C20_A01.txt` | 5 bullets, longest 80/85 characters |
| Graphical abstract | `Graphical_Abstract_ECOMOD_C20_A01.tiff` | 1328 × 531 px (Elsevier minimum width met); `.pdf` and `.png` also supplied |
| Response to reviewers | `00_Response_to_Reviewers_ECOMOD_C20_A01.txt` | rewritten against the submitted text |
| Response to reviewers (attachment) | `01_BEFORE_AFTER_v35_vs_C20.txt` | replaces the old before/after note |
| Supplementary material | `REPRODUCTION_GUIDE_ECOMOD_C20_A01.md` | rebuild and re-execution instructions |
| Data availability (field + file) | `DATA_AVAILABILITY_ECOMOD_C20_A01.md` | statement as printed in the paper, dataset link, Option C compliance table |
| Figure captions (optional) | `FIGURE_CAPTIONS_ECOMOD_C20_A01.md` | verbatim from the LaTeX sources; use only if EM asks for a separate caption list |
| Figure source code (optional) | `CODE_AND_FIGURE_SOURCES/` | 3 scripts + pinned requirements; replaces the old two .py files |
| LaTeX dependencies (optional) | `LaTeX_dependencies/` | figure PDFs + 9 table fragments so the .tex compiles anywhere; EM does not need it |
| Cover letter | `Cover_Letter_ECOMOD_C20_A01.docx` | updated for this version |

Still needed from your side, unchanged and still valid: the **Declaration of competing interests** (`.docx`, already in EM) and any **author/ORCID** confirmations.

## Do not re-upload (superseded)

| Old file | Why it is out of date |
|---|---|
| `manuscript_ECOMOD_v41.tex` | Five model/empirical generations old; units convention since reversed; no NFA 2026 analysis, no identification bounds, no budgets |
| `03_SUPPLEMENTARY_INFORMATION_v2.md` | Superseded by the typeset SI (S1–S12); the .md is not the submitted SI |
| `04_FIGURE_CAPTIONS.md` | Captions are in the LaTeX and PDF; a current list, extracted verbatim from the sources, is supplied as `FIGURE_CAPTIONS_ECOMOD_C20_A01.md` |
| `FigureS1…S13_*.png` | Thirteen single-stock PNGs; the current SI uses five vector PDFs (S1–S5). The rest belong to the superseded single-stock presentation |
| `FigureS1_feedback_diagram.png`, `…tau_g_calibration.png`, `…fishery_recovery.png`, `…bf_af_calibration.png`, `…multi_ecosystem_tau_g.png` | Single-stock material, now SI S7/S8 text and Figs. S1–S5 |
| `Highlights11_HIGHLIGHTS.txt` | Quoted +23%, 2.85×, 1961–2022 and "typed floor" — all superseded (`Highlights_ECOMOD_C20_A01.txt` replaces it) |
| `composition_attribution.py`, `real_series_aggregation_face.py` | Superseded figure code; the current generators are in `CODE_AND_FIGURE_SOURCES/` |
| `GraphicalAbstract.pdf/.png/.tiff` | Legacy graphic with the +24.5% / 1961–2022 strip and `R_fc` notation; replaced by `Graphical_Abstract_ECOMOD_C20_A01.*` |
| `05_REPRODUCTION_GUIDE.md`, `06_DATA_AVAILABILITY.md` | Replaced by `REPRODUCTION_GUIDE_ECOMOD_C20_A01.md` and `DATA_AVAILABILITY_ECOMOD_C20_A01.md`, whose links and numbers match the submitted version |
| `00_UPDATED_REVIEWER_RESPONSE.txt`, `Response to reviewers-01_…txt` | Contain the withdrawn units convention and 1961–2022 values; replaced |

If EM does not allow deleting old files, upload the new ones and note in the cover letter that the previous attachments are superseded, so the editor uses the C20 set.

## Resolved / remaining

1. **Keywords and frontmatter layout — done, no content touched.** The manuscript carries **six** keywords: biocapacity; ecological footprint; land-use conversion; aggregation; identifiability; delay differential equations. The keyword line had been spilling two words onto page 2 since C19. That straddle was a typesetting fault, so it was fixed in the layout: the abstract block now uses 14 pt leading (font size and every word unchanged; abstract still 217 words). Keywords sit entirely on page 1, no text overlaps, zero LaTeX warnings, and the main text is **38 pages** (one page shorter because the title page now closes cleanly). No abstract text was edited, and none should be.

2. **Graphical abstract permission/GenAI statement.** The GA is generated from the manuscript's own computed outputs, so no third-party material is involved; if EM asks, that is the answer. It contains no provider imagery.
3. **Zenodo deposit** for the Option C data requirement is prepared: `ecomod_zenodo_deposit/` — new version of record 22554480, not a new deposit. See `HOW_TO_DEPOSIT.md`.

## Not needed for this journal submission

- The **Preprints.org source ZIP** (`ecomod_C20_preprints_source_20261031.zip`) is for the Preprints.org source-file request, not for EM. EM wants the manuscript, SI, figures and declarations. The ZIP can stay out of the submission.
- **Numerical code and data** are referenced through the Data availability statement rather than uploaded, which matches research-data Option C (repository deposit with citation). The reproduction guide explains how to obtain and run them.

## Where the SI LaTeX is

`Supplementary_Information_ECOMOD_C20_A01.tex` (97,423 bytes) is in this folder — third row of the upload table. It is the editable source of the 31-page SI. Like the main source it references `figures/`, `tables/` and `inherited_C17/…` by relative path; copy it into `LaTeX_dependencies/` to compile it there, or use the Preprints source archive, where both documents build with three `pdflatex` passes and no BibTeX step.

## Option C, in the journal's own words

Ecological Modelling applies Option C of Elsevier's research-data guidelines, which **requires** depositing the research data in a relevant repository, supplying a link to the dataset during submission, and — only where sharing is impossible — a statement explaining why. Sharing is possible here, so the requirement is the deposit plus the link, not an explanation. Consequences for this upload:

- The data/code files are **not optional**. They are the deposit backing the statement.
- The link goes in the submission system's data-availability field: `DATA_AVAILABILITY_ECOMOD_C20_A01.md` holds the exact text and the URL to paste.
- GitHub is a code host without a DOI. A Zenodo or Figshare DOI for the reproduction package would put the submission on the strongest footing; the package can be deposited as-is.

# C20 A01 — deposit DOI added to the manuscript

**Date:** 31 October 2026
**Base:** frozen C19 A01 (unchanged at 39 pp main / 31 pp SI)
**Preprint DOI recorded in the manuscript:** https://doi.org/10.20944/preprints202611.0852.v1 (version 1)
**Main:** 38 pages · **SI:** 31 pages · 0 LaTeX warnings, 0 overfull boxes, no unresolved references or citations

## Changes

**(i) Deposit DOI** — one addition per document; no other text, claim, number, figure, table or reference was altered.

1. **Main, Data availability paragraph:** a closing clause, "Deposited at \url{https://doi.org/10.20944/preprints202611.0852.v1}."
2. **SI, end of §S12 (before Supplementary references):** "This Supplementary Information accompanies the manuscript deposited at Preprints.org as version 1: \url{https://doi.org/10.20944/preprints202611.0852.v1}."

The first draft used a full sentence and a dedicated SI subsection heading; both pushed a two-line bibliography tail onto an extra page (40/32). The DOI is therefore carried as a clause, preserving the C19 pagination exactly (39/31).

## Verification

- Extracted-text diff against C19: one added line in the main, two in the SI, plus whitespace-only reflow lines; nothing removed or reworded.
- Rendered-page comparison at 72 dpi against C19: 39 pages and 31 pages, with exactly **one** differing page in each document (main p. 35, SI p. 31) — the pages carrying the addition.
- DOI string present once in each PDF's extracted text.
- Rebuild from the published source ZIP reproduces the same text, the same page counts and zero warnings.

## Note on DOI status

The DOI handle did not resolve on 31 October 2026 (doi.org 404 / Crossref 404), which is expected while a Preprints.org deposit is pending posting. It is cited as the author-directed deposit identifier. Re-check with `curl -sS https://doi.org/api/handles/10.20944/preprints202611.0852.v1`; a registered handle returns `"responseCode":1`.

## Provenance

`ecomod_C20_A01_main.tex` and `ecomod_C20_A01_SI.tex` are byte-identical to their C19 counterparts except for the insertions above (verified by diff). Figures, table fragments and `DATA_LICENSE` are byte-identical to C19. The GitHub data-availability link still points to the published C19 package, which remains the location of the executable numerical pipeline.

## (ii) Frontmatter layout fix and six keywords

- The keyword list was reduced from eight to six for the journal limit: "critical slowing down" and "carrying capacity" removed (both now secondary or negative results). Kept: biocapacity; ecological footprint; land-use conversion; aggregation; identifiability; delay differential equations.
- The keyword block had straddled pages 1-2 since C19, a typesetting fault rather than a content problem. Fixed in the layout only: `\begin{abstract}` now carries `\setlength{\baselineskip}{14pt}`, giving the abstract looser leading at unchanged font size.
- **No content was edited.** The abstract remains 217 words and its extracted text is identical to the previous build (verified). No sentence, number or citation was touched.
- Result: keywords entirely on page 1, no text overlap, zero LaTeX warnings, main text **38 pages**. The one-page reduction comes from the title page closing cleanly.
- Rejected variants, for the record: `\small` on the abstract, a compact keyword block, and negative vertical spacing. The first two also gave 38 pages but changed font size; the negative-spacing variants either pushed the title onto a duplicate page or overlapped the abstract heading. The leading change was the only fix that altered neither content nor typeface.

## (iii) Reproduction-package DOI

- The Data availability paragraph now reads: "Deposited at \url{https://doi.org/10.20944/preprints202611.0852.v1}; the reproduction package is archived at \url{https://doi.org/10.5281/zenodo.24092131}."
- Zenodo record verified before citing: 10.5281/zenodo.24092131 resolves, is typed **Dataset**, and its single file is `ECOMOD_C20_A01_reproduction_package.zip` at 6,021,179 bytes — byte-size identical to the package built here.
- The added clause initially pushed a two-line reference tail onto a 39th page. Fixed in the layout, not the text: `\enlargethispage{3\baselineskip}` on the references page. Main text returns to **38 pages**, the reference list ends complete on p. 38, keywords remain entirely on p. 1, and warnings remain zero.

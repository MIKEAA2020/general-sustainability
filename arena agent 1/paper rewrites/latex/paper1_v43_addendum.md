# v43 — Environmental Modeling & Assessment restructure

## Changes (per the journal's technical requirements)

1. **List of abbreviations** (new section, after Conclusions, before the
   appendices): CES (constant elasticity of substitution), MSY (maximum
   sustainable yield), PROMETHEE (Preference Ranking Organisation Method for
   Enrichment Evaluation) — the abbreviations used in the text. SEEA appears
   only inside a reference title and is not listed.
2. **Declarations** (end matter) rebuilt with the seven required entries:
   Ethics approval and consent to participate (not applicable); Consent for
   publication (not applicable); Availability of data and materials; Competing
   interests ("The authors declare that they have no competing interests.");
   Funding (not applicable); Authors' contributions ("A.A. conceptualized the
   entire work, wrote, edited and reviewed the manuscript."); Acknowledgements
   (not applicable). The brief AI declaration is retained as the final entry.
3. **Availability of data and materials** now cites the figshare deposit
   (verification artifact, figure code, figure files, novelty-search strings):
   https://doi.org/10.6084/m9.figshare.33764023 — replacing v42's pointer to
   the Zenodo record 22545740, which hosts the superseded preprint PDF, not
   the code. A matching DataCite-style data citation was added to the
   reference list (after the "Typed flux ledgers" entry, alphabetical).

No other content was modified; v42 is untouched.

## QA

- Compile: exit 0 (tectonic; elsarticle review mode).
- Render: 54 pages, 3 images, 0 `??`.
- All Declarations entries, the List of abbreviations, the figshare DOI, and
  the data citation verified present in the rendered PDF; ordering
  List of abbreviations → References → Declarations verified.
- `zenodo.org/records/22545740` no longer appears anywhere in the document.
- Warning profile identical to v42 (no regressions): one pre-existing 2.43 pt
  overfull at `\end{frontmatter}` and one pre-existing 9.07 pt overfull on the
  FP_agg display in Appendix B (v42 lines 67/1221; v43 lines 67/1229).

# F14_A01 — Implemented main/SI division of labour

**Ecological assets behind improving accounts: national forest evidence and biomass-change identifiability**  
Amin Abaee · ORCID https://orcid.org/0000-0002-0019-1842

## Read the paper

- **`integrated_F14_A01_main.pdf` — 15 pages, six figures, two tables, five Results subsections.** The main text contains the complete argument, principal national and local findings, uncertainty qualifications and conclusions.
- **`integrated_F14_A01_SI.pdf` — 22 pages, two figures and 17 tables.** Protocols, exact supporting values, sensitivity results, source definitions, proofs and verification. Every figure/table is explicitly cited in the main text.
- **`national_results_F14_A01.xlsx` — 31 sheets.** All 30 F13 sheets retained unchanged in value; one reader-navigation sheet added.
- `REVISION_AND_MIGRATION_ACCOUNT_F14_A01.md` — where each F12/F13 item went, what was compressed, and what was removed from the typeset narrative without deleting source evidence.

This is an editorial implementation, **not a new national AGB analysis**. The eight original calibrated national 2015–2023 forest-AGB analyses, Australia/Cameroon physical numerical modules, and independent conversion-association/reporting-accuracy evaluations remain unfinished. A completed calibrated comparison may include zero: incomplete analysis and unresolved sign are not equated.

## The implemented main figures

1. Eight-country account composition, replotted from the complete original F12 candidate changes. Legend moved outside the plotting area; full country names used.
2. The matched Brazilian endpoint forest-fraction maps, preserving the original numerical figure.
3. Coherent joint sign ambiguity, preserving the original figure.
4. Aggregation, information-width and density-contrast analysis, preserving the original three-panel figure.
5. All seven unique mapped endpoint-cohort ranges, replotted from F12 in separate Brazil/Indonesia panels, with numerical annotations and distinct scales.
6. Three separate inventory panels: Finnish uncertainty-assumption sensitivity, French longest contrast, Canadian earlier-domain annualized change. Different periods, quantities, units and interval meanings are explicitly labelled; no pooling or unsupported Canadian 95% label.

Main Table 1 retains every candidate with exact account percentages and typed physical results/periods/qualifications. Main Table 2 retains the local conditional allocation ranges. Full account sensitivities are SI Table S2; Indonesia source/definition sensitivity is SI Figure S2; exact cohort ranges are SI Table S13.

## Rebuild and verify

Python 3.13; observed versions are in `requirements_F14_A01.txt`. TeX Live with `latexmk`, Latin Modern and the listed LaTeX packages is required.

```bash
python -m pip install -r requirements_F14_A01.txt
python src/build_assets_F14.py
python src/build_F14.py
python src/reproduce_editorial_F14.py
# Rebuild PDFs and QA after any assembly/asset regeneration.
python src/build_F14.py
python src/qa_F14.py
# Inspect every rendered contact sheet before setting this flag.
python src/qa_F14.py --confirm-visual-review
python src/verify_package_F14.py
```

Verify the untouched frozen deposit first; rebuild in a working copy. The publisher is one-shot and must not be rerun after publication. Workspace long folder names and canonical `F11_A01`, `F12_A01`, `F13_A01`, `F14_A01` sibling layouts are supported. Prior packages are read-only numerical dependencies, not separate proposed submissions:

- F11 local identification: package commit `ce9a36f1bc17a84c3fd0994500766e1df72f3ae8`.
- F12 national analyses/certificates: package commit `3e3606157cf11d2c5c8b7d0cf08bd379663718da`.
- F13 new country/source analyses: package commit `809829f6c946f9078a0270e2a3474b8e88b1eb19`; receipt `e3b33bf1c7a18a37d61c68c0caa6c86d62520e7a`.
- All are under `batch 9/agent 2/ecomod_empirical_followup/` in https://github.com/MIKEAA2020/general-sustainability .

The new code repeats **nine editorial/plot artifacts byte-identically** in normal/optimized Python with hash seeds 17/73; **20 tests per mode** pass. It does not describe those repetitions as new empirical estimates or new optimization runs. Original F12 and F13 numerical provenance and witness checks remain immutable dependencies. All **537** durable F11–F13 files are protected by individual SHA-256 checks.

Minimal typesetting inputs and four frozen F13 assembly inputs are included, not whole prior deposits. Selected derived CSVs and one existing numerical inference JSON are copied byte-identically for independent reconstruction of the revised plots and tables. `metadata/input_lineage_F14.json` records exact identities. The workbook inheritance check compares **60,314 cells** across 30 sheets, including blanks.

`build_F14.py` compiles SI first and reads its actual LaTeX labels. Generated cross-document numbers are checked against every main-text SI citation before compiling main. No SI figure/table is uncited or guessed by hand. `qa_F14.py` checks PDF text bounds, font embedding (including Type3 glyph streams), ORCID, exact AI declaration, key results, source structure and workbook identity. Visual confirmation is recorded separately from programmatic rendering.

## Attribution and source rights

Account-derived tables and figures retain **CC BY-SA 4.0** and attribution to Lo et al. (2026)/Footprint Data Foundation. MapBiomas source-specific classes, collections and limitations remain explicit. IGN, Canada's NFI, Luke and original inventory publications are credited in the main/SI and immutable source registries. Existing original local figures retain their earlier documented terms; boundary-derived data retain source-specific licensing and OSM attribution. No blanket licence overrides provider terms.

No provider PDF body, raw raster, raw workbook, DBF, archive, native density array or private credential is redistributed. Source-derived numerical figures are not provider PDF bodies. Unrelated C17 and companion manuscripts remain unchanged.

Arena.ai Agent Mode was used to assist with computational methods and literature review.

# F15_A01 — Restored editorial coverage and access audit

**Ecological assets behind improving accounts: national forest evidence and biomass-change identifiability**  
Amin Abaee · ORCID https://orcid.org/0000-0002-0019-1842

## Read the paper

- **`integrated_F15_A01_main.pdf` — 16 pages, six figures, two tables, five Results subsections.** The main is self-contained: national accounts/maps, local support and coherent sign ambiguity, information increments, endpoint cohorts, inventory evidence, uncertainty and conclusions.
- **`integrated_F15_A01_SI.pdf` — 25 pages, two figures and 25 tables.** Every SI figure/table is explicitly cited from a relevant main-text location. The SI provides verification and specialist depth, not a second Results/Discussion or future-work paper.
- **`national_results_F15_A01.xlsx` — 31 sheets.** All 30 inherited sheets and 60,314 cells are unchanged in value; one reader-navigation sheet is retained.
- **`CONTENT_COVERAGE_AUDIT_F15_A01.md`** — claim-by-claim placement, the F14 losses restored here, deliberate specialist compression and automated guards.
- **`ACCESS_AND_EVIDENCE_WORKAROUNDS_F15_A01.md`** — verified download routes, manual-fetch candidates, provider-request targets and the distinction between access and calibration.
- **`REVISION_AND_MIGRATION_ACCOUNT_F15_A01.md`** — additive revision history and exact migration/omission account.

F15 is an **editorial restoration**, not a new national AGB analysis. The eight original calibrated national 2015–2023 forest-AGB analyses, Australia/Cameroon physical numerical modules, current map-reference calibration and independent conversion-association/reporting-accuracy evaluations remain unfinished. A completed calibrated comparison may include zero; incomplete analysis and unresolved sign are not equated.

## What F15 restores

The main now retains the Indonesian class-level sign reversal and collection/support distinction, direct oil-palm event total, Brazilian and Indonesian subnational compensation, account-composition mechanisms and the Finnish bias threshold. The SI adds exact tables for:

1. 2010–2020 account-domain sensitivity;
2. 2015–2022 account-domain sensitivity;
3. all five primary account-component contributions;
4. all three forest-account area-by-factor decompositions;
5. exact Indonesian class and collection/support changes;
6. annual mapped transition-event totals;
7. Brazilian/Indonesian regional compensation;
8. the Finnish 2022–2023 stock–flow ledger.

It also repairs the extent–density and cancellation definitions and makes the Finnish second-moment construction explicit. Seven additional original F12 CSVs are vendored byte-identically to generate these tables; no result is re-estimated.

## Main figures and tables

1. Eight-country account composition, with external legend and full country names.
2. Original matched Brazilian endpoint forest-fraction maps.
3. Original coherent joint identification set.
4. Original aggregation, information-width and density-contrast panels.
5. All seven endpoint-cohort ranges, with separate Brazil/Indonesia scales and labels.
6. Finland/France/Canada inventory panels with distinct periods, units and interval meanings.

Main Table 1 types every country's account and physical evidence, actual periods and qualifications. Main Table 2 retains the local conditional allocation sets. The additional numerical detail is in the linked SI rather than crowding the main.

## Reproduce, build and verify

Python 3.13; observed package pins are in `requirements_F15_A01.txt`. TeX Live with `latexmk`, Latin Modern and the listed LaTeX packages is required.

```bash
python -m pip install -r requirements_F15_A01.txt
python src/build_assets_F15.py
python src/build_F15.py
python src/reproduce_editorial_F15.py
# Rebuild PDFs and QA after any assembly/asset regeneration.
python src/build_F15.py
python src/qa_F15.py
# Inspect every rendered contact sheet before setting this flag.
python src/qa_F15.py --confirm-visual-review
python src/verify_package_F15.py
```

Verify the frozen deposit first; rebuild in a working copy. Long folder names and canonical `F11_A01` through `F15_A01` sibling layouts are supported. The publisher is one-shot and must not be rerun after publication.

The independent editorial repetition compares **nine source-generated artifacts byte-for-byte** under normal/optimized Python with hash seeds 17/73; **28 tests per mode** pass. These checks do not constitute new empirical estimates or new LP runs. The original F12/F13 numerical pipelines and certificates remain immutable dependencies. All **597 durable F11–F14 files** are protected by individual SHA-256 checks, and the F14 verifier is invoked as part of F15 verification.

`build_F15.py` compiles SI first and reads actual LaTeX labels, then rejects any uncited or unknown SI reference before compiling main. `qa_F15.py` checks PDF text bounds, embedded fonts, ORCID, exact AI declaration, key results, structure and workbook identity. Visual review is separately recorded for every page.

## Prior verified deposits

Under `batch 9/agent 2/ecomod_empirical_followup/` in https://github.com/MIKEAA2020/general-sustainability:

- F11 package `ce9a36f1bc17a84c3fd0994500766e1df72f3ae8`;
- F12 package `3e3606157cf11d2c5c8b7d0cf08bd379663718da`;
- F13 package `809829f6c946f9078a0270e2a3474b8e88b1eb19`, receipt `e3b33bf1c7a18a37d61c68c0caa6c86d62520e7a`;
- F14 package `cd6c3757d4aeeca874c950acb8df2b7f0bc2e45f`, receipt `84a70030c5e5139b5b85c5c8516ce5930fc31072`.

No earlier publisher is rerun. No prior file, figure, workbook, source registry or receipt is overwritten.

## Attribution and source rights

Account-derived tables and figures retain **CC BY-SA 4.0** and attribution to Lo et al. (2026)/Footprint Data Foundation. MapBiomas source-specific classes, collections and limitations remain explicit. IGN, Canada's NFI, Luke and original inventory publications are credited. Existing local figures retain their documented terms; boundary-derived data retain source-specific licensing and OSM attribution.

No provider PDF body, raw raster, raw workbook, DBF, archive, native density array or private credential is redistributed. Newly identified public sources in the access audit are linked with factual retrieval metadata, not copied into the package. Unrelated C17 and companion manuscripts remain unchanged.

Arena.ai Agent Mode was used to assist with computational methods and literature review.

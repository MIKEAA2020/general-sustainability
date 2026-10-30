# F16_A01 — additive Cameroon and Australia physical modules

F16 preserves published F15 and adds reproducible, source-pinned reported forest-area/CO₂e modules for Cameroon and Australia. It does **not** claim completion of either country's calibrated national 2015–2023 forest-AGB comparison.

## Deliverables

- `integrated_F16_A01_main.tex` / `.pdf`: self-contained 18-page manuscript, seven figures and two tables.
- `integrated_F16_A01_SI.tex` / `.pdf`: 27-page SI with two figures and 28 tables; every SI figure/table is cited in main.
- `national_results_F16_A01.xlsx`: 41 sheets. All 60,336 cells in the 31 inherited F15 sheets are unchanged in value; ten F16 sheets are added.
- `data/*F16*`: annual source extractions and the machine-readable module summary.
- `metadata/source_provenance_F16.json`: URLs, source hashes, exact table/page use and the selective CRT-range audit.
- `src/`: extraction, plotting, workbook, assembly, compilation, testing, QA and verification code.

## New empirical results

**Cameroon, reported 2000–2020 series.** Table 9 reports total forest area of 31,332,386 ha in 2015 and 31,183,654 ha in 2020: −148,732 ha (−0.4746909476%). Dense humid and dry forest decrease by 88,916 and 59,817 ha; the other three classes are unchanged. Five annual class sums exceed the reported total by 1 ha, including 2015; reported totals are not altered to force closure. Tables 31/37 report net forest CO₂e flux of −113,383,116.17 tCO₂e/yr in 2015 and −109,599,895.35 in 2020, a +3,783,220.82 tCO₂e/yr difference and 3.3367% smaller net-sink magnitude. Provider Monte-Carlo relative uncertainty is 31.10% and 32.14%. These fluxes are not forest-AGB stock changes, and the public table does not provide a 2023 annual endpoint.

**Australia, separate source lineages.** ABARES-adjusted forest area rises from 132.51 Mha in 2015 to 133.57 Mha in 2021: +1.06 Mha (+0.7999396%). The separate NIR2021 transition stock rises from 132.98 to 134.03 Mha; its 2021 gross loss/gain/reported net values are −216/+487/+270 kha. NIR2023 forest land rises from 135,318 kha in 2014–15 to 136,862 kha in 2020–21 and 137,372 kha in 2021–22: +2,054 kha (+1.5179060%) through 2021–22. The 2022–23 row repeats 2021–22 under a documented carry-forward and is not an independent annual observation. NIR2023 2021–22 primary conversion, re-clearing, identified regrowth and net clearing are 21.6, 164.5, 436.7 and −250.6 kha. Forests of Australia (2023) contains exactly 133,564,800 forest ha in its 687-row attribute table, but its latest-information currency is 30 June 2021, not 2023.

No source lineage is spliced with another. Area, annual CO₂e flux, land-transition gains/losses and AGB remain different estimands. Their differences are not confidence intervals or reporting-error estimates.

## Reproduction

The derived CSV/JSON files are included, so manuscript reproduction does not require the provider PDFs. Install `requirements_F16_A01.txt` and Tectonic 0.17+ (or latexmk), then run:

```bash
python src/reproduce_F16.py
python src/test_F16.py
python -O src/test_F16.py
```

`reproduce_F16.py` rebuilds the figure/workbook and both PDFs from the frozen F15 inputs and deposited derived data. The optional source-extraction step is:

```bash
python src/extract_national_modules_F16.py
```

It expects the official sources in `../.cache/F16_sources/`; URLs and hashes are in `metadata/source_provenance_F16.json`. Do not redistribute the cached provider PDFs or CRT archive. Run `python src/qa_F16.py --confirm-visual-review` only after inspecting every rendered page. `python src/verify_package_F16.py --write-manifest` freezes the verified package; verification without that flag performs no rebuild.

## Inference boundary

All eight primary calibrated national 2015–2023 forest-AGB analyses remain incomplete. The new modules elevate the reported physical evidence on its actual periods; they do not calibrate AGB change, establish ecological composition masking, estimate conversion associations or certify reporting accuracy. Provider-held inputs needed for stronger reproduction/uncertainty designs are listed in `ACCESS_AND_EVIDENCE_WORKAROUNDS_F16_A01.md`.

# F12_A01 — actual national empirical extension

This is an additive empirical extension, not a replacement of F11 and not a completed calibrated national biomass study. The main deliverable is **national_empirical_extension_F12_A01.pdf**; its editable text is the adjacent Markdown file. **national_results_F12_A01.xlsx** contains readable numeric tables, source links and explicit quantity/status definitions.

## Executed in dependency order

1. **Freeze inputs and operands.** Preserve all eight inherited candidates, inherited eligibility and original primary 2015–2023 AGB target. Source selection is exploratory and feasibility-led, not outcome-naive or preregistered.
2. **Actual accounts.** Compute annual 2015–2023 accounts for all 183 eligible identifiers, endpoint/domain/component/per-person changes, symmetric forest-account decomposition, inherited 2010–2020 secondary window (182 comparable; SSD missing/disallowed in 2010), and separate 2015–2022 sensitivity.
3. **Complete national classifications.** Acquire and analyze official Brazil C11 and Indonesia C4.1 coverage and annual transition workbooks. Check leaf classes, geographic partitions, every adjacent transition margin and mapped stock-flow balance. Analyze Indonesia C3 as a collection-and-reported-support sensitivity, not a pure version effect.
4. **Reference/design investigation.** Read current C11 and C4.1 technical documentation and stream the complete old public Brazilian point archive. Quantify actual endpoint-label completeness and source/design mismatches; do not equate nonblank labels with usable representative truth.
5. **Finnish inventory inference.** Recover archived official API tables, including Åland, and original marginal volume SE tables. Compute an approximate 95% Bonferroni cycle-volume change interval without cross-cycle independence; separately report moment/bias sensitivities and forest-account reconciliation.
6. **Unique endpoint-conversion bounds.** Solve 634 marked-flow LPs on actual annual class-transition capacities; restrict paths to finest reported geographic units. Deposit compressed capacities and all primal/dual witnesses. Independently audit witnesses without solving again. These are conditional mapped-conversion bounds, not ecological validation or causal inference.
7. **Reproduce, test, report and publish.** All 50 numeric artifacts are byte-identical in normal/optimized Python under different hash seeds; 40 tests pass in each mode. Publication verification is documented separately.

## Main findings

- Total biocapacity: **91 increasing, 92 decreasing** identifiers. Of the increasing totals, **68** have declining forest *account components*, not demonstrated physical forest losses.
- **Brazil:** total account −1.2076%; mapped formations −10.863 million ha (−2.6365%). Not an increasing-total masking example.
- **Indonesia:** total account +5.4556%; combined C4.1 mapped forest −702,562 ha (−0.6563%). Forest Formation alone is approximately unchanged/slightly increasing; most combined net decline is in the peat-swamp class. C3 reports −3.106 million ha, but its reported footprint differs.
- **Indonesia endpoint cohort:** conditional mapped 2015 forest → 2023 oil-palm area about **0.112–2.326 million ha** with provincial constraints. It is not the sum of annual direct transition events and is not a confidence interval.
- **Finland:** NFI13 minus NFI12 growing-stock volume **+76.772 million m³**; approximate 95% Bonferroni interval **+17.3 to +136.3 million m³**, conditional on marginal-normal sampling inference and no unbounded differential bias. The moment-only sensitivity is unresolved. Inventory windows are not exact primary endpoints; volume is not AGB.

## Important unfinished work

All eight original calibrated national 2015–2023 AGB admissions remain held. This does **not** mean the new national map or secondary inventory modules have no usable results. Original national AGB aggregation, cross-account/physical support equivalence and reference-error calibration are incomplete. Independent conversion associations and reporting-accuracy evaluation are not executed. Five candidates have no completed physical national analysis in this increment; this is unfinished work, not demonstrated irreparability. See COMPLETION_AND_REMAINING_WORK_F12_A01.md and data/national_evidence_status_all_eight_F12.csv.

## Reproduction

Python 3.11+; dependencies in requirements_F12.txt. Supply the exact NEFBA 2026 workbook, SHA-256 `26e4f5c78d9fe20cb5cd51c073815157566711b53278a1f9118d7726ab60ad1b`. The current workspace copy is under `ecomod_audit_remediation_C18_A01/repository_sources/ecomod_audit/reference/NEFBA_2026.xlsx`.

From any working directory:

```bash
python src/reproduce_F12.py --account-workbook /path/to/NEFBA_2026.xlsx --download
python -m unittest discover -s tests -v
python -O -m unittest discover -s tests -v
python src/build_deliverables_F12.py
python src/qa_deliverables_F12.py
```

`--download` retrieves SHA-pinned official source bodies to the sibling excluded `.cache/F12/raw/` directory. Omit it when those caches are already present. No global native-resolution raster download occurs. All files remain within the inherited 25 MB per-source acquisition cap. Luke JSON-stat responses and exact POST queries are deposited; numerical reruns use those responses offline. To refresh the live statistical API intentionally, run `src/finland_inventory_F12.py` without `--offline`; changed returned data cause an amendment-required stop.

The reproducibility check runs normal and optimized Python, with different hash seeds and a one-thread numerical environment, and verifies source-script hashes. Scientific `require` guards are not removed by `python -O`. Provider PDFs/workbooks are not redistributed; source URLs, byte sizes and hashes are in metadata/source_registry_F12.json. The compressed capacities are **derived numerical tables**, not provider raster arrays. The NPZ witness archive is read with `allow_pickle=False` and is independently audited by src/audit_transition_witnesses_F12.py.

No F11, C17, C18 or earlier file is overwritten or deleted. Protected local F11 identities are recorded in metadata/protected_F11_identity_F12.json, and additive publication verifies every pre-existing remote leaf path.

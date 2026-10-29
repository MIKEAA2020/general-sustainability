# F11 A01 — matched-support biomass identification elevation

**Active article:** `followup_F11_A01_main.pdf` and `followup_F11_A01_SI.pdf`.

This is an additive scientific revision of F10, not a merge of the audit branch and not a replacement of F10 or C17. The complete 218-file F10 package is preserved byte-for-byte under `inherited_F10/`, with pinned Git identities in `metadata/inherited_F10_identity_F11.json`. Historical README files and historical claims in that directory are not the active F11 entry point.

## New substantive work

1. Actual area-weighted differences from freshly reacquired, hash-guarded Brazilian 2015/2023 native AGB: positive and negative local differences, net and cancellation on the same full footprint.
2. Nine nested observation-information scales, retaining every case and the fine mapped geometry, to quantify the effect of aggregation on cancellation and sharp allocation-set width.
3. Constructive allocations attaining both group-change signs while preserving every native-cell total and mapped support.
4. A **sharp coherent joint set** for formations and formations plus savanna, respecting their nested relation through a three-component partition. All four strict sign quadrants have reconstructed feasible allocations.
5. A separately labelled, uncalibrated density-contrast sensitivity family with exact sharp bounds and sign-identification boundaries. No finite density contrast is adopted for the primary result.
6. Explicit coverage CSV link and a 16-row SI table, plus unrounded-difference reporting notes in both articles.

**Limits:** point-map differences are not validated ecological change. The eight national physical-analysis holds remain. No national stock trend, account–asset divergence, conversion association, change confidence interval or reporting-rule accuracy is supplied. See `AUDIT_RESOLUTION_AND_ELEVATION_F11_A01.md` for the open high-priority ecological inference gap, and `REVISION_AND_DELETION_ACCOUNT_F11_A01.md` for the exact framing changes. The original four ecological questions are preserved verbatim as prospective comparisons in the SI, not represented as answered.

## Reproduction

Python dependencies:

```bash
python -m pip install -r requirements_F11.txt
```

A TeX installation containing `pdflatex`, `latexmk`, AMS/natbib/hyperref, xurl, needspace and standard fonts is needed for the documents. On Debian, the tested installation used `texlive-latex-extra texlive-publishers lmodern latexmk poppler-utils`.

Verify the deposited bytes **before** rerunning commands that update logs or PDFs:

```bash
python src/verify_package_F11.py
```

Reacquire only the two bounded, exact-identity native queries, then compute and render:

```bash
python src/identification_F11.py
python src/joint_identification_F11.py --offline
python src/render_results_F11.py
python src/check_numerical_reproducibility_F11.py --offline
python -m unittest discover -s tests -v
python -O -m unittest discover -s tests -v
bash src/build_F11.sh
python src/qa_documents_F11.py
```

Native response sizes and SHA-256 hashes are pinned by the unchanged F10 source registry. Responses are capped at their expected sizes and rejected on identity drift. Native arrays and range caches live only under `.cache/` and are not deposited. `--offline` requires an already verified cache. Changed source bytes require an explicit amendment, not silent substitution.

For the complete F10 comparison suite, the unchanged historical tests require protected F08/F09 comparison packages. This helper restores them from immutable commit `37b520805cd94be875a6d045c2806c9463eae4d5`, stages F10 in scratch, runs all 134 tests without skips in both modes, rebuilds both F10 documents, and optionally reruns guarded F05/F07 source derivations:

```bash
# Set GITHUB_TOKEN privately, or pass --token-file /private/path.
python src/reproduce_inherited_F11.py --source-rerun
```

Alternatively, `--comparator-root /path/to/parent` accepts an existing parent containing `ecomod_followup_F08` and `ecomod_followup_F09`. That route and the authenticated one-file restoration route were both exercised. No credentials are stored or printed. All historical reproduction occurs in `.cache/legacy_reproduction_F11/`, leaving durable inherited files unchanged.

## Verification results

- **134 inherited + 58 new = 192 tests pass in each Python mode**, without skips in the full inherited comparison run.
- Eleven F05/F07 derived files from guarded native/land-cover source reruns are **byte-identical** to inherited inputs.
- Freshly recomputed native SD diagnostics reproduce every numeric field of the two inherited R03 rows.
- Thirteen numerical CSV/metadata files agree byte-for-byte across normal and optimized analysis executions.
- Main and SI rebuilt; final document QA records page counts, SHA-256 identities, reference checks and warning status.
- Complete native/reference/document acquisition is **not** claimed. Reference-eligibility and provider-document assessments are carried forward; two native biomass queries and the bounded local MapBiomas ranges were reprocessed in this task.

PDF bytes may vary after reproduction because of timestamps and software versions. Numerical determinism checks do not assert cross-environment PDF byte identity. `evidence/environment_F11.txt` records the tested environment; version ranges in the requirements are not a lockfile.

## Data, provenance and preservation

The analysis specification is `ANALYSIS_SPECIFICATION_F11_A01.md`; this is an exploratory specification, not preregistration. New results are in `data/` and `results/`; source and review identities, numerical QA and preservation records are in `metadata/`. Final-run logs are in `evidence/`. An initial development traceback is retained and is superseded by the explicitly named final-run logs, not represented as a successful run.

Source attribution and licensing are retained in the main/SI and inherited package. NEFBA-derived tables remain CC BY-SA 4.0; boundary-derived data retain their separate terms; MapBiomas-derived summaries retain provider attribution; the limited AGBref-derived subset retains its CC BY 4.0 attribution. No new full provider document, reference archive, land-cover raster or native-density array is redistributed.

Publication is additive under `batch 9/agent 2/ecomod_empirical_followup/F11_A01/`. The publication utility requires an explicit `--publish` flag, refuses an existing target prefix, checks every previous remote leaf path, uses non-force updates and downloads package blobs for byte comparison. It never deletes local or remote files. Do not rerun a completed publisher; inspect its receipt.

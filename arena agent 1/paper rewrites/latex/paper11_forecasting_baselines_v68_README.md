# Paper11 v68 — source, verification, and build record

**Edition basis (2026-10-17).** A fresh GitHub API audit covered all six branches, both tags, and both releases in `MIKEAA2020/general-sustainability`. The latest relevant editions before this work were Paper11 v67 and P11c v5; no v68/v6 existed on any checked ref before this edition was assigned. The canonical Paper11 v67 and P11c v5 files are preserved. Paper11 v67 is in `arena agent 1/paper rewrites/latex/` on `main`; the parallel v67/v5 copies on `e2-v3-source-year` are in `arena agent 1/agent workspace/papers/`. The local v67 main text, SI, and verifier match the canonical `main` files byte-for-byte. The version-currency and split/prior-art notes were checked on `e2-v3-source-year`; they record the three-way split of the older concatenated manuscript. The local P11c v6 draft was not treated as a substantive new edition; v5 remains the edition of record.

## Source bundle and assembly

The versioned source bundle is `paper11_forecasting_baselines_v68_src/`:

- `parts/00_front.tex`–`parts/07_back.tex`: main-text fragments.
- `si_parts/si_00_front.tex`–`si_05_s23_s24.tex` and `si_parts/gen/`: Supplementary Information fragments and generated table bodies.
- `work/cod/`: deterministic simulation runner, four batch archives and manifests, hash-checking aggregator, aggregate CSVs, plotting helper, and related analyses.
- `work/edw/`: Edwards-derived data and records carried forward from v67.
- `figs/`: figures used by the two documents, including the regenerated operating-characteristic figure.
- `assemble_si.py`: SI assembler.

From the repository root, reassemble and test the edition with:

```sh
SRC='arena agent 1/paper rewrites/latex/paper11_forecasting_baselines_v68_src'
cat "$SRC"/parts/0*.tex > paper11_forecasting_baselines_v68.tex
(cd "$SRC" && python3 assemble_si.py)
cp "$SRC"/paper11_forecasting_baselines_v68_supplementary.tex .
python3 -m py_compile paper11_forecasting_baselines_v68_verification.py \
  "$SRC"/work/cod/sim_retention_power_repro.py \
  "$SRC"/work/cod/aggregate_power_simulation_repro.py \
  "$SRC"/work/cod/plot_operating_characteristics.py
python3 paper11_forecasting_baselines_v68_verification.py
tectonic --keep-logs paper11_forecasting_baselines_v68.tex
tectonic --keep-logs paper11_forecasting_baselines_v68_supplementary.tex
```

The final assembled sources have balanced braces and environments, 118 labels and 97 references across the combined main/SI pair, and no missing references. The standard-library verifier passes **237/237 checks**; its recorded output is `paper11_forecasting_baselines_v68_verification_output.txt`.

## Completed cod operating-characteristic rerun

The v68 runner uses stable per-cell/per-replicate SHA-256 seeds, restartable replicate-ID ranges, PCG64, and within-origin reuse of identical M2/M3/M4 fits. Four disjoint batches (IDs 0–49, 50–99, 100–149, 150–199) cover 14 DGP/noise cells × 200 replicates = 2,800 seeded series and 14,000 module rows. All batch manifests and source/output hashes were checked; there were no failed or non-finite replicates. The aggregate manifest records the batch and canonical-output hashes. Python 3.13.16, NumPy 2.3.5, and pandas 2.2.3 were used for the recorded run.

Primary-rule retention rates (rate [95% Wilson interval], low/high process noise):

| DGP | Truth-matching retention for D1–D4; any-module retention for D5–D7 | σ = 11.8 kt | σ = 33.8 kt |
|---|---|---:|---:|
| D1 collapse | M1 true | 0.975 [0.943, 0.989] | 0.950 [0.910, 0.973] |
| D2 recovery | M1 true | 0.660 [0.592, 0.722] | 0.110 [0.074, 0.161] |
| D3 stock-flow | M2 true | 0.105 [0.070, 0.155] | 0.130 [0.090, 0.184] |
| D4 depensation | M1b true | 0.000 [0.000, 0.019] | 0.015 [0.005, 0.043] |
| D5 persistence null | any module | 0.025 [0.011, 0.057] | 0.075 [0.046, 0.120] |
| D6 drifting productivity | any module | 0.720 [0.654, 0.778] | 0.770 [0.707, 0.823] |
| D7 smooth path + observation error | any module | 0.970 [0.936, 0.986] | 0.950 [0.910, 0.973] |

The SI also reports D3/D4 any-module retention, to distinguish low truth-specific power from no selection: D3 105/200 and 122/200 (intervals [0.456, 0.593] and [0.541, 0.675]); D4 61/200 and 11/200 (intervals [0.245, 0.372] and [0.031, 0.096]). The persistence-only versus full-rule decomposition attributes 64% of D3 and 95% of D4 persistence-hurdle survivors to comparator attrition. The v68 Protocol C reference row reports mean power 0.368 and D5 specificity 0.950; other rule comparisons remain explicitly historical and unreproduced. These operating characteristics are conditional on the fixed DGPs and parameter settings, not a general guarantee.

To reproduce the four batches and aggregate, see the executable recipe in SI S13. `work/cod/aggregate_power_simulation_repro.py` validates disjoint complete coverage, manifests, hashes, row counts, seed uniqueness, and raw-to-summary consistency before writing canonical results. `work/cod/plot_operating_characteristics.py` reads that summary and rebuilds the cod operating-characteristic figure (Figure 5 in the manuscript) without hard-coded rates.

## Final TeX build and inspection

Both assembled documents were freshly compiled with Tectonic 0.15.0 after the latest fragment edits. The main PDF has 49 pages and the SI 36 pages (US Letter). Log scans found **no undefined references, undefined citations, or LaTeX errors**. PDF text/metadata checks confirmed the explicit main-to-SI Table S16 reference, SI-to-main Proposition 2 reference, the Table S16 values and D3/D4 intervals, and the embedded 237/237 verification record.

- Main PDF SHA-256: `ecda406aceaf731a96c2af59cbe97a512c5ee46bf4f619d8deffb4645e60a3a9`
- SI PDF SHA-256: `60a965874da24d84a8abafa048b7a97fa11ee9df0393e3513beca1c7b25b9097`
- Maximum remaining overfull box: 11.71 pt in the main text; 2.44 pt horizontal and 0.91 pt vertical in the SI. The earlier 36.90-pt SI code-block overfull was corrected before this final build.

The final PDFs are `paper11_forecasting_baselines_v68.pdf` and `paper11_forecasting_baselines_v68_supplementary.pdf`. Any pre-final PDF copies retained locally are clearly marked interim and are not part of the publication bundle.

## Preservation and release path

Paper11 v67 and P11c v5 remain unchanged. The finalized v68 bundle belongs on branch `main` under `arena agent 1/paper rewrites/latex/`, alongside a new `paper11_forecasting_baselines_v68_src/` source directory. No older edition, tag, release, or unrelated lineage is to be renamed or deleted as part of this update. P11c v6 is not asserted as a new edition.

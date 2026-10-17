# Paper11 v68 — changes from v67

**Edition basis (2026-10-17).** A fresh audit checked all six branches, both tags, and both releases in `MIKEAA2020/general-sustainability`, plus the version-currency and split/prior-art records on `e2-v3-source-year`. Paper11 v67 is the latest relevant combined manuscript before this revision; the canonical copy is on `main` at `arena agent 1/paper rewrites/latex/`. P11c v5 is preserved. No v68/v6 was present on a checked remote ref before numbering this edition. The local v67 main source, SI, and verifier match the canonical remote files. The separate local P11c v6 draft was not treated as a substantive edition.

## Scientific and claim-scope corrections

- The operating-characteristic section now reports the completed 200-replicate-per-cell v68 run, not the earlier 150-replicate interim aggregate. The narrative and cod operating-characteristic figure (Figure 5) distinguish truth-matching power for D1–D4 from any-module false retention for D5–D7. D3/D4 any-module retention is reported separately so low truth-specific power is not mistaken for no selection.
- The SI decomposition separates the persistence-only hurdle from the next-simpler-comparator clause. The displayed rates use four decimal places; the Protocol C comparison row is refreshed to mean power 0.368 and D5 specificity 0.950. Other rule comparisons and historical diagnostic correlations remain labelled carried-forward, not independently reproduced.
- The cod discussion keeps results conditional on the specified DGPs and parameter settings. It distinguishes the persistence-null result from the high false-retention rates under drifting productivity and smooth observation error; it does not turn the simulations into a general guarantee.
- The Edwards reporting keeps the H1/H2 score gate separate from M2m's broader function-class clause; the realized-future-flux calculation is a conditional diagnostic/hindcast, not a forecast or nowcast; the five-year result is scoped to the tested J-17 origins; and no prospective-registration or general policy-advice claim is made.
- Main and SI cross-document references are explicit: the main text names SI Table S16, and the SI names main-text Proposition 2. The SI reproducibility section distinguishes the preceding edition's archived forecast runners from the new v68 operating-characteristic rerun and provides a restartable batch/aggregation recipe.

## Completed simulation and archive

- The restartable runner derives stable seeds from SHA-256, uses PCG64, reuses identical M2/M3/M4 fit inputs within an origin, and fails rather than silently accepting missing or non-finite scores.
- Four disjoint replicate-ID batches (0–49, 50–99, 100–149, 150–199) cover all 14 DGP/noise cells. The archive contains 2,800 seeded series and 14,000 module rows; all batch manifests, source/output hashes, coverage, unique seeds, flags, and summary rates were checked. No replicate failed.
- Truth-specific primary-rule retention (low/high noise): D1 M1 0.975/0.950; D2 M1 0.660/0.110; D3 M2 0.105/0.130; D4 M1b 0.000/0.015. Any-module retention: D5 0.025/0.075; D6 0.720/0.770; D7 0.970/0.950. SI Table S16 gives cell-specific Wilson intervals and D3/D4 any-module intervals.
- The cod operating-characteristic figure (Figure 5 in the manuscript) and the current Protocol C row in the SI are regenerated from the validated aggregate. The full raw archive, batch manifests, seed records, aggregate summaries, and plotting/reproduction scripts are in `paper11_forecasting_baselines_v68_src/work/cod/`.

## Verification and build

- Both TeX documents were reassembled from their fragments. The combined-source check passes with 118 labels, 97 references, balanced braces/environments, and no missing references. Python syntax checks pass for the verifier and simulation/build scripts. The expanded verifier passes **237/237 checks**; the run is recorded in `paper11_forecasting_baselines_v68_verification_output.txt`.
- Fresh separate main and SI PDFs were built with Tectonic 0.15.0 and checked by log scan and PDF text/metadata inspection. There are no undefined references, undefined citations, or LaTeX errors. The main PDF is 49 pages; the SI is 36 pages.
- Final PDF SHA-256: main `ecda406aceaf731a96c2af59cbe97a512c5ee46bf4f619d8deffb4645e60a3a9`; SI `60a965874da24d84a8abafa048b7a97fa11ee9df0393e3513beca1c7b25b9097`. Remaining nonfatal overfull boxes are at most 11.71 pt in the main text and 2.44 pt horizontal / 0.91 pt vertical in the SI; the initially overlong SI command-list line was shortened before the final build.

## Preservation and target

Paper11 v67 and P11c v5 remain unchanged. The new Paper11 edition and its source bundle belong on `main` under `arena agent 1/paper rewrites/latex/`. No prior edition, tag, release, or unrelated lineage is renamed or deleted for this update. P11c v6 is not asserted or published as a new edition.

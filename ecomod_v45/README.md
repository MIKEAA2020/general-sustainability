# ECOMOD v45 working package

**Status:** uncommitted local working candidate, derived directly from published v44. V44 remains unchanged; this v45 candidate has not been committed, pushed, or published. The latest source-matched QA PDFs are in `output_v45_citation_framing_final_QA_20261025/` (35-page main; 20-page SI). The earlier `output_v45_citation_framing_SI_verified_20261025/` PDFs were overwritten during the follow-up and their pre-continuation copies were not preserved. Earlier readability and citation-audit snapshots remain comparison artifacts; the local checksum list is not a remote release manifest.

## Scientific and empirical scope

- Uses the official National Ecological Footprint and Biocapacity Accounts (NFA), Edition 2026, results and metadata v1.0. The primary world window is 1961–2023; the 1961–2022 sensitivity uses the same edition and population series. Estimated 2024–2025 rows are excluded.
- Reports NFA component changes as account-composition results in gha, not as physical-stock findings. The paper does not claim a measured decline in biomass, soil condition, wetlands, fish biomass, or the model state `A_c`.
- Separates the conditional model trajectory for `A_c`, `Upsilon(q)`, and `Upsilon(q) A_c` from NFA account movements. The reduced frozen-demand equilibrium branch can be unique while realized land allocation remains path-dependent when conversion is one-way and restoration is disabled.
- Keeps the physical-stock scoreboard as an unpopulated specification. No common-boundary global physical-stock inventory for the relevant components was assembled; no physical-stock composite or decline finding is presented. Heterogeneous stock/extent/condition measures are a nonadditive vector unless boundaries, normalization or valuation, and substitution rules are declared.
- Treats the exploratory crop proxy `X = b_hat_f A_f`, `C = B_NFA - X` as an accounting construction. It uses independently sourced OWID/FAOSTAT cropland-area and cereal-yield inputs; cereal yield is a sentinel, not an all-crops measure. `C` is not physical or ecological capital and is not identified with `Upsilon(q) A_c`. The spliced World Bank all-crops production-index series remains excluded because its base-period discontinuities make it unsuitable for this decomposition.
- The earlier restoration pass used P1 v59, P3 v32, and P4 v41 companion locators. The current citation/framing follow-up replaces those with the explicitly approved key mapping: `Abaee2026a` = Paper4/governance v41; `Abaee2026b` = Paper06/assessment v71; `Abaee2026c` = Paper3 pinned to the current repository commit, with the PDF v50 / README-checksum v49 / TeX-header v48 mismatch disclosed. Earlier locators remain historical, not current citations.

## Audit follow-up (2026-10-25)

- Promotes delayed-quality regeneration, `q(t-tau_g)`, to the canonical reported solver in `work/twoland_fixed.py`, matching the stated equation. The former current-quality solver is preserved at `work/twoland_fixed_current.py`; the duplicate delayed solver file is retained for reproducibility.
- Corrects the custom recovery-gate integrator to use delayed quality and fixes the current/delayed imports in the technology-wave scan. The old current-quality integrator is preserved as `work/recovery_metric_and_tau_p_scan_current_quality.py`.
- Regenerated the demonstration figure, drawdown CSV, technology-wave outputs, and recovery/gate summaries from the canonical model. `work/render_si_model_tables.py` now generates the SI drawdown and recovery tables from the CSV. The recovery table is corrected: the delayed-quality drawdown cases recover only partially (`R_c=0.21–0.89`). The pre-audit table snapshots are preserved under `_current_quality` filenames for provenance, but the prior recovery-table values did not match the drawdown CSV and are not endorsed as reproducible sensitivity results.
- Removed a duplicated Poorter citation construction and clarified that `B,E` are NFA account values, `Y_f,Y_c` are model-derived contributions, `S` is a model shortfall, and `D` is a model-internal time-integral—not NFA-reported items.
- The audit's `Poelau`, `Hurt/Hurtt`, and `E_cell` claims were not found; `Poeplau` is correctly spelled. The parameter paragraph and the §3.1 opening were not duplicated; the apparent page-10 fragment was a continuation. Zenodo record 22554480 lists a v1 record with v35 manuscript files, so no v42/v43 lineage claim is made.

The earlier restoration build remains a historical comparison. The latest fresh citation/framing and SI QA build is in `output_v45_citation_framing_final_QA_20261025/`; the checks cover the scoped Paper06 claim, commit-pinned Paper3 citation, matching titles, Table S4/S6 layout, main Table 2(a), and the final §S4.2 page break.

## Main files

- `parts/00_front.tex` — title, abstract, introduction, and revision history.
- `parts/01_methods.tex`, `parts/02_results.tex`, `parts/03_discussion.tex` — methods, model and empirical results, discussion, limitations, conclusions, and working data-availability note.
- `parts/si_00.tex`, `parts/si_01.tex`, `parts/si_02.tex` — SI front matter, numerical protocol, Edition 2026 empirical details, physical-stock scoreboard specification, policy extensions, and comparator.
- `parts/si_tab_drawdown.tex`, `parts/si_tab_recovery.tex` — generated SI model tables; current-quality backups have `_current_quality` suffixes.
- `parts/04_refs.tex`, `parts/si_refs.tex` — synchronized main/SI bibliographies.
- `data/NEFBA_2026.xlsx`, `data/empirical/` — official NFA workbook and independent OWID/FAOSTAT input snapshots.
- `data/nfa_2026_*.csv`, `data/nfa_2026_summary.json` — reproducible account extracts and calculations.
- `work/nfa_2026_recompute.py`, `work/nfa_2026_proxy_divisia.py` — NFA recomputation and exploratory proxy calculations.
- `work/twoland_fixed.py`, `work/twoland_fixed_current.py` — canonical delayed-quality solver and preserved current-quality sensitivity solver.
- `drawdown_depth.py`, `make_fig_model.py`, `work/render_si_model_tables.py` — regenerate drawdown data, Figure 1, and SI model tables.
- `work/tb_wave_debt_scan.py`, `work/recovery_metric_and_tau_p_scan.py`, `work/verify_tab_conv_basin.py` — controlled wave experiment and model validation.
- `fig2_nfa_aggregation_face.png`, `fig3_composition_attribution.png` — Edition 2026 NFA figures.
- `ECOMOD_VERSION_CURRENCY_v45.md`, `REVIEW_STATUS_v45.md`, `CHANGELOG_v44_to_v45.md` — version scan, audit review, and revision log.
- `output_v45_citation_framing_final_QA_20261025/` — fresh main/SI QA PDFs and TeX logs; not a release package.
- `SHA256SUMS_v45_working.txt` — local working checksums; not a remote publication manifest.

## Rebuild

From the repository root, regenerate the assembled sources and fresh QA PDFs with Python and Tectonic 0.17.0:

```sh
python assemble.py
mkdir -p output_v45_citation_framing_final_QA_20261025
tectonic --reruns 2 --outdir output_v45_citation_framing_final_QA_20261025 manuscript_working_main.tex
tectonic --reruns 2 --outdir output_v45_citation_framing_final_QA_20261025 manuscript_working_si.tex
```

The data/model regeneration scripts are listed above; rerun them if the underlying data or model changes. The QA output directory contains build outputs only; it is not a release package. A public v45 archive path and permanent release filenames remain undeclared pending an explicit release decision.

## Release status

The v44 package and PDFs remain intact. The latest local QA PDFs are in `output_v45_citation_framing_final_QA_20261025/`. No commit, push, or publication has occurred. The pre-follow-up PDFs formerly in `output_v45_citation_framing_SI_verified_20261025/` were overwritten and their exact prior bytes were not preserved. The local checksum list is not a remote publication manifest. Before any publication, insert an approved archive URL in the data-availability statement, obtain a separate release decision, create a release manifest, and byte-verify the approved remote destination. Historical PDFs must not be used as current outputs.


Local-only SI-verification bundle: `output_v45_citation_framing_SI_verified_20261025/` remains available; its staged SI text matches a fresh source rebuild, but it is not the original overwritten PDF binary or a public release.

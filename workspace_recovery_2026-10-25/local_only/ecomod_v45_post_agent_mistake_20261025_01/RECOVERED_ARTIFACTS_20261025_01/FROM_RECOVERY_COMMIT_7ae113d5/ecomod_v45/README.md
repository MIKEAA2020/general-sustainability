# ECOMOD v45 working package

**Status:** uncommitted working candidate, derived directly from published v44. V44 remains unchanged at its original repository path. This v45 candidate has not been pushed or published. The PDFs in `output_v45_release_candidate_final2/` are the pre-audit build and do **not** match the current source. The refreshed audit build is in `output_v45_audit_current/` (36-page main; 23-page SI) and has passed visual inspection. The local working checksum list is refreshed and verified; it is not a remote publication manifest.

## Scientific and empirical scope

- Uses the official National Ecological Footprint and Biocapacity Accounts (NFA), Edition 2026, results and metadata v1.0. The primary world window is 1961–2023; the 1961–2022 sensitivity uses the same edition and population series. Estimated 2024–2025 rows are excluded.
- Reports NFA component changes as account-composition results in gha, not as physical-stock findings. The paper does not claim a measured decline in biomass, soil condition, wetlands, fish biomass, or the model state `A_c`.
- Separates the conditional model trajectory for `A_c`, `Upsilon(q)`, and `Upsilon(q) A_c` from NFA account movements. The reduced frozen-demand equilibrium branch can be unique while realized land allocation remains path-dependent when conversion is one-way and restoration is disabled.
- Keeps the physical-stock scoreboard as an unpopulated specification. No common-boundary global physical-stock inventory for the relevant components was assembled; no physical-stock composite or decline finding is presented. Heterogeneous stock/extent/condition measures are a nonadditive vector unless boundaries, normalization or valuation, and substitution rules are declared.
- Treats the exploratory crop proxy `X = b_hat_f A_f`, `C = B_NFA - X` as an accounting construction. It uses independently sourced OWID/FAOSTAT cropland-area and cereal-yield inputs; cereal yield is a sentinel, not an all-crops measure. `C` is not physical or ecological capital and is not identified with `Upsilon(q) A_c`. The spliced World Bank all-crops production-index series remains excluded because its base-period discontinuities make it unsuitable for this decomposition.
- Updates companion references to version-specific GitHub permalinks for P1 v59, P3 v32, and P4 v41; earlier Zenodo deposits are identified as earlier versions, not as archives of the current manuscripts.

## Audit follow-up (2026-10-25)

- Promotes delayed-quality regeneration, `q(t-tau_g)`, to the canonical reported solver in `work/twoland_fixed.py`, matching the stated equation. The former current-quality solver is preserved at `work/twoland_fixed_current.py`; the duplicate delayed solver file is retained for reproducibility.
- Corrects the custom recovery-gate integrator to use delayed quality and fixes the current/delayed imports in the technology-wave scan. The old current-quality integrator is preserved as `work/recovery_metric_and_tau_p_scan_current_quality.py`.
- Regenerated the demonstration figure, drawdown CSV, technology-wave outputs, and recovery/gate summaries from the canonical model. `work/render_si_model_tables.py` now generates the SI drawdown and recovery tables from the CSV. The recovery table is corrected: the delayed-quality drawdown cases recover only partially (`R_c=0.21–0.89`). The pre-audit table snapshots are preserved under `_current_quality` filenames for provenance, but the prior recovery-table values did not match the drawdown CSV and are not endorsed as reproducible sensitivity results.
- Removed a duplicated Poorter citation construction and clarified that `B,E` are NFA account values, `Y_f,Y_c` are model-derived contributions, `S` is a model shortfall, and `D` is a model-internal time-integral—not NFA-reported items.
- The audit's `Poelau`, `Hurt/Hurtt`, and `E_cell` claims were not found; `Poeplau` is correctly spelled. The parameter paragraph and the §3.1 opening were not duplicated; the apparent page-10 fragment was a continuation. Zenodo record 22554480 lists a v1 record with v35 manuscript files, so no v42/v43 lineage claim is made.

The fresh build and visual inspection are complete in `output_v45_audit_current/`; the pre-audit PDFs remain unchanged and are not current outputs.

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
- `SHA256SUMS_v45_working.txt` — local working checksums; not a remote publication manifest.

## Rebuild

From this directory, with Python, the analysis packages, and TeX Live (`pdflatex`) installed:

```sh
python work/nfa_2026_recompute.py
python work/nfa_2026_proxy_divisia.py
python drawdown_depth.py
python work/render_si_model_tables.py
python make_fig_model.py
python work/verify_tab_conv_basin.py
python work/tb_wave_debt_scan.py
PYTHONPATH=work python -c 'from recovery_metric_and_tau_p_scan import s54; s54()'
python assemble.py
mkdir -p output_v45_audit_current
for i in 1 2 3; do
  pdflatex -interaction=nonstopmode -halt-on-error -output-directory=output_v45_audit_current manuscript_working_main.tex
done
for i in 1 2 3; do
  pdflatex -interaction=nonstopmode -halt-on-error -output-directory=output_v45_audit_current manuscript_working_si.tex
done
```

The pre-audit `output_v45_release_candidate_final2/` folder is retained unchanged for comparison; do not distribute it as representing the current source. A public v45 archive path and permanent release filenames are intentionally undeclared until checks and an explicit release decision are complete.

## Release status

The v44 package and PDFs remain intact. The current local audit PDFs and `SHA256SUMS_v45_working.txt` are verified; the pre-audit final2 PDFs are not current. No commit, push, publication, cleanup, or deletion has been performed for v45. Before any publication, insert the approved archive URL in the data-availability statement, create a release manifest, and byte-verify the approved remote destination after an explicit release decision. The previous final2 PDFs must not be used.

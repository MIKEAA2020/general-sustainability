# ECOMOD v43 → v44

**Edition date:** 2026-10-24<br>
**Base edition:** ECOMOD v43, preserved unchanged at its original package path<br>
**New package path:** `agent 2 productivity illusion/manuscript_ECOMOD_v44_src/` on `main`

## Why v44

A complete reachable-history scan (all fetched branches and tags; 1,636 commits; 97 unique ECOMOD-named paths) found v43 as the latest numbered ECOMOD edition and no v44 path. V44 therefore uses the available successor number without overwriting an earlier edition. See [`ECOMOD_VERSION_CURRENCY_v44.md`](ECOMOD_VERSION_CURRENCY_v44.md).

## Solver and numerical corrections

- Corrected the history origin in both `work/twoland_fixed.py` and `work/twoland_fixed_delayed.py`: the pre-run `B` history is initialized from the supplied initial state across the maximum active delay, and the time-zero sample is computed rather than inserted as zero. This removes an artificial dip in delayed carrying capacity when the delayed query reaches `t=0`.
- Propagated the optional logistic technology increment consistently through the fast-land yield, current `B`, the returned account series, and the delayed `B` history used by `K(t-\tau_p)`. The wave is off in the baseline and activated only in the controlled SI experiment.
- Made all state arrays explicitly floating point, so an integer `D0=0` cannot truncate accumulated debt. Added `t`, `E`, and `T_b` to solver outputs and updated the solver documentation.
- Preserved both current-quality and delayed-quality variants. The difference between these variants remains a separately disclosed numerical convention, not a recalibration.

### Recovered/superseded v43 wave artifact

The prior wave-on recovery outcome that drove capital area to about 2.44 ha, reserve below its 0.10 ha floor, and returned `B` to about 0.15 gha was reproduced with the v43 solver. The root cause was inconsistent bookkeeping: `T_b` affected the within-step fast-land yield but was omitted from returned `B` and from delayed `B` history. With the corrected v44 implementation and the same wave-on recovery initial state (`dt=0.05 yr`, `T=900 yr`), the current-quality solver gives `max(A_c)=1.731 ha`, `min(A_r)=0.321 ha`, and final `B=0.899 gha`; the reserve floor is respected. The earlier values are explicitly superseded and are not reported as model results.

## Controlled technology-wave experiment

`work/tb_wave_debt_scan.py` pairs active-wave and no-wave runs with identical physical initial states, parameters, pre-run history, and solver; only the wave switch differs. The test includes `P0=1.0` and the reference `P0=1.2` cases, step halving from `dt=0.05` to `0.025 yr`, both solver variants, a conservation/domain check, and an integer-`D0` regression test.

- At `P0=1.0`, the delayed-quality solver's all-time peak `D` is 0.00812593 gha yr without the wave and 0.02020493 gha yr with it (ratio 2.4865) at `dt=0.05 yr`; the refined-step ratio is 2.4917. The current-quality ratio at `dt=0.05 yr` is 2.4222.
- At reference `P0=1.2`, the wave run has a lower all-time maximum (0.05103741 vs. 0.06121790 gha yr; ratio 0.8337), but a higher post-midpoint maximum for `t >= t_wave = 40 yr` (0.02518414 vs. 0.01085412 gha yr; ratio 2.3202). The refined-step ratios are 0.8329 (all-time) and 2.3283 (post-midpoint). These are distinct responses; neither is generalized beyond the declared scenario.
- The maximum area-conservation residual in the active-wave demonstration is `4.44e-16 ha`; the minimum reserve is 0.286 ha, above its 0.10 ha floor. Reported debt maxima change by less than 0.9% under step halving.
- The generated SI figure is `figures/fig_tb_wave_debt.pdf` (PNG companion); full metrics and trajectories are in `work/tb_wave_debt_metrics.csv` and the two `work/tb_wave_debt_timeseries_*.csv` files.

## Manuscript and SI revisions

- American English throughout author-written manuscript and SI prose; official titles, journal names, and source titles retain their published spelling.
- Added acknowledgments to Global Footprint Network for publicly available data, Mathis Wackernagel for thoughtful review, the *Ecological Modelling* editors for trust and support, and Arena.ai for its ingenuity and online tools.
- Removed “and language editing” from the generative-AI declaration.
- Clarified that the model's baseline frozen-demand run has a modeled capital-area decline from 1.500 to 0.808 ha while `B` rises from 0.594 to 0.825 gha, and that this conditional model trajectory is not a measured NFA stock trend.
- Added a component-level physical-stock scoreboard with explicit extent/condition and stock/flow distinctions, units, overlap cautions, and valuation requirements. NFA land-type accounts remain flow/account proxies and are not treated as direct measurements of `A_c`.
- Updated methods and parameter tables so the technology wave is explicitly off in baseline figures/tables and on only in SI S8.

## Additional editorial and accounting audit

- Tightened the abstract to 232 words while keeping the complete keyword list on the title page.
- Made the central baseline distinction explicit throughout: capital-land area `A_c` declines 46.156%, per-hectare `Upsilon(q)` declines 10.330%, and the modeled annual contribution `Upsilon(q) A_c` declines 51.718%. The text does not characterize any one of these as a measured global physical-stock trend.
- Added the fast-book contribution `Y_f` to the SI numerical audit; checked its endpoint against the solver output. The endpoint `b_f=0.849974 gha ha^-1` (not exactly 0.85 because `D` remains nonzero) gives `A_f=0.923107 ha`, which rounds to the displayed 0.923 ha.
- Added a carefully qualified model-to-NFA mapping table. It distinguishes an empirical non-cropland/vintage residual from the model contribution and does not claim that NFA categories identify `A_c`.
- Recast the baseline's terminal behavior as an asymptotic approach to balance, rather than floor contact; the panel (b) label was reduced and repositioned after visual review so it no longer overlaps the heading.
- Completed a source spelling scan of author-written manuscript/SI prose; the only British-form match was the official journal title *Ecological Modelling*. Published titles retain original spelling. Reviewed every `46` and `0.808` match: remaining percentages refer specifically to capital-land area; all `0.808` values are `A_c` in hectares.
- Audited citation/reference-list consistency: the main and SI bibliographies have the same 57 entries, byte-identical entry text, no duplicate keys, no missing citations, and no uncited entries.
- The fetched historical figure listing confirms the preserved S1--S15 scope. Current v42 suggestions were adopted where they improved precision and did not duplicate existing material; blanket claims about NFA-measured physical stocks, new stand-alone summaries, and unscoped CSD/collapse language were not added.

## Revalidation

- Both corrected solver modules pass `py_compile` and the controlled regression/test script.
- `make_fig_model.py` passes its baseline assertions; masking window remains 150.3 yr and `E_ceil = 1.1384 gha`.
- `drawdown_depth.py`, `work/verify_tab_conv_basin.py`, and `work/recovery_metric_and_tau_p_scan.py` were rerun with the corrected solver. The main paper's floor-proximity thresholds were rechecked at `dt=0.05 yr`, `T=1000 yr`: 2.4101, 2.7005, 2.9779, and 3.1407 cap for initial capital areas 0.40, 0.70, 1.00, and 1.18 ha, respectively; they remain unchanged at the manuscript's displayed precision and are not described as finite-time floor contact.
- `assemble.py` and three-pass pdfLaTeX builds complete successfully for the main paper and SI (36 and 22 pages). Visual checks cover the title/abstract, baseline results, discussion, SI demonstration tables, and model-to-NFA mapping table. No unresolved references/citations or overfull boxes are present; nonfatal PDF-string and underfull-box warnings remain.
- Final release copies, checksums, and remote-tree/blob verification are still pending; v44 has not been published. These are to be recorded after the package audit and publication.

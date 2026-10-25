# ECOMOD v45 review status

**As of:** 2026-10-25  
**Working package:** `/home/user/ecomod_v45/`  
**Release state:** local working candidate only. No commit, push, publication, cleanup, or deletion has occurred. Published v44 remains unchanged. The `output_v45_release_candidate_final2/` PDFs are preserved pre-audit artifacts and do not match current sources.

## Audit evaluation and corrections

| Audit point | Finding | Action / evidence |
|---|---|---|
| Duplicate Poorter citation | **Survived.** The methods prose wrapped `Poorter et al.` around an author-year citation that already supplies the author. | Removed the duplicated construction in `parts/01_methods.tex`; the citation now renders once. |
| Solver does not use the stated delayed-quality equation | **Survived.** The old canonical solver updated quality using current `q(t)` while the equation specifies `q(t-\tau_g)`. | Promoted the delayed-quality implementation to `work/twoland_fixed.py`; the previous implementation is preserved in `work/twoland_fixed_current.py`. `work/twoland_fixed_delayed.py` remains as a compatibility/reproduction copy. All reported trajectories use delayed quality. |
| Custom gate integrator and variant imports are inconsistent | **Survived.** The custom integrator independently used current quality, and the wave scan's aliases did not reflect the intended current/delayed comparison after solver promotion. | The reported recovery integrator now uses delayed-quality history; the wave scan imports `twoland_fixed_current` for sensitivity and canonical `twoland_fixed` for reported runs. The former custom integrator is preserved as `work/recovery_metric_and_tau_p_scan_current_quality.py`. |
| Recovery table/prose are supported by the declared drawdown run | **Survived as a stale-output issue.** The prior hand-maintained `si_tab_recovery.tex` values did not match the accompanying drawdown CSV and its stated run. | Regenerated from the canonical delayed-quality `si_drawdown_depth.csv` using `work/render_si_model_tables.py`. The six reported recovery ratios are 0.89, 0.46, 0.39, 0.29, 0.24, and 0.21; none reaches the reference. The old table snapshot remains preserved under `_current_quality` for provenance, but is not endorsed as a validated sensitivity result. The prose now distinguishes this drawdown table from the separate gate-sign experiment, where over-restoration is reproduced. |
| Units conflate NFA accounts with model quantities | **Survived.** `Y_f`, `Y_c`, `S`, and `D` were too broadly described as NFA account amounts. | Main and SI conventions now distinguish annual NFA account values `B,E` from model-derived contributions `Y_f,Y_c`, model shortfall `S`, and model-internal debt integral `D`. `D` is in gha yr; it is not an NFA-reported item. |
| Alleged `Poelau`, `Hurt/Hurtt`, and `E_cell` defects | **Not reproduced.** `Poeplau` is correctly spelled; none of the alleged strings occurs in the manuscript/SI source. | No invented correction was made. |
| Duplicate parameter paragraph | **Not reproduced.** The source has one parameter-registry paragraph; the other grep hit was its assembled copy. | No content was deleted. |
| Duplicate §3.1 opening | **Not reproduced.** The top of main page 10 is a continuation of the numerical-method paragraph from page 9; Results and the §3.1 opening occur once. | Removed the redundant base-model-wave clause; the page transition was visually checked. |
| Wrong regeneration-delay symbol / central anchor | **Not reproduced.** The parameter row correctly uses `tau_g`; `phi_0=0.1286472202` is the central proxy anchor and `0.19` is a sensitivity. | Retained the correct parameterization and clarified the equation reference in the SI. |
| Claimed Zenodo v42/v43 lineage | **Unverified and not asserted.** The fetched record 22554480 identifies a v1 preprint record and lists v35 manuscript files; it does not establish a v42/v43 archive. | Removed/avoided the lineage claim; no Zenodo record was changed. |

## Scientific and empirical acceptance criteria

- **NFA scope:** Edition 2026 v1.0, primary world window 1961–2023; the 1961–2022 sensitivity is from the same edition and population series. Estimated 2024–2025 rows are excluded.
- **Accounting versus physical stocks:** component movements are described as NFA account attributions in gha, not biomass, soil-condition, wetland, fish-biomass, or global physical-stock trends. The conditional model trajectory for `A_c`, `Upsilon(q)`, and `Upsilon(q) A_c` is kept separate from measured accounts.
- **Physical-stock scoreboard:** remains an unpopulated specification. No common-boundary global physical-stock series for the relevant components was assembled; no physical-stock composite or decline finding is presented. This is not stated as proof that such an inventory could never be assembled.
- **Proxy:** `X=b_hat_f A_f` and `C=B_NFA-X` remain accounting constructions. Cereal yield is a sentinel rather than an all-crops measure; `C` is neither ecological capital nor `Upsilon(q)A_c`.
- **Frozen equilibrium/path dependence:** the frozen-demand balance branch may be unique while realized land allocation remains path-dependent under one-way conversion and disabled restoration; the text does not imply perpetual equilibrium decline.

## Canonical model outputs and validation

- Demonstration mask window: **149.0 yr** with delayed quality, compared with **150.3 yr** under the preserved current-quality sensitivity variant. At `A_c0=1.0 ha`, floor thresholds at `tau_g=20` and `40 yr` are 2.954 cap (delayed) versus 2.955 cap (current); at `tau_g=5 yr` both are 2.955 cap.
- At the canonical demonstration mask end, `B=0.825000 gha`, `A_c=0.807657 ha`, and `A_f=0.923109 ha`. The modeled capital contribution `Upsilon(q) A_c` falls from 0.08364 to 0.04038 gha (51.72%). These are conditional model results, not empirical global-stock estimates.
- The separate gate-sign table was recomputed with delayed quality. Its conversion-frozen surplus row has peak debt 0.543 gha yr (the former current-quality output was 0.546 gha yr); other displayed gate-table values were checked against the helper output.
- The controlled wave/no-wave experiment passes its assertions: at `P0=1.0`, delayed-quality all-time peak-debt ratio is 2.4865 at `dt=0.05 yr`, 2.4917 after step halving, and 2.4222 for the current-quality sensitivity. At `P0=1.2`, all-time ratio is 0.8337 while post-midpoint ratio is 2.3202. The distinction and conditional scope remain explicit.
- `drawdown_depth.py`, `work/render_si_model_tables.py`, `make_fig_model.py`, `work/verify_tab_conv_basin.py`, `work/tb_wave_debt_scan.py`, and the delayed-quality gate helper were rerun. Python sources compile. The NFA endpoint/component and proxy Divisia scripts were rerun; their Edition 2026 results remain unchanged.

## Build, citations, and visual review

- **Current restoration-review build:** `output_v45_restoration_finalcheck_20261025/manuscript_working_main.pdf` — **33 pages, US Letter**; `manuscript_working_si.pdf` — **20 pages, A4**. `assemble.py` was followed by three pdfLaTeX passes for each document. The 32/17-page `output_v45_editorial/`, earlier 36/23-page audit PDFs, `output_v45_restoration_review_20261025/`, and prior release-candidate PDFs are preserved comparison artifacts; only the finalcheck PDFs match the latest sources.
- **Final restoration-pass diagnostics:** no fatal errors, undefined or multiply defined references, unresolved citations, overfull boxes, or oversized-float warnings. The four Hyperref PDF-string warnings trace to `elsarticle` corresponding-author markup (`\corref{cor1}`/`\cortext[cor1]`), whose internal note commands are stripped from PDF strings; the printed author/correspondence content is present, so no suppression patch was warranted. Underfull-\hbox warnings fell from 34 to 28 in the main and remain 12 in the SI after the Table 4 scope column was changed to ragged-right; remaining instances are associated mainly with long reference titles/URLs, table cells, and a short equation paragraph. The rendered pages show no clipping or materially disruptive spacing, so no further box edits were made. The earlier parameter-table float warning remains resolved.
- **Editorial and scientific-content corrections validated:** gha is defined as a productivity-normalized hectare, with the annual basis of NFA account amounts implicit. The focused §4.2 audit now states that annual account values are in gha, per-capita ratios are in gha per person, $E_{\mathrm{prod}}/B$ is dimensionless, and the proxy $X$ and residual $C$ are in gha. The restored orchard analogy distinguishes annual harvest flow from productive capital; the elevator analogy is limited to observability and does not predict model failure. The data-availability paragraph commits to a future public GitHub deposit and Zenodo archive without claiming either exists or supplying a URL. The one-stock comparator is intentionally placed at SI S7 and the controlled wave experiment at S8. No old ECOMOD draft/version history is cited; Edition 2026 account results remain distinct from physical-stock evidence; the crop-proxy residual is not represented as ecological capital or the model's capital contribution; the physical-stock scoreboard remains an unpopulated specification; and frozen-equilibrium results remain distinct from path-dependent trajectories. The debt/wave result is conditional and distinguishes all-time from post-midpoint maxima.
- **Citation/label audit:** main has 44 unique labels and 46 cited bibliography entries; SI has 45 unique labels and 12 cited bibliography entries. Every entry is cited in its document; there are no duplicate labels/keys or unresolved local references.
- **Source-checked typo/unit audit:** `Poeplau` is correct and no `Poelau` or `E_cell` error is present; $E_{\mathrm{ceil}}$ is correctly named; Table 2a's header and the Table 2 caption symbol/units were checked; Table 4's $\tau_g$/$\tau_p$ context is explicit. The §4.2 per-capita and proxy units are now stated directly. No unsupported correction was applied.
- **Extracted-PDF checks:** no `??`, TODO/FIXME, accidental placeholder, or local-work-path marker was found. The one-stock comparator is present intentionally in SI S7, with the controlled wave experiment in S8; the main cross-reference points to S7. The source-only American-English scan found no targeted British spellings; official titles and technical terms are retained.
- **Visual review of latest restoration build:** main pp. 16, 22–25, and 27–28; SI pp. 15–19. Inspected Table 2, Table 4, §4.1–4.2, the revised per-capita/proxy units, conclusion and full data-availability statement, and the comparator/wave equations, tables, figures, and captions. These pages are legible and unclipped.
- **Current PDF SHA-256:** main `0f3332b70b216353c812aaa7f49da9f4b72d010c6cb3dafea6f962d98dc01801`; SI `e6b9071367c1889c3a8ab1e121947561e809b2bf5e9da44c288690f3a2cdf96f`.
- Current model Figure 1 PDF SHA-256: `84f6da8f02cc2b232f234692b52a3a0ea9d0c60f0c435eba4e533bbb509b4a4a`; controlled-wave figure PDF: `71b0f033ae330f31a566ef5204e2ba06624208fcc8baac4e929cc92544b634a9`.
- Official NFA Edition 2026 workbook SHA-256: `26e4f5c78d9fe20cb5cd51c073815157566711b53278a1f9118d7726ab60ad1b`.
- The unchanged pre-audit `final2` PDFs retain their earlier hashes: main `313989f9d3a70b8bc84f4d682ac2cc568016c026449057143fb0f398ca0fa872`; SI `607b00a9e064da2601a7f6b05152f35dd5a3a2b26a946856ec1133f6c4ea8185`. They are not current deliverables.

NFA endpoint summary:

| Window | Total biocapacity `B` | `B/P` | `E_prod/P` | First `E_prod/B > 1` |
|---|---:|---:|---:|---:|
| 1961–2023 | +24.8568% | −52.7085% | +16.7327% | 1973 |
| 1961–2022 (same edition) | +24.5450% | −52.4131% | +17.6994% | 1973 |

These are NFA account results and per-capita accounting ratios, not physical-stock measurements.

## Remaining release conditions

1. Regenerate and verify `SHA256SUMS_v45_working.txt` against the restored sources, data, figures, and finalcheck PDFs before any release; the existing manifest is stale after this pass.
2. The data-availability text is a future-deposit commitment only. Add repository/Zenodo identifiers only after the deposits actually exist and have been verified; do not create release filenames without an approved destination and release decision.
3. No commit, push, publication, cleanup, or deletion has occurred in this restoration pass. Preserve v44, current-quality backups, and prior candidate builds until the required remote-copy audit and release approval.

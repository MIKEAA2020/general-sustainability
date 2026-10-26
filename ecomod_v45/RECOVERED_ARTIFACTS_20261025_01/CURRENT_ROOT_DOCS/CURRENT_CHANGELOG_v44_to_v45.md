# ECOMOD v44 → v45 working revision

**Revision date:** 2026-10-24  
**Base:** published ECOMOD v44, unchanged at its existing package path  
**Current package:** `/home/user/ecomod_v45/`  
**Status:** not committed, pushed, or published

## Audit follow-up (2026-10-25; current source and reviewed local build)

- The audit found a real duplicated `Poorter` citation construction in `parts/01_methods.tex`; it has been corrected. The canonical model solver now evaluates regeneration at delayed quality `q(t-\tau_g)`, exactly as stated in the governing equation. The former current-quality solver is preserved at `work/twoland_fixed_current.py`; pre-audit Figure 1, drawdown CSV, and SI table-source snapshots are backed up under `_current_quality` names for provenance. One pre-audit recovery-table snapshot was later found not to match its drawdown CSV and is not treated as validated sensitivity output.
- Updated the technology-wave scan to compare the preserved current-quality solver with canonical `work/twoland_fixed.py`. Updated the custom recovery-gate integrator to use delayed quality; the old current-quality integrator is retained separately. Regenerated the drawdown CSV, Figure 1, wave diagnostics, and SI recovery/gate results.
- Found that the hand-maintained SI recovery table did not match the drawdown CSV and its stated run. It is now generated from `si_drawdown_depth.csv` by `work/render_si_model_tables.py`; the delayed-quality recovery ratios are 0.89, 0.46, 0.39, 0.29, 0.24, and 0.21 for the six displayed initial-population cases. The prose no longer claims over-restoration in that table; over-restoration remains confined to the separate gate-sign experiment where it is reproduced.
- Clarified unit language: only `B` and `E` are identified as NFA account values; `Y_f` and `Y_c` are model-derived annual contributions, `S` is a model shortfall, and `D` is a model-internal time-integral, not NFA-reported items. Removed a redundant base-model wave clause and updated the canonical window from 150.3 to 149.0 years.
- Several audit claims were not supported by the checked source: `Poeplau` is correct and `Poelau`, `Hurt/Hurtt`, and `E_cell` are absent; the parameter paragraph occurs once; the apparent duplicate §3.1 opening is a page continuation, not a duplicated paragraph; the delay parameter is correctly written as `tau_g`. The fetched Zenodo record 22554480 identifies a v1 preprint deposit with v35 manuscript files, not a v42/v43 archive, so no such lineage is asserted.
- Source/model scripts and data have been updated. The pre-audit `output_v45_release_candidate_final2/` PDFs remain unchanged and must not be treated as current. The 36-page/23-page `output_v45_audit_current/` build was an intermediate audit artifact; it was superseded by the later restoration build documented below. The local working checksum list must be regenerated after restoration; remote manifest/byte-verification and release approval remain outstanding.

## Restoration and finalcheck (2026-10-25; current working state)

- The content-recovery review compared current main/SI sources with v44/v45 history and original material. It restores the orchard flow-versus-productive-capital explanation and the elevator observability analogy in a qualified form; neither is removed as mere redundancy. The companion discussion and comparator pedagogy are retained.
- The public code/data availability statement now promises a future public GitHub deposit and Zenodo archive, without claiming a deposit exists or inventing a URL. SI numbering is comparator S7 and controlled technology-wave experiment S8, with the main comparator reference corrected accordingly.
- Source checks confirm `Poeplau`, correct $E_{\mathrm{ceil}}$ notation, Table 2a header and caption symbols/units, §4.2 account/per-capita/proxy units, and the Table 4 $\tau_g$/$\tau_p$ scope. Table 4's scope column was changed to ragged-right after visual review of underfull-box spacing.
- Current finalcheck PDFs are in `output_v45_restoration_finalcheck_20261025/`: main 33 pages (US Letter), SI 20 pages (A4), each compiled in three pdfLaTeX passes. Latest PDF SHA-256: main `0f3332b70b216353c812aaa7f49da9f4b72d010c6cb3dafea6f962d98dc01801`; SI `e6b9071367c1889c3a8ab1e121947561e809b2bf5e9da44c288690f3a2cdf96f`.
- Visual checks cover main pp. 16, 22–25, 27–28 and SI pp. 15–19. No unresolved/duplicate references, overfull boxes, or clipping were found. Four non-fatal Hyperref warnings arise from `elsarticle` corresponding-author metadata; remaining underfull boxes are principally in bibliography URLs/titles and a small number of table/text lines. No additional layout edits were warranted.
- This remains a local v45 working candidate. No commit, push, publication, cleanup, or deletion occurred; v44 remains unchanged. The checksum manifest must be refreshed after this pass, and remote-copy verification and release approval remain outstanding.

## Empirical revision

- Rebuilt the empirical backbone from the official NFA Edition 2026 workbook, results and metadata v1.0. The primary window is 1961–2023; the 1961–2022 sensitivity is from the same edition. Estimated 2024–2025 observations are excluded, and no 2025-edition values are blended into the series.
- Recomputed per-capita quantities from unrounded account totals and the workbook's UN PopStat population field. The exact log identity is retained as an accounting split, not a causal decomposition.
- Added NFA component ratios/contributions under their exact workbook labels. Every statement is scoped to account movement in gha, not biomass, soil condition, wetland extent, fish biomass, or a physical-stock trend.
- Regenerated Figures 2–3 from the 2026 workbook and updated the main results, discussion, conclusion, and methods.
- Updated SI S5 with the endpoint windows, population identity, NFA account composition, direct crop-account quotient caveat, and proxy sensitivity.

## Model-versus-physical-stock interpretation

- Clarified that the representative `A_c` decrease, the change in `Upsilon(q)`, and the change in `Upsilon(q) A_c` are conditional model outputs. They are not measurements or estimates of a real-world global physical-stock decline.
- Kept the frozen-demand branch result conditional: its balance point can be unique without making the realized land allocation history-independent. With one-way conversion and restoration disabled, the post-overshoot `A_c` state persists below its pre-overshoot level, but it does not decline perpetually at equilibrium.
- Reframed the physical-stock scoreboard as a specification only. No common-boundary global physical-stock inventory for the relevant components was assembled; no decline finding or composite is reported. The SI explains why heterogeneous stocks, extents, condition measures, and flows are nonadditive absent shared boundaries, normalization/valuation, and substitution rules.

## Exploratory crop proxy

- The proxy is explicitly mapped as `X = b_hat_f A_f`, `C = B_NFA - X`; `C` is an accounting residual, not ecological capital, a measured non-cropland stock, or `Upsilon(q) A_c`.
- Uses the independent OWID/FAOSTAT cropland-area and cereal-yield inputs. Cereal yield is labeled a sentinel, not an all-crops measure. The central anchor is the 1961 NFA cropland account share, with the declared sensitivity retained.
- Preserves the exclusion of the spliced World Bank all-crops production-index series because discontinuous base-period changes make it unsuitable for this decomposition.

## Citation and alignment review

- Added citations for NFA Edition 2026 and both OWID/FAOSTAT series; removed superseded generic FAOSTAT entries and unused references.
- Rechecked references and labels after the prose/SI revision. Companion citations now point to commit-specific current sources (P1 v59, P3 v32, P4 v41). The P1/P4 Zenodo records are explicitly identified by their earlier deposited titles and versions; P3 links directly to v32 and identifies the related v31 file set. No Zenodo record was modified.
- Ran the requested source-only `sed` spelling pass (`modelled` to `modeled`) while preserving official *Ecological Modelling* and the specified American-English forms. Added a controlled page break before SI S5.2 so its heading and proxy data citation do not split across pages.
- Compared the current manuscript/SI against the v36 ECOMOD alignment-audit flags: weak/strong sustainability and exact-tube references are attributed; P1 v59's Lemma A/Theorem S2(ii) are the cited results; the mobilizing/protective taxonomy is cited; and the affiliation is present. The earlier broad productivity-illusion gloss remains outside ECOMOD. The orchard analogy is restored to distinguish harvest flow from productive capital; the elevator analogy is retained only as an observability comparison and does not imply inevitable or abrupt model failure. The material-cycle definition in SI is explicitly quoted and attributed. The external Zenodo refresh remains a separate owner-side action, not part of this revision.

## Currency and publication gate

A fresh scan of the repository's fetched branches and tags found v44 as the latest numbered ECOMOD package and no v45 path/tag or ECOMOD-specific split/merge record. See `ECOMOD_VERSION_CURRENCY_v45.md`. V44 remains immutable. This v45 working revision has not been pushed or published; the final archive URL, release manifest, and remote hash verification are still to be created only after the remaining checks and release decision.

## Build and validation

Final compile details are recorded in `REVIEW_STATUS_v45.md`. The NFA endpoint and proxy identity checks, citation/label check, PDF page counts and visual review were performed locally. Any change after those checks requires a fresh build and inspection before release.
## Citation/framing and SI verification follow-up — 2026-10-25

- Preserved the existing companion key map: `Abaee2026a` for Paper4/governance, `Abaee2026b` for Paper06/assessment, and `Abaee2026c` for Paper3/ledger. Updated companion locators, titles, versions, and commit links in place.
- Checked Paper06 v71 Theorem 4(iii) against its exact witness-defined diagonal-gap region. Narrowed the positive-elasticity safety claim in main and SI to that region; did not state the theorem as a general result outside it.
- Pinned the Paper3 reference to commit `2efaa62083f2007dec3446c15c475af88f0925f3` and disclosed the PDF v50 / README-checksum v49 / TeX-header v48 metadata mismatch in a short main-text footnote.
- Kept matching result-style titles in main and SI; made the fixed-point reference Eq. (18), the SI Table S2 reference in §S3, and the Paper3 weak/strong discussion location explicit.
- Distinguished the model's annual human-available-flow reservation from Half-Earth's spatial conservation target. Left out broad boom–bust and the removed blanket “no Allee threshold” claims.
- Verified the Table S4 `0.050` minimum against both drawdown CSVs. Checked all 124 sampled rows per CSV: both minimum-area columns are monotone in the tested directions (non-increasing with `P0`, non-decreasing with `A_c0`), with no grid violations. No visual-pattern edit was applied.
- Added a page break before the final SI §S4.2 threshold comparison so the sentence begins cleanly on SI p. 7. Rebuilt and visually checked Tables S4/S6, main Table 2(a), citations, footnote, matching titles, and the scoped theorem claim.
- Built fresh QA PDFs in `output_v45_citation_framing_final_QA_20261025/` (main 35 pages, SI 20 pages). Extraction found no unresolved `??` markers; visual review covered the title, citation note, Table 2(a), theorem scope, Half-Earth framing, Tables S4/S6, and the revised SI §S4.2 page break. No commit, push, or publication was performed.

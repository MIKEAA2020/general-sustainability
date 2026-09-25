# Round 22 — §D Roadmap Conducted: Window Matrix, Band Certificates, Backward Extension, Panel Study, Residue LP Study

**Date:** 2026-09-26. **Base:** `905d708` (round 21 final). **Directives:** (1) triage the remaining audit points (implement as-is or after correction); (2) run the continuous-time residue LP study and the window matrix; (3) acquire data and conduct the §D roadmap, searching repo, releases, and the web.

## Deliverables this round

1. **`applied_regime_viability_v5.{tex,pdf}`** (7 pp) with `applied_regime_viability_v5_verification.py` — **229/229 exact checks** (185 inherited + 44 new). Build gate: exit 0, overfull 0, halt 0, no "??", rendered text identical across consecutive builds. New certified content (all in §"The window profile and the band certificates" + scope sentences):
   - **Window profile (opus U2/U10):** the reference window's minimum end-to-start ratio per horizon k: k=1: 41800/45147 (2/6 subwindows below unity); k=2: 83600/86323; k=3: 44320/45147; **k = 4, 5, 6: every subwindow grows** (15361/15049, 22160/21027, 15361/14018); 15 of 21 subwindows all-growth. The sustained-decline reading holds only at horizons one to three — the selection critique is discharged at all horizons and the sustained-rate scenario is delimited by the record itself.
   - **Band certificates (astra U2):** on the reassessment vintage's published 95% bands, a step is band-certified iff B_hi(t+1) < B_lo(t); over all seventy consecutive pairs of 1954–2024, **exactly the four collapse-era steps certify** (1991→92 upper bound 468/478 = 0.9791; 92→93: 115/265 = 0.4340; plus 93→94, 94→95) and no reference-decade step; the **1993 floor breach is band-certified at the upper edge (115 < 276)**; 1992 is indeterminate (265 ≤ 276 ≤ 468). The full-uncertainty method isolates the collapse era exactly.
   - **Vintage dependence (opus U6):** in the reassessment vintage the reference decade is **all-growth** (minimum multiplier 1.01) with the decline beginning 1989→90 at 738/864 ≈ 0.854 — the worst-step typology is vintage-internal, and the paper states its decade claims in the input vintage. A third vintage (database extract, 2021) reads 1990–93 as 765, 747, 354, 83 kt; all three vintages agree on the breach sign pattern.
   - **Backward extension (opus U18):** the vintage's 1954–1982 record peaks at 1508 kt (1962); the 1983 window opens at 427 kt = **28.3% of the peak**, three years after a **prior floor episode** (crossings exactly {1977, 1980, 1993, 2016}; 1978 band-certified below the floor). The window's placement is certified as a data artifact — fable/opus F16 answered exactly.
   - **Scope sentences:** the covariate is a single acoustic instrument with no comparability guarantee across the redistribution years (fable's caveat, no literature assertion); and the certificate does not extend to the way up — on the 2020→2021 step removals were 10977/29000 ≈ 37.9% of that year's decline (opus F13/U4's recovery-side breakdown, certified).
2. **Window matrix:** computed in full (all 435 record windows scan; the profile above is its certified summary; the matrix itself is reproducible from the verifier's profile block).
3. **`minimax_residue_grid_lp_v1.py` + record** — the theory-line LP study: 42/42 exact checks; four findings recorded in `minimax_residue_grid_lp_v1_record.md` (the certified policy's envelope is coupling-independent; a certified coupling-selection gap ½ vs 1 on the instance; the product coupling is interior at every K ≥ 2, so no vertex-selection law can pin it; the dyadic refinement limit is exactly monotone with rate ½). Does not resolve the conjecture; certifies the boundary conditions any evolution law must satisfy.
4. **`applied_panel_discrimination_v1.py` + record + locked panel CSV** — opus U17 first pass: RAM Legacy v4.66 (DOI 10.5281/zenodo.14043031, md5 `ed6d7cd3f7da1fdcbc60015c3d65014b`) extracted to `paperE1_calibration_data_v2_ram_panel_v1.csv` (10 Atlantic cod stocks, 498 stock-years; the extract's 2J3KL 2016–2021 equals the paper's locked database rows exactly). Result: the level statistic C2 fires 10/10 (non-selective); the bracket certificate C3 fires 5/10 with **zero false alarms on the three controls**, at-or-before the episode on 2J3KL (one-year lead), 4TVn (exact), 4VsW (exact), early on FAPL/IS, and conservative misses on GB/KAT (catch-heavy declines).
5. **Records:** this addendum; `minimax_residue_grid_lp_v1_record.md`; `applied_panel_discrimination_v1_record.md`; roadmap v41; supersession map v11; cover note enclosure line flipped to ARV v5 (229/229).

## Q1 — Remaining audit points: disposition after this round

| Remaining point (source) | Disposition |
|---|---|
| k-window robust multiplier profile (opus U2) | **Implemented** (window profile proposition). |
| Full window matrix, no selection (opus U10) | **Implemented** (profile = certified summary; full scan in verifier). |
| Interval certification under published bands (astra U2, opus U5) | **Implemented** (band certificates; the xte bands are the only published per-year uncertainty in the locked files). |
| Backward window extension (opus U18) | **Implemented** (1954–1982 vintage-internal remark). |
| Vintage matrix / vintage mixing (opus U6, F14; fable 1.9) | **Partially implemented** (three vintages tabulated; typology vintage-dependence certified; the 49.7% cross-vintage ratio retained with B_ref argued as a management constant — recorded). |
| Recognition-time across vintages (fable 2.5c) | **Data-gated** — needs the real-time 1991–93 assessment documents (CSAS archive); the three-vintage agreement now certified is the closest in-vitro substitute; located as the next acquisition target. |
| Multi-stock discrimination panel (opus U17; grok) | **First pass implemented** (panel study; full ROC/AUC protocol over a larger panel remains roadmap, seeded by the locked CSV). |
| Model-free breakdown factors (opus U4) | **Implemented in round 21** (8.61×/24.66×); the recovery-side 37.9% added this round. |
| Age-structured lifting (astra U4–5, opus U14) | **Data-gated** — needs machine-readable age compositions (DFO 2016 CSR tables are PDF-only; extraction is an owner-scale task). Recorded with pointer. |
| Regime sojourn/value-of-monitoring kernels (astra U5, opus U15) | **Out of scope for the applied paper** (theory-paper material); recorded. |
| Harvest viability kernel (opus U13); DR breach probabilities (U16); Lean export (U19); full online decision-time table (U9); reference-point admissibility alternatives (U12) | **Roadmap** (recorded in v41; U12 partially realized by the discrimination proposition; U9 partially by the contemporaneity/lead statements). |
| Capelin comparability caveat (fable 1.8) | **Implemented** (scope sentence). |
| M-baseline question (fable: "M 1990 already double baseline") | **Answered by the spine table**: M 1990 = 0.403 lies inside the reference decade's own range (0.277–0.494); the crossing to 1.002 is the certified event. No further action. |
| F-column selective refusal (fable) | **Adjudicated, no change**: the F column is derived from assumed catch given the model, not an independent decomposition; the bracket lemma performs the accounting separation without it. |
| Hash-pinned data manifest (opus U7) | **Already satisfied** by the data record (2026d) + this round's CSV carries its source md5 in the verifier and record. |

## Data-acquisition ledger

- **Repo** (full tree, 5,668 files): no cod data beyond the known wave-e-cod CSVs and RAM extract; build scripts and other lineages only.
- **Releases:** two workspace archives (`edwards-framework-e1` 56.1 MB + 73.7 MB; `compendium-v1.0` 135 MB) inventoried by name/size; content listing blocked by sandbox bandwidth (~12 KB/s to the release CDN); no cod-data indication; the previously recorded PAT-in-release owner-action note stands.
- **Web:** RAM Legacy v4.66 (latest, 2024-11-06) downloaded from Zenodo (111.9 MB, md5 verified against the API), parsed, panel extracted, locked. The 1991–93 CSAS assessment documents for the recognition-time item located as the next web target (not extracted this round).

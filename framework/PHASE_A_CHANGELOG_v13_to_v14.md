# PHASE A CHANGELOG — v13 → v14 (2026-09-13)

Text-only implementation pass. Source: `paperF1_retention_framework_v13.md` (untouched).
Result: `paperF1_retention_framework_v14.md` (62,408 chars, 450 lines; +18 lines ≈ +4.2%).
Applied by `framework/apply_phaseA_v13_to_v14.py` — 41 asserted replacement rules (grouped into the 37 rows below; 4 rules are second-occurrence variants), one pass, no overwrites.
Adjudications: `REMAINING_POINTS_TWO_AUDITS_v13.md` (register) and `JOINT_EVALUATION_TWO_AUDITS_v13.md` §5.
Style gate: `journal_style_automated_scan.py` on v14 → **0 blockers, PASS**.

## Edit → audit point

| # | Edit | Audit point | Notes |
|---|---|---|---|
| 1 | K-bound wording: "per-origin lower bound max_train S + 10 kt … ≈950.8 kt at the earliest origins … and 50.8 kt on the recovery-window training set (predictor-state maximum 40.8 kt, 2006)" | **AD1 + N2** | E1 v20 A6 convention + data-verified; kills the wrong "lower bound 50.8 kt general" AND the wrong "≈91 kt recovery-window" (91.1/81.1 was the terminal state; recovery bound is 50.8 from 2006's 40.8) |
| 2 | "0.0359 kt" (was 0.0358) | qwen 2.4 | 114.8024 − 114.7665 = 0.0359 |
| 3 | Ladder is a rooted tree, not a chain | claude 2.2 | M1b = branch, not rung |
| 4 | Model inventory table (rungs / auxiliary / diagnostics / baselines per object) | claude 2.3 | inserted after the seven/eight-model totals |
| 5 | "Retention is decided per specification." | claude 5 | fragment fix |
| 6 | "reported as a sensitivity row on the primary passes" | qwen 4.10 | gloss |
| 7 | moratorium gloss — "the 1992–1993 fishing moratorium is deliberately not evaluated" | qwen 4.11 | gloss |
| 8 | Algorithm box reordered — class-grounds check pre-gate, first | claude 2.1 | box + prose now match the declared operational order |
| 9 | Table 4 M2m h=5: "margin −3.66 ft, CI [−5.76, −2.19] excludes zero" | **D1 (resolved)** | computed with the archived E3 machinery (e3_audit_uncertainty.py, seed 20260905, block 8, nboot 10000, n=71) |
| 10 | Table 4 M2m h=1: CI [−1.445, −0.676] | **D1** | same archived uncertainty layer |
| 11 | MAE tie gloss "10.72 vs 10.73 ft" (4 occurrences) | **D2** | single-cell 10.73 anomaly (Table 2d vs Table 5) explained |
| 12 | Table 5-2 comparator band 12.1971 | qwen 4.18 batch | the H1 band is 0.95 × comparator, not 0.95 × persist |
| 13 | Alternative-comparator counterfactual: verdict unchanged under M1 comparator | qwen 3.6 | closes the unexamined counterfactual |
| 14 | h>1 held-constant justification (both occurrences incl. summary block) | qwen 3.7 | origin-available flux estimate |
| 15 | "17.44/17.64" gloss (3 occurrences) | qwen 4.24 | rolling vs fixed-window h=5 |
| 16 | "bold 193" deleted (2 occurrences) | qwen 4.18 / claude 1.12 | typesetting instruction, not prose |
| 17 | Origin-set sensitivity sentence (264.72 → 193 shift) | qwen 3.9 | verdict robust to origin-set choice |
| 18 | D3 row note: "18–22× the null false-retention rate (0.005 per module)" | claude 2.4 | was "< chance (20%)" — that's retention frequency among candidates, not the module's chance against the bar |
| 19 | Per-cell adequacy sentence: "2 of 8 clear the bar (D1 only); specificity clears 90% in both null cells (D5) and in 0 of 4 misspecified cells (D6/D7)" | claude 2.5 | — |
| 20 | Licensing sentence + D6/D7 predictive-gain registration | claude 2.6 (**AD2**) | retention licenses a prediction claim, never a mechanism claim |
| 21 | Evidential-weight table (LR+/LR− per DGP cell; D4 low σ null instrument) | claude 4.1 | — |
| 22 | Tolerance sentence (±17 kt on 445.5 kt = 3.8%; load-bearing 4.33% decision) | claude 3.2 (**AD3**) | framed as pre-registered robustness requirement, not an executed run |
| 23 | Persistence-baseline justification (pre-registered H2/H3 anchor; training-mean h=5 result reported as evidence about baseline choice) | qwen 3.10 (**AD7**) | — |
| 24 | Fixed-window sentence rewritten (both occurrences) | qwen 3.8 / claude 5 | declared trains for fixed windows; 15-year floor is rolling-only |
| 25 | Coarse regime labelled "the frozen primary catch treatment" | claude 3.5 | confirmed against SPECIFICATION.md Ω_2016 |
| 26 | Audit table: third status **revised** + row "Predictand dated before origin, published only in a later vintage" | claude 3.1 | cod SSB = assessment output conditioned on the full series |
| 27 | Two-systems sentence — "share a scalar stock driven by fluxes" + candidate-mechanism paragraph (smoother artefact; decisive test registered) | claude 3.1 + claude 5 | test not run; framed as registered, not result |
| 28 | "They do not return it for the same reason" | claude 5 | grammar |
| 29 | Archive paths: `batch 7 (audits of agent arena 1 paper rewrites)/results/e1_dm_uncertainty.csv` + `e3_dm_uncertainty.csv` | **N5** | the DM CSVs live under batch 7, not `wave_e_cod/results/` |
| 30 | Addendum JSON referenced in Data availability | **D1** | `wave_e_edwards/results/e3_audit_uncertainty_add_M2m_h5.json` |
| 31 | D6/D7 line: "the frozen sheet's Amendment-1 wording of eight cells is corrected here against the archived row count" | **N3 / AD8** | dated correction note; the frozen sheet stays untouched |
| 32 | "5 of 32 rows in the full 32-row universe — including the four alternative-comparator M2-versus-M1b rows, which the E1 companion's 'four of the twenty-eight' excludes" | **N4** | reconciliation without altering E1 |
| 33 | `sim_retention_power.csv` provenance note 2026-09-13 | **N1 / D3** | release file does not reproduce the published §4.3 rates; replacement files registered |
| 34 | Makridakis et al. (2020) cited in §1 | qwen 9 | reference existed but was uncited |
| 35 | "information criterion n log MSE + 2k (AIC-style), MASE, bare beat-persistence, 0%/10% band variants, no refitting" | — | resolves the dangling "AIC" mention vs the §4.5 comparison table |
| 36 | Scale sentence at Table 1: SD(target)/SD(Δtarget) 356.5/89.5 kt (Spec A), 423.2/89.6 kt (Spec B), 14.70/12.34 ft (Edwards) | claude 4.8 | computed 2026-09-13 from archived data (n=33/71/90) |
| 37 | §4.5: prospective replacement band sentence (power ≥0.80 / specificity ≥0.90 at the object’s own T and SNR) | **AD4** | per register §4 AD4 directive — registration only, nothing about the 5% band changed |

## Deliberately NOT edited in Phase A (awaiting later phases)

- **Phase B (owner decisions):** qwen 9/10 (Sims-type simulation), qwen 11–14 (wording/redundancy cluster), qwen 2.1 (audit presentation — pending E3/companion style), claude 1.x compression subset (non-destructive), K-bound symbol-pair choice.
- **Phase C (computations):** D3/N1 replacement power CSVs (needs the `tools/sim_*` generators re-run), the smoother rescoring test, the cross-environment tolerance figure, D6/D7 realised predictive gains.
- **Phase D:** prospective-registration subsection (the three registered-but-not-run items are now all named in-text).

## Audit trail

- v13 → v14 diff: `diff framework/paperF1_retention_framework_v13.md framework/paperF1_retention_framework_v14.md`
- v13 is untouched; the edit script reproduces v14 from v13 byte-for-byte.
- AD1 correction record: register §4 AD1 updated (91.1 wrong; recovery bound 50.8 from predictor-state max 40.8 in 2006; general bound 950.8 from 940.8 in 1987).

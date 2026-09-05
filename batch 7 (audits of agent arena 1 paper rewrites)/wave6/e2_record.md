# Wave-6 record — E2 (paperE2_cod_intervention_v19.md from v18)

**Task ID:** 76-E2 · **Build:** `apply_batch7_wave6_e2.py` (fail-loud, byte-reproducible; MD5 `84197badf70a083cd02573812351c46b`, identical on re-execution)

## Item — the critical-zone supply gloss (Result 3.4's Reason)

* **Scan finding** (`wave6/scan/paperE2_cod_intervention.md`, transition v14→v15, item 80): v13/v14's §3.3 supply-replay paragraph carried "S1 gives 10.0 kt (the critical-zone cut is active in 83% of observed years — the stock was below the LRP for almost the entire history, a fact about the collapsed-era estimation window rather than about the rule's post-recovery supply properties, and the two regimes are not mixed)". The v14→v15 source-year restructure kept the supply-replay values (now printed in Result 3.4's Reason) and lost the explanation. Unregistered: v13–v16 carry no version logs; the v17/v18 logs and wave-2/4/5 records do not mention it.
* **Disposition: IMPLEMENTED (restored, wording decided).** One sentence appended inside Result 3.4's Reason, immediately after the supply-replay values it explains (v18 L123 → v19 L123):
  > "The critical-zone rule's low mean is a property of the window, not of the rule: the cut is active in 20 of the 24 replay years (the stock sat below the reference point in all but the 1985 and 1987–1989 states, $83\%$ of the window), a fact about the collapsed-era estimation window rather than about the rule's post-recovery supply properties, and the two regimes are not mixed."
* **Wording decisions:** v13's "83% of observed years" upgraded to the exact "20 of the 24 replay years" with the four above-LRP states named; v13's scoping caveat kept verbatim in substance; house percent style ($83\%$); no new numbers beyond the checkable window fraction.
* **Verification (in-script, fail-loud):** the committed DFO-2016 series (`wave_e_cod/data/ncam_2016_table_a2.csv`) gives exactly 4 above-LRP (884.6 kt) states in 1983–2006 — {1985, 1987, 1988, 1989} — and the same four in 1984–2007 (convention-robust); 60 × 4/24 = 10.0 kt matches the printed S1 mean; 20/24 = 83.3%. Mechanical checks: the gloss present exactly once in the body; changed lines exactly {5, 123}; line count unchanged; all 50 markdown table rows byte-identical; the proof-end marker count unchanged; the abstract untouched.

## Declines (scan items with reasons — full table in `wave6/SCAN_EVALUATION.md`)

* The Chow-type 1992 break test (F = 3.68, p = 0.062) — pre-correction residual pool; recomputation = new computation (registered behind the owner gate).
* The "3.3–50.6% higher permitted supply" companion contrast — superseded by v18's recorded non-comparability correction.
* The K-grid SSE values, the 57.6-kt-era bounds, the old stress-replay/stochastic/from-1990 rows — pre-source-year-correction numbers; restoring them would restore errors.
* All other v13–v18 drops — recorded docket edits (v17's dominance restructure, v18's MSE relabelling), corrections, or preserved content (verified by grep: the supply-replay row, family declarations, residual description, K-grid statement, companion contrasts, stochastic layer, §3.9's source-year table).

## Non-destructiveness

One sentence added, nothing removed; no frozen verdict, score, kernel, boundary, or table value changes; Tables 1–5 byte-identical; the abstract untouched. Version log replaced in place (single-log convention, as v17→v18).

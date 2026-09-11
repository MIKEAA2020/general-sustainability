# Paper 5 open-items discharge record (v37 / supp v13) — 2026-09-11

Discharges six research items into manuscript v37 + supplementary v13. All
research was executed against repo HEAD `4620c633` (re-fetched same-day;
no paper-5 commits by other agents since) with repo-wide pre-build search
(full tree, code-search API, release compendium-v1.0, issue/tag check).

## U5 — case table + query log (new deposits)

- `u5_case_table.csv`: 32 systems, 8 domains, §2.6 criteria (i)–(iv) with
  binding-fail + evidence columns. Rows 1–20 re-verdicted from the
  2026-08-08 tau-window screen (whose continuous-delay criteria differ
  from §2.6); rows 21–22 Icelandic cod/haddock; rows 23–32 cross-domain
  inventory (groundwater, rangeland, wildlife, aquaculture, forestry,
  produced capital). Zero systems meet all four criteria.
- `u5_query_log.md`: repository searches (R1–R8), public-data pulls
  (D1–D3), web searches (W1–W7), re-verdicting rule.
- Manuscript: §2.6 zero-result + S4 pointer; Data availability flipped
  to deposited; S1/S4/S8 register updates.

## η = 0.914 basis (new deposits: `eta_basis.py`, `eta_basis.log`)

- Self-contained window runs on the validated gated three-state core:
  r-windows empty at η = 0.3/0.5; (0.0096, 0.0144) at 0.7; (0.0083,
  0.0215) at 0.914; wider at 1.5/3.0. Window opens between 0.5 and 0.7;
  r = 0.02 inclusion threshold at η\* ≈ 0.85 (bracketed 0.83–0.86).
- Verdict: 0.914 is neither threshold nor a round E\*/N\*/τ₋ target —
  inherited illustrative baseline. Companion (paper4 v30) explicitly
  declares institutional coefficients uncalibrated, confirming the
  verdict. Manuscript: Appendix-A basis statement + §3.3 first-use
  clause + S9.2 run tables. All window claims bracketed at 0.914/3.0.

## Icelandic-cod calc audit (new deposits: `cod_audit.py/.log`, ICES CSVs)

- Re-derivation from ICES standardgraphs series (cod.27.5a key 22640,
  had.27.5a key 22494, current vintage): cod post-1995 SSB CV 0.394
  confirms manuscript 0.387 within revision noise (kept as stated).
- Haddock 0.143 is dead on every concept/window tested; corrected to
  0.24 (SSB, post-2013 own-HCR window — HCR adopted April 2013).
  Both manuscript comparisons preserved on the 2013 window: lower CV
  (0.24 < 0.39) and higher recruitment variability (0.68 vs 0.15).

## Lemma 2.2 seal + Proposition 2.1 demotion (E7, recovered primary text)

- E7's actual text was recovered from the review record before acting.
  The earlier reconstruction was inverted on the Lemma half (E7 says
  apply-or-drop, not don't-apply); the prior verify-and-record decision
  was superseded on evidence.
- Executed: Prop 2.1 → Remark 2.1; Lemma hypothesis 0 < 𝔰 < K stated;
  (ii) tightened (smaller root in (𝔰, S_h)); minimal qualitative §3.8
  application (seal predation as M_x-like extra mortality → threshold
  raised; directional, non-quantitative, no M_x estimated).

## I5 — data/code split

- Data availability now separates analysis datasets from analysis code
  in one sentence with two parentheticals; new deposits listed.

## §4.4(iii) + T_r-ranked test (new deposits: `tr_ranked_test.py`, `tr_table.csv`, `tr_test.log`)

- New S10: 42-stock T_r-ranked test executed (spec from recommendations
  memo; repo search confirms never executed before). Result: no
  window-approach gradient identifiable (all T_r ∈ {0.5, 1.0} below all
  windows — structural); T_r ≈ 1 dormancy holds (0/42 A, 1/42 B flags);
  sub-annual elevation is the ENSO confound (opposite direction).
- §4.4(iii) carries the cod-band illustration (10–15 yr inside
  9.9–20.3 yr, no institutional signature via criterion (iii)); §4.5
  opens with the executed-test pointer.

## Reproducibility

Builders `build_paper5_v37.py` / `build_paper5_supp_v13.py` regenerate
both files from v36/v12 with count-guarded edits. T_r test rerun after
import fix is bit-identical to the frozen log; η runs reproduce the
research values exactly.

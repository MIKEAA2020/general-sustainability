# Four-Part Sweep: Line-Level Scan, Version-Chain Content Audit, and Supplementary Alignment (2026-09-03)

Executed per the owner's four-part directive. Versions scanned (the finals at turn start):
P1 v10, P2 v4, P3 v15, P4 v14, P5 v13, E1 v6, E2 v11, E3 v7, E4 v8, plus the four
supplementaries (paper1_supplementary, paper3 v5, paper4 v3, paper5 v4).
New versions issued this turn: **P3 v16, paper3_supplementary_v6, P5 v14** (details in §5).

## 1. Hybrid placement (broader-fishery results) — implemented

- **Main text (P3 v16, §6.5.2):** the class-scope sentence now carries the executed
  comparison: 454-stock broad cohort, median 3.39 yr, the long-lived groups carrying the
  upper end (elasmobranchs 11.5 / sebastids 9.0 / pleuronectids 6.0 yr), and only 2% of
  random 43-stock draws at or below the class cohort's 1.79 yr. The version-sensitivity
  sentence is upgraded to the recovered protocol's exact values (v4.44: 415 / 2.57;
  v4.66: 454 / 3.39 — reproduced to printed precision under the recovered
  micro-specification).
- **Supplementary (paper3_supplementary_v6, S5):** the full comparison record — recovered
  protocol micro-specification, the 14-row taxGroup table (n, zeros, median, positive
  median, max), the overlap/vintage decomposition (33/43 extant ids; 10 dropped/merged;
  mean |ΔADH| = 3.44 yr; vintage counterfactual 2.79 → 2.34 yr), and the 10,000-draw
  null benchmark (2.12% broad / 0.29% forage-fish below 1.7902), with the descriptive
  (not hypothesis-test) status declared.

## 2. Granular line-level scan of all final versions — findings

Scan protocol (automated, per line, all 13 files): placeholder/TODO remnants; change-log
and process language (`previously`, `earlier draft/version`, `this version`, `now fixed`,
`reverted`, `bugfix`, `change log`, `pull request`, `this repo`); informal register
(`basically`, `obviously`, `of course`, `let's`, contractions, first-person casual,
exclamations, smileys); stray LaTeX remnants (`\cite`, `\ref`, `\label`, `\section` in
the markdown papers); `$`-balance per file; markdown-table pipe consistency; trailing
whitespace and double spaces; header numbering sequence; every "Section N" reference
resolved against actual headers; sentence-level and paragraph-level duplicate detection.

**Results: clean on every axis.**
- Zero hits for placeholders, change-log language, informal register, exclamations
  (all `!` are image embeds or math `\!`), smileys (the single hit is a colon in math
  `\mathcal O:D`), and stray LaTeX environments (the supplements' `\begin{pmatrix}` is
  the one legitimate math block, in S5's Jacobian display).
- `$`-parity even in every file; zero table pipe-mismatches; zero trailing whitespace.
- All "Section N" references resolve to existing headers in all nine papers (P5's
  headers use "## 1 Introduction" spacing, verified separately).
- One sentence-level duplicate: P1's priority disclaimer appearing twice — the known,
  deliberate echo (turn-52 scan already judged it legitimate: intro + §5.2 qualified form).
- Flow: the organization paragraphs (P2 §1.4, P3 §1.3, P4 §1.3) match the actual section
  lists exactly; the earlier P4 numbering defect fixed in v9 remains fixed in v14.
- "Committed"/"superseded" language occurrences are the established status vocabulary for
  pre-registered computational records (owner-directed), not change-log remnants.

**Verdict:** no line-level defect requiring a fix. No new versions were needed for this
part alone.

## 3. Version-chain content audit (latest vs every earlier version)

Method: for each of the nine chains, diffed the latest against *each* earlier version
(SequenceMatcher, blocks ≥ 180 chars, minus blocks whose head/tail reappear in the
latest), deduplicated — 55 unique candidate blocks. Every block was read and classified:

- **Present in upgraded form in the latest** (no loss): P1's equality/common-selector
  condition (v10 §3, now with the finite-enumeration remark), FAST/SLOW/STAGED witness
  rows, the FP_agg = I identity, the rescue-operation theorem (v10 §5.5 keeps the Aug_r
  map, the r* = 1−x formula, and adds a five-item data-requirements block); P2's
  viability-theory background (v4 §1 with Veliov 1993, estimation tubes, barrier
  certificates and citations), Theorem 2 (epistemic emptiness), Theorem 3's
  sampled-review reading absorbing the old Proposition 7, Theorem 1's proof (with the
  added δ-argument), and the five-mechanism taxonomy with its remedy mapping (v4 §6.4);
  P3's Theorem 3 proof bounds, Theorem 13 with the frozen-biomass face (v15's version
  adds the basal-mortality collapse remark), the groundwater and phosphate tables
  (v15's phosphate table adds the implied-production column and the Australian
  quarantine); P4's frozen-A proof (the V_A drift term legitimately absorbed into the
  hypothesis A(t) ≥ A_min), the no-Hopf theorem, the Euler monodromy, and the Figure-1
  caption (updated to the two committed campaigns); P5's flow-then-update convention
  (v13's pre-review/post-review form), the extra-loss threshold-shift lemma (richer:
  two cases + coalescence), the two-structural-reasons null explanation (with the
  operator-period distinction), the descriptive-partition statement; E1's retention-rule
  intro, E2's productivity finding (present in its corrected "vacuous robustness, not a
  productivity finding" form), E3's 0.39-ft margin statement (richer), E4's
  certified-level analysis (upgraded to the margins reading).
- **Deliberately superseded per the owner's directives** (correctly absent): P4's old
  lower-boundary two-fold narrative ([5.574, 5.576] basin collapse) and the old upper
  bracket [148.125, 148.438] — replaced by the certified single fold 5.5872362 and
  second fold 64.4023272 + capture-onset [148.6, 149.5] records.
- **Correctly removed meta text:** P4's v6 registration note with repository paths;
  the versioned supplementary-pointer paragraphs (each replaced by the current pointer).
- **Superseded caveat upgraded to a theorem:** P1's "no claim about the convex hull"
  (v3) → Theorem 8 (blend collapse) in v10.

File sizes grew monotonically on every chain (e.g., P3 94.6K → 128.8K), corroborating
the block-level verdict.

**Restorations confirmed present in the latest versions** (the analogy set): P3 v16's
elevator analogy (§1.1), P5 v14's budworm aside, P4 v14's hen/delay link, P1 v10's
orchard → Theorem 5(4). **Nothing to restore; no content loss found.**

## 4. Supplementary alignment — findings and fixes

- P1 v10 → `paper1_supplementary.md`: pointer correct; the listed extensions exist.
- P2, E1–E4: no supplementary files referenced — consistent (no supplements exist for them).
- P4 v14 → `paper4_supplementary_v3.md` (S1–S10): all ten sections exist; the main-text
  numbers match S1 (Hopf enclosures), S5 (the UNH proposition α+ηβ<1 and its status in
  Proposition 2), S9 (registration records), S10 (expanded proofs).
- P5 v13 → the supplementary description lists S1–S8, matching the v4 file's actual
  S1–S8 headers; the §3.7 citation "(Supplementary S4)" resolves correctly — the SAU
  battery record lives inside S4's Peruvian-anchoveta case record. **One precision
  mismatch fixed in P5 v14:** the main text's Chile Granger p = 0.0002 vs the battery
  and S4's 0.00016 → aligned to 0.00016.
- P3 → **pointer updated to `paper3_supplementary_v6.md` in P3 v16**, and every number
  the main text quotes from S5 (1.79/2.86; 2.57/3.39; 43/8; 35 positives) matches the
  v6 file exactly.

## 5. Files issued this turn

| New version | Built from | Changes |
|---|---|---|
| `paper3_material_ledgers_v16.md` | v15 | Hybrid broad-cohort citation (§6.5.2); exact protocol values 2.57/3.39; pointer → supplementary v6 |
| `paper3_supplementary_v6.md` | v5 | S5 extended: recovered protocol, taxGroup table, overlap/vintage, null-draw benchmark |
| `paper5_sampled_governance_v14.md` | v13 | Chile Granger p 0.0002 → 0.00016 (alignment with S4) |

Prior versions untouched. Scan/diff artifacts: `/tmp/scan/` (scan_report.json,
diff_latest_report.json; scripts scan.py, diff_extract.py — copied to
`analysis/scan_work/` for reproducibility).

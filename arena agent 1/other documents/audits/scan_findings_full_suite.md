# Deep Scan — Consolidated Full-Suite Findings (P1–P5, E1–E4) — 2026-08-30

Harness: `audits/numdiff.py` — significant-number multiset diff, official source vs
arena-agen1 rewrite (+ SI merged). Fixed this campaign: (1) the ID-stripper regex
`[A-Z]{0,2}\d{2,3}` ate pure integer prefixes of decimals (`[150.358…` →
`358…`); now `[A-Z]+\d{2,3}`. (2) SI files merged into the rewrite multiset
(P1, P3, P4, P5). Current full output: `audits/numdiff_full.txt`.
Per-paper detail for P1/P2/P4: `audits/scan_findings_p1p2p4.md`.

## Verdicts at a glance

| Paper | Verdict | Real errors fixed | Content restorations | Notes |
|---|---|---|---|---|
| P1 | CLEAN | 0 | 0 | extras = Steffen 2015 Science 347(6223):1259855 citation |
| P2 | FIXED | 0 | 3 | App. A (2 examples) + §5(d) Farkas alternative; audit template → P4 SI |
| P3 ×4 | FIXED | 0 | 3 sites | see P3 block below |
| P4 | FIXED | **1 (Theorem 3 Routh-array coefficient 0.2774 → 1.0682)** | 10 | all derived coefficients hand-verified |
| P5 | FIXED | 0 | 2 | constrained-M quantities + unrounded values restored |
| E1 | CLEAN | 0 | 0 | Rose-2026 engagement is the mandated ENGAGE addition |
| E2 | CLEAN | 0 | 0 | values = committed JSON; official's self-correction note correctly excluded |
| E3 | CLEAN | 0 | 0 | Table 3 = committed CSV exactly; sub-variant narrative present |
| E4 | CLEAN | 0 | 0 | tables = committed CSV/manuscript exactly |

## P3 block (four candidate files vs official manuscript_v2.md)

**Restorations applied this campaign:**
1. **US-reserves clause** ("US reserves have remained near 1,000,000 kt while
   cumulative production since 1996 is of order 600,000 kt") — was missing from
   ALL FOUR mains. Added to paper3_material_ledgers.md,
   paper3_material_ledgers_v2.md, paper3_material_ledgers_reconstructed_v2.md.
2. **Non-reduction boundary block** (the official's five-reason no-reduction
   statement incl. the support flux ω_A(A^{eq,W}−A^{act,*}) = 4.652133… stock
   units/yr) — was missing from the reconstruction line only (present in main +
   v2). Restored into paper3_material_ledgers_reconstructed_v2.md, together with
   the hand-off projection and the frozen-donor limit blocks (theorem refs
   adapted: official Thm 3.11 → recon Thm 5; 3.13 → Thm 7).
3. **Companion working-point sentence** (89.526, 397.87, E*≈2.090, R*=qE*N*≈0.187)
   — verified PRESENT in all current files (the harness flagged a count
   difference: the official repeats 0.187 in its registry).
4. **ψ-pairs** (soil zinc 0.85/0.25; pollinators 0.70/0.20; factor ≈1.5) —
   retained in the shared SI (paper3_supplementary.md) with full routing
   discipline; the reconstruction's pointer to the SI is accurate. No action.
5. `10.5880` = fragment of the G3P DOI 10.5880/G3P.2024.001 in all four files —
   benign citation, not a value.

**Canonical-file decision (still open, for the user):** the current corrected
line is paper3_material_ledgers_v2.md (main lineage) and
paper3_material_ledgers_reconstructed_v2.md (reconstruction lineage, now
complete after restoration 2). The superseded files
(paper3_material_ledgers.md, paper3_material_ledgers_reconstructed.md) were left
untouched per the never-overwrite directive except the one-clause factual fix in
the main file. Remaining harness noise on all four: official section-numbering
(§2.5, §3.5, §5.5, §9.x), count differences vs the official's internal registry.

## P5 detail

Restored: (1) constrained-M quantities (crash M=0.46, F=1.37, unreported catch
257.8 kt/yr = 102.5% of mean SSB; non-recovery M=0.43, F=0.25, 3.7 kt/yr —
reproduction targets); (2) the unrounded-value disclosure (381.95, 101.05,
30.55 kt). Verified present: the full assessment table (M 1.002–0.278 and the
ten survival values — I hand-checked all ten exp(−M) roundings: 0.367, 0.109,
0.076, 0.097, 0.750, 0.711, 0.488, 0.696, 0.750, 0.499, 0.757 — all correct),
the community-level table (all per-community percentages in the SI), Tam & Bundy
49,600→161,183 t / 13.77→4.97 t km⁻² (main + SI), Icelandic CVs 0.387/0.143,
anchoveta |r|≈0.31, Sheridan R²≈0.47, RAM v4.66, power 0.02–0.14.

## E-papers detail

- **E1:** Table 6 (M2/M3/M4 rows with 0.25) identical to the official's table.
  My 0.3/0.25-Mt LRP-drift numbers come from the Rose (2026) engagement — the
  novelty-sweep-mandated addition; the official v2 does not discuss Rose 2026.
  Rose citation VERIFIED this campaign: Can. J. Fish. Aquat. Sci. **83**, 1–14,
  DOI 10.1139/cjfas-2025-0141 (published 27 Jan 2026) — the placeholder page
  range was correct; DOI now added to the E1 and P5 reference entries.
- **E2:** my r-sequence (460.0, 990.5, 1602.1, 3120.5, 6385.9) matches the
  official's committed intervention_results_v2.json exactly (a_max=1.1531,
  460.029/990.467/1602.092/3120.507/6385.924) — mine are faithful roundings of
  the committed artifact; the official manuscript itself rounds to 460/3121/6386.
  The official-only 1456/2335.4 are its internal self-correction note about an
  earlier committed table value — change-log content, correctly excluded; the
  corrected fixpoint 2338.3 is used.
- **E3:** Table 3 matches fixed_window_scores.csv to the displayed precision
  (e.g. persist 23.7475→23.75; M2 18.1053→18.11; oracle 19.6916→19.69). The
  climate-module sub-variant narrative (M2_Renso/M2_Rprecip/M2_Rar/M2_combo,
  24.30/28.67/24.70, 22.03/23.03/23.94/25.71, 14.52/14.67/16.01/16.57; oracles
  18.16/10.98/9.75) is carried in §5.4-equivalent. Correlations 0.17/0.78/0.41
  present; Umphres & Choi (2025) with DOI 10.5066/P1BI62NY present in the data
  statement; TWDB well 6837203 present. 12.28 is official-provenanced (its own
  M2m table row).
- **E4:** supply table (282.16/253.94/225.73/197.51/262.36/254.93) matches the
  official manuscript exactly; kernel boundaries 618.8/625.6/658.4 match the
  committed intervention_boundaries_v2.csv (618.777/625.591/658.425); crossover
  12.7 and T=12 boundary 692.6 present; 21.81/15.41/169.29/+50.6%/+16.2%/3.3/8.4
  all official-provenanced. The official's "the first edition's ≈14 was
  inconsistent" fragment is change-log content — correctly excluded.

## Forbidden-content exclusions (verified correct)

- Official P2's "≈27.2k words" word-budget meta — excluded.
- Official E2's 1456/2335.4 self-correction note — excluded (corrected value used).
- Official E4's "first edition's ≈14" note — excluded.

## Cross-paper delegations (harness-invisible, documented)

- P2 Props 10.3/10.4 (audit template, 0.573 bound) → paper4_supplementary.md S8.
- P2 App. A.3 moiety remark → retained in both P3 main-lineage files.
- P5 community-level table → paper5_supplementary.md S6 (main defers).
- P3 ψ-pairs → shared paper3_supplementary.md (reconstruction defers).

## Remaining open items

1. **P3 canonical-file decision** — user's call between
   paper3_material_ledgers_v2.md and paper3_material_ledgers_reconstructed_v2.md
   (now content-complete).
2. Rose 2026 page range — RESOLVED (verified 83, 1–14; DOIs added).
3. Per-manuscript checklists and final venue passes — the last remaining
   milestone items, unstarted.

## Files changed this campaign

- audits/numdiff.py (regex fix; SI merge; P3×4 + P5 + E1–E4 pairs)
- audits/numdiff_full.txt (full current output)
- paper4_delay_dynamics.md + paper4_supplementary.md (see scan_findings_p1p2p4.md)
- paper2_obstruction_calculus.md (Appendix A; §5(d); Farkas/Gale refs)
- paper5_sampled_governance.md (constrained-M; unrounded values; Rose DOI)
- paper3_material_ledgers.md, paper3_material_ledgers_v2.md,
  paper3_material_ledgers_reconstructed_v2.md (US-reserves clause; reconV2:
  interface block)
- paperE1_cod_forecast_ladder.md (Rose DOI)

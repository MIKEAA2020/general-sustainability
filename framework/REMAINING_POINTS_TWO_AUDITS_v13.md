# Remaining Points from the Two Audits — Gap Register, Adjudication, Implementation Plan (v13 → v14)

**Date:** 2026-09-13
**Audits:** qwen + claude, both inside `uploads/audit of framework v12.txt` (qwen lines 1–515, claude lines 516–940).
**Decision record:** `framework/JOINT_EVALUATION_TWO_AUDITS_v13.md` (C1–C15 adjudicated, implemented in v13).
**This register:** cross-checks every point of both audits against the actual v13 text (`framework/paperF1_retention_framework_v13.md`, grep-verified) and against the extracted source CSVs (`wave_e_cod/results/`, `wave_e_edwards/results/`), adjudicates what remains, and fixes the implementation order so no edit is made before its contradictions are resolved.

---

## 1. Answer to the question

**Yes — the remaining points from the two audits are implemented via the joint evaluation, but only after adjudication.** That is already the established discipline in this workspace (v11→v12: `CONTRADICTORY_POINTS_ADJUDICATION.md`; v12→v13: `JOINT_EVALUATION_TWO_AUDITS_v13.md` §1). This register extends the same discipline to what is left. Implementation target is the **paper** (v14); the joint evaluation is the decision record that v14 must implement.

**What v13 already fixed (verified, no action needed):** −48.65% → −48.52% (8 occurrences, 0 left); +41.55%/+43.99% → +41.50%/+43.98% (0 left); D5 0.025 → 0.015–0.030/mean 0.0225; "17.09% smallest" → 9.01%; band 12.57/20.05 ft per horizon; post-hoc band disclosure (3×); class-grounds pre-gate note; strictly >5% (5×); 4 cells 800 passes; Table 2b identified; oracle h=5 row added; k_param/k_decay disambiguation; "240 daily" floor; M4 collapse-window scoping; sign-convention fix; Table 5 separator fix; delay-vs-model-cost fix.

**What remains is non-trivial:** ~20 unadjudicated points, of which **three are data-backed contradictions the v13 joint evaluation did not catch** (§2), plus claude's registered upgrade list (§3) and several unflagged items (§3).

---

## 2. Discrepancies between the v13 joint evaluation record and v13 itself

These must be resolved **before** any implementation, because the record currently claims things the paper does not contain (or the archive does not support).

### D1 — "M2m h=5 also separated" is not in the archived uncertainty layer

- The C7 adjudication text and v13 prose say "h=5 M2m and training mean also separated."
- `wave_e_edwards/results/e3_audit_uncertainty.json` contains **8 DM tests only**: h=1 M1/M2m/M2 vs persist, M2m vs M1, h=5 naive_mean vs persist (CI [−9.72, −2.085], excludes zero), h=5 M1 vs persist (covers zero), and two pass-2 climate comparisons. **There is no M2m vs persist h=5 test.**
- Table 4's M2m h=5 Uncertainty cell shows "—" — consistent with no archived interval.
- **Adjudication:** the claim "h=5 M2m separated" is unsupported as stated. Either (a) compute the missing block-bootstrap CI from `wave_e_edwards/results/rolling_forecasts.csv` (per-origin h=5 obs/pred are archived; `src/e3_audit_uncertainty.py` exists in the release zip, not yet extracted), or (b) amend v13/v14 to claim only the archived separation (naive_mean vs persist h=5). **Decision needed before touching §5.2/Table 4.** Default if silent: (a) compute, then single-pass edit.

### D2 — "MAE tie with values 10.72 vs 10.73" claimed fixed but values absent from v13

- The joint evaluation's implemented-list says the MAE tie now carries values 10.72 vs 10.73. v13 contains "MAE tie" three times, **never with values**.
- The values are real: `wave_e_edwards/results/rolling_summary.csv` M1 h=1 MAE = 10.7166, naive_persist h=1 MAE = 10.7289 (Δ = 0.0123 ft). The evaluation's numbers are right; the paper just never received them.
- **Adjudication:** trivial, uncontested — insert once (qwen 4.23 / Table 4 issue 4).

### D3 — `sim_retention_power.csv` retained counts do not reproduce the §4.3 power cells

- §4.3 publishes D1 0.965/0.985, D2 0.710/0.130, D3 0.090/0.110, D4 0.005/0.015, D5 false-retention 0.015/0.030.
- The archived CSV's `retained=True` counts per cell (n=200) are: D1 194/199 (0.970/0.995), D2 144/28 (0.720/0.140), D3 104/123 (0.520/0.615), D4 77/14 (0.385/0.070), D5 4/6 (0.020/0.030). **None of the published rows matches any straightforward reading of this column** (full rule, baseline-only, one-horizon: all differ).
- **Adjudication:** pin the semantics of `retained` and the file the §4.3 table was actually computed from (candidates: a gate-variant column, a different archived CSV, a post-v13 rerun). Requires `wave_e_cod/src/run_ladder.py` + the campaign code (in the release zip, not yet extracted). **No Monte-Carlo-error/Wilson work (claude 3.4) may proceed until this is pinned** — computing CIs on an unidentified column would silently contradict the published table.

---

## 3. Gap register — every remaining point of the two audits

Status: ✓ fixed in v13 (verified) | P partial | R remaining | RG registered for future work in the joint evaluation | NEW not registered.

### qwen audit

| ID | Point | Status |
|---|---|---|
| 1.1–1.22 | 22 major inconsistencies | ✓ all in C1–C15/implemented list (verified) |
| 2.1–2.3, 2.5–2.7 | numerical checks | ✓ fixed (verified) |
| 2.4 | M1b diff "0.0358" — true value 0.0359 (114.8024−114.7665) | R — micro-fix, still 0.0358 in v13 |
| 2.8 | p=0.000 → report `<1/B` | ✓ p_perc language in place |
| 3.1–3.2 | band versioning; class-grounds | ✓ C1/C11 |
| 3.3 | state whether the rule is *recommended* or merely the pre-registered instrument | P — "stated plainly" but recommendation question open; ties to AD7 |
| 3.4 | M3/M4 no power estimate | ✓ #19 scoped |
| 3.5 | specificity in-class scoping | ✓ #18 + scoping |
| 3.6 | climate modules under an *alternative* comparator? | P — "kink acknowledged" but the counterfactual is unanswered |
| 3.7 | justify why climate modules are not iterated at h>1 | P — stated, not justified |
| 3.8 | fixed-window vs 15-year floor labelling | ✓ |
| 3.9 | origin-set sensitivity discussion | P — capelin example present; explicit sensitivity statement thin |
| 3.10 | why persistence remains the decision baseline when training mean beats it at h=5 | R — not addressed anywhere in v13 |
| 4.1–4.9, 4.12–4.28 | ambiguous statements | ✓ mostly; **R: 4.10 "printed on primary passes"** (still unglossed), **4.11 "moratorium"** (still undefined), **4.18 "bold 193"** (still present ×2), **4.23 MAE values** (see D2), **4.24 "17.64"** (still unglossed — iterated M2m h=5) |
| 5 Table 2-2, 3-2 | rank fix; Spec B "Yes several margins" vagueness | ✓ / P (identify which margins or cite table) |
| 5 Table 4-2, 4-4 | M2m h=5 uncertainty; MAE support | R — see D1, D2 |
| 5 Table 5-2 | comparator band 0.95×12.8391 = 12.1971 not shown | R — micro-fix |
| 6.7 | abstract should mention IC does not enforce h=5 requirement | P — partially; fold into AD7 |
| 7 §5.2 | Edwards missing h=5 oracle row | ✓ added |
| 8 | Table 2b / power map / climate table / M4 / Q / tail failure / moratorium / safe set | ✓ all except climate-module table (covered by claude 2.3 inventory, RG) |
| 9 | typos incl. Makridakis 2020 cited? | P — Makridakis in References only, no in-text citation; "fibre" phrasing |
| Appendix | AIC vs "information criterion n log MSE+2k" wording | R — one sentence to reconcile |

### claude audit

| ID | Point | Status |
|---|---|---|
| 1.1–1.5, 1.7, 1.10–1.11 | arithmetic defects | ✓ verified fixed |
| 1.6 | **K lower bound "50.8 general" incompatible** | R — **data-backed adjudication in §4-AD1; the claim is wrong as written** |
| 1.8 | alt-comparator +29.3 vs interval midpoint +7.6; verify statistic | R — needs the archived alt-comparator run; do not edit numbers until verified |
| 1.9 | M4 worst raw RMSE vs M2 1058.9 | ✓ scoped to collapse window |
| 1.12 | "bold 193 marks winner" leftover, twice | R — delete (also qwen 4.18) |
| 2.1 | algorithm box pre-gate reorder | P — v13 kept the check inside the retained branch with a note; claude wants the actual reorder (0) class → H2 → H1 → H3. Safe one-paragraph change; adopt in Phase A |
| 2.2 | ladder is a tree, not a chain | R — not adopted; one sentence repairs §2.1–§2.3 |
| 2.3 | model inventory table (comparator map complete) | RG — adopt as Phase A text table (no new computation) |
| 2.4 | "< chance (20%)" category error | R — the D3 row still reads "< chance (20%), below bar"; chance retention is 0.005/module → D3 0.090 is 18-fold enrichment. Keep the valid "3.8% best-ranked vs 20%" comparison; delete the retention-vs-20% one |
| 2.5 | per-cell 80% bar ("2 of 8 cells clear"; specificity 2/2 in-class, 0/4 misspecified) | R — v13 keeps the scalar framing; additive fix |
| 2.6 | D6/D7 "false retention" → mechanism misattribution + predictive-gain column | R — adjudicated in §4-AD2 (rename is pre-registered vocabulary; adopt claude's sentence + column) |
| 3.1 | smoothed predictand: §6 inference + third audit status "revised" + decisive experiment | P/R — status class and §6 sentence are text-only (Phase A); experiment is RG |
| 3.2 | reproducibility ±3.8% is the same order as the 5% band; gate slack 0.67pp; no Edwards reproducibility figure | R — **adjudication in §4-AD3; text caveat now, rerun later** |
| 3.3 | SNR normalization; power curves on common SNR axis | RG |
| 3.4 | MC error, Wilson intervals, paired comparisons | R — **blocked by D3 until `retained` semantics pinned** |
| 3.5 | coarse regime handicaps M2; state why coarse is pre-registered primary | P — add one justification sentence or the rationale statement |
| 3.6 | identification-failures subsection; effective-parameter count vs IC penalty | R — partially present (profile-likelihood sentence); collect into §2.1.1 |
| 4.1 | LR evidential-weight table (D4 low-σ LR=1.0) | RG — **text-only, from existing §4.3 numbers; highest-payoff upgrade; Phase A** |
| 4.2 | calibrate the band by simulation ("pre-register the operating characteristics, not the threshold") | NEW — **adjudication §4-AD4: new rule version for a future cycle, NOT a v14 retro-fit** |
| 4.3/4.4 | uncertainty-aware gate + hybrid IC+H2/H3 rows in §4.5 | RG — new runs required; disclose as post-hoc rows |
| 4.5 | pre-check candidates (inner-loop pseudo-OOS index; training-window profile curvature) | NEW — register as campaigns; cheap and falsifiable |
| 4.6 | MCS + forecast encompassing | RG — **adjudication §4-AD5: context diagnostics only, not verdict instruments** |
| 4.7 | run T=71 | RG — campaign |
| 4.8 | scale reporting SD(target), SD(Δtarget) in Table 1 | RG — text-only, needs SDs from the series (cod panel available; Edwards head series needs the J-17 file) |
| 4.9 | per-regime skill decomposition | NEW — campaign |
| 4.10 | prospective registration subsection | NEW — text-only; freeze model set + next origins |
| 5 | compression: Appendix verification block → paths+checksums; repeat cuts; "Two systems share nothing physically" → "share a scalar stock with forced flux"; notation table; "Retention per specification" fragment; §5.1 subheadings; Table 3 per-row intervals | P/R — adopt the non-destructive items in Phase A |
| §0 | reframe: deliverable = minimum reporting standard for non-retention claims; rule = worked example | NEW — **owner-gated; adjudication §4-AD6** |

---

## 4. Adjudications — contradictions resolved BEFORE implementation

### AD1 (claude 1.6) — K lower bound: claude upheld; v12/v13 wording wrong. **Data-backed.**

Computed from `wave_e_cod/data/ncam_2016_table_a2.csv` (fetched from the repo, the exact input series named in `wave_e_cod/results/meta.json`):

| Window | max predictor SSB (kt) | K lower bound = max+10 |
|---|---|---|
| 1983–1989 (origin-1990 train) | 940.75 (1987) | **950.8** |
| 1995–2007 (recovery train) | 40.83 (2006); 2007's 81.1 is the terminal state and never a predictor state | **50.83 ≈ "50.8"** |

- **Correction recorded 2026-09-13 (before the Phase A edit):** `run_ladder.py` L82 (`np.max(S0)+10` over the predictor states of training transitions) + E1 v20 A6 wording ("maximum over predictor states of the training transitions, excluding the terminal state") show the earlier "recovery-window ≈91.1" figure was **wrong**: 81.1 (=2007) is the terminal state and is excluded. The recovery-window bound is 50.83 (predictor-state max 40.83 in 2006). Do not reuse 91.1 anywhere.
- v13's "lower bound 50.8 kt general" is wrong as labelled — 50.8 is the recovery-window (per-origin) bound, and the "≈91 kt on recovery window (max_train S≈81 kt)" half is wrong too. Both halves replaced in Phase A with the E1 v20 wording and the data-verified figures (950.8 / 50.8).
- This also dissolves claude's "incompatible" objection: the 670 kt collapse-window RMSE and D1 K=1032.7 are consistent with pre-collapse SSB ≈ 700–940 kt; the 50.8 figure never implied a 40.8 kt global training max.

### AD2 (claude 2.6) — D6/D7 naming. No auditor contradiction; the conflict is with the paper's own pre-registered vocabulary.

- Renaming "false retention" to "mechanism misattribution" across the pre-registered DGP table and abstract would edit row labels of a frozen table. Adjudication: **keep the pre-registered label**, add claude's framing as a sentence + column: "retention licenses a prediction claim, never a mechanism claim; D6/D7 measure the gap between the two" and a realised-predictive-gain column once the per-replicate gains are archived (D3-dependent).
- No opposing-revision risk if done in one pass with AD3/AD5 text fixes.

### AD3 (claude 3.2) — reproducibility vs the band. The one point that could overturn a headline claim.

- Cod's own numbers: ±17 kt on 445.5 = 3.8% environment sensitivity vs a 5% band; the load-bearing decision (M2m 4.33% vs 5%) has 0.67pp slack; no Edwards reproducibility figure exists.
- Adjudication: cannot be resolved by text alone. **Do not** reword §6's "gates are load-bearing" claim silently (either direction would be an unadjudicated overwrite). Directive: add the tolerance sentence now ("the load-bearing gate decision sits within numerical tolerance of the environment sensitivity measured on cod; an Edwards cross-environment figure is required and registered"), and register the Edwards rerun as a campaign. If the rerun shows sensitivity ≥0.67pp, the claim must be downgraded — a single coordinated edit, not patches.

### AD4 (claude 4.2) — band calibration. Direct conflict with the just-adjudicated C1 framing.

- "Pre-register the operating characteristics, not the threshold" would supersede the 5% band — overwriting the C1/C7 fixes ("algorithm box is unified rule", band values 12.57/20.05) that were adjudicated this week. That is exactly the opposing-revision pattern to avoid.
- Adjudication: 4.2 is the **prospective replacement rule**, to be designed by simulation on the same harness and adopted in a future version with its own pre-registration statement. v14 adds one sentence: "a simulation-calibrated band targeting power ≥0.80 / specificity ≥0.90 at the object's own T and SNR is registered as the prospective replacement." Nothing about the 5% band changes in v14.

### AD5 (claude 4.6) — MCS/encompassing vs the DM posture.

- v13 (A1) adjudicated: "paper declines to rest verdicts on DM; DM relabelled descriptive loss-differential diagnostics." Adding MCS as a verdict instrument would contradict that posture; adding it as *context* ("can these data distinguish these models at all?") does not.
- Adjudication: MCS/encompassing enter as **context diagnostics, never gate inputs**, with the same descriptive label; report "indistinguishable" vs "worse" as distinct outcomes.

### AD6 (claude §0) — the reframe. Owner-gated, and the only item that changes the paper's stated contribution.

- Reframing the deliverable as "a minimum reporting standard for non-retention claims" (rule as a worked example) resolves qwen 3.3 and converts the IC-dominance result into an asset. It also contradicts the title, abstract, §7 and §8 as written — so it must be executed as **one coordinated rewrite of §1/§7/§8 (+title/abstract) or not at all**.
- Adjudication: recommend adopting; implementation waits for the owner's decision and is then a single-pass rewrite, never incremental patches.

### AD7 (qwen 3.10) — persistence as decision baseline.

- No contradiction between auditors; the paper must simply answer the question: persistence remains the decision baseline because it is the pre-registered H2/H3 anchor, and training-mean superiority at h=5 is reported as evidence about the baseline choice, not as a re-baselining. One sentence in §5.2.

---

## 5. Implementation plan — phases, each one a single coordinated pass

**Rule inherited from this workspace:** adjudicate (§4) → then implement each phase as one pass over the paper → version bump once per phase. Never implement point-by-point against a moving target.

- **Phase A — text-only, uncontested fixes → v14.** **DONE 2026-09-13** — applied as one asserted pass (41 replacement rules, grouped into 37 changelog rows) to `framework/paperF1_retention_framework_v14.md`; verification: all old strings gone, all new present, `journal_style_automated_scan.py` → 0 blockers. Applied: D1 (computed M2m h=5 CI [−5.76, −2.19], inserted; M2m h=1 CI from the archived layer), D2 (MAE values 10.72 vs 10.73), AD1 (K bound sentence — corrected both halves), AD2 sentence, AD3 tolerance sentence + AD7 baseline sentence, AD4 prospective-band registration sentence (§4.5; registration only), claude 2.1 reorder, 2.2 tree sentence, 2.3 inventory table, 2.4 chance fix, 2.5 per-cell sentences, 3.1 "revised" status + §6 candidate-mechanism phrasing, 4.1 LR table, 4.8 scale reporting (SDs computed: cod 356.5/89.5, Spec B 423.2/89.6, Edwards 14.70/12.34), qwen 2.4 (0.0359), 4.10/4.11 glosses, 4.18 (deleted bold 193), 4.24 (gloss 17.44/17.64), Table 5-2 (12.1971), AIC reconciliation, Makridakis cite, 3.5/3.6/3.7/3.9 justification sentences, compression items (claude 5 subset: 4 grammar/fragment fixes), N2 wording, N3/AD8 dated note, N4 32-row reconciliation, N5 archive paths, N1 provenance note. Full mapping: `framework/PHASE_A_CHANGELOG_v13_to_v14.md`. See §8.
- **Phase B — owner decisions before any edit.** **DONE 2026-09-13** — decisions collected interactively: AD6 adopt fully (title/abstract/§1/§7/§8 reframed in one pass — the deliverable is a minimum reporting standard for non-retention claims, rule as worked example), AD2 option (a) (frozen labels kept, prose rename to "mechanism misattribution", Table 2b gained a "Row measures" column), AD4 option (b) (prospective band reworded: future applications only, never re-opens reported verdicts). Applied as one asserted pass (25 replacement rules) to `framework/paperF1_retention_framework_v15.md`; verified idempotent, style scan 0 blockers. Decision record: `PHASE_B_ROOT_CAUSE_DECISION_MEMO.md`; mapping: `PHASE_B_CHANGELOG_v14_to_v15.md`.
- **Phase C — computational campaigns** (require extracting `wave_e_cod/src/`, `wave_e_edwards/src/`, `data/`): T=71; smoothed-predictand experiment; SNR power curves; uncertainty-aware gate + hybrid rows; MCS/encompassing; per-regime decomposition; Edwards reproducibility rerun; D3 provenance pin (read `run_ladder.py`); M3/M4-as-truth cells (optional); pre-check candidates (4.5). **IN PROGRESS 2026-09-13** — harness in `phase_c/` (adaptations only: estimator/map/scorer imported from `wave_e_cod/src/run_ladder.py`; seeds pinned with `PYTHONHASHSEED=0`; every CSV paired with a `_provenance.json` recording shas, versions, wall time). Running: `campaign_power.py` (D1–D5 × {11.8, 33.8}; 200 reps for D1/D5 per the frozen sheet, 100 for D2/D3/D4 — Phase C scaling decision, binomial CIs reported honestly) + `campaign_smoother.py`; `campaign_misspecified.py` (D6/D7 at 100 reps, T=71 D1/D5 at 50 reps — the author's 200/200 design was benchmarked at ~10 h and is registered as a longer campaign). **DONE 2026-09-13** — full results in `phase_c/PHASE_C_RESULTS.md`, changelog `PHASE_C_CHANGELOG_v15_to_v16.md`, applied as `apply_phaseC_v15_to_v16.py` (25 asserted rules) → `paperF1_retention_framework_v16.md` (68,918 chars, 454 lines; verified idempotent, style scan 0 blockers). Campaigns (all pinned-seed, provenance-archived): Edwards rerun — all six archived specs exact + D1 citation cell exact (margin −3.6607, z=−3.284, p=0.0016); power campaign D1–D5 (n=200/100) → §4.3 reproduces: 12 cells PASS, 2 marginal (D1-σ33.8 0.960 vs 0.985, D2-σ33.8 0.060 vs 0.130 — verdicts unchanged, replaced in v16); D6/D7 n=30 PASS with AD2 gain (retained modules beat persistence in 100% of retention reps, mean +2.6…+9.4 kt h=1); T=71 first execution n=10 (D1 0.900/1.000, D5 0.000/0.000) replacing all "not executed" sentences; smoother test: assessment-like 3-yr smoother compresses M1 margin 7–13× and cuts D1 power 0.90/1.00→0.63/0.67 (real, not sufficient alone — §6); SNR sweep: D1 flat 0.88–1.00 over σ∈{5,20,45}, D3/D4 0.00 even at σ=5 (identification limit structural); uncertainty gate + hybrid + MCS disclosed as §4.5 post-hoc rows (gate power D1 0.64, specificity D5 1.00/0.96; MCS never eliminates persistence); per-regime decomposition (no verdict flips); D3 provenance pinned (M2 error spikes 33× at the 1991–92 catch-regime transition; §4.6 third pre-check candidate); mean-power 0.376 provenance resolved (fresh 0.373). M3/M4-as-truth cells: optional — skipped, noted in v16 as remaining registered work.
- **Phase E — journal formalization → v17.** **DONE 2026-09-13** — user directives: never overwrite versions; reference companion papers (Abaee 2026a/b) but never superseded manuscript states; no changelog/diary/meta commentary or informal register; no naive over-hedging (legitimate scope statements kept); scan for navigation/self-description patterns; scan for lost scientific/pedagogical content. Applied as `apply_phaseE_v16_to_v17.py` (75 asserted rules) → `paperF1_retention_framework_v17.md` (69,282 chars, 455 lines; idempotent; style scan 0 blockers). Single authoritative number set from the pinned-seed campaign (D1 0.955/0.960; D2 0.780/0.060; D3 0.110/0.100; D4 0.010/0.010; D5 0.995/0.950; D6 0.633/0.733; D7 0.933/0.867; T=71 0.900/1.000, 0.000/0.000; wrong-module 0.034; null 0.0055; mean power 0.373; verdicts unchanged). New automated guards: `journal_formalization_scan.py` (v17 → 0 flags) and `content_coverage_scan.py` (all v0/v13 numeric claims covered; 30/30 domain terms present — no lost content). Changelog: `PHASE_E_CHANGELOG_v16_to_v17.md`.
- **Phase D — prospective registration subsection** (claude 4.10) — freezes model set and next origins; pairs with AD4. **DONE 2026-09-13** — v18 pass (22 asserted rules): remnant/redundancy scan (new `redundancy_scan.py`; v17 had 91 findings incl. the §6 table row still carrying pre-Phase-C numbers — fixed; v18 → 0 findings) + new §4.7 Prospective registration (model set frozen; next origins: Edwards 2024–2033, cod Spec B 2025+ per new xteNCAM vintage, Spec A closed; AD4 band-calibration procedure made operational; never re-opens reported verdicts; §4.5/§1/Data availability cross-referenced; Amendment-1 length-sensitivity check appended to §4.3 — satisfied: |Δ| 0.055/0.040). Verification: formalization 0 flags, redundancy 0 findings, style PASS, coverage clean, idempotent. Changelog: `PHASE_D_CHANGELOG_v17_to_v18.md`.

## 6. Evidence needed from the owner / next pulls

1. ~~The CSV/script behind the §4.3 power table (D3)~~ — `run_ladder.py` reviewed; L82 K-bound semantics pinned (`np.max(S0)+10` over predictor states). Remaining for Phase C: owner confirmation that the `tools/sim_retention_power.py` / `tools/sim_misspecified.py` generators reproduce the published §4.3 rates, so the replacement CSVs can be archived (D3/N1).
2. Confirmation on Phase B decisions (AD6 reframe, AD2 rename, AD4 wording).
3. ~~`wave_e_cod/data/` + `wave_e_edwards/data/` for SD reporting (4.8)~~ — fetched; SDs computed (356.5/89.5, 423.2/89.6, 14.70/12.34) and now in v14.
4. Edwards cross-environment rerun (AD3) — `wave_e_edwards/src/` + data both fetched; the rerun itself is a Phase C campaign.

**Bottom line:** the two audits are fully traceable; the defect-class points are implemented in v13; what remains is ~20 points, of which three are real contradictions that this register adjudicates (one data-backed, claude upheld on the K bound), and none may be implemented until the adjudications in §4 are accepted. Implementation then proceeds phase-by-phase, one pass per phase, no overwrites.

---

## 7. Addendum — previously unscanned locations scanned (2026-09-13)

Sources brought in for this pass (minimum set for audit checks): `wave_e_cod/` and `wave_e_edwards/` SPECIFICATION v1–v4, protocols, admission memos, full `src/` trees and result CSVs; `specifications/`; `uploads/audit of framework v12.txt`, `uploads/framework audits.txt`, `uploads/last message.txt`, `uploads/paperF1_retention_framework_v0.md`; `audits_E1_E3/source_audits/*.txt`, `wave6/`, `e1_audit_2026-09/*`; `arena_agent_1/…/rerun_campaigns/` (e1/e3), `_scan_work/` (E1/E3), `joint_assessment_wave2/3/grok_reviews/wave5/open_items`, `E1_TIER3_RESTRUCTURING_PLAN.md`, `E1_V20_CHANGELOG.md`; `agent 2 productivity illusion/analysis/*`, `TRANSFER_AUDIT_RESPONSE.md`; data inputs from main (`ncam_2016_table_a2.csv`, `annual_panel.csv`, EAA discharge, USGS recharge, capelin/catch/landings).

Full findings are incorporated in `JOINT_EVALUATION_TWO_AUDITS_v13.md` §5. Effects on this register:

- **§2 D3 (simulation provenance):** RESOLVED — the verification transcript proves the published §4.3 computation and the release-zip CSVs fail to reproduce it (N1). Phase C item changes from "pin `retained` semantics" to "replace or disclose the archived CSVs"; `run_ladder.py` review still scheduled for the replacement-run spec.
- **§4 AD1 (K bound):** STRENGTHENED — E1 v20 A6 supplies the authoritative wording ("maximum over predictor states of the training transitions, excluding the terminal state"); Phase A adopts it (N2).
- **New AD8 (frozen-spec wording, N3):** v13's "4 cells 800 passes" corrects `SPECIFICATION_v4`'s frozen "eight cells, 1,600 passes" without recording the divergence. Phase A: dated note in §4.3/Data Availability (no numeric change), or amend the sheet. No opposing-revision risk; single edit.
- **New alignment item (N4/N5):** DM-row count "5 of 32" verified against the archived CSV; reconcile with E1 v20's "four of the twenty-eight" or state the criterion; fix the `e1_dm_uncertainty.csv` archive path in Data Availability. Both Phase A.
- **New caveat (N6):** "all surviving points implemented" is as-of-verified, not exhaustive (precedent: E1 round-2 evaluation was found non-exhaustive by its own Tier-3 plan). Attach to the joint assessment record; no paper edit.
- **Phase A gains four confirmed-fix items** (N2, AD8, N4-alignment, N5) plus the D1/D2/AD2/AD3/AD7/2.1/2.2/2.3/2.4/2.5/3.1/4.1 list already in §5. Nothing else from the newly scanned locations changes the phase plan; no valid framework-relevant point was found that contradicts an existing adjudication.

---

## 8. Phase A outcome (2026-09-13)

- **Artifacts:** `paperF1_retention_framework_v14.md` (62,408 chars, 450 lines; +18 lines ≈ +4.2% vs v13's 432) produced from the untouched v13 by `apply_phaseA_v13_to_v14.py` (40 asserted replacement rules; a re-run reproduces v14 byte-for-byte). Mapping: `PHASE_A_CHANGELOG_v13_to_v14.md`.
- **Verification:** every old string confirmed absent, every new string present; `journal_style_automated_scan.py` on v14 → 0 blockers, PASS. v13 untouched.
- **Computed this phase and used in v14:** D1 M2m h=5 DM test (margin −3.6607, z=−3.284, p=0.0016, block-bootstrap CI [−5.7637, −2.1862], archived as `wave_e_edwards/results/e3_audit_uncertainty_add_M2m_h5.json`); M2m h=1 CI [−1.445, −0.676] (archived layer); SDs for scale reporting (Spec A 356.5/89.5 kt n=33; Spec B 423.2/89.6 kt n=71; Edwards 14.70/12.34 ft n=90); K bounds 950.8 (1987) / 50.8 (2006, terminal state excluded).
- **Discrepancies closed:** D1 (interval now in Table 4), D2 (values in text), D3/N1 (provenance note in Data availability; replacement CSVs → Phase C).
- **New findings folded in:** N2 (E1 v20 A6 K-bound wording adopted), N3/AD8 (dated cell-count note), N4 (32-row DM universe stated; E1's 28 reconciles as the 24 primary + 4 comparisons — no E1 edit), N5 (batch-7 archive paths), N6 (as-of-verified scope — see below).
- **Registered-but-not-run items now named in v14 text:** Edwards cross-environment tolerance figure (AD3), smoother rescoring test (claude 3.1), D6/D7 realised predictive gains (AD2), prospective band calibration (AD4).
- **Remaining:** Phase B (owner decisions: AD6 reframe, AD2 rename, AD4 wording), Phase C (computational campaigns incl. D3 replacement CSVs, T=71, smoother test, MCS/encompassing, Edwards rerun), Phase D (prospective-registration subsection). N6 caveat: "all surviving points implemented" holds only as-of the 2026-09-13 verification; new evidence can reopen items.

---

## 9. User directives (2026-09-13) — standing workflow rules

1. **Push workflow.** Commit and push all previous and future creations in appropriate folders (create new folders when appropriate). Executed 2026-09-13: branch `edwards-framework-e1-audit-implementation` (HEAD `3b71317`, based on main, +10 files, zero modifications to existing repo content): `framework/` v14 paper, apply script, Phase A changelog, this register, the extended joint evaluation, the ASCII/JSON v13 wrappers; `wave_e_edwards/results/e3_audit_uncertainty_add_M2m_h5.json`; root `MANIFEST.md` + `AUDIT_IMPLEMENTATION_README.md`. Helper: `push_to_github.sh` (re-run after each phase; append new artifacts to its FILES list).
2. **Pull policy.** Remaining files related to framework/E1/E3 were fetched as newest-only (112 files, all git-blob-sha verified; ~60 duplicates skipped; nothing on the repo was modified). Verified: newest repo-wide are F1 v13 (release branch only — no paperF1 on main), E1 v49, E3 v16. New mirrors: `batch 2/4/5`, `reaudit/`, `batch 7` waves 4–13 + full `e1_audit_2026-09` + new `source_audits`, `arena agent1/audits`, `arena agent 1/other documents`, `wave_e_cod/{admission,manuscript}`, `wave_e_edwards/{manuscript,exploratory_second_pool,data extras,readiness.md}`, `revised_articles/`, `research_program/` A014 records, repo `README.md`/`RELEASE_NOTES.md`.
3. **Version discipline.** All revisions are new versions; previous versions are never overwritten (v13 untouched; Phase B output will be v15, etc.).
4. **Phase B mandate.** Profound resolutions and root-cause analysis over shallow quick-fixes; honesty and novelty. **Executed 2026-09-13:** root-cause memo, owner decisions (AD6 adopt fully / AD2 option a / AD4 option b), single coordinated pass → v15. Remaining: Phase C (computational campaigns incl. D3 replacement CSVs, T=71, smoother test, MCS/encompassing, Edwards rerun), Phase D (prospective-registration subsection).
- 2026-09-13 Phase C DONE: 12 PASS / 2 marginal CHANGE / 4 NEW reconciliation; v16 written (25 asserted rules), verified; changelog PHASE_C_CHANGELOG_v15_to_v16.md; results PHASE_C_RESULTS.md; harness phase_c/ (10 scripts, provenance-archived).
- 2026-09-13 Phase E DONE: journal formalization v17 (75 rules); single pinned-seed number set; formalization + coverage scanners added (0 flags); no earlier-version references; companion papers cited.
- 2026-09-13 Phase F2 DONE: v20 (6 rules) — O8 IC co-primary subsection written from the archived O9 check (cod agrees with the standard; on Edwards the IC would retain the class-grounds-declined M2m — gates load-bearing against the IC; D5 0.5%/3.5% vs rule 0.5%/5.0%); O12 four densest passages narrated (numbers retained in Table 2 / Section 6).
- 2026-09-13 Phase J DONE: v21_restructured + Supplement S1 (owner decision NEW-2) — worked examples precede the simulation, standard/demonstration/simulation separated, uncertainty variants/open problem/verification appendix moved to S1 with main-text summaries; line-completeness audit 0 unaccounted; coverage scanner refined for the renumbering. Main 10,695 words; remaining V9-A compression → O16 (optional).
- 2026-09-13 O7 DONE: companion cross-check vs newest E1 (v49) and E3 (v16) + cited archives — COMPANION_CROSSCHECK_20260913.md; all F1-companion numbers verified except NEW-4a (M1 h=1 point-rule retention reconciled in v22) and NEW-4b (O9 M3/M4 corrected to 14.46/14.30; IC-best unchanged). Re-runs at E1/E3 finalization.
- 2026-09-13 O17 DONE: v23 (2 rules) — M4/M5 protocols named in the reproducibility paragraph + M5 reference; every V9 item now implemented or declined with recorded reason. O6 web search: data available (EAA data portal, DFO 2026 xteNCAM vintage); execution remains a future-application event.
- 2026-09-13 Phase K DONE: O6 executed — cod band calibration on the pinned-seed archive (validated: all 10 published cells reproduce at 5%; frontier 0.444→0.312 power, 0.760→1.000 specificity; no band attains both → 5% retained, v24 §8). Edwards calibration draft sheet registered (owner-gated); origin-2024 inputs archived (2024/2025 panel); Spec B origin 2025 scores at the 2027 vintage. Companion venues scanned (V10): CV1–CV5 recorded, none contradicts F1.
- 2026-09-13 V11 (humanized rewrites) DONE: joint evaluation → v25_restructured (base = Grok rewrite, drift-audited: 0 fabricated numbers; Gemini harvested selectively; NEW-5 M4 citation fixed 54→61 methods; NEW-6..9 rejected with reasons; redundancy regressions re-fixed). Numeric drift v24→v25 none; scanners green.
- 2026-09-13 Phase F DONE: v19 (12 rules) — journal-fit text pass from the merged plan (O1 abstract IC caveat; O2 fibre→formal; O3 climate Table 5b + NEW-3 adjudication: archived E3 Table 7 governs, R-ENSO→M2_Rar 0.41 ft, edge-past scoped to the 2015–23 window; O10 structural-redundancy principle; O11 one-page standard statement; O13 reproducibility paragraph + Chambers 2013; O14 consolidated limitations). Owner decisions recorded: NEW-1 root-cause resolution (AD4 stands, O9 empirical completion); NEW-2 Phase J after text passes with distinguishing filename, version count continuous. Venues V1–V9 fully incorporated; contradictions 28 adjudicated, 0 outstanding.
- 2026-09-13 Phase D DONE: v18 (22 rules) — redundancy scan 91→0 findings (incl. §6 table sync), §4.7 Prospective registration added (AD4 pairing, Amendment-1 length check). All four register phases A–E complete; every audit item closed or disclosed.

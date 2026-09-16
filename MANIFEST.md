# Clone Manifest — Framework (F1) + E1 + E3, newest versions only

**Source:** GitHub release tag [`edwards-framework-e1`](https://github.com/MIKEAA2020/general-sustainability/releases/tag/edwards-framework-e1)
**Asset:** `workspace-edwards.framework.2nd.zip` (the newer of the release's two zip assets, uploaded 2026-09-12 22:49 UTC)
**Cloned on:** 2026-09-13

Only the **newest version of each related file** was extracted — no older versions, no unrelated papers (E2/E4, paper1/2/5, audits, transcripts).

---

## 1. Framework paper (newest release: v13; current working version: v14)

| File | Size | Notes |
|---|---|---|
| `framework/paperF1_retention_framework_v13.md` | 56.8 KB | Latest framework version. Title: *"When does added model structure earn its place?"* Byte-identical to the tag's git blob (sha256 `ecf9c751…`). Contains Unicode math/typography glyphs only (em/en dashes, σ, φ, Δ, ≤, ≥, →, ×, ≈, ∈, superscripts, combining accents) — valid UTF-8, zero control chars/tabs/BOM. |
| `framework/paperF1_retention_framework_v13.json` | 58.6 KB | JSON-hardened copy (added 2026-09-13): the md embedded as a properly escaped JSON string (`ensure_ascii=True` — pure ASCII, all escapes as `\uXXXX`). Strict-parsed and verified round-trip identical. |
| `framework/paperF1_retention_framework_v13.ascii.md` | 56.5 KB | ASCII-only transliteration (added 2026-09-13) for pipelines that reject non-ASCII: `σ→sigma, φ→phi, Δ→Delta, ≤→<=, →→->, φ̂→phi-hat, yr⁻¹→yr^-1, …`. Original stays untouched. |
| `framework/paperF1_retention_framework_v14.md` | 62.6 KB | **Phase A output (2026-09-13)** — the v13 → v14 text-only implementation pass (41 asserted replacement rules). All surviving audit points from the qwen+claude pair plus the N1–N6 / AD1–AD8 findings; style scan 0 blockers. Produced by `apply_phaseA_v13_to_v14.py`; per-edit mapping in `PHASE_A_CHANGELOG_v13_to_v14.md`. |
| `framework/apply_phaseA_v13_to_v14.py` | 17 KB | The Phase A edit script (reproducible: re-running it on v13 yields v14 byte-for-byte). |
| `framework/PHASE_A_CHANGELOG_v13_to_v14.md` | 8 KB | Edit → audit point → adjudication reference for all 37 changelog rows; also lists what was deliberately left for Phases B/C/D. |

*(v0–v11 were intentionally not cloned; v12 was added on request — see §2.)*

## 2. Framework audit set (added 2026-09-13, on request)

| File | Size | Notes |
|---|---|---|
| `framework/JOINT_EVALUATION_TWO_AUDITS_v13.md` | 16.9 KB | Joint evaluation of the two framework audits; carries a §4 pointer to the register with the three record-vs-paper discrepancies. |
| `framework/paperF1_retention_framework_v12.md` | 54.1 KB | The v12 framework paper — explicitly requested alongside the v12 audit docs (older than v13, kept for audit cross-reference). |
| `framework/CONTRADICTORY_POINTS_ADJUDICATION.md` | 15.6 KB | Adjudication of contradictory audit points (v11→v12 cycle). |
| `framework/JOINT_AUDIT_REMAINING_POINTS_v12.md` | 27.4 KB | Remaining points from the joint audit at v12. |
| `framework/REMAINING_POINTS_IMPLEMENTATION_v12.md` | 15.7 KB | Implementation of the remaining points at v12. |
| `framework/REMAINING_POINTS_TWO_AUDITS_v13.md` | 15 KB | Added 2026-09-13: gap register for the two audits (qwen+claude) — every point traced to v13, contradictions adjudicated before implementation (incl. a data-backed K-bound adjudication from `wave_e_cod/data/ncam_2016_table_a2.csv`, corrected 2026-09-13 against `run_ladder.py` L82), phase-by-phase implementation plan (§5), §7 addendum (N1–N6), §8 Phase A outcome. |

Related: the release zip also contains `uploads/framework audits.txt` (126.6 KB, the four grok/gemini audits used for the v11→v12 cycle — extracted to `framework/framework_audits.txt`) and `uploads/audit of framework v12.txt` (95.4 KB — byte-identical to the attachment you uploaded, the qwen+claude pair).

## 3. Audit-check backends (added 2026-09-13)

| Path | Contents |
|---|---|
| `wave_e_cod/` | SPECIFICATION v1–v4, protocol, `src/*.py` (incl. run_ladder.py), results CSVs, data inputs (NCAM, capelin, catch, landings, SOURCES). |
| `wave_e_edwards/` | SPECIFICATION v1–v2, protocols, admission memos, `src/*.py` (incl. e3_audit_uncertainty.py), results, data inputs (annual_panel.csv, EAA discharge, USGS recharge). |
| `specifications/` | SPECIFICATION v1–v4 copies (the frozen pre-registration sheets). |
| `uploads/` | `audit of framework v12.txt` (qwen+claude), `framework audits.txt` (grok/gemini ×4), `last message.txt` (verification transcript behind §4.3 — provenance key), original v0 draft. |
| `audits_E1_E3/source_audits/` | 30 raw audit transcripts (rounds 1–9 sources, joint, orchard, human reviewer, empirical, top-down, turnover, profound upgrades, …). |
| `audits_E1_E3/wave6/`, `e1_audit_2026-09/` | E1/E3 wave-6 scans and the 24 processed round evaluations. |
| `arena_agent_1/…/rerun_campaigns/` | e1/e3 campaign scripts + result CSVs (baselines, reconciliation, pumpage). |
| `arena_agent_1/…/audits/` | `_scan_work/` (E1/E3 content-survival classifications), joint assessments waves 2–5, open_items wave 7. |
| `arena_agent_1/paper rewrites/` | `E1_TIER3_RESTRUCTURING_PLAN.md`, `E1_V20_CHANGELOG.md` (source of N2/N6). |
| `agent 2 productivity illusion/analysis/` | JOINT/ECOMOD assessments (checked — no framework-relevant points). |
| `TRANSFER_AUDIT_RESPONSE.md` | Checked — no framework hits. |

Findings from scanning these: `JOINT_EVALUATION_TWO_AUDITS_v13.md` §5 (N1–N6) and `REMAINING_POINTS_TWO_AUDITS_v13.md` §7. **Phase A (2026-09-13):** all uncontested, adjudicated text fixes are now implemented in `framework/paperF1_retention_framework_v14.md` (changelog: `PHASE_A_CHANGELOG_v13_to_v14.md`; new computed artifact: `wave_e_edwards/results/e3_audit_uncertainty_add_M2m_h5.json`). Phases B (owner decisions), C (computational campaigns), D (prospective-registration subsection) remain, per the register §5/§8.

## 4. E1 — Cod forecast ladder (newest: v49)

| File | Size | Notes |
|---|---|---|
| `e1/paperE1_cod_forecast_ladder_v49.tex` | 129 KB | **Authoritative source.** Generated from md v15 by `wave13/build_latex_v13.py`, then edited directly through v49. |
| `e1/paperE1_cod_forecast_ladder_v49.pdf` | 743 KB | Compiled PDF of v49. |
| `e1/E1_SUPPLEMENTARY.md` | 11 KB | Supplementary material. |
| `e1/COVER_LETTER_paperE1_cod_forecast_ladder_FR.md` | 4 KB | Cover letter (Frontiers/FR). |
| `e1/figs/` (8 PNGs) | ~0.8 MB | fig1_series, fig2_windows, fig3_rmse, fig4_production/xtencam, fig5_production/xtencam, fig6_power. |

## 5. E3 — Edwards forecast ladder (newest: v16)

| File | Size | Notes |
|---|---|---|
| `e3/paperE3_edwards_forecast_ladder_v16.tex` | 64.5 KB | **Authoritative source** — the v16 .md is marked *SUPERSEDED SOURCE*: the .tex contains extra material added after build (Generalizability boundary, Practical reading, AR(1)/head-AC(1) mechanism, Uvalde no-transfer clarification). Do not rebuild the .tex from the .md. |
| `e3/paperE3_edwards_forecast_ladder_v16.pdf` | 564 KB | Compiled PDF of v16. |
| `e3/paperE3_edwards_forecast_ladder_v16.md` | 50.6 KB | Kept for reference only — superseded by the .tex (see warning above). |
| `e3/figs/` (5 PNGs) | ~0.5 MB | fig1_series, fig2_windows, fig3_rmse, fig4_pass2, fig5_fibre. |

---

## Intentionally NOT cloned

- **Older versions** of all three papers (F1 v0–v11; E1 v14–v48 and md v2–v15; E3 v2–v15). F1 v12 was cloned on request (§2). Available in the release zip if ever needed.
- **Unrelated papers/work:** E2 (cod intervention), E4 (Edwards intervention), paper1/2/5 LaTeX trees, cover letters for other papers.
- **Process artifacts:** audit rounds (`audits_E1_E3/`), `joint_assessments/`, source-transcript `.txt` audits, scan work, changelogs.
- **Analysis workspaces:** `wave_e_cod/` and `wave_e_edwards/` (data, results CSVs, src scripts, SPECIFICATION v1–v4). These are the E1/E3 computation backends — say the word and I'll pull the current versions of either folder.

## Verification

SHA-256 of every extracted file was recorded at clone time (see file list above for size checks). The papers' newest-version numbers were cross-checked against the repo's `main` branch and the release tag's full tree: no newer F1/E1/E3 versions exist anywhere.

---

## 6. Second fetch (2026-09-13, on owner directive) + push

**Pulled (newest-only, 112 files, every one verified against the repo's git blob shas; ~60 more skipped as byte-duplicates of files already here; nothing in the repo was modified):**
- `batch 2/` E1_LANGUAGE_COMPLETENESS, E3_CLASSIFICATION_THEOREMS, WAVE_E_UPDATE; `batch 4/` E3_C63_REPAIRED, WAVE_E_RERUN, WAVE_E_SPEC_MATCH + verify scripts; `batch 5/glm/review_report_wave_e.md`; `reaudit/` verify scripts.
- `batch 7 …/` root (JOINT_AUDIT_EVALUATION, WAVE2_IMPLEMENTATION, E2_V17_E3_V12_VERIFICATION, apply scripts), `e1_audit_2026-09/` (ROUND1–9 evaluations, V16/V17/V30–V37 changelogs, BAND_CHECK, LINE_LEVEL, MERGE_DECISION, METHODS_FRAMING, SIMULATION_RESULTS, DEFERRED_ITEMS, E2_E4_IMPORT), `source_audits/` (e1 rounds 1–9 sources, deepseek e3/e4 ×4, grok-claude e1/e3, 4 audits_v33, grok gemini upgrade), `results/e3_dm_uncertainty.csv`, waves 4–13 E1/E3 items (records, apply scripts, build_latex, logs).
- `arena agent1/audits/` gpt+grok audit e1/e3; `arena agent 1/other documents/` WRITING_PLAN, stage_code_recovery_report; `arena agent 1/paper rewrites/` E3_E4_strengthening (IMPLEMENTED + REPORT), submission zips E1 v15 / E3 v16, aug08 survey (byte-identical to the analysis README).
- `wave_e_cod/` admission kernel + manuscript v2 + figs; `wave_e_edwards/` data (6), readiness, manuscript v2 + figs, full `exploratory_second_pool/` (J-27 second pool: 3 records + 6 data + 9 results + 8 src).
- `revised_articles/A014_northern_cod_revised.md`, `research_program/` A014 records ×2, repo `README.md` + `RELEASE_NOTES.md`, `tools/selftest_fixtures/sabotage1.tex`, agent-2 framework-named docs ×2.

**Verified repo-wide newest:** F1 v13 (release branch only — no paperF1 on main), E1 v49, E3 v16. All shared files byte-identical to main (173 paths, 0 diffs).

**Pushed:** new branch `edwards-framework-e1-audit-implementation` (HEAD `3b71317`, = main + 10 new files, nothing modified): framework v14 + apply script + changelog + register + extended joint evaluation + v13 wrappers, `wave_e_edwards/results/e3_audit_uncertainty_add_M2m_h5.json`, root MANIFEST + `AUDIT_IMPLEMENTATION_README.md`. Re-run `push_to_github.sh` after each phase (append new artifacts to its FILES list).
- 2026-09-13 (Phase C, intermediate): pushed @ 050497a — Phase C harness (10 scripts + PHASE_C_RESULTS.md + Edwards rerun JSON); branch edwards-framework-e1-audit-implementation; main untouched.
- 2026-09-13 (Phase C, final): pushed @ 5074700 — F1 v16 + apply_phaseC + PHASE_C_CHANGELOG + 10 campaign scripts + 24 results files (all provenance-archived); branch edwards-framework-e1-audit-implementation (4,045 blobs = main + 48); main untouched (3,997 blobs).
- 2026-09-13 (Phase E, journal formalization): v17 written (75 asserted rules); single pinned-seed number set; journal_formalization_scan.py + content_coverage_scan.py added (0 flags); no earlier-version references in the manuscript.
- 2026-09-13 (Phase D): v18 (22 asserted rules) — remnant/redundancy scan 91→0 (redundancy_scan.py; §6 table synced), §4.7 Prospective registration; register phases A–E all DONE.
- 2026-09-13 (planning): MERGED_IMPROVEMENT_PLAN_ALL_VENUES_v18.md — all venues merged (V1–V9), 25 contradictions adjudicated / 0 outstanding, open items O1–O7 phased (F text / G compute / H events); qwen journal-fit venue arrived empty, pipeline ready.
- 2026-09-13 (planning): V9 (qwen framework journal fit) received and processed into MERGED_IMPROVEMENT_PLAN — NEW-1 adjudicated (AD4 binds; IC co-primary check adopted as O8/O9), NEW-2 owner-gated (Phase J structural pass), open items now O1–O15.
- 2026-09-13 (Phase F): v19 — journal-fit text pass (O1/O2/O3/O10/O11/O13/O14), NEW-3 adjudicated via archived E3 Table 7, new Table 5b, structural-redundancy gloss, one-page standard statement, reproducibility paragraph, consolidated limitations. v18 frozen.
- 2026-09-13 (Phase F2): v20 — IC co-primary subsection (O8, from archived O9 check), parenthetical density unpacked (O12). Phase G O9 computation archived + validated. v19 frozen.
- 2026-09-13 (O7): companion cross-check (COMPANION_CROSSCHECK_20260913.md) → v22_restructured (NEW-4a M1 reconciliation) + O9 archive fix (NEW-4b). E1/E3 finalization re-run trigger registered. v21 frozen.
- 2026-09-13 (O17): v23 (M4/M5 protocols + M5 ref; V9 fully closed). O6 data-availability recorded from web search (EAA portal; DFO 2026 assessment). v22 frozen.
- 2026-09-13 (Phase K): O6 executed — cod band calibration (no band attains both targets; 5% retained; v24 §8); Edwards calibration DRAFT sheet (owner-gated); companion venues V10 (CV1–CV5). v23 frozen.
- 2026-09-13 (V11): joint evaluation of humanized rewrites (JOINT_EVALUATION_HUMANIZED_REWRITES_V11.md) → v25_restructured; M4 citation fixed (61 methods); Gemini unarchived numbers and fabricated refs rejected. v24 frozen.
- 2026-09-13 (V12): joint evaluation of novelty/impact audits (JOINT_EVALUATION_IMPACT_AUDITS_V12.md); O18–O39 opened; NEW-10…17 adjudicated (43 total, 0 outstanding).
- 2026-09-13 (owner review): NEW-18 (supplement restructuring approved when merited — DM mechanics to S1 unblocked; full 8-10k compression not merited) and NEW-19 (relaxation test of all frozen pre-registrations/spec rules: none merits relaxing; O29 extended with band-invariance statement; O19 concrete prospective criterion proposed). Phase L scope finalized, awaiting go.
- 2026-09-13 (Phase L): v26_restructured — O18/O22/O24/O25/O27/O29(+band-invariance)/O33/O37/O38/O39 + NEW-18 DM-to-S1.4 (16 rules, apply_phaseL_v25_to_v26.py); v26 supplement (S1.4 + S2 two-page specification/checklist); numeric accounting 0 added / 13 removed = moved DM tokens; scanners green. v25 frozen.
- 2026-09-13 (Phase M): S1.5 supplement added — O20/O30/O32 archive computations (instrument comparison, Wilson intervals, identification decomposition) on sim_retention_power_20260913.csv; frozen JSON at phase_c/results/phaseM_archive_computations_20260913.json; zero new simulation; v26 supplement scanners green. Also: full-read sweep of both impact audits → NEW-20/21/22 addendum in OWNER_REVIEW memo; no additional open audit items.
- 2026-09-16 (Phase N+O): S3 (fillable audit canvas S3.1 + verdict record S3.2 + machine-readable validator S3.3 `framework/certificate_schema_S3.py`) and S4 (verified literature positioning, 7 references) added to the v26 supplement; Edwards prospective DRAFT finalisation-gated — O19 criterion (§3a) and E2m convention decided with-decline (§4). Zero contact with frozen numbers; scanners green on supplement; v26 main text untouched.
- 2026-09-16 (Edwards finalization): owner-review closed (NEW-20/NEW-22 bequeathed); prospective band sheet FROZEN — harness `framework/campaign_edwards_band_calibration.py` with E2m-collapse self-test first gate, dry-run (`phase_c/results/edwards_band_calibration_dryrun_20260916.json`) degenerate at the Edwards T=90/σ=12.34 regime — honestly recorded, no retuning; full 100-rep/cell campaign registered follow-through.
- 2026-09-16 (Edwards full-campaign root cause): pre-flight audit (`framework/campaign_edwards_band_calibration_audit.py`) caught an M4 comparator-gate deadlock (lag-1 start state, h1 −16% vs M3 at every cell); root-cause-fixed in the harness with a DECLARED ASYMMETRY (M4 scorable, H1(M4) recorded-not-enforced, machine-visible) rather than weakening the gate; audit passes on its own merits. Campaign remains registered follow-through per newest-only. Cod Spec-B deep root cause recorded (`framework/COD_SPECB_ROOTCAUSE_20260916.md`): three coupled problems — A (origin-2025 data, resolved: post-2026-assessment vintage), B (T=71 identifiability, binding, DEFERRED by the frozen sheet v4 that places T=71 outside the core design; trigger = a dedicated pre-registered Spec-B sheet + owner approval), C (execution, follows B). 200-rep T=71 estimated 3.8 h, inside sandbox. No T=71/speculative run launched.
- 2026-09-16 (campaigns): Edwards full band-calibration campaign launched (100 reps/cell x 6 cells x 31 bands, frozen sheet, audit-passed harness with declared-asymmetry M4); Cod Spec-B not launched (sheet-frozen v4 deferral; see COD_SPECB_ROOTCAUSE_20260916.md); NEW-20/NEW-22 and O34/O35 closed as bequeathals.
- 2026-09-16 (Edwards campaign + origin 2024): registered 100-rep/cell calibration executed (233 s; 6 cells x 31 bands) — 20 bands attain power>=0.80 & specificity>=0.90; smallest qualifying band ADOPTED = 0 (Edwards T=90/σ=12.34 regime, mirror of cod's identification-limited frontier); 5% pre-registered band inside the window. First origin 2024 scored provisionally at h=1 (M1 not retained; M2/M3/M4 deferred on archived-NaN inputs; h=5 at 2029 actual). Artifacts: phase_c/results/edwards_band_calibration_full_20260916.json + edwards_origin2024_scores_20260916.json. Cod Spec-B not executed (frozen v4 deferral; dedicated Spec-B sheet + owner approval is the trigger).
- 2026-09-16 (close-outs): deferred Edwards inputs — R_2024 (154.0) + H_2024/H_2025 already archived; the ONLY remaining input is P_2024 (EAA/USGS annual pumpage, ~early-2026 per edwardsaquifer.net); archived as `wave_e_edwards/data/pumpage_2024_sidecar.json` (AWAITING SOURCE) + build_panel.py sidecar-merge hook (tested no-op/FILLED; annual_panel.csv never hand-edited). 2029 h=5 verdict = designed waiting per frozen sheet §6. Cod Spec-B dedicated sheet drafted: `specifications/SPECIFICATION_cod_T71_frontier_DRAFT_20260916.md` — lifts v4's deferred T=71 (D1/D5 at 200 reps, σ{11.8,33.8}, + D6/D7), §3a/§4 adopted as-is, band sweep declared as a registered refinement (superset of v4's single-band check), pilot points reconciled as the dry-run gate; owner-gated for freeze, not executed.
- 2026-09-16 (owner-gate lattice audit): dispositions for every 'owner gate' in the lattice — P_2024 publish-gated (sidecar), 2029 h=5 designed waiting, Cod Spec-B sheet freeze = the only genuinely parked pre-registration decision (dedicated T=71 sheet drafted), companion CV1–CV5 owner-gated by instruction; stale carries O21 (sheet-gated, props to Spec-B sheet) and O35/O36 (executed in v25 lineage) closed in the merged plan.
- 2026-09-16 (Cod Spec-B sheet improvement): five root-cause fixes to `SPECIFICATION_cod_T71_frontier_DRAFT_20260916.md`, none touching frozen v4 elements — (i) §4a pins the pooled-mean convention + per-σ frontier (republished from the archived Phase-K pooled entry, power=unweighted mean over D1/D3/D6/D7 each averaged over two σ; specificity analogous; adopted band chosen on the pooled curve, per-σ splits reported), (ii) §4b mandates exact counts + Wilson intervals with pilot-resolution reconciliation at the dry-run gate, (iii) §3 adds a runtime-guard sidecar (`cod_t71_calibration_partial_20260916.json`, resumable, never half-pooled), (iv) pre-registered MD5 seed map declared in-sheet (family convention, PYTHONHASHSEED=0), (v) D6/D7 σ shift made explicit in-sheet. Owner gate for freeze unchanged; the change is integrity, not a new decision.
- 2026-09-16 (Spec-B sheet, second root-cause pass): added §6 'Declared space' — (i) D2/D4 cross-over question registered as the first candidate for a follow-up amendment (NOT a frozen element: Phase M identified D2 as inference-limited, so the T=71 length question is sharper than v4's D1/D5 check; widening frozen scope silently would be drift), (ii) deferred elements σ=0 / 𝔰∈{5,30} given an explicit trigger (own future sheet + owner approval, never silently folded in), (iii) frozen bounds restated. Yet among conventions — rep counts, cells, rule, vocabularies, procedures — all now pinned; remaining gaps are editorial, not methodological. Owner freeze gate unchanged.
- 2026-09-16 (correction): COD_SPECB_ROOTCAUSE memo corrected — Spec-B historical series IS archived (wave_e_cod/data/xtencam_table17_ssb.csv, 1954–2024, Regular et al. 2025 Table 17, checkpoint-verified, SOURCES.md-locked); the gap is only the 2025/2026 tail needed by new origins 2024/2025 (SSB_2025, SSB_2026, 2024+ landings), which exists publicly in the 2026 assessment documents but is not transcribed — owner-gated ingestion, same pattern as the Edwards pumpage sidecar.

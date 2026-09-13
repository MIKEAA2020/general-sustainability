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

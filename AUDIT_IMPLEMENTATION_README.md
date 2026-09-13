# Audit Implementation Branch — edwards-framework-e1-audit-implementation

**Created:** 2026-09-13 by the Arena audit-implementation agent, at the owner's request
(commit & push all creations in appropriate folders; never overwrite existing repo content).

This branch is based on `main` and adds **only new files** — no existing repo file is modified
or deleted. The owner's original work remains intact on `main` and on the `edwards-framework-e1`
branch; nothing here overwrites it.

## Contents

### framework/ — the retention framework paper F1
| File | What it is |
|---|---|
| `framework/paperF1_retention_framework_v14.md` | **Phase A output.** The v13 → v14 text-only implementation pass of every surviving, adjudicated point from the two audits (`uploads/audit of framework v12.txt`: qwen + claude) plus the new findings N1–N6. Produced from the untouched v13 by the script below; journal style scan: 0 blockers, PASS. |
| `framework/apply_phaseA_v13_to_v14.py` | The Phase A edit script (40+ asserted replacement rules; re-running it on v13 reproduces v14 byte-for-byte). |
| `framework/PHASE_A_CHANGELOG_v13_to_v14.md` | Per-edit mapping: edit → audit point → adjudication reference; also lists what was deliberately left for Phases B/C/D. |
| `framework/REMAINING_POINTS_TWO_AUDITS_v13.md` | Gap register: every point of the two audits traced, contradictions adjudicated **before** implementation (AD1–AD8, incl. the data-backed K-bound adjudication corrected against `wave_e_cod/src/run_ladder.py` L82), phase-by-phase plan (§5), §7 addendum (N1–N6), §8 Phase A outcome. |
| `framework/JOINT_EVALUATION_TWO_AUDITS_v13.md` | The author's original joint evaluation (sections 1–3, kept byte-faithful) extended with §4 (the three record-vs-paper discrepancies D1–D3) and §5 (recovered points N1–N6). |
| `framework/paperF1_retention_framework_v13.json` / `.ascii.md` | Hardened copies of v13 (pure-ASCII JSON wrapper + ASCII transliteration) for pipelines that reject non-ASCII. Original untouched. |
| `framework/JOINT_EVALUATION_FOUR_AUDITS_v2.md` | *(local mirror only — fetched from the release branch, not re-pushed; it already exists there.)* |

### wave_e_edwards/
- `wave_e_edwards/results/e3_audit_uncertainty_add_M2m_h5.json` — the M2m-versus-persistence h=5 test
  (margin −3.6607, DM z=−3.284, p=0.0016, block-bootstrap CI [−5.7637, −2.1862]) computed with the
  archived E3 machinery (`wave_e_edwards/src/e3_audit_uncertainty.py`, seed 20260905, block 8, nboot 10000, n=71).
  This substantiates the v13 claim now carrying the interval in Table 4 of v14.

### Root
- `MANIFEST.md` — clone manifest (source release asset, newest-version policy, verification).
- `AUDIT_IMPLEMENTATION_README.md` — this file.

## Version policy (owner directive)
All revisions are created as **new versions**; no previous version is ever overwritten.
Phase B/C/D outputs will be pushed to this branch as they are produced (v15+, new scripts, new data).

## What this branch deliberately does NOT contain
- No older versions of papers (F1 v0–v12, E1 v14–v48, E3 v1–v15) — newest-only per owner directive.
- No E2/E4/paper1–5 files — out of scope ("related to framework, E1 and E3").
- No re-pushed copies of files already on `main` (fetched mirrors stay local).

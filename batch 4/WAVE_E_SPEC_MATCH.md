# Wave E Part III — Specification Matching: Execution Record

**Executed 2026-08-26.** This document discharges the specific limitation *"Wave E specification matching: NOT CONFIRMED — no specification has been frozen and no matching performed"* (`RELEASE_NOTES.md` §5; `PROOF_MANIFEST.md` "Reproducibility status" issue 4) **for the two scored trees**.

**What this does NOT do:** it does not close Wave E, and it does not flip any Part III paper-support row (those rows concern paper claims — the continuum lift, the NAIM persistence theorem, governance-template instantiation — not the scored trees). The scored trees keep their Part VI status (`INDEPENDENT_RERUN`, nothing certified).

**Verifier:** `reaudit/verify_wave_e_spec_match.py` — 36 machine checks, exit 0 (all passed). Every check recomputes scores from the committed per-observation forecast files or the committed raw series; nothing is taken from prose.

---

## The frozen specifications (as now recorded)

### Edwards Aquifer, San Antonio Pool (`wave_e_edwards/`) — Ω_SA

| Element | Frozen value | Source of freeze |
|---|---|---|
| S | Edwards Aquifer SA Pool as indexed by J-17 | `protocol.md` (locked 2026-08-25, *before scores*) |
| y_t | calendar-year mean of daily-high J-17 elevation, ft AMSL | protocol |
| B | calendar years 1934–2023; measured well, no interpolation, <240-day years dropped | protocol |
| Ladder | naive_persist, naive_mean, M1, M2, M2m, M3, M4, M2_oracle (diagnostic only) | protocol |
| T | four fixed windows (DOR drawdown 1934–1950/1951–1956; DOR recovery 1934–1956/1957–1961; pre-permit wet 1980–1990/1991–1995; CPM era 1997–2014/2015–2023) + rolling origin (min 15 training years, h=1,5) | protocol |
| Scoring | primary RMSE of annual-mean J-17 (ft); secondary MAE, Brier-660 (origins ≥ 2007), direction | protocol |
| Retention | causal module retained only if it beats the next-simpler causal model **and** naive_persist on primary RMSE; oracle/fibre cannot promote | protocol |

Pass 2 carries its own pre-score protocol (`protocol_pass2.md`: causal R from SON Niño 3.4 / lagged CD rain / AR).

### Northern cod (`wave_e_cod/`) — Ω_2016 and Ω_xte

| Element | Frozen value | Source of freeze |
|---|---|---|
| S / y_t (Ω_2016) | NCAM M-shift SSB, DFO SAR 2016/026 Table A2, 1983–2015; LRP = 884.58 kt (1983–1989 mean) | manuscript §2 + `results/meta.json` |
| S / y_t (Ω_xte) | xteNCAM SSB, 1954–2024; LRP = 276 kt; **not pooled** with Ω_2016 | manuscript + `results/xte_meta.json` |
| Ladder | naive_persist, naive_train_mean, M1 (Schaefer), M1b (Allee), M2 (stock-flow), M3 (AR residual), M4 (delay); pass-2 extension M2_survey_start (not retained on primary) | manuscript §2 |
| Catch | regime (240/120/5 kt) and annual (Schijns 2021) treatments; NCAM F/M never drivers | manuscript §2 |
| T | fixed collapse (1983–1990/1991–1995) and recovery (1995–2007/2008–2015) windows + rolling origin | manuscript |
| Scoring | primary rolling RMSE (kt) at h=1, h=5; log-RMSE/Brier secondary | manuscript |
| Retention | complexity kept only if it improves the preregistered score vs persistence | manuscript §1 |

## Match results (all machine-verified)

**Edwards (16 checks).** Protocol lock markers present; J-17 years cover 1934–2023 (90 years); ladder = frozen protocol set; all 16 rolling-summary rows recomputed exactly from the per-observation forecasts; rolling counts 75/71 (min-15 rule); all four fixed windows match the frozen train/test ranges; persist 13.230 / M1 12.839 / M2 14.698 (worse than persist) / M2m 12.283 & 17.445 (listed by point rule) / oracle 7.547 (diagnostic); pass-2 retention bookkeeping (`listed_by_point_rule` = [M2_enso, M2_precip, M2_combo], `retained_as_structure` = [] — the class-demotion split) matches the frozen rule's application; the Brier-660 modern subsample exists.

**Cod (20 checks).** Series locks in meta.json (1983–2015, LRP 884.58); ladder = manuscript set + recorded survey-start extension; all annual-treatment rolling rows recomputed exactly from the per-observation file; M2_survey_start recomputed from its own pass-2 artifact; naive baselines recomputed **from the raw committed series** (98.0494 = 98.0494 at h=1; 264.72 at h=5); the negative certificate verifies (no ladder model beats persistence at h=1; ladder range 115–206 kt as in the manuscript); collapse/recovery windows frozen and matched; collapse missed by every model (694–819 kt); Ω_xte ladder recomputed; xte naive recomputed from the raw xteNCAM series (87.65 = 87.65); persist 88 vs M1 120 as claimed; the two specifications are **not pooled** (distinct obs values on all 25 shared origins; xte obs match the committed series file exactly).

## Verdicts

1. **Edwards Ω_SA (Pass 1 + Pass 2): SPEC-MATCHED at the artifact level.** The specification was frozen in a dated protocol file before scores were generated, and every scored artifact implements it exactly. This is the strongest freeze discipline available in the two trees.
2. **Cod Ω_2016 + Ω_xte (Pass 1/2/6): SPEC-MATCHED at the artifact level, with two recorded caveats.** (i) *Freeze discipline is weaker*: the specification is manuscript-declared (manuscript §2 + meta.json locks), not a dated pre-score protocol file; the passes also evolved (1→6) with extensions declared in the manuscript rather than pre-registered. (ii) *Artifact coverage*: the per-observation rolling artifact stores the annual (Schijns) catch treatment; the regime treatment is recorded at summary level (presence and count-consistency checked; per-observation match not available).

## Standing obligations (unchanged)

- Part III paper-support rows: all remain **NOT CONFIRMED** (they concern paper claims, not the trees).
- The intervention-selection leg of §15 and the G1 Track 2 admission certificate: still open (see `research_program/remaining_obstacles_to_general_theory.md`, post-v1.0 update).
- Wave E is **not closed**; this record narrows the disclosure gap to the Part III paper claims.

## Reproduction

```
python3 reaudit/verify_wave_e_spec_match.py     # 36 checks, exit 0
```

# Wave-5 E1 record — paperE1_cod_forecast_ladder_v12.md (from v11)

**Task ID:** 75-a. **Directive:** owner gate opened — re-evaluate the registered
follow-ups; re-open what is now worth doing.

## The re-opened items (recorded reason mis-stated for both)

The wave-2 docket registered E1's "longer methodological asks" with the blanket
reason *"new computations/analyses, not corrections; they need a scored
campaign, not an edit."* Re-verified item by item at v11: two of the seven are
presentation-layer collections of values the article already prints — the
reason is mis-stated for them, and the P5-Table-3 pattern (parameters as
printed, unprinted members marked as archive items) is the repo's established
answer.

| Item | Endorsement | Re-verification at v11 | Disposition |
|---|---|---|---|
| Parameter table: "fitted r, K, s, φ and which bounds were hit" (claude priority 5: "Without it, 'unidentified Allee' is an assertion") | claude | Printed but scattered: the collapse-window M1 fit (r = 1.935, K = 1032.7, C = 240) at §1/§4/Prop 4.1; the bounds declaration and M1b's interior fit at §2.2; the recovery-window pinned pairs, SSEs, and flat-valley sweep at §3.2; M1b's stall-window fragility at §3.3; M3's φ = 0.95 at §3.1. No consolidated table; no computation needed. | **IMPLEMENTED**: new §3.6 "Fitted parameters as printed (post-freeze presentation layer)" + **Table 10** (11 rows, values quoted verbatim with source sections; the per-origin rolling fits, M3's per-window b, and M4's structural setting marked as archive items; the §2.2 bounds quoted as declared), plus a §2.2 pointer sentence |
| claude A7's constructive half — "The constructive finding is being buried: a one-year-stale persistence (184) loses to every structural model at h=1, so the value of a timely assessment (86 kt) exceeds the value of any structure tested" | claude (A7; echoed in grok's and claude's priority lists) | Verified: v10 implemented A7's label fix (the decomposition with correct labels at §4) but the positive timeliness finding is absent — no "timely/timeliness/stale" token anywhere in v11. | **IMPLEMENTED** (one sentence at §4, from printed values only): "Read constructively, the same printed arithmetic says the value of a timely assessment exceeds the value of any structure tested: the one-year information delay costs 86.4 kt at h=1 on Specification A — more than the entire structural cost of any delay-free module (M1 23 kt, M1b 17 kt, M2 46 kt, M3 37 kt over timely persistence, each a one-line subtraction of Table 4's printed values) and more than M4's own structure-given-delay cost of 11.1 kt — and the stale-persistence control, 184.4 kt, still loses at h=1 to every delay-free module while beating only the delay-carrying M4 (195.6 kt)." (claude's "every structural model" corrected in the wording to "every delay-free module" — M4 itself, at 196, does not beat the stale control; the honest statement is strictly stronger.) |

## Build and verification

- `apply_batch7_wave5_e1.py` (fail-loud: three asserted-once sub1 anchors + the
  version-log splice). Ran clean twice: **MD5 fa7632aa4c344a3fa929d8b82cea5425**
  both runs (447 lines, 10,480 words). v11 untouched.
- Diff = exactly 4 hunks: L5 (version log), L109 (§2.2 pointer), L323a324–345
  (§3.6 + Table 10, 22 inserted lines), L342→L364 (the constructive sentence).
- Mechanical checks: every v11 table line survives byte-identically and the
  table-line count is exactly +13 (Table 10's header/separator/11 rows); the
  abstract block is byte-identical and pinned at 300 words (Keywords line
  excluded); every printed-value needle's body count equals v11's count plus
  the additions' own count (computed programmatically — no value enters the
  paper except by quoting a printed source); Tables 1–9 captions and the
  frozen DM/1898/ε_log anchors intact; section order 3.5 < 3.6 < 4 verified.

## Still registered (reasons re-verified, still valid)

- **Drift/damped-trend baseline** (grok #7, claude) — a new scored computation;
  the standing rule authorizes no computation beyond R3.
- **Leave-one-origin-out influence for h=5** (grok #8, claude Table-8 note:
  the 1990 origin contributes ~110 kt of the rolling h=5 RMSE) — a new
  computation.
- **The 900–1900 kt Table-6 forecast explanation** and **the M3/M4 609/586
  deterioration explanation** — new analyses, not edits.
- **The M4 decomposition as a results table** — the §4 prose (v10's A7
  relabel + the new constructive sentence) now states the decomposition twice
  with correct labels; promoting it into §3 as a table relocates frozen-record
  prose for presentational gain only. Registered, not declined on merit.
- **log-RMSE demotion** — declined, reason updated: v11 already carries the
  full floor disclosure (ε_log = 10⁻³, per-origin hit counts, "the raw-RMSE
  column is the retention score"); dropping a recorded score column from
  frozen Table 4 contradicts cite-don't-drop, and grok's own alternative
  (move to a supplement) relocates frozen table content.

## Non-destructiveness

No frozen verdict, score, kernel, or table value changes; Tables 1–9
byte-identical; the abstract untouched; Table 10 quotes only printed values;
the constructive sentence's only derived figures are one-line subtractions of
Table 4's printed values, flagged as such.

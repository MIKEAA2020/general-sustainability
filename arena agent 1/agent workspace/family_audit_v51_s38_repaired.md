# E2 v26 — Sections 3.8 and 3.10 repaired; P3/P4/P5 spot-check

**Pushed `f9459e6`** — `paperE2_cod_intervention_v26.tex` + v26 battery (53/53).

## Why these numbers are authoritative

`rerun_campaigns/campaign_e2_elevation.py` is deterministic:
`SEED = 20260831`, `NMC = 20000` trajectories. Re-running it reproduces **all
six result CSVs byte for byte** (verified by re-running and diffing). Monte
Carlo error is ~0.003, so these are not seed-dependent — the campaign's output
*is* the value, and the paper's Data availability claims the elevation layers
are produced by exactly this script.

## What was wrong

None of §3.8's numbers reproduced:

- **0.837 and 0.917 appear nowhere in the campaign output at all.**
- **0.809 appears only at T = 5, not T = 20** (the paper calls it a 20-year figure).
- §3.8 **contradicted itself**: survival at C = 57.6 kt was given as
  0.837/0.809/0.917 and, four sentences later, as 0.74/0.73/0.85.
- The P ≥ 0.9 passage was internally inconsistent: it said the bar "is not
  attained by any tested constant catch under i.i.d. resampling" and then
  immediately gave an i.i.d. crossing of 12.5 kt. Under i.i.d. the maximum is
  0.868 and under blocks 0.808, so neither attains 0.9; only no-1992 does.

§3.10 (bootstrap) was stale in the same way — all nine of its numbers differed.

## Corrections

| quantity | printed | campaign |
|---|---|---|
| survival at the bound (i.i.d./blocks/no-1992) | 0.837 / 0.809 / 0.917 *and* 0.74 / 0.73 / 0.85 | **0.77 / 0.79 / 0.88** |
| P ≥ 0.8 crossings | 81.2 / 72.3 / 105.2 | **48.4 / 38.9 / 95.1** |
| P ≥ 0.9 crossing | 12.5 (i.i.d., contradictory) | **unattained (i.i.d. max 0.868, blocks 0.808); 48.6 no-1992** |
| i.i.d. range, zero catch → 120 kt | 0.90 → 0.65 | **0.87 → 0.58** |
| bootstrap: r median | 0.219 | **0.207** |
| bootstrap: g(K*) median | 159.6 | **150.5** |
| bootstrap: bound median | 44.7 | **35.6** |
| bootstrap: F′(K*) median | 1.142 | **1.134** |
| bootstrap 90% interval | [0, 87.1] | **[0, 84.8]** |
| refits with positive bound | 79.1% | **71.3%** |

The bound (57.6 kt) sits inside its corrected interval [0, 84.8]; the
superseded 91.6 did not sit inside [0, 87.1].

Battery v26 pins every §3.8 and §3.10 number to the campaign CSVs and asserts
the superseded values are absent: **53 passed, 0 failed**.

## Still open in E2

1. **Figure 7** (`figs_e2/fig7_stochastic.png`) and **Figure 2** were plotted
   against the superseded numbers; the text is now corrected but the PNGs need
   regenerating from the campaign's figures.
2. **Certified horizon "to T = 7"** — still unverified against the −114.85
   floors. It is the one consequence of the leak I have not traced.

---

## P3 v32 / P4 v41 / P5 v47 — spot-check result

Checked three cheap, independent classes across all three manuscripts:

| check | P3 | P4 | P5 |
|---|---|---|---|
| point estimate outside its own interval | 0 | 0 | 0 |
| abstract number absent from the body | 0 | 0 | 0 |
| "N of M (P%)" and "P% of M (N)" arithmetic | 0 | 0 | 0 |
| inline `a + b = c` / `a − b = c` | 0 | 0 | 0 |
| table rows vs stated totals | 0 | 0 | 0 (11 heuristic false positives: a year column read as a summand) |

No defects found. **This is a weak test, and I say so plainly** — it would not
have caught E2's leak either (that was caught by recomputing against the
pipeline, not by reading the prose). The analogue of what actually worked on E2
would be running `campaign_p4_dr_registration.py`,
`campaign_p5_crossing_scan.py`, `campaign_p5_stage_reconstruction.py` and
`campaign_p5_comparator_mse.py` and diffing against the papers. That is the
remaining step and it is not done.

Status: **structurally and arithmetically clean; not verified against their
pipelines.**

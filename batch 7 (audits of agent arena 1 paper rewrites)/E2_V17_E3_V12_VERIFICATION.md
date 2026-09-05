# E2 v17 / E3 v12 — evaluation, verification, and incorporation record

**Task.** The owner supplied a parallel sandbox's implementation report ("E2 v17" + "E3 v11",
with the companion uncertainty script `campaign_e3_dm_uncertainty.py`) and directed: *evaluate,
verify, and incorporate in latest versions if applicable.* That sandbox's manuscript files were
lost in its reset; the surviving script was owner-archived into this batch-7 directory (remote
commit `da1b609`) and is the only artifact verifiable directly. This record documents the
verification and the incorporation, which produced:

- `arena agent 1/paper rewrites/paperE2_cod_intervention_v17.md` (from v16; restructure-level)
- `arena agent 1/paper rewrites/paperE3_edwards_forecast_ladder_v12.md` (from v11)
- `results/e3_dm_uncertainty.csv` (the script's deterministically reproduced output)
- `apply_batch7_restructure.py` (the fail-loud build script for both papers)

---

## 1. Verification of `campaign_e3_dm_uncertainty.py`

**Run.** Executed unmodified against the registered
`wave_e_edwards/results/rolling_forecasts.csv` (per-origin obs/pred; models M1, M2, M2m,
M2_oracle, naive_mean, naive_persist at h = 1, n = 75 and h = 5, n = 71 — exactly the file the
script's docstring names). The script computes Diebold–Mariano statistics (HAC lag h − 1,
unweighted truncation, population-variance scaling) and moving-block (Künsch) bootstrap RMSE-gap
intervals (block length h, 20,000 replications, seed 0) for five model pairs at each horizon,
all against `naive_persist`.

**Determinism.** Two consecutive runs produce byte-identical output
(`md5 6900566d4ec8a9c04e1088d775831fbf`, both runs). The archived
`results/e3_dm_uncertainty.csv` is the verified output.

**Claimed numbers — all reproduce exactly:**

| Owner's description | Script output (verified) |
|---|---|
| "the 0.39 ft that retains the AR(1) is statistically indistinguishable from zero" | gap −0.391 ft, CI [−1.218, +0.560] (covers 0) |
| "DM z = −0.86" | −0.858 |
| "block 95% CI [−1.22, +0.56] ft" | [−1.218, +0.560] |
| "p = 0.38" | 0.384 (bootstrap p) |
| "M2m's edge (p = 0.001)" | 0.0012 |
| "the h = 5 climatology win (p = 0.035)" | 0.0354 (gap −4.301, CI [−10.405, −0.375]) |

The script additionally registers two rows this repository's v11 layer did not carry: the h = 1
climatology loss (+2.941 ft against persistence, p = 0.046) and the M2 h = 5 loss (+12.380 ft,
p < 0.001) — both consistent with the paper's readings; both are now registered in the v12 prose.

**Cross-implementation agreement** with the repository's own post-freeze layer
(`wave_e_edwards/src/e3_audit_uncertainty.py`, v11's §5.3.1). Every load-bearing conclusion is
identical: the M1 retention margin covers zero; the M2m margin is the only one-year margin that
separates; the h = 5 climatology interval excludes zero. The small statistic differences are
fully attributable to declared convention differences, verified analytically:

- DM h = 1: campaign −0.858 vs repo −0.852 — the ratio is exactly `sqrt((n−1)/n)` =
  sqrt(74/75): the campaign uses population variance (`g0 = Σx²/n`) and the repo layer uses
  sample variance (`np.var(ddof=1)`). With lag 0 at h = 1 both estimators reduce to `g0`.
- DM h = 5: campaign −1.580 vs repo −1.652 — beyond the ddof factor, the campaign sums the
  first 4 autocovariances unweighted (truncated HAC) while the repo layer applies Bartlett
  weights. Both are standard HAC variants.
- p-values: the campaign reports the bootstrap gap percentile p; the repo layer reports a
  Student-t(n−1) DM p alongside its own bootstrap CI (block 8). Both separate the same margins.
- Bootstrap: block length h vs 8; 20,000 vs 10,000 replications; different seeds.

**Verdict.** The script is genuine, deterministic, and its headline claims are true. It is
registered in the E3 v12 (§5.3.1 replication paragraph + Data Availability) as an independent
replication, with its output archived alongside it.

---

## 2. E2 v17 — item-by-item evaluation and implementation

Base: `paperE2_cod_intervention_v16.md` (the arena agent's latest). Constraint honoured:
non-destructive, restructure-level; **no value, kernel, or boundary changed** — verified
mechanically: the set of table rows in v17 is byte-identical to v16's (zero rows removed or
added; the diff is prose-only, 60 changed lines).

1. **"Abstract re-scoped to lead with the governed-object scope (a single fitted map, not a
   Northern-cod-general result); the K = 5000 pin is named a declared fit defect."**
   → **Implemented.** The abstract now opens with the governed object ("The governed object of
   this paper is a single fitted map — … — and every statement below is scoped to that map, its
   declared disturbance classes, and its declared catch-policy family; nothing here is a
   Northern-cod-general result"), and the pin is named in the abstract ("K = 5000 kt pinned at
   its optimization bound, a declared fit defect"). The abstract's numbered list renumbers to
   five findings plus an unnumbered definitional-note sentence (see item 3).
2. **"Retention filter → dominance partial order (Definition 2.6): 'retain/retention' is no
   longer used as a filter, since clause (H1) at every reading makes it a tautology. Result 3.1
   → 'No dominance'."**
   → **Implemented, with the tautology claim verified and stated honestly.** Verification: under
   the 5th-percentile class at T = ∞ every declared positive-catch rule has an empty kernel
   (constructive bound −114.9 kt for flat caps; for the reactive family the hold criterion
   φ < 0.029 fails for every declared φ) while BAU's kernel is nonempty (2219.6 kt — itself
   marginal: its zero-catch-equivalent requirement 5 + 287.4 = 292.4 kt lies just under
   g_max = 296.1 kt). So clause (H1), read at every reading with empty scored as worst,
   structurally blocks every positive-catch rule: the rule's outcome is fixed by the declared
   classes, which is the audit's tautology point. v17 restates Definition 2.6 as the dominance
   partial order (clauses verbatim — the frozen rule's own content is untouched; only the
   vocabulary and framing change), adds the "Why the filter vocabulary is retired" note, retitles
   Result 3.1 to "No dominance", states the verdict's selection-theoretic status, and reframes
   the groundwater-companion comparison (different constraint structure — not a single fatal
   floor — hence not comparable selections; the audit's "misleading comparison" item). The
   retention-filter vocabulary is swept from every filter role (abstract, Q2, §2.1, §3.2,
   §3.4, §3.6, §4, §5); the only remaining "retention rule" occurrences are the two deliberate
   correspondence statements (the version log and Definition 2.6's "the rule the frozen protocol
   calls its retention rule").
3. **"Finding-2 reframing: the vacuous-emptiness statement is demoted from a numbered result to
   a definitional note (an arithmetic identity, not an empirical finding); Conclusions
   renumbered to 5 findings + 2 definitional notes."**
   → **Implemented.** Result 3.2 becomes *Definitional note 3.2 (the vacuous-class identity)*
   with the identity stated as such (|e| > g_max ⇒ monotone decline for every C ≥ 0, "an
   identity of the map's algebra, not a measurement"); §3.2's header and intro are retitled
   accordingly; the slogan sentence gains its "On this map" scope tag. The Conclusions list is
   renumbered to five findings (v16's (1), (3)→(2), (4)→(3), (5)→(4), (6)→(5)) plus two
   definitional notes (A = the identity; B = the rule-level structural block, i.e. the
   tautology note). The abstract follows the same demotion (its (2) becomes the unnumbered
   definitional-note sentence; its (5) merges into the new (2)).
4. **"§3.7 / §4 expansion contradiction resolved consistently across §3.7, Figure 4, §4, and
   Conclusions: expansion is not an artifact of the particular pinned value (holds for every
   admissible K ≥ 2K*), and is explicitly conditional on K ≥ 2K* = 1769.2."**
   → **Implemented, and verified.** The v16 tension was real: §3.7/Figure 4 said "not an
   artifact of the pinned carrying capacity" while §4 said "conditional on the bound-pinned
   carrying capacity". Verified facts: (i) pure algebra — F′(K*) = 1 + r(1 − 2K*/K) ≥ 1 ⟺
   K ≥ 2K* = 1769.2 kt (2K* = 2 × 884.6); (ii) the admissible box is (940.75, 5000] kt, so
   expansion holds on [1769.2, 5000] but contraction is admissible on (940.75, 1769.2); (iii)
   Table 3's r and F′(K*) columns reproduce exactly at every grid K (recomputed from
   `wave_e_cod/data/`); (iv) the fit cost does rise below 2K* (SSE falls monotonically
   521,053 → 407,523 → 356,392 → 338,773 → 330,318 → 320,230 → 314,899 → 309,371 → 306,532
   kt² for K = 1000 → 5000). v17 states one consistent reading in all four sites: not an
   artifact of the particular pinned value (holds for every admissible K ≥ 2K*), explicitly
   conditional on K ≥ 2K*, data-selected within that range.
5. **"Freeze date stated as prior to scoring; post-freeze objects disclosed."**
   → **Verified already present in v16** (frozen 2026-08-26 "before any kernel, boundary, replay,
   or retention score was computed", stated in §1 and §2.1; §2.1 lists the post-freeze objects).
   Retained; only the rule's name in those statements follows the rename.

**Additional numerical re-verification of v16's frozen layer (all reproduce, source-year
convention, from `wave_e_cod/data/`):** r = 0.236869; residual mean −10.88, SD 114.91 (sample,
ddof = 1), min −328.97, max +206.55; q05 = −287.36, q10 = −80.87; lag-1 autocorrelation 0.554;
g_max = rK/4 = 296.1; g(K*) = 172.46 (Result 3.3's "172.46 − 80.87 = 91.59"); F′(K*) = 1.1531;
the r_T chain 329.0 / 708.4 / 1146.1 / 2232.4 / 3675.2 with K* + r_7 = 4559.8 < K and
K* + r_8 = 5451.3 > K (the certified horizon T = 7).

**Registered residual (deliberately NOT changed in v17 — outside the described scope):**
§3.6's "residual SSE 7690.1 kt² against 12,772.2 kt²" — 12,772.2 is the **MSE** (SSE 306,532.1 /
24), and by the same scaling 7690.1 and 13,873.1 are MSEs, so the first occurrence's "SSE" label
is a one-word mislabel (the audit's priority-1 "reconcile SSE" item, half-answered already by the
joint evaluation's A2-labelling note). One-word fix at owner acceptance; noted here and in the
joint evaluation's (D-b) block.

---

## 3. E3 — item-by-item evaluation and disposition of the described "E3 v11"

Base: this repository's `paperE3_edwards_forecast_ladder_v11.md` (Task 69's batch-7
implementation; unpushed local commit `8e67c97`). The parallel sandbox's own "E3 v11" file is
lost; its described elements were evaluated one by one:

1. **New uncertainty section (their §5.7 / Table 8, DM + Künsch bootstrap on every head margin,
   computed from the registered per-origin forecasts).** → **Already present in v11 as §5.3.1**
   (8-row DM/bootstrap layer, seeded, on the same registered forecast files), verified equivalent
   in substance (Section 1 above). **Incorporated in v12**: the owner-archived campaign script is
   registered as an independent replication (paragraph in §5.3.1 + Data Availability + archived
   CSV), the two replication-only rows are registered in prose, and the DM 1995 / Künsch 1989
   citations are added (v11 credited the methods but cited nothing).
2. **"Abstract/Implications/Conclusions lead with causal-loses → AR(1) coin-flip → climatology
   wins at h=5 → nowcast skill."** → **Already present in v11** (abstract, Impact Statement,
   Conclusions all lead with exactly that sequence) — verified, no change needed.
3. **"Protocol kink resolved: climate rung's comparator corrected from the declined M2m to the
   retained M1; Proposition 5.3 proof updated."** → **Incorporated in v12, after verifying which
   statement is the frozen one.** The frozen Pass-2 protocol document
   (`wave_e_edwards/protocol_pass2.md`, locked 2026-08-25) states the climate question as
   "reduce primary RMSE on J-17 relative to persistence **and relative to M1**"; M2m-as-
   comparator appears in no frozen document (grep of all four protocol/specification files).
   The v10/v11 papers' "declared nested comparator M2m" was therefore the papers' own
   (mis)statement — v11 had disclosed it as a kink; the audit demanded resolution. v12 corrects
   the comparator to the frozen document's M1: §4.1 deviation #2 is rewritten (the correction
   disclosed), the §5.4 narrative restates the rejection on the frozen gate (the three modules
   are *listed* by within-noise point margins against persist and M1; not retained on three
   stated grounds — within-noise gate margins, h = 5 persistence failure, and no forecast
   structure beyond the declined M2m class), and the M2m margins are kept as a nested-baseline
   reading (Table 7's caption relabelled). **No frozen verdict changes** — no climate module is
   retained under either statement — and the corrected mechanism matches the repo's own final
   edition's reasoning (wave_e v2: "they are M2m with a weakly adjusted intercept and do not
   constitute additional forecast structure"). v11 has no "Proposition 5.3" (propositions were
   converted to result sentences there); the equivalent passages are the ones restated.
   The §6 "entire causal ladder is rejected" sentence is qualified for precision.
4. **"'Certificate for current year' recast into the nowcast/forecast/contemporaneous-accounting
   trio."** → **Already present in v11** (§6: the word "certificate" retired; the map with
   realized fluxes is a nowcast (7.55 ft); the contemporaneous increment ΔH_t–R_t closure
   (r = 0.74) stated) — verified, no change needed.
5. **"'Pre-registered' → fixed computational protocol frozen before scoring."** → **Already
   present in v11** (§4.1: "The design is a fixed computational protocol rather than a
   prospective clinical-style registration; the phrase 'pre-registered' is avoided for that
   reason"; freeze dated; deviations in one place) — verified, no change needed.
6. **"Diebold & Mariano 1995 + Künsch 1989 references; results table + companion script
   registered."** → **Incorporated in v12** (references with hooks; Table 6 label for the
   §5.3.1 table; Tables 6→7, 7→8 renumbered; script + CSV registered in Data Availability).
7. **Their §5.7 placement and Table 8 numbering.** → **Declined as literal layout**, reason
   recorded: this repo's v11 already implemented the same layer as §5.3.1 (placed with the
   retention verdict it qualifies), and renumbering v11's section structure to imitate a lost
   file would churn the already-implemented paper for no content gain. The substance (the
   layer, its verification, its registration, its citations) is fully incorporated.

**Non-destructiveness of v12, verified mechanically:** the only table-row difference between
v11 and v12 is one label ("M2_combo − M2m (climate gate)" → "(nested baseline)"); every value
is identical; no score, verdict, or archived number changed.

---

## 4. Standing constraints honoured

- No file in `arena agent 1/` was modified: the two new versions are new files
  (`paperE2_cod_intervention_v17.md`, `paperE3_edwards_forecast_ladder_v12.md`); v16 and v11 are
  untouched baselines.
- No frozen verdict, no reported score, no kernel, no boundary, and no archived number changed
  in either paper (verified by table-row diff and number-level diff).
- The batch-7 audit directory holds only additive audit artifacts (the build script, the
  verified CSV under `results/`, this record, and the joint-evaluation update).
- The E4 v11 (Task 69) is untouched — the owner's message concerned E2 v17 and E3 v11 only.

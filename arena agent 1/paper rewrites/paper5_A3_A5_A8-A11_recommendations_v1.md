# Paper 5 — profound recommendations for the author-blocked items (A3, A5, A8–A11)

v1 — 2026-09-11. Basis: audit v1 (397 lines) + audit v2 (225 lines) reread in full;
v30 manuscript (`paper5_sampled_governance_v30.tex`, 120737 B); deposited
Aug-08 analysis files; `stage_scan_recovered/` rerun outputs; independent
numerical verification of the A3 fixed point (this round). Nothing below is a
decorative edit: every recommendation states the root finding first, then the
precise action, then how the author checks it.

## 0. Cross-cutting: the A6 rebuild resolved three fork-conditional items

The audits were written pre-fork. A6 went **REBUILD** (v30), which settles:

1. **A10-retitle: closed, no retitle.** The retitle ("detectable"→"diagnosed")
   was R2-tied to the reframe fork (audit v1 §2 cap "(R2)" = "preconditioned on
   the A6 reframe fork"). Rebuild keeps the screen as a result, so the title
   stands. A10 is now compression-only.
2. **A5 band-stakes: severed.** v30 §2.4 derives the screen bands from model
   predictions (four-state + stage-map, D10), not from §3.3's archived
   diagnostics. Qwen's band-provenance concern is therefore moot as a
   band-dependence question: §3.3's status no longer propagates to any band.
   The §3.3 restructure now serves disclosure readability and §4.1's honesty
   — still worth doing (R/Q agree it is), but its failure mode is presentational,
   not inferential. Scope the work accordingly.
3. **A11 fork-gate: open.** The audit plan gated R's §5.3 sensitivity battery on
   rebuild-only ("rebuild only" — audit v1 §4 sheet). That gate is now open:
   the battery is executable (the rebuilt pipeline exists) and its absence is
   the largest remaining evidence gap in the paper. §0.3 below is the
   highest-priority recommendation in this document.

---

## A3 — Table-3 full vector + interiority + pointer (do it; verified this round)

**Root finding.** The "not listed here → computational record (this appendix)"
pointer is dangling in two senses: the appendix contains no such record section,
and the constants' code home was never pinned. This round located both:

- The full baseline vector lives in `droop_test.py` L49–58 (Candidate A base
  core constants block): `K=100.0, qc=0.001, Emax=30.0, eta=0.914,
  delta0=0.01, Dref=1.0, taum=5.0, Zref=1.0, k=10.0, delta=ln2/10`, with
  `r=0.02` passed as the validation argument (L357) — the same constants are
  imported by `noise_robustness.py`, so they are the shared calibration, not a
  one-script happenstance.
- The fixed point is computed by `base_equilibrium` (L86–93): `Z*=delta`,
  `E*` the positive root of the effort-law quadratic, `N*=K(1−qE*/r)`.

Independent verification against §2.1's printed equations (replicating
`base_equilibrium`'s arithmetic exactly):

- `E* = 2.089623` (target 2.08962 ✓); the quadratic's other root is
  `−0.010182`, so the interior rest is unique among physical roots.
- `N* = 89.551883` (target 89.55188 ✓). `Z* = δ = 0.06931472` exactly.
- `Φ_k(0) = δ` to machine precision; `sp_k′(0) = 1/2` exactly (k cancels —
  state this, it is why the slope claim needs no numerical qualification).
- `s* = 0` uniquely: at any equilibrium with N > 0, Ṅ = 0 ⟺ qEN = S(N) ⟺ the
  deficit argument of Φ is 0. The "uniquely" is a one-line consequence of (1),
  not a numerical claim.
- Π-interiority: `E* = 2.09 ∈ (0, 30)`; Φ-floor non-binding near 0
  (Φ_k(0) = δ > 0, continuity).

**Recommendation.**

1. Table 3: delete the grouped "not listed here" row; add seven printed rows
   (r = 0.02, K = 100, E_max = 30, Z_ref = 1, δ_0 = 0.01, Δ_ref = 1, τ_m = 5,
   each "Stated at: this table (baseline calibration; code constants block
   `droop_test.py` L49–58 @ commit)"); update the fixed-point row to
   `(89.55188, δ, 2.08962)` with an interiority note
   ("E* ∈ (0,E_max); Φ_k(0)=δ, floor non-binding; sp_k′(0)=1/2").
   Printing the values **dissolves** the dangling pointer rather than fixing
   it — no pointer is needed once the values are in the table.
2. §2.1: one sentence after the Φ_k display —
   "Φ_k(0) = δ gives the equilibrium deficit s* = 0 uniquely with
   sp_k′(0) = 1/2, and the fixed point is interior to the nonsmooth regions
   of Φ_k and Π (values: Table 3)." This is the sentence both audits ask for;
   the verification above is its evidence base.
3. Cite the code home honestly: the constants block sits in a file named
   `droop_test.py` whose subject is a *different* (negative, correctly
   excluded) experiment. Cite as "base-core calibration (constants block)"
   with path + line range + commit — never as "the Droop test" — so no reader
   infers the baseline depends on the nutrient-coupling study. (If the author
   prefers, relocate the constants to a campaign module; that is taste, not
   substance — the pin is what matters.)

**Check.** Recompute E*/N* from the printed §2.1 equations (5 lines); confirm
Table 3 has no remaining "not listed here" row; confirm the commit pin resolves.

## A5 — §3.3 restructure + decomposition (do it; corrected grid)

**Root findings (three corrections to the audit plan's data description).**

1. **Grid mismatch.** The plan scopes "core cells g ∈ {1,2,5,10,20} ×
   η ∈ {0.914, 3.0}". Neither file matches: `tau0_out.txt` §A tabulates
   g ∈ {0.5, 1, 2, 5, 10, 20} (g = 0.5 present) while `rwin_out.txt` scans
   g ∈ {0.5, 1, 2, 5, 10, 15, 20, 50} (g = 15, 50 extra). Transcribe the
   τ₀ grid as-is (12 cells); pointer, don't silently drop, the rwin-only cells.
2. **Two "raw window" numbers per cell.** At (g=5, η=0.914): rwin-scan gives
   [0.00754, 0.36675] but tau0-scan's raw gives [0.0076, 0.3705] — different
   beyond rounding (separate scans: `stage_r_window.py` vs
   `stage_tau0_decomposition.py`). Likewise crossings: rwin counts *grid
   points* at r ≥ 0.2 (13) while tau0 counts *crossings* (raw 12,
   institutional 8). The supplement tables must label scan-source and
   count-definition per column, and §3.3's paragraph must use one source
   consistently (recommend tau0_out's, since the paragraph centres on the
   decomposition; cite rwin for the g = 0 validation + extended grid).
3. **§3.3's existing transcriptions are exact** (audit against
   `stage_decomp_results.md` §2): the g = 2 band r ∈ (0.77, 0.81) / delay
   2.6–7.8 yr, the g = 1 band 1.565–1.585 / 1.6–3.5 yr, and the slow-stock
   cohort cycle P ≈ 250–360 yr all match; decomp2_out's τ₀ classification
   (P₀ = 358.7 yr at r = 0.02, g = 5) is consistent. Nothing in §3.3 needs a
   numerical correction — the restructure is purely architectural.

**Further scoping results.**

- The τ₀ decomposition does **not** resolve §3.3's "no decomposition has
  established whether the baseline term, signal regularisation, or another
  controller component dominates" sentence: that sentence is about
  *controller-component* dominance, the τ₀ work about *mechanism* (cohort vs
  institutional-delay) separation. The new decomposition paragraph must not
  claim to answer it; leave that sentence intact.
- The g = 5 middle band (τ-window 9.9–20.3 yr) is correctly absent from the main
  text (grep confirms no "9.9"/"20.3" in v30): it belongs in the supplement
  band table, transcribed from decomp §2's table (g = 1/2/3/5 rows) with that
  table's honest caveats ("mapped at finite resolution; not
  collocation-classified"; "g = 7, 10 bands deviate from rg ≈ 1.5–1.6").
- The cod-class implication (middle band overlaps the cod range but is
  confounded with cohort resonance — decomp §2(c)) may be stated in the
  decomposition paragraph **without touching §3.7's four-state sentence**:
  the four-state 15–25× mismatch and the stage-model confounded match are
  different operators; cross-operator discipline (audit v2 J3 §5.3) requires
  they never share a sentence.
- `sampled_governance_results.md`'s "one-sentence manuscript refinement" (the
  continuous cod middle band does not survive sampled governance) has **no
  manuscript target**: the merged middle-band claim it would refine is not in
  the text. No action — record-level note only. (Its genuine content, the
  T_r-ranked cross-sectional test, was never executed; it is §4.5 fodder at
  the author's option, not a requirement — the screen stands as the T_r ≈ 1
  null.)

**Recommendation.** Restructure §3.3 into: (i) the windows paragraph as now
(keep; append a supplement-table pointer); (ii) a new decomposition paragraph
built on the (g = 5, η = 0.914) illustration — raw r-window [0.0076, 0.3705]
vs institutional-only [0.2660, 0.3285], fish-r crossings 12 → 8 — stating the
within-operator discipline in one sentence (separation of mechanisms under one
operator; the cross-operator comparison of §4.1 is not claimed isolated);
(iii) supplement tables: the full 12-cell τ₀ table (raw window,
institutional-only window, crossings raw/institutional, scan-source labelled)
+ the decomp §2 band table (g = 1/2/3/5) + pointers to the full logs. Optional
strengthening (same scope, author's call): cite the cod-class
sampled-governance stability result as the §4.4(iii) illustration — condition
(iii) ("sampled-data analysis removes a continuous-delay band") currently
states without an instance what the deposited computation demonstrates.

**Check.** Every §3.3 number traceable to a labelled supplement cell; the
rwin/tau0 dual-source note present; the controller-component sentence untouched;
no sentence mixing the four-state mismatch with the stage-model band.

## A8/A9 — keep / leave (close both; the text already justifies it)

**A8 root.** The Notation paragraph (§2.1) already scopes S explicitly:
surplus production in the control sections, SSB (reported as SSB in Table 2)
in the cod sections, with "the two scopes of S never share an equation" and no
other symbol serving two sorts. A rename would churn §§2.7/3.8/Table 2 to
resolve an ambiguity that the scope statement already eliminates — there is no
shared equation in which a reader could misbind S. **Recommendation: keep;
close the item with no edit.** (If a referee demands it, the fallback is
SSB-subscripting in Table 2 only — the one place the cod scope surfaces
tabularly.)

**A9 root.** The H1→subsection numbering is consistent (Introduction = §1 …
Conclusion = §5, appendices lettered); journals reflow hierarchy at typesetting
regardless. Renumbering risks cross-reference drift across ~1900 lines for zero
referee-facing gain. **Recommendation: leave; close with no edit.**

## A10 — compression without renumbering (do it; retitle settled; map below)

**Root finding: the redundancy is mappable, not atmospheric.** The same claims
recur at fixed addresses (v30 line numbers):

- "Descriptive partition / split is the positive content": §3.8 (~L1349–1355),
  §4.3 (L1512), Box 1, Conclusion, §4.7(vi) — 5×.
- "Formulation-dependent crash interpretation": abstract, §3.8, §4.3, Box 1 — 4×.
- "Obstruction scope" (exact-trajectory class only): §3.8 (~L1415–1430), §4.3
  (L1524–1528), §4.7(vii) — 3×.
- "Falsification benchmark": §4.3, §4.5 — 2× (legitimate forward-reference; keep).
- §4.1's first paragraph (~L1457–1480) restates the §3.4 comparison record
  (crossings, q-sensitivity flips) before delivering its one new moral
  (operator as testable component) — the restatement is compressible to a
  pointer.
- §3.7 (~L1269–1348) is the longest demonstration: the zero-count search, the
  three-group partition, the anchoveta comparison, and the budworm/Russell
  hypotheses each restate the null before adding their clause.

**Recommendation.**

1. Results (§§3.5–3.8): one finding-sentence + one method-limit sentence per
   demonstration; move surviving detail to the supplement only where it is
   evidence (numbers), never where it is restatement.
2. Discussion (§§4.1–4.4): keep only operator-relevant morals (§4.1's testable-
   component moral; §4.2 as-is — see A11; §4.3 reduced to the benchmark
   forward-pointer; §4.4's five conditions verbatim — they are the paper's
   contract with refutation and must not be summarised). §4.5 intact, Appendix B
   intact (per the audit plan; the integration at §4.6 is load-bearing for the
   cod case's measurement-level claim).
3. Box 1 stays a summary, but delete any sentence duplicated verbatim in §4.3 —
   Box 1 should compress, not echo.
4. Notation table: the prose Notation paragraph already *defines* every symbol,
   so a table's only non-decorative function is lookup consolidation +
   gap detection. Draft it as 15 rows with a "defined at" column —
   N, Z, E; P_Tr, DP_Tr(X*), Π; Φ/Φ_k, δ, k, δ_0; F_B, A_n, O; S(·);
   plus g (→ §3.3), C_E/C_Z (→ §3.4), the §3.7 four-state (A, J, Z, E),
   and the Table-2 cod scope (S/SSB, s, K, C(t), M/M_x, F) as one grouped row —
   and treat any row lacking a definition site as a gap to fix in text, not in
   the table. If every row resolves to the existing paragraph, the author may
   legitimately decline the table; the decline criterion is that test, not taste.

**Check.** Each listed claim appears once as finding (Results) + once as moral
(Discussion) at most; Box 1 shares no verbatim sentence with §4.3; §4.4's five
conditions byte-intact; notation-table rows all resolve or expose a named gap.

## A11 — first-use note + §5.3 battery (highest priority; redraft required)

**Root finding: R's prescribed sentence is triply inapplicable post-rebuild.**
"Non-archival, illustrative application; no confirmatory weight" was drafted for
the reframe fork. Under rebuild: (i) *non-archival* is false — the materials
are archived (A1) with content hashes; (ii) *illustrative* is false — the screen
is a reported result (§§3.5–3.6), not an illustration; (iii) *no confirmatory
weight* contradicts §4.2, which stands — the null's stated refutation value
(robust target-band cycles are not common in assessed-stock records) is a
legitimate, bounded inferential contribution. Adopting R's sentence verbatim
would therefore misstate the paper's own evidence architecture. What survives
from R is the demand both audits endorse: a first-use status note exists at
§2.4 — but its content must be written for rebuild status.

**Recommendation.**

1. First-use note at §2.4 (rebuild-status redraft, author's wording to finalise):
   *"The screen is a restricted result: its weight is limited to the refutation
   stated in §4.2; materials archived (Appendix A); robustness battery §5.3
   [reported | specified in §4.7 — delete as applicable]."* — with the §3.5
   pointer R asked for. Keep §4.7(iv) verbatim: F31 (AR(1) may understate
   low-frequency power) still stands, and the battery below is what tests it —
   the caveat and the check cohere.
2. §4.2 stands as-is (no Russell revision — that was reframe-only; the
   precedent-analog is intact under rebuild).
3. Execute the §5.3 battery — now the paper's largest evidence gap. None of the
   five exists in the repo (verified: `noise_robustness.py`'s AR(1), ρ = 0.6,
   is assessment-noise on the *stage model*, not screen sensitivity —
   DeepSeek's mislocation, confirmed inapplicable; the screen pipeline has no
   sensitivity branch). Specs, in execution order:
   - (a) **Block bootstrap** (assumption-lightest): resample block-lengths
     spanning the AR(1) decorrelation scale; pass = 0/42 SOI-clean verdict
     stable across block choices.
   - (b) **Detrending sensitivity**: linear vs HP vs first-difference
     pre-treatment; pass = verdict pattern (0/42 clean, 2/42 Taylor) stable.
   - (c) **ARMA(1,1) null**: replace the AR(1) surrogate with ARMA(1,1) fitted
     per series; pass = band-power verdicts within stated precision.
   - (d) **Trend-stationary null**: deterministic-trend + stationary-noise
     surrogate; pass = same.
   - (e) **Regime-surrogate**: piecewise-stationary surrogate with one break
     (median-split, then break-date sensitivity); pass = same.
   
   Pass criterion throughout is *verdict stability*, and any flip is reported
   as a scope restriction, never buried. The honest alternative, if execution
   is deferred: state in §4.7 that the battery is specified-but-unexecuted and
   preregister these specs — a legitimate preregistration-pattern outcome, not
   a failure — but do not leave the gate silently open.
4. Not required: the sampled-governance T_r-ranked test (never executed; §4.5
   fodder at author's option).

**Check.** §2.4 note present with rebuild-true content; §4.7(iv) intact; battery
reported with verdict-stability table, or §4.7 carries the specified-but-
unexecuted statement with these specs.

## Erratum (2026-09-11, same day, before build)

The A11 battery specs above mislabel the pass criteria: "0/42 SOI-clean"
and "2/42 Taylor" conflate the screen verdict with the §3.7 anchoveta
analysis. Corrected attribution (verified against v30 text): the battery
target is the 42-stock screen whose verdict is the **BH-adjusted zero count
over 84 target-band cells** (`verify_bh.py`, 0 rejections); the "0 of 90"
SOI figure belongs to the §3.7 anchoveta index–lag grid, a different
analysis. The v31 build implements the corrected spec (verdict stability of
the BH-adjusted zero count), and the executed battery holds it 11/11.

## Execution order (author's build sequence)

A11-battery decision first (it determines §2.4-note wording and possibly §4.7);
then A3 (mechanical, verified); then A5 (transcription + one new paragraph);
then A10 (compression pass); A8/A9 already closed. "v6" is not specified in this
round's instructions and is not built here.

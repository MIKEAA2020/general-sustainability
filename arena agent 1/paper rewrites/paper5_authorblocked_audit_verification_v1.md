# Joint verification of the two author-blocked audits (DeepSeek + Qwen)

Target: `paper5_sampled_governance_v29.tex` + `paper5_supplementary_v7.md`, repo
evidence as of 2026-09-11, prior round `paper5_audit_verification.md` (§§1–11)
and `paper5_A1-A11_rootcause_report_v1.md`. Line numbers are v29 unless noted.
Verdict scale: CONFIRMED / PARTIAL / WEAK / REJECTED, each with v29-line evidence.
Both auditors reason largely from the root-cause report (DeepSeek cites "the
report" and the v29 fix list; Qwen cites "4139 repo paths"); Qwen additionally
shows direct manuscript knowledge (v4.66, band numbers, Appendix B, §3.5–3.7).

## 0. Auditor-accuracy notes (read first)

- Neither auditor was given the manuscript, but Qwen's specifics (RAM v4.66,
  4–8/12–60 bands, Appendix B, §§3.5–3.7) all check out against v29 — Qwen either
  read the text or the report very closely. DeepSeek is explicit about working
  without the text for A8/A9 and from the report elsewhere; its repo numbers
  (decomposition windows, parameter values) are exact.
- Both auditors miss the same two textual facts, which reverses two
  recommendations: (1) the A6 disclosure they prescribe already exists in ~8
  locations including the abstract; (2) the F31/A11 clause they debate already
  exists as §4.7(iv). Several "actions" are therefore already-executed — verified
  below item by item.
- Convention: "strengthen" = the recommendation survives with corrected
  reasoning/scope; "complete" = the auditor left a gap this report fills with
  v29 evidence; "defect" = a verifiable factual error, corrected.

## 1. DeepSeek — item verdicts

### 1.1 A3 disclosure policy — PARTIAL (sound split, stale delta, two misfilings)

Values quoted (r, K, q, η, Emax, δ, Zref, A0, H, four classes) are all correct
against code. But against v29 Table 3 + text:

- Already stated (no action): q, k, η (Table 3); δ = ln2/10 (v29 §2.1 + Table 3);
  A0 = 100, h = 0.75 + sensitivity {0.6, 0.9} (Table 3, §3.4 Plant para);
  M/τ classes with sources (Table 3); FD step 1e-6, grid, trajectory settings
  (Table 3). DeepSeek's Table-3 list is ~60% already satisfied.
- True remaining delta: r, K, Emax, Zref (DeepSeek's list) **plus δ0, Δref, τm**,
  which DeepSeek misfiles to the supplement as "sensitivity values"/"choices":
  δ0 = 0.01 and τm = 5 are BASELINE calibration, and Δref = 1 is missing from
  both of DeepSeek's lists entirely. A function-split must put all three with
  the baseline vector, not with q = 0.1 / H-sensitivity.
- "Supplement S_X" is a placeholder (completed in §4: S8 register + App-A
  pointer fix; see the dangling-pointer finding below).
- The positivity sentence DeepSeek prescribes is already in v29 §2.1 (F9).
- DeepSeek misses the strongest A3 fact (credit Qwen §2.1 for sensing it):
  Table 3's grouped row points at "computational record (this appendix)" for
  r, K, Emax, δ0, Zref, Δref, τm and the fixed point — and App A contains NONE
  of these values (grep-verified). The pointer dangles. This converts A3 from
  "policy" to "policy + one broken pointer."

**Strengthened A3:** disclose the full 8-parameter baseline vector + fixed point;
placement per §4; fix the dangling pointer regardless of placement.

### 1.2 A5 archive role — PARTIAL (exact numbers, backwards mechanism gloss)

- Numbers exact: tau0_out η = 0.914 block, g = 5: raw [0.0076, 0.3705],
  institutional-only [0.2660, 0.3285] ✓. (DeepSeek correctly used the η = 0.914
  block, not the η = 3.0 block below it.)
- Defect 1 — "it verifies the main-text calculations": backwards. The archive is
  the UNVERIFIED object (generating computation unattached; §3.3 provisional).
  Its checkable parts are the g = 0 validation (reproduces base windows
  (0.00796, 0.0219)/(0.00676, 0.0603)) and the RK4 dt-convergence, not
  verification "of the main text."
- Defect 2 — "the delay contributes a large share of the raw window": loose to
  the point of misreading. Correct reading: most of the raw window is
  τ = 0-unstable (biological cohort mechanism); the institutional-delay-induced
  part is the narrow HIGH-r slice [0.2660, 0.3285] — narrower and shifted UP,
  not "the delay's large share." Unmentioned supporting detail: fish-r crossings
  raw 12 vs institutional 8 at the same cell.
- Gap: no engagement with the actual A5 stakes (do the empirical bands depend on
  the archive?). Completed in §3 (J-A5).

**Strengthened A5:** keep + cite the decomposition as a sensitivity result with
code location (`stage_scan_recovered/`, tau0 decomposition) and the corrected
reading above; the "verification" framing is rejected.

### 1.3 A6 registration materials — PARTIAL (right severity, false premise, weak remedy)

- "Described as if it were reproducible" is FALSE. Non-attachment is disclosed in
  the abstract (L52), Box 1 (L123–127), §2.2 (L453–461), §3.3 (L826), §3.4
  (L1081), §4.7 (L1715), App A (L1755–1782), Data availability (L2068+), and
  supp S8. The prescribed "one-paragraph disclosure" exists eight times over;
  the gap is MATERIALS, not disclosure.
- "Available from the author on request" is a DOWNGRADE: Data availability
  currently promises deposit ("registration requirements... until those artifacts
  are attached"), and "on request" is journal-insufficient for a screen whose
  null result sits in the abstract and whose name sits in the TITLE. Rejected.
- The result/context distinction is the right test — but DeepSeek doesn't apply
  it. Applied (§3 J-A6): title + abstract + §3.5/§3.6 + §4.2's refutation claim
  make the screen a RESULT. By DeepSeek's own logic, that forces
  reconstruct-or-reframe, not a paragraph.
- "Reframe so the screen is not load-bearing" is sound but incomplete: no
  mention that reframing implies retitling + abstract rewrite + §4.2 revision
  (completed in §4).

**Strengthened A6:** see the §4 decision matrix. Disclosure: done. Remedy space:
deposit materials or reframe-with-retitle. "On request": rejected.

### 1.4 A8/A9 — WEAK (auditor admits no text) — COMPLETED here

- A8: keep. The S-overload acknowledgment exists at v29 L321–322 ("S is instead
  spawning stock biomass (reported as SSB in Table 2)"); a rename churns
  §§2.7/3.8/Table 2 for no reader gain. No repo aspect (prior round stands).
- A9: leave. Hierarchy verified consistent in the prior round (H1→subsection);
  journals reflow. No action.

### 1.5 A10 structural options — WEAK (generic) — COMPLETED here

"Does the central result survive without it" + "cut anything that does not carry
a claim" is unobjectionable process with zero paper-specific content. Completed
in §3 (J-A10) per option: claim registry ≈ Box 1 (exists); notation table
(partial: Table 1 is an ontology, not a symbol table); §3 split; paper split;
figures; Appendix B (jointly with Qwen §2.5).

### 1.6 A11 AR(1) — PARTIAL (right fork, wrong locus, stale clause, unapplied test)

- Defect (locus): "You have the comparator code; implementing an AR(1) variant
  is a modest addition" mislocates the item. The AR(1) item (original Qwen 5.3:
  "The AR(1) null may be too simple... If not feasible, state this as a
  limitation") concerns the SCREEN's spectral null, whose pipeline is missing
  (A6) — not comparator dynamical noise. Comparator-AR(1) would answer a
  question no auditor asked.
- The F31 clause DeepSeek debates already exists as §4.7(iv) ("the AR(1) null
  may understate low-frequency power," inside "the null is not proof of absence").
- DeepSeek's own centrality test, applied: the screen IS in the title and
  abstract — so the test says "run the check." But A6 blocks execution (no
  pipeline). Joint conclusion (§3 J-A11): clause-only until A6 resolves; the
  check-list (ARMA/block-bootstrap/detrending, per 5.3) becomes the gated
  prescription.

### 1.7 Process recommendation + meta-comment — CONFIRMED

A6-first sequencing is correct (only reframing-capable item); A3+A5 pairing is
sensible (both disclosure placement); "approve v29, then decide" matches the
executed order. The meta-comment (policy vs materials; A6 the sole genuine gap)
is accurate and is adopted as the frame for §4.

## 2. Qwen — item verdicts

### 2.1 A3 full disclosure — PARTIAL (right demand, triple-misdirected reasoning)

- Defect 1: "finite-difference artifact" suspicion of ρ = 1.00035 is misdirected.
  The logistic record is CLOSED-FORM monodromy (Box-1 L106/112; §3.4 L897; Table
  3 "200,001-point scan with bisection"). FD step 1e-6 belongs to the STAGE
  reconstruction only (Table 3, stage rows). A reviewer suspecting FD artifacts
  in the logistic margin is auditing the wrong object.
- Defect 2: "solver-tolerance issue" is likewise misdirected for ρ: the margin
  comes from deterministic linear algebra (expm), not solve_ivp, whose tolerances
  govern the nonlinear comparator trajectories only.
- Defect 3: "create a new Table 2" collides — Table 2 exists (northern cod SSB,
  L1400). The target must be Table 3.
- "Un-auditable and will be rejected" overstates: the margin's SIGN is
  triply corroborated (exact 1.00035, Euler 1.00055, undelayed Reλ > 0) and the
  record is re-execution-verified with validation gates. The honest fragility is
  parameter-tuning auditability, not numerical artifact.
- Credit: Qwen correctly senses the hiding place ("hidden in the 'computational
  record'"). Strengthened: the pointer doesn't just hide values — it resolves
  NOWHERE (App A contains none of them). That is the load-bearing A3 fact.

**Strengthened A3:** full baseline disclosure is warranted (near-unit margin +
dangling pointer), placed in Table 3 (no new Table 2); solver/FD settings stay
with their objects (comparator paragraph/S8), not because they are hidden but
because that is where they are auditable.

### 2.2 A5 decouple-and-demote — PARTIAL (true provenance, false circularity, unexecutable action)

- Provenance premise TRUE: bands "derived from the archived, unreproduced
  stage-map diagnostics" (§2.4 L521–524; peaks near 4/8 yr biomass, 12/60 yr
  effort) ✓; reconstruction does not reproduce anchovy/sprat windows ✓.
- Defect 1 — "fatal circularity": misdiagnosis. Theory-driven band selection
  with disclosed provisional status (Box-1 L125–127 + §2.4, status carried into
  the target definition) is hypothesis testing with quarantined inputs, not
  circularity. Nothing is hidden ("ghost in the machine" overstates twice-told
  disclosure).
- Defect 2 — the proposed re-banding is internally inconsistent: "3–8 year" and
  "10–20 year" bands vs the actual prespecified 4–8 / 12–60. The numbers shift
  without justification; "multi-decadal policy regimes" for a 10–20 yr band
  misuses "multi-decadal."
- Defect 3 — "superseded by the reconstruction... different stability
  boundaries" contradicts the manuscript's operator-locality logic: different
  operators (sampled vs continuous-delay); the governing stance is
  "uninformative rather than a non-reproduction" (abstract L55; Reading L1209).
  "Superseded" asserts a contradiction the paper explicitly refuses.
- Defect 4 — management-theory re-justification relocates provenance rather than
  repairing it (institutional-cadence bands need their own sourcing).
- Sharpest completion: Qwen's Action 1 (redefine bands) is UNEXECUTABLE without
  A6 — re-banding requires re-running the missing screen pipeline. A5-as-Qwen-frames-it
  is gated on A6, which Qwen never notes.

**Strengthened A5:** see J-A5. Decouple-via-rebanding: rejected as framed
(inconsistent numbers, operator-illiterate "superseded," A6-gated). Adoptable
core: bands debate belongs in the open; IF the author wants archive-independent
bands, that is a newly-authored, separately-sourced prespecification + a screen
re-run (A6-dependent), not a redescription.

### 2.3 A6 ultimatum — PARTIAL (right severity, overstated blast radius, correct v4.66)

- v4.66 vindicated: §2.4 L508–509 states "RAM Legacy Stock Assessment Database
  v4.66" — Qwen's "document the v4.66 extraction" is text-grounded (the repo's
  v466 ADH cohort is indeed a different analysis, but the version tag stands).
- Defect 1 — "credibility collapses": overstates. The screen is firewalled by
  the §3.5 three-way restriction (not proof of absence / not controller-sign /
  not causal), §4.2's bounded refutation, §4.4(v) (low-power nulls cannot
  adjudicate), and §4.7. Actual blast radius (§3 J-A6): title, abstract null
  sentence, §§3.5–3.6 status, §4.2's "what it refutes." Serious but bounded —
  neither collapse nor paragraph-fixable.
- Defect 2 — Path B's "formal, pre-registered execution remains a target for
  future work" misframes: prespecification EXISTS in-text (bands, BY fallback,
  stated detrending rule); what's missing is materials + identifier. An honest
  demotion is materials-framed, not prespecification-framed.
- Defect 3 — misses the title consequence: demoting §§3.5–3.7 while the title
  names the "Selected 42-Stock Spectral Screen" implies retitling (+ abstract
  rewrite). Also unnoted: §3.8 cod stays (DFO values published; only the
  constrained-mortality package is on the S8 open docket).
- Defect 4 — "missing falsification pipeline": overcouples. The falsification
  apparatus is §4.4 (five conditions) + §4.5 (prospective designs); the screen
  is one diagnostic, already limited by §4.4(v).

**Strengthened A6:** the ultimatum's fork is right (deposit or demote) with
corrected blast radius, materials-framed demotion language, and title/abstract
consequences — see §4.

### 2.4 A11 clause + sensitivity — PARTIAL (good gated prescription, incoherent clause)

- The sensitivity prescription (ARMA(1,1)/block-bootstrap if A6 resolves) is
  correct and matches original 5.3's fix list. Adopted, A6-gated.
- Defect 1 — the exact clause is REDUNDANT: §4.7(iv) already states the AR(1)
  limitation ("the null is not proof of absence... the AR(1) null may
  understate low-frequency power").
- Defect 2 — the gloss is statistically incoherent: if the null UNDERestimates
  low-frequency power, the threshold is too LOW, the test is LENIENT, and a
  zero-count is thereby strengthened — Qwen's "conservative lower-bound on
  target-band periodicity rather than a definitive absence" gets the direction
  backwards ("lower bound on periodicity" is meaningless for a zero count), and
  "definitive absence" is a strawman (§4.7(iv) already disclaims proof of
  absence; §3.5/§4.2 repeat it).
- Defect 3 — "a reviewer runs ARMA on your 42 stocks": impossible without A6
  materials; the scenario presumes the pipeline Qwen elsewhere says is missing.

**Strengthened A11:** keep F31; reject Qwen's clause as drafted; adopt the 5.3
sensitivity list gated on A6; an optional direction-fixed augmentation is
drafted in §4 (masked-peak risk runs via OVERestimated null power, not under).

### 2.5 A10 carve-the-marble — PARTIAL (merit in the diagnosis, four defects)

- Defect 1 — "entirely disconnected": false. Appendix B is integrated via the
  cod case (§4.6 L1693+: 2J3KL constituency, mismatch table, StatsCan series,
  S6 pipeline register) under the explicit "documenting the gap is the finding"
  design (§4.7(viii)). Qwen never engages that framing.
- Defect 2 — cost of keeping overstated: Appendix B is ~65 lines; its removal
  saves little and contradicts the §4.6/§4.7(viii) design the author already chose.
- Defect 3 — the paper split doesn't solve A6, it MOVES it: "Empirical
  Falsification of Institutional Feedback Cycles" as Paper 2 carries the same
  undischarged registration. A split is A6-orthogonal at best.
- Defect 4 — Parts 1/2/3 "restructure" mostly relabels the existing arc
  (theory §§2–3.2, spectra §3.4, screen/cod §§3.5–3.8, prospective §4.5); the
  substantive move inside it is the A6 demotion, not organisation. Editorial
  praise ("brilliant") is unusable per journal conventions.
- Residual merit: the "three papers" pressure is real IF the screen stays a
  result with missing materials — i.e., A10's sharp part is A6-contingent.

### 2.6 Summary path — CONFIRMED as process

Today/tomorrow/week sequencing is sensible; "drop Appendix B" inherits §2.5's
defects; "add the full vector" is actionable via the §4 Table-3 delta.

## 3. Joint adjudications (audits in conflict or complement)

### J-A3: split (DeepSeek) vs full-main-text (Qwen) — Qwen's placement, DeepSeek's tidiness, both corrected

The true delta is SEVEN numbers + one fixed point (r, K, Emax, δ0, Zref, Δref,
τm; N*, Z*, E*) — about three Table-3 rows. At that price, DeepSeek's
main/supplement split saves almost nothing, and the dangling "computational
record" pointer must resolve SOMEWHERE citable. Adopt: full baseline vector +
fixed point in Table 3 (Qwen's placement, on corrected grounds: near-unit-margin
auditability + pointer repair, NOT FD/solver fears); numerical settings stay
with their objects (comparator paragraph states H = 800/reviews/seeds-fixed;
solve_ivp tolerances to S8; stage FD settings already in Table 3). "New
Table 2" rejected (exists); δ0/τm/Δref classified baseline (DeepSeek corrected);
positivity sentence already present (both moot).

### J-A5: keep+cite (DeepSeek) vs decouple+demote (Qwen) — keep+cite, with Qwen's concern logged openly

Decisive facts: (1) band provenance is disclosed + quarantined (Box-1, §2.4);
(2) "superseded" is operator-illiterate (manuscript's "uninformative" stance
governs); (3) re-banding is A6-gated (needs a pipeline re-run) and Qwen's
numbers are inconsistent. Adopt DeepSeek (cite the τ = 0 decomposition as a
sensitivity result with code location + the §1.2 corrected reading) and reject
Qwen's Actions as framed — while logging Qwen's real concern (bands rest on
unreproduced computations the reconstruction doesn't confirm) as an OPEN author
note, since archive-independent re-prespecification remains available post-A6.

### J-A6: paragraph (DeepSeek) vs ultimatum (Qwen) — the ultimatum, materials-framed, bounded blast radius

Both agree on severity; DeepSeek under-remedies (disclosure exists; "on request"
rejected), Qwen over-blasts ("collapses") and misframes Path B. Joint finding:
the screen is a RESULT (title + abstract + §3.5/§3.6 + §4.2), so the remedy fork
is deposit-materials OR reframe-with-retitle — see §4 matrix. Blast radius:
title, abstract null sentence, §§3.5–3.6, §4.2's refutation sentence, Box-1
screen row; §3.8 cod and §§3.1–3.4 untouched either way.

### J-A11: centrality fork (DeepSeek) vs clause+prescription (Qwen) — clause stands, prescription gated, loci corrected

F31/§4.7(iv) already implements 5.3's fallback. DeepSeek's comparator locus is
corrected to the screen null; Qwen's clause is rejected as drafted (redundant +
backwards gloss) with a direction-fixed optional augmentation in §4; both
converge on: no checks possible until A6 resolves; then ARMA/block-bootstrap/
detrending sensitivity per 5.3.

### J-A10: generic process (DeepSeek) vs concrete carve (Qwen) — per-option verdicts

- Claim registry: exists (Box 1, "Claims at their exact evidential status").
  No action.
- Notation table: partial (Table 1 = ontology, not symbol table). Optional,
  cheap, author-taste. (Overlaps A8-keep.)
- §3 split / extra figures: no auditor makes a paper-specific case; v29's arc
  (methods → invariance/limits → archived regions → spectra → screen/power/
  cases) is coherent. No action without author motivation.
- Appendix B: KEEP (65 lines, §4.6-integrated, gap-finding design). Qwen's drop
  rejected with reasons (§2.5 defects 1–2).
- Paper split: REJECTED as an A6 remedy (moves the missing materials, doesn't
  cure them); as pure narrative taste it is author-optional and orthogonal.

### J-A8/A9: completed unopposed (§1.4). No conflict; Qwen silent.

## 4. Strengthened author decision sheet (corrected, actionable)

- **A3.** Add to Table 3: r = 0.02, K = 100, Emax = 30, Zref = 1, δ0 = 0.01,
  Δref = 1, τm = 5 (values code-verified, root-cause report §A3); fixed point
  (N*, Z*, E*) = (89.55188, δ, 2.08962). Add solve_ivp tolerances + seeds to S8;
  repoint "computational record (this appendix)" so it resolves (it currently
  dangles). Grounds: near-unit-margin auditability + pointer repair.
- **A5.** Keep archive; cite the τ = 0 decomposition in the supplement with code
  location and the corrected reading (raw window mostly τ = 0-unstable/cohort;
  institutional-only slice [0.2660, 0.3285] narrow and high-r; fish-r crossings
  12→8). Log Qwen's band-dependence concern as open; archive-independent
  re-prespecification stays available post-A6 (it needs a screen re-run).
- **A6.** Fork: (i) reconstruct + deposit (42 IDs, eligibility table, detrending
  rule code, spectral routines, power code + seeds, query log, periodogram CSV —
  Zenodo/repo, NOT "on request"); or (ii) reframe: demote §§3.5–3.7 to
  prospective/preliminary WITH retitle (screen leaves the title), abstract
  rewrite, §4.2 revision, Box-1 row restatement; §3.8 + theory untouched.
  Materials-framed demotion language (prespecification already exists in-text).
- **A11.** Keep §4.7(iv). Optional direction-fixed augmentation: the masked-peak
  risk runs via OVERestimated null power (e.g., unmodelled observation-error
  or retrospective-bias variance raising the threshold), not via the
  underestimation Qwen/F31 already cover. If A6 resolves: ARMA(1,1),
  trend-stationary, block-bootstrap, regime-shift-surrogate, and detrending
  sensitivity (5.3 list) in the supplement.
- **A10.** Keep Appendix B; no split for A6 reasons; notation table optional;
  claim registry done (Box 1); §3/figures only on author motivation.
- **A8/A9.** Keep/leave as reasoned in §1.4.

## 5. Defects corrected (auditor errors with fixes)

D1 DeepSeek-A3: δ0/τm misfiled as sensitivity values → baseline. Δref omitted →
  added. "S_X" → S8 + pointer fix. Positivity "to add" → already present.
D2 DeepSeek-A5: "verifies main-text calculations" → archive is the unverified
  object; g = 0 validation is the check. "Delay's large share" → corrected
  τ = 0/institutional reading + crossings 12→8.
D3 DeepSeek-A6: "as if reproducible" → disclosed ×8 (list in §1.3). "One
  paragraph" → materials are the gap. "On request" → rejected (downgrade).
D4 DeepSeek-A8/A9/A10: admitted-generic → completed with v29 evidence (§1.4, J-A10).
D5 DeepSeek-A11: comparator-AR(1) locus → screen null (5.3). F31 "to add" →
  exists (§4.7(iv)). Centrality test applied ⇒ run-if-possible, A6-gated.
D6 Qwen-A3: FD-artifact fear → logistic is closed-form (FD is stage-only).
  Solver-tolerance fear → ρ is expm, not solve_ivp. "New Table 2" → collides;
  use Table 3. "Un-auditable" → triple-corroborated sign + re-execution.
D7 Qwen-A5: "fatal circularity" → disclosed, quarantined hypothesis testing.
  "Ghost" → disclosed twice. Re-banding numbers → inconsistent + "multi-decadal"
  misused. "Superseded" → operator-illiterate; "uninformative" governs.
  Re-justification → relocates provenance; re-banding → A6-gated.
D8 Qwen-A6: "collapses" → bounded blast radius (listed). Path B
  prespecification-framing → materials-framing. Missing title consequence →
  retitle required. "Missing pipeline" → screen is one diagnostic (§4.4/§4.5
  are the apparatus).
D9 Qwen-A11: exact clause → redundant with F31; "conservative lower-bound" gloss
  → backwards + strawman ("definitive absence" never claimed); reviewer-runs-ARMA
  scenario → A6-gated. Direction-fixed augmentation drafted instead.
D10 Qwen-A10: "entirely disconnected" → §4.6-integrated, gap-finding design.
  Drop-App-B savings → ~65 lines. Split → moves A6, doesn't cure it. Parts
  1/2/3 → relabeling; real move inside is A6 demotion.

## 6. Completeness re-sweep

- DeepSeek process recommendation (§1.7): assessed, adopted (A6 first).
- DeepSeek meta-comment: adopted as §4's frame (policy vs materials).
- Qwen summary path: process-confirmed; content items folded into §§2–4.
- Both auditors' shared blind spots (pre-existing disclosure ×8; pre-existing
  F31; title consequence; A6-gating of A5-rebanding and A11-checks; dangling
  "computational record" pointer) are now explicit above — these five are the
  value-add of joint verification against v29 rather than against the report alone.
- No manuscript edits made in this round (evaluation only). Standing rules
  (new versions only; no superseded-version references; no change-log in paper)
  respected throughout; the "superseded by" language proposed by Qwen-A5 is
  rejected partly on these grounds as well.

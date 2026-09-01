# P4 five-regime continuation data — provenance, exact names, repo presence

Date: 2026-09-02 (turn 55). Answers the three questions: which chat is Task 52; the exact
name of the continuation data; which original repo papers carry the numbers.

## 1. Which chat is "Task 52"

Task 52 is a task entry in the repo's own **`worklog.md`** (line 1085):

> Task 52 — general-sustainability: draft the three remaining assured-core manuscripts
> (Papers 3, 4, 5) from the row-closed concordance…

Executed by **"Agent: main (Z.ai Code) via manuscript-drafting subagents (52-a Paper 3,
52-b Paper 4, 52-c Paper 5)"** (worklog line 1086). Its repo commit is **`68f4eee`**
(2026-08-28, commit author "Z User <z@container>"): "Task 52 — Papers 3, 4, and 5 are
DRAFTED…". So the Task-52 chat is **the user's Z.ai Code session** in which the draft of
`papers/paper4_delay_dynamics/manuscript.md` (entry 52-b) was produced. The drafting
session *stated* the five-regime numbers from the concordance rows — it did not compute them.

The computations behind the numbers live in earlier chats, also identifiable in the repo:
- The **A018 source authoring** ("ecol" workspace): `uploads/manuscript.txt` arrived in
  commit `6ef8299` "Upload complete healthy research workspace from ecol extracted"
  (2026-08-23, author MIKEAA2020). Its §6 carries the five-regime evidence.
- The **Z.ai Code fold/orbit sessions**: worklog Task 1 ("Clone repository, identify and
  complete unfinished computations (fold, orbit, Floquet, branch certification)") completed
  the A025 collocation/continuation scripts; **Task 31** (post-v1.0 session) rebuilt the
  A025 fold pipeline (worklog cites commits `65c8a90`, `3f1cbc5`) and the C4 monodromy
  dt=0.1 (commit `365e111`).

## 2. Exact name of the continuation data we need

The P4 manuscript's own designation: **"the publication-artifact archives (branch, Floquet,
history, solver, and environment artifacts)"**, plus **"the sampled-numerics documentation
action"** (P4 §6.5 / §12 / Appendix A.3 status sentences — verbatim from the original
draft; the obligation is the *original authoring's*, inherited by our versions).

For the five-regime topology figure specifically, the needed records are:
1. **Branch-continuation records** of the gated C3 core at Candidate A over τ: per-τ orbit
   amplitude / period / Floquet-multiplier / residual — lower-boundary large-cycle
   termination τ∈[5.574,5.576] (multiplier track 0.240@τ=4.0 → 0.964@τ=5.5815, residual
   ~10⁻¹²); small-branch fold ≈5.587 (multiplier 1.0514@5.584 → 0.99898@5.587; amplitude
   21.80, period 313.76 at 5.58667); upper boundary [148.125,148.438] (Hopf small branch
   amplitude 0.11–1.87 on [130,150.30]; interior large family 15.9–19.5 on [147.5,160];
   E≥E_max third family to ≈144.5); upper-window attractor at τ=131.8 (Poincaré spread
   <5×10⁻³, envelope constant to 0.005% over 2×10⁶ yr, period ≈135.6, Floquet dominant
   pair ≈0.81, RK45 method-of-steps reproduction); large cycle at τ=5.55 (E≤9.2, N≥68.7,
   period 324).
2. **Four-state C4 working-core continuation** (folds 5.63/64.4; periods ≈371→320 lower,
   ≈156→73 upper; ω_A* ≈ 0.001316).
3. **Family records** (M3-U 6.8814/132.3749; M3-B 3.67/150.36; M3-LC ψ-shift
   131.998/132.499 + first-hitting 158/430; M4-A turnover boundary; MPF η_crit≈2.337,
   intermittency CV 1.58, return-map r=−0.47).
4. **History/basin test records** ("basins restricted to the histories actually tested").
5. **Solver configuration and environment artifacts** (continuation step budgets,
   persistence-test durations, collocation orders, tolerances).

## 3. What already exists on the repo (checked against the tree API, 2026-09-02)

Present — the A025 fold machinery and the C4 orbit certificates:
- `research_program/validated_computations/a025_fold/` — `a025_fold_pipeline.py`,
  `a025_model.py`, `a025_branch_continuation.json` (+ `_m96` / `_m128`),
  `a025_moore_spence_fold.npz` (+ `_m96` / `_m128`), `a025_interval_hopf.py/.json`,
  `fold_run.log`. These are the m=64/96/128 nominal Moore–Spence solves of the small-branch
  fold τ_f = 5.587236198690 (|M|≈2×10⁻¹²), the exact rebuild P4 Appendix A.3 references
  ("a nominal fold rebuild at three collocation resolutions (m=64/96/128)… places all three
  resolutions inside the interval for which the certificate was never obtained"). Krawczyk
  stage unimplemented, as declared.
- `research_program/validated_computations/a021_c4/` — `c4_monodromy.py`,
  `c4_monodromy_dt0p25/dt0p1` artifacts + enclosure JSONs, `c4_orbit_krawczyk_certificate.json`,
  piecewise-Chebyshev stage artifacts (C4 orbit/Floquet certificates).
- `reaudit/postv10_rerun/` — independent rerun copies of the fold_m64 and dt0p1 artifacts.

Absent — the A018 §6 records (items 1, 3, 4, and the C4-core folds of item 2): no branch
track over τ, no 5.574–5.576 basin-collapse evidence, no 148.125–148.438 records, no family
logs, no history-test records anywhere in the tree or in git history. These are precisely
the declared-open "publication-artifact archives" of the A018 authoring.

Consequence for the figure: the ≈5.587 small-branch fold could be drawn from committed
artifacts alone, but the five-regime topology (all five windows over τ) still requires
either the A018 authoring's records (retrievable from the "ecol" chat / Z.ai Code sessions)
or the pre-registered recomputation campaign already recorded in the registry.

## 4. Which original repo papers pertain

- **A018** — `uploads/manuscript.txt` (§6, rows CC-A018-014/-015; the direct source of the
  five-regime numbers) and `revised_articles/A018_capital_liquidation_corrected.tex`.
- **A025** — `uploads/paper_VIII_interval_folds.txt` and
  `revised_articles/A025_interval_folds_corrected.tex` (interval-folds paper; its committed
  pipeline artifacts cover the shared ≈5.587 fold; its 13 appendix rows sit in P4's
  Appendix A).
- **P4 itself** — `papers/paper4_delay_dynamics/manuscript.md` (+ `manuscript_v2.md`; the
  Task-52 draft) and the uploaded versions `uploads/paper4_final.md` (A017),
  `uploads/paper4_rev3.md` (A008), `uploads/paper4_perspective.txt` (A010); packet copies
  under `research_program/general_theory_math_closure_packet/sources/full/`.
- **Model registry** — `uploads/MODEL_REGISTRY.md` (Candidate A/B parameter vectors,
  required input to any recomputation).

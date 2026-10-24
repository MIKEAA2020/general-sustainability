# general-sustainability — where the new editions are (pushed 2026-10-15)

| Paper | New edition | Built from | Repository folder (identical on both branches listed) | Commit |
|---|---|---|---|---|
| ECOMOD (productivity illusion) | **v42** main 33 pp + SI 17 pp | v41 (`main`) | `agent 2 productivity illusion/manuscript_ECOMOD_v42.*`, `manuscript_ECOMOD_v42_supplementary.*`, `manuscript_ECOMOD_v42_{README,CHANGELOG_v41_to_v42,HIGHLIGHTS}.md`, sources `manuscript_ECOMOD_v42_src/` | `main` f144fac |
| Paper 1 (assessment separation) | **v64** main 40 pp + SI 30 pp | v62 (`main`) / v63 (`e2-v3-source-year`, `lean-audit-v4`) | `arena agent 1/paper rewrites/latex/paper1_assessment_separation_v64.*`, `..._v64_supplementary.*`, `..._v64_{README,CHANGELOG_v62_to_v64,highlights}.md`, `COVER_LETTER_paper1_assessment_separation_JMCDA_v64.md`, sources `paper1_assessment_separation_v64_src/` | `main` f144fac, `e2-v3-source-year` a2725e2 |
| Paper E1 (cod forecast ladder) | **v69** main 33 pp + SI 19 pp, verifier 87/87 | v59 (`main`) / v60 (`e2-v3-source-year`, `lean-audit-v4`) | `arena agent 1/paper rewrites/latex/paperE1_cod_forecast_ladder_v69.*`, `..._v69_SI.*`, `..._v69_verification.py`, `..._v69_{README,CHANGELOG_v59_v60_to_v69,highlights}.md`, `COVER_LETTER_paperE1_cod_forecast_ladder_FR_v69.md`, sources `paperE1_cod_forecast_ladder_v69_src/` | `main` f144fac, `e2-v3-source-year` a2725e2 |
| Paper 01 (obstruction calculus) | **v73** main 28 pp + SI 23 pp, verifier 30/30 | v72 (`e2-v3-source-year`) | `arena agent 1/agent workspace/paper 2 family/01_obstruction/paper01_obstruction_calculus_v73.*`, `..._v73_supplementary.*`, `paper01_v73_verification.py`, `..._v73_{README,CHANGELOG_v72_to_v73,HIGHLIGHTS}.md`, `COVER_LETTER_paper01_obstruction_calculus_SVVA_v73.md`, sources `paper01_obstruction_calculus_v73_src/` | `main` f144fac, `e2-v3-source-year` a2725e2 |

Both commits only add files (201 on `main`, 169 on `e2-v3-source-year`); nothing existing was modified or deleted. Every `.tex` compiles unchanged inside its repository folder (checked with tectonic in a mirror of the layout; PDFs pushed are those builds).

## Version numbers across ALL branches (checked 2026-10-15; the rule is never to reuse a number)

| family | main | e2-v3-source-year | lean-audit-v4 | edwards-framework-e1 | edwards-framework-e1-audit-implementation |
|---|---|---|---|---|---|
| paper1_assessment_separation | v62 → **v64 added** | v63 → **v64 added** | v63 | v42 | v42 |
| paperE1_cod_forecast_ladder | v59 → **v69 added** | v60 → **v69 added** | v60 | v49 | `e1/` v49…**v68** (parallel line, different manuscript: "Does Structural Elaboration Improve Biomass Forecasts? …", 17–22 Sep 2026, with E1_SUPPLEMENTARY_V2–V8 and submission builds) |
| manuscript_ECOMOD | v41 → **v42 added** | v37 | v37 | v35 | v35 |
| paper01_obstruction_calculus | — → **v73 added** | v72 → **v73 added** | — | — | — |
| paper2_obstruction_calculus | v49 addendum (v56 tex on branch) | v56 | — | v20 | v20 |

Other branches: `archive/paper3-v48-workspace` (none of these families).

## Local workspace after cleanup (12 MB, ~200 files)
`ecomod_v42/`, `paper1_v64/`, `e1_v69/` (renumbered from the local working label v61), `p01_v73/` — the same content as pushed (flat local names for Paper 1: `manuscript_paper1_v64*`). Removed as re-clonable/re-derivable: `gs/` (broken 55 MB clone), `push_stage/`, `e2branch/`, `repo_branch/`, `review_pages/`, `p01_v73/src/` (v72 inputs), QA page renders under `*/work/`, `e1_v61/` (superseded by `e1_v69/`).
Re-create a minimal clone with `repo_clone_min.sh` (see header).

## Update (2026-10-15, later): renamed-lineage correction, part 1 — paper06 v71
* Discovery: the Paper 1 and E1 lineages had been renamed/continued in `arena agent 1/agent workspace/papers/` on `e2-v3-source-year` (paper06_assessment_separation v64–v70; paper11_forecasting_baselines v61–v66). The 2026-10-15 rewrites `paper1_assessment_separation_v64*` and `paperE1_cod_forecast_ladder_v69*` were built on stale bases (v63 / v60).
* **paper06 v71 pushed** (research-article edition rebuilt on v70; main 47 pp. + SI 39 pp.):
  * `e2-v3-source-year` a2725e2 → **14cee87**: `arena agent 1/agent workspace/papers/paper06_assessment_separation_v71{.tex,.pdf,_supplementary.tex,_supplementary.pdf,_README.md,_CHANGELOG_v70_to_v71.md,_highlights.md}`, `COVER_LETTER_paper06_assessment_separation_JMCDA_v71.md`, `paper06_assessment_separation_v71_src/{parts,figs,work}`; the stale-based `paper rewrites/latex/paper1_assessment_separation_v64*` + its JMCDA cover letter moved (renamed only) to `paper rewrites/latex/superseded/` with a README.
  * `main` f144fac → **3bb6d1c**: same v71 files placed in `arena agent 1/paper rewrites/latex/` (main has no `agent workspace/papers/` folder), same superseded move.
* Local: `/home/user/p06_v71/` (parts, figs, work, push plans, companion md files). Push tool: `/home/user/tools/gitpush_index.py` (index-only commits on the blob:none clone; refuses unexpected deletions).
* Still to do: paper11 v66 → v67 (then move `paperE1_cod_forecast_ladder_v69*` to `superseded/`), paper03 v22 → v23.

## Update (2026-10-15, later): renamed-lineage correction, part 2 — paper11 v67
* **paper11 v67 pushed** (one research article on both systems — Northern cod ladder + Edwards J-17 ladder — rebuilt on `paper11_forecasting_baselines_v66` with the cod half carrying every paperE1 v69 improvement; main 49 pp., 10 tables, 8 figures, Props 1–2; SI S1–S24, 35 pp.; verifier 139/139):
  * `main` 3bb6d1c → **1644411**: `arena agent 1/paper rewrites/latex/paper11_forecasting_baselines_v67{.tex,.pdf,_supplementary.tex,_supplementary.pdf,_verification.py,_verification_output.txt,_README.md,_CHANGELOG_v66_to_v67.md,_highlights.md}`, `COVER_LETTER_paper11_forecasting_baselines_EMS_v67.md`, `paper11_forecasting_baselines_v67_src/{parts,si_parts(+gen),figs,work/{edw/results,edw/data/annual_panel.csv,cod}}`; `paperE1_cod_forecast_ladder_v69*` + `COVER_LETTER_paperE1_cod_forecast_ladder_FR_v69.md` moved (renamed only, 92 files) to `paper rewrites/latex/superseded/`, README appended.
  * `e2-v3-source-year` 14cee87 → **3f48897**: same v67 files in `arena agent 1/agent workspace/papers/`; same superseded move.
  * Content: v66's cross-system claim ("weakly autocorrelated surplus production") withdrawn — AC1 of cod apparent net production is 0.71–0.91; replaced by Proposition 2 (increment decomposition: misspecification term vs persisted-driver term σ²(1−2ρ)−μ²) and Remark 2 (climatology overtakes persistence when ρ_h < ½; J-17 crossover at h=2, cod never). No archived score changed; new computations = SI S23 + Fig. 8.
* Local: `/home/user/p11_v67/` (parts, si_parts, figs, work, push plans, companion md). `/home/user/e1_v69/` is now fully on the repo (superseded/) and re-clonable.
* Still to do: paper03 computational certification v22 → v23.

## Update (2026-10-15, later): paper03 v23 — computational certification
* **paper03 v23 pushed** (research-article edition rebuilt on `paper03_computational_certification_v22`, the newest edition on any branch; main 26 pp. — Sections 1–10 + Appendices A–B, 4 figures, 2 tables, 30 cited references; SI 10 pp. S1–S8; exact verifier **63/63**; figure script recompute-then-assert; inherited scripts re-run 9/9, 51/51, viacert 12/12):
  * `e2-v3-source-year` 3f48897 → **eca5d37**: `arena agent 1/agent workspace/papers/paper03_computational_certification_v23{.tex,.pdf,_supplementary.tex,_supplementary.pdf,_verification.py,_verification_output.txt,_README.md,_CHANGELOG_v22_to_v23.md,_highlights.md}`, `COVER_LETTER_paper03_computational_certification_SICON_v23.md`, and `paper03_computational_certification_v23_src/{parts,si_parts,figs,work}` (work: `p03_core.py`, `make_figs.py`, `observer_sweep.tsv`, `repo_scripts/`, `viacert/`).
  * `main` 1644411 → **3decd70**: the same files in `arena agent 1/paper rewrites/latex/`.
  * Additions only (58 files per branch); no renames, no deletions.
  * New content vs v22: mesh law on arbitrary aligned meshes (Prop 5.3, Table 2), support-vs-rank corollary, shared-authority ladder with Γ_B = peak − 2 identity, exact erosion table (Prop 6.3), observer-installation bracket [3/25, (6−√29)/5] with explicit schedule and LP sweep (Prop 6.4, Fig. 4), dilation counterexample (SM S6); corrections: {2,3} pair policy description, 12193/6250 typo, n₂·n₃ = −7/25, sandwich bound with h_t = h/2.
* Local: `/home/user/p03_v23/` (parts, si_parts, figs, work, push plans, companion md). `gs2` re-cloned minimal after the push (the push temporarily inflated it to 318 MB).
* Lineage table now: paper01 v73, paper03 **v23**, paper06 v71, paper11 v67, ECOMOD v42 current. Next candidates (newest on e2 `agent workspace/papers/`): paper02 v15, paper04 v19, paper05 v19, paper07 v52, paper08 v48, paper09 v43, paper10 v53.

## Update (2026-10-15, later): paper02 v16 — probabilistic sufficiency
* **paper02 v16 pushed** (research-article edition rebuilt on `paper02_probabilistic_sufficiency_v15`, the newest edition on any branch — main `paper2_probabilistic_sufficiency_v*` stops at v14; title now *Probabilistic sufficiency under partial observation: belief-state safety values, survivable-set antichains, and the exact price of late information*; main 23 pp. — Sections 1–11, 4 figures, 37 cited references; SI 8 pp. S1–S8 with script-generated tables; exact verifier **62/62** incl. five text-binding checks; new exact module `p02_core.py` with a generic α-vector backup):
  * `main` 3decd70 → **7fd760c**: `arena agent 1/paper rewrites/latex/paper02_probabilistic_sufficiency_v16{.tex,.pdf,_supplementary.tex,_supplementary.pdf,_verification.py,_verification_output.txt,_README.md,_CHANGELOG_v15_to_v16.md,_highlights.md}`, `COVER_LETTER_paper02_probabilistic_sufficiency_MOR_v16.md`, `paper02_probabilistic_sufficiency_v16_src/{parts,si_parts,figs,work}` (work: `p02_core.py`, `make_figs.py`, `make_si_tables.py`, `assemble.py`, `repo_scripts/` = the four inherited v15 scripts).
  * `e2-v3-source-year` eca5d37 → **fc16cb8**: the same files in `arena agent 1/agent workspace/papers/`.
  * Additions only (53 files per branch); no renames, no deletions.
  * New content vs v15: value-of-observation bound with attaining family F_n (Prop 3.2), Sperner bound attained (Thm 3.3), exact threshold theorem for hold–probe–learn schedules with misaligned counterexample 1+max(T,1) vs 2+T (Thm 6.2, Ex 6.3), class-scoped timing obstruction as a corollary (Cor 5.3), deficit profile (Cor 5.5), two-stage contamination counterexample 1/16 vs 1/8 + convexity (Prop 8.1), prior contamination closed form (Prop 8.2); removed: minimax reciprocal cross-check paragraph, unrelated Zenodo self-citation; references 14 uncited → 37 cited.
* Local: `/home/user/p02_v16/` (parts, si_parts, figs, work, push_src, push plans, companion md). `gs2` re-cloned minimal after the push (the push inflated it to 324 MB — always re-clone after pushing).
* Lineage table now: paper01 v73, paper02 **v16**, paper03 v23, paper06 v71, paper11 v67, ECOMOD v42 current. Next candidates (newest on e2 `agent workspace/papers/`): paper04 v19 → v20, paper05 v19 → v20, paper11c v4 → v5, paper09 v43 → v44, paper10 v53 → v54, paper08 v48 → v49 + paper07 v52 → v53.

## paper04 v20 pushed (2026-10-15, later)
* `main` → **59b5b22**, `e2-v3-source-year` → **1d61630** (58 files each: `paper04_minimax_dual_certificates_v20.{tex,pdf}`, `_supplementary.{tex,pdf}`, `_verification.py` + `_output.txt` (66/66), `_README.md`, `_CHANGELOG_v19_to_v20.md`, `_highlights.md`, `COVER_LETTER_paper04_minimax_dual_certificates_JOTA_v20.md`, `paper04_minimax_dual_certificates_v20_src/{parts,si_parts,figs,work(+repo_scripts),Minimax_Dual.lean}`), main in `arena agent 1/paper rewrites/latex/`, e2 in `arena agent 1/agent workspace/papers/`.
* Base: paper04 v19 (e2 `agent workspace/papers/`). Main 19 pp (Sections 1–8, 4 figs, 30 refs all cited), SI 13 pp (S1–S8, all tables generated). Local edition folder: `/home/user/p04_v20/`.
* Lineage table now: paper01 v73, paper02 v16, paper03 v23, **paper04 v20**, paper06 v71, paper11 v67, ECOMOD v42 current. Next candidates: paper05 v19 → v20, paper11c v4 → v5, paper09 v43 → v44, paper10 v53 → v54, paper08 v48 → v49, paper07 v52 → v53.

## paper05 v20 pushed (2026-10-15, later)
* `main` → **eeea0fc**, `e2-v3-source-year` → **a47bd6b** (107 files each: `paper05_exact_belief_computation_v20.{tex,pdf}`, `_supplementary.{tex,pdf}`, `_verification.py` + `_output.txt` (53/53 full run, 354 s), `_README.md`, `_CHANGELOG_v19_to_v20.md`, `_highlights.md`, `COVER_LETTER_paper05_exact_belief_computation_MOR_v20.md`, `paper05_exact_belief_computation_v20_src/{parts,si_parts,figs,work(+repo_scripts, results.json, stage outputs, census_m4/5.npz),lean(8 modules + ebc_verification_report.md),paper05_reviewers.txt}`), main in `arena agent 1/paper rewrites/latex/`, e2 in `arena agent 1/agent workspace/papers/`.
* Base: paper05 v19 (e2 `agent workspace/papers/`). Main 20 pp (Sections 1–10, 3 figs, 6 tables, 29 refs all cited), SI 15 pp (S1–S9, all tables generated). Local edition folder: `/home/user/p05_v20/`.
* Lineage table now: paper01 v73, paper02 v16, paper03 v23, paper04 v20, **paper05 v20**, paper06 v71, paper11 v67, ECOMOD v42 current. Next candidates: paper11c v4 → v5, paper09 v43 → v44, paper10 v53 → v54, paper08 v48 → v49, paper07 v52 → v53.

## paper11c v5 pushed (2026-10-15, later)
* Base: `paper11c_worked_systems_audit_v4.tex` (e2 `agent workspace/papers/` + `paper 2 family/11c_worked_systems/`; lineage `paper2_worked_systems_v17` on main `paper rewrites/latex/`). New edition **v5**: main 22 pp. (6 thm, 10 prop, 3 cor, 2 lem, 8 def; 5 figs, 2 tables; 31 refs all cited) + SI 13 pp. (S1–S11, 16 tables) + verifier 64/64 (full 71 s; `--quick` 2 s) + exact core `ws_core.py`/`run_all.py`/`results.json` + table/figure generators + Lean modules copied (not rebuilt).
* Commits: `main` → **217d110** (11 plan entries, 74 files); `e2-v3-source-year` → **e920243** (19 plan entries, 82 files: `agent workspace/papers/` full set + `_src/`, and `paper 2 family/11c_worked_systems/` tex/pdf/SI/verifier/output/README/CHANGELOG). Remote confirmed by `git ls-remote`.
* Local edition folder: `/home/user/p11c_v5/` (parts, si_parts, work, figs, push_src, push plans).
* Lineage table at that point: paper01 v73, paper02 v16, paper03 v23, paper04 v20, paper05 v20, paper06 v71, paper11 v67, **paper11c v5**, ECOMOD v42 current. Next candidates then: paper09 v43 → v44, paper10 v53 → v54, paper08 v48 → v49, paper07 v52 → v53 (also paper09b v5, paper10b v2, paper11b v3 lineages).

## paper09 v44 pushed (2026-10-15, later) — cod/Edwards viability certification
* **Base/version check:** refreshed all remote branch refs and searched branch trees; no paper09 v44 existed on any branch. Latest cod–Edwards article in `e2-v3-source-year` was `arena agent 1/agent workspace/papers/paper09_cod_certification_v43.tex`; v44 continues that lineage in the same directory.
* **Pushed:** `e2-v3-source-year` e920243 → **fe1eabd**; 151 additions, no deletions or overwrites. Main + SI (25 pp. + 18 pp.), 77/77 full verifier checks, 74/74 quick checks; final abstract edit included in the builds. A separate sibling-layout run and a fresh source-only rebuild/verification both passed 77/77.
* Repository files in `arena agent 1/agent workspace/papers/`: `paper09_cod_certification_v44.{tex,pdf}`, `_SI.{tex,pdf}`, `_verification.py`, `_verification_output.txt`, `_README.md`, `_CHANGELOG_v43_to_v44.md`, `_highlights.md`, `COVER_LETTER_paper09_cod_certification_v44.md`, and complete `paper09_cod_certification_v44_src/` (141 source files, 3.1 MB); 151 files total including top-level deliverables. Main and SI compile without unresolved references; SI has no overfull boxes. Full verifier record is 77/77; quick mode leaves it unchanged.
* Content clarifies finite- versus infinite-horizon kernel classification and distinguishes exact-kernel horizons from the Lipschitz certificate, including the 660-ft T=2 certificate failure and zero-pumping OOS horizon. Generated tables/figures and exact re-derivation core are in the source bundle.
* Local edition: `/home/user/p09_v44/`; source `push_src/paper09_cod_certification_v44_src/`; `push_plan_e2.json`. Remote was confirmed by a post-push budget-safe minimal clone (`fe1eabd`).
* Updated lineage table: paper01 v73, paper02 v16, paper03 v23, paper04 v20, paper05 v20, paper06 v71, **paper09 v44**, paper11 v67, paper11c v5, ECOMOD v42. Remaining e2 candidates: paper07 v52 → v53, paper08 v48 → v49, paper10 v53 → v54; separate lines paper09b v5, paper10b v2, paper11b v3.

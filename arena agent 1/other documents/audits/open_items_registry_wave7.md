# Open-items registry, wave 7 — all remaining audit/joint-assessment points across the eight papers

**How to read this file.** Every item below was either (i) implemented earlier and verified, (ii) executed in wave 7 (this turn), (iii) judged feasible-next with an execution recipe, or (iv) classified to a non-computational pass (venue, new mathematics, external data, or code that is not in this workspace). Nothing is dropped silently; each row carries the reason. Classes: EXECUTED-W7 · FEASIBLE-NEXT · VENUE-PASS · NEW-MATH · NEEDS-DATA · CODE-ABSENT · DISPOSED · STALE.

---

## 1. The user's two questions, answered directly

**Q1 — remaining points worth implementing?** Yes, exactly these were worth executing, and they are now executed: the P5 operator-comparison package (the complete crossing record, the protective-controller run, and the model-level comparator management-strategy evaluation — all registered as unexecuted in P5 v3 and flagged by its audit), P4's two skipped optional micros (the ordering-similarity clause, the C₁ anchor), and — in the wave-7 extension of turn 44 — all five FEASIBLE-NEXT recipes that Section 3 had queued: the E2 Fox form and xteNCAM row, the E4 finite-duration floors and floor-class supply, and the E3 pumpage counterfactuals (new versions E2 v7, E4 v6, E3 v5). Everything else remaining in the assessments is either (a) venue-pass framing/taste items with no correctness content, (b) new mathematics, (c) real-world preregistration designs that require institutions and data rather than computation, or (d) computations whose code is not in this workspace — all classified below with reasons.

**Q2 — unexecuted work worth executing?** The P5 items named in the question (the declared-but-unrun protective/fixed-plan comparators and the registered multiplier scan) are moderately feasible and are now executed at model level. The **five prospective designs of P5 §4.5 are NOT executable in silico**: they are preregistration targets for real systems — each needs dated observation releases/assessment products/command records (Design 1), or candidate systems with archived management records (Designs 2–5) — and the paper correctly labels them as preregistration targets without protocol IDs; executing them would require fabricated empirical records, which the no-fabrication rule forbids. The stage-structured map's multiplier scan is **code-absent**: the turn-44 sweep confirmed it exists nowhere on the repository (local or GitHub — full tree, 2,935 entries), and the deleted `research_program/file_archive/` held 1,318 documents and zero code files, so no code was lost in the turn-42 budget cleanup; the paper's "exploratory status" sentence stands (and is now explicitly scoped in P5 v4).

---

## 2. Executed in wave 7 (this turn)

| Paper | Item (origin) | Execution | Artifact |
|---|---|---|---|
| P5 | Complete crossing record + stable intervals, Euler and exact updates, both channels, T_r ∈ [0.2, 200] yr (paper's own §2.2/§3.4 registration; audit U1(i) completion) | 200,001-point scan + bisection; committed numbers reproduced first (0.9838, 2.306, 1.00055, 47.536, 79.143, 1.00035, 0.9967) | `rerun_campaigns/campaign_p5_crossing_scan.py`, `results/p5_crossing_record.csv`, `results/p5_linear_trajectory_mse.csv`; text in `paper5_sampled_governance_v4.md` §3.4 |
| P5 | Protective controller on the same maps (audit U3) | exact protective stable on [0.2, 200] (max ρ = 0.9967); Euler protective artefact band quantified | same script; §3.4 |
| P5 | Comparator management-strategy evaluation, protective + fixed-plan (audit line 133: "declared for MSE, not run") | nonlinear closed loop on the logistic hold-map core, N0 = 0.95 N*, 800 reviews, assessment error {0, 0.3}, 10 seeds per noisy cell, seed-fixed | `rerun_campaigns/campaign_p5_comparator_mse.py`, `results/p5_comparator_mse.csv`, `results/p5_comparator_mse_mc.csv`; §3.4 |
| P5 | Linear trajectory MSE Euler-vs-exact (command-step distortion) | scaled-norm RMSD table over T_r grid | same script; §3.4 |
| P4 | Wave-5 item 9 (optional micro): flow-then-update vs update-then-flow similarity | clause added: similar monodromies, identical spectra, linear classification transfers | `paper4_delay_dynamics_v5.md` §7 |
| P4 | Wave-5 item 10 (optional micro): C₁ unexpanded | C₁ anchored: the scaled-norm Lipschitz constant of the difference vector field, finite by the statement's Lipschitz hypothesis | `paper4_delay_dynamics_v5.md` §2.4 |
| E2 | Fox/Pella–Tomlinson third surplus form (wave-6 #22) | Refit in the committed fit_params convention on 1983–2007, frozen floor classes, forward-mask kernels incl. S1: r = 0.1044, K = 5000 pinned, MSE 13,873.1 kt² (Schaefer 12,772.2; Allee 7,690.1 — Fox worst-fitting); F′(K*) = 1.0764 > 1; constructive q10 = 45.08 kt; BAU/zero-catch q10 certificates exactly unchanged (884.6 kt at every horizon); 60-kt rule T∞ = 1119.0 (S1 shares it), 120-kt rule empty; harsh classes keep empty T∞ kernels | `rerun_campaigns/campaign_e2_fox_form.py`, `results/e2_fox_form.csv`, `results/e2_fox_kernels.csv`; text in `paperE2_cod_intervention_v6.md` → **v7** §3.6 |
| E2 | xteNCAM labelled sensitivity row (wave-6 #23) | No pooling; own classes from own training residuals (e_min −470.8, e_q05 −269.5, e_q10 −178.7, not vacuous); r = 0.5023, K = 4812.9, MSE 18,028.3, F′(276) = 1.4447; own-q10 constructive bound **negative** (−48.03 kt); zero-catch T1 = 309.4 kt > LRP 276; 2024 stock (342 kt) between T1 (309.4) and T5 (368.1) boundaries | `rerun_campaigns/campaign_e2_xteNCAM_row.py`, `results/e2_xteNCAM_row.csv`, `results/e2_xteNCAM_summary.csv`; `paperE2_cod_intervention_v7.md` §3.11 |
| E4 | Sequence disturbances (wave-5 #13 part) — finite-duration floors | n years at the class floor then training-mean recharge, exact backward recursion: BAU n=5/10 reproduce the committed T=5/T=10 boundaries (625.6/658.4 ft); n=15 empty (committed 13-year bound); every cut policy and every q05/q10 BAU row holds 618 ft at all n ∈ {5, 10, 15} — duration differentiates BAU alone | `rerun_campaigns/campaign_e4_elevation.py`, `results/e4_finite_floors.csv`; `paperE4_edwards_intervention_v6.md` §3.6, Table 4 |
| E4 | Closed-loop supply (wave-5 #13 part) — floor-class supply | Closed loop from the observed 1934 head at each class floor: reactive rules converge to their matched flat-cap attractors (S1 → flat-80's 622.04 ft, CPM → flat-60's 628.36 ft); span-mean supply exceeds the matched caps only by the trigger-lag margin (S1 +0.4%, CPM +3.1%); BAU end head 615.72 = committed worst-case attractor; no domain exits | `rerun_campaigns/campaign_e4_elevation.py`, `results/e4_floor_supply.csv`; `paperE4_edwards_intervention_v6.md` §3.6, Table 5 |
| E3 | Pumpage scenarios (wave-5 deferred list) | Four counterfactual pumpage paths through the fitted pre-permit map (actual recharge, 1991–2023): actual 382.1 (RMSE 8.56 ft, closest); frozen-at-1990 489.4 (14.22); pre-permit mean 469.8 (13.02); 20% cut 305.7 (7.19, end head +5.1 ft). Policy spread at 2023 spans 630.9–646.8 ft — same order as the map's own RMSE: pumpage is a secondary, level-side lever; the ladder's primary failure is recharge timing (§5.3) | `rerun_campaigns/campaign_e3_pumpage_scenarios.py`, `results/e3_pumpage_scenarios.csv`; `paperE3_edwards_forecast_ladder_v5.md` §5.6, Table 7 |

Key executed numbers (P5 v4 §3.4): Euler mobilising crossings {47.536 complex, 79.143 real −1}, stable band [47.54, 79.14]; exact mobilising single crossing 6.501, stable [6.50, 200+]; Euler protective crossing 2.306 (real −1), stable [0.2, 2.31]; exact protective none, stable [0.2, 200], max ρ = 0.9967. Comparator MSE (30% assessment error, 10 seeds): extractive-Euler crashes in 10/10 seeds at T_r = 8/12/20; extractive-exact never crashes (depletion 0.07 → 0.001); protective-exact holds (depletion 0, min 0.89 N*); protective-Euler crashes 10/10 at T_r = 20; fixed plan = exact rest point.

---

## 3. Feasible-next (with recipes — the remaining moderately feasible executions)

| Paper | Item (origin) | Recipe | Effort |
|---|---|---|---|
| E2 | Fox/Pella–Tomlinson third surplus form (wave-6 #22) | **EXECUTED (wave 7)** — see Section 2 | — |
| E2 | xteNCAM labelled sensitivity row (wave-6 #23) | **EXECUTED (wave 7)** — see Section 2 | — |
| E4 | Sequence disturbances (wave-5 #13 part) | **EXECUTED (wave 7)** as the finite-duration floors layer — see Section 2 | — |
| E4 | Closed-loop supply (wave-5 #13 part) | **EXECUTED (wave 7)** as the floor-class supply layer — see Section 2 | — |
| E3 | Pumpage scenario (wave-5 deferred list) | **EXECUTED (wave 7)** — see Section 2 | — |

All five recipes were executed in the wave-7 extension (turn 44); none remains in this class.

## 4. Not executable / not computational (classified)

| Paper | Item (origin) | Class | Reason |
|---|---|---|---|
| P5 | Five prospective designs (§4.5) | NEEDS-DATA | Real-system preregistration targets: dated observation/assessment/command records, candidate institutions, protocol IDs. Executing them in silico would fabricate empirical records. |
| P5 | Stage-structured map multiplier scan (paper registration; audit U1(ii) second half) | CODE-ABSENT | Definitively: the turn-44 sweep (local find/grep + full GitHub tree, 2,935 entries) found no stage/recruit-map computation anywhere; the deleted `file_archive/` held 1,318 documents and 0 code files. The paper's exploratory-status sentence is explicitly scoped to the stage map only (P5 v4). |
| P5 | U1(ii) continuous-delay analogue of the delayed-recruitment plant | NEW-MATH | The continuous-delay equation of the stage-structured plant is not a declared object in any paper; it would be a new model. |
| E2 | DFO-grounded policy rows (wave-6 #19) | NEEDS-DATA | Requires DFO-document sourcing of the historical inshore TAC path before it can be scored. |
| E2 | DP/viability-kernel regret (wave-6 #20) | NEW-MATH (heavy) | Existential kernels over controls on this map: a new computation class, registered as the next methods extension. |
| E2 | Co-viability second constraint (wave-6 #21) | NEW-MATH (heavy) | New constraint object; design choice needed. |
| E4 | Certified-layer redesign; springs in K*/drain; one-pool control volume (wave-5 #13) | NEW-MATH | Model-structure changes, not computations on the declared object. |
| E4 | "Viability kernel" vocabulary (wave-5 #12) | VENUE-PASS | Wording alongside the existing disclosure; no content change. |
| E3 | One-pool blackboard rebuild; wet-season information set; M4-as-physics; companion-cod syntax pruning; sign-hit strike line (wave-5 deferred) | VENUE-PASS / NEW-MATH | Text-polish items go to the venue pass; the blackboard rebuild is a new model. |
| P2 | EViab belief-space kernel characterisation (wave-5 U4) | NEW-MATH | Theorem-level extension; the coupling caveat implemented earlier stands. |
| P1 | BLEND_δ mixed action; x-in-aggregate variant; two-stage erasure witness; predecessor bridge; Farkas duals; information-refinement/authority monotonicity theorems (wave-2 deferred) | NEW-MATH | Open extensions recorded for the venue pass. |
| P3 | I1 types-as-types page; I2 phosphate as Thm-15 instance (wave-4) | VENUE-PASS | Framing items. |
| P1 | P1.6 minimax/game framing; P1.16 information-asymmetry gloss (wave-3) | VENUE-PASS | Accessibility upgrades, one optional sentence each. |
| E1 | E1.10 h=5 persistence demographic point; E1.15 martingale gloss (wave-3) | VENUE-PASS | Interpretive. |
| E3 | E3.10 persistence-win dynamic-equilibrium gloss (wave-3) | VENUE-PASS | Interpretive. |
| E4 | E4.9 transmissivity contrast in conclusions (wave-3) | VENUE-PASS | Optional mechanism sentence. |
| P5 | U1(ii) sample-and-hold vs continuous delay on the logistic plant — continuous half | DONE (imported) | The continuous-delay Hopf pair on the same plant is P4's certified τ− = 3.666 / τ+ = 150.358 yr; the sampled half is the exact-hold 6.501 yr crossing now complete. P5 v4 §3.4 states the one-plant contrast: continuous-delay windows {3.67, 150.36} yr versus sampled single crossing 6.50 yr. |

**REBUILD-SPEC — what a non-fabricated stage-map multiplier scan requires.** The stage map's equations and parameter sets appear nowhere in the committed record (checked: every P5 version, the supplementary, P2, P4 — only the stock-class names and the exploratory windows are on record). A legitimate rebuild therefore needs, in order of bindingness: (1) **the plant** — the delayed-recruitment stage-structured map's defining equations and the four stock-class parameter sets (anchovy, sprat, cod, slow-stock); without this any implementation invents the object, which is fabrication; (2) **the loop instantiation** — what effort acts on in the stage plant (recruitment suppression, harvest, both), the controller linearisation, equilibrium, and parameter vector; (3) **the computation spec** — the paper's own registration list: exact flow/update ordering and information pattern, all observation and deployment lags, the derivative construction for the review-map Jacobian $M = D\mathcal P_{T_r}(X^*)$, multiplier trajectories and crossing directions, nonlinear trajectories on both sides, numerical refinement, solver configuration and initial histories; (4) **the validation gates** — the legacy exploratory bands against which any new record must be checked: anchovy-class 3–4 yr (weak response at 2 yr), sprat-class 6–12 yr, cod-class convergence over the 1–20 yr grid, slow-stock transitions ≈30–50 yr for $r \in (0.01, 0.05)$ yr⁻¹, robustness to 30% multiplicative assessment error, the diagnostic peaks (≈4 yr biomass / 12 yr effort; ≈8 yr / 60 yr), and the amplitude signatures (80–240% effort vs 1–2% biomass excursions); (5) **an ownership decision** — either the original author supplies the record/specification (the scan then completes the registration), or the agent declares a NEW reconstructed map (equations and parameters chosen and labelled as a reconstruction) whose full multiplier record is computed and compared against the legacy bands — a legitimate new declared object, with the wave-7 comparator evaluation as precedent, but one that cannot silently claim to be the object that produced the legacy numbers.

## 5. Closed this wave (status changes in the assessments)

- `joint_assessment_wave5.md` P5 row 10 (U1(ii)/U3/MSE): DEFERRED → EXECUTED (wave 7), model-level.
- `joint_assessment_wave5.md` P4 rows 9–10 (optional micros): skipped → EXECUTED (wave 7).
- `joint_assessment_wave5.md` E4 #13 (sequence disturbances; closed-loop supply): DEFERRED → EXECUTED (wave 7) as the finite-duration floors and floor-class supply layers (E4 v6 §3.6, Tables 4–5).
- `joint_assessment_wave5.md` E3 deferred list (pumpage scenario): DEFERRED → EXECUTED (wave 7) as the §5.6 counterfactual layer (E3 v5, Table 7).
- `joint_assessment_wave6_e2.md` rows 22 (Fox form) and 23 (xteNCAM row): DEFERRED → EXECUTED (wave 7) (E2 v7 §3.6, §3.11).
- Turn 45 version-restoration scan (`audits/version_restoration_scan.md`; working files in `audits/_scan_work/`): all 9 latest versions diffed at sentence level against all 21 earlier agent-version pairs — **zero restoration candidates**; every changed unit survives (identical/reworded/expanded), was audit-corrected with the correction in place, or was superseded by executed work; the numbered-result structure lost nothing anywhere. One coherence repair surfaced: E2 v7 §2.1 "no row is produced on the second assessment specification" now conflicts with the turn-44 §3.11 xteNCAM row — fixed in **E2 v8** by scoping the §2.1 sentence to the frozen protocol (older versions untouched).
- P5 v4: §2.2 comparators declaration, §3.4 executed record, limitations (ii) rescoped, abstract and §4.1 clauses.
- P4 v5: §7 similarity clause, §2.4 C₁ anchor.

**Bottom line.** After the wave-7 extension (turn 44), the FEASIBLE-NEXT class is empty: every remaining open item is venue-pass wording, new mathematics, external data, or code-absent, and no moderately feasible in-silico execution remains unrun.

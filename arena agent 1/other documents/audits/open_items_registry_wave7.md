# Open-items registry, wave 7 — all remaining audit/joint-assessment points across the eight papers

**How to read this file.** Every item below was either (i) implemented earlier and verified, (ii) executed in wave 7 (this turn), (iii) judged feasible-next with an execution recipe, or (iv) classified to a non-computational pass (venue, new mathematics, external data, or code that is not in this workspace). Nothing is dropped silently; each row carries the reason. Classes: EXECUTED-W7 · FEASIBLE-NEXT · VENUE-PASS · NEW-MATH · NEEDS-DATA · CODE-ABSENT · DISPOSED · STALE.

---

## 1. The user's two questions, answered directly

**Q1 — remaining points worth implementing?** Yes, exactly these were worth executing now, and they are now executed: the P5 operator-comparison package (the complete crossing record, the protective-controller run, and the model-level comparator management-strategy evaluation — all registered as unexecuted in P5 v3 and flagged by its audit), and P4's two skipped optional micros (the ordering-similarity clause, the C₁ anchor). Everything else remaining in the assessments is either (a) venue-pass framing/taste items with no correctness content, (b) new mathematics, (c) real-world preregistration designs that require institutions and data rather than computation, or (d) computations whose code is not in this workspace — all classified below with reasons.

**Q2 — unexecuted work worth executing?** The P5 items named in the question (the declared-but-unrun protective/fixed-plan comparators and the registered multiplier scan) are moderately feasible and are now executed at model level. The **five prospective designs of P5 §4.5 are NOT executable in silico**: they are preregistration targets for real systems — each needs dated observation releases/assessment products/command records (Design 1), or candidate systems with archived management records (Designs 2–5) — and the paper correctly labels them as preregistration targets without protocol IDs; executing them would require fabricated empirical records, which the no-fabrication rule forbids. The stage-structured map's multiplier scan is **code-absent**: its computational record is not in this workspace, so the paper's "exploratory status" sentence stands (and is now explicitly scoped in P5 v4).

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

Key executed numbers (P5 v4 §3.4): Euler mobilising crossings {47.536 complex, 79.143 real −1}, stable band [47.54, 79.14]; exact mobilising single crossing 6.501, stable [6.50, 200+]; Euler protective crossing 2.306 (real −1), stable [0.2, 2.31]; exact protective none, stable [0.2, 200], max ρ = 0.9967. Comparator MSE (30% assessment error, 10 seeds): extractive-Euler crashes in 10/10 seeds at T_r = 8/12/20; extractive-exact never crashes (depletion 0.07 → 0.001); protective-exact holds (depletion 0, min 0.89 N*); protective-Euler crashes 10/10 at T_r = 20; fixed plan = exact rest point.

---

## 3. Feasible-next (with recipes — the remaining moderately feasible executions)

| Paper | Item (origin) | Recipe | Effort |
|---|---|---|---|
| E2 | Fox/Pella–Tomlinson third surplus form (wave-6 #22) | Refit g(S) = r·S·ln(K/S) by one-step LS on 1983–2007 with the frozen box r ∈ (0.001, 2], K ∈ [951, 5000]; keep the floor classes frozen at the committed residual percentiles (classes are declared objects, not refit); compute the kernel by forward-mask grid iteration (the map is monotone on the domain); constructive bound g(K*) − |e_q10|; expansion classification F′(K*) = 1 + r·ln(K/K*) − r. Report as the third co-equal form in §3.6 | ~1 session |
| E2 | xteNCAM labelled sensitivity row (wave-6 #23) | Load Specification B through E1's `run_ladder`; refit the same map on the 1954–2024 series; compute kernels against the 276 kt LRP as a labelled different-safe-set row; no pooling | ~1 session |
| E4 | Sequence disturbances (wave-5 #13 part) | Additional post-freeze disturbance layer: e.g. two consecutive drought-floor years then recovery, on the existing kernel recursion | ~1 session |
| E4 | Closed-loop supply (wave-5 #13 part) | Replay-mean pumping under the declared rules on the fitted map with the frozen floor classes (the historical-replay supply exists; the floor-class supply is the declared-scoring missing half) | ~1 session |
| E3 | Pumpage scenario (wave-5 deferred list) | Counterfactual pumpage paths through the fitted map; declared as scenarios, not forecasts | ~1 session |

These are not executed now because the P5 package was the user-named priority; each recipe is complete above.

## 4. Not executable / not computational (classified)

| Paper | Item (origin) | Class | Reason |
|---|---|---|---|
| P5 | Five prospective designs (§4.5) | NEEDS-DATA | Real-system preregistration targets: dated observation/assessment/command records, candidate institutions, protocol IDs. Executing them in silico would fabricate empirical records. |
| P5 | Stage-structured map multiplier scan (paper registration; audit U1(ii) second half) | CODE-ABSENT | The stage map's computational record is not in this workspace; the paper's exploratory-status sentence is now explicitly scoped to the stage map only (P5 v4). |
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

## 5. Closed this wave (status changes in the assessments)

- `joint_assessment_wave5.md` P5 row 10 (U1(ii)/U3/MSE): DEFERRED → EXECUTED (wave 7), model-level.
- `joint_assessment_wave5.md` P4 rows 9–10 (optional micros): skipped → EXECUTED (wave 7).
- P5 v4: §2.2 comparators declaration, §3.4 executed record, limitations (ii) rescoped, abstract and §4.1 clauses.
- P4 v5: §7 similarity clause, §2.4 C₁ anchor.

**Bottom line.** After wave 7, every remaining open item is either venue-pass wording, new mathematics, external data, or code-absent; the only executions still available in silico are the five FEASIBLE-NEXT recipes of Section 3, each about one session, queued in the order listed.

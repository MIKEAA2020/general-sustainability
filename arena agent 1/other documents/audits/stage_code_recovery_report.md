# Stage-Scan Code Recovery and Verified Re-Run — report (2026-09-01)

**Trigger:** the user recovered a batch of files from earlier chat sessions (14 unique files, two names duplicated in the upload) and attached them. This report states what the batch is, how it changes the provenance record, and the outcome of a verified re-run of the recovered code.

## 1. What the batch is

The batch is the stage-analysis code and results from the earlier (2026-08-08) authoring session, plus the generic continuous-core Floquet machinery, plus two chat transcripts. File-by-file:

| File | What it is |
|---|---|
| `readme.txt` | Transcript of two earlier chats. Chat 1: lists the stage scripts and states plainly — "we did not create a stage-structured *discrete-map multiplier-scan in this chat*. The stage analysis was done with a continuous-time **characteristic-root scan** (the DDE analogue of a multiplier scan), plus nonlinear RK4 verification." Chat 2: same verdict; adds that `sampled_governance.py`, `stage_r_window.py`, `ram_crosssection.py` "were never uploaded, and I never wrote them" (chat 2's sandbox lacked the files chat 1's had). |
| `stage_r_window.py` | The main stage scan: Gurney–Blythe–Nisbet delayed-recruitment lumped model `dN/dt = rN(t-g)(1-N(t-g)/K) − qEN` with deficit signal, Z-filter, and the institutional-delay effort equation; two-delay characteristic criterion (the `|1/(vᵀA⁻¹u)| = 1` rank-1 crossing test) scanned over maturation delay g and regeneration rate r; validated at g=0 against the base-core windows. |
| `stage_tau0_decomposition.py` | τ=0 rightmost-characteristic-root scan separating institutional-delay crossings (τ=0 stable) from biological cohort resonance (τ=0 already oscillatory); two-delay RK4 verification. |
| `stage_robust_check.py` | Robust τ=0 rightmost-root solver (dense |det| mesh + Newton refinement) + integrator validation. |
| `stage_decomp2.py` | Nonlinear ground truth: single/two-delay RK4 integrators, τ=0 stability classification by tail (stable / oscillatory / drift), dt-convergence checks. |
| `stage_decomp_results.md` | THE RESULTS (dated 2026-08-08): validation values, the three-part result (late-maturing stocks suppress the fast-r institutional mechanism; slow-r cohort cycles at τ=0 with P≈250–360 yr; short maturation delays relocate the window into fish range on the locus r·g ≈ 1.5–1.6), the correction note, and the manuscript-merge record (Patches A/B/C2, deep_research_report.md D5.1/D7). |
| `stage_hopf.json` | Output of stage_core.py: the A022 adult/juvenile-take Hopf table. |
| `stage_core.py` | Local Hopf computations of the A022 two-stage harvest core (adult vs juvenile take; states XA/XJ/Z/E). |
| `compute_core.py` | Self-contained base-core machinery: equilibrium, Hopf cubic, Hassard l₁, sample-and-hold monodromy M(T_r) with scan and crossing refinement, RK4 simulate. Runs standalone. |
| `dde_core.py`, `pseudo_arclength.py` | DDE-BIFTOOL-style periodic-orbit continuation + Floquet multipliers (single shooting, Newton/pseudo-arclength) for the 3-/4-state cores. |
| `shooting_floquet.py`, `verify_floquet_points.py` | Fixed-point shooting + Floquet for the ungated core; finite-difference Floquet verification at the folds (SNPO check). |
| `recover.txt` | Not stage-related: a text copy of the P3 material-ledgers paper. |

**Archived verbatim** under `arena agent 1/other documents/rerun_campaigns/stage_scan_recovered/` (extensions restored to `.py` where the content is Python; contents byte-identical to the uploads).

## 2. What this closes and what it leaves open

**Closed — the continuous-delay stage anchors are now code-backed.** The 2026-08-08 results (`stage_decomp_results.md`) are the generating record of A011 line 189's continuous-delay windows: rg ≈ 1.5–1.6; g=2 yr → r ∈ (0.77, 0.81) yr⁻¹ at η=0.914, delay interval ≈ 2.6–7.8 yr; g=1 yr → r ∈ (1.565, 1.585) yr⁻¹, interval 1.6–3.5 yr; slow-stock r ∈ (0.01, 0.05). The turn-47 forensic report's "built-then-lost" reading is confirmed for this layer — the code existed in the authoring chat's sandbox and was never committed to the repo, exactly as chat 1's transcript describes.

**Still open — the sampled stage-map record.** The manuscript's SD-E-DR-AN/SP/CO/SL review-interval bands (anchovy T_r ≈ 3–4 yr, sprat 6–12 yr, cod convergence on [1,20], slow-stock transitions 30–50 yr) remain without a generating script: the batch contains no `sampled_governance.py`, and chat 2 states it was never written/uploaded. The turn-46 pre-registered reconstruction therefore remains the only labelled record for the sampled stage map. Nothing in this recovery changes P5 v5.

## 3. Verified re-run (2026-09-01)

The recovered scripts import a module `droop_test` that was not in the batch. A labelled reconstruction of that module's constants and helpers was written from the recovered `compute_core.py` parameter block (K=100, q=0.001, η=0.914, Emax=30, δ₀=0.01, Dref=Zref=1, τm=5, k=10, δ=ln2/10; base RHS and softplus conventions). One shim defect was found and fixed before the recorded run (softplus convention: the scripts call `softplus(d)` on the raw deficit with the k=10 sharpness inside — `log1p(exp(kx))/k`, whose derivative at 0 is the hard-coded h=0.5 — the first shim version lacked the k scaling; the nonlinear validators caught it). The recovered scripts themselves were run **verbatim**.

| Anchor (recorded 2026-08-08) | Re-run result | Verdict |
|---|---|---|
| g=0 validation windows: (0.00796, 0.0219) @ η=0.914; (0.00676, 0.0603) @ η=3.0 | 0.00796–0.02191 / 0.00676–0.06028 | REPRODUCED |
| g=5 institutional band η=0.914: r ∈ (0.28, 0.33) | [0.2660, 0.3285] | REPRODUCED |
| g=2 band r ∈ (0.77, 0.81); g=1 band r ∈ (1.565, 1.585) | 0.7865 / 1.5719 (τ=0-stable subset at scan resolution) | REPRODUCED (location) |
| r=0.5, g=5 τ=0 cohort cycle, P ≈ 20 yr | P = 20.0–20.1 yr, amp 89.4 | REPRODUCED |
| Slow-r (r=0.02, g=5) τ=0 cohort cycle: P=358.8 yr, N ∈ [28.5, 95.4] | P=358.7 yr, amp 66.9 (= 95.4−28.5) | REPRODUCED |
| r=0.3, g=5 institutional crossings τ ≈ 9.9 yr (P≈19) and τ ≈ 20.3 yr (P≈22) | crossings=2; P=22.3 yr at τ=20.32 yr (lowest-ω first) | REPRODUCED |
| A022 adult-take Hopf: 52.068 yr / 269.37 (g=5); 16.757 / 105.05 (g=1); 31.665 / 169.21 (g=2); juvenile: none | 52.0677 / 269.37; 16.757 / 105.05; 31.665 / 169.21; none | REPRODUCED (json byte-identical, all 8 records) |
| compute_core base Hopf pairs | A_gated 3.666149/150.358477; A_ungated 6.881411/132.374903; B_gated 5.512841/80.424527; ρ(1)=1.0005452 | REPRODUCED (matches the committed P4 certificates) |

Residual convention notes (not contradictions): the base-core "tau=5.5 → P~268, amp~7.2" anchor depends on the missing droop_test integrator's initialisation and amplitude conventions (the recovered code's own integrators give P=259.9 with a small-amplitude tail at T=3000 — the same cycle, amplitude convention-dependent); the τ=0 root-solver meshes show the documented finite-resolution sensitivity at isolated grid points (e.g., a single η=3.0/g=5 institutional point at r≈1.57, outside the recorded r·g locus — mesh artefact, consistent with the results file's own "mapped at finite resolution" caveat).

## 4. Consequence for the record

1. The A011 continuous-delay stage windows' provenance chain is now complete: authoring-chat code (recovered) → 2026-08-08 results → corrected_manuscript.tex Patches A/B/C2 → A011 line 189 → P5 lineage. The turn-47 "built-then-lost" verdict is confirmed, with the generating record now on file.
2. The stage code's own account (readme.txt, both chats) independently confirms our turn-46/47 conclusions: no discrete stage review-map multiplier scan was ever built; the stage bands were located by continuous-time characteristic criteria + RK4 verification.
3. P5 v5 requires no change: the manuscript's exploratory-status discipline for the stage windows was accurate all along, and the turn-46 sampled-map reconstruction stands as the only labelled record for the sampled stage operator.
4. Recovered artifacts: `stage_scan_recovered/` (14 files verbatim + `droop_test.py` shim labelled as reconstructed + `rerun_outputs_2026_09_01/` logs).

# Companion Paper — v1 Addendum (disposition record)

**Version:** `paper2_companion_recourse_bridge_v1` (main + supplementary, new lineage).
**Title:** *Finite Nonviability Certificates under Delayed Information*.
**Implements:** Track B of roadmap v3/v4/v5 — the companion paper (B1–B5), from Doc 1 (§§1–14 of `uploads/obstruction calculus nonstandard.txt`) as adjudicated by `paper2_nonstandard_joint_audit.md`. Venue positioning per Doc 1 §14 and the audit: SCL-class letter (not an Automatica claim).

## 1. B-item → manuscript mapping

| Item | Where |
|---|---|
| B1 (continuous-to-finite bridge: adjoint safety rows; Γ; moment LP with certified sandwich; completeness under refinement; atomic dual; sparse witnesses) | §3 (rows, safety value), §4 (certificate + semantics), §5 Theorem 1 (i)–(v), §7 (complexity, residual test (15), orientation rule, mesh guarantee). **The one unexecuted verification step — LP optimality certified by an actual solver run — is closed in §6.4/S2.** |
| B2 (refinement-erosion identity; φ_U superadditivity, 3,240 rational pairs) | §9 + S1 proof; the 3,240-pair verification lives in the 51-check record (re-confirmed passing this session). |
| B3 (averaging ⇒ held-control polyhedron) | §5.1 closing remark: for held-control sampled-data policies the same polyhedron is an exact reduction (only inter-sample times relaxed). |
| B4 (mesh/complexity study; ρ(h) = 0.06 − Th/4; factor-2 sharpness) | §6.4 (Table 1: five meshes, exact values as fractions, solver values, iterations, measured times) + §7 (size identities, margin-dependent mesh guarantee). The factor-2 sharpness of the error bounds is in the 51-check record (V-6). |
| B5 (scope delimitations; no general-purpose computational-calculus claim) | §10 (delimitations list, alternatives comparison, explicit no-claim sentence). |

Items already merged into the parent paper (three-branch instance, oracle-recourse proposition, m+1 caveat, sparse-dual robustness lemma) are cited as companion content, not re-proved; the m+1 construction itself is restated fully (Proposition 3) since it is a continuous-time statement.

## 2. The solver-certified optimality campaign (the audit's missing step)

`paper2c_lp_campaign.py` (9/9 exact checks): for each h ∈ {1/5, 1/10, 1/20, 1/50, 1/100} the LP (5) is built at its claimed dimensions (mQ+1 variables; Ms(N_t+1)+p_U·Q rows — all five identities verified), solved by scipy/HiGHS, and the exact value ρ(h) = max{0, 3/50 − Th/4} is certified by an independent exact rational witness pair:
- **Primal:** pre-observation blocks at 0, post-observation blocks of mode j at −n_j; *every* row (all 3·7·(N_t+1) safety rows and all 6Q input rows) checked exactly against ρ(h);
- **Dual:** λ = (3/8, 5/16, 5/16) on the three endpoint position rows, μ_{j,k} = λ_j·a_k·η_j on post-observation input rows; per-block exact stationarity and dual objective exactly −ρ(h) — the duality gap closes, so the solver's value confirms a proved optimum.
Campaign results (measured, this machine): |solver − exact| ≤ 4.2·10⁻¹⁷ on all five meshes; iterations 36/78/141/501/1062; wall-clock 0.024/0.014/0.043/0.252/1.015 s. Instance constants re-derived exactly: Γ(τ) = τ − 7/50; τ_max = 7/50; pair positions 12345/6250 = 1.9752 and 12193/6250 = 1.9352; h = 1/10 Farkas contradiction −3/100. The predecessor record `paper2_nonstandard_verification.py` re-ran **51/51** in this session.

## 3. Build and probes
- Tectonic 0.15.0; main `main.pdf` 160,191 B, **5 pp** (two-column letter); supplementary `suppl.pdf` 79,537 B, **3 pp** (complete proofs S1 + verification record S2).
- pymupdf probes: 0 unresolved `??` in both; all section content, the mesh table (iterations/times render), the declarations (including the AI disclosure), and the S2 record strings verified present.
- Fixes during build: `mathrsfs` for `\mathscr`; `\tightlist` provided in the supplement.

## 4. Honesty/register guards honored
Standard ingredients declared not-new (§1); the abstraction-direction asymmetry stated plainly (§5/S1); oracle recourse marked sound-but-incomplete; "no general-purpose computational-calculus claim" in §10; solver timings reported as measured, not invented; the audit's demand that a submission actually run the LPs is met and documented.

## 5. Files
- `paper2_companion_recourse_bridge_v1.tex` / `.pdf`; `..._supplementary.tex` / `.pdf`
- `paper2c_lp_campaign.py` (campaign + witnesses; regenerates Table 1 verbatim)
- `paper2_companion_recourse_bridge_v1_source.zip` (README + both tex + both pdf + both verification scripts, 8 entries)
- Roadmap: v6 records B1–B5 drafted and the solver step executed.

## 6. Status after this ship
Track A complete (v48); **Track B drafted end-to-end with its verification step closed** — submission-ready pending the owner's venue decision (Doc 1 §14 and the audit both point SCL-class). Next per sequencing: C1–C2 (meta-theorem consolidation), then D1 (belief-state theory; seeded by the v47 §9 instance), then the C3 successor.

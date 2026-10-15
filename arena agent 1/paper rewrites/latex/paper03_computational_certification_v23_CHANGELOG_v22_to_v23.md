# paper03 — computational certification: changes from v22 to v23

**Base.** `paper03_computational_certification_v22.tex` + `_supplementary.tex` (`e2-v3-source-year`, `arena agent 1/agent workspace/papers/`), the newest edition of the lineage on any branch (branch-wide check 2026-10-15; the `main` lineage `paper2_computational_certification_v*` stops at v18/v20 and is an ancestor of v22).

**Title (new).** *Finite certificates of nonviability under incomplete observation: a continuous-to-finite bridge with exact witnesses* (v22: *Computational Viability Certification under Incomplete Observation*).

## 1. From technical report to research article

| v22 | v23 |
|---|---|
| `\subsection` used as top level, numbered by hand; one running counter Prop 1 … Prop 9 | Sections 1–10, Appendices A–B; theorem environments numbered by section (Def 2.1 … Prop 7.1) |
| Contributions interleaved with definitions; main theorem stated on p. 3 before the setting is complete | §1 problem → contributions (five, each pointing to a numbered result) → organisation; §2 setting; §3 the bridge theorem; §4 size; §5 instance; §6 prescriptive reading; §7 extensions; §8 computation; §9 related work; §10 discussion |
| References as an unnumbered author–year text list; 25 entries, several uncited | Numeric `thebibliography`, **30 entries, every one cited**; 11 new sources (see §5 below) |
| Two figures (`fig_trajectories`, `fig_hierarchy`) | Four figures: Fig. 1 exact trajectories (redrawn from closed forms), Fig. 2 mesh study with the certified sandwich, Fig. 3 the shared-authority ladder, Fig. 4 pricing an observer; `fig_hierarchy` dropped |
| One mesh table (five uniform meshes) | Table 1 (six uniform meshes, timings re-measured) and Table 2 (seven non-uniform aligned meshes incl. the 2^7-fold refinement with 8 469 rows) |
| Proof of the main theorem in the SI, headline proofs interleaved with discussion | Appendix A: full proof of Theorem 3.2 (seven steps); Appendix B: proofs of Prop 6.1 and Thm 6.2; SI S1–S8 for everything else |

## 2. New mathematical content

* **Proposition 5.3 (mesh law on arbitrary aligned meshes).** ρ(𝓗) = 3/50 − ¼ Σ_J |J|² for *every* aligned mesh containing τ, certified by one mesh-independent primal–dual witness pair; v22 had only the uniform case ρ(h) = 3/50 − Th/4. Verified on twelve meshes (solver agreement ≤ 4.2·10⁻¹⁷ uniform, ≤ 10⁻⁹ non-uniform). Consequence: the smallest certifying aligned program (1 + 6 blocks, 39 variables, 282 rows, ρ = 1/120) and why two blocks cannot certify (ρ = −1/5).
* **Corollary 5.5 (support vs rank).** Minimal support 3 = depth, against the rank bound r + 1 = 65 at h = 1/10 (exact rank computed); the gap is explained, not just reported.
* **Remark 5.4 (a-priori vs realised resolution).** h < 3/340 guaranteed vs h = 1/10 realised (≈ 11× coarser).
* **Proposition 6.1 (shared-authority ladder)** with the exact authorities t*({1,2}) = 2/5, t*({2,3}) = 3/5 and the identity Γ_B(τ) = ζ^max(τ) − 2: dual and schedule are tight against each other at *every* delay, not only at the thresholds.
* **Theorem 6.2** keeps v22's exact pair thresholds (15−√183)/6 and (10−√58)/6 but now with a complete all-control proof (junction values in SM S3) and closed-endpoint statements.
* **Proposition 6.3 (erosion table).** Exact erosion of the triple certificate under every time-zero observer: 33/200, 11/80, 11/80, 11/50 — new; v22 stated the identity but priced no observer.
* **Proposition 6.4 (an observer installed at τ₁) — new.** Eroded certificate Γ(τ₁) = 3/50 − (3/8)[(6/5−τ₁)² − 1] with zero at (6−√29)/5; explicit safe schedule at τ₁ = 3/25 (peaks 999621/500000 and 24993709/12500000); certified bracket [3/25, (6−√29)/5] of width < 3·10⁻³; archived LP sweep at h = 1/100 (21 solves) showing the finite program switching from the triple's certificate to the pair's.
* **Section 6.3 / SM S6 (scoping).** The dilation extrapolation of v22 is demoted to a caution with an explicit counterexample (a = 2, τ = 16/25: weighted critical position 209/100 at t = 37/50 even with independent controls in 2U; nonviable for every τ > 39/100).
* **SM S5.** Example showing the label term moving by 3/4 under a split with zero kernel erosion (the two effects are separate and can have opposite signs).

## 3. Corrections of v22 statements

* v22 SI described the pair {2,3} policy as a "two-phase brake −(2/5)n_j then −n_j"; that leg would peak above 2. The verified policies are: {1,2} blind control (−2/5, ∓4/5), {2,3} blind control n₁, then −n_j to rest (peaks 2469/1250 and 2419/1250).
* Campaign label "12193/6250" for the {2,3} peak is a typo for 2419/1250 (noted in SM S7).
* "n_i·n_j = −3/5 for all pairs" → n₁·n₂ = n₁·n₃ = −3/5 but n₂·n₃ = −7/25 (this is why the {2,3} rung is the highest).
* The certified upper bound now uses h_t = h/2 consistently: ρ + Th/4 + Lh/2 = 7/25, 17/100, 23/200, 41/500, 71/1000 at the five meshes (Fig. 2, SM S2).
* The loose-budget example (ē = e + 1/2) is stated with the correct conclusion: bound 17/100 valid; the uniform special-case formula would give −6/25 < J, which is false — the sandwich must be charged with the budget the program used.
* Residual test and halting-resolution statements now cite the correct equation/theorem numbers in the verifier messages.

## 4. Verification

* New primary record: `paper03_computational_certification_v23_verification.py` (**63 checks, 63 pass**, groups A–K) on top of the exact module `p03_core.py`; optional HiGHS cross-check; reads `observer_sweep.tsv`.
* `make_figs.py`: recompute-then-assert for all four figures; writes the sweep.
* Inherited scripts retained and re-run in this environment: `paper2c_lp_campaign.py` 9/9, `paper2_nonstandard_verification.py` 51/51, `viacert` self-test 12/12.
* Lean layer unchanged (60/60 modules; Farkas soundness only; `native_decide` exceptions declared) — described in §8.2 and SM S7 with the same provenance (runs 36946730855, 36990482599).

## 5. Related work and bibliography

Rewritten as five contrasts (two-sided kernel approximation; moment relaxations; scenario approach — why the guarantee here is worst-case, not probabilistic; minimax reachability / set-membership estimation / imperfect-information games; verified numerics and exact LP) ending in an explicit *what is claimed / not claimed* list. New references: Vinter 1993; Lasserre–Henrion–Prieur–Trélat 2008; Korda–Henrion–Jones 2014; Blanchini 1999; Bertsekas–Rhodes 1971; Witsenhausen 1968; Chatterjee–Doyen–Henzinger–Raskin 2007; Applegate–Cook–Dash–Espinoza 2007; de Moura–Ullrich 2021; Wei–Zhang 2024; Helly 1923. Removed: uncited v22 entries (Anderson–Nash, Cardaliaguet et al. 1999, Hettich–Kortanek, the Zenodo fisheries deposit, the belief-state computation manuscript).

## 6. Files

Main 26 pp. (10 sections + 2 appendices, 4 figures, 2 tables, 30 references); SI 10 pp. (S1–S8, 1 table). Source folder `paper03_computational_certification_v23_src/` with `parts/`, `si_parts/`, `figs/`, `work/` (exact module, figure script, sweep data, inherited scripts, `viacert`).

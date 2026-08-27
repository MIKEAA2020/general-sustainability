# Wave E Design Update — Findings from This Session

**Question:** Does the Wave E design described in the repository require updating to meet findings from this session?

**Answer: Yes — in three specific ways.** The core architecture (five papers, fisheries as the G1 case, the publication waves) is unchanged. But the session produced new theorems, new computational artifacts, and status corrections that the Wave E documents do not yet reflect.

---

## What changed and what it means for Wave E

### 1. New theorems strengthen Papers 1–3 (not yet reflected) — **all statuses are `PROVEN (reconstructed)`**

The following results are recorded in the session theorem files, but **every one of them is a same-agent reconstruction after the filesystem loss** (TRANSFER_AUDIT_RESPONSE Finding 1; PROOF_MANIFEST.md vocabulary): reconstructed ≠ closed atlas content. They may be added to the paper descriptions **only with that qualifier**, and Wave E does not close on them until the independent line-by-line re-verification (the Wave-0 gate) is done:

| Theorem | Paper it strengthens | How |
|---|---|---|
| **A4** Nonlinear assume–guarantee (monotone-operator theorem) | Paper 2 (atlas) + Paper 1 (composition lesson) | The composition gate now has FOUR theorems (not two): the restricted proximal-normal, the tubular A–G, the eroded generation transfer, and the nonlinear monotone-operator version. Paper 2's composition section is substantially richer. |
| **B1** Sampled-data erosion theorem | Paper 5 (governance design) | R02.Cor6's bridge is closed **at the two-depth form** (B1.Thm1 repaired: a sample-time certificate at depth `R` converts to continuous-time safety at depth `r` at the cost `V_max T_s ≤ R − r`; the invariance reading of the original headline is refuted and withdrawn). Paper 5's governance-design section can cite it with that depth bookkeeping. |
| **B9** Stochastic viability (chance-kernel, filter soundness, quantile erosion) | Paper 2 (atlas) + Paper 5 | The stochastic layer — previously a docket item (D3) — now has proved restricted results. |
| **B10** Stackelberg equilibrium existence | Paper 1 (architecture) | The strategic-implementation docket (D5) has its foundational record. Paper 1's institutional section can acknowledge the reduction. |
| **C-a** Decidability at fixed data | Paper 1 (scope) + Paper 5 (computability) | Every governance claim is decidable on the finite class. Paper 5's empirical falsification design is backed by a computability theorem. |
| **E7** Conservation–viability coupling | Paper 3 (the "so what") | Moiety barriers produce kernel bounds from flux data alone. This is Paper 3's missing bridge between conservation and viability. |

### 2. New computational artifacts upgrade Paper 4 (partially reflected)

| Artifact | What it upgrades | Status |
|---|---|---|
| C4 orbit Krawczyk (margin 1186) | Paper 4's certified-computation section | Committed; **interval computation certified with local uniqueness at the K=80 level (discrete)** — Part II validated computation, not a proof |
| C4 off-grid residual (interval-certified v2) | Paper 4's continuum-lift evidence | Committed; interval-verified residual bounds (Part II computation; manifest vocabulary: COMPUTED_PARTIAL-adjacent, no `INTERVAL-CERTIFIED` status exists) |
| C4 monodromy/Floquet (dt=0.25) | Paper 4's cycle stability | Committed; validated computation (not a manifest vocabulary term — Part II row) |
| A025 Hopf certificates (interval) | Paper 4's Hopf section reproducibility | Committed; interval computation with outward-rounded coefficients (Part II) |
| E5 module admission | Paper 3's worked example + Paper 5's template | Committed; **interval-verified admission of the linear A001 §§6–10 toy** (Part II computation; toy scope, R04 transfer prohibition applies) |
| **A025 fold Moore–Spence** | Paper 4's fold certification | **REBUILT (NOMINAL, 2026-08-26)** — the pipeline's four defects are repaired and the nominal fold is reproduced at m=64/96/128, all three inside the lost certificate interval (agreeing to 2.7e-11); the interval Krawczyk certification stage is still not reimplemented |

### 3. Status corrections the Wave E documents must respect

The audit imposed a mandatory vocabulary and the rule "no gate is closed for Wave E." The Wave E documents (D_TIER_EMPIRICAL_AGENDA.md, PUBLICATION_STRATEGY.md) still use the original optimistic phrasing in places.

| Document | What needs updating |
|---|---|
| `D_TIER_EMPIRICAL_AGENDA.md` | The readiness matrix should note that the E5 admission is committed and reproducible (with SHA-256 hash), not just "complete." The three preregistered protocols should reference the E6 matching matrix for their external-literature obligations. |
| `PUBLICATION_STRATEGY.md` | The G-item statuses are stale: G2 (coupling) is now DECLARED, not just open; G4 (selectors) has a proved measurable half; G6 (TCS-1.1) is FROZEN. The Paper 2 content description should include the new theorems (A4, B1, B9, B10). The Paper 3 description should include E7. **[Post-transfer-audit correction: G6 FROZEN means the DIFF is frozen — TCS-1.0 remains the controlling schema; migration open; see TRANSFER_AUDIT_RESPONSE.md Finding 3.]** |
| `OPEN_PROBLEMS_REGISTER.md` | Already updated with the post-addressment statuses — but the rebuilt version (from the filesystem reset) is abbreviated and may have lost some detail. |

---

## Concrete updates needed

### PUBLICATION_STRATEGY.md additions

1. **Paper 2 content**: add "nonlinear assume–guarantee composition (A4), sampled-data erosion (B1), stochastic viability layer (B9), Stackelberg equilibrium (B10), decidability (C-a)" — **each cited as `PROVEN (reconstructed)` pending independent re-verification, not as closed atlas content**
2. **Paper 3 content**: add "conservation–viability coupling (E7) as the paper's bridge theorem" — **same reconstruction qualifier**
3. **G-item statuses**: G2 → DECLARED; G4 → measurable selection proved; G6 → FROZEN (**diff only — NOT controlling; TCS-1.0 controls; migration open**)
4. **Wave 0 readiness**: add "independent rerun of all committed computational artifacts" as a prerequisite (it is the gating item per PROOF_MANIFEST.md “Reproducibility status” (the consolidated disclosure content))

### D_TIER_EMPIRICAL_AGENDA.md additions

1. **E5 cross-reference**: note the committed artifact with hash
2. **Protocol external obligations**: reference E6's matching matrix
3. **G1 readiness note**: the fisheries resource–sink template is not just designed but committed with interval-verified numbers (E5_NUMBERS.json)

### OPEN_PROBLEMS_REGISTER.md

Already has the post-addressment update. The rebuilt version is faithful.

---

## What does NOT need updating

| Item | Why |
|---|---|
| Five-paper architecture | Unchanged — the session's theorems strengthen existing papers, they don't create new ones |
| Fisheries as the G1 case | Unchanged as the **empirical** G1 case; E5's admission is the linear toy's — it strengthens the worked example, **not** any real-system claim (R04.Thm1's converse forbids transfer to 2J3KL without the five-map certificate, not constructed; repaired per `batch 4/CROSS_DOCUMENT_CONSISTENCY.md` C5) |
| Consolidation decisions (Paper 6/7 folds) | Unchanged **as proposals** — the folds are editorial defaults, not gates; final decisions wait for Wave-0 close (the Paper 4 capstone content they fold into is itself NOT CONFIRMED; see PUBLICATION_STRATEGY.md "Proposed consolidations") |
| Release wave structure | Unchanged (Wave 0 still gates on G5/G6-migration/manifests — G6's *migration*, not merely the freeze, is the gate) |
| The monograph and compendium roles | Unchanged |

---

## Bottom line

**Scored trees now live on this repository:** `wave_e_cod/` and `wave_e_edwards/`. Strategy documents must cite those paths, not a “local-only” tree. Independent rerun of those scores is **done** (`batch 4/WAVE_E_RERUN.md`: 30/30 result files byte-identical) — `INDEPENDENT_RERUN_NONE` is false for the scored trees. Wave E is not closed.

**The Wave E design is structurally sound but needs three specific content updates:**

1. **Add the new theorems to the paper descriptions** (A4, B1, B9, B10, C-a, E7)
2. **Update the G-item statuses** (G2 DECLARED, G4 half-proved, G6 FROZEN-diff-only — TCS-1.0 controls until migration)
3. **Add the independent-rerun prerequisite to Wave 0** (it is the single gating item)

None of these changes the architecture or the sequencing. They make the existing design reflect what was actually proved and computed this session. **Wave E is not closed:** the theorem files are reconstructions pending independent line-by-line re-verification, and the Paper 6/7 folds remain proposals. **[Update 2026-08-26: the two scored trees are now spec-matched at the artifact level (`batch 4/WAVE_E_SPEC_MATCH.md`, 36 machine checks exit 0); the Part III paper-support rows remain NOT CONFIRMED — they concern paper claims, not the trees.]** The scored-tree artifacts and the five Part II discrete certificates now have independent reruns (`WAVE_E_RERUN.md`, `VALIDATED_COMPUTATIONS_RERUN.md`); that is a citation-gate discharge, not a Wave E close.

---

## Update 2026-08-26 (b): the Edwards intervention-selection leg — §15's third leg exercised on a real system

**New scored leg** in `wave_e_edwards/`: `protocol_intervention.md` (locked before scores), `src/run_intervention.py` (deterministic), `results/intervention_results.json` + `results/intervention_boundaries.csv`, manuscript `manuscript/wave_E_edwards_intervention.md`, and the kernel-level Cor2 admission row `admission/R04_Cor2_edwards_kernel.md` (the H0 forecast-map row's sibling, with the Cor2 triple computed and the R03.Cor5 erosion conversion invoked — the first kernel-level admission of a real governed system in this programme).

What it scores: governance operators (BAU / flat caps / Stage-I reactive / CPM cascade) by robust viability kernels under declared persistent recharge floors (UC-min/q05/q10), at both declared safe sets (618 ft physical, 660 ft institutional), with supply replays, the 1950s stress counterfactual, and a frozen retention rule mirroring the ladder's persistence benchmark.

Verdicts (first run 2026-08-26; independent rerun 2026-08-26 BYTE-IDENTICAL — `reaudit/intervention_rerun/INTERVENTION_RERUN.md`):

1. **S1 and cpm RETAINED** (nominal, drought-floor/physical reading): the reactive rules match the flat caps' robust invariance while supplying +3.3% (vs flat-90) to +50.6% (cpm vs flat-60) more water. The reactive architecture earns its complexity — the first *positive* selection result of the empirical programme.
2. **BAU is not robustly viable beyond ~14 years** under the perpetual-1956 floor (kernel empty; a 7.2% mean pumping cut restores invariance of the 618 ft set).
3. **Negative certificate at the institutional threshold**: every declared policy ≡ BAU there (the CPM triggers sit below every policy's robust boundary); even zero pumping empties by T≈6–11. The institutional set is protected by wet years, not demand management — the frequency-management rationale is outside the robust-kernel frame.
4. **Certified kernels are defect-bound to T ≤ 3 years** (ε = 15.41 ft train max, r_∞ = 60.7 ft; the OOS audit exceeds ε at 21.81 ft). The binding constraint on certified intervention claims is the model defect, not the governance — the information-layer rent again.

Status discipline: no forecast module promoted or demoted; the fibre and oracle stay excluded; no two-pool claim; K_inst not applied pre-2007; everything `APPROXIMATION`. Wave E is still not closed (Part III paper-support rows remain NOT CONFIRMED). **[Update 2026-08-26 (d): the intervention artifacts are now rerun — both artifacts byte-identical on a fresh second-session execution of the committed runner (`reaudit/intervention_rerun/`; same environment as the original run — committed-code reproducibility verified, cross-toolchain standard not met in this sandbox and still available); the first-run limitation is discharged at the reproducibility level.]**

---

## Update 2026-08-26 (c): the two forecast-ladder manuscripts consolidated (one paper per system)

At the owner's instruction, each Wave E forecast-ladder paper's two versions were made into one file: `wave_e_cod/manuscript/wave_E_cod_forecast_ladder.md` and `wave_e_edwards/manuscript/wave_E_edwards_forecast_ladder.md`. Neither version strictly superseded the other as delivered — the version-2 rewrite had dropped substantive version-1 facts while adding its own (the d844e0a restorations had already recovered the figure-caption values, the rolling n=21 at h=5 clause, the STATLANT identity, the 2021 ≈ 400 kt checkpoint, and the Regular LRP interval) — so the consolidation first restored every residual dropped fact into the version-2 base, making it a verified strict superset of both predecessors, then deleted the superseded `*2.md` files.

Residual facts restored into the cod paper: the A005/A004 conditional-admissibility + blocking-list clause and the groundwater/phosphorus opening condition; the two dropped specification rows (𝒟 capelin-excluded, 𝒩 not-the-2023-LRP); the regime-coarseness honesty clause; the M4 information-cost sentence; the Figure 2 AR-under-prediction caption; A014 Proposition 2 (conditional form) on the unidentified Allee; the 2015 Schijns-catch-matches-DFO clause; ΔS ≫ C_t; the three checkpoint confidence intervals (22–31 / 381–534 / 246–475); the no-licence-to-splice and 34%-of-the-old-LRP clauses; the second-independent-negative-certificate framing; the A014-L4 tightens clause; the R03 descriptive/inner-certificate clause; the H8 kernel framing; the new-admission-row requirement; the computational-protocol-not-preregistration honesty clause; the E5-template / A012-not-RFDE / A016-unarchived-CSD programme rows; the Wave E support rule; and the honest-reading paragraph.

Residual facts restored into the Edwards paper: the series-lock/status header; the R04-prefers-groundwater clause; the "Phosphorus is not opened" clause; the ENSO/rain-not-substitutes clause; both F1-pinned class-demotion phrases ("not extra structure", "Promoting them is inflation"); the M2m demotion sentence; "thin retain (0.39 ft)"; the 2016-cod-LRP parallel; the A005 parameterization row (q_rel removed, leakage N/A, no B_k or χ); the declared-APPROXIMATION-defect clause; E5-is-not-this-specification; the Wave E support rule; the honest-reading paragraph; the fibre caption role clause; and the next-article discipline (no PDO/AMO reopening on this origin; a mid-year nowcast is a new protocol).

Machine check: `reaudit/verify_wave_e_consolidation.py` (exit 0) audits the superset claim at the fact level — every fact string from both predecessor versions (v1-only, v2-only, and shared, including all table numbers) is verified present in the consolidated file, the `*2.md` files are verified gone, all referenced figures exist, and the F1-pinned phrases survive. PROOF_MANIFEST Part VI re-pins both manuscripts at their consolidated hashes. No score, retention decision, admission status, or spec-match verdict changed: the consolidated papers are the same scored objects with the same frozen numbers. All suites pass on the edited tree (verify_wave_e 64 OK, verify_wave_e_spec_match 36/36, verify_wave_e_consolidation, verify_validated_computations, verify_manuscript_sweep, verify_concordance_rows, and verify_consistency with exactly its documented 10 defect-gone failures). The intervention manuscript (`wave_E_edwards_intervention.md`) is a separate leg, not a version pair, and is untouched.

---

## Update 2026-08-26 (e): the cod-side Cor2 analogue — the §15 intervention-selection leg executed on Ω_2016 (G1a)

**New scored leg** in `wave_e_cod/`: `protocol_intervention.md` (frozen before scores), `src/run_intervention.py` (deterministic), `results/intervention_results.json` + `results/intervention_boundaries.csv`, manuscript `manuscript/wave_E_cod_intervention.md`, and the kernel-level Cor2 admission row `admission/R04_Cor2_cod_kernel.md` (APPROXIMATION — the governed surplus object of the ladder's own M2 class; no E5 transfer; no Ω_xte row). The last open G-EMP gap item (i) is closed at the executed level: the intervention-selection leg now runs on **both** scored systems.

What it scores: robust viability kernels of the single declared safe set (the LRP, 884.6 kt) for a declared catch-policy family (BAU moratorium-level 5 kt; flat caps ρ·240 kt; S1 — the DFO-2009 critical-zone rule at a 60 kt cap; a declared [N] cascade) under persistent productivity-shock floors from the fit-window residual distribution (UC-min −460.0 / q05 −318.8 / q10 −114.8 kt yr⁻¹), with supply and stress replays and the frozen retention rule (the Edwards rule verbatim, one safe set).

Verdicts (first run 2026-08-26; independent rerun 2026-08-26 BYTE-IDENTICAL — `reaudit/intervention_rerun_cod/INTERVENTION_RERUN_COD.md`):

1. **Productivity negative certificate.** Under UC-min and UC-q05 the worst-case map has no positive fixed point for any catch level, zero included (g_max = rK/4 = 296 kt yr⁻¹ is below the persistent floor): every infinite-horizon kernel is empty for every policy. The LRP is protected by good years, not by catch management — the cod analogue of the Edwards institutional negative certificate, here at the primary safe set.
2. **No policy retained (negative selection).** S1/cpm are strictly less protective than BAU at the boundary (their 60 kt cap removes catch exactly where the moratorium already sits at 5 kt) and improve on BAU at no reading. The mirror image of the Edwards positive result: which governance architecture earns its complexity is system-dependent — the theory's deliverable is the scored comparison, not a universal architecture verdict.
3. **Constructive boundary.** The maximal robust flat catch is 57.6 kt (24% of the pre-1992 240 kt) under UC-q10; no positive catch is robust under the harsher classes. Certification geometry, not a harvest rule.
4. **The expansion obstruction (certified layer).** The governed surplus map is expansive at the LRP (F′(K*) = 1.153 > 1), so the contraction form of the Cor2/Cor5 erosion conversion is inapplicable — the first object in this programme where this occurs; the expansive form empties every certified kernel beyond T = 5 yr. A qualitatively different failure mode from the Edwards defect-bound (T ≤ 3 yr, contracting map).
5. **Contrasts with Edwards recorded:** the cod defect declaration holds out-of-window (OOS max 47.1 kt vs the 460.0 declaration; Edwards' was exceeded); the cod stress replay confirms the crash is a productivity event (every policy exits the LRP under the observed 1991–95 residuals); only 3–4 of the 33 observed years (the 1980s peaks) lie inside the T=5 nominal kernel even under the mildest class.

Also found while building this leg: a latent `lt` asymmetry in the Edwards runner (empty kernel treated as −∞ in the strict-improvement test but +∞ in the weak test) — provably inert for the committed Edwards artifacts (zero module-empty/BAU-nonempty boundary pairs; audit recorded in PROOF_MANIFEST Part VI); the cod runner implements the consistent semantics. The pinned Edwards code and artifacts are untouched.

Status discipline: no forecast module promoted or demoted; no E5 transfer; no Ω_xte row; K bound-pinned disclosed; the residual's shock/model-error conflation disclosed; everything APPROXIMATION. First run; rerun NONE. Wave E is still not closed (Part III paper-support rows remain NOT CONFIRMED). **[Update 2026-08-26 (f): the cod intervention artifacts are now rerun — both artifacts byte-identical on a fresh second-session execution of the committed runner (`reaudit/intervention_rerun_cod/`; same environment as the original run — committed-code reproducibility verified, cross-toolchain standard not met in this sandbox and still available); the first-run limitation is discharged at the reproducibility level.]**

---

## Update 2026-08-26 (f): the cod intervention leg rerun — both systems' §15 legs now rerun-verified

The cod intervention artifacts are now rerun byte-identical on a fresh second-session execution of the committed runner (`reaudit/intervention_rerun_cod/`: `intervention_results.json` 76f31745… and `intervention_boundaries.csv` cd8e97cb… both hash-match the committed pins; exit 0, ~1.9 s, deterministic). Every headline verdict re-observed: the fit (r = 0.2369, K = 5000.0 bound-pinned; ε train max 460.0 kt at 1992; OOS max 47.1 kt not exceeded), the productivity negative certificate (no positive fixed point under UC-min/q05 for any catch level), the no-retention verdict (S1/cpm strictly less protective than BAU), the maximal robust flat catch 57.62 kt at UC-q10, the expansive erosion conversion (a_max = 1.1531, r_5 = 3120.5 kt; certified horizons T = 5), and every stress replay exiting the LRP. Same honest scope as the Edwards rerun: same-environment second session (Python 3.12.13 / numpy 2.1.3 / pandas 2.2.3 — the same interpreter as the original run), so this verifies committed-code reproducibility, determinism, and freedom from uncommitted state; the cross-toolchain standard of the Task-29 Part II reruns remains available to a future rerun.

With this, **both scored systems' intervention legs are rerun-verified**, and the empirical programme's central cross-system finding — opposite retention verdicts on the two real systems under the same frozen retention rule (Edwards: S1/cpm retained; cod: nothing retained) — is reproduced on fresh executions of both committed runners. The first-run limitation on the cod leg is discharged at the reproducibility level. Registers updated: PROOF_MANIFEST Part VI (the six cod rows + the independent-rerun-status paragraph), ARTIFACT_MANIFESTS (status overrides, 50 artifacts, 7/7 pinned verified), remaining_obstacles (G-EMP gap (i) rerun clause), OPEN_PROBLEMS_REGISTER G1, D_TIER (the three-object table's rerun column).

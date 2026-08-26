# PROOF_MANIFEST — Complete Theorem and Artifact Register

**Commit context:** This manifest accompanies the commit "Status corrections after audit: no closed gates for Wave E". It is the authoritative register of every theorem, computation, and artifact in the programme, with honest statuses.

**Post-transfer-audit revision (see `TRANSFER_AUDIT_RESPONSE.md`):** all three external-audit findings accepted and repaired — (1) the session theorem files were short summary cards after the filesystem loss, and are now **expanded to full self-contained proof documents with provenance headers**; (2) the E5 module is re-scoped everywhere as the **linear A001 §§6–10 toy — no transfer to either real system (the 2J3KL cod fishery or the Edwards J-17 aquifer system) or any other model without the R04 certificate**; (3) **TCS-1.0 is the controlling schema** (TCS-1.1 is a frozen, unapplied diff — no record conforms to it).

**Controlling-schema statement:** every theorem, record, and artifact below is a **TCS-1.0** object. The judgment language of E1/C-a is the TCS-1.0 §4 inventory. No compatibility claim "under TCS-1.1" is available to any entry. Migration is an open Wave-0 obligation (see `04_open_problems/TCS_1_1_FREEZE.md`).

**Vocabulary (mandatory, no exceptions):**
- `PROVEN` — formal proof, self-contained in the cited file
- `PROVEN_CONDITIONAL` — formal proof under explicitly listed hypotheses
- `PROVEN (reconstructed)` — full proof now self-contained in the cited file, but the proof is a same-agent reconstruction from the session record after the filesystem loss; **independent line-by-line re-verification is an open obligation before submission**
- `COMPUTED_PARTIAL` — numerical computation with validated or unvalidated inputs; the result is evidence, not proof
- `SPECIFIED` — method or route described but not executed
- `OPEN` — no proof, no computation, no specification

**Rule:** No gate is treated as closed for Wave E. Every Wave E support row is NOT CONFIRMED.

---

## Part I — Theorems (by source)

### A. Packet bases (pre-existing, accepted in the math closure packet)

| # | Theorem | Statement (abbreviated) | File | Status |
|---|---|---|---|---|
| B1 | Strong invariance + conditional tubular erosion | Lipschitz envelope + proximal normal inequality ⟹ strong invariance; erosion `L_G r + Δ ≤ α` under prox-regularity | `research_program/general_theory_math_closure_packet/corrected_theorems/02_*.md` | PROVEN |
| B2 | Restricted proximal-normal composition | Joint feasibility of proximal normals on product sets ⟹ product invariance | `corrected_theorems/03_*.md` | PROVEN |
| B3 | Finite-architecture exact-tube Operator II recursion | Backward recursion with exact tubes = the transformation kernel | `corrected_theorems/04_*.md` | PROVEN |
| B4 | Sampled/RFDE/hybrid kernel chain | Review-time, inter-sample-safe, and information-state kernels under compactness/continuity | `corrected_theorems/08_*.md` | PROVEN (restricted classes) |
| B5 | Projectability criterion, fibre obstruction, spatial aggregation | Exact autonomous closure ⟺ dPF fibre-constant | `corrected_theorems/09_*.md` | PROVEN |
| B6 | Conservation, moiety positivity, noncompensation, Farkas | Typed conservation telescoping; Farkas separation for linear substitution | `corrected_theorems/07_*.md` | PROVEN |
| B7 | Operator I judgment hierarchy (Props 1–8) | Monotonicity calculus for viability judgments | `corrected_theorems/01_*.md` | PROVEN |
| B8 | Recovery idempotence, common-action obstruction, delayed-information obstruction, adversarial exit | Selected Operator I audit results | `corrected_theorems/06_*.md` | PROVEN |

### B. Batch-2 result records R01–R09 (as submitted; repairs documented in the joint audit)

| # | Theorem/Result | Statement (abbreviated) | File | Status | Notes |
|---|---|---|---|---|---|
| R01.Thm1 | Endpoint-only false positives | Endpoint-only recursion accepts states where every policy violates tube safety | `batch 2/01_result_records/R01_*.md` | PROVEN (with repair: W₁=[−1,1]; open-loop meta-action class) | Original had proof errors; repaired per joint audit |
| R01.Thm2 | Aggregate false positives | Aggregate test passes while componentwise kernel is empty | same | PROVEN | |
| R01.Prop3 | Divergence mechanism | Policy-independent branch divergence vs. safe-set width bounds tube exit | same | PROVEN (with repair: global projected width) | |
| R02.Thm1 | Closed-loop robust institutional viability | If (REG) holds on a downward-closed certificate family, a causal observation-based policy keeps all branches in K | `batch 2/01_result_records/R02_*.md` | PROVEN (with repairs: observation retyped; "computable" withdrawn) | |
| R02.Lem2 | Conservative-filter soundness | Inclusion-monotone update ⟹ B_k ⊆ C_k | same | PROVEN | |
| R02.Prop3 | Conservative incompleteness | Exact filter viable; non-separating coarsened filter nonviable | same | PROVEN (witness repaired: quantized observation) | Original witness was flawed |
| R02.Cor6 | Eroded closed-loop safety | Erosion condition for the sampled system | same | PROVEN_CONDITIONAL (bridge **closed at the two-depth form**: `L_G R + Δ ≤ α`, `V_max T_s ≤ R − r` — B1.Thm1 repaired; residual conditions are model-level, and the empirical NOT CONFIRMED gate stands) | Demoted from "proved"; bridge bookkeeping per `batch 4/PROOF_ELEVATION.md` Finding 8 |
| R03.Thm1 | Certificate trichotomy | Adversarial-exit ⟹ sound for nonviability; margin-with-budget ⟹ sound for viability; else descriptive | `batch 2/01_result_records/R03_*.md` | PROVEN (restated as partial taxonomy) | |
| R03.Thm2 | Stock-to-rate margin failure | T_diag/T* → ∞ without rate persistence | same | PROVEN | |
| R03.Thm3 | Aggregate margins not kernels | Positive aggregate margin while kernel empty | same | PROVEN | |
| R03.Lem4 | Horizon compactness closure | R_∞ = ⋂R_n = RViab_∞ under compactness + Hausdorff continuity | same | PROVEN (hypothesis repaired: Hausdorff continuity, not usc) | Original had insufficient hypothesis |
| R04.Thm1 | Domain admission certificate | Five-map conjugacy ⟹ judgment transfer; witness-necessity | `batch 2/01_result_records/R04_*.md` | PROVEN (necessity re-scoped to uniform transfer) | |
| R04.Cor2 | Approximate admission | Pushed-forward defect + Grönwall | same | PROVEN (with policy-correspondence caveat) | |
| R05.Thm1 | Contract-amplitude composition (Version A) | Λ_i Σ δ_ij(0) + Δ_i ≤ α_i ⟹ product strongly invariant (convexified) | `batch 2/01_result_records/R05_*.md` | PROVEN (with retyping: one-sided (H3), convexified conclusion) | |
| R05.Thm2 | Eroded composition (Version B) | L_i r_i + Λ_i Σ δ_ij(r_j) + Δ_i ≤ α_i ⟹ eroded product invariant | same | PROVEN (same retyping) | |
| R05.Cor3 | Linear gain feasibility | ρ(Γ) < 1 ⟹ M-matrix; r* = A⁻¹b maximal feasible | same | PROVEN (scoping: linearized sufficient; b ≥ 0 for monotone iteration) | |
| R06.Lem1 | Fibre-separation lemma | Exact closure ⟹ dPF fibre-constant | `batch 2/01_result_records/R06_*.md` | PROVEN | |
| R06.Thm2 | Finite-augmentation obstruction | Corrected ∀A∃pair schema ⟹ no finite closure | same | PROVEN_CONDITIONAL (schema; hypothesis near-unsatisfiable for smooth data) | Demoted from "proved" |
| R06.Thm3 | Raw-moment non-closure | No finite raw-moment family closes on non-atomic Σ | same | PROVEN (scope-locked to non-atomic; finite/atomic closures exist) | |
| R06.Cor4 | Approximate closure → erosion | Grönwall + P-saturation/lift | same | PROVEN (lifting-typed) | |
| R07.Thm2 | Generation-indexed continuation | Backward induction with typed reset preimage | `batch 2/01_result_records/R07_*.md` | PROVEN (universal reset preimage displayed) | |
| R07.Thm4 | Alternating-disjoint impossibility | Continuous evolution cannot cross disjoint specifications | same | PROVEN | |
| R07.Thm5 | Nested-compact existence | Compactness + nonempty finite predecessors + policy-tree compactness ⟹ W_∞ ≠ ∅ | same | PROVEN (hypotheses repaired: embeddings, Hausdorff continuity, policy-tree argument) | |
| R08.Prop1 | Exact-observation typed correspondence | Injective observation + exact filter + policy alignment ⟹ kernel correspondence | `batch 2/01_result_records/R08_*.md` | PROVEN (update-commutation hypothesis added) | |
| R08.Ex2(a)-(e) | Five converse counterexamples | Each non-implication witnessed | same | PROVEN (ż typo corrected) | |
| R09.Thm1 Part U | Universal conditional laws | U1–U5: conservation, monotonicity, noncompensation, status discipline, kernel recursion | `batch 2/01_result_records/R09_*.md` | PROVEN (registered inventory; "exact list" withdrawn) | |
| R09.Thm1 Part M | Six independence results | M1–M6: each refuted by axiom-consistent witness pairs | same | PROVEN (M1 global root-locus; M3 scope-locked; M5 forward-complete) | |

### C. Elevation-wave theorems E1–E7 (session artifacts; **full proofs now in the cited files — reconstructed; see TRANSFER_AUDIT_RESPONSE Finding 1**)

| # | Theorem | Statement (abbreviated) | File | Status |
|---|---|---|---|---|
| E1.A1 | Representation theorem | Every judgment = typed viability statement on the product Z; block-necessity by counter-models | `batch 2/02_elevation/E1_*.md` | PROVEN (reconstructed) |
| E1.A2 | Relative completeness | Five inference rules sound; U1–U5 derivable; M1–M6 refuted; maintenance clause | same | PROVEN (reconstructed; relative to claim inventory) |
| E2.B2(a) | Measurable selection | Closed graph + compact U ⟹ KRN measurable selector of safe-action map (weak measurability via the metric decomposition `O = ⋃ₙ{dist ≥ 1/n}`) | `batch 2/02_elevation/E2_*.md` | PROVEN (repaired: one-line measurability repair; conclusion unchanged) |
| E2.B1(a) | Maximal certificate family | Γ monotone on compact lattice ⟹ greatest fixed point exists (Knaster–Tarski); post-fixed sets join-closed, NOT subset-closed; R02.Thm1 applies to 𝒱* itself with 𝒱*-tracking | same | PROVEN (repaired: subfamily-inheritance sentence was backwards — explicit counterexample) |
| E2.B1(b) | Backward iteration = gfp | Closed Vietoris graph + compactness ⟹ backward iteration converges to the gfp | same | PROVEN (reconstructed) |
| E3.C1 | Scalar-delay classification | Complete stability classification for ẋ = −αx(t) − βx(t−τ) | `batch 2/02_elevation/E3_*.md` | PROVEN (reconstructed) |
| E3.C4.1 | Separation ⟺ soundness | M sound ⟺ {M < 0} ∩ kernel = ∅ | same | PROVEN (reconstructed) |
| E3.C4.2 | Uniform-horizon theorem | Compact certified set ⟹ uniform finite exit horizon | same | PROVEN (reconstructed) |
| E3.C6.3 | Delayed-revelation lemma | `Viab_del = T_del` (truncated kernel) exactly; inertness ⟺ `Viab_full ⊆ T_del`; holds if `Viab_full` is prior-admissible-invariant to `t_d`; R02.Prop3 = sharpness witness | same | PROVEN (repaired: recorded iff replaced by the provable truncated-kernel characterisation — the one conjecture-demotion of the lost original is eliminated) |
| E4.Lem1 | Jump-margin transfer | Non-vacuous depth co-Lipschitz margin (`b < ℓ·r̄_g`) ⟹ eroded sets map into eroded sets; declared-data refutation (inradius-extending witness, first failure at `g > 1/(ℓ−2b)`); co-Lipschitz + exterior-preserving companion `(κ, 0)` | `batch 2/02_elevation/E4_*.md` | PROVEN (repaired: non-vacuity added — the recorded definition admitted vacuous pairs; the recorded witness was not load-bearing) |
| E4.Thm2 | Eroded generation transfer | Within-generation (with genuine lower bounds `ρ_g > 0`) + non-vacuous jump-margin + non-Zeno ⟹ eroded path invariant; budget threshold `(b/(ℓ−1))(1−ℓ^{−G})` (tight); sustainability at unbounded horizon iff `ℓ > 1` or (`ℓ = 1`, `b = 0`); required margin `u₀ ~ (ρ + b/(1−ℓ))ℓ^{−G}` | same | PROVEN (repaired: both recorded thresholds were wrong — the corrected negative is stronger: a contracting reset is unsustainable at ANY initial margin) |
| E7.Thm1 | Moiety-barrier production rules | Balanced-budget inner; (b1) robust-kernel emptying / (b2) pathwise exit / (b3) sharp exit time; **sharp** outer `D⁻_T − F⁻_T`; corrected sandwich | `batch 2/02_elevation/E7_*.md` | PROVEN (repaired: (b) split; (c) sharpened with a sharpness proof; (d) sandwich corrected) |
| E7.Thm2 | Multi-moiety noncompensatory | Product inclusion per moiety; sharp noncompensation at `D⁻_{i,T} − F⁻_{i,T}` with the ledger-identity certificate; transfer-invariance verified | same | PROVEN (repaired: committed-budget test refuted — deficit relative to an inner bound does not exclude kernel membership; Farkas invocation removed as unnecessary) |

### D. Open-problems-wave theorems (session artifacts; **full proofs now in the cited files — reconstructed; see TRANSFER_AUDIT_RESPONSE Finding 1**)

| # | Theorem | Statement (abbreviated) | File | Status |
|---|---|---|---|---|
| A3.Thm1 | Interleaved-segment compactness | Budgeted piecewise-history space (with the common segment modulus, derived from the velocity bound) is compact metrizable in the reparametrized interleaved-segment metric; delayed evaluation continuous off break epochs (both window edges) | `batch 2/04_open_problems/A3_*.md` | PROVEN (repaired: common-modulus hypothesis added; derived by dynamical closure; original FALSE_AS_STATED — two counterexamples incl. the bounded-TV witness) |
| A3.Thm2 | Clopen-fibre kernel | Clopen observations + **finite information space** ⟹ information predecessor closes on the finite quotient; kernel = gfp; termination in at most |𝒜|·|ℬ| strict decreases (sharp) | same | PROVEN (repaired: ℬ finite; undefined bound corrected; vacuous clopen clause dropped) |
| A3.Thm3 | Conditional kernel theorem | Budgeted (+ segment modulus, free by dynamical closure) + transversal + clopen + **finite information states** ⟹ variable-event kernel exists | same | PROVEN_CONDITIONAL (condition list extended; substance unchanged) |
| A4.Thm1 | Nonlinear assume–guarantee | Monotone depth-feasibility operator; sub-solution ⟹ eroded product invariant with shared controls, via ⟨n_i, f_i⟩ ≤ −α_i + L_i r*_i + Λ_i Σ_j δ_ij(r*_j) + Δ_i ≤ 0 | `batch 2/04_open_problems/A4_*.md` | PROVEN (repaired: Step 2 sign corrected — the recorded display admitted outward velocities; conclusion unchanged) |
| A4.Thm2 | Sub-solution existence | Tarski greatest sub-solution; monotone iteration; linear case recovered | same | PROVEN (reconstructed) |
| B1.Thm1 | Sampled-data erosion | **Two-depth theorem (R, r)**: envelope + confinement `V_max T_s ≤ R − r` (tight) + successor certificate at depth `R` ⟹ sample-time invariance at `R` and continuous-time safety at `r`; sample-period budget `T_s ≤ (R−r)/V_max` | `batch 2/04_open_problems/B_TIER_*.md` | PROVEN (repaired: two-depth form; the invariance reading of the original headline is refuted and withdrawn) |
| B6.Thm1 | Nonlinear substitution classification | (1) quantitative lsc of the tangent cone with modulus (2L/γ)‖x−x̄‖‖d‖ + exact constancy for strictly feasible directions; (2) Clarke separation under (BLK) with explicit multipliers, reducing to Farkas in the affine case | same | PROVEN (repaired: the original iff is false and robust to MFCQ strengthenings; part (2)'s blocking-direction sign corrected from −d to d) |
| B7.Thm1 | Bifurcation classification | (1) no bifurcation + continuous boundary + **uniform exhaustion radius** ⟹ no kernel change; (2) transversal contact ⟹ kernel change; (3) genericity **conditional on a versal unfolding** | same | PROVEN ((1),(2) with the uniform exhaustion named; (3) PROVEN_CONDITIONAL on versality — narrowed; no strengthening available) |
| B9.Thm1 | Chance-kernel characterisation | `K_p = {x : V_N(x) ≥ p}` exactly (value iteration); the quantile-budget recursion is a sound lower bound at any fixed split; the exact quantile form is the residual-budget DP; `p = 1` reduces to the robust predecessor under support alignment | same | PROVEN (restricted; repaired: the recorded fixed-split equality is refuted by explicit witnesses, as is split-union completeness — see the adjudication in `batch 4/PROOF_ELEVATION.md` Finding 9) |
| B10.Thm1 | Stackelberg strategic implementation | Optimistic value attained (unconditional); pessimistic value lsc — existence **conditional** on BR lsc / single-valuedness / fibre-constancy; `V_pes = V_opt` iff the leader is indifferent on `BR(c*_opt)`; existential safe-command set closed under Berge alone, universal needs lsc; reduction license split per target theorem | same | PROVEN (repaired: ψ-usc and coincidence claims false; pessimistic non-attainment witnessed; see the adjudication in `batch 4/PROOF_ELEVATION.md` Finding 10) |
| C-a.Thm2 | Full decidability | Every judgment sentence (incl. negations) decidable at fixed data, O(N·|grid|) | `batch 2/04_open_problems/CA_*.md` | PROVEN (reconstructed; at declared scope: finite class, TCS-1.0 language) |
| C-a.Thm3 | Zero-one law sharpness | Satisfying sets are exactly the definable Boolean algebra (kernel-membership atoms); models separated only up to kernel-equivalence; non-monotone definable sentences exist (no extremal shortcut); per-instance decidability unaffected | same | PROVEN (repaired: "arbitrary subsets" re-scoped to the definable algebra — the language does not separate table-distinct models) |
| C-e.Thm1 | Quadratic-form moiety barriers | Quadratic moiety sandwich with **finite tubular radius** `τ = √c·√λ_min/λ_max` and **normal variation** `L_n = 1/τ`; sharp ledger outer bound `{B ≥ Φ⁻_T}` | `batch 2/04_open_problems/C_TIER_*.md` | PROVEN (repaired: reach/L_n constants replace the misidentified `L_G`, which is envelope data) |
| C-f.Thm1 | RFDE-aggregate memory | For **window-restriction** observables: closed autonomous aggregate dynamics ⟺ `f` factors through the window projection; minimal such window = memory horizon; general-observable case OPEN (σ-algebra obstruction) | same | PROVEN (repaired, scope-aligned to window observables) |

---

## Part II — Computation artifacts

**Rebuilt and committed from code (this session — git commits 5405654 through 0df499c).** All scripts and artifacts are in `research_program/validated_computations/` in the repository. File hashes are SHA-256 of the committed files.

### Discrete-level validated computations (committed, reproducible)

| Artifact | Description | File | SHA-256 | Reproduction command | Solver | Independent rerun |
|---|---|---|---|---|---|---|
| A025 Hopf certificates | τ± reproduced with outward-rounded interval arithmetic (dps=50) | `a025_fold/a025_interval_hopf.json` | `eda36cd1...95b3b2` | `python3 a025_fold/a025_interval_hopf.py` | Python 3.12.13, numpy 2.1.3, mpmath 1.3.0 | **NONE** |
| C4 orbit Krawczyk | Unique orbit in 1e-8 box, margin 1186, period 370.9311778394 | `a021_c4/c4_orbit_krawczyk_certificate.json` | `5e8df633...65ab133` | `python3 a021_c4/c4_orbit_krawczyk.py` | same | **NONE** |
| C4 orbit Krawczyk (box data) | Orbit + period box (npz) | `a021_c4/c4_orbit_krawczyk_box.npz` | `85f72c76...7ba4c69` | same | same | **NONE** |
| C4 off-grid continuum residual (v2, interval-certified) | Interval-certified bounds: N≤6.6e-8, A≤1.0e-9, Z≤8.3e-7, E≤2.8e-6 | `a021_c4/c4_offgrid_residual_interval.json` | `2a4a5e82...1c74a7f4` | `python3 a021_c4/c4_offgrid_interval_v2.py` | same | **NONE** |
| C4 monodromy/Floquet (dt=0.25) | Phase 1.00480 simple+neutral; dominant 0.68764+0.069<1; all nontrivial inside unit disc | `a021_c4/c4_monodromy_enclosure.json` | `01d8c253...dbaef76` | `python3 a021_c4/c4_monodromy.py` | same | **NONE** |
| C4 monodromy data (dt=0.25) | Monodromy matrix + eigenvalues (npz) | `a021_c4/c4_monodromy_dt0p25.npz` | `f3dc5445...a7ca5f` | same | same | **NONE** |
| E5 module admission | Five maps exact; margins/L/erosion triple interval-verified — **LINEAR A001 §§6–10 TOY ONLY; no transfer to either real system (2J3KL cod fishery; Edwards J-17 aquifer) or any other model without the R04 certificate (not constructed)** | `E5_NUMBERS.json` | `5670bcc8...236e72db` | `python3 e5_admission.py` | same | **NONE** |
| Interval library | Rigorous float64 interval arithmetic (outward rounding, mpmath bridge, dd products) | `interval_lib.py` | see git | — | same | **NONE** |

**Not yet rebuilt (from the prior session, lost to filesystem reset):**

| Artifact | Description | Status |
|---|---|---|
| A025 fold Moore–Spence Krawczyk | τ_f ∈ [5.587236197890, 5.587236199490]; nondegeneracy certified | **NOT REBUILT** — requires the collocation, continuation, and Moore–Spence pipeline (~30 min of computation) |
| A025 fold resolution (m=96, 128) | Both inside the certified interval | **NOT REBUILT** — requires the fold pipeline |
| C4 monodromy (dt=0.1) | Second mesh level | **NOT REBUILT** — the dt=0.25 level is rebuilt and committed |

### Partial computations (COMPUTED_PARTIAL)

| Artifact | Description | Status | What is missing |
|---|---|---|---|
| A1 "orbit ball" (5.544e-3) | Heuristic inference: β_K80 × off-grid residual | **COMPUTED_PARTIAL** | The identification of the discrete inverse with the continuum inverse is unjustified; the piecewise-Chebyshev campaign was NOT executed |
| B4 bunching (**n=35 periods, prefactor-aware**) | Discrete product bunching incl. the prefactor (`product_prefactor_bunching_assessment.md`: closes marginally at 30 periods, robustly by 35; `NUMERICALLY_VERIFIED_DISCRETE_PRODUCT_BUNCHING_AT_35_PERIODS`; not a continuum operator bound) | **COMPUTED_PARTIAL** | Float64 output (not interval); continuum transfer open; the register's earlier n=15 figure was the stable-multiplier-only value superseded by the prefactor-aware assessment (`batch 4/CROSS_DOCUMENT_CONSISTENCY.md` C6) |
| A3 toy kernel | 1D system on the declared class | **NOT IN TREE** (the cited `A3_KERNEL_CERTIFICATE.json` was lost with the filesystem reset and not rebuilt; register entry only, certifies nothing) | Toy instance; no Wave E relevance; see `batch 4/CROSS_DOCUMENT_CONSISTENCY.md` C1 |
| K=1600 Newton (residual 5.6e-6) | Matrix-free GMRES with Fourier preconditioner | **COMPUTED_PARTIAL** | Numerical only; no validated output |
| Tail envelope (Steps 1–2) | Per-state geometric coefficient envelopes verified for k=1..80 | **COMPUTED_PARTIAL** | Verified for computed modes only; extension to k>80 is hypothesis H-tail |

---

## Part III — Wave E candidate support table

**Every row is NOT CONFIRMED. No gate is closed for Wave E.**

| Wave E need | Candidate support | Type | Spec match | Status |
|---|---|---|---|---|
| Paper 4: certified computation (continuum orbit) | K=80 Krawczyk (discrete, PROVEN) + off-grid residual (PROVEN) | Validated computation | The discrete level is confirmed; the continuum lift is NOT PROVED | **NOT CONFIRMED** |
| Paper 4: NAIM persistence capstone | B4 discrete bunching + A2 coupling declaration | Computation + declaration | The bunching is discrete-level; the coupling is declared but the persistence theorem is not proved | **NOT CONFIRMED** |
| Paper 4: fold certification | A025 fold Krawczyk (discrete, PROVEN) + resolution cross-checks | Validated computation | The m=64 level is confirmed; the continuous-DDE lift is open | **NOT CONFIRMED** |
| Paper 5: governance design template | R02 closed-loop bridge (PROVEN) + B1 erosion theorem (PROVEN) | Mathematical theorem | The theorems are proved; no specific model has been verified against their hypotheses | **NOT CONFIRMED** |
| Paper 5: computability guarantee | C-a.Thm2 decidability (PROVEN at declared scope) | Mathematical theorem | The theorem is for the abstract finite class; per-model hypothesis verification needed | **NOT CONFIRMED** |
| Paper 5: falsification predictions | Floquet data (validated at discrete level) | Validated computation | The multipliers are certified at the discrete level; predictions require the calibrated model | **NOT CONFIRMED** |
| Paper 5: empirical case (G1a) | E5 admission template + D-tier readiness matrix | Method + decision | The template is proved; the data assembly is external and NOT DONE | **NOT CONFIRMED** |

---

## Part IV — What Wave E can safely cite (correctly labeled)

| Result | Correct citation form |
|---|---|
| K=80 orbit Krawczyk | "The collocation orbit is certified with local uniqueness at the K=80 level (discrete)" |
| Off-grid residual | "The interpolant's continuum residual is ≤ 3e-6 on a 512-point grid" |
| Monodromy/Floquet (dt=0.25, 0.1) | "The Floquet multipliers are enclosed with certified error balls at two mesh levels (discrete)" |
| A025 fold Krawczyk | "The fold is certified with nondegeneracy at the m=64 collocation level (discrete)" |
| A025 Hopf | "The Hopf delays are certified by outward-rounded interval Newton (exact arithmetic)" |
| A3 topology + kernel theorem | "The variable-event kernel closes on the budgeted-transversal-clopen class (conditional theorem)" |
| A4 composition theorem | "The nonlinear assume–guarantee theorem covers nonlinear contract amplitudes with shared controls" |
| C-a decidability | "Every judgment-language sentence is decidable at fixed data on the finite class (theorem)" |
| E7 conservation coupling | "Moiety barriers produce kernel bounds from flux data alone (theorem)" |
| E5 module admission | "The **linear A001 §§6–10 resource–sink module** is admitted with interval-verified numerical constants — a method demonstration; **no transfer to either real system (2J3KL cod fishery; Edwards J-17 aquifer) or any other model without the R04 certificate (forbidden by R04.Thm1's converse; certificate not constructed)**" |
| B1 erosion theorem | "The **two-depth** erosion theorem converts a sample-time certificate at depth `R` into continuous-time safety at depth `r`, at the cost `V_max T_s ≤ R − r`; this closes the sampled-data bridge with explicit depth bookkeeping (repaired form; the invariance reading of the original headline is withdrawn)" |

## Part V — What Wave E cannot yet cite

| Desired claim | Why not |
|---|---|
| "The continuum orbit exists within a declared ball" | The piecewise-Chebyshev campaign was not executed |
| "The bunching inequality closes in the continuum" | The continuum transfer is open |
| "The NAIM persistence theorem's hypotheses are verified" | The coupling is declared; the theorem is not proved; the computational hypotheses are partially verified at the discrete level only |
| "Every governance claim is decidable against the calibrated model" | Per-model hypothesis verification has not been done |
| "The fold is certified for the continuous DDE" | The bordered infinite-dimensional lift is open |

---

## Reproducibility status

**Rebuilt and committed:** the interval library, A025 Hopf certificate, C4 orbit Krawczyk, C4 off-grid residual, C4 monodromy (dt=0.25), and E5 admission — all with committed code, committed artifacts, and SHA-256 hashes (Part II above).

**Post-transfer-audit expansion (see TRANSFER_AUDIT_RESPONSE.md):** all session theorem documents (E1–E7, A3, A4, B-tier, C-tier, C-a) are expanded from summary cards to full self-contained proof documents with provenance headers; their statuses carry the `PROVEN (reconstructed)` qualifier — same-agent reconstructions from the session record, pending independent line-by-line re-verification. **TCS-1.0 is the controlling schema** (TCS-1.1 is a frozen, unapplied diff; migration open). The E5 artifact is scoped to the linear toy; real-system claims (G1a: 2J3KL cod fishery; G1b: Edwards J-17-type aquifer, Cor2 forecast-map only) are gated on the R04/Cor2 transfer certificate; the A021 J-series is an audit docket, not a real system.

**Not yet rebuilt:** the A025 fold pipeline (collocation → continuation → Moore–Spence → Krawczyk), the C4 monodromy at dt=0.1, and the A025 fold resolution cross-checks.

**Independent rerun status:** NONE for all artifacts. At least one independent rerun is required before submission.

**Environment:** Python 3.12.13 (`/home/z/.venv/bin/python3`), numpy 2.1.3, scipy 1.14.1, mpmath 1.3.0. No containerization. No version pinning beyond the listed versions. The interval arithmetic library (`interval_lib.py`) uses `np.nextafter` for outward rounding — verified against exact rational arithmetic on test cases.

---

## Part VI — Wave E scored trees

Committed on `main` in `4af53e4`. These are **single-run forecast-ladder artifacts**, not kernel certificates. They do **not** close any Wave E gate (Part III still applies: every support row is NOT CONFIRMED). Status vocabulary used here is only:

- `SINGLE_RUN` — produced once from the committed scripts in this tree
- `INDEPENDENT_RERUN_NONE` — no second agent or CI has rerun and matched hashes

Nothing in this section is labeled certified or validated.

Working directory for reproduction commands: repository root, then `cd` as written. Python 3 with `numpy`, `pandas`, `scipy`, `matplotlib`.

### A. `wave_e_cod/` — Northern cod (\(\Omega_{2016}\), \(\Omega_{\mathrm{xte}}\))

Primary \(z\): NCAM M-shift SSB (`data/ncam_2016_table_a2.csv`); xteNCAM Table 17 scored separately (`data/xtencam_table17_ssb.csv`). Not pooled.

| Artifact | Path | SHA-256 | Reproduction command | Status |
|---|---|---|---|---|
| \(\Omega_{2016}\) run metadata | `wave_e_cod/results/meta.json` | `7ae9ba738b3b36665a77ca2ff5002a9e5f801b1d8c64efb1a968d1d867a52eb9` | `cd wave_e_cod && python3 src/run_ladder.py` | `SINGLE_RUN`; `INDEPENDENT_RERUN_NONE` |
| \(\Omega_{2016}\) rolling RMSE summary | `wave_e_cod/results/rolling_summary.csv` | `075b72cff057562a1c6dc1b33db0c5fb73efd12338e766992436ada778d8357d` | same | `SINGLE_RUN`; `INDEPENDENT_RERUN_NONE` |
| \(\Omega_{2016}\) fixed-window scores | `wave_e_cod/results/fixed_window_scores.csv` | `0af788ee59926c285526d539642b255b64f929731442900f9ca7ce7ea68aecf9` | same | `SINGLE_RUN`; `INDEPENDENT_RERUN_NONE` |
| \(\Omega_{2016}\) rolling forecast paths | `wave_e_cod/results/rolling_forecasts.csv` | `d36865d3a5a2a2cd01070ccf160b5d8e5b138ada17911ea0610a49c171b6f9b4` | same | `SINGLE_RUN`; `INDEPENDENT_RERUN_NONE` |
| \(\Omega_{\mathrm{xte}}\) run metadata | `wave_e_cod/results/xte_meta.json` | `7f3730059875007195813acd9041843d06a14332baa21e72cf73a6b473d83649` | `cd wave_e_cod && python3 src/run_xte.py` | `SINGLE_RUN`; `INDEPENDENT_RERUN_NONE` |
| \(\Omega_{\mathrm{xte}}\) rolling RMSE summary | `wave_e_cod/results/xte_rolling_summary.csv` | `b9d5ddbc0d456c27f74d72b50c2049b9ce26676183c808aa2b2c776790032298` | same | `SINGLE_RUN`; `INDEPENDENT_RERUN_NONE` |
| \(\Omega_{\mathrm{xte}}\) fixed-window scores | `wave_e_cod/results/xte_fixed_window_scores.csv` | `073e3f68f2c18625899827d0967478ecb56231819530f2dbefdf2d783bbb0ef8` | same | `SINGLE_RUN`; `INDEPENDENT_RERUN_NONE` |
| \(\Omega_{\mathrm{xte}}\) rolling forecast paths | `wave_e_cod/results/xte_rolling_forecasts.csv` | `080b7255e289cd0d7ed2636ec567e495f40bb0a2d1242459ad2a776c68a04f79` | same | `SINGLE_RUN`; `INDEPENDENT_RERUN_NONE` |
| Capelin-regime summary | `wave_e_cod/results/capelin_regime_summary.csv` | `b874797dc98a5d63e608b04bb264f08cf43f775b92e8f02eec30dcd7622356ae` | `cd wave_e_cod && python3 src/run_capelin_regime.py` | `SINGLE_RUN`; `INDEPENDENT_RERUN_NONE` |
| Capelin-index summary | `wave_e_cod/results/capelin_index_summary.csv` | `0323fc1ee5f9f0fdea0e428c66e11ad0090fbbf19687c8eebe4b9ab635aa7a4e` | `cd wave_e_cod && python3 src/run_capelin_index.py` | `SINGLE_RUN`; `INDEPENDENT_RERUN_NONE` |
| NCAM vs xte overlap audit | `wave_e_cod/results/ncam_vs_xtencam_overlap.csv` | `e8b459383bdc5589c7746cb8d8e6553485a10e48798eb7fe087ca815882f1c83` | derived by `src/run_xte.py` | `SINGLE_RUN`; `INDEPENDENT_RERUN_NONE` |
| Catch overlap audit | `wave_e_cod/results/catch_overlap_audit.csv` | `6759298db718e1cdfa8767f6beb90481c9e51d21f6e6cf6606e37a03f62b007c` | `cd wave_e_cod && python3 src/compare_catch.py` | `SINGLE_RUN`; `INDEPENDENT_RERUN_NONE` |
| Locked NCAM Table A2 | `wave_e_cod/data/ncam_2016_table_a2.csv` | `6645c8e5a4a94074c700a73bad6acc054e1f7b867dcce9ff2f4635fcf9b5dbf6` | input (not generated) | `SINGLE_RUN`; `INDEPENDENT_RERUN_NONE` |
| Locked xteNCAM Table 17 | `wave_e_cod/data/xtencam_table17_ssb.csv` | `c4f4a1ce473f30e9707cb422726c852b1311fac47c207c40d622cead306fd549` | input (not generated) | `SINGLE_RUN`; `INDEPENDENT_RERUN_NONE` |
| Locked Schijns catch | `wave_e_cod/data/catch_schijns_2021.csv` | `4dc174f9e7f6dd5090f9d02cb569165bd0bdbd5038d171026f75e47459fe6db0` | input (not generated) | `SINGLE_RUN`; `INDEPENDENT_RERUN_NONE` |
| Working manuscript | `wave_e_cod/manuscript/wave_E_cod_forecast_ladder.md` | `d8025bb8bcb7c9c18999447b4264bbd3e665cdca40bcca82ca3afc63c72b8f43` | prose; figures via `python3 src/make_figures.py` | `SINGLE_RUN`; `INDEPENDENT_RERUN_NONE` |

A rerun may rewrite floating-point summaries; hash identity is not guaranteed across machines. The retention claim (persist beats M2–M4 on primary RMSE) is a score ranking, not a kernel transfer.

### B. `wave_e_edwards/` — Edwards San Antonio Pool (\(\Omega_{\mathrm{SA}}\))

Primary \(z\): J-17 calendar-year mean head. Locked daily series: `data/j17_twdb_6837203_raw.csv`. Annual panel used by the ladders: `data/annual_panel.csv`.

| Artifact | Path | SHA-256 | Reproduction command | Status |
|---|---|---|---|---|
| Pass 1 run metadata | `wave_e_edwards/results/meta.json` | `0bec06323a66061ac4c1393084c0fb1e3255efe9486ba9e73ce908127bef03b2` | `cd wave_e_edwards && python3 src/run_ladder.py` (uses committed `data/annual_panel.csv`) | `SINGLE_RUN`; `INDEPENDENT_RERUN_NONE` |
| Pass 1 rolling RMSE | `wave_e_edwards/results/rolling_summary.csv` | `5e4b524cd2d0157b0bca5a2ab2ef9a174021c6aa4249a31a74cb71f58e396828` | same | `SINGLE_RUN`; `INDEPENDENT_RERUN_NONE` |
| Pass 1 fixed-window scores | `wave_e_edwards/results/fixed_window_scores.csv` | `bbebc398cd98cdc08412042c58c2e90fdb06006e3365c9d3eb3a6e7e96ad7beb` | same | `SINGLE_RUN`; `INDEPENDENT_RERUN_NONE` |
| Pass 1 rolling forecast paths | `wave_e_edwards/results/rolling_forecasts.csv` | `aa1706bbce24e4aee0df4e4ce16b972e3038c763735da79b6bb531f99b68203f` | same | `SINGLE_RUN`; `INDEPENDENT_RERUN_NONE` |
| Pass 2 metadata | `wave_e_edwards/results/pass2_meta.json` | `f302021f575d22259ee177f35ff268bda3838e89d919cd5326ef1ff1fed25b97` | `cd wave_e_edwards && python3 src/run_recharge.py` (uses committed `annual_panel.csv` climate columns) | `SINGLE_RUN`; `INDEPENDENT_RERUN_NONE` |
| Pass 2 H RMSE | `wave_e_edwards/results/pass2_H_summary.csv` | `088d8b22d8d1e80e3399e0613c49957f670e1935b995cdffb0daefed3d2accce` | same | `SINGLE_RUN`; `INDEPENDENT_RERUN_NONE` |
| Pass 2 R RMSE | `wave_e_edwards/results/pass2_R_summary.csv` | `8690a87128a8fffe34502b8d01bda5ffcc5ab45bfdd831506eb17f4242ef9b88` | same | `SINGLE_RUN`; `INDEPENDENT_RERUN_NONE` |
| Comal fibre summary (post-freeze) | `wave_e_edwards/results/fibre_comal_summary.csv` | `aff3037cfd14e8978d837051b7d3c08b132f0f1a4279c397fde8e0c0f51d102e` | produced by `src/run_ladder.py` fibre block | `SINGLE_RUN`; `INDEPENDENT_RERUN_NONE` |
| Frozen Pass 1 protocol | `wave_e_edwards/protocol.md` | `a9304da9b2b981177cddfcb3bf8f512d7a5c124badf644cd056f081807128ec5` | text | `SINGLE_RUN`; `INDEPENDENT_RERUN_NONE` |
| Frozen Pass 2 protocol | `wave_e_edwards/protocol_pass2.md` | `0573a0fa912942b07213ef8f8bfc3ae4ef8a4885c92429c0d62308602a1061f6` | text | `SINGLE_RUN`; `INDEPENDENT_RERUN_NONE` |
| R04.Cor2 forecast-map row | `wave_e_edwards/admission/R04_Cor2_edwards_H0.md` | `28c0880c16358ede0832274ca8280ceceb267690d43fac62cd94c960cef81449` | text; not a kernel certificate | `SINGLE_RUN`; `INDEPENDENT_RERUN_NONE` |
| Annual panel (H, R, P, climate columns) | `wave_e_edwards/data/annual_panel.csv` | `d6d725db57af5c820d3f62506aa2d5fcd862da3206824d0fa8beb06478706019` | H/R/P: `cd wave_e_edwards && python3 src/build_panel.py`. Climate columns: the three `pcp_*` columns are `NOT_REPRODUCIBLE_FROM_COMMITTED_CODE` (nClimDiv raw omitted); the two Niño columns (`nino34_son`, `nino34_ann`) **do** rebuild from the committed `data/psl_nino34_long.data` (verified to 2.2e-16 / 1.1e-16) | `SINGLE_RUN`; `INDEPENDENT_RERUN_NONE` |
| Locked J-17 daily series | `wave_e_edwards/data/j17_twdb_6837203_raw.csv` | `90208dd6fb30b04cea7cd3b6d85499bf073781bd757b8f2d73269231f9474c2d` | input (TWDB pull) | `SINGLE_RUN`; `INDEPENDENT_RERUN_NONE` |
| Working manuscript | `wave_e_edwards/manuscript/wave_E_edwards_forecast_ladder.md` | `b72d03011fe825a69b5dce3cefa811e3d3e0ff20d6b67ce59b45a13e77b82638` | prose; figures via `python3 src/make_figures.py` | `SINGLE_RUN`; `INDEPENDENT_RERUN_NONE` |

**Climate rebuild.** `src/build_climate.py` reads `data/climdiv-pcpndv-v1.0.0-20260806`, which is **not committed** (URL in `wave_e_edwards/data/SOURCES.md`). Rebuilding the three `pcp_*` precipitation columns from source is `NOT_REPRODUCIBLE_FROM_COMMITTED_CODE`; the two Niño columns rebuild exactly from the committed PSL file (independent rerun reproduced them to machine precision — `batch 4/WAVE_E_RERUN.md` F3). Scoring Pass 1/2 from the committed `annual_panel.csv` does not need the nClimDiv file. Note: `python3 src/build_panel.py` **overwrites** the committed panel with a 15-column version (dropping all five climate columns, no error raised) — reproducing the pinned hash requires restoring the climate columns afterwards (`build_climate.py` with the nClimDiv file, or `git checkout`); see WAVE_E_RERUN F4.

These scores are not E5 numbers, not A021 C4 artifacts, and not a transferred judgment.

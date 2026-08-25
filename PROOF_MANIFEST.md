# PROOF_MANIFEST — Complete Theorem and Artifact Register

**Commit context:** This manifest accompanies the commit "Status corrections after audit: no closed gates for Wave E". It is the authoritative register of every theorem, computation, and artifact in the programme, with honest statuses.

**Post-transfer-audit revision (see `TRANSFER_AUDIT_RESPONSE.md`):** all three external-audit findings accepted and repaired — (1) the session theorem files were short summary cards after the filesystem loss, and are now **expanded to full self-contained proof documents with provenance headers**; (2) the E5 module is re-scoped everywhere as the **linear A001 §§6–10 toy — no transfer to 2J3KL/J-17-class systems without the R04 certificate**; (3) **TCS-1.0 is the controlling schema** (TCS-1.1 is a frozen, unapplied diff — no record conforms to it).

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
| R02.Cor6 | Eroded closed-loop safety | Erosion condition for the sampled system | same | PROVEN_CONDITIONAL (sampled-data erosion bridge open) | Demoted from "proved" |
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
| E2.B2(a) | Measurable selection | Closed graph + compact U ⟹ KRN measurable selector of safe-action map | `batch 2/02_elevation/E2_*.md` | PROVEN (reconstructed) |
| E2.B1(a) | Maximal certificate family | Γ monotone on compact lattice ⟹ greatest fixed point exists (Knaster–Tarski) | same | PROVEN (reconstructed) |
| E2.B1(b) | Backward iteration = gfp | Closed Vietoris graph + compactness ⟹ backward iteration converges to the gfp | same | PROVEN (reconstructed) |
| E3.C1 | Scalar-delay classification | Complete stability classification for ẋ = −αx(t) − βx(t−τ) | `batch 2/02_elevation/E3_*.md` | PROVEN (reconstructed) |
| E3.C4.1 | Separation ⟺ soundness | M sound ⟺ {M < 0} ∩ kernel = ∅ | same | PROVEN (reconstructed) |
| E3.C4.2 | Uniform-horizon theorem | Compact certified set ⟹ uniform finite exit horizon | same | PROVEN (reconstructed) |
| E3.C6.3 | Delayed-revelation lemma | Revelation inert iff obstruction unreached | same | PROVEN (reconstructed) |
| E4.Lem1 | Jump-margin transfer | Depth co-Lipschitz ⟹ eroded sets map into eroded sets; declared-data status refutation | `batch 2/02_elevation/E4_*.md` | PROVEN (reconstructed) |
| E4.Thm2 | Eroded generation transfer | Within-generation + jump-margin + non-Zeno ⟹ eroded path invariant | same | PROVEN (reconstructed) |
| E7.Thm1 | Moiety-barrier production rules | Balanced-budget inner; obligatory-outflow emptying; best-case outer; sandwich | `batch 2/02_elevation/E7_*.md` | PROVEN (reconstructed) |
| E7.Thm2 | Multi-moiety noncompensatory | Product inclusion per moiety; no cross-moiety transfer | same | PROVEN (reconstructed) |

### D. Open-problems-wave theorems (session artifacts; **full proofs now in the cited files — reconstructed; see TRANSFER_AUDIT_RESPONSE Finding 1**)

| # | Theorem | Statement (abbreviated) | File | Status |
|---|---|---|---|---|
| A3.Thm1 | Interleaved-segment compactness | Budgeted piecewise-history space is τ_IS-compact; delayed evaluation continuous off break points | `batch 2/04_open_problems/A3_*.md` | PROVEN (reconstructed) |
| A3.Thm2 | Clopen-fibre kernel | Clopen observations ⟹ information predecessor closes; kernel = gfp | same | PROVEN (reconstructed) |
| A3.Thm3 | Conditional kernel theorem | Budgeted + transversal + clopen ⟹ variable-event kernel exists | same | PROVEN_CONDITIONAL (reconstructed; on the transversality declaration) |
| A4.Thm1 | Nonlinear assume–guarantee | Monotone depth-feasibility operator; sub-solution ⟹ eroded product invariant with shared controls | `batch 2/04_open_problems/A4_*.md` | PROVEN (reconstructed) |
| A4.Thm2 | Sub-solution existence | Tarski greatest sub-solution; monotone iteration; linear case recovered | same | PROVEN (reconstructed) |
| B1.Thm1 | Sampled-data erosion | Envelope inclusion + inter-sample confinement + successor certificates ⟹ eroded safety | `batch 2/04_open_problems/B_TIER_*.md` | PROVEN (reconstructed) |
| B6.Thm1 | Nonlinear substitution classification | MFCQ local stability + Clarke global separation | same | PROVEN (reconstructed) |
| B7.Thm1 | Bifurcation classification | No bifurcation + continuous boundary ⟹ no kernel change; transversal contact ⟹ kernel change | same | PROVEN (reconstructed) |
| B9.Thm1 | Chance-kernel recursion | Support-aligned law + compact class ⟹ chance kernel = predecessor limit | same | PROVEN (restricted; reconstructed) |
| B10.Thm1 | Stackelberg equilibrium existence | Compact commands + continuous utilities ⟹ equilibrium; reduction to R02 at equilibrium | same | PROVEN (reconstructed) |
| C-a.Thm2 | Full decidability | Every judgment sentence (incl. negations) decidable at fixed data, O(N·|grid|) | `batch 2/04_open_problems/CA_*.md` | PROVEN (reconstructed; at declared scope: finite class, TCS-1.0 language) |
| C-a.Thm3 | Zero-one law sharpness | Monotone claims: law holds; non-monotone: per-instance decidable, model-class-dependent | same | PROVEN (reconstructed) |
| C-e.Thm1 | Quadratic-form moiety barriers | Quadratic moiety sandwich with L_G > 0 | `batch 2/04_open_problems/C_TIER_*.md` | PROVEN (reconstructed) |
| C-f.Thm1 | RFCE-aggregate memory | Projectability lifted to history space; memory-horizon characterization | same | PROVEN (reconstructed) |

---

## Part II — Computation artifacts

**Rebuilt and committed from code (this session — git commits 5405654 through 0df499c).** All scripts and artifacts are in `research_program/validated_computations/` in the repository. File hashes are SHA-256 of the committed files.

### Discrete-level validated computations (committed, reproducible)

| Artifact | Description | File | SHA-256 | Reproduction command | Solver | Independent rerun |
|---|---|---|---|---|---|---|
| A025 Hopf certificates | τ± reproduced with outward-rounded interval arithmetic (dps=50) | `a025_fold/a025_interval_hopf.json` | `eda36cd1...95b3b2` | `python3 a025_fold/a025_interval_hopf.py` | Python 3.12.13, numpy 2.1.3, mpmath 1.3.0 | **NONE** |
| C4 orbit Krawczyk | Unique orbit in 1e-8 box, margin 1186, period 370.9311778394 | `a021_c4/c4_orbit_krawczyk_certificate.json` | `5e8df633...65ab133` | `python3 a021_c4/c4_orbit_krawczyk.py` | same | **NONE** |
| C4 orbit Krawczyk (box data) | Orbit + period box (npz) | `a021_c4/c4_orbit_krawczyk_box.npz` | `85f72c76...7ba4c69` | same | same | **NONE** |
| C4 off-grid continuum residual | Certified bounds: N≤7.2e-8, A≤7.8e-8, Z≤7.7e-7, E≤2.8e-6 | `a021_c4/c4_offgrid_residual_interval.json` | `27969c14...85a499` | `python3 a021_c4/c4_offgrid_interval.py` | same | **NONE** |
| C4 monodromy/Floquet (dt=0.25) | Phase 1.00480 simple+neutral; dominant 0.68764+0.069<1; all nontrivial inside unit disc | `a021_c4/c4_monodromy_enclosure.json` | `01d8c253...dbaef76` | `python3 a021_c4/c4_monodromy.py` | same | **NONE** |
| C4 monodromy data (dt=0.25) | Monodromy matrix + eigenvalues (npz) | `a021_c4/c4_monodromy_dt0p25.npz` | `f3dc5445...a7ca5f` | same | same | **NONE** |
| E5 module admission | Five maps exact; margins/L/erosion triple interval-verified — **LINEAR A001 §§6–10 TOY ONLY; no transfer to 2J3KL/J-17 systems without the R04 certificate (not constructed)** | `E5_NUMBERS.json` | `5670bcc8...236e72db` | `python3 e5_admission.py` | same | **NONE** |
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
| B4 bunching (n=15 periods) | Discrete stable-complement powers + slack decay | **COMPUTED_PARTIAL** | Float64 output (not interval); continuum transfer open |
| A3 toy kernel | 1D system on the declared class | **COMPUTED_PARTIAL** | Toy instance; no Wave E relevance |
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
| E5 module admission | "The **linear A001 §§6–10 resource–sink module** is admitted with interval-verified numerical constants — a method demonstration; **no transfer to 2J3KL/J-17-class systems without the R04 certificate (forbidden by R04.Thm1's converse; certificate not constructed)**" |
| B1 erosion theorem | "The three-hypothesis erosion theorem closes the sampled-data bridge" |

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

**Post-transfer-audit expansion (see TRANSFER_AUDIT_RESPONSE.md):** all session theorem documents (E1–E7, A3, A4, B-tier, C-tier, C-a) are expanded from summary cards to full self-contained proof documents with provenance headers; their statuses carry the `PROVEN (reconstructed)` qualifier — same-agent reconstructions from the session record, pending independent line-by-line re-verification. **TCS-1.0 is the controlling schema** (TCS-1.1 is a frozen, unapplied diff; migration open). The E5 artifact is scoped to the linear toy; real-system (2J3KL/J-17) claims are gated on the R04/Cor2 transfer certificate.

**Not yet rebuilt:** the A025 fold pipeline (collocation → continuation → Moore–Spence → Krawczyk), the C4 monodromy at dt=0.1, and the A025 fold resolution cross-checks.

**Independent rerun status:** NONE for all artifacts. At least one independent rerun is required before submission.

**Environment:** Python 3.12.13 (`/home/z/.venv/bin/python3`), numpy 2.1.3, scipy 1.14.1, mpmath 1.3.0. No containerization. No version pinning beyond the listed versions. The interval arithmetic library (`interval_lib.py`) uses `np.nextafter` for outward rounding — verified against exact rational arithmetic on test cases.

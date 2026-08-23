# Master Mathematical Closure Review — General Theory of Sustainability

**Packet:** `general_theory_math_closure_packet` (self-contained, per `14_SELF_CONTAINMENT_REPORT.md`)
**Controlling objects:** `TCS-1.0` (`control/01_canonical_system_schema_TCS_1_0.md`), corrected theorem records (`corrected_theorems/01`–`09`), immutable A001/A002 sources (`sources/`), docket `11_OPEN_THEOREM_DOCKET.md` (targets T1–T9), output schema `12_REQUIRED_OUTPUT_SCHEMA.md`.
**Reviewer role:** per `10_MASTER_REVIEW_PROMPT.md` (senior mathematician spanning viability theory, differential inclusions, hybrid/RFDE systems, robust control, set-valued analysis, aggregation, stochastic viability, compositional systems).
**Result-record files:** `01_result_records/R01`–`R09`, one per docket target, each in the required 17-field schema. This document carries: the schema audit (§1), the theorem dependency graph (§2), the verdict table (§3), the universal/model-class separation (§4), the source-unity vs. publication-dependence audit (§5), the minimum new-theorem set (§6), and the dependency-ordered research plan (§7).
**Status discipline:** every claim below carries either a packet-internal proof/anchor (file + label/line), a complete proof in a result record, or an explicit open/conditional flag. No external bibliographic verification was available in the packet; all novelty fields are correspondingly qualified (`14_SELF_CONTAINMENT_REPORT.md`: "novelty adjudication and exact bibliographic theorem-number verification still require the cited publications").

---

## 1. Audit of the canonical schema TCS-1.0 (docket task 1)

The audit examines `control/01_canonical_system_schema_TCS_1_0.md` (with its JSON freeze) for missing types, incompatible quantifiers, and hidden circularity. Findings are graded: **[GAP]** missing type/field, **[QF]** quantifier conflict needing a guard, **[CIRC]** circularity risk needing an explicit acyclicity declaration. Each finding ends with the minimal repair; none requires abandoning the frozen schema — all are additive and belong in a `TCS-1.1` migration as foreseen by §10 of the schema.

### 1.1 Missing types

**[GAP-1] Generation/specification-change index is not a typed object.**
`TCS-1.0` §1 states that changing a threshold, authority, population, horizon, information pattern, or action class changes `Ω`, but the schema has no type for a *declared sequence* `(Ω_g)_{g∈G}` of specifications with transition maps between the corresponding admissible sets and architectures. Target T7 (intergenerational continuation) cannot even be *stated* inside the current type system without smuggling the generation structure through an ad-hoc construction. A001 §14 (Definition 14.1, `sources/A001_topdown_source.txt` line 1752) already uses generation-indexed constraint sets `𝒱^{(k)}` — this exists in a source but not in the canonical types. **Repair:** add a `specification_path` type: a locally finite index set `G`, a map `g ↦ Ω_g`, and per-transition typed translation maps (state, identity/liability/obligation, harm). Record R07 instantiates exactly this and can serve as the migration template.

**[GAP-2] Forward-completeness / confinement certificate is not a typed field.**
The theorem-record schema §6 (Θ) lists `premises` and `horizon` but has no dedicated field for the forward-completeness or compact-confinement certificate. Yet the controlling corrected theorems *demand* it: the strong-invariance theorem (corrected `02`, assumption 2), the restricted composition theorem (corrected `03`, assumption 4), and the finite/infinite-horizon non-implication (corrected `01`, non-implication 8: "Finite-horizon viability does not imply infinite-horizon viability without a closure/compactness argument"). The compactness lemma proved in record R03.2 shows the field is load-bearing, not cosmetic. **Repair:** add `confinement_certificate` to Θ with values {`forward_complete`, `compact_enclosure(K̂)`, `none`} and require it non-`none` for any infinite-horizon claim.

**[GAP-3] Erosion/error budget triple is not a first-class typed object.**
Mapping type 5 (`APPROXIMATION`) of §7 requires "error, domain, horizon, and safety erosion" to be explicit, but the Θ record has no structured field for the erosion triple `(ε, r, α)` that the conditional tubular erosion lemma (corrected `02`, Lemma 2: `L_G r + Δ_ε ≤ α`) makes canonical. The required output schema (field 11) asks for it per result; the canonical record should ask for it per *mapping*. **Repair:** add an `erosion_triple` sub-record to every `APPROXIMATION` concordance row: `(error_budget Δ_ε, erosion depth r, boundary margin α, Lipschitz gain L_G, tubular radius ρ)`, with the feasibility condition `L_G r + Δ_ε ≤ α` recorded as a checkable contract. Records R03 and R05 both populate this structure.

**[GAP-4] Observation kernel typing (deterministic set-valued vs. stochastic) is under-specified.**
§2.3 declares `𝖮_q` as "observation map/kernel" without separating (i) deterministic set-valued observations `Y = O(x)` (used by the epistemic-viability chain, corrected `01` §Epistemic viability via `Compat(b)`), (ii) stochastic observation kernels (required by chance viability, §4.6, which needs an "explicit law and filtration"). The two are different types with different fibre semantics; conflating them is precisely the type error the schema elsewhere prohibits. **Repair:** type `𝖮_q` as a tagged union `{deterministic_setvalued | stochastic_kernel(filtration-aligned)}`; require the chance-viability judgment to declare the stochastic branch with its filtration and the support condition of Proposition 8 (corrected `01`).

**[GAP-5] Cumulative-harm/obligation block has no declared transition semantics at architecture resets.**
§2.1 lists `h` (cumulative harm, obligation, accounting states) as a state block, and Operator II (§5) requires "cumulative identity/liability/harm constraints" in the transition-safe sets — but no typed rule says how `h` translates across an architecture reset (additive accrual? capped carry-over? forgiveness event?). R07 (§2, obligation translation) shows the choice is mathematically decisive: monotone accrual with a harm floor yields a finite support horizon (R07 Corollary 3), whereas forgiveness resets change the judgment entirely. **Repair:** declare `h`-translation as part of the Operator II reset data `R_{qe}`, with named variants {`accumulate`, `cap`, `forgive`}.

### 1.2 Incompatible quantifiers needing guards

**[QF-1] The canonical judgments in §4 do not bind the solution concept per judgment.**
§4 defines the eight judgments "for fixed `(Ω,q,T)` and aligned classes" — the solution concept `𝔖` appears only in the hierarchy document (corrected `01`, signature `Ξ`). Since the same `Ω,q,T` can admit ODE, Filippov, and RFDE solution concepts with *different* solution sets, two records could disagree while claiming the same judgment. The hierarchy's guard ("Empty solution sets never make a safety statement true") is controlling but lives outside the frozen schema. **Repair (TCS-1.1):** bind `𝔖` into every judgment record; import the empty-solution guard as an axiom-level clause of causal admissibility.

**[QF-2] Chance viability lacks a support-alignment clause in the schema.**
§4.6 defines chance viability "under an explicit law and filtration" but does not require the declared law's support to be related to the robust disturbance class. Proposition 8 (corrected `01`) is exactly the missing guard: robust-to-chance implication holds only "if the stochastic law is supported on the robust disturbance class", and "no implication is available when the stochastic support exceeds the robust class". **Repair:** add to §4.6: "A chance-viability record must declare `supp(law) ⊆ 𝕎` or `supp(law) ⊄ 𝕎`; only the former may cite Proposition 8." Counterexample (c) in record R08 instantiates the failure.

**[QF-3] Implementation-branch quantifier is defaultable and therefore dangerous.**
§2.3 says prescribed and realized actions are different types; the hierarchy (Proposition 7) proves that existential (some branch) and universal (every branch) implementation semantics are *not* mutually monotone: enlarging the implementation correspondence shrinks all-branches safety and enlarges some-branch safety. The schema permits an institution record without declaring which semantics it uses. **Repair:** make the branch quantifier `∀u^real ∈ 𝖨_q` vs `∃u^real ∈ 𝖨_q` a mandatory declared field of institutional viability; forbid silent switching (the flip is an axiom-4 violation when it rescues a claim).

**[QF-4] Recoverability's three quantifier levels (robust/existential/disturbance-strategic) need explicit declaration.**
§4.7 defines recoverability "robustly or existentially according to the recorded quantifiers" — acceptable as a schema, but the docket T2 acceptance and the corrected A001 audit (corrected `06` §7: Theorem 5.2's repair turns "every trajectory exits" into an adversarial-selection statement) show the mis-recorded version has already occurred in sources. **Repair:** require the disturbance quantifier pattern (pure `∀w`, adversarial nonanticipative strategy, or `∃w`) as a named field.

### 1.3 Hidden circularity checks

**[CIRC-1] Admissible-set generation from the typed registry — benign if and only if the registry is layered.**
`𝕂_{q,Ω}⊂𝖹_q` is "generated from the typed registry" including epistemic conditions (§2.5). Since the information state `b` is itself a state block (§2.1), an epistemic constraint inside `𝕂` constrains the *estimate*, not the plant — a physical viability judgment computed against such a `𝕂` would silently reward optimistic filters (smaller compatible sets make epistemic constraints easier). No circularity arises if physical and epistemic constraint blocks are kept as separately typed generators of `𝕂`; the danger is only in an unlayered registry. **Verdict: no circularity in the corrected hierarchy (physical/epistemic judgments live on different spaces with typed maps, corrected `01`), but the schema must state the layering.** Repair: declare `𝕂_{q,Ω} = 𝕂^{phys} ∩ π^{-1}_{info}(𝕂^{epi})` with the two generators separately typed, and forbid physical judgments from citing `𝕂^{epi}` blocks.

**[CIRC-2] Composition gate refers to an open class of theorems — bounded, not circular, but currently ill-typed.**
§5 admits composition "after … an applicable invariance/small-gain theorem" — a gate whose content depends on which theorems exist. This is status discipline, not circularity, but as written the gate is uncheckable because the admissible theorem list is not enumerated. **Repair:** enumerate the controlling records: (i) the corrected restricted proximal-normal composition theorem (`03`); (ii) *new:* the tubular assume–guarantee theorem of record R05 (this review); (iii) explicitly excluded until proved: nonlinear small-gain with nonconvex implementation, variable-event hybrid composition. Composition citing anything else is `UNRESOLVED`.

**[CIRC-3] Implementation map must be declared non-strategically.**
`𝖨_q` maps prescriptions to realized actions. If `𝖨_q`'s declaration were allowed to depend on the policy class `𝖯_q` (e.g., compliance responses tailored to the specific policy), then institutional viability `∃π ∀u^real ∈ 𝖨(π,·)` would be a fixed-point condition across the declaration boundary — a genuine circularity. §2.3 does not forbid it. **Repair:** require `𝖨_q` declared before and independently of `𝖯_q`; strategic compliance (𝖨 responding to the policy) must be re-typed as a game model class with equilibrium solution concept, outside the present judgment family. This matches the master prompt's non-negotiable rule "One causal policy must be distinguished from disturbance-observing controls" and extends it to the implementation side.

**[CIRC-4] Operator II's "admits the proved … predecessor construction" — sound, keep.**
The gate references a specific proved record (corrected `04`), so no circularity; R01 adds the missing converse (what the theorem would silently certify if tubes were replaced by endpoints — nothing, provably).

**[CIRC-5] Status monotonicity vs. theorem-record promotion — already guarded.**
Axiom 5 (status monotonicity) plus the concordance requirement blocks the classic circularity in which an integrated narrative promotes a conditional source claim to `proved` because a neighbouring corrected theorem "covers" it. The master prompt's rule "Do not strengthen a source claim by proximity to a corrected theorem" is enforced by the schema; no change needed.

### 1.4 Audit verdict

`TCS-1.0` is structurally sound: no destructive circularity, and the mapping vocabulary (§7) is adequate for every bridge examined in this review. The five gaps and four quantifier guards are all additive; the recommended `TCS-1.1` diff is: `specification_path` type (GAP-1), `confinement_certificate` field (GAP-2), `erosion_triple` field (GAP-3), tagged observation types (GAP-4), `h`-translation variants (GAP-5), per-judgment `𝔖` binding (QF-1), chance-support clause (QF-2), mandatory implementation-branch quantifier (QF-3), recoverability quantifier pattern (QF-4), registry layering (CIRC-1), enumerated composition gate (CIRC-2), non-strategic `𝖨` declaration (CIRC-3). Every result record below is written so as to be valid under both `TCS-1.0` and the proposed `TCS-1.1`; where a record *uses* a proposed new type (R07's specification path, R03/R05's erosion triples), this is stated in its field 16 (remaining obligations).

---

## 2. Theorem dependency graph for the open docket (docket task 2)

Proved bases on which the docket targets rest (all packet-internal):

- **B1** — Strong invariance + conditional tubular erosion (corrected `02`).
- **B2** — Restricted proximal-normal composition (corrected `03`).
- **B3** — Finite-architecture exact-tube Operator II recursion (corrected `04`).
- **B4** — Sampled/RFDE/hybrid kernel chain, information-state kernel, sample-and-hold comparison (corrected `08`; A002 `thm:sampled-viability`–`thm:sampled-limit`).
- **B5** — Projectability criterion, fibre obstruction, spatial aggregation identity, support-saturated reduction, local-horizon bracket, Halanay small-gain (corrected `09`; A002 `thm:projectability`, `thm:coarse-graining`, `thm:horizon`, `thm:small-gain`).
- **B6** — Conservation, moiety positivity, noncompensation, Farkas substitution, observation fibres (corrected `07`; A002 `thm:conservation`, `thm:farkas`, `thm:observation`).
- **B7** — Operator I judgment hierarchy, Propositions 1–8, non-implications (corrected `01`).
- **B8** — A001 selected Operator I audit: recovery idempotence, common-action obstruction, delayed-information obstruction, adversarial exit (corrected `06`).

```text
                    B7 hierarchy ─────────────┐
                    B8 obstructions ──────────┤
                    B4 sampled kernels ───────┼──>  T2 closed-loop bridge (R02)  ──┬──> institutional
                              ^                │                                    │    operationalization
                              │                └──>  T8 typed hierarchy maps (R08) ┘    (Wave 3, empirical)
        B1 erosion ───────────┼──>  T3 viability-diagnostic bridge (R03) ──> empirical falsification
              ^               │                │                                      design (Paper 5)
              │               │                └──>  T4 domain admission (R04) ──> domain classification
        B2 composition ───────┼──>  T5 restricted assume-guarantee (R05) ──┬──> T6 aggregation (R06)
              ^               │                                           │      └─> spatial/stage (A023)
              │               │                                           └─> nonlinear small-gain [OPEN]
        B5 projectability ────┤
              │               └──>  T6 aggregation & memory (R06)
              │
        B3 Operator II ──────────>  T1 transformation false positives (R01) ──> Paper 1 gate
              │
              └──────────────────>  T7 intergenerational recursion (R07) ──> obligations/architecture change

        B6 conservation+noncompensation ──>  T9 boundary theorem (R09)  <── consumes: B5,B7, R01,R03,R05,R06
                                             (synthesis; needs all U-part and M-part witnesses)
```

Adjacency (edge = "unblocks" / "is prerequisite for"):

| From | To | Edge content |
|---|---|---|
| B7, B8, B4 | **T2** | judgment quantifiers; common-action obstruction; exact/conservative filter pattern |
| T2 | T8 | lift/projection typed maps instantiated on the bridge's information states |
| B1, B8, B5 | **T3** | erosion lemma; adversarial-exit; local-horizon bracket (band-necessity) |
| B5, T2 | **T4** | projectability for reduction claims; policy/information map typing |
| B1, B2 | **T5** | erosion machinery; joint-feasibility pattern |
| B5, B1, T5 | **T6** | fibre criterion; erosion conversion for approximate closure; scale composition |
| B3, B6 | **T7** | reset/translation semantics; obligation typing |
| B3 | **T1** | exact-tube predecessor is the object whose endpoint-only weakening is refuted |
| B6, B7, B5 + R01, R03, R05, R06 | **T9** | universal-part witnesses; model-class counterexample pairs |

Critical path (longest prerequisite chain): **B1 → T3 → T9** and **B4 → T2 → T8**. The synthesis target T9 is a sink: it can only be closed after the M-part witnesses exist, which is why this review proves them first (R01, R03, R05, R06) and closes T9 last (R09).

---

## 3. Verdict table for the docket targets (docket task 3)

Legend: verdicts as demanded by the master prompt (`already proved` / `repairable` / `false` / `classical but useful` / `genuinely new`), possibly compound. "Record" points to the full 17-field result file.

| Target | Verdict | Basis | Record |
|---|---|---|---|
| **T1** typed transformation beyond reachability | **classical but useful + genuinely new (negative results)**: the exact-tube backward recursion is standard robust dynamic programming (packet's own novelty gate says the same, `control/03` §2A.4); the endpoint-only and aggregate transformation tests are now *provably unsound* (new false-positive theorems with a sharp characterization: endpoint tests are sound only in the degenerate automatically-invariant case) | B3 + R01 new proofs | R01 |
| **T2** observation–assessment–implementation bridge | **repairable → proved** (this review, at the sampled exact/conservative-filter level): one closed-loop theorem with exact quantifiers covering measured/hidden disturbance, exact/conservative filter, prescribed/realized action, latency/held commands, all-branches implementation; common-action counterexample retained; conservative filter proved sound but incomplete | B4, B7, B8 | R02 |
| **T3** viability–diagnostic bridge | **repairable → proved (assembled)**: certificate trichotomy (outer soundness via adversarial exit; inner certificate via erosion conversion; otherwise descriptive); compactness closure of finite→infinite horizon; counterexamples: rate-band necessity (stock-to-rate margin fails by factor >4), aggregate margin is not a kernel | B1, B8, B5 | R03 |
| **T4** domain admission and projectability | **proved at the structural level**: exact-admission certificate theorem (necessary and sufficient map quintuple) + classification of groundwater/phosphorus/fisheries from the included sources with missing-field flags exactly matching the live error register; empirical calibration explicitly out of scope | B5, T2 | R04 |
| **T5** composition beyond the first restricted theorem | **partially closed (new restricted theorems) + genuinely open remainder**: tubular assume–guarantee theorem with contract amplitude (Version A) and state-dependent contract tightening with a true linear gain operator and feasibility fixed point (Version B); counterexample: gain loop collapses the joint kernel to {0}; general nonlinear small-gain with nonconvex implementation stated precisely with all missing hypotheses, left open | B1, B2 | R05 |
| **T6** cross-scale aggregation and dynamic closure | **already proved at scoped level + genuinely new negative result**: exact characterization = projectability criterion (classical in substance, packet-proved); *new:* finite moment-closure impossibility for nonlinear (quadratic) field dynamics — no finite family of moments closes exactly, so exact coarse variables are necessarily memory-bearing; approximate closure carries O(κ)/variance defect with erosion conversion | B5, B1 | R06 |
| **T7** intergenerational continuation | **repairable → proved** (set level): generation-indexed recursion separating fixed-specification viability from specification change; alternating-disjoint impossibility (continuous evolution cannot cross disjoint specifications — typed resets are necessary and sufficient rescue); nested-compact existence; monotone-obligation finite-horizon corollary; A001 Thm 14.2 impossibility retained | B3, B6 | R07 |
| **T8** robust–epistemic–chance hierarchy | **classical but useful (propositions) + new completion**: typed lift/projection maps formalized; five converse counterexamples (controlled⇏robust; chance-p⇏robust; support-mismatch; epistemic emptiness with nonempty physical kernel; implementation-branch monotonicity reversal) | B7, B8 | R08 |
| **T9** general-theory boundary theorem | **proved (new as a stated theorem)**: Part U — the exact list of universal consequences of the structural axioms (conditional conservation, monotonicity calculus, noncompensation-in-domain, status/interface axioms); Part M — six independence results: for each of delay effect, substitution, dynamic aggregation closure, diagnostic causality, local-bifurcation/global-safety, and information monotonicity, two axiom-consistent instantiations with opposite truth values | B5, B6, B7 + R01, R03, R05, R06 | R09 |

No docket target received the verdict `false` as a whole; the `false` verdicts apply to specific *claims inside* targets (endpoint-only tests: false as soundness claims — R01; universal delay law, universal substitution, universal dynamic aggregation, universal diagnostic causality: false as axiom-level theorems — R09 Part M; general metric erosion for arbitrary closed sets: already rejected in corrected `02`).

---

*(Continued in §4–§7 below.)*

---

## 4. Universal axioms versus model-class mechanisms (docket task 6)

The separation below is the load-bearing discipline for the phrase "general theory": the left column is what the typed axioms *force* in every admitted instantiation; the right column is what remains a mechanism of a model class, with the paired witnesses that prove non-universality (full statements and proofs in R09).

### 4.1 Universal consequences of the structural axioms (Part U of R09)

| # | Universal statement | Status / proof anchor |
|---|---|---|
| U1 | **Conservation is conditional on declared closure and moiety:** for any declared boundary and moiety vector in the left kernel of every active internal/jump matrix, the telescoping identity `Lᵀx(t) − Lᵀx(0) = ∫ LᵀBφ ds + Σ LᵀB^J β_j` holds for every locally finite execution | proved, A002 `thm:conservation` (accepted with the φ-notation correction, corrected `07`); re-proved from the axioms in R09 §U.1 |
| U2 | **Viability is set-, quantifier-, and class-conditional:** the monotonicity calculus (Robust ⊆ Controlled; fixed-policy ⊆ Robust; action expansion enlarges; disturbance expansion shrinks; safe-set expansion enlarges) holds in every aligned instantiation | proved, corrected `01` Props 1–5; R09 §U.2 |
| U3 | **Noncompensation is conditional on declared binding components:** outside a domain with a proved scalar certificate, componentwise failure is not erased; on the restricted linear domain, feasibility is exactly Farkas-separated (pathway-specific certificate, never an exchange rate) | proved, A002 domain-qualified noncompensation + `thm:farkas` (accepted, corrected `07`); R09 §U.3 |
| U4 | **Status monotonicity and interface explicitness:** no integration step strengthens a proof/evidence status; no cross-module transfer without an admitted mapping + contract | axioms 5–6 of `TCS-1.0` §9 (definitional); R09 §U.4 |
| U5 | **Exact kernel recursions equal their judgments under stated hypotheses:** sampled robust kernel, held-tube kernel, information-state kernel characterize their judgments exactly when their compactness/continuity/exactness hypotheses hold | proved, corrected `08`; R09 §U.5 |

### 4.2 Model-class-dependent mechanisms (Part M of R09) — none is a theorem of the axioms

| # | Claimed universal law | Refuting pair (both axiom-consistent) | Record |
|---|---|---|---|
| M1 | "Delay destabilizes" / "delay is harmless" | `ẋ = −2x(t) − x(t−τ)`: delay-independent exponential stability for every τ (Halanay certificate, A002 `thm:small-gain`, proved) **vs.** `ẋ = −x(t−τ)`: unstable for every τ > π/2 (explicit characteristic-root witness `x(t) = e^{λt}`, Re λ > 0, constructed in R09) | R09 §M.1 |
| M2 | "Substitution is always possible" / "never possible" | feasible linear pathway (Farkas multipliers certify an exact allocation) **vs.** infeasible pathway (strict separation certificate `γᵀs^req > αᵀx + βᵀe`) — both inside the same axiom system with different endowments | R09 §M.2 (A002 `thm:farkas` witnesses) |
| M3 | "Coarse variables close dynamically" | identical-patch spatial system: mean dynamics exactly closed on the diagonal (variance ≡ 0 invariant) **vs.** two-patch heterogeneous system: fibre obstruction — same mean, different mean-derivatives, no autonomous mean closure; strengthened by R06: no finite moment family closes for quadratic field dynamics | R09 §M.3; R06 Thm 3 |
| M4 | "Diagnostics are causal certificates" | observation-fibre criterion: safety-crossing fibres obstruct any observation-only certificate (A002 `thm:observation`, proved) **vs.** injective observation on the declared domain: exact certification; plus R03: stock-to-rate margin fails by unbounded factor without a rate-persistence band | R09 §M.4; R03 Thm 2 |
| M5 | "Local bifurcation ⇒ global safe-set change" | fold in an uncoupled coordinate leaves the viability kernel of an independent safe set unchanged (explicit 2-D witness, R09) **vs.** A018 C3/C4-class systems where the fold interacts with the constraint set (source-stated status, not promoted here) | R09 §M.5 |
| M6 | "More information/implementation is always better" | refinement monotonicity holds only through typed lift maps (corrected `01` Prop 6) **vs.** all-branches implementation enlargement shrinks safety (Prop 7 reversal; one-step witness in R08 Ex (e)) | R09 §M.6; R08 |

### 4.3 Reading of the separation

The theory's universality is exactly of the form **"conditional laws + obstruction calculus"**: conservation, viability, noncompensation, kernel recursion, and status/interface discipline are universal *as conditional statements with typed hypotheses*; every mechanism that would make the theory *predictive without a model* — delay effects, substitution elasticities, aggregation closure, diagnostic causality, bifurcation-to-collapse links — fails at least one independence witness. This is the honest content of the phrase "general theory" under TCS typing and is stated as a theorem (not a narrative) in R09.

---

## 5. Source-level unity versus publication-level dependence (docket task 7)

The master prompt requires preventing the (real) source-level unity of the corpus from becoming (unsupported) publication-level dependence. The audit against `control/05_publication_architecture.md` (federated orchestration, citation-closure rules) and the corrected records yields:

1. **The seam that had to be exact is exact.** The A018 ledger→dynamics seam is closed by an `EXACT_SPECIALIZATION` (single-resource deficit identity `D = qEN − R = −Ṅ`) plus an explicit `REJECTED_MAPPING` for the dynamic reduction (corrected `05`). Paper 3/Paper 4 dependence is therefore *contextual*, not load-bearing — the refereeability test in that record is satisfied. This review adds nothing to that seam and flags one enforcement obligation: Paper 4 must carry the open-projection accounting paragraph verbatim (corrected `05`, "Open-projection accounting").

2. **Two new load-bearing interfaces are now proved and must be cited as theorems, not narratives.** The closed-loop bridge (R02) is the first interface theorem connecting observation, filter, prescription, and implementation in one quantifier chain. Papers 1 and 5 currently *describe* this chain architecturally (`TCS-1.0` §3); after R02 they may cite a theorem, but only with its exact hypotheses (compact held-action sets, declared implementation correspondence, conservative-update soundness). The diagnostic bridge (R03) is the analogous interface for Paper 5's falsification design: margin diagnostics may be cited as outer/inner certificates only with the adversarial-exit or erosion hypotheses attached.

3. **One tempting dependence is now formally blocked.** Because endpoint-only transformation tests are unsound (R01), no paper may present an architecture transformation as safe on the basis of successor-set membership alone; and because aggregate tests are unsound under noncompensatory constraints (R01 Thm 2), no paper may certify transition safety from an aggregate/projection tube. Both prohibitions are now theorems, not editorial cautions — they belong in Paper 1's transformation section and in the monograph's composition chapter.

4. **The composition gate remains two-theorem-wide.** Until the nonlinear small-gain/open problem of R05 §Field 16 closes, cross-module safety claims may cite only the restricted proximal-normal theorem (corrected `03`) and the tubular assume–guarantee theorem (R05) — the latter only with its erosion/gain constants recorded per the `erosion_triple` field proposed in §1.1 GAP-3. Any other composition claim stays `UNRESOLVED`.

5. **Empirical and novelty dependencies are unchanged and remain external.** This packet is self-contained for the mathematics (per its own report) but not for bibliographic novelty adjudication or calibration data. Every novelty field in R01–R09 says precisely what internal evidence supports and what external check is outstanding; the research plan (§7) keeps both outside the critical path of the theorem work.

---

## 6. Minimum set of new theorems justifying "general theory" (docket task 8)

The claim "general theory of sustainability" under TCS typing is justified — without implying universal delay, substitution, aggregation, or empirical laws — by exactly the following closure set (bases B1–B8 are already proved in the packet; the numbered items are the new closures, each proved in this review):

1. **Closed-loop governance bridge (R02).** One theorem carrying the full causal chain physical state → observation → information state → prescription → realized action → trajectory with all docket distinctions enforced. *Why minimum:* without it the theory describes modules but cannot state a governance guarantee.
2. **Scope boundary theorem (R09).** The exact Part U / Part M split. *Why minimum:* it is what licenses the word "general" honestly — universal conditional laws plus proved non-universality of the predictive claims.
3. **Viability–diagnostic bridge (R03).** Soundness/completeness/descriptive trichotomy + erosion conversion + horizon closure. *Why minimum:* it connects the normative kernel language to anything empirically testable, which the docket's T3 and Paper 5 require.
4. **Domain admission certificate (R04).** Necessary-and-sufficient map quintuple + classification of the three domain modules. *Why minimum:* "general" across domains needs an admission test, not verbal analogy; the certificate is the test.
5. **Restricted assume–guarantee composition (R05) + aggregation non-closure (R06).** The positive restricted composition rule with true gain operator, and the negative moment-closure result. *Why minimum:* together they state exactly when modules compose and when scales do not close — the two honesty boundaries of any cross-scale theory.

Everything else in the docket is either already proved (bases), a refinement that does not change the claim structure (R01's false-positive theorems sharpen Operator II's necessity; R07 separates specification change; R08 completes converse counterexamples), or remains explicitly conditional (nonlinear small-gain, variable-event hybrid kernels, stochastic filter exactness, empirical calibration). **With items 1–5 proved, the phrase "general theory" is defensible; without any one of them it is not:** dropping R09 leaves "general" unbounded; dropping R02 leaves governance unhinged; dropping R03/R04 leaves the theory untestable and domain-bound; dropping R05/R06 leaves cross-scale claims unaudited.

---

## 7. Dependency-ordered research plan (closing requirement of the master prompt)

Ordering rule per `control/03_dependency_plan.md` (prerequisite depth, downstream unblocking, validity risk, feasibility, value). Waves A–C below are *complete in this review*; waves D–F are the remaining programme.

### Wave A — negative/structural closures (no unmet prerequisites; **done here**)
- A1. Endpoint-only and aggregate transformation tests: unsoundness theorems + degenerate-case characterization (**R01**). Unblocks: Paper 1 transformation-section discipline.
- A2. Hierarchy completion: typed lift/projection maps + five converse counterexamples (**R08**). Unblocks: Paper 2 hierarchy section finalization.
- A3. Boundary theorem Part M witnesses (**R09**, together with waves B–C inputs). Unblocks: monograph scope chapter.

### Wave B — positive bridge closures (prerequisites: B1, B4, B8; **done here**)
- B1*. Closed-loop observation→assessment→prescription→implementation theorem + conservative-filter soundness/incompleteness + common-action necessity (**R02**). Unblocks: institutional operationalization (wave E), Paper 5 closed-loop design.
- B2*. Diagnostic bridge: trichotomy + erosion conversion + compactness horizon closure + rate-band and aggregate-margin counterexamples (**R03**). Unblocks: falsification design, T4's diagnostic fields.

### Wave C — composition, scale, generation (prerequisites: B1, B2, B3, B5; **done here**)
- C1*. Tubular assume–guarantee theorem, Versions A and B, with linear gain feasibility + collapse counterexample (**R05**). Unblocks: T6, A023 spatial branch, polycentric composition docket.
- C2*. Moment-closure impossibility + memory-necessity + approximate-closure erosion conversion (**R06**). Unblocks: A023, cross-scale claims in the monograph.
- C3*. Generation recursion + specification-change separation + alternating-disjoint impossibility + nested-compact existence (**R07**). Unblocks: intergenerational applications, `TCS-1.1` specification-path type.
- C4*. Domain admission certificate + classification of groundwater/phosphorus/fisheries (**R04**). Unblocks: wave E case selection.

### Wave D — conditional extensions (prerequisites: waves B–C; open, precisely stated)
- D1. Nonlinear small-gain / assume–guarantee with nonconvex implementation and shared controls beyond R05's tubular class (R05 field 16: all missing hypotheses listed). Parallelizable once R05 constants are instantiated on one application pair.
- D2. Measurable/continuous selector regularity for R02's witness correspondence (currently: arbitrary selector, set-valued existence — the packet's standing selector caution, corrected `08` §1).
- D3. Stochastic filter exactness + chance-viability support alignment instances (QF-2 guard; needs a declared law).
- D4. Variable-event delayed-hybrid kernel (A002 conjecture; unchanged by this review).

### Wave E — empirical instantiation (prerequisites: R02, R03, R04; external data)
- E1. Groundwater vs. phosphorus readiness comparison per `control/03` wave 3 (groundwater preferred unless the matrix fails); admission certificate instantiated per R04 with the module's open fields (error register B.5 items) closed first.
- E2. Institutional/distributive operationalization on the selected case.

### Wave F — audit and publication (prerequisites: stable theorem set; external literature)
- F1. Global novelty map: R01–R09 novelty fields are pre-populated with internal evidence and outstanding external checks; the audit must verify each against robust DP/reachability, viability, hybrid-systems, small-gain, and moment-closure literatures.
- F2. Paper-1 independent-result gate: R01 + R05 give the false-positive/negative and restricted-positive content that the gate sought beyond the standard recursion; decision on sufficiency is editorial, after F1.
- F3. Per-paper artifact manifests, `TCS-1.1` migration (§1.4 diff), drafting per `control/05`.

**Parallelism:** A1–A3 and B1*–B2* are independent of C1*–C4*; within C, C1*–C4* are independent. D1–D4 run in parallel after C. E requires B* and C4* only. F1 can start as soon as any wave-B/C record stabilizes. **Explicitly conditional forever (never silently promoted):** D1 in full generality, D4, empirical calibration claims, and any bibliographic novelty claim before F1.

---

## 8. What was checked, what was proved, what remains open — one-paragraph summary

The packet's controlling objects were audited (§1): TCS-1.0 is sound with five additive gaps and four quantifier guards proposed for TCS-1.1. The dependency graph for T1–T9 was built (§2) and every target received a verdict with a full 17-field record (§3, files R01–R09): the exact-tube Operator II recursion is classical, and its endpoint-only and aggregate weakenings are now provably unsound (R01); the observation–assessment–prescription–implementation bridge is proved as one closed-loop theorem with exact quantifiers and a common-action necessity counterexample, including the sound-but-incomplete conservative-filter calculus (R02); the viability–diagnostic bridge is proved as a certificate trichotomy with erosion conversion, horizon closure, and two necessity counterexamples (R03); domain admission is a necessary-and-sufficient certificate theorem that classifies the three included domain modules without verbal analogy (R04); composition gains a genuine restricted assume–guarantee theorem with a linear gain operator and feasibility fixed point, with the general nonlinear small-gain problem stated precisely and left open (R05); aggregation is exactly characterized by projectability, and finite moment closure is proved impossible for quadratic field dynamics, making memory-bearing closure a theorem rather than a slogan (R06); intergenerational continuation is a generation-indexed recursion separating fixed specification from specification change, with the disjoint-alternation impossibility proving typed resets necessary (R07); the judgment hierarchy is completed by typed comparison maps and five converse counterexamples (R08); and the general-theory boundary theorem states exactly which claims are universal consequences of the typed axioms and proves six independence results for the predictive claims that are not (R09). The minimum closure set justifying "general theory" is identified (§6) and the remaining programme is dependency-ordered (§7), with novelty fields honestly limited to internal evidence pending external literature access.

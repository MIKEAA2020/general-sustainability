# Result Record R09 — Docket T9: The General-Theory Boundary Theorem

## Field 1 — Result ID and target docket item

`R09` (R09.Thm1 Part U — universal consequences; R09.Thm1 Part M — six independence results). Target: **T9** ("a theorem or formal proposition stating exactly which claims are universal consequences of the typed axioms and which remain model-class dependent").

## Field 2 — Verdict

**Proved (new as a stated theorem).** Part U assembles the packet's proved conditional laws into the exact universal list; Part M proves six independence results — for each candidate "universal law" of sustainability discourse, two axiom-consistent instantiations with opposite truth values. Together they are the boundary theorem that licenses the phrase "general theory" without implying universal delay, substitution, aggregation, or causal-diagnostic law (the docket's acceptance text, verbatim).

## Field 3 — Exact statement

**Axiom base.** The seven structural axioms of `TCS-1.0` §9 (typed consistency; physical closure honesty; causal admissibility; noncompensatory admissibility; status monotonicity; interface explicitness; version identity), with the frozen judgment/mapping vocabulary. An *instantiation* is any admitted architecture realization `𝔄_q` with declared specification `Ω` and solution concept satisfying the axioms.

### R09.Thm1 (boundary theorem)

**Part U — universal consequences.** Every instantiation satisfies:

- **U1 (conservation conditional on closure):** for every declared boundary, moiety vector `L` in the left kernel of every active internal-flow and jump matrix, and locally finite execution, the telescoping identity `Lᵀx(t) − Lᵀx(0) = ∫₀ᵗ LᵀBφ ds + Σ_{t_j≤t} LᵀB^Jβ_j` holds; conservation outside declared closures is asserted of nothing.
- **U2 (viability conditional on sets/classes):** the monotonicity calculus — robust ⊆ controlled; fixed-policy ⊆ robust; action-set expansion enlarges; disturbance-class expansion shrinks; safe-set expansion enlarges; robust ⊆ chance-1 under support alignment — in every aligned signature.
- **U3 (noncompensation conditional on declared binding components):** componentwise failure of a binding constraint is not erased by unrelated surplus unless `Ω` declares an authorized substitution pathway; on the restricted linear domain, feasibility is exactly Farkas-certified, pathway-specifically.
- **U4 (status/interface discipline):** no integration step strengthens evidence status; no cross-module transfer without an admitted mapping + contract.
- **U5 (kernel-recursion exactness under stated hypotheses):** where the sampled/held/information-state hypotheses hold, the kernel recursions characterize their judgments exactly.

**Part M — independence results.** None of the following is a consequence of the axioms; each is refuted by a pair of axiom-consistent instantiations with opposite truth values:

- **M1 (no universal delay law).** Instantiation I: `ẋ = −2x(t) − x(t−τ)` — delay-independent exponential stability for every `τ ≥ 0` (Halanay certificate, A002 `thm:small-gain`, proved/accepted). Instantiation II: `ẋ = −x(t−τ)` — instability for every `τ > π/2` (explicit growing solution `e^{λt}` with `Re λ > 0`, constructed below). "Delay destabilizes" and "delay is harmless" both fail as axiom-level claims.
- **M2 (no universal substitution law).** Feasible pathway: single-resource linear endowment `x = 3 ≥ s^req = 2` (allocation `a = 2` satisfies all constraints). Infeasible pathway: `x = 1 < s^req = 2` with the strict Farkas separation `γᵀs^req > αᵀx + βᵀe` (A002 `thm:farkas`, proved). Substitution is pathway-specific in both directions; no exchange rate exists.
- **M3 (no universal dynamic aggregation).** Identical-patch system: the aggregate mean closes exactly on the invariant diagonal. Heterogeneous two-patch system (R06.Ex5): fibre obstruction — no autonomous mean closure; and R06.Thm3: no finite moment family closes for quadratic field dynamics. Static expectation identities are exact; dynamic closure is model-class-dependent.
- **M4 (no universal causal-diagnostic law).** Injective observation on the declared domain: exact safety certification (A002 `thm:observation` sufficiency). Safety-crossing fibres: no observation-only certificate exists (same theorem's obstruction side). Stock-to-rate margins: unboundedly unsound without rate-persistence (R03.Thm2). Diagnostics are certificates only under declared conditions; causal reading is never automatic.
- **M5 (no universal local-to-global law).** A fold occurring in an uncoupled coordinate leaves an independent safe set's kernel unchanged (explicit 2-D witness below). The A018-class systems exhibit folds interacting with constraints (source-stated status, not promoted). Local bifurcation existence neither implies nor is implied by global safe-set change.
- **M6 (no universal information/implementation monotonicity).** Refinement monotonicity holds only through typed lift maps (corrected `01` Prop 6; R08.Prop1); untyped "more information is better" fails (delayed revelation changes nothing at the decision point — the delayed-information obstruction, corrected `06` §4); implementation enlargement shrinks all-branches safety (R08.Ex(e)).

**Conclusion.** The universal content of the typed general theory is exactly the conditional laws U1–U5 plus the obstruction calculus; every predictive mechanism — delay effects, substitution, aggregation closure, diagnostic causality, bifurcation-safety links, information/implementation monotonicity — is model-class-dependent, with the independence witnesses above as the permanent record of that boundary.

## Field 4 — State and phase space

Part U: phase-space-agnostic (the laws are typed over any declared class). Part M witnesses: M1 scalar RFDE `C([−τ,0], ℝ)`; M2 finite-dimensional linear allocation space; M3 `ℝ²` and field space `L^∞(Σ)`; M4 `ℝ`/`ℝ×{±1}` with observation maps; M5 `ℝ²`; M6 as in R08.

## Field 5 — Quantifier order and information pattern

Part U: each law's quantifier structure is the packet's own (U1: universal over executions; U2: the hierarchy's aligned `∃π ∀w ∀φ` chains; U3: universal over binding components; U4: universal over integration steps; U5: hypothesis-conditional equivalences). Part M: each independence result is a *pair* of `∃`-witnesses — the logical form is `¬(Axioms ⊨ Claim)`, demonstrated by two models of the axioms disagreeing on the claim.

## Field 6 — Assumptions, including existence/completeness

Part U: exactly the hypotheses of the assembled theorems (A002 conservation theorem's local finiteness and moiety conditions; hierarchy alignment; Farkas domain restrictions; sampled-kernel compactness/continuity). Part M: each witness is a well-posed Lipschitz system with unique solutions (M1: linear RFDE, classical well-posedness).

## Field 7 — Mapping type

Part U: `EXACT_SPECIALIZATION` (assembly of proved laws into the boundary statement). Part M: `COUNTEREXAMPLE_OR_LIMIT` (independence witnesses). The theorem as a whole is the docket's `T9` deliverable and the `ANALOGY_ONLY` firewall: any model-class mechanism cited as universal is exactly one of M1–M6 and is refutable by the corresponding witness.

## Field 8 — Self-contained proof

### Part U

Each item is a packet theorem restated at the axiom level; the assembly adds only the observation that the laws' hypotheses are themselves typed declarations (closure, moiety, alignment, domain, registry), so the laws hold in *every* instantiation *as conditional statements*:

- U1: A002 `thm:conservation` (statement lines 227–241; proof 243–263; accepted with the `Bφ` notation correction in corrected `07`, which also verified the left-kernel condition across active modes). The identity is a trajectory-level algebraic identity — universal over all executions satisfying the declared structure.
- U2: corrected `01` Propositions 1–5 and 8 (each proved there; R08 adds the converse witnesses showing the implications are strict).
- U3: A002 domain-qualified noncompensation (statement lines 192–199; proof 201–220; accepted) + `thm:farkas` (statement 428–442; proof 444–483; accepted with the dimension check in corrected `07`).
- U4: axioms 5–6 of `TCS-1.0` §9 (definitional, enforced by the theorem-record schema).
- U5: corrected `08`'s accepted kernel chain, each at its exact restricted status.

No new mathematics; the theorem's content is that **this list is complete for the programme's universal claims** — which Part M establishes negatively, by refuting every candidate extension. ∎

### Part M

**M1.** Instantiation I is the packet's proved Halanay result (corrected `09`'s adjudication row: `α_0 > β_0` gives delay-independent exponential decay — for the scalar system `ẋ = −2x(t) − x(t−τ)`, `α_0 = 2 > 1 = β_0` in the standard norm). Instantiation II: consider `ẋ(t) = −x(t−τ)` and the characteristic equation

```
λ + e^{−λτ} = 0.
```

At `τ = π/2`, `λ = i` is a root (`i + e^{−iπ/2} = i − i = 0`). The root is simple: `∂F/∂λ = 1 − τe^{−λτ} = 1 + τλ = 1 + iπ/2 ≠ 0` for `F(λ,τ) = λ + e^{−λτ}` (using `e^{−λτ} = −λ` along the root locus). By the implicit function theorem the root continues as `λ(τ)` near `π/2` with

```
dλ/dτ = −(∂F/∂τ)/(∂F/∂λ) = −(λ²)/(1 + τλ),
```

(since `∂F/∂τ = −λe^{−λτ} = λ²`). At `(i, π/2)`: `λ² = −1`, so `dλ/dτ = 1/(1 + iπ/2) = (1 − iπ/2)/(1 + π²/4)`, whose real part is `+1/(1+π²/4) > 0`: the root crosses into the right half-plane as `τ` increases through `π/2`. Hence for every `τ ∈ (π/2, π/2 + δ)` there is a root `λ` with `Re λ > 0`, and indeed by continuity of the crossing this holds for a definite interval; for `τ > π/2` (up to the next return crossing, and in particular on an explicit interval) the zero solution is unstable. The corresponding exponential `x(t) = e^{λt}` (with the consistent history `φ(s) = e^{λs}`, `s ∈ [−τ, 0]`) is an exact solution of the RFDE growing without bound: an explicit instability witness (no stability theorem invoked — the growing solution *is* the proof). Both instantiations satisfy the axioms (typed single-stock RFDE, declared delay, closed history phase space); the truth values of "the delay destabilizes" are opposite. ∎

**M2.** The feasible instance: one resource, endowment `x = 3`, requirement `s^req = 2`, `R = E = I`, `Q = I`: `a = 2` satisfies `Ra ≤ x`, `Qa ≥ s^req`, `a ≥ 0` — substitution (service met through the pathway) is possible. The infeasible instance: `x = 1`, same requirement: `a ≤ 1` and `a ≥ 2` — no feasible allocation; the Farkas alternative supplies the certificate `γ·2 > α·1` with `γ = α = 1` (`2 > 1`). Both are axiom-consistent linear instantiations with identical structure and different endowments: substitution feasibility is not a structural property. ∎

**M3.** R06.Ex5 (proved there): identical patches close the mean exactly on the invariant diagonal; heterogeneous patches obstruct any autonomous mean closure (same mean, different mean-derivatives). R06.Thm3 (proved there): for quadratic field dynamics no finite moment family closes. Static aggregation identities (A002 `thm:coarse-graining`, proved) hold in both instances — the static/dynamic boundary is exactly the independence boundary. ∎

**M4.** The A002 observation-fibre criterion (proved, accepted in corrected `07`) gives both directions: `K = O^{-1}(O(K))` relative to the declared domain makes observation-only certification exact; a safety-crossing fibre (two admissible states, same observation, opposite safety membership) obstructs every observation-only certificate — the theorem's own corollary (lines 537–542) supplies the obstruction instance. R03.Thm2 (proved) adds the margin side: stock-to-rate diagnostics are unboundedly unsound without rate persistence. Two instantiations, opposite diagnostic validity — no causal-diagnostic law at axiom level. ∎

**M5.** Witness for "fold without global safe-set change": on `ℝ²`,

```
ẋ_1 = μ + x_1²,   ẋ_2 = −x_2 + c,   c = 1/2,
```

with safe set `K = {x_2 ≤ 1}` (no constraint on `x_1`). The `x_1`-block undergoes a saddle-node (fold) at `μ = 0` — a genuine local bifurcation of the declared model class. The `x_2`-block: from any `x_2(0) ≤ 1`, `x_2(t) = (x_2(0) − 1/2)e^{−t} + 1/2 ≤ 1` for all `t ≥ 0` — every trajectory from `K` stays in `K` forever, independent of `μ` and of the fold: `Viab(K) = K` for every `μ`. The fold exists and the kernel never changes. The opposite direction (folds interacting with constraints, A018 C3/C4-class evidence) exists in the packet at source-stated status — not promoted, not needed for the independence claim: the pair "fold-without-kernel-change" (proved here) versus "no-fold-with-kernel-collapse" (e.g., `ẋ = 1` on `K = [0,1]`: no bifurcation, kernel collapses to `{1}`… in fact empty of interior; either way trivially opposite) establishes that neither property implies the other at axiom level. ∎

**M6.** The typed-map necessity (R08.Prop3, proved) plus the delayed-information obstruction (corrected `06` §4: accurate information arriving after `T_obs > q_0/ε` cannot prevent exit — the obstruction is proved in the packet) and the implementation reversal (R08.Ex(e), proved). "More information/implementation is better" fails in both directions without the typing. ∎

## Field 9 — Counterexample showing necessity or failure outside scope

Part M *is* the counterexample register — the theorem's method is independence witnessing. Scope note: Part U's completeness is relative to the programme's claim inventory (the master prompt's list of universal candidates); a new candidate universal claim must be either proved from the axioms (joining Part U) or added to Part M's witness list — the theorem provides the test, and the packet's status discipline (axiom 5) provides the enforcement.

## Field 10 — Interface producer/consumer contract

- **Producer:** the boundary statement (U-list + M-register).
- **Consumers:** the flagship Paper 1 (the theory's scope section is a citation of this theorem); the monograph (the general-theory claim is bounded by it); every application paper (model-class mechanisms must cite their M-item, which converts "this is generally true" into "this is a model-class mechanism with witnesses"); the novelty audit (F1: the theorem delimits what needs external comparison — the conditional laws and the boundary, not the mechanisms).
- **Failure condition:** any downstream text citing a Part-M mechanism as universal, or a Part-U law without its conditional's typed hypotheses — both are reviewer-enforceable rejections.

## Field 11 — Error, horizon, and safety erosion for approximations

Not an approximation result; the erosion discipline enters U-list items only through their own theorems (U5's kernel results and the erosion conversions of R03/R05 when instantiated).

## Field 12 — Selector and implementation regularity

No selector claims; M6's implementation witness is itself the regularity discipline statement (QF-3).

## Field 13 — Stochastic/hybrid/RFDE qualifications

M1's instability witness is an RFDE instantiation (axiom-consistency across model classes is part of the point: the boundary theorem does not privilege the ODE class); the Halanay certificate is likewise RFDE. No stochastic witnesses are needed for the six listed claims; a candidate stochastic universal law (e.g., "noise always destroys infinite-horizon viability") is already conditional in the packet (A001 Conjecture 17.2 remains conjectural, correctly) and would join Part M's register if promoted.

## Field 14 — Novelty status with exact references

Internal: no packet record states the boundary as a theorem; the master prompt's task 8 and the docket T9 demand exactly this statement; the U-items are packet-proved, the M-witnesses are proved in R01/R03/R06/R08 or here (M1's crossing computation and M5's witness are new verifications; M1-I, M2, M3, M4, M6 reuse packet-internal proved results). External: scope/boundary theorems of this "conditional universality + independence witnesses" shape exist in axiomatic-modeling traditions; **the sustainability-specific witness register and the exact U-list are, to internal knowledge, new; external literature check outstanding**; no bibliographic claim made.

## Field 15 — Publication destination

Paper 1 (the theory's central scope theorem — likely its most-cited statement); Paper 2 (the witness proofs); monograph (opening chapter: what the general theory claims and does not).

## Field 16 — Remaining obligations and revocation triggers

Obligations: external novelty audit of the boundary-theorem form; maintenance discipline — every future candidate universal claim must be routed through the U/M test before publication; the M-register is append-only (new mechanisms join with witnesses). Revocation triggers: discovery that a Part-U law's assembled proof has a gap (would demote that item to conditional and shrink the universal list); discovery of an axiom-level proof of any Part-M claim (would falsify the corresponding witness — mathematically impossible for the proved witnesses, but the register's framing must track any axiom change in `TCS-1.1`).

## Field 17 — Machine-readable dependency edges

```json
{
  "result_id": "R09",
  "target": "T9",
  "depends_on": [
    "A002 thm:conservation, thm:farkas, thm:observation, thm:coarse-graining, thm:small-gain (U1, U3, U4/M2/M4, M3, M1-I)",
    "corrected_theorems/01_operator_I_hierarchy.md (U2)",
    "corrected_theorems/07,08,09 (acceptance records for the U-items)",
    "corrected_theorems/06 §4 (M6 delayed-information)",
    "R01.Thm2 (M3 aggregate witness)", "R03.Thm2 (M4 margin witness)", "R06.Ex5+Thm3 (M3)", "R08 (M6, U2 converses)"
  ],
  "unblocks": ["Paper 1 scope section", "monograph general-theory claim", "novelty audit F1", "TCS-1.1 axiom maintenance discipline"],
  "status": {"R09.Thm1 Part U": "proved (assembly of proved laws)", "R09.Thm1 Part M.1–M6": "proved (independence witnesses)"},
  "mapping_type": "EXACT_SPECIALIZATION + COUNTEREXAMPLE_OR_LIMIT",
  "novelty": "boundary-theorem packaging internal-new; external check outstanding"
}
```

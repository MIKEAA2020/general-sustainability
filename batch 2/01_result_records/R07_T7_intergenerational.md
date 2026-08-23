# Result Record R07 — Docket T7: Intergenerational Continuation and Specification Change

## Field 1 — Result ID and target docket item

`R07` (R07.Def1 specification path — the proposed `TCS-1.1` type; R07.Thm2 generation recursion; R07.Prop3 fixed-specification reduction; R07.Thm4 alternating-disjoint impossibility and the necessity of typed resets; R07.Thm5 nested-compact existence; R07.Cor6 monotone-obligation finite horizon). Target: **T7** ("formalize generation-indexed safe sets, changing authorities/thresholds, continuation kernels, obligations, and architecture transitions").

## Field 2 — Verdict

**Repairable → proved** (set level). The packet holds A001 §14's three results (verified below); what was missing is the typed specification-path object, the generation-indexed recursion with reset/obligation translation, the sharp impossibility showing *typed resets are necessary* (not merely convenient) for specification change, and the compactness existence complement. All proved here. No universal ethical claim is made (docket acceptance rule).

## Field 3 — Exact statement

### R07.Def1 (specification path — proposed typed object)

A **specification path** is `(G, (Ω_g)_{g∈G}, (𝕋_g)_{g∈G})` where: `G = {0, 1, 2, …}` is the generation index with decision epochs `t_g` (locally finite: `t_g → ∞`); `Ω_g` is the frozen specification in force on `[t_g, t_{g+1})`; and `𝕋_g = (τ^z_g, τ^h_g)` are **typed transition maps** at the generation boundary `t_{g+1}`: `τ^z_g` translates the phase state between architectures (`x ↦ R_g(x)`, set-valued, possibly architecture-changing — an Operator II reset), and `τ^h_g` translates the cumulative obligation/harm block with a declared variant from `{accumulate, cap, forgive}` (schema audit GAP-5). The generation-safe sets are `K_g := 𝕂_{q(g), Ω_g}`; intergenerational viability requires `x(t) ∈ K_g` for `t ∈ [t_g, t_{g+1})` along the whole path, with boundaries stitched by `τ_g`.

### R07.Thm2 (generation-indexed continuation recursion)

Under the Operator II data conventions (corrected `04` §1) applied per generation with transition maps `𝕋_g`, define

```
W_G := K_G  (terminal generation: maintenance condition, possibly an Operator I kernel)
W_g := { x ∈ K_g : ∃a ∀d :  Tube_g(x, a, d) ⊆ K_g   and   Succ_g(x, a, d) ⊆ τ_g^{-1}(W_{g+1}) }
```

(`τ_g^{-1}(W_{g+1})` = the set of phase states whose every translated successor branch lies in `W_{g+1}`). Then `W_g` is **exactly** the set of states from which a causal generation policy maintains every generation's safe set through generation `G` — the finite-horizon intergenerational continuation kernel — and the infinite-generation set is `W_∞ := ⋂_G W^{(G)}` (intersected over terminal horizons `G`, characterized by R03.Lem4's machinery under compactness).

### R07.Prop3 (fixed-specification reduction)

If `Ω_g = Ω`, `K_g = K`, and `τ_g = id` for all `g`, then intergenerational viability equals ordinary viability on the concatenated horizon (A001 Theorem 14.1, `sources/A001_topdown_source.txt` line 1754 — trivial and verified: the generation index is a relabeling of time). Specification change is therefore exactly the added content of T7.

### R07.Thm4 (alternating-disjoint impossibility; typed resets are necessary)

Let `K_{2k} = A`, `K_{2k+1} = B` with `A, B` closed and **disjoint** (`A ∩ B = ∅`), and `τ_g = id` (no reset: the state evolves continuously across the boundary). Then **no** intergenerationally viable trajectory exists, for any policy and any dynamics, regardless of generation lengths: continuity forces `x(t_{g+1}) ∈ closure(K_g) ∩ K_{g+1} = K_g ∩ K_{g+1} = ∅`. Conversely, with a typed reset `τ^z_g` whose range meets `K_{g+1}` (an architecture-changing translation), the recursion of Thm2 can be nonempty: **specification change across disjoint regimes is possible only through typed transformation, never through continuous evolution.** The necessity direction is the content: continuous dynamics cannot cross disjoint specifications — Operator II resets are not an optional modeling convenience but the only mathematical route.

### R07.Thm5 (nested-compact existence)

If the `K_g` are nested decreasing (`K_{g+1} ⊆ K_g`) compact nonempty with `⋂_g K_g ≠ ∅`, trajectories are confined to a compact enclosure, the per-generation predecessor sets are nonempty in the sense of Thm2 at every finite `G`, and the successor maps satisfy the compactness/Hausdorff-upper-semicontinuity hypotheses of R03.Lem4, then `W_∞ ≠ ∅`: an infinite-generation continuation policy exists. (Complement of A001 Theorem 14.2, which proves impossibility when `⋂_g K_g = ∅` under compact confinement — verified: the subsequential-limit argument at line 1758–1760 is correct.)

### R07.Cor6 (monotone obligations bound the generation count)

If the harm block translates by `accumulate` with a strictly positive obligatory increment `≥ c > 0` per generation (i.e., every admissible generation policy incurs it), and the normative floor is `h ≤ H_max` with `h ≥ 0`, then no intergenerationally viable path exists beyond `⌊H_max/c⌋` generations. (The A001 Corollary 9.1 integrability mechanism, line ~1660s region, in generation-indexed form.)

## Field 4 — State and phase space

Phase space per generation: the architecture's typed product `𝖹_{q(g)}` (physical, obligation/harm, mode blocks); the path structure lives in the disjoint union `⨆_g {g} × 𝖹_{q(g)}` (Operator II's phase-state convention, corrected `04` §1); transitions may change `q` through `τ^z_g`. Cumulative block `h` carried through `τ^h_g`.

## Field 5 — Quantifier order and information pattern

Thm2: `∃a ∀d` per generation (meta-action before disturbance, exactly corrected `04`'s order); the generation policy is causal in the observed phase state at each `t_g`. Thm4: universal impossibility (`∀ policies ∀ dynamics` — the impossibility is information-independent). Thm5: `∃π ∀d ∀φ` infinite-horizon. No intergenerational welfare aggregation is performed anywhere — the recursion is set-valued viability, not optimization (the docket's "no universal ethical claim").

## Field 6 — Assumptions, including existence/completeness

Thm2: Operator II data assumptions (exact tubes/successors, nonempty solution branches, at most one transition per interval — here exactly one, at the generation boundary). Thm4: closed `K_g`, continuous flow (no reset). Thm5: compactness + confinement + Hausdorff-usc successors (R03.Lem4's hypotheses). Cor6: positivity of the increment under *every* admissible policy (a strong hypothesis — flagged: if any policy can avoid the increment, the bound fails).

## Field 7 — Mapping type

`TRANSFORMATION` (the whole record is an Operator II instance); Prop3 is `EXACT_SPECIALIZATION` to ordinary viability; Thm4's necessity is `COUNTEREXAMPLE_OR_LIMIT`.

## Field 8 — Self-contained proof

### Proof of R07.Thm2

Backward induction over generations, structurally identical to corrected `04` §5 (the packet's proved exact-tube recursion) with three replacements: the stage index becomes the generation index; the terminal set `G` becomes the terminal generation's maintenance kernel `K_G` (or an Operator I kernel when post-path maintenance is required); and the successor clause is composed with the typed translation: an endpoint branch `x'` at `t_{g+1}` succeeds iff every translated state `τ^z_g(x')` (and translated harm `τ^h_g`) lies in `W_{g+1}` — this is precisely `Succ_g ⊆ τ_g^{-1}(W_{g+1})`.

*Sufficiency:* at generation `g`, play the witness meta-action; every branch stays in `K_g` (tube clause) and lands in `τ_g^{-1}(W_{g+1})` (successor clause); the induction hypothesis at `g+1` continues from every translated branch. *Necessity:* a viable policy's first action must satisfy both clauses for every declared disturbance branch (a tube violation is a safety violation during generation `g`; a successor outside `τ_g^{-1}(W_{g+1})` lands outside `W_{g+1}`, from which — by induction — no continuation exists). The infinite-generation statement follows from R03.Lem4 applied to the generation-indexed predecessor chain under the stated compactness. ∎

### Proof of R07.Thm4

Let `x(·)` be any continuous trajectory with `x(t) ∈ K_g` for `t ∈ [t_g, t_{g+1})`. At the boundary: `x(t_{g+1}) = lim_{t ↑ t_{g+1}} x(t)` with `x(t) ∈ K_g`, and `K_g` closed gives `x(t_{g+1}) ∈ K_g`; the next generation's constraint requires `x(t_{g+1}) ∈ K_{g+1}`. With `K_g ∩ K_{g+1} = ∅` this is impossible — for every policy, every dynamic, every generation length. (Convention check: whether the endpoint belongs to the closing or opening generation, one of the two memberships is forced by closedness and continuity, and the intersection is empty either way.) Conversely, if `τ^z_g` is a reset with `R_g(x) ∩ K_{g+1} ≠ ∅` on a nonempty set of states, the successor clause of Thm2 can be met on that set: the disjointness obstruction vanishes at the cost of a *typed jump* — which is exactly the Operator II semantics (state translation with identity/liability/obligation/harm carried by declared maps, not by continuous evolution). ∎

### Proof of R07.Thm5

The finite-horizon kernels `W^{(G)}` are decreasing in `G` (a longer obligation can only shrink the viable set: `W^{(G+1)}`'s successor clause requires reaching `W^{(G)}`, and monotonicity of predecessors in their target is corrected `04` Corollary 1's pattern) and compact (closed subsets of the compact enclosure, by the closedness of predecessor sets under closed successor values). Nonemptiness at every finite `G` is the hypothesis. The intersection `W_∞ = ⋂_G W^{(G)}` is nonempty by the finite-intersection property of compact sets. That `W_∞` supports an infinite-generation policy and coincides with the set of states viable at all finite generation horizons is R03.Lem4's fixed-point argument, applied verbatim to the generation-indexed predecessor operator (the witness-action compactness extraction is the same). ∎

### Verification of the retained A001 results

- Theorem 14.1 (line 1754): trivial relabeling — verified.
- Theorem 14.2 (lines 1758–1760): the subsequential-limit argument (`x(t_{k_j}) → x̄ ∈ 𝒦`, closedness of each `𝒱^{(m)}`, `x̄ ∈ ⋂_m 𝒱^{(m)} = ∅`, contradiction) — verified correct as stated, with the compact-confinement hypothesis explicitly retained (the source's own remark on its necessity stands).
- Theorem 14.3 (discounting pulse, lines 1766–1784): the welfare comparison `C(1 − e^{−ρT}) > c_v ⟺ ρ > −(1/T)ln(1 − c_v/C)` — verified correct; retained as the *behavioral* separation (a discounting objective can prefer exit), not integrated into the viability recursion (the two judgments stay typed apart, matching `TCS-1.0`'s noncompensation discipline).

### Proof of R07.Cor6

By induction: `h(t_{g+1}) = τ^h_g(h(t_g)) ≥ h(t_g) + c ≥ h(0) + (g+1)c` under `accumulate` with mandatory increment; the floor `h ≤ H_max` with `h(0) ≥ 0` gives `(g+1)c ≤ H_max`, so `g ≤ H_max/c − 1`. Beyond that generation count no admissible translated harm block satisfies the normative floor. ∎

## Field 9 — Counterexample showing necessity or failure outside scope

Thm4 is itself the impossibility witness (disjoint alternation). Failure outside scope: if the generation boundaries are *endogenous* (events inside intervals rather than fixed epochs), Thm2's fixed-review recursion does not apply — the packet's standing variable-event gap; if `τ^h_g = forgive` is chosen, Cor6's bound vanishes (forgiveness resets the count — a modeling choice with normative content, not a theorem); if compactness fails, Thm5's conclusion can fail (escape-to-infinity, the packet's own remark on Theorem 14.2).

## Field 10 — Interface producer/consumer contract

- **Producer:** the specification-path type + generation recursion + transition-map semantics (`τ^z`, `τ^h` variants).
- **Consumers:** `TCS-1.1` migration (GAP-1: the type is ready); the monograph's intergenerational chapter; any application claiming regime change (e.g., A018-style institutional transitions: their reset maps must be declared as `τ^z_g` records with harm translation — reviewer-enforceable); R09 Part U/M (the trichotomy fixed/change/disjoint is a scope statement, not a normative claim).
- **Failure condition:** applications asserting smooth (reset-free) transition between disjoint regimes — Thm4 makes this refutable in one line; applications using `forgive` without declaring it.

## Field 11 — Error, horizon, and safety erosion for approximations

Not an approximation result (exact set-valued recursion). Approximate generation tubes follow corrected `04` Corollary 3's outer-tube discipline (inner certificates); erosion enters only through per-generation `K_{g,−r}` if margins are needed — the R03/R05 machinery applies per generation unchanged.

## Field 12 — Selector and implementation regularity

Arbitrary selectors (axiom-of-choice level) as in corrected `04`; measurable/regular generation policies need a selection theorem (open obligation D2, shared with R02). Implementation of `τ^z_g` (the reset) is an institutional act — its own implementation correspondence must be declared and all-branches-checked per R02's pattern before any intergenerational *institutional* claim.

## Field 13 — Stochastic/hybrid/RFDE qualifications

The recursion is deterministic fixed-epoch; stochastic generation lengths or chance-constrained continuation require QF-2's support alignment and a chance-version of Thm2 (open); RFDE phase states translate through `τ^z_g` as history resets (the review-synchronised resettable-memory semantics of corrected `08` is the compatible precedent); interior events remain outside scope.

## Field 14 — Novelty status with exact references

Internal: A001 §14 supplies Definitions 14.1 and Theorems 14.1–14.3; nothing in the packet indexes specifications by typed paths with obligation translation, proves the disjoint-alternation necessity of resets, or states the nested-compact existence complement. External: generation-indexed viability and regime-switching safe sets have relatives in hybrid-systems and multistage-control literatures; **the typed-translation necessity statement (Thm4) and the accumulate/cap/forgive obligation semantics are, to internal knowledge, new packaging; external check outstanding**; no bibliographic claim made.

## Field 15 — Publication destination

Paper 1 (intergenerational structure section: Def1, Thm2, Thm4); Paper 2 (theorem atlas: proofs); monograph intergenerational chapter (with A001 §14's verified results integrated and the discounting separation kept behavioral).

## Field 16 — Remaining obligations and revocation triggers

Obligations: `TCS-1.1` adoption of the specification-path type; endogenous-boundary (variable-event) extension — open; stochastic continuation — open; selector regularity (D2). Revocation triggers: withdrawal of the fixed-epoch convention without a variable-event theorem; any application presenting `τ^h = forgive` as consequence-free (the normative content must be declared).

## Field 17 — Machine-readable dependency edges

```json
{
  "result_id": "R07",
  "target": "T7",
  "depends_on": [
    "corrected_theorems/04_operator_II_transformation_candidate.md (exact-tube recursion, data conventions, monotonicity corollaries)",
    "corrected_theorems/08_A002_sampled_hybrid_audit.md (review-synchronised reset semantics for history states)",
    "R03.Lem4 (compactness horizon closure for Thm5)",
    "A001 §14 (Definition 14.1 line 1752; Theorems 14.1–14.3 lines 1754–1784) — verified"
  ],
  "unblocks": ["TCS-1.1 specification_path type (GAP-1)", "intergenerational applications", "monograph chapter"],
  "status": {"R07.Thm2": "proved", "R07.Prop3": "proved (trivial reduction, verified)", "R07.Thm4": "proved", "R07.Thm5": "proved", "R07.Cor6": "proved"},
  "mapping_type": "TRANSFORMATION + COUNTEREXAMPLE_OR_LIMIT",
  "novelty": "typed packaging internal-new; external check outstanding"
}
```

# The Substitutability-Elasticity (σ) Spectrum on the Paper-1 Witness Datum — Research Wave Record

**Task 105 / batch 8 / paper 1 (*Ecological Indicators*).** This wave executes joint-assessment point **3.A-8** (`BATCH8_PAPER1_ECOLOGICAL_INDICATORS_JOINT_ASSESSMENT.md`, §3.A point 8, §4 third residual): *the σ-spectrum program as its own research wave, with exact rational witnesses, machine verification, and the relevance test (named ecological decision; changes what an actual indicator reports; new exact witness datum; alters at least one management action).*

**Audited state.** All manuscript facts are verified against the current version `arena agent 1/paper rewrites/latex/paper1_assessment_separation_v52.tex` (still the current version at repo commit `988042a`). Per the owner's standing re-verification rule (this round's directive 3): the audit streams were written against a v51/v52-era state; every point below was re-verified against v52 before use, and several audit asks are pre-answered by v52's own content (§5.1's information reading; §5.5's scope delimitations; the Gao et al. 2023 addition) — see the companion `QUEUE_REVERIFICATION_AND_PLAN.md`.

**Standing rules honored.** New files only (no existing file modified); no legitimate content removed or condensed; the manuscript v52 is untouched — this wave is research, not a manuscript edit; a future implementation round (owner-gated) will carry the results into a new version under the never-overwrite rule.

**Artifacts in this folder.**
- `sigma_spectrum_verify.py` — the fail-loud exact-arithmetic verifier (standard library only; `fractions.Fraction` exclusively; no floats, no tolerances, no randomness; deterministic; any failed gate exits nonzero).
- `sigma_spectrum_run_log.txt` — the committed run output: **57/57 checks pass** (`ALL CHECKS PASS`, exit 0).

---

## 1. The program being executed (as consolidated by the joint assessment)

The batch-8 final (generalization) stream proposed pathway A — *nonlinear aggregation, the σ-spectrum, do this first* — with the relevance discipline "generalize the datum, not just the theorem": every generalization must ship its own small exact witness anchored to a named indicator. The joint assessment recorded it as point 3.A-8 with the Leontief identification (the typed operator `E_typ` as the σ→0 member of the aggregate family), the regime-mismatch framing, audit-Theorem 11 parts (1)/(3) as elementary and part (2) as a conjecture needing its own exact witness, and point 3.E-41's demand that the "Living Planet Index = σ=1" identification be made precise. This wave delivers all of that on the manuscript's own witness datum.

## 2. The σ-family, defined on the manuscript's own currency

**The datum (v52 §4.5).** Phase state `(q, x, s₁, s₂)`; transition-safe set `S₀ = {x ≥ 0, s₁ ≥ 0, s₂ ≥ 0}`; destination `G = {(1, x, s) : x ≥ 0, s ≥ 0}`; destination gain `e = (1/4, 1/4)`; rescue cost `c = 1`; action-indexed disturbances; menu `{NO-SWITCH, FAST, SLOW, STAGED}` with FAST's worst-case tube `[s₁−2, s₁]` in `s₁` (SLOW the mirror) and STAGED spending one unit of `x`. Weights `W₊ = ℝ²₊∖{0}` (the full cone; scale-invariant, so WLOG the closed simplex `p ∈ [0,1]`, `p` = weight share of coordinate 1).

**The floor-referenced indices (the LPI's currency).** `λᵢ := 1 + sᵢ`. `λᵢ = 1` exactly at the floor; `λᵢ > 1` above it; `λᵢ ≤ 0` = the coordinate is a full floor-unit below the floor (the collapse level). This is the currency in which geometric-mean abundance indices (the Living Planet Index structure) are defined.

**The family.** For weights normalized to sum 1, the CES/power means
`M_θ(λ; w) = (Σᵢ wᵢ λᵢ^θ)^{1/θ}`, with elasticity of substitution `σ = 1/(1−θ)`:

| member | θ | σ | reading |
|---|---|---|---|
| linear aggregate | 1 | ∞ | **the manuscript's own engine** (perfect substitutes; weak-sustainability dashboards) |
| CES | 2/3 | 3 | intermediate |
| CES | 1/2 | 2 | intermediate |
| geometric mean | 0 | 1 | **the LPI functional structure** |
| CES | −m | 1/(m+1) | m=1: the harmonic mean |
| Leontief min | −∞ | 0 | **the typed operator** (no substitution; Liebig) |

**Notation guard.** The manuscript's per-weight thresholds `ρ₁ = 2/3`, `ρ₂ = 3/2` (§4.5/§6.3) are *weight ratios*; the CES exponent here is `θ`. The two never interact. (The collision is exactly why this wave uses θ.)

**Lemma A (the θ=1 handshake — machine checks 1.1, 0.8).** With weights normalized, `Σwᵢλᵢ ≥ 1 ⟺ w·s ≥ 0`. So the θ=1 member of the family reproduces the manuscript's compensatory engine *exactly* — same acceptance set at every state and weight (verified on a 242-state grid: `P2(θ=1) = {x ≥ 1} ∪ {s₁+s₂ ≥ 2}`, Theorem 5(2) verbatim), and at the §6.3 datum the per-weight plan assignment (`FAST` for `p ≤ 3/5`, `SLOW` for `p ≥ 2/5`, i.e. the deposited thresholds `ρ₂ = 3/2`, `ρ₁ = 2/3` in ratio units).

**Lemma B (collapse convention).** For every θ < 1 member, any tube value `λᵢ ≤ 0` rejects the plan: a coordinate at or below the collapse level cannot be compensated by surpluses elsewhere. (The geometric mean is 0 there; CES with θ ≤ 0 is undefined; for θ ∈ (0,1) the convention is the family's defining honesty and is what makes the LPI reading coherent.) The θ=1 member alone keeps the manuscript's compensatory semantics — *only the perfectly-substitutable dashboard can compensate a collapsed coordinate*: itself an exact statement of the difference between the doctrines. On the diagonal grid the convention and the branch-free reading agree everywhere (at `s ≤ 1` both reject; the document's derivations note this).

**The protocol.** `P2(θ)` at state `z` = per-weight acceptance under the θ-aggregate: for every weight some plan in the menu keeps `M_θ ≥ 1` along its worst-case tube (physical and destination constraints unchanged — they are aggregator-independent; STAGED needs `x ≥ 1` and then serves every weight at every rung; NO-SWITCH misses `G` at every rung). FAST's worst tube point is `λ^F = (s₁−1, s₂+1)`, SLOW's the mirror.

**Lemma C (interval structure).** At fixed `z`, FAST's acceptance set in `p` is a downward interval `[0, U_θ]` and SLOW's an upward interval `[L_θ, 1]` (the mean is monotone in the weight share — linear in `p` for every θ ≠ 0, log-linear at θ = 0). `P2(θ)` accepts ⟺ `L_θ ≤ U_θ` (cover), with single-plan covers exactly at the typed margins (`sᵢ ≥ 2`).

## 3. The diagonal master equation and the exact closed forms

On the gap-region diagonal `z = (x < 1, s, s)`, `s ∈ (1, 2)` — the manuscript's §6.3 datum sits on it at `s = 6/5` — the cover condition collapses to one comparison:

**Master equation.** For θ > 0: `P2(θ)` accepts ⟺ `(s−1)^θ + (s+1)^θ ≥ 2`. For θ < 0: ⟺ `(s−1)^θ + (s+1)^θ ≤ 2` (the inequality flips with the sign of the denominator when solving the threshold comparison `p_F ≥ 1/2` — a flip the derivation must carry and the machine cross-validates). The θ = 0 member is its own limit: accept ⟺ `(s−1)(s+1) ≥ 1 ⟺ s² ≥ 2`.

**The exact rational closed forms** (all pure `Fraction` comparisons — no radicals ever evaluated; each is cross-validated by a second, independent code path, machine checks 2.1–2.3):

| rung | accept ⟺ | derivation |
|---|---|---|
| θ=1 | `s ≥ 1` | `(s−1)+(s+1) = 2s` |
| θ=2/3 | `s² ≥ 3`, else `27(s²−1)² ≥ (3−s²)³` | cube isolation: with `u³=(s−1)², v³=(s+1)², w=uv`, `t=u+v` satisfies `t³ = 2s²+2+3wt`; `f(t)=t³−3wt−(2s²+2)` is strictly increasing on `[√w,∞)` because `t² ≥ 4w > w` and `4 > w` (certificates `0 < (s²−1)² < 64`, rational); so `t ≥ 2 ⟺ f(2) ≤ 0 ⟺ 3w ≥ 3−s²`; cube the nonnegative sides |
| θ=1/2 | `s ≥ 5/4` | double squaring (both sides nonnegative on `1<s<2`): `√(s−1)+√(s+1) ≥ 2 ⟺ 2s+2√(s²−1) ≥ 4 ⟺ √(s²−1) ≥ 2−s ⟺ s²−1 ≥ (2−s)² ⟺ 4s ≥ 5` |
| θ=0 | `s² ≥ 2` | `p_F(0) ≥ 1/2 ⟺ (s−1)(s+1) ≥ 1` |
| θ=−1 | `s² ≥ s+1` | `2s/(s²−1) ≤ 2`; the critical floor is **φ = (1+√5)/2** |
| θ=−2 | `s² ≥ 3` | `(s+1)²+(s−1)² ≤ 2(s²−1)²`; the critical floor is **√3** |
| θ=−3 | `s³+3s ≤ (s²−1)³` | `(s−1)³+(s+1)³ = 2s³+6s` |
| θ=−m | `(s−1)^m + (s+1)^m ≤ 2(s²−1)^m` | multiply through by `(s²−1)^m` |
| Leontief | `s ≥ 2` | `min λᵢ ≥ 1` on both tubes = the typed boundary |

**The critical-floor ladder** (machine Table, checks 3.0–3.10; brackets are 1/100-grid, the algebraic identifications exact):

| θ | σ | critical floor s* | exact form / witnesses |
|---|---|---|---|
| 1 | ∞ | **1** | rational (equality at s=1) |
| 2/3 | 3 | ∈ (117/100, 59/50] | root of `27(s²−1)² = (3−s²)³`; witnesses 23/20 ✗, 6/5 ✓ |
| 1/2 | 2 | **5/4** | rational (equality; `√(1/4)+√(9/4) = 2`) |
| 0 | 1 | **√2** | `s² = 2`; bracket (141/100, 142/100] |
| −1 | 1/2 | **φ = (1+√5)/2** | `s² = s+1`; Fibonacci witnesses 8/5 ✗, 13/8 ✓ |
| −2 | 1/3 | **√3** | `s² = 3`; bracket (173/100, 174/100] |
| −3 | 1/4 | ∈ (179/100, 9/5] | root of `s³+3s = (s²−1)³`; witnesses 7/4 ✗, 9/5 ✓ |
| −4 | 1/5 | ∈ (46/25, 37/20] | |
| −6 | 1/7 | ∈ (189/100, 19/10] | |
| −8 | 1/9 | ∈ (191/100, 48/25] | |
| −12 | 1/13 | ∈ (97/50, 39/20] | |
| −16 | 1/17 | ∈ (39/20, 49/25] | |
| −∞ | 0 | **2** | the typed boundary |

The ladder is strictly increasing `1 < 5/4 < √2 < φ < √3 < s*(−3) < … → 2` (check 3.10): *the deeper the state sits in the discrepancy region (floors each nearly satisfying the typed margin 2), the lower the substitutability needed to expose the breach — and the collapse point of the whole ladder is exactly the typed boundary.* The appearance of **√2, φ, √3** as exact critical floors of the LPI-structured, harmonic, and CES(σ=1/3) aggregators on the manuscript's own datum is, to our knowledge, a new exact datum for the substitutability debate.

## 4. The critical-elasticity landscape σ*(z) — the new exact witness data

For each gap state `z` (typed-reject, linear-accept), the accepted rungs form a *prefix* of the ladder (nesting, §5), so there is a **critical elasticity** `σ*(z) = 1/(1−θ*(z))`: the σ-aggregator false-certifies `z` exactly when `σ ≥ σ*(z)`.

**Machine Table (Part 5 of the run log):**

| state `z = (x, s₁, s₂)` | σ*(z) | note |
|---|---|---|
| (1/2, 1, 1) | **∞ exactly** | only the linear member certifies |
| (1/2, 3/2, 1/2) | **∞ exactly** | min coordinate ≤ 1 kills both plans' viability under every θ<1 member |
| **(1/2, 6/5, 6/5) — the §6.3 canonical datum** | **∈ (2, 3), strict both ends** | θ=2/3 (σ=3) accepts strictly; θ=1/2 (σ=2) rejects strictly |
| (1/2, 5/4, 5/4) | **= 2 exactly** | the equality state of the θ=1/2 rung |
| (1/2, 13/10, 13/10) | ∈ (1, 2) | |
| **(1/2, 3/2, 3/2) — the LPI witness** | **∈ (1/2, 1), strict** | the LPI-structured member still certifies; the harmonic rejects |
| (1/2, 13/8, 13/8) | ∈ (1/3, 1/2) | the harmonic member's false-certification witness |
| (1/2, 9/5, 9/5) | ∈ (1/5, 1/4) | deep state |
| (1/2, 39/20, 39/20) | ∈ (1/17, 1/13) | near-typed-boundary state: σ* → 0 |

**The structure theorem on the witness (proved in §5; machine-checked Parts 4–6).** Gap states split exactly: (i) states with `min(s₁,s₂) ≤ 1` — only the linear member certifies (`σ* = ∞`); (ii) states with both `> 1` — a finite `σ* ∈ (0, ∞)`, given on the diagonal by the master-equation root; and `σ*(s) → 0` as `s → 2⁻` while `σ*(s) → ∞` as `s → 1⁺`.

## 5. The two theorems (with proofs on the witness; machine-anchored)

**Theorem S1 (nesting and the critical elasticity).** *For every pair of rungs θ > θ′ and every state z: acceptance at θ′ implies acceptance at θ.* Proof: for fixed positive λ and weights, `M_θ(λ; w)` is nondecreasing in θ (the power-mean inequality); the collapse convention preserves this (acceptance at any θ′<1 forces `λ > 0` on the serving plan's tube). Per (plan, weight), hence per weight, hence for P2. Consequently the accepted rungs at each state form a prefix of the ladder and `σ*(z)` is well defined; on the diagonal it is the master-equation root, and it is *strictly positive and finite* on every gap state with both coordinates > 1 (the master left-hand side `(s−1)^θ → ∞` as `θ → −∞` since `s−1 < 1`, so some finite θ rejects; `s₁+s₂ ≥ 2` accepts at θ=1). Machine: checks 4.1, 4.2, 8.2 (40 diagonal states, all ladder pairs; 64-state off-diagonal grid, rational rungs).

**Theorem S2 (uniform collapse at the Leontief limit only).** *(i) Pointwise:* every gap state is safe under some strictly positive elasticity — you never need full Leontief at a fixed state. *(ii) Uniform:* for every θ < 1 the rung false-certifies an exact rational interval of gap states (the critical floor `s*(θ) < 2` strictly; concretely: σ=3 certifies `s = 6/5`; σ=2 certifies `s = 13/10`; σ=1 (the LPI form) certifies `s = 3/2`; σ=1/2 certifies `s = 13/8`; σ=1/3 certifies `26/15`; σ=1/4 certifies `9/5`; σ=1/5 certifies `29/15`; σ=1/9 certifies `39/20`; σ=1/13 certifies `39/20`; machine checks 6.x). Hence no positive σ is uniformly safe on the gap region; the uniform critical elasticity is `inf_z σ*(z) = 0`, attained only in the limit; **the only uniformly safe aggregator on the gap region is σ = 0 — the Leontief member, which is exactly the typed operator** (machine checks 1.2, 3.9, 6.y: `V⁰ = V_typ`). Proof sketches: (ii) follows from `s*(θ) < 2` for every finite θ — evaluate the master comparison at `s = 2`: for θ ∈ (0,1) the accepting side is `≥ 2` and `(s−1)^θ + (s+1)^θ = 1 + 3^θ > 2` (strictly accepting); for θ < 0 the accepting side is `≤ 2` and `1 + 3^θ < 2` (strictly accepting); by continuity in `s`, some `ε > 0` has every `s ∈ (2−ε, 2)` accepted at that rung, and all of these are gap states (typed acceptance needs `s ≥ 2`). The machine exhibits a concrete rational witness per rung (checks 6.x).

**The audit-Theorem-11 adjudication, upgraded (closing joint-assessment points 3.E-40/41).**
- **(1)** "the gap is maximal at σ→∞" — confirmed; elementary (the θ=1 member contains every other member's acceptance; power-mean; machine 8.1).
- **(2)** "monotonicity of the gap in σ" — the *conjecture* label is now retired: the nesting is elementary (Theorem S1), and the substantive content — *where* the collapse happens — is now exactly computed as the critical elasticity `σ*(z)` with the master equation and the algebraic ladder (§3–4). **The audit's punchline is refined two-sidedly:** "protection comes from substitutability approaching zero" is true *uniformly* (Theorem S2(ii): only σ=0 is safe on the whole gap region) but *not pointwise* (S2(i): every fixed gap state is protected at some strictly positive σ — e.g. the canonical datum already at σ ≤ 2, the LPI boundary state at σ < 1). The ecologically correct statement is: *treat floors as constraints if you need one aggregator for all states; otherwise bound the elasticity below the state's critical value σ*(z).*
- **(3)** "V⁰ = V_typ" — confirmed exactly on the witness (machine 1.2): the Leontief member's acceptance is weight-independent, so P2 collapses into the common-plan/typed criterion. The audit's "structurally enforces the common plan" is precisely this weight-independence.
- **The LPI identification, made precise (point 41).** The σ=1 member is *the LPI's functional form* — the geometric mean of floor-referenced abundance indices `λᵢ = 1 + sᵢ` — evaluated under the manuscript's Protocol-2 quantifier structure (the full weight cone). Two caveats state the exact scope: (a) the LPI's inputs are abundance indices relative to a base year, not floor margins — the identification is at the level of the functional form on the ratio scale, with the floor as reference (`λ = 1` at the floor); (b) the LPI's operational weighting (equal weights on system-level indices, chained) is a *point* in the weight cone, whereas the protocol quantifies over the whole cone — the rung decision is therefore the *adversarial* version of the LPI reading (if anything, over-, not under-states the index's exposure). No claim is made that the LPI as published implements Protocol 2.

## 6. The relevance test — all four components, machine-anchored (Part 7 of the run log)

**(1) Named ecological decision.** The §6.3 resource-transition benchmark's closure decision: at the canonical datum `B(0) = 16/5` kt, `B_lim = 2` kt, heatwave `δ₀ = 1/2` — under the DFO-Precautionary-Approach-style limit rule, does the composite certification license the FAST plan (quota pulse + closure) *without* triggering the mandatory below-LRP response, given FAST's certified trough `B = 6/5` kt `= 0.6·B_lim` (the floor breached by 4/5 kt mid-transition on the adverse branch) while the dashboard's own tube minimum reads `2/5 > 0`? (Checks 0.2–0.6, 7.1.)

**(2) Changes what an actual indicator reports.** At the canonical trough `λ = (1/5, 11/5)`: the linear dashboard (equal weight) reports `6/5 ≥ 1` — "nonnegative margin, certified"; the LPI-structured geometric index reports `√(11/25) < 1` (exactly: `11 < 25`) — "below reference, decline signal." The *same datum, opposite reports* (check 7.2). And at the (3/2,3/2) witness trough `λ = (1/2, 5/2)`: the LPI-form reports `√(5/4) ≥ 1` — it *still certifies* (a false certification by the geometric structure itself) — while the harmonic form reports `5/6 < 1` and rejects (check 7.3). The indicator's report is a function of σ, and the wave gives the exact report table.

**(3) New exact witness datum.** The critical-elasticity bracket of the canonical datum **σ* ∈ (2, 3)** (strict both ends; machine 7.4), the algebraic critical-floor ladder `{1, 5/4, √2, φ, √3, …} → 2`, the master equation, the σ*-landscape table (§4), and the per-rung false-certification witnesses — every number an exact rational, every decision pure `Fraction` arithmetic, all in the committed verifier and log.

**(4) Alters at least one management action.** At the canonical datum: under the linear dashboard (or any CES with σ ≥ 3) the weight-adaptive protocol certifies — the transition proceeds with *no* mid-transition LRP response (the false certification; the floors breach at `−4/5` while the index reads `≥ 2/5`); under every σ ≤ 2 member (CES 2, the LPI-geometric, the harmonic, …, Leontief) the protocol rejects — the mandatory closure/rebuilding response triggers (check 7.6). At the (3/2,3/2) witness the action flip is sharper (check 7.5): *linear and LPI-form both certify* (no closure) while the *harmonic rejects* — so an agency that "fixed" its dashboard by switching from the linear to the LPI-structured form would still not trigger the response at this state; the flip requires σ below the state's critical elasticity `σ* ∈ (1/2, 1)`; and the triggered response is concretely the reserve top-up `κ* = 1 − x = 1/2` financing STAGED (converting the impossibility state into a rescue state, Prop 11's chain). **The aggregator choice — a reporting decision, not a management decision — flips a management action.**

## 7. Honest limits and scope

1. **Off-diagonal geometric decisions are log-transcendental.** The exact cover comparison off the diagonal is `ln(s₁−1)·ln(s₂−1) ≤ ln(s₁+1)·ln(s₂+1)`; the machine decides the proven-sufficient rational condition (both single-weight products ≥ 1) and the proven-necessary one (`max(s₁,s₂) ≥ √2`), and reports the residual honestly (10 undecided cells in the 64-state grid). All other rungs are exact in full generality. The headline results are all on the diagonal (the canonical datum is diagonal), so nothing load-bearing rests on the undecided cells.
2. **Interior-θ brackets only at tested rungs.** σ*(z) is bracketed between adjacent machine rungs (e.g. (2,3) at the canonical datum); the exact interior value is the master root, transcendental in general. The brackets are exact and strictness-refined.
3. **The ratio-currency choice.** The family is defined on `λ = 1 + s` (the LPI's currency), which is what makes the θ=1 member identical to the manuscript's engine (Lemma A). An alternative absolute-margin CES family would *not* contain the paper's engine as a member; that choice is documented rather than hidden.
4. **Grid vs continuum.** As in the manuscript's own discipline (§4.7): the grids validate the symbolic classification on enumerated instances; the continuum statements (S1, S2, the ladder identifications) carry proofs in this document, machine-anchored at every decidable point.
5. **Scope.** The witness datum only (v52 §4.5's menu, disturbance convention, horizon); no claim about other data, no empirical claim, and — per v52 §5.5's own delimitations — no transfer to the coupled-shock or infinite-horizon regimes (those are the audit's pathways C/F, unpre-answered and open). v52 §5.1's own line remains true and is *sharpened* here: "Nonlinear aggregate indices — CES-type substitutability … are different assessment operators, and the theorems claim nothing for them" — this wave is the first tranche of what *can* be claimed for them.
6. **The regime-mismatch framing** (Idealized vs Practical; Liebig as the physical norm) is carried as the *interpretation* layer of the manuscript-facing summary below, not as a theorem; the theorems are S1/S2.

## 8. What a future manuscript round can transcribe (owner-gated; additive only)

Under the never-overwrite rule this is a sketch for a labelled-extension subsection (e.g. §5.x "The substitutability spectrum on the witness datum"), not an edit made now: (i) the family table (§2) with Lemma A's handshake — it *extends* rather than replaces the §5.1 CES disclaimer; (ii) the master equation and the closed-form ladder (§3) with the √2/φ/√3 floors; (iii) the σ*-landscape and Theorems S1/S2 with the two-sided punchline; (iv) the LPI identification with its two caveats; (v) the relevance-test chain at the §6.3 datum (σ* ∈ (2,3); the report flip at the trough; the action flip at (3/2,3/2)); (vi) a pointer to this folder's verifier as the datum's companion extension. All additive; every existing sentence of v52 stays.

## 9. Reproduction

```
python3 "batch 8/sigma_spectrum_wave/sigma_spectrum_verify.py"   # exit 0
```
Standard library only; deterministic; `sigma_spectrum_run_log.txt` is the committed output of exactly this invocation (57/57 checks, `ALL CHECKS PASS`). Re-running reproduces it byte-identically (no timestamps, no randomness, no floats).

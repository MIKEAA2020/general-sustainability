# Result Record R08 — Docket T8: Robust–Epistemic–Chance Hierarchy Completion (Typed Maps and Converse Counterexamples)

## Field 1 — Result ID and target docket item

`R08` (R08.Prop1 exact-observation typed correspondence; R08.Ex2 five converse counterexamples (a)–(e); R08.Prop3 typed-map necessity). Target: **T8** ("state exact implications among robust, epistemic, institutional, and chance viability under support, filtration, information-state, and implementation assumptions … typed mappings rather than literal inclusions across different phase spaces; counterexamples to converses").

## Field 2 — Verdict

**Classical but useful (the monotonicity propositions, already fixed in corrected `01`) + new completion:** the typed correspondence between physical and information-state judgments under exact observation, and five converse counterexamples closing every non-implication the hierarchy lists informally. Nothing here is mathematically deep; everything here is load-bearing for citation discipline, which is precisely the docket's demand.

## Field 3 — Exact statement

**Setting.** The hierarchy's common signature `Ξ = (Ω, 𝔄_q, H, K, ℙ, 𝕎, 𝔖)` (corrected `01` §Common signature); epistemic judgments on information states `B` with compatible sets `Compat(B)`; chance judgments under a declared law with filtration.

### R08.Prop1 (exact-observation typed correspondence)

Let `O` be injective on a domain `D ⊇ K`, the filter exact (`B(x-history) = {x-history}` up to the observation identification), and the policy classes aligned (every observation-based policy on exact singletons is a state-feedback policy and conversely). Then the singleton map `Λ: x ↦ {x}` is a **typed correspondence**:

```
x ∈ RViab(Ξ)  ⟺  Λ(x) ∈ EViab(Ξ_B),   and   Λ(RViab(Ξ)) = EViab(Ξ_B) ∩ Singletons.
```

The epistemic kernel restricted to singleton information states *is* the physical robust kernel — through the map `Λ`, not as a subset statement. Under the same hypotheses with an implementation correspondence `𝖨`, the institutional judgment corresponds on pairs `(Λ(x), c)`.

### R08.Ex2 (converse counterexamples — each closes a hierarchy non-implication)

**(a) Controlled ⇏ robust.** `ẋ = u + d`, `K = [−1,1]`, `u ∈ [−1,1]`, `d ∈ [−2,2]`: `0 ∈ CViab` (policy `u ≡ 0` with branch `d ≡ 0` stays at 0) but `0 ∉ RViab` (against `d ≡ 2`, `ẋ = u + 2 ≥ 1` always: exit within time 1).

**(b) Chance-`p` ⇏ robust (support inside the robust class).** Same system, law `ℙ(d ≡ 0) = 0.9, ℙ(d ≡ 2) = 0.1`: `0 ∈ PViab_{0.9}` under `u ≡ 0` (safe with probability 0.9) while `0 ∉ RViab` — chance safety at `p < 1` is strictly weaker than robust safety even when the law's support is inside `𝕎`.

**(c) Robust ⇏ chance-1 (support exceeding the robust class).** `𝕎 = {0}` (robust class: no disturbance), law `ℙ(d ≡ 2) = 1`: `0 ∈ RViab(𝕎 = {0})` trivially, but `PViab_1` fails (the trajectory exits under the law's disturbance) — corrected `01` Proposition 8's guard is necessary, and the schema's QF-2 typing is what prevents the silent error.

**(d) Physical nonempty ⇏ epistemic nonempty (typed failure).** The hidden-mode system (A001 Example 4.1, line 558; R02.Prop3's plant): each physical state `(0, ±1)` is individually robustly viable, while the reachable information state `B = {(0,+1), (0,−1)}` lies in no epistemic kernel (empty common safe command). The physical kernel and the epistemic kernel are both nonempty and empty respectively — no inclusion can hold without the typed map, because the objects live on different spaces.

**(e) Implementation enlargement shrinks all-branches safety (Prop 7 reversal).** `K = {0}`, `ẋ = u + d`, `u ∈ {0}`, `d ≡ 0`: under `𝖨(u) = {u}` the institution is safe (stay at 0); under the *larger* `𝖨′(u) = {u, u+1}` the all-branches judgment fails (the branch `u+1 = 1` exits immediately). Enlarging implementation destroys all-branches institutional safety while enlarging some-branch safety — the quantifier flip is the whole content, and the schema's QF-3 guard (mandatory branch-quantifier declaration) is what makes the reversal visible before publication.

### R08.Prop3 (typed-map necessity)

Without an explicit correspondence map, cross-space statements ("the epistemic kernel contains the physical kernel", "more information enlarges viability") are **ill-typed**: there is no subset relation between subsets of `X` and subsets of the information-state hyperspace, and any apparent inclusion smuggles in a map whose hypotheses (injectivity, filter exactness, policy lifting, commuting updates — corrected `01` Proposition 6's conditions) must then be proved. Every hierarchy comparison must therefore cite either an aligned signature (same space) or a declared map.

## Field 4 — State and phase space

(a)–(c): `X = ℝ`. (d): `X = ℝ × {±1}` with information states in the hyperspace of closed subsets. (e): `X = ℝ` with implementation correspondence. Prop1: physical space `X` vs. information hyperspace `𝔅` (closed subsets of `X`).

## Field 5 — Quantifier order and information pattern

(a): `∃π ∃w ∃φ` vs `∃π ∀w ∀φ` — the controlled/robust gap is exactly the disturbance quantifier. (b): `∃π: ℙ(safe) ≥ p` vs `∃π ∀w`. (c): support condition `supp(ℙ) ⊆ 𝕎` vs `⊄`. (d): `∃π^{obs}` against compatible-state universality. (e): `∃π ∀u^real ∈ 𝖨` vs `∃π ∃u^real ∈ 𝖨`.

## Field 6 — Assumptions, including existence/completeness

All witnesses use Lipschitz dynamics with unique solutions; no existence subtleties. Prop1: injectivity of `O` on `D ⊇ K`, exact filter, policy-class alignment (all three hypotheses are exactly what corrected `01` Proposition 6 and A002's observation-fibre results already require — the packet's own observation-fibre criterion `K = O^{-1}(O(K))`, `thm:observation` line 501, is the static shadow of the same condition).

## Field 7 — Mapping type

Prop1: `EXACT_SPECIALIZATION`/typed correspondence (an admitted mapping in `TCS-1.0` §7 terms — the bridge that makes hierarchy comparisons well-typed). Ex2: `COUNTEREXAMPLE_OR_LIMIT`. Prop3: schema-discipline statement (feeds QF-2/QF-3 guards).

## Field 8 — Self-contained proof

### Proof of R08.Prop1

Under injectivity of `O` on `D` and the exact filter, the information state generated by a physical history is the singleton of the observation-identified state: `B_t = Λ(x_t)`. Policy-class alignment: a policy on singletons is a function of the (identified) state, i.e. a state feedback, and every state feedback factors through the singleton information state. Hence closed-loop solution sets correspond one-to-one: `Sol(π, w)` maps onto `Sol(π^Λ, w)` for the corresponding policies, with identical disturbance classes and horizons. The robust judgment `∃π ∀w ∀φ` on the physical side translates clause-by-clause into the epistemic judgment `∃π^Λ ∀w ∀φ` on singleton information states (the compatible-state universality is vacuous on singletons). Kernel correspondence follows. The institutional extension adds the correspondence `(Λ(x), c) ↦ 𝖨`-branches, unchanged in structure. ∎

### Verification of R08.Ex2

**(a)** `u ≡ 0, d ≡ 0`: `x ≡ 0 ∈ K` — controlled viability. Against `d ≡ 2`: `ẋ = u + 2 ∈ [1, 3]`, so `x(t) ≥ t` and `x` exits `{|x| ≤ 1}` by `t = 1` for every policy — not robust. **(b)** Under `u ≡ 0` the safety event `{d ≡ 0}` has probability `0.9 ≥ p`: chance-viable at `p = 0.9`; robustness fails by (a)'s branch. **(c)** With `𝕎 = {0}` the robust judgment quantifies over a single trivial branch; the law puts mass 1 on `d ≡ 2 ∉ 𝕎`: the pathwise safety event has probability 0. **(d)** At `z = 0` with `K = {z ≥ 0}`: state `(0,+1)` is maintained by `u = +1` (`ż = +1`), state `(0,−1)` by `u = −1`; from `B = {(0,+1),(0,−1)}` every command crashes one branch — no observation-based policy is robustly safe, while each singleton is (R02.Prop3's plant at `z = 0`; the packet's own Example 4.1 verbatim). **(e)** `𝖨 = {u}`: trajectory stays at 0 — safe. `𝖨′ ⊃ 𝖨`: the realized-action set at the single command is `{0, 1}`; the branch `u^real = 1` gives `ẋ = 1`, exiting `K = {0}` immediately — the all-branches judgment fails under the *larger* correspondence. ∎

### Proof of R08.Prop3

A subset statement `A ⊆ B` requires `A, B` to be subsets of a common space. Physical kernels are subsets of `X`; epistemic kernels are subsets of the hyperspace `𝔅`. The only well-typed comparisons are (i) same-space comparisons (the hierarchy's Propositions 1–5, aligned signatures) or (ii) comparisons through a declared map `Λ` (Prop1's pattern), whose hypotheses must be proved. Corrected `01`'s Proposition 6 (information refinement) already encodes this discipline for refinement maps ("Without the policy-lifting and state-comparison maps, 'more information enlarges viability' is not a well-typed inclusion statement") — Prop3 generalizes the requirement to every hierarchy comparison and is enforced by the schema-audit guards QF-2/QF-3. ∎

## Field 9 — Counterexample showing necessity or failure outside scope

Ex2 is the counterexample set; each is minimal. Failure outside scope: Prop1's correspondence requires injectivity on `D ⊇ K` — A002's safety-crossing fibres (`thm:observation` corollary, line 537–542 region: two admissible states, same observation, opposite safety) are the standing obstruction to extending the correspondence beyond injective observations, and the packet's criterion is exactly the boundary: exact observation-only certification is possible iff safety is constant on observation fibres.

## Field 10 — Interface producer/consumer contract

- **Producer:** the typed correspondence `Λ` + the counterexample register.
- **Consumers:** corrected `01` (the hierarchy document gains its converse counterexample appendix and the typed-map clause); Paper 2 (hierarchy section finalized); R09 Part U.2/M.6 (witnesses); every application paper that compares judgments across spaces (must cite `Λ` or an aligned signature — reviewer-enforceable).
- **Failure condition:** any publication asserting a literal inclusion between physical and epistemic/institutional kernels without a declared map (ill-typed per Prop3).

## Field 11 — Error, horizon, and safety erosion for approximations

Not an approximation record. (Approximate observation/injectivity failure routes to R02's conservative filter soundness and R03's erosion; the correspondence degrades to outer/inner certificates exactly as there.)

## Field 12 — Selector and implementation regularity

Prop1's policy correspondence is at the class level (no selector claims); Ex(e) is the implementation-regularity witness: the quantifier declaration is mandatory before any monotonicity claim (QF-3).

## Field 13 — Stochastic/hybrid/RFDE qualifications

Ex(b)/(c) are the chance-qualification witnesses: support alignment (QF-2) is the typing that separates Proposition 8's valid direction from its failure; no filtration subtleties beyond support (the witnesses use constant-in-time laws). RFDE/hybrid: the correspondence pattern extends with the history-space machinery (corrected `08`) — declared, not proved here.

## Field 14 — Novelty status with exact references

Internal: corrected `01` states Propositions 1–8 and eight non-implications *informally* (as warnings); this record supplies the typed correspondence and the explicit minimal witnesses — the completion the docket demands. External: monotonicity calculus and quantifier-gap counterexamples are standard robust-control/game folklore; **no external novelty claim is made or needed** — the value is citation discipline, and the external check is only to ensure the counterexample register doesn't duplicate a standard textbook list verbatim (irrelevant to truth).

## Field 15 — Publication destination

Paper 2 (hierarchy section appendix: Prop1 + Ex2); corrected `01` successor document (the hierarchy record updated with this completion); monograph.

## Field 16 — Remaining obligations and revocation triggers

Obligations: fold Ex2 into the corrected hierarchy record's next version; enforce QF-2/QF-3 in the `TCS-1.1` migration. Revocation triggers: none for the witnesses (they are concrete systems); Prop1 is revoked only if the correspondence hypotheses are dropped in citation.

## Field 17 — Machine-readable dependency edges

```json
{
  "result_id": "R08",
  "target": "T8",
  "depends_on": [
    "corrected_theorems/01_operator_I_hierarchy.md (Propositions 1–8, non-implication list)",
    "corrected_theorems/06_A001_selected_operatorI_audit.md (§2–§3: observation empties kernel, common-action obstruction)",
    "A002 thm:observation (fibre criterion, injectivity boundary)",
    "R02.Prop3 (hidden-mode witness reuse)"
  ],
  "unblocks": ["Paper 2 hierarchy section finalization", "R09 (U.2/M.6 witnesses)", "TCS-1.1 guards QF-2/QF-3 enforcement"],
  "status": {"R08.Prop1": "proved", "R08.Ex2(a)-(e)": "proved witnesses", "R08.Prop3": "proved (typing discipline)"},
  "mapping_type": "EXACT_SPECIALIZATION (typed correspondence) + COUNTEREXAMPLE_OR_LIMIT",
  "novelty": "completion packaging; no external novelty claim"
}

# Verification report — external review of the Automatica routes manuscript (v30) and the resulting v31

Manuscript audited: `paper2_obstruction_calculus_v30_Automatica_routes.tex` (and its v28 source).
Revision produced: `paper2_obstruction_calculus_v31_Automatica_routes.tex` + `..._v31_Automatica_routes_supplementary.tex` (v30 is untouched).

Each claim of the attached review (`/home/user/uploads/gpt paper 2 automatica.txt`) was checked
line-by-line against the source. Disposition: **FIXED** (claim correct, changed), **ALREADY SATISFIED**
(claim correct but the manuscript already handled it), or **REJECTED** (claim does not check out).

## A. Claims that were correct and are now fixed

| # | Review claim | Verification | Fix in v31 |
|---|---|---|---|
| 1 | Theorem 6 (static-observation completeness) is false as stated: static observation does not imply a constant control | CONFIRMED — the record is constant, so the policy is a function of time only (open-loop), not necessarily constant; the iff statement via the Nagumo boundary condition overclaims | Theorem 6 rewritten as **static-observation reduction to open-loop viability**: policies coincide with open-loop controls, `B0 ∈ ERViab` iff an open-loop control keeps all branches in `𝒱`; the robust Nagumo condition is stated as exact *within the constant-control subclass* only |
| 2 | Remark 3 (certainty-equivalence) overclaims: `Viab(𝒱;Π_CE)=∅` is not established; the bias-corrected member may keep viability | CONFIRMED — the class definition admits laws using the observation map's structure | Remark 3 rewritten as a **policy-specific (singleton) claim**: the uncorrected controller `u=g(Ŝ)` empties the kernel; the bias-corrected controller restores it; no class-emptiness assertion. Consistent fixes in §1.2 item 6, the abstract, the §6 discussion table, and the conclusion |
| 3 | Belief definition is circular without an explicit applied-control history | CONFIRMED — `B_t` uses `u(s)` but the regulator's knowledge is stated only via the record | §2.3 now states the regulator knows *its own applied controls `(u(s))_{s<t}`*, which are common to every candidate trajectory |
| 4 | `𝒜_N` used before definition | CONFIRMED — used in the §3.3 ladder and Fig. caption, never defined | `𝒜_N(B)` defined in §3.5 (`{a ∈ U^B(B) : Post(B,a,y) ∈ 𝒲_{N-1} ∀ possible y}`) and referenced as such in the ladder |
| 5 | Blind-window hypothesis near-circular / wrong control class (`∪_{x∈B₀}U(x)`) | CONFIRMED — the class should be the controls an observation-based policy can actually realize | (H4.2) re-quantified over the **implementable blind-window class** (`u(t)∈U^B(B_t)`), with an explicit inadmissibility branch added to the proof |
| 6 | Finite-fibre / finite-checkability overstated in abstract and §1.1 | CONFIRMED — Prop. 2's fibre is a continuum, so "finite-fibre" misdescribes finiteness | Abstract and §1.1 now say **finite-state, polyhedral, and finite-horizon** |
| 7 | Proposition 5 (fibre) preimage must be relative to `Z` | CONFIRMED (minor) — the proof text already says "on the admissible domain", but the display was bare | Statement retained; the `K = O⁻¹(O(K))` display is explicitly scoped "on the admissible domain" (it was already correct in the proposition; the bare display is unchanged but unobjectionable) |
| 8 | §1.2 five-vs-six taxonomy unmapped | CONFIRMED — the abstract splits five+six; §1.2 lists six items with no tags | Each §1.2 item tagged: two *(finitely checkable)*, two *(closed-form conditional)*, one *(minimal construction)*, sixth *(policy-class restriction)*; intro sentence aligned ("a sixth under a policy-class restriction") |
| 9 | Viab vs RViab quantifier in §2.1 | CONFIRMED (minor) — Viab bullet omits the disturbance reading | Viab bullet now states "no disturbance, or a known disturbance trajectory" |
| 10 | `D_ε(x,u)` used before defined | PARTLY CONFIRMED — declared in §2.4 but the defining formula lived only in the v28 full proof (which the condensed main replaced by a sketch) | Defining formula added to §2.4 notation |
| 11 | Theorem 4 initial-observation convention / alternating tree | CONFIRMED (minor clarity) | §3.5 states the convention: `B₀` is post-observation; the tree alternates regulator/nature turns |
| 12 | §9 type ambiguity `supp b ∈ 𝒲_k` and over-strong deterministic-limit claim | CONFIRMED — `supp b` is a set, `𝒲_k` a family of beliefs; and `V_k(b) → 1_{B∈𝒲_k}` needs a uniform-concentration argument, not a bare assertion | Theorem 7 now states the Smallwood–Sondik recursion with `P(y|b,a)` and the time convention; Prop. 7 uses `b ∈ Δ(𝒱)`; Remark 5 replaced by **Proposition 8 (degenerate limit)** proved for the finite case with the uniform-concentration hypothesis, with the continuous-state caveat stated honestly |
| 13 | Case study not reproducible | CONFIRMED — the delayed hidden-regime model was not formally defined | §8 adds **"A reproducible delayed hidden-regime model"**: exact instance, belief evolution, closed form `σ*(B₀)=z₀−1`, viability iff `z₀ ≥ 1+T_obs`, and where each certificate fires |
| 14 | CE hitting time | CONFIRMED as approximately right; 3.34 is a truncation | Stated as ≈3.3 |
| 15 | "region where the index may certify safety" | CONFIRMED (wording) | Now "the set of observation values where the index may certify safety" |

## B. Claims that are already satisfied (no change needed)

- **Theorem 1 measurable selection**: (H1.2) plus the explicit Aubin–Frankowska Thm 8.1.3 measurable-selection step are present.
- **Theorem 2 local tangency vs finite exit**: (H3.3) already handles closed-loop realization of the local adverse selection.
- **Proposition 3 reach-set quantifier**: `Reach_{[0,Δ]}` is defined as the all-disturbance robust reach set; a single exiting trajectory shows non-inclusion, as in the proof.
- **Proposition 4 ladder**: stated as nested *necessary* conditions with "emptiness descends"; the missing piece was only `𝒜_N` (fixed above).
- **Proposition 5 measurability of the certifier**: the proof already covers the measurable certifier on standard Borel spaces.
- **Kernel hierarchy/`proj_∃`**: §2.1 already gives the explicit inclusion chain and the epistemic→physical implication `B₀ ∈ ERViab ⟹ B₀ ⊆ RViab`.
- **Novelty**: §1.3 already scopes the claims ("not stated in this form; the elementary facts are classical").

## C. Claims that do not check out (rejected)

- **"MSC 91B761 typo"**: the manuscript has `49J53; 93B03; 93C41; 91B76` — correct, no typo.
- **"Title spacing 'ObservationAmin'"**: a PDF text-extraction artifact; the source title is correctly spaced.
- **"Section 6.3 referenced where 6.2/6.4 intended"**: every §6.x cross-reference in the source is correct.
- **"`D_ε` never defined"**: it was defined in the v28 proof and declared in §2.4; the real (now fixed) gap was that the condensed main's proof sketch dropped the formula.
- **"Prop. uniform-margin proof gap"**: the full proof (supplementary) already uses closed-graph + measurable local selection; correct.

## Build verification (v31)

- Main: 15 pages, two-column, 4 figures, 1 table, 0 `??`, no overfull boxes, no undefined references; abstract 262 words.
- Supplementary: 13 pages, 3 figures, 0 `??`, no warnings; S1 carries the corrected statements/proofs (the revisions are applied to the shared source before extraction).
- Both `.tex` and `.pdf` compile standalone with tectonic 0.15.0.

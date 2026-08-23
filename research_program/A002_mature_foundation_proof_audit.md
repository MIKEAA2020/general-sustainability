# A002 Mature-Foundation Proof Audit — Conservation, Substitution, and Observation

## Scope

This audit checks the first dependency-closed A002 theorem families directly against immutable source `uploads/general_theory.txt`. It covers algebraic noncompensation, typed conservation, positive-moiety boundedness, positivity, donor limitation, the conditional BIBS criterion, the Farkas substitution alternative, and exact observation fibres. It does not certify later sampled/RFDE/hybrid knowledge-kernel theorems.

## Source identity

SHA-256 is recorded row by row in `A001_A002_source_proof_locator.csv`. Source line locations below refer to the immutable uploaded file.

## Adjudication

| Result | Source lines | Decision | Required correction/qualification |
|---|---:|---|---|
| Domain-qualified noncompensation | statement 192–199; proof 201–220 | **Proof accepted** | Keep unrestricted counterexample separate from the restricted-domain iff certificate |
| Typed hybrid conservation | statement 227–241; proof 243–263 | **Proof accepted after one notation correction** | In the final telescoping display, replace `B b(s)` by the declared boundary rate `B varphi(s)`; require the same moiety vector to lie in the left kernel of every active mode's internal flow/jump matrix |
| Closed positive-moiety bound | statement 269–274; proof 276–290 | **Proof accepted** | Requires a nonnegative trajectory, strict positivity of every moiety coefficient, closed boundary, and local execution |
| ODE/RFDE/hybrid nonnegative invariance | statement 295–317; proof 319–345 | **Conditional proof accepted** | Restricted to the declared continuous-history RFDE phase space, local well-posedness, quasipositivity, reset/history preservation, and locally finite execution; no Zeno continuation claim |
| Donor limitation sufficiency | statement 349–351; proof 353–375 | **Proof accepted as a local tangency corollary** | Donor limitation establishes the boundary sign condition, not global existence or boundedness |
| BIBS criterion | statement 363–378; proof 380–406 | **Conditional proof accepted** | Completeness, locally finite resets, coercive `V` in the declared phase-space norm, flow absolute continuity, Dini inequality, and reset non-expansiveness are hypotheses—not consequences of bounded input |
| Linear substitution alternative | statement 428–442; proof 444–483 | **Proof and dimensions accepted** | Stacking `-I a≤0` treats `a` as an unconstrained variable in the Farkas system; multiplier dimensions are `alpha∈R^m_+`, `beta∈R^h_+`, `gamma∈R^n_+`, `delta∈R^p_+`; certificate is pathway-specific, not an exchange rate |
| Observation-fibre criterion | statement 500–510; proof 512–533 | **Proof accepted** | `K=O^{-1}(O(K))` is relative to the declared admissible domain `Z`; no statistical-identification claim |
| Safety-crossing fibres | statement 537–542; proof 544–559 | **Proof accepted** | The certainly-safe observation set is sound and maximal among sound labels, not necessarily complete or computable |

## Verification decisions

### Boundary symbol

The conservation statement uses `varphi` for the boundary-flow vector. The proof's final `B b(s)` is a symbol slip, not a mathematical change. The canonical corrected identity is

\[
L^T x(t)-L^T x(0)
=\int_0^t L^T B\,\varphi(s)\,ds
+\sum_{t_j\le t}L^T B^J\beta_j.
\]

### Farkas orientation

The orientation is correct. Feasibility

\[
Ra\le x,\quad Ea\le e,\quad Qa\ge s^{req},\quad a\ge0
\]

is written as

\[
\begin{pmatrix}R\\E\\-Q\\-I\end{pmatrix}a
\le
\begin{pmatrix}x\\e\\-s^{req}\\0\end{pmatrix}.
\]

The alternative multiplier equality gives

\[
\alpha^TR+\beta^TE-\gamma^TQ=\delta^T\ge0,
\]

and the strict separation inequality gives

\[
\gamma^Ts^{req}>\alpha^Tx+\beta^Te.
\]

No sign reversal is required.

### BIBS phase-space scope

The proof is valid as a scalar comparison theorem on any declared current/history phase space satisfying the explicitly stated hypotheses. It does not infer completeness and does not claim that a bounded pointwise physical state controls an RFDE history norm without the coercive functional.

## Publication routing

- These nine results form a coherent early Paper 2 block.
- Paper 3 may restate ledger-specific conservation/positivity instances but cites the canonical theorem family for abstraction.
- The Farkas theorem and CES theorem remain complementary and must not be merged.
- Observation-fibre results remain in Paper 2; empirical observation models in Paper 5 must establish their own `O`, admissible domain, and uncertainty semantics.

## Remaining A002 gates

Still open after this audit:

1. sampled, finite-clopen, RFDE, hybrid, and information-state kernel chain;
2. sample-and-hold convergence assumptions;
3. projectability and reduction theorems;
4. local-horizon and delay small-gain certificates;
5. theorem numbering, bibliography, and full status audit.

No later theorem is promoted by this partial audit.
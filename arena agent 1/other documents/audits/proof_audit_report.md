# Proof Presentation Audit
## *A Viability Theory of Constrained Sustainability under Uncertainty, Coupling, and Recoverability*

**Principle applied.** Every proof should be presented in full unless it is a standard
textbook or literature result, in which case an external citation replaces the repeated
proof. This audit classifies each proof in the manuscript.

**Method.** (1) Internet search to identify which results are standard/citable
(Nagumo, Hoeffding, Kamke/Hirsch, Poincaré–Bendixson, Rosen, Hayes, etc.). (2) Full
manuscript scan to find proofs that are condensed or sketched where a full proof is
warranted, and proofs of standard results that are unnecessarily reproduced.

---

## Part A — Internet classification of standard (citable) results

The following results are standard and are **correctly cited rather than reproved** in
the manuscript. No action needed.

| Result | Standard source | Manuscript handling |
|---|---|---|
| Nagumo viability / invariance theorem | Aubin (1991), Thm 4.1 | Cited (Thm 2.4, 5.1) — correct |
| Robust Nagumo (disturbance extension) | Aubin (1991), Ch. 1 (measurable selection) | Cited (Thm 4.5, 5.1) — correct |
| Kamke comparison theorem (cooperative systems) | Hirsch & Smith (2005), Thm 3.1.1 | Cited (Thm 6.1, 6.6, 10.1) — correct |
| No periodic orbits for strongly monotone planar flows | Hirsch (1988); Smith (1995) | Cited (Thm 10.2) — correct |
| Poincaré–Bendixson | Perko (2001) | Cited (Thm 10.2) — correct |
| Rosen's uniqueness (concave games) | Rosen (1965) | Cited (Lemma 12.1) — correct |
| Hoeffding's inequality | Hoeffding (1963) | Cited — correct |
| Hayes delay-equation stability | Hayes (1950) | Cited (Thm 4.3) — correct |
| Scalar comparison theorem for ODEs | Hale (2009) | Cited — correct |
| Feller absorption (diffusion exit) | standard SDE text | Cited — correct |
| Dasgupta–Heal / Solow–Hartwick | Dasgupta & Heal (1979); Solow (1974) | Cited — correct |
| Cobb–Douglas concavity | standard | Cited ("standard") — correct |

These are all standard results where external citation appropriately replaces a full
proof.

---

## Part B — Proofs already presented in full (no action)

The following proofs are complete and correct as written:
- Theorem 2.1, 2.2 (constraint/control monotonicity)
- Theorem 2.3 (product structure)
- Proposition 3.1 (recovery triviality), Corollary 3.1
- Theorem 4.1 (information refinement), Prop 4.2 (downward closure)
- Theorem 4.2 (observation empties kernel)
- Theorem 4.9 (observer safety buffer)
- Proposition 6.1 (mass balance)
- Theorem 6.2 (unimodal kernel — full phase-line + necessity proof)
- Theorem 7.2 (stationary joint viability)
- Theorem 8.1 (CES classification), Corollary 8.1
- Theorem 9.1 (exhaustible), Corollary 9.1
- Theorem 11.1–11.4 (cascade termination/containment/nilpotent)
- Theorem 12.1 (over-extraction — full FOC comparison)
- Theorem 12.2, 13.1–13.4, 14.2, 14.3, 16.1, 17.1

---

## Part C — Condensed proofs that should be presented in full

These are **original results** (not standard literature) whose proofs are currently
one-line sketches or phase-line statements. Per the stated principle, they warrant
full presentation.

| Location | Result | Current proof | Recommended action |
|---|---|---|---|
| **Theorem 4.5** | Robust invariance / tangency | "Measurable selection of k∈R_K plus the robust Nagumo condition" (1 line) | Expand to a full argument: define the closed-loop inclusion, verify the subtangential condition holds at every boundary point, apply the viability theorem. |
| **Theorem 4.6** | Belief viability fixed point | "Greatest-fixed-point argument in the complete lattice; Pre is antitone-then-monotone" (1 line) | Expand: state the partial order on belief collections, prove monotonicity of Pre, apply the Knaster–Tarski fixed-point theorem, verify the fixed point equals ERViab. |
| **Theorem 4.8** | Delayed-information obstruction | "Theorem 5.2 applied over [0,T_obs)" (1 line) | Expand: show the strip condition holds on each uncertainty branch, apply the finite-time exit bound, conclude nonviability before the informative observation. |
| **Theorem 6.3** | Affine recharge kernel | "Phase-line analysis" | Expand the phase-line reasoning explicitly (equilibrium, monotonicity, invariance of the interval). |
| **Theorem 6.4/6.5** | Allee kernels | "Phase-line"/"Theorem 6.2 applies" | Expand the Allee phase-line (g<0 below A, g>0 on (A,C), attraction to C). |
| **Theorem 6.6(d)** | Pollution frontier | "follows from the strict monotonicity of the frontier along a backward orbit" (1 line) | Expand: prove the backward orbit is a strictly decreasing curve Γ(K) and that it bounds the kernel. |
| **Theorem 10.1** | Coupled kernel upper set | "Kamke comparison" (already cited) | The citation is correct (standard result), but the deduction "y ∈ K" needs the closedness argument spelled out (it's one sentence now). |
| **Proposition 10.1** | Generic non-polyhedrality | "Proof sketch" | Expand into a full algebraic-genericity proof (transversality, dimension counting of the algebraic subvariety). |
| **Theorem 13.5/13.6** | Ostrom sufficiency / necessity | "Proof sketch" | Expand each into a full argument (especially 13.6's eight cases). |
| **Theorem 17.1** | Small-noise stochastic viability | Full proof present | No action (full). |
| **Lemma 12.1** | Rosen concavity | Concise but complete | Optionally expand the negative-definiteness verification. |

---

## Part D — Results whose proof is correctly cited (no action)
Standard results cited rather than reproved: Nagumo (Thm 2.4, 5.1), Kamke (6.1, 6.6,
10.1), monotone-flow no-cycles (10.2), Poincaré–Bendixson (10.2), Rosen (12.1),
Hayes (4.3), Hale scalar comparison (6.2), Feller (17).

---

## Summary

| Category | Count | Action |
|---|---|---|
| Standard results, correctly cited | ~12 | none |
| Proofs already full | ~30 | none |
| **Condensed original proofs needing expansion** | **~10** | expand to full |
| Proof sketches (Ostrom, non-polyhedrality) | 3 | expand to full |

The highest-priority expansions are **Theorem 4.5** (robust tangency), **Theorem 4.6**
(belief fixed point), and **Theorem 6.6(d)** (pollution frontier), since these are
central original results currently given as one-line sketches. The Ostrom
Theorems 13.5–13.6 and Proposition 10.1 should be converted from "proof sketch" to
full proofs.

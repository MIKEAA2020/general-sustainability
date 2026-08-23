# Self-Contained Specialist Prompt — Repair or Reject the A001 Composition Theorem

## Role

Act as a specialist in viability theory, controlled invariance, differential inclusions, barrier certificates, and compositional control. Produce a referee-grade mathematical decision. Do not assume access to any external project files.

## Source theorem to audit

Consider `n` coupled controlled subsystems

\[
\dot x_i=f_i(x_i,u_i,z_i,d_i),\qquad
z_i=C_i(x_{-i}),\qquad i=1,\dots,n,
\]

with local candidate safe sets

\[
Q_i=\{x_i:b_{i\ell}(x_i)\ge0,\ \ell=1,\dots,r_i\},
\qquad Q=\prod_iQ_i.
\]

The submitted source states, in essence:

> Suppose each subsystem has an input tolerance `bar z_i` such that `||z_i||≤bar z_i` implies there exists `u_i` with `D^+b_i(x_i)≥0` on `boundary Q_i`. If `sup_{x∈product Q_j}||C_i(x_-i)||≤bar z_i` for all `i`, then `product Q_i` is controlled invariant.

Its proof says only that each subsystem can be kept safe and therefore all can be kept safe simultaneously.

## Known defects that must not be ignored

1. Pointwise existence of each local `u_i` does not by itself provide a measurable/continuous/implementable feedback or well-posed closed loop.
2. Local controls may share actuators, budgets, allocations, or algebraic constraints, so separately nonempty safe-control sets need not have a jointly feasible product.
3. Every active boundary constraint must be handled simultaneously; one scalar `b_i` is insufficient for nonsmooth/intersection boundaries unless a valid tangent-cone formulation is used.
4. Disturbance quantifiers and information patterns are absent.
5. The solution concept and regularity assumptions required by the selected strong-invariance theorem are absent.
6. Coupling/interface bounds must hold on the proposed joint invariant set for every declared disturbance and mode.
7. Hybrid resets/events require reset preservation and nonblocking/non-Zeno assumptions; do not add them unless you state a separate hybrid extension.
8. Intersecting separately computed kernels is not a joint-kernel proof.

## Canonical requirements

Use an aligned robust quantifier order:

\[
\exists\text{ one causal admissible joint policy}\quad
\forall\text{ declared disturbances/branches}\quad
\forall\text{ admitted solutions}.
\]

Prescribed controls and realized controls must be distinguished if implementation is set-valued. Any theorem must state:

- state spaces and solution concept;
- regularity/compactness/convexity assumptions;
- local safe-control correspondences;
- joint shared-control feasibility;
- interface bounds;
- feedback-selection/well-posedness assumptions;
- exact conclusion and horizon.

## Preferred first theorem class

Seek the narrowest useful continuous-time theorem first:

- finite-dimensional controlled differential inclusion or Carathéodory ODE;
- closed product set `Q`;
- bounded interfaces on `Q`;
- robust tangent/barrier condition;
- product controls only if truly independent, otherwise an explicit joint feasibility correspondence;
- an identified viability/strong-invariance theorem that applies under the stated hypotheses.

A later nonlinear small-gain extension may be proposed separately. Do not put nonlinear gain functions into a numerical matrix without a valid reduction.

## Required output

1. **Verdict on the submitted theorem:** valid, repairable, or false as written.
2. **Minimal counterexample** if separate local feasibility does not imply joint feasibility.
3. **Repaired theorem statement** with all quantifiers and assumptions explicit.
4. **Self-contained proof** or a clause-level theorem match whose hypotheses are checked one by one.
5. **Independent-control corollary** for genuine Cartesian control sets.
6. **Shared-control version** using a joint safe-control feasibility condition.
7. **Destruction/rescue examples:** one where coupling destroys safety and one where bounded coupling plus feasible controls preserves it.
8. **Exact limitations:** partial observation, hybrid events, discontinuous feedback, nonconvex controls, and stochastic systems.
9. **Publication disposition:** main Paper 2 theorem, Paper 1 architecture theorem, monograph-only result, or open obligation.
10. A concise list of any remaining proof obligations.

## Rejection criteria

Reject any answer that:

- repeats “choose all `u_i` simultaneously” without proving joint feasibility;
- invokes Nagumo/viability theory without matching its regularity and solution hypotheses;
- silently changes existential control into universal-action safety;
- assumes a selector exists merely because pointwise sets are nonempty;
- claims a general hybrid/stochastic/partial-observation theorem from the continuous product argument;
- hides an essential proof in a supplement reference.

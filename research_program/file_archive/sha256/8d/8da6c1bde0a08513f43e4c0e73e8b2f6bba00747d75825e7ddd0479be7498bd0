# Provisional Reconciliation — A001 Composition Audit Batch

## Status

Inputs currently compared:

1. internal provisional answer;
2. ER044;
3. ER045;
4. ER046.

The user announced several responses. This reconciliation is therefore provisional. **No theorem or manuscript implementation is authorized until the batch is declared complete and jointly adjudicated.**

## Strong convergence

All three inputs agree that:

1. A001 Theorem 16.1 is false/invalid as proved.
2. Separate local nonemptiness does not imply joint feasibility.
3. The shared-control counterexample is decisive.
4. Interface bounds must hold on the proposed joint safe set.
5. All active boundary constraints must be enforced simultaneously.
6. Independent Cartesian controls and shared controls require different theorem clauses.
7. A selector, closed-loop solution concept, well-posedness, and an exact Nagumo/strong-invariance theorem match are mandatory.
8. Partial observation, hybrid resets, discontinuous feedback, stochastic systems, and nonlinear small-gain extensions remain separate.

## Current disagreements

### Disturbance information pattern

- Internal answer and ER044 use the desired robust order: one state-based policy must work for all unmeasured disturbances.
- ER045's main theorem uses `kappa(x,d)` and therefore treats the current disturbance as measured. ER045 recognizes this limitation later.

**Provisional preference:** retain `exists one policy / forall unmeasured disturbances` as the main theorem. A measured-disturbance corollary may be added separately.

### Theorem regularity route

- Internal answer uses a joint robust safe-control correspondence and a matched strong-invariance theorem, with a continuous selector as the clean first version.
- ER044 allows measurable selection plus an independently assumed Hausdorff-Lipschitz compact-convex closed-loop inclusion.
- ER045 uses affine controls, smooth inequalities, a locally Lipschitz selector, and Carathéodory/Nagumo invariance.

**Provisional preference:** state one abstract robust tangent-cone theorem with explicit selector/well-posedness assumptions, followed by a finite-dimensional smooth Carathéodory corollary. Do not conflate measurable selection with Lipschitz closed-loop regularity.

### Publication destination

- Internal answer: rigorous theorem in Paper 2; architectural lesson in Paper 1.
- ER044: Paper 1 architecture lemma, not main Paper 2.
- ER045: main Paper 2 theorem; broad architecture principle in Paper 1/monograph.

**Provisional preference:** Paper 2 for the fully proved theorem and counterexample; Paper 1 may state the architectural consequence only if citation closure is satisfied. Final routing awaits the full batch and Paper 2 length decision.

## Defects that must be corrected regardless of final wording

1. Do not claim linear growth follows from compact inputs/disturbances plus local Lipschitz continuity on an unbounded state domain.
2. Do not claim locally Lipschitz selection without matching a precise selection theorem or giving an explicit formula.
3. Do not allow the robust policy to depend on unmeasured disturbance.
4. Do not infer convexity or Hausdorff-Lipschitz continuity of the closed-loop velocity set from selector existence.
5. Do not use one barrier derivative when several constraints are simultaneously active.
6. Do not state global-time invariance without completeness/continuation assumptions.

## Candidate final theorem architecture — not yet adopted

1. Abstract robust product-invariance theorem using:
   - closed/prox-regular product set;
   - bounded interfaces;
   - robust joint regulation map `R_Q(x)={u: f(x,u,d)∈T_Q(x) for all d}`;
   - nonempty joint map;
   - valid selector and all-solutions strong-invariance hypotheses.
2. Smooth finite-dimensional corollary using all active gradient inequalities and a locally Lipschitz selector.
3. Cartesian-control corollary.
4. Shared-control counterexample.
5. Bounded-coupling destruction/rescue pair.
6. Explicit exclusions for hybrid, partial-observation, stochastic, and nonlinear-gain extensions.

## ER046 update

ER046 strengthens the provisional convergence by supplying both a single-valued robust causal-feedback theorem and a set-valued all-realizations theorem. Unlike ER045's main statement, it preserves an unmeasured-disturbance policy independent of `d`. Its shared-budget counterexample, joint safe-control correspondence, forward-completeness hypothesis, and Paper 2 routing align closely with the internal answer.

ER046 is provisionally the most complete theorem architecture received so far. Final wording must still fix one tangent-cone/strong-invariance route, treat convexification carefully, and prove selector/composition regularity rather than infer it.

## Awaited evidence

- remaining announced composition responses;
- exact clause-level citation for the chosen strong-invariance theorem;
- selector theorem match or explicit selector construction;
- final publication routing after Paper 2 length/split adjudication.

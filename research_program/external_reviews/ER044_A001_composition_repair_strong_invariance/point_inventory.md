# ER044 Point Inventory — Preliminary, Pending Full Composition-Audit Batch

## Strong points

1. Correctly rejects the source proof and gives the decisive shared-control counterexample.
2. Correctly elevates joint safe-control feasibility over separate local feasibility.
3. Correctly preserves the robust quantifier order for unmeasured disturbances.
4. Correctly requires simultaneous treatment of all active constraints.
5. Correctly distinguishes prescribed feedback from Filippov/Krasovskii realized velocities.
6. Correctly requires a clause-level match to a strong-invariance theorem.
7. Correctly isolates hybrid, stochastic, partial-observation, and nonconvex extensions.

## Qualifications and possible defects

1. Compact input/disturbance sets plus local Lipschitz continuity do not by themselves imply linear growth on an unbounded state domain. Forward completeness must remain an independent assumption or conclusion from a growth/Lyapunov bound.
2. A locally bounded measurable selector does not automatically make the closed-loop map Hausdorff-Lipschitz or its values convex; those are additional hypotheses that must be verified.
3. The cited strong-invariance clause must be checked against the exact tangent cone, regularity, and all-solutions semantics used in the final theorem.
4. The rescue example's proposed feedback is useful, but its displayed interval of safe selections should be checked face by face; the explicit choice `u=-C` under the stated bound is cleaner.
5. Routing the repaired theorem only to Paper 1 conflicts with the internal answer and ER045, which place the rigorous theorem in Paper 2 and the architectural lesson in Paper 1.

## Provisional disposition

Retain the diagnosis, counterexample, joint regulation map, and robust quantifiers. Keep theorem wording and publication destination open pending the remaining announced audits and exact strong-invariance citation check. No implementation.
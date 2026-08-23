# A002 Sampled, RFDE, Hybrid, and Information-Kernel Proof Audit

## Decision

Accept the sampled/full-state, finite-clopen observation, exact-tube, RFDE-history, review-synchronised hybrid, bounded-jump hybrid, compact-information, and finite-time sample-and-hold results **only at their explicitly restricted/conditional status**. The proofs establish exact predecessor recursions once their compactness, continuity, total-solution, reset, tube, selector, and information-state hypotheses are supplied. They do not establish those hypotheses for any A018–A025 application.

## Result-level adjudication

| Result | Decision | Binding scope |
|---|---|---|
| Sampled robust-viability kernel | Accepted | Compact `K,U,W`, continuous transition, full augmented state, arbitrary selectors; measurable/continuous policy requires another selection result |
| Policy-set expansion | Accepted | `F,K,W`, information, and policy semantics fixed |
| Finite-clopen observation knowledge kernel | Accepted | Exact finite clopen partition and exact prediction sets; endpoint safety only |
| Held-control tube predecessor and inter-sample-safe kernel | Accepted | Fixed review period, continuous exact held solution map, exact disturbance-segment encoding |
| Finite-clopen inter-sample-safe knowledge kernel | Accepted | Observation-before-action timing, clopen relative fibres, aggregate unobserved disturbance prediction |
| Sampled RFDE finite-clopen knowledge kernel | Accepted | Continuous-history phase space; compact uniformly bounded/equi-Lipschitz history class; total held solutions; speed bound; exact translated histories |
| Review-synchronised hybrid RFDE kernel | Accepted as conditional | Review-time events only; finite modes; continuous phase reset; clopen reset branch; total solutions and speed bound; no variable interior event theorem |
| Outer-semicontinuity counterexample | Accepted | Correctly shows OSC alone does not close a universal tube-containment predecessor |
| Bounded-jump hybrid ODE kernel | Accepted as conditional | Exact compact Hausdorff-continuous tube/endpoint maps and finite jump budget are assumptions; no derivation from hybrid basic conditions alone |
| Restricted sampled information-state tube kernel | Accepted | Compact information state and exact Hausdorff-continuous filter/tubes are assumed and observation-history computable |
| Finite-time sample-and-hold convergence | Accepted as conditional | Common compact enclosure and existence for exact, sampled, and comparison arcs; `C1` bounded derivatives; immediate unprojected deployment; finite horizon; uniform norm; global `O(h)` |

## Key interface checks

### RFDE history closure

The RFDE proof correctly checks all three required steps:

1. the safe history class is compact by Arzelà–Ascoli because histories remain in compact `K` and share a Lipschitz bound;
2. old and newly generated history segments meet at the common current value;
3. splitting increments at that join preserves the global Lipschitz bound.

Thus translated-history membership is proved under the declared speed and history hypotheses rather than assumed silently.

### Review reset semantics

The review-synchronised theorem treats a reset as a map on the full phase history plus mode. It does not overwrite physical history with an ordinary state reset. The reset branch is explicitly separated from the identity branch on clopen domains. This is a valid restricted resettable-memory construction, not a general delayed-hybrid event theorem.

### Exact-tube continuity

The source explicitly distinguishes:

- outer semicontinuity, which is insufficient for closed universal-containment predecessors;
- lower/Hausdorff continuity, which provides the reverse approximation needed for exact tube and knowledge-set recursion.

Hausdorff continuity remains a theorem hypothesis for the bounded-jump and compact-information constructions. It is not inferred from a jump budget or hybrid basic conditions.

### Information-state theorem

The compact information model assumes, rather than derives:

- exact compatible-state sets;
- exact latent tubes;
- compact branch parametrisation;
- recursive observation-history computability;
- Hausdorff continuity.

The theorem is therefore logically valid as a conditional kernel result and cannot be cited as proof that an application possesses an exact filter.

### Sample-and-hold comparison

The proof establishes a uniform local defect `O(h^2)` and applies discrete Grönwall over `O(T/h)` steps to obtain finite-horizon global error `O(h)`. The common compact enclosure, absence of projections/events, immediate deployment, and exact contemporaneous assessment are indispensable assumptions. The result does not identify review intervals with physical delay and does not transfer bifurcation boundaries.

## Closed verification actions

This audit closes the source-level questions corresponding to:

- RFDE translated-history Lipschitz closure;
- review-synchronised resettable-memory semantics;
- exact-tube Hausdorff continuity as a hypothesis;
- exact information-state/filter conditionality;
- sample-and-hold interpolation, common enclosure, and norm.

## Remaining limitations

1. No measurable/continuous/computable selector is supplied by arbitrary set-theoretic selection.
2. No variable-event delayed-hybrid kernel is proved.
3. No Zeno continuation theorem is proved.
4. No application exact filter/tube is constructed.
5. No finite-to-infinite horizon result is transferred outside the compact nested-set hypotheses.
6. The long theorem chain remains a major Paper 2 length driver and is the leading candidate for Paper 2A if the split trigger closes.
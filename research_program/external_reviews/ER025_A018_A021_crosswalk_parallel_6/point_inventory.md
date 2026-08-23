# ER025 Point Inventory — Preliminary, Pending Remaining Parallel Audits

## Status

Received during the announced multi-audit batch. No implementation or final disposition before batch completion.

## Strong points

1. Strong evidence-based and source-faithful C4/C5 crosswalk.
2. Correct no-concrete-NAIM decision.
3. Correct separation of equilibrium existence, stability evidence, quantitative NAIM data, and regional graph meaning.
4. Correct rejection of positive-dimensional promotion for incomplete Floquet/projection/prefactor data.
5. Correct identification of missing `G,f,g`, slack blocks, perturbation neighborhood, and physical coupling.
6. Correct model/operator and Hopf/Floquet/fold distinctions.
7. Correct memory-floor localization requirement.
8. Correct prefactor-aware domination refusal.
9. Correct BLZ bibliography versus exact-match distinction.
10. Correct minimal missing-data request.
11. Concise optional source remark is preferable to equation duplication.

## Points requiring correction or qualification

1. **`DT(0)` wording:** for a semiflow, `T(0)=Id` and the state derivative `DT(0)=Id` are not the problem. What may fail is operator-norm continuity `DT(t)->Id` as `t downarrow 0`, differentiability in time at zero, or the exact joint regularity demanded by a theorem. ER025's CSV row saying `DT(0)=Id` fails in `C0` is incorrect.
2. **History-cube wording:** use the established path-rich/nonempty-interior qualification; do not blanket-deny manifold structure for every compact target.
3. **Yield parity wording:** parity removes the exponential yield-gap certificate; it does not force total coupling to be large if other constants are small.
4. **Equilibrium stability:** source-stated stability supports qualitative hyperbolicity at `tau=10`, but the full A021 product remains unverified exactly as ER025 concludes.
5. **Optional remark:** if implemented, say C4 is the natural/selected architectural candidate, not a fully instantiated multi-block A021 model.
6. **Slack tube status:** retain as a proved theorem under its explicit assumptions, not merely a conjectural condition.

## Provisional disposition

ER025 is highly aligned with ER022–ER023 and the internal attempt. Retain its partial-crosswalk, concise architectural remark, and no-promotion result after correcting the `DT(0)` and history/parity wording. Await remaining audits.
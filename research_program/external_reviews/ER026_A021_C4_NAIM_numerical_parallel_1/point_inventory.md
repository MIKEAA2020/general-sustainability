# ER026 Point Inventory — Preliminary, Pending Remaining Numerical Audits

## Status

Received as the first of several audits of the numerical C4 periodic-NAIM work. No manuscript implementation or final status change until the announced batch is complete and jointly adjudicated.

## Strong points

1. Correctly upgrades the selected C4 object from unnamed/incomplete to a specific numerically supported periodic base.
2. Correctly reports the three-level monodromy convergence and empirical stable multiplier interval.
3. Correctly distinguishes numerical validation from interval/computer-assisted proof.
4. Correctly preserves the phase/normal distinction and the compact one-dimensional graph geometry.
5. Correctly identifies rigorous monodromy enclosure, continuum projections/prefactors, concrete coupling, and theorem matching as remaining barriers.
6. Correctly refuses unconditional theorem promotion.
7. A concise numerical-validation remark may be publication-useful after joint review.

## Issues for joint adjudication

1. **Floor-margin mechanism misstated.** ER026 says `qEN-R>0` on the cycle. The verified quantity is the full outer-floor argument
   `softplus_k(qEN-R)-ln(2)/k+delta`, whose minimum is about `0.00147554`. With `delta=ln(2)/k`, this equals positive softplus for finite deficit; the raw deficit need not be positive.
2. **Empirical interval is not rigorous.** `[0.687639,0.687704]` is a conservative discretization envelope, not an interval-arithmetic spectral enclosure or statistical confidence interval.
3. **Product bunching error.** ER026 writes `q_1(kT_0)<=M_sM_c(0.6877)^k`, using only the binding multiplier. For the actual two-block scaffold, the slack equilibrium at `tau=10` has the slower rate `beta_y approximately 0.00052673/yr`; product bunching must use `beta=min(beta_x,beta_y)` and the full prefactor.
4. **Prefactors not optional.** The machine table labels bunching `NUMERICALLY_VALIDATED` despite admitting `M_s,M_c` are missing. The binding finite-discrete work estimates `M_c about 4.55` and strong nonnormality; product bunching is a prefactor-dependent target, not verified.
5. **Complete-continuity overstatement.** Eventual compactness implies nonzero continuum multipliers can accumulate only at zero; it does not prove that the unresolved continuum spectrum follows the discretization or lies inside the empirical stable bound.
6. **Slack status superseded.** Subsequent internal work selected an identical C4 slack equilibrium at `tau=10`, refined its rightmost pair, and globally counted it numerically. ER026's generic slack discussion should be updated in joint review, while concrete `f,g` remain missing.
7. **Projection/attraction remain conditional.** The geometric graph and attraction statements are valid only after persistence and theorem matching; they are not conclusions of the numerical monodromy alone.
8. **Publication timing.** Any numerical validation remark must wait for all numerical audits and should use “method-of-steps/RK4 history discretization,” not imply validated collocation.

## Provisional disposition

Retain the numerical periodic-base upgrade and no-promotion decision. Correct the floor, empirical-interval, product-bunching, compactness, and slack wording. Defer the proposed manuscript remark to joint batch adjudication.
# ER034 Point Inventory — Preliminary, Pending Second CAP Audit

## Status

First of two CAP-specification audits. No implementation or final disposition until jointly assessed with the second audit.

## Strong points

1. Correctly approves the specification rather than claiming execution.
2. Correctly preserves seed/residual/floor values and outward-rounding requirement.
3. Correctly retains continuum Floquet, projection, slack, and bunching validation gates.
4. Correctly keeps concrete coupling and sampled-to-semiflow/projection obligations separate.
5. Correctly forbids theorem promotion.
6. Proposed CAP-status note is potentially useful after joint review.

## Corrections and qualifications

1. **Floor-margin functional:** the validated quantity is the full floor argument `softplus_k(qEN-R)-ln2/k+delta`, not raw `qEN-R-threshold`. The radius condition must use a Lipschitz bound for the full composed floor argument.
2. **Binding nonnormality:** `M_x mu_*^40` cannot be declared negligible before a validated binding projection/prefactor `M_x` is bounded. The direct discrete stable-complement norm is the relevant numerical benchmark.
3. **Slack bound:** `0.026` is an empirical MOL extrapolation target, not a validated continuum bound until Module 3 executes.
4. **Bunching margin:** `q40 approximately 0.118` is a target with error budget, not `THEORETICAL_MARGIN_ROBUST` in a theorem sense.
5. **Coupling norm convention:** if equations are written `F+epsilon f`, bound `f,g` independently and bound the residual by `epsilon`; do not state `||f||+||g||<=C epsilon` unless `f,g` denote residuals.
6. **Seed clearance status:** positive on the approximate seed; true-orbit clearance awaits the radii ball.
7. **CAP note timing:** defer manuscript insertion until the second audit is jointly reviewed; avoid implying interval execution has begun.

## Provisional disposition

Retain `SPECIFICATION_APPROVED_FOR_EXECUTION`, correct the floor, nonnormality, slack, bunching, and coupling wording, and defer the optional status note.
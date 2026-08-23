# A002 Projectability, Reduction, Diagnostic, and Stability Proof Audit

## Decision

Accept the projectability criterion, fibre obstruction, support-saturated stock limit, spatial aggregation identity/curvature bound, local-horizon bracket, and delay-independent small-gain result at their exact scoped status. None provides an automatic reduction of A018, a closed spatial moment system, a global depletion forecast, or a model-specific Hopf boundary.

## Adjudication

| Result | Decision | Binding scope |
|---|---|---|
| Four model-map definitions | Accepted | Specialisation, exact projection, approximation, and singular reduction remain distinct mapping types |
| Projectability criterion | Proof accepted | Autonomous full/reduced systems, `C1` projection, unique full/reduced solutions on stated domains |
| Fibre obstruction | Proof accepted | Rules out only an exact autonomous Markovian reduction on the specified projection |
| Support-saturated logistic stock limit | Proof accepted | Fixed finite horizon; uniform positive support lower bound; bounded stock; common bounded effort; existing absolutely continuous solutions; stock equation only |
| Logistic variance/covariance identity | Proof accepted | Static probability-normalised spatial aggregation with square-integrable fields |
| General curvature bound | Proof accepted | `C2` function on interval containing support and finite second moment |
| Local-horizon bracket | Proof accepted as conditional | Rate remains within the declared relative band on an interval already long enough to force crossing |
| Delay-independent small-gain theorem | Proof accepted as conditional | Linear RFDE, chosen logarithmic/induced norm, `alpha_0>beta_0`, each fixed finite delay |

## Technical checks

### Projectability

Differentiating semiconjugacy at time zero gives necessity. Conversely, the projected full trajectory satisfies the reduced initial-value problem, and uniqueness gives semiconjugacy while both solutions exist. Hidden fibres with unequal projected derivatives therefore obstruct an exact autonomous reduced vector field. Approximate, memory-bearing, nonautonomous, stochastic, or singular closures are not rejected.

### Support-saturated limit

The source correctly uses

\[
\left|\frac{A_\kappa}{\kappa+A_\kappa}-1\right|
=\frac{\kappa}{\kappa+A_\kappa}
\le \frac{\kappa}{a_0}.
\]

The resulting uniform vector-field defect is `O(kappa)`; finite-horizon Grönwall gives an `O(kappa)` stock-trajectory error. This does not control hidden detritus, memory, governance, effort feedback, or global bifurcations.

### Spatial aggregation

The logistic identity follows exactly from

\[
E[X^2]=\bar X^2+Var(X),\qquad
E[E_sX]=\bar E\bar X+Cov(E_s,X).
\]

The Taylor remainder gives the curvature bound. Neither statement supplies evolution equations for variance or covariance, so dynamic coarse-graining remains unclosed.

### Local horizon

The proof does not assume the hitting time exists. The upper rate bound forces `y(t_+)≤0`; continuity gives a zero, while strict negative drift gives uniqueness. The result is invalid if the rate reverses, policy switches, or the required rate band cannot be certified over the a priori interval.

### Halanay rate

The logarithmic-norm estimate yields

\[
D^+v(t)\le-\alpha_0v(t)+\beta_0\sup_{t-\tau\le s\le t}v(s).
\]

For each fixed `tau`, the decay-rate equation

\[
\eta=\alpha_0-\beta_0e^{\eta\tau}
\]

has exactly one positive root because `h(0)=beta_0-alpha_0<0` and `h' >0`. This proves delay-independent stability, while the numerical decay rate itself deteriorates with delay. It is a sufficient condition, not a characterization of Hopf crossings.

## Closed verification gates

This audit closes the source-level checks for:

- projectability uniqueness and scope;
- support lower bound, regularity, and `O(kappa)` constants;
- exact-static versus unclosed-dynamic coarse-graining;
- Halanay sign convention and stability-versus-rate distinction.

## Publication routing

- Projectability/fibre obstruction belong in Paper 2 and constrain every cross-module mapping.
- The stock-limit and aggregation results may appear as compact Paper 2 examples; application-specific reductions remain in Papers 3–4.
- The local-horizon theorem supports Paper 3 diagnostics.
- The Halanay certificate is an abstract Paper 2 result or concise Paper 4 prerequisite, not a substitute for the named C3/C4 spectral analysis.
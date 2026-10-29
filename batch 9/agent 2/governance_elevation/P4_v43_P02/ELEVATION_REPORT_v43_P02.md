# P02 substantive elevation report

**Priority applied:** elevation over softening unless truly irreparable. No outstanding mathematical problem is declared irreparable. New theorems and computations were pursued; residual gaps and negative field endpoints are not relabelled as closure.

## Outcomes against the three requested areas

| Area | Work executed | Outcome |
|---|---|---|
| Complete basin guarantees | Nonlinear persistence, logarithmic-stock asymptotic gains, exact review contraction, full proof and interval point/box constants | **Closed for the protective law under the sufficient assumptions of Theorem 7.5**, with the exact interior physical basin and excluded invariant faces. Not closed for mobilising/mixed/Euler laws. |
| Global spectral guarantees | All-delay analytic RHP root count, Routh starting count, invariant recurrence directions, finite interval event ordering and eventual-instability cutoff | **Closed for equilibrium stability at all four registered mobilising vectors and every positive delay.** Full periodic-orbit Floquet spectra and nonlinear mobilising basins remain separate. |
| Continuum folds | Six actual augmented orbit/kernel solves on odd 65/129/257 grids; analytic strip/pole/branch exclusions; interval FFT and rigorous alias/infinite-tail bounds for the whole orbit and kernel residuals | **Substantially advanced, not closed.** No validated full bordered inverse, nonlinear contraction or continuum nondegeneracy inclusion was obtained. A small rigorous residual is not an existence proof. |
| Dynamic field validation | Frozen public ICES data; common-support blocked response fits; stress and integration checks; ecological/recruitment competitors; exploratory recursive annual-surrogate prediction without future observations | **Actually tested, not fully validated.** Protective response gains over AR(1) are tiny; ecological and recursive stock endpoints fail baselines. The original autonomous DDE mechanism is not validated. |

## Numerical anchors

- Protective point global gain: **0.4749970566879342**; full declared box upper bound **0.6862935969581749** (outer displays are rounded upward in the manuscripts).
- A gated stable intervals: approximately **(3.666149014274, 150.358477310141)** and **(253.082596557594, 309.682275054844)** years.
- A ungated: **(6.881410630478, 132.374903454401)** and **(269.252385064090, 274.629634339065)**.
- B gated: **(5.512840731443, 80.424526714227)**; B ungated: **(6.213598734018, 76.290635687952)**.
- Odd257 fold approximations: lower **5.587236198663494**, upper **64.40232665082372** years. The upper differs from the finite m64 certified system by about **5.5e-7** years. Finite interval width is not continuum accuracy.
- Whole infinite-Fourier residual component maxima: lower orbit **<3.170e-10**, kernel **<6.360e-12**; upper orbit **<2.560e-10**, kernel **<3.140e-12**, in phase-variable weighted l1 norm with nu=1.001. Exact input decimals and outward bounds are deposited.

## Field endpoints retained, including failures

Primary corrected target support: 1960–1994 training; 1995–2009 validation; 2010–2024 test. Both response laws have 260 validation-selected candidates and two bounded locally fitted coefficients. Reference medians remain fixed to 1950–1994. The initial implementation had lag-dependent early training availability. Its outputs were inspected before the common-support correction and are preserved. Thus this is a disclosed retrospective test, **not** an untouched confirmatory holdout or external preregistration.

| Endpoint | RMSE / persistence | RMSE / autoregression |
|---|---:|---:|
| Mobilising response, one step | 0.899739 | 1.035233 |
| Protective response, one step | 0.865045 | 0.995314 |
| Logistic stock, one step | 1.354725 | 1.354675 |
| Recruitment-lag1 stock, one step | 1.003512 | 1.003475 |
| Mobilising stock, recursive | 2.354687 | 3.166058 |
| Protective stock, recursive | 1.934792 | 2.601476 |

One-step autoregression is AR(1); recursive autoregression is two-state VAR(1). Recursive persistence is the fixed 2009 state, not annual refreshed persistence. The protective recursive **proxy** improves on VAR(1), but its stock forecast fails. This does not count as joint model validation. The mobilising additive coefficient hits its positive lower bound. Central/scenario scalar integration differences under step halving are below 6e-13. Low/high reported biomass paths are stress scenarios, not independent replicated data or joint confidence sets. The fitted protective sufficient basin gain is about 2.31309, outside the theorem; exceeding one does not prove instability.

## Why the remaining gaps are not declared closed

A full continuum fold proof requires a validated infinite bordered inverse/coupling bound and a nonlinear existence/nondegeneracy argument that handles free-delay/period shift regularity. The implemented whole-series residual is a real prerequisite, not a replacement. Extending this to complete periodic Floquet spectra and mobilising basin separators requires additional validated operator/global dynamics analysis.

The field study has assessment smoothing, correlated stock/catch errors, a derived effort proxy, limited annual resolution, and no directly measured institutional states. Better ecological structure and direct decision/deployment/compliance observations are needed before an institutional-delay claim is identifiable. More flexible post hoc tuning of this same holdout would not close those issues. The negative stock endpoints are reported rather than hidden, and no policy threshold is transported to herring.

## Deliverables and checks

Main v43: **54 pages**; SI v10: **20 pages**. Three prior scientific figure assets are retained byte-for-byte under new versioned names; a new field figure is added in raster/vector form. All prior scientific sections remain, with scoped claim/status replacements documented in the separate assessment and complete diffs. Author identity, linked ORCID, seven keywords and approved AI declaration are retained.

Executed tests: **49 new + 64 inherited = 113 normally, and 113 with optimisation**, all passed. Independent numerical contour winding checks corroborate the analytic root count but are not mislabelled interval proofs. Source-build determinism, PDF text/visual layout, versioned cross-references and inherited byte identities were checked. Publication preserves all prior remote paths, modes and hashes and records byte verification in a separate receipt. No ECOMOD C17, deposit citation or unrelated companion is changed.

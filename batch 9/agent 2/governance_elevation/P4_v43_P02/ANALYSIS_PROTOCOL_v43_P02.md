# P02 analysis protocol — initial plan and disclosed amendments

29 October 2026. The initial plan below was recorded after data-availability inspection and before the first fits. It was not externally preregistered. The final integrity amendment records a correction made after initial outputs were inspected; the current analysis is therefore retrospective and not confirmatory.

## Priority and scope

1. Prove or reject a global-basin theorem for the protective law using nonlinear asymptotic gains, rather than extrapolating local spectra. Do not transfer it to the mobilising law.
2. Investigate the actual continuum-fold obstruction using odd-grid augmented solves and explicit off-grid/tail diagnostics. A finite-dimensional enclosure or convergence plot is not a continuum certificate. Report failure to obtain a complete certificate.
3. Conduct a quantitative, held-out field test of the governance response component using published ICES North Sea herring assessment data. Do not call this an autonomous ecological/governance DDE validation or a causal identification of institutional delay.

## Field source and observation model

Primary assessment: ICES SAG stock her.27.3a47d, assessment year 2025, key 19373 discovered from the StockList endpoint. Preserve raw API responses and hashes. Use completed years through 2024 only; exclude the 2025 terminal row, which lacks catches/fishing pressure and has no biomass uncertainty limits. No projected value is an observed repeat.

Use reported total biomass (TBiomass), not spawning biomass, as the stock-size observable. Because the API leaves TotalBiomassUnits empty, normalize biomass by the training-period median; preserve the unit metadata rather than silently filling it. Use U=(C/C_median)/(B/B_median), with both reference medians fixed on the training period, as a dimensionless catch-intensity proxy, not age-2–6 fishing mortality or directly measured institutional effort. Catch and total biomass share an assessment and are not independent measurements. No absolute-rate interpretation is made: separate normalization makes this proxy well-defined even while total-biomass unit metadata remain incomplete. Its scale is a declared observation gauge, not a measured qE.

For the dimensionless stock series N, derive a causal observed decline signal D_y=N_(y-1)-N_y. Apply softplus with kappa=10 and an exact held-input memory update, initializing at log(2)/10. This is an observation-driven response-component test, not a fit of the full endogenous stock equation.

## Original splits, candidates and selection (see the final amendment)

Target years: training 1951–1994, validation 1995–2009, test 2010–2024. Prediction origin y targets annual catch-intensity proxy y+1. Use only origin-known quantities. Assessment-vintage smoothing means these are blocked retrospective tests, not real-time historical forecasts.

Compare mobilising and protective response laws with the signal held over the one-year prediction interval. Integrate the scalar effort dynamics accurately (not an Euler command approximation). Search delay 0–12 integer years; memory times {0.25,1,2,5,10}; effort ceiling multipliers {1.05,1.5,2,4} times the maximum catch-intensity proxy in the fitting period. Fit the two positive effort-response coefficients on training data for each candidate; select hyperparameters by validation RMSE. Then refit only the two coefficients on training+validation using the frozen hyperparameters and evaluate once on test years. No selection on test performance.

Baselines: persistence and an affine AR(1), fitted on the same pretest targets. Primary endpoint: one-step test RMSE and ratio to each baseline. Also report MAE, bias and invariant-domain violations. A response-law predictive claim requires beating both baselines, not merely fitting the training record. Preserve negative and boundary-hitting results. Delay profiles are predictive hyperparameter profiles, not confidence intervals or identified deployment delays.

Numerical sensitivity: double scalar-flow resolution and compare predictions. Observational sensitivity: rerun with the published low and high total-biomass paths, explicitly as coherent-envelope stress scenarios, not independent draws or a simultaneous confidence set. A second assessment vintage, if retrieved, is a dependent sensitivity analysis, not independent replication.

## Reporting boundaries

A successful component test is partial field validation of the specified observation-driven law, not proof of the autonomous DDE mechanism. Poor predictive performance must be reported without changing the holdout split, adding a post hoc flexible law, or transporting theoretical thresholds to herring. Complete mobilising basins and validated full Floquet spectra require actual additional proofs, not relabelled sampled simulations.

## Integrity amendment after the first run

The first implementation dropped unavailable pre-1947 lagged predictors, which gave candidate-dependent training support (including different AR(1) fitting sets). This is not an acceptable common-support comparison. All initial outputs are preserved under `initial_unequal_support_...`. The corrected primary analysis uses common target support **1960–1994 training**, **1995–2009 validation**, **2010–2024 test**; every lag then has observed history. Reference scaling remains fixed to 1950–1994 as originally declared. This correction is disclosed as occurring after the first test output was seen; the result is a transparent retrospective test, not a confirmatory preregistered result. No hyperparameter is chosen from test performance.

A secondary ecological test and recursive annual-surrogate test will now be added before their estimation: compare held-pressure logistic production with recruitment-augmented production (lags 1,2,3 selected on validation), against persistence/AR(1), on the same common support. Then fit the logistic ecological component on pretest data and run a 2010–2024 recursive annual sampled surrogate using no future stock/catch data. This is exploratory, does not replace the primary component endpoint, and is not labelled a validation of the original continuous DDE.

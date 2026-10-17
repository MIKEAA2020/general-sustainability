# Cover Letter — Paper11 v68 (working edition)

**Title:** Forecasting against naive benchmarks: a scored test of process-based modules on Northern cod and the Edwards Aquifer  
**Author:** Amin Abaee  
**Journal:** *Environmental Modelling & Software*  
**Article type:** Research paper; Supplementary Information S1–S24

Dear Editor,

Please consider the enclosed manuscript for publication in *Environmental Modelling & Software*.

**Question and design.** Process-based modules are often added to environmental forecasting models on the assumption that mechanistic fidelity improves accuracy. This article treats that assumption as a testable claim, evaluating rolling-origin forecasts on two unrelated systems without pooling them: Northern cod spawning-stock biomass under two retrospective assessment series, and annual-mean head at Edwards Aquifer index well J-17. Each system is compared with persistence and the training mean under its own scoring rule and information set.

**Results.** Under the cod rule, no module clears the empirical two-horizon retention gate; the largest forecast deficit is concentrated in the 1991–1995 collapse, which the tested class cannot reproduce at the recorded catch. The completed operating-characteristic rerun estimates D1 true-M1 power at 95.0–97.5%, D3 true-M2 power at 10.5–13.0%, and D5 any-module false retention at 2.5–7.5%; the D6/D7 out-of-class false-retention estimates are much higher (72–97%), with cell-specific intervals in the SI. The rerun is distinguished from the carried-forward, unreproduced alternative-rule comparisons. On J-17, the one-year M2 forecast that persists recharge loses to persistence (14.70 versus 13.23 ft RMSE). M1 passes the Edwards H1/H2 point gate by 0.39 ft, but its uncertainty interval covers zero and its ranking reverses at five years. M2m also passes the point gate; the broader frozen specification separately classifies it as the same affine-AR(1) function class, not as an H1/H2 failure. Three Pass 2 climate variants pass the point gate but are class-demoted as M2m-plus-intercept variants. These score and class dispositions are reported separately.

**Contribution.** Proposition 2 gives an exact identity separating driver substitution from residual covariance. The rolling J-17 application reports both terms: the empirical substitution contribution is +76.03 ft², the residual cross-term is −27.49 ft², and the raw MSE gap is +48.54 ft². A single upper output clip at the 1992 origin reduces the archived scored gap to +40.99 ft². The 7.55-ft realized-flux result is a conditional diagnostic using target-year drivers unavailable at the forecast origin; it is not forecast skill. The half-autocorrelation threshold is presented only as a special case under its stated assumptions, and the separate stationary baseline comparison crosses at horizon two on the J-17 origins. The article also withdraws an earlier cross-system attribution of the cod deficit to weakly autocorrelated surplus production; the measured apparent net-production series is strongly autocorrelated.

**Protocol status.** The Edwards H1/H2 score gates were frozen and archived before their corresponding passes. The cod 5% band and some comparator declarations were formalised after the first pass had been scored; those completions and their chronology are disclosed, and they do not change the cod verdict. Neither system was prospectively registered, and the manuscript makes no such claim. The paper draws system-specific methodological inferences, not general management advice.

**Reproducibility.** The source bundle includes the exact rolling-origin J-17 identity audit, the deterministic cod simulation runner, stable seed derivation, restartable batch controls, four disjoint batch manifests, the hash-checking aggregator, the 14,000-row raw simulation archive and summaries, archived analysis data, and an extended standard-library verifier. The complete 200-replicate-per-cell rerun has been validated across all 14 DGP/noise cells, with no failed or non-finite replicates; the cod operating-characteristic figure and SI rate/decomposition tables are regenerated from the aggregate. The verifier passes 237/237 checks. Historical alternative-rule comparisons remain explicitly marked as carried-forward, not independently reproduced because their implementation was not located.

The work is original, is not under consideration elsewhere, and I have no competing interests to declare. Paper11 v67 remains preserved unchanged; v68 is the corrected working edition.

Yours sincerely,

**Amin Abaee**  
Independent Researcher

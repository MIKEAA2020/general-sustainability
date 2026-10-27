# Verification addendum for the v76 audits

This addendum records checks performed after the two original audit reports. It supersedes the original reports only where explicitly stated below. The submitted manuscript and supplementary source were not edited.

## Historical DFO scale anchor: resolved

DFO Science Advisory Report 2016/026, Table A2, PDF/printed page 16, reports 1983–1989 spawning-stock biomass estimates of 841.08, 863.23, 902.94, 836.00, 940.75, 886.40, and 921.66 thousand tonnes. Their sum is 6,192.06 kt and arithmetic mean is **884.58 kt**, rounding to **884.6 kt**. The table's 2015 SSB estimate, 298.65 kt, is **33.7618%** of this mean, consistent with the report's rounded 34% statement.

Primary source: https://waves-vagues.dfo-mpo.gc.ca/Library/365622.pdf

The original main audit's statement that the precise value had not been independently located is therefore superseded. The historical assessment-vintage qualification remains necessary. Later assessment material uses a revised reference-point framework; no current-2026 LRP was verified in this audit.

## Model-unit versus physical-unit ambiguity

Mapping the model floor of 2 biomass units to 884.6 physical kt requires **442.3 physical kt per model biomass unit**. An actual rescaling must apply consistently to biomass, carrying capacity, harvest rates, and biomass disturbances:

| Quantity | Model value | Rescaled physical value |
|---|---:|---:|
| Opening biomass | 3.2 | 1,415.36 kt |
| Adverse trough | 1.2 | 530.76 kt |
| Carrying capacity | 10 | 4,423 kt |
| Heatwave loss | 0.5 | 221.15 kt |
| Harvest capacity | 13/year | 5,749.9 kt/year |

Either label the toy values as model biomass units and declare this conversion, or retain the toy system's literal kt labels and describe the Northern-cod comparison as a separate dimensionless context comparison, not a physical conversion of the toy system. Neither interpretation is a fitted cod model.

The nonlinear index must preserve its normalization: if physical margin is `s_phys = c*s_model`, the same index is `lambda = 1+s_model = 1+s_phys/c`. Income and reserve quantities require their own declared scales; the biomass conversion does not automatically apply to them.

## Audit artifacts and reruns

Both independent-check scripts and their JSON results are included in this package. Both were rerun successfully:

- Main audit: 1,183 states, at least 41 weight probes per state; finite switching example; shared-shock margin calculation; logistic endpoint calculation.
- Supplement audit: four rationally enclosed geometric witness verdicts; 361 rational harmonic checks; numerical tangency corroboration; coordinate-cut counterexample.

These are independent audit checks, not the manuscript author's missing verifier families. Finite checks do not prove continuum identities. Numerical tangency estimates do not establish the global stationary-point count or minimum.

## Other evaluation qualifications

- The full-excursion time-sharing proposition is not refuted within its explicitly stipulated union-of-tubes class. The finite-switch example concerns a different natural derivative/control extension.
- Performance improvement must be distinguished from restoration of feasibility, and physical blending from randomised plan selection.
- The Kuhn-theorem objection is substantive, not merely a citation-scope issue: equal induced path distributions preserve safety-event probabilities; pathwise assessment alone does not defeat realization equivalence.
- The v76 CES continuity paragraph improves on v75. A uniform positive-slack argument over the compact weight simplex completes the intended deep-interior reasoning.
- Prior successful v76 PDF builds were reported by the user, but no PDFs/build logs were supplied for independent reproduction in this workspace. Source-level label checks do not validate hard-coded section/table numbers.
- Figure 2's appearance was not independently verified in the final follow-up. No figure edits were made. The user's requested future label rotation remains unimplemented here.
- No Lean build was run. Coverage conclusions are based on the pinned source, not an independently reproduced compilation.

## Overall recommendation

Major revision remains appropriate. This addendum resolves the historical DFO-number question and adds a normalization concern. It does not resolve the supplementary findings on erasure semantics, global certificates, Leontief fixed-sum claims, nested impossibility, or conjecture C5. The main rational witness remains intact.

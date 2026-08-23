# Northern Cod (NAFO 2J3KL): What a Fixed Scalar Depensation Model Cannot Explain

## Abstract

The post-moratorium spawning-stock-biomass series for Northern cod is used to test a deliberately narrow model class: a one-dimensional autonomous surplus-production equation with fixed parameters and fixed removals. Under local uniqueness, every non-equilibrium trajectory of a scalar autonomous ordinary differential equation is monotone between equilibria. A biomass series with repeated rises and falls therefore cannot be an exact trajectory of one such model. This rejects an exact fixed scalar-autonomous explanation; it does not reject depensation in richer models or identify the causes of collapse and delayed recovery.

Values reproduced from DFO Science Advisory Report 2016/026 show that the M-shift formulation of the Northern Cod Assessment Model assigns very high mortality to 1992–1994. That attribution is model-conditional: assessment proceedings caution that estimated M represents unreported deaths and may absorb unreported fishing mortality. The evidence therefore supports a split between the collapse window and the subsequent low-biomass/non-recovery window, but not a uniquely identified biological mechanism. Calculations previously reported for a constrained-M alternative and institutional margins are retained as reproduction targets, not verified results.

## 1. Scope

This paper asks one bounded question: can one fixed scalar autonomous depensation model reproduce the observed non-monotonic assessment trajectory exactly?

It does not provide a stock assessment, estimate an Allee threshold, identify the cause of collapse, or evaluate the full adequacy of fisheries governance. Measurement error, process noise, migration, age structure, time-varying mortality, time-varying catch, and observation models all lie outside the rejected class.

## 2. Model class

Consider

\[
\dot S=F(S)
=rS\left(1-\frac{S}{K}\right)
\frac{S-\mathfrak s}{K-\mathfrak s}-C,
\]

where parameters and the removal term \(C\ge0\) are constant. When removals are written as \(C(t)\), the model is nonautonomous and the theorem below no longer applies without augmenting and specifying the forcing dynamics.

### Proposition 1. Scalar-autonomous phase-line obstruction

Let \(F\) be locally Lipschitz on an interval. A nonconstant solution of \(\dot S=F(S)\) cannot have an interior local maximum or minimum and cannot cross the same equilibrium in either direction. Consequently, an exact path that repeatedly rises and falls across a common biomass interval is incompatible with one fixed scalar autonomous model.

**Proof.** If \(F(S_0)>0\), continuity gives a neighborhood in which the solution increases; if \(F(S_0)<0\), it decreases. If \(F(S_0)=0\), the constant equilibrium solution passes through \(S_0\), and local uniqueness prevents a distinct trajectory from crossing it. A nonconstant trajectory therefore remains monotone within one phase-line interval between equilibria. ∎

This proposition is stronger and cleaner than a threshold-location trichotomy. It is also narrower: it concerns exact trajectories, not noisy estimates or forced systems.

### Proposition 2. Extra-loss shift, conditional form

Let

\[
g(S)=rS\left(1-\frac{S}{K}\right)
\frac{S-\mathfrak s}{K-\mathfrak s}.
\]

For a constant loss \(C>0\), positive equilibria solve \(g(S)=C\). If \(C\) lies below the positive local maximum of \(g\), the lower positive root lies above \(\mathfrak s\). If \(C\) reaches or exceeds that maximum, the positive pair coalesces or disappears. A proportional extra mortality term is handled analogously through the per-capita equation. Thus an “effective threshold” is conditional on the modified equilibria existing; it is not automatically a shifted structural parameter.

## 3. Verified assessment values

DFO SAR 2016/026 Table A2 reports the following estimates from the NCAM M-shift formulation:

| Year | SSB (kt) | M (yr⁻¹) | \(e^{-M}\) |
|---|---:|---:|---:|
| 1991 | 734.51 | 1.002 | 0.367 |
| 1992 | 381.95 | 2.214 | 0.109 |
| 1993 | 101.05 | 2.575 | 0.076 |
| 1994 | 30.55 | 2.331 | 0.097 |
| 1995 | 9.68 | 0.288 | 0.750 |
| 1996 | 16.05 | 0.341 | 0.711 |
| 2000 | 34.42 | 0.717 | 0.488 |
| 2004 | 20.07 | 0.362 | 0.696 |
| 2005 | 25.18 | 0.288 | 0.750 |
| 2010 | 96.91 | 0.696 | 0.499 |
| 2015 | 298.65 | 0.278 | 0.757 |

The survival column is a transformation of the reported instantaneous M estimate, not an independently observed survival series.

## 4. Two-window interpretation

### 4.1 Collapse window

The M-shift formulation allocates much of the estimated mortality during 1992–1994 to M. This is evidence about that fitted formulation, not direct identification of starvation, predation, disease, or another biological cause. DFO framework proceedings note that de-facto M can also contain unreported fishing deaths.

### 4.2 Low-biomass and delayed-recovery window

After the collapse, SSB remained low and non-monotonic before a substantial increase after the mid-2000s. The scalar-autonomous proposition shows that one exact fixed scalar equation cannot reproduce all reversals. It does not select among residual removals, time-varying mortality, weak depensation, food limitation, migration, age structure, or assessment error.

### 4.3 Positive result

The defensible positive result is a model-discrimination split:

1. the exact fixed scalar-autonomous class is inadequate for the full path;
2. the M-shift assessment allocates the collapse-period residual mortality differently from alternative formulations;
3. the causes of delayed recovery require a model comparison with explicit observation and process error.

## 5. Governance facts and limits

The directed-fishery moratorium was announced on 2 July 1992. An annual 1992 SSB estimate does not identify the date on which a within-year threshold was crossed, so no one-year governance lead is inferred. Response timing also does not establish action magnitude, compliance, ecological effect, or counterfactual adequacy.

DFO announced a renewed commercial fishery on 26 June 2024 with a Canadian TAC of 18,000 t. This provides a later decision event for prospective analysis; it is not treated here as evidence that the earlier institutional response caused either collapse or recovery.

## 6. Reproduction obligations

The submitted constrained-M values, unreported-catch estimates, catch-to-production ratios, institutional margins, and ecosystem discriminants require a registered package containing:

- equations and model version;
- source series and transformations;
- window definitions;
- parameter constraints;
- estimation or optimization code;
- uncertainty and sensitivity analysis;
- machine-readable outputs.

Until that package exists, those numbers are hypotheses or reproduction targets rather than results of this revised article.

## 7. Minimal computational check

The original appendix simulations were rerun successfully. They confirm only that selected parameterized toy trajectories behave as expected below and above an Allee threshold. They do not fit Northern cod and do not validate the constrained-M experiment.

## 8. Conclusion

A fixed scalar autonomous depensation model cannot exactly reproduce a repeatedly rising-and-falling biomass trajectory. Northern cod therefore provides a useful negative model test, not a uniquely identified mechanism. The assessment evidence supports separating collapse from delayed recovery and comparing alternative mortality allocations with explicit uncertainty. Stronger biological or institutional conclusions require data and models not supplied by the scalar theorem.

## References

DFO. 2016. *Stock Assessment of Northern Cod (NAFO Divs. 2J3KL) in 2016*. DFO Can. Sci. Advis. Sec. Sci. Advis. Rep. 2016/026.

DFO. 2018. *Proceedings of the Northern Cod Framework Review Meeting*. Canadian Science Advisory Secretariat Proceedings Series.

DFO. 2024. *The Government of Canada announces the historic return of the commercial Northern cod fishery in Newfoundland and Labrador*. News release, 26 June 2024.

Liermann, M., and R. Hilborn. 2001. Depensation: evidence, models, and implications. *Fish and Fisheries* 2: 33–58.

Rose, G. A., and C. J. Walters. 2019. The state of Canada’s iconic Northern cod: a second opinion. *Fisheries Research* 219.

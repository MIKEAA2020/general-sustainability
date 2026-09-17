# Does a surplus-production ladder improve forecasts of Northern cod? A scored test on NAFO 2J3KL

**Reader-oriented restructuring draft (v51_reader_draft, 2026-09-17).**
This file re-expresses the frozen v50 paper (`paperE1_cod_forecast_ladder_v50.tex`)
in plainer academic prose, following the conventions of the landmark papers it
cites (Hutchings & Myers 1994; Hyndman & Koehler 2006; Kell et al. 2016, 2021;
Carvalho et al. 2021; Cadigan 2016): question-first abstract, one idea per
paragraph, every term defined at first use, numbers with units, limitations
stated as plainly as results. **No number changes from v50.** Text marked
`[carried]` is to be transplanted verbatim from v50 during typesetting.

---

## Abstract (plain rewrite)

Do more complicated models forecast fish abundance better than simple ones? We
answer this for one stock and one task: predicting next year's spawning stock
biomass of Northern cod (NAFO Divisions 2J3KL), and predicting it five years
ahead. We placed seven forecasting rules in a fixed order of increasing
complexity — from "next year equals this year" up to models with a stock-flow
equation, correlated errors, and delayed information — and scored every one of
them by a procedure decided before scoring began. At each of many forecast
origins, every model was fitted only to the past and then asked to predict the
future; its errors were pooled over origins. The result is negative and clean:
no complicated rule beats "next year equals this year" by more than a small
tie margin, at one year or at five. This holds on two differently estimated
biomass series for the same stock, and it holds even for the three models that
we allowed to see the catches over the forecast horizon — an advantage no real
forecast ever has. The evaluation is a conditional hindcast, not an operational
forecast, and it draws no conclusion about whether the stock itself is
sustainable. What it establishes is narrower: on this record, added model
structure did not earn its place.

**Keywords:** forecast evaluation; surplus production; northern cod;
rolling-origin; hindcasting; model selection; time series.

---

## 1. Introduction (plain rewrite)

Fisheries advice rests on models of how a stock grows and is fished. When such
models miss, the safe instinct is to add structure — a drift term, a lag, a
covariate — on the argument that the truth is complicated. Sometimes that
works. Sometimes it adds noise that a sparse historical record cannot carry,
and the added parameters simply track the last few noisy years. The two
outcomes look identical until the model is asked to predict data it has never
seen. This paper performs that test for Northern cod, in the style of the
forecast-evaluation literature (Hyndman & Koehler 2006) and of hindcasting in
stock assessment (Kell et al. 2016, 2021): many origins, refit each time, score
only out of sample, against a benchmark a child could state.

The stock gives the test its interest. Northern cod collapsed in the early
1990s under the harvest regimes documented by Hutchings & Myers (1994) and has
since partly recovered. A forecaster fit to this record confronts both regimes.
We use two biomass series for the same stock: a shorter one from the 2016
assessment (1983–2015) and a longer reconstruction from the most recent
assessment model (1954–2024), kept separate throughout — the two vintages are
never pooled.

[carried: §2 data description, assessment-vintage table, LRP definition]
[carried: §3 ladder specification, seven models with equations, Table 2]
[carried: §3.1 fixed-window collapse test]
[carried: §4 the information-set table and the conditional-hindcast statement]

## 2. The design in plain words

**The race.** Seven forecasters, ranked beforehand: naive persistence ("next
year like this year"); a training mean; then five structural models — two
logistic-growth models (one standard, one with a low-abundance penalty), a
stock-flow model fed each year's catch, a model adding correlated errors, and
one forced to work with one-year-old information.

**The rules, fixed first.** At a forecast origin t, each model is trained on
the past alone. It then predicts one year and five years ahead. Errors are
squared, averaged over origins, and square-rooted: the pooled rolling RMSE.
The benchmark is persistence. A structural model wins — is "retained" — only
if it beats persistence AND the next-simpler model by more than a 5% tie
margin at both horizons. Anything less is a tie by the rule, not a loss.

**Who knew what, when.** The information-set table [carried from §4] says, for
every input, whether it was knowable at the origin. Three models are
voluntarily handicapped upward: they receive the actual catches over the
forecast horizon — knowledge no operational forecast possesses. The biomass
series itself is a single modern reconstruction, not the assessment vintage
that was current at each origin; both smoothings press toward the structural
models. The test is therefore generous to complexity by construction.

## 3. Results in plain words

[carried: Tables 4–8 and the DM table, verbatim numbers from v50/ledger]

Pooled over origins, persistence is 98.05 kt at one year and 264.72 kt at five
on the short series; the closest structural model is 17% worse at one year and
9% worse at five. On the long series, persistence is 87.65 kt (mixed origins)
and 84.43 kt (origin-matched) at one year; the best structural model is 36–42%
worse. No verdict approaches the tie margin needed for retention. Splitting
the origins by period [carried §5 period split] shows the pooled statement
hides regime detail: in the collapse years the structural models are the
better next-year forecaster on five origins — too few to score, and not the
question this evaluation asks. On the pre-collapse fixed-window test, no model
fit before 1991 anticipates the crash; on the secondary capelin-index module,
every added covariate loses to persistence in every cell [carried Table 8].
Uncertainty statements [carried; with the v50 DM row note] are descriptive: no
short-series margin against persistence separates from zero, several
long-series margins do — in the wrong direction for retention.

## 4. What this means, and what it does not

The negative result is not "models fail on cod." The three catch-fed models
had future knowledge real forecasts lack, and still lost; that asymmetry
strengthens the result rather than excusing it. It is also not a verdict about
the stock: the paper forecasts a reconstructed series and concludes nothing
about sustainability. And it is not a claim that the assessment's state-space
model is redundant — that model produces the series being forecast; the ladder
here is deliberately simple so that a clean question can be asked.

The honest summary: on two vetted series for this stock, under a rule fixed
before scoring, simple persistence was not beaten by any structure that the
record could support. Where such a verdict is credible and where it merely
reflects a weak decision instrument is the subject of the framework companion
(Abaee, retention-rule framework).

## References (unchanged from v50) [carried]

# Does a surplus-production ladder improve forecasts of Northern cod? A scored test on NAFO 2J3KL

**Humanized version v53 (2026-09-17).** Merged from the Gemini and Grok
humanized rewrites after joint drift audit and adjudication (see
`audits_E1_E3/e1_audit_2026-09/E1_JOINT_EVAL_GEMINI_GROK_HUMANIZED_20260917.md`).
Prose mechanics follow the Gemini rewrite (topic sentences, numbered moves,
short declaratives); every number is a frozen v50/ledger value. Rejected
material (recorded in the evaluation): Gemini's simulation ranges (96.5–98.5),
the Cadigan page range 286–308, the added Fisheries-paper references, derived
percentages presented as results, and ASCII figure mocks; Grok's single
reference-string slip (Kell 2016) is corrected to the frozen string.
Supersedes v52 as the humanized line; v50 remains the frozen scientific text.

---

## Abstract

This paper asks a plain question and answers it negatively: does adding
structure to a forecasting model of the Northern cod stock (NAFO Divisions
2J3KL) make its forecasts better? Five surplus-production models and two naive
baselines were compared under a rule whose scoring core was fixed before the
scores were read. Three parts of that rule matter for reading the
results. (1) **The benchmark is trivial by design**: "next year's spawning
biomass equals this year's." (2) **The bar is double and pre-set**: a model is
kept only if it beats that benchmark and the next-simpler model by more than
a 5% tie margin, at one year and at five years ahead alike, on error pooled
over many rolling forecast origins. (3) **The information set is audited**:
for every quantity a model uses, the paper records whether it was knowable at
the forecast origin. The target series is a modern assessment reconstruction,
so its earlier values embed information produced after the nominal forecast
dates, and three models are given the catches over the forecast horizon — an
advantage no real forecast has. Both asymmetries favour the structural side.

One context warning, moved here at the audits' request. The ladder's
one-dimensional maps cannot crash and then recover, so the collapse years are
not a fair contest between persistence and structure; they measure how large
the penalty is for a class that cannot generate the event. (The mathematical
statement of that obstruction is an open review item in the audit record; it
frames interpretation here, not proof.)

The result, on both estimated biomass series for this stock, held separate
throughout: nothing is retained. On the 2016-assessment series (1983–2015),
pooled one-year RMSE is 98 kt for persistence against 115–196 kt for the
structural models; at five years, 265 kt against 289–488 kt. On the extended
series (1954–2024), the origin-matched one-year figures are 84 kt for
persistence against 120 kt for the closest structural model; the mixed-origin
reading of the same persistence number is 88 kt, a training-window artefact
the paper discloses. From a fixed pre-collapse origin, every model misses the
1991–1995 collapse (694–819 kt against 670 and 688 kt for the baselines). A
prey-index module loses in every cell. The read is scoped plainly: on these
two series, under this rule, added structure did not earn its place — a
statement about this ladder, this estimator, and this scoring design, not
about the sustainability of the stock and not about surplus production in
nature.

**Keywords:** forecast evaluation; surplus-production models; northern cod;
rolling-origin; hindcasting; persistence benchmark; time series.

---

## 1. Introduction (humanized)

The fisheries literature asks constantly whether better models fit better.
This paper asks whether better models *forecast* better — the question that
matters for advice. Two features of the cod record make it a hard, honest
test. First, the stock collapsed in the early 1990s and partly recovered, so a
forecaster refit year by year meets two regimes (Hutchings & Myers 1994).
Second, two independently estimated series describe the same stock: the 2016
assessment's spawning-biomass series (1983–2015) and the extended 1954–2024
reconstruction. The design scores both, never mixes them, and reports where
each side of the contest has help: persistence inherits the reconstruction's
smoothness; the structural models receive future catches as a gift.

*(Frozen v50 sections on data, specifications, models Table 2, and equations
carry over verbatim at typesetting.)*

## 2. Design, in plain words

**The race, fixed in advance.** Persistence; the training mean; logistic
growth with a training-mean catch (M1); the same with a low-abundance penalty
(M1b); stock-flow with realised catches (M2); M2 with correlated errors (M3);
and M3 started one year late (M4). The order was declared before scoring.

**The scoring rule.** Pooled rolling RMSE at one and five years; retention
needs the persistence margin and the comparator margin, both beyond 5%, at
both horizons. Scores that are undefined for persistence by construction
(the 0/1 direction and Brier-type scores at h=1 on the short series) are
assigned 0.00 by convention — stated here, at first use.

**Who knew what, when.** The full table is carried verbatim from v50. One row
deserves its own sentence: for the collapse window, supplying the 1992 catch
drop to a constant-productivity map turns that run into a *policy-as-exogenous*
counterfactual, not a retention candidate on that window.

**The freeze, honestly.** The scoring core was fixed before the first primary
pass; later passes (annual-landings, survey-start, capelin, Specification B)
each carry their own archived freeze records. The unified band is the
instrument's stated rule.

## 3. Results (numbers frozen; narrative humanized)

*(Tables 3–8 and the DM/bootstrap table transplant verbatim, including the
v50 DM row note.)*

**Pooling hides regime detail.** Persistence wins the quiescent bands and
loses the collapse band on five origins — a window too small to score. The
fixed recovery-window row where M1b reads 90 kt against persistence's 104 is
reported as a fixed-window structural win the rolling-origin rule does not
score.

**The delay experiment, decomposed once.** At one year (short series), the
cost of the delay itself is about 86 kt (stale persistence 184 vs fresh 98);
the cost of the structural model given the delay is about 12 kt (stale M4
196 vs 184). At five years on the extended series, the model cost given the
delay dominates: 1030.7 for stale M4 against 337.4 for stale persistence and
300.0 for fresh persistence — the staleness penalty compounds through the
iterated dynamics, not through information loss alone. The constructive
reading, buried in v50's phrasing and surfaced by the audits: a timely trivial
forecast added more value at one year than any structure tested.

**Uncertainty is descriptive.** No short-series margin against persistence
has an interval excluding zero; several long-series margins do — against
structure.

## 4. Status notes (carried without expansion)

- Simulation operating characteristics belong to the framework companion, at
  its frozen values; this paper quotes the conclusion only (the rule recovers
  a true autonomous module in ~97% of replicates at collapse-window
  parameters and is weak for stock-flow and depensation alternatives).
- Rose (2026) is cited for reconstruction-level corroboration; bibliographic
  status to be locked at submission.
- Where "Table 1" appears, the typesetting pass prefixes the citation
  (this paper's Table 1 vs Regular et al. 2025 Table 1 vs Schijns et al.
  Table 1).

## 5. What this licenses

(1) On rolling-origin RMSE for these two series, under the frozen rule, no
tested structure earns its place. (2) The collapse-window outcome measures a
class misspecification penalty; it is not a discovery about forecasting
skill. (3) Nothing here says the stock is unsustainable, or that the ladder's
simple models are the best available. (4) Whether such a "no" is informative
depends on the scoring rule's measured behaviour against known truths; that
question is the framework companion's, and it is answered there with
operating characteristics.

## References (frozen strings from v50; verbatim)

# When does added model structure earn its place? A retention rule, an information-set audit, and two out-of-domain applications

**Reader-oriented restructuring draft (v27_reader_draft, 2026-09-17).**
Plain-prose re-expression of `paperF1_retention_framework_v26_restructured.md`,
in the conventions of its landmark references (Hyndman & Koehler 2006;
Diebold & Mariano 1995; Künsch 1989; Makridakis et al. 2020; Kell et al.
2016, 2021; Carvalho et al. 2021). **No number changes from v26.** `[carried]`
sections transplant verbatim at typesetting.

---

## Abstract (plain rewrite)

People add structure to forecasting models — drift terms, feedbacks,
covariates — faster than they test whether the additions predict. This paper
supplies the missing test as an explicit, reusable procedure, and then shows
what the procedure can and cannot certify. The procedure has three parts. (1) A
**retention rule**: rank the candidate models once, simplest first; a model is
kept only if it beats both the naive benchmark and the next-simpler model by
more than a small tie band, at one step and at a longer horizon alike. (2) An
**information-set audit**: for every quantity a model uses, record whether it
was knowable at the forecast origin or was supplied from the future — so that
a hindcast cannot masquerade as a forecast. (3) An **operating-characteristics
study**: before trusting any verdict, run the rule on artificial data where
the truth is known, and measure how often it recovers structure that is truly
there (power) and how often it refrains when nothing is there (specificity).
Applied unchanged to two unrelated systems — the Northern cod stock (two
biomass series) and the J-17 index well of the Edwards Aquifer — the rule
retains nothing: no structure earns its place on either. The operating-
characteristics study says when that matters: the rule recovers
threshold-growth dynamics in ~96% of replicates where such dynamics are
planted, and wrongly retains in only ~3–5% when persistence is the truth — so
the cod verdicts are informative exactly where the planted alternatives
resemble the candidates. Elsewhere power is low, and the same verdict there
would mean little. A finding with operating characteristics attached is a
different object from a bare score; supplying them is the standard this paper
proposes.

**Keywords:** model selection; retention rule; out-of-sample forecasting;
operating characteristics; hindcasting; information set; power; specificity.

---

## 1. Introduction (plain rewrite)

The forecasting literature has long known that accuracy measures can mislead
(Hyndman & Koehler 2006) and that simple methods are hard to beat at scale
(Makridakis et al. 2020). Hindcasting traditions in stock assessment (Kell et
al. 2016, 2021) and model-diagnostics guidance (Carvalho et al. 2021) ask for
out-of-sample evidence, but stop short of a decision rule one can freeze. The
gap this paper fills: a rule, frozen in advance, that converts pooled
out-of-sample scores into keep/discard decisions — and, crucially, a measured
account of the rule's own reliability on processes resembling the data at
hand. Without the second part, "the complex model lost" cannot be told from
"the test could not see complexity."

## 2. The rule in plain words

Any ordered list of models will do, so long as the order is fixed first. At
each origin every model is refit to the past and scored on the future; pooled
RMSE is the currency. A model is **retained** when it beats naive persistence
and its declared next-simpler comparator by more than the tie band, at both
horizons. The band exists so that a 0.2% numerical edge cannot masquerade as
evidence; the comparator gate exists so that beating persistence while losing
to a simpler cousin does not credit structure. The audit table then records,
per input, knowable-at-origin versus supplied-later; results are reported as
operational forecasts or conditional hindcasts accordingly, never ambiguously.

## 3. The operating characteristics in plain words

[carried: full simulation design from v26 §4 — D1–D5 in-class DGPs, D6–D7
out-of-class amendments, seeds pinned, rep counts (200/100/30), Wilson
discipline]

On artificial records where a collapse-type threshold model is truly at work,
the rule finds it almost always (D1, ~96%). Where recovery, smooth stock-flow,
or low-abundance penalties are the truth, it mostly cannot (D2–D4: 0–11%) —
and there the non-retention of a real mechanism says nothing about nature. On
persistence-generated noise it refrains over 95% of the time (D5 specificity),
with false retain well under one in twenty. Against out-of-class truths it
over-retains (D6/D7) — so specificity is a property of the rule *relative to
the candidate class*, a limitation stated, not fitted away. A simple
information criterion outperforms the rule on both axes (0.509/0.992 vs
0.373/0.973) in this suite; that comparison is reported as a result, and the
rule is kept for its transparent gate structure. Extensions at the longer
cod-series length and on Edwards-native generators are archived and registered
in the project's claims ledger [citable artifact; no duplication].

## 4. The two applications in plain words

[carried: §5 cod — two specifications, empty retained set, collapse-window
misses, catch-supplied generosity; §5 Edwards — point-rule vs unified-rule
M1 reading recorded per ledger CL-RULE-EDW-M1-DIFF; gate decomposition;
climate rung; recharge whiteness]

One rule, two unrelated physical systems, one verdict by different routes: on
cod nothing approaches the band; at the well, two margins beat persistence by
point score and are stopped — one by the band/comparator, one because the
structure literally reduces to the autoregression under realistic inputs. The
pair states the paper's thesis cleanly: structure earns its place only when a
fixed rule says so, and whether "no" is believable depends on the rule's
measured power in the relevant class.

## 5. What the pair licenses, and for whom

For the applied reader: a template — freeze the order, the benchmark, the
band, the audit table, and the power study before the first score table.
For the methods reader: a limit result — retention verdicts carry meaning
conditional on class and on measured operating characteristics; both are
operational requirements, not optional caveats.
For this project: the framework is the authority on instrument properties;
every domain number it cites is owned by a companion paper or an archive, one
claim at a time, as registered in the claims ledger.

## References (unchanged from v26) [carried]

# Does a surplus-production ladder improve forecasts of Northern cod? A scored test on NAFO 2J3KL

**Humanized version v52 (2026-09-17), Gemini-weighted style under the standing
style directive and accuracy firewall.** Implements the W1 (textual) items of
the joint evaluation of the Grok and Claude audits
(`audits_E1_E3/e1_audit_2026-09/E1_HUMANIZED_JOINT_EVALUATION_20260917.md`).
Every number replicates v50/claims-ledger values; the W2 scientific items
(Prop 4.1 restatement, Lemma 3.2, box-prior sensitivity, new analyses) are
open owner-gated items and are flagged, never silently repaired. `[carried]`
marks v50 text that transplants verbatim at typesetting.

---

## Abstract (v52 rewrite)

This paper scores five structural forecasting models and two naive baselines on
the Northern cod stock (NAFO Divisions 2J3KL), and reports a negative result
whose shape was partly known in advance. Three design choices should be stated
first, because they frame everything that follows. (1) A scoring rule was
written down before the scores were read: a structural module is kept only if
it beats naive persistence and the next-simpler module, by more than a 5% tie
band, at both one year and five years ahead, on error pooled over many rolling
forecast origins. (2) The biomass series being forecast is a reconstructed
assessment, not a raw observation; persistence inherits its smoothness, and
later versions of this evaluation note that the reconstruction embeds
information produced after each nominal forecast date. (3) Because the models
in the ladder are one-dimensional and roughly monotone, they cannot in
principle both crash and recover — so on the 1991–1995 collapse the test is
not a fair contest between persistence and structure; it measures how large
the penalty is for a class that cannot generate the event. (The mathematical
form of this obstruction is one of two scientific points currently under
review in the audit record; its role as *interpretation* is used here, not as
proof.)

With that framing: nothing is retained. On the shorter series (2016
assessment SSB, 1983–2015) pooled one-year RMSE is 98 kt for persistence
against 115–196 kt for the structural models; at five years, 265 kt against
289–488 kt. On the longer series (1954–2024 reconstruction), the
origin-matched one-year figures are 84 kt for persistence against 120 kt for
the closest structural module; the mixed-origin reading of the same
persistence number is 88 kt, and the 3–4 kt difference between the two
readings is a training-window artefact the paper reports rather than hides.
The result survives three forms of generosity to structure: future catches are
supplied along the forecast horizon (an advantage no operational forecast has);
a prey index is added as a candidate covariate (it loses in every cell); and a
second fixed-window design is examined (where the structural models are
sometimes better on five collapse-band origins — too few to score, and
explicitly not the retention question). The evaluation is a conditional
hindcast, not an operational forecast, and it is read as a statement about
this ladder and this estimator on these two series — not as a verdict on the
stock's sustainability, and not as a verdict on surplus production in nature.
What it does establish is small, testable, and negative: on this record, added
model structure did not earn its place under a rule fixed before the scores
were read.

**Keywords:** forecast evaluation; surplus production models; northern cod;
rolling-origin; hindcasting; persistence benchmark; time series. (Corrected:
v50's keyword "recruitment forecasting" removed — nothing in the paper
forecasts recruitment.)

---

## 1. Introduction (v52 rewrite)

*(Plain-prose version of v50 §1; facts unchanged.)*

**1.1 The question.** Does elaborating a forecasting model make it forecast
better? The fisheries literature usually answers by fitting a more complex
model and showing a better fit on the training record. This paper answers by
scoring predictions on data the models never saw, against a benchmark that
requires no fitting at all.

**1.2 Why this stock.** Northern cod collapsed in the early 1990s and partly
recovered; a forecaster fitted to its record confronts two regimes
(Hutchings & Myers 1994). Two independently estimated biomass series exist for
the same stock — a 1983–2015 series from the 2016 assessment and a 1954–2024
reconstruction from the most recent assessment model — and the design scores
both, separately. They are never pooled.

**1.3 What the reader should expect.** The stopping rule, the benchmark, the
tie band, and the audit of who-knew-what-when were fixed before scoring; the
paper's job is to report what happened, including where the design hands an
advantage to the structural side (future catch supplied) and where it hands
one to persistence (a smoothed predictand). One caution about the headline:
for the collapse years the ladder's one-dimensional maps cannot crash and
recover, so the collapse experiment is a measurement of the class's
misspecification penalty, not a discovery about skill — the audits asked that
this be said at the front, and it is said at the front.

[carried from v50: §1 remaining literature positioning; §2 data and
specifications (Tables 1, A2); the LRP definitions]

## 2. The seven rules and the ground rules (v52 rewrite)

**The ladder, in one sentence each:** (P) persistence — next year equals this
year; (M) the training mean; (M1) logistic growth with a training-mean catch;
(M1b) logistic growth with a low-abundance penalty term; (M2) stock-flow with
the actual catch each year; (M3) M2 with correlated errors; (M4) M3 started
one year late. [carried: exact equations and Table 2]

**The scoring rule, exactly as frozen:** pooled rolling RMSE at one and five
years; retention requires beating persistence AND the declared next-simpler
model by more than 5% at both horizons. **Conventions stated at first use**
(audit items): where a score is undefined for persistence by construction —
the 0/1 "direction" and Brier-type scores — the paper assigns 0.00 by
convention and says so when the score is introduced, not three pages later.

**Who knew what, when** [carried: information-set table]. The single row that
makes this a conditional hindcast is the supplied future catch, labeled here
at first mention: for the collapse window that run is a *policy-as-exogenous*
counterfactual — the 1992 catch drop is prescribed to a constant-productivity
map that must then rebound — not a candidate for retention on that window.

**Freeze discipline, honestly** (audit item): the scoring core was fixed
before the first score table was read; later passes (annual landings,
survey-start, capelin, Specification B) have their own freeze dates archived
with the harness. The abstract's sentence about the 5% band refers to the
unified rule used for retention decisions.

## 3. Results (structure carried from v50; readings v52)

[carried: Tables 3–8, the DM/bootstrap table, equations — numbers unchanged.
The A h=1 M4-vs-M3 DM row retains its v50 row note.]

Three readings, in plain words:

3.1 **Pooling hides regime detail.** Split by period [carried], persistence
wins the quiescent bands and loses the collapse band on five origins — a
window too small to score. The fixed recovery-window row where M1b scores 90
kt against persistence's 104 is reported as what it is: a fixed-window
structural win that the rolling-origin rule does not score, with the bolding
audit-noted (the table note says it is not a retention table).

3.2 **The delay experiment has a positive message, restated.** Decompose the
one-year-stale experiment into two quantities, defined once: the cost of the
delay itself (stale persistence 184 versus fresh persistence 98, about 86 kt)
and the cost of the structural model given the delay (stale M4 196 versus
stale persistence 184, about 12 kt). Read: an up-to-date trivial forecast
added far more value (86 kt) than any structure tested (≤ their deficits); at
h=5 on Specification B the model-cost-given-delay is the large term
(≈694 kt of the 989), so the staleness penalty compounds through the
dynamics, not through the information loss alone. (This restates v50 §4's
decomposition under the corrected labels from the audit.)

3.3 **Uncertainty is descriptive.** No Specification A margin against
persistence has an interval excluding zero; several Specification B margins
do, against the structural side. The one-origin influence on five-year scores
(the 1990 origin moves the persistence baseline from 265 to 193 kt in the
index-module origin set) is disclosed as an influence caveat; quantifying it
formally is a deferred analysis (W2).

## 4. Status notes carried without expansion (audit items)

- **Rose (2026)** is cited for reconstruction-level corroboration
  [carried §4]; its bibliographic status (published / in press / preprint with
  DOI) is to be locked at submission and is flagged here because two audits
  raised it. Where that corroboration load-bearing, the paper also cites
  DFO (2024a) and Regular et al. (2025).
- **Log-RMSE** rows exist because fitted trajectories can hit the floor at the
  fitted upper growth bound; the counts of floor-hitting origins and the
  ε-floor specification are deferred-reporting items (W2/W3), and the raw-RMSE
  tables remain primary.
- **"Table 1" phrase discipline.** Wherever "Table 1" appears, the draft's
  typesetting pass distinguishes this paper's Table 1 from Regular et al.
  (2025) Table 1 and Schijns et al. Table 1 by prefix.

## 5. What this licenses (v52)

Four statements, each within its evidence class:
(1) On rolling-origin RMSE for these two series, no tested structure earns its
place under the frozen rule. (2) The class-level obstruction on collapse is
measurement, not discovery — restated per audit, and its mathematical
statement is an open review item, not a load-bearing proof here. (3) Nothing
in the paper argues the stock is unsustainable, and nothing argues the
ladder's simple models are the best available; both readings are out of scope.
(4) Whether a "no" like (1) is informative depends on the decision rule's
measured behaviour against known truths — that operating-characteristics
question belongs to the framework companion, which owns it
(Abaee, retention-rule framework; claims ledger rows CL-INST-*).

## References [carried verbatim from v50 — frozen strings per style firewall]

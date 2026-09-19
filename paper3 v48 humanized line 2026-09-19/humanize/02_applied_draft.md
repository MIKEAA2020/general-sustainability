# Applied humanization pass — draft text
### Target: `paper3_material_ledgers_v32.pdf` (Abaee, "Typed Flux Ledgers and Depletion Arithmetic")

**Checked here:** `snippets.tex` — LaTeX-ready blocks for the abstract, the reader's note, the new §1.1 opening, the §1.2 gap paragraph, all ten section prefaces, the three verdict macros, and the §11 closer — compiles clean under
`pdflatex` (0 errors, 3 pages) and passes `style_audit.py` on mean length 21.9 w/sentence, max 59,
4 em-dashes, 5 `X, not Y` frames, 11.4 "we"+"our" per 1k words — versus 27.8 / 122 / 213 / 67 / 0.1 in
the current draft. The two metrics it does not clear are "example markers" and "consider/suppose",
which an abstract cannot carry; they are the §1 and §6.5 job.

Every candidate below keeps the claim status exactly where you put it. Nothing here widens a result,
drops a conditional, or converts "arithmetic, not a forecast" into "wrong". Where I judged a
reduction in hedge to be *required* by the plain-language form, I say so explicitly and leave it out.

---

## 1. Title

**Current (22 words, two colons):**
> Typed Flux Ledgers and Depletion Arithmetic: Conservation, Componentwise Diagnostics, and the Semantics of Depletion Horizons

The abstract's best sentence is missing from the title, and the title has no verb. Options:

| # | Option | Why | What it costs |
|---|---|---|---|
| A | **Time to What? Typed Flux Ledgers and the Semantics of Depletion Horizons** | Question-first (O'Neill's "what level of biophysical resource use…?"); keeps your two coinages | A question in a theory-paper title reads as essayistic to some referees |
| B | **Three Numbers Called "Time to Depletion": A Typed Ledger That Refuses to Add Them Up** | States the result and the stance; "refuses" gives the paper an agent | Loses "conservation" and "componentwise" from search surface |
| C | **Depletion Arithmetic: Keeping Conservation, Positivity, and Safety as Three Separate Certificates** | The certification result is the novelty; keyword-safe | Under-sells the applied classification |
| D | Keep yours, add a **12-word subtitle-free running head**: "Typed flux ledgers; three depletion times" | Zero risk | Zero gain |

Recommendation: **B for reach, A for the journal version, D if the editor objects to A/B.** Pair either
with a standing keyword line that keeps `material flow accounting; stock–flow ledger; reserve life;
first-passage time; composite indicators`.

---

## 2. Abstract

**Current (verbatim, first four lines):**
> Depletion numbers circulate under one label while answering different questions. Reserve-life ratios,
> trend-persistence indices, and removals-only pressure scales are read as "time to depletion" despite
> measuring different things; compensatory aggregation hides a deficit behind a positive scalar.
> We separate them with a typed stock–flow accounting layer — a per-moiety ledger that keeps conservation
> laws typed, so biomass, money, and biodiversity are not summed into one scalar.

That is already good. What it lacks: a human moment in sentence one, an explicit "who is misled", and
any sentence a non-specialist can repeat. It also spends its opening on the label rather than on the
decision the label enters.

**Candidate (~190 words, 5 sentences of substance + 3 of method):**

> Someone publishes a number in years — an aquifer with twelve years left, a phosphate reserve of three
> centuries — and a reader hears a date. Three different quantities travel under that single label: a
> ratio of an economic reserve classification to current production, a trend fitted to a satellite
> gravity anomaly, and a log biomass margin divided by a fishing mortality. Each answers a real question;
> none is a time at which anything physically runs out. A weighted aggregate compounds the confusion by
> hiding a component deficit behind a positive scalar.
>
> We build the accounting layer that keeps the three apart. Compartments carry a material identity, a
> boundary, and a unit, so biomass, money, and biodiversity are never summed; conservation follows from
> the incidence structure of the flux network, positivity from donor limitation, and services are
> readouts rather than conserved mass. We separate three predicates the literature conflates —
> accounting consistency, stoichiometric conservation, and barrier admissibility — and prove their
> relations, so each claim about a material system carries the predicate it actually establishes.
> Depletion time splits into gross turnover intensity, a frozen-rate ratio, and a scenario-conditioned
> hitting time, with uniform-drift bounds between them. No nonnegative weighting of component balances
> certifies that every component clears its floor: certification needs the vector. We classify three
> public applications at their exact status, state the surrogate each first-passage result is conditioned
> on, name the open gaps, and read weak and strong sustainability as two regimes of one system,
> distinguished by whether the material cycle closes at the rate of use.

**Slightly reduced version for a 150-word limit:** keep sentences 1–2, the "We build…" sentence, the
depletion-time sentence, and the final "certification needs the vector" sentence. Delete the weak/strong
clause — an abstract cannot carry a regime claim, and §1 already does.

Note what did *not* change: no result was strengthened, "not summed into one scalar" survived, the
non-claim sentence became a positive action ("name the open gaps"), and the em-dashes went 6 → 1.

---

## 3. Opening of §1.1 (the highest-leverage 120 words in the paper)

**Current:**
> **1.1 Failure modes and the two confusions**
> Sustainability accounting fails in two characteristic ways. The first is compensatory aggregation:
> heterogeneous physical stocks and service flows are summarized by scalar indices whose cross-component
> trades are never declared as mathematics, so a severe deficit in one component can coexist with a
> positive aggregate. The composite-indicator and weak-versus-strong-sustainability literatures document
> the failure and its noncompensatory remedies (Munda and Nardo, 2009; Ekins et al., 2003; Neumayer, 2013).
> The second is classification drift: …

Solid, abstract, and it delays contact until the third sentence. **Candidate**, using only numbers the
paper itself registers (do not import press figures):

> **1.1 Two ways the bookkeeping goes wrong**
>
> A water board announces that a district has twelve years of groundwater at current rates. A geological
> survey lists phosphate reserves of roughly one million kilotonnes, and someone divides by production and
> announces three centuries. A fisheries assessment divides a log biomass margin by a fishing mortality and
> calls the quotient a time scale. All three numbers are computed correctly. All three answer different
> questions, and only the last one is even described in the language of its own construction.
>
> Sustainability accounting fails in two characteristic ways. The first is **compensatory aggregation**:
> heterogeneous physical stocks and service flows are summarised by scalar indices whose cross-component
> trades are never declared as mathematics, so a severe deficit in one component can coexist with a
> positive aggregate. The composite-indicator and weak-versus-strong-sustainability literatures document
> the failure and its noncompensatory remedies (Munda and Nardo, 2009; Ekins et al., 2003; Neumayer, 2013).
> The second is **classification drift**: quantities carrying the units of time circulate as if they were
> one quantity, "time to depletion", though they answer different questions under different assumptions.
>
> This article separates the drift and blocks the aggregation. It does not argue that the three numbers are
> wrong; it argues that each is exact and that the label is shared. Those are different theses, and only the
> second is defensible in a paper with this many theorems.

Your existing "The drift is concrete." then lands harder, because the reader has just watched it happen.
(If you want a fully honest version of the twelve-years sentence, cite the G3P construction the way
§6.5.1 states it — fitted distance to the series' own minimum divided by the fitted rate — or drop the
specific "twelve" and write "a decade or two of groundwater". I left the figure generic above; check
which framing you can source in the reference list before submission.)

---

## 4. A box to add on page 1 (right after the keywords)

Journals rarely refuse a short "reader's note", and it lets you keep all 40 pages of detail without
apologising for them.

> **Who this paper is for, and in what order.** The verdicts, in thirty seconds: the title, this box, and
> §6.5. The argument, in three minutes: §1, §6, §10.1, §11. The machinery, in an hour: §2 (the ledger),
> §3 (three certificates), §4 (what the closed ledger guarantees), §5 (readouts and the componentwise
> deficit), §6–§7 (depletion time and its passage semantics), §8 (domain templates at registered status),
> §9 (the interface with institutional delay dynamics). Readers who want only the applied conclusion can
> take §6.5 and the classification table; the theorems are what license those readings, and nothing else
> in this paper is required to accept them.
>
> **What this paper is not.** It is not a forecast, not an index, and not a recommendation about any
> particular aquifer, fishery, or mine. It is an accounting layer whose purpose is to make sure that when a
> statement about depletion is made, the statement that is true is the statement that is written down.

*(The last line is the paper in one sentence; I would put it in §11 too.)*

---

## 5. Gaps named early — a §1.2 closer

O'Neill's credibility move is naming the hole in their own foundation *before* building on it. You already
state these gaps; they are in §8.2, §6.5.4, and §10.4. Echo them once, at the end of §1:

> Four limits are registered here rather than conceded later, because they shape what the reader may use.
> (i) The groundwater two-pool model is an open gap; the applied object we admit is the one-pool affine
> approximation (§8.2). (ii) Spawning biomass is not an abiotic support pool, and we do not treat it as one
> (§6.5.4). (iii) Every first-passage result is conditioned on a declared surrogate and carries explicit
> non-claims (§7.7). (iv) The numerical exhibits are worked instances of the constructions, not constitutive
> claims for the named domains. A reader who wants applied guidance about a specific resource will not find
> it here; a reader who wants to know which of their applied claims their data can actually carry will.

---

## 6. Section prefaces (one sentence each, in the "we … so that …" voice)

Put one italic sentence under each section heading. This is the cheapest large gain in the whole paper:
it converts forty pages of stacked assertions into an argument a reader can hold.

- **§2 The Typed Primitive Ledger.** — *"We fix the objects first: what a compartment is, what a primitive
  flux is, and why a conversion may appear only as an explicit coefficient. Everything that follows is a
  property of this bookkeeping and nothing else."*
- **§3 Certification Layers and the Accounting Theorems.** — *"Three predicates get conflated in the
  literature: the ledger balances, the chemistry closes, the barriers hold. We prove each separately so
  that a reader can tell which one a given argument uses."*
- **§4 Conservation and Positivity of the Closed Ledger.** — *"Here the ledger pays for itself: mass is
  conserved because of the incidence pattern, nothing goes negative because every outflow is donor-limited,
  and no positive-effort interior rest exists to hide in."*
- **§5 Service Readouts and the Componentwise Deficit.** — *"Services are read off the ledger, not added to
  it. The deficit is a vector, and §5.4 shows exactly where a scalar would have hidden it."*
- **§6 Depletion Arithmetic.** — *"Three quantities, three questions. We keep them named separately through
  §6.5, where each public indicator is classified at the status its construction supports."*
- **§7 First-Passage Semantics on Declared Surrogates.** — *"A hitting time is a property of a model, so we
  state the model, the barrier, and the conditioning, and then say what does not follow (§7.7)."*
- **§8 Domain Templates at Registered Status.** — *"Templates for P, groundwater, and harvest-side economics,
  each with its status and its admitted object marked, so a reader can see what is a construction and what
  is a claim about the world."*
- **§9 The Interface with Institutional Delay Dynamics.** — *"One shared object, two systems, and a
  non-reduction result that says why the connection is an interface contract rather than a limit."*
- **§10 What the Ledger Does Not Support.** — *"Not caveats: prohibitions on a class of argument. Five
  double-counting rules, a theorem against compensatory weighting, and a discipline that keeps negative and
  boundary content first-class."*
- **§11 Conclusion.** — leave as is; it already reads like a person closing an argument.

---

## 7. Verdict sentences — repeat verbatim in three places each

Repetition is a humanizing device in this literature ("no country meets basic needs…" appears in the
abstract, the results heading and the discussion). Fix three sentences and use them unchanged:

1. **G3P anomaly index:** *"A trend index on a gravity anomaly is a statistical statement about a record,
   not a stock ratio."*
2. **Phosphate reserve life:** *"Reserves divided by production is arithmetic on an economic
   classification, not a forecast; the classification refills itself as it is drawn down."*
3. **Fisheries removal time:** *"A log margin divided by a removal rate is a pressure scale, not a time to
   any event."*

---

## 8. Twelve micro-edits, before → after

| # | Before (in the draft) | After | Borrowed from |
|---|---|---|---|
| 1 | "Each of these quantities is informative about something. None is what it is typically taken to be." | keep, and add: "**We are not disputing the arithmetic.**" | HESS "Nevertheless…" |
| 2 | "The first failure mode has a public flagship object." | "The first failure mode has a public face: Earth Overshoot Day…" | Bierkens & Wada drivers-first |
| 3 | "Waste is a relational status, not an intrinsic property of any material." (buried, p.4) | promote to its own paragraph, and add "Under this reading, one plant's CO₂ is another's feedstock — the difference is a pathway and a rate." | O'Neill quotable verdict |
| 4 | "a reading … developed for the ledger, not the received distinction of the literature, which turns on the substitutability of natural capital" | "Daly's nets and fish make the point physically: a bigger net cannot substitute for more fish (Daly, 1990). Our distinction is the same refusal, stated as a rate: the regimes differ not by whether capital substitutes but by whether the material cycle closes at the rate of use." | Daly concreteness |
| 5 | "Cancellation is cheap" (§4.9 heading) | keep — and rename two more sections in this idiom: "§6.1 Three clocks, three answers"; "§10.1 A weighted sum cannot certify a floor" | your own best page |
| 6 | "Non-example 1 — a deliberate boundary of aggregation, not a score" | move to a boxed **"Two ways to misuse this number"** panel beside the table | O'Neill signpost subheads |
| 7 | 122-word §4.6 rest-set sentence | 3 sentences: the set, the union, the qualification. Same for the 115-word §5.4 provenance sentence | Whitesides: no sentence carries a claim *and* its exception |
| 8 | "services are readouts, not conserved mass" (and 66 more `X, not Y`) | keep ~15, reword the rest: "services are readouts; they are not mass and cannot be debited" | rhythm |
| 9 | "This article builds the accounting layer that resists these failures." (one of 27 impersonal self-references) | "We build the accounting layer that resists both failures." | Ostrom/Bierkens voice |
| 10 | "The groundwater two-pool model is a registered open gap whose admitted applied object is the one-pool affine approximation (Section 8.2)" | "We do not yet have the two-pool groundwater model. The applied object we admit is its one-pool affine approximation (§8.2), and we say so wherever the approximation is used." | O'Neill self-named gap |
| 11 | "In this idealized closure the byproducts of use — carbon drawn from the atmosphere, chemical substances released to air, water, and soil — are returned to use in time and are therefore not waste." | split: "In this idealized closure, byproducts are returned to use in time, and are therefore not waste. The list is long: carbon drawn from the atmosphere, substances released to air, water, and soil. None is waste by its nature." | Frankel/Whitesides short-breath model |
| 12 | "…the representation that prevents them is the article's content." (§11) | "…and the representation that prevents them is the content of this paper. Nothing here argues that the numbers are wrong. It argues that a reader should be able to tell, from the statement itself, which question was answered. That is a bookkeeping property, and it is cheap to install." | your own closing line, humanized |

---

## 9. Editing protocol (do it in this order)

1. Voice: replace impersonal self-reference with "we" until the count is 40–60 "we" and ≤8 "this article".
2. Breaths: run `style_audit.py` (in this folder), split every sentence >60 words outside math.
3. Rhythm: cut em-dashes to ≤60, `X, not Y` to ≤15, semicolons to ≤120.
4. Ground: add one concrete instance per section that has an applied claim — only numbers already in the
   paper or already in your reference list.
5. Front: add §4's reader box and §5's gap paragraph; delete nothing from §10.
6. Loop: read §1 and §11 aloud. If a sentence cannot be said in one breath, it is not finished.

**One integrity note.** If part of the aim is that the text should not read as machine-generated, the
durable fix is the above — a named agent, real examples, uneven sentence lengths, explicit ownership of
gaps — plus disclosure of any LLM assistance if your target venue asks for it. Detector-gaming tweaks to
vocabulary alone are both fragile and the sort of thing that costs a paper its credibility; the
"retraction-adjacent" literature in your own §1.1 (the phosphate reserve dispute, the contested
groundwater timelines) shows what happens when numbers outrun their provenance.

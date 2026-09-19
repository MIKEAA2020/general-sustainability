# Claim ledger over the draft’s non-shared sentences

Written by `claim_ledger_v1.py`, pairs only. It does not rewrite, merge, repair or reword anything, and the
adjudication line under each entry is left blank for the author.

**What was paired.** The draft’s body prose, `paper3_humanized_v1_full.md`, against the deposited article,
`paper3_material_ledgers_v42.md`. 719 draft sentences were extracted from 292 body blocks; 161 of
them are verbatim sentences of the deposit and were excluded as pairs, because where the wording is shared there is
nothing to adjudicate - the first pass of this audit measured 0 hedges, 0 quantifiers and 0 values out of place in
the paragraphs the two files share outright. The other 558 sentences are the ledger.
They are paired through an alignment: 164 of 292 draft blocks sit opposite a deposit block, and a sentence
is checked against the **whole aligned passage** rather than one sentence, because a hedge or a condition can live
in the neighbouring sentence and a comparison that misses that reports faithful plain-language writing as a change
of claim.

**The rules that produced each verdict.**

| verdict | fires when |
|---|---|
| `excluded: shared verbatim` | the sentence is the deposit’s own wording, character for character |
| `not a claim (signposting)` | the sentence reports what the document does (this section, we defer to, the appendix holds) |
| `supported (near-verbatim)` | a partner passage was found and its overlap with the sentence is high |
| `supported (reworded)` | a partner passage was found and no marker differs |
| `needs check: strength` | the passage hedges and the sentence asserts, with a universal, a causal verb or a value |
| `needs check: scope` | the passage states a condition, population or limit the sentence drops |
| `needs check: attribution` | the passage names a source the sentence drops, or the sentence names one the passage lacks |
| `needs check: inference` | the sentence opens on *therefore, thus, because* and the passage asserts no consequence |
| `contradicted: value` | the sentence states a figure the deposit never states anywhere in the file |
| `contradicted: causality` | the passage says association and the sentence says cause |
| `unsupported: no partner located` | no deposit passage shares enough content with the sentence to be its original |

**Confidence** is printed with every entry: `high` above 0.60 character ratio or 0.45 token overlap, `medium` above
0.18 overlap, `low` below. Low confidence here usually means the draft wrote a technical sentence in plain English,
which is the operation the draft was asked to perform; it is printed rather than hidden so the author can see how
much of the ledger rests on a thin pairing.

**What the counts say.** 463 of the 558 ledgered sentences - 82% - restate a deposit proposition with no marker out of place, and 0 contradict the deposit on a value or on the direction of a claim (0 on a figure, 0 on association turned into cause). 63 sentences differ from their original in force, condition or attribution and are listed below for an adjudication; 1 are sentences the deposit does not contain at all. The value test reads the deposit’s maths, so a figure the draft spells out that the paper wrote as `$6 \times 10^5$` is recognised as the same figure and not reported as invented. Nothing in this ledger is a correction: it is the list of places where the draft said something the paper did not, or said it with different force, which is what a policy choice is made from.

---


**A strict census, so the zero reads as a measurement and not a claim.** Running these same sentences with the aligned passage no longer answering for the sentence - a figure has to sit in the matched sentence itself, a hedge or a condition too - moves 1 rows out of `supported` into a flag, 0 of them into a contradiction. That is what the shipped tolerances buy: a divergence visible only against a sentence the alignment pairs loosely is left to the passage to answer for, and the pair is printed either way so the author sees it.

## Counts

| verdict | sentences |
|---|---|

| `supported (reworded)` | 263 |
| `supported (near-verbatim)` | 200 |
| `excluded: shared verbatim` | 161 |
| `not a claim (signposting)` | 31 |
| `needs check: attribution` | 28 |
| `needs check: strength` | 18 |
| `needs check: scope` | 12 |
| `needs check: inference` | 5 |
| `unsupported: no partner located` | 1 |

confidence over the ledgered rows: high 338, medium 210, low 10


---

## The 64 pairs that need an adjudication, most severe first

### D0081 · unsupported: no partner located · draft §1.1 · confidence medium · overlap 0.212, ratio 0.237, paired through the elsewhere in the deposit

**Draft, the claim as the draft makes it.**

> That is why support drawdowns cannot be traded against revenue anywhere in the ledger.

**Deposit, the proposition it corresponds to** (§1.3):

> Section 10 states what the ledger does not support, and Section 11 concludes.

- *recorded, not judged* - nothing in the deposit shares enough content words with this sentence to be its original

<details><summary>the whole aligned passage</summary>

> Section 2 defines the typed ledger. Section 3 develops the certification layers and the accounting theorems. Section 4 proves the closed-ledger theorem set. Section 5 adds the service layer and the componentwise deficit. Section 6 develops the depletion taxonomy, the uniform-drift bounds, and the application classifications. Section 7 supplies first-passage semantics. Section 8 records the domain templates at registered status. Section 9 fixes the interface with delay dynamics. Section 10 states what the ledger does not support, and Section 11 concludes.

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0005 · needs check: attribution · draft §front · confidence high · overlap 0.552, ratio 0.663, paired through the elsewhere in the deposit

**Draft, the claim as the draft makes it.**

> Each thing in the ledger has a material identity, a container with a boundary, and a unit.

**Deposit, the proposition it corresponds to** (§1.2):

> 1. A typed primitive-flux ledger. Compartments carry a material identity, a boundary, and a unit.

- *needs check: attribution* - the sentence this one restates cites Brunner & Rechberger, 2004; the draft dropped the source
- *recorded, not judged* - polarity phrased differently (passage no negator, draft ['cannot', 'not'])

<details><summary>the whole aligned passage</summary>

> 1. A typed primitive-flux ledger. Compartments carry a material identity, a boundary, and a unit. Non-negative primitive fluxes connect them through a signed incidence matrix (the compartment–flux bookkeeping of material flow analysis: Brunner and Rechberger, 2004; Fischer-Kowalski et al., 2011; the incidence formalism of reaction-network theory: Feinberg, 2019). Conversions between types appear only as explicit stoichiometric coefficients. Every one-way transfer is donor-limited.

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0043 · needs check: attribution · draft §1.1 · confidence high · overlap 0.545, ratio 0.062, paired through the elsewhere in the deposit

**Draft, the claim as the draft makes it.**

> The second failure is classification drift: *a number that is described one way gets read as something else.* Several quantities have "years" in their units — reserve-life ratios, trend-persistence indices, removals-only pressure scales — and circulate as if they were one thing: "time to depletion".

**Deposit, the proposition it corresponds to** (§1.1):

> The second is *classification drift*: quantities with the units of time — reserve-life ratios, trend-persistence indices, removals-only pressure scales — circulate as if they were one thing, "time to depletion," when they answer different questions under different assumptions.

- *needs check: attribution* - the sentence this one restates cites Munda & Nardo, 2009; the draft dropped the source

<details><summary>the whole aligned passage</summary>

> Sustainability accounting fails in two characteristic ways. The first is *compensatory aggregation*: heterogeneous physical stocks and service flows are summarized by scalar indices whose cross-component trades are never declared as mathematics, so a severe deficit in one component can coexist with a positive aggregate. The composite-indicator and weak-versus-strong-sustainability literatures document the failure and its noncompensatory remedies (Munda and Nardo, 2009; Ekins et al., 2003; Neumayer, 2013). The second is *classification drift*: quantities with the units of time — reserve-life ratios, trend-persistence indices, removals-only pressure scales — circulate as if they were one thing, "time to depletion," when they answer different questions under different assumptions.

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0088 · needs check: attribution · draft §1.1 · confidence high · overlap 0.723, ratio 0.803, paired through the elsewhere in the deposit

**Draft, the claim as the draft makes it.**

> Spawning biomass is explicitly not an abiotic support pool (Section 6.5.4).

**Deposit, the proposition it corresponds to** (§6.5.4):

> Spawning biomass is not an abiotic support pool.

- *needs check: strength* - the passage hedges with ['would']; this sentence asserts without a hedge
- *needs check: attribution* - the sentence this one restates cites Ricard, 2012; the draft dropped the source

<details><summary>the whole aligned passage</summary>

> The fisheries column of the classification matrix is the removals-only pressure time. When and , define and the fishing-only time-to-reference: the crossing time of the deliberately incomplete comparison process . With this is the construction tabled as ADH in Section 6.5.2; the two notations are kept because the boundary hypotheses stated here ( , ) are exactly the conditions of the positive sub-cohort of Section 6.5.2 (35 stocks, median yr); the reported Section 6.5.2 median ( yr) additionally carries the eight zero entries for stocks at or below the reference, per the zero convention of the source caption. It is a removals-only pressure time scale — the time unit comes from rescaling a stock-reference margin by one isolated gross-loss rate. Because recruitment, somatic growth, maturation, natural mortality, density dependence, environmental forcing, and future policy are omitted, is not a net biomass depletion diagnostic, not a demographic hitting-time estimate, and not a member of the – – hierarchy. A genuinely local biomass-decline ratio would require a compatible net estimate, and a demographic hitting time a fully specified population model; RAM Legacy SSB and data (Ricard e

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0116 · needs check: attribution · draft §front · confidence medium · overlap 0.426, ratio 0.522, paired through the elsewhere in the deposit

**Draft, the claim as the draft makes it.**

> 1. bookkeeping balance — the accounts add up; 2. stoichiometric conservation — the declared materials are conserved by construction; 3. thermodynamic admissibility — the flows are physically possible; 4. sustainability safety — the declared limits hold.

**Deposit, the proposition it corresponds to** (§1.1):

> But bookkeeping balance, stoichiometric conservation, thermodynamic admissibility, and sustainability safety are four different predicates, and the literature routinely slides between them.

- *needs check: attribution* - the sentence this one restates cites Feinberg, 2019; the draft dropped the source

<details><summary>the whole aligned passage</summary>

> The same conflation pervades accounting itself. Material flow analysis supplies the bookkeeping of society's material throughput (Brunner and Rechberger, 2004; Eurostat, 2001; Fischer-Kowalski et al., 2011). Its incidence structure is shared with reaction-network theory, where the sign pattern of the stoichiometric matrix is a conservation object (Feinberg, 2019). But bookkeeping balance, stoichiometric conservation, thermodynamic admissibility, and sustainability safety are four different predicates, and the literature routinely slides between them. A mass-balanced ledger can be chemically impossible. A chemically consistent ledger can violate every declared barrier. A ledger satisfying all declared barriers can fail conservation. Separating these layers and proving their relationships, so that each claim about a material system carries the predicate it actually establishes, is this article's first task (Section 3).

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0133 · needs check: attribution · draft §1.2 · confidence high · overlap 0.713, ratio 0.805, paired through the aligned passage

**Draft, the claim as the draft makes it.**

> It applies only to the slow compartments: geological donors and mineral stocks, which renew on deep time.

**Deposit, the proposition it corresponds to** (§1.1):

> The deep-time clause is scoped to the slow compartments — geological donors and mineral stocks, whose renewal runs on deep time.

- *needs check: attribution* - the sentence this one restates cites Daly, 1990; the draft dropped the source

<details><summary>the whole aligned passage</summary>

> The third task is to locate substitution within the ledger, rather than alongside it. Weak and strong sustainability are not competing hypotheses but two regimes of one dynamic system, distinguished not by whether substitution alone keeps pace with depletion but by whether the material cycle can be closed at the rate of use — a reading of the two regimes developed for the ledger, not the received distinction of the literature, which turns on the substitutability of natural capital (Neumayer, 2013; Ekins et al., 2003). Weak sustainability is the idealized regime: humans consume and populate slowly enough that technological substitution and natural regeneration together redistribute matter so that it is used as it arises. On human-relevant timescales substitution is the dominant term; natural regeneration acts far more slowly — often on deep-time scales — and is included for physical completeness rather than as a co-equal mechanism (Daly, 1990). The deep-time clause is scoped to the slow compartments — geological donors and mineral stocks, whose renewal runs on deep time. The regenerative compartments this article's applied record tabulates renew on human timescales — a crop within a

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0140 · needs check: attribution · draft §1.2 · confidence high · overlap 0.798, ratio 0.855, paired through the aligned passage

**Draft, the claim as the draft makes it.**

> *Strong sustainability* is the regime where the closure fails: either because no identified physical pathway re-routes the extracted matter, or because depletion outruns the rate at which such a pathway could be built.

**Deposit, the proposition it corresponds to** (§1.1):

> Strong sustainability is the regime in which that closure fails — either because no identified physical pathway re-routes the extracted matter, or because depletion outruns the rate at which such a pathway could be deployed (Neumayer, 2013; Ekins et al., 2003).

- *needs check: attribution* - the sentence this one restates cites Neumayer, 2013; the draft dropped the source

<details><summary>the whole aligned passage</summary>

> Strong sustainability is the regime in which that closure fails — either because no identified physical pathway re-routes the extracted matter, or because depletion outruns the rate at which such a pathway could be deployed (Neumayer, 2013; Ekins et al., 2003). Substitution is admissible only where an identified physical pathway exists and does not draw down a different critical stock. No substitute is admitted merely because an aggregate production function or a weighted index permits it. In ledger terms, a substitute is either a recycled or recovered flux returned to the regenerating pool, or a non-renewable drawdown on a second compartment. The two are different ledger entries and carry different statuses (Section 2.3, Section 6).

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0141 · needs check: attribution · draft §1.2 · confidence high · overlap 0.917, ratio 0.829, paired through the aligned passage

**Draft, the claim as the draft makes it.**

> Substitution is admissible only where a physical pathway has been identified and does not draw a different critical stock down.

**Deposit, the proposition it corresponds to** (§1.1):

> Substitution is admissible only where an identified physical pathway exists and does not draw down a different critical stock.

- *needs check: attribution* - the sentence this one restates cites Neumayer, 2013; the draft dropped the source

<details><summary>the whole aligned passage</summary>

> Strong sustainability is the regime in which that closure fails — either because no identified physical pathway re-routes the extracted matter, or because depletion outruns the rate at which such a pathway could be deployed (Neumayer, 2013; Ekins et al., 2003). Substitution is admissible only where an identified physical pathway exists and does not draw down a different critical stock. No substitute is admitted merely because an aggregate production function or a weighted index permits it. In ledger terms, a substitute is either a recycled or recovered flux returned to the regenerating pool, or a non-renewable drawdown on a second compartment. The two are different ledger entries and carry different statuses (Section 2.3, Section 6).

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0197 · needs check: attribution · draft §2.1 · confidence high · overlap 0.609, ratio 0.766, paired through the elsewhere in the deposit

**Draft, the claim as the draft makes it.**

> A conversion between types is an explicit stoichiometric coefficient, never an implicit sum.

**Deposit, the proposition it corresponds to** (§1.2):

> Conversions between types appear only as explicit stoichiometric coefficients.

- *needs check: attribution* - the sentence this one restates cites Brunner & Rechberger, 2004; the draft dropped the source
- *recorded, not judged* - polarity phrased differently (passage no negator, draft ['never'])

<details><summary>the whole aligned passage</summary>

> 1. A typed primitive-flux ledger. Compartments carry a material identity, a boundary, and a unit. Non-negative primitive fluxes connect them through a signed incidence matrix (the compartment–flux bookkeeping of material flow analysis: Brunner and Rechberger, 2004; Fischer-Kowalski et al., 2011; the incidence formalism of reaction-network theory: Feinberg, 2019). Conversions between types appear only as explicit stoichiometric coefficients. Every one-way transfer is donor-limited.

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0210 · needs check: attribution · draft §2.2 · confidence high · overlap 0.58, ratio 0.646, paired through the aligned passage

**Draft, the claim as the draft makes it.**

> These donor primitives instantiate one of three recharge laws that appear across this article and the companion delay-dynamics analysis (Author, D., et al., *in review*).

**Deposit, the proposition it corresponds to** (§2.2):

> These donor primitives instantiate one of three recharge laws that appear across this article and the companion delay-dynamics analysis (Abaee, 2026a, doi:10.5281/zenodo.22554217); the three are distinct objects, tabulated once so that none is silently substituted for another:

- *needs check: attribution* - the sentence this one restates cites Abaee, 2026; the draft dropped the source

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0262 · needs check: attribution · draft §front · confidence medium · overlap 0.381, ratio 0.374, paired through the elsewhere in the deposit

**Draft, the claim as the draft makes it.**

> Then , and the sink exceeds any finite ceiling in finite time. 2. Weak assimilation ( ).

**Deposit, the proposition it corresponds to** (§2.4):

> With sink loading , assimilation , and a harvest floor (in the four-stock specialization, and ): under *no assimilation* ( ), , and the sink exceeds any finite ceiling in finite time; under *weak assimilation* ( ), the sink load at the ceiling is still positive — at — so exits above in finite time, the explicit negation of the ceiling condition with .

- *needs check: attribution* - the sentence this one restates cites Aubin, 1991; the draft dropped the source

<details><summary>the whole aligned passage</summary>

> Sink obstructions independent of the stock. The mass balance has a sink-side physical reading with two empty-kernel mechanisms that operate whatever the resource stock does. With sink loading , assimilation , and a harvest floor (in the four-stock specialization, and ): under *no assimilation* ( ), , and the sink exceeds any finite ceiling in finite time; under *weak assimilation* ( ), the sink load at the ceiling is still positive — at — so exits above in finite time, the explicit negation of the ceiling condition with . In both cases the viability kernel (Aubin, 1991) of the constraint set — the states from which some admissible harvest keeps both constraints for all time — is empty. The obstruction needs the sink-generation fraction : if , harvest never loads the sink and the loading argument does not apply — emptiness would then have to come from the resource constraint or an undeclared ceiling on the product stock.

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0263 · needs check: attribution · draft §front · confidence medium · overlap 0.429, ratio 0.205, paired through the elsewhere in the deposit

**Draft, the claim as the draft makes it.**

> The sink load at the ceiling is still positive: at , so exits above in finite time.

**Deposit, the proposition it corresponds to** (§2.4):

> With sink loading , assimilation , and a harvest floor (in the four-stock specialization, and ): under *no assimilation* ( ), , and the sink exceeds any finite ceiling in finite time; under *weak assimilation* ( ), the sink load at the ceiling is still positive — at — so exits above in finite time, the explicit negation of the ceiling condition with .

- *needs check: attribution* - the sentence this one restates cites Aubin, 1991; the draft dropped the source

<details><summary>the whole aligned passage</summary>

> Sink obstructions independent of the stock. The mass balance has a sink-side physical reading with two empty-kernel mechanisms that operate whatever the resource stock does. With sink loading , assimilation , and a harvest floor (in the four-stock specialization, and ): under *no assimilation* ( ), , and the sink exceeds any finite ceiling in finite time; under *weak assimilation* ( ), the sink load at the ceiling is still positive — at — so exits above in finite time, the explicit negation of the ceiling condition with . In both cases the viability kernel (Aubin, 1991) of the constraint set — the states from which some admissible harvest keeps both constraints for all time — is empty. The obstruction needs the sink-generation fraction : if , harvest never loads the sink and the loading argument does not apply — emptiness would then have to come from the resource constraint or an undeclared ceiling on the product stock.

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0267 · needs check: attribution · draft §front · confidence high · overlap 0.823, ratio 0.859, paired through the elsewhere in the deposit

**Draft, the claim as the draft makes it.**

> If , harvest never loads the sink and the loading argument does not apply; emptiness would then have to come from the resource constraint or from an undeclared ceiling on the product stock.

**Deposit, the proposition it corresponds to** (§2.4):

> The obstruction needs the sink-generation fraction : if , harvest never loads the sink and the loading argument does not apply — emptiness would then have to come from the resource constraint or an undeclared ceiling on the product stock.

- *needs check: attribution* - the sentence this one restates cites Aubin, 1991; the draft dropped the source

<details><summary>the whole aligned passage</summary>

> Sink obstructions independent of the stock. The mass balance has a sink-side physical reading with two empty-kernel mechanisms that operate whatever the resource stock does. With sink loading , assimilation , and a harvest floor (in the four-stock specialization, and ): under *no assimilation* ( ), , and the sink exceeds any finite ceiling in finite time; under *weak assimilation* ( ), the sink load at the ceiling is still positive — at — so exits above in finite time, the explicit negation of the ceiling condition with . In both cases the viability kernel (Aubin, 1991) of the constraint set — the states from which some admissible harvest keeps both constraints for all time — is empty. The obstruction needs the sink-generation fraction : if , harvest never loads the sink and the loading argument does not apply — emptiness would then have to come from the resource constraint or an undeclared ceiling on the product stock.

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0497 · needs check: attribution · draft §6.3 · confidence high · overlap 0.772, ratio 0.803, paired through the aligned passage

**Draft, the claim as the draft makes it.**

> Atmospheric CO₂ accumulation violates an upper concentration barrier while fossil carbon stocks decline.

**Deposit, the proposition it corresponds to** (§6.3):

> Atmospheric CO₂ accumulation violates an upper concentration barrier while fossil carbon stocks decline; the depletion diagnostic must check both barriers.

- *needs check: attribution* - the sentence this one restates cites Aubin, 1991; the draft dropped the source

<details><summary>the whole aligned passage</summary>

> Upper-barrier violations matter symmetrically: a system may satisfy every lower-barrier condition while violating an upper barrier, . Atmospheric CO₂ accumulation violates an upper concentration barrier while fossil carbon stocks decline; the depletion diagnostic must check both barriers. And a stock can remain above a barrier until an assessment horizon and still be unsustainable thereafter: if the assessment claims sustainability rather than finite-horizon admissibility, it requires a terminal condition where — the set from which barrier safety is indefinitely maintainable, the viability kernel of the barrier set under the admissible controls (Aubin, 1991). The finite-horizon diagnostic is a necessary but not sufficient condition for sustainability; the full certificate requires the terminal state to lie in the maintainability set.

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0498 · needs check: attribution · draft §6.3 · confidence medium · overlap 0.418, ratio 0.488, paired through the aligned passage

**Draft, the claim as the draft makes it.**

> The depletion diagnostic must check both barriers.

**Deposit, the proposition it corresponds to** (§6.3):

> Atmospheric CO₂ accumulation violates an upper concentration barrier while fossil carbon stocks decline; the depletion diagnostic must check both barriers.

- *needs check: attribution* - the sentence this one restates cites Aubin, 1991; the draft dropped the source

<details><summary>the whole aligned passage</summary>

> Upper-barrier violations matter symmetrically: a system may satisfy every lower-barrier condition while violating an upper barrier, . Atmospheric CO₂ accumulation violates an upper concentration barrier while fossil carbon stocks decline; the depletion diagnostic must check both barriers. And a stock can remain above a barrier until an assessment horizon and still be unsustainable thereafter: if the assessment claims sustainability rather than finite-horizon admissibility, it requires a terminal condition where — the set from which barrier safety is indefinitely maintainable, the viability kernel of the barrier set under the admissible controls (Aubin, 1991). The finite-horizon diagnostic is a necessary but not sufficient condition for sustainability; the full certificate requires the terminal state to lie in the maintainability set.

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0499 · needs check: attribution · draft §6.3 · confidence medium · overlap 0.398, ratio 0.441, paired through the elsewhere in the deposit

**Draft, the claim as the draft makes it.**

> And a stock can remain above a barrier until an assessment horizon and still be unsustainable thereafter.

**Deposit, the proposition it corresponds to** (§6.3):

> And a stock can remain above a barrier until an assessment horizon and still be unsustainable thereafter: if the assessment claims sustainability rather than finite-horizon admissibility, it requires a terminal condition where — the set from which barrier safety is indefinitely maintainable, the viability kernel of the barrier set under the admissible controls (Aubin, 1991).

- *needs check: attribution* - the sentence this one restates cites Aubin, 1991; the draft dropped the source
- *recorded, not judged* - polarity phrased differently (passage ['not'], draft no negator)

<details><summary>the whole aligned passage</summary>

> Upper-barrier violations matter symmetrically: a system may satisfy every lower-barrier condition while violating an upper barrier, . Atmospheric CO₂ accumulation violates an upper concentration barrier while fossil carbon stocks decline; the depletion diagnostic must check both barriers. And a stock can remain above a barrier until an assessment horizon and still be unsustainable thereafter: if the assessment claims sustainability rather than finite-horizon admissibility, it requires a terminal condition where — the set from which barrier safety is indefinitely maintainable, the viability kernel of the barrier set under the admissible controls (Aubin, 1991). The finite-horizon diagnostic is a necessary but not sufficient condition for sustainability; the full certificate requires the terminal state to lie in the maintainability set.

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0533 · needs check: attribution · draft §6.5.2 · confidence high · overlap 1.0, ratio 0.987, paired through the aligned passage

**Draft, the claim as the draft makes it.**

> The qualifying positive sub-cohort ( and ; 35 stocks) has median 2.9 yr; both medians come from the archived pull alone.

**Deposit, the proposition it corresponds to** (§6.5.2):

> The qualifying positive sub-cohort ( and ; 35 stocks) has median yr; both medians come from the archived pull alone.

- *needs check: attribution* - the sentence this one restates cites Abaee, 2026; the draft dropped the source

<details><summary>the whole aligned passage</summary>

> The fisheries column reports the archived-depletion-horizon (ADH) pure-decay proxy under current fishing mortality , with median yr across the 43 assessed stocks with finite spawning-stock-biomass (SSB) and series — the archived pull, designated the headline cohort under the data-vintage rule recorded in S5 — computed with entered for the eight stocks already at or below the reference, the zero convention of the source table's caption, which the median includes. Two disclosures accompany the headline value: the archived 43-stock cohort is reproduced by neither public RAM Legacy release — S5's version-sensitivity record, cross-referenced here, is the retraction and the row-by-row re-verification — and the v4.66 public-release broad-cohort reading (454 stocks, median yr) is the primary public-release comparison, executed in S5 and detailed below. The qualifying positive sub-cohort ( and ; 35 stocks) has median yr; both medians come from the archived pull alone. The cohort is a selected class, not a random sample of assessed stocks: all 43 stocks are small pelagics (18 anchovy, 20 herring, 4 sprat, 1 sardine), the fast-maturing class the companion review screen (Abaee, 2026b, doi:10.5

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0534 · needs check: attribution · draft §6.5.2 · confidence high · overlap 0.897, ratio 0.921, paired through the elsewhere in the deposit

**Draft, the claim as the draft makes it.**

> The cohort is a selected class, not a random sample of assessed stocks: all 43 stocks are small pelagics (18 anchovy, 20 herring, 4 sprat, 1 sardine), the fast-maturing class the companion review screen (Author, E., et al., *in review*) selects by its annual-review eligibility criterion (42 of the 43 are that screen's annual-managed spectral-null stocks, per the source caption).

**Deposit, the proposition it corresponds to** (§6.5.2):

> The cohort is a selected class, not a random sample of assessed stocks: all 43 stocks are small pelagics (18 anchovy, 20 herring, 4 sprat, 1 sardine), the fast-maturing class the companion review screen (Abaee, 2026b, doi:10.5281/zenodo.22554297) selects by its annual-review eligibility criterion (42 of the 43 are that screen's annual-managed spectral-null stocks, per the source caption).

- *needs check: attribution* - the sentence this one restates cites Abaee, 2026; the draft dropped the source

<details><summary>the whole aligned passage</summary>

> The fisheries column reports the archived-depletion-horizon (ADH) pure-decay proxy under current fishing mortality , with median yr across the 43 assessed stocks with finite spawning-stock-biomass (SSB) and series — the archived pull, designated the headline cohort under the data-vintage rule recorded in S5 — computed with entered for the eight stocks already at or below the reference, the zero convention of the source table's caption, which the median includes. Two disclosures accompany the headline value: the archived 43-stock cohort is reproduced by neither public RAM Legacy release — S5's version-sensitivity record, cross-referenced here, is the retraction and the row-by-row re-verification — and the v4.66 public-release broad-cohort reading (454 stocks, median yr) is the primary public-release comparison, executed in S5 and detailed below. The qualifying positive sub-cohort ( and ; 35 stocks) has median yr; both medians come from the archived pull alone. The cohort is a selected class, not a random sample of assessed stocks: all 43 stocks are small pelagics (18 anchovy, 20 herring, 4 sprat, 1 sardine), the fast-maturing class the companion review screen (Abaee, 2026b, doi:10.5

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0536 · needs check: attribution · draft §6.5.2 · confidence high · overlap 0.674, ratio 0.681, paired through the elsewhere in the deposit

**Draft, the claim as the draft makes it.**

> The executed broad-cohort comparison (§5) runs the same protocol on the full public release — 454 stocks, median 3.39 yr, the upper end carried by the long-lived groups: elasmobranchs 11.5, sebastids 9.0, pleuronectids 6.0 yr — and only 2% of random 43-stock draws from that broad cohort have medians at or below the class cohort's 1.79 yr.

**Deposit, the proposition it corresponds to** (§6.5.2):

> The yr median is therefore a class-specific diagnostic for fast-maturing, annually managed pelagics, not a statistic of assessed fisheries in general; the executed broad-cohort comparison (S5) runs the same protocol on the full public release — 454 stocks, median yr, the upper end carried by the long-lived groups (elasmobranchs , sebastids , pleuronectids yr) — and only of random 43-stock draws from that broad cohort have medians at or below the class cohort's yr.

- *needs check: attribution* - the sentence this one restates cites Abaee, 2026; the draft dropped the source

<details><summary>the whole aligned passage</summary>

> The fisheries column reports the archived-depletion-horizon (ADH) pure-decay proxy under current fishing mortality , with median yr across the 43 assessed stocks with finite spawning-stock-biomass (SSB) and series — the archived pull, designated the headline cohort under the data-vintage rule recorded in S5 — computed with entered for the eight stocks already at or below the reference, the zero convention of the source table's caption, which the median includes. Two disclosures accompany the headline value: the archived 43-stock cohort is reproduced by neither public RAM Legacy release — S5's version-sensitivity record, cross-referenced here, is the retraction and the row-by-row re-verification — and the v4.66 public-release broad-cohort reading (454 stocks, median yr) is the primary public-release comparison, executed in S5 and detailed below. The qualifying positive sub-cohort ( and ; 35 stocks) has median yr; both medians come from the archived pull alone. The cohort is a selected class, not a random sample of assessed stocks: all 43 stocks are small pelagics (18 anchovy, 20 herring, 4 sprat, 1 sardine), the fast-maturing class the companion review screen (Abaee, 2026b, doi:10.5

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0537 · needs check: attribution · draft §6.5.2 · confidence medium · overlap 0.448, ratio 0.504, paired through the aligned passage

**Draft, the claim as the draft makes it.**

> The extract is the RAM Legacy cohort of Ricard et al. (2012), and the pull date is archived in the analysis repository; the archived pull has been re-verified row by row against the formula — all 43 rows reproduce with .

**Deposit, the proposition it corresponds to** (§6.5.2):

> The extract is the RAM Legacy cohort of Ricard et al. (2012) at release v4.66 (Zenodo 14043031, 6 November 2024), recorded as the cohort file of the supplementary's S5 record; its vintage is verified from the extract's own contents, four of six published values reproducing that release exactly, and the pull has been re-verified row by row against the formula — all 43 rows reproduce with .

- *needs check: attribution* - the sentence this one restates cites November & Zenodo, 2024; the draft dropped the source

<details><summary>the whole aligned passage</summary>

> The extract is the RAM Legacy cohort of Ricard et al. (2012) at release v4.66 (Zenodo 14043031, 6 November 2024), recorded as the cohort file of the supplementary's S5 record; its vintage is verified from the extract's own contents, four of six published values reproducing that release exactly, and the pull has been re-verified row by row against the formula — all 43 rows reproduce with . The value is reported with its cohort conditions and is not promoted to a forecast. Because cohort composition is database-version-dependent, every cohort statistic is pinned to the archived pull: the quartile summary of and over the cohort belongs to that pull alone, and no cohort statistic is quoted from a different database version. The cohort protocol is fully specified in the accompanying supplementary material (S5) — including the zero entries for stocks at or below the reference, which enter the median — together with the version-sensitivity record: on the public RAM Legacy releases the same protocol qualifies 415 stocks (v4.44, median yr) and 454 (v4.66, median yr) — both reproduced to printed precision under the recovered micro-specification (S5) — neither reproducing the archived 43-stoc

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0552 · needs check: attribution · draft §6.5.3 · confidence high · overlap 0.507, ratio 0.587, paired through the elsewhere in the deposit

**Draft, the claim as the draft makes it.**

> The reserves/resources split discipline is part of the classification: a resource-threshold calculation answers a different question and must not share a column with the reserve-life ratio without an explicit convention label.

**Deposit, the proposition it corresponds to** (§6.5.3):

> The reserves/resources split discipline is part of the classification: a resource-threshold calculation answers a different question and must not share a column with the reserve-life ratio without an explicit convention label; the reserve classification is economic — US reserves have remained near kt while cumulative production since 1996 is of order kt — and the resource-based world horizon ( yr at ) is more than three times the reserve-based figure ( yr); the two-compartment split is what prevents these from being collapsed into one number.

- *needs check: attribution* - the sentence this one restates cites Tilton, 2003, Srivastava & Vegi, 2024; the draft dropped the source

<details><summary>the whole aligned passage</summary>

> The phosphate column of the classification matrix is the reserve-life ratio. At constant current production , the reserve-life ratio is ; at approximately kt ( Mt) of world reserves and kt/yr of production (U.S. Geological Survey, 2026) this is approximately years. The arithmetic is internally consistent as a reserve-life ratio to zero; it is not a physical exhaustion forecast, because reserve classification changes with prices, technology, exploration, and regulation — the point made independently, and forcefully, by Illakwahhi, Vegi, and Srivastava (2024) for the single-source USGS data behind the influential phosphate depletion estimates, and standard in mineral economics, where reserves have grown through a century of rising production for copper (Tilton, 2003; Tilton and Lagos, 2007). The reserves/resources split discipline is part of the classification: a resource-threshold calculation answers a different question and must not share a column with the reserve-life ratio without an explicit convention label; the reserve classification is economic — US reserves have remained near kt while cumulative production since 1996 is of order kt — and the resource-based world horizon ( yr

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0553 · needs check: attribution · draft §6.5.3 · confidence medium · overlap 0.428, ratio 0.515, paired through the elsewhere in the deposit

**Draft, the claim as the draft makes it.**

> The reserve classification is economic — US reserves have remained near 1,000,000 kt while cumulative production since 1996 is of order 600,000 kt — and the resource-based world horizon (≈ 1,125 yr at ) is more than three times the reserve-based figure (≈ 309 yr).

**Deposit, the proposition it corresponds to** (§1.1):

> The United States' phosphate reserves have remained near kt for decades while cumulative production since 1996 is of order kt.

- *needs check: strength* - the passage hedges with ['at least', 'somewhat']; this sentence asserts without a hedge
- *needs check: attribution* - the sentence this one restates cites Tilton, 2003, Srivastava & Vegi, 2024; the draft dropped the source
- *recorded, not judged* - the figure 309, 1125 is stated in the deposit but outside this passage ; polarity phrased differently (passage no negator, draft ['not', 'without'])

<details><summary>the whole aligned passage</summary>

> The classification-drift failure is well documented on the data side. Reserve-life ratios are arithmetic: remaining reserves divided by current production. Because reserves are an economic classification that changes with prices, technology, exploration, and regulation — not a fixed physical stock — the ratio is not an exhaustion forecast. The critique has been made forcefully for phosphate. Illakwahhi, Vegi, and Srivastava (2024) show that the influential "depletion within a century" estimates rest on single-source U.S. Geological Survey (USGS) data whose credibility is questionable, ignore recovery and recycling, and that timeframes estimated from inadequate reserve data "are somewhat misleading." The same point is standard in mineral economics, where the distinction between reserves and resources has been central at least since Tilton (2003). The United States' phosphate reserves have remained near kt for decades while cumulative production since 1996 is of order kt. The classification replenishes itself, and a ratio built on it inherits that behaviour. For copper, Tilton and Lagos (2007) document reserves growing through a century of rising production — the same replenishment u

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0555 · needs check: attribution · draft §6.5.3 · confidence high · overlap 0.927, ratio 0.979, paired through the elsewhere in the deposit

**Draft, the claim as the draft makes it.**

> The implied-production column of the §6.5.2 table reproduces the production figure each horizon assumes (production = reserves ÷ horizon) and thereby exposes the source arithmetic; the country horizons reproduce the recorded MCS-vintage ratios.

**Deposit, the proposition it corresponds to** (§6.5.3):

> The implied-production column of the Section 6.5.2 table reproduces the production figure each horizon assumes (production = reserves/horizon) and thereby exposes the source arithmetic; the country horizons reproduce the recorded MCS-vintage ratios.

- *needs check: attribution* - the sentence this one restates cites Geological & Survey, 2026; the draft dropped the source
- *recorded, not judged* - polarity phrased differently (passage ['not', 'without'], draft no negator)

<details><summary>the whole aligned passage</summary>

> The phosphate column of the classification matrix is the reserve-life ratio. At constant current production , the reserve-life ratio is ; at approximately kt ( Mt) of world reserves and kt/yr of production (U.S. Geological Survey, 2026) this is approximately years. The arithmetic is internally consistent as a reserve-life ratio to zero; it is not a physical exhaustion forecast, because reserve classification changes with prices, technology, exploration, and regulation — the point made independently, and forcefully, by Illakwahhi, Vegi, and Srivastava (2024) for the single-source USGS data behind the influential phosphate depletion estimates, and standard in mineral economics, where reserves have grown through a century of rising production for copper (Tilton, 2003; Tilton and Lagos, 2007). The reserves/resources split discipline is part of the classification: a resource-threshold calculation answers a different question and must not share a column with the reserve-life ratio without an explicit convention label; the reserve classification is economic — US reserves have remained near kt while cumulative production since 1996 is of order kt — and the resource-based world horizon ( yr

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0626 · needs check: attribution · draft §8.3 · confidence high · overlap 0.763, ratio 0.774, paired through the elsewhere in the deposit

**Draft, the claim as the draft makes it.**

> is set by cost, price and catchability — and is infeasible as a management target under a conservation floor : the unregulated equilibrium lies below the floor, and no open-access trajectory is viable against it.

**Deposit, the proposition it corresponds to** (§8.3):

> In the open-access equilibrium of a single-species fishery (Clark, 1990), the bioeconomic equilibrium stock is set by cost, price, and catchability — and is infeasible as a management target under a conservation floor : the unregulated equilibrium lies below the floor, and no open-access trajectory is viable against it.

- *needs check: attribution* - the sentence this one restates cites Clark, 1990; the draft dropped the source
- *recorded, not judged* - polarity phrased differently (passage ['not'], draft no negator)

<details><summary>the whole aligned passage</summary>

> On the extractor side, the same discipline applies to economic steady states. In the open-access equilibrium of a single-species fishery (Clark, 1990), the bioeconomic equilibrium stock is set by cost, price, and catchability — and is infeasible as a management target under a conservation floor : the unregulated equilibrium lies below the floor, and no open-access trajectory is viable against it. The modified golden rule in its constant-unit-cost form, , sets the optimal steady stock for the discount rate (Clark's general form carries an additional marginal-stock-effect term); a harvest tax shifts the open-access equilibrium to — the tax moves the economic equilibrium, but it does not move the physical floor. The distinction is the extractor-side counterpart of the accounting discipline of Section 6: instrument parameters and constraint thresholds are different objects, and no tax schedule substitutes for a constraint the ledger must satisfy. The growth function of this paragraph is a declared constitutive readout on the stock for this extractor-side remark only; it is not a primitive of the closed natural block of Section 2, and nothing in this section is promoted into the typed l

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0627 · needs check: attribution · draft §8.3 · confidence high · overlap 0.682, ratio 0.725, paired through the elsewhere in the deposit

**Draft, the claim as the draft makes it.**

> The modified golden rule in its constant-unit-cost form, , sets the optimal steady stock for the discount rate (Clark's general form carries an additional marginal-stock-effect term).

**Deposit, the proposition it corresponds to** (§8.3):

> The modified golden rule in its constant-unit-cost form, , sets the optimal steady stock for the discount rate (Clark's general form carries an additional marginal-stock-effect term); a harvest tax shifts the open-access equilibrium to — the tax moves the economic equilibrium, but it does not move the physical floor.

- *needs check: attribution* - the sentence this one restates cites Clark, 1990; the draft dropped the source
- *recorded, not judged* - polarity phrased differently (passage ['not'], draft no negator)

<details><summary>the whole aligned passage</summary>

> On the extractor side, the same discipline applies to economic steady states. In the open-access equilibrium of a single-species fishery (Clark, 1990), the bioeconomic equilibrium stock is set by cost, price, and catchability — and is infeasible as a management target under a conservation floor : the unregulated equilibrium lies below the floor, and no open-access trajectory is viable against it. The modified golden rule in its constant-unit-cost form, , sets the optimal steady stock for the discount rate (Clark's general form carries an additional marginal-stock-effect term); a harvest tax shifts the open-access equilibrium to — the tax moves the economic equilibrium, but it does not move the physical floor. The distinction is the extractor-side counterpart of the accounting discipline of Section 6: instrument parameters and constraint thresholds are different objects, and no tax schedule substitutes for a constraint the ledger must satisfy. The growth function of this paragraph is a declared constitutive readout on the stock for this extractor-side remark only; it is not a primitive of the closed natural block of Section 2, and nothing in this section is promoted into the typed l

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0633 · needs check: attribution · draft §9 · confidence high · overlap 0.743, ratio 0.824, paired through the aligned passage

**Draft, the claim as the draft makes it.**

> The partition between this article and the companion delay-dynamics analysis (Author, D., et al., *in review*) is fixed by an interface contract.

**Deposit, the proposition it corresponds to** (§9):

> The partition between this article and the companion delay-dynamics analysis (Abaee, 2026a, doi:10.5281/zenodo.22554217) is fixed by an interface contract.

- *needs check: attribution* - the sentence this one restates cites Abaee, 2026; the draft dropped the source
- *recorded, not judged* - polarity phrased differently (passage no negator, draft ['not'])

<details><summary>the whole aligned passage</summary>

> The partition between this article and the companion delay-dynamics analysis (Abaee, 2026a, doi:10.5281/zenodo.22554217) is fixed by an interface contract. This article owns the closed material accounting: the primitive ledger equations and full routing, the conservation and positivity theorems of Section 4, the componentwise deficit and depletion diagnostics of Sections 5–6, and the closed-donor no-rest and extraction-integrability limitations. The companion owns the open frozen-donor retarded systems and their bifurcation results. The interface is viable, but not because the closed primitive ledger dynamically reduces to the open working system: the two are different completions, and the contract records both the exact shared object and the rejected mapping.

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0634 · needs check: attribution · draft §9 · confidence high · overlap 0.963, ratio 0.969, paired through the aligned passage

**Draft, the claim as the draft makes it.**

> This article owns the closed material accounting: the primitive ledger equations and full routing, the conservation and positivity theorems of §4, the componentwise deficit and depletion diagnostics of §§5–6, and the closed-donor no-rest and extraction-integrability limitations.

**Deposit, the proposition it corresponds to** (§9):

> This article owns the closed material accounting: the primitive ledger equations and full routing, the conservation and positivity theorems of Section 4, the componentwise deficit and depletion diagnostics of Sections 5–6, and the closed-donor no-rest and extraction-integrability limitations.

- *needs check: attribution* - the sentence this one restates cites Abaee, 2026; the draft dropped the source
- *recorded, not judged* - polarity phrased differently (passage no negator, draft ['not'])

<details><summary>the whole aligned passage</summary>

> The partition between this article and the companion delay-dynamics analysis (Abaee, 2026a, doi:10.5281/zenodo.22554217) is fixed by an interface contract. This article owns the closed material accounting: the primitive ledger equations and full routing, the conservation and positivity theorems of Section 4, the componentwise deficit and depletion diagnostics of Sections 5–6, and the closed-donor no-rest and extraction-integrability limitations. The companion owns the open frozen-donor retarded systems and their bifurcation results. The interface is viable, but not because the closed primitive ledger dynamically reduces to the open working system: the two are different completions, and the contract records both the exact shared object and the rejected mapping.

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0687 · needs check: attribution · draft §10.1 · confidence high · overlap 0.889, ratio 0.918, paired through the elsewhere in the deposit

**Draft, the claim as the draft makes it.**

> The companion assessment analysis (Author, F., et al., *in review*) proves the *dynamic* form of the same separation for transition operators; the ledger side contributes the *static prerequisite*: the aggregation question is only well posed after the balance domain is declared, and the burden of proof sits on the aggregation, not on the componentwise report.

**Deposit, the proposition it corresponds to** (§10.1):

> The companion assessment analysis (Abaee, 2026c, doi:10.5281/zenodo.22545740) proves the dynamic form of the same separation for transition operators; the ledger side contributes the static prerequisite: the aggregation question is only well posed after the balance domain is declared, and the burden of proof sits on the aggregation, not on the componentwise report.

- *needs check: attribution* - the sentence this one restates cites Abaee, 2026; the draft dropped the source

<details><summary>the whole aligned passage</summary>

> The companion assessment analysis (Abaee, 2026c, doi:10.5281/zenodo.22545740) proves the dynamic form of the same separation for transition operators; the ledger side contributes the static prerequisite: the aggregation question is only well posed after the balance domain is declared, and the burden of proof sits on the aggregation, not on the componentwise report. The same separation holds at the service layer: a weighted sum on cannot see the directional support gap of Definition 2 — an aggregate that mixes regenerative and non-regenerative provenance never reports which component carries the gap. In the terms of the ecological-economics literature of Section 1.1, componentwise adequacy on the typed ledger is strong sustainability as a conjunctive predicate; a positive weighted sum is weak sustainability as a ranking device. The ledger authorizes the first and does not authorize the second.

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0691 · needs check: attribution · draft §10.2 · confidence high · overlap 0.697, ratio 0.747, paired through the aligned passage

**Draft, the claim as the draft makes it.**

> Five rules, each carried by a proved or defined statement of this article, jointly prevent double counting and phantom mass.

**Deposit, the proposition it corresponds to** (§10.2):

> Five rules, each carried by a proved or defined statement of this article and specified as a checkable procedure in the companion methods study (Abaee, 2026d), jointly prevent double counting and phantom mass:

- *needs check: attribution* - the sentence this one restates cites Abaee, 2026; the draft dropped the source

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0073 · needs check: inference · draft §1.1 · confidence high · overlap 0.553, ratio 0.597, paired through the aligned passage

**Draft, the claim as the draft makes it.**

> So a drawdown is recoverable only insofar as the pool regrows faster than it is taken.

**Deposit, the proposition it corresponds to** (§1.1):

> A drawdown is recoverable only insofar as the pool regenerates faster than it is taken; if a pool regenerates too slowly for the rate at which it is taken, drawdown is still liquidation.

- *needs check: inference* - the sentence opens on an inferential connective and the passage states no consequence

<details><summary>the whole aligned passage</summary>

> The second sense is dynamical and is yield inflation. A measured yield can exceed the true sustainable yield when it is maintained by drawing down the support pool — groundwater, soil carbon, bioavailable nutrients — rather than by that pool's regeneration. The resource appears productive while what sustains it is liquidated silently. The support pool need not be a superficially non-renewable reserve for this diagnosis to run, and it can be read in more than one way at once — as natural capital, as a stock, or as a slowly regenerating flow of services. These are overlapping readings of the same pool, not mutually exclusive ones. Every such pool is regenerative on some timescale — a crop within a season, an aquifer within years to decades, a mineral deposit over geological time — and the failure is the same in each case. What decides is the renewal rate of the pool relative to the rate of use. A use that falls on the pool's regeneration is sustained. One that falls on the pool itself is liquidation. A drawdown is recoverable only insofar as the pool regenerates faster than it is taken; if a pool regenerates too slowly for the rate at which it is taken, drawdown is still liquidation.

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0157 · needs check: inference · draft §1.2 · confidence high · overlap 1.0, ratio 0.978, paired through the aligned passage

**Draft, the claim as the draft makes it.**

> So this article builds the accounting layer that resists these failures.

**Deposit, the proposition it corresponds to** (§1.1):

> This article builds the accounting layer that resists these failures.

- *needs check: inference* - the sentence opens on an inferential connective and the passage states no consequence

<details><summary>the whole aligned passage</summary>

> This article builds the accounting layer that resists these failures. Its objects are typed ledgers in which conservation follows from the incidence structure, positivity follows from donor limitation, services are readouts rather than conserved mass, and each depletion quantity carries its own classification, stated at its actual strength.

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0345 · needs check: inference · draft §3.5 · confidence medium · overlap 0.354, ratio 0.48, paired through the elsewhere in the deposit

**Draft, the claim as the draft makes it.**

> So the certificate may fail when a trajectory with jointly realizable fluxes would pass.

**Deposit, the proposition it corresponds to** (§?):

> Corollary (Flux-derived barrier certificate). *If and for all and all , then every trajectory compatible with the flux bounds is barrier-safe on .*

- *needs check: inference* - the sentence opens on an inferential connective and the passage states no consequence
- *recorded, not judged* - polarity phrased differently (passage no negator, draft ['not', 'without'])

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0366 · needs check: inference · draft §3.6 · confidence high · overlap 0.751, ratio 0.805, paired through the aligned passage

**Draft, the claim as the draft makes it.**

> Consequently every finite hitting time of a zero readout is the hitting time of a compartment or of a barrier on a readout, never of total mass, and "exhaustion of the natural block" (Theorems 7 and 14) is transfer across the block boundary into the product, waste and inert compartments.*

**Deposit, the proposition it corresponds to** (§3.6):

> Proposition (Depletion is compartmental). *On a closed typed ledger, the total mass of each conserved moiety is invariant along trajectories; consequently every finite hitting time of a zero readout is the hitting time of a compartment or of a barrier on a readout, never of total mass, and "exhaustion of the natural block" (Theorems 7 and 14) is transfer across the block boundary into the product, waste, and inert compartments.*

- *needs check: inference* - the sentence opens on an inferential connective and the passage states no consequence

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0685 · needs check: inference · draft §10.1 · confidence high · overlap 0.972, ratio 0.984, paired through the aligned passage

**Draft, the claim as the draft makes it.**

> Consequently, on any feasible balance domain containing a compensating pair — and Definition 1's domain is exactly that whenever the operating set admits states with mixed balances — no non-negative weighting can stand in for the conjunctive criterion of §3.2.

**Deposit, the proposition it corresponds to** (§10.1):

> Consequently, on any feasible balance domain containing a compensating pair — and Definition 1's domain is exactly that whenever the operating set admits states with mixed balances — no nonnegative weighting can stand in for the conjunctive criterion of Section 3.2.

- *needs check: inference* - the sentence opens on an inferential connective and the passage states no consequence

<details><summary>the whole aligned passage</summary>

> The construction never uses the dynamics: the failure is a property of nonnegative weightings over mixed-sign balances, not of the donor-limited positivity mechanism. Consequently, on any feasible balance domain containing a compensating pair — and Definition 1's domain is exactly that whenever the operating set admits states with mixed balances — no nonnegative weighting can stand in for the conjunctive criterion of Section 3.2. The reading is the algebraic form of the weak-comparability thesis stated in Section 1.1.

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0085 · needs check: scope · draft §1.1 · confidence medium · overlap 0.354, ratio 0.527, paired through the elsewhere in the deposit

**Draft, the claim as the draft makes it.**

> That distinction has teeth, because the article does not oversell it.

**Deposit, the proposition it corresponds to** (§6):

> The distinction matters because "time to depletion" is publicly used as if all three were one quantity.

- *needs check: scope* - the sentence this one restates is conditioned by ['if']; the draft states it unconditionally

<details><summary>the whole aligned passage</summary>

> The ledger supplies the net active-pool derivative needed to distinguish gross throughput from net decline and from a model-conditioned threshold time. The distinction matters because "time to depletion" is publicly used as if all three were one quantity. They are not, and the worked instances of this section make the differences explicit. Let be a declared threshold for the active abiotic pool with .

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0123 · needs check: scope · draft §1.2 · confidence high · overlap 0.645, ratio 0.702, paired through the aligned passage

**Draft, the claim as the draft makes it.**

> In material accounting the thesis has a precise algebraic form, stated in Section 10.1: no non-negative weighting of component balances can certify that every component clears its floor. A positive weighted sum never proves that the individual parts are non-negative.

**Deposit, the proposition it corresponds to** (§1.1):

> At the level of material accounting this thesis has a precise algebraic form, which Section 10.1 states: no nonnegative weighting of component balances certifies that every component satisfies its floor.

- *needs check: scope* - the sentence this one restates is conditioned by ['at the level of']; the draft states it unconditionally

<details><summary>the whole aligned passage</summary>

> The weak-comparability thesis of ecological economics holds that values relevant to environmental decisions may not be commensurable in a single metric (Martinez-Alier, Munda, and O'Neill, 1998). At the level of material accounting this thesis has a precise algebraic form, which Section 10.1 states: no nonnegative weighting of component balances certifies that every component satisfies its floor. A positive weighted sum never certifies componentwise nonnegativity. Scalar summaries may rank and communicate; certification requires the vector.

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0251 · needs check: scope · draft §2.3 · confidence medium · overlap 0.302, ratio 0.458, paired through the elsewhere in the deposit

**Draft, the claim as the draft makes it.**

> In the scaffold, assimilation is a slow flux and mortality a slow flux.

**Deposit, the proposition it corresponds to** (§2.1):

> Write for the admissible stationary flux patterns.

- *needs check: scope* - the sentence this one restates is conditioned by ['admissible']; the draft states it unconditionally
- *recorded, not judged* - polarity phrased differently (passage no negator, draft ['not'])

<details><summary>the whole aligned passage</summary>

> Definition 21 (Closure cone). The regimes above can be stated on the ledger's own objects rather than as attitudes toward them. Let be the incidence operator declared here, let be the primitive fluxes under declared capacities , let collect the declared boundary transfers, and let project a flux vector onto its use columns. Write for the admissible stationary flux patterns. A demanded use vector closes at the rate of use if and only if . The closure capacity is a linear programme on the declared capacities, and its feasibility is the cut condition on return capacity (Gale, 1957; Ahuja et al., 1993). Where , the cycle closes at the demanded rate. Where , every trajectory meeting has a non-stationary stock, and by conservation the shortfall appears as support drawdown together with sink accumulation; the deficit share is not a free parameter. Yield inflation is the same statement read outside the projection: demand met with no stationary pattern behind it.

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0257 · needs check: scope · draft §front · confidence high · overlap 0.524, ratio 0.575, paired through the elsewhere in the deposit

**Draft, the claim as the draft makes it.**

> Adding the four equations gives the mass balance

**Deposit, the proposition it corresponds to** (§2.4):

> Adding the four equations gives the mass balance so total mass is conserved exactly when both boundary transfers vanish.

- *needs check: scope* - the sentence this one restates is conditioned by ['when']; the draft states it unconditionally
- *recorded, not judged* - polarity phrased differently (passage ['not'], draft no negator)

<details><summary>the whole aligned passage</summary>

> A second exact specialization closes a resource–sink system with a nutrient stock and product stock. The state is (in this block's local notation, is the resource stock, the sink stock, the nutrient stock, and the input flux; the carrying capacity and living stock of Section 2.2 do not enter), with where is the sink-generation fraction, the assimilation rate, external nutrient input, and product disposal. Adding the four equations gives the mass balance so total mass is conserved exactly when both boundary transfers vanish. This mass balance is an exact specialization of the incidence discipline of Section 2.1: every internal transfer cancels in the column sum, and the boundary terms survive as the ledger's declared inputs and outputs.

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0371 · needs check: scope · draft §front · confidence medium · overlap 0.319, ratio 0.427, paired through the aligned passage

**Draft, the claim as the draft makes it.**

> Along every trajectory of the closed natural block (2) with optional mining restored,*

**Deposit, the proposition it corresponds to** (§3.6):

> Then obeys along every admissible trajectory, and for every trajectory that remains inside the declared barriers If additionally and , then .

- *needs check: scope* - the sentence this one restates is conditioned by ['admissible', 'if']; the draft states it unconditionally

<details><summary>the whole aligned passage</summary>

> Theorem 24 (Critical-margin budget). Let the declared barrier margins be affine, , and let the delivered service rate be with . Suppose some satisfies componentwise, with carrying the units that convert margin into cumulative service. Then obeys along every admissible trajectory, and for every trajectory that remains inside the declared barriers If additionally and , then .

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0477 · needs check: scope · draft §6.1 · confidence high · overlap 0.855, ratio 0.88, paired through the elsewhere in the deposit

**Draft, the claim as the draft makes it.**

> Definition 5 (Scenario-conditioned hitting time). *For a fully specified dynamical model, policy or scenario , disturbance history , and initial state ,*

**Deposit, the proposition it corresponds to** (§6.1):

> Definition 5 (Scenario-conditioned hitting time). *For a fully specified dynamical model, policy or scenario , disturbance history , and initial state ,* *with if the threshold is never reached.

- *needs check: scope* - the sentence this one restates is conditioned by ['if']; the draft states it unconditionally
- *recorded, not judged* - polarity phrased differently (passage ['never', 'not'], draft no negator)

<details><summary>the whole aligned passage</summary>

> Definition 5 (Scenario-conditioned hitting time). *For a fully specified dynamical model, policy or scenario , disturbance history , and initial state ,* *with if the threshold is never reached. Under parameter, observation, and scenario uncertainty the appropriate output is a distribution or robust interval of , not a single universal date.*

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0482 · needs check: scope · draft §6.2 · confidence medium · overlap 0.316, ratio 0.467, paired through the elsewhere in the deposit

**Draft, the claim as the draft makes it.**

> In words: promise that the decline stays within 10% of a fixed rate, and the frozen-rate ratio is guaranteed to be within about 11% of the true crossing time.

**Deposit, the proposition it corresponds to** (§?):

> Proposition 26 (Sign of the frozen-rate error). Let with on , and write the true horizon and the frozen-rate ratio as If is nondecreasing in then , and the frozen-rate number is conservative.

- *needs check: scope* - the sentence this one restates is conditioned by ['if']; the draft states it unconditionally
- *recorded, not judged* - the figure 10, 11 is stated in the deposit but outside this passage

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0487 · needs check: scope · draft §6.2 · confidence medium · overlap 0.391, ratio 0.47, paired through the aligned passage

**Draft, the claim as the draft makes it.**

> — the only regime in which the frozen-rate ratio *is* a horizon.

**Deposit, the proposition it corresponds to** (§6.2):

> When the clocks coincide. Under the rate bracket the frozen-rate ratio and the true hitting time agree within the bracket: gives , hence — the only regime in which the frozen-rate ratio is a horizon.

- *needs check: scope* - the sentence this one restates is conditioned by ['when']; the draft states it unconditionally

<details><summary>the whole aligned passage</summary>

> When the clocks coincide. Under the rate bracket the frozen-rate ratio and the true hitting time agree within the bracket: gives , hence — the only regime in which the frozen-rate ratio is a horizon. At a stationary state ( ) with , while : the three quantities of Section 6.1 coincide only under a declared rate bracket, and the false implication is the reason.

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0505 · needs check: scope · draft §6.4 · confidence high · overlap 0.635, ratio 0.746, paired through the aligned passage

**Draft, the claim as the draft makes it.**

> and the depletion-horizon classification is fourfold: nominal ( , ); worst-case ( ); probabilistic ( ); and scenario-conditioned ( ).

**Deposit, the proposition it corresponds to** (§?):

> For uncertain parameters and admissible disturbances , robust barrier safety is and the depletion-horizon classification is fourfold: nominal ( , ); worst-case ( ); probabilistic ( ); and scenario-conditioned ( ).

- *needs check: scope* - the sentence this one restates is conditioned by ['admissible']; the draft states it unconditionally
- *recorded, not judged* - polarity phrased differently (passage no negator, draft ['without'])

<details><summary>the whole aligned passage</summary>

> For uncertain parameters and admissible disturbances , robust barrier safety is and the depletion-horizon classification is fourfold: nominal ( , ); worst-case ( ); probabilistic ( ); and scenario-conditioned ( ). The componentwise diagnostic applies to each scenario, and the conjunctive criterion applies within each scenario and across scenarios. No single number is promoted across the four classes without a declared map.

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0560 · needs check: scope · draft §6.5.4 · confidence high · overlap 0.898, ratio 0.905, paired through the elsewhere in the deposit

**Draft, the claim as the draft makes it.**

> the fishing-only time-to-reference: the crossing time of the deliberately incomplete comparison process .

**Deposit, the proposition it corresponds to** (§6.5.4):

> When and , define and the fishing-only time-to-reference: the crossing time of the deliberately incomplete comparison process .

- *needs check: scope* - the sentence this one restates is conditioned by ['when']; the draft states it unconditionally

<details><summary>the whole aligned passage</summary>

> The fisheries column of the classification matrix is the removals-only pressure time. When and , define and the fishing-only time-to-reference: the crossing time of the deliberately incomplete comparison process . With this is the construction tabled as ADH in Section 6.5.2; the two notations are kept because the boundary hypotheses stated here ( , ) are exactly the conditions of the positive sub-cohort of Section 6.5.2 (35 stocks, median yr); the reported Section 6.5.2 median ( yr) additionally carries the eight zero entries for stocks at or below the reference, per the zero convention of the source caption. It is a removals-only pressure time scale — the time unit comes from rescaling a stock-reference margin by one isolated gross-loss rate. Because recruitment, somatic growth, maturation, natural mortality, density dependence, environmental forcing, and future policy are omitted, is not a net biomass depletion diagnostic, not a demographic hitting-time estimate, and not a member of the – – hierarchy. A genuinely local biomass-decline ratio would require a compatible net estimate, and a demographic hitting time a fully specified population model; RAM Legacy SSB and data (Ricard e

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0581 · needs check: scope · draft §front · confidence high · overlap 0.546, ratio 0.621, paired through the elsewhere in the deposit

**Draft, the claim as the draft makes it.**

> In particular — the deterministic horizon to the window minimum, — and .*

**Deposit, the proposition it corresponds to** (§7.3):

> Conditional on treating and the barrier as fixed,* *in the mean–shape parameterization; in particular — the deterministic horizon to the window minimum, — and .*

- *needs check: scope* - the sentence this one restates is conditioned by ['conditional']; the draft states it unconditionally

<details><summary>the whole aligned passage</summary>

> Proposition 18 (Inverse-Gaussian first passage — a standard fact, stated for notation). *Let for the process of Definition 6 and . Conditional on treating and the barrier as fixed,* *in the mean–shape parameterization; in particular — the deterministic horizon to the window minimum, — and .*

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0709 · needs check: scope · draft §11 · confidence medium · overlap 0.376, ratio 0.411, paired through the elsewhere in the deposit

**Draft, the claim as the draft makes it.**

> And depletion time is three quantities, not one.

**Deposit, the proposition it corresponds to** (§6):

> The distinction matters because "time to depletion" is publicly used as if all three were one quantity.

- *needs check: scope* - the sentence this one restates is conditioned by ['if']; the draft states it unconditionally

<details><summary>the whole aligned passage</summary>

> The ledger supplies the net active-pool derivative needed to distinguish gross throughput from net decline and from a model-conditioned threshold time. The distinction matters because "time to depletion" is publicly used as if all three were one quantity. They are not, and the worked instances of this section make the differences explicit. Let be a declared threshold for the active abiotic pool with .

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0137 · needs check: strength · draft §1.2 · confidence high · overlap 0.64, ratio 0.808, paired through the elsewhere in the deposit

**Draft, the claim as the draft makes it.**

> In this idealised closure, the by-products of use — carbon taken from the atmosphere, chemicals released to air, water and soil — come back into use in time.

**Deposit, the proposition it corresponds to** (§1.1):

> In this idealized closure the byproducts of use — carbon drawn from the atmosphere, chemical substances released to air, water, and soil — are returned to use in time and are therefore not waste.

- *needs check: strength* - the passage hedges with ['relative', 'relative to']; this sentence asserts without a hedge

<details><summary>the whole aligned passage</summary>

> The third task is to locate substitution within the ledger, rather than alongside it. Weak and strong sustainability are not competing hypotheses but two regimes of one dynamic system, distinguished not by whether substitution alone keeps pace with depletion but by whether the material cycle can be closed at the rate of use — a reading of the two regimes developed for the ledger, not the received distinction of the literature, which turns on the substitutability of natural capital (Neumayer, 2013; Ekins et al., 2003). Weak sustainability is the idealized regime: humans consume and populate slowly enough that technological substitution and natural regeneration together redistribute matter so that it is used as it arises. On human-relevant timescales substitution is the dominant term; natural regeneration acts far more slowly — often on deep-time scales — and is included for physical completeness rather than as a co-equal mechanism (Daly, 1990). The deep-time clause is scoped to the slow compartments — geological donors and mineral stocks, whose renewal runs on deep time. The regenerative compartments this article's applied record tabulates renew on human timescales — a crop within a

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0212 · needs check: strength · draft §2.2 · confidence medium · overlap 0.381, ratio 0.53, paired through the aligned passage

**Draft, the claim as the draft makes it.**

> In the closed block, recharge is donor-limited and cannot run backward: at .

**Deposit, the proposition it corresponds to** (§2.2):

> In the closed block no derived target appears.

- *needs check: strength* - the passage hedges with ['appears']; this sentence asserts ['cannot']

<details><summary>the whole aligned passage</summary>

> In the closed block no derived target appears. Recharge is donor-limited and cannot run backward ( at ; the positive-part convention , read as a one-way valve at a nonpositive target, never binds here because the registered intrinsic target is positive), and mining is donor-limited the same way extraction is. With the donor fraction is smooth and strictly increasing in the donor level.

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0213 · needs check: strength · draft §2.2 · confidence high · overlap 0.609, ratio 0.514, paired through the aligned passage

**Draft, the claim as the draft makes it.**

> The positive-part convention — read as a one-way valve at a non-positive target — never binds here, because the registered intrinsic target is positive.

**Deposit, the proposition it corresponds to** (§2.2):

> Recharge is donor-limited and cannot run backward ( at ; the positive-part convention , read as a one-way valve at a nonpositive target, never binds here because the registered intrinsic target is positive), and mining is donor-limited the same way extraction is.

- *needs check: strength* - the passage hedges with ['appears']; this sentence asserts ['never', 'never binds']

<details><summary>the whole aligned passage</summary>

> In the closed block no derived target appears. Recharge is donor-limited and cannot run backward ( at ; the positive-part convention , read as a one-way valve at a nonpositive target, never binds here because the registered intrinsic target is positive), and mining is donor-limited the same way extraction is. With the donor fraction is smooth and strictly increasing in the donor level.

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0223 · needs check: strength · draft §front · confidence medium · overlap 0.442, ratio 0.453, paired through the elsewhere in the deposit

**Draft, the claim as the draft makes it.**

> The geological half-saturation is declared positive (for smoothness of ) under the separation-of-scale condition , a regime in which .

**Deposit, the proposition it corresponds to** (§?):

> The registered parameterization is , , , , , , , ; the geological half-saturation is declared positive (smoothness of the donor fraction ) under the separation-of-scale condition , in which regime ; the scale separation is registered rather than a numerical value, and the corner is the discontinuous-perturbation limit, not the registered regime.

- *needs check: strength* - the passage hedges with ['would']; this sentence asserts without a hedge

<details><summary>the whole aligned passage</summary>

> The pair is the registered object of the companion delay-dynamics analysis (Abaee, 2026a, doi:10.5281/zenodo.22554217; its eq. (1), where the memory--effort pair is defined on the gated three-state core with the stock-decline rate as memory input, and its Section 2.4, which relates that core to the four-state working model in which the input is ) and is not analysed in this article. Net regeneration is the difference of two non-negative primitives — gross regeneration (support stock) and density-dependent return (stock support) — so (2) stays within the primitive-flux discipline of Section 2.1 despite the signed entry. The block's harvest routing is the corner of Section 2.3: harvest exits the natural block entirely as product, and a positive detritus-routed fraction would add to and reduce the block export to ; the mass identity of Theorem 7 is stated for the declared routing. The registered parameterization is , , , , , , , ; the geological half-saturation is declared positive (smoothness of the donor fraction ) under the separation-of-scale condition , in which regime ; the scale separation is registered rather than a numerical value, and the corner is the discontinuous-perturba

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0224 · needs check: strength · draft §front · confidence high · overlap 0.476, ratio 0.377, paired through the elsewhere in the deposit

**Draft, the claim as the draft makes it.**

> The scale separation is registered rather than a numerical value, and the corner is the discontinuous-perturbation limit, not the registered regime.

**Deposit, the proposition it corresponds to** (§?):

> The registered parameterization is , , , , , , , ; the geological half-saturation is declared positive (smoothness of the donor fraction ) under the separation-of-scale condition , in which regime ; the scale separation is registered rather than a numerical value, and the corner is the discontinuous-perturbation limit, not the registered regime.

- *needs check: strength* - the passage hedges with ['would']; this sentence asserts without a hedge

<details><summary>the whole aligned passage</summary>

> The pair is the registered object of the companion delay-dynamics analysis (Abaee, 2026a, doi:10.5281/zenodo.22554217; its eq. (1), where the memory--effort pair is defined on the gated three-state core with the stock-decline rate as memory input, and its Section 2.4, which relates that core to the four-state working model in which the input is ) and is not analysed in this article. Net regeneration is the difference of two non-negative primitives — gross regeneration (support stock) and density-dependent return (stock support) — so (2) stays within the primitive-flux discipline of Section 2.1 despite the signed entry. The block's harvest routing is the corner of Section 2.3: harvest exits the natural block entirely as product, and a positive detritus-routed fraction would add to and reduce the block export to ; the mass identity of Theorem 7 is stated for the declared routing. The registered parameterization is , , , , , , , ; the geological half-saturation is declared positive (smoothness of the donor fraction ) under the separation-of-scale condition , in which regime ; the scale separation is registered rather than a numerical value, and the corner is the discontinuous-perturba

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0270 · needs check: strength · draft §2.4 · confidence medium · overlap 0.412, ratio 0.454, paired through the aligned passage

**Draft, the claim as the draft makes it.**

> Which constraint fails first depends on the total mass , the ceiling and the remaining stock.

**Deposit, the proposition it corresponds to** (§2.4):

> Which constraint fails first depends on the total mass , the ceiling , and the remaining stock: a ceiling below the sink's reachable mass share is crossed in finite time, while a ceiling at or above the total mass is unreachable and the violated constraint is the resource floor (the finite-budget bound of Theorem 14).

- *needs check: strength* - the passage hedges with ['can']; this sentence asserts without a hedge

<details><summary>the whole aligned passage</summary>

> The closed-ledger corollary is the same mechanism in ledger language. In a closed ledger without recycling, where enters the sink irreversibly and , the sink rises monotonically against the finite total mass, and any positive output floor forces an empty viability kernel. Which constraint fails first depends on the total mass , the ceiling , and the remaining stock: a ceiling below the sink's reachable mass share is crossed in finite time, while a ceiling at or above the total mass is unreachable and the violated constraint is the resource floor (the finite-budget bound of Theorem 14). For material-flows accounting this is the precise sense in which a "balanced" mass ledger can still be physically inadmissible: the bookkeeping is exact, but no harvest schedule respects both the resource floor and the sink ceiling simultaneously.

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0271 · needs check: strength · draft §2.4 · confidence high · overlap 0.76, ratio 0.503, paired through the aligned passage

**Draft, the claim as the draft makes it.**

> A ceiling below the sink's reachable mass share is crossed in finite time; a ceiling at or above the total mass is unreachable, and the constraint violated is the resource floor (the finite-budget bound of Theorem 14).

**Deposit, the proposition it corresponds to** (§2.4):

> Which constraint fails first depends on the total mass , the ceiling , and the remaining stock: a ceiling below the sink's reachable mass share is crossed in finite time, while a ceiling at or above the total mass is unreachable and the violated constraint is the resource floor (the finite-budget bound of Theorem 14).

- *needs check: strength* - the passage hedges with ['can']; this sentence asserts without a hedge

<details><summary>the whole aligned passage</summary>

> The closed-ledger corollary is the same mechanism in ledger language. In a closed ledger without recycling, where enters the sink irreversibly and , the sink rises monotonically against the finite total mass, and any positive output floor forces an empty viability kernel. Which constraint fails first depends on the total mass , the ceiling , and the remaining stock: a ceiling below the sink's reachable mass share is crossed in finite time, while a ceiling at or above the total mass is unreachable and the violated constraint is the resource floor (the finite-budget bound of Theorem 14). For material-flows accounting this is the precise sense in which a "balanced" mass ledger can still be physically inadmissible: the bookkeeping is exact, but no harvest schedule respects both the resource floor and the sink ceiling simultaneously.

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0274 · needs check: strength · draft §2.5 · confidence high · overlap 0.767, ratio 0.623, paired through the elsewhere in the deposit

**Draft, the claim as the draft makes it.**

> - Standing-stock culling — present extraction removes reproductive stock directly. - Recruitment suppression — present use prevents future recruits, without removing adults now. - Weak viability coupling — use has limited or indirect effect on reproduction.

**Deposit, the proposition it corresponds to** (§2.5):

> Extraction has at least three distinct physical meanings — standing-stock culling (present extraction removes reproductive stock directly), recruitment suppression (present use prevents future recruits without immediate adult removal), and weak viability coupling (use has limited or indirect effect on reproduction).

- *needs check: strength* - the passage hedges with ['at least']; this sentence asserts without a hedge

<details><summary>the whole aligned passage</summary>

> Extraction has at least three distinct physical meanings — standing-stock culling (present extraction removes reproductive stock directly), recruitment suppression (present use prevents future recruits without immediate adult removal), and weak viability coupling (use has limited or indirect effect on reproduction). In the ledger, standing-stock culling enters as an outflow from the standing-stock compartment. The typing is the physical module's, not the diagnostic's: a diagnostic label such as "unsustainable portion" never determines physical destination. Material routing is determined by the typed physical module alone, and the diagnostic threshold that flags a flow has no standing in the incidence matrix.

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0328 · needs check: strength · draft §3.3 · confidence high · overlap 0.732, ratio 0.747, paired through the aligned passage

**Draft, the claim as the draft makes it.**

> In both cases the barriers are declared, not computed: the flux data do not compute ecological threshold values, aquifer collapse thresholds, or concentration boundaries.

**Deposit, the proposition it corresponds to** (§3.3):

> In both cases the barriers are declared, not computed: the flux data do not compute ecological threshold values, aquifer collapse thresholds, or concentration boundaries — the theorem establishes trajectory compliance with declared barriers, not derivation of the barriers themselves.

- *needs check: strength* - the passage hedges with ['generally']; this sentence asserts without a hedge

<details><summary>the whole aligned passage</summary>

> Two cases are distinguished. Prescribed or observed fluxes: if and are known and integrable, stock balances are reconstructed by integration without solving the internal constitutive dynamics — the computationally simple auditing case. Endogenous fluxes: if , flux-only auditing is not generally possible without solving, estimating, or bounding the coupled system; the identity still holds, but the integral cannot be evaluated without determining . In both cases the barriers are declared, not computed: the flux data do not compute ecological threshold values, aquifer collapse thresholds, or concentration boundaries — the theorem establishes trajectory compliance with declared barriers, not derivation of the barriers themselves.

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0329 · needs check: strength · draft §3.3 · confidence high · overlap 0.484, ratio 0.568, paired through the aligned passage

**Draft, the claim as the draft makes it.**

> The theorem establishes trajectory *compliance with declared barriers*, not derivation of the barriers themselves.

**Deposit, the proposition it corresponds to** (§3.3):

> In both cases the barriers are declared, not computed: the flux data do not compute ecological threshold values, aquifer collapse thresholds, or concentration boundaries — the theorem establishes trajectory compliance with declared barriers, not derivation of the barriers themselves.

- *needs check: strength* - the passage hedges with ['generally']; this sentence asserts without a hedge

<details><summary>the whole aligned passage</summary>

> Two cases are distinguished. Prescribed or observed fluxes: if and are known and integrable, stock balances are reconstructed by integration without solving the internal constitutive dynamics — the computationally simple auditing case. Endogenous fluxes: if , flux-only auditing is not generally possible without solving, estimating, or bounding the coupled system; the identity still holds, but the integral cannot be evaluated without determining . In both cases the barriers are declared, not computed: the flux data do not compute ecological threshold values, aquifer collapse thresholds, or concentration boundaries — the theorem establishes trajectory compliance with declared barriers, not derivation of the barriers themselves.

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0501 · needs check: strength · draft §6.3 · confidence high · overlap 0.496, ratio 0.562, paired through the elsewhere in the deposit

**Draft, the claim as the draft makes it.**

> — the set from which barrier safety is indefinitely maintainable: the viability kernel of the barrier set under the admissible controls (Aubin, 1991).

**Deposit, the proposition it corresponds to** (§6.3):

> And a stock can remain above a barrier until an assessment horizon and still be unsustainable thereafter: if the assessment claims sustainability rather than finite-horizon admissibility, it requires a terminal condition where — the set from which barrier safety is indefinitely maintainable, the viability kernel of the barrier set under the admissible controls (Aubin, 1991).

- *needs check: strength* - the passage hedges with ['can']; this sentence asserts without a hedge

<details><summary>the whole aligned passage</summary>

> Upper-barrier violations matter symmetrically: a system may satisfy every lower-barrier condition while violating an upper barrier, . Atmospheric CO₂ accumulation violates an upper concentration barrier while fossil carbon stocks decline; the depletion diagnostic must check both barriers. And a stock can remain above a barrier until an assessment horizon and still be unsustainable thereafter: if the assessment claims sustainability rather than finite-horizon admissibility, it requires a terminal condition where — the set from which barrier safety is indefinitely maintainable, the viability kernel of the barrier set under the admissible controls (Aubin, 1991). The finite-horizon diagnostic is a necessary but not sufficient condition for sustainability; the full certificate requires the terminal state to lie in the maintainability set.

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0502 · needs check: strength · draft §6.3 · confidence high · overlap 0.588, ratio 0.687, paired through the elsewhere in the deposit

**Draft, the claim as the draft makes it.**

> The finite-horizon diagnostic is a necessary but not sufficient condition for sustainability.

**Deposit, the proposition it corresponds to** (§6.3):

> The finite-horizon diagnostic is a necessary but not sufficient condition for sustainability; the full certificate requires the terminal state to lie in the maintainability set.

- *needs check: strength* - the passage hedges with ['can']; this sentence asserts without a hedge

<details><summary>the whole aligned passage</summary>

> Upper-barrier violations matter symmetrically: a system may satisfy every lower-barrier condition while violating an upper barrier, . Atmospheric CO₂ accumulation violates an upper concentration barrier while fossil carbon stocks decline; the depletion diagnostic must check both barriers. And a stock can remain above a barrier until an assessment horizon and still be unsustainable thereafter: if the assessment claims sustainability rather than finite-horizon admissibility, it requires a terminal condition where — the set from which barrier safety is indefinitely maintainable, the viability kernel of the barrier set under the admissible controls (Aubin, 1991). The finite-horizon diagnostic is a necessary but not sufficient condition for sustainability; the full certificate requires the terminal state to lie in the maintainability set.

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0503 · needs check: strength · draft §6.3 · confidence high · overlap 0.592, ratio 0.641, paired through the elsewhere in the deposit

**Draft, the claim as the draft makes it.**

> The full certificate requires the terminal state to lie in the maintainability set.

**Deposit, the proposition it corresponds to** (§6.3):

> The finite-horizon diagnostic is a necessary but not sufficient condition for sustainability; the full certificate requires the terminal state to lie in the maintainability set.

- *needs check: strength* - the passage hedges with ['can']; this sentence asserts without a hedge

<details><summary>the whole aligned passage</summary>

> Upper-barrier violations matter symmetrically: a system may satisfy every lower-barrier condition while violating an upper barrier, . Atmospheric CO₂ accumulation violates an upper concentration barrier while fossil carbon stocks decline; the depletion diagnostic must check both barriers. And a stock can remain above a barrier until an assessment horizon and still be unsustainable thereafter: if the assessment claims sustainability rather than finite-horizon admissibility, it requires a terminal condition where — the set from which barrier safety is indefinitely maintainable, the viability kernel of the barrier set under the admissible controls (Aubin, 1991). The finite-horizon diagnostic is a necessary but not sufficient condition for sustainability; the full certificate requires the terminal state to lie in the maintainability set.

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0514 · needs check: strength · draft §6.5.1 · confidence high · overlap 1.0, ratio 0.997, paired through the aligned passage

**Draft, the claim as the draft makes it.**

> Classification, stated at the product's own status: a statistical anomaly index with units of time — not the physical stock ratio , and not a forecast of aquifer exhaustion.

**Deposit, the proposition it corresponds to** (§6.5.1):

> Classification, stated at the product's own status: a statistical anomaly index with units of time — not the physical stock ratio and not a forecast of aquifer exhaustion.

- *needs check: strength* - the passage hedges with ['can']; this sentence asserts without a hedge

<details><summary>the whole aligned passage</summary>

> Classification, stated at the product's own status: a statistical anomaly index with units of time — not the physical stock ratio and not a forecast of aquifer exhaustion. Its value depends on the product window, basin mask, anomaly reference, and linear-trend convention --- the reference period is the product's declared long-term mean over April 2002 to December 2020, the coverage ends September 2023, and the producer documents a faulty snow-water-equivalent entry for June 2005 that propagates into groundwater storage, recommending that the month be excluded; the window above spans it, so a re-derivation must declare whether June 2005 is retained, since it can move both the fitted trend and the series' own historical minimum; a physical requires an absolute stock estimate and a net stock derivative (aquifer geometry or saturated thickness together with storage parameters), not an anomaly series alone.

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0516 · needs check: strength · draft §6.5.1 · confidence medium · overlap 0.308, ratio 0.349, paired through the aligned passage

**Draft, the claim as the draft makes it.**

> A physical requires an absolute stock estimate and a net stock derivative — aquifer geometry or saturated thickness together with storage parameters — not an anomaly series alone.

**Deposit, the proposition it corresponds to** (§6.5.1):

> Its value depends on the product window, basin mask, anomaly reference, and linear-trend convention --- the reference period is the product's declared long-term mean over April 2002 to December 2020, the coverage ends September 2023, and the producer documents a faulty snow-water-equivalent entry for June 2005 that propagates into groundwater storage, recommending that the month be excluded; the window above spans it, so a re-derivation must declare whether June 2005 is retained, since it can move both the fitted trend and the series' own historical minimum; a physical requires an absolute stock estimate and a net stock derivative (aquifer geometry or saturated thickness together with storage parameters), not an anomaly series alone.

- *needs check: strength* - the passage hedges with ['can']; this sentence asserts without a hedge

<details><summary>the whole aligned passage</summary>

> Classification, stated at the product's own status: a statistical anomaly index with units of time — not the physical stock ratio and not a forecast of aquifer exhaustion. Its value depends on the product window, basin mask, anomaly reference, and linear-trend convention --- the reference period is the product's declared long-term mean over April 2002 to December 2020, the coverage ends September 2023, and the producer documents a faulty snow-water-equivalent entry for June 2005 that propagates into groundwater storage, recommending that the month be excluded; the window above spans it, so a re-derivation must declare whether June 2005 is retained, since it can move both the fitted trend and the series' own historical minimum; a physical requires an absolute stock estimate and a net stock derivative (aquifer geometry or saturated thickness together with storage parameters), not an anomaly series alone.

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0622 · needs check: strength · draft §8.2 · confidence high · overlap 0.691, ratio 0.702, paired through the aligned passage

**Draft, the claim as the draft makes it.**

> - Admitted object. The one-pool affine approximation behind the anomaly-persistence index of §6.5.1. - Not established. The two-pool model — active storage with a slow donor pool, the two-compartment structure of §2.2.

**Deposit, the proposition it corresponds to** (§8.2):

> The groundwater template enters at registered status with one admitted object and one declared gap: the admitted object is the one-pool affine approximation behind the anomaly-persistence index of Section 6.5.1, and the two-pool model --- active storage with a slow donor pool, the two-compartment structure of Section 2.2 --- is not established.

- *needs check: strength* - the passage hedges with ['may']; this sentence asserts without a hedge

<details><summary>the whole aligned passage</summary>

> The groundwater template enters at registered status with one admitted object and one declared gap: the admitted object is the one-pool affine approximation behind the anomaly-persistence index of Section 6.5.1, and the two-pool model --- active storage with a slow donor pool, the two-compartment structure of Section 2.2 --- is not established. The registered identification requirements for closing that gap, and the discipline that leakage terms may not absorb unexplained residuals, are the subject of the supplementary's S2.1, and none of them is met by the record used in Section 6.5; the registration as this article previously stated it is the supplementary's S14.

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0646 · needs check: strength · draft §9 · confidence high · overlap 0.579, ratio 0.54, paired through the aligned passage

**Draft, the claim as the draft makes it.**

> The memory–effort pair is the gated three-state core and working four-state core of the companion delay-dynamics analysis (*in review*; eq.

**Deposit, the proposition it corresponds to** (§9):

> What the proposition does not claim is the next step, and the distinction is the point of stating it: the memory-effort pair is the gated three-state core and working four-state core of the companion delay-dynamics analysis (under review; its eq.

- *needs check: strength* - the passage hedges with ['would']; this sentence asserts without a hedge

<details><summary>the whole aligned passage</summary>

> What the proposition does not claim is the next step, and the distinction is the point of stating it: the memory-effort pair is the gated three-state core and working four-state core of the companion delay-dynamics analysis (under review; its eq. (1), the gated three-state core, and its Section 2.4, which relates that core to the working four-state model), not an object of this article, and the semiconjugacy condition on the history phase space --- which would carry closed-block results across to that system --- is made under the citation and is not re-proved here.

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______

### D0647 · needs check: strength · draft §9 · confidence medium · overlap 0.429, ratio 0.224, paired through the aligned passage

**Draft, the claim as the draft makes it.**

> (1) and §2.4 of that analysis), not an object of this article; the projection claim — the semiconjugacy condition on the history phase space — is made under that citation and is not re-proved here.

**Deposit, the proposition it corresponds to** (§9):

> (1), the gated three-state core, and its Section 2.4, which relates that core to the working four-state model), not an object of this article, and the semiconjugacy condition on the history phase space --- which would carry closed-block results across to that system --- is made under the citation and is not re-proved here.

- *needs check: strength* - the passage hedges with ['would']; this sentence asserts without a hedge

<details><summary>the whole aligned passage</summary>

> What the proposition does not claim is the next step, and the distinction is the point of stating it: the memory-effort pair is the gated three-state core and working four-state core of the companion delay-dynamics analysis (under review; its eq. (1), the gated three-state core, and its Section 2.4, which relates that core to the working four-state model), not an object of this article, and the semiconjugacy condition on the history phase space --- which would carry closed-block results across to that system --- is made under the citation and is not re-proved here.

</details>

**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, the deposit should say it ☐ other: ______


---

## Where the rest of the ledger is


Every row, including the supported ones, is in `claim_ledger_v1.csv` (one row per sentence, `adjudication` column empty) and in `claim_ledger_v1.json` (the same rows with the full aligned passage attached). Nothing was dropped from the CSV to shorten this file: 719 sentences, 263 supported-reworded, 200 near-verbatim, and the 64 above.

# Typed Flux Ledgers and Depletion Arithmetic
### Conservation, componentwise diagnostics, and the semantics of depletion horizons

*Amin Abaee — Independent Researcher — ORCID 0000-0002-0019-1842 — amin_abaee@ut.ac.ir — 6 September 2026*

> **How to read this version.** This is a plain-language rendering of the article. The argument, the numbers, the tables, the named examples and every stated limit are the author's own. What changed is the language: shorter sentences, everyday words, and a plain gloss the first time a technical term appears. Nothing was removed to make it read more smoothly. If a claim in the article is uncertain, it is still uncertain here. If a number is labelled "illustrative" in the article, it is labelled "illustrative" here too.
>
> **The four status labels, in everyday words.** Throughout the article, every object carries one of these:
> - **established** — proved here, with the proof in the text.
> - **registered** — an agreed, checkable fact about data or an interface: it is filed, not proved.
> - **illustrative** — a worked example with invented parameters. It shows what the machinery does. It is not a measurement of anything.
> - **quarantined** — a number we produced and are deliberately *not* releasing as a finding, with the reason stated.
>
> Two more labels appear for things the article refuses to do: a **non-example** is a quantity someone might expect here, shown to be undefined; a **banned** construction is not "discouraged" but excluded from the accounting layer.
>
> *Key words (unchanged):* material flow accounting; stock–flow ledger; depletion indicators; first-passage time; conservation laws; composite indicators; reserve life.

---

## Abstract — in plain words, then in the author's terms

**Plain version.** Numbers that are supposed to tell us how soon a resource runs out are traded as if they were all the same kind of number. A "reserve life" of 45 years, a groundwater trend index, and a fishing-pressure timescale are all read as "years left", but each one answers a different question. A second problem is worse: when many different things are added together into a single score, one collapsing component can be hidden by another doing fine. This article builds a bookkeeping layer that refuses both. Each thing in the ledger has a material identity, a container with a boundary, and a unit. Nothing gets added to something else unless the conversion between them is written down. Because of how the containers and flows are wired together, mass cannot quietly appear or vanish. Because every outflow is limited by how much its source holds, no stock goes negative. Services — drinking water, crop yield, fish caught — are readings taken off the ledger, not substances flowing in it.

Three things are then proved, in full, inside the article. First, an identity that lets you recover flows you did not measure from the stock changes you did measure. Second, a reduction: conservation of a material can be checked once, on the wiring, instead of case by case. Third, an envelope theorem that bounds what any admissible flow can do, with a safety-barrier corollary. For the closed ledger with a finite geological donor, five more facts hold: a mass identity for the natural block, non-negativity of all stocks, no resting point at positive extraction effort, an exact description of where the system can rest when extraction stops, and the integrability of extraction against the donor budget.

"Time to depletion" is then split into **three quantities that cannot substitute for one another**: how hard the system is turning over, a ratio computed with rates frozen, and a hitting time conditional on a stated scenario. Bounds are proved for the case of uniform drift. Three public data cases are then classified honestly for what they are. The groundwater anomaly index is a statistical index, not a stock ratio. The phosphate reserve-life figure is arithmetic, not a forecast. The fisheries removals-only time is a pressure scale, not a depletion diagnostic. No weighted average of components can certify that each component is safe, and five bookkeeping rules stop phantom mass. Stochastic passage times are computed against a barrier defined by the record itself, and come with seven explicit statements of what they do not say. Weak and strong sustainability turn out to be two regimes of one system: the test is whether the material cycle can be closed as fast as we use things. Finally, an interface contract fixes the one object this article shares with work on delayed, reviewed institutions, so the two bodies of work cannot be confused. Every depletion claim here is stated with the exact thing it establishes.

**Author's abstract, kept as written.** Depletion numbers circulate under one label while answering different questions. Reserve-life ratios, trend-persistence indices, and removals-only pressure scales are read as "time to depletion" despite measuring different things; compensatory aggregation hides a deficit behind a positive scalar. We separate them with a typed stock–flow accounting layer — a per-moiety ledger that keeps conservation laws typed, so biomass, money, and biodiversity are not summed into one scalar. Conservation follows from the incidence structure of the compartment–flux network; positivity from donor limitation (each primitive outflow vanishes when its donor is empty); services are readouts, not conserved mass. Three certification layers carry a flux-reconstruction identity (an algebraic relation reconstructing unobserved internal fluxes from observed stock changes), a conservation-law reduction, and a flux-bounding envelope theorem. The closed finite-donor ledger satisfies the natural-block mass identity, orthant invariance (state stays nonnegative), no interior rest at positive effort, the vanishing-extraction rest set, and extraction integrability. Depletion time separates into three non-interchangeable quantities — gross turnover intensity, a frozen-rate ratio, and a scenario-conditioned hitting time — with uniform-drift bounds. Three public-data applications are classified: G3P anomaly index is a statistical index, not a stock ratio; phosphate reserve-life ratio is arithmetic, not a forecast; fisheries removals-only time is a pressure scale, not a depletion diagnostic. No nonnegative weighting certifies componentwise nonnegativity, and five double-counting rules block phantom mass. First-passage semantics on declared stochastic surrogates — stochastic passage times against a relative barrier — carry explicit non-claims. Weak and strong sustainability are two regimes of one system, distinguished by whether the material cycle closes at the rate of use. Each depletion claim carries the predicate it actually establishes, with an interface contract fixing the shared object with delay-based institutional dynamics.

> **[Editor's note — flagged for the author, not their claim.]** The abstract's "flux-reconstruction identity" says unobserved *fluxes* are recovered from observed *stock* changes. Lemma 3 in Section 3.3, and its proof, do the reverse: they reconstruct the moiety readout $S(t)$ by integrating observed fluxes. The proof is the authority. See `review/joint_evaluation_v1.md` §2.3/D11.

---

# 1. Introduction

## 1.1 Two ways this kind of accounting goes wrong

Sustainability accounting fails in two characteristic ways.

The first is what we call **compensatory aggregation**: *adding different things together into one score, so that gains and losses can cancel.* Here "compensatory" means exactly that — a shortfall in one place is paid for by a surplus in another. A single number is built from many unlike parts, and the trade between them is never written down as an equation. So one component can be in serious deficit while the overall score looks fine. The literatures on composite indicators and on weak versus strong sustainability document both the failure and the non-compensatory fixes that have been proposed (Munda and Nardo, 2009; Ekins et al., 2003; Neumayer, 2013).

The second failure is **classification drift**: *a number that is described one way gets read as something else.* Several quantities have "years" in their units — reserve-life ratios, trend-persistence indices, removals-only pressure scales — and circulate as if they were one thing: "time to depletion". They are not. They answer different questions from different assumptions.

The drift is easy to see in the numbers themselves.

- A **reserve-life ratio** divides a reserve figure by a production figure. It then calls the answer a horizon: the number of years left at this rate, for as long as the rate and the reserve definition hold.
- A **groundwater anomaly index** fits a trend line to a satellite product, then reports the fitted distance from the fitted curve to the series' own historical minimum, divided by the fitted rate.
- A **fisheries pressure indicator** divides a log biomass margin by a fishing mortality, and presents the result as a timescale.

Each is informative about something. None is what it is usually taken to be.

This first failure has a well-known public object. **Earth Overshoot Day** collapses every component into one calendar date. A severe deficit in one component can therefore coexist with a date that still falls late in the year (Lin et al., 2018; Wackernagel and Beyers, 2019; Blomqvist et al., 2013). The systems-dynamics overshoot models raise the same aggregation question in a moving form (Meadows et al., 1972). What this article builds in their place is resolved by component from the start. The per-asset, per-pool depletion horizons of Section 6.5.2 are each reported next to the pool they draw on, and are never added into a single date.

A third failure mode is what we call the **productivity illusion**: the appearance that a system is producing enough, while the base that lets it produce is being reduced. The word "illusion" is doing real work here. Nothing is hidden by anyone. The bookkeeping is simply silent, and everyone reads the number that is present. The illusion has two senses, and they are distinct.

The first sense is arithmetic. It is the compensatory-aggregation failure above: a deficit in one component is offset by a surplus in another, and a positive aggregate reads as adequacy. Section 10.1 formalises this sense as an aggregation obstruction.

The second sense is dynamical: inflated yield. A measured yield can exceed the true sustainable yield when it is held up by drawing down the support pool — groundwater, soil carbon, available nutrients — instead of by the pool's own regrowth. The resource looks productive while what sustains it is being sold off. "Support pool" means exactly one thing here: a stock that receives the current draw and is not renewed as fast. The diagnosis does not need a superficially non-renewable reserve. The same pool can also be read as natural capital, as a stock, or as a slowly regenerating flow of services. These are overlapping readings of one pool, not rival claims about it.

Every such pool regrows on some timescale. A crop within a season. An aquifer within years to decades. A mineral deposit over geological time. The failure is identical in all three cases. What decides it is the ratio between the pool's renewal rate and the rate at which it is used. A draw that falls on the pool's regrowth is sustained use. A draw that falls on the pool itself is liquidation. So a drawdown is recoverable only insofar as the pool regrows faster than it is taken. If a pool regrows too slowly for the rate at which it is taken, the drawdown is liquidation however large the pool is. The size of a pool is a property of the resource. Whether its drawdown is recoverable is a property of the rate.

This is where the "depletion paradox" belongs. It is a **non-example** in our terms, not a result: the intuition that a huge deposit is therefore safe is not a claim the ledger can even state, because size and recoverability are quantities of different kinds.

Two design choices follow from this reading, and both are load-bearing.

The first is that a measured yield is booked against its own generating flux, never against a stock level. A revenue or an extraction rate is recorded from the flow that produced it. That is why support drawdowns cannot be traded against revenue anywhere in the ledger.

The second is that the two-pool architecture exists to detect the wear phase of the productivity illusion. In plain terms: it is built to make a hidden drawdown visible while the yield line still looks normal. It is built to detect this phase, and no more. That distinction has teeth, because the article does not oversell it. No two-pool model is claimed as established. The groundwater two-pool model is a **registered open gap**, and the applied object actually admitted is a one-pool affine approximation (Section 8.2). Spawning biomass is explicitly not an abiotic support pool (Section 6.5.4). And "the stock is large" is not an available argument at all: size and recoverability are different kinds of quantity, and every depletion horizon in this article is stated against a rate and a barrier.

The asymmetry that makes this second sense dangerous has a mechanical picture. An elevator rated for ten people will carry fourteen for a long time. The cable does not part on the fourteenth passenger. It parts later, under accumulated wear that the passenger count never shows. During the overshoot nothing announces the damage. The wear is diffuse, gradual, and invisible to everyone riding. The snap, when it comes, is sudden and total. The productivity illusion is the wear phase: measured yield stays up, and nothing in the yield record registers the drawdown. The two-pool architecture exists to make the wear measurable while the cable still holds. Not to predict the snap. Section 7 states what the passage-time results do and do not condition on, and it is not a snapping-time calculation.

What Section 6.5.2 actually reports is per-resource, per-pool horizons for each component, at each object's own status. There is no "supporting pool" column, because the applied data do not carry one.

**Why reserve-life arithmetic is not a forecast.** The classification-drift failure is well documented on the data side. A reserve-life ratio is arithmetic: reserves left, divided by current production. Because reserves are an *economic* classification — they move with price, technology, exploration, and regulation — the quotient is not an exhaustion forecast. "Reserves" in this article means exactly one thing: the economically extractable portion as classified by the publishing agency, at the vintage of the report, in the report's own units. This is the USGS/industry definition and not any other. The critique has been made forcefully for phosphate. Illakwahhi, Vegi and Srivastava (2024) show that influential "depletion within a century" estimates rest on single-source US Geological Survey data of questionable credibility, ignore recovery and recycling, and that timeframes estimated from inadequate reserve data "are somewhat misleading". The same point is standard in mineral economics, where the reserves-versus-resources distinction has been central at least since Tilton (2003). The United States' phosphate reserves have stayed near 1,000,000 kt for decades, while cumulative production since 1996 is of the order of 600,000 kt. The classification refills itself, and any ratio built on it inherits that behaviour. For copper, Tilton and Lagos (2007) document reserves growing through a century of rising production. Same classification, same replenishment.

**The same conflation runs through accounting itself.** Material flow analysis supplies the bookkeeping of a society's material throughput (Brunner and Rechberger, 2004; Eurostat, 2001; Fischer-Kowalski et al., 2011). Its wiring is shared with reaction-network theory, where the signs in the stoichiometric matrix are themselves a conservation object (Feinberg, 2019). But four things look alike and are not the same thing:

1. **bookkeeping balance** — the accounts add up;
2. **stoichiometric conservation** — the declared materials are conserved by construction;
3. **thermodynamic admissibility** — the flows are physically possible;
4. **sustainability safety** — the declared limits hold.

The literature slides between them. A mass-balanced ledger can be chemically impossible. A chemically consistent ledger can break every declared barrier. A ledger that satisfies all declared barriers can fail conservation. Separating these layers, and proving what each one buys, is this article's first task (Section 3). "Each claim carries the predicate it actually establishes" is the exact discipline that sentence names.

## 1.2 What this article builds, and what it refuses to

**Task two is non-compensation.** Ecological economics has a thesis called weak comparability: the values that matter in environmental decisions may not be commensurable in one metric (Martinez-Alier, Munda and O'Neill, 1998). In material accounting the thesis has a precise algebraic form, stated in Section 10.1: **no non-negative weighting of component balances can certify that every component clears its floor.** A positive weighted sum never proves that the individual parts are non-negative. A scalar can rank, and a scalar can communicate. Certification needs the vector.

**Task three is to put substitution inside the ledger, not beside it.** Weak and strong sustainability are not rival hypotheses. They are two regimes of one dynamic system. What separates them is not whether substitution alone keeps up with depletion, but whether the material cycle can be closed at the rate of use. This is a reading built for the ledger. It is not the received distinction in the literature, which turns on whether natural capital can be substituted (Neumayer, 2013; Ekins et al., 2003).

*Weak sustainability* is the idealised regime. People consume and multiply slowly enough that technological substitution and natural regeneration together move matter so that it is used as it appears. On timescales people care about, substitution is the dominant term. Natural regeneration is far slower, sometimes on geological timescales, and it is included for physical completeness rather than as a co-equal mechanism (Daly, 1990).

That "deep time" clause needs a scope, because read too widely it would sit badly against the article's own recoverability rule. It applies only to the slow compartments: geological donors and mineral stocks, which renew on deep time. It does not apply to the compartments the applied record actually tabulates. Those renew on human timescales — a crop within a season, an aquifer within years to decades, a fish stock within years. For them, regeneration is a co-equal or dominant term, and the regime is decided by the rate of use against that renewal rate, not by any deep-time regrowth.

In this idealised closure, the by-products of use — carbon taken from the atmosphere, chemicals released to air, water and soil — come back into use in time. So they are not waste. **Waste is a relationship, not a property of a substance.** Waste is matter that, under the present relation and the present circumstances, accumulates because there is not yet the knowledge, the technology, or the timely redistribution to use it. A chemical that is a product in one setting is waste-in-waiting in another. Nothing is waste by its nature.

*Strong sustainability* is the regime where the closure fails: either because no identified physical pathway re-routes the extracted matter, or because depletion outruns the rate at which such a pathway could be built. Substitution is admissible only where a physical pathway has been identified and does not draw a different critical stock down. No substitute counts just because an aggregate production function or a weighted index allows it. In ledger terms a substitute is one of two things: a recycled or recovered flux returned to the regenerating pool, or a non-renewable drawdown taken from a second compartment. They are different entries, and they carry different statuses (Sections 2.3 and 6).

**The two regimes are two readings of one object.** The scalar reading is $B = b\cdot M$: total regeneration flow, with $b$ the regrowth rate per unit mass and $M$ the mass of the natural block. These two letters are local to the introduction, because from Section 2.2 onwards $B$ means something else (gross turnover $R+T$) while $M$ keeps its natural-block meaning. Against consumption, $B$ is the weak-sustainability flow check: does the cycle close in total? The multi-compartment ledger is the vector reading: does the cycle close only by emptying a critical compartment or by over-filling the waste one? That is, is a local depletion or a waste pile-up just being moved off the books?

Both readings are needed, and neither demotes stocks. The ledger keeps stock compartments first-class, and it supplies the thresholds, hitting times and sink constraints from which $B$ is derived. The scalar reading is the operational overshoot test, run on top of that.

Both readings are instantaneous. A one-period check says nothing about what has to hold over time, namely that the checks do not drift into overshoot as the system moves. The balance has to hold while neither consumption nor population grows faster than the productivity supporting them, and the drawdown must not be recoverable only on a timescale longer than the time it takes to draw it down. The scenario-conditioned hitting time of Section 6.5.2 exists to give that drift a horizon. The reserve classification carries the same point: a horizon estimate built on reserves inherits the substitution and technology assumptions inside the classification, which is why it is read as a ratio, never as a forecast.

So this article builds the accounting layer that resists these failures. Its objects are typed ledgers in which conservation follows from the wiring, positivity follows from donor limitation, services are readings rather than conserved mass, and every depletion quantity carries its own classification, stated at its actual strength.

**Contributions, with each one's status.**

1. **A typed primitive-flux ledger.** *(definitions; §2)* Every compartment has a material identity, a boundary and a unit. Non-negative primitive fluxes connect compartments through a signed incidence matrix — the compartment-and-flow bookkeeping of material flow analysis (Brunner and Rechberger, 2004; Fischer-Kowalski et al., 2011) and the incidence formalism of reaction-network theory (Feinberg, 2019). Conversions between types appear only as explicit stoichiometric coefficients. Every one-way transfer is donor-limited: it cannot exceed what its source holds.
2. **Three certification layers, separated and proved.** *(theorems; §3)* Accounting consistency (the balance law holds), conservation consistency (the declared moieties are invariant up to boundary flows) and barrier safety (the declared lower and upper barriers hold) are different predicates with different proof obligations. The flux-reconstruction identity, the conservation-law reduction and the flux-bounding envelope theorem — with a barrier-certificate corollary — are proved in full.
3. **The closed finite-donor theorem set.** *(theorems; §4)* For the closed ledger in which the geological donor is a state and no derived target appears: the natural-block mass identity, orthant invariance, no interior rest point at positive effort, the vanishing-extraction rest set (extinction, carrying capacity, and the frozen-biomass face), and integrability of extraction against the finite donor budget. Positivity is proved face by face using the tangent cone (Aubin, 1991); the classical compartmental-systems non-negativity theory (Jacquez and Simon, 1993) is the lineage.
4. **Depletion arithmetic.** *(taxonomy and bounds; §6.1–6.5)* Depletion time is split into three non-interchangeable quantities — gross turnover intensity, a frozen-rate ratio, and a scenario-conditioned hitting time — extended to upper barriers, infimum exit times and infinite-horizon maintainability, with uniform-drift bounds proved and the failure of "positive extraction implies finite exhaustion" shown by counterexample.
5. **Application classifications at exact status.** *(classification; §6.5)* The G3P anomaly-persistence index, the phosphate reserve-life ratio and the fisheries removals-only pressure time are classified as what they are — statistical index, arithmetic ratio, pressure scale — against the published critiques they corroborate.
6. **First-passage semantics on declared surrogates.** *(derivations with stated non-claims; §7)* The inverse-Gaussian groundwater passage and the geometric-Brownian fisheries passage are stated with complete derivations, the record-relative-barrier discipline, and seven explicit non-claims separating them from the ledger.
7. **The interface with institutional dynamics.** *(interface contract; §9)* The exact shared object with delay-based institutional models is the single-resource deficit identity $q e_N - R = -\dot N$. The boundary is the non-reduction theorem: there is no exact dynamic reduction from the closed ledger to the open working system, for five stated mathematical reasons.

**What is not claimed.** The article is as explicit about what it does not establish. No stochastic completion of the ledger is claimed: the surrogate processes of Section 7 do not conserve the ledger's mass and are not small perturbations of its dynamics. No thermodynamic admissibility is claimed. No identification of the two-pool groundwater hypothesis is claimed — its identification requirements are registered in Section 8, not discharged. And no empirical finding about any basin, aquifer or fishery is claimed beyond the descriptive status of the tabulated indicators. That is the standing rule of this article, and it is stated in the abstract, here, and again in Sections 7.7, 8, 10.4 and 11, because it is the rule that would otherwise be lost in the middle.

## 1.3 How the article is organised

Section 2 defines the typed ledger. Section 3 develops the certification layers and the accounting theorems. Section 4 proves the closed-ledger theorem set. Section 5 adds the service layer and the componentwise deficit. Section 6 develops the depletion taxonomy, the uniform-drift bounds and the application classifications. Section 7 supplies first-passage semantics. Section 8 records the domain templates at registered status. Section 9 fixes the interface with delay dynamics. Section 10 states what the ledger does not support, and Section 11 concludes.
# 2. The typed ledger — what gets recorded, and in which box

> **In plain words.** This section builds the ledger. Four rules do all the work. (1) Every box holds one named material in one named place, with one unit. (2) Nothing moves without a named flow. (3) A flow can only take out what its source box holds. (4) Two boxes can be added together only when the conversion between them is written down. Because of rule 4, conservation is a property of the wiring, not a hope about the data.

**Notation discipline.** One letter carries one kind of thing wherever a computation is displayed. Section-local aliases are declared where they occur. The incidence operator is never written $N$ — that letter is reserved for the living stock. The table below sits at the head of Section 2 so that every alias is declared before it is used.

| Symbol | Means | Where |
|---|---|---|
| $N$ | living stock; nutrient stock *(local to §2.4)* | §2.2; §2.4 |
| $S^{\top}$ | typed stoichiometric (incidence) operator | §2.1, Lemma 3, Prop. 4, Thm 5, Thm 8 |
| $v$ | non-negative primitive flux vector | §2.1 |
| $S$ | moiety readout $S=Cx$ | Lemma 3, §6 |
| $s$ | support factor $A_{\mathrm{act}}/(A_{\mathrm{act}}+A_0)$ | §2.2 |
| $\sigma$ | donor fraction $A_{\mathrm{geo}}/(A_{\mathrm{geo}}+A_{g0})$ | §2.2 |
| $\varsigma$ | noise scale of the stochastic surrogates | §7 |
| $M$ | natural-block mass $N+A_{\mathrm{act}}+A_{\mathrm{geo}}+U$ | Thms 7, 14 |
| $\hat M$ | demand-coverage matrix of the physical deficit | §5.4 |
| $K$ | carrying capacity; sink stock *(local to §2.4)*; maintainability kernel $K_{\mathrm{maint}}$ *(subscripted)* | §2.2; §2.4; §6.3 |
| $T$ | gross uptake $\kappa_A N s$; finite horizon *(local to each statement)* | §2.2; Thms 1, 5 |
| $C$ | moiety-composition matrix; operative extraction-law readout; mining intensity $C_A$ | Lemma 3; §5.4; §2.2 |
| $B$ | $R+T$; barriers *(local to §3.1)*; aggregate regeneration flow $b\cdot M$ *(local to §1.1)*; fisheries biomass $B_t$ and barrier $B_{\min}$ *(local to §7.5)*; reference $B_{\mathrm{lim}}$ *(local to §6.5.2, §6.5.4)* | §2.2; §3.1; §1.1; §6.5.2 |
| $b$ | boundary-transfer term; service balance $b_i$ *(subscripted)*; specific regeneration rate *(local to §1.1)* | Lemma 3, Prop. 4, Thm 5; §5.1; §1.1 |
| $R$ | net regeneration; log margin $R_B$ *(local to §6.5.4)* | §2.2; §6.5.4 |
| $r$ | intrinsic growth rate; net boundary inflow $r_m$ *(subscripted, §3.3)* | §2.2; §2.6; §3.3 |
| $G$ | geological pool (scaffold); reserves *(local to §6.5.3, §7.6)*; donor stock $G_0$ *(subscripted)* | §2.3; §6.5.3; §9 |
| $I$ | inert sink; boundary input $I_N$ *(subscripted)* | §2.2; §2.4 |
| $z$ | six-compartment state *(local to §2.3)* | §2.3 |
| $h$ | harvest primitive; net boundary outflow $h_m$ *(subscripted, §3.3)*; geometric-Brownian drift *(local to §7.5)* | §2.3; §3.3; §7.5 |
| $x$ | ledger state | §2.1, Lemma 3, Prop. 4, Thm 5 |
| $y$ | declared boundary states feeding the primitive fluxes | §2.1, eq. (1) |
| $\theta$ | declared constitutive parameter vector; sink-generation fraction $\theta_K$; parameter set $\Theta$ and fisheries pressure time $\Theta_F$ *(distinct objects)* | §2.1, eq. (1); §2.4; §6.4, §6.5.4 |
| $E$ | extraction effort, $E\ge 0$ along classical solutions | §2.2; §4.5; Thm 14 |
| $\alpha$ | harvest routing fraction; directional support fraction $\alpha_{\mathrm{reg}}$ | §2.2–2.3, §4.2; §5.3 |
| $\rho_P$ | product-retirement fraction routing $r_P$ to $U$ versus $W$ | §2.3; §4.3; §4.4; §8.1 |
| $\mu,\nu,\rho$ | product, waste and price parameters of the unreduced ledger (zero in the single-resource specialization); $\mu$ also the growth parameter of Theorem 1 and the drift of the §7 surrogates; $\nu$ also the inverse-Gaussian mean *(local to §7.3)* | §2.2; §5.4; §9 |
| $\varepsilon$ | drift bracket (Prop. 17); probabilistic level (§6.4); resource-threshold fraction (§6.5.2, §7.6); donor-draw diagnostic $\varepsilon_G$; slack (§10.1) | §6.2; §6.4; §6.5.2; §9; §10.1 |
| $\tau$ | hitting and exit times ($\tau_B$, $\tau_m^{\pm}$, $\tau_{\mathrm{exit}}$) | §3.6; §6.3 |
| $d$ | disturbance (§2.1); demand vector (§5.2); drift distance *(local to §7.3)* | §2.1; §5.2; §7.3 |
| $A_0$ | half-saturation constant (§2.2); latest observed anomaly *(local to §7.2–7.4)* | §2.2; §7.2 |
| $\lambda$ | inverse-Gaussian shape parameter | §7.3 |
| $\chi,\eta$ | hybrid state and primitive-flux vector of Conditional Theorem 15 | §4.8 |
| $P$ | product compartment; production rate *(local to §6.5.3, §7.6)* | §2.2–2.3; §6.5.3 |

## 2.1 Typed stocks, primitive fluxes, and the incidence discipline

Material flow accounting starts from a few distinctions. Unlike substances must be tracked separately. Place and function must be distinguished. Conversions between chemical forms must be written out. This section sets out the discipline that makes conservation a property of the structure rather than an assumption.

The ledger separates four ideas that accounting practice tends to merge.

- A **moiety** is a conserved substance class — an element, or a declared conserved combination. It is the only kind of object a conservation law attaches to.
- A **species** is a chemical or biological form of a moiety.
- A **compartment** is a place, spatial or functional, that holds a stock.
- A **stock** is the amount of a species currently in a compartment, with a physical unit.

"Carbon in the atmosphere" is a place-specific stock, not a moiety. Carbon is the moiety; the atmosphere is a compartment. Conservation laws are stated per moiety. **Nothing is conserved merely by being a compartment.**

A ledger state $x\in\mathbb{R}^m_+$ collects compartments, and each entry carries a material identity, a spatial support and a physical unit. Internal dynamics use non-negative primitive fluxes:

$$\dot x = S^{\top} v(x,y,\theta) + B\,u_\partial(t) + d\,x(t),\qquad v\ge 0 \tag{1}$$

Read this line in words: *what changes in each box equals the wiring applied to the flows, plus what crosses the boundary, plus a stated disturbance.* Here $S^{\top}$ is the typed stoichiometric (incidence) operator; $y$ collects declared boundary states — environmental or companion variables that live outside the ledger; $\theta$ is the declared constitutive parameter vector; $B u_\partial$ collects declared boundary transfers; and $dx$ belongs to a stated disturbance class.

Entries are added within a row only when their types and units agree. A conversion between types is an explicit stoichiometric coefficient, never an implicit sum.

If $L^{\top}S^{\top}=0$, then $\tfrac{d}{dt}(L^{\top}x) = L^{\top}B u_\partial + L^{\top}dx$: one conservation law per conserved moiety and boundary. That identity does **not** create a single scalar sustainability mass across incommensurable systems.

Three clarifications are part of the statement.

1. $dx$ must itself be typed. A physical disturbance on represented material is a different object from a structural discrepancy term.
2. $S^{\top}$ may contain signed entries even though $v\ge 0$. The sign pattern of the incidence matrix and the non-negativity of the primitives are separate declarations.
3. Forward invariance is a separate requirement. Every primitive outflow must vanish or be limited when its donor compartment is empty, and a target-relaxation flux from a finite donor is admissible **only after** donor limitation is made explicit.

## 2.2 The closed finite-donor ledger

The closed ledger of this article is the finite-donor primitive system. Let $x_L=(N,A_{\mathrm{act}},A_{\mathrm{geo}},U)$, with $N$ the living stock, $A_{\mathrm{act}}$ the active abiotic pool, $A_{\mathrm{geo}}$ the geological donor and $U$ the detritus compartment. Two saturation factors and three constitutive laws do the work:

$$s=\frac{A_{\mathrm{act}}}{A_{\mathrm{act}}+A_0}\ (\text{support factor}),\qquad \sigma=\frac{A_{\mathrm{geo}}}{A_{\mathrm{geo}}+A_{g0}}\ (\text{donor fraction}),$$
$$R(N,A_{\mathrm{act}})=rN\Big(1-\frac NK\Big)s,\qquad T=\kappa_A N s,\qquad B=R+T.$$

$R$ is net regeneration — how much new living stock appears. $T$ is gross uptake — how much mineral the living stock pulls in. $B$ is gross turnover: everything the biota moves, whether or not it stays. The four geo-interface and closure primitives are

$$e_{GA}=\omega_A A_{\mathrm{eq,intrinsic}}\,\sigma,\qquad e_{AG}=\omega_A A_{\mathrm{act}},\qquad C_{A,\mathrm{lim}}=C_A\sigma,\qquad \gamma_U U\ \text{(detritus return)}.$$

These donor primitives instantiate one of **three recharge laws** that appear across this article and the companion delay-dynamics analysis (Author, D., et al., *in review*). The three are distinct objects. They are tabulated once so that none is silently substituted for another.

| Recharge law | Form | Status |
|---|---|---|
| **Primitive donor-limited exchange** | $e_{GA}=\omega_A A_{\mathrm{eq,intrinsic}}\sigma$ | The closed block's law (§2.2). The forward rate depends on the donor alone, not on how empty the receiving pool is — linear donor-limited exchange, whose rest is $A_{\mathrm{act}}=A_{\mathrm{eq,intrinsic}}\sigma$ (Theorem 13). |
| **Target-relaxation** | $\omega_A(A_{\mathrm{eq}}-A)$ | **Banned unless donor-limited** (§4.4): it runs *backward* at an empty donor. Admissible only with the source declared an effectively infinite external reservoir — which makes the system open. |
| **Working derived target** | $A_{\mathrm{eq},W}=A_{\mathrm{eq,intrinsic}}+\kappa_A K/\omega_A$ | The delay-dynamics analysis's working completion (that analysis; this article's §9). Not a closed-block law, and the reason the two systems do not reduce. In the closed block **no derived target appears**. |

In the closed block, recharge is donor-limited and cannot run backward: $e_{GA}=0$ at $A_{\mathrm{geo}}=0$. The positive-part convention $[\cdot]_+$ — read as a one-way valve at a non-positive target — never binds here, because the registered intrinsic target is positive. Mining $C_{A,\mathrm{lim}}$ is donor-limited in the same way extraction is. With $A_{g0}>0$ the donor fraction $\sigma$ is smooth and strictly increasing in the donor level.

Under the **institutional-failure specialization** ($\mu=\nu=\rho=0$ and $C_A=0$ — the product, waste and price parameters of the unreduced ledger, its macroeconomic-feedback, recycling and price-response channels, set to zero together with the mining intensity $C_A$; the parameters are glossed at their §5.4 site) the closed natural block is

$$\dot N=R-qEN,\qquad \dot A_{\mathrm{act}}=-B+e_{GA}-e_{AG}+\gamma_U U,$$
$$\dot A_{\mathrm{geo}}=-e_{GA}+e_{AG},\qquad \dot U=T-\gamma_U U. \tag{2}$$

This comes with a **memory–effort pair** $(Z,E)$ driven by $qEN-R$ — never by mining; $q$ is the per-effort extraction coefficient of the harvest law. The pair is the registered object of the companion delay-dynamics analysis (Author, D., et al., *in review*; eq. (1) and §2.4 of that analysis) and is **not analysed in this article**.

Net regeneration is the difference of two non-negative primitives — gross regeneration $rNs$ (support → stock) and density-dependent return $rN^2s/K$ (stock → support) — so (2) stays inside the primitive-flux discipline of §2.1 despite the signed entry.

The block's harvest routing is the $\alpha=0$ corner of §2.3: harvest $qEN$ leaves the natural block entirely as product. A positive detritus-routed fraction $\alpha>0$ would add $\alpha qEN$ to $\dot U$ and reduce the block export to $(1-\alpha)qEN$. The mass identity of Theorem 7 is stated **for the declared routing**.

The **registered parameterization** is

$$r=0.02,\quad K=100,\quad q=0.001,\quad \kappa_A=0.05,\quad \omega_A=10^{-3},\quad A_0=1,\quad A_{\mathrm{eq,intrinsic}}=50,\quad \gamma_U=0.2.$$

The geological half-saturation $A_{g0}$ is declared positive (for smoothness of $\sigma$) under the separation-of-scale condition $A_{\mathrm{geo}}\gg A_{g0}$, a regime in which $\sigma\approx 1$. The scale separation is **registered rather than a numerical value**, and the $A_{g0}=0$ corner is the discontinuous-perturbation limit, not the registered regime.

With $A_0>0$ and $A_{g0}>0$ the right-hand side of (2) is locally Lipschitz on the closed orthant, and the comparison $\dot N\le rN(1-N/K)$, with $\dot N\le0$ once $N\ge K$, bounds the stock by $\max\{N(0),K\}$. Classical solutions therefore exist globally and stay in the orthant by Theorem 10 — the existence clause behind every "classical solution" statement below.

Written out for the closed block, the incidence discipline of §2.1 is the four-row block incidence. Rows are $(N,A_{\mathrm{act}},A_{\mathrm{geo}},U)$; the eight columns are gross regeneration $rNs$, density-dependent return $rN^2s/K$, harvest $qEN$, uptake $T=\kappa_A Ns$, detritus return $\gamma_U U$, geological recharge $e_{GA}$, geological return $e_{AG}$, and mining $C_{A,\mathrm{lim}}$:

```
            rNs   rN²s/K  qEN   T     γ_U U  e_GA  e_AG  C_A,lim
  N          1     −1      −1     0     0      0     0      0
  A_act     −1      1       0    −1     1      1    −1      0
  A_geo      0      0       0     0     0     −1     1     −1
  U           0      0       0     1    −1      0     0      0
```

Every column is a two-compartment transfer or a boundary export. The six internal columns sum to zero. The two exports — harvest and mining — each carry the column sum $-1$. So summing the four rows reads off

$$\dot M=-qEN-C_{A,\mathrm{lim}},\qquad M=N+A_{\mathrm{act}}+A_{\mathrm{geo}}+U,$$

the mass identity proved as Theorem 7, directly from the display. Under the institutional-failure specialization the mining column is inactive ($C_A=0$). The harvest column is written at the declared $\alpha=0$ routing, under which harvest leaves the block; a detritus-routed fraction $\alpha>0$ moves $\alpha$ into the $U$ entry of that column and reduces the block export to $(1-\alpha)qEN$ — the full-ledger routing displayed in §4.2.

When product, waste and the inert sink are restored with the same donor-limited routing, the full ledger $N+A_{\mathrm{act}}+A_{\mathrm{geo}}+U+P+W+I$ is closed (§4.2). The geological donor is an internal state throughout — **no infinite reservoir is declared** — and the block boundary is crossed only by harvest (to product) and, when restored, mining (to product or waste). The full seven-compartment incidence is the nested completion of this four-block routing.

One routing point is easy to misread, so it is stated where it is first used. Uptake $T=\kappa_A Ns$ never enters $\dot N$. It is an $A_{\mathrm{act}}\to U$ throughput in which the living stock appears as a catalytic factor, not as stored biomass. That is legitimate in a monomaterial projection, and the masses below are defined on this routing.

## 2.3 The six-compartment illustration

For one conserved limiting material, the scaffold is instantiated by six compartments — living biomass $X$, detritus or recoverable residual $U$, active abiotic pool $A$, geological or slowly available pool $G$, product or in-use stock $P$, and absorbing or currently unavailable stock $W$ — with eight non-negative primitive fluxes: assimilation $g(X,A)$, mortality $m(X)$, harvest $h(X,E)$, decomposition $d_U(U)$, geological-to-active transfer $e_{GA}(G,A)$, active-to-geological transfer $e_{AG}(A,G)$, direct mining $c_G(G,E_G)$, and product retirement $r_P(P)$. With harvest fraction $\alpha\in[0,1]$ routed to $U$ and retirement fraction $\rho_P\in[0,1]$ returning to $U$ rather than $W$,

$$\dot z=S(\alpha,\rho_P)\,v(z,u),\quad z=(X,U,A,G,P,W)^{\top},\quad v=(g,m,h,d_U,e_{GA},e_{AG},c_G,r_P)^{\top},$$

$$S(\alpha,\rho_P)=\begin{pmatrix} 1&-1&-1&0&0&0&0&0\\ 0&1&\alpha&-1&0&0&0&\rho_P\\ -1&0&0&1&1&-1&0&0\\ 0&0&0&0&-1&1&-1&0\\ 0&0&1-\alpha&0&0&0&1&-1\\ 0&0&0&0&0&0&0&1-\rho_P \end{pmatrix},\qquad \mathbb{1}^{\top}S=0 .$$

In words: each column is one flow, and each column has a $+1$ where the flow arrives and a $-1$ where it leaves. So every column sums to zero, which is the incidence statement of mass conservation (proved for the full system in §4.2). The matrix is what makes the routing choices visible.

The constitutive choices belong to this example, not to every typed ledger: the constant splits $\alpha$ and $\rho_P$, the compartment set, and the absorbing-sink convention are declared choices. The construction is a **monomaterial projection**. Coupled multi-element accounts need additional typed rows and a conservation matrix. If an application makes recovery claims, $U$ and $P$ must be split by material, location and quality grade, with declared yields, residual routes and exergy or capacity inputs; the conservation argument then applies to that expanded typed incidence system, not automatically to an undifferentiated quality-neutral loop.

The four-block system (2) is **not** a specialization of this scaffold. In the scaffold, assimilation $g$ is a slow $A\to X$ flux and mortality $m$ a slow $X\to U$ flux. In (2), the uptake $T$ transfers $A_{\mathrm{act}}\to U$ with the living stock catalytic and no separate mortality primitive. These are two different timescale lumpings of the same physical story, and no incidence specialization maps one onto the other.

## 2.4 The four-stock resource–sink–nutrient–product system

A second exact specialization closes a resource–sink system by adding a nutrient stock and a product stock. The state is $(\mathsf{S},\mathsf{K},\mathsf{N},\mathsf{P})\in\mathbb{R}^4_+$ — in this block's local notation, resource stock, sink stock, nutrient stock and input flux; the carrying capacity and living stock of §2.2 do not enter — with

$$\dot{\mathsf S}=g(\mathsf S,\mathsf N)-H,\qquad \dot{\mathsf K}=\theta_K H-\theta_\delta \mathsf K,$$
$$\dot{\mathsf N}=-g(\mathsf S,\mathsf N)+\theta_\delta\mathsf K+I_{\mathsf N},\qquad \dot{\mathsf P}=(1-\theta_K)H-Q_{\mathsf P},$$

where $\theta_K$ is the sink-generation fraction, $\theta_\delta$ the assimilation rate, $I_{\mathsf N}$ external nutrient input and $Q_{\mathsf P}$ product disposal. Adding the four equations gives the mass balance

$$\frac{d}{dt}(\mathsf S+\mathsf K+\mathsf N+\mathsf P)=I_{\mathsf N}-Q_{\mathsf P},$$

so total mass is conserved exactly when both boundary transfers vanish. This balance is an exact specialization of the incidence discipline of §2.1: every internal transfer cancels in the column sum, and the boundary terms survive as the ledger's declared inputs and outputs.

**Sink obstructions that do not care what the stock does.** The mass balance has a sink-side physical reading with two empty-kernel mechanisms that operate whatever the resource stock does. With sink loading $w(H)$, assimilation $\delta(K)$ and a harvest floor $H\ge H_{\min}>0$ — in this specialization $w(H)=\theta_K H$ and $\delta(K)=\theta_\delta K$ — two cases close off every option:

1. **No assimilation** ($\delta\equiv0$). Then $\dot{\mathsf K}\ge w(H_{\min})>0$, and the sink exceeds any finite ceiling $K_{\max}$ in finite time.
2. **Weak assimilation** ($\delta(K_{\max})<w(H_{\min})$). The sink load at the ceiling is still positive: $\dot{\mathsf K}=w(H_{\min})-\delta(K_{\max})>0$ at $K=K_{\max}$, so $K$ exits above $K_{\max}$ in finite time. This is the explicit negation of the ceiling condition $\delta(K^\dagger)=w(H_{\min})$ with $K^\dagger\le K_{\max}$.

In both cases the viability kernel (Aubin, 1991) of the constraint set $\{\mathsf S\ge \mathsf S_{\min},\,0\le K\le K_{\max}\}$ — the states from which *some* admissible harvest keeps both constraints forever — **is empty**.

The obstruction needs a sink-generation fraction $\theta_K>0$. If $\theta_K=0$, harvest never loads the sink and the loading argument does not apply; emptiness would then have to come from the resource constraint or from an undeclared ceiling on the product stock.

The closed-ledger corollary is the same mechanism in ledger language. In a closed ledger without recycling, where $w(H)$ enters the sink irreversibly and $\delta=0$, the sink rises monotonically against the finite total mass, and any positive output floor forces an empty viability kernel. Which constraint fails first depends on the total mass $M$, the ceiling $K_{\max}$ and the remaining stock. A ceiling below the sink's reachable mass share is crossed in finite time; a ceiling at or above the total mass is unreachable, and the constraint violated is the resource floor (the finite-budget bound of Theorem 14).

For material-flow accounting this is the precise sense in which a "balanced" mass ledger can still be **physically inadmissible**: the bookkeeping is exact, but no harvest schedule respects the resource floor and the sink ceiling at the same time.

## 2.5 Mechanism typing: routing is never determined by diagnostic labels

Extraction has at least three different physical meanings.

- **Standing-stock culling** — present extraction removes reproductive stock directly.
- **Recruitment suppression** — present use prevents future recruits, without removing adults now.
- **Weak viability coupling** — use has limited or indirect effect on reproduction.

In the ledger, standing-stock culling enters as an outflow from the standing-stock compartment. The typing belongs to the physical module, not to the diagnostic. A diagnostic label such as "unsustainable portion" **never** determines physical destination. Material routing is determined by the typed physical module alone, and the diagnostic threshold that flags a flow has no standing in the incidence matrix.

**The split-assignment evidence requirement.** Where an application splits extraction between standing-stock removal and recruitment suppression — $C_{\mathrm{stock}}=\psi qEN$ and $C_{\mathrm{recruit}}=(1-\psi)qEN$ for $\psi\in[0,1]$ — the assignment requires evidence per channel. The dominant physical mechanism sets it, never a diagnostic label.

The illustrative assignments below run through a logistic two-channel proxy. They are stated as **illustrative, calibrated examples — not constitutive claims for the named domains**.

| System | Existing-unit removal | Replenishment degradation | Spread |
|---|---|---|---|
| Soil zinc under crop export | $\psi=0.85$ | $\psi=0.25$ (impaired mineralisation) | trough depth varies by a factor of about 1.5 from mechanism alone |
| Pollinators | $\psi=0.70$ (adult mortality) | $\psi=0.20$ (brood failure) | as above |

**The mass-routing discipline** is the same typing made explicit.

1. Literally harvesting pre-recruit stages *is* a harvest of existing units, and routes to the product and waste fractions.
2. Habitat-induced failed recruitment is a **prevented inflow**. Routing it into product or waste would create mass that was never in the stock.
3. Damage to the capital stock itself — aquifer compaction, severe soil loss — is not a split-assignment channel at all. It is a slow drift in capacity, or a transfer to the inert sink.

## 2.6 Support saturation and the logistic limit

Two results control what the ledger's stock equation becomes when its support pool saturates. Both are singular reductions with explicit scope, and neither is a full-system reduction.

**Theorem 1 (Support-saturated logistic stock limit).** *Fix $T<\infty$ and non-negative parameters $\mu,\delta,c,q$. Assume (H1) $A_\kappa$ is measurable with $A_\kappa(t)\ge a_0>0$ and $0\le X_\kappa(t)\le X_{\max}$; (H2) common effort $E\in L^\infty([0,T])$. Let $X_\kappa$ solve*

$$\dot X_\kappa=\mu X_\kappa\frac{A_\kappa}{\kappa+A_\kappa}-\delta X_\kappa-cX_\kappa^2-qE(t)X_\kappa,$$

*and let $X_0$ solve the limiting equation with the same initial value. Then $\sup_{t\le T}|X_\kappa(t)-X_0(t)|=O(\kappa)$. If $\mu>\delta$ and $c>0$ the limit is $\dot X_0=rX_0(1-X_0/K_{\log})-qE(t)X_0$ with $r=\mu-\delta$ and $K_{\log}=(\mu-\delta)/c$.*

*Proof.* Write $e(t)=|X_\kappa(t)-X_0(t)|$. The saturation defect satisfies $\big|\tfrac{A_\kappa}{\kappa+A_\kappa}-1\big|=\tfrac{\kappa}{\kappa+A_\kappa}\le\tfrac{\kappa}{a_0}$, so the vector-field defect obeys $|\dot X_\kappa-\dot X_0|\le L_1\kappa+L_2 e(t)$ with $L_1=\mu X_{\max}/a_0$ and $L_2=\mu+\delta+2cX_{\max}+q\|E\|_\infty$, using $|\mu-\delta|\le\mu+\delta$ and $c(X_\kappa+X_0)\le 2cX_{\max}$. Gronwall's inequality with Lipschitz constant $L_2$ and particular-term scale $L_1$ gives $e(t)\le(L_1/L_2)\kappa\,(e^{L_2t}-1)\le C_T\kappa$ on $[0,T]$. The bound $0\le X_\kappa\le X_{\max}$ is satisfiable in the registered family: under $\mu>\delta$ the comparison $\dot X_\kappa\le X_\kappa(\mu-\delta-cX_\kappa)$ keeps $X_\kappa\le\max\{X(0),(\mu-\delta)/c\}$, so $X_{\max}=\max\{X(0),K_{\log}\}$ suffices. The limiting equation is $\dot X_0=\mu X_0-\delta X_0-cX_0^2-qEX_0$, i.e. $\dot X_0=(\mu-\delta)X_0(1-X_0/K_{\log})-qEX_0$ with $K_{\log}=(\mu-\delta)/c$. $\blacksquare$

**Remark 2 (Registered-family support-saturated identity).** *In the primitive-flux core with $g(X,A)=\mu XA/(K_A+A)$, $m(X)=dX+cX^2$, $h(X,E)=qEX$, the support-saturated stock equation is, for each fixed interior $A>0$ in the limit $K_A\to0$,*

$$\dot X=(\mu-d)X-cX^2-qEX=rX\Big(1-\frac XK\Big)-qEX,\qquad r=\mu-d,\quad K=\frac{\mu-d}{c},$$

*requiring $\mu>d$ and $c>0$. The identity is pointwise on the interior support region and not uniform through the depleted-pool boundary: for every $K_A>0$, $A/(K_A+A)=0$ at $A=0$.*

*Proof.* At fixed $A>0$, $A/(K_A+A)\to1$ as $K_A\to0$, so $g\to\mu X$ pointwise and $g-m\to(\mu-d)X-cX^2$; the algebraic reduction to logistic form with $r=\mu-d$, $K=(\mu-d)/c$ is immediate. The non-uniformity statement is the identity $A/(K_A+A)=0$ at $A=0$ for every $K_A>0$, which the pointwise limit does not touch.

The scope is restricted. The limit does not eliminate the detritus compartment $U$, does not make $A$ constant near its boundary, and does not transform the memory or effort laws. It is an ecological stock-equation identity — **not a full-system reduction and not a transfer principle for bifurcation thresholds**. In the correspondence, the logistic law of (2) is this saturated, mortality-folded readout of the Theorem 1 and Remark 2 family — not the vector field of the closed four-tuple of §2.2 — and bifurcation numbers of the two families do not transfer between them. $\blacksquare$

**What this means for material-flow accounting.** A logistic stock equation is a saturated support-pool readout, not a primitive physical law. Substituting it for the underlying stock-support dynamics is legitimate only where the support pool is at interior saturation, and only on the timescales over which the saturated approximation holds.
# 3. The certification layers — three things that look alike and are proved separately

> **In plain words.** Three claims about a ledger are routinely treated as one. "The accounts add up." "The materials are conserved." "Nothing crosses a safety limit." They are three different claims, and the second does not imply the third. This section keeps them apart and proves exactly which way the arrows go. One practical consequence: an assessment that reports only one of them declares less than it appears to.

## 3.1 Three predicates, separated

The four predicates of §1.1 — bookkeeping balance, stoichiometric conservation, thermodynamic admissibility, sustainability safety — are this section's working layer. It separates the first, second and fourth and proves their relationships. The third, thermodynamic admissibility, is out of scope here, per Proposition 2's layering. This is the point at which the Daly/Ayres tradition of throughput accounting meets the formalism of reaction-network theory (Feinberg, 2019; Brunner and Rechberger, 2004).

The ledger supports three distinct predicates that are related but not identical.

```
Layer 1  Accounting consistency    the balance law (1) holds almost everywhere on [0,T]
Layer 2  Conservation consistency   ℓᵀSᵀ = 0 for every declared conserved quantity ℓ
Layer 3  Barrier safety             for declared lower and upper barriers,
                                    B_m(t) ≤ S_m(t) ≤ B̄_m(t) for every component m
                                    and every t ∈ [0,T], where S = Cx is the
                                    moiety-composition readout
```

Layer 2 is a structural predicate on the incidence operator alone. Layers 1 and 3 are properties of a trajectory triple $(x,v,b)$. The logical relations between them are the content of the next two propositions.

> **Numbering note.** The two layering propositions in this section carry their own counter — Propositions 1–2. Every other numbered statement in the article runs on a single 1–20 sequence counter. So "Proposition 4", "Proposition 6", "Proposition 17", "Proposition 18" and "Proposition 20" are main-counter statements, not further members of the layering counter. Every label is unique and resolves directly. The supplementary's statement inventory and this status-word offset are reconciled in its §6.

**Proposition 1 (Layer 2 ⇒ Layer 1, for the conserved quantities).** *If $\ell^{\top}S^{\top}=0$, then $\tfrac{d}{dt}(\ell^{\top}x)=\ell^{\top}b$, and in a closed system ($b=0$) $\ell^{\top}x$ is invariant.*

*Proof.* $\tfrac{d}{dt}(\ell^{\top}x)=\ell^{\top}\dot x=\ell^{\top}(S^{\top}v+b)=(\ell^{\top}S^{\top})v+\ell^{\top}b=\ell^{\top}b$. $\blacksquare$

In words: if a quantity is invisible to the wiring, it can only change through the boundary. Close the boundary and it cannot change at all.

**Proposition 2 (The layers do not collapse).** *Barrier safety does not follow from accounting consistency: a trajectory can be perfectly mass-balanced while violating a declared barrier; and a trajectory can satisfy declared barriers while violating a conservation law or a stoichiometric constraint. Conversely, thermodynamic admissibility (energy conservation, entropy-production non-negativity, reaction feasibility) implies accounting consistency, but the converse does not hold; this article establishes Layers 1–3 only.*

*Proof.* First clause: on the closed ledger (2), constant extraction at a rate exceeding regeneration — a comparison flux, not a donor-limited primitive of the ledger's own discipline — is exactly mass-balanced (Theorem 7 states the identity) and drives the living stock through any positive lower barrier in finite time. Likewise the trajectory with $N\equiv0$ (the extinction rest of §4.6) is mass-balanced yet violates any positive lower barrier on $N$. Conversely, a trajectory satisfying the barriers may be generated by fluxes that fail a stoichiometric constraint — mass balance does not certify that the flux decomposition is physically realizable — or by bookkeeping that silently drops a moiety through the yield-routing violation of rule (iii) in §10.2, failing conservation without touching the barriers. Second clause: thermodynamic admissibility presupposes a mass balance, but a mass-balanced flux decomposition need not satisfy energy or entropy constraints; establishing those requires structure outside the present scope. $\blacksquare$

**The implication for industrial-ecology measurement.** Mass-balance closure, stoichiometric consistency and barrier compliance must each be audited separately. A single integrated assessment that reports only one of them declares less than it appears to.

## 3.2 The typed safety set

The typed safety set at time $t$ is

$$\mathcal K(t)=\{x\ge 0: \underline B(t)\le Cx\le \overline B(t)\},$$

and the non-compensatory assessment reads $\mathcal V_{\mathrm{typed}}=\{x(\cdot): x(t)\in\mathcal K(t)\ \forall t\in[0,T]\}$. This is a **conjunctive** criterion: all moiety barriers must be satisfied simultaneously, and no weighted aggregate $\sum_m w_m S_m$ is used as the decision criterion. The force of that conjunction is the subject of §10.1.

In plain words: the test is "every box clears its own limit", not "the average looks fine". An average can always be rescued by a component with room to spare. A conjunction cannot.

## 3.3 The flux-reconstruction identity

**Lemma 3 (Flux reconstruction under a typed balance law).** *Let $x:[0,T]\to\mathbb R^n_+$ be absolutely continuous with $\dot x(t)=S^{\top}v(t)+b(t)$ almost everywhere, $v\in L^1([0,T];\mathbb R^J_+)$, $b\in L^1([0,T];\mathbb R^n)$, and $S=Cx$ with $C\in\mathbb R^{M\times n}$ the moiety-composition matrix. Then*

$$S(t)=S(0)+\int_0^t\big(CS^{\top}v(\tau)+Cb(\tau)\big)\,d\tau,$$

*and for continuous barriers $\underline B,\overline B$ the trajectory satisfies $\underline B_m(t)\le S_m(t)\le\overline B_m(t)$ for all $t\in[0,T]$ if and only if the corresponding integrated inequalities hold for all $t\in[0,T]$.*

*Proof.* Integrate $\dot S=C\dot x=C(S^{\top}v+b)=CS^{\top}v+Cb$ from $0$ to $t$; this is valid because $x$ is absolutely continuous and $C$ is linear. The barrier equivalence follows because $S_m$ is continuous (as $x$ is absolutely continuous) and the barriers are continuous, so a pointwise inequality violation is an integrated-inequality violation at the same time. $\blacksquare$

**What the lemma buys, in words.** The readout at any date equals the readout you started with plus the recorded flows in between. Two cases are distinguished.

- **Prescribed or observed fluxes.** If $v(t)$ and $b(t)$ are known and integrable, stock balances are reconstructed by integration without solving the internal constitutive dynamics. This is the computationally simple auditing case.
- **Endogenous fluxes.** If $v(t)=v(x(t),u(t),d(t))$, flux-only auditing is not generally possible without solving, estimating or bounding the coupled system. The identity still holds, but the integral cannot be evaluated without determining $v(t)$.

In both cases the barriers are **declared, not computed**: the flux data do not compute ecological threshold values, aquifer collapse thresholds, or concentration boundaries. The theorem establishes trajectory *compliance with declared barriers*, not derivation of the barriers themselves.

With $h_m(t)\ge0$ the net outflow of moiety $m$ across the system boundary and $r_m(t)\ge0$ the net inflow, the sign convention reads

$$S_m(t)=S_m(0)+\int_0^t\big(r_m(\tau)-h_m(\tau)\big)\,d\tau,\qquad\text{and barrier safety is}\qquad S_m(0)+\int_0^t\big(r_m(\tau)-h_m(\tau)\big)\,d\tau\ \ge\ \underline B_m(t).$$

> **[Editor's note — flagged for the author, not their claim.]** The lemma's name and the abstract both describe recovering *fluxes* from *stocks*; the statement and proof above integrate observed fluxes to reconstruct the readout. This rendering keeps the author's title and adds no claim. The fix belongs in the abstract or the lemma's name. See `review/joint_evaluation_v1.md` §2.3/D11.

## 3.4 The conservation-law reduction

**Proposition 4 (Conservation-law reduction).** *If $\ell^{\top}S^{\top}=0$ for some vector $\ell\in\mathbb R^n$, then $\ell^{\top}x(t)=\ell^{\top}x(0)+\int_0^t\ell^{\top}b(\tau)d\tau$; in a closed system ($b=0$), $\ell^{\top}x$ is invariant.*

*Proof.* This is Proposition 1 integrated: $\tfrac{d}{dt}(\ell^{\top}x)=\ell^{\top}b$; integrate. $\blacksquare$

A conserved moiety is a row $c_m^{\top}$ of $C$ with $c_m^{\top}S^{\top}=0$; then $S_m=c_m^{\top}x$ satisfies $\dot S_m=c_m^{\top}b$. In a closed system $S_m$ is constant, and in an open system $S_m$ changes only through boundary flows.

**Conservation does not imply barrier safety.** If a closed conserved moiety has fixed total stock $S_m(t)=S_m(0)$, a time-varying barrier can become infeasible solely because the barrier moves. The three objects are distinct: the conservation invariant ($S_m$ constant), the barrier tube ($\underline B_m\le S_m\le\overline B_m$), and the intersection of the invariant manifold with the barrier tube. A conservation law alone does not imply that the trajectory satisfies the barrier. The precise sense is linear: the set $\{x\ge0:\ell^{\top}x=\ell^{\top}x(0),\ \underline B\le Cx\le\overline B\}$ **may be empty even though each of the three objects is separately well-defined**. Barrier–conservation compatibility is a linear feasibility programme, not a slogan.

## 3.5 The flux-bounding envelope theorem

**Theorem 5 (Flux-bounding envelopes).** *Assume:*

**(H1)** *the primitive fluxes and boundary transfers satisfy componentwise bounds $v(t)\in[\underline v(t),\overline v(t)]$ and $b(t)\in[\underline b(t),\overline b(t)]$ for all $t\in[0,T]$.*

*For any matrix $A$ write $A^+=\max\{A,0\}$ and $A^-=\max\{-A,0\}$ entrywise, and define for each moiety $m$ the envelope integrands*

$$\varphi_m(\tau)=(CS^{\top})_m^+\underline v(\tau)-(CS^{\top})_m^-\overline v(\tau)+C_m^+\underline b(\tau)-C_m^-\overline b(\tau),$$
$$\psi_m(\tau)=(CS^{\top})_m^+\overline v(\tau)-(CS^{\top})_m^-\underline v(\tau)+C_m^+\overline b(\tau)-C_m^-\underline b(\tau),$$

*and the envelopes $\underline S_m(t)=S_m(0)+\int_0^t\varphi_m(\tau)d\tau$, $\overline S_m(t)=S_m(0)+\int_0^t\psi_m(\tau)d\tau$. Then $S_m(t)\in[\underline S_m(t),\overline S_m(t)]$ for all $t\in[0,T]$ and all $m$.*

*(The lower/upper bars on $v$, $b$, $\varphi$, $\psi$ and $S$ are lost in the PDF text layer; the arrangement above is the one the sandwich relation requires, and it is stated here so the theorem can be checked.)*

*Proof.* By Lemma 3, $\dot S_m=(CS^{\top}v+Cb)_m$. For each row $m$ and time $\tau$, the bilinear form $(CS^{\top})_m v$ is linear in $v$ with coefficient vector $(CS^{\top})_m$, whose positive and negative parts give, over the box $[\underline v(\tau),\overline v(\tau)]$, the pointwise bounds $\varphi_m(\tau)\le(CS^{\top})_m v(\tau)\le\psi_m(\tau)$, attained at the extreme points of the box. The same argument applies to $C_m b(\tau)$, and adding gives $\varphi_m(\tau)\le\dot S_m(\tau)\le\psi_m(\tau)$. Integrating over $[0,t]$ yields the stated envelope. $\blacksquare$

**Corollary (Flux-derived barrier certificate).** *If $\underline S_m(t)\ge\underline B_m(t)$ and $\overline S_m(t)\le\overline B_m(t)$ for all $t\in[0,T]$ and all $m$, then every trajectory compatible with the flux bounds is barrier-safe on $[0,T]$.*

*Proof.* By Theorem 5 every such trajectory satisfies $\underline S_m(t)\le S_m(t)\le\overline S_m(t)$; the certificate conditions sandwich $S_m$ between the barriers. $\blacksquare$

**Two qualifications are part of the theorem.**

1. **The bounds are conservative.** They hold for *all* flux selections in the declared boxes, including selections that are not jointly realizable by the coupled dynamics. So the certificate may fail when a trajectory with jointly realizable fluxes would pass. Attainability requires solving or bounding the coupled system.
2. **State-dependence needs one more condition.** When $v=v(x)$, the declared box must additionally be forward-invariant under the coupled dynamics for the envelopes to bound the system's reachable set. Without that condition the corollary is a certificate for flux-admissible paths only, not for the ODE's trajectories.

And the envelope is an interval computation on the flux data, **not a forecast**. It says nothing about what the fluxes *will* be, only about what every admissible flux path implies for the stock. Stoichiometric and donor-limit constraints make the jointly admissible flux selections a *polytope* rather than a box; the tight certificate is the linear programme over that polytope, and the box envelope above is its auditing relaxation — the box is what is audited, the polytope what is realizable. The envelope is the interval-arithmetic counterpart, at the level of declared flux bounds, of the data-reconciliation practice of material flow analysis (Brunner and Rechberger, 2004).

**Worked envelope on the closed block.** On (2), with declared boxes $N\in[0,K]$ and $E\in[0,E_{\max}]$, the mass row of the incidence gives

$$\dot M=-qEN-C_{A,\mathrm{lim}}\in[-(qE_{\max}K+C_A),\,0],\qquad\text{hence}\qquad M(t)\in\big[M(0)-(qE_{\max}K+C_A)t,\;M(0)\big].$$

The conservatism is visible in the extremes: maximal extraction $qE_{\max}K$ is realizable only at $N=K$, where regeneration vanishes, and maximal recharge coincides with minimal extraction — box extremes the coupled dynamics cannot realize jointly.

## 3.6 Finite exhaustion under uniform drift, and its failure mode

**Proposition 6 (Finite exhaustion under uniform negative drift).** *Assume (H1) $S$ is absolutely continuous with $\dot S(t)\le-\varepsilon<0$ whenever $S(t)>\underline B$, where $\underline B$ is a constant lower barrier and $\varepsilon>0$ a uniform drift bound; (H2) $S(0)>\underline B$. Then the first hitting time satisfies $\tau_{\underline B}=\inf\{t\ge0:S(t)\le\underline B\}\le\dfrac{S(0)-\underline B}{\varepsilon}$.*

*Proof.* While $S(t)>\underline B$ the drift bound integrates to $S(t)\le S(0)-\varepsilon t$; the right-hand side reaches $\underline B$ at $t=(S(0)-\underline B)/\varepsilon$, so by continuity of $S$ the crossing occurs no later. $\blacksquare$

In words: if you can promise the stock falls by at least $\varepsilon$ per year until it hits the line, then the distance to the line divided by $\varepsilon$ is a hard deadline. The uniform-margin assumption is doing all the work, and its absence is the classical failure mode.

**Counterexample (proportional extraction).** For donor-controlled proportional extraction $\dot S=-kS$ with $k>0$ and $S(0)>0$, the stock satisfies $S(t)=S(0)e^{-kt}>0$ for every finite $t$: it approaches zero asymptotically and is never exhausted in finite time, $\tau_0=\infty$. The time to a positive barrier $B>0$ is $\tau_B=k^{-1}\log(S(0)/B)$, finite for $B>0$ but diverging as $B\to0$.

In particular, the claim that **positive extraction implies finite exhaustion is false**, and every exhaustion statement must name its referent. Internal transfers do not exhaust a total moiety: in a closed system, internal conversion redistributes a conserved moiety but does not exhaust it. Exhaustion of a compartment requires one of: a boundary outflow; an irreversible conversion into an uncounted or unavailable form; destruction of the relevant function; or a barrier defined on a particular compartment rather than on the total moiety. Whether "exhaustion" refers to the total conserved moiety, a compartment stock, an accessible or functional stock, a stock above a lower barrier, or an economically recoverable reserve — these are different quantities, and the theorem must specify which (§6.4).

The counterexample and this taxonomy are the content of the following named statement, which the rest of the article uses as its boundary discipline.

**Proposition (Depletion is compartmental).** *On a closed typed ledger, the total mass $\mathbb 1^{\top}x$ of each conserved moiety is invariant along trajectories. Consequently every finite hitting time of a zero readout is the hitting time of a **compartment** or of a **barrier on a readout**, never of total mass, and "exhaustion of the natural block" (Theorems 7 and 14) is transfer across the block boundary into the product, waste and inert compartments.*

The boundary discipline this proposition fixes is the ecological-economics one of Daly (1990): depletion is not loss of matter. It is loss of access to matter in the form and place that supports the service in question. The remainder of the article keeps that distinction in force.
# 4. Conservation and positivity of the closed ledger — what the wiring guarantees

> **In plain words.** Here the article stops building and starts proving, for the closed system of §2.2. Eight things are shown. Nothing disappears from the natural block except through the named exits. Nothing ever goes negative. The system cannot sit still while people keep extracting at effort. When extraction stops, there are exactly three kinds of place it can settle. The total amount ever extracted is capped by the budget you started with. A hybrid (jump) version of the balance holds on stated conditions. Summing equations is not a proof of anything. And all of that together forms a complete portrait of the closed ledger, which §9 then uses as the boundary against an open system.

## 4.1 The natural-block mass identity

**Theorem 7 (Natural-block mass identity).** *Let $M=N+A_{\mathrm{act}}+A_{\mathrm{geo}}+U$. Along every trajectory of the closed natural block (2) with optional mining restored,*

$$\dot M=-qEN-C_{A,\mathrm{lim}},$$

*i.e. mass leaves the natural block exactly at the extraction rate, plus the donor-limited mining rate. Under the institutional-failure specialization ($C_A=0$), $\dot M=-qEN$. The identity is stated for the declared harvest routing $\alpha=0$ of §2.2; with a detritus-routed harvest fraction $\alpha>0$ the block export is $(1-\alpha)qEN$ and the identity reads $\dot M=-(1-\alpha)qEN-C_{A,\mathrm{lim}}$.*

*Proof.* Sum the four equations of (2), with the mining term subtracted from $\dot A_{\mathrm{geo}}$:

$$\dot M=(R-qEN)+(-B+e_{GA}-e_{AG}+\gamma_UU)+(-e_{GA}+e_{AG}-C_{A,\mathrm{lim}})+(T-\gamma_UU)=R-B+T-qEN-C_{A,\mathrm{lim}},$$

and $R-B+T=R-(R+T)+T=0$. The mined fraction routes out of the four-coordinate natural block; the full-ledger theorems of §4.2–4.3 record the mining column as an internal transfer between compartments outside the block — consistent because the **block** boundary, not the **ledger** boundary, is crossed. $\blacksquare$

## 4.2 Stoichiometric conservation of the full ledger

**Theorem 8 (Stoichiometric conservation).** *Let $X=(N,P,W,I,U,A_{\mathrm{act}},A_{\mathrm{geo}})$ be the mass compartments of one resource system and $S^{\top}$ the incidence matrix of its flux ledger. One-way transfers are non-negative and donor-limited; net regeneration is the difference of two such primitives and is signed when $N>K$. Under the unit-sum routing constraints with $0\le\alpha\le1$,*

$$\dot X=S^{\top}F(X),\qquad \frac{d}{dt}\mathbb 1^{\top}X=0.$$

*Proof.* Every primitive is a transfer between two compartments, or a pair of opposite primitives implementing a two-way exchange; the corresponding column of $S^{\top}$ has entries $+1$ and $-1$ in the receiving and donating rows and zeros elsewhere. Routing tensors are column-stochastic in the destination-indexed convention by construction: each unit of a split flux sums to one across destinations. Hence $\mathbb 1^{\top}S^{\top}=0$ and $\mathbb 1^{\top}\dot X=\mathbb 1^{\top}S^{\top}F=0$. The theorem is an exact conservation identity **under the routing constraints**. $\blacksquare$

The seven-compartment incidence claimed by Theorem 8 is displayed here — in the compartment order of its statement, with the closed block's primitive fluxes, the pattern of the six-compartment $S(\alpha,\rho_P)$ of Theorem 9 with the inert column (no outflow from the inert compartment) appended, and the harvest column split by $(\alpha,1-\alpha)$. Rows $(N,P,W,I,U,A_{\mathrm{act}},A_{\mathrm{geo}})$; columns gross regeneration, density-dependent return, harvest, uptake, detritus return, $e_{GA}$, $e_{AG}$, mining (to product), product retirement, inert-bound transfer (waste → inert):

$$S^{\top}=\begin{pmatrix} 1&-1&-1&0&0&0&0&0&0&0\\ 0&0&1-\alpha&0&0&0&0&1&-1&0\\ 0&0&0&0&0&0&0&0&1-\rho_P&-1\\ 0&0&0&0&0&0&0&0&0&1\\ 0&0&\alpha&1&-1&0&0&0&\rho_P&0\\ -1&1&0&-1&1&1&-1&0&0&0\\ 0&0&0&0&0&-1&1&-1&0&0 \end{pmatrix}$$

Every column is a two-compartment transfer under the unit-sum routing constraints, so $\mathbb 1^{\top}S^{\top}=0$ column by column — Theorem 8's conservation, at sight. The natural-block rows $(N,U,A_{\mathrm{act}},A_{\mathrm{geo}})$ reproduce the four-row display of §2.2, with the harvest column now carrying its full routing ($\alpha$ to $U$, $1-\alpha$ to $P$) instead of the block-export convention of the $\alpha=0$ corner. The waste-routed mining variant appends a column with $-1$ in the $A_{\mathrm{geo}}$ row and $+1$ in the $W$ row under the same pattern. The retirement split $(\rho_P,1-\rho_P)$ and the inert-bound source (the absorbing stock $W$) are **declared routing choices of this displayed instance**; the incidence pattern — every primitive a two-compartment transfer, column sums zero — is the theorem's content, and no classification depends on the declared choices.

## 4.3 Conservation of the six-compartment ledger

**Theorem 9 (Six-compartment conservation).** *For the system of §2.3, $\tfrac{d}{dt}\mathbb 1^{\top}z=0$; the total mass $M_6=X+U+A+G+P+W$ is constant along every trajectory on which the classical solution is defined.*

*Proof.* With $M_6=\mathbb 1^{\top}z$, $\dot M_6=\mathbb 1^{\top}S(\alpha,\rho)v=0$ because each column of $S$ sums to zero. Term by term: assimilation gives $g-g=0$; mortality gives $-m+m=0$; decomposition gives $-d_U+d_U=0$; geological exchange gives $e_{GA}-e_{GA}=0$ and $-e_{AG}+e_{AG}=0$; mining gives $-c_G+c_G=0$; and the remaining harvest and retirement terms satisfy $-h+\alpha h+(1-\alpha)h=0$ and $\rho_Pr_P-r_P+(1-\rho_P)r_P=0$. $\blacksquare$

**Two scope notes are part of the theorem.** The conservation argument applies to the *expanded typed incidence system* when quality grades are split — not automatically to an undifferentiated quality-neutral loop. And open systems are explicit: imports, exports, atmospheric losses and cross-boundary transport enter as typed boundary fluxes, giving $\dot M_6=I_\partial-O_\partial$. Writing these flows explicitly is preferable to preserving a nominal invariant by allowing an unobserved or finite donor compartment to become negative.

Theorems 7–9 are three instances of the conservation lemma of Proposition 1. Each is the identity $\tfrac{d}{dt}(\ell^{\top}x)=\ell^{\top}b$ for a declared ledger and boundary with $\ell=\mathbb 1$, differentiated only by which compartments the declaration includes.

## 4.4 Orthant invariance

**Theorem 10 (Orthant invariance of the closed ledger).** *The non-negative orthant in $(N,A_{\mathrm{act}},A_{\mathrm{geo}},U)$ is forward invariant for the closed natural block (2).*

*Proof.* The right-hand side is locally Lipschitz on a neighbourhood of the closed orthant: each Michaelis–Menten factor, and $\sigma$, is $C^\infty$ on the non-negative half-line because the registered regime keeps $A_0>0$ and $A_{g0}>0$. Face by face. On $A_{\mathrm{geo}}=0$ one has $\sigma=0$, hence $e_{GA}=0$ and $\dot A_{\mathrm{geo}}=e_{AG}=\omega_AA_{\mathrm{act}}\ge0$. On $A_{\mathrm{act}}=0$ one has $s=0$, so $R=B=T=e_{AG}=0$ and $\dot A_{\mathrm{act}}=e_{GA}+\gamma_UU\ge0$. On $N=0$, extraction and uptake vanish and $\dot N=0$. On $U=0$, $\dot U=T\ge0$. Nagumo's inward-pointing criterion (Aubin, 1991) yields forward invariance of the orthant. $\blacksquare$

**Theorem 11 (Forward invariance of the six-compartment cone).** *Under the donor boundary assumptions of §2.3 — each primitive flux vanishes when its donor is empty, fluxes continuous in effort and locally Lipschitz in the state — $\mathbb R^6_+$ is forward invariant for the six-compartment system.*

*Proof.* Face by face: at $X=0$, $g=m=h=0$ so $\dot X=0$; at $U=0$, $\dot U=m+\alpha h+\rho_Pr_P\ge0$; at $A=0$, $\dot A=-g+d_U+e_{GA}-e_{AG}=d_U+e_{GA}\ge0$, the two negative terms vanishing by donor limitation ($A$ is the donor of both $g$ and $e_{AG}$); at $G=0$, $\dot G=e_{AG}\ge0$; at $P=0$, $\dot P=(1-\alpha)h+c_G\ge0$; at $W=0$, $\dot W=(1-\rho_P)r_P\ge0$. The vector field belongs to the tangent cone at every boundary point, and the tangent-cone invariance theorem applies.

Conservation and boundary admissibility are separate obligations, and the finite-donor condition carries a discipline: a target-relaxation law $e_{GA}=\omega(A_{\mathrm{eq}}-A)$ **does not satisfy it** unless also limited by $G$. It may be used only with the source declared an effectively infinite external reservoir, in which case the system is open rather than closed. $\blacksquare$

The classical lineage of these statements is the compartmental-systems non-negativity theory (Jacquez and Simon, 1993). The donor-limitation condition is the exact sufficiency requirement — **algebraic cancellation alone does not establish invariance**.

## 4.5 No interior rest at positive effort

**Theorem 12 (No interior rest at positive effort).** *Assume (H1) $E\equiv E^*>0$ is constant. Then a rest point of the closed natural block satisfies $R+C_{A,\mathrm{lim}}=0$ after restoring optional mining; with $C_A=0$ this is $R=0$, hence $N=0$ or $N=K$ or $A_{\mathrm{act}}=0$. None of these is compatible with $E^*>0$ and $N^*>0$: (i) $N=K$ and $E^*>0$ give $\dot N=-qE^*K<0$; (ii) $A_{\mathrm{act}}=0$ and $A_{\mathrm{geo}}>0$ give $\dot A_{\mathrm{act}}=\omega_AA_{\mathrm{eq,intrinsic}}\sigma>0$; (iii) $N=0$ forces $R=T=0$ and reduces to the extinction family $\mathsf R_{\mathrm{ext}}$ of Theorem 13. In particular the working point $(N^*,A_{\mathrm{act}}{}^*)=(89.526,\,397.87)$ **is not** a rest point at $E=E^*\approx2.090$: $\dot N=0$ holds there by construction ($R^*=qE^*N^*\approx0.187>0$), and the rest condition of the proof fails on the abiotic pair.*

*Proof.* At a rest point, $\dot U=0$ forces $\gamma_UU=T$. Adding $\dot A_{\mathrm{act}}+\dot A_{\mathrm{geo}}$ gives $-B+\gamma_UU-C_{A,\mathrm{lim}}=0$; with $\gamma_UU=T$ and $B=R+T$ this is $R+C_{A,\mathrm{lim}}=0$. With mining declared ($C_A>0$) this forces $R\le0$; with $C_A=0$ it is $R=0$, and from the constitutive law $R=rN(1-N/K)s=0$ implies $N=0$ or $N=K$ or $s=0$ (that is, $A_{\mathrm{act}}=0$). Cases (i)–(iii) exclude each branch at positive effort. In the mining case the contradiction is more direct: $\dot N=0$ with $E^*>0$ and $N^*>0$ gives $R=qE^*N^*>0$, while the abiotic rest condition gives $R=-C_{A,\mathrm{lim}}\le0$. At the working point $\dot N=0$ by construction while rest would require $R=0$; with $\dot U=0$ the abiotic pair would satisfy $\dot A_{\mathrm{act}}+\dot A_{\mathrm{geo}}=-R<0$. $\blacksquare$

In words: you cannot have a steady state with living stock in it while effort stays positive. The bookkeeping forces one pool or another to keep moving.

## 4.6 The extinction–geochemical rest set

**Theorem 13 (Vanishing-extraction rest set).** *With vanishing extraction ($E\equiv0$), the rest points of the closed natural block (2) are **exactly** the three sets — the extinction family $\mathsf R_{\mathrm{ext}}$, the carrying-capacity family $\mathsf R_K$, and the frozen-biomass face $\mathsf R_{\mathrm{frozen}}$; the union symbol $\mathsf R_0=\mathsf R_{\mathrm{ext}}\cup\mathsf R_K$ is retained for the two geochemical families:*

$$\mathsf R_{\mathrm{ext}}=\{N=0,\;U=0,\;A_{\mathrm{act}}=A_{\mathrm{eq,intrinsic}}\sigma(A_{\mathrm{geo}}),\;A_{\mathrm{geo}}\ge0\},$$
$$\mathsf R_K=\{N=K,\;U=\kappa_AKs/\gamma_U,\;A_{\mathrm{act}}=A_{\mathrm{eq,intrinsic}}\sigma,\;A_{\mathrm{geo}}\ge0\},$$

*where in the second family $s=A_{\mathrm{act}}/(A_{\mathrm{act}}+A_0)$ is evaluated at the solution — together with the frozen-biomass face $\mathsf R_{\mathrm{frozen}}=\{(N,0,0,0):N\ge0\}$, on which $s=0$ identically and the biomass is frozen at its initial value. With $E>0$ constant, no interior rest point (with $N^*>0$) exists (Theorem 12); the extinction face $\mathsf R_{\mathrm{ext}}$ of this set persists at positive effort, because extraction $qEN$ vanishes identically at $N=0$, and it is a boundary rest rather than an interior one. If $A_{g0}=0$ and $\sigma\equiv1$ is imposed for $A_{\mathrm{geo}}>0$, the shared active-pool ray of $\mathsf R_{\mathrm{ext}}$ and $\mathsf R_K$ is $A_{\mathrm{act}}=A_{\mathrm{eq,intrinsic}}$, $A_{\mathrm{geo}}>0$ — the endpoint $A_{\mathrm{geo}}=0$ is excluded, because there the donor-limited recharge vanishes and $\dot A_{\mathrm{act}}=-\omega_AA_{\mathrm{eq,intrinsic}}<0$. The constitutive laws carry no basal mortality independent of the support factor; adding one ($\mu_{\mathrm{basal}}N$, stock → detritus) collapses the frozen-biomass face and does not touch Theorems 7–12 or 14.*

*Proof.* With $E\equiv0$, set the four derivatives to zero. From $\dot A_{\mathrm{geo}}=-e_{GA}+e_{AG}=0$: $\omega_AA_{\mathrm{eq,intrinsic}}\sigma=\omega_AA_{\mathrm{act}}$, so $A_{\mathrm{act}}=A_{\mathrm{eq,intrinsic}}\sigma$ — the geological-exchange balance, in which the active pool is pinned to the donor-scaled intrinsic target. From $\dot N=R=0$: $rN(1-N/K)s=0$. If $A_{\mathrm{geo}}>0$ the geo-balance pins $A_{\mathrm{act}}>0$, so $s>0$ and $N=0$ or $N=K$. At the boundary $A_{\mathrm{geo}}=0$ the geo-balance forces $A_{\mathrm{act}}=0$ (since $\sigma(0)=0$), hence $s=0$ and $\dot N=0$ for every $N\ge0$; with $U=0$ the remaining equations vanish identically, so the frozen-biomass face is a rest set. From $\dot U=T-\gamma_UU=0$: $U=T/\gamma_U=\kappa_ANs/\gamma_U$, which vanishes in the $N=0$ branch and is positive in the $N=K$ branch. From $\dot A_{\mathrm{act}}=-(R+T)+0+\gamma_UU$: this vanishes in both branches, since $\gamma_UU=T$ and $R=0$ hold there. The two families together with the frozen-biomass face are exactly the stated rest set. "Geochemical" names the mechanism of both families' active-pool rest: the pool rests at the donor-scaled intrinsic target. Apart from the frozen-biomass face, no rest point exists away from extinction or carrying capacity. The institutional memory yields $E\to E^*$ at $N=0$ with extraction vanishing identically — consistent with the rest set, and not an interior rest. $\blacksquare$

## 4.7 Extraction integrability

**Theorem 14 (Integrable extraction).** *Assume $E(s)\ge0$ along the trajectory (effort is non-negative; $N\ge0$ along classical solutions is Theorem 10's). Let $M=N+A_{\mathrm{act}}+A_{\mathrm{geo}}+U$. Then*

$$M(t)=M(0)-\int_0^t qE(s)N(s)\,ds\ \ge\ 0,\qquad\text{so}\qquad \int_0^\infty qE(s)N(s)\,ds\ \le\ M(0)<\infty,$$

*in particular $qEN\in L^1(0,\infty)$, and **no trajectory maintains extraction at the working value $qE^*N^*\approx0.187$ for all time**; with mining restored, $\int_0^\infty(qE(s)N(s)+C_{A,\mathrm{lim}}(s))\,ds\le M(0)$.*

*Proof.* By Theorem 7, $M(t)=M(0)-\int_0^tqE(s)N(s)ds$; forward invariance (Theorem 10) gives $M(t)\ge0$, so the improper integral is at most $M(0)$. If $qEN\equiv qE^*N^*$ for all $t\ge0$, the integral would diverge. $\blacksquare$

This is the depletion-horizon semantics of the closed ledger in its strongest form: the donor budget is finite, and extraction is integrable against it. A constant extraction flux $c>0$ — a comparison flux only, not a donor-limited primitive the ledger's own discipline admits as a sustained law — exhausts the budget in finite time ($M$ reaches its lower bound no later than $M(0)/c$), while proportional extraction $qEN$ need not drive $M$ to zero in finite time. The integral bound of the theorem **is** the whole statement, and the hitting time of $M=0$ may be infinite. This is the finite-budget fact that §9 turns into the non-reduction boundary with the open working system.

The theorem does not select among the vanishing-extraction rests of Theorem 13: integrable extraction is compatible with approach to either the extinction family or the carrying-capacity–geochemical family, and the $L^1$ bound alone decides nothing between them.

## 4.8 The conditional hybrid moiety balance

**Conditional Theorem 15 (Hybrid moiety balance).** *Let $\chi$ denote the hybrid state and $\eta\ge0$ its primitive-flux vector — letters local to this statement, chosen so that $r$ stays the growth rate of §2.2 and $\nu$ a macro parameter of §5.4. Assume (H1) $\chi$ is absolutely continuous between locally finite event times, with left and right limits at events; (H2) $\dot\chi=S\eta+b$ with $\eta\ge0$, separate reverse columns, and donor-limited negative boundary flows; (H3) $L^{\top}S=0$. Then*

$$L^{\top}\chi(t)-L^{\top}\chi(0)=\int_0^tL^{\top}b\,ds+\sum_{t_k\le t}L^{\top}\big[\chi(t_k^+)-\chi(t_k^-)\big].$$

*Proof.* Integrate the continuous balance between consecutive events and telescope the left/right state differences. $\blacksquare$

The theorem is conditional, and its jump interpretation is part of the content: an internal-transformation jump requires $L^{\top}(\chi^+-\chi^-)=0$ or a jump incidence factorization with left-kernel conservation; a boundary-crossing jump is a boundary impulse and belongs in the boundary term. Two obligations ride the theorem. The **yield-routing obligation**: if a transformation is represented with a yield below one for a declared moiety, the omitted fraction must be routed to another represented compartment or a declared boundary flow — otherwise the claimed moiety balance holds only after silently dropping that moiety from $L$. And the **separation obligation**: this is the hybrid variant of Proposition 4, retained at its own conditional status; the two statements are not merged.

## 4.9 Cancellation is cheap

Summing the six material equations of a ten-state admissibility template gives the exact identity

$$\frac{d}{dt}\big(\bar X_A+X_J+P+U+A+G\big)=0 .$$

This is an algebraic cancellation only. It does **not** prove forward invariance of the six material states, or physical admissibility of every term. The ghost-sink check is part of the discipline: the same birth-transfer rate $gB$ enters $\dot X_J$ and $\dot A$ with opposite signs, so material not transferred to juveniles remains in $A$ — there is no unmatched sink in the six-state ledger.

The identity is retained precisely for its discipline. Formal cancellation coexists with boundary failure elsewhere in the same template (its geological exchange is **not** donor-limited), and the cancellation by itself establishes nothing about admissibility. Conservation (Theorems 7–9) and positivity (Theorems 10–11) are proved separately in every well-posed ledger of this article, exactly because **cancellation is cheap and admissibility is not**. The template's remaining negative witnesses — a variance closure that is not realizable by a non-negative spatial distribution, and an output functional without a displayed state equation — are recorded in the supplementary material as audited admissibility failures.

**The closed-ledger portrait.** Theorems 7–14 assemble into a complete qualitative portrait of the closed orthant: conservation (Theorems 7–9), positivity (Theorems 10–11), no interior rest at positive effort (Theorem 12), the two-family vanishing-extraction rest set with the frozen-biomass face (Theorem 13), and the finite donor budget (Theorem 14). The portrait is the source object handed to the interface of §9: the closed system's candidate long-time set is the rest set of Theorem 13, and the budget of Theorem 14 bounds how long any positive-flux configuration can persist.

For industrial-ecology measurement the message is direct: a "balanced" closed ledger is a **finite-budget** object, and any sustained extraction against it must integrate to a quantity no greater than the initial budget.

---

# 5. Services and the componentwise deficit — what is delivered, and what is missing

> **In plain words.** A service is not a substance. Drinking water, crop yield, fish landed: these are readings taken off the physical state, not extra mass in the boxes. This section says what a reading has to declare before it can be used, and then builds the deficit — the shortfall, component by component, which is a vector and never a number.

Services are observations or feasible outputs of the physical state, not additional conserved mass. Internal physical transfers are not services merely because they appear in a ledger. A typed readout identifies the delivered flow, its boundary, and any unit conversion. This distinction is the accounting counterpart of the ecological-economics point that a service flow — Ayres' useful-work reading, Daly's throughput-of-services reading — is not the same object as the mass that delivers it.

## 5.1 The service readout and the contemporaneous balance

For services indexed by $i=1,\dots,n$, write $s_i(t)=O_i(x(t),u(t),\theta)$, where $u$ denotes admissible operating or extraction choices and $s_i$ and the demand $d_i$ share service-specific units. Where delivered services are selected or converted ledger fluxes, the readout is linear in the primitives,

$$s=O(x,u,\theta)=Q(\theta)v(x,u),$$

with every row of $Q$ declaring the delivery boundary and the conversion into one service-specific unit. More general state-dependent readouts are possible. The contemporaneous component balance is

$$b_i(t)=s_i(t)-d_i(t),$$

and $b_i(t)\ge0$ means measured supply meets measured demand for component $i$ at that instant. It does not by itself imply that the underlying trajectory is sustainable. A stock can meet current demand while declining toward a threshold, and a stock below a desired level can have a positive current balance while recovering.

## 5.2 The state-dependent feasible balance domain

**Definition 1 (Feasible balance domain).** *For an admissible operating set $\mathcal U(x,t)$ and a declared demand set $\mathcal D(t)$,*

$$\mathcal B(x,t)=\{O(x,u,\theta)-d: u\in\mathcal U(x,t),\ d\in\mathcal D(t)\}.$$

The geometry of the balance domain is state dependent and inherited partly from the stock–flow model. **No unrestricted argument can replace an application-specific analysis of $\mathcal B(x,t)$.** This domain is the object against which any scalar certificate claim must be checked (§10.1): a weighted sum certifies componentwise non-negativity on $\mathcal B(x,t)$ only through an implication proved from the physical restrictions that define the domain.

## 5.3 Support provenance and the directional support gap

Current service adequacy and regenerative feasibility are different claims. Let $\Gamma_{\mathrm{all}}(x,t)\subseteq\mathbb R^n_+$ contain the service vectors feasible through all pathways admitted by an application, and $\Gamma_{\mathrm{reg}}(x,t)\subseteq\Gamma_{\mathrm{all}}(x,t)$ the feasible set after imposing the declared regenerative-flow, system-boundary, material-quality, and exergy or capacity restrictions. These correspondences are **application inputs** obtained from a typed pathway or technology model; the stock ledger alone does not construct them.

**Definition 2 (Directional regenerative-support fraction and gap).** *Assume (H1) $0\in\Gamma_{\mathrm{reg}}(x,t)$; (H2) a nonzero service direction $\bar s\ge0$ is chosen. Define*

$$\alpha_{\mathrm{reg}}(\bar s;x,t)=\sup\{\alpha\in[0,1]:\alpha\bar s\in\Gamma_{\mathrm{reg}}(x,t)\}.$$

*The vector $(1-\alpha_{\mathrm{reg}})\bar s$ is the directional support gap, measured in the same service units as $\bar s$. A realized service $s\in\Gamma_{\mathrm{all}}\setminus\Gamma_{\mathrm{reg}}$ is **support-dependent under that declaration** even when $s\ge d$.*

Attainment requires closedness: if $\Gamma_{\mathrm{reg}}$ is not closed the supremum may not be attained, and the gap is relative to a supremal fraction, not necessarily to an achievable boundary service. The **non-interpretation discipline** is equally part of the definition: the statement neither subtracts raw material from service nor proves that a physical stock is declining. Net depletion still requires a negative stock balance or a trajectory argument. The provenance partition behind $\Gamma_{\mathrm{reg}}$ — renewable flow, recovered or recycled material, imports, non-renewable drawdown — never adds unlike physical units.

## 5.4 The componentwise deficit and the specialization identity

On the unreduced ledger the physical deficit is the diagnostic

$$\Delta_{\mathrm{phys}}(t)=C(t)-\hat M^{\top}S(t),$$

with $C$ the operative extraction-law readout and $\hat M$ the declared demand-coverage matrix mapping the moiety readout $S=Cx$ — the composition matrix $C$ of Lemma 3, **a different object from the coverage vector $C(t)$ despite the shared letter** — into the units of that coverage vector: rows indexed by covered services, columns by moieties, entries the declared stoichiometric coefficients of the coverage convention. The hat distinguishes the matrix from the scalar natural-block mass $M$ of §4.1. It does not drive the physical equations, and it is not equal to $-\dot N$ unless waste–product feedback vanishes and the service is identified with regeneration. The single-resource specialization (the omitted product, waste and price parameters $\mu,\nu,\rho$ of the unreduced ledger set to zero, together with $C_A=0$) makes that identification, and **on that class — and only on that class — the deficit collapses to the stock-decline rate.**

**Remark 16 (Exact specialization deficit identity).** *On every trajectory of the specialized system, and of every reduced system whose stock equation is $\dot N=R(N,A)-qEN$,*

$$qEN-R(N,A)=-\dot N,\qquad \Lambda(t):=[qEN-R]_+=[-\dot N]_+ .$$

*Proof.* Substitute the stock equation: $qEN-R=-(R-qEN)=-\dot N$. $\blacksquare$

The collapse is a **property of the specialization**, not a definition of liquidation on the unreduced ledger. The general diagnostic remains $C-\hat M^{\top}S$.

**Decline pressure.** In the registered delay family the depletion-pressure classification is

$$\Lambda(t)=\max\{0,\;qE(t)N(t)-R(N(t),A_{\mathrm{act}}(t))\}=\max\{0,-\dot N(t)\}:$$

the memory input of the institutional dynamics is a smoothed stock-decline rate, exactly the positive part of the decline. It is **not** a stock-level scarcity measure, **not** an unmet-consumption measure, and **not** an independently observed service deficit.

Since $qEN-R(N,A_{\mathrm{act}})=O(N)$ as $N\to0$, the raw decline input vanishes near extinction while the positive baseline source of the effort law can still sustain commanded effort. The incremental decline amplification disappears, but the effort command need not. A controller intended to respond to low stock *irrespective of its current rate of change* requires a separately registered level-dependent channel.
# 6. Depletion arithmetic — three numbers that all get called "years left"

> **In plain words.** People ask one question — how long do we have? — and three different numbers answer it. (1) How hard the system is turning over right now. (2) How long the current decline would take if the rate were frozen at today's value. (3) When a *stated* model, under a *stated* scenario, first crosses a *stated* line. These are not three estimates of one thing. They are three different questions. This section defines all three, proves how far apart they can be, and then classifies the three public numbers everyone quotes.

The ledger supplies the net active-pool derivative needed to tell gross throughput apart from net decline and from a model-conditioned threshold time. The distinction matters because "time to depletion" is publicly used as if all three were one quantity. They are not, and the worked instances below make the differences explicit. Let $A_{\min}$ be a declared threshold for the active abiotic pool, with $A>A_{\min}$.

## 6.1 The three quantities

**Definition 3 (Gross turnover intensity and support coverage).** *With assimilation $g(X,A)>0$, the gross turnover intensity is $J^{\mathrm{gross}}_A=g(X,A)/A$ and the gross support-coverage ratio is $H^{\mathrm{gross}}_A=(A-A_{\min})/g(X,A)$. **Neither is a time to depletion.***

The implication $g>0\Rightarrow\dot A<0$ is false in general. At an interior steady state, $g$ can be positive while decomposition and geological transfer balance it exactly, so that $\dot A=0$. Gross uptake measures throughput or dependency. Net depletion is a balance property.

This false-implication record is the first rung of the taxonomy, and it governs every application below.

**Definition 4 (Local net-depletion ratio).**

$$\mathcal H^{\mathrm{loc}}_A(t)=\frac{A(t)-A_{\min}}{[-\dot A(t)]_+},\qquad\text{with the extended-real convention }\ \mathcal H^{\mathrm{loc}}_A=+\infty\ \text{when }\ \dot A\ge0.$$

The convention is not a courtesy. It correctly reports *no current net decline* at a stationary or replenishing state. The ratio is still not a trajectory forecast: it freezes the current net rate. If the fluxes change with $A$, policy, climate, prices or other states, the realized threshold time can differ substantially.

**Definition 5 (Scenario-conditioned hitting time).** *For a fully specified dynamical model, policy or scenario $\pi$, disturbance history $d$, and initial state $x_0$,*

$$T_A(x_0;\pi,d)=\inf\{t\ge0: A^{\pi,d}_t(x_0)\le A_{\min}\},\qquad T_A=+\infty\ \text{if the threshold is never reached}.$$

Under parameter, observation and scenario uncertainty, the appropriate output is a **distribution or robust interval** of $T_A$, not a single universal date.

| Quantity | Question it answers |
|---|---|
| $J^{\mathrm{gross}}_A,\ \mathcal H^{\mathrm{gross}}_A$ | How strongly does the system depend on, or turn over, the pool at the current gross rate? |
| $\mathcal H^{\mathrm{loc}}_A$ | If the current net decline were frozen, what is the local stock-to-rate ratio? |
| $T_A$ | Under a stated model, policy and disturbance scenario, when is the threshold first reached? |

The three quantities answer different questions and must not share one depletion-horizon label.

## 6.2 Uniform-drift bounds

**Proposition 17 (Local threshold-horizon bracket).** *Assume (H1) $A:[0,T]\to\mathbb R$ is absolutely continuous with $A(0)>A_{\min}$; (H2) constants $v_0>0$ and $0<\varepsilon<1$ are given, and $H_0=(A(0)-A_{\min})/v_0$; (H3) $T\ge H_0/(1-\varepsilon)$; (H4) $(1-\varepsilon)v_0\le-\dot A(t)\le(1+\varepsilon)v_0$ for almost every $t$ while $A$ stays above $A_{\min}$. Then a first crossing time $H$ exists no later than $H_0/(1-\varepsilon)$, and*

$$\frac{H_0}{1+\varepsilon}\ \le\ H\ \le\ \frac{H_0}{1-\varepsilon},\qquad |H-H_0|\ \le\ \frac{\varepsilon}{1-\varepsilon}\,H_0.$$

*Proof.* If no crossing occurs before $t^*=H_0/(1-\varepsilon)$, absolute continuity gives $A(t^*)\le A(0)-(1-\varepsilon)v_0t^*=A_{\min}$, a contradiction; hence $H\le t^*$. Integrating both rate bounds over $[0,H]$ and using $A(0)-A(H)=v_0H_0$ gives the two-sided bracket: from the upper rate bound $v_0H_0\le(1+\varepsilon)v_0H$, and from the lower rate bound $v_0H_0\ge(1-\varepsilon)v_0H$. $\blacksquare$

In words: promise that the decline stays within 10% of a fixed rate, and the frozen-rate ratio is guaranteed to be within about 11% of the true crossing time.

This is a **local** diagnostic only. It fails when depletion reverses, when the rate approaches zero, or when feedback moves the trajectory outside the declared rate bounds. Its companion is the one-sided exhaustion proposition of §3.6, whose counterexample — proportional extraction never exhausts in finite time — shows that the uniform margin $\varepsilon>0$ is load-bearing in both directions. The bracket bounds the frozen-rate ratio's error under declared rate bounds, and nothing more.

**When the clocks coincide.** Under the rate bracket the frozen-rate ratio and the true hitting time agree within the bracket: $-\dot A\in[(1-\varepsilon)v_0,(1+\varepsilon)v_0]$ gives $\mathcal H^{\mathrm{loc}}_A=(A(0)-A_{\min})/[-\dot A]_+\in[H_0/(1+\varepsilon),H_0/(1-\varepsilon)]$, hence

$$|H-\mathcal H^{\mathrm{loc}}_A|\le\frac{2\varepsilon H_0}{1-\varepsilon}$$

— the only regime in which the frozen-rate ratio *is* a horizon. At a stationary state ($\dot A=0$) with $g>0$, $\mathcal H^{\mathrm{loc}}_A=+\infty$ while $\mathcal H^{\mathrm{gross}}_A<\infty$. The three quantities of §6.1 coincide only under a declared rate bracket, and the false implication $g>0\Rightarrow\dot A<0$ is the reason.

## 6.3 Upper barriers, exit times, and maintainability

The lower-barrier setting of §6.1 is one half of the story. For each moiety $m$ define the lower and upper exit times

$$\tau_m^-=\inf\{t\ge0:S_m(t)\le\underline B_m(t)\},\qquad \tau_m^+=\inf\{t\ge0:S_m(t)\ge\overline B_m(t)\},\qquad \inf\varnothing=\infty,$$

and the overall admissibility exit time $\tau_{\mathrm{exit}}=\min_m\{\tau_m^-,\tau_m^+\}$; **horizon safety on $[0,T]$ is $\tau_{\mathrm{exit}}>T$**. Note the minimum is taken over all moieties $m$ — both signs, every component.

Two disciplines attach.

1. **Equality at the hitting time** — $S_m(\tau_m^-)=\underline B_m(\tau_m^-)$ — requires continuity of both $S_m$ and $\underline B_m$ and appropriate initial separation. If fluxes or barriers can jump, the stock can cross the barrier *without* satisfying equality.
2. **Lower barriers need not be exhaustion thresholds.** The diagnostic distinguishes physical exhaustion ($S_m=0$), functional failure ($S_m=\underline B_m^{\mathrm{func}}$), a resilience or regime-shift threshold, an economically recoverable reserve, and a minimum service-supporting stock. The term "exhaustion" is reserved for $S_m=0$; all other thresholds are barrier violations.

Upper-barrier violations matter symmetrically: a system may satisfy every lower-barrier condition while violating an upper barrier, $S_m(t)>\overline B_m(t)$. Atmospheric CO₂ accumulation violates an upper concentration barrier while fossil carbon stocks decline. The depletion diagnostic must check both barriers.

And a stock can remain above a barrier until an assessment horizon $T$ and still be unsustainable thereafter. If the assessment claims *sustainability* rather than *finite-horizon admissibility*, it needs a terminal condition $x(T)\in\mathcal K_{\mathrm{maint}}$, where

$$\mathcal K_{\mathrm{maint}}=\{x:\exists\ \text{an admissible continuation satisfying all barriers for } t\ge T\}$$

— the set from which barrier safety is indefinitely maintainable: the viability kernel of the barrier set under the admissible controls (Aubin, 1991). The finite-horizon diagnostic is a **necessary but not sufficient** condition for sustainability. The full certificate requires the terminal state to lie in the maintainability set.

## 6.4 Robust semantics

For uncertain parameters $\theta\in\Theta$ and admissible disturbances $d\in\mathcal D$, robust barrier safety is

$$\text{RobustBarrierSafe}(x(\cdot))\iff \underline B_m(t)\le S_m(t;\theta,d)\le\overline B_m(t)\ \ \forall m,\ \forall t,\ \forall\theta\in\Theta,\ \forall d\in\mathcal D,$$

and the depletion-horizon classification is fourfold: **nominal** ($\theta=\theta_0$, $d=0$); **worst-case** ($\inf_{\theta,d}\tau_{\mathrm{exit}}(\theta,d)$); **probabilistic** ($\Pr[\tau_{\mathrm{exit}}>T]\ge1-\varepsilon$); and **scenario-conditioned** ($\tau_{\mathrm{exit}}\mid\theta=\theta_s$). The componentwise diagnostic applies to each scenario, and the conjunctive criterion applies within each scenario and across scenarios. **No single number is promoted across the four classes without a declared map.**

## 6.5 Application classifications at their exact status

The classification matrix records, quantity by quantity, what each application computes and what each object is. The numerical exhibits that follow are worked instances of the constructions, and **the classification of each row does not depend on the magnitudes**.

| Time-like quantity | G3P $\mathcal L^{\mathrm{anom}}_{\mathrm{hist}}$ | Phosphate $\mathcal T_{\mathrm{reserve}}$ | Fisheries $\Theta_F$ |
|---|---|---|---|
| $J^{\mathrm{gross}}_A,\ \mathcal H^{\mathrm{gross}}_A$ — turnover / dependency | no | no | gross-loss analogue only — **not a member** (§6.5.4) |
| $\mathcal H^{\mathrm{loc}}_A$ — frozen net-rate ratio | no (anomaly, not stock) | no (classification, not stock) | no (no net $\dot B$) |
| $T_A$ — scenario hitting time | no | no | no |
| **What it is** | record-relative statistical index | arithmetic ratio of an economic class | removals-only pressure scale |

### 6.5.1 Groundwater anomaly-persistence indices

The G3P column of the matrix is the groundwater case. The Global Gravity-based Groundwater Product (G3P v1.12; Güntner et al., 2024; the GRACE line it descends from is Tapley et al., 2004) provides monthly **groundwater-storage anomalies relative to a reference period**, not absolute aquifer volumes. For a basin-mean anomaly series over the reported April 2002 – September 2023 window, the linear-trend anomaly persistence index is

$$\mathcal L^{\mathrm{anom}}_{\mathrm{hist}}=\frac{a_{\mathrm{latest}}-a_{\mathrm{hist,min}}}{[-\dot a]_+},$$

the fitted distance to the series' own historical minimum divided by the fitted decline rate. The four-basin record: Indo-Gangetic $-49.7$ cm/yr with index $\approx2.7$ yr; North China Plain $-18.6$ with $\approx7.9$; Central Valley $-16.1$ with $\approx9.5$; La Mancha $-3.2$ with $\approx21.4$.

Classification, stated at the product's own status: a **statistical anomaly index with units of time** — not the physical stock ratio $\mathcal H^{\mathrm{loc}}_A$, and not a forecast of aquifer exhaustion. Its value depends on the product window, the basin mask, the anomaly reference and the linear-trend convention. A physical $\mathcal H^{\mathrm{loc}}_A$ requires an absolute stock estimate and a net stock derivative — aquifer geometry or saturated thickness together with storage parameters — not an anomaly series alone.

A structural point sharpens the boundary. The **access structure** — a well, or an index well — is infrastructure rather than the resource. It draws on stored water (the stock), which is replenished by recharge (the flow). The anomaly series measures the stored stock as observed at the access point; it measures neither the access infrastructure nor the recharge. An index built on it therefore cannot distinguish a drawdown of stored water that is recoverable on the recharge timescale from one that is not — although heavy over-extraction can make the loss permanent through compaction, subsidence or saline intrusion, in which case it is not recoverable at all. The index is exactly the record-relative object analysed in §7.3, and its interpretive boundary is that record-relativity (§7.7).

### 6.5.2 The applied depletion-horizon tables

Component-resolved depletion horizons on public data products are tabulated below, computed **without fitting any dynamical parameter** of the reduced systems. Rows marked with a dagger (†) are quarantined and must not be taken at face value: the Australia phosphate row dates to a pre-2026 reserve vintage (§6.5.3), and the Indo-Gangetic groundwater magnitude sits an order of magnitude beyond published basin-mean trends (the quarantine note below). Both are retained only as worked instances of the constructions, and neither enters any classification below.

**Groundwater (G3P v1.12 basin series).**

| Basin | Trend (cm/yr) | 2023 anomaly (cm) | Window minimum (cm, implied) | Horizon to window minimum (yr) |
|---|---|---|---|---|
| Indo-Gangetic (N. India)† | −49.7 | −414 | −548 | ≈ 2.7 |
| North China Plain | −18.6 | −145 | −292 | ≈ 7.9 |
| Central Valley (US) | −16.1 | −84 | −237 | ≈ 9.5 |
| La Mancha (Spain) | −3.2 | −20 | −88.5 | ≈ 21.4 |
| High Plains (US) | −7.9 | −160 | −160 | already at minimum (0.0) |
| global mean | −0.4 | −14 | −33.0 | ≈ 47.5 |

> **Quarantine note, placed adjacent to the row it marks** (recorded data-vintage decision: the row stays first, daggered). The Indo-Gangetic magnitude **must not be reused numerically**: it sits an order of magnitude beyond published basin-mean trends and awaits re-derivation from the product's basin masks — the full quarantine record is the paragraph below. The basin rows are reported extractions from the G3P v1.12 basin series, used here only to exhibit the index construction of §6.5.1. The window-minimum column is implied by the displayed trend and horizon through the index formula of §6.5.1 — **arithmetic, not product-endorsed** — and every basin row must be re-derived from the product's basin masks before any numerical reuse. The Indo-Gangetic magnitude is the extreme case: it sits an order of magnitude beyond published basin-mean groundwater-equivalent trends (typically a few cm yr⁻¹), and a linear trend of −49.7 cm yr⁻¹ maintained over the reported ≈ 21.4 yr window would place the fitted 2002 value near **+6.5 m** above the anomaly reference — the fitted segment convention is part of the quarantine. The rows are retained only as the worked instance of the index construction, and the classification status assigned below does not depend on the magnitudes.

**Phosphate (reserve-life arithmetic).**

| Country | Reserves (kt) | Reserve-life horizon (yr) | Implied production (kt/yr) |
|---|---|---|---|
| China | 3,400,000 | ≈ 28 | 121,429 |
| United States | 1,000,000 | ≈ 45 | 22,222 |
| Jordan | 820,000 | ≈ 62 | 13,226 |
| Morocco | 50,000,000 | ≈ 1,250 | 40,000 |
| Australia† | 5,800,000 | ≈ 2,088 | 2,778 |
| World (reserves) | 74,000,000 | ≈ 309 | 239,482 |
| World (resources, $\varepsilon=0.10$) | > 300,000,000 | > 1,125 | 240,000 |

*How to read the last two rows.* They answer different questions, and they are kept apart on purpose. The reserve horizon is reserves ÷ production. The resources row applies the article's declared threshold convention of §6.5.3, $T_{\mathrm{resource},10\%}=0.9\,G_{\mathrm{resource}}/C_G$ — the horizon runs to the point where 10% of the resource base remains, which is why it is 0.9 × (resources ÷ production) rather than 0.1 × (resources ÷ production).

**Fisheries.** The column reports the **archived-depletion-horizon (ADH)** pure-decay proxy

$$\mathrm{ADH}=F^{-1}\log\!\big(\mathrm{SSB}_{\mathrm{now}}/(0.2\max \mathrm{SSB})\big)$$

under current fishing mortality $F$, with median **≈ 1.8 yr** across the **43** assessed stocks with finite spawning-stock-biomass (SSB) and $F$ series — the archived pull, kept in place as the headline cohort by the recorded data-vintage decision — computed with $\mathrm{ADH}=0$ entered for the **eight** stocks already at or below the reference: the zero convention of the source table's caption, **which the median includes**.

Two disclosures accompany the headline value (both recorded). The archived 43-stock cohort is reproduced by **neither** public RAM Legacy release — S5's version-sensitivity record, cross-referenced here, is the retraction and the row-by-row re-verification — and the v4.66 public-release broad-cohort reading (454 stocks, median 3.39 yr) is the primary public-release comparison, executed in S5 and detailed below. The qualifying positive sub-cohort ($F>0$ and $\mathrm{SSB}_{\mathrm{now}}>\mathcal B_{\mathrm{lim}}$; 35 stocks) has median 2.9 yr; both medians come from the archived pull alone.

The cohort is a **selected class, not a random sample** of assessed stocks: all 43 stocks are small pelagics (18 anchovy, 20 herring, 4 sprat, 1 sardine), the fast-maturing class the companion review screen (Author, E., et al., *in review*) selects by its annual-review eligibility criterion (42 of the 43 are that screen's annual-managed spectral-null stocks, per the source caption). The ≈ 1.8 yr median is therefore a class-specific diagnostic for fast-maturing, annually managed pelagics — not a statistic of assessed fisheries in general. The executed broad-cohort comparison (§5) runs the same protocol on the full public release — 454 stocks, median 3.39 yr, the upper end carried by the long-lived groups: elasmobranchs 11.5, sebastids 9.0, pleuronectids 6.0 yr — and only **2%** of random 43-stock draws from that broad cohort have medians at or below the class cohort's 1.79 yr.

The extract is the RAM Legacy cohort of Ricard et al. (2012), and the pull date is archived in the analysis repository; the archived pull has been re-verified row by row against the formula — all 43 rows reproduce $\mathrm{ADH}=\max(0,F^{-1}\log(\mathrm{SSB}/B_{\mathrm{lim}}))$ with $B_{\mathrm{lim}}=0.2\max\mathrm{SSB}$. The value is reported with its cohort conditions and is **not promoted to a forecast**. Because cohort composition is database-version-dependent, every cohort statistic is pinned to the archived pull: the quartile summary of $F$ and $\log(\mathrm{SSB}/B_{\mathrm{lim}})$ over the cohort belongs to that pull alone, and no cohort statistic is quoted from a different database version. The cohort protocol is fully specified in the accompanying supplementary material (S5) — including the zero entries for stocks at or below the reference, which enter the median — together with the version-sensitivity record: on the public RAM Legacy releases the same protocol qualifies **415** stocks (v4.44, median **2.57** yr) and **454** (v4.66, median **3.39** yr) — both reproduced to printed precision under the recovered micro-specification (S5) — **neither reproducing the archived 43-stock cohort**: the archived pull's 43-stock list and extract-time series state — supplied and re-verified — differ from both public releases.

**The scope discipline is the tables' load-bearing content.** None of the reported numbers is a computed instance of any model's first-hitting time. The groundwater column is a trend-to-window-minimum extrapolation, the phosphate column a reserve-life ratio, and the fisheries column a pure-decay proxy with recruitment omitted. They are descriptive, component-resolved diagnostics in the two-pool logic of the taxonomy — not dynamical predictions.

**Non-example 1 — a deliberate boundary of aggregation, not a score of the framework.** The equal-weight inverse-horizon score of the four basins still above their window minimum and world phosphate reserves,

$$\Sigma_{\mathrm{reserves}}\approx\frac15\Big(\frac1{2.7}+\frac1{7.9}+\frac1{9.5}+\frac1{21.4}+\frac1{309}\Big)\approx0.130\ \mathrm{yr}^{-1},$$

is a **ranking device, not a componentwise certificate**: it mixes basins and reserves, incommensurable objects under the typing of §2.1, and is retained only to mark the boundary of legitimate aggregation. It is exhibited as the worked instance of the non-compensation boundary of §10.1: a positive aggregate coexisting with componentwise deficits by construction — admissible as communication, **inadmissible as certification**. The article stops at the aggregate. It is not turned back into a horizon, and no reciprocal of it is reported here as a "blended years-left" figure — doing so would be exactly the move the non-example blocks.

### 6.5.3 The phosphate reserve-life ratio

The phosphate column of the classification matrix is the reserve-life ratio. At constant current production $C_G$,

$$\mathcal T_{\mathrm{reserve}}=G_{\mathrm{reserve}}/C_G ;$$

at approximately 74,000,000 kt (74,000 Mt) of world reserves and 240,000 kt/yr of production (U.S. Geological Survey, 2026) this is approximately **309 years**. The arithmetic is internally consistent as a reserve-life ratio to zero. It is **not a physical exhaustion forecast**, because reserve classification changes with prices, technology, exploration and regulation — the point made independently, and forcefully, by Illakwahhi, Vegi and Srivastava (2024) for the single-source USGS data behind the influential phosphate depletion estimates, and standard in mineral economics, where reserves have grown through a century of rising production for copper (Tilton, 2003; Tilton and Lagos, 2007).

The reserves/resources split discipline is part of the classification: a resource-threshold calculation $\mathcal T_{\mathrm{resource},10\%}=0.9\,G_{\mathrm{resource}}/C_G$ answers a different question and **must not share a column with the reserve-life ratio without an explicit convention label**. The reserve classification is economic — US reserves have remained near 1,000,000 kt while cumulative production since 1996 is of order 600,000 kt — and the resource-based world horizon (≈ 1,125 yr at $\varepsilon=0.10$) is more than three times the reserve-based figure (≈ 309 yr). The two-compartment split is what prevents these from being collapsed into one number.

The implied-production column of the §6.5.2 table reproduces the production figure each horizon assumes (production = reserves ÷ horizon) and thereby exposes the source arithmetic; the country horizons reproduce the recorded MCS-vintage ratios.

**The vintage is pinned once.** The single pinned source of record is the *Mineral Commodity Summaries* (MCS) 2026 (U.S. Geological Survey, 2026), and every figure this article quotes at pin status is that vintage's — the pinned source's 2025 world-production column ≈ 250,000 kt and Australia's reserves 120,000 kt (JORC-compliant). The displayed country rows remain at their recorded **pre-2026** vintage under the quarantine dagger (the Australian 5,800,000 kt among them, retained rather than blanked), kept in place as worked instances of the reserve-life construction. Completing the re-pin — replacing the displayed rows row by row with the pinned vintage's per-country reserve figures — is the **registered open data action**; it requires the per-country MCS 2026 reserve table, and no displayed classification depends on it.

### 6.5.4 The fisheries removals-only pressure time

The fisheries column of the classification matrix is the removals-only pressure time. When $\mathrm{SSB}_{\mathrm{now}}>\mathcal B_{\mathrm{lim}}>0$ and $F_{\mathrm{now}}>0$, define

$$R_{\mathcal B}=\log(\mathrm{SSB}_{\mathrm{now}}/\mathcal B_{\mathrm{lim}}),\qquad \Theta_F=\frac{R_{\mathcal B}}{F_{\mathrm{now}}},$$

the **fishing-only time-to-reference**: the crossing time of the deliberately incomplete comparison process $\dot B=-F_{\mathrm{now}}B$. With $\mathcal B_{\mathrm{lim}}=0.2\max\mathrm{SSB}$ this is the construction tabled as ADH in §6.5.2; the two notations are kept because the boundary hypotheses stated here ($F_{\mathrm{now}}>0$, $\mathrm{SSB}_{\mathrm{now}}>\mathcal B_{\mathrm{lim}}$) are exactly the conditions of the positive sub-cohort of §6.5.2 (35 stocks, median 2.9 yr). The reported §6.5.2 median (≈ 1.8 yr) additionally carries the eight zero entries for stocks at or below the reference, per the zero convention of the source caption.

It is a **removals-only pressure timescale**: the time unit comes from rescaling a stock-reference margin by one isolated gross-loss rate. Because recruitment, somatic growth, maturation, natural mortality, density dependence, environmental forcing and future policy are omitted, $\Theta_F$ is not a net biomass depletion diagnostic, not a demographic hitting-time estimate, and **not a member of the $J^{\mathrm{gross}}$–$\mathcal H^{\mathrm{loc}}$–$T_A$ hierarchy**. A genuinely local biomass-decline ratio $\mathcal H^{\mathrm{loc}}_{\mathcal B}=(\mathcal B-\mathcal B_{\mathrm{lim}})/[-\dot{\mathcal B}]_+$ would require a compatible net $\dot{\mathcal B}$ estimate, and a demographic hitting time would require a fully specified population model; RAM Legacy SSB and $F$ data (Ricard et al., 2012) do not by themselves supply these quantities or models.

Spawning biomass is **not** an abiotic support pool. The construction is retained specifically to show why an isolated gross-removal timescale must not be promoted to a net depletion diagnostic.

**The collective implication for material-flow measurement.** The three published "depletion time" numbers — G3P index, phosphate reserve-life, fisheries removals-only time — answer three distinct questions at three distinct evidentiary levels.
# 7. First-passage semantics on declared surrogates — a probability statement about a *statistic*, not about the aquifer

> **In plain words.** A "first-passage time" is the random moment at which something drifting and wobbling first crosses a line. Section 6 used deterministic ratios. Here the article adds noise, because that is what the published critiques and the public debate ask for. The discipline is what makes the result usable: the noise is attached to the *trend statistic* fitted to the data, not to the aquifer, the fish stock or the orebody. So every probability below is a statement about a fitted number. None of them is a forecast about nature, and the section ends with seven sentences that say so.

## 7.1 Two objects, not one

The ledger's own first-passage object is the model hitting time of Definition 5 — a quantity on trajectories of the mass-conserved ledger, or of a named reduced system. The public-data quantities of §6.5 are constructed proxies on observed series. That distinction is the entry discipline of this section: the surrogates below **do not compute the ledger's hitting time**, **do not complete the ledger stochastically**, and **do not identify physical failure thresholds**.

## 7.2 The observed-drift Brownian surrogate

**Definition 6 (Observed-drift Brownian surrogate).** *Let $A_0$ (local to §7.2–7.4; **not** the half-saturation constant of §2.2) be the latest observed anomaly and $\mu=\hat\mu<0$ the fitted drawdown rate. On the scale of the tabulated series, define*

$$A(t)=A_0+\mu t+\varsigma W_t,\qquad A(0)=A_0>\mathcal A^{\mathrm{win}}_{\min},$$

*where $W$ is a standard Wiener process, $\varsigma>0$ a chosen noise scale, and the process is stopped at first reaching the record-relative barrier $\mathcal A^{\mathrm{win}}_{\min}$. This is a statistical surrogate for the empirical trend extrapolation. It is not a hydrological constitutive law, is not mass-conserving, and is not a perturbation or stochastic completion of the ledger's active-pool equation or of the finite-donor primitive system of §2.2. **The non-completion non-claim is part of the definition.***

In words: take the straight line that was fitted to the observations, then allow it to wobble. Anything computed from that wobble is about the line.

## 7.3 The inverse-Gaussian groundwater first passage

**Proposition 18 (Inverse-Gaussian first passage — a standard fact, stated for notation).** *Let $T_{\mathrm{GW}}=\inf\{t>0: A(t)\le\mathcal A^{\mathrm{win}}_{\min}\}$ for the process of Definition 6, and $d=A_0-\mathcal A^{\mathrm{win}}_{\min}>0$. Conditional on treating $\mu$ and the barrier as fixed,*

$$T_{\mathrm{GW}}\sim \mathrm{IG}(\nu,\lambda),\qquad \nu=\frac{d}{|\mu|},\qquad \lambda=\frac{d^2}{\varsigma^2},$$

*in the mean–shape parameterization. In particular $\mathbb E[T_{\mathrm{GW}}]=\nu=\mathcal H^{\mathrm{win}}_{\mathrm{GW}}$ — the deterministic horizon to the window minimum, $=d/|\mu|$ — and $\mathrm{Var}(T_{\mathrm{GW}})=\nu^3/\lambda=d\varsigma^2/|\mu|^3$.*

*Proof.* The first-passage time of a Brownian motion with constant negative drift to a lower barrier is inverse Gaussian — the classical first-passage result (Chhikara and Folks, 1989; Redner, 2001) — with the stated mean and shape parameters; the standard inverse-Gaussian moments give the displayed mean and variance. $\blacksquare$

The mean of the stochastic surrogate equals the deterministic trend-to-window-minimum ratio of §6.5.1. That equality is the precise sense in which the tabled groundwater numbers are first-passage means of a declared surrogate.

**Corollary 19 (Zero-noise limit and median).** *As $\varsigma\to0^+$, $T_{\mathrm{GW}}\to\mathcal H^{\mathrm{win}}_{\mathrm{GW}}$ in probability, and at $\varsigma=0$ the deterministic trajectory reaches the barrier exactly there. For every finite $\varsigma>0$ the inverse-Gaussian median $m$ satisfies $m<\nu=\mathcal H^{\mathrm{win}}_{\mathrm{GW}}$,*

$$F_{\mathcal T}(\nu)=\tfrac12+e^{2\lambda/\nu}\,\Phi\big(-2\sqrt{\lambda/\nu}\big)>\tfrac12 .$$

*The variance scales as $\varsigma^2$ and the standard deviation and small-noise quantile widths as $\varsigma$. The median below the mean is the inverse Gaussian's right skew toward short passage times; **the inequality must not be inverted.***

*Proof.* Evaluate the inverse-Gaussian CDF $F_{\mathcal T}(t)=\Phi\big(\sqrt{\lambda/t}\,(t/\nu-1)\big)+e^{2\lambda/\nu}\Phi\big(-\sqrt{\lambda/t}\,(t/\nu+1)\big)$ at $t=\nu$: the first term is $\Phi(0)=1/2$ and the second is strictly positive for finite $\lambda$, so the median lies strictly below the mean; the concentration statement follows from the variance. $\blacksquare$

These are conditional distributional statements about the surrogate. **They are not corrections to the tabled years, and they do not show that physical water mass is depleted faster.**

## 7.4 The record-relative barrier discipline

The barrier $\mathcal A^{\mathrm{win}}_{\min}$ is selected from the *same finite observation window* used to estimate $\hat\mu$. It is therefore a path-dependent, record-relative threshold, not an independently identified hydrological failure floor. Future passage below it represents a record-breaking stress event under the surrogate, not physical exhaustion.

Three boundary facts complete the discipline.

1. **Already at minimum.** If $A_0=\mathcal A^{\mathrm{win}}_{\min}$, the stopping-time convention gives $T_{\mathrm{GW}}=0$ deterministically for every $\varsigma$. The inverse-Gaussian family has a degenerate boundary limit concentrated at zero, and $\mathrm{IG}(0,0)$ is not an ordinary inverse-Gaussian distribution. **Zero cells report zero relative to the selected observational barrier** — not zero physical uncertainty, and no confirmation of collapse.
2. **Independent physical thresholds.** If an independent physical threshold $\mathcal A^{\sharp}<\mathcal A^{\mathrm{win}}_{\min}$ is specified, the same constant-drift surrogate gives the conditional mean $\mathbb E[T^{\sharp}]=(A_0-\mathcal A^{\sharp})/|\mu|$, longer than the record-relative proxy because the barrier is lower. This is a statement *within the surrogate*, not a general lower-bound theorem for the physical ledger, whose drift and state coupling may differ.
3. **Classification.** The load-bearing content is the interpretation boundary itself: a record-relative barrier makes the passage time a property of the observation window, and no reading of the tabled numbers escapes that qualification.

## 7.5 The geometric-Brownian fisheries first passage

**Proposition 20 (Geometric-Brownian correction — a standard fact, stated for notation).** *Let $\mathrm dB_t=-h\mathcal B_t\,\mathrm dt+\varsigma\mathcal B_t\,\mathrm dW_t$ under the Itô convention, with $h>0$ and $0<\mathcal B_{\min}<\mathcal B_0$, and $\mathcal T_{\mathrm{fish}}=\inf\{t>0:\mathcal B_t\le\mathcal B_{\min}\}$. Then*

$$\mathcal T_{\mathrm{fish}}\sim \mathrm{IG}(\nu_F,\lambda_F),\qquad \nu_F=\frac{\log(\mathcal B_0/\mathcal B_{\min})}{h+\varsigma^2/2},\qquad \lambda_F=\frac{\log(\mathcal B_0/\mathcal B_{\min})^2}{\varsigma^2},$$

*so $\mathbb E[\mathcal T_{\mathrm{fish}}]=\log(\mathcal B_0/\mathcal B_{\min})/(h+\varsigma^2/2)$; as $\varsigma\to0^+$ this converges to the deterministic pure-decay horizon when $h=F$ and $\mathcal B_{\min}=\mathcal B_{\mathrm{lim}}$.*

*Proof.* Itô's lemma (Øksendal, 2003) gives $\mathrm d\log\mathcal B_t=-(h+\varsigma^2/2)\mathrm dt+\varsigma\,\mathrm dW_t$, so the logarithmic threshold is a Brownian first-passage problem with initial distance $\log(\mathcal B_0/\mathcal B_{\min})$ and downward drift $h+\varsigma^2/2$; Proposition 18 applies. Under the Stratonovich convention the log-drift would be $-h$ and the deterministic limit would match the pure-decay horizon $h=F$ exactly: **the $\varsigma^2/2$ shortening is the Itô choice, not a property of the physical process.** $\blacksquare$

For fixed arithmetic drift and the Itô parameterization, the finite-noise mean is strictly shorter than the deterministic horizon. This is a property of the chosen surrogate parameterization; it is **not** a universal claim that environmental variability accelerates physical biomass loss. The construction joins the removals-only classification of §6.5.4 — the same pure-decay process, now under a declared stochastic surrogate.

## 7.6 The constant-production phosphate passage time

Under the deterministic surrogate $\dot G=-P$ with constant production $P>0$, the first-passage time to a fixed threshold $G_{\min}\in[0,G_0)$ is

$$\mathcal T_{\mathrm{phos}}=\frac{G_0-G_{\min}}{P},$$

the reserve-life ratio being the $G_{\min}=0$ special case, and a threshold fraction $\varepsilon G_0$ giving $(1-\varepsilon)G_0/P$. This is a conditional reserve-classification proxy under constant production. Because reserves are an economic classification rather than a fixed physical stock, it is not a forecast of geological exhaustion without an explicit resource and production model. **No stochastic phosphate extension is required for the interpretation.**

## 7.7 The explicit non-claims

The first-passage semantics close with seven explicit non-claims, all of which hold in this article.

1. The Brownian and geometric-Brownian processes are **not** stochastic completions of the ledger and do not conserve its mass compartments.
2. No theorem relates $\hat\mu$ to $-\dot A$ of the reduced systems, to the finite-donor primitive system, or to the institutional delay equations.
3. The model hitting time $T_A$ of Definition 5 is **not shown to be inverse Gaussian**: it would be inverse Gaussian only if the active-pool residual were Brownian with constant drift, which the coupled balance (2) does not supply — the tabled groundwater numbers inherit inverse-Gaussian means from Definition 6's surrogate and from nothing else.
4. The historical groundwater minimum is not an independently identified physical failure barrier.
5. A shorter surrogate median or Itô mean is not evidence of faster physical depletion.
6. The gross active-pool horizon $\mathcal H^{\mathrm{gross}}_A$ of Definition 3 and its productivity-illusion interpretation — the misreading of a large gross-turnover horizon as evidence of slow net depletion, the false implication recorded in §6.1 — are not first-passage results treated here.
7. The fisheries calculation is not a stage-structured fisheries model, and the phosphate calculation is not a geological-reserve model.

## 7.8 Parameter and observation uncertainty

The inverse-Gaussian results condition on the drift, the barrier and the noise scale. In the groundwater application, $\hat\mu$ is estimated from a finite, potentially autocorrelated record, and the barrier is selected from that same record. Measurement error, serial dependence, seasonal forcing, spatial aggregation, trend breaks and common climatic drivers are **separate** uncertainties, and integrating any of them out yields a predictive mixture rather than a single inverse-Gaussian law. A residual scale estimated from the same window does not by itself identify process noise. **No calibrated predictive distribution is claimed**; the full uncertainty treatment belongs to an empirical identification study, not to this article.

For industrial-ecology measurement this discipline is the practical message: first-passage distributions on declared surrogates are usable as descriptive statistics, but their drift, barrier and noise inputs each carry their own identification story, and a calibrated forecast requires that story to be discharged.
# 8. Domain templates at registered status — what a real application would still have to do

> **In plain words.** A "template" is a scaffold with its holes visible. The article names the data and the checks that would have to arrive before a domain claim could be made, and it says plainly that they have not arrived. Nothing in this section is a result. This is also where the paper keeps its promise about the groundwater two-pool model: the requirements are registered, not discharged.

## 8.1 The phosphorus template

The phosphorus domain enters at **registered template status**: an identification ladder for the resource–product–waste–detritus structure of §2.3 (phosphate rock → fertilizer → soil pool → runoff, with the mining flux $c_G$ and the recycling routes $\alpha,\rho_P$), whose constitutive content — the yield and loss functions, the recovery fractions, the price response of the reserve classification — is **declared, not established**. The reserve and production quantities used in §6.5.3 carry their source vintage (U.S. Geological Survey, 2026). The template's competing-model ladder is an identification object, and its falsification protocols — *which observation would reject which routing assumption* — are recorded obligations, not results.

## 8.2 The groundwater template and the two-pool gap

The groundwater template enters at registered status with an admitted object and a declared gap.

- **Admitted object.** The one-pool affine approximation behind the anomaly-persistence index of §6.5.1.
- **Not established.** The two-pool model — active storage with a slow donor pool, the two-compartment structure of §2.2.

The registered identification requirements for closing the gap are: geological geometry (aquitard depth and extent); multi-depth heads; pumping tests; tracer, isotope or water-age evidence; recharge estimates; prior ranges for the storage and fast–slow coupling parameters; and the discipline that **leakage terms may not absorb unexplained residuals**.

## 8.3 Extractor-side harvest economics

On the extractor side, the same discipline applies to economic steady states.

In the open-access equilibrium of a single-species fishery (Clark, 1990), the bioeconomic equilibrium stock

$$S_{\mathrm{OA}}=\frac{c}{pq}$$

is set by cost, price and catchability — and is **infeasible as a management target** under a conservation floor $S_{\min}>S_{\mathrm{OA}}$: the unregulated equilibrium lies below the floor, and no open-access trajectory is viable against it. The modified golden rule in its constant-unit-cost form, $g'(S_\delta)=\delta$, sets the optimal steady stock for the discount rate $\delta$ (Clark's general form carries an additional marginal-stock-effect term). A harvest tax shifts the open-access equilibrium to

$$S_{\mathrm{OA}}=\frac{c}{(p-\tau)q}.$$

The tax moves the economic equilibrium, but it does not move the physical floor. That distinction is the extractor-side counterpart of the accounting discipline of §6: **instrument parameters and constraint thresholds are different objects, and no tax schedule substitutes for a constraint the ledger must satisfy.**

The growth function $g$ of this paragraph is a declared constitutive readout on the stock **for this extractor-side remark only**. It is not a primitive of the closed natural block of §2, and nothing in this section is promoted into the typed ledger.

---

# 9. The interface with institutional delay dynamics — one shared equation, and a wall

> **In plain words.** There is a companion paper about institutions that review extraction periodically, with delays. This article is about the material ledger. They agree on exactly one object, an identity for the deficit. Beyond that object they cannot be merged, and this section proves the impossibility rather than asserting compatibility. That is the unusual part: a paper naming the bridge *and* the gap, with numbers for both.

The partition between this article and the companion delay-dynamics analysis (Author, D., et al., *in review*) is fixed by an **interface contract**. This article owns the closed material accounting: the primitive ledger equations and full routing, the conservation and positivity theorems of §4, the componentwise deficit and depletion diagnostics of §§5–6, and the closed-donor no-rest and extraction-integrability limitations. The companion owns the open frozen-donor retarded systems and their bifurcation results. The interface is viable — but **not** because the closed primitive ledger dynamically reduces to the open working system. The two are different completions, and the contract records both the exact shared object and the rejected mapping.

**The exact shared object.** Under the single-resource specialization of §5.4 ($\mu=\nu=\rho=0$ — the product, waste and price parameters of the unreduced ledger: its macroeconomic-feedback, recycling and price-response channels, per the §2.2 gloss — and the mining intensity $C_A=0$), with the local stock equation $\dot N=R-qEN$, the deficit identity

$$D(t):=qE(t)N(t)-R(N(t),A(t))=-\dot N(t),\qquad \Lambda(t):=[D(t)]_+=[-\dot N(t)]_+$$

holds for every trajectory of either the specialized ledger or the reduced core (Remark 16). The identity is the **one** object both analyses may use without substantive duplication. The reduced core's constitutive replacement $R(N,A)\to rN(1-N/K)$ is separately an approximation and carries its own finite-time scope (Theorem 1 and Remark 2: the replacement is pointwise on the interior support region and non-uniform through the depleted-pool boundary).

The contract fixes more than the deficit identity. The shared object includes the non-negative orthant and the sign pattern of harvest as an outflow from the living stock. **A companion model that routes the "unsustainable portion" of a flow into a different compartment changes the incidence and thereby leaves the interface** (§2.5).

**The hand-off projection.** Under the institutional-failure specialization, the macroeconomic block, prices and demand do not appear in $(\dot N,\dot A_{\mathrm{act}},\dot A_{\mathrm{geo}},\dot U,\dot Z,\dot E)$ — the closed block's six right-hand sides, geological donor included: each depends only on the block's own variables and the delayed memory, and none contains the macroeconomic states, prices or demand. The ecological–institutional subsystem is an exact closed projection **for every parameter value**, with no singular limit required. The memory–effort pair $(Z,E)$ is the gated three-state core and working four-state core of the companion delay-dynamics analysis (*in review*; eq. (1) and §2.4 of that analysis), not an object of this article; the projection claim — the semiconjugacy condition $\mathcal D_\pi(\xi)f(\xi)=F(\pi(\xi))$ on the history phase space — is made under that citation and is **not re-proved here**.

**The non-reduction boundary.** There is no exact dynamic reduction from the closed primitive finite-donor ledger to the open working system — not as a projectable reduction and not as a regular perturbation. The reasons are mathematical.

1. **Different targets.** The primitive ledger uses the intrinsic donor-limited target $A_{\mathrm{eq,intrinsic}}$; the working system uses the derived target $A_{\mathrm{eq},W}=A_{\mathrm{eq,intrinsic}}+\kappa_AK/\omega_A$. The three registered numbers display the separation: $A_{\mathrm{eq,intrinsic}}=50$, the working active pool $A_{\mathrm{act},*}=397.87$, and $A_{\mathrm{eq},W}=50+\kappa_AK/\omega_A=5{,}050$ — the two equilibria differ by a factor of eight and the two targets by two orders of magnitude.
2. **Same state, different fields.** At the working equilibrium the two $A_{\mathrm{act}}$ vector fields, written at the same state $(N,A_{\mathrm{act}},U)$, differ by

$$\omega_A\big(A_{\mathrm{eq},W}-A_{\mathrm{eq,intrinsic}}\sigma\big)-\gamma_UU=\kappa_AK-\gamma_UU$$

under the registered scale separation ($\sigma\approx1$): approximately **0.535** stock units per year at the working point's quasi-rest detritus level (where $\gamma_UU=\mathcal T^*\approx4.47$, the gross uptake at the working point) and $\kappa_AK=\mathbf{5.000}$ stock units per year at $U=0$ — an $O(1)$ to $O(\kappa_AK)$ discrepancy, not a small residual. The two same-state flux readings behind it are the working recharge $\omega_A(A_{\mathrm{eq},W}-A_{\mathrm{act},*})=4.652$ and the closed donor flow $e_{GA}-e_{AG}\approx-0.348$, whose signed difference is $4.652+0.348=5.000=\kappa_AK$. The difference is $U$-dependent because the working field omits the detritus return $\gamma_UU$ that the closed field carries — the $U$-handling split is part of this obstruction, and $\mathcal B^*-R^*=\mathcal T^*$ is the working system's turnover balance, **not** the field difference.
3. **The working point is not at rest in the closed system.** It requires continuing geological support — the flux $\omega_A(A_{\mathrm{eq},W}-A_{\mathrm{act},*})=4.652133\ldots$ stock units per year, supplied every year by a donor the working system treats as a parameter — and is not a rest point of the closed finite-donor system (Theorem 12). At the same state the closed primitive donor flow is $e_{GA}-e_{AG}=\omega_A(A_{\mathrm{eq,intrinsic}}-A_{\mathrm{act},*})\approx-0.348$: **the donor gains in the closed ledger where the working completion has it losing 4.652** — the two fields have opposite signs on the donor coordinate, not merely different magnitudes. The working-point figures $E^*\approx2.090$, $N^*=89.526$, $A_{\mathrm{act},*}=397.87$ and the recharge $4.652$ are imported at the companion's registered precision; the reverse check $qE^*N^*=0.001\times2.090\times89.526\approx0.187$ is consistent to the quoted digits.
4. **The draw diagnostic is not an error measure.** The cumulative donor-draw quantity $\varepsilon_G(T)=G_0^{-1}\int_0^T|e_{GA}-e_{AG}|\,dt$ is a diagnostic of the *derived-target completion*, not a trajectory-tracking error between the two fields; **no finite-time tracking theorem between the completions holds**.
5. **Integrability forbids indefinite persistence.** The closed primitive system makes sustained extraction integrable (Theorem 14) and therefore cannot possess the working positive-flux rest indefinitely.

The five reasons form a trichotomy: **(1)–(3)** are short-time obstructions — the two $A_{\mathrm{act}}$ fields differ by $\kappa_AK-\gamma_UU$ at the same state, which is $O(1)$ at the working point's quasi-rest detritus level ($\approx0.535$) and at most $\kappa_AK=O(5)$ (at $U=0$), and trajectories of the two systems diverge on $O(1)$ timescales; **(5)** is the long-time obstruction — extraction on the closed ledger is $L^1$ in time (Theorem 14); **(4)** is neither — $\varepsilon_G$ is not a tracking error between the two fields at any timescale.

**Theorem (Non-reduction of the open working completion).** *There is no exact dynamic reduction, no regular perturbation, and no finite-time tracking correspondence from the closed primitive ledger (2) to the open working system, because (i) the targets differ by $\kappa_AK/\omega_A=5{,}000$ stock units (structural); (ii) the $A_{\mathrm{act}}$ fields differ by $O(1)$ at the working point (short-time); (iii) the working point is not a rest point of (2) (Theorem 12; equilibrium); (iv) $\varepsilon_G$ is not a tracking metric (diagnostic misuse); and (v) extraction on (2) is $L^1$ in time (Theorem 14; long-time).*

The mapping type for exact dynamic reduction is **rejected**. The permitted relation is analogy for shared mechanism language, plus diagnostic reconstruction of omitted mass flows. The companion's global periodic results are properties of its reduced systems and do not transfer to the closed primitive ledger; in particular, Hopf or periodic orbits of the frozen-donor working system are not properties of (2). In the other direction, the working system is an open projection: omitted turnover is routed to a diagnostic detritus or inert sink, imposed recharge corresponds to geological draw, and the reduced trajectory's mass discrepancy is reconstructible from the omitted flows.

**The frozen-donor limit is a corollary of the structural clause (i).** Rescaling the donor as $G=G_0g$ with $g(0)=1$ gives $\dot g=-G_0^{-1}(e_{GA}-e_{AG})$. The limit $G_0\to\infty$ freezes $g$ but does not restore the working completion's derived target: the limiting recharge field still uses $A_{\mathrm{eq,intrinsic}}$, not $A_{\mathrm{eq},W}$, so the scaling is **not** a regular perturbation of the working vector field. Local Hopf persistence of the working system under this primitive scaling is not claimed; a different derived-target completion would be required before a regular-perturbation theorem could be formulated.

**The long-time finite-budget interpretation.** With the donor $G(t)$ included as a state, the closed system is an autonomous retarded equation with a slow donor coordinate. The companion's $\tau_+\approx150$ yr upper cycle is a frozen-donor object; on the closed system it can persist only as a *transient* on the finite donor budget. The transient-duration statement is an order/budget bound, not an asymptotic estimate: under a sustained lower extraction flux $c>0$ the duration is bounded above by $G_0/c$.

The scale must name its flux. At the closed-block extraction rate $c=qE^*N^*\approx0.187$ stock units per year, the budget bound is $G_0/c\approx2\times10^{6}$ years; at the working completion's recharge flux $\mathcal B^*\approx4.652$ stock units per year, the draw scale is $G_0/\mathcal B^*\approx8.6\times10^{4}$ years. The "tens of thousands of years" heuristic uses the working flux (at $G_0/A_{\mathrm{act},*}=10^3$), and both scales sit far above the institutional delays of the companion family. Whether the frozen-donor local Hopf structure persists as a slowly drifting transient in the closed donor system is an **open slow-passage problem**; the mass budget alone does not establish it.

**The implication for industrial-ecology coupling** is concrete: a closed physical ledger and an open working system can share one diagnostic identity without sharing a dynamics, and the temptation to import one system's theorems into the other must be resisted.
# 10. What the ledger does not support — the section that says no, with proofs

> **In plain words.** Most papers end by listing what they did achieve. This one ends by listing what it refuses to license, and it proves the refusals. Two results matter here. First, no weighted average of components can certify that each component is safe — and this is shown to fail for *every* possible set of weights, by construction. Second, five bookkeeping rules make double counting impossible rather than unlikely.

## 10.1 Compensatory aggregation is rejected, not merely discouraged

On the unreduced ledger, **no scalar weighting of components is authorized by the accounting itself**. The precise statement is on the feasible balance domain (Definition 1): a weighted sum $\sum_m w_m s_m$ certifies componentwise adequacy $s_m\ge d_m$ for all $m$ on $\mathcal B(x,t)$ **only through an implication proved from the physical restrictions defining the domain** — and, in general, no such implication holds. The feasible domain can admit vectors with a positive aggregate and a negative component, exactly the geometry documented in the composite-indicator literature (Munda and Nardo, 2009). In short: a positive weighted sum never certifies componentwise non-negativity. Scalar summaries may rank and communicate; certification requires the vector.

**Proposition (No weighted certification).** *Let $\mathcal B(x,t)$ be the feasible balance domain (Definition 1). If $\mathcal B(x,t)$ contains a vector with $b_i<0$ and $w^{\top}b>0$ for a fixed $w\ge0$, then the certificate $\{w^{\top}b\ge0\}$ does not imply $b\ge0$; if $\mathcal B(x,t)$ is not known to exclude that pattern, no non-negative weighting is authorized as a componentwise certificate.*

*Proof.* On the exhibited vector the componentwise predicate fails ($b_i<0$) while the weighted predicate holds ($w^{\top}b>0$); the two predicates differ on $\mathcal B(x,t)$. The inverse-horizon score of §6.5.2 (Non-example 1) is the worked witness: a positive aggregate coexisting with componentwise deficits by construction. $\blacksquare$

The conditional form is not an accident of a particular domain. The compensating pattern is constructible against **any** weight, so the failure is universal to the method of weighted certification.

**Theorem (Universal failure of weighted certification).** *Let the ledger have $m\ge2$ components. For every weight vector $w\in\mathbb R^m_+$, $w\ne0$, there exist a typed ledger as in §2, a demand vector $d$, and an admissible state–operation pair $(x,u)$ with $u\in\mathcal U(x,t)$ whose attainable balance $b=O(x,u,\theta)-d$ satisfies $w^{\top}b\ge0$ while $b_m<0$ for some component $m$. No non-negative weighting is therefore a valid componentwise certificate in general.*

*Proof.* Take the two-compartment ledger with stock $x=(x_1,x_2)\in\mathbb R^2_+$, one donor-limited transfer flux $f=kx_1$ from compartment 1 to compartment 2 ($k>0$), identity readout $O(x,u,\theta)=x$, and demands $d=(d_1,d_2)$. Every non-negative state is admissible with the declared flux, because donor limitation holds ($f=0$ at $x_1=0$), so the balance $b=x-d$ is attainable for every $x\in\mathbb R^2_+$; the admissible operating set is the flux declaration itself. Fix $w$ and let $j$ be an index with $w_j>0$. If some $m\ne j$ has $w_m=0$, place the deficit there: choose $x_m<d_m$ and $x_j\ge d_j$, giving $w^{\top}b=w_j(x_j-d_j)\ge0$ while $b_m<0$. Otherwise $w_m>0$ for every $m\ne j$: choose any $m\ne j$ with $x_m<d_m$, and choose $x_j\ge d_j+\big(w_m(d_m-x_m)+\varepsilon\big)/w_j$ for any $\varepsilon>0$. Then

$$w^{\top}b=w_m(x_m-d_m)+w_j(x_j-d_j)\ \ge\ w_m(x_m-d_m)+w_m(d_m-x_m)+\varepsilon=\varepsilon\ \ge\ 0,$$

while $b_m=x_m-d_m<0$. The pair $(x,d)$ is the witness for $w$. $\blacksquare$

The construction **never uses the dynamics**: the failure is a property of non-negative weightings over mixed-sign balances, not of the donor-limited positivity mechanism. Consequently, on any feasible balance domain containing a compensating pair — and Definition 1's domain is exactly that whenever the operating set admits states with mixed balances — no non-negative weighting can stand in for the conjunctive criterion of §3.2. The reading is the algebraic form of the weak-comparability thesis stated in §1.1.

The companion assessment analysis (Author, F., et al., *in review*) proves the *dynamic* form of the same separation for transition operators; the ledger side contributes the *static prerequisite*: the aggregation question is only well posed after the balance domain is declared, and the burden of proof sits on the aggregation, not on the componentwise report.

The same separation holds at the service layer: a weighted sum on $\mathcal B(x,t)$ cannot see the directional support gap $(1-\alpha_{\mathrm{reg}})\bar s$ of Definition 2 — an aggregate that mixes regenerative and non-regenerative provenance never reports which component carries the gap.

In the terms of the ecological-economics literature of §1.1: componentwise adequacy on the typed ledger is **strong sustainability as a conjunctive predicate**; a positive weighted sum is **weak sustainability as a ranking device**. The ledger authorizes the first and does not authorize the second.

## 10.2 The double-counting discipline

Five rules, each carried by a proved or defined statement of this article, jointly prevent double counting and phantom mass.

1. **One balance per moiety.** Conservation laws attach to declared moieties (Theorems 7–8). Adding unlike units — biomass, money, biodiversity indices, exergy — into one conserved scalar is not authorized by any conservation theorem.
2. **Explicit stoichiometry.** Entries are added within an incidence row only when their types and units agree; every conversion is an explicit coefficient in $S^{\top}$, never an implicit sum (§2.1).
3. **Yield routing.** A transformation represented with yield below one must route the omitted fraction to a represented compartment or a declared boundary flow; otherwise the moiety balance holds only after silently dropping the moiety (Theorem 15).
4. **No ghost sinks.** Every primitive with an outflow from some compartment must have its routed inflow represented, and every inflow its source — opposite-sign incidence of the same primitive is checkable column by column. The six-state cancellation of §4.9 shows the check passing, while the same template shows that cancellation without donor-limited admissibility establishes nothing.
5. **Classification labels stay out of the columns.** Reserve-life and resource-threshold quantities answer different questions and share a column only under an explicit convention label (§6.5.3); diagnostic labels never determine material routing (§2.5).

Every unit of mass is routed once: the unit-sum split routing of Theorem 8 and the column-sum-zero incidence of Theorem 9 are the mechanism, and the yield-routing obligation of Theorem 15 is its enforcement. A flux omitted from the ledger is not thereby conserved. A recovery claimed in a quality-neutral loop is not thereby real. A diagnostic index that mixes basins and reserves (the ranking device of §6.5.2) is identified as such in the text that reports it. **Double counting is a representation error, and the representation that prevents it is the contribution.**

## 10.3 Negative and boundary content is first-class

The classification results of §6.5 are negative results stated as such: the anomaly index is not a stock ratio; the reserve-life ratio is not a forecast; the removals-only time is not a depletion diagnostic. The non-reduction boundary of §9 is a rejected mapping with five mathematical reasons. The sink obstructions of §2.4 are empty-kernel mechanisms.

None of these is a failure of the framework. A quantity that answers exactly one question, stated with that question, **is** the framework working — and the framework's claim about itself is limited to the accounting layer it establishes.

## 10.4 Limitations

These are stated as limitations of what follows, not as future work.

1. **(i)** The two-pool exact specialization of the groundwater template remains **open**. The admitted object is the one-pool affine approximation, and **no two-pool model is claimed as established** (§8.2).
2. **(ii)** The phosphorus and groundwater rows are **registered template obligations**: no constitutive content exists behind their identification ladders.
3. **(iii)** The first-passage propositions of §7 concern **declared stochastic surrogates, not the ledger**: they do not compute the ledger's hitting time, do not conserve its mass, and carry the record-relative-barrier and non-claim disciplines.
4. **(iv)** The applied records of §6.5 are classified diagnostics at their stated evidentiary levels — statistical index, arithmetic ratio, removals-only pressure scale — and **none is a calibrated early-warning system or a forecast**.
5. **(v)** The non-reduction boundary of §9 is **permanent mathematics, not a gap**: the closed primitive ledger and the open working system are different completions.
6. **(vi)** The conditional hybrid balance of Theorem 15 stays **conditional**, with its jump-interpretation and yield-routing obligations open per application.
7. **(vii)** The support-saturation limits of §2.6 are **local and finite-time**; neither is a full-system reduction.
8. **(viii)** The article asserts **nothing empirical** about any named resource system beyond the classifications of public data products stated at their source status.

---

# 11. Conclusion

The two failure modes of the introduction — compensatory aggregation and classification drift — are **representation errors**, and the representation that prevents them is the article's content.

Conservation is proved from the incidence structure, not assumed. Positivity is proved from donor limitation, not asserted. Services are readouts, not mass. And depletion time is three quantities, not one.

The closed finite-donor ledger carries its complete theorem set — the natural-block mass identity, orthant invariance, no interior rest at positive effort, the vanishing-extraction rest set (extinction, carrying capacity, and the frozen-biomass face), extraction integrability — and the non-reduction boundary records, with reasons, why the closed ledger and the open working systems of institutional dynamics are **different completions sharing one exact object**.

The depletion numbers of the applied record answer, each, exactly the question their construction poses: a statistical index of record-relative stress, an arithmetic ratio of an economic classification, a pressure scale of one gross loss rate. Stating them with those questions — against the published critiques they corroborate — is what makes them usable. Collapsing them into one "time to depletion" is what makes them false.

The article likewise locates substitution **within** the ledger rather than alongside it. The weak and strong regimes of §1.1 are two readings of one typed stock–flow ledger, distinguished by whether the material cycle closes at the rate of use; that reading is developed once, in the introduction, and is not re-argued here. They are not rival doctrines. The vector reading is the one that carries the certificate; the scalar $b\cdot M$ check of §1.1 is the operational reading on top of it. A substitute is either a recycled flux returned to the regenerating pool, or a non-renewable drawdown on a second compartment — different ledger entries with different statuses.

An exhaustion-horizon estimate built on a reserve figure carries the substitution and technology premises of the reserve classification, not a physical forecast. For ecological-economics measurement, that is the closing statement: not rival doctrines but two readings of one ledger — and the vector reading is what carries the certificate.

---

## Supplementary material

The accompanying file `paper3_supplementary_v8.md` carries: the ten-state admissibility template and its three audited negative witnesses (the non-donor-limited geological exchange, the variance-closure failure, the undefined output functional); the registered identification ladders of the phosphorus and groundwater templates at full detail; the split-assignment mechanism table; the statement inventory with the status of every statement in the main text (theorem with displayed proof, conditional theorem, definition, application record, or boundary statement) — read with the S6 statement-status naming offset, which maps the supplementary's status words to the main text's current labels; and the fisheries cohort record with the archived-pull verification and the executed broad-cohort comparison (S5).

## Declarations

**Data availability.** All computations underlying §6.5 are descriptive arithmetic on the cited public data products: the G3P groundwater anomaly product v1.12 (Güntner et al., 2024; GFZ Data Services, doi:10.5880/G3P.2024.001), the U.S. Geological Survey *Mineral Commodity Summaries* 2026 (the January 2026 release), and the RAM Legacy Stock Assessment Database (Ricard et al., 2012; the cohort pull date is archived in the analysis repository). The parameter tables of §2 are declared parameterizations. No other data were used.

**Declaration of competing interest.** None.

**AI declaration.** GLM (Z.ai), Qwen (AlibabaCloud) and DeepSeek AI assisted with drafting and iterative review.
# References — carried unchanged

> A reference list is not prose, so nothing here is rewritten. The block below is the source's own list, reflowed from the PDF text layer with hyphenation repaired and **no entry added, dropped, or re-ordered**. Precise per-entry segmentation is deliberately deferred to the LaTeX assembly step (a `\bibitem` list or a `.bib` file must be generated from the source file, not from a flattened PDF), which is why the list is presented unsegmented. Head-like entry starts counted in the flattened text: **28**; `doi.org` links: **7** (listed below so any loss is visible).

## The list as it stands in the source

Abaee, A., 2026. Delay-induced regime change in harvested stocks: the mobilising and protective channels of institutional feedback, and the review interval as control. Zenodo. https://doi.org/10.5281/zenodo.22554217. Companion delay-dynamics study. Abaee, A., 2026. Periodic review as sampled governance: sample-and-hold dynamics of assessment-driven effort control, a selected 42-stock spectral screen, and the Northern Cod case. Zenodo. https://doi.org/10.5281/zenodo.22554297. Companion review-screen study. Abaee, A., 2026. The limits of compensatory aggregation: a formal separation of weak and strong sustainability assessment. Zenodo. https://doi.org/10.5281/zenodo.22545740. Companion assessment-separation study. Aubin, J.-P., 1991. Viability Theory. Birkhäuser, Boston. Blomqvist, L., Brook, B.W., Ellis, E.C., Kareiva, P.M., Nordhaus, T., Shellenberger, M., 2013. Does the shoe fit? Real versus imagined ecological footprints. PLoS Biology 11, e1001700. https://doi.org/10.1371/journal.pbio.1001700 Brunner, P.H., Rechberger, H., 2004. Practical Handbook of Material Flow Analysis. Lewis Publishers, Boca Raton. Chhikara, R.S., Folks, J.L., 1989. The Inverse Gaussian Distribution: Theory, Methodology, and Applications. Marcel Dekker, New York. 38 Daly, H.E., 1990. Towardsomeoperationalprinciplesofsustainabledevelopment. Ecological Economics 2, 1–6. Clark, C.W., 1990. Mathematical Bioeconomics: The Optimal Management of Renewable Resources, 2nd ed. Wiley, New York. Ekins, P., Simon, S., Deutsch, L., Folke, C., De Groot, R., 2003. A framework for the practical application of the concepts of critical natural capital and strong sustainability. Ecological Economics 44, 165–185. Eurostat, 2001. Economy-wide Material Flow Accounts and Derived Indicators: A Methodological Guide. Eurostat, Luxembourg. Feinberg, M., 2019. Foundations of Chemical Reaction Network Theory. Springer, Cham. Fischer-Kowalski, M., Krausmann, F., Giljum, S., Lutter, S., Mayer, A., Bringezu, S., Moriguchi, Y., Schütz, H., Schandl, H., Weisz, H., 2011. Methodology and indicators of economy-wide material flow accounting: state of the art and reliability across sources. Journal of Industrial Ecology 15, 855–876. Güntner, A., Sharifi, E., Haas, J., et al., 2024. Global Gravity-based Groundwater Product (G3P), V. 1.12. GFZ Data Services. https://doi.org/10.5880/G3P.2024.001 Illakwahhi, D.T., Vegi, M.R., Srivastava, B.B.L., 2024. Phosphorus’ future insecurity, the horrorofdepletion, andsustainabilitymeasures. InternationalJournalofEnvironmentalScience and Technology 21, 9265–9280. https://doi.org/10.1007/s13762-024-05664-y Jacquez, J.A., Simon, C.P., 1993. Qualitative theory of compartmental systems. SIAM Review 35, 43–79. Lin, D., Hanscom, L., Murthy, A., Galli, A., Evans, M., Neill, E., Mancini, M.S., Martindill, J., Medouar, F.-Z., Huang, S., Wackernagel, M., 2018. Ecological footprint accounting for countries: Updates and results of the National Footprint Accounts, 2012–2018. Resources 7, 58. https://doi.org/10.3390/resources7030058 Martinez-Alier, J., Munda, G., O’Neill, J., 1998. Weak comparability of values as a foundation for ecological economics. Ecological Economics 26, 277–286. Meadows, D.H., Meadows, D.L., Randers, J., Behrens III, W.W., 1972. The Limits to Growth. Universe Books, New York. Munda, G., Nardo, M., 2009. Noncompensatory/nonlinear composite indicators for ranking countries: a defensible setting. Applied Economics 41, 1513–1523. Neumayer, E., 2013. Weak versus Strong Sustainability: Exploring the Limits of Two Opposing Paradigms, 4th ed. Edward Elgar, Cheltenham. Øksendal, B., 2003. Stochastic Differential Equations: An Introduction with Applications, 6th ed. Springer, Berlin. Redner, S., 2001. A Guide to First-Passage Processes. Cambridge University Press, Cambridge. Ricard, D., Minto, C., Jensen, O.P., Baum, J.K., 2012. Examining the knowledge base and status of commercially exploited marine species with the RAM Legacy Stock Assessment Database. Fish and Fisheries 13, 380–398. Tapley, B.D., Bettadpur, S., Ries, J.C., Thompson, P.F., Watkins, M.M., 2004. GRACE measurements of mass variability in the Earth system. Science 305, 503–505. Tilton, J.E., 2003. On Borrowed Time? Assessing the Threat of Mineral Depletion. Resources for the Future, Washington, DC. Tilton, J.E., Lagos, G., 2007. Assessing the long-run availability of copper. Resources Policy 32, 19–23. U.S. Geological Survey, 2026. Mineral Commodity Summaries 2026: Phosphate Rock. USGS, Reston, VA. https://www.usgs.gov/centers/national-minerals-informationcenter/mineral-commodity-summaries Wackernagel, M., Beyers, B., 2019. EcologicalFootprint: ManagingourBiocapacityBudget. New Society Publishers, Gabriola Island, BC. 39

## DOI links present in the source list

- https://doi.org/10.1007/s13762-024-05664-y
- https://doi.org/10.1371/journal.pbio.1001700
- https://doi.org/10.3390/resources7030058
- https://doi.org/10.5281/zenodo.22545740.
- https://doi.org/10.5281/zenodo.22554217.
- https://doi.org/10.5281/zenodo.22554297.
- https://doi.org/10.5880/G3P.2024.001

## Two open items the author must settle before submission

1. The in-text placeholders **"Author, D., et al., in review"** (§2.2, twice; §9, once), **"Author, E., et al., in review"** (§6.5.2) and **"Author, F., et al., in review"** (§10.1) — five mentions naming three works — are *kept as the author wrote them*. The reference list already carries three Abaee (2026) Zenodo records (22554217 delay-dynamics; 22554297 review-screen; 22545740 assessment-separation), which is very likely the intended mapping, but substituting it is the author's decision, not the humanizer's.
2. The AI declaration names GLM (Z.ai), Qwen (AlibabaCloud) and DeepSeek AI. It is reproduced verbatim; if a target journal requires a different disclosure form, that is a submission step, not a prose step.

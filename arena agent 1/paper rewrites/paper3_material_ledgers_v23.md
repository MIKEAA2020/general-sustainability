# Typed Flux Ledgers and Depletion Arithmetic: Conservation, Componentwise Diagnostics, and the Semantics of Depletion Horizons

## Abstract

Depletion numbers circulate under one label while answering different questions. Reserve-life ratios, trend-persistence indices, and removals-only pressure scales are read as "time to depletion" despite measuring different things; compensatory aggregation hides a deficit behind a positive scalar.

We separate them with a typed stock–flow accounting layer — a per-moiety ledger that keeps conservation laws typed, so biomass, money, and biodiversity are not summed into one scalar. Conservation follows from the incidence structure of the compartment–flux network; positivity from donor limitation (each primitive outflow vanishes when its donor is empty); services are readouts, not conserved mass.

Three certification layers carry a flux-reconstruction identity (an algebraic relation reconstructing unobserved internal fluxes from observed stock changes), a conservation-law reduction, and a flux-bounding envelope theorem. The closed finite-donor ledger satisfies the natural-block mass identity, orthant invariance (state stays nonnegative), no interior rest at positive effort, the vanishing-extraction rest set, and extraction integrability. Depletion time separates into three non-interchangeable quantities — gross turnover intensity, a frozen-rate ratio, and a scenario-conditioned hitting time — with uniform-drift bounds. Three public-data applications are classified: G3P anomaly index is a statistical index, not a stock ratio; phosphate reserve-life ratio is arithmetic, not a forecast; fisheries removals-only time is a pressure scale, not a depletion diagnostic. No nonnegative weighting certifies componentwise nonnegativity, and five double-counting rules block phantom mass. First-passage semantics on declared stochastic surrogates — stochastic passage times against a relative barrier — carry explicit non-claims. Weak and strong sustainability are two regimes of one system, distinguished by whether the material cycle closes at the rate of use.

Each depletion claim carries the predicate it actually establishes, with an interface contract fixing the shared object with delay-based institutional dynamics.

**Keywords:** material flow accounting; stock–flow ledger; depletion indicators; first-passage time; conservation laws; composite indicators; reserve life

---

## 1. Introduction

### 1.1 Failure modes and the two confusions

Sustainability accounting fails in two characteristic ways. The first is *compensatory aggregation*: heterogeneous physical stocks and service flows are summarized by scalar indices whose cross-component trades are never declared as mathematics, so a severe deficit in one component can coexist with a positive aggregate. The composite-indicator and weak-versus-strong-sustainability literatures document the failure and its noncompensatory remedies (Munda and Nardo, 2009; Ekins et al., 2003; Neumayer, 2013). The second is *classification drift*: quantities with the units of time — reserve-life ratios, trend-persistence indices, removals-only pressure scales — circulate as if they were one thing, "time to depletion," when they answer different questions under different assumptions.

The drift is concrete. A reserve-life ratio divides a reserve figure by a production figure and calls the quotient a horizon. A groundwater anomaly index fits a trend to a satellite product and reports the fitted distance to the series' own minimum divided by the fitted rate. The result is a number in units of years that is not a time to any physical event. A fisheries pressure indicator divides a log biomass margin by a fishing mortality and presents the result as a time scale. Each of these quantities is informative about something. None is what it is typically taken to be.

The first failure mode has a public flagship object. Earth Overshoot Day aggregates component flows into a single calendar date, so a severe deficit in one component can coexist with a date that still falls late in the year (Lin et al., 2018; Wackernagel and Beyers, 2019; Blomqvist et al., 2013). The systems-dynamics overshoot models raise the same aggregation question in dynamic form (Meadows et al., 1972). The replacements built in this article are component-resolved by construction: the per-asset, per-pool depletion horizons of Section 6.5.2 are each reported beside the pool it draws on and never summed into a scalar date.

A further failure mode is what we call the *productivity illusion*: the appearance that a system is delivering adequately while the base that sustains the delivery is being reduced. It has two senses, and they are distinct. The first is arithmetic and is the compensatory-aggregation failure above — a deficit in one component offset by a surplus in another, so that a positive aggregate reads as adequate. This article formalises this sense as the aggregation obstruction of Section 10.1.

The second sense is dynamical and is yield inflation. A measured yield can exceed the true sustainable yield when it is maintained by drawing down the supporting pool — groundwater, soil carbon, bioavailable nutrients — rather than by that pool's regeneration. The resource appears productive while what sustains it is liquidated silently. The supporting pool need not be a superficially non-renewable reserve for this diagnosis to run, and it can be read in more than one way at once — as natural capital, as a stock, or as a slowly regenerating flow of services. These are overlapping readings of the same pool, not mutually exclusive ones. Every such pool is regenerative on some timescale — a crop within a season, an aquifer within years to decades, a mineral deposit over geological time — and the failure is the same in each case. What decides is the renewal rate of the pool relative to the rate of use. A use that falls on the pool's regeneration is sustained. One that falls on the pool itself is liquidation. A drawdown is recoverable only insofar as the pool regenerates faster than it is taken; if a pool regenerates too slowly for the rate at which it is taken, drawdown is still liquidation. The size of the pool is a property of the resource. Whether that drawdown is recoverable is a property of the rate.

The two-pool architecture of this article exists to detect exactly this yield-inflation sense. The applied tables of Section 6.5.2 report each resource beside its supporting pools, so a stock's apparent adequacy cannot hide the silent liquidation of what sustains it. The temporal asymmetry that makes the yield-inflation sense dangerous has a mechanical picture. An elevator rated for ten people will hold fourteen for a long time: the cable does not part on the fourteenth passenger but only after the accumulated wear it never shows. During the overshoot nothing announces the damage — the wear is diffuse, gradual, and invisible to everyone riding the car — while the snap, when it comes, is sudden and total. The yield-inflation sense of the productivity illusion is the wear phase. Measured yield stays up because the supporting pool is being drawn down, and nothing in the yield series records the drawdown. The two-pool tables of Section 6.5.2 report each resource beside its supporting pool for exactly this reason: to make the wear measurable while the cable still holds, not to predict the snap (Section 7 states what the passage-time results do and do not condition on).

The classification-drift failure is well documented on the data side. Reserve-life ratios are arithmetic: remaining reserves divided by current production. Because reserves are an economic classification that changes with prices, technology, exploration, and regulation — not a fixed physical stock — the ratio is not an exhaustion forecast. The critique has been made forcefully for phosphate. Illakwahhi, Vegi, and Srivastava (2024) show that the influential "depletion within a century" estimates rest on single-source USGS data whose credibility is questionable, ignore recovery and recycling, and that timeframes estimated from inadequate reserve data "are somewhat misleading." The same point is standard in mineral economics, where the distinction between reserves and resources has been central at least since Tilton (2003). The United States' phosphate reserves have remained near one million kilotons for decades while cumulative production since 1996 is of order six hundred thousand kilotons. The classification replenishes itself, and a ratio built on it inherits that behaviour. For copper, Tilton and Lagos (2007) document reserves growing through a century of rising production — the same replenishment under the same classification.

The same conflation pervades accounting itself. Material flow analysis supplies the bookkeeping of society's material throughput (Brunner and Rechberger, 2004; Eurostat, 2001; Fischer-Kowalski et al., 2011). Its incidence structure is shared with reaction-network theory, where the sign pattern of the stoichiometric matrix is a conservation object (Feinberg, 2019). But bookkeeping balance, stoichiometric conservation, thermodynamic admissibility, and sustainability safety are four different predicates, and the literature routinely slides between them. A mass-balanced ledger can be chemically impossible. A chemically consistent ledger can violate every declared barrier. A ledger satisfying all declared barriers can fail conservation. Separating these layers and proving their relationships, so that each claim about a material system carries the predicate it actually establishes, is this article's first task (Section 3).

The second task is noncompensation. The weak-comparability thesis of ecological economics holds that values relevant to environmental decisions may not be commensurable in a single metric (Martinez-Alier, Munda, and O'Neill, 1998). At the level of material accounting this thesis has a precise algebraic form, which Section 10.1 states: no nonnegative weighting of component balances certifies that every component satisfies its floor. A positive weighted sum never certifies componentwise nonnegativity. Scalar summaries may rank and communicate; certification requires the vector.

The third task is to locate substitution within the ledger, rather than alongside it. Weak and strong sustainability are not competing hypotheses but two regimes of one dynamic system, distinguished not by whether substitution alone keeps pace with depletion but by whether the material cycle can be closed at the rate of use. Weak sustainability is the idealized regime: humans consume and populate slowly enough that technological substitution and natural regeneration together redistribute matter so that it is used as it arises. On human-relevant timescales substitution is the dominant term; natural regeneration acts far more slowly — often on deep-time scales — and is included for physical completeness rather than as a co-equal mechanism (Daly, 1990). In this idealized closure the byproducts of use — carbon drawn from the atmosphere, chemical substances released to air, water, and soil — are returned to use in time and are therefore not waste. Waste is a relational status, not an intrinsic property of any material. It is the matter that, under the present relation and circumstances, accumulates because it cannot be put to immediate use for lack of knowledge, technology, or timely redistribution. So a chemical substance that is a product in one context is waste-in-waiting in another, and no substance is waste by its nature.

Strong sustainability is the regime in which that closure fails — either because no identified physical pathway re-routes the extracted matter, or because depletion outruns the rate at which such a pathway could be deployed (Neumayer, 2013; Ekins et al., 2003). Substitution is admissible only where an identified physical pathway exists and does not draw down a different critical stock. No substitute is admitted merely because an aggregate production function or a weighted index permits it. In ledger terms, a substitute is either a recycled or recovered flux returned to the regenerating pool, or a non-renewable drawdown on a second compartment. The two are different ledger entries and carry different statuses (Section 2.3, Section 6).

The two regimes correspond to two readings of the same object. The scalar reading $B = b\cdot M$ against consumption is the weak-sustainability flow check: does the cycle close in aggregate? The multi-compartment ledger is the vector reading: does it close only by drawing down a critical compartment or by over-filling the waste compartment — that is, are local depletions or waste accumulation merely being pushed off-book? Both readings are required, and neither demotes stocks. The ledger keeps the stock compartments first-class and supplies the thresholds, hitting times, and sink constraints from which $B$ is derived. The scalar reading is the operational overshoot test on top of it. Both readings are instantaneous; a single-period check has no view of what must also hold over time, namely that the checks do not drift into overshoot. The balance must be maintained as neither consumption nor population grows faster than the productivity that supports them, and the drawdown must not be recoverable only on a timescale longer than it is taken. A static $C \le B$ can be re-satisfied on a path that is already committed to failure. The scenario-conditioned hitting time of Section 6.5.2 exists to give the drift a horizon. The balance is a rate condition, and it also has to hold as a growth condition: a $C \le B$ satisfied at each instant does not by itself rule out the path on which consumption or population grows faster than the regeneration and substitution available — the same no-drift requirement. The reserve classification itself encodes this. Reserves change with prices, technology, exploration, and regulation, so a horizontal exhaustion estimate built on a reserve figure carries the substitution and technology premises of the classification, not a physical forecast.

This article builds the accounting layer that resists these failures. Its objects are typed ledgers in which conservation follows from the incidence structure, positivity follows from donor limitation, services are readouts rather than conserved mass, and each depletion quantity carries its own classification, stated at its actual strength.

### 1.2 Contributions

1. **A typed primitive-flux ledger.** Compartments carry a material identity, a boundary, and a unit. Non-negative primitive fluxes connect them through a signed incidence matrix (the compartment–flux bookkeeping of material flow analysis: Brunner and Rechberger, 2004; Fischer-Kowalski et al., 2011; the incidence formalism of reaction-network theory: Feinberg, 2019). Conversions between types appear only as explicit stoichiometric coefficients. Every one-way transfer is donor-limited.

2. **Three certification layers, separated and proved.** Accounting consistency (the balance law holds), conservation consistency (declared moieties are invariant up to boundary flows), and barrier safety (declared lower and upper barriers hold) are distinct predicates with distinct proof obligations. The flux-reconstruction identity, the conservation-law reduction, and a flux-bounding envelope theorem — with a barrier certificate corollary — are proved in full (Section 3).

3. **The closed finite-donor theorem set.** For the closed ledger in which the geological donor is a state and no derived target appears: the natural-block mass identity, orthant invariance, absence of any interior rest point at positive effort, the vanishing-extraction rest set (extinction, carrying capacity, and the frozen-biomass face), and integrability of extraction on the finite donor budget (Section 4). Positivity is proved face by face via the tangent cone (Aubin, 1991). The classical compartmental-systems nonnegativity theory (Jacquez and Simon, 1993) is the lineage.

4. **Depletion arithmetic.** Depletion time is separated into three non-interchangeable quantities — gross turnover intensity, a frozen-rate ratio, and a scenario-conditioned hitting time — extended to upper barriers, infimum exit times, and infinite-horizon maintainability, with uniform-drift bounds proved and the failure of "positive extraction implies finite exhaustion" exhibited by counterexample (Sections 6.1–6.5).

5. **Application classifications at exact status.** The G3P anomaly-persistence index, the phosphate reserve-life ratio, and the fisheries removals-only pressure time are classified as what they are — statistical index, arithmetic ratio, pressure scale — against the published critiques they corroborate (Section 6.5).

6. **First-passage semantics on declared surrogates.** The inverse-Gaussian groundwater passage and the geometric-Brownian fisheries passage are stated with complete derivations, the record-relative-barrier discipline, and seven explicit non-claims separating them from the ledger (Section 7).

7. **The interface with institutional dynamics.** The exact shared object with delay-based institutional models is the single-resource deficit identity $qEN - R = -\dot N$. The boundary is the non-reduction theorem: no exact dynamic reduction from the closed ledger to the open working system, for five stated mathematical reasons (Section 9).

**What is not claimed.** The article is equally explicit about what it does not establish. No stochastic completion of the ledger is claimed: the surrogate processes of Section 7 do not conserve the ledger's mass and are not perturbations of its dynamics. No thermodynamic admissibility is claimed. No identification of the two-pool groundwater hypothesis is claimed (its identification requirements are registered in Section 8, not discharged). And no empirical finding about any basin, aquifer, or fishery is claimed beyond the descriptive status of the tabulated indicators.

### 1.3 Organization

Section 2 defines the typed ledger. Section 3 develops the certification layers and the accounting theorems. Section 4 proves the closed-ledger theorem set. Section 5 adds the service layer and the componentwise deficit. Section 6 develops the depletion taxonomy, the uniform-drift bounds, and the application classifications. Section 7 supplies first-passage semantics. Section 8 records the domain templates at registered status. Section 9 fixes the interface with delay dynamics. Section 10 states what the ledger does not support, and Section 11 concludes.

---

## 2. The Typed Primitive Ledger

### 2.1 Typed stocks, primitive fluxes, and the incidence discipline

Material flow accounting begins with a small set of distinctions. Heterogeneous substances must be tracked separately. Spatial and functional locations must be distinguished. Conversions between chemical forms must be made explicit. This section sets out the four concepts that the typed ledger keeps apart, and the incidence discipline that makes conservation a property of the structure rather than an assumption.

The ledger separates four concepts that accounting practice often merges. A *moiety* is a conserved substance class (an element, or a declared conserved combination) — the only object to which a conservation law attaches. A *species* is a chemical or biological form of a moiety. A *compartment* is a spatial or functional location holding a stock. A *stock* is a compartment's current amount of a species, with a physical unit. "Carbon in the atmosphere" is a location-specific stock, not a moiety: carbon is the moiety, and the atmosphere is a compartment. Conservation laws are stated per moiety; nothing is conserved merely by being a compartment.

A ledger state $x \in \mathbb{R}^m_+$ collects compartments, each entry carrying a material identity, spatial support, and physical unit. Internal dynamics use non-negative primitive fluxes:
$$\dot x = S_{\mathcal{T}} v(x, y, \theta) + B_{\mathcal{T}} u_{\partial}(t) + d_x(t), \qquad v \ge 0, \tag{1}$$
where $S_{\mathcal{T}}$ is the typed stoichiometric (incidence) operator, $y$ collects the declared boundary states — environmental or companion variables external to the ledger — $\theta$ the declared constitutive parameter vector, $B_{\mathcal{T}} u_{\partial}$ collects declared boundary transfers, and $d_x$ belongs to a stated disturbance class. Entries are added within a row only when their types and units agree; a conversion between types is represented by an explicit stoichiometric coefficient, never by an implicit sum. If $L^\top S_{\mathcal{T}} = 0$, then
$$\frac{d}{dt}(L^\top x) = L^\top B_{\mathcal{T}} u_{\partial} + L^\top d_x,$$
one conservation law per conserved moiety and boundary; the identity does not create a scalar sustainability mass across incommensurable systems. Three clarifications are part of the statement. First, $d_x$ must itself be typed: a physical disturbance on represented material is a different object from a structural discrepancy term. Second, $S_{\mathcal{T}}$ may contain signed entries even though $v \ge 0$: the sign pattern of the incidence matrix and the nonnegativity of the primitives are separate declarations. Third, forward invariance is a separate requirement: every primitive outflow must vanish or be limited when its donor compartment is empty, and a target-relaxation flux from a finite donor is admissible only after donor limitation is made explicit.

### 2.2 The closed finite-donor ledger

The closed ledger of this article is the finite-donor primitive system. Let
$$x_L = (N, A^{\mathrm{act}}, A^{\mathrm{geo}}, U), \qquad s = \frac{A^{\mathrm{act}}}{A^{\mathrm{act}} + A_0}, \qquad \sigma = \frac{A^{\mathrm{geo}}}{A^{\mathrm{geo}} + A_{g0}},$$
with $N$ the living stock, $A^{\mathrm{act}}$ the active abiotic pool, $A^{\mathrm{geo}}$ the geological donor, and $U$ the detritus compartment. Net regeneration and gross uptake are the constitutive laws
$$R(N, A^{\mathrm{act}}) = rN\left(1 - \frac{N}{K}\right)s, \qquad T = \kappa_A N s, \qquad B = R + T,$$
and the four primitives involving the donor are
$$e_{GA} = \omega_A A^{\mathrm{eq,intrinsic}} \sigma, \qquad e_{AG} = \omega_A A^{\mathrm{act}}, \qquad C^{A,\mathrm{lim}} = C^A \sigma, \qquad \gamma_U U \ \text{(detritus return)}.$$

These donor primitives instantiate one of three recharge laws that appear across this article and the companion analyses (each under review); the three are distinct objects, tabulated once so that none is silently substituted for another:

| Recharge law | Form | Status |
|---|---|---|
| Primitive donor-limited exchange | $e_{GA} = \omega_A A^{\mathrm{eq,intrinsic}} \sigma$ | The closed block's law (Section 2.2): the forward rate depends on the donor alone, not on how empty the receiving pool is — linear donor-limited exchange, whose rest is $A^{\mathrm{act}} = A^{\mathrm{eq,intrinsic}}\sigma$ (Theorem 13). |
| Target-relaxation | $\omega_A(A^{\mathrm{eq}} - A)$ | Banned unless donor-limited (Section 4.4): runs backward at an empty donor; admissible only with the source declared an effectively infinite external reservoir, making the system open. |
| Working derived target | $A^{\mathrm{eq,W}} = A^{\mathrm{eq,intrinsic}} + \kappa_A K/\omega_A$ | The delay-dynamics analysis's working completion (that analysis, Section 9): not a closed-block law, and the reason the two systems do not reduce. |

In the closed block no derived target appears. Recharge is donor-limited and cannot run backward ($e_{GA} = 0$ at $A^{\mathrm{geo}} = 0$; the positive-part convention $[\cdot]_+$, read as a one-way valve at a nonpositive target, never binds here because the registered intrinsic target is positive), and mining $C^{A,\mathrm{lim}}$ is donor-limited the same way extraction is. With $A_{g0} > 0$ the donor fraction $\sigma$ is smooth and strictly increasing in the donor level.

Under the institutional-failure specialization ($\mu = \nu = \rho = 0$, $C^A = 0$) the closed natural block is
$$\begin{aligned}
\dot N &= R - qEN, \\
\dot A^{\mathrm{act}} &= -B + e_{GA} - e_{AG} + \gamma_U U, \\
\dot A^{\mathrm{geo}} &= -e_{GA} + e_{AG}, \\
\dot U &= T - \gamma_U U,
\end{aligned} \tag{2}$$
together with a memory–effort pair $(Z, E)$ driven by $qEN - R$ (never by mining). The pair is the registered object of the companion delay-dynamics analysis (under review; eq. (1) and Section 2.4 of that analysis) and is not analysed in this article. Net regeneration is the difference of two non-negative primitives — gross regeneration $rNs$ (support $\to$ stock) and density-dependent return $rN^2 s/K$ (stock $\to$ support) — so (2) stays within the primitive-flux discipline of Section 2.1 despite the signed entry. The block's harvest routing is the $\alpha = 0$ corner of Section 2.3: harvest $qEN$ exits the natural block entirely as product, and a positive detritus-routed fraction $\alpha > 0$ would add $\alpha qEN$ to $\dot U$ and reduce the block export to $(1-\alpha)qEN$; the mass identity of Theorem 7 is stated for the declared routing. The registered parameterization is $r = 0.02$, $K = 100$, $q = 0.001$, $\kappa_A = 0.05$, $\omega_A = 10^{-3}$, $A_0 = 1$, $A^{\mathrm{eq,intrinsic}} = 50$, $\gamma_U = 0.2$; the geological half-saturation $A_{g0}$ is declared positive (smoothness of the donor fraction $\sigma$) under the separation-of-scale condition $A^{\mathrm{geo}} \gg A_{g0}$, in which regime $\sigma \approx 1$; the scale separation is registered rather than a numerical value, and the $A_{g0} = 0$ corner is the discontinuous-perturbation limit, not the registered regime. With $A_0 > 0$ and $A_{g0} > 0$ the right-hand side of (2) is locally Lipschitz on the closed orthant, and the comparison $\dot N \le rN(1 - N/K)$ (with $\dot N \le 0$ once $N \ge K$) bounds the stock by $\max\{N(0), K\}$. Classical solutions therefore exist globally and stay in the orthant by Theorem 10 — the existence clause behind every 'classical solution' statement below.

When product, waste, and the inert sink are restored with the same donor-limited routing, the full ledger $N + A^{\mathrm{act}} + A^{\mathrm{geo}} + U + P + W + I$ is closed (Section 4.2). The geological donor is an internal state throughout — no infinite reservoir is declared — and the block boundary is crossed only by harvest (to product) and, when restored, mining (to product or waste). The full seven-compartment incidence is the nested completion of the four-block routing. Uptake $T = \kappa_A N s$ never enters $\dot N$: it is an $A^{\mathrm{act}} \to U$ throughput with the living stock entering as a catalytic factor, not stored biomass — legitimate in a monomaterial projection; the masses below are defined on this routing.

### 2.3 The six-compartment illustration

For one conserved limiting material, the accounting scaffold is instantiated by six compartments — living biomass $X$, detritus or recoverable residual $U$, active abiotic pool $A$, geological or slowly available pool $G$, product or in-use stock $P$, and absorbing or currently unavailable stock $W$ — with eight non-negative primitive fluxes: assimilation $g(X,A)$, mortality $m(X)$, harvest $h(X,E)$, decomposition $d_U(U)$, geological-to-active transfer $e_{GA}(G,A)$, active-to-geological transfer $e_{AG}(A,G)$, direct mining $c_G(G,E_G)$, and product retirement $r_P(P)$. With harvest fraction $\alpha \in [0,1]$ routed to $U$ and retirement fraction $\rho \in [0,1]$ returning to $U$ rather than $W$,
$$\dot z = S(\alpha, \rho)\, v(z, u), \qquad z = (X, U, A, G, P, W)^\top, \qquad v = (g, m, h, d_U, e_{GA}, e_{AG}, c_G, r_P)^\top,$$
where
$$S(\alpha, \rho) =
\begin{pmatrix}
1 & -1 & -1 & 0 & 0 & 0 & 0 & 0 \\
0 & 1 & \alpha & -1 & 0 & 0 & 0 & \rho \\
-1 & 0 & 0 & 1 & 1 & -1 & 0 & 0 \\
0 & 0 & 0 & 0 & -1 & 1 & -1 & 0 \\
0 & 0 & 1-\alpha & 0 & 0 & 0 & 1 & -1 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 1-\rho
\end{pmatrix}, \qquad \mathbf{1}^\top S = 0.$$
The zero column sums are the incidence statement of mass conservation (proved for the full system in Section 4.2). The matrix makes the routing choices visible, and the constitutive choices are features of this example, not properties of every typed ledger: the constant splits $\alpha$ and $\rho$, the compartment set, and the absorbing-sink convention are declared choices. The construction is a monomaterial projection. Coupled multi-element accounts require additional typed rows and a conservation matrix. If an application makes recovery claims, $U$ and $P$ must be split by material, location, and quality grade, with declared yields, residual routes, and exergy or capacity inputs — the conservation argument then applies to the expanded typed incidence system, not automatically to an undifferentiated quality-neutral loop. The four-block system (2) is not a specialization of this scaffold: in the scaffold assimilation $g$ is a slow $A \to X$ flux and mortality $m$ a slow $X \to U$ flux, while in (2) the uptake $T$ transfers $A^{\mathrm{act}} \to U$ with the living stock catalytic and no separate mortality primitive — two different timescale lumpings of the same physical story, and no incidence specialization maps one onto the other.

### 2.4 The four-stock resource–sink–nutrient–product system

A second exact specialization closes a resource–sink system with a nutrient stock and product stock. The state is $(S, K, N, P) \in \mathbb{R}^4_+$ (in this block's local notation, $K$ is the sink stock and $N$ the nutrient stock; the carrying capacity and living stock of Section 2.2 do not enter), with
$$\dot S = g(S,N) - H, \qquad \dot K = \theta_K H - \theta_\delta K, \qquad \dot N = -g(S,N) + \theta_\delta K + I_N, \qquad \dot P = (1 - \theta_K)H - Q_P,$$
where $\theta_K$ is the sink-generation fraction, $\theta_\delta$ the assimilation rate, $I_N$ external nutrient input, and $Q_P$ product disposal. Adding the four equations gives the mass balance
$$\frac{d}{dt}(S + K + N + P) = I_N - Q_P,$$
so total mass is conserved exactly when both boundary transfers vanish. This mass balance is an exact specialization of the incidence discipline of Section 2.1: every internal transfer cancels in the column sum, and the boundary terms survive as the ledger's declared inputs and outputs.

**Sink obstructions independent of the stock.** The mass balance has a sink-side physical reading with two empty-kernel mechanisms that operate whatever the resource stock does. With sink loading $w(H)$, assimilation $\delta(K)$, and a harvest floor $H \ge H_{\min} > 0$ (in the four-stock specialization, $w(H) = \theta_K H$ and $\delta(K) = \theta_\delta K$): under *no assimilation* ($\delta \equiv 0$), $\dot K \ge w(H_{\min}) > 0$, and the sink exceeds any finite ceiling $K_{\max}$ in finite time; under *weak assimilation* ($\delta(K_{\max}) < w(H_{\min})$), the sink load at the ceiling is still positive — $\dot K = w(H_{\min}) - \delta(K_{\max}) > 0$ at $K = K_{\max}$ — so $K$ exits above $K_{\max}$ in finite time, the explicit negation of the ceiling condition $\delta(K^\dagger) = w(H_{\min})$ with $K^\dagger \le K_{\max}$. In both cases the viability kernel (Aubin, 1991) of the constraint set $\{S \ge S_{\min},\ 0 \le K \le K_{\max}\}$ — the states from which some admissible harvest keeps both constraints for all time — is empty. The obstruction needs the sink-generation fraction $\theta_K > 0$: if $\theta_K = 0$, harvest never loads the sink and the loading argument does not apply — emptiness would then have to come from the resource constraint or an undeclared ceiling on the product stock.

The closed-ledger corollary is the same mechanism in ledger language. In a closed ledger without recycling, where $w(H)$ enters the sink irreversibly and $\delta = 0$, the sink rises monotonically against the finite total mass, and any positive output floor forces an empty viability kernel. Which constraint fails first depends on the total mass $M$, the ceiling $K_{\max}$, and the remaining stock: a ceiling below the sink's reachable mass share is crossed in finite time, while a ceiling at or above the total mass is unreachable and the violated constraint is the resource floor (the finite-budget bound of Theorem 14). For material-flows accounting this is the precise sense in which a "balanced" mass ledger can still be physically inadmissible: the bookkeeping is exact, but no harvest schedule respects both the resource floor and the sink ceiling simultaneously.

### 2.5 Mechanism typing: routing is never determined by diagnostic labels

Extraction has at least three distinct physical meanings — standing-stock culling (present extraction removes reproductive stock directly), recruitment suppression (present use prevents future recruits without immediate adult removal), and weak viability coupling (use has limited or indirect effect on reproduction). In the ledger, standing-stock culling enters as an outflow from the standing-stock compartment. The typing is the physical module's, not the diagnostic's: a diagnostic label such as "unsustainable portion" never determines physical destination. Material routing is determined by the typed physical module alone, and the diagnostic threshold that flags a flow has no standing in the incidence matrix.

**The split-assignment evidence requirement.** Where an application splits extraction between standing-stock removal and recruitment suppression — $C_{\mathrm{stock}} = \psi qEN$ and $C_{\mathrm{recruit}} = (1-\psi)qEN$ for $\psi \in [0,1]$ — the assignment requires evidence per channel. The dominant physical mechanism sets it, never a diagnostic label. Illustrative assignments through a logistic two-channel proxy (stated as illustrative, calibrated examples, not constitutive claims for the named domains): soil zinc under crop export, an existing-unit removal, at $\psi = 0.85$, against impaired mineralisation, a replenishment degradation, at $\psi = 0.25$; pollinators under adult mortality at $\psi = 0.70$ against brood failure at $\psi = 0.20$ — and across such mechanism pairs the trough depth varies by a factor of about $1.5$ from mechanism alone. The mass-routing discipline is the typing made explicit. Literally harvesting pre-recruit stages is a harvest of existing units and routes to the product and waste fractions. Habitat-induced failed recruitment is a prevented inflow — routing it into product or waste would create mass that was never in the stock. Damage to the capital stock itself (aquifer compaction, severe soil loss) is not a split-assignment channel at all, but a slow drift in capacity or a transfer to the inert sink.

### 2.6 Support saturation and the logistic limit

Two results control what the ledger's stock equation becomes when its support pool saturates. Both are singular reductions with explicit scope, and neither is a full-system reduction.

**Theorem 1 (Support-saturated logistic stock limit).**
*Fix $T < \infty$ and non-negative parameters $\mu, \delta, c, q$. For $\kappa > 0$, assume:*

*(H1) $A_\kappa$ is measurable with $A_\kappa(t) \ge a_0 > 0$ and $0 \le X_\kappa(t) \le X_{\max}$.*

*(H2) Common effort $E \in L^\infty([0,T])$.*

*Let $X_\kappa$ solve $\dot X_\kappa = \mu X_\kappa A_\kappa/(\kappa + A_\kappa) - \delta X_\kappa - cX_\kappa^2 - qE(t)X_\kappa$ and $X_0$ solve the limiting equation with the same initial value. Then $\sup_{t \le T} |X_\kappa(t) - X_0(t)| = O(\kappa)$; if $\mu > \delta$ and $c > 0$ the limit is $\dot X_0 = rX_0(1 - X_0/K_{\log}) - qE(t)X_0$ with $r = \mu - \delta$ and $K_{\log} = (\mu - \delta)/c$.*

*Proof.* Write $e(t) = |X_\kappa(t) - X_0(t)|$. The saturation defect satisfies
$$\left| \frac{A_\kappa}{\kappa + A_\kappa} - 1 \right| = \frac{\kappa}{\kappa + A_\kappa} \le \frac{\kappa}{a_0},$$
so the vector-field defect obeys
$$|\dot X_\kappa - \dot X_0| \le L_1 \kappa + L_2 e(t), \qquad L_1 = \frac{\mu X_{\max}}{a_0}, \qquad L_2 = \mu + \delta + 2cX_{\max} + q\|E\|_\infty,$$
using $|\mu - \delta| \le \mu + \delta$ and $c(X_\kappa + X_0) \le 2cX_{\max}$. Gronwall's inequality with the Lipschitz constant $L_2$ and the particular-term scale $L_1$ gives $e(t) \le (L_1/L_2)\kappa\,(e^{L_2 t} - 1) \le C_T \kappa$ on $[0,T]$. The bound $0 \le X_\kappa \le X_{\max}$ is satisfiable in the registered family: under $\mu > \delta$ the comparison $\dot X_\kappa \le X_\kappa(\mu - \delta - cX_\kappa)$ keeps $X_\kappa \le \max\{X(0), (\mu-\delta)/c\}$, so $X_{\max} = \max\{X(0), K_{\log}\}$ suffices. The limiting equation is $\dot X_0 = \mu X_0 - \delta X_0 - cX_0^2 - qE X_0$, i.e. $\dot X_0 = (\mu - \delta)X_0 (1 - X_0/K_{\log}) - qE X_0$ with $K_{\log} = (\mu - \delta)/c$. □

**Theorem 2 (Registered-family support-saturated identity).**
*In the primitive-flux core with $g(X,A) = \mu XA/(K_A + A)$, $m(X) = dX + cX^2$, $h(X,E) = qEX$, the support-saturated stock equation is, for each fixed interior $A > 0$ in the limit $K_A \to 0$,*
$$\dot X = (\mu - d)X - cX^2 - qEX = rX\left(1 - \frac{X}{K}\right) - qEX, \qquad r = \mu - d, \quad K = \frac{\mu - d}{c},$$
*requiring $\mu > d$ and $c > 0$. The identity is pointwise on the interior support region and not uniform through the depleted-pool boundary: for every $K_A > 0$, $A/(K_A + A) = 0$ at $A = 0$.*

*Proof.* At fixed $A > 0$, $A/(K_A + A) \to 1$ as $K_A \to 0$, so $g \to \mu X$ pointwise and $g - m \to (\mu - d)X - cX^2$; the algebraic reduction to the logistic form with $r = \mu - d$, $K = (\mu - d)/c$ is immediate. The non-uniformity statement is the identity $A/(K_A + A) = 0$ at $A = 0$ for every $K_A > 0$, which the pointwise limit does not touch. The scope is restricted: the limit does not eliminate the detritus compartment $U$, does not make $A$ constant near its boundary, and does not transform the memory or effort laws — an ecological stock-equation identity, not a full-system reduction and not a transfer principle for bifurcation thresholds. In the correspondence, the logistic law of (2) is this saturated, mortality-folded readout of the Theorems 1–2 family — not the vector field of the closed four-tuple of Section 2.2 — and bifurcation numbers of the two families do not transfer between them. □

**Notation.** One letter carries one sort wherever a computation is displayed; section-local aliases are declared where they occur, and the incidence operator is never written $N$ (which is reserved for the living stock):

| Symbol | Meaning | Where |
|---|---|---|
| $N$ | living stock; nutrient stock (local to §2.4) | §2.2; §2.4 |
| $S_{\mathcal{T}}$ | typed stoichiometric (incidence) operator | §2.1, Theorems 3–5, 8 |
| $v$ | non-negative primitive flux vector | §2.1 |
| $S$ | moiety readout $S = Cx$ | Theorem 3, §6 |
| $s$ | support factor $A^{\mathrm{act}}/(A^{\mathrm{act}}+A_0)$ | §2.2 |
| $\sigma$ | donor fraction $A^{\mathrm{geo}}/(A^{\mathrm{geo}}+A_{g0})$ | §2.2 |
| $\varsigma$ | noise scale of the stochastic surrogates | §7 |
| $M$ | natural-block mass $N + A^{\mathrm{act}} + A^{\mathrm{geo}} + U$ | Theorems 7, 14 |
| $\widehat{M}$ | demand-coverage matrix of the physical deficit | §5.4 |
| $K$ | carrying capacity; sink stock (local to §2.4) | §2.2; §2.4 |
| $T$ | gross uptake $\kappa_A N s$; finite horizon (local to each statement) | §2.2; Theorems 1, 5 |
| $C$ | moiety-composition matrix; operative extraction-law readout; mining intensity $C^A$ | Theorem 3; §5.4; §2.2 |
| $B$ | $R + T$; barriers (local to §3.1) | §2.2; §3.1 |
| $R$ | net regeneration; log-margin $R_B$ (local to §6.5.4) | §2.2; §6.5.4 |
| $G$ | geological pool (scaffold); reserves (local to §6.5.3, §7.6) | §2.3; §6.5.3 |
| $I$ | inert sink; boundary input $I_N$ (subscripted) | §2.2; §2.4 |
| $z$ | six-compartment state (local to §2.3) | §2.3 |
| $h$ | harvest primitive (§2.3); geometric-Brownian drift (local to §7.5) | §2.3; §7.5 |
| $x$ | ledger state | §2.1, Theorems 3–5 |
| $y$ | declared boundary states feeding the primitive fluxes | §2.1, eq. (1) |
| $\theta$ | declared constitutive parameter vector; sink-generation fraction $\theta_K$ (subscripted) | §2.1, eq. (1); §2.4 |

The implication for material-flows accounting is that a logistic stock equation is a saturated support-pool readout, not a primitive physical law: substituting it for the underlying stock-support dynamics is legitimate only where the support pool is at interior saturation and only on the timescales over which the saturated approximation holds.

---

## 3. Certification Layers and the Accounting Theorems

### 3.1 Three predicates, separated

Bookkeeping balance, stoichiometric conservation, thermodynamic admissibility, and sustainability safety are different predicates, and material-flows accounting practice routinely slides between them. This section separates the first three and proves their relationships. The argument is needed because a mass-balanced ledger can be chemically impossible, a chemically consistent ledger can violate every declared barrier, and a barrier-satisfying ledger can fail conservation — a point at which the Daly/Ayres tradition of throughput accounting meets the formalism of reaction-network theory (Feinberg, 2019; Brunner and Rechberger, 2004).

The ledger supports three distinct predicates that are related but not identical.

**Layer 1: Accounting consistency.** The balance law (1) holds almost everywhere on $[0,T]$.

**Layer 2: Conservation consistency.** $\ell^\top S_{\mathcal{T}} = 0$ for every declared conserved quantity $\ell$.

**Layer 3: Barrier safety.** For declared lower and upper barriers $\underline{B}_m(t) \le S_m(t) \le \overline{B}_m(t)$ for every component $m$ and every $t \in [0,T]$, where $S = Cx$ is the moiety-composition readout.

Layer 2 is a structural predicate on the incidence operator alone. Layers 1 and 3 are properties of a trajectory triple $(x, v, b)$. The logical relations are the content of the next two propositions.

**Proposition 1.** *Conservation consistency implies accounting consistency for the conserved quantities: if $\ell^\top S_{\mathcal{T}} = 0$, then $\frac{d}{dt}(\ell^\top x) = \ell^\top b$, and in a closed system ($b = 0$), $\ell^\top x$ is invariant.*

*Proof.* $\frac{d}{dt}(\ell^\top x) = \ell^\top \dot x = \ell^\top(S_{\mathcal{T}} v + b) = (\ell^\top S_{\mathcal{T}}) v + \ell^\top b = \ell^\top b$. □

**Proposition 2.** *Barrier safety does not follow from accounting consistency: a trajectory can be perfectly mass-balanced while violating a declared barrier; and a trajectory can satisfy declared barriers while violating a conservation law or a stoichiometric constraint. Conversely, thermodynamic admissibility (energy conservation, entropy-production nonnegativity, reaction feasibility) implies accounting consistency, but the converse does not hold; this article establishes Layers 1–3 only.*

*Proof.* First clause: on the closed ledger (2), constant extraction at a rate exceeding regeneration is exactly mass-balanced (Theorem 3 states the identity) and drives the living stock through any positive lower barrier in finite time; likewise the trajectory with $N \equiv 0$ (extinction rest of Section 4.6) is mass-balanced yet violates any positive lower barrier on $N$. Conversely, a trajectory satisfying the barriers may be generated by fluxes that fail a stoichiometric constraint — mass balance does not certify that the flux decomposition is physically realizable — or by bookkeeping that silently drops a moiety through the yield-routing violation of rule (iii) in Section 10.2, failing conservation without touching the barriers. Second clause: thermodynamic admissibility presupposes a mass balance, but a mass-balanced flux decomposition need not satisfy energy or entropy constraints; establishing those requires structure outside the present scope. □

The implication for industrial-ecology measurement is that mass-balance closure, stoichiometric consistency, and barrier compliance must each be audited separately. A single integrated assessment that reports only one of them declares less than it appears to.

### 3.2 The typed safety set

The typed safety set at time $t$ is
$$\mathcal{K}(t) = \{ x \ge 0 : \underline{B}(t) \le Cx \le \overline{B}(t) \},$$
and the non-compensatory assessment reads
$$\mathcal{V}_{\mathrm{typed}} = \{ x(\cdot) : x(t) \in \mathcal{K}(t)\ \forall t \in [0,T] \}.$$
This is a conjunctive criterion: all moiety barriers must be satisfied simultaneously, and no weighted aggregate $\sum_m w_m S_m$ is used as the decision criterion. The force of the conjunction is the subject of Section 10.1.

### 3.3 The flux-reconstruction identity

**Theorem 3 (Flux reconstruction under a typed balance law).**
*Let $x : [0,T] \to \mathbb{R}_+^n$ be absolutely continuous with $\dot x(t) = S_{\mathcal{T}} v(t) + b(t)$ almost everywhere, $v \in L^1([0,T]; \mathbb{R}_+^J)$, $b \in L^1([0,T]; \mathbb{R}^n)$, and $S = Cx$ with $C \in \mathbb{R}^{M \times n}$ the moiety-composition matrix. Then*
$$S(t) = S(0) + \int_0^t \bigl( C S_{\mathcal{T}} v(\tau) + Cb(\tau) \bigr) d\tau,$$
*and for continuous barriers $\underline{B}, \overline{B}$ the trajectory satisfies $\underline{B}_m(t) \le S_m(t) \le \overline{B}_m(t)$ for all $t \in [0,T]$ if and only if the corresponding integrated inequalities hold for all $t \in [0,T]$.*

*Proof.* Integrate $\dot S = C\dot x = C(S_{\mathcal{T}} v + b) = C S_{\mathcal{T}} v + Cb$ from $0$ to $t$; this is valid because $x$ is absolutely continuous and $C$ linear. The barrier equivalence follows because $S_m$ is continuous (as $x$ is absolutely continuous) and the barriers are continuous, so a pointwise inequality violation is an integrated-inequality violation at the same time. □

Two cases are distinguished. **Prescribed or observed fluxes:** if $v(t)$ and $b(t)$ are known and integrable, stock balances are reconstructed by integration without solving the internal constitutive dynamics — the computationally simple auditing case. **Endogenous fluxes:** if $v(t) = v(x(t), u(t), d(t))$, flux-only auditing is not generally possible without solving, estimating, or bounding the coupled system; the identity still holds, but the integral cannot be evaluated without determining $v(t)$. In both cases the barriers are declared, not computed: the flux data do not compute ecological threshold values, aquifer collapse thresholds, or concentration boundaries — the theorem establishes trajectory compliance with declared barriers, not derivation of the barriers themselves.

With $h_m(t) \ge 0$ the net outflow of moiety $m$ across the system boundary and $r_m(t) \ge 0$ the net inflow, the sign convention reads
$$S_m(t) = S_m(0) + \int_0^t \bigl( r_m(\tau) - h_m(\tau) \bigr) d\tau,$$
and the depletion condition is
$$S_m(0) + \int_0^t \bigl( r_m(\tau) - h_m(\tau) \bigr) d\tau \ge \underline{B}_m(t).$$

### 3.4 The conservation-law reduction

**Theorem 4 (Conservation-law reduction).** *If $\ell^\top S_{\mathcal{T}} = 0$ for some vector $\ell \in \mathbb{R}^n$, then*
$$\ell^\top x(t) = \ell^\top x(0) + \int_0^t \ell^\top b(\tau) d\tau;$$
*in a closed system ($b = 0$), $\ell^\top x$ is invariant.*

*Proof.* This is Proposition 1 integrated: $\frac{d}{dt}(\ell^\top x) = \ell^\top b$; integrate. □

A conserved moiety is a row $c_m^\top$ of $C$ with $c_m^\top S_{\mathcal{T}} = 0$; then $S_m = c_m^\top x$ satisfies $\dot S_m = c_m^\top b$. In a closed system $S_m$ is constant, and in an open system $S_m$ changes only through boundary flows. Conservation does not imply barrier safety: if a closed conserved moiety has fixed total stock $S_m(t) = S_m(0)$, a time-varying barrier can become infeasible solely because the barrier moves. The three objects are distinct: the conservation invariant ($S_m$ constant), the barrier tube ($\underline{B}_m \le S_m \le \overline{B}_m$), and the intersection of the invariant manifold with the barrier tube. A conservation law alone does not imply that the trajectory satisfies the barrier. The precise sense is linear: the set $\{x \ge 0 : \ell^\top x = \ell^\top x(0),\ \underline{B} \le Cx \le \overline{B}\}$ may be empty even though each of the three objects is separately well-defined. Barrier–conservation compatibility is a linear feasibility programme, not a slogan.

### 3.5 The flux-bounding envelope theorem

**Theorem 5 (Flux-bounding envelopes).**
*Assume:*

*(H1) The primitive fluxes and boundary transfers satisfy componentwise bounds $v(t) \in [\underline{v}(t), \overline{v}(t)]$ and $b(t) \in [\underline{b}(t), \overline{b}(t)]$ for all $t \in [0,T]$.*

*For any matrix $\mathsf{A}$ write $\mathsf{A}^{+} = \max\{\mathsf{A}, 0\}$ and $\mathsf{A}^{-} = \max\{-\mathsf{A}, 0\}$ entrywise, and define for each moiety $m$ the envelope integrands*
$$\varphi_m(\tau) = (C S_{\mathcal{T}})_{m}^{+} \underline{v}(\tau) - (C S_{\mathcal{T}})_{m}^{-} \overline{v}(\tau) + C_{m}^{+} \underline{b}(\tau) - C_{m}^{-} \overline{b}(\tau),$$
$$\psi_m(\tau) = (C S_{\mathcal{T}})_{m}^{+} \overline{v}(\tau) - (C S_{\mathcal{T}})_{m}^{-} \underline{v}(\tau) + C_{m}^{+} \overline{b}(\tau) - C_{m}^{-} \underline{b}(\tau),$$
*and the envelopes*
$$\underline{S}_m(t) = S_m(0) + \int_0^t \varphi_m(\tau)\, d\tau, \qquad \overline{S}_m(t) = S_m(0) + \int_0^t \psi_m(\tau)\, d\tau.$$
*Then $S_m(t) \in [\underline{S}_m(t), \overline{S}_m(t)]$ for all $t \in [0,T]$ and all $m$.*

*Proof.* By Theorem 3, $\dot S_m = (C S_{\mathcal{T}} v + Cb)_m$. For each row $m$ and time $\tau$, the bilinear form $(C S_{\mathcal{T}})_m v$ is linear in $v$ with coefficient vector $(C S_{\mathcal{T}})_m$, whose positive and negative parts give, over the box $[\underline{v}(\tau), \overline{v}(\tau)]$, the pointwise bounds
$$(C S_{\mathcal{T}})_{m}^{+} \underline{v}(\tau) - (C S_{\mathcal{T}})_{m}^{-} \overline{v}(\tau) \;\le\; (C S_{\mathcal{T}})_m v(\tau) \;\le\; (C S_{\mathcal{T}})_{m}^{+} \overline{v}(\tau) - (C S_{\mathcal{T}})_{m}^{-} \underline{v}(\tau),$$
attained at the extreme points of the box; the same argument applies to $C_m b(\tau)$, and adding gives $\varphi_m(\tau) \le \dot S_m(\tau) \le \psi_m(\tau)$. Integrating over $[0,t]$ yields the stated envelope. □

**Corollary (Flux-derived barrier certificate).** *If $\underline{S}_m(t) \ge \underline{B}_m(t)$ and $\overline{S}_m(t) \le \overline{B}_m(t)$ for all $t \in [0,T]$ and all $m$, then every trajectory compatible with the flux bounds is barrier-safe on $[0,T]$.*

*Proof.* By Theorem 5 every such trajectory satisfies $\underline{S}_m(t) \le S_m(t) \le \overline{S}_m(t)$; the certificate conditions sandwich $S_m$ between the barriers. □

Two qualifications are part of the theorem. The bounds are conservative: they hold for *all* flux selections in the declared boxes, including selections that are not jointly realizable by the coupled dynamics, so the certificate may fail when a trajectory with jointly realizable fluxes would pass; attainability requires solving or bounding the coupled system. When the fluxes are state-dependent, $v = v(x)$, the declared box must additionally be forward-invariant under the coupled dynamics for the envelopes to bound the system's reachable set; without that condition the corollary is a certificate for flux-admissible paths only, not for the ODE's trajectories. And the envelope is an interval computation on the flux data, not a forecast: it says nothing about what the fluxes will be, only about what every admissible flux path implies for the stock. Stoichiometric and donor-limit constraints make the jointly admissible flux selections a polytope rather than a box; the tight certificate is the linear programme over that polytope, and the box envelope above is its auditing relaxation — the box is what is audited, the polytope what is realizable. The envelope is the interval-arithmetic counterpart, at the level of declared flux bounds, of the data-reconciliation practice of material flow analysis (Brunner and Rechberger, 2004).

**Worked envelope on the closed block.** On (2) with declared boxes $N \in [0, K]$ and $E \in [0, E_{\max}]$, the mass row of the incidence gives $\dot M = -qEN - C^{A,\mathrm{lim}} \in [-(qE_{\max}K + C^A),\, 0]$, hence $M(t) \in [M(0) - (qE_{\max}K + C^A)t,\ M(0)]$. The conservatism is visible in the extremes: the maximal extraction $qE_{\max}K$ is realizable only at $N = K$, where regeneration vanishes, and maximal recharge coincides with minimal extraction — box extremes the coupled dynamics cannot realize jointly.

### 3.6 Finite exhaustion under uniform drift, and its failure mode

**Theorem 6 (Finite exhaustion under uniform negative drift).**
*Assume:*

*(H1) $S$ is absolutely continuous with $\dot S(t) \le -\varepsilon < 0$ whenever $S(t) > B$, where $B$ is a constant lower barrier and $\varepsilon > 0$ a uniform drift bound.*

*(H2) $S(0) > B$.*

*Then the first hitting time satisfies*
$$\tau_B = \inf\{ t \ge 0 : S(t) \le B \} \le \frac{S(0) - B}{\varepsilon}.$$

*Proof.* While $S(t) > B$, the drift bound integrates to $S(t) \le S(0) - \varepsilon t$; the right-hand side reaches $B$ at $t = (S(0) - B)/\varepsilon$, so by continuity of $S$ the crossing occurs no later. □

The uniform-margin assumption is essential, and its absence is the classical failure mode.

**Counterexample (proportional extraction).** *For donor-controlled proportional extraction $\dot S = -kS$ with $k > 0$ and $S(0) > 0$, the stock satisfies $S(t) = S(0)e^{-kt} > 0$ for every finite $t$: the stock approaches zero asymptotically and is never exhausted in finite time, $\tau_0 = \infty$. The time to a positive barrier $B > 0$ is $\tau_B = k^{-1}\log(S(0)/B)$, finite for $B > 0$ but diverging as $B \to 0$.*

In particular, the claim that positive extraction implies finite exhaustion is false, and every exhaustion statement must name its referent. Internal transfers do not exhaust a total moiety: in a closed system, internal conversion redistributes a conserved moiety but does not exhaust it. Exhaustion of a compartment requires a boundary outflow, an irreversible conversion into an uncounted or unavailable form, destruction of the relevant function, or a barrier defined on a particular compartment rather than on the total moiety. Whether "exhaustion" refers to the total conserved moiety, a compartment stock, an accessible or functional stock, a stock above a lower barrier, or an economically recoverable reserve — these are different quantities, and the theorem must specify which (Section 6.4). The counterexample and this taxonomy are the content of the following named statement, which the rest of the article uses as its boundary discipline.

**Proposition (Depletion is compartmental).** *On a closed typed ledger, the total mass $\mathbf{1}^\top x$ of each conserved moiety is invariant along trajectories; consequently every finite hitting time of a zero readout is the hitting time of a compartment or of a barrier on a readout, never of total mass, and "exhaustion of the natural block" (Theorems 7 and 14) is transfer across the block boundary into the product, waste, and inert compartments.*

The boundary discipline this proposition fixes is the ecological-economics one of Daly (1990): depletion is not loss of matter, it is loss of access to matter in the form and place that supports the service in question. The remainder of the article keeps that distinction in force.

---

## 4. Conservation and Positivity of the Closed Ledger

### 4.1 The natural-block mass identity

**Theorem 7 (Natural-block mass identity).**
*Let $M = N + A^{\mathrm{act}} + A^{\mathrm{geo}} + U$. Along every trajectory of the closed natural block (2) with optional mining restored,*
$$\dot M = -qEN - C^{A,\mathrm{lim}},$$
*i.e. mass leaves the natural block exactly at the extraction rate, plus the donor-limited mining rate; under the institutional-failure specialization ($C^A = 0$), $\dot M = -qEN$. The identity is stated for the declared harvest routing $\alpha = 0$ of Section 2.2; with a detritus-routed harvest fraction $\alpha > 0$ the block export is $(1-\alpha)qEN$ and the identity reads $\dot M = -(1-\alpha)qEN - C^{A,\mathrm{lim}}$.*

*Proof.* Sum the four equations of (2), with the mining term subtracted from $\dot A^{\mathrm{geo}}$:
$$\dot M = (R - qEN) + (-B + e_{GA} - e_{AG} + \gamma_U U) + (-e_{GA} + e_{AG} - C^{A,\mathrm{lim}}) + (T - \gamma_U U) = R - B + T - qEN - C^{A,\mathrm{lim}},$$
and $R - B + T = R - (R + T) + T = 0$. The mined fraction routes out of the four-coordinate natural block; the full-ledger theorems of Sections 4.2–4.3 record the mining column as an internal transfer between compartments outside the block — consistent because the block boundary, not the ledger boundary, is crossed. □

### 4.2 Stoichiometric conservation of the full ledger

**Theorem 8 (Stoichiometric conservation).** *Let $X = (N, P, W, I, U, A^{\mathrm{act}}, A^{\mathrm{geo}})$ be the mass compartments of one resource system and $S_{\mathcal{T}}$ the incidence matrix of its flux ledger. One-way transfers are non-negative and donor-limited; net regeneration is the difference of two such primitives and is signed when $N > K$. Under the unit-sum routing constraints with $0 \le \alpha \le 1$,*
$$\dot X = S_{\mathcal{T}} F(X), \qquad \frac{d}{dt}\mathbf{1}^\top X = 0.$$

*Proof.* Every primitive is a transfer between two compartments, or a pair of opposite primitives implementing a two-way exchange; the corresponding column of $S_{\mathcal{T}}$ has entries $+1$ and $-1$ in the receiving and donating rows and zeros elsewhere. Routing tensors are column-stochastic in the destination-indexed convention by construction: each unit of a split flux sums to one across destinations. Hence $\mathbf{1}^\top S_{\mathcal{T}} = 0$ and $\mathbf{1}^\top \dot X = \mathbf{1}^\top S_{\mathcal{T}} F = 0$. The theorem is an exact conservation identity under the routing constraints. □

The seven-compartment incidence claimed by Theorem 8 is not displayed separately: it is the pattern of the displayed six-compartment $S(\alpha,\rho)$ of Theorem 9 with the inert column (no outflow) appended and the harvest column split by $(\alpha, 1-\alpha)$.

### 4.3 Conservation of the six-compartment ledger

**Theorem 9 (Six-compartment conservation).** *For the system of Section 2.3, $\frac{d}{dt}\mathbf{1}^\top z = 0$; the total mass $M_6 = X + U + A + G + P + W$ is constant along every trajectory on which the classical solution is defined.*

*Proof.* With $M_6 = \mathbf{1}^\top z$, $\dot M_6 = \mathbf{1}^\top S(\alpha,\rho) v = 0$ because each column of $S$ sums to zero; term by term: assimilation gives $g - g = 0$; mortality gives $-m + m = 0$; decomposition gives $-d_U + d_U = 0$; geological exchange gives $e_{GA} - e_{GA} = 0$ and $-e_{AG} + e_{AG} = 0$; mining gives $-c_G + c_G = 0$; and the remaining harvest and retirement terms satisfy $-h + \alpha h + (1-\alpha)h = 0$ and $\rho r_P - r_P + (1-\rho)r_P = 0$. □

Two scope notes are part of the theorem. The conservation argument applies to the expanded typed incidence system when quality grades are split — not automatically to an undifferentiated quality-neutral loop. And open systems are explicit: imports, exports, atmospheric losses, and cross-boundary transport enter as typed boundary fluxes, giving $\dot M_6 = I_{\partial} - O_{\partial}$; writing these flows explicitly is preferable to preserving a nominal invariant by allowing an unobserved or finite donor compartment to become negative. Theorems 7–9 are three instances of the conservation lemma of Proposition 1 — each is the identity $\frac{d}{dt}(\ell^\top x) = \ell^\top b$ for a declared ledger and boundary with $\ell = \mathbf{1}$ — differentiated only by which compartments the declaration includes.

### 4.4 Orthant invariance

**Theorem 10 (Orthant invariance of the closed ledger).** *The nonnegative orthant in $(N, A^{\mathrm{act}}, A^{\mathrm{geo}}, U)$ is forward invariant for the closed natural block (2).*

*Proof.* The right-hand side is locally Lipschitz on a neighbourhood of the closed orthant: each Michaelis–Menten factor $s$, $\sigma$ is $C^\infty$ on the nonnegative half-line because the registered regime keeps $A_0 > 0$ and $A_{g0} > 0$. Face by face. On $A^{\mathrm{geo}} = 0$ one has $\sigma = 0$, hence $e_{GA} = 0$ and $\dot A^{\mathrm{geo}} = e_{AG} = \omega_A A^{\mathrm{act}} \ge 0$. On $A^{\mathrm{act}} = 0$ one has $s = 0$, so $R = B = T = e_{AG} = 0$ and $\dot A^{\mathrm{act}} = e_{GA} + \gamma_U U \ge 0$. On $N = 0$, extraction and uptake vanish and $\dot N = 0$. On $U = 0$, $\dot U = T \ge 0$. Nagumo's inward-pointing criterion (Aubin, 1991) yields forward invariance of the orthant. □

**Theorem 11 (Forward invariance of the six-compartment cone).** *Under the donor boundary assumptions of Section 2.3 (each primitive flux vanishes when its donor is empty, fluxes continuous in effort and locally Lipschitz in the state), $\mathbb{R}^6_+$ is forward invariant for the six-compartment system.*

*Proof.* Face by face: at $X = 0$, $g = m = h = 0$ so $\dot X = 0$; at $U = 0$, $\dot U = m + \alpha h + \rho r_P \ge 0$; at $A = 0$, $\dot A = -g + d_U + e_{GA} - e_{AG} = d_U + e_{GA} \ge 0$, the two negative terms vanishing by donor limitation ($A$ is the donor of both $g$ and $e_{AG}$); at $G = 0$, $\dot G = e_{AG} \ge 0$; at $P = 0$, $\dot P = (1-\alpha)h + c_G \ge 0$; at $W = 0$, $\dot W = (1-\rho)r_P \ge 0$. The vector field belongs to the tangent cone at every boundary point, and the tangent-cone invariance theorem applies. Conservation and boundary admissibility are separate obligations, and the finite-donor condition carries a discipline: a target-relaxation law $e_{GA} = \omega(A^{\mathrm{eq}} - A)$ does not satisfy it unless also limited by $G$; it may be used only with the source declared an effectively infinite external reservoir, in which case the system is open rather than closed. □

The classical lineage of these statements is the compartmental-systems nonnegativity theory (Jacquez and Simon, 1993); the donor-limitation condition is the exact sufficiency requirement — algebraic cancellation alone does not establish invariance.

### 4.5 No interior rest at positive effort

**Theorem 12 (No interior rest at positive effort).**
*Assume:*

*(H1) $E \equiv E_* > 0$ is constant.*

*Then a rest point of the closed natural block satisfies $R + C^{A,\mathrm{lim}} = 0$ after restoring optional mining; with $C^A = 0$ this is $R = 0$, hence $N = 0$ or $N = K$ or $A^{\mathrm{act}} = 0$. None of these is compatible with $E_* > 0$ and $N_* > 0$: (i) $N = K$ and $E_* > 0$ give $\dot N = -qE_* K < 0$; (ii) $A^{\mathrm{act}} = 0$ and $A^{\mathrm{geo}} > 0$ give $\dot A^{\mathrm{act}} = \omega_A A^{\mathrm{eq,intrinsic}} \sigma > 0$; (iii) $N = 0$ forces $R = T = 0$ and reduces to the extinction family $\mathcal{R}_0$ of Theorem 13. In particular the working point $(N^*, A^{\mathrm{act}*}) = (89.526, 397.87)$ is not a rest point at $E = E^* \approx 2.090$: $\dot N = 0$ holds there by construction ($R^* = qE^*N^* \approx 0.187 > 0$), and the rest condition of the proof below fails on the abiotic pair.*

*Proof.* At a rest point, $\dot U = 0$ forces $\gamma_U U = T$. Adding $\dot A^{\mathrm{act}} + \dot A^{\mathrm{geo}}$ gives $-B + \gamma_U U - C^{A,\mathrm{lim}} = 0$; with $\gamma_U U = T$ and $B = R + T$ this is $R + C^{A,\mathrm{lim}} = 0$. With mining declared ($C^A > 0$) this forces $R \le 0$; with $C^A = 0$ it is $R = 0$, and from the constitutive law $R = rN(1 - N/K)s = 0$ implies $N = 0$ or $N = K$ or $s = 0$ (that is, $A^{\mathrm{act}} = 0$). Cases (i)–(iii) exclude each branch at positive effort; in the mining case the contradiction is more direct — $\dot N = 0$ with $E_* > 0$ and $N_* > 0$ gives $R = qE_*N_* > 0$, while the abiotic rest condition gives $R = -C^{A,\mathrm{lim}} \le 0$. At the working point $\dot N = 0$ by construction while rest would require $R = 0$; with $\dot U = 0$ the abiotic pair would satisfy $\dot A^{\mathrm{act}} + \dot A^{\mathrm{geo}} = -R < 0$. □

### 4.6 The extinction–geochemical rest set

**Theorem 13 (Vanishing-extraction rest set).** *With vanishing extraction ($E \equiv 0$), the rest points of the closed natural block (2) are exactly the two families*
$$\mathcal{R}_0 = \bigl\{ N = 0,\ U = 0,\ A^{\mathrm{act}} = A^{\mathrm{eq,intrinsic}}\,\sigma(A^{\mathrm{geo}}),\ A^{\mathrm{geo}} \ge 0 \bigr\} \cup \bigl\{ N = K,\ U = \kappa_A K s/\gamma_U,\ A^{\mathrm{act}} = A^{\mathrm{eq,intrinsic}}\,\sigma,\ A^{\mathrm{geo}} \ge 0 \bigr\},$$
*where in the second family $s = A^{\mathrm{act}}/(A^{\mathrm{act}} + A_0)$ is evaluated at the solution — together with the frozen-biomass face $\{(N, 0, 0, 0) : N \ge 0\}$, on which $s = 0$ identically and the biomass is frozen at its initial value. With $E > 0$ constant, no rest point exists at all (Theorem 12). If $A_{g0} = 0$ and $\sigma \equiv 1$ is imposed for $A^{\mathrm{geo}} > 0$, the $\mathcal{R}_0$ ray is $A^{\mathrm{act}} = A^{\mathrm{eq,intrinsic}}$, $A^{\mathrm{geo}} > 0$ — the endpoint $A^{\mathrm{geo}} = 0$ is excluded, because there the donor-limited recharge vanishes and $\dot A^{\mathrm{act}} = -\omega_A A^{\mathrm{eq,intrinsic}} < 0$. The constitutive laws carry no basal mortality independent of the support factor; adding one ($\mu_{\mathrm{basal}} N$, stock $\to$ detritus) collapses the frozen-biomass face and does not touch Theorems 7–12 or 14.*

*Proof.* With $E \equiv 0$, set the four derivatives to zero. From $\dot A^{\mathrm{geo}} = -e_{GA} + e_{AG} = 0$: $e_{GA} = e_{AG}$, i.e. $\omega_A A^{\mathrm{eq,intrinsic}} \sigma = \omega_A A^{\mathrm{act}}$, so $A^{\mathrm{act}} = A^{\mathrm{eq,intrinsic}} \sigma$ — the geological-exchange balance, in which the active pool is pinned to the donor-scaled intrinsic target. From $\dot N = R = 0$: $rN(1 - N/K)s = 0$. If $A^{\mathrm{geo}} > 0$ the geo-balance pins $A^{\mathrm{act}} > 0$, so $s > 0$ and $N = 0$ or $N = K$. At the boundary $A^{\mathrm{geo}} = 0$ the geo-balance forces $A^{\mathrm{act}} = 0$ (since $\sigma(0) = 0$), hence $s = 0$ and $\dot N = 0$ for every $N \ge 0$; with $U = 0$ the remaining equations vanish identically, so the frozen-biomass face $\{(N, 0, 0, 0) : N \ge 0\}$ is a rest set. From $\dot U = T - \gamma_U U = 0$: $U = T/\gamma_U = \kappa_A N s/\gamma_U$, which vanishes in the $N = 0$ branch and is positive in the $N = K$ branch. From $\dot A^{\mathrm{act}} = -B + e_{GA} - e_{AG} + \gamma_U U = -(R + T) + 0 + \gamma_U U$: this vanishes in both branches, since $\gamma_U U = T$ and $R = 0$ hold there. The two families together with the frozen-biomass face are exactly the stated rest set. "Geochemical" names the mechanism of both families' active-pool rest: the pool rests at the donor-scaled intrinsic target; apart from the frozen-biomass face, no rest point exists away from extinction or carrying capacity. The institutional memory yields $E \to E^*$ at $N = 0$ with extraction vanishing identically — consistent with the rest set and not an interior rest. □

### 4.7 Extraction integrability

**Theorem 14 (Integrable extraction).** *Let $M = N + A^{\mathrm{act}} + A^{\mathrm{geo}} + U$. Then $M(t) = M(0) - \int_0^t qE(s)N(s)\, ds \ge 0$, so*
$$\int_0^\infty qE(s)N(s)\, ds \le M(0) < \infty;$$
*in particular $qEN \in L^1(0,\infty)$, and no trajectory maintains extraction at the working value $qE^*N^* \approx 0.187$ for all time; with mining restored, $\int_0^\infty \bigl( qE(s)N(s) + C^{A,\mathrm{lim}}(s) \bigr) ds \le M(0)$.*

*Proof.* By Theorem 7, $M(t) = M(0) - \int_0^t qE(s)N(s)\, ds$; forward invariance (Theorem 10) gives $M(t) \ge 0$, so the improper integral is at most $M(0)$. If $qEN \equiv qE^*N^*$ for all $t \ge 0$, the integral would diverge. □

This is the depletion-horizon semantics of the closed ledger in its strongest form: the donor budget is finite and extraction is integrable against it. A constant extraction flux $c > 0$ exhausts the budget in finite time ($M$ reaches its lower bound no later than $M(0)/c$), while proportional extraction $qEN$ need not drive $M$ to zero in finite time — the integral bound of the theorem is the whole statement, and the hitting time of $M = 0$ may be infinite. This is the finite-budget fact that Section 9 turns into the non-reduction boundary with the open working system. The theorem does not select among the vanishing-extraction rests of Theorem 13: integrable extraction is compatible with approach to either the extinction family or the carrying-capacity–geochemical family, and the $L^1$ bound alone decides nothing between them.

### 4.8 The conditional hybrid moiety balance

**Conditional Theorem 15 (Hybrid moiety balance).**
*Assume:*

*(H1) $r$ is absolutely continuous between locally finite event times with left and right limits at events.*

*(H2) $\dot r = \mathsf{S}\nu + b$ with $\nu \ge 0$, separate reverse columns, and donor-limited negative boundary flows.*

*(H3) $\mathsf{L}^\top \mathsf{S} = 0$.*

*Then*
$$\mathsf{L}^\top r(t) - \mathsf{L}^\top r(0) = \int_0^t \mathsf{L}^\top b\, ds + \sum_{t_k \le t} \mathsf{L}^\top \bigl[ r(t_k^+) - r(t_k^-) \bigr].$$

*Proof.* Integrate the continuous balance between consecutive events and telescope the left/right state differences. □

The theorem is conditional, and its jump interpretation is part of the content: an internal-transformation jump requires $\mathsf{L}^\top(r^+ - r^-) = 0$ or a jump incidence factorization with left-kernel conservation; a boundary-crossing jump is a boundary impulse and belongs in the boundary term. Two obligations ride the theorem. The *yield-routing obligation*: if a transformation is represented with a yield below one for a declared moiety, the omitted fraction must be routed to another represented compartment or a declared boundary flow — otherwise the claimed moiety balance holds only after silently dropping that moiety from $\mathsf{L}$. And the *separation obligation*: this is the hybrid variant of Theorem 4, retained at its own conditional status; the two statements are not merged.

### 4.9 Cancellation is cheap

Summing the six material equations of a ten-state admissibility template gives the exact identity
$$\frac{d}{dt}\bigl( \bar X_A + X_J + P + U + A + G \bigr) = 0.$$
This is an algebraic cancellation only: it does not prove forward invariance of the six material states or physical admissibility of every term. The ghost-sink check is part of the discipline: the same birth-transfer rate $g_B$ enters $\dot X_J$ and $\dot A$ with opposite signs, so material not transferred to juveniles remains in $A$ — there is no unmatched sink in the six-state ledger. The identity is retained precisely for its discipline: formal cancellation coexists with boundary failure elsewhere in the same template (its geological exchange is not donor-limited), and the cancellation by itself establishes nothing about admissibility. Conservation (Theorems 7–9) and positivity (Theorems 10–11) are proved separately in every well-posed ledger of this article, exactly because cancellation is cheap and admissibility is not. The template's remaining negative witnesses — a variance closure that is not realizable by a non-negative spatial distribution, and an output functional without a displayed state equation — are recorded in the supplementary material as audited admissibility failures.

**The closed-ledger portrait.** Theorems 7–14 assemble into a complete qualitative portrait of the closed orthant: conservation (Theorems 7–9), positivity (Theorems 10–11), no interior rest at positive effort (Theorem 12), the two-family vanishing-extraction rest set with the frozen-biomass face (Theorem 13), and the finite donor budget (Theorem 14). The portrait is the source object handed to the interface of Section 9: the closed system's candidate long-time set is the rest set of Theorem 13, and the budget of Theorem 14 bounds how long any positive-flux configuration can persist. For industrial-ecology measurement the message is direct: a "balanced" closed ledger is a finite-budget object, and any sustained extraction against it must integrate to a quantity no greater than the initial budget.

---

## 5. Service Readouts and the Componentwise Deficit

Services are observations or feasible outputs of the physical state, not additional conserved mass. Internal physical transfers are not services merely because they appear in a ledger: a typed readout identifies the delivered flow, its boundary, and any unit conversion. This distinction is the accounting counterpart of the ecological-economics point that a service flow (Ayres' "useful work", Daly's "throughput-of-services") is not the same object as the mass that delivers it.

### 5.1 The service readout and the contemporaneous balance

For services indexed by $i = 1, \ldots, n$, write $s_i(t) = \mathcal{O}_i(x(t), u(t), \theta)$, where $u$ denotes admissible operating or extraction choices and $s_i$ and the demand $d_i$ share service-specific units. Where delivered services are selected or converted ledger fluxes, the readout is linear in the primitives,
$$s = \mathcal{O}(x, u, \theta) = Q(\theta)\, v(x, u),$$
with every row of $Q$ declaring the delivery boundary and the conversion into one service-specific unit; more general state-dependent readouts are possible. The contemporaneous component balance is
$$b_i(t) = s_i(t) - d_i(t),$$
and $b_i(t) \ge 0$ means measured supply meets measured demand for component $i$ at that instant. It does not by itself imply that the underlying trajectory is sustainable: a stock can meet current demand while declining toward a threshold, and a stock below a desired level can have a positive current balance while recovering.

### 5.2 The state-dependent feasible balance domain

**Definition 1 (Feasible balance domain).** *For an admissible operating set $\mathcal{U}(x,t)$ and a declared demand set $\mathcal{D}(t)$,*
$$\mathcal{B}(x,t) = \{ \mathcal{O}(x,u,\theta) - d : u \in \mathcal{U}(x,t),\ d \in \mathcal{D}(t) \}.$$

The geometry of the balance domain is state dependent and inherited partly from the stock–flow model; no unrestricted argument can replace an application-specific analysis of $\mathcal{B}(x,t)$. This domain is the object against which any scalar certificate claim must be checked (Section 10.1): a weighted sum certifies componentwise nonnegativity on $\mathcal{B}(x,t)$ only through an implication proved from the physical restrictions that define the domain.

### 5.3 Support provenance and the directional support gap

Current service adequacy and regenerative feasibility are different claims. Let $\Gamma_{\mathrm{all}}(x,t) \subseteq \mathbb{R}^n_+$ contain the service vectors feasible through all pathways admitted by an application, and $\Gamma_{\mathrm{reg}}(x,t) \subseteq \Gamma_{\mathrm{all}}(x,t)$ the feasible set after imposing the declared regenerative-flow, system-boundary, material-quality, and exergy or capacity restrictions. These correspondences are application inputs obtained from a typed pathway or technology model; the stock ledger alone does not construct them.

**Definition 2 (Directional regenerative-support fraction and gap).**
*Assume:*

*(H1) $0 \in \Gamma_{\mathrm{reg}}(x,t)$.*

*(H2) A nonzero service direction $\bar s \ge 0$ is chosen.*

*Define*
$$\alpha_{\mathrm{reg}}(\bar s; x, t) = \sup\{ \alpha \in [0,1] : \alpha \bar s \in \Gamma_{\mathrm{reg}}(x,t) \}.$$
*The vector $(1 - \alpha_{\mathrm{reg}})\bar s$ is the directional support gap, measured in the same service units as $\bar s$. A realized service $s \in \Gamma_{\mathrm{all}} \setminus \Gamma_{\mathrm{reg}}$ is support-dependent under that declaration even when $s \ge d$.*

Attainment requires closedness: if $\Gamma_{\mathrm{reg}}$ is not closed the supremum may not be attained, and the gap is relative to a supremal fraction, not necessarily an achievable boundary service. The non-interpretation discipline is equally part of the definition: the statement neither subtracts raw material from service nor proves that a physical stock is declining; net depletion still requires a negative stock balance or a trajectory argument. The provenance partition behind $\Gamma_{\mathrm{reg}}$ (renewable flow, recovered or recycled material, imports, non-renewable drawdown) never adds unlike physical units.

### 5.4 The componentwise deficit and the specialization identity

On the unreduced ledger the physical deficit is the diagnostic
$$\Delta^{\mathrm{phys}}(t) = C(t) - \widehat{M}^\top S(t),$$
with $C$ the operative extraction-law readout and $\widehat{M}$ the declared demand-coverage matrix mapping the moiety readout $S = Cx$ into the units of the coverage vector $C(t)$ — rows indexed by covered services, columns by moieties, entries the declared stoichiometric coefficients of the coverage convention (the hat distinguishes the matrix from the scalar natural-block mass $M$ of Section 4.1). It does not drive the physical equations, and it is not equal to $-\dot N$ unless waste–product feedback vanishes and the service is identified with regeneration. The single-resource specialization (the omitted product, waste, and price parameters $\mu, \nu, \rho$ of the unreduced ledger set to zero, together with $C^A = 0$) makes that identification, and on that class — and only on that class — the deficit collapses to the stock-decline rate.

**Lemma 16 (Exact specialization deficit identity).** *On every trajectory of the specialized system, and of every reduced system whose stock equation is $\dot N = R(N,A) - qEN$,*
$$qEN - R(N,A) = -\dot N, \qquad \Lambda(t) := \bigl[ qEN - R \bigr]_+ = \bigl[ -\dot N \bigr]_+.$$

*Proof.* Substitute the stock equation: $qEN - R = -(R - qEN) = -\dot N$. □

The collapse is a property of the specialization, not a definition of liquidation on the unreduced ledger; the general diagnostic remains $C - \widehat{M}^\top S$.

**Decline pressure.** In the registered delay family the depletion-pressure classification is $\Lambda(t) = \max\{0, qE(t)N(t) - R(N(t), A^{\mathrm{act}}(t))\} = \max\{0, -\dot N(t)\}$: the memory input of the institutional dynamics is a smoothed stock-decline rate, exactly the positive part of the decline. It is not a stock-level scarcity measure, not an unmet-consumption measure, and not an independently observed service deficit. Since $qEN - R(N, A^{\mathrm{act}}) = O(N)$ as $N \to 0$, the raw decline input vanishes near extinction while the positive baseline source of the effort law can still sustain commanded effort — the incremental decline amplification disappears, but the effort command need not; a controller intended to respond to low stock irrespective of its current rate of change requires a separately registered level-dependent channel.

---

## 6. Depletion Arithmetic

The ledger supplies the net active-pool derivative needed to distinguish gross throughput from net decline and from a model-conditioned threshold time. The distinction matters because "time to depletion" is publicly used as if all three were one quantity. They are not, and the worked instances of this section make the differences explicit. Let $A_{\min}$ be a declared threshold for the active abiotic pool with $A > A_{\min}$.

### 6.1 The three quantities

**Definition 3 (Gross turnover intensity and support coverage).** *With assimilation $g(X,A) > 0$, the gross turnover intensity is $J_A^{\mathrm{gross}} = g(X,A)/A$ and the gross support-coverage ratio is $H_A^{\mathrm{gross}} = (A - A_{\min})/g(X,A)$.*

Neither is a time to depletion. The implication $g > 0 \Rightarrow \dot A < 0$ is false in general: at an interior steady state, $g$ can be positive while decomposition and geological transfer balance it exactly, so that $\dot A = 0$. Gross uptake measures throughput or dependency; net depletion is a balance property. This false-implication record is the first rung of the taxonomy and governs every application below.

**Definition 4 (Local net-depletion ratio).**
$$H_A^{\mathrm{loc}}(t) = \frac{A(t) - A_{\min}}{\bigl[ -\dot A(t) \bigr]_+},$$
*with the extended-real convention $H_A^{\mathrm{loc}} = +\infty$ when $\dot A \ge 0$ — correctly reporting no current net decline at a stationary or replenishing state. The ratio is still not a trajectory forecast: it freezes the current net rate. If the fluxes change with $A$, policy, climate, prices, or other states, the realized threshold time can differ substantially.*

**Definition 5 (Scenario-conditioned hitting time).** *For a fully specified dynamical model, policy or scenario $\pi$, disturbance history $d$, and initial state $x_0$,*
$$T_A(x_0; \pi, d) = \inf\{ t \ge 0 : A^{\pi,d}(t; x_0) \le A_{\min} \},$$
*with $T_A = +\infty$ if the threshold is never reached. Under parameter, observation, and scenario uncertainty the appropriate output is a distribution or robust interval of $T_A$, not a single universal date.*

The three quantities answer different questions and must not share one depletion-horizon label:

| Quantity | Question answered |
|---|---|
| $J_A^{\mathrm{gross}}$, $H_A^{\mathrm{gross}}$ | How strongly does the system depend on, or turn over, the pool at the current gross rate? |
| $H_A^{\mathrm{loc}}$ | If the current net decline were frozen, what is the local stock-to-rate ratio? |
| $T_A$ | Under a stated model, policy, and disturbance scenario, when is the threshold first reached? |

### 6.2 Uniform-drift bounds

**Theorem 17 (Local threshold-horizon bracket).**
*Assume:*

*(H1) $A : [0,T] \to \mathbb{R}$ is absolutely continuous with $A(0) > A_{\min}$.*

*(H2) Constants $v_0 > 0$ and $0 < \varepsilon < 1$ are given; set $H_0 = (A(0) - A_{\min})/v_0$.*

*(H3) $T \ge H_0/(1-\varepsilon)$.*

*(H4) $(1-\varepsilon)v_0 \le -\dot A(t) \le (1+\varepsilon)v_0$ for almost every $t$ while $A$ stays above $A_{\min}$.*

*Then a first crossing time $H$ exists no later than $H_0/(1-\varepsilon)$, and*
$$\frac{H_0}{1+\varepsilon} \le H \le \frac{H_0}{1-\varepsilon}, \qquad |H - H_0| \le \frac{\varepsilon}{1-\varepsilon}H_0.$$

*Proof.* If no crossing occurs before $t_* = H_0/(1-\varepsilon)$, absolute continuity gives $A(t_*) \le A(0) - (1-\varepsilon)v_0 t_* = A_{\min}$, a contradiction; hence $H \le t_*$. Integrating both rate bounds over $[0,H]$ and using $A(0) - A(H) = v_0 H_0$ gives the two-sided bracket: from the upper rate bound, $v_0 H_0 \le (1+\varepsilon) v_0 H$, and from the lower rate bound, $v_0 H_0 \ge (1-\varepsilon) v_0 H$. □

This is a local diagnostic only: it fails when depletion reverses, the rate approaches zero, or feedback moves the trajectory outside the declared rate bounds. Its companion is the one-sided exhaustion theorem of Section 3.6, whose counterexample — proportional extraction never exhausts in finite time — shows that the uniform margin $\varepsilon > 0$ is load-bearing in both directions. The bracket bounds the frozen-rate ratio's error under declared rate bounds, and nothing more.

**When the clocks coincide.** Under the rate bracket the frozen-rate ratio and the true hitting time agree within the bracket: $-\dot A \in [(1-\varepsilon)v_0, (1+\varepsilon)v_0]$ gives $H_A^{\mathrm{loc}} = (A(0) - A_{\min})/[-\dot A]_+ \in [H_0/(1+\varepsilon), H_0/(1-\varepsilon)]$, hence $|H - H_A^{\mathrm{loc}}| \le 2\varepsilon H_0/(1-\varepsilon)$ — the only regime in which the frozen-rate ratio is a horizon. At a stationary state ($\dot A = 0$) with $g > 0$, $H_A^{\mathrm{loc}} = +\infty$ while $H_A^{\mathrm{gross}} < \infty$: the three quantities of Section 6.1 coincide only under a declared rate bracket, and the false implication $g > 0 \Rightarrow \dot A < 0$ is the reason.

### 6.3 Upper barriers, exit times, and maintainability

The lower-barrier setting of Section 6.1 is one half of the story. For each moiety $m$, define the lower and upper exit times
$$\tau_m^- = \inf\{ t \ge 0 : S_m(t) \le \underline{B}_m(t) \}, \qquad \tau_m^+ = \inf\{ t \ge 0 : S_m(t) \ge \overline{B}_m(t) \}, \qquad \inf\varnothing = \infty,$$
and the overall admissibility exit time
$$\tau_{\mathrm{exit}} = \min_m \{ \tau_m^-, \tau_m^+ \};$$
horizon safety on $[0,T]$ is $\tau_{\mathrm{exit}} > T$. Two disciplines attach. First, equality at the hitting time — $S_m(\tau_m^-) = \underline{B}_m(\tau_m^-)$ — requires continuity of both $S_m$ and $\underline{B}_m$ and appropriate initial separation; if fluxes or barriers can jump, the stock can cross the barrier without satisfying equality. Second, lower barriers need not be exhaustion thresholds: the diagnostic distinguishes physical exhaustion ($S_m = 0$), functional failure ($S_m = B_m^{\mathrm{func}}$), a resilience or regime-shift threshold, an economically recoverable reserve, and a minimum service-supporting stock — the term "exhaustion" is reserved for $S_m = 0$, and all other thresholds are barrier violations.

Upper-barrier violations matter symmetrically: a system may satisfy every lower-barrier condition while violating an upper barrier, $S_m(t) > \overline{B}_m(t)$. Atmospheric CO₂ accumulation violates an upper concentration barrier while fossil carbon stocks decline; the depletion diagnostic must check both barriers. And a stock can remain above a barrier until an assessment horizon $T$ and still be unsustainable thereafter: if the assessment claims sustainability rather than finite-horizon admissibility, it requires a terminal condition
$$x(T) \in K_{\mathrm{maint}},$$
where $K_{\mathrm{maint}} = \{ x : \exists \text{ an admissible continuation satisfying all barriers for } t \ge T \}$ — the set from which barrier safety is indefinitely maintainable, the viability kernel of the barrier set under the admissible controls (Aubin, 1991). The finite-horizon diagnostic is a necessary but not sufficient condition for sustainability; the full certificate requires the terminal state to lie in the maintainability set.

### 6.4 Robust semantics

For uncertain parameters $\theta \in \Theta$ and admissible disturbances $d \in \mathcal{D}$, robust barrier safety is
$$\mathrm{RobustBarrierSafe}(x(\cdot)) \iff \underline{B}_m(t) \le S_m(t; \theta, d) \le \overline{B}_m(t) \quad \forall m, \forall t, \forall \theta \in \Theta, \forall d \in \mathcal{D},$$
and the depletion-horizon classification is fourfold: nominal ($\theta = \theta_0$, $d = 0$); worst-case ($\inf_{\theta,d} \tau_{\mathrm{exit}}(\theta,d)$); probabilistic ($\Pr[\tau_{\mathrm{exit}} > T] \ge 1 - \varepsilon$); and scenario-conditioned ($\tau_{\mathrm{exit}} \mid \theta = \theta_s$). The componentwise diagnostic applies to each scenario, and the conjunctive criterion applies within each scenario and across scenarios. No single number is promoted across the four classes without a declared map.

### 6.5 Application classifications at their exact status

The classification matrix records, quantity by quantity, what each application computes and what each object is; the numerical exhibits that follow are worked instances of the constructions, and the classification of each row does not depend on the magnitudes.

| Time-like quantity | Question answered | G3P $L_{\mathrm{hist}}^{\mathrm{anom}}$ | Phosphate $T_{\mathrm{reserve}}$ | Fisheries $\Theta_F$ |
|---|---|---|---|---|
| $J_A^{\mathrm{gross}}$, $H_A^{\mathrm{gross}}$ | turnover / dependency | no | no | this (isolated gross loss) |
| $H_A^{\mathrm{loc}}$ | frozen net-rate ratio | no (anomaly, not stock) | no (classification, not stock) | no (no net $\dot B$) |
| $T_A$ | scenario hitting time | no | no | no |
| What it is | — | record-relative statistical index | arithmetic ratio of an economic class | removals-only pressure scale |

#### 6.5.1 Groundwater anomaly-persistence indices

The G3P column of the classification matrix is the groundwater case. The Global Gravity-based Groundwater Product (G3P v1.12; Güntner et al., 2024; the GRACE line it descends from is Tapley et al., 2004) provides monthly groundwater-storage anomalies relative to a reference period rather than absolute aquifer volumes. For a basin-mean anomaly series over the reported April 2002–September 2023 window, the linear-trend anomaly persistence index is
$$L_{\mathrm{hist}}^{\mathrm{anom}} = \frac{a_{\mathrm{latest}} - a_{\mathrm{hist,min}}}{\bigl[ -\widehat{\dot a} \bigr]_+},$$
the fitted distance to the series' own historical minimum divided by the fitted decline rate. The four-basin record: Indo-Gangetic $-49.7$ cm/yr with index $\approx 2.7$ yr; North China Plain $-18.6$ with $\approx 7.9$; Central Valley $-16.1$ with $\approx 9.5$; La Mancha $-3.2$ with $\approx 21.4$.

Classification, stated at the product's own status: a statistical anomaly index with units of time — not the physical stock ratio $H_A^{\mathrm{loc}}$ and not a forecast of aquifer exhaustion. Its value depends on the product window, basin mask, anomaly reference, and linear-trend convention; a physical $H_A^{\mathrm{loc}}$ requires an absolute stock estimate and a net stock derivative (aquifer geometry or saturated thickness together with storage parameters), not an anomaly series alone.

A structural point sharpens the boundary. The access structure — a well or an index well — is infrastructure rather than the resource: it draws on stored water, the stock, which is replenished by recharge, the flow. The anomaly series is a measure of the stored stock as observed at the access point; it measures neither the access infrastructure nor the recharge. An index built on it therefore cannot distinguish a drawdown of stored water that is recoverable on the recharge time scale from one that is not — although heavy over-extraction can make the loss permanent through compaction, subsidence, or saline intrusion, in which case it is not recoverable at all. The index is exactly the record-relative object analysed in Section 7.3, and its interpretive boundary is that record-relativity (Section 7.7).

#### 6.5.2 The applied depletion-horizon tables

Component-resolved depletion horizons on public data products are tabulated below, computed without fitting any dynamical parameter of the reduced systems:

| Basin | Trend (cm/yr) | 2023 anomaly (cm) | Window minimum (cm, implied) | Horizon to window minimum (yr) |
|---|---|---|---|---|
| Indo-Gangetic (N. India) | $-49.7$ | $-414$ | $-548$ | $\approx 2.7$ |
| North China Plain | $-18.6$ | $-145$ | $-292$ | $\approx 7.9$ |
| Central Valley (US) | $-16.1$ | $-84$ | $-237$ | $\approx 9.5$ |
| La Mancha (Spain) | $-3.2$ | $-20$ | $-88.5$ | $\approx 21.4$ |
| High Plains (US) | $-7.9$ | $-160$ | $-160$ | already at minimum |
| global mean | $-0.4$ | $-14$ | $-33.0$ | $\approx 47.6$ |

The basin rows are reported extractions from the G3P v1.12 basin series, used here only to exhibit the index construction of Section 6.5.1. The window-minimum column is implied by the displayed trend and horizon through the index formula of Section 6.5.1 — arithmetic, not product-endorsed — and every basin row must be re-derived from the product's basin masks before any numerical reuse. The Indo-Gangetic magnitude is the extreme case: it sits an order of magnitude beyond published basin-mean groundwater-equivalent trends (typically a few cm yr$^{-1}$), and a linear trend of $-49.7$ cm yr$^{-1}$ maintained over the reported $\approx 21.4$ yr window would place the fitted 2002 value near $+6.5$ m above the anomaly reference — the fitted segment convention is part of the quarantine. The rows are retained only as the worked instance of the index construction, and the classification status assigned below does not depend on the magnitudes.

| Country | Reserves (kt) | Reserve-life horizon (yr) | Implied production (kt/yr) |
|---|---|---|---|
| China | $3{,}400{,}000$ | $\approx 28$ | $121{,}429$ |
| United States | $1{,}000{,}000$ | $\approx 45$ | $22{,}222$ |
| Jordan | $820{,}000$ | $\approx 62$ | $13{,}226$ |
| Morocco | $50{,}000{,}000$ | $\approx 1{,}250$ | $40{,}000$ |
| Australia | $5{,}800{,}000$ | $\approx 2{,}088$ | $2{,}778$ |
| World (reserves) | $74{,}000{,}000$ | $\approx 309$ | $239{,}482$ |
| World (resources, $\varepsilon = 0.10$) | $>300{,}000{,}000$ | $>1{,}125$ | $240{,}000$ |

The fisheries column reports the pure-decay proxy $\mathrm{ADH} = F^{-1}\log(\mathrm{SSB}_{\mathrm{now}}/(0.2\max\mathrm{SSB}))$ under current $F$, with median $\approx 1.8$ yr across the 43 assessed stocks with finite SSB and $F$ series, computed with $\mathrm{ADH} = 0$ entered for the eight stocks already at or below the reference — the zero convention of the source table's caption, which the median includes. The qualifying positive sub-cohort ($F > 0$ and $\mathrm{SSB}_{\mathrm{now}} > B_{\lim}$; 35 stocks) has median $2.9$ yr; both medians come from the archived pull alone. The cohort is a selected class, not a random sample of assessed stocks: all 43 stocks are small pelagics (18 anchovy, 20 herring, 4 sprat, 1 sardine), the fast-maturing class the companion review screen selects by its annual-review eligibility criterion (42 of the 43 are that screen's annual-managed spectral-null stocks, per the source caption). The $\approx 1.8$ yr median is therefore a class-specific diagnostic for fast-maturing, annually managed pelagics, not a statistic of assessed fisheries in general; the executed broad-cohort comparison (S5) runs the same protocol on the full public release — 454 stocks, median $3.39$ yr, the upper end carried by the long-lived groups (elasmobranchs $11.5$, sebastids $9.0$, pleuronectids $6.0$ yr) — and only $2\%$ of random 43-stock draws from that broad cohort have medians at or below the class cohort's $1.79$ yr. The extract is the RAM Legacy cohort of Ricard et al. (2012), and the pull date is archived in the analysis repository; the archived pull has been re-verified row by row against the formula — all 43 rows reproduce $\mathrm{ADH} = \max(0,\, F^{-1}\log(\mathrm{SSB}/B_{\lim}))$ with $B_{\lim} = 0.2 \max \mathrm{SSB}$. The value is reported with its cohort conditions and is not promoted to a forecast. Because cohort composition is database-version-dependent, every cohort statistic is pinned to the archived pull: the quartile summary of $F$ and $\log(\mathrm{SSB}/B_{\lim})$ over the cohort belongs to that pull alone, and no cohort statistic is quoted from a different database version. The cohort protocol is fully specified in the accompanying supplementary material (S5) — including the zero entries for stocks at or below the reference, which enter the median — together with the version-sensitivity record: on the public RAM Legacy releases the same protocol qualifies 415 stocks (v4.44, median $2.57$ yr) and 454 (v4.66, median $3.39$ yr) — both reproduced to printed precision under the recovered micro-specification (S5) — neither reproducing the archived 43-stock cohort — the archived pull's 43-stock list and extract-time series state, now supplied and re-verified, differ from both public releases.

The scope discipline is the tables' load-bearing content: none of the reported numbers is a computed instance of any model's first-hitting time — the groundwater column is a trend-to-window-minimum extrapolation, the phosphate column a reserve-life ratio, and the fisheries column a pure-decay proxy with recruitment omitted. They are descriptive, component-resolved diagnostics in the two-pool logic of the taxonomy, not dynamical predictions. The equal-weight inverse-horizon score of the four basins still above their window minimum and world phosphate reserves, displayed as **Non-example 1** — a deliberate boundary of aggregation, not a score of the framework,
$$\Sigma_{\mathrm{reserves}} \approx \frac{1}{5}\left( \frac{1}{2.7} + \frac{1}{7.9} + \frac{1}{9.5} + \frac{1}{21.4} + \frac{1}{309} \right) \approx 0.130\ \mathrm{yr}^{-1},$$
is a ranking device, not a componentwise certificate: it mixes basins and reserves, incommensurable objects under the typing of Section 2.1, and is retained only to mark the boundary of legitimate aggregation. The score is exhibited here as the worked instance of the noncompensation boundary of Section 10.1: a positive aggregate coexisting with componentwise deficits by construction — admissible as communication, inadmissible as certification.

#### 6.5.3 The phosphate reserve-life ratio

The phosphate column of the classification matrix is the reserve-life ratio. At constant current production $C_G$, the reserve-life ratio is $T_{\mathrm{reserve}} = G_{\mathrm{reserve}}/C_G$; at approximately $74{,}000$ Mt of world reserves and $240{,}000$ kt/yr of production (U.S. Geological Survey, 2026) this is approximately $309$ years. The arithmetic is internally consistent as a reserve-life ratio to zero; it is not a physical exhaustion forecast, because reserve classification changes with prices, technology, exploration, and regulation — the point made independently, and forcefully, by Illakwahhi, Vegi, and Srivastava (2024) for the single-source USGS data behind the influential phosphate depletion estimates, and standard in mineral economics, where reserves have grown through a century of rising production for copper (Tilton, 2003; Tilton and Lagos, 2007). The reserves/resources split discipline is part of the classification: a resource-threshold calculation $T_{\mathrm{resource},10\%} = 0.9\, G_{\mathrm{resource}}/C_G$ answers a different question and must not share a column with the reserve-life ratio without an explicit convention label; the reserve classification is economic — US reserves have remained near $1{,}000{,}000$ kt while cumulative production since 1996 is of order $600{,}000$ kt — and the resource-based world horizon ($\approx 1{,}125$ yr at $\varepsilon = 0.10$) is more than three times the reserve-based figure ($\approx 309$ yr); the two-compartment split is what prevents these from being collapsed into one number. The implied-production column of the Section 6.5.2 table reproduces the production figure each horizon assumes (production = reserves/horizon) and thereby exposes the source arithmetic; the country horizons reproduce the recorded MCS-vintage ratios, and re-pinning every row to the single MCS 2026 vintage — whose 2025 world production column reads $\approx 250{,}000$ kt — is a registered revision requirement. MCS 2026 reports Australia's reserves as $120{,}000$ kt (JORC-compliant; the main table leaves that cell blank), so the displayed pre-2026 Australian row is quarantined pending the re-pin.

#### 6.5.4 The fisheries removals-only pressure time

The fisheries column of the classification matrix is the removals-only pressure time. When $\mathrm{SSB}_{\mathrm{now}} > B_{\lim} > 0$ and $F_{\mathrm{now}} > 0$, define $R_B = \log(\mathrm{SSB}_{\mathrm{now}}/B_{\lim})$ and
$$\Theta_F = \frac{R_B}{F_{\mathrm{now}}},$$
the fishing-only time-to-reference: the crossing time of the deliberately incomplete comparison process $\dot B = -F_{\mathrm{now}}B$. With $B_{\lim} = 0.2 \max \mathrm{SSB}$ this is the construction tabled as ADH in Section 6.5.2; the two notations are kept because the boundary hypotheses stated here ($F_{\mathrm{now}} > 0$, $\mathrm{SSB}_{\mathrm{now}} > B_{\lim}$) are exactly the conditions of the positive sub-cohort of Section 6.5.2 (35 stocks, median $2.9$ yr); the reported Section 6.5.2 median ($\approx 1.8$ yr) additionally carries the eight zero entries for stocks at or below the reference, per the zero convention of the source caption. It is a removals-only pressure time scale — the time unit comes from rescaling a stock-reference margin by one isolated gross-loss rate. Because recruitment, somatic growth, maturation, natural mortality, density dependence, environmental forcing, and future policy are omitted, $\Theta_F$ is not a net biomass depletion diagnostic, not a demographic hitting-time estimate, and not a member of the $J^{\mathrm{gross}}$–$H^{\mathrm{loc}}$–$T_A$ hierarchy. A genuinely local biomass-decline ratio $H_B^{\mathrm{loc}} = (B - B_{\lim})/[-\dot B]_+$ would require a compatible net $\dot B$ estimate, and a demographic hitting time a fully specified population model; RAM Legacy SSB and $F$ data (Ricard et al., 2012) do not by themselves supply these quantities or models. Spawning biomass is not an abiotic support pool. The construction is retained specifically to show why an isolated gross-removal time scale must not be promoted to a net depletion diagnostic.

The collective implication for material-flows measurement is that the three published "depletion time" numbers — G3P index, phosphate reserve-life, fisheries removals-only time — answer three distinct questions at three distinct evidentiary levels. Stating them with those questions is what makes them usable; collapsing them into one "time to depletion" is what makes them false.

---

## 7. First-Passage Semantics on Declared Surrogates

### 7.1 Two objects, not one

The ledger's own first-passage object is the model hitting time of Definition 5 — a quantity on trajectories of the mass-conserved ledger or of a named reduced system. The public-data quantities of Section 6.5 are constructed proxies on observed series. The distinction is the entry discipline of this section: the surrogates below do not compute the ledger's hitting time, do not complete the ledger stochastically, and do not identify physical failure thresholds.

### 7.2 The observed-drift Brownian surrogate

**Definition 6 (Observed-drift Brownian surrogate).** *Let $A_0$ be the latest observed anomaly and $\mu = \widehat\mu < 0$ the fitted drawdown rate. On the scale of the tabulated series define*
$$A(t) = A_0 + \mu t + \varsigma W_t, \qquad A(0) = A_0 > A_{\min}^{\mathrm{win}},$$
*where $W$ is a standard Wiener process, $\varsigma > 0$ a chosen noise scale, and the process is stopped at first reaching the record-relative barrier $A_{\min}^{\mathrm{win}}$.*

This is a statistical surrogate for the empirical trend extrapolation. It is not a hydrological constitutive law, is not mass-conserving, and is not a perturbation or stochastic completion of the ledger's active-pool equation or of the finite-donor primitive system of Section 2.2. The non-completion non-claim is part of the definition.

### 7.3 The inverse-Gaussian groundwater first passage

**Theorem 18 (Inverse-Gaussian first passage).** *Let $T_{\mathrm{GW}} = \inf\{ t > 0 : A(t) \le A_{\min}^{\mathrm{win}} \}$ for the process of Definition 6 and $d = A_0 - A_{\min}^{\mathrm{win}} > 0$. Conditional on treating $\mu$ and the barrier as fixed,*
$$T_{\mathrm{GW}} \sim \mathrm{IG}(\nu, \lambda), \qquad \nu = \frac{d}{|\mu|}, \qquad \lambda = \frac{d^2}{\varsigma^2},$$
*in the mean–shape parameterization; in particular $\mathbb{E}[T_{\mathrm{GW}}] = \nu = H^{\mathrm{win}}_{\mathrm{GW}}$ and $\operatorname{Var}(T_{\mathrm{GW}}) = \nu^3/\lambda = d\,\varsigma^2/|\mu|^3$.*

*Proof.* The first-passage time of a Brownian motion with constant negative drift to a lower barrier is inverse Gaussian — the classical first-passage result (Chhikara and Folks, 1989; Redner, 2001) — with the stated mean and shape parameters; the standard inverse-Gaussian moments give the displayed mean and variance. □

The mean of the stochastic surrogate equals the deterministic trend-to-window-minimum ratio of Section 6.5.1; that equality is the precise sense in which the tabled groundwater numbers are first-passage means of a declared surrogate.

**Corollary 19 (Zero-noise limit and median).** *As $\varsigma \to 0^+$, $T_{\mathrm{GW}} \to H^{\mathrm{win}}_{\mathrm{GW}}$ in probability, and at $\varsigma = 0$ the deterministic trajectory reaches the barrier exactly there. For every finite $\varsigma > 0$ the inverse-Gaussian median $m$ satisfies*
$$m < \nu = H^{\mathrm{win}}_{\mathrm{GW}}, \qquad F_T(\nu) = \frac{1}{2} + e^{2\lambda/\nu}\,\Phi\!\left( -2\sqrt{\lambda/\nu} \right) > \frac{1}{2}.$$
*The variance scales as $\varsigma^2$ and the standard deviation and small-noise quantile widths as $\varsigma$. The median below the mean is the inverse Gaussian's right skew toward short passage times; the inequality must not be inverted.*

*Proof.* Evaluate the inverse-Gaussian CDF $F_T(t) = \Phi(\sqrt{\lambda/t}(t/\nu - 1)) + e^{2\lambda/\nu}\Phi(-\sqrt{\lambda/t}(t/\nu + 1))$ at $t = \nu$: the first term is $\Phi(0) = 1/2$ and the second is strictly positive for finite $\lambda$, so the median lies strictly below the mean; the concentration statement follows from the variance. □

These are conditional distributional statements about the surrogate. They are not corrections to the tabled years, and they do not show that physical water mass is depleted faster.

### 7.4 The record-relative barrier discipline

The barrier $A_{\min}^{\mathrm{win}}$ is selected from the same finite observation window used to estimate $\widehat\mu$. It is therefore a path-dependent, record-relative threshold, not an independently identified hydrological failure floor; future passage below it represents a record-breaking stress event under the surrogate, not physical exhaustion. Three boundary facts complete the discipline.

1. **Already-at-minimum.** If $A_0 = A_{\min}^{\mathrm{win}}$, the stopping-time convention gives $T_{\mathrm{GW}} = 0$ deterministically for every $\varsigma$; the inverse-Gaussian family has a degenerate boundary limit concentrated at zero, and $\mathrm{IG}(0,0)$ is not an ordinary inverse-Gaussian distribution. Zero cells report zero relative to the selected observational barrier — not zero physical uncertainty and no confirmation of collapse.
2. **Independent physical thresholds.** If an independent physical threshold $A^\sharp < A_{\min}^{\mathrm{win}}$ is specified, the same constant-drift surrogate gives the conditional mean $\mathbb{E}[T^\sharp] = (A_0 - A^\sharp)/|\mu|$, longer than the record-relative proxy because the barrier is lower. This is a statement within the surrogate, not a general lower-bound theorem for the physical ledger, whose drift and state coupling may differ.
3. **Classification.** The load-bearing content is the interpretation boundary itself: a record-relative barrier makes the passage time a property of the observation window, and no reading of the tabled numbers escapes that qualification.

### 7.5 The geometric-Brownian fisheries first passage

**Theorem 20 (Geometric-Brownian correction).** *Let $dB_t = -hB_t\, dt + \varsigma B_t\, dW_t$ under the Itô convention with $h > 0$ and $0 < B_{\min} < B_0$, and $T_{\mathrm{fish}} = \inf\{ t > 0 : B_t \le B_{\min} \}$. Then*
$$T_{\mathrm{fish}} \sim \mathrm{IG}(\nu_F, \lambda_F), \qquad \nu_F = \frac{\log(B_0/B_{\min})}{h + \varsigma^2/2}, \qquad \lambda_F = \frac{\log(B_0/B_{\min})^2}{\varsigma^2},$$
*so $\mathbb{E}[T_{\mathrm{fish}}] = \log(B_0/B_{\min})/(h + \varsigma^2/2)$; as $\varsigma \to 0^+$ this converges to the deterministic pure-decay horizon when $h = F$ and $B_{\min} = B_{\lim}$.*

*Proof.* Itô's lemma (Øksendal, 2003) gives $d\log B_t = -(h + \varsigma^2/2)\, dt + \varsigma\, dW_t$, so the logarithmic threshold is a Brownian first-passage problem with initial distance $\log(B_0/B_{\min})$ and downward drift $h + \varsigma^2/2$; Theorem 18 applies. Under the Stratonovich convention the log-drift would be $-h$ and the deterministic limit would match the pure-decay horizon $h = F$ exactly: the $\varsigma^2/2$ shortening is the Itô choice, not a property of the physical process. □

For fixed arithmetic drift and the Itô parameterization, the finite-noise mean is strictly shorter than the deterministic horizon. This is a property of the chosen surrogate parameterization; it is not a universal claim that environmental variability accelerates physical biomass loss. The construction joins the removals-only classification of Section 6.5.4 — the same pure-decay process, now under a declared stochastic surrogate.

### 7.6 The constant-production phosphate passage time

Under the deterministic surrogate $\dot G = -P$ with constant production $P > 0$, the first-passage time to a fixed threshold $G_{\min} \in [0, G_0)$ is
$$T_{\mathrm{phos}} = \frac{G_0 - G_{\min}}{P},$$
the reserve-life ratio being the $G_{\min} = 0$ special case and a threshold fraction $\varepsilon G_0$ giving $(1-\varepsilon)G_0/P$. This is a conditional reserve-classification proxy under constant production; because reserves are an economic classification rather than a fixed physical stock, it is not a forecast of geological exhaustion without an explicit resource and production model. No stochastic phosphate extension is required for the interpretation.

### 7.7 The explicit non-claims

The first-passage semantics close with seven explicit non-claims, all of which hold in this article:

1. The Brownian and geometric-Brownian processes are not stochastic completions of the ledger and do not conserve its mass compartments.
2. No theorem relates $\widehat\mu$ to $-\dot A$ of the reduced systems, to the finite-donor primitive system, or to the institutional delay equations.
3. The model hitting time $T_A$ of Definition 5 is not shown to be inverse Gaussian: it would be inverse Gaussian only if the active-pool residual were Brownian with constant drift, which the coupled balance (2) does not supply — the tabled groundwater numbers inherit inverse-Gaussian means from Definition 6's surrogate and from nothing else.
4. The historical groundwater minimum is not an independently identified physical failure barrier.
5. A shorter surrogate median or Itô mean is not evidence of faster physical depletion.
6. The gross active-pool horizon $H_A^{\mathrm{gross}}$ of Definition 3 and its productivity-illusion interpretation — the misreading of a large gross-turnover horizon as evidence of slow net depletion, the false implication recorded in Section 6.1 — are not first-passage results treated here.
7. The fisheries calculation is not a stage-structured fisheries model, and the phosphate calculation is not a geological-reserve model.

### 7.8 Parameter and observation uncertainty

The inverse-Gaussian results condition on the drift, barrier, and noise scale. In the groundwater application $\widehat\mu$ is estimated from a finite, potentially autocorrelated record and the barrier is selected from that same record; measurement error, serial dependence, seasonal forcing, spatial aggregation, trend breaks, and common climatic drivers are separate uncertainties, and integrating any of them out yields a predictive mixture rather than a single inverse-Gaussian law. A residual scale estimated from the same window does not by itself identify process noise. No calibrated predictive distribution is claimed; the full uncertainty treatment belongs to an empirical identification study, not to this article. For industrial-ecology measurement this discipline is the practical message: first-passage distributions on declared surrogates are usable as descriptive statistics, but their drift, barrier, and noise inputs each carry their own identification story, and a calibrated forecast requires that story to be discharged.

---

## 8. Domain Templates at Registered Status

### 8.1 The phosphorus template

The phosphorus domain enters at registered template status: an identification ladder for the resource–product–waste–detritus structure of Section 2.3 (phosphate rock → fertilizer → soil pool → runoff, with the mining flux $c_G$ and the recycling routes $\alpha, \rho$), whose constitutive content — the yield and loss functions, the recovery fractions, the price response of the reserve classification — is declared, not established. The reserve and production quantities used in Section 6.5.3 carry their source vintage (U.S. Geological Survey, 2026); the template's competing-model ladder is an identification object, and its falsification protocols (which observation would reject which routing assumption) are recorded obligations, not results.

### 8.2 The groundwater template and the two-pool gap

The groundwater template enters at registered status with an admitted object and a declared gap. The admitted object is the one-pool affine approximation behind the anomaly-persistence index of Section 6.5.1; the two-pool model (active storage with a slow donor pool, the two-compartment structure of Section 2.2) is not established. The registered identification requirements for closing the gap are: geological geometry (aquitard depth and extent); multi-depth heads; pumping tests; tracer, isotope, or water-age evidence; recharge estimates; prior ranges for the storage and fast-slow coupling parameters; and the discipline that leakage terms may not absorb unexplained residuals.

### 8.3 Extractor-side harvest economics

On the extractor side, the same discipline applies to economic steady states. In the open-access equilibrium of a single-species fishery (Clark, 1990), the bioeconomic equilibrium stock $S_{\mathrm{OA}} = c/(pq)$ is set by cost, price, and catchability — and is infeasible as a management target under a conservation floor $S_{\min} > S_{\mathrm{OA}}$: the unregulated equilibrium lies below the floor, and no open-access trajectory is viable against it. The modified golden rule in its constant-unit-cost form, $g'(S_\delta) = \delta$, sets the optimal steady stock for the discount rate $\delta$ (Clark's general form carries an additional marginal-stock-effect term); a harvest tax shifts the open-access equilibrium to $S_{\mathrm{OA}} = c/((p - \tau)q)$ — the tax moves the economic equilibrium, but it does not move the physical floor. The distinction is the extractor-side counterpart of the accounting discipline of Section 6: instrument parameters and constraint thresholds are different objects, and no tax schedule substitutes for a constraint the ledger must satisfy. The growth function $g$ of this paragraph is a declared constitutive readout on the stock for this extractor-side remark only; it is not a primitive of the closed natural block of Section 2, and nothing in this section is promoted into the typed ledger.

---

## 9. The Interface with Institutional Delay Dynamics

The partition between this article and the companion delay-dynamics analysis is fixed by an interface contract. This article owns the closed material accounting: the primitive ledger equations and full routing, the conservation and positivity theorems of Section 4, the componentwise deficit and depletion diagnostics of Sections 5–6, and the closed-donor no-rest and extraction-integrability limitations. The companion owns the open frozen-donor retarded systems and their bifurcation results. The interface is viable, but not because the closed primitive ledger dynamically reduces to the open working system: the two are different completions, and the contract records both the exact shared object and the rejected mapping.

**The exact shared object.** Under the single-resource specialization of Section 5.4 ($\mu = \nu = \rho = 0$, the macroeconomic-feedback, recycling, and mining channels switched off, and $C^A = 0$) — with the local stock equation $\dot N = R - qEN$, the deficit identity
$$D(t) := qE(t)N(t) - R(N(t), A(t)) = -\dot N(t), \qquad \Lambda(t) := [D(t)]_+ = [-\dot N(t)]_+$$
holds for every trajectory of either the specialized ledger or the reduced core (Lemma 16). The identity is the one object both analyses may use without substantive duplication; the reduced core's constitutive replacement $R(N,A) \to rN(1 - N/K)$ is separately an approximation and carries its own finite-time scope (Theorems 1–2: the replacement is pointwise on the interior support region and non-uniform through the depleted-pool boundary). The contract fixes more than the deficit identity: the shared object includes the nonnegative orthant and the sign pattern of harvest as an outflow from the living stock — a companion model that routes the "unsustainable portion" of a flow into a different compartment changes the incidence and thereby leaves the interface (Section 2.5).

**The hand-off projection.** Under the institutional-failure specialization, the macroeconomic block, prices, and demand do not appear in $(\dot N, \dot A, \dot U, \dot Z, \dot E)$: each of the five right-hand sides depends only on the block's own variables and the delayed memory, and none contains the macroeconomic states, prices, or demand. The ecological–institutional subsystem is an exact closed projection for every parameter value, with no singular limit required. The memory–effort pair $(Z, E)$ is the gated three-state core and working four-state core of the companion delay-dynamics analysis (under review; eq. (1) and Section 2.4 of that analysis), not an object of this article; the projection claim — the semiconjugacy condition $D\pi(\xi) f(\xi) = F(\pi(\xi))$ on the history phase space — is made under that citation and is not re-proved here.

**The non-reduction boundary.** There is no exact dynamic reduction from the closed primitive finite-donor ledger to the open working system — not as a projectable reduction and not as a regular perturbation. The reasons are mathematical:

1. The primitive ledger uses the intrinsic donor-limited target $A^{\mathrm{eq,intrinsic}}$; the working system uses the derived target $A^{\mathrm{eq,W}} = A^{\mathrm{eq,intrinsic}} + \kappa_A K/\omega_A$. The three registered numbers display the separation: $A^{\mathrm{eq,intrinsic}} = 50$, the working active pool $A^{\mathrm{act,*}} = 397.87$, and $A^{\mathrm{eq,W}} = 50 + \kappa_A K/\omega_A = 5050$ — the two equilibria differ by a factor of eight and the two targets by two orders of magnitude.
2. At the working equilibrium the two $A^{\mathrm{act}}$ vector fields differ by an $O(1)$ term — in fact by $B^* - R^* = T^* \approx 4.47$ stock units per year, the gross uptake at the working point, not a small residual.
3. The working point requires continuing geological support — the flux $\omega_A(A^{\mathrm{eq,W}} - A^{\mathrm{act,*}}) = 4.652133\ldots$ stock units per year, supplied every year by a donor the working system treats as a parameter — and is not a rest point of the closed finite-donor system (Theorem 12). At the same state the closed primitive donor flow is $e_{GA} - e_{AG} = \omega_A(A^{\mathrm{eq,intrinsic}} - A^{\mathrm{act,*}}) \approx -0.348$: the donor gains in the closed ledger where the working completion has it losing $4.652$ — the two fields have opposite signs on the donor coordinate, not merely different magnitudes. The working-point figures $E^* \approx 2.090$, $N^* = 89.526$, $A^{\mathrm{act,*}} = 397.87$, and the recharge $4.652$ are imported at the companion's registered precision; the reverse check $qE^*N^* = 0.001 \times 2.090 \times 89.526 \approx 0.187$ is consistent to the quoted digits.
4. The cumulative donor-draw quantity $\varepsilon_G(T) = G_0^{-1}\int_0^T |e_{GA} - e_{AG}|\, dt$ is a diagnostic of the derived-target completion, not a trajectory-tracking error between the two fields; no finite-time tracking theorem between the completions holds.
5. The closed primitive system makes sustained extraction integrable (Theorem 14) and therefore cannot possess the working positive-flux rest indefinitely.

The five reasons form a trichotomy: (1)–(3) are short-time obstructions — the two $A^{\mathrm{act}}$ fields differ by $O(\kappa_A K) = O(5)$ at the working point, and trajectories of the two systems diverge on $O(1)$ time scales; (5) is the long-time obstruction — extraction on the closed ledger is $L^1$ in time (Theorem 14); (4) is neither — $\varepsilon_G$ is not a tracking error between the two fields at any time scale. Collectively:

**Theorem (Non-reduction of the open working completion).** *There is no exact dynamic reduction, no regular perturbation, and no finite-time tracking correspondence from the closed primitive ledger (2) to the open working system, because (i) the targets differ by $\kappa_A K/\omega_A = 5{,}000$ stock units (structural); (ii) the $A^{\mathrm{act}}$ fields differ by $O(1)$ at the working point (short-time); (iii) the working point is not a rest point of (2) (Theorem 12; equilibrium); (iv) $\varepsilon_G$ is not a tracking metric (diagnostic misuse); and (v) extraction on (2) is $L^1$ in time (Theorem 14; long-time).*

The mapping type for exact dynamic reduction is rejected; the permitted relation is analogy for shared mechanism language plus diagnostic reconstruction of omitted mass flows. The companion's global periodic results are properties of its reduced systems and do not transfer to the closed primitive ledger; in particular, Hopf or periodic orbits of the frozen-donor working system are not properties of (2). In the other direction, the working system is an open projection: omitted turnover is routed to a diagnostic detritus or inert sink, imposed recharge corresponds to geological draw, and the reduced trajectory's mass discrepancy is reconstructible from the omitted flows.

**The frozen-donor limit is a corollary of the structural clause (i).** Rescaling the donor as $G = G_0 g$ with $g(0) = 1$ gives $\dot g = -G_0^{-1}(e_{GA} - e_{AG})$. The limit $G_0 \to \infty$ freezes $g$ but does not restore the working completion's derived target: the limiting recharge field still uses $A^{\mathrm{eq,intrinsic}}$, not $A^{\mathrm{eq,W}}$, so the scaling is not a regular perturbation of the working vector field. Local Hopf persistence of the working system under this primitive scaling is not claimed; a different derived-target completion would be required before a regular-perturbation theorem could be formulated.

**The long-time finite-budget interpretation.** With the donor $G(t)$ included as a state, the closed system is an autonomous retarded equation with a slow donor coordinate. The companion's $\tau_+ \approx 150$ yr upper cycle is a frozen-donor object; on the closed system it can persist only as a transient on the finite donor budget. The transient-duration statement is an order/budget bound, not an asymptotic estimate: under a sustained lower extraction flux $c > 0$ the duration is bounded above by $G_0/c$. The scale must name its flux: at the closed-block extraction rate $c = qE^*N^* \approx 0.187$ yr$^{-1}$ the budget bound is $G_0/c \approx 2 \times 10^6$ years, while at the working completion's recharge flux $B^* \approx 4.652$ yr$^{-1}$ the draw scale is $G_0/B^* \approx 8.6 \times 10^4$ years — the "tens of thousands of years" heuristic uses the working flux (at $G_0/A^{\mathrm{act}*} = 10^3$), and both scales sit far above the institutional delays of the companion family. Whether the frozen-donor local Hopf structure persists as a slowly drifting transient in the closed donor system is an open slow-passage problem; the mass budget alone does not establish it. The implication for industrial-ecology coupling is concrete: a closed physical ledger and an open working system can share one diagnostic identity without sharing a dynamics, and the temptation to import one system's theorems into the other must be resisted.

---

## 10. What the Ledger Does Not Support

### 10.1 Compensatory aggregation is rejected, not merely discouraged

On the unreduced ledger, no scalar weighting of components is authorized by the accounting itself. The precise statement is on the feasible balance domain (Definition 1): a weighted sum $\sum_m w_m s_m$ certifies componentwise adequacy $s_m \ge d_m$ for all $m$ on $\mathcal{B}(x,t)$ only through an implication proved from the physical restrictions defining the domain — and, in general, no such implication holds. The feasible domain can admit vectors with a positive aggregate and a negative component, exactly the geometry documented in the composite-indicator literature (Munda and Nardo, 2009). In short, a positive weighted sum never certifies componentwise nonnegativity; scalar summaries may rank and communicate, but certification requires the vector.

**Proposition (No weighted certification).** *Let $\mathcal{B}(x,t)$ be the feasible balance domain (Definition 1). If $\mathcal{B}(x,t)$ contains a vector with $b_i < 0$ and $w^\top b > 0$ for a fixed $w \ge 0$, then the certificate $\{w^\top b \ge 0\}$ does not imply $b \ge 0$; if $\mathcal{B}(x,t)$ is not known to exclude that pattern, no nonnegative weighting is authorized as a componentwise certificate.*

*Proof.* On the exhibited vector the componentwise predicate fails ($b_i < 0$) while the weighted predicate holds ($w^\top b > 0$); the two predicates differ on $\mathcal{B}(x,t)$. The inverse-horizon score of Section 6.5.2 (Non-example 1) is the worked witness: a positive aggregate coexisting with componentwise deficits by construction. □

The conditional form is not an accident of a particular domain: the compensating pattern is constructible against *any* weight, so the failure is universal to the method of weighted certification.

**Theorem (Universal failure of weighted certification).** *Let the ledger have $m \ge 2$ components. For every weight vector $w \in \mathbb{R}_+^m$, $w \neq 0$, there exist a typed ledger as in Section 2, a demand vector $d$, and an admissible state–operation pair $(x, u)$ with $u \in \mathcal{U}(x,t)$ whose attainable balance $b = \mathcal{O}(x,u,\theta) - d$ satisfies $w^\top b \ge 0$ while $b_m < 0$ for some component $m$. No nonnegative weighting is therefore a valid componentwise certificate in general.*

*Proof.* Take the two-compartment ledger with stock $x = (x_1, x_2) \in \mathbb{R}^2_+$, one donor-limited transfer flux $f = kx_1$ from compartment 1 to compartment 2 ($k > 0$), identity readout $\mathcal{O}(x, u, \theta) = x$, and demands $d = (d_1, d_2)$. Every nonnegative state is admissible with the declared flux, because donor limitation holds ($f = 0$ at $x_1 = 0$), so the balance $b = x - d$ is attainable for every $x \in \mathbb{R}^2_+$; the admissible operating set is the flux declaration itself. Fix $w$ and let $j$ be an index with $w_j > 0$. If some $m \neq j$ has $w_m = 0$, place the deficit there: choose $x_m < d_m$ and $x_j \ge d_j$, giving $w^\top b = w_j (x_j - d_j) \ge 0$ while $b_m < 0$. Otherwise $w_m > 0$ for every $m \neq j$: choose any $m \neq j$ with $x_m < d_m$, and choose $x_j \ge d_j + \bigl( w_m (d_m - x_m) + \varepsilon \bigr)/w_j$ for any $\varepsilon > 0$. Then
$$w^\top b = w_m (x_m - d_m) + w_j (x_j - d_j) \ge w_m (x_m - d_m) + w_m (d_m - x_m) + \varepsilon = \varepsilon \ge 0,$$
while $b_m = x_m - d_m < 0$. The pair $(x, d)$ is the witness for $w$. □

The construction never uses the dynamics: the failure is a property of nonnegative weightings over mixed-sign balances, not of the donor-limited positivity mechanism. Consequently, on any feasible balance domain containing a compensating pair — and Definition 1's domain is exactly that whenever the operating set admits states with mixed balances — no nonnegative weighting can stand in for the conjunctive criterion of Section 3.2. The reading is the algebraic form of the weak-comparability thesis stated in Section 1.1: scalar summaries may rank and communicate, but certification requires the vector.

The companion assessment analysis proves the dynamic form of the same separation for transition operators; the ledger side contributes the static prerequisite: the aggregation question is only well posed after the balance domain is declared, and the burden of proof sits on the aggregation, not on the componentwise report. The same separation holds at the service layer: a weighted sum on $\mathcal{B}(x,t)$ cannot see the directional support gap $(1 - \alpha_{\mathrm{reg}})\bar s$ of Definition 2 — an aggregate that mixes regenerative and non-regenerative provenance never reports which component carries the gap. In the terms of the ecological-economics literature of Section 1.1, componentwise adequacy on the typed ledger is strong sustainability as a conjunctive predicate; a positive weighted sum is weak sustainability as a ranking device. The ledger authorizes the first and does not authorize the second.

### 10.2 The double-counting discipline

Five rules, each carried by a proved or defined statement of this article, jointly prevent double counting and phantom mass:

1. **One balance per moiety.** Conservation laws attach to declared moieties (Theorems 7–8); adding unlike units — biomass, money, biodiversity indices, exergy — into one conserved scalar is not authorized by any conservation theorem.
2. **Explicit stoichiometry.** Entries are added within an incidence row only when their types and units agree; every conversion is an explicit coefficient in $S_{\mathcal{T}}$, never an implicit sum (Section 2.1).
3. **Yield routing.** A transformation represented with yield below one must route the omitted fraction to a represented compartment or a declared boundary flow; otherwise the moiety balance holds only after silently dropping the moiety (Theorem 15).
4. **No ghost sinks.** Every primitive with an outflow from some compartment must have its routed inflow represented, and every inflow its source — opposite-sign incidence of the same primitive is checkable column by column — and the six-state cancellation of Section 4.9 shows the check passing, while the same template shows that cancellation without donor-limited admissibility establishes nothing.
5. **Classification labels stay out of the columns.** Reserve-life and resource-threshold quantities answer different questions and share a column only under an explicit convention label (Section 6.5.3); diagnostic labels never determine material routing (Section 2.5).

Every unit of mass is routed once: the unit-sum split routing of Theorem 8 and the column-sum-zero incidence of Theorem 9 are the mechanism, and the yield-routing obligation of Theorem 15 is its enforcement. A flux omitted from the ledger is not thereby conserved; a recovery claimed in a quality-neutral loop is not thereby real; and a diagnostic index that mixes basins and reserves (the ranking device of Section 6.5.2) is identified as such in the text that reports it. Double counting is a representation error, and the representation that prevents it is the contribution.

### 10.3 Negative and boundary content is first-class

The classification results of Section 6.5 are negative results stated as such: the anomaly index is not a stock ratio; the reserve-life ratio is not a forecast; the removals-only time is not a depletion diagnostic. The non-reduction boundary of Section 9 is a rejected mapping with five mathematical reasons. The sink obstructions of Section 2.4 are empty-kernel mechanisms. None of these is a failure of the framework: a quantity that answers exactly one question, stated with that question, is the framework working — and the framework's claim about itself is limited to the accounting layer it establishes.

### 10.4 Limitations

(i) The two-pool exact specialization of the groundwater template remains open; the admitted object is the one-pool affine approximation, and no two-pool model is claimed as established (Section 8.2). (ii) The phosphorus and groundwater rows are registered template obligations: no constitutive content exists behind their identification ladders. (iii) The first-passage theorems of Section 7 concern declared stochastic surrogates, not the ledger: they do not compute the ledger's hitting time, do not conserve its mass, and carry the record-relative-barrier and non-claim disciplines. (iv) The applied records of Section 6.5 are classified diagnostics at their stated evidentiary levels — statistical index, arithmetic ratio, removals-only pressure scale — and none is a calibrated early-warning system or a forecast. (v) The non-reduction boundary of Section 9 is permanent mathematics, not a gap: the closed primitive ledger and the open working system are different completions. (vi) The conditional hybrid balance of Theorem 15 stays conditional, with its jump-interpretation and yield-routing obligations open per application. (vii) The support-saturation limits of Section 2.6 are local and finite-time; neither is a full-system reduction. (viii) The article asserts nothing empirical about any named resource system beyond the classifications of public data products stated at their source status.

---

## 11. Conclusion

The two failure modes of the introduction — compensatory aggregation and classification drift — are representation errors, and the representation that prevents them is the article's content. Conservation is proved from the incidence structure, not assumed; positivity is proved from donor limitation, not asserted; services are readouts, not mass; and depletion time is three quantities, not one. The closed finite-donor ledger carries its complete theorem set — the natural-block mass identity, orthant invariance, no interior rest at positive effort, the vanishing-extraction rest set (extinction, carrying capacity, and the frozen-biomass face), extraction integrability — and the non-reduction boundary records, with reasons, why the closed ledger and the open working systems of institutional dynamics are different completions sharing one exact object. The depletion numbers of the applied record answer, each, exactly the question their construction poses: a statistical index of record-relative stress, an arithmetic ratio of an economic classification, a pressure scale of one gross loss rate. Stating them with those questions — against the published critiques they corroborate — is what makes them usable; collapsing them into one "time to depletion" is what makes them false.

The article likewise locates substitution within the ledger rather than alongside it. Weak and strong sustainability are two regimes of one system, distinguished by whether the material cycle closes at the rate of use. Weak sustainability is the idealized regime in which slow consumption and population let substitution (dominant, with regeneration deeper-time and included for completeness) redistribute matter so that it is used as it arises, and in which byproducts are therefore not waste. Waste is the relational status of matter that accumulates when that redistribution fails in time, for lack of knowledge, technology, or timely re-routing; no substance is waste by its nature, and the same redistribution is a local depletion rather than a product only when it fails to run ahead of the rate of use. A substitute is either a recycled flux returned to the regenerating pool or a non-renewable drawdown on a second compartment — different ledger entries with different statuses — and the ledger keeps stock compartments first-class, with the scalar $B\cdot M$ against consumption the operational reading on top of it. A horizontal exhaustion estimate built on a reserve figure carries the substitution and technology premises of the reserve classification, not a physical forecast. For ecological-economics measurement, the implication is that "strong" and "weak" sustainability are not rival doctrines but two readings of one typed stock–flow ledger — and the vector reading is what carries the certificate.

---

## Data availability

All computations underlying Section 6.5 are descriptive arithmetic on the cited public data products: the G3P groundwater anomaly product v1.12 (Güntner et al., 2024; GFZ Data Services, doi:10.5880/G3P.2024.001), the U.S. Geological Survey Mineral Commodity Summaries 2026 (the January 2026 release), and the RAM Legacy Stock Assessment Database (Ricard et al., 2012; the cohort pull date is archived in the analysis repository). The parameter tables of Section 2 are declared parameterizations. No other data were used.

## Declaration of competing interest

None.

---

## References

Aubin, J.-P., 1991. Viability Theory. Birkhäuser, Boston.

Blomqvist, L., Brook, B.W., Ellis, E.C., Kareiva, P.M., Nordhaus, T., Shellenberger, M., 2013. Does the shoe fit? Real versus imagined ecological footprints. PLoS Biology 11, e1001700. https://doi.org/10.1371/journal.pbio.1001700

Brunner, P.H., Rechberger, H., 2004. Practical Handbook of Material Flow Analysis. Lewis Publishers, Boca Raton.

Chhikara, R.S., Folks, J.L., 1989. The Inverse Gaussian Distribution: Theory, Methodology, and Applications. Marcel Dekker, New York.

Clark, C.W., 1990. Mathematical Bioeconomics: The Optimal Management of Renewable Resources, 2nd ed. Wiley, New York.

Ekins, P., Simon, S., Deutsch, L., Folke, C., De Groot, R., 2003. A framework for the practical application of the concepts of critical natural capital and strong sustainability. Ecological Economics 44, 165–185.

Eurostat, 2001. Economy-wide Material Flow Accounts and Derived Indicators: A Methodological Guide. Eurostat, Luxembourg.

Feinberg, M., 2019. Foundations of Chemical Reaction Network Theory. Springer, Cham.

Fischer-Kowalski, M., Krausmann, F., Giljum, S., Lutter, S., Mayer, A., Bringezu, S., Moriguchi, Y., Schütz, H., Schandl, H., Weisz, H., 2011. Methodology and indicators of economy-wide material flow accounting: state of the art and reliability across sources. Journal of Industrial Ecology 15, 855–876.

Güntner, A., Sharifi, E., Haas, J., et al., 2024. Global Gravity-based Groundwater Product (G3P), V. 1.12. GFZ Data Services. https://doi.org/10.5880/G3P.2024.001

Illakwahhi, D.T., Vegi, M.R., Srivastava, B.B.L., 2024. Phosphorus' future insecurity, the horror of depletion, and sustainability measures. International Journal of Environmental Science and Technology 21, 9265–9280. https://doi.org/10.1007/s13762-024-05664-y

Jacquez, J.A., Simon, C.P., 1993. Qualitative theory of compartmental systems. SIAM Review 35, 43–79.

Lin, D., Hanscom, L., Murthy, A., Galli, A., Evans, M., Neill, E., Mancini, M.S., Martindill, J., Medouar, F.-Z., Huang, S., Wackernagel, M., 2018. Ecological footprint accounting for countries: Updates and results of the National Footprint Accounts, 2012–2018. Resources 7, 58. https://doi.org/10.3390/resources7030058

Martinez-Alier, J., Munda, G., O'Neill, J., 1998. Weak comparability of values as a foundation for ecological economics. Ecological Economics 26, 277–286.

Meadows, D.H., Meadows, D.L., Randers, J., Behrens III, W.W., 1972. The Limits to Growth. Universe Books, New York.

Munda, G., Nardo, M., 2009. Noncompensatory/nonlinear composite indicators for ranking countries: a defensible setting. Applied Economics 41, 1513–1523.

Neumayer, E., 2013. Weak versus Strong Sustainability: Exploring the Limits of Two Opposing Paradigms, 4th ed. Edward Elgar, Cheltenham.

Øksendal, B., 2003. Stochastic Differential Equations: An Introduction with Applications, 6th ed. Springer, Berlin.

Redner, S., 2001. A Guide to First-Passage Processes. Cambridge University Press, Cambridge.

Ricard, D., Minto, C., Jensen, O.P., Baum, J.K., 2012. Examining the knowledge base and status of commercially exploited marine species with the RAM Legacy Stock Assessment Database. Fish and Fisheries 13, 380–398.

Tapley, B.D., Bettadpur, S., Ries, J.C., Thompson, P.F., Watkins, M.M., 2004. GRACE measurements of mass variability in the Earth system. Science 305, 503–505.

Tilton, J.E., 2003. On Borrowed Time? Assessing the Threat of Mineral Depletion. Resources for the Future, Washington, DC.

Tilton, J.E., Lagos, G., 2007. Assessing the long-run availability of copper. Resources Policy 32, 19–23.

U.S. Geological Survey, 2026. Mineral Commodity Summaries 2026: Phosphate Rock. USGS, Reston, VA. https://www.usgs.gov/centers/national-minerals-information-center/mineral-commodity-summaries

Wackernagel, M., Beyers, B., 2019. Ecological Footprint: Managing our Biocapacity Budget. New Society Publishers, Gabriola Island, BC.

---

## Supplementary material

The accompanying file `paper3_supplementary_v6.md` carries: the ten-state admissibility template and its three audited negative witnesses (the non-donor-limited geological exchange, the variance-closure failure, the undefined output functional); the registered identification ladders of the phosphorus and groundwater templates at full detail; the split-assignment mechanism table; the statement inventory with the status of every statement in the main text (theorem with displayed proof, conditional theorem, definition, application record, or boundary statement); and the fisheries cohort record with the archived-pull verification and the executed broad-cohort comparison (S5).

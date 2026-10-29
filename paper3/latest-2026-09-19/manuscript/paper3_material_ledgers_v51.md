# Typed Flux Ledgers and Depletion Arithmetic: Conservation, Componentwise Diagnostics, and the Semantics of Depletion Horizons

## Graphical abstract

![Graphical abstract: scalar compression can hide a failed component; a typed stock–flow ledger separates balance, conservation, safety and closure; and gross turnover intensity, frozen-rate ratios and scenario hitting times are distinct depletion-time concepts.](paper3_material_ledgers_v51_graphical_abstract.png)

*Graphical abstract. A positive weighted aggregate can conceal a failed component. The typed ledger keeps stocks and fluxes typed, distinguishes late return from ultimate loss, certifies balance, conservation, safety and closure separately, and does not interchange the three depletion-time concepts.*

## Abstract

Depletion indicators can carry similar units while built to inform distinct questions. Reserve-life ratios, trend-persistence metrics, and gross-removal pressure scales are widely interpreted as a literal “time to depletion,” despite measuring distinct physical or statistical quantities. Compounding this ambiguity, compensatory scalar aggregation routinely masks critical physical deficits behind positive aggregates.

In this paper, we resolve these confusions by constructing a typed stock–flow accounting ledger. By tracking conserved substance classes (*moieties*) independently, conservation laws remain typed: under the declared type discipline, biomass, financial flows, and biodiversity metrics do not form one typed scalar conservation readout. A cross-type numerical sum may still be computed, but it is an additional declared readout—not a conservation law of the typed ledger. Mass conservation follows directly from the incidence structure of the compartment–flux network, nonnegativity is guaranteed by donor limitation (primitive outflows vanish whenever their source compartment empties), and ecosystem services are treated strictly as observable readouts rather than conserved mass.

We formalize three certification layers: an exact flux-identifiability criterion for what an observed readout trajectory can and cannot determine about unobserved primitive fluxes, the conservation-law projection of an already balanced trajectory, and an envelope theorem providing verifiable flux-bounding certificates. The closure calculus is state- and boundary-conditioned, and it separates material not yet returned by a declared use deadline from material never returned: the first is a recoverable in-transit or pipeline requirement, while only the second liquidates the available-plus-recoverable stock. For the closed finite-donor ledger, we establish the natural-block mass identity, orthant invariance, the absence of interior rest points under positive extraction effort, a characterization of the vanishing-extraction rest set (extinction, carrying capacity, and a frozen-biomass face), and extraction integrability over finite budgets. Furthermore, we unpack “depletion time” into three mutually non-interchangeable concepts: gross turnover intensity, a frozen-rate local ratio, and a scenario-conditioned hitting time equipped with uniform-drift bounds.

We classify three widely cited public-data indicators within this taxonomy: the G3P groundwater anomaly index is shown to be a record-relative statistical metric rather than a physical stock ratio; the USGS phosphate reserve-life ratio is an arithmetic convention of an economic class rather than an exhaustion forecast; and fisheries removals-only timescales represent gross pressure scales rather than demographic depletion diagnostics. We prove that no nonnegative linear weighting can universally certify componentwise nonnegativity on arbitrary balance domains, and we establish five double-counting rules to prevent the emergence of phantom mass. Finally, we formulate first-passage semantics on declared stochastic surrogates against record-relative barriers alongside explicit non-claims. The argument separates two questions often compressed into “weak versus strong sustainability”: whether material cycles close at demanded throughput—a state-conditioned dynamical feasibility question—and whether an assessment is scalar-compensatory or componentwise—a certification-semantics question. A stationary bridge between them is proved, but the two distinctions are not identified.

**Keywords:** material flow accounting, stock–flow ledger, depletion indicators, first-passage time, conservation laws, composite indicators, reserve life.

## 1. Introduction

### 1.1 Failure Modes and the Two Confusions

Sustainability accounting consistently suffers from two structural pathologies:

1. **Compensatory Aggregation:** Heterogeneous physical stocks and service flows are compressed into scalar indices. Because cross-component substitution rates are rarely declared formally, acute physical deficits in one critical sub-system are mathematically obscured by surpluses elsewhere. While the composite-indicator and ecological economics literatures have long critiqued this flaw and proposed noncompensatory remedies (Munda & Nardo, 2009; Ekins et al., 2003; Neumayer, 2013), scalar index construction remains ubiquitous.
2. **Classification Drift:** Heterogeneous metrics with the dimension of time—reserve-life ratios, trend-persistence indicators, and removals-only pressure scales—are conflated into a single catch-all quantity: “time to depletion.” Yet, these metrics answer fundamentally different questions under incompatible boundary assumptions.

The operational reality of classification drift is striking. A reserve-life ratio simply divides an economically declared reserve by current annual production, christening the quotient a “depletion horizon.” A satellite groundwater anomaly index fits a linear trend to gravimetric anomalies, reporting the time needed to reach the historical record minimum at current rates; the result is expressed in years, yet corresponds to no physical exhaustion event. A fisheries pressure scale scales a logarithmic biomass margin by instantaneous fishing mortality, presenting a gross clearance timescale as if it were a demographic extinction date. Each metric provides specific institutional or descriptive information; none represents what is popularly claimed.

The primary manifestation of compensatory aggregation is exemplified by public awareness metrics such as *Earth Overshoot Day*. By collapsing ecological footprints and biocapacities into a single annual calendar date, a catastrophic deficit in an irreplaceable sub-component can easily coexist with an aggregate overshoot date that falls comfortably late in the calendar year (Lin et al., 2018; Wackernagel & Beyers, 2019; Blomqvist et al., 2013). Systems-dynamics models encounter identical aggregation ambiguities when multidimensional state spaces are collapsed into scalar stress variables (Meadows et al., 1972). The framework developed here is component-resolved by construction: depletion horizons are defined and tracked per asset and per pool, so a scalar date, if also computed, remains an additional aggregate readout rather than the ledger's componentwise certificate.

Beyond these accounting failures lies a deeper dynamical failure mode: the **productivity illusion**. This is the deceptive phenomenon in which an extractive system appears fully functional while the underlying support base sustaining its throughput is liquidated silently.

It has two senses, and they are distinct. The first is arithmetic and is the compensatory-aggregation failure above — a deficit in one component offset by a surplus in another, so that a positive aggregate reads as adequate. This article formalises this sense as the aggregation obstruction of Section 10.1. The second sense is dynamical and is yield inflation. A measured yield can exceed the true sustainable yield when it is maintained by drawing down the support pool — groundwater, soil carbon, bioavailable nutrients — rather than by that pool's regeneration. The resource appears productive while what sustains it is liquidated silently.

The support pool need not be an absolute, non-renewable geological stock. Whether framed as natural capital, an abiotic storage compartment, or a slowly replenishing ecosystem service, the governing physics remains identical. Every such pool regenerates over some characteristic timescale: an agricultural crop regenerates seasonally, an alluvial aquifer over decades or centuries, and mineral deposits over geological epochs.

A first accounting question is the rate of extraction relative to the rate of regeneration:

$$\text{Extraction sustained by regeneration} \implies \text{No net drawdown from that balance alone}$$

$$\text{Extraction exceeding regeneration} \implies \text{Net stock drawdown over that interval}$$

A drawdown can be reversed while the trajectory remains in a basin from which replenishment can exceed harvest for long enough to restore the declared margin; crossing a structural barrier can destroy that possibility even if harvest is later reduced. The physical size of a reserve determines one capacity bound, while whether an ongoing extraction pattern is regenerative throughput, recoverable drawdown, or liquidation also depends on the return lags, ultimate non-return share, capacities, and barriers declared with the ledger.

Dynamically, yield inflation mimics an overloaded mechanical structure. An elevator engineered for ten passengers can readily hold fourteen: the cable does not snap immediately upon loading the fourteenth person. Rather, it accumulates unseen microscopic strain. To the passengers, the ride feels normal until the threshold of tensile failure is breached, at which point catastrophe is instantaneous. Yield inflation corresponds to this silent wear phase: observable extraction rates remain stable, giving no hint of the drawdown occurring beneath the surface.

Our two-pool architecture is engineered specifically to capture this wear phase—making resource liquidation measurable while the supporting structure is still functional, rather than attempting to forecast the precise moment of failure.

Classification drift on the empirical side is equally well-documented. A reserve-life ratio ($\text{Reserves}/\text{Production}$) is purely arithmetic. Because an economic “reserve” is defined by extraction technology, market prices, exploration budgets, and legal permissions, it does not represent an immutable physical inventory. It replenishes dynamically through new discoveries and shifting economics. This issue has been demonstrated for phosphate rock by Illakwahhi, Vegi, and Srivastava (2024), who showed that widely publicized claims of global phosphorus exhaustion within a century stem from an uncritical reading of single-source U.S. Geological Survey (USGS) data. Such projections disregard industrial recycling, price feedbacks, and technological substitution. In mineral economics, this distinction between reserves (economic inventories) and resources (crustal abundance) has been recognized since Tilton (2003). For example, United States phosphate reserves have remained stable near $1.0\times 10^6\text{ kt}$ for decades despite cumulative extraction exceeding $6.0\times 10^5\text{ kt}$ over the same period. Copper demonstrates an identical dynamic: global reserves have increased over a century of exponential extraction (Tilton & Lagos, 2007).

Similar ambiguities plague material flow accounting (MFA; Brunner & Rechberger, 2004; Eurostat, 2001; Fischer-Kowalski et al., 2011). While MFA shares its incidence structure with chemical reaction network theory (Feinberg, 2019), practitioners frequently conflate four distinct operational properties:

1. **Bookkeeping balance** (mass accounting),
2. **Stoichiometric conservation** (reaction invariants),
3. **Thermodynamic admissibility** (nonnegative entropy production),
4. **Barrier safety** (maintenance of state variables within viability sets).

A perfectly balanced mass ledger can be chemically absurd; a chemically consistent network may violate all declared ecological safety barriers; and a trajectory satisfying every environmental constraint may violate basic conservation laws through phantom mass injections. Disentangling these layers and establishing their formal relations is the first primary objective of this work (Section 3).

Our second objective is to enforce **noncompensation**. Ecological economics asserts the *weak comparability of values*, maintaining that multi-criteria environmental decisions cannot be collapsed into a single metric without arbitrary value judgments (Martinez-Alier, Munda, & O'Neill, 1998). At the level of physical accounting, this thesis takes an exact algebraic form (Section 10.1): *no nonnegative linear weighting of balance vectors can certify that every underlying physical stock remains above its minimum critical threshold*. A positive weighted sum cannot by itself—without proved restrictions on the feasible balance domain—prove componentwise nonnegativity. Scalar indices are suitable for high-level communication and rough ranking; physical certification requires evaluating the full vector.

Our third objective is to integrate **technological substitution** directly into the ledger’s internal architecture, rather than treating it as an exogenous correction. This requires separating two distinctions that the weak/strong-sustainability vocabulary often compresses into one.

The first distinction is **dynamical closure**. At a declared state, boundary schedule, technology graph, and set of joint capacities, a demanded throughput is either *cycle-closing*—there is a stationary admissible flux pattern supplying it—or *closure-deficient*—there is no such pattern on that frozen feasible set. Closure deficiency does not make current service impossible: stocks, in-transit returns, imports, capacity changes, or unmet demand can absorb the mismatch for a time. It rules out one precise thing, indefinite delivery at that rate without changing the declaration. Technical change acts on this axis when it changes the process graph, the return kernel, a conversion coefficient, or a capacity. It cannot be represented by a smooth elasticity alone unless those physical changes have been declared.

The second distinction is **assessment semantics**. A *weak-assessment* readout permits a scalar aggregate to compensate a deficit in one component with a surplus in another. A *strong-assessment* predicate is conjunctive and componentwise: every declared balance or margin must pass. This is a question about what a certificate means, not about whether a stationary cycle exists. A cycle-closing system can still be reported through a weak scalar, and a closure-deficient system can be monitored component by component while its buffers last.

The two axes meet at a stationary bridge, proved after the service layer is defined: if a stationary closure pattern supplies the demanded services and the current state satisfies the declared componentwise margins, then holding that admissible pattern fixed preserves both. Neither converse holds. Componentwise adequacy over a finite interval can be bought by drawing down a buffer in a closure-deficient declaration; failure of stationary closure does not imply an immediate componentwise barrier violation. Throughout this article, “weak” and “strong” are therefore used with the qualifier *assessment* when they refer to certification semantics, while the dynamical distinction is called cycle-closing versus closure-deficient. This preserves the connection to the sustainability literature (Daly, 1990; Neumayer, 2013; Ekins et al., 2003) without asserting an isomorphism the mathematics does not supply.

The older regime language can now be read without conflating those axes:

* **Cycle-closing operation:** at the declared state and capacities, a stationary admissible flux pattern supplies the demanded throughput. Byproducts may still spend time in transit; what matters for ultimate liquidation is the never-returned share, while the return lag determines how much working stock the pipeline must hold.
* **Closure-deficient operation:** no stationary admissible pattern supplies the demanded throughput on the frozen feasible set, whether because a return pathway is absent, a shared donor has emptied, or the ultimate non-return share is positive without a declared replenishment. Service can continue transiently, but only by drawing a buffer, importing across the boundary, changing the declaration, or going unmet.

Independently:

* **Weak-assessment view:** A scalar aggregate is allowed to rank or alarm, including by offsetting one component against another.
* **Strong-assessment view:** the full balance and margin vector must pass component by component; no surplus elsewhere repairs a failed entry.

Both views have uses, but they answer different questions. A scalar can summarize or refute an aggregate condition; it cannot certify the componentwise predicate. The componentwise ledger maintains stocks as first-class physical entities and tracks the hitting times and sink boundaries that constrain throughput. Neither an instantaneous scalar check nor an instantaneous vector check, by itself, guarantees persistence: that requires the dynamical closure and horizon analysis developed below.

To quantify this drift, we construct scenario-conditioned hitting times (Sections 6.1 and 6.5). When applied to economic reserves, these hitting times capture the institutional assumptions embedded within reserve classifications, converting static ratios into rigorous diagnostics.

### 1.2 Contributions

1. **A Typed Primitive-Flux Ledger:** We formalize physical compartments by assigning each a material identity, spatial boundary, and physical unit. Compartments are linked via a signed incidence matrix driven by nonnegative primitive fluxes, synthesizing the accounting discipline of MFA (Brunner & Rechberger, 2004) with the algebraic formalism of reaction network theory (Feinberg, 2019). Type conversions require explicit stoichiometric coefficients, and all unilateral mass transfers are strictly donor-limited.
2. **Separation of Three Certification Layers:** We mathematically separate and prove the relationships between:
   * *Accounting consistency* (local preservation of balance equations),
   * *Conservation consistency* (invariance of declared moieties modulo boundary flows), and
   * *Barrier safety* (confinement of stocks within declared upper and lower limits).

   We prove an exact readout-to-flux identifiability criterion, the conservation-law projection of a balanced trajectory, and an envelope theorem providing bounding certificates for state-dependent fluxes. The layers are kept distinct: a left-null conservation vector alone does not prove that an arbitrary trajectory is balanced, and a balanced trajectory need not be barrier-safe.

3. **The Closed Finite-Donor Theorem Set:** For closed systems with finite geological donors, we prove:
   * The natural-block mass identity,
   * Orthant forward invariance (state nonnegativity),
   * The nonexistence of interior equilibria under positive extraction effort,
   * The structural characterization of the vanishing-extraction rest set (extinction, carrying capacity, and a frozen-biomass face), and
   * The $L^1$ integrability of extraction over finite budgets.

   Positivity is verified face-by-face using Bouligand tangent cones (Aubin, 1991), grounding our results in compartmental systems theory (Jacquez & Simon, 1993).

4. **Depletion Arithmetic:** We formally decompose the ambiguous notion of “depletion time” into three distinct physical and operational metrics:
   * Gross turnover intensity,
   * Local frozen-rate ratios, and
   * Scenario-conditioned hitting times.

   We derive uniform-drift horizon brackets and disprove the common assumption that “positive extraction guarantees finite exhaustion” via explicit counterexamples.

5. **Rigorous Classification of Empirical Indicators:** We establish the exact methodological status of three widely used metrics:
   * The GRACE/G3P groundwater anomaly index is shown to be a record-relative statistical index, not a physical stock-depletion ratio;
   * The USGS phosphate reserve-life metric is proved to be a static arithmetic quotient of an economic classification, not a physical depletion forecast;
   * The RAM Legacy fisheries clearance timescale is identified as a removals-only pressure scale, not a demographic hitting time.
6. **First-Passage Semantics on Declared Surrogates:** We formalize first-passage processes using inverse-Gaussian distributions (for linear drift models) and geometric Brownian motion (for relative fisheries proxies) against empirical barriers. We provide complete derivations and formalize seven explicit non-claims separating these surrogates from structural ledger dynamics.
7. **Coupling Interface with Institutional Delay Dynamics:** We define the shared mathematical boundary between our mass-conserved ledger and institutional harvest models via the decline-pressure identity $qEN - R = -\dot{N}$. For explicitly declared institutional memory and effort maps, we show when the ecological–institutional subsystem is closed on its history space, and we prove that the registered working field is not a coordinate-preserving exact reduction of—nor uniformly small-parameter close to—the closed field. No claim is made about arbitrary nonlinear conjugacies that do not preserve the named coordinates.

#### What Is Explicitly Not Claimed

* We make **no claim of a stochastic completion** for the full ledger: the surrogate processes in Section 7 do not conserve mass and are not stochastic perturbations of the underlying vector field.
* We make **no claim of thermodynamic completeness**: energy balances, chemical affinities, and entropy production are not formalized here.
* We make **no claim that the groundwater two-pool model is empirically identified**: the observational data required to resolve fast and slow groundwater storage are outlined as open requirements in Section 8.2.
* We make **no empirical forecasts** regarding specific aquifers, phosphate reserves, or marine fisheries beyond the descriptive classifications derived from published data.

### 1.3 Organization

Section 2 formulates the typed ledger, its constitutive laws, and its limiting properties. Section 3 formalizes the three certification layers and proves the core accounting theorems. Section 4 establishes the theorem set for the closed finite-donor ledger. Section 5 constructs the service readout layer and defines the componentwise deficit. Section 6 develops depletion arithmetic, proves the uniform-drift brackets, and classifies empirical indicators. Section 7 details first-passage semantics and its analytical boundaries. Section 8 details domain templates for phosphorus, groundwater, and bioeconomic harvesting. Section 9 states the interface hypotheses under which the ecological–institutional subsystem closes and proves the scoped coordinate-preserving non-reduction result. Section 10 outlines analytical boundaries, the failure of weighted aggregation, and double-counting safeguards. Section 11 concludes.

---

## 2. The Typed Primitive Ledger

**Notation.** One letter carries one sort wherever a computation is displayed; section-local aliases are declared where they occur, and the incidence operator is never written $N$ (which is reserved for the living stock). The table below sits at the head of Section 2 so that every alias is declared before it is used.

| Symbol | Meaning | Where |
|---|---|---|
| $N$ | living stock; nutrient stock (local to §2.4) | §2.2; §2.4 |
| $S_{\mathcal{T}}$ | typed stoichiometric (incidence) operator | §2.1, Lemma 3, Proposition 4, Theorem 5, Theorem 8 |
| $v$ | non-negative primitive flux vector | §2.1 |
| $S$ | moiety readout $S = Cx$ | Lemma 3, §6 |
| $s$ | support factor $A^{\mathrm{act}}/(A^{\mathrm{act}}+A_0)$ | §2.2 |
| $\sigma$ | donor fraction $A^{\mathrm{geo}}/(A^{\mathrm{geo}}+A_{g0})$ | §2.2 |
| $\varsigma$ | noise scale of the stochastic surrogates | §7 |
| $M$ | natural-block mass $N + A^{\mathrm{act}} + A^{\mathrm{geo}} + U$ | Theorems 7, 14 |
| $\widehat{M}$ | demand-coverage matrix of the physical deficit | §5.4 |
| $K$ | carrying capacity; sink stock (local to §2.4); maintainability kernel $K_{\mathrm{maint}}$ (subscripted) | §2.2; §2.4; §6.3 |
| $T$ | gross uptake $\kappa_A N s$; finite horizon (local to each statement) | §2.2; Theorems 1, 5 |
| $C$ | moiety-composition matrix; operative extraction-law readout; mining intensity $C^A$ | Lemma 3; §5.4; §2.2 |
| $B$ | $R + T$; barriers (local to §3.1); aggregate regeneration flow $b \cdot M$ (local to §1.1); fisheries biomass $B_t$ and barrier $B_{\min}$ (local to §7.5); reference $B_{\lim}$ (local to §6.5.2, §6.5.4) | §2.2; §3.1; §1.1; §6.5.2 |
| $b$ | total non-primitive term $b=B_{\mathcal{T}}u_\partial+d_x$; service balance $b_i$ (subscripted) | §2.1, Lemma 3, Proposition 4, Theorem 5, Theorem 24; §5.1 |
| $\kappa_m,\ell_m,W_m$ | cumulative return kernel, ultimate non-return share, and recoverable in-transit stock for moiety $m$ | Definition 22 |
| $R$ | net regeneration; log-margin $R_B$ (local to §6.5.4) | §2.2; §6.5.4 |
| $r$ | intrinsic growth rate; net boundary inflow $r_m$ (subscripted, §3.3) | §2.2; §2.6; §3.3 |
| $G$ | geological pool (scaffold); reserves (local to §6.5.3, §7.6); donor stock $G_0$ (subscripted) | §2.3; §6.5.3; §9 |
| $I$ | inert sink; boundary input $I_N$ (subscripted) | §2.2; §2.4 |
| $z$ | six-compartment state (local to §2.3) | §2.3 |
| $h$ | harvest primitive; net boundary outflow $h_m$ (subscripted, §3.3); geometric-Brownian drift (local to §7.5) | §2.3; §3.3; §7.5 |
| $x$ | ledger state | §2.1, Lemma 3, Proposition 4, Theorem 5 |
| $y$ | declared boundary states feeding the primitive fluxes | §2.1, eq. (1) |
| $\theta$ | declared constitutive parameter vector; sink-generation fraction $\theta_K$ (subscripted); parameter set $\Theta$ and fisheries pressure time $\Theta_F$ (distinct objects) | §2.1, eq. (1); §2.4; §6.4, §6.5.4 |
| $E$ | extraction effort, $E \ge 0$ along classical solutions | §2.2; §4.5; Theorem 14 |
| $\alpha$ | harvest routing fraction; directional support fraction $\alpha_{\mathrm{reg}}$ (subscripted) | §2.2–§2.3, §4.2; §5.3 |
| $\rho_P$ | product-retirement fraction routing $r_P$ to $U$ versus $W$ | §2.3; §4.3; §4.4; §8.1 |
| $\mu, \nu, \rho$ | product, waste, and price parameters of the unreduced ledger (zero in the single-resource specialization); $\mu$ also the growth parameter of Theorem 1 and the drift of the §7 surrogates; $\nu$ also the inverse-Gaussian mean (local to §7.3) | §2.2; §5.4; §9 |
| $\varepsilon$ | drift bracket (Proposition 17); probabilistic level (§6.4); resource-threshold fraction (§6.5.2, §7.6); donor-draw diagnostic $\varepsilon_G$ (subscripted); slack (§10.1) | §6.2; §6.4; §6.5.2; §9; §10.1 |
| $\tau$ | hitting and exit times ($\tau_B$, $\tau_m^{\pm}$, $\tau_{\mathrm{exit}}$) | §3.6; §6.3 |
| $d$ | disturbance (§2.1); demand vector (§5.2); drift distance (local to §7.3) | §2.1; §5.2; §7.3 |
| $A_0$ | half-saturation constant (§2.2); latest observed anomaly (local to §7.2–§7.4) | §2.2; §7.2 |
| $\lambda$ | inverse-Gaussian shape parameter | §7.3 |
| $\chi, \eta$ | hybrid state and primitive-flux vector of Conditional Theorem 15 | §4.8 |
| $P$ | product compartment; production rate (local to §6.5.3, §7.6) | §2.2–§2.3; §6.5.3 |

### 2.1 Typed stocks, primitive fluxes, and the incidence discipline

Material flow accounting starts from a few distinctions. Unlike substances must be tracked separately. Spatial and functional locations must be distinguished. Conversions between chemical forms must be written out. This section sets out the discipline that makes conservation a property of the structure rather than an assumption.

The ledger separates four ideas that accounting practice tends to merge. - A **moiety** is a conserved substance class — an element, or a declared conserved combination. A *species* is a chemical or biological form of a moiety. A *compartment* is a spatial or functional location holding a stock. A *stock* is a compartment's current amount of a species, with a physical unit. "Carbon in the atmosphere" is a place-specific stock, not a moiety. Conservation laws are stated per moiety; nothing is conserved merely by being a compartment.

A ledger state $x\in\mathbb{R}^m_+$ collects compartments, and each entry carries a material identity, a spatial support and a physical unit. Internal dynamics use non-negative primitive fluxes:
$$\dot x = S_{\mathcal{T}} v(x, y, \theta) + B_{\mathcal{T}} u_{\partial}(t) + d_x(t), \qquad v \ge 0, \tag{1}$$
where $S_{\mathcal{T}}$ is the typed stoichiometric (incidence) operator, $y$ collects the declared boundary states — environmental or companion variables external to the ledger — $\theta$ the declared constitutive parameter vector, $B_{\mathcal{T}} u_{\partial}$ collects declared boundary transfers, and $d_x$ belongs to a stated disturbance class. Throughout the article the total non-primitive term is the single object
$$b(t):=B_{\mathcal{T}}u_{\partial}(t)+d_x(t),$$
so equation (1) is $\dot x=S_{\mathcal{T}}v+b$. A bound, readout, or certificate stated for $b$ is therefore a statement about boundary transfer and disturbance together; splitting them requires a separate displayed hypothesis. Entries are added within a row only when their types and units agree. That sentence presumes a declaration, and the declaration is Definition 47: types, units and conversion coefficients are declared with the ledger, and $S_{\mathcal{T}}$ carries the subscript for that reason. If $L^\top S_{\mathcal{T}} = 0$, then along a trajectory satisfying equation (1),
$$\frac{d}{dt}(L^\top x) = L^\top b,$$
one projected balance per conserved moiety and boundary; the identity does not create a scalar sustainability mass across incommensurable systems, and Proposition 42 states exactly in what typed sense it cannot. Three admissibility requirements are imposed before equation (1) is used as a physical ledger rather than as a formal vector equation. First, $d_x$ must itself be typed: a physical disturbance on represented material is a different object from a structural discrepancy term, and only the former may be interpreted as mass crossing a represented compartment. Second, the sign pattern of the incidence matrix and the non-negativity of the primitives are separate declarations. Third, every primitive outflow must vanish or be limited when its donor compartment is empty, and a target-relaxation flux from a finite donor is admissible **only after** donor limitation is made explicit. Particular consequences of these requirements are proved where they are used; they are not themselves presented as theorems of this section.

**Definition 21 (State-conditioned closure set and closure capacity).** The dynamical distinction of Section 1.1 can be stated on the ledger's own objects rather than as an attitude toward them. Freeze a state $x$, boundary declaration $y$, parameter vector $\theta$, and a *stationary declared boundary schedule* $b_0=B_{\mathcal{T}}u_{\partial,0}$. The disturbance $d_x$ is not part of $b_0$: an unspecified discrepancy cannot be used as a stationary supply. Let $\bar v(x,y,\theta)$ collect the individual flux capacities at that frozen declaration, and let $A_dv\le h(x,y,\theta)$ collect every capacity jointly consumed by two or more fluxes—return plant, transport link, donor stock, energy budget expressed as a flux constraint, or any other declared shared capacity. Row omission is itself the declaration that there is no such coupling. Donor limitation is part of these bounds: if flux $j$ draws on compartment $i$, then $\bar v_j=0$ when $x_i=0$, and a joint donor row has $h=0$ when its donor stock is empty. The admissible stationary patterns at the frozen declaration are
$$\mathcal K(x;b_0):=\{v\in\mathbb R_+^q:\ S_{\mathcal{T}}v+b_0=0,\quad 0\le v\le\bar v(x,y,\theta),\quad A_dv\le h(x,y,\theta)\}.$$
Let $P$ be the declared linear use/service readout from primitive fluxes—a coordinate projection when the demanded services are selected primitive fluxes, and the readout matrix $Q$ of Section 5.1 when services are converted flux combinations. A demanded use vector $D$ *closes at the rate of use at $(x,b_0)$* if and only if $D\in P(\mathcal K(x;b_0))$. Its closure capacity is
$$\Lambda^*(x;D,b_0):=\max\{\mu\ge0:\ \mu D\in P(\mathcal K(x;b_0))\},$$
a linear programme once $(x,y,\theta,b_0)$ are frozen; on network specializations its feasibility is the corresponding cut condition on return and joint capacities (Gale, 1957; Ahuja et al., 1993). Where $\Lambda^*(x;D,b_0)\ge1$, the cycle closes at the demanded rate *at that state and boundary schedule*. Where it is below $1$, no stationary flux pattern in the frozen feasible set supplies $D$. Any interval on which $D$ is nevertheless met must therefore use at least one of four exits from the frozen statement: non-stationary stock change, a different declared boundary schedule, a changed state/capacity/technology declaration, or demand left unmet. Definition 21 alone does not say which stock changes, at what rate, in which direction relative to a barrier, or whether a sink fills; those are trajectory questions for Definitions 22 and 45–46 and for the barrier analysis. Yield inflation is the observable form of the first exit when service is maintained by drawing a support buffer.

Left-null vectors express conservation; feasible stationary circulations are constrained right-null patterns. The closure distinction is about the second object, and the depletion readouts of Section 6 are largely about the first; neither membership follows from the other's.

**Definition 22 (Return kernel, use-timescale deficit, late return, and ultimate loss).** For each moiety $m$, let $\kappa_m(\tau;\Theta)\in[0,1]$ be the cumulative fraction of a mobilised cohort returned to a usable compartment within lag $\tau$ under the declared technology and process graph $\Theta$. It is a cumulative return kernel: nondecreasing and right-continuous in $\tau$, with $\kappa_m(0-;\Theta)=0$ unless an instantaneous return atom at lag zero is explicitly declared. Write
$$\kappa_m^\infty:=\lim_{\tau\to\infty}\kappa_m(\tau;\Theta),\qquad
\delta_m^{\mathrm{use}}:=1-\kappa_m(\tau_{\mathrm{use}};\Theta),\qquad
d_m^{\mathrm{late}}:=\kappa_m^\infty-\kappa_m(\tau_{\mathrm{use}};\Theta),\qquad
\ell_m:=1-\kappa_m^\infty,$$
so that, exactly,
$$\delta_m^{\mathrm{use}}=d_m^{\mathrm{late}}+\ell_m.$$
The use-timescale deficit $\delta_m^{\mathrm{use}}$ is the share **not back by the deadline**. The late share $d_m^{\mathrm{late}}$ eventually returns. Only $\ell_m$, the *ultimate non-return share*, never returns under the declared kernel. Conflating the first with the third is the finite-lag error this definition exists to prevent.

The kernel has a stock consequence that a single return fraction hides. Let $g_m(s)$ be the mobilisation history and let $r_m(t)$ be the resulting return flux,
$$r_m(t)=\int_{(-\infty,t]} g_m(s)\,d\kappa_m(t-s;\Theta),$$
read as a Stieltjes convolution. The recoverable in-transit stock—the material already mobilised, not yet back, but still destined to return—is
$$W_m(t):=\int_{-\infty}^{t}\bigl[\kappa_m^\infty-\kappa_m(t-s;\Theta)\bigr]g_m(s)\,ds,$$
whenever the integral is finite. If $A_m$ is the available support stock, $j_m$ collects all other declared replenishment and boundary transfers into that support, and differentiation under the integral is legitimate, then
$$\dot W_m=\kappa_m^\infty g_m-r_m,\qquad \dot A_m=-g_m+r_m+j_m,\qquad\text{hence}\qquad \frac{d}{dt}(A_m+W_m)=-\ell_mg_m+j_m.$$
Late return can make the *available* stock $A_m$ scarce, but by itself it does not liquidate the combined circulation stock $A_m+W_m$; only $\ell_mg_m$ does, net of $j_m$. For constant $g_m>0$, $j_m=0$, and $\ell_m>0$, the identity gives the outer time bound
$$T\le \frac{A_m(0)+W_m(0)}{\ell_mg_m}$$
for maintaining that mobilisation with $A_m,W_m\ge0$. It is an outer bound, not an exhaustion date: service can fail earlier because $W_m$ is not yet usable. Started from an empty pipeline, $W_m(t)=g_m\int_0^t[\kappa_m^\infty-\kappa_m(s;\Theta)]ds$; if the mean recoverable residence integral $\bar L_m:=\int_0^\infty[\kappa_m^\infty-\kappa_m(s;\Theta)]ds$ is finite, the steady pipeline requirement is $W_m^\infty=g_m\bar L_m$. Thus a completely returning cycle ($\ell_m=0$) can still fail transiently if the initial available stock cannot finance its own pipeline, $A_m(0)<W_m^\infty$, even though it liquidates nothing in the long run. Conversely, at an already filled steady pipeline it can run with $\dot A_m=0$. Only in the special case $d_m^{\mathrm{late}}=0$—all eventual returns arrive by $\tau_{\mathrm{use}}$—does $\delta_m^{\mathrm{use}}=\ell_m$, and only then may the use-timescale deficit be used as a liquidation share. If an accounting convention refuses credit for returns after $\tau_{\mathrm{use}}$, $\delta_m^{\mathrm{use}}$ is an *effective deadline deficit under that convention*, not a physical loss rate.

Two readings follow. An indicator that reports a return fraction with no lag argument does not distinguish $\kappa_m(\tau_{\mathrm{use}})$, $\kappa_m^\infty$, pipeline stock, and ultimate loss; the recycled-input and circularity-rate families are exposed to exactly that ambiguity. And “a material is waste at the use timescale” means $\delta_m^{\mathrm{use}}>0$ for the declared graph, whereas permanent loss under that graph means $\ell_m>0$. Unlocking a stream can therefore do two different measurable things: move mass from late return to timely return at fixed $\ell_m$, or reduce $\ell_m$ itself. A positive deficit is still not a barrier-reachability claim: the binding event may be available-stock exhaustion, pipeline under-financing, or an upper sink barrier, and each has its own clock.

### 2.2 The closed finite-donor ledger

The closed ledger of this article is the finite-donor primitive system. Let
$$x_L = (N, A^{\mathrm{act}}, A^{\mathrm{geo}}, U), \qquad s = \frac{A^{\mathrm{act}}}{A^{\mathrm{act}} + A_0}, \qquad \sigma = \frac{A^{\mathrm{geo}}}{A^{\mathrm{geo}} + A_{g0}},$$
with $N$ the living stock, $A^{\mathrm{act}}$ the active abiotic pool, $A^{\mathrm{geo}}$ the geological donor, and $U$ the detritus compartment. Net regeneration and gross uptake are the constitutive laws
$$R(N, A^{\mathrm{act}}) = rN\left(1 - \frac{N}{K}\right)s, \qquad T = \kappa_A N s, \qquad B = R + T,$$
and the four geo-interface and closure primitives are
$$e_{GA} = \omega_A A^{\mathrm{eq,intrinsic}} \sigma, \qquad e_{AG} = \omega_A A^{\mathrm{act}}, \qquad C^{A,\mathrm{lim}} = C^A \sigma, \qquad \gamma_U U \ \text{(detritus return)}.$$

These donor primitives instantiate one of three recharge laws that appear across this paper and the companion delay-dynamics analysis (Abaee, 2026a, doi:10.5281/zenodo.22554217); the three are distinct objects, tabulated once so that none is silently substituted for another:

| Recharge law | Form | Status |
|---|---|---|
| Primitive donor-limited exchange | $e_{GA} = \omega_A A^{\mathrm{eq,intrinsic}} \sigma$ | The closed block's law (Section 2.2): the forward rate depends on the donor alone, not on how empty the receiving pool is — linear donor-limited exchange, whose rest is $A^{\mathrm{act}} = A^{\mathrm{eq,intrinsic}}\sigma$ (Theorem 13). |
| Target-relaxation | $\omega_A(A^{\mathrm{eq}} - A)$ | Banned unless donor-limited (Section 4.4): runs backward at an empty donor; admissible only with the source declared an effectively infinite external reservoir, making the system open. |
| Working derived target | $A^{\mathrm{eq,W}} = A^{\mathrm{eq,intrinsic}} + \kappa_A K/\omega_A$ | The delay-dynamics analysis's working completion (that analysis; this article's Section 9): not a closed-block law, and the reason the two systems do not reduce. |

In the closed block no derived target appears. Recharge is donor-limited and cannot run backward ($e_{GA} = 0$ at $A^{\mathrm{geo}} = 0$; the positive-part convention $[\cdot]_+$, read as a one-way valve at a nonpositive target, never binds here because the registered intrinsic target is positive), and mining $C^{A,\mathrm{lim}}$ is donor-limited the same way extraction is. With $A_{g0} > 0$ the donor fraction $\sigma$ is smooth and strictly increasing in the donor level.

Under the institutional-failure specialization ($\mu = \nu = \rho = 0$ and $C^A = 0$ — the product, waste, and price parameters $\mu, \nu, \rho$ of the unreduced ledger, its macroeconomic-feedback, recycling, and price-response channels, set to zero together with the mining intensity $C^A$; the parameters are glossed at their Section 5.4 site) the closed natural block is
$$\begin{aligned}
\dot N &= R - qEN, \\
\dot A^{\mathrm{act}} &= -B + e_{GA} - e_{AG} + \gamma_U U, \\
\dot A^{\mathrm{geo}} &= -e_{GA} + e_{AG}, \\
\dot U &= T - \gamma_U U,
\end{aligned} \tag{2}$$
together with a memory–effort pair $(Z, E)$ driven by $qEN - R$ (never by mining; $q$ the per-effort extraction coefficient of the harvest law). The pair is the registered object of the companion delay-dynamics analysis (Abaee, 2026a, doi:10.5281/zenodo.22554217; its eq. (1), where the memory--effort pair is defined on the
gated three-state core with the stock-decline rate as memory input, and its Section 2.4, which relates that
core to the four-state working model in which the input is $qEN - R(N, A)$) and is not analysed in this article. Net regeneration is the difference of two non-negative primitives — gross regeneration $rNs$ (support → stock) and density-dependent return $rN^2s/K$ (stock → support) — so (2) stays inside the primitive-flux discipline of §2.1 despite the signed entry. The block's harvest routing is the $\alpha = 0$ corner of Section 2.3: harvest $qEN$ exits the natural block entirely as product, and a positive detritus-routed fraction $\alpha > 0$ would add $\alpha qEN$ to $\dot U$ and reduce the block export to $(1-\alpha)qEN$; the mass identity of Theorem 7 is stated for the declared routing. The registered parameterization is $r = 0.02$, $K = 100$, $q = 0.001$, $\kappa_A = 0.05$, $\omega_A = 10^{-3}$, $A_0 = 1$, $A^{\mathrm{eq,intrinsic}} = 50$, $\gamma_U = 0.2$; the geological half-saturation $A_{g0}$ is declared positive (smoothness of the donor fraction $\sigma$) under the separation-of-scale condition $A^{\mathrm{geo}} \gg A_{g0}$, in which regime $\sigma \approx 1$; the scale separation is registered rather than a numerical value, and the $A_{g0} = 0$ corner is the discontinuous-perturbation limit, not the registered regime. With $A_0>0$ and $A_{g0}>0$ the right-hand side of (2) is locally Lipschitz on the closed orthant, and the comparison $\dot N\le rN(1-N/K)$, with $\dot N\le0$ once $N\ge K$, bounds the stock by $\max\{N(0),K\}$. Classical solutions therefore exist globally and stay in the orthant by Theorem 10 — the existence clause behind every 'classical solution' statement below.

The incidence discipline of Section 2.1, written out for the closed block, is the four-row block incidence — rows $(N, A^{\mathrm{act}}, A^{\mathrm{geo}}, U)$, columns gross regeneration $rNs$, density-dependent return $rN^2 s/K$, harvest $qEN$, uptake $T = \kappa_A N s$, detritus return $\gamma_U U$, geological recharge $e_{GA}$, geological return $e_{AG}$, mining $C^{A,\mathrm{lim}}$:
$$S_{\mathrm{block}} =
\begin{pmatrix}
1 & -1 & -1 & 0 & 0 & 0 & 0 & 0 \\
-1 & 1 & 0 & -1 & 1 & 1 & -1 & 0 \\
0 & 0 & 0 & 0 & 0 & -1 & 1 & -1 \\
0 & 0 & 0 & 1 & -1 & 0 & 0 & 0
\end{pmatrix}.$$
Every column is a two-compartment transfer or a block-boundary export: the six internal columns sum to zero, and the two exports — harvest and mining — carry the column sums $-1$ each, so summing the four rows reads off $\dot M = -qEN - C^{A,\mathrm{lim}}$, the mass identity proved as Theorem 7, directly from the display (under the institutional-failure specialization the mining column is inactive, $C^A = 0$). The harvest column is written at the declared $\alpha=0$ routing, under which harvest leaves the block; a detritus-routed fraction $\alpha>0$ moves $\alpha$ into the $U$ entry of that column and reduces the block export to $(1-\alpha)qEN$ — the full-ledger routing displayed in §4.2.

When product, waste and the inert sink are restored with the same donor-limited routing, the full ledger $N+A_{\mathrm{act}}+A_{\mathrm{geo}}+U+P+W+I$ is closed (§4.2). The geological donor is an internal state throughout — no infinite reservoir is declared — and the block boundary is crossed only by harvest (to product) and, when restored, mining (to product or waste). The full seven-compartment incidence is the nested completion of this four-block routing. It is an $A_{\mathrm{act}}\to U$ throughput in which the living stock appears as a catalytic factor, not as stored biomass. Uptake $T = \kappa_A N s$ never enters $\dot N$: it is an $A^{\mathrm{act}} \to U$ throughput with the living stock entering as a catalytic factor, not stored biomass — legitimate in a monomaterial projection; the masses below are defined on this routing

### 2.3 The six-compartment illustration

For one conserved limiting material, the scaffold is instantiated by six compartments — living biomass $X$, detritus or recoverable residual $U$, active abiotic pool $A$, geological or slowly available pool $G$, product or in-use stock $P$, and absorbing or currently unavailable stock $W$ — with eight non-negative primitive fluxes: assimilation $g(X,A)$, mortality $m(X)$, harvest $h(X,E)$, decomposition $d_U(U)$, geological-to-active transfer $e_{GA}(G,A)$, active-to-geological transfer $e_{AG}(A,G)$, direct mining $c_G(G,E_G)$, and product retirement $r_P(P)$. With harvest fraction $\alpha \in [0,1]$ routed to $U$ and retirement fraction $\rho_P \in [0,1]$ returning to $U$ rather than $W$,
$$\dot z = S(\alpha, \rho_P)\, v(z, u), \qquad z = (X, U, A, G, P, W)^\top, \qquad v = (g, m, h, d_U, e_{GA}, e_{AG}, c_G, r_P)^\top,$$
where
$$S(\alpha, \rho_P) =
\begin{pmatrix}
1 & -1 & -1 & 0 & 0 & 0 & 0 & 0 \\
0 & 1 & \alpha & -1 & 0 & 0 & 0 & \rho_P \\
-1 & 0 & 0 & 1 & 1 & -1 & 0 & 0 \\
0 & 0 & 0 & 0 & -1 & 1 & -1 & 0 \\
0 & 0 & 1-\alpha & 0 & 0 & 0 & 1 & -1 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 1-\rho_P
\end{pmatrix}, \qquad \mathbf{1}^\top S = 0.$$
The zero column sums are the incidence statement of mass conservation (proved for the full system in Section 4.2). So every column sums to zero, which is the incidence statement of mass conservation (proved for the full system in §4.2). The constitutive choices belong to this example, not to every typed ledger: the constant splits $\alpha$ and $\rho_P$, the compartment set, and the absorbing-sink convention are declared choices. Coupled multi-element accounts require additional typed rows and a conservation matrix. Coupled multi-element accounts need additional typed rows and a conservation matrix. If an application makes recovery claims, $U$ and $P$ must be split by material, location and quality grade, with declared yields, residual routes and exergy or capacity inputs; the conservation argument then applies to that expanded typed incidence system, not automatically to an undifferentiated quality-neutral loop.

### 2.4 The four-stock resource–sink–nutrient–product system

A second exact specialization closes a resource–sink system by adding a nutrient stock and a product stock. The state is $(S, K, N, P) \in \mathbb{R}^4_+$ (in this block's local notation, $S$ is the resource stock, $K$ the sink stock, $N$ the nutrient stock, and $P$ the input flux; the carrying capacity and living stock of Section 2.2 do not enter), with
$$\dot S = g(S,N) - H, \qquad \dot K = \theta_K H - \theta_\delta K, \qquad \dot N = -g(S,N) + \theta_\delta K + I_N, \qquad \dot P = (1 - \theta_K)H - Q_P,$$
where $\theta_K$ is the sink-generation fraction, $\theta_\delta$ the assimilation rate, $I_N$ external nutrient input, and $Q_P$ product disposal. Adding the four equations gives the mass balance
$$\frac{d}{dt}(S + K + N + P) = I_N - Q_P,$$
so total mass is conserved exactly when both boundary transfers vanish. This balance is an exact specialization of the incidence discipline of §2.1: every internal transfer cancels in the column sum, and the boundary terms survive as the ledger's declared inputs and outputs.

**Sink obstructions that do not care what the stock does.** The mass balance has a sink-side physical reading with two empty-kernel mechanisms that operate whatever the resource stock does. With sink loading $w(H)$, assimilation $\delta(K)$, and a harvest floor $H \ge H_{\min} > 0$ (in the four-stock specialization, $w(H) = \theta_K H$ and $\delta(K) = \theta_\delta K$): under *no assimilation* ($\delta \equiv 0$), $\dot K \ge w(H_{\min}) > 0$, and the sink exceeds any finite ceiling $K_{\max}$ in finite time; under *weak assimilation* ($\delta(K_{\max}) < w(H_{\min})$), the sink load at the ceiling is still positive — $\dot K = w(H_{\min}) - \delta(K_{\max}) > 0$ at $K = K_{\max}$ — so $K$ exits above $K_{\max}$ in finite time, the explicit negation of the ceiling condition $\delta(K^\dagger) = w(H_{\min})$ with $K^\dagger \le K_{\max}$. In both cases the viability kernel (Aubin, 1991) of the constraint set $\{\mathsf S\ge \mathsf S_{\min},\,0\le K\le K_{\max}\}$ — the states from which *some* admissible harvest keeps both constraints forever — **is empty**. The obstruction needs the sink-generation fraction $\theta_K > 0$: if $\theta_K = 0$, harvest never loads the sink and the loading argument does not apply — emptiness would then have to come from the resource constraint or an undeclared ceiling on the product stock.

The closed-ledger corollary is the same mechanism in ledger language. In a closed ledger without recycling, where $w(H)$ enters the sink irreversibly and $\delta = 0$, the sink rises monotonically against the finite total mass, and any positive output floor forces an empty viability kernel. Which constraint fails first depends on the total mass $M$, the ceiling $K_{\max}$, and the remaining stock: a ceiling below the sink's reachable mass share is crossed in finite time, while a ceiling at or above the total mass is unreachable and the violated constraint is the resource floor (the finite-budget bound of Theorem 14). For material-flow accounting this is the precise sense in which a "balanced" mass ledger can still be **physically inadmissible**: the bookkeeping is exact, but no harvest schedule respects the resource floor and the sink ceiling at the same time.

### 2.5 Mechanism typing: routing is never determined by diagnostic labels

Extraction has at least three distinct physical meanings — standing-stock culling (present extraction removes reproductive stock directly), recruitment suppression (present use prevents future recruits without immediate adult removal), and weak viability coupling (use has limited or indirect effect on reproduction). In the ledger, standing-stock culling enters as an outflow from the standing-stock compartment. A diagnostic label such as "unsustainable portion" **never** determines physical destination. Material routing is determined by the typed physical module alone, and the diagnostic threshold that flags a flow has no standing in the incidence matrix.

**The split-assignment evidence requirement.** Where an application splits extraction between standing-stock removal and recruitment suppression — $C_{\mathrm{stock}} = \psi qEN$ and $C_{\mathrm{recruit}} = (1-\psi)qEN$ for $\psi \in [0,1]$ — the assignment requires evidence per channel. The dominant physical mechanism sets it, never a diagnostic label. Illustrative assignments through a logistic two-channel proxy (stated as illustrative, calibrated examples, not constitutive claims for the named domains): soil zinc under crop export, an existing-unit removal, at $\psi = 0.85$, against impaired mineralisation, a replenishment degradation, at $\psi = 0.25$; pollinators under adult mortality at $\psi = 0.70$ against brood failure at $\psi = 0.20$ The numerical depth of any resulting trough is proxy- and parameter-specific; no trough-depth factor is asserted as a theorem from these illustrative assignments. **The mass-routing discipline** is the same typing made explicit. Literally harvesting pre-recruit stages *is* a harvest of existing units, and routes to the product and waste fractions. 2. Habitat-induced failed recruitment is a **prevented inflow** — routing it into product or waste would create mass that was never in the stock. Damage to the capital stock itself — aquifer compaction, severe soil loss — is not a split-assignment channel at all.

### 2.6 Support saturation and the logistic limit

Two results control what the ledger's stock equation becomes when its support pool saturates. Both are singular reductions with explicit scope, and neither is a full-system reduction.

**Theorem 1 (Support-saturated logistic stock limit).**
*Fix $T < \infty$ and non-negative parameters $\mu, \delta, c, q$. For $\kappa > 0$, let $X_\kappa$ be an absolutely continuous solution of*
$$\dot X_\kappa=\mu X_\kappa\frac{A_\kappa(t)}{\kappa+A_\kappa(t)}-\delta X_\kappa-cX_\kappa^2-qE(t)X_\kappa,$$
*and let $X_0$ solve the limiting equation*
$$\dot X_0=(\mu-\delta)X_0-cX_0^2-qE(t)X_0$$
*with the same initial value. Assume:*

*(H1) $A_\kappa$ is measurable with $A_\kappa(t) \ge a_0 > 0$ almost everywhere, and both $X_\kappa$ and $X_0$ remain in $[0,X_{\max}]$ on $[0,T]$.*

*(H2) The common effort satisfies $E\ge0$ almost everywhere and $E \in L^\infty([0,T])$.*

*Then $\sup_{t \le T} |X_\kappa(t) - X_0(t)| = O(\kappa)$. If additionally $\mu > \delta$ and $c > 0$, the limiting equation has the logistic form $\dot X_0 = rX_0(1 - X_0/K_{\log}) - qE(t)X_0$ with $r = \mu - \delta$ and $K_{\log} = (\mu - \delta)/c$.*

*Proof.* Write $e(t) = |X_\kappa(t) - X_0(t)|$. The saturation defect satisfies
$$\left| \frac{A_\kappa}{\kappa + A_\kappa} - 1 \right| = \frac{\kappa}{\kappa + A_\kappa} \le \frac{\kappa}{a_0},$$
so the vector-field defect obeys
$$|\dot X_\kappa - \dot X_0| \le L_1 \kappa + L_2 e(t), \qquad L_1 = \frac{\mu X_{\max}}{a_0}, \qquad L_2 = \mu + \delta + 2cX_{\max} + q\|E\|_\infty,$$
using $|\mu - \delta| \le \mu + \delta$ and $c(X_\kappa + X_0) \le 2cX_{\max}$. Integrating and applying Gronwall's inequality in the form that needs no division by $L_2$ gives $e(t)\le L_1\kappa\,t e^{L_2t}\le C_T\kappa$ on $[0,T]$; this remains valid at $L_2=0$, where necessarily $\mu=0$ and hence $L_1=0$. The common bound in (H1) is satisfiable in the registered family: when $\mu>\delta$ and $c>0$, the comparison $\dot X_\kappa \le X_\kappa(\mu - \delta - cX_\kappa)$ (using $A_\kappa/(\kappa+A_\kappa)\le1$ and $E\ge0$) keeps both solutions below $\max\{X(0),(\mu-\delta)/c\}$, so $X_{\max} = \max\{X(0), K_{\log}\}$ suffices. Outside that parameter corner, (H1) remains an explicit finite-horizon hypothesis rather than a conclusion smuggled into the proof. The limiting equation is $\dot X_0 = \mu X_0 - \delta X_0 - cX_0^2 - qE X_0$, i.e. $\dot X_0 = (\mu - \delta)X_0 (1 - X_0/K_{\log}) - qE X_0$ with $K_{\log} = (\mu - \delta)/c$. □

**Remark 2 (Registered-family support-saturated identity).**
*In the primitive-flux core with $g(X,A) = \mu XA/(K_A + A)$, $m(X) = dX + cX^2$, $h(X,E) = qEX$, the support-saturated stock equation is, for each fixed interior $A > 0$ in the limit $K_A \to 0$,*
$$\dot X = (\mu - d)X - cX^2 - qEX = rX\left(1 - \frac{X}{K}\right) - qEX, \qquad r = \mu - d, \quad K = \frac{\mu - d}{c},$$
*requiring $\mu > d$ and $c > 0$. The identity is pointwise on the interior support region and not uniform through the depleted-pool boundary: for every $K_A > 0$, $A/(K_A + A) = 0$ at $A = 0$.*

*Proof.* At fixed $A > 0$, $A/(K_A + A) \to 1$ as $K_A \to 0$, so $g \to \mu X$ pointwise and $g - m \to (\mu - d)X - cX^2$; the algebraic reduction to the logistic form with $r = \mu - d$, $K = (\mu - d)/c$ is immediate. The non-uniformity statement is the identity $A/(K_A + A) = 0$ at $A = 0$ for every $K_A > 0$, which the pointwise limit does not touch. The scope is restricted: the limit does not eliminate the detritus compartment $U$, does not make $A$ constant near its boundary, and does not transform the memory or effort laws — an ecological stock-equation identity, not a full-system reduction and not a transfer principle for bifurcation thresholds. In the correspondence, the logistic law of (2) is this saturated, mortality-folded readout of the Theorem 1 and Remark 2 family — not the vector field of the closed four-tuple of Section 2.2 — and bifurcation numbers of the two families do not transfer between them. □

Substituting it for the underlying stock-support dynamics is legitimate only where the support pool is at interior saturation, and only on the timescales over which the saturated approximation holds.

---

## 3. Certification Layers and the Accounting Theorems

### 3.1 Three predicates, separated

The four predicates of Section 1.1 — bookkeeping balance, stoichiometric conservation, thermodynamic admissibility, and sustainability safety — are this section's working layer: it separates the first, second, and fourth and proves the relationships that actually hold among the predicates defined here. Thermodynamic admissibility is not defined by this paper's ledger objects, so no theorem about it is asserted; if a companion framework defines that term to include mass balance as one conjunct, the resulting implication belongs to that definition, not to a proof here. This is the point at which the Daly/Ayres tradition of throughput accounting meets the formalism of reaction-network theory (Feinberg, 2019; Brunner and Rechberger, 2004).

The ledger supports three distinct predicates that are related but not identical.

**Layer 1: Accounting consistency.** The balance law (1) holds almost everywhere on $[0,T]$.

**Layer 2: Conservation consistency.** $\ell^\top S_{\mathcal{T}} = 0$ for every declared conserved quantity $\ell$.

**Layer 3: Barrier safety.** For declared lower and upper barriers $\underline{B}_m(t) \le S_m(t) \le \overline{B}_m(t)$ for every component $m$ and every $t \in [0,T]$, where $S = Cx$ is the moiety-composition readout.

Layer 2 is a structural predicate on the incidence operator alone. Layers 1 and 3 are properties of a trajectory triple $(x, v, b)$. The logical relations between them are the content of the next two propositions. (Numbering: the two layering propositions of this section carry their own counter, Propositions 1–2. Every other statement is cited by the ordered pair (kind, number)—for example, Definition 34 and Remark 34 are distinct labels—so a bare number is not a complete reference. The inherited numbering is retained for cross-version traceability rather than renumbered in appearance order; its maxima are Definition 47, Lemma 4, Proposition 43, Theorem 24 and Remark 37. The supplementary’s S6 gives the corresponding reading rule.)

**Proposition 1 (Conservation projection of a balanced trajectory).** *If the triple $(x,v,b)$ is accounting-consistent, so that $\dot x=S_{\mathcal{T}}v+b$ almost everywhere, and if $\ell^\top S_{\mathcal{T}} = 0$, then*
$$\frac{d}{dt}(\ell^\top x) = \ell^\top b\quad\text{almost everywhere},$$
*and in a closed system ($b = 0$), $\ell^\top x$ is invariant. Layer 2 alone asserts no such identity for an arbitrary curve: it is a property of the operator, whereas the displayed identity uses Layer 1 as a hypothesis.*

*Proof.* Differentiate the linear readout and use accounting consistency: $\frac{d}{dt}(\ell^\top x) = \ell^\top \dot x = \ell^\top(S_{\mathcal{T}} v + b) = (\ell^\top S_{\mathcal{T}}) v + \ell^\top b = \ell^\top b$. The qualification is immediate from the definitions: if $S_{\mathcal{T}}=0$, every $\ell$ is left-null, yet the curve $x(t)=t$ with $b=0$ does not satisfy the balance law or the projected invariance. □

**Proposition 2 (Non-implications among the defined layers).** *Accounting consistency does not imply barrier safety; barrier safety of a readout curve does not imply accounting consistency; and Layer 2, being a property of $S_{\mathcal{T}}$, does not by itself make an arbitrary curve balanced or safe. No implication involving thermodynamic admissibility is stated, because that predicate is outside the definitions of this paper.*

*Proof.* For the first non-implication, the extinction rest $N\equiv0$ of the closed ledger (2) is an accounting-consistent trajectory and violates every positive lower barrier on $N$. For the second, take a one-compartment formal ledger with $S_{\mathcal{T}}=0$, $C=1$, $b=0$, and barriers $0\le x\le2$; the readout curve $x(t)=1+t/2$ on $[0,1]$ is barrier-safe but is not generated by the balance law, which would require $\dot x=0$. For the third, the same operator has every vector in its left kernel, while the preceding curve still satisfies neither the balance law nor the projected closed-system invariance. Thus the three layers must be audited as the distinct predicates they are. □

**The implication for industrial-ecology measurement.** Mass-balance closure, stoichiometric consistency and barrier compliance must each be audited separately. A single integrated assessment that reports only one of them declares less than it appears to.

**Certification state.** The obligations developed in this section are reported as a vector
$$\mathrm{Cert}=(\mathsf{Typed},\ \mathsf{Balanced},\ \mathsf{Conserved},\ \mathsf{Positive},\ \mathsf{Admissible},\ \mathsf{Safe},\ \mathsf{Adequate\ service},\ \mathsf{Closed}),$$
each entry taking one of three values: established, not established, and not applicable to this
object. The third value is not a failure and the second is not a refutation. The same three values are the
vocabulary of the per-parameter field of the declaration protocol, applied to identification rather than to
proof: a declared parameter is *established* when the observation map pins it, *not established* when the
record leaves it free, and *not applicable* when no identification question is live for it, as for a
normalising convention. Status is a property of the pair (model, record) and never of a parameter alone, so a
value that is unidentifiable for one readout may be identifiable for another, and the field is reported per
readout --- which is the entry-level content of Proposition 39. A classification record
that establishes an accounting identity and nothing else reports $\mathsf{Safe}$ as not applicable,
not as refuted; a record that establishes every entry except closure is not thereby unsafe. The
predicates are separately certified and generally non-equivalent rather than pairwise independent:
the only cross-layer implications available are those explicitly proved from their stated hypotheses,
beginning with Propositions 1 and 2, and an unlisted implication is not available by inference. The
proof obligation attached to each entry, and the certificate vectors of the indicators classified in
Section 6.5, are tabulated in the supplementary material.

### 3.2 The typed safety set

The typed safety set at time $t$ is
$$\mathcal{K}_{\mathrm{safe}}(t) = \{ x \ge 0 : \underline{B}(t) \le Cx \le \overline{B}(t) \},$$
and the non-compensatory assessment reads
$$\mathcal{V}_{\mathrm{typed}} = \{ x(\cdot) : x(t) \in \mathcal{K}_{\mathrm{safe}}(t)\ \forall t \in [0,T] \}.$$
The subscript distinguishes this state-safety set from the flux-feasibility set $\mathcal K(x;b_0)$ of Definition 21. This is a conjunctive, strong-assessment criterion: all moiety barriers must be satisfied simultaneously, and no weighted aggregate $\sum_m w_m S_m$ is used as the decision criterion. The force of that conjunction is the subject of §10.1.

### 3.3 Flux identifiability from a readout trajectory

**Lemma 3 (Flux identifiability under a typed balance law).**
*Let $x : [0,T] \to \mathbb{R}_+^n$ be absolutely continuous, let $v \in L^1([0,T]; \mathbb{R}_+^J)$ and $b \in L^1([0,T]; \mathbb{R}^n)$, and let $S = Cx$ with $C \in \mathbb{R}^{M \times n}$ the moiety-composition matrix. Put $A:=CS_{\mathcal{T}}$.*

*(i) **Forward identity.** If $\dot x(t) = S_{\mathcal{T}} v(t) + b(t)$ almost everywhere, then*
$$S(t) = S(0) + \int_0^t \bigl( A v(\tau) + Cb(\tau) \bigr) d\tau.$$

*(ii) **Inverse fibre.** Conversely, suppose the readout trajectory $S(\cdot)$ and the total non-primitive term $b(\cdot)$ are known. A measurable nonnegative flux history $v$ is compatible with that record if and only if*
$$Av(t)=\dot S(t)-Cb(t)\qquad\text{for almost every }t.$$
*If $v^\dagger$ is one compatible history, the full compatible fibre is, pointwise almost everywhere,*
$$\mathfrak F(S,b)=\bigl(v^\dagger+\ker A\bigr)\cap L^1([0,T];\mathbb R_+^J).$$
*Hence flux histories are unique for every compatible record if and only if $A=CS_{\mathcal{T}}$ is injective. For one fixed compatible history on the boundary of the flux orthant, the sharper pointwise uniqueness condition is*
$$\ker A\cap\bigl(\mathbb R_+^J-v^\dagger(t)\bigr)=\{0\}\qquad\text{almost everywhere},$$
*so a particular boundary record can be uniquely explained even when $A$ is not injective. If the full state $x$ rather than $Cx$ is observed, the same criterion applies with $C=I$ and $A=S_{\mathcal{T}}$. If $b$ is not known, the record constrains only the combination $Av+Cb$; $v$ and $b$ are not separately identifiable without further declared restrictions.*

*(iii) **Sampled records.** Observations $S(t_k)$ determine only the integrated constraints*
$$\int_{t_k}^{t_{k+1}}Av(\tau)\,d\tau=S(t_{k+1})-S(t_k)-\int_{t_k}^{t_{k+1}}Cb(\tau)\,d\tau,$$
*not the pointwise flux history inside a sampling interval, even when $A$ is injective.*

*Proof.* Part (i) is integration of $\dot S=C\dot x=Av+Cb$, legitimate because $x$ is absolutely continuous and $C$ is linear. For (ii), differentiation of the readout gives the displayed linear equation. If $v^\dagger$ solves it, another measurable $v$ solves it exactly when $v-v^\dagger\in\ker A$ almost everywhere; intersecting with the nonnegative histories gives the fibre. If $A$ is injective the fibre has at most one element. If $0\ne w\in\ker A$, choose a constant strictly positive $v_0$ and generate its readout from (i); for all sufficiently small $\varepsilon>0$, $v_0\pm\varepsilon w$ are distinct nonnegative compatible histories, proving necessity of injectivity for uniqueness over all records. The boundary criterion is the same fibre calculation at a fixed $v^\dagger(t)$: a nonzero kernel displacement is feasible exactly when it lies in $\mathbb R_+^J-v^\dagger(t)$. Part (iii) is integration over each sampling interval. □

The direction of inference matters. **Prescribed fluxes:** if $v$ and $b$ are known, part (i) reconstructs the readout by integration without solving a constitutive law. **Observed readout:** part (ii) gives a fibre of possible flux histories, not a reconstruction, unless its injectivity or boundary-uniqueness condition is established. In neither direction do flux data compute the barriers: ecological thresholds, aquifer-collapse limits, and concentration boundaries remain declarations whose satisfaction is then checked.

For a *conserved readout row* $c_m^\top$ satisfying $c_m^\top S_{\mathcal{T}}=0$, write the signed total non-primitive contribution as $c_m^\top b=r_m-h_m$, with $r_m,h_m\ge0$ its positive and negative parts. Only under that row-conservation hypothesis does the sign convention reduce to
$$S_m(t) = S_m(0) + \int_0^t \bigl( r_m(\tau) - h_m(\tau) \bigr) d\tau,$$
with lower-barrier condition
$$S_m(0) + \int_0^t \bigl( r_m(\tau) - h_m(\tau) \bigr) d\tau \ge \underline{B}_m(t).$$
For a non-conserved readout row the internal term $(CS_{\mathcal{T}}v)_m$ must be retained.

### 3.4 The conservation-law projection in integrated form

**Proposition 4 (Conservation-law projection).** *If $(x,v,b)$ satisfies the balance law (1) and $\ell^\top S_{\mathcal{T}} = 0$ for some vector $\ell \in \mathbb{R}^n$, then*
$$\ell^\top x(t) = \ell^\top x(0) + \int_0^t \ell^\top b(\tau) d\tau;$$
*in a closed system ($b = 0$), $\ell^\top x$ is invariant.*

*Proof.* This is Proposition 1 integrated: $\frac{d}{dt}(\ell^\top x) = \ell^\top b$; integrate. □

A conserved moiety is a row $c_m^\top$ of $C$ with $c_m^\top S_{\mathcal{T}} = 0$; then $S_m = c_m^\top x$ satisfies $\dot S_m = c_m^\top b$. In a closed system ($b=0$) $S_m$ is constant; otherwise it changes only through the total non-primitive contribution $c_m^\top b$, which is a boundary flow alone only when the disturbance part is zero or has been separately booked as one. Conservation does not imply barrier safety: if a closed conserved moiety has fixed total stock $S_m(t) = S_m(0)$, a time-varying barrier can become infeasible solely because the barrier moves. The three objects are distinct: the conservation invariant ($S_m$ constant), the barrier tube ($\underline{B}_m \le S_m \le \overline{B}_m$), and the intersection of the invariant manifold with the barrier tube. A conservation law alone does not imply that the trajectory satisfies the barrier. The precise sense is linear: the set $\{x \ge 0 : \ell^\top x = \ell^\top x(0),\ \underline{B} \le Cx \le \overline{B}\}$ may be empty even though each of the three objects is separately well-defined. Barrier–conservation compatibility is a linear feasibility programme, not a slogan.

**Definition 23 (Bounded residual).** Conservation consistency is stated with a declared residual budget for a declared, normalised family $\mathcal L$ of left-null vectors of $S_{\mathcal{T}}$. For each $\ell\in\mathcal L$,
$$\Bigl|\int_0^T\ell^{\top}d_x(t)\,dt\Bigr|\ \le\ \epsilon_\ell(T), \qquad \epsilon_\ell\ \text{declared with the model}.$$
The normalisation matters because both sides scale with $\ell$. Proposition 4 then decomposes exactly as
$$\ell^\top x(T)=\ell^\top x(0)+\int_0^T\ell^\top B_{\mathcal{T}}u_\partial(t)\,dt+\int_0^T\ell^\top d_x(t)\,dt,$$
with the disturbance carried rather than absorbed into a boundary flow. A residual on a moiety readout is the same object only when the readout covector is itself left-null on the state incidence: if $w^\top CS_{\mathcal{T}}=0$, set $\ell=C^\top w$, and then $w^\top Cx$ has residual $\int_0^T w^\top C d_x(t)\,dt=\int_0^T\ell^\top d_x(t)\,dt$. Without $w^\top CS_{\mathcal{T}}=0$, $w^\top C d_x$ may be a readout discrepancy, but it is not the whole change in that readout because the internal term $w^\top CS_{\mathcal{T}}v$ remains. The budget $\epsilon_\ell$ is the quantity material-flow reconciliation books as statistical discrepancy. An envelope computed without it supports no barrier certificate once the residual-inflated envelope leaves the declared barriers. Where no budget is declared for $d_x$, the residual is neither established at zero nor bounded: the predicate carries the gap rather than closing it.

### 3.5 The flux-bounding envelope theorem

**Theorem 5 (Flux-bounding envelopes).**
*Assume:*

*(H1) The primitive fluxes and the total non-primitive term $b=B_{\mathcal{T}}u_\partial+d_x$ satisfy componentwise integrable bounds $v(t) \in [\underline{v}(t), \overline{v}(t)]$ and $b(t) \in [\underline{b}(t), \overline{b}(t)]$ for almost every $t \in [0,T]$. A bound on $B_{\mathcal{T}}u_\partial$ alone may be substituted only with a separately declared bound on $d_x$ and the resulting Minkowski sum for $b$.*

*For any matrix $\mathsf{A}$ write $\mathsf{A}^{+} = \max\{\mathsf{A}, 0\}$ and $\mathsf{A}^{-} = \max\{-\mathsf{A}, 0\}$ entrywise, and define for each moiety $m$ the envelope integrands*
$$\varphi_m(\tau) = (C S_{\mathcal{T}})_{m}^{+} \underline{v}(\tau) - (C S_{\mathcal{T}})_{m}^{-} \overline{v}(\tau) + C_{m}^{+} \underline{b}(\tau) - C_{m}^{-} \overline{b}(\tau),$$
$$\psi_m(\tau) = (C S_{\mathcal{T}})_{m}^{+} \overline{v}(\tau) - (C S_{\mathcal{T}})_{m}^{-} \underline{v}(\tau) + C_{m}^{+} \overline{b}(\tau) - C_{m}^{-} \underline{b}(\tau),$$
*and the envelopes*
$$\underline{S}_m(t) = S_m(0) + \int_0^t \varphi_m(\tau)\, d\tau, \qquad \overline{S}_m(t) = S_m(0) + \int_0^t \psi_m(\tau)\, d\tau.$$
*Then $S_m(t) \in [\underline{S}_m(t), \overline{S}_m(t)]$ for all $t \in [0,T]$ and all $m$.*

*Proof.* By the forward identity in Lemma 3(i), $\dot S_m = (C S_{\mathcal{T}} v + Cb)_m$ almost everywhere. For each row $m$ and time $\tau$, the bilinear form $(C S_{\mathcal{T}})_m v$ is linear in $v$ with coefficient vector $(C S_{\mathcal{T}})_m$, whose positive and negative parts give, over the box $[\underline{v}(\tau), \overline{v}(\tau)]$, the pointwise bounds
$$(C S_{\mathcal{T}})_{m}^{+} \underline{v}(\tau) - (C S_{\mathcal{T}})_{m}^{-} \overline{v}(\tau) \;\le\; (C S_{\mathcal{T}})_m v(\tau) \;\le\; (C S_{\mathcal{T}})_{m}^{+} \overline{v}(\tau) - (C S_{\mathcal{T}})_{m}^{-} \underline{v}(\tau),$$
attained at the extreme points of the box; the same argument applies to $C_m b(\tau)$, and adding gives $\varphi_m(\tau) \le \dot S_m(\tau) \le \psi_m(\tau)$. Integrating over $[0,t]$ yields the stated envelope. □

**Corollary (Flux-derived barrier certificate).** *If $\underline{S}_m(t) \ge \underline{B}_m(t)$ and $\overline{S}_m(t) \le \overline{B}_m(t)$ for all $t \in [0,T]$ and all $m$, then every trajectory compatible with the flux bounds is barrier-safe on $[0,T]$.*

*Proof.* By Theorem 5 every such trajectory satisfies $\underline{S}_m(t) \le S_m(t) \le \overline{S}_m(t)$; the certificate conditions sandwich $S_m$ between the barriers. □

Two qualifications are part of the theorem. 1. **The bounds are conservative.** They hold for *all* flux selections in the declared boxes, including selections that are not jointly realizable by the coupled dynamics. Attainability requires solving or bounding the coupled system. 2. **State-dependence needs one more condition.** When $v=v(x)$, the declared box must additionally be forward-invariant under the coupled dynamics for the envelopes to bound the system's reachable set. And the envelope is an interval computation on the flux data, **not a forecast**. Stoichiometric and donor-limit constraints make the jointly admissible flux selections a polytope, not a box; the tight certificate is the linear programme over that polytope, and the box envelope above is its auditing relaxation — the box is what is audited, the polytope what is realizable. The envelope is the interval-arithmetic counterpart, at the level of declared flux bounds, of the data-reconciliation practice of material flow analysis (Brunner and Rechberger, 2004).

**Worked envelope on the closed block.** On (2) with declared boxes $N \in [0, K]$ and $E \in [0, E_{\max}]$, the mass row of the incidence gives $\dot M = -qEN - C^{A,\mathrm{lim}} \in [-(qE_{\max}K + C^A),\, 0]$, hence $M(t) \in [M(0) - (qE_{\max}K + C^A)t,\ M(0)]$. The conservatism is visible in the extremes: maximal extraction $qE_{\max}K$ is realizable only at $N=K$, where regeneration vanishes, and maximal recharge coincides with minimal extraction — box extremes the coupled dynamics cannot realize jointly.

### 3.6 Finite exhaustion under uniform drift, and its failure mode

**Proposition 6 (Finite exhaustion under uniform negative drift).**
*Assume:*

*(H1) $S$ is absolutely continuous with $\dot S(t) \le -\varepsilon < 0$ whenever $S(t) > B$, where $B$ is a constant lower barrier and $\varepsilon > 0$ a uniform drift bound.*

*(H2) $S(0) > B$.*

*Then the first hitting time satisfies*
$$\tau_B = \inf\{ t \ge 0 : S(t) \le B \} \le \frac{S(0) - B}{\varepsilon}.$$

*Proof.* While $S(t) > B$, the drift bound integrates to $S(t) \le S(0) - \varepsilon t$; the right-hand side reaches $B$ at $t = (S(0) - B)/\varepsilon$, so by continuity of $S$ the crossing occurs no later. □

The uniform-margin assumption is doing all the work, and its absence is the classical failure mode.

**Counterexample (proportional extraction).** For donor-controlled proportional extraction $\dot S=-kS$ with $k>0$ and $S(0)>0$, the stock satisfies $S(t)=S(0)e^{-kt}>0$ for every finite $t$: it approaches zero asymptotically and is never exhausted in finite time, $\tau_0=\infty$. The time to a positive barrier $B > 0$ is $\tau_B = k^{-1}\log(S(0)/B)$, finite for $B > 0$ but diverging as $B \to 0$.*

In particular, the claim that positive extraction implies finite exhaustion is false, and every exhaustion statement must name its referent. Internal transfers do not exhaust a total moiety: in a closed system, internal conversion moves a conserved moiety but does not exhaust it. Exhaustion of a compartment requires one of: a boundary outflow; an irreversible conversion into an uncounted or unavailable form; destruction of the relevant function; or a barrier defined on a particular compartment rather than on the total moiety. Whether "exhaustion" refers to the total conserved moiety, a compartment stock, an accessible or functional stock, a stock above a lower barrier, or an economically recoverable reserve — these are different quantities, and the theorem must specify which (§6.4). The counterexample and this taxonomy are the content of the following named statement, which the rest of this paper uses as its boundary discipline.

**Proposition (Depletion is compartmental).** *On a closed typed ledger, the total mass $\mathbf{1}^\top x$ of each conserved moiety is invariant along trajectories; consequently every finite hitting time of a zero readout is the hitting time of a compartment or of a barrier on a readout, never of total mass, and "exhaustion of the natural block" (Theorems 7 and 14) is transfer across the block boundary into the product, waste, and inert compartments.*

The boundary discipline this proposition fixes is the ecological-economics one of Daly (1990): depletion is not loss of matter. The remainder of this paper keeps that distinction in force.

**Theorem 24 (Critical-margin budget).** Let the declared barrier margins be affine,
$m(x)=Gx+a\ge0$, and let the delivered service rate be $y=c^{\top}v$ with $c\ge0$. Suppose some
$\lambda\ge0$ satisfies $\lambda^{\top}GS_{\mathcal{T}}+c^{\top}\le0$ componentwise, with $\lambda_j$
carrying the units that convert margin $j$ into cumulative service. Here $b$ is the total non-primitive term of Section 2.1, and $v$, $b$, and $y$ are integrable on $[0,T]$. Then $V=\lambda^{\top}m(x)$
obeys $\dot V\le-y+\lambda^{\top}Gb$ along every admissible trajectory, and for every trajectory
that remains inside the declared barriers
$$\int_0^Ty(t)\,dt\ \le\ V(x(0))+\int_0^T\lambda^{\top}Gb(t)\,dt .$$
If additionally $y\ge y_{\mathrm{req}}$ and $\lambda^{\top}Gb\le\beta<y_{\mathrm{req}}$ almost everywhere, then
$T\le V(x(0))/(y_{\mathrm{req}}-\beta)$.

*Proof.* $\dot V=\lambda^{\top}G(S_{\mathcal{T}}v+b)=(\lambda^{\top}GS_{\mathcal{T}})v+\lambda^{\top}Gb\le
-c^{\top}v+\lambda^{\top}Gb$ since $v\ge0$; integrate and use $V(T)\ge0$, which holds because
$m\ge0$ and $\lambda\ge0$. □

The search for $\lambda$ is a linear programme, and its infeasibility is no evidence of safety: it
certifies only that this multiplier family does not close. The theorem bounds how long adequate
service can coexist with componentwise safety; it is not a scalar certificate, and $V>0$
establishes nothing about the sign of any individual margin. The uniform-drift bound above is its
single-margin instance, and the two-sided demand version replaces no statement of Section 5.

---

### 3.7 Composition of ledgers and the calculus of certificates

Everything above is stated for one ledger. Applications assemble ledgers --- a resource module, a
process module, a territory --- and an assembled object inherits its obligations only if the
assembly is itself an object of the theory. This section supplies that missing definition, and with it
the two results the rest of this paper needs: closure is not compositional, and the margin an
interface costs is computable.

**Definition 34 (Composition of typed ledgers).** Let $L_1 = (x^1, v^1, S_1, B_1, C_1)$ and $L_2 = (x^2, v^2, S_2, B_2, C_2)$ be ledgers whose coordinate names have first been made disjoint. An *interface* $\Theta$ declares: a finite set $J$ of pairs representing **the same physical compartment** in the two coordinate systems; a finite set $\Phi$ of directed exchange fluxes with named source and destination compartments; all joint capacity rows created by the assembly; and the rule reconciling boundary and disturbance terms that occur in both parts. Composition is a two-stage construction, and the two stages must not be conflated.

First form the **disjoint coupled composition**: concatenate the states, take $S^0=\mathrm{diag}(S_1,S_2)$ and $B^0=\mathrm{diag}(B_1,B_2)$, and append one column for each directed exchange. In concatenated coordinates a flux from $a$ to $b$ has column $E^0_\varphi=e_b-e_a$. This stage is the whole composition when $J$ is empty.

Second, if $J$ is nonempty, form the **shared-stock quotient**. Let $\mathcal C$ be the equivalence classes generated by $J$, and let $R$ be the class-incidence matrix, $R_{Ca}=1$ exactly when coordinate $a$ represents class $C$. The quotient incidence and boundary operators are
$$S_\Theta=R\,[\,S^0\ \ E^0\,],\qquad B_\Theta=RB^0.$$
Thus $R$ **sums derivative and incidence contributions** incident to the same physical stock. It does not sum the stock itself. The compatible initial quotient state is obtained with a selector $P$ having exactly one $1$ in each class row: $\bar x(0)=Px^0(0)$, defined only when all coordinates in a class have the same initial value. The vector $Rx^0(0)$ would double-count a duplicated stock and is not the quotient state. Likewise, duplicate moiety-readout rows for the same class must have the same coefficients and are retained once; additional distinct service readouts may be retained as distinct functions of $\bar x$, but they do not resurrect a second copy of the stock. A quotient disturbance $d_\Theta=Rd^0$ is used only when the identified entries are distinct additive physical contributions. If they are alternative estimates or two names for one discrepancy, they must be reconciled to one declared term before composition; adding them would manufacture a disturbance.

The composition is *admissible* when all of the following hold on the declared data:

1. **Like with like throughout each class:** type, unit, and moiety-composition coefficients are constant on every $J$-class; equivalently the interface defect counting type/unit/readout mismatches over the generating pairs is zero.
2. **One physical initial stock:** all coordinates in each class agree at the initial time, so the selector state $\bar x(0)=Px^0(0)$ is well defined. Distinct stocks that merely need aggregation are not put in $J$; they require a separate declared aggregation readout.
3. **No double-counted donor or joint capacity:** every capacity incident to the same quotient donor, and every capacity jointly consumed by fluxes from both parts, is represented once as a quotient-level row in the sense of Definition 21. Retaining two separate caps on what is now one drainable stock is inadmissible unless they constrain genuinely distinct resources.
4. **Antisymmetric, donor-limited exchange:** each $\varphi\in\Phi$ is one directed column, not two independently chosen part fluxes. After quotienting it has the form $e_{C_{\mathrm{dest}}}-e_{C_{\mathrm{src}}}$ with distinct source and destination classes, and its rate obeys $0\le f_\varphi(t)\le\bar f_\varphi(\bar x_{C_{\mathrm{src}}}(t),\cdot)$ with $\bar f_\varphi(0,\cdot)=0$. A constant upper box may supplement that donor law; it cannot replace it. If source and destination are identified, the quotient column is zero and the object is not an exchange flux of the composition.
5. **Reconciled non-primitive terms:** boundary transfers and disturbances on identified coordinates are combined by the rule above, so the quotient has one total $b_\Theta=B_\Theta u_{\partial,\Theta}+d_\Theta$ rather than duplicated copies of a single physical term.

At a frozen quotient state the stationary feasible set is therefore
$$\mathcal K_\Theta(\bar x;b_{0,\Theta})=\{(v^1,v^2,f)\ge0:\ R[S^0(v^1,v^2)+E^0f]+b_{0,\Theta}=0,\ \text{all individual and joint capacity rows hold}\}.$$
It is a quotient of a coupled polytope in disjoint coordinates. It is **not**, in general, the fibre product of the two parts' separate stationary polytopes: stationarity is imposed after class rows are summed, and joint rows can couple fluxes that were feasible separately. A fibre-product description is available only after enlarging the part polytopes to expose common interface coordinates and only in the absence of the shared-stock identification and unmodelled joint coupling; it is not the definition of admissibility. A composition failing any condition above is not a typed ledger on the quotient, and no statement below applies to it.

**Definition 35 (Interface price for a disjoint coupled composition).** Suppose $J$ is empty, so the two parts retain distinct compartments, and each part is certified as in Theorem 24, with multiplier $\lambda_i \ge 0$, margins $m_i(x^i) = G_i x^i + a_i$, and readout $y_i = c_i^{\top} v^i$. For a directed exchange $\varphi$ from compartment $a$ in part 1 to compartment $b$ in part 2, its *certificate exchange coefficient*, or interface price, is
\[
\pi_\varphi = \bigl(\lambda_1^{\top} G_1\bigr)_a - \bigl(\lambda_2^{\top} G_2\bigr)_b .
\]
The endpoints are part of the definition. Along the summed certificate $V=V_1+V_2$, this flux contributes $-\pi_\varphi f_\varphi$ to $\dot V$. For a one-way flux bounded by $0\le f_\varphi\le\bar v_\varphi$, the sharp worst-case weakening of the summed cumulative-service budget over $[0,T]$ is therefore
$$(-\pi_\varphi)^+\bar v_\varphi T,$$
not $|\pi_\varphi|\bar v_\varphi T$. The absolute value is a looser symmetric bound, appropriate for a reversible or orientation-unspecified flux, not a directed one. When $\pi_\varphi\ge0$ the interface is *free for this aggregate certificate* in the narrow sense that it does not weaken that upper-bound budget; it can still drain an individual compartment or violate an individual margin, and Theorem 24's summed $V$ does not certify those componentwise facts. Reversing the physical direction swaps source and destination and recomputes $\pi$; it is not a relabelling that automatically moves an equal charge to the other ledger. In a nonempty shared-stock quotient there are no two copies of an identified compartment between which a pair price can be charged: margins and multipliers must be recertified on the quotient operator $S_\Theta$, with every quotient column included. Additivity of the pairwise corrections is asserted for directed exchanges in a two-part disjoint coupling; multi-part or shared-stock assemblies need the corresponding global quotient certificate.

An equality-row representation is sometimes useful as a *consistency test*—keep both coordinate copies and ask whether $x_a^1=x_b^2$ for every $(a,b)\in J$—but it is not the same dynamical object as the quotient. If each copy continued to evolve only under its own part's fluxes, equality for all time would require the two copies' separate net derivatives to agree; in the physical quotient, by contrast, the one stock receives the sum of all incident derivative contributions. Those conditions coincide only under additional synchronisation hypotheses that Definition 34 does not make. The quotient is therefore the composition used below. It is meaningful only when type, unit, and readout coefficients agree throughout each class, in the sense of Definition 47. Nor does the construction carry certificates across on its own: descent of a conservation law is the pullback condition of Proposition 36, and descent of a margin certificate requires checking the multiplier inequality against every column of $S_\Theta$, including columns contributed by the other part to a shared stock.

**Proposition 36 (Conservation pullbacks compose; closure capacities need not).** Let $\Theta$ be admissible, with $S^0$, $E^0$, and $R$ as in Definition 34. A quotient covector $\bar\ell$ is a conservation covector of the composition, $\bar\ell^\top S_\Theta=0$, if and only if its pullback $\ell=R^\top\bar\ell$ satisfies all three conditions
$$\ell_1^\top S_1=0,\qquad \ell_2^\top S_2=0,\qquad \ell^\top E^0=0.$$
The last condition says that, for every directed exchange, the covector values at its destination and source agree after class pullback. Thus the surviving part-covectors are exactly the part-wise left-null pairs that are constant on every $J$-class and have equal values at exchange endpoints. The pullback $R^\top$ is injective but need not be onto that part-wise product: a separate part conservation can fail to descend because its values disagree on an identified stock, or because an exchange joins coordinates carrying different values. Closure at a demanded rate also need not compose: the state-conditioned closure capacity of the composition can be strictly below the minimum of the parts' capacities once a joint capacity is represented. Instance: two cycles each demand $1$ unit per year and separately have return capacity $1$, so each has $\Lambda^{*}=1$ at its declared frozen state. If the composed declaration correctly replaces the two apparently separate caps by one shared return capacity $q+s\le1.5$, the combined demand $(1,1)$ has $\Lambda^{*}=0.75$. The number $1-\Lambda^{*}=0.25$ is a stationary capacity shortfall relative to that demanded pattern. It is not Definition 22's $\delta_m^{\mathrm{use}}$ or $\ell_m$, and it does not by itself fix a drawdown rate: Definition 21 leaves open whether the gap is met from a buffer or pipeline, by a changed boundary/capacity declaration, or not met.

*Proof.* By Definition 34, $\bar\ell^\top S_\Theta=\bar\ell^\top R[S^0\ E^0]=(R^\top\bar\ell)^\top[S^0\ E^0]$. Block diagonality of $S^0$ gives the two part conditions, and the exchange columns give $\ell^\top E^0=0$; the converse is the same calculation. A vector in the image of $R^\top$ is constant on classes, proving injectivity and the characterisation of the image. Non-surjectivity has elementary witnesses: with two zero-incidence one-compartment parts, $(1,0)$ is part-wise left-null but is not constant on a class identifying the compartments; with $J$ empty and one exchange $a\to b$, the same pair fails the endpoint equality, while $(1,1)$ descends. For the closure instance the composed programme is $\max\mu$ subject to $q=\mu$, $s=\mu$, $q+s\le1.5$, $q,s\ge0$, whose optimum is $0.75$; separately, $q\le1$ and $s\le1$ give optimum $1$. □

**Proposition 37 (Interface correction to a summed certificate budget).** Let $\Theta$ be an admissible **disjoint** coupled composition ($J$ empty), and let each part satisfy Theorem 24 with budget $B_i = V_i(x^i(0)) + \int_0^T \lambda_i^{\top} G_i b_i\,dt$, where $b_i$ is that part's total non-primitive term. For directed exchanges $\varphi$ with $0\le f_\varphi\le\bar v_\varphi$ and prices $\pi_\varphi$ as in Definition 35, every barrier-respecting trajectory of the composition satisfies
\[
\int_0^T\bigl(y_1(t)+y_2(t)\bigr)\,dt
\ \le\
B_1+B_2+\sum_{\varphi\in\Phi}(-\pi_\varphi)^+\,\bar v_\varphi\,T .
\]
The final sum is the sharp worst-case *certificate-budget correction* for this multiplier pair and these one-way boxes. Replacing $(-\pi_\varphi)^+$ by $|\pi_\varphi|$ gives a valid but generally weaker bound. The two part budgets add with no correction exactly when every directed exchange with $\bar v_\varphi>0$ has $\pi_\varphi\ge0$. This is not a physical “margin needed” and it is not an admissibility threshold for the exchange rate: the inequality holds at every $L$, with a weaker right-hand side as $L$ grows. If a reporting convention declares an allowable budget weakening $\Delta\ge0$, then for one exchange of box $[0,L]$ the corresponding allowance-relative condition is
\[
(-\pi)^+LT\le\Delta,
\qquad\text{equivalently}\qquad
L\le \frac{\Delta}{(-\pi)^+T}\ \text{when }\pi<0,
\]
with no finite restriction from this certificate when $\pi\ge0$. Choosing $\Delta=B_1+B_2$ is one possible reporting convention, not a theorem about safe composition. Another multiplier pair, or a quotient-level certificate, can give a different correction; on a shared-stock quotient Proposition 37's pair formula does not apply until Theorem 24 has been recertified on $S_\Theta$. Instance: $G_1=G_2=1$, $b_1=b_2=0$, $\lambda_1=1$, $\lambda_2=2$, and a directed flux from part 1 to part 2, so $\pi=1-2=-1$. At $T=30$ yr the correction is $6$ at $L=0.2$ and $15$ at $L=0.5$; against a declared allowance $\Delta=9$, the allowance-relative rate is $0.30$ unit per year. Reversing the physical flux gives $\pi_{\mathrm{rev}}=2-1=+1$ and zero correction *to this summed upper-bound certificate*, although the reversed flux may still stress an individual margin. Merely interchanging labels changes nothing physical.

*Proof.* Take $V=V_1+V_2$. Along the disjoint composition,
$$\dot V\le-(y_1+y_2)+\lambda_1^\top G_1b_1+\lambda_2^\top G_2b_2-\sum_\varphi\pi_\varphi f_\varphi,$$
because a directed exchange removes one unit from its source coordinate and adds one to its destination coordinate, each priced by its own part's multiplier row. On a one-way box,
$$\max_{0\le f\le\bar v_\varphi}(-\pi_\varphi f)=(-\pi_\varphi)^+\bar v_\varphi\le|\pi_\varphi|\bar v_\varphi.$$
Integrate over $[0,T]$ and use $V(T)\ge0$ on a barrier-respecting trajectory. The allowance-relative formula is the one-exchange correction solved for $L$. □

**Definition 40 (Compensation as a decidable predicate).** Fix a partition of the declared
compartments into donor and recipient sides, a demanded service rate, and the joint polytope of the
composition. *Compensation holds at fraction $\kappa$* when one linear programme on that polytope is
feasible: maximise the recipient's sink-weighted margin release net of the donor's, subject to the joint
polytope, to the demanded service, and to the donor's budgets being drawn at no more than $\kappa$ times
what its own service costs; the predicate is true when the optimum covers the demanded drawdown. It is a
feasibility test on the quotient joint polytope rather than a price comparison, and it is the exact form of the
question the aggregation cannot answer. Prices do not substitute for it: the shared return capacity that
leaves each of the two cycles of Proposition 36 closing at $\Lambda^{*} = 1$ individually puts the
composition at $\Lambda^{*} = 0.75$, and cutting one side's own return capacity to $10^{-4}$ units per
year leaves that shared-capacity programme well posed and finite while the cut side cannot close at all.
Substitutability is decided by the joint programme, not by whether a capacity price is finite.
The verdict has three branches and they should not be collapsed. Feasibility establishes steady-rate
compensation *under the declared inputs*. Infeasibility establishes failure of that programme, and it comes
with its own witness: a nonnegative combination of the constraint rows of the displayed system reducing to
$0 \le -1$, the linear-programming alternative read in the direction that certifies failure rather than the
one that certifies safety. Where the declaration is incomplete --- a substitution column missing, a shared
constraint unlisted, a target unnamed --- neither branch is available, and the predicate is reported as not
established, which is a statement about the declaration and not about the ledger. The programme is a
steady-rate object throughout: it says nothing about the trajectory between endpoints, and it establishes no
dynamic safety, no exit-time bound and no corridor invariance; those are the questions of Sections 3.5 to 3.6
and they need their own hypotheses. A positive interface charge does not prohibit compensation either: it
prices it, and with adequate stock, capacity and budget the composition may close --- which is why the charge
enters the certificate budgets of Proposition 37 and never Definition 34's admissibility conditions.

**Remark 34 (What the multiplier search can and cannot prove).** The certificates above search over the
conservation multipliers $\lambda$ alone, because those are what the declared conservation structure
supplies; the capacity and box rows of the declared polytope carry no multiplier, and the gap is visible
in a single-compartment example: with $\dot m = -y + \sigma$, $y \in [0, 1]$, $m(0) = \sigma(0) = 0$
and $m(T) \le 1$, a certificate built from $\lambda$ only returns $100.0$ units of cumulative service
where the exact value over the horizon is $1.0$, and pricing the capacity row as well --- the full dual
pair $\lambda = 0$, $\rho = 1$ --- returns $1.0$ exactly. The same refinement applies to the interface
bound of Proposition 37. In the other direction the search is complete for the terminal affine relaxation
of a linear differential inclusion, and on the joint polytope exactness follows from Proposition 37's
joint programme; it is not complete for quadratic certificates, since a valid quadratic margin need not be a sum
of squares --- Motzkin's polynomial is the standard non-negative-not-sum-of-squares obstruction --- so a
search restricted to diagonal multipliers and sums of squares can miss a certificate that exists, and that
failure is no evidence of unsafety.

Two dependencies belong with this reading. The interface price of Definition 35 is a *certificate-relative*
number: with unit service coefficients on both sides, $\lambda = (2,1)$ and $\lambda = (1,2)$ are both
feasible part certificates for the same pair of drain ledgers, and they return $\pi_\varphi = +1$ and
$\pi_\varphi = -1$ for the same declared exchange. Physical admissibility cannot turn on which certificate was
quoted, and here it does not: Definition 34's admissibility conditions involve no multiplier, and
Definition 40's programme decides substitution without reference to either sign. What is certificate-relative
is the charge's size, so it is reported with the certificate that produced it, not as a property of
the interface. A capacity multiplier is a selection in the same sense: the value of the shared-capacity
programme is a concave function of the capacity, at a kink its subdifferential is an interval --- in the
two-cycle instance of Definition 40, where the capacity equals the sum of the two cycles' own returns, that
interval is $[0, 1]$ in units of one cycle's marginal return --- and its one-sided derivatives at the kink
differ. A single quoted price there is a convention, and it is properly named as a supergradient of the value
function, not as the shadow value of the capacity.

**Definition 41 (Control margin).** Let $(\mathcal K_\rho)_{\rho \ge 0}$ be the declared nested family of
corridor sets. The *control margin* of a state is
$$\mu(x_0) \;=\; \sup\{\, \rho \;:\; x_0 \in \mathcal K_\rho \,\}.$$
Two readings are licensed and no third is: with a normalised margin $\mu$ is dimensionless, and it is a
min-type quantity in the sense that $\mu(x_0) \ge \rho$ if and only if $x_0 \in \mathcal K_\rho$, so what it
answers is whether a declared corridor contains the state. It prices no recovery, it bounds no exit time on
its own, and it inherits every conservatism of the envelope that produced the family.

**Definition 42 (Affinity, the fourth admissibility predicate).** Conservation, capacity and typing
(Definition 47) are the three predicates a declared flux must pass. Where the declaration also carries a specific Gibbs energy
$g_j$ for each compartment, a fourth is available: a conversion with stoichiometric row $\nu$ (products
positive) has *affinity* $\mathsf{A} = -\nu^{\top} g$, and the conversion is admissible only when
$\mathsf{A} \cdot J \ge 0$ along its declared rate $J$ --- equivalently, only when it does not raise the
total Gibbs energy in the direction it is booked. A flux with $\mathsf{A} \cdot J < 0$ is not a noisy
observation of an allowed process but an impossible one, and the reparation is to re-declare the ledger,
never to re-estimate the flux. Where energies are not declared the predicate is reported as not
established, exactly as the conservation residual of Definition 23 is.

**Proposition 40 (An empty corridor comes with a named conflict).** For declared bounds $A v \le b$ and
declarative identities $C v = d$, the corridor $\{v : A v \le b,\ C v = d\}$ is empty if and only if there
are $y \ge 0$ and free $z$ with
\[
y^{\top} A + z^{\top} C = 0 \qquad \text{and} \qquad y^{\top} b + z^{\top} d \;<\; 0 .
\]
Any such pair is a *corridor-infeasibility witness*, and its support --- the rows with $y_i > 0$ --- names
the declared floors and ceilings that cannot hold at once. The empty-corridor findings of Section 6.5 are of
this kind: they say not that the system is unstable but that the declaration is jointly unsatisfiable, and
the remedy is to withdraw a bound, not to re-tune a controller.

*Proof.* Append the identities as $C v \le d$ and $-C v \le -d$ and apply Gale's theorem of the
alternative (Gale, 1957; Ahuja et al., 1993): its second system is the displayed pair, with $z$ the
difference of the two multiplier blocks and the strict inequality normalised from $-1$. □

**Definition 43 (Circulation time).** On a stationary pattern in which a cycle of $n$ pools carries the
common rate $q > 0$ past masses $m_1, \dots, m_n$, the *circulation time* is
$$\tau^{\mathrm{circ}} \;=\; \frac{\sum_i m_i}{q} \;=\; \sum_i \frac{m_i}{q} ,$$
the mean time a unit of the moiety takes per revolution of that cycle. It is a property of the declared
pattern, not of a trajectory, and it is not any pool's residence time: stationarity forces one common rate
around a simple cycle, so a pool that several cycles share has a residence time per source rather than one
overall, and where several cycles coexist the quantity is a vector indexed by cycle --- a scalar quotation
must name its cycle. Yield inflation is invisible here by construction: a demand met with no stationary pattern behind it
has no circulation time to report, which is the statement of Section 6.6 in reciprocal units.
**Definition 44 (Governability ratio).** Let $h$ be the declared review interval of Section 9, $\tau$ the
declared response delay of the assessment channel, and $T_{\mathcal{K},m}$ the margin-return time of moiety
$m$: the time its margin needs to re-enter the declared corridor $\mathcal K$ under the command in force.
The *governability ratio* is
$$G_{\mathcal{K},m} \;=\; \frac{T_{\mathcal{K},m}}{\tau + h} .$$
The reading is a comparison of clocks, not a stability theorem. Where $G_{\mathcal{K},m} > 1$ the corridor is
left and re-entered faster than the periodic assessment can act on it, so review cannot be the instrument
holding that moiety and only the automatic triggers named with the declaration act within the corridor's own
time scale; where $G_{\mathcal{K},m} \le 1$ the channel acts at least once per excursion. The ratio is
dimensionless and per moiety, so a scalar quotation must name its moiety and its corridor. In the registered
delay family of the companion analysis the same comparison sits between the two thresholds reported there: the
regime change its owner reports near $\tau \approx 3.7$ yr, and the review interval above which the same
analysis reports restabilisation, about $6.5$ yr (Section 9). Both are witnesses inside a declared model, not
constants for the class.

**Lemma 4 (A moving baseline contributes a covariance term).** For an index reported as the difference
$Y - B$ of an estimate and its own baseline,
$$\operatorname{Var}(Y - B) \;=\; \operatorname{Var} Y + \operatorname{Var} B - 2\operatorname{Cov}(Y, B) ,$$
so a declining reported anomaly is compatible with a stationary process whose baseline alone moved: the part
of the variance manufactured by the baseline is $\operatorname{Var} B - 2\operatorname{Cov}(Y, B)$, and it is
invisible unless both are declared. This is the covariance form of a warning the index already carries, and
it is why an anomaly is reported together with the construction of its baseline rather than against an
implicit one.

*Proof.* When the second moments are finite, this is bilinearity of covariance applied to $Y-B$. □

**Definition 45 (Latest safe intervention time).** Fix the full initial condition/history $\mathfrak h_0$ on which the future trajectory depends: the state $x_0$, the mobilisation/return history (equivalently the pipeline stocks $W_m(0)$ under Definition 22), the return kernels and capacities, the barrier family, the baseline service vector, and a declared class of delayed intervention responses. An intervention *initiated at time $L\ge0$* follows the no-intervention dynamics on $[0,L]$ and an admissible response from the declared class thereafter. It is safe and service-preserving if the resulting trajectory remains in $\mathcal K_{\mathrm{safe}}(t)$, maintains the declared service, and reaches a declared admissible non-liquidating operating condition. The latest safe intervention time from $\mathfrak h_0$ is
$$t_{\mathrm{last}}(\mathfrak h_0):=\sup\{L\ge0:\text{ a safe, service-preserving intervention initiated at }L\text{ exists}\},$$
with the conventions $t_{\mathrm{last}}=-\infty$ if no initiation time is feasible and $t_{\mathrm{last}}=+\infty$ if every finite initiation time is feasible. It is a feasibility deadline, not a forecast.

No formula depending only on a current stock margin and current net decline is asserted at this level. Two histories can have the same available-stock margin and the same current $d_0=g_0-r_0$, yet different deadlines: in one a financed pipeline is about to return, so future $r(t)$ is high; in the other the pipeline is empty and the same instantaneous net decline has no imminent returns behind it. Where a disturbance class is declared, the quantifier order must also be declared: “there exists one response policy that works for every declared disturbance” and “for each disturbance there is a response chosen with knowledge of it” define different deadlines.

**Proposition 41 (Scalar frozen-drawdown deadline).** Specialize Definition 45 to one available support pool with barrier $A_{\min}$, margin $m_0=A_0-A_{\min}>0$, and scalar dynamics $\dot A=-d(t)$ throughout the transition. Assume that an intervention initiated at $L$ leaves $d(t)=d_0>0$ on $[0,L+\tau]$ (postponement plus unavoidable implementation delay), after which $d$ is absolutely continuous, $\dot d\ge-\rho$ and $d\ge0$; assume further that reaching $d=0$ is the declared service-preserving terminal condition and that no constraint other than $A\ge A_{\min}$ binds. For initiation at $L=0$, the least attainable further stock loss is
$$m_{\mathrm{needed}} \;=\; d_0\tau + \frac{d_0^{2}}{2\rho} .$$
A safe transition initiated at $L\ge0$ exists if and only if $d_0L+m_{\mathrm{needed}}\le m_0$. Hence the *signed latest-initiation slack* is
$$t_{\mathrm{last}}^{\mathrm{sgn}} \;=\; \frac{m_0-m_{\mathrm{needed}}}{d_0}=\frac{m_0}{d_0} - \tau - \frac{d_0}{2\rho} \;=\; H^{\mathrm{loc}} - \tau - \frac{d_0}{2\rho} ,$$
where $H^{\mathrm{loc}}=m_0/d_0$. If $t_{\mathrm{last}}^{\mathrm{sgn}}\ge0$, it equals $t_{\mathrm{last}}(\mathfrak h_0)$ for this scalar specialization. If it is negative, no nonnegative initiation time is feasible; its magnitude is the amount by which initiation would have had to precede the present under the same frozen backward scenario. Here $d_0$ is the declared net decline of the *available* pool in this specialization. Definition 22 can decompose such a decline into pipeline filling, late-return timing, and ultimate loss, but neither $\delta_m^{\mathrm{use}}$ nor $\ell_m$ alone determines $d_0$ without the return history. The deadline and the frozen-rate horizon differ by the physical costs of implementation delay and finite ramp speed; the gap is not a discount applied to a horizon.
Illustration, declared as illustrative and not empirical: $m_0 = 100$ units, $d_0 = 10$ units per year,
$\tau = 2$ yr, $\rho = 1$ unit per year per year gives $H^{\mathrm{loc}} = 10$ yr and $m_{\mathrm{needed}} = 70$,
so ten years of frozen-rate coverage leaves three years before initiation must begin: $t_{\mathrm{last}}^{\mathrm{sgn}} = 10 - 2 - 5 = 3$ yr. With $m_0 = 25$, $d_0 = 4$, $\tau = 3$ yr and $\rho = 0.5$, the frozen-rate ratio reads $6.25$ yr while $t_{\mathrm{last}}^{\mathrm{sgn}} = -0.75$ yr: no initiation at or after the present is feasible in that scalar scenario. Proposition 26 does not license replacing $H^{\mathrm{loc}}$ by a stock-dependent true horizon $T$ in this formula. It compares uncontrolled hitting times only; with a stock-dependent baseline or return history, the controlled loss before and during the ramp changes as well, and the deadline must be recomputed from Definition 45.

*Proof.* For initiation at $L$, the loss on $[0,L+\tau]$ is fixed at $d_0(L+\tau)$. After $s=L+\tau$, the slope constraint and $d(s)=d_0$ imply $d(t)\ge[d_0-\rho(t-s)]_+$. The pointwise smallest admissible ramp is therefore $d(t)=[d_0-\rho(t-s)]_+$, whose remaining integral is $d_0^2/(2\rho)$. Thus the minimum total loss is $d_0L+d_0\tau+d_0^2/(2\rho)=d_0L+m_{\mathrm{needed}}$, and safety is exactly the condition that this not exceed $m_0$. Solving for $L$ gives the signed slack and the stated interpretation of its sign. □

**Definition 46 (Supportable-output envelope).** For a declared ledger, initial state $x_0$, initial mobilisation/return history $\mathfrak h_0$ (equivalently the initial pipeline stocks $W_m(0)$ when return kernels are used), admissible control or flux-law class, barrier family, and horizon,
$$\mathcal Y(T;x_0,\mathfrak h_0) \;=\; \bigl\{\, y \ge 0 \;:\; \exists\ \text{an admissible trajectory from }(x_0,\mathfrak h_0)\text{ on } [0,T]
\ \text{with service at least } y \ \text{throughout and } x(t) \in \mathcal K_{\mathrm{safe}}(t) \ \forall t \bigr\}$$
is the set of constant service-rate vectors supportable for the whole horizon under that full declaration. Three readings and no fourth. For fixed $(x_0,\mathfrak h_0)$ and admissible class, the set is decreasing in $T$ by restriction, so an envelope number is always at least a triple (rate, horizon, initial state/history). A single quoted rate is a selection from the set, and Proposition 29 says which selections can be certified aggregators; the envelope itself is the report. At the scalar frozen-rate corner of Definition 22—constant mobilisation $g_m$, no other replenishment, and a barrier margin $m_0$ measured on the combined circulation stock $A_m+W_m$—the outer empty-horizon bound is $m_0/(\ell_mg_m)$ when $\ell_m>0$, because only ultimate non-return liquidates $A_m+W_m$. If the barrier is instead on available stock $A_m$ alone, emptiness can occur earlier and depends on the whole kernel and pipeline history; if $\ell_m=0$ and the pipeline is already financed, ultimate loss does not empty the envelope at all. The old $\delta_m^{\mathrm{use}}$ may replace $\ell_m$ only when $d_m^{\mathrm{late}}=0$. A published “years of supply” therefore measures a declared stock, barrier, history, and drawdown mechanism together, never the stock alone.

**Remark 35 (What a non-displacement gate can say on this apparatus).** An additionality or non-displacement claim is a comparison of two declarations, not a forecast of a counterfactual world. On this apparatus it is a joint-feasibility gate on the admissible quotient of host and project: the intervention is non-displacing at the declared state, boundary schedule, capacities, and horizon only if there exists an admissible composed trajectory or stationary pattern that simultaneously (i) delivers the host's baseline service vector, (ii) delivers the project's claimed additional service vector, (iii) respects the host's barrier and pipeline-history constraints, and (iv) does not increase the relevant ultimate-loss rates $\ell_mg_m$ or other declared drawdown rates above their host-baseline values, except where an explicitly declared replenishment in the project covers that increase. A change in a single closure-deficit number is neither necessary nor sufficient: $\delta_m^{\mathrm{use}}$ can improve by bringing returns earlier while host service is displaced, and it can worsen through a longer pipeline while joint feasibility and ultimate loss are unchanged. The gate is checkable from the declarations and fails in the ordinary way—a project that relabels an existing mobilisation cannot meet clauses (i) and (ii) at once when the shared capacity is represented once on the quotient. What the gate cannot say is carried by its baseline: the host ledger is declared, not estimated, and where the two declarations share a compartment all quantities are read on the quotient, not added across duplicate coordinates.
These three statements are the calculus the account's own citations had deferred to a companion: an
object of composition, the predicate that survives it, and the number that prices what does not. No
further deferral is made here, and nothing in Sections 4 to 10 depends on a claim about composition
that is not proved above.
### 3.8 The type structure the operator's subscript abbreviates

**Definition 47 (Type structure).** Equation (1) writes the incidence operator as $S_{\mathcal{T}}$, and the
subscript has not been defined. It is not decoration. The sentence of Section 2.1 that entries may be added
within a row "only when their types and units agree", the requirement that a disturbance $d_x$ be itself typed,
Definition 42's listing of typing as one of the three predicates a declared flux must pass, and Section 6.5's
charge that a score mixes objects which are incommensurable under the typing it invokes --- all of these
presuppose an object that is never given. A *type structure* $\mathcal{T}$ on a ledger is a single declaration consisting of three
items: a set $\mathsf{Ty}$ of types; for each compartment $i$, a type $\mathrm{ty}_i \in \mathsf{Ty}$ and a
unit $\mathrm{un}_i$, so that an entry of the state vector carries the pair
$(\mathrm{ty}_i, \mathrm{un}_i)$ rather than a number alone; and a declared set $\mathsf{Cv}$ of *conversion
templates*. A template is a named, finitely supported stoichiometric coefficient vector $\nu$, with negative entries at its declared inputs and positive entries at its declared outputs, together with the unit in which one unit of the associated process flux is measured. The elementary pair template with entries $-c$ at a type-$\alpha$ input and $+1$ at a type-$\beta$ output is the special case read as "one unit of $\beta$ is obtained from $c$ units of $\alpha$ by that process"; multi-input, multi-output and fractional-yield processes use the full vector $\nu$, not a fictitious sequence of pair conversions. Nothing in this list is derived from the stoichiometry; all of it is declared alongside it.

Admissibility then has content. A sum $\sum_{i \in I} x_i$ is admissible as one ledger quantity only when
$\mathrm{ty}_i$ and $\mathrm{un}_i$ agree for every $i \in I$; across types there is no typed sum, only an explicitly declared conversion process (or an additional untyped numerical readout, in the sense of Proposition 42). A primitive/process flux is *typed-admissible* when its column is of exactly one of two kinds.
(i) A **transfer/routing column**: all compartments in its support have one type and one unit, and, after the process-flux unit is declared, its entries sum to zero. The elementary transfer $-e_a+e_b$ is included, and so is a split-routing column $-e_a+\sum_k\theta_k e_{b_k}$ with $\theta_k\ge0$ and $\sum_k\theta_k=1$—the form used by the harvest and retirement splits in Theorem 8. Any routed remainder must have an explicit destination compartment or boundary entry; it cannot disappear from the column.
(ii) A **conversion column**: the column is a positive scalar multiple of one declared template $\nu\in\mathsf{Cv}$, with its support, input/output signs, stoichiometric coefficients, and process-flux unit exactly as declared. The pair column $-c e_a+e_b$ is the elementary special case.
No column is both kinds unless its support lies in one type and it is declared as a transfer. The same support discipline applies to the rest of the ledger interface: a boundary column, a disturbance entry, and a typed scalar readout each belong to one declared row family, or are carried explicitly as a tuple of such objects; a boundary process that converts types is represented by a conversion column carrying its declared template. Where the declaration draws no type distinction beyond units, every admissible column is a transfer/routing column and
the predicate is reported as not applicable, not as passed. Changing $\mathsf{Ty}$, $\mathrm{ty}$ or
$\mathsf{Cv}$ is a change of ledger and not a change of notation: the admissible stationary set $\mathcal K(x;b_0)$ of
Definition 21 is defined through $S_{\mathcal{T}}$, so it moves with the declaration, and every certificate
built on that set moves with it.

**Proposition 42 (Conservation decomposes by type class; no typed scalar conservation readout crosses classes).** *Form the graph on $\mathsf{Ty}$ in which two types are joined when they occur together in the support of one conversion template in $\mathsf{Cv}$ (equivalently, each template support is a clique), call the pullback of a connected component a type class, and let $I_\gamma$ be the compartments of class $\gamma$. In the typed category of Definition 47 the state is the tuple $x=(x_\gamma)_\gamma\in\prod_\gamma\mathbb R_+^{I_\gamma}$, and a typed scalar readout is supported on one class; a multi-class readout is a tuple of class readouts. No admissible column of $S_{\mathcal{T}}$ has nonzero entries in two distinct classes, and for a permutation of rows and columns*
$$S_{\mathcal{T}} \;=\; \bigoplus_{\gamma} S_{\gamma}, \qquad \ker S_{\mathcal{T}}^{\top} \;=\;
\bigoplus_{\gamma} \ker S_{\gamma}^{\top} .$$
*Consequently every ambient conservation covector decomposes uniquely as a tuple of class-supported conservation covectors, and every typed scalar conservation readout is carried by one class. If the class quantities are separately invariant, their numerical sum in an ambient untyped vector space is of course also invariant; that sum is the compression of a tuple by an additional cross-class addition, not a typed scalar conservation law of the ledger. It becomes one only under a new declaration that merges the classes or declares the cross-class readout and its conversion semantics, after which the residual and composition rules must be rechecked. No typed conserved quantity prices one class against another.*

*Proof.* A transfer/routing column meets one type, hence one class, whether it is an elementary $\pm1$ transfer or a fractional split with destination coefficients summing to one. A conversion column is supported on the support of one template, and all types in that support lie in one connected component by the graph construction. Therefore every admissible column is supported in a single class, which is block diagonality after grouping rows and columns by class. A covector $L$ satisfies $L^\top S_{\mathcal{T}}=0$ if and only if every class restriction satisfies $L_\gamma^\top S_\gamma=0$, giving the kernel splitting and unique decomposition $L=(L_\gamma)_\gamma$. By Definition 47, a typed scalar readout must be supported on one class; a covector with several nonzero class components is therefore the tuple of its class readouts. Adding those components' numerical values is an extra untyped readout operation, even when invariance of the sum follows from invariance of the parts. □

**Remark 36 (What the type structure yields, and what it does not).** Three consequences are worth separating,
because the literature runs them together. *Reporting boundaries.* A pure relabelling of a fixed numerical operator and a fixed admissible-column set does not change the ambient set $\ker S_{\mathcal{T}}^\top$; linear algebra does not see report names. Changing the type declaration is a different act when it declares or withdraws a conversion, removes columns that were admissible only as same-type transfers, or changes which readouts count as typed scalars. Any of those can change the classes, the admissible flux set, and the typed conservation readouts. Merging two report labels without a conversion declaration does not create a typed cross-class scalar, and splitting a label can destroy formerly admissible transfers. That is the exact scope of the invariance: names alone are invariant, declarations are not. Redrawing a shared-stock boundary inside a class is decided by Proposition 36's pullback condition, not by this remark. *Valuation.* The predicate is a
well-posedness condition on declarations, not a thesis about worth. It says that a ledger which has added a
gigajoule to an hour of labour has not declared what it did; it says nothing about whether the two are
comparable in worth. A material-and-energy-value position stated as a substantive claim about worth is
therefore not a corollary of this apparatus, and this paper does not make it: what is available here is the
position's checkable content --- Definition 47's predicate, and Proposition 29's aggregator, which does not
compensate a deficit in one compartment with a surplus in another. *Reclassification.* A reserve class entering or leaving an asset boundary is not, without more, a change of $\mathsf{Cv}$; it is a boundary or classification transfer governed by its own declared law—for the reserve-life model, the reclassification elasticity $\eta$ of Proposition 28. Definition 22 enters only if that act also changes a return kernel, pipeline history, capacity, or ultimate-loss share. The statistical standards recalled in Section 1.2 draw their own asset boundary in economic terms of exactly that kind, so the exposure is common to the frameworks rather than peculiar to this one, and it is a reason the horizon readouts of Section 6 state the operative mechanism—reclassification, return lag, or ultimate loss—rather than attaching an undifferentiated “deficit”.

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

*Proof.* Every column is a same-unit transfer/routing column in the sense of Definition 47: either an elementary two-compartment transfer with entries $-1$ at the donor and $+1$ at the recipient, or a split-routing column with donor entry $-1$ and nonnegative destination entries summing to $1$. Opposite one-way primitives implement two-way exchanges. In both forms the column sum is zero, so $\mathbf{1}^\top S_{\mathcal{T}} = 0$ and $\mathbf{1}^\top \dot X = \mathbf{1}^\top S_{\mathcal{T}} F = 0$. The theorem is an exact conservation identity under the routing constraints. □

The seven-compartment incidence claimed by Theorem 8 is displayed here — in the compartment order of its statement, with the closed block's primitive fluxes, the pattern of the six-compartment $S(\alpha,\rho_P)$ of Theorem 9 with the inert column (no outflow from the inert compartment) appended, and the harvest column split by $(\alpha,1-\alpha)$. Rows $(N, P, W, I, U, A^{\mathrm{act}}, A^{\mathrm{geo}})$; columns gross regeneration, density-dependent return, harvest, uptake, detritus return, $e_{GA}$, $e_{AG}$, mining (to product), product retirement, inert-bound transfer (waste $\to$ inert):
$$S_{\mathcal{T}} =
\begin{pmatrix}
1 & -1 & -1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 1-\alpha & 0 & 0 & 0 & 0 & 1 & -1 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1-\rho_P & -1 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 \\
0 & 0 & \alpha & 1 & -1 & 0 & 0 & 0 & \rho_P & 0 \\
-1 & 1 & 0 & -1 & 1 & 1 & -1 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & -1 & 1 & -1 & 0 & 0
\end{pmatrix}.$$
Every column is either an elementary two-compartment transfer or a unit-sum split-routing transfer, so $\mathbf{1}^\top S_{\mathcal{T}} = 0$ column by column — Theorem 8's conservation, at sight — and the natural-block rows $(N, U, A^{\mathrm{act}}, A^{\mathrm{geo}})$ reproduce the four-row display of Section 2.2, with the harvest column now carrying its full routing ($\alpha$ to $U$, $1-\alpha$ to $P$) instead of the block-export convention of the $\alpha = 0$ corner. The retirement split $(\rho_P, 1-\rho_P)$ and the inert-bound source (the absorbing stock $W$) are declared routing choices of this displayed instance; the incidence pattern — every column a zero-sum transfer/routing column — is the theorem's content, and no classification depends on the declared choices.

### 4.3 Conservation of the six-compartment ledger

**Theorem 9 (Six-compartment conservation).** *For the system of Section 2.3, $\frac{d}{dt}\mathbf{1}^\top z = 0$; the total mass $M_6 = X + U + A + G + P + W$ is constant along every trajectory on which the classical solution is defined.*

*Proof.* With $M_6 = \mathbf{1}^\top z$, $\dot M_6 = \mathbf{1}^\top S(\alpha,\rho) v = 0$ because each column of $S$ sums to zero; term by term: assimilation gives $g - g = 0$; mortality gives $-m + m = 0$; decomposition gives $-d_U + d_U = 0$; geological exchange gives $e_{GA} - e_{GA} = 0$ and $-e_{AG} + e_{AG} = 0$; mining gives $-c_G + c_G = 0$; and the remaining harvest and retirement terms satisfy $-h + \alpha h + (1-\alpha)h = 0$ and $\rho_P r_P - r_P + (1-\rho_P)r_P = 0$. □

Two scope notes are part of the theorem. The conservation argument applies to the *expanded typed incidence system* when quality grades are split — not automatically to an undifferentiated quality-neutral loop. And open systems are explicit: imports, exports, atmospheric losses and cross-boundary transport enter as typed boundary fluxes, giving $\dot M_6=I_\partial-O_\partial$. Theorems 7–9 are three instances of the conservation projection of Proposition 1 applied to trajectories already known to satisfy their balance laws: each is the identity $\frac{d}{dt}(\ell^\top x) = \ell^\top b$ for a declared ledger and boundary with $\ell = \mathbf{1}$ on the included compartments, differentiated only by which compartments and boundary fluxes the declaration includes.

### 4.4 Orthant invariance

**Theorem 10 (Orthant invariance of the closed ledger).** *The nonnegative orthant in $(N, A^{\mathrm{act}}, A^{\mathrm{geo}}, U)$ is forward invariant for the closed natural block (2).*

*Proof.* The right-hand side is locally Lipschitz on a neighbourhood of the closed orthant: each Michaelis–Menten factor $s$, $\sigma$ is $C^\infty$ on the nonnegative half-line because the registered regime keeps $A_0 > 0$ and $A_{g0} > 0$. Face by face. On $A^{\mathrm{geo}} = 0$ one has $\sigma = 0$, hence $e_{GA} = 0$ and $\dot A^{\mathrm{geo}} = e_{AG} = \omega_A A^{\mathrm{act}} \ge 0$. On $A^{\mathrm{act}} = 0$ one has $s = 0$, so $R = B = T = e_{AG} = 0$ and $\dot A^{\mathrm{act}} = e_{GA} + \gamma_U U \ge 0$. On $N = 0$, extraction and uptake vanish and $\dot N = 0$. On $U = 0$, $\dot U = T \ge 0$. Nagumo's inward-pointing criterion (Aubin, 1991) yields forward invariance of the orthant. □

**Theorem 11 (Forward invariance of the six-compartment cone).** *Under the donor boundary assumptions of Section 2.3 (each primitive flux vanishes when its donor is empty, fluxes continuous in effort and locally Lipschitz in the state), $\mathbb{R}^6_+$ is forward invariant for the six-compartment system.*

*Proof.* Face by face: at $X = 0$, $g = m = h = 0$ so $\dot X = 0$; at $U = 0$, $\dot U = m + \alpha h + \rho_P r_P \ge 0$; at $A = 0$, $\dot A = -g + d_U + e_{GA} - e_{AG} = d_U + e_{GA} \ge 0$, the two negative terms vanishing by donor limitation ($A$ is the donor of both $g$ and $e_{AG}$); at $G = 0$, $\dot G = e_{AG} \ge 0$; at $P = 0$, $\dot P = (1-\alpha)h + c_G \ge 0$; at $W = 0$, $\dot W = (1-\rho_P)r_P \ge 0$. The vector field belongs to the tangent cone at every boundary point, and the tangent-cone invariance theorem applies. Conservation and boundary admissibility are separate obligations, and the finite-donor condition carries a discipline: a target-relaxation law $e_{GA} = \omega(A^{\mathrm{eq}} - A)$ does not satisfy it unless also limited by $G$; it may be used only with the source declared an effectively infinite external reservoir, in which case the system is open rather than closed. □

The classical lineage of these statements is the compartmental-systems non-negativity theory (Jacquez and Simon, 1993).

### 4.5 No interior rest at positive effort

**Theorem 12 (No interior rest at positive effort).** *Assume:*

*(H1) $E \equiv E_* > 0$ is constant.*

*Then a rest point of the closed natural block satisfies $R + C^{A,\mathrm{lim}} = 0$ after restoring optional mining; with $C^A = 0$ this is $R = 0$, hence $N = 0$ or $N = K$ or $A^{\mathrm{act}} = 0$. None of these is compatible with $E_* > 0$ and $N_* > 0$: (i) $N = K$ and $E_* > 0$ give $\dot N = -qE_* K < 0$; (ii) $A^{\mathrm{act}} = 0$ and $A^{\mathrm{geo}} > 0$ give $\dot A^{\mathrm{act}} = \omega_A A^{\mathrm{eq,intrinsic}} \sigma > 0$; (iii) $N = 0$ forces $R = T = 0$ and reduces to the extinction family $\mathcal{R}_{\mathrm{ext}}$ of Theorem 13. In particular the working point $(N^*, A^{\mathrm{act}*}) = (89.526, 397.87)$ is not a rest point at $E = E^* \approx 2.090$: $\dot N = 0$ holds there by construction ($R^* = qE^*N^* \approx 0.187 > 0$), and the rest condition of the proof below fails on the abiotic pair.*

*Proof.* At a rest point, $\dot U = 0$ forces $\gamma_U U = T$. Adding $\dot A^{\mathrm{act}} + \dot A^{\mathrm{geo}}$ gives $-B + \gamma_U U - C^{A,\mathrm{lim}} = 0$; with $\gamma_U U = T$ and $B = R + T$ this is $R + C^{A,\mathrm{lim}} = 0$. With mining declared ($C^A > 0$) this forces $R \le 0$; with $C^A = 0$ it is $R = 0$, and from the constitutive law $R = rN(1 - N/K)s = 0$ implies $N = 0$ or $N = K$ or $s = 0$ (that is, $A^{\mathrm{act}} = 0$). Cases (i)–(iii) exclude each branch at positive effort; in the mining case the contradiction is more direct — $\dot N = 0$ with $E_* > 0$ and $N_* > 0$ gives $R = qE_*N_* > 0$, while the abiotic rest condition gives $R = -C^{A,\mathrm{lim}} \le 0$. At the working point $\dot N = 0$ by construction while rest would require $R = 0$; with $\dot U = 0$ the abiotic pair would satisfy $\dot A^{\mathrm{act}} + \dot A^{\mathrm{geo}} = -R < 0$. □

### 4.6 The extinction–geochemical rest set

**Theorem 13 (Vanishing-extraction rest set).** *With vanishing extraction ($E \equiv 0$), the full rest set of the closed natural block (2) is the three-component union $\mathcal{R}_{E=0}=\mathcal{R}_{\mathrm{ext}}\cup\mathcal{R}_K\cup\mathcal{R}_{\mathrm{frozen}}$: the extinction family, the carrying-capacity family, and the frozen-biomass face. The symbol $\mathcal{R}_0 = \mathcal{R}_{\mathrm{ext}} \cup \mathcal{R}_K$ denotes only the two geochemical components and is not the full rest set:*
$$\mathcal{R}_{\mathrm{ext}} = \bigl\{ N = 0,\ U = 0,\ A^{\mathrm{act}} = A^{\mathrm{eq,intrinsic}}\,\sigma(A^{\mathrm{geo}}),\ A^{\mathrm{geo}} \ge 0 \bigr\}, \qquad \mathcal{R}_K = \bigl\{ N = K,\ U = \kappa_A K s/\gamma_U,\ A^{\mathrm{act}} = A^{\mathrm{eq,intrinsic}}\,\sigma,\ A^{\mathrm{geo}} \ge 0 \bigr\},$$
*where in the second family $s = A^{\mathrm{act}}/(A^{\mathrm{act}} + A_0)$ is evaluated at the solution — together with the frozen-biomass face $\mathcal{R}_{\mathrm{frozen}} = \{(N, 0, 0, 0) : N \ge 0\}$, on which $s = 0$ identically and the biomass is frozen at its initial value. With $E>0$ constant, no interior rest point (with $N^*>0$) exists (Theorem 12); the extinction face $\mathsf R_{\mathrm{ext}}$ of this set persists at positive effort, because extraction $qEN$ vanishes identically at $N=0$, and it is a boundary rest rather than an interior one. If $A_{g0} = 0$ and $\sigma \equiv 1$ is imposed for $A^{\mathrm{geo}} > 0$, the shared active-pool ray of $\mathcal{R}_{\mathrm{ext}}$ and $\mathcal{R}_K$ is $A^{\mathrm{act}} = A^{\mathrm{eq,intrinsic}}$, $A^{\mathrm{geo}} > 0$ — the endpoint $A^{\mathrm{geo}} = 0$ is excluded, because there the donor-limited recharge vanishes and $\dot A^{\mathrm{act}} = -\omega_A A^{\mathrm{eq,intrinsic}} < 0$. The constitutive laws carry no basal mortality independent of the support factor; adding one ($\mu_{\mathrm{basal}} N$, stock $\to$ detritus) collapses the frozen-biomass face and does not touch Theorems 7–12 or 14.*

*Proof.* With $E \equiv 0$, set the four derivatives to zero. From $\dot A^{\mathrm{geo}} = -e_{GA} + e_{AG} = 0$: $e_{GA} = e_{AG}$, i.e. $\omega_A A^{\mathrm{eq,intrinsic}} \sigma = \omega_A A^{\mathrm{act}}$, so $A^{\mathrm{act}} = A^{\mathrm{eq,intrinsic}} \sigma$ — the geological-exchange balance, in which the active pool is pinned to the donor-scaled intrinsic target. From $\dot N = R = 0$: $rN(1 - N/K)s = 0$. If $A^{\mathrm{geo}} > 0$ the geo-balance pins $A^{\mathrm{act}} > 0$, so $s > 0$ and $N = 0$ or $N = K$. At the boundary $A^{\mathrm{geo}} = 0$ the geo-balance forces $A^{\mathrm{act}} = 0$ (since $\sigma(0) = 0$), hence $s = 0$ and $\dot N = 0$ for every $N \ge 0$; with $U = 0$ the remaining equations vanish identically, so the frozen-biomass face $\{(N, 0, 0, 0) : N \ge 0\}$ is a rest set. From $\dot U = T - \gamma_U U = 0$: $U = T/\gamma_U = \kappa_A N s/\gamma_U$, which vanishes in the $N = 0$ branch and is positive in the $N = K$ branch. From $\dot A^{\mathrm{act}} = -B + e_{GA} - e_{AG} + \gamma_U U = -(R + T) + 0 + \gamma_U U$: this vanishes in both branches, since $\gamma_U U = T$ and $R = 0$ hold there. The two families together with the frozen-biomass face are exactly the stated rest set. "Geochemical" names the mechanism of both families' active-pool rest: the pool rests at the donor-scaled intrinsic target; apart from the frozen-biomass face, no rest point exists away from extinction or carrying capacity. The institutional memory yields $E \to E^*$ at $N = 0$ with extraction vanishing identically — consistent with the rest set and not an interior rest. □

### 4.7 Extraction integrability

**Theorem 14 (Integrable extraction).** *Assume $E(s) \ge 0$ along the trajectory (effort is nonnegative; $N \ge 0$ along classical solutions is Theorem 10's). Let $M = N + A^{\mathrm{act}} + A^{\mathrm{geo}} + U$. Then $M(t) = M(0) - \int_0^t qE(s)N(s)\, ds \ge 0$, so*
$$\int_0^\infty qE(s)N(s)\, ds \le M(0) < \infty;$$
*in particular $qEN \in L^1(0,\infty)$, and no trajectory maintains extraction at the working value $qE^*N^* \approx 0.187$ for all time; with mining restored, $\int_0^\infty \bigl( qE(s)N(s) + C^{A,\mathrm{lim}}(s) \bigr) ds \le M(0)$.*

*Proof.* By Theorem 7, $M(t) = M(0) - \int_0^t qE(s)N(s)\, ds$; forward invariance (Theorem 10) gives $M(t) \ge 0$, so the improper integral is at most $M(0)$. If $qEN \equiv qE^*N^*$ for all $t \ge 0$, the integral would diverge. □

This is the depletion-horizon semantics of the closed ledger in its strongest form: the donor budget is finite and extraction is integrable against it. A constant extraction flux $c>0$ — a comparison flux only, not a donor-limited primitive the ledger's own discipline admits as a sustained law — exhausts the budget in finite time ($M$ reaches its lower bound no later than $M(0)/c$), while proportional extraction $qEN$ need not drive $M$ to zero in finite time. This is the finite-budget fact that §9 turns into the non-reduction boundary with the open working system. The theorem does not select among the vanishing-extraction rests of Theorem 13: integrable extraction is compatible with approach to either the extinction family or the carrying-capacity–geochemical family, and the $L^1$ bound alone decides nothing between them.

### 4.8 The conditional hybrid moiety balance

**Conditional Theorem 15 (Hybrid moiety balance).** *Let $\chi$ denote the hybrid state and $\eta\ge0$ its primitive-flux vector — letters local to this statement, chosen so that $r$ stays the growth rate of §2.2 and $\nu$ a macro parameter of §5.4. Assume:*

*(H1) $\chi$ is absolutely continuous between locally finite event times with left and right limits at events.*

*(H2) $\dot \chi = \mathsf{S}\eta + b$ with $\eta \ge 0$, separate reverse columns, and donor-limited negative boundary flows.*

*(H3) $\mathsf{L}^\top \mathsf{S} = 0$.*

*Then*
$$\mathsf{L}^\top \chi(t) - \mathsf{L}^\top \chi(0) = \int_0^t \mathsf{L}^\top b\, ds + \sum_{t_k \le t} \mathsf{L}^\top \bigl[ \chi(t_k^+) - \chi(t_k^-) \bigr].$$

*Proof.* Integrate the continuous balance between consecutive events and telescope the left/right state differences. □

The theorem is conditional, and its jump interpretation is part of the content: an internal-transformation jump requires $\mathsf{L}^\top(\chi^+ - \chi^-) = 0$ or a jump incidence factorization with left-kernel conservation; a boundary-crossing jump is a boundary impulse and belongs in the boundary term. Two obligations ride the theorem. The *yield-routing obligation*: if a transformation is represented with a yield below one for a declared moiety, the omitted fraction must be routed to another represented compartment or a declared boundary flow — otherwise the claimed moiety balance holds only after silently dropping that moiety from $\mathsf{L}$. And the *separation obligation*: this is the hybrid variant of Proposition 4, retained at its own conditional status; the two statements are not merged.

### 4.9 Cancellation is cheap

Summing the six material equations of a ten-state admissibility template gives the exact identity
$$\frac{d}{dt}\bigl( \bar X_A + X_J + P + U + A + G \bigr) = 0.$$
This is an algebraic cancellation only: it does not prove forward invariance of the six material states or physical admissibility of every term. The ghost-sink check is part of the discipline: the same birth-transfer rate $g_B$ enters $\dot X_J$ and $\dot A$ with opposite signs, so material not transferred to juveniles remains in $A$ — there is no unmatched sink in the six-state ledger. Formal cancellation coexists with boundary failure elsewhere in the same template (its geological exchange is **not** donor-limited), and the cancellation by itself establishes nothing about admissibility. Conservation (Theorems 7–9) and positivity (Theorems 10–11) are proved separately in every well-posed ledger of this article, exactly because cancellation is cheap and admissibility is not. The template's remaining negative witnesses — a variance closure that is not realizable by a non-negative spatial distribution, and an output functional without a displayed state equation — are recorded in the supplementary material as audited admissibility failures.

**The closed-ledger portrait.** Theorems 7–14 assemble into a complete qualitative portrait of the closed orthant: conservation (Theorems 7–9), positivity (Theorems 10–11), no interior rest at positive effort (Theorem 12), the three-component vanishing-extraction rest set—two geochemical families plus the frozen-biomass face (Theorem 13), and the finite donor budget (Theorem 14). The portrait is the source object handed to the interface of §9: the closed system's candidate long-time set is the rest set of Theorem 13, and the budget of Theorem 14 bounds how long any positive-flux configuration can persist. For industrial-ecology measurement the message is direct: a "balanced" closed ledger is a finite-budget object, and any sustained extraction against it must integrate to a quantity no greater than the initial budget.

---

## 5. Service Readouts and the Componentwise Deficit

Services are observations or feasible outputs of the physical state, not additional conserved mass. Internal physical transfers are not services merely because they appear in a ledger. This distinction is the accounting counterpart of the ecological-economics point that a service flow — Ayres' useful-work reading, Daly's throughput-of-services reading — is not the same object as the mass that delivers it.

### 5.1 The service readout and the contemporaneous balance

For services indexed by $i = 1, \ldots, n$, write $s_i(t) = \mathcal{O}_i(x(t), u(t), \theta)$, where $u$ denotes admissible operating or extraction choices and $s_i$ and the demand $d_i$ share service-specific units. Where delivered services are selected or converted ledger fluxes, the readout is linear in the primitives,
$$s = \mathcal{O}(x, u, \theta) = Q(\theta)\, v(x, u),$$
with every row of $Q$ declaring the delivery boundary and the conversion into one service-specific unit; more general state-dependent readouts are possible. The contemporaneous component balance is
$$b_i(t) = s_i(t) - d_i(t),$$
and $b_i(t) \ge 0$ means measured supply meets measured demand for component $i$ at that instant. A stock can meet current demand while declining toward a threshold, and a stock below a desired level can have a positive current balance while recovering.

**Proposition (Stationary bridge from closure to strong-assessment adequacy).** *Freeze $(x,y,\theta,b_0)$ as in Definition 21 and suppose $v^*\in\mathcal K(x;b_0)$ has service readout $s^*=Pv^*$ satisfying $s^*-d\ge0$ componentwise for a constant demand $d$. Suppose also that $x\in\mathcal K_{\mathrm{safe}}(t)$ for every $t$ in the interval considered (in particular, the barriers may be time-independent with $x$ safe), and that holding the flux pattern $v(t)\equiv v^*$ is admissible under the declared operating law while the boundary schedule remains $b_0$. Then the constant trajectory $x(t)\equiv x$ delivers componentwise-adequate service and remains barrier-safe on that interval.*

*Proof.* Membership in $\mathcal K(x;b_0)$ gives $S_{\mathcal{T}}v^*+b_0=0$, so the constant state is an admissible trajectory under the stated holding hypothesis. Its service balance is constantly $s^*-d\ge0$, and the safety hypothesis is exactly $x\in\mathcal K_{\mathrm{safe}}(t)$ throughout. ∎

The bridge is one-way. If $\Lambda^*(x;d,b_0)<1$, the same initial state can still be safe and can still meet $d$ for a finite interval by drawing a stock or pipeline buffer; if $\Lambda^*\ge1$, the current state can nevertheless already violate a barrier. Stationary closure is therefore a sufficient route to persistent strong-assessment adequacy under a frozen declaration, not a synonym for a componentwise pass at an instant.

### 5.2 The state-dependent feasible balance domain

**Definition 1 (Feasible balance domain).** *For an admissible operating set $\mathcal{U}(x,t)$ and a declared demand set $\mathcal{D}(t)$,*
$$\mathcal{B}(x,t) = \{ \mathcal{O}(x,u,\theta) - d : u \in \mathcal{U}(x,t),\ d \in \mathcal{D}(t) \}.$$

The geometry of the balance domain is state dependent and inherited partly from the stock–flow model. **No unrestricted argument can replace an application-specific analysis of $\mathcal B(x,t)$.** This domain is the object against which any scalar certificate claim must be checked (§10.1): a weighted sum certifies componentwise non-negativity on $\mathcal B(x,t)$ only through an implication proved from the physical restrictions that define the domain.

### 5.3 Support provenance and the directional support gap

Current service adequacy and regenerative feasibility are different claims. Let $\Gamma_{\mathrm{all}}(x,t) \subseteq \mathbb{R}^n_+$ contain the service vectors feasible through all pathways admitted by an application, and $\Gamma_{\mathrm{reg}}(x,t) \subseteq \Gamma_{\mathrm{all}}(x,t)$ the feasible set after imposing the declared regenerative-flow, system-boundary, material-quality, and exergy or capacity restrictions. These correspondences are application inputs obtained from a typed pathway or technology model; the stock ledger alone does not construct them.

**Definition 2 (Directional regenerative-support fraction and gap).** *Assume:*

*(H1) $0 \in \Gamma_{\mathrm{reg}}(x,t)$.*

*(H2) A nonzero service direction $\bar s \ge 0$ is chosen.*

*Define*
$$\alpha_{\mathrm{reg}}(\bar s; x, t) = \sup\{ \alpha \in [0,1] : \alpha \bar s \in \Gamma_{\mathrm{reg}}(x,t) \}.$$
*The vector $(1 - \alpha_{\mathrm{reg}})\bar s$ is the directional support gap, measured in the same service units as $\bar s$. A realized service $s \in \Gamma_{\mathrm{all}} \setminus \Gamma_{\mathrm{reg}}$ is support-dependent under that declaration even when $s \ge d$.*

Attainment requires closedness: if $\Gamma_{\mathrm{reg}}$ is not closed the supremum may not be attained, and the gap is relative to a supremal fraction, not necessarily to an achievable boundary service. The **non-interpretation discipline** is equally part of the definition: the statement neither subtracts raw material from service nor proves that a physical stock is declining. The provenance partition behind $\Gamma_{\mathrm{reg}}$ — renewable flow, recovered or recycled material, imports, non-renewable drawdown — never adds unlike physical units.

### 5.4 The componentwise deficit and the specialization identity

On the unreduced ledger the physical deficit is the diagnostic
$$\Delta^{\mathrm{phys}}(t) = C(t) - \widehat{M}^\top S(t),$$
with $C$ the operative extraction-law readout and $\widehat{M}$ the declared demand-coverage matrix mapping the moiety readout $S = Cx$ — the composition matrix $C$ of Lemma 3, a different object from the coverage vector $C(t)$ despite the shared letter — into the units of that coverage vector — rows indexed by covered services, columns by moieties, entries the declared stoichiometric coefficients of the coverage convention (the hat distinguishes the matrix from the scalar natural-block mass $M$ of Section 4.1). It does not drive the physical equations, and it is not equal to $-\dot N$ unless waste–product feedback vanishes and the service is identified with regeneration. The single-resource specialization (the omitted product, waste, and price parameters $\mu, \nu, \rho$ of the unreduced ledger set to zero, together with $C^A = 0$) makes that identification, and on that class — and only on that class — the deficit collapses to the stock-decline rate.

**Remark 16 (Exact specialization deficit identity).** *On every trajectory of the specialized system, and of every reduced system whose stock equation is $\dot N = R(N,A) - qEN$,*
$$qEN - R(N,A) = -\dot N, \qquad \Lambda(t) := \bigl[ qEN - R \bigr]_+ = \bigl[ -\dot N \bigr]_+.$$

*Proof.* Substitute the stock equation: $qEN - R = -(R - qEN) = -\dot N$. □

The collapse is a **property of the specialization**, not a definition of liquidation on the unreduced ledger.

On this specialization, the memory input used by the institutional interface of Section 9 is a smoothed stock-decline rate: before smoothing it is exactly $\Lambda(t)=[-\dot N(t)]_+$, the positive part of the decline. (This time-dependent $\Lambda(t)$ is local to the specialization/interface and is distinct from the closure capacity $\Lambda^*(x;D,b_0)$.) It is not a stock-level scarcity measure, not an unmet-consumption measure, and not an independently observed service deficit. Since $qEN-R(N,A_{\mathrm{act}})=O(N)$ as $N\to0$, the raw decline input vanishes near extinction while the positive baseline source of the effort law can still sustain commanded effort.

**Proposition 25 (Accumulated support drawdown certified by delivered service).** Let the declared support pool
obey $\dot A=r-c$, where $r$ is its total replenishment/return inflow and $c$ its support-use outflow, and let the declared production relation require at least $\alpha\ge0$ units
of support use per unit of delivered service, $c(t)\ge\alpha Y(t)$. Then
$$A(0)-A(T)\ \ge\ \alpha\int_0^TY(t)\,dt-\int_0^Tr(t)\,dt .$$
Where the right-hand side is positive, delivered service certifies at least that much net drawdown of the declared pool over $[0,T]$, whatever the interior allocation of fluxes. Whether that finite-interval drawdown is permanent liquidation depends on what $A$ and $r$ represent: if $A$ is only available stock and some of $c$ is still in a return pipeline, part of the decline can reverse; if $A=A_m+W_m$ is the combined circulation stock of Definition 22 and $r$ includes all replenishment, the certified decline is liquidation of that combined stock.

*Proof.* $A(0)-A(T)=\int_0^T(c-r)\,dt\ge\alpha\int_0^TY\,dt-\int_0^Tr\,dt$. □

The statement is falsifiable against the record, not self-sealing: a stock change smaller than
the certified lower bound exposes a wrong coefficient, a missing flux, or a measurement inconsistency,
and each of the three is a registered obligation, not a licence to reconcile. The coefficient
$\alpha$ is a declared relation, not an estimate; the proposition is conditional on it and is not
computed anywhere here.

---

## 6. Depletion Arithmetic

The ledger supplies the net active-pool derivative needed to tell gross throughput apart from net decline and from a model-conditioned threshold time. The distinction matters because "time to depletion" is publicly used as if all three were one quantity. They are not, and the worked instances below make the differences explicit. Let $A_{\min}$ be a declared threshold for the active abiotic pool with $A > A_{\min}$.

### 6.1 The three quantities

**Definition 3 (Gross turnover intensity and support coverage).** *With assimilation $g(X,A) > 0$, the gross turnover intensity is $J_A^{\mathrm{gross}} = g(X,A)/A$ and the gross support-coverage ratio is $H_A^{\mathrm{gross}} = (A - A_{\min})/g(X,A)$.*

Neither is a time to depletion. At an interior steady state, $g$ can be positive while decomposition and geological transfer balance it exactly, so that $\dot A=0$. Gross uptake measures throughput or dependency. This false-implication record is the first rung of the taxonomy, and it governs every application below.

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

**Proposition 17 (Local threshold-horizon bracket).**
*Assume:*

*(H1) $A : [0,T] \to \mathbb{R}$ is absolutely continuous with $A(0) > A_{\min}$.*

*(H2) Constants $v_0 > 0$ and $0 < \varepsilon < 1$ are given; set $H_0 = (A(0) - A_{\min})/v_0$.*

*(H3) $T \ge H_0/(1-\varepsilon)$.*

*(H4) $(1-\varepsilon)v_0 \le -\dot A(t) \le (1+\varepsilon)v_0$ for almost every $t$ while $A$ stays above $A_{\min}$.*

*Then a first crossing time $H$ exists no later than $H_0/(1-\varepsilon)$, and*
$$\frac{H_0}{1+\varepsilon} \le H \le \frac{H_0}{1-\varepsilon}, \qquad |H - H_0| \le \frac{\varepsilon}{1-\varepsilon}H_0.$$

*Proof.* If no crossing occurs before $t_* = H_0/(1-\varepsilon)$, absolute continuity gives $A(t_*) \le A(0) - (1-\varepsilon)v_0 t_* = A_{\min}$, a contradiction; hence $H \le t_*$. Integrating both rate bounds over $[0,H]$ and using $A(0) - A(H) = v_0 H_0$ gives the two-sided bracket: from the upper rate bound, $v_0 H_0 \le (1+\varepsilon) v_0 H$, and from the lower rate bound, $v_0 H_0 \ge (1-\varepsilon) v_0 H$. □

It fails when depletion reverses, when the rate approaches zero, or when feedback moves the trajectory outside the declared rate bounds. Its companion is the one-sided exhaustion proposition of §3.6, whose counterexample — proportional extraction never exhausts in finite time — shows that the uniform margin $\varepsilon>0$ is load-bearing in both directions. The bracket bounds the frozen-rate ratio's error under declared rate bounds, and nothing more.

**When the clocks coincide.** Under the rate bracket the frozen-rate ratio and the true hitting time agree within the bracket: $-\dot A \in [(1-\varepsilon)v_0, (1+\varepsilon)v_0]$ gives $H_A^{\mathrm{loc}} = (A(0) - A_{\min})/[-\dot A]_+ \in [H_0/(1+\varepsilon), H_0/(1-\varepsilon)]$, hence $|H - H_A^{\mathrm{loc}}| \le 2\varepsilon H_0/(1-\varepsilon)$ — the only regime in which the frozen-rate ratio is a horizon. The three quantities of §6.1 coincide only under a declared rate bracket, and the false implication $g>0\Rightarrow\dot A<0$ is the reason.

**Proposition 26 (Sign of the frozen-rate error).** Let $\dot A=-\varphi(A)$ with $\varphi>0$ on
$(A_{\min},A_0]$, and write the true horizon and the frozen-rate ratio as
$$T=\int_{A_{\min}}^{A_0}\frac{dA}{\varphi(A)}, \qquad H^{\mathrm{loc}}=\frac{A_0-A_{\min}}{\varphi(A_0)} .$$
If $\varphi$ is nondecreasing in $A$ then $T\ge H^{\mathrm{loc}}$, and the frozen-rate number
is conservative. If $\varphi$ is nonincreasing in $A$ then $T\le H^{\mathrm{loc}}$, and it is
optimistic.

*Proof.* If $\varphi$ is nondecreasing, then for $A\le A_0$ one has $\varphi(A)\le\varphi(A_0)$, hence $1/\varphi(A)\ge1/\varphi(A_0)$ and $T\ge(A_0-A_{\min})/\varphi(A_0)$. If $\varphi$ is nonincreasing, both inequalities reverse. The comparison is the standard one for one-dimensional monotone dynamics (Smith, 1995). □

Proportional extraction is the first case, with $T=q^{-1}\ln(A_0/A_{\min})$ against
$H^{\mathrm{loc}}=(A_0-A_{\min})/(qA_0)$; at $A_{\min}=0$ the two disagree by being infinite
against finite. The sign is estimable from the data the classification already requires, by
regressing the decline rate on the stock; it is declared, not computed, in Section 6.5.

**Proposition 27 (Curvature correction).** On the barrier distance $u=A-A_{\min}$, let
$\dot u=-\varphi(u)$ with $u(0)=u_0>0$, and define the dimensionless curvature number
$$\kappa=\frac{u\,\ddot u}{\dot u^{2}}=\frac{u\,\varphi'(u)}{\varphi(u)} .$$
For the power-law family $\varphi(u)=cu^{p}$ with $c>0$ one has $\kappa=p$ identically, and for $\kappa<1$
$$T=\frac{H^{\mathrm{loc}}}{1-\kappa}, \qquad T<\infty\iff\kappa<1,$$
while for $\kappa\ge1$ the integral diverges at the barrier and the family reaches it only
asymptotically, so the frozen-rate ratio understates by an unbounded factor. Constant extraction is
$\kappa=0$, where the frozen-rate ratio is exact; stock-proportional decline is $\kappa=1$,
where the true horizon is infinite against a finite ratio; and $\kappa=\tfrac12$ doubles the
horizon exactly, which is the smallest correction with a real effect. The correction is a one-number
statement about the bias, and it inherits its input requirement: $\kappa$ needs $\ddot u$, which
is a second difference of the same noisy series whose first difference the classification already
distrusts, so it is reported as declared or not at all. Where $\varphi$ is not of the family, only
the sign statement of Proposition 26 is available.

*Proof.* For $\varphi(u)=cu^p$ with $c>0$, $\kappa=u\varphi'(u)/\varphi(u)=p$ for $u>0$, and separation of variables gives the barrier hitting time $T=\int_0^{u_0}du/(cu^p)$. This integral is finite exactly when $p<1$, in which case $T=u_0^{1-p}/[c(1-p)]$; since $H^{\mathrm{loc}}=u_0/(cu_0^p)=u_0^{1-p}/c$, this is $H^{\mathrm{loc}}/(1-\kappa)$. For $p\ge1$ the integral diverges at $0$. □

**Proposition 28 (Exact reserve-life crossover).** In the stipulated reserve-class scenario, let reserves obey $\dot R=-(1-\eta)P$ with constant reclassification elasticity $\eta\in[0,1]$, production $P=P_0e^{gt}$, $R_0,P_0,g>0$, and reserve-life ratio $\tau=R_0/P_0$. Put $x=g\tau$. If $\eta<1$, exhaustion of the modelled reserve class occurs at
$$T(\eta)=\frac1g\ln\Bigl(1+\frac{x}{1-\eta}\Bigr);$$
if $\eta=1$, $\dot R=0$ and this scenario has no finite exhaustion time. The exact crossover is
$$T(\eta)\ge\tau\quad\Longleftrightarrow\quad \eta\ge\eta_*(x):=1-\frac{x}{e^x-1},$$
with the endpoint $\eta=1$ included by the no-finite-exhaustion reading. Since
$$\eta_*(x)=\frac{x}{2}-\frac{x^2}{12}+O(x^4)\qquad(x\to0),$$
the familiar first-order condition $\eta\gtrsim x/2$ is only a small-$x$ approximation. It is already quantitatively misleading for moderate $x$, and for large $x$ it can demand an impossible $\eta>1$ even though the exact threshold remains below $1$ and tends to $1$ as $x\to\infty$.

On the consistently pinned USGS MCS 2026 world record used in Section 6.5.3—$73{,}000{,}000$ kt reserves and $250{,}000$ kt/yr 2025 production—$\tau=292$ yr. For the illustrative growth scenario $g=0.03\,\mathrm{yr}^{-1}$, $x=8.76$ and $\eta_*=0.998625\ldots$. The same scenario gives $T(0)=75.94$ yr, $T(0.99)=225.88$ yr, $T(0.995)=248.97$ yr, and $T(0.999)=302.60$ yr. Thus the static ratio overstates this growing-production scenario's exhaustion time for almost the entire elasticity range, but the direction reverses in the narrow interval $\eta\in[\eta_*,1]$ where reclassification offsets at least $99.8625\%$ of production. The corrected conclusion is sharper than a fixed-sign slogan: the reserve-life ratio has no model-free error direction once growth and reclassification are both allowed; its relation to a scenario hitting time is exactly the crossover above. That is another reason the ratio itself remains an arithmetic classification quantity, not a forecast.

*Proof.* For $\eta<1$, integration gives
$$R(t)=R_0-(1-\eta)P_0\frac{e^{gt}-1}{g}.$$
Setting $R(T)=0$ and using $R_0/P_0=\tau$ gives $e^{gT}=1+g\tau/(1-\eta)$, hence the displayed $T(\eta)$. Moreover $T(\eta)\ge\tau$ if and only if $\ln(1+x/(1-\eta))\ge x$, equivalently $x/(1-\eta)\ge e^x-1$, equivalently $1-\eta\le x/(e^x-1)$. The expansion is the Bernoulli expansion of $x/(e^x-1)$. The $\eta=1$ case is immediate from $\dot R=0$. □

### 6.3 Upper barriers, exit times, and maintainability

The lower-barrier setting of §6.1 is one half of the story. For each moiety $m$, define the lower and upper exit times
$$\tau_m^- = \inf\{ t \ge 0 : S_m(t) \le \underline{B}_m(t) \}, \qquad \tau_m^+ = \inf\{ t \ge 0 : S_m(t) \ge \overline{B}_m(t) \}, \qquad \inf\varnothing = \infty,$$
and the overall admissibility exit time
$$\tau_{\mathrm{exit}} = \min_m \{ \tau_m^-, \tau_m^+ \};$$
horizon safety on $[0,T]$ is $\tau_{\mathrm{exit}} > T$. Two disciplines attach. 1. **Equality at the hitting time** — $S_m(\tau_m^-)=\underline B_m(\tau_m^-)$ — requires continuity of both $S_m$ and $\underline B_m$ and appropriate initial separation. If fluxes or barriers can jump, the stock can cross the barrier *without* satisfying equality. 2. **Lower barriers need not be exhaustion thresholds.** The diagnostic distinguishes physical exhaustion ($S_m=0$), functional failure ($S_m=\underline B_m^{\mathrm{func}}$), a resilience or regime-shift threshold, an economically recoverable reserve, and a minimum service-supporting stock.

Upper-barrier violations matter symmetrically: a system may satisfy every lower-barrier condition while violating an upper barrier, $S_m(t) > \overline{B}_m(t)$. Atmospheric CO₂ accumulation violates an upper concentration barrier while fossil carbon stocks decline; the depletion diagnostic must check both barriers. And a stock can remain above a barrier until an assessment horizon $T$ and still be unsustainable thereafter: if the assessment claims sustainability rather than finite-horizon admissibility, it requires a terminal condition
$$x(T) \in K_{\mathrm{maint}},$$
where $K_{\mathrm{maint}} = \{ x : \exists \text{ an admissible continuation satisfying all barriers for } t \ge T \}$ — the set from which barrier safety is indefinitely maintainable, the viability kernel of the barrier set under the admissible controls (Aubin, 1991). The finite-horizon diagnostic is a necessary but not sufficient condition for sustainability; the full certificate requires the terminal state to lie in the maintainability set.

One consequence for reporting. The exit time is itself a minimum, over moieties and over both barrier
signs, so a statement about its joint distribution is already a componentwise statement: no product
of marginal probabilities is required, and none is admissible in its place.

### 6.4 Robust semantics

For uncertain parameters $\theta \in \Theta$ and admissible disturbances $d \in \mathcal{D}$, robust barrier safety is
$$\mathrm{RobustBarrierSafe}(x(\cdot)) \iff \underline{B}_m(t) \le S_m(t; \theta, d) \le \overline{B}_m(t) \quad \forall m, \forall t, \forall \theta \in \Theta, \forall d \in \mathcal{D},$$
and the depletion-horizon classification is fourfold: nominal ($\theta = \theta_0$, $d = 0$); worst-case ($\inf_{\theta,d} \tau_{\mathrm{exit}}(\theta,d)$); probabilistic ($\Pr[\tau_{\mathrm{exit}} > T] \ge 1 - \varepsilon$); and scenario-conditioned ($\tau_{\mathrm{exit}} \mid \theta = \theta_s$). The componentwise diagnostic applies to each scenario, and the conjunctive criterion applies within each scenario and across scenarios. No single number is promoted across the four classes without a declared map.

### 6.5 Application classifications at their exact status

The classification matrix records, quantity by quantity, what each application computes and what each object is.

| Time-like quantity | Question answered | G3P $L_{\mathrm{hist}}^{\mathrm{anom}}$ | Phosphate $T_{\mathrm{reserve}}$ | Fisheries $\Theta_F$ |
|---|---|---|---|---|
| $J_A^{\mathrm{gross}}$, $H_A^{\mathrm{gross}}$ | turnover / dependency | no | no | gross-loss analogue only — not a member (§6.5.4) |
| $H_A^{\mathrm{loc}}$ | frozen net-rate ratio | no (anomaly, not stock) | no (classification, not stock) | no (no net $\dot B$) |
| $T_A$ | scenario hitting time | no | no | no |
| What it is | — | record-relative statistical index | arithmetic ratio of an economic class | removals-only pressure scale |

#### 6.5.1 Groundwater anomaly-persistence indices

The G3P column of the matrix is the groundwater case. The Global Gravity-based Groundwater Product (G3P v1.12; Güntner et al., 2024; the GRACE line it descends from is Tapley et al., 2004) provides monthly **groundwater-storage anomalies relative to a reference period**, not absolute aquifer volumes. For a basin-mean anomaly series over the reported April 2002–September 2023 window, the linear-trend anomaly persistence index is
$$L_{\mathrm{hist}}^{\mathrm{anom}} = \frac{a_{\mathrm{latest}} - a_{\mathrm{hist,min}}}{\bigl[ -\widehat{\dot a} \bigr]_+},$$
the fitted distance to the series' own historical minimum divided by the fitted decline rate. The four-basin record: Indo-Gangetic $-49.7$ cm/yr with index $\approx 2.7$ yr; North China Plain $-18.6$ with $\approx 7.9$; Central Valley $-16.1$ with $\approx 9.5$; La Mancha $-3.2$ with $\approx 21.4$.

Classification, stated at the product's own status: a statistical anomaly index with units of time — not the physical stock ratio $H_A^{\mathrm{loc}}$ and not a forecast of aquifer exhaustion. Its value depends on the product window, basin mask, anomaly reference, and linear-trend convention
--- the reference period is the product's declared long-term mean over April 2002 to December 2020,
the coverage ends September 2023, and the producer documents a faulty snow-water-equivalent entry for
June 2005 that propagates into groundwater storage, recommending that the month be excluded; the
window above spans it, so a re-derivation must declare whether June 2005 is retained, because it can
move both the fitted trend and the series' own historical minimum; a physical $H_A^{\mathrm{loc}}$ requires an absolute stock estimate and a net stock derivative (aquifer geometry or saturated thickness together with storage parameters), not an anomaly series alone.

A structural point sharpens the boundary. The **access structure** — a well, or an index well — is infrastructure rather than the resource: it draws on stored water, the stock, which is replenished by recharge, the flow. The anomaly series measures the stored stock as observed at the access point; it measures neither the access infrastructure nor the recharge. An index built on it therefore cannot distinguish a drawdown of stored water that is recoverable on the recharge timescale from one that is not — although heavy over-extraction can make the loss permanent through compaction, subsidence or saline intrusion, in which case it is not recoverable at all. The index is exactly the record-relative object analysed in §7.3, and its interpretive boundary is that record-relativity (§7.7).

#### 6.5.2 The applied depletion-horizon tables

Component-resolved depletion horizons on public data products are tabulated below, computed without fitting any dynamical parameter of the reduced systems. The dagger (†) quarantines the Indo-Gangetic groundwater magnitude, which sits an order of magnitude beyond published basin-mean trends (the quarantine note below). The phosphate rows are now a single consistent USGS MCS 2026 vintage; Australia appears twice because the source itself carries two differently typed reserve figures, and the table keeps those declarations separate rather than averaging them.

| Basin | Trend (cm/yr) | 2023 anomaly (cm) | Window minimum (cm, implied) | Horizon to window minimum (yr) |
|---|---|---|---|---|
| Indo-Gangetic (N. India)† | $-49.7$ | $-414$ | $-548$ | $\approx 2.7$ |
| North China Plain | $-18.6$ | $-145$ | $-292$ | $\approx 7.9$ |
| Central Valley (US) | $-16.1$ | $-84$ | $-237$ | $\approx 9.5$ |
| La Mancha (Spain) | $-3.2$ | $-20$ | $-88.5$ | $\approx 21.4$ |
| High Plains (US) | $-7.9$ | $-160$ | $-160$ | already at minimum |
| global mean | $-0.4$ | $-14$ | $-33.0$ | $\approx 47.5$ |

† *Quarantine note, adjacent to the row it marks (recorded data-vintage decision: the row stays first, daggered).* The Indo-Gangetic magnitude must not be reused numerically: it sits an order of magnitude beyond published basin-mean trends and awaits re-derivation from the product's basin masks — its full provenance is the supplementary's S5.4.

The basin rows are reported extractions from the G3P v1.12 basin series, used here only to exhibit the
index construction of Section 6.5.1 and never as product-endorsed values: the window-minimum column is implied
arithmetically through the index formula, every row must be re-derived from the product's basin masks before any
numerical reuse, and the extraction provenance --- including why the Indo-Gangetic row is the extreme case and
how its fitted segment convention enters --- is recorded in the supplementary's S5.4 with the vintage record it
belongs to. The classification status assigned below does not depend on the magnitudes.

Phosphate-rock rows below are USGS *Mineral Commodity Summaries* 2026, using estimated 2025 production and the reserves printed in that same table unless the convention column says otherwise. The ratio is reserves divided by that production; it is not an implied-production inversion from a rounded horizon.

| Row | Reserve convention | Reserves (kt) | 2025 production (kt/yr) | Reserve-life ratio (yr) |
|---|---|---:|---:|---:|
| China | MCS 2026 tabulated reserves | $3{,}400{,}000$ | $110{,}000$ | $30.9$ |
| United States | MCS 2026 tabulated reserves | $1{,}000{,}000$ | $20{,}000$ | $50.0$ |
| Jordan | MCS 2026 tabulated reserves | $820{,}000$ | $12{,}000$ | $68.3$ |
| Morocco | MCS 2026 tabulated reserves | $50{,}000{,}000$ | $36{,}000$ | $1{,}388.9$ |
| Australia | MCS 2026 tabulated reserves | $5{,}800{,}000$ | $2{,}500$ | $2{,}320.0$ |
| Australia | JORC-compliant or equivalent reserves (MCS 2026 footnote) | $120{,}000$ | $2{,}500$ | $48.0$ |
| World total (rounded) | MCS 2026 tabulated reserves | $73{,}000{,}000$ | $250{,}000$ | $292.0$ |

The world-resources quantity is deliberately not another row of that reserve table: MCS 2026 states world phosphate-rock resources of more than $300$ billion tons ($300{,}000{,}000$ kt), so at the same production the separate $10\%$-threshold resource arithmetic $0.9G_{\mathrm{resource}}/P$ exceeds $1{,}080$ yr. It answers a resource question, not the reserve-life question.

**Fisheries cohort record.** The archived ADH construction asks how long the current SSB margin over $B_{\lim}$ would last under current fishing mortality $F$ alone. It has median **≈ 1.8 yr** across the **43** assessed stocks with finite spawning-stock-biomass (SSB) and $F$ series — the archived pull, kept in place as the headline cohort by the recorded data-vintage decision — computed with $\mathrm{ADH}=0$ entered for the **eight** stocks already at or below the reference: the zero convention of the source table's caption, **which the median includes**. The archived 43-stock cohort is reproduced by **neither** public RAM Legacy release — S5's version-sensitivity record, cross-referenced here, is the retraction and the row-by-row re-verification — and the v4.66 public-release broad-cohort reading (454 stocks, median 3.39 yr) is the primary public-release comparison, executed in S5 and detailed below. The qualifying positive sub-cohort ($F > 0$ and $\mathrm{SSB}_{\mathrm{now}} > B_{\lim}$; 35 stocks) has median $2.9$ yr; both medians come from the archived pull alone. The cohort is a selected class, not a random sample of assessed stocks: all 43 stocks are small pelagics (18 anchovy, 20 herring, 4 sprat, 1 sardine), the fast-maturing class the companion review screen (Abaee, 2026b, doi:10.5281/zenodo.22554297) selects by its annual-review eligibility criterion (42 of the 43 are that screen's annual-managed spectral-null stocks, per the source caption). The $\approx 1.8$ yr median is therefore a class-specific diagnostic for fast-maturing, annually managed pelagics, not a statistic of assessed fisheries in general; the executed broad-cohort comparison (S5) runs the same protocol on the full public release — 454 stocks, median $3.39$ yr, the upper end carried by the long-lived groups (elasmobranchs $11.5$, sebastids $9.0$, pleuronectids $6.0$ yr) — and a uniformly random 43-stock draw without replacement from that broad cohort has exact probability $2.47\%$ of a median at or below the class cohort's exact $1.790211$ yr.

The extract is the RAM Legacy cohort of Ricard et al. (2012) at release v4.66 (Zenodo 14043031,
6 November 2024), recorded as the cohort file of the supplementary's S5 record; its vintage is verified from
the extract's own contents, four of six published $F$ values reproducing that release exactly, and the pull
has been re-verified row by row against the formula — all 43 rows reproduce $\mathrm{ADH} = \max(0,\, F^{-1}\log(\mathrm{SSB}/B_{\lim}))$ with $B_{\lim} = 0.2 \max \mathrm{SSB}$. The value is reported with its cohort conditions and is not promoted to a forecast. Because cohort composition is database-version-dependent, every cohort statistic is pinned to the archived pull: the quartile summary of $F$ and $\log(\mathrm{SSB}/B_{\lim})$ over the cohort belongs to that pull alone, and no cohort statistic is quoted from a different database version. The cohort protocol is fully specified in the accompanying supplementary material (S5) — including the zero entries for stocks at or below the reference, which enter the median — together with the version-sensitivity record: on the public RAM Legacy releases the same protocol qualifies **415** stocks (v4.44, median **2.57** yr) and **454** (v4.66, median **3.39** yr) — both reproduced to printed precision under the recovered micro-specification (S5) — **neither reproducing the archived 43-stock cohort**: the archived pull's 43-stock list and extract-time series state — supplied and re-verified — differ from both public releases.

**The scope discipline is the tables' load-bearing content.** None of the reported numbers is a computed instance of any model's first-hitting time. They are descriptive, component-resolved diagnostics in the two-pool logic of the taxonomy — not dynamical predictions. The equal-weight inverse-horizon score of the four basins still above their window minimum and world phosphate reserves, displayed as **Non-example 1** — a deliberate boundary of aggregation, not a score of the framework,
$$\Sigma_{\mathrm{reserves}} \approx \frac{1}{5}\left( \frac{1}{2.7} + \frac{1}{7.9} + \frac{1}{9.5} + \frac{1}{21.4} + \frac{1}{292} \right) \approx 0.130\ \mathrm{yr}^{-1},$$
is a ranking device, not a componentwise certificate: it mixes basins and reserves, incommensurable objects under the type structure of Definition 47, and is retained only to mark the boundary of legitimate aggregation. It is exhibited as the worked instance of the non-compensation boundary of §10.1: a positive aggregate coexisting with componentwise deficits by construction — admissible as communication, **inadmissible as certification**.

#### 6.5.3 The phosphate reserve-life ratio

The phosphate column of the classification matrix is the reserve-life ratio. On the single pinned vintage now used consistently—USGS *Mineral Commodity Summaries* 2026—world reserves are $73{,}000{,}000$ kt ($73{,}000$ Mt) and estimated 2025 world production is $250{,}000$ kt/yr, giving **292 years**. It is **not a physical exhaustion forecast**, because reserve classification changes with prices, technology, exploration and regulation—the point made independently, and forcefully, by Illakwahhi, Vegi and Srivastava (2024) for the single-source USGS data behind influential phosphate depletion estimates, and standard in mineral economics, where reserves have grown through a century of rising production for copper (Tilton, 2003; Tilton and Lagos, 2007). The Australia pair in the table is the typed-classification point in miniature: the MCS tabulated-reserve figure ($5{,}800{,}000$ kt) and the same source's JORC-compliant-or-equivalent footnote figure ($120{,}000$ kt) yield ratios of $2{,}320$ and $48$ years at one production rate. Neither number may be averaged with or substituted for the other without changing the reserve declaration. The reserves/resources split is likewise part of the classification: a resource-threshold calculation $T_{\mathrm{resource},10\%} = 0.9\, G_{\mathrm{resource}}/P$ answers a different question and must not share a column with the reserve-life ratio without an explicit convention label. On MCS 2026's “more than 300 billion tons” world-resource statement, that separate resource arithmetic exceeds $1{,}080$ yr, more than three and a half times the $292$-year reserve ratio; the typed split is what prevents those answers from being collapsed into one number. The exact growth/reclassification relation between the static $292$ and any scenario exhaustion time is Proposition 28, including its narrow high-elasticity crossover; no direction of error is claimed without that scenario.

#### 6.5.4 The fisheries removals-only pressure time

The fisheries column of the classification matrix is the removals-only pressure time. When $\mathrm{SSB}_{\mathrm{now}} > B_{\lim} > 0$ and $F_{\mathrm{now}} > 0$, define $R_B = \log(\mathrm{SSB}_{\mathrm{now}}/B_{\lim})$ and
$$\Theta_F = \frac{R_B}{F_{\mathrm{now}}},$$
the fishing-only time-to-reference: the crossing time of the deliberately incomplete comparison process $\dot B = -F_{\mathrm{now}}B$. With $B_{\lim} = 0.2 \max \mathrm{SSB}$ this is the construction tabled as ADH in Section 6.5.2; the two notations are kept because the boundary hypotheses stated here ($F_{\mathrm{now}} > 0$, $\mathrm{SSB}_{\mathrm{now}} > B_{\lim}$) are exactly the conditions of the positive sub-cohort of Section 6.5.2 (35 stocks, median $2.9$ yr); the reported Section 6.5.2 median ($\approx 1.8$ yr) additionally carries the eight zero entries for stocks at or below the reference, per the zero convention of the source caption. It is a **removals-only pressure timescale**: the time unit comes from rescaling a stock-reference margin by one isolated gross-loss rate. Because recruitment, somatic growth, maturation, natural mortality, density dependence, environmental forcing, and future policy are omitted, $\Theta_F$ is not a net biomass depletion diagnostic, not a demographic hitting-time estimate, and not a member of the $J^{\mathrm{gross}}$–$H^{\mathrm{loc}}$–$T_A$ hierarchy. A genuinely local biomass-decline ratio $H_B^{\mathrm{loc}} = (B - B_{\lim})/[-\dot B]_+$ would require a compatible net $\dot B$ estimate, and a demographic hitting time a fully specified population model; RAM Legacy SSB and $F$ data (Ricard et al., 2012) do not by themselves supply these quantities or models. Spawning biomass is not an abiotic support pool. The construction is retained specifically to show why an isolated gross-removal timescale must not be promoted to a net depletion diagnostic.

**The collective implication for material-flow measurement.** The three published "depletion time" numbers — G3P index, phosphate reserve-life, fisheries removals-only time — answer three distinct questions at three distinct evidentiary levels.

**Proposition 32 (Boundedness, and limiting law, of the persistence index on the declared trend class).** Let
$$a_k=a_0-\beta k+\varepsilon_k,\qquad k=0,\dots,n,$$
with fixed $\beta>0$ and independent mean-zero sub-Gaussian errors $\varepsilon_k$ with variance proxy $\sigma^2$ (the Gaussian simulation below is the special case used for the exhibit). Let $\widehat\beta_n>0$ be the ordinary-least-squares fitted decline rate, on the usable event that the fitted slope is negative, and define
$$I_n:=\frac{a_n-\min_{0\le k\le n}a_k}{\widehat\beta_n}.$$
Then $I_n$ converges in distribution to a finite nondegenerate random variable $M_\infty/\beta$ characterised in the proof; in particular $I_n=O_{\mathbb P}(\sigma/\beta)$ as $n\to\infty$. The intercept $a_0$ cancels, and no physical stock, barrier, or storage coefficient enters the statistic.

*Proof.* The numerator can be indexed backward from the endpoint:
$$M_n:=a_n-\min_{0\le k\le n}a_k=\max_{0\le j\le n}\bigl(\varepsilon_n-\varepsilon_{n-j}-\beta j\bigr).$$
On a two-sided stationary extension of the error sequence, $M_n$ has the same law as $\max_{0\le j\le n}(\varepsilon_0-\varepsilon_{-j}-\beta j)$, an increasing sequence whose limit is $M_\infty:=\sup_{j\ge0}(\varepsilon_0-\varepsilon_{-j}-\beta j)$. This supremum is finite almost surely: by the sub-Gaussian tail bound, $\mathbb P(\varepsilon_0-\varepsilon_{-j}>\beta j/2)$ is summable in $j$ (it is $O(e^{-c\beta^2j^2/\sigma^2})$), so Borel–Cantelli leaves only finitely many indices with $\varepsilon_0-\varepsilon_{-j}-\beta j>-\beta j/2$, while the maximum over that finite random set is finite. Hence $M_n\Rightarrow M_\infty$ (indeed almost surely on the two-sided coupling). For deterministic equally spaced regressors and independent finite-variance errors, the OLS slope is consistent, with variance $O(\sigma^2/n^3)$ in the homoscedastic case; thus $\widehat\beta_n\to\beta$ in probability and the usable event has probability tending to one. Slutsky's theorem gives $I_n=M_n/\widehat\beta_n\Rightarrow M_\infty/\beta$. Writing $\varepsilon_k=\sigma Z_k$ exhibits the scale $\sigma/\beta$. ∎

The archived Gaussian simulation is now an exhibit for a proved limit, not the evidence for boundedness. With 400 replicates at each of $n=10^2,10^3,10^4,10^5$, $\beta=\sigma=1$, and seed 7, it returns mean index $0.21,0.25,0.21,0.25$ and 90th percentile $0.81,0.84,0.95,1.00$, while the anomaly series' deterministic drop $\beta n$ grows by three orders of magnitude across those record lengths. The simulated median is zero at every length because in more than half the replicates the endpoint itself is the record minimum; the proposition does not need that endpoint event, since the backward-maximum representation controls all cases. Lengthening or densifying an anomaly record therefore cannot manufacture a physical horizon from this statistic: its limit is a finite trend-detection quantity expressed in years. This is a property of the declared linear-trend class, not a claim about any basin.

---

### 6.6 What an aggregate record fixes

**Definition 38 (Identifiability set of an event time).** Fix the readout, the declared boxes and
bounds, and an observed aggregate record $z$. The *fibre* $\mathcal F(z)$ is the set of admissible
component initial states whose induced aggregate trajectory equals $z$. The *identifiability set* of
the first component exit time is
\[
\mathrm T(z) \;=\; \bigl\{\tau(x_0) : x_0 \in \mathcal F(z)\bigr\},
\]
and the event time is identifiable from the aggregate record if and only if $\mathrm T(z)$ is a
singleton.

**Proposition 39 (The set is a polytope image, and it is usually an interval).** On the decay pair of
Proposition 31, with $\dot x_i = -x_i$, $Z(t) = 100 e^{-t}$ and barrier $x_i \ge 1$, the fibre is
$\{x_1 + x_2 = 100,\ 1 \le x_1, x_2 \le 99\}$ and
\[
\mathrm T(z) \;=\; \bigl[\,0,\ \log 50\,\bigr] \;=\; [\,0,\ 3.9120\,] \ \text{yr},
\]
its maximum attained at the balanced start $(50, 50)$ and its minimum $0$ attained at either endpoint, where one component starts on its barrier. Both recorded instances lie in the set, $0.6931$ yr from $(2, 98)$ and $3.9120$ yr
from $(50, 50)$, and the aggregate record is silent on everything between them. More generally, where the declared constraints are linear the fibre is a polytope, and a continuous
event time has an interval image on a connected fibre: $\mathrm T(z)$ is that interval, and its endpoints
are its maximum and minimum over the polytope. Those two values are programmes rather than aspirations
exactly where the event time is declared in polyhedral form, $\tau(x) = g(\min_{j \le k}(a_j^{\top} x + b_j))$
with $g$ continuous and increasing: the upper endpoint is the single linear programme over $(x, r)$ with
$r \le a_j^{\top} x + b_j$ for every $j$, and the lower endpoint is the minimum over the polytope's vertices,
finite to enumerate, because a minimum of affine functions is concave and a concave function attains its
minimum at an extreme point. No such reduction holds for an arbitrary continuous event time: its extremum sits
where it sits, and in the instance above it is attained at the balanced start, in the interior of the fibre. Monotonicity of the event time along the fibre
is neither needed nor true in general --- an exit time is typically the minimum of several monotone branch
functions, which is not itself monotone --- and where the declared set is non-convex the fibre can split,
in which case the same two programmes bound the value set from outside instead of recovering it. Identifiability of the event time holds exactly when $\mathrm T(z)$ is a singleton, as Definition 38 states. A singleton fibre is sufficient but not necessary: $\tau$ can be constant on a non-singleton fibre, in which case the aggregate identifies the event time without identifying the component state. Conversely, a non-singleton $\mathrm T(z)$ is a statement about what the aggregate record leaves open, never something the aggregate alone can repair.

*Proof.* $\tau(x_0) = \min\{\log x_1(0), \log x_2(0)\}$ with $x_2(0) = 100 - x_1(0)$: the function is
increasing then decreasing in $x_1$ on $[1, 99]$, symmetric about $50$, with maximum $\log 50$ and
value $\log 1=0$ at both ends, so its image is $[0, \log 50]$. The fibre is an intersection of the declared
boxes with the invariant hyperplane, hence a convex polytope; $\tau$ is continuous, so its image is a
connected interval. Its maximum is not a vertex value --- $\min_j$ of affine functions is concave, and a
concave function attains its maximum where it likes, here at $x_1 = x_2 = 50$ --- while its minimum over the
segment is attained at an end, where $\tau=0$. The two programmes of the statement are read off
those two facts, and the fact that one of them is an interior value is why the polyhedral form is quoted with
its hypothesis instead of as a general method. □
## 7. First-Passage Semantics on Declared Surrogates

### 7.1 Two objects, not one

The ledger's own first-passage object is the model hitting time of Definition 5 — a quantity on trajectories of the mass-conserved ledger or of a named reduced system. The public-data quantities of §6.5 are constructed proxies on observed series. That distinction is the entry discipline of this section: the surrogates below **do not compute the ledger's hitting time**, **do not complete the ledger stochastically**, and **do not identify physical failure thresholds**.

The surrogates used here are standard objects, and the section's content is the discipline attached
to them, not the passage-time formulae. The inverse-Gaussian law and its parameterisations are
those of the first-passage literature on Brownian motion with drift (Chhikara and Folks, 1989;
Redner, 2001); the stochastic machinery is Itô calculus in its textbook form (Øksendal, 2003). The
comparison between a surrogate mean and the deterministic margin is a monotone-dynamics statement
(Smith, 1995), and the barrier construction is the deterministic safety argument used in hybrid-systems
verification, whose stochastic extension is the nearest formal relative of the record-relative
discipline of Section 7.4 (Prajna and Jadbabaie, 2004; Prajna et al., 2007). None of these sources
supplies a calibrated input: every drift, barrier and noise scale entering Sections 7.2 to 7.6 is
declared by the analysis, and the results are statements about the declared class. Transfer noise obeys the same typing as
transfer fluxes: process noise on a conserved moiety must be zero-sum across the pools it moves between,
or must carry an explicit boundary term; where it does neither, the violation is a residual and belongs in
the budget of Definition 23, not in the drift --- a diffusion that creates mass is not a conservative ledger
with noisy data but a different object. The converse discipline holds as well: a bracket on the drift of a
selected set does not transfer to a bracket on its support or on its exit time, so no drift bound in this
section is a deterministic hitting time, and the surrogate means are means.

### 7.2 The observed-drift Brownian surrogate

**Definition 6 (Observed-drift Brownian surrogate).** *Let $A_0$ (local to §7.2–7.4; **not** the half-saturation constant of §2.2) be the latest observed anomaly and $\mu=\hat\mu<0$ the fitted drawdown rate. On the scale of the tabulated series define*
$$A(t) = A_0 + \mu t + \varsigma W_t, \qquad A(0) = A_0 > A_{\min}^{\mathrm{win}},$$
*where $W$ is a standard Wiener process, $\varsigma > 0$ a chosen noise scale, and the process is stopped at first reaching the record-relative barrier $A_{\min}^{\mathrm{win}}$.*

This is a statistical surrogate for the empirical trend extrapolation. It is not a hydrological constitutive law, is not mass-conserving, and is not a perturbation or stochastic completion of the ledger's active-pool equation or of the finite-donor primitive system of Section 2.2. The non-completion non-claim is part of the definition.

### 7.3 The inverse-Gaussian groundwater first passage

**Proposition 18 (Inverse-Gaussian first passage — a standard fact, stated for notation).** *Let $T_{\mathrm{GW}} = \inf\{ t > 0 : A(t) \le A_{\min}^{\mathrm{win}} \}$ for the process of Definition 6 and $d = A_0 - A_{\min}^{\mathrm{win}} > 0$. Conditional on treating $\mu$ and the barrier as fixed,*
$$T_{\mathrm{GW}} \sim \mathrm{IG}(\nu, \lambda), \qquad \nu = \frac{d}{|\mu|}, \qquad \lambda = \frac{d^2}{\varsigma^2},$$
*in the mean–shape parameterization; in particular $\mathbb{E}[T_{\mathrm{GW}}] = \nu = H^{\mathrm{win}}_{\mathrm{GW}}$ — the deterministic horizon to the window minimum, $= d/|\mu|$ — and $\operatorname{Var}(T_{\mathrm{GW}}) = \nu^3/\lambda = d\,\varsigma^2/|\mu|^3$.*

*Proof.* The first-passage time of a Brownian motion with constant negative drift to a lower barrier is inverse Gaussian — the classical first-passage result (Chhikara and Folks, 1989; Redner, 2001) — with the stated mean and shape parameters; the standard inverse-Gaussian moments give the displayed mean and variance. □

The mean of the stochastic surrogate equals the deterministic trend-to-window-minimum ratio of §6.5.1.

**Corollary 19 (Zero-noise limit and median).** *As $\varsigma \to 0^+$, $T_{\mathrm{GW}} \to H^{\mathrm{win}}_{\mathrm{GW}}$ in probability, and at $\varsigma = 0$ the deterministic trajectory reaches the barrier exactly there. For every finite $\varsigma > 0$ the inverse-Gaussian median $m$ satisfies*
$$m < \nu = H^{\mathrm{win}}_{\mathrm{GW}}, \qquad F_T(\nu) = \frac{1}{2} + e^{2\lambda/\nu}\,\Phi\!\left( -2\sqrt{\lambda/\nu} \right) > \frac{1}{2}.$$
*The variance scales as $\varsigma^2$ and the standard deviation and small-noise quantile widths as $\varsigma$. The median below the mean is the inverse Gaussian's right skew toward short passage times; the inequality must not be inverted.*

*Proof.* Evaluate the inverse-Gaussian CDF $F_T(t) = \Phi(\sqrt{\lambda/t}(t/\nu - 1)) + e^{2\lambda/\nu}\Phi(-\sqrt{\lambda/t}(t/\nu + 1))$ at $t = \nu$: the first term is $\Phi(0) = 1/2$ and the second is strictly positive for finite $\lambda$, so the median lies strictly below the mean; the concentration statement follows from the variance. □

These are conditional distributional statements about the surrogate. They are not corrections to the tabled years, and they do not show that physical water mass is depleted faster.

### 7.4 The record-relative barrier discipline

The barrier $A_{\min}^{\mathrm{win}}$ is selected from the same finite observation window used to estimate $\widehat\mu$. It is therefore a path-dependent, record-relative threshold, not an independently identified hydrological failure floor. Three boundary facts complete the discipline.

1. **Already-at-minimum.** If $A_0 = A_{\min}^{\mathrm{win}}$, the stopping-time convention gives $T_{\mathrm{GW}} = 0$ deterministically for every $\varsigma$; the inverse-Gaussian family has a degenerate boundary limit concentrated at zero, and $\mathrm{IG}(0,0)$ is not an ordinary inverse-Gaussian distribution. Zero cells report zero relative to the selected observational barrier — not zero physical uncertainty and no confirmation of collapse.
2. **Independent physical thresholds.** If an independent physical threshold $A^\sharp < A_{\min}^{\mathrm{win}}$ is specified, the same constant-drift surrogate gives the conditional mean $\mathbb{E}[T^\sharp] = (A_0 - A^\sharp)/|\mu|$, longer than the record-relative proxy because the barrier is lower. This is a statement within the surrogate, not a general lower-bound theorem for the physical ledger, whose drift and state coupling may differ.
3. **Classification.** The load-bearing content is the interpretation boundary itself: a record-relative barrier makes the passage time a property of the observation window, and no reading of the tabled numbers escapes that qualification.

### 7.5 The geometric-Brownian fisheries first passage

**Proposition 20 (Geometric-Brownian correction — a standard fact, stated for notation).** *Let $dB_t = -hB_t\, dt + \varsigma B_t\, dW_t$ under the Itô convention with $h > 0$ and $0 < B_{\min} < B_0$, and $T_{\mathrm{fish}} = \inf\{ t > 0 : B_t \le B_{\min} \}$. Then*
$$T_{\mathrm{fish}} \sim \mathrm{IG}(\nu_F, \lambda_F), \qquad \nu_F = \frac{\log(B_0/B_{\min})}{h + \varsigma^2/2}, \qquad \lambda_F = \frac{\log(B_0/B_{\min})^2}{\varsigma^2},$$
*so $\mathbb{E}[T_{\mathrm{fish}}] = \log(B_0/B_{\min})/(h + \varsigma^2/2)$; as $\varsigma \to 0^+$ this converges to the deterministic pure-decay horizon when $h = F$ and $B_{\min} = B_{\lim}$.*

*Proof.* Itô's lemma (Øksendal, 2003) gives $d\log B_t = -(h + \varsigma^2/2)\, dt + \varsigma\, dW_t$, so the logarithmic threshold is a Brownian first-passage problem with initial distance $\log(B_0/B_{\min})$ and downward drift $h + \varsigma^2/2$; Proposition 18 applies. Under the Stratonovich convention the log-drift would be $-h$ and the deterministic limit would match the pure-decay horizon $h = F$ exactly: the $\varsigma^2/2$ shortening is the Itô choice, not a property of the physical process. □

For fixed arithmetic drift and the Itô parameterization, the finite-noise mean is strictly shorter than the deterministic horizon. This is a property of the chosen surrogate parameterization; it is not a universal claim that environmental variability accelerates physical biomass loss. The construction joins the removals-only classification of §6.5.4 — the same pure-decay process, now under a declared stochastic surrogate.

### 7.6 The constant-production phosphate passage time

Under the deterministic surrogate $\dot G = -P$ with constant production $P > 0$, the first-passage time to a fixed threshold $G_{\min} \in [0, G_0)$ is
$$T_{\mathrm{phos}} = \frac{G_0 - G_{\min}}{P},$$
the reserve-life ratio being the $G_{\min} = 0$ special case and a threshold fraction $\varepsilon G_0$ giving $(1-\varepsilon)G_0/P$. This is a conditional reserve-classification proxy under constant production; because reserves are an economic classification rather than a fixed physical stock, it is not a forecast of geological exhaustion without an explicit resource and production model. No stochastic phosphate extension is required for the interpretation.

The classification addresses the status of the ratio, not the adequacy of the resource base. The
reserve-life convention and its long defence against depletion-pessimistic readings are the subject of
a separate literature (Tilton, 2003; Tilton and Lagos, 2007), whose arguments about substitution,
price-induced discovery and economic recovery are exactly the premises this paper registers as
carried, not discharged; nothing here contradicts them.

### 7.7 The explicit non-claims

The first-passage semantics close with seven explicit non-claims, all of which hold here:

1. The Brownian and geometric-Brownian processes are not stochastic completions of the ledger and do not conserve its mass compartments. 2. No theorem relates $\widehat\mu$ to $-\dot A$ of the reduced systems, to the finite-donor primitive system, or to the institutional delay equations. 3. The model hitting time $T_A$ of Definition 5 is not shown to be inverse Gaussian: it would be inverse Gaussian only if the active-pool residual were Brownian with constant drift, which the coupled balance (2) does not supply — the tabled groundwater numbers inherit inverse-Gaussian means from Definition 6's surrogate and from nothing else. 4. The historical groundwater minimum is not an independently identified physical failure barrier. 5. A shorter surrogate median or Itô mean is not evidence of faster physical depletion. 6. The gross active-pool horizon $H_A^{\mathrm{gross}}$ of Definition 3 and its productivity-illusion interpretation — the misreading of a large gross-turnover horizon as evidence of slow net depletion, the false implication recorded in Section 6.1 — are not first-passage results treated here. 7. The fisheries calculation is not a stage-structured fisheries model, and the phosphate calculation is not a geological-reserve model.

### 7.8 Parameter and observation uncertainty

The inverse-Gaussian results condition on the drift, the barrier and the noise scale. Measurement error, serial dependence, seasonal forcing, spatial aggregation, trend breaks and common climatic drivers are **separate** uncertainties, and integrating any of them out yields a predictive mixture rather than a single inverse-Gaussian law. A residual scale estimated from the same window does not by itself identify process noise. **No calibrated predictive distribution is claimed**; the full uncertainty treatment belongs to an empirical identification study, not to this paper. For industrial-ecology measurement this discipline is the practical message: first-passage distributions on declared surrogates are usable as descriptive statistics, but their drift, barrier, and noise inputs each carry their own identification story, and a calibrated forecast requires that story to be discharged.

---

## 8. Domain Templates at Registered Status

### 8.1 The phosphorus template

The phosphorus domain enters at **registered template status**: an identification ladder for the resource–product–waste–detritus structure of §2.3 (phosphate rock → fertilizer → soil pool → runoff, with the mining flux $c_G$ and the recycling routes $\alpha,\rho_P$), whose constitutive content — the yield and loss functions, the recovery fractions, the price response of the reserve classification — is **declared, not established**. The template's competing-model ladder is an identification object, and its falsification protocols — *which observation would reject which routing assumption* — are recorded obligations, not results. The ladders themselves are the supplementary's S2, next to the groundwater ladder this one pairs
with, and the registered detail these paragraphs used to carry --- the competing-model structure and the
falsification protocols in full --- is its S14; nothing in Sections 6 to 10 uses either.

### 8.2 The groundwater template and the two-pool gap

The groundwater template enters at registered status with one admitted object and one declared gap: the
admitted object is the one-pool affine approximation behind the anomaly-persistence index of Section 6.5.1, and
the two-pool model --- active storage with a slow donor pool, the two-compartment structure of Section 2.2 ---
is not established. The registered identification requirements for closing that gap, and the discipline that
leakage terms may not absorb unexplained residuals, are the subject of the supplementary's S2.1, and none of
them is met by the record used in Section 6.5; the registration as this paper previously stated it is the
supplementary's S14.

### 8.3 Extractor-side harvest economics

On the extractor side, the same discipline applies to economic steady states. In the open-access equilibrium of a single-species fishery (Clark, 1990), the bioeconomic equilibrium stock $S_{\mathrm{OA}} = c/(pq)$ is set by cost, price, and catchability — and is infeasible as a management target under a conservation floor $S_{\min} > S_{\mathrm{OA}}$: the unregulated equilibrium lies below the floor, and no open-access trajectory is viable against it. The modified golden rule in its constant-unit-cost form, $g'(S_\delta) = \delta$, sets the optimal steady stock for the discount rate $\delta$ (Clark's general form carries an additional marginal-stock-effect term); a harvest tax shifts the open-access equilibrium to $S_{\mathrm{OA}} = c/((p - \tau)q)$ — the tax moves the economic equilibrium, but it does not move the physical floor. The distinction is the extractor-side counterpart of the accounting discipline of Section 6: instrument parameters and constraint thresholds are different objects, and no tax schedule substitutes for a constraint the ledger must satisfy. The growth function $g$ of this paragraph is a declared constitutive readout on the stock **for this extractor-side remark only**; it is not a primitive of the closed natural block of Section 2, and nothing in this section is promoted into the typed ledger.

---

## 9. The Interface with Institutional Delay Dynamics

The partition between this paper and the companion delay-dynamics analysis (Abaee, 2026a, doi:10.5281/zenodo.22554217) is fixed by an interface contract. This paper owns the closed material accounting: the primitive ledger equations and full routing, the conservation and positivity theorems of Section 4, the componentwise deficit and depletion diagnostics of Sections 5–6, and the closed-donor no-rest and extraction-integrability limitations. The companion owns the open frozen-donor retarded systems and their bifurcation results. The interface is viable — but **not** because the closed primitive ledger dynamically reduces to the open working system.

**The exact shared object.** Under the single-resource specialization of Section 5.4 ($\mu = \nu = \rho = 0$ — the product, waste, and price parameters of the unreduced ledger: its macroeconomic-feedback, recycling, and price-response channels, per the Section 2.2 gloss — and the mining intensity $C^A = 0$) — with the local stock equation $\dot N = R - qEN$, the deficit identity
$$D(t) := qE(t)N(t) - R(N(t), A(t)) = -\dot N(t), \qquad \Lambda(t) := [D(t)]_+ = [-\dot N(t)]_+$$
holds for every trajectory of either the specialized ledger or the reduced core (Remark 16). The reduced core's constitutive replacement $R(N,A)\to rN(1-N/K)$ is separately an approximation and carries its own finite-time scope (Theorem 1 and Remark 2: the replacement is pointwise on the interior support region and non-uniform through the depleted-pool boundary). The shared object includes the non-negative orthant and the sign pattern of harvest as an outflow from the living stock. **A companion model that routes the "unsustainable portion" of a flow into a different compartment changes the incidence and thereby leaves the interface** (§2.5).

The institutional states are not compartments of the mass ledger, so closure of an ecological–institutional subsystem is a hypothesis about the arguments of their laws, not a consequence of the incidence matrix. It is stated once, in the form actually used.

**Interface Hypothesis I (declared memory and effort maps).** Let $\xi=(N,A^{\mathrm{act}},A^{\mathrm{geo}},U)$ be the natural block of equation (2) under the institutional-failure specialization, let $h\ge0$ be the maximal declared delay, and write $\xi_t$, $Z_t$, and $E_t$ for history segments on $[-h,0]$. Define the instantaneous algebraic decline pressure from current/history values by
$$\Lambda(\xi,E):=\bigl[qEN-R(N,A^{\mathrm{act}})\bigr]_+,$$
which equals $[-\dot N]_+$ along solutions of (2) but requires no derivative of a history segment. The institutional laws have the form
$$\dot Z(t)=F_Z(\Lambda_t,Z_t,E_t),\qquad \dot E(t)=F_E(\Lambda_t,Z_t,E_t),$$
for declared causal, locally Lipschitz history functionals $F_Z,F_E$ (with $\Lambda_t$ the history segment generated by $\Lambda(\xi,E)$), and they keep the effort entering (2) in its declared nonnegative range. The decisive restriction is the argument list: neither $F_Z$ nor $F_E$ takes a product, waste, inert, price, macroeconomic, or other excluded-ledger state as an argument. Excluded equations may be appended downstream and driven by $(\xi,Z,E)$, but exert no feedback on $F_Z$, $F_E$, or (2).

**Proposition 43 (Closure of the declared ecological–institutional subsystem).** *Under the institutional-failure specialization of Section 5.4 and Interface Hypothesis I, the ecological–institutional subsystem is closed on its history space: an initial natural-block history together with initial $Z$ and $E$ histories determines $(\xi,Z,E)$ without any excluded variable, for every parameter value for which the declared maps satisfy Hypothesis I and the retarded system is well posed. No singular limit, small parameter, or timescale separation is used. Projection from a full appended system satisfying the one-way condition in Hypothesis I to this subsystem intertwines the two solution flows; the excluded variables are then driven readouts as far as this subsystem is concerned.*

*Proof.* The four natural-block right-hand sides in (2) depend only on the current $\xi$ and current $E$. By Hypothesis I, $\dot Z$ and $\dot E$ depend only on history segments of $\Lambda(\xi,E)$, $Z$, and $E$. Hence the six laws form a retarded system on the product history space of $(\xi,Z,E)$ with no excluded argument; local Lipschitz continuity gives the usual local well-posedness, and continuation is governed by that subsystem alone. If further variables $w$ obey $\dot w=G(\xi,Z,E,w)$ with no feedback into the six laws, solving the subsystem first and then the driven $w$-equation gives the appended solution, so coordinate projection intertwines the flows. ∎

The proposition's scope is exactly its hypothesis. It does not say that $Z$ and $E$ are projections of mass compartments—they are additional institutional states—and it does not prove from a citation alone that any particular companion implementation has the required argument list. That is a check against the companion's displayed equations (its gated memory–effort core is the intended instance when its input is $qEN-R$ and no excluded feedback is present). In particular, Proposition 43 supplies no semiconjugacy to the companion's *working* active-pool completion and transfers no bifurcation result in either direction. If a memory or effort law is modified to read a price, product, waste, or macroeconomic state, Hypothesis I fails and closure must be reproved for the enlarged subsystem.

**The non-reduction boundary.** “Reduction” needs a definition before its absence can be a theorem. A *coordinate-preserving exact reduction* (or factor) from the closed system to the working system is a $C^1$ map $\pi$ between their state/history spaces that fixes the named shared coordinates—at least $N$, $A^{\mathrm{act}}$, and where the working history carries them, $U$, $Z$, and $E$—and intertwines the solution maps, $\pi\circ\Phi_{\mathrm{closed}}^t=\Phi_{\mathrm{working}}^t\circ\pi$. Differentiating at $t=0$ forces the two fields to agree on every shared coordinate at corresponding states. A *regular small-parameter approximation* is a family of closed fields, obtained by a named scaling of the closed system, converging uniformly on compact subsets of the common coordinate domain to the working field while the registered constants $\kappa_A$, $K$, $\omega_A$, and $A^{\mathrm{eq,intrinsic}}$ retain their meanings. The theorem below addresses exactly those two notions. It does not address arbitrary nonlinear conjugacies that rename or mix the physical coordinates, nor loose finite-time “tracking” claims with an unspecified tolerance.

Only one working-system equation is needed. Its registered active-pool law is
$$\dot A_W=-B(N,A)+\omega_A(A^{\mathrm{eq,W}}-A),\qquad A^{\mathrm{eq,W}}=A^{\mathrm{eq,intrinsic}}+\frac{\kappa_AK}{\omega_A},$$
whereas the closed law in (2) is
$$\dot A_C=-B(N,A)+\omega_A(A^{\mathrm{eq,intrinsic}}\sigma-A)+\gamma_UU,\qquad \sigma=\frac{A^{\mathrm{geo}}}{A^{\mathrm{geo}}+A_{g0}}\in[0,1].$$
At the same named state their difference is therefore exact:
$$\dot A_W-\dot A_C=\kappa_AK+\omega_AA^{\mathrm{eq,intrinsic}}(1-\sigma)-\gamma_UU.$$
On the nonempty coordinate face $U=0$ this difference is at least $\kappa_AK=5$ stock units per year at the registered values, for every donor fraction $\sigma$. That single display is the short-time obstruction; the remaining observations separate what does and does not follow from it.

1. **Different targets and an exact same-state field gap.** The primitive ledger uses the intrinsic donor-limited target $A^{\mathrm{eq,intrinsic}}=50$; the working completion uses $A^{\mathrm{eq,W}}=50+\kappa_AK/\omega_A=5050$. Those are targets, not two equilibria: the working point's active pool $A^{\mathrm{act,*}}=397.87$ is about eight times the intrinsic target, while the two targets differ by a factor of $101$. Under the registered scale separation $\sigma\approx1$, the exact difference formula above is approximately $\kappa_AK-\gamma_UU$: about $0.535$ stock units per year at the working point's quasi-rest detritus level ($\gamma_UU=\mathcal T^*\approx4.47$) and $5.000$ at $U=0$. The flux readings behind the latter are the working recharge $\omega_A(A^{\mathrm{eq,W}}-A^{\mathrm{act,*}})=4.652$ and, at $\sigma=1$, the closed donor flow $\omega_A(A^{\mathrm{eq,intrinsic}}-A^{\mathrm{act,*}})=-0.348$. The $U$-dependence is structural: the working $A$-field omits the detritus return $\gamma_UU$ that the closed field carries. The turnover identity $\mathcal B^*-R^*=\mathcal T^*$ is not this field difference.
2. **The working point is not a closed rest point.** It requires continuing geological support — the flux $\omega_A(A_{\mathrm{eq},W}-A_{\mathrm{act},*})=4.652133\ldots$ stock units per year, supplied every year by a donor the working system treats as a parameter — and is not a rest point of the closed finite-donor system (Theorem 12). At the same state, under the registered $\sigma\approx1$ reading, the closed primitive donor flow is $e_{GA}-e_{AG}=\omega_A(A^{\mathrm{eq,intrinsic}}\sigma-A^{\mathrm{act,*}})\approx\omega_A(A^{\mathrm{eq,intrinsic}}-A^{\mathrm{act,*}})\approx-0.348$: **the donor gains in the closed ledger where the working completion has it losing 4.652** — the two fields have opposite signs on the donor coordinate, not merely different magnitudes. The working-point figures $E^* \approx 2.090$, $N^* = 89.526$, $A^{\mathrm{act,*}} = 397.87$, and the recharge $4.652$ are imported at the companion's registered precision; the reverse check $qE^*N^* = 0.001 \times 2.090 \times 89.526 \approx 0.187$ is consistent to the quoted digits.
3. **The long-time budget differs.** The closed primitive system makes sustained extraction integrable (Theorem 14), so it cannot sustain the working positive extraction flux indefinitely. This is an independent long-time incompatibility with interpreting a frozen-donor positive-flux regime as a closed-system regime; the theorem below does not need it, because item 1 already blocks the two named reduction notions at $t=0$.

A diagnostic often quoted in this discussion is deliberately **not** a reason in the proof: $\varepsilon_G(T)=G_0^{-1}\int_0^T|e_{GA}-e_{AG}|dt$ measures cumulative donor draw inside one completion. It is not a distance between trajectories or fields, and neither its smallness nor its largeness proves or refutes a reduction. It may be reported as a budget diagnostic only.

**Theorem (No coordinate-preserving exact or regular reduction to the open working completion).** *For the closed primitive ledger (2) and the registered working active-pool law above, with the named shared coordinates and registered constants held fixed, there is no coordinate-preserving exact reduction and no regular small-parameter approximation in the senses defined at the start of this boundary discussion.*

*Proof.* A coordinate-preserving exact factor would fix $A^{\mathrm{act}}$ and intertwine the flows, so differentiation at $t=0$ would force $\dot A_W=\dot A_C$ at every corresponding same-named state. But on $U=0$ the exact difference is $\kappa_AK+\omega_AA^{\mathrm{eq,intrinsic}}(1-\sigma)\ge\kappa_AK=5>0$, a contradiction. The same lower bound blocks uniform convergence on any compact common-coordinate set meeting $U=0$ for any scaling family whose fields retain the closed law's target and constants: the $A$-components remain at least $5$ apart there rather than converging. ∎

Theorem 12 and Theorem 14 add the rest-point and long-time incompatibilities recorded in items 2 and 3, but they are corroborating separations, not premises needed for the two reduction conclusions just proved. The theorem makes no claim about a conjugacy that mixes $A^{\mathrm{act}}$ with donor, detritus, memory, or price coordinates; such a map would no longer be a reduction *of these named material coordinates*, and its existence or nonexistence is a different mathematical question.

The permitted relation is analogy for shared mechanism language, plus diagnostic reconstruction of omitted mass flows. The companion's global periodic results are properties of its reduced systems and do not transfer to the closed primitive ledger; in particular, Hopf or periodic orbits of the frozen-donor working system are not properties of (2). In the other direction, the working system is an open projection: omitted turnover is routed to a diagnostic detritus or inert sink, imposed recharge corresponds to geological draw, and the reduced trajectory's mass discrepancy is reconstructible from the omitted flows.

**The frozen-donor scaling does not remove the gap.** Rescaling the donor as $A^{\mathrm{geo}}=G_0g$ with $g(0)=1$ gives $\dot g=-G_0^{-1}(e_{GA}-e_{AG})$. With $A_{g0}$ fixed, $G_0\to\infty$ sends $\sigma\to1$ and freezes the scaled donor fraction, but the limiting closed recharge field still uses $A^{\mathrm{eq,intrinsic}}$, not $A^{\mathrm{eq,W}}$; on $U=0$ the field gap tends to $\kappa_AK=5$, not to zero. This is the regular-perturbation clause of the theorem for that named scaling. Local Hopf persistence of the working system under this primitive scaling is not claimed; a different derived-target completion would be required before such a perturbation theorem could be formulated.

**The long-time finite-budget interpretation.** With the donor included as a state and Interface Hypothesis I in force, the closed system is an autonomous retarded equation on its history space; the donor is “slow” only under an additional large-donor scaling, not by definition. The companion's $\tau_+ \approx 150$ yr upper cycle is a frozen-donor object. On the closed system, Theorem 14 supplies the correct budget object: if extraction from the natural block is sustained at a rate at least $c>0$, its duration is at most $M(0)/c$, where $M(0)=N(0)+A^{\mathrm{act}}(0)+A^{\mathrm{geo}}(0)+U(0)$ is the **total** initial natural-block mass. It is not $G_0/c$ in general, because the active pool, living stock, and detritus can also supply extraction and because gross donor outflow can be offset by return flow. A donor-only bound $G_0/c$ would require the extra hypothesis that *net* donor outflow is sustained at at least $c$ with no replenishment of the donor from the rest of the block. At $c=qE^*N^*\approx0.187$, the theorem-scale is therefore $M(0)/0.187$; the previously quoted donor-dominated scale $G_0/c\approx2\times10^6$ yr is only an order-of-magnitude reading when $M(0)$ is dominated by $G_0$ under the registered scale separation. Likewise $G_0/4.652\approx8.6\times10^4$ yr is a diagnostic draw scale for the working completion's imposed support flux, not a closed-system duration bound. Whether frozen-donor local Hopf structure persists as a slowly drifting transient in the closed donor system is an open slow-passage problem; the mass budget alone does not establish it. The implication for industrial-ecology coupling is concrete: a closed physical ledger and an open working system can share one diagnostic identity without sharing a dynamics, and the temptation to import one system's theorems into the other must be resisted.

The companion analysis supplies the one numerical fact about governance timing that this paper may
use without re-deriving it: at its calibrated point, annual review under the mobilising law is
unstable, and stability returns above a review interval of about 6.5 years, with the two subcritical
Hopf crossings of the continuous-delay problem certified near 3.7 years and 150 years. The readout of
Section 6.4 inherits the consequence. A margin computed at an interval longer than the admissible
one is not conservative, because the declared object it is computed on has already changed between
reviews; the admissible interval is a property of the institutional block, is reported there, and is
not estimated here.

---

## 10. What the Ledger Does Not Support

### 10.1 Compensatory aggregation is rejected, not merely discouraged

On the unreduced ledger, no scalar weighting of components is authorized by the accounting itself. The precise statement is on the feasible balance domain (Definition 1): a weighted sum $\sum_m w_m s_m$ certifies componentwise adequacy $s_m \ge d_m$ for all $m$ on $\mathcal{B}(x,t)$ only through an implication proved from the physical restrictions defining the domain — and, in general, no such implication holds. The feasible domain can admit vectors with a positive aggregate and a negative component, exactly the geometry documented in the composite-indicator literature (Munda and Nardo, 2009). In short: a positive weighted sum does not, without a proved restriction on the feasible balance domain, certify componentwise non-negativity.

**Proposition (No weighted certification).** *Let $\mathcal{B}(x,t)$ be the feasible balance domain (Definition 1). If $\mathcal{B}(x,t)$ contains a vector with $b_i < 0$ and $w^\top b > 0$ for a fixed $w \ge 0$, then the certificate $\{w^\top b \ge 0\}$ does not imply $b \ge 0$; if $\mathcal{B}(x,t)$ is not known to exclude that pattern, no nonnegative weighting is authorized as a componentwise certificate.*

*Proof.* On the exhibited vector the componentwise predicate fails ($b_i < 0$) while the weighted predicate holds ($w^\top b > 0$); the two predicates differ on $\mathcal{B}(x,t)$. The inverse-horizon score of Section 6.5.2 (Non-example 1) is the worked witness: a positive aggregate coexisting with componentwise deficits by construction. □

The compensating pattern is constructible against **any** weight, so the failure is universal to the method of weighted certification.

**Theorem (Universal failure of weighted certification).** *Let the ledger have $m \ge 2$ components. For every weight vector $w\in\mathbb R^m_+$, $w\ne0$, there exist a typed ledger as in §2, a demand vector $d$, and an admissible state–operation pair $(x,u)$ with $u\in\mathcal U(x,t)$ whose attainable balance $b=O(x,u,\theta)-d$ satisfies $w^{\top}b\ge0$ while $b_m<0$ for some component $m$. No nonnegative weighting is therefore a valid componentwise certificate in general.*

*Proof.* Take the two-compartment ledger with stock $x = (x_1, x_2) \in \mathbb{R}^2_+$, one donor-limited transfer flux $f = kx_1$ from compartment 1 to compartment 2 ($k > 0$), identity readout $\mathcal{O}(x, u, \theta) = x$, and demands $d = (d_1, d_2)$. Every nonnegative state is admissible with the declared flux, because donor limitation holds ($f = 0$ at $x_1 = 0$), so the balance $b = x - d$ is attainable for every $x \in \mathbb{R}^2_+$; the admissible operating set is the flux declaration itself. Fix $w$ and let $j$ be an index with $w_j > 0$. If some $m \neq j$ has $w_m = 0$, place the deficit there: choose $x_m < d_m$ and $x_j \ge d_j$, giving $w^\top b = w_j (x_j - d_j) \ge 0$ while $b_m < 0$. Otherwise $w_m > 0$ for every $m \neq j$: choose any $m \neq j$ with $x_m < d_m$, and choose $x_j \ge d_j + \bigl( w_m (d_m - x_m) + \varepsilon \bigr)/w_j$ for any $\varepsilon > 0$. Then
$$w^\top b = w_m (x_m - d_m) + w_j (x_j - d_j) \ge w_m (x_m - d_m) + w_m (d_m - x_m) + \varepsilon = \varepsilon \ge 0,$$
while $b_m = x_m - d_m < 0$. The pair $(x, d)$ is the witness for $w$. □

The construction never uses the dynamics: the failure is a property of nonnegative weightings over mixed-sign balances, not of the donor-limited positivity mechanism. Consequently, on any feasible balance domain containing a compensating pair — and Definition 1's domain is exactly that whenever the operating set admits states with mixed balances — no nonnegative weighting can stand in for the conjunctive criterion of Section 3.2. The reading is the algebraic form of the weak-comparability thesis stated in §1.1.

The companion assessment analysis (Abaee, 2026c, doi:10.5281/zenodo.22545740) proves the dynamic form of the same separation for transition operators; the ledger side contributes the static prerequisite: the aggregation question is only well posed after the balance domain is declared, and the burden of proof sits on the aggregation, not on the componentwise report. The same separation holds at the service layer: a weighted sum on $\mathcal{B}(x,t)$ cannot see the directional support gap $(1 - \alpha_{\mathrm{reg}})\bar s$ of Definition 2 — an aggregate that mixes regenerative and non-regenerative provenance never reports which component carries the gap. In the terminology fixed in §1.1: componentwise adequacy on the typed ledger is a **strong-assessment conjunctive predicate**; a positive weighted sum is a **weak-assessment ranking or alarm device**. The ledger authorizes the first as a componentwise certificate and the second only for the weaker semantic role its construction supports. Neither label, by itself, says whether the underlying cycle is stationary-closing; that is Definition 21's separate dynamical question.

**Proposition 29 (The certifying aggregator is unique).** Let $r\in\mathbb R^{n}$ be component
adequacies expressed in common units, and let $\mathcal A:\mathbb R^{n}\to\mathbb R$ be monotone,
$r\le r'\Rightarrow\mathcal A(r)\le\mathcal A(r')$, calibrated, $\mathcal A(c\mathbf 1)=c$ for
every $c$, and certifying, $\mathcal A(r)\ge c\Rightarrow r\ge c\mathbf 1$ for every $c$. Then
$\mathcal A(r)=\min_ir_i$.

*Proof.* Certification at $c=\mathcal A(r)$ gives $\min_ir_i\ge\mathcal A(r)$. Since
$r\ge(\min_ir_i)\mathbf 1$, monotonicity and calibration give $\mathcal A(r)\ge\min_ir_i$.
□

For any admissible aggregator the compensation premium
$$\Pi(r)=\mathcal A(r)-\min_ir_i\ \ge\ 0$$
measures the part of a published aggregate that was produced by cross-component trades. Calibration
cannot be dropped: the additively separable functional $\sum_i\min(0,r_i)$ is continuous, monotone,
faithful in the sense that a nonnegative value admits no deficit, and complete in the sense that no
deficit forces a negative value; it is not the minimum and it is not calibrated. It reports the depth
of the deficits where the minimum reports their existence, and either may be published provided
neither is called the other. Nor can monotonicity be strengthened to strict monotonicity while
keeping both directions: if a continuous $\mathcal A$ satisfied $\mathcal A(r)\ge0\Leftrightarrow
r\ge0$, then $\mathcal A$ would vanish on the faces of the nonnegative orthant, since it is
negative wherever some component is and nonnegative on the orthant, and continuity forces equality
at the boundary; a strictly increasing functional then cannot take one value at $(0,1)$ and another
at $(0,2)$. Certification and strict monotonicity are incompatible, which is why the minimum is not
an arbitrary convention.

**Proposition 30 (Worst concealed deficit at a published aggregate).** Let the component balances lie in declared finite bounds $\ell\le b\le u$, let $w\ge0$, $w\ne0$, and let $z$ be a published aggregate value for which the feasible set $\{b:\ w^{\top}b=z,\ \ell\le b\le u\}$ is nonempty (as it is when $z$ was computed from an admissible $b$ inside those bounds). The signed worst concealed deficit in component $j$ at that exact aggregate is
$$\delta^{*}_j(z)=\max\ \{-b_j:\ w^{\top}b=z,\ \ell\le b\le u\},$$
a linear programme over a nonempty compact polytope, hence finite and attained. Moreover,
$$\delta^{*}_j(z)>0\quad\Longleftrightarrow\quad \exists\, b\ \text{with}\ w^{\top}b=z,\ \ell\le b\le u,\ \text{and}\ b_j<0.$$
The existence of some other admissible vector with $b_j<0$ at a different aggregate value is not sufficient. If $\delta^{*}_j(z)\le0$, the reported concealed deficit is $[\delta^{*}_j(z)]_+=0$, and $-\delta^{*}_j(z)$ is instead a forced minimum surplus in component $j$ under those bounds. Together with the premium this turns noncompensation into a two-sided audit: the premium measures what a displayed aggregate bought with trades, and $[\delta^{*}_j(z)]_+$ measures what the same aggregate value could hide. Where the bounds or aggregate construction are not declared, the value is reported as not established.

*Proof.* The feasible set is a nonempty compact polytope, so the linear objective $-b_j$ attains its maximum. If that maximum is positive, any optimizer is feasible at the same $z$ and has $b_j<0$. Conversely, any feasible vector at the same $z$ with $b_j<0$ gives a positive objective value, hence a positive maximum. □

**Proposition 31 (Aggregates do not transport event times).** Let two stocks and their sinks obey
$\dot x_i=-kx_i$, $\dot w_i=kx_i$ with $k>0$, so that each pair conserves material and remains
nonnegative, and let the aggregate $Z=x_1+x_2$ obey the exact closed dynamics $\dot Z=-kZ$. The
initial states $(x_1,x_2)=(2,98)$ and $(50,50)$ generate the identical aggregate trajectory
$Z(t)=100e^{-kt}$ and, at the common lower barrier $x_i\ge1$, first hitting times $(\log2)/k$
and $(\log50)/k$. No function of the aggregate trajectory determines the component event time.
Dynamical closure and barrier observability are therefore separate obligations: an exact reduced
model is not thereby competent about the events its components are declared to suffer.

*Proof.* Direct evaluation of each exponential at its own barrier; the two aggregate trajectories
coincide identically. □

The asymmetry is exact and one-directional. A coarse aggregate can refute the corresponding aggregate barrier statement and can alarm through a positive premium; it does not certify componentwise adequacy whenever Proposition 30's exact feasibility condition gives $\delta^{*}_j(z)>0$ at the published value. Whether that condition holds is an LP on the declared domain, not a slogan about all aggregates.

### 10.2 The double-counting discipline

Five rules, each carried by a proved or defined statement of this paper and specified as a checkable procedure in the companion methods study (Abaee, 2026d), jointly prevent double counting and phantom mass:

1. **One balance per moiety.** Conservation laws attach to declared moieties (Theorems 7–8); adding unlike units — biomass, money, biodiversity indices, exergy — does not create a *typed* conserved scalar. Such a numerical sum can be declared as a separate readout, and if its summands are separately invariant it may be ambiently invariant, but Proposition 42 does not authorize calling it a typed conservation law. 2. **Explicit stoichiometry.** Entries are added within an incidence row only when their types and units agree; every conversion is an explicit coefficient in $S_{\mathcal{T}}$, never an implicit sum (Section 2.1). 3. **Yield routing.** A transformation represented with yield below one must route the omitted fraction to a represented compartment or a declared boundary flow; otherwise the moiety balance holds only after silently dropping the moiety (Theorem 15). 4. **No ghost sinks.** Every primitive with an outflow from some compartment must have its routed inflow represented, and every inflow its source — opposite-sign incidence of the same primitive is checkable column by column — and the six-state cancellation of Section 4.9 shows the check passing, while the same template shows that cancellation without donor-limited admissibility establishes nothing. 5. **Classification labels stay out of the columns.** Reserve-life and resource-threshold quantities answer different questions and share a column only under an explicit convention label (Section 6.5.3); diagnostic labels never determine material routing (Section 2.5).

Every unit of mass is routed once: the unit-sum split routing of Theorem 8 and the column-sum-zero incidence of Theorem 9 are the mechanism, and the yield-routing obligation of Theorem 15 is its enforcement. A flux omitted from the ledger is not thereby conserved. Double counting is a representation error, and the representation that prevents it is the contribution.

**Remark 33 (One-signed bias of an aggregate overshoot date).** Let components carry biocapacity
$b_i$ and demand $d_i$, and form an aggregate overshoot date from the aggregates:
$$\tau_{\mathrm{agg}}=365\,\frac{\sum_ib_i}{\sum_id_i}=365\sum_iw_ir_i, \qquad w_i=\frac{d_i}{\sum_jd_j}, \qquad r_i=\frac{b_i}{d_i}.$$
Then $\tau_{\mathrm{agg}}$ is a demand-weighted mean of the component ratios, so
$\tau_{\mathrm{agg}}\ge\tau_{\min}:=365\min_ir_i$, with equality exactly where every component of
positive weight coincides. The difference
$$\Pi_\tau=\tau_{\mathrm{agg}}-\tau_{\min}=365\sum_iw_i\bigl(r_i-r_{\min}\bigr)$$
is the compensation premium of Section 10.1 in unit disguise: one-signed, exactly decomposable,
unbounded in the dispersion of the components, and computable from published component tables. An aggregate overshoot date is therefore optimistic in a known direction, which is a statement about the construction rather than about any territory; what this settles, and what it leaves open against the accounting standards, is taken up in the companion commentary (Abaee, 2026e). A figure can be read straight off the published component table: on the world totals of the 2025 edition of the National Footprint and Biocapacity Accounts --- the edition whose series contains that year, since the release Lin et al. (2018) document runs from 1961 to 2014 --- the 2022 aggregate ratio is $0.584$ of biocapacity to demand, so $\tau_{\mathrm{agg}} = 213$ d, and because the carbon component carries zero
biocapacity the minimum component ratio is $0$ --- hence $\Pi_\tau = 213$ d, the whole aggregate date.
Restricted to the five components of positive biocapacity with renormalised weights, the same arithmetic
gives $\tau_{\mathrm{agg}} = 538$ d against $\tau_{\min} = 365$ d, a premium of $173$ d, and the
restricted premium runs $547$ d (1961), $346$ d (1980), $251$ d (2000), $173$ d (2022): it shrinks as the
components converge, exactly as the display says it must. Which rows enter the ratio set is fixed by the accounts, not by this
construction: the Guidebook to the National Footprint and Biocapacity Accounts states that no biocapacity
figure is computed for carbon uptake, because carbon demand is charged against forest land biocapacity and a
carbon biocapacity of its own would double count it (Global Footprint Network, 2021, Section 9.1.2). The zero
row is therefore a published convention, and it is what makes $\tau_{\min} = 0$ identically, so the premium
above equals the whole aggregate date by construction rather than by dispersion. Excluding the carbon
*demand* instead is a different object --- the non-carbon components only --- on which
$\tau_{\mathrm{agg}} > 365$ d states that no included component overshoots within the year, not that no
overshoot occurs. Both figures are world totals of one data vintage: the accounts are recomputed for every
year of the series at each release, so the 2022 row of the 2025 edition (213 d) need not reproduce the date
announced for 2022 (28 July, the 209th day of that year), and that four-day difference is vintage, nowcasting and aggregation level rather than arithmetic. On the newest edition of the accounts that can be fetched without an account --- the 2018 edition, whose series ends in 2014 --- reading the publisher's world aggregate instead of summing the national rows moves that date by up to 9 d over the last decade of the release, while a whole edition step on a closed year moves it by at most 1.9 d. A difference of a few days therefore discriminates
neither the arithmetic nor the vintage on its own: the level at which the accounts are aggregated is a choice made in
reading them, and on this release it moves the date by as much as an edition step. The figures are world totals, not any territory's.

**Remark 37 (Two component ratios are identities at a world aggregate).** *On the world aggregate of the published accounts the restricted minimum $\tau_{\min}$ is 365 d in every year of the series, because the two components whose demand is the area itself --- cropland and built-up land --- have $b_i = d_i$ identically; the restricted premium is then the distance of the aggregate date past the year boundary, and its decline measures the dispersion of the three yield-based components around a level the accounts fix, not a convergence the ecosystem exhibits.* *Verification.* On the 2018 edition, $r_{\mathrm{crop}} = r_{\mathrm{built}} = 1$ exactly in 54 of 54 years and $\tau_{\min}^{\mathrm{NOC}} = 365$ d in 54 of 54; over the last decade of that series the ratio $\tau_{\mathrm{agg}}^{\mathrm{NOC}}/\tau_{\mathrm{agg}}^{\mathrm{ALL}}$ equals $1/(1-s_{\mathrm{carbon}})$ to within 4.4e-16, where $s_{\mathrm{carbon}}$ is carbon's share of demand and runs between 58.6% and 61.6%. The computation is a weighted sum of the published component rows, recorded in the supplementary (S17). *Consequence.* A premium computed at a world aggregate and a premium computed on a country's own component table are not two readings of one ecological fact, because only at the aggregate level are two of the ratios pinned by the convention that prices world demand at world-average yields; the level at which the accounts are read is part of the quantity, as Section 10.2 records.

### 10.3 Negative and boundary content is first-class

The classification results of §6.5 are negative results stated as such: the anomaly index is not a stock ratio; the reserve-life ratio is not a forecast; the removals-only time is not a depletion diagnostic. The non-reduction boundary of §9 is a rejected class of mappings—coordinate-preserving exact factors and named regular perturbations—proved from an exact same-state field gap and accompanied by separate rest-point and finite-budget incompatibilities. The sink obstructions of §2.4 are empty-kernel mechanisms. A quantity that answers exactly one question, stated with that question, **is** the framework working — and the framework's claim about itself is limited to the accounting layer it establishes.

### 10.4 Limitations

1. **(i)** The two-pool exact specialization of the groundwater template remains **open**. (ii) The phosphorus and groundwater rows are registered template obligations: no constitutive content exists behind their identification ladders. (iii) The first-passage propositions of Section 7 concern declared stochastic surrogates, not the ledger: they do not compute the ledger's hitting time, do not conserve its mass, and carry the record-relative-barrier and non-claim disciplines. (iv) The applied records of Section 6.5 are classified diagnostics at their stated evidentiary levels — statistical index, arithmetic ratio, removals-only pressure scale — and none is a calibrated early-warning system or a forecast. (v) The non-reduction boundary of Section 9 is scoped mathematics, not a gap: it rules out coordinate-preserving exact factors and the named regular perturbations between the closed primitive ledger and the open working completion; arbitrary coordinate-mixing conjugacies are a different, unaddressed question. (vi) The conditional hybrid balance of Theorem 15 stays conditional, with its jump-interpretation and yield-routing obligations open per application. (vii) The support-saturation limits of Section 2.6 are local and finite-time; neither is a full-system reduction. (viii) This paper asserts nothing empirical about any named resource system beyond the classifications of public data products stated at their source status.

---

## 11. Conclusion

The two failure modes of the introduction — compensatory aggregation and classification drift — are representation errors, and the representation that prevents them is the account's content. Conservation is proved from the incidence structure, not assumed; positivity is proved from donor limitation, not asserted; services are readouts, not mass; and depletion time is three quantities, not one. The closed finite-donor ledger carries its complete theorem set — the natural-block mass identity, orthant invariance, no interior rest at positive effort, the vanishing-extraction rest set (extinction, carrying capacity, and the frozen-biomass face), extraction integrability — and the non-reduction boundary records, with reasons, why the closed ledger and the open working systems of institutional dynamics are different completions sharing one exact object. The depletion numbers of the applied record answer, each, exactly the question their construction poses: a statistical index of record-relative stress, an arithmetic ratio of an economic classification, a pressure scale of one gross loss rate. Stating them with those questions — against the published critiques they corroborate — is what makes them usable.

This paper likewise locates substitution within the ledger, not alongside it. A substitution is a declared change to a process graph, conversion coefficient, capacity row, or return kernel; it is not the semantic act of letting one scalar component compensate for another. It can reduce ultimate loss $\ell_m$, bring late returns inside the use deadline, enlarge a shared process capacity, or shift demand to a different compartment with its own ledger entries. Those are different interventions with different stock consequences, and Definition 22's distinction between pipeline stock and never-returned material is what keeps them apart. The two questions often compressed into weak versus strong sustainability therefore remain separate at the close: Definition 21 asks whether a cycle closes stationarily at a declared state and demand, while §§3.2 and 10.1 ask whether an assessment is allowed to compensate across components. The stationary bridge connects them in one direction; it does not collapse them. The reserve classification carries the same discipline: a horizon estimate built on reserves inherits the substitution, growth, and reclassification assumptions of its scenario—exactly quantified for one canonical scenario by Proposition 28—which is why the ratio itself is read as a ratio, never as a forecast. Services—drinking water, crop yield, fish caught—are readings taken off the ledger, not substances flowing in it. For ecological-economics measurement, that is the closing statement: closure is a dynamical feasibility property, compensation is a certification choice, and the component vector is what carries the strong-assessment certificate.

---

## Data availability

The v51 reproduction package is in `paper3/latest-2026-09-19/v51/` beside this manuscript. Its `data/` directory contains (i) `usgs_mcs2026_phosphate_used.csv`, a row-by-row transcription of the USGS *Mineral Commodity Summaries* 2026 phosphate-rock production/reserve figures actually used in the table and Proposition 28, with Australia's tabulated and JORC-compliant reserve conventions kept as separate typed rows; and (ii) byte copies of the three fisheries cohort CSVs whose stored ADH values are summarised in Section 6.5.2—the archived 43-stock pull and the RAM Legacy v4.44 and v4.66 comparison cohorts—so every quoted cohort count and median is labelled by, and recomputable from, its own cohort file. The package does not re-extract or reclassify the underlying RAM Legacy database (Ricard et al., 2012; v4.66 at Zenodo 14043031); that provenance and its limits are recorded in supplementary S5. The G3P basin rows remain reported extractions from G3P v1.12 (Güntner et al., 2024; GFZ Data Services, doi:10.5880/G3P.2024.001) with the provenance and quarantine record in supplementary S5.4; the raw basin-mask extraction is not redistributed in the v51 package and no v51 script claims to re-derive it. The overshoot-date arithmetic of Section 10.2 and Remarks 33 and 37 is read from National Footprint and Biocapacity Accounts component tables as recorded in supplementary S17; those edition tables are likewise not redistributed in the v51 package. This boundary is intentional: the v51 package reproduces the arithmetic for which it contains inputs, and marks the remaining figures as cited reported extractions rather than silently promoting them to package-reproduced results. The parameter tables of Section 2 are declared parameterizations. No other data were used.

## Code availability

The v51 scripts are in `paper3/latest-2026-09-19/v51/code/`, with run instructions, dependency versions, captured outputs, and SHA-256 checksums in the package README and manifest. `curvature_and_crossover_v51.py` (Python standard library) reproduces Propositions 26–28, reads the transcribed MCS 2026 CSV, and uses the exact threshold $\eta_*=1-x/(e^x-1)$. `fisheries_cohorts_v51.py` (standard library) recomputes the three cohort counts, zero counts, and medians; checks the archived ADH formula row by row; reproduces the v4.66 taxonomic summary and archived/public identifier overlap; and evaluates the exact finite-population random-draw benchmark from the included CSVs. `persistence_index_simulation_v51.py` (NumPy; seed 7) reproduces the Gaussian exhibit now accompanying the proved Proposition 32. `certification_lp_v51.py` (NumPy, with SciPy/HiGHS when available and an exact small-instance vertex fallback) reproduces the premium/concealed-deficit exhibit and the Proposition 31 witness. No script in the v51 package re-derives the G3P basin extraction, rebuilds a RAM Legacy cohort from the source database, or recomputes the National Footprint edition tables; those exclusions are stated in the data availability statement and supplementary S9.3 rather than left to be inferred from a missing file.

## Funding

None declared.

## Declaration of competing interest

None.

---

## References

Abaee, A., 2026a. Governance delay and the stability of harvested stocks: mobilising and protective feedback rules, and the review interval as a design parameter. Zenodo. https://doi.org/10.5281/zenodo.22554217. Companion delay-dynamics study.

Abaee, A., 2026b. Periodic review as sampled governance: sample-and-hold dynamics of assessment-driven effort control, a selected 42-stock spectral screen, and the Northern Cod case. Zenodo. https://doi.org/10.5281/zenodo.22554297. Companion review-screen study.

Abaee, A., 2026c. Aggregate indices and transition safety: a quantifier-order separation between scalarized and coordinate-wise feasibility. Zenodo. https://doi.org/10.5281/zenodo.22545740. Companion assessment-separation study.

Abaee, A., 2026d. Certifying a typed ledger: the predicates, the programmes, the vintages, and the reproduction bundle. Companion methods study, submitted with this article.

Abaee, A., 2026e. What the accounts settle, and what they leave open: depletion as a cost of production, and the missing step from a rate to a horizon. Companion commentary, submitted with this article.

Ahuja, R.K., Magnanti, T.L., Orlin, J.B., 1993. Network Flows: Theory, Algorithms, and Applications. Prentice-Hall, Englewood Cliffs.

Aubin, J.-P., 1991. Viability Theory. Birkhäuser, Boston.

Baez, J., Li, X., Libkind, S., Osgood, N.D., Patterson, E., 2023. Compositional modeling with stock and flow diagrams. In: Applied Category Theory 2022. Electronic Proceedings in Theoretical Computer Science 380, 77–96. https://doi.org/10.4204/EPTCS.380.5

Blomqvist, L., Brook, B.W., Ellis, E.C., Kareiva, P.M., Nordhaus, T., Shellenberger, M., 2013. Does the shoe fit? Real versus imagined ecological footprints. PLoS Biology 11, e1001700. https://doi.org/10.1371/journal.pbio.1001700

Brunner, P.H., Rechberger, H., 2004. Practical Handbook of Material Flow Analysis. Lewis Publishers, Boca Raton.

Chhikara, R.S., Folks, J.L., 1989. The Inverse Gaussian Distribution: Theory, Methodology, and Applications. Marcel Dekker, New York.

Daly, H.E., 1990. Toward some operational principles of sustainable development. Ecological Economics 2, 1–6.
Clark, C.W., 1990. Mathematical Bioeconomics: The Optimal Management of Renewable Resources, 2nd ed. Wiley, New York.

Ekins, P., Simon, S., Deutsch, L., Folke, C., De Groot, R., 2003. A framework for the practical application of the concepts of critical natural capital and strong sustainability. Ecological Economics 44, 165–185.

Eurostat, 2001. Economy-wide Material Flow Accounts and Derived Indicators: A Methodological Guide. Eurostat, Luxembourg.

Feinberg, M., 2019. Foundations of Chemical Reaction Network Theory. Springer, Cham.

Fischer-Kowalski, M., Krausmann, F., Giljum, S., Lutter, S., Mayer, A., Bringezu, S., Moriguchi, Y., Schütz, H., Schandl, H., Weisz, H., 2011. Methodology and indicators of economy-wide material flow accounting: state of the art and reliability across sources. Journal of Industrial Ecology 15, 855–876.

Gale, D., 1957. A theorem on flows in networks. Pacific Journal of Mathematics 7, 1073–1082.

Global Footprint Network, 2021. Working Guidebook to the National Footprint and Biocapacity Accounts, 2021 edition. Global Footprint Network, Oakland, CA.

Güntner, A., Sharifi, E., Haas, J., et al., 2024. Global Gravity-based Groundwater Product (G3P), V. 1.12. GFZ Data Services. https://doi.org/10.5880/G3P.2024.001

Illakwahhi, D.T., Vegi, M.R., Srivastava, B.B.L., 2024. Phosphorus' future insecurity, the horror of depletion, and sustainability measures. International Journal of Environmental Science and Technology 21, 9265–9280. https://doi.org/10.1007/s13762-024-05664-y

Jacquez, J.A., Simon, C.P., 1993. Qualitative theory of compartmental systems. SIAM Review 35, 43–79.

Lin, D., Hanscom, L., Murthy, A., Galli, A., Evans, M., Neill, E., Mancini, M.S., Martindill, J., Medouar, F.-Z., Huang, S., Wackernagel, M., 2018. Ecological footprint accounting for countries: Updates and results of the National Footprint Accounts, 2012–2018. Resources 7, 58. https://doi.org/10.3390/resources7030058

Martinez-Alier, J., Munda, G., O'Neill, J., 1998. Weak comparability of values as a foundation for ecological economics. Ecological Economics 26, 277–286.

Meadows, D.H., Meadows, D.L., Randers, J., Behrens III, W.W., 1972. The Limits to Growth. Universe Books, New York.

Munda, G., Nardo, M., 2009. Noncompensatory/nonlinear composite indicators for ranking countries: a defensible setting. Applied Economics 41, 1513–1523.

Neumayer, E., 2013. Weak versus Strong Sustainability: Exploring the Limits of Two Opposing Paradigms, 4th ed. Edward Elgar, Cheltenham.

Øksendal, B., 2003. Stochastic Differential Equations: An Introduction with Applications, 6th ed. Springer, Berlin.

Prajna, S., Jadbabaie, A., 2004. Safety verification of hybrid systems using barrier certificates. In: Hybrid Systems: Computation and Control VII. Lecture Notes in Computer Science 2993, 477–492.

Prajna, S., Jadbabaie, A., Pappas, G.J., 2007. A framework for worst-case and stochastic safety verification using barrier certificates. IEEE Transactions on Automatic Control 52, 1415–1428.

Redner, S., 2001. A Guide to First-Passage Processes. Cambridge University Press, Cambridge.

Ricard, D., Minto, C., Jensen, O.P., Baum, J.K., 2012. Examining the knowledge base and status of commercially exploited marine species with the RAM Legacy Stock Assessment Database. Fish and Fisheries 13, 380–398.

Smith, H.L., 1995. Monotone Dynamical Systems: An Introduction to the Theory of Competitive and Cooperative Systems. Mathematical Surveys and Monographs 41. American Mathematical Society, Providence.

Tapley, B.D., Bettadpur, S., Ries, J.C., Thompson, P.F., Watkins, M.M., 2004. GRACE measurements of mass variability in the Earth system. Science 305, 503–505.

Tilton, J.E., 2003. On Borrowed Time? Assessing the Threat of Mineral Depletion. Resources for the Future, Washington, DC.

Tilton, J.E., Lagos, G., 2007. Assessing the long-run availability of copper. Resources Policy 32, 19–23.

U.S. Geological Survey, 2026. Mineral Commodity Summaries 2026: Phosphate Rock. USGS, Reston, VA. https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-phosphate.pdf

United Nations, 2025. System of National Accounts 2025. United Nations Statistics Division, New York. Endorsed by the United Nations Statistical Commission at its fifty-sixth session, March 2025. https://unstats.un.org/unsd/nationalaccount/sna2025.asp

United Nations, European Commission, International Monetary Fund, Organisation for Economic Co-operation and Development, World Bank, 2014. SEEA Central Framework: 2012 Technical Implementation. Statistical Papers, Series M No. 96. United Nations, New York.

Wackernagel, M., Beyers, B., 2019. Ecological Footprint: Managing our Biocapacity Budget. New Society Publishers, Gabriola Island, BC.

---

## Supplementary material

The accompanying supplementary file carries: the ten-state admissibility template and its three audited negative witnesses (the non-donor-limited geological exchange, the variance-closure failure, the undefined output functional); the registered identification ladders of the phosphorus and groundwater templates at full detail; the split-assignment mechanism table; the statement inventory with the status of every statement in the main text (theorem with displayed proof, conditional theorem, definition, application record, or boundary statement) — read with the S6 label rule, under which every citation is the ordered pair (kind, number); and the fisheries cohort record with the archived-pull verification and the executed broad-cohort comparison (S5); the proof obligations attached to each entry of the certification state of Section 3.1 (S7), the certificate vectors of the classified indicators (S9.1), the linear programmes of Definition 21, Theorem 24 and Proposition 30 with their input requirements and the reading rule for an infeasible programme (S8), and the worked exhibits of Sections 6.2, 6.5 and 10.1 with their reproduction record in S9.3 and the full statement inventory in S9.4; the extraction provenance of the G3P basin rows (S5.4); the
per-parameter identifiability and value records (S10, S11); the registered template detail behind Sections 8.1 and 8.2 (S14) and the discharge-label readings (S15 to S16); and the retained external recomputation record for the aggregate overshoot date reported in Remark 37, with the two editions of the accounts it reads named, licensed and hashed and its v51 non-reproduction boundary stated (S17).

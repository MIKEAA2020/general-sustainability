# Typed Flux Ledgers and Depletion Arithmetic: Conservation, Componentwise Diagnostics, and the Semantics of Depletion Horizons

## Abstract

Depletion indicators can carry similar units while built to inform distinct questions. Reserve-life ratios, trend-persistence metrics, and gross-removal pressure scales are widely interpreted as a literal “time to depletion,” despite measuring distinct physical or statistical quantities. Compounding this ambiguity, compensatory scalar aggregation routinely masks critical physical deficits behind positive aggregates.

In this paper, we resolve these confusions by constructing a typed stock–flow accounting ledger. By tracking conserved substance classes (*moieties*) independently, conservation laws remain strictly typed: biomass, financial flows, and biodiversity metrics cannot be summed into a single scalar. Mass conservation follows directly from the incidence structure of the compartment–flux network, nonnegativity is guaranteed by donor limitation (primitive outflows vanish whenever their source compartment empties), and ecosystem services are treated strictly as observable readouts rather than conserved mass.

We formalize three certification layers: a flux-reconstruction identity that recovers unobserved internal fluxes from observed stock trajectories, a conservation-law reduction, and an envelope theorem providing verifiable flux-bounding certificates. For the closed finite-donor ledger, we establish the natural-block mass identity, orthant invariance, the absence of interior rest points under positive extraction effort, a characterization of the vanishing-extraction rest set (extinction, carrying capacity, and a frozen-biomass face), and extraction integrability over finite budgets. Furthermore, we unpack “depletion time” into three mutually non-interchangeable concepts: gross turnover intensity, a frozen-rate local ratio, and a scenario-conditioned hitting time equipped with uniform-drift bounds.

We classify three widely cited public-data indicators within this taxonomy: the G3P groundwater anomaly index is shown to be a record-relative statistical metric rather than a physical stock ratio; the USGS phosphate reserve-life ratio is an arithmetic convention of an economic class rather than an exhaustion forecast; and fisheries removals-only timescales represent gross pressure scales rather than demographic depletion diagnostics. We prove that no nonnegative linear weighting can universally certify componentwise nonnegativity on arbitrary balance domains, and we establish five double-counting rules to prevent the emergence of phantom mass. Finally, we formulate first-passage semantics on declared stochastic surrogates against record-relative barriers alongside explicit non-claims. Weak and strong sustainability emerge not as competing paradigms, but as two operational regimes of a single dynamic system, governed by whether material cycles close at the rate of throughput.

**Keywords:** material flow accounting, stock–flow ledger, depletion indicators, first-passage time, conservation laws, composite indicators, reserve life.

## 1. Introduction

### 1.1 Failure Modes and the Two Confusions

Sustainability accounting consistently suffers from two structural pathologies:

1. **Compensatory Aggregation:** Heterogeneous physical stocks and service flows are compressed into scalar indices. Because cross-component substitution rates are rarely declared formally, acute physical deficits in one critical sub-system are mathematically obscured by surpluses elsewhere. While the composite-indicator and ecological economics literatures have long critiqued this flaw and proposed noncompensatory remedies (Munda & Nardo, 2009; Ekins et al., 2003; Neumayer, 2013), scalar index construction remains ubiquitous.
2. **Classification Drift:** Heterogeneous metrics with the dimension of time—reserve-life ratios, trend-persistence indicators, and removals-only pressure scales—are conflated into a single catch-all quantity: “time to depletion.” Yet, these metrics answer fundamentally different questions under incompatible boundary assumptions.

The operational reality of classification drift is striking. A reserve-life ratio simply divides an economically declared reserve by current annual production, christening the quotient a “depletion horizon.” A satellite groundwater anomaly index fits a linear trend to gravimetric anomalies, reporting the time needed to reach the historical record minimum at current rates; the result is expressed in years, yet corresponds to no physical exhaustion event. A fisheries pressure scale scales a logarithmic biomass margin by instantaneous fishing mortality, presenting a gross clearance timescale as if it were a demographic extinction date. Each metric provides specific institutional or descriptive information; none represents what is popularly claimed.

The primary manifestation of compensatory aggregation is exemplified by public awareness metrics such as *Earth Overshoot Day*. By collapsing ecological footprints and biocapacities into a single annual calendar date, a catastrophic deficit in an irreplaceable sub-component can easily coexist with an aggregate overshoot date that falls comfortably late in the calendar year (Lin et al., 2018; Wackernagel & Beyers, 2019; Blomqvist et al., 2013). Systems-dynamics models encounter identical aggregation ambiguities when multidimensional state spaces are collapsed into scalar stress variables (Meadows et al., 1972). The framework developed here is component-resolved by construction: depletion horizons are defined and tracked per asset and per pool, completely precluding cross-component summation into a scalar date.

Beyond these accounting failures lies a deeper dynamical failure mode: the **productivity illusion**. This is the deceptive phenomenon in which an extractive system appears fully functional while the underlying support base sustaining its throughput is liquidated silently.

It has two senses, and they are distinct. The first is arithmetic and is the compensatory-aggregation failure above — a deficit in one component offset by a surplus in another, so that a positive aggregate reads as adequate. This article formalises this sense as the aggregation obstruction of Section 10.1. The second sense is dynamical and is yield inflation. A measured yield can exceed the true sustainable yield when it is maintained by drawing down the support pool — groundwater, soil carbon, bioavailable nutrients — rather than by that pool's regeneration. The resource appears productive while what sustains it is liquidated silently.

* This is simply compensatory aggregation in disguise—a deficit in an unmonitored capital stock is mathematically masked by current consumption flows. We formalize this limitation as an aggregation obstruction in Section 10.1.
* Here, harvest or extraction yield remains high because the system draws down an unmodeled support pool—such as fossil groundwater, soil organic matter, or parent mineral deposits—rather than operating within the regenerative flux of that pool. The resource appears highly productive precisely because its natural foundation is being liquidated.

The support pool need not be an absolute, non-renewable geological stock. Whether framed as natural capital, an abiotic storage compartment, or a slowly replenishing ecosystem service, the governing physics remains identical. Every such pool regenerates over some characteristic timescale: an agricultural crop regenerates seasonally, an alluvial aquifer over decades or centuries, and mineral deposits over geological epochs.

The viability of the system depends strictly on the rate of extraction relative to the rate of regeneration:

$$\text{Extraction sustained by regeneration} \implies \text{Sustainable Throughput}$$

$$\text{Extraction exceeding regeneration} \implies \text{Stock Liquidation}$$

A drawdown is recoverable if and only if the rate of harvest drops below the rate of replenishment before structural collapse occurs. The physical size of a reserve determines its absolute capacity; whether an ongoing extraction pattern represents sustainable harvest or irreversible liquidation depends entirely on the flow rates.

Dynamically, yield inflation mimics an overloaded mechanical structure. An elevator engineered for ten passengers can readily hold fourteen: the cable does not snap immediately upon loading the fourteenth person. Rather, it accumulates unseen microscopic strain. To the passengers, the ride feels normal until the threshold of tensile failure is breached, at which point catastrophe is instantaneous. Yield inflation corresponds to this silent wear phase: observable extraction rates remain stable, giving no hint of the drawdown occurring beneath the surface.

Our two-pool architecture is engineered specifically to capture this wear phase—making resource liquidation measurable while the supporting structure is still functional, rather than attempting to forecast the precise moment of failure.

Classification drift on the empirical side is equally well-documented. A reserve-life ratio ($\text{Reserves}/\text{Production}$) is purely arithmetic. Because an economic “reserve” is defined by extraction technology, market prices, exploration budgets, and legal permissions, it does not represent an immutable physical inventory. It replenishes dynamically through new discoveries and shifting economics. This issue has been demonstrated for phosphate rock by Illakwahhi, Vegi, and Srivastava (2024), who showed that widely publicized claims of global phosphorus exhaustion within a century stem from an uncritical reading of single-source U.S. Geological Survey (USGS) data. Such projections disregard industrial recycling, price feedbacks, and technological substitution. In mineral economics, this distinction between reserves (economic inventories) and resources (crustal abundance) has been recognized since Tilton (2003). For example, United States phosphate reserves have remained stable near $1.0\times 10^6\text{ kt}$ for decades despite cumulative extraction exceeding $6.0\times 10^5\text{ kt}$ over the same period. Copper demonstrates an identical dynamic: global reserves have increased over a century of exponential extraction (Tilton & Lagos, 2007).

Similar ambiguities plague material flow accounting (MFA; Brunner & Rechberger, 2004; Eurostat, 2001; Fischer-Kowalski et al., 2011). While MFA shares its incidence structure with chemical reaction network theory (Feinberg, 2019), practitioners frequently conflate four distinct operational properties:

1. **Bookkeeping balance** (mass accounting),
2. **Stoichiometric conservation** (reaction invariants),
3. **Thermodynamic admissibility** (nonnegative entropy production),
4. **Barrier safety** (maintenance of state variables within viability sets).

A perfectly balanced mass ledger can be chemically absurd; a chemically consistent network may violate all declared ecological safety barriers; and a trajectory satisfying every environmental constraint may violate basic conservation laws through phantom mass injections. Disentangling these layers and establishing their formal relations is the first primary objective of this work (Section 3).

Our second objective is to enforce **noncompensation**. Ecological economics asserts the *weak comparability of values*, maintaining that multi-criteria environmental decisions cannot be collapsed into a single metric without arbitrary value judgments (Martinez-Alier, Munda, & O'Neill, 1998). At the level of physical accounting, this thesis takes an exact algebraic form (Section 10.1): *no nonnegative linear weighting of balance vectors can certify that every underlying physical stock remains above its minimum critical threshold*. A positive weighted sum can never prove componentwise nonnegativity. Scalar indices are suitable for high-level communication and rough ranking; physical certification requires evaluating the full vector.

Our third objective is to integrate **technological substitution** directly into the ledger’s internal architecture, rather than treating it as an exogenous correction. We formalize weak and strong sustainability not as irreconcilable ethical doctrines, but as two distinct operating regimes of a single dynamic system:

* **Weak Sustainability Regime:** Extractive throughput and population demands are small enough relative to technological substitution and natural biogeochemical cycling that material loops can close at the rate of extraction. The dominant stabilizing term over human horizons is technical substitution, with deep-time geological regeneration treated as a slow boundary condition (Daly, 1990). In this regime, metabolic byproducts—atmospheric carbon, agricultural runoff, mineral processing tailings—are returned to productive reuse fast enough that they never accumulate as unmanageable sinks. Here, "waste" is not an inherent property of a material, but an operational condition: matter that currently cannot be reused due to constraints in technology, economics, or logistical capacity.
* **Strong Sustainability Regime:** The material loop fails to close at the required throughput rate, either because no physical recycling pathway exists or because industrial extraction outpaces technological implementation (Neumayer, 2013; Ekins et al., 2003). In this regime, substitution is physically admissible only when explicit stoichiometric mechanisms route matter through viable regenerative channels without depleting adjacent critical stocks. Substitution cannot be assumed via smooth Cobb–Douglas production elasticity; it requires physical mass pathways.

These two regimes reflect two distinct mathematical views of the same ledger:

* **The Aggregate Scalar View ($B = b \cdot M$):** Here, $b$ is the specific replenishment rate and $M$ is total natural mass. This view evaluates whether the system balances in aggregate—the central criterion of weak sustainability.
* **The Componentwise Vector View:** This perspective assesses whether closing one balance requires the catastrophic liquidation of an unmonitored donor compartment or the overfilling of a waste sink.

Both views are indispensable. The componentwise ledger maintains stocks as first-class physical entities and tracks the hitting times and sink boundaries that constrain the aggregate throughput $B$. The scalar check provides an instantaneous operational measure of overshoot. However, both are strictly instantaneous tests; neither can guarantee that a balanced state will persist without drifting into overshoot over time.

To quantify this drift, we construct scenario-conditioned hitting times (Section 6.5.2). When applied to economic reserves, these hitting times capture the institutional assumptions embedded within reserve classifications, converting static ratios into rigorous diagnostics.

### 1.2 Contributions

1. **A Typed Primitive-Flux Ledger:** We formalize physical compartments by assigning each a material identity, spatial boundary, and physical unit. Compartments are linked via a signed incidence matrix driven by nonnegative primitive fluxes, synthesizing the accounting discipline of MFA (Brunner & Rechberger, 2004) with the algebraic formalism of reaction network theory (Feinberg, 2019). Type conversions require explicit stoichiometric coefficients, and all unilateral mass transfers are strictly donor-limited.
2. **Separation of Three Certification Layers:** We mathematically separate and prove the relationships between:
   * *Accounting consistency* (local preservation of balance equations),
   * *Conservation consistency* (invariance of declared moieties modulo boundary flows), and
   * *Barrier safety* (confinement of stocks within declared upper and lower limits).

   We prove an algebraic flux-reconstruction identity, a conservation-law reduction theorem, and an envelope theorem providing bounding certificates for state-dependent fluxes.

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
7. **Coupling Interface with Institutional Delay Dynamics:** We define the shared mathematical boundary between our mass-conserved ledger and institutional harvest models via the decline-pressure identity $qEN - R = -\dot{N}$. We prove a non-reduction theorem demonstrating why closed mass-conserving ledgers cannot be reduced to open, delay-driven institutional systems.

#### What Is Explicitly Not Claimed

* We make **no claim of a stochastic completion** for the full ledger: the surrogate processes in Section 7 do not conserve mass and are not stochastic perturbations of the underlying vector field.
* We make **no claim of thermodynamic completeness**: energy balances, chemical affinities, and entropy production are not formalized here.
* We make **no claim that the groundwater two-pool model is empirically identified**: the observational data required to resolve fast and slow groundwater storage are outlined as open requirements in Section 8.2.
* We make **no empirical forecasts** regarding specific aquifers, phosphate reserves, or marine fisheries beyond the descriptive classifications derived from published data.

### 1.3 Organization

Section 2 formulates the typed ledger, its constitutive laws, and its limiting properties. Section 3 formalizes the three certification layers and proves the core accounting theorems. Section 4 establishes the theorem set for the closed finite-donor ledger. Section 5 constructs the service readout layer and defines the componentwise deficit. Section 6 develops depletion arithmetic, proves the uniform-drift brackets, and classifies empirical indicators. Section 7 details first-passage semantics and its analytical boundaries. Section 8 details domain templates for phosphorus, groundwater, and bioeconomic harvesting. Section 9 proves the non-reduction interface with institutional delay models. Section 10 outlines analytical boundaries, the failure of weighted aggregation, and double-counting safeguards. Section 11 concludes.

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
| $b$ | boundary-transfer term; service balance $b_i$ (subscripted); specific regeneration rate (local to §1.1) | Lemma 3, Proposition 4, Theorem 5; §5.1; §1.1 |
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
where $S_{\mathcal{T}}$ is the typed stoichiometric (incidence) operator, $y$ collects the declared boundary states — environmental or companion variables external to the ledger — $\theta$ the declared constitutive parameter vector, $B_{\mathcal{T}} u_{\partial}$ collects declared boundary transfers, and $d_x$ belongs to a stated disturbance class. Entries are added within a row only when their types and units agree. That sentence presumes a
declaration, and the declaration is Definition 47: types, units and conversion coefficients are declared with
the ledger, and $S_{\mathcal{T}}$ carries the subscript for that reason. If $L^\top S_{\mathcal{T}} = 0$, then
$$\frac{d}{dt}(L^\top x) = L^\top B_{\mathcal{T}} u_{\partial} + L^\top d_x,$$
one conservation law per conserved moiety and boundary; the identity does not create a scalar
sustainability mass across incommensurable systems, and Proposition 42 states exactly in what sense it cannot. Three things are then proved, in full, inside the article. First, $d_x$ must itself be typed: a physical disturbance on represented material is a different object from a structural discrepancy term. The sign pattern of the incidence matrix and the non-negativity of the primitives are separate declarations. 3. Every primitive outflow must vanish or be limited when its donor compartment is empty, and a target-relaxation flux from a finite donor is admissible **only after** donor limitation is made explicit.

**Definition 21 (Closure cone).** The regimes above can be stated on the ledger's own objects rather
than as attitudes toward them. Let $S_{\mathcal{T}}$ be the incidence operator declared here, let $v\ge0$
be the primitive fluxes under declared capacities $\bar v$, let $B_Tu_\partial$ collect the
declared boundary transfers, and let $P$ project a flux vector onto its use columns. Write
$\mathcal K=\{v\ge0:\ S_Tv+B_Tu_\partial=0,\ v\le\bar v\}$ for the admissible stationary flux
patterns. A demanded use vector $D$ closes at the rate of use if and only if
$D\in P(\mathcal K)$. The closure capacity
$\Lambda^{*}=\max\{\mu:\ \mu D\in P(\mathcal K)\}$ is a linear programme on the declared
capacities, and its feasibility is the cut condition on return capacity (Gale, 1957; Ahuja et al.,
1993). Where $\Lambda^{*}\ge1$, the cycle closes at the demanded rate. Where $\Lambda^{*}<1$,
every trajectory meeting $D$ has a non-stationary stock, and by conservation the shortfall appears
as support drawdown together with sink accumulation; the deficit share is not a free parameter. Yield
inflation is the same statement read outside the projection: demand met with no stationary pattern
behind it.

Left-null vectors express conservation; right-null vectors express circulation. The regimes of
Section 1.1 are statements about the second set, and the depletion readouts of Section 6 are
statements about the first; neither set's membership follows from the other's.

**Definition 22 (Closure deficit at the use timescale).** For each moiety $m$, let
$\kappa_m(\tau;\Theta)\in[0,1]$ be the fraction of mobilised flux returned to a usable compartment
within lag $\tau$ under the declared technology and process graph $\Theta$, and let
$\delta_m=1-\kappa_m(\tau_{\mathrm{use}};\Theta)$ be the closure deficit at the declared use
timescale. The deficit is a property of a declared graph at a declared timescale, not a rate of the
material itself. Where a mobilisation $g_m$ is sustained with $\delta_m\ge\underline\delta>0$,
the net drawdown of the support pool is $\delta_mg_m$, so
$$\int_0^T(\text{liquidation})\,dt\ \ge\ \underline\delta\int_0^Tg_m\,dt, \qquad T\ \le\ \frac{m_0}{\underline\delta\,g_m},$$
the second inequality being the frozen-rate horizon read on the liquidation flux rather than on gross
use. Both bounds are one-sided by construction, and neither reverses in the limit
$\delta_m\to0^+$. A positive deficit is not a barrier-reachability claim: a deficit that decays
with the stock need never reach a barrier, and where the binding constraint is an upper barrier the
relevant object is the complementary headroom.

Two readings follow from the definition. An indicator that reports a return fraction with no lag
argument reports $\kappa_m(\infty)$ where $\kappa_m(\tau_{\mathrm{use}})$ is being read; the
recycled-input and circularity-rate families are of that form, because a ratio of fluxes carries no
timescale. And "a material is waste" is, on this reading, the statement
$\kappa_m(\tau_{\mathrm{use}};\Theta)<1$ for the declared graph, so unlocking a stream is an
increase of $\kappa$ at fixed $\tau$: measurable, and not in need of a new substance category.

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

**The split-assignment evidence requirement.** Where an application splits extraction between standing-stock removal and recruitment suppression — $C_{\mathrm{stock}} = \psi qEN$ and $C_{\mathrm{recruit}} = (1-\psi)qEN$ for $\psi \in [0,1]$ — the assignment requires evidence per channel. The dominant physical mechanism sets it, never a diagnostic label. Illustrative assignments through a logistic two-channel proxy (stated as illustrative, calibrated examples, not constitutive claims for the named domains): soil zinc under crop export, an existing-unit removal, at $\psi = 0.85$, against impaired mineralisation, a replenishment degradation, at $\psi = 0.25$; pollinators under adult mortality at $\psi = 0.70$ against brood failure at $\psi = 0.20$ — and across such mechanism pairs the trough depth varies by a factor of about $1.5$ from mechanism alone. **The mass-routing discipline** is the same typing made explicit. Literally harvesting pre-recruit stages *is* a harvest of existing units, and routes to the product and waste fractions. 2. Habitat-induced failed recruitment is a **prevented inflow** — routing it into product or waste would create mass that was never in the stock. Damage to the capital stock itself — aquifer compaction, severe soil loss — is not a split-assignment channel at all.

### 2.6 Support saturation and the logistic limit

Two results control what the ledger's stock equation becomes when its support pool saturates. Both are singular reductions with explicit scope, and neither is a full-system reduction.

**Theorem 1 (Support-saturated logistic stock limit).**
*Fix $T < \infty$ and non-negative parameters $\mu, \delta, c, q$. For $\kappa > 0$, assume:*

*(H1) $A_\kappa$ is measurable with $A_\kappa(t) \ge a_0 > 0$ and $0 \le X_\kappa(t) \le X_{\max}$.*

*(H2) Common effort $E \in L^\infty([0,T])$.*

*and let $X_0$ solve the limiting equation with the same initial value. Then $\sup_{t \le T} |X_\kappa(t) - X_0(t)| = O(\kappa)$; if $\mu > \delta$ and $c > 0$ the limit is $\dot X_0 = rX_0(1 - X_0/K_{\log}) - qE(t)X_0$ with $r = \mu - \delta$ and $K_{\log} = (\mu - \delta)/c$.*

*Proof.* Write $e(t) = |X_\kappa(t) - X_0(t)|$. The saturation defect satisfies
$$\left| \frac{A_\kappa}{\kappa + A_\kappa} - 1 \right| = \frac{\kappa}{\kappa + A_\kappa} \le \frac{\kappa}{a_0},$$
so the vector-field defect obeys
$$|\dot X_\kappa - \dot X_0| \le L_1 \kappa + L_2 e(t), \qquad L_1 = \frac{\mu X_{\max}}{a_0}, \qquad L_2 = \mu + \delta + 2cX_{\max} + q\|E\|_\infty,$$
using $|\mu - \delta| \le \mu + \delta$ and $c(X_\kappa + X_0) \le 2cX_{\max}$. Gronwall's inequality with the Lipschitz constant $L_2$ and the particular-term scale $L_1$ gives $e(t) \le (L_1/L_2)\kappa\,(e^{L_2 t} - 1) \le C_T \kappa$ on $[0,T]$. The bound $0 \le X_\kappa \le X_{\max}$ is satisfiable in the registered family: under $\mu > \delta$ the comparison $\dot X_\kappa \le X_\kappa(\mu - \delta - cX_\kappa)$ keeps $X_\kappa \le \max\{X(0), (\mu-\delta)/c\}$, so $X_{\max} = \max\{X(0), K_{\log}\}$ suffices. The limiting equation is $\dot X_0 = \mu X_0 - \delta X_0 - cX_0^2 - qE X_0$, i.e. $\dot X_0 = (\mu - \delta)X_0 (1 - X_0/K_{\log}) - qE X_0$ with $K_{\log} = (\mu - \delta)/c$. □

**Remark 2 (Registered-family support-saturated identity).**
*In the primitive-flux core with $g(X,A) = \mu XA/(K_A + A)$, $m(X) = dX + cX^2$, $h(X,E) = qEX$, the support-saturated stock equation is, for each fixed interior $A > 0$ in the limit $K_A \to 0$,*
$$\dot X = (\mu - d)X - cX^2 - qEX = rX\left(1 - \frac{X}{K}\right) - qEX, \qquad r = \mu - d, \quad K = \frac{\mu - d}{c},$$
*requiring $\mu > d$ and $c > 0$. The identity is pointwise on the interior support region and not uniform through the depleted-pool boundary: for every $K_A > 0$, $A/(K_A + A) = 0$ at $A = 0$.*

*Proof.* At fixed $A > 0$, $A/(K_A + A) \to 1$ as $K_A \to 0$, so $g \to \mu X$ pointwise and $g - m \to (\mu - d)X - cX^2$; the algebraic reduction to the logistic form with $r = \mu - d$, $K = (\mu - d)/c$ is immediate. The non-uniformity statement is the identity $A/(K_A + A) = 0$ at $A = 0$ for every $K_A > 0$, which the pointwise limit does not touch. The scope is restricted: the limit does not eliminate the detritus compartment $U$, does not make $A$ constant near its boundary, and does not transform the memory or effort laws — an ecological stock-equation identity, not a full-system reduction and not a transfer principle for bifurcation thresholds. In the correspondence, the logistic law of (2) is this saturated, mortality-folded readout of the Theorem 1 and Remark 2 family — not the vector field of the closed four-tuple of Section 2.2 — and bifurcation numbers of the two families do not transfer between them. □

Substituting it for the underlying stock-support dynamics is legitimate only where the support pool is at interior saturation, and only on the timescales over which the saturated approximation holds.

---

## 3. Certification Layers and the Accounting Theorems

### 3.1 Three predicates, separated

The four predicates of Section 1.1 — bookkeeping balance, stoichiometric conservation, thermodynamic admissibility, and sustainability safety — are this section's working layer: it separates the first, second, and fourth and proves their relationships (the third, thermodynamic admissibility, is out of scope here, per Proposition 2's layering), for the reasons Section 1.1 states — a point at which the Daly/Ayres tradition of throughput accounting meets the formalism of reaction-network theory (Feinberg, 2019; Brunner and Rechberger, 2004).

The ledger supports three distinct predicates that are related but not identical.

**Layer 1: Accounting consistency.** The balance law (1) holds almost everywhere on $[0,T]$.

**Layer 2: Conservation consistency.** $\ell^\top S_{\mathcal{T}} = 0$ for every declared conserved quantity $\ell$.

**Layer 3: Barrier safety.** For declared lower and upper barriers $\underline{B}_m(t) \le S_m(t) \le \overline{B}_m(t)$ for every component $m$ and every $t \in [0,T]$, where $S = Cx$ is the moiety-composition readout.

Layer 2 is a structural predicate on the incidence operator alone. Layers 1 and 3 are properties of a trajectory triple $(x, v, b)$. The logical relations between them are the content of the next two propositions. (Numbering: the two layering propositions of this section carry their own counter, Propositions 1–2. Every other numbered statement runs on one sequence shared by definitions, lemmas, propositions, theorems, corollaries and remarks, so each number belongs to exactly one statement and the kind name says which; the sequence reaches 47, and its maxima are Definition 47, Lemma 4, Proposition 43, Theorem 24 and Remark 37. The supplementary’s statement inventory reconciles its status words with these labels in S6.

**Proposition 1.** *Conservation consistency implies accounting consistency for the conserved quantities: if $\ell^\top S_{\mathcal{T}} = 0$, then $\frac{d}{dt}(\ell^\top x) = \ell^\top b$, and in a closed system ($b = 0$), $\ell^\top x$ is invariant.*

*Proof.* $\frac{d}{dt}(\ell^\top x) = \ell^\top \dot x = \ell^\top(S_{\mathcal{T}} v + b) = (\ell^\top S_{\mathcal{T}}) v + \ell^\top b = \ell^\top b$. □

**Proposition 2.** *Barrier safety does not follow from accounting consistency: a trajectory can be perfectly mass-balanced while violating a declared barrier; and a trajectory can satisfy declared barriers while violating a conservation law or a stoichiometric constraint. Conversely, thermodynamic admissibility (energy conservation, entropy-production nonnegativity, reaction feasibility) implies accounting consistency, but the converse does not hold; this paper establishes Layers 1–3 only.*

*Proof.* First clause: on the closed ledger (2), constant extraction at a rate exceeding regeneration — a comparison flux, not a donor-limited primitive of the ledger's own discipline — is exactly mass-balanced (Theorem 7 states the identity) and drives the living stock through any positive lower barrier in finite time; likewise the trajectory with $N \equiv 0$ (extinction rest of Section 4.6) is mass-balanced yet violates any positive lower barrier on $N$. Conversely, a trajectory satisfying the barriers may be generated by fluxes that fail a stoichiometric constraint — mass balance does not certify that the flux decomposition is physically realizable — or by bookkeeping that silently drops a moiety through the yield-routing violation of rule (iii) in Section 10.2, failing conservation without touching the barriers. Second clause: thermodynamic admissibility presupposes a mass balance, but a mass-balanced flux decomposition need not satisfy energy or entropy constraints; establishing those requires structure outside the present scope. □

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
the implications that hold among them are the ones stated in Propositions 1 and 2 and in the
thermodynamic clause of Section 3.2, and an unlisted implication is not available by inference. The
proof obligation attached to each entry, and the certificate vectors of the indicators classified in
Section 6.5, are tabulated in the supplementary material.

### 3.2 The typed safety set

The typed safety set at time $t$ is
$$\mathcal{K}(t) = \{ x \ge 0 : \underline{B}(t) \le Cx \le \overline{B}(t) \},$$
and the non-compensatory assessment reads
$$\mathcal{V}_{\mathrm{typed}} = \{ x(\cdot) : x(t) \in \mathcal{K}(t)\ \forall t \in [0,T] \}.$$
This is a conjunctive criterion: all moiety barriers must be satisfied simultaneously, and no weighted aggregate $\sum_m w_m S_m$ is used as the decision criterion. The force of that conjunction is the subject of §10.1.

### 3.3 The flux-reconstruction identity

**Lemma 3 (Flux reconstruction under a typed balance law).**
*Let $x : [0,T] \to \mathbb{R}_+^n$ be absolutely continuous with $\dot x(t) = S_{\mathcal{T}} v(t) + b(t)$ almost everywhere, $v \in L^1([0,T]; \mathbb{R}_+^J)$, $b \in L^1([0,T]; \mathbb{R}^n)$, and $S = Cx$ with $C \in \mathbb{R}^{M \times n}$ the moiety-composition matrix. Then*
$$S(t) = S(0) + \int_0^t \bigl( C S_{\mathcal{T}} v(\tau) + Cb(\tau) \bigr) d\tau,$$
*and for continuous barriers $\underline{B}, \overline{B}$ the trajectory satisfies $\underline{B}_m(t) \le S_m(t) \le \overline{B}_m(t)$ for all $t \in [0,T]$ if and only if the corresponding integrated inequalities hold for all $t \in [0,T]$.*

*Proof.* Integrate $\dot S = C\dot x = C(S_{\mathcal{T}} v + b) = C S_{\mathcal{T}} v + Cb$ from $0$ to $t$; this is valid because $x$ is absolutely continuous and $C$ linear. The barrier equivalence follows because $S_m$ is continuous (as $x$ is absolutely continuous) and the barriers are continuous, so a pointwise inequality violation is an integrated-inequality violation at the same time. □

- **Prescribed or observed fluxes.** If $v(t)$ and $b(t)$ are known and integrable, stock balances are reconstructed by integration without solving the internal constitutive dynamics. In both cases the barriers are declared, not computed: the flux data do not compute ecological threshold values, aquifer collapse thresholds, or concentration boundaries — the theorem establishes trajectory compliance with declared barriers, not derivation of the barriers themselves.

With $h_m(t) \ge 0$ the net outflow of moiety $m$ across the system boundary and $r_m(t) \ge 0$ the net inflow, the sign convention reads
$$S_m(t) = S_m(0) + \int_0^t \bigl( r_m(\tau) - h_m(\tau) \bigr) d\tau,$$
and the barrier-safety (non-depletion) condition is
$$S_m(0) + \int_0^t \bigl( r_m(\tau) - h_m(\tau) \bigr) d\tau \ge \underline{B}_m(t).$$

### 3.4 The conservation-law reduction

**Proposition 4 (Conservation-law reduction).** *If $\ell^\top S_{\mathcal{T}} = 0$ for some vector $\ell \in \mathbb{R}^n$, then*
$$\ell^\top x(t) = \ell^\top x(0) + \int_0^t \ell^\top b(\tau) d\tau;$$
*in a closed system ($b = 0$), $\ell^\top x$ is invariant.*

*Proof.* This is Proposition 1 integrated: $\frac{d}{dt}(\ell^\top x) = \ell^\top b$; integrate. □

A conserved moiety is a row $c_m^\top$ of $C$ with $c_m^\top S_{\mathcal{T}} = 0$; then $S_m = c_m^\top x$ satisfies $\dot S_m = c_m^\top b$. In a closed system $S_m$ is constant, and in an open system $S_m$ changes only through boundary flows. Conservation does not imply barrier safety: if a closed conserved moiety has fixed total stock $S_m(t) = S_m(0)$, a time-varying barrier can become infeasible solely because the barrier moves. The three objects are distinct: the conservation invariant ($S_m$ constant), the barrier tube ($\underline{B}_m \le S_m \le \overline{B}_m$), and the intersection of the invariant manifold with the barrier tube. A conservation law alone does not imply that the trajectory satisfies the barrier. The precise sense is linear: the set $\{x \ge 0 : \ell^\top x = \ell^\top x(0),\ \underline{B} \le Cx \le \overline{B}\}$ may be empty even though each of the three objects is separately well-defined. Barrier–conservation compatibility is a linear feasibility programme, not a slogan.

**Definition 23 (Bounded residual).** Conservation consistency is stated with a declared residual
budget. For every left-null vector $\ell$ of $S_{\mathcal{T}}$, with $C$ the moiety-composition matrix of Section 2.1 (Lemma 3),
$$\Bigl|\int_0^T\ell^{\top}C\,d_x(t)\,dt\Bigr|\ \le\ \epsilon_\ell(T), \qquad \epsilon_\ell\ \text{declared with the model}.$$
Proposition 1 then reads $\ell^{\top}Cx(T)=\ell^{\top}Cx(0)+\int_0^T\ell^{\top}C\,b(t)\,dt$ with
the disturbance term carried rather than absorbed, and $\epsilon_\ell$ is the quantity
material-flow reconciliation books as statistical discrepancy. An envelope computed without
$\epsilon_\ell$ supports no barrier certificate once the residual-inflated envelope leaves the
declared barriers, and where $\epsilon_\ell$ is undeclared the conservation predicate is reported
as not established rather than assumed at zero. Where no budget is declared for $d_x$, the
residual is not established at zero and is not bounded: the predicate carries the gap rather than
closing it.

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

*Proof.* By Lemma 3, $\dot S_m = (C S_{\mathcal{T}} v + Cb)_m$. For each row $m$ and time $\tau$, the bilinear form $(C S_{\mathcal{T}})_m v$ is linear in $v$ with coefficient vector $(C S_{\mathcal{T}})_m$, whose positive and negative parts give, over the box $[\underline{v}(\tau), \overline{v}(\tau)]$, the pointwise bounds
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
$\lambda\ge0$ satisfies $\lambda^{\top}GS_T+c^{\top}\le0$ componentwise, with $\lambda_j$
carrying the units that convert margin $j$ into cumulative service. Then $V=\lambda^{\top}m(x)$
obeys $\dot V\le-y+\lambda^{\top}Gb$ along every admissible trajectory, and for every trajectory
that remains inside the declared barriers
$$\int_0^Ty(t)\,dt\ \le\ V(x(0))+\int_0^T\lambda^{\top}Gb(t)\,dt .$$
If additionally $y\ge y_{\mathrm{req}}$ and $\lambda^{\top}Gb\le\beta<y_{\mathrm{req}}$, then
$T\le V(x(0))/(y_{\mathrm{req}}-\beta)$.

*Proof.* $\dot V=\lambda^{\top}G(S_Tv+b)=(\lambda^{\top}GS_T)v+\lambda^{\top}Gb\le
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

**Definition 34 (Composition of typed ledgers).** Let $L_1 = (x^1, v^1, S_1, B_1, C_1)$ and
$L_2 = (x^2, v^2, S_2, B_2, C_2)$ be ledgers over disjoint compartment sets, and let an *interface*
$\Theta = (J, \Phi, \bar v)$ consist of a finite set $J$ of declared identifications pairing a
compartment of $L_1$ with a compartment of $L_2$, a finite set $\Phi$ of declared exchange fluxes
with boxes $0 \le f_\varphi \le \bar v_\varphi$, and, for each $\varphi$, the two endpoints it drains
and fills. The composition $L_1 \oplus_\Theta L_2$ is the ledger on the quotient compartment set
(disjoint union modulo $J$) whose incidence is the block-diagonal $\mathrm{diag}(S_1, S_2)$ extended
by the identification rows and by the endpoint columns of $\Phi$, with readouts carried over unchanged
on each side. The composition is *admissible* when three conditions hold on the declared data:

1. Like with like: every identification pairs compartments of the same material type and the same
 unit, and the *interface defect*
 $d_\Theta = \sum_{(a,b) \in J} \bigl[\,\mathbf 1\{\mathrm{type}(a) \ne \mathrm{type}(b)\} +
   \mathbf 1\{\mathrm{unit}(a) \ne \mathrm{unit}(b)\}\bigr]$ vanishes;
2. Joint boxes declared: no capacity constrains fluxes of both ledgers unless that sharing is one of
 the declared objects, in which case the shared box is a constraint of the composition and not of
 either part;
3. Antisymmetry: each exchange enters one ledger as an outflow and the other as an inflow of the same
 magnitude, $\textstyle\sum_{i} B_i\, e_\varphi = 0$ on the identified compartments.

The admissible compositions are exactly those for which the flux polytope of the whole is the fibre
product of the parts' polytopes over the interface coordinates. The defect and the antisymmetry
residual are computed from the declaration, not assumed away; a composition with $d_\Theta > 0$ is not
a ledger, and no statement below applies to it.

**Definition 35 (Interface price).** Suppose each part is certified as in Theorem 24, with multiplier
$\lambda_i \ge 0$, margins $m_i(x^i) = G_i x^i + a_i$, and readout $y_i = c_i^{\top} v^i$. For a
declared exchange $\varphi$ draining compartment $c$ on the paying side, its *price* is
\[
\pi_\varphi = \bigl(\lambda_1^{\top} G_1\bigr)_c - \bigl(\lambda_2^{\top} G_2\bigr)_c ,
\]
evaluated at the identified compartments. A price is margin consumed (positive) or margin released (negative) per unit of interface flux per
unit of time, *in the declared orientation*: what the composition must budget for is the magnitude
$|\pi_\varphi|\,\bar v_\varphi T$, and the sign only decides which side pays. Reversing an exchange's
declared direction leaves that magnitude unchanged and moves the charge to the partner ledger, so no claim
of a free interface can rest on the sign of $\pi_\varphi$ alone. The additivity of these charges is
asserted for a two-part composition; a composition of three or more parts sharing a compartment needs a
declared global interface, because a flux the whole admits need not decompose into part-wise admissible
exchanges, and two parts each delivering into a third attain service their summed budgets do not cover.

The two ways of reading the display above are different constructions, and the distinction is
load-bearing, so both are given. *Rows.* Take the disjoint union, keep every declared coordinate, and add the
equalities $x_a^1 = x_b^2$ for each $(a,b) \in J$ as constraint rows; capacities stay attached to the flux
columns. *Quotient.* Let $R$ be the class-incidence matrix of the equivalence relation generated by $J$, with
$R_{Ca} = 1$ exactly when $a \in C$, and set $x_C = R x_0$, $S_C = R\,[\,\mathrm{diag}(S_1, S_2)\ \ E\,]$,
$B_C = R B_0$, where an exchange $\varphi$ draining $a$ and filling $b$ enters as the column
$E_\varphi = -e_a + e_b$, and the classes are read off by connected components. The row form is the one this
article uses, because the certificates are stated on the declared coordinates and because the row form stays
meaningful when the interface defect of condition 1 fails; the quotient form is meaningful only when types and
units agree \emph{throughout} each class, not pair by pair, and then the two coincide on the feasible
flux set. Condition 1's $\mathrm{type}(\cdot)$ is $\mathrm{ty}$ of Definition 47, which is what makes the
agreement check decidable from the declaration. Neither construction carries certificates across on its own:
the descent of a part's conservation law to the composition is exactly the agreement condition of
Proposition 36, and it can fail.

**Proposition 36 (Conservation composes; closure does not).** Let $\Theta$ be admissible. The conserved quantities of the composition are exactly the pairs of part-wise left-null vectors that
agree on every identified compartment: such a pair lifts to a conservation of the whole, and every
conservation of the whole arises that way. The lift is injective and need not be onto, so a conserved total
of a part can be destroyed by an identification the typing permits. Closure of
the cycle at a demanded rate does not compose: the closure capacity of the composition can be strictly
below the minimum of the parts' closure capacities. Instance: two cycles, each with demand $1$ unit
per year and return capacity exactly $1$ unit per year, each therefore closing tightly at $\Lambda^{*} = 1$; when the two return fluxes draw on a single declared capacity of $1.5$ units per year, the composition has $\Lambda^{*} = 0.75$ and closure deficit $0.25$. Every trajectory of the
composition meeting the demanded rate then has non-stationary stock, so by Definition 22 the shortfall
appears as support drawdown together with sink accumulation, at a rate the linear programme fixes.

*Proof.* The identification rows are the only further constraints, so a covector is left-null on the
quotient precisely when its pullback is left-null on each part and constant on each identification class;
the pullback is therefore injective, with image the compatible subspace, and it is not onto. Witness: two
compartments in series in each part carry two moieties, and after the admissible identification of the two
middle compartments the quotient carries one, so the moiety of the first part is gone. Which subspace
survives is a rank computation on the declared data --- with $D_J$ the matrix of merged-compartment rows,
the surviving conserved covectors are $(U_1 \oplus U_2) \cap \ker D_J^{\top}$ --- the same computation
that decides closure. For the instance, the composition's programme is $\max \mu$ subject to $q = \mu$, $s = \mu$, $q + s \le 1.5$
with $q, s \ge 0$, whose optimum is $\mu = 0.75$; the parts' programmes are $q \le 1$ and $s \le
1$, both with optimum $1$. □

**Proposition 37 (Margin needed, and the admissible exchange rate).** Let $\Theta$ be admissible and
let each part satisfy Theorem 24 with budget $B_i = V_i(x^i(0)) + \int_0^T \lambda_i^{\top} G_i
b_i\,dt$. Then the composition satisfies the same bound for the summed service $y_1 + y_2$ with budget
\[
B_1 + B_2 + \sum_{\varphi \in \Phi} |\pi_\varphi|\, \bar v_\varphi\, T .
\]
The sum is the *margin needed* to absorb the interface; the parts' budgets add without remainder
exactly when every declared interface either releases margin on the side that carries the budget or is
slack at its declared bound. Under the outflow-negative convention of Definition 35 the sharper charge
$(-\pi_\varphi)^{+}\bar v_\varphi T$ applies and the interface is free when $\pi_\varphi \ge 0$.
With a single exchange of box $[0, L]$, non-zero price $\pi$ and horizon $T$, this multiplier pair
certifies the composition whenever
\[
L \;\le\; L_{\max} := \frac{B_1 + B_2}{|\pi|\, T},
\]
and at $L = L_{\max}$ the interface charge equals the combined budget by construction. The converse is not
claimed: another multiplier pair can certify a rate this one does not, and the exact threshold for the
declared horizons is the value of the joint programme over the fibre product of the two declared polytopes
--- not the scalars $\lambda_i$, $G_i$, $\pi$ quoted here, which do not determine it on their own.
Instance: $G_1 = G_2 = 1$, $b_1 = b_2 = 0$, $\lambda_1 = 1$, $\lambda_2 = 2$, so $\pi = -1$ and the
exchange drains the ledger holding the cheaper margin; with $B_1 + B_2 = 9$ units of margin and $T = 30$
yr, $L_{\max} = 0.30$ unit per year --- an exchange at $0.2$ stays inside the combined budget ($6 \le 9$)
and one at $0.5$ does not ($15 > 9$). Interchanging the two multipliers leaves the magnitude unchanged and
moves the charge to the other ledger.

*Proof.* Take $V = V_1 + V_2$. Along the composition, $\dot V \le -(y_1 + y_2) + \lambda_1^{\top} G_1 b_1 + \lambda_2^{\top}
G_2 b_2 - \sum_\varphi \pi_\varphi f_\varphi$: the exchange terms are the only ones that do not
decouple, because a flux that leaves margin in one part enters it in the other at the partner's
multiplier. Each interface term is then bounded over its box by its worst case,
$\max_{0 \le f \le \bar v_\varphi}(-\pi_\varphi f) = (-\pi_\varphi)^{+}\bar v_\varphi \le
|\pi_\varphi|\bar v_\varphi$, and integrating with $V(T) \ge 0$ gives the stated budget. The
one-dimensional case is the equality $L|\pi|T = B_1 + B_2$ solved for $L$. □

**Definition 40 (Compensation as a decidable predicate).** Fix a partition of the declared
compartments into donor and recipient sides, a demanded service rate, and the joint polytope of the
composition. *Compensation holds at fraction $\kappa$* when one linear programme on that polytope is
feasible: maximise the recipient's sink-weighted margin release net of the donor's, subject to the joint
polytope, to the demanded service, and to the donor's budgets being drawn at no more than $\kappa$ times
what its own service costs; the predicate is true when the optimum covers the demanded drawdown. It is a
feasibility test on the fibre product rather than a price comparison, and it is the exact form of the
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
enters Definition 34's budgets and never its admissibility conditions.

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
quoted, and here it does not: Definition 34's three conditions involve no multiplier, and
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
**Definition 45 (Latest safe intervention time).** Let a critical support pool have margin
$m_0 = A_0 - A_{\min} > 0$ over its declared barrier and net drawdown $d_0 > 0$, so $\dot A = -d$.
Let $\tau$ be the declared unavoidable delay before drawdown can begin to fall, and let $\rho > 0$ be the
declared maximum rate of that fall, with the reaching of $d = 0$ declared achievable. The *latest safe
intervention time* is the largest further postponement that still admits a service-preserving transition:
$$t_{\mathrm{last}} \;=\; \sup\Bigl\{\, L \;:\; m_0 \;\ge\; \inf_{d(\cdot)} \int_0^{\,\tau+L+d_0/\rho} \!\! d(t)\,dt
\;\text{over}\; d \equiv d_0 \;\text{on}\; [0,\tau],\ \dot d \ge -\rho,\ d \ge 0 \Bigr\} .$$
It is a feasibility deadline, not a forecast: the quantifier order is "there exists one response, and every
declared disturbance is then respected", not "every disturbance has some response of its own", and the inner
infimum prices the best admissible response rather than an expected one.

**Proposition 41 (The deadline has a closed form, and it is not the horizon).** Under the declaration of
Definition 45 the least attainable additional loss is
$$m_{\mathrm{needed}} \;=\; d_0\tau + \frac{d_0^{2}}{2\rho} ,$$
a transition respecting $A \ge A_{\min}$ exists exactly when $m_0 \ge m_{\mathrm{needed}}$, and
$$t_{\mathrm{last}} \;=\; \frac{m_0}{d_0} - \tau - \frac{d_0}{2\rho} \;=\; H^{\mathrm{loc}} - \tau - \frac{d_0}{2\rho} ,$$
with $H^{\mathrm{loc}} = m_0/d_0$ the frozen-rate ratio of Proposition 26, read on the support pool in
the manner of Definition 22. The two objects differ by the
physical cost of delay and of finite deployment speed, so $t_{\mathrm{last}} < H^{\mathrm{loc}}$ whenever
$\tau$ and $\rho$ are finite, and the gap is not a discount applied to the horizon but a different
quantifier over the same declaration. Where $t_{\mathrm{last}} < 0$ the pool can lie above its barrier,
every trajectory inside the declared corridor, while the service-preserving transition is already
infeasible --- which is the case a horizon cannot express.
Illustration, declared as illustrative and not empirical: $m_0 = 100$ units, $d_0 = 10$ units per year,
$\tau = 2$ yr, $\rho = 1$ unit per year per year gives $H^{\mathrm{loc}} = 10$ yr and $m_{\mathrm{needed}} = 70$,
so ten years of coverage leaves three years to begin: $t_{\mathrm{last}} = 10 - 2 - 5 = 3$ yr. With
$m_0 = 25$, $d_0 = 4$, $\tau = 3$ yr and $\rho = 0.5$ the horizon reads $6.25$ yr while
$t_{\mathrm{last}} = -0.75$ yr. Replacing $H^{\mathrm{loc}}$ by the true horizon $T$ is a step Proposition 26
licenses in direction only: where the depletion law is nondecreasing in the stock, $T \ge H^{\mathrm{loc}}$
and the deadline moves later, never earlier, while the two ramp terms are untouched; the closed form above is
then the conservative side of the substituted expression, and no equality is claimed for it.

*Proof.* The integrand $d$ is non-negative and the constraint set is lower-bounded in slope, so the loss is
minimised by letting $d$ fall as early and as fast as it is allowed to: any postponement of the ramp adds
area and nothing else. On $[0, \tau]$ the drawdown is held at $d_0$, contributing $d_0 \tau$; the ramp from
$d_0$ to $0$ at slope $-\rho$ lasts $d_0/\rho$ and contributes the triangle $\tfrac{1}{2} d_0^{2}/\rho$.
Adding gives $m_{\mathrm{needed}}$; the equivalence is the definition of the supremum; and solving
$d_0(\tau + L) + d_0^2/(2\rho) = m_0$ for $L$ gives the stated $t_{\mathrm{last}}$. □

**Definition 46 (Supportable-output envelope).** For a declared ledger, barrier family and horizon,
$$\mathcal Y(T) \;=\; \bigl\{\, y \ge 0 \;:\; \exists\ \text{an admissible trajectory on } [0,T]
\ \text{with service at least } y \ \text{throughout and } x(t) \in \mathcal K(t) \ \forall t \bigr\}$$
is the set of service rates supportable for the whole horizon. Three readings and no fourth. The set is
decreasing in $T$ by restriction, so an envelope number is always a pair (rate, horizon). A single quoted
rate is a selection from the set, and Proposition 29 says which selections can be certified aggregators;
the envelope itself is the report. And at the frozen-rate corner the first empty horizon is the
$T = m_0/(\underline\delta g_m)$ of Definition 22, so a published "years of supply" measures the declared
drawdown path together with the barrier, never the stock alone: it is an envelope statement, and a
sustained deficit below the declared $\underline\delta$ moves it without moving the stock.

**Remark 35 (What a non-displacement gate can say on this apparatus).** An additionality or
non-displacement claim is a comparison of two declarations, not a forecast of a counterfactual world: on this
apparatus the intervention is non-displacing at the declared timescale when the closure deficit of
Definition 22, evaluated on the composition of the project block with the host ledger, is not below the
deficit of the host ledger alone. The gate is then checkable from the declarations, and it fails in the
ordinary way --- a project that re-labels an existing mobilisation as its own leaves the composed deficit
where it was, and a predicate on deficits reports that, where a predicate on attributions would not. What
the gate cannot say is carried by its baseline: the host ledger is declared, not estimated, and where the
two declarations share a compartment the deficit is read on the quotient, so it is not the sum of the two
deficits --- Proposition 36's warning about conserved quantities applies to deficits as well.
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
coefficients*, each an ordered triple $(\alpha, \beta, c)$ with $\alpha$ and $\beta$ distinct types and
$c > 0$, attached to a named conversion process and read as "one unit of $\beta$ is obtained from $c$ units of
$\alpha$ by that process". Nothing in this list is derived from the stoichiometry; all of it is declared
alongside it.

Admissibility then has content. A sum $\sum_{i \in I} x_i$ is admissible as one ledger quantity only when
$\mathrm{ty}_i$ and $\mathrm{un}_i$ agree for every $i \in I$; across types there is no sum, only a conversion,
and a conversion appears as a signed pair of entries in the column of the primitive flux that performs it. A
primitive flux is *typed-admissible* when its column is of exactly one of two kinds: a *transfer*, all of whose
nonzero entries are $\pm 1$ among compartments of one type and one unit; or a *conversion*, whose entries on
the two compartments it joins are $-c$ and $+1$ for a declared $(\alpha, \beta, c) \in \mathsf{Cv}$; and no
column is both. Where the declaration draws no type distinction beyond units, every column is a transfer and
the predicate is reported as not applicable, not as passed. Changing $\mathsf{Ty}$, $\mathrm{ty}$ or
$\mathsf{Cv}$ is a change of ledger and not a change of notation: the admissible flux set $\mathcal{K}$ of
Definition 21 is defined through $S_{\mathcal{T}}$, so it moves with the declaration, and every certificate
built on $\mathcal{K}$ moves with it.

**Proposition 42 (No conservation law crosses a type class).** *Form the graph on $\mathsf{Ty}$ in which two
types are joined when $\mathsf{Cv}$ declares a conversion between them, and call the pullback of a connected
component a type class. Then no admissible column of $S_{\mathcal{T}}$ has nonzero entries in two distinct
classes, and for a permutation of rows and columns*
$$S_{\mathcal{T}} \;=\; \bigoplus_{\gamma} S_{\gamma}, \qquad \ker S_{\mathcal{T}}^{\top} \;=\;
\bigoplus_{\gamma} \ker S_{\gamma}^{\top} .$$
*Every conservation law of the ledger is therefore carried by a single class; no conserved quantity of the
ledger prices one class against another; and an aggregate formed by adding across classes is not a consequence
of equation (1) but an additional declaration, admitted or refused on Definition 23's terms and propagating
through the certificates exactly as Proposition 36 describes.*

*Proof.* A transfer column meets one type, hence one class. A conversion column meets two types joined by a
declared coefficient, hence one class. So every admissible column has support inside a single class, which is
block-diagonality of $S_{\mathcal{T}}$ once rows are grouped by class; a vector $L$ satisfies
$L^{\top} S_{\mathcal{T}} = 0$ if and only if its restriction to each block does, which is the splitting in the
display. The final clause is read off that splitting: a left-null vector is a tuple of left-null vectors, so
nothing in the kernel relates one block to another. □

**Remark 36 (What the type structure yields, and what it does not).** Three consequences are worth separating,
because the literature runs them together. *Reporting boundaries.* Since the classes are built from the
declared conversions, drawing a reporting boundary differently --- merging two type names into one report
label, or splitting one --- cannot change $\ker S_{\mathcal{T}}^{\top}$ unless it declares or withdraws a
conversion. That is the invariance the composition calculus is sometimes asked to supply, with the hypothesis
that makes it true and with the boundary of its scope: redrawing *inside* a class is a different act, decided
by Proposition 36's compatibility condition and not by this one. *Valuation.* The predicate is a
well-posedness condition on declarations, not a thesis about worth. It says that a ledger which has added a
gigajoule to an hour of labour has not declared what it did; it says nothing about whether the two are
comparable in worth. A material-and-energy-value position stated as a substantive claim about worth is
therefore not a corollary of this apparatus, and this paper does not make it: what is available here is the
position's checkable content --- Definition 47's predicate, and Proposition 29's aggregator, which does not
compensate a deficit in one compartment with a surplus in another. *Reclassification.* A reserve class
entering or leaving an asset boundary is not a change of $\mathsf{Cv}$ but a boundary transfer, and it is
priced by Definition 22's closure deficit with its declared elasticity, not by the typing predicate. The
statistical standards recalled in Section 1.2 draw their own asset boundary in economic terms of exactly that
kind, so the exposure is common to the frameworks rather than peculiar to this one, and it is a reason the
horizon readouts of Section 6 are stated with their deficit attached.

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
Every column is a two-compartment transfer under the unit-sum routing constraints, so $\mathbf{1}^\top S_{\mathcal{T}} = 0$ column by column — Theorem 8's conservation, at sight — and the natural-block rows $(N, U, A^{\mathrm{act}}, A^{\mathrm{geo}})$ reproduce the four-row display of Section 2.2, with the harvest column now carrying its full routing ($\alpha$ to $U$, $1-\alpha$ to $P$) instead of the block-export convention of the $\alpha = 0$ corner. The natural-block rows $(N,U,A_{\mathrm{act}},A_{\mathrm{geo}})$ reproduce the four-row display of §2.2, with the harvest column now carrying its full routing ($\alpha$ to $U$, $1-\alpha$ to $P$) instead of the block-export convention of the $\alpha=0$ corner. The retirement split $(\rho_P, 1-\rho_P)$ and the inert-bound source (the absorbing stock $W$) are declared routing choices of this displayed instance; the incidence pattern — every primitive a two-compartment transfer, column sums zero — is the theorem's content, and no classification depends on the declared choices.

### 4.3 Conservation of the six-compartment ledger

**Theorem 9 (Six-compartment conservation).** *For the system of Section 2.3, $\frac{d}{dt}\mathbf{1}^\top z = 0$; the total mass $M_6 = X + U + A + G + P + W$ is constant along every trajectory on which the classical solution is defined.*

*Proof.* With $M_6 = \mathbf{1}^\top z$, $\dot M_6 = \mathbf{1}^\top S(\alpha,\rho) v = 0$ because each column of $S$ sums to zero; term by term: assimilation gives $g - g = 0$; mortality gives $-m + m = 0$; decomposition gives $-d_U + d_U = 0$; geological exchange gives $e_{GA} - e_{GA} = 0$ and $-e_{AG} + e_{AG} = 0$; mining gives $-c_G + c_G = 0$; and the remaining harvest and retirement terms satisfy $-h + \alpha h + (1-\alpha)h = 0$ and $\rho_P r_P - r_P + (1-\rho_P)r_P = 0$. □

Two scope notes are part of the theorem. The conservation argument applies to the *expanded typed incidence system* when quality grades are split — not automatically to an undifferentiated quality-neutral loop. And open systems are explicit: imports, exports, atmospheric losses and cross-boundary transport enter as typed boundary fluxes, giving $\dot M_6=I_\partial-O_\partial$. Theorems 7–9 are three instances of the conservation lemma of Proposition 1. Theorems 7–9 are three instances of the conservation lemma of Proposition 1 — each is the identity $\frac{d}{dt}(\ell^\top x) = \ell^\top b$ for a declared ledger and boundary with $\ell = \mathbf{1}$ — differentiated only by which compartments the declaration include

### 4.4 Orthant invariance

**Theorem 10 (Orthant invariance of the closed ledger).** *The nonnegative orthant in $(N, A^{\mathrm{act}}, A^{\mathrm{geo}}, U)$ is forward invariant for the closed natural block (2).*

*Proof.* The right-hand side is locally Lipschitz on a neighbourhood of the closed orthant: each Michaelis–Menten factor $s$, $\sigma$ is $C^\infty$ on the nonnegative half-line because the registered regime keeps $A_0 > 0$ and $A_{g0} > 0$. Face by face. On $A^{\mathrm{geo}} = 0$ one has $\sigma = 0$, hence $e_{GA} = 0$ and $\dot A^{\mathrm{geo}} = e_{AG} = \omega_A A^{\mathrm{act}} \ge 0$. On $A^{\mathrm{act}} = 0$ one has $s = 0$, so $R = B = T = e_{AG} = 0$ and $\dot A^{\mathrm{act}} = e_{GA} + \gamma_U U \ge 0$. On $N = 0$, extraction and uptake vanish and $\dot N = 0$. On $U = 0$, $\dot U = T \ge 0$. Nagumo's inward-pointing criterion (Aubin, 1991) yields forward invariance of the orthant. □

**Theorem 11 (Forward invariance of the six-compartment cone).** *Under the donor boundary assumptions of Section 2.3 (each primitive flux vanishes when its donor is empty, fluxes continuous in effort and locally Lipschitz in the state), $\mathbb{R}^6_+$ is forward invariant for the six-compartment system.*

*Proof.* Face by face: at $X = 0$, $g = m = h = 0$ so $\dot X = 0$; at $U = 0$, $\dot U = m + \alpha h + \rho_P r_P \ge 0$; at $A = 0$, $\dot A = -g + d_U + e_{GA} - e_{AG} = d_U + e_{GA} \ge 0$, the two negative terms vanishing by donor limitation ($A$ is the donor of both $g$ and $e_{AG}$); at $G = 0$, $\dot G = e_{AG} \ge 0$; at $P = 0$, $\dot P = (1-\alpha)h + c_G \ge 0$; at $W = 0$, $\dot W = (1-\rho_P)r_P \ge 0$. The vector field belongs to the tangent cone at every boundary point, and the tangent-cone invariance theorem applies. Conservation and boundary admissibility are separate obligations, and the finite-donor condition carries a discipline: a target-relaxation law $e_{GA} = \omega(A^{\mathrm{eq}} - A)$ does not satisfy it unless also limited by $G$; it may be used only with the source declared an effectively infinite external reservoir, in which case the system is open rather than closed. □

The classical lineage of these statements is the compartmental-systems non-negativity theory (Jacquez and Simon, 1993).

### 4.5 No interior rest at positive effort

**Theorem 12 (No interior rest at positive effort).** *Assume (H1) $E\equiv E^*>0$ is constant.

*(H1) $E \equiv E_* > 0$ is constant.*

*Then a rest point of the closed natural block satisfies $R + C^{A,\mathrm{lim}} = 0$ after restoring optional mining; with $C^A = 0$ this is $R = 0$, hence $N = 0$ or $N = K$ or $A^{\mathrm{act}} = 0$. None of these is compatible with $E_* > 0$ and $N_* > 0$: (i) $N = K$ and $E_* > 0$ give $\dot N = -qE_* K < 0$; (ii) $A^{\mathrm{act}} = 0$ and $A^{\mathrm{geo}} > 0$ give $\dot A^{\mathrm{act}} = \omega_A A^{\mathrm{eq,intrinsic}} \sigma > 0$; (iii) $N = 0$ forces $R = T = 0$ and reduces to the extinction family $\mathcal{R}_{\mathrm{ext}}$ of Theorem 13. In particular the working point $(N^*, A^{\mathrm{act}*}) = (89.526, 397.87)$ is not a rest point at $E = E^* \approx 2.090$: $\dot N = 0$ holds there by construction ($R^* = qE^*N^* \approx 0.187 > 0$), and the rest condition of the proof below fails on the abiotic pair.*

*Proof.* At a rest point, $\dot U = 0$ forces $\gamma_U U = T$. Adding $\dot A^{\mathrm{act}} + \dot A^{\mathrm{geo}}$ gives $-B + \gamma_U U - C^{A,\mathrm{lim}} = 0$; with $\gamma_U U = T$ and $B = R + T$ this is $R + C^{A,\mathrm{lim}} = 0$. With mining declared ($C^A > 0$) this forces $R \le 0$; with $C^A = 0$ it is $R = 0$, and from the constitutive law $R = rN(1 - N/K)s = 0$ implies $N = 0$ or $N = K$ or $s = 0$ (that is, $A^{\mathrm{act}} = 0$). Cases (i)–(iii) exclude each branch at positive effort; in the mining case the contradiction is more direct — $\dot N = 0$ with $E_* > 0$ and $N_* > 0$ gives $R = qE_*N_* > 0$, while the abiotic rest condition gives $R = -C^{A,\mathrm{lim}} \le 0$. At the working point $\dot N = 0$ by construction while rest would require $R = 0$; with $\dot U = 0$ the abiotic pair would satisfy $\dot A^{\mathrm{act}} + \dot A^{\mathrm{geo}} = -R < 0$. □

### 4.6 The extinction–geochemical rest set

**Theorem 13 (Vanishing-extraction rest set).** *With vanishing extraction ($E \equiv 0$), the rest points of the closed natural block (2) are exactly the three sets — the extinction family $\mathcal{R}_{\mathrm{ext}}$, the carrying-capacity family $\mathcal{R}_K$, and the frozen-biomass face $\mathcal{R}_{\mathrm{frozen}}$; the union symbol $\mathcal{R}_0 = \mathcal{R}_{\mathrm{ext}} \cup \mathcal{R}_K$ is retained for the two geochemical families:*
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

**The closed-ledger portrait.** Theorems 7–14 assemble into a complete qualitative portrait of the closed orthant: conservation (Theorems 7–9), positivity (Theorems 10–11), no interior rest at positive effort (Theorem 12), the two-family vanishing-extraction rest set with the frozen-biomass face (Theorem 13), and the finite donor budget (Theorem 14). The portrait is the source object handed to the interface of §9: the closed system's candidate long-time set is the rest set of Theorem 13, and the budget of Theorem 14 bounds how long any positive-flux configuration can persist. For industrial-ecology measurement the message is direct: a "balanced" closed ledger is a finite-budget object, and any sustained extraction against it must integrate to a quantity no greater than the initial budget.

---

## 5. Service Readouts and the Componentwise Deficit

Services are observations or feasible outputs of the physical state, not additional conserved mass. Internal physical transfers are not services merely because they appear in a ledger. This distinction is the accounting counterpart of the ecological-economics point that a service flow — Ayres' useful-work reading, Daly's throughput-of-services reading — is not the same object as the mass that delivers it.

### 5.1 The service readout and the contemporaneous balance

For services indexed by $i = 1, \ldots, n$, write $s_i(t) = \mathcal{O}_i(x(t), u(t), \theta)$, where $u$ denotes admissible operating or extraction choices and $s_i$ and the demand $d_i$ share service-specific units. Where delivered services are selected or converted ledger fluxes, the readout is linear in the primitives,
$$s = \mathcal{O}(x, u, \theta) = Q(\theta)\, v(x, u),$$
with every row of $Q$ declaring the delivery boundary and the conversion into one service-specific unit; more general state-dependent readouts are possible. The contemporaneous component balance is
$$b_i(t) = s_i(t) - d_i(t),$$
and $b_i(t) \ge 0$ means measured supply meets measured demand for component $i$ at that instant. A stock can meet current demand while declining toward a threshold, and a stock below a desired level can have a positive current balance while recovering.

### 5.2 The state-dependent feasible balance domain

**Definition 1 (Feasible balance domain).** *For an admissible operating set $\mathcal{U}(x,t)$ and a declared demand set $\mathcal{D}(t)$,*
$$\mathcal{B}(x,t) = \{ \mathcal{O}(x,u,\theta) - d : u \in \mathcal{U}(x,t),\ d \in \mathcal{D}(t) \}.$$

The geometry of the balance domain is state dependent and inherited partly from the stock–flow model; no unrestricted argument can replace an application-specific analysis of $\mathcal{B}(x,t)$. The geometry of the balance domain is state dependent and inherited partly from the stock–flow model. **No unrestricted argument can replace an application-specific analysis of $\mathcal B(x,t)$.** This domain is the object against which any scalar certificate claim must be checked (§10.1): a weighted sum certifies componentwise non-negativity on $\mathcal B(x,t)$ only through an implication proved from the physical restrictions that define the domain.

### 5.3 Support provenance and the directional support gap

Current service adequacy and regenerative feasibility are different claims. Let $\Gamma_{\mathrm{all}}(x,t) \subseteq \mathbb{R}^n_+$ contain the service vectors feasible through all pathways admitted by an application, and $\Gamma_{\mathrm{reg}}(x,t) \subseteq \Gamma_{\mathrm{all}}(x,t)$ the feasible set after imposing the declared regenerative-flow, system-boundary, material-quality, and exergy or capacity restrictions. These correspondences are application inputs obtained from a typed pathway or technology model; the stock ledger alone does not construct them.

**Definition 2 (Directional regenerative-support fraction and gap).** *Assume (H1) $0\in\Gamma_{\mathrm{reg}}(x,t)$; (H2) a nonzero service direction $\bar s\ge0$ is chosen.

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

the memory input of the institutional dynamics is a smoothed stock-decline rate, exactly the positive part of the decline. It is not a stock-level scarcity measure, not an unmet-consumption measure, and not an independently observed service deficit. Since $qEN-R(N,A_{\mathrm{act}})=O(N)$ as $N\to0$, the raw decline input vanishes near extinction while the positive baseline source of the effort law can still sustain commanded effort.

**Proposition 25 (Accumulated liquidation certified by delivered service).** Let the support pool
obey $\dot A=r-c$, and let the declared production relation require at least $\alpha\ge0$ units
of support use per unit of delivered service, $c(t)\ge\alpha Y(t)$. Then
$$A(0)-A(T)\ \ge\ \alpha\int_0^TY(t)\,dt-\int_0^Tr(t)\,dt .$$
Where the right-hand side is positive, the delivered service certifies that much support liquidation,
whatever the interior allocation of fluxes.

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

*Proof.* Nondecreasing $\varphi$ gives $\varphi(A)\ge\varphi(A_0)$ for $A\le A_0$, hence
$T\ge(A_0-A_{\min})/\varphi(A_0)$; the second case reverses the inequality. The comparison is the
standard one for one-dimensional monotone dynamics (Smith, 1995). □

Proportional extraction is the first case, with $T=q^{-1}\ln(A_0/A_{\min})$ against
$H^{\mathrm{loc}}=(A_0-A_{\min})/(qA_0)$; at $A_{\min}=0$ the two disagree by being infinite
against finite. The sign is estimable from the data the classification already requires, by
regressing the decline rate on the stock; it is declared, not computed, in Section 6.5.

**Proposition 27 (Curvature correction).** On the barrier distance $u=A-A_{\min}$, let
$\dot u=-\varphi(u)$ and define the dimensionless curvature number
$$\kappa=\frac{u\,\ddot u}{\dot u^{2}}=\frac{u\,\varphi'(u)}{\varphi(u)} .$$
For the power-law family $\varphi(u)=cu^{p}$ one has $\kappa=p$ identically, and for $\kappa<1$
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

**Proposition 28 (Reserve-life crossover).** Let reserves obey $\dot R=-(1-\eta)P$, with
production $P=P_0e^{gt}$, $g>0$, and let $\tau=R_0/P_0$ be the reserve-life ratio. Exhaustion of
the reserve class occurs at
$$T=\frac1g\ln\Bigl(1+\frac{g\tau}{1-\eta}\Bigr),$$
and $T\ge\tau$ holds to first order in $g\tau$ exactly when $\eta\ge\tfrac12g\tau$. A
reserve-life ratio therefore bounds the reserve class from above only where reclassification keeps
pace with growth. On the article's own pinned record, $\tau\approx309$ yr at
$g=0.03\,\mathrm{yr}^{-1}$, the condition requires $\eta\ge\tfrac12g\tau\approx4.6$, which
exceeds unity: reclassification would have to outpace extraction itself, and no declared reserve
convention admits that. At $\eta=0$ the same record gives $T=g^{-1}\ln(1+g\tau)\approx77.6$ yr
against the tabulated 309. The direction of the error is therefore fixed by the model class rather
than by the data, and the classification of Section 6.5 is strengthened, not changed: the ratio
remains an arithmetic relation whose promotion to a forecast is unavailable at every admissible
elasticity.

*Proof.* Integrate $\dot R=-(1-\eta)P_0e^{gt}$ to $R(T)=0$ and solve; the comparison with $\tau$
is the first-order expansion $\ln(1+x)=x-x^2/2+O(x^3)$ at $x=g\tau/(1-\eta)$. □

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

Component-resolved depletion horizons on public data products are tabulated below, computed without fitting any dynamical parameter of the reduced systems. Rows marked with a dagger (†) are quarantined and must not be taken at face value: the Australia phosphate row dates to a pre-2026 reserve vintage (§6.5.3), and the Indo-Gangetic groundwater magnitude sits an order of magnitude beyond published basin-mean trends (the quarantine note below).

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

| Country | Reserves (kt) | Reserve-life horizon (yr) | Implied production (kt/yr) |
|---|---|---|---|
| China | $3{,}400{,}000$ | $\approx 28$ | $121{,}429$ |
| United States | $1{,}000{,}000$ | $\approx 45$ | $22{,}222$ |
| Jordan | $820{,}000$ | $\approx 62$ | $13{,}226$ |
| Morocco | $50{,}000{,}000$ | $\approx 1{,}250$ | $40{,}000$ |
| Australia† | $5{,}800{,}000$ | $\approx 2{,}088$ | $2{,}778$ |
| World (reserves) | $74{,}000{,}000$ | $\approx 309$ | $239{,}482$ |
| World (resources, $\varepsilon = 0.10$) | $>300{,}000{,}000$ | $>1{,}125$ | $240{,}000$ |

under current fishing mortality $F$, with median **≈ 1.8 yr** across the **43** assessed stocks with finite spawning-stock-biomass (SSB) and $F$ series — the archived pull, kept in place as the headline cohort by the recorded data-vintage decision — computed with $\mathrm{ADH}=0$ entered for the **eight** stocks already at or below the reference: the zero convention of the source table's caption, **which the median includes**. The archived 43-stock cohort is reproduced by **neither** public RAM Legacy release — S5's version-sensitivity record, cross-referenced here, is the retraction and the row-by-row re-verification — and the v4.66 public-release broad-cohort reading (454 stocks, median 3.39 yr) is the primary public-release comparison, executed in S5 and detailed below. The qualifying positive sub-cohort ($F > 0$ and $\mathrm{SSB}_{\mathrm{now}} > B_{\lim}$; 35 stocks) has median $2.9$ yr; both medians come from the archived pull alone. The cohort is a selected class, not a random sample of assessed stocks: all 43 stocks are small pelagics (18 anchovy, 20 herring, 4 sprat, 1 sardine), the fast-maturing class the companion review screen (Abaee, 2026b, doi:10.5281/zenodo.22554297) selects by its annual-review eligibility criterion (42 of the 43 are that screen's annual-managed spectral-null stocks, per the source caption). The $\approx 1.8$ yr median is therefore a class-specific diagnostic for fast-maturing, annually managed pelagics, not a statistic of assessed fisheries in general; the executed broad-cohort comparison (S5) runs the same protocol on the full public release — 454 stocks, median $3.39$ yr, the upper end carried by the long-lived groups (elasmobranchs $11.5$, sebastids $9.0$, pleuronectids $6.0$ yr) — and only $2\%$ of random 43-stock draws from that broad cohort have medians at or below the class cohort's $1.79$ yr.

The extract is the RAM Legacy cohort of Ricard et al. (2012) at release v4.66 (Zenodo 14043031,
6 November 2024), recorded as the cohort file of the supplementary's S5 record; its vintage is verified from
the extract's own contents, four of six published $F$ values reproducing that release exactly, and the pull
has been re-verified row by row against the formula — all 43 rows reproduce $\mathrm{ADH} = \max(0,\, F^{-1}\log(\mathrm{SSB}/B_{\lim}))$ with $B_{\lim} = 0.2 \max \mathrm{SSB}$. The value is reported with its cohort conditions and is not promoted to a forecast. Because cohort composition is database-version-dependent, every cohort statistic is pinned to the archived pull: the quartile summary of $F$ and $\log(\mathrm{SSB}/B_{\lim})$ over the cohort belongs to that pull alone, and no cohort statistic is quoted from a different database version. The cohort protocol is fully specified in the accompanying supplementary material (S5) — including the zero entries for stocks at or below the reference, which enter the median — together with the version-sensitivity record: on the public RAM Legacy releases the same protocol qualifies **415** stocks (v4.44, median **2.57** yr) and **454** (v4.66, median **3.39** yr) — both reproduced to printed precision under the recovered micro-specification (S5) — **neither reproducing the archived 43-stock cohort**: the archived pull's 43-stock list and extract-time series state — supplied and re-verified — differ from both public releases.

**The scope discipline is the tables' load-bearing content.** None of the reported numbers is a computed instance of any model's first-hitting time. They are descriptive, component-resolved diagnostics in the two-pool logic of the taxonomy — not dynamical predictions. The equal-weight inverse-horizon score of the four basins still above their window minimum and world phosphate reserves, displayed as **Non-example 1** — a deliberate boundary of aggregation, not a score of the framework,
$$\Sigma_{\mathrm{reserves}} \approx \frac{1}{5}\left( \frac{1}{2.7} + \frac{1}{7.9} + \frac{1}{9.5} + \frac{1}{21.4} + \frac{1}{309} \right) \approx 0.130\ \mathrm{yr}^{-1},$$
is a ranking device, not a componentwise certificate: it mixes basins and reserves, incommensurable objects under the type structure of Definition 47, and is retained only to mark the boundary of legitimate aggregation. It is exhibited as the worked instance of the non-compensation boundary of §10.1: a positive aggregate coexisting with componentwise deficits by construction — admissible as communication, **inadmissible as certification**.

#### 6.5.3 The phosphate reserve-life ratio

The phosphate column of the classification matrix is the reserve-life ratio. at approximately 74,000,000 kt (74,000 Mt) of world reserves and 240,000 kt/yr of production (U.S. Geological Survey, 2026) this is approximately **309 years**. It is **not a physical exhaustion forecast**, because reserve classification changes with prices, technology, exploration and regulation — the point made independently, and forcefully, by Illakwahhi, Vegi and Srivastava (2024) for the single-source USGS data behind the influential phosphate depletion estimates, and standard in mineral economics, where reserves have grown through a century of rising production for copper (Tilton, 2003; Tilton and Lagos, 2007). The reserves/resources split discipline is part of the classification: a resource-threshold calculation $T_{\mathrm{resource},10\%} = 0.9\, G_{\mathrm{resource}}/C_G$ answers a different question and must not share a column with the reserve-life ratio without an explicit convention label; the reserve classification is economic — US reserves have stayed near $1{,}000{,}000$ kt while cumulative production since 1996 is of order $600{,}000$ kt — and the resource-based world horizon ($\approx 1{,}125$ yr at $\varepsilon = 0.10$) is more than three times the reserve-based figure ($\approx 309$ yr); the two-compartment split is what prevents these from being collapsed into one number. **The vintage is pinned once.** The single pinned source of record is the *Mineral Commodity Summaries* (MCS) 2026 (U.S. Geological Survey, 2026), and every figure this paper quotes at pin status is that vintage's — the pinned source's 2025 world-production column ≈ 250,000 kt and Australia's reserves 120,000 kt (JORC-compliant). Completing the re-pin — replacing the displayed rows row by row with the pinned vintage's per-country reserve figures — is the **registered open data action**; it requires the per-country MCS 2026 reserve table, and no displayed classification depends on it.

#### 6.5.4 The fisheries removals-only pressure time

The fisheries column of the classification matrix is the removals-only pressure time. When $\mathrm{SSB}_{\mathrm{now}} > B_{\lim} > 0$ and $F_{\mathrm{now}} > 0$, define $R_B = \log(\mathrm{SSB}_{\mathrm{now}}/B_{\lim})$ and
$$\Theta_F = \frac{R_B}{F_{\mathrm{now}}},$$
the fishing-only time-to-reference: the crossing time of the deliberately incomplete comparison process $\dot B = -F_{\mathrm{now}}B$. With $B_{\lim} = 0.2 \max \mathrm{SSB}$ this is the construction tabled as ADH in Section 6.5.2; the two notations are kept because the boundary hypotheses stated here ($F_{\mathrm{now}} > 0$, $\mathrm{SSB}_{\mathrm{now}} > B_{\lim}$) are exactly the conditions of the positive sub-cohort of Section 6.5.2 (35 stocks, median $2.9$ yr); the reported Section 6.5.2 median ($\approx 1.8$ yr) additionally carries the eight zero entries for stocks at or below the reference, per the zero convention of the source caption. It is a **removals-only pressure timescale**: the time unit comes from rescaling a stock-reference margin by one isolated gross-loss rate. Because recruitment, somatic growth, maturation, natural mortality, density dependence, environmental forcing, and future policy are omitted, $\Theta_F$ is not a net biomass depletion diagnostic, not a demographic hitting-time estimate, and not a member of the $J^{\mathrm{gross}}$–$H^{\mathrm{loc}}$–$T_A$ hierarchy. A genuinely local biomass-decline ratio $H_B^{\mathrm{loc}} = (B - B_{\lim})/[-\dot B]_+$ would require a compatible net $\dot B$ estimate, and a demographic hitting time a fully specified population model; RAM Legacy SSB and $F$ data (Ricard et al., 2012) do not by themselves supply these quantities or models. Spawning biomass is not an abiotic support pool. The construction is retained specifically to show why an isolated gross-removal timescale must not be promoted to a net depletion diagnostic.

**The collective implication for material-flow measurement.** The three published "depletion time" numbers — G3P index, phosphate reserve-life, fisheries removals-only time — answer three distinct questions at three distinct evidentiary levels.

**Proposition 32 (Boundedness of the persistence index on the declared trend class).** Let
$a_k=-\beta k+\varepsilon_k$ for $k=1,\dots,n$, with $\varepsilon_k$ independent of scale
$\sigma$ and $\beta>0$. Within the declared class, the record minimum lies at the end of the
record once the trend dominates the noise, so the fitted distance from the current level up to that
minimum is a noise-scale gap and the index
$$\frac{a_n-\min_ka_k}{\text{fitted decline rate}}$$
is $O_{\mathbb P}(\sigma/\beta)$: bounded in probability as the record length grows, and
independent of the stock. A simulation of 400 replicates at each of $n=10^2,10^3,10^4,10^5$ with
$\beta=\sigma=1$ returns a mean index of 0.21, 0.25, 0.21 and 0.25 yr, and a 90th percentile of
0.81, 0.84, 0.95 and 1.00 yr, while the stock implied by the same series falls by five orders of
magnitude; the median is zero at every length, because under a downward trend the current level is
usually the record minimum. The index is therefore flat in the record length at the noise-to-trend
scale $\sigma/\beta$, which is the sense in which it cannot be extended into a horizon; the code
and the seed are archived with the supplementary material. Lengthening or densifying an anomaly
record cannot produce a horizon, because the statistic converges to a trend-detection quantity
expressed in years. This is a property of the declared linear-trend class and of the reported
simulation, not a claim about any basin.

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
its supremum attained at the balanced start $(50, 50)$ and its infimum approached as either component
nears its barrier. Both recorded instances lie in the set, $0.6931$ yr from $(2, 98)$ and $3.9120$ yr
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
in which case the same two programmes bound the value set from outside instead of recovering it, and identifiability from an aggregate record holds exactly when the declared
component data reduce the fibre to a point --- which is a statement about the input, never about the
aggregate.

*Proof.* $\tau(x_0) = \min\{\log x_1(0), \log x_2(0)\}$ with $x_2(0) = 100 - x_1(0)$: the function is
increasing then decreasing in $x_1$ on $[1, 99]$, symmetric about $50$, with maximum $\log 50$ and
limit $0$ at the ends, so its image is $[0, \log 50]$. The fibre is an intersection of the declared
boxes with the invariant hyperplane, hence a convex polytope; $\tau$ is continuous, so its image is a
connected interval. Its maximum is not a vertex value --- $\min_j$ of affine functions is concave, and a
concave function attains its maximum where it likes, here at $x_1 = x_2 = 50$ --- while its minimum over the
segment is attained at an end, where $\tau$ tends to $0$. The two programmes of the statement are read off
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

The inverse-Gaussian results condition on the drift, the barrier and the noise scale. Measurement error, serial dependence, seasonal forcing, spatial aggregation, trend breaks and common climatic drivers are **separate** uncertainties, and integrating any of them out yields a predictive mixture rather than a single inverse-Gaussian law. A residual scale estimated from the same window does not by itself identify process noise. A residual scale estimated from the same window does not by itself identify process noise. **No calibrated predictive distribution is claimed**; the full uncertainty treatment belongs to an empirical identification study, not to this paper. For industrial-ecology measurement this discipline is the practical message: first-passage distributions on declared surrogates are usable as descriptive statistics, but their drift, barrier, and noise inputs each carry their own identification story, and a calibrated forecast requires that story to be discharged.

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

**Proposition 43 (The institutional-failure subsystem is exactly closed).** *Under the institutional-failure
specialization of Section 5.4, the ecological-institutional subsystem on $(N, A^{\mathrm{act}}, A^{\mathrm{geo}},
U, Z, E)$ is an exact closed projection of the ledger for every parameter value: no singular limit, no small
parameter and no timescale separation is required, and no macroeconomic variable enters its vector field.*
*Proof.* The six right-hand sides displayed above depend only on the block's own states and the delayed memory; a
subsystem whose vector field involves no excluded variable is invariant, and invariance is the projection. The
converse fails by construction --- the excluded block is driven by the subsystem --- so the projection is
one-way, and Section 5's macroeconomic readouts remain available without being determined. $\square$

What the proposition does not claim is the next step, and the distinction is the point of stating it: the
memory-effort pair $(Z, E)$ is the gated three-state core and working four-state core of the companion
delay-dynamics analysis (under review; its eq. (1), the gated three-state core, and its Section 2.4, which
relates that core to the working four-state model), not an object of this paper, and the semiconjugacy
condition $D\pi(\xi) f(\xi) = F(\pi(\xi))$ on the history phase space --- which would carry closed-block
results across to that system --- is made under the citation and is not re-proved here.

**The non-reduction boundary.** There is no exact dynamic reduction from the closed primitive finite-donor ledger to the open working system — not as a projectable reduction and not as a regular perturbation. The reasons are mathematical:

1. 1. **Different targets.** The primitive ledger uses the intrinsic donor-limited target $A_{\mathrm{eq,intrinsic}}$; the working system uses the derived target $A_{\mathrm{eq},W}=A_{\mathrm{eq,intrinsic}}+\kappa_AK/\omega_A$. The three registered numbers display the separation: $A^{\mathrm{eq,intrinsic}} = 50$, the working active pool $A^{\mathrm{act,*}} = 397.87$, and $A^{\mathrm{eq,W}} = 50 + \kappa_A K/\omega_A = 5050$ — the two equilibria differ by a factor of eight and the two targets by two orders of magnitude.
2. under the registered scale separation ($\sigma\approx1$): approximately **0.535** stock units per year at the working point's quasi-rest detritus level (where $\gamma_UU=\mathcal T^*\approx4.47$, the gross uptake at the working point) and $\kappa_AK=\mathbf{5.000}$ stock units per year at $U=0$ — an $O(1)$ to $O(\kappa_AK)$ discrepancy, not a small residual. The two same-state flux readings behind it are the working recharge $\omega_A(A_{\mathrm{eq},W}-A_{\mathrm{act},*})=4.652$ and the closed donor flow $e_{GA}-e_{AG}\approx-0.348$, whose signed difference is $4.652+0.348=5.000=\kappa_AK$. The difference is $U$-dependent because the working field omits the detritus return $\gamma_UU$ that the closed field carries — the $U$-handling split is part of this obstruction, and $\mathcal B^*-R^*=\mathcal T^*$ is the working system's turnover balance, **not** the field difference. 3. **The working point is not at rest in the closed system.** It requires continuing geological support — the flux $\omega_A(A_{\mathrm{eq},W}-A_{\mathrm{act},*})=4.652133\ldots$ stock units per year, supplied every year by a donor the working system treats as a parameter — and is not a rest point of the closed finite-donor system (Theorem 12). At the same state the closed primitive donor flow is $e_{GA}-e_{AG}=\omega_A(A_{\mathrm{eq,intrinsic}}-A_{\mathrm{act},*})\approx-0.348$: **the donor gains in the closed ledger where the working completion has it losing 4.652** — the two fields have opposite signs on the donor coordinate, not merely different magnitudes. The working-point figures $E^* \approx 2.090$, $N^* = 89.526$, $A^{\mathrm{act,*}} = 397.87$, and the recharge $4.652$ are imported at the companion's registered precision; the reverse check $qE^*N^* = 0.001 \times 2.090 \times 89.526 \approx 0.187$ is consistent to the quoted digits.
4. The cumulative donor-draw quantity $\varepsilon_G(T) = G_0^{-1}\int_0^T |e_{GA} - e_{AG}|\, dt$ is a diagnostic of the derived-target completion, not a trajectory-tracking error between the two fields; no finite-time tracking theorem between the completions holds.
5. The closed primitive system makes sustained extraction integrable (Theorem 14) and therefore cannot possess the working positive-flux rest indefinitely.

The five reasons form a trichotomy: **(1)–(3)** are short-time obstructions — the two $A_{\mathrm{act}}$ fields differ by $\kappa_AK-\gamma_UU$ at the same state, which is $O(1)$ at the working point's quasi-rest detritus level ($\approx0.535$) and at most $\kappa_AK=O(5)$ (at $U=0$), and trajectories of the two systems diverge on $O(1)$ timescales; **(5)** is the long-time obstruction — extraction on the closed ledger is $L^1$ in time (Theorem 14); **(4)** is neither — $\varepsilon_G$ is not a tracking error between the two fields at any timescale. Collectively:

**Theorem (Non-reduction of the open working completion).** *There is no exact dynamic reduction, no regular perturbation, and no finite-time tracking correspondence from the closed primitive ledger (2) to the open working system, because (i) the targets differ by $\kappa_A K/\omega_A = 5{,}000$ stock units (structural); (ii) the $A^{\mathrm{act}}$ fields differ by $O(1)$ at the working point (short-time); (iii) the working point is not a rest point of (2) (Theorem 12; equilibrium); (iv) $\varepsilon_G$ is not a tracking metric (diagnostic misuse); and (v) extraction on (2) is $L^1$ in time (Theorem 14; long-time).*

The permitted relation is analogy for shared mechanism language, plus diagnostic reconstruction of omitted mass flows. The companion's global periodic results are properties of its reduced systems and do not transfer to the closed primitive ledger; in particular, Hopf or periodic orbits of the frozen-donor working system are not properties of (2). In the other direction, the working system is an open projection: omitted turnover is routed to a diagnostic detritus or inert sink, imposed recharge corresponds to geological draw, and the reduced trajectory's mass discrepancy is reconstructible from the omitted flows.

**The frozen-donor limit is a corollary of the structural clause (i).** Rescaling the donor as $G = G_0 g$ with $g(0) = 1$ gives $\dot g = -G_0^{-1}(e_{GA} - e_{AG})$. The limit $G_0 \to \infty$ freezes $g$ but does not restore the working completion's derived target: the limiting recharge field still uses $A^{\mathrm{eq,intrinsic}}$, not $A^{\mathrm{eq,W}}$, so the scaling is not a regular perturbation of the working vector field. Local Hopf persistence of the working system under this primitive scaling is not claimed; a different derived-target completion would be required before a regular-perturbation theorem could be formulated.

**The long-time finite-budget interpretation.** With the donor $G(t)$ included as a state, the closed system is an autonomous retarded equation with a slow donor coordinate. The companion's $\tau_+ \approx 150$ yr upper cycle is a frozen-donor object; on the closed system it can persist only as a transient on the finite donor budget. The transient-duration statement is an order/budget bound, not an asymptotic estimate: under a sustained lower extraction flux $c > 0$ the duration is bounded above by $G_0/c$. At the closed-block extraction rate $c=qE^*N^*\approx0.187$ stock units per year, the budget bound is $G_0/c\approx2\times10^{6}$ years; at the working completion's recharge flux $\mathcal B^*\approx4.652$ stock units per year, the draw scale is $G_0/\mathcal B^*\approx8.6\times10^{4}$ years. Whether the frozen-donor local Hopf structure persists as a slowly drifting transient in the closed donor system is an open slow-passage problem; the mass budget alone does not establish it. The implication for industrial-ecology coupling is concrete: a closed physical ledger and an open working system can share one diagnostic identity without sharing a dynamics, and the temptation to import one system's theorems into the other must be resisted.

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

On the unreduced ledger, no scalar weighting of components is authorized by the accounting itself. The precise statement is on the feasible balance domain (Definition 1): a weighted sum $\sum_m w_m s_m$ certifies componentwise adequacy $s_m \ge d_m$ for all $m$ on $\mathcal{B}(x,t)$ only through an implication proved from the physical restrictions defining the domain — and, in general, no such implication holds. The feasible domain can admit vectors with a positive aggregate and a negative component, exactly the geometry documented in the composite-indicator literature (Munda and Nardo, 2009). In short: a positive weighted sum never certifies componentwise non-negativity.

**Proposition (No weighted certification).** *Let $\mathcal{B}(x,t)$ be the feasible balance domain (Definition 1). If $\mathcal{B}(x,t)$ contains a vector with $b_i < 0$ and $w^\top b > 0$ for a fixed $w \ge 0$, then the certificate $\{w^\top b \ge 0\}$ does not imply $b \ge 0$; if $\mathcal{B}(x,t)$ is not known to exclude that pattern, no nonnegative weighting is authorized as a componentwise certificate.*

*Proof.* On the exhibited vector the componentwise predicate fails ($b_i < 0$) while the weighted predicate holds ($w^\top b > 0$); the two predicates differ on $\mathcal{B}(x,t)$. The inverse-horizon score of Section 6.5.2 (Non-example 1) is the worked witness: a positive aggregate coexisting with componentwise deficits by construction. □

The compensating pattern is constructible against **any** weight, so the failure is universal to the method of weighted certification.

**Theorem (Universal failure of weighted certification).** *Let the ledger have $m \ge 2$ components. For every weight vector $w\in\mathbb R^m_+$, $w\ne0$, there exist a typed ledger as in §2, a demand vector $d$, and an admissible state–operation pair $(x,u)$ with $u\in\mathcal U(x,t)$ whose attainable balance $b=O(x,u,\theta)-d$ satisfies $w^{\top}b\ge0$ while $b_m<0$ for some component $m$. No nonnegative weighting is therefore a valid componentwise certificate in general.*

*Proof.* Take the two-compartment ledger with stock $x = (x_1, x_2) \in \mathbb{R}^2_+$, one donor-limited transfer flux $f = kx_1$ from compartment 1 to compartment 2 ($k > 0$), identity readout $\mathcal{O}(x, u, \theta) = x$, and demands $d = (d_1, d_2)$. Every nonnegative state is admissible with the declared flux, because donor limitation holds ($f = 0$ at $x_1 = 0$), so the balance $b = x - d$ is attainable for every $x \in \mathbb{R}^2_+$; the admissible operating set is the flux declaration itself. Fix $w$ and let $j$ be an index with $w_j > 0$. If some $m \neq j$ has $w_m = 0$, place the deficit there: choose $x_m < d_m$ and $x_j \ge d_j$, giving $w^\top b = w_j (x_j - d_j) \ge 0$ while $b_m < 0$. Otherwise $w_m > 0$ for every $m \neq j$: choose any $m \neq j$ with $x_m < d_m$, and choose $x_j \ge d_j + \bigl( w_m (d_m - x_m) + \varepsilon \bigr)/w_j$ for any $\varepsilon > 0$. Then
$$w^\top b = w_m (x_m - d_m) + w_j (x_j - d_j) \ge w_m (x_m - d_m) + w_m (d_m - x_m) + \varepsilon = \varepsilon \ge 0,$$
while $b_m = x_m - d_m < 0$. The pair $(x, d)$ is the witness for $w$. □

The construction never uses the dynamics: the failure is a property of nonnegative weightings over mixed-sign balances, not of the donor-limited positivity mechanism. Consequently, on any feasible balance domain containing a compensating pair — and Definition 1's domain is exactly that whenever the operating set admits states with mixed balances — no nonnegative weighting can stand in for the conjunctive criterion of Section 3.2. The reading is the algebraic form of the weak-comparability thesis stated in §1.1.

The companion assessment analysis (Abaee, 2026c, doi:10.5281/zenodo.22545740) proves the dynamic form of the same separation for transition operators; the ledger side contributes the static prerequisite: the aggregation question is only well posed after the balance domain is declared, and the burden of proof sits on the aggregation, not on the componentwise report. The same separation holds at the service layer: a weighted sum on $\mathcal{B}(x,t)$ cannot see the directional support gap $(1 - \alpha_{\mathrm{reg}})\bar s$ of Definition 2 — an aggregate that mixes regenerative and non-regenerative provenance never reports which component carries the gap. In the terms of the ecological-economics literature of §1.1: componentwise adequacy on the typed ledger is **strong sustainability as a conjunctive predicate**; a positive weighted sum is **weak sustainability as a ranking device**. The ledger authorizes the first and does not authorize the second.

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

**Proposition 30 (Worst concealed deficit).** Let the component balances lie in declared bounds
$\ell\le b\le u$, and let $z$ be a published aggregate value $z=w^{\top}b$ with $w\ge0$,
$w\ne0$. The most severe deficit an aggregate of that value can conceal in component $j$ is
$$\delta^{*}_j(z)=\max\ \{-b_j:\ w^{\top}b=z,\ \ell\le b\le u\},$$
a linear programme, finite whenever the bounds are, and positive whenever any admissible $b$ has
$b_j<0$. Together with the premium it turns the noncompensation result into a two-sided audit: the
premium measures what the aggregate bought with trades, and $\delta^{*}_j$ measures what it can
hide. Reported on declared bounds only, it is arithmetic on a published construction; where the
bounds are not declared, the value is reported as not established.

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

The asymmetry is exact and one-directional. A coarse aggregate refutes, because a violated aggregate
barrier is a violated component barrier, and it alarms, because a positive premium is a measured
quantity; it does not certify, because the concealed deficit of Proposition 30 can be made positive
at any published aggregate value the domain admits.

### 10.2 The double-counting discipline

Five rules, each carried by a proved or defined statement of this paper and specified as a checkable procedure in the companion methods study (Abaee, 2026d), jointly prevent double counting and phantom mass:

1. **One balance per moiety.** Conservation laws attach to declared moieties (Theorems 7–8); adding unlike units — biomass, money, biodiversity indices, exergy — into one conserved scalar is not authorized by any conservation theorem. 2. **Explicit stoichiometry.** Entries are added within an incidence row only when their types and units agree; every conversion is an explicit coefficient in $S_{\mathcal{T}}$, never an implicit sum (Section 2.1). 3. **Yield routing.** A transformation represented with yield below one must route the omitted fraction to a represented compartment or a declared boundary flow; otherwise the moiety balance holds only after silently dropping the moiety (Theorem 15). 4. **No ghost sinks.** Every primitive with an outflow from some compartment must have its routed inflow represented, and every inflow its source — opposite-sign incidence of the same primitive is checkable column by column — and the six-state cancellation of Section 4.9 shows the check passing, while the same template shows that cancellation without donor-limited admissibility establishes nothing. 5. **Classification labels stay out of the columns.** Reserve-life and resource-threshold quantities answer different questions and share a column only under an explicit convention label (Section 6.5.3); diagnostic labels never determine material routing (Section 2.5).

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

The classification results of §6.5 are negative results stated as such: the anomaly index is not a stock ratio; the reserve-life ratio is not a forecast; the removals-only time is not a depletion diagnostic. The non-reduction boundary of §9 is a rejected mapping with five mathematical reasons. The sink obstructions of §2.4 are empty-kernel mechanisms. A quantity that answers exactly one question, stated with that question, **is** the framework working — and the framework's claim about itself is limited to the accounting layer it establishes.

### 10.4 Limitations

1. **(i)** The two-pool exact specialization of the groundwater template remains **open**. (ii) The phosphorus and groundwater rows are registered template obligations: no constitutive content exists behind their identification ladders. (iii) The first-passage propositions of Section 7 concern declared stochastic surrogates, not the ledger: they do not compute the ledger's hitting time, do not conserve its mass, and carry the record-relative-barrier and non-claim disciplines. (iv) The applied records of Section 6.5 are classified diagnostics at their stated evidentiary levels — statistical index, arithmetic ratio, removals-only pressure scale — and none is a calibrated early-warning system or a forecast. (v) The non-reduction boundary of Section 9 is permanent mathematics, not a gap: the closed primitive ledger and the open working system are different completions. (vi) The conditional hybrid balance of Theorem 15 stays conditional, with its jump-interpretation and yield-routing obligations open per application. (vii) The support-saturation limits of Section 2.6 are local and finite-time; neither is a full-system reduction. (viii) This paper asserts nothing empirical about any named resource system beyond the classifications of public data products stated at their source status.

---

## 11. Conclusion

The two failure modes of the introduction — compensatory aggregation and classification drift — are representation errors, and the representation that prevents them is the account's content. Conservation is proved from the incidence structure, not assumed; positivity is proved from donor limitation, not asserted; services are readouts, not mass; and depletion time is three quantities, not one. The closed finite-donor ledger carries its complete theorem set — the natural-block mass identity, orthant invariance, no interior rest at positive effort, the vanishing-extraction rest set (extinction, carrying capacity, and the frozen-biomass face), extraction integrability — and the non-reduction boundary records, with reasons, why the closed ledger and the open working systems of institutional dynamics are different completions sharing one exact object. The depletion numbers of the applied record answer, each, exactly the question their construction poses: a statistical index of record-relative stress, an arithmetic ratio of an economic classification, a pressure scale of one gross loss rate. Stating them with those questions — against the published critiques they corroborate — is what makes them usable.

This paper likewise locates substitution within the ledger, not alongside it. The weak and strong regimes of §1.1 are two readings of one typed stock–flow ledger, distinguished by whether the material cycle closes at the rate of use; that reading is developed once, in the introduction, and is not re-argued here. A substitute is either a recycled flux returned to the regenerating pool, or a non-renewable drawdown on a second compartment — different ledger entries with different statuses. The reserve classification carries the same point: a horizon estimate built on reserves inherits the substitution and technology assumptions inside the classification, which is why it is read as a ratio, never as a forecast. Services — drinking water, crop yield, fish caught — are readings taken off the ledger, not substances flowing in it. For ecological-economics measurement, that is the closing statement: not rival doctrines but two readings of one ledger, and the vector reading is what carries the certificate.

---

## Data availability

All computations underlying Section 6.5 are descriptive arithmetic on the cited public data products: the G3P groundwater anomaly product v1.12 (Güntner et al., 2024; GFZ Data Services, doi:10.5880/G3P.2024.001), the U.S. Geological Survey Mineral Commodity Summaries 2026 (the January 2026 release), and the RAM Legacy Stock Assessment Database, release v4.66 (Ricard et al., 2012; Zenodo 14043031; the cohort is the
dated extract recorded in the supplementary's S5 record, and no cohort statistic is quoted from any other release). The overshoot-date arithmetic of Section 10.2 and Remark 33 is read off the component tables of the National Footprint and Biocapacity Accounts, whose current edition the publisher distributes free but behind registration. The two editions used for the sensitivity check recorded in the supplementary (S17) — the 2018 edition, with series 1961 to 2014, and the 2017 edition, with series 1961 to 2013, both distributed by the publisher under CC BY-SA 4.0 — are held with the analysis record beside the script that computes both conventions from them and the outputs of that run, so that the computation can be re-run without a network. The tables themselves are not redistributed with this deposit: the manifest beside them gives the two retrieval commands, the sizes and the checksums of the bytes as read, and the script records the checksum it obtained, so that the copy read can be shown to be the copy analysed. The parameter tables of Section 2 are declared parameterizations. No other data were used.

## Code availability

The scripts that generate every computed figure in this article — the persistence-index simulation of Section 6.5, the curvature and crossover arithmetic of Section 6.2, and the compensation-premium and worst-concealed-deficit linear programmes of Section 10.1 — are archived with the supplementary material, with the random seed and the library versions recorded in the archive manifest. The overshoot-date recomputation reported in Remark 37 and in the supplementary (S17) is archived as a separate analysis record beside the reproduction bundle, whose manifest restricts that bundle to arithmetic on declared figures and excludes data ingestion. It reads the two edition tables named in the data availability statement, requires nothing beyond the Python standard library, prints the aggregation diagnostic reported in Section 10.2, and reproduces its tabulated outputs from the archived copies of those tables; a newer edition of the accounts is run by supplying a different input file.

## Funding

None declared.

## Declaration of competing interest

None.

---

## References

Abaee, A., 2026a. Delay-induced regime change in harvested stocks: the mobilising and protective channels of institutional feedback, and the review interval as control. Zenodo. https://doi.org/10.5281/zenodo.22554217. Companion delay-dynamics study.

Abaee, A., 2026b. Periodic review as sampled governance: sample-and-hold dynamics of assessment-driven effort control, a selected 42-stock spectral screen, and the Northern Cod case. Zenodo. https://doi.org/10.5281/zenodo.22554297. Companion review-screen study.

Abaee, A., 2026c. The limits of compensatory aggregation: a formal separation of weak and strong sustainability assessment. Zenodo. https://doi.org/10.5281/zenodo.22545740. Companion assessment-separation study.

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

U.S. Geological Survey, 2026. Mineral Commodity Summaries 2026: Phosphate Rock. USGS, Reston, VA. https://www.usgs.gov/centers/national-minerals-information-center/mineral-commodity-summaries

United Nations, 2025. System of National Accounts 2025. United Nations Statistics Division, New York. Endorsed by the United Nations Statistical Commission at its fifty-sixth session, March 2025. https://unstats.un.org/unsd/nationalaccount/sna2025.asp

United Nations, European Commission, International Monetary Fund, Organisation for Economic Co-operation and Development, World Bank, 2014. SEEA Central Framework: 2012 Technical Implementation. Statistical Papers, Series M No. 96. United Nations, New York.

Wackernagel, M., Beyers, B., 2019. Ecological Footprint: Managing our Biocapacity Budget. New Society Publishers, Gabriola Island, BC.

---

## Supplementary material

The accompanying supplementary file carries: the ten-state admissibility template and its three audited negative witnesses (the non-donor-limited geological exchange, the variance-closure failure, the undefined output functional); the registered identification ladders of the phosphorus and groundwater templates at full detail; the split-assignment mechanism table; the statement inventory with the status of every statement in the main text (theorem with displayed proof, conditional theorem, definition, application record, or boundary statement) — read with the S6 statement-status naming offset, which maps the supplementary’s status words to the main text’s current labels; and the fisheries cohort record with the archived-pull verification and the executed broad-cohort comparison (S5); the proof obligations attached to each entry of the certification state of Section 3.1 with the certificate vectors of the classified indicators (S7), the linear programmes of Definitions 21–22 and Theorem 24 with their input requirements and the reading rule for an infeasible programme (S8), and the worked exhibits of Sections 6.2, 6.5 and 10.1 with their reproduction record and the statement
inventory extended to the later labels (S9); the extraction provenance of the G3P basin rows (S5.4); the
per-parameter identifiability and value records (S10, S11); the registered template detail behind Sections
8.1 and 8.2 at its full extent (S14 to S16); and the recomputation of the aggregate overshoot date reported
in Remark 37, with the two editions of the accounts it reads named, licensed and hashed (S17).

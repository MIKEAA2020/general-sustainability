# Typed Flux Ledgers and Depletion Arithmetic: Conservation, Componentwise Diagnostics, and the Semantics of Depletion Horizons

**Amin Abaee**  
*Independent Researcher*  
ORCID: [0000-0002-0019-1842](https://orcid.org/0000-0002-0019-1842)  
`amin_abaee@ut.ac.ir`  
*September 6, 2026*

---

### Abstract
Depletion metrics routinely circulate under a single colloquial label while answering fundamentally incompatible questions. Reserve-life ratios, trend-persistence metrics, and gross-removal pressure scales are widely interpreted as a literal “time to depletion,” despite measuring distinct physical or statistical quantities. Compounding this ambiguity, compensatory scalar aggregation routinely masks critical physical deficits behind positive aggregates. 

In this paper, we resolve these confusions by constructing a typed stock–flow accounting ledger. By tracking conserved substance classes (*moieties*) independently, conservation laws remain strictly typed: biomass, financial flows, and biodiversity metrics cannot be summed into a single scalar. Mass conservation follows directly from the incidence structure of the compartment–flux network, nonnegativity is guaranteed by donor limitation (primitive outflows vanish whenever their source compartment empties), and ecosystem services are treated strictly as observable readouts rather than conserved mass.

We formalize three certification layers: a flux-reconstruction identity that recovers unobserved internal fluxes from observed stock trajectories, a conservation-law reduction, and an envelope theorem providing verifiable flux-bounding certificates. For the closed finite-donor ledger, we establish the natural-block mass identity, orthant invariance, the absence of interior rest points under positive extraction effort, a characterization of the vanishing-extraction rest set (extinction, carrying capacity, and a frozen-biomass face), and extraction integrability over finite budgets. Furthermore, we unpack “depletion time” into three mutually non-interchangeable concepts: gross turnover intensity, a frozen-rate local ratio, and a scenario-conditioned hitting time equipped with uniform-drift bounds. 

We classify three widely cited public-data indicators within this taxonomy: the G3P groundwater anomaly index is shown to be a record-relative statistical metric rather than a physical stock ratio; the USGS phosphate reserve-life ratio is an arithmetic convention of an economic class rather than an exhaustion forecast; and fisheries removals-only timescales represent gross pressure metrics rather than demographic depletion diagnostics. We prove that no nonnegative linear weighting can universally certify componentwise nonnegativity on arbitrary balance domains, and we establish five double-counting rules to prevent the emergence of phantom mass. Finally, we formulate first-passage semantics on declared stochastic surrogates against record-relative barriers alongside explicit non-claims. Weak and strong sustainability emerge not as competing paradigms, but as two operational regimes of a single dynamic system, governed by whether material cycles close at the rate of throughput.

**Keywords:** material flow accounting, stock–flow ledger, depletion indicators, first-passage time, conservation laws, composite indicators, reserve life.

---

## 1. Introduction

### 1.1 Failure Modes and the Two Confusions
Sustainability accounting consistently suffers from two structural pathologies:

1. **Compensatory Aggregation:** Heterogeneous physical stocks and service flows are compressed into scalar indices. Because cross-component substitution rates are rarely declared formally, acute physical deficits in one critical sub-system are mathematically obscured by surpluses elsewhere. While the composite-indicator and ecological economics literatures have long critiqued this flaw and proposed noncompensatory remedies (Munda & Nardo, 2009; Ekins et al., 2003; Neumayer, 2013), scalar index construction remains ubiquitous.
2. **Classification Drift:** Heterogeneous metrics with the dimension of time—reserve-life quotients, trend-persistence indicators, and gross extraction timescales—are conflated into a single catch-all quantity: “time to exhaustion.” Yet, these metrics answer fundamentally different questions under incompatible boundary assumptions.

The operational reality of classification drift is striking. A reserve-life ratio simply divides an economically declared reserve by current annual production, christening the quotient a “depletion horizon.” A satellite groundwater anomaly index fits a linear trend to gravimetric anomalies, reporting the time needed to reach the historical record minimum at current rates; the result is expressed in years, yet corresponds to no physical exhaustion event. A fisheries pressure metric scales a logarithmic biomass margin by instantaneous fishing mortality, presenting a gross clearance timescale as if it were a demographic extinction date. Each metric provides specific institutional or descriptive information; none represents what is popularly claimed.

The primary manifestation of compensatory aggregation is exemplified by public awareness metrics such as *Earth Overshoot Day*. By collapsing ecological footprints and biocapacities into a single annual calendar date, an catastrophic deficit in an irreplaceable sub-component can easily coexist with an aggregate overshoot date that falls comfortably late in the calendar year (Lin et al., 2018; Wackernagel & Beyers, 2019; Blomqvist et al., 2013). Systems-dynamics models encounter identical aggregation ambiguities when multidimensional state spaces are collapsed into scalar stress variables (Meadows et al., 1972). The framework developed here is component-resolved by construction: depletion horizons are defined and tracked per asset and per pool, completely precluding cross-component summation into a scalar date.

Beyond these accounting failures lies a deeper dynamical failure mode: the **productivity illusion**. This is the deceptive phenomenon in which an extractive system appears fully functional while the underlying support base sustaining its throughput is hollowed out. The illusion operates on two levels:
* **The Arithmetic Level:** This is simply compensatory aggregation in disguise—a deficit in an unmonitored capital stock is mathematically masked by current consumption flows. We formalize this limitation as an aggregation obstruction in Section 10.1.
* **The Dynamical Level (Yield Inflation):** Here, harvest or extraction yield remains high because the system draws down an unmodeled support pool—such as fossil groundwater, soil organic matter, or parent mineral deposits—rather than operating within the regenerative flux of that pool. The resource appears highly productive precisely because its natural foundation is being liquidated.

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

---

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
   * The RAM Legacy fisheries clearance timescale is identified as a removals-only pressure metric, not a demographic hitting time.
6. **First-Passage Semantics on Declared Surrogates:** We formalize first-passage processes using inverse-Gaussian distributions (for linear drift models) and geometric Brownian motion (for relative fisheries proxies) against empirical barriers. We provide complete derivations and formalize seven explicit non-claims separating these surrogates from structural ledger dynamics.
7. **Coupling Interface with Institutional Delay Dynamics:** We define the shared mathematical boundary between our mass-conserved ledger and institutional harvest models via the decline-pressure identity $qEN - R = -\dot{N}$. We prove a non-reduction theorem demonstrating why closed mass-conserving ledgers cannot be reduced to open, delay-driven institutional systems.

#### What Is Explicitly Not Claimed
* We make **no claim of a stochastic completion** for the full ledger: the surrogate processes in Section 7 do not conserve mass and are not stochastic perturbations of the underlying vector field.
* We make **no claim of thermodynamic completeness**: energy balances, chemical affinities, and entropy production are not formalized here.
* We make **no claim that the groundwater two-pool model is empirically identified**: the observational data required to resolve fast and slow groundwater storage are outlined as open requirements in Section 8.2.
* We make **no empirical forecasts** regarding specific aquifers, phosphate reserves, or marine fisheries beyond the descriptive classifications derived from published data.

---

### 1.3 Organization
Section 2 formulates the typed ledger, its constitutive laws, and its limiting properties. Section 3 formalizes the three certification layers and proves the core accounting theorems. Section 4 establishes the theorem set for the closed finite-donor ledger. Section 5 constructs the service readout layer and defines the componentwise deficit. Section 6 develops depletion arithmetic, proves the uniform-drift brackets, and classifies empirical indicators. Section 7 details first-passage semantics and its analytical boundaries. Section 8 details domain templates for phosphorus, groundwater, and bioeconomic harvesting. Section 9 proves the non-reduction interface with institutional delay models. Section 10 outlines analytical boundaries, the failure of weighted aggregation, and double-counting safeguards. Section 11 concludes.

---


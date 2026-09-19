# Typed Flux Ledgers and Depletion Arithmetic: Conservation, Componentwise Diagnostics, and the Semantics of Depletion Horizons

**Amin Abaee**  
Independent Researcher  
ORCID: 0000-0002-0019-1842 | amin_abaee@ut.ac.ir

---

## Abstract

Depletion indicators can carry the same units while addressing distinct questions. A reserve-life ratio divides an economic inventory by current production. A groundwater anomaly-persistence index divides a fitted distance to a historical minimum by a fitted trend. A fisheries removals-only pressure scale divides a log biomass margin by a fishing mortality. These quantities share a unit, but they do not share a measurand. The same problem appears in aggregate sustainability accounting: heterogeneous stocks and service flows are compressed into scalar indices, and a deficit in one component can be hidden behind a positive aggregate.

This paper constructs a typed stock–flow accounting layer that separates these objects. Conservation follows from the incidence structure of the compartment–flux network. Positivity follows from donor limitation. Services are readouts, not conserved mass. Three certification layers are separated: accounting consistency, conservation consistency, and barrier safety. A flux-reconstruction identity, a conservation-law reduction, and a flux-bounding envelope theorem provide the auditing machinery. For the closed finite-donor ledger, we prove the natural-block mass identity, orthant invariance, absence of interior rest at positive effort, the vanishing-extraction rest set, and extraction integrability. Depletion time is separated into three non-interchangeable quantities: gross turnover intensity, a frozen-rate ratio, and a scenario-conditioned hitting time. A universal noncompensation theorem proves that no nonnegative weighting certifies componentwise adequacy. Three public-data applications are classified at their exact evidentiary status. An interface contract fixes the shared object with delay-based institutional dynamics and proves the non-reduction boundary.

The result is a formal grammar for material depletion claims: each claim carries the predicate it actually establishes, and no claim is promoted beyond that predicate.

**Keywords:** material flow accounting; stock–flow ledger; depletion indicators; conservation laws; composite indicators; noncompensation; reserve life

---

## 1. Introduction

### 1.1 Two representation failures

Sustainability accounting fails in two characteristic ways.

The first is **compensatory aggregation**. Heterogeneous physical stocks and service flows are summarized by scalar indices whose cross-component trades are never declared as mathematics. A severe deficit in one component can coexist with a positive aggregate. Composite indicators and aggregated overshoot dates illustrate the problem: component flows are carried into one scalar, and the scalar becomes the object of debate rather than the componentwise balances behind it.

The second is **classification drift**. Quantities with units of time circulate under a common label—“time to depletion”—while answering different questions. A reserve-life ratio divides a reserve figure by current production. A groundwater anomaly index divides the fitted distance to a historical minimum by a fitted trend. A fisheries pressure indicator divides a log biomass margin by a fishing mortality. Each construction is exact for the question it poses. The problem is promotion: an answer to one question is read as an answer to another.
The same conflation pervades accounting itself. Material flow analysis supplies the bookkeeping of society's material throughput (Brunner and Rechberger, 2004; Eurostat, 2001; Fischer-Kowalski et al., 2011), and its incidence structure is shared with reaction-network theory, where the sign pattern of the stoichiometric matrix is a conservation object (Feinberg, 2019). Bookkeeping balance, stoichiometric conservation, thermodynamic admissibility, and sustainability safety are four different predicates, and the literature routinely slides between them. A mass-balanced ledger can be chemically impossible. A chemically consistent ledger can violate every declared barrier. A ledger satisfying all declared barriers can fail conservation. Separating these layers and proving their relationships, so that each claim about a material system carries the predicate it actually establishes, is this article's first task.

The issue is not the unit. All three quantities have the dimension of time. The issue is the measurand. Same dimension does not imply same quantity. Period, half-life, residence time, and time constant all have units of seconds, but they are not interchangeable. Work and torque both have units of N·m, yet they are different objects. The category error that could occur is inferential: it arises when indicators that belong to different categories are equated, or when one indicator is read as establishing the predicate of another.

The vulnerability is documented in specific public cases. Reserve-life ratios have been central to mineral depletion debates, and mineral economists have repeatedly emphasized that reserves are economic classifications rather than fixed physical stocks. Satellite groundwater anomaly products provide anomalies relative to a reference period, not absolute aquifer volumes; yet anomaly-based trend indices can be communicated as if they were physical exhaustion horizons. Fisheries removals-only pressure scales can be read as collapse forecasts even though they omit recruitment, growth, natural mortality, and future management. These cases show the structural risk: a shared unit invites a shared interpretation that the mathematics does not support.

### 1.2 The productivity illusion

A related failure is the **productivity illusion**: a system appears productive while the base that sustains production is being drawn down.

Its arithmetic form is compensatory aggregation: a positive aggregate masks a deficit in one component. Its dynamical form is yield inflation: measured yield exceeds sustainable yield because it is maintained by liquidating a support pool—groundwater, soil carbon, bioavailable nutrients—rather than by that pool’s regeneration.

The decisive quantity is the renewal rate of the pool relative to the rate of use. A use that falls on regeneration is sustained. A use that falls on the pool itself is liquidation. The size of the pool is a property of the resource; whether drawdown is recoverable is a property of the rate. The pool may be read as natural capital, as a stock, or as a slowly regenerating flow of services: these are overlapping readings of the same pool, not mutually exclusive ones. Every such pool is regenerative on some timescale — a crop within a season, an aquifer within years to decades, a mineral deposit over geological time — and the failure is the same in each case. A drawdown is recoverable only insofar as the pool regenerates faster than it is taken; if a pool regenerates too slowly for the rate at which it is taken, the drawdown is still liquidation.

The two-pool logic of this paper exists to make that distinction visible. Depletion horizons are reported component by component, each beside the pool it draws on, and never summed into a scalar date.

### 1.3 Weak and strong sustainability as two regimes of one ledger

Weak and strong sustainability are not rival hypotheses. They are two regimes of one material system, distinguished by whether the material cycle closes at the rate of use.

Weak sustainability is the idealized regime in which substitution and regeneration together close the cycle: matter is returned, redistributed, or replaced as it is used. Strong sustainability is the regime in which closure fails—either because no identified physical pathway re-routes the extracted matter, or because depletion outruns deployment of such a pathway.

In ledger terms, substitution is admissible only where an identified physical pathway exists and does not draw down another critical stock. A substitute is either a recycled or recovered flux returned to a regenerating pool, or a drawdown on a second compartment. These are different ledger entries with different statuses. The balance must be maintained as neither consumption nor population grows faster than the productivity that supports them, and the drawdown must not be recoverable only on a timescale longer than it is taken (Daly, 1990). The scenario-conditioned hitting time of Definition 5 exists to give that drift a horizon.

The two regimes can be stated on the ledger's own objects rather than as attitudes toward them. Let \(S_T\) be the incidence operator of Section 2.2, let \(v\ge0\) be the primitive fluxes under declared capacities \(\bar v\), let \(B_Tu_\partial\) collect the declared boundary transfers, and let \(P\) project a flux vector onto its use columns. Write \(\mathcal K=\{v\ge0:\ S_Tv+B_Tu_\partial=0,\ v\le\bar v\}\) for the admissible stationary flux patterns.

**Definition 21 (Closure cone).** A demanded use vector \(D\) closes at the rate of use if and only if \(D\in P(\mathcal K)\). The closure capacity \(\lambda^{*}=\max\{\lambda:\ \lambda D\in P(\mathcal K)\}\) is a linear programme on the declared capacities, and its feasibility is the cut condition on return capacity (Gale, 1957; Ahuja et al., 1993). Where \(\lambda^{*}\ge1\), the cycle closes at the demanded rate. Where \(\lambda^{*}<1\), every trajectory meeting \(D\) has a non-stationary stock, and by conservation the shortfall appears as support drawdown together with sink accumulation; the deficit share is not a free parameter. Yield inflation is the same statement read outside the projection: demand met with no stationary pattern behind it.

Left-null vectors express conservation; right-null vectors express circulation. The regimes of this section are statements about the second set, and the depletion readouts of Section 6 are statements about the first; neither set's membership follows from the other's.

**Definition 22 (Closure deficit at the use timescale).** For each moiety \(m\), let \(\kappa_m(\tau;\Theta)\in[0,1]\) be the fraction of mobilised flux returned to a usable compartment within lag \(\tau\) under the declared technology and process graph \(\Theta\), and let \(\delta_m=1-\kappa_m(\tau_{\mathrm{use}};\Theta)\) be the closure deficit at the declared use timescale. The deficit is a property of a declared graph at a declared timescale, not a rate of the material itself. Where a mobilisation \(g_m\) is sustained with \(\delta_m\ge\underline\delta>0\), the net drawdown of the support pool is \(\delta_mg_m\), so
\[
\int_0^T(\text{liquidation})\,dt\ \ge\ \underline\delta\int_0^Tg_m\,dt,
\qquad
T\ \le\ \frac{m_0}{\underline\delta\,g_m},
\]
the second inequality being the frozen-rate horizon read on the liquidation flux rather than on gross use. Both bounds are one-sided by construction, and neither reverses in the limit \(\delta_m\to0^+\). A positive deficit is not a barrier-reachability claim: a deficit that decays with the stock need never reach a barrier, and where the binding constraint is an upper barrier the relevant object is the complementary headroom.

Two readings follow from the definition. An indicator that reports a return fraction with no lag argument reports \(\kappa_m(\infty)\) where \(\kappa_m(\tau_{\mathrm{use}})\) is being read; the recycled-input and circularity-rate families are of that form, since a ratio of fluxes carries no timescale. And "a material is waste" is, on this reading, the statement \(\kappa_m(\tau_{\mathrm{use}};\Theta)<1\) for the declared graph, so unlocking a stream is an increase of \(\kappa\) at fixed \(\tau\): measurable, and not in need of a new substance category.

### 1.4 Contributions

This paper builds the accounting layer that makes the two representation failures explicit and auditable.

1. **A typed primitive-flux ledger.** Compartments carry a material identity, a boundary, and a unit. Nonnegative primitive fluxes connect them through a signed incidence matrix. Conservation follows from incidence structure. Positivity follows from donor limitation. Services are readouts, not conserved mass.

2. **Three certification layers.** Accounting consistency, conservation consistency, and barrier safety are distinct predicates with distinct proof obligations. The paper proves their relationships through a flux-reconstruction identity, a conservation-law reduction, and a flux-bounding envelope theorem.

3. **The closed finite-donor theorem set.** For the closed ledger in which the geological donor is an internal state, the paper proves the natural-block mass identity, orthant invariance, absence of interior rest at positive effort, the vanishing-extraction rest set, and extraction integrability.

4. **Depletion arithmetic.** Depletion time is separated into three non-interchangeable quantities: gross turnover intensity, a frozen-rate ratio, and a scenario-conditioned hitting time. Uniform-drift bounds and a maintainability terminal condition make the hierarchy operational.

5. **Universal noncompensation.** No nonnegative weighting of component balances certifies componentwise adequacy. The failure is constructive and universal.

6. **Application classifications at exact status.** The G3P anomaly-persistence index, the phosphate reserve-life ratio, and the fisheries removals-only pressure time are classified as statistical index, arithmetic ratio, and pressure scale, respectively.

7. **Interface with institutional dynamics.** The exact shared object with delay-based institutional models is the single-resource deficit identity \(qEN - R = -\dot N\). The boundary is a non-reduction theorem: the closed physical ledger does not dynamically reduce to the open working institutional system.

### 1.5 Scope

The framework establishes relations among declared objects: compartments, fluxes, barriers, scenarios, and readouts. It does not by itself estimate unobserved fluxes, choose ecological thresholds, or identify physical failure barriers. Those remain empirical and institutional tasks. The contribution is the accounting grammar that keeps those tasks separate.

**Antecedents.** The bookkeeping idiom and its reconciliation practice are those of material flow analysis (Section 1.1; Brunner and Rechberger, 2004), and the incidence apparatus is that of compartmental systems and reaction-network theory (Jacquez and Simon, 1993; Feinberg, 2019). The two regimes separated in Section 1.3 are the contested distinction of the weak-versus-strong sustainability and critical-natural-capital literatures (Ekins et al., 2003; Neumayer, 2013), and the aggregate-versus-component question is the non-compensatory-aggregation question posed for composite indicators (Munda and Nardo, 2009), where the footprint accounts that animate part of that debate are themselves under assessment (Wackernagel and Beyers, 2019; Lin et al., 2018; Blomqvist et al., 2013). The terminal-condition tradition is viability theory (Aubin, 1991); the horizon arithmetic sits on a bioeconomic and extractive-price literature (Clark, 1990; Tilton, 2003; Tilton and Lagos, 2007), as do the growth-limit arguments with which depletion horizons are confused (Meadows et al., 1972; Daly, 1990). The statistical standards are closer than that genealogy suggests: the System of National Accounts 2025 treats the depletion of natural resources as a cost of production alongside depreciation, following the treatment developed under the SEEA Central Framework (United Nations, 2014; United Nations, 2025), which leaves the classification of depletion settled and the identification of a horizon open. None of these sources is used as a premise here. The objects proved about are the ledger's own.
**What is not claimed.** No stochastic completion of the ledger is claimed: the surrogate processes of Section 9 do not conserve the ledger's mass and are not perturbations of its dynamics. No thermodynamic admissibility is claimed. No identification of the two-pool groundwater hypothesis is claimed: its identification requirements are registered in Section 8.1, not discharged. And no empirical finding about any basin, aquifer, or fishery is claimed beyond the descriptive status of the tabulated indicators.

---

## 2. The Typed Primitive Ledger

Notation is fixed once and is not re-assigned silently. One letter carries one sort wherever it appears; where a letter is overloaded, the overload is declared and scoped.

**Notation and symbols.** Symbols that recur in more than one role are declared with their scopes.

- \(B\) — gross turnover \(R+T\) (Section 2.3); the barrier pair \(\underline{B},\overline{B}\) (local to Section 3.1); the aggregate regeneration flow \(b\cdot M\) (local to Section 1.3); the biomass variable of Sections 4.6–4.8, where it replaces \(B_{\text{stock}}\).
- \(b(t):=B_Tu_\partial+d_x\) — the boundary-plus-production scalar of the divergence identity (Section 4.1), local to that identity.
- \(d\) — natural mortality in the ledger (Section 2.3) and the divergence operator (Section 4.1), distinguished by position.
- \(s\) — specific uptake in Theorem 13 and the integration variable of the \(L^1\) bound in Theorem 14.
- \(\sigma\) — donor-fraction parameter of the closed ledger; the saturation scale of Section 2.4; the diffusion coefficient of Sections 6.4 and 9.5, whose role there is notational only, since those arguments never invoke the donor or \(g(A)=A/(\sigma+A)\).
- \(S,S^{\mathsf T}\) — service coefficients (Section 5.1) and stoichiometric matrices (Section 2.2).
- \(\tau\) — retention time (Section 2.3) and the integration variable of the Lyapunov–LaSalle argument (Section 4.7).
- \(K\) and \(K_{\mathrm{maint}}\) — capacity in the biological laws and maintainability capacity in Section 6.3, distinguished by the subscript on the latter.

The same discipline applies to the labels of numbered statements: the layering results of Section 3 are cited as Propositions 3.1 and 3.2, to keep them apart from the article-wide proposition counter. Two typographic conventions are in force throughout. \(x\lesssim y\) means \(x\le Cy\) for a constant \(C>0\) fixed by context and independent of the limit variable. A displayed sum over a named index set equals \(+\infty\) when that set is empty. Two conventions of the application sections are likewise fixed once: the record of the 42-stock cohort is its archived-pull origin, which is not a member of the public data releases named in the same section, and no cohort statistic is quoted from a different database version; and the zero convention, \(\mathcal H^{\mathrm{win}}_{\mathrm{GW}}=0\) when the anomaly series is already at its window minimum, applies at every table row where it holds.


### 2.1 Four concepts, separated

Material flow accounting begins with distinctions that practice often merges.

A **moiety** is a conserved substance class—an element or a declared conserved combination. It is the only object to which a conservation law attaches.

A **species** is a chemical or biological form of a moiety.

A **compartment** is a spatial or functional location holding a stock.

A **stock** is a compartment’s current amount of a species, with a physical unit.

“Carbon in the atmosphere” is a location-specific stock, not a moiety. Carbon is the moiety; the atmosphere is a compartment. Conservation laws are stated per moiety. Nothing is conserved merely by being a compartment.

### 2.2 Incidence structure and typed balance law

A ledger state \(x \in \mathbb{R}^n_+\) collects compartments. Each entry carries a material identity, spatial support, and physical unit. Internal dynamics use nonnegative primitive fluxes:

\[
\dot{x} = S_T v(x,y,\theta) + B_T u_\partial(t) + d_x(t), \qquad v \ge 0,
\tag{1}
\]

where:

- \(S_T\) is the typed stoichiometric, or incidence, operator;
- \(y\) collects declared boundary states external to the ledger;
- \(\theta\) is the declared constitutive parameter vector;
- \(B_T u_\partial\) collects declared boundary transfers;
- \(d_x\) belongs to a stated disturbance class.

Where a single vector is more convenient, \(b(t) := B_T u_\partial(t) + d_x(t)\) collects the boundary-transfer and disturbance terms; the two notations denote one object and are used interchangeably below. Where no budget is declared for \(d_x\), the residual is not established at zero and is not bounded: the conservation predicate of Section 3.5 then carries the gap rather than closing it, and Definition 23 states the requirement.

The incidence discipline is load-bearing. Entries are added within a row only when their types and units agree. A conversion between types appears as an explicit stoichiometric coefficient, never as an implicit sum.

If \(L^{\top}S_T = 0\) (the same covector written \(\ell\) in Section 3), then

\[
\frac{d}{dt}(L^\top x) = L^\top B_T u_\partial + L^\top d_x.
\]

This gives one conservation law per conserved moiety and boundary. The identity does not create a scalar sustainability mass across incommensurable systems.

Three clarifications are part of the statement.

First, \(d_x\) must itself be typed. A physical disturbance on represented material is a different object from a structural discrepancy term.

Second, \(S_T\) may contain signed entries even though \(v \ge 0\). The sign pattern of the incidence matrix and the nonnegativity of the primitives are separate declarations.

Third, forward invariance is a separate requirement. Every primitive outflow must vanish or be limited when its donor compartment is empty. Donor limitation is the exact condition that keeps the orthant physically meaningful.

### 2.3 The closed finite-donor ledger

The closed ledger of this paper is the finite-donor primitive system. Let

\[
x_L = (N, A_{\text{act}}, A_{\text{geo}}, U),
\]

with:

- \(N\): living stock;
- \(A_{\text{act}}\): active abiotic pool;
- \(A_{\text{geo}}\): geological donor;
- \(U\): detritus compartment.

Define the support factor and donor fraction:

\[
s = \frac{A_{\text{act}}}{A_{\text{act}} + A_0},
\qquad
\sigma = \frac{A_{\text{geo}}}{A_{\text{geo}} + A_{g0}},
\]

with \(A_0 > 0\), \(A_{g0} > 0\). With \(A_{g0}>0\) the donor fraction \(\sigma\) is smooth and strictly increasing in the donor level. The registered regime is the separation of scales \(A_{\text{geo}}\gg A_{g0}\), in which \(\sigma\approx1\); the separation is registered rather than assigned a numerical value, and the corner \(A_{g0}=0\) is the discontinuous limit \(\sigma\equiv1\) for \(A_{\text{geo}}>0\), not the registered regime.

Net regeneration and gross uptake are:

\[
R(N,A_{\text{act}}) = rN\left(1 - \frac{N}{K}\right)s,
\]

\[
T = \kappa_A N s,
\]

\[
B = R + T.
\]

Net regeneration is the difference of two non-negative primitives — gross regeneration \(rNs\) (support → stock) and density-dependent return \(rN^2s/K\) (stock → support) — so (2a)–(2d) below stay within the primitive-flux discipline of Section 2.1 despite the signed entry. Where the two primitives must be tracked separately they appear as their own columns of the incidence matrix rather than folded into \(R\).

The donor-limited geo-interface primitives are:

\[
e_{GA} = \omega_A A_{\text{eq,intrinsic}} \sigma,
\]

\[
e_{AG} = \omega_A A_{\text{act}},
\]

\[
C_{A,\lim} = C_A \sigma,
\]

together with detritus return \(\gamma_U U\).

Under the institutional-failure specialization,

\[
\mu = \nu = \rho = 0,
\qquad
C_A = 0,
\]

the product, waste and price parameters of the unreduced ledger — its macroeconomic-feedback, recycling and price-response channels, set to zero together with the mining intensity \(C_A\) — are switched off, and the closed natural block is:

\[
\dot N = R - qEN,
\tag{2a}
\]

\[
\dot A_{\text{act}} = -B + e_{GA} - e_{AG} + \gamma_U U,
\tag{2b}
\]

\[
\dot A_{\text{geo}} = -e_{GA} + e_{AG},
\tag{2c}
\]

\[
\dot U = T - \gamma_U U.
\tag{2d}
\]

Equations (2a)–(2d) are written for the specialization with mining inactive. With mining restored, (2c) reads \(\dot A_{\text{geo}} = -e_{GA} + e_{AG} - C_{A,\lim}\) and the mass identity of Theorem 7 acquires its second export term. The mined fraction routes out of the four-coordinate block; the full-ledger theorems record the mining column as an internal transfer between compartments outside it, which is consistent because the block boundary, not the ledger boundary, is crossed.

Three recharge specifications occur in this article and in the companion analysis, and they are distinct objects:

| Recharge law | Form | Status |
|---|---|---|
| Primitive donor-limited exchange | \(e_{GA}=\omega_A A_{\text{eq,intrinsic}}\sigma\) | the closed block's law: the forward rate depends on the donor alone, not on how empty the receiver is; the rest state is \(A_{\text{act}}=A_{\text{eq,intrinsic}}\sigma\) (Theorem 13) |
| Target-relaxation | \(\omega_A(A_{\text{eq}}-A)\) | admissible only when donor-limited (Theorem 11): run backward at an empty donor it violates the primitive discipline, and it may be used only with the source declared an effectively infinite external reservoir, which makes the system open |
| Working derived target | \(A_{\text{eq},W}=A_{\text{eq,intrinsic}}+\kappa_A K/\omega_A\) | the companion delay-dynamics analysis's working completion; not a closed-block law, and one of the reasons recorded in Section 10.2 for the failure of reduction. No derived target appears in the closed block |

Recharge is donor-limited and cannot run backward: at \(A_{\text{geo}}=0\), \(e_{GA}=0\). Mining \(C_{A,\lim}=C_A\sigma\) is donor-limited in the same sense as extraction. The geological donor is an internal state throughout; no infinite reservoir is declared.

The registered parameterization is \(r=0.02\), \(K=100\), \(q=0.001\), \(\kappa_A=0.05\), \(\omega_A=10^{-3}\), \(A_0=1\), \(A_{\text{eq,intrinsic}}=50\) and \(\gamma_U=0.2\). With \(A_0>0\) and \(A_{g0}>0\) the right-hand side of (2a)–(2d) is locally Lipschitz on the closed orthant, and the comparison \(\dot N\le rN(1-N/K)\), together with \(\dot N\le0\) once \(N\ge K\), bounds the stock by \(\max\{N(0),K\}\). Classical solutions therefore exist globally and remain in the orthant by Theorem 10; that is the sense in which "classical solution" is used throughout.

Harvest routing in the block is the corner \(\alpha=0\) of the routing example below: harvest \(qEN\) exits the natural block entirely as product, and a positive detritus-routed fraction \(\alpha>0\) would add \(\alpha qEN\) to \(\dot U\) and reduce the block export to \((1-\alpha)qEN\). The mass identity of Theorem 7 is stated for the declared routing. The positive-part convention \([\cdot]_+\), read as a one-way valve at a non-positive target, never binds here: the registered intrinsic target is positive.

The four-row block incidence is:

\[
S_{\text{block}} =
\begin{pmatrix}
1 & -1 & -1 & 0 & 0 & 0 & 0 & 0 \\
-1 & 1 & 0 & -1 & 1 & 1 & -1 & 0 \\
0 & 0 & 0 & 0 & 0 & -1 & 1 & -1 \\
0 & 0 & 0 & 1 & -1 & 0 & 0 & 0
\end{pmatrix},
\]

with rows \((N,A_{\text{act}},A_{\text{geo}},U)\) and columns, in order, gross regeneration, density-dependent return, harvest, uptake, detritus return, \(e_{GA}\), \(e_{AG}\) and mining.

Every column is a two-compartment transfer or a block-boundary export. The six internal columns — gross regeneration, density-dependent return, uptake, detritus return, \(e_{GA}\) and \(e_{AG}\) — have column sums \(0\); the two exports, harvest and mining, carry column sums \(-1\) each:

\[
\mathbf{1}^{\top}S_{\text{block}}=\begin{pmatrix}0&0&-1&0&0&0&0&-1\end{pmatrix}.
\]

Summing the rows therefore reads off the mass identity directly; under the specialization \(C_A=0\) mining is inactive and only the harvest term survives:

\[
\dot M = -qEN - C_{A,\lim}.
\]

This is not an assumption. It is a column-sum property of the incidence matrix.

### 2.4 Support saturation: the logistic equation as a readout

**Theorem 1 (Support-saturated logistic stock limit).** Fix \(T<\infty\) and non-negative \(\mu,\delta,c,q\). Assume (H1) \(A_\kappa\) is measurable with \(A_\kappa(t)\ge a_0>0\) and \(0\le X_\kappa(t)\le X_{\max}\), and (H2) \(E\in L^\infty([0,T])\). Let \(X_\kappa\) solve
\[
\dot X_\kappa=\mu X_\kappa\frac{A_\kappa}{\kappa+A_\kappa}-\delta X_\kappa-cX_\kappa^2-qE(t)X_\kappa
\]
and let \(X_0\) solve the limiting equation with the same initial value. Then \(\sup_{0\le t\le T}\lvert X_\kappa(t)-X_0(t)\rvert=O(\kappa)\). If \(\mu>\delta\) and \(c>0\) the limit is the logistic stock equation with extraction,
\[
\dot X_0=rX_0\left(1-\frac{X_0}{K_{\log}}\right)-qEX_0,\qquad r=\mu-\delta,\quad K_{\log}=\frac{\mu-\delta}{c}.
\]
*Proof.* With \(e(t)=\lvert X_\kappa(t)-X_0(t)\rvert\), the saturation defect is \(\bigl\lvert\tfrac{A_\kappa}{\kappa+A_\kappa}-1\bigr\rvert=\tfrac{\kappa}{\kappa+A_\kappa}\le\tfrac{\kappa}{a_0}\), so \(\lvert\dot X_\kappa-\dot X_0\rvert\le L_1\kappa+L_2e(t)\) with \(L_1=\mu X_{\max}/a_0\) and \(L_2=\mu+\delta+2cX_{\max}+q\lVert E\rVert_\infty\), using \(\lvert\mu-\delta\rvert\le\mu+\delta\) and \(c(X_\kappa+X_0)\le2cX_{\max}\); Gronwall's inequality gives \(e(t)\le(L_1/L_2)\kappa(e^{L_2t}-1)\le C_T\kappa\). The bound \(X_\kappa\le X_{\max}\) is satisfiable in the registered family, since \(\dot X_\kappa\le X_\kappa(\mu-\delta-cX_\kappa)\) keeps \(X_\kappa\le\max\{X(0),(\mu-\delta)/c\}\). \(\square\)

**Remark 2 (Registered-family identity).** In the primitive-flux core with \(g=\mu XA/(K_A+A)\), \(m=dX+cX^2\) and \(h=qEX\), the saturated stock equation is, for each fixed interior \(A>0\) as \(K_A\to0\),
\[
\dot X=(\mu-d)X-cX^2-qEX=rX(1-X/K)-qEX,\qquad r=\mu-d,\quad K=(\mu-d)/c,
\]
requiring \(\mu>d\) and \(c>0\). The identity is pointwise on the interior support region and is not uniform through the depleted-pool boundary, since \(A/(K_A+A)=0\) at \(A=0\) for every \(K_A>0\).

The scope of the limit is part of the statement: it does not eliminate \(U\), it does not make \(A\) constant near its boundary, and it does not transform the memory or effort laws. It is an ecological stock-equation identity, not a full-system reduction and not a transfer principle for bifurcation thresholds; bifurcation numbers of the two families do not transfer. A logistic stock equation is therefore a saturated support-pool readout rather than a primitive physical law, and substituting it for stock-support dynamics is legitimate only at interior saturation and only on timescales where the approximation holds.

### 2.5 Mechanism typing

Extraction has at least three distinct physical meanings: standing-stock culling, in which present extraction removes reproductive stock directly; recruitment suppression, in which present use prevents future recruits without immediate removal of adults; and weak viability coupling, in which use has limited or indirect effect on reproduction. In the ledger, standing-stock culling enters as an outflow from the standing-stock compartment. The typing is the physical module's, not the diagnostic's: routing is never determined by diagnostic labels, and a label such as "unsustainable portion" never determines physical destination. Material routing is determined by the typed physical module alone, and a diagnostic threshold that flags a flow has no standing in the incidence matrix.

Where an application splits extraction between standing-stock removal and recruitment suppression, \(C_{\mathrm{stock}}=\psi qEN\) and \(C_{\mathrm{recruit}}=(1-\psi)qEN\) for \(\psi\in[0,1]\), the assignment requires evidence per channel, and the dominant physical mechanism sets it. Two illustrative assignments through a logistic two-channel proxy, stated as calibrated examples and not as constitutive claims for the named domains: soil zinc under crop export, an existing-unit removal, at \(\psi=0.85\), against impaired mineralisation, a replenishment degradation, at \(\psi=0.25\); pollinators under adult mortality at \(\psi=0.70\) against brood failure at \(\psi=0.20\). Across such mechanism pairs the trough depth varies by a factor of about 1.5 from mechanism alone. The mass-routing discipline is the typing made explicit. Harvesting pre-recruit stages is a harvest of existing units, and routes to the product and waste fractions. Habitat-induced failed recruitment is a prevented inflow: routing it into product or waste would create mass that was never in the stock. Damage to the capital stock itself — aquifer compaction, severe soil loss, permafrost-driven ground instability — is not a split-assignment channel at all, but a slow drift in capacity or a transfer to the inert sink.

---

## 3. Certification Layers

### 3.1 Three predicates, separated

The ledger supports three distinct predicates.

**Layer 1: Accounting consistency.**  
The balance law (1) holds almost everywhere on \([0,T]\).

**Layer 2: Conservation consistency.**  
For every declared conserved quantity \(\ell\),

\[
\ell^\top S_T = 0.
\]

**Layer 3: Barrier safety.**  
For declared lower and upper barriers,

\[
\underline{B}_m(t) \le S_m(t) \le \overline{B}_m(t)
\]

for every component \(m\) and every \(t \in [0,T]\), where \(S = Cx\) is the moiety-composition readout.

Layer 2 is structural: it concerns the incidence operator alone. Layers 1 and 3 are trajectory-level: they concern a particular solution \((x,v,b)\).

The logical relations are the content of the next two propositions.

**Numbering convention.** The two layering propositions of this section carry their own counter, Propositions 1 and 2; every other numbered statement runs on a single sequence — Definitions 1–6 and 21–23, Theorems 1–15 and 24, the remaining propositions, the remarks and the corollary — so Proposition 4, Proposition 6, Proposition 17, Proposition 18, Proposition 20 and Propositions 25–32 are main-counter statements rather than further members of the layering counter, and all labels are unique. Four results are stated without a number (*Depletion is compartmental*, *No weighted certification*, *Universal failure of weighted certification*, *Non-reduction*) because they are recorded as boundary statements rather than as entries in the sequence.

**Certification state.** The obligations developed in this section are reported as a vector
\[
\mathrm{Cert}=(\mathsf{Typed},\ \mathsf{Balanced},\ \mathsf{Conserved},\ \mathsf{Positive},\ \mathsf{Admissible},\ \mathsf{Safe},\ \mathsf{Adequate\ service},\ \mathsf{Closed}),
\]
each entry taking one of three values: established, not established, and not applicable to this object. The third value is not a failure and the second is not a refutation. A classification record that establishes an accounting identity and nothing else reports \(\mathsf{Safe}\) as not applicable, not as refuted; a record that establishes every entry except closure is not thereby unsafe. The predicates are separately certified and generally non-equivalent rather than pairwise independent: the implications that hold among them are the ones stated in Propositions 1 and 2 and in the thermodynamic clause of Section 3.3, and an unlisted implication is not available by inference. The proof obligation attached to each entry, and the certificate vectors of the three classified indicators, are tabulated in the supplementary material.

### 3.2 Conservation implies accounting consistency for conserved quantities

**Proposition 1.** If \(\ell^\top S_T = 0\), then

\[
\frac{d}{dt}(\ell^\top x) = \ell^\top b,
\]

and in a closed system, \(b=0\), \(\ell^\top x\) is invariant.

*Proof.*

\[
\frac{d}{dt}(\ell^\top x)
= \ell^\top \dot{x}
= \ell^\top(S_T v + b)
= (\ell^\top S_T)v + \ell^\top b
= \ell^\top b.
\]

\(\square\)

### 3.3 Barrier safety is independent

**Proposition 2.** Barrier safety does not follow from accounting consistency. A trajectory can be perfectly mass-balanced while violating a declared barrier. Conversely, a trajectory can satisfy declared barriers while violating a conservation law or stoichiometric constraint. Thermodynamic admissibility — energy conservation, entropy-production non-negativity, reaction feasibility — implies accounting consistency, but the converse does not hold, and this article establishes the three layers above without claiming the fourth.

*Proof.* On the closed ledger (2), extraction exceeding regeneration is exactly mass-balanced but drives the living stock through any positive lower barrier in finite time. Conversely, a trajectory may remain inside declared barriers while its flux decomposition violates stoichiometric constraints or silently drops a moiety through a yield-routing omission. Thermodynamic admissibility presupposes a mass balance, but a mass-balanced flux decomposition need not satisfy energy or entropy constraints; establishing those requires structure outside the present scope. \(\square\)

The implication for measurement is direct. Mass-balance closure, stoichiometric consistency, and barrier compliance must each be audited separately. An assessment that reports only one of them declares less than it appears to.

### 3.4 Flux-reconstruction identity

**Lemma 3 (Flux reconstruction).** Let \(x:[0,T]\to \mathbb{R}^n_+\) be absolutely continuous with

\[
\dot{x}(t) = S_T v(t) + b(t)
\]

almost everywhere, \(v \in L^1([0,T];\mathbb{R}^J_+)\), \(b \in L^1([0,T];\mathbb{R}^n)\), and \(S = Cx\). Then

\[
S(t) = S(0) + \int_0^t \left(CS_T v(\tau) + Cb(\tau)\right)d\tau.
\]

For continuous barriers, the trajectory satisfies

\[
\underline{B}_m(t) \le S_m(t) \le \overline{B}_m(t)
\]

for all \(t\) if and only if the corresponding integrated inequalities hold.

*Proof.* Integrate

\[
\dot S = C\dot x = C(S_T v + b).
\]

Because \(S_m\) and the barriers are continuous, a pointwise violation is an integrated violation at the same time. \(\square\)

Two cases are distinguished.

If fluxes are prescribed or observed, stock balances are reconstructed by integration without solving the internal constitutive dynamics. This is the simple auditing case.

If fluxes are endogenous, \(v = v(x,u,d)\), flux-only auditing is not generally possible without solving, estimating, or bounding the coupled system. The identity still holds, but the integral cannot be evaluated without determining \(v(t)\).

In both cases, barriers are declared, not computed. Flux data do not derive ecological thresholds, aquifer collapse floors, or concentration limits. The theorem establishes compliance with declared barriers, not derivation of the barriers themselves.

### 3.5 Conservation-law reduction

**Proposition 4 (Conservation-law reduction).** If \(\ell^\top S_T = 0\), then

\[
\ell^\top x(t)
=
\ell^\top x(0)
+
\int_0^t \ell^\top b(\tau)d\tau.
\]

In a closed system, \(\ell^\top x\) is invariant.

*Proof.* Integrate Proposition 1. \(\square\)

A conservation law alone does not imply barrier safety. The set

\[
\{x \ge 0 : \ell^\top x = \ell^\top x(0),\; \underline{B} \le Cx \le \overline{B}\}
\]

may be empty even though each object is separately well-defined. Barrier–conservation compatibility is a feasibility problem, not a slogan.

**Definition 23 (Bounded residual).** Conservation consistency is stated with a declared residual budget. For every left-null vector \(\ell\) of \(S_T\), with \(C\) the readout matrix of Section 2.2,
\[
\Bigl|\int_0^T\ell^{\top}C\,d_x(t)\,dt\Bigr|\ \le\ \epsilon_\ell(T),
\qquad \epsilon_\ell\ \text{declared with the model}.
\]
Proposition 1 then reads \(\ell^{\top}Cx(T)=\ell^{\top}Cx(0)+\int_0^T\ell^{\top}C\,b(t)\,dt\) with the disturbance term carried rather than absorbed, and \(\epsilon_\ell\) is the quantity material-flow reconciliation books as statistical discrepancy. An envelope computed without \(\epsilon_\ell\) supports no barrier certificate once the residual-inflated envelope leaves the declared barriers, and where \(\epsilon_\ell\) is undeclared the conservation predicate is reported as not established rather than assumed at zero.

### 3.6 Flux-bounding envelope theorem

**Theorem 5 (Flux-bounding envelopes).** Assume primitive fluxes and boundary transfers satisfy componentwise bounds:

\[
\underline{v}(t) \le v(t) \le \overline{v}(t),
\qquad
\underline{b}(t) \le b(t) \le \overline{b}(t),
\]

for all \(t \in [0,T]\). For any matrix \(A\), write \(A^+ = \max\{A,0\}\) and \(A^- = \max\{-A,0\}\) entrywise. For each moiety \(m\), define

\[
\varphi_m(\tau)
=
(CS_T)^+_m \underline{v}(\tau)
-
(CS_T)^-_m \overline{v}(\tau)
+
C^+_m \underline{b}(\tau)
-
C^-_m \overline{b}(\tau),
\]

\[
\psi_m(\tau)
=
(CS_T)^+_m \overline{v}(\tau)
-
(CS_T)^-_m \underline{v}(\tau)
+
C^+_m \overline{b}(\tau)
-
C^-_m \underline{b}(\tau).
\]

Define the envelopes

\[
\underline{S}_m(t)
=
S_m(0)
+
\int_0^t \varphi_m(\tau)d\tau,
\]

\[
\overline{S}_m(t)
=
S_m(0)
+
\int_0^t \psi_m(\tau)d\tau.
\]

Then

\[
S_m(t) \in [\underline{S}_m(t), \overline{S}_m(t)]
\]

for all \(t \in [0,T]\) and all \(m\).

*Proof.* By Lemma 3,

\[
\dot S_m = (CS_T v + Cb)_m.
\]

For each row \(m\) and time \(\tau\), the expression \((CS_T)_m v\) is linear in \(v\). Over the box \([\underline{v},\overline{v}]\), its minimum and maximum are attained at the box extremes, giving

\[
(CS_T)^+_m \underline{v}
-
(CS_T)^-_m \overline{v}
\le
(CS_T)_m v
\le
(CS_T)^+_m \overline{v}
-
(CS_T)^-_m \underline{v}.
\]

The same argument applies to \(C_m b\). Adding gives

\[
\varphi_m(\tau) \le \dot S_m(\tau) \le \psi_m(\tau).
\]

Integrating over \([0,t]\) gives the envelope. \(\square\)

**Corollary (Flux-derived barrier certificate).** If

\[
\underline{S}_m(t) \ge \underline{B}_m(t),
\qquad
\overline{S}_m(t) \le \overline{B}_m(t),
\]

for all \(t\) and all \(m\), then every trajectory compatible with the flux bounds is barrier-safe on \([0,T]\).

*Proof.* By Theorem 5, every compatible trajectory satisfies

\[
\underline{S}_m \le S_m \le \overline{S}_m.
\]

The certificate conditions sandwich \(S_m\) between the barriers. \(\square\)

Two qualifications belong to the theorem.

Two qualifications are part of the theorem. The bounds are conservative: they hold for all flux selections in the declared boxes, including selections not jointly realizable by the coupled dynamics, so the certificate may fail where a trajectory with jointly realizable fluxes would pass, and attainability requires solving or bounding the coupled system. And when \(v=v(x)\) is state-dependent, the declared box must additionally be forward-invariant under the coupled dynamics for the envelopes to bound the reachable set; without it the corollary certifies flux-admissible paths only, not the trajectories of the differential equation. The envelope is an interval computation on the flux data, not a forecast: it says nothing about what the fluxes will be, only what every admissible path implies for the stock. Row indices in the display are rows of the matrices \((CS_T)^+\), \((CS_T)^-\), \(C^+\) and \(C^-\).

Stoichiometric and donor-limit constraints make the jointly admissible selections a polytope rather than a box; the tight certificate is the linear programme over that polytope, and the box envelope above is its auditing relaxation — the box is what is audited, the polytope what is realizable. The envelope is the interval-arithmetic counterpart, at the level of declared flux bounds, of the data-reconciliation practice of material flow analysis (Brunner and Rechberger, 2004): reconciliation solves unmeasured fluxes under an imposed mass balance, and the envelope bounds them without solving them.

**Worked envelope on the closed block.** On (2a)–(2d) with declared boxes \(N\in[0,K]\) and \(E\in[0,E_{\max}]\), the mass row gives
\[
\dot M=-qEN-C_{A,\lim}\in\bigl[-(qE_{\max}K+C_A),\,0\bigr],\qquad
M(t)\in\bigl[M(0)-(qE_{\max}K+C_A)t,\;M(0)\bigr].
\]
The conservatism is visible in the extremes: maximal extraction \(qE_{\max}K\) is realizable only at \(N=K\), where regeneration vanishes, and maximal recharge coincides with minimal extraction — box extremes the coupled dynamics cannot realize jointly.

The envelope is an interval computation on flux data, not a forecast. It says nothing about what the fluxes will be. It says what every admissible flux path implies for the stock.

Stoichiometric and donor-limit constraints make the jointly admissible flux selections a polytope rather than a box. The tight certificate is the linear programme over that polytope. The box envelope is its auditing relaxation.

### 3.7 Finite exhaustion under uniform drift

**Proposition 6.** In this proposition \(S\) is a scalar readout of the declared moiety, with \(C\) the identity composition on that moiety, and \(\underline B\) is a constant lower barrier. Assume \(S\) is absolutely continuous, \(S(0) > \underline{B}\), and

\[
\dot S(t) \le -\varepsilon < 0
\]

whenever \(S(t) > \underline{B}\), with \(\varepsilon > 0\). Then the first hitting time satisfies

\[
\tau_{\underline{B}}
=
\inf\{t \ge 0 : S(t) \le \underline{B}\}
\le
\frac{S(0) - \underline{B}}{\varepsilon}.
\]

*Proof.* While \(S(t) > \underline{B}\), integration gives

\[
S(t) \le S(0) - \varepsilon t.
\]

The right-hand side reaches \(\underline{B}\) at \(t = (S(0)-\underline{B})/\varepsilon\). By continuity, the crossing occurs no later. \(\square\)

Proportional extraction, by contrast, satisfies the hypotheses for every positive barrier and still misses zero: the stock approaches zero asymptotically, so the time to the zero barrier is infinite. The claim that positive extraction implies finite exhaustion is therefore false at \(\underline B=0\), and every exhaustion statement must name its referent.

**Counterexample (proportional extraction).** For

\[
\dot S = -kS,
\qquad k > 0,
\qquad S(0)>0,
\]

the solution is

\[
S(t) = S(0)e^{-kt} > 0
\]

for every finite \(t\). The stock approaches zero asymptotically and is never exhausted in finite time. The claim that positive extraction implies finite exhaustion is therefore false.

**Proposition (Depletion is compartmental).** On a closed typed ledger, the total mass of each conserved moiety is invariant along trajectories. Every finite hitting time of a zero readout is the hitting time of a compartment or of a barrier on a readout, never of total mass.

This fixes the boundary discipline: depletion is not loss of matter. It is loss of access to matter in the form and place that supports the service in question.

---

## 4. The Closed Finite-Donor Ledger

The closed finite-donor ledger satisfies a complete qualitative portrait. The theorem set is stated here in sequence.

### 4.1 Natural-block mass identity

**Theorem 7.** Let

\[
M = N + A_{\text{act}} + A_{\text{geo}} + U.
\]

Along every trajectory of the closed natural block (2), with optional mining restored,

\[
\dot M = -qEN - C_{A,\lim}.
\]

Under the institutional-failure specialization, \(C_A = 0\),

\[
\dot M = -qEN.
\]

*Proof.* Sum the four equations of (2):

\[
\dot M
=
(R-qEN)
+
(-B+e_{GA}-e_{AG}+\gamma_U U)
+
(-e_{GA}+e_{AG}-C_{A,\lim})
+
(T-\gamma_U U).
\]

Internal terms cancel:

\[
R - B + T = R - (R+T) + T = 0.
\]

What remains is

\[
\dot M = -qEN - C_{A,\lim}.
\]

\(\square\)

### 4.2 Stoichiometric conservation

**Theorem 8.** Let \(X\) collect the mass compartments of one resource system and let \(S_T\) be the incidence matrix of its flux ledger. Under unit-sum routing constraints,

\[
\dot X = S_T F(X),
\]

and

\[
\frac{d}{dt}\mathbf{1}^\top X = 0.
\]

*Proof.* Every primitive is a transfer between two compartments, or a pair of opposite primitives implementing a two-way exchange. The corresponding column of \(S_T\) has entries \(+1\) and \(-1\) in the receiving and donating rows and zeros elsewhere. Routing tensors are column-stochastic by construction. Hence

\[
\mathbf{1}^\top S_T = 0,
\]

and therefore

\[
\mathbf{1}^\top \dot X = \mathbf{1}^\top S_T F = 0.
\]

\(\square\)

Conservation is structural. It is read from the columns of the incidence matrix, and it is exact under the routing constraints on a state vector that includes the product, waste and inert compartments: harvest and mining are internal transfers of the full ledger and exports of the natural block, which is why Theorem 7 records a nonzero right-hand side while this theorem records zero.

### 4.3 Six-compartment conservation

For one conserved limiting material the scaffold can be instantiated as six compartments \((X,U,A,G,P,W)\) — living stock, detritus, active abiotic pool, geological pool, product and waste — with eight non-negative primitives: assimilation \(g\) from \(A\) to \(X\), mortality \(m\) from \(X\) to \(U\), harvest \(h\) from \(X\) to \(P\), decomposition \(d_U\) from \(U\) to \(A\), the two-way geological exchange \(e_{GA}\) and \(e_{AG}\) between \(G\) and \(A\), direct mining \(c_G\) from \(G\) to \(P\), and product retirement \(r_P\) from \(P\) to \(W\), split by a declared fraction \(\rho_P\). The constant splits \(\alpha,\rho_P\), the compartment set and the absorbing-sink convention are declared choices of the example, and the construction is a monomaterial projection: recovery claims require \(U\) and \(P\) split by material, location and grade with declared yields and residual routes.

**Theorem 9.** *For the six-compartment system, \(\mathbf{1}^{\top}\dot z=0\): the total material mass \(M_6=X+U+A+G+P+W\) is constant along every trajectory on which the classical solution is defined.* *Proof.* Each primitive is a two-compartment transfer, so every column of the incidence matrix carries one \(+1\) and one \(-1\) and \(\mathbf{1}^{\top}S(\alpha,\rho_P)v=0\) column by column: \(g-g=0\), \(-m+m=0\), \(-d_U+d_U=0\), \(e_{GA}-e_{GA}=0\), \(-e_{AG}+e_{AG}=0\), \(-c_G+c_G=0\), \(-h+\alpha h+(1-\alpha)h=0\), and \(\rho_Pr_P-r_P+(1-\rho_P)r_P=0\). The argument applies to the expanded typed incidence system when quality grades are split, and not automatically to an undifferentiated quality-neutral loop. Open systems are explicit: imports, exports, atmospheric losses and cross-boundary transport enter as typed boundary fluxes giving \(\dot M_6=I_\partial-O_\partial\), which is preferable to preserving a nominal invariant by allowing an unobserved or finite donor compartment to become negative. \(\square\)

The four-block system (2a)–(2d) is not a specialization of this scaffold: in the scaffold assimilation \(g\) is a slow \(A\to X\) flux and mortality \(m\) a slow \(X\to U\) flux, while in (2a)–(2d) the uptake \(T\) transfers \(A_{\text{act}}\to U\) with the living stock catalytic and no separate mortality primitive. The two are different timescale lumpings of the same physical story, and no incidence specialization maps one onto the other. Theorems 7–9 are three instances of Proposition 1 with \(\ell=\mathbf{1}\), differentiated only by which compartments the declaration includes.

### 4.4 Orthant invariance

**Theorem 10.** The nonnegative orthant in \((N,A_{\text{act}},A_{\text{geo}},U)\) is forward invariant for the closed natural block (2).

*Proof.* The right-hand side is locally Lipschitz on a neighbourhood of the closed orthant. Check each face.

On \(A_{\text{geo}}=0\), \(\sigma=0\), hence \(e_{GA}=0\), and

\[
\dot A_{\text{geo}} = e_{AG} = \omega_A A_{\text{act}} \ge 0.
\]

On \(A_{\text{act}}=0\), \(s=0\), so

\[
R = B = T = e_{AG} = 0,
\]

and

\[
\dot A_{\text{act}} = e_{GA} + \gamma_U U \ge 0.
\]

On \(N=0\), extraction and uptake vanish and \(\dot N = 0\).

On \(U=0\),

\[
\dot U = T \ge 0.
\]

By Nagumo’s inward-pointing criterion, the orthant is forward invariant. \(\square\)

The donor-limitation condition is the exact sufficiency requirement. Algebraic cancellation alone does not establish invariance.

**Theorem 11 (Orthant invariance of the general closed block).** *For the general closed block in which every primitive outflow of a compartment vanishes when that compartment is empty — including a two-way exchange \(e_i=k_i\Pi_i\Pi_{1i}x_i\) and a donor-scaled \(e_{GA}\) — the non-negative orthant is forward invariant. A target-relaxation law \(e_{GA}=\omega(A_{\mathrm{eq}}-A)\) does not satisfy the donor boundary assumption unless it is also limited by the donor stock; it may be used only with the source declared an effectively infinite external reservoir, in which case the system is open rather than closed.* *Proof.* On the face \(x_1=0\) every primitive out of \(x_1\) vanishes, so \(\dot x_1=\sum_i k_i\Pi_i\Pi_{1i}x_i+\omega_A A_{\mathrm{eq,intrinsic}}\sigma\ge0\). On the face \(x_2=0\) with a single non-empty donor, the exchange inflow is donor-scaled and \(\dot x_2\ge0\), vanishing only if the declared exchange fraction is zero, which is a decoupled transfer. In both cases this is the inward-pointing (Nagumo) condition on each face; a target-relaxation law violates it because it changes sign at an empty donor, the inadmissible case recorded in the recharge-law table of Section 2.3. The classical lineage is the compartmental-systems non-negativity theory, including donor-limited Michaelis–Menten uptake and outflow vanishing at the donor (Jacquez and Simon, 1993); the donor-limitation condition is the exact sufficiency requirement, and algebraic cancellation alone does not establish invariance. \(\square\)

### 4.5 No interior rest at positive effort

**Theorem 12.** Assume \(E \equiv E^* > 0\) is constant. Rest points are sought in the closed orthant with \(N^*>0\), so the boundary branches must be excluded by the flow rather than by interiority. Then a rest point of the closed natural block satisfies

\[
R + C_{A,\lim} = 0.
\]

With \(C_A = 0\), this is \(R=0\), hence

\[
N=0, \quad \text{or} \quad N=K, \quad \text{or} \quad A_{\text{act}}=0.
\]

None of these is compatible with \(E^*>0\) and \(N^*>0\).

*Proof.* At a rest point, \(\dot U=0\) forces

\[
\gamma_U U = T.
\]

Adding \(\dot A_{\text{act}} + \dot A_{\text{geo}}\) gives

\[
-B + \gamma_U U - C_{A,\lim} = 0.
\]

With \(\gamma_U U = T\) and \(B=R+T\), this becomes

\[
R + C_{A,\lim} = 0.
\]

With \(C_A=0\), \(R=0\). From

\[
R = rN\left(1-\frac{N}{K}\right)s,
\]

this implies \(N=0\), \(N=K\), or \(s=0\), i.e. \(A_{\text{act}}=0\).

Each branch is excluded at positive effort:

- If \(N=K\) and \(E^*>0\), then \(\dot N = -qE^*K < 0\).
- If \(A_{\text{act}}=0\) and \(A_{\text{geo}}>0\), then \(\dot A_{\text{act}} > 0\).
- If \(N=0\), then \(R=T=0\), reducing to the extinction family.

Thus no interior rest point exists at positive effort. \(\square\)

### 4.6 Vanishing-extraction rest set

**Theorem 13.** With \(E \equiv 0\), the rest points of the closed natural block are exactly

1. the extinction family \(\mathcal{R}_{\text{ext}}\);
2. the carrying-capacity family \(\mathcal{R}_K\);
\(\mathcal{R}_{\text{ext}}\cup\mathcal{R}_K\), together with the frozen-biomass face \(\mathcal{R}_{\text{frozen}}\). The families are not disjoint: the origin lies in \(\mathcal{R}_{\text{ext}}\) and in \(\mathcal{R}_{\text{frozen}}\), and \((K,0,0,0)\) lies in \(\mathcal{R}_K\) at \(A_{\text{geo}}=0\) and in the frozen face. They are:

\[
\mathcal{R}_{\text{ext}}
=
\{N=0,\; U=0,\; A_{\text{act}} = A_{\text{eq,intrinsic}}\sigma(A_{\text{geo}}),\; A_{\text{geo}} \ge 0\},
\]

\[
\mathcal{R}_K
=
\{N=K,\; U = \kappa_A K s/\gamma_U,\; A_{\text{act}} = A_{\text{eq,intrinsic}}\sigma(A_{\text{geo}}),\; A_{\text{geo}}\ge0\},
\qquad(\text{$s$ evaluated at the solution}),
\]

and

\[
\mathcal{R}_{\text{frozen}}
=
\{(N,0,0,0): N \ge 0\}.
\]

*Proof.* With \(E=0\), set the four derivatives to zero.

From \(\dot A_{\text{geo}}=0\),

\[
e_{GA}=e_{AG},
\]

so

\[
A_{\text{act}} = A_{\text{eq,intrinsic}}\sigma.
\]

From \(\dot N = R = 0\),

\[
rN\left(1-\frac{N}{K}\right)s = 0.
\]

If \(A_{\text{geo}}>0\), then \(A_{\text{act}}>0\), so \(s>0\), and \(N=0\) or \(N=K\).

At the boundary \(A_{\text{geo}}=0\), the geo-balance forces \(A_{\text{act}}=0\), hence \(s=0\), and \(\dot N=0\) for every \(N \ge 0\). With \(U=0\), the remaining equations vanish. This is the frozen-biomass face.

From \(\dot U=0\),

\[
U = T/\gamma_U.
\]

This vanishes in the \(N=0\) branch and is positive in the \(N=K\) branch. Apart from the frozen-biomass face, no rest point exists away from extinction or carrying capacity. If \(A_{g0}=0\) and \(\sigma\equiv1\) are imposed for \(A_{\text{geo}}>0\), the shared active-pool ray of both families is \(A_{\text{act}}=A_{\text{eq,intrinsic}}\) with \(A_{\text{geo}}>0\), and the endpoint \(A_{\text{geo}}=0\) is excluded because there the donor-limited recharge vanishes and \(\dot A_{\text{act}}=-\omega_AA_{\text{eq,intrinsic}}<0\). The constitutive laws of this section carry no basal mortality independent of the support factor; adding one, a stock-to-detritus flux \(\mu_{\mathrm{basal}}N\), collapses the frozen-biomass face and leaves Theorems 7–12 and 14 unchanged. With \(E>0\) constant the extinction family persists as a boundary rest, since \(qEN\) vanishes identically at \(N=0\), while no interior rest exists by Theorem 12; the institutional memory can therefore yield \(E\to E^*\) at \(N=0\) with extraction vanishing identically. \(\square\)

### 4.7 Extraction integrability

**Theorem 14.** Assume \(E(s) \ge 0\) along the trajectory, where \(s\) is a dummy integration variable and not the support factor of Section 2.3. Let

\[
M = N + A_{\text{act}} + A_{\text{geo}} + U.
\]

Then

\[
M(t)
=
M(0)
-
\int_0^t qE(s)N(s)\,ds
\ge 0.
\]

Therefore

\[
\int_0^\infty qE(s)N(s)\,ds \le M(0) < \infty.
\]

In particular,

\[
qEN \in L^1(0,\infty).
\]

*Proof.* By Theorem 7,

\[
M(t) = M(0) - \int_0^t qE(s)N(s)\,ds.
\]

By Theorem 10, \(M(t)\ge 0\). Hence the improper integral is bounded above by \(M(0)\). \(\square\)

This is the depletion-horizon semantics of the closed ledger in its strongest form: the donor budget is finite and extraction is integrable against it. In particular no trajectory maintains extraction at the working value \(qE^*N^*\approx0.187\) for all time (Section 10.2), and with mining restored the same argument bounds \(\int_0^\infty(qEN+C_{A,\lim})\,ds\) by \(M(0)\). A constant extraction flux \(c>0\) exhausts the budget in finite time, with \(M\) reaching its lower bound no later than \(M(0)/c\). The constant flux is a comparison flux only, not a donor-limited primitive the ledger's discipline admits as a sustained law. Proportional extraction \(qEN\) need not drive \(M\) to zero in finite time: the integral bound is the whole statement, and the hitting time of \(M=0\) may be infinite. The theorem does not select among the vanishing-extraction rests of Theorem 13; the \(L^1\) bound alone decides nothing between them. This finite-budget fact is the long-time obstruction recorded in Section 10.2.

A constant extraction flux \(c>0\) exhausts the budget in finite time. Proportional extraction \(qEN\) need not drive \(M\) to zero in finite time. The integral bound is the whole statement.

### 4.8 The conditional hybrid moiety balance, and the limit of cancellation

**Theorem 15 (Conditional hybrid moiety balance).** Let \(\chi\) denote the hybrid state and \(\eta\ge0\) its primitive fluxes, letters chosen so that \(r\) retains the growth-rate meaning of Section 2.3 and \(\nu\) remains a macroeconomic parameter of the unreduced ledger. Assume (H1) \(\chi\) is absolutely continuous between locally finite event times, with left and right limits at each event; (H2) \(\dot\chi=S\eta+b\) with \(\eta\ge0\), separate reverse columns for two-way exchange, and donor-limited negative boundary flows; and (H3) \(L^{\top}S=0\). Then
\[
L^{\top}\chi(t)-L^{\top}\chi(0)=\int_0^tL^{\top}b\,ds+\sum_{t_k\le t}L^{\top}\bigl[\chi(t_k^+)-\chi(t_k^-)\bigr].
\]
*Proof.* Integrate between events and telescope the jumps. \(\square\)

The theorem is conditional, and its jump interpretation is part of the content: an internal-transformation jump requires \(L^{\top}(\chi^+-\chi^-)=0\) or a jump incidence factorization with left-kernel conservation, while a boundary-crossing jump is a boundary impulse and belongs in the boundary term. Two obligations ride the statement. The yield-routing obligation: a transformation represented with yield below one must route the omitted fraction to a represented compartment or a declared boundary flow, or the balance holds only after silently dropping that moiety from \(L\). The separation obligation: this is the hybrid variant of Proposition 4, retained at its own conditional status, and the two statements are not merged.

**Cancellation is cheap.** Summing the six material equations of the ten-state admissibility template of the supplementary material gives the exact identity \(\tfrac{d}{dt}(\bar X_A+X_J+P+U+A+G)=0\). This is an algebraic cancellation only: it does not prove forward invariance of the six material states or physical admissibility of every term. The ghost-sink check is part of the discipline — the birth-transfer rate \(gB\) enters \(\dot X_J\) and \(\dot A\) with opposite signs, so material not transferred to juveniles remains in \(A\) and no unmodelled sink absorbs it — and the check passes while the same template fails elsewhere, because its geological exchange is not donor-limited. Conservation (Theorems 7–9) and positivity (Theorems 10–11) are proved separately in every well-posed ledger of this article, exactly because cancellation is cheap and admissibility is not. The template's remaining negative witnesses — a variance closure not realizable by a non-negative spatial distribution, and an output functional without a displayed state equation — are recorded in the supplementary material as audited admissibility failures.

**Theorem 24 (Critical-margin budget).** Let the declared barrier margins be affine, \(m(x)=Gx+a\ge0\), and let the delivered service rate be \(y=c^{\top}v\) with \(c\ge0\). Suppose some \(\lambda\ge0\) satisfies \(\lambda^{\top}GS_T+c^{\top}\le0\) componentwise, with \(\lambda_j\) carrying the units that convert margin \(j\) into cumulative service. Then \(V=\lambda^{\top}m(x)\) obeys \(\dot V\le-y+\lambda^{\top}Gb\) along every admissible trajectory, and for every trajectory that remains inside the declared barriers
\[
\int_0^Ty(t)\,dt\ \le\ V(x(0))+\int_0^T\lambda^{\top}Gb(t)\,dt .
\]
If additionally \(y\ge y_{\mathrm{req}}\) and \(\lambda^{\top}Gb\le\beta<y_{\mathrm{req}}\), then \(T\le V(x(0))/(y_{\mathrm{req}}-\beta)\).

*Proof.* \(\dot V=\lambda^{\top}G(S_Tv+b)=(\lambda^{\top}GS_T)v+\lambda^{\top}Gb\le-c^{\top}v+\lambda^{\top}Gb\) since \(v\ge0\); integrate and use \(V(T)\ge0\), which holds because \(m\ge0\) and \(\lambda\ge0\). \(\square\)

The search for \(\lambda\) is a linear programme, and its infeasibility is no evidence of safety: it certifies only that this multiplier family does not close. The theorem bounds how long adequate service can coexist with componentwise safety; it is not a scalar certificate, and \(V>0\) establishes nothing about the sign of any individual margin. Theorem 14 is the single-margin instance, and the one-way valve of Section 2.3 is the instance with \(b=0\).

**The closed-ledger portrait.** Theorems 7–14 assemble into a complete qualitative portrait of the closed orthant: conservation (Theorems 7–9), positivity (Theorems 10–11), no interior rest at positive effort (Theorem 12), the two-family vanishing-extraction rest set with the frozen-biomass face (Theorem 13), and the finite donor budget (Theorem 14). The portrait is the source object handed to the interface of Section 10: the closed system's candidate long-time set is the rest set of Theorem 13, and the budget of Theorem 14 bounds how long any positive-flux configuration can persist. A "balanced" closed ledger is thus a finite-budget object, and any sustained extraction against it must integrate to a quantity no greater than the initial budget.

---

## 5. Service Readouts and the Componentwise Deficit

Services are observations or feasible outputs of the physical state. They are not additional conserved mass.

### 5.1 Service readout and contemporaneous balance

For services indexed by \(i=1,\ldots,n\), write

\[
s_i(t) = O_i(x(t),u(t),\theta),
\]

where \(u\) denotes admissible operating or extraction choices. The service \(s_i\) and the demand \(d_i\) share service-specific units.

The contemporaneous component balance is

\[
b_i(t) = s_i(t) - d_i(t).
\]

The condition \(b_i(t)\ge 0\) means measured supply meets measured demand for component \(i\) at that instant.

It does not by itself imply sustainability. A stock can meet current demand while declining toward a threshold. A stock below a desired level can have a positive current balance while recovering.

### 5.2 Feasible balance domain

**Definition 1.** For an admissible operating set \(\mathcal{U}(x,t)\) and a declared demand set \(\mathcal{D}(t)\), the feasible balance domain is

\[
\mathcal{B}(x,t)
=
\{O(x,u,\theta)-d : u \in \mathcal{U}(x,t),\; d \in \mathcal{D}(t)\}.
\]

The geometry of \(\mathcal{B}(x,t)\) is state-dependent. No unrestricted scalar argument can replace an application-specific analysis of this domain.

### 5.3 Support provenance

Current service adequacy and regenerative feasibility are different claims.

Let \(\Gamma_{\text{all}}(x,t)\) contain service vectors feasible through all admitted pathways. Let \(\Gamma_{\text{reg}}(x,t)\subseteq \Gamma_{\text{all}}(x,t)\) be the feasible set after imposing declared regenerative-flow, boundary, material-quality, and energy or capacity restrictions.

**Definition 2.** Assume \(0 \in \Gamma_{\text{reg}}(x,t)\). For a nonzero service direction \(\bar{s}\ge 0\), define

\[
\alpha_{\text{reg}}(\bar{s};x,t)
=
\sup\{\alpha \in [0,1] : \alpha \bar{s} \in \Gamma_{\text{reg}}(x,t)\}.
\]

The vector

\[
(1-\alpha_{\text{reg}})\bar{s}
\]

is the directional support gap, measured in the same service units as \(\bar{s}\).

A realized service \(s \in \Gamma_{\text{all}}\setminus \Gamma_{\text{reg}}\) is support-dependent under that declaration even when \(s \ge d\).

### 5.4 Specialization identity

On the single-resource specialization,

\[
\dot N = R(N,A) - qEN.
\]

Therefore

\[
qEN - R(N,A) = -\dot N,
\]

and

\[
\Lambda(t) := [qEN - R]_+ = [-\dot N]_+.
\]

This identity is the exact shared object used in the interface with institutional delay dynamics.
**Remark 16 (Exact specialization deficit identity).** On every trajectory of the specialized system (\(\mu=\nu=\rho=0\), \(C_A=0\)), and of every reduced system whose stock equation is \(\dot N=R-qEN\),
\[
\Lambda(t):=\bigl[qE(t)N(t)-R(N(t),A_{\text{act}}(t))\bigr]_+=\bigl[-\dot N(t)\bigr]_+.
\]
*Proof.* The stock equation gives \(qEN-R=-\dot N\) identically; taking the positive part of both sides proves the claim. \(\square\)

The identity does not hold on the general ledger, where the deficit is the diagnostic \(C(t)-\hat M^{\top}S(t)\) and need not equal \(-\dot N\): the collapse of the deficit to the stock-decline rate is a property of the specialization, not a definition of liquidation. In the registered delay family the depletion-pressure input \(\Lambda=\max\{0,qEN-R\}\) is therefore a smoothed stock-decline rate and not a scarcity signal: it vanishes at the saturated rest \(R=qEN\) with \(N>0\), and it vanishes at the extinction face because the extraction flux vanishes there.

---

**Proposition 25 (Accumulated liquidation certified by delivered service).** Let the support pool obey \(\dot A=r-c\), and let the declared production relation require at least \(\alpha\ge0\) units of support use per unit of delivered service, \(c(t)\ge\alpha Y(t)\). Then
\[
A(0)-A(T)\ \ge\ \alpha\int_0^TY(t)\,dt-\int_0^Tr(t)\,dt .
\]
Where the right-hand side is positive, the delivered service certifies that much support liquidation, whatever the interior allocation of fluxes.

*Proof.* \(A(0)-A(T)=\int_0^T(c-r)\,dt\ge\alpha\int_0^TY\,dt-\int_0^Tr\,dt\). \(\square\)

The statement is falsifiable against the record rather than self-sealing: a stock change smaller than the certified lower bound exposes a wrong coefficient, a missing flux, or a measurement inconsistency, and each of the three is a registered obligation, not a licence to reconcile. The coefficient \(\alpha\) is a declared relation, not an estimate; the proposition is conditional on it and is not computed anywhere in this article.

## 6. Depletion Arithmetic

The ledger supplies the net derivative needed to distinguish gross throughput from net decline and from a model-conditioned threshold time. The distinction matters because “time to depletion” is used publicly as if all three quantities were one. They are not.

Let \(A_{\min}\) be a declared threshold for the active pool, with \(A > A_{\min}\).

### 6.1 Three non-interchangeable quantities

**Definition 3 (Gross turnover intensity).** With assimilation \(g(X,A)>0\), define

\[
J_A^{\text{gross}} = \frac{g(X,A)}{A},
\]

and the gross support-coverage ratio

\[
H_A^{\text{gross}} = \frac{A-A_{\min}}{g(X,A)}.
\]

Neither is a time to depletion. The implication

\[
g>0 \Rightarrow \dot A < 0
\]

is false in general. At an interior steady state, \(g\) can be positive while decomposition and geological transfer balance it exactly, giving \(\dot A=0\). Gross uptake measures throughput or dependency. Net depletion is a balance property.

**Definition 4 (Local net-depletion ratio).**

\[
H_A^{\text{loc}}(t)
=
\frac{A(t)-A_{\min}}{[-\dot A(t)]_+},
\]

with the convention

\[
H_A^{\text{loc}} = +\infty
\]

when \(\dot A \ge 0\).

This ratio freezes the current net rate. If fluxes change with \(A\), policy, climate, prices, or other states, the realized threshold time can differ substantially.

**Definition 5 (Scenario-conditioned hitting time).** For a fully specified dynamical model, policy or scenario \(\pi\), disturbance history \(d\), and initial state \(x_0\),

\[
T_A(x_0;\pi,d)
=
\inf\{t \ge 0 : A_{\pi,d}(t;x_0) \le A_{\min}\},
\]

with \(T_A=+\infty\) if the threshold is never reached.

The three quantities answer different questions:

| Quantity | Question answered |
|---|---|
| \(J_A^{\text{gross}}, H_A^{\text{gross}}\) | How strongly does the system depend on the pool at the current gross rate? |
| \(H_A^{\text{loc}}\) | If the current net decline were frozen, what is the local stock-to-rate ratio? |
| \(T_A\) | Under a stated model, policy, and scenario, when is the threshold first reached? |

They share units. They do not share a measurand.

### 6.2 Uniform-drift bounds

**Proposition 17.** Assume \(A:[0,T]\to \mathbb{R}\) is absolutely continuous with \(A(0)>A_{\min}\). Let \(v_0>0\), \(0<\varepsilon<1\), and

\[
H_0 = \frac{A(0)-A_{\min}}{v_0}.
\]

Assume

\[
T \ge \frac{H_0}{1-\varepsilon},
\]

and

\[
(1-\varepsilon)v_0 \le -\dot A(t) \le (1+\varepsilon)v_0
\]

for almost every \(t\) while \(A\) remains above \(A_{\min}\). Then a first crossing time \(H\) exists no later than \(H_0/(1-\varepsilon)\), and

\[
\frac{H_0}{1+\varepsilon}
\le
H
\le
\frac{H_0}{1-\varepsilon}.
\]

Moreover,

\[
|H-H_0|
\le
\frac{\varepsilon}{1-\varepsilon}H_0.
\]

*Proof.* If no crossing occurs before

\[
t^* = \frac{H_0}{1-\varepsilon},
\]

then

\[
A(t^*) \le A(0) - (1-\varepsilon)v_0 t^* = A_{\min},
\]

a contradiction. Hence \(H \le t^*\). Integrating both rate bounds over \([0,H]\) and using

\[
A(0)-A(H)=v_0H_0
\]

gives the two-sided bracket. \(\square\)

This is a local diagnostic. It fails when depletion reverses, when the rate approaches zero, or when feedback moves the trajectory outside the declared rate bounds.

**Proposition 26 (Sign of the frozen-rate error).** Let \(\dot A=-\varphi(A)\) with \(\varphi>0\) on \((A_{\min},A_0]\), and write the true horizon and the frozen-rate ratio as
\[
T=\int_{A_{\min}}^{A_0}\frac{dA}{\varphi(A)},
\qquad
H^{\mathrm{loc}}=\frac{A_0-A_{\min}}{\varphi(A_0)} .
\]
If \(\varphi\) is nondecreasing in \(A\) then \(T\ge H^{\mathrm{loc}}\), and the frozen-rate number is conservative. If \(\varphi\) is nonincreasing in \(A\) then \(T\le H^{\mathrm{loc}}\), and it is optimistic.

*Proof.* Nondecreasing \(\varphi\) gives \(\varphi(A)\ge\varphi(A_0)\) for \(A\le A_0\), hence \(T\ge(A_0-A_{\min})/\varphi(A_0)\); the second case reverses the inequality. The comparison is the standard one for one-dimensional monotone dynamics (Smith, 1995). \(\square\)

Proportional extraction is the first case, with \(T=q^{-1}\ln(A_0/A_{\min})\) against \(H^{\mathrm{loc}}=(A_0-A_{\min})/(qA_0)\); at \(A_{\min}=0\) the two disagree by being infinite against finite. The sign is estimable from the data the classification already requires, by regressing the decline rate on the stock; it is declared, not computed, in Sections 8.1 and 8.2.

**Proposition 27 (Curvature correction).** On the barrier distance \(u=A-A_{\min}\), let \(\dot u=-\varphi(u)\) and define the dimensionless curvature number
\[
\kappa=\frac{u\,\ddot u}{\dot u^{2}}=\frac{u\,\varphi'(u)}{\varphi(u)} .
\]
For the power-law family \(\varphi(u)=cu^{p}\) one has \(\kappa=p\) identically, and for \(\kappa<1\)
\[
T=\frac{H^{\mathrm{loc}}}{1-\kappa},
\qquad
T<\infty\iff\kappa<1,
\]
while for \(\kappa\ge1\) the integral diverges at the barrier and the family reaches it only asymptotically, so the frozen-rate ratio understates by an unbounded factor. Constant extraction is \(\kappa=0\), where the frozen-rate ratio is exact; stock-proportional decline is \(\kappa=1\), where the true horizon is infinite against a finite ratio; and \(\kappa=\tfrac12\) doubles the horizon exactly, which is the smallest correction with a real effect. The correction is a one-number statement about the bias, and it inherits its input requirement: \(\kappa\) needs \(\ddot u\), which is a second difference of the same noisy series whose first difference the classification already distrusts, so it is reported as declared or not at all. Where \(\varphi\) is not of the family, only the sign statement of Proposition 26 is available.

**Proposition 28 (Reserve-life crossover).** Let reserves obey \(\dot R=-(1-\eta)P\), with production \(P=P_0e^{gt}\), \(g>0\), and let \(\tau=R_0/P_0\) be the reserve-life ratio. Exhaustion of the reserve class occurs at
\[
T=\frac1g\ln\Bigl(1+\frac{g\tau}{1-\eta}\Bigr),
\]
and \(T\ge\tau\) holds to first order in \(g\tau\) exactly when \(\eta\ge\tfrac12g\tau\). A reserve-life ratio therefore bounds the reserve class from above only where reclassification keeps pace with growth. On the article's own pinned record, \(\tau\approx309\) yr at \(g=0.03\,\mathrm{yr}^{-1}\), the condition requires \(\eta\ge\tfrac12g\tau\approx4.6\), which exceeds unity: reclassification would have to outpace extraction itself, and no declared reserve convention admits that. At \(\eta=0\) the same record gives \(T=g^{-1}\ln(1+g\tau)\approx77.6\) yr against the tabulated 309. The direction of the error is therefore fixed by the model class rather than by the data, and the classification of Section 8.2 is strengthened, not changed: the ratio remains an arithmetic relation whose promotion to a forecast is unavailable at every admissible elasticity.

*Proof.* Integrate \(\dot R=-(1-\eta)P_0e^{gt}\) to \(R(T)=0\) and solve; the comparison with \(\tau\) is the first-order expansion \(\ln(1+x)=x-x^2/2+O(x^3)\) at \(x=g\tau/(1-\eta)\). \(\square\)

### 6.3 Upper barriers, exit times, and maintainability

For each moiety \(m\), define lower and upper exit times:

\[
\tau_m^- = \inf\{t \ge 0 : S_m(t) \le \underline{B}_m(t)\},
\]

\[
\tau_m^+ = \inf\{t \ge 0 : S_m(t) \ge \overline{B}_m(t)\},
\]

with \(\inf \emptyset = \infty\). The overall admissibility exit time is

\[
\tau_{\text{exit}} = \min_m\{\tau_m^-,\tau_m^+\}.
\]

Horizon safety on \([0,T]\) is

\[
\tau_{\text{exit}} > T.
\]

Two disciplines attach. First, equality at the hitting time, \(S_m(\tau_m^-)=\underline{B}_m(\tau_m^-)\), requires continuity of both \(S_m\) and \(\underline{B}_m\) and appropriate initial separation: if fluxes or barriers can jump, the stock can cross the barrier without satisfying equality. Second, lower barriers need not be exhaustion thresholds. The diagnostic distinguishes physical exhaustion \(S_m=0\), functional failure \(S_m=\mathcal{B}^{\mathrm{func}}_m\), a resilience or regime-shift threshold, an economically recoverable reserve, and a minimum service-supporting stock; the term exhaustion is reserved for \(S_m=0\), and every other threshold is a barrier violation. Upper-barrier violations matter symmetrically. Atmospheric CO₂ accumulation violates an upper concentration barrier while fossil carbon stocks decline. A depletion diagnostic must check both barriers.

Finite-horizon safety is not sustainability. A stock can remain above a barrier until an assessment horizon \(T\) and still be unsustainable thereafter. A sustainability certificate requires a terminal condition:

\[
x(T) \in K_{\text{maint}},
\]

where

\[
K_{\text{maint}}
=
\{x : \exists \text{ an admissible continuation satisfying all barriers for } t \ge T\}.
\]

This is the viability kernel of the barrier set under the admissible controls. The finite-horizon diagnostic is necessary but not sufficient. The full certificate requires the terminal state to lie in the maintainability set. One consequence for reporting. The exit time is itself a minimum, over moieties and over both barrier signs, so a statement about its joint distribution is already a componentwise statement: no product of marginal probabilities is required, and none is admissible in its place.

### 6.4 Robust semantics

For uncertain parameters \(\theta\in\Theta\) and admissible disturbances \(d\in\mathcal D\), robust barrier safety is
\[
\underline B_m(t)\le S_m(t;\theta,d)\le\overline B_m(t)\qquad\forall m,\ \forall t,\ \forall\theta\in\Theta,\ \forall d\in\mathcal D,
\]
and the depletion-horizon classification is fourfold: nominal (\(\theta=\theta_0\), \(d=0\)); worst-case (\(\inf_{\theta,d}\tau_{\mathrm{exit}}(\theta,d)\)); probabilistic (\(\Pr[\tau_{\mathrm{exit}}>T]\ge1-\varepsilon\)); and scenario-conditioned (\(\tau_{\mathrm{exit}}\mid\theta=\theta_s\)). The componentwise diagnostic applies to each scenario, and the conjunctive criterion applies within each scenario and across scenarios. No single number is promoted across the four classes without a declared map. In the probabilistic class \(\tau_{\mathrm{exit}}\) is the minimum over moieties and over both barrier signs, so \(\Pr[\tau_{\mathrm{exit}}>T]\) is the probability that every component remains inside its barriers simultaneously — a joint pathwise event, not a collection of per-component reliabilities.

---

## 7. Noncompensation and Double Counting

### 7.1 No weighted certification

**Proposition (No weighted certification).** Let \(\mathcal{B}(x,t)\) be the feasible balance domain. If \(\mathcal{B}(x,t)\) contains a vector with

\[
b_i < 0
\]

and

\[
w^\top b > 0
\]

for a fixed \(w \ge 0\), then the certificate

\[
w^\top b \ge 0
\]

does not imply

\[
b \ge 0.
\]

*Proof.* On the exhibited vector, the componentwise predicate fails while the weighted predicate holds. The two predicates differ on \(\mathcal{B}(x,t)\). \(\square\)

The failure is not an accident of a particular domain. The compensating pattern is constructible against any weight.

**Proposition 29 (The certifying aggregator is unique).** Let \(r\in\mathbb R^{n}\) be component adequacies expressed in common units, and let \(\mathcal A:\mathbb R^{n}\to\mathbb R\) be monotone, \(r\le r'\Rightarrow\mathcal A(r)\le\mathcal A(r')\), calibrated, \(\mathcal A(c\mathbf 1)=c\) for every \(c\), and certifying, \(\mathcal A(r)\ge c\Rightarrow r\ge c\mathbf 1\) for every \(c\). Then \(\mathcal A(r)=\min_ir_i\).

*Proof.* Certification at \(c=\mathcal A(r)\) gives \(\min_ir_i\ge\mathcal A(r)\). Since \(r\ge(\min_ir_i)\mathbf 1\), monotonicity and calibration give \(\mathcal A(r)\ge\min_ir_i\). \(\square\)

For any admissible aggregator the compensation premium
\[
\Pi(r)=\mathcal A(r)-\min_ir_i\ \ge\ 0
\]
measures the part of a published aggregate that was produced by cross-component trades. Calibration cannot be dropped: the additively separable functional \(\sum_i\min(0,r_i)\) is continuous, monotone, faithful in the sense that a nonnegative value admits no deficit, and complete in the sense that no deficit forces a negative value; it is not the minimum and it is not calibrated. It reports the depth of the deficits where the minimum reports their existence, and either may be published provided neither is called the other. Nor can monotonicity be strengthened to strict monotonicity while keeping both directions: if a continuous \(\mathcal A\) satisfied \(\mathcal A(r)\ge0\Leftrightarrow r\ge0\), then \(\mathcal A\) would vanish on the faces of the nonnegative orthant, since it is negative wherever some component is and nonnegative on the orthant, and continuity forces equality at the boundary; a strictly increasing functional then cannot take one value at \((0,1)\) and another at \((0,2)\). Certification and strict monotonicity are incompatible, which is why the minimum is not an arbitrary convention.

**Proposition 30 (Worst concealed deficit).** Let the component balances lie in declared bounds \(\ell\le b\le u\), and let \(z\) be a published aggregate value \(z=w^{\top}b\) with \(w\ge0\), \(w\ne0\). The most severe deficit an aggregate of that value can conceal in component \(j\) is
\[
\delta^{*}_j(z)=\max\ \{-b_j:\ w^{\top}b=z,\ \ell\le b\le u\},
\]
a linear programme, finite whenever the bounds are, and positive whenever any admissible \(b\) has \(b_j<0\). Together with the premium it turns the noncompensation result into a two-sided audit: the premium measures what the aggregate bought with trades, and \(\delta^{*}_j\) measures what it can hide. Reported on declared bounds only, it is arithmetic on a published construction; where the bounds are not declared, the value is reported as not established.



### 7.2 Universal failure of weighted certification

**Theorem (Universal failure of weighted certification).** Let the ledger have \(m \ge 2\) components. For every weight vector

\[
w \in \mathbb{R}^m_+,
\qquad
w \ne 0,
\]

there exist a typed ledger, a demand vector \(d\), and an admissible state–operation pair whose attainable balance \(b\) satisfies

\[
w^\top b \ge 0
\]

while

\[
b_i < 0
\]

for some component index \(i\). No nonnegative weighting is therefore a valid componentwise certificate in general.

*Proof.* Take the two-compartment ledger with stock

\[
x = (x_1,x_2) \in \mathbb{R}^2_+,
\]

one donor-limited transfer flux

\[
f = kx_1
\]

from compartment 1 to compartment 2, identity readout

\[
O(x,u,\theta)=x,
\]

and demands \(d=(d_1,d_2)\). The witness is exhibited on two components; in a ledger with \(m>2\) components the remaining coordinates are placed at their demands, which contributes nothing to the aggregate and cannot restore a certificate. Every nonnegative state is admissible under the declared flux, because donor limitation holds: \(f=0\) at \(x_1=0\). Thus the balance

\[
b=x-d
\]

is attainable for every \(x \in \mathbb{R}^2_+\).

Fix \(w\). Let \(j\) be an index with \(w_j>0\).

If some index \(i\ne j\) has \(w_i=0\), place the deficit there: choose

\[
x_i < d_i,
\qquad
x_j \ge d_j.
\]

Then

\[
w^\top b = w_j(x_j-d_j) \ge 0,
\]

while \(b_i<0\).

Otherwise \(w_i>0\) for every \(i\ne j\). Choose any \(i\ne j\) with \(x_i<d_i\), and choose

\[
x_j \ge d_j + \frac{w_i(d_i-x_i)+\varepsilon}{w_j}
\]

for any \(\varepsilon>0\). Then

\[
w^\top b
=
w_i(x_i-d_i)
+
w_j(x_j-d_j)
\ge
\varepsilon
\ge 0,
\]

while

\[
b_i = x_i-d_i < 0.
\]

The pair \((x,d)\) is the witness for \(w\), in every dimension \(m\ge2\). \(\square\)

The construction does not use the dynamics: the failure is a property of non-negative weightings over mixed-sign balances, not of the donor-limited positivity mechanism. The conditional form of Section 7.1 is therefore not an accident of a particular domain — the compensating pattern is constructible against any weight, so the failure is universal to the method of weighted certification — while a non-compensatory test is equivalent to componentwise adequacy: the conjunctive criterion of Section 3.2, or the min-margin functional \(\min_m(S_m-\underline B_m)\) reported together with the name of the binding component.

A scalar summary may rank. It may communicate. It cannot certify componentwise adequacy. The asymmetry is exact and one-directional: a coarse aggregate refutes, because a violated aggregate barrier is a violated component barrier, and it alarms, because a positive premium is a measured quantity; it does not certify, because the concealed deficit in Proposition 30 can be made positive at any published aggregate value the domain admits.

**Proposition 31 (Aggregates do not transport event times).** Let two stocks and their sinks obey \(\dot x_i=-kx_i\), \(\dot w_i=kx_i\) with \(k>0\), so that each pair conserves material and remains nonnegative, and let the aggregate \(Z=x_1+x_2\) obey the exact closed dynamics \(\dot Z=-kZ\). The initial states \((x_1,x_2)=(2,98)\) and \((50,50)\) generate the identical aggregate trajectory \(Z(t)=100e^{-kt}\) and, at the common lower barrier \(x_i\ge1\), first hitting times \((\log2)/k\) and \((\log50)/k\). No function of the aggregate trajectory determines the component event time.

Dynamical closure and barrier observability are therefore separate obligations: an exact reduced model is not thereby competent about the events its components are declared to suffer. *Proof.* Direct evaluation of each exponential at its own barrier; the two aggregate trajectories coincide identically. \(\square\)

### 7.3 The double-counting discipline

Five rules prevent double counting and phantom mass.

1. **One balance per moiety.** Conservation laws attach to declared moieties. Adding unlike units—biomass, money, biodiversity indices, exergy—into one conserved scalar is not authorized by any conservation theorem.

2. **Explicit stoichiometry.** Entries are added within an incidence row only when their types and units agree. Every conversion is an explicit coefficient in \(S_T\), never an implicit sum.

3. **Yield routing.** A transformation represented with yield below one must route the omitted fraction to a represented compartment or a declared boundary flow. Otherwise the moiety balance holds only after silently dropping the moiety.

4. **No ghost sinks.** Every primitive with an outflow from some compartment must have its routed inflow represented, and every inflow its source.

5. **Classification labels stay out of the columns.** Reserve-life and resource-threshold quantities answer different questions. They share a column only under an explicit convention label. Diagnostic labels never determine material routing.

Every unit of mass is routed once. A flux omitted from the ledger is not thereby conserved. A recovery claimed in a quality-neutral loop is not thereby real. Double counting is a representation error, and the representation that prevents it is the contribution.

---

## 8. Application Classifications at Exact Status

The classification matrix records what each application computes.

| Time-like quantity | Question answered | G3P | Phosphate | Fisheries |
|---|---|---|---|---|
| \(J_A^{\text{gross}}, H_A^{\text{gross}}\) | turnover/dependency | no | no | gross-loss analogue only |
| \(H_A^{\text{loc}}\) | frozen net-rate ratio | no: anomaly, not stock | no: classification, not stock | no: no net \(\dot B\) |
| \(T_A\) | scenario hitting time | no | no | no |
| What it is | — | record-relative statistical index | arithmetic ratio of an economic class | removals-only pressure scale |

The point is not that these quantities are invalid. The point is that each is complete for one question and incomplete for another.

### 8.1 Groundwater anomaly-persistence indices

The Global Gravity-based Groundwater Product provides monthly groundwater-storage anomalies relative to a reference period rather than absolute aquifer volumes.

For a basin-mean anomaly series, the linear-trend anomaly persistence index is

\[
L_{\text{anom}}^{\text{hist}}
=
\frac{a_{\text{latest}} - a_{\text{hist,min}}}{[-\hat{a}']_+}.
\]

This is the fitted distance to the series’ own historical minimum divided by the fitted decline rate.

**Classification.** A statistical anomaly index with units of time. It is not the physical stock ratio \(H_A^{\text{loc}}\). It is not a forecast of aquifer exhaustion. Its value depends on the product window, basin mask, anomaly reference, and trend convention. A physical \(H_A^{\text{loc}}\) requires an absolute stock estimate and a net stock derivative, not an anomaly series alone.

**Proposition 32 (Boundedness of the persistence index on the declared trend class).** Let \(a_k=-\beta k+\varepsilon_k\) for \(k=1,\dots,n\), with \(\varepsilon_k\) independent of scale \(\sigma\) and \(\beta>0\). Within the declared class, the record minimum lies at the end of the record once the trend dominates the noise, so the fitted distance to that minimum is a noise-scale gap and the index
\[
\frac{\min_ka_k-a_n}{\text{fitted decline rate}}
\]
is \(O_{\mathbb P}(\sigma/\beta)\): bounded in probability as the record length grows, and independent of the stock. A simulation of 400 replicates at each of \(n=10^2,10^3,10^4,10^5\) with \(\beta=\sigma=1\) returns a mean index of 0.21, 0.25, 0.21 and 0.25 yr, and a 90th percentile of 0.81, 0.84, 0.95 and 1.00 yr, while the stock implied by the same series falls by five orders of magnitude; the median is zero at every length, because under a downward trend the current level is usually the record minimum. The index is therefore flat in the record length at the noise-to-trend scale \(\sigma/\beta\), which is the sense in which it cannot be extended into a horizon; the code and the seed are archived with the supplementary material. Lengthening or densifying an anomaly record therefore cannot produce a horizon, because the statistic converges to a trend-detection quantity expressed in years. This is a property of the declared linear-trend class and of the reported simulation, not a claim about any basin.

The access structure also matters. A well is infrastructure, not the resource. It draws on stored water, which is replenished by recharge. An anomaly series measures stored stock changes as observed from gravity; it does not measure access infrastructure, recharge, or the physical bottom of the aquifer. An index built on the anomaly series therefore cannot distinguish a drawdown of stored water that is recoverable on the recharge timescale from one that is not — although heavy over-extraction can make the loss permanent through compaction, subsidence or saline intrusion, in which case it is not recoverable at all.

For the four-basin record on the reported April 2002 – September 2023 window: Indo-Gangetic \(-49.7\) cm/yr with index \(\approx2.7\) yr; North China Plain \(-18.6\) with \(\approx7.9\); Central Valley \(-16.1\) with \(\approx9.5\); La Mancha \(-3.2\) with \(\approx21.4\); High Plains \(-7.9\) with the series already at its window minimum, index \(0.0\); global mean \(-0.4\) with \(\approx47.5\). The denominator carries the same extended-real convention as Definition 4: at \(\hat a'\ge0\) the index is \(+\infty\).

The classification is stated at the product's own status. A re-labelling of an anomaly-based year cannot produce an exhaustion forecast, because the absolute stock-to-barrier distance is not identifiable from an anomaly series: adding a constant to the whole series and to the reference leaves every observation unchanged, so neither a tighter anomaly record nor a narrower posterior supplies the missing absolute anchor. A physical \(H_A^{\text{loc}}\) requires an independent anchor — aquifer geometry or saturated thickness together with storage parameters, an anchor this article registers but does not discharge, and not an anomaly series alone. The product of record is G3P v1.12 (Güntner et al., 2024).

**Quarantine of one magnitude.** The Indo-Gangetic row is marked and must not be reused numerically. Its \(-49.7\) cm/yr sits an order of magnitude beyond published basin-mean groundwater-equivalent trends, which are typically a few cm/yr. A linear trend of that size maintained over the reported \(\approx21.4\) yr window would place the fitted 2002 value near \(+6.5\) m above the anomaly reference, outside the range the product's anomaly convention supports. The row is retained as a worked instance of the index construction, with its magnitude quarantined rather than blanked, awaiting re-derivation from the product's basin masks; the window-minimum column throughout is implied by the displayed trend and horizon through the index formula, which is arithmetic and not product-endorsed. The classification of the index does not depend on the magnitude.

### 8.2 The phosphate reserve-life ratio

At constant current production \(C_G\), the reserve-life ratio is

\[
T_{\text{reserve}}
=
\frac{G_{\text{reserve}}}{C_G}.
\]

At approximately \(74{,}000{,}000\) kt of world reserves and \(240{,}000\) kt/yr of production, this is approximately 309 years.

**Classification.** The arithmetic is internally consistent as a reserve-life ratio to zero. It is not a physical exhaustion forecast, because reserve classification changes with prices, technology, exploration, and regulation.

The reserves/resources distinction is central. A resource-threshold calculation,

\[
T_{\text{resource},10\%}
=
\frac{0.9 G_{\text{resource}}}{C_G},
\]

answers a different question. It must not share a column with the reserve-life ratio without an explicit convention label.

The phosphate case illustrates the classification problem cleanly. The reserve classification is economic. An exhaustion-horizon estimate built on a reserve figure carries the substitution and technology premises of that classification, not a physical forecast.

At constant current production \(C_G\), \(\mathcal T_{\mathrm{reserve}}=G_{\mathrm{reserve}}/C_G\). At approximately 74,000,000 kt of world reserves and 240,000 kt/yr of production (U.S. Geological Survey, 2026) this is approximately **309 years**. The per-country pairs of reserves and horizon are China 3,400,000 kt and \(\approx28\) yr, United States 1,000,000 kt and \(\approx45\) yr, Jordan 820,000 kt and \(\approx62\) yr, Morocco 50,000,000 kt and \(\approx1{,}250\) yr, and Australia 5,800,000 kt and \(\approx2{,}088\) yr. They imply production of 121,429, 22,222, 13,226, 40,000 and 2,778 kt/yr respectively, against the world figure of 239,482 kt/yr. Those implied figures are not independent data: each reproduces the production the horizon assumes, production = reserves/horizon, and exposes the source arithmetic, since a horizon computed from a reserve figure and a production figure must return it.

The reserves/resources split is part of the classification. A resource-threshold calculation \(\mathcal T_{\mathrm{resource},10\%}=(1-\varepsilon)G_{\mathrm{resource}}/C_G\) with \(\varepsilon=0.10\) the share left unextracted answers a different question and must not share a column with the reserve-life ratio without the convention label: at resources above 300,000,000 kt the same production gives a horizon above **1,125 years**, more than three times the reserve-based figure. The label is printed with the row. That the reserve classification is economic rather than physical is visible in the record itself: United States reserves have remained near 1,000,000 kt while cumulative production since 1996 is of order 600,000 kt.

The vintage is pinned once. The single pinned source of record is *Mineral Commodity Summaries* 2026, and every figure quoted at pin status is that vintage's: the 2025 world-production column of \(\approx250{,}000\) kt and Australia's reserves of 120,000 kt (JORC-compliant). The remaining country rows above are at their recorded pre-2026 vintage and are retained rather than blanked, as worked instances of the construction; Australia's 5,800,000 kt with \(\approx2{,}088\) yr is one of them. Completing the re-pin row by row with the pinned vintage's per-country reserve figures is the registered open data action, and no classification stated in this section depends on it.

The classification addresses the status of the ratio, not the adequacy of the resource base. The reserve-life convention and its long defence against depletion-pessimistic readings are the subject of a separate literature (Tilton, 2003; Tilton and Lagos, 2007), whose arguments about substitution, price-induced discovery and economic recovery are exactly the premises this article registers as carried rather than discharged; nothing here contradicts them.

### 8.3 The fisheries removals-only pressure time

When

\[
SSB_{\text{now}} > B_{\lim} > 0,
\qquad
F_{\text{now}} > 0,
\]

define

\[
R_B = \log\left(\frac{SSB_{\text{now}}}{B_{\lim}}\right),
\]

and

\[
\Theta_F = \frac{R_B}{F_{\text{now}}}.
\]

This is the crossing time of the deliberately incomplete comparison process

\[
\dot B = -F_{\text{now}}B.
\]

**Classification.** A removals-only pressure scale. The time unit comes from rescaling a stock-reference margin by one isolated gross-loss rate.

Because recruitment, somatic growth, maturation, natural mortality, density dependence, environmental forcing, and future policy are omitted, \(\Theta_F\) is not a net biomass depletion diagnostic. It is not a demographic hitting-time estimate. It is not a member of the \(J^{\text{gross}}\)–\(H^{\text{loc}}\)–\(T_A\) hierarchy.

The collective implication is direct. The three published “depletion time” numbers answer three distinct questions at three distinct evidentiary levels.
### 8.4 The fisheries cohort record, and the scope of the applied tables

The reported cohort figure is the archived-depletion-horizon (ADH) pure-decay proxy
\[
\mathrm{ADH}=F^{-1}\log\!\bigl(\mathrm{SSB}_{\mathrm{now}}/(0.2\max\mathrm{SSB})\bigr)
\]
under current fishing mortality \(F\), with \(\mathrm{ADH}=0\) entered for the **eight** stocks already at or below the reference, per the zero convention of the source table's caption, which the median includes: median **\(\approx1.8\) yr across the 43** assessed stocks with finite SSB and \(F\) series, from the archived pull. Two disclosures accompany the value. The archived 43-stock cohort is reproduced by **neither** public RAM Legacy release, and the record of that retraction is the version-sensitivity analysis, executed row by row against the formula: all 43 rows reproduce \(\mathrm{ADH}=\max(0,F^{-1}\log(\mathrm{SSB}/\mathcal B_{\mathrm{lim}}))\) with \(\mathcal B_{\mathrm{lim}}=0.2\max\mathrm{SSB}\). On the public releases the same protocol qualifies **415** stocks (v4.44, median **2.57** yr) and **454** stocks (v4.66, median **3.39** yr), neither reproducing the archived cohort, whose stock list and extract-time series state differ from both releases.

The cohort is a selected class, not a random sample: all 43 stocks are small pelagics (18 anchovy, 20 herring, 4 sprat, 1 sardine), the fast-maturing class the companion review screen selects by its annual-review eligibility criterion, **42 of the 43** being annual-managed spectral-null stocks per the source caption. The \(\approx1.8\) yr median is therefore a class-specific diagnostic for fast-maturing, annually managed pelagics, not a statistic of assessed fisheries in general. The qualifying positive sub-cohort (\(F>0\) and \(\mathrm{SSB}_{\mathrm{now}}>\mathcal B_{\mathrm{lim}}\); 35 stocks) has median **2.9 yr**, both medians coming from the archived pull; the long-lived groups carry the upper end of the broad cohort (elasmobranchs 11.5, sebastids 9.0, pleuronectids 6.0 yr), and only **2%** of random 43-stock draws from the 454-stock broad cohort have medians at or below the class cohort's 1.79 yr. Every cohort statistic is pinned to the archived pull (Ricard et al., 2012), whose date is archived with the analysis, and no cohort statistic is quoted from a different database version. The value is reported with its cohort conditions and is not promoted to a forecast.

**Scope of the applied records.** None of the numbers in Sections 8.1–8.4 is a computed instance of any model's first-hitting time: the groundwater column is a trend-to-window-minimum extrapolation, the phosphate column a reserve-life ratio, and the fisheries column a pure-decay proxy with recruitment omitted. They are descriptive, component-resolved diagnostics reported beside the pool each draws on, not dynamical predictions, and the classification of each row does not depend on the magnitudes.

**Remark 33 (One-signed bias of an aggregate overshoot date).** Let components carry biocapacity \(b_i\) and demand \(d_i\), and form an aggregate overshoot date from the aggregates:
\[
\tau_{\mathrm{agg}}=365\,\frac{\sum_ib_i}{\sum_id_i}=365\sum_iw_ir_i,
\qquad
w_i=\frac{d_i}{\sum_jd_j},
\qquad
r_i=\frac{b_i}{d_i}.
\]
Then \(\tau_{\mathrm{agg}}\) is a demand-weighted mean of the component ratios, so \(\tau_{\mathrm{agg}}\ge\tau_{\min}:=365\min_ir_i\), with equality exactly where every component of positive weight coincides. The difference
\[
\Pi_\tau=\tau_{\mathrm{agg}}-\tau_{\min}=365\sum_iw_i\bigl(r_i-r_{\min}\bigr)
\]
is the compensation premium of Section 7.1 in unit disguise: one-signed, exactly decomposable, unbounded in the dispersion of the components, and computable from published component tables. An aggregate overshoot date is therefore optimistic in a known direction, which is a statement about the construction rather than about any territory, and it is the one applied claim of this section that requires no recomputation of a public dataset to state. No premium figure is reported here, because the component tables of the published construction are not reproduced in this article.

**Non-example 1 — a boundary of aggregation, not a score of the framework.** The equal-weight inverse-horizon score of the four basins still above their window minimum and world phosphate reserves,
\[
\Sigma_{\mathrm{reserves}}\approx\tfrac15\left(\tfrac1{2.7}+\tfrac1{7.9}+\tfrac1{9.5}+\tfrac1{21.4}+\tfrac1{309}\right)\approx0.130\ \mathrm{yr}^{-1},
\]
is a ranking device, not a componentwise certificate: it mixes basins and reserves, incommensurable objects under the typing of Section 2.1, and it is retained only to mark the boundary of legitimate aggregation — a positive aggregate coexisting with componentwise deficits by construction, admissible as communication and inadmissible as certification. No reciprocal of it is reported as a horizon.


---

## 9. First-Passage Semantics on Declared Surrogates

### 9.1 Two objects, not one

The ledger’s own first-passage object is the model hitting time of Definition 5. The public-data quantities of Section 8 are constructed proxies on observed series.

The surrogates below do not compute the ledger’s hitting time. They do not stochastically complete the ledger. They do not identify physical failure thresholds.

### 9.2 Observed-drift Brownian surrogate

**Definition 6 (Observed-drift Brownian surrogate).** Let \(A_0\) be the latest observed anomaly — the symbol is local to Sections 9.2–9.4 and is not the half-saturation constant of Section 2.3 — and let \(\mu=\hat\mu<0\) be the fitted drawdown rate. Define

\[
A(t) = A_0 + \mu t + \varsigma W_t,
\]

stopped at first reaching the record-relative barrier \(A_{\text{win}}^{\min}\).

This is a statistical surrogate for the empirical trend extrapolation. It is not a hydrological constitutive law. It is not mass-conserving. It is not a perturbation or stochastic completion of the ledger's active-pool equation or of the finite-donor primitive system of Section 2.3; the non-completion statement is part of the definition, not a caveat added later.

### 9.3 Inverse-Gaussian groundwater first passage

**Proposition 18.** Let

\[
T_{\text{GW}}
=
\inf\{t>0 : A(t) \le A_{\text{win}}^{\min}\},
\]

and let

\[
d = A_0 - A_{\text{win}}^{\min} > 0.
\]

Conditional on treating \(\mu\) and the barrier as fixed,

\[
T_{\text{GW}} \sim IG(\nu,\lambda),
\]

with

\[
\nu = \frac{d}{|\mu|},
\qquad
\lambda = \frac{d^2}{\varsigma^2}.
\]

In particular,

\[
\mathbb{E}[T_{\text{GW}}]
=
\nu
=
\frac{d}{|\mu|}.
\]

*Proof.* The first-passage time of Brownian motion with constant negative drift to a lower barrier is inverse Gaussian. \(\square\)

The mean of the stochastic surrogate equals the deterministic trend-to-window-minimum ratio. That equality is the precise sense in which the groundwater numbers are first-passage means of a declared surrogate.

**Corollary 19 (Zero-noise limit and median).** As \(\varsigma\to0^+\), \(T_{\mathrm{GW}}\to\mathcal H^{\mathrm{win}}_{\mathrm{GW}}\) in probability, and at \(\varsigma=0\) the deterministic trajectory reaches the barrier exactly there. For every finite \(\varsigma>0\) the inverse-Gaussian median \(m\) satisfies \(m<\nu=\mathcal H^{\mathrm{win}}_{\mathrm{GW}}\), with
\[
F_{\mathcal T}(\nu)=\tfrac12+e^{2\lambda/\nu}\Phi\bigl(-2\sqrt{\lambda/\nu}\bigr)>\tfrac12 .
\]
The variance scales as \(\varsigma^2\), and the standard deviation and small-noise quantile widths as \(\varsigma\). The median below the mean is the inverse Gaussian's right skew toward short passage times; the inequality must not be inverted. *Proof.* Evaluate \(F_{\mathcal T}(t)=\Phi(\sqrt{\lambda/t}\,(t/\nu-1))+e^{2\lambda/\nu}\Phi(-\sqrt{\lambda/t}\,(t/\nu+1))\) at \(t=\nu\): the first term is \(\Phi(0)=1/2\) and the second is strictly positive for finite \(\lambda\). \(\square\)

These are conditional distributional statements about the surrogate. They are not corrections to the tabled years, and they do not show that physical water mass is depleted faster.

### 9.4 Record-relative barrier discipline

The barrier \(A_{\text{win}}^{\min}\) is selected from the same finite observation window used to estimate \(\hat{\mu}\). It is therefore path-dependent and record-relative. It is not an independently identified hydrological failure floor.

Future passage below it represents a record-breaking stress event under the surrogate, not physical exhaustion.

Three boundary facts are part of the discipline. **Already at minimum.** If \(A_0=A_{\text{win}}^{\min}\) the stopping-time convention gives \(T_{\mathrm{GW}}=0\) deterministically for every \(\varsigma\); the inverse-Gaussian family has a degenerate boundary limit concentrated at zero, and \(\mathrm{IG}(0,0)\) is not an ordinary inverse-Gaussian distribution. Zero cells report zero relative to the selected observational barrier — not zero physical uncertainty, and no confirmation of collapse. **Independent physical thresholds.** If a threshold \(A^{\sharp}<A_{\text{win}}^{\min}\) is specified independently of the record, the same constant-drift surrogate gives \(\mathbb E[\mathcal T^{\sharp}]=(A_0-A^{\sharp})/|\mu|\), longer than the record-relative proxy because the barrier is lower; this is a statement within the surrogate, not a general lower-bound theorem for the physical ledger, whose drift and state coupling may differ. **Classification.** The load-bearing content is the interpretation boundary itself: a record-relative barrier makes the passage time a property of the observation window, and no reading of the tabled numbers escapes that qualification.

### 9.5 Geometric-Brownian fisheries first passage

**Proposition 20.** Let

\[
dB_t = -hB_t dt + \varsigma B_t dW_t
\]

under the Itô convention, with \(h>0\) and

\[
0 < B_{\min} < B_0.
\]

Let

\[
T_{\text{fish}}
=
\inf\{t>0 : B_t \le B_{\min}\}.
\]

Then

\[
T_{\text{fish}} \sim IG(\nu_F,\lambda_F),
\]

with

\[
\nu_F
=
\frac{\log(B_0/B_{\min})}{h+\varsigma^2/2},
\]

\[
\lambda_F
=
\frac{\log(B_0/B_{\min})^2}{\varsigma^2}.
\]

Thus

\[
\mathbb{E}[T_{\text{fish}}]
=
\frac{\log(B_0/B_{\min})}{h+\varsigma^2/2}.
\]

*Proof.* Itô’s lemma gives

\[
d\log B_t = -(h+\varsigma^2/2)dt + \varsigma dW_t.
\]

The logarithmic threshold is therefore a Brownian first-passage problem. Proposition 18 applies. \(\square\)

For fixed arithmetic drift and the Itô parameterization, the finite-noise mean is strictly shorter than the deterministic horizon. This is a property of the chosen surrogate parameterization. It is not a universal claim that environmental variability accelerates physical biomass loss.

Under the Stratonovich convention the log-drift would be \(-h\), and the deterministic limit would match the pure-decay horizon \(h=F\) exactly: the \(\varsigma^2/2\) shortening is the Itô choice, not a property of the physical process.

### 9.6 Scope of the first-passage section

The first-passage results are distributional statements about declared surrogates. They are not corrections to the tabled years. They do not show that physical water mass or fish biomass is depleted faster. They do not supply calibrated forecasts unless the drift, barrier, and noise inputs are separately identified.
The surrogates used here are standard objects, and the section's content is the discipline attached to them rather than the passage-time formulae. The inverse-Gaussian law and its parameterisations are those of the first-passage literature on Brownian motion with drift (Chhikara and Folks, 1989; Redner, 2001); the stochastic machinery is Itô calculus in its textbook form (Øksendal, 2003). The comparison between a surrogate mean and the deterministic margin is a monotone-dynamics statement (Smith, 1995), and the barrier construction is the deterministic safety argument used in hybrid-systems verification, whose stochastic extension is the nearest formal relative of the record-relative discipline of Section 9.4 (Prajna and Jadbabaie, 2004; Prajna et al., 2007). None of these sources supplies a calibrated input: every drift, barrier and noise scale entering Sections 9.2 to 9.5 is declared by the analysis, and the results are statements about the declared class.

### 9.7 Non-claims of the first-passage section

Seven statements bound the section and are part of its content. **(1)** The Brownian and geometric-Brownian processes are not stochastic completions of the ledger and do not conserve its mass compartments. **(2)** No theorem relates \(\hat\mu\) to \(-\dot A\) of the reduced systems, to the finite-donor primitive system, or to the institutional delay equations. **(3)** The model hitting time \(T_A\) of Definition 5 is not shown to be inverse Gaussian; it would be inverse Gaussian only if the active-pool residual were Brownian with constant drift, which the coupled balance (2a)–(2d) does not supply, and the tabled groundwater numbers inherit inverse-Gaussian means from the surrogate of Section 9.2 and from nothing else. **(4)** The historical groundwater minimum is not an independently identified physical failure barrier. **(5)** A shorter surrogate median or Itô mean is not evidence of faster physical depletion. **(6)** The gross turnover horizon \(\mathcal H^{\mathrm{gross}}_A\) of Definition 3 and its productivity-illusion reading — the misreading of a large gross-turnover horizon as evidence of slow net depletion, recorded in Section 6.1 — are not first-passage results and are not treated here. **(7)** The fisheries calculation is not a stage-structured fisheries model, and the phosphate calculation is not a geological-reserve model.

The inverse-Gaussian results condition on the drift, the barrier and the noise scale. In the groundwater application \(\hat\mu\) is estimated from a finite, potentially autocorrelated record and the barrier is selected from that same record; measurement error, serial dependence, seasonal forcing, spatial aggregation, trend breaks and common climatic drivers are separate uncertainties, and integrating any of them out yields a predictive mixture rather than a single inverse-Gaussian law. A residual scale estimated from the same window does not by itself identify process noise. No calibrated predictive distribution is claimed; the full uncertainty treatment belongs to an empirical identification study.


---

## 10. Interface with Institutional Delay Dynamics

### 10.1 The exact shared object

Under the single-resource specialization,

\[
\dot N = R(N,A) - qEN.
\]

The deficit identity is

\[
D(t)
:=
qE(t)N(t) - R(N(t),A(t))
=
-\dot N(t),
\]

and its positive part is

\[
\Lambda(t)
:=
[D(t)]_+
=
[-\dot N(t)]_+.
\]

This identity holds for every trajectory of either the specialized ledger or the reduced institutional core. It is the one object both analyses may use without duplication.

The memory–effort pair that enters the institutional block is the registered object of the companion delay-dynamics analysis (Abaee, 2026, doi:10.5281/zenodo.22554217; its equation (1) and Section 2.4) and is not analysed in this article; the projection statement — the semiconjugacy condition \(\mathcal D_\pi(\xi)f(\xi)=F(\pi(\xi))\) on the history phase space — is made under that citation and is not re-proved here. The contract fixes more than the identity: the shared object includes the non-negative orthant and the sign pattern of harvest as an outflow from the living stock, and a companion model that routes the unsustainable portion of a flow into a different compartment changes the incidence and thereby leaves the interface. The reduced core's constitutive replacement \(R(N,A)\to rN(1-N/K)\) is separately an approximation with its own finite-time scope (Theorem 1, Remark 2). Under the institutional-failure specialization the macroeconomic block, prices and demand do not appear in the six right-hand sides of (2a)–(2d) together with the memory and effort laws: the ecological–institutional subsystem is an exact closed projection for every parameter value, with no singular limit required.

The companion analysis supplies the one numerical fact about governance timing that this article may use without re-deriving it: at its calibrated point, annual review under the mobilising law is unstable, and stability returns above a review interval of about 6.5 years, with the two subcritical Hopf crossings of the continuous-delay problem certified near 3.7 years and 150 years. The readout of Section 6.4 inherits the consequence. A margin computed at an interval longer than the admissible one is not conservative, because the declared object it is computed on has already changed between reviews; the admissible interval is a property of the institutional block, is reported there, and is not estimated here.

### 10.2 The non-reduction boundary

There is no exact dynamic reduction from the closed primitive finite-donor ledger to the open working institutional system.

The reasons are mathematical.

1. **Different targets.** The primitive ledger uses the intrinsic donor-limited target \(A_{\text{eq,intrinsic}}\). The working system uses a derived target of the form

   \[
   A_{\text{eq,W}}
   =
   A_{\text{eq,intrinsic}}
   +
   \frac{\kappa_A K}{\omega_A}.
   \]

   The two targets are different objects.

2. **Different vector fields at the same state.** At the working equilibrium, the active-pool vector fields of the two systems differ by an \(O(1)\) amount. The difference is not a small residual.

3. **The working point is not a rest point of the closed ledger.** The working point requires continuing geological support. The closed finite-donor system admits no interior rest at positive effort (Theorem 12).

4. **The donor-draw diagnostic is not a tracking error.** The cumulative donor-draw quantity is a diagnostic of the derived-target completion. It is not a finite-time tracking metric between the two fields.

5. **Extraction integrability.** The closed primitive system makes sustained extraction integrable (Theorem 14). It therefore cannot possess the working positive-flux rest indefinitely.

The five reasons have quantitative content on the registered parameterization. (1) The three targets are \(A_{\text{eq,intrinsic}}=50\), the working active pool \(A_{\text{act},*}=397.87\), and \(A_{\text{eq},W}=50+\kappa_AK/\omega_A=5{,}050\): the two equilibria differ by a factor of eight and the two targets by two orders of magnitude. (2) At the working equilibrium, write the two \(A_{\text{act}}\) vector fields at the same state \((N,A_{\text{act}},U)\). Under the registered scale separation they differ by \(\omega_A(A_{\text{eq},W}-A_{\text{eq,intrinsic}}\sigma)-\gamma_UU=\kappa_AK-\gamma_UU\). At the working point's quasi-rest detritus level, where \(\gamma_UU=\mathcal T^*\approx4.47\), that difference is approximately **0.535** stock units per year; at \(U=0\) it is \(\kappa_AK=5.000\). This is an \(O(1)\) to \(O(\kappa_AK)\) discrepancy, not a small residual. It is \(U\)-dependent because the working field omits the detritus return \(\gamma_UU\) that the closed field carries, and \(\mathcal B^*-R^*=\mathcal T^*\) is the working system's turnover balance, not the field difference. (3) The working point \((N^*,A_{\text{act},*})=(89.526,\,397.87)\) at \(E^*\approx2.090\) requires continuing geological support — the flux \(\omega_A(A_{\text{eq},W}-A_{\text{act},*})=4.652133\ldots\) stock units per year, supplied every year by a donor the working system treats as a parameter — and at the same state the closed primitive donor flow is \(e_{GA}-e_{AG}=\omega_A(A_{\text{eq,intrinsic}}-A_{\text{act},*})\approx-0.348\): the donor gains in the closed ledger where the working completion has it losing 4.652, opposite signs rather than different magnitudes. The reverse check \(qE^*N^*=0.001\times2.090\times89.526\approx0.187\) is consistent to the quoted digits, and these working-point figures are imported at the companion's registered precision. (4) The donor-draw diagnostic
\[
\varepsilon_G(T)=G_0^{-1}\int_0^T\bigl|e_{GA}-e_{AG}\bigr|\,dt
\]
measures the derived-target completion, not trajectory tracking; no finite-time tracking correspondence between the completions holds. (5) Extraction on the closed ledger is \(L^1\) in time (Theorem 14), which is what forbids indefinite persistence of the working positive-flux rest.

The five reasons form a trichotomy: (1)–(3) are short-time obstructions, since the fields differ by \(O(1)\) at the working point and trajectories diverge on \(O(1)\) timescales; (5) is the long-time obstruction; (4) is neither, because the diagnostic does not measure tracking at any timescale.

**Theorem (Non-reduction).** There is no exact dynamic reduction, no regular perturbation, and no finite-time tracking correspondence from the closed primitive ledger to the open working system.

The permitted relation is analogy for shared mechanism language plus diagnostic reconstruction of omitted mass flows. A closed physical ledger and an open working system can share one diagnostic identity without sharing a dynamics.

---

The frozen-donor limit is a corollary of the structural clause (1). Rescaling \(G=G_0g\) with \(g(0)=1\) gives \(\dot g=-G_0^{-1}(e_{GA}-e_{AG})\); the limit \(G_0\to\infty\) freezes \(g\) but does not restore the working completion's derived target, because the limiting recharge field still uses \(A_{\text{eq,intrinsic}}\). The scaling is therefore not a regular perturbation of the working vector field, and local Hopf persistence of the working system under this primitive scaling is not claimed; a different derived-target completion would be required before such a statement could be formulated.

On the closed system with the donor \(G(t)\) included as a state, the dynamics are an autonomous retarded equation with a slow donor coordinate. The companion's \(\tau_+\approx150\) yr upper cycle is a frozen-donor object and can persist only as a transient on the finite donor budget, where the transient-duration statement is an order-and-budget bound and not an asymptotic estimate: under a sustained lower extraction flux \(c>0\) the duration is bounded above by \(G_0/c\), and the scale must name its flux. At the closed-block extraction rate \(c=qE^*N^*\approx0.187\) stock units per year the budget bound is \(G_0/c\approx2\times10^{6}\) years; at the working completion's recharge flux \(\mathcal B^*\approx4.652\) the draw scale is \(G_0/\mathcal B^*\approx8.6\times10^{4}\) years, the "tens of thousands of years" heuristic using the working flux (at \(G_0/A_{\text{act},*}=10^3\)); both scales sit far above the institutional delays of the companion family. Whether the frozen-donor local Hopf structure persists as a slowly drifting transient in the closed donor system is an open slow-passage problem; the mass budget alone does not establish it.

### 10.3 Negative content and limitations

The negative and boundary results of this article are stated as results. The classifications of Section 8 are negative results: the anomaly index is not a stock ratio, the reserve-life ratio is not a forecast, the removals-only time is not a depletion diagnostic. The non-reduction boundary fixes a rejected mapping with five reasons. The empty-kernel mechanisms of the sink obstruction are structural. A violation of a declared barrier is a loss of safety; a data or certificate failure — a quarantined row, a retraction, a stale vintage — is a loss of assurance, and the two are not interchangeable.

**Limitations.** (i) The two-pool exact specialization of the groundwater template remains open; the admitted object is the one-pool affine trend approximation of Section 8.1, and no two-pool model is claimed as established. (ii) The phosphorus and groundwater records are registered template obligations with no constitutive content behind them. (iii) The first-passage propositions of Section 9 concern declared surrogates, not the ledger. (iv) The applied records of Section 8 are classified diagnostics at their stated evidentiary levels and are not calibrated early-warning systems or forecasts. (v) The non-reduction boundary of Section 10.2 is permanent, not a gap. (vi) The conditional hybrid balance of Theorem 15 stays conditional, with its jump-interpretation and yield-routing obligations open per application. (vii) The support-saturation limits of Theorem 1 and Remark 2 are local and finite-time; neither is a full-system reduction. (viii) No theorem in this article identifies the maintainability kernel \(K_{\mathrm{maint}}\) of Section 6.3 with any family of the rest set of Theorem 13: whether the carrying-capacity rest lies in the kernel is a question about the declared barrier values and the admissible control class, and it is not answered here. (ix) The article asserts nothing empirical about any named resource system beyond the classifications of public data products stated at their source status.

## 11. Conclusion

The two failure modes of the introduction—compensatory aggregation and classification drift—are representation errors. The representation that prevents them is this paper’s content.

Conservation is proved from the incidence structure, not assumed. Positivity is proved from donor limitation, not asserted. Services are readouts, not mass. Depletion time is three quantities, not one.

The closed finite-donor ledger carries its complete theorem set: mass identity, orthant invariance, no interior rest at positive effort, the vanishing-extraction rest set, and extraction integrability. The non-reduction boundary records why the closed ledger and the open working systems of institutional dynamics are different completions sharing one exact object.

The applied depletion numbers answer exactly the questions their constructions pose. The groundwater anomaly index is a record-relative statistical index. The phosphate reserve-life ratio is arithmetic on an economic classification. The fisheries removals-only time is a pressure scale. Stating them with those questions is what makes them usable. Collapsing them into one “time to depletion” is what makes them false.

No nonnegative weighting certifies componentwise adequacy: the obstruction is compensation, not the scalar form as such. A scalar summary may rank and communicate; it certifies only if it is non-compensatory, such as the binding margin of the conjunctive criterion reported with the name of the component that binds. Certification requires that test.

---

## Declarations

**Data availability.** No new data were generated. The application classifications are arithmetic on public data products, each named with the vintage used: the U.S. Geological Survey *Mineral Commodity Summaries 2026* for phosphate reserves and production; G3P v1.12 (Güntner et al., 2024), derived from GRACE and GRACE-FO monthly mascon solutions (Tapley et al., 2004), for the groundwater anomaly series and their window minima; the RAM Legacy Stock Assessment Database v4.44 and v4.66 for the broad public cohorts; the archived assessment pull of Ricard et al. (2012), whose extract date is archived with the analysis, for the 43-stock cohort record and its re-verification; and the spectral-null classification of the companion review-screen study for the 42-stock annual-management count. The two-pool hydrological objects, the phosphorus template parameters and the split-assignment mechanism values are declared parameterizations and identification targets, not measurements; no observational file is claimed for them.

**Supplementary material.** The accompanying file carries the ten-state admissibility template and its three audited negative witnesses, the registered identification ladders of the phosphorus and groundwater templates, the split-assignment mechanism table, the statement inventory with the status of every statement in the main text, and the fisheries cohort record with the archived-pull verification and the executed broad-cohort comparison. It additionally carries the proof obligations attached to each entry of the certification state of Section 3.1, the two linear programmes of Definitions 21 and 22 and Theorem 24 with their input requirements, the certificate vectors of the three classified indicators, the promotion-rule table collecting the conditions under which each published ratio may be read as an event time, and the worked ledger exhibit with the code that reproduces every computed figure in Sections 6.2, 7.1, 8.1 and 8.4.

**Code availability.** The scripts that generate every computed figure in this article — the persistence-index simulation of Section 8.1, the curvature and crossover arithmetic of Section 6.2, the compensation premium and worst-concealed-deficit linear programmes of Section 7.1, and the worked ledger exhibit of the supplementary material — are archived with the supplementary file, with the random seed and library versions recorded in the archive manifest. The scripts read no data other than the public products named in the data availability statement.

**Declaration of competing interest.** None.

**AI declaration.** GLM, Qwen, and DeepSeek AI assisted with drafting and iterative review.

## References

Abaee, A., 2026. Delay-induced regime change in harvested stocks: the mobilising and protective channels of institutional feedback, and the review interval as control. Zenodo. https://doi.org/10.5281/zenodo.22554217. Companion delay-dynamics study. Abaee, A., 2026. Periodic review as sampled governance: sample-and-hold dynamics of assessment-driven effort control, a selected 42-stock spectral screen, and the Northern Cod case. Zenodo. https://doi.org/10.5281/zenodo.22554297. Companion review-screen study. Abaee, A., 2026. The limits of compensatory aggregation: a formal separation of weak and strong sustainability assessment. Zenodo. https://doi.org/10.5281/zenodo.22545740. Compan- ion assessment-separation study. Ahuja, R.K., Magnanti, T.L., Orlin, J.B., 1993. Network Flows: Theory, Algorithms, and Applications. Prentice-Hall, Englewood Cliffs. Aubin, J.-P., 1991. Viability Theory. Birkhäuser, Boston. Baez, J., Li, X., Libkind, S., Osgood, N.D., Patterson, E., 2023. Compositional modeling with stock and flow diagrams. In: Applied Category Theory 2022. Electronic Proceedings in Theoretical Computer Science 380, 77–96. https://doi.org/10.4204/EPTCS.380.5 Blomqvist, L., Brook, B.W., Ellis, E.C., Kareiva, P.M., Nordhaus, T., Shellenberger, M., 2013. Does the shoe fit? Real versus imagined ecological footprints. PLo S Biology 11, e1001700. https://doi.org/10.1371/journal.pbio.1001700 Brunner, P.H., Rechberger, H., 2004. Practical Handbook of Material Flow Analysis. Lewis Publishers, Boca Raton. Chhikara, R.S., Folks, J.L., 1989. The Inverse Gaussian Distribution: Theory, Methodology, and Applications. Marcel Dekker, New York. 38 Daly, H.E., 1990. Towardsomeoperationalprinciplesofsustainabledevelopment. Ecological Economics 2, 1–6. Clark, C.W., 1990. Mathematical Bioeconomics: The Optimal Management of Renewable Resources, 2nd ed. Wiley, New York. Ekins, P., Simon, S., Deutsch, L., Folke, C., De Groot, R., 2003. A framework for the prac- tical application of the concepts of critical natural capital and strong sustainability. Ecological Economics 44, 165–185. Eurostat, 2001. Economy-wide Material Flow Accounts and Derived Indicators: A Method- ological Guide. Eurostat, Luxembourg. Feinberg, M., 2019. Foundations of Chemical Reaction Network Theory. Springer, Cham. Fischer-Kowalski, M., Krausmann, F., Giljum, S., Lutter, S., Mayer, A., Bringezu, S., Moriguchi, Y., Schütz, H., Schandl, H., Weisz, H., 2011. Methodology and indicators of economy-wide material flow accounting: state of the art and reliability across sources. Journal of Industrial Ecology 15, 855–876. Gale, D., 1957. A theorem on flows in networks. Pacific Journal of Mathematics 7, 1073–1082. Güntner, A., Sharifi, E., Haas, J., et al., 2024. Global Gravity-based Groundwater Product (G3P), V. 1.12. GFZ Data Services. https://doi.org/10.5880/G3P.2024.001 Illakwahhi, D.T., Vegi, M.R., Srivastava, B.B.L., 2024. Phosphorus’ future insecurity, the horrorofdepletion, andsustainabilitymeasures. International Journalof Environmental Science and Technology 21, 9265–9280. https://doi.org/10.1007/s13762-024-05664-y Jacquez, J.A., Simon, C.P., 1993. Qualitative theory of compartmental systems. SIAM Review 35, 43–79. Lin, D., Hanscom, L., Murthy, A., Galli, A., Evans, M., Neill, E., Mancini, M.S., Martindill, J., Medouar, F.-Z., Huang, S., Wackernagel, M., 2018. Ecological footprint accounting for countries: Updates and results of the National Footprint Accounts, 2012–2018. Resources 7, 58. https://doi.org/10.3390/resources7030058 Martinez-Alier, J., Munda, G., O’Neill, J., 1998. Weak comparability of values as a founda- tion for ecological economics. Ecological Economics 26, 277–286. Meadows, D.H., Meadows, D.L., Randers, J., Behrens III, W.W., 1972. The Limits to Growth. Universe Books, New York. Munda, G., Nardo, M., 2009. Noncompensatory/nonlinear composite indicators for ranking countries: a defensible setting. Applied Economics 41, 1513–1523. Neumayer, E., 2013. Weak versus Strong Sustainability: Exploring the Limits of Two Opposing Paradigms, 4th ed. Edward Elgar, Cheltenham. Øksendal, B., 2003. Stochastic Differential Equations: An Introduction with Applications, 6th ed. Springer, Berlin. Prajna, S., Jadbabaie, A., 2004. Safety verification of hybrid systems using barrier certificates. In: Hybrid Systems: Computation and Control VII. Lecture Notes in Computer Science 2993, 477–492. Prajna, S., Jadbabaie, A., Pappas, G.J., 2007. A framework for worst-case and stochastic safety verification using barrier certificates. IEEE Transactions on Automatic Control 52, 1415–1428. Redner, S., 2001. A Guide to First-Passage Processes. Cambridge University Press, Cam- bridge. Ricard, D., Minto, C., Jensen, O.P., Baum, J.K., 2012. Examining the knowledge base and status of commercially exploited marine species with the RAM Legacy Stock Assessment Database. Fish and Fisheries 13, 380–398. Smith, H.L., 1995. Monotone Dynamical Systems: An Introduction to the Theory of Competitive and Cooperative Systems. Mathematical Surveys and Monographs 41. American Mathematical Society, Providence. Tapley, B.D., Bettadpur, S., Ries, J.C., Thompson, P.F., Watkins, M.M., 2004. GRACE measurements of mass variability in the Earth system. Science 305, 503–505. Tilton, J.E., 2003. On Borrowed Time? Assessing the Threat of Mineral Depletion. Re- sources for the Future, Washington, DC. Tilton, J.E., Lagos, G., 2007. Assessing the long-run availability of copper. Resources Policy 32, 19–23. U.S. Geological Survey, 2026. Mineral Commodity Summaries 2026: Phosphate Rock. USGS, Reston, VA. https://www.usgs.gov/centers/national-minerals-information-center/mineral-commodity-summaries United Nations, European Commission, International Monetary Fund, Organisation for Economic Co-operation and Development, World Bank, 2014. SEEA Central Framework: 2012 Technical Implementation. United Nations, New York. Statistical Papers, Series M No. 96. United Nations, 2025. System of National Accounts 2025. United Nations Statistics Division, New York. Adopted by the United Nations Statistical Commission at its fifty-sixth session. https://unstats.un.org/unsd/nationalaccount/sna2025.asp Wackernagel, M., Beyers, B., 2019. Ecological Footprint: Managing our Biocapacity Budget.

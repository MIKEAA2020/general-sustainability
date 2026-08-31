<!-- Reconstruction of the earlier draft of the material-ledgers paper, rebuilt from the user's saved copy (abstract, introduction, Sections 2–4.5) plus the source-read passes for the remaining sections. Saved separately; does not overwrite paper3_material_ledgers.md. -->

# Typed Stoichiometric Ledgers and the Semantics of Depletion Claims: Certification Layers, the Closed Finite-Donor Theorem Set, and Depletion-Horizon Diagnostics

## Abstract

Depletion claims are often made on quantities that do not support them: reserve-life ratios are arithmetic, not forecasts; anomaly-persistence indices carry units of time without being times to any physical event; gross-throughput measures are read as net decline. This paper builds the accounting layer that gives each such claim its exact status. A typed stoichiometric ledger (state $\dot x = Nv + b$, moiety readout $S = Cx$, conservation $\ell^\top N = 0$, donor-limited primitives) separates three certification layers — accounting consistency, conservation consistency, and barrier safety — and proves their logical relationships. On the closed finite-donor ledger it proves: the natural-block mass identity; forward invariance of the nonnegative orthant; the absence of interior rest points at positive effort; the extinction–geochemical rest set; integrability of extraction against the donor budget; and, by counterexample, that positive extraction alone does not imply finite exhaustion. A depletion-diagnostics taxonomy separates gross turnover, the frozen-rate local ratio, and the scenario-conditioned hitting time, with a threshold-horizon bracket bounding the frozen-rate error and a flux-bounding envelope theorem converting flux bounds into barrier certificates. First-passage semantics are supplied for the public-data proxies (inverse Gaussian for groundwater anomalies; geometric Brownian for removals-only fisheries pressure), with a record-relative barrier discipline stating what tabled numbers mean. Applications are classified: G3P anomaly-persistence indices, depletion-horizon tables, the phosphate reserve-life ratio, and the fisheries removals-only pressure time. The ledger also proves what it does not support: no nonnegative weighting of component balances certifies componentwise nonnegativity, and five double-counting rules block phantom mass.

**Keywords:** material flow accounting; stoichiometric ledger; depletion indicators; certification layers; first-passage time; noncompensation; reserve life

---

## 1. Introduction

### 1.1 Two failure modes and the two confusions

A reserve-life ratio divides a reserve figure by a production figure and calls the quotient a horizon. A groundwater anomaly index fits a trend to a satellite product and reports the fitted distance to the series' own minimum divided by the fitted rate — a number in units of years that is not a time to any physical event. A fisheries pressure indicator divides a log biomass margin by a fishing mortality and presents the result as a time scale. Each of these quantities is informative about something; none is what it is typically taken to be. The reserve-life ratio is an arithmetic property of an economic classification: reserves are the fraction of a geological resource that is currently profitable to extract, and they grow and shrink with prices, technology, and exploration — a point made forcefully for phosphorus by Illakwahhi, Vegi, and Srivastava (2024), who show that single-source reserve data support neither the depletion dates nor the peak-production dates commonly computed from them, and made for copper by Tilton and Lagos (2007), who document reserves growing through a century of rising production.

The same ambiguity pervades accounting itself. Material flow analysis (MFA) supplies the bookkeeping of society's material throughput (Brunner and Rechberger, 2004; Eurostat, 2001; Fischer-Kowalski et al., 2011), and its incidence structure is shared with reaction-network theory, where the sign pattern of the stoichiometric matrix is a conservation object (Feinberg, 2019). But bookkeeping balance, stoichiometric conservation, thermodynamic admissibility, and sustainability safety are four different predicates, and the literature routinely slides between them. A mass-balanced ledger can be chemically impossible; a chemically consistent ledger can violate every declared barrier; and a ledger satisfying all declared barriers can fail conservation. This paper's first contribution is to separate the layers and prove their relationships, so that each claim about a material system carries the predicate it actually establishes.

The paper's second motivation is noncompensation. The weak-comparability thesis of ecological economics holds that values relevant to environmental decisions may not be commensurable in a single metric (Martinez-Alier, Munda, and O'Neill, 1998). At the level of material accounting this thesis has a precise algebraic form, which this paper proves: no nonnegative weighting of component balances can certify that every component satisfies its floor — a positive weighted sum never certifies componentwise nonnegativity. Scalar summaries may rank and communicate; certification requires the vector.

### 1.2 What this paper establishes

- **The typed stoichiometric ledger (Section 2):** a state equation $\dot x = Nv + b$ in primitive nonnegative fluxes with an explicit moiety-composition map $S = Cx$, one conservation law per declared moiety, donor limitation as the admissibility condition on outflows, and five double-counting rules.
- **Three certification layers (Section 3):** accounting consistency, conservation consistency, and barrier safety, with proofs of what implies what, and the explicit statement of what this paper does not establish — thermodynamic admissibility — which requires energy accounting, nonnegative entropy production, and reaction feasibility outside the present scope.
- **The closed finite-donor theorem set (Sections 4–5):** mass identity, orthant invariance, no interior rest point at positive effort, the extinction–geochemical rest set, and integrability of extraction — each proved in full, together with the counterexample that disciplines the exhaustion reading (donor-controlled proportional extraction $\dot S = -kS$ extracts positively forever without finite exhaustion).
- **A depletion-diagnostics taxonomy (Section 7):** gross turnover, the frozen-rate local ratio, and the scenario-conditioned hitting time, with a bracket theorem bounding the frozen-rate error under declared rate bounds, and a flux-bounding envelope theorem turning componentwise flux bounds into barrier certificates.
- **First-passage semantics for the public-data proxies (Section 8):** the trend-extrapolated groundwater anomaly series as an observed-drift Brownian surrogate with inverse-Gaussian first passage; the removals-only fisheries pressure as geometric Brownian motion; and a record-relative barrier discipline stating exactly what the tabled numbers mean — in particular, that a passage time computed against a barrier selected from the same observation window is a record-breaking stress statistic, not a physical exhaustion date.
- **Applications classified at their exact status (Section 9):** G3P anomaly-persistence indices, component-resolved depletion-horizon tables, the phosphate reserve-life ratio, and the fisheries removals-only pressure time — each labelled as the proxy it is.

### 1.3 What is not claimed

No stochastic completion of the ledger is claimed: the surrogate processes of Section 8 do not conserve the ledger's mass and are not perturbations of its dynamics. No thermodynamic admissibility is claimed. No identification of the two-pool groundwater hypothesis is claimed (its identification requirements are registered in Section 10, not discharged). And no empirical finding about any basin, aquifer, or fishery is claimed beyond the descriptive status of the tabulated indicators.

---

## 2. The Typed Stoichiometric Ledger

### 2.1 Ontology: four distinct concepts

The ledger separates four concepts that accounting practice often merges. A *moiety* is a conserved substance class (an element, or a declared conserved combination), the only object to which a conservation law attaches. A *species* is a chemical or biological form of a moiety. A *compartment* is a spatial or functional location holding a stock. A *stock* is a compartment's current amount of a species, with a physical unit. "Carbon in the atmosphere" is a location-specific stock, not a moiety: carbon is the moiety, and the atmosphere is a compartment. Conservation laws are stated per moiety; nothing is conserved merely by being a compartment.

### 2.2 The balance law

A ledger state $x \in \mathbb{R}^n_+$ collects compartment stocks, each entry carrying its material identity, spatial support, and unit. Internal dynamics use nonnegative primitive fluxes:

$$
\dot x = N v(x, y, \theta) + b(t), \qquad v \ge 0, \tag{1}
$$

where $N \in \mathbb{R}^{n \times J}$ is the typed stoichiometric (incidence) operator — the compartment–flux bookkeeping of material flow analysis (Brunner and Rechberger, 2004; Eurostat, 2001; Fischer-Kowalski et al., 2011), on the incidence formalism of reaction-network theory (Feinberg, 2019) — and $b$ collects declared boundary transfers. Entries are added within a row only when their types and units agree; a conversion between types is an explicit stoichiometric coefficient, never an implicit sum. The sign pattern of $N$ and the nonnegativity of $v$ are separate declarations: columns of $N$ carry signed entries even though $v \ge 0$.

**Theorem 1 (Conservation law).** *If $L^\top N = 0$ for a matrix $L$ of moiety-accounting vectors, then*
$$
\frac{d}{dt}\bigl(L^\top x\bigr) = L^\top b:
$$
*one conservation law per conserved moiety and boundary.*

*Proof.* Multiply (1) by $L^\top$: $\frac{d}{dt}(L^\top x) = L^\top N v + L^\top b = L^\top b$. $ \square $

The identity does not create a scalar sustainability mass across incommensurable systems: adding biomass, money, biodiversity indices, and exergy into one conserved scalar is authorized by no conservation theorem.

**Donor limitation.** An outflow primitive from compartment $i$ must vanish when $x_i = 0$. This single condition — the mass-action principle of reaction networks, and the condition behind nonnegativity of compartmental systems (Jacquez and Simon, 1993; Feinberg, 2019) — is the admissibility requirement throughout: a target-relaxation flux such as $\omega(A^{\mathrm{eq}} - A)$ is admissible only after donor limitation is made explicit, and otherwise declares its source an effectively infinite external reservoir, making the system open rather than closed.

### 2.3 The double-counting discipline

Five rules, each carried by a proved or defined statement of this paper, jointly prevent double counting and phantom mass. (i) **One balance per moiety:** conservation laws attach to declared moieties (Theorem 1). (ii) **Explicit stoichiometry:** conversions are explicit coefficients in $N$. (iii) **Yield routing:** a transformation with yield below one must route the omitted fraction to a represented compartment or a declared boundary flow (Section 5). (iv) **No ghost sinks:** every primitive with an outflow from some compartment must have its routed inflow represented, and every inflow its source — a column of $N$ carrying both signs requires the two row sets to match the declared routing, and Section 4.2's matrix discharges the check column by column. (v) **Classification labels stay out of the columns:** reserve-life and resource-threshold quantities answer different questions and share a column only under an explicit convention label.

---

## 3. Three Certification Layers

The ledger supports three distinct predicates. Fix a trajectory $x(\cdot)$ on $[0,T]$.

**Layer 1 (accounting consistency).** The balance law holds: $\dot x = Nv + b$ almost everywhere, with $v \ge 0$ admissible.

**Layer 2 (conservation consistency).** Every declared conserved quantity $\ell$ satisfies $\ell^\top N = 0$ — equivalently, for a closed system ($b = 0$), every declared moiety total $\ell^\top x$ is invariant.

**Layer 3 (barrier safety).** For every declared component barrier pair $\underline{B}_m(t) \le S_m(t) \le \overline{B}_m(t)$, with $S = Cx$ the moiety readout, the trajectory satisfies both bounds for all $t \in [0,T]$.

**Proposition 1 (Conservation implies accounting, for the conserved quantities).** *If $\ell^\top N = 0$, then $\frac{d}{dt}(\ell^\top x) = \ell^\top b$; in a closed system $\ell^\top x$ is invariant.*

*Proof.* Multiply (1) by $\ell^\top$: $\frac{d}{dt}(\ell^\top x) = \ell^\top N v + \ell^\top b = \ell^\top b$. With $b = 0$ the derivative vanishes. $ \square $

**Proposition 2 (Barrier safety is independent of accounting).** *A trajectory can be perfectly mass-balanced while violating a declared barrier, and a trajectory can satisfy all declared barriers while violating a conservation law.*

*Proof.* Both directions by construction. For the first: constant extraction at a rate exceeding regeneration in the ledger of Section 4 is exactly mass-balanced (Theorem 3 below states the identity) and drives the active pool through any positive barrier in finite time. For the second: a trajectory that respects the barriers but whose bookkeeping drops a moiety (the yield-routing violation of Section 2.3(iii)) fails conservation without touching the barriers. $ \square $

**Proposition 3 (Thermodynamic admissibility is a fourth layer).** *Thermodynamic admissibility — energy conservation, nonnegative entropy production, reaction feasibility — implies accounting consistency, but accounting consistency does not imply it. This paper establishes Layers 1–3 only.*

The proposition is a scope statement, not a theorem about thermodynamics: the additional structure (energy accounting, entropy production, feasibility) is outside the present framework and is not supplied by any of the three layers.

The typed safety set at time $t$ is

$$
K(t) = \{ x \ge 0 : \underline{B}(t) \le Cx \le \overline{B}(t) \},
$$

and the noncompensatory assessment criterion is conjunctive: all barriers simultaneously, with no weighted aggregate used as the decision criterion (Section 11 proves why).

---

## 4. The Closed Finite-Donor Ledger

### 4.1 The natural block

The closed ledger of this paper is the finite-donor primitive system. Let

$$
x_L = (N, A^{\mathrm{act}}, A^{\mathrm{geo}}, U), \qquad
s = \frac{A^{\mathrm{act}}}{A^{\mathrm{act}} + A_0}, \qquad
\sigma = \frac{A^{\mathrm{geo}}}{A^{\mathrm{geo}} + A_{g0}},
$$

with $N$ the living stock, $A^{\mathrm{act}}$ the active abiotic pool, $A^{\mathrm{geo}}$ the geological donor, and $U$ the detritus compartment. Net regeneration and gross uptake are the constitutive laws

$$
R(N, A^{\mathrm{act}}) = rN\left(1 - \frac{N}{K}\right) s, \qquad
T = \kappa_A N s, \qquad
B = R + T,
$$

and the four primitives involving the donor are

$$
e_{GA} = \omega_A\, [A^{\mathrm{eq,intrinsic}}]_+\, \sigma, \qquad
e_{AG} = \omega_A A^{\mathrm{act}}, \qquad
C_{A,\mathrm{lim}} = C^A \sigma, \qquad
\gamma_U U \ \text{(detritus return)}.
$$

No derived target appears: recharge is donor-limited and cannot run backward ($e_{GA} = 0$ at $A^{\mathrm{geo}} = 0$ and at a nonpositive intrinsic target), and mining $C_{A,\mathrm{lim}}$ is donor-limited exactly as extraction is. With $A_{g0} > 0$ the donor fraction $\sigma$ is smooth and strictly increasing in the donor level. Under the institutional-failure specialization ($\mu = \nu = \rho = 0$, $C^A = 0$) the closed natural block is

$$
\begin{aligned}
\dot N &= R - qEN, \\
\dot A^{\mathrm{act}} &= -B + e_{GA} - e_{AG} + \gamma_U U, \\
\dot A^{\mathrm{geo}} &= -e_{GA} + e_{AG}, \\
\dot U &= T - \gamma_U U,
\end{aligned} \tag{2}
$$

together with a memory–effort pair $(Z, E)$ driven by $qEN - R$ (never by mining) — a pair analysed dynamically in a companion paper and used here only as the extraction schedule. The registered parameterisation is $r = 0.02$, $K = 100$, $q = 0.001$, $\kappa_A = 0.05$, $\omega_A = 10^{-3}$, $A_0 = 1$, $A^{\mathrm{eq,intrinsic}} = 50$, $\gamma_U = 0.2$, with the geological half-saturation $A_{g0}$ declared positive under the separation-of-scale condition $A^{\mathrm{geo}} \gg A_{g0}$ (in which regime $\sigma \approx 1$); no numerical value of $A_{g0}$ is asserted, and the $A_{g0} = 0$ corner is the discontinuous-perturbation limit, not the registered regime.

### 4.2 The six-compartment illustration

For one conserved limiting material, the scaffold is instantiated by six compartments — living biomass $X$, detritus $U$, active abiotic pool $A$, geological pool $G$, product $P$, and absorbing stock $W$ — with eight nonnegative primitive fluxes: assimilation $g(X,A)$, mortality $m(X)$, harvest $h(X,E)$, decomposition $d_U(U)$, geological-to-active transfer $e_{GA}(G,A)$, active-to-geological transfer $e_{AG}(A,G)$, direct mining $c_G(G,E_G)$, and product retirement $r_P(P)$. With harvest fraction $\alpha \in [0,1]$ routed to $U$ and retirement fraction $\rho \in [0,1]$ returning to $U$,

$$
\dot z = S(\alpha,\rho)\, v(z,u), \qquad
z = (X,U,A,G,P,W)^\top, \qquad
v = (g,\,m,\,h,\,d_U,\,e_{GA},\,e_{AG},\,c_G,\,r_P)^\top,
$$

with

$$
S(\alpha,\rho) =
\begin{pmatrix}
1 & -1 & -1 & 0 & 0 & 0 & 0 & 0 \\
0 & 1 & \alpha & -1 & 0 & 0 & 0 & \rho \\
-1 & 0 & 0 & 1 & 1 & -1 & 0 & 0 \\
0 & 0 & 0 & 0 & -1 & 1 & -1 & 0 \\
0 & 0 & 1-\alpha & 0 & 0 & 0 & 1 & -1 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 1-\rho
\end{pmatrix}, \qquad \mathbf{1}^\top S = 0.
$$

The zero column sums are the incidence statement of mass conservation, proved in Theorem 3 below. The matrix makes the routing choices visible, and the constitutive choices are features of this example, not properties of every typed ledger: the constant splits $\alpha$ and $\rho$, the compartment set, and the absorbing-sink convention are declared choices; the construction is a monomaterial projection, not a universal ecological mechanism.

### 4.3 The four-stock resource–sink–nutrient–product system

A second exact specialization closes a resource–sink system: state $(S, K, N, P) \in \mathbb{R}^4_+$, with $K$ the sink stock, $N$ the nutrient stock, $S$ the resource, $P$ the product, and

$$
\dot S = g(S,N) - H, \qquad
\dot K = \theta_K H - \theta_\delta K, \qquad
\dot N = -g(S,N) + \theta_\delta K + I_N, \qquad
\dot P = (1-\theta_K) H - Q_P,
$$

where $\theta_K$ is the sink-generation fraction, $\theta_\delta$ the assimilation rate, $I_N$ external nutrient input, and $Q_P$ product disposal. Adding the four equations gives

$$
\frac{d}{dt}(S + K + N + P) = I_N - Q_P:
$$

total mass is conserved exactly when both boundary transfers vanish. Every internal transfer cancels in the column sum; the boundary terms survive as the ledger's declared inputs and outputs.

**Sink obstruction (independent of the resource).** The mass balance has a sink-side reading with two empty-kernel mechanisms that operate whatever the resource stock does. With sink loading $w(H)$, assimilation $\delta(K)$, and a harvest floor $H \ge H_{\min} > 0$: under *no assimilation* ($\delta \equiv 0$), $\dot K \ge w(H_{\min}) > 0$ and the sink exceeds any finite ceiling $K_{\max}$ in finite time; under *weak assimilation* ($\delta(K_{\max}) < w(H_{\min})$), the sink load at the ceiling is still positive — $\dot K = w(H_{\min}) - \delta(K_{\max}) > 0$ at $K = K_{\max}$ — so $K$ exits above $K_{\max}$ in finite time. In both cases the viability kernel (Aubin, 1991) of the constraint set $\{ S \ge S_{\min},\ 0 \le K \le K_{\max} \}$ is empty. In ledger language: in a closed ledger without recycling, any positive output floor forces an empty viability kernel — positive throughput accumulates in the sink forever.

### 4.4 Mechanism typing: routing is never determined by diagnostic labels

Extraction has at least three distinct physical meanings — standing-stock culling (present extraction removes reproductive stock directly), recruitment suppression (present use prevents future recruits without immediate adult removal), and weak viability coupling (use has limited or indirect effect on reproduction). In the ledger, standing-stock culling enters as an outflow from the standing-stock compartment; the typing is the physical module's, not the diagnostic's: a diagnostic label such as "unsustainable portion" never determines physical destination. Where an application splits extraction between culling and recruitment suppression — $C_{\mathrm{stock}} = \psi qEN$, $C_{\mathrm{recruit}} = (1-\psi) qEN$ for $\psi \in [0,1]$ — the assignment requires evidence per channel: literally harvesting pre-recruit stages is a harvest of existing units and routes to product and waste fractions; habitat-induced failed recruitment is a prevented inflow, and routing it into product or waste would create mass that was never in the stock; damage to the capital stock itself (aquifer compaction, severe soil loss) is not a $\psi$ channel at all but a slow drift in capacity or a transfer to the inert sink. (Illustrative calibrated $\psi$ values for named domains are tabulated in the supplementary material at their declared illustrative status.)

### 4.5 Support saturation and the logistic limit

Two registered results control what the ledger's stock equation becomes when its support pool saturates; both are singular reductions with explicit scope.

**Theorem 2 (Support-saturated logistic stock limit).** *Fix $T < \infty$ and nonnegative parameters $\mu, \delta, c, q$. For $\kappa > 0$, assume $A_\kappa$ is measurable with $A_\kappa(t) \ge a_0 > 0$, $0 \le X_\kappa(t) \le X_{\max}$, and common effort $E \in L^\infty([0,T])$. Let $X_\kappa$ solve*
$$
\dot X_\kappa = \mu X_\kappa \frac{A_\kappa}{\kappa + A_\kappa} - \delta X_\kappa - c X_\kappa^2 - qE(t) X_\kappa
$$
*and $X_0$ solve the limiting equation from the same initial value. Then the vector-field defect obeys*
$$
\left| \mu X_\kappa \frac{A_\kappa}{\kappa + A_\kappa} - \mu X_\kappa \right| \le \mu X_{\max} \frac{\kappa}{a_0},
$$
*and $\sup_{t \le T} |X_\kappa(t) - X_0(t)| = O(\kappa)$ by Grönwall's inequality; if $\mu > \delta$ and $c > 0$ the limit has the logistic form $\dot X_0 = rX_0(1 - X_0/K_{\mathrm{log}}) - qE(t)X_0$ with $r = \mu - \delta$, $K_{\mathrm{log}} = (\mu - \delta)/c$.*

*Proof.* The defect bound is $|A_\kappa/(\kappa + A_\kappa) - 1| = \kappa/(\kappa + A_\kappa) \le \kappa/a_0$; Grönwall's lemma applied to the difference of the two solutions converts the bounded vector-field defect into the $O(\kappa)$ trajectory bound on $[0,T]$; the logistic form is elementary algebra. $ \square $

The saturation identity is pointwise on the interior support region and not uniform through the depleted-pool boundary: for every $\kappa > 0$, $A/(\kappa + A) = 0$ at $A = 0$, so support saturation does not justify replacing the factor by one on or uniformly near the boundary. It does not eliminate the detritus compartment, make $A$ constant near its boundary, or transform the memory or effort laws — an ecological stock-equation identity, not a full-core reduction and not a transfer principle for bifurcation thresholds.

---

## 5. Conservation and Positivity of the Closed Ledger

### 5.1 The natural-block mass identity

**Theorem 3 (Mass conservation and the natural-block mass identity).** *(a) For the six-compartment system of Section 4.2, $\frac{d}{dt}\mathbf{1}^\top z = 0$: the total mass $M_6 = X + U + A + G + P + W$ is constant along every trajectory on which the solution is defined. (b) For the closed natural block (2), mass leaves the natural block exactly at the extraction rate:*
$$
\frac{d}{dt}\left( N + A^{\mathrm{act}} + A^{\mathrm{geo}} + U \right) = -qEN, \tag{3}
$$
*and with optional mining restored ($C^A > 0$) the identity becomes $\frac{d}{dt}(N + A^{\mathrm{act}} + A^{\mathrm{geo}} + U) = -qEN - C^A \sigma$, the mining term donor-limited exactly as extraction is.*

*Proof.* (a) With $M_6 = \mathbf{1}^\top z$, $\dot M_6 = \mathbf{1}^\top S(\alpha,\rho)\, v = 0$ because each column of $S$ sums to zero; term by term: assimilation gives $g - g = 0$; mortality gives $-m + m = 0$; decomposition gives $-d_U + d_U = 0$; geological exchange gives $e_{GA} - e_{GA} = 0$ and $-e_{AG} + e_{AG} = 0$; mining gives $-c_G + c_G = 0$; and the harvest and retirement terms satisfy $-h + \alpha h + (1-\alpha)h = 0$ and $\rho r_P - r_P + (1-\rho) r_P = 0$. (b) Differentiate the four coordinates of (2) and add, using $B = R + T$:
$$
\dot N + \dot A^{\mathrm{act}} + \dot A^{\mathrm{geo}} + \dot U
= (R - qEN) + (-B + e_{GA} - e_{AG} + \gamma_U U) + (-e_{GA} + e_{AG}) + (T - \gamma_U U)
= R - qEN - R - T + \gamma_U U + T - \gamma_U U = -qEN.
$$
Every internal flux cancels pairwise; the only surviving term is extraction. With mining restored, the donor equation loses the additional outflow $C^A \sigma$, which enters the identity additively; the mined fraction routes out of the four-coordinate natural block to the product or waste compartments of Section 4.2, whose matrix records the mining column as an internal transfer between compartments outside the block — the two statements are consistent because the block boundary, not the ledger boundary, is crossed. $ \square $

The identity states that mass leaves the natural block at the extraction rate — not at the consumption rate, the product rate, or any derived target rate. The balance is governed by the primitives of the ledger, not by downstream demand.

### 5.2 The yield-routing obligation

Rule (iii) of Section 2.3 is enforced by construction here: a transformation with yield below one must route the omitted fraction to a represented compartment or a declared boundary flow. In the six-compartment scaffold the harvest split $\alpha h \to U$, $(1-\alpha) h \to P$ and the retirement split $\rho r_P \to U$, $(1-\rho) r_P \to W$ discharge the obligation explicitly, and the column sums of $S(\alpha,\rho)$ are zero *because* the routing is complete. The failure mode is Proposition 2's second witness: a bookkeeping that silently drops a moiety makes the balance hold only after the moiety is dropped — the ledger then certifies a conservation law for a system it no longer represents. The obligation is conditional on the routing choices of the application and is declared, not assumed, for every transformation used below.

### 5.3 Orthant invariance

**Theorem 4 (Orthant invariance of the closed ledger).** *The nonnegative orthant in $(N, A^{\mathrm{act}}, A^{\mathrm{geo}}, U)$ is forward invariant for the closed natural block (2).*

*Proof.* The right-hand side is locally Lipschitz on a neighbourhood of the closed orthant: each Michaelis–Menten factor $s$, $\sigma$ is smooth for nonnegative arguments. Face by face. On $A^{\mathrm{geo}} = 0$ one has $\sigma = 0$, hence $e_{GA} = 0$ and $\dot A^{\mathrm{geo}} = e_{AG} = \omega_A A^{\mathrm{act}} \ge 0$. On $A^{\mathrm{act}} = 0$ one has $s = 0$, so $R = B = T = e_{AG} = 0$ and $\dot A^{\mathrm{act}} = e_{GA} + \gamma_U U \ge 0$. On $N = 0$, extraction and uptake vanish and $\dot N = 0$. On $U = 0$, $\dot U = T \ge 0$. The vector field belongs to the tangent cone at every boundary point, and the tangent-cone invariance theorem (Aubin, 1991) yields forward invariance of the orthant. $ \square $

The classical lineage of these statements is the compartmental-systems nonnegativity theory (Jacquez and Simon, 1993); the donor-limitation condition is the exact sufficiency requirement — algebraic cancellation alone does not establish invariance.

### 5.4 No interior rest at positive effort

**Theorem 5 (No interior rest at positive effort).** *The closed natural block (2) admits no rest point with all four coordinates positive and $E > 0$.*

*Proof.* At a rest point all four derivatives vanish, so $\frac{d}{dt}(N + A^{\mathrm{act}} + A^{\mathrm{geo}} + U) = 0$; but Theorem 3 gives $\frac{d}{dt}(N + A^{\mathrm{act}} + A^{\mathrm{geo}} + U) = -qEN < 0$ at an interior point with $E > 0$ (both $q$ and $N$ positive). Contradiction. $ \square $

The argument records exactly which assumptions do the work: a positive extraction rate at a positive stock makes the natural block lose mass, and a rest point cannot lose mass. The same reasoning excludes the working point $(N^*, A^{\mathrm{act}*}) = (89.526, 397.87)$ of the registered parameterisation from being a rest point at $E = E^* \approx 2.090$, since there $R^* = qE^*N^* \approx 0.187 > 0$ keeps $\dot N \neq 0$.

### 5.5 The extinction–geochemical rest set

**Theorem 6 (Extinction–geochemical rest set).** *With vanishing extraction ($E \equiv 0$), the rest points of (2) are exactly the two families*
$$
\mathcal{R}_0 = \bigl\{ N = 0,\ U = 0,\ A^{\mathrm{act}} = A^{\mathrm{eq,intrinsic}}\,\sigma(A^{\mathrm{geo}}),\ A^{\mathrm{geo}} \ge 0 \bigr\}
\cup
\bigl\{ N = K,\ U = \kappa_A K s/\gamma_U,\ A^{\mathrm{act}} = A^{\mathrm{eq,intrinsic}}\,\sigma,\ A^{\mathrm{geo}} \ge 0 \bigr\},
$$
*where in the second family $s = A^{\mathrm{act}}/(A^{\mathrm{act}} + A_0)$ is evaluated at the solution — and together with the frozen-biomass face $\{(N, 0, 0, 0) : N \ge 0\}$, on which $s = 0$ identically and the biomass is frozen at its initial value. With $E > 0$ no rest point exists at all (Theorem 5).*

*Proof.* With $E \equiv 0$, set the four derivatives to zero. From $\dot A^{\mathrm{geo}} = -e_{GA} + e_{AG} = 0$: $e_{GA} = e_{AG}$, i.e. $\omega_A [A^{\mathrm{eq,intrinsic}}]_+ \sigma = \omega_A A^{\mathrm{act}}$, so $A^{\mathrm{act}} = [A^{\mathrm{eq,intrinsic}}]_+ \sigma$ — the geological-exchange balance, in which the active pool is pinned to the donor-scaled intrinsic target. From $\dot N = R = 0$: $rN(1 - N/K)s = 0$. If $A^{\mathrm{geo}} > 0$ then the geo-balance pins $A^{\mathrm{act}} > 0$, so $s > 0$ and $N = 0$ or $N = K$. At the boundary $A^{\mathrm{geo}} = 0$ the geo-balance forces $A^{\mathrm{act}} = 0$ (since $\sigma(0) = 0$), hence $s = 0$ and $\dot N = 0$ for every $N \ge 0$; with $U = 0$ the remaining equations vanish identically, so the frozen-biomass face $\{(N, 0, 0, 0) : N \ge 0\}$ is a rest set. The constitutive laws carry no basal mortality independent of the support factor; the face is part of the declared model, not a defect of the balance. From $\dot U = T - \gamma_U U = 0$: $U = T/\gamma_U = \kappa_A N s/\gamma_U$, which vanishes in the $N = 0$ branch and is positive in the $N = K$ branch. From $\dot A^{\mathrm{act}} = -B + e_{GA} - e_{AG} + \gamma_U U = -(R + T) + 0 + \gamma_U U$: this vanishes in both branches, since $R = T = \gamma_U U$ holds there. The two families together with the frozen-biomass face are exactly the stated rest set. "Geochemical" names the mechanism: the active pool rests at the donor-scaled intrinsic target, and apart from the frozen-biomass face, no rest point exists away from extinction or carrying capacity. $ \square $

### 5.6 Extraction integrability

**Theorem 7 (Integrable extraction).** *Let $M = N + A^{\mathrm{act}} + A^{\mathrm{geo}} + U$. Then $M(t) = M(0) - \int_0^t qE(s)N(s)\, ds \ge 0$, so*
$$
\int_0^\infty qE(s)N(s)\, ds \le M(0) < \infty;
$$
*with mining restored, $\int_0^\infty \bigl( qE(s)N(s) + C^A \sigma(s) \bigr) ds \le M(0)$.*

*Proof.* Theorem 3(b) gives $\dot M = -qEN$; integrating, $M(t) = M(0) - \int_0^t qEN$. Theorem 4 gives $M(t) \ge 0$ for all $t$, so $\int_0^t qEN \le M(0)$ for every $t$; the integral is nondecreasing in $t$ and bounded, hence convergent with the stated bound. The mining-restored case is identical with the integrand of Theorem 3(b), and orthant invariance carries over with it: at $A^{\mathrm{geo}} = 0$ one has $\sigma = 0$, so the donor face satisfies $\dot A^{\mathrm{geo}} = e_{AG} \ge 0$ exactly as in the closed block, while the other three faces are unchanged — mining is an outflow from $A^{\mathrm{geo}}$ and the positivity of $M(t)$ used in the bound is Theorem 4 applied to the restored system. $ \square $

Total extraction against the finite donor budget is integrable — the formal content of "finite donor budget" — and the budget is the initial natural-block mass, not the initial living stock alone.

### 5.7 Counterexample: positive extraction does not imply finite exhaustion

**Counterexample 1 (Proportional extraction).** *For donor-controlled proportional extraction $\dot S = -kS$ with $k > 0$ and $S(0) > 0$, the stock satisfies $S(t) = S(0) e^{-kt} > 0$ for every finite $t$: the stock approaches zero asymptotically and is never exhausted in finite time, $\tau_0 = \infty$. The time to a positive barrier $B > 0$ is $\tau_B = k^{-1} \log(S(0)/B)$, finite for $B > 0$ but diverging as $B \to 0$.*

Positive extraction alone therefore does not imply finite exhaustion: the exhaustion reading requires a floor $B > 0$ and a uniform positive rate of net loss (the hypothesis that Theorem 8 of Section 7 makes precise). The counterexample also fixes the exhaustion referent: exhaustion of a compartment is not exhaustion of a moiety, which is not failure of a functional stock, which is not depletion of a reserve — the four statements differ, and the classification labels of Section 2.3(v) keep them in different columns.

---

## 6. Services as Readouts

### 6.1 The service readout and the feasible balance domain

A *service* is a typed readout of the material state, never conserved mass. On the ledger (1), declare a readout map $\mathcal{O}(x, u, \theta)$ — typically linear in the primitives, $s = Q(\theta) v(x, u)$ — and a declared demand set $\mathcal{D}(t)$; the contemporaneous balance is the vector $b_i(t) = s_i(t) - d_i(t)$. Services do not appear in the mass-balance equations; they are functions of the state, and a service deficit does not imply a mass deficit, nor a mass surplus a service surplus.

**Definition 1 (Feasible balance domain).** For an admissible operating set $\mathcal{U}(x,t)$ and a declared demand set $\mathcal{D}(t)$,
$$
\mathcal{B}(x,t) = \bigl\{ \mathcal{O}(x,u,\theta) - d : u \in \mathcal{U}(x,t),\ d \in \mathcal{D}(t) \bigr\}.
$$

When $\mathcal{O}$ is linear in $u$ and $\mathcal{U}(x,t)$, $\mathcal{D}(t)$ are convex, $\mathcal{B}(x,t)$ is convex. This domain is the object on which any scalar certificate claim must be checked — the setting of Theorem 12 in Section 11.

### 6.2 Support provenance and the directional support gap

The *support provenance* of a moiety is the declared set of compartments and fluxes that can supply it; the *regenerative support* $\Gamma_{\mathrm{reg}}(x,t)$ is the part of the attainable balances supplied by regeneration rather than by drawing down a stock. For a target balance vector $\bar s$,

$$
\alpha_{\mathrm{reg}}(\bar s; x,t) = \sup\bigl\{ \alpha \in [0,1] : \alpha \bar s \in \Gamma_{\mathrm{reg}}(x,t) \bigr\}
$$

is the directional regenerative-support fraction, and the *directional support gap* is the vector $(1 - \alpha_{\mathrm{reg}}) \bar s$: the part of the target not coverable by regenerative support at that state. The directional decomposition identifies which support direction is insufficient; it does not by itself identify the mechanism of the insufficiency.

### 6.3 The componentwise deficit and the specialization identity

The physical deficit on the unreduced ledger is $\Delta^{\mathrm{phys}}(t) = C(t) - \widehat{M}^\top S(t)$, where $\widehat{M}$ is the declared demand-coverage matrix mapping the moiety readout $S = Cx$ into the units of the demand-coverage vector $C(t)$ — rows indexed by covered services, columns by moieties, entries the declared stoichiometric coefficients of the coverage convention (the hat distinguishes it from the scalar total mass $M$ of Section 5.6): demand coverage less than supply, component by component. In the single-resource specialization of the closed natural block it collapses to an exact identity:

**Lemma 1 (Specialization identity).** *On every trajectory of the specialized system ($\mu = \nu = \rho = 0$, $C^A = 0$),*
$$
qEN - R(N, A^{\mathrm{act}}) = -\dot N, \qquad
\Lambda(t) := \bigl[ qEN - R \bigr]_+ = \bigl[ -\dot N \bigr]_+ .
$$

*Proof.* From the first equation of (2), $\dot N = R - qEN$; rearranging gives $qEN - R = -\dot N$; the positive parts are equal because the two arguments are identical. $ \square $

The identity holds by direct algebra from the resource equation, and the decline pressure $\Lambda(t)$ is exactly the positive part of the stock's decline rate. This is the exact shared object with the companion dynamics paper: the memory–effort pair of Section 4.1 is driven by $qEN - R$, and the identity is what transfers between the ledger and the institutional dynamics — nothing else does.

**The hand-off projection.** Under the institutional-failure specialization, the macroeconomic block, prices, and demand do not appear in $(\dot N, \dot A^{\mathrm{act}}, \dot U, \dot Z, \dot E)$: each of the five right-hand sides depends only on the block's own variables and the delayed memory, and none contains the macroeconomic states, prices, or demand. The ecological–institutional subsystem is an exact closed projection for every parameter value, with no singular limit required. This is a projectable reduction in the sense of the semiconjugacy condition $D\pi(y) f(y) = F(\pi(y))$ on the history phase space, and it is the object the companion receives.

**The non-reduction boundary.** There is no exact dynamic reduction from the closed primitive finite-donor ledger to the open working system — not as a projectable reduction and not as a regular perturbation. The reasons are mathematical:

1. The primitive ledger uses the intrinsic donor-limited target $A^{\mathrm{eq,intrinsic}}$; the working system uses the derived target $A^{\mathrm{eq,W}} = A^{\mathrm{eq,intrinsic}} + \kappa_A K/\omega_A$.
2. At the working equilibrium the two $A^{\mathrm{act}}$ vector fields differ by an $O(1)$ term.
3. The working point requires continuing geological support — the flux $\omega_A(A^{\mathrm{eq,W}} - A^{\mathrm{act,*}}) = 4.652133\ldots$ stock units per year, supplied every year by a donor the working system treats as a parameter — and is not a rest point of the closed finite-donor system (Theorem 5).
4. The cumulative donor-draw quantity $\varepsilon_G(T) = G_0^{-1}\int_0^T |e_{GA} - e_{AG}|\, dt$ is a diagnostic of the derived-target completion, not a trajectory-tracking error between the two fields; no finite-time tracking theorem between the completions holds.
5. The closed primitive system makes sustained extraction integrable (Theorem 7) and therefore cannot possess the working positive-flux rest indefinitely.

The mapping type for exact dynamic reduction is rejected; the permitted relation is analogy for shared mechanism language plus diagnostic reconstruction of omitted mass flows. The companion's global periodic results are properties of its reduced systems and do not transfer to the closed primitive ledger. In the other direction, the working system is an open projection: omitted turnover is routed to a diagnostic detritus or inert sink, imposed recharge corresponds to geological draw, and the reduced trajectory's mass discrepancy is reconstructible from the omitted flows.

**The frozen-donor limit and its scope.** Rescaling the donor as $G = G_0 g$ with $g(0) = 1$ gives $\dot g = -G_0^{-1}(e_{GA} - e_{AG})$. The limit $G_0 \to \infty$ freezes $g$ but does not restore the working completion's derived target: the limiting recharge field still uses $A^{\mathrm{eq,intrinsic}}$, not $A^{\mathrm{eq,W}}$, so the scaling is not a regular perturbation of the working vector field. Local Hopf persistence of the working system under this primitive scaling is not claimed; a different derived-target completion would be required before a regular-perturbation theorem could be formulated.

---

## 7. The Depletion-Diagnostics Taxonomy

### 7.1 The three quantities

Let $A_{\min}$ be a declared threshold for the active abiotic pool with $A > A_{\min}$.

**Definition 2 (Gross turnover intensity).** With assimilation $g(X,A) > 0$, the gross turnover intensity is $J_A^{\mathrm{gross}} = g(X,A)/A$.

Neither gross turnover nor any function of it is a time to depletion. The implication $g > 0 \Rightarrow \dot A < 0$ is **false** in general: at an interior steady state, $g$ can be positive while decomposition and geological transfer balance it exactly, so that $\dot A = 0$. Gross uptake measures throughput or dependency; net depletion is a balance property. This false-implication record is the first rung of the taxonomy and governs every application below.

**Definition 3 (Frozen-rate local ratio).**
$$
H_A^{\mathrm{loc}}(t) = \frac{A(t) - A_{\min}}{\bigl[ -\dot A(t) \bigr]_+},
$$
with the extended-real convention $H_A^{\mathrm{loc}} = +\infty$ when $\dot A \ge 0$ — correctly reporting no current net decline at a stationary or replenishing state. The ratio is still not a trajectory forecast: it freezes the current net rate. If the fluxes change with $A$, policy, climate, prices, or other states, the realized threshold time can differ substantially.

**Definition 4 (Scenario-conditioned hitting time).** For a fully specified dynamical model, policy or scenario $\pi$, disturbance history $d$, and initial state $x_0$,
$$
T_A(x_0; \pi, d) = \inf\bigl\{ t \ge 0 : A^{\pi,d}(t; x_0) \le A_{\min} \bigr\},
$$
with $T_A = +\infty$ if the threshold is never reached. Under parameter, observation, and scenario uncertainty the appropriate output is a distribution or robust interval of $T_A$, not a single universal date.

The three quantities answer different questions and must not share one depletion-horizon label:

| Quantity | Question answered |
|---|---|
| $J_A^{\mathrm{gross}}$ | How strongly does the system depend on, or turn over, the pool at the current gross rate? |
| $H_A^{\mathrm{loc}}$ | If the current net decline were frozen, what is the local stock-to-rate ratio? |
| $T_A$ | Under a stated model, policy, and disturbance scenario, when is the threshold first reached? |

### 7.2 The threshold-horizon bracket

**Theorem 8 (Local threshold-horizon bracket).** *Let $A : [0,T] \to \mathbb{R}$ be absolutely continuous with $A(0) > A_{\min}$, let $v_0 > 0$ and $0 < \varepsilon < 1$, set $H_0 = (A(0) - A_{\min})/v_0$, and suppose $T \ge H_0/(1-\varepsilon)$ and*
$$
(1-\varepsilon) v_0 \le -\dot A(t) \le (1+\varepsilon) v_0
$$
*for almost every $t$ while $A$ stays above $A_{\min}$. Then a first crossing time $H$ exists no later than $H_0/(1-\varepsilon)$, and*
$$
\frac{H_0}{1+\varepsilon} \le H \le \frac{H_0}{1-\varepsilon}, \qquad |H - H_0| \le \frac{\varepsilon}{1-\varepsilon} H_0 .
$$

*Proof.* If no crossing occurs before $t_* = H_0/(1-\varepsilon)$, absolute continuity gives $A(t_*) \le A(0) - (1-\varepsilon) v_0 t_* = A_{\min}$, a contradiction; hence $H \le t_*$. Integrating both rate bounds over $[0,H]$ and using $A(0) - A(H) = v_0 H_0$ gives the two-sided bracket: from the upper rate bound, $v_0 H_0 \le (1+\varepsilon) v_0 H$, and from the lower rate bound, $v_0 H_0 \ge (1-\varepsilon) v_0 H$. $ \square $

The bracket bounds the frozen-rate ratio's error under declared rate bounds, and nothing more: it fails when depletion reverses, the rate approaches zero, or feedback moves the trajectory outside the declared bounds. Its companion is Counterexample 1, which shows that the uniform margin $\varepsilon > 0$ is load-bearing in both directions — proportional extraction never exhausts in finite time.

### 7.3 The flux-bounding envelope theorem

**Theorem 9 (Flux-bounding envelopes).** *Let the primitive fluxes and boundary transfers satisfy componentwise bounds $v(t) \in [\underline{v}(t), \overline{v}(t)]$ and $b(t) \in [\underline{b}(t), \overline{b}(t)]$ for all $t \in [0,T]$. Write $M^{+} = \max\{M, 0\}$ and $M^{-} = \max\{-M, 0\}$ entrywise, and define for each moiety $m$ the envelope integrands*
$$
\varphi_m(\tau) = (CN)_{m}^{+} \underline{v}(\tau) - (CN)_{m}^{-} \overline{v}(\tau) + C_{m}^{+} \underline{b}(\tau) - C_{m}^{-} \overline{b}(\tau),
$$
$$
\psi_m(\tau) = (CN)_{m}^{+} \overline{v}(\tau) - (CN)_{m}^{-} \underline{v}(\tau) + C_{m}^{+} \overline{b}(\tau) - C_{m}^{-} \underline{b}(\tau),
$$
*and the envelopes*
$$
\underline{S}_m(t) = S_m(0) + \int_0^t \varphi_m(\tau)\, d\tau, \qquad \overline{S}_m(t) = S_m(0) + \int_0^t \psi_m(\tau)\, d\tau.
$$
*Then $S_m(t) \in [\underline{S}_m(t), \overline{S}_m(t)]$ for all $t \in [0,T]$ and all $m$.*

*Proof.* By Theorem 1's structure, $\dot S_m = (CNv + Cb)_m$. For each row $m$ and time $\tau$, the linear form $(CN)_m v$ over the box $[\underline{v}(\tau), \overline{v}(\tau)]$ satisfies the pointwise bounds
$$
(CN)_{m}^{+} \underline{v}(\tau) - (CN)_{m}^{-} \overline{v}(\tau) \;\le\; (CN)_m v(\tau) \;\le\; (CN)_{m}^{+} \overline{v}(\tau) - (CN)_{m}^{-} \underline{v}(\tau),
$$
attained at the extreme points of the box — a coefficient with positive row entry $c_j > 0$ is minimized at $\underline{v}_j$ and maximized at $\overline{v}_j$, and one with negative row entry $c_j < 0$ is minimized at $\overline{v}_j$ and maximized at $\underline{v}_j$, which is exactly the stated pairing of the positive and negative parts. The same argument applies to $C_m b(\tau)$, and adding gives $\varphi_m(\tau) \le \dot S_m(\tau) \le \psi_m(\tau)$. Integrating over $[0,t]$ yields the stated envelope. $ \square $

**Corollary 1 (Flux-derived barrier certificate).** *If $\underline{S}_m(t) \ge \underline{B}_m(t)$ and $\overline{S}_m(t) \le \overline{B}_m(t)$ for all $t \in [0,T]$ and all $m$, then every trajectory compatible with the flux bounds is barrier-safe on $[0,T]$.*

*Proof.* By Theorem 9 every such trajectory satisfies $\underline{S}_m(t) \le S_m(t) \le \overline{S}_m(t)$; the certificate conditions sandwich $S_m$ between the barriers. $ \square $

Two qualifications are part of the theorem. The bounds are conservative: they hold for *all* flux selections in the declared boxes, including selections that are not jointly realizable by the coupled dynamics, so the certificate may fail when a trajectory with jointly realizable fluxes would pass; attainability requires solving or bounding the coupled system. And the envelope is an interval computation on the flux data, not a forecast: it says nothing about what the fluxes will be, only about what every admissible flux path implies for the stock.

---

## 8. First-Passage Semantics for the Public-Data Proxies

### 8.1 Two objects, not one

The ledger's own first-passage object is the model hitting time of Definition 4 — a quantity on trajectories of the mass-conserved ledger or of a named reduced system. The public-data quantities of Section 9 are constructed proxies on observed series. The distinction is the entry discipline of this section: the surrogates below do not compute the ledger's hitting time, do not complete the ledger stochastically, and do not identify physical failure thresholds.

### 8.2 The observed-drift Brownian surrogate

**Definition 5 (Observed-drift Brownian surrogate).** Let $A_0$ be the latest observed anomaly and $\mu = \widehat\mu < 0$ the fitted drawdown rate. On the scale of the tabulated series define
$$
A(t) = A_0 + \mu t + \sigma W_t, \qquad A(0) = A_0 > A_{\min}^{\mathrm{win}},
$$
where $W$ is a standard Wiener process, $\sigma > 0$ a chosen noise scale, and the process is stopped at first reaching the record-relative barrier $A_{\min}^{\mathrm{win}}$.

This is a statistical surrogate for the empirical trend extrapolation. It is not a hydrological constitutive law, is not mass-conserving, and is not a perturbation or stochastic completion of the ledger's active-pool equation or of the finite-donor primitive system of Section 2.2. The non-completion non-claim is part of the definition.

### 8.3 The inverse-Gaussian groundwater first passage

**Theorem 10 (Inverse-Gaussian first passage).** *Let $T_{\mathrm{GW}} = \inf\{ t > 0 : A(t) \le A_{\min}^{\mathrm{win}} \}$ for the process of Definition 5 and $d = A_0 - A_{\min}^{\mathrm{win}} > 0$. Conditional on treating $\mu$ and the barrier as fixed,*
$$
T_{\mathrm{GW}} \sim \mathrm{IG}(\nu, \lambda), \qquad \nu = \frac{d}{|\mu|}, \qquad \lambda = \frac{d^2}{\sigma^2},
$$
*in the mean–shape parameterization; in particular $\mathbb{E}[T_{\mathrm{GW}}] = \nu$ and $\operatorname{Var}(T_{\mathrm{GW}}) = \nu^3/\lambda = d\,\sigma^2/|\mu|^3$.*

*Proof.* The first-passage time of a Brownian motion with constant negative drift to a lower barrier is inverse Gaussian — the classical first-passage result (Chhikara and Folks, 1989; Redner, 2001) — with the stated mean and shape parameters; the standard inverse-Gaussian moments give the displayed mean and variance. $ \square $

The mean of the stochastic surrogate equals the deterministic trend-to-window-minimum ratio of Section 9.1; that equality is the precise sense in which the tabled groundwater numbers are first-passage means of a declared surrogate.

**Corollary 2 (Zero-noise limit and median).** *As $\sigma \to 0^+$, $T_{\mathrm{GW}}$ converges in probability to the deterministic ratio $d/|\mu|$, and at $\sigma = 0$ the deterministic trajectory reaches the barrier exactly there. For every finite $\sigma > 0$ the inverse-Gaussian median $m$ satisfies*
$$
m < \nu, \qquad F_T(\nu) = \frac{1}{2} + e^{2\lambda/\nu}\,\Phi\!\left( -2\sqrt{\lambda/\nu} \right) > \frac{1}{2}.
$$

*Proof.* Evaluate the inverse-Gaussian CDF $F_T(t) = \Phi(\sqrt{\lambda/t}\,(t/\nu - 1)) + e^{2\lambda/\nu}\Phi(-\sqrt{\lambda/t}\,(t/\nu + 1))$ at $t = \nu$: the first term is $\Phi(0) = 1/2$ and the second is strictly positive for finite $\lambda$, so the median lies strictly below the mean; the concentration statement follows from the variance. $ \square $

These are conditional distributional statements about the surrogate. They are not corrections to the tabled years, and they do not show that physical water mass is depleted faster.

### 8.4 The record-relative barrier discipline

The barrier $A_{\min}^{\mathrm{win}}$ is selected from the same finite observation window used to estimate $\widehat\mu$. It is therefore a path-dependent, record-relative threshold, not an independently identified hydrological failure floor; future passage below it represents a record-breaking stress event under the surrogate, not physical exhaustion. A passage time computed against a barrier selected from the same observation window is a record-breaking stress statistic, not a physical exhaustion date. Three boundary facts complete the discipline.

1. **Already-at-minimum.** If $A_0 = A_{\min}^{\mathrm{win}}$, the stopping-time convention gives $T_{\mathrm{GW}} = 0$ deterministically for every $\sigma$; the inverse-Gaussian family has a degenerate boundary limit concentrated at zero, and $\mathrm{IG}(0,0)$ is not an ordinary inverse-Gaussian distribution. Zero cells report zero relative to the selected observational barrier — not zero physical uncertainty and no confirmation of collapse.
2. **Independent physical thresholds.** If an independent physical threshold $A^\sharp < A_{\min}^{\mathrm{win}}$ is specified, the same constant-drift surrogate gives the conditional mean $\mathbb{E}[T^\sharp] = (A_0 - A^\sharp)/|\mu|$, longer than the record-relative proxy because the barrier is lower. This is a statement within the surrogate, not a general lower-bound theorem for the physical ledger, whose drift and state coupling may differ.
3. **Classification.** The load-bearing content is the interpretation boundary itself: a record-relative barrier makes the passage time a property of the observation window, and no reading of the tabled numbers escapes that qualification.

### 8.5 The geometric-Brownian fisheries first passage

**Theorem 11 (Geometric-Brownian first passage).** *Let $dB_t = -hB_t\, dt + \sigma B_t\, dW_t$ under the Itô convention with $h > 0$ and $0 < B_{\min} < B_0$, and $T_{\mathrm{fish}} = \inf\{ t > 0 : B_t \le B_{\min} \}$. Then*
$$
T_{\mathrm{fish}} \sim \mathrm{IG}(\nu_F, \lambda_F), \qquad
\nu_F = \frac{\log(B_0/B_{\min})}{h + \sigma^2/2}, \qquad
\lambda_F = \frac{\log(B_0/B_{\min})^2}{\sigma^2},
$$
*so $\mathbb{E}[T_{\mathrm{fish}}] = \log(B_0/B_{\min})/(h + \sigma^2/2)$; as $\sigma \to 0^+$ this converges to the deterministic pure-decay horizon when $h = F$ and $B_{\min} = B_{\lim}$.*

*Proof.* Itô's lemma (Øksendal, 2003) gives $d\log B_t = -(h + \sigma^2/2)\, dt + \sigma\, dW_t$, so the logarithmic threshold is a Brownian first-passage problem with initial distance $\log(B_0/B_{\min})$ and downward drift $h + \sigma^2/2$; Theorem 10 applies. $ \square $

For fixed arithmetic drift and the Itô parameterization, the finite-noise mean is strictly shorter than the deterministic horizon. This is a property of the chosen surrogate parameterization; it is not a universal claim that environmental variability accelerates physical biomass loss.

### 8.6 The constant-production phosphate passage time

Under the deterministic surrogate $\dot R = -P$ with constant production $P > 0$, the first-passage time to a fixed threshold $R_{\min} \in [0, R_0)$ is
$$
T_{\mathrm{phos}} = \frac{R_0 - R_{\min}}{P},
$$
the reserve-life ratio being the $R_{\min} = 0$ special case and a threshold fraction $\varepsilon R_0$ giving $(1-\varepsilon) R_0/P$. This is a conditional reserve-classification proxy under constant production; because reserves are an economic classification rather than a fixed physical stock, it is not a forecast of geological exhaustion without an explicit resource and production model.

### 8.7 The explicit non-claims

The first-passage semantics close with seven explicit non-claims, all of which hold in this article:

1. The Brownian and geometric-Brownian processes are not stochastic completions of the ledger and do not conserve its mass compartments.
2. No theorem relates $\widehat\mu$ to $-\dot A$ of the reduced systems, to the finite-donor primitive system, or to the institutional delay equations.
3. The model hitting time $T_A$ of Definition 4 is not shown to be inverse Gaussian.
4. The historical groundwater minimum is not an independently identified physical failure barrier.
5. A shorter surrogate median or Itô mean is not evidence of faster physical depletion.
6. The gross active-pool horizon and its productivity-illusion interpretation are not first-passage results treated here.
7. The fisheries calculation is not a stage-structured fisheries model, and the phosphate calculation is not a geological-reserve model.

### 8.8 Parameter and observation uncertainty

The inverse-Gaussian results condition on the drift, barrier, and noise scale. In the groundwater application $\widehat\mu$ is estimated from a finite, potentially autocorrelated record and the barrier is selected from that same record; measurement error, serial dependence, seasonal forcing, spatial aggregation, trend breaks, and common climatic drivers are separate uncertainties, and integrating any of them out yields a predictive mixture rather than a single inverse-Gaussian law. A residual scale estimated from the same window does not by itself identify process noise. No calibrated predictive distribution is claimed.

---

## 9. Applications Classified at Their Exact Status

### 9.1 Groundwater anomaly-persistence indices

The Global Gravity-based Groundwater Product (G3P v1.12; Güntner et al., 2024; the GRACE line it descends from is Tapley et al., 2004) provides monthly groundwater-storage anomalies relative to a reference period rather than absolute aquifer volumes. For a basin-mean anomaly series over the reported April 2002–September 2023 window, the linear-trend anomaly persistence index is

$$
L_{\mathrm{hist}}^{\mathrm{anom}} = \frac{a_{\mathrm{latest}} - a_{\mathrm{hist,min}}}{\bigl[ -\widehat{\dot a} \bigr]_+},
$$

the fitted distance to the series' own historical minimum divided by the fitted decline rate. The four-basin record: Indo-Gangetic $-49.7$ cm/yr with index $\approx 2.7$ yr; North China Plain $-18.6$ with $\approx 7.9$; Central Valley $-16.1$ with $\approx 9.5$; La Mancha $-3.2$ with $\approx 21.4$.

Classification, stated at the product's own status: a statistical anomaly index with units of time — not the physical stock ratio $H_A^{\mathrm{loc}}$ and not a forecast of aquifer exhaustion. Its value depends on the product window, basin mask, anomaly reference, and linear-trend convention; a physical $H_A^{\mathrm{loc}}$ requires an absolute stock estimate and a net stock derivative (aquifer geometry or saturated thickness together with storage parameters), not an anomaly series alone. The index is exactly the record-relative object analyzed in Section 8.4, and its interpretive boundary is that record-relativity.

### 9.2 Component-resolved depletion-horizon tables

Component-resolved depletion horizons on the same public data products are tabulated below, computed without fitting any dynamical parameter of the reduced systems:

| Basin | Trend (cm/yr) | 2023 anomaly (cm) | Horizon to window minimum (yr) |
|---|---|---|---|
| Indo-Gangetic (N. India) | $-49.7$ | $-414$ | $\approx 2.7$ |
| North China Plain | $-18.6$ | $-145$ | $\approx 7.9$ |
| Central Valley (US) | $-16.1$ | $-84$ | $\approx 9.5$ |
| La Mancha (Spain) | $-3.2$ | $-20$ | $\approx 21.4$ |
| High Plains (US) | $-7.9$ | $-160$ | already at minimum |
| global mean | $-0.4$ | $-14$ | $\approx 47.6$ |

The basin rows are reported extractions from the G3P v1.12 basin series, used here only to exhibit the index construction of Section 9.1; the Indo-Gangetic magnitude sits at the high end of published basin-mean groundwater-equivalent trends (typically a few cm yr$^{-1}$ basin-mean), and the column is to be re-derived from the product's basin masks before any numerical reuse. The classification status assigned below does not depend on the magnitudes.

| Country | Reserves (kt) | Reserve-life horizon (yr) |
|---|---|---|
| China | $3{,}400{,}000$ | $\approx 28$ |
| United States | $1{,}000{,}000$ | $\approx 45$ |
| Jordan | $820{,}000$ | $\approx 62$ |
| Morocco | $50{,}000{,}000$ | $\approx 1{,}250$ |
| Australia | $5{,}800{,}000$ | $\approx 2{,}088$ |
| World (reserves) | $74{,}000{,}000$ | $\approx 309$ |
| World (resources, $\varepsilon = 0.10$) | $>300{,}000{,}000$ | $\approx 1{,}125$ |

The fisheries column reports the pure-decay proxy $\mathrm{ADH} = F^{-1}\ln(\mathrm{SSB}_{\mathrm{now}}/(0.2 \max \mathrm{SSB}))$ under current $F$, with median $\approx 1.8$ yr across the 43 assessed stocks with finite SSB and $F$ series (the median is over the qualifying cohort with $F > 0$ and $\mathrm{SSB}_{\mathrm{now}} > 0.2 \max \mathrm{SSB}$; stocks already at or below the reference are reported separately, not included in the median; the RAM Legacy cohort of Ricard et al., 2012).

The scope discipline is the tables' load-bearing content: none of the reported numbers is a computed instance of any model's first-hitting time — the groundwater column is a trend-to-window-minimum extrapolation, the phosphate column a reserve-life ratio, and the fisheries column a pure-decay proxy with recruitment omitted. They are descriptive, component-resolved diagnostics in the taxonomy of Section 7, not dynamical predictions. The equal-weight inverse-horizon score of the four basins still above their window minimum and world phosphate reserves,

$$
\Sigma_{\mathrm{reserves}} \approx \frac{1}{5}\left( \frac{1}{2.7} + \frac{1}{7.9} + \frac{1}{9.5} + \frac{1}{21.4} + \frac{1}{309} \right) \approx 0.130\ \mathrm{yr}^{-1},
$$

is a ranking device, not a componentwise certificate: it mixes basins and reserves, incommensurable objects under the typing of Section 2.1, and is retained only to mark the boundary of legitimate aggregation. The score is exhibited here as the worked instance of Theorem 12: a positive aggregate coexisting with componentwise deficits by construction — admissible as communication, inadmissible as certification.

### 9.3 The phosphate reserve-life ratio

At constant current production $C_G$, the reserve-life ratio is $T_{\mathrm{reserve}} = G_{\mathrm{reserve}}/C_G$; at approximately $74{,}000$ Mt of world reserves and $240{,}000$ kt/yr of production (U.S. Geological Survey, 2026) this is approximately $309$ years. The arithmetic is internally consistent as a reserve-life ratio to zero; it is not a physical exhaustion forecast, because reserve classification changes with prices, technology, exploration, and regulation — the point made forcefully by Illakwahhi, Vegi, and Srivastava (2024) for the single-source USGS data behind the influential phosphate depletion estimates, and documented for copper by Tilton and Lagos (2007). The reserves/resources split discipline of Section 2.3(v) is part of the classification: a resource-threshold calculation $T_{\mathrm{resource},10\%} = 0.9\, G_{\mathrm{resource}}/C_G$ answers a different question and must not share a column with the reserve-life ratio without an explicit convention label; the reserve classification is economic — US reserves have remained near $1{,}000{,}000$ kt while cumulative production since 1996 is of order $600{,}000$ kt — and the resource-based world horizon ($\approx 1{,}125$ yr at $\varepsilon = 0.10$) is more than three times the reserve-based figure; the two-compartment split is what prevents these from being collapsed into one number.

### 9.4 The fisheries removals-only pressure time

When $\mathrm{SSB}_{\mathrm{now}} > B_{\lim} > 0$ and $F_{\mathrm{now}} > 0$, define $R_B = \log(\mathrm{SSB}_{\mathrm{now}}/B_{\lim})$ and

$$
\Theta_F = \frac{R_B}{F_{\mathrm{now}}},
$$

the fishing-only time-to-reference: the crossing time of the deliberately incomplete comparison process $\dot B = -F_{\mathrm{now}} B$. With $B_{\lim} = 0.2 \max \mathrm{SSB}$ this is the construction tabled as ADH in Section 9.2; the two notations are kept because the boundary hypotheses stated here ($F_{\mathrm{now}} > 0$, $\mathrm{SSB}_{\mathrm{now}} > B_{\lim}$) are exactly the cohort conditions under which the Section 9.2 median is computed. It is a removals-only pressure time scale — the time unit comes from rescaling a stock-reference margin by one isolated gross-loss rate. Because recruitment, somatic growth, maturation, natural mortality, density dependence, environmental forcing, and future policy are omitted, $\Theta_F$ is not a net biomass depletion diagnostic, not a demographic hitting-time estimate, and not a member of the $J^{\mathrm{gross}}$–$H^{\mathrm{loc}}$–$T_A$ hierarchy of Section 7. Spawning biomass is not an abiotic support pool. The construction is retained specifically to show why an isolated gross-removal time scale must not be promoted to a net depletion diagnostic.

---

## 10. Domain Templates at Registered Status

### 10.1 The phosphorus template

The phosphorus domain enters at registered template status: an identification ladder for the resource–product–waste–detritus structure of Section 4.2 (phosphate rock → fertilizer → soil pool → runoff, with the mining flux $c_G$ and the recycling routes $\alpha, \rho$), whose constitutive content — the yield and loss functions, the recovery fractions, the price response of the reserve classification — is declared, not established. The ladder declares, for each registered parameter, the observation that would identify it and the prior range: reserve and resource estimates (economic classification; vintage-dependent); mining cost and price response (which determines the reserve-to-resource conversion); recovery fractions $\alpha, \rho$ (material-flow observations at the waste and product stages); soil-pool retention and runoff coefficients (mass-balance closure at the catchment scale); and the yield functions of the fertilizer conversion (stoichiometric, declared per process). The falsification protocol for each routing assumption is registered: a recovery claim is falsified by a mass-balance audit of the claimed route; a retention claim by a catchment closure test. The reserve and production quantities used in Section 9.3 carry their source vintage (U.S. Geological Survey, 2026). No constitutive content is claimed; the ladder is an identification object.

### 10.2 The groundwater template and the two-pool gap

The groundwater template enters at registered status with an admitted object and a declared gap. The admitted object is the one-pool affine approximation behind the anomaly-persistence index of Section 9.1; the two-pool model (active storage with a slow donor pool, the two-compartment structure of Section 2.2) is not established. The registered identification requirements for closing the gap — registered in this section, not discharged — are: geological geometry (aquitard depth and extent); multi-depth heads; pumping tests; tracer, isotope, or water-age evidence; recharge estimates; prior ranges for the storage parameters and the fast–slow coupling; and the discipline that leakage terms may not absorb unexplained residuals. No two-pool claim appears in this article, and no identification of the two-pool hypothesis is claimed.

### 10.3 Extractor-side harvest economics

On the extractor side, the same discipline applies to economic steady states. In the open-access equilibrium of a single-species fishery (Clark, 1990), the bioeconomic equilibrium stock $S_{\mathrm{OA}} = c/(pq)$ is set by cost, price, and catchability — and is infeasible as a management target under a conservation floor $S_{\min} > S_{\mathrm{OA}}$: the unregulated equilibrium lies below the floor, and no open-access trajectory is viable against it. The modified golden rule in its constant-unit-cost form, $g'(S_\delta) = \delta$, sets the optimal steady stock for the discount rate $\delta$ (Clark's general form carries an additional marginal-stock-effect term); a harvest tax shifts the open-access equilibrium to $S_{\mathrm{OA}} = c/((p - \tau)q)$ — the tax moves the economic equilibrium, but it does not move the physical floor. Instrument parameters and constraint thresholds are different objects, and no tax schedule substitutes for a constraint the ledger must satisfy. The growth function $g$ of this paragraph is a declared constitutive readout on the stock for this extractor-side remark only; it is not a primitive of the closed ledger of Section 4.1, and nothing in this section is promoted into the typed ledger.

---

## 11. What the Ledger Does Not Support

### 11.1 No weighted certification

**Theorem 12 (No nonnegative weighting certifies componentwise nonnegativity).** *For every $m \ge 2$ and every weight vector $w \in \mathbb{R}_+^m$, $w \neq 0$, there exist a typed ledger as in Section 2, a demand vector $d$, and an attainable balance vector $s$ in its feasible balance domain (Definition 1) such that the weighted aggregate is nonnegative,*
$$
w^\top s \ge 0,
$$
*while some component of the balance is negative, $s_m < 0$ (equivalently, the corresponding component lies below its floor, $x_m < d_m$). A positive weighted sum never certifies componentwise nonnegativity.*

*Proof.* Take the two-compartment ledger with stock $x = (x_1, x_2) \in \mathbb{R}^2_+$, identity readout $C = I$, and demands $d = (d_1, d_2)$. Every $x \in \mathbb{R}^2_+$ is admissible as an initial condition — attainable here means valid as a ledger state at the witness instant, with the balance computed at that state, and no reachability claim along trajectories is made. The balance vector is $s = x - d$. Fix $w$ and let $j$ be an index with $w_j > 0$; place the deficit in the other component $i \neq j$: pick $x_i < d_i$. Now choose $x_j \ge d_j + \bigl( w_i (d_i - x_i) + \varepsilon \bigr) / w_j$ for any $\varepsilon > 0$. Then
$$
w^\top s = w_i (x_i - d_i) + w_j (x_j - d_j) \ge w_i (x_i - d_i) + w_i (d_i - x_i) + \varepsilon = \varepsilon \ge 0,
$$
while $s_i = x_i - d_i < 0$. The pair $(x, d)$ is the witness for $w$. Because the construction never uses the dynamics, the fact is a property of nonnegative weightings over mixed-sign balances, not of the donor-limited ledger: it transfers verbatim to any readout map whose feasible domain contains such a compensating pair. $ \square $

The reading is the algebraic form of the weak-comparability thesis stated in Section 1.1: scalar summaries may rank and communicate, but certification requires the vector. On any feasible balance domain containing such a compensating pair — and Definition 1's domain is exactly that whenever the operating set admits states with mixed balances — no nonnegative weighting can stand in for the conjunctive criterion of Section 3. The burden of proof sits on the aggregation, not on the componentwise report.

### 11.2 Boundary content

The negative content of the article is stated as such, and none of it is a failure of the framework. The ledger does not support: a stochastic completion (Section 8.7, non-claims 1–3); thermodynamic admissibility (Proposition 3); the two-pool groundwater identification (Section 10.2); any scalar certification of componentwise adequacy (Theorem 12); or any empirical claim about a named basin, aquifer, or fishery beyond the classified descriptive status of the tabulated indicators (Section 9). The sink obstructions of Section 4.3 are empty-kernel mechanisms, the classification results of Section 9 are negative results stated as such, and Counterexample 1 is a limit statement — a quantity that answers exactly one question, stated with that question, is the framework working. The ledger's claim about itself is limited to the accounting layer it establishes.

---

## Data availability

All computations underlying Section 9 are descriptive arithmetic on the cited public data products: the G3P groundwater anomaly product v1.12 (Güntner et al., 2024; GFZ Data Services, doi:10.5880/G3P.2024.001), the U.S. Geological Survey Mineral Commodity Summaries (U.S. Geological Survey, 2026), and the RAM Legacy Stock Assessment Database (Ricard et al., 2012). The parameter tables of Section 4 are declared parameterizations. No other data were used.

## Declaration of competing interest

None.

## References

Aubin, J.-P., 1991. Viability Theory. Birkhäuser, Boston.

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

Martinez-Alier, J., Munda, G., O'Neill, J., 1998. Weak comparability of values as a foundation for ecological economics. Ecological Economics 26, 277–286.

Munda, G., Nardo, M., 2009. Noncompensatory/nonlinear composite indicators for ranking countries: a defensible setting. Applied Economics 41, 1513–1523.

Neumayer, E., 2013. Weak versus Strong Sustainability: Exploring the Limits of Two Opposing Paradigms, 4th ed. Edward Elgar, Cheltenham.

Øksendal, B., 2003. Stochastic Differential Equations: An Introduction with Applications, 6th ed. Springer, Berlin.

Redner, S., 2001. A Guide to First-Passage Processes. Cambridge University Press, Cambridge.

Ricard, D., Minto, C., Jensen, O.P., Baum, J.K., 2012. Examining the knowledge base and status of commercially exploited marine species with the RAM Legacy Stock Assessment Database. Fish and Fisheries 13, 380–398.

Tapley, B.D., Bettadpur, S., Ries, J.C., Thompson, P.F., Watkins, M.M., 2004. GRACE measurements of mass variability in the Earth system. Science 305, 503–505.

Tilton, J.E., 2003. On Borrowed Time? Assessing the Threat of Mineral Depletion. Resources for the Future, Washington, DC.

Tilton, J.E., Lagos, G., 2007. Assessing the long-run availability of copper. Resources Policy 32, 19–23.

U.S. Geological Survey, 2026. Mineral Commodity Summaries 2026: Phosphate Rock. USGS, Reston, VA. https://www.usgs.gov/centers/national-minerals-information-center/mineral-commodity-summaries

---

**Supplementary material** accompanies this article: the ten-state admissibility template with its audited negative witnesses, the registered identification ladders of the phosphorus and groundwater templates at full detail, the split-assignment ($\psi$) mechanism table, and the statement inventory.

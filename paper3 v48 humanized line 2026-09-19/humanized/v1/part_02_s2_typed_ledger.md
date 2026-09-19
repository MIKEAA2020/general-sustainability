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

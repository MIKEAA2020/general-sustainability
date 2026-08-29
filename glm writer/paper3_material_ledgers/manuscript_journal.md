% TITLE: Conserved Material Ledgers and Componentwise Depletion Diagnostics: Typed Stock–Flow Accounting, the Closed Finite-Donor Ledger, and Depletion-Horizon Semantics
% VENUE: Ecological Modelling
% TYPE: Methods / formal-framework article
% RUNNING: Material ledgers and depletion diagnostics
% KEYWORDS: material flow analysis; conservation laws; depletion diagnostics; viability; stock-flow accounting; first-passage
% CONTRIBUTION: The paper develops a typed conservation-ledger representation for renewable-resource systems with proved mass identities, depletion diagnostics, and first-passage surrogates, applied to three contrasting resource systems.

# Abstract

Resource accounting that condenses heterogeneous material stocks into a single index lets compensation hide: a severe deficit in one stock can coexist with a positive aggregate, and quantities carrying the units of time — reserve-life ratios, trend-persistence indices, removals-only pressure scales — circulate as if they answered a single question. This paper develops a typed conservation-ledger representation for renewable-resource systems that blocks both failures by construction. Compartments carry a moiety, a boundary, and a unit; non-negative primitive fluxes connect them through a signed incidence matrix; conversions appear only as explicit stoichiometric coefficients; and every one-way transfer is donor-limited — so conservation and nonnegativity are proved rather than assumed. For the closed finite-donor ledger — living stock $N$, active abiotic pool $A^{\mathrm{act}}$, geological donor $A^{\mathrm{geo}}$, and detritus $U$ — the paper proves the mass identity $\frac{d}{dt}(N+A^{\mathrm{act}}+A^{\mathrm{geo}}+U)=-qEN$, forward invariance of the nonnegative orthant, the absence of interior rest points at positive effort, the extinction–geochemical rest set, and integrability of extraction against the finite donor budget. Depletion time is separated into three non-interchangeable quantities — gross turnover intensity, a frozen-rate ratio, and a scenario-conditioned hitting time — and three application records are classified at exactly their evidentiary status: a satellite groundwater anomaly-persistence index, the phosphate reserve-life ratio ($\approx309$ years), and a fisheries removals-only pressure time outside the hierarchy. Two proved first-passage theorems on declared stochastic surrogates (inverse-Gaussian groundwater passage; geometric-Brownian fisheries passage) carry seven explicit non-claims, and a five-reason boundary separates the closed ledger from the delayed working core.

# 1. Introduction

## 1.1 The question this paper answers

**How should material stocks, services, products, waste, active and geological pools, and depletion diagnostics be represented so that conservation and nonnegativity are proved rather than assumed, compensation cannot hide in an aggregate, and every depletion number states exactly which question it answers?**

Sustainability accounting fails in two characteristic ways. The first is *compensatory aggregation*: heterogeneous physical stocks and service flows are summarized by a scalar index whose cross-component trades are never declared as mathematics, so a single severe deficit can coexist with a positive aggregate — the composite-indicator and weak-versus-strong-sustainability literatures document the failure and its noncompensatory remedies (Munda and Nardo 2009; Neumayer 2013; Ekins et al. 2003). The second is *classification drift*: quantities with the units of time — reserve-life ratios, trend-persistence indices, removals-only pressure scales — circulate as if they were one thing ("time to depletion"), when they answer different questions under different assumptions. This paper builds the accounting layer that resists both failures. Its objects are typed ledgers in which conservation follows from the incidence structure, positivity follows from donor limitation, services are readouts rather than conserved mass, and each depletion quantity carries its own classification.

The gap this paper fills is on the dynamic side of the accounting tradition. Material flow analysis supplies the compartment–flux bookkeeping on which any physical account of a resource system rests (Brunner and Rechberger 2004; Eurostat 2001; Fischer-Kowalski et al. 2011), and reaction network theory supplies the incidence formalism (Feinberg 2019); what neither supplies for renewable-resource systems is a representation in which conservation, positivity, rest-point structure, and depletion semantics are theorems about the system's vector field rather than conventions of the accounting scheme. Closing that gap — for ecological and resource modellers who need account structures whose mass identities hold exactly, whose diagnostics declare their scope, and whose application records state their evidentiary level — is the purpose of what follows.

## 1.2 What enters this paper

This article is the accounting and diagnostics paper of a series of companion studies under separate review. Its retained set consists of the 52 statement-inventory rows routed to it by this research programme's destination pass: the closed finite-donor ledger and its theorem set (A019); the componentwise accounting scaffold, its conservation and invariance theorems, and its depletion taxonomy with the three application records (A013); the first-passage surrogate theorems and their boundary disciplines (A024); the ledger rows of the unified applied source (A018 — the full-ledger conservation theorem, the nonnegative-orthant theorem, the deficit identity, the exact triangular projection, and the applied depletion-horizon tables); the domain templates of the phosphorus and groundwater sources at registered status (A004, A005); the relevant general results of the typed theory (A001, A002, A006, A010); the two ledger-side identities of the registered delay family (A012); and one mechanism-typing row (A003). The sources of the retained set are A001 (1 row), A002 (5), A003 (1), A004 (3), A005 (5), A006 (1), A010 (3), A012 (2), A013 (11), A018 (5), A019 (8), and A024 (7). Per-statement provenance keys link every inventory-sourced statement to the 409-row statement inventory (source location, canonical module, mapping type, evidence status, destination); the complete statement-level inventory is Appendix A.

## 1.3 Claim-status discipline

Every statement below carries a status label from the research programme's hierarchy (the A002 source's own table, adopted programme-wide):

| Status | Admission rule |
|---|---|
| Axiom/definition | Declares an object, domain, type, or convention; asserts no empirical truth |
| Identity | Follows by construction or direct algebra |
| Theorem | Complete proof under explicit mathematical assumptions |
| Conditional theorem | Complete implication whose hypotheses are not established for every intended application |
| Conjecture | Precise unproved statement with a declared proof gap and disproof route |
| Counterexample/limit | An explicit construction establishing that an implication fails |

Application records additionally carry their source-specific evidentiary level (defined source object; values accepted at attested source status with a submission-stage supplement pending; source-specific empirical status check required), stated per record. Two rules govern this article. **No promotion:** a conditional theorem is never stated as a theorem; an arithmetic ratio is never stated as a forecast; conditionality and classification are part of the mathematical content. **No silent transfer:** a status proven for one model class does not transfer to extensions, reductions, or applications without a declared map, and no diagnostic transfers across modules without the interface contract recorded per row.

## 1.4 Provenance and auditability

All 52 of this paper's inventory rows are closed at content level: each was verified against its source in a dated scientific pass over a full source read (A001 and A002 on 2026-08-27; A003, A004, A005, A006, A010, A012, A013, A018, A019, and A024 on 2026-08-28), each pass confirming per statement its existence, kind, proof presence, module, and mapping type, and each is stated below at exactly its source-declared status, with no promotion. Content-level acceptance means the statement's existence, kind, proof presence, module, and mapping type were verified against the source; it is not a theorem-status promotion, and the cross-module interface contract remains an open obligation recorded per row. Of the 409-row statement inventory, 354 rows have completed this dated verification; the 27 rows that remain open are exactly the three conditional-paper sources (A021, A022, A023) — none of them behind this paper.

## 1.5 Relationship to the companion papers

This paper is one of five companion papers under separate review. The architecture companion owns the typed canonical architecture (the type system, the diagnostic types and their no-transfer rule, the model-map taxonomy); this paper carries a Minimal Working Realization of the ledger objects it needs and never transfers a status across modules. The theorem-atlas companion owns the proof corpus, including the canonical conservation and invariance family whose ledger-side readings are stated here — where a full proof lives in the atlas, it is cited there, not reproduced beyond what local use requires. The delay-dynamics companion owns the named open/frozen-donor retarded systems and their bifurcation results; the boundary between that study and this one is fixed by the ledger-to-dynamics interface contract, stated in §8, whose exact shared object is the single-resource deficit identity. The sampled-governance companion owns the sampled-governance family, the empirical identification programme, and the worked fisheries case. A monograph reintegrates the material at full length after the papers receive external scrutiny; the research programme's four scored empirical manuscripts are outside this paper's scope. No companion paper depends on another for a locally load-bearing definition: the ledger equations, closures, and diagnostics used here are stated in full.

**Roadmap.** The remainder of this article is organized as follows. §2 states the primitive typed ledger: the incidence discipline, the closed natural block with its donor-limited primitives, the six-compartment and four-stock illustrations, mechanism typing, and the support-saturated logistic limits. §3 proves the closed-ledger theorem set — the canonical conservation family, the conditional hybrid moiety balance, the natural-block mass identity, orthant invariance, the absence of interior rest at positive effort, the extinction–geochemical rest set, extraction integrability, and the six-state cancellation with its audit witnesses. §4 adds services as typed readouts and derives the componentwise deficit with its exact specialization identity $qEN-R=-\dot N$. §5 develops the three-quantity depletion taxonomy, the local threshold-horizon bracket, and the application classifications (groundwater anomaly-persistence indices, the applied depletion-horizon tables, the phosphate reserve-life ratio, and the fisheries removals-only pressure time). §6 supplies first-passage semantics: the observed-drift Brownian surrogate, the inverse-Gaussian and geometric-Brownian theorems, the record-relative-barrier discipline, the constant-production phosphate passage time, and the seven explicit non-claims. §7 registers the phosphorus and groundwater domain templates, the two-pool identification requirements, and the extractor-side harvest-economics remark. §8 fixes the interface contract with the delay-dynamics companion — the exact shared object, the hand-off projection, the non-reduction boundary with its five reasons, and the model-version identifiers. §9 states what the ledger does not support, and §10 records provenance, reproducibility, and limits. Appendix A carries the complete statement inventory; the References and the data-availability statement close the article.

# 2. The primitive typed ledger (Minimal Working Realization)

## 2.1 Typed stocks, primitive fluxes, and the incidence discipline

A ledger state $z\in\mathbb R^m_+$ collects compartments, each entry carrying a material identity, spatial support, and physical unit. Internal dynamics use non-negative primitive fluxes:

$$
\dot x=S_{\mathcal T}v(x,y,\theta)+B_{\mathcal T}u_{\partial}(t)+d_x(t),\qquad v\ge0,
$$

where $S_{\mathcal T}$ is the typed stoichiometric (incidence) operator (the compartment–flux bookkeeping of material flow analysis, Brunner and Rechberger 2004; Eurostat 2001; Fischer-Kowalski et al. 2011, on the incidence formalism of reaction network theory, Feinberg 2019), $B_{\mathcal T}u_{\partial}$ contains declared boundary transfers, and $d_x$ belongs to a stated disturbance class. Entries are added within a row only when their types and units agree; a conversion between types is represented by an explicit stoichiometric coefficient, never by an implicit sum. If $L^{\top}S_{\mathcal T}=0$, then

$$
\frac{d}{dt}(L^{\top}x)=L^{\top}B_{\mathcal T}u_{\partial}+L^{\top}d_x:
$$

one conservation law per conserved moiety and boundary. The identity does not create a scalar sustainability mass across incommensurable systems. Two clarifications are part of the statement: $d_x$ must itself be typed (a physical disturbance on represented material is a different object from a structural discrepancy term), and $S_{\mathcal T}$ may contain signed entries even though $v\ge0$ — the sign pattern of the incidence and the nonnegativity of the primitives are separate declarations. Forward invariance is a separate requirement: every primitive outflow must vanish or be limited when its donor compartment is empty, and a target-relaxation flux from a finite donor is admissible only after donor limitation is made explicit. This typed-flux identity is the ledger-side form of the canonical typed hybrid conservation theorem (§3.1); the theorem-atlas companion carries the general statement, and this identity is its incidence-level form.

## 2.2 The closed natural block and its donor-limited primitives

The closed ledger of this paper is the finite-donor primitive system. Let

$$
x_L=(N,A^{\mathrm{act}},A^{\mathrm{geo}},U),
\qquad
s=\frac{A^{\mathrm{act}}}{A^{\mathrm{act}}+A_0},
\qquad
\sigma=\frac{A^{\mathrm{geo}}}{A^{\mathrm{geo}}+A_{g0}},
$$

with $N$ the living stock, $A^{\mathrm{act}}$ the active abiotic pool, $A^{\mathrm{geo}}$ the geological donor, and $U$ the detritus compartment. Net regeneration and gross uptake are the constitutive laws

$$
R(N,A^{\mathrm{act}})=rN\bigl(1-\frac{N}{K}\bigr)s,
\qquad
T=\kappa_A Ns,
\qquad
B=R+T,
$$

and the four primitives involving the donor are

$$
e_{GA}=\omega_A\bigl[A^{\mathrm{eq,intrinsic}}\bigr]_+\sigma,
\qquad
e_{AG}=\omega_A A^{\mathrm{act}},
\qquad
C^{A,\mathrm{lim}}=C^A\sigma,
\qquad
\gamma_UU\ \text{(detritus return)}.
$$

No derived target appears: recharge is donor-limited and cannot run backward ($e_{GA}=0$ at $A^{\mathrm{geo}}=0$ and at a nonpositive intrinsic target), and mining $C^{A,\mathrm{lim}}$ is donor-limited the same way extraction is. With $A_{g0}>0$ the donor fraction $\sigma$ is smooth and strictly increasing in the donor level. Under the registered institutional-failure specialization ($\mu=\nu=\rho=0$, $C^A=0$) the closed natural block is

$$
\begin{aligned}
\dot N&=R-qEN,\\
\dot A^{\mathrm{act}}&=-B+e_{GA}-e_{AG}+\gamma_UU,\\
\dot A^{\mathrm{geo}}&=-e_{GA}+e_{AG},\\
\dot U&=T-\gamma_UU,
\end{aligned}
$$

together with the memory–effort pair $(Z,E)$ driven by $qEN-R$ (never by mining). The registered parameterization is $r=0.02$, $K=100$, $q=0.001$, $\kappa_A=0.05$, $\omega_A=10^{-3}$, $A_0=1$, $A^{\mathrm{eq,intrinsic}}=50$, $\gamma_U=0.2$; the geological half-saturation $A_{g0}$ is declared positive (smoothness of the donor fraction $\sigma$) under the separation-of-scale condition $A^{\mathrm{geo}}\gg A_{g0}$, in which regime $\sigma\approx1$ and the working-core quantities are computed — the source registers the scale separation rather than a numerical value, so none is asserted here, and the $A_{g0}=0$ corner of Theorem 3.12 is the discontinuous-perturbation limit, not the registered regime. When product, waste, and the inert sink are restored with the same donor-limited routing, the full ledger $N+A^{\mathrm{act}}+A^{\mathrm{geo}}+U+P+W+I$ is closed (§3.4). The primitive laws are exact typed-flux objects of the closed ledger; the approximation content of the frozen-donor specialization is stated at its own scope in §8.

## 2.3 The six-compartment illustration

For one conserved limiting material, the accounting scaffold is instantiated by six compartments — living biomass $X$, detritus or recoverable residual $U$, active abiotic pool $A$, geological or slowly available pool $G$, product or in-use stock $P$, and absorbing or currently unavailable stock $W$ — with eight non-negative primitive fluxes: assimilation $g(X,A)$, mortality $m(X)$, harvest $h(X,E)$, decomposition $d_U(U)$, geological-to-active transfer $e_{GA}(G,A)$, active-to-geological transfer $e_{AG}(A,G)$, direct mining $c_G(G,E_G)$, and product retirement $r_P(P)$. With harvest fraction $\alpha\in[0,1]$ routed to $U$ and retirement fraction $\rho\in[0,1]$ returning to $U$ rather than $W$,

$$
\dot z=S(\alpha,\rho)\,v(z,u),
\qquad
z=(X,U,A,G,P,W)^{\top},
\qquad
v=(g,m,h,d_U,e_{GA},e_{AG},c_G,r_P)^{\top},
$$

where

$$
S(\alpha,\rho)=
\begin{pmatrix}
 1&-1&-1& 0& 0& 0& 0& 0\\
 0& 1&\alpha&-1& 0& 0& 0&\rho\\
-1& 0& 0& 1& 1&-1& 0& 0\\
 0& 0& 0& 0&-1& 1&-1& 0\\
 0& 0&1-\alpha&0&0&0&1&-1\\
 0& 0& 0& 0& 0& 0& 0&1-\rho
\end{pmatrix},
\qquad
\mathbf 1^{\top}S=0 .
$$

The zero column sums are the incidence statement of mass conservation (proved for the full system in §3.5). The matrix makes the routing choices visible, and the constitutive choices are features of this example, not properties of every typed ledger: the constant splits $\alpha$ and $\rho$, the compartment set, and the absorbing-sink convention are declared choices; the construction is a monomaterial projection, not a universal ecological mechanism; and coupled multi-element accounts require additional typed rows and a conservation matrix. If an application makes recovery claims, $U$ and $P$ must be split by material, location, and quality grade, with declared yields, residual routes, and exergy or capacity inputs — the conservation argument then applies to the expanded typed incidence system, not automatically to an undifferentiated quality-neutral loop.

## 2.4 The four-stock resource–sink–nutrient–product system

A second exact specialization closes a resource–sink system with a nutrient stock $N$ and product stock $P$: state $(S,K,N,P)\in\mathbb R^4_+$ with — in the source's notation, local to this block: here $K$ is the sink stock and $N$ the nutrient stock, and the carrying capacity $K$ of §2.2 and the living stock $N$ do not enter —

$$
\dot S=g(S,N)-H,\quad
\dot K=\theta_KH-\theta_\delta K,\quad
\dot N=-g(S,N)+\theta_\delta K+I_N,\quad
\dot P=(1-\theta_K)H-Q_P,
$$

where $\theta_K$ is the sink-generation fraction, $\theta_\delta$ the assimilation rate, $I_N$ external nutrient input, and $Q_P$ product disposal. Adding the four equations gives the mass balance

$$
\frac{d}{dt}(S+K+N+P)=I_N-Q_P,
$$

so total mass is conserved exactly when both boundary transfers vanish. The proposition is an exact specialization of the incidence discipline of §2.1: every internal transfer cancels in the column sum, and the boundary terms survive as the ledger's declared inputs and outputs.

**Sink obstructions independent of the stock (remark: construction and corollary).** The mass balance has a sink-side physical reading with two empty-kernel mechanisms that operate whatever the resource stock does. With sink loading $w(H)$, assimilation $\delta(K)$, and a harvest floor $H\ge H_{\min}>0$ (in the four-stock specialization $w(H)=\theta_KH$ and $\delta(K)=\theta_\delta K$): under *no assimilation* ($\delta\equiv0$), $\dot K\ge w(H_{\min})>0$ and the sink exceeds any finite ceiling $K_{\max}$ in finite time; under *weak assimilation* ($\delta(K_{\max})<w(H_{\min})$), the sink load at the ceiling is still positive — $\dot K=w(H_{\min})-\delta(K_{\max})>0$ at $K=K_{\max}$ — so $K$ exits above $K_{\max}$ in finite time, the explicit negation of the ceiling condition $K^\dagger\le K_{\max}$ with $\delta(K^\dagger)=w(H_{\min})$. In both cases the viability kernel (Aubin 1991) of the constraint set $\{S\ge S_{\min},\ 0\le K\le K_{\max}\}$ — the states from which some admissible harvest keeps both constraints for all time — is empty (A001, Remark 6.1). The corollary for closed ledgers is the same mechanism in ledger language: in a closed ledger without recycling, where $w(H)$ enters the sink irreversibly and $\delta=0$, any positive output floor forces an empty viability kernel — positive throughput accumulates in the sink forever.

## 2.5 Mechanism typing: routing is never determined by diagnostic labels

Extraction has at least three distinct physical meanings — standing-stock culling (present extraction removes reproductive stock directly), recruitment suppression (present use prevents future recruits without immediate adult removal), and weak viability coupling (use has limited or indirect effect on reproduction). In the ledger, standing-stock culling enters as an outflow from the standing-stock compartment; the typing is the physical module's, not the diagnostic's: a diagnostic label such as "unsustainable portion" never determines physical destination. Material routing is determined by the typed physical module alone, and the diagnostic threshold that flags a flow has no standing in the incidence matrix. This discipline governs §§4–6: diagnostics read the ledger; they do not rewrite it.

**$\psi$-assignment and the evidence requirement (illustrative calibrated examples).** Where an application splits extraction between standing-stock removal and recruitment suppression — $C_\mathrm{stock}=\psi qEN$ and $C_\mathrm{recruit}=(1-\psi)qEN$ for $\psi\in[0,1]$ — the assignment requires evidence per channel: the dominant physical mechanism sets it, never a diagnostic label. Illustrative calibrated assignments, stated at the source's illustrative status (the assignments treat the named domains through the logistic two-channel proxy): soil zinc under crop export at $\psi=0.85$, an existing-unit removal, against impaired mineralisation at $\psi=0.25$, replenishment degradation; pollinators under adult mortality at $\psi=0.70$ against brood failure at $\psi=0.20$ — and across such mechanism pairs the trough depth varies by a factor of about $1.5$ from mechanism alone (A018, §5 $\psi$-mechanism table). The mass-routing discipline is this section's typing made explicit: literally harvesting pre-recruit stages is a harvest of existing units and routes to the product and waste fractions; habitat-induced failed recruitment is a prevented inflow — routing it into product or waste would create mass that was never in the stock; and damage to the capital stock itself (aquifer compaction, severe soil loss) is not a $\psi$ channel at all, but a slow drift in capacity or a transfer to the inert sink.

## 2.6 Support saturation and the logistic limit

Two registered results control what the ledger's stock equation becomes when its support pool saturates; both are singular reductions with explicit scope, and neither is a full-core reduction.

**Theorem 2.1 (Support-saturated logistic stock limit).** Fix $T<\infty$ and non-negative parameters $\mu,\delta,c,q$. For $\kappa>0$, assume $A_\kappa$ is measurable with $A_\kappa(t)\ge a_0>0$, $0\le X_\kappa(t)\le X_{\max}$, and common effort $E\in L^\infty([0,T])$. Let $X_\kappa$ solve $\dot X_\kappa=\mu X_\kappa A_\kappa/(\kappa+A_\kappa)-\delta X_\kappa-cX_\kappa^2-qE(t)X_\kappa$ and $X_0$ solve the limiting equation with the same initial value. Then the vector-field defect obeys $|\mu X_\kappa A_\kappa/(\kappa+A_\kappa)-\mu X_\kappa|\le\mu X_{\max}\kappa/a_0$ and $\sup_{t\le T}|X_\kappa(t)-X_0(t)|=O(\kappa)$ by Grönwall's inequality; if $\mu>\delta$ and $c>0$ the limit has the logistic form $\dot X_0=rX_0(1-X_0/K_{\log})-qE(t)X_0$ with $r=\mu-\delta$, $K_{\log}=(\mu-\delta)/c$.

**Theorem 2.2 (Registered-family support-saturated identity).** In the registered primitive-flux core with $g(X,A)=\mu XA/(K_A+A)$, $m(X)=dX+cX^2$, $h(X,E)=qEX$, the support-saturated stock equation is, for each fixed interior $A>0$ in the limit $K_A\to0$,

$$
\dot X=(\mu-d)X-cX^2-qEX=rX\bigl(1-\frac{X}{K}\bigr)-qEX,
\qquad r=\mu-d,\quad K=\frac{\mu-d}{c},
$$

requiring $\mu>d$ and $c>0$. The identity is pointwise on the interior support region and not uniform through the depleted-pool boundary: for every $K_A>0$, $A/(K_A+A)=0$ at $A=0$, so support saturation does not justify replacing the factor by one on or uniformly near the boundary. Its scope is restricted: it does not eliminate the detritus compartment $U$, make $A$ constant near its boundary, or transform the memory or effort laws — an ecological stock-equation identity, not a full-core reduction and not a transfer principle for Hopf or fold thresholds.

The active-material admissibility obligation of the registered core — invariance of $X+U\le\mathcal M$ — is discharged by its companion boundary theorem: on the face $X+U=\mathcal M$ the active pool is $A=0$ and $g(X,0)=0$, so $\frac{d}{dt}(X+U)=-qEX-\gamma_UU\le0$, and together with $g(0,A)=0$, $m(0)=0$, and the donor-limited flux assumptions this proves forward invariance of the simplex $\{X\ge0,\ U\ge0,\ X+U\le\mathcal M\}$ for the ecological subsystem under admissible effort. The registered model family and its effort laws belong to the delay-dynamics companion paper; the two results above are its ledger-side content.

# 3. Conservation and positivity: the closed-ledger theorem set

## 3.1 The canonical conservation family

Three canonical results govern every ledger in this paper; the theorem-atlas companion states and proves them in full, and they are recorded here at their ledger-side reading.

**Theorem 3.1 (Typed hybrid conservation).** Let $L\in\mathbb R^{m\times k}$ collect $k$ moiety-accounting vectors. Along every locally finite hybrid execution satisfying $L^{\top}S=0$ and $L^{\top}S^J=0$,

$$
L^{\top}x(t)-L^{\top}x(0)=\int_0^tL^{\top}B\varphi(s)\,ds+\sum_{t_j\le t}L^{\top}B^J\beta_j ,
$$

and if all boundary rates and impulses vanish, each component of $L^{\top}x$ is constant. *Proof (verified present; summary):* on every flow segment the null-space condition removes the internal flux contribution; at each jump the reset contributes $L^{\top}B^J\beta_j$; the segments telescope. $\blacksquare$ (Full proof: the theorem-atlas companion, Thm 4.1.) The balance requires local finiteness of the execution; it gives one balance per declared moiety and does not authorize adding biomass, money, biodiversity indices, and exergy into one conserved scalar.

**Corollary 3.2 (Closed positive-moiety bound).** For a closed physical network with zero boundary transfer and a strictly positive conservation vector $\ell\in\mathbb R^m_{++}$ satisfying $\ell^{\top}S=\ell^{\top}S^J=0$ in every active mode, every non-negative trajectory obeys $0\le x_i(t)\le\ell^{\top}x(0)/\ell_i$. This is the ledger's stock-boundedness mechanism: a closed moiety with positive weights bounds every compartment by the conserved total.

**Corollary 3.3 (Donor limitation is sufficient).** Under the regularity and reset assumptions of the atlas's nonnegative-invariance theorem (Thm 4.3 of the companion atlas), if every primitive outflow from compartment $i$ vanishes when $x_i=0$, all internal inflows are non-negative, and every negative boundary flow is donor-limited, then the tangency condition holds and the nonnegative cone is forward invariant. The corollary is an exact sufficiency result; the separate-obligation discipline is the point: algebraic cancellation alone does not establish invariance, and invariance does not establish completeness.

## 3.2 The conditional hybrid moiety balance

**Conditional Theorem 3.4 (Hybrid moiety balance).** Let $r$ be absolutely continuous between locally finite event times with left and right limits at events, satisfying $\dot r=\mathsf S\nu+b$ with $\nu\ge0$, separate reverse columns, and donor-limited negative boundary flows. If $\mathsf L^{\top}\mathsf S=0$, then

$$
\mathsf L^{\top}r(t)-\mathsf L^{\top}r(0)=\int_0^t\mathsf L^{\top}b\,ds+\sum_{t_k\le t}\mathsf L^{\top}\bigl[r(t_k^+)-r(t_k^-)\bigr].
$$

*Proof (verified present; summary):* integrate the continuous balance between consecutive events and telescope the left/right state differences. $\blacksquare$ The theorem is conditional, and its jump interpretation is part of the content: an internal-transformation jump requires $L^{\top}(r^+-r^-)=0$ or a jump incidence factorization with left-kernel conservation; a boundary-crossing jump is a boundary impulse and belongs in the boundary term. Two obligations ride the theorem. First, the *yield-routing obligation*: if a transformation is represented with a yield below one for a declared moiety, the omitted fraction must be routed to another represented compartment or a declared boundary flow — otherwise the claimed moiety balance holds only after silently dropping that moiety from $\mathsf L$. Second, the relation to Theorem 3.1: this is the conditional variant of the typed hybrid conservation theorem, retained at its own status; the canonical form is the A002 statement, and both are stated here without merging their statuses.

## 3.3 Stoichiometric conservation of the full ledger

**Theorem 3.5 (Stoichiometric conservation).** Let $X=(N,P,W,I,U,A^{\mathrm{act}},A^{\mathrm{geo}})$ be the mass compartments of one resource system and $\mathcal I$ the incidence matrix of its flux ledger. One-way transfers are non-negative and donor-limited; net regeneration is the difference of two such primitives and is signed when $N>K$. Under the unit-sum routing constraints and $0\le\alpha\le1$,

$$
\dot X=\mathcal IF(X),\qquad \frac{d}{dt}\mathbf 1^{\top}X=0 .
$$

*Proof (verified present; summary):* every primitive is a transfer between two compartments, or a pair of opposite primitives implementing a two-way exchange; the corresponding column of $\mathcal I$ has entries $+1$ and $-1$ in the receiving and donating rows and zeros elsewhere. Routing tensors are row-stochastic by construction, so each unit of a split flux sums to one across destinations; hence $\mathbf 1^{\top}\mathcal I=0$ and $\mathbf 1^{\top}\dot X=\mathbf 1^{\top}\mathcal IF=0$. $\blacksquare$ The theorem is an exact conservation identity under the routing constraints; the approximation content of the reduced cores — the open projection whose frozen-donor mass error is the recorded integral of the omitted donor and turnover flows — belongs to the working and quasi-steady closures owned by the delay-dynamics companion paper and is separated from this theorem by that boundary.

## 3.4 The natural-block mass identity

**Theorem 3.6 (Natural-block mass identity).** Along every absolutely continuous solution of the closed natural block of §2.2,

$$
\frac{d}{dt}\bigl(N+A^{\mathrm{act}}+A^{\mathrm{geo}}+U\bigr)=-qEN .
$$

If product, waste, and the inert sink are restored with the same donor-limited routing, the full ledger $N+A^{\mathrm{act}}+A^{\mathrm{geo}}+U+P+W+I$ is constant.

*Proof.* Adding the four equations gives

$$
\dot N+\dot A^{\mathrm{act}}+\dot A^{\mathrm{geo}}+\dot U
=(R-qEN)+(-B+e_{GA}-e_{AG}+\gamma_UU)+(-e_{GA}+e_{AG})+(T-\gamma_UU).
$$

Since $B=R+T$, one has $R-B+T=0$; the pairs $\pm e_{GA}$, $\pm e_{AG}$, and $\pm\gamma_UU$ cancel; the remainder is $-qEN$. With the donor-limited product/waste/inert routing restored, each extracted unit appears in $P$ or $W$ and each recovery from $W$ returns to $A^{\mathrm{act}}$, so the seven-compartment sum is constant. $\blacksquare$

The reading is exact: the closed natural block loses mass at precisely the extraction rate — plus the donor-limited mining rate when optional mining is restored, which the registered institutional-failure specialization sets to zero ($C^A=0$) — and nothing else. Conservation is a property of the routing, not of the constitutive laws' magnitudes.

## 3.5 Conservation of the six-compartment ledger

**Theorem 3.7 (Mass conservation).** For the six-compartment system of §2.3, the total tracked material $M=X+U+A+G+P+W$ is constant along every classical solution.

*Proof.* Differentiate $M$ and substitute: the assimilation terms give $g-g=0$; mortality gives $-m+m=0$; decomposition gives $-d_U+d_U=0$; geological exchange gives $e_{GA}-e_{GA}=0$ and $-e_{AG}+e_{AG}=0$; mining gives $-c_G+c_G=0$; and the remaining harvest and retirement terms satisfy $-h+\alpha h+(1-\alpha)h=0$ and $\rho r_P-r_P+(1-\rho)r_P=0$. Hence $\dot M(t)=0$ wherever the classical solution is defined. $\blacksquare$

Two scope notes are part of the row. The conservation argument applies to the expanded typed incidence system when quality grades are split — not automatically to an undifferentiated quality-neutral loop. And open systems are explicit: imports, exports, atmospheric losses, and cross-boundary transport enter as typed boundary fluxes, giving $\dot M=I_{\partial}-O_{\partial}$; writing these flows explicitly is preferable to preserving a nominal invariant by allowing an unobserved or finite donor compartment to become negative.

## 3.6 Orthant invariance

**Theorem 3.8 (Orthant invariance of the closed ledger).** The nonnegative orthant in $(N,A^{\mathrm{act}},A^{\mathrm{geo}},U,Z,E)$ is forward invariant for the closed natural block.

*Proof.* The right-hand side is locally Lipschitz on a neighbourhood of the closed orthant (each Michaelis–Menten factor $s$, $\sigma$ is $C^\infty$ for non-negative arguments after the usual $C^1$ extension through the origin). On the face $A^{\mathrm{geo}}=0$ one has $\sigma=0$, hence $e_{GA}=0$ and $\dot A^{\mathrm{geo}}=e_{AG}=\omega_AA^{\mathrm{act}}\ge0$. On $A^{\mathrm{act}}=0$ one has $s=0$, so $R=B=T=e_{AG}=0$ and $\dot A^{\mathrm{act}}=e_{GA}+\gamma_UU\ge0$. On $N=0$, extraction and uptake vanish and $\dot N=0$. On $U=0$, $\dot U=T\ge0$. Nagumo's inward-pointing criterion yields forward invariance of the orthant. $\blacksquare$

**Theorem 3.9 (Forward invariance of the nonnegative cone).** Under the donor boundary assumptions of §2.3 (each primitive flux vanishes when its donor is empty, fluxes continuous in effort and locally Lipschitz in the state), $\mathbb R^6_+$ is forward invariant for the six-compartment system. *Proof (verified present; summary):* face by face — at $X=0$, $g=m=h=0$ so $\dot X=0$; at $U=0$, $\dot U=m+\alpha h+\rho r_P\ge0$; at $A=0$, $\dot A=d_U+e_{GA}\ge0$; at $G=0$, $\dot G=e_{AG}\ge0$; at $P=0$, $\dot P=(1-\alpha)h+c_G\ge0$; at $W=0$, $\dot W=(1-\rho)r_P\ge0$ — the vector field belongs to the tangent cone at every boundary point, and the tangent-cone invariance theorem applies. $\blacksquare$ Conservation and boundary admissibility are separate obligations (the source's own emphasis), and the finite-donor condition carries a discipline: a target-relaxation law $e_{GA}=\omega(A^{\mathrm{eq}}-A)$ does not satisfy it unless also limited by $G$; it may be used only with the source declared an effectively infinite external reservoir, in which case the system is open rather than closed.

**Theorem 3.10 (Forward invariance of the mass orthant).** On the specialized system of the unified applied source and on its five-, four-, and three-state cores, the set $\Omega=\{N,A^{\mathrm{act}},U,P,W,I,A^{\mathrm{geo}},Z\ge0,\ 0\le E\le E_{\max}\}$ is forward invariant; in particular $A^{\mathrm{geo}}$ cannot become negative. *Proof (verified present; summary):* the face-by-face Nagumo argument, with the clamp $[A^{\mathrm{eq}}]_+$ keeping $e_{GA}\ge0$ for transiently negative derived targets and the gated effort prefactor vanishing at $E=E_{\max}$. $\blacksquare$ The scope notes are part of the statement: the $E\le E_{\max}$ bound holds for the gated law and fails for the ungated comparison system, and the stoichiometric core's signed memory lies outside the $Z\ge0$ scope.

## 3.7 No interior rest at positive effort

**Theorem 3.11 (No interior rest at positive effort).** Suppose $E\equiv E_*>0$ is constant. A rest point of the closed natural block satisfies $R+C^{A,\mathrm{lim}}=0$ after restoring optional mining; with $C^A=0$ this is $R=0$, hence $N=0$ or $N=K$ or $A^{\mathrm{act}}=0$. None of these is compatible with $E_*>0$ and $N_*>0$: (i) $N=K$ and $E_*>0$ give $\dot N=-qE_*K<0$; (ii) $A^{\mathrm{act}}=0$ and $A^{\mathrm{geo}}>0$ give $\dot A^{\mathrm{act}}=\omega_AA^{\mathrm{eq,intrinsic}}\sigma>0$; (iii) $N=0$ forces $R=T=0$ and reduces to the extinction–geochemical rest of Theorem 3.12. In particular the companion working point $(N^*,A^{\mathrm{act}*})=(89.526,\,397.87)$ is not a rest point at $E=E^*\approx2.090$, since $R^*=qE^*N^*\approx0.187>0$.

*Proof.* At a rest point, $\dot U=0$ forces $\gamma_UU=T$. Adding $\dot A^{\mathrm{act}}+\dot A^{\mathrm{geo}}$ gives $-B+\gamma_UU=0$, hence $B=T$; since $B=R+T$, $R=0$. From the constitutive law, $R=rN(1-N/K)s=0$ implies $N=0$ or $N=K$ or $s=0$ (that is, $A^{\mathrm{act}}=0$). Cases (i)–(iii) exclude each branch; at the working point $R^*=qE^*N^*>0$ contradicts $R=0$. $\blacksquare$

## 3.8 The extinction–geochemical rest set

**Theorem 3.12 (Extinction–geochemical rest set).** The set $N=0$, $U=0$, $E$ arbitrary, $A^{\mathrm{act}}=A^{\mathrm{eq,intrinsic}}\sigma$ consists of rest points of the natural block. If $A_{g0}=0$ and $\sigma\equiv1$ for $A^{\mathrm{geo}}>0$, this is the ray $A^{\mathrm{act}}=A^{\mathrm{eq,intrinsic}}$, $A^{\mathrm{geo}}\ge0$. *Proof (verified present; summary):* with $N=U=0$ the remaining equations are $\dot A^{\mathrm{act}}=\omega_AA^{\mathrm{eq,intrinsic}}\sigma-\omega_AA^{\mathrm{act}}$ and its negative in $A^{\mathrm{geo}}$; both vanish iff $A^{\mathrm{act}}=A^{\mathrm{eq,intrinsic}}\sigma$. $\blacksquare$ The institutional memory yields $E\to E^*$ at $N=0$ with extraction vanishing identically — consistent with the rest set and not an interior rest. The scope statement is exact: the only rest points with vanishing extraction are extinction plus geochemical equilibrium.

## 3.9 Extraction integrability

**Theorem 3.13 (Integrable extraction).** Let $M=N+A^{\mathrm{act}}+A^{\mathrm{geo}}+U$. Then $M(t)=M(0)-\int_0^tqE(s)N(s)\,ds\ge0$, so

$$
\int_0^\infty qE(s)N(s)\,ds\le M(0)<\infty,
$$

in particular $qEN\in L^1(0,\infty)$. No trajectory maintains extraction at the companion working value $qE^*N^*\approx0.187$ for all time.

*Proof.* By Theorem 3.6, $M(t)=M(0)-\int_0^tqE(s)N(s)\,ds$; forward invariance (Theorem 3.8) gives $M(t)\ge0$, so the improper integral is at most $M(0)$. If $qEN\equiv qE^*N^*$ for all $t\ge0$, the integral would diverge. $\blacksquare$

This is the depletion-horizon semantics of the closed ledger in its strongest form: the donor budget is finite, extraction is integrable against it, and any constant extraction flux is eventually exhausted — the finite-budget fact that §8 turns into the non-reduction boundary with the working retarded core.

## 3.10 The six-state material cancellation and its limit

Summing the six material equations of a ten-state admissibility stress-test template gives the exact identity

$$
\frac{d}{dt}\bigl(\bar X_A+X_J+P+U+A+G\bigr)=0 .
$$

This is an algebraic cancellation only: it does not prove forward invariance of the six material states or physical admissibility of every term. The ghost-sink check is part of the row: the same birth-transfer rate $g_B$ enters $\dot X_J$ and $\dot A$ with opposite signs, so material not transferred to juveniles remains in $A$ — there is no unmatched sink in the six-state ledger. The identity is retained precisely for its discipline: formal cancellation coexists with boundary failure elsewhere in the same template (its geological exchange is not donor-limited), and the cancellation by itself establishes nothing about admissibility. Conservation (§§3.4–3.5) and positivity (§3.6) are proved separately in every well-posed ledger of this paper, exactly because cancellation is cheap and admissibility is not.

**The audit's remaining negative witnesses (negative witnesses, audited status).** The geological-exchange failure named above is one of three negative witnesses recorded by the same admissibility audit, and the other two complete the triad: the variance-unclosed witness — at $V_N=0$ the variance equation gives $\dot V_N=-2q\bar X_A\operatorname{Cov}(E,\bar X_A)$, which can be negative, the covariance is not a functional of the ten displayed states, and the variance dynamics are not guaranteed realizable by a non-negative spatial distribution, so the variance closure does not exist as stated — and the $Q$-undefined witness — the capital equation's output functional $Q$ has no displayed state equation or constitutive closure, the broader production function cannot silently supply the omission, and the ten equations therefore determine no unique autonomous DDE or characteristic quasi-polynomial (A010, admissibility stress test).

**Application prerequisites and calibration underidentification (registered application prerequisites).** Four prerequisites are registered for any application of the ten-state template: the geological exchange must be donor-limited, the variance equation must receive a realizable closure, the output functional $Q$ must be defined, and the information and governance operators must be declared. The calibration discipline rides them: calibration from spawning-stock biomass and fishing mortality alone would remain underidentified — juvenile abundance, recruitment, maturation, natural mortality, selectivity, active-pool measurements, spatial variance and covariance, capital/exergy, and governance timing are also required — so applications begin from a minimum module set and measured observables rather than fitting all ten states from two series (A010, §11).

# 4. Service readouts and the componentwise deficit

Services are observations or feasible outputs of the physical state, not additional conserved mass. The architecture's typing governs this layer throughout: a diagnostic claim has its own type and the no-transfer rule applies — a diagnostic is not a causal claim (the architecture companion paper, §2.4). Internal physical transfers are not services merely because they appear in a ledger: a typed readout identifies the delivered flow, its boundary, and any unit conversion.

## 4.1 The service readout and the contemporaneous balance

For services indexed by $i=1,\ldots,n$, write $s_i(t)=\mathcal O_i(x(t),u(t),\theta)$, where $u$ denotes admissible operating or extraction choices and $s_i$ and the demand $d_i$ share service-specific units. Where delivered services are selected or converted ledger fluxes, the readout is linear in the primitives,

$$
s=\mathcal O(z,u,\theta)=Q(\theta)\,v(z,u),
$$

with every row of $Q$ declaring the delivery boundary and the conversion into one service-specific unit; more general state-dependent readouts are possible. The contemporaneous component balance is

$$
b_i(t)=s_i(t)-d_i(t),
$$

and $b_i(t)\ge0$ means measured supply meets measured demand for component $i$ at that instant. It does not by itself imply that the underlying trajectory is sustainable: a stock can meet current demand while declining toward a threshold, and a stock below a desired level can have a positive current balance while recovering.

## 4.2 The state-dependent feasible balance domain

**Definition 4.1 (Feasible balance domain).** For an admissible operating set $\mathcal U(x,t)$ and a declared demand set $\mathcal D(t)$,

$$
\mathcal B(x,t)=\{\mathcal O(x,u,\theta)-d:\ u\in\mathcal U(x,t),\ d\in\mathcal D(t)\}.
$$

The geometry of the balance domain is state dependent and inherited partly from the stock–flow model; no unrestricted argument can replace an application-specific analysis of $\mathcal B(x,t)$. This domain is the object against which any scalar certificate claim must be checked (§9.1): a weighted sum certifies componentwise nonnegativity on $\mathcal B(x,t)$ only through an implication proved from the physical restrictions that define the domain.

## 4.3 Support provenance and the directional support gap

Current service adequacy and regenerative feasibility are different claims. Let $\Gamma_\mathrm{all}(x,t)\subseteq\mathbb R^n_+$ contain the service vectors feasible through all pathways admitted by an application, and $\Gamma_\mathrm{reg}(x,t)\subseteq\Gamma_\mathrm{all}(x,t)$ the feasible set after imposing the declared regenerative-flow, system-boundary, material-quality, and exergy or capacity restrictions. These correspondences are application inputs obtained from a typed pathway or technology model; the stock ledger alone does not construct them.

**Definition 4.2 (Directional regenerative-support fraction and gap).** Assume $0\in\Gamma_\mathrm{reg}(x,t)$ and choose a nonzero service direction $\bar s\ge0$. Define

$$
\alpha_\mathrm{reg}(\bar s;x,t)=\sup\{\alpha\in[0,1]:\ \alpha\bar s\in\Gamma_\mathrm{reg}(x,t)\}.
$$

The vector $(1-\alpha_\mathrm{reg})\bar s$ is the *directional support gap*, measured in the same service units as $\bar s$. A realized service $s\in\Gamma_\mathrm{all}\setminus\Gamma_\mathrm{reg}$ is support-dependent under that declaration even when $s\ge d$.

The inventory's own status line is part of the statement: attainment requires closedness — if $\Gamma_\mathrm{reg}$ is not closed the supremum may not be attained, and the gap is relative to a supremal fraction, not necessarily an achievable boundary service. The non-interpretation discipline is equally part of it: the statement neither subtracts raw material from service nor proves that a physical stock is declining; net depletion still requires a negative stock balance or a trajectory argument. The provenance partition behind $\Gamma_\mathrm{reg}$ (renewable flow, recovered or recycled material, imports, non-renewable drawdown) never adds unlike physical units.

## 4.4 The componentwise deficit and the specialization identity

On the unreduced ledger the physical deficit is the diagnostic

$$
\Delta^{\mathrm{phys}}(t)=C(t)-M^{\top}S(t),
$$

with $C$ the operative extraction law and $M$ the stock–service conversion. It does not drive the physical equations, and it is not equal to $-\dot N$ unless waste–product feedback vanishes and the service is identified with regeneration. The single-resource specialization ($S=R$, $\chi=1$, $\mu=\nu=\rho=0$, $C^A=0$) makes that identification, and on that class — and only on that class — the deficit collapses to the stock-decline rate:

**Lemma 4.3 (Exact specialization deficit identity).** On every trajectory of the specialized system, and of every reduced core whose stock equation is $\dot N=R(N,A)-qEN$,

$$
qEN-R(N,A)=-\dot N,
\qquad
\Lambda(t):=\bigl[qEN-R\bigr]_+=\bigl[-\dot N\bigr]_+ .
$$

*Proof.* Substitute the stock equation: $qEN-R=-(R-qEN)=-\dot N$. $\blacksquare$ The collapse is a property of the specialization, not a definition of liquidation on the unreduced ledger; the general diagnostic remains $C-M^{\top}S$.

**Identity 4.4 (Decline pressure).** In the registered delay family the depletion-pressure classification is $\Lambda(t)=\max\{0,\,qE(t)N(t)-S(N(t))\}=\max\{0,\,-\dot N(t)\}$: the memory input is a smoothed stock-decline rate, exactly the positive part of the decline. It is not a stock-level scarcity measure, not an unmet-consumption measure, and not an independently observed service deficit. Since $qEN-S(N)=O(N)$ as $N\to0$, the raw decline input vanishes near extinction while the positive baseline source of the effort law can still sustain commanded effort — the incremental decline amplification disappears, but the effort command need not; a controller intended to respond to low stock irrespective of its current rate of change requires a separately registered level-dependent channel. The memory and effort laws that consume $\Lambda$ are the delay-dynamics companion's named systems; the identity itself is ledger-side content and is the object the seam of §8 shares.

# 5. The depletion-diagnostics taxonomy

The ledger supplies the net active-pool derivative needed to distinguish gross throughput from net decline and from a model-conditioned threshold time. Let $A_{\min}$ be a declared threshold for the active abiotic pool with $A>A_{\min}$.

## 5.1 Gross turnover and dependency

**Definition 5.1 (Gross turnover intensity and support coverage).** With assimilation $g(X,A)>0$, define the gross turnover intensity $J_A^\mathrm{gross}=g(X,A)/A$ and the gross support-coverage ratio $H_A^\mathrm{gross}=(A-A_{\min})/g(X,A)$.

Neither is a time to depletion. The implication $g>0\Rightarrow\dot A<0$ is false in general: at an interior steady state, $g$ can be positive while decomposition and geological transfer balance it exactly, so that $\dot A=0$. Gross uptake measures throughput or dependency; net depletion is a balance property. This false-implication record is the first rung of the taxonomy and governs every application below.

## 5.2 The frozen-rate ratio

**Definition 5.2 (Local net-depletion ratio).**

$$
H_A^\mathrm{loc}(t)=\frac{A(t)-A_{\min}}{\bigl[-\dot A(t)\bigr]_+},
$$

with the extended-real convention $H_A^\mathrm{loc}=+\infty$ when $\dot A\ge0$ — correctly reporting no current net decline at a stationary or replenishing state.

The ratio is still not a trajectory forecast: it freezes the current net rate. If the fluxes change with $A$, policy, climate, prices, or other states, the realized threshold time can differ substantially. This is the middle rung of the taxonomy.

## 5.3 The scenario-conditioned hitting time

**Definition 5.3 (Scenario-conditioned hitting time).** For a fully specified dynamical model, policy or scenario $\pi$, disturbance history $d$, and initial state $x_0$,

$$
T_A(x_0;\pi,d)=\inf\{t\ge0:\ A^{\pi,d}(t;x_0)\le A_{\min}\},
$$

with $T_A=+\infty$ if the threshold is never reached. Under parameter, observation, and scenario uncertainty the appropriate output is a distribution or robust interval of $T_A$, not a single universal date.

The three quantities answer different questions and must not share one depletion-horizon label:

| Quantity | Question answered |
|---|---|
| $J_A^\mathrm{gross}$ or $H_A^\mathrm{gross}$ | How strongly does the system depend on, or turn over, the pool at the current gross rate? |
| $H_A^\mathrm{loc}$ | If the current net decline were frozen, what is the local stock-to-rate ratio? |
| $T_A$ | Under a stated model, policy, and disturbance scenario, when is the threshold first reached? |

## 5.4 The local threshold-horizon bound

**Theorem 5.4 (Local threshold-horizon bracket).** Let $A:[0,T]\to\mathbb R$ be absolutely continuous with $A(0)>A_{\min}$, let $v_0>0$ and $0<\varepsilon<1$, set $H_0=(A(0)-A_{\min})/v_0$, and suppose $T\ge H_0/(1-\varepsilon)$ and

$$
(1-\varepsilon)v_0\le-\dot A(t)\le(1+\varepsilon)v_0
$$

for almost every $t$ while $A$ stays above $A_{\min}$. Then a first crossing time $H$ exists no later than $H_0/(1-\varepsilon)$, and

$$
\frac{H_0}{1+\varepsilon}\le H\le\frac{H_0}{1-\varepsilon},
\qquad
|H-H_0|\le\frac{\varepsilon}{1-\varepsilon}H_0 .
$$

*Proof (verified present; summary):* if no crossing occurs before $t_*=H_0/(1-\varepsilon)$, absolute continuity gives $A(t_*)\le A(0)-(1-\varepsilon)v_0t_*=A_{\min}$, a contradiction; integrating both rate bounds over $[0,H]$ and using $A(0)-A(H)=v_0H_0$ yields the two-sided bracket. $\blacksquare$ The scope note is part of the row: this is a local diagnostic only — it fails when depletion reverses, the rate approaches zero, or feedback moves the trajectory outside the declared rate bounds. The theorem-atlas companion carries the canonical form of the same bracket (Conditional Theorem 10.1 there); this statement is its predecessor, recorded here with canonical credit and used locally to bracket the frozen-rate ratio's error under declared rate bounds.

## 5.5 Application classifications at their exact status

### 5.5.1 Groundwater anomaly-persistence indices (application record)

The G3P v1.12 product (Griebmeier et al. 2023; the GRACE line it descends from is Tapley et al. 2004) provides monthly groundwater-storage anomalies relative to a reference period rather than absolute aquifer volumes. For a basin-mean anomaly series over the reported April 2002–September 2023 window, the Linear-Trend Anomaly Persistence Index is

$$
L_\mathrm{hist}^\mathrm{anom}=\frac{a_\mathrm{latest}-a_\mathrm{hist,min}}{\bigl[-\widehat{\dot a}\bigr]_+},
$$

the fitted distance to the series' own historical minimum divided by the fitted decline rate. The four-basin record: Indo-Gangetic $-49.7$ cm/yr with index $\approx2.7$ yr; North China Plain $-18.6$ with $\approx7.9$; Central Valley $-16.1$ with $\approx9.5$; La Mancha $-3.2$ with $\approx21.4$. Classification, stated at the source's own status: a statistical anomaly index with units of time — not the physical stock ratio $H_A^\mathrm{loc}$ and not a forecast of aquifer exhaustion. Its value depends on the product window, basin mask, anomaly reference, and linear-trend convention; a physical $H_A^\mathrm{loc}$ requires an absolute stock estimate and a net stock derivative (aquifer geometry or saturated thickness together with storage parameters), not an anomaly series alone. The values are accepted at attested source status; the submission-stage supplement (processing files, source extracts, shared references) is pending.

### 5.5.2 The applied depletion-horizon tables (application record)

The unified applied source reports component-resolved depletion horizons on the same three public domains, computed without fitting any dynamical parameter of the reduced core (the G3P/GRACE product line: Tapley et al. 2004; Griebmeier et al. 2023; Guentner et al. 2024):

| Basin | Trend (cm/yr) | 2023 anomaly (cm) | Horizon to window minimum (yr) |
|---|---|---|---|
| Indo-Gangetic (N. India) | $-49.7$ | $-414$ | $\approx2.7$ |
| North China Plain | $-18.6$ | $-145$ | $\approx7.9$ |
| Central Valley (US) | $-16.1$ | $-84$ | $\approx9.5$ |
| La Mancha (Spain) | $-3.2$ | $-20$ | $\approx21.4$ |
| High Plains (US) | $-7.9$ | $-160$ | already at minimum |
| global mean | $-0.4$ | $-14$ | $\approx47.6$ |

| Country | Reserves (kt) | Reserve-life horizon (yr) |
|---|---|---|
| China | $3{,}400{,}000$ | $\approx28$ |
| United States | $1{,}000{,}000$ | $\approx45$ |
| Jordan | $820{,}000$ | $\approx62$ |
| Morocco | $50{,}000{,}000$ | $\approx1{,}250$ |
| Australia | $5{,}800{,}000$ | $\approx2{,}088$ |
| World (reserves) | $74{,}000{,}000$ | $\approx309$ |
| World (resources, $\varepsilon=0.10$) | $>300{,}000{,}000$ | $\approx1{,}125$ |

The fisheries column reports the pure-decay proxy $\mathrm{ADH}=F^{-1}\ln(\mathrm{SSB}_{\mathrm{now}}/(0.2\max\mathrm{SSB}))$ under current $F$, with median $\approx1.8$ yr across the 43 assessed stocks with finite SSB and $F$ series (zero entries included; the RAM Legacy cohort of Ricard et al. 2012). The sampled-governance companion paper's spectral screen uses the 42-stock annual-managed subset of this same 43-stock population — a nested pair per the source's own caption, not two different cohorts. The scope discipline is the row's load-bearing content: none of the reported numbers is a computed instance of the model's own first-hitting time — the groundwater column is a trend-to-window-minimum extrapolation, the phosphate column a reserve-life ratio, and the fisheries column a pure-decay proxy with recruitment omitted (its caption states it is not an abiotic horizon). They are descriptive, component-resolved diagnostics in the framework's two-pool logic, not dynamical predictions. The equal-weight inverse-horizon score of the four basins still above their window minimum and world phosphate reserves, $\Sigma_\mathrm{reserves}\approx\frac15(\frac1{2.7}+\frac1{7.9}+\frac1{9.5}+\frac1{21.4}+\frac1{309})\approx0.130\ \mathrm{yr}^{-1}$, is a ranking device, not a componentwise certificate. The record carries source-specific empirical status: the reserve classification is economic (US reserves have remained near $1{,}000{,}000$ kt while cumulative production since 1996 is of order $600{,}000$ kt), and the resource-based world horizon ($\approx1{,}125$ yr at $\varepsilon=0.10$) is more than three times the reserve-based figure ($\approx309$ yr) — the two-compartment split is what prevents these from being collapsed into one number. These tables are the A018 statement of the same diagnostics; the G3P index record of §5.5.1 is its A013 statement, and the two are cited together.

### 5.5.3 The phosphate reserve-life ratio (application record)

At constant current production $C_G$, the reserve-life ratio is $T_\mathrm{reserve}=G_\mathrm{reserve}/C_G$; at approximately $74{,}000$ Mt of world reserves and $240{,}000$ kt/yr of production (U.S. Geological Survey 2026) this is approximately $309$ years. The arithmetic is internally consistent as a reserve-life ratio to zero; it is not a physical exhaustion forecast, because reserve classification changes with prices, technology, exploration, and regulation. The reserves/resources split discipline is part of the row: a resource-threshold calculation $T_\mathrm{resource,10\%}=0.9\,G_\mathrm{resource}/C_G$ answers a different question and must not share a column with the reserve-life ratio without an explicit convention label. The source vintage of the reserve and production quantities is supplied at submission; the record carries source-specific empirical status.

### 5.5.4 The fisheries removals-only pressure time (counterexample/limit)

When $\mathrm{SSB}_\mathrm{now}>B_{\lim}>0$ and $F_\mathrm{now}>0$, define $R_B=\log(\mathrm{SSB}_\mathrm{now}/B_{\lim})$ and

$$
\Theta_F=\frac{R_B}{F_\mathrm{now}},
$$

the Fishing-Only Time-to-Reference: the crossing time of the deliberately incomplete comparison process $\dot B=-F_\mathrm{now}B$. It is a removals-only pressure time scale — the time unit comes from rescaling a stock-reference margin by one isolated gross-loss rate. Because recruitment, somatic growth, maturation, natural mortality, density dependence, environmental forcing, and future policy are omitted, $\Theta_F$ is not a net biomass depletion diagnostic, not a demographic hitting-time estimate, and not a member of the $J^\mathrm{gross}$–$H^\mathrm{loc}$–$T_A$ hierarchy. A genuinely local biomass-decline ratio $H_B^\mathrm{loc}=(B-B_{\lim})/[-\dot B]_+$ would require a compatible net $\dot B$ estimate, and a demographic hitting time a fully specified population model; RAM Legacy SSB and $F$ data (Ricard et al. 2012) do not by themselves supply these quantities or models. Spawning biomass is not an abiotic support pool. The construction is retained specifically to show why an isolated gross-removal time scale must not be promoted to a net depletion diagnostic; the worked fisheries instance of exactly this discipline is the sampled-governance companion paper's case study.

# 6. Depletion horizons and first-passage semantics

## 6.1 Two objects, not one

The ledger's own first-passage object is the model hitting time of Definition 5.3 — a quantity on trajectories of the mass-conserved ledger or of a named reduced system. The public-data quantities of §5.5 are constructed proxies on observed series. The distinction is the entry discipline of this section: the surrogates below do not compute the ledger's hitting time, do not complete the ledger stochastically, and do not identify physical failure thresholds; the scoping statement is shared with the sampled-governance companion paper, which owns the model-side object and its empirical identification.

## 6.2 The observed-drift Brownian surrogate

**Definition 6.1 (Observed-drift Brownian surrogate).** Let $A_0$ be the latest observed anomaly and $\mu=\widehat\mu<0$ the fitted drawdown rate. On the scale of the tabulated series define

$$
A(t)=A_0+\mu t+\sigma W_t,
\qquad A(0)=A_0>A_{\min}^{\mathrm{win}},
$$

where $W$ is a standard Wiener process, $\sigma>0$ a chosen noise scale, and the process is stopped at first reaching the record-relative barrier $A_{\min}^{\mathrm{win}}$.

This is a statistical surrogate for the empirical trend extrapolation. It is not a hydrological constitutive law, is not mass-conserving, and is not a perturbation or stochastic completion of the ledger's active-pool equation or of the finite-donor primitive system of §2.2. The non-completion non-claim is part of the definition.

## 6.3 The inverse-Gaussian groundwater first passage

**Theorem 6.2 (Inverse-Gaussian first passage).** Let $T_{\mathrm{GW}}=\inf\{t>0:\ A(t)\le A_{\min}^{\mathrm{win}}\}$ for the process of Definition 6.1 and $d=A_0-A_{\min}^{\mathrm{win}}>0$. Conditional on treating $\mu$ and the barrier as fixed,

$$
T_{\mathrm{GW}}\sim\operatorname{IG}(\nu,\lambda),
\qquad
\nu=\frac{d}{|\mu|},
\qquad
\lambda=\frac{d^2}{\sigma^2},
$$

in the mean–shape parameterization; in particular $\mathbb E[T_{\mathrm{GW}}]=\nu=H^{\mathrm{win}}_{\mathrm{GW}}$ and $\operatorname{Var}(T_{\mathrm{GW}})=\nu^3/\lambda=d\,\sigma^2/|\mu|^3$.

*Proof (verified present; summary).* The first-passage time of a Brownian motion with constant negative drift to a lower barrier is inverse Gaussian (the classical first-passage framework: Chhikara and Folks 1989; Redner 2001); substituting the initial gap $d$, drift magnitude $|\mu|$, and diffusion scale $\sigma$ gives the law, and the standard inverse-Gaussian moments give the displayed mean and variance. $\blacksquare$

The mean of the stochastic surrogate equals the deterministic trend-to-window-minimum ratio of §5.5.1; that equality is the precise sense in which the tabled groundwater numbers are first-passage means of a declared surrogate.

## 6.4 Moments, zero-noise limit, and median

**Corollary 6.3 (Zero-noise limit and median).** As $\sigma\to0^+$, $T_{\mathrm{GW}}\to H^{\mathrm{win}}_{\mathrm{GW}}$ in probability, and at $\sigma=0$ the deterministic trajectory reaches the barrier exactly there. For every finite $\sigma>0$ the inverse-Gaussian median $m$ satisfies

$$
m<\nu=H^{\mathrm{win}}_{\mathrm{GW}},
\qquad
F_T(\nu)=\frac12+e^{2\lambda/\nu}\,\Phi\!\bigl(-2\sqrt{\lambda/\nu}\bigr)>\frac12 .
$$

The variance scales as $\sigma^2$ and the standard deviation and small-noise quantile widths as $\sigma$.

*Proof (verified present; summary):* evaluate the inverse-Gaussian CDF $F_T(t)=\Phi(\sqrt{\lambda/t}(t/\nu-1))+e^{2\lambda/\nu}\Phi(-\sqrt{\lambda/t}(t/\nu+1))$ at $t=\nu$; the second term is strictly positive for finite $\lambda$, so the median lies strictly below the mean; the concentration statement follows from the variance. $\blacksquare$

These are conditional distributional statements about the surrogate. They are not corrections to the tabled years, and they do not show that physical water mass is depleted faster.

## 6.5 The record-relative barrier discipline

The barrier $A_{\min}^{\mathrm{win}}$ is selected from the same finite observation window used to estimate $\widehat\mu$. It is therefore a path-dependent, record-relative threshold, not an independently identified hydrological failure floor; future passage below it represents a record-breaking stress event under the surrogate, not physical exhaustion. Three boundary facts complete the discipline:

1. **Already-at-minimum.** If $A_0=A_{\min}^{\mathrm{win}}$, the stopping-time convention gives $T_{\mathrm{GW}}=0$ deterministically for every $\sigma$; the inverse-Gaussian family has a degenerate boundary limit concentrated at zero, and $\operatorname{IG}(0,0)$ is not an ordinary inverse-Gaussian distribution. Zero cells report zero relative to the selected observational barrier — not zero physical uncertainty and no confirmation of collapse.
2. **Independent physical thresholds.** If an independent physical threshold $A^\sharp<A_{\min}^{\mathrm{win}}$ is specified, the same constant-drift surrogate gives the conditional mean $\mathbb E[T^\sharp]=(A_0-A^\sharp)/|\mu|$, longer than the record-relative proxy because the barrier is lower. This is a statement within the surrogate, not a general lower-bound theorem for the physical ledger, whose drift and state coupling may differ.
3. **Classification.** The load-bearing content of this row is the interpretation boundary itself: a record-relative barrier makes the passage time a property of the observation window, and no reading of the tabled numbers escapes that qualification.

## 6.6 The geometric-Brownian fisheries first passage

**Theorem 6.4 (Geometric-Brownian correction).** Let $dB_t=-hB_t\,dt+\sigma B_t\,dW_t$ under the Itô convention with $h>0$ and $0<B_{\min}<B_0$, and $T_{\mathrm{fish}}=\inf\{t>0:\ B_t\le B_{\min}\}$. Then

$$
T_{\mathrm{fish}}\sim\operatorname{IG}(\nu_F,\lambda_F),
\qquad
\nu_F=\frac{\log(B_0/B_{\min})}{h+\sigma^2/2},
\qquad
\lambda_F=\frac{\log(B_0/B_{\min})^2}{\sigma^2},
$$

so $\mathbb E[T_{\mathrm{fish}}]=\log(B_0/B_{\min})/(h+\sigma^2/2)$; as $\sigma\to0^+$ this converges to the deterministic pure-decay horizon when $h=F$ and $B_{\min}=B_{\lim}$.

*Proof (verified present; summary):* Itô's lemma (Øksendal 2003) gives $d\log B_t=-(h+\sigma^2/2)\,dt+\sigma\,dW_t$, so the logarithmic threshold is a Brownian first-passage problem with initial distance $\log(B_0/B_{\min})$ and downward drift $h+\sigma^2/2$; the inverse-Gaussian result of Theorem 6.2 applies. $\blacksquare$

For fixed arithmetic drift and the Itô parameterization, the finite-noise mean is strictly shorter than the deterministic horizon. This is a property of the chosen surrogate parameterization; it is not a universal claim that environmental variability accelerates physical biomass loss. The construction joins the removals-only classification of §5.5.4 — the same pure-decay process, now under a declared stochastic surrogate — and the worked fisheries case at the boundary with the sampled-governance companion paper.

## 6.7 The constant-production phosphate passage time (application record)

Under the deterministic surrogate $\dot R=-P$ with constant production $P>0$, the first-passage time to a fixed threshold $R_{\min}\in[0,R_0)$ is

$$
T_{\mathrm{phos}}=\frac{R_0-R_{\min}}{P},
$$

the reserve-life ratio being the $R_{\min}=0$ special case and a threshold fraction $\varepsilon R_0$ giving $(1-\varepsilon)R_0/P$. This is a conditional reserve-classification proxy under constant production; because reserves are an economic classification rather than a fixed physical stock, it is not a forecast of geological exhaustion without an explicit resource and production model. No stochastic phosphate extension is required for the interpretation. The record's status is consistent with §5.5.3 (source-specific empirical status; the two rows are the same content's A024 and A013 statements, cited together).

## 6.8 The explicit non-claims

The first-passage semantics close with the source's explicit boundary list, all seven of which hold in this paper:

1. The Brownian and geometric-Brownian processes are not stochastic completions of the ledger and do not conserve its mass compartments.
2. No theorem relates $\widehat\mu$ to $-\dot A$ of the companion cores, to the finite-donor primitive system, or to the three-state delay equation.
3. The model hitting time $T^{\mathrm{dep}}$ is not shown to be inverse Gaussian.
4. The historical groundwater minimum is not an independently identified physical failure barrier.
5. A shorter surrogate median or Itô mean is not evidence of faster physical depletion.
6. The gross active-pool horizon and its productivity-illusion interpretation are not first-passage results treated here.
7. The fisheries calculation is not a stage-structured fisheries model, and the phosphate calculation is not a geological-reserve model.

## 6.9 Parameter and observation uncertainty

The inverse-Gaussian results condition on the drift, barrier, and noise scale. In the groundwater application $\widehat\mu$ is estimated from a finite, potentially autocorrelated record and the barrier is selected from that same record; measurement error, serial dependence, seasonal forcing, spatial aggregation, trend breaks, and common climatic drivers are separate uncertainties, and integrating any of them out yields a predictive mixture rather than a single inverse-Gaussian law. A residual scale estimated from the same window does not by itself identify process noise. No calibrated predictive distribution is claimed; the full uncertainty treatment belongs to the sampled-governance companion paper.

# 7. The domain templates at registered status

The phosphorus and groundwater sources enter this paper as **registered template obligations**: both sources' own inventories state that no constitutive content — no equations, parameter files, code, or outputs — was supplied. What they contribute, and what is stated here at exactly that status, is the identification architecture: the competing-model ladders (one identification object per source), the falsifiability protocols, and the displacement disciplines. Their empirical identification and observation governance belong to the sampled-governance companion paper.

## 7.1 The phosphorus template (registered template obligations)

The minimum competing model set is a three-step ladder:

- **H0 — aggregate regional phosphorus balance**: the null comparator of the identification ladder, supported over the more complex models only if those fail to improve held-out prediction, calibrated uncertainty, safety-boundary relevance, or decision advantage.
- **H1 — multi-compartment regional/catchment model**: the typed moiety ledger with extraction, regional, and catchment layers linked by trade and land-routing interfaces. The displacement discipline rides this rung: a regional safety claim must check exported phosphorus burden through imports, trade, waste shipment, or feed supply.
- **H2 — spatial trade-network/catchment model**: trade and transport as explicit matrices or correspondences with sign, units, delay, ownership, and boundary status declared at every interface. The compositional-certificate conditions ride this rung — interface assumptions, shared-control compatibility, and nonblocking institutional events — together with the falsification protocol: the module is falsified as a necessary architecture if simpler models predict held-out material, service, and safety outcomes equally well with equal or better calibrated uncertainty, in which case the architecture must be narrowed.

## 7.2 The groundwater template (registered template obligations)

The physical ladder is likewise three-step: **H0** one-pool storage, the null comparator; **H1** fast/slow two-pool storage with bidirectional leakage; **H2** a justified distributed or higher-dimensional model. The two-pool hypothesis is a falsifiable competing physical hypothesis, not a universal ontology: it is supported only by improved held-out state, service, and safety prediction or demonstrably better calibrated uncertainty. The three rungs are one identification object; the ladder is not to be split. The institutional ladder restates the response-sign taxonomy: scarcity-amplifying extraction (the H1 statement, whose named instantiation belongs to the delay-dynamics companion paper) and protective restraint or restoration (the H2 statement, likewise instantiated there), with the discipline that no generic delay parameter is interpreted as an institutional lag without dated evidence of observation, assessment, authorization, implementation, and enforcement.

## 7.3 The two-pool gap

The two-pool exact specialization remains open. The admitted object is the one-pool affine approximation; no two-pool model is claimed as established anywhere in this paper. The two-pool structure enters only as the descriptive logic of the applied tables of §5.5.2 — component-resolved diagnostics distinguishing active-pool stress from geological classification — and as the registered identification hypothesis H1 whose support conditions are those of §7.2. This boundary is restated in §10 among the limits.

**Two-pool identification requirements (registered identification requirements).** The identification requirements of the two-pool hypothesis are registered with the ladder, and they are what make H1 falsifiable rather than nominal. Identifying the fast/slow split against the one-pool null requires independent constraints: geological geometry — the depth and extent of the aquitard separating the fast and slow formations — multi-depth hydraulic heads, pumping tests, tracer, isotope, and water-age evidence where available, recharge estimates, and prior ranges for the storage coefficients $C_i$ and the cross-formational leakage coefficient $\kappa_{fs}$ (A005, §7). The residual discipline is part of the requirements: leakage may not absorb unexplained residuals — a residual left unexplained by the identified flux structure is model error, reported as such and not attributed to leakage. These are registered identification requirements at the module's template status; no constitutive content stands behind them, and their empirical evaluation belongs to the sampled-governance companion paper.

## 7.4 Extractor-side harvest economics: a scoped remark

**Open access, the modified golden rule, and instrument scope (a remark on policy-instrument scope).** The depletion diagnostics of §§5–6 read a ledger whose realized trajectory can be set by the economics of extraction; the extractor-side counterpart of those diagnostics is stated here as a scoped remark of this applications area. In a Schaefer-style stock $\dot S=g(S)-H$ with $g$ strictly unimodal, cost $c$ per unit effort, price $p$ per unit harvest, and catchability $q$ (A001, Remark 12.1): under open access, rent dissipation drives the equilibrium stock to $S_\mathrm{OA}=c/(pq)$, where per-unit-effort profit vanishes, so a viability floor $S_{\min}>S_\mathrm{OA}$ makes every open-access equilibrium infeasible — the system is driven below the floor; and the rent-maximizing private steady state obeys the modified golden rule $g'(S_\rho)=\rho$, with $S_\rho$ falling toward the MSY-over-exploitation side as the discount rate rises, so a floor $S_{\min}>S_\rho$ is violated by the private optimum as well. The instrument scope is the remark's discipline: a per-unit harvest tax $t$ shifts the open-access stock to $S_\mathrm{OA}(t)=c/((p-t)q)$, increasing in $t$, so that for $t$ large enough the shifted equilibrium lies above any floor $S_{\min}<S_\mathrm{OA}(t)$ — it is the open-access stock, not the floor, that the instrument moves. The remark is the extractor-side counterpart of the commons-obstruction family of strategic over-extraction: the same exit from viability, reached through rent dissipation and discounting rather than through equilibrium over-harvesting.

# 8. The seam to the delay-dynamics companion paper

The partition between this paper and the delay-dynamics companion study is fixed by the research programme's ledger-to-dynamics interface contract. This paper owns the closed material accounting: the primitive ledger equations and full routing, the conservation and positivity theorems of §3, the componentwise deficit and depletion diagnostics of §§4–6, and the closed-donor no-rest and extraction-integrability limitations. The delay-dynamics companion owns the named open/frozen-donor retarded systems and their bifurcation results, stated locally there. The seam is viable, but not because the closed primitive ledger dynamically reduces to the working retarded field: the two are different completions, and the contract records both the exact shared object and the rejected mapping.

**The exact shared object (identity, restated from the interface contract).** Under the single-resource specialization contract

$$
\mathcal S_{1R}:\quad \text{single resource},\quad S=R,\quad \chi=1,\quad \mu=\nu=\rho=0,\quad C^A=0,
$$

with the local stock equation $\dot N=R-qEN$, the deficit identity

$$
D(t):=qE(t)N(t)-R(N(t),A(t))=-\dot N(t),
\qquad
\Lambda(t):=[D(t)]_+=[-\dot N(t)]_+
$$

holds for every trajectory of either the specialized ledger or the named core. *Proof:* substitute the stock equation (Lemma 4.3). $\blacksquare$ The mapping type is exact specialization for the identity once the local stock equation and $\mathcal S_{1R}$ are imposed; the three-state core's constitutive replacement $R(N,A)\to rN(1-N/K)$ is separately an approximation and carries its own finite-time scope. The delay-dynamics companion restates the same identity locally in one line; the identity is the one object both papers may prove without substantive duplication.

**The hand-off projection (a projectable reduction).** Under the institutional-failure specialization, the macroeconomic block, prices, and demand do not appear in $(\dot N,\dot A,\dot U,\dot Z,\dot E)$; the ecological–institutional subsystem is an exact closed projection for every $\varepsilon>0$, with no singular limit required. *Proof (verified present; summary):* under the specialization, each of the five right-hand sides depends only on the block's own variables and the delayed memory; none contains the macroeconomic states, prices, or demand. $\blacksquare$ The projection is classified as a projectable reduction in the theorem-atlas companion's projectability-criterion family; this paper states the hand-off, and the delay-dynamics companion states the named retarded equations it receives.

**The non-reduction boundary (boundary statement, restated from the interface contract).** There is no exact dynamic reduction from the closed primitive finite-donor ledger (`LEDGER-PRIM-CLOSED-v1`) to the working four-state field (`DYN-C4-WORKING`) — not as a projectable reduction and not as a regular perturbation. The reasons are mathematical:

1. The primitive ledger uses the intrinsic donor-limited target $A^{\mathrm{eq,intrinsic}}$; the working core uses the derived target $A^{\mathrm{eq,W}}=A^{\mathrm{eq,intrinsic}}+\kappa_AK/\omega_A$.
2. At the working equilibrium the two $A^{\mathrm{act}}$ vector fields differ by an $O(1)$ term.
3. The working point requires continuing geological support — the flux $\omega_A(A^{\mathrm{eq,W}}-A^{\mathrm{act,*}})=4.652133\ldots$ stock units per year, supplied every year by a donor the working core treats as a parameter — and is not a rest point of the closed finite-donor system (Theorem 3.11).
4. The cumulative donor-draw quantity $\varepsilon_G(T)=G_0^{-1}\int_0^T|e_{GA}-e_{AG}|\,dt$ is a diagnostic of the derived-target completion, not a trajectory-tracking error between the two fields; no finite-time tracking theorem between the completions holds.
5. The closed primitive system makes sustained extraction integrable (Theorem 3.13) and therefore cannot possess the working positive-flux rest indefinitely.

The mapping type for exact dynamic reduction is rejected; the permitted relation is analogy for shared mechanism language plus diagnostic reconstruction of omitted mass flows. The delay-dynamics companion's global periodic results are properties of its named cores and do not transfer to the closed primitive ledger. In the other direction, the working core is an open projection: omitted turnover is routed to a diagnostic detritus or inert sink, imposed recharge corresponds to geological draw, and the reduced trajectory's mass discrepancy is reconstructible from the omitted flows — a disclosure the delay-dynamics companion carries as part of its local model statement, and the approximation content separated from this paper's conservation theorem in §3.3.

**The frozen-donor limit and its scope (a completion distinction at approximation scope).** Rescaling the donor as $G=G_0g$ with $g(0)=1$ gives $\dot g=-G_0^{-1}(e_{GA}-e_{AG})$. The limit $G_0\to\infty$ freezes $g$ but does not restore the working completion's derived target: the limiting recharge field still uses $A^{\mathrm{eq,intrinsic}}$, not $A^{\mathrm{eq,W}}$, so the scaling is not a regular perturbation of the working four-state vector field. Local Hopf persistence of the working core under this primitive scaling is not claimed; a different derived-target completion would be required before a regular-perturbation theorem could be formulated.

**The long-time finite-budget interpretation (an interpretation at conditional/open status).** With the donor $G(t)$ included as a state, the closed system is an autonomous retarded equation with a slow donor coordinate. The companion's $\tau_+\approx150$ yr upper cycle is a frozen-donor object; on the closed system it can persist only as a transient on the finite donor budget. The transient-duration statement is an order/budget bound, not an asymptotic estimate: under a sustained lower extraction flux $c>0$ the duration is bounded above by $G_0/c$, and an $O(G_0/\text{flux})$ scale is the appropriate heuristic (at $G_0/A^{\mathrm{act}*}=10^3$, tens of thousands of years — far above the institutional delays of the companion family). Whether the frozen-donor local Hopf structure persists as a slowly drifting transient in the closed donor system is an open slow-passage problem; the mass budget alone does not establish it. The precise transient duration and any attractor continuation in $(G_0,\tau)$ require a separate computation and remain registered open, not asserted.

**Model-version identifiers.** The closed primitive ledger of this paper is `LEDGER-PRIM-CLOSED-v1`; the delay-dynamics companion's three-state gated core (`DYN-C3-GATED`), turnover-corrected four-state working core (`DYN-C4-WORKING`), and fixed-intrinsic-target quasi-steady core (`DYN-C4-QSS`) are registered as distinct objects, the last never merged with the working core. The refereeability test of the contract holds on both sides: none of this paper's conservation, positivity, no-rest, or diagnostic claims requires the companion's bifurcation results, and the companion contains the full named equations, phase spaces, parameters, and version identifiers without citing this paper for the existence or validity of its dynamics. No circular edge exists.

# 9. What the ledger does not support

## 9.1 Compensatory aggregation is rejected, not merely discouraged

The certification boundary is an algebraic fact. For every positive weight vector $w$ and every component $k$, the construction $b_k=-L$, $b_j=(w_kL+1)/w_j$ (all other components zero) gives $w^{\top}b=1>0$ despite $b_k=-L<0$, for any severity $L$; the theorem-atlas companion carries the two witness constructions of this argument from the accounting and applied sources. Consequently an unrestricted compensatory certificate does not exist: a positive weighted sum cannot certify the conjunction of componentwise nonnegativity. On a restricted feasible domain such as $\mathcal B(x,t)$ (Definition 4.1), a scalar certificate requires the separately proved implication $b\in\mathcal B(x,t)$, $w^{\top}b\ge0\Rightarrow b\ge0$ — provable only from the physical restrictions defining the domain, and vacuous where they exclude nothing. Non-compensatory scalar encodings exist when reference scales and zero conventions are declared — $\min_ib_i$, $\|[-b]_+\|$, and $\max_i[-b_i]_+/s_i^\mathrm{ref}$ preserve the conjunction $b_i\ge0$ — but they discard the identity and cause of the limiting component, so the vector accompanies them. Scalar summaries may rank or communicate; certification requires the full vector, a logically equivalent non-compensatory encoding, component thresholds, or a proved feasible-domain implication.

## 9.2 The double-counting discipline

Five rules, each carried by a proved or defined row of this paper, jointly prevent double counting and phantom mass:

1. **One balance per moiety.** Conservation laws attach to declared moieties (Theorem 3.1); adding unlike units — biomass, money, biodiversity indices, exergy — into one conserved scalar is not authorized by any conservation theorem.
2. **Explicit stoichiometry.** Entries are added within an incidence row only when types and units agree; every conversion is an explicit coefficient in $S$ (§2.1, §2.3).
3. **Yield routing.** A transformation represented with yield below one must route the omitted fraction to a represented compartment or a declared boundary flow; otherwise the moiety balance holds only after silently dropping the moiety (§3.2).
4. **No ghost sinks.** Opposite-sign incidence of the same primitive is checkable, and the six-state cancellation shows the check passing (§3.10) — while the same template shows that cancellation without donor-limited admissibility establishes nothing.
5. **Classification labels stay out of the columns.** Reserve-life and resource-threshold quantities answer different questions and share a column only under an explicit convention label (§5.5.3); diagnostic labels never determine material routing (§2.5).

## 9.3 The negative and boundary content is first-class

Three rows of this paper are counterexample-or-limit rows and are stated as such: the fisheries removals-only time (§5.5.4) exists to block a promotion; the record-relative barrier discipline (§6.5) exists to qualify every groundwater number in §5.5; the seven non-claims (§6.8) exist to fence the first-passage theorems off from the physical ledger. Together with the false-implication record of §5.1, the conditional status of §3.2, and the rejected dynamic mapping of §8, they carry the paper's boundary content: the accounting layer certifies balances, positivity, and classifications — and it declares, on the line, everything it does not certify. A diagnostic identifies where a floor is violated or how fast a stock currently declines; it does not establish a mechanism, and under the architecture's no-transfer rule a diagnostic claim never inherits the status of a control or causal claim (the architecture companion paper).

# 10. Provenance, reproducibility, and limits

**Sources.** The retained set derives from twelve sources of the research programme's corpus, each read in full by the scientific closure passes whose per-statement findings govern the statuses above: A001 (the top-down architecture source; 1 row), A002 (the general typed-theory source; 5 rows), A003 (the institutional-feedback source; 1 row), A004 (the phosphorus-agriculture module source; 3 rows), A005 (the groundwater module source; 5 rows), A006 (the robust epistemic viability source; 1 row), A010 (the ten-state admissibility-perspective source; 3 rows), A012 (the registered delay-family source; 2 rows), A013 (the componentwise-accounting source; 11 rows), A018 (the unified applied source; 5 rows), A019 (the closed finite-donor ledger source; 8 rows), and A024 (the first-passage source; 7 rows). The committed articles of record for five of these sources are read alongside the source manuscripts and carry the governing mathematics where they differ: the corrected articles of record for the closed ledger (A019), the delay dynamics (A012), the capital-liquidation study (A018), the componentwise accounting (A013), and the first-passage study (A024). Row-level evidence: the canonical statement inventory (409 rows; the 52 rows behind this paper each verified against its source in the dated closure campaign). Closure record: the per-source closure record of that campaign. Seam: the ledger-to-dynamics interface contract. Architecture: the research programme's publication-architecture record. Six manuscript-native entries carry source-declared content at its own statuses, with no inventory row: the A005 two-pool identification requirements at registered template status (§7.3); the A001 sink-obstruction construction and closed-unrecycled-ledger corollary at remark status (§2.4); the A018 illustrative $\psi$-assignment calibrated examples (§2.5); the A010 registered application prerequisites and the audited negative witnesses of the ten-state admissibility audit (§3.10); and the A001 Clark under-extraction remark at policy-instrument scope (§7.4).

**Proof handling.** Proofs marked *reproduced* are printed in full from the source. Proofs marked *verified present; summary* exist in full in the source (the closure passes verified proof presence and read them); the summaries are faithful to the source arguments, and the publication version reproduces each proof verbatim. The canonical conservation and invariance family (§3.1) is stated with the theorem-atlas companion as proof owner; this paper reproduces no atlas proof beyond what its local statements require.

**Reproducibility.** The paper is analytical; it cites no computational artifact as evidence. The application records of §5.5 and §6.7 carry their source-stated evidentiary levels: the G3P values are accepted at attested source status with the submission-stage supplement pending (processing files, source extracts, and shared references not yet distributed); the phosphate reserve and production quantities carry source-specific empirical status with the source vintage supplied at submission; the fisheries proxy values are descriptive statistics of the cited assessment database. The unreproduced data pipelines remain on this research programme's computational docket. A manuscript self-check script (standard-library only, idempotent), committed with the programme's repository, verifies that every cited inventory identifier resolves, that the cited set equals the retained set plus the declared cross-references, and that the statement inventory contains every retained row exactly once.

**Limits.** (i) The two-pool exact specialization of the groundwater template remains open; the admitted object is the one-pool affine approximation, and no two-pool model is claimed as established (§7.3). (ii) The phosphorus and groundwater rows are registered template obligations: no constitutive content exists behind their identification ladders, and their empirical evaluation belongs to the sampled-governance companion paper. (iii) The domain templates' competing-model ladders are one identification object per source and are stated as observation-governance content, not as ledger theorems. (iv) The non-reduction boundary of §8 is permanent mathematics, not a gap: the closed primitive ledger and the working retarded field are different completions, and no result of this paper or of the delay-dynamics companion may be read as reducing one to the other. (v) The first-passage theorems of §6 concern declared stochastic surrogates, not the ledger: they do not compute the ledger's hitting time, do not conserve its mass, and carry the record-relative-barrier and non-claim disciplines verbatim. (vi) The G3P, phosphate, and fisheries application records are classified diagnostics at their stated evidentiary levels — statistical index, arithmetic ratio, removals-only pressure scale — and none is a calibrated early-warning system or a forecast. (vii) The frozen-donor transient-duration statement is an order/budget bound, and the slow-passage persistence question is open; the conditional theorem of §3.2 stays conditional, with its jump-interpretation and yield-routing obligations open per application. (viii) All inventory rows behind this paper (Appendix A) completed the dated source-verification campaign; no statement depends on a pending verification, and the 27 open rows of the inventory (the conditional-paper sources A021, A022, A023) are behind no claim of this paper.

# Appendix A. Statement inventory

This appendix inventories the formal statements of the paper in two tables. The **identifier** column carries the research programme's statement-inventory row codes (`CC-A0dd-ddd`) or manuscript-native keys (`MS-Native-n`); the codes key each statement to the source-to-canonical provenance inventory committed with the programme's repository and are provenance keys, not citations. Every inventory-sourced entry was verified against its source manuscript in the dated closure campaign (full-source reads with per-statement confirmation of existence, kind, proof presence, module, and mapping type; A001 and A002 on 2026-08-27, the remaining ten sources on 2026-08-28) — content-level acceptance, with no theorem status promoted and the cross-module interface contract remaining open per row. The tables show 54 inventory codes because two of them (CC-A002-040, the canonical form owned by the theorem-atlas companion; CC-A018-007, the approximation content owned by the delay-dynamics companion) appear only as cross-citation pointers inside the basis cells of other rows — they are cross-references, not retained rows, and the retained count is 52.

**Legend and disclaimer.** Entries categorized as *Definition*, *Registered template obligation*, *Registered identification requirements*, *Registered application prerequisites*, or *Illustrative calibrated examples* are stipulated or declared — they carry no empirical truth-value and need no proof. Entries categorized as *Theorem*, *Lemma*, *Identity*, *Corollary*, or *Conditional theorem* are established under the assumptions stated where they appear (proved in this paper, or summarized from the identified source's proof, with the full proof verified present in the source). Entries categorized as *Application record* carry their source-specific evidentiary level; entries categorized as *Counterexample/limit*, *Boundary statement*, *Negative witnesses*, *Completion distinction*, *Interpretation*, or *Remark* state rejections, scope restrictions, constructions, or source-declared commentary at exactly their declared status. The formal validity of any entry within the declared framework does not by itself imply applicability to an empirical system (§10, Limits). No status is promoted anywhere in this inventory; the manuscript-native rows are restatements of the interface contract (MS-Native-1, MS-Native-2) and source-declared remarks, requirements, examples, and witnesses carried at their declared statuses without inventory rows (MS-Native-3 through MS-Native-8), not new results, and the paper asserts nothing beyond the statuses above.

**Table A1. Stipulated definitions and registered entries.**

| Identifier | Statement | Category | Basis |
|---|---|---|---|
| CC-A002-014 | Support-provenance partition and directional support gap (§4.3) | Definition | Defined source object; closure campaign 2026-08-27; atlas-companion entry |
| CC-A003-004 | Standing-stock culling mechanism type (routing never set by diagnostic labels) (§2.5) | Definition | Defined source object; closure campaign 2026-08-28 |
| CC-A004-001 | H0 aggregate regional phosphorus balance (null comparator) (§7.1) | Definition (registered template obligation) | Defined source object; closure campaign 2026-08-28; identification shared with the sampled-governance companion |
| CC-A004-002 | H1 multi-compartment regional/catchment model (displacement discipline) (§7.1) | Definition (registered template obligation) | Defined source object; closure campaign 2026-08-28 |
| CC-A004-003 | H2 spatial trade-network/catchment model (falsification protocol) (§7.1) | Definition (registered template obligation) | Defined source object; closure campaign 2026-08-28 |
| CC-A005-001 | H0 one-pool storage (null comparator) (§7.2) | Definition (registered template obligation) | Defined source object; closure campaign 2026-08-28 |
| CC-A005-002 | H1 fast/slow two-pool storage with bidirectional leakage (§7.2) | Definition (registered template obligation; falsifiable hypothesis, not an ontology) | Defined source object; closure campaign 2026-08-28; two-pool gap: §7.3 |
| CC-A005-003 | H2 distributed or higher-dimensional groundwater model (§7.2) | Definition (registered template obligation; one identification object with -001/-002) | Defined source object; closure campaign 2026-08-28 |
| CC-A005-004 | Scarcity-amplifying extraction (institutional hypothesis) (§7.2) | Definition (registered template obligation; A003 H1 restatement) | Defined source object; closure campaign 2026-08-28; named instantiation in the delay-dynamics companion |
| CC-A005-005 | Protective restraint/restoration (institutional hypothesis) (§7.2) | Definition (registered template obligation; A003 H2 restatement) | Defined source object; closure campaign 2026-08-28; named instantiation in the delay-dynamics companion |
| CC-A013-002 | State-dependent feasible balance domain (§4.2) | Definition | Defined source object; closure campaign 2026-08-28 |
| CC-A013-003 | Directional regenerative-support fraction and gap (attainment requires closedness) (§4.3) | Definition | Defined source object; closure campaign 2026-08-28 |
| CC-A013-007 | Gross turnover/dependency intensity (false-implication record) (§5.1) | Definition | Defined source object; closure campaign 2026-08-28 |
| CC-A013-008 | Local net-depletion ratio (frozen-rate; +$\infty$ convention) (§5.2) | Definition | Defined source object; closure campaign 2026-08-28 |
| CC-A013-009 | Scenario-conditioned hitting time (§5.3) | Definition | Defined source object; closure campaign 2026-08-28 |
| CC-A019-001 | Primitive donor-limited exchange and mining laws (closed natural block) (§2.2) | Definition (exact specialization) | Defined source object; closure campaign 2026-08-28 |
| CC-A024-002 | Brownian observed-drift surrogate (non-completion non-claim) (§6.2) | Definition (exact specialization) | Defined source object; closure campaign 2026-08-28 |
| MS-Native-3 | Two-pool identification requirements (geological geometry — aquitard depth and extent; multi-depth heads; pumping tests; tracer/isotope/water-age evidence; recharge estimates; prior ranges for $C_i$ and $\kappa_{fs}$; leakage may not absorb unexplained residuals) (§7.3) | Registered identification requirements (template status) | Source-declared template content (A005, §7); no constitutive content behind it; empirical evaluation with the sampled-governance companion |
| MS-Native-5 | $\psi$-assignment mass-routing discipline (evidence per channel; soil-zinc $0.85/0.25$ and pollinator $0.70/0.20$ illustrative pairs; $\approx1.5\times$ trough-depth factor; pre-recruit harvest vs prevented inflow; capital damage not a $\psi$ channel) (§2.5) | Illustrative calibrated examples (logistic two-channel proxy) | Source's illustrative $\psi$-mechanism table (A018, §5); no constitutive claim for the named domains |
| MS-Native-6 | Ten-state calibration underidentification (SSB and $F$ alone insufficient; juvenile abundance through governance timing required; minimum module set) with the four application prerequisites (§3.10) | Registered application prerequisites | Source-declared prerequisites and calibration remark (A010, §11) |

**Table A2. Theorems, identities, application records, and boundary content.**

| Identifier | Statement | Category | Basis |
|---|---|---|---|
| CC-A001-042 | Four-stock mass balance (Proposition 6.1) (§2.4) | Theorem (exact specialization) | Proof verified in source §6.6; closure campaign 2026-08-27; the monograph restates it |
| CC-A002-008 | Typed hybrid conservation ($L^{\top}S=0$, $L^{\top}S^{J}=0$) (§3.1) | Theorem | Proof verified in source §3; closure campaign 2026-08-27; atlas-companion proof owner |
| CC-A002-010 | Closed positive-moiety component bound (§3.1) | Theorem (corollary) | Proof verified in source §3; closure campaign 2026-08-27; atlas-companion proof owner |
| CC-A002-012 | Donor-limited outflows and boundary flows suffice for tangency (§3.1) | Theorem (corollary) | Proof verified in source §3; closure campaign 2026-08-27; atlas-companion proof owner; module formal_foundations |
| CC-A002-038 | Support-saturated logistic stock limit ($O(\kappa)$ Grönwall bound) (§2.6) | Theorem (approximation; partial reduction) | Proof verified in source §9; closure campaign 2026-08-27 |
| CC-A006-001 | Conditional hybrid moiety balance (jump interpretation + yield-routing obligation) (§3.2) | Conditional theorem | Proof verified in source §2; closure campaign 2026-08-28 |
| CC-A010-002 | Local threshold-horizon bound (two-sided bracket) (§5.4) | Theorem | Proof verified in source §8; closure campaign 2026-08-28; canonical form in the atlas companion (CC-A002-040 — cross-reference, not a retained row); predecessor statement |
| CC-A010-003 | Typed conservation under the left-kernel condition (§2.1) | Identity | Verified in source §3.1; closure campaign 2026-08-28; CC-A002-008 family precedent |
| CC-A010-008 | Six-state material cancellation (ghost-sink check; cancellation only) (§3.10) | Identity | Verified on the line in source §9.2; closure campaign 2026-08-28 |
| CC-A012-005 | Decline pressure equals the positive stock-decline rate (§4.4) | Identity | Verified in source §2.1 Eq. (4); closure campaign 2026-08-28; dynamics family owned by the delay-dynamics companion |
| CC-A012-008 | MPF support-saturated logistic stock limit (+ companion simplex invariance) (§2.6) | Theorem (approximation; interior-pointwise, not boundary-uniform) | Proof verified in source §5.5; companion simplex theorem in the committed article of record; closure campaign 2026-08-28; registered family owned by the delay-dynamics companion |
| CC-A013-004 | Six-compartment incidence matrix, zero column sums ($\mathbf 1^{\top}S=0$) (§2.3) | Identity | Verified in source §3.2; closure campaign 2026-08-28 |
| CC-A013-005 | Total represented material conserved (§3.5) | Theorem | Proof verified in source §3.3; closure campaign 2026-08-28 |
| CC-A013-006 | Nonnegative cone forward invariant (donor boundary assumptions) (§3.6) | Theorem | Proof verified in source §3.3; closure campaign 2026-08-28 |
| CC-A013-010 | G3P anomaly-persistence indices (statistical index, not $H^\mathrm{loc}$) (§5.5.1) | Application record | Values accepted at attested source status; submission supplement pending; closure campaign 2026-08-28; cited with CC-A018-017 |
| CC-A013-011 | Phosphate reserve-life ratio (arithmetic, not a forecast) (§5.5.3) | Application record | Source-specific empirical status check required; closure campaign 2026-08-28 |
| CC-A013-012 | Fisheries removals-only threshold time $\Theta_F$ (outside the J/H/T hierarchy) (§5.5.4) | Counterexample/limit | Defined source object; closure campaign 2026-08-28; worked case in the sampled-governance companion |
| CC-A018-002 | Donor-limited vector material ledger and conservation theorem (§3.3) | Theorem (exact conservation identity) | Proof verified in source §3.3; closure campaign 2026-08-28; approximation content separated to the delay-dynamics companion (CC-A018-007 — cross-reference, not a retained row) |
| CC-A018-003 | Nonnegative-orthant theorem (mass orthant, gated-law scope) (§3.6) | Theorem (exact specialization) | Proof verified in source §6; closure campaign 2026-08-28 |
| CC-A018-004 | Exact specialization deficit identity (§4.4) | Lemma (exact specialization) | Proof verified in source §6; closure campaign 2026-08-28; the seam's shared object; restated as MS-Native-1 |
| CC-A018-005 | Exact triangular projection (the seam hand-off) (§8) | Theorem (projectable reduction) | Proof verified in source §6; closure campaign 2026-08-28; A002-036 family |
| CC-A018-017 | Groundwater/phosphate/fisheries applied depletion-horizon tables (§5.5.2) | Application record (descriptive diagnostics, not dynamical predictions) | Source-specific empirical status check required; closure campaign 2026-08-28; cited with CC-A013-010 |
| CC-A019-002 | Natural-block mass identity (full-ledger conservation restored) (§3.4) | Theorem | Proof verified in source §3; closure campaign 2026-08-28 |
| CC-A019-003 | Orthant invariance of the closed ledger (§3.6) | Theorem | Proof verified in source §3; closure campaign 2026-08-28 |
| CC-A019-004 | No interior rest at positive effort (the source's title result) (§3.7) | Theorem | Proof verified in source §4; closure campaign 2026-08-28; routed here by the interface contract |
| CC-A019-005 | Extinction–geochemical rest set (§3.8) | Theorem | Proof verified in source §4; closure campaign 2026-08-28 |
| CC-A019-007 | Extraction integrability (finite donor budget) (§3.9) | Theorem | Proof verified in source §6; closure campaign 2026-08-28 |
| CC-A019-008 | Frozen-donor limit distinction (intrinsic target retained) (§8) | Completion distinction (approximation scope) | Verified in source §7; closure campaign 2026-08-28 |
| CC-A019-009 | Long-time finite-budget interpretation (order/budget bound; open slow-passage problem) (§8) | Interpretation (approximation; conditional/open) | Conditional/open; closure campaign 2026-08-28 |
| CC-A024-003 | Inverse-Gaussian groundwater first passage (§6.3) | Theorem | Proof verified in source §2; closure campaign 2026-08-28 |
| CC-A024-004 | Mean, variance, zero-noise limit, and median results (§6.4) | Corollary | Proofs verified in source §2; closure campaign 2026-08-28 |
| CC-A024-005 | Record-relative barrier and boundary-degenerate case (zero-cells discipline) (§6.5) | Counterexample/limit | Verified in source §3; closure campaign 2026-08-28 |
| CC-A024-006 | Geometric-Brownian fisheries first passage (Itô drift) (§6.6) | Theorem | Proof verified in source §5; closure campaign 2026-08-28 |
| CC-A024-007 | Constant-production phosphate passage time (§6.7) | Application record | Source-specific empirical status check required; closure campaign 2026-08-28; consistent with CC-A013-011 |
| CC-A024-009 | Seven explicit non-claims relative to the physical ledger (§6.8) | Counterexample/limit | Defined source object; closure campaign 2026-08-28 |
| MS-Native-1 | The seam specialization identity ($\mathcal S_{1R}$: $D=qEN-R=-\dot N$, $\Lambda=[D]_+$) (§8) | Identity | Restatement of the ledger-to-dynamics interface contract; one-line proof here |
| MS-Native-2 | The non-reduction boundary (no exact dynamic reduction of `LEDGER-PRIM-CLOSED-v1` to `DYN-C4-WORKING`) (§8) | Boundary statement (rejected mapping) | Restatement of the contract's five reasons |
| MS-Native-4 | Sink obstructions independent of the stock (no assimilation $\delta\equiv0$; weak assimilation $\delta(K_{\max})<w(H_{\min})$) and the closed-unrecycled-ledger corollary (positive output floor forces an empty viability kernel) (§2.4) | Remark (construction and corollary at source-declared status) | Source remark (A001, Remark 6.1); mechanisms argued inline in the source |
| MS-Native-7 | Variance-unclosed and $Q$-undefined negative witnesses of the ten-state admissibility audit (§3.10) | Negative witnesses (audited status) | Source admissibility stress test (A010); no unique autonomous DDE at the displayed scope |
| MS-Native-8 | Clark under-extraction remark (open access $S_\mathrm{OA}=c/(pq)$ infeasible under a floor $S_{\min}>S_\mathrm{OA}$; modified golden rule $g'(S_\rho)=\rho$; harvest tax shifts $S_\mathrm{OA}(t)=c/((p-t)q)$, not the floor) (§7.4) | Remark (policy-instrument scope) | Source remark (A001, Remark 12.1); extractor-side counterpart of the commons-obstruction family |

# References

Aubin, J.-P. 1991. *Viability Theory*. Birkhäuser, Boston.

Brunner, P. H., and Rechberger, H. 2004. *Practical Handbook of Material Flow Analysis*. Lewis Publishers, Boca Raton.

Chhikara, R. S., and Folks, J. L. 1989. *The Inverse Gaussian Distribution: Theory, Methodology, and Applications*. Marcel Dekker, New York.

Clark, C. W. 1990. *Mathematical Bioeconomics: The Optimal Management of Renewable Resources*. Second edition. Wiley, New York.

Ekins, P., Simon, S., Deutsch, L., Folke, C., and De Groot, R. 2003. A framework for the practical application of the concepts of critical natural capital and strong sustainability. *Ecological Economics* 44: 165–185.

Eurostat. 2001. *Economy-wide Material Flow Accounts and Derived Indicators: A Methodological Guide*. Statistical Office of the European Communities, Luxembourg.

Feinberg, M. 2019. *Foundations of Chemical Reaction Network Theory*. Springer, Cham.

Fischer-Kowalski, M., Krausmann, F., Giljum, S., Lutter, S., Mayer, A., Bringezu, S., Moriguchi, Y., Schütz, H., van Drecht, G., and Wassermann, Y. 2011. Methodology and indicators of economy-wide material flow accounting. *Journal of Industrial Ecology* 15: 855–876.

Griebmeier, P., Kvas, A., Kusche, J., and Dobslaw, H. 2023. G3P: a gravimetric groundwater product for global groundwater monitoring. *Remote Sensing of Environment* 296: 113713.

Guentner, A., Sharifi, E., Haas, J., Boergens, E., Dahle, C., Dobslaw, H., Dorigo, W., Dussailant, I., Flechtner, F., Jaeggi, A., Kosmale, M., Luojus, K., Mayer-Guerr, T., Meyer, U., Preimesberger, W., Ruz Vargas, C., and Zemp, M. 2024. Global Gravity-based Groundwater Product (G3P), Version 1.12. GFZ Data Services.

Munda, G., and Nardo, M. 2009. Noncompensatory/nonlinear composite indicators for ranking countries: a defensible setting. *Applied Economics* 41: 1513–1523.

Nagumo, M. 1942. Über die Lage der Integralkurven gewöhnlicher Differentialgleichungen. *Proceedings of the Physico-Mathematical Society of Japan* 24: 551–559.

Neumayer, E. 2013. *Weak versus Strong Sustainability: Exploring the Limits of Two Opposing Paradigms*. Fourth edition. Edward Elgar, Cheltenham.

Øksendal, B. 2003. *Stochastic Differential Equations: An Introduction with Applications*. Sixth edition. Springer, Berlin.

Redner, S. 2001. *A Guide to First-Passage Processes*. Cambridge University Press, Cambridge.

Ricard, D., Minto, C., Jensen, O. P., and Baum, J. K. 2012. Examining the knowledge base and status of commercially exploited marine species with the RAM Legacy Stock Assessment Database. *Fish and Fisheries* 13: 380–398.

Tapley, B. D., Bettadpur, S., Ries, J. C., Thompson, P. F., and Watkins, M. M. 2004. GRACE measurements of mass variability in the Earth system. *Science* 305: 503–505.

U.S. Geological Survey. 2026. *Mineral Commodity Summaries 2026*. U.S. Geological Survey, Reston, Virginia.

Programme sources. The statement-inventory provenance record (the 409-row canonical inventory, of which the 52 rows behind this paper completed the dated source-verification campaign), the per-source closure record of that campaign, the ledger-to-dynamics interface contract, the research programme's publication-architecture record, and the committed articles of record read alongside the source manuscripts for the closed-ledger, delay-dynamics, capital-liquidation, componentwise-accounting, and first-passage sources, as listed in §10 (Sources), are committed to the project repository at <https://github.com/MIKEAA2020/general-sustainability>.

# Data and code availability

The paper is analytical: no computational artifact is cited as evidence, and every proof is either reproduced in full in this article or summarized with its full version verified present in the identified source. The application records of §5.5 and §6.7 carry their source-stated data provenance. The groundwater anomaly-persistence values derive from the G3P v1.12 satellite product (Griebmeier et al. 2023; Guentner et al. 2024, GFZ Data Services; the GRACE line of Tapley et al. 2004) over the reported April 2002–September 2023 window, and are accepted at attested source status with a submission-stage supplement — the processing files, source extracts, and shared references — pending distribution. The phosphate reserve and production quantities derive from the U.S. Geological Survey *Mineral Commodity Summaries 2026* (U.S. Geological Survey 2026), with the source vintage of the reserve and production quantities supplied at submission. The fisheries proxy values are descriptive statistics of the cited assessment database (the RAM Legacy cohort of Ricard et al. 2012). The unreproduced data pipelines remain on this research programme's computational docket. The verification artifacts — the 409-row statement-inventory provenance record with its 52 paper-retained rows, the dated per-source closure record of the verification campaign, the ledger-to-dynamics interface contract, and the standard-library-only, idempotent manuscript self-check that verifies every cited inventory identifier resolves and that the statement inventory contains every retained row exactly once — are available in the programme's public repository at <https://github.com/MIKEAA2020/general-sustainability>.

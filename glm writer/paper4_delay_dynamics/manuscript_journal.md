% TITLE: Delay-Driven Capital Liquidation and Nonlinear Institutional Dynamics: Named C3/C4 Retarded Systems, the Complete Hopf Cubic, and the Two Institutional Channels
% VENUE: Communications in Nonlinear Science and Numerical Simulation
% TYPE: Applied nonlinear-dynamics article
% RUNNING: Delay-driven institutional dynamics
% KEYWORDS: delay differential equations; Hopf bifurcation; interval certification; institutional dynamics; renewable resources
% CONTRIBUTION: This paper carries out the complete Hopf analysis of a family of named delayed institutional-dynamics systems — interval-certified crossing delays, a sign separation between mobilising and protective delay channels, and an explicit certification hierarchy that separates certified crossings from nominal-tier folds.

# Abstract

This article develops the complete local Hopf analysis of named renewable-resource retarded systems that model delayed institutional response, separating explicitly what is interval-certified from what is numerical evidence. The systems are stated in full: an effort-bounded three-state core of stock, filtered deficit memory, and gated extractive effort; a registered family of ungated, two-channel, active-pool, and primitive-flux variants; a turnover-corrected four-state working core with a declared frozen-donor mass status and a distinct quasi-steady singular-limit object; and a quota-tracking protective channel with two delays. For the mobilising channel the paper states the closed-form equilibrium, the characteristic quasi-polynomial, and the complete Hopf cubic — at most three local frequency families, with an even-pairs algebra that makes the number of positive frequency roots zero or two — together with interval-certified crossing delays $\tau_-\in[3.6661490142739,\,3.6661490142743]$ yr and $\tau_+\in[150.3584773101408,\,150.3584773101421]$ yr at the gated Candidate A point, and first Lyapunov coefficients $\ell_1(\tau_-)=+5.75\times10^{-5}$ and $\ell_1(\tau_+)=+3.55\times10^{-4}$: both crossings subcritical, with the ungated Candidate B lower crossing supercritical ($-9.84\times10^{-5}$). The organising finding is a sign separation. The mobilising delayed gain closes the loop and produces the Hopf pair; the protective sign leaves the Hopf cubic without a positive root (all coefficients positive, $c_2c_1-c_0=0.02209>0$; loop gain $0.08011<1$) and, under the zero-root and characteristic-continuity requirements, excludes delay-induced Hopf points at every protective delay (the $T_r=2.306$ crossing of the sampled protective channel is a crossing of the explicit-Euler factor $1+T_rC_E$, not a Hopf point of the retarded equation); a weighted small-gain theorem for the two-delay interpolation makes a Hopf conditional on sufficient mobilising weight. Every claim carries its level in a four-level certification hierarchy — nominal, re-execution-verified, independently re-executed, certified: the Hopf interval certificates are reproduced identically on re-execution by the committed interval pipeline, while every fold event remains nominal (no Moore–Spence or Krawczyk certificate is obtained).

**Keywords:** delay differential equations; Hopf bifurcation; interval certification; institutional dynamics; renewable resources

---

# 1. Introduction

## 1.1 The question this paper answers

**How do delayed scarcity-mobilising and protective institutional channels generate or suppress Hopf crossings, cycles, bistability, and global periodic events in named C3/C4 retarded systems — and what exactly is established, at what evidentiary level, for each named system?**

The mechanism under study is a specified institutional failure mode, not a general governance theory: an observed stock decline is filtered into a memory state, acted on after a delay, and used to mobilise *more* extractive effort. The named systems are capital and institutional objects — extractive effort as a bounded deployment intensity, a filtered deficit memory, governance capital — coupled to a renewable stock; they are institutional-dynamics models, not biological population models, and their delays are institutional action and deployment lags. Delay-driven resource cycles have a long modelling lineage — the cobweb theorem (Ezekiel 1938), insect-outbreak systems (Ludwig, Jones, and Holling 1978), Nicholson's blowflies (Gurney, Blythe, and Nisbet 1980), and delayed bioeconomic harvesting models (Gao and Zhang 2022; Khiyar et al. 2026) — and the perception and commons-governance literatures document exactly the failure mode under study (Moxnes 1998; Ostrom 1990). The channel with the opposite sign — an institution that tracks a decreasing quota map and cuts effort as the deficit memory rises — is a different loop and is analysed as such. The paper's organising finding is that the sign of the delayed gain $C_Z$ separates the two channels' local mathematics: the mobilising sign closes the loop at sufficient gain and produces a pair of Hopf crossings with subcritical criticality at the baseline parameterisation, while the protective sign leaves the Hopf cubic without a positive root and excludes delay-induced Hopf points at every delay. Between the two sits a two-delay interpolation whose instabilities are governed by a weighted small-gain condition.

What is rare for institutional delay systems, and what this article supplies, is the combination of two disciplines. The first is complete delay-margin analysis in the classical retarded-equation tradition (Hayes 1950; Hale 1977; Hale and Verduyn Lunel 1993): closed-form equilibrium, characteristic quasi-polynomial, crossing delays with simplicity and transversality, and criticality from the first Lyapunov coefficient. The second is validated-numerics certification in the interval tradition (Moore 1979; Kearfott 1996; Cloud, Moore, and Kearfott 2009): the crossing delays are enclosed by interval-Newton certificates on the Hopf cubic and its phase relation, reproduced identically on re-execution by a committed interval pipeline, while the global fold events carry no Moore–Spence or Krawczyk certificate and are labelled nominal. The certification hierarchy (nominal, re-execution-verified, independently re-executed, certified; §10) is enforced per claim, and the separation of what is certified from what is not is offered as a principal result of the presentation.

Two further disciplines organise the paper. First, a *model-registration* discipline: no threshold is cited without its named system and parameterisation, and changing the effort law, the channel split, the support-pool structure, or the memory architecture changes the system — thresholds do not transport between registered variants. Second, a *fold-status* discipline: local Hopf points can be certified, but the global disappearance and reappearance of large-amplitude cycles are located by continuation, multiplier, basin, and turning-region computations, and no Moore–Spence, Krawczyk, or nondegeneracy certificate and no continuous-delay fold proof is claimed for them.

## 1.2 What enters this paper

This paper is the named nonlinear-dynamics paper of a five-paper research programme. Its retained set consists of the 55 inventory rows routed to it by the programme's destination pass (the named gated and ungated C3/C4 systems, their equilibria and characteristic equations, the Hopf cubic and crossings, the Lyapunov coefficients, the branch-continuation and Floquet evidence, the protective channel and the two-delay identity, the loop-gain family, the stress-test frame with its variant registry, and the registration and reproduction-target obligations) plus 13 bounded-appendix rows from the interval Hopf/fold validation source, stated in Appendix B. The sources of the retained set, with their per-source row counts, are identified in Appendix A. Per-statement provenance keys link every source-derived statement to the research programme's 409-row statement inventory (source location, canonical module, mapping type, evidence status, destination); the complete per-statement inventory is Appendix A.

## 1.3 Claim-status discipline

Every statement below carries a status label from the research programme's hierarchy (the source corpus's own status table, adopted programme-wide):

| Status | Admission rule |
|---|---|
| Axiom/definition | Declares an object, domain, type, or convention; asserts no empirical truth |
| Identity | Follows by construction or direct algebra |
| Theorem | Complete proof under explicit mathematical assumptions |
| Conditional theorem | Complete implication whose hypotheses are not established for every intended application |
| Conjecture | Precise unproved statement with a declared proof gap and disproof route |
| Counterexample/limit | An explicit construction establishing that an implication fails |

Two further evidentiary labels are used for computational content, following the registered model-family source's own four-status discipline (identity/theorem; numerical result; inferred numerical classification; conjecture): a **numerical result** is a computed output tied to a registered equation, parameter set, history class, method, tolerance, and finite domain; an **inferred numerical classification** adds an interpretation (for example Hopf criticality inferred from branch scaling) that has not been established by the corresponding normal-form calculation. Two rules govern this article. **No promotion:** a conditional theorem is never stated as a theorem; conditionality is part of the mathematical content. **No silent transfer:** a status established for one model class does not transfer to extensions, reductions, or applications without a declared map, and thresholds do not transport between registered variants.

## 1.4 Provenance and auditability

All 68 of this paper's inventory rows were verified against their sources in a dated full-read campaign (scientific closure passes over full source reads, 2026-08-27/28); they are stated below at exactly those statuses, with no promotion. Content-level acceptance means the row's existence, kind, proof presence, module, and mapping type were verified against the source; it is not a theorem-status promotion, and the cross-module interface contract remains an open obligation recorded per row. Of the research programme's 409-row statement inventory, the 27 rows that remain open are exactly those of the three conditional-allocation sources — none of them behind this paper. Numerical results carry their evidentiary level under the certification hierarchy of §10 (nominal; re-execution-verified; independently re-executed; certified), stated per claim.

## 1.5 Relationship to the companion papers

This paper is the fourth of five companion papers of the research programme, all in preparation or under separate review. The architecture companion owns the typed canonical architecture; the theorem-atlas companion owns the general delay-certificate families — the small-gain delay-independent stability certificate, the sampled and hybrid RFDE knowledge kernels, and the projectability criterion — whose *named instantiations* are this paper's; where a general family is invoked, the atlas states the canonical form and this paper states the named system. A companion study develops the closed material ledger whose deficit identity supplies the coupling channel examined at the seam of §9: the seam between that companion and this paper is fixed by an interface contract whose exact shared object is the single-resource deficit identity and whose explicit non-reduction boundary is restated there. The sampled-governance companion owns the sampled-governance family and the empirical identification programme. No paper depends on another for a locally load-bearing definition: this paper states its full named retarded equations, phase spaces, histories, and parameters locally, as its Minimal Working Realization of the canonical objects it needs (the retarded-equation framework itself is classical: Hale 1977; Hale and Verduyn Lunel 1993; Diekmann et al. 1995).

## 1.6 Roadmap

The remainder of this article is organized as follows. Section 2 states the named systems in full with their parameterisations and admissible domains: the gated three-state core, its box-invariance and boundedness theorems, the registered model family (M3-U, M3-B, M3-LC, M4-A, MPF), the turnover-corrected four-state working core with its closure theorems and frozen-donor mass status, the protective quota-tracking law and the two-channel interpolation, and the model-registration discipline. Section 3 derives the interior equilibrium and the extinction face, the characteristic quasi-polynomial, and the complete Hopf cubic with its even-pairs algebra, and frames the named systems with the scalar Hayes delay margin and the no-sign-free-delay counterexample. Section 4 develops the mobilising channel: the interval-certified crossing delays and the gate's threshold relocation, the first Lyapunov coefficients and criticality, conditional Hopf persistence under residual feedback, and the two-delay interpolation with the weighted small-gain theorem and the conditional mobilising-weight corollary. Section 5 analyses the protective channel: the no-Hopf theorem under quota tracking, the iso-gain sign flip and the false-reversal hazard, the sampled protective monodromy with its discretisation crossing, and channel-specific pacing. Section 6 states the numerical evidence at its declared certification level — branch continuation and the lower and upper boundaries, the five-regime attractor topology, the registered numerical families, the four-state working core, the sample-and-hold monodromy, and the parameter windows. Section 7 develops the loop-gain family — the general feedback identity, the loop-gain exclusion theorem with the Halanay-type delay-independent certificate, the logistic identification theorem, the saturating-gate negative screen, the exergy-gated suppression conjecture — and the open conjecture register. Section 8 states the stress-test frame: the response-sign hypotheses, the physical mechanism types, the variant registry with its registered obligations, and the thermodynamic tether with its institutional Allee effect. Section 9 fixes the seam to the material-ledger companion, including the exact shared deficit identity and the non-reduction boundary. Section 10 states the four-level certification hierarchy and applies it claim by claim, and Section 11 records provenance, reproducibility, and limits. Appendix A carries the complete statement inventory in two tables; Appendix B states the interval Hopf enclosures and the fold non-certificate. The references and the data-and-code availability statement close the article.

---

# 2. The named systems and their admissible domains

Throughout, $N$ is a renewable stock (material or biomass units), $Z$ a filtered deficit-memory state (stock per time), and $E$ an extraction effort (a dimensionless institutional deployment intensity, not a conserved material or energy stock). The catchability $q$ has units (effort·yr)$^{-1}$; the signal references $\Delta_\mathrm{ref}$, $Z_\mathrm{ref}$ and the offset $\delta$ have stock-per-time units; $\eta$ and $\delta_0$ have time$^{-1}$ and effort-per-time units. These assignments make each equation dimensionally homogeneous without treating effort as physical mass. The delay $\tau$ is a discrete action/deployment delay; the filter timescale $\tau_m$ is an ordinary state relaxation time, not a second delay.

## 2.1 The gated three-state core (DYN-C3-GATED / M3-B)

Let

$$
S(N)=rN\bigl(1-\frac{N}{K}\bigr),\qquad
\operatorname{sp}_k(s)=\frac1k\log(1+e^{ks}),\qquad
\Phi_k(s)=\max\bigl\{0,\ \operatorname{sp}_k(s)-\frac{\log 2}{k}+\delta\bigr\},
$$

where $\Phi_k$ is a shifted, non-negative signal map. The boundary-exact (gated) three-state core is

$$
\begin{aligned}
\dot N &= S(N)-qEN,\\
\dot Z &= \frac{1}{\tau_m}\bigl[\Phi_k(qEN-S(N))-Z\bigr],\\
\dot E &= \bigl(1-\frac{E}{E_{\max}}\bigr)
\biggl[\eta E\biggl(\frac{Z(t-\tau)}{\Delta_\mathrm{ref}}-\frac{E}{E_{\max}}\biggr)
+\delta_0\frac{Z(t-\tau)}{Z_\mathrm{ref}+Z(t-\tau)}\biggr].
\end{aligned}
\tag{M3-B}
$$

The memory input is a smoothed version of the stock-decline rate: on this core the identity $qEN-S(N)=-\dot N$ holds exactly, so $\Phi_k$ filters $-\dot N$ (the deficit identity and its seam role are stated in §9). The multiplicative gate $(1-E/E_{\max})$ is load-bearing — a hard saturation architecture, not a generic effort law: it enforces $E\in[0,E_{\max}]$ by construction. The registered parameterisations are:

| Parameter | Candidate A | Candidate B | Role |
|---|---|---|---|
| $r$ | $0.02$ | $0.02$ | yr$^{-1}$; stock renewal |
| $K$ | $100$ | $100$ | stock units; normalisation |
| $q$ | $0.001$ | $0.001$ | (effort·yr)$^{-1}$ |
| $\eta$ | $0.914$ | $2.756$ | yr$^{-1}$; effort response |
| $E_{\max}$ | $30$ | $26$ | effort units; saturation boundary |
| $\Delta_\mathrm{ref}$ | $1.0$ | $1.0$ | stock yr$^{-1}$; signal scale |
| $\delta_0$ | $0.01$ | $0.01$ | effort yr$^{-1}$; baseline source |
| $\tau_m$ | $5$ | $5$ | yr; filter relaxation |
| $Z_\mathrm{ref}$ | $1.0$ | $1.0$ | stock yr$^{-1}$; signal scale |
| $\delta$ | $\log 2/10$ | $\log 2/10$ | stock yr$^{-1}$; signal offset |
| $k$ | $10$ | $10$ | (stock yr$^{-1}$)$^{-1}$; regularisation |
| $\tau$ | varied | varied | yr; action/deployment delay |

These are mathematical parameterisations and sensitivity anchors, not a joint calibration to a named resource or institution; the effort scale is normalised, $k$ is a regularisation constant, and the institutional coefficients have not been independently identified from a field system. Candidates A and B are two points in the effort-response chart, not rescalings of one class. For the reported pair $\delta=\log(2)/k$ the outer floor cancels algebraically ($\Phi_k(s)=\operatorname{sp}_k(s)>0$ for every finite $s$), so the floor is inactive on every reported periodic orbit; the identity is parameter-specific, and for $\delta\ne\log(2)/k$ floor contact must be checked orbit by orbit.

## 2.2 Admissibility

**Theorem 2.1 (Forward invariance of the M3-B box).** For the history class $\varphi\in C([-\tau,0],\mathbb R^3)$ define

$$
\mathcal D=\{0\le N\le K,\ Z\ge0,\ 0\le E\le E_{\max}\}.
$$

If the initial history lies in $\mathcal D$ — every history value, not only the endpoint — then every classical solution of (M3-B) remains in $\mathcal D$ for as long as it exists. The proof is the five boundary-face tangent-cone calculation (at $N=0$ both renewal and harvest vanish; at $N=K$, $\dot N=-qEK\le0$; at $Z=0$ the floored source is non-negative; at $E=0$ the baseline source is non-negative; at $E=E_{\max}$ the gate vanishes) with the delayed history non-negative on each step, induction over $[n\tau,(n+1)\tau]$ by the method of steps, and the $\tau=0$ ordinary-differential-equation fallback.

**Corollary 2.2 (Boundedness and global continuation).** With $\bar Z=\max\{\sup_{[-\tau,0]}Z,\ \Phi_k(qE_{\max}K)\}$, variation of constants in the $Z$ equation with the monotone bounded input $\nu\le\Phi_k(qE_{\max}K)$ gives $0\le Z(t)\le\bar Z$; all three states remain in a bounded set on which the vector field is locally Lipschitz, and the solution continues for all $t\ge0$. On the invariant extinction face $N=0$ the memory input is $\Phi_k(0)=\delta$, so $Z$ relaxes to $\delta$ and the extinction rest carries the same admissible positive effort root as the interior branch: institutional memory sustains baseline commanded effort against zero realised harvest. Effort is an institutional deployment intensity, not a conserved stock; the core makes no closed-effort-energetics claim, and a materially closed application must add and donor-limit that support explicitly.

The general positivity layer beneath these statements is the cross-mode invariance theorem: **non-negative invariance for ordinary, hybrid, and RFDE modes** — quasipositivity on the history space $C_\tau$ with reset preservation (theorem, proof verified; the canonical statement is the theorem-atlas companion's). Its classification is positive-cone invariance theory (the architecture's positivity principle); the RFDE case is one of its three modes. A companion conditional result covers the hybrid history cone: **conditional hybrid history-cone invariance** — quasipositivity at zero material components, reset positivity, and induction over the locally finite event sequence (conditional theorem, proof verified), with an interval-of-existence limitation and a positivity-only scope (positivity, boundedness, persistence, and viability are distinct properties); relative to the cross-mode theorem it is superseded but preserved as the hybrid-mode statement.

## 2.3 The registered model family

The variants below form a family, not a derivation hierarchy. No invariant set, equilibrium formula, local threshold, periodic branch, or admissibility result transfers between rows without a separate argument; the exact-reduction obligation is the projectability condition $D\pi(y)f(y)=F(\pi(y))$ on the history phase space, posed on the projectability criterion stated in the theorem-atlas companion, and neither that condition nor an approximate-reduction estimate has been established among the registered rows.

| ID | Structure | Signal, memory, effort | Boundary status |
|---|---|---|---|
| M3-U | One logistic stock, ungated effort | $\Phi_k$, leaky memory; effort law without the outer gate | Non-negative states; $E_{\max}$ a self-limitation scale only |
| M3-B | The same ecology | $\Phi_k$, memory; gated law (M3-B) | Primary boundary-exact DDE on $\mathcal D$ |
| M3-LC | One displayed stock, phenomenological two-channel law | M3-U signal, memory, and effort in the reported instance | Non-negative stock through a recruitment floor |
| M4-A | Stock plus dynamic active-support pool | Three-state decline memory; gate declared per instance | Separate state space and active-pool boundary |
| MPF | Living biomass, detritus, residual active material | Signed memory of $-\dot X$; distinct bounded effort law | Distinct support-pool boundary and equilibrium conditions |

**M3-LC (two-channel law).** Write the logistic renewal as a gross birth–mortality decomposition $B(N)=S(N)+\kappa rN$, $M(N)=\kappa rN$ ($\kappa\ge0$), and split the pressure $qEN$ by $\psi\in[0,1]$:

$$
\dot N=\max\{0,\ B(N)-(1-\psi)qEN\}-M(N)-\psi qEN .
\tag{M3-LC}
$$

$C_\mathrm{stock}=\psi qEN$ is a realised removal of standing stock; $C_\mathrm{recruit}=(1-\psi)qEN$ is demographic suppression — a prevented inflow, not a material transfer out of the adult-stock compartment. M3-LC is a phenomenological stock equation, not a closed mass ledger; a physically closed stage model must represent juveniles, adults, prevented recruitment, harvest, mortality, and receiving compartments as distinct primitive fluxes.

**Theorem 2.3 (Local identity, global divergence).** Whenever the recruitment floor in (M3-LC) is inactive, the law reduces exactly to $\dot N=S(N)-qEN$; the floor never binds at the interior equilibrium (the binding condition reduces to $-\psi S(N)>\kappa rN$, which is impossible), so the equilibrium, the Jacobian, the characteristic equation, and both Hopf points are independent of $\psi$ and $\kappa$. Local equality does not imply excursion equality: the floor truncates recruitment on large excursions, and the two channels diverge there (§6.2).

**M4-A (active-pool extension).** Replace logistic renewal by

$$
R(N,A)=rN\bigl(1-\frac NK\bigr)\frac{A}{A+A_0},\qquad
\dot N=R(N,A)-qEN,\qquad
\dot A=-B(N,A)+\omega_A(A^\mathrm{eq}-A),
$$

with a fully declared donor-limited gross draw $B$. The relaxation term makes this a reduced open-pool model unless its donor/receiver reservoir is included explicitly; it is not a closed material ledger and not a proved Tikhonov reduction of the typed primitive-flux model. Freezing $A$ is not a justified fast-variable elimination at the baseline $\omega_A=10^{-3}$ yr$^{-1}$.

**MPF (primitive-flux core).** With living biomass $X$, detritus $U$, active material $A=\mathcal M-X-U$, primitive fluxes $g(X,A)=\mu XA/(K_A+A)$, $m(X)=dX+cX^2$, $h(X,E)=qEX$, and a signed memory $\dot Z=((-\dot X)-Z)/\tau_m$ with the bounded effort law

$$
\dot E=\bigl(1-\frac{E}{E_{\max}}\bigr)\bigl[\eta E\frac{Z(t-\tau)}{\Delta_\mathrm{ref}}+\delta_0-\eta\frac{E^2}{E_{\max}}\bigr],
\tag{MPF-E}
$$

the core has a signed zero-equilibrium memory ($Z^*=0$, so the baseline is a true constant), detritus, and a different effort equilibrium; it is not M3-B. Its active-material admissibility obligation is discharged by a boundary theorem: on the boundary $X+U=\mathcal M$ the active pool is $A=0$ and $g(X,0)=0$, so

$$
\frac{d}{dt}(X+U)=-qEX-\gamma_UU\le0,
$$

which, with $g(0,A)=0$, $m(0)=0$, and the donor-limited flux assumptions, proves forward invariance of the MPF simplex $\{X\ge0,\ U\ge0,\ X+U\le\mathcal M\}$ for the ecological subsystem under admissible effort — a boundary theorem independent of the numerical regime classifications. The support-saturated logistic stock-equation identity of this core ($A/(K_A+A)\to1$ as $K_A\to0$ with $r=\mu-d$, $K=(\mu-d)/c$) is ledger content and is owned by the material-ledger companion; it is an ecological stock-equation identity, not a full-core reduction or a transfer principle for Hopf or fold thresholds, and it does not transform the MPF memory or effort law into (M3-B)'s.

## 2.4 The turnover-corrected four-state working core (DYN-C4-WORKING)

The working four-state core restores the active abiotic pool as a state:

$$
\begin{aligned}
\dot N &= R(N,A)-qEN,\\
\dot A &= -B(N,A)+\omega_A\bigl(A^{\mathrm{eq},W}-A\bigr),
\end{aligned}\qquad A^{\mathrm{eq},W}=A^{\mathrm{eq,intrinsic}}+\frac{\kappa_AK}{\omega_A},
\tag{C4-W}
$$

with the $Z$ and $E$ equations of (M3-B) unchanged except that $S(N)$ is replaced by $R(N,A)$; at the baseline $\omega_A=10^{-3}$ yr$^{-1}$, $\kappa_A=0.05$ yr$^{-1}$, $A_0=0.01K$, $A^{\mathrm{eq,intrinsic}}=0.5K$, so $A^{\mathrm{eq},W}=5050$. Two closure theorems fix its status (proofs verified):

**Theorem 2.4 (Working-core projection).** In the ideal large-reservoir limit $\sigma_\mathrm{geo}=1$, on the specialised system with the dynamic derived target, $\omega_A(A^\mathrm{eq}-A)+\gamma_UU=\omega_A(A^{\mathrm{eq,intrinsic}}-A)+\kappa_AK$ identically, and $(N,A,Z,E)$ satisfies (C4-W) exactly, with detritus $U$ a driven auxiliary ($\dot U=T-\gamma_UU$, $T=\kappa_ANA/(A+A_0)$) that does not feed back. For finite $A^\mathrm{geo}$ the working-core vector field is perturbed by $O(1-\sigma_\mathrm{geo})$ and $U$ feeds back through $\gamma_UU(1-\sigma_\mathrm{geo})$; the reported four-state thresholds are $\sigma_\mathrm{geo}=1$ properties.

**Theorem 2.5 (Detritus slaving under a fixed intrinsic target).** Holding $A^\mathrm{eq}=A^{\mathrm{eq,intrinsic}}$ fixed with $\gamma_U=\varepsilon_U^{-1}\gamma_{U,0}$, after a transient of length $O(\varepsilon_U|\log\varepsilon_U|)$, $U=U^*(N,A)+O(\varepsilon_U)$ with $U^*=\gamma_U^{-1}\kappa_ANA/(A+A_0)$, and $(N,A,Z,E)$ is $O(\varepsilon_U)$-close on compact intervals to the quasi-steady (QSS) four-state core. At Candidate A the QSS core has a positive low-$A$ equilibrium $(N^*,A^*)\approx(23.85,0.159)$ and no high-$A$ near-logistic exploited equilibrium (the high-stock branch gives $A^*\approx-137$, inadmissible).

The QSS core is a distinct singular-limit object: it is a valid limit but is **not dynamically connected** to the high-$A$ working equilibrium used for the reported thresholds, and the two objects are never merged. At the baseline $\gamma_U/r=10$, so $\varepsilon_U$ is not small: the slaving theorem is a finite-time estimate that does not control global periodic orbits.

**Theorem 2.6 (Frozen-active-pool finite-time approximation).** If on $[0,T]$ the four-state solution has $A(t)\ge A_{\min}>0$ and $|\dot A|\le V_A$, and $(N^{(3)},Z^{(3)},E^{(3)})$ solves (M3-B), then

$$
\sup_{t\in[0,T]}\bigl(|N-N^{(3)}|+|Z-Z^{(3)}|+|E-E^{(3)}|\bigr)\le C_T\bigl(\frac{A_0}{A_{\min}}+V_AT\bigr).
$$

This is an inner approximation on $[0,T]$, not a Tikhonov reduction. At the baseline $1/\omega_A\sim10^3$ yr while the four-state oscillation periods are $250$–$390$ yr, so the theorem justifies the three-state core for local, near-equilibrium questions on institutional timescales — in particular the location of $\tau_-$, whose $3.2\%$ shift under restoration of $A$ lies inside the bound — but not the large-amplitude cycle or its period.

**Mass status (open projection).** The working core is an open projection and is declared as such: omitted turnover is routed to a diagnostic detritus/inert sink; imposed recharge corresponds to geological draw; the reduced $(N,A,Z,E)$ trajectory is not mass-closed by itself; its mass discrepancy is reconstructible from the omitted donor/turnover flows; and its global periodic results are model-version-specific and do not transfer to the closed primitive ledger (§9). The working equilibrium is a frozen-donor quasi-equilibrium sustained by geological support of order $\omega_A(A^{\mathrm{eq},W}-A^*)\approx4.652$ stock units per year, not a rest point of a closed $A^\mathrm{geo}$ equation; the cumulative donor change at that constant flux is $\varepsilon_G(T)=4.652\,T/A^\mathrm{geo}$, which is $1.2\%$ on a century horizon at the lower geological ratio $A^\mathrm{geo}/A^*=10^2$ and $0.12\%$ at $10^3$.

## 2.5 The protective two-channel system

A protective institution is the law

$$
\dot E=\bigl(1-\frac{E}{E_{\max}}\bigr)\,\eta_p\bigl(E_\mathrm{cap}(Z(t-\tau_p))-E\bigr),
\tag{P}
$$

where $E_\mathrm{cap}$ is $C^2$, positive, and strictly decreasing, with the calibration $E_\mathrm{cap}(Z)=E_0Z_\mathrm{ref}/(Z_\mathrm{ref}+Z)$ and $E_0=E^*_A(Z_\mathrm{ref}+\delta)/Z_\mathrm{ref}$ (model definition). The calibration places the unique interior rest of (P) on the stock–memory block of the companion core at the Candidate A point $(N^*,Z^*,E^*)=(89.55188,\,\delta,\,2.08962)$, so the stock–memory block is identical to (M3-B)'s and only the effort law changes. At that rest $E_\mathrm{cap}(\delta)=E^*$ and

$$
C_E=-\bigl(1-\frac{E^*}{E_{\max}}\bigr)\eta_p,\qquad
C_Z=\bigl(1-\frac{E^*}{E_{\max}}\bigr)\eta_pE_\mathrm{cap}'(\delta),
$$

which at $\eta_p=\eta_A=0.914$ give $C_E=-0.850336$ and $C_Z=-1.661702$ (calibration arithmetic, source-stated numerical status) — both signs those of a restoring quota, not of scarcity mobilisation; the mobilising counterpart at the same point has $C_Z=+1.785$. The channel-separation object is exactly this sign discipline.

The two-channel interpolation replaces the effort law by

$$
\dot E=\bigl(1-\frac{E}{E_{\max}}\bigr)\bigl[\chi_mF_m\bigl(E,Z(t-\tau_m)\bigr)+\chi_p\eta_p\bigl(E_\mathrm{cap}(Z(t-\tau_p))-E\bigr)\bigr],
\tag{2ch}
$$

with $\chi_m,\chi_p\ge0$; the pure mobilising channel is $(\chi_m,\chi_p)=(1,0)$, pure protection $(0,1)$.

## 2.6 Model registration and the delayed-recruitment obligation

Numerical propositions require a registered model that determines the vector field and the characteristic equation. For stage-structured (delayed-recruitment) extensions the registration requirement is explicit (the experimental delayed-recruitment lineage being Costantino et al. 1995): reproduction requires a companion registration stating the complete delayed-recruitment equations and state dimension, each class-specific parameter vector, the effort gate, $\Phi$, the initial history, the flow/update order, and the numerical and tail-classification conventions (registration requirement). The class-labelled delayed-recruitment values in the source record (anchovy-, sprat-, cod-, and slow-stock classes) are exploratory computational summaries pending that complete stage registration and are not attributed to the registered three-state sampled system whose complete Candidate A/B vectors live in the research programme's model registry; their response-region outputs are the sampled-governance companion's content. The equations-versus-outputs split is the same seam discipline as the ledger seam of §9.

---

# 3. Equilibria and characteristic equations

## 3.1 The interior equilibrium and the extinction face (verified model algebra)

At any interior equilibrium $qE^*N^*=S(N^*)$, the signal argument vanishes, the floor is inactive, and

$$
Z^*=\Phi_k(0)=\delta,
$$

independent of $\tau_m$, $k$, and $(N^*,E^*)$. Substituting into $\dot E=0$ (away from $E=E_{\max}$) produces

$$
-\frac{\eta}{E_{\max}}(E^*)^2+\eta\frac{\delta}{\Delta_\mathrm{ref}}E^*+\delta_0\frac{\delta}{Z_\mathrm{ref}+\delta}=0,
$$

whose constant term is positive and quadratic coefficient negative, so there is exactly one positive root; admissibility requires $0<E^*<\min\{E_{\max},r/q\}$, and then $N^*=K(1-qE^*/r)$, positive iff $qE^*<r$. The equilibrium is independent of $\tau$ and $k$, which does not make its stability delay-independent. At Candidate A, $N^*\approx89.55$, $E^*\approx2.090$, $Z^*=\delta\approx0.0693$.

On the extinction face $N=0$ the same zero raw signal gives $Z=\delta$, and the gated law has both the interior-effort extinction rest $(0,\delta,E^*)$ (when the interior root is admissible) and the boundary rest $(0,\delta,E_{\max})$ created by the multiplicative gate. The stock-direction eigenvalue at either branch is $r-qE$; the interior positive-stock branch exchanges stock-direction stability with the interior-effort extinction branch at the transcritical point $r=qE^*$, while the $E=E_{\max}$ boundary branch is classified separately and is not part of that exchange. The survival condition $r>qE^*$ is identical to $N^*>0$; interior and extinction branches are not simultaneously stable.

## 3.2 The characteristic quasi-polynomial (proposition, proof verified)

With $x=N-N^*$, $z=Z-Z^*$, $e=E-E^*$, $\operatorname{sp}_k'(0)=1/2$, and the floor inactive at $\delta>0$, the linearisation is

$$
\dot x=A_Nx+A_Ee,\qquad
\dot z=B_Nx+B_Ee-\frac{1}{\tau_m}z,\qquad
\dot e=C_Ee+C_Zz(t-\tau),
$$

with

$$
\begin{aligned}
A_N&=r\bigl(1-\frac{2N^*}{K}\bigr)-qE^*,& A_E&=-qN^*,\\
B_N&=\frac{qE^*-S'(N^*)}{2\tau_m},& B_E&=\frac{qN^*}{2\tau_m},\\
C_E&=\bigl(1-\frac{E^*}{E_{\max}}\bigr)\eta\bigl(\frac{\delta}{\Delta_\mathrm{ref}}-\frac{2E^*}{E_{\max}}\bigr),\qquad
C_Z&=\bigl(1-\frac{E^*}{E_{\max}}\bigr)\bigl[\frac{\eta E^*}{\Delta_\mathrm{ref}}+\frac{\delta_0Z_\mathrm{ref}}{(Z_\mathrm{ref}+\delta)^2}\bigr].
\end{aligned}
$$

The gate factors $(1-E^*/E_{\max})$ distinguish the gated from the ungated variant and are the algebraic source of threshold relocation between the two. Substitution of the modal ansatz and expansion of the $3\times3$ characteristic determinant along the first row gives

$$
P(\lambda)-C_ZL(\lambda)e^{-\lambda\tau}=0,\qquad
P(\lambda)=(\lambda-A_N)(\lambda+d)(\lambda-C_E),\quad
L(\lambda)=B_E(\lambda-A_N)+A_EB_N,
$$

with $d=1/\tau_m$. This factorisation and the equilibrium of §3.1 form one local-bifurcation analysis: the linear coefficients are evaluated at exactly the interior equilibrium above.

## 3.3 The complete Hopf cubic (theorem, proof verified; theorem + interval certificates)

**Theorem 3.1 (Cubic modulus condition and phase branches).** $\lambda=i\omega$, $\omega>0$, is a characteristic root iff $x=\omega^2$ is a positive root of

$$
H(x)=(x+A_N^2)(x+d^2)(x+C_E^2)-C_Z^2\bigl[B_E^2x+(A_EB_N-A_NB_E)^2\bigr]=0,
$$

and $\tau=\bigl(-\arg\{P(i\omega)/(C_ZL(i\omega))\}+2\pi k\bigr)/\omega>0$, $k\in\mathbb Z$. A cubic has at most three positive roots, so there are at most three Hopf-frequency families; higher branches recur within a family as $\tau_{n,0}+2\pi k/\omega_n$ and are not additional frequencies.

The proof squares the moduli of the characteristic identity and conversely reads the unit-modulus ratio $P(i\omega)/(C_ZL(i\omega))$ for the phase. Candidates qualify as Hopf crossings only after simplicity and transversality are verified separately; the cubic determines neither criticality nor global folds.

**Even pairs.** At the interior equilibrium the filter identities $B_N=-A_N/(2\tau_m)$ and $B_E=-A_E/(2\tau_m)$ (the deficit signal is $qEN-S(N)=-A_Nx-A_Ee$ and $\operatorname{sp}_k'(0)=1/2$) make the cross term vanish identically, $A_EB_N-A_NB_E\equiv0$, so

$$
H(x)=(x+A_N^2)(x+d^2)(x+C_E^2)-C_Z^2B_E^2x .
$$

Since $H(0)=A_N^2d^2C_E^2>0$ and $H(x)\to+\infty$, the positive roots occur in even number (zero or two), never one or three — the algebraic reason an $\eta$-sweep over $[0.5,3.0]$ finds zero or two positive roots throughout, and the reason the two-crossing structure is generic on this architecture.

For both Candidate A and Candidate B the cubic has exactly two positive roots on both the gated and the ungated variant; the completed local spectrum (Theorem 3.1 with the interval-Newton certificates) is stated in §4.1.

## 3.4 The scalar archetype and the sign discipline

Two general statements frame the named systems' delay mathematics.

**Theorem 3.2 (Scalar delay margin).** For $\dot x=-ax-Bx(t-\tau)$ with $a>0$, $B\ge0$: if $B\le a$ the zero equilibrium is stable for all $\tau\ge0$; if $B>a$ it is stable for $\tau<\tau_\mathrm{crit}=\arccos(-a/B)/\sqrt{B^2-a^2}$ and unstable beyond, with **no restabilisation** as $\tau$ grows (the crossing is destabilising, $\operatorname{Re}(ds/d\tau)>0$ at $s=i\omega$; Hayes). This is the scalar mechanism by which loop delay destroys stability that undelayed feedback sustains.

**Proposition 3.3 (No sign-free delay conclusion).** The scalar systems $\dot x=-ax-bx(t-\tau)$ and $\dot x=-ax+bx(t-\tau)$ ($a,b>0$) have different feedback signs and different stability properties; no delay conclusion is sign-free. This is a valid non-universality statement (the two sign-contrast systems are named in the statement; explicit parameter examples are desirable and not supplied); it is non-universality only — not an analysis of any particular sampled institution, distributed delay, non-minimum-phase plant, or ecological system.

The named systems of this paper instantiate the two signs: the mobilising law of (M3-B) carries $C_Z>0$, the protective law (P) carries $C_Z<0$, and §§4–5 show that the local mathematics separates accordingly. The general delay-certificate families — the sampled RFDE finite-clopen knowledge kernel and the review-synchronised hybrid RFDE knowledge kernel — are conditional theorems of the theorem-atlas companion (compact single-delay history class; review-clock hybrid RFDE with continuous phase-space reset; each carrying substantive compactness and held-solution-map hypotheses) and are stated with the sampled operators in §6.4 (conditional theorems, source-declared status).

---

# 4. The mobilising channel: crossings, criticality, and the two-channel interpolation

## 4.1 Local crossings and interval-certified delays

The complete cubic search (Theorem 3.1) with separately verified simplicity and transversality, independently checked by direct root tracking of the quasi-polynomial, gives the crossing pairs:

| System | Candidate A $\tau_-$ / $\tau_+$ (yr) | Candidate B $\tau_-$ / $\tau_+$ (yr) |
|---|---|---|
| M3-U (ungated C3) | $6.8814$ / $132.3749$ | $6.2136$ / $76.2906$ |
| M3-B (gated C3) | $3.67$ / $150.36$ | $5.5128$ / $80.4245$ |
| Gated C3, interval-certified | $\tau_-\in[3.6661490142739,\,3.6661490142743]$, $\tau_+\in[150.3584773101408,\,150.3584773101421]$ | gated: $\tau_-\in[5.5128407314433,\,5.5128407314436]$, $\tau_+\in[80.4245267142270,\,80.4245267142276]$; ungated: $\tau_-\in[6.2135987340180,\,6.2135987340183]$, $\tau_+\in[76.2906356879512,\,76.2906356879518]$ |

The interval certificates are interval-Newton enclosures of the simple positive roots of $H$ in $x=\omega^2$ (width $\le4\times10^{-17}$ in $x$) followed by branch-safe interval evaluation of the phase relation; the delay is the interval evaluation of the phase formula at a certified positive root of $H$, not a root of the argument formula. The committed interval pipeline reproduces the displayed Candidate A intervals exactly, with outward rounding, interval transcendentals, simple-root and transversality sign checks (the lower crossing stabilising, $\mathrm{d\,Re\,\lambda}/\mathrm{d}\tau<0$; the upper crossing destabilising), and outputs identical on re-execution (§10, Appendix B.1). This certifies the local spectrum of $H$; it is not an interval certificate of any global fold.

The undelayed gated mobilisation law is already unstable ($\operatorname{Re}\lambda>0$ at $\tau=0$): institutional delay acts as a phase filter that opens the phase-stabilised window $(\tau_-,\tau_+)$ and closes it again at $\tau_+$. Delay-amplified instability refers to the upper crossing and the bistable windows, not to delay creating the short-delay instability. Enforcing the effort boundary relocates the local thresholds by approximately $47\%$ (lower) and $14\%$ (upper) at Candidate A without changing the equilibrium — thresholds do not transport between the gated and ungated variants, and the gate's threshold relocation is itself a registered comparison, not a calibration.

## 4.2 Lyapunov coefficients and criticality (numerical results, source-stated status)

The first Lyapunov coefficient at a Hopf of the gated three-state core is the Hassard–Faria–Magalhães cubic evaluated from the exact second and third derivatives of the vector field at equilibrium, under unit Hermitian normalisation of the right eigenvector and $q^*\Delta'(i\omega)p=1$:

$$
\ell_1(\tau_-^\mathrm{A})=+5.75\times10^{-5},\qquad
\ell_1(\tau_+^\mathrm{A})=+3.55\times10^{-4},
$$

both subcritical at gated Candidate A; the ungated Candidate B lower crossing is supercritical, $\ell_1(\tau_-^\mathrm{B})=-9.84\times10^{-5}$ (hence no lower fold for that class), with $\ell_1(\tau_+^\mathrm{B})=+2.19\times10^{-3}$. The subcritical small branch satisfies $\|N-N^*\|\sim C\sqrt{\tau-\tau_-}$ (slope $29.8$ in amplitude-squared, $R^2=0.994$; the collocated orbit at $\tau=3.700$ has residual $\sim10^{-7}$ and escapes onto the large cycle by roundoff alone).

Two status distinctions are load-bearing. First, within the registered model family the criticality statements obtained from branch scaling — amplitude exponent $0.47$ and surrogate cubic coefficient $\approx3.9\times10^{-6}$ near the lower gated crossing — are inferred numerical classifications, not first Lyapunov coefficients from a centre-manifold calculation; the $\ell_1$ values above are the computed coefficients for the gated core. Second, criticality is not invariant under the regularisation: the first Lyapunov coefficient contains $\operatorname{sp}_k''(0)=k/4$, so the reported $\ell_1(\tau_\pm)$ are at $k=10$, Hopf points are invariant under $k\in\{5,10,20,40\}$ at fixed $\delta$, and a sign change in $\ell_1$ under that sweep would rearrange the lower window. $k$-independence of equilibria and linearisations is a local statement only; fold locations depend on $k$, and no $k$-uniform topology is claimed.

## 4.3 Hopf persistence under residual feedback (conditional)

The relation of the named cores to the five-state specialised system rests on a slow-fast statement that is a **conjecture**:

**Conjecture 4.1 (Finite-time reduction to the five-state core).** Under a $C^1$ macroeconomic feedback of size $\varepsilon$ and the scale/Hurwitz/Lipschitz hypotheses, the specialised solution tracks the five-state core with $\sup_{[0,T]}\|\mathbf x^\varepsilon-\mathbf x^0\|\le C(\varepsilon+\omega_AT)$ and slow-manifold tracking $\|\mathbf y^\varepsilon-\mathbf h(\mathbf x^\varepsilon)\|\le C(\varepsilon+\omega_AT)+Ce^{-\gamma_{\mathbf y}t/\varepsilon}$. The declared gap: the classical Tikhonov and Fenichel theorems are ordinary-differential-equation statements, and the infinite-dimensional Fenichel-type theorems for slow-fast evolution systems apply only subject to a spectral gap and compactness of the memory kernel that are not verified here; the Hurwitz hypothesis on the fast Jacobian is supported by a finite-difference sweep on the literature-anchored class and is not proved on the whole domain. The geological-freezing budget is the cumulative donor change $\varepsilon_G(T)$, not $\omega_AT$ alone.

**Theorem 4.2 (Local Hopf persistence, conditional).** Assume Conjecture 4.1 and the working-core projection (Theorem 2.4); assume the working four-state (respectively three-state) characteristic equation has a simple pair $\pm i\omega$ at $\tau=\tau_\star\in\{\tau_-,\tau_+\}$ with $\mathrm{d\,Re\,\lambda}/\mathrm{d}\tau\ne0$ and no other imaginary eigenvalues; assume the fast Jacobian remains uniformly Hurwitz at the joint equilibrium and that non-feedback mass compartments stay outside the delay loop. Then under the strict specialisation the core spectrum is a literal factor of the full characteristic function and the Hopf points persist exactly; under residual macroeconomic feedback of size $\varepsilon$ the specialised system has a Hopf point $\tau_\star(\varepsilon)=\tau_\star+O(\varepsilon)$ in the ideal large-reservoir limit (add $O(1-\sigma_\mathrm{geo})$ for the finite reservoir), by the Schur-complement/Rouché argument.

The conditionality is mathematical content: the persistence statement is conditional on the conjecture's unverified spectral hypotheses, and the global fold events of §6 lie explicitly outside its hypotheses. The macro-reduction conjecture itself is owned by the theorem-atlas companion; this paper states it only as the hypothesis it inherits.

## 4.4 The two-delay interpolation and the conditional mobilising-weight corollary

Linearising (2ch) at an interior rest where both brackets vanish separately (the Candidate A point, under the calibration of §2.5) gives $\dot e=C_Ee+C_mz(t-\tau_m)+C_pz(t-\tau_p)$ with $C_m=\chi_mC_Z^\mathrm{mob}$, $C_p=\chi_pC_Z^\mathrm{prot}$, and $C_E$ the sum of the two gate-adjusted $E$-derivatives.

**Theorem 4.3 (Two-delay characteristic identity).** The characteristic function of the stock–memory block coupled to the interpolated effort law is

$$
P(\lambda)-L(\lambda)\bigl(C_me^{-\lambda\tau_m}+C_pe^{-\lambda\tau_p}\bigr)=0,
$$

with $P$ and $L$ the polynomials of §3.2; the proof expands the variational system's characteristic determinant along the third row.

**Theorem 4.4 (Weighted small gain).** If

$$
\sup_{\omega>0}\frac{(|C_m|+|C_p|)\,|L(i\omega)|}{|(i\omega-A_N)(i\omega+d)(i\omega-C_E)|}<1,
$$

then the two-delay characteristic equation has no imaginary-axis root for any $\tau_m,\tau_p\ge0$. The proof is the triangle inequality $|P(i\omega)|\le|L(i\omega)|(|C_m|+|C_p|)$ using $|e^{-i\omega\tau}|=1$. The theorem holds together with the zero-root and characteristic-continuity requirements carried by the delay-independent stability argument of §5.2.

**Corollary 4.5 (Mobilising weight, conditional).** At Candidate A the pure mobilising loop gain exceeds $1$ and the pure protective loop gain is $0.080$. Assume (i) the common equilibrium and all linear coefficients depend continuously on $\chi_m$; (ii) the characteristic denominator remains nonzero on the imaginary axis; (iii) the protective endpoint has a strict gain margin. Then there exists $\chi_m^*\in(0,1)$ such that every interpolation with $\chi_m<\chi_m^*$ and $\chi_p=1-\chi_m$ satisfies Theorem 4.4. A Hopf of the interpolated system therefore requires a sufficiently large mobilising weight; it cannot be produced by decreasing $\tau_p$ alone.

The corollary holds exactly under the listed hypotheses; the interpolation family is not otherwise established to preserve a common equilibrium or a nonvanishing denominator, and no promotion of the corollary beyond them is made.

---

# 5. The protective channel

## 5.1 The quota-tracking law and its calibration

The protective law (P) with its calibration is stated in §2.5. The interpretation discipline at the seam is that the effort variable may be an endogenous industry response, a legal quota-utilisation state, or an actual institutional control, and these interpretations are not interchangeable; the quota-tracking law is an institutional control law.

## 5.2 The no-Hopf theorem

**Theorem 5.1 (No delay-induced Hopf under quota tracking).** At the Candidate A stock–memory linearisation and the protective gains of §2.5, the monic cubic $H(x)=x^3+c_2x^2+c_1x+c_0$ has

$$
c_2=A_N^2+d^2+C_E^2=0.76339,\qquad c_1=0.028946,\qquad c_0=9.278\times10^{-6},
$$

all positive, with $c_2c_1-c_0=0.02209>0$; by Descartes' rule of signs $H$ has no positive real root, and the Routh–Hurwitz criterion confirms all roots of $H$ have negative real parts. Consequently $|P(i\omega)|=|C_Z||L(i\omega)|$ has no solution $\omega>0$. Equivalently, the loop gain

$$
\Gamma(\omega)=\bigl|\frac{C_ZL(i\omega)}{(i\omega-A_N)(i\omega+d)(i\omega-C_E)}\bigr|
$$

is continuous, vanishes at $0$ and $\infty$, and attains its maximum $0.08011<1$ at $\omega\approx0.0589$ (a numerically located maximum). The loop-gain exclusion argument (§7.2) then excludes every nonzero imaginary characteristic root for all $\tau_p\ge0$. In addition the undelayed characteristic system is Hurwitz and the zero-root condition is delay-independent with $P(0)\ne0$ because $L(0)=0$; by continuous dependence of retarded characteristic roots, exponential stability persists for every $\tau_p\ge0$.

The channel-separation reading is the theorem's interpretation: destabilisation by short delay is confined to the mobilising summand. The undelayed Jacobian is Hurwitz ($C_E=-0.850$), so the protective channel has no small periodic branch born from the equilibrium at any delay.

## 5.3 The iso-gain sign flip

**Proposition 5.2 (Iso-gain sign flip).** Replacing $C_Z$ by $-C_Z$ in the gated Candidate A linearisation, leaving every other coefficient unchanged, leaves $H$ identical (it depends on $C_Z$ only through $C_Z^2$), leaves the frequencies identical, and shifts each family's fundamental delay by $\pi/\omega$ on the branch that keeps it fundamental: the lower family ($\omega_1\approx0.02518$) moves up, $3.666+\pi/\omega_1=128.374$ yr, and the upper family ($\omega_2\approx0.03944$) moves down, $150.358-\pi/\omega_2=70.697$ yr, both remaining local Hopfs. (The subscripts retain their original-family meaning — $\tau_-$ is the lower family's shifted delay, $\tau_+$ the upper family's — so on the shifted axis the order is reversed: $\tau_+<\tau_-<\tau_+^\mathrm{unshifted}$.) The reversed-gain linearisation has loop gain $1.016>1$ and retains the factor $\eta E^*/\Delta_\mathrm{ref}$: it is **not** the quota law, whose genuine form changes the modulus as well as the sign.

This is the false-reversal identification hazard: a pure sign flip is not a protective institution, and attributing the reversed-gain crossings to a quota tracker would confuse two different effort laws.

## 5.4 Sampled protection and the discretisation crossing

**Proposition 5.3 (Protective sample-and-hold monodromy).** Replacing the protective delayed feedback by sample-and-hold of period $T_r$ with one explicit Euler review step (the sample-and-hold review operator of computer-controlled systems: Åström and Wittenmark 1997), the monodromy is

$$
M_p(T_r)=\begin{pmatrix}1&0&0\\0&1&0\\0&T_rC_Z&1+T_rC_E\end{pmatrix}\exp(A_\mathrm{hold}T_r),
\qquad
A_\mathrm{hold}=\begin{pmatrix}A_N&0&A_E\\B_N&-d&B_E\\0&0&0\end{pmatrix}.
$$

At the protective gains, $\rho(M_p(1))=0.9838<1$: annual review of the quota-tracking channel is linearly stable at Candidate A. On the grid $T_r\in[0.2,20]$ the spectral radius is strictly below one on $[0.2,2.306)$ and strictly above one on $(2.306,20]$, so the Euler hold map crosses $\rho=1$ at $T_r=2.306$. That crossing is a discretisation of the explicit Euler factor $1+T_rC_E$ with $C_E=-0.850$ — it is not a Hopf point of the protective delay equation, whose continuous spectrum is excluded by Theorem 5.1.

The finding is the mathematical statement: the $T_r=2.306$ crossing belongs to the discretisation. The sampled numerics are accepted at source-stated numerical status; the publication-artifact documentation action remains open (§10). The operator-specific scope is recorded: the mobilising hold map is unstable at $T_r=1$ because the undelayed mobilising Jacobian is already unstable, and the protective map does not inherit that instability.

## 5.5 Channel-specific pacing

**Theorem 5.4 (Channel-specific pacing).** For the mobilising bracket the equilibrium is linearly unstable for $0<\tau<\tau_-$; for the protective law at Candidate A it is linearly stable for every $\tau_p\ge0$; for the two-channel system any delay-induced instability lies in a region of $(\tau_m,\chi_m)$ and is independent of $\tau_p$ wherever the weighted small-gain theorem applies. The proof cites Theorem 5.1 and Corollary 4.5; the pacing synthesis inherits the corollary's interpolation hypotheses wherever its interpolation clause applies.

The policy-scope reading, instantiated: faster protective governance is not the hazard — the mobilising sign is.

---

# 6. Numerical evidence and its certification level

All results in this section are numerical results at their declared status: computed outputs tied to registered equations, parameter sets, history classes, methods, tolerances, and finite domains, with basins restricted to the histories actually tested. The fold-status discipline governs every global statement: the events below are numerical continuation, multiplier, basin, and turning-region results; no Moore–Spence, Krawczyk, or nondegeneracy certificate and no continuous-delay fold proof is claimed (Appendix B.3; rigorous saddle-node-of-periodic-orbit results for DDEs exist for specific classes — Beretka and Vas 2020 — but none is claimed for the events below).

## 6.1 Branch continuation and the lower boundary of the gated C3 core

Hopf points are located by root tracking of the characteristic equation and independently by the cubic; folds by Keller pseudo-arclength continuation of the periodic orbit with $1.5$–$5\times10^6$ yr persistence tests per step and far-from-equilibrium cross-checks (collocation-continuation numerics in the DDE-bifurcation tradition: Engelborghs, Luzyanina, and Roose 2002; the bifurcation-theoretic background is Guckenheimer and Holmes 1983 and Kuznetsov 2004). Fixed-initial-condition bisection mislocates folds by more than $20$ yr under the critical slowing down near each Hopf (linear rates $10^{-4}$–$10^{-5}$ yr$^{-1}$) and is not used.

For the effort-bounded three-state core at Candidate A the lower bistable boundary is the disappearance of the stable large cycle in $\tau\in[5.574,5.576]$, with the evidence branch-resolved. Long-horizon simulation shows the basin collapse between $\tau=5.574$ and $5.576$: beyond that interval no tested far-from-equilibrium history is captured by the large cycle. Adaptive-mesh collocation with variational Floquet tracking, on the other hand, resolves the dominant multiplier of the collocated large-cycle branch as a single real eigenvalue — imaginary part identically zero at every measured point — rising monotonically from $0.240$ at $\tau=4.0$ to $0.964$ at $\tau=5.5815$ with orbit residual $\sim10^{-12}$: the orbit remains a converged fixed point of the collocation map through $\tau=5.5815$, past the basin-collapse interval, with its multiplier still below $+1$. The $+1$-crossing signature is exhibited directly on the small unstable branch (below); for the large branch the exact crossing point and the $0.002$ yr gap between basin collapse and multiplier crossing remain to be pinned, so the saddle-node-of-periodic-orbits classification of this lower boundary is provisional — the alternative reading is a crisis-like loss of the attracting cycle's basin while the branch persists — and no Neimark–Sacker or torus event is involved in either reading (the multiplier is real throughout). The small unstable branch born at the subcritical Hopf $\tau_-=3.666$ undergoes a continuation-supported fold at $\tau\approx5.587$ (real multiplier $1.0514$ at $\tau=5.584$ to $0.99898$ at $\tau=5.587$; Fourier collocation succeeds through $\tau=5.58667$ with residual $5\times10^{-14}$, amplitude $21.80$, period $313.76$ yr, and fails at $\tau=5.590$ under the stated budget). The two families do not meet (amplitudes $\approx25$ and $\approx21.7$; periods $\approx322.9$ and $\approx314.3$ yr), so the lower boundary is a pair of nearby folds of two distinct periodic-orbit families and the $\sqrt{\tau-\tau_\mathrm{SNPO}}$ collision scaling of a single saddle-node does not apply. At the upper boundary, persistence bisection gives $\tau\in[148.125,148.438]$ yr, summarised as $148.3$ yr, with the exact fold type and branch connection undetermined; collocation pins two distinct families through that value — the Hopf small branch (residual $\sim10^{-13}$ on $\tau\in[130,150.30]$, amplitude $0.11$–$1.87$) and an interior large family (residual $\sim10^{-13}$ on $\tau\in[147.5,160]$, amplitude $15.9$–$19.5$) — which remain distinct there, with a third family at $E\ge E_{\max}$ collocating down to $\tau\approx144.5$. On the large cycle at $\tau=5.55$ the filter floor never binds, $E\le9.2\ll E_{\max}$, and $N\ge68.7$: the termination is not a gate singularity, not a graze of $N=0$, and not a homoclinic connection (the period is $324$ yr and decreasing).

The attractor sequence is the five-regime topology: (i) $0<\tau<\tau_-$, equilibrium unstable with a single large-amplitude cycle the attractor; (ii) $\tau_-<\tau<\tau_\mathrm{term,L}$, stable focus coexisting with the large cycle (lower bistable window $\approx0.5$–$2$ yr wide); (iii) $\tau_\mathrm{term,L}<\tau<\tau_\mathrm{fold,R}$, monostable settling; (iv) $\tau_\mathrm{fold,R}<\tau<\tau_+$, the large cycle reappears beside the still-stable equilibrium (upper bistable window $\approx1$–$2$ yr wide); (v) $\tau>\tau_+$, equilibrium unstable, the cycle the sole attractor. Inside either bistable window, histories at a large stock with low effort are captured by the cycle while near-collapse histories recover to the quiet equilibrium — abundance plus slow adjustment is the exposed trajectory, not scarcity. The upper-window attractor is a period-1 limit cycle (at $\tau=131.8$ ungated: Poincaré spread $<5\times10^{-3}$, envelope constant to $0.005\%$ over $2\times10^6$ yr, fundamental period $\approx135.6$ yr, all Floquet multipliers inside the unit circle with dominant nontrivial pair modulus $\approx0.81$; independent method-of-steps RK45 reproduces the envelope).

## 6.2 The registered numerical families

**M3-U (numerical result, accepted at source-stated status).** Candidate A crossings $6.8814$ / $132.3749$ yr (Candidate B $6.2136$ / $76.2906$ yr); persistence boundaries near $7.355$ and $131.24$ yr; lower bistable window $\approx0.47$ yr, upper $\approx1.1$ yr; basin-dependent capture at $\tau=131.8$ yr (near-equilibrium histories remain at the equilibrium while large-stock/low-effort histories converge to a large cycle); the upper-window attractor a stable period-one cycle with all nontrivial computed Floquet multipliers inside the unit circle and the near-lower-Hopf small orbit unstable (dominant multiplier $>1$). The saddle-node-of-periodic-orbits classification of either persistence boundary remains conjectural unless branch collision and nondegeneracy are demonstrated; sensitivity sweeps over $\eta\in[0.5,3.0]$ find zero or two positive cubic roots, and the two-crossing window in $r$ is bounded ($\approx(0.008,0.022)$ yr$^{-1}$ at $\eta=0.914$, extending to $\approx0.061$ yr$^{-1}$ at $\eta=3$) — model sensitivity results, not empirical calibration. A Droop nutrient–quota variant of the same core — an external nutrient pool and internal quota with quota-limited growth $\mu(q)=r(1-q_{\min}/q)$, a growth-coupled pool, the interior equilibrium preserved — leaves the $r$-window unchanged, with window upper edge $\le0.023$ yr$^{-1}$ at $\eta=0.914$ and no Hopf crossing at any $r\ge0.2$ yr$^{-1}$: a growth-coupled pool cannot be slow at large $r$ (the quota self-relaxes at exactly $r$ and the nutrient pool's relaxation grows with the throughput; the only $r$-independent slow pool is the working core's $\omega_A$-type exchange, which narrows the window) (numerical robustness result, source-stated). This is the nutrient–quota twin of the stage-structured robustness result carried in the sampled-governance companion study.

**M3-B (numerical result, accepted at source-stated status).** Candidate A crossings $3.67$ / $150.36$ yr (Candidate B $5.5128$ / $80.4245$ yr; this variant's own source registers no gated-Candidate-B global branch or fold result); the lower global boundary is not one saddle-node — the stable large-cycle branch folds near $\tau=5.574$–$5.575$ yr while the small unstable branch folds separately near $5.587$ yr (multiplier $1.0514\to0.998983$); the upper boundary is bracketed $[148.125,148.438]$ yr, summarised $148.3$ yr, type undetermined. Multiple far-from-equilibrium seeds failed to reach a large cycle throughout the tested interior range $5.57<\tau<148.3$ yr — finite searches that support, but cannot prove, interior monostability. The inferred subcritical signatures (amplitude exponent $0.47$; surrogate cubic coefficient $\approx3.9\times10^{-6}$) are inferred numerical classifications, not centre-manifold Lyapunov coefficients; the two lower folds belong to distinct families, so a single square-root collision law is inapplicable; $k$-independence is local only. Ungated-Candidate-B global values are registered in the source of the four-state pipeline: the three-state ungated Candidate B has no lower fold (its lower crossing is supercritical, §4.2) and an upper fold of the large cycle at $76.075$ yr against $\tau_+=76.2906$ yr — a narrow upper bistable window $(76.075,\,76.29)$ — while the four-state ungated Candidate B carries the corresponding Hopf crossings at $6.25$ and $76.33$ yr with its upper fold not pinned; these are registered numerical values, their classification as saddle-nodes of periodic orbits remains open, and no gated-Candidate-B fold location follows from them (numerical result — registered values, saddle-node classification open).

**M3-LC (numerical result, accepted at stated scope).** Upper persistence boundary $\approx132.0$ yr at $\psi=1$ versus $\approx132.5$ yr at $\psi=0$ (raw outputs $131.998$/$132.499$; separation $0.501$ yr), with an inter-locator discrepancy of $\approx0.8$ yr against an independent locator's $131.24$ yr taken as the localisation-uncertainty scale; the defensible conclusion is an order-of-one-year shift, not an exact percentage. At $\tau=115$ yr, $\kappa=0.5$, long-lived transients of order $10^4$–$10^5$ yr reach minimum $N\approx33$ under pure stock culling and $N\approx10$ under pure recruitment suppression. In the fixed-demand experiment ($D=0.7>S_{\max}=0.5$, $N(0)=50$), stock culling is stopped at its first hitting time of $N=0$ (equivalently implemented with an explicit donor limiter; the unconstrained vector field is not continued into negative stock), placing pure culling at zero near time $158$, while pure recruitment suppression approaches zero asymptotically and reaches $N<1$ near time $430$ — a first-hitting-time result. Local equivalence does not imply excursion equivalence; assigning $\psi$ to a field system requires age-, stage-, or replenishment-specific evidence.

**M4-A (numerical result, accepted).** Ungated Candidate A donor-limited equilibrium $(N^*,A^*,E^*)=(89.5256,\,397.8665,\,2.0896)$ with crossings $6.982022$ / $132.272044$ yr and persistence boundaries near $7.374$ and $130.77$ yr (upper bracketed $[130.770,130.771]$); gated counterpart crossings $\approx3.7849$ / $150.12$ yr with cycle periods $\approx360$–$380$ yr (lower regime) and $150$–$160$ yr (upper regime). The turnover stability boundary at $\tau=0$ is $\omega_A^*\approx0.001316298$ (gated $\approx0.001330$; the boundary is reported in the $\omega_A$ notation throughout), located by a $1798$-point equilibrium sweep, sixty sub-threshold simulations (ten $\omega_A$ values, six delays in $[0,300]$ yr, all converging to the equilibrium), and sixty continuation points above it producing a continuous Hopf pair — finite sweeps supporting delay-independent sub-threshold stability, not a theorem for all parameter values. The reduced open-pool caveat stands: freezing $A$ is not a justified fast-variable elimination at the baseline $\omega_A=10^{-3}$ yr$^{-1}$.

**MPF (numerical result, accepted).** At the illustrative baseline $(\mathcal M,\mu,K_A,d,c,\gamma_U,q,E_{\max},\eta,\delta_0,\Delta_\mathrm{ref},\tau_m)=(100,0.340,24.5,0.072,0.00995,0.388,0.0384,35.8,2.23,0.0118,2.29,5.13)$ the equilibrium is $(X^*,U^*,E^*)\approx(16.68,10.23,0.435)$, with no local Hopf crossing for $0\le\tau\le500$ (characteristic-root and argument-principle counts) and small perturbations decaying at all directly tested delays. The apparent onset near $\tau=33.4$–$33.6$ is a long-lived decaying transient (return within $\approx2\times10^4$ time units throughout the tested $33.4$–$34.8$ interval); for $\tau\gtrsim35$ a slow-fast oscillation persists for some tested memory histories and not others — basin-selective global dynamics, not a local Hopf or a classified periodic-orbit fold. The absence of a baseline Hopf is parametric: Hopf roots first appear at $\eta_\mathrm{crit}\approx2.337$, with two interleaving pairs over $\eta\in(2.337,3]$ (at $\eta=2.5$: $\approx0.6$, $54.2$, $92.9$, $113.1$ yr; at $\eta=3.0$ one pair spans $\approx4.5$–$41.2$ yr; at the out-of-range $\eta=10$: $17.568$/$18.362$ yr with a supercritical-consistent onset, exponent $0.59$, inferred). Above $\tau_+$ at $\eta=10$ the attractor is classified as homoclinic-like slow–fast (relaxation) intermittency rather than a torus or a period doubling — diagnostics: a broad onset-interval spectrum with no sharp peak, a thin map-like Poincaré section on $Z$-crossings, inter-excursion-interval coefficient of variation $1.58$, and return-map anticorrelation $r=-0.47$ — with the large-amplitude time fraction rising monotonically from $0\%$ at $\tau=18.4$ to $100\%$ by $\tau\approx22$ and no sharp second threshold separating quiet and captured regimes (inferred numerical classification, source-stated). The pair-birth structure behind the interleaving is registered: the large-delay pair is born at $\eta_\mathrm{crit}\approx2.337$ ($\tau_-\approx71.2$, $\tau_+\approx72.9$ yr) and migrates downward as $\eta$ rises, while the small-delay pair is born at $\eta\approx2.454$ with $\tau_-\to0$ at its onset. A sigmoid-gated effort variant of the same ecological core was screened across more than $300$ parameterisations without finding a genuine delay-induced Hopf — a numerical negative result over the sampled domain, not a structural impossibility theorem. The MPF regime is neither the M3-B regime nor a transfer of its threshold values.

## 6.3 The four-state working core (numerical results, source-stated status)

The characteristic matrix $\Delta(\lambda)=\lambda I-A_0-A_\tau e^{-\lambda\tau}$ of the gated working core at the frozen-donor equilibrium $(N,A,Z,E)=(89.52562,\,397.8665,\,\ln2/10,\,2.08962)$ has simple imaginary roots at

$$
\tau_-=3.78487\ \mathrm{yr}\ (\text{period }250.44\ \mathrm{yr}),\qquad
\tau_+=150.12175\ \mathrm{yr}\ (\text{period }159.13\ \mathrm{yr}),
$$

with $|\det\Delta(i\omega,\tau)|<10^{-18}$ — the characteristic-pinned pair, within $3.2\%$ (lower) and $0.2\%$ (upper) of the three-state values, inside the frozen-active-pool bound. Fourier collocation produces a small periodic orbit of residual $\sim10^{-13}$ immediately below $\tau_+$ (amplitude $0.090$ at $\tau=150.082$). Continuation of the large-amplitude cycle (converged orbit state and delay history carried between steps, $10^4$–$10^5$ yr per step) locates the two global folds at

$$
\tau_\mathrm{term,L}^{(4)}\approx5.63\ \mathrm{yr},\qquad \tau_\mathrm{fold,R}^{(4)}\approx64.4\ \mathrm{yr},
$$

the lower bracketed by steady behaviour at $\tau=5.62$ (peak-to-peak $N$-amplitude $\approx23$) and collapse by $5.64$, the upper by steady behaviour at $\tau=64.5$ (amplitude $\approx11$) and collapse by $64.25$. The resulting topology is a narrow lower bistable window $(3.78,5.63)$ yr, a wide monostable interval $(5.63,64.4)$ yr, and a wide upper bistable window $(64.4,150.1)$ yr in which the large cycle coexists with the stable equilibrium but, from generic far-from-equilibrium histories, is reached only for $\tau$ above roughly $75$–$100$ yr (depleted-stock histories only near $\tau\gtrsim135$). Cycle periods run from $\approx371$ yr at $\tau=4.5$ to $\approx320$ yr at the lower fold, and from $\approx156$ yr near $\tau_+$ to $\approx73$ yr at the upper fold. Whether either fold is a saddle-node of periodic orbits (versus a Neimark–Sacker or torus-mediated transition) is not established. A second bifurcation parameter invisible to the three-state core appears: at $\tau=0$ the four-state equilibrium is unstable for $\omega_A>\omega_A^*\approx0.001316$ and delay-independently stable below it; above it, on the ungated system, both Hopf points and both folds track smoothly, $\tau_-$ falling from $\approx17.5$ to $\approx6.9$ yr with the monostable interval remaining $\approx120$–$260$ yr; the gated $\tau_-\approx3.78$ is the baseline $(\omega_A,\kappa_A)$ value, not a uniform constant. Oscillation periods throughout $\tau<\tau_-$ are $250$–$390$ yr, essentially independent of $\tau$: the frequency is pinned by $r$ and $\tau_m$, not by institutional delay, and uniformly raising $r$ toward fish-like values destroys the oscillatory regime rather than compressing the period into a decade.

The frozen-donor quasi-equilibrium discipline governs all of these numbers: the working point requires continuing geological support ($\approx4.652$ stock units per year) and is not a rest point of the closed mass ledger; it is incompatible with the formal QSS target; and the working-core thresholds are $\sigma_\mathrm{geo}=1$ properties.

## 6.4 The sample-and-hold monodromy (theorem, proof verified)

**Theorem 6.1 (Sampled-data monodromy).** Linearise the gated three-state core about the interior equilibrium and replace the delayed feedback by sample-and-hold of period $T_r$ with one Euler review step. Between reviews the variational system is $\dot\xi=A_\mathrm{hold}\xi$ with $A_\mathrm{hold}$ as in §5.4; the monodromy of one review interval is

$$
M(T_r)=\begin{pmatrix}1&0&0\\0&1&0\\0&T_rC_Z&1+T_rC_E\end{pmatrix}\exp(A_\mathrm{hold}T_r).
$$

The sampled equilibrium is exponentially stable iff every eigenvalue of $M(T_r)$ lies in the open unit disc; a Neimark–Sacker crossing occurs at those $T_r$ where $M(T_r)$ has a simple pair $e^{\pm i\theta}$, $\theta\notin\{0,\pi\}$, with the remaining spectrum inside the disc; and $(M(T_r)-I)/T_r\to$ the continuous undelayed Jacobian as $T_r\to0$. The statement concerns this sample-and-hold/Euler review scheme, not the continuous-delay equation.

On the gated Candidate A hold map, annual review is unstable — $\rho(M(1))=1.00055$, the undelayed linearisation being already unstable — and the sampled equilibrium restabilises by a Neimark–Sacker pair at $T_r^\mathrm{NS}=47.536$ yr with a period-doubling multiplier at $T_r^{(-1)}=79.143$ yr: for a slow stock under this review operator, the control is the review interval, and the continuous-delay settling recommendation does not transfer to periodic review. The fast-pelagic review windows ($T_r\approx3$–$4$ yr anchovy-class, $6$–$12$ yr sprat-class) reported in the source record are zeros of the stage-structured review map, a different operator; both statements are $\det(M-e^{i\theta}I)=0$ on the map to which they refer. The information-layer companions of these sampled operators are the conditional knowledge-kernel theorems of the theorem-atlas companion stated in §3.4: what can be known under sampled observation of an RFDE on a compact history class, and under review-synchronised hybrid resets — each conditional on its compactness and held-solution-map hypotheses.

## 6.5 Parameter windows

Within the parameter subregion where the Candidate A two-Hopf pair exists, one-at-a-time variation across the reported ranges preserves the pair and the lower-boundary structure. Outside the bounded $r$-window the system is delay-independently stable or lacks a positive equilibrium. $\tau_-$ lies in $3.7$–$7$ yr across the two effort laws and both candidates, and in $4$–$25$ yr across the full $(r,\eta)$ rectangle; $\tau_+$ is primarily controlled by the biological time $1/r$ but also depends on the effort-response chart — Candidates A and B share $r=0.02$ and have $\tau_+\approx132$–$150$ yr and $\approx76$–$80$ yr respectively across the two effort laws (A: $132.37$ ungated, $150.36$ gated; B: $76.29$ ungated, $80.42$ gated). The literature range $r\in[0.005,0.4]$ yr$^{-1}$ is wider than the instability window. The dimensionless groups that fix $N^*/K$ and $r\tau_\pm$ once effort is scaled by $E_{\max}$ — and the complementary fact that the separate effort scale is not identifiable from $(N,Z)$ alone — are the identification pair owned by the sampled-governance and architecture companion studies respectively; the $k$-qualifications of §4.2 ride the same parameter audit.

---

# 7. The loop-gain family and the open conjecture register

## 7.1 The general feedback equation (identity + theorems, proofs verified)

The vector ledger and the reduced cores share a linearised feedback identity, not one nonlinear system. Writing the ledger in primitive fluxes — assimilation $g$, mortality $m$, decomposition $d_U$, harvest $h$ — the signed depletion signal

$$
\ell=h-(g-m)=-\dot X
$$

is an identity, and liquidation is $[\ell]_+$. Let $\boldsymbol\xi$ be the ecological perturbation, $\dot{\boldsymbol\xi}=\mathbf J\boldsymbol\xi+\mathbf b_Ee$, with memory a gain-$\gamma_m$ filter of $-\mathbf c^\top\dot{\boldsymbol\xi}$ (the memory gain is written $\gamma_m$ here to free $g$ for the assimilation flux of $\ell=h-(g-m)=-\dot X$; the source reuses $g$ for both, fixed by context in each formula). The linearised loop of every core in this paper is

$$
\lambda-C_E-C_Ze^{-\lambda\tau}\,\frac{-\gamma_m\lambda\,\mathbf c^\top(\lambda\mathbf I-\mathbf J)^{-1}\mathbf b_E}{1+\tau_m\lambda}=0 .
$$

The three-state core is the $1\times1$ case ($\mathbf J=A_N$, $\mathbf b_E=A_E$, $\gamma_m=1/2$); the primitive-flux (stoichiometric) core is the $2\times2$ stock–detritus block with $\gamma_m=1$ (its signed memory $\ell=-\dot X$ is unregularised, which places it outside the $Z\ge0$ invariance statement of §2.2). Both reductions are symbolic identities: the three systems share this characteristic identity but differ in their nonlinear objects — the upper global fold moves from $\approx148$ yr (three-state) to $\approx64$ yr (four-state) while the Hopf pair stays within a few percent, the equilibrium memory differs ($Z^*=\delta>0$ versus $0$), and the primitive-flux core has no baseline Hopf ($\eta_\mathrm{crit}\approx2.34$). The three ingredients are an ecological resolvent supplying admissible frequencies, an institutional gain $C_Z\gamma_m$ that must close the loop, and a delay supplying phase; the gain condition is $\tau$-independent, the phase condition rotates through match and past it, and non-monotone delay-stability is the generic behaviour of the architecture.

## 7.2 The loop-gain exclusion theorem and the delay-independent certificate

**Theorem 7.1 (Loop-gain exclusion of delay-induced Hopf).** Write the general feedback equation as $\lambda-C_E-C_Ze^{-\lambda\tau}G(\lambda)=0$. If

$$
\sup_{\omega\in\mathbb R}\frac{|C_Z|\,|G(i\omega)|}{|i\omega-C_E|}<1,
$$

then there is no purely imaginary characteristic root for any $\tau\ge0$, hence no delay-induced Hopf. (Proof: an imaginary root would give $|i\omega-C_E|=|C_Z||G(i\omega)|$, contradicting the strict supremum.) The companion **Nyquist Hopf criterion** states that a Hopf root exists iff $L(i\omega,\tau)=C_ZG(\lambda)e^{-\lambda\tau}/(\lambda-C_E)$ equals $1$ for some $\omega>0$, with the small-gain bound $|L|<1$ as the uniform special case.

The theorem-atlas companion's general delay-independent certificate is the Halanay-type small-gain theorem (a conditional theorem and a sufficient certificate; the canonical statement is the atlas's): if for some $\alpha_0>\beta_0\ge0$ the logarithmic matrix measure satisfies $\mu_*(A_0)\le-\alpha_0$ and $\|A_1\|_*\le\beta_0$, then the zero solution is exponentially stable for every fixed $\tau\ge0$, with decay rate the unique $\eta>0$ solving $\eta=\alpha_0-\beta_0e^{\eta\tau}$. The condition is sufficient, not necessary: its failure removes the certificate without proving instability or a Hopf bifurcation, and in nonlinear applications the theorem is local after a declared linearisation unless a global incremental bound is proved. The named-system theorems of §§4.4–5.2 are instances of this certificate family at declared linearisations.

## 7.3 The logistic identification theorem

**Theorem 7.2 (Logistic identification).** In the primitive-flux core take $A\gg K_A$ and set $\mu-d=r>0$, $c=r/K$; then $g-m=rX(1-X/K)+O(K_A/A)$, and under the fixed-target exchange closure the stock component converges to the quasi-steady four-state stock equation at saturated $A$. The identification requires the mortality identification: $K_A\to0$ **without** $\mu-d=r$ and $c=r/K$ yields $g\to\mu X$, which is not logistic. The claim concerns the linearised feedback identity, not the nonlinear objects, which also differ in the equilibrium memory level, the effort baseline, and the closed form of $E^*$.

## 7.4 The saturating-gate negative screen

Replacing the autocatalytic factor $\eta EZ_\tau/\Delta_\mathrm{ref}$ by a saturating gate $\sigma(Z_\tau/Z_0)$ whose linearisation at equilibrium decreases in deployed effort and contains no factor $\eta E^*/\Delta_\mathrm{ref}$, a search of more than $300$ randomised parameterisations (Newton eigenvalue tracking, joint modulus minimisation, nonlinear integration) found no genuine imaginary-axis root of the general feedback equation (a numerical nonexistence report). This is a numerical nonexistence report on a compact searched set, not an analytic exclusion on the parameter space; the bound itself is not verified analytically over the full domain. The gated law (M3-B) is not of this class — its $C_Z$ contains both the gate factor and the autocatalytic factor, and it admits the Hopf pair. Autocatalytic coupling $\eta E^*/\Delta_\mathrm{ref}$, which grows with deployed effort, is the mechanism that produces the Hopf pair.

## 7.5 The exergy-gated suppression conjecture

**Conjecture 7.3 (Exergy-gated suppression).** For a declared class of autocatalytic extractive controllers, sufficiently low deployable exergy reduces the loop gain below every admissible Hopf-frequency modulus condition. This is not universal: depletion of institutional capacity may also disable protective action or create hysteresis.

The conjecture is a loop-gain theorem target — a prospective member of the exclusion family of Theorem 7.1 and the weighted small-gain theorem of §4.4, to be proved by exhibiting the gain bound of Theorem 7.1 under a declared exergy-limited controller class. Its audit status is model-specific: the architecture-level exergy programme (quality grades, typed feasibility constraints) is a different object owned by the architecture companion, and this conjecture makes no claim on it. The conjecture is stated at conjecture status; no class, bound, or proof is claimed here.

## 7.6 The open conjecture register

The following statements are registered conjectures with declared gaps and disproof routes; none is asserted.

**Periodic-orbit-fold persistence under typed coupling (conjectures, merged family).** A transverse fold of periodic orbits in a registered retarded subsystem persists under sufficiently small typed vector coupling and compatible additional fixed delays when the orbit has the required spectral gap and the infinite-dimensional Poincaré map is sufficiently smooth; equivalently, persistence requires normal hyperbolicity, a spectral gap, and regularity of the Poincaré map, verified for the actual infinite-dimensional system. Missing proof: establish the baseline fold by periodic-branch continuation, formulate the coupled system on a common phase space, and verify transversality, spectral separation, and regularity — finite-dimensional slow-manifold citations do not establish these points. Disproof route: exhibit arbitrarily small admissible coupling that destroys the fold through resonance, boundary contact, loss of regularity, or a competing centre direction. The stress-test frame's structured-persistence statement is the same family and carries the fold caution that transverse normal hyperbolicity does not imply normal hyperbolicity of the fold orbit itself (§8.3).

**RFDE/hybrid transition persistence (conjecture).** Persistence of a reduced hybrid/RFDE nonlinear transition requires well-posedness of the semiflow, fast difference-operator contractivity, spectral separation, centre-manifold reduction, transverse Poincaré-map conditions, regular coupling, and preservation of material feasibility and safety. The fast difference-operator contractivity condition applies to particular neutral/difference formulations and is not a universal RFDE condition; the fold-orbit caveat is inherited.

**$n$-patch super-equilibrium equivalence (conjecture).** For $n$ coupled patches with cooperative diffusion, the kernel is nonempty iff the minimal-harvest field has a super-equilibrium in the admissible set (two-patch instances are verified in the super-equilibrium criterion stated below), which for type-(U) patches with product controls is equivalent to the existence of an equilibrium there. The equivalence holds for cooperative transport and fails in general for competitive or predator–prey couplings, where super-equilibria need not exist and an unstable focus can sit inside the set with a cycle that leaves it.

**The two-patch super-equilibrium criterion (remark — criterion, source-declared).** For cooperative patch fields the two-patch kernel is nonempty if and only if a super-equilibrium with componentwise minimal flow exists in the admissible set — a point $x$ with $f_{\min}(x)\ge0$ coordinatewise. The mechanism: for a cooperative field, the trajectory from a point where the vector field points weakly into the admissible set cannot leave the upper set, and any viable orbit has an $\omega$-limit point in the set at which $f_{\min}\ge0$. Unlike the equilibrium test, the super-equilibrium test is checkable directly — by grid search or by monotone root-finding — without solving the quartic equilibrium system; the identical-patch instance $(a,s^*)$ exists, and the asymmetric MSY counterexample admits none, consistent with its empty kernel (the source record's Remark 10.2). The $n$-patch equivalence itself remains the conjecture above.

**Variable-time delayed-hybrid information kernel (conjecture).** A nontrivial class of variable-event delayed hybrids with compact piecewise-history phase space, uniform break and jump budgets, resets, and bounded-error partial observations admits an exact compact information process and closed information-state tube kernel. Two independent gaps are declared: the piecewise-history topology (compactness under the break budget with continuous delayed evaluation and outer-semicontinuous reset correspondence plus the lower stability needed for predecessor closure) and the closure of bounded-error observation fibres. Disproof route: shifted jump histories or an observation model whose conditioned information sets destroy predecessor closedness.

**Restricted delay-separation principle (conjecture).** If ecological observation, assessment, decision, and deployment modules are independently identified and enter a locally linear loop as a product of stable transfer operators, their phase contributions can be separated from sufficiently rich input–output data up to declared structural symmetries. Missing proof: structural identifiability of factored transfer functions and persistence under feedback. Disproof route: two non-equivalent lag factorisations with identical admissible closed-loop observations.

**Early-warning diagnostic indicators (scoped remark, source-declared).** Beside the fold events of §§6–7, four leading indicators are candidate diagnostics for approaching a fold-type transition: critical slowing down (the lag-1 autocorrelation of the stock rises near a fold bifurcation); rising variance (rolling variance increases under additive noise near a bifurcation); epistemic divergence (a growing gap $|\hat S-S|$ in the continuous observation track); and policy inertia (physical stress increasing without a corresponding control adjustment). The caveat is load-bearing and stated exactly: these are not universal early-warning signals — they apply near fold bifurcations under additive noise with responsive control, they do not follow from the viability machinery alone, and each is a separate falsifiable empirical-statistical claim (the regime-shift and early-warning framing is Scheffer and Carpenter 2003, Scheffer 2009, Scheffer et al. 2009, and Carpenter et al. 2011, and the scope caveat above is exactly what that literature's own caveats require).

---

# 8. The stress-test frame: response-sign hypotheses and the variant registry

## 8.1 The response-sign hypotheses (policy hypotheses, defined objects)

The interpretive frame of this paper's two channels is a three-hypothesis response-sign taxonomy: **H1**, scarcity-amplifying extraction ($\partial\mathcal G_\mathrm{H1}/\partial Z>0$ over the relevant range); **H2**, protective restraint or restoration (the reversed or restoration-including effect on extraction); **H3**, inertia, capture, or state-dependent response. The frame's own discipline is preserved verbatim: no result for H1 is generalised to H2 or H3. H1's named instantiation is the mobilisation family of §4 (the registered delay-amplified extractive mobilisation systems); H2's named instantiation is the protective channel of §5 (the two-delay identity content); H3 rides the theorem-atlas companion's institutional-implementation family. The model must state whether $E$ is an endogenous industry response, a legal quota-utilisation state, or an actual institutional control; these interpretations are not interchangeable, and the three-hypothesis comparison frame is the interpretive context for both named families. The frame does not claim that institutions generally behave in any of the three ways; a model-specific bifurcation threshold is not a universal policy threshold. One caveat disciplines the empirical reading of the delay parameter itself: the response-lag values that anchor $\tau$'s timescale plausibility rest on the Hocherman synthesis (101 studies) as a lower-bound proxy only — the distribution covers response lag (problem recognition to decision), not implementation lag (decision to effected action), in the DPSIR terminology the review itself uses; the review reserves implementation lags for future work, and no implementation-lag dataset exists, so measured $\tau$ values underestimate total institutional delay (scope caveat, source-declared).

## 8.2 The physical mechanism types (mechanism-type definition)

The phrase "liquidation" has three distinct physical meanings: standing-stock culling (present extraction removes reproductive stock directly — the typed-flux object owned by the material-ledger companion); recruitment suppression (present use prevents future recruits without immediate adult removal); and weak viability coupling (limited or indirect effect on reproduction — the composition object owned by the architecture companion). Recruitment suppression modifies or diverts a recruitment flux and is one typed-flux incidence family with culling and weak coupling; its named treatment in this paper is the recruitment channel of the two-channel law (§2.3, §6.2). A diagnostic label never determines physical destination: material routing is determined by the typed physical module, not by whether a flow exceeds a service or regeneration benchmark.

## 8.3 The variant registry (registered obligations)

The stress-test programme archives nine numerical-programme variants: ungated, gated, hybrid-effort, four-state support-pool, two-channel liquidation, stage-structured, sampled-review, thermodynamic-tether, and unified-core. Eight of the nine registry rows are routed to this paper; the sampled-review row rides the sampled-governance companion study. Each row is a **registered obligation, not a discharged artifact**: the source's own inventory includes no equations, parameter files, code, or outputs for the archived variants, so each requires source equations, parameters, scripts or software settings, and outputs in the research programme's registry before any numerical claim. The registry's tabulation discipline is the reproduction obligation's content: governing equations and state/control interpretation; parameter units and identifiability status; equilibrium and boundary conditions; numerical method, mesh, time-step, event handling, and horizon; branch identity and uncertainty; and the status label (analytical, independently reproduced numerical, conjectural, or superseded). Distinct claim types are kept distinct: a persistence boundary, a fold, an SNPO-confirmed fold, and an initial-condition basin observation are different claims, and no fold is called SNPO-confirmed without branch-specific multiplier and transversality evidence.

Where a variant's verified content exists, it lives in the closed rows of this paper and is cited together: the ungated and gated variants are the registered systems M3-U and M3-B (§§2, 4, 6); the four-state support-pool variant is the working core of §2.4 and §6.3; the two-channel liquidation variant is the M3-LC law and the protective two-channel system (§2.3, §2.5, §4.4, §5); the unified-core variant is the primitive-flux core (§2.3, §7); the stage-structured variant's theorem content belongs to the gated conditional sources and is cited at the seam if that paper is triggered. Two discipline remarks frame every row: a frozen $A$ is a formal limiting case, not a default physical assertion; and gating, damping, or saturation is not accepted merely because it preserves a desired bifurcation — it must have a constitutive interpretation and an independently stated parameter role (the multiplicative gate of (M3-B) does: it is the effort ceiling's hard saturation). The safety-relevance ladder is the interpretive frame for all of them: a local bifurcation in a reduced model is not automatically a sustainability transition — the three levels are existence of the bifurcation in a specified model, persistence of the organising structure under physically admissible coupling (the conjecture register of §7.6), and safety relevance, measured by the intersection of an attractor, basin, or uncertainty tube with the declared unsafe set, where basin membership and not only attractor location matters in bistable systems.

**The thermodynamic tether (illustrative worked extension).** The thermodynamic-tether variant's equations are stated in the working-core source record at illustrative status; the registry row remains a registered obligation, and this section's tabulation discipline governs any numerical claim on it. If $E$ is physical effort with an energetic cost, the extinction rest $(0,\delta,E^*)$ of §3.1 requires an unmodelled subsidy, and closing that gap without disturbing the interior Hopf analysis adds a governance-capital stock $K_\mathrm{cap}$ (distinct from the carrying capacity $K$) with its own dynamics and a pole-free gate,

$$
\dot K_\mathrm{cap}=qEN-K_\mathrm{cap}(\delta_K+c_EE),\qquad
\dot E=\bigl(1-\frac{E}{E_{\max}}\bigr)\bigl(1-e^{-K_\mathrm{cap}/K_0}\bigr)\bigl[\eta E\bigl(\frac{Z(t-\tau)}{\Delta_\mathrm{ref}}-\frac{E}{E_{\max}}\bigr)+\delta_0\frac{Z(t-\tau)}{Z_\mathrm{ref}+Z(t-\tau)}\bigr]-\mu_EE,
$$

with $\delta_K$, $c_E$, $K_0$, $\mu_E>0$ the capital depreciation, marginal effort cost, capital half-saturation, and institutional-entropy decay rates. At $K_\mathrm{cap}=0$: $\dot K_\mathrm{cap}=qEN\ge0$ and $\dot E=-\mu_EE$; on the extinction face $N=0$ the yield vanishes, $K_\mathrm{cap}\to0$, the gate vanishes exactly, and $E\to0$, so every tested trajectory from $(E_0,K_{\mathrm{cap},0})\in[0.5,29]\times[0.1,1000]$ converges to the thermodynamically closed extinction state $(0,\delta,0,0)$ — the extinction state is an attractor when the tether binds. The pole-free gate $1-e^{-K_\mathrm{cap}/K_0}$ is chosen over the rational gate $K_\mathrm{cap}/(K_\mathrm{cap}+K_0)$, whose pole at $K_\mathrm{cap}=-K_0$ silently re-opens the gate once an insufficiently protected coupling drives $K_\mathrm{cap}$ negative. The interior equilibrium survives as the transcendental root of $F(E^*)=(1-E^*/E_{\max})(1-e^{-K_\mathrm{cap}^*(E^*)/K_0})\mathcal B(E^*)-\mu_EE^*=0$, with $\mathcal B$ the untethered effort bracket and $K_\mathrm{cap}^*(E)=qEN^*(E)/(\delta_K+c_EE)$; a necessary condition for a positive root is $\mu_E<\alpha:=qK\delta_0\delta/(K_0\delta_K(Z_\mathrm{ref}+\delta))$, and the true collapse threshold is a saddle-node of the equilibrium branch at $\mu_E^\mathrm{SN}\approx5.9\alpha$ (the source locates the saddle-node at this multiple under an illustrative parameterisation that it does not itself tabulate, so no numerical value of $\alpha$ is asserted here), and between $\alpha$ and $\mu_E^\mathrm{SN}$ the tether exhibits an institutional Allee effect: $E=0$ and a positive $E_2^*$ are both locally stable, separated by an unstable basin boundary $E_1^*$. The extension is a worked feasibility analysis: the registered thresholds of §§4–6 use the untethered effort law, the parameters $\delta_K$, $c_E$, $K_0$, $\mu_E$ carry no calibration, the tether's effect on the Hopf crossings and folds is not computed, and the variant's tabulation obligation stands.

---

# 9. The seam to the material-ledger companion

The partition between this paper and the material-ledger companion is fixed by the ledger-to-dynamics interface contract. The ledger companion owns the closed primitive finite-donor ledger — its equations and full routing, its conservation and positivity theorems, the componentwise deficit diagnostics and depletion horizons, and the closed-donor no-rest and extraction-integrability limitations. This paper owns the named open/frozen-donor retarded systems and their bifurcation results, stated locally in §2.

**The exact shared object.** Under the single-resource specialisation $\mathcal S_{1R}$ (single resource, $S=R$, $\chi=1$, $\mu=\nu=\rho=0$, $C^A=0$) with the local stock equation $\dot N=R-qEN$, the deficit identity

$$
D(t):=qE(t)N(t)-R(N(t),A(t))=-\dot N(t),\qquad \Lambda(t):=[D(t)]_+=[-\dot N(t)]_+
$$

holds for every trajectory of either the specialised ledger or the named core (identity, restated). *Proof:* substitute the stock equation. For the three-state core, the declared frozen-active-pool constitutive limit $R(N,A)\to rN(1-N/K)$ applies on its stated finite-time, local scope; that replacement is separately an approximation and carries the error status of Theorem 2.6. The collapse $\Lambda=[-\dot N]_+$ is a property of the specialisation, not a definition of liquidation on the unreduced ledger. The ledger-side row for this identity is the ledger companion's (a cross-reference, not a retained row of this paper); the projection handing the specialised ecological–institutional block to the dynamics is likewise the ledger companion's, and the closed ledger and its positivity theorem are stated there.

**The non-reduction boundary (restatement of the contract).** There is no exact dynamic reduction from the closed primitive finite-donor ledger to the working four-state field — not as a projectable reduction and not as a regular perturbation. The reasons are mathematical: the primitive ledger uses the intrinsic donor-limited target while the working core uses the derived target; at the working equilibrium the two active-pool vector fields differ by an $O(1)$ term; the working point requires continuing geological support and is not a rest point of the closed finite-donor system; the cumulative donor-draw quantity is not a trajectory-tracking error between the fields; and the closed primitive system makes sustained extraction integrable and therefore cannot possess the working positive-flux rest indefinitely (the no-interior-rest theorem is the ledger companion's). The mapping type for exact dynamic reduction is rejected; the permitted relation is analogy for shared mechanism language plus diagnostic reconstruction of omitted mass flows. This paper's global periodic results are properties of the named cores and do not transfer to the closed primitive ledger.

**Open-projection accounting.** As declared in §2.4, the working core routes omitted turnover to a diagnostic detritus/inert sink, treats imposed recharge as geological draw, is not mass-closed on $(N,A,Z,E)$, has a mass discrepancy reconstructible from the omitted donor/turnover flows, and carries version-specific global results. This disclosure is part of the local model statement, not an optional citation.

**Model-version identifiers.** The three-state gated core (`DYN-C3-GATED`), the turnover-corrected four-state working core (`DYN-C4-WORKING`), and the fixed-intrinsic-target quasi-steady core (`DYN-C4-QSS`) are registered as distinct objects; the quasi-steady core is a comparison object only and is never merged with the working core. The refereeability test of the contract holds on both sides: none of the ledger companion's conservation, positivity, no-rest, or diagnostic claims requires this paper's bifurcation results, and this paper contains the full named equations, phase spaces, parameter and version identifiers, local positivity, characteristic results, and computational artifacts without citing the ledger companion for the existence or validity of its dynamics.

---

# 10. Reproducibility and the certification hierarchy

Every computational claim in this paper carries one of four certification levels:

| Level | Meaning |
|---|---|
| Nominal | A computed output exists; no independent reproduction is recorded |
| Re-execution-verified | A committed runner reproduces the outputs identically on re-execution |
| Independently re-executed | Reproduction on a fresh execution in a second session or environment |
| Certified | A validated (interval/rigorous) enclosure of the mathematical object |

Applied to this paper's claims:

**Hopf interval certificates (gated Candidate A).** The interval-Newton enclosures of the positive roots of $H$ and the branch-safe phase evaluation, giving $\tau_-\in[3.6661490142739,\,3.6661490142743]$ and $\tau_+\in[150.3584773101408,\,150.3584773101421]$ yr, are reproduced by the committed interval pipeline (the research programme's interval-Newton Hopf-certificate runner script, part of its validated-computations artifact set; outward-rounded float64 via nextafter, interval transcendentals at 50-digit working precision, branch-safe interval atan2, simple-root and transversality sign checks with the lower crossing stabilising and the upper destabilising; the interval-arithmetic foundations are Moore 1979, Kearfott 1996, and Cloud, Moore, and Kearfott 2009); the outputs are identical on re-execution. Level: **re-execution-verified**; within the interval-pipeline scope the certificate condition is discharged at the repository level — the interval-Newton enclosures are the certification hierarchy's certified tier for the *local spectrum of $H$*, while the global fold events of §6 remain at the nominal tier (no Moore–Spence/Krawczyk certificate; Appendix B.3), so the paper's use of the certified tier is exactly scoped to what the interval pipeline establishes. The publication-archive obligation remains open.

**Fold evidence.** The fold and turning-region events of §§6.1–6.3 are **nominal**: numerical continuation, multiplier, basin, and turning-region results. The fold certificate is not obtained: no Moore–Spence zero, no interval Krawczyk inclusion, no interval transversality or curvature enclosure, and no continuous-delay bordered lift exist for these events (Appendix B.3). A nominal fold rebuild at three collocation resolutions ($m=64/96/128$), with executions reproducing the committed artifacts identically, places all three resolutions inside the interval for which the certificate was never obtained; the interval Krawczyk stage is unimplemented, so the rebuild is re-execution-verified at the nominal level and certifies nothing.

**Source-stated numerical families.** The Lyapunov coefficients, continuation, Floquet, monodromy, and basin results of §6 (inventoried row by row in Appendix A) are accepted at their exact source-stated status; the publication-artifact archives (branch, Floquet, history, solver, and environment artifacts; the sampled-numerics documentation action) remain open obligations. Level: **nominal** at the paper level, with the archive actions registered.

**Reproduction targets (not numerical propositions).** A simple crossing recorded near $\tau^*\approx43$ with period $\approx263$ time units and $\mathrm{d\,Re\,\lambda}/\mathrm d\tau<0$ at $\eta=5$, $\varsigma=0.8$, $K_0=0.03$, $q=0.01$ (an elevated-forcing cod-class calculation on an incompletely specified ten-state template) is retained as a reproduction target pending recovery and registration of the constitutive closures actually used; the closure convention, remaining parameters, root count, active nonsmooth branch, residual values, tolerances, and full search domain remain to be recovered. The record's other two run classes are carried at the same status: class 1 — life-history anchoring, with maturation times $g\approx1$, $2$, and $5$ yr associated respectively with the anchovy-, sprat-, and cod-class cases and productivity chosen to satisfy the interior survival condition, for which no crossing is detected over the tested delay search at the default economic settings (the tested interval and complete parameter vector remain to be recovered); class 2 — the broader crossing search, in which crossings occur in a parameter subset, all examined with $\mathrm{d\,Re\,\lambda}/\mathrm d\tau<0$ and generally with periods of order $10^3$–$10^4$ time units, and no two-crossing $\tau_-/\tau_+$ window is recorded (exact residual values, tolerances, and the full search domain remain to be registered) (reproduction targets, not numerical propositions). The sign discipline governs any future use: $\mathrm{d\,Re\,\lambda}/\mathrm d\tau<0$ at a simple crossing is a stabilising local crossing — the equilibrium is locally unstable just below and stable just above — and such a result cannot support language asserting that increasing delay creates oscillatory instability.

**Registration obligations.** Two registration obligations are carried, not discharged: the delayed-recruitment companion registration of §2.6, and the variant-registry tabulation discipline of §8.3. Until the computational records are complete, the corresponding outputs have exploratory status rather than the status of reproducible numerical propositions.

---

# 11. Provenance, reproducibility, and limits

**Provenance.** Every source-derived statement carries its provenance key; the keyed inventory row links to source location, canonical module, mapping type (exact specialization / approximation / counterexample-or-limit), evidence status, and destination. The retained set (55 main + 13 bounded-appendix rows) derives from the ten sources of the research programme's corpus, identified with their per-source row counts in Appendix A. The per-row verification record, the row-level evidence table, and the ledger-to-dynamics seam contract are part of the programme's verification artifact set, available in the project repository. The manuscript-native entries (Appendix A, Table A2) restate source content that carries no inventory row, at source-declared statuses: the two-patch super-equilibrium criterion and the early-warning-indicator scope; the reproduction-record run classes 1–2; the implementation-lag caveat; the thermodynamic tether, the $\eta=10$ intermittency classification and pair births, the Droop $r$-window robustness experiment, and the ungated-Candidate-B registrations; and the verification-status update and certification protocol.

**Reproducibility.** The certification hierarchy of §10 is stated per claim. The Hopf interval certificates are reproduced by the committed interval pipeline with outputs identical on re-execution; the nominal fold rebuild is re-execution-verified at three collocation resolutions; the source-stated numerical families carry their declared status with the publication-artifact archives registered as open obligations. The research programme's verification battery passes on the repository tree containing this manuscript.

**Limits.** (i) The slow-fast reduction of the five-state system is a conjecture with a declared spectral gap; the local Hopf persistence theorem is conditional on it, and no global fold event falls under any proved statement. (ii) The fold certificate is not obtained for any event in this paper; every fold statement is numerical continuation, multiplier, basin, or turning-region evidence, and the interval Krawczyk stage is unimplemented. (iii) The conditional corollary holds exactly under its four interpolation hypotheses; the interpolation family's common-equilibrium and denominator properties are not otherwise established. (iv) The variant registry rows are registered obligations — the archived variants are registered, not established — and the delayed-recruitment registration is absent, so the corresponding outputs are exploratory. (v) The sampled numerics carry source-stated status with the archive actions open; the $T_r=2.306$ crossing belongs to the Euler discretisation, and the review-window statements belong to the operator (hold map or stage-structured map) on which they are computed. (vi) Basin statements are restricted to the histories actually tested; interior monostability is supported by finite searches, not proved. (vii) Nothing in this paper is empirical: the parameterisations are mathematical anchors, the reproduction targets of §10 are not numerical propositions, and the empirical identification programme is the sampled-governance companion's. (viii) The research programme's three conditional-allocation sources are outside this paper's retained set, and no claim here depends on them.

---

# Appendix A. Statement inventory

This appendix inventories the formal statements of the paper in two tables. The **source key** column carries the research programme's inventory row codes (`CC-A0dd-ddd`) or manuscript-native keys (`MS-Native-n`); the codes key each statement to the source-to-canonical statement inventory committed in the project repository and are provenance keys, not citations. Every source-derived entry was verified against its source manuscript in the closure campaign of 2026-08-27/28 (full-source reads with per-statement confirmation of existence, kind, proof presence, module, and mapping type); this is content-level verification of provenance, not a promotion of any entry's mathematical status, and the cross-module interface contract remains an open obligation recorded per row. The retained set (55 main + 13 bounded-appendix rows) derives from ten sources of the programme's corpus: A001 (2 rows), A002 (7), A003 (11), A006 (3), A010 (3), A011 (1), A012 (11), A018 (8), A020 (9), and A025 (13 appendix rows). The tables show 70 concordance codes because two of them (CC-A018-004, CC-A019-004) appear only as cross-citation pointers inside the seam-restatement records of §9 — cross-references owned by the material-ledger companion, not retained rows; the retained count is 68.

**Legend and disclaimer.** Entries categorized as *Definition*, *Model definition*, *Registration*, *Registry*, *Programme*, *Scope*, or *Reproduction target* are stipulated or declared — they carry no empirical truth-value and need no proof. Entries categorized as *Theorem*, *Proposition*, *Corollary*, *Identity*, *Conjecture*, *Counterexample/limit*, *Numerical result*, or *Record* carry exactly the status stated: theorems, propositions, and identities are established under the assumptions stated where they appear (proved in this paper or verified against the identified source's proof); conditional entries retain their hypotheses as mathematical content; numerical entries are computed outputs tied to registered equations, parameter sets, history classes, methods, tolerances, and finite domains; inferred numerical classifications add an interpretation not established by the corresponding normal-form calculation. The formal validity of any entry within the declared framework does not by itself imply applicability to an empirical system (§11, Limits).

**Table A1. Stipulated definitions, model registrations, scope restrictions, registered obligations, and declared programme entries.**

| Source key | Statement | Status | Proof availability and evidence | Location |
|---|---|---|---|---|
| CC-A003-001 | H1: scarcity-amplifying extraction (response-sign hypothesis) | policy hypothesis (defined object) | sign condition verified in source; named instantiation §4 | §8.1 |
| CC-A003-002 | H2: protective restraint/restoration | policy hypothesis (defined object) | verified in source; named instantiation §5 | §8.1 |
| CC-A003-005 | Recruitment-suppression mechanism type | mechanism-type definition | typed-flux incidence family verified in source | §8.2 |
| CC-A003-007 | Ungated variant (registry entry) | registered obligation | no equations/parameters/code/outputs in source | §8.3 |
| CC-A003-008 | Gated variant (registry entry) | registered obligation | same registry status | §8.3 |
| CC-A003-009 | Hybrid-effort variant (registry entry) | registered obligation | same registry status | §8.3 |
| CC-A003-010 | Four-state support-pool variant (registry entry) | registered obligation | same; verified content in the A018 rows | §8.3 |
| CC-A003-011 | Two-channel liquidation variant (registry entry) | registered obligation | same; verified content in the A020 rows | §8.3 |
| CC-A003-012 | Stage-structured variant (registry entry) | registered obligation | same; theorem content is the conditional sources' | §8.3 |
| CC-A003-014 | Thermodynamic-tether variant (registry entry) | registered obligation | same registry status; illustrative source equations stated at §8.3 (MS-Native-3) | §8.3 |
| CC-A003-015 | Unified-core variant (registry entry) | registered obligation | same; verified content in the A018 rows; safety-relevance ladder + fold caution the frame | §8.3 |
| CC-A010-015 | Delay crossing near 43 / period 263 | reproduction targets (not numerical propositions) | closures and provenance incomplete; stabilising-sign discipline | §10 |
| CC-A011-017 | Delayed-recruitment registration object | registration requirement | source-declared absent stage registration; response-region outputs the sampled-governance companion's | §2.6 |
| CC-A020-001 | Quota-tracking protective effort law | model definition | calibrated at the Candidate A point | §2.5 |
| CC-A025-003 | 193-dimensional phase-fixed collocation map | formulation definition | correctly dimensioned; phase-value and transversality obligations recorded | App. B.2 |
| CC-A025-007 | Moore–Spence fold formulation (387-dimensional) | formulation/protocol definition | the certification standard the gap rows are measured against | App. B.3 |
| CC-A025-012 | Model-scope boundary (no transfer) | scope statement (counterexample/limit) | inner gated three-state model only | App. B.3, §9 |
| MS-Native-6 | Hocherman implementation-lag caveat (response-lag distribution a lower-bound proxy; implementation-lag dataset absent; measured $\tau$ underestimates total institutional delay) | scope caveat (source-declared) | 101-study synthesis covers response lag, not implementation lag, in DPSIR terminology (A012, §8.1) | §8.1 |
| MS-Native-8 | Reproduction-record run classes 1–2 (life-history anchoring $g\approx1/2/5$ yr, no crossing at default economic settings; broader-search crossings all stabilising, periods $10^3$–$10^4$, no two-crossing window) | reproduction targets (not numerical propositions) | recorded settings and observations in the reproduction record (A010); recovery and registration pending | §10 |

**Table A2. Theorems, propositions, identities, conjectures, counterexamples/limits, numerical records, and examples.**

| Source key | Statement | Status | Proof availability and evidence | Location |
|---|---|---|---|---|
| CC-A001-021 | Scalar delay margin (Hayes): $\dot x=-ax-Bx(t-\tau)$ stable for all $\tau$ if $B\le a$; $\tau_\mathrm{crit}$ with no restabilisation if $B>a$ | theorem | proof + numerical check verified in source | §3.4 |
| CC-A001-097 | $n$-patch super-equilibrium equivalence (cooperative scope; competitive failure) | conjecture | falsification criterion verified in source | §7.6 |
| CC-A002-011 | Non-negative invariance for ordinary, hybrid, and RFDE modes | theorem | proof verified in source | §2.2 |
| CC-A002-027 | Sampled RFDE finite-clopen knowledge kernel (compact single-delay history class) | conditional theorem | source-declared conditional status | §3.4, §6.4 |
| CC-A002-028 | Review-synchronised hybrid RFDE knowledge kernel | conditional theorem | source-declared conditional status | §3.4, §6.4 |
| CC-A002-041 | Small-gain delay-independent stability (Halanay certificate, unique decay rate) | conditional theorem | source-declared conditional status | §7.2 |
| CC-A002-042 | Periodic-orbit-fold persistence under typed coupling | conjecture | declared missing proof + disproof route | §7.6 |
| CC-A002-043 | Variable-time delayed-hybrid information kernel | conjecture | two declared gaps + disproof route | §7.6 |
| CC-A002-044 | Restricted delay-separation principle | conjecture | declared missing proof + disproof route | §7.6 |
| CC-A006-002 | Conditional hybrid history-cone invariance | conditional theorem | proof verified; interval-of-existence + positivity-only scope; superseded-but-preserved vs CC-A002-011 | §2.2 |
| CC-A006-011 | No sign-free delay conclusion | counterexample/limit | two sign-contrast systems named; explicit examples desirable | §3.4 |
| CC-A006-016 | RFDE/hybrid transition persistence | conjecture | class-specific conditions required | §7.6 |
| CC-A010-006 | Periodic-orbit-fold persistence (fold-specific spectral/nondegeneracy conditions) | conjecture | merged family with CC-A002-042 | §7.6 |
| CC-A010-007 | Exergy-gated suppression | conjecture | loop-gain theorem target; model-specific status | §7.5 |
| CC-A012-001 | Forward invariance of the M3-B box | theorem | proof verified (five faces; method of steps) | §2.2 |
| CC-A012-002 | Boundedness and global continuation | corollary | proof verified (variation of constants) | §2.2 |
| CC-A012-003 | Characteristic quasi-polynomial $P-C_ZLe^{-\lambda\tau}=0$ | proposition | proof verified (determinant expansion) | §3.2 |
| CC-A012-004 | Cubic modulus condition and phase branches | theorem | proof verified; simplicity/transversality separate; first Lyapunov coefficients undone in that source | §3.3 |
| CC-A012-006 | Interior equilibrium and stock branch | verified model algebra | full extinction-face classification: the gate-created boundary rest is classified separately from the $r=qE^*$ branch exchange | §3.1 |
| CC-A012-007 | M3-LC equals M3-U while the floor is inactive | identity/theorem | proof verified; excursion divergence demonstrated | §2.3 |
| CC-A012-010 | M3-U thresholds, cycles, folds, basins | numerical result (accepted) | source-stated status; reproducibility archive pending; SNPO classification conjectural | §4.1, §6.2 |
| CC-A012-011 | M3-B thresholds, folds, Floquet, basins | numerical result (accepted) | source-stated status; inferred classifications labelled as such; archive pending | §4.1, §6.2 |
| CC-A012-012 | M3-LC persistence and fixed-demand experiments | numerical result (accepted at stated scope) | first-hitting-time form; inter-locator discrepancy the uncertainty scale | §6.2 |
| CC-A012-013 | M4-A thresholds and turnover boundary | numerical result (accepted) | $\omega_A$ notation throughout; open-relaxation caveat; archive pending | §6.2 |
| CC-A012-014 | MPF Hopf/transient/basin/sweep results | numerical result (accepted) | simplex theorem discharges admissibility; negative screen is a numerical negative result | §6.2 |
| CC-A018-007 | Working and QSS four-state closures | theorems | proofs verified; approximation mapping; $\varepsilon_U$ not small; QSS object distinct | §2.4 |
| CC-A018-008 | Frozen-active-pool finite-time approximation | theorem | proof verified; local/near-equilibrium scope only | §2.4 |
| CC-A018-010 | Local Hopf persistence under residual feedback | conditional (conjecture-grade) | conditional on the Tikhonov conjecture + simple-pair/transversality/no-other-imaginary/Hurwitz conditions; global folds outside | §4.3 |
| CC-A018-011 | Sample-and-hold monodromy | theorem | proof verified; scoped to the Euler review scheme; $T_r^\mathrm{NS}=47.536$, $T_r^{(-1)}=79.143$ | §6.4 |
| CC-A018-013 | Three-state Hopf cubic + interval certificates | theorem + interval certificates | certificates reproduced at repository level (re-execution-verified); local spectrum of $H$ only | §3.3, §4.1, App. B.1 |
| CC-A018-014 | Lyapunov, continuation, Floquet, fold, basin results | numerical results (source-stated) | fold non-certificate discipline; archive pending | §4.2, §6.1 |
| CC-A018-015 | Four-state working-core numerical results | numerical results (source-stated) | frozen-donor quasi-equilibrium discipline; archive pending | §6.3 |
| CC-A018-016 | Stoichiometric identity, general feedback equation, loop-gain/Nyquist/logistic-identification theorems | identity + theorems | proofs verified; signed-memory scope; saturating-gate screen numerical | §7.1–7.4 |
| CC-A020-002 | Candidate protective linear coefficients ($C_E=-0.850336$, $C_Z=-1.661702$) | calibration arithmetic | source-stated numerical status; the sign discipline is the channel-separation object | §2.5 |
| CC-A020-003 | No positive Hopf frequency under quota tracking | theorem | proof verified; zero-root and continuity requirements included | §5.2 |
| CC-A020-004 | Iso-gain sign-flip phase relation | proposition | proof verified; false-reversal hazard recorded | §5.3 |
| CC-A020-005 | Two-delay characteristic identity | theorem | proof verified (third-row expansion) | §4.4 |
| CC-A020-006 | Weighted small-gain theorem | theorem | proof verified (triangle inequality); zero-root/continuity requirements carried | §4.4 |
| CC-A020-007 | Mobilising-weight threshold | conditional corollary | holds under the continuity/common-equilibrium/denominator-nonvanishing/gain-margin hypotheses | §4.4 |
| CC-A020-008 | Protective sample-and-hold monodromy | proposition + sampled numerics | source-stated numerical status; archive action open; the $T_r=2.306$ crossing is the Euler factor's | §5.4 |
| CC-A020-009 | Channel-specific pacing | theorem | proof verified (cites the no-Hopf theorem and the conditional corollary); interpolation hypotheses inherited | §5.5 |
| CC-A025-001 | Inner three-state Hopf cubic algebra (filter-identity reduction) | exact algebra (verified) | derivative identity cross-checked in source | App. B.1 |
| CC-A025-002 | Interval Hopf certificates (gated Candidate A) | interval certificates (accepted) | repository-level reproduction, outputs identical on re-execution; publication archive open | App. B.1, §10 |
| CC-A025-004 | Small-branch continuation ($m=64$) | numerical continuation record (accepted) | residual $\le6\times10^{-14}$; solver bracket, not nonexistence; rebuild re-execution-verified | App. B.2 |
| CC-A025-005 | Last collocation point diagnostics | numerical diagnostic (accepted) | not a continuous-DDE error bound; non-uniqueness caveat | App. B.2 |
| CC-A025-006 | Companion Floquet multiplier evidence | supporting external evidence (not enclosed) | parameter-mismatch caution recorded | App. B.2 |
| CC-A025-008 | Converged Moore–Spence zero | not obtained (counterexample/limit) | fixed-$\tau$ Krawczyk limitation recorded; no promotion | App. B.3 |
| CC-A025-009 | Discrete Krawczyk inclusion | not started/completed (counterexample/limit) | repository fold rebuild agrees (interval stage unimplemented) | App. B.3 |
| CC-A025-010 | Interval transversality and curvature conditions | not completed (counterexample/limit) | left-nullvector enclosure absent | App. B.3 |
| CC-A025-011 | Continuous-DDE bordered radii-polynomial lift | not implemented (counterexample/limit) | discrete/continuous separation stated | App. B.3 |
| CC-A025-013 | Fold certificate headline | not obtained (counterexample/limit) | numerical evidence, not a validated fold theorem | App. B.3, §6, §10 |
| MS-Native-1 | Single-resource deficit identity $qEN-R=-\dot N$ (seam restatement) | identity | one-line proof; restates the interface contract's shared object (ledger row is the ledger companion's CC-A018-004 — cross-reference, not a retained row of this paper) | §9 |
| MS-Native-2 | Non-reduction boundary: no exact dynamic reduction of the closed ledger to the working C4 field | rejected-mapping statement | restates the interface contract's five mathematical reasons (no-rest theorem is the ledger companion's CC-A019-004 — cross-reference, not a retained row of this paper) | §9 |
| MS-Native-3 | Thermodynamic tether: governance-capital state $K_\mathrm{cap}$ with its own dynamics, pole-free gate $1-e^{-K_\mathrm{cap}/K_0}$ (rational-gate pole failure mode), extinction convergence to $(0,\delta,0,0)$, necessary condition $\mu_E<\alpha$, equilibrium-branch saddle-node $\mu_E^\mathrm{SN}\approx5.9\alpha$, institutional Allee effect with basin boundary $E_1^*$ | illustrative worked extension (source-declared illustrative status) | source equations at illustrative parameterisation (A018, §9); no calibration for $\delta_K,c_E,K_0,\mu_E$; registry tabulation obligation stands | §8.3 |
| MS-Native-4 | $\eta=10$ intermittency classification (homoclinic-like slow–fast, not a torus; CV $1.58$, return-map $r=-0.47$, large-amplitude time fraction $0\%\to100\%$) and unified-core pair births (large-delay pair at $\eta_\mathrm{crit}\approx2.337$, $\tau\approx71.2/72.9$; small-delay pair at $\eta\approx2.454$) | inferred numerical classification (source-stated) | three independent diagnostics in the source (A018, §6); no sharp second threshold located | §6.2 |
| MS-Native-5 | Droop nutrient–quota $r$-window robustness (window unchanged; upper edge $\le0.023$ yr$^{-1}$ at $\eta=0.914$; no crossing at $r\ge0.2$ yr$^{-1}$; growth-coupled pool cannot be slow at large $r$) | numerical robustness result (source-stated) | structural reason: quota self-relaxation exactly $r$, pool relaxation growing with throughput (A018, §6 robustness); stage-structured twin in the sampled-governance companion study | §6.2 |
| MS-Native-7 | Ungated Candidate-B upper fold $76.075$ yr with window $(76.075,76.29)$; four-state ungated-B Hopf crossings $6.25$/$76.33$ yr | numerical result (registered values; saddle-node classification open) | registered in the four-state pipeline source (A018, §6); the gated-family no-registration discipline is qualified, not overridden | §6.2 |
| MS-Native-9 | Nominal fold-rebuild values $\tau_f=5.587236198690/5.587236198663/5.587236198663$ at $m=64/96/128$ (cross-resolution agreement $2.7\times10^{-11}$, all inside the interval for which the certificate was never obtained) | nominal numerical values (re-execution-verified at the nominal level; no certificate) | verification-status update (A025); interval Krawczyk stage unimplemented; the fold-certificate family stays not-obtained | App. B.2 |
| MS-Native-10 | Continuous-lift insufficiency reason (Fourier tail of softplus, rational, and gated terms does not vanish at finite support) | protocol statement | certification protocol (A025); a periodic-orbit radii polynomial without the bordered fold equations is insufficient | App. B.3 |
| MS-Native-11 | Two-patch super-equilibrium criterion (kernel nonempty iff componentwise $f_{\min}\ge0$; checkable by grid search or monotone root-finding without the quartic; identical-patch instance exists, asymmetric MSY counterexample has none) | remark — criterion (two-patch instances verified) | source remark (A001, Remark 10.2); the $n$-patch equivalence itself stays the conjecture CC-A001-097 | §7.6 |
| MS-Native-12 | Early-warning diagnostic indicators (critical slowing down, rising variance, epistemic divergence, policy inertia) with the non-universality caveat | scoped remark (source-declared) | valid only near fold bifurcations under additive noise with responsive control; each a separate falsifiable claim (A001, §5.5) | §7.6 |

No status is promoted anywhere in this inventory; the manuscript-native rows MS-Native-1 and -2 restate the interface contract, and MS-Native-3 through -12 restate no-row source content at its source-declared status — none is a new result.

---

# Appendix B. The interval Hopf enclosures and the fold non-certificate

This appendix carries the thirteen bounded-appendix rows of the interval Hopf/fold validation source, stated at their repository-reproduced statuses. The source's two evidentiary levels are kept distinct throughout: the local Hopf calculation is certifiable once the coefficient construction and phase evaluation are enclosed; the periodic-orbit calculation is a high-accuracy collocation computation, not a validated enclosure of a continuous-DDE fold.

## B.1 The Hopf cubic and its interval certificates

With $P(\lambda)=(\lambda-A_N)(\lambda+d)(\lambda-C_E)$ and $L(\lambda)=B_E(\lambda-A_N)+A_EB_N$, the modulus condition gives the explicit cubic

$$
H(x)=(x+A_N^2)(x+d^2)(x+C_E^2)-C_Z^2\bigl[B_E^2x+(A_EB_N-A_NB_E)^2\bigr],
$$

and at the interior equilibrium of the gated inner core the filter identity $A_EB_N-A_NB_E=0$ reduces it to $H(x)=(x+A_N^2)(x+d^2)(x+C_E^2)-C_Z^2B_E^2x$ (exact algebra, verified; derivative identity cross-checked). The delay is the interval evaluation of the phase relation $\tau(\omega)=(-\arg(P(i\omega)/(C_ZL(i\omega)))+2\pi k)/\omega$ at a certified positive root of $H$, not a root of the argument formula.

**Interval Hopf certificates (accepted at source-stated scope; repository-level reproduction).** For gated Candidate A, interval Newton applied to the interval-enclosed coefficient representation certifies simple positive roots in $x=\omega^2$, and branch-safe interval evaluation of the phase relation gives

$$
\tau_-\in[3.6661490142739,\,3.6661490142743],\qquad
\tau_+\in[150.3584773101408,\,150.3584773101421],
$$

with upper-interval width of order $10^{-12}$ yr. The certificate is conditional on the stated interval coefficient and phase-evaluation pipeline, including correct handling of the argument branch; the repository's committed pipeline implements the outward-rounded coefficient/equilibrium/phase construction and reproduces the displayed intervals exactly, with outputs identical on re-execution, discharging that condition at the repository level. The publication-archive obligation remains open. A full independent record must state the interval library, working precision, rounding mode, parameter and equilibrium enclosures, coefficient intervals, and the branch-safe implementation of the argument function — implementation details that are part of an interval certificate, not merely numerical-method metadata.

## B.2 The collocation formulation and the small-branch computation

**Formulation (formulation definition).** With $m=64$ Fourier nodes, $Y\in\mathbb R^{192}$ the coefficients of the three state variables, and $T>0$ the unknown period, the phase-fixed collocation map is $F:\mathbb R^{192}\times\mathbb R\to\mathbb R^{193}$, with the phase equation (an integral phase condition, or the first-sine-coefficient convention of the reported implementation) among the 193 equations, removing the time-translation degeneracy; $D_{(Y,T)}F$ is $193\times193$. The map is a finite-dimensional collocation map; no continuous-DDE truncation bound is implied by its residual. The formulation is correctly dimensioned; the exact first-sine phase value and transversality to time translation are recorded obligations.

**Small-branch continuation (numerical continuation record, accepted).** A Newton–Levenberg–Marquardt solver, initialised from the Hopf normal-form predictor at $\tau=\tau_-+0.05$ and continued with a $\sqrt{\tau-\tau_-}$ predictor, finds one approximate periodic-orbit solution at each sampled $\tau\in[3.716,5.58667]$ with discretised residual $\|F\|_2\le6\times10^{-14}$; the peak-to-peak amplitude of $N$ grows from $1.10$ to $21.80$ and the period from $250.0$ to $313.76$ yr. The solver fails at $\tau=5.590$ under the stated budget with residual $2.8\times10^{-6}$: a solver-success/failure bracket, not a nonexistence result. The repository's rebuilt fold pipeline at $m=64/96/128$ — all three resolutions inside the interval for which the certificate was never obtained — is the same evidentiary class, with executions reproducing the committed artifacts identically. The rebuilt nominal fold values are $\tau_f=5.587236198690$, $5.587236198663$, and $5.587236198663$ at $m=64/96/128$, in cross-resolution agreement to $2.7\times10^{-11}$ and all inside the interval for which the certificate was never obtained (nominal numerical values, re-execution-verified at the nominal level; no certificate).

**Last collocation point (numerical diagnostic, accepted).** At $\tau=5.586666666666667$ the computed orbit satisfies $\|F\|_2=5.43\times10^{-14}$, $\|J^{-1}F\|_2=5.69\times10^{-12}$, with $\sigma_{\min}(J)=4.54\times10^{-7}$ and $\operatorname{cond}_2(J)=1.25\times10^7$; the effort gate and filter floor are inactive ($E=7.93\ll E_{\max}$, $N\ge72.2$). $\|J^{-1}F\|_2$ is the norm of a linearised Newton correction for the finite-dimensional collocation map; it is not a rigorous error bound for the continuous equation or for the fold location. The data do not establish uniqueness of the collocation zero at each $\tau$, and solver failure at $5.590$ does not exclude another zero or family there.

**Companion Floquet evidence (supporting external evidence, not enclosed here).** Independent shooting/Floquet calculations of the companion core give a real nontrivial multiplier changing from approximately $1.0514$ at $\tau=5.584$ to $0.99898$ at $\tau=5.587$ on the corresponding small branch, consistent with a candidate simple turning point. This is not an interval certificate, and the present record does not independently recompute or enclose those multipliers; the parameter-mismatch caution applies ($5.58667$ and the fold-quoted $5.587$ are not the same parameter).

## B.3 The fold-certificate gap family

**The certification standard (formulation/protocol definition).** A practical validated fold computation uses the Moore–Spence system: with a right nullvector $v\in\mathbb R^{193}$ and normalisation $\ell$,

$$
\mathcal M(Y,T,\tau,v)=\bigl(F(Y,T;\tau),\ J(Y,T;\tau)v,\ \ell^\top v-1\bigr)=0,
$$

$387$ unknowns and equations; a validated Krawczyk or interval-Newton inclusion would establish a unique fold of the $m=64$ collocation equations inside the resulting box. For a simple fold one should additionally enclose a left nullvector $w$ and verify the nondegeneracy conditions $w^\top F_\tau\not\ni0$ and $w^\top D^2F[v,v]\not\ni0$ with the phase condition regular; a pseudo-arclength system continues through the turn but does not by itself certify fold nondegeneracy.

**The gap, component by component.** The converged Moore–Spence zero: **not obtained**; a preliminary fixed-$\tau$ Krawczyk construction based on an inverse of $J$ does not provide a contracting free-$\tau$ enclosure near the ill-conditioned turning region — a limitation of that formulation, not an exclusion of the fold. The discrete Krawczyk inclusion: **not started/completed**. The interval transversality and curvature conditions: **not completed**. The continuous-DDE bordered radii-polynomial lift (a validated Moore–Spence or pseudo-arclength fold computation followed by a Fourier-tail or function-space error bound): **not implemented**; the discrete collocation proof and the continuous-RFDE proof are correctly separated. The insufficiency is structural: the tail of $f(U,SU)$ does not vanish merely because $U$ has finite Fourier support — softplus, rational terms, and gated products generate infinitely many modes — so a periodic-orbit radii polynomial without the bordered fold equations is insufficient for the lift (protocol statement). The repository's nominal fold rebuild does not alter these statuses: three collocation resolutions place the turning region inside the interval for which the certificate was never obtained, and the interval Krawczyk stage remains unimplemented.

**Headline status (counterexample/limit).** The fold certificate is **not obtained**. The computations support — but do not interval-certify — a small-branch turning point near $\tau\approx5.587$; the fold statement is numerical evidence, not a validated fold theorem.

**Model-scope boundary (counterexample/limit).** All fold and branch statements in this appendix concern the gated inner three-state equation and its $m=64$ collocation discretisation only. No transfer is claimed to the turnover-corrected working four-state core, the finite-donor primitive system, the vector Liebig system, the stage-structured models, or the spatial system; the lower termination of the attracting large-cycle family and the upper-window periodic families are not analysed here. This is the architecture's no-transfer rule instantiated at the named-dynamics level and cited together with the ledger seam discipline of §9.

---

# References

Åström, K. J., and Wittenmark, B. 1997. *Computer-Controlled Systems: Theory and Design*. Third edition. Prentice Hall, Upper Saddle River, New Jersey.

Beretka, S., and Vas, G. 2020. Saddle-node bifurcation of periodic orbits for a delay differential equation. *Journal of Differential Equations* 269: 4215–4252.

Carpenter, S. R., Cole, J. J., Pace, M. L., Batt, R., Brock, W. A., Cline, T., Coloso, J., Hodgson, J. R., Kitchell, J. F., Seekell, D. A., Smith, L., and Weidel, B. 2011. Early warnings of regime shifts: a whole-ecosystem experiment. *Science* 332: 1079–1082.

Cloud, M. J., Moore, R. E., and Kearfott, R. B. 2009. *Introduction to Interval Analysis*. SIAM, Philadelphia.

Costantino, R. F., Cushing, J. M., Dennis, B., and Desharnais, R. A. 1995. Experimentally induced transitions in the dynamic behaviour of insect populations. *Nature* 375: 227–230.

Descartes, R. 1637. *La Géométrie*. In *Discours de la méthode pour bien conduire sa raison, et chercher la vérité dans les sciences*. Ian Maire, Leiden.

Diekmann, O., van Gils, S. A., Verduyn Lunel, S. M., and Walther, H.-O. 1995. *Delay Equations: Functional-, Complex-, and Nonlinear Analysis*. Springer, New York.

Droop, M. R. 1973. Some thoughts on nutrient limitation in algae. *Journal of Phycology* 9: 264–272.

Engelborghs, K., Luzyanina, T., and Roose, D. 2002. Numerical bifurcation analysis of delay differential equations using DDE-BIFTOOL. *ACM Transactions on Mathematical Software* 28: 1–21.

Ezekiel, M. 1938. The cobweb theorem. *Quarterly Journal of Economics* 52: 255–280.

Faria, T., and Magalhães, L. 1995. Normal forms for retarded functional differential equations with parameters and applications to Hopf bifurcation. *Journal of Differential Equations* 122: 181–200.

Gao, X., and Zhang, Y. 2022. Bifurcation analysis and optimal control of a delayed single-species fishery economic model. *Mathematical Biosciences and Engineering* 19: 8081–8106.

Guckenheimer, J., and Holmes, P. 1983. *Nonlinear Oscillations, Dynamical Systems, and Bifurcations of Vector Fields*. Springer, New York.

Gurney, W. S. C., Blythe, S. P., and Nisbet, R. M. 1980. Nicholson's blowflies revisited. *Nature* 287: 17–21.

Halanay, A. 1966. *Differential Equations: Stability, Oscillations, Time Lags*. Academic Press, New York.

Hale, J. K. 1977. *Theory of Functional Differential Equations*. Springer, New York.

Hale, J. K., and Verduyn Lunel, S. M. 1993. *Introduction to Functional Differential Equations*. Springer, New York.

Hassard, B. D., Kazarinoff, N. D., and Wan, Y.-H. 1981. *Theory and Applications of Hopf Bifurcation*. Cambridge University Press, Cambridge.

Hayes, N. D. 1950. Roots of the transcendental equation associated with a certain difference-differential equation. *Journal of the London Mathematical Society* 25: 226–232.

Hocherman, T., Trop, T., and Ghermandi, A. 2025. Time lags in environmental governance: a critical review. *Ambio* 54: 2042–2059.

Hurwitz, A. 1895. Über die Bedingungen, unter welchen eine Gleichung nur Wurzeln mit negativen reellen Teilen besitzt. *Mathematische Annalen* 46: 273–284.

Kearfott, R. B. 1996. *Rigorous Global Search: Continuous Problems*. Kluwer, Dordrecht.

Keller, H. B. 1977. Numerical solution of bifurcation and nonlinear eigenvalue problems. In Rabinowitz, P. H. (ed.), *Applications of Bifurcation Theory*, pp. 359–384. Academic Press, New York.

Khiyar, S., Hafdane, M., Boutayeb, H., and Elberrai, I. 2026. Qualitative dynamics and optimal control of a delayed algae–fish bioeconomic system with nitrate recycling. *Frontiers in Applied Mathematics and Statistics* 12: 1795340.

Krawczyk, R. 1969. Newton-Algorithmen zur Bestimmung von Nullstellen mit Fehlerschranken. *Computing* 4: 187–201.

Kuznetsov, Y. A. 2004. *Elements of Applied Bifurcation Theory*. Third edition. Springer, New York.

Ludwig, D., Jones, D. D., and Holling, C. S. 1978. Qualitative analysis of insect outbreak systems: the spruce budworm and forest. *Journal of Animal Ecology* 47: 315–332.

Moore, G., and Spence, A. 1980. The calculation of turning points of nonlinear equations. *SIAM Journal on Numerical Analysis* 17: 567–576.

Moore, R. E. 1979. *Methods and Applications of Interval Analysis*. SIAM, Philadelphia.

Moxnes, E. 1998. Not only the tragedy of the commons: misperceptions of bioeconomics. *Management Science* 44: 1234–1248.

Neimark, J. 1959. Some cases of the dependence of periodic motions on parameters. *Doklady Akademii Nauk SSSR* 129: 736–739.

Ostrom, E. 1990. *Governing the Commons: The Evolution of Institutions for Collective Action*. Cambridge University Press, Cambridge.

Routh, E. J. 1877. *A Treatise on the Stability of a Given State of Motion*. Macmillan, London.

Sacker, R. J. 1964. On invariant surfaces and bifurcation of periodic solutions of ordinary differential equations. *New York University Courant Institute IMM-NYU 333*.

Scheffer, M. 2009. *Critical Transitions in Nature and Society*. Princeton University Press, Princeton.

Scheffer, M., Bascompte, J., Brock, W. A., Brovkin, V., Carpenter, S. R., Dakos, V., Held, H., van Nes, E. H., Rietkerk, M., and Sugihara, G. 2009. Early-warning signals for critical transitions. *Nature* 461: 53–59.

Scheffer, M., and Carpenter, S. R. 2003. Catastrophic regime shifts in ecosystems: linking theory to observation. *Trends in Ecology & Evolution* 18: 648–656.

Programme sources. The research programme's statement inventory (the 409-row source-to-canonical mapping), its row-closure verification record and row-level evidence table, the ledger-to-dynamics interface contract, and the five-paper publication architecture, together with the source corpus (A001–A025), are committed to the project repository at <https://github.com/MIKEAA2020/general-sustainability>; the statement-level listing is §11 and Appendix A of this article.

---

# Data and code availability

The interval-Hopf certificates are deterministic, re-execution-verified computations. The committed interval pipeline — the research programme's interval-Newton Hopf-certificate runner script, part of its validated-computations artifact set — reproduces the displayed Candidate A intervals exactly, with outward-rounded float64 via nextafter, interval transcendentals at 50-digit working precision, branch-safe interval atan2, and simple-root and transversality sign checks (the lower crossing stabilising, the upper destabilising); the outputs are identical on re-execution. The nominal fold rebuild at three collocation resolutions ($m=64/96/128$) is likewise re-execution-verified at the nominal level, its executions reproducing the committed artifacts identically; the interval Krawczyk stage is unimplemented. The publication-artifact archives for the source-stated numerical families (branch, Floquet, history, solver, and environment artifacts, and the sampled-numerics documentation action) are registered as open obligations, and the reproduction targets of §10 are not numerical propositions. The computational record — the runner scripts, the statement inventory with its per-row verification record and row-level evidence table, and the ledger-to-dynamics interface contract — is available in the research programme's public repository at <https://github.com/MIKEAA2020/general-sustainability>; an anonymized copy of the full artifact set is available for double-anonymous review.

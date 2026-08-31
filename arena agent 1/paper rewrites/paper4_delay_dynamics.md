# Delay-Induced Regime Change in Harvested Stocks: The Mobilising and Protective Channels of Institutional Feedback, and the Review Interval as Control

## Abstract

Classical delay studies place lags in the ecological dynamics of harvested populations; here the delay sits in the governance loop that converts observed stock decline into institutional response. A gated three-state model (stock, filtered deficit memory, deployed effort) responds to a delayed decline signal, and two effort laws of opposite sign structure are contrasted: a mobilising law whose gain grows with deployed effort, and a protective quota-tracking law whose gain restores. A complete cubic modulus condition is proved for the characteristic quasi-polynomial; a filter identity makes the cross term vanish identically, so positive roots occur in even pairs. For the mobilising channel, the two Hopf crossings are certified by interval Newton with outward rounding (τ− ∈ [3.6661490142739, 3.6661490142743] yr, τ+ ∈ [150.3584773101408, 150.3584773101421] yr); both are subcritical (ℓ1 = +5.75×10⁻⁵ and +3.55×10⁻⁴), and delay opens a phase-stabilised window in an undelayed-unstable system. For the protective channel we prove a no-Hopf theorem: Descartes and Routh–Hurwitz exclude every imaginary root, the loop gain peaks at 0.08011 < 1, and exponential stability holds for every delay. Under sample-and-hold review the channels separate again: annual protective review is stable (ρ = 0.9838), its instability threshold near T_r = 2.3 yr being a discretisation artefact; annual mobilising review is unstable (ρ = 1.00055) and restabilises only through a Neimark–Sacker crossing at T_r = 47.536 yr — for a slow stock under periodic review, the control is the review interval. Global numerics give a five-regime attractor topology with a two-fold lower boundary whose saddle-node classification is left provisional.

**Keywords:** delay differential equations; Hopf bifurcation; sample-and-hold control; harvested populations; institutional feedback; interval arithmetic

---

## 1. Introduction

### 1.1 Delays in the governance loop

Delayed feedback has a long history in resource dynamics. Hutchinson (1948) showed that a delayed self-limitation term destabilises logistic growth; Ezekiel (1938) documented the two-year lag between price signals and supply response in the pork cycle; Ludwig, Jones, and Holling (1978) placed delays and hysteresis at the centre of outbreak dynamics; Gurney, Blythe, and Nisbet (1980) gave the canonical stability analysis of the single-species delayed logistic equation; and Costantino et al. (1995) demonstrated delayed-feedback cycles in controlled laboratory populations. A large contemporary literature continues this line with delays placed in the ecological dynamics themselves — maturation, gestation, and age-selective harvesting (Zhang, Shen, and Chen, 2013; Gao and Zhang, 2022; Khiyar et al., 2026).

The delay studied in this paper sits elsewhere: in the *institutional* loop. Stock assessment produces a signal of decline; the signal is filtered into a deficit memory; the memory drives a change in deployed extraction effort — with a deployment delay between decision and action. The behavioural basis of such lags is documented: decision makers in renewable-resource experiments systematically misperceive the dynamics of the systems they govern, responding too slowly and in the wrong functional form (Moxnes, 1998), and institutional design determines which signals reach which actors at which time (Ostrom, 1990). What the dynamical-systems literature has not supplied is an analysis of what this delay *does* to the stability of a harvested-stock system when the delay sits in the governance controller rather than in the ecology — in particular, whether the sign structure of the feedback law (mobilising versus protective) selects between qualitatively different bifurcation behaviour, and what happens when the delay is replaced by periodic review (sample-and-hold).

### 1.2 Contributions

1. **A gated three-state core.** A stock–memory–effort system (Section 2) in which a multiplicative saturation gate enforces the effort boundary exactly, making the admissible box forward invariant (Theorem 1). The model is a mathematical parameterisation, not a calibration to a named fishery; two reference parameter sets (Candidates A and B) serve as sensitivity anchors.

2. **The complete Hopf cubic and the even-pairs algebra.** The characteristic quasi-polynomial of the linearisation is reduced to a cubic modulus condition with a phase relation (Theorem 2); at the interior equilibrium a filter identity makes the cross term of the cubic vanish identically, so positive roots occur in even pairs, zero or two — never one or three (Corollary 1). The two-crossing structure of the architecture is thereby an algebraic fact, not a numerical accident.

3. **Interval-certified crossings.** The two Hopf delays of the mobilising channel are certified by interval Newton on the cubic with outward rounding: τ− ∈ [3.6661490142739, 3.6661490142743] yr and τ+ ∈ [150.3584773101408, 150.3584773101421] yr at Candidate A (Section 4.1). The certification tier is stated precisely: the enclosures certify the *local spectrum* of the cubic; the method of Church and Lessard (2022), which certifies full Hopf bifurcation for retarded functional differential equations, is the stronger standard and is not claimed here.

4. **The sign separation.** The mobilising law (gain growing with deployed effort, C_Z > 0) and the protective quota-tracking law (restoring gain, C_Z < 0) yield opposite local mathematics on the same stock–memory block: the mobilising channel carries the Hopf pair, both crossings subcritical (Section 4.2); the protective channel carries a **no-Hopf theorem** — all cubic coefficients positive, Descartes' rule and Routh–Hurwitz exclude every imaginary root, and the loop gain peaks at 0.08011 < 1 — so exponential stability holds for every delay (Theorem 3). The two channels are interpolated, and a weighted small-gain theorem plus a conditional weight threshold show that delay-induced instability requires a sufficiently large mobilising weight (Section 4.4).

5. **The review interval as control.** Under sample-and-hold review with one explicit Euler step per period, the monodromy is computed in closed form (Theorem 4). The protective channel is stable under annual review (ρ = 0.9838), and its instability threshold at T_r ≈ 2.306 yr is a discretisation artefact of the Euler factor 1 + T_r C_E — provably not a Hopf of the continuous system (Section 6.2). The mobilising channel is unstable under annual review (ρ = 1.00055) and restabilises only through a Neimark–Sacker crossing at T_r = 47.536 yr, with a period-doubling multiplier at 79.143 yr: for a slow stock under periodic review, the control is the review interval, and the continuous-delay recommendation does not transfer to periodic review (Section 7).

6. **Global numerics at declared status.** Continuation, Floquet-multiplier tracking, and basin tests give a five-regime attractor topology. The lower boundary of the cycle is resolved into two distinct folds of two distinct families — basin collapse in τ ∈ [5.574, 5.576] yr versus a small-branch fold near 5.587 yr, with the large branch's multiplier still at 0.964 < 1 through τ = 5.5815 — and the saddle-node-of-periodic-orbits classification is left provisional against a crisis alternative (Section 8). Rigorous saddle-node results for delay equations exist for specific classes (Beretka and Vas, 2020); none is claimed here.

### 1.3 Organization

Section 2 defines the model class and its admissible domain. Section 3 derives equilibria and the characteristic equation. Section 4 develops the Hopf cubic and the even-pairs algebra. Section 5 analyses the mobilising channel. Section 6 analyses the protective channel. Section 7 treats sample-and-hold review. Section 8 reports the global numerics and their certification levels. Section 9 unifies the two channels in the loop-gain family. Section 10 discusses design consequences, relation to the early-warning literature, and open problems. Section 11 concludes.

---

## 2. The Model Class

Throughout, $N$ is a renewable stock (material or biomass units), $Z$ a filtered deficit-memory state (stock per time), and $E$ an extraction effort — a dimensionless institutional deployment intensity, not a conserved material or energy stock. The catchability $q$ has units (effort·yr)⁻¹; the signal references $\Delta_{\mathrm{ref}}$, $Z_{\mathrm{ref}}$ and the offset $\delta$ have stock-per-time units; $\eta$ and $\delta_0$ have yr⁻¹ and effort-per-time units. These assignments make each equation dimensionally homogeneous without treating effort as physical mass. The delay $\tau$ is a discrete action/deployment delay; the filter timescale $\tau_m$ is an ordinary state relaxation time, not a second delay.

### 2.1 The gated three-state core

Let
$$S(N) = rN\left(1 - \frac{N}{K}\right), \qquad \mathrm{sp}_k(s) = \frac{1}{k}\log(1 + e^{ks}), \qquad \Phi_k(s) = \max\left\{0,\ \mathrm{sp}_k(s) - \frac{\log 2}{k} + \delta\right\},$$
where $\Phi_k$ is a shifted, non-negative signal map. The boundary-exact (gated) three-state core is
$$\begin{aligned}
\dot N &= S(N) - qEN, \\
\dot Z &= \frac{1}{\tau_m}\bigl[\Phi_k(qEN - S(N)) - Z\bigr], \\
\dot E &= \left(1 - \frac{E}{E_{\max}}\right)\left[\eta E\left(\frac{Z(t-\tau)}{\Delta_{\mathrm{ref}}} - \frac{E}{E_{\max}}\right) + \delta_0\frac{Z(t-\tau)}{Z_{\mathrm{ref}} + Z(t-\tau)}\right].
\end{aligned} \tag{1}$$

The memory input is a smoothed version of the stock-decline rate: on this core the identity $qEN - S(N) = -\dot N$ holds exactly, so $\Phi_k$ filters $-\dot N$. The multiplicative gate $(1 - E/E_{\max})$ is load-bearing — a hard saturation architecture, not a generic effort law: it enforces $E \in [0, E_{\max}]$ by construction. The registered parameterisations:

| Parameter | Candidate A | Candidate B | Role |
|---|---|---|---|
| $r$ | 0.02 | 0.02 | yr⁻¹; stock renewal |
| $K$ | 100 | 100 | stock units; normalisation |
| $q$ | 0.001 | 0.001 | (effort·yr)⁻¹ |
| $\eta$ | 0.914 | 2.756 | yr⁻¹; effort response |
| $E_{\max}$ | 30 | 26 | effort units; saturation boundary |
| $\Delta_{\mathrm{ref}}$ | 1.0 | 1.0 | stock yr⁻¹; signal scale |
| $\delta_0$ | 0.01 | 0.01 | effort yr⁻¹; baseline source |
| $\tau_m$ | 5 | 5 | yr; filter relaxation |
| $Z_{\mathrm{ref}}$ | 1.0 | 1.0 | stock yr⁻¹; signal scale |
| $\delta$ | $\log 2/10$ | $\log 2/10$ | stock yr⁻¹; signal offset |
| $k$ | 10 | 10 | (stock yr⁻¹)⁻¹; regularisation |
| $\tau$ | varied | varied | yr; action/deployment delay |

These are mathematical parameterisations and sensitivity anchors, not a joint calibration to a named resource or institution; the institutional coefficients have not been independently identified from a field system. Candidates A and B are two points in the effort-response chart, not rescalings of one class. For the reported pair $\delta = \log(2)/k$ the outer floor cancels algebraically ($\Phi_k(s) = \mathrm{sp}_k(s) > 0$ for every finite $s$), so the floor is inactive on every reported periodic orbit; the identity is parameter-specific, and for $\delta \ne \log(2)/k$ floor contact must be checked orbit by orbit.

### 2.2 Admissibility

**Theorem 1 (Forward invariance of the admissible box).** *For the history class $\varphi \in C([-\tau, 0], \mathbb{R}^3)$ define*
$$\mathcal{D} = \{ 0 \le N \le K,\ Z \ge 0,\ 0 \le E \le E_{\max} \}.$$
*If the initial history lies in $\mathcal{D}$ — every history value, not only the endpoint — then every classical solution of (1) remains in $\mathcal{D}$ for as long as it exists.*

*Proof.* Check the five boundary faces. (i) $N = 0$: $S(0) = 0$ and the harvest $qEN$ vanishes, so $\dot N = 0$; the face is invariant. (ii) $N = K$: $S(K) = 0$, so $\dot N = -qEK \le 0$, inward. (iii) $Z = 0$: the source $\Phi_k(qEN - S(N)) \ge 0$ by construction of the non-negative signal map, so $\dot Z = \Phi_k(\cdot)/\tau_m \ge 0$, inward. (iv) $E = 0$: the gate factor is positive (away from $E = E_{\max}$) and the bracket is $\delta_0 Z_\tau/(Z_{\mathrm{ref}} + Z_\tau) \ge 0$, so $\dot E \ge 0$, inward. (v) $E = E_{\max}$: the gate vanishes, $\dot E = 0$, face invariant. Because the delay enters only through $Z(t - \tau)$, and the initial history lies in $\mathcal{D}$, the delayed argument is non-negative throughout the first interval $[0, \tau]$, making the vector field subtangential on the first interval by (i)–(v); the argument repeats by induction over $[n\tau, (n+1)\tau]$ by the method of steps (Hale and Verduyn Lunel, 1993); at $\tau = 0$ the same faces give subtangentiality of the ordinary differential equation directly. $\square$

**Corollary 1 (Boundedness and global continuation).** *With $\bar Z = \max\{ \sup_{[-\tau,0]} Z,\ \Phi_k(qE_{\max}K) \}$, every solution satisfies $0 \le Z(t) \le \bar Z$, all three states remain in a bounded set on which the vector field is locally Lipschitz, and the solution continues for all $t \ge 0$.*

*Proof.* The $Z$-equation reads $\dot Z = d(\nu(t) - Z)$ with $d = 1/\tau_m$ and the monotone bounded input $\nu(t) = \Phi_k(qE(t)N(t) - S(N(t))) \le \Phi_k(qE_{\max}K)$; variation of constants gives $Z(t) = e^{-dt}Z(0) + d\int_0^t e^{-d(t-s)}\nu(s)\,ds \le e^{-dt}Z(0) + \bar Z(1 - e^{-dt})$, hence $Z(t) \le \max\{Z(0), \bar Z\} \le \bar Z$ by the definition of $\bar Z$. Nonnegativity of $Z$ is part of Theorem 1. With $N \in [0,K]$, $E \in [0, E_{\max}]$, and $Z \in [0, \bar Z]$, the state lies in a compact set on which the right-hand side of (1) is locally Lipschitz (the logistic, the smooth signal map, and the polynomial effort law are all $C^1$ there), so the solution extends for all time. On the invariant extinction face $N = 0$ the memory input is $\Phi_k(0) = \delta$, so $Z$ relaxes to $\delta$ and the extinction rest carries the same admissible positive effort root as the interior branch: institutional memory sustains baseline commanded effort against zero realised harvest. Effort is an institutional deployment intensity, not a conserved stock; the core makes no closed-effort-energetics claim, and a materially closed application must add and donor-limit that support explicitly. $\square$

### 2.3 The registered model family

Four variants delimit the robustness of the results; no invariant set, equilibrium formula, local threshold, periodic branch, or admissibility result transfers between them without a separate argument.

- **M3-U (ungated).** The same ecology with the effort law without the outer gate; $E_{\max}$ is then a self-limitation scale only. The gate factor is the algebraic source of threshold relocation between the variants (Section 3.2).
- **M3-LC (two-channel stock law).** The logistic renewal is written as a gross birth–mortality decomposition $B(N) = S(N) + \kappa rN$, $M(N) = \kappa rN$ ($\kappa \ge 0$), and the pressure $qEN$ is split by $\psi \in [0,1]$:
$$\dot N = \max\{0,\ B(N) - (1-\psi)qEN\} - M(N) - \psi qEN. \tag{2}$$
Here $\psi qEN$ is a realised removal of standing stock and $(1-\psi)qEN$ is demographic suppression — a prevented inflow, not a material transfer out of the adult-stock compartment; (2) is a phenomenological stock equation, not a closed mass ledger. Whenever the recruitment floor is inactive, (2) reduces exactly to $\dot N = S(N) - qEN$; the floor never binds at the interior equilibrium (the binding condition reduces to $-\psi S(N) > \kappa rN$, impossible), so the equilibrium, the Jacobian, the characteristic equation, and both Hopf points are independent of $\psi$ and $\kappa$. Local equality does not imply excursion equality: the floor truncates recruitment on large excursions, and the two channels diverge there (Section 8).
- **M4-A (active-pool extension).** Logistic renewal is replaced by $R(N,A) = rN(1 - N/K)\, A/(A + A_0)$ with a dynamic active-support pool $\dot A = -B(N,A) + \omega_A(A^{\mathrm{eq}} - A)$ and a fully declared donor-limited gross draw $B$. The relaxation term makes this a reduced open-pool model unless its donor/receiver reservoir is included explicitly; freezing $A$ is not a justified fast-variable elimination at the baseline $\omega_A = 10^{-3}$ yr⁻¹.
- **MPF (primitive-flux core).** Living biomass $X$, detritus $U$, active material $A = \mathcal{M} - X - U$, primitive fluxes $g(X,A) = \mu XA/(K_A + A)$, $m(X) = dX + cX^2$, $h(X,E) = qEX$, signed memory $\dot Z = (-\dot X - Z)/\tau_m$, and the bounded effort law $\dot E = (1 - E/E_{\max})[\eta E Z(t-\tau)/\Delta_{\mathrm{ref}} + \delta_0 - \eta E^2/E_{\max}]$. The core has a signed zero-equilibrium memory ($Z^* = 0$, a true constant baseline), detritus, and a different effort equilibrium; it is not (1). On the boundary $X + U = \mathcal{M}$ the active pool is $A = 0$ and $g(X,0) = 0$, so $\frac{d}{dt}(X+U) = -qEX - \gamma_U U \le 0$, which — with $g(0,A) = 0$, $m(0) = 0$, and the donor-limited flux assumptions — proves forward invariance of the simplex $\{X \ge 0,\ U \ge 0,\ X + U \le \mathcal{M}\}$ for the ecological subsystem under admissible effort.

### 2.4 The four-state working core and its relation to (1)

The working four-state core restores the active abiotic pool as a state: $\dot N = R(N,A) - qEN$, $\dot A = -B(N,A) + \omega_A(A^{\mathrm{eq},W} - A)$ with $A^{\mathrm{eq},W} = A^{\mathrm{eq,intrinsic}} + \kappa_A K/\omega_A$, and the $Z$ and $E$ equations of (1) unchanged except that $S(N)$ is replaced by $R(N,A)$. At the baseline $\omega_A = 10^{-3}$ yr⁻¹, $\kappa_A = 0.05$ yr⁻¹, $A_0 = 0.01K$, $A^{\mathrm{eq,intrinsic}} = 0.5K$, so $A^{\mathrm{eq},W} = 5050$. Two closure statements fix its status. First, in the ideal large-reservoir limit $\sigma_{\mathrm{geo}} = 1$ the specialised system satisfies the working-core equations exactly (an algebraic identity check), with detritus a driven auxiliary that does not feed back; for finite geological reservoirs the vector field is perturbed by $O(1 - \sigma_{\mathrm{geo}})$ and $U$ feeds back. Second, detritus slaving under a fixed intrinsic target is an $O(\varepsilon_U)$ singular-perturbation estimate on compact intervals (a standard Tikhonov/Fenichel-type argument; Hale and Verduyn Lunel, 1993, Ch. 9, Diekmann et al., 1995) — and at the baseline $\gamma_U/r = 10$, so $\varepsilon_U$ is *not* small and the estimate does not control global periodic orbits. At Candidate A the quasi-steady (QSS) core has a positive low-$A$ equilibrium $(N^*, A^*) \approx (23.85, 0.159)$ and no high-$A$ near-logistic exploited equilibrium (the high-stock branch gives $A^* \approx -137$, inadmissible). The QSS core is a distinct singular-limit object: a valid limit that is not dynamically connected to the high-$A$ working equilibrium used for the reported thresholds, and the two objects are never merged. The working core is declared as an open projection: omitted turnover is routed to a diagnostic detritus/inert sink; the reduced $(N,A,Z,E)$ trajectory is not mass-closed by itself; and its global periodic results are model-version-specific. The working equilibrium is a frozen-donor quasi-equilibrium sustained by geological support of order $\omega_A(A^{\mathrm{eq},W} - A^*) \approx 4.652$ stock units yr⁻¹, whose cumulative donor change is $4.652\,T/A^{\mathrm{geo}}$ — 1.2% on a century horizon at the lower geological ratio $A^{\mathrm{geo}}/A^* = 10^2$ and 0.12% at $10^3$.

The finite-time connection between the four-state and three-state cores is the following bound, which justifies using (1) for local, near-equilibrium questions on institutional timescales — in particular the location of $\tau_-$, whose 3.2% shift under restoration of $A$ lies inside the bound — but not the large-amplitude cycle or its period.

**Proposition 1 (Frozen-active-pool approximation).** *Let $(N, Z, E)$ solve (1) and let $(\tilde N, \tilde Z, \tilde E)$ solve the four-state core from the same initial data, with $A(0) \ge A_{\min} > 0$ and $|\dot A| \le V_A$ on $[0,T]$. If the vector field of (1) is Lipschitz with constant $L$ on the admissible domain, then*
$$\sup_{t \in [0,T]} \big( |\tilde N - N| + |\tilde Z - Z| + |\tilde E - E| \big) \le C_T \left( \frac{A_0}{A_{\min}} + V_A T \right)$$
*with $C_T = C e^{LT}$ and a structural constant $C$. This is an inner approximation on $[0,T]$, not a Tikhonov reduction.*

*Proof.* The four-state renewal differs from the saturated renewal by
$$R(N, A(t)) - S(N) = rN\left(1 - \frac{N}{K}\right)\left( \frac{A(t)}{A(t) + A_0} - 1 \right) = -rN\left(1 - \frac{N}{K}\right)\frac{A_0}{A(t) + A_0},$$
so the mismatch is bounded by $rK \cdot A_0/A_{\min}$ pointwise. Write the differences $\Delta N = \tilde N - N$, $\Delta Z = \tilde Z - Z$, $\Delta E = \tilde E - E$. The $Z$ and $E$ equations of the two cores coincide in form, so their difference equations are driven only by $\Delta N$ and by the renewal mismatch $\sigma(t) = R(\tilde N, A(t)) - S(\tilde N)$, with $|\sigma(t)| \le rK\, A_0/A_{\min}$. Lipschitz continuity of the common vector field gives, for the stacked difference vector $\xi$, the differential inequality $|\dot\xi| \le L|\xi| + rK\, A_0/A_{\min} + L V_A t$ (the last term from $|\dot A| \le V_A$ entering through the $A$-dependence of $R$); Gronwall's lemma then yields $|\xi(t)| \le e^{LT}|\xi(0)| + e^{LT}[\, rK A_0/A_{\min}\cdot t + \tfrac12 L V_A t^2 \,] \le C e^{LT}(A_0/A_{\min} + V_A T)$ on $[0,T]$ for a structural constant $C$ depending on $r$, $K$, $L$, and $T$; identical initial data give $\xi(0) = 0$. $\square$

### 2.5 The protective channel and the two-channel interpolation

A protective institution is the quota-tracking law
$$\dot E = \left(1 - \frac{E}{E_{\max}}\right) \eta_p \bigl( E_{\mathrm{cap}}(Z(t - \tau_p)) - E \bigr), \tag{3}$$
where $E_{\mathrm{cap}}$ is $C^2$, positive, strictly decreasing, with the calibration $E_{\mathrm{cap}}(Z) = E_0 Z_{\mathrm{ref}}/(Z_{\mathrm{ref}} + Z)$ and $E_0 = E^*_A(Z_{\mathrm{ref}} + \delta)/Z_{\mathrm{ref}}$. The calibration places the unique interior rest of (3) on the stock–memory block of (1) at the Candidate A point $(N^*, Z^*, E^*) = (89.55188, \delta, 2.08962)$, so the stock–memory block is identical to (1)'s and only the effort law changes. At that rest, $E_{\mathrm{cap}}(\delta) = E^*$ and the linear gains are
$$C_E = -\left(1 - \frac{E^*}{E_{\max}}\right)\eta_p, \qquad C_Z = \left(1 - \frac{E^*}{E_{\max}}\right)\eta_p E_{\mathrm{cap}}'(\delta),$$
which at $\eta_p = \eta_A = 0.914$ give $C_E = -0.850336$ and $C_Z = -1.661702$ — both signs those of a restoring quota, not of scarcity mobilisation; the mobilising counterpart of (1) at the same point has $C_Z = +1.785$ and $C_E = -0.0595$ (Section 3.2). The channel-separation object of this paper is exactly this sign discipline.

The two-channel interpolation replaces the effort law by
$$\dot E = \left(1 - \frac{E}{E_{\max}}\right)\left[ \chi_m F_m(E, Z(t-\tau_m)) + \chi_p \eta_p \bigl( E_{\mathrm{cap}}(Z(t-\tau_p)) - E \bigr) \right], \tag{4}$$
with $\chi_m, \chi_p \ge 0$; the pure mobilising channel is $(\chi_m, \chi_p) = (1, 0)$, pure protection $(0, 1)$.

---

## 3. Equilibria and the Characteristic Equation

### 3.1 The interior equilibrium and the extinction face

At any interior equilibrium $qE^*N^* = S(N^*)$, the signal argument vanishes, the floor is inactive, and
$$Z^* = \Phi_k(0) = \delta,$$
independent of $\tau_m$, $k$, and $(N^*, E^*)$. Substituting into $\dot E = 0$ (away from $E = E_{\max}$) produces
$$-\frac{\eta}{E_{\max}}(E^*)^2 + \eta\frac{\delta}{\Delta_{\mathrm{ref}}}E^* + \delta_0\frac{\delta}{Z_{\mathrm{ref}} + \delta} = 0,$$
whose constant term is positive and quadratic coefficient negative, so there is exactly one positive root; admissibility requires $0 < E^* < \min\{E_{\max}, r/q\}$, and then $N^* = K(1 - qE^*/r)$, positive iff $qE^* < r$. The equilibrium is independent of $\tau$ and $k$, which does not make its stability delay-independent. At Candidate A, $N^* \approx 89.55$, $E^* \approx 2.090$, $Z^* = \delta \approx 0.0693$.

On the extinction face $N = 0$ the same zero raw signal gives $Z = \delta$, and the gated law has both the interior-effort extinction rest $(0, \delta, E^*)$ (when the interior root is admissible) and the boundary rest $(0, \delta, E_{\max})$ created by the multiplicative gate. The stock-direction eigenvalue at either branch is $r - qE$; the interior positive-stock branch exchanges stock-direction stability with the interior-effort extinction branch at the transcritical point $r = qE^*$, while the $E = E_{\max}$ boundary branch is classified separately and is not part of that exchange. The survival condition $r > qE^*$ is identical to $N^* > 0$; interior and extinction branches are not simultaneously stable.

### 3.2 The characteristic quasi-polynomial

With $x = N - N^*$, $z = Z - Z^*$, $e = E - E^*$, $\mathrm{sp}_k'(0) = 1/2$, and the floor inactive at $\delta > 0$, the linearisation of (1) is
$$\dot x = A_N x + A_E e, \qquad \dot z = B_N x + B_E e - \frac{1}{\tau_m}z, \qquad \dot e = C_E e + C_Z z(t - \tau),$$
with
$$\begin{aligned}
A_N &= r\left(1 - \frac{2N^*}{K}\right) - qE^*, & A_E &= -qN^*, \\
B_N &= \frac{qE^* - S'(N^*)}{2\tau_m}, & B_E &= \frac{qN^*}{2\tau_m}, \\
C_E &= \left(1 - \frac{E^*}{E_{\max}}\right)\eta\left(\frac{\delta}{\Delta_{\mathrm{ref}}} - \frac{2E^*}{E_{\max}}\right), & C_Z &= \left(1 - \frac{E^*}{E_{\max}}\right)\left[\frac{\eta E^*}{\Delta_{\mathrm{ref}}} + \frac{\delta_0 Z_{\mathrm{ref}}}{(Z_{\mathrm{ref}} + \delta)^2}\right].
\end{aligned}$$
The gate factors $(1 - E^*/E_{\max})$ distinguish the gated from the ungated variant and are the algebraic source of threshold relocation between the two. Substituting the modal ansatz $(x,z,e)e^{\lambda t}$ and expanding the $3 \times 3$ characteristic determinant along the third row gives the characteristic quasi-polynomial
$$P(\lambda) - C_Z L(\lambda) e^{-\lambda\tau} = 0, \qquad P(\lambda) = (\lambda - A_N)(\lambda + d)(\lambda - C_E), \qquad L(\lambda) = B_E(\lambda - A_N) + A_E B_N, \tag{5}$$
with $d = 1/\tau_m$. At the interior equilibrium the filter identities hold:
$$B_N = -\frac{A_N}{2\tau_m}, \qquad B_E = -\frac{A_E}{2\tau_m},$$
because the deficit signal is $qEN - S(N) = -A_N x - A_E e + o(\cdot)$ and $\mathrm{sp}_k'(0) = 1/2$. Consequently
$$L(\lambda) = B_E(\lambda - A_N) + A_E B_N = B_E\lambda - B_E A_N - A_E \frac{A_N}{2\tau_m} = B_E\lambda,$$
since $B_E A_N + A_E B_N = 0$ exactly. This cancellation — the even-pairs algebra below — is the structural identity of the architecture.

---

## 4. The Complete Hopf Cubic

**Theorem 2 (Cubic modulus condition and phase branches).** *For the linearisation (5), $\lambda = i\omega$ ($\omega > 0$) is a characteristic root if and only if $x = \omega^2$ is a positive root of*
$$H(x) = (x + A_N^2)(x + d^2)(x + C_E^2) - C_Z^2\left[ B_E^2 x + (A_E B_N - A_N B_E)^2 \right] = 0, \tag{6}$$
*and*
$$\tau = \frac{-\arg\{P(i\omega)/(C_Z L(i\omega))\} + 2\pi k}{\omega} > 0, \qquad k \in \mathbb{Z}. \tag{7}$$
*A cubic has at most three positive roots, so there are at most three Hopf-frequency families; higher branches recur within a family as $\tau_{n,0} + 2\pi k/\omega_n$ and are not additional frequencies.*

*Proof.* At $\lambda = i\omega$, equation (5) reads $P(i\omega) = C_Z L(i\omega)e^{-i\omega\tau}$, so the moduli must match:
$$|P(i\omega)|^2 = C_Z^2 |L(i\omega)|^2. \tag{8}$$
Compute $|P(i\omega)|^2 = |(i\omega - A_N)(i\omega + d)(i\omega - C_E)|^2 = (\omega^2 + A_N^2)(\omega^2 + d^2)(\omega^2 + C_E^2)$, and $L(i\omega) = B_E i\omega + (A_E B_N - A_N B_E)$, whence $|L(i\omega)|^2 = B_E^2\omega^2 + (A_E B_N - A_N B_E)^2$. Substituting into (8) and writing $x = \omega^2$ gives exactly (6). Given a positive root $x$ of (6), the phase condition reads $e^{-i\omega\tau} = P(i\omega)/(C_Z L(i\omega))$; since both sides have unit modulus on the root locus, $\tau$ is recovered as (7) up to the $2\pi k$ ambiguity. A cubic has at most three positive roots, giving at most three frequency families; for a fixed family $\omega_n$ the delays $\tau_{n,0} + 2\pi k/\omega_n$ recur with period $2\pi/\omega_n$ in $\tau$, and are branches of the same frequency, not additional frequencies. Candidates qualify as Hopf crossings only after simplicity and transversality are verified separately; the cubic determines neither criticality nor global folds. $\square$

**Corollary 2 (Even pairs).** *At the interior equilibrium of (1), the cross term vanishes identically, $A_E B_N - A_N B_E \equiv 0$, so*
$$H(x) = (x + A_N^2)(x + d^2)(x + C_E^2) - C_Z^2 B_E^2 x,$$
*with $H(0) = A_N^2 d^2 C_E^2 > 0$ and $H(x) \to +\infty$. Hence the positive roots of $H$ occur in even number — zero or two, never one or three — on this architecture.*

*Proof.* The identities $B_N = -A_N/(2\tau_m)$, $B_E = -A_E/(2\tau_m)$ give $A_E B_N - A_N B_E = -A_E A_N/(2\tau_m) + A_N A_E/(2\tau_m) = 0$. With the cross term zero, $H$ has the stated form; $H(0) > 0$ because $A_N^2, d^2, C_E^2 > 0$ (the gate factor makes $C_E \ne 0$; in the degenerate coincidence $A_N = 0$ or $C_E = 0$ the count is unchanged since $H(0) \ge 0$ and the leading term is $x^3$). A cubic polynomial with positive value at $0$ and positive leading coefficient crosses the positive axis an even number of times (counting multiplicity), i.e. zero or two. $\square$

For both Candidate A and Candidate B the cubic has exactly two positive roots on both the gated and the ungated variant; the certified local spectrum is stated in Section 5.1.

### 4.1 The scalar archetype

Two general statements frame the delay mathematics. First, the scalar Hayes result (Hayes, 1950; Hale and Verduyn Lunel, 1993, Ch. 3): for $\dot x = -ax - Bx(t-\tau)$ with $a > 0$, $B \ge 0$, the zero equilibrium is stable for all $\tau \ge 0$ if $B \le a$; if $B > a$ it is stable for $\tau < \tau_{\mathrm{crit}} = \arccos(-a/B)/\sqrt{B^2 - a^2}$ and unstable beyond, with *no restabilisation* as $\tau$ grows (the crossing is destabilising). This is the scalar mechanism by which loop delay destroys stability that undelayed feedback sustains. Second, no delay conclusion is sign-free: the systems $\dot x = -ax - bx(t-\tau)$ and $\dot x = -ax + bx(t-\tau)$ ($a, b > 0$) have different feedback signs and different stability properties. The named systems of this paper instantiate the two signs — the mobilising law of (1) carries $C_Z > 0$, the protective law (3) carries $C_Z < 0$ — and Sections 5–6 show that the local mathematics separates accordingly.

---

## 5. The Mobilising Channel

### 5.1 Local crossings and interval-certified delays

The complete cubic search (Theorem 2) with separately verified simplicity and transversality, independently checked by direct root tracking of the quasi-polynomial, gives the crossing pairs:

| System | Candidate A $\tau_-$ / $\tau_+$ (yr) | Candidate B $\tau_-$ / $\tau_+$ (yr) |
|---|---|---|
| M3-U (ungated) | 6.8814 / 132.3749 | 6.2136 / 76.2906 |
| M3-B (gated) | 3.67 / 150.36 | 5.5128 / 80.4245 |
| M3-B (gated), interval-certified | $\tau_- \in [3.6661490142739, 3.6661490142743]$, $\tau_+ \in [150.3584773101408, 150.3584773101421]$ | gated: $\tau_- \in [5.5128407314433, 5.5128407314436]$, $\tau_+ \in [80.4245267142270, 80.4245267142276]$; ungated: $\tau_- \in [6.2135987340180, 6.2135987340183]$, $\tau_+ \in [76.2906356879512, 76.2906356879518]$ |

The interval certificates are interval-Newton enclosures of the simple positive roots of $H$ in $x = \omega^2$ (width $\le 4\times10^{-17}$ in $x$) followed by branch-safe interval evaluation of the phase relation (7); the delay is the interval evaluation of the phase formula at a certified positive root of $H$, not a root of an argument formula. The committed interval pipeline uses outward rounding and interval transcendentals, checks simplicity and transversality signs (the lower crossing stabilising, $\mathrm{d\,Re}\,\lambda/\mathrm{d}\tau < 0$; the upper crossing destabilising), and reproduces the displayed Candidate A intervals exactly on re-execution. The certification tier is scoped precisely: these are certified enclosures of the *local spectrum* of the cubic — a strictly weaker statement than a certified Hopf bifurcation for retarded functional differential equations in the sense of Church and Lessard (2022) and Church and Queirolo (2024), whose radii-polynomial methods certify the bifurcation itself; no such full certificate is claimed here, and none is claimed for any global fold (Section 8, and the supplementary material).

The undelayed gated mobilising law is already unstable ($\mathrm{Re}\,\lambda > 0$ at $\tau = 0$; the cubic $\lambda^3 + 0.2774\lambda^2 + 0.00056\lambda + 0.000213 = 0$ violates the Routh–Hurwitz condition $0.2774 \times 0.00056 > 0.000213$). Institutional delay acts as a phase filter that opens the phase-stabilised window $(\tau_-, \tau_+)$ and closes it again at $\tau_+$; delay-amplified instability refers to the upper crossing and the bistable windows, not to delay creating the short-delay instability. Enforcing the effort boundary relocates the local thresholds by approximately 47% (lower) and 14% (upper) at Candidate A without changing the equilibrium — thresholds do not transport between the gated and ungated variants, and the gate's threshold relocation is a registered comparison, not a calibration.

### 5.2 Lyapunov coefficients and criticality

The first Lyapunov coefficient at a Hopf point of the gated three-state core is the Hassard–Faria–Magalhães cubic (Hassard, Kazarinoff, and Wan, 1981; Faria and Magalhães, 1995) evaluated from the exact second and third derivatives of the vector field at equilibrium, under unit Hermitian normalisation of the right eigenvector and $q^*\Delta'(i\omega)p = 1$:
$$\ell_1(\tau_-^{\mathrm{A}}) = +5.75\times10^{-5}, \qquad \ell_1(\tau_+^{\mathrm{A}}) = +3.55\times10^{-4},$$
both subcritical at gated Candidate A; the ungated Candidate B lower crossing is supercritical, $\ell_1(\tau_-^{\mathrm{B}}) = -9.84\times10^{-5}$ (hence no lower fold for that class), with $\ell_1(\tau_+^{\mathrm{B}}) = +2.19\times10^{-3}$. The subcritical small branch satisfies $\|N - N^*\| \sim C\sqrt{\tau - \tau_-}$ (slope 29.8 in amplitude-squared, $R^2 = 0.994$; the collocated orbit at $\tau = 3.700$ has residual $\sim10^{-7}$ and escapes onto the large cycle by roundoff alone). These are numerical evaluations of the coefficient formulas at declared parameter points — computational results, stated as such.

Two status distinctions are load-bearing. First, within the registered model family the criticality statements obtained from branch scaling — amplitude exponent $0.47$ and surrogate cubic coefficient $\approx3.9\times10^{-6}$ near the lower gated crossing — are inferred numerical classifications, not first Lyapunov coefficients from a centre-manifold calculation; the $\ell_1$ values above are the computed coefficients for the gated core. Second, criticality is not invariant under the regularisation: the first Lyapunov coefficient contains $\mathrm{sp}_k''(0) = k/4$, so the reported $\ell_1(\tau_\pm)$ are at $k = 10$, Hopf points are invariant under $k \in \{5, 10, 20, 40\}$ at fixed $\delta$, and a sign change in $\ell_1$ under that sweep would rearrange the lower window. $k$-independence of equilibria and linearisations is a local statement only; fold locations depend on $k$, and no $k$-uniform topology is claimed.

### 5.3 Hopf persistence under residual feedback

**Proposition 2 (Local Hopf persistence, conditional).** *Assume the five-state macro-reduction conjecture of the supplementary material (a slow-fast reduction with verified spectral gap and compact memory kernel — not proved here), and the working-core projection of Section 2.4. If the working four-state (respectively three-state) characteristic equation has a simple pair $\pm i\omega$ at $\tau = \tau_\star \in \{\tau_-, \tau_+\}$ with $\mathrm{d\,Re}\,\lambda/\mathrm{d}\tau \ne 0$ and no other imaginary eigenvalues, if the fast Jacobian remains uniformly Hurwitz at the joint equilibrium, and if non-feedback mass compartments stay outside the delay loop, then: under the strict specialisation the core spectrum is a literal factor of the full characteristic function and the Hopf points persist exactly; under residual macroeconomic feedback of size $\varepsilon$ the specialised system has a Hopf point $\tau_\star(\varepsilon) = \tau_\star + O(\varepsilon)$ in the ideal large-reservoir limit (add $O(1 - \sigma_{\mathrm{geo}})$ for the finite reservoir).*

The conditionality is mathematical content: the statement is conditional on unverified spectral hypotheses, and the global fold events of Section 8 lie explicitly outside its hypotheses. (Proof: under the strict specialisation the characteristic function factors and the simple pair persists by the implicit function theorem; under residual feedback the $O(\varepsilon)$ shift follows from the Schur-complement/Rouché perturbation argument. The reduction conjecture itself is the unproved hypothesis.)

### 5.4 The two-delay interpolation and the conditional mobilising-weight corollary

Linearising the interpolation (4) at the Candidate A point — an interior rest where both brackets vanish separately under the calibration of Section 2.5 — gives $\dot e = C_E e + C_m z(t-\tau_m) + C_p z(t-\tau_p)$, with $C_m = \chi_m C_Z^{\mathrm{mob}}$, $C_p = \chi_p C_Z^{\mathrm{prot}}$, and $C_E$ the sum of the two gate-adjusted $E$-derivatives.

**Proposition 3 (Two-delay characteristic identity).** *The characteristic function of the stock–memory block coupled to the interpolated effort law is*
$$P(\lambda) - L(\lambda)\bigl( C_m e^{-\lambda\tau_m} + C_p e^{-\lambda\tau_p} \bigr) = 0, \tag{9}$$
*with $P$ and $L$ the polynomials of Section 3.2.*

*Proof.* The variational system of the interpolation has the same stock–memory block as (1) and the effort row $\dot e = C_E e + C_m z(t-\tau_m) + C_p z(t-\tau_p)$; expanding the characteristic determinant along the effort row, the minor associated with $z(t-\tau_m)$ is exactly $L(\lambda)e^{-\lambda\tau_m}$ (the cofactor of the memory row, the same cofactor that produced (5)), and likewise for $\tau_p$. $\square$

**Proposition 4 (Weighted small gain).** *If*
$$\sup_{\omega > 0} \frac{(|C_m| + |C_p|)\, |L(i\omega)|}{|(i\omega - A_N)(i\omega + d)(i\omega - C_E)|} < 1, \tag{10}$$
*then (9) has no imaginary-axis root for any $\tau_m, \tau_p \ge 0$.*

*Proof.* An imaginary root $\lambda = i\omega$ would satisfy $P(i\omega) = L(i\omega)(C_m e^{-i\omega\tau_m} + C_p e^{-i\omega\tau_p})$, hence, taking moduli and using $|e^{-i\omega\tau}| = 1$,
$$|P(i\omega)| \le |L(i\omega)|(|C_m| + |C_p|),$$
contradicting (10), which is the triangle inequality reversed strictly. The statement holds together with the zero-root and characteristic-continuity requirements carried by the delay-independent stability argument of Section 6.2. $\square$

**Corollary 3 (Mobilising weight, conditional).** *At Candidate A the pure mobilising loop gain exceeds 1 and the pure protective loop gain is 0.080. Assume (i) the common equilibrium and all linear coefficients depend continuously on $\chi_m$; (ii) the characteristic denominator remains nonzero on the imaginary axis; (iii) the protective endpoint has a strict gain margin. Then there exists $\chi_m^* \in (0,1)$ such that every interpolation with $\chi_m < \chi_m^*$ and $\chi_p = 1 - \chi_m$ satisfies (10). A Hopf of the interpolated system therefore requires a sufficiently large mobilising weight; it cannot be produced by decreasing $\tau_p$ alone.*

The corollary holds exactly under the listed hypotheses; the interpolation family is not otherwise established to preserve a common equilibrium or a nonvanishing denominator, and no promotion of the corollary beyond them is made.

---

## 6. The Protective Channel

### 6.1 The quota-tracking law and its calibration

The protective law (3) with its calibration is stated in Section 2.5. The interpretation discipline is that the effort variable may be an endogenous industry response, a legal quota-utilisation state, or an actual institutional control, and these interpretations are not interchangeable; the quota-tracking law is an institutional control law.

### 6.2 The no-Hopf theorem

**Theorem 3 (No delay-induced Hopf under quota tracking).** *At the Candidate A stock–memory linearisation and the protective gains of Section 2.5, the modulus cubic $H(x) = x^3 + c_2 x^2 + c_1 x + c_0$ has*
$$c_2 = A_N^2 + d^2 + C_E^2 = 0.76339, \qquad c_1 = 0.028946, \qquad c_0 = 9.278\times10^{-6},$$
*all positive, with $c_2 c_1 - c_0 = 0.02209 > 0$. Consequently the characteristic quasi-polynomial has no purely imaginary root for any delay $\tau_p \ge 0$, and — the undelayed Jacobian being Hurwitz and the zero-root condition delay-independent with $P(0) \ne 0$ — the equilibrium is exponentially stable for every $\tau_p \ge 0$.*

*Proof.* (a) Exclude imaginary roots. At $\lambda = i\omega$ the modulus balance of (5) reads $|P(i\omega)| = |C_Z||L(i\omega)|$; by Theorem 2 this is equivalent to $H(\omega^2) = 0$. For the protective channel, $C_E = -0.850336$ and $C_Z = -1.661702$ with the same $A_N = -0.0179$, $d = 0.2$, $B_E = 0.008955$, and the even-pairs cancellation gives
$$H(x) = (x + A_N^2)(x + d^2)(x + C_E^2) - C_Z^2 B_E^2 x = x^3 + c_2 x^2 + c_1 x + c_0$$
with $c_2 = A_N^2 + d^2 + C_E^2 = 0.76339$, $c_1 = A_N^2 d^2 + A_N^2 C_E^2 + d^2 C_E^2 - C_Z^2 B_E^2 = 0.028946$, $c_0 = A_N^2 d^2 C_E^2 = 9.278\times10^{-6}$. All three coefficients are strictly positive, so by Descartes' rule of signs $H$ has no positive real root; no $\omega > 0$ solves the modulus balance. Equivalently, by the Routh–Hurwitz criterion applied to $H$: $c_2 > 0$, $c_2 c_1 - c_0 = 0.02209 > 0$, $c_0 > 0$, so all roots of $H$ have negative real part — the modulus condition cannot hold for real $\omega$ because $H(\omega^2) = 0$ would give $\omega^2$ as a positive (hence nonnegative) real root of $H$. (b) Delay-independent stability. The undelayed linearisation is Hurwitz: its characteristic polynomial is $P(\lambda) - C_Z L(\lambda)$ with $L(\lambda) = B_E\lambda$ (even-pairs cancellation), i.e. $\lambda^3 + 1.0682\,\lambda^2 + c_1'\lambda + c_0'$ with all Routh conditions satisfied (the protective $C_E = -0.850$ dominates, so the $\lambda^2$-coefficient $-A_N + d - C_E = 1.0682$); explicitly the Routh array for $P(\lambda) - C_Z B_E\lambda$ has first column entries $1, 1.0682, c > 0, c_0' > 0$. The zero root is excluded independently of delay: $P(0) - C_Z L(0) = P(0) \ne 0$ because $L(0) = 0$ and $P(0) = (-A_N)(d)(-C_E) = A_N d C_E \ne 0$. Since (a) shows the imaginary axis is never crossed for any $\tau_p \ge 0$, and the characteristic roots of retarded equations depend continuously on $\tau_p$ (Hale and Verduyn Lunel, 1993, Ch. 1), the roots remain in the open left half-plane for every $\tau_p \ge 0$. $\square$

The channel-separation reading is the theorem's interpretation: destabilisation by short delay is confined to the mobilising summand, and the protective channel has no periodic branch born from the equilibrium at any delay.

The same conclusion is visible in the loop-gain form. Define
$$\Gamma(\omega) = \left| \frac{C_Z L(i\omega)}{(i\omega - A_N)(i\omega + d)(i\omega - C_E)} \right|.$$
Then $\Gamma$ is continuous on $[0,\infty)$, $\Gamma(0) = 0$ (since $L(0) = 0$), $\Gamma(\omega) \to 0$ as $\omega \to \infty$ (quadratic over cubic), and a numerically located maximum gives $\sup_\omega \Gamma(\omega) = 0.08011 < 1$, attained at $\omega \approx 0.0589$; the loop-gain exclusion argument of Section 9 then excludes every imaginary root for all delays directly. The maximum is a numerical location, stated as such; the analytic certificate is the Descartes/Routh–Hurwitz argument above.

### 6.3 The iso-gain sign flip

**Proposition 5 (Iso-gain sign flip).** *Replacing $C_Z$ by $-C_Z$ in the gated Candidate A linearisation, leaving every other coefficient unchanged, leaves $H$ identical (it depends on $C_Z$ only through $C_Z^2$), leaves the frequencies identical, and shifts each family's fundamental delay by $\pi/\omega$ on the branch that keeps it fundamental: the lower family ($\omega_1 \approx 0.02518$) moves up, $3.666 + \pi/\omega_1 = 128.374$ yr, and the upper family ($\omega_2 \approx 0.03944$) moves down, $150.358 - \pi/\omega_2 = 70.697$ yr, both remaining local Hopfs. (The subscripts retain their original-family meaning — $\tau_-$ is the lower family's shifted delay, $\tau_+$ the upper family's — so on the shifted axis the order is reversed: $\tau_+ < \tau_- < \tau_+^{\mathrm{unshifted}}$.) The reversed-gain linearisation has loop gain $1.016 > 1$ and retains the factor $\eta E^*/\Delta_{\mathrm{ref}}$: it is **not** the quota law, whose genuine form changes the modulus as well as the sign.*

This is the false-reversal identification hazard: a pure sign flip is not a protective institution, and attributing the reversed-gain crossings to a quota tracker would confuse two different effort laws.

### 6.4 Sampled protection and the discretisation crossing

**Proposition 6 (Protective sample-and-hold monodromy).** *Replace the protective delayed feedback by sample-and-hold of period $T_r$ with one explicit Euler review step (the sample-and-hold review operator of computer-controlled systems; Åström and Wittenmark, 1997). Between reviews the variational system is $\dot\xi = A_{\mathrm{hold}}\xi$ with*
$$A_{\mathrm{hold}} = \begin{pmatrix} A_N & 0 & A_E \\ B_N & -d & B_E \\ 0 & 0 & 0 \end{pmatrix},$$
*(the effort is frozen between reviews), and at each review the effort update is the explicit Euler step $e_{k+1} = e_k + T_r(C_E e_k + C_Z z_k)$. The monodromy of one review interval is therefore*
$$M_p(T_r) = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & T_r C_Z & 1 + T_r C_E \end{pmatrix} \exp(A_{\mathrm{hold}} T_r). \tag{11}$$

*Proof.* On one interval $[kT_r, (k+1)T_r)$ the frozen-effort system is linear with matrix $A_{\mathrm{hold}}$ (the effort row is zero), so the state at the end of the interval is $\exp(A_{\mathrm{hold}}T_r)\xi_k$; the review then applies the affine update $\xi_{k+1} = \xi(t_{k+1}^-) + T_r(C_E e_{k+1}^- + C_Z z_{k+1}^-)\,\mathbf{e}_3$, i.e. the matrix factor displayed in (11). The sampled equilibrium is exponentially stable iff every eigenvalue of $M_p(T_r)$ lies in the open unit disc. $\square$

At the protective gains, $\rho(M_p(1)) = 0.9838 < 1$: annual review of the quota-tracking channel is linearly stable at Candidate A. On the grid $T_r \in [0.2, 20]$, the spectral radius is strictly below one on $[0.2, 2.306)$ and strictly above one on $(2.306, 20]$, so the Euler hold map crosses $\rho = 1$ at $T_r \approx 2.306$ (a grid resolution). That crossing is carried by the discretisation — specifically by the Euler-update factor $1 + T_r C_E$ with $C_E = -0.850$ and its interaction with the hold flow — and it is **not** a Hopf point of the protective delay equation, whose continuous spectrum Theorem 3 excludes at every delay. The finding is the mathematical statement: the $T_r = 2.306$ crossing belongs to the discretisation. The operator-specific scope is recorded: the mobilising hold map is unstable at $T_r = 1$ because the undelayed mobilising Jacobian is already unstable, and the protective map does not inherit that instability (Section 7).

### 6.5 Channel-specific pacing

**Theorem 4 (Channel-specific pacing).** *For the mobilising bracket the equilibrium is linearly unstable for $0 < \tau < \tau_-$; for the protective law at Candidate A it is linearly stable for every $\tau_p \ge 0$; for the two-channel system any delay-induced instability lies in a region of $(\tau_m, \chi_m)$ and is independent of $\tau_p$ wherever the weighted small-gain bound (10) applies.*

*Proof.* The first clause is Section 5.1 (undelayed instability with a stabilising lower crossing at $\tau_-$). The second is Theorem 3. The third is Proposition 4 together with Corollary 3: wherever (10) holds, no imaginary root exists for any $(\tau_m, \tau_p)$, so instability — if present — must originate in parameter regions where the mobilising weight is large, and is independent of the protective delay there. The synthesis inherits Corollary 3's interpolation hypotheses wherever its clause applies. $\square$

The policy-scope reading, instantiated: faster protective governance is not the hazard — the mobilising sign is.

---

## 7. The Review Interval as Control

**Theorem 5 (Sampled-data monodromy of the mobilising channel).** *Linearise the gated three-state core about the interior equilibrium and replace the delayed feedback by sample-and-hold of period $T_r$ with one Euler review step. Between reviews the variational system is $\dot\xi = A_{\mathrm{hold}}\xi$ with $A_{\mathrm{hold}}$ as in Proposition 6; the monodromy of one review interval is*
$$M(T_r) = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & T_r C_Z & 1 + T_r C_E \end{pmatrix} \exp(A_{\mathrm{hold}} T_r), \tag{12}$$
*now with the mobilising gains $C_E = -0.0595$, $C_Z = +1.785$. The sampled equilibrium is exponentially stable iff every eigenvalue of $M(T_r)$ lies in the open unit disc; a Neimark–Sacker crossing occurs at those $T_r$ where $M(T_r)$ has a simple pair $e^{\pm i\theta}$, $\theta \notin \{0, \pi\}$, with the remaining spectrum inside the disc; and $(M(T_r) - I)/T_r$ converges to the continuous undelayed Jacobian as $T_r \to 0$. The statement concerns this sample-and-hold/Euler review scheme, not the continuous-delay equation.*

*Proof.* The monodromy formula is Proposition 6's derivation with the mobilising gains; the stability criterion is the discrete-time spectral radius condition; the Neimark–Sacker characterisation is the standard eigenvalue-crossing criterion for maps; and the consistency limit follows from $\exp(A_{\mathrm{hold}}T_r) = I + A_{\mathrm{hold}}T_r + O(T_r^2)$ and the update factor $I + T_r \begin{pmatrix} 0&0&0\\0&0&0\\0&C_Z&C_E\end{pmatrix}$, whose sum with $A_{\mathrm{hold}}T_r$ is $I + T_r J_{\mathrm{cont}} + O(T_r^2)$ where $J_{\mathrm{cont}}$ is the undelayed Jacobian of the continuous linearisation. $\square$

On the gated Candidate A hold map: annual review is unstable, $\rho(M(1)) = 1.00055$ (the undelayed linearisation being already unstable, Section 5.1), and the sampled equilibrium restabilises by a Neimark–Sacker pair at
$$T_r^{\mathrm{NS}} = 47.536\ \mathrm{yr},$$
with a period-doubling multiplier at $T_r^{(-1)} = 79.143$ yr. The computation is the zero set of $\det(M(T_r) - e^{i\theta}I) = 0$ on the declared map: for a slow stock under this review operator, **the control is the review interval** — lengthening review restabilises a system that annual review destabilises, and the continuous-delay settling recommendation (decrease the delay) does not transfer to periodic review (lengthen the interval). The contrast with the protective channel (stable at annual review, destabilised near $T_r \approx 2.3$ yr by the discretisation) is complete: the two sign channels respond to the review interval in opposite directions.

---

## 8. Global Numerics at Declared Certification Levels

All results in this section are numerical results at their declared status: computed outputs tied to registered equations, parameter sets, history classes, methods, tolerances, and finite domains, with basins restricted to the histories actually tested. The fold-status discipline governs every global statement: the events below are numerical continuation, multiplier, basin, and turning-region results; no Moore–Spence, Krawczyk, or nondegeneracy certificate and no continuous-delay fold proof is claimed. Rigorous saddle-node-of-periodic-orbit results for delay equations exist for specific classes (Beretka and Vas, 2020); none is claimed for the events below.

### 8.1 Methods

Hopf points are located by root tracking of the characteristic equation and independently by the cubic (Theorem 2); folds by Keller pseudo-arclength continuation of the periodic orbit with $1.5$–$5\times10^6$ yr persistence tests per step and far-from-equilibrium cross-checks (collocation-continuation numerics in the DDE-bifurcation tradition: Engelborghs, Luzyanina, and Roose, 2002; background: Guckenheimer and Holmes, 1983; Kuznetsov, 2004). Fixed-initial-condition bisection mislocates folds by more than 20 yr under the critical slowing down near each Hopf (linear rates $10^{-4}$–$10^{-5}$ yr⁻¹) and is not used.

### 8.2 The attractor topology and the two-fold lower boundary

For the effort-bounded three-state core at Candidate A the lower bistable boundary is the disappearance of the stable large cycle in $\tau \in [5.574, 5.576]$ yr, with the evidence branch-resolved. Long-horizon simulation shows basin collapse between $\tau = 5.574$ and $5.576$: beyond that interval no tested far-from-equilibrium history is captured by the large cycle. Adaptive-mesh collocation with variational Floquet tracking, on the other hand, resolves the dominant multiplier of the collocated large-cycle branch as a single real eigenvalue — imaginary part identically zero at every measured point — rising monotonically from $0.240$ at $\tau = 4.0$ to $0.964$ at $\tau = 5.5815$ with orbit residual $\sim10^{-12}$: the orbit remains a converged fixed point of the collocation map through $\tau = 5.5815$, past the basin-collapse interval, with its multiplier still below $+1$. The $+1$-crossing signature is exhibited directly on the small unstable branch: the small branch born at the subcritical Hopf $\tau_- = 3.666$ undergoes a continuation-supported fold at $\tau \approx 5.587$ (real multiplier $1.0514$ at $\tau = 5.584$ falling to $0.99898$ at $\tau = 5.587$; Fourier collocation succeeds through $\tau = 5.58667$ with residual $5\times10^{-14}$, amplitude $21.80$, period $313.76$ yr, and fails at $\tau = 5.590$ under the stated budget). The two families do not meet (amplitudes $\approx25$ and $\approx21.7$; periods $\approx322.9$ and $\approx314.3$ yr), so the lower boundary is a pair of nearby folds of two distinct periodic-orbit families, and the $\sqrt{\tau - \tau_{\mathrm{SNPO}}}$ collision scaling of a single saddle-node does not apply. For the large branch the exact crossing point and the $0.002$ yr gap between basin collapse and multiplier crossing remain to be pinned, so the saddle-node-of-periodic-orbits classification of this lower boundary is **provisional** — the alternative reading is a crisis-like loss of the attracting cycle's basin while the branch persists — and no Neimark–Sacker or torus event is involved in either reading (the multiplier is real throughout). On the large cycle at $\tau = 5.55$ the filter floor never binds, $E \le 9.2 \ll E_{\max}$, and $N \ge 68.7$: the termination is not a gate singularity, not a graze of $N = 0$, and not a homoclinic connection (the period is 324 yr and decreasing).

The attractor sequence is the five-regime topology: (i) $0 < \tau < \tau_-$, the equilibrium unstable with a single large-amplitude cycle the attractor; (ii) $\tau_- < \tau < \tau_{\mathrm{term},L}$, a stable focus coexisting with the large cycle (lower bistable window $\approx0.5$–$2$ yr wide); (iii) $\tau_{\mathrm{term},L} < \tau < \tau_{\mathrm{fold},R}$, monostable settling; (iv) $\tau_{\mathrm{fold},R} < \tau < \tau_+$, the large cycle reappears beside the still-stable equilibrium (upper bistable window $\approx1$–$2$ yr wide); (v) $\tau > \tau_+$, the equilibrium unstable and the cycle the sole attractor. Inside either bistable window, histories at a large stock with low effort are captured by the cycle while near-collapse histories recover to the quiet equilibrium — abundance plus slow adjustment is the exposed trajectory, not scarcity. The upper-window attractor is a period-1 limit cycle (at $\tau = 131.8$ yr ungated: Poincaré spread $<5\times10^{-3}$, envelope constant to $0.005\%$ over $2\times10^6$ yr, fundamental period $\approx135.6$ yr, all Floquet multipliers inside the unit circle with dominant nontrivial pair modulus $\approx0.81$; an independent method-of-steps RK45 reproduces the envelope).

At the upper boundary, persistence bisection gives $\tau \in [148.125, 148.438]$ yr, summarised as 148.3 yr, with the exact fold type and branch connection undetermined; collocation pins two distinct families through that value — the Hopf small branch (residual $\sim10^{-13}$ on $\tau \in [130, 150.30]$, amplitude $0.11$–$1.87$) and an interior large family (residual $\sim10^{-13}$ on $\tau \in [147.5, 160]$, amplitude $15.9$–$19.5$) — which remain distinct there, with a third family at $E \ge E_{\max}$ collocating down to $\tau \approx 144.5$.

### 8.3 The registered numerical families

**M3-U.** Candidate A crossings $6.8814$ / $132.3749$ yr (Candidate B $6.2136$ / $76.2906$ yr); persistence boundaries near $7.355$ and $131.24$ yr; lower bistable window $\approx0.47$ yr, upper $\approx1.1$ yr; basin-dependent capture at $\tau = 131.8$ yr; the upper-window attractor a stable period-one cycle with all nontrivial computed Floquet multipliers inside the unit circle and the near-lower-Hopf small orbit unstable (dominant multiplier $>1$). The saddle-node-of-periodic-orbits classification of either persistence boundary remains conjectural unless branch collision and nondegeneracy are demonstrated. Sensitivity sweeps over $\eta \in [0.5, 3.0]$ find zero or two positive cubic roots; the two-crossing window in $r$ is bounded ($\approx(0.008, 0.022)$ yr⁻¹ at $\eta = 0.914$, extending to $\approx0.061$ yr⁻¹ at $\eta = 3$) — model sensitivity results, not empirical calibration. A Droop nutrient–quota variant of the same core — an external nutrient pool and an internal quota with quota-limited growth $\mu(q) = r(1 - q_{\min}/q)$, a growth-coupled pool, and the interior equilibrium preserved — leaves the $r$-window unchanged, with window upper edge $\le 0.023$ yr⁻¹ at $\eta = 0.914$ and no Hopf crossing at any $r \ge 0.2$ yr⁻¹: a growth-coupled pool cannot be slow at large $r$ (the quota self-relaxes at exactly $r$, and the nutrient pool's relaxation grows with the throughput; the only $r$-independent slow pool is the working core's $\omega_A$-type exchange, which narrows the window).

**M3-B.** Candidate A crossings $3.67$ / $150.36$ yr (Candidate B $5.5128$ / $80.4245$ yr; no gated-Candidate-B global branch or fold result is registered). The lower global boundary is not one saddle-node — the stable large-cycle branch folds near $\tau = 5.574$–$5.575$ yr while the small unstable branch folds separately near $5.587$ yr (multiplier $1.0514 \to 0.998983$); the upper boundary is bracketed $[148.125, 148.438]$ yr, type undetermined. Multiple far-from-equilibrium seeds failed to reach a large cycle throughout the tested interior range $5.57 < \tau < 148.3$ yr — finite searches that support, but cannot prove, interior monostability. The inferred subcritical signatures (amplitude exponent $0.47$; surrogate cubic coefficient $\approx3.9\times10^{-6}$) are inferred numerical classifications, not centre-manifold Lyapunov coefficients; the two lower folds belong to distinct families, so a single square-root collision law is inapplicable; $k$-independence is local only. Ungated-Candidate-B global values are registered: the three-state ungated Candidate B has no lower fold (its lower crossing is supercritical, Section 5.2) and an upper fold of the large cycle at $76.075$ yr against $\tau_+ = 76.2906$ yr — a narrow upper bistable window $(76.075, 76.29)$ — while the four-state ungated Candidate B carries the corresponding Hopf crossings at $6.25$ and $76.33$ yr with its upper fold not pinned; these are registered numerical values, their classification as saddle-nodes of periodic orbits remains open, and no gated-Candidate-B fold location follows from them.

**M3-LC.** Upper persistence boundary $\approx132.0$ yr at $\psi = 1$ versus $\approx132.5$ yr at $\psi = 0$ (raw outputs $131.998$/$132.499$; separation $0.501$ yr), with an inter-locator discrepancy of $\approx0.8$ yr against an independent locator's $131.24$ yr taken as the localisation-uncertainty scale; the defensible conclusion is an order-of-one-year shift, not an exact percentage. At $\tau = 115$ yr, $\kappa = 0.5$, long-lived transients of order $10^4$–$10^5$ yr reach minimum $N \approx 33$ under pure stock culling and $N \approx 10$ under pure recruitment suppression: the two channels of harvest pressure — removing standing stock versus suppressing recruitment — differ in the depth of their transient excursions, though the local bifurcation structure cannot see them. In the fixed-demand experiment ($D = 0.7 > S_{\max} = 0.5$, $N(0) = 50$), stock culling is stopped at its first hitting time of $N = 0$ (equivalently implemented with an explicit donor limiter; the unconstrained vector field is not continued into negative stock), placing pure culling at zero near time $158$, while pure recruitment suppression approaches zero asymptotically and reaches $N < 1$ near time $430$ — a first-hitting-time result. Local equivalence does not imply excursion equivalence; assigning $\psi$ to a field system requires age-, stage-, or replenishment-specific evidence.

**Four-state working core.** Ungated Candidate A donor-limited equilibrium $(N^*, A^*, E^*) = (89.5256, 397.8665, 2.0896)$ with crossings $6.982022$ / $132.272044$ yr and persistence boundaries near $7.374$ and $130.77$ yr (upper bracketed $[130.770, 130.771]$); gated counterpart crossings $\approx3.7849$ / $150.12$ yr with cycle periods $\approx360$–$380$ yr (lower regime) and $150$–$160$ yr (upper regime). The turnover stability boundary at $\tau = 0$ is $\omega_A^* \approx 0.001316298$ (gated $\approx0.001330$), located by a 1798-point equilibrium sweep, sixty sub-threshold simulations (ten $\omega_A$ values, six delays in $[0, 300]$ yr, all converging to the equilibrium), and sixty continuation points above it producing a continuous Hopf pair — finite sweeps supporting delay-independent sub-threshold stability, not a theorem for all parameter values. The reduced open-pool caveat stands: freezing $A$ is not a justified fast-variable elimination at the baseline $\omega_A = 10^{-3}$ yr⁻¹. The upper global fold moves from $\approx148$ yr (three-state) to $\approx64$ yr (four-state) while the Hopf pair stays within a few percent — the global objects are model-version-specific in a way the local ones are not; the characteristic-pinned detail is in Section 8.4.

**MPF (primitive-flux core).** At the illustrative baseline $(\mathcal{M}, \mu, K_A, d, c, \gamma_U, q, E_{\max}, \eta, \delta_0, \Delta_{\mathrm{ref}}, \tau_m) = (100, 0.340, 24.5, 0.072, 0.00995, 0.388, 0.0384, 35.8, 2.23, 0.0118, 2.29, 5.13)$ the equilibrium is $(X^*, U^*, E^*) \approx (16.68, 10.23, 0.435)$, with no local Hopf crossing for $0 \le \tau \le 500$ (characteristic-root and argument-principle counts) and small perturbations decaying at all directly tested delays. The apparent onset near $\tau = 33.4$–$33.6$ is a long-lived decaying transient (return within $\approx2\times10^4$ time units throughout the tested $33.4$–$34.8$ interval); for $\tau \gtrsim 35$ a slow-fast oscillation persists for some tested memory histories and not others — basin-selective global dynamics, not a local Hopf or a classified periodic-orbit fold. The absence of a baseline Hopf is parametric: Hopf roots first appear at $\eta_{\mathrm{crit}} \approx 2.337$, with two interleaving pairs over $\eta \in (2.337, 3]$ (at $\eta = 2.5$: $\approx0.6$, $54.2$, $92.9$, $113.1$ yr; at $\eta = 3.0$ one pair spans $\approx4.5$–$41.2$ yr; at the out-of-range $\eta = 10$: $17.568$/$18.362$ yr with a supercritical-consistent onset, exponent $0.59$, inferred). Above $\tau_+$ at $\eta = 10$ the attractor is classified as homoclinic-like slow-fast (relaxation) intermittency rather than a torus or a period doubling — diagnostics: a broad onset-interval spectrum with no sharp peak, a thin map-like Poincaré section on $Z$-crossings, inter-excursion-interval coefficient of variation $1.58$, and return-map anticorrelation $r = -0.47$ — with the large-amplitude time fraction rising monotonically from $0\%$ at $\tau = 18.4$ to $100\%$ by $\tau \approx 22$ and no sharp second threshold separating quiet and captured regimes. The pair-birth structure behind the interleaving is registered: the large-delay pair is born at $\eta_{\mathrm{crit}} \approx 2.337$ ($\tau_- \approx 71.2$, $\tau_+ \approx 72.9$ yr) and migrates downward as $\eta$ rises, while the small-delay pair is born at $\eta \approx 2.454$ with $\tau_- \to 0$ at its onset. A sigmoid-gated effort variant of the same ecological core was screened across more than $300$ parameterisations without finding a genuine delay-induced Hopf — a numerical negative result over the sampled domain, not a structural impossibility theorem. The MPF regime is neither the M3-B regime nor a transfer of its threshold values.

### 8.4 The four-state working core

The characteristic matrix $\Delta(\lambda) = \lambda I - A_0 - A_\tau e^{-\lambda\tau}$ of the gated working core at the frozen-donor equilibrium $(N, A, Z, E) = (89.52562, 397.8665, \ln 2/10, 2.08962)$ has simple imaginary roots at
$$\tau_- = 3.78487\ \mathrm{yr}\ (\text{period }250.44\ \mathrm{yr}),\qquad \tau_+ = 150.12175\ \mathrm{yr}\ (\text{period }159.13\ \mathrm{yr}),$$
with $|\det\Delta(i\omega, \tau)| < 10^{-18}$ — the characteristic-pinned pair, within $3.2\%$ (lower) and $0.2\%$ (upper) of the three-state values, inside the frozen-active-pool bound of Proposition 1. Fourier collocation produces a small periodic orbit of residual $\sim10^{-13}$ immediately below $\tau_+$ (amplitude $0.090$ at $\tau = 150.082$). Continuation of the large-amplitude cycle (converged orbit state and delay history carried between steps, $10^4$–$10^5$ yr per step) locates the two global folds at
$$\tau_{\mathrm{term},L}^{(4)} \approx 5.63\ \mathrm{yr},\qquad \tau_{\mathrm{fold},R}^{(4)} \approx 64.4\ \mathrm{yr},$$
the lower bracketed by steady behaviour at $\tau = 5.62$ (peak-to-peak $N$-amplitude $\approx23$) and collapse by $5.64$, the upper by steady behaviour at $\tau = 64.5$ (amplitude $\approx11$) and collapse by $64.25$. The resulting topology is a narrow lower bistable window $(3.78, 5.63)$ yr, a wide monostable interval $(5.63, 64.4)$ yr, and a wide upper bistable window $(64.4, 150.1)$ yr in which the large cycle coexists with the stable equilibrium but, from generic far-from-equilibrium histories, is reached only for $\tau$ above roughly $75$–$100$ yr (depleted-stock histories only near $\tau \gtrsim 135$). Cycle periods run from $\approx371$ yr at $\tau = 4.5$ to $\approx320$ yr at the lower fold, and from $\approx156$ yr near $\tau_+$ to $\approx73$ yr at the upper fold. Whether either fold is a saddle-node of periodic orbits (versus a Neimark–Sacker or torus-mediated transition) is not established. A second bifurcation parameter invisible to the three-state core appears: at $\tau = 0$ the four-state equilibrium is unstable for $\omega_A > \omega_A^* \approx 0.001316$ and delay-independently stable below it; above it, on the ungated system, both Hopf points and both folds track smoothly, $\tau_-$ falling from $\approx17.5$ to $\approx6.9$ yr with the monostable interval remaining $\approx120$–$260$ yr; the gated $\tau_- \approx 3.78$ is the baseline $(\omega_A, \kappa_A)$ value, not a uniform constant. Oscillation periods throughout $\tau < \tau_-$ are $250$–$390$ yr, essentially independent of $\tau$: the frequency is pinned by $r$ and $\tau_m$, not by institutional delay, and uniformly raising $r$ toward fish-like values destroys the oscillatory regime rather than compressing the period into a decade.

The frozen-donor quasi-equilibrium discipline governs all of these numbers: the working point requires continuing geological support ($\approx4.652$ stock units per year) and is not a rest point of the closed mass ledger; it is incompatible with the formal quasi-steady slaving target of Section 2.4; and the working-core thresholds are $\sigma_{\mathrm{geo}} = 1$ properties.

### 8.5 Parameter windows

Within the parameter subregion where the Candidate A two-Hopf pair exists, one-at-a-time variation across the reported ranges preserves the pair and the lower-boundary structure. Outside the bounded $r$-window the system is delay-independently stable or lacks a positive equilibrium. $\tau_-$ lies in $3.7$–$7$ yr across the two effort laws and both candidates, and in $4$–$25$ yr across the full $(r, \eta)$ rectangle; $\tau_+$ is primarily controlled by the biological time $1/r$ but also depends on the effort-response chart — Candidates A and B share $r = 0.02$ and have $\tau_+ \approx 132$–$150$ yr and $\approx76$–$80$ yr respectively across the two effort laws (A: $132.37$ ungated, $150.36$ gated; B: $76.29$ ungated, $80.42$ gated). The literature range $r \in [0.005, 0.4]$ yr⁻¹ is wider than the instability window. The dimensionless groups that fix $N^*/K$ and $r\tau_\pm$ once effort is scaled by $E_{\max}$ — and the complementary fact that the separate effort scale is not identifiable from $(N, Z)$ alone — are identification statements treated in the companion papers on sampled governance and assessment architectures.

### 8.6 Reproduction targets

A simple crossing recorded near $\tau^* \approx 43$ with period $\approx263$ time units and $\mathrm{d\,Re}\,\lambda/\mathrm{d}\tau < 0$ at $\eta = 5$, $\varsigma = 0.8$, $K_0 = 0.03$, $q = 0.01$ (an elevated-forcing cod-class calculation on an incompletely specified ten-state template) is retained as a reproduction target pending recovery and registration of the constitutive closures actually used; the closure convention, remaining parameters, root count, active nonsmooth branch, residual values, tolerances, and full search domain remain to be recovered. The record's other two run classes are carried at the same status: class 1 — life-history anchoring, with maturation times $g \approx 1$, $2$, and $5$ yr associated respectively with the anchovy-, sprat-, and cod-class cases and productivity chosen to satisfy the interior survival condition, for which no crossing is detected over the tested delay search at the default economic settings (the tested interval and complete parameter vector remain to be recovered); class 2 — the broader crossing search, in which crossings occur in a parameter subset, all examined with $\mathrm{d\,Re}\,\lambda/\mathrm{d}\tau < 0$ and generally with periods of order $10^3$–$10^4$ time units, and no two-crossing $\tau_-/\tau_+$ window is recorded (exact residual values, tolerances, and the full search domain remain to be registered). The sign discipline governs any future use: $\mathrm{d\,Re}\,\lambda/\mathrm{d}\tau < 0$ at a simple crossing is a stabilising local crossing — the equilibrium is locally unstable just below and stable just above — and such a result cannot support language asserting that increasing delay creates oscillatory instability.

---

## 9. The Loop-Gain Family

### 9.1 The general feedback identity

The vector ledger and the reduced cores share a linearised feedback identity, not one nonlinear system. Writing the ledger in primitive fluxes — assimilation $g$, mortality $m$, decomposition $d_U$, harvest $h$ — the signed depletion signal $\ell = h - (g - m) = -\dot X$ is an identity, and liquidation is $[\ell]_+$. Let $\boldsymbol{\xi}$ be the ecological perturbation, $\dot{\boldsymbol{\xi}} = \mathbf{J}\boldsymbol{\xi} + \mathbf{b}_E e$, with memory a gain-$\gamma_m$ filter of $-\mathbf{c}^\top\dot{\boldsymbol{\xi}}$. The linearised loop of every core in this paper is
$$\lambda - C_E - C_Z e^{-\lambda\tau}\, \frac{-\gamma_m\lambda\,\mathbf{c}^\top(\lambda\mathbf{I} - \mathbf{J})^{-1}\mathbf{b}_E}{1 + \tau_m\lambda} = 0. \tag{13}$$
The three-state core is the $1\times1$ case ($\mathbf{J} = A_N$, $\mathbf{b}_E = A_E$, $\gamma_m = 1/2$); the primitive-flux (stoichiometric) core is the $2\times2$ stock–detritus block with $\gamma_m = 1$ (its signed memory $\ell = -\dot X$ is unregularised, which places it outside the $Z \ge 0$ invariance statement of Section 2.2). Both reductions are symbolic identities: the three systems share this characteristic identity but differ in their nonlinear objects — the upper global fold moves from $\approx148$ yr (three-state) to $\approx64$ yr (four-state) while the Hopf pair stays within a few percent, the equilibrium memory differs ($Z^* = \delta > 0$ versus $0$), and the primitive-flux core has no baseline Hopf ($\eta_{\mathrm{crit}} \approx 2.34$). The three ingredients are an ecological resolvent supplying admissible frequencies, an institutional gain $C_Z\gamma_m$ that must close the loop, and a delay supplying phase; the gain condition is $\tau$-independent, the phase condition rotates through match and past it, and non-monotone delay-stability is the generic behaviour of the architecture.

### 9.2 The loop-gain exclusion theorem

**Theorem 6 (Loop-gain exclusion of delay-induced Hopf).** *Write the general feedback equation as $\lambda - C_E - C_Z e^{-\lambda\tau}G(\lambda) = 0$. If*
$$\sup_{\omega \in \mathbb{R}} \frac{|C_Z|\,|G(i\omega)|}{|i\omega - C_E|} < 1, \tag{14}$$
*then there is no purely imaginary characteristic root for any $\tau \ge 0$, hence no delay-induced Hopf.*

*Proof.* An imaginary root $\lambda = i\omega$ would give $i\omega - C_E = C_Z e^{-i\omega\tau}G(i\omega)$, hence $|i\omega - C_E| = |C_Z||G(i\omega)|$, contradicting the strict supremum (14). $\square$

The companion Nyquist reading: a Hopf root exists iff the loop transfer $L(i\omega, \tau) = C_Z G(\lambda)e^{-\lambda\tau}/(\lambda - C_E)$ equals $1$ for some $\omega > 0$, with the small-gain bound $|L| < 1$ as the uniform special case. The general delay-independent certificate is the Halanay-type small-gain theorem: if for some $\alpha_0 > \beta_0 \ge 0$ the logarithmic matrix measure satisfies $\mu_*(A_0) \le -\alpha_0$ and $\|A_1\|_* \le \beta_0$, then the zero solution is exponentially stable for every fixed $\tau \ge 0$, with decay rate the unique $\eta > 0$ solving $\eta = \alpha_0 - \beta_0 e^{\eta\tau}$ (Halanay, 1966). The condition is sufficient, not necessary: its failure removes the certificate without proving instability, and in nonlinear applications the theorem is local after a declared linearisation unless a global incremental bound is proved. The named-system theorems of Sections 5.4 and 6.2 are instances of this certificate family at declared linearisations.

### 9.3 The logistic identification theorem

**Proposition 7 (Logistic identification).** *In the primitive-flux core take $A \gg K_A$ and set $\mu - d = r > 0$, $c = r/K$; then $g - m = rX(1 - X/K) + O(K_A/A)$. The identification requires the mortality identification: $K_A \to 0$ without $\mu - d = r$ and $c = r/K$ yields $g \to \mu X$, which is not logistic.*

*Proof.* Write $g - m = \mu X \frac{A}{K_A + A} - dX - cX^2$; for $A \gg K_A$, $\frac{A}{K_A + A} = 1 - \frac{K_A}{A} + O((K_A/A)^2)$, so $g - m = (\mu - d)X - cX^2 + O(K_A/A)$. With $\mu - d = r$ and $c = r/K$ this is $rX(1 - X/K) + O(K_A/A)$. Taking $K_A \to 0$ alone gives $\frac{A}{K_A + A} \to 1$, hence $g - m \to (\mu - d)X - cX^2$, which is $\mu X$ only if $d = c = 0$; the logistic identification is a joint statement about mortality and saturation, not a limit of the assimilation flux alone. The claim concerns the linearised feedback identity, not the nonlinear objects, which also differ in the equilibrium memory level, the effort baseline, and the closed form of $E^*$. $\square$

### 9.4 The saturating-gate negative screen

Replacing the autocatalytic factor $\eta E Z_\tau/\Delta_{\mathrm{ref}}$ by a saturating gate $\sigma(Z_\tau/Z_0)$ whose linearisation at equilibrium decreases in deployed effort and contains no factor $\eta E^*/\Delta_{\mathrm{ref}}$, a search of more than 300 randomised parameterisations (Newton eigenvalue tracking, joint modulus minimisation, nonlinear integration) found no genuine imaginary-axis root of the general feedback equation (13). This is a numerical nonexistence report on a compact searched set, not an analytic exclusion on the parameter space. The gated law (1) is not of this class — its $C_Z$ contains both the gate factor and the autocatalytic factor, and it admits the Hopf pair. Autocatalytic coupling $\eta E^*/\Delta_{\mathrm{ref}}$, which grows with deployed effort, is the mechanism that produces the Hopf pair; removing it removes the pair on the searched set.

---

## 10. Discussion

### 10.1 The two channels as a design distinction

The sign separation is the paper's structural finding: on the identical stock–memory block, the mobilising law ($C_Z > 0$) carries a subcritical Hopf pair and a five-regime attractor topology, while the protective quota-tracking law ($C_Z < 0$) carries the no-Hopf theorem — stability at every delay — and stability under annual review. The distinction is not an artefact of the calibration: the iso-gain sign flip (Proposition 5) shows that a sign flip alone, without the genuine quota law's modulus change, retains the Hopf pair at shifted delays and a loop gain above one. Institutions that respond to decline by mobilising further effort with a delayed signal are generically exposed to delay-induced cycles; institutions that track a quota are not — on this architecture. The channel-separation reading answers the question posed by the behavioural literature (Moxnes, 1998): the hazard is not slow governance as such, but slow governance of the mobilising sign.

### 10.2 The review interval as control

Under periodic review the two channels respond in opposite directions to the same instrument. The protective channel is stable at annual review and destabilised only by the discretisation itself near $T_r \approx 2.3$ yr — an artefact to be recognised, not a design threshold. The mobilising channel is unstable at annual review and restabilises as the review interval is lengthened, through a Neimark–Sacker crossing at $T_r = 47.5$ yr. The practical reading: for a slow stock governed by a mobilising effort law, frequent assessment and rapid response is destabilising, and the only control that restores stability within this operator is the review interval itself — a governance parameter, not an ecological one. The result echoes, in a single-species institutional setting, the sampled-data principle that the sampling period is a controller design variable (Åström and Wittenmark, 1997), and it supplies the missing dynamical content to the observation that institutional timing structures resource governance (Ostrom, 1990).

### 10.3 Certification levels

The paper's results carry three distinct certification levels, and the distinction is maintained claim by claim. The cubic modulus condition, the even-pairs algebra, the no-Hopf theorem, the monodromy formulas, and the loop-gain exclusions are proved theorems. The Hopf delay enclosures are interval-Newton certificates of the local spectrum of the cubic — re-execution-verified with outward rounding — but are not certificates of the bifurcation in the sense of Church and Lessard (2022); upgrading them to that standard is a stated open task. The global folds, the attractor classification, and the Lyapunov coefficients are numerical results at declared status, with the two-fold lower boundary left as a provisional saddle-node against a crisis reading, and the fold-certificate gap (Moore–Spence/Krawczyk) documented component by component in the supplementary material. Rigorous saddle-node results for delay equations exist for specific classes (Beretka and Vas, 2020); closing the gap for this system is a second stated open task.

### 10.4 Relation to the early-warning literature

The regime-shift literature's early-warning indicators — rising autocorrelation, rising variance — are candidate diagnostics near fold-type transitions under additive noise with responsive control (Scheffer and Carpenter, 2003; Scheffer et al., 2009; Carpenter et al., 2011). Four indicators are candidate diagnostics for the fold events of Section 8: critical slowing down (the lag-1 autocorrelation of the stock rises near a fold), rising variance (rolling variance increases under additive noise near a bifurcation), epistemic divergence (a growing gap $|\hat S - S|$ between observed and estimated stock), and policy inertia (physical stress increasing without a corresponding control adjustment). The caveat is load-bearing: these are not universal early-warning signals — they apply near fold bifurcations under additive noise with responsive control, they do not follow from the local machinery of this paper, and each is a separate falsifiable empirical-statistical claim. In the bistable windows of Section 8.2 the relevant diagnostic is not a pre-collapse trend but the history-dependence of capture — abundance plus slow adjustment is the exposed trajectory, not scarcity — which the variance/autocorrelation pair cannot see.

### 10.5 Limitations

(i) The model class is a mathematical parameterisation: no stock, effort law, or delay value is calibrated to a named fishery, and the institutional coefficients have not been identified from field data; the results are theorems about the declared class, with the parameter windows of Section 8.5 delimiting the regime of the two-crossing structure. (ii) The delay is a single discrete lag; distributed delays and variable-time institutional lags require separate analysis. (iii) The sample-and-hold results concern the declared Euler review scheme; other discretisations have different monodromies, and the continuous-delay and periodic-review recommendations are not interchangeable (Theorem 5). (iv) The global classification of Section 8 is provisional where stated: the lower boundary's saddle-node classification, the upper boundary's type, and interior monostability are open. (v) The Hopf-persistence statements are conditional on the unproved reduction conjecture (Section 5.3). (vi) The ecological subsystem is scalar logistic; stage structure, spatial structure, and multispecies interactions are outside the analysed class, and the delayed-recruitment literature (Costantino et al., 1995) is engaged only as background.

### 10.6 Open problems

The following are stated as open problems with declared gaps: persistence of a transverse fold of periodic orbits under small typed coupling (requires a verified fold baseline, spectral separation, and regularity of the infinite-dimensional Poincaré map); the RFDE/hybrid transition-persistence analogue; an $n$-patch super-equilibrium criterion (two-patch instances verified, the $n$-patch equivalence open); a variable-time delayed-hybrid information kernel with compact piecewise-history phase space; a restricted delay-separation principle for modularly identified governance loops; and — in the direction suggested by the mobilising channel's autocatalytic mechanism — an exergy-limited controller class for which the loop-gain exclusion of Theorem 6 can be established analytically (a declared conjecture: sufficiently low deployable exergy reduces the loop gain below every admissible Hopf-frequency modulus condition; not universal — depletion of institutional capacity may also disable protective action or create hysteresis).

---

## 11. Conclusion

Where the delay sits determines what it does. Delays in the ecological dynamics of harvested stocks are the classical subject of delayed-logistic and delayed-recruitment analysis; the delay analysed here sits in the institutional loop that converts observed decline into deployed effort, and its mathematics separates sharply along the sign structure of that loop. The mobilising channel — effort responds to decline by deploying more effort — carries a subcritical Hopf pair with interval-certified crossings, a five-regime attractor topology whose lower boundary is a pair of nearby folds of distinct periodic-orbit families, and, under periodic review, instability at the annual scale with restabilisation only through a Neimark–Sacker crossing near a half-century review interval. The protective channel — effort is restored toward a quota — carries a no-Hopf theorem valid at every delay, stability under annual review, and an instability threshold that is provably an artefact of the discretisation. The unifying object is the loop-gain family: an ecological resolvent, an institutional gain, and a delay supplying phase, with the gain condition delay-independent and the phase condition rotating through match and past it. For the design of extractive governance the conclusion is specific: the mobilising sign is the hazard, the review interval is a control variable with opposite effects in the two channels, and the institutional coefficients — the gains and delays of the governance loop — are dynamical parameters with the same standing as the biological ones, to be identified, bounded, and designed against.

---

## Data availability

All computations are deterministic and re-executable from the committed model registry and runners; the interval pipeline reproduces the displayed enclosures exactly with outward rounding. The parameter tables, the certified enclosures, and the numerical protocols are available from the authors and are deposited with the supplementary material.

## Declaration of competing interest

None.

---

## References

Åström, K.J., Wittenmark, B., 1997. Computer-Controlled Systems: Theory and Design, 3rd ed. Prentice Hall, Upper Saddle River.

Beretka, S., Vas, G., 2020. Computer-assisted proof of saddle-node bifurcations in differential equations with delay. Preprint (rigorous SNPO results for specific DDE classes).

Carpenter, S.R., Cole, J.J., Pace, M.L., et al., 2011. Early warnings of regime shifts: a whole-ecosystem experiment. Science 332, 1079–1082.

Church, K.E.M., Lessard, J.-P., 2022. Rigorous verification of Hopf bifurcations in functional differential equations of mixed type. Physica D 429, 133072.

Church, K.E.M., Queirolo, E., 2024. Computer-assisted proofs of Hopf bubbles and degenerate Hopf bifurcations. J. Dyn. Differ. Equ. 36, 3385–3439.

Cloud, M.J., Moore, R.E., Kearfott, R.B., 2009. Introduction to Interval Analysis. SIAM, Philadelphia.

Costantino, R.F., Cushing, J.M., Dennis, B., Desharnais, R.A., 1995. Experimentally induced transitions in the dynamic behaviour of insect populations. Nature 375, 227–230.

Diekmann, O., van Gils, S.A., Verduyn Lunel, S.M., Walther, H.-O., 1995. Delay Equations: Functional-, Complex-, and Nonlinear Analysis. Springer, New York.

Engelborghs, K., Luzyanina, T., Roose, D., 2002. Numerical bifurcation analysis of delay differential equations using DDE-BIFTOOL. ACM Trans. Math. Softw. 28, 1–21.

Ezekiel, M., 1938. The cobweb theorem. Q. J. Econ. 52, 255–280.

Faria, T., Magalhães, L.T., 1995. Normal forms for retarded functional differential equations with parameters and applications to Hopf bifurcation. J. Differ. Equ. 122, 181–200.

Gao, S., Zhang, Z., 2022. Delay-induced stability switches in a harvested resource model. (Delay-harvesting lineage; representative of the ecological-delay literature.)

Guckenheimer, J., Holmes, P., 1983. Nonlinear Oscillations, Dynamical Systems, and Bifurcations of Vector Fields. Springer, New York.

Gurney, W.S.C., Blythe, S.P., Nisbet, R.M., 1980. Nicholson's blowflies revisited. Nature 287, 17–21.

Halanay, A., 1966. Differential Equations: Stability, Oscillations, Time Lags. Academic Press, New York.

Hale, J.K., Verduyn Lunel, S.M., 1993. Introduction to Functional Differential Equations. Springer, New York.

Hassard, B.D., Kazarinoff, N.D., Wan, Y.-H., 1981. Theory and Applications of Hopf Bifurcation. Cambridge University Press, Cambridge.

Hayes, N.D., 1950. Roots of the transcendental equation associated with a certain difference-differential equation. J. Lond. Math. Soc. 25, 226–232.

Hutchinson, G.E., 1948. Circular causal systems in ecology. Ann. N.Y. Acad. Sci. 50, 221–246.

Khiyar, O., et al., 2026. Delay-harvesting dynamics. (Delay-harvesting lineage; representative of the ecological-delay literature.)

Kuznetsov, Y.A., 2004. Elements of Applied Bifurcation Theory, 3rd ed. Springer, New York.

Ludwig, D., Jones, D.D., Holling, C.S., 1978. Qualitative analysis of insect outbreak systems: the spruce budworm and forest. J. Anim. Ecol. 47, 315–332.

Moore, R.E., 1979. Methods and Applications of Interval Analysis. SIAM, Philadelphia.

Moxnes, E., 1998. Not only the tragedy of the commons: misperceptions of bioeconomics. Manag. Sci. 44, 1234–1248.

Ostrom, E., 1990. Governing the Commons: The Evolution of Institutions for Collective Action. Cambridge University Press, Cambridge.

Scheffer, M., Carpenter, S.R., 2003. Catastrophic regime shifts in ecosystems: linking theory to observation. Trends Ecol. Evol. 18, 648–656.

Scheffer, M., Bascompte, J., Brock, W.A., et al., 2009. Early-warning signals for critical transitions. Nature 461, 53–59.

Zhang, G.D., Shen, Y., Chen, B.S., 2013. Hopf bifurcation of a predator-prey system with predator harvesting and two delays. Nonlinear Dyn. 73, 2119–2131.

---

## Supplementary material

The full interval-enclosure table (enclosures for both candidates and both gating variants, with the verified root intervals in $x = \omega^2$ and the branch-safe phase evaluations), the collocation formulation details (mesh $m = 64/96/128$ and the small-branch computation), the fold-certificate gap documentation (why the continuous-lift and Moore–Spence routes fail for this system, component by component), the variant registry (the response-sign hypotheses and the registered variants with their obligations), and the statement inventory are provided in the accompanying file `paper4_supplementary.md`.

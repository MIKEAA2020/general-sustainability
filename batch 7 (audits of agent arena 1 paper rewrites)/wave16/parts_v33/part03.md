
## 2. The Model Class

*Notation.* Throughout, $N$ is a renewable stock (material or biomass units); $Z$ is a filtered deficit-memory state (stock per time); and $E$ is an extraction effort — a dimensionless institutional deployment intensity, not a conserved material or energy stock. The catchability $q$ has units (effort·yr)$^{-1}$. The signal references $\Delta_{\mathrm{ref}}$, $Z_{\mathrm{ref}}$ and the offset $\delta$ have stock-per-time units; $\eta$ and $\delta_0$ carry yr$^{-1}$ and effort-per-time units. These assignments make each equation dimensionally homogeneous without treating effort as physical mass. The delay $\tau$ is a discrete action (deployment) delay. The filter timescale $\tau_m$ is an ordinary state relaxation time, not a second delay. The two sign channels are called the *mobilising channel* — the feedback law whose gain grows with deployment — and the *protective channel* — the quota-tracking law whose gain restores toward a cap. Periodic-review results use *sample-and-hold*: an Euler-reviewed zero-order-hold sampling of the delayed signal at intervals of length $T_r$. In plain words, the delayed signal is measured once at each review instant and held fixed between reviews, so the review interval $T_r$ is the cadence at which the institution re-decides.

### 2.1 The gated three-state core

Let

@@V32:DEFS@@

where $\Phi_k$ is a shifted, non-negative signal map. The boundary-exact (gated) three-state core is

@@V32:EQ1@@

The memory input is a smoothed version of the stock-decline rate: on this core the identity $qEN - S(N) = -\dot N$ holds exactly, so $\Phi_k$ filters $-\dot N$. The multiplicative gate $(1 - E/E_{\max})$ is essential to what follows. It is a hard saturation architecture, not a generic effort law, and it enforces $E \in [0, E_{\max}]$ by construction. The registered parameterisations are:

@@V32:PARAMTABLE@@

These are mathematical parameterisations and sensitivity anchors, not a joint calibration to a named resource or institution. The institutional coefficients have not been independently identified from a field system. Candidates A and B are two points in the effort-response chart, not rescalings of one class. For the reported pair $\delta = \log(2)/k$ the outer floor cancels algebraically ($\Phi_k(s) = \mathrm{sp}_k(s) > 0$ for every finite $s$), so the floor is inactive on every reported periodic orbit. This identity is parameter-specific; for $\delta \ne \log(2)/k$ floor contact must be checked orbit by orbit.

### 2.2 Admissibility

**Theorem 2.1 (Forward invariance of the admissible region).** *For the history class $\varphi \in C([-\tau, 0], \mathbb{R}^3)$ define*

@@V32:DSET@@

*Assume*

*(H1) the initial history lies in $\mathcal{D}$ — every history value, not only the endpoint.*

*Then every classical solution of (1) remains in $\mathcal{D}$ for as long as it exists.*

*Proof.* Check the five boundary faces. (i) $N = 0$: $S(0) = 0$ and the harvest $qEN$ vanishes, so $\dot N = 0$; the face is invariant. (ii) $N = K$: $S(K) = 0$, so $\dot N = -qEK \le 0$, inward. (iii) $Z = 0$: the source $\Phi_k(qEN - S(N)) \ge 0$ by construction of the non-negative signal map, so $\dot Z = \Phi_k(\cdot)/\tau_m \ge 0$, inward. (iv) $E = 0$: the gate factor is positive (away from $E = E_{\max}$) and the bracket is $\delta_0 Z_\tau/(Z_{\mathrm{ref}} + Z_\tau) \ge 0$, so $\dot E \ge 0$, inward. (v) $E = E_{\max}$: the gate vanishes, $\dot E = 0$; the face is invariant. The delay enters only through $Z(t - \tau)$, and the initial history lies in $\mathcal{D}$, so the delayed argument is non-negative throughout the first interval $[0, \tau]$. The vector field is therefore subtangential on the first interval by (i)–(v); the argument repeats by induction over $[n\tau, (n+1)\tau]$ by the method of steps (Hale and Verduyn Lunel, 1993). At $\tau = 0$ the same faces give subtangentiality of the ordinary differential equation directly. □

**Corollary 2.1 (Boundedness and global continuation).** *Let $\bar Z = \max\{ \sup_{[-\tau,0]} Z,\ \Phi_k(qE_{\max}K) \}$. Then every solution satisfies $0 \le Z(t) \le \bar Z$; all three states remain in a bounded set on which the vector field is locally Lipschitz; and the solution continues for all $t \ge 0$.*

*Proof.* The $Z$-equation reads $\dot Z = d(\nu(t) - Z)$ with $d = 1/\tau_m$ and the monotone bounded input $\nu(t) = \Phi_k(qE(t)N(t) - S(N(t))) \le \Phi_k(qE_{\max}K)$. The letter $\nu$ is used only in this section, for the filter input; it denotes the Halanay decay rate in Section 10.2. Variation of constants gives $Z(t) = e^{-dt}Z(0) + d\int_0^t e^{-d(t-s)}\nu(s)\,ds \le e^{-dt}Z(0) + \bar Z(1 - e^{-dt})$, hence $Z(t) \le \max\{Z(0), \bar Z\} \le \bar Z$ by the definition of $\bar Z$. Nonnegativity of $Z$ is part of Theorem 2.1. With $N \in [0,K]$, $E \in [0, E_{\max}]$, and $Z \in [0, \bar Z]$, the state lies in a compact set on which the right-hand side of (1) is locally Lipschitz: the logistic and the polynomial effort law are smooth; the signal map $\Phi_k$ is locally Lipschitz in general and smooth where its floor is inactive — in particular, at the registered relation $\delta = \log 2 / k$ the floor cancels and $\Phi_k = \mathrm{sp}_k$ is $C^1$ everywhere. The solution therefore extends for all time. Local Lipschitz regularity suffices for the existence, uniqueness, and continuation arguments; the $C^1$ statements are needed only where bifurcation coefficients are computed, and there the floor-inactive parameter sets of Section 5.2 are the declared scope. One further observation is recorded here because Section 3 uses it. On the invariant extinction face $N = 0$ the memory input is $\Phi_k(0) = \delta$, so $Z$ relaxes to $\delta$, and the extinction rest carries the same admissible positive effort root as the interior branch: institutional memory sustains baseline commanded effort against zero realised harvest. Effort is an institutional deployment intensity, not a conserved stock; the core makes no closed-effort-energetics claim, and a materially closed application must add and donor-limit that support explicitly. □

### 2.3 The registered model family

The reference member of the family is **M3-B (boundary-exact gated)** — the core (1) itself, whose multiplicative saturation gate enforces $E \in [0, E_{\max}]$ exactly (Theorem 2.1). Its crossings, folds, and basins are the paper's reference records (Sections 5.1 and 9.3). Four further variants delimit the robustness of those results. No invariant set, equilibrium formula, local threshold, periodic branch, or admissibility result transfers between them without a separate argument.

- **M3-U (ungated).** The same ecology with the effort law without the outer gate; $E_{\max}$ is then a self-limitation scale only. The gate factor is the algebraic source of threshold relocation between the variants (Section 3.2).

- **M3-LC (two-channel stock law).** The logistic renewal is written as a gross birth–mortality decomposition $B(N) = S(N) + \kappa rN$, $M(N) = \kappa rN$ ($\kappa \ge 0$), and the pressure $qEN$ is split by $\psi \in [0,1]$:

@@V32:EQ2@@

Here $\psi qEN$ is a realised removal of standing stock and $(1-\psi)qEN$ is demographic suppression — a prevented inflow, not a material transfer out of the adult-stock compartment. Equation (2) is a phenomenological stock equation, not a closed mass ledger. Whenever the recruitment floor is inactive, (2) reduces exactly to $\dot N = S(N) - qEN$. The floor never binds at the interior equilibrium (the binding condition reduces to $-\psi S(N) > \kappa rN$, impossible), so the equilibrium, the Jacobian, the characteristic equation, and both Hopf points are independent of $\psi$ and $\kappa$. Local equality does not imply excursion equality: the floor truncates recruitment on large excursions, and the two channels diverge there (Section 9).

- **M4-A (active-pool extension).** Logistic renewal is replaced by $R(N,A) = rN(1 - N/K)\, A/(A + A_0)$ with a dynamic active-support pool $\dot A = -B(N,A) + \omega_A(A^{\mathrm{eq}} - A)$ and a fully declared donor-limited gross draw $B$. The relaxation term makes this a reduced open-pool model unless its donor/receiver reservoir is included explicitly. Freezing $A$ is not a justified fast-variable elimination at the baseline $\omega_A = 10^{-3}$ yr$^{-1}$.

- **MPF (primitive-flux core).** Living biomass $X$, detritus $U$, active material $A = \mathcal{M} - X - U$, primitive fluxes $g(X,A) = \mu XA/(K_A + A)$, $m(X) = dX + cX^2$, $h(X,E) = qEX$, signed memory $\dot Z = (-\dot X - Z)/\tau_m$, the detritus equation $\dot U = m(X) - \gamma_U U$ — the detritus compartment receives the full mortality flux $m(X) = dX + cX^2$ and exports it at the specific rate $\gamma_U > 0$, yr$^{-1}$; this is the equation the invariance argument below uses — and the bounded effort law $\dot E = (1 - E/E_{\max})[\eta E Z(t-\tau)/\Delta_{\mathrm{ref}} + \delta_0 - \eta E^2/E_{\max}]$. The core has a signed zero-equilibrium memory ($Z^* = 0$, a true constant baseline), detritus, and a different effort equilibrium; it is not (1). On the boundary $X + U = \mathcal{M}$ the active pool is $A = 0$ and $g(X,0) = 0$, so $\frac{d}{dt}(X+U) = -qEX - \gamma_U U \le 0$, which — with $g(0,A) = 0$, $m(0) = 0$, and the donor-limited flux assumptions — proves forward invariance of the simplex $\{X \ge 0,\ U \ge 0,\ X + U \le \mathcal{M}\}$ for the ecological subsystem under admissible effort.

### 2.4 The four-state working core and its relation to (1)

The working four-state core restores the active abiotic pool as a state: $\dot N = R(N,A) - qEN$, $\dot A = -B(N,A) + \omega_A(A^{\mathrm{eq},W} - A)$ with $A^{\mathrm{eq},W} = A^{\mathrm{eq,intrinsic}} + \kappa_A K/\omega_A$, and the $Z$ and $E$ equations of (1) unchanged except that $S(N)$ is replaced by $R(N,A)$. At the baseline $\omega_A = 10^{-3}$ yr$^{-1}$, $\kappa_A = 0.05$ yr$^{-1}$, $A_0 = 0.01K$, $A^{\mathrm{eq,intrinsic}} = 0.5K$, so $A^{\mathrm{eq},W} = 5050$.

Two closure statements fix its status. First, in the ideal large-reservoir limit $\sigma_{\mathrm{geo}} = 1$ — where $\sigma_{\mathrm{geo}} \in (0,1]$ is the geological-reservoir adequacy ratio, a dimensionless companion-ledger quantity measuring how far the geological reservoir sustains the working core's donor draw ($\sigma_{\mathrm{geo}} = 1$ the ideal limit, $1 - \sigma_{\mathrm{geo}}$ the scale of the finite-reservoir perturbation) — the specialised system satisfies the working-core equations exactly (an algebraic identity check), with detritus a driven auxiliary that does not feed back; for finite geological reservoirs the vector field is perturbed by $O(1 - \sigma_{\mathrm{geo}})$ and $U$ feeds back. Second, detritus slaving under a fixed intrinsic target is an $O(\varepsilon_U)$ singular-perturbation estimate on compact intervals — a standard Tikhonov/Fenichel-type argument (Hale and Verduyn Lunel, 1993, Ch. 9, Diekmann et al., 1995); $\varepsilon_U$ is the fast-variable slaving parameter, of the order of the slow-to-fast timescale ratio $r/\gamma_U$, with $\gamma_U$ the detritus export rate of the MPF core, Section 2.3. At the baseline $\gamma_U/r = 10$ detritus is an order of magnitude faster than the stock, so the fast-variable slaving parameter $r/\gamma_U \approx 0.1$ is small and the compact-interval estimate holds. It is only moderately small, however, so it does not control global periodic orbits.

At Candidate A the quasi-steady (QSS) core has a positive low-$A$ equilibrium $(N^*, A^*) \approx (23.85, 0.159)$ and no high-$A$ near-logistic exploited equilibrium (the high-stock branch gives $A^* \approx -137$, inadmissible). The QSS core is a distinct singular-limit object: a valid limit that is not dynamically connected to the high-$A$ working equilibrium used for the reported thresholds, and the two objects are never merged. The working core is declared as an open projection: omitted turnover is routed to a diagnostic detritus/inert sink; the reduced $(N,A,Z,E)$ trajectory is not mass-closed by itself; and its global periodic results are model-version-specific. The working equilibrium is a frozen-donor quasi-equilibrium sustained by geological support of order $\omega_A(A^{\mathrm{eq},W} - A^*) \approx 4.652$ stock units yr$^{-1}$, whose cumulative donor change is $4.652\,T/A^{\mathrm{geo}}$ — 1.2% on a century horizon at the lower geological ratio $A^{\mathrm{geo}}/A^* = 10^2$ and 0.12% at $10^3$.

**Remark (companion-interface numbers).** *The quantities $A^{\mathrm{eq},W} = 5050$, the geological support $\approx 4.652$ stock units yr$^{-1}$, and the century draws $1.2\%/0.12\%$ are interface values carried from the companion material-ledger paper — where the closed mass ledger and its quasi-steady slaving target are the subjects — for cross-paper consistency. They are not hypotheses of any theorem of this paper, and they do not make the working-core quasi-equilibrium a rest point of a closed ledger: the four-state working core is an open projection, sustained by continuing geological support, precisely as stated above. If this paper is read alone, the four-state core should be taken as an open working model, with the 4.652 accounting a remark citing the companion rather than a structural result.*

The finite-time connection between the four-state and three-state cores is the following bound. It justifies using (1) for local, near-equilibrium questions on institutional timescales — but not the large-amplitude cycle or its period, and not spectral quantities. A trajectory bound does not transfer to Hopf thresholds, so the proximity of the four-state crossings to the three-state values (with $\tau_-$ 3.2% higher and $\tau_+$ 0.2% lower than the three-state values, Section 9.4) is reported as a numerical observation, not derived from this bound.

**Lemma 2.1 (Frozen-active-pool approximation).** *Let $(N, Z, E)$ solve (1) and let $(\tilde N, \tilde Z, \tilde E)$ solve the four-state core from the same initial data, with $A(t) \ge A_{\min} > 0$ on $[0,T]$. Measure state differences in the scaled norm*

@@V32:NORMSTAR@@

*where $\Delta N = \tilde N - N$, $\Delta Z = \tilde Z - Z$, $\Delta E = \tilde E - E$ (stock, flux, and effort scales respectively). Assume*

*(H1) the vector field of (1) is Lipschitz on the admissible region.*

*Then*

@@V32:LEMMABOUND@@

*with $C_T$ a constant depending on the structural parameters and $T$. This is an inner approximation on $[0,T]$, not a Tikhonov reduction.*

*Proof.* The four-state renewal differs from the saturated renewal by

@@V32:RMISMATCH@@

so the mismatch is bounded pointwise by $\frac{rK}{4} \cdot \frac{A_0}{A_{\min} + A_0}$ (the renewal factor is at most $rK/4$ and the saturation deficit is at most $A_0/(A_{\min} + A_0)$). The $Z$ and $E$ equations of the two cores coincide in form, so their difference equations are driven only by $\Delta N$ and by the renewal mismatch $\sigma(t) = R(\tilde N, A(t)) - S(\tilde N)$, with $|\sigma(t)| \le \frac{rK}{4} \frac{A_0}{A_{\min} + A_0}$. The difference system is retarded (the $E$-row contains $\Delta Z(t - \tau)$), so the estimate is taken in the history norm: with $Y(t) = \sup_{s \in [-\tau, t]} \|\xi(s)\|_*$, Lipschitz continuity of the common vector field gives the retarded differential inequality

@@V32:GRONWALL@@

for the structural constant $C_1$ — the scaled-norm Lipschitz constant of the difference vector field, finite by the Lipschitz hypothesis of the statement. The retarded Gronwall estimate (Hale and Verduyn Lunel, 1993, Ch. 6) then yields $\sup_{s \in [-\tau, T]} \|\xi(s)\|_* \le C_T A_0/(A_{\min} + A_0)$ on $[0,T]$, with $C_T = C_1 T e^{C_1 T}$ after absorbing constants; identical initial data give $\xi(0) = 0$. □

### 2.5 The protective channel and the two-channel interpolation

A protective institution is the quota-tracking law

@@V32:EQ3@@

where $E_{\mathrm{cap}}$ is $C^2$, positive, strictly decreasing, with the calibration $E_{\mathrm{cap}}(Z) = E_0 Z_{\mathrm{ref}}/(Z_{\mathrm{ref}} + Z)$ and $E_0 = E^*_A(Z_{\mathrm{ref}} + \delta)/Z_{\mathrm{ref}}$. The calibration places the unique interior rest of (3) on the stock–memory block of (1) at the Candidate A point $(N^*, Z^*, E^*) = (89.55188, \delta, 2.08962)$, so the stock–memory block is identical to (1)'s and only the effort law changes. At that rest $E_{\mathrm{cap}}(\delta) = E^*$ and the linear gains are

@@V32:GAINS@@

which at $\eta_p = \eta_A = 0.914$ give $C_E = -0.850336$ and $C_Z = -1.661702$. Both signs are those of a restoring quota, not of scarcity mobilisation; the mobilising counterpart of (1) at the same point has $C_Z = +1.785$ and $C_E = -0.0595$ (Section 3.2). The channel-separation object of this paper is exactly this sign discipline.

The two-channel interpolation replaces the effort law by

@@V32:EQ4@@

with $\chi_m, \chi_p \ge 0$; the pure mobilising channel is $(\chi_m, \chi_p) = (1, 0)$, pure protection $(0, 1)$. The mobilising bracket is

@@V32:FM@@

the bracket of the mobilising law (1) written with its $Z$-argument displayed; $\tau_M$ is the mobilising deployment delay and $\tau_p$ the protective one. Throughout, the memory-filter timescale keeps its own symbol $\tau_m$ (used in the filter $\dot Z = (\Phi_k(\cdot) - Z)/\tau_m$); the two are distinct objects, distinguished by subscript wherever they co-occur.

---

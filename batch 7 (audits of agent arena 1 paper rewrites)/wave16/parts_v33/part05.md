
## 5. The Mobilising Channel

The mobilising channel is the effort law of (1) with positive delayed gain on the deficit memory. Its behavioural reading comes from fisheries governance: when an institution sees a deficit signal, it deploys more extraction effort — a fleet expansion, a subsidy release, an open-access licence issuance — and the deployment is realised only after a delay. The mathematics of this section says two things. First, the undelayed gated version of such a law is already unstable. Second, an interval of intermediate delays — rather than the short-delay regime familiar from the scalar Hayes example — is the window in which the loop is stabilised by phase. The implication for governance is direct: on this architecture the institutional deployment delay is a phase filter that can either stabilise or destabilise depending on its value. It is not a one-directional hazard.

### 5.1 Local crossings and interval-certified delays

Two terms are used throughout, and both are defined here for the broad reader. A *Hopf crossing* is a parameter value at which a complex-conjugate pair of characteristic roots crosses the imaginary axis and oscillatory dynamics are born. *Interval-certified* means the crossing delay is enclosed by interval Newton iteration with outward rounding, so the enclosure is guaranteed to contain the exact root of the registered equations (Moore, 1979; Cloud, Moore, and Kearfott, 2009).

The complete cubic search (Theorem 4.1) with separately verified simplicity and transversality, independently checked by direct root tracking of the quasi-polynomial, gives the crossing pairs:

@@V32:CROSSTABLE@@

The interval certificates are interval-Newton enclosures of the simple positive roots of $H$ in $x = \omega^2$ (width $\le 4\times10^{-17}$ in $x$) followed by branch-safe interval evaluation of the phase relation (7). The delay is the interval evaluation of the phase formula at a certified positive root of $H$, not a root of an argument formula. The registered interval pipeline uses outward rounding and interval transcendentals, checks simplicity and transversality signs — the lower crossing stabilising, $\mathrm{d\,Re}\,\lambda/\mathrm{d}\tau < 0$; the upper crossing destabilising — and reproduces the displayed Candidate A intervals exactly on re-execution.

The certification tier is scoped precisely. These are certified enclosures of the *local spectrum* of the cubic — a strictly weaker statement than a certified Hopf bifurcation for retarded functional differential equations in the sense of Church and Lessard (2022) and Church and Queirolo (2024), whose radii-polynomial methods certify the bifurcation itself. No such full certificate is claimed here, and none is claimed for any global fold (Section 9, and the supplementary material). The interval machinery itself is standard (Moore, 1979; Cloud, Moore, and Kearfott, 2009). The pair is registered as gate G5 of the registration campaign — the gate log is deposited with the supplementary material, S9. The registered compute-core Hopf pair $3.666149$ / $150.358477$ yr — the base core (1)'s institutional-delay certificates, reproduced by the recovered compute core (Supplementary S9.5) — certifies this pair; it is a record of the compute core, not an object of the delayed-recruitment system of Section 7.

The undelayed gated mobilising law is already unstable ($\mathrm{Re}\,\lambda > 0$ at $\tau = 0$): the undelayed characteristic polynomial $P(\lambda) - C_Z B_E\lambda = (\lambda - A_N)(\lambda + d)(\lambda - C_E) - C_Z B_E\lambda$ in the symbols of Section 3.2 — the $-C_Z B_E\lambda$ term being exactly what the filter identity leaves of the delay coupling at $\tau = 0$ — at the declared Candidate A constants violates the Routh–Hurwitz condition. The linear coefficient is reduced by $C_Z B_E$, so the product of the first two coefficients falls below the constant term, which is the algebraic signature of the shortest-delay instability; and $P(\lambda) - C_Z B_E\lambda = 0$ is the undelayed case of (5). Institutional delay acts as a phase filter that opens the phase-stabilised window $(\tau_-, \tau_+)$ and closes it again at $\tau_+$. Delay-amplified instability refers to the upper crossing and the bistable windows, not to delay creating the short-delay instability. Enforcing the effort boundary relocates the local thresholds by approximately 47% (lower) and 14% (upper) at Candidate A without changing the equilibrium — thresholds do not transport between the gated and ungated variants, and the gate's threshold relocation is a registered comparison, not a calibration.

### 5.2 Lyapunov coefficients and criticality

The first Lyapunov coefficient at a Hopf point of the gated three-state core is the Hassard–Faria–Magalhães cubic (Hassard, Kazarinoff, and Wan, 1981; Faria and Magalhães, 1995) evaluated from the exact second and third derivatives of the vector field at equilibrium, under unit Hermitian normalisation of the right eigenvector $v$ and its adjoint $w$, with the normalisation $w^*\Delta'(i\omega)v = 1$ ($w^*$ the conjugate transpose; the eigenvector pair is denoted $v, w$ so that $q$ remains the catchability throughout):

@@V32:L1@@

both subcritical at gated Candidate A; the ungated Candidate B lower crossing is supercritical, $\ell_1(\tau_-^{\mathrm{B}}) = -9.84\times10^{-5}$ — hence no lower fold for that class — with $\ell_1(\tau_+^{\mathrm{B}}) = +2.19\times10^{-3}$. The subcritical small branch satisfies $\|N - N^*\| \sim C\sqrt{\tau - \tau_-}$ (slope 29.8 in amplitude-squared, $R^2 = 0.994$; the collocated orbit at $\tau = 3.700$ has residual $\sim10^{-7}$ and escapes onto the large cycle by roundoff alone). These are numerical evaluations of the coefficient formulas at declared parameter points — computational results, stated as such.

Two status distinctions matter here. First, within the registered model family the criticality statements obtained from branch scaling — amplitude exponent $0.47$ and surrogate cubic coefficient $\approx3.9\times10^{-6}$ near the lower gated crossing — are inferred numerical classifications, not first Lyapunov coefficients from a centre-manifold calculation; the $\ell_1$ values above are the computed coefficients for the gated core. Second, criticality is not invariant under the regularisation: the first Lyapunov coefficient contains $\mathrm{sp}_k''(0) = k/4$, so the reported $\ell_1(\tau_\pm)$ are at $k = 10$; Hopf points are invariant under $k \in \{5, 10, 20, 40\}$ at fixed $\delta$ — the sweep holds $\delta$ numerically fixed rather than maintaining the table relation $\delta = \log 2/k$, and this is the declared reading — and a sign change in $\ell_1$ under that sweep would rearrange the lower window. The $k$-independence of equilibria and linearisations is a local statement only; fold locations depend on $k$, and no $k$-uniform topology is claimed.

### 5.3 Hopf persistence under residual feedback

**Remark 5.1 (Local Hopf persistence, conditional).** *Assume*

*(H1) the five-state macro-reduction conjecture of the supplementary material — a slow-fast reduction whose fast-block uniform normal hyperbolicity is now established as the proposition of S5, proved analytically on the parameter set $\alpha + \eta\beta < 1$, where $\alpha$ and $\beta$ are the two coupling weights of the fast block's $K$–$L$ Jacobian displayed in Supplementary S5, so that the inequality is that block's uniform-Hurwitz condition — with the sweep-quantified margin and the class-violation fraction recorded, and whose compact-memory-kernel condition for infinite-time persistence remains unverified,*

*(H2) the working-core projection of Section 2.4,*

*(H3) the working four-state (respectively three-state) characteristic equation has a simple pair $\pm i\omega$ at $\tau = \tau_\star \in \{\tau_-, \tau_+\}$ with $\mathrm{d\,Re}\,\lambda/\mathrm{d}\tau \neq 0$ and no other imaginary eigenvalues,*

*(H4) the fast Jacobian remains uniformly Hurwitz at the joint equilibrium,*

*(H5) non-feedback mass compartments stay outside the delay loop.*

*Then: under the strict specialisation the core spectrum is a literal factor of the full characteristic function and the Hopf points persist exactly; under residual macroeconomic feedback of size $\varepsilon$ the specialised system has a Hopf point $\tau_\star(\varepsilon) = \tau_\star + O(\varepsilon)$ in the ideal large-reservoir limit (add $O(1 - \sigma_{\mathrm{geo}})$ for the finite reservoir, $\sigma_{\mathrm{geo}}$ being the geological-reservoir adequacy ratio of Section 2.4).*

The conditionality is mathematical content, and it is stated as such: the statement is conditional on the reduction's residual hypotheses — fast-block Hurwitzness beyond the verified parameter set of S5, and the memory-kernel condition — and the global fold events of Section 9 lie explicitly outside its hypotheses.

*Derivation (conditional, in full).* Under the strict specialisation, the block-triangular identity granted by the reduction conjecture factors the full characteristic function as $\Delta_{\mathrm{full}}(\lambda,\tau) = \Delta_{\mathrm{core}}(\lambda,\tau)\,\Delta_{\mathrm{fast}}(\lambda,\tau)$ with $\Delta_{\mathrm{fast}}$ uniformly Hurwitz on the declared set. The simple imaginary pair $\pm i\omega$ of the core is therefore a simple imaginary pair of the full function, and the implicit function theorem applied to $\Delta_{\mathrm{full}}(\lambda,\tau) = 0$ at $(\pm i\omega, \tau_\star)$ — where $\partial_\lambda \Delta_{\mathrm{full}} \neq 0$ by simplicity — preserves the crossing exactly. Under residual macroeconomic feedback of size $\varepsilon$, write $\Delta_{\mathrm{full}}(\lambda,\tau;\varepsilon) = \Delta_{\mathrm{core}}(\lambda,\tau) + \varepsilon\,\chi(\lambda,\tau;\varepsilon)$ with $\chi$ continuous. Near $(\omega_\star, \tau_\star, 0)$ the zero set of $F(\omega,\tau;\varepsilon) = (\mathrm{Re}\,\Delta_{\mathrm{full}}(i\omega,\tau;\varepsilon),\, \mathrm{Im}\,\Delta_{\mathrm{full}}(i\omega,\tau;\varepsilon))$ is a smooth curve through $(\omega_\star, \tau_\star)$ whenever $D_{(\omega,\tau)}F$ is nonsingular there. That nonsingularity is the Cauchy–Riemann restatement of the two hypotheses of the statement — simplicity of $\pm i\omega$ ($\partial_\lambda \Delta_{\mathrm{core}} \neq 0$) and transversality ($\mathrm{d}\,\mathrm{Re}\,\lambda/\mathrm{d}\tau \neq 0$) — so the implicit function theorem yields $\tau_\star(\varepsilon) = \tau_\star + O(\varepsilon)$. The finite-reservoir $O(1-\sigma_{\mathrm{geo}})$ term is the same argument with the perturbation scale replaced. The reduction conjecture itself remains the unproved hypothesis. □

### 5.4 The two-delay interpolation and the conditional mobilising-weight corollary

Linearising the interpolation (4) at the Candidate A point — an interior rest where both brackets vanish separately under the calibration of Section 2.5 — gives $\dot e = C_E e + C_m z(t-\tau_M) + C_p z(t-\tau_p)$, with $C_m = \chi_m C_Z^{\mathrm{mob}}$, $C_p = \chi_p C_Z^{\mathrm{prot}}$, and $C_E$ the sum of the two gate-adjusted $E$-derivatives.

**Proposition 5.1 (Two-delay characteristic identity).** *The characteristic function of the stock–memory block coupled to the interpolated effort law is*

@@V32:EQ9@@

*with $P$ and $L$ the polynomials of Section 3.2.*

*Proof.* The variational system of the interpolation has the same stock–memory block as (1) and the effort row $\dot e = C_E e + C_m z(t-\tau_M) + C_p z(t-\tau_p)$. Expanding the characteristic determinant along the effort row, the minor associated with $z(t-\tau_M)$ is exactly $L(\lambda)e^{-\lambda\tau_M}$ — the cofactor of the memory row, the same cofactor that produced (5) — and likewise for $\tau_p$. □

**Proposition 5.2 (Weighted small gain).** *Assume*

*(H1) the undelayed interpolation is stable (Hurwitz at $\tau_M = \tau_p = 0$),*

*(H2) the zero root is excluded ($P(0) - L(0)(C_m + C_p) \neq 0$).*


*If*

@@V32:EQ10@@

*then (9) has no purely imaginary root for any $\tau_M, \tau_p \ge 0$, and — since for retarded equations finitely many roots lie to the right of any vertical line and the right-half-plane root count changes only through imaginary-axis crossings — the equilibrium is exponentially stable for every fixed pair of delays (pointwise in the delays; the decay rate need not be delay-uniform).*


*Proof.* An imaginary root $\lambda = i\omega$ with $\omega > 0$ would satisfy $P(i\omega) = L(i\omega)(C_m e^{-i\omega\tau_M} + C_p e^{-i\omega\tau_p})$; taking moduli and using $|e^{-i\omega\tau}| = 1$,

@@V32:MODBOUND@@

contradicting (10), which is the triangle inequality reversed strictly. The excluded case $\omega = 0$ is covered by the stated zero-root hypothesis; stability at the reference point is the stated undelayed-stability hypothesis; and the stability-switch principle (finitely many roots in the right half-plane, locally constant count off the imaginary axis; Hale and Verduyn Lunel, 1993, Ch. 11) transfers the reference stability to every delay pair. □

**Corollary 5.1 (Mobilising weight, conditional).** *At Candidate A the pure mobilising loop gain exceeds 1 and the pure protective loop gain is 0.080. Assume*

*(H1) the common equilibrium and all linear coefficients depend continuously on $\chi_m$,*

*(H2) the characteristic denominator remains nonzero on the imaginary axis,*

*(H3) the protective endpoint has a strict gain margin.*

*Then there exists a conservative threshold radius $\chi_m^* \in (0,1)$ such that every interpolation with $\chi_m < \chi_m^*$ and $\chi_p = 1 - \chi_m$ satisfies (10): the small-gain exclusion remains valid on a nonzero protective-dominated weight interval. **Claimed:** existence of a sufficient-condition radius. **Not claimed:** identification of the actual onset weight for Hopf frequencies — failure of (10) does not imply Hopf, and $\chi_m^*$ is a sufficient-condition radius, not a physical critical weight. A Hopf of the interpolated system therefore requires a sufficiently large mobilising weight; it cannot be produced by decreasing $\tau_p$ alone.*

The corollary holds exactly under the listed hypotheses. The interpolation family is not otherwise established to preserve a common equilibrium or a nonvanishing denominator, and no promotion of the corollary beyond them is made.

*Proof (in full).* Define the certificate map

@@V32:CERTMAP@@

Hypothesis (H2) keeps the denominator nonzero on the imaginary axis. Because $|L(i\omega)|/|(i\omega-A_N)(i\omega+d)(i\omega-C_E)| = O(\omega^{-2})$ as $\omega \to \infty$, and because the coefficients $A_N, d, C_E$ are bounded uniformly on $[0,1]$ (hypothesis (H1), continuity on a compact set), the tail $\omega > \overline\omega$ contributes less than $F(0)/2$ for some $\overline\omega$ uniformly in $\chi_m$. The supremum is therefore a maximum over the fixed compact range $[\underline\omega, \overline\omega]$, on which the integrand is jointly continuous in $(\omega, \chi_m)$, so $F$ is continuous in $\chi_m$ (the maximum of a jointly continuous function over a fixed compact set is continuous). At the protective endpoint, $F(0)$ is the pure protective loop gain, $0.080 < 1$ (the stated value; hypothesis (H3) is its strict-margin form). Continuity supplies $\varepsilon > 0$ with $F(\chi_m) < 1$ for every $\chi_m < \varepsilon$; the conservative threshold radius is any $\chi_m^* \in (0, \min\{\varepsilon, 1\})$. For $\chi_m < \chi_m^*$ and $\chi_p = 1 - \chi_m$, (10) holds, which is Proposition 5.2's small-gain exclusion, valid for every pair $(\tau_M, \tau_p)$. The final clause follows from the sufficient-condition status of the certificate: on the certified weight range no imaginary root can be produced by any $\tau_p$, so a Hopf of the interpolated system requires $\chi_m \ge \chi_m^*$ — a sufficiently large mobilising weight — and cannot be produced by decreasing $\tau_p$ alone. □

For institutional design this says that, on the interpolated architecture, delay-induced cycles cannot be generated by accelerating the protective response alone; the mobilising weight must first cross a sufficient-condition threshold. This is a sufficient-condition statement, not an empirical calibration, and the actual onset of Hopf frequencies may lie below $\chi_m^*$.

---

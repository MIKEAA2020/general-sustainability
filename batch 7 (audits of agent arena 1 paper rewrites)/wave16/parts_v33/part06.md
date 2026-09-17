
## 6. The Protective Channel

The protective channel is the quota-tracking law of (3). Its behavioural reading for fisheries governance is direct: when an institution observes a deficit signal, effort is restored toward a cap rather than mobilised further; landing pressure is reduced as the signal worsens. The channel acts on the same stock–memory block as the mobilising channel, but with the sign of $C_Z$ reversed and the gain modulus reorganised by the cap calibration. Its local mathematics is qualitatively different. There are no Hopf crossings at any delay at the calibrated point — a no-Hopf theorem — and the channel is stable under annual sample-and-hold review. The implication for institutional design is that, on this architecture, the calibrated quota-tracking law is the protective direction the loop should take, and the only sampled instability it exhibits is a discretisation artefact.

### 6.1 The quota-tracking law and its calibration

The protective law (3) with its calibration is stated in Section 2.5. One interpretation discipline travels with it. The effort variable may be an endogenous industry response, a legal quota-utilisation state, or an actual institutional control, and these interpretations are not interchangeable; the quota-tracking law is an institutional control law.

### 6.2 The no-Hopf theorem

**Theorem 6.1 (Delay-independent local stability of the calibrated quota tracker).** *Consider the Candidate A stock–memory linearisation together with the protective gains of Section 2.5. The statement is pointwise in the declared coefficients — not a theorem for every decreasing cap function or every protective law. The modulus cubic*

@@V32:HCUBIC@@

*has*

@@V32:CCOEF@@

*all positive, with $c_2 c_1 - c_0 = 0.02209 > 0$. Assume*

*(H1) the undelayed Jacobian is Hurwitz,*

*(H2) the zero-root condition holds delay-independently, $P(0) \ne 0$.*

*Then the characteristic quasi-polynomial has no purely imaginary root for any delay $\tau_p \ge 0$, and the equilibrium is exponentially stable for every $\tau_p \ge 0$.*

*Proof.* (a) *Exclude imaginary roots.* At $\lambda = i\omega$ the modulus balance of (5) reads $|P(i\omega)| = |C_Z||L(i\omega)|$; by Theorem 4.1 this is equivalent to $H(\omega^2) = 0$. For the protective channel, $C_E = -0.850336$ and $C_Z = -1.661702$ with the same $A_N = -0.0179$, $d = 0.2$, $B_E = 0.008955$, and the even-pairs cancellation gives

@@V32:HCUBICFULL@@

with $c_2 = A_N^2 + d^2 + C_E^2 = 0.76339$, $c_1 = A_N^2 d^2 + A_N^2 C_E^2 + d^2 C_E^2 - C_Z^2 B_E^2 = 0.028946$, $c_0 = A_N^2 d^2 C_E^2 = 9.278\times10^{-6}$. All three coefficients are strictly positive, so by Descartes' rule of signs $H(x) > 0$ for every $x \ge 0$ and no positive real root exists; no $\omega > 0$ solves the modulus balance. (The Routh–Hurwitz array of $H$, with $c_2 > 0$, $c_2 c_1 - c_0 = 0.02209 > 0$, $c_0 > 0$, is the strictly stronger statement that all roots of $H$ lie in the left half-plane; it is reported for completeness, while the undelayed Jacobian's own stability array is the separate polynomial of step (b) below. A symbolic sufficient condition for the no-root property is $c_1 = A_N^2 d^2 + A_N^2 C_E^2 + d^2 C_E^2 - C_Z^2 B_E^2 \ge 0$, the only coefficient of $H$ that can change sign.)

(b) *Delay-independent stability.* The undelayed linearisation is Hurwitz: its characteristic polynomial is $P(\lambda) - C_Z L(\lambda)$ with $L(\lambda) = B_E\lambda$ (even-pairs cancellation), i.e. $\lambda^3 + 1.0682\,\lambda^2 + c_1'\lambda + c_0'$ with $c_1' = 0.2038$ and $c_0' = 0.00305$; all Routh conditions are satisfied (the protective $C_E = -0.850$ dominates, so the $\lambda^2$-coefficient $-A_N + d - C_E = 1.0682$). Explicitly, the Routh array for $P(\lambda) - C_Z B_E\lambda$ has first column entries $1,\ 1.0682,\ c,\ c_0'$, where $c = (1.0682\,c_1' - c_0')/1.0682$ is the standard third first-column entry of a cubic's Routh array (the quotient $(a_2a_1 - a_0)/a_2$ with $a_2 = 1.0682$, $a_1 = c_1'$, $a_0 = c_0'$), and both $c > 0$ and $c_0' > 0$. The zero root is excluded independently of delay: $P(0) - C_Z L(0) = P(0) \ne 0$ because $L(0) = 0$ and $P(0) = (-A_N)(d)(-C_E) = A_N d C_E \ne 0$. Since (a) shows the imaginary axis is never crossed for any $\tau_p \ge 0$, the stability-switch principle for retarded equations — finitely many characteristic roots lie to the right of any vertical line, and their count is locally constant while no root lies on the imaginary axis, so stability changes only through imaginary-axis crossings (Hale and Verduyn Lunel, 1993, Ch. 11) — transfers the undelayed Hurwitz property of (b) to every fixed delay: the equilibrium is exponentially stable for each $\tau_p \ge 0$, pointwise in $\tau_p$, without a delay-uniform decay rate being claimed. □

The channel-separation reading is the theorem's interpretation: destabilisation by short delay is confined to the mobilising summand, and the protective channel has no periodic branch born from the equilibrium at any delay.

The same conclusion is visible in the loop-gain form. Define

@@V32:GAMMA@@

Then $\Gamma$ is continuous on $[0,\infty)$, $\Gamma(0) = 0$ (since $L(0) = 0$), $\Gamma(\omega) \to 0$ as $\omega \to \infty$ — linear over cubic, $O(\omega^{-2})$: the numerator carries $L(i\omega) = B_E i\omega$ — and a numerically located maximum gives $\sup_\omega \Gamma(\omega) = 0.08011 < 1$, attained at $\omega \approx 0.0589$ yr$^{-1}$ (frequencies in yr$^{-1}$, the unit of $C_E$, $d$, $A_N$; Section 2). The loop-gain exclusion argument of Section 10 then excludes every imaginary root for all delays directly. The maximum is a numerical location, stated as such; the analytic certificate is the Descartes/Routh–Hurwitz argument above.

### 6.3 The iso-gain sign flip

**Proposition 6.1 (Iso-gain sign flip).** *Consider the gated Candidate A linearisation. Replacing $C_Z$ by $-C_Z$, leaving every other coefficient unchanged:*

*(i) leaves $H$ identical (it depends on $C_Z$ only through $C_Z^2$);*

*(ii) leaves the frequencies identical;*

*(iii) shifts each family's fundamental delay by $\pi/\omega$ on the branch that keeps it fundamental: the lower family ($\omega_1 \approx 0.02518$) moves up, $3.666 + \pi/\omega_1 = 128.374$ yr, and the upper family ($\omega_2 \approx 0.03944$) moves down, $150.358 - \pi/\omega_2 = 70.697$ yr, both remaining local Hopfs.*

*The subscripts retain their original-family meaning — $\tau_-$ is the lower family's shifted delay, $\tau_+$ the upper family's — so on the shifted axis the order is reversed: $\tau_+ < \tau_- < \tau_+^{\mathrm{unshifted}}$. The reversed-gain linearisation has loop gain $1.016 > 1$ and retains the factor $\eta E^*/\Delta_{\mathrm{ref}}$: it is **not** the quota law, whose genuine form changes the modulus as well as the sign. The proposition is the paper's sign-phase invariance statement: for a single delayed scalar feedback term $C_Z L(\lambda) e^{-\lambda\tau}$, replacing $C_Z$ by $-C_Z$ leaves the imaginary-root frequency equation unchanged and shifts every admissible delay branch by an odd half-period — consequently, **feedback sign alone cannot create or eliminate Hopf-frequency families over the unrestricted delay axis**, and the protective no-Hopf property of Theorem 6.1 is a property of the quota law's modulus (its direct damping and delayed gain), not of its sign.*

This is the false-reversal identification hazard: a pure sign flip is not a protective institution, and attributing the reversed-gain crossings to a quota tracker would confuse two different effort laws.

*Proof (in full).* The imaginary-root condition of the gated Candidate A linearisation is $P(i\omega) - C_Z L(i\omega) e^{-i\omega\tau} = 0$ with the polynomials of (5). Separating modulus and phase,

@@V32:PHASEEQ@@

The modulus equation depends on the effort coupling only through $|C_Z| = |-C_Z|$, so the frequency equation — the cubic in $x = \omega^2$ of Section 4 — and its certified positive roots are unchanged by the flip; the phase equation changes by exactly $\pi$, so every admissible delay branch is translated by an odd half-period, $(2k+1)\pi/\omega$. The certified fundamental pair and its frequencies are $(\tau_-, \tau_+) = (3.666149, 150.358477)$ yr and $(\omega_1, \omega_2) = (0.0251915, 0.0394366)$ (Section 5.1). The fundamental branch of each family is its smallest positive representative, which for the flipped gain is

@@V32:FLIPDELAYS@@

the lower family moving up and the upper family moving down, as stated. Both shifted crossings remain simple and transverse — the certified evaluation gives $\mathrm{d}\,\mathrm{Re}\,\lambda/\mathrm{d}\tau = -6.07\times10^{-6}$ at $(\omega_1, 128.374)$ and $+1.83\times10^{-5}$ at $(\omega_2, 70.697)$, both nonzero — so each remains a local Hopf point of the flipped system. The invariance of the frequency equation is the stated sign-phase invariance: over the unrestricted delay axis the families are translated, never created or destroyed, and the protective no-Hopf property of Theorem 6.1 is accordingly a property of the quota law's modulus — its direct damping and delayed gain — not of its sign. □

### 6.4 Sampled protection and the discretisation crossing

**Proposition 6.2 (Protective Euler-reviewed zero-order-hold monodromy).** *Replace the protective delayed feedback by sample-and-hold of period $T_r$ with one explicit Euler review step — an Euler-reviewed zero-order-hold controller, one particular sampled-data implementation among many (the standard reviewed controller of computer-controlled systems; Åström and Wittenmark, 1997), not sample-and-hold governance in general. Between reviews the variational system is $\dot\xi = A_{\mathrm{hold}}\xi$ with*

@@V32:AHOLD@@

*(the effort is frozen between reviews), and at each review — at the end of the interval, on the flowed state (the flow-then-update convention of Section 8) — the effort update is the explicit Euler step $e_{k+1} = e_k + T_r\big(C_E e_k + C_Z z(t_{k+1}^-)\big)$. The monodromy of one review interval is therefore*

@@V32:EQ11@@

*Proof.* On one interval $[kT_r, (k+1)T_r)$ the frozen-effort system is linear with matrix $A_{\mathrm{hold}}$ (the effort row is zero), so the state at the end of the interval is $\exp(A_{\mathrm{hold}}T_r)\xi_k$; the review then applies the affine update $\xi_{k+1} = \xi(t_{k+1}^-) + T_r(C_E e_{k+1}^- + C_Z z_{k+1}^-)\,\mathbf{e}_3$, i.e. the matrix factor displayed in (11). The sampled equilibrium is exponentially stable iff every eigenvalue of $M_p(T_r)$ lies in the open unit disc. □*

At the protective gains, $\rho(M_p(1)) = 0.9838 < 1$: annual review of the quota-tracking channel is linearly stable at Candidate A. On the grid $T_r \in [0.2, 20]$, the spectral radius is strictly below one on $[0.2, 2.306)$ and strictly above one on $(2.306, 20]$, so the Euler hold map crosses $\rho = 1$ at $T_r \approx 2.306$ (a grid resolution).

That crossing is carried by the discretisation, not by the governance system. Specifically, it comes from the interaction of the Euler-update factor $(1 + T_r C_E)$ with the hold flow $\exp(A_{\mathrm{hold}}T_r)$ — the $C_E$ row of the update restoring the coupling that the hold flow's zero third row lacks — and not from the scalar condition $1 + T_r C_E = 0$ alone, which (with $C_E = -0.850$) would place a threshold near $T_r \approx 1.176$, not at $2.306$. So the crossing is a property of the Euler factor *combined with* the hold dynamics. It also sits within about $2\%$ of the explicit-Euler stability limit of the scalar effort equation, $T_r < 2/|C_E| = 2.352$ yr (with $C_E = -0.850336$; the limit at which the scalar factor $1 + T_r C_E$ itself reaches $-1$), which makes the discretisation origin of the crossing self-evident. It is **not** a Hopf point of the protective delay equation, whose continuous spectrum Theorem 6.1 excludes at every delay. The finding is the mathematical statement: the $T_r = 2.306$ crossing belongs to the discretisation. The separating computation confirms it: under the exact held-measurement update (Proposition 8.1) the protective monodromy has spectral radius below one at every tested review interval — 0.9838 at $T_r = 1$ yr and at most 0.9967 on $[0.2, 300]$ yr — so the crossing is carried entirely by the explicit-Euler command step, and the protective channel's sampled stability is not cadence-limited. The operator-specific scope is recorded: the mobilising hold map is unstable at $T_r = 1$ because the undelayed mobilising Jacobian is already unstable, and the protective map does not inherit that instability (Section 8).

### 6.5 Channel-specific pacing

**Corollary 6.1 (Channel-specific pacing).** *Three pacing statements hold.*

*(i) For the mobilising bracket the equilibrium is linearly unstable for $0 < \tau < \tau_-$.*

*(ii) For the protective law at Candidate A the equilibrium is linearly stable for every $\tau_p \ge 0$.*

*(iii) For the two-channel system, in every connected parameter region where the undelayed interpolation is stable, the zero root is excluded, and the strict weighted small-gain bound (10) holds, stability is independent of both delays — any delay-induced stability loss must occur outside that certified region.*

*Proof.* The first clause is Section 5.1 (undelayed instability with a stabilising lower crossing at $\tau_-$). The second is Theorem 6.1. The third is Proposition 5.2 together with Corollary 5.1: wherever (10) holds, no imaginary root exists for any $(\tau_M, \tau_p)$, so instability — if present — must originate in parameter regions where the mobilising weight is large, and is independent of the protective delay there. The synthesis inherits Corollary 5.1's interpolation hypotheses wherever its clause applies. □*

The policy-scope reading, instantiated: faster protective governance is not the hazard — the mobilising sign is.

---

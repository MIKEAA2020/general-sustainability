
## 3. Equilibria and the Characteristic Equation

### 3.1 The interior equilibrium and the extinction face

At any interior equilibrium $qE^*N^* = S(N^*)$, the signal argument vanishes, the floor is inactive, and

@@V32:ZSTAR@@

independent of $\tau_m$, $k$, and $(N^*, E^*)$. Substituting into $\dot E = 0$ (away from $E = E_{\max}$) produces

@@V32:EQ_ESTAR@@

whose constant term is positive and quadratic coefficient negative, so there is exactly one positive root. Admissibility requires $0 < E^* < \min\{E_{\max}, r/q\}$, and then $N^* = K(1 - qE^*/r)$, positive iff $qE^* < r$. The equilibrium is independent of $\tau$ and $k$, which does not make its stability delay-independent. One certified value is used throughout: at Candidate A the positive quadratic root is $E^* = 2.08962$ and $N^* = K(1 - qE^*/r) = 89.55188$, with $Z^* = \delta \approx 0.0693$. (The four-state donor-limited equilibrium of Section 9.4, $N^* = 89.52562$, $A^* = 397.8665$, is a distinct object and is never used as the three-state rest.)

On the extinction face $N = 0$ the same zero raw signal gives $Z = \delta$, and the gated law has both the interior-effort extinction rest $(0, \delta, E^*)$ — when the interior root is admissible — and the boundary rest $(0, \delta, E_{\max})$ created by the multiplicative gate. The stock-direction eigenvalue at either branch is $r - qE$. The interior positive-stock branch exchanges stock-direction stability with the interior-effort extinction branch at the transcritical point $r = qE^*$, while the $E = E_{\max}$ boundary branch is classified separately and is not part of that exchange. The survival condition $r > qE^*$ is identical to $N^* > 0$; interior and extinction branches are not simultaneously stable.

### 3.2 The characteristic quasi-polynomial

With $x = N - N^*$, $z = Z - Z^*$, $e = E - E^*$, $\mathrm{sp}_k'(0) = 1/2$, and the floor inactive at $\delta > 0$, the linearisation of (1) is

@@V32:LINFIRST@@

with

@@V32:LINCOEF@@

The gate factors $(1 - E^*/E_{\max})$ distinguish the gated from the ungated variant and are the algebraic source of threshold relocation between the two. Substituting the modal ansatz $(x,z,e)e^{\lambda t}$ and expanding the $3 \times 3$ characteristic determinant along the third row gives the characteristic quasi-polynomial

@@V32:EQ5@@

with $d = 1/\tau_m$. At the interior equilibrium the filter identities hold:

@@V32:FILTERID@@

because the deficit signal is $qEN - S(N) = -A_N x - A_E e + o(\cdot)$ and $\mathrm{sp}_k'(0) = 1/2$. Consequently

@@V32:LCANCEL@@

since $B_E A_N = A_E B_N$. This cancellation — the even-pairs algebra below — is the structural identity of the architecture.

---

## 4. The Complete Hopf Cubic

The Hopf-frequency equation of the linearised system (5) takes a particularly clean form on this architecture: a cubic in $x = \omega^2$ for the modulus, plus a phase relation in $\tau$. The cubic has at most three positive roots, so the system supports at most three Hopf-frequency families. The interior equilibrium's filter identity then collapses one structural term, and the resulting even-pairs algebra explains why, generically, two crossings are observed rather than one or three.

**Theorem 4.1 (Cubic modulus condition and phase branches).** *Consider the linearisation (5). Assume*

*(H1) $C_Z L(i\omega) \neq 0$ at every candidate imaginary root. This is automatic on the declared family: by the filter identity of Section 3.2, $L(i\omega) = B_E i\omega$, so $C_Z L(i\omega) = 0$ only at $\omega = 0$, which is excluded by $\omega > 0$; the degenerate case $C_Z B_E = 0$ is excluded by the standing assumptions. Hypothesis (H1) is stated for completeness, to make the phase balance (7) well defined; it imposes no additional restriction here.*

*Then $\lambda = i\omega$ ($\omega > 0$) is a characteristic root of (5) if and only if $x = \omega^2$ is a positive root of*

@@V32:EQ6@@

*and*

@@V32:EQ7@@

*A cubic has at most three positive roots, so there are at most three Hopf-frequency families; higher branches recur within a family as $\tau_{n,0} + 2\pi k/\omega_n$ and are not additional frequencies. The certified branch pairs are separated — $\tau_{1,k} \neq \tau_{2,\ell}$ over the declared search range — so simultaneous double-Hopf collisions are excluded on the computed set (computed on the declared search range; not an algebraic consequence of the cubic). Simplicity and transversality are verified separately for each reported crossing.*

*Proof.* At $\lambda = i\omega$, equation (5) reads $P(i\omega) = C_Z L(i\omega)e^{-i\omega\tau}$, so the moduli must match:

@@V32:EQ8@@

Compute $|P(i\omega)|^2 = |(i\omega - A_N)(i\omega + d)(i\omega - C_E)|^2 = (\omega^2 + A_N^2)(\omega^2 + d^2)(\omega^2 + C_E^2)$, and $L(i\omega) = B_E i\omega + (A_E B_N - A_N B_E)$, whence $|L(i\omega)|^2 = B_E^2\omega^2 + (A_E B_N - A_N B_E)^2$. Substituting into (8) and writing $x = \omega^2$ gives exactly (6). Given a positive root $x$ of (6), the phase condition reads $e^{-i\omega\tau} = P(i\omega)/(C_Z L(i\omega))$; since both sides have unit modulus on the root locus, $\tau$ is recovered as (7) up to the $2\pi k$ ambiguity. A cubic has at most three positive roots, giving at most three frequency families; for a fixed family $\omega_n$ the delays $\tau_{n,0} + 2\pi k/\omega_n$ recur with period $2\pi/\omega_n$ in $\tau$, and are branches of the same frequency, not additional frequencies. Candidates qualify as Hopf crossings only after simplicity and transversality are verified separately; the cubic determines neither criticality nor global folds. □

**Corollary 4.1 (Even pairs).** *At the interior equilibrium of (1), the cross term vanishes identically, $A_E B_N - A_N B_E \equiv 0$, so*

@@V32:HEVEN@@

*Assume $A_N d C_E \neq 0$ (nonzero filter rate, memory rate, and equilibrium effort derivative). Then $H(0) = A_N^2 d^2 C_E^2 > 0$ and $H(x) \to +\infty$; the total algebraic multiplicity of the strictly positive roots of $H$ is even, and generically $H$ has zero or two distinct simple positive roots. The double-root boundary — the birth or annihilation of a Hopf-frequency pair — solves $H(x) = H'(x) = 0$.*

*Proof.* The identities $B_N = -A_N/(2\tau_m)$, $B_E = -A_E/(2\tau_m)$ give $A_E B_N - A_N B_E = -A_E A_N/(2\tau_m) + A_N A_E/(2\tau_m) = 0$. With the cross term zero, $H$ has the stated form, and $H(0) > 0$ follows from the nondegeneracy assumption. A polynomial with positive value at $0$ and positive leading coefficient crosses the positive axis an even number of times counting multiplicity, which is the multiplicity claim; a single positive double root is the degenerate residual case and sits on the boundary $H = H' = 0$. □

For both Candidate A and Candidate B the cubic has exactly two positive roots on both the gated and the ungated variant; the certified local spectrum is stated in Section 5.1.

### 4.1 The scalar archetype

Two general statements frame the delay mathematics. First, the scalar Hayes result (Hayes, 1950; Hale and Verduyn Lunel, 1993, Ch. 3): for $\dot x = -ax - Bx(t-\tau)$ with $a > 0$, $B \ge 0$, the zero equilibrium is stable for all $\tau \ge 0$ if $B \le a$; if $B > a$ it is stable for $\tau < \tau_{\mathrm{crit}} = \arccos(-a/B)/\sqrt{B^2 - a^2}$ and unstable beyond, with *no restabilisation* as $\tau$ grows — the crossing is destabilising. This is the scalar mechanism by which loop delay destroys stability that undelayed feedback sustains. Second, no delay conclusion is sign-free: the systems $\dot x = -ax - bx(t-\tau)$ and $\dot x = -ax + bx(t-\tau)$ ($a, b > 0$) have different feedback signs and different stability properties. The named systems of this paper instantiate the two signs — the mobilising law of (1) carries $C_Z > 0$, the protective law (3) carries $C_Z < 0$ — and Sections 5–6 show that the local mathematics separates accordingly.

---

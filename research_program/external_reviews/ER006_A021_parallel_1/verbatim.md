# External Review ER006 — A021 RFDE Proof, Parallel Response 1

## Specialist assessment

The central diagnosis is substantially correct: the original vertical-graph claim is not justified by boundedness of the binding histories and exponential stability of the slack equilibrium. In particular, the compact-manifold and full-normal-hyperbolicity hypotheses are missing.

However, the proposed replacement is **not yet publication-ready**. Theorem 2 is generally false as stated, Theorem 3 needs stronger and more precise hypotheses, and the Hopf statement conflates the coupling parameter with the bifurcation parameter.

# 1. Corrections to Output A

### A.1 needs a qualification

The statement

\[
C([-\tau,0],K_x)\quad\text{is not compact}
\]

is true for the intended nontrivial \(K_x\), but not for every compact \(K_x\). For example, if \(K_x\) is finite and totally disconnected, every continuous map from the connected interval \([-\tau,0]\) into \(K_x\) is constant, so the history set is finite and compact.

A precise formulation is:

> Compactness does not follow from compactness of \(K_x\). If \(K_x\) contains a nontrivial path, then \(C([-\tau,0],K_x)\) is generally noncompact because no uniform modulus of continuity is imposed.

The broader objection remains valid.

### A.4 should not overstate what is impossible

Backward uniqueness is required by a classical two-sided Lyapunov–Perron construction, but not by every persistence theorem for semiflows. There are normally attracting/inflowing invariant-manifold theorems designed for noninvertible semiflows.

Thus the correct conclusion is:

> A theorem for diffeomorphisms or two-sided flows cannot be used without additional assumptions. One must instead invoke a persistence theorem specifically formulated for semiflows, or impose invertibility on the dynamics restricted to the base manifold.

# 2. Theorem 1: valid after minor repairs

The finite-time estimate is the strongest clearly defensible unconditional result, but its assumptions and estimate should be sharpened.

## 2.1 Compact confinement is unnecessarily strong

If a common compact subset of \(B_0\) contains every trajectory starting in \(U\), then it contains \(U\) at \(t=0\); hence \(U\) is relatively compact, not merely bounded.

More natural assumptions are:

- the trajectories remain in a common neighborhood \(V\Subset B_0\);
- \(F,G,f,g\) are uniformly bounded and uniformly Lipschitz on \(V\).

In infinite-dimensional Banach spaces, continuity or \(C^1\) regularity does not imply boundedness on bounded sets.

## 2.2 The estimate should include differing initial histories

The clean version is

\[
\sup_{0\le t\le T}\|z^\varepsilon_t-z^0_t\|_B
\le
C_T\left(
\|z^\varepsilon_0-z^0_0\|_B+|\varepsilon|
\right).
\]

Then the assertion about an initial \(y\)-history that is \(O(\varepsilon)\)-close to \(\widehat y_*\) follows directly. As currently written, the proof assumes identical initial histories, while the subsequent sentence allows different \(y\)-histories.

# 3. Theorem 2 is not established and is false in the stated generality

This is the most serious remaining defect.

## 3.1 The proposed graph transform is not defined

The expression

\[
\operatorname{graph}(\Gamma_\varepsilon h)
=
P_\varepsilon(\operatorname{graph}h)
\cap(K_{M,L}\times Y)
\]

does not ensure that the right-hand side is the graph of a function. It may have:

- no point over some base history;
- several points over the same base history;
- base points outside \(K_{M,L}\).

The assumption that \(K_{M,L}\) is positively invariant under the **unperturbed binding map** does not imply that the \(x\)-projection of

\[
P_\varepsilon(\operatorname{graph}h)
\]

is \(K_{M,L}\), or even lies in \(K_{M,L}\), because the perturbed \(x\)-equation depends on \(y\).

## 3.2 Fibre contraction alone does not produce a graph over a noninvertible base

For a genuine skew product

\[
P(x,y)=(q(x),H(x,y)),
\]

the invariant graph equation is

\[
h(q(x))=H(x,h(x)).
\]

If \(q\) is a homeomorphism, one may define

\[
(\Gamma h)(x)
=
H(q^{-1}x,h(q^{-1}x)).
\]

If \(q\) is noninvertible, different preimages of \(x\) may impose incompatible values of \(h(x)\). Fibre contraction does not remove this compatibility obstruction. One generally obtains a graph over the inverse-limit space, not necessarily over \(K_{M,L}\) itself.

The actual coupled RFDE is not even a skew product, since the \(x\)-component depends on \(y\).

## 3.3 Time-\(T\) invariance does not automatically imply semiflow invariance

From

\[
P_\varepsilon(M)=M
\]

one only obtains

\[
P_\varepsilon(\Phi_\varepsilon^tM)
=
\Phi_\varepsilon^tM.
\]

To conclude \(\Phi_\varepsilon^tM=M\), one needs a local uniqueness theorem showing that \(\Phi_\varepsilon^tM\) belongs to the same admissible class. That is not supplied by “concatenation.”

## 3.4 Correct replacement for Theorem 2

A valid elementary graph theorem would require, for example:

1. a compact metric base \(K\);
2. a homeomorphism \(q:K\to K\);
3. a true skew product
   \[
   P_\varepsilon(x,y)
   =
   \bigl(q_\varepsilon(x),H_\varepsilon(x,y)\bigr);
   \]
4. uniform contraction of \(H_\varepsilon\) in \(y\);
5. suitable Lipschitz estimates in \(x\).

Alternatively, for a noninvertible base, the graph should be constructed over its inverse limit, together with a separate argument showing that it descends to the original phase space.

Consequently, Theorem 2 should be removed or relabelled as a conjectural route with these additional hypotheses.

# 4. Theorem 3 needs stronger hypotheses

The conditional NHIM route is conceptually correct, but the stated rate and regularity assumptions are insufficient.

## 4.1 Forward tangent growth alone is not the required bunching condition

The estimates

\[
\|DP_0|_{E^s}\|\le M_se^{-\beta T},
\qquad
\|DP_0|_{TM_0}\|\le M_ce^{\alpha T}
\]

do not control the inverse tangent dynamics. For a normally attracting invariant manifold whose internal map is invertible, the relevant \(C^k\) condition is of the form

\[
\sup_{p\in M_0}
\|DP_0(p)|_{E_p^s}\|
\,
\left\|
\bigl(DP_0(p)|_{T_pM_0}\bigr)^{-1}
\right\|^k
<1,
\qquad 0\le k\le r,
\]

possibly after passing to an iterate.

Thus \(\beta>r\alpha\) is adequate only if \(\alpha\) has been defined to control the appropriate backward tangent expansion, not merely the forward norm.

For a genuinely noninvertible restricted semiflow, the assumptions must instead be those of a specific normally attracting semiflow theorem.

## 4.2 \(C^1\)-smallness alone does not yield the stated \(C^r\) conclusion quantitatively

To obtain a \(C^r\) persistent manifold, one normally needs:

- \(P_\varepsilon\) to be \(C^r\);
- uniform \(C^r\) bounds on a common neighborhood;
- the required \(r\)-bunching inequalities;
- at least \(C^1\)-smallness for persistence, with higher-order control for quantitative \(C^r\) estimates.

The conclusion

\[
\|\iota_\varepsilon-\iota_0\|_{C^1}=O(\varepsilon)
\]

also does not follow from \(F,G,f,g\in C^1\) alone. Comparing variational equations involves terms such as

\[
DF(z_\varepsilon)-DF(z_0).
\]

Continuity of \(DF\) gives \(o(1)\), but not necessarily \(O(\varepsilon)\). An \(O(\varepsilon)\) derivative estimate requires, for example, \(C^{1,1}\) or \(C^2\) regularity with uniform bounds.

## 4.3 “The external theorem applies verbatim” is tautological

Assumption 4 currently says, in effect, that the desired theorem applies. It should be replaced by the exact hypotheses of a named theorem, including:

- whether the theorem concerns maps or semiflows;
- whether the restricted dynamics must be invertible;
- the boundary condition;
- the precise normal-hyperbolicity inequalities;
- regularity and bounded-geometry assumptions;
- the admissible perturbation topology.

This is particularly important because the RFDE time-\(T\) map is compact and generally not a local diffeomorphism on the ambient history space.

## 4.4 Compact Banach submanifolds are necessarily finite-dimensional

A compact embedded Banach manifold cannot have positive infinite Banach dimension, since infinite-dimensional Banach spaces are not locally compact. Thus \(\mathcal A_x\) in Theorem 3 is necessarily finite-dimensional. It is clearer to state this explicitly.

## 4.5 Projection transversality needs a global argument

Smallness of

\[
D\pi_x|_{TM_\varepsilon}
\]

gives local invertibility, not automatically global injectivity. For compact \(\mathcal A_x\), one can obtain the desired conclusion if the NHIM is parameterized by an embedding

\[
\iota_\varepsilon:\mathcal A_x\to X\times Y
\]

such that

\[
\pi_x\circ\iota_\varepsilon
\]

is sufficiently \(C^1\)-close to the original embedding \(\mathcal A_x\hookrightarrow X\). One then proves that this map remains an embedding and hence is a diffeomorphism onto its image.

This does not follow merely from a choice of normal complement.

# 5. RFDE regularity and compactness statements need qualification

The blanket statement

> “For \(t>\tau\) the operators are compact”

should be localized. What is generally available is that the time-\(t\) solution operator maps appropriately bounded sets of solutions into relatively compact sets, because solution segments acquire a uniform derivative bound. Global compactness requires uniform bounds ensuring that all relevant trajectories exist and remain in a region where the RFDE right-hand side is uniformly bounded.

Likewise, \(C^r\) smoothness of the solution map should be tied to a standard RFDE theorem and its exact phase-space hypotheses. For state-dependent delays or neutral equations, the phase space and smoothness theory are substantially different; fortunately, the present text excludes those cases.

# 6. Hopf theorem requires revision

The direct full-RFDE Hopf route is preferable, but Theorem 5 currently mixes two parameters.

Let \(\mu\) denote the distinguished Hopf parameter and \(\varepsilon\) the coupling. The correct setup is

\[
\lambda=\lambda(\mu,\varepsilon),
\qquad
\operatorname{Re}\lambda(\mu_*,0)=0,
\]

with transversality

\[
\partial_\mu\operatorname{Re}\lambda(\mu_*,0)\ne0.
\]

The implicit-function theorem then gives a Hopf curve

\[
\mu=\mu_*(\varepsilon),
\qquad
\mu_*(\varepsilon)=\mu_*+O(\varepsilon).
\]

It is generally incorrect to require

\[
\alpha'(0)\ne0
\]

where the derivative is taken with respect to \(\varepsilon\). The coupling may move the eigenvalue tangentially or not at all; Hopf persistence only requires nonzero crossing with respect to \(\mu\).

Additional repairs:

1. The equilibrium curve requires invertibility of the equilibrium derivative. This follows if \(\lambda=0\) is excluded from the characteristic spectrum, but should be stated.
2. A classical smooth Hopf branch requires sufficient smoothness, usually at least \(C^3\) for normal-form conclusions.
3. To claim a nondegenerate, locally unique branch with a specified criticality, one must assume the first Lyapunov coefficient is nonzero.
4. Spectral continuity can be formulated directly using the finite-dimensional characteristic matrix for a retarded finite-delay equation; an unspecified “operator norm on the appropriate exponential-weight space” is unnecessary unless a more general functional equation is intended.

A corrected statement is:

> If the full RFDE depends \(C^k\)-smoothly on \((\mu,\varepsilon)\), \(k\ge3\), has an equilibrium near \(z_*\), possesses at \((\mu_*,0)\) a simple pair \(\pm i\omega_*\) with no other imaginary roots, and
> \[
> \partial_\mu\operatorname{Re}\lambda(\mu_*,0)\ne0,
> \]
> then there is a local Hopf curve
> \[
> \mu_*(\varepsilon)=\mu_*+O(\varepsilon).
> \]
> If the first Lyapunov coefficient is nonzero, the corresponding nondegenerate branch of periodic solutions persists.

# 7. Yield-parity conclusion

Output F is appropriately cautious. The correct conclusion is only that the specific estimate

\[
C_{\mathrm{gap}}e^{-\rho\Delta_y}
\]

ceases to provide exponential smallness when \(\Delta_y=0\). It does not rule out:

- a small numerical prefactor \(C_{\mathrm{gap}}\);
- cancellation;
- symmetry-based invariant manifolds;
- averaging;
- center-manifold reductions;
- a different spectral-gap mechanism.

The current text already makes this distinction correctly.

# 8. Corrected hierarchy of valid claims

The final hierarchy should be:

1. **Finite-time tracking:** valid under uniform local boundedness and Lipschitz assumptions.
2. **Lipschitz invariant graph:** not established for the coupled RFDE; requires a true skew-product/invertible-base structure, an inverse-limit formulation, or a separate invariant-manifold theorem.
3. **Conditional NHIM persistence:** valid only after specifying and verifying the hypotheses of an appropriate Banach-space semiflow theorem, including the full normal bundle and correct bunching inequalities.
4. **Vertical graph:** follows only after proving that the \(x\)-projection of the persistent manifold is globally an embedding.
5. **Direct Hopf persistence:** valid independently of the NHIM after introducing a separate bifurcation parameter and imposing the standard RFDE Hopf hypotheses.
6. **Yield parity:** destroys the stated exponential-smallness mechanism, but no broader nonexistence conclusion follows.

## Final verdict

The critique of the original A021 claim is fundamentally sound, especially regarding compactness, manifold structure, the incomplete normal bundle, and the nonautomatic vertical projection. But the document overstates what has subsequently been proved:

- Theorem 1 is repairable.
- Theorem 2 is not valid as stated.
- Theorem 3 is a reasonable conditional template but needs exact semiflow hypotheses, inverse-tangent bunching, and stronger regularity assumptions.
- The Hopf theorem needs separate coupling and bifurcation parameters.

Accordingly, the sentence claiming that both Theorems 1 and 2 are proved should be replaced by the statement that **finite-time \(O(\varepsilon)\) tracking is the only unconditional theorem presently established**.

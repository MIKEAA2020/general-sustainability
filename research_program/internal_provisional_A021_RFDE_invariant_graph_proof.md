# Internal Provisional A021 RFDE Proof Attempt

## Status

This is the programme’s internal proof attempt for comparison with forthcoming external responses. It is **not an implementation decision**. No A021 source, flagship text, action status, or publication claim should be changed from this document until the external responses and this attempt are jointly adjudicated.

## Executive result

The original A021 invariant-graph theorem does not follow from its stated assumptions. The strongest results I can currently justify are:

1. a complete finite-time \(O(\varepsilon)\) binding-block tracking theorem, requiring no invariant graph;
2. a conditional compact-NHIM persistence theorem obtained by matching the A021 RFDE semiflow to a Banach-semiflow persistence theorem, but only after adding a genuine compact invariant binding manifold, the full normal splitting, and normal/tangent domination;
3. a direct local characteristic-root/Hopf persistence theorem that does not require the invariant graph;
4. failure of the yield-gap reduction at parity only in the sense that its small parameter disappears.

The compact-NHIM theorem is much narrower than the original claim. It gives a graph over the **perturbed projected base**, not automatically over the old set of all binding histories.

---

# 1. Diagnosis of the original claim

## 1.1 Bounded history sets are not compact

Let \(K=[-1,1]\) and define

\[
\phi_n(\theta)=\sin(n\theta),
\qquad \theta\in[-\tau,0].
\]

Then \(\phi_n\in C([ -\tau,0],K)\) and the sequence is uniformly bounded, but it is not equicontinuous and has no uniformly convergent subsequence. Therefore

\[
C([ -\tau,0],K)
\]

is not compact in the supremum norm merely because \(K\) is compact.

The original proof’s “compact absorbing history set” step is therefore invalid unless it supplies equicontinuity or an actually compact invariant history object.

## 1.2 Stable slack dynamics do not establish normal hyperbolicity

Suppose the slack variational dynamics contract at rate \(\beta>0\), while tangent vectors along the binding dynamics can grow at rate \(\alpha\ge0\). Normal attraction requires the theorem-specific domination condition, at least of the form

\[
\beta>\alpha
\]

for \(C^1\) persistence and a stronger \(r\)-normal inequality for \(C^r\) persistence. The original assumptions provide \(\beta\) but no bound on \(\alpha\).

This omission is substantive. A tangent cocycle with expansion faster than the slack contraction is not normally attracting in the required sense, even though the isolated slack equilibrium is exponentially stable.

## 1.3 The normal bundle is incomplete

If the binding base \(\mathcal A_x\subset\mathcal X\) is a proper submanifold, its normal bundle includes directions in \(\mathcal X\) transverse to \(T\mathcal A_x\). The original argument treated only \(\mathcal Y\) as normal. That is valid only in a separate skew-product/open-base graph theorem or after all transverse \(x\)-directions are included and controlled.

## 1.4 An RFDE gives a semiflow

RFDE solution maps on \(C([ -\tau,0],\mathbb R^d)\) are generally forward semiflows. They need not have unique backward continuations. A Lyapunov–Perron construction over current base histories may therefore be multivalued unless the base restriction is a two-sided flow, possesses unique complete trajectories, or the theorem is formulated as a one-sided inflowing/overflowing persistence result.

## 1.5 Persistence need not be vertical over the old base

Even in finite dimensions, a persistent invariant set generally moves in every normal direction. For example,

\[
\dot x=-x+\varepsilon,
\qquad
\dot y=-2y
\]

has unperturbed invariant point \((0,0)\), while the perturbed point is \((\varepsilon,0)\). It is not a graph over the unchanged old base \(x=0\). One first obtains a nearby embedding; a vertical graph follows only after proving the coordinate projection is a diffeomorphism onto the perturbed projected base.

## 1.6 Conclusion of the diagnosis

The original assumptions—small yield-gap coupling, a stable slack equilibrium, and bounded absorbing state sets—are insufficient for a \(C^1\) RFDE invariant graph. They do support a finite-time perturbation estimate.

---

# 2. A theorem that is fully provable now: finite-time tracking

## Theorem 2.1 — Finite-time binding-block perturbation

Let

\[
\mathcal X=C([ -\tau,0],\mathbb R^m),
\qquad
\mathcal Y=C([ -\tau,0],\mathbb R^n).
\]

Consider

\[
\dot x^\varepsilon(t)
=F(x_t^\varepsilon)
+\varepsilon f(x_t^\varepsilon,y_t^\varepsilon),
\]

and the uncoupled binding equation

\[
\dot x^0(t)=F(x_t^0),
\]

with the same initial binding history

\[
x_0^\varepsilon=x_0^0=\phi.
\]

Assume that on \([0,T]\):

1. both solutions exist and remain in domains on which \(F\) is Lipschitz with constant \(L\) in the history norm;
2. \(f\) is bounded by \(M\) along the coupled solution;
3. \(y^\varepsilon\) exists on \([0,T]\).

Then

\[
\sup_{0\le t\le T}
\|x_t^\varepsilon-x_t^0\|_\infty
\le
\begin{cases}
\displaystyle
\frac{\varepsilon M}{L}
(e^{LT}-1),&L>0,\\[1.2ex]
\varepsilon MT,&L=0.
\end{cases}
\tag{2.1}
\]

Consequently, if

\[
\varepsilon
=C_{gap}e^{-\rho\Delta_y}
+\varepsilon_{phys},
\]

then the binding block is \(O(e^{-\rho\Delta_y}+\varepsilon_{phys})\)-close on every fixed finite horizon for which the common enclosure assumptions hold.

### Proof

Set

\[
e(t)=x^\varepsilon(t)-x^0(t)
\]

and

\[
E(t)
=
\sup_{-\tau\le s\le t}|e(s)|.
\]

Because the initial histories coincide, \(E(0)=0\). For \(t\in[0,T]\),

\[
|e(t)|
\le
\int_0^t
|F(x_s^\varepsilon)-F(x_s^0)|\,ds
+
\varepsilon
\int_0^t
|f(x_s^\varepsilon,y_s^\varepsilon)|\,ds.
\]

Using the assumptions,

\[
|e(t)|
\le
L\int_0^t
\|x_s^\varepsilon-x_s^0\|_\infty\,ds
+
\varepsilon Mt
\le
L\int_0^tE(s)\,ds+
\varepsilon Mt.
\]

Taking the supremum up to time \(t\) gives

\[
E(t)
\le
L\int_0^tE(s)\,ds+
\varepsilon Mt.
\]

Gronwall’s inequality yields

\[
E(t)
\le
\frac{\varepsilon M}{L}(e^{Lt}-1)
\]

when \(L>0\), and direct integration gives \(E(t)\le\varepsilon Mt\) when \(L=0\). Evaluating at \(T\) proves (2.1). \(\square\)

## Limitation

This theorem proves neither an invariant graph nor all-time tracking. The constant can grow rapidly with \(T\), and the common enclosure must be established independently.

---

# 3. Conditional invariant-manifold theorem

The following result is valid only under substantially stronger assumptions. It is an application of Banach-semiflow normally hyperbolic persistence, not a consequence of the original A021 hypotheses.

## Hypotheses NH

Let \(\Phi_\varepsilon^t\) be the local semiflow on

\[
\mathcal B=\mathcal X\times\mathcal Y
\]

generated by the coupled RFDE.

Assume:

### NH1 — Smooth semiflow

For some \(r\ge1\), \(\Phi_\varepsilon^t\) is a \(C^r\) semiflow on an open neighborhood \(U\subset\mathcal B\) for the times required by the persistence theorem, and

\[
\sup_{0\le t\le T_0}
\|\Phi_\varepsilon^t-
\Phi_0^t\|_{C^1(U)}
\le C\varepsilon.
\]

### NH2 — Genuine compact invariant binding manifold

The uncoupled binding semiflow has a compact \(C^r\) invariant manifold

\[
\mathcal A_x\subset\mathcal X.
\]

The restriction of the semiflow to this manifold has the forward/backward or inflowing/overflowing structure required by the selected persistence theorem.

### NH3 — Product manifold

The slack equilibrium \(\widehat y_*\) is hyperbolic for the slack RFDE, and

\[
\mathcal M_0
=
\mathcal A_x\times\{\widehat y_*\}
\]

is a compact \(C^r\) invariant manifold of the product semiflow.

### NH4 — Full invariant splitting

There is a continuous invariant splitting

\[
T\mathcal B|_{\mathcal M_0}
=E^s\oplus T\mathcal M_0\oplus E^u,
\]

where \(E^s\) and \(E^u\) include every direction transverse to \(\mathcal M_0\), including transverse binding-history directions and slack-history directions.

### NH5 — Uniform normal hyperbolicity

The derivative cocycle satisfies the exact stable, tangent, unstable, conorm, and domination estimates required by the chosen Banach-semiflow theorem. In a normally attracting case with \(E^u=0\), a representative sufficient form is

\[
\|D\Phi_0^t|_{E^s}\|
\le M_s e^{-\beta t},
\]

\[
\|D\Phi_0^t|_{T\mathcal M_0}\|
\le M_c e^{\alpha t},
\]

with the theorem-specific strict domination, at least \(\beta>\alpha\) for \(C^1\) persistence.

### NH6 — Boundary and geometry

If \(\mathcal M_0\) has a boundary, it is inflowing or overflowing as required. Tubular neighborhoods, projections, and uniform derivative bounds required by the theorem exist.

## Theorem 3.1 — Conditional Banach-semiflow persistence

Under NH1–NH6 and the hypotheses of the selected persistence theorem—for example the applicable result in Bates, Lu, and Zeng, *Existence and Persistence of Invariant Manifolds for Semiflows in Banach Space*, Memoirs AMS 135 (1998), no. 645—there exists \(\varepsilon_0>0\) such that, for \(|\varepsilon|<\varepsilon_0\), the coupled semiflow has a locally invariant \(C^1\) manifold

\[
\mathcal M_\varepsilon
=
\iota_\varepsilon(\mathcal A_x),
\]

with

\[
\|\iota_\varepsilon-
\iota_0\|_{C^1}
\le C\varepsilon.
\tag{3.1}
\]

If \(E^u=0\), the local stable foliation supplied by the persistence theorem yields constants \(C_a,\beta'>0\) and a neighborhood \(V\) such that

\[
\operatorname{dist}
(\Phi_\varepsilon^t z,
\mathcal M_\varepsilon)
\le
C_a e^{-\beta't}
\operatorname{dist}
(z,\mathcal M_\varepsilon)
\tag{3.2}
\]

while the orbit remains in \(V\).

### Proof

NH2–NH6 assert exactly that \(\mathcal M_0\) is a compact normally hyperbolic invariant manifold for the unperturbed Banach-space semiflow in the sense required by the selected theorem. NH1 gives the required \(C^1\)-small perturbation of the semiflow. The Banach-semiflow persistence theorem therefore supplies a unique nearby invariant manifold, represented by a \(C^1\)-close embedding, and preserves the normal hyperbolicity estimates. This gives (3.1). In the normally attracting case, the associated stable-foliation theorem gives exponential contraction toward the perturbed manifold, yielding (3.2). \(\square\)

## Hypothesis-matching table

| Persistence requirement | A021 replacement hypothesis | Status for the concrete A021 blocks |
|---|---|---|
| Banach-space \(C^1\) semiflow | NH1 | Must be verified |
| Compact \(C^1\) invariant manifold | NH2–NH3 | Not supplied by original A021 |
| Complete normal splitting | NH4 | Not supplied |
| Normal/tangent domination | NH5 | Not supplied |
| Uniform projections/tubular geometry | NH6 | Not supplied |
| \(C^1\)-small semiflow perturbation | NH1 plus yield-gap bound | Small vector-field coupling is plausible; semiflow estimate must be proved |
| Boundary/inflow/overflow conditions | NH6 | Not supplied |

Thus Theorem 3.1 is valid as a conditional theorem but is not yet verified for the concrete A021 model family.

---

# 4. From the persistent embedding to a graph

Let

\[
q_\varepsilon
=
\pi_x\circ\iota_\varepsilon:
\mathcal A_x\to\mathcal X.
\]

At \(\varepsilon=0\), \(q_0\) is the inclusion of \(\mathcal A_x\). By (3.1), \(q_\varepsilon\) is \(C^1\)-close to that inclusion. Assume additionally that it is an embedding and a diffeomorphism onto its image

\[
\mathcal A_{x,\varepsilon}
=q_\varepsilon(\mathcal A_x).
\]

Define

\[
h_\varepsilon
=
\pi_y\circ\iota_\varepsilon
\circ q_\varepsilon^{-1}:
\mathcal A_{x,\varepsilon}	o\mathcal Y.
\]

Then

\[
\mathcal M_\varepsilon
=
\{(\phi,h_\varepsilon(\phi)):
\phi\in\mathcal A_{x,\varepsilon}\}.
\tag{4.1}
\]

Because \(\mathcal M_\varepsilon\) is invariant,

\[
\pi_y\Phi_\varepsilon^t
(\phi,h_\varepsilon(\phi))
=
h_\varepsilon
\left(
\pi_x\Phi_\varepsilon^t
(\phi,h_\varepsilon(\phi))
\right)
\]

whenever the orbit remains in the chart. The graph is over the perturbed projected base \(\mathcal A_{x,\varepsilon}\), not automatically over the old \(\mathcal A_x\).

This graph step is elementary after persistence, but the projection-diffeomorphism assumption must be proved in the concrete application.

---

# 5. Direct local Hopf persistence without an invariant graph

A021’s local Hopf transfer can be treated more directly than its invariant graph.

## Theorem 5.1 — Persistence of a simple RFDE characteristic crossing

Let \(D_\varepsilon(\lambda,	au)\) be a scalar analytic characteristic function for the full coupled linearized RFDE near an equilibrium \(z_\varepsilon^*\), with \(D_\varepsilon\) continuously differentiable in \((\varepsilon,	au)\) and locally uniform in \(\lambda\). Assume:

1. \(z_\varepsilon^*\) exists and is \(C^1\) in \(\varepsilon\);
2. at \(\varepsilon=0\),
   \[
   D_0(i\omega_*,	au_*)=0,
   \qquad \omega_*>0;
   \]
3. the root is simple:
   \[
   \partial_\lambda D_0(i\omega_*,	au_*)\ne0;
   \]
4. no other characteristic root lies on the imaginary axis near the crossing;
5. the root branch is transverse:
   \[
   \frac{d}{d	au}
   \operatorname{Re}\lambda_0(	au_*)
   \ne0;
   \]
6. all slack/normal characteristic roots remain uniformly separated from the imaginary axis.

Then there are \(C^1\) functions \(\omega(\varepsilon)\) and \(\tau(\varepsilon)\) for sufficiently small \(\varepsilon\) such that

\[
D_\varepsilon
(i\omega(\varepsilon),	au(\varepsilon))=0,
\]

and

\[
\omega(\varepsilon)
=
\omega_*+O(\varepsilon),
\qquad
\tau(\varepsilon)
=
\tau_*+O(\varepsilon).
\tag{5.1}
\]

### Proof

Define

\[
\mathcal F(\omega,\tau,\varepsilon)
=
\begin{pmatrix}
\operatorname{Re}
D_\varepsilon(i\omega,\tau)\\
\operatorname{Im}
D_\varepsilon(i\omega,\tau)
\end{pmatrix}.
\]

At \((\omega_*,\tau_*,0)\), \(\mathcal F=0\). Its columns with respect to \((\omega,	au)\) are the real-imaginary representations of

\[
iD_\lambda
\quad\text{and}\quad
D_\tau.
\]

The two columns are linearly independent exactly when

\[
\operatorname{Re}
\left(-\frac{D_\tau}{D_\lambda}
\right)
\ne0,
\]

which is the transverse-crossing condition because

\[
\lambda'(\tau)
=-\frac{D_\tau}{D_\lambda}.
\]

Therefore the real \(2\times2\) Jacobian of \(\mathcal F\) with respect to \((\omega,	au)\) is invertible. The implicit function theorem gives \(C^1\) functions \((\omega(\varepsilon),	au(\varepsilon))\) and the \(O(\varepsilon)\) estimates in (5.1). Simplicity and spectral separation persist by continuity. \(\square\)

## Nonlinear Hopf qualification

Theorem 5.1 proves persistence of the simple spectral crossing. To claim a nonlinear Hopf bifurcation of the full RFDE, additionally invoke a matching RFDE Hopf theorem and verify its smoothness, nonresonance, center-dimension, and nonlinear nondegeneracy assumptions. No invariant graph is required for the spectral result.

---

# 6. Yield parity

For the smooth minimum,

\[
\pi_j
=
\frac{w_j e^{-\rho y_j}}
{\sum_m w_m e^{-\rho y_m}}.
\]

When the binding component has a uniform gap \(y_j-y_k\ge\Delta_y>0\),

\[
\pi_j
\le
w_{min}^{-1}e^{-\rho\Delta_y}.
\]

At yield parity \(\Delta_y=0\), this estimate becomes only \(O(1)\). The coupling parameter produced by the yield-gap argument is no longer small. Therefore Theorem 2.1 no longer gives an exponentially small reduction error from the yield gap, and Theorem 3.1 cannot use the gap as its perturbation-smallness certificate.

This proves failure of the **yield-gap reduction argument**, not nonexistence of every possible invariant manifold or reduction.

---

# 7. Recommended A021 claim statuses

## Theorem

- Soft-minimum off-limiting derivative bound
- Finite-time binding-block perturbation theorem

## Conditional theorem

- Compact Banach-semiflow NHIM persistence under NH1–NH6 and a matched theorem
- Vertical graph only after projection diffeomorphism
- Simple characteristic crossing persistence under Theorem 5.1 assumptions

## Conjecture/application obligation

- The concrete A021 blocks satisfy NH1–NH6
- The concrete perturbed manifold is a global graph over the intended binding-history domain
- The concrete Hopf crossing is carried by the full coupled RFDE after all spectra are checked

## Not established

- A global graph over all histories in \(C([ -\tau,0],K_x)\)
- Normal hyperbolicity from slack stability alone
- Global periodic-fold persistence

---

# 8. Publication-ready replacement LaTeX

```latex
\subsection{Yield-gap reduction: status and phase space}
Let
\[
\mathcal X=C([ -\tau,0],\mathbb R^m),
\qquad
\mathcal Y=C([ -\tau,0],\mathbb R^n),
\]
and consider
\[
\dot x=F(x_t)+\varepsilon_c f(x_t,y_t),
\qquad
\dot y=G(y_t)+\varepsilon_c g(x_t,y_t),
\]
with
\[
\varepsilon_c
=C e^{-\rho\Delta_y}+\varepsilon_{\rm phys}.
\]
A compact finite-dimensional state set does not make
$C([ -\tau,0],K)$ compact. The invariant-graph result below therefore
requires a genuine compact invariant history manifold and a complete
normal-hyperbolicity hypothesis.

\begin{theorem}[Finite-time binding-block perturbation]
Suppose the coupled and uncoupled binding solutions share their initial
history and remain on $[0,T]$ in a region where $F$ is Lipschitz with
constant $L$ and $\|f\|\le M$. Then
\[
\sup_{0\le t\le T}
\|x_t^{\varepsilon_c}-x_t^0\|_\infty
\le
\frac{\varepsilon_c M}{L}(e^{LT}-1)
\]
for $L>0$, with the bound $\varepsilon_c MT$ when $L=0$.
\end{theorem}

\begin{proof}
Let
$E(t)=\sup_{-\tau\le s\le t}|x^{\varepsilon_c}(s)-x^0(s)|$.
Then
\[
E(t)\le L\int_0^tE(s)\,ds+\varepsilon_c Mt,
\]
and Gronwall's inequality gives the result.
\end{proof}

\begin{conditionaltheorem}[Compact normally attracting RFDE manifold]
Assume the uncoupled binding semiflow possesses a compact $C^1$
invariant manifold $\mathcal A_x$; the product
$\mathcal M_0=\mathcal A_x\times\{\widehat y_*\}$ has a complete
invariant splitting containing every transverse binding and slack
history direction; normal contraction uniformly dominates tangent
growth; the RFDE generates a $C^1$ semiflow; and the coupled semiflow is
$C^1$-$O(\varepsilon_c)$ close on a neighborhood of $\mathcal M_0$.
Assume all remaining compactness, boundary, and tubular-neighborhood
hypotheses of the selected Banach-semiflow persistence theorem.
Then a locally invariant $C^1$ manifold
$\mathcal M_{\varepsilon_c}$ exists with
\[
\operatorname{dist}_{C^1}
(\mathcal M_{\varepsilon_c},\mathcal M_0)
=O(\varepsilon_c).
\]
If the $x$-projection is a diffeomorphism onto
$\mathcal A_{x,\varepsilon_c}$, then
\[
\mathcal M_{\varepsilon_c}
=
\{(\phi,h_{\varepsilon_c}(\phi)):
\phi\in\mathcal A_{x,\varepsilon_c}\}.
\]
\end{conditionaltheorem}

\begin{remark}[Unverified application hypotheses]
The preceding theorem is not established for the concrete A021 blocks
until the compact invariant binding manifold, full normal bundle,
tangent growth, normal spectral bounds, domination ratio, semiflow
regularity, and projection transversality are verified.
\end{remark}

\begin{conditionaltheorem}[Persistence of a simple characteristic crossing]
Let $D_{\varepsilon_c}(\lambda,\tau)$ be the characteristic function of
the full coupled RFDE at a smoothly varying equilibrium. If at
$\varepsilon_c=0$ there is a simple pair $\pm i\omega_*$, no other
imaginary spectrum, a transverse delay crossing, and a uniform spectral
gap to every slack/normal root, then
\[
\omega(\varepsilon_c)=\omega_*+O(\varepsilon_c),
\qquad
\tau(\varepsilon_c)=\tau_*+O(\varepsilon_c).
\]
\end{conditionaltheorem}

\begin{remark}[Yield parity]
At $\Delta_y=0$ the off-limiting softmax weights are $O(1)$, so the
exponentially small yield-gap parameter disappears. This invalidates the
yield-gap reduction argument but does not exclude another reduction.
\end{remark}
```

---

# 9. Concrete verification checklist for A021

Before promoting the conditional invariant-manifold theorem, verify:

1. exact RFDE phase space and open domain;
2. \(C^1\) or stronger semiflow regularity;
3. compact invariant binding manifold—not merely a bounded absorbing set;
4. tangent cocycle bound \(\alpha\);
5. every stable and unstable normal spectral bound;
6. full normal bundle, including transverse binding directions;
7. domination inequality;
8. boundary inflow/overflow conditions;
9. uniform tubular projection;
10. \(C^1\) perturbation norm bounded by \(C\varepsilon_c\);
11. vertical-projection transversality;
12. yield-gap lower bound on the whole neighborhood;
13. equilibrium continuation;
14. complete characteristic spectrum and simple crossing;
15. separation of local Hopf persistence from global-fold persistence.

## Final internal judgment

A correct invariant-graph theorem is possible under strong compact-NHIM hypotheses, but the original A021 source did not verify them. The finite-time theorem is fully proved now. Local spectral/Hopf crossing persistence can be proved directly under explicit characteristic assumptions and does not need the graph. The concrete invariant graph should remain conditional until the checklist is discharged.
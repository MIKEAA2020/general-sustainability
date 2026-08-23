# Self-Contained Generic Two-Block Periodic Persistence Theorem

## Status

This theorem and proof close the abstract graph-transform/persistence step without citing BLZ. They do not verify the continuum numerical hypotheses or identify the original A021 coupling. Application to the C4 scaffold remains conditional on CAP and perturbation bounds.

## Theorem

Let `B=X x Y` be a Banach space and `Phi_epsilon^t` a family of local semiflows. Let

\[
M_0=\{(\gamma_\theta,\widehat y_*):\theta\in S^1\}
\]

be a compact `C2` embedded circle invariant under `Phi_0`. Assume:

### H1 — Positive-time regularity and localization

There exist `T>0`, a neighborhood `U` of `M0`, and `epsilon_0>0` such that every `Phi_epsilon^t`, `0<=t<=T`, is defined on `U`; `P_epsilon=Phi_epsilon^T` is `C2`; and

\[
\|P_\varepsilon-P_0\|_{C^1(U)}\le\delta_\varepsilon,
\qquad \delta_\varepsilon\to0.
\]

### H2 — Split tubular coordinates

There is a `C1` stable bundle `E^s -> M0`, a uniformly complemented splitting

\[
TB|_{M_0}=TM_0\oplus E^s,
\]

and a `C1` tubular chart

\[
\Psi:\{(m,v):m\in M_0,\ \|v\|<\rho\}\to U.
\]

### H3 — Invariant linear splitting and bunching

In tube coordinates write

\[
\widetilde P_\varepsilon(m,v)
=(\chi_\varepsilon(m,v),Q_\varepsilon(m,v)).
\]

At `epsilon=0,v=0`,

\[
Q_0(m,0)=0,
\qquad D_mQ_0(m,0)=0,
\qquad D_v\chi_0(m,0)=0.
\]

The base map `f=P_0|M0` is a `C2` diffeomorphism, and

\[
a:=\sup_m\|D_vQ_0(m,0)\|,
\qquad
b:=\sup_m\|(Df(m))^{-1}\|
\]

satisfy

\[
ab<1.
\]

### H4 — Intermediate-time tangent continuity

For every `C1` embedding `iota:S1->U` sufficiently close to the inclusion of `M0`,

\[
s\mapsto\Phi_\varepsilon^s\circ\iota
\]

is continuous at `s=0` in `C1(S1,B)`.

Then, for sufficiently small `delta_epsilon`, there is a unique small `C1` section

\[
\sigma_\varepsilon:M_0\to E^s
\]

whose graph

\[
M_\varepsilon
=\Psi\{(m,\sigma_\varepsilon(m)):m\in M_0\}
\]

has the following properties:

1. `M_epsilon` is a compact `C1` embedded circle;
2. `Phi_epsilon^t(M_epsilon)=M_epsilon` for every `t>=0` for which the localized semiflow is defined;
3. `||sigma_epsilon||_{C1}<=C delta_epsilon`;
4. there is a tube and `theta in (0,1)` such that
   \[
   \operatorname{dist}(P_\varepsilon^n z,M_\varepsilon)
   \le C\theta^n\operatorname{dist}(z,M_\varepsilon)
   \]
   while the iterates remain in the tube;
5. if the binding projection restricted to the unperturbed circle is an embedding and the perturbed embedding is sufficiently `C1` close, then `M_epsilon` is a vertical graph over its perturbed projected binding curve.

## Proof

### 1. Section space

Choose constants `r>0` and `ell>0`. Let

\[
\Sigma(r,\ell)
=\{\sigma:M_0\to E^s:\|\sigma\|_\infty\le r,
\operatorname{Lip}\sigma\le\ell\}.
\]

Use a finite bundle atlas and ambient differences with the stable projections to define the Lipschitz norm. This set is closed in the supremum metric and therefore complete.

### 2. Base map of a section

For `sigma in Sigma`, define

\[
\chi_\sigma(m)
=\chi_\varepsilon(m,\sigma(m)).
\]

By H3 and continuity, for every `eta>0`, after reducing `r` and `delta_epsilon`,

\[
\operatorname{Lip}(\chi_\sigma-f)
\le C(r+\delta_\varepsilon),
\]

and

\[
\operatorname{Lip}(\chi_\sigma^{-1})
\le b+\eta.
\]

Locally this follows from the inverse function theorem and the conorm of `Df`. Globally, `chi_sigma` is a local diffeomorphism of the compact circle and is homotopic to `f`; it has the same degree, one, and is therefore a global diffeomorphism.

### 3. Graph transform

Define

\[
(\Gamma_\varepsilon\sigma)\circ\chi_\sigma
=Q_\varepsilon(\cdot,\sigma(\cdot)).
\]

Near the zero section,

\[
\|D_vQ_\varepsilon\|\le a+\eta,
\qquad
\|D_mQ_\varepsilon\|\le C(r+\delta_\varepsilon).
\]

Hence

\[
\|\Gamma_\varepsilon\sigma\|_\infty
\le(a+\eta)r+C\delta_\varepsilon+Cr^2.
\]

Choose `r=K delta_epsilon` with `K` sufficiently large, then reduce `delta_epsilon`; the right side is at most `r`.

For slopes,

\[
\operatorname{Lip}(\Gamma_\varepsilon\sigma)
\le(b+\eta)
\{(a+\eta)\operatorname{Lip}\sigma+C(r+\delta_\varepsilon)\}.
\]

Because `ab<1`, choose `eta`, then `ell,r,delta_epsilon`, so the right side is at most `ell`.

### 4. Supremum contraction

For `sigma_1,sigma_2`, compare the two outputs at a common base point and split the difference into:

1. a normal-fiber difference at the same preimage;
2. the change caused by the two inverse base maps.

The first is bounded by `(a+eta)||sigma_1-sigma_2||`. The inverse-base difference is bounded by `(b+eta)` times `D_v chi`, which vanishes on the unperturbed zero section and is `O(r+delta_epsilon)`. Thus

\[
\|\Gamma_\varepsilon\sigma_1-
\Gamma_\varepsilon\sigma_2\|_\infty
\le
\{a+C(r+\delta_\varepsilon)\}
\|\sigma_1-
\sigma_2\|_\infty.
\]

If a chart convention places the inverse tangent in the leading term, the bound is `ab+C(r+delta_epsilon)`. In either convention H3 permits a contraction factor below one after shrinking. Banach's fixed-point theorem supplies a unique Lipschitz fixed section `sigma_epsilon`, with `||sigma_epsilon||=O(delta_epsilon)`.

### 5. C1 regularity

For a `C1` section with `L=D sigma`, differentiation gives

\[
D(\Gamma_\varepsilon\sigma)(\chi_\sigma(m))
=
(D_mQ+D_vQ\,L)
(D_m\chi+D_v\chi\,L)^{-1}.
\]

At the zero section, `D_mQ=0`; this is the inhomogeneous term of size `O(delta_epsilon+r)`. The derivative with respect to `L` has leading norm at most `ab`. The fiber-contraction theorem therefore gives a continuous fixed derivative and

\[
\|D\sigma_\varepsilon\|\le C\delta_\varepsilon.
\]

Thus the fixed graph is `C1`.

### 6. Time-T invariance

The fixed-point identity is exactly

\[
P_\varepsilon(M_\varepsilon)=M_\varepsilon.
\]

The restricted map is conjugate through the graph to `chi_sigma`, hence is a diffeomorphism of the circle; no ambient inverse is used.

### 7. Semiflow invariance

For small `s>=0`, commutation gives

\[
P_\varepsilon(\Phi_\varepsilon^sM_\varepsilon)
=\Phi_\varepsilon^sM_\varepsilon.
\]

By H4, `Phi_epsilon^s` composed with the graph embedding is `C1` close to that embedding. Compact-embedding stability and the tube projection show that the image is another section in `Sigma(r,ell)`. By uniqueness of the graph-transform fixed point,

\[
\Phi_\varepsilon^sM_\varepsilon=M_\varepsilon
\]

for all sufficiently small `s`. The semigroup property extends this equality to all forward times in the localized domain.

### 8. Attraction

In tube coordinates, subtract the invariant section from a nearby normal coordinate. The mean-value theorem and the normal derivative bound give

\[
\|v_{n+1}-\sigma(m_{n+1})\|
\le\theta\|v_n-
\sigma(m_n)\|,
\]

with `theta<1` after the same shrinkings. Equivalence of tube and ambient distance gives the discrete estimate. Finite-time Lipschitz bounds interpolate between multiples of `T`. This proves local in-tube attraction, not a global basin.

### 9. Vertical representation

Write the persistent embedding as

\[
\iota_\varepsilon(m)
=(q_\varepsilon(m),r_\varepsilon(m)).
\]

The map `q_0` is the binding-history embedding of the compact circle. A sufficiently small `C1` perturbation of a compact embedding remains an embedding: use local conorm for near pairs and compact separation for far pairs. Therefore `q_epsilon` is a diffeomorphism onto its image, and

\[
h_\varepsilon
=r_\varepsilon\circ q_\varepsilon^{-1}
\]

gives the vertical representation over the perturbed projected closed curve.

This completes the proof. `square`

## Quantitative application target

For the C4 two-block scaffold, take

\[
T=40P.
\]

Validation must provide continuum constants satisfying, with chart/error margin,

\[
ab\le q_{40}^{\rm cont}<\frac14.
\]

The current finite-discrete estimate is approximately `0.1164`. This number is evidence for H3, not H3 itself.

## What remains outside this theorem

1. validated continuum orbit/Floquet/projections and product bunching;
2. a concrete perturbation class. For a generic theorem, declare `||R_epsilon||C1<=C|epsilon|`; for original A021, supply source-derived `G,f,g`;
3. a localized long-time tube on `[0,T]`;
4. optional stable foliation/asymptotic phase, which requires extra proof or a matched theorem.

## Publication status

The proof is complete as an abstract quantitative graph-transform theorem. Its application to the C4/A021 scaffold remains conditional until the numerical and coupling hypotheses are certified.
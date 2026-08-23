# Specialist Proof Prompt — A021 RFDE Yield-Gap Invariant Graph, Version 2

## Role

Act as a specialist in:

- retarded functional differential equations (RFDEs);
- differentiable semiflows on Banach spaces;
- exponential dichotomies;
- normally hyperbolic invariant manifolds for maps/semiflows;
- graph-transform and Lyapunov–Perron methods;
- local Hopf bifurcation for RFDEs.

Your job is not to preserve the original theorem’s strength. Your job is to determine the strongest statement that is actually provable and to provide publication-ready replacement text.

Do not appeal generically to “Fenichel theory,” “standard invariant-manifold theory,” or “Hale–Lin.” State an exact theorem and match every hypothesis, or give a self-contained proof.

---

# 1. A021 model and notation

Fix \(\tau>0\). Let

\[
\mathcal X=C([ -\tau,0],\mathbb R^m),
\qquad
\mathcal Y=C([ -\tau,0],\mathbb R^n),
\qquad
\mathcal B=\mathcal X\times\mathcal Y,
\]

initially with the supremum norm. If another phase space is needed, define it and explain why it is appropriate for the RFDE and the persistence theorem.

For trajectories \(x\) and \(y\), use

\[
x_t(\theta)=x(t+\theta),
\qquad
y_t(\theta)=y(t+\theta),
\qquad \theta\in[-\tau,0].
\]

Consider

\[
\dot x(t)=F(x_t)+\varepsilon f(x_t,y_t),
\]

\[
\dot y(t)=G(y_t)+\varepsilon g(x_t,y_t),
\tag{1}
\]

where

\[
F:\mathcal X\to\mathbb R^m,
\qquad
G:\mathcal Y\to\mathbb R^n,
\]

and

\[
f:\mathcal B\to\mathbb R^m,
\qquad
g:\mathcal B\to\mathbb R^n.
\]

The parameter is

\[
\varepsilon
=C_{gap}e^{-\rho\Delta_y}
+\varepsilon_{phys},
\tag{2}
\]

where \(\rho>0\), \(\Delta_y>0\), and \(\varepsilon_{phys}\ge0\).

This scaling comes from a smooth vector Liebig service. If component \(k\) is uniformly binding,

\[
\widetilde Y_k
\le
\widetilde Y_j-\Delta_y S^{max}
\qquad(j\ne k),
\]

then the off-limiting soft-minimum weights satisfy

\[
\pi_j
\le
w_{min}^{-1}e^{-\rho\Delta_y}.
\tag{3}
\]

You may accept (3) as proved. It establishes small coupling; it does not establish an invariant manifold.

At \(\varepsilon=0\),

\[
\dot x(t)=F(x_t),
\qquad
\dot y(t)=G(y_t).
\tag{4}
\]

Assume \(G\) has an equilibrium \(y_*\in\mathbb R^n\), with constant history \(\widehat y_*\in\mathcal Y\).

In A021, \(x\) is the binding resource block and \(y\) collects slack blocks. Each block may contain states such as \((N,A,Z,E)\), but this prompt deliberately asks for an abstract conditional theorem. Do not claim that any concrete block satisfies your assumptions unless the necessary equations and spectra are explicitly checked.

---

# 2. First task: determine whether the original claim is even well posed

The original claim tried to use

\[
\mathcal M_0
=
\{(\phi,\widehat y_*):
\phi\in C([ -\tau,0],K_x)\}
\]

as an unperturbed normally hyperbolic manifold and concluded that it persists as

\[
y_t=h_\varepsilon(x_t).
\]

Before proving anything, address all of the following.

## 2.1 The base is not automatically compact

A compact finite-dimensional set \(K_x\subset\mathbb R^m\) does not make

\[
C([ -\tau,0],K_x)
\]

compact in the supremum norm.

## 2.2 The base is not automatically a manifold

An absorbing set or compact invariant set need not be a \(C^r\) Banach submanifold. A normally hyperbolic invariant-manifold theorem cannot be applied merely because the set is invariant and bounded.

## 2.3 The full normal bundle is not only the slack variable

If \(\mathcal A_x\subset\mathcal X\) is a proper invariant manifold, directions in \(\mathcal X\) transverse to \(\mathcal A_x\) also belong to the normal bundle of

\[
\mathcal A_x\times\{\widehat y_*\}.
\]

You must account for them. You may treat \(\mathcal Y\) alone as the normal direction only if the base is an open Banach manifold in \(\mathcal X\), a graph setting provides an equivalent splitting, or another exact theorem permits it.

## 2.4 RFDE solution maps are generally semiflows, not invertible flows

A graph over present histories may fail to be single valued if the base has multiple backward continuations. If your theorem needs a two-sided flow, unique backward extension, or complete base trajectories, state and prove/assume that property. Otherwise use a one-sided inflowing/overflowing or pullback formulation that genuinely applies.

## 2.5 Generic persistence need not preserve a vertical graph over the old base

A perturbed invariant manifold may be parameterized as

\[
\iota_\varepsilon(\phi)
=
\bigl(
\phi+u_\varepsilon(\phi),
\widehat y_*+v_\varepsilon(\phi)
\bigr),
\tag{5}
\]

rather than \((\phi,h_\varepsilon(\phi))\) with the old \(x\)-coordinate unchanged. A vertical graph is legitimate only after proving that the \(x\)-projection restricted to the perturbed manifold is a local/global diffeomorphism.

Your first output must explicitly say which of these issues defeats the original proof.

---

# 3. Choose one rigorous theorem route

Do not mix the conclusions of the following routes.

## Route A — Compact normally attracting invariant manifold

Assume or construct a compact \(C^r\) invariant manifold

\[
\mathcal A_x\subset\mathcal X
\]

for the uncoupled binding semiflow. Define

\[
\mathcal M_0
=
\mathcal A_x\times\{\widehat y_*\}
\subset\mathcal B.
\]

You must provide an invariant splitting

\[
T\mathcal B|_{\mathcal M_0}
=
T\mathcal M_0
\oplus E^s
\quad
\text{or the full }E^s\oplus T\mathcal M_0\oplus E^u
\text{ splitting required by your theorem}.
\]

State uniform estimates. For example,

\[
\|D\Phi_0^t|_{E^s}\|
\le M_s e^{-\beta t},
\]

\[
\|D\Phi_0^t|_{T\mathcal M_0}\|
\le M_c e^{\alpha t}.
\]

If tangent inversion/conorm estimates are required, state them. For a \(C^r\) persistent graph, give the exact domination inequality required by the theorem, such as

\[
\beta>r\alpha,
\]

only if that is genuinely the theorem’s condition.

A stable slack equilibrium alone is not sufficient: normal contraction must dominate tangent growth, and all other normal directions must be included.

## Route B — Normally attracting manifold for a time-\(T\) map

For some \(T>\tau\), use the RFDE time-\(T\) solution map

\[
P_\varepsilon=\Phi_\varepsilon^T.
\]

Prove:

1. \(P_\varepsilon\) is \(C^r\) on an open neighborhood of \(\mathcal M_0\);
2. \(P_\varepsilon\) is \(C^1\)-close to \(P_0\) with a bound \(O(\varepsilon)\);
3. \(\mathcal M_0\) is a compact normally attracting invariant manifold for \(P_0\);
4. the exact persistence theorem for Banach-space maps applies;
5. persistence for the map implies the desired semiflow invariance.

This route is often cleaner for RFDEs, but every step must be proved.

## Route C — Lyapunov–Perron or graph transform over a complete base flow

If the base dynamics restricted to \(\mathcal A_x\) is a two-sided flow or has unique complete trajectories, define an explicit Lyapunov–Perron or graph-transform operator.

You must:

1. define the function space of graphs;
2. define the operator;
3. prove it maps the graph space into itself;
4. prove contraction using an explicit domination/smallness inequality;
5. prove invariance;
6. prove attraction;
7. prove \(C^1\) regularity only if the derivative transform is also contractive.

## Route D — Compact equicontinuous set and Lipschitz graph only

You may use

\[
\mathcal K_{M,L}
=
\{
\phi\in\mathcal X:
\|\phi\|_\infty\le M,
\operatorname{Lip}(\phi)\le L
\},
\]

which is compact by Arzelà–Ascoli. You must prove positive invariance.

This route does not automatically provide a \(C^1\) manifold. If the available theorem yields only a continuous or Lipschitz invariant graph, state only that result.

## Route E — Noncompact bounded geometry

If the base is noncompact, state an exact noncompact NHIM theorem and verify:

- bounded geometry of the manifold and ambient space;
- uniform tubular neighborhoods/projections;
- uniform bounds on derivatives;
- uniform exponential splitting;
- normal/tangent domination;
- perturbation smallness in the required uniform norm.

Do not say “bounded geometry” without constructing the objects and bounds.

## Route F — No invariant graph; finite-time perturbation only

If no persistence theorem can be matched, prove only:

\[
\|x^\varepsilon-x^0\|_{C([0,T])}
\le C_T\varepsilon
\tag{6}
\]

for finite \(T\), assuming both solutions remain in a common compact region and the perturbation is bounded/Lipschitz. State the invariant graph as a conjecture with explicit missing hypotheses.

This is an acceptable and scientifically preferable outcome.

---

# 4. Mandatory history-space and well-posedness audit

State explicitly:

- open domains of \(F,G,f,g\);
- \(C^r\) class;
- local existence, uniqueness, and continuation assumptions;
- whether the solution semiflow is differentiable at \(t=0\) or only for \(t>0\);
- phase-space norm;
- compatibility conditions if a \(C^1\)-solution manifold is used;
- eventual compactness, smoothing, or equicontinuity used to obtain compact invariant sets;
- whether delays are fixed, state dependent, or mode dependent;
- whether the manifold has a boundary and, if so, whether it is invariant, inflowing, or overflowing.

Do not infer compactness from boundedness.

---

# 5. Mandatory theorem citation and hypothesis mapping

Candidate Banach-semiflow references include:

- P. W. Bates, K. Lu, and C. Zeng, *Existence and Persistence of Invariant Manifolds for Semiflows in Banach Space*, Memoirs of the AMS **135** (1998), no. 645, DOI `10.1090/memo/0645`;
- P. W. Bates, K. Lu, and C. Zeng, *Persistence of Overflowing Manifolds for Semiflow*, *Communications on Pure and Applied Mathematics* **52** (1999), 983–1046;
- P. W. Bates, K. Lu, and C. Zeng, *Invariant Foliations Near Normally Hyperbolic Invariant Manifolds for Semiflows*, *Transactions of the AMS* **352** (2000), 4641–4676.

These are candidates, not automatic matches. Retrieve the exact theorem statement used and verify that its manifold, splitting, smoothness, compactness/noncompactness, semiflow, and perturbation hypotheses fit system (1).

State the exact persistence theorem used:

- full bibliographic reference;
- theorem number or exact named result where possible;
- whether it concerns flows, semiflows, or maps;
- finite- or infinite-dimensional setting;
- compact or bounded-geometry manifold;
- required smoothness;
- required exponential splitting and domination;
- perturbation topology/norm;
- conclusion and regularity.

Then provide this table:

| External theorem hypothesis | A021 object/assumption | Verification or unresolved obligation |
|---|---|---|

A finite-dimensional Fenichel citation alone is not acceptable for an RFDE semiflow.

---

# 6. Correct graph formulation

Prefer a parameterized embedding

\[
\iota_\varepsilon:
\mathcal A_x\to\mathcal B,
\qquad
\mathcal M_\varepsilon
=
\iota_\varepsilon(\mathcal A_x),
\tag{7}
\]

with

\[
\|\iota_\varepsilon-\iota_0\|_{C^1}
\le C\varepsilon,
\]

provided by the selected persistence theorem.

If the \(x\)-projection is proved to be a diffeomorphism onto

\[
\mathcal A_{x,\varepsilon}
=
\pi_x\mathcal M_\varepsilon,
\]

then define the vertical graph

\[
h_\varepsilon:
\mathcal A_{x,\varepsilon}
\to\mathcal Y,
\qquad
\mathcal M_\varepsilon
=
\{(\phi,h_\varepsilon(\phi)):
\phi\in\mathcal A_{x,\varepsilon}\}.
\tag{8}
\]


The invariance identity is

\[
\pi_y\Phi_\varepsilon^t
(\phi,h_\varepsilon(\phi))
=
h_\varepsilon
\left(
\pi_x\Phi_\varepsilon^t
(\phi,h_\varepsilon(\phi))
\right),
\tag{9}
\]

with the projected history required to remain in \(\mathcal A_{x,\varepsilon}\).

Do not use \(h(x_\tau)\) when \(h\) maps histories. Use \(h(x_t)\).

State whether the graph is local, global, positively invariant, inflowing, or overflowing.

---

# 7. Required estimates

Prove the estimates supported by your theorem, for example

\[
\|h_\varepsilon-\widehat y_*\|_{C^0}
\le C\varepsilon,
\]

and only if justified,

\[
\|Dh_\varepsilon\|
\le C\varepsilon.
\]

For attraction, state the exact neighborhood and prove

\[
\operatorname{dist}
\left(
\Phi_\varepsilon^t z,
\mathcal M_\varepsilon
\right)
\le
C e^{-\beta' t}
\operatorname{dist}
(z,\mathcal M_\varepsilon),
\tag{10}
\]

for the time range supported by the theorem.

If initial data are already \(O(\varepsilon)\)-close, do not automatically claim an additional \(O(|\log\varepsilon|)\) transient. A logarithmic transient is relevant when contracting an \(O(1)\) initial distance down to \(O(\varepsilon)\).


---

# 8. Hopf persistence: keep it separate

Do not use an invariant-graph claim as a shortcut unless it has already been proved.

There are two possible outputs.

## 8.1 Direct full-RFDE Hopf persistence

If the full coupled characteristic operator is a \(C^1\) perturbation of the uncoupled operator, prove directly that a simple pair \(\pm i\omega_*\) persists. Require:

- existence and smooth dependence of the equilibrium;
- a simple imaginary pair;
- no other imaginary spectrum;
- transverse parameter crossing;
- separation from slack/normal spectrum;
- a valid characteristic-operator perturbation theorem.

## 8.2 Hopf on a proved invariant graph

Only after proving the graph, show that all center spectrum lies tangent to it and the normal spectrum remains uniformly stable. Then state whether the Hopf of the reduced graph dynamics is also a Hopf of the full RFDE.

The desired result is

\[
\tau_*(\varepsilon)
=
\tau_*+O(\varepsilon).
\tag{11}
\]


Do not claim persistence of global periodic folds from a local Hopf argument.

---

# 9. Yield-parity limitation

Explain precisely:

\[
\Delta_y=0
\quad\Longrightarrow\quad
\pi_j=O(1)
\]

for competing components, so the exponential small parameter in (2) disappears. Conclude only that the yield-gap reduction fails. Do not claim that no other reduction or invariant manifold can exist.

---

# 10. Required outputs

Return all of the following in order.

## Output A — Original-claim diagnosis

Identify exactly which original assumptions are insufficient. Include a counterexample or a precise mechanism for failure of at least:

- tangent/normal domination;
- compactness/manifold structure;
- backward uniqueness or graph single-valuedness;
- vertical graph over the unperturbed base.

## Output B — Strongest valid theorem

State the strongest theorem actually proved under a minimal explicit hypothesis set. Separate:

1. \(C^1\) NHIM persistence;
2. Lipschitz invariant graph;
3. finite-time perturbation;
4. conjecture.

## Output C — Complete proof

Give a line-by-line proof. If using graph transform or Lyapunov–Perron, define the operator and prove every mapping, contraction, invariance, attraction, and regularity property.

## Output D — Hypothesis-matching table

Provide the external-theorem mapping table required in §5.

## Output E — Hopf result

Give either a proved direct full-RFDE result, a proved graph-based corollary, or an explicit conjecture. Do not blur them.

## Output F — Yield-parity result

State the exact limitation from §9.

## Output G — Publication-ready LaTeX

Provide replacement LaTeX for A021’s:

- phase-space/hypothesis block;
- invariant-graph theorem or conjecture;
- proof or missing-proof paragraph;
- finite-time perturbation theorem;
- Hopf theorem/corollary or conjecture;
- yield-parity limitation;
- status paragraph.

## Output H — Verification checklist

End with a checklist of concrete quantities that must be verified for the actual A021 blocks:

- compact invariant binding object;
- tangent growth bound;
- every normal spectral bound;
- domination ratio;
- perturbation \(C^1\) norm;
- projection transversality;
- equilibrium and characteristic spectra;
- yield-gap lower bound;
- neighborhood and continuation bounds.

---

# 11. Non-negotiable safeguards

- Bounded does not imply compact in an infinite-dimensional history space.
- A stable slack equilibrium does not imply normal hyperbolicity.
- Normal directions include every direction transverse to the base, not only \(y\).
- RFDE semiflows are not automatically invertible.
- Generic persistence does not automatically produce a vertical graph over the old base.
- Finite-dimensional Fenichel theory is not automatically an RFDE persistence theorem.
- Do not write \(h(x_\tau)\) for a history map.
- Do not infer a global graph from a local theorem.
- Do not infer all-time tracking from a finite-time estimate.
- Do not infer global-fold persistence from local Hopf persistence.
- Do not hide a missing theorem behind “standard arguments.”
- If the strong proof fails, return a corrected conjecture and the strongest rigorous finite-time theorem.

The preferred answer is the weakest correct theorem with a complete proof, not the strongest plausible theorem.
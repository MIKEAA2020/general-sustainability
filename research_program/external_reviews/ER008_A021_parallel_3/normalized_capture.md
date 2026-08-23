# Parallel A021 Proof Response 3 — Publication-Ready Replacement Analysis

Below is the publication-ready replacement analysis and text for A021.  
Every accidental “DEL” in (5)–(11) has been removed; all history arguments are written as $x_t,y_t\in X,Y$ (not as pointwise $x(\tau)$); and the vertical-graph notation uses $h_\varepsilon(x_t)$ with $x_t\in\mathcal A_{x,\varepsilon}$.

---

# Output A — Original-claim diagnosis

The original argument attempts to treat  
$\mathcal M_0=\{(\phi,\hat y_*):\phi\in C([-τ,0],K_x)\}$  
as a compact, $C^r$-smooth, normally hyperbolic invariant manifold for the uncoupled semiflow $\Phi_0^t$ and then asserts that $\varepsilon>0$ produces a vertical graph $y_t=h_\varepsilon(x_t)$. This collapses for five independent reasons.

| Issue | Precise failure mechanism |
|---|---|
| **2.1 Non-compactness** | $C([-τ,0],K_x)$ is bounded but **not** precompact in $\|\cdot\|_\infty$; Arzelà–Ascoli requires equicontinuity, which is not inherited from $K_x\subset\mathbb R^m$. Hence $\mathcal M_0$ is not compact. |
| **2.2 Not a manifold** | An invariant absorbing set need not be a $C^r$ Banach submanifold of $X$. Without a local chart $\iota:\mathbb R^d\supset U\to X$ with $\iota(U)\subset C([-τ,0],K_x)$, “tangent space $T\mathcal M_0$” is undefined and Fenichel-type theorems do not apply. |
| **2.3 Normal bundle misidentified** | Even if $\mathcal A_x\subset X$ were a manifold, $T_{(\phi,\hat y_*)}\mathcal M_0 = T_\phi\mathcal A_x \oplus \{0\}$. The normal space is $(X/T_\phi\mathcal A_x)\oplus Y$. Restricting attention to $Y$ alone ignores all transverse directions in $X\setminus T\mathcal A_x$. Normal hyperbolicity requires uniform contraction in **all** of these directions. |
| **2.4 Non-invertible semiflow** | RFDEs generate a **one-sided** $C^0$-semiflow $\Phi^t$, $t\ge 0$. Backward continuation is not unique (and usually does not exist). Consequently a graph $\{(\phi,h_\varepsilon(\phi))\}$ can be multi-valued: two different prehistories $\phi^{(1)},\phi^{(2)}$ may flow to the same $(x_t,y_t)$. A globally single-valued vertical graph requires either unique backward extension or an explicit inflowing/overflowing formulation, neither of which is present. |
| **2.5 Vertical graph not generic** | Persistence theorems produce parameterized manifolds $\iota_\varepsilon(\phi)=(\phi+u_\varepsilon(\phi),\hat y_*+v_\varepsilon(\phi))$. The projection $\pi_x|_{\mathcal M_\varepsilon}$ need **not** be a diffeomorphism. A vertical representation $y_t=h_\varepsilon(x_t)$ is legitimate only after proving transversality $\pi_x|_{\mathcal M_\varepsilon}$ is invertible with $C^1$ inverse. The original proof assumes this without verification. |

**Conclusion of A:** The original proof lacks a manifold base, misidentifies the normal bundle, ignores non-invertibility, and assumes an unjustified vertical parameterization. No invariant-graph or Hopf-shift result follows.

---

# Output B — Strongest valid theorem (separation of provability)

We separate four levels **without mixing conclusions**.

## B1. Conditional $C^1$ NHIM persistence (Route A — **not verified**)

This is the strongest statement that *would* apply if the missing structure existed.

[The response states a conditional theorem with hypotheses H1–H8: a compact $C^2$ finite-dimensional invariant manifold $\mathcal A_x$, splitting $T\mathcal B|_{\mathcal M_0}=T\mathcal M_0\oplus E^s$, forward rate bounds with $\beta>r\alpha$, all transverse $X$ and $Y$ directions stable, $C^1$ semiflow and $O(\varepsilon)$ derivative closeness, bounded perturbation, small coupling, projection transversality, and interior domain. It concludes a nearby $C^1$ manifold, vertical graph, and attraction. It expressly says these hypotheses are not established for A021.]

## B2. Lipschitz invariant graph (Route D — **not available**)

If $\mathcal A_x$ were replaced by a compact convex invariant set $\mathcal K_M=\{\phi\in X:\|\phi\|_\infty\le M,\operatorname{Lip}\phi\le L\}$ (Arzelà–Ascoli compact), a graph-transform argument yields only a **Lipschitz** invariant graph $h_\varepsilon$ with $\|h_\varepsilon-\hat y_*\|_\infty\le C|\varepsilon|$. Even this requires (i) positive invariance of $\mathcal K_M\times\{\hat y_*\}$ and (ii) uniform contraction in $Y$. Neither is verified for A021.

## B3. Unconditional finite-time perturbation (Route F — **proved**)

This is the **only fully rigorous result** that does not depend on an unproven manifold structure.

The response states a finite-time theorem under local Lipschitz and bounded perturbation assumptions, identical initial data, a common bounded enclosure, and yields
\[
\|x_\varepsilon(t)-x_0(t)\|+\|y_\varepsilon(t)-y_0(t)\|\le C|\varepsilon|e^{Lt}.
\]
If the slack equilibrium is locally exponentially stable, it additionally claims
\[
\|y_\varepsilon(t)-\hat y_*\|\le C|\varepsilon|e^{Lt}+C'\delta e^{-\gamma t}.
\]

## B4. Conjecture for A021

If all compact-manifold, full-normal-bundle, domination, and projection assumptions are verified for the concrete blocks, the vertical graph is conjectured to follow.

---

# Output C — Complete proof (Route F only)

The response gives an integral-equation/Gronwall proof for finite-time tracking. It then attempts to add the exponentially decaying initial slack term from local exponential stability.

---

# Output D — Hypothesis-matching table

The response supplies a table marking the Banach phase space structural, local existence assumed, compact invariant manifold unresolved, full normal splitting unresolved, spectral domination unresolved, vertical projection unresolved, and yield-gap smallness conditional.

It cites Hale–Verduyn Lunel and proposes Banach-space NHIM references, while rejecting a pure finite-dimensional Fenichel citation.

---

# Output E — Hopf result

The response introduces a bifurcation parameter $\mu$ distinct from coupling $\varepsilon$. It states a structural characteristic-root persistence theorem using a simple root, transversality in $\mu$, spectral separation, and a holomorphic perturbation, yielding
\[
\mu_*(\varepsilon)=\mu_*+O(|\varepsilon|),
\qquad
\omega(\varepsilon)=\omega_*+O(|\varepsilon|).
\]
It classifies the concrete A021 Hopf result as conjectural until characteristic functions are computed.

---

# Output F — Yield-parity limitation

The response correctly limits the conclusion to loss of the exponential-smallness mechanism at $\Delta_y=0$ and does not rule out other reductions.

---

# Output G — Publication-ready replacement LaTeX

The response supplies LaTeX with:

- phase-space definitions;
- a finite-time perturbation theorem;
- a conditional NHIM template;
- a direct spectral Hopf theorem;
- parity and status paragraphs;
- the same compactness and normal-bundle diagnosis.

---

# Output H — Verification checklist

The response lists compact invariant binding object, equicontinuity, tangent growth, full normal bounds, domination ratio, perturbation norm, projection transversality, equilibrium/spectral data, yield-gap lower bound, neighborhood bounds, boundary character, and route-specific backward uniqueness.

---

**Bottom line in the response:** Only the finite-time theorem is fully proved. The vertical graph, NHIM persistence for concrete A021, and Hopf shift remain conditional/conjectural until the checklist is discharged.

## Full response note

The full user-supplied response also contains detailed theorem statements, proofs, hypothesis tables, a publication-ready LaTeX block, and the explicit final statement that only finite-time tracking is unconditional. Its mathematical content and internal consistency are inventoried separately in `point_inventory.md` for joint review.
# Specialist Proof Analysis — A021 RFDE Yield-Gap Invariant Graph

## Output A — Original-claim diagnosis

The original claim (persistence of  
\[
M_0=\bigl\{(\phi,\widehat y_*):\phi\in C([-\tau,0],K_x)\bigr\}
\]  
as a vertical graph \(y_t=h_\varepsilon(x_t)\)) is **not well-posed**. The following independent obstructions each defeat a direct application of any standard NHIM theorem.

### A.1 Compactness failure
Let \(K_x\subset\R^m\) be compact. The set  
\[
\mathcal{K}:=C([-\tau,0],K_x)
\]  
is closed and bounded in \(X=C([-\tau,0],\R^m)\) but **not compact**. Equicontinuity is missing: the family of constant functions is equicontinuous, but arbitrary continuous curves in \(K_x\) need not be. Arzelà–Ascoli requires a uniform Lipschitz (or modulus-of-continuity) bound that is not implied by invariance of a bounded set for a general \(C^1\) RFDE. Boundedness of histories does **not** yield precompactness in the supremum norm.

### A.2 Manifold-structure failure
Even if a compact invariant set \(\mathcal{A}_x\subset X\) exists, it need not be a \(C^r\) embedded Banach submanifold. Absorbing sets, global attractors, or omega-limit sets of RFDEs are typically compact metric spaces with no manifold structure. Normally hyperbolic invariant-manifold theorems require a \(C^r\) submanifold (or at least a \(C^1\) embedded disk/annulus with boundary) together with a continuous splitting of the tangent bundle. Invariance + boundedness alone are insufficient.

### A.3 Incomplete normal bundle
Suppose \(\mathcal{A}_x\subset X\) is a proper invariant submanifold. The candidate  
\[
M_0=\mathcal{A}_x\times\{\widehat y_*\}\subset B=X\times Y
\]  
has normal space at each point that contains  
- all directions in \(T_\phi X\) transverse to \(T_\phi\mathcal{A}_x\), **and**  
- the full fibre \(Y\).  
Treating only the slack variable \(y\) as normal ignores the transverse \(x\)-directions. A spectral-gap assumption solely on \(DG(\widehat y_*)\) does not control the full normal bundle. Consequently the domination condition required by any NHIM theorem is not even stated.

### A.4 Semiflow versus two-sided flow
The RFDE (1) generates a **semiflow** \(\Phi_\varepsilon^t\) (\(t\ge0\)), not a flow. Backward uniqueness fails in general: a history \(\phi\in X\) may possess multiple continuous backward extensions, or none that remain in a prescribed set. Graph-transform or Lyapunov–Perron arguments that integrate along complete base orbits therefore require an additional unique-backward-continuation hypothesis that is not automatic. One-sided (inflowing/overflowing) formulations must be used instead; the original claim never supplies them.

### A.5 Vertical-graph failure
Even when a perturbed manifold \(M_\varepsilon\) exists, the natural parameterization furnished by the persistence theorem is an embedding  
\[
\iota_\varepsilon(\phi)=\bigl(\phi+u_\varepsilon(\phi),\;\widehat y_*+v_\varepsilon(\phi)\bigr),
\]  
not necessarily a vertical graph over the original base. A vertical representation  
\[
M_\varepsilon=\bigl\{(\psi,h_\varepsilon(\psi)):\psi\in\mathcal{A}_{x,\varepsilon}\bigr\}
\]  
holds only after one proves that the \(x\)-projection \(\pi_x|_{M_\varepsilon}\) is a \(C^1\)-diffeomorphism onto its image. This is an extra transversality argument that was omitted.

**Conclusion.** Any of A.1–A.5 already renders the original proof invalid. The most immediate fatal gaps are the absence of a compact \(C^r\) base manifold and the incomplete normal bundle.

---

## Output B — Strongest valid theorem

We separate four statements of decreasing strength. Only the first two are theorems; the third is a conditional theorem under explicit extra hypotheses; the fourth is a conjecture.

### B.1 Finite-time perturbation (unconditional under standard RFDE hypotheses)

**Theorem 1 (Finite-time \(O(\varepsilon)\) tracking).**  
Assume:
- \(F\in C^1(X_0,\R^m)\), \(G\in C^1(Y_0,\R^n)\), \(f,g\in C^1(B_0,\R^{m+n})\) on open sets \(X_0\subset X\), \(Y_0\subset Y\), \(B_0\subset B\);
- local existence, uniqueness and continuous dependence for (1);
- there exist \(R>0\), \(T>0\) and a bounded set \(U\subset B_0\) such that every solution of (1) and of (4) starting in \(U\) remains in a common compact subset of \(B_0\) on \([0,T]\).

Then there is \(C_T<\infty\) (depending on Lipschitz constants on the compact set and on \(T\)) such that if \(z_\varepsilon(t)=(x^\varepsilon_t,y^\varepsilon_t)\) and \(z_0(t)=(x^0_t,y^0_t)\) are solutions with \(z_\varepsilon(0)=z_0(0)\in U\),  
\[
\|z_\varepsilon-z_0\|_{C([0,T],B)}\le C_T\varepsilon.
\]
In particular the \(y\)-components satisfy \(\|y^\varepsilon_t-\widehat y_*\|\le C_T\varepsilon\) whenever the unperturbed \(y\)-solution is identically \(\widehat y_*\) and the initial \(y\)-history is \(O(\varepsilon)\)-close to \(\widehat y_*\).

No invariant manifold is claimed.

### B.2 Lipschitz graph over a compact equicontinuous positively invariant set (Route D)

**Theorem 2 (Lipschitz invariant graph — conditional).**  
Assume in addition:
- the binding equation \(\dot x=F(x_t)\) admits a compact, positively invariant set  
  \[
  K_{M,L}=\{\phi\in X:\|\phi\|_\infty\le M,\;\operatorname{Lip}(\phi)\le L\}
  \]  
  that is mapped into itself by the time-\(T\) map for some \(T>\tau\) (hence compact by Arzelà–Ascoli);
- \(\widehat y_*\) is locally exponentially stable for \(\dot y=G(y_t)\) with rate \(\beta>0\);
- the coupling terms satisfy \(\|f\|+\|g\|\le C\) and \(\operatorname{Lip}(f,g)\le C\) uniformly on a neighborhood of \(K_{M,L}\times\{\widehat y_*\}\);
- \(\varepsilon>0\) is small enough that the perturbed time-\(T\) map sends a Lipschitz-graph bundle over \(K_{M,L}\) into itself and is a contraction in the sup-Lipschitz metric (explicit smallness: \(\varepsilon C(1+e^{\omega T})<\gamma\) where \(\gamma\) is the contraction rate induced by \(\beta\)).

Then there exists a Lipschitz function  
\[
h_\varepsilon:K_{M,L}\to Y,\qquad \|h_\varepsilon-\widehat y_*\|_\infty\le C\varepsilon,
\]  
whose graph is positively invariant under the time-\(T\) map of (1). The graph is in general only Lipschitz, not \(C^1\).

### B.3 Conditional \(C^1\) NHIM persistence (Route B — time-\(T\) map)

**Theorem 3 (Conditional \(C^1\) NHIM).**  
Assume the hypotheses of the well-posedness audit (Output C below) and:
1. there exists a compact \(C^r\) embedded submanifold \(\mathcal{A}_x\subset X\) (\(r\ge1\)), invariant under the binding semiflow, possibly with inflowing boundary;
2. the time-\(T\) map \(P_0=\Phi_0^T\) (\(T>\tau\)) is \(C^r\) on a neighborhood of \(M_0:=\mathcal{A}_x\times\{\widehat y_*\}\) and admits a continuous \(DP_0\)-invariant splitting  
   \[
   TB\big|_{M_0}=T M_0\oplus E^s
   \]  
   (or the full stable/unstable splitting if needed) satisfying the rate conditions  
   \[
   \|DP_0|_{E^s}\|\le M_s e^{-\beta T},\qquad
   \|DP_0|_{TM_0}\|\le M_c e^{\alpha T},\qquad
   \beta>r\alpha\ge0;
   \]  
   the stable bundle \(E^s\) contains **all** directions normal to \(M_0\), including transverse directions in \(X\) and the full \(Y\)-fibre;
3. \(\|P_\varepsilon-P_0\|_{C^1}=O(\varepsilon)\) on a uniform tubular neighborhood of \(M_0\);
4. the external persistence theorem of Bates–Lu–Zeng (or an equivalent Banach-space map theorem) applies verbatim under (1)–(3).

Then for all sufficiently small \(\varepsilon>0\) there exists a \(C^r\) embedded manifold \(M_\varepsilon=\iota_\varepsilon(\mathcal{A}_x)\) with  
\[
\|\iota_\varepsilon-\iota_0\|_{C^1}\le C\varepsilon,
\]  
positively invariant under \(P_\varepsilon\), and locally exponentially attracting with rate \(\beta'= \beta-O(\varepsilon)\). If in addition \(\pi_x|_{M_\varepsilon}\) is a \(C^1\)-diffeomorphism onto its image, \(M_\varepsilon\) is the vertical graph of a \(C^r\) map \(h_\varepsilon\).

**All of (1)–(4) are extra hypotheses not implied by exponential stability of \(\widehat y_*\) alone.**

### B.4 Conjecture (full vertical graph for the A021 blocks)

**Conjecture 4.**  
If each concrete binding block of A021 is shown to possess a compact \(C^1\) normally hyperbolic attracting manifold whose normal rates (including all transverse \(x\)-modes) dominate the tangent growth by a margin larger than the coupling size \(C_{\mathrm{gap}}e^{-\rho\Delta_y}+\varepsilon_{\mathrm{phys}}\), then the conclusion of Theorem 3 holds and the manifold is a vertical graph \(y_t=h_\varepsilon(x_t)\).

This remains a conjecture until the spectral and compactness obligations of the verification checklist (Output H) are discharged for the concrete equations.

---

## Output C — Complete proof

### C.1 Well-posedness audit (mandatory)

- **Domains.** Let \(X_0\subset X\), \(Y_0\subset Y\) be open and \(B_0=X_0\times Y_0\). Assume \(F:X_0\to\R^m\), \(G:Y_0\to\R^n\), \(f:B_0\to\R^m\), \(g:B_0\to\R^n\).
- **Smoothness.** \(F,G,f,g\in C^r\) with \(r\ge1\).
- **Local existence.** For every \((\phi,\psi)\in B_0\) there exist \(t_+>0\) and a unique continuous solution  
  \[
  (x,y):[-\tau,t_+)\to\R^{m+n}
  \]  
  with \((x_0,y_0)=(\phi,\psi)\) satisfying (1) almost everywhere (or everywhere if the right-hand sides are continuous). Continuation holds up to the boundary of \(B_0\).
- **Semiflow.** The solution operators \(\Phi_\varepsilon^t\) form a \(C^0\)-semiflow on \(B_0\) for \(t\ge0\). For \(t>\tau\) the operators are compact (smoothing by integration). Differentiability of \(\Phi_\varepsilon^t\) with respect to initial data holds for \(t>0\) under the \(C^1\) assumption (standard variational equation along the RFDE).
- **Norm.** Supremum norm on \(X\) and \(Y\); product norm on \(B\).
- **Delays.** Fixed delay \(\tau>0\) (not state-dependent).
- **Boundary.** If a manifold with boundary is used, the boundary is assumed inflowing for the unperturbed semiflow (or the theorem is local in the interior).

No claim is made that bounded orbits are precompact without an equicontinuity or smoothing argument.

### C.2 Proof of Theorem 1 (finite-time tracking)

Let \(U\subset B_0\) be as in the statement and let \(K\subset B_0\) be a compact set containing all orbits of both the perturbed and unperturbed equations on \([0,T]\) that start in \(U\). On \(K\) the maps \(F,G,f,g\) are bounded and Lipschitz; write  
\[
L=\operatorname{Lip}(F)+\operatorname{Lip}(G)+\operatorname{Lip}(f)+\operatorname{Lip}(g),\qquad
M=\|f\|_\infty+\|g\|_\infty.
\]
Let \(z_\varepsilon=(x^\varepsilon,y^\varepsilon)\) and \(z_0=(x^0,y^0)\) with the same initial history. The integral forms differ by  
\[
\begin{aligned}
x^\varepsilon(t)-x^0(t)
&=\int_0^t\Bigl(F(x^\varepsilon_s)-F(x^0_s)+\varepsilon f(x^\varepsilon_s,y^\varepsilon_s)\Bigr)ds,\\
y^\varepsilon(t)-y^0(t)
&=\int_0^t\Bigl(G(y^\varepsilon_s)-G(y^0_s)+\varepsilon g(x^\varepsilon_s,y^\varepsilon_s)\Bigr)ds.
\end{aligned}
\]
Taking supremum norms on histories and applying Gronwall’s inequality yields  
\[
\sup_{t\in[0,T]}\bigl(\|x^\varepsilon_t-x^0_t\|+\|y^\varepsilon_t-y^0_t\|\bigr)
\le C(T,L)M\varepsilon\,e^{LT}=:C_T\varepsilon.
\]
This is the claimed estimate. No invariant set is used beyond the a-priori confinement to \(K\).

### C.3 Proof of Theorem 2 (Lipschitz graph)

**Step 1 — Compactness.**  
\(K_{M,L}\) is closed, bounded and equicontinuous, hence compact in \(X\) by Arzelà–Ascoli. Positive invariance under the binding time-\(T\) map is an assumption (must be checked on the concrete vector field; it follows if the binding RFDE has an a-priori \(L^\infty\) bound and a Lipschitz bound coming from the equation itself after time \(\tau\)).

**Step 2 — Graph transform.**  
Let \(\mathcal{G}_\delta\) be the complete metric space of Lipschitz maps  
\[
h:K_{M,L}\to Y,\qquad \|h-\widehat y_*\|_\infty\le\delta,\qquad\operatorname{Lip}(h)\le\ell,
\]  
with metric \(d(h_1,h_2)=\|h_1-h_2\|_\infty\). For \(\varepsilon\) small and \(\delta=C\varepsilon\), \(\ell\) fixed large enough, define the graph transform \(\Gamma_\varepsilon h\) by  
\[
\operatorname{graph}(\Gamma_\varepsilon h)=P_\varepsilon\bigl(\operatorname{graph}(h)\bigr)\cap\bigl(K_{M,L}\times Y\bigr),
\]  
where \(P_\varepsilon=\Phi_\varepsilon^T\). Because the unperturbed \(y\)-dynamics contracts toward \(\widehat y_*\) at rate \(e^{-\beta T}\) and the coupling is \(O(\varepsilon)\), a standard estimate (variation of constants for the \(y\)-component along the base orbit) shows that \(\Gamma_\varepsilon\) maps \(\mathcal{G}_\delta\) into itself once  
\[
e^{-\beta T}\delta+C\varepsilon(1+\ell)<\delta
\]  
and the Lipschitz constant is controlled by a similar inequality provided \(\beta T\) dominates the base Lipschitz constant plus \(O(\varepsilon)\).  

**Step 3 — Contraction.**  
The same variation-of-constants representation yields  
\[
d(\Gamma_\varepsilon h_1,\Gamma_\varepsilon h_2)\le\bigl(e^{-\beta T}+C\varepsilon\bigr)d(h_1,h_2).
\]  
For \(\varepsilon\) small the factor is \(<1\). The unique fixed point \(h_\varepsilon\) has Lipschitz graph invariant under \(P_\varepsilon\). Positive invariance of the graph under the semiflow for all \(t\ge0\) follows by the usual concatenation argument for time-\(T\) maps once \(T\) is fixed.

**Step 4 — No \(C^1\) claim.**  
The contraction is in the \(C^0\) metric on a Lipschitz ball; the derivative graph transform is not shown to be contractive. Hence only Lipschitz regularity is obtained.

### C.4 Sketch of the conditional proof of Theorem 3

Under the extra spectral-gap and compactness hypotheses, the time-\(T\) map \(P_0\) satisfies all structural assumptions of the Bates–Lu–Zeng persistence theorem for normally hyperbolic invariant manifolds of \(C^r\) maps on Banach spaces (compact base, continuous splitting, rate conditions \(\beta>r\alpha\), \(C^1\)-small perturbation). The theorem directly yields a \(C^r\) manifold \(M_\varepsilon\) that is a \(C^1\)-small graph in the tubular coordinates of the normal bundle of \(M_0\). Invariance under \(P_\varepsilon\) and local exponential attraction follow from the same reference. The vertical-graph representation requires the additional (open) verification that \(D\pi_x|_{TM_\varepsilon}\) remains invertible, which holds for small \(\varepsilon\) by the implicit-function theorem once it holds at \(\varepsilon=0\) (i.e., once the normal bundle has been chosen so that the \(x\)-component of the normal space is complementary to \(T\mathcal{A}_x\)).

All rate constants and the tubular radius must be uniform, which is part of the “bounded geometry” package already contained in the compactness of \(\mathcal{A}_x\).

### C.5 Why a full Lyapunov–Perron proof is not given

A self-contained Lyapunov–Perron argument would require unique two-sided base orbits on \(\mathcal{A}_x\). For a general RFDE this forces either  
- \(\mathcal{A}_x\) to be a single equilibrium or periodic orbit (too restrictive for A021), or  
- an a-priori unique-backward-continuation assumption that is not implied by the equations.  
Route B (time-\(T\) map) avoids backward orbits and is therefore preferred; the external theorem already encodes the fixed-point argument.

---

## Output D — Hypothesis-matching table

External theorem used for the conditional \(C^1\) result:  
Bates, P.W., Lu, K. & Zeng, C. *Existence and Persistence of Invariant Manifolds for Semiflows in Banach Space*. Memoirs of the American Mathematical Society, Vol. 135, No. 645 (1998). (Alternatively the map version in their later work on NHIM for infinite-dimensional dynamical systems.)  
Setting: \(C^r\) maps/semiflows on Banach spaces, compact normally hyperbolic invariant manifolds, exponential dichotomies, graph transform / Lyapunov–Perron.

| External theorem hypothesis | A021 object/assumption | Verification or unresolved obligation |
|-----------------------------|------------------------|---------------------------------------|
| Ambient space Banach | \(B=X\times Y=C([-\tau,0],\R^{m+n})\) | Verified (sup-norm) |
| \(C^r\) semiflow/map, \(r\ge1\) | Time-\(T\) map \(P_\varepsilon=\Phi_\varepsilon^T\), \(T>\tau\) | Verified for \(t>\tau\) under \(C^r\) right-hand sides; \(C^1\)-closeness \(O(\varepsilon)\) by variational equation + Gronwall |
| Compact \(C^r\) embedded base manifold \(M_0\) | \(\mathcal{A}_x\times\{\widehat y_*\}\) | **Unresolved**: existence of compact \(C^r\) manifold \(\mathcal{A}_x\) for the binding RFDE must be proved separately |
| Continuous \(DP\)-invariant splitting \(TM_0\oplus E^s\) | Full normal bundle = (transverse \(X\)) \(\oplus Y\) | **Unresolved**: spectral gap for all normal directions, not only slack block |
| Rates \(\|DP|_{E^s}\|\le M_se^{-\beta T}\), \(\|DP|_{TM_0}\|\le M_ce^{\alpha T}\), \(\beta>r\alpha\) | Normal rate from linearization at \(\widehat y_*\) plus transverse binding spectrum; tangent rate from binding linearization on \(\mathcal{A}_x\) | **Unresolved**: concrete eigenvalue/growth bounds needed; domination may fail if binding block itself has slow modes |
| Uniform tubular neighborhood & projection | Compactness of \(M_0\) supplies them | Conditional on compactness of \(\mathcal{A}_x\) |
| Perturbation small in \(C^1\) | \(\varepsilon=C_{\mathrm{gap}}e^{-\rho\Delta_y}+\varepsilon_{\mathrm{phys}}\) | Verified once \(\Delta_y>0\) fixed and \(\varepsilon_{\mathrm{phys}}\) small; size must be \(<\operatorname{gap}\) |
| Inflowing boundary (if any) | Boundary of \(\mathcal{A}_x\) | **Unresolved** if \(\mathcal{A}_x\) has boundary |
| Conclusion: \(C^r\) persistent manifold, locally exponentially attracting | \(M_\varepsilon=\iota_\varepsilon(\mathcal{A}_x)\) | Follows from theorem **once all rows above are verified** |
| Vertical graph over original base | \(\pi_x|_{M_\varepsilon}\) diffeomorphism | Extra obligation; true for small \(\varepsilon\) if normal bundle is chosen complementary to the \(x\)-tangent space |

A pure finite-dimensional Fenichel citation is **not** used and would be invalid.

---

## Output E — Hopf result

### E.1 Direct full-RFDE Hopf (preferred when the graph is unavailable)

**Theorem 5 (Direct Hopf persistence — conditional).**  
Assume:
- the uncoupled system (\(\varepsilon=0\)) possesses an equilibrium \(z_*=(x_*,\widehat y_*)\) whose characteristic operator  
  \[
  \Delta_0(\lambda)= \operatorname{diag}\bigl(\lambda I-DF(\widehat x_*)e^{\lambda\cdot},\;\lambda I-DG(\widehat y_*)e^{\lambda\cdot}\bigr)
  \]  
  has a simple pair of roots \(\pm i\omega_*\) on the imaginary axis, no other imaginary roots, and the rest of the spectrum in \(\operatorname{Re}\lambda\le-\delta<0\);
- the pair crosses the imaginary axis transversely under a distinguished parameter (e.g., a delay or a kinetic coefficient) with non-zero speed;
- the coupled characteristic operator \(\Delta_\varepsilon(\lambda)\) is a \(C^1\) perturbation of \(\Delta_0(\lambda)\) of size \(O(\varepsilon)\) in the operator norm on the appropriate exponential-weight space;
- the imaginary pair remains separated from the rest of the spectrum by a uniform gap for small \(\varepsilon\).

Then there exists a unique \(C^1\) curve of equilibria \(z_*(\varepsilon)\) and a unique \(C^1\) curve of simple characteristic roots \(\lambda(\varepsilon)=\alpha(\varepsilon)+i\omega(\varepsilon)\) with \(\alpha(0)=0\), \(\omega(0)=\omega_*\), \(\alpha'(0)\ne0\) (after possible re-parameterization). Consequently a local Hopf bifurcation occurs at a parameter value  
\[
\tau_*(\varepsilon)=\tau_*+O(\varepsilon)
\]  
(or the analogous kinetic parameter). The bifurcating periodic orbits are those of the full coupled RFDE.

**Proof sketch.** The characteristic matrix function depends \(C^1\)-smoothly on \(\varepsilon\) by the assumed smoothness of \(F,G,f,g\) and the equilibrium curve (implicit-function theorem on the equilibrium map). Rouché’s theorem on a small contour about \(i\omega_*\) keeps exactly one root inside; the root is simple and moves \(C^1\)-smoothly. Transversality persists for small \(\varepsilon\). The classical Hopf theorem for RFDEs (Hale, or Diekmann et al.) then applies directly to the full system. No invariant-graph reduction is required.

### E.2 Graph-based corollary (only after Theorem 3)

If the conditional NHIM of Theorem 3 has been established and the center subspace at the Hopf point lies inside the tangent bundle of \(M_\varepsilon\) while the normal spectrum remains uniformly stable, then the Hopf bifurcation of the reduced vector field on \(M_\varepsilon\) is also a Hopf bifurcation of the full RFDE, and the same expansion \(\tau_*(\varepsilon)=\tau_*+O(\varepsilon)\) holds. This route is strictly heavier than E.1 and is not needed for local Hopf persistence.

### E.3 What is not claimed
Local Hopf persistence does **not** imply persistence of global periodic folds, canards, or large-amplitude relaxation cycles. Those require separate global arguments.

---

## Output F — Yield-parity limitation

When the yield gap vanishes,  
\[
\Delta_y=0\qquad\Longrightarrow\qquad\pi_j=O(1)
\]  
for every competing soft-minimum weight (see (3)). Consequently the prefactor \(C_{\mathrm{gap}}e^{-\rho\Delta_y}\) in the coupling strength (2) becomes \(O(1)\). The exponential smallness that makes \(\varepsilon\) a singular perturbation parameter disappears.  

**Precise conclusion:** the yield-gap mechanism that produces an exponentially small coupling (and thereby makes a normally hyperbolic persistence argument possible for small \(\varepsilon\)) **fails**.  

This does **not** assert that no other invariant-manifold or averaging reduction can exist by a different mechanism; it only asserts that the specific exponential-smallness route used in A021 is unavailable at yield parity.

---

## Output G — Publication-ready LaTeX

```latex
\subsection*{Phase space and standing hypotheses}

Fix $\tau>0$. Let
\[
X=C([-\tau,0],\R^m),\qquad
Y=C([-\tau,0],\R^n),\qquad
B=X\times Y,
\]
equipped with the supremum norm. For a continuous trajectory we write
$x_t(\theta)=x(t+\theta)$, $\theta\in[-\tau,0]$, and likewise for $y$. 
Consider the coupled RFDE
\begin{equation}
\label{eq:A021}
\begin{aligned}
\dot x(t)&=F(x_t)+\varepsilon f(x_t,y_t),\\
\dot y(t)&=G(y_t)+\varepsilon g(x_t,y_t),
\end{aligned}
\end{equation}
where $F\in C^r(X_0,\R^m)$, $G\in C^r(Y_0,\R^n)$, $f,g\in C^r(B_0,\R^{m+n})$
($r\ge1$) on open sets $X_0\subset X$, $Y_0\subset Y$, $B_0\subset B$.
The parameter admits the yield-gap representation
\[
\varepsilon=C_{\mathrm{gap}}e^{-\rho\Delta_y}+\varepsilon_{\mathrm{phys}},
\qquad\rho>0,\;\Delta_y>0,\;\varepsilon_{\mathrm{phys}}\ge0.
\]
Local existence, uniqueness, continuation and continuous dependence
for~\eqref{eq:A021} are assumed; the solution operators $\Phi_\varepsilon^t$
form a $C^0$-semiflow on $B_0$ that is compact for $t>\tau$.

At $\varepsilon=0$ the systems decouple. Let $\widehat y_*\in Y$ be the
constant history of an equilibrium $y_*\in\R^n$ of the slack equation.

\subsection*{Finite-time perturbation theorem}

\begin{theorem}[Finite-time $O(\varepsilon)$ tracking]
Assume there exist $R,T>0$ and a bounded set $U\subset B_0$ such that
all solutions of~\eqref{eq:A021} and of the uncoupled system that start
in $U$ remain in a common compact subset of $B_0$ on the interval $[0,T]$.
Then there is a constant $C_T<\infty$ such that any two solutions
$z_\varepsilon$ and $z_0$ with identical initial data in $U$ satisfy
\[
\|z_\varepsilon-z_0\|_{C([0,T],B)}\le C_T\varepsilon.
\]
\end{theorem}

\begin{proof}
On the compact confining set the nonlinearities are bounded and Lipschitz.
Subtracting the integral equations and applying Gronwall's inequality
yields the claim.
\end{proof}

\subsection*{Conditional invariant-graph theorem}

\begin{theorem}[Conditional $C^1$ NHIM for the time-$T$ map]
\label{thm:cond-NHIM}
Let $T>\tau$ and write $P_\varepsilon=\Phi_\varepsilon^T$. Assume:
\begin{enumerate}
\item the binding semiflow admits a compact $C^r$ embedded invariant
  manifold $\mathcal{A}_x\subset X$ (possibly with inflowing boundary);
\item $M_0=\mathcal{A}_x\times\{\widehat y_*\}$ is normally hyperbolic
  for $P_0$ with $DP_0$-invariant splitting
  $TB|_{M_0}=TM_0\oplus E^s$ whose rates satisfy
  $\|DP_0|_{E^s}\|\le M_se^{-\beta T}$,
  $\|DP_0|_{TM_0}\|\le M_ce^{\alpha T}$ and $\beta>r\alpha$
  (the stable bundle $E^s$ contains every direction transverse to $M_0$,
  including transverse directions in $X$ and the whole fibre $Y$);
\item $\|P_\varepsilon-P_0\|_{C^1}=O(\varepsilon)$ uniformly in a tubular
  neighborhood of $M_0$.
\end{enumerate}
Then, for all sufficiently small $\varepsilon>0$, there exists a $C^r$
embedded manifold $M_\varepsilon=\iota_\varepsilon(\mathcal{A}_x)$ with
$\|\iota_\varepsilon-\iota_0\|_{C^1}\le C\varepsilon$, positively invariant
under $P_\varepsilon$ and locally exponentially attracting. If in addition
$\pi_x|_{M_\varepsilon}$ is a diffeomorphism onto its image, $M_\varepsilon$
is the vertical graph of a $C^r$ map $h_\varepsilon$ satisfying
\[
\|h_\varepsilon-\widehat y_*\|_{C^0}\le C\varepsilon.
\]
\end{theorem}

\begin{remark}[Status]
The hypotheses on $\mathcal{A}_x$ and on the full normal spectrum are
\textbf{not} implied by exponential stability of $\widehat y_*$ alone.
They must be verified on the concrete binding blocks. Until that
verification is complete, Theorem~\ref{thm:cond-NHIM} remains conditional
and the vertical-graph representation of the A021 slow manifold is a
conjecture.
\end{remark}

\subsection*{Hopf persistence}

\begin{theorem}[Direct Hopf persistence]
Assume the uncoupled characteristic operator possesses a simple pair
$\pm i\omega_*$ and no other imaginary spectrum, that the pair crosses
transversely under a distinguished parameter, and that the coupled
characteristic operator is a $C^1$ perturbation of size $O(\varepsilon)$.
Then the Hopf point persists:
\[
\tau_*(\varepsilon)=\tau_*+O(\varepsilon)
\]
(or the analogous statement for a kinetic bifurcation parameter).
The bifurcating periodic orbits are those of the full coupled RFDE.
\end{theorem}

\subsection*{Yield-parity limitation}

If $\Delta_y=0$, then the soft-minimum weights remain $O(1)$ and the
exponential factor $e^{-\rho\Delta_y}$ disappears from~$\varepsilon$.
The yield-gap mechanism that produces an exponentially small coupling
therefore fails. This does not preclude the existence of other reductions,
but it removes the singular-perturbation justification used above.

\subsection*{Status paragraph}

The original claim that
$M_0=C([-\tau,0],K_x)\times\{\widehat y_*\}$
persists as a vertical graph $y_t=h_\varepsilon(x_t)$ is not justified:
$C([-\tau,0],K_x)$ is not compact, need not be a manifold, the normal
bundle is larger than the slack fibre, the RFDE semiflow need not be
invertible, and vertical graphs are not automatic. The strongest
unconditional result is finite-time $O(\varepsilon)$ tracking. A $C^1$
normally hyperbolic invariant manifold persists once a compact $C^r$
binding manifold with a sufficient spectral gap in the \emph{full}
normal bundle is established; that spectral-gap obligation is left to
the concrete A021 blocks. Local Hopf bifurcation of the full system
persists under standard characteristic-operator hypotheses without
any graph reduction. At yield parity the exponential smallness of the
coupling is lost.
```

---

## Output H — Verification checklist

Concrete quantities that must be checked on the actual A021 binding and slack blocks before any NHIM claim can be asserted:

1. **Compact invariant binding object**  
   Existence of a compact set \(\mathcal{A}_x\subset X\) that is invariant (or absorbing and then replace by the attractor) under \(\dot x=F(x_t)\). If a manifold is required, prove it is a \(C^r\) embedded submanifold (e.g., via a prior Fenichel or Hopf reduction inside the binding block).

2. **Equicontinuity / smoothing**  
   Uniform Lipschitz bound (or modulus of continuity) on histories in \(\mathcal{A}_x\), or use of the smoothing property for \(t>\tau\), so that Arzelà–Ascoli applies.

3. **Tangent growth bound**  
   Constant \(\alpha\in\R\) such that \(\|D\Phi_0^t|_{T\mathcal{A}_x}\|\le M_c e^{\alpha t}\) (or the discrete analogue for the time-\(T\) map).

4. **Full normal spectral bound**  
   Exponential decay rate \(\beta>0\) on the whole normal bundle of \(M_0=\mathcal{A}_x\times\{\widehat y_*\}\), including:  
   - all directions in \(X\) transverse to \(\mathcal{A}_x\),  
   - the full slack fibre \(Y\).  
   A stable eigenvalue of \(DG(\widehat y_*)\) alone is insufficient.

5. **Domination ratio**  
   Verify \(\beta>r\alpha\) (or the precise inequality required by the cited theorem). Compute the numerical margin.

6. **Perturbation \(C^1\) norm**  
   Explicit bound \(\|P_\varepsilon-P_0\|_{C^1}\le C\varepsilon\) on a uniform tubular neighborhood; confirm that \(C\varepsilon\) is smaller than the spectral gap.

7. **Projection transversality**  
   If a vertical graph is desired, prove that \(D\pi_x\) remains invertible on \(TM_\varepsilon\) for small \(\varepsilon\).

8. **Equilibrium and characteristic spectra (Hopf)**  
   Location of the equilibrium, simplicity of \(\pm i\omega_*\), spectral gap to the rest of the spectrum, transverse crossing speed, and \(O(\varepsilon)\) closeness of the coupled characteristic operator.

9. **Yield-gap lower bound**  
   Concrete positive lower bound on \(\Delta_y\) (or on \(\rho\Delta_y\)) that makes \(C_{\mathrm{gap}}e^{-\rho\Delta_y}\) smaller than the domination margin; separate control of \(\varepsilon_{\mathrm{phys}}\).

10. **Neighborhood and continuation bounds**  
    Radius of the tubular neighborhood in which the NHIM theorem operates, and a-priori bounds preventing blow-up on the time scales of interest.

11. **Boundary character**  
    If \(\mathcal{A}_x\) has a boundary, verify it is inflowing (or restrict the theorem to the interior).

12. **Backward uniqueness (only if a two-sided flow argument is used)**  
    Not required for the time-\(T\) map route; mandatory for a classical Lyapunov–Perron argument along complete orbits.

---

**Final assessment.**  
The original vertical-graph claim is defeated by compactness, manifold structure, incomplete normal bundle, semiflow character, and projection issues. The strongest statements that are actually proved under minimal hypotheses are the finite-time \(O(\varepsilon)\) estimate (Theorem 1) and the conditional Lipschitz-graph statement (Theorem 2). A \(C^1\) NHIM persists only after the full spectral-gap and compactness obligations listed above are discharged; until then it remains a precisely formulated conjecture. Local Hopf bifurcation of the full RFDE is independent of the graph and persists under standard characteristic-operator hypotheses. At yield parity the exponential smallness mechanism fails.

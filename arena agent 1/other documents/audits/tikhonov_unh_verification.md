# Tikhonov reduction — hypothesis verification and the "exact" verdict (2026-09-03)

**Audit point.** "The manuscript calls the three-state core the 'exact leading-order slow
manifold' via Tikhonov's theorem, but the theorem's actual hypotheses (uniform normal
hyperbolicity, correct epsilon-scaling, RFDE-specific convergence) are not fully verified."
Directive: state the precise RFDE/DAE singular-perturbation hypotheses, verify uniform
normal hyperbolicity computationally, then decide whether "exact" is defensible.

## 1. Where the claim lives now

- The quoted phrase is **v18/A018** ("the leading-order slow manifold … obtained by
  eliminating the fast macroeconomic variables via Tikhonov's theorem", `sec:asymptotic-reduction`,
  `sec:core-model`). The corrected manuscript layer (`manuscript_corrected.txt`) already
  replaces it with the formal chain: **Theorem (exact triangular projection)** →
  **Theorem (finite-time reduction, conditional)** → **Theorem (working-core projection)**
  → **Theorem (frozen-A)** → **Theorem (Hopf persistence, conditional)**, with
  Hypotheses `hyp:scale`/`hyp:hurwitz`/`hyp:lipschitz`.
- Our latest rewrites inherit that chain: **P4 v13** Proposition 1 (frozen-A inner
  approximation, "not a Tikhonov reduction"), Proposition 2 (Hopf persistence,
  conditional), and supplementary **S5** carrying the macro-reduction conjecture with
  the declared gap: "The Hurwitz hypothesis on the fast Jacobian is supported by a
  finite-difference sweep on the literature-anchored class and is not proved on the
  whole domain."
- **Verdict on applicability**: the audit point applies to the v18 phrasing, not to the
  rewrites' phrasing — with one residual slip in P4 v13 (fixed in v14, §5 below): a
  sentence placing the 3.2% Hopf shift "inside the frozen-active-pool bound of
  Proposition 1", which is a category error (the bound is on trajectories, not on
  eigenvalue locations). What the rewrites lacked was not honesty but the *executed*
  verification of the spectral hypothesis. That is now supplied, and it changes the
  status of the hypothesis from "sweep-supported" to "proved on a parameter set,
  sweep-quantified on the anchored class".

## 2. The precise theorem (RFDE/DAE Tikhonov, finite-time)

**Setting.** State $(x, y)$ with slow $x \in \mathbb{R}^5$ (N, A, U, Z, E), fast
$y \in \mathbb{R}^4$ (K, L, A_TFP, T), algebraic $p$; histories in
$C([-\tau, 0], \mathbb{R}^5)$:

$$\dot x = g(x, y, x(t-\tau), p, \varepsilon), \qquad \varepsilon \dot y = f(x, y, \varepsilon), \qquad 0 = F(x, p) - qEN,$$

where $F(\cdot, p)$ is the (CES) demand function and the delay enters **only** through
the slow variable. The physical system is the member $\varepsilon = 1$ of the family
(the `hyp:scale` rate-constant scalings define the family).

**Hypotheses.**
- **(H1, DAE regularity)** $F$ is $C^1$ and strictly decreasing in $p$, so the algebraic
  equation has a unique solution $p^*(x)$ with $\|(\partial F/\partial p)^{-1}\|$ bounded
  on the compact slow set $\mathcal{K}$ (index-1).
- **(H2, QSS manifold)** $f(x, \cdot, 0) = 0$ has a unique root $y = h(x)$ on $\mathcal{K}$,
  with $h$ $C^1$.
- **(H3, uniform normal hyperbolicity)** $D_y f(x, h(x), 0)$ has all eigenvalues in
  $\{\mathrm{Re} \le -\gamma_y < 0\}$, uniformly in $x \in \mathcal{K}$.
- **(H4, delay placement)** $f$ and $F$ contain no delayed arguments.
- **(H5, regularity)** $g, f$ locally Lipschitz; initial data compatible;
  $x(0)$ in the interior of $\mathcal{K}$.

**Conclusion.** For every finite $T$ there exist $\varepsilon_0, C$ such that for all
$\varepsilon \in (0, \varepsilon_0)$, with $x^0$ solving the reduced RFDE
$\dot x^0 = g(x^0, h(x^0), x^0(t-\tau), p^*(x^0), 0)$:

$$\sup_{[0,T]} \|x^\varepsilon - x^0\| \le C(\varepsilon + \omega_A T), \qquad
\|y^\varepsilon(t) - h(x^\varepsilon(t))\| \le C e^{-\gamma_y t/\varepsilon} + C(\varepsilon + \omega_A T).$$

**Proof sketch (in full, the standard argument).** On the fast clock $s = t/\varepsilon$
the slow state and the delayed history $x(\varepsilon s - \tau)$ vary at rate
$O(\varepsilon)$: H4 makes the fast block an ODE with a slowly drifting parameter, so
the classical boundary-layer argument (Tikhonov, 1952; the index-1 DAE treatment of
Hairer and Wanner, 1996) gives $y = h(x(0)) + O(e^{-\gamma_y t/\varepsilon})$ on the
layer. The slow-error equation $\dot e = g(x, y, x_\tau, p) - g(x^0, h(x^0), x^0_\tau, p^*)$
is driven by $y - h(x) = O(\varepsilon + e^{-\gamma_y t/\varepsilon})$ (via the Lipschitz
estimate in $y$) and by the algebraic error $p - p^* = O(\varepsilon)$ (implicit function
theorem on H1); the retarded Gronwall estimate (Hale and Verduyn Lunel, 1993, Ch. 6)
closes $\|e\|_{[0,T]} \le C(\varepsilon + \omega_A T)$, the $\omega_A T$ term being the
frozen-A drift allowance of Theorem `thm:frozenA`. The argument is finite-time by
construction; infinite-time persistence of the global bifurcation objects would need
the infinite-dimensional Fenichel-type machinery (spectral gap and compactness of the
memory kernel of the semigroup) — not verified, and not claimed.

## 3. The fast block, and uniform normal hyperbolicity as a theorem

The Layer-4 macro block, in the boundary-layer scaling of `hyp:scale`
($K_{\mathrm{ref}} = L_0 = Q_0 = a_{\max} = T_{\max} = 1$ after normalization):

$$\varepsilon \dot K = \varsigma Q - \delta_K K - \theta K \tilde\Delta, \quad
\varepsilon \dot L = r_{L,0} L (1 - L/L_{\max}(Q)), \quad
L_{\max} = \max(L_{\min}, Q^\eta),$$
$$\varepsilon \dot a = \eta_{A,0} a (1 - a) - \varepsilon \nu a \tilde\Delta, \quad
\varepsilon \dot T = (\eta_{T,0} + \eta_{T,1}\tilde\Delta T)(1 - T), \quad
Q = a K^{\alpha} L^{\beta} S_{\mathrm{agg}}^{\delta_S}, \quad \alpha+\beta+\delta_S = 1.$$

**Proposition (fast-block UNH, proved).** At the QSS $(a^*, T^*) = (1, 1)$,
$K^* = \varsigma Q/(\delta_K + \theta \tilde\Delta)$, $L^*$ the fixed point of
$L = \max(L_{\min}, Q(L)^\eta)$, the Jacobian $D_y f$ is block lower-triangular with
eigenvalues $\{-\eta_{A,0} - \nu\tilde\Delta,\ -(\eta_{T,0} + \eta_{T,1}\tilde\Delta)\} \cup \mathrm{eig}(J_{KL})$, where
$$J_{KL} = \begin{pmatrix} -(1-\alpha)(\delta_K + \theta\tilde\Delta) & \beta \varsigma Q/L \\ \eta\alpha r_{L,0} L/K & -r_{L,0}(1-\eta\beta) \end{pmatrix}$$
at the QSS, with trace $(\alpha-1)(\delta_K+\theta\tilde\Delta) + r_{L,0}(\eta\beta - 1)$
and determinant $r_{L,0}(\delta_K+\theta\tilde\Delta)(1 - \alpha - \eta\beta)$.
Hence $D_y f$ is Hurwitz **uniformly in $\tilde\Delta \ge 0$ and in the slow state** if
and only if
$$\alpha + \eta\beta < 1,$$
and the QSS fixed point is then unique (contraction with exponent $\eta\beta/(1-\alpha) < 1$);
at the labor floor the block is triangular with eigenvalues $-(1-\alpha)(\delta_K+\theta\tilde\Delta)$
and $-r_{L,0}$.

*Proof.* The K-row entries at the QSS use the identity $\varsigma Q/K = \delta_K + \theta\tilde\Delta$
(the K-QSS equation), giving $\partial(\varepsilon\dot K)/\partial K = \alpha(\delta_K+\theta\tilde\Delta)
- (\delta_K+\theta\tilde\Delta) = -(1-\alpha)(\delta_K+\theta\tilde\Delta)$; the L-row uses
$M' = \eta L_{\max}/Q$ at the interior fixed point. The determinant identity
$r_{L,0}(\delta_K+\theta\tilde\Delta)(1-\alpha-\eta\beta)$ follows from
$(\beta\varsigma Q/L)\cdot(\eta\alpha r_{L,0}L/K) = \eta\alpha\beta r_{L,0}(\delta_K+\theta\tilde\Delta)$.
Routh–Hurwitz for the $2\times2$ block: trace $< 0$ and determinant $> 0$ are both
equivalent to $\alpha + \eta\beta < 1$ (given $r_{L,0}, \delta_K > 0$). ∎

This upgrades the corrected manuscript's claim ("Hurwitzness is not a consequence of
triangularity … sweep only") to a theorem with an explicit, parameter-only condition:
the earlier pessimism was wrong — the QSS identity $\varsigma Q/K = \delta_K + \theta\tilde\Delta$,
not triangularity, collapses the block.

**Verification (committed, `analysis/unh_verification/`):**
- Sympy: the trace/determinant formulas reproduced symbolically.
- Finite differences: the analytic 4×4 Jacobian agrees with central differences of the
  vector field to $3.9\times10^{-7}$ across 400 draws × QSS roots (including unstable
  draws), ruling out assembly errors.
- Sweep (declared anchored class: $\alpha\in[0.25,0.45]$, $\beta\in[0.30,0.60]$,
  $\eta\in[0.3,1.2]$, $\varsigma\in[0.10,0.30]$, $\delta_K\in[0.03,0.10]$,
  $\theta\in[0,0.05]$, $\nu\in[0,0.02]$, $r_{L,0}\in[0.005,0.03]$,
  $\eta_{A,0}\in[0.005,0.02]$, $\eta_{T,0}\in[0.01,0.05]$, $\eta_{T,1}\in[0,0.5]$,
  $\tilde\Delta\in[0,5]$, $S_{\mathrm{agg}}\in[0.2,1]$; 11,792 accepted draws):
  - **1.9% of the declared class violates $\alpha+\eta\beta<1$**, and exactly there the
    fast block is genuinely unstable (worst $\mathrm{Re}\,\lambda = +3.9\times10^{-3}$;
    multi-root QSS confined to the same 0.7% subset). The hypothesis therefore does
    **not** hold on the declared class as stated.
  - On the restricted class $\{\alpha+\eta\beta \le 0.95\}$: worst
    $\mathrm{Re}\,\lambda = -4.1\times10^{-4}$ over 56,127 draws — uniform margin
    $\gamma_y \ge 4.1\times10^{-4}$; on $\{\alpha+\eta\beta \le 0.90\}$:
    $\gamma_y \ge 7.1\times10^{-4}$ (53,859 draws). The margin scales with the
    distance to the boundary, as the determinant formula predicts
    ($\det J_{KL} \propto 1-\alpha-\eta\beta$).

**Consequence for the hypothesis.** `hyp:hurwitz` must be stated with the parameter
condition: the reduction is valid on $\{\alpha+\eta\beta<1\}$ with the computed margin;
on the declared class the 1.9% violating subset is excluded with the worst violation
reported. This is now the supplementary's content (S5, v3).

## 4. The epsilon-scaling and frozen-A numbers

- Physical separation: macro rates $0.005$–$0.1\ \mathrm{yr}^{-1}$ vs ecological
  $r \approx 0.23$ — the physical $\varepsilon$ is not asymptotically small (formally
  the family exists; numerically the correction is $O(1)$, carried by direct
  computation, not by the asymptotic constant).
- Frozen-A: $\varepsilon_A = A_0/A^* = 1/397.87 = 2.5\times10^{-3}$;
  $\omega_A T = 0.25$–$0.39$ on one oscillation period (250–390 yr) — the
  $O(\omega_A T)$ term does not control one period, exactly as the corrected
  manuscript's scope paragraph states.
- The recorded Hopf shifts (τ₋ +3.2%, τ₊ −0.2%) are **12.7× the parameter ratio**
  $\varepsilon_A$: they are the directly computed spectral sensitivities of the
  crossings, and they are **not** implied by the trajectory bound of Proposition 1.

## 5. The "exact" decision

| Claim | Defensible? | Status |
|---|---|---|
| "Exact triangular projection" (Theorem `thm:triangle`) | **Yes — exact.** Algebraic block closure at the strict specialisation, proved. | keep as is |
| "Exact leading-order slow manifold via Tikhonov" (v18) | **No.** Leading-order with $O(\varepsilon+\omega_A T)$ corrections; finite-time only; UNH needs $\alpha+\eta\beta<1$. | already dropped in the rewrites; v18 phrasing superseded |
| "The three-state core is the frozen-A inner problem / leading-order frozen-A limit" | **Yes** (as an approximation with the Proposition-1 bound and the scope caveats). | keep as is |
| "τ₋ 3.2% higher … inside the frozen-active-pool bound" (P4 v13 line ~395) | **No** — category error (trajectory bound vs eigenvalue location) and numerically 13× the parameter ratio. | **fixed in P4 v14** |
| S5's "Hurwitz hypothesis … supported by a sweep … not proved" | **Superseded** — now proved on $\{\alpha+\eta\beta<1\}$ with the sweep-quantified margin and the 1.9% violation fraction. | **S5 updated (supplementary v3)** |

**Bottom line.** "Exact" survives only for the strict-specialisation triangular
projection. For the macro reduction the correct statement is the finite-time
conditional theorem of §2 with the now-verified H3 (on the parameter set
$\{\alpha+\eta\beta<1\}$, margin quantified); for the frozen-A step, the correct
statement is the inner-approximation bound with the $\omega_A T$ scope. The rewrites
already said all of this except the two items fixed in this pass (P4 v14 line-395
sentence; supplementary S5 status upgrade).

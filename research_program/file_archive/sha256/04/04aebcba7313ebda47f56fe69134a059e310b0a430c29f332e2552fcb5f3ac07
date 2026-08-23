# Corrected Operator I Strong Invariance and Conditional Erosion

## Status

Controlling correction to A001 Theorems 4.5/5.1 and Proposition 4.1. Immutable A001 is not edited.

## Theorem 1 — Robust strong invariance

Let `K subset R^n` be closed. Let one feedback `kappa`, independent of unmeasured disturbance, define

\[
G_\kappa(x)=\operatorname{clco}\{f(x,\kappa(x),d):d\in D(x)\}.
\]

Assume:

1. `G_kappa` has nonempty compact convex values and is locally Hausdorff-Lipschitz near `K`.
2. `G_kappa` has linear growth, or every admitted solution is otherwise forward complete.
3. For all `x in K` and `zeta in N_K^P(x)`,
   \[
   \sup_{v\in G_\kappa(x)}\langle\zeta,v\rangle\le0.
   \]
4. Every physical disturbed trajectory under `kappa` is an admitted solution of `dot x in G_kappa(x)`.

Then

\[
\exists\kappa\;\forall d(\cdot)\;\forall x(\cdot)\in\operatorname{Sol}_{\kappa,d},
\qquad x(0)\in K\Rightarrow x(t)\in K\quad\forall t\ge0.
\]

### Proof

For a solution set `rho(t)=dist(x(t),K)` and choose `p(t) in proj_K(x(t))`. Then `x-p in N_K^P(p)`. Hausdorff-Lipschitz continuity supplies `w(t) in G_kappa(p(t))` with

\[
\|\dot x(t)-w(t)\|\le L\|x(t)-p(t)\|.
\]

The Hamiltonian inequality gives `inner(x-p,w)<=0`; therefore

\[
D^+\frac12\rho^2\le L\rho^2.
\]

Since `rho(0)=0`, Gronwall gives `rho=0`. Completeness extends the conclusion to all forward time. Every actual disturbed trajectory is an envelope trajectory, so the quantifiers follow. ∎

### Implementable sufficient construction

A clean sufficient route is: `kappa` locally Lipschitz on a neighborhood of `K`; `f` jointly locally Lipschitz in `(x,u)` uniformly in `d`; and state-dependent `D(x)` Hausdorff-Lipschitz. A measurable selector alone does not establish these properties. If discontinuous feedback is used, the Hamiltonian condition must be rechecked on its actual Filippov/Krasovskii envelope.

### Correct weak/strong distinction

A viability theorem establishes existence of one safe trajectory. It cannot prove all-disturbance/all-solutions safety. A duplicate weak proof must not appear as a second theorem.

## Counterexamples retained

1. `K={0}`, `dot x=sqrt(|x|)`: `x=0` is viable while `x=t^2/4` escapes; Lipschitzness is essential.
2. Discontinuous feedback on `K=R^2\(0,infinity)^2` can cross a face at one a.e.-invisible instant.
3. For Filippov escape use switching on `x_1=x_2`, so the diagonal path remains on the switching surface and admits velocity `(1/2,1/2)`.

## Lemma 2 — Conditional tubular metric erosion

Let `K` have a two-sided tubular radius `rho>0`; signed distance is `C^{1,1}` in `|s_K|<rho`; and normals of `partial K_{-r}` correspond to normals of `partial K` for `0<r<rho`. Let nominal envelope `G` satisfy

\[
d_H(G(x),G(p))\le L_G\|x-p\|
\]

in the inner tube and

\[
\sup_{v\in G(p)}\langle n(p),v\rangle\le-\alpha<0
\]

on `partial K`. Let

\[
\widetilde G_\varepsilon(x)\subseteq G(x)+\Delta_\varepsilon B
\]

and assume the implemented inclusion has the regularity and completeness required by Theorem 1.

If

\[
L_Gr+\Delta_\varepsilon\le\alpha,
\quad 0<r<\rho,
\quad K_{-r}\ne\varnothing,
\]

then `K_{-r}` is strongly invariant.

### Proof

At `x in partial K_{-r}`, let `p in partial K` be the corresponding boundary point with common outward normal `n`. For `w in tilde G_epsilon(x)`, choose `v_x in G(x)`, error `e`, and `v_p in G(p)` so that

\[
w=v_x+e,
\quad \|e\|\le\Delta_\varepsilon,
\quad \|v_x-v_p\|\le L_Gr.
\]

Then

\[
\langle n,w\rangle\le-\alpha+L_Gr+\Delta_\varepsilon\le0.
\]

The strong-invariance theorem applied to `K_{-r}` gives the result. ∎

### Error conversion and explicit `c`

If

\[
\|\hat x-x\|\le a_o\varepsilon,
\qquad
\|u_{impl}-\kappa(\hat x)\|\le a_u\varepsilon,
\]

`kappa` has Lipschitz constant `L_kappa`, and the plant is Lipschitz in control with constant `L_u`, one may take

\[
\Delta_\varepsilon=C\varepsilon,
\qquad C=L_u(L_\kappa a_o+a_u),
\]

plus separately converted model/plant errors. For `r=c epsilon`, require

\[
(L_Gc+C)\varepsilon\le\alpha,
\qquad c\varepsilon<\rho,
\qquad K_{-c\varepsilon}\ne\varnothing.
\]

If erosion must convert estimated-state membership into actual-state safety, also require `c>=a_o`. The feasible interval may be empty.

## Why arbitrary closed sets are excluded

For

\[
K=\bigcup_{j\ge1}[2j,2j+1],
\]

choose transition widths `delta_j downarrow0`, field `+1` at each left endpoint, transition to `-1` over `delta_j`, and `-1` at each right endpoint. `K` is strongly invariant with uniform endpoint margin. For any `0<r<1/2`, choose `delta_j<r`; at the left boundary `2j+r` of the eroded component the field is `-1`, so `K_{-r}` is not invariant. A uniform tubular field-sensitivity bound is indispensable.

## Metric versus barrier erosion

`K_{-r}` and `{h>=eta}` are different unless `h` is signed distance or explicit two-sided comparison constants are proved. Neither may be substituted for the other silently.

## Routing and limits

- Paper 2 main: Theorem 1.
- Paper 2 appendix: Lemma 2 only after application constants are verified.
- Paper 1: architecture consequence only.
- Remove the arbitrary-closed-set erosion proposition.
- Hybrid resets, delays, stochastic systems, discontinuous implementation, and general measurable-selection claims remain separate obligations.

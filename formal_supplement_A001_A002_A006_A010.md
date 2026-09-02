# Formal Supplement: Restricted Viability, Information, Reduction, Network, and Audit Results

## Status and scope

This supplement restores legitimate formal material from the corrected A001, A002, A006, and A010 sources without expanding the flagship into a catalogue of proofs. Statements retain their original scope and status. Full derivations and source-specific notation remain in the corrected article files under `revised_articles/`.

No result here establishes a universal sustainability law. Each applies only to its declared state space, horizon, policy class, disturbance class, observation structure, and solution semantics.

---

# S1. Constructive viability and information-kernel ladder

## S1.1 Compact sampled full-state kernel

Let compact state, action, and disturbance sets be given, with continuous transition

\[
z_{k+1}=F(z_k,u_k,w_k)
\]

and closed safe set \(K\). Define

\[
K_0=K,
\qquad
K_{n+1}
=\{z\in K:\exists u\ \forall w,\ F(z,u,w)\in K_n\}.
\]

Then \(K_n\) is the exact \(n\)-step robust kernel. Compactness gives closed nested action-witness sets, so

\[
K_\infty=\bigcap_{n\ge0}K_n
\]

is robustly invariant under arbitrary state-feedback selection. Measurable or continuous selectors require separate theorems.

## S1.2 Finite-clopen observation kernel

For a finite clopen observation partition, exact conditioning is Hausdorff-continuous on compact information sets. A predecessor on prediction sets can therefore require one observation-dependent command whose every disturbance successor returns to the next information family. Nested compact command-witness sets yield an exact infinite-horizon knowledge kernel for the declared endpoint model.

This construction does not cover noisy overlapping fibres, continuous observations, delays, or inter-sample exit.

## S1.3 Held-control tube safety

For a fixed review period, replace endpoint containment by an exact held-control tube condition:

\[
\operatorname{Tube}(z,u,w;[0,h])\subseteq K
\]

for every disturbance, with the endpoint in the next kernel. This prevents a sampled endpoint from hiding inter-sample failure. The corresponding information kernel requires exact aggregate hidden-state tubes and a compact predecessor.

## S1.4 Compact Lipschitz RFDE history kernel

For a declared compact set of Lipschitz histories in

\[
C([ -\tau,0],\mathbb R^m),
\]

held controls, finite-clopen current observations, and a Hausdorff-continuous history solution map, predecessor iteration produces a conditional sampled RFDE knowledge kernel. The kernel lives in history space; current-value projection is not an equality of kernels.

## S1.5 Review-synchronised hybrid RFDE

A restricted hybrid RFDE theorem remains valid when resettable abstract memory is reset at fixed reviews by a continuous phase-space reset. It does not justify an interior point jump with the old continuous tail retained. A physical delayed jump requires a proper hybrid or càdlàg history space and a new continuation theorem.

## S1.6 Bounded-jump hybrid ODE with exact tubes

For a compact hybrid ODE with a fixed review clock, a finite jump budget, locally finite events, compact exact tube and endpoint maps, and Hausdorff-continuous transition branches, a robust predecessor yields a closed tube-safe kernel. Generic outer semicontinuity is insufficient: universal tube containment can fail to be closed at grazing guards without lower stability or Hausdorff continuity.

## S1.7 Compact exact information-state kernel

If an application supplies a compact Markov information process, continuous exact tube/update maps, and an arbitrary-selector policy class, the same compact predecessor argument gives a restricted information-state kernel. The theorem assumes the exact filter; it does not construct one from arbitrary noisy data.

## S1.8 Ladder limitation

The preceding objects are distinct restricted classes. They do not combine into a general variable-event, delayed, partially observed, Zeno-capable hybrid theorem. A bridge must declare phase space, reset semantics, event times, information update, nonanticipation, and predecessor closure.

---

# S2. Explicit resource–sink kernels

## S2.1 Unimodal renewable resource with sink

Let

\[
\dot S=g(S)-H,
\qquad
\dot L=w(H)-\delta(L),
\]

where \(g\) is strictly unimodal with maximum \(H_*\), \(w\) is nondecreasing, \(\delta\) increasing, and

\[
K=[S_{min},\infty)\times[0,L_{max}].
\]

Let \(H\in[H_{min},h_{max}(S)]\),

\[
S_\sharp=\inf\{S:h_{max}(S)\ge H_{min}\},
\]

and let \(L^\dagger\) solve \(\delta(L^\dagger)=w(H_{min})\). If \(0<H_{min}\le H_*\), let \(S_-<S_+\) be the roots of \(g(S)=H_{min}\). Under the declared regularity assumptions, the kernel is empty unless

\[
L^\dagger\le L_{max},
\quad
S_\sharp\le S_+,
\quad
S_{min}\le S_+.
\]

When these hold,

\[
\operatorname{Viab}(K)
=[S_\circ,\infty)\times[0,L_{max}],
\qquad
S_\circ=\max(S_{min},S_\sharp,S_-),
\]

with witness \(H\equiv H_{min}\). The result is existential, not all-control safety.

## S2.2 Constrained constant yield

Among constant-harvest equilibria, the maximum viable yield is bounded jointly by biological growth at the stock floor and sink assimilation. If the stock floor lies above the maximum-growth stock, it reduces the viable constant yield below unconstrained MSY.

## S2.3 Affine recharge

For \(g(S)=R-aS\), \(a>0\), the minimum-harvest equilibrium is

\[
S^*=(R-H_{min})/a.
\]

Under action feasibility and sink conditions, the stock kernel is

\[
[\max(S_{min},S_\sharp),\infty)
\]

when both lower bounds do not exceed \(S^*\); otherwise it is empty. The \(a=0\) case is treated separately as a constant net input.

## S2.4 Strong Allee growth

For growth negative on \((0,A)\), positive on \((A,C)\), and negative above \(C\):

- with shutdown admissible and no output floor, states below the Allee threshold are not viable when the protected floor lies below \(A\); states at or above \(A\) can remain viable under the declared sink conditions;
- with a positive output floor, no state at or below \(A\) is viable, and the lower kernel boundary is the larger of the protected floor, action-feasibility threshold, and lower root of \(g=H_{min}\).

## S2.5 Four-stock material balance

The open resource–sink model can be embedded in a closed four-stock ledger by routing extraction, products, residuals, and sink material through explicit nonnegative fluxes. The conservation identity and nonnegative invariance are separate: the first requires cancellation/left-nullspace structure; the second requires donor limitation at every boundary.

## S2.6 Pollution-suppressed growth

If \(g_L\le0\) and \(L\le L_{max}\), then

\[
g(S,L)\ge g(S,L_{max}).
\]

The ceiling-frozen growth law is pessimistic. Its invariant rectangle is an inner viable set only when the sink ceiling is also invariant. In the coupled model the exact frontier may be a curve rather than a product.

---

# S3. Coupled-patch algebra and frontier status

For cooperative two-patch diffusion,

\[
\dot S_i=g_i(S_i)-H_i+d(S_j-S_i),
\]

order-upper kernels and equilibrium tests can be developed under the source assumptions.

- A product of isolated kernels can fail the corner tangent condition when carrying capacities differ.
- Coupling can rescue a patch whose required harvest exceeds its isolated maximum growth.
- Equilibria of logistic two-patch systems reduce to a quartic polynomial after eliminating one coordinate.
- Product-set invariance is equivalent to checking the active corner tangent inequalities when the boundary drift is monotone along each face.
- A regular \(C^2\) frontier with nonzero curvature is locally non-polyhedral.
- Generic non-polyhedrality remains a conjecture; the former algebraic proof was insufficient.

The flagship contains the destruction and rescue examples. The detailed quartic, corner inequalities, and orbital-frontier calculations remain in corrected A001.

---

# S4. Cascade-network results

Let a finite directed network have failure set \(F\), edge loads \(a_{ji}\ge0\), thresholds \(\theta_i>0\), and irreversible monotone update

\[
R(F)=F\cup\{i\notin F:L_i(F)>\theta_i\}.
\]

## S4.1 Finite termination

Because every strict round adds at least one node and failures are irreversible, the cascade terminates in at most \(|V|-|F_0|\) strict rounds.

## S4.2 Redundancy containment

If each node can tolerate every subset of at most \(k\) failed in-neighbors and \(|F_0|\le k\), no new node fails.

## S4.3 Row-sum containment

With normalized matrix \(M_{ij}=a_{ji}/\theta_i\),

\[
\|M\|_\infty<1
\]

implies total possible incoming load is below threshold at every node, so no non-seed failure occurs.

## S4.4 Spectral-radius antitheorem

Spectral radius alone does not bound cascade size. A directed chain with edge weight exceeding threshold has a strictly triangular, nilpotent normalized matrix and hence \(\rho(M)=0\), yet one seed can trigger an arbitrarily long cascade.

## S4.5 Dynamic loads

If loads depend on continuous state \(x_c\), static containment does not automatically transfer. A protection set \(P\) is sufficient when physical dynamics keep \(x_c\in P\) and

\[
L_i(x_c,F_0)\le\theta_i
\qquad
\forall x_c\in P,
\quad i\notin F_0.
\]

Then no cascade guard activates while the protection-set certificate holds. Outside that set, the coupled hybrid kernel remains open.

---

# S5. Coarse-graining, local horizon, and delay stability

## S5.1 Exact logistic aggregation correction

For spatial stock \(X\) and effort \(E_s\),

\[
\mathbb E\left[rX\left(1-\frac{X}{K}\right)-qE_sX\right]
=
r\bar X\left(1-\frac{\bar X}{K}\right)
-\frac rK\operatorname{Var}(X)
-q\bar E\bar X
-q\operatorname{Cov}(E_s,X).
\]

The mean state does not obey the local logistic equation unless variance and effort–stock covariance vanish or are closed correctly.

More generally, for \(f\in C^2\) on the support interval,

\[
|\mathbb E[f(X)]-f(\mathbb E[X])|
\le
\frac12\sup|f''|\operatorname{Var}(X).
\]

These are static identities/bounds, not closed moment dynamics.

## S5.2 Local-horizon bracket

Let \(H_{loc}=(A(0)-A_{min})/v_0\), where \(v_0=-\dot A(0)>0\). If the depletion rate remains within relative error \(\epsilon<1\),

\[
(1-\epsilon)v_0
\le-\dot A(t)
\le(1+\epsilon)v_0,
\]

on an interval long enough to contain the crossing, then

\[
\frac{H_{loc}}{1+\epsilon}
\le T_A\le
\frac{H_{loc}}{1-\epsilon}.
\]

Without the rate-control assumption, a local ratio is not a forecast.

## S5.3 Halanay certificate

For

\[
\dot\xi(t)=A_0\xi(t)+A_1\xi(t-\tau),
\]

if a logarithmic norm and induced norm satisfy

\[
\mu_*(A_0)\le-\alpha_0,
\qquad
\|A_1\|_*\le\beta_0,
\qquad
\alpha_0>\beta_0\ge0,
\]

then zero is exponentially stable for every fixed \(\tau\ge0\). A decay rate solves

\[
\eta=\alpha_0-\beta_0e^{\eta\tau}.
\]

The condition is sufficient, not necessary; failure does not imply instability or Hopf bifurcation.

---

# S6. Finite-horizon stochastic viability

Define the pathwise chance kernel

\[
\operatorname{Viab}_{T,p}(K)
=
\left\{x:
\sup_\pi
\mathbb P_x^\pi(X_t\in K\ \forall t\in[0,T])
\ge p
\right\}.
\]

For a deterministic viable feedback and small-noise perturbation

\[
dX_t^\varepsilon
=f(X_t^\varepsilon)dt
+\varepsilon\Sigma(X_t^\varepsilon)dW_t,
\]

suppose deterministic trajectories from compact \(K_0\) remain at distance at least \(2\delta\) from the boundary over fixed finite \(T\), with Lipschitz drift and bounded diffusion nearby. Then

\[
\inf_{x_0\in K_0}
\mathbb P_{x_0}
(X_t^\varepsilon\in K\ \forall t\in[0,T])
\longrightarrow1
\quad
\text{as }\varepsilon\to0.
\]

This finite-horizon result does not imply positive infinite-horizon survival for a nondegenerate diffusion in a bounded domain. Horizon is load-bearing.

---

# S7. Institutional equivalence, information value, and safe learning

## S7.1 Institutional equivalence

Two institutions have the same viability kernel when they induce the same belief dynamics, effective implementable-action correspondence, allocation correspondence, actuator map, disturbance class, and policy timing. Labels or organizational forms alone do not change viability.

## S7.2 Informational recovery

Physical recovery to a physical region does not imply institutional recovery. Informational recovery requires a policy that remains inside an authorized emergency envelope until the information/institution state \((B,h)\) reaches a viable information-state kernel.

## S7.3 Safe learning

Because compatible-state updates depend on action, learning is a dual-control problem. An action is safely informative only when:

1. every compatible inter-review tube is safe; and
2. every compatible observation branch contracts a declared belief-size functional.

Uncertainty reduction without tube safety is not admissible learning.

## S7.4 Value of information

A safety-margin value of information compares aligned policy, dynamics, authority, disturbance, and initial-prior domains under two information structures. A supremal nonnegative value establishes an available safe policy only when the supremum is attained or the relevant closed viability object is used.

## S7.5 Normative monotonicity

If one specification tightens state and action constraints while state space, dynamics, information, authority, and disturbance classes remain aligned, its viability kernel cannot be larger. Comparisons without those alignments are ill typed.

---

# S8. Preserved A010 admissibility audit

The high-dimensional scaffold examined in A010 is retained as a negative model-audit example.

Verified audit results include:

- cancellation in the displayed six-state material subledger;
- possible violation of a geological/support-pool boundary without donor limitation;
- a variance coordinate whose proposed dynamics are unclosed and can violate nonnegativity;
- an undefined output quantity preventing a unique autonomous model;
- valid stage-structured equilibrium algebra under interior assumptions;
- valid effort-sensitivity coefficients within their declared gate range;
- an interior effort bound.

Historical delay-crossing and spectral values are not propositions of the unclosed scaffold. They remain status-qualified reproduction targets only. Closing the model would create a new version requiring a new verification record.

---

# S9. Source and proof map

| Supplement family | Full corrected source |
|---|---|
| Resource, capital, coupling, cascade, intergenerational, stochastic | `revised_articles/A001_viability_theory_corrected.md` |
| Typed conservation, Farkas, observation, sampled/RFDE/hybrid kernels, reduction, coarse graining, Halanay | `revised_articles/A002_general_theory_corrected.tex` |
| Institutional information state, safe learning, observer and recovery templates | `revised_articles/A006_robust_epistemic_corrected.tex` |
| Admissibility and closure audit | `uploads/paper4_perspective.txt` and its registered evaluation |
| Numerical witness appendix (S10) | `arena agent 1/other documents/audits/computational_appendix.md` (archived verbatim; block C corrected per Remark 8.3 of A001) |

This supplement and the corrected sources are alternate publication layers of one developing theoretical system. They do not create additional paper identities by file count.

# S10. Numerical witness appendix (corrected computational appendix)

**Provenance.** The ten witness blocks below are the corrected fold of the computational
appendix companion to A001 (`uploads/topdown.txt`), received 2026-09-01 from a parallel
authoring session and archived verbatim at
`arena agent 1/other documents/audits/computational_appendix.md`. On receipt, nine of the
ten blocks were independently re-derived and verified exactly; the one defective block —
the CES witness (archived block C) — carried the stated parameters σ=2, α=0.5, Y₀=10, A₀=2
while its displayed values F(5,0)=3.125, F(10,0)=6.25 require A₀=4, the parameter its
computation actually used. The correction is recorded as **Remark 8.3** of A001 (applied
2026-09-01 to both A001 copies under the owner's one-turn permission; record
`audits/computational_appendix_ces_correction.md`), and S10.3 below carries the corrected
witness. The archived appendix file is left verbatim; this section supersedes its block C.
Each block states the model it instantiates and the numbers that were computed.

## S10.1 Constrained MSY (Corollary 6.1)

Logistic growth \(g(S)=rS(1-S/C)\), \(H_*=rC/4\) at \(S_m=C/2\). The reduced formula
\(\min(H_*,H_{\mathrm{sink}})\) overstates the true constrained MSY when the floor is
above the MSY stock. Parameters: \(r=1\), \(C=10\) (so \(H_*=2.5\), \(S_m=5\)),
\(H_{\mathrm{sink}}=4\). (The article's single-instance witness uses
\(H_{\mathrm{sink}}=3\); the overstatement \(9/10\) is independent of the loose sink cap.)

| \(S_{\min}\) | \(\min(H_*,H_{\mathrm{sink}})\) | \(\min(g(S_{\min}),H_{\mathrm{sink}})\) | Verdict |
|---|---|---|---|
| 5.0 | 2.500 | 2.500 | match |
| 7.0 | 2.500 | 2.100 | overstated |
| 9.0 | 2.500 | 0.900 | overstated |

Single-instance witness used in the article: \(r=1\), \(C=10\), \(S_{\min}=8\) gives
\(g(8)=8/5=1.6<H_*=25/10=2.5\), overstatement \(9/10\).

## S10.2 Over-extraction comparison (Theorem 12.1)

Payoffs \(\pi_i(h)=a_ih-h^2\), damage \(d_i(H)=c_iH^2/2\). Interior comparison:
\(H_{\mathrm{Nash}}=\sum a/(2+\sum c)\), \(H_{\mathrm{soc}}=\sum a/(2+n\sum c)\).

| Scenario (\(n=2\)) | \(H_{\mathrm{Nash}}\) | \(H_{\mathrm{soc}}\) | strict \(>\) |
|---|---|---|---|
| symmetric \(\pi,d\) | 1.923 | 1.200 | yes |
| asymmetric benefits \(a=9,1.2\) | 2.000 | 1.500 | yes |
| one zero-damage agent | 2.250 | 1.600 | yes |
| all zero damages | 4.000 | 4.000 | no (equal) |

Witness: \(a_1=a_2=5\), \(c_1=c_2=0.8\) gives \(H_{\mathrm{Nash}}=10/3.6=2.78 >
H_{\mathrm{soc}}=10/5.2=1.92\); decoupled (\(c=0\)) gives \(H_{\mathrm{Nash}}=H_{\mathrm{soc}}=5\).

## S10.3 CES essentiality (Corollary 8.1) — corrected witness

\(F(A,R)=Y_0[\alpha(A/A_0)^{\rho}+(1-\alpha)(R/R_0)^{\rho}]^{1/\rho}\),
\(\rho=(\sigma-1)/\sigma\).

- \(F(A,0)=0\) for \(\sigma\le1\); \(F(A,0)=Y_0\alpha^{\sigma/(\sigma-1)}(A/A_0)\) for
  \(\sigma>1\).
- **Corrected witness** \(\sigma=2\), \(\alpha=0.5\), \(Y_0=10\), \(A_0=4\):
  \(F(5,0)=3.125\), \(F(10,0)=6.25\) (the displayed values of the archived block;
  they require \(A_0=4\), not the archived block's stated \(A_0=2\) — see the provenance
  note above and Remark 8.3 of A001).
- \(c_{\max}(R)=+\infty\) when \(\sigma>1\) and \(\mu_A>\delta_A\); verified that
  \(\Phi(A)\approx(\mu_A-\delta_A)A\) with ratio \(\to1\) as \(A\to\infty\)
  (e.g. at \(A=10^{15}\), ratio \(=1.000000\)).

## S10.4 Sink obstructions (Remark 6.1)

\(\delta\equiv0\) or \(\delta(K_{\max})<w(H_{\min})\) force an empty kernel. Witness:
\(K_{\max}=2\), \(H_{\min}=1\), \(w(H)=0.5H\), \(\delta(K)=0.1K\) gives
\(\delta(K_{\max})=0.2<w(H_{\min})=0.5\), \(K^\dagger=5>K_{\max}=2\).

## S10.5 Delay margin (Theorem 4.3)

\(\dot x=-ax-Bx(t-\tau)\), stable for
\(\tau<\tau_{\mathrm{crit}}=\arccos(-a/B)/\sqrt{B^2-a^2}\) when \(B>a\).

- Witness \(a=1\), \(B=2\): \(\tau_{\mathrm{crit}}=\arccos(-1/2)/\sqrt3\approx1.209\).
  Stable at \(0.4\tau_{\mathrm{crit}}\), unstable at \(1.6\tau_{\mathrm{crit}}\).
  Stable for all \(\tau\) when \(B\le a\) (e.g. \(a=1\), \(B=0.5\)).

## S10.6 Pollution-suppressed growth (Theorem 6.6)

\(g(S,K)=S(1-S/C(K))\), \(C(K)=10/(1+0.05K)\), \(w(H)=0.5H\), \(\delta(K)=0.3K\).

- The \(H_{\min}\)-control dominates coordinatewise (\(S\) higher, \(K\) lower).
- Rectangle \([S_\circ(K_{\max}),\infty)\times[0,K_{\max}]\) is invariant.
- Threshold stock \(S(K)\) needed for viability increases in \(K\):
  \(0.528,0.531,0.534\) at \(K=0,2,4\) (frontier is a strictly decreasing curve).

## S10.7 Observer safety buffer (Theorem 4.4)

On the boundary, \(L\bar e\le\eta\) preserves \(Q\); \(L\bar e>\eta\) causes exit.
Witness \(\dot x=-z+u+d\), \(u\in[0,2]\), \(d\in[-0.1,0.1]\), margin \(\eta=0.2\),
sensitivity \(L=1\): safe for \(\bar e\le0.2\), exit for \(\bar e>0.2\).

## S10.8 Hidden-mode conflict (Theorem 4.7)

\(\dot z=\theta u\), \(\theta\in\{-1,+1\}\), \(u\in\{-1,+1\}\), \(z\ge0\).
At \(z=0\): \(R((0,+1))=\{+1\}\), \(R((0,-1))=\{-1\}\), common action empty. Each
state individually in \(\mathrm{RViab}\); the joint belief \(\{(0,+1),(0,-1)\}\) is not
in \(\mathrm{ERViab}\). \(\mathrm{Viab}=\mathrm{RViab}\) (six states) but
\(K_I=\emptyset\) under constant observation — a purely epistemic contraction.

## S10.9 Jump discontinuity (Theorem 10.1)

Two-patch MSY, \(C_1=10\), \(C_2=12\), \(d=0.2\): decoupled equilibrium \((5,6)\) at
\(d=0\); no equilibrium for any \(d>0\) (so kernel empty), since \(d>0\), \(C_1\ne C_2\)
forces \(C_1=C_2\).

## S10.10 Clark under-extraction (Theorem 12.1)

Open-access stock \(S_{\mathrm{OA}}=c/(pq)\). Witness \(p=10\), \(c=5\), \(q=1\):
\(S_{\mathrm{OA}}=0.5\). A per-unit harvest tax \(t\) shifts
\(S_{\mathrm{OA}}(t)=c/((p-t)q)\): \(S_{\mathrm{OA}}(0)=0.50\), \(S_{\mathrm{OA}}(1)=0.56\),
\(S_{\mathrm{OA}}(4)=0.83\) (increasing in \(t\)).

---

# References

Aubin, J.-P. (2009). *Viability theory*. Birkhäuser.

Aubin, J.-P., Bayen, A. M., & Saint-Pierre, P. (2011). *Viability theory: New directions*. Springer.

Ethier, S. N., & Kurtz, T. G. (1986). *Markov processes: Characterization and convergence*. Wiley.

Halanay, A. (1966). *Differential equations: Stability, oscillations, time lags*. Academic Press.

Kloeden, P. E., & Platen, E. (1992). *Numerical solution of stochastic differential equations*. Springer.

Rockafellar, R. T. (1970). *Convex analysis*. Princeton University Press.

Rosen, J. B. (1965). Existence and uniqueness of equilibrium points for concave N-person games. *Econometrica, 33*(3), 520–534.

Saint-Pierre, P. (1994). Approximation of the viability kernel. *Applied Mathematics and Optimization, 29*, 187–209.
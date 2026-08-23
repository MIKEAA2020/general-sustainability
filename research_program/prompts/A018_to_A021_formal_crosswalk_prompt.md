# Self-Contained Specialist Prompt — Formal A018-to-A021 Crosswalk

## Role and decision rule

Act as a specialist in RFDEs, Banach-space semiflows, characteristic equations, Floquet theory, normally attracting invariant manifolds, and mathematical source traceability.

Everything available for this task is reproduced below. Do **not** assume access to external workspace files. Do not invent equations, parameters, spectra, couplings, or theorem clauses. If the embedded dossier does not contain a required datum, mark it `MISSING`.

Choose exactly one executive outcome:

- `COMPLETE_CROSSWALK_AND_PROMOTION_SUPPORTED`;
- `PARTIAL_CROSSWALK_ONLY`;
- `NO_A018_CANDIDATE_SUPPORTS_A021_NAIM`.

The weakest correct result is preferred.

---

# I. Embedded source dossier

## I.1 A021 abstract model

A021 considers companion blocks

\[
X^i=(N_i,A_i,Z_i,E_i)\in\mathbb R^4,
\]

selects one binding block `k`, and writes

\[
\dot x(t)=F^k(x_t)+\varepsilon f(x_t,y_t),
\qquad
\dot y(t)=G(y_t)+\varepsilon g(x_t,y_t),
\tag{A021.1}
\]

on

\[
X=C([ -\tau,0],\mathbb R^m),
\qquad
Y=C([ -\tau,0],\mathbb R^n),
\qquad
B=X\times Y,
\]

with the product supremum norm. Here `x_t(theta)=x(t+theta)` and similarly for `y_t`.

The perturbation scale is

\[
\varepsilon=C_{\rm gap}e^{-\rho\Delta_y}+\varepsilon_{\rm phys}.
\tag{A021.2}
\]

If component `k` is uniformly binding,

\[
\widetilde Y_k\le \widetilde Y_j-\Delta_yS^{\max}
\quad(j\ne k),
\]

then the off-limiting soft-minimum weights obey

\[
\pi_j\le w_{\min}^{-1}e^{-\rho\Delta_y}.
\tag{A021.3}
\]

This proves only a scalar small-coupling certificate. The original A021 source does **not** give coordinate-level formulas for the reduced multi-block residuals `f,g`, does not list the number or parameterization of slack blocks, and does not select a concrete binding equilibrium or periodic orbit.

### Current implemented A021 hierarchy

Already proved under their own hypotheses:

1. finite-time mismatch-aware tracking;
2. a forward slack tube conditional on binding confinement and local quadratic/modulus control;
3. equilibrium continuation from invertibility at zero;
4. persistence of a simple transverse characteristic crossing.

Still conditional:

1. compact Banach-semiflow NAIM persistence;
2. vertical representation over the perturbed projected base;
3. nonlinear Hopf and orbital stability.

The full history cube `C([−tau,0],K_x)` is not an admissible compact finite-dimensional NAIM for the intended path-rich state domains.

---

## I.2 A018 Candidate C3 — gated three-state core

State: `(N,Z,E)`.

\[
S(N)=rN\left(1-\frac NK\right),
\]

\[
\dot N=S(N)-qEN,
\tag{C3.1}
\]

\[
\dot Z=\frac1{\tau_m}\left[
\max\left(0,
\operatorname{softplus}_k(qEN-S(N))-\frac{\ln2}{k}+\delta
\right)-Z
\right],
\tag{C3.2}
\]

\[
\dot E=\left(1-\frac{E}{E_{\max}}\right)
\left[
\eta E\left(\frac{Z(t-\tau)}{\Delta_{\rm ref}}-
\frac{E}{E_{\max}}\right)
+\delta_0\frac{Z(t-\tau)}{Z_{\rm ref}+Z(t-\tau)}
\right].
\tag{C3.3}
\]

The delay `tau` occurs only through `Z(t−tau)` in the effort equation. `tau_m` is a memory relaxation time, not a second delay.

### Candidate-A parameters

\[
r=0.02,\quad K=100,\quad q=0.001,\quad
\eta=0.914,\quad E_{\max}=30,
\]

\[
\delta_0=0.01,\quad \Delta_{\rm ref}=1,
\quad \tau_m=5,\quad k=10,
\quad \delta=\ln2/10,
\]

and `Z_ref/delta approximately 14.43` (hence `Z_ref approximately 1` in this calibration).

The interior equilibrium is

\[
(N^*,Z^*,E^*)=(89.55188,\ln2/10,2.08962).
\tag{C3.4}
\]

### C3 linearization and characteristic equation

With `x=N−N*`, `z=Z−Z*`, and `y=E−E*`,

\[
\dot x=A_Nx+A_Ey,
\qquad
\dot z=B_Nx+B_Ey-\tau_m^{-1}z,
\qquad
\dot y=C_Ey+C_Zz(t-\tau),
\]

where

\[
A_N=r(1-2N^*/K)-qE^*,
\qquad A_E=-qN^*,
\]

\[
B_N=\frac{qE^*-S'(N^*)}{2\tau_m},
\qquad B_E=\frac{qN^*}{2\tau_m},
\]

and `C_E,C_Z` are the exact effort-law derivatives at equilibrium. The characteristic equation is

\[
\det
\begin{pmatrix}
\lambda-A_N&0&-A_E\\
-B_N&\lambda+\tau_m^{-1}&-B_E\\
0&-C_Ze^{-\lambda\tau}&\lambda-C_E
\end{pmatrix}=0.
\tag{C3.5}
\]

Writing `d=1/tau_m`,

\[
P(\lambda)=(\lambda-A_N)(\lambda+d)(\lambda-C_E),
\]

\[
L(\lambda)=B_E(\lambda-A_N)+A_EB_N,
\]

the identity is

\[
P(\lambda)=C_ZL(\lambda)e^{-\lambda\tau}.
\]

The Hopf modulus cubic in `u=omega^2` is

\[
H(u)=(u+A_N^2)(u+d^2)(u+C_E^2)
-C_Z^2\left[B_E^2u+(A_EB_N-A_NB_E)^2\right].
\tag{C3.6}
\]

For gated Candidate A, the interval-certified fundamental Hopf delays are

\[
\tau_-\in[3.6661490142739,3.6661490142743],
\]

\[
\tau_+\in[150.3584773101408,150.3584773101421].
\tag{C3.7}
\]

The periods at these crossings are approximately `249.42 yr` and `159.32 yr`. The first Lyapunov coefficients are

\[
l_1(\tau_-)=5.75\times10^{-5},
\qquad
l_1(\tau_+)=3.55\times10^{-4},
\tag{C3.8}
\]

so both gated Candidate-A crossings are subcritical under the source normalization.

### C3 periodic-orbit evidence

- A small unstable periodic orbit exists just above `tau_-`; at `tau=3.700` its collocation residual is about `10^{-7}`. Its dominant radial multiplier is greater than one and tends to one near Hopf.
- A stable large cycle exists in the lower bistable window. At `tau=5.55`, its period is about `324 yr`, `N` lies in `[68.7,94.2]`, `E<=9.2`, and the memory floor in (C3.2) never binds.
- The large cycle terminates near `tau in [5.574,5.576]`. Variational Floquet tracking gives a dominant real multiplier rising from `0.240` at `tau=4.0` to `0.964` at `tau=5.5815`. The exact crossing and a narrow gap remain unpinned.
- The small unstable branch has a separate turning region near `tau approximately 5.587`.
- At the exact fold/turning event normal hyperbolicity cannot be assumed because an additional multiplier approaches `+1`.
- The source does not provide, in this dossier, a complete infinite-dimensional Floquet spectrum and invariant history-space projections for one selected C3 orbit.

The outer `max(0,·)` in (C3.2) is nonsmooth at its switching surface. It is inactive near the interior equilibrium and on the reported large cycle at `tau=5.55`; any smooth-semiflow theorem must localize its tube away from that switching surface or use a nonsmooth theorem.

---

## I.3 A018 Candidate C4 — gated turnover-corrected four-state working core

State: `(N,A,Z,E)`, with `A=A^{act}`.

\[
R(N,A)=rN\left(1-\frac NK\right)\frac{A}{A+A_0},
\tag{C4.1}
\]

\[
B(N,A)=R(N,A)+\kappa_A N\frac{A}{A+A_0},
\tag{C4.2}
\]

\[
\dot N=R(N,A)-qEN,
\tag{C4.3}
\]

\[
\dot A=-B(N,A)+\omega_A(A^{\rm eq,W}-A),
\tag{C4.4}
\]

\[
A^{\rm eq,W}=A^{\rm eq,intrinsic}+\frac{\kappa_AK}{\omega_A}.
\tag{C4.5}
\]

The `Z` and delayed `E` equations are (C3.2)–(C3.3) with `S(N)` replaced by `R(N,A)`.

This C4 system is the large-reservoir, dynamic-target working core. Its source scope must remain explicit: its frozen-donor equilibrium requires geological support and is not a rest point of a closed geological donor equation.

### Additional Candidate-A values

\[
\omega_A=10^{-3}\ {\rm yr}^{-1},
\qquad
\kappa_A=0.05\ {\rm yr}^{-1},
\qquad
A_0=0.01K,
\]

\[
A^{\rm eq,intrinsic}=0.5K,
\qquad
A^{\rm eq,W}=5050.
\tag{C4.6}
\]

The Candidate-A frozen-donor equilibrium is

\[
(N^*,A^*,Z^*,E^*)
=(89.52562,397.8665,\ln2/10,2.08962).
\tag{C4.7}
\]

The characteristic matrix has the standard one-discrete-delay form

\[
\Delta(\lambda)=\lambda I-A_0-A_\tau e^{-\lambda\tau},
\tag{C4.8}
\]

where the exact matrices are derivatives of (C4.3)–(C4.4), (C3.2), and (C3.3) at (C4.7). The dossier does not reproduce every entry of `A_0,A_tau`; they are available only by differentiation from the equations above.

The characteristic-pinned gated C4 Hopf pair is

\[
\tau_-=3.78487\ {\rm yr}
\quad(\text{period }250.44\ {\rm yr}),
\]

\[
\tau_+=150.12175\ {\rm yr}
\quad(\text{period }159.13\ {\rm yr}),
\tag{C4.9}
\]

with reported determinant residual below `10^{-18}`.

The source-stated large-cycle fold locations are approximately

\[
\tau_{\rm term,L}^{(4)}=5.63\ {\rm yr},
\qquad
\tau_{\rm fold,R}^{(4)}=64.4\ {\rm yr}.
\tag{C4.10}
\]

These are continuation-supported event locations; their periodic-fold classification remains open in the source. The monostable interval is reported as approximately `(5.63,64.4) yr`; the equilibrium is stable there. A convenient equilibrium test point is `tau=10 yr`, but this prompt does not supply its numerical spectral abscissa or semigroup prefactor.

The dossier does not supply a complete Floquet spectrum and invariant history-space projections for one named attracting gated C4 periodic orbit. Therefore C4 cannot yet support a positive-dimensional NAIM verification.

---

## I.4 A018 Candidate C5 — five-state extension

State: `(N,A,U,Z,E)`.

\[
\dot N=R(N,A)-qEN,
\]

\[
\dot A=-B(N,A)+\omega_A(A^{\rm eq}-A)+\gamma_UU,
\]

\[
\dot U=\kappa_A N\frac{A}{A+A_0}-\gamma_UU,
\]

with the same `Z` and delayed `E` equations using the deficit `qEN-R(N,A)`.

Under the **dynamic derived target** and ideal large-reservoir closure,

\[
\omega_A(A^{\rm eq}-A)+\gamma_UU
=
\omega_A(A^{\rm eq,intrinsic}-A)+\kappa_AK,
\tag{C5.1}
\]

so `U` is a driven auxiliary and does not feed back into `(N,A,Z,E)`. This is the exact working-core projection used to justify C4.

Under a different fixed intrinsic-target closure, `U` enters `dot A` and cannot be dropped without a separate singular-perturbation argument. Do not mix these closures.

---

## I.5 A018 model/operator distinctions

Treat the following as different objects:

1. gated C3 Candidate A;
2. ungated C3 Candidate A;
3. gated/ungated Candidate B;
4. gated C4 Candidate A;
5. C5 under dynamic-target versus fixed-target closure;
6. equilibrium, small Hopf branch, stable large cycle, and fold event.

No spectrum or branch result transfers across these distinctions without proof.

---

## I.6 Concrete data absent from the dossier

The following are genuinely absent and must not be invented:

1. number and identity of A021 slack blocks;
2. parameter point of each slack block;
3. concrete product slack functional `G`;
4. coordinate-level vector-Liebig coupling residuals `f,g`;
5. coordinate-level physical coupling represented by `epsilon_phys`;
6. a uniform history neighborhood on which the yield gap and `C1` coupling bounds hold;
7. complete characteristic-root abscissae and transient semigroup prefactors for a selected equilibrium product;
8. complete Floquet spectrum, invariant history-space projections, and prefactors for a selected gated C4 periodic orbit;
9. exact theorem page/number and verbatim hypotheses from BLZ 1998.

---

## I.7 External theorem dossier

Verified bibliography:

P. W. Bates, K. Lu, and C. Zeng, *Existence and Persistence of Invariant Manifolds for Semiflows in Banach Space*, Memoirs of the American Mathematical Society, vol. 135, no. 645, 1998, DOI `10.1090/memo/0645`.

Broad verified scope: persistence of compact normally hyperbolic invariant manifolds for `C1` semiflows in Banach space under sufficiently small `C1` perturbations, with complete invariant tangent/normal splitting and normal domination. Related results on invariant stable/unstable foliations occur in the 2000 TAMS paper.

The exact theorem statement, theorem number, boundary conventions, perturbation interval, bunching formula, uniqueness class, attraction rate, and foliation/asymptotic-phase conclusion are **not embedded here**. Consequently, a response may verify bibliography and broad compatibility but must return

`THEOREM_NOT_SOURCE_MATCHED`

unless it can derive the needed result self-containedly from the time-map graph transform. Do not invent theorem numbering.

---

# II. Required analysis

## II.1 Source crosswalk

Map every A021 object to the dossier:

| A021 object | Dossier object | Status | Reason |
|---|---|---|---|

Use only:

- `EXACT_CROSSWALK`;
- `DERIVED_WITH_PROOF`;
- `ADDITIONAL_ASSUMPTION`;
- `MISSING`;
- `INCOMPATIBLE`.

At minimum cover `x,y,F^k,G,f,g`, states, parameters, delay, phase space, norm, invariant object, slack equilibrium, and perturbation topology.

## II.2 Candidate comparison

Compare C3, C4, and C5; Candidate A/B; gated/ungated; equilibrium versus periodic base. Select the strongest supportable object or return `NO_CONCRETE_NAIM_SELECTED`.

## II.3 Equilibrium option

For the C4 equilibrium at a selected stable delay such as `tau=10`, distinguish:

- existence and invertibility at zero;
- hyperbolicity;
- strict stability;
- missing numerical spectral abscissa/prefactor;
- zero-dimensional geometry.

Do not call a point a graph over a history region.

## II.4 Periodic-orbit option

A candidate periodic NAIM requires:

- one named core/operator and delay;
- branch identity;
- period and source status;
- simple phase multiplier `1`;
- every nontrivial Floquet multiplier;
- invariant projections in the history space;
- uniform normal rate and prefactor;
- distance from Hopf/fold loss of hyperbolicity;
- a smooth tube avoiding the memory-floor switching surface.

If any row is absent, return `INCOMPLETE_FLOQUET_NAIM_PACKAGE`.

## II.5 Slack and coupling

Do not define a scalar slack rate until every slack block is selected and checked. Determine whether missing `G,f,g` independently blocks concrete persistence.

## II.6 Domination

For a time-`T` map, define

\[
q_1(T)=M_sM_c e^{-(\beta-\alpha_{\rm inv})T}.
\]

For `Cr`,

\[
q_r(T)=M_sM_c^r e^{-(\beta-r\alpha_{\rm inv})T}.
\]

Evaluate numerically only if every input is in the dossier. Otherwise list missing inputs and return `DOMINATION_NOT_VERIFIED`.

## II.7 Theorem match

Use the external theorem dossier exactly as bounded above. Bibliographic verification is not a line-by-line theorem match. Return `THEOREM_NOT_SOURCE_MATCHED` unless a complete self-contained proof is supplied.

## II.8 Geometry after persistence

If an embedding persists, prove projected-base injectivity separately. A graph may be over

\[
\mathcal A_{x,\varepsilon}=\pi_x\mathcal M_\varepsilon,
\]

not over the old history cube.

## II.9 Hopf consistency

Separate:

- characteristic crossing;
- nonlinear Hopf branch;
- first Lyapunov coefficient;
- complete Floquet stability;
- fold events.

Do not transfer local or global claims between C3 and C4.

---

# III. Required outputs

Return all outputs in order.

## Output A — Executive decision

Choose one of the three decision labels. State whether C4 is selected only architecturally, as an equilibrium point, or as a verified positive-dimensional NAIM.

## Output B — Complete crosswalk table

Use exact equations and data from this dossier; do not claim lack of file access.

## Output C — Candidate comparison

Give a concise C3/C4/C5 and equilibrium/periodic decision table.

## Output D — Selected invariant object

State equations, parameters, delay, dimension, atlas/boundary, restricted dynamics, and evidence. If none, list the precise blockers.

## Output E — Binding/slack/coupling decomposition

Write `F^k` explicitly from C4 if selected. Mark `G,f,g` missing unless derivable from the dossier.

## Output F — Complete spectral/Floquet table

Do not replace a complete spectrum with selected multipliers.

## Output G — Domination calculation

Show the exact prefactor expression and whether it can be evaluated.

## Output H — Theorem matching

Distinguish bibliographic verification from exact theorem matching.

## Output I — Vertical graph and attraction status

State whether the object is a point, curve, or regional graph and exactly what attraction claim follows.

## Output J — Hopf consistency report

Preserve all model/operator distinctions.

## Output K — Minimal missing-data request

Request only genuinely absent material listed in I.6; do not request equations or parameters already embedded.

## Output L — Publication consequence

Choose:

- no source change;
- add a crosswalk remark but retain conditional status;
- promote an equilibrium-only result;
- promote a positive-dimensional theorem.

Provide LaTeX only if supported.

## Output M — Machine-readable CSV

Columns:

`item_id,claim,selected_source,status,evidence,missing_dependency,publication_action`

Include every theorem hypothesis and proposed source change.

---

# IV. Acceptance criteria

The response fails if it:

1. claims source files are inaccessible;
2. invents missing slack/coupling equations;
3. substitutes C3 data for C4;
4. mixes Candidate A/B or gated/ungated results;
5. treats a selected Floquet multiplier as the full spectrum;
6. selects a Hopf or fold point as a normally hyperbolic periodic base;
7. ignores the memory-floor smoothness issue;
8. claims numerical domination without every prefactor;
9. invents BLZ theorem numbers or conclusions;
10. describes a point or closed curve as a graph over a history region.

The expected answer may still be `PARTIAL_CROSSWALK_ONLY`. Self-containment means the decision must follow from the dossier above, not that missing scientific data may be guessed.
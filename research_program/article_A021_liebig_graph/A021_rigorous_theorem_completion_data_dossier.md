# Self-Contained Data Dossier for Completing the Rigorous A021 Periodic-NAIM Theorem

## 0. Purpose and exact status

This dossier contains the model, parameter choices, selected invariant object, numerical orbit/Floquet/slack data, finite and tail operator bounds, and exact remaining validation outputs needed to complete a rigorous theorem.

Current status:

- a concrete uncoupled two-block product is fully specified;
- the binding periodic orbit is reproduced and solved to high finite-collocation accuracy;
- binding/slack finite-discretization product bunching is verified numerically;
- the finite/structured/tail inverse architecture closes numerically;
- interval validation of the periodic orbit, continuum Floquet projections, continuum product norm, and perturbation class remains incomplete;
- no theorem promotion is currently authorized.

The dossier supports two possible final theorems:

1. **Generic perturbation theorem:** persistence for any explicitly declared `C1`-small perturbation of the concrete two-block product.
2. **A021 vector-Liebig theorem:** requires the additional source-derived coordinate functionals `G,f,g` and a uniform yield-gap tube. Those functions are not present in the source record and must not be invented.

---

# 1. Phase space and concrete uncoupled product

Use the common maximal history space

\[
B=C([-10,0],\mathbb R^4)\times C([-10,0],\mathbb R^4)
\]

with product supremum norm. Write `z=(x,y)`.

- Binding functional evaluates its delayed memory coordinate at `-4.5`.
- Slack functional evaluates its delayed memory coordinate at `-10`.

At zero coupling,

\[
\dot x(t)=F_{4.5}(x_t),
\qquad
\dot y(t)=F_{10}(y_t).
\]

The product semiflow is denoted `Phi_0^t`.

---

# 2. Gated Candidate-A C4 vector field

For present state `(N,A,Z,E)` and delayed memory `W=Z(t-tau)`, define

\[
R(N,A)
=rN\left(1-\frac NK\right)\frac{A}{A+A_0},
\]

\[
B(N,A)
=R(N,A)+\kappa_A N\frac{A}{A+A_0},
\]

\[
d(N,A,E)=qEN-R(N,A),
\]

\[
\operatorname{sp}_k(d)=\frac1k\log(1+e^{kd}).
\]

The equations are

\[
\dot N=R(N,A)-qEN,
\]

\[
\dot A=-B(N,A)+\omega_A(A^{\rm eq,W}-A),
\]

\[
\dot Z=\tau_m^{-1}
\left[
\max\left(0,
\operatorname{sp}_k(d)-\frac{\ln2}{k}+\delta
\right)-Z
\right],
\]

\[
\dot E=
\left(1-\frac{E}{E_{\max}}\right)
\left[
\eta E\left(\frac{W}{\Delta_{\rm ref}}-rac{E}{E_{\max}}\right)
+
\delta_0\frac{W}{Z_{\rm ref}+W}
\right].
\]

Candidate-A parameters:

\[
r=0.02,
\quad K=100,
\quad q=0.001,
\quad \eta=0.914,
\quad E_{\max}=30,
\]

\[
\delta_0=0.01,
\quad \Delta_{\rm ref}=1,
\quad \tau_m=5,
\quad k=10,
\quad \delta=\frac{\ln2}{10},
\quad Z_{\rm ref}=1,
\]

\[
\omega_A=10^{-3},
\quad \kappa_A=0.05,
\quad A_0=1,
\quad A^{\rm eq,intrinsic}=50,
\]

\[
A^{\rm eq,W}
=A^{\rm eq,intrinsic}+\frac{\kappa_AK}{\omega_A}
=5050.
\]

Because `delta=ln(2)/k`, the argument of the outer maximum is exactly `sp_k(d)`, which is strictly positive for every finite real `d`. Hence the maximum is inactive on every bounded real state box. The source equation must retain the maximum, but the smooth branch is exact on the validation box.

---

# 3. Selected unperturbed invariant object

## 3.1 Binding orbit

- Core: gated Candidate-A C4.
- Delay: `tau_x=4.5 yr`.
- Branch: lower-window large-cycle candidate, away from the lower Hopf (`3.78487`) and lower continuation event (about `5.63`).
- History orbit:

\[
\Gamma_x=\{\gamma_t:t\in\mathbb R\}
\subset C([-10,0],\mathbb R^4),
\]

where histories include unused values before `-4.5` through the common embedding.

Phase-corrected period seed:

\[
P=370.9311778394~\mathrm{yr}.
\]

Numerical state ranges:

\[
N\in[45.69208,94.87305],
\]

\[
A\in[834.58311,943.05308],
\]

\[
Z\in[0.001534,0.678093],
\]

\[
E\in[0.354363,20.082770].
\]

Minimum full floor argument on the seed:

\[
1.4755423\times10^{-3}.
\]

## 3.2 Slack equilibrium

Use an identical gated Candidate-A C4 block with delay

\[
\tau_y=10~\mathrm{yr}
\]

at the constant equilibrium

\[
y_*=(89.52562,397.8665,\ln2/10,2.08962).
\]

## 3.3 Product manifold

\[
\mathcal M_0
=
\Gamma_x\times\{\widehat y_*\}
\subset B.
\]

The desired object is a compact one-dimensional closed curve, not a graph over an open history region.

---

# 4. Binding periodic-orbit numerical passport

A fixed-step method-of-steps RK4 reproduction used:

- `dt=0.05 yr` for the fine orbit;
- horizon `50000 yr`;
- phase at a subgrid-corrected maximum of `N`.

A 1025-mode seed (512 positive, 512 negative, and zero mode) was archived. A finite K=80 phase-fixed Fourier Newton system has 645 unknowns.

Corrected finite Fourier data:

\[
P_{80}=370.9311778394287~\mathrm{yr},
\]

\[
\|F_{80}\|_{\rm nodes,\infty}
=1.54\times10^{-10},
\]

\[
\|F_{80}\|_{\rm offgrid,\infty}
<7.87\times10^{-9}.
\]

At K=100:

\[
\|F_{100}\|_{\rm offgrid,\infty}
=2.67\times10^{-10}.
\]

At K=120:

\[
\|F_{120}\|_{\rm offgrid,\infty}
=2.82\times10^{-12}.
\]

At K=160–240 the off-grid residual stays near `2.4e-12` to `3.1e-12`.

Finite inverse diagnostics at K=80:

\[
\|J_{80}^{-1}\|_\infty=1847.8638,
\]

\[
\kappa_\infty(J_{80})=1.02\times10^7,
\]

\[
\|J_{80}^{-1}F_{80}\|_\infty
=1.2941\times10^{-11},
\]

\[
\|I-J_{80}^{-1}J_{80}\|_\infty
\le2.4364\times10^{-7}
\]

including the stored IEEE matrix-product rounding allowance.

Outward interval vector-field bounds on the broad orbit box:

\[
\|F\|_\infty\le13.30145,
\]

\[
\|DF\|_\infty\le20.72046,
\]

\[
\|D^2F\|_{\infty,\rm bilinear}
\le1.91308.
\]

A conservative finite-collocation Jacobian-Lipschitz target is

\[
L_{\rm coll}\le2000.
\]

The finite numerical Kantorovich quantity is below

\[
4.8\times10^{-5}.
\]

These are finite-block data, not a continuum radii theorem.

---

# 5. Binding Floquet data

Full finite-history monodromy matrices were computed:

| `dt` | dimension | phase multiplier | leading nontrivial multiplier |
|---:|---:|---:|---:|
| 0.25 | 76 | 0.98687854 | 0.68774849 |
| 0.10 | 184 | 0.99774865 | 0.68770289 |
| 0.05 | 364 | 1.00136091 | 0.68768669 |

Empirical extrapolation:

\[
\mu_s\approx0.68767164,
\]

with empirical discretization envelope

\[
\mu_s\in[0.68763924,0.68770405].
\]

Numerical leading normal exponent:

\[
\beta_x\approx1.0094\times10^{-3}~\mathrm{yr}^{-1}.
\]

Phase-tangent history norm ratio:

\[
M_c\approx4.55356.
\]

Finite-discrete phase projection norms are large (about 170 in the induced infinity norm at the finest retained history grid), demonstrating nonnormality.

These data do not prove algebraic simplicity or the full continuum Floquet spectrum.

---

# 6. Slack equilibrium data

At `tau_y=10`, the exact characteristic matrix is

\[
\Delta_y(\lambda)
=\lambda I-J-De^{-10\lambda},
\]

with

\[
J=
\begin{pmatrix}
-0.0178602301&1.1788283\!\times10^{-6}&0&-0.08952562\\
-0.0341040347&-0.0010293148&0&0\\
0.0017860199&-1.1788262\!\times10^{-7}&-0.2&0.0089525463\\
0&0&0&-0.0595178317
\end{pmatrix},
\]

and the only nonzero delayed entry

\[
D_{4,3}=1.7850160431.
\]

Refined rightmost roots:

\[
\lambda_{1,2}
=-0.00052673009564114
\pm0.0220846350193287i,
\]

with determinant residual below `3e-21`. The next root is

\[
\lambda_3=-0.00103151651411957.
\]

Analytic exterior exclusion plus 70-digit winding counts give:

| half-plane | root count |
|---|---:|
| `Re lambda>=0` | 0 |
| `Re lambda>=-0.0005` | 0 |
| `Re lambda>=-0.0006` | 2 |
| `Re lambda>=-0.0010` | 2 |
| `Re lambda>=-0.0011` | 3 |

This is high-confidence numerical certification, not outward-rounded interval proof.

Provisional slack decay:

\[
\beta_y=0.00052673009564114~\mathrm{yr}^{-1}.
\]

---

# 7. Product operator norms and discrete bunching

Binding stable-complement and slack semigroup induced infinity norms were computed directly. Inverse-resolution extrapolation of the slack norms gives:

| binding periods | slack norm | `M_c` product |
|---:|---:|---:|
| 30 | 0.20898 | 0.95160 |
| 35 | 0.07414 | 0.33761 |
| 40 | 0.02557 | 0.11643 |

Thus finite-discrete product bunching is marginal at 30 periods and robust at 35–40 periods.

The manuscript may report these only as finite-discretization operator-norm evidence.

---

# 8. Fourier/collocation validation data

## 8.1 Seed and weight

- Initial archive: 512 positive/negative modes.
- Signal-dominated coefficient decay through about mode 70.
- Numerical noise begins around modes 80–120.
- First interval/collocation choice: K=80.
- Revised initial weighted-space diagnostic: `nu=1.01`.

## 8.2 Finite Fourier Newton convergence

| K | dimension | period | inverse infinity norm | off-grid residual |
|---:|---:|---:|---:|---:|
| 40 | 325 | 370.9311774696 | 1847.8333 | `2.71e-5` |
| 60 | 485 | 370.9311778385 | 1847.8959 | `8.04e-7` |
| 80 | 645 | 370.9311778395 | 1847.8638 | `7.85e-9` |
| 100 | 805 | 370.9311778396 | 1847.7928 | `2.67e-10` |
| 120 | 965 | 370.9311778396 | 1847.7290 | `2.82e-12` |
| 160 | 1285 | 370.9311778394 | 1847.7110 | `2.35e-12` |
| 200 | 1605 | 370.9311778394 | not formed | `2.81e-12` |
| 240 | 1925 | 370.9311778394 | not formed | `3.07e-12` |

## 8.3 Low-mode inverse-transfer defects

| transfer | preconditioned defect |
|---|---:|
| 40→60 | 1.75747 |
| 60→80 | 0.016480 |
| 80→100 | 0.012943 |
| 100→120 | 0.005936 |
| 120→160 | `4.577e-5` |
| 160→200 | `3.118e-5` |
| 200→240 | `2.182e-5` |

Empirical unresolved transfer tail beyond K=240: conservative numerical allowance `1e-4`.

## 8.4 Structured K240→K600 transfer

\[
\left\|J_{240}^{-1}
(J_{240}-R J_{600}E)
\right\|_\infty
=1.5950\times10^{-6}.
\]

## 8.5 High-mode contraction

Subdivided outward interval bounds on the tight orbit box give

\[
\|L(t)\|_\infty\le7.60895.
\]

In periodic L2/Sobolev norms,

\[
\eta_K
\le
\frac{P\,7.60895}{2\pi(K+1)}.
\]

At K=600,

\[
\eta_{600}\le0.7475<1.
\]

## 8.6 Block-Neumann precursor

Numerical sixth-derivative coefficient bound:

\[
\|L^{(6)}\|_\infty
\approx9.214\times10^{-5}.
\]

Factor-two target:

\[
1.843\times10^{-4}<2.0\times10^{-4}.
\]

The sixth-derivative tail gives approximate cross blocks

\[
b_{LT}\approx0.286,
\qquad
b_{TL}\approx4.1\times10^{-8}.
\]

Together with finite defect `1.595e-6` and tail factor `0.7475`, the numerical block row bound is

\[
<0.748<1.
\]

Orbit-ball sensitivity at radius `2e-5` changes the sixth-derivative bound by at most `1.264e-8` in 88 numerical directions. A rigorous all-direction interval sensitivity bound remains open.

---

# 9. Exact remaining proof data

## 9.1 Periodic orbit CAP

Must produce outward-rounded:

- a unique phase-fixed periodic orbit ball;
- period interval `[P_-,P_+]`;
- residual/preconditioner bounds `Y,Z0,Z1,Z2`;
- ball radius `r_orb`;
- true-orbit floor margin;
- interpolation/tail theorem in the selected function norm.

## 9.2 Continuum Floquet CAP

Must prove:

- multiplier `1` algebraically simple;
- every other multiplier in `|mu|<=mu_*<1`;
- validated Riesz projections;
- continuum normal prefactors/rates.

## 9.3 Slack CAP

Must replace high-precision winding counts by outward interval argument-principle/interval-Newton proof and validate the semigroup norm at `40P`.

## 9.4 Continuum product bunching

Must establish

\[
q_{40}^{\rm cont}
=
\|D\Phi_0^{40P}|_{E^s}\|
\left\|(D\Phi_0^{40P}|_{T\mathcal M_0})^{-1}\right\|
<\frac14.
\]

## 9.5 Coupling choice

Choose and document one:

### Generic perturbation theorem

\[
\dot z=H_0(z_t)+R_\varepsilon(z_t),
\qquad
\|R_\varepsilon\|_{C^1(\mathcal U)}
\le C|\varepsilon|.
\]

### Original A021 vector-Liebig theorem

Supply the exact block list, `G`, coordinate-level `f,g`, physical coupling, and a uniform yield-gap neighborhood. These data are currently absent.

## 9.6 Persistence proof

Supply either:

- exact source-opened BLZ theorem and every matched row; or
- complete time-map graph transform, derivative fiber contraction, sampled-to-semiflow promotion, projected-curve embedding, and in-tube attraction.

---

# 10. Target theorem statement after validation

Let the concrete two-block product above generate a `C1` semiflow on a tube around

\[
\mathcal M_0
=\Gamma_x\times\{\widehat y_*\}.
\]

Assume the validated data prove:

1. `M0` is a compact `C1` normally attracting invariant curve;
2. the full normal splitting and `q40<1/4`;
3. `C1` perturbation closeness on the tube for time `40P`.

Then a matched theorem or complete graph transform yields a nearby locally positively invariant `C1` curve `M_epsilon`. A vertical representation exists only after the binding projection is proved to be a global embedding, and its domain is the perturbed projected closed curve.

The theorem is not established until every validation gate above is closed.

---

# 11. Required deliverables from the next solver

Return:

1. `CAP-ORB`: interval radii-polynomial table and orbit/period enclosure;
2. `CAP-FLOQ`: multiplier disks, tail radius, and projection norms;
3. `CAP-SLACK`: interval root count and semigroup norm;
4. `CAP-BUNCH`: complete continuum `q40` inequality;
5. `MODEL`: declared perturbation class or exact A021 `G,f,g`;
6. `THEOREM`: exact theorem match or complete proof;
7. `STATUS`: precise publication consequence.

No new equations, spectra, or constants may be invented.

---

# 12. Raw Fourier coefficient deliverables

The floating-point Newton coefficient vectors are exported directly as CSV files; no workspace-specific binary reader is required:

| truncation | coefficient rows | file | SHA-256 |
|---:|---:|---|---|
| K=80 | 644 | `computations/c4_fourier_coefficients_K80.csv` | `9ee11550ec447ed5638e57a232161d61e7bdca7eea8429e640a207eb69f4977d` |
| K=120 | 964 | `computations/c4_fourier_coefficients_K120.csv` | `f6273d99f2eefcd21a0b843da0783ca26eec537e164962d54f0c8d5f29d5b783` |
| K=240 | 1924 | `computations/c4_fourier_coefficients_K240.csv` | `7f730b92bb4345b923152aa37d39cc1b02a17297085ca08e54a9cefaccd1c5aa` |

Each row contains:

- truncation K and period;
- signed Fourier mode;
- state name;
- real and imaginary coefficient;
- one-ULP outward IEEE-754 hull for each component.

Convention:

\[
u(\theta_j)=\sum_k a_k e^{2\pi i k j/n}.
\]

The one-ULP hull encloses storage rounding only. It is not a validated orbit enclosure. The manifest is `computations/c4_fourier_coefficients_manifest.json`, and the exporter is `computations/export_c4_fourier_coefficients.py`.

# 13. Reproducibility paths

Primary scripts and summaries are under

`research_program/article_A021_liebig_graph/computations/`.

Key compact artifacts:

- `c4_tau4p5_cap_seed.npz/json`;
- `c4_fourier_K80_newton.npz/json`;
- `c4_fourier_K*_operator.npz`;
- `c4_fourier_operator_consistency_convergence.json`;
- `c4_fourier_structured_transfer_K240_K600.json`;
- `c4_tight_jacobian_interval.json`;
- `c4_linearization_fourier_decay.json`;
- `c4_sixth_derivative_coefficient_sum.json`;
- `c4_slack_tau10_argument_count.json`;
- `c4_slack_semigroup_convergence_extrapolation.json`.

Large raw trajectories/matrices are content-addressed in `research_program/file_archive/sha256/` with hashes recorded in `research_program/file_manifest.csv`.

---

# 14. Final status box

```text
CONCRETE_UNCOUPLED_PRODUCT:          SPECIFIED
BINDING_PERIODIC_SEED:               HIGH_ACCURACY_NUMERICAL
FINITE_FLOQUET:                      CONVERGED_NUMERICALLY
SLACK_RIGHTMOST_ROOT:                HIGH_CONFIDENCE_NUMERICAL_COUNT
FINITE_PRODUCT_BUNCHING:             VERIFIED_NUMERICALLY
FINITE_FOURIER_NEWTON:               SOLVED_HIGH_ACCURACY
FINITE_INTERVAL_DERIVATIVES:         CLOSED
STRUCTURED_K600_TRANSFER:             DEFECT_1.595E-6
HIGH_MODE_SOBOLEV_TAIL:              FACTOR_0.7475
BLOCK_NEUMANN_PRECURSOR:             <0.748 NUMERICAL
PERIODIC_ORBIT_INTERVAL_PROOF:       PENDING
CONTINUUM_FLOQUET_PROOF:             PENDING
CONTINUUM_PRODUCT_DOMINATION:        PENDING
SOURCE_DERIVED_A021_COUPLING:         MISSING
EXACT_PERSISTENCE_THEOREM/PROOF:     PENDING
MANUSCRIPT_NAIM_PROMOTION:           BLOCKED
```
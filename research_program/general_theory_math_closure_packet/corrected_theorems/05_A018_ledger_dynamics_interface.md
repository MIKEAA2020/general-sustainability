# A018 Ledger-to-Dynamics Interface Contract

## Decision

**The Paper 3/Paper 4 cut is viable, but not because the closed primitive ledger dynamically reduces to the working C3/C4 systems.** The natural seam is an exact **diagnostic specialization plus an explicit non-reduction boundary**:

- Paper 3 owns closed material accounting, donor limitation, conservation/positivity, and componentwise diagnostics.
- Paper 4 owns named open/frozen-donor C3/C4 RFDE models and their bifurcation results.
- The exact shared object is the single-resource deficit/readout identity, not a shared closed vector field.

This closes the publication-partition question while preserving the scientific fact that the primitive finite-donor field and the working C4 field are different completions.

## Source and version identities

| Internal model ID | Source of record | SHA-256/status | Role |
|---|---|---|---|
| `LEDGER-PRIM-CLOSED-v1` | `uploads/paper_II_closed_ledger.txt` (A019) | `0f3dabd48ff6a4c3197c669b4fe955b5ff1933dacda95d06d720c70b74f37764`; analytical core verified and corrected | Closed donor-limited ledger specialization |
| `A018-CANONICAL-WORKING` | `uploads/manuscript.txt` (A018) | `756b331f3ff99fe9db239d9a6f6cc6d3a3df92e3ed4bcaf007bc52486177e46e`; corrected working source exists | Source for specialized C3/C4 definitions and source-stated results |
| `DYN-C3-GATED` | A018 named gated three-state core | local model; source equations and parameter table control | Paper 4 three-state dynamics |
| `DYN-C4-WORKING` | A018 turnover-corrected four-state working core | dynamic derived-target/ideal large-reservoir closure | Paper 4 four-state working dynamics |
| `DYN-C4-QSS` | A018 fixed-intrinsic-target detritus-QSS core | distinct low-`A` singular-limit object | Comparison only; never merge with working C4 |
| `SRC-A018-V18` | `uploads/manuscript_v18_dehedged.txt` | supplemental, not canonical pending full version audit | No substitution into this contract |

## Producer object: Paper 3 ledger

### Primitive natural block

Let

\[
x_L=(N,A^{act},A^{geo},U)
\]

with

\[
s=\frac{A^{act}}{A^{act}+A_0},\qquad
\sigma=\frac{A^{geo}}{A^{geo}+A_{g0}},
\]

\[
R=rN(1-N/K)s,\quad T=\kappa_A Ns,\quad B=R+T,
\]

and donor-limited transfers

\[
e_{GA}=\omega_A[A^{eq,intrinsic}]_+\sigma,
\qquad e_{AG}=\omega_AA^{act}.
\]

Under the registered institutional-failure specialization and no optional mining,

\[
\begin{aligned}
\dot N&=R-qEN,\\
\dot A^{act}&=-B+e_{GA}-e_{AG}+\gamma_UU,\\
\dot A^{geo}&=-e_{GA}+e_{AG},\\
\dot U&=T-\gamma_UU.
\end{aligned}
\]

The producer exports:

1. typed state `x_L` and nonnegative domain;
2. named fluxes `R,T,B,e_GA,e_AG,qEN` with source units;
3. natural-block identity
   \[
   \frac d{dt}(N+A^{act}+A^{geo}+U)=-qEN;
   \]
4. full-ledger conservation after product/waste/inert routing is restored;
5. orthant-invariance conditions;
6. componentwise diagnostic readout;
7. the no-positive-effort-rest and extraction-integrability limitations.

## Consumer object: Paper 4 dynamics

Paper 4 defines its models locally rather than importing a hidden vector field.

### Three-state core

`DYN-C3-GATED` has phase state `(N_t,Z_t,E_t)` and stock equation

\[
\dot N=rN(1-N/K)-qEN,
\]

with the registered memory equation and gated delayed effort law. It is a single-resource, frozen-active-pool modelling choice.

### Four-state working core

`DYN-C4-WORKING` has phase state `(N_t,A_t,Z_t,E_t)` and stock equation

\[
\dot N=R(N,A)-qEN.
\]

Its active-pool equation uses the turnover-corrected working target

\[
A^{eq,W}=A^{eq,intrinsic}+\kappa_AK/\omega_A
\]

under the ideal large-reservoir/dynamic-derived-target closure. Its reported four-state Hopf/Floquet/fold evidence belongs only to this version.

## Exact interface map

Define the specialization contract

\[
\mathcal S_{1R}:\quad
\text{single resource},\ S=R,\ \chi=1,\ \mu=\nu=\rho=0,
\ C^A=0,
\]

with the local stock equation `dot N=R-qEN`. Then for every trajectory of either the specialized ledger or the named C3/C4 core,

\[
D(t):=qE(t)N(t)-R(N(t),A(t))=-\dot N(t),
\]

and

\[
\Lambda(t):=[D(t)]_+=[-\dot N(t)]_+.
\]

For C3, use the declared frozen-active-pool constitutive limit `R(N,A)→rN(1-N/K)` on its stated finite-time/local scope.

**Mapping type:** `EXACT_SPECIALIZATION` for the deficit identity once the local stock equation and `𝒮_1R` are imposed. The C3 constitutive replacement is separately `APPROXIMATION` and carries its finite-time error/status.

## Explicitly rejected dynamic mapping

There is no exact mapping

\[
LEDGER\text{-}PRIM\text{-}CLOSED\text{-}v1
\longrightarrow DYN\text{-}C4\text{-}WORKING
\]

as a projectable reduction or regular perturbation.

Reasons:

1. The primitive ledger uses the intrinsic donor-limited target; the working C4 uses a derived target.
2. At the working equilibrium the two `A^{act}` vector fields differ by an `O(1)` term.
3. The working point requires continuing geological support and is not a rest point of the closed finite-donor system.
4. The cumulative donor-draw quantity is not a trajectory-tracking error between these fields.
5. The closed primitive system makes sustained extraction integrable and therefore cannot possess the working positive-flux rest indefinitely.

**Mapping type:** `REJECTED_MAPPING` for exact dynamic reduction.  
**Permitted relation:** `ANALOGY_ONLY` for shared mechanism language, plus diagnostic reconstruction of omitted mass flows.

## Open-projection accounting for Paper 4

The working core is an open projection. Paper 4 must state that:

- omitted turnover is routed to a diagnostic detritus/inert sink;
- imposed recharge corresponds to geological draw;
- the reduced `(N,A,Z,E)` trajectory is not mass-closed by itself;
- its mass discrepancy is reconstructible from the omitted donor/turnover flows;
- global periodic results are model-version-specific and do not transfer to the closed primitive ledger.

This disclosure is part of the local Minimal Working Realization, not an optional citation to Paper 3.

## Publication interface allocation

| Item | Paper 3 | Paper 4 |
|---|---|---|
| Primitive ledger equations and full routing | Full statement/proof | One-paragraph boundary statement and citation |
| Conservation and positivity | Full proof | Local positivity needed for its model; no claim of closed mass conservation |
| Componentwise deficits/depletion horizons | Full definitions and interpretation | Restate only `D=qEN-R` and `Lambda=[D]_+` |
| C3/C4 RFDE equations | Context only | Full local equations, phase space, histories, parameters |
| Hopf/Floquet/fold results | No | Full result/status/artifacts |
| Closed-donor no-rest/integrability | Full theorem | State as limitation preventing transfer to primitive closed system |
| Model-version table | Ledger versions | C3/C4 versions; shared registry citation |

## Refereeability test

- **Paper 3 is independent:** none of its conservation, positivity, no-rest, or diagnostic claims requires Paper 4's bifurcation results.
- **Paper 4 is independent:** it contains the full named RFDEs, phase spaces, parameter/version identifiers, local positivity, characteristic results, and computational artifacts. It does not cite Paper 3 for existence or validity of its main dynamics.
- **No circular edge:** the exact deficit identity may be proved in one line in both papers without substantive duplication.

## Remaining obligations

1. Attach exact equation labels and parameter-file hashes when the two publication drafts are instantiated.
2. Complete the full `SRC-A018-V18` version audit before substituting it for `A018-CANONICAL-WORKING`.
3. Keep `DYN-C4-WORKING` and `DYN-C4-QSS` outputs separate.
4. Archive Paper 4's branch, Floquet, history, solver, and environment artifacts.
5. Do not use this seam to promote A021 coupling or periodic-NAIM claims.

## Final seam verdict

**Natural seam found and accepted:** accounting/diagnostics versus named nonlinear dynamics, connected by an exact diagnostic specialization and an explicit non-reduction contract. The Paper 3/Paper 4 split is reproducible and noncircular if this contract is enforced.
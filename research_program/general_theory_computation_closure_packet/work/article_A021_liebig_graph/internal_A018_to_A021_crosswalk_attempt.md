# Internal Attempt — Formal A018-to-A021 Crosswalk

## Output A — Executive decision

**Decision: `PARTIAL_CROSSWALK_ONLY`.**

The best architectural candidate for A021 is the **gated Candidate-A four-state working core** `(N,A,Z,E)` from corrected A018 because its state dimension and variable names coincide with A021's declared block `X^i=(N_i,A_i,Z_i,E_i)`. Its equations, principal parameters, equilibrium, delay placement, and local characteristic data are available.

A complete A021 NAIM promotion is not supported because A021 never specifies:

1. which A018 core and parameter point is the binding copy;
2. which blocks are slack and at what parameter points;
3. the concrete vector-Liebig coupling functionals `f,g` in the reduced RFDE;
4. a selected positive-dimensional compact invariant object with complete Floquet spectrum and history-space projections;
5. all normal prefactors/rates needed for bunching;
6. an exact source-opened persistence theorem match.

A concrete **equilibrium point** can be nominated from A018, but it is a zero-dimensional object already covered by equilibrium continuation. It does not establish A021's intended graph over a region of binding histories. A periodic-orbit template is available, but no selected orbit has the complete Floquet/projection package needed for the A021 theorem.

---

## Output B — Source-identity crosswalk

| A021 symbol/object | Selected A018 object | Source | Transformation/specialization | Status |
|---|---|---|---|---|
| `x` | `(N,A^{act},Z,E)` | A018, `eq:four-state-working` plus `eq:Z-core`–`eq:effort-core` | Rename `A^{act}` as `A` | `EXACT_CROSSWALK` after a formal selection decision |
| `F^k` | Gated Candidate-A four-state working vector field | A018, Definition `def:working-four`, `eq:four-state-working`, `eq:Z-core`, `eq:effort-core` | Large-reservoir dynamic-target working core | `EXACT_CROSSWALK` candidate, not selected by A021 |
| binding phase space | `C([−tau,0],R^4)` | A018 fixed-delay DDE; A021 abstract phase space | Four-state histories | `DERIVED_WITH_PROOF` |
| binding delay | institutional delay `tau` only through `Z(t−tau)` in effort | A018, `eq:effort-core` | `tau_m` remains an ODE relaxation time, not a second delay | `EXACT_CROSSWALK` |
| binding parameter point | Candidate A | A018 Table `tab:params`, equilibrium and methods appendices | See Output D | `ADDITIONAL_ASSUMPTION`: A021 never selects Candidate A |
| `y` | product of all nonbinding companion blocks | A021 abstract split | No actual number/types/parameters of copies supplied | `MISSING_FROM_SOURCE` |
| `G` | product of nonbinding A018 vector fields | Would require block list and parameter map | Cannot infer all slack copies are identical | `MISSING_FROM_SOURCE` |
| `f,g` | perturbations induced by vector soft-minimum plus physical coupling | A021 prose only | No reduced-core formula connects the soft-minimum to each `(N,A,Z,E)` equation | `MISSING_FROM_SOURCE` |
| `epsilon` | `C_gap exp(−rho Delta_y)+epsilon_phys` | A021 | Soft-minimum derivative estimate accepted | `EXACT_CROSSWALK` as a scale, not as a `C1` norm bound |
| `A_x` | equilibrium point or one named periodic history orbit | A018 local/global objects | Must choose one object and one delay | `ADDITIONAL_ASSUMPTION` |
| slack equilibrium | product `hat y_*` | A021 abstract | No named block equilibria or complete spectra | `MISSING_FROM_SOURCE` |
| compact NAIM theorem | BLZ Banach-semiflow persistence | A021 conditional template | Exact theorem/page not source-opened in this attempt | `MISSING_FROM_SOURCE` for promotion |

### Exact selected candidate vector field

For the Candidate-A four-state working core,

\[
R(N,A)=rN\left(1-\frac NK\right)\frac{A}{A+A_0},
\]

\[
B(N,A)=R(N,A)+\kappa_A N\frac{A}{A+A_0},
\]

\[
\dot N=R(N,A)-qEN,
\]

\[
\dot A=-B(N,A)+\omega_A(A^{\mathrm{eq,W}}-A),
\qquad
A^{\mathrm{eq,W}}=A^{\mathrm{eq,intrinsic}}+\frac{\kappa_AK}{\omega_A},
\]

\[
\dot Z=\frac1{\tau_m}\left[
\max\left(0,
\operatorname{softplus}_k(qEN-R(N,A))-\frac{\ln2}{k}+\delta
\right)-Z
\right],
\]

\[
\dot E=\left(1-\frac{E}{E_{\max}}\right)
\left[
\eta E\left(\frac{Z(t-\tau)}{\Delta_{\mathrm{ref}}}-\frac{E}{E_{\max}}\right)
+\delta_0\frac{Z(t-\tau)}{Z_{\mathrm{ref}}+Z(t-\tau)}
\right].
\]

This is the exact A018 working-core candidate. It becomes A021's `F^k` only after an explicit cross-article selection; that selection is not present in A021.

---

## Output C — Candidate comparison

### C3: gated Candidate-A three-state core

**Strengths**

- Named, explicit DDE.
- Closed-form equilibrium.
- Complete local Hopf-frequency cubic.
- Interval-certified fundamental crossings.
- First Lyapunov coefficients.
- Numerically continued small and large periodic families with selected Floquet evidence.

**Weaknesses for A021**

- State is `(N,Z,E)`, whereas A021 declares `(N,A,Z,E)`.
- It freezes `A`; it is an inner approximation, not the primary vector-Liebig block.
- Its nonlinear diagram differs materially from the four-state working core.

**Decision:** excellent source for local spectral formulas and a possible periodic-orbit test case; not the primary A021 block.

### C4: gated Candidate-A four-state working core

**Strengths**

- Exact state match `(N,A,Z,E)`.
- Exact working-core projection in A018's stated large-reservoir/dynamic-target scope.
- Named equilibrium and parameterization.
- Characteristic-pinned Hopf pair.
- Four-state large-cycle continuation and fold locations at source-stated numerical status.

**Weaknesses**

- A021 does not select it explicitly.
- The frozen-donor equilibrium is not a rest point of a closed geological donor equation; this scope must remain visible.
- The complete Floquet spectrum and invariant projections for one chosen attracting four-state cycle are not tabulated.

**Decision:** selected as the architectural binding candidate, but only for a partial crosswalk.

### C5: five-state `(N,A,U,Z,E)` extension

`U` is driven under the dynamic-target working closure but may feed back under another closure. Selecting C5 would conflict with A021's four-state block unless the driven auxiliary is explicitly excluded by an exact triangular projection. It adds no advantage for the NAIM question.

**Decision:** reject as the primary A021 block; retain as a consistency check on the chosen closure.

### Candidate B and ungated systems

These are distinct model/operator points, not rescalings of gated Candidate A. Their spectra and periodic families cannot be transferred to the gated Candidate-A four-state block. They may illustrate alternative dynamics but should not be used to close A021.

### Equilibrium versus periodic base

- **Equilibrium:** supportable as a zero-dimensional compact object at a stable Candidate-A parameter, but yields only a persistent point.
- **Periodic orbit:** scientifically closer to a one-dimensional graph, but the complete Floquet/projection package is missing for a selected gated four-state orbit.

---

## Output D — Selected invariant object

### D1. Strongest presently supportable concrete object: equilibrium point

Take the gated Candidate-A four-state equilibrium

\[
(N^*,A^*,Z^*,E^*)
=(89.52562,397.8665,\ln2/10,2.08962)
\]

at a fixed delay in the source-stated stable/monostable interval, for example `tau=10 yr`.

Define the constant history `hat x_*` and

\[
\mathcal A_x=\{\widehat x_*\}.
\]

- dimension: `0`;
- atlas: one point;
- boundary: empty;
- compactness: immediate;
- restricted flow: identity on one point.

This selection requires confirmation that the complete four-state characteristic spectrum at `tau=10` is strictly stable. A018's reported Hopf ordering and monostable interval support that conclusion at source-stated status, but a numerical spectral abscissa and semigroup prefactor are not reported in the crosswalk packet.

Even if completed, this is an equilibrium-continuation result, not an invariant graph over a positive-dimensional binding region.

### D2. Best periodic candidate, not selected as verified NAIM

A possible test object is the attracting gated three-state large cycle near `tau=5.55 yr`, with source-stated period about `324 yr`, `N` range `[68.7,94.2]`, and large-family continuation/Floquet evidence. It is not selected because:

1. it belongs to C3 rather than the primary C4 block;
2. the complete nontrivial Floquet spectrum and history-space projections are not supplied;
3. the nearby large-cycle termination/fold makes uniform normal bounds parameter-sensitive.

The upper ungated orbit near `tau=131.8` has stronger reported full-stability language, including dominant nontrivial modulus about `0.81`, but it is the wrong operator (ungated).

**Selected-object status:** `NO_POSITIVE_DIMENSIONAL_CONCRETE_NAIM_SELECTED`.

---

## Output E — Binding/slack/coupling decomposition

### Binding functional

The selected candidate `F^k` is the C4 vector field displayed in Output B, acting on `C([−tau,0],R^4)` and depending on the delayed history only through the `Z` component in the effort equation.

### Slack functional

A021 requires

\[
G(y_t)=\bigl(F^1(y_t^1),\ldots,F^{k-1}(y_t^{k-1}),F^{k+1}(y_t^{k+1}),\ldots\bigr),
\]

but the source does not provide:

- the number of slack copies;
- their core choices (C3/C4/C5, gated/ungated);
- their parameter points;
- their equilibria;
- their complete spectra.

Therefore `G` is `MISSING_FROM_SOURCE` as a concrete A021 functional.

### Coupling functionals

The soft-minimum identifies exponentially small off-limiting derivatives, but no source derives a reduced four-state formula showing exactly how those derivatives enter `dot N`, `dot A`, `dot Z`, or `dot E` across blocks. Physical coupling `epsilon_phys R` is likewise abstract.

Therefore:

- `f`: `MISSING_FROM_SOURCE`;
- `g`: `MISSING_FROM_SOURCE`;
- uniform `C1` perturbation bound: not established for a concrete multi-block system;
- uniform yield-gap region: not instantiated.

This missing coupling is independently fatal to concrete A021 persistence, even if a binding NAIM were selected.

---

## Output F — Complete spectral/Floquet table

| Quantity | Definition | Existing evidence | Value/bound | Missing work |
|---|---|---|---|---|
| `alpha` | tangent forward growth | equilibrium base has zero tangent bundle | vacuous | none for point |
| `alpha_inv` | inverse tangent | equilibrium base | vacuous | none for point |
| `M_c` | tangent prefactor | equilibrium base | vacuous | avoid artificial value |
| `beta_x` | worst binding-normal decay | C4 characteristic matrix and Hopf ordering | positive at a stable `tau`, but not numerically tabulated at `tau=10` | complete root abscissa and semigroup bound |
| `M_x` | binding-normal transient prefactor | not reported | missing | semigroup/solution-operator estimate |
| `beta_y,j` | slack-block decay | no concrete slack blocks | missing | choose blocks/parameters and compute all roots |
| `M_y,j` | slack prefactor | absent | missing | semigroup estimates |
| full complement | all modes assigned | impossible without concrete `G` | incomplete | full product splitting |
| periodic `alpha` | phase direction | for a genuine periodic orbit exponent is zero | `0` with prefactor | selected orbit needed |
| periodic `beta_x` | all nontrivial Floquet exponents | selected/dominant multipliers exist in A018 | incomplete for selected C4 orbit | complete monodromy spectrum and projections |

### Existing characteristic data that must not be overstated

A018 supplies a complete **local Hopf-frequency enumeration** for C3 through its cubic `H`. That is not the same as a complete characteristic-root list in a right half-plane at an arbitrary stable parameter, and it is not a Floquet spectrum of a periodic orbit.

A018 supplies selected Floquet multipliers and, for some named cycles, statements that all computed nontrivial multipliers lie inside the unit circle. Those claims may be trusted at their source-stated numerical status, but they do not supply the exact uniform projections and prefactors required by the NAIM theorem.

---

## Output G — Domination calculation

For the zero-dimensional equilibrium base, tangent bunching is vacuous. Normal attraction would require

\[
\|D\Phi_F^t(\widehat x_*)\|\le M_x e^{-\beta_xt}
\]

for the selected binding equilibrium and corresponding estimates for every slack equilibrium. The product rate would be

\[
\beta=\min(\beta_x,\beta_{y,1},\ldots),
\qquad
M_s=\max(M_x,M_{y,1},\ldots).
\]

Neither `beta_y,j` nor any slack prefactor is available. Thus even the product-equilibrium attraction table is incomplete.

For a periodic base, the required time-`T` quantity is

\[
q_1(T)=M_sM_c e^{-(\beta-\alpha_{\rm inv})T}.
\]

Although `alpha=alpha_inv=0` for a bounded phase direction, `M_s`, `M_c`, and the worst complete normal exponent are unavailable for a selected gated C4 orbit.

**Decision:** `DOMINATION_NOT_VERIFIED`.

No numerical bunching value can be computed without fabricating missing prefactors and spectra.

---

## Output H — External-theorem matching table

### Source status

The verified bibliography is:

P. W. Bates, K. Lu, and C. Zeng, *Existence and Persistence of Invariant Manifolds for Semiflows in Banach Space*, Memoirs AMS **135** (1998), no. 645, DOI `10.1090/memo/0645`.

The AMS record confirms that Chapter 10 concerns persistence, but the exact theorem statement/page was not available in the supplied local packet. The related 2000 TAMS foliation paper explicitly describes the 1998 memoir as the persistence source. This is enough to correct the bibliography, not enough to claim a line-by-line theorem match.

| External theorem hypothesis | Selected object | Evidence | Status |
|---|---|---|---|
| Banach ambient space | `B=X×Y` | standard | `VERIFIED` |
| `C1` semiflow on localized neighborhood | candidate C4 plus concrete slack/coupling | binding map available; full product absent | `MISSING` |
| compact embedded invariant manifold | equilibrium point | binding point candidate | `ASSUMED` pending selected stable delay |
| complete invariant splitting | all binding and slack directions | slack/coupling absent | `MISSING` |
| normal contraction | full product | binding qualitative; slack absent | `MISSING` |
| tangent/conorm bounds | zero tangent for point | vacuous | `VERIFIED` for point only |
| exact bunching | product rates/prefactors | missing | `MISSING` |
| tubular geometry | point or compact orbit | automatic for point | `VERIFIED` for point only |
| boundary condition | point has no boundary | immediate | `VERIFIED` |
| perturbation topology | concrete `f,g` | absent | `MISSING` |
| exact theorem number/conclusion | BLZ 1998 | source statement not opened | `MISSING` |
| stable foliation/asymptotic phase | selected theorem | not matched | `MISSING` |

**Decision:** `THEOREM_NOT_SOURCE_MATCHED` for concrete A021 promotion.

---

## Output I — Vertical graph and attraction status

For the equilibrium base, persistence would yield one nearby point

\[
\mathcal M_\varepsilon=\{(x_*(\varepsilon),y_*(\varepsilon))\}.
\]

Its projection is trivially a point and can be written as a graph over a singleton. This is not the regional slaving relation intended by A021 and adds nothing beyond equilibrium continuation plus stability roughness.

For a periodic base, a persistent closed curve could become a vertical graph only over its perturbed projected closed curve after compact-embedding stability is proved. It would not be a graph over a history region or over `C([−tau,0],K_x)`.

No all-time basin, asymptotic phase, or attraction rate is promoted because the exact theorem/foliation match and full product data are absent.

---

## Output J — Hopf consistency report

1. **Characteristic crossing:** supported for named A018 equilibria at the exact source-stated status and independently covered by A021's direct crossing theorem.
2. **Periodic-branch existence:** supported locally where A018 reports Hopf/continuation results, but operator and branch identities must be preserved.
3. **Criticality:** A018 reports normalized first Lyapunov coefficients for named C3 cases. These do not automatically transfer to C4 or a multi-block A021 system.
4. **Periodic-orbit stability:** selected Floquet evidence exists, but no complete C4 NAIM package is assembled.
5. **Folds:** local Hopf persistence does not transfer fold locations. A018 explicitly distinguishes C3 and C4 global diagrams.
6. **NAIM parameter choice:** do not select the Hopf point itself; normal hyperbolicity fails in the center direction there. Do not select a fold where a nontrivial multiplier approaches `+1`.

---

## Output K — Minimal missing-data request

The smallest additional package is:

1. A formal decision: “A021 binding block equals gated Candidate-A C4 at parameter point ___.”
2. A list of every slack block, its selected core and parameter point.
3. Explicit reduced-core formulas for cross-block `f` and `g`, including `epsilon_phys`.
4. The uniform state/history region on which the yield gap and `C1` coupling bound hold.
5. If using an equilibrium: complete characteristic-root abscissae and semigroup prefactors for binding and every slack block at the selected delay.
6. If using a periodic orbit: one orbit file/identifier, complete Floquet multipliers, history-space spectral projections, and transient prefactors.
7. The exact BLZ theorem statement/page and perturbation topology.

Do not request A018 equations, baseline tables, Hopf crossings, or already reported selected Floquet evidence again.

---

## Output L — Publication consequence

**Decision: add a source crosswalk note, but retain conditional status.**

The defensible addition is a sentence identifying C4 as the natural candidate while stating that A021 has not selected the product/slack/coupling instance or verified complete NAIM data. No concrete graph theorem should be promoted.

Suggested LaTeX:

```latex
\begin{remark}[Relation to the companion working core]
The turnover-corrected gated four-state system $(N,A,Z,E)$ in the
companion manuscript is the natural candidate for the abstract binding
functional $F^k$ used here. The present article does not yet select a
multi-block parameter instance, identify every slack block, or derive
the reduced cross-block functionals $f$ and $g$. Nor has a complete
characteristic/Floquet splitting with prefactor-aware domination been
assembled for a selected compact invariant object. The candidate-core
crosswalk therefore does not promote Conjecture~\ref{conj:graph}.
\end{remark}
```

This patch is optional because the existing implemented A021 source already states the substantive conditional status.

---

## Output M — Machine-readable decision table

```csv
item_id,claim,selected_source,status,evidence,missing_dependency,publication_action
XW-01,A021 binding candidate is gated four-state working core,A018 eq:four-state-working + eq:Z-core + eq:effort-core,PARTIAL,"state and variable match",formal A021 selection,"add crosswalk note only"
XW-02,Candidate-A parameters are available,A018 tab:params and appendices,VERIFIED,"baseline table and equilibrium",none,"cite exact source"
XW-03,Fixed delay structure is available,A018 eq:effort-core,VERIFIED,"tau enters through Z(t-tau); tau_m is relaxation",none,"state explicitly"
XW-04,Concrete slack product G is available,A021/A018,MISSING,"no block list or parameter map",slack selection,"retain conditional"
XW-05,Concrete couplings f and g are available,A021,MISSING,"soft-minimum scale only",derive reduced multi-block coupling,"retain conditional"
XW-06,Equilibrium point is a compact binding manifold,A018 C4 equilibrium,ASSUMED,"named equilibrium at Candidate A",select stable delay and complete root bound,"point result only"
XW-07,Positive-dimensional binding NAIM is verified,A018 periodic branches,MISSING,"selected Floquet evidence only",select orbit and complete spectrum/projections,"do not promote"
XW-08,Full binding-normal decay beta_x is known,A018 characteristic/Floquet records,MISSING,"no complete selected-object bound/prefactor",root or monodromy package,"do not compute bunching"
XW-09,All slack rates beta_yj are known,A021,MISSING,"slack blocks unspecified",slack spectra,"retain conditional"
XW-10,Prefactor-aware domination is verified,A018+A021,MISSING,"M_s and complete beta unavailable",complete rate table,"retain conditional"
XW-11,BLZ theorem is source matched,BLZ Memoirs AMS 135 no 645,MISSING,"bibliography verified; exact theorem not opened",theorem statement/page,"retain template"
XW-12,Vertical graph over a history region follows,A021,INCOMPATIBLE,"point/curve persistence is not regional graph",positive-dimensional verified base and projection,"do not claim"
XW-13,Direct characteristic crossing remains valid,A018+A021,VERIFIED,"named characteristic data and A021 theorem",fixed-space parameterization where needed,"retain"
XW-14,Global folds transfer to A021,A018,INCOMPATIBLE,"local crossing does not transfer folds",independent global continuation theorem,"do not claim"
XW-15,Concrete A021 NAIM theorem can be promoted,A018+A021,MISSING,"crosswalk coupling spectrum and theorem rows open",XW-04 through XW-11,"no promotion"
```

## External bibliography checks used in this attempt

- AMS volume record: `http://www.ams.org/books/memo/0645/`.
- BLZ overflowing-manifold article: `https://onlinelibrary.wiley.com/doi/10.1002/(SICI)1097-0312(199908)52:8%3C983::AID-CPA4%3E3.0.CO;2-O`.
- BLZ invariant-foliations article: `https://community.ams.org/journals/tran/2000-352-10/S0002-9947-00-02503-4/`.

These checks establish the bibliography and the broad persistence/foliation relationship. They do not substitute for opening the exact theorem statement used for a concrete match.

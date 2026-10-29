# Standalone audit of ECOMOD continued 10 — Supplementary Information

**Audited upload:** `ecomod_continued_10_SI.txt`  
**Recommendation:** **Major revision.** The empirical-accounting material is reproducible and several reduced derivations are correct. The SI is not yet a consistent mathematical specification and verification record for the bounded delayed model.

## 1. Version, scope and evidence

The uploaded SI is **byte-for-byte identical** to the repository reference used in the preceding main-paper audit:

`SHA-256: 7e815ab3c5e384448c871d05cc71a735798c4ac265e66f8a068260cc10fb3aab`.

There is therefore no SI revision that resolves those earlier findings. This audit checks the upload directly, adds SI-specific counterexamples, checks the one-stock characteristic equation, and extends the empirical verification to the anchor-sensitivity table and 2022 proxy split.

I did not edit either submitted manuscript, compile a fresh PDF, or run the author's original simulation code. Figures and the named `si_drawdown_depth.csv` were not attached. The independent Euler reconstruction is available in the adjacent audit package and is explicitly not the author's implementation. No claim is made that the named CSV is absent from every location in the wider repository.

## 2. Findings by priority

| Priority | Finding | Assessment |
|---|---|---|
| High | Quality DDE versus clamp; well-posedness and stability | Different mathematical systems are being combined |
| High | Population-delay classification | Hutchinson criterion applied to the wrong equation |
| High | Full debt Jacobian | A feedback derivative is missing |
| Medium | Scalar boundary-debt dynamics versus full land dynamics | Equilibrium reduction needs an explicit scope qualification |
| High | Main/SI recovery endpoint | Same cited scenario has incompatible values |
| Medium | Delay sensitivity | 20/40-year quality paths coincide because saturation occurs first |
| Medium | Reserve lower-bound assertion | Contradicted by a listed initial condition |
| Medium | General debt-channel bound | Initial-debt term is dropped; bound confused with equality |
| Medium | Gate-table extrema | Reported maximum is below the declared initial state |
| Medium | Aggregate-only control claim | Non-identification does not prove impossibility of robust control |
| Medium | Empirical regeneration fits | New fit summaries lack the information needed for reproduction |
| Minor | Undefined ceiling, units, rounded cutoffs | Specification/editorial repairs |

## 3. Mathematical consistency corrections

### SI-1. The stated quality equation leaves the declared state space

**Locations:** S2.3, S3 well-posedness paragraph; main Eq. (10).

For constant history `q=0.9`, `rho_c=0.08`, `tau_g=20`, `qmax=1`, the raw DDE has the exact first-interval solution

`q(t)=0.9+0.0072t`, for `0<=t<=20`.

It reaches 1 at **13.8889 years** and reaches **1.044 at year 20**. Thus `[0,qmax]` is not invariant for the written equation.

The SI explicitly discloses clamping. That disclosure is a strength, but it means the simulated trajectory is a solution of a **bounded/projected law**, not the raw DDE after saturation. Local Lipschitzness of the positive-part and minimum operators does not establish the claimed domain invariance: the raw quality vector field points outward at the ceiling for an admissible delayed history.

The raw equation's equilibrium has characteristic equation

`lambda=-rho_c exp(-lambda tau_g)`.

At baseline, its leading conjugate roots have positive real part, about `0.00065568 +/- 0.0789550 i per year`. Its instability is not an artifact of linearising the raw equation. Rather, the clamp changes the boundary dynamics and invalidates transfer of the raw smooth characteristic calculation to that projected system.

**Repair:** Define the continuous bounded model before analysing it. For the reported monotone implementation, one possible specification is the interior delayed growth law together with zero outward velocity at `q=qmax`, interpreted through a projected/reflected solution definition. State existence and uniqueness for that model and analyse its boundary using appropriate one-sided methods. Alternatively choose a bounded delayed-growth equation and rerun the results. Do not silently identify either alternative with the original smooth DDE.

### SI-2. The population mode is not Hutchinson delayed self-inhibition

**Location:** S2.3, final sentence.

The actual equation delays K:

`P'=rP[1-P/K(t-tau_p)]`.

For constant K it reduces to an ordinary logistic ODE. At `P*=K*`, with the carrying-capacity floor inactive,

`delta P'=-r delta P+(r/e) delta B(t-tau_p)`.

A mode with constant supply therefore has eigenvalue `-r`, not the scalar delayed-self-inhibition characteristic equation. Where supply feeds back from population through land, debt, or restoration, one must examine the coupled active-set matrices.

Using `r tau_p=0.5<pi/2` to declare this mode non-oscillatory is consequently incorrect. Even in the different scalar Hutchinson linear equation, being below the instability threshold does not guarantee monotone decay.

**Repair:** Delete that classification. Supply the actual current-state population row, delayed supply row, capacity-floor status, and feedback-active conditions. No universal oscillation or stability conclusion follows from the product `r tau_p` alone for the equation used here.

### SI-3. Correct the full-system Jacobian and its active-set scope

**Location:** S2.3.

On the aggregate-deficit-active face,

`D'=eP-b_f(D)Af-Upsilon(q)Ac-eta D`.

Therefore

`partial D'/partial D=alpha b_f Af-eta`,

not the printed `-eta`. An independent finite-difference check at an interior test state gives **-0.0271872877**, agreeing with the corrected expression and not with -0.05.

The earlier frozen-debt 2x2 land block is also not the land block on **every** active set. It requires a deficit, the shortfall-limited branch of conversion, restoration off, and the specified fixed quality. Floor-limited conversion, no conversion, restoration, and the K floor produce different derivatives. Reserved availability shares can also make the conversion-shortfall switch differ from the aggregate-deficit switch that drives D.

**Repair:** Give complete matrices, state ordering, parameter values, and all active-set conditions. Include the correct D derivatives in every row. The generic determinant notation is valid as a template; it is not a completed characteristic analysis of the switched/projected model.

### SI-4. An equilibrium supply substitution is not the full transient debt equation

**Location:** S2.4, first two sentences.

At the capital floor, `Ac=Amin` and conversion is zero. But fast land still relaxes according to

`Af'=mu(Atot-Amin)-(mu+eta_f)Af`.

The equality `Af=k(Atot-Amin)` is its equilibrium condition. It is not automatic at every time the capital floor is imposed or approached. Thus the printed scalar equation

`D'=E-B_eq(Amin;D)-eta D`

is exact only after restricting fast land to that equilibrium allocation, or as an asymptotic reduced equation. The full boundary transient instead uses the current Af:

`D'=E-b_f(D)Af(t)-bc Amin-eta D`

on the deficit-active face.

For example, at `Ac=0.05`, `Af=0.6`, `q=1`, `D=0`, `E=1.158`, the full deficit-active boundary gives `Af'=0.081 ha/year` and `D'=0.6455 gha`, whereas the equilibrium substitution gives `D'=0.0195909 gha`. This is a transient-reduction issue, not evidence that the stated fixed points are wrong.

The equilibrium root calculation is correct. The sufficient slope condition also supports a stable reduced scalar root. Those facts do not justify labelling the equilibrium-substituted equation the exact transient dynamics of the full boundary system.

**Repair:** State the reduction explicitly and, if claiming attraction for the full boundary dynamics, use the coupled triangular land/debt system or an asymptotically autonomous argument. Keep the valid equilibrium results.

### SI-5. Reconcile the main/SI recovery example

**Location:** S4.3 and main §3.4.

For the cited run `Ac0=1`, `P0=2`, `chi_r=0.10`, the SI reports **Ac(400)=0.677 ha**, recovery fraction **0.46**. The main text reports **0.828 ha** and **0.71**, without declaring a different endpoint horizon or intervention.

The earlier independent reconstruction at `dt=0.05`, `T=400` gives **0.67818 ha**, close to the SI value. It does not reproduce 0.828 under those settings. Exact update-order/step differences were not resolved because the author's code was not supplied.

**Repair:** Generate the main text and SI from the same run manifest. If both numbers are valid under different horizons or settings, identify them precisely rather than citing the SI table as if it establishes the main value.

## 4. Additional SI-specific errors and scope issues

### SI-6. The reserve minimum of 0.80 ha is contradicted at time zero

**Location:** S1 conventions; S4.2 drawdown sweep initial conditions.

The SI says reserve remains at least **0.80 ha** in the drawdown sweeps. One listed sweep uses `Atot=2.5`, `Af0=0.6`, `Ac0=1.18`, hence

`Ar0=2.5-0.6-1.18=0.72 ha`.

This directly refutes the 0.80 claim without requiring numerical integration. It does **not** by itself violate the separate reserve floor of 0.10 ha; those are different assertions.

The SI also declares `Afmax` a domain constraint but supplies no numerical value for it in the main parameter table or SI symbol table. Further, the raw reserve dynamics preserve the zero boundary under the stated nonnegative flows, not automatically the stricter positive reserve floor.

**Repair:** Report actual extrema including the initial state; specify Afmax and any flow limiter; distinguish constraints guaranteed by the equations from constraints merely observed to remain inactive in reported runs.

### SI-7. The gate-table maximum cannot be a full-trajectory maximum

**Location:** S4.4, gate-sign comparison.

The declared starting capital area is **0.058 ha**, but the no-restoration row reports maximum Ac of **0.057 ha**. A maximum over the trajectory including t=0 must be at least its initial value.

There is a plausible implementation explanation: on a floor-limited first Euler step of 0.1 years,

`Ac_new=0.058-0.1(0.058-0.05)=0.0572`,

which rounds to 0.057. That suggests a summary array may omit the initial state, but this was not verified against the author's implementation.

**Repair:** Include t=0 in extrema or explicitly label a post-initial summary window. Audit minimum and maximum columns, debt peaks, and their times under one shared indexing convention. Also identify which T the single endpoint-area columns use, since the table reports recovery at both 100 and 900 years.

### SI-8. The debt-channel bound loses its initial condition and confuses a bound with equality

**Location:** S2.5.

The valid bound is

`D(t)<=max{D0, sup(F)/eta}`, where `F=[E-B]+` over the elapsed interval.

It follows that the negative log-yield channel is bounded below by

`-alpha max{D0, sup(F)/eta}`,

not always by `-alpha sup(F)/eta`, as stated.

**Counterexample:** let F be identically zero and D0=10. Then `D(t)=10 exp(-eta t)>0`, so the channel remains negative, while the printed lower bound would be zero.

The running supremum of shortfall is also not generally the sustained shortfall or the actual debt. Equality between the technology log-cap and the debt loss requires `alpha D=log(1+Delta b/bf0)`. Replacing D by a supremum bound gives a sufficient bounding comparison, not equality of realised channels. The stationary threshold based on a limiting constant shortfall is valid under that explicit limit.

**Repair:** Retain D0, distinguish finite-time bounds from limiting equalities, and use dimensionless yield ratios for log-channel comparisons. The additive comparison also requires a separately dimensioned coefficient: the multiplicative alpha cannot be reused unchanged in `bf=bf0+Tb-alpha D`.

### SI-9. Aggregate non-identification does not establish impossibility of safe output-based control

**Location:** S6, typed floors and conversion stop.

The SI says a control based only on B cannot guarantee the capital floor because B does not identify Ac. The non-identification is correct; the impossibility conclusion needs a specified initial-information set, controller class and performance requirement.

For example, a controller that stops conversion everywhere, `u_c=0`, gives `Ac'=R_rc>=0`; from a known-safe initial set, it preserves the floor without observing Ac. A constant control is also a permissible function of B if that is the only observation allowed.

Moreover, the displayed conversion rule already satisfies

`u_c<=(Ac-Amin)/tau_conv`.

With nonnegative restoration, this directly guarantees forward preservation of the capital floor from admissible initial states. That guarantee is built into the action law; it is not a successful empirical test of aggregate monitoring, nor a new consequence of a stop action at a boundary that is approached only asymptotically.

**Repair:** Say B alone cannot reconstruct Ac or implement arbitrary Ac-dependent interventions. Any stronger impossibility theorem must exclude robust blanket controls and declare the competing provision/control requirements. Keep the companion finite-plan separation distinct from this hard-constrained model.

### SI-10. Delay insensitivity and numerical resolution need a different explanation

**Locations:** S2.3, S3, S4.2.

With the reported constant history, projected quality saturates at 13.8889 years. For any delay at least that long—including 20 and 40 years—the same projected quality path is obtained. The equality is structural under the clamp, not merely a small numerical effect.

The SI separately reports a step-size shift from **2.955 to about 2.98 cap**, larger than its highlighted delay differences of at most **0.001 cap**. Matched numerical differences can sometimes be estimated more accurately than individual levels, but that requires a convergence study of the differences; the SI does not establish it.

**Repair:** Explain saturation degeneracy first. Provide matched-step refinements and event/proximity definitions before interpreting three-decimal delay differences. Qualify monotonicity of drawdown with initial conditions as a tested finite-grid observation unless a comparison theorem is provided.

### SI-11. Recovery-timescale fits are not reproducible from the cited summaries alone

**Location:** S5.5.

The SI introduces original-seeming analyses: 35 selected forest fits from 41 chronosequences, lagged recovery parameters, and 33 collapsed-stock trajectories. It gives neither the fit equation in full nor the selected records, fitting procedure, censoring treatment, uncertainty, or reproduced outputs.

The cited publications provide legitimate contextual evidence, but a citation alone does not verify these newly summarised fit medians. Mixing a fitted 30-year median half-recovery with a separate statement about roughly half recovery by 20 years requires identifying the different statistics and estimators, not treating them as interchangeable.

**Repair:** Supply the fit inputs and methods or restrict the discussion to directly sourced published summaries. Include unsuccessful/unrecovered trajectories in the selection/censoring account; do not infer a pooled ecological rate or delay from unlike systems. The existing no-calibration caveat is appropriate and should remain.

## 5. What independently verifies

### Empirical accounting: strong

The previous main audit reproduced the headline NFA changes and land-component contributions. The additional SI check now reproduces **all eight 2023 anchor-sensitivity rows** and the **2022 central-anchor split**.

For 2022, the independent LMDI terms are:

- cereal yield: **+0.2646956740**;
- area: **+0.0375056622**;
- residual: **-0.0827045979**;
- total: **+0.2194967384**.

The residual-zero anchors calculate as:

- 2023: **0.340531298672...**;
- 2022: **0.343399803524...**.

These support the rounded thresholds, but use an approximation sign rather than treating the six-decimal number as an exact inequality boundary. At phi0=0.340531, for example, the 2023 residual is still slightly positive.

The decomposition's weights need not sum to one; its exactness follows from the logarithmic-mean identity, not an ordinary convex-weight interpretation. The SI correctly treats the residual as an account construction, not physical capital. The physical-stock scoreboard is explicitly unpopulated; it should not be mistaken for an empirical inventory.

### Reduced two-land derivations: retain with scope

The general composition identity, including debt, technology and restoration terms, checks out. The affine land matrix and its baseline spectrum check out under the declared fixed-quality/frozen-debt/active-conversion reduction. The floor-distance exponential law is correct while floor-limited conversion and no restoration remain active.

The no-conversion equilibrium family acknowledged in S2.2 is important: it supports the main audit's distinction between a unique equality-balance point and multiple switched-system equilibria.

The debt equilibrium roots **1.18577 and 5.37506** check at demands **1.158 and 1.238**. If the demands are instead the unrounded ceiling plus 0.02 and 0.10, the roots change to **1.20965 and 5.39454**. Use consistent inputs when comparing analytic roots and simulations.

### One-stock comparator: reported local positive roots check out

**Location:** S7.

For the stated debt-free active-branch equilibrium, the 2x2 characteristic equation is

`[lambda-b/bG-G'(A*) exp(-lambda tau_g)](lambda+r)`

` + (r/bG)B'(A*) exp(-lambda tau_p)=0`.

It has the reported neutral root at zero. Independent root finding reproduces a positive real root of

- **0.5883333333/year** at delays (0,0);
- **0.6249999968/year** at delays (30,25).

Thus those local instability statements are supported. They are not the same erroneous scalar population-mode classification discussed in SI-2. They also do not verify the comparator's long trajectories, 721-year floor event, or basin-grid classification. Those require the RK4/interpolation/projection code and outputs.

### Matched technology-wave experiment: design is clearly described

S8 appropriately states the common no-wave prehistory, the nonzero current wave tail at t=0, the difference between all-time and post-midpoint maxima, and the conditional nature of the debt result. These are strengths.

The table's reported step-halving changes are internally consistent with its less-than-0.9% statement. Independent reconstruction broadly agrees with the direction and approximate size of the effects, but does not reproduce every maximum exactly; it is not a replacement for the author's run logs.

## 6. Reproducibility and editorial requirements

1. Publish the exact simulator, delay interpolation/indexing, projection rule and update order for each formulation. Two-land Euler and one-stock RK4 are distinct implementations.
2. Include `si_drawdown_depth.csv`, initial states, parameter dictionaries, run horizons, event definitions and both T values used for gate summaries.
3. Separate exact derivations, finite-grid observations, asymptotic reductions and numerical illustrations in headings/captions.
4. Generate main-text and SI summary values from the same versioned data products.
5. Replace claims that capital contribution is “unaffected” by technology/debt with “has no direct functional dependence at fixed Ac and q”; its trajectory can change through land feedbacks.
6. Clarify restoration timing: reserve-to-capital restoration contributes `+Upsilon R_rc` instantaneously to B. Any provision cost through depleted reserve/maintenance is a dynamic effect, not an automatically negative instantaneous contribution.
7. Internal reference labels and citation keys resolve; no duplicates were found. This is not a PDF-layout check. Complete graphics and build assets remain necessary for an independently reproduced supplement.

## 7. Recommended disposition

Keep S5's careful account/physical-stock separation and verified accounting calculations. Keep the valid affine derivations and the comparator's correctly scoped local roots. Rebuild S2.3 and the well-posedness paragraph around the actual bounded model, correct the new numerical/table inconsistencies, and attach a reproducible run package.

**Final assessment:** This SI is useful supporting material, but it currently mixes valid algebra with incompatible model semantics and inadequately supported numerical claims. Major revision is warranted. These issues do not invalidate the simple composition-masking identity or the reproduced NFA accounting trends.

---

## Audit artifacts

- `verify_ecomod_si.py`: additional SI checks.
- `si_verification_results.json`: machine-readable results.
- `si_verification_stdout.txt`: printed results.
- `AUDIT_ECOMOD_C10.md`: preceding main-paper audit.

The SI check uses the same attributed public data as the main audit and adds exact boundary/constraint counterexamples, a finite-difference Jacobian check, comparator characteristic-root checks and proxy-sensitivity recalculation. The upload and reference source were not modified.

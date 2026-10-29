# Audit: ECOMOD continued 10

**Manuscript:** *A rising biocapacity total can mask ecological-capital land drawdown: a two-land model*  
**Submitted source:** `ecomod_continued_10.txt`  
**Recommendation:** **Major revision before submission.** The accounting mechanism and empirical calculations survive checking. The specification and analysis of the delayed, bounded dynamical system need substantive correction.

## 1. Scope and bottom line

I read the complete supplied main source and retrieved its companion SI from the pinned repository version. The retrieved main `.tex` is **byte-for-byte identical** to the submitted `.txt`, establishing the version match. I also downloaded the cited NFA Edition 2026 workbook and the two OWID series, recalculated the empirical results, and independently implemented the displayed Euler equations with the disclosed state clipping.

This is a source/equation/data audit, not a PDF-layout audit. No manuscript or figure edits were made. The author's simulation code was not supplied with the attachment; the audit implementation is an independent reconstruction, not a claim to reproduce the author's exact update ordering. I did not run a fresh LaTeX build.

### Overall finding

There are two substantially different conclusions:

- **Empirical accounting:** unusually strong reproducibility from the public inputs. The headline NFA percentages, component contributions, first overshoot year, and proxy LMDI split all reproduce.
- **Dynamics and interpretation:** the continuous equations, numerical bounds, and stability claims do not consistently describe the same model. A disclosed clamp is doing substantive mathematical work, not merely preventing numerical roundoff. The full-system linearisation and recovery reporting also require repair.

The title's narrow claim remains defensible: a weighted total can rise while a constituent area falls. The manuscript should be presented as a conditional accounting/model illustration, not as a demonstrated delayed-system stability classification or physical-stock diagnosis.

## 2. Highest-priority findings

### E1 — The quality equation does not preserve its stated domain; the simulations solve a different bounded law

**Main locations:** Eq. `eq:q`; Methods, numerical implementation; Proposition 2 opening.  
**SI locations:** S2.3, characteristic structure; S3, well-posedness paragraph.

The written equation is

`q'(t)=rho_c q(t-tau_g)[1-q(t-tau_g)/qmax]`.

With the stated constant history `q=0.9`, `rho_c=0.08`, `qmax=1`, and `tau_g=20`, the first method-of-steps interval is exactly

`q(t)=0.9+0.0072 t`, for `0<=t<=20`.

It reaches 1 at **13.8889 years** and reaches **1.044 at year 20**. Thus the original DDE leaves `[0,1]` before the first delay interval ends.

The SI explicitly acknowledges clamping at `qmax`. That is valuable disclosure, so this is **not an undisclosed implementation trick**. But the clamp must be part of the mathematical model itself. The bounded trajectory is not a solution of the raw DDE after the ceiling is reached.

The raw equilibrium has characteristic equation

`lambda=-0.08 exp(-20 lambda)`.

Its leading conjugate roots have positive real part, approximately **0.00065568 +/- 0.0789550 i per year**. Its linear stability threshold is `tau_g=pi/(2 rho_c)=19.635 years`. The baseline raw DDE is beyond it. Calling this instability an artifact of linearisation is misleading: it belongs to the written smooth DDE; the clamp changes the system to a unilateral/projected model.

The SI's assertion that positive-part/minimum Lipschitzness establishes forward invariance and uniqueness does not fix the ceiling violation. The raw vector field is locally Lipschitz but points out of the proposed domain. Conversely, the projected boundary law needs its own solution definition and well-posedness argument.

**Required repair:** Choose and state one model before deriving results:

1. a properly defined projected/saturating delay equation, with a boundary regulator or explicit admissible solution rule; or
2. a different bounded delayed-growth equation, followed by new simulations and analysis.

Remove the unqualified assertion that `qmax` attracts every positive initial condition of the raw equation. Do not apply its ordinary smooth characteristic equation as the stability theory of the projected model.

### E2 — The weak delay sensitivity is partly an exact saturation degeneracy

**Locations:** main predictions P4, Table 2(b)/delay discussion; SI S3, Table S2.

Under the reported initial history, saturation occurs at 13.8889 years. For **every delay at least this long**, including both 20 and 40 years, the projected quality path is identical:

`q(t)=min(1,0.9+0.0072 t)`.

Before saturation it still sees the constant history; after saturation it is clamped forever. Therefore changing the regeneration delay from 20 to 40 does not test a different quality-response trajectory at all under this implementation. With other inputs unchanged, the rest of the model also receives the same current quality path.

**Required repair:** Report this analytical degeneracy explicitly. The 5/20/40 comparison is not evidence of generic delay robustness. If ecological-delay effects are a research question, include initial histories, quality levels, or a bounded growth law for which the delay actually changes the dynamics over a substantive interval.

### E3 — The SI imports the wrong population-delay stability criterion

**Locations:** main Eq. `eq:P`; SI S2.3.

The paper uses

`P'(t)=r P(t)[1-P(t)/K(t-tau_p)]`,

which delays carrying capacity, not population in the crowding term. When K is constant, the equation is the **ordinary logistic ODE**. At its positive equilibrium, the population perturbation obeys `delta P'=-r delta P` if the capacity perturbation is zero.

More generally, with the capacity floor inactive,

`delta P'=-r delta P+(r/e) delta B(t-tau_p)`.

On a face where supply has no feedback from population, this is a delayed forcing of a stable current-state population mode, not Hutchinson's delayed self-inhibition mode. If land/debt/restoration create feedback, the coupled characteristic equation must be analysed; it does not reduce automatically to the scalar Hutchinson criterion.

The SI nevertheless uses `r tau_p=0.5<pi/2` to declare a non-oscillatory mode. That criterion belongs to a different equation. Even for the scalar equation `x'=-r x(t-tau)`, stability below the Hopf threshold does **not** imply non-oscillatory decay.

**Required repair:** Remove this classification and derive the actual active-set linearisation. State the capacity-floor and restoration/shortfall assumptions used for each mode.

### E4 — The debt row of the full Jacobian omits a feedback derivative

**Location:** SI S2.3, displayed debt row in prose.

On the deficit-active face, `D'=eP-B-eta D` and `b_f=b_f0 exp(-alpha D)`. Thus

`partial D'/partial D = alpha b_f A_f - eta`,

not `-eta`, as written in the SI's debt row. The remaining D-dependence in the land equations must also be included consistently.

**Required repair:** Publish complete active-set matrices with explicit variable ordering, delayed/current arguments, and switch status. Recheck any full-system spectral conclusions against the corrected matrices. The separate frozen-debt 2x2 land matrix checks out and is not invalidated by this correction.

### E5 — The main-text recovery endpoint conflicts with its SI

**Locations:** main §3.4, recovery example; SI S4.3, recovery table.

For `Ac0=1`, `P0=2`, and surplus restoration `chi_r=0.10`:

- The main text gives recovery to **0.828 ha**, with recovery fraction **0.71**.
- The SI table gives **0.677 ha at T=400 years**, with fraction **0.46**.

The main text cites that same SI subsection without identifying a different horizon or intervention. My independent Euler reconstruction at `dt=0.05`, `T=400` gives minimum **0.399785 ha** and final restored area **0.678183 ha**. This supports the SI-scale result, not 0.828. Differences from the table's rounded minimum 0.398 are consistent with numerical-resolution/update details, but cannot explain a 0.15 ha endpoint discrepancy.

**Required repair:** Use a single versioned run record, state its step size and endpoint horizon, and generate both main and SI values from it. If 0.828 belongs to another horizon or scenario, label it explicitly and provide that run.

## 3. Reduced-system claims: preserve the valid algebra, narrow the interpretation

### E6 — There is one equality-balance point, but generally many fixed-demand equilibria

**Locations:** Proposition 2; §3.2; Discussion, no-fold/hysteresis statements.

The equation `B_eq(Ac)=E` has at most one root under the stated yield ordering. That algebra is correct. But the shortfall switch turns conversion off whenever **B>=E**, not only at equality. With restoration off and quality/debt fixed, every maintenance-balanced allocation with `B_eq(Ac)>=E` is an equilibrium.

For example, at `E=0.825`, both the equality point `Ac=0.807692...` and the surplus allocation

- `Ac=0.5`;
- `Af=1.090909...`;
- `Ar=0.909091...`;
- `B=0.952273...`

are equilibria of the reduced land system.

On the surplus/no-conversion face, the land Jacobian is

```
[ -(mu+eta_f)   -mu ]
[       0        0 ]
```

and has eigenvalues **-0.11 and 0**, unlike the two negative deficit-side eigenvalues. A displacement into surplus need not return to the original equality point: it can settle at another equilibrium. The deficit-side return rate is therefore not a two-sided return rate for an isolated equilibrium of the switched system.

The manuscript already distinguishes a balance relation from history-dependent realised paths in several places. Retain that useful qualification, but make it mathematically explicit: the no-fold statement applies to the **equality-balance locus**, not a unique global equilibrium family with ordinary two-sided asymptotic stability. A reversible demand protocol can also produce path-dependent loops under irreversible conversion; absence of a fold does not by itself exclude every meaning of hysteresis.

**Required repair:** State the equilibrium inequality/set, both active-set Jacobians, and the exact definition of hysteresis being excluded. Keep “no fold on the stated equality locus”; avoid presenting its 19-year deficit-side rate as a full-system safety or early-warning result.

### E7 — Proposition 1(ii)'s maintained balance is not an invariant conversion regime

**Location:** Proposition 1(ii) and proof.

The comparison assumes `mu Ar=eta_f Af` while conversion continues, restoration is off, and quality/debt are fixed. Under the original land equations this gives `Ar'=0`, `Af'=u_c`, and hence

`d/dt(mu Ar-eta_f Af)=-eta_f u_c`.

For positive retirement and conversion, the maintenance balance immediately breaks. It can cancel terms at an instant, but cannot persist along a positive-duration conversion interval without an additional control or altered flow rule.

**Required repair:** Mark this as a counterfactual reduced bookkeeping comparison and specify the changed dynamics, or derive the result using the actual affine land system. Instantaneous re-equilibration of fast/reserve shares would change the marginal supply coefficient to `b_f k-Upsilon`, not simply `b_f-Upsilon`.

Also replace Proposition 1(i)'s “determines the sign ... only if” with “in particular when.” Vanishing other terms is sufficient, not necessary; nonzero terms can have the same sign or be too small to reverse it.

### E8 — Identifiability must be scoped to the observation equation, not all dynamic observations

**Location:** Proposition 1(iii).

The fixed-profile non-identifiability and feasible perturbation are correct. The account equation identifies `b_G,c rho_c` rather than its factors. But an informative quality **time series**, a known delay, and a specified interior quality law can identify rho from that law, after which the product can identify b_G,c.

The limitations already use the narrower word “cross-section.” Carry it into the proposition: the non-identification concerns the account equation/cross-sectional data alone, not structural non-identifiability of the entire observed dynamical system.

## 4. Numerical, dimensional, and interpretation repairs

### E9 — Threshold precision is weaker than the highlighted delay effect

**Locations:** main Table 2(b), P4; SI S3.

The SI reports that halving the Euler step changes a population proximity value from **2.955 to about 2.98 cap**, while the claimed regeneration-delay effect is at most **0.001 cap**. The paper does disclose step sensitivity and calls its markers bands, which is appropriate. But these figures do not establish that a 0.001 physical/dynamical delay effect is resolved.

**Required repair:** Use matched-step comparisons and a convergence study on the **difference between scenarios**, including smaller steps and event/proximity definitions. Report uncertainty bands before quoting the delay difference to three decimals. The analytic saturation degeneracy in E2 explains part of the invariance exactly and should take precedence over numerical precision claims.

### E10 — A debt-root comparison uses rounded and unrounded demand inputs

**Location:** §3.2, comparison of analytic and integrated debt equilibria.

The reduced ceiling checks as **1.1384090909 gha**. Solving the stated debt equation gives:

| Demand used | Debt equilibrium |
|---|---:|
| 1.158 | 1.18576698 |
| 1.238 | 5.37506262 |
| Eceil+0.02 = 1.15840909... | 1.20965490 |
| Eceil+0.10 = 1.23840909... | 5.39453751 |

These reproduce both the “calculated” 1.19/5.38 and the “integrated” 1.21/5.39, suggesting mismatched rounded versus exact demand inputs rather than solver disagreement. This diagnosis should be checked against the author's code, which was not supplied.

**Required repair:** Store and compare identical numerical inputs; give the ceiling offsets as the scenario definition and distinguish display rounding from calculation values.

### E11 — Smaller specification and units issues

- **Additive-yield comparison:** `b_f=b_f0+T_b-alpha D` reuses the multiplicative alpha, whose units are `(gha yr)^-1`. Then alpha D is dimensionless and cannot be subtracted from yield in gha/ha. Introduce an additive coefficient with units `ha^-1 yr^-1`, or explicitly nondimensionalise yield.
- **Reserve floor:** `Ar>=0` is compatible with the raw flow at Ar=0. The stricter declared floor `Ar>=0.10` is not generally invariant without a limiter. The SI says reported trajectories respect it; distinguish observed inactivity from a general domain theorem. Enforcing this floor also changes the extreme feasible low-demand area range used in Proposition 2.
- **Carrying-capacity statement:** `P=K` implies `E=B` only when the K floor is inactive. An instantaneous crossing of P and current K also does not imply equilibrium when the denominator uses delayed K. State the equilibrium and inactive-floor qualifications.
- **Quality versus condition:** Upsilon declines as q improves from 0.9 to 1 because the regeneration-rate term declines near maturity. The extra decline from 46.16% area loss to 51.72% account-contribution loss partly reflects this chosen maturation valuation, not worsening quality. The source largely discloses this; retain the distinction prominently and avoid reading that percentage as physical ecological degradation.
- **Lifetime of the mask:** the strict-inequality duration is a numerical/event criterion, not an invariant ecological horizon. State thresholds for derivative/area-change detection and check event-time convergence; the audit reconstruction gives 148.6, 149.0, and 149.175 years at dt=0.1, 0.05, and 0.025.

## 5. Empirical results: independently reproduced

The following were recomputed from the actual cited workbook, not merely checked for internal arithmetic.

### NFA Edition 2026 world series

| Measure | Independent value | Manuscript |
|---|---:|---:|
| B change, 1961–2023 | +24.8567877% | +24.86% |
| B/P change | -52.7085280% | -52.71% |
| Production footprint/person change | +16.7327097% | +16.73% |
| delta log B | +0.2219971963 | +0.221997 |
| delta log P | +0.9708373983 | +0.970837 |
| delta log(B/P) | -0.7488402020 | -0.748840 |
| First production-footprint/B > 1 | 1973 | 1973 |

The workbook marks 2023 as `+++` and 2024–2025 as estimated `E`; excluding the last two years is correctly implemented in the paper's stated window.

### Component contributions, percentage points of 1961 B

| Component | Independent value |
|---|---:|
| Cropland | +24.0577408 |
| Grazing | -0.2688172 |
| Forest | -5.9525373 |
| Fishing grounds | -0.4212268 |
| Built-up land | +7.4416281 |

The endpoint ratios and same-edition 2022 sensitivity also reproduce. Small integer-gha component-total differences are consistent with workbook rounding. Cropland accounts for about 96.8% of the **net change**, not 96.8% of all positive component growth; preserve that denominator.

### Auxiliary proxy LMDI split

Using the downloaded OWID cropland-area and cereal-yield series and the declared 1961 NFA crop anchor gives:

- yield contribution: **+0.2686622953**;
- area contribution: **+0.0377097964**;
- residual contribution: **-0.0843748954**;
- sum: **+0.2219971963**.

These match the manuscript. The construction is a defensible exact proxy identity, not an independent estimate of physical ecological capital. The paper's explicit caveats about cereal yield, boundary mismatches, built-up land, residuals, and physical stocks should remain. This separation between data description and model mechanism is a major strength.

## 6. Other checks and presentation

- No missing main-source reference labels, duplicate labels, or missing citation keys were found. SI internal labels also resolve. This does not establish PDF layout or the correctness of hard-coded equation/table numbers.
- The core differentiation identity, affine deficit-side J, yield sweep eigenvalues, equality-balance formula, debt-root uniqueness condition, and technology/debt bound check out under their stated reductions.
- Independent clipped-Euler reconstruction closely reproduces the frozen-demand demonstration, including its 149-year mask event, and broadly reproduces the matched wave debt effects. Some maxima differ at sub-percent levels from the reported numbers, so I do not certify identical implementation or update ordering.
- Do not call every recovery timescale a published result of the cited papers. The SI introduces its own apparent lagged fits, selected chronosequences, and 33-stock summaries. Supply those inputs, fit equations, selection rules, code and uncertainty, or report only clearly sourced published context. Poorter et al.'s published abstract supports a median 66 years to 90% recovery, but does not by itself verify this manuscript's fitted median 30-year half-recovery figure [1](https://www.nature.com/articles/nature16512).
- The “five empirical predictions” include identities, assumptions, and consequences of disabling return flows. Distinguish testable model implications from independent empirical predictions, and state observable quantities and falsification conditions.
- Data/code availability should give an actual versioned release and repository path rather than “will be deposited.” Include the projection rule and exact update ordering, prehistories, initial D, run horizons, parameter dictionaries and the scripts generating both main and SI tables.
- Acknowledgments to named reviewers and journal editors should be retained only if the stated assistance occurred and appropriate permission has been obtained. I did not verify those claims; no impropriety is inferred.

## 7. Recommended revision sequence

1. Define the bounded quality dynamics mathematically, rather than only through a numerical clamp.
2. Remove the incorrect population-delay classification and correct the debt Jacobian.
3. State the complete switched equilibrium set and distinguish one-sided rates from full-system stability.
4. Repair Proposition 1(ii)'s non-invariant maintained-balance reduction.
5. Reconcile recovery values and demand inputs using one versioned run manifest.
6. Reassess delay comparisons after accounting for saturation degeneracy and time-step error.
7. Publish the source/SI/code/figure/data bundle with exact reproduction instructions.
8. Retain the verified empirical analysis and narrow the claims to its genuinely accounting role.

**Bottom line:** The empirical account decomposition is reproducible, and the compositional masking mechanism is correct under explicit assumptions. The manuscript is not yet ready to support its current delayed-model stability discussion. Correcting the model/projection specification and associated analysis is the main prerequisite for publication.

---

## Audit artifacts and provenance

- `verify_ecomod.py`: independent checks and Euler reconstruction.
- `verification_results.json`: machine-readable results.
- `verification_stdout.txt`: printed verification results.
- `world_data_extracted.csv`: extracted NFA world series, under CC BY-SA 4.0 with source attribution in README.
- `reference/NEFBA_2026.xlsx`: unchanged public workbook.
- `reference/cropland-area.csv`, `reference/cereal-yield.csv`: downloaded OWID/FAOSTAT inputs.
- `reference/ecomod_continued_10.tex`, `reference/ecomod_continued_10_SI.tex`: retrieved version-matched reference sources.

Primary workbook: https://footprint.info.yorku.ca/files/2026/04/NEFBA_Data_global_national_ecological_footprint_biocapacity.xlsx

Pinned source directory: https://github.com/MIKEAA2020/general-sustainability/tree/6f626ee48b2a3a59282b5df5adda76c8d5993fdc/agent%202%20productivity%20illusion/output_v45_ecomod_continued_10_gemini38_v4base_si_review_20261026

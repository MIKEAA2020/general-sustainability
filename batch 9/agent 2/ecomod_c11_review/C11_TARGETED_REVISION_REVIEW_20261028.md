# C11 targeted revision review

**Input:** `ecomod_continued_11_revision_draft_20261028.pdf` (35 PDF pages; 774,126 bytes).  
**SHA-256:** `1433afaf75dc43f318545a695277d7b05a31aeb950a1283de962829199ce43db`  
**Date:** 2026-10-28  
**Scope selected by user:** Check whether C11 resolves the recorded C10 audit findings, particularly the projected quality law, stability, recovery, and numerical reproducibility. This is not a fresh full scientific or publication-layout audit.

## Executive assessment

**Substantial improvement; the audit should not yet be closed.** C11 adopts the agreed constrained phenomenological interpretation rather than quietly substituting a new biological mechanism. The key quality-model mismatch is addressed at the equation level, the delay comparison is correctly reinterpreted, recovery numbers are reconciled in the main text, and equilibrium/stability claims are substantially better scoped.

An independent reconstruction following the newly disclosed timing convention now reproduces the reported 0.677 ha recovery endpoint at the stated step size. Most of the new frozen-demand refinement statistics also reproduce to their printed precision. These are meaningful improvements, not merely disclaimers.

Outstanding work is narrower: repair several remaining mathematical/control statements, provide the revised SI, and attach the versioned code/run outputs that support the new numerical disclosures. **There is no reason on this evidence to reopen the choice between projection and an unvalidated smooth replacement.**

Page numbers below are PDF page numbers. Original manuscript, PDF and existing C10 audit files were not edited.

## 1. Disposition of the six core findings

| C10 finding | C11 assessment | Evidence in this PDF |
|---|---|---|
| E1: Raw quality DDE violates ceiling; simulated clamp changes model | **Addressed in the main specification** | pp. 4, 6: q is uncalibrated; qmax is an imposed bound; Eq. (10) explicitly projects onto the tangent cone. Histories and an absolutely continuous, almost-everywhere interpretation are supplied. Numerical realization is described on pp. 10–11. SI well-posedness proof remains to be checked. |
| E2: 20/40-year comparison is saturation-degenerate | **Addressed** | pp. 17–18 and Table 4, p. 25 explicitly explain identical baseline quality paths and reject a general robustness inference. |
| E3: Population equation is not Hutchinson delayed self-inhibition | **Misclassification removed from main; SI verification pending** | p. 6 explicitly locates delay in K, not the crowding population. No Hutchinson criterion appears in the extracted main PDF. The main text does not supply the full revised characteristic analysis. |
| E4: Missing debt own-state feedback derivative | **Not verifiable from this upload** | The correct debt equation remains on p. 6, but no explicit corrected full-system debt Jacobian is given in the main PDF. Need the revised SI to verify `partial D'/partial D = alpha bf Af - eta` on the deficit-active face, with its active-set conditions. |
| E5: Main/SI recovery conflict | **Main-text correction independently supported** | p. 20 now reports minimum about 0.398 ha, endpoint 0.677 ha, recovery 0.46, T=400, dt=0.1. Independent reconstruction gives 0.398299, 0.677125, 0.463396. The cited revised Table S5 was not supplied. |
| E6: Unique equality point confused with unique switched equilibrium | **Substantially addressed in the main** | pp. 15–17 and Table 4 distinguish the fixed-demand surplus family, one-sided deficit spectrum, endogenous-population equality family, and history dependence. The abstract/conclusion restrict the no-fold result to the reduced equality relation. |

### Positive clarification about ceiling attraction

Proposition 2, p. 15, now restricts convergence to qmax to admissible histories with `q(0)>0`, and acknowledges the zero-history exception. This is mathematically appropriate for the selected projected quality law: q is nondecreasing and bounded; if its limit were strictly between zero and qmax, the delayed growth would eventually remain strictly positive, contradicting boundedness. If q reaches qmax it remains there. This is distinct from any raw smooth-DDE characteristic-root argument.

## 2. New numerical disclosures: independently checked

### 2.1 Reconstruction and limits

I implemented the p. 10 convention as follows: old current states at `t_(k-1)`, delayed inputs evaluated at `t_k`, linear interpolation of stored delay histories, projected Euler quality followed by clipping, and recomputation/storage of updated supply. Technology is off in these tests. The reconstruction is **not the author's code**. Its detailed assumptions are in `verify_c11.py`.

In frozen-demand checks, E is overridden as an exogenous constant; the demographic state is retained as a diagnostic and does not set that E. Exact historical implementation provenance cannot be established from a PDF description.

### 2.2 Recovery endpoint now reproduces

Scenario: `Ac0=1`, `Af0=0.6`, `q0=0.9`, `P0=2`, `chi_r=0.1`, `T=400`, endogenous demand.

| dt (yr) | Minimum Ac (ha) | Ac(400) (ha) | Recovery fraction |
|---|---:|---:|---:|
| 0.1 | 0.398299216 | 0.677124696 | 0.463395574 |
| 0.05 | 0.399784987 | 0.677713859 | 0.463048851 |
| 0.025 | 0.400516852 | 0.678008880 | 0.462885452 |

The dt=0.1 row matches the precision of p. 20. The old 0.828 endpoint is no longer printed in the main PDF. Changes in the minimum and endpoint under refinement should remain visible; they are not evidence of an exact, timestep-independent endpoint of 0.677.

The earlier C10 reconstruction sampled delays at the left step endpoint and gave a slightly different dt=0.05 endpoint. That implementation difference helps explain why the new, more explicit numerical specification matters. It does not prove the provenance of any historical C10 run.

### 2.3 Main refinement statistics largely reproduce

Frozen-demand run, T=100, comparison at matching grid times against dt=0.003125:

| Quantity | C11 reported dt=0.05 error | Independent | C11 reported dt=0.025 error | Independent |
|---|---:|---:|---:|---:|
| Ac, ha | 0.00221 | 0.00221430 | 0.00102 | 0.00102297 |
| B, gha | 0.00180 | 0.00179916 | 0.000831 | 0.000831026 |
| D, gha yr | 0.00200 | 0.00200063 | 0.000924 | 0.000924251 |
| P, cap | 0.000252 | 0.000244934 | 0.000118 | 0.000114441 |

Thus Ac, B and D agree to the stated rounding. The P errors are about 3% smaller in this reconstruction; this minor discrepancy remains unresolved and is another reason to attach the exact implementation and run configuration. It does not undermine the much larger improvement in numerical consistency.

### 2.4 Projection and clipping tests

The independent projected-before-update and clip-only versions give exactly equal stored arrays in the tested dt=0.05, T=100 cases at quality delays 5, 20 and 40 years. The 20/40 cases also agree exactly with each other. This supports the finite-case claim while remaining distinct from verification of the author's arrays.

For the baseline exact quality path `min(1,0.9+0.0072t)`, independent piecewise-linear contact errors decrease from about `7.1111e-5` at dt=0.1 to `8.8889e-6` at dt=0.0125. This supports the described refinement. Do not infer a universal error estimate or convergence theorem for every switched delayed scenario; the PDF correctly avoids that inference.

## 3. Remaining mathematical corrections

### R1. Proposition 1 still contains an invalid necessity claim and an incompatible transient closure

**Location:** pp. 12–13, Proposition 1(i)–(ii).

The sentence that the conversion term determines the sign of net B' **“only if”** maintenance balances retirement and quality is unchanged is too strong. Those are sufficient conditions for other terms to vanish, not necessary conditions for agreement of signs.

**Concrete admissible counterexample in the stated frozen-debt/quality regime:**

- `Af=1.2`, `Ac=0.8`, `Ar=0.5`, `q=1`, `E=1.2`, `bf=0.85`, restoration off;
- B=1.06, hence uc=0.14/0.85=0.164705882 and the capital-floor limiter is inactive;
- conversion contribution to B' = `0.8*(0.14/0.85) = 0.131764706`;
- maintenance imbalance = `0.06*0.5 - 0.05*1.2 = -0.03`;
- maintenance contribution = `-0.0255`;
- net B' = **+0.106264706**, with the same positive sign as conversion despite nonzero maintenance imbalance.

Also, maintaining `M=mu Ar-eta_f Af=0` throughout active conversion is not a closure inherited from Eqs. (6)–(8). With restoration off,

`M'=-(mu+eta_f)M-eta_f uc`.

At M=0 and uc>0, M'<0. Thus the proposed balanced-maintenance transient in Proposition 1(ii) does not remain in that submanifold under the displayed land dynamics.

**Required repair:** Change “only if” to a sufficient-condition formulation such as “in particular, when.” Either make the reduced statement explicitly instantaneous, drop its claimed transient implication, or define a genuinely different counterfactual flow closure. Proposition 2's separately derived maintenance-balanced *equilibria* are not the problem and should be retained.

### R2. The B-only safety impossibility claim remains false without controller restrictions

**Location:** pp. 27–28, §4.3.

The statement that a governor monitoring only total B cannot guarantee the capital floor does not follow from non-identification. A constant stop control uc=0 is a B-only control in the mathematical sense and gives Ac'=Rrc>=0 from safe initial conditions.

Furthermore, the displayed conversion rule already guarantees

`y'=Ac' >= -y/tau_conv`, where `y=Ac-Amin>=0`.

Consequently `y(t)>=y(0)exp(-t/tau_conv)`, so the capital floor is built into the admissible action law independently of what aggregate observation is available. A stop triggered exactly at the asymptotically approached floor is not an additional demonstrated safety mechanism in that continuous model.

**Required repair:** State that B alone cannot reconstruct Ac or implement arbitrary Ac-dependent policies. If an impossibility result is wanted, specify the permitted controller class, initial uncertainty and competing provision objectives. Distinguish an information deficit from universal control impossibility.

### R3. Rounded demands still accompany mismatching debt equilibria

**Location:** p. 17.

C11 retains analytic equilibria 1.19/5.38 and integrated results 1.21/5.39 at printed demands 1.158/1.238. The equilibrium condition itself implies:

| Exact demand E | Debt equilibrium D* |
|---|---:|
| 1.158 | 1.18576698 |
| 1.238 | 5.37506262 |
| Eceil+0.02 = 1.1584090909... | 1.20965490 |
| Eceil+0.10 = 1.2384090909... | 5.39453751 |

The last pair explains the reported integrated values strikingly well. This is strong evidence of an input-rounding inconsistency, not evidence of a new dynamical effect. I have not verified the actual author-run inputs.

**Required repair:** Use the same unrounded demands in both calculations, publish those inputs, and regenerate the comparison.

### R4. Typed reserve-floor enforcement remains unspecified

**Locations:** Table 1, p. 9, versus enforcement list p. 10 and Eqs. (6)–(9).

The table calls Armin=0.10 a domain constraint, but the enforcement list does not explain how this strictly positive reserve floor is preserved. Reconstructing reserve as total minus other areas preserves accounting, not this lower bound.

For example, `Af=0.1`, `Ac=2.3`, `Ar=0.1`, `q=1`, `D=0`, `E=1` gives B=0.2, restoration zero, and

`Ar'=-0.06*0.1+0.05*0.1=-0.001 ha/year`.

Thus the raw flow leaves the declared reserve-floor domain. This is a domain counterexample, **not a claim that a reported baseline run violates the floor**.

**Required repair:** If the reserve floor is merely monitored and inactive in all reported scenarios, say so. If it is a hard invariant constraint, specify the flow-limiting/projection rule and verify it. Do not introduce a numerical adjustment without documenting its effects on area conservation and the equations.

### R5. Smaller scope and dimensional corrections remain

- **Identifiability, p. 12:** Qualify the bG,c/rho_c product non-identification as applying to the supply observation relation alone. Informative quality *trajectories*, with known delayed inputs in the interior, can identify rho_c from the quality equation and thereby permit separation. Cross-sectional non-identification and dynamic identifiability are different questions.
- **Additive comparator, p. 19:** The coefficient multiplying D in `bf=bf0+Tb-alpha D` must have yield-per-debt units, not the same units as multiplicative alpha. Give it a distinct symbol/units or explicitly state the redefinition. The repair is small but mathematically necessary.
- **Debt crossover, p. 19:** The proof now correctly compares a limiting sustained shortfall, and keeps D0 in the bound. However, the subsequent assertion that the minimum-area constraint acts before debt exceeds the technology cap requires scenario/demand qualifications; E is not globally bounded by baseline B. Treat it as an observation about specified runs, not a consequence merely of the crossover exceeding baseline B.
- **Finite-grid monotonicity:** Table 4 is appropriately empirical; ensure Fig. 1c's caption and p. 17 also say “in the tested runs” rather than assert a general comparison theorem.
- **Supply kernel versus quality velocity:** Eq. (2) evaluates raw Gc at *current* q, while Eq. (10) uses a delayed projected velocity. Retain this distinction explicitly: the supply kernel is not generally equal to q'. Changing Eq. (2) to use projected velocity would be another model change, not a notation repair.

## 4. Revised SI is essential to close the audit

Only the main PDF was attached. Do not infer that the old SI has been corrected merely because the main text cites new sections and tables.

Request the version-matched SI and verify:

1. Full deficit-active debt Jacobian and all relevant active-set matrices.
2. Population-delay linearisation and removal of the Hutchinson argument.
3. Projected-law well-posedness/invariance statement, without transferring raw-DDE stability claims.
4. Removal of the old drawdown reserve assertion of at least 0.80 ha (a listed sweep starts at 0.72 ha).
5. Gate-comparison maximum Ac below its own initial Ac, with inclusion of t=0 and endpoint windows specified.
6. Initial-debt term and bound-versus-stationary-equality distinction in the log-channel argument.
7. Boundary debt transient distinguished from the equilibrium fast-land substitution.
8. Recovery tables and all main/SI links generated from common run outputs.
9. Reproducible inputs/methods for the newly reported forest/fish recovery-fit medians, or removal of those unsupported fit summaries. The caveat that records do not calibrate ECOMOD does not itself verify the quoted 30-year/5.6-year fit statistics still repeated on p. 7.
10. Threshold timestep sensitivity, exact masks/events, gate summaries, comparator outputs and wave-run configurations.

The main p. 30 still promises future code/data deposition rather than providing an immutable code/run archive. Closing numerical provenance requires an actual version identifier and run artifacts, not a statement that deposition will occur.

## 5. What to do next

1. **Keep the selected projected, uncalibrated-index model.** Its main specification and evidence limitations are materially improved.
2. Correct R1–R4 and the small scope/unit issues; these do not require selecting a new ecological mechanism.
3. Supply the revised SI and the generator used for C11, with histories, exact inputs, interpolation and update order.
4. Regenerate main/SI comparisons together, especially the debt-root example and any corrected gate extrema.
5. Archive the code, environment, configurations and numerical output tables. Distinguish historical C10 provenance from newly reproducible C11 outputs; recovering every old script is not a prerequisite to an honest revision.

**Disposition:** Do not reject the revision as unchanged, and do not certify all audit findings as resolved. The main conceptual repair is successful; targeted mathematical corrections and SI/code verification remain before closing the audit.

## Audit artifacts and reproducibility

- `verify_c11.py`: independent reconstruction and counterexamples.
- `c11_verification_results.json`: full numerical outputs.
- `c11_verification_stdout.txt`: printed outputs.
- `c11_extracted_text.txt`: search/reference extraction of the supplied PDF; extraction has font/ligature artifacts and is not an authoritative replacement for the PDF.
- `README.md`, `requirements.txt`, `artifact_manifest.json`: run instructions, dependencies, integrity.

No original author code, revised SI, complete source/build bundle or run manifest was supplied. No new empirical source datasets were used in these C11 checks; previously verified NFA statistics were not re-audited from scratch. Companion-paper theorem claims and full PDF layout were outside the selected review scope.

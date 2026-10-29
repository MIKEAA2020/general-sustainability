# Audit of the governance paper cited in ECOMOD C17

**Date:** 29 October 2026  
**Target:** Amin Abaee, *Governance delay and the stability of harvested stocks: mobilising and protective feedback rules, and the review interval as a design parameter*, v41, 45 pages.  
**Disposition:** substantive corrections warranted; the central local channel contrast survives the checks performed. The paper is not an independently verified global RFDE bifurcation result or an empirically validated governance model. C17’s limited qualitative citation remains defensible.

## 1. Version, evidence and audit boundary

C17 main and SI cite the PDF at commit `2efaa62083f2007dec3446c15c475af88f0925f3`. The latest numbered `paper4_delay_dynamics` manuscript on main at the audit’s version check, HEAD `8daaba761a133559e55bf60c4c5e58e262c0120f`, is **v41**. Its PDF and TEX blobs are identical to the cited version. This audit therefore examines the actual cited paper, not an older deposited version or an uncited replacement.

- [Pinned PDF](https://github.com/MIKEAA2020/general-sustainability/blob/2efaa62083f2007dec3446c15c475af88f0925f3/arena%20agent%201/paper%20rewrites/latex/paper4_delay_dynamics_v41.pdf)
- [Pinned TEX, with line numbers](https://github.com/MIKEAA2020/general-sustainability/blob/2efaa62083f2007dec3446c15c475af88f0925f3/arena%20agent%201/paper%20rewrites/latex/paper4_delay_dynamics_v41.tex)
- [Pinned supplementary v8](https://github.com/MIKEAA2020/general-sustainability/blob/2efaa62083f2007dec3446c15c475af88f0925f3/arena%20agent%201/paper%20rewrites/paper4_supplementary_v8.md)

The audit checked equations, selected proofs, local spectra, sampled-data operators, certification records and C17 citation use. Fourteen governance source files were retrieved and Git-blob/hash checked, including the manuscript, SI, model, Hopf interval code/output, both discrete-fold certificates, and campaign/status records. Their identities are in `data/source_registry_R01.json`.

**New independent work:** an equation-level implementation with no imports from the paper’s computational code; interval sign/derivative and phase-image checks for the two principal frequency roots; an interval-validated mixed-delay counterexample; sampled-map calculations; and a second native-ZOH implementation through direct ODE integration. **26 tests pass normally and 26 under `python -O`.** These are software checks, not empirical validation.

**Not rerun:** the long-horizon nonlinear DDE campaigns, global periodic-orbit continuation, fold Krawczyk pipelines, Lyapunov-coefficient calculations, or maturation-delay campaign. The fold findings below distinguish inspection of deposited records from independent re-execution. This is not an exhaustive line-by-line proof audit, figure-production audit, or novelty/literature review.

## 2. What reproduces

The equilibrium calculation, even-pairs cancellation and local characteristic structure agree with the displayed model. At Candidate A:

- `E* = 2.089623397737668`, `N* = 89.55188301131166`.
- `A_N = -0.0179103766022623`, `C_E = -0.0595180098425612`, `C_Z = 1.785018714984997`.
- The cancellation `B_E A_N = B_N A_E` gives `L(lambda) = B_E lambda`.
- The characteristic equation is `P(lambda) - C_Z B_E lambda exp(-lambda tau) = 0`, with `P=(lambda-A_N)(lambda+d)(lambda-C_E)`.

### Local delay crossings

| Family | First fundamental crossing, years | Second fundamental crossing, years | Audit status |
|---|---:|---:|---|
| A, gated | 3.6661490142741 | 150.3584773101414 | Floating-point agreement plus independent interval checks of scalar roots/phase images |
| A, ungated | 6.8814106304780 | 132.3749034544013 | Floating-point reproduction |
| B, gated | 5.5128407314435 | 80.4245267142273 | Floating-point reproduction |
| B, ungated | 6.2135987340182 | 76.2906356879514 | Floating-point reproduction |

For gated A, the frequencies are approximately `0.02519154358` and `0.03943657756` per year. The real-part crossing derivatives are respectively `-9.48314e-5` and `+5.50936e-6`, consistent with stabilisation at the lower crossing and destabilisation at the upper crossing.

The independent interval calculation uses the exact registered decimal parameters and interval `log(2)`. It proves opposite endpoint signs and a derivative excluding zero for each of two positive scalar-root boxes, then encloses their phase-derived delays **inside the published delay intervals**. It does not certify nonlinear RFDE Hopf bifurcations or their first Lyapunov coefficients. Decimal interval endpoints in the output are rounded outward using exact integer arithmetic.

### Protective endpoint

The quota-tracker coefficients reproduce: `C_E = -0.8503361404822591`, `C_Z = -1.661701896635287`. Its modulus cubic has coefficients

`[1, 0.7633923334002992, 0.028946201580653245, 9.277921683946986e-6]`.

All are positive; the undelayed Jacobian is Hurwitz and the zero root is excluded. The paper’s pointwise, calibrated **delay-independent local stability argument survives**. The numerically located protective gain maximum is approximately `0.0801130`, in agreement with the text. This is not a theorem for every decreasing quota law or for arbitrary mixed channels.

### Reviewed operators

| Channel / implementation | Annual spectral radius | Located crossing(s), years |
|---|---:|---:|
| Mobilising / Euler review | 1.0005452356 | 47.5359823; 79.1426878 |
| Mobilising / exact held-measurement review | 1.0003506565 | 6.50129495 |
| Mobilising / native signal ZOH | 1.0003092332 | 6.72785007 |
| Protective / Euler review | 0.9837962340 | 2.30635442 |
| Protective / exact held-measurement review | 0.9838095183 | none found on the independent grid, 0.2–300 years |
| Protective / native signal ZOH | **0.9838194826** | none found on the independent grid, 0.2–300 years |

The crossing locations are floating-point results, not interval-certified unit-circle or nonlinear Neimark–Sacker bifurcations. The independent grid contains 1,501 points per channel/implementation. A finite grid cannot exclude arbitrarily narrow instability windows.

The model’s undelayed mobilising equilibrium is already weakly unstable. Annual review inherits that instability; it is not evidence that introducing annual review destabilises an otherwise stable equilibrium. The paper itself recognises this distinction in its consolidated interpretation. The frozen-effort exact update and native ZOH are different controllers, and **the paper explicitly discloses that difference**.

## 3. Material findings

### H1 — The mixed-channel proof overreaches; protective-delay independence outside the certificate is false

**Location:** Corollary 6.1 proof, TEX approximately lines 1562–1574; related closing language in Corollary 5.1.

Corollary 6.1(iii), as formally stated, is sound: if the undelayed interpolation is Hurwitz, the zero root is excluded and strict weighted small gain holds, both delays are harmless. Its proof then goes further, saying that instability outside this certified region “is independent of the protective delay there.” That extra conclusion does not follow and admits an explicit counterexample within the displayed interpolation.

Set the exact decimal weights and delay to

- `chi_m = 0.9988`, `chi_p = 0.0012`;
- `eta_p = 0.914` as in the paper;
- `tau_M = 0` years;
- `C_E = chi_m C_E^mob + chi_p C_E^prot`, with the calibrated common equilibrium.

At `tau_p = 0`, an independent interval calculation verifies all cubic Routh conditions. The equilibrium is therefore locally exponentially stable. The oscillatory eigenvalues are approximately

`-5.73721526e-5 +/- 0.02789961315 i`.

Changing **only** `tau_p` to `110` years produces a characteristic root near

`+6.28594815e-6 + 0.02789563101 i`.

An independent two-dimensional real Krawczyk calculation strictly includes this root in a box whose real component is entirely positive, with contraction norm below `1.03e-16`. Thus this is a validated right-half-plane root, not merely a plotted root-finder trace. The common coefficients and mobilising delay have not changed.

The witness has weighted gain approximately `1.006606 > 1`, so it **does not contradict Proposition 5.2**, the low-weight certificate, or the pure-protective theorem. It refutes the proof’s extension beyond that certificate. Numerically, the protective-delay crossings in this example occur near `86.0259` and `132.0765` years; those locations were not interval-enclosed here.

For this explicit calibrated interpolation, analytic maximisation reduces to a unique positive root of `2x^3 + (A_N^2+d^2+C_E^2)x^2 - A_N^2 d^2 C_E^2 = 0`. The resulting *numerical* small-gain boundary is approximately `chi_m=0.9981597676`; the undelayed Routh boundary is approximately `0.9989651942`. These values quantify a sufficient margin, not a general physical onset weight.

**Required correction:** retain the conditional theorem; remove the outside-region independence assertion. Explain that a protective summand which is harmless by itself need not make its delay harmless when combined with a near-critical mobilising loop. The long delays and near-pure mobilising weight in this witness are mathematical evidence, not estimates of a real institution.

### H2 — “Every consistent periodic-review scheme restabilises” is not proved

**Location:** Section 7 scheme-dependence remark, approximately TEX lines 1810–1835.

Small-step consistency fixes `(M(T)-I)/T` as `T -> 0`; it does **not** constrain an arbitrary implementation’s large-step behaviour. The proof transfers the large-interval limit of an exact hold to “every consistent” scheme without an additional hypothesis. The Euler map, for example, is consistent yet loses stability again near 79.143 years. That fact does not by itself disprove the weaker claim that every such scheme has *some* stable interval; it does show why the stated large-step argument cannot prove the universal conclusion.

A rigorous narrower conclusion is available for the **two named exact maps**. Since `A_N`, `-d` and `C_E` are negative, the native matrix `A_Z` is Hurwitz. Its limiting map is `-A_Z^{-1} C_Z e3 e2^T`. The cancellation makes `e2^T A_Z^{-1} e3=0`, so this rank-one limit has only zero eigenvalues. For the frozen-effort exact map, the held flow tends to `u e3^T`, with `u=(-A_E/A_N,0,1)^T`; the exact review sends this to `(-A_E/A_N,0,0)^T e3^T`, again a rank-one, nilpotent limit. Spectral-radius continuity gives eventual local stability for each of these exact maps.

**Required correction:** state/prove eventual stability for the specified operators, or add sufficient restrictions defining an admissible wider implementation class. Keep the finite-grid evidence distinct from an all-cadences claim. The tight 6.50–6.73-year comparison concerns the selected exact realizations, not every first-order-consistent implementation.

### H3 — The cited “2–13-year governance-lag distribution” is not substantiated by the audited reference text

**Location:** Sections 9.3, 11.4 and 11.7; TEX approximately lines 2520–2525, 2933–2937 and 3064–3068.

The manuscript repeatedly attributes a documented `2–13`-year governance-lag distribution to Hocherman, Trop and Ghermandi (2025). The referenced article is a review of **101 studies**, not a fitted fishery institutional-delay distribution. Its main text discusses heterogeneous response and implementation lags: six- and seven-year policy-preparation examples, a twelve-year ratification example, a 10–15-year integration example, and science-policy examples extending from 13 to 55–58 years or longer. These are different event definitions and domains, not an exchangeable sample estimating this model’s `tau_M` or `tau_p`.

The article identity is verified by [2](https://pubmed.ncbi.nlm.nih.gov/40610782/); the checked [full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC12569336/) does not establish the stated distribution. Its supplementary PDF link returned HTML rather than a PDF in this audit; an alternate CDN retrieval failed. Consequently this finding is **a failed support check requiring an exact source/table/data identification**, not proof that no relevant underlying data can exist.

This matters because the manuscript uses the overlap to single out fast-maturing small pelagics as a predicted exposed class. The model-derived bands can motivate a test, but the inspected citation does not supply the claimed empirical distribution or a species-specific calibration.

**Gap closure, not just softer wording:** identify the exact cited dataset or assemble a traceable event-level dataset with separately defined recognition, decision, implementation and ecological-response dates. Estimate institutional delays for the chosen fisheries, with censoring and uncertainty, before testing overlap with independently estimated biological bands. Do not replace the missing distribution with a convenient range extracted from unlike examples. The model’s approximately eight-year cycle period is its own prediction, not an empirical median reported by this review.

### M1 — The native protective annual spectral radius is wrong in two places

**Location:** Section 7 scheme-dependence remark and consolidated table, approximately TEX lines 1841–1844 and 1880–1881; PDF pages 23–24.

The displayed native-ZOH operator gives

`rho(M_ZOH(1)) = 0.9838194826251283`, **not `0.9928`**.

This was checked through an augmented matrix exponential and, independently, direct high-accuracy integration of each variational basis vector while holding the sampled signal fixed. The other named crossing locations reproduce, making an operator-wide reconstruction error unlikely.

**Effect:** quantitative correction; the annual protective stability conclusion remains unchanged. Correct both occurrences and trace the provenance of the printed number.

### M2 — “Below” reverses the small-gain certificate’s implication

**Location:** Section 5.4, TEX approximately lines 1262–1272; PDF page 16.

The text says the actual onset may lie “below” the sufficient-condition radius. Under the stated stable-reference hypotheses, the certificate excludes Hopf below that radius. Onset cannot be earlier than a valid exclusion boundary; failure of the certificate above it still does not imply onset.

**Required correction:** “at or above the boundary of the certified region, and potentially substantially above it,” with the distinction between a chosen conservative radius and a maximal sufficient bound preserved.

### M3 — Iso-gain phase identity has the wrong sign in its proof

**Location:** Proposition 6.1 proof, approximately TEX lines 1446–1459; PDF page 18.

From `P/Q = exp(-i omega tau)`, the phase identity is `-omega tau = arg(P/Q) mod 2pi`, not `omega tau = arg(P/Q) mod 2pi`. The earlier phase formula and the reported shifted crossings are consistent with the correct convention.

The independent sign-flip calculation reproduces approximately `128.3743728` and `70.6965784` years. This is a repairable proof typo, not a failed numerical sign-flip result.

### M4 — A rank-one update row is treated as possibly invertible

**Location:** Theorem 7.1 ordering comparison, approximately TEX lines 1657–1665; PDF page 21.

`R_0=e3(C_Z e2^T+C_E e3^T)` has rank one and cannot be invertible as a 3-by-3 matrix. The relevant update factor is `R(T)=I+T R_0`, not `R_0`. The products `R(T)F(T)` and `F(T)R(T)` have identical characteristic polynomials by the AB–BA determinant identity; the held flow is itself invertible, so a similarity argument is also available without assuming invertibility of the rank-one row.

**Effect:** repair the proof and keep the stated timing convention. This does not invalidate the displayed monodromy or establish equality of nonlinear maps.

### M5 — The complete upper bistability interval remains unclosed

**Location:** Section 8.2, especially the regime-(iv) description and the paragraph after Figure 2; PDF pages 25–27.

The records support a discrete upper fold near 64.4023 years and a short stable returning segment through about 64.438 years. The manuscript also explicitly acknowledges that the connection from this segment to the captured face-riding object near 148.6 years is unverified. That disclosure is important and should not be erased.

However, describing the entire interval `(64.4023,150.3585)` as mathematical bistability of that stable returning arm is stronger than these disconnected records establish. The intervening roughly 84-year gap could contain additional turns or stability changes. The inspected records do not resolve it. This is not evidence that the branch must terminate, nor that the five-regime numerical reading is false.

**Substantive closure:** continue the stable arm across the gap, track all relevant nontrivial multipliers and branch turns, and establish or reject the connection to the captured object. Until that computation is done, distinguish local fold/arm evidence, distant basin-capture evidence and the unresolved connection. Finite-history “settles” outcomes are not proofs of global monostability.

### Additional low-priority inconsistencies

1. **Loop gain:** Proposition 6.1 quotes `1.016`; the exact registered gated-A coefficients give approximately `1.0192213`. This does not change the `>1` conclusion.
2. **Tested interior interval:** Section 8.3’s failure-to-capture range `5.57 < tau < 148.3` includes `tau=5.575`, where Section 8.2 explicitly records H2 capture. Use the actual tested grid or the post-lower-fold range rather than an encompassing interval that includes a known counterexample.
3. **SI status:** S12 leaves interval transversality/curvature conditions “open,” whereas both deposited discrete certificates contain nonzero intervals for the discrete nondegeneracy constants. Clarify **discrete conditions obtained / continuum conditions still open**. This ambiguity does not establish a failed discrete certificate.

## 4. What the fold records do—and do not—certify

### Lower fold

The inspected record reports a successful Krawczyk inclusion on the `m=64` Moore–Spence system, with delay enclosure

`[5.587236198689235, 5.587236198690484]`.

Its first inclusion has positive gap `7.992e-10`; the two discrete nondegeneracy intervals exclude zero. A subsequent failed tightening iteration does **not** cancel the earlier successful inclusion. The `m=64/96/128` locations agree to about `2.69e-11`.

### Upper fold

The inspected record reports successful inclusions for the `m=64` system and delay enclosure

`[64.40232720336789, 64.40232720337167]`.

Both discrete nondegeneracy intervals exclude zero. The `m=64/96/128` locations differ by about `5.53e-7`. The source records an unsuccessful original frozen-box attempt followed by a documented widened/deviation-box calculation; that history is not itself evidence that the successful later inclusion is invalid.

**Interpretation:** these are certificate records for finite-dimensional collocation systems. They are not continuous-delay fold enclosures, and cross-order agreement does not become one. In particular, the upper fold’s discretization shift is much larger than its tiny `m=64` interval width; those widths quantify different things. The main paper generally discloses this distinction correctly.

**Audit limit:** these fold certificates were inspected, not independently recomputed. Off-grid residual control, continuous-delay lifting and a complete global basin classification remain open. The audit supplies no new global fold theorem and no verification of the reported nonlinear Lyapunov coefficients.

## 5. C17 citation fidelity

| C17 context | Use of governance companion | Audit judgement |
|---|---|---|
| Main, “Policy controls and limits,” around line 533 | Surplus- and deficit-gated restoration “echo” protective/mobilising feedback | Acceptable explicitly qualitative analogy; it does not inherit the governance paper’s stability theorem |
| Main, “Relation to prior work,” around line 537 | Companion studies institutional feedback; C17 delays are ecological regeneration/demographic response | Correct separation of mechanisms |
| SI, “Institutional signature,” around line 468 | Related work distinguishes the two feedback classes; C17 states its own restoration-gate behaviour | Acceptable scoped comparison |

The checked passages do **not** transfer the 6.5-year review threshold, the governance Hopf/fold locations, or an empirical calibration into ECOMOD. The defects above therefore do not invalidate C17’s own equations or gate comparison. C17 should not later be strengthened into a universal claim that the protective sign makes all mixed-channel delays harmless.

The earlier DOI-link audit remains applicable: the verified Zenodo governance deposit is v30, not this cited v41. Retaining the exact GitHub v41 citation is preferable to silently substituting an older DOI-linked manuscript.

**No governance manuscript, C17 manuscript, declaration, bibliography or deposit has been edited by this audit.**

## 6. Gap closure in dependency order

1. **Repair the mathematical boundary and numerical record now.** Correct the mixed-channel proof using the validated witness; retain the valid certificate. Correct the native annual radius, phase sign, rank-one argument and certificate-direction sentence. Replace the unsupported all-implementations inference with the named-operator limit argument or an actually proved wider theorem.
2. **Repair the empirical evidence chain before ecological targeting.** Locate the precise 2–13-year dataset or build a provenance-rich event table. Separate deployment delay from review cadence, recognition lag and ecological recovery lag. Only then estimate the relevant institutional parameters for an identified fishery; independently estimate biological rates/maturation and measurement mappings. Test joint parameter uncertainty rather than asserting exposure from a generic review range.
3. **Close the upper branch gap computationally.** Continue the stable arm from 64.438 years through the unresolved region; use mesh refinement and multiplier tracking, and investigate the captured object without assuming it is the same family. Check numerical saturation/gate handling and long transients rather than inferring branch identity from basin amplitude alone.
4. **Lift discrete folds to the DDE.** Obtain validated off-grid residual and inverse/operator bounds, verify the phase condition and continuum nondegeneracy, and lift both finite systems. This requires new computation, not relabelling existing mesh agreement as validation.
5. **Validate nonlinear bifurcation and governance safety separately.** Verify nonlinear Hopf/Neimark–Sacker hypotheses where claimed, then address inter-review stock floors and disturbances. A local contraction radius is not a safety certificate.

Steps 3–5 are genuine remaining computations. The audit has not completed them. Step 2 is a data-identification and estimation task; no stock/institution time series was fitted here. The paper is useful as an analysable mechanism and candidate test programme, but the checked evidence does not yet validate its thresholds in a field institution.

## 7. Reproducibility package

- `src/verify_governance_R01.py`: independent equilibrium, cubic, phase, crossing, gain, reviewed-map and scalar interval calculations.
- `src/check_mixed_delay_R01.py`: exact-parameter mixed-channel witness, interval Routh test and complex-root Krawczyk checks.
- `src/interval_decimal_R01.py`: outward decimal serialization.
- `src/test_governance_R01.py`: 26 tests, including native-ZOH comparison with a direct ODE solver.
- `data/verification_results_R01.json`, `data/mixed_delay_check_R01.json`: numerical results and explicit certification boundaries.
- `data/source_registry_R01.json`: pinned source identities and C17 source hashes.
- `data/external_reference_check_R01.json`: checked review reference, selected context and retrieval limitation.
- `data/tests_normal_R01.txt`, `data/tests_optimized_R01.txt`: actual test output.

Run commands and pinned dependency versions are in `README_R01.md` and `requirements_R01.txt`. The manifest covers the audit files, not a claim that all cited source computations were rerun.

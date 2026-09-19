# Cover Letter — Paper E1 (resubmission to *Fisheries Research*)

**Title:** Forecasting biomass under structural non-stationarity: an out-of-sample evaluation of surplus-production models for Northern cod (Gadus morhua)
**Author:** Amin Abaee (Independent Researcher; ORCID 0000-0002-0019-1842; amin_abaee@ut.ac.ir)
**Journal:** *Fisheries Research*
**Date:** September 18, 2026

---

Dear Editor,

I resubmit the manuscript **"Forecasting biomass under structural non-stationarity: an out-of-sample evaluation of surplus-production models for Northern cod"** for consideration in *Fisheries Research*, following your initial decision. The revision responds directly to the three concerns raised at that stage; I have addressed two by clarifying and specifying, and the third — the decisive one — by running the demanded test empirically.

## What the paper intends to be

The paper is a **forecast-comparison study**, not a proposed assessment method and not a sustainability verdict. Its intention is narrowly stated: whether adding structure to a surplus-production ladder improves out-of-sample forecasts of the quantity that management advice actually consumes — spawning stock biomass — is an empirical question with a stated burden of proof. The manuscript tests that question on the canonical demanding case (Northern cod, NAFO 2J3KL) under a scoring rule fixed before the scores were read, with persistence treated as an active competitor, not a scaling denominator. The claims are deliberately conservative: the negative result is scoped to the fitted estimator family and ladder, and the paper explicitly does not conclude anything about the stock's sustainability or about the adequacy of historical management decisions.

## Response to the three concerns

**Concern 1 — Technical and computational specification.** We understood the first concern as: the ladder could not be independently reconstructed from the manuscript. The revised paper carries a dedicated **Appendix A (A.1–A.7)** that consolidates the full specification in one place: the map equations, per-window estimation mechanics (bounds, multi-start, the frozen autoregressive rule, catch handling), the rolling-origin machinery and metrics, the executable retention rule, and the uncertainty layer (Diebold–Mariano with Newey–West HAC; moving-block bootstrap; 20,000 replications, seed 0). Together with the reproducibility package in Supplementary SI-6 and the deterministic campaign scripts archived with the revision, every number in the results is regenerable byte-for-byte.

**Concern 2 — Scope and status of the benchmark.** We understood the second concern as a misreading risk: that the manuscript might be taken to propose a new assessment method for the stock. The opening section now states the scope in its first paragraph: the ladder is a scored test of structural additions against a demanding naive baseline, in the tradition of persistent-benchmark diagnostics (MASE; Hyndman and Koehler, 2006) that assessment science already treats as canonical. Nothing in the paper is offered as a replacement assessment tool, and no management advice is issued from it.

**Concern 3 — The choice of scoreboard.** We understood the third — and in our view correct — concern as: the verdict might depend on the smoothed assessment reconstruction as target rather than on the models themselves; a raw monitoring series could tell a different story. The first revision could only reserve this question for follow-up. **The revision now answers it empirically.** Section 3.8 scores the same frozen ladder, under the same pre-registered rule, against the raw autumn research-vessel survey index (1983–2015, 33 consecutive years; Schijns et al., 2021, Table 3), on origin sets identical to the assessment runs. The retained set is empty on the monitoring target as well: persistence records 120.5 kt-equivalents at one year against 156.3–371.3 for the structural ladder, and 249.2 at five years against 355.5–880.5 — the persistence advantage *increases* on the raw index (+29.8% vs +17.1% at one year; +42.7% vs +9.0% at five years). Section 4.3 explains the mechanism explicitly: smoothing a fixed target and substituting a different, noisier target are different interventions; observation noise compounds through iterated structural forecasts while persistence pays only the bounded one-step noise floor. The conversion constant, the one non-separating cell (the stock-flow module at one year, whose gap remains a deficit either way), and the verdict-level invariance of every outcome to that constant, are all documented in the text and SI-7. The headline therefore changed form: **no surplus-production module is retained on either a reconstructed or a monitoring target.**

## What changed since the first submission

1. **Scope clarifications** in §1 and the abstract (concern 2), with the paper's intention stated before any method.
2. **Appendix A.1–A.7** technical/computational specification (concern 1); SI extended to v5, including the reproducibility inventory.
3. **A new empirical object**: the pre-registered survey-index campaign (§3.8, Table 12b; design frozen before any survey score was read), the target-contrast mechanism discussion (§4.3), and the machinery-fidelity, determinism, and scale-sensitivity verification recorded in SI-7.

The manuscript is self-contained; all inputs, scripts, and result files are archived (https://github.com/MIKEAA2020/general-sustainability). The work is original, is not under consideration elsewhere, and I have no conflicts of interest.

I believe the revision has converted an arguably *target-dependent* negative result into a *target-robust* one, and that this is now squarely within the journal's remit. Thank you for your consideration.

Yours sincerely,

**Amin Abaee**
Independent Researcher
ORCID: 0000-0002-0019-1842
Email: amin_abaee@ut.ac.ir

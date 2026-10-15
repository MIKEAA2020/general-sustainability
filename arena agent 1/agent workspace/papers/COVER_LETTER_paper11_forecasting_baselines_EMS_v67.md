# Cover Letter — paper11 (v67)

**Title:** Forecasting against naive benchmarks: a scored test of process-based modules on Northern cod and the Edwards Aquifer
**Author:** Amin Abaee (Independent Researcher, Tehran)
**Journal:** *Environmental Modelling & Software*
**Article type:** Research paper (main text 49 pp. preprint format, 10 tables, 8 figures, two propositions with proofs; Supplementary Information S1–S24, 35 pp.)
**Keywords:** forecast evaluation; persistence benchmark; rolling-origin cross-validation; surplus production; groundwater balance; model retention; Diebold–Mariano test; Northern cod; Edwards Aquifer

---

Dear Editor,

Please consider the enclosed manuscript for publication in *Environmental Modelling & Software*.

**The question.** Process-based modules are added to environmental forecasting models on the assumption that mechanistic fidelity buys accuracy. The paper treats that assumption as a hypothesis and scores it on two unrelated managed systems with the same instrument: a ladder of nested modules, scored by rolling-origin RMSE against last-value persistence and the training mean, under a retention protocol disclosed before the scores were read. The systems are a surplus-production ladder on the spawning-stock biomass of Northern cod (two assessment series, 1983–2015 and 1954–2024) and a one-pool water-balance ladder on annual-mean head at the Edwards Aquifer index well J-17 (1934–2023). The two systems are never pooled; each is scored under its own protocol.

**The result.** No structural module is retained on either system. On cod, persistence has one-year RMSE 98 kt against 115–196 kt for the modules, the deficit is carried by the 1991–1995 collapse that no member of the class can reproduce at the recorded catch (Proposition 1), and under known truth the rule retains a true autonomous module in 97% of replicates, so the verdict is a property of the series rather than of the test. On J-17, a balance that persists last year's recharge loses to persistence (14.70 against 13.23 ft) because annual recharge is near-white (r = 0.17) while the head increment tracks it (r = 0.74); a univariate AR(1) is retained by a 0.39-ft margin whose bootstrap interval covers zero; the same map given the realised fluxes nowcasts at 7.55 ft; and the training mean beats persistence from two years ahead.

**What is new.** An elementary decomposition (Proposition 2) separates a one-step structural forecaster's gain on persistence into a mechanism term and a driver-substitution term, and shows that a persisted driver with lag-one autocorrelation below one half loses to persisting the predictand; a companion remark gives the horizon at which climatology overtakes persistence as the first horizon at which the predictand's autocorrelation falls below one half, which the aquifer record follows to within 0.1. The two systems fail on the two different terms of that decomposition — the cod modules on misspecification, the aquifer module on driver substitution — and the paper corrects an earlier combination of the two studies that had attributed the cod failure to a weakly autocorrelated driver (the computed autocorrelations are 0.71–0.91).

**Why it fits the journal.** The paper is about how environmental models should be evaluated before their mechanisms are trusted for forecasting: a reusable protocol (information set at the origin, nested comparators, naive benchmarks, pre-stated hurdles, uncertainty on every load-bearing margin, and a power study of the rule itself), applied across a fishery and an aquifer with full code and data. Everything needed to re-score either ladder is archived.

**Protocol status, stated plainly.** Both designs are fixed computational protocols with recorded execution orders — the aquifer protocol frozen and dated before scoring, the cod protocol established from the analysis code and its metadata — not prospective registrations, and the manuscript says so. Three deviations from the aquifer protocol as frozen are disclosed in one place (SI S15); none changes a verdict.

**Reproducibility.** All input data, scripts, result files, the frozen protocol documents and an environment record are archived (GitHub MIKEAA2020/general-sustainability; Zenodo 22553609). A standard-library verification script recomputes the baselines and autocorrelations from the registered series, checks every cell of the aquifer tables against the archived result files and asserts the textual invariants (139 checks, all passing).

The work is original, is not under consideration elsewhere, and I have no competing interests to declare. The cod half supersedes the single-system manuscript *Does a surplus-production ladder improve forecasts of Northern cod?*, which has not been submitted.

Yours sincerely,

**Amin Abaee**
Independent Researcher
ORCID: 0000-0002-0019-1842
amin_abaee@ut.ac.ir

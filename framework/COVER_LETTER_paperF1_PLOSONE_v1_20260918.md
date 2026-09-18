# Cover Letter — Paper F1

**Title:** When a model is not retained: a pre-registered out-of-sample audit standard for structural modules in empirical environmental forecasting
**Author:** Amin Abaee (Independent Researcher)
**Journal:** *PLOS ONE*
**Manuscript carrier:** `paperF1_retention_framework_v30_humanized` (typst stamp `se30-c1375ed`), with Supplement S1 v30
**Keywords:** forecast evaluation; model retention; pre-registration; negative results; environmental forecasting; stock assessment; groundwater; operating characteristics

---

Dear Editor,

I am pleased to submit my manuscript, **"When a model is not retained: a pre-registered out-of-sample audit standard for structural modules in empirical environmental forecasting,"** for consideration in *PLOS ONE*.

**What the paper does.** Environmental forecasting practice—across fisheries, water resources, and beyond—builds structural modules by default, yet there is no pre-registered standard that says when added structure has earned its place out-of-sample. This paper supplies and demonstrates one: a frozen retention rule in which a candidate causal module is retained only if it reduces rolling-origin RMSE against both last-value persistence and the next-simpler rung by more than a stated 5% tie band, at both one-step and multi-step horizons, with information availability documented per input at each forecast origin. The rule is applied to two unrelated, management-demanding empirical cases—Northern cod biomass (NAFO 2J3KL, two assessment series) and Edwards Aquifer head at index well J-17 (1934–2023)—with per-origin forecast files archived so every verdict can be recomputed.

**Why it matters.** The two worked examples reach empty retained sets for opposite reasons: on cod, the closest structural approach misses the band at +9.01% (five years) and +17.09% (one year), never approaching retention, while on Edwards the best-scoring module passes the predictive gates but is declined on pre-specified class grounds (it collapses to an affine AR(1) map). The paper then measures the instrument itself against known ground truth, because a negative verdict is informative only if the gate has teeth where truth is strong. On 10,000 pre-registered simulation replicates the rule is highly specific (0.978 under a persistence null), powerful only where signal is strong (0.955–0.960 at collapse-window parameters), and weak against stock-flow and depensatory dynamics—power is low for three of four in-class processes, and the paper shows the cause is parameter identification (likelihood flatness and compensation), not gate conservatism: removing all gates adds almost no power. Out-of-class truths (time-varying productivity, observation error) produce false retention at 0.633–0.933, delimiting what non-retention can and cannot certify. A comparison against rule variants on the same archived replicates (information criterion: 0.509/0.992/0.615; scaled-error gate: 0.651/0.675/0.945; the rule as stated: 0.376/0.978/0.835) locates the trade the pre-registered rule makes, and the verdicts are shown band-invariant, with a simulation-calibrated band (power ≥ 0.80, specificity ≥ 0.90) registered exclusively for future applications—it never re-opens the verdicts reported here.

**Why it is appropriate for *PLOS ONE*.** *PLOS ONE* evaluates rigour and methodology rather than perceived impact, and explicitly welcomes well-executed negative results—exactly what this paper is: a methodological standard proven out on two hard real datasets, calibrated against known synthetic truth, every intermediate classification reproducible from registered files. The contribution is a certified instrument for auditing structural complexity claims in any forecast-driven environmental discipline, together with its measured limits: which failure modes it detects, which it cannot, and where a stronger band is licensed only prospectively. That combination—pre-registration, conflict-free negative certificates scoped to estimator and series, byte-level reproducibility, and honest power accounting—sits at the centre of the journal's reproducibility and methodology remit.

**Fit and originality.** To my knowledge this is the first pre-registered forecast-retention audit standard applied jointly across fisheries and groundwater with archived per-origin replicates, likelihood-ratio evidential weights per generating mechanism, and a calibrated prospective band registered before use. The paper's claims are conservative throughout: it makes no sustainability statement about either system, draws no unlicensed physical inference from predictive retention, and states precisely which conclusions are licensed, which are open, and which are ruled out.

**Declarations.** All input data, analysis campaigns, frozen result files, the 10,000-replicate archives, and the independent band-calibration audits are archived in a public repository (https://github.com/MIKEAA2020/general-sustainability) and regenerate deterministically, byte for byte. The work is original, is not under consideration elsewhere, and I have no competing interests. Funding: none received.

Thank you for your consideration.

Yours sincerely,

**Amin Abaee**
Independent Researcher
ORCID: [0000-0002-0019-1842](https://orcid.org/0000-0002-0019-1842)
Email: [amin_abaee@ut.ac.ir](mailto:amin_abaee@ut.ac.ir)

Date: 18 September 2026

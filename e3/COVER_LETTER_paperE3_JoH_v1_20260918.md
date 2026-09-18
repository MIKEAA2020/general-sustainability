# Cover Letter — Paper E3

**Title:** Does a one-pool water-balance model improve forecasts of Edwards Aquifer head? A scored test at J-17
**Author:** Amin Abaee (Independent Researcher)
**Journal:** *Journal of Hydrology*
**Manuscript carrier:** `paperE3_edwards_forecast_ladder_v24_humanized` (typst stamp `se24-c1375ed`), with Supplement v2
**Keywords:** Edwards Aquifer; J-17 index well; groundwater level forecasting; water balance; forecast evaluation; persistence benchmark; prediction skill; negative result

---

Dear Editor,

I am pleased to submit my manuscript, **"Does a one-pool water-balance model improve forecasts of Edwards Aquifer head? A scored test at J-17,"** for consideration in the *Journal of Hydrology*.

**What the paper does.** Groundwater management decisions at the Edwards (Balcones Fault Zone) Aquifer — drought-stage declarations, critical-period pumping reductions, springflow protections — are triggered by threshold crossings of head at index well J-17 in the San Antonio Pool. Yet the process-based water-balance models used in conceptual planning for such triggers are almost never scored formally against the naive statistical baselines they would have to beat to justify their structure. This paper runs that test: on the 90-year annual record (1934–2023), a forward-ordered ladder of discrete-time models — last-value persistence, training-mean climatology, a univariate AR(1), a one-pool stock-flow water balance with causal recharge–pumpage fluxes, residual and delay variants, and climate-informed recharge modules — is scored for out-of-sample RMSE on fixed historical windows and rolling origins, under a retention rule locked before scoring: a module is retained only if it beats both persistence and the next-simpler causal model.

**Why it matters.** The results invert the usual expectation, for a diagnosed physical reason. The one-pool balance that persists last year's recharge loses to naive persistence at one year (14.70 ft versus 13.23 ft): annual recharge is near-white (corr($R_t$, $R_{t-1}$) = 0.17), while head increments track contemporaneous recharge (corr($\Delta H_t$, $R_t$) = 0.74) — the model's structural information arrives one year too late to help a forecast. The univariate AR(1) gains only 0.39 ft (12.84 ft), a margin statistically indistinguishable from zero (tied MAE at 10.7 ft, five-year loss, bootstrap interval [$-1.51$, $+0.71$] ft). A water balance driven by climatological fluxes scores best at one step (12.28 ft) but is an affine AR(1) map and is declined by a pre-specified class clause. Given *realized* future recharge and pumping, the same one-pool balance nowcasts head at 7.55 ft RMSE ($-42.96\%$ against persistence; 10.87 ft at five years, $-48.52\%$) — the timing bottleneck is access to future fluxes, not pool structure. Pre-season climate predictors (ENSO and division precipitation) add at most 0.13 ft. At five years, training-mean climatology beats persistence robustly (16.80 versus 21.11 ft). Margin claims are accompanied by a post-freeze uncertainty layer (Diebold–Mariano with Newey–West HAC; moving-block bootstrap), replicated end-to-end under a second implementation with different seeds, block lengths, and HAC conventions, and every conclusion survives (for example, the climatological module's one-year edge: DM $z = 3.07$, $p = 0.003$, CI $[-1.45, -0.68]$ ft). The manuscript also reports the Comal Springs cessation diagnostics (rated channel RMSE driver values and the zero-discharge threshold conflict at 602.9 ft) and the archived pumpage counterfactuals (a 20% pumping cut from 1991 ends 2023 +5.2 ft above the observed trajectory, 646.8 versus 641.6 ft, at 7.19 versus 8.56 ft RMSE), so the reader can see both the forecast and the planning-regime readings.

**Why it is appropriate for the *Journal of Hydrology*.** The paper is a strictly scored, physically diagnosed forecast-evaluation study of one of the most management-critical karst index wells in the United States, on the journal's core subject matter: groundwater-level predictability at the attribution resolution of a lumped water balance. It demonstrates — with archived, reproducible evidence — that forecast skill at the one-year horizon is capped by flux nowcast availability, and that a frozen retention protocol changes what counts as a defensible model claim in the aquifer-forecasting literature. The paper states its limits explicitly: one index well, one aquifer, one annual resolution, one scoring rule; it makes no sustainability claim about the Edwards system, and its negative certificates are scoped to the estimator and series evaluated.

**Fit and originality.** The originality lies in the disciplined benchmark design — a frozen retention rule with declared comparator structure, a persistent-versus-climatological-flux decomposition that isolates identity of the failing module (recharge persistence, not pool dynamics), an explicit forecast-versus-nowcast oracle bound, and a twice-implemented deterministic uncertainty layer with a public replication. This is, to my knowledge, the first forecast-ladder evaluation against a persistence benchmark on the J-17 record under a pre-registered protocol with archived per-origin forecast files.

The manuscript is self-contained and all input data, analysis scripts, frozen result files, the scored panel, and both independent uncertainty implementations are archived in a public repository (https://github.com/MIKEAA2020/general-sustainability); all computations are deterministic and regenerate every archived file byte for byte. I confirm the work is original, is not under consideration elsewhere, and I have no conflicts of interest.

Thank you for your consideration.

Yours sincerely,

**Amin Abaee**
Independent Researcher
ORCID: [0000-0002-0019-1842](https://orcid.org/0000-0002-0019-1842)
Email: [amin_abaee@ut.ac.ir](mailto:amin_abaee@ut.ac.ir)

Date: 18 September 2026

# Supplementary Material — Typed Flux Ledgers and Depletion Arithmetic

*Accompanies: "Typed Flux Ledgers and Depletion Arithmetic: Conservation, Componentwise Diagnostics, and the Semantics of Depletion Horizons."*

This file carries the audited admissibility failures, the registered domain-template ladders, the split-assignment mechanism table, and the statement inventory.

---

## S1. The Ten-State Admissibility Template and Its Negative Witnesses

The six-state material cancellation of the main text (Section 4.9) arises in a ten-state admissibility template (living stock, juveniles, product, waste, detritus, active pool, geological pool, institutional memory, effort, and a variance coordinate). The template is an admissibility stress test, not a published system, and its audit produced three negative witnesses, recorded here as audited failures:

1. **The geological-exchange witness.** The template's geological exchange is a fixed-target law $\dot G = -\omega_A(A^{\mathrm{eq}} - A)$, which is not donor-limited: at $G = 0$ with $A < A^{\mathrm{eq}}$ it gives $\dot G < 0$, so the nonnegative geological orthant is not forward invariant. A physically admissible formulation must replace the fixed-target exchange by separate non-negative donor-limited fluxes $e_{GA}(G,A)$ and $e_{AG}(A,G)$ with $e_{GA}(0,A) = 0$ and $e_{AG}(0,G) = 0$ — the construction used throughout the main text's closed ledger.

2. **The variance-unclosed witness.** At $V_N = 0$ the variance equation gives $\dot V_N = -2q\bar X_A \operatorname{Cov}(E, \bar X_A)$, which can be negative; the covariance is not a functional of the ten displayed states, and the variance dynamics are not guaranteed realizable by a non-negative spatial distribution. The variance closure does not exist as stated.

3. **The $Q$-undefined witness.** The capital equation's output functional $Q$ has no displayed state equation or constitutive closure; a broader production function cannot silently supply the omission. The ten equations therefore determine no unique autonomous system or characteristic quasi-polynomial.

**Application prerequisites.** Four prerequisites are registered for any application of the ten-state template: the geological exchange must be donor-limited; the variance equation must receive a realizable closure; the output functional $Q$ must be defined; and the information and governance operators must be declared. The calibration discipline rides them: calibration from spawning-stock biomass and fishing mortality alone would remain underidentified — juvenile abundance, recruitment, maturation, natural mortality, selectivity, active-pool measurements, spatial variance and covariance, capital/exergy, and governance timing are also required — so applications begin from a minimum module set and measured observables rather than fitting all ten states from two series.

---

## S2. Registered Domain-Template Ladders

**S2.1 Phosphorus template.** The identification ladder declares, for each registered parameter, the observation that would identify it, the prior range, and the observation that would reject the routing assumption: reserve and resource estimates (economic classification; vintage-dependent); mining cost and price response (which determines the reserve-to-resource conversion); recovery fractions $\alpha, \rho$ (material-flow observations at the waste and product stages); soil-pool retention and runoff coefficients (mass-balance closure at the catchment scale); and the yield functions of the fertilizer conversion (stoichiometric, declared per process). The falsification protocol for each routing assumption is registered: a recovery claim is falsified by a mass-balance audit of the claimed route; a retention claim by a catchment closure test. No constitutive content is claimed; the ladder is an identification object.

**S2.2 Groundwater template.** The one-pool affine approximation is the admitted object. The registered requirements for the two-pool closure are: geological geometry (aquitard depth and extent); multi-depth heads; pumping tests; tracer, isotope, or water-age evidence; recharge estimates; prior ranges for the storage parameters $C_i$ and the fast–slow coupling $\kappa_{fs}$; and the discipline that leakage terms may not absorb unexplained residuals. The two-pool model is not established, and no two-pool claim appears in the main text.

---

## S3. Split-Assignment Mechanism Table

The split-assignment discipline of the main text (Section 2.5) is instantiated by the following illustrative pairs, stated as calibrated examples through the logistic two-channel proxy — illustrative status, no constitutive claim for the named domains:

| Domain | Mechanism A (existing-unit removal) | $\psi$ | Mechanism B (replenishment degradation) | $\psi$ |
|---|---|---|---|---|
| Soil zinc | crop export | $0.85$ | impaired mineralisation | $0.25$ |
| Pollinators | adult mortality | $0.70$ | brood failure | $0.20$ |

Across such mechanism pairs the trough depth varies by a factor of about $1.5$ from mechanism alone. The routing discipline: harvesting pre-recruit stages routes to product and waste fractions; habitat-induced failed recruitment is a prevented inflow and must not be routed into product or waste; capital-stock damage (compaction, severe soil loss) is a capacity drift or a transfer to the inert sink, not a split channel.

---

## S4. Statement Inventory

Every statement of the main text carries one of the following statuses; none is promoted.

- **Theorems with displayed proofs:** Theorem 1 (support-saturated logistic limit); Theorem 2 (registered-family support-saturated identity); Proposition 1 and Theorem 4 (conservation reduction); Proposition 2 (layer relations); Theorem 3 (flux reconstruction); Theorem 5 and corollary (flux-bounding envelopes); Theorem 6 and counterexample (finite exhaustion under uniform drift); Theorems 7–14 (natural-block identity, stoichiometric conservation, six-compartment conservation, orthant invariance, no interior rest, extinction–geochemical rest, extraction integrability); Theorem 17 (threshold-horizon bracket); Lemma 16 (specialization deficit identity); Theorem 18 and Corollary 19 (inverse-Gaussian passage and median); Theorem 20 (geometric-Brownian passage).
- **Theorems whose proofs rest on classical cited results:** Theorem 18 (first-passage law, Chhikara and Folks, 1989; Redner, 2001); Theorem 20 (Itô lemma, Øksendal, 2003); Theorem 10–11 (tangent-cone invariance, Aubin, 1991, in the compartmental lineage of Jacquez and Simon, 1993).
- **Conditional theorems:** Theorem 15 (hybrid moiety balance), conditional on local finiteness, jump factorization, and the yield-routing obligation.
- **Definitions:** the certification predicates (Section 3.1); the typed safety set (3.2); the feasible balance domain (Definition 1); the directional support gap (Definition 2); the depletion trichotomy (Definitions 3–5); the Brownian surrogate (Definition 6); the robust semantics (Section 6.4).
- **Application records at source status:** the G3P index (6.5.1); the applied tables (6.5.2); the phosphate reserve-life ratio (6.5.3); the fisheries removals-only time (6.5.4); the constant-production phosphate passage (7.6).
- **Boundary statements:** the sink obstructions (2.4); the non-reduction boundary with its five reasons and the frozen-donor limit (Section 9); the seven non-claims (7.7); the registered template obligations (Section 8).
- **Audited negative witnesses:** S1 of this file.
- **Cohort-sensitivity records:** S5 (fisheries cohort, database-version sensitivity).


## S5. Fisheries cohort statistics — corrected protocol and version-sensitivity record

The main-text fisheries column reports the pure-decay proxy $\mathrm{ADH} = F^{-1}\log(\mathrm{SSB}_{\mathrm{now}}/(0.2\max\mathrm{SSB}))$, with **zero entered for any stock already at or below the reference**, median $\approx 1.8$ yr over the archived 43-stock cohort (RAM Legacy v4.66 extract `fisheries_adh.csv`, pull archived in the analysis repository; the spectral-null subset is the 42 annual-managed stocks within it — a nested pair, not two cohorts). The quartile summary of $F$ and $\log(\mathrm{SSB}/B_{\lim})$ over that cohort is defined by, and quoted from, that archived pull alone.

**Specification recovered from the source caption** (the zero convention is load-bearing: an earlier draft of this record excluded below-reference stocks and understated the protocol). The extract's own example rows verify the vintage: four of six published $F$ values reproduce the public RAM Legacy v4.66 release exactly (Adriatic anchovy 17–18: 1.0026 vs published 1.00; North Sea herring: 0.2274 vs 0.23; W. Baltic herring (ICES 22–24): 0.193 vs 0.19; Argentine anchovy south: 0.0114 vs 0.011). The corresponding ADH values require the extract-time series state: two example stocks (N. Adriatic anchovy, W. Scotland herring) no longer carry any series in public releases v4.64–v4.66, and several stocks' SSB series have since been revised (the North Sea herring series now reaches back to 1947 with a maximum 60% larger than the extract's, which is exactly the difference between the published ADH 3.5 and the 1.5 the current series gives).

**Version-sensitivity record** (same protocol — zeros included, last finite year, most-recent-assessment view, $F$ column — computed independently on the public releases):

| RAM Legacy release | cohort size | zeros | median ADH (yr) |
|---|---|---|---|
| v4.44 (2018, Zenodo 2542919) | 415 | 63 | 2.57 |
| v4.66 (2024, Zenodo 14043031) | 454 | 69 | 3.39 |

Neither release reproduces the archived cohort (43 stocks, median 1.8 yr): the difference is not the protocol but the cohort — the archived extract's 43-stock list and its extract-time series are what the archived pull supplies, and no public release's full-cohort statistic substitutes for them. This is why the main text pins every cohort statistic to the archived pull and quotes no cohort statistic from a different database version.

**Archived-pull verification (2026-09-03).** The archived extract itself is now in hand (`fisheries_adh.csv`, 44 lines: header + 43 stocks, columns `stock, SSB, F, B_lim, ADH_yr, lastyear`), and every row has been recomputed against the recovered specification. With $B_{\lim}$ identified as $0.2\max\mathrm{SSB}$ (confirmed row by row), all 35 positive rows reproduce $\mathrm{ADH} = F^{-1}\log(\mathrm{SSB}/B_{\lim})$ to relative error below $10^{-9}$, and the eight zero rows are exactly the stocks with $\mathrm{SSB} \le B_{\lim}$ (no zero row has $\mathrm{SSB} > B_{\lim}$): the extract's ADH column is $\max(0, F^{-1}\log(\mathrm{SSB}/B_{\lim}))$ throughout. Cohort statistics recomputed from the pull: 43 stocks; 8 zeros; **median 1.7902 yr with zeros included** (the reported value; $2.8578$ yr over the 35-stock positive sub-cohort); maximum 201.1797 yr (ANCHMEDGSA7, $F=0.008$, $\mathrm{SSB}/B_{\lim}=5.000$); quartiles of $F$: $0.1752$ / $0.2680$ / $0.5298$; quartiles of $\log(\mathrm{SSB}/B_{\lim})$: $0.2133$ / $0.8019$ / $1.1056$. The four published-$F$ anchors read off the file itself: Adriatic anchovy 17–18 $F=1.0026$ (published 1.00); North Sea herring — extract id `HERRNS-IIIa-VIId` — $F=0.2274$ (published 0.23) with $\mathrm{ADH}=3.461$ (published 3.5); W. Baltic herring (ICES 22–24) $F=0.193$ (published 0.19); Argentine anchovy south $F=0.0114$ (published 0.011). The two example stocks that no longer carry series in public releases are present in the extract (W. Scotland herring `HERRVIa`, ADH 0.385; N. Adriatic anchovy `ANCHMEDGSA17`, ADH 4.782), confirming the extract predates their removal. The earlier "not reproducible" reading is fully retracted: the archived pull is internally consistent and carries exactly the cohort statistics the main text reports.

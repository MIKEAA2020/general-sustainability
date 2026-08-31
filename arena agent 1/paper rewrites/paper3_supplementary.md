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

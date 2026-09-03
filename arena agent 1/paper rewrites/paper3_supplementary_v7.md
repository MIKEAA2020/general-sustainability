# Supplementary Material — Typed Flux Ledgers and Depletion Arithmetic

*Accompanies: "Typed Flux Ledgers and Depletion Arithmetic: Conservation, Componentwise Diagnostics, and the Semantics of Depletion Horizons."*

This supplementary accompanies the main text. It carries the audited admissibility failures of the ten-state template, the registered domain-template identification ladders, the split-assignment mechanism table, the statement inventory, and the fisheries cohort protocol and version-sensitivity record. The orientation is material-flows accounting and ecological-economics measurement: a *typed stock–flow ledger* (a per-moiety accounting layer that keeps conservation laws typed) records each *moiety* (a named conserved substance with a unit) on its own coordinate, so that mass-balance identities can be checked componentwise rather than only in aggregate. *Depletion arithmetic* refers to the family of operations the ledger supports for converting stock magnitudes, fluxes, and drift rates into horizon times.

The contents are organised as follows. Section S1 records the three audited negative witnesses of the ten-state admissibility template and the four application prerequisites that follow from them. Section S2 registers the phosphorus and groundwater identification ladders, which declare — for each parameter — the observation that would identify it, the prior range, and the observation that would reject the routing assumption. Section S3 reports the split-assignment mechanism table for the logistic two-channel proxy. Section S4 is the statement inventory: every claim of the main text is listed with its status; none is promoted. Section S5 carries the corrected fisheries cohort protocol, the broad-cohort comparison, and the version-sensitivity record against the two public RAM Legacy releases.

---

## S1. The Ten-State Admissibility Template and Its Negative Witnesses

The six-state material cancellation of the main text (Section 4.9) arises in a ten-state admissibility template. The ten states are: living stock, juveniles, product, waste, detritus, active pool, geological pool, institutional memory, effort, and a variance coordinate. The template is an admissibility stress test, not a published system. Its audit produced three negative witnesses, recorded here as audited failures. The witnessing is in the tradition of industrial-ecology material-balance auditing: a model that fails conservation under a stated closure is rejected at the closure, not repaired by an unregistered residual.

**Definition S1.1 (Ten-state admissibility template).** The ten-state admissibility template is the system on the ten states above, with the geological exchange set to the fixed-target law $\dot G = -\omega_A(A^{\mathrm{eq}} - A)$, the variance equation set to $\dot V_N = -2q\bar X_A \operatorname{Cov}(E, \bar X_A)$, and the capital equation's output functional $Q$ left without a displayed state equation or constitutive closure. The template is an admissibility object: its purpose is to be checked for forward-invariance and closure, not to be calibrated as a published system.

**Proposition S1.1 (Geological-exchange admissibility failure).** *Under the fixed-target geological exchange $\dot G = -\omega_A(A^{\mathrm{eq}} - A)$, the nonnegative geological orthant is not forward invariant.*

*Proof.* At $G = 0$ with $A < A^{\mathrm{eq}}$, the law gives $\dot G = -\omega_A(A^{\mathrm{eq}} - A) < 0$, so a trajectory initiated on the boundary exits the nonnegative orthant. □

A physically admissible formulation must replace the fixed-target exchange by separate non-negative donor-limited fluxes $e_{GA}(G, A)$ and $e_{AG}(A, G)$ with $e_{GA}(0, A) = 0$ and $e_{AG}(0, G) = 0$. This is the construction used throughout the main text's closed ledger.

**Proposition S1.2 (Variance-unclosed failure).** *The variance equation $\dot V_N = -2q\bar X_A \operatorname{Cov}(E, \bar X_A)$ is not closed in the ten displayed states.*

*Proof.* At $V_N = 0$ the right-hand side gives $\dot V_N = -2q\bar X_A \operatorname{Cov}(E, \bar X_A)$, which can be negative. The covariance $\operatorname{Cov}(E, \bar X_A)$ is not a functional of the ten displayed states, so the variance dynamics are not guaranteed realisable by a non-negative spatial distribution. The variance closure does not exist as stated. □

**Proposition S1.3 ($Q$-undefined failure).** *The capital equation's output functional $Q$ has no displayed state equation or constitutive closure in the template. A broader production function cannot silently supply the omission. The ten equations therefore determine no unique autonomous system or characteristic quasi-polynomial.*

*Proof.* Inspection of the ten displayed equations: $Q$ appears in the capital equation but is not itself the left-hand side of any displayed equation and is not given by a constitutive law in the template. □

**Application prerequisites.** Four prerequisites are registered for any application of the ten-state template. The geological exchange must be donor-limited. The variance equation must receive a realisable closure. The output functional $Q$ must be defined. The information and governance operators must be declared.

The calibration discipline rides them. Calibration from spawning-stock biomass and fishing mortality alone would remain underidentified: juvenile abundance, recruitment, maturation, natural mortality, selectivity, active-pool measurements, spatial variance and covariance, capital/exergy, and governance timing are also required. Applications therefore begin from a minimum module set and measured observables rather than fitting all ten states from two series. For material-flows accounting, the lesson is that an admissible closed ledger must be donor-limited on every outflow edge and closed on every coordinate that the audit invokes; a model that fails either test is rejected at the audit, not patched by an unregistered residual.

---

## S2. Registered Domain-Template Ladders

The phosphorus and groundwater templates are identification objects. Each ladder declares, for each registered parameter, the observation that would identify it, the prior range, and the observation that would reject the routing assumption. No constitutive content is claimed; the ladders exist to make the falsification protocol explicit.

**Definition S2.1 (Phosphorus identification ladder).** The phosphorus identification ladder declares, for each registered parameter, the triple (identification observation, prior range, rejection observation). The registered parameters are:

- reserve and resource estimates (economic classification; vintage-dependent);
- mining cost and price response (which determines the reserve-to-resource conversion);
- recovery fractions $\alpha, \rho$ (material-flow observations at the waste and product stages);
- soil-pool retention and runoff coefficients (mass-balance closure at the catchment scale);
- the yield functions of the fertilizer conversion (stoichiometric, declared per process).

The falsification protocol for each routing assumption is registered. A recovery claim is falsified by a mass-balance audit of the claimed route. A retention claim is falsified by a catchment closure test. No constitutive content is claimed; the ladder is an identification object.

**Definition S2.2 (Groundwater identification ladder).** The one-pool affine approximation is the admitted object. The registered requirements for the two-pool closure are:

- geological geometry (aquitard depth and extent);
- multi-depth heads;
- pumping tests;
- tracer, isotope, or water-age evidence;
- recharge estimates;
- prior ranges for the storage parameters $C_i$ and the fast–slow coupling $\kappa_{fs}$;
- the discipline that leakage terms may not absorb unexplained residuals.

The two-pool model is not established, and no two-pool claim appears in the main text. For groundwater accounting, the registered requirements make explicit what would have to be measured to escalate from the one-pool affine approximation to a two-pool closure; in their absence the one-pool model is the admissible object.

---

## S3. Split-Assignment Mechanism Table

The split-assignment discipline of the main text (Section 2.5) is instantiated by the illustrative pairs reported below. The pairs are calibrated examples through the logistic two-channel proxy; they have illustrative status, and no constitutive claim is made for the named domains.

**Definition S3.1 (Split-assignment mechanism pair).** A split-assignment mechanism pair is a pair $(A, B)$ of mechanisms operating on a stock, with calibrated $\psi$ values drawn from the logistic two-channel proxy, where:

- (H1) Mechanism $A$ removes biomass from existing units (for example, crop export, adult mortality);
- (H2) Mechanism $B$ degrades replenishment (for example, impaired mineralisation, brood failure);
- (H3) Each mechanism carries its own calibrated $\psi$ value.

The illustrative calibrated pairs are as follows.

| Domain | Mechanism A (existing-unit removal) | $\psi$ | Mechanism B (replenishment degradation) | $\psi$ |
|---|---|---|---|---|
| Soil zinc | crop export | $0.85$ | impaired mineralisation | $0.25$ |
| Pollinators | adult mortality | $0.70$ | brood failure | $0.20$ |

**Proposition S3.1 (Trough-depth variation).** *Across split-assignment mechanism pairs satisfying (H1)–(H3), the trough depth varies by a factor of about $1.5$ from mechanism alone.*

*Proof.* Direct computation on the calibrated soil-zinc and pollinator pairs under the logistic two-channel proxy. The two trough-depth readings differ by approximately the stated factor; the variation is mechanism-attributable because the underlying stock parameter is held fixed within each domain pair. □

The routing discipline for split-assignment has three clauses. Harvesting pre-recruit stages routes to product and waste fractions. Habitat-induced failed recruitment is a prevented inflow and must not be routed into product or waste. Capital-stock damage — compaction, severe soil loss — is a capacity drift or a transfer to the inert sink, not a split channel. For material-flows accounting, the discipline enforces that a prevented inflow cannot be silently recorded as a product or waste flux: each channel of the typed ledger must carry a physically admissible direction.

---

## S4. Statement Inventory

Every statement of the main text carries one of the following statuses; none is promoted. The inventory is recorded so that any later use of a statement can be checked against its declared status, in the spirit of explicit scope discipline for sustainability-accounting claims.

- **Theorems with displayed proofs:** Theorem 1 (support-saturated logistic limit); Theorem 2 (registered-family support-saturated identity); Proposition 1 and Theorem 4 (conservation reduction); Proposition 2 (layer relations); Theorem 3 (flux reconstruction); Theorem 5 and corollary (flux-bounding envelopes); Theorem 6 and counterexample (finite exhaustion under uniform drift); Theorems 7–14 (natural-block identity, stoichiometric conservation, six-compartment conservation, orthant invariance, no interior rest, extinction–geochemical rest, extraction integrability); Theorem 17 (threshold-horizon bracket); Lemma 16 (specialization deficit identity); Theorem 18 and Corollary 19 (inverse-Gaussian passage and median); Theorem 20 (geometric-Brownian passage).
- **Theorems whose proofs rest on classical cited results:** Theorem 18 (first-passage law, Chhikara and Folks, 1989; Redner, 2001); Theorem 20 (Itô lemma, Øksendal, 2003); Theorem 10–11 (tangent-cone invariance, Aubin, 1991, in the compartmental lineage of Jacquez and Simon, 1993).
- **Conditional theorems:** Theorem 15 (hybrid moiety balance), conditional on local finiteness, jump factorization, and the yield-routing obligation.
- **Definitions:** the certification predicates (Section 3.1); the typed safety set (3.2); the feasible balance domain (Definition 1); the directional support gap (Definition 2); the depletion trichotomy (Definitions 3–5); the Brownian surrogate (Definition 6); the robust semantics (Section 6.4).
- **Application records at source status:** the G3P index (6.5.1); the applied tables (6.5.2); the phosphate reserve-life ratio (6.5.3); the fisheries removals-only time (6.5.4); the constant-production phosphate passage (7.6).
- **Boundary statements:** the sink obstructions (2.4); the non-reduction boundary with its five reasons and the frozen-donor limit (Section 9); the seven non-claims (7.7); the registered template obligations (Section 8).
- **Audited negative witnesses:** S1 of this file.
- **Cohort-sensitivity records:** S5 (fisheries cohort, database-version sensitivity).

For ecological-economics measurement, the inventory's role is to keep every claim tied to its declared status — theorem, conditional theorem, definition, application record, boundary statement, or audited negative witness — so that no application claim can be smuggled in as a theorem and no boundary statement can be promoted to a theorem without an explicit new proof.

---

## S5. Fisheries cohort statistics — corrected protocol and version-sensitivity record

The main-text fisheries column reports the pure-decay proxy $\mathrm{ADH} = F^{-1}\log(\mathrm{SSB}_{\mathrm{now}}/(0.2\max\mathrm{SSB}))$, with **zero entered for any stock already at or below the reference**, median $\approx 1.8$ yr over the archived 43-stock cohort (RAM Legacy v4.66 extract `fisheries_adh.csv`, pull archived in the analysis repository; the spectral-null subset is the 42 annual-managed stocks within it — a nested pair, not two cohorts). The quartile summary of $F$ and $\log(\mathrm{SSB}/B_{\lim})$ over that cohort is defined by, and quoted from, that archived pull alone. The pure-decay proxy is a *first-passage time* (the time at which a pure-decay trajectory first crosses the reference level $B_{\lim}$); the qualifier "pure-decay" marks that recruitment is not represented in the trajectory.

**Definition S5.1 (Archived-depletion-horizon protocol).** The archived-depletion-horizon (ADH) protocol is defined on a stock with finite $F$ and SSB series by

$$\mathrm{ADH} \;=\; \max\!\left(0,\; F^{-1}\log\!\left(\mathrm{SSB}_{\mathrm{now}}/B_{\lim}\right)\right), \qquad B_{\lim} \;=\; 0.2\max(\mathrm{SSB}),$$

where $\max(\mathrm{SSB})$ is taken over all SSB-finite years. The protocol hypotheses are:

- (H1) the stock's $F$ series has a finite last value (the last finite $F$ of its own series is used; rows with $F \le 0$ are dropped);
- (H2) zeros are included (below-reference stocks enter as zero, not omitted);
- (H3) the most-recent-assessment view is used.

**Cohort composition and class scope (verified 2026-09-03).** The 43-stock cohort is a selected class, not a random sample of assessed stocks. All 43 are small pelagics — 18 anchovy, 20 herring, 4 sprat, 1 sardine (SSARDCH) — the fast-maturing, annually managed class the companion review screen selects by its annual-review eligibility criterion, with 42 of the 43 being that screen's annual-managed spectral-null stocks (source caption). The $1.8$ yr median is therefore a class-specific diagnostic for that class, not a statistic of assessed fisheries in general. The public-release medians below ($2.57$ / $3.39$ yr) are higher because the full database adds long-lived stocks (cod, rockfish, sharks and other slow-maturing assessed stocks) absent from the class cohort. The difference between the archived and public medians is cohort composition, not a protocol or computation discrepancy.

**Broader-cohort comparison (executed 2026-09-03; hybrid placement — main-text citation in Section 6.5.2).** The recovered micro-specification (last finite $F$ of its own series; drop $F \le 0$; $B_{\lim} = 0.2\max(\mathrm{SSB})$ over all SSB-finite years; $\mathrm{ADH} = \max(0, F^{-1}\ln(\mathrm{SSB}_{\mathrm{now}}/B_{\lim}))$; zeros included) was recovered by a protocol grid over the two public releases (Zenodo 14043031 and 2542919, exported via each release's own R loader) and reproduces both anchors to printed precision — v4.66: 454 / 69 zeros / median 3.3893; v4.44: 415 / 63 / 2.5683. The broad v4.66 cohort decomposes by the database's taxGroup classification:

| group | n | zeros | median ADH (yr) | median, positives | max |
|---|---:|---:|---:|---:|---:|
| elasmobranchs | 19 | 2 | 11.51 | 12.96 | 1555.9 |
| sebastids | 33 | 1 | 9.03 | 9.13 | 163.8 |
| pleuronectids | 59 | 8 | 5.99 | 7.40 | 517.9 |
| other scorpaenids | 11 | 0 | 3.99 | 3.99 | 16.1 |
| crabs-lobsters | 22 | 3 | 3.90 | 5.48 | 40.0 |
| other marine fish | 39 | 7 | 3.73 | 4.88 | 87.7 |
| other marine percoidids | 60 | 7 | 2.87 | 3.40 | 53.8 |
| forage fish | 64 | 12 | 2.69 | 3.63 | 718.7 |
| tuna-billfish | 16 | 4 | 2.57 | 3.17 | 42.5 |
| bivalves-gastropods | 5 | 2 | 2.57 | 3.20 | 65.2 |
| gadids | 83 | 16 | 2.17 | 3.48 | 50.7 |
| carangids-mackerels | 20 | 5 | 1.62 | 3.46 | 65.5 |
| shrimps | 23 | 2 | 1.08 | 1.34 | 7.3 |
| **overall** | 454 | 69 | 3.39 | 4.13 | 1555.9 |
| **archived class cohort** | 43 | 8 | **1.79** | 2.86 | 201.2 |

The life-history gradient is clean and monotone across groups. The broad median is carried by the long-lived groups the class cohort excludes. The fast-turnover groups (shrimps 1.1, carangids 1.6, forage fish 2.7) sit closest to the class cohort.

**Overlap and vintage.** 33 of the 43 archived ids exist in current v4.66; 10 were dropped or merged — for example, HERR2532/HERR30/HERR31 $\to$ HERR30-31, HERRVIa $\to$ HERRVIaVIIbc, ANCHMEDGSA17 $\to$ ANCHMEDGSA17-18. Among the 33, per-stock ADH deltas (current minus archived) average 3.44 yr in absolute value, and the 33's archived-vintage median of 2.79 yr becomes 2.34 yr on current series. The all-43 archived median of 1.79 yr is pulled down substantially by the ten since-dropped ids. Its lowness is therefore a property of the extract-time stock list and series as well as of the pelagic class.

**Random-draw benchmark.** 10,000 draws of 43 stocks without replacement from the broad 454 cohort (and from the current 64-stock forage-fish group): only 2.12% (0.29%) of sample medians fall at or below 1.7902. The class cohort's median is unusually low against both pools. This is a descriptive benchmark, not a selection-bias hypothesis test: the class cohort is a dated extraction with a declared selection rule, not a random sample from either pool.

**Proposition S5.1 (Specification recovered from the source caption).** *The extract's own example rows verify the vintage. Four of six published $F$ values reproduce the public RAM Legacy v4.66 release exactly:*

- Adriatic anchovy 17–18: $F = 1.0026$ vs published $1.00$;
- North Sea herring: $F = 0.2274$ vs $0.23$;
- W. Baltic herring (ICES 22–24): $F = 0.193$ vs $0.19$;
- Argentine anchovy south: $F = 0.0114$ vs $0.011$.

*The zero convention is load-bearing: an earlier draft of this record excluded below-reference stocks and understated the protocol.* The corresponding ADH values require the extract-time series state. Two example stocks (N. Adriatic anchovy, W. Scotland herring) no longer carry any series in public releases v4.64–v4.66, and several stocks' SSB series have since been revised (the North Sea herring series now reaches back to 1947 with a maximum 60% larger than the extract's, which is exactly the difference between the published ADH 3.5 and the 1.5 the current series gives).

**Version-sensitivity record** (same protocol — zeros included, last finite year, most-recent-assessment view, $F$ column — computed independently on the public releases):

| RAM Legacy release | cohort size | zeros | median ADH (yr) |
|---|---|---|---|
| v4.44 (2018, Zenodo 2542919) | 415 | 63 | 2.57 |
| v4.66 (2024, Zenodo 14043031) | 454 | 69 | 3.39 |

**Proposition S5.2 (Version-sensitivity).** *Neither release reproduces the archived cohort (43 stocks, median 1.8 yr). The difference is not the protocol but the cohort: the archived extract's 43-stock list and its extract-time series are what the archived pull supplies, and no public release's full-cohort statistic substitutes for them.*

*Proof.* The same protocol (H1)–(H3) was applied independently to the public releases v4.44 and v4.66. The resulting medians are 2.57 yr and 3.39 yr respectively; neither matches the archived 1.8 yr median. Since the protocol is identical across the three pulls, the discrepancy must be attributed to the cohort composition, not to the protocol. □

This is why the main text pins every cohort statistic to the archived pull and quotes no cohort statistic from a different database version.

**Proposition S5.3 (Archived-pull internal consistency, verified 2026-09-03).** *The archived extract itself is internally consistent with the recovered specification (H1)–(H3). With $B_{\lim}$ identified as $0.2\max\mathrm{SSB}$ (confirmed row by row), all 35 positive rows reproduce $\mathrm{ADH} = F^{-1}\log(\mathrm{SSB}/B_{\lim})$ to relative error below $10^{-9}$, and the eight zero rows are exactly the stocks with $\mathrm{SSB} \le B_{\lim}$ (no zero row has $\mathrm{SSB} > B_{\lim}$). The extract's ADH column is $\max(0, F^{-1}\log(\mathrm{SSB}/B_{\lim}))$ throughout.*

*Proof.* Direct recomputation against the recovered specification, row by row, on 2026-09-03. □

Cohort statistics recomputed from the pull: 43 stocks; 8 zeros; **median 1.7902 yr with zeros included** (the reported value; $2.8578$ yr over the 35-stock positive sub-cohort); maximum 201.1797 yr (ANCHMEDGSA7, $F=0.008$, $\mathrm{SSB}/B_{\lim}=5.000$); quartiles of $F$: $0.1752$ / $0.2680$ / $0.5298$; quartiles of $\log(\mathrm{SSB}/B_{\lim})$: $0.2133$ / $0.8019$ / $1.1056$.

The four published-$F$ anchors read off the file itself: Adriatic anchovy 17–18 $F=1.0026$ (published 1.00); North Sea herring — extract id `HERRNS-IIIa-VIId` — $F=0.2274$ (published 0.23) with $\mathrm{ADH}=3.461$ (published 3.5); W. Baltic herring (ICES 22–24) $F=0.193$ (published 0.19); Argentine anchovy south $F=0.0114$ (published 0.011). The two example stocks that no longer carry series in public releases are present in the extract (W. Scotland herring `HERRVIa`, ADH 0.385; N. Adriatic anchovy `ANCHMEDGSA17`, ADH 4.782), confirming the extract predates their removal. The earlier "not reproducible" reading is fully retracted: the archived pull is internally consistent and carries exactly the cohort statistics the main text reports.

For ecological-economics measurement, the implication is that an archived, dated extraction with a declared selection rule is a legitimate unit of analysis when its protocol and cohort are pinned; a public release's full-cohort statistic is not a substitute. The pure-decay ADH proxy is a class-specific first-passage diagnostic, not a general forecast of fishery removals time, and its cohort-sensitivity record makes that scoping explicit.

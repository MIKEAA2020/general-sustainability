# Supplementary Material — Typed Flux Ledgers and Depletion Arithmetic

*Accompanies: "Typed Flux Ledgers and Depletion Arithmetic: Conservation, Componentwise Diagnostics, and the Semantics of Depletion Horizons."*

This file is the checking half of the pair. The main text carries the argument; this file carries what an editor, a referee or a reader of the record asks to see when the request is "show me". It holds the material the main text refers to but cannot hold without becoming unreadable: the audited admissibility failures of the ten-state template, the registered identification ladders, the split-assignment mechanism table, the statement inventory, and the fisheries cohort protocol with its version-sensitivity record.

Two words carry most of the file. A *typed stock–flow ledger* is a per-moiety accounting layer, so mass-balance identities can be checked componentwise instead of only in aggregate; a *moiety* is a named conserved substance with a unit. *Depletion arithmetic* names the operations that turn stock magnitudes, fluxes and drift rates into horizons. Each is glossed again where it is first used.

For example, the contents run as follows. S1 records the three audited negative witnesses of the ten-state admissibility template, and the four application prerequisites that follow from them. S2 registers the phosphorus and groundwater identification ladders: for each parameter, the observation that would identify it, the prior range, and the observation that would reject the routing assumption. S3 reports the split-assignment mechanism table for the logistic two-channel proxy. S4 is the statement inventory, where every claim of the main text is listed with the status it holds and none is promoted. S5 carries the corrected fisheries cohort protocol, the broad-cohort comparison, and the version-sensitivity record against the two public RAM Legacy releases.

S7 to S9 carry the proof obligations of the certification state, the linear programmes with the reading rule for an infeasible programme, and the worked exhibits, promotion rules, reproduction record and statement inventory. S10 and S11 record what is and is not checkable in the applied classifications. S5.4, S14, S15 and S16 hold the extraction provenance, the domain-template detail and the label reconciliations the main text points to. S17 recomputes the aggregate overshoot date with carbon demand excluded, on two editions of the accounts.

---

## S1. The Ten-State Admissibility Template and Its Negative Witnesses

We record the three audited witnesses here, and the four prerequisites that follow from them. The six-state
material cancellation of the main text (Section 4.9) arises in a ten-state admissibility template. The ten
states are: living stock, juveniles, product, waste, detritus, active pool, geological pool, institutional
memory, effort, and a variance coordinate. The template is an admissibility stress test, not a published
system. Its audit produced three negative witnesses, recorded here as audited failures. The witnessing is in
the tradition of industrial-ecology material-balance auditing: a model that fails conservation under a stated
closure is rejected at the closure. It is not repaired by an unregistered residual.

**Definition S1.1 (Ten-state admissibility template).** The ten-state admissibility template is the system on
the ten states above, with the geological exchange set to the fixed-target law $\dot G = -\omega_A(A^{\mathrm{eq}} - A)$, the variance equation set
to $\dot V_N = -2q\bar X_A \operatorname{Cov}(E, \bar X_A)$, and the capital equation's output functional $Q$ left without a displayed state equation or
constitutive closure. The template is an admissibility object: its purpose is to be checked for forward-
invariance and closure, not to be calibrated as a published system.

**Proposition S1.1 (Geological-exchange admissibility failure).** *Under the fixed-target geological exchange
$\dot G = -\omega_A(A^{\mathrm{eq}} - A)$, the nonnegative geological orthant is not forward invariant.*

*Proof.* At $G = 0$ with $A < A^{\mathrm{eq}}$, the law gives $\dot G = -\omega_A(A^{\mathrm{eq}} - A) < 0$, so a trajectory initiated on the boundary exits the nonnegative
orthant. □

A physically admissible formulation must replace the fixed-target exchange by separate non-negative donor-
limited fluxes $e_{GA}(G, A)$ and $e_{AG}(A, G)$ with $e_{GA}(0, A) = 0$ and $e_{AG}(0, G) = 0$. This is the construction used throughout the main text's closed
ledger.

**Proposition S1.2 (Variance-unclosed failure).** *The variance equation $\dot V_N = -2q\bar X_A \operatorname{Cov}(E, \bar X_A)$ is not closed in the ten
displayed states.*

*Proof.* At $V_N = 0$ the right-hand side gives $\dot V_N = -2q\bar X_A \operatorname{Cov}(E, \bar X_A)$, which can be negative. The covariance $\operatorname{Cov}(E, \bar X_A)$ is not a functional
of the ten displayed states. The variance dynamics are not guaranteed realisable by a non-negative spatial
distribution. The variance closure does not exist as stated. □

**Proposition S1.3 ($Q$-undefined failure).** *The capital equation's output functional $Q$ has no displayed
state equation or constitutive closure in the template. A broader production function cannot silently supply
the omission. The ten equations therefore determine no unique autonomous system or characteristic quasi-
polynomial.*

*Proof.* Inspection of the ten displayed equations: $Q$ appears in the capital equation but is not itself the
left-hand side of any displayed equation and is not given by a constitutive law in the template. □

**Application prerequisites.** Four prerequisites are registered for any application of the ten-state
template. The geological exchange must be donor-limited. The variance equation must receive a realisable
closure. The output functional $Q$ must be defined. The information and governance operators must be declared.

The calibration discipline rides them. Calibration from spawning-stock biomass and fishing mortality alone
would remain underidentified: juvenile abundance, recruitment, maturation, natural mortality, selectivity,
active-pool measurements, spatial variance and covariance, capital/exergy, and governance timing are also
required. Applications therefore begin from a minimum module set and measured observables instead of fitting
all ten states from two series. For material-flows accounting, the lesson is that an admissible closed ledger
must be donor-limited on every outflow edge and closed on every coordinate that the audit invokes. A model
that fails either test is rejected at the audit, not patched by an unregistered residual.

---

## S2. Registered Domain-Template Ladders

The phosphorus and groundwater templates are identification objects. Each ladder declares, for each registered
parameter, the observation that would identify it, the prior range. The observation that would reject the
routing assumption. No constitutive content is claimed. The ladders exist to make the falsification protocol
explicit.

**Definition S2.1 (Phosphorus identification ladder).** The phosphorus identification ladder declares, for
each registered parameter, the triple (identification observation, prior range, rejection observation). The
registered parameters are:

- reserve and resource estimates (economic classification; vintage-dependent); - mining cost and price
  response (which determines the reserve-to-resource conversion); - recovery fractions $\alpha, \rho$ (material-flow
  observations at the waste and product stages); - soil-pool retention and runoff coefficients (mass-balance
  closure at the catchment scale); - the yield functions of the fertilizer conversion (stoichiometric,
  declared per process).

The falsification protocol for each routing assumption is registered. A recovery claim is falsified by a mass-
balance audit of the claimed route. A retention claim is falsified by a catchment closure test. No
constitutive content is claimed. The ladder is an identification object.

**Definition S2.2 (Groundwater identification ladder).** The one-pool affine approximation is the admitted
object. The registered requirements for the two-pool closure are:

- geological geometry (aquitard depth and extent); - multi-depth heads; - pumping tests; - tracer, isotope,
  or water-age evidence; - recharge estimates; - prior ranges for the storage parameters $C_i$ and the
  fast–slow coupling $\kappa_{fs}$; - the discipline that leakage terms may not absorb unexplained residuals.

The two-pool model is not established, and no two-pool claim appears in the main text. For groundwater
accounting, the registered requirements make explicit what would have to be measured to escalate from the one-
pool affine approximation to a two-pool closure. In their absence the one-pool model is the admissible object.

---

## S3. Split-Assignment Mechanism Table

The split-assignment discipline of the main text (Section 2.5) is instantiated by the illustrative pairs
reported below. The pairs are calibrated examples through the logistic two-channel proxy. They have
illustrative status, and no constitutive claim is made for the named domains.

**Definition S3.1 (Split-assignment mechanism pair).** A split-assignment mechanism pair is a pair $(A, B)$ of
mechanisms operating on a stock, with calibrated $\psi$ values drawn from the logistic two-channel proxy, where:

- (H1) Mechanism $A$ removes biomass from existing units (for example, crop export, adult mortality); - (H2)
  Mechanism $B$ degrades replenishment (for example, impaired mineralisation, brood failure); - (H3) Each
  mechanism carries its own calibrated $\psi$ value.

The illustrative calibrated pairs are as follows.

| Domain | Mechanism A (existing-unit removal) | $\psi$ | Mechanism B (replenishment degradation) | $\psi$ |
|---|---|---|---|---|
| Soil zinc | crop export | $0.85$ | impaired mineralisation | $0.25$ |
| Pollinators | adult mortality | $0.70$ | brood failure | $0.20$ |

**Proposition S3.1 (Trough-depth variation).** *Across split-assignment mechanism pairs satisfying (H1)–(H3),
the trough depth varies by a factor of about $1.5$ from mechanism alone.*

*Proof.* Direct computation on the calibrated soil-zinc and pollinator pairs under the logistic two-channel
proxy. The two trough-depth readings differ by approximately the stated factor. The variation is mechanism-
attributable because the underlying stock parameter is held fixed within each domain pair. □

The routing discipline for split-assignment has three clauses. Harvesting pre-recruit stages routes to product
and waste fractions. Habitat-induced failed recruitment is a prevented inflow and must not be routed into
product or waste. Capital-stock damage, compaction, severe soil loss. S a capacity drift or a transfer to the
inert sink. It is not a split channel. For material-flows accounting, the discipline enforces that a prevented
inflow cannot be silently recorded as a product or waste flux: each channel of the typed ledger must carry a
physically admissible direction.

---

## S4. Statement Inventory

We list every claim of the main text with the status it holds, and we promote none. Every statement of the
main text carries one of the following statuses. None is promoted. The inventory is recorded so that any later
use of a statement can be checked against its declared status, in the spirit of explicit scope discipline for
sustainability-accounting claims.

- **Theorems with displayed proofs:** Theorem 1 (support-saturated logistic limit); Theorem 2 (registered-
  family support-saturated identity); Proposition 1 and Theorem 4 (conservation reduction); Proposition 2
  (layer relations); Theorem 3 (flux reconstruction); Theorem 5 and corollary (flux-bounding envelopes);
  Theorem 6 and counterexample (finite exhaustion under uniform drift); Theorems 7–14 (natural-block
  identity, stoichiometric conservation, six-compartment conservation, orthant invariance, no interior rest,
  extinction–geochemical rest, extraction integrability); Theorem 17 (threshold-horizon bracket); Lemma 16
  (specialization deficit identity); Theorem 18 and Corollary 19 (inverse-Gaussian passage and median);
  Theorem 20 (geometric-Brownian passage). - **Theorems whose proofs rest on classical cited results:**
  Theorem 18 (first-passage law, Chhikara and Folks, 1989; Redner, 2001); Theorem 20 (Itô lemma, Øksendal,
  2003); Theorem 10–11 (tangent-cone invariance, Aubin, 1991, in the compartmental lineage of Jacquez and
  Simon, 1993). - **Conditional theorems:** Theorem 15 (hybrid moiety balance), conditional on local
  finiteness, jump factorization, and the yield-routing obligation. - **Definitions:** the certification
  predicates (Section 3.1); the typed safety set (3.2); the feasible balance domain (Definition 1); the
  directional support gap (Definition 2); the depletion trichotomy (Definitions 3–5); the Brownian surrogate
  (Definition 6); the robust semantics (Section 6.4). - **Application records at source status:** the G3P
  index (6.5.1); the applied tables (6.5.2); the phosphate reserve-life ratio (6.5.3); the fisheries
  removals-only time (6.5.4); the constant-production phosphate passage (7.6). - **Boundary statements:**
  the sink obstructions (2.4); the non-reduction boundary with its five reasons and the frozen-donor limit
  (Section 9); the seven non-claims (7.7); the registered template obligations (Section 8). - **Audited
  negative witnesses:** S1 of this file. - **Cohort-sensitivity records:** S5 (fisheries cohort, database-
  version sensitivity).

For ecological-economics measurement, the inventory's role is to keep every claim tied to its declared status.
Theorem, conditional theorem, definition, application record, boundary statement, or audited negative witness,
so that no application claim can be smuggled in as a theorem and no boundary statement can be promoted to a
theorem without an explicit new proof.

---

## S5. Fisheries cohort statistics — corrected protocol and version-sensitivity record

For example, the main-text fisheries column reports the pure-decay proxy $\mathrm{ADH} = F^{-1}\log(\mathrm{SSB}_{\mathrm{now}}/(0.2\max\mathrm{SSB}))$. With **zero entered for any
stock already at or below the reference**, median $\approx 1.8$ yr over the archived 43-stock cohort (RAM Legacy v4.66
extract `fisheries_adh.csv`, pull archived in the analysis repository; the spectral-null subset is the 42 annual-managed
stocks within it, a nested pair, not two cohorts). The quartile summary of $F$ and $\log(\mathrm{SSB}/B_{\lim})$ over that cohort is
defined by, and quoted from, that archived pull alone. The pure-decay proxy is a *first-passage time* (the
time at which a pure-decay trajectory first crosses the reference level $B_{\lim}$). The qualifier "pure-decay" marks
that recruitment is not represented in the trajectory.

**Definition S5.1 (Archived-depletion-horizon protocol).** The archived-depletion-horizon (ADH) protocol is
defined on a stock with finite $F$ and SSB series by

$$\mathrm{ADH} \;=\; \max\!\left(0,\; F^{-1}\log\!\left(\mathrm{SSB}_{\mathrm{now}}/B_{\lim}\right)\right), \qquad B_{\lim} \;=\; 0.2\max(\mathrm{SSB}),$$

Where $\max(\mathrm{SSB})$ is taken over all SSB-finite years. The protocol hypotheses are:

- (H1) the stock's $F$ series has a finite last value (the last finite $F$ of its own series is used; rows
  with $F \le 0$ are dropped); - (H2) zeros are included (below-reference stocks enter as zero, not omitted); -
  (H3) the most-recent-assessment view is used.

**Cohort composition and class scope (verified 2026-09-03).** The 43-stock cohort is a selected class, not a
random sample of assessed stocks. All 43 are small pelagics. 18 anchovy, 20 herring, 4 sprat, 1 sardine
(SSARDCH), the fast-maturing, annually managed class the companion review screen selects by its annual-review
eligibility criterion, with 42 of the 43 being that screen's annual-managed spectral-null stocks (source
caption). The $1.8$ yr median is therefore a class-specific diagnostic for that class, not a statistic of
assessed fisheries in general. The public-release medians below ($2.57$ / $3.39$ yr) are higher because the full
database adds long-lived stocks (cod, rockfish, sharks and other slow-maturing assessed stocks) absent from
the class cohort. The difference between the archived and public medians is cohort composition, not a protocol
or computation discrepancy.

**Broader-cohort comparison (executed 2026-09-03; hybrid placement. Main-text citation in Section 6.5.2).**
The recovered micro-specification (last finite $F$ of its own series; drop $F \le 0$; $B_{\lim} = 0.2\max(\mathrm{SSB})$ over all SSB-finite years;
$\mathrm{ADH} = \max(0, F^{-1}\ln(\mathrm{SSB}_{\mathrm{now}}/B_{\lim}))$; zeros included) was recovered by a protocol grid over the two public releases (Zenodo 14043031 and
2542919, exported via each release's own R loader) and reproduces both anchors to printed precision. V4.66:
454 / 69 zeros / median 3.3893; v4.44: 415 / 63 / 2.5683. The broad v4.66 cohort decomposes by the database's
taxGroup classification:

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

The life-history gradient is clean and monotone across groups. The broad median is carried by the long-lived
groups the class cohort excludes. The fast-turnover groups (shrimps 1.1, carangids 1.6, forage fish 2.7) sit
closest to the class cohort.

**Overlap and vintage.** 33 of the 43 archived ids exist in current v4.66; 10 were dropped or merged, for
example, HERR2532/HERR30/HERR31 $\to$ HERR30-31, HERRVIa $\to$ HERRVIaVIIbc, ANCHMEDGSA17 $\to$ ANCHMEDGSA17-18.
Among the 33, per-stock ADH deltas (current minus archived) average 3.44 yr in absolute value, and the 33's
archived-vintage median of 2.79 yr becomes 2.34 yr on current series. The all-43 archived median of 1.79 yr is
pulled down substantially by the ten since-dropped ids. Its lowness is therefore a property of the extract-
time stock list and series as well as of the pelagic class.

**Random-draw benchmark.** 10,000 draws of 43 stocks without replacement from the broad 454 cohort (and from
the current 64-stock forage-fish group): only 2.12% (0.29%) of sample medians fall at or below 1.7902. The
class cohort's median is unusually low against both pools. This is a descriptive benchmark, not a selection-
bias hypothesis test: the class cohort is a dated extraction with a declared selection rule, not a random
sample from either pool.

**Proposition S5.1 (Specification recovered from the source caption).** *The extract's own example rows verify
the vintage. Four of six published $F$ values reproduce the public RAM Legacy v4.66 release exactly:*

- Adriatic anchovy 17–18: $F = 1.0026$ vs published $1.00$; - North Sea herring: $F = 0.2274$ vs $0.23$; - W. Baltic herring (ICES
  22–24): $F = 0.193$ vs $0.19$; - Argentine anchovy south: $F = 0.0114$ vs $0.011$.

*The zero convention is load-bearing: excluding below-reference stocks would understate the protocol.* The
corresponding ADH values require the extract-time series state. Two example stocks (N. Adriatic anchovy, w.
Scotland herring) no longer carry any series in public releases v4.64–v4.66. Several stocks' SSB series have
since been revised (the North Sea herring series now reaches back to 1947 with a maximum 60% larger than the
extract's, which is exactly the difference between the published ADH 3.5 and the 1.5 the current series
gives).

**Version-sensitivity record** (same protocol. Zeros included, last finite year, most-recent-assessment view,
$F$ column, computed independently on the public releases):

| RAM Legacy release | cohort size | zeros | median ADH (yr) |
|---|---|---|---|
| v4.44 (2018, Zenodo 2542919) | 415 | 63 | 2.57 |
| v4.66 (2024, Zenodo 14043031) | 454 | 69 | 3.39 |

**Proposition S5.2 (Version-sensitivity).** *Neither release reproduces the archived cohort (43 stocks, median
1.8 yr). The difference is not the protocol but the cohort: the archived extract's 43-stock list and its
extract-time series are what the archived pull supplies, and no public release's full-cohort statistic
substitutes for them.*

*Proof.* The same protocol (H1)–(H3) was applied independently to the public releases v4.44 and v4.66. The
resulting medians are 2.57 yr and 3.39 yr respectively, neither matches the archived 1.8 yr median. Since the
protocol is identical across the three pulls, the discrepancy must be attributed to the cohort composition. It
is not to the protocol. □

This is why the main text pins every cohort statistic to the archived pull and quotes no cohort statistic from
a different database version.

**Proposition S5.3 (Archived-pull internal consistency, verified 2026-09-03).** *The archived extract itself
is internally consistent with the recovered specification (H1)–(H3). With $B_{\lim}$ identified as $0.2\max\mathrm{SSB}$ (confirmed row
by row), all 35 positive rows reproduce $\mathrm{ADH} = F^{-1}\log(\mathrm{SSB}/B_{\lim})$ to relative error below $10^{-9}$, and the eight zero rows are exactly
the stocks with $\mathrm{SSB} \le B_{\lim}$ (no zero row has $\mathrm{SSB} > B_{\lim}$). The extract's ADH column is $\max(0, F^{-1}\log(\mathrm{SSB}/B_{\lim}))$ throughout.*

*Proof.* Direct recomputation against the recovered specification, row by row, on 2026-09-03. □

Cohort statistics recomputed from the pull: 43 stocks. 8 zeros.**median 1.7902 yr with zeros included** (the
reported value; $2.8578$ yr over the 35-stock positive sub-cohort). Maximum 201.1797 yr (ANCHMEDGSA7, $F=0.008$, $\mathrm{SSB}/B_{\lim}=5.000$).
Quartiles of $F$: $0.1752$ / $0.2680$ / $0.5298$. Quartiles of $\log(\mathrm{SSB}/B_{\lim})$: $0.2133$ / $0.8019$ / $1.1056$.

The four published-$F$ anchors read off the file itself: Adriatic anchovy 17–18 $F=1.0026$ (published 1.00). North
Sea herring, extract id `HERRNS-IIIa-VIId`, $F=0.2274$ (published 0.23) with $\mathrm{ADH}=3.461$ (published 3.5) w. Baltic herring (ICES 22–24) $F=0.193$
(published 0.19). Argentine anchovy south $F=0.0114$ (published 0.011). The two example stocks that no longer carry
series in public releases are present in the extract (W. Scotland herring `HERRVIa`, ADH 0.385; N. Adriatic anchovy
`ANCHMEDGSA17`, ADH 4.782), confirming the extract predates their removal. The "not reproducible" reading is retracted:
the archived pull is internally consistent and carries exactly the cohort statistics the main text reports.

For ecological-economics measurement, the implication is that an archived, dated extraction with a declared
selection rule is a legitimate unit of analysis when its protocol and cohort are pinned. A public release's
full-cohort statistic is not a substitute. The pure-decay ADH proxy is a class-specific first-passage
diagnostic. It is not a general forecast of fishery removals time, and its cohort-sensitivity record makes
that scoping explicit.

## S6. Statement-Status Naming Offset

*This section records the naming offset between this file and the main text's statement labels: S1–S5 carry
the supplementary's own status words, and the table maps them to the main text's labels.*

The main text's status-word map (status word changed, number unchanged):

| this file's label (S1–S5) | main text's current label |
|---|---|
| Theorem 2 (registered-family support-saturated identity) | Remark 2 |
| Theorem 3 (flux reconstruction) | Lemma 3 |
| Theorem 4 (conservation reduction) | Proposition 4 |
| Theorem 6 (finite exhaustion under uniform drift) | Proposition 6 |
| Lemma 16 (specialization deficit identity) | Remark 16 |
| Theorem 17 (threshold-horizon bracket) | Proposition 17 |
| Theorem 18 (inverse-Gaussian passage) | Proposition 18 |
| Theorem 20 (geometric-Brownian passage) | Proposition 20 |

Every other label in S1–S5 (Theorems 1, 5, 7–15, Corollary 19, Definitions 1–6, and the layering Propositions
1–2) is unchanged and matches the main text. No statement content, hypothesis, proof, number, or recorded
value changed in any of these relabels. Only the status word differs. Every reference resolves by number.
Because the numbers are unchanged, every reference in this file still resolves by number, with this table as
the status-word key.

One further numbering declaration, recorded here for the same reason: the main text runs two statement
counters. The main counter carries the results in order of appearance (with the mixed status words above). The
two layering propositions of the main text's Section 3.1 ("conservation consistency implies accounting
consistency"; "barrier safety does not follow from accounting consistency") carry their own counter,
Propositions 1–2. The main counter's Propositions 4, 6, 17, 18, and 20 join the layering pair to produce the
proposition list 1, 2, 4, 6, 17, 18, 20. The first two are the layering pair, the rest keep their main-
sequence numbers. Each label is unique in the main text and resolves directly. The main text declares this
convention at the layering site.

---

# Part II · Certification obligations, programmes, and the statement inventory

The three sections below hold the material the main text points to instead of carries: the proof obligations
of the certification state (S7), the linear programmes of the closure-cone, deficit and critical-margin
statements with the reading rule for an infeasible programme (S8). The worked exhibits, promotion rules,
reproduction record and extended statement inventory (S9). Section references are to the main text’s
numbering, and the statement labels are the main text’s own.

## S7 · Proof obligations of the certification state (§3.1)

Each entry of `Cert` with the statement that discharges it, the object it needs, and what its absence means. "Not
established" is a status, never a refutation. "not applicable" is a statement about the object, never about
the system it describes.

| Entry | What must be shown | Discharged by | Needs as input | Meaning when not established |
|---|---|---|---|---|
| `Typed` | every compartment carries a material identity, a boundary and a unit, and no column mixes types | §2.1 | the compartment table | the ledger cannot be balanced by addition; arithmetic on it is not meaningful |
| `Balanced` | the accounting identity `S_T v + B_T u_∂ = ḃ` holds as written | §3.2 | flux table and incidence matrix | an entry is missing, duplicated, or routed wrongly |
| `Conserved` | `ℓᵀ C d_x` carries a declared budget and the invariants follow | Definition 23, Proposition 1 | left-null vectors of `S_T`, disturbance budget `ε_ℓ` | conservation is asserted, not certified; the statistical discrepancy is unbounded |
| `Positive` | the nonnegative orthant is forward-invariant | Theorems 10–11 (donor limitation, Nagumo condition) | constitutive laws at the boundary of the orthant | a compartment may go negative, so the ledger admits unphysical states |
| `Admissible` | every term is realizable by the declared chemistry/physics, incl. thermodynamic sign constraints | §3.2 Proposition 2 and its thermodynamic clause | reaction feasibility, energy and entropy balances | a mass-balanced ledger may still be physically impossible |
| `Safe` | declared lower and upper barriers hold over the horizon for every scenario | §3.5 envelope theorem, §6.3–6.4, Theorem 24 | barriers, horizon, declared disturbance class | margin may be violated; the aggregate is at best an alarm |
| `Adequate service` | the readout meets the declared demand relation | §5.1–5.4, Proposition 25 | service definition, production relation | service is delivered by unpriced drawdown of support |
| `Closed` | demand lies in the closure cone, and the deficit is declared at a stated timescale | Definitions 21–22 | stationary-flux LP, process graph, `τ_use` | the shortfall is being carried by the support pool or the sink, in a quantity not stated |

The implications that hold among the entries are exactly those proved in the main text: `Conserved ⇒ Balanced` for the conserved
quantities (Proposition 1), the thermodynamic clause of Section 3.3. Nothing else. `Safe` over a barrier set
contained in the nonnegative orthant implies `Positive` over that horizon. That instance is an artefact of the
declared barrier set and is not an implication between the predicates.

---

## S8 · The linear programmes, their inputs, and the reading rule

All three are ordinary LPs, solved by any simplex or interior-point routine. The exhibit code solves the third
with `scipy.optimize.linprog(method="highs")`.

**1. Closure capacity (Definition 21).** Over variables `(v, λ)`:
```
maximise   λ
subject to S_T v + B_T u_∂ = 0
           0 ≤ v ≤ v̄
           λ D ≤ P v
```
Inputs: incidence operator, declared capacities `v̄`, the boundary-transfer schedule, the demanded
use vector `D`. Feasibility for `λ ≥ 1` is the regime in which the cycle closes at the demanded
rate. The dual is the cut condition on return capacity (Gale, 1957; Ahuja et al, 1993): for every
set of use edges, the return capacity into them must cover the demand placed on them.

**2. Critical-margin multiplier (Theorem 24).** Over variables `λ`:
```
find   λ
subject to λᵀ G S_T + cᵀ ≤ 0
           0 ≤ λ ≤ λ̄        (declared bound, needed for the budget to be finite)
```
If feasible, `T ≤ V(x₀)/(y_req − β)` is available with `β = max λᵀGb` over the declared box.
**Infeasibility carries no conclusion**: it shows only that this multiplier family does not close.
Inputs: the affine margin map `Gx + a`, the service weights `c`, the flux bounds, the required
service rate `y_req`, and the units assigned to each `λ_j`.

**3. Worst concealed deficit (Proposition 30).** Over variables `b`, for each component `j`:
```
minimise   b_j
subject to wᵀ b = z
           ℓ ≤ b ≤ u
```
and `δ*_j(z) = −b_j^min`. Infeasible means the published aggregate `z` is outside the declared box's
image, which is itself a finding about the disclosure, not about the system. Inputs: published
aggregate `z`, weights `w`, and the component bounds `ℓ, u` — the last are what a publisher must
supply, and their absence is why no numeric value for a public indicator is printed in the article.

Exhibit (two components, `w = (0.5, 0.5)`, declared bounds `ℓ = (−4, −4)`, `u = (10, 10)`), from `code/certification_lp.py`:

```
published aggregate z =  0.0 :  displayed split [0.0, 0.0] -> premium Pi =  0.00 ;
                                 concealed deficits delta*_1 = 4.00 , delta*_2 = 4.00
published aggregate z =  1.0 :  displayed split [2.0, 0.0] -> premium Pi =  1.00 ;
                                 concealed deficits delta*_1 = 4.00 , delta*_2 = 4.00
published aggregate z =  3.0 :  displayed split [6.0, 0.0] -> premium Pi =  3.00 ;
                                 concealed deficits delta*_1 = 4.00 , delta*_2 = 4.00
```
The point the exhibit makes is visible in the third line: the same published value is compatible
with a deficit of 4 in *either* component while the premium is reported as 3. The premium and the
concealed deficit are not redundant; one measures the trades that produced the number, the other
measures what the number can hide.

---

## S9.1 · Worked ledger exhibit

We give the statement inventory here so that a reader can check each predicate against the proof. Everything
below is arithmetic on the main text's own declared relations and pinned figures, and on simulated series
inside a declared class. No new data were obtained, and no row of any public table is re-computed here.

**1. Curvature correction (Proposition 27), family `φ(u) = c u^p`, `c = 1`, `u₀ = 1`:**

| `p = κ` | `H_loc` | exact `T` | `T / H_loc` |
|---|---|---|---|
| 0 | 1.0000 | 1.0000 | 1.0000 |
| 0.5 | 1.0000 | 2.0000 | 2.0000 |
| 0.75 | 1.0000 | 4.0000 | 4.0000 |
| 1 | 1.0000 | ∞ | ∞ |
| 1.5 | 1.0000 | ∞ (diverges at the barrier) | — |
| −0.5 | 1.0000 | 0.6667 | 0.6667 |

`T = H_loc/(1 − κ)` reproduces the closed form exactly for every `κ < 1`. At and above `κ = 1` the integral diverges at the barrier,
so the frozen-rate ratio understates without bound.

**2. Reserve-life crossover (Proposition 28), on the pinned record**. Reserves 74,000,000 kt, production
240,000 kt/yr (USGS *Mineral Commodity Summaries* 2026, as tabulated in §6.5.3), `τ = 308.33` yr, `g = 0.03 yr⁻¹`:

| `η` | `T` (yr) | `T/τ` |
|---|---|---|
| 0 | 77.58 | 0.252 |
| 0.25 | 86.34 | 0.280 |
| 0.50 | 99.01 | 0.321 |
| 0.75 | 121.25 | 0.393 |
| 0.90 | 151.27 | 0.491 |
| 0.99 | 227.70 | 0.739 |

The first-order condition for the ratio to be conservative is `η ≥ ½gτ = 4.625`, outside the admissible interval `0 ≤ η ≤ 1`: the
reserve-life ratio is optimistic in a direction fixed by the model class, independent of the data.

**3. Persistence index on the declared trend class (Proposition 32)**. 400 replicates, `β = σ = 1`, seed 7, `index = (a_n − min_k a_k)/(−fitted slope)`:

| `n` | mean | median | 90th pct | implied stock drop |
|---|---|---|---|---|
| 10² | 0.211 | 0 | 0.812 | 98.9 |
| 10³ | 0.247 | 0 | 0.835 | 998.9 |
| 10⁴ | 0.206 | 0 | 0.953 | 9 999.1 |
| 10⁵ | 0.246 | 0 | 0.999 | 99 999.0 |

Flat in record length while the stock falls by five orders of magnitude: the statistic is a trend-detection
quantity expressed in years.

**4. Aggregate non-transport (Proposition 31)**. `k = 1`, barrier `x_i ≥ 1`: starts `(2, 98)` and `(50, 50)` give the identical
aggregate `Z(t) = 100e^{−t}` with first component exits at 0.6931 yr and 3.9120 yr respectively.

**5. Certificate vectors of the three classified indicators:**

| Indicator | Typed | Balanced | Conserved | Positive | Admissible | Safe | Adequate | Closed |
|---|---|---|---|---|---|---|---|---|
| G3P anomaly-persistence index (§6.5.1) | not est. | established | n/a | n/a | n/a | n/a | n/a | n/a |
| phosphate reserve-life ratio (§6.5.3) | not est. | established | n/a | n/a | n/a | n/a | n/a | n/a |
| fisheries removals-only pressure time (§6.5.4) | not est. | established | n/a | n/a | n/a | not est. | n/a | n/a |

Each row is the main text's own classification written in the vector's alphabet: a statistical index or an
arithmetic ratio declares no compartments, no barriers and no production relation. Six of the eight entries
are not applicable instead of failed. The fisheries row records `Safe` as not established because a pressure
scale states a rate against no declared barrier.

---

## S9.2 · Promotion-rule table

For example, when a published ratio may be read as an event time. Every condition listed is stated somewhere
in §6.5.1–6.5.4 of the main text. The table collects them so that the promotion test is checkable in one
place, and it adds no condition.

| Published object | To be read as an event time only if | Article's own note |
|---|---|---|
| reserve-life ratio `R/P` | `R` is a fixed physical inventory, `Ṙ = −P`, `P` constant, and no discovery, price response or reclassification occurs | §6.5.3: the reserve classification is economic; the premises are carried, not discharged |
| anomaly index `(a_n − min a)/(−trend)` | an absolute stock-to-barrier distance is identified, i.e. geometry and storage coefficient supply an anchor, and the trend persists | §6.5.1: not identifiable from an anomaly series; adding a constant to the series and the reference leaves every observation unchanged |
| removals-only pressure time `log(B/B_min)/F` | `Ḃ = −FB̄` with `F` constant, no growth, no recruitment, no catch misreporting | §6.5.4: exact hitting time of the declared removals-only law, nothing more |
| cohort median or mean of any of the above | the cohort is a sample of the population the claim is about | §6.5.2: a selected class, 43 small pelagics, not a random sample |
| a scenario-conditioned hitting time | the scenario, drift, barrier and noise class are declared and the surrogate is not read as the ledger | §7.6, §7.7 |

The rule has a one-line form: **a ratio becomes an event time only when its denominator is a declared constant
law of the stock itself and its numerator is a physical inventory.** Absent that, it remains an index, a
ratio, or a pressure scale, which is the status §6.5 assigns.

---

## S9.3 · Reproduction

`code/persistence_index_simulation.py` (Proposition 32), `code/curvature_and_crossover.py` (Propositions 26–28), `code/certification_lp.py` (premium, `δ*_j`, Proposition 31, and the vectors of S-C.5).
Fixed seed 7. `numpy` and `scipy` versions recorded in `code/MANIFEST.md`. Complete stdout in `code/outputs.txt`. The scripts read no data beyond
the figures quoted in the main text. Every printed value is reproducible from this file alone.

## S9.4 · Statement inventory, extended form

Main counter 1–47, with the layering counter (Propositions 1–2) separate, per §3.1. Every statement numbered
from 21 onward, with the section it sits in:

| Label | Section |
|---|---|
| Definition 21 (Closure cone) | 2.1 |
| Definition 22 (Closure deficit at the use timescale) | 2.1 |
| Definition 23 (Bounded residual) | 3.4 |
| Theorem 24 (Critical-margin budget) | 3.6 |
| Proposition 25 (Accumulated liquidation certified by delivered service) | 5.4 |
| Proposition 26 (Sign of the frozen-rate error) | 6.2 |
| Proposition 27 (Curvature correction) | 6.2 |
| Proposition 28 (Reserve-life crossover) | 6.2 |
| Proposition 29 (The certifying aggregator is unique) | 10.1 |
| Proposition 30 (Worst concealed deficit) | 10.1 |
| Proposition 31 (Aggregates do not transport event times) | 10.1 |
| Proposition 32 (Boundedness of the persistence index on the declared trend class) | 6.5.4 |
| Remark 33 (One-signed bias of an aggregate overshoot date) | 10.2 |
| Definition 34 (Composition of typed ledgers) | 3.7 |
| Remark 34 (What the multiplier search can and cannot prove) | 3.7 |
| Definition 35 (Interface price) | 3.7 |
| Remark 35 (What a non-displacement gate can say on this apparatus) | 3.7 |
| Proposition 36 (Conservation composes; closure does not) | 3.7 |
| Remark 36 (What the type structure yields, and what it does not) | 3.8 |
| Proposition 37 (Margin needed, and the admissible exchange rate) | 3.7 |
| Remark 37 (Two component ratios are identities at a world aggregate) | 10.2 |
| Definition 38 (Identifiability set of an event time) | 6.6 |
| Proposition 39 (The set is a polytope image, and it is usually an interval) | 6.6 |
| Definition 40 (Compensation as a decidable predicate) | 3.7 |
| Proposition 40 (An empty corridor comes with a named conflict) | 3.7 |
| Definition 41 (Control margin) | 3.7 |
| Proposition 41 (The deadline has a closed form, and it is not the horizon) | 3.7 |
| Definition 42 (Affinity, the fourth admissibility predicate) | 3.7 |
| Proposition 42 (No conservation law crosses a type class) | 3.8 |
| Definition 43 (Circulation time) | 3.7 |
| Proposition 43 (The institutional-failure subsystem is exactly closed) | 9 |
| Definition 44 (Governability ratio) | 3.7 |
| Definition 45 (Latest safe intervention time) | 3.7 |
| Definition 46 (Supportable-output envelope) | 3.7 |
| Definition 47 (Type structure) | 3.8 |

Two unnumbered notes sit alongside the inventory: *Certification state* in §3.1 and *Antecedents* in §1.2,
together with the refute/alarm clause in §10.1, the joint-minimal reporting note in §6.3, and the review-
interval note in §9. The disturbance/residual material is not unnumbered: it is Definition 23 in §3.4.

---

# Part III · Checkability records and the detail behind the applied sections

For example, the two tables below record what is and is not checkable in the applied classifications. The
records after them hold material the main text points to instead of carries: the extraction provenance of the
G3P basin rows (S5.4, continuing the S5 record it belongs to), the registered domain-template ladders (S14,
next to the S2 ladders they elaborate). The proof-obligation row for `Typed` (S15, which cites the main text’s
Definition 47 in place of an undefined use of the word “typing”). S5.4 and S14 give that material at its full
extent.

## S10 · Per-parameter identifiability status, with the main text's labels

Status vocabulary is the main text's own (§3.1): *established*, *not established*, *not applicable*. A value
is established when the observation map pins it relative to a declared model and record. Not established when
the record leaves it free. Not applicable when no identification question is live for it, which is the correct
status for a convention, and is not a failure. Status belongs to the pair (model, readout), never to the
parameter alone.

| quantity | enters | identification question | status | what would settle it |
|---|---|---|---|---|
| $\mathsf{Ty}, \mathrm{ty}, \mathsf{Cv}$ (type structure) | Def. 47, Prop. 42, `Typed` | none — declared | **not applicable** | — (a re-declaration, not an estimate) |
| $\Lambda^{*}$ closure capacity | Def. 21, `Closed` | is the LP feasible on the declared capacities? | **established** (as the value of a programme on declared data) | nothing further; its *inputs* are the declared capacities |
| $\kappa_m,\ \delta_m$ (reclassification deficit) | Def. 22, Prop. 28, Rem. 35 | is a reclassification series published by the reserve authority? | **not established** — read from a declared box in S9 | a publisher-declared reclassification series (none exists for USGS reserve classes) |
| $\tau_{\mathrm{use}}$ (timescale of the deficit readout) | Def. 22's $\kappa_m$ | none — declared by the analysis | **not applicable** | — |
| $\bar\delta,\ g_m$ (bounds on reclassification and demand growth) | Def. 22's horizon $T \le m_0/(\underline\delta g_m)$ | published bounds? | **not established** (bounds only, declared) | a declared source for the growth bound; the horizon is reported with it |
| $\mathcal A_{\min}$, $\mathcal A_{\max}$ (barriers) | `Safe`, Def. 45, Prop. 41 feasibility | none — declared | **not applicable** | — |
| $d_0,\ \rho,\ \tau$ (drawdown level, ramp rate, delay) | Prop. 41's $m_{\mathrm{needed}}$, $t_{\mathrm{last}}$ | published values for any named ledger? | **not established** — the article's two instances are illustrative | an empirical declaration by whoever runs the certificate |
| $H^{\mathrm{loc}}$ (frozen-rate ratio) | Prop. 26, Def. 46's corner | computable from the declared pair? | **established as a ratio**; its direction against $T$ is established **only under** Prop. 26's monotonicity hypothesis | the monotonicity (or a declared $\varphi$) |
| $q_i$ (normalisation choice) | Def. 23, Prop. 36 | none — freely chosen | **not applicable**, with Prop. 36's compatibility condition as the price | — |
| $\varepsilon_\ell$ (disturbance budget) | `Conserved` | declared, then checked against the record? | **established relative to the declaration** | the declared class |
| G3P $\widehat{\dot a}$, $a_{\mathrm{hist,min}}$ | $L_{\mathrm{hist}}^{\mathrm{anom}}$ (§6.5.1) | reproducible from the product's basin masks? | **not established numerically** — the rows are quarantined for reuse for exactly this reason, and the product documents a faulty June-2005 snow entry that the window spans | re-derivation from the masks, with the June-2005 choice declared |
| G3P anomaly reference period | the same index | is the baseline published? | **established** — April 2002 to December 2020, per the product documentation; coverage ends September 2023 | — |
| $\mathrm{SSB}_{\mathrm{now}},\ F_{\mathrm{now}},\ B_{\lim}$ | $\Theta_F$, the ADH proxy | defined by the protocol on the archived cohort | **established on the cohort**; **not established** as a statement about the population of assessed stocks | nothing further: the extract is pinned to release v4.66 (Zenodo 14043031, 6 Nov 2024) and its vintage is verified from its own contents in S5.1 (four of six published $F$ values reproduce that release exactly), with the cohort recomputed in S5.3 to $10^{-9}$ |
| reserves, production | $T_{\mathrm{reserve}}$ (§6.5.3) | published for a stated vintage? | **established for the vintage named**, not established forward | the vintage statement, which the row carries |
| $\tau_{\min},\ \tau_{\mathrm{agg}}$ (premium, Remark 33) | the overshoot premium | computable from the published accounts? | **established as arithmetic** on the published ratio; the zero-carbon-biocapacity row is **not applicable** as a modelling choice — it is the accounts' documented convention, cited in Remark 33 | whether the author also reports the carbon-demand-excluded variant |

No cell in these tables is left for the author to fill. Every row was read off the main text, the deposited
repository at `refs/tags/edwards-framework-e1`, or a published source. The cell that would otherwise have required the analysis repository
is closed by the release identifier together with S5.1’s row-level vintage check, a stronger claim than a pull
date.

## S11 · Material and energy value: what is checkable, and what is not

The position we record it here so that it can be cited, tested, and kept out of the main text's claim list.
Each row states the position's clause, the object in the main text that carries it, and its status.

| clause of the position | object in the article | status | what is *not* claimed |
|---|---|---|---|
| value may be assessed only within a type; no substitution across types | Definition 47's predicate, and Proposition 42's splitting $\ker S_{\mathcal T}^{\top} = \bigoplus_\gamma \ker S_\gamma^{\top}$ | **established for conservation laws** | no theorem about worth: Proposition 42 says no conserved quantity prices one class against another, which is not the same statement as "value is not comparable" |
| no cross-type compensation in an aggregate | Proposition 29 (the calibrated monotone certifier is `= min`, and continuity with certification and strict monotonicity are incompatible) | **established** | no claim that a compensating index is useless; only that it is not a certificate |
| an effect at the interface must be re-declared, not summed | Definition 23 (free choice of normalisation) with Proposition 36 (conserved quantities do not compose unless compatible on the classes) | **established as a conditional** | no blanket invariance |
| boundary redrawing does not change what is conserved | Remark 36's reporting-boundary clause | **established under a hypothesis**: redrawing is harmless exactly while no conversion is declared or withdrawn | not invariance to redrawing *inside* a class — Proposition 36 governs that, and it can fail |
| reclassification is bounded by a declared elasticity | Definition 22's $\delta_m$, $\kappa_m$; Proposition 28 | **established as a deficit bound** | no forecast of reclassification, and no estimate of its rate |
| a certificate should carry an "MDV" field | no such field exists in the article | **not established here**; supplementary/project-side only | the article's `Cert` vector has eight entries and none of them is a value-type score |
| one umbrella invariance theorem covering all of the above | declined in favour of the per-case results (Propositions 28, 29, 36, 40, 42 and Definition 47) | — | the umbrella's hypotheses would have to include a primitive the article does not define |

## S5.4 · G3P basin-row extraction provenance (the record behind main-text Section 6.5.2)

*The main text keeps the classification sentence and this record's pointer. What follows is the demoted
provenance, reproduced without change. Deictic words are the main text's: "the classification status assigned
below" named the table that still follows it there.*

The basin rows are reported extractions from the G3P v1.12 basin series, used here only to exhibit the index
construction of Section 6.5.1. The window-minimum column is implied by the displayed trend and horizon through
the index formula of Section 6.5.1, arithmetic. It is not product-endorsed. Nd every basin row must be re-
derived from the product's basin masks before any numerical reuse. The Indo-Gangetic magnitude is the extreme
case: it sits an order of magnitude beyond published basin-mean groundwater-equivalent trends (typically a few
cm yr$^{-1}$). A linear trend of $-49.7$ cm yr$^{-1}$ maintained over the reported $\approx 21.4$ yr window would place the fitted
2002 value near $+6.5$ m above the anomaly reference. The fitted segment convention is part of the quarantine.
The rows are retained only as the worked instance of the index construction. The classification status
assigned below does not depend on the magnitudes.

## S14 · Registered domain-template detail (the full extent behind main-text Sections 8.1 and 8.2)

*The main text now states the registered status and the gap for each template and points here. The ladders
above (S2) are the objects these paragraphs name, so the two records belong together.*

### 8.1 The phosphorus template

The phosphorus domain enters at registered template status: an identification ladder for the
resource–product–waste–detritus structure of Section 2.3 (phosphate rock → fertilizer → soil pool → runoff,
with the mining flux $c_G$ and the recycling routes $\alpha, \rho_P$), whose constitutive content. The yield and loss
functions, the recovery fractions, the price response of the reserve classification, is declared, not
established. The reserve and production quantities used in Section 6.5.3 carry their source vintage (U.S.
Geological Survey, 2026). The template's competing-model ladder is an identification object, and its
falsification protocols (which observation would reject which routing assumption) are recorded obligations,
not results.

### 8.2 The groundwater template and the two-pool gap

For example, the groundwater template enters at registered status with an admitted object and a declared gap.
The admitted object is the one-pool affine approximation behind the anomaly-persistence index of Section
6.5.1. The two-pool model (active storage with a slow donor pool, the two-compartment structure of Section
2.2) is not established. The registered identification requirements for closing the gap are: geological
geometry (aquitard depth and extent). Multi-depth heads. Pumping tests. Tracer, isotope, or water-age
evidence. Recharge estimates. Prior ranges for the storage and fast-slow coupling parameters, and the
discipline that leakage terms may not absorb unexplained residuals.

## S16 · S7's discharge column, restated against the main text's labels

For example, three of S7’s “discharged by” pointers name sections that no longer carry the statements they
cite. None of the three is wrong in substance. The table below gives the labels to read against the main text
as it stands. The `Typed` row is corrected in S15 instead of here.

| Entry | S7 says | Read this instead |
|---|---|---|
| `Balanced` | §3.2 | Lemma 3, with the typing of Definition 47 |
| `Conserved` | Definition 23, Proposition 1 | Proposition 4 with Theorems 7–9; Definition 23 is now the bounded-residual clause of §3.4, and the Proposition 1 of that row is the layering counter's, not the main counter's |
| `Admissible` | §3.2 Proposition 2 and its thermodynamic clause | Definitions 1 and 42, with Proposition 40 for the empty-corridor case |
| `Safe` | §3.5 envelope theorem, §6.3–6.4, Theorem 24 | Theorem 24 unchanged, plus Definitions 45 and 46 for the deadline and the envelope it is read against |

The same care applies to the sentence after the table: "`Conserved ⇒ Balanced` for the conserved quantities (Proposition 1)" is
the layering counter's Proposition 1, which is the main counter's Proposition 4.

## S15 · `Typed` proof-obligation row, corrected

| predicate | statement | main-text locus | witness | fails when |
|---|---|---|---|---|
| `Typed` | every compartment carries a declared type and unit, and no column of `S_T` is both a transfer and a conversion | Definitions 47, Proposition 42 | the declaration `(Ty, ty, Cv)` itself | a row sums unlike types, or a conversion is booked as a sum |

`Typed` is the only one of the eight obligations decidable from a declaration alone instead of from a declaration
and a trajectory. Proposition 42 states what no such check can deliver, namely a conservation law crossing a
type class.

## S17 · The overshoot-date recomputation, and the significance of a difference of a few days

*This section records the recomputation of the aggregate overshoot date with and without carbon demand, on two
editions of the National Footprint and Biocapacity Accounts, with the data provenance, the arithmetic and the
reproduction command in full. The main text carries its conclusions in Section 10.2 and Remark 37.*

**Data.** Two editions of the National Footprint and Biocapacity Accounts, chosen because they are the newest
ones obtainable without an account: the 2018 edition (series 1961–2014, the release Lin et al. (2018)
documents) and the 2017 edition (1961–2013), both deposited by the publisher under CC BY-SA 4.0. The tables
are held with the analysis record so that the run can be repeated without a network; they are not
redistributed with the deposit, whose copy of the record carries `source/MANIFEST.md` with the two retrieval commands and the
hashes that settle what was read. edition is free but registration-gated, so the 2022 row quoted in the main
text's Remark 33 is not reproducible from an open download, and the limitation is recorded here. The checksums
of the two tables as read: 60968f7c9959537f8e67f915aca4259662b5cd42c3a0ec02d094677b4c280ef6
NFA_2018_edition_kaggle.csv 11857080 bytes · 0dd766d975cd5e85f2a2d39cff1f914b92c514186ce507cb1f721a63be57b6a5
NFA_2017_edition_kaggle.zip.csv 13195855 bytes

**Arithmetic.** Exactly the main text's, on the publisher's `World` rows: component totals in gha for `record ∈ {BiocapTotGHA, EFConsTotGHA}`, then
$\tau_{\mathrm{agg}} = 365\sum_i b_i/\sum_i d_i$ and $\Pi_\tau = \tau_{\mathrm{agg}} - 365\min_i(b_i/d_i)$, computed once with all six demand components (ALL, the published convention, in which the carbon
row's zero biocapacity forces the minimum ratio to 0 and the premium to the whole date) and once with carbon
demand removed from numerator and denominator and the weights renormalised over the five components of
positive biocapacity (NOC, the main text's restricted set). No interpolation, no model, no network, no third-
party library.

**Results.** The 2018 edition, world aggregate, days of a 365-day year:

| year | carbon share of demand | τ_agg, carbon in the ratio set | τ_agg, carbon demand excluded | gap, d | restricted premium |
|---|---:|---:|---:|---:|---:|
| 1961 | 43.9% | 498.7 d | 889.5 d | 390.8 d | 524.5 d |
| 1980 | 55.4% | 307.1 d | 688.3 d | 381.1 d | 323.3 d |
| 2000 | 55.3% | 266.2 d | 595.3 d | 329.2 d | 230.3 d |
| 2005 | 58.6% | 237.1 d | 571.9 d | 334.9 d | 206.9 d |
| 2006 | 59.5% | 231.5 d | 572.1 d | 340.6 d | 207.1 d |
| 2007 | 60.3% | 225.9 d | 568.8 d | 342.9 d | 203.8 d |
| 2008 | 60.3% | 226.8 d | 571.2 d | 344.4 d | 206.2 d |
| 2009 | 60.1% | 230.0 d | 576.5 d | 346.5 d | 211.5 d |
| 2010 | 61.3% | 219.4 d | 567.1 d | 347.7 d | 202.1 d |
| 2011 | 61.6% | 215.8 d | 561.9 d | 346.0 d | 196.9 d |
| 2012 | 61.4% | 216.1 d | 559.3 d | 343.2 d | 194.3 d |
| 2013 | 60.8% | 215.3 d | 549.6 d | 334.3 d | 184.6 d |
| 2014 | 60.2% | 216.5 d | 543.9 d | 327.4 d | 178.9 d |

Four findings, each reproducible from the table by inspection.

1.**The premium's downward trend survives the exclusion.** With carbon demand removed, the restricted premium
on this release runs 524 d (1961), 323 d (1980), 230 d (2000), 179 d (2014); the decade means are 1960s 464 d,
1970s 358 d, 1980s 288 d, 1990s 253 d, 2000s 216 d, 2010s 191 d, with 45 of 53 year-on-year changes negative.
The article's series. 547, 346, 251, 173 d, read off a later edition. Carries the same sign and shape and sits
4–8% above this release on the shared years, which is a further instance of the point the main text makes about
vintages rather than a contradiction of it. 2.**The two conventions part by about a year, and by a known
factor.** Over 2005–2014 the restricted date exceeds the published-convention date by 340.8 d on average
(327.4–347.7 d), a ratio of 2.41 to 2.60, and that ratio equals $1/(1-s_{\mathrm{carbon}})$ to within 4.4e-16, with $s_{\mathrm{carbon}}$ between 58.6%
and 61.6%. Excluding carbon demand multiplies the reported date by a factor of two and a half rather than
refining it. 3.**The restricted date is the fragile one.** From the 2017 to the 2018 edition the aggregate
date moves by 1.1 d on average and 1.9 d at most on a closed year, while the restricted date moves by 6.3 d on
average and 9.1 d at most, a factor of 5.8. The reason is structural: the excluded denominator is the smaller
quantity, so an absolute revision in the non-carbon components is divided by less. A headline-versus-
recomputed difference of a few days is inside that noise for the restricted date and outside it for the
aggregate date, so whether a difference of a few days is material depends on which date it concerns.
4.**Aggregation level accounts for as much as vintage does.** Reading the publisher's `World` row rather than
summing the national rows moves the aggregate date by up to 9.2 d over the last decade of the release; and
summing them *including* the `World` row —. E natural first attempt at a world total in a table that carries both,
— a. Rror this section documents, which doubles both sides of every ratio, which leaves the number of Earths
untouched and moves the date by about a week. A few-day disagreement between a published headline and a
reader's own recomputation is therefore expected, and it is not primarily a matter of vintage.

**The identity the main text's Remark 37 records.** $r_{\mathrm{crop}} = r_{\mathrm{built}} = 1$ exactly in 54 of 54 years, and $\tau_{\min}^{\mathrm{NOC}} = 365$ d in 54 of 54: at a
world aggregate the footprint of a component whose demand *is* the area is priced at world-average yields, so
biocapacity and demand coincide by construction. The restricted minimum is thus not an observed convergence,
and any reading of the premium as the components coming together has to name the level at which it was
computed.

**Reproducing and extending.** `analysis/nfa_tau/recompute_tau.py`, with the per-year outputs `tau_by_year_2018edition.csv` and `tau_by_year_2017edition.csv`, the revision ledger `edition_delta.csv`, the
complete stdout `results.txt`, `checksums.txt`, the two tables as fetched under `source/` with a manifest recording their retrieval
commands and the hashes of the archive and its extracted member, and a `README.md` recording the licence, the
aggregation trap and the reason the current edition is not fetched. A newer edition of the accounts is run by
supplying a different input file; the arithmetic is unchanged.
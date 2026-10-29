# Supplementary Material v19 — Typed Flux Ledgers and Depletion Arithmetic

*Accompanies main-text Version 51 (29 October 2026): "Typed Flux Ledgers and Depletion Arithmetic: Conservation, Componentwise Diagnostics, and the Semantics of Depletion Horizons."*

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
parameter, the observation that would identify it, the prior range, and the observation that would reject the
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

**Record S3.2 (Status of the trough-depth comparison).** Conditions (H1)–(H3) and the four
illustrative $\psi$ values do not by themselves define a trough depth: that quantity depends on
the proxy equations, stock parameters, forcing, and time window. Those proxy specifications and
code are not part of the v51 package, so the trough-depth factor reported in earlier drafts is
withdrawn as a proposition in v19. The retained content is the mechanism table and the routing
discipline below; neither depends on a numerical trough-depth factor.

The routing discipline for split-assignment has three clauses. Harvesting pre-recruit stages routes to product
and waste fractions. Habitat-induced failed recruitment is a prevented inflow and must not be routed into
product or waste. Capital-stock damage, compaction, and severe soil loss are a capacity drift or a transfer to the
inert sink. It is not a split channel. For material-flows accounting, the discipline enforces that a prevented
inflow cannot be silently recorded as a product or waste flux: each channel of the typed ledger must carry a
physically admissible direction.

---

## S4. Statement Inventory

This inventory records the status of the main text's claims without promoting any of them. The
complete label-and-section list is S9.4. References are by the ordered pair (kind, number): for
example, Definition 34 and Remark 34 are different statements, and a bare number is not a
complete citation.

- **Definitions and declared constructions:** Definitions 21–23 (state-conditioned closure;
  return kernel with late return separated from ultimate loss; bounded residual), Definitions
  34–35 and 40–47 (composition, interface price, compensation, control/affinity/circulation/
  governability objects, latest safe intervention, supportable-output envelope, and type
  structure), and Definitions 1–6 and 38.
- **Proved structural statements:** Theorem 1; Propositions 1–2 on the layering counter; Lemma 3
  (flux identifiability fibre, not unconditional reconstruction); Proposition 4; Theorem 5;
  Proposition 6; Theorem 24; Propositions 36–37; Proposition 40; Proposition 41 only as the
  scalar frozen-drawdown specialization of Definition 45; Proposition 42 only for typed scalar
  conservation readouts; Theorems 7–14; Proposition 17; Propositions 25–28; Proposition 32
  (proved limiting law, with simulation as exhibit); Proposition 39; and Propositions 29–31.
- **Classical facts restated for notation:** Proposition 18, Corollary 19, and Proposition 20.
  They concern declared stochastic surrogates, not stochastic completions of the ledger.
- **Conditional statements:** Conditional Theorem 15 (hybrid moiety balance) and Proposition 43
  (closure only under Interface Hypothesis I). The §9 non-reduction result is scoped to
  coordinate-preserving exact factors and the regular approximations defined there; it is not a
  claim about arbitrary coordinate-mixing conjugacies.
- **Remarks and boundary records:** Remarks 2, 16, 33–37, Non-example 1, the sink obstructions,
  the seven non-claims of §7.7, and the registered-template obligations of §8. Remarks are not
  promoted to theorems by being listed here.
- **Application records at source status:** the quarantined G3P index construction, the pinned
  USGS MCS 2026 phosphate table, and the fisheries removals-only/ADH records. The v51 package
  recomputes only the items named in S9.3; it does not re-derive the G3P extraction, rebuild RAM
  cohorts from source releases, or recompute the National Footprint edition tables.

Theorem/definition status therefore travels with the exact hypotheses printed in the main text.
In particular, stationary closure, service adequacy, trajectory safety, and strong/weak
assessment semantics are separate predicates; no inventory entry collapses them.

---

## S5. Fisheries cohort statistics — corrected protocol and version-sensitivity record

For example, the main-text fisheries column reports the pure-decay proxy $\mathrm{ADH} = F^{-1}\log(\mathrm{SSB}_{\mathrm{now}}/(0.2\max\mathrm{SSB}))$. With **zero entered for any
stock already at or below the reference**, median $1.7902$ yr over the archived 43-stock cohort (v51 file
`v51/data/fisheries_adh_archived_43.csv`; the spectral-null subset is the 42 annual-managed
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

**Random-draw benchmark (exact finite-population form).** For a uniformly random draw of 43 stocks
without replacement, the sample median is at or below the archived exact median $1.7902112680$ yr
exactly when at least 22 drawn ADH values are at or below that threshold. The hypergeometric tail
is therefore exact, with no Monte Carlo seed: from the broad 454-stock v4.66 cohort (164 values at
or below threshold) the probability is $2.472112\%$; from its 64-stock forage-fish group (26 at or
below threshold) it is $1.289214\%$. The class cohort's median is unusually low against both pools.
This is a descriptive benchmark, not a selection-bias hypothesis test: the class cohort is a dated
extraction with a declared selection rule, not a random sample from either pool. (Earlier Monte Carlo
percentages based on the rounded threshold 1.7902 are superseded by this exact calculation.)

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

**v51 reproduction boundary.** `v51/code/fisheries_cohorts_v51.py` recomputes, from the three CSVs
distributed in `v51/data/`, the cohort sizes, zero counts, and medians (archived $n=43$, 8 zeros,
$1.790211$ yr; RAM v4.44 $n=415$, 63 zeros, $2.568299$ yr; RAM v4.66 $n=454$, 69 zeros,
$3.389282$ yr); checks every archived row against $\max(0,F^{-1}\log(\mathrm{SSB}/B_{\lim}))$;
reproduces the v4.66 taxonomic table and the 33-of-43 exact identifier overlap; and evaluates the
exact random-draw benchmark above. It reads each file's actual ADH column (`ADH_yr` archived;
`ADH` in the RAM files). It does not rebuild any cohort from a RAM Legacy database release or
recover the original protocol grid; those upstream extraction records remain source records.

## S6. Statement-label reading rule

Version 51 is cited by **kind and number together**. Propositions 1–2 are the layering pair in
main-text §3.1. All other references likewise require their kind word: Definition 34 and Remark
34, Definition 40 and Proposition 40, and Definition 42 and Proposition 42 are distinct labels.
A bare number therefore does not resolve a reference in v51. The inherited numbers are retained
for traceability across revisions and are not a promise of appearance order.

For readers comparing older drafts, the former status-word offsets were: registered-family
support-saturated identity, now Remark 2; flux identifiability, now Lemma 3; conservation-law
projection, now Proposition 4; finite exhaustion under uniform negative drift, now Proposition 6;
specialization deficit identity, now Remark 16; threshold-horizon bracket, now Proposition 17;
inverse-Gaussian passage, now Proposition 18; and geometric-Brownian passage, now Proposition 20.
Those historical aliases must not be used as v51 citations. In particular, Proposition 1 is the
conservation projection of an already balanced trajectory; it is not Proposition 4, and neither
statement says that structural left-nullity alone makes an arbitrary curve balanced.

---

# Part II · Certification obligations, programmes, and the statement inventory

The three sections below hold the material the main text points to instead of carries: the proof obligations
of the certification state (S7), the linear programmes of the closure-cone, deficit and critical-margin
statements with the reading rule for an infeasible programme (S8). The worked exhibits, promotion rules,
reproduction record and extended statement inventory (S9). Section references are to the main text’s
numbering, and the statement labels are the main text’s own.

## S7 · Proof obligations of the certification state (§3.1)

Each entry of `Cert` with the statement that discharges it, the object it needs, and what its absence means. "Not
established" is a status, never a refutation. "Not applicable" is a statement about the object, never about
the system it describes.

| Entry | What must be shown | Discharged by | Needs as input | Meaning when not established |
|---|---|---|---|---|
| `Typed` | every compartment has declared type/unit; transfer-routing and conversion columns obey Definition 47 | Definition 47 and Proposition 42 | type/unit table, routing columns, conversion templates | no typed conservation readout is licensed; any numerical cross-type sum is only an additional untyped readout |
| `Balanced` | the declared trajectory satisfies $\dot x=S_{\mathcal T}v+b$ with $b=B_{\mathcal T}u_\partial+d_x$ | §2.1; Lemma 3 characterizes compatible flux fibres | incidence/boundary operators, flux and total boundary/disturbance records | a term is missing, duplicated, misrouted, or the readout does not determine the claimed fluxes |
| `Conserved` | for each claimed $\ell$ with $\ell^\top S_{\mathcal T}=0$, the projected law $d(\ell^\top x)/dt=\ell^\top b$ and its residual budget hold | Propositions 1 and 4; Definition 23 for the residual budget | left-null covectors and the total $b$, not boundary flux alone | conservation is asserted rather than certified for that readout |
| `Positive` | the nonnegative orthant is forward-invariant under the declared donor-limited laws | Theorems 10–11 for the closed ledgers treated there; otherwise a system-specific invariance proof | boundary constitutive laws and donor limits | a compartment may go negative, so the ledger admits unphysical states |
| `Admissible` | columns, capacities, donor limits, and any declared affinity/constitutive predicates are jointly realizable | Definitions 21, 34, 42, and 47; Proposition 40 names an empty declared corridor | process declarations, joint capacities, boundary schedule, and energies if affinity is invoked | a formally balanced ledger may still use an impossible or donor-unlimited process |
| `Safe` | every declared componentwise barrier holds on the stated horizon and response class | §3.2, Theorem 5 or Theorem 24 where applicable, and Definitions 45–46 for deadline/envelope questions | barriers, initial state/history, horizon, disturbances, and admissible responses | some component margin may be violated even if an aggregate remains acceptable |
| `Adequate service` | the componentwise service relation is met without relying on an undeclared support/pipeline draw | §5, including Proposition 25 | service definition, production/return processes, available and pipeline stocks, replenishment | output may be financed by support drawdown or an unfinanced return pipeline |
| `Closed` | at a named frozen state and boundary schedule, a stationary feasible pattern meets the demanded output fraction; late return and ultimate loss are separately reported | Definitions 21–22 | state-conditioned joint capacities and kernel/history where dynamic interpretation is claimed | stationary closure is not established; this alone says neither that current service is impossible nor that drawdown is permanent |

No unproved implication among these predicates is available. In particular, `Balanced` plus a
left-null covector gives its projected conservation law (Propositions 1 and 4); structural
left-nullity alone does not make an arbitrary curve balanced, and accounting consistency does not
imply barrier safety (Proposition 2). Stationary `Closed`, trajectory `Safe`, and `Adequate
service` remain distinct.

---

## S8 · The linear programmes, their inputs, and the reading rule

All three are ordinary LPs, solved by any simplex or interior-point routine. The exhibit code solves the third
with `scipy.optimize.linprog(method="highs")`.

**1. Closure capacity (Definition 21).** At a named frozen state $x_0$ and boundary vector
$b_0=B_{\mathcal T}u_{\partial,0}$ (with $d_x=0$ for an undisturbed stationary test), use variables
$(v,\mu)$:
```
maximise   μ
subject to S_T v + b0 = 0
           v ≥ 0
           A_cap(x0) v ≤ h_cap(x0)       (all individual and joint capacity rows)
           P v ≥ μ g                     (demanded service/use pattern)
```
Here `S_T` in the code block denotes the typed operator $S_{\mathcal T}$. The optimum is
$\Lambda^*(x_0;b_0,g)$. It is a stationary capacity statement at that state and boundary
schedule, not a trajectory-safety or permanent-drawdown conclusion. Donor rows must vanish at an
empty donor, and capacities consumed jointly must appear once as joint rows. Farkas/Gale
infeasibility witnesses may identify the binding rows, but a generic cut slogan is not a
substitute for the declared programme.

**2. Critical-margin multiplier (Theorem 24).** Over variables `λ`:
```
find   λ
subject to λᵀ G S_T + cᵀ ≤ 0
           0 ≤ λ ≤ λ̄        (optional declared search bound; otherwise state how β is controlled)
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
and report the concealed deficit as `[δ*_j(z)]_+ = [−b_j^min]_+`. If the feasible set at the
published $z$ is empty, Proposition 30 gives no concealed-deficit value; that infeasibility is a
finding about the disclosure constraints, not by itself a finding about the underlying system. Inputs: published
aggregate `z`, weights `w`, and the component bounds `ℓ, u` — the last are what a publisher must
supply, and their absence is why no numeric value for a public indicator is printed in the article.

Exhibit (two components, `w = (0.5, 0.5)`, declared bounds `ℓ = (−4, −4)`, `u = (10, 10)`), from `v51/code/certification_lp_v51.py`:

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

**2. Reserve-life crossover (Proposition 28), on the pinned record.** Reserves
73,000,000 kt and estimated 2025 production 250,000 kt/yr (USGS *Mineral Commodity Summaries*
2026), so `τ = 292` yr. At `g = 0.03 yr⁻¹`, $x=g\tau=8.76$ and the exact crossover is
$\eta_*=1-x/(e^x-1)=0.998625475$:

| `η` | `T` (yr) | relation to `τ` |
|---|---|---|
| 0 | 75.94 | below |
| 0.99 | 225.88 | below |
| 0.995 | 248.97 | below |
| 0.998625475 | 292.00 | equal |
| 0.999 | 302.60 | above |
| 1 | no finite exhaustion in this scenario | — |

The first-order approximation $\eta_*\approx x/2-x^2/12$ is not usable at $x=8.76$. The static
ratio is optimistic for every $\eta<\eta_*$ in this scenario and conservative in the narrow
interval $\eta_*<\eta<1$; no model-free direction is claimed.

**3. Persistence index on the declared trend class (Proposition 32).** Proposition 32 is now
proved by the backward-maximum representation and OLS consistency, giving
$I_n\Rightarrow M_\infty/\beta$. The Gaussian simulation (400 replicates, `β = σ = 1`, seed 7) is
an exhibit for that limit, not the proof:

| `n` | mean | median | 90th pct | deterministic observed drop $\beta n$ |
|---|---|---|---|---|
| 10² | 0.211 | 0 | 0.812 | 100 |
| 10³ | 0.247 | 0 | 0.835 | 1,000 |
| 10⁴ | 0.206 | 0 | 0.953 | 10,000 |
| 10⁵ | 0.246 | 0 | 0.999 | 100,000 |

The index remains a finite trend-detection quantity expressed in years while the deterministic
observed-series drop grows by three orders of magnitude over the displayed record lengths. No
physical stock drop is inferred from the anomaly series.

**4. Aggregate non-transport (Proposition 31)**. `k = 1`, barrier `x_i ≥ 1`: starts `(2, 98)` and `(50, 50)` give the identical
aggregate `Z(t) = 100e^{−t}` with first component exits at 0.6931 yr and 3.9120 yr respectively.

**5. Certificate vectors of the three classified indicators:**

| Indicator | Typed | Balanced | Conserved | Positive | Admissible | Safe | Adequate | Closed |
|---|---|---|---|---|---|---|---|---|
| G3P anomaly-persistence index (§6.5.1) | not est. | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| phosphate reserve-life ratio (§6.5.3) | not est. | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| fisheries removals-only pressure time (§6.5.4) | not est. | n/a | n/a | n/a | n/a | not est. | n/a | n/a |

Each row is the main text's own classification written in the vector's alphabet: a statistical index or an
arithmetic ratio is not a ledger trajectory, so the fact that its defining arithmetic is well formed does
not establish `Balanced`. It declares no compartments, barriers, or production relation. The fisheries row
records `Safe` as not established because a pressure scale states a rate against no declared barrier.

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

The v51 package is `paper3/latest-2026-09-19/v51/`. Its scripts are
`code/curvature_and_crossover_v51.py` (Propositions 26–28 and the MCS 2026 table),
`code/fisheries_cohorts_v51.py` (the three included cohort CSV summaries),
`code/persistence_index_simulation_v51.py` (the Gaussian exhibit for Proposition 32), and
`code/certification_lp_v51.py` (the premium/concealed-deficit exhibit and Proposition 31
witness). Run instructions, dependency versions, captured output, data provenance, and SHA-256
checksums are in the package `README.md`, `outputs/`, and `CHECKSUMS.sha256` described there.

The exclusion boundary is part of the reproduction claim. No v51 script re-derives the G3P basin
extraction from product masks, rebuilds a fisheries cohort from a RAM Legacy source release, or
recomputes National Footprint and Biocapacity Accounts edition tables. Those remain explicitly
labelled source/provenance records (S5, S5.4, and S17), not silently reproduced computations.

## S9.4 · Statement inventory, extended form

All numbered main-text statements in appearance order. A complete citation is the ordered pair
(kind, number); repeated bare numbers under different kinds are distinct labels. Non-example 1
is an unnumbered-kind exhibit in §6.5.2 and is included after Proposition 28 in appearance order.

| Label | Main-text section |
|---|---|
| Definition 21 (State-conditioned closure set and closure capacity) | 2.1 |
| Definition 22 (Return kernel, use-timescale deficit, late return, and ultimate loss) | 2.1 |
| Theorem 1 (Support-saturated logistic stock limit) | 2.6 |
| Remark 2 (Registered-family support-saturated identity) | 2.6 |
| Proposition 1 (Conservation projection of a balanced trajectory) | 3.1 |
| Proposition 2 (Non-implications among the defined layers) | 3.1 |
| Lemma 3 (Flux identifiability under a typed balance law) | 3.3 |
| Proposition 4 (Conservation-law projection) | 3.4 |
| Definition 23 (Bounded residual) | 3.4 |
| Theorem 5 (Flux-bounding envelopes) | 3.5 |
| Proposition 6 (Finite exhaustion under uniform negative drift) | 3.6 |
| Theorem 24 (Critical-margin budget) | 3.6 |
| Definition 34 (Composition of typed ledgers) | 3.7 |
| Definition 35 (Interface price for a disjoint coupled composition) | 3.7 |
| Proposition 36 (Conservation pullbacks compose; closure capacities need not) | 3.7 |
| Proposition 37 (Interface correction to a summed certificate budget) | 3.7 |
| Definition 40 (Compensation as a decidable predicate) | 3.7 |
| Remark 34 (What the multiplier search can and cannot prove) | 3.7 |
| Definition 41 (Control margin) | 3.7 |
| Definition 42 (Affinity, the fourth admissibility predicate) | 3.7 |
| Proposition 40 (An empty corridor comes with a named conflict) | 3.7 |
| Definition 43 (Circulation time) | 3.7 |
| Definition 44 (Governability ratio) | 3.7 |
| Lemma 4 (A moving baseline contributes a covariance term) | 3.7 |
| Definition 45 (Latest safe intervention time) | 3.7 |
| Proposition 41 (Scalar frozen-drawdown deadline) | 3.7 |
| Definition 46 (Supportable-output envelope) | 3.7 |
| Remark 35 (What a non-displacement gate can say on this apparatus) | 3.7 |
| Definition 47 (Type structure) | 3.8 |
| Proposition 42 (Conservation decomposes by type class; no typed scalar conservation readout crosses classes) | 3.8 |
| Remark 36 (What the type structure yields, and what it does not) | 3.8 |
| Theorem 7 (Natural-block mass identity) | 4.1 |
| Theorem 8 (Stoichiometric conservation) | 4.2 |
| Theorem 9 (Six-compartment conservation) | 4.3 |
| Theorem 10 (Orthant invariance of the closed ledger) | 4.4 |
| Theorem 11 (Forward invariance of the six-compartment cone) | 4.4 |
| Theorem 12 (No interior rest at positive effort) | 4.5 |
| Theorem 13 (Vanishing-extraction rest set) | 4.6 |
| Theorem 14 (Integrable extraction) | 4.7 |
| Conditional Theorem 15 (Hybrid moiety balance) | 4.8 |
| Definition 1 (Feasible balance domain) | 5.2 |
| Definition 2 (Directional regenerative-support fraction and gap) | 5.3 |
| Remark 16 (Exact specialization deficit identity) | 5.4 |
| Proposition 25 (Accumulated support drawdown certified by delivered service) | 5.4 |
| Definition 3 (Gross turnover intensity and support coverage) | 6.1 |
| Definition 4 (Local net-depletion ratio) | 6.1 |
| Definition 5 (Scenario-conditioned hitting time) | 6.1 |
| Proposition 17 (Local threshold-horizon bracket) | 6.2 |
| Proposition 26 (Sign of the frozen-rate error) | 6.2 |
| Proposition 27 (Curvature correction) | 6.2 |
| Proposition 28 (Exact reserve-life crossover) | 6.2 |
| Non-example 1 (equal-weight inverse-horizon aggregate) | 6.5.2 |
| Proposition 32 (Boundedness, and limiting law, of the persistence index on the declared trend class) | 6.5.4 |
| Definition 38 (Identifiability set of an event time) | 6.6 |
| Proposition 39 (The set is a polytope image, and it is usually an interval) | 6.6 |
| Definition 6 (Observed-drift Brownian surrogate) | 7.2 |
| Proposition 18 (Inverse-Gaussian first passage — a standard fact, stated for notation) | 7.3 |
| Corollary 19 (Zero-noise limit and median) | 7.3 |
| Proposition 20 (Geometric-Brownian correction — a standard fact, stated for notation) | 7.5 |
| Proposition 43 (Closure of the declared ecological–institutional subsystem) | 9 |
| Proposition 29 (The certifying aggregator is unique) | 10.1 |
| Proposition 30 (Worst concealed deficit at a published aggregate) | 10.1 |
| Proposition 31 (Aggregates do not transport event times) | 10.1 |
| Remark 33 (One-signed bias of an aggregate overshoot date) | 10.2 |
| Remark 37 (Two component ratios are identities at a world aggregate) | 10.2 |

Interface Hypothesis I (§9) and the §9 scoped non-reduction theorem are named results inside
their section rather than additions to the inherited numbered sequence; Proposition 43 is
conditional on that hypothesis. The certification-state paragraph in §3.1 is likewise named but
unnumbered.

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
| $\kappa_m(\tau_{\mathrm{use}}), d_m^{\mathrm{late}}, \ell_m$ | Definition 22, Remark 35 | are the return kernel, returnable fraction, and pipeline history identified? | **not established** for the public indicators; declared objects in the theory | process-level return observations that separate delayed return from ultimate non-return |
| $\tau_{\mathrm{use}}$ (timescale of the deficit readout) | Def. 22's $\kappa_m$ | none — declared by the analysis | **not applicable** | — |
| $\ell_m g_m$ and pipeline history | Definitions 22, 45–46 | is permanent combined-stock draw separated from available-stock timing? | **not established** for the public indicators | return-kernel/history data; $\delta_m^{\mathrm{use}}$ alone cannot settle it |
| $\mathcal A_{\min}$, $\mathcal A_{\max}$ (barriers) | `Safe`, Def. 45, Prop. 41 feasibility | none — declared | **not applicable** | — |
| $d_0,\ \rho,\ \tau$ (drawdown level, ramp rate, delay) | Prop. 41's $m_{\mathrm{needed}}$, $t_{\mathrm{last}}$ | published values for any named ledger? | **not established** — the article's two instances are illustrative | an empirical declaration by whoever runs the certificate |
| $H^{\mathrm{loc}}$ (frozen-rate ratio) | Prop. 26, Def. 46's corner | computable from the declared pair? | **established as a ratio**; its direction against $T$ is established **only under** Prop. 26's monotonicity hypothesis | the monotonicity (or a declared $\varphi$) |
| $q_i$ (normalisation choice) | Definition 23, Proposition 36 | is the same covector class-constant and exchange-compatible after composition? | **not applicable as an estimate**; compatibility is checkable | Proposition 36's pullback conditions |
| $\varepsilon_\ell$ (disturbance budget) | `Conserved` | declared, then checked against the record? | **established relative to the declaration** | the declared class |
| G3P $\widehat{\dot a}$, $a_{\mathrm{hist,min}}$ | $L_{\mathrm{hist}}^{\mathrm{anom}}$ (§6.5.1) | reproducible from the product's basin masks? | **not established numerically** — the rows are quarantined for reuse for exactly this reason, and the product documents a faulty June-2005 snow entry that the window spans | re-derivation from the masks, with the June-2005 choice declared |
| G3P anomaly reference period | the same index | is the baseline published? | **established** — April 2002 to December 2020, per the product documentation; coverage ends September 2023 | — |
| $\mathrm{SSB}_{\mathrm{now}},\ F_{\mathrm{now}},\ B_{\lim}$ | $\Theta_F$, the ADH proxy | defined by the protocol on the archived cohort | **established on the cohort**; **not established** as a statement about the population of assessed stocks | nothing further: the extract is pinned to release v4.66 (Zenodo 14043031, 6 Nov 2024) and its vintage is verified from its own contents in S5.1 (four of six published $F$ values reproduce that release exactly), with the cohort recomputed in S5.3 to $10^{-9}$ |
| reserves, production | $T_{\mathrm{reserve}}$ (§6.5.3) | published for a stated vintage? | **established for the vintage named**, not established forward | the vintage statement, which the row carries |
| $\tau_{\min},\ \tau_{\mathrm{agg}}$ (premium, Remark 33) | the overshoot premium | computable from the published accounts? | **established as arithmetic** on the published ratio; the zero-carbon-biocapacity row is **not applicable** as a modelling choice — it is the accounts' documented convention, cited in Remark 33 | whether the author also reports the carbon-demand-excluded variant |

No cell in these tables is left for the author to fill. Every row was read off the main text, the deposited
repository in the v51 package, or a published source. The cell that would otherwise have required the analysis repository
is closed by the release identifier together with S5.1’s row-level vintage check, a stronger claim than a pull
date.

## S11 · Material and energy value: what is checkable, and what is not

The position is recorded here so that it can be cited, tested, and kept out of the main text's claim list.
Each row states the position's clause, the object in the main text that carries it, and its status.

| clause of the position | object in the article | status | what is *not* claimed |
|---|---|---|---|
| value may be assessed only within a type; no substitution across types | Definition 47's typed readouts and Proposition 42's class decomposition | **established for typed scalar conservation readouts** | no theorem about worth and no prohibition of an extra untyped numerical index; such an index is not a typed conservation law |
| no cross-type compensation in an aggregate | Proposition 29 (the calibrated monotone certifier is `= min`, and continuity with certification and strict monotonicity are incompatible) | **established** | no claim that a compensating index is useless; only that it is not a certificate |
| an effect at an interface must be represented on the composed object | Definitions 34–35 and Propositions 36–37 | **established under the stated disjoint/quotient scopes** | pair prices do not descend automatically to a shared-stock quotient |
| pure reporting relabelling does not change the ambient operator | Remark 36's reporting-boundary clause | **established for names alone**; changing declarations can change admissible columns and typed readouts | not invariance to redrawing *inside* a class — Proposition 36 governs that, and it can fail |
| reserve reclassification/growth changes a reserve-life scenario | Proposition 28's elasticity $\eta$ | **established as an exact scenario crossover** | no forecast or estimate of $\eta$; Definition 22 is a separate return-kernel object |
| a certificate should carry an "MDV" field | no such field exists in the article | **not established here**; supplementary/project-side only | the article's `Cert` vector has eight entries and none of them is a value-type score |
| one umbrella invariance theorem covering all of the above | declined in favour of the per-case results (Propositions 28, 29, 36, 40, 42 and Definition 47) | — | the umbrella's hypotheses would have to include a primitive the article does not define |

## S5.4 · G3P basin-row extraction provenance (the record behind main-text Section 6.5.2)

*The main text keeps the classification sentence and this record's pointer. What follows is the demoted
provenance, reproduced without change. Deictic words are the main text's: "the classification status assigned
below" named the table that still follows it there.*

The basin rows are reported extractions from the G3P v1.12 basin series, used here only to exhibit the index
construction of Section 6.5.1. The window-minimum column is implied by the displayed trend and horizon through
the index formula of Section 6.5.1, arithmetic. It is not product-endorsed, and every basin row must be re-
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

## S16 · S7 discharge pointers in v51 labels

S7 above is already written in the v51 labels. The load-bearing readings are: `Balanced` is the
trajectory identity with total $b=B_{\mathcal T}u_\partial+d_x$, while Lemma 3 gives only the
compatible flux fibre; `Conserved` is Propositions 1 and 4 for a balanced trajectory, not a
consequence of left-nullity alone; `Admissible` is Definitions 21, 34, 42, and 47 together;
`Safe` and `Closed` are not synonyms; and Proposition 25 concerns accumulated support drawdown,
with permanent combined-stock liquidation requiring the pipeline distinction of Definition 22.

## S15 · `Typed` proof-obligation row, corrected

| predicate | statement | main-text locus | witness | fails when |
|---|---|---|---|---|
| `Typed` | every compartment carries a declared type and unit; every column is either a same-type/unit zero-sum transfer-routing column (including a unit-sum split) or a positive multiple of a declared finitely supported conversion template | Definition 47, Proposition 42 | the declaration $(\mathsf{Ty},\mathrm{ty},\mathrm{un},\mathsf{Cv})$ itself | a transfer mixes type/unit, a split does not sum to one, or a conversion is used without its template |

`Typed` is decidable from a complete declaration. Proposition 42 then gives class-supported
typed scalar conservation readouts and tuple-valued multi-class readouts. It does not forbid
declaring an additional untyped numerical sum; it forbids calling that sum a typed conservation
law.

## S17 · The overshoot-date recomputation, and the significance of a difference of a few days

*This section records the recomputation of the aggregate overshoot date with and without carbon demand, on two
editions of the National Footprint and Biocapacity Accounts, with the data provenance, the arithmetic and the
reproduction command in full. The main text carries its conclusions in Section 10.2 and Remark 37.*

**Data.** Two editions of the National Footprint and Biocapacity Accounts, chosen because they are the newest
ones obtainable without an account: the 2018 edition (series 1961–2014, the release Lin et al. (2018)
documents) and the 2017 edition (1961–2013), both deposited by the publisher under CC BY-SA 4.0. The tables
are held with the analysis record so that the run can be repeated without a network; they are not
redistributed with the deposit, whose copy of the record carries `source/MANIFEST.md` with the two retrieval commands and the
hashes that settle what was read. The current edition is free but registration-gated, so the 2022 row quoted in the main
text's Remark 33 is not reproducible from an open download, and the limitation is recorded here. The checksums
of the two tables as read: 60968f7c9959537f8e67f915aca4259662b5cd42c3a0ec02d094677b4c280ef6
NFA_2018_edition_kaggle.csv 11857080 bytes · 0dd766d975cd5e85f2a2d39cff1f914b92c514186ce507cb1f721a63be57b6a5
NFA_2017_edition_kaggle.zip.csv 13195855 bytes

**Reproduction boundary.** This is an external provenance record. The source tables are not redistributed in the v51 package and no v51 script recomputes this section; the hashes and retrieval record below are the audit trail retained from the earlier analysis.

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

1. **The premium's downward trend survives the exclusion.** With carbon demand removed, the restricted premium
on this release runs 524 d (1961), 323 d (1980), 230 d (2000), 179 d (2014); the decade means are 1960s 464 d,
1970s 358 d, 1980s 288 d, 1990s 253 d, 2000s 216 d, 2010s 191 d, with 45 of 53 year-on-year changes negative.
The article's series. 547, 346, 251, 173 d, read off a later edition. Carries the same sign and shape and sits
4–8% above this release on the shared years, which is a further instance of the point the main text makes about
vintages rather than a contradiction of it. 2. **The two conventions part by about a year, and by a known factor.** Over 2005–2014 the restricted date exceeds the published-convention date by 340.8 d on average
(327.4–347.7 d), a ratio of 2.41 to 2.60, and that ratio equals $1/(1-s_{\mathrm{carbon}})$ to within 4.4e-16, with $s_{\mathrm{carbon}}$ between 58.6%
and 61.6%. Excluding carbon demand multiplies the reported date by a factor of two and a half rather than
refining it. 3. **The restricted date is the fragile one.** From the 2017 to the 2018 edition the aggregate
date moves by 1.1 d on average and 1.9 d at most on a closed year, while the restricted date moves by 6.3 d on
average and 9.1 d at most, a factor of 5.8. The reason is structural: the excluded denominator is the smaller
quantity, so an absolute revision in the non-carbon components is divided by less. A headline-versus-
recomputed difference of a few days is inside that noise for the restricted date and outside it for the
aggregate date, so whether a difference of a few days is material depends on which date it concerns.
4. **Aggregation level accounts for as much as vintage does.** Reading the publisher's `World` row rather than
summing the national rows moves the aggregate date by up to 9.2 d over the last decade of the release; and
summing them *including* the `World` row — the natural first attempt at a world total in a table that carries both,
and an error this section documents — doubles both sides of every ratio, which leaves the number of Earths
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
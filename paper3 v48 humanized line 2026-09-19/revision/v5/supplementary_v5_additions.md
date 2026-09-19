# Supplementary material — v5 additions

**Purpose.** The article's Declarations paragraph promises a supplementary file. Its author's own
file (`paper3_supplementary_v8.md`, named at that paragraph's head in the source of record) carries
the ten-state admissibility template and its audited negative witnesses, the registered
identification ladders, the split-assignment mechanism table, the statement inventory, and the
fisheries cohort record with the archived-pull verification. Those five items are **not reproduced
here**, because they exist in the author's file and not in this workspace; nothing in this
document should be read as replacing them. What follows are the sections that the v5 revision of
the article newly depends on, written to be appended to that file in the order below.

| New section | Supplies | Required by |
|---|---|---|
| S-A | proof obligations of the certification state | §3.1 |
| S-B | the three linear programmes, their inputs, and the reading rule | Definitions 21–22, Theorem 24, Proposition 30 |
| S-C | the worked ledger exhibit | §6.2, §7.1, §8.1, §8.4 |
| S-D | the promotion-rule table | §8.1–8.3 |
| S-E | reproduction: scripts, seed, library versions | §8.1 (Proposition 32), all of S-C |
| S-F | statement inventory at v5 labels 1–33 | §3.1 numbering convention |

---

## S-A · Proof obligations of the certification state (§3.1)

Each entry of `Cert` with the statement that discharges it, the object it needs, and what its
absence means. "Not established" is a status, never a refutation; "not applicable" is a statement
about the object, never about the system it describes.

| Entry | What must be shown | Discharged by | Needs as input | Meaning when not established |
|---|---|---|---|---|
| `Typed` | every compartment carries a material identity, a boundary and a unit, and no column mixes types | §2.1, §2.2 incidence discipline | the compartment table | the ledger cannot be balanced by addition; arithmetic on it is not meaningful |
| `Balanced` | the accounting identity `S_T v + B_T u_∂ = ḃ` holds as written | §2.2, §3.4 flux-reconstruction identity | flux table and incidence matrix | an entry is missing, duplicated, or routed wrongly |
| `Conserved` | `ℓᵀ C d_x` carries a declared budget and the invariants follow | Definition 23, Proposition 1 | left-null vectors of `S_T`, disturbance budget `ε_ℓ` | conservation is asserted, not certified; the statistical discrepancy is unbounded |
| `Positive` | the nonnegative orthant is forward-invariant | Theorems 10–11 (donor limitation, Nagumo condition) | constitutive laws at the boundary of the orthant | a compartment may go negative, so the ledger admits unphysical states |
| `Admissible` | every term is realizable by the declared chemistry/physics, incl. thermodynamic sign constraints | §3.3 Proposition 2 and its thermodynamic clause | reaction feasibility, energy and entropy balances | a mass-balanced ledger may still be physically impossible |
| `Safe` | declared lower and upper barriers hold over the horizon for every scenario | §3.6 envelope theorem, §6.3–6.4, Theorem 24 | barriers, horizon, declared disturbance class | margin may be violated; the aggregate is at best an alarm |
| `Adequate service` | the readout meets the declared demand relation | §5.1–5.4, Proposition 25 | service definition, production relation | service is delivered by unpriced drawdown of support |
| `Closed` | demand lies in the closure cone, and the deficit is declared at a stated timescale | Definitions 21–22 | stationary-flux LP, process graph, `τ_use` | the shortfall is being carried by the support pool or the sink, in a quantity not stated |

The implications that hold among the entries are exactly those proved in the article:
`Conserved ⇒ Balanced` for the conserved quantities (Proposition 1), the thermodynamic clause of
Section 3.3, and nothing else. `Safe` over a barrier set contained in the nonnegative orthant
implies `Positive` over that horizon — that instance is an artefact of the declared barrier set and
is not an implication between the predicates.

---

## S-B · The linear programmes, their inputs, and the reading rule

All three are ordinary LPs, solved by any simplex or interior-point routine; the exhibit code solves
the third with `scipy.optimize.linprog(method="highs")`.

**1. Closure capacity (Definition 21).** Over variables `(v, λ)`:
```
maximise   λ
subject to S_T v + B_T u_∂ = 0
           0 ≤ v ≤ v̄
           λ D ≤ P v
```
Inputs: incidence operator, declared capacities `v̄`, the boundary-transfer schedule, the demanded
use vector `D`. Feasibility for `λ ≥ 1` is the regime in which the cycle closes at the demanded
rate. The dual is the cut condition on return capacity (Gale, 1957; Ahuja et al., 1993): for every
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

Exhibit (two components, `w = (0.5, 0.5)`, declared bounds `ℓ = (−4, −4)`, `u = (10, 10)`), from
`code/certification_lp.py`:

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

## S-C · Worked ledger exhibit

Everything below is arithmetic on the article's own declared relations and pinned figures, and on
simulated series inside a declared class. No new data were obtained, and no row of any public table
is re-computed here.

**1. Curvature correction (Proposition 27), family `φ(u) = c u^p`, `c = 1`, `u₀ = 1`:**

| `p = κ` | `H_loc` | exact `T` | `T / H_loc` |
|---|---|---|---|
| 0 | 1.0000 | 1.0000 | 1.0000 |
| 0.5 | 1.0000 | 2.0000 | 2.0000 |
| 0.75 | 1.0000 | 4.0000 | 4.0000 |
| 1 | 1.0000 | ∞ | ∞ |
| 1.5 | 1.0000 | ∞ (diverges at the barrier) | — |
| −0.5 | 1.0000 | 0.6667 | 0.6667 |

`T = H_loc/(1 − κ)` reproduces the closed form exactly for every `κ < 1`; at and above `κ = 1` the
integral diverges at the barrier, so the frozen-rate ratio understates without bound.

**2. Reserve-life crossover (Proposition 28), on the pinned record** — reserves 74,000,000 kt,
production 240,000 kt/yr (USGS *Mineral Commodity Summaries* 2026, as tabulated in §8.2),
`τ = 308.33` yr, `g = 0.03 yr⁻¹`:

| `η` | `T` (yr) | `T/τ` |
|---|---|---|
| 0 | 77.58 | 0.252 |
| 0.25 | 86.34 | 0.280 |
| 0.50 | 99.01 | 0.321 |
| 0.75 | 121.25 | 0.393 |
| 0.90 | 151.27 | 0.491 |
| 0.99 | 227.70 | 0.739 |

The first-order condition for the ratio to be conservative is `η ≥ ½gτ = 4.625`, outside the
admissible interval `0 ≤ η ≤ 1`: the reserve-life ratio is optimistic in a direction fixed by the
model class, independent of the data.

**3. Persistence index on the declared trend class (Proposition 32)** — 400 replicates,
`β = σ = 1`, seed 7, `index = (a_n − min_k a_k)/(−fitted slope)`:

| `n` | mean | median | 90th pct | implied stock drop |
|---|---|---|---|---|
| 10² | 0.211 | 0 | 0.812 | 98.9 |
| 10³ | 0.247 | 0 | 0.835 | 998.9 |
| 10⁴ | 0.206 | 0 | 0.953 | 9 999.1 |
| 10⁵ | 0.246 | 0 | 0.999 | 99 999.0 |

Flat in record length while the stock falls by five orders of magnitude: the statistic is a
trend-detection quantity expressed in years.

**4. Aggregate non-transport (Proposition 31)** — `k = 1`, barrier `x_i ≥ 1`: starts `(2, 98)` and
`(50, 50)` give the identical aggregate `Z(t) = 100e^{−t}` with first component exits at 0.6931 yr
and 3.9120 yr respectively.

**5. Certificate vectors of the three classified indicators:**

| Indicator | Typed | Balanced | Conserved | Positive | Admissible | Safe | Adequate | Closed |
|---|---|---|---|---|---|---|---|---|
| G3P anomaly-persistence index (§8.1) | not est. | established | n/a | n/a | n/a | n/a | n/a | n/a |
| phosphate reserve-life ratio (§8.2) | not est. | established | n/a | n/a | n/a | n/a | n/a | n/a |
| fisheries removals-only pressure time (§8.3) | not est. | established | n/a | n/a | n/a | not est. | n/a | n/a |

Each row is the article's own classification written in the vector's alphabet: a statistical index or
an arithmetic ratio declares no compartments, no barriers and no production relation, so six of the
eight entries are not applicable rather than failed; the fisheries row records `Safe` as not
established because a pressure scale states a rate against no declared barrier.

---

## S-D · Promotion-rule table

When a published ratio may be read as an event time. Every condition listed is stated somewhere in
§8.1–8.3 of the article; the table collects them so that the promotion test is checkable in one
place, and it adds no condition.

| Published object | To be read as an event time only if | Article's own note |
|---|---|---|
| reserve-life ratio `R/P` | `R` is a fixed physical inventory, `Ṙ = −P`, `P` constant, and no discovery, price response or reclassification occurs | §8.2: the reserve classification is economic; the premises are carried, not discharged |
| anomaly index `(a_n − min a)/(−trend)` | an absolute stock-to-barrier distance is identified, i.e. geometry and storage coefficient supply an anchor, and the trend persists | §8.1: not identifiable from an anomaly series; adding a constant to the series and the reference leaves every observation unchanged |
| removals-only pressure time `log(B/B_min)/F` | `Ḃ = −FB̄` with `F` constant, no growth, no recruitment, no catch misreporting | §8.3: exact hitting time of the declared removals-only law, nothing more |
| cohort median or mean of any of the above | the cohort is a sample of the population the claim is about | §8.4: a selected class, 43 small pelagics, not a random sample |
| a scenario-conditioned hitting time | the scenario, drift, barrier and noise class are declared and the surrogate is not read as the ledger | §9.6, §9.7 |

The rule has a one-line form: **a ratio becomes an event time only when its denominator is a
declared constant law of the stock itself and its numerator is a physical inventory.** Absent that,
it remains an index, a ratio, or a pressure scale, which is the status §8 assigns.

---

## S-E · Reproduction

`code/persistence_index_simulation.py` (Proposition 32), `code/curvature_and_crossover.py`
(Propositions 26–28), `code/certification_lp.py` (premium, `δ*_j`, Proposition 31, and the vectors
of S-C.5). Fixed seed 7; `numpy` and `scipy` versions recorded in `code/MANIFEST.md`; complete
stdout in `code/outputs.txt`. The scripts read no data beyond the figures quoted in the article, so
every printed value is reproducible from this file alone.

## S-F · Statement inventory at v5

Main counter 1–33, with the layering counter (Propositions 1–2) separate, per §3.1. New in v5:

| Label | Section |
|---|---|
| Definition 21 (Closure cone) | 1.3 |
| Definition 22 (Closure deficit at the use timescale) | 1.3 |
| Definition 23 (Bounded residual) | 3.5 |
| Theorem 24 (Critical-margin budget) | 4.8 |
| Proposition 25 (Accumulated liquidation certified by delivered service) | 5.4 |
| Proposition 26 (Sign of the frozen-rate error) | 6.2 |
| Proposition 27 (Curvature correction) | 6.2 |
| Proposition 28 (Reserve-life crossover) | 6.2 |
| Proposition 29 (The certifying aggregator is unique) | 7.1 |
| Proposition 30 (Worst concealed deficit) | 7.1 |
| Proposition 31 (Aggregates do not transport event times) | 7.2 |
| Proposition 32 (Boundedness of the persistence index on the declared trend class) | 8.1 |
| Remark 33 (One-signed bias of an aggregate overshoot date) | 8.4 |

Unnumbered statements added in v5: *Certification state* (§3.1), *Antecedents* (§1.5), the
refute/alarm clause (§7.2), the joint-minimal reporting note (§6.3), the disturbance-budget note
(§2.2), the review-interval note (§10.1).

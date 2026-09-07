# Paper3 overlap check: ECOMOD v33 vs. the actual paper3 (Zenodo 22554177)

**Source checked:** `Typed Flux Ledgers and Depletion Arithmetic: Conservation, Componentwise Diagnostics, and the
Semantics of Depletion Horizons` (doi/record 22554177, v1). Downloaded `paper3_material_ledgers_v31.pdf`
(40 pp) and `paper3_supplementary_v7.md`, searched the full extracted text.

**Question addressed:** Is ECOMOD v33 still too similar to paper3, and does it merit merging or splitting?
This resolves the one open flag I could not settle without the paper — whether paper3 already owns the
gha-/biocapacity observability-ladder result that sits in ECOMOD's §Discussion Identifiability.

---

## 1. What paper3 actually is

A **general closed material-flow ledger / depletion-arithmetic theory**: typed compartments and primitive fluxes,
conservation from the flux-network incidence structure, positivity from donor limitation, services as readouts.
Its contributions are the **certification layers** (flux-reconstruction identity, conservation reduction,
flux-bounding envelope theorem), a **depletion-time taxonomy** (gross turnover intensity, frozen-rate ratio,
scenario-conditioned hitting time), **first-passage semantics** on declared stochastic surrogates, classification
of **three public-data objects** (G3P anomaly index; phosphate reserve-life ratio; fisheries removals-only
pressure scale), and the no-nonnegative-weighting aggregation obstruction (§10.1).

Its domain is **material flow accounting** — biomass, money, biodiversity, phosphate, groundwater, fisheries.
This is *not* the footprint/biocapacity domain.

## 2. Direct text evidence (searched the full PDF, 136,657 chars)

| Term | paper3 hits | Notes |
|---|---|---|
| `identifiability` | **0** | paper3 has no identifiability/observability ladder |
| `observab` | **0** | no observability-analysis content |
| `composition illusion` | **0** | term is ECOMOD's alone |
| `two-book` | **0** | ECOMOD's two-book structure is absent |
| `biocapacity` | **1** | only in a *reference* (Wackernagel & Beyers 2019 book title) |
| `global hectare` / `gha` | **0 / 0** | paper3 never uses global hectares |
| `National Footprint` | **1** | also only in a reference |
| `ecosystem footprint` | 3 | framing only |
| `conversion` | 8 | **all stoichiometric/chemical** ("conversion between types is an explicit stoichiometric coefficient") — *not* land-use conversion |
| `two-pool` | 10 | **all groundwater**, and explicitly "registered open gap", "no such model is claimed as established"; the admitted applied object is the **one-pool affine approximation** |
| `Hopf` | 3 | **ceded** — "the companion's global periodic results ... do not transfer to the closed primitive ledger" |
| `productivity illusion` | 1 | conceptual framing in §1.1, separated into arithmetic vs. yield-inflation senses |

## 3. Explicit self-declared boundaries (paper3 §1.2–§8.3+, "Interface contract")

> "The partition between this article and the companion delay-dynamics analysis ... is fixed by an interface
> contract. This article owns the closed material accounting: the primitive ledger equations and full routing,
> the conservation and positivity theorems of Section 4, the componentwise [diagnostics] ..."

> "The exact shared object with delay-based institutional models is the single-resource deficit identity
> `qEN − R = −ṅ`. The boundary is the **non-reduction theorem**: no exact dynamic reduction from the closed
> ledger to the delay-dynamic working system exists."

> "The companion's global periodic results are properties of its reduced systems and do not transfer to the
> closed primitive ledger; in particular, **Hopf or periodic orbits** of the frozen-donor working system are
> not properties of (2)."

So paper3 **owns statics/accounting**, **explicitly does NOT build the two-pool dynamical model** (registers the
groundwater two-pool as an open gap), **cedes all delay/Hopf/periodic dynamics to the companion** (paper4/v18),
and **has no identifiability/observability or biocapacity content**.

## 4. Verdict

### Q2 — Is ECOMOD still too similar to paper3? **No.**
The two occupy different objects, domains, and machinery:

| | paper3 | ECOMOD v33 |
|---|---|---|
| object | closed material-flow ledger (typed moieties) | dynamical two-book biocapacity system |
| domain | phosphate, groundwater, fisheries, biomass | global-hectare biocapacity / NFA |
| machinery | incidence-structure conservation, depletion arithmetic, first-passage | DDE with ecological delays, no-fold/no-CSD, phase-dependent recovery gate-sign |
| dynamics | **none** (explicitly one-pool, two-pool = open gap) | central (delay-amplified; S5.4/S5.5) |
| identifiability | **none** | central ("value-weighting is inside the unit" → not identifiable from aggregate) |

paper3 has **no** ecological-delay dynamics, **no** two-book composition, **no** gha identifiability result.
ECOMOD's three overlapping touchpoints are all **framing fragments already handled**:
- "productivity illusion" term — paper3 uses it; ECOMOD uses "**composition illusion**" (a *distinct* term,
  absent from paper3). Fine, but ECOMOD should cite paper3's framing where it invokes the concept.
- The no-nonnegative-weighting aggregation obstruction — **paper3 §10.1**, and ECOMOD already defers this to
  **paper1** (the aggregation-theorem paper). No conflict; it is cited, not re-claimed.
- The single-resource deficit identity `qEN − R = −ṅ` (paper3's shared object) — ECOMOD generalises this to the
  two-book deficit `S=[E−σ_fY_f−σ_cY_c]_+` and debt `dD/dt=[E−B]_+−ηD`. Same *structure*, extended to two books.

### Q3 — Merge with paper3, or split? **Neither.**
- **Do not merge.** A dynamical two-book footprint paper is not a material-flow-ledger paper. Merging buries
  ECOMOD's actual novelty (the no-fold/no-CSD negative result, the recovery gate-sign asymmetry, the two-book
  dynamics, the gha-identifiability claim) under ledger formalism, and breaks the program's
  v18/paper1–5/E1–E4/ECOMOD architecture that your own positioning doc already establishes.
- **Do not split ECOMOD.** Its §Discussion Identifiability is *not* redundant with paper3 (the conditional
  trigger I flagged earlier is **FALSE** — paper3 does not own the gha observability ladder). Trimming it would
  gut the abstract's honest real-series claim.

## 5. Refined recommendation (two sentences, no trimming)

Add to ECOMOD's §Discussion Identifiability (and/or the "Division of labour" bullet):

1. **Cross-reference paper3** for the general ledger/depletion-arithmetic and the aggregation obstruction, and
   note that ECOMOD's term is the *composition* illusion (not paper3's "productivity illusion" framing).
2. **Complementarity (strongest differentiation):** paper3 explicitly registers a two-pool dynamical model as
   an open gap and cedes delay/Hopf dynamics to the companion; ECOMOD is exactly the focused *two-book
   dynamical* realisation for the biocapacity case. Phrase it as "paper3 owns the closed ledger and cedes the
   dynamical two-pool realisation (its groundwater two-pool is a registered open gap); ECOMOD supplies that
   dynamical realisation for global-hectare biocapacity."

This turns a potential "this is paper3" objection into an explicit, defensible slot and strengthens ECOMOD's
novelty rather than diluting it.

*Verified against the actual paper3 text + supplementary; downloaded to `paper3/`. No ECOMOD file was modified in
this step.*

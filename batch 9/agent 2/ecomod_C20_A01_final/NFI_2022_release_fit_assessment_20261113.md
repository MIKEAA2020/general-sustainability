# NFI (NRCan) ground-plot release — fit assessment (rev. 2)

Date: 2026-11-13. Trigger: forwarded email from Michael Smith (NRCan, Canadian Forest Service).
**No data request filed. No manuscript or plan text changed.**

## 0. Naming — correction of rev. 1

Rev. 1 said "the manuscript is in EM submission" without naming it, which read as if a follow-up
manuscript were in EM. To be exact:

| Object | What it is | Status |
|---|---|---|
| **C20 A01 — "A rising biocapacity total can mask ecological-capital land drawdown: a two-land model"** | The manuscript in EM submission. Title verified in both `ecomod_C20_A01_main.tex` and `Manuscript_ECOMOD_C20_A01_portalsafe.tex` | **In EM submission**, 13-item upload list, portal-safe sources verified 38/31 pp |
| **Follow-up project** ("ecological assets behind improving accounts") | `ecomod_followup_plan/`, `ecomod_followup_paper_review/`, `ecomod_followup_external_review/` — implementation plan + contribution/prior-art reviews | **Not in submission. No manuscript exists yet.** Only a plan and reviews |

These are two different things. Rev. 1's timing argument was about the first; the NFI belongs to the
second. Corrected below.

## 1. What the release is

- New NFI **ground plot** data, released annually; this release extends **measurements through 2022**
  and includes the **first Yukon ground plots** (previously territory absent).
- Tree- and plot-level: DBH, height, species, condition/damage, stumps, woody debris, compiled volume
  and **aboveground biomass (kg oven-dry)** by component — stem wood, stem bark, branches, foliage —
  for large trees (DBH ≥ 9 cm), small trees (< 9 cm) and stumps.
- Biomass from **individual-tree and shrub biomass equations**; `BMEQ_*` equation IDs travel with the
  data, so every value traces to its equation.
- Genuine **physical, remeasured field observations** — repeated plots with survey dates and locations.
  Not a value-weighted account.
- Access: **Data Download Tool** (authorized users) or **Data Request Form**
  (`https://nfi.nfis.org/en/datarequestform`) with a project description and a coordinate-precision
  choice (**exact** vs. **±10 km rounded**). Licence: Open Government Licence – Canada.
  Standards: *NFI National Standards for Ground Plots*, compilation procedures v2.4; data dictionary
  for the 2018–2027 second remeasurement period, v6.0.

## 2. Fit to C20 A01 (the paper in EM): none

Verified in the deposited sources:

- "Canada"/"Canadian": **0 occurrences in the main text, 0 in the SI.**
- §3.7 is a **world-aggregate** NFA Edition 2026 decomposition (1961–2023; 2024–2025 excluded), plus a
  1961–2022 same-edition sensitivity, plus an OWID/FAOSTAT **world** cropland-area / cereal-yield proxy.
- No Canadian series exists anywhere in the paper, so there is nothing to update.
- NFI biomass cannot enter a world gha account decomposition: different boundary, different unit, one
  country, physical stock vs. value-weighted account. The paper is explicit that NFA forest biocapacity
  and measured biomass are not interchangeable and that `Y_c = Υ(q)A_c` is unidentified by either.

**So: NFI is not relevant to C20 A01.** Not a scope question — a category question.

## 3. Fit to the follow-up: direct, and already on the requirements list

This is the part rev. 1 missed. The follow-up plan's purpose is to *"test the observable implications
of composition masking using independent physical-asset estimates"*
(`FOLLOWUP_IMPLEMENTATION_PLAN_20261029.md`). And `DATA_REQUIREMENTS_20261029.csv` already carries:

> **D05** — "National forest inventories and repeated field plots" · role **Validation** ·
> priority **Core where available** · spatial support "Plot to inventory domain" · temporal "Record
> actual survey dates" · minimum variables "AGB methods; dates; locations; sampling design; errors;
> training overlap" · critical limit "Inventories may also train maps; level validation does not
> validate change" · provider **"Country inventory provider selection pending"**.

The NFI release satisfies D05 item-for-item: AGB from documented equations, survey dates, plot
locations, a standardized sampling design, and repeat measurements (2000–2022, Yukon now included).
It also fits the plan's structure: "independently held-out" physical validation of account movements,
with the caveat D05 itself flags — inventory plots are also used to train biomass maps, so
independence must be argued, and level validation ≠ change validation.

**"Provider selection pending" is the open slot, and this release is a candidate for it.**

## 4. Consequence for timing (revised)

- Inserting NFI into **C20 A01** is out: the paper has no Canadian content, and the EM package,
  portal-safe compile verification (38/31 pp) and the Zenodo deposit
  (`10.5281/zenodo.24092131`, md5 `8a51345b76609063d10c8a282c1b8387`) are all frozen around it.
- Filing the request for the **follow-up is not blocked by the EM submission at all** — the follow-up
  has no manuscript and no submission clock. Requests have review + delivery latency, so filing early
  shortens the lead time on D05 rather than creating work now.
- The only real cost is a commitment: an NFI request names a project and a use, so the project
  description should be the follow-up's masking-validation study, not C20 A01.

## 5. Recommendation (revised)

**File the NFI data request against the follow-up project's D05 slot — not against C20 A01, and not
"after submission" for its own sake.**

Request should specify:

- **Purpose**: independent physical-biomass validation of account-level signals in the follow-up's
  masking analysis (D05 validation role), Canada as the country-inventory case.
- **Coordinates: ±10 km rounded, not exact.** Rounding is enough for plot→inventory-domain aggregation
  and keeps the request cleanly inside NFI confidentiality rules; exact coordinates matter only for
  slope/aspect or edge-effect work, which this analysis does not do.
- **Variables**: `PLOTBIO_LGTR_LIVE`; `BIOMASS_TOTAL/WOOD/STEMWOOD/STEMBARK/BRANCHES/FOLIAGE`;
  `MEAS_NUM`, `MEAS_DATE`; plot size; `BMEQ_*` IDs; province/territory; small-tree and stump tables;
  plus the equation support table (`gpcsd_tree_biom_eqs`) so the biomass chain is reproducible end to end.
- **Years**: full available span to 2022, so the second remeasurement period and the new Yukon plots are included.

Say which you want and I'll do it: (a) draft the request text for you to send, (b) add the D05 provider
selection note (Canada / NFI, with this release's version) to the follow-up data-requirements record —
a plan-document edit, not a manuscript edit — or (c) leave the record as is.

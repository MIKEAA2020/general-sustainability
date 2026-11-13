# NFI (NRCan) ground-plot release — fit assessment for ECOMOD C20 A01

Date: 2026-11-13. Trigger: forwarded email from Michael Smith (NRCan, Canadian Forest Service).
Decision requested: whether to request data now, log it, or set aside. **Assessment only — no data
request filed, no manuscript change made.**

## 1. What the release is

- New National Forest Inventory (NFI) **ground plot** data, released annually since 2000 under NFI's
  standardized pan-Canadian design; latest release extends **measurements through 2022** and includes
  the **first Yukon ground plot data** (previously territory absent).
- Plot-level and tree-level attributes: DBH, height, species, condition/damage, stump and woody-debris
  measures, compiled volume and **aboveground biomass (kg oven-dry) by component** — stem wood, stem
  bark, branches, foliage — for large trees (DBH ≥ 9 cm), small trees (DBH < 9 cm) and stumps.
- Biomass is computed from **individual-tree and shrub biomass equations** (published coefficients;
  `BMEQ_*` equation IDs are carried in the data so any value can be traced to its equation).
- Ground plots are thus a genuine **physical** measurement layer: per-hectare biomass by component,
  remeasured over time — not a value-weighted account.
- Access: two routes. The **Data Download Tool** (`https://nfi.nfis.org/en/datadownloadtool`) for
  authorized users, and the **Data Request Form** (`https://nfi.nfis.org/en/datarequestform`) for
  anyone, with a project description and a stated coordinate precision choice (**exact** vs
  **±10 km rounded**). Licence: Open Government Licence – Canada (attribution required).
  Standards documented in *NFI National Standards for Ground Plots* (compilation procedures v2.4,
  data dictionary for the 2018–2027 second remeasurement period, v6.0).

## 2. What C20 A01 actually uses

Verified in the deposited sources (`ecomod_deposit_doi_C20_A01/`):

| Check | Result |
|---|---|
| Occurrences of "Canada"/"Canadian" in main text | **0** |
| Same in Supplementary Information | **0** |
| Empirical section (§3.7, "NFA account composition, 1961–2023") | **World aggregate only** — NFA Edition 2026, results+metadata v1.0, 1961–2023, 2024–2025 excluded |
| Sensitivity window | 1961–2022, same edition, same population series |
| Second empirical input | OWID/FAOSTAT **world** cropland area + cereal yield (illustrative proxy) |
| Model calibration | None from national data; parameters are representative, not fitted |

So the paper contains **no Canadian series at all**. §3.7 is a world-aggregate accounting decomposition
(B +24.86 %, B/person −52.71 %, E_prod/person +16.73 %, cropland +24.06 pp etc.). NFI data — Canadian,
sub-national, physical-biomass — cannot enter that computation without changing its unit of analysis.

## 3. Where NFI *would* fit, and where it cannot

NFI speaks directly to one stated gap. SI §S5 "Observation-operator hierarchy", item
*Ecological-capital components* currently reads: separate physical observation operators **could** use
forest extent and biomass, soil carbon and condition, wetland extent and condition, fish biomass by
stock, and "we assembled no common-boundary global physical-stock series for these components."

NFI is exactly such a physical forest-biomass operator — for **one country**. Consequences:

- **Cannot** support the world NFA decomposition (different boundary, different unit, one country).
- **Cannot** substitute for NFA forest biocapacity (account value vs. measured biomass) — the paper is
  explicit that these are not interchangeable, and that `Y_c = Υ(q)A_c` is not identified by either.
- **Could** support a *separate* single-country demonstration: measured forest biomass/removals as an
  independent observation operator alongside an account value, i.e. a worked example of the hierarchy
  the SI already describes in the abstract.
- Would require a **new analysis unit, new figure or table, and new text** — a scope extension, not a
  layout or verification fix. It also breaks the standing freeze on adding national cases (eight
  national holds unchanged) and would reopen the manuscript during EM submission.

## 4. Why now is the wrong moment

- The manuscript is in EM submission with a fixed 13-item upload list and portal-safe sources verified
  to compile at 38/31 pp. Any added section invalidates that verification and the reproduction package
  (Zenodo `10.5281/zenodo.24092131`, md5 `8a51345b76609063d10c8a282c1b8387`).
- The NFI request itself has latency (request review + delivery), so it cannot be in hand inside this
  submission cycle anyway.
- Editorial constraint on record: "Don't touch the content. Fix the layout or leave it to copy editor."

## 5. Recommendation

**Log it as a candidate source for the post-submission extension; do not request data for C20 A01.**
Concretely, treat it as the named candidate for the SI §S5 forest-biomass operator in any follow-up
paper, where a Canada case study (with Yukon now available, 2000–2022 remeasurements) would be a
defensible single-country illustration. When that time comes:

- Request **±10 km rounded coordinates**, not exact: plot-level biomass aggregates are unaffected at
  national/regional scale, and rounding keeps the request cleanly inside NFI's confidentiality rules —
  exact coordinates are only needed for slope/aspect or edge-effect work, neither of which applies here.
- Ask for: `PLOTBIO_LGTR_LIVE`, component biomass (`BIOMASS_STEMWOOD/STEMBARK/BRANCHES/FOLIAGE/
  TOTAL`), `MEAS_NUM`/`MEAS_DATE`, plot size, `BMEQ_*` IDs, province/territory, and the small-tree and
  stump tables; plus the equation support table so the biomass chain is reproducible.

**Nothing has been filed and nothing in the manuscript has changed.** Say the word if you want me to
(a) file the request anyway, (b) draft the request text for you to send, or (c) add a one-line
"candidate future source" note to the repo audit notes (no manuscript edit).

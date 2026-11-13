# R1 — Canada's National Forest Inventory (NFI) ground plot data request

**Route:** NFI Data Request Form, https://nfi.nfis.org/en/datarequestform
**Also send as an email** to the NFI Project Office / Michael Smith (NRCan–CFS) — the release
announcement is the natural thread, and the two clarification items below are questions the form has
no field for.
**Unblocks:** follow-up paper, F13 remaining-work items **1** (primary calibrated national forest-AGB
comparison 2015–2023) and **4** (Canadian current-period/coverage and uncertainty reconciliation).

---

## A. Form fields

**Project title**
Boundary-matched test of composition masking: independent physical-biomass validation of national
biocapacity accounts.

**Requester**
Amin Abaee, Independent Researcher, Tehran, Iran — amin_abaee@ut.ac.ir, ORCID 0000-0002-0019-1842.

**Project description (form text)**
> We are testing whether improvements in national biological-supply accounts (National Footprint and
> Biocapacity Accounts, global hectares) are accompanied by independently measured changes in physical
> forest aboveground biomass within matched boundaries and periods. Canada is one of eight national
> cases in the study. The required input is a repeated field-plot-based estimate of aboveground
> biomass stock and change, with a credible sampling design, used separately from, and never as a
> substitute for, the value-weighted account. NFI ground plots are the only Canadian source with the
> required design information. The work is non-commercial academic research; results will be published
> in a peer-reviewed journal, NFI and NRCan will be acknowledged and cited as specified, and no
> plot-level record will be redistributed — only aggregates derived under NFI's stated support and
> confidentiality rules.

**Coordinates**
> **Rounded to ±10 km. Exact coordinates are not requested.** Our analysis aggregates plots to the
> inventory domain; we do not evaluate slope, aspect or edge effects, so sub-kilometre location adds
> nothing to our use.

**Geographic coverage**
> All jurisdictions available, **including Yukon and any other northern coverage** in the current
> release. Coverage north of the current inventory boundary is central to our use: the published
> Canada-wide change estimate omits a large northern area (262.190 million ha), and we need to state
> explicitly whether the omission is a definitional exclusion, a sampling gap, or a projection.

**Period**
> All available measurement years through the **2022** release, with actual survey dates, so we can
> construct same-period contrasts rather than assume calendar endpoints.

**Variables requested (ground plots)**
- Plot and design: `NFI_PLOT`, `MEAS_NUM`, `MEAS_DATE`, plot size (`MEAS_PLOT_SIZE`), plot type,
  province/territory, ecozone, ownership/land-use class, projected-vs-observed status flag,
  artificial-change / disturbance flags.
- Large trees (DBH ≥ 9 cm): species, DBH, height, condition/damage, and
  `BIOMASS_TOTAL`, `BIOMASS_WOOD`, `BIOMASS_STEMWOOD`, `BIOMASS_STEMBARK`, `BIOMASS_BRANCHES`,
  `BIOMASS_FOLIAGE`, with the corresponding `BMEQ_*` equation IDs.
- Small trees (DBH < 9 cm): `SMTREE_BIOMASS`, `SMTREE_VOL_TOTAL`, projected height, `BMEQ_*`.
- Stumps and woody debris: `PLOTBIO_STUMP`, `PLOTBIO_SMSTUMP`, `PLOTBIO_ROUNDWD`, `PLOTVOL_ODDWD`.
- Plot-level compiled biomass: `PLOTBIO_LGTR_LIVE` and related compiled totals.
- **Support table `gpcsd_tree_biom_eqs`** (biomass equation definitions and coefficients), so the
  biomass chain from tree measurements to plot biomass is reproducible end to end.
- Any provided design information: plot selection/panel structure, remeasurement panel identifiers,
  and any documented inclusion probabilities or expansion factors.

**Format**
> CSV or equivalent tabular export, one file per logical table, with the corresponding data dictionary
> version (currently the 2018–2027 second remeasurement period, v6.0) and compilation-procedures
> version (v2.4). We can consume the NFI standard export layout; no custom product is needed.

**Ancillary**
> Photo-plot data are **not** requested, nor the Soil Sample Archive, HILLdata or CASFRI layers — our
> analysis is limited to ground-plot biomass.

---

## B. Two clarification questions (email; the form has no field for them)

These are the two items that currently block the Canadian case. Both are about documentation, not
additional data — which is why they are worth asking even if the plot request is declined.

> **1. Table 17C.0 change uncertainty.**
> The published national change estimates, their relative standard errors and their confidence
> intervals do not reconcile under the ordinary definition, across all three HTML representations that
> carry the same version 3.1 label. We are not asking you to re-estimate anything, and we will not
> substitute a narrower interval of our own. We need the *implementation*: (a) the exact definition of
> the change RSE — is it computed on the change estimate directly, from the two period estimates, or
> from a projected variance with a covariance term; (b) what confidence level and degrees of freedom
> the reported interval assumes; (c) whether the interval reflects sampling error alone or also
> model/projection error; and (d) whether remeasured and non-remeasured (projected) plots enter the
> change variance differently. A pointer to the estimation document or script implementing Table 17C.0
> would settle it.

> **2. Current-period coverage and the northern omission.**
> Which land areas within the NFI reporting domain are (i) sampled by ground plots, (ii) represented
> by photo plots only, or (iii) excluded and represented by projection? Specifically, how is the
> ~262.190 million ha of northern geography treated in the current change estimates, and does the
> Yukon ground-plot release change that treatment? We need to describe coverage limits honestly rather
> than assume they are uniform.

---

## C. Short summary field (if the form caps the description)

> Non-commercial academic study testing whether reported increases in national biological-supply
> accounts are accompanied by independent physical changes in forest aboveground biomass. Canada is
> one of eight national cases. Requesting NFI ground-plot data through the 2022 release, all
> jurisdictions including Yukon, coordinates rounded to ±10 km, with tree- and plot-level biomass by
> component and the `BMEQ_*` equation support table, plus survey dates and design information. Results
> will be published in a peer-reviewed journal with NFI/NRCan acknowledged and cited; no plot-level
> record will be redistributed.

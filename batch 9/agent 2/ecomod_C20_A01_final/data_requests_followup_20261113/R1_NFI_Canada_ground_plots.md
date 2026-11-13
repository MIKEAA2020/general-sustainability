# R1 — NFI (Canada) data request — form-ready

**Route:** https://nfi.nfis.org/en/datarequestform
**Unblocks:** follow-up paper (F13) items **1** (primary calibrated national forest-AGB comparison
2015–2023) and **4** (Canadian current-period/coverage and uncertainty reconciliation).
**Form checked live on 2026-11-13** — field names, character limits and the exact-coordinate warning
below are quoted from the form itself.

---

## 1. Data Type — what to tick

The form offers nine checkboxes: Photo Plot, Map Product, **Ground Plot**, Special Analysis,
HILL Dataset, Access to Archived Soil Samples, **MAGPlot**, **Other**, CASFRI.

### Tick: **Ground Plot** — required, this is the whole request
Tree- and plot-level AGB by component, remeasured plots, survey dates, `BMEQ_*` equation IDs, and a
sampling design. Nothing else gives a physical biomass observation with design information.

### Tick: **MAGPlot** — yes, and this is the one that covers Yukon
Per the Data Access Guide, MAGPlot is "a forest ground-plot dataset repository from the NFI and 12
Canadian jurisdictions (excluding NU)". Canada has 13 provinces/territories, so **excluding Nunavut
means Yukon and all other jurisdictions are in scope** — which is exactly the northern coverage gap
(item 4). It also widens the plot base behind item 1.
Caveat to state in the request: provincial/territorial contributions may not share the NFI plot design,
so ask for NFI-standard vs. jurisdiction-contributed plots to be flagged, with their designs. If the
office says MAGPlot would stall the request, **drop it and keep Ground Plot alone** — MAGPlot is
additive, not load-bearing.

### Tick: **Other** — optional
Only if you want the Table 17C.0 uncertainty documentation to travel *inside* the request record.
Recommended: **leave it unticked** and carry those two documentation questions in the email thread
(below), because the 500-character Request Details field cannot hold them without pushing out the
data specification, which is the part the office actually needs.

### Do not tick
| Option | Why not |
|---|---|
| **Photo Plot** | The 1 % photo-plot sample gives land-use/cover and forest attributes, not measured tree biomass. It answers "which area is photo-only", a **documentation** question, asked in the email. Requesting the data would enlarge the ask without serving the AGB comparison. |
| **Map Product** | Model/derived maps are not physical observations; SCANFI v2 is already publicly downloadable, and its 5-year periods cannot be relabelled as a 2023 endpoint. |
| **Special Analysis** | Would have NFI staff run a custom analysis for us. Hold as a **fallback only** — if plot-level release is refused, a custom national AGB change tabulation *with design-based variance* becomes the best remaining route. |
| **HILL Dataset** | Human-activity mapping near forests; a pressure layer, not biomass. |
| **Access to Archived Soil Samples** | Soil carbon belongs to the follow-up's later ecological-capital components, not the pre-specified forest–cropland core; the form warns this "may have costs associated", and physical sample handling is out of scope now. |
| **CASFRI** | Harmonized vector forest inventory for management/conservation — a compilation of heterogeneous provincial inventories, not repeated field plots with a design. Extent-only, and not design-based. |

---

## 2. Exact Coordinates — answer **No**

The form asks: "If requesting ground plot data, are exact coordinates needed?" and warns that
requesting them "could significantly delay the release of NFI data to fulfill your request", with
coordinates "by default rounded to +/- 10 kilometers".

**Answer No.** The analytical case is not a compromise, it is the correct answer:

- Our analysis unit is the **ecozone and the national inventory domain**. Province/territory and
  ecozone are **supplied as attributes**, so we never need coordinates to place a plot.
- Plot matching across remeasurements is by **`NFI_PLOT` / `MEAS_NUM` identifiers**, not by location.
- Exact coordinates matter for slope, aspect, edge effects, or sub-kilometre site matching. **We do none
  of these.** Requesting them would be a request for no analytical gain, at the cost of delay.
- The NFI terms state the data are "intended for ecozone or national-level analysis". Asking for
  rounded coordinates is consistent with the use we actually declare; asking for exact ones would not be.

---

## 3. Remaining fields — copy-paste values

| Field | Value |
|---|---|
| First/Last name, Email, Phone | Amin Abaee · amin_abaee@ut.ac.ir · (your phone) |
| Project Lead | same as requestor |
| Title | Mr |
| Organization | Independent Researcher |
| Country | **Iran** |
| **Affiliation (check one)** | **Other** — the list has no "independent researcher"; "Private" reads as industry, "University" is false |
| Project Title | Boundary-matched test of composition masking: independent physical-biomass validation of national biocapacity accounts |
| Project Start Date (YYYY) | 2026 |
| Project End Date (YYYY) | 2028 |
| Project URL | leave blank (or the Zenodo DOI 10.5281/zenodo.24092131 of the companion deposit) |
| **Study Area** | **Canada** (national). Not Prov/Terr — we make no jurisdiction-level inference, and the terms require other sources for that scale. |
| Join NFI Data Community | **Yes** — annual releases; this is how you learn the next one exists |

### Project Objectives (1,297 / 1,500 characters)

> Purpose: test whether reported increases in national biological-supply accounts (National Footprint
> and Biocapacity Accounts, gha, 1961-2023) are accompanied by independently measured changes in forest
> aboveground biomass within matched boundaries and periods. Canada is one of eight national cases in a
> peer-reviewed empirical study, and it is currently the case with unresolved change uncertainty:
> published annualized AGB change of +17.639 Mt/year carries a labelled interval of [-21.279, 56.557]
> Mt/year, and the reported change RSE and interval do not reconcile under the ordinary definition.
>
> NFI ground plots are the only Canadian source with both repeated field measurements and design
> information. Intended uses: (1) national and ecozone-level AGB stock and change as an independent
> physical observation, kept strictly separate from the value-weighted account and never substituted for
> it; (2) coverage characterization, i.e. which parts of the NFI reporting domain are ground-sampled,
> photo-plot only, or represented by projection; (3) comparison of remeasured versus projected
> observations within the change estimate.
>
> Non-commercial academic research. Analysis at ecozone or national level only, consistent with NFI
> terms; no plot-level results published and no raw data redistributed.

### Project Deliverables (545 / 1,000 characters)

> Peer-reviewed journal article (empirical follow-up paper) with main text and supplementary
> information. Published outputs are derived aggregates only (national and ecozone AGB totals, changes
> and bounded uncertainty), with the Canadian National Forest Inventory and NRCan acknowledged as
> specified. A methods appendix documents exactly how the change variance is computed and how the
> northern coverage omission is treated, so the treatment is reproducible. A short written summary of
> Canadian findings can be provided to the NFI team on request.

### Request Details (475 / 500 characters)

> Ground plots: all jurisdictions incl. Yukon, measurement years through the 2022 release, coordinates
> rounded to +/-10 km. Attributes: plot/measurement IDs, survey dates, plot size, province/territory,
> ecozone, projected-vs-observed and disturbance flags; tree and small-tree records with component
> biomass and BMEQ_* IDs; stump/woody-debris biomass; support table gpcsd_tree_biom_eqs; dictionary v6.0.
> MAGPlot: flag NFI-standard vs jurisdiction-contributed plots and designs.

---

## 4. Email accompanying the form — two documentation questions

Send to the NFI Project Office / Michael Smith, replying to the release announcement. The form has no
field for these, and item 4 cannot close without them:

> **1. Table 17C.0 change uncertainty.** The published national change estimates, their relative
> standard errors and their confidence intervals do not reconcile under the ordinary definition, across
> all three HTML representations carrying the same version 3.1 label. We are not asking for a
> re-estimate and will not substitute a narrower interval of our own. We need the implementation: (a) is
> the change RSE computed on the change directly, from the two period estimates, or from a projected
> variance with a covariance term; (b) what confidence level and degrees of freedom does the interval
> assume; (c) does it reflect sampling error alone or also model/projection error; (d) do remeasured and
> projected plots enter the change variance differently? A pointer to the estimation document or
> program implementing Table 17C.0 would settle it.
>
> **2. Coverage classes and the northern omission.** Which land areas in the NFI reporting domain are
> (i) sampled by ground plots, (ii) represented by photo plots only, or (iii) excluded and represented
> by projection? Specifically, how is the ~262.190 million ha of northern geography treated in the
> current change estimates, and does the Yukon ground-plot release change that treatment? We need to
> describe coverage limits rather than assume they are uniform.

---

## 5. Terms to obey once data arrive

The form's declaration is binding: derived products only, no raw data publication, one project per
request, NFI acknowledged in any publication. So CANFIS/NFI plot records stay out of the deposited
reproduction package — unlike C20's world-account inputs, the Canadian plot layer cannot be
redistributed, and the package will carry derived aggregates plus the script.

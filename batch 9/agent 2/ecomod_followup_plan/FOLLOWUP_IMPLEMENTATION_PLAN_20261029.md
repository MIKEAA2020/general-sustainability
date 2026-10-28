# Follow-up implementation plan: ecological assets behind improving accounts

**Planning date:** 29 October 2026  
**Status:** Proposed empirical research protocol, not completed analysis or a claim of novelty.  
**Relationship to ECOMOD:** Test the observable implications of composition masking using independent physical-asset estimates. Do not attempt to empirically validate the entire projected-delay model or equate observed assets with its uncalibrated q. The source-revision anchor is continued_12 at commit `65c8464a3cf83d9aef525cb6695668898de18ac6`, under `batch 9/agent 2/ecomod_audit/`; no C12 source is edited by this plan.

## 1. Executive decision

**Include both aims, but organize them as one nested study rather than two competing papers.**

1. **Measure what is happening to specified ecological assets.** This supplies the physical outcomes and establishes where decline, increase or unresolved change is supported.
2. **Test whether improving biological-supply accounts coexist with those losses, and whether documented land conversion explains the compositional pattern.** This is the direct follow-up to ECOMOD.

The unifying question is:

> When biological-supply accounts improve, what happens to independently estimated ecosystem extent, stocks and condition, and how much of any divergence is associated with land-use conversion rather than within-class improvement or accounting changes?

**Recommended scope:** A forest–cropland empirical core, a four-component evidence scoreboard with honest missingness, and optional soil/wetland/fisheries modules that are not prerequisites for the core paper. Do not promise an annual global time series for all four components or a scalar global ecological-capital stock.

### Working title

**Ecological assets behind improving accounts: a boundary-matched test of composition masking**

Avoid a title asserting decline before observing results. High impact is an aspiration, not a demonstrated novelty or publication forecast.

## 2. What the paper should contribute

The contribution is not “natural capital has never been measured.” Existing assessments already measure particular assets. For example, FRA 2025 reports that global forest growing stock, biomass and carbon increased after 2000, while noting substantial climatic-domain differences, including tropical declines. Those findings rule out presuming that every physical forest measure must decline together. [1](https://openknowledge.fao.org/server/api/core/bitstreams/2dee6e93-1988-4659-aa89-30dd20b43b15/content/FRA-2025/key-findings.html)

The intended advance is a reproducible connection between:

- an explicit accounting signal;
- physically defined asset changes;
- an observed land-transition pathway;
- the assessment consequence of reading one without the others;
- uncertainty, coverage and boundary sensitivity.

A literature screen must establish how much of that combination is new. A multicolour dashboard alone is unlikely to be sufficient. A convincing negative result—little robust masking in eligible observations—is publishable evidence about the mechanism's limits and must remain an allowed outcome.

## 3. Claims ladder: distinguish what each analysis establishes

| Level | Allowed conclusion | Additional evidence needed for a stronger claim |
|---|---|---|
| 1. Asset trend | Specified physical stock/extent changed within a defined domain and period | Comparable repeat estimates, uncertainty and coverage |
| 2. Aggregate–asset divergence | A reported account increase coexists with a resolved decline in that asset | Matched domains/dates; do not infer conversion from coexistence |
| 3. Composition pathway | Divergence is consistent with independently observed forest-to-crop transition and account decomposition | Transition maps, within-class changes, disturbance controls and mapping assumptions |
| 4. Causal mechanism | An identified intervention or pressure caused conversion and the resulting divergence | Separate identification design, assumptions and diagnostics |
| 5. ECOMOD dynamics | The particular shortfall rule, delayed q law, parameters or irreversibility describe the system | A new measurement/identification exercise; outside this paper's default scope |

Do not call a forest-account/biomass disagreement the same test as total-account/capital-area masking. The former is a **within-category account–stock discrepancy**; the latter is an **aggregate–asset divergence**. Conversion-linked divergence is a third, stronger result.

## 4. Primary questions and pre-specified outcomes

### Q1 — What is changing physically?

Estimate forest extent, above-ground biomass stock, and their spatial distribution separately. Where available, add independent structure/condition indicators. Do not call AGB a complete measure of biodiversity, integrity or ecosystem capacity.

### Q2 — Does the aggregate conceal that change?

Across all eligible country–interval observations, estimate the frequency and size of:

- increasing account / decreasing asset;
- increasing account / increasing asset;
- decreasing account / decreasing asset;
- decreasing account / increasing asset;
- unresolved or insufficiently observed changes.

The reported frequency applies to the eligible sample, not automatically to all countries or all natural capital.

### Q3 — Is land conversion part of the explanation?

Test whether independently mapped forest-to-cropland transitions are associated with the amount of aggregate–asset divergence, considering agricultural productivity, forest regrowth, planted forests, timber harvest, fire and climate. Assess associations in the full eligible sample; do not fit the main model only after selecting increasing-account cases.

### Q4 — Does adding asset information change an assessment?

Compare a pre-specified **account-improvement screen** with a **joint account-and-asset reporting rule**. These are transparent study-defined diagnostics, not universal sustainability standards. Quantify cases where an account-only improvement label coexists with a resolved asset loss. Avoid declaring “unsafe” without a justified asset threshold.

## 5. Dataset assessment: corrections to the proposed inventory

### Forest biomass — strongest core, but estimates are not independent truth

The proposed 2007/2010/2015–2022 inventory describes ESA CCI Biomass v6. The verified current ESA catalogue lists **v7.0**, with 100 m maps for **2005–2012 and 2015–2024**, AGB uncertainty, change products, change uncertainty and quality flags. It explicitly notes updated earlier maps and ICESat-2 calibration information. Freeze a single release; do not mix v6 early years with v7 later years. [2](https://climate.esa.int/en/catalogue/6429d1aafe1e43b9b414e4a5a7f8b903/)

100 m is grid spacing, not guaranteed effective change-detection precision. Download the product documentation and relevant regional tiles first, not the entire approximately 816 GB catalogue. [2](https://climate.esa.int/en/catalogue/6429d1aafe1e43b9b414e4a5a7f8b903/)

**Validation rule:** GEDI, ICESat-2, CCI and national inventories may share calibration data or models. The ESA catalogue explicitly describes ICESat-2 inputs; they cannot automatically be called independent benchmarks. GEDI offers footprint and gridded biomass products, but its sampling support differs from wall-to-wall maps. Build a training/validation lineage table; reserve genuinely held-out field inventories where possible. [2](https://climate.esa.int/en/catalogue/6429d1aafe1e43b9b414e4a5a7f8b903/) [1](https://gedi.umd.edu/dataproducts/download/)

Use **FRA 2025**, with country-report measurement dates and methods, for updated long-run context; FRA 2020 can be a vintage sensitivity, not the default latest assessment. FRA values must not be presumed independent of national inventories used elsewhere. [1](https://openknowledge.fao.org/server/api/core/bitstreams/2dee6e93-1988-4659-aa89-30dd20b43b15/content/FRA-2025/key-findings.html)

### Soil organic carbon — baseline feasible; change is a separate acquisition problem

SoilGrids 2.0 offers mapped SOC stock for 0–30 cm at 250 m, with prediction quantiles and model-derived spatial estimates. It is not an annual repeat-inventory series. [1](https://data.isric.org/geonetwork/srv/api/records/713396f4-1687-11ea-a7c0-a0481ca9e724)

Acquire repeated national inventory/plot observations with dates, depths, bulk density, coarse fragments and management histories to estimate change. Use consistent depth or an explicit equivalent-soil-mass approach where appropriate. SoilGrids/GSOCmap can provide baseline context or sampling strata, not observational trend merely by differencing product releases.

**Reject this inference:** a cited 17–23-year equilibration timescale does not guarantee detectable SOC change over 20–30 years. Detectability depends on effect size, sampling design, stock-estimation errors and disturbances. The existing ECOMOD recovery summaries are not a power calculation.

**Gate:** No defensible repeat observations means “stock baseline only; trend not assessed,” not a reconstructed observational decline.

### Wetlands — distinguish hydrological state from persistent asset loss

GIEMS-MC v1.1 is a verified archive of monthly 0.25-degree wetland surfaces for 1992–2020, including inundated/saturated wetlands and an all-wetlands/peatlands layer. The product is designed for methane-emitting aquatic areas, incorporating static masks and other ancillary information. Its publication discusses limitations involving rice, coastal and peatland areas. [1](https://zenodo.org/records/16530038) [1](https://essd.copernicus.org/articles/17/2985/2025/)

This is useful for hydroperiod and inundation anomalies, **not by itself proof of permanent wetland conversion or peat-stock depletion**. A dry year can reduce inundation without destroying the ecosystem; a flooded degraded wetland can retain inundation while losing condition.

Require repeat, finer-scale ecosystem/land-use observations and local inventories to classify persistent conversion. Use GLWDv2 for baseline delineation, not as an annual history. Separate climate-driven variability, drainage, rice changes and permanent conversion. Do not upsample the coarse product and report invented 100 m change detail.

### Fisheries — useful external domain; not part of the terrestrial conversion regression

RAM Legacy v4.66 is a verified archived release. Do not label it the latest without checking the provider/version registry at data freeze. Prefer its assessment-data-only version for the primary analysis; the separately archived extended release contains additional gap-filled/model-generated quantities, and its documentation recommends the assessment-only version for ordinary use. [1](https://zenodo.org/records/14043031) [2](https://zenodo.org/records/14043038)

Analyse one selected assessment per stock, with stable units and a consistent historical reconstruction. Do not count repeated assessments as different stocks or add spawning-stock biomass to total biomass. Distinguish biomass in mass units from B/BMSY, a reference-relative status measure. Changing reference points and assessment revisions need explicit handling.

**Scope:** An assessed-stock sample, not a global fish census. Fisheries have stock/ecosystem boundaries that need not follow national borders. Do not manufacture a country biomass allocation or a global total by adding catch-model estimates to RAM without a separate integration model. Treat unassessed stocks as missing, with coverage metadata.

### Feasibility verdict

The infrastructure supports a **forest-led study now**, conditional soil and wetland trend modules, and an assessed-fisheries extension. It does **not** yet establish that all four can support an aligned annual physical-stock panel. Baseline availability, repeat-change detection and common-boundary comparability are distinct feasibility tests.

## 6. Data needed: minimum viable core

| Input | Required fields | Purpose | Blocking issue |
|---|---|---|---|
| Version-frozen NFA country accounts | Country ID, year, component and total biocapacity, observation/estimate flags, source vintage, units | Define account change | Country/year completeness and boundary reconciliation |
| NFA physical areas and factors, if available | Component area, yield/equivalence factors, reference definitions | Attribute account changes | Without factors, no claim to isolate equivalence-factor effects |
| ESA CCI Biomass v7 | AGB density, quality/no-data, epoch, uncertainty and supported change uncertainties | Estimate biomass stock and change | Temporal/spatial error dependence and conversion-pixel coverage |
| Consistent land-cover transition data | Natural/planted forest, crop, other classes, dates, transition error/validation | Measure extent and actual forest-to-crop pathway | Tree-cover loss is not automatically cropland conversion |
| Independent forest validation | Plot/inventory dates, locations, area, AGB methods, sampling errors, calibration overlap | Assess biomass levels/change | Shared training data; level validation is not change validation |
| Agricultural observations | Cropland physical area, harvested area separately, crop production/yields, units | Separate expansion and intensification | Double cropping; tonnes/calories cannot be subtracted from gha |
| Boundaries | Stable country polygons, disputed/boundary-change crosswalk, land masks | Common spatial support | Downscaling national B does not create an observed local account |
| Disturbance/environment covariates | Fire, rainfall/drought, harvest, storm where relevant; dates/coverage | Alternative explanations | Do not interpret every biomass loss as conversion |
| Population | Consistent series and vintage | Report per-person results separately | Per-person decline is not absolute stock decline |

**Additional modules:** SOC repeat inventories; wetland transition/condition data plus GIEMS-MC; RAM stock assessment and boundary/coverage metadata. These require separate observation models and are not interchangeable rows in one scalar stock.

## 7. Sample, domains and time windows

### Core window

Use **2015–2023 as the provisional main overlap** between v7 forest observations and the already audited NFA complete-data endpoint. Verify country-specific NFA flags before locking this window. Evaluate 2010–2020 or other supported epoch pairs as a historical sensitivity, conditional on cross-sensor change quality. Do not interpolate missing 2013–2014 biomass years and call them observations.

Eight-year change may be too small relative to uncertainty in some domains. This is a pilot go/no-go condition, not a reason to declare small estimated losses significant.

### Geographic design

1. Screen all candidate countries using **pre-outcome data availability/quality criteria**.
2. Select a pilot of approximately 6–8 countries spanning forest conversion, forest recovery/plantations, and relatively stable land use. Names such as Brazil and Indonesia are candidates, not predetermined positive findings; candidate controls must be selected under the same rules.
3. Scale to the eligible panel only if physical-change precision and transition validity pass. A planning target of roughly 20–40 countries is not a power justification or a required sample size.
4. Add subnational landscapes for pathway validation. Compare their physical dynamics with local measured production if available; do not assign national NFA B to them without identifying a modelled allocation as such.

### Account domains

Report national total B, a clearly labelled terrestrial subtotal, and a pre-specified excluding-built-up sensitivity. Keep the component definitions visible. The terrestrial subtotal helps distinguish land-conversion evidence from unrelated changes in marine accounts. None of these is a physical-capital total.

Global, national, biome and local quantities cannot be substituted for one another. Do not force national accounting categories into the conserved two-land partition of ECOMOD.

## 8. Physical-stock estimation and decomposition

### 8.1 Extent and density must remain separate

For a defined domain i,

`M_it = sum_p a_p * m_pt`,

where a_p is pixel area and m_pt is biomass density with valid observation support. Apply equal-area/geodesic area calculations and record units. Do not sum Mg/ha pixel values without multiplying by hectares.

Produce separate estimates for:

- stable forest;
- mapped forest-to-crop transitions;
- forest gains/regrowth;
- other disturbances;
- unknown/unobserved transitions.

A pixel leaving a forest mask is not automatically observed to have zero remaining woody biomass. If the AGB product does not support that converted pixel, report an uncertainty/coverage gap or bring in an appropriate independent estimate. Report **forest-class biomass** and **total woody biomass on a fixed geographic domain** as different estimands when both are feasible.

Within a compatible class, use the exact midpoint identity:

`Delta(A*m) = mean(m)*Delta A + mean(A)*Delta m`.

It separates extent and mean-density contributions, but a changing class membership can still change the mean composition. Use transition strata to interpret that change rather than equating it automatically with deterioration of surviving forest.

### 8.2 Account decomposition

For compatible component area A_j and account intensity v_j=B_j/A_j,

`Delta B_j = mean(v_j)*Delta A_j + mean(A_j)*Delta v_j`.

This is an exact two-factor level decomposition. v_j is **account value per area**, not necessarily physical crop yield. Further separate productivity, reference normalization and equivalence factors only when the requisite metadata support it. Otherwise keep them bundled and say so.

Fixed-reference counterfactuals may test sensitivity to changing account weights, but must be labelled counterfactual account indices. Do not confuse them with independently observed biological production.

### 8.3 Do not use the crop residual to identify capital

All-crop measures improve agricultural description but do not establish `B-bf*Af=observed capital`. The model identity is not an empirical observation equation until boundaries, units, valuation and omitted components are mapped and validated. Keep any crop-index residual as a secondary accounting diagnostic, not the primary physical outcome.

## 9. Uncertainty, tests and statistical analysis

### Error propagation

For biomass change:

`Var(M1-M0)=Var(M1)+Var(M0)-2 Cov(M1,M0)`.

For spatial aggregation, include cross-pixel covariance; dividing pixel uncertainty by sqrt(number of pixels) is not a defensible default. Prefer product-supported change uncertainty and propagate plausible spatial/temporal dependence with documented sensitivity analyses. Plot-level confidence, map prediction error and change-detection uncertainty are different quantities.

Carry land-transition classification uncertainty, missing area, validation bias, forest-definition choices and data-vintage sensitivity. Do not assume that alternative maps are independent replications.

### Account uncertainty

An NFA point estimate with revision sensitivity does not provide a sampling confidence interval. If defensible probabilistic account errors are unavailable, report:

> a reported account increase in the frozen edition, accompanied by a statistically resolved physical decline under the specified physical observation model.

Do not fabricate a joint 95% probability of masking. Test account-sign stability under supported vintages, factor conventions and practical-change thresholds, labelling those as scenarios rather than calibrated confidence bounds.

### Primary analysis

- Plot continuous paired changes first; classification is a secondary communication device.
- Pre-specify practically meaningful changes before outcomes are inspected; report sensitivity to thresholds and an unresolved category.
- Distinguish total from per-person stock/account change.
- Provide country and area/stock-weighted summaries separately, with the eligible population stated. Do not silently weight all indicators or all countries equally.
- Estimate interval-change associations with conversion and relevant covariates. With repeated observations, address country clustering and temporal dependence; use spatial blocks where appropriate. Effective sample size is not the raster-pixel count.
- Apply multiplicity control or an explicitly hierarchical analysis for numerous assets/regions. Do not headline only significant losses.
- Use a causal event study or difference-in-differences only if an actual treatment/comparison design, timing and identifying assumptions exist. Ordinary panel fixed effects do not establish that overshoot caused depletion.
- Treat Eprod/B, if used, as an account pressure ratio, not an identified land-clearing trigger or a direct observation of ECOMOD's conversion rule. Trade and differing footprint boundaries matter.

## 10. Four-component scoreboard specification

Each row is an asset–domain–interval observation, not a forced annual country record.

Minimum fields:

`asset_id, metric, domain_id, domain_type, t0, t1, unit, estimate_t0, estimate_t1, absolute_change, relative_change, uncertainty_method, uncertainty_interval, coverage_fraction, estimator_type, source_version, account_domain_match, quality_status, trend_status, limitations`.

Distinguish **increase / decrease / unresolved / not assessed**. Preserve the difference between “no detectable decline” and evidence of stability. Add separate condition indicators where data allow; extent alone cannot represent condition.

The scoreboard should include forest, SOC, wetland and fish rows even if some say “trend not assessed.” Do not aggregate them into a capital scalar, vote “three of four declined,” or interpret the absence of one component as zero. Forest and wetland carbon/SOC overlap must be mapped before any later carbon aggregation.

A scalar capital index is optional future work requiring explicit asset coverage, weights/valuation, substitution assumptions, overlap treatment and sensitivity. Non-identification from B alone does not make external valuation impossible; it means additional information and normative choices are required. NPP is a flow, not a universal stock unit; common carbon units do not make ecological functions interchangeable.

## 11. Implementation work packages and decision gates

Times are planning estimates for a small team with geospatial, ecological and statistical expertise, after access is available. They are not guarantees.

| Phase | Approximate effort | Tasks and deliverables | Gate |
|---|---|---|---|
| 0. Novelty and estimands | 1–2 weeks | Literature matrix; asset/domain definitions; claim ladder; preregistration draft | Demonstrate a contribution beyond existing condition/wealth/account comparisons |
| 1. Data audit and pilot | 2–3 weeks | Frozen source registry; licences; 6–8-country pilot; lineage table; small tile/sample downloads | Matched intervals and adequate change precision; no fatal boundary mismatch |
| 2. Core extraction | 3–4 weeks | Physical stock/extent estimates; validated transition strata; accounts and agriculture tables | Reconcile masks, units, missing coverage and source totals |
| 3. Decomposition and uncertainty | 2–3 weeks | Account/physical decompositions; covariance-sensitive uncertainty; robustness | Main results not driven solely by sensor breaks or unknown converted pixels |
| 4. Mechanism and reporting analysis | 2–3 weeks | Eligible-panel associations; discrepancy typology; diagnostic comparison; negative controls | Claims remain within identification strength |
| 5. Writing and reproducibility | 2–3 weeks | Main/SI, figures, limitations, code tests, immutable archive | Independent rerun from manifest to tables and figures |

**Core total:** roughly 12–18 weeks conditional on data readiness, with possible overlap. Repeated SOC observations or wetland-condition work may require a separate, longer collaboration. Do not delay a coherent forest-led paper indefinitely to force four superficially complete time series.

### Minimum viable paper

- Frozen national account series plus boundary-matched forest extent/AGB change.
- Independently supported forest-to-cropland transitions in a subset.
- Explicit extent/density/account decomposition.
- Coverage-aware uncertainty and mixed/null cases.
- Four-component scoreboard that honestly distinguishes assessed trends from evidence gaps.

### Stop/reframe conditions

- If NFA/physical domains cannot be matched: present a local production–asset test, not an NFA validation.
- If AGB-change uncertainty overwhelms signals: lengthen supported intervals or focus on extent with a narrower title; do not infer biomass loss from mask loss alone.
- If conversion is not independently observed: claim account–asset divergence only, not the conversion mechanism.
- If novelty is insufficient: narrow to a genuinely informative mechanism/measurement comparison or publish a reusable data/method contribution without overstating impact.
- If outcomes are mixed or opposite to ECOMOD's illustration: retain them and explain scope; do not change the hypothesis after selection.

## 12. Figures, tables and reproducible outputs

**Main figures:**

1. Measurement/claims diagram separating account, extent, stock, condition and flows.
2. Matched account-versus-asset changes with uncertainty, unresolved cases and coverage.
3. Physical extent/density and account area/intensity decompositions.
4. Validated conversion landscapes versus stable/regrowth landscapes, without national-to-local account pseudo-observations.
5. Sensitivity of conclusions to spatial scale, reference weights and uncertainty assumptions.

**Main tables:** Dataset fitness/lineage; eligible sample/coverage; four-component scoreboard with metric-specific dates; assessment-label changes and scope.

**Repository design:**

```text
followup/
  protocol/            # preregistration, estimands, amendments
  metadata/            # source IDs, checksums, licences, lineage, boundaries
  configs/             # country eligibility, epochs, masks, uncertainty scenarios
  src/                 # ingest, harmonise, estimate, decompose, model, render
  tests/               # units, pixel areas, masks, totals, joins, synthetic recovery
  data/derived/        # redistributable analysis tables and coverage flags
  results/             # generated tables, figures and diagnostics
  manuscript/          # text and matching SI
```

Keep large/raw or restricted data in suitable archives/object storage with checksummed retrieval instructions, not indiscriminately in Git. Record DOI/version, download date, processing environment and all source-use restrictions. Ensure every plotted number comes from a named derived table; preserve failed quality checks and exclusions. Include a synthetic test where pure area change, pure density change and mixed change recover the known decomposition.

## 13. Decisions to approve before downloading large datasets

1. Adopt the nested two-aim design, not a global yes/no capital-decline claim.
2. Approve forest–cropland as the core and other assets as conditional modules.
3. Select provisional windows, frozen NFA edition, and ESA v7 pending pilot checks.
4. Approve prospective eligibility/quality rules and practical-change thresholds.
5. Agree that causal claims and calibration of ECOMOD q are not default objectives.
6. Require mixed, null and unresolved results to remain in the reporting plan.

**Recommended decision:** Proceed to a small preflight and preregistration, not a full global download. The limiting issues are not just integration: observation repeatability, change detectability, lineage independence and boundary compatibility are genuine go/no-go conditions.

## Source verification notes

Dataset specifications above were checked against provider/publication pages on 29 October 2026. This was a focused feasibility check, not a downloaded-data audit, full licence review or exhaustive search for the latest RAM release. Source IDs, roles and verification limits are recorded in `DATA_REQUIREMENTS_20261029.csv`. No empirical results have been generated for the proposed paper. The source-only C12 revision does not by itself supply the empirical foundation proposed here.

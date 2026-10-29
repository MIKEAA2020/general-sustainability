# Follow-up F04 — physical sample and support report

**Outcome: physical-sample screening advanced; the analytical forest sample is not yet finalized.**

This report is separate from the journal article. It documents what the next-step work established, what it did not establish, and the specific requirement preventing physical estimation.

## Completed in F04

1. **Pinned eight candidate boundary objects.** Full published geoBoundaries ADM0 TopoJSON files are retained losslessly, with full repository commits, original bytes/hashes, represented years, source attribution and licences. These are candidate territorial geometries, not certified account-matched forest boundaries.
2. **Computed geographic-domain intersections.** WGS84 polygon areas were intersected with the native biomass domain, 80 N to 60 S. A separate 1-degree geographic planning index records polygon intersections. Polygon and forest areas are not interchangeable.
3. **Constructed a territory/account crosswalk.** The 2015 account identifier inventory and explicit country notes identify overseas/island questions instead of equating a sovereign-state name with every account component's domain.
4. **Checked the forest-observation endpoint.** The examined CDS satellite-land-cover catalogue, download form and version constraints list 1992–2022 observations, not 2023. The exact source snapshots and hashes are retained. This is a gap for that candidate product, not a finding that no other fit-for-purpose forest observations exist.
5. **Retrieved bounded native observations.** One geometry-selected 256-by-256 native-grid window per country was frozen before retrieving AGB and AGB-SD at the same indices in 2015 and 2023: sixteen small responses, each below 0.7 MB. No global native-resolution raster was downloaded.
6. **Separated valid, zero and missing observations.** All eight selected windows have 65,536 polygon-centre-selected cells with in-range AGB and SD at both endpoints. Zero is counted separately, not relabelled as missing or as independently established nonforest. Exact response hashes and query URLs are recorded. The deterministic windows are not a national or forest probability sample.

## Consequential findings

### Canada: geographic domain truncation

Approximately **1.2363% of the selected Canadian polygon area** lies north of 80 N. The polygon reaches approximately 83.14 N. This percentage is **not** omitted forest area, biomass, or national valid-data coverage. The ecological content of omitted support remains unestablished. A forest mask must determine whether relevant support is omitted, and any restriction or alternative observation must be explicit rather than silently treating uncovered cells as zero.

### France and Australia: territorial definitions matter

The French candidate geometry is metropolitan-European, whereas the account workbook separately identifies French Guiana, Guadeloupe, Martinique, Réunion and Mayotte. Separate identifiers support checking a metropolitan interpretation; they do not certify identical territory conventions for every component, including marine accounts.

The Australian geometry includes outlying components over a wide longitude range. The lack of separate CXR, CCK, NFK and HMD identifiers in the 2015 inventory does not prove that the AUS account includes those territories in every component. Component-specific correspondence must be established.

Finland's island coverage, archipelagic Indonesia and the remaining source geometries likewise require explicit correspondence checks. None is automatically approved because an ISO code matches.

### Boundary geometry is not an independent forest mask

Represented boundary years range from 2016 to 2021; use of one geometry at both endpoints does not establish historical invariance. Five released TopoJSON representations have invalid polygon topology and require documented computational repair. Original quantization and positional/coverage limits remain. The planning database is useful for locating and bounding requests; it is not a native-resolution forest mask or authoritative territorial certification.

### The 2023 forest-support requirement is still open

The retained comparison is **2015–2023**. Substituting a 2022 land-cover map, assuming that tree cover equals forest land use, or defining forest as positive biomass would not satisfy the design. Compatible national observations or another documented product may supply the endpoint, but their forest definition, observation dates, lineage, positional support and validation must be assessed. Shared inputs with the biomass product must not be described as independent validation.

### A concrete alternative for the next forest-support acquisition

The current MapBiomas Brazil download page advertises Collection 11 annual 30 m land-cover/land-use maps for 1985–2025. HTTP metadata checks for its 2015 and 2023 GeoTIFF endpoints are recorded in `metadata/forest_observation_candidates_F04.json`. No raster body was downloaded or forest mask adopted. This is a concrete Brazil candidate for class-definition, lineage and validation review, not a solution for all eight countries.

An inspected 2026 global ensemble record explicitly uses temporal interpolation, weighted averaging and resampling; its nominal 2023 layer must not be mistaken for an independently observed endpoint. The inspected record is cropland rather than forest and was not adopted.

## Admission and exclusions

| Candidates | Account availability | Candidate boundary/probe records | Final physical admission |
|---|---|---|---|
| BRA, IDN, COD, CMR, CAN, FIN, FRA, AUS | All pass the retained account rules | All recorded | **All on hold; none admitted yet** |

No candidate is permanently excluded by F04. A hold means that required evidence remains incomplete, not that the country lacks usable data or that its assets declined. The detailed reasons are in [physical_admission_F04.csv](data/support/physical_admission_F04.csv).

National physical stock changes, divergence prevalence, conversion associations and diagnostic performance **have not been estimated**. Valid endpoint values in local windows do not establish those outcomes.

## Next decisive work

1. Identify defensible **2015 and 2023 forest-support observations** for each candidate, including compatible country-specific sources where justified. Distinguish forest land use, woody cover, plantations and temporarily unstocked forest; document independent information versus shared product lineage.
2. Confirm account territories and choose a common terrestrial support; resolve overseas/island components and Canadian high-Arctic support without silently changing the target population.
3. Acquire complete bounded native coverage on that support, with land/water and forest fractions, observed zeros, missing cells and converted support kept distinct.
4. Only then finalize a versioned physical analytical sample and proceed to change-uncertainty/validation work before physical outcome estimation. If an interval or target domain must change, record the protocol departure before that inference.

The uncertainty model and independent change-reference work can be researched alongside support selection, but successful access is not a substitute for either.

## Inspect the evidence

- [Country geographic-domain support](data/support/country_domain_support.csv)
- [Geographic planning grid](data/support/geographic_planning_grid.csv)
- [Native endpoint coverage counts](data/support/native_probe_coverage.csv)
- [Common valid support in the local windows](data/support/native_probe_common_coverage.csv)
- [Frozen native probe plan](configs/native_probe_plan_F04.json)
- [Source register](metadata/physical_source_registry.json)
- [Working physical-support specification](protocol/PHYSICAL_SUPPORT_F04.md)
- [Boundary attribution and licences](metadata/BOUNDARY_LICENCES.md)

The native arrays were necessarily read for these support counts, and zero/missing distributions and single-year 2015 account forest-area/population values have been inspected. No pristine prospective-registration or blinded-outcome claim is made. Earlier F03, ECOMOD C17 and all preceding published revisions remain unchanged.

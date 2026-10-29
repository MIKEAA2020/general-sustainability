# F04 physical-support specification

Date: 2026-10-29. This is an external working specification, not an externally registered preregistration. It supplements the retained study design and does not change the primary interval, candidate countries, account criteria or planned substantive estimands.

## Scope and sequence

1. Freeze the eight full published geoBoundaries gbOpen ADM0 TopoJSON objects by full repository commit, byte count and SHA256. Retain provider metadata, represented years, original quantization and upstream licences. These are candidate territorial representations, not certified matches to every account component or historical legal boundary.
2. Decode all polygon rings, respecting reversed arcs and holes. Record source geometric validity and any computational `make_valid` repair. No computational repair certifies the accuracy or legal status of a boundary.
3. Compute polygon area and its intersection with the documented native CCI Biomass domain, 80 N to 60 S, using WGS84 area calculations. Polygon areas can include internal waters or jurisdictional water; they are not measured forest or terrestrial land areas. Report excluded polygon area separately without assuming it contains no forest or biomass.
4. Produce a 1-degree geographic index with polygon-intersection areas. This is a navigation/download-planning product, not a forest mask, national biomass weighting scheme or independent physical measurement. In particular, multiplying a coarse whole-cell biomass mean by a boundary fraction would impose unverified within-cell homogeneity.
5. Freeze one 256-by-256 native-grid rectangle per country around a representative point of its largest supported polygon. This deterministic geometry-only rule is not selected using biomass, forest cover, coverage or change signs. Do not move an unsuccessful or water-dominated probe to obtain a more favourable result. Native product spacing is approximately 1/1125 degree, not a globally constant ground distance. The rectangle can cross a coastline or boundary; report both the whole probe and polygon-centre-selected pixels.
6. Only after freezing that plan, retrieve AGB and AGB-SD arrays for the exact same rows and columns at 2015 and 2023 through bounded DAP queries. Each response must be at most 25,000,000 bytes. Record exact query URLs, payload hashes, byte counts and schema. No global native-resolution file is downloaded. Raw native payloads stay in an external cache and are not redistributed.
7. Count fill, zero and finite in-range observations separately; use the declared fill value and range rather than treating zero as missing. Record overlap of valid AGB and SD at both endpoints. Do not calculate density means, stocks, stock changes, account–asset signs, classification thresholds or performance from these probes. The probes are not a probability sample and cannot establish national coverage, forest eligibility or change precision.

## Territorial crosswalk and support selection

Use the account workbook's identifier inventory to identify separately tabulated territories, without treating ISO-code agreement as proof of boundary compatibility. Inspect named overseas/island components explicitly, including France and Australia, and distinguish the national boundary from marine account domains. A public ADM0 polygon is not a common boundary for all fishing-account components. Record unresolved territory mappings instead of approving them silently.

The CDS satellite-land-cover catalogue and its current retrieval form are examined for endpoint compatibility. A catalogue ending in 2022 is not evidence that a 2022 map measures 2023 or that all other sources lack a 2023 observation. Do not silently substitute endpoints, treat tree cover as forest land use, infer forest cover from nonzero AGB, or switch to the secondary interval. Country-specific forest observations remain admissible if definitions, dates, independence/lineage and validation can be justified and harmonized.

## Admission status

Physical analytical admission remains on hold until territorial correspondence, matched independently supported forest observations, complete-area coverage/missingness treatment and change-validation requirements are met. A frozen candidate-boundary database, geographic domain report or successful bounded request does not freeze the analytical forest sample. Unresolved requirements are not evidence of ecological decline, absence of data everywhere, or permanent scientific exclusion.

## Prior information and outcome access

The inherited prior-information disclosure remains applicable. Boundary geometry, national-account metadata, product documentation and catalogue availability have been inspected. The probe plan is written before the bounded biomass payloads are requested; software records its hash. F04 necessarily accesses native pixel values to count validity, zeros and missing observations, but performs no country physical-outcome calculation. Accordingly, this phase must not be described as never having read biomass values or as pristine blinded validation. Any later outcome inspection, mask choice or design departure must be recorded accurately before the relevant inference.

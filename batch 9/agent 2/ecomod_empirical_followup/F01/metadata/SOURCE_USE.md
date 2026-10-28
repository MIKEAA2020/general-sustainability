# Source attribution, use restrictions and evidence scope

## NEFBA Edition 2026, results and metadata v1.0

**Citation:** Lo, K., Basnet, N., Miller, E., Srikanthalingam, B., Foley, B., Van Berkum, J. L., Long, A. H., Toneva, P., Ermina, M., and Klinkenberg, C. (2026). *National Ecological Footprint and Biocapacity Accounts, Edition 2026 (1961–2025): Results and metadata, version 1.0.* Produced for Footprint Data Foundation by researchers at York University and the University of Iceland. Public data: https://footprint.info.yorku.ca/data/ ; provider: https://fodafo.org/data/ .

The workbook `readme` states **Creative Commons Attribution–ShareAlike 4.0 International**: https://creativecommons.org/licenses/by-sa/4.0/ . The NEFBA-derived availability tables (`data/derived/account_eligibility.csv`, `pilot_candidate_audit.csv`), account definitions and corresponding account summary/coverage outputs are distributed under that same licence. Changes: selected the 2015–2023 window; tested publication, completeness, numeric/nonnegative values and rounded component totals; joined source regions to a declared logistical candidate list. These are derived metadata/availability checks, not endorsed provider products or physical-stock conclusions. Attribution is retained. The complete raw workbook is not redistributed here; checksummed retrieval instructions are supplied.

Publication flags +++, ++ and + all publish the biocapacity/production fields used by this study. Their trade/consumption detail differs. They are not biomass measurement-precision ranks. The source sheet calls the actual column `flag`, while its definition table also uses the name `quality_flag`; the pipeline uses the actual header. NFA component areas are account-lineage inputs, not independent validation outcomes.

## ESA CCI Biomass v7.0

**Citation:** Santoro, M., and Cartus, O. (2026). *ESA Biomass Climate Change Initiative: Global datasets of forest above-ground biomass for 2005–2012 and 2015–2024, v7.0.* NERC EDS CEDA, 21 May 2026. https://doi.org/10.5285/6429d1aafe1e43b9b414e4a5a7f8b903 .

Acknowledge the **ESA Climate Change Initiative, Biomass CCI project, and the individual data providers**. Dataset terms: https://artefacts.ceda.ac.uk/licences/specific_licences/esacci_biomass_terms_and_conditions_v2.pdf . The terms allow use by any user for any purpose with attribution; they disclaim fitness/warranty and retain producer IPR. They encourage interaction and consideration of co-authorship where the data are a major component; no contact, authorship agreement or endorsement is claimed here.

Raw files are held only in the external cache. The v7 Product User Guide has a separate restrictive reproduction notice: the guide and its text/figures are **not redistributed**. The method audit records factual interpretations, URLs, exact hashes and targeted reading scope; it is not a copy of the guide. The provider example script was read for method provenance, not executed, modified, or republished. Its reuse licence must be checked before any later redistribution.

The 0.5° aggregate contains per-grid-cell-area biomass averages. Its `agb_sd` layer must be interpreted using the aggregate-method documentation, not automatically as independent native-pixel standard deviations. The guide's geographic validity and source masks take precedence over an array's global coordinate extent. No 50 km-resolution product can support invented 100 m transitions, precise small-country boundaries or local conversion attribution.

Quality-flag semantics were recovered from the provider's example code, not from the incomplete NetCDF attributes. The labels do not become independent truth merely because the code calls some changes significant. The example computes a change SD without a temporal covariance term and uses endpoint-derived decision operations, a growth-limit rule and spatial filtering. Those operations must not be copied as independently validated scientific thresholds. A flag of zero estimated biomass at both endpoints does not by itself prove the absence of forest.

## Evidence depth and exclusions

The CEDA/ESA catalogue, public account page and source-file headers were checked directly. The Product User Guide was read in targeted portions (sections 2.3, 4–6 and related metadata/aggregation passages), not fully audited cover to cover. Data-use terms were read. The provider code's input, variance and flag/filter logic was inspected, not executed. Product validation and detailed uncertainty reports were located on the documentation page but not downloaded/read in this stage; they remain next-stage requirements.

No inherited archive data are repurposed as new ecological observations. The earlier literature review informs the study framing; it is not exhaustive novelty or publication-ethics clearance.

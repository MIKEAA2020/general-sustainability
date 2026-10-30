# Access and evidence workarounds — F16_A01

Only genuinely provider-held inputs are left for provider follow-up. All public files needed for the modules in this package were retrieved by the agent; the user is not asked to fetch them.

## Retrieved and used

### Cameroon

- Official 149-page revised national forest reference level: `https://redd.unfccc.int/media/cmr_nrf_zero_final_20janvier2026_f.pdf?download=1`
- SHA-256: `5436e1c0c4af723ff4025b830223470534a5b34248a152d86ecbafba74ced3d4`.
- Used: Table 9 (PDF p.31), Table 31 (pp.86–87) and Table 37 (pp.140–141). Coordinate-based annual extraction is checked for all 21 years; Table 31 decimals round to every Table 37 whole-tCO₂e Total REDD+ value.
- Sufficiency decision: the aggregate PDF is sufficient for the completed descriptive reported-area/flux module. It is not represented as raw CEO data, independent reproduction or calibrated AGB change.

### Australia

- NIR2023 Volume 1, official UNFCCC document 647190: Table 6.2.2 (PDF p.316) and the carry-forward statement (p.302). SHA-256 `76fe8fdadb01c01995a3ada41e8a8c8ef3d3873b43c33a046a8cfe43e52a1074`.
- NIR2023 Volume 2, official UNFCCC document 647191: Annex Tables A5.6.12.1a/b (PDF pp.352–354). SHA-256 `e7d348103186dc59c18c236ff6d638887acdd90c551787712f3f53bd70ef3811`.
- ABARES Indicator 1.1a.iv workbook: direct binary routes failed, but the complete five-sheet public workbook was retrieved through Jina, including every annual cell used here. Extraction SHA-256 `49dd32d7bdc04c286dcc11e99910093e1eb025b9c140c9455117862ce405db3d`. The original URL and extraction identity are pinned; no value is inferred from a chart image.
- Forests of Australia (2023) attribute CSV, metadata and lookup tables were retrieved directly from data.gov.au. Attribute SHA-256 `ff44e7b815ac1a2f4ca7f181ef84e6664acfddc3c909fb71722f94660898743c`. The lookup table explicitly states that 100-m-cell `COUNT` equals hectares; metadata gives 30 June 2021 latest-information currency.
- The ABARES-adjusted series is documented as NIR2021 area changes applied to the ABARES 133.6-Mha multiple-lines-of-evidence total. It is not conflated with the unadjusted NIR stock.

Full URLs, byte counts and hashes are in `metadata/source_provenance_F16.json`.

## Large CRT archive: selective access without waste

UNFCCC document 647189 links the 130,761,002-byte `Common Reporting Tables 1990-2023.zip`. A custom HTTP-range ZIP reader used four range requests and only 6,160 downloaded bytes to list 34 annual XLSX members. The 2023 member is 645,066 bytes. No wholesale archive was downloaded. No member was extracted because official NIR Tables 6.2.2 and A5.6.12.1a/b already supplied every annual physical value required for this module; redundant CRT retrieval would not add an AGB endpoint or uncertainty calibration. The range reader and member listing remain in the non-durable source cache, while the access accounting is preserved in source provenance.

## Provider-held inputs still needed for stronger analyses

These items do **not** block the completed reported-aggregate module. They remain necessary for independent reproduction, a calibrated 2023 endpoint and a defensible joint uncertainty analysis:

- `CAM_FRL_FINALE_CalculationTool_02Jan2026`
- `CAM_FRL_CalculationTool_MonteCarlo_02jan2026`
- underlying CEO/raw-count export and complete annual 2000–2023 input sheets, including Monte-Carlo draws/covariances or sufficient design information.

Provider route: MINEPDED/ONACC (`contacts@minepded.gov.cm`) or the Coalition for Rainforest Nations (`info@rainforestcoalition.org`). The PDF's anonymous SharePoint DOCX link redirects to Microsoft sign-in; repeated anonymous retrieval is not a workaround. The provider request should name the two workbooks and raw annual inputs explicitly. Do not ask the user for the already acquired public PDF.

The F15 access register for Brazil/Indonesia reference-design inputs, Finnish biomass-design variance information and Canada's uncertainty implementation remains applicable to their stronger respective analyses. Those provider/design gaps are not used as reasons to pause the completed Cameroon/Australia modules, and no new public-source gap is asserted without a corresponding retrieval attempt.

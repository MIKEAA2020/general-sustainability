# A016 Evaluation — Who Holds Adaptive Capacity

## Source identity

- Source: `uploads/paper3_final.md`
- SHA-256: `b15afc1e5ddb40fea6d29713f99f23bd3bca4c70d5c23d33e89c299640d19fde`
- Submitted title: *Who Holds Adaptive Capacity*

## Overall verdict

**Substantively useful normative/distributive redesign, but not integration-ready as an empirical article.** The typed split, refusal of a master scalar, componentwise-margin rule, anti-domination residue, and named cod-community research object align with the canonical architecture. The empirical population, tables, floors, and poverty vintage need correction and reproducible extraction.

## Verified or supported items

1. Statistics Canada tables 38-10-0167-01 and 38-10-0168-01 exist and report CSD-level resource-industry income/employment measures for 2016 and 2021.
2. The Statistics Canada method defines resource-based communities as the top 2% of Canadian CSDs by proportion of employment income from the resource industry; the fishing thresholds are 25.1% in 2016 and 21.4% in 2021.
3. PIP and the global MPI are legitimate external measurement instruments, but neither exhausts the paper’s normative B6 object.
4. Reporting typed component margins rather than a compensatory master score is consistent with the accepted redesign.

## Live defects and required corrections

### A016-L1 — Current poverty-line vintage

As of June 2025, the World Bank’s primary international poverty line is $3.00/day in 2021 PPP. The former $2.15/day 2017-PPP line remains available only for historically vintage-consistent analysis. The manuscript must either use $3.00/2021 PPP or explicitly freeze a historical 2017-PPP query and explain why.

### A016-L2 — Population mismatch

The declared group `G` is registered inshore harvesters/licence holders in 2J3KL, while the displayed data concern all residents/employment income in selected fishing-dependent CSDs and include aquaculture, fishing, and seafood processing under Statistics Canada’s industry definition. Redefine `G` as CSD populations or obtain licence-holder micro/administrative data. Do not treat the CSD table as a licence-holder panel.

### A016-L3 — Geography mismatch

Newfoundland and Labrador fishing-dependent CSDs are not automatically the 2J3KL impact population. Establish a geographic crosswalk from CSDs to 2J3KL dependence and distinguish Labrador, northeast-coast, south-coast, aquaculture, processing, and multispecies fisheries.

### A016-L4 — Unarchived extraction

The claims of 43 CSDs, means of 32.2% and 25.6%, and the top-ten values require a locked query, CSV extract, filters, missing-value rules, geography crosswalk, and reproduction code. They are plausible but not verified from the article alone.

### A016-L5 — Internal contradiction

Section 5 displays a computed table while the limitations say “No Newfoundland income or licence table is computed.” Correct this to distinguish the displayed CSD-income extraction from the missing licence/participation/recruitment panel.

### A016-L6 — Floors and non-decline

“Non-decline” is a normative rule, not automatically an empirically justified floor. Define baseline, cohort/population, inflation/PPP treatment, uncertainty, attrition, acceptable variation, authority, and treatment of structural diversification.

### A016-L7 — Smooth conjunction wording

For dimensionless margins, finite LogSumExp is a conservative inner certificate with a quantified approximation gap, not simply “compensation reintroduced.” The exact conjunction is the minimum/essential infimum; smoothness may be useful when conservatism is declared.

### A016-L8 — Causal conjecture

Biomass recovery coinciding with deteriorating community indicators is not by itself a causal effect of fisheries governance. Predefine comparison populations, confounders, migration, shellfish substitution, transfers, policy timing, and a causal or explicitly descriptive design.

### A016-L9 — Terminology and publication style

Replace internal phrases such as “this program,” “Paper 5,” “killed,” and dated conversational references. Present the norm, measurement scope, and evidence directly.

## Integration and publication decision

- Integrate the typed B6 split, anti-domination residue, and measurement cautions into the distributive module/flagship.
- Treat the cod-community case as a bridge to A014/A011 after a reproducible geographic and administrative-data pipeline exists.
- No standalone publication at present. Reassess only if the human-series panel and independent empirical result are completed.

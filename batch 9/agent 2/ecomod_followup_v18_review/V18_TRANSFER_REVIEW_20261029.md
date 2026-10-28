# V18 manuscript: genuine additions to the empirical ECOMOD follow-up

**Date:** 29 October 2026  
**Verdict:** One worthwhile core refinement; one conditional forest-mechanism extension. Most of V18 should not be imported. Neither recommendation is a claim of globally novel methodology or a guarantee against duplicate publication.

## 1. Source and review scope

Reviewed the repository file [`uploads/manuscript_v18_dehedged.txt`](https://github.com/MIKEAA2020/general-sustainability/blob/47c99d772d46ec4165b5235e15c4923487ed3962/uploads/manuscript_v18_dehedged.txt), titled *Scarcity-Driven Capital Liquidation and Delay-Amplified Instability: A Vector-Valued Flow-Balance Framework for Sustainability*.

- Repository snapshot: `47c99d772d46ec4165b5235e15c4923487ed3962`.
- Git blob: `e5ff1364cb383126467e74280bd12f0823a10df7`.
- SHA-256: `15b6da19449d40ae9c5233dc8110e44b4f604f1673fd34a1671ab45b50d99acd`.
- Size: 606,247 bytes; approximately 72,580 whitespace-delimited words. Although named `.txt`, the file contains TeX source.

The file was retrieved from the repository: it was not present among the local uploaded attachments. I screened its structure and inspected the passages relevant to spatial aggregation, stock/service mapping, gross/net fluxes, depletion diagnostics, two liquidation channels, material/functional states, empirical examples, proxy construction and Appendix J. This is a targeted transfer review, not a full line-by-line proof, numerical, citation, data or publication-status audit.

The comparison baseline comprises the [implementation plan](../ecomod_followup_plan/FOLLOWUP_IMPLEMENTATION_PLAN_20261029.md) and the [previous companion-paper review](../ecomod_followup_paper_review/RECOMMENDATIONS_20261029.md). No source manuscript or existing plan has been edited.

## 2. What is actually additional?

| V18 idea | Already covered? | Decision |
|---|---|---|
| Component-level losses despite improving aggregate accounts | Central question of the plan | Not another contribution |
| Typed units, explicit boundaries, material versus functional states | Plan §§5–10; previous review | Implementation discipline, not a new framework section |
| Spatial heterogeneity and local losses hidden within an asset total | Spatial distributions and scale sensitivity are already required, but a specific within-asset cancellation test is not | **Sharpen into a new empirical analysis** |
| Standing-stock removal versus suppressed replenishment | The plan lists disturbance and regrowth, but does not directly measure recruitment/replacement failure | **Conditional empirical extension** |
| Stock state versus current rate of change | Prior review's reference-relative path/recovery analysis already addresses much of this | Tighten interpretation; do not count again |
| Diagnostic sensitivity/power and signal detectability | Previous review already recommends operating-characteristic calibration | Do not add a second power workstream |
| Supporting-pool drawdown behind maintained output | Conceptually different, but current core inputs do not identify it | Defer unless a matched, independently observed support budget exists |
| Depletion horizons, stress indices, response-delay thresholds, nine-state scaffold | Neither required nor identified for the proposed core study | Reject as imports into this follow-up |

## 3. Recommended core refinement: measure within-asset spatial cancellation

**V18 source:** “Spatial Heterogeneity and the Vector Projection,” source lines 117–127. The motivating point is that a mean or total can conceal local losses and differences in spatial configuration.

### New empirical question

> Among observations with improving accounts and little or no national biomass decline, how much resolved local biomass loss is offset by gains elsewhere—and in which predefined ecological strata does that loss occur?

This is different from the existing cross-category question, “Do crop-account gains coexist with forest-asset loss?” It asks whether the **forest total itself** hides a redistribution of losses and gains. It is also different from the previous review's temporal drawdown analysis: losses and gains here differ across places, not merely across dates.

### Concrete implementation

Use a fixed geographic domain and a predeclared set of comparable spatial units. For local biomass-stock changes `d_j`, all measured in the same mass units:

- `G = sum_j max(d_j, 0)`;
- `L = sum_j max(-d_j, 0)`;
- `net change = G - L`.

Report G and L alongside net change, not only a net national trend. A large L alongside a nonnegative net change identifies spatial offsetting at that declared resolution. An optional cancellation summary is `1 - abs(G-L)/(G+L)` when `G+L > 0`; it is a descriptive mass-change statistic, not a sustainability index, and is undefined when there is no local change.

These are **positive and negative local net stock changes**, not gross physiological growth, harvest, recruitment or mortality fluxes. Two-date maps cannot identify those underlying fluxes or detect every intervening disturbance.

Stratify losses and gains using independently supported forest type and land-transition information—e.g., natural versus planted forest, conversion versus stable land use, and relevant ecological regions. Test whether gains and losses occur in different strata. Do not assume that a tonne gained in one stratum replaces the habitat or other services of a tonne lost elsewhere.

### Why this is non-decorative

It changes the assessment of cases that otherwise look like “account improvement / no net asset loss.” The added result is the prevalence, magnitude and location of concealed local loss in those cases—not simply another map or a citation to Jensen's inequality.

**Primary new output:** A nested comparison of account change, national biomass change, and within-country losses/gains by predeclared strata. Pre-specify its comparison with net-only reporting, rather than selecting visually dramatic countries after inspection.

### Evidence and uncertainty gates

- Preserve the plan's fixed-domain versus forest-class distinction. A pixel leaving a forest mask is not automatically zero biomass.
- Define spatial grain before examining outcomes and report supported coarser-grain sensitivities. Do not treat nominal map spacing as change-detection precision.
- Positive-part operations generate apparent G and L from noise even when true change is zero. Calibrate this analysis inside the **already recommended simulation pipeline**, retaining temporal and spatial error dependence. A bootstrap that preserves the same uncorrected map bias is not a cure.
- Resolve change at defensible spatial support; do not label every negative pixel estimate a real local loss. If only larger regions have adequate precision, use those regions and state the resulting limit on local detection.
- Do not count all raster cells as independent replicates or multiply country frequencies across overlapping intervals.

### Duplication boundary

Cite V18 for its relevant conceptual motivation, alongside appropriate external spatial-accounting literature. Do not reproduce its logistic variance identity, forest thought experiment, theoretical diagrams or dynamical scaffold as new results. The stock-change identities above are elementary bookkeeping, not a new theorem.

**Important limit:** V18's logistic identity assumes a particular response law and common parameters; its Ricker extension has a curvature-dependent correction. Biomass variance is not a universal indicator of degraded regeneration. Do not convert observed spatial variance into lost sustainable yield without an independently supported ecological response model. Nor does spatial offsetting itself prove damage to every ecosystem service.

**Recommendation:** Add this as a focused extension of the existing spatial analysis, not as a separate theory chapter or a claim that spatial masking has never been studied.

## 4. Conditional extension: distinguish standing stock from replenishment capacity

**V18 source:** “Extending the Core: Two Liquidation Channels” and the resource assignments, lines 1079–1155; explicit juvenile compartments in Appendix J, lines 2113–2170.

The useful question is not whether to fit V18's channel parameter. It is:

> Can standing biomass remain stable or rise while independently observed recruitment or establishment deteriorates?

### What would genuinely change

In an eligible forest subset, add repeated field-demographic evidence: established recruit/sapling entry and survival, adult mortality, species/size classes, disturbance history and management where available. Keep demographic indicators in their proper units; counts of saplings cannot be subtracted from tonnes of adult biomass without a validated conversion.

Estimate recruitment/establishment changes against a predeclared, ecologically defensible comparator, with uncertainty. Examine whether biomass-only and biomass-plus-demography reporting give different descriptions. A one-time low seedling count is not automatically recruitment failure: census thresholds, life history, episodic recruitment, stand age and management matter.

**New result if supported:** Direct evidence of divergence between standing biomass and measured replenishment processes. That would strengthen interpretation of what an improving stock/account record does—and does not—establish about future productive capacity.

### Non-negotiable gate

Repeated demographic observations or a separately validated process measure are required. Canopy greening, a single forest-age map, biomass change, or time since disturbance alone does not establish recruitment. Existing plot records may be reusable as data, but their provenance, previous analyses and calibration overlap must be disclosed.

If those observations are unavailable, report “regeneration not assessed” and omit the extension. Do not delay the core paper or manufacture a recruitment index to fill the gap.

### Duplication boundary

Do not reuse V18's illustrative channel assignments, excursion troughs, simulation figures or local-stability claims as empirical findings. Do not estimate its channel parameter from aggregate biomass and account series alone. Actual recruitment suppression, harvest of existing seeds/juveniles, and adult removal have different physical meanings; they should not be collapsed into a universal “liquidation” label.

A recruitment difference is not, by itself, an identified causal effect of extraction, proof of future collapse, or a measured sustainable-yield gap. The new contribution would be the demographic observation and comparison—not a re-presentation of V18's mechanism.

**Recommendation:** Optional nested forest study only if suitable repeated records already exist or are realistically accessible.

## 5. Other tempting imports: useful cautions, not recommended additions

### Supporting-pool drawdown and output maintained by subsidies

V18 distinguishes aggregate compensation from output sustained while a supporting pool declines. This is a genuinely different empirical mechanism, but it is not identified by observing crop output rise while forest biomass falls.

To test it, a matched production landscape would need independent output observations and a defensible supporting-pool budget—e.g., groundwater storage change, withdrawals, recharge, return flows and boundary exchanges. Rising irrigation or fertilizer use alone does not establish depletion; replenished inputs may maintain stocks. An NFA account is not automatically observed delivered output or measured sustainable yield.

The existing core inventory does not provide that complete budget. Do not add a general support-dependence fraction or an “inflated sustainable yield” result. A future tightly bounded case could be worthwhile, but it would be additional research, not a free enhancement supplied by V18's equations.

### State, trend and gross throughput

Retain the safeguards that stable or rising stocks may remain below a declared historical reference, and that gross extraction is not net depletion. Conversely, a current zero decline rate is not evidence of future safety. These clarify the existing path/reference and stock–flow work; they are not separate new contributions.

### Depletion horizons and stress indices

Do not import V18's ADHs, service-specific overshoot days, composite stress score or published example tables. A stock/flow ratio is not a validated forecast; an anomaly-relative historical minimum is not necessarily an ecological failure threshold. Gross uptake can be positive in a balanced system. A net-rate extrapolation remains conditional on continuing that rate, and an infinite current-rate horizon does not guarantee future safety. Recovery-time ratios additionally need calibrated recovery and failure definitions.

These requirements would expand the paper into forecasting or risk assessment without resolving its current measurement question.

## 6. Do not use V18's proxy recipes to manufacture asset coverage

The “Unobserved Proxies” section and Appendix E (lines 1575–1582 and 1847–1878) propose constructions that cannot simply be adopted as validated observations:

- **Soil microbial function:** Static SOC/pH/clay predictions do not create an annual microbial-function series. A regression target based on microbial diversity does not, without validation, establish carbon-cycling rates.
- **Pollinator function:** NDVI, hive counts and pollinator-dependent crop area mix environmental signals, managed-bee statistics and crop exposure/demand. Increasing crop area can mechanically increase the proposed index without increased pollination effectiveness. This is especially problematic in a study already examining crop expansion.
- **Freshwater-lens integrity:** A terrestrial-water-storage anomaly is not an isolated coastal freshwater-lens volume. As written, Appendix E integrates a storage anomaly alongside recharge/extraction rates without supplying the derivative and unit reconciliation needed for that balance. Independent separation of storage components, boundary support and validation would be essential.

These are reasons to **reject the recipes as ready-to-use measurements**, not a completed audit of their underlying datasets. Follow the existing plan's “not assessed” category rather than obtain superficial four-asset completeness through unvalidated proxies.

## 7. Publication and implementation decision

**Recommended change to the analysis plan:** Make within-asset spatial cancellation an explicit question, estimand and generated output, sharing the existing data extraction and diagnostic-calibration work. Add demographic replenishment only behind a repeated-observation gate. Do not otherwise broaden the forest–cropland core.

No new empirical analysis was performed for this review. The plan and manuscripts remain unchanged; these are recommendations for approval, not an implemented protocol amendment.

For publication:

1. Attribute adapted ideas and identify V18's actual draft/submission/publication status before citing it; the filename alone does not establish that status.
2. Distinguish existing conceptual and mathematical contributions from the follow-up's new data and analyses. New wording, a new title or a citation does not cure substantive duplication.
3. Do not reissue V18's empirical groundwater/phosphate/fisheries demonstrations, numerical thresholds, model variants or figures as the follow-up's results. Shared raw data are not automatically prohibited, but reuse needs disclosure and a substantively different question and analysis.
4. Make the new spatial or demographic results carry the contribution. If those additions yield little reliable information beyond the existing plan, omit them rather than preserve them for conceptual completeness.
5. Check external prior art and target-journal policies. Spatial cancellation, forest demography and stock–flow accounting are established research areas; this review does not establish global novelty or guarantee editorial acceptability.

**Bottom line:** V18 lends a practical question about **where losses are hidden within apparently stable asset totals**, and a data-gated question about **whether the standing stock is still being replenished**. Its large theoretical architecture, diagnostic indices and proxy recipes should not be carried into this follow-up.

# What the latest repository papers can genuinely add to the ECOMOD empirical follow-up

**Review date:** 29 October 2026  
**Status:** Targeted contribution/overlap review and proposed analyses; not completed empirical research, a full proof audit, an external novelty search, or a publication-ethics clearance.  
**Baseline:** The completed [implementation plan](../ecomod_followup_plan/FOLLOWUP_IMPLEMENTATION_PLAN_20261029.md), published at repository commit `1c51153eaa7edfffa661648bb7505e1d0f50f903`. No manuscript or implementation-plan text has been changed.

## 1. Verdict

**Yes—but borrow a small number of methodological ideas, not the companion papers’ scientific contributions.** I recommend two additions to the forest–cropland core and one conditional extension:

1. **Calibrate the masking diagnostic’s operating characteristics.** Establish what the proposed measurement pipeline can distinguish, including false masking caused by measurement or classification artefacts.
2. **Compare endpoint improvement with the observed asset path.** Measure losses and recoveries hidden by the choice of start and end dates.
3. **Conditionally, test which additional observations actually reduce account-only ambiguity.** Go beyond counting disagreements to evaluating a small, predeclared set of reporting additions.

These would produce new empirical or study-specific simulation results. Merely adding a theory section, citing the family, reproducing its examples, or renaming the existing dashboard would not.

**Do not advertise unit typing, provenance tables, the existing account/asset disagreement count, or the existing extent–density decomposition as fresh additions:** the implementation plan already contains them. Improve their implementation where necessary, but do not count them again as new scientific contributions.

## 2. What “latest” means in this review

The search covered the recursive trees of **15 branches and 3 tags**, rather than assuming `main` contained every latest edition. Highest-numbered files were treated as edition candidates, not automatically as author-designated canonical or published versions. The review read abstracts, contribution statements and section structures across the relevant families, and inspected the particular methods, limitations and overlap passages underlying the recommendations. It did not verify every proof, SI, executable or PDF.

Important edition findings:

- **Paper06 v77** is on `agent/p06-ecomod-c11-local-draft-20261028`, not the reviewed `main` snapshot. Its README identifies an audit-repair package with October 28 submission-text cleanup, not a DOI deposit or publication. Its revised scope matters: the plan/weight gap can be static; paths are an application setting, not a necessary cause of that gap.
- **Paper3 v54** is also restored on that branch. Its README describes a citation-only derivative of v53. The separate October 28 contact-link repair is not a new substantive edition. **Paper10 v55**, in the renamed depletion-ledger family, was checked separately; version numbers across renamed families are not one universal release sequence.
- **Paper4 v42**, **Paper07 v54**, and the integrated **Paper08 v51** were checked rather than relying only on older delay/review editions.
- The applied/intervention screen included **Paper09 v44, Paper09b v6, Paper10b v4, E2 v29, E3 v26 and E4 v16**. Canonical-looking E2/E4 source copies were checked against archived originals and were byte-identical at the pinned commit.
- Other screened sources included **Paper01 v73, Paper02 v16, Paper03 v23, Paper04 v20, Paper05 v20, Paper11 v68 and Paper11c v5**. Earlier main copies were used as comparators where newer branch editions existed.

The accompanying `SOURCE_INVENTORY_20261029.json` records exact paths, commits, hashes and review depth. Repository filenames and READMEs establish the edition evidence used here; they do not establish every paper’s external publication or submission status.

## 3. Addition A — calibrate the masking diagnostic, not just the uncertainty bars

**Source:** Paper11 v68, “What the test could have seen.” Its cod analysis simulates specified truths and measures the test’s power and false retention; it explicitly distinguishes that exercise from the aquifer’s realized-flux retrospective diagnostic.

### What would change in the follow-up

The plan already requires uncertainty propagation, practical-change thresholds and a detectability gate. Add a **locked, study-specific simulation experiment that runs the entire proposed masking pipeline**, including country eligibility, account-change screening, biomass estimation, land-transition classification and the final claim level.

Use a small set of declared scenarios:

- no true physical loss, but correlated spatial/temporal measurement error;
- genuine conversion-linked biomass loss combined with increasing accounts;
- genuine biomass loss from another process alongside an unrelated account improvement;
- apparent divergence generated by mask, coverage or vintage changes rather than physical loss.

Use pilot-supported error magnitudes where available and sensitivity ranges where they are not. Preserve shared calibration errors and spatial/temporal dependence; do not simulate millions of independent pixels and mistake them for independent evidence. Do not invent probabilistic NFA errors when only revision scenarios are available.

**New outputs:** false-divergence rate, sensitivity by loss magnitude, unresolved rate, interval coverage, and the rate at which non-conversion loss is wrongly classified as conversion-linked. Compare the proposed rule with a simple endpoint-sign comparator on the same simulated records. Freeze thresholds and retention criteria before scoring the evaluation simulations; if pilot tuning is necessary, separate tuning from evaluation.

**Scientific value:** A small or null empirical masking estimate can then be interpreted against what the design could have detected. Conversely, a strong-looking pattern that the pipeline produces under artefact scenarios cannot be sold as evidence of physical depletion.

**Additional requirement/gate:** A usable pilot observation-error and transition-error model. If its inputs are only scenarios, label the outputs scenario-conditional—not field-calibrated probabilities or universal power claims.

**Duplication boundary:** Borrow the operating-characteristic discipline, not Paper11’s cod/aquifer models, simulated truths, numerical results, benchmark tables or retention verdicts. The contribution is the evaluation of a different measurement problem on newly specified scenarios and data.

**Recommendation:** Include in the core. This makes the plan’s existing precision gate operational rather than rhetorical.

## 4. Addition B — endpoint-versus-path asset diagnostics

**Source:** Paper06 v77, “Design tests for composite indicators,” especially its explicit distinction between path and endpoint checks.

### What would change in the follow-up

The provisional main analysis compares interval changes, especially 2015–2023. Add a compact annual-path analysis wherever comparable observations genuinely support one:

- endpoint biomass change;
- largest observed peak-to-later-trough proportional loss;
- loss relative to the declared starting reference;
- whether, and when observed, the asset returns above that reference within the study window.

For a positive stock series, the observed maximum drawdown is

`max over observed s <= t of (X_s - X_t) / X_s`.

Propagate observation dependence into drawdown uncertainty. Searching over many noisy dates creates extreme-value selection effects; use simultaneous uncertainty or the calibrated simulation pipeline rather than treating the lowest map estimate as a precisely known trough.

**New output:** an endpoint/path comparison identifying cases that look stable or improved at the endpoint but experienced a resolved intervening loss. All directions of change remain eligible; do not select only dramatic recovered cases.

**Scientific value:** It tests an actual assessment consequence of date selection. It can reveal damage-and-recovery histories that a net-change comparison misses, without adding a new dynamical model.

**Additional requirement/gate:** Sufficiently comparable repeated estimates and documented temporal resolution. Annual observations cannot certify a continuously safe path. “No observed crossing” is not “no crossing.” Use an externally justified ecological floor only where one exists; otherwise report reference-relative loss and recovery, not safety or ecological threshold breach. A detected recovery is not a guarantee of permanent recovery.

**Duplication boundary:** This is not an empirical test of Paper06’s plan/weight quantifier theorem. A historical trajectory supplies neither alternative action menus nor common-plan feasibility. Do not reuse its rational witness, reserve threshold, CES results, figures or synthetic cod illustration.

**Recommendation:** Include as a focused core analysis, with failure to meet temporal-comparability requirements an allowed reason to omit it.

## 5. Addition C — test the informational value of specific reporting additions

**Sources:** Paper01 v73, §5, observation-fibre criterion and its monitoring-design discussion; Paper11c v5’s monitoring-design analysis. The latter’s strongest results concern actions and institutions in a finite worked system, not empirical classification of forest change.

### What would change in the follow-up

The plan already asks whether an account-only improvement label coexists with physical loss. **Repeating that count with a theorem citation adds nothing.** The substantive extension is to ask:

> Among observations with comparable headline account changes, which small, predeclared additions materially reduce uncertainty about the physical outcome?

Define headline comparability before inspecting physical outcomes, using declared reporting precision or defensible tolerances. Account level, absolute change, proportional change and per-person change are different signals; do not silently substitute one for another. Opposing resolved asset trends within a tolerance group demonstrate ambiguity at that reporting resolution, not identical exact mathematical observation fibres.

Predeclare a short candidate set, for example:

1. headline account change alone;
2. headline plus forest extent change;
3. headline plus extent and mapped conversion information;
4. those observations plus an independently sourced structure/condition measure, if available.

Evaluate reduction in unresolved classifications or held-out prediction loss for the same declared physical outcome. Report uncertainty and missing-data costs. Where fitted mappings are used, separate fitting from evaluation by country/spatial blocks and avoid overlapping-window leakage. Do not include a biomass variable that algebraically determines the biomass outcome and advertise its near-perfect reconstruction as a discovery. Shared training and calibration sources must be disclosed.

**New output:** an evidence-based comparison of candidate reporting packages—possibly showing that a cheap addition suffices, or that none reliably resolves the ambiguity.

**Scientific value:** This can turn the follow-up from a disagreement inventory into a test of reporting design. It does not establish a uniquely minimal or universally sufficient monitoring system.

**Additional requirement/gate:** Enough independent eligible observations, relevant overlap in account signals, and a non-circular target/evaluation design. If country counts or validation support are too weak, retain descriptive ambiguity results and omit claims about incremental information. This is not a prerequisite for the core paper.

**Duplication boundary:** Cite the established criterion; do not re-prove it, reproduce the finite-system census or claim that observed heterogeneity proves an institution cannot act. No claims about policy obstruction, common-action feasibility or dynamic viability follow without action sets, constraints and dynamics.

**Recommendation:** Conditional extension, not a mandatory forecasting or machine-learning workstream.

## 6. Useful discipline that should not become another claimed contribution

**Paper3 v54 / Paper10 v55:** Typed stock–flow–boundary accounting can guide executable join checks: compatible units, dates, compartments, spatial support, source lineage and overlap. Report excluded or unresolved records if those checks change the empirical sample. But the plan already separates extent, stock, condition and flow and requires these crosswalks. No new closed-system theorem, conservation model or additional ledger paper is needed. Do not force partial ecological datasets into a closed mass balance when boundary fluxes are unobserved. Conservation of matter does not establish preservation of ecological function.

**Paper09b v6:** Its unresolved landings-to-SSB conversion and timing assignments reinforce a useful discipline: an exact unit conversion is not a validated ecological measurement map. Apply that discipline to the follow-up’s existing crosswalk and sensitivity work. Do not import the cod conversion thresholds, claim that AGB measures all natural capital, or treat an account residual as a physical stock merely because its arithmetic is exact.

**E3 v26 / Paper11 v68:** Keep retrospective information distinct from issuance-time information. The proposed study is retrospective; no forecast contribution should be manufactured by adding realized drivers to a fitted model. Validation independence also requires checking data lineage, already specified in the plan.

These are safeguards for implementation and interpretation, not reasons to add theory sections or multiply self-citations to elementary procedures.

## 7. Imports I would reject

- **Delay, Hopf, review-cadence or institutional-cycle modules:** Paper07 v54/Paper08 v51 explicitly limit numerical thresholds to their operators and parameterizations; their empirical screens do not identify a general governance oscillator. The follow-up has no identified governance feedback model. More clocks would not improve its present estimand.
- **Robust viability kernels, policy optimization and certified horizons:** Paper09/E2/E4/Paper10b answer action-, disturbance- and threshold-specific questions. Account–asset divergence is not evidence sufficient to answer them.
- **Belief recursions, minimax dual certificates, probabilistic-policy extensions or Lean formalization:** No demonstrated empirical bottleneck here requires those structures. Formal verification could check code statements but would not validate the ecological observation map.
- **Regenerative-support fractions or a general depletion/closure theorem:** Paper10’s support-feasibility correspondences require pathway, flow, boundary and capacity information that the current inventory does not identify. Aggregate output cannot supply these missing inputs.
- **Recycled cod/Edwards cases, synthetic witnesses or family-wide conceptual synthesis:** Those contributions already have a home. Repackaging them as the empirical follow-up’s principal result would create substantive overlap rather than resolve it.

## 8. Publication boundary and practical decision

The proposed paper must stand on **new matched observations, new pathway evidence, new study-specific diagnostics and genuinely new results**. Established companion methods can be cited and adapted transparently; their propositions and results must not become the follow-up’s principal claimed discoveries.

Before submission:

1. Maintain a contribution-overlap table covering ECOMOD C12, the companion papers and the follow-up: shared concepts, methods, data, analyses, figures and results. This review supplies the initial boundary, not a completed exhaustive overlap audit.
2. Identify any overlapping data explicitly. New data are not the sole test of originality, and new data alone do not justify duplicating the same substantive analysis. Here, the new measurement question and analyses must carry the paper.
3. Cite and disclose adapted methods and related manuscripts, including their actual submitted/draft/publication status. Give editors the related work when journal policy requires it.
4. Do not recycle prose, figures, numerical demonstrations or empirical results as new. Paraphrase and citation do not cure duplicate substantive publication. Historical ECOMOD/NFA findings can be brief, attributed motivation—not a second headline result.
5. Complete the external prior-art and journal-policy checks before making an originality or acceptability claim. This repository review cannot guarantee either.

**Lean recommendation:** Keep the existing forest–cropland scope. Add operating-characteristic calibration and an observed-path comparison; pursue reporting-package evaluation only if the pilot supports it. Do not add another theoretical framework or expand into policy certification.

A defensible prospective contribution statement is:

> Building on established distinctions between aggregate accounts and typed ecological constraints, this study tests boundary-matched account–asset divergence using new physical observations, evaluates sensitivity to intervening asset paths, and calibrates the diagnostic’s susceptibility to measurement artefacts. An optional extension evaluates whether specific additional observations reduce ambiguity in account-only reporting.

Use this only to describe planned work until those analyses exist. It is not a present claim of results or established novelty.

## 9. Principal pinned source links

- [Paper01 v73](https://github.com/MIKEAA2020/general-sustainability/blob/1c51153eaa7edfffa661648bb7505e1d0f50f903/arena%20agent%201/agent%20workspace/paper%202%20family/01_obstruction/paper01_obstruction_calculus_v73.tex).
- [Paper06 v77](https://github.com/MIKEAA2020/general-sustainability/blob/d2b5e2c9e60c6e2a26b04a199dbe34064508251e/companion_restorations_20261026/Paper06_v77/paper06_assessment_separation_v77.tex).
- [Paper06 v77 edition status](https://github.com/MIKEAA2020/general-sustainability/blob/d2b5e2c9e60c6e2a26b04a199dbe34064508251e/companion_restorations_20261026/Paper06_v77/README_v77.md).
- [Paper11 v68](https://github.com/MIKEAA2020/general-sustainability/blob/1c51153eaa7edfffa661648bb7505e1d0f50f903/arena%20agent%201/paper%20rewrites/latex/paper11_forecasting_baselines_v68.tex).
- [Paper11c v5](https://github.com/MIKEAA2020/general-sustainability/blob/1c51153eaa7edfffa661648bb7505e1d0f50f903/arena%20agent%201/paper%20rewrites/latex/paper11c_worked_systems_audit_v5.tex).
- [Paper3 v54](https://github.com/MIKEAA2020/general-sustainability/blob/d2b5e2c9e60c6e2a26b04a199dbe34064508251e/companion_restorations_20261026/Paper3_v54/paper3_material_ledgers_v54.tex).
- [Paper10 v55](https://github.com/MIKEAA2020/general-sustainability/blob/c867b66fc74c3e1c5f812ca42650879914b59650/arena%20agent%201/agent%20workspace/papers/paper10_depletion_ledgers_v55.tex).
- [Paper09b v6](https://github.com/MIKEAA2020/general-sustainability/blob/c867b66fc74c3e1c5f812ca42650879914b59650/arena%20agent%201/agent%20workspace/papers/paper09b_arv_certification_v6.tex).
- [Paper07 v54 abstract](https://github.com/MIKEAA2020/general-sustainability/blob/c867b66fc74c3e1c5f812ca42650879914b59650/arena%20agent%201/agent%20workspace/papers/paper07_sampled_governance_v54/parts/frontmatter.tex).
- [Paper08 v51](https://github.com/MIKEAA2020/general-sustainability/blob/c867b66fc74c3e1c5f812ca42650879914b59650/arena%20agent%201/agent%20workspace/papers/paper08_governance_delay_v51.tex).
- [E3 v26](https://github.com/MIKEAA2020/general-sustainability/blob/2bdf39ff1c13357a44c48b5ed7385c9945aff0b5/e3/paperE3_edwards_forecast_ladder_v26.tex).

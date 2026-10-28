# Which release material earns a place in the work?
## Separate recommendations for the empirical follow-up and ECOMOD
**29 October 2026 — actual release assets inspected; no manuscripts edited**

## 1. Verdict

**Yes, but the useful transfers are small, testable additions—not another theoretical framework.** The release archives contribute implementation details and negative examples that the earlier branch/tag review did not establish by inspecting the actual assets.

### Empirical follow-up: three worthwhile refinements

| Priority | Borrow | What must change in the work | Status relative to earlier recommendations |
|---|---|---|---|
| F1 | Information-availability tests, not just a provenance table | Test whether an apparent diagnostic increment survives removing future-derived or shared-outcome inputs; distinguish retrospective from real-time claims | A concrete refinement of existing independence/temporal-support requirements |
| F2 | Identical-support comparisons plus assessed-coverage reporting | Recompute every comparator on the same cases/years/weights; separate information gain from easier-case selection | Makes the existing reporting-package comparison operational |
| F3 | Algebraic-redundancy and physical-identification gates | Reject claims of new information from recoverable transformations; require independent evidence before interpreting extra states as physical mechanisms | A specific gate for the conditional modules, not a new index |

Keep the already recommended full-pipeline calibration. The releases sharpen it: compare decision rules and expose misspecification failures rather than copy one retention rule. This is **not a fourth newly discovered contribution**.

### ECOMOD: two substantive additions, one conditional experiment

| Priority | Borrow/adapt | New output required | Why it is not decorative |
|---|---|---|---|
| M1 | Quantitative compatible-state bounds | An interval for capital-land area under each observation package, with exact feasible witnesses | Converts “not identified” into “how much remains unresolved, and what observation resolves it?” |
| M2 | Integrated primitive-flow attribution | A closed numerical budget for the rise/fall in model biocapacity, including conversion, maintenance/retirement, restoration, quality and fast-yield changes | Measures whether the conversion term actually accounts for the reported change rather than merely having the right sign |
| M3, conditional | History-sensitive delay experiment | A declared delay × initial-history comparison outside the saturation-degenerate baseline | Tests whether the delay comparison is informative instead of adding more indistinguishable delay values |

**Do not add** the old scaffold, two-pool model, Hopf machinery, depletion horizons, proxy recipes, or another vector/viability chapter. Do not import the cod/aquifer numerical results as ECOMOD evidence. Most of the broad conceptual territory is already covered by the current drafts and earlier reviews.

## 2. What was actually checked

The GitHub Releases API returned **three releases, all marked prerelease**, with **eight downloadable assets**. These are not eight newly published papers. Release labels do not establish peer review or canonical status.

| Release | Published | Actual assets | Review disposition |
|---|---|---|---|
| [saved_on_pc](https://github.com/MIKEAA2020/general-sustainability/releases/tag/saved_on_pc) | 25 Oct 2026 | Five standalone PDFs: editorial/working v45 main texts, v45 SI, v44 main and a working main | Text extracted from all five; abstracts and targeted content compared with the later C12 working source. No layout audit |
| [edwards-framework-e1](https://github.com/MIKEAA2020/general-sustainability/releases/tag/edwards-framework-e1) | 12 Sep 2026 | `workspace-edwards-ecomod.sustainability.zip` and `workspace-edwards.framework.2nd.zip` | Both downloaded; research-document index screened; selected framework, application, protocol, model and audit passages inspected; selected score artifacts reaggregated |
| [compendium-v1.0](https://github.com/MIKEAA2020/general-sustainability/releases/tag/compendium-v1.0) | 4 Sep 2026 | `workspace-01a00d79-f20f-70dc-938a-8c93ce245a8c.zip` | Downloaded; V18/model/research-document index checked. Its broad scaffold does not supply a new ready-to-use enhancement beyond the V18 review |

All eight downloads matched the API asset byte counts and SHA-256 digests. The three ZIPs contain 3,452 file members in total, much of it repeated versions, software/runtime material or generated output. A filtered heading/index pass covered 512 research `.tex`/`.md` entries with 367 distinct byte hashes. **That is an indexing count, not 367 fully reviewed documents.** Runtime bundles, keys/certificates, generated binaries and unrelated material were not executed or republished. Only selected research text and score artifacts were examined more deeply; exact paths, hashes and depth are recorded in the source inventory.

### Baselines and version discipline

- **Follow-up:** the implementation plan and the completed companion, V18 and external-prior-art reviews, as present at main commit `c7d86ff40f9efcd1f1a2b8041ca82cefd971ea9d`.
- **ECOMOD:** the previously reviewed **C12 source-only working draft**, main/SI at `65c8464a3cf83d9aef525cb6695668898de18ac6`, used as an explicit comparison baseline. This is not a claim that C12 is the submitted or canonical manuscript. Submitted v76 sources remain untouched.
- A released ZIP is not the same object as its tag's repository tree. Assets are identified by asset ID and content hash; tag commit IDs and asset metadata are recorded separately.
- Archive filenames and the bundled README are imperfect edition guides. For example, the second workspace's README describes framework v4 while the archive actually contains v13. Highest version number is an inspection candidate, not authorial or external validation.
- These releases predate some branch editions already screened in the earlier review. Their value is recoverable evidence and concrete implementation lessons, **not a presumption that released means newer or better**.

Source IDs S01–S14 below refer to the inventory, not external literature. This is an internal transfer review; the external-grounding limits from the preceding review still apply.

## 3. Empirical follow-up: what to borrow

### F1. Turn information provenance into an exclusion test

**Source:** framework F1 v13, §3; Edwards Pass 2 protocol; E1 forecast-ladder v49 (S01/S03/S04).

The framework distinguishes inputs available at a forecast origin from inputs supplied afterwards. Pass 2 explicitly prohibits using future winter climate observations and excludes oracle drivers from retention. The useful transfer is not the table's appearance: it is a contrast that can overturn a claimed information gain.

**Required implementation:** for each proposed reporting package, record the observation period, release date, revision vintage, model training period, covariate time window and overlap with the validation target. Then test the relevant exclusion:

- remove inputs derived from the target or its calibration/reference data;
- for a temporal holdout, prevent multi-year feature windows and gap filling from crossing the split, or enlarge the embargo accordingly;
- where a real-time claim is made, remove observations and revisions not available at that decision date;
- compare the resulting diagnostic performance and assessed coverage on matched support.

An observation dated year *t* is not necessarily published or available at the end of *t*. The release's “dated at/before origin” shorthand therefore needs extending with actual availability/vintage evidence; do not simply copy it. A 2026-reconstructed map of 2015 can support a retrospective study without supporting a 2015 operational forecast.

**Non-decorative output:** an information-exclusion/availability contrast showing whether the additional reporting signal survives. If no operational claim is made, do not manufacture a forecast exercise: audit input independence and validation leakage within the retrospective question.

**Boundary:** this tightens the existing lineage and observation-support requirements; it is not a new conceptual contribution or permission to turn modelled annual soil/crop values into independent observations. An oracle diagnostic under one fitted model is not a universal bound on achievable prediction skill.

### F2. Compare packages on exactly the same support

**Source:** F1 v13, §2.2, explicitly recomputing the baseline on each module's origin set (S01).

A spatial or demographic package will often cover fewer—and easier—cases than the aggregate baseline. Comparing its error on those cases with the baseline's error across all cases confounds information gain with selection.

**Required implementation:** score every pair on the same eligible country/region, years, spatial support, weights, validation labels and decision criterion. Report both:
1. paired performance on common support; and
2. assessed coverage/abstention and the excluded population, without pretending that restricted support represents the original population.

Also retain a common-support comparison across all packages where feasible. If pairwise and global common supports differ, label both and do not rank packages by incomparable numbers.

A small synthetic check included in this package illustrates the problem: baseline errors of 1 and 10 give RMSE 7.106 over two cases. A candidate scored only on the easy case has RMSE 1, apparently a major gain; the baseline on that same case also has RMSE 1. The gain disappears. This is an illustration, not a repository empirical result.

**Non-decorative output:** a paired comparison and coverage frontier. A package earns an incremental-information claim only if the gain is not explained by support selection and survives the already required error/coverage calibration.

### F3. Require added observations or identified mechanisms—not just extra symbols

**Sources:** F1 v13, §2.3; A005 two-pool specialization test, §§1–5 (S01/S02).

The framework notes that a climatological-flux formulation can reduce algebraically to a simpler autoregression. The A005 test distinguishes improved fit/prediction, physical admissibility and independent identification of an extra pool. It reports a failed two-pool comparison rather than treating the added state as scientific progress.

A reaggregation of the archived A005 score table confirms **zero of four windows** beating the best baseline, even before worrying about the adopted 5% margin. This checks stored scores, not model fitting or registration history. The transfer is the exclusion discipline—not the aquifer model or its numerical threshold.

**Required implementation:** before promoting a new indicator or module, ask:
- Is its value deterministically recoverable from the lower package's existing observations? If so, it adds no observation information, although a different computational representation might improve a poorly implemented predictor.
- Does it add an independently observed quantity, or merely a latent fitted state/residual?
- Are physically interpreted parameters or stocks independently identified and admissible? Better prediction alone does not establish that interpretation.
- Does any claimed increment survive held-out comparison against the appropriate simpler implementation?

Use this especially for demographic replenishment, soil support and any supporting-pool extension. Keep “not needed for this reporting task,” “not identified by these observations,” and “ecological mechanism absent” as different conclusions.

**Caution from the source itself:** the A005 document's total-storage row describes cancellation in a sum of heads. Under unequal storage capacities, internal exchange cancels in the **capacity-weighted storage balance**, not generally in `H_f + H_s`. The included algebra check makes this explicit. Borrow the test structure, not every formula or assurance in an archived audit.

### Calibration: retain the earlier recommendation, but compare instruments

**Sources:** F1 §§4.3–4.5 and specification v4 (S01/S10).

Reaggregating stored retention flags reproduces the reported contrast: 97–98.5% specificity under the persistence null, but 68–76% retention under time-varying-productivity misspecification and 92.5–97.5% under observation-error-only misspecification. Those are conditional properties of that archived instrument and those scenarios—not expected error rates for the follow-up.

The framework also compares alternative rules and reports an information-criterion variant outperforming its adopted rule on selected simulation measures, with different decision semantics. Its unified 5% tie band includes a disclosed post-hoc application change. **Do not borrow its thresholds or advertise the entire unified procedure as prospectively registered.** The protocol's “locked” statements were inspected as documents, not independently verified as external preregistration.

For the follow-up, compare a small predeclared set of appropriate diagnostic rules and remove individual gates to show which ones drive false alarms, sensitivity and abstention. Use tuning/evaluation separation and independent truths/misspecification scenarios. The general calibration task is already endorsed; this is a concrete implementation refinement, not another contribution to count.

## 4. ECOMOD: where a substantive addition remains

### M1. Quantify the compatible capital-area interval

**Source/adaptation:** Paper2 v20, §4.1, exact observation fibres and the certainly-safe set (S05), applied to C12's existing Proposition 1(iii). The release supplies the classification discipline; the bounds below are a **new target-specific derivation in this review**, not a theorem copied from the archive.

C12 already proves non-identifiability and explains that `C = B − b_f A_f = Υ(q) A_c` identifies a product. Repeating the fibre theorem would be decorative. Computing the compatible interval and its reduction under additional observations would not.

For a fixed instantaneous model setting, suppose `b_f > u_+ ≥ u_- > 0`, `Υ(q) ∈ [u_-,u_+]`, `A_f,A_r ≥ 0`, `A_c ≥ a_min`, and total area `T`. With only exact `B`, the compatible area interval is

`a_min ≤ A_c ≤ min(T, B/u_-, (b_f T − B)/(b_f − u_+))`,

provided the interval is nonempty. For fixed `A_c`, possible B values range continuously from `u_- A_c` to `b_f(T−A_c)+u_+ A_c`, which gives the bounds. These are sharp under the stated static domain and attainable continuous yield range; they are not a claim of dynamic reachability from a shared initial history.

With an independent exact `A_f` and `C ≥ 0`, the sharper interval is

`max(a_min, C/u_+) ≤ A_c ≤ min(T−A_f, C/u_-)`.

An empty interval is an incompatibility flag, not a negative area to clip away. Parameter/observation uncertainty requires a declared **joint** compatible set; do not mislabel a structural interval as a confidence interval or assume unrelated marginal extremes can always occur together.

**Checked illustration using C12's representative parameter values:** `b_f=.85`, `T=2.5`, `a_min=.05`, `Υ ∈ [.05,.066]`, `B=.825`. Aggregate alone permits `A_c ∈ [.05,1.65816]` ha. With `C=.04` and independent `A_f=.923529` ha, the interval narrows to `[.606061,.800000]` ha. Both endpoints have explicit feasible allocations and q values in the check output. If q is independently known to be .9 under those same parameter assumptions, `A_c=.717360` ha.

The interval crosses an illustrative .7 ha cut. That number is **not** an ecological threshold, C12's enforced .05 ha floor, or an estimated forest limit. The example shows what different information packages can distinguish. Because Υ is symmetric in q around .5, knowing Υ need not identify q; none of this turns q into measured ecological health.

**Required manuscript output:** one short bound result and one interval/witness table or figure across declared model states. Keep ecological safety separate from instantaneous floor classification. This is the strongest small analytical enhancement to borrow.

**Follow-up transfer limit:** do not apply this model formula to NFA residuals or physical biomass without the missing mapping and independent parameters. The empirical study can adopt the compatible-set idea, not assume account tonnes/hectares interchangeability.

### M2. Close the full model budget over the reported interval

**Source/adaptation:** Paper3 v32, §§3.3–3.5, primitive-flux integration and envelopes (S06). C12 already conserves area and displays an instantaneous conversion identity. Neither fact quantifies how much of a reported aggregate change came from each active term.

For C12's stated equations, let `M=μA_r−η_fA_f`. The full identity, almost everywhere along a supported projected solution, is

`Ḃ = (b_f−Υ)u_c + b_f M + Υ R_rc + b_G,c G'_c(q) A_c q̇ + A_f ḃ_f`,

where

`ḃ_f = exp(−αD) Ṫ_b − α b_f Ḋ`.

All terms are in gha/year. Integrating each term gives a budget for `B(T)−B(0)`. It works with restoration, debt and technology active; under C12's restricted proposition it reduces to its existing identity. The package includes a synthetic instantaneous chain-rule check; **the integrated trajectory budget has not yet been computed**.

**Required manuscript output:** for the key existing runs, report the signed cumulative conversion, maintenance/retirement, restoration, quality and fast-yield contributions; their sum; observed model ΔB; and the numerical closure residual under step refinement. If technology and debt are split further, retain their exact contribution to `ḃ_f` rather than use a separate unexplained attribution index.

This answers a real question: did the positive conversion contribution dominate the net rise, or did other terms offset/amplify it? It also makes the difference between a pointwise sufficient condition and an interval result concrete. Closure should be checked at the projected-law switches and reported numerical tolerances.

**Boundary:** this is within-model bookkeeping, not causal attribution from observed national accounts. It does not identify gross harvest, ecological function, a sustainability threshold or a historical conversion effect. Do not add Paper3's material-stock/moiety machinery to a model whose conserved object is land area. The contribution would be the quantified budget, not an elementary integration theorem.

### M3. Test delay sensitivity where the delay can actually matter

**Sources:** the model-registration/operator distinctions in Paper4 v30 and Paper5 v37, plus the archived power-window closeout's lesson about transient placement (S07/S08/S09). Transfer the experimental discipline, not their characteristic equations, institutional operators or numerical thresholds.

C12 already recognizes that the baseline 20/40-year quality paths coincide because the imposed q cap binds before either delay takes effect. Repeating a wider delay sweep at the same saturated history adds no evidence.

For constant history `q(s)=q0`, `qmax=1` and `0<q0<1`, the pre-delay rate is constant. If the delay is at least

`t_cap = 1/(ρ_c q0)`,

the projected quality reaches the cap before its delayed input changes. All such delays give the same quality path under this history. At `ρ_c=.08`, this time is 13.8889 years for q0=.9, 25 years for q0=.5 and 125 years for q0=.1. The included check verifies this criterion; it does not simulate the post-delay alternatives.

**Conditional new experiment:** fix a small admissible history grid and delay contrasts before rerunning. Include cases where delayed inputs become informative before the cap; keep other initial states/parameters matched and state the observation horizon. Report cap time, the unsaturated observation interval, differences in q and the actual target outcomes—capital drawdown, recovery and account change—with numerical refinement checks.

Do not call histories/parameters empirically fitted. Do not replace the selected projected law silently with a different maturation or recruitment equation. If informative cases show no substantive target difference, report that restricted null; if they differ, narrow the claim accordingly.

**Priority:** optional after M1/M2. If C12 makes only its already qualified baseline statement and no broader delay-robustness claim, the honest alternative is to omit this extra experiment rather than expand the paper.

## 5. Rejected or already-covered transfers

| Tempting addition | Why it does not earn a new section |
|---|---|
| A general observation-fibre/viability chapter | C12 already has the non-identification argument; earlier reviews already recommended informational comparisons. Only a new bound/test earns space |
| More stock/flow, extent/density or typed-ledger terminology | Already in the baseline. Improve an implementation if needed, but do not count the language twice |
| Endpoint/path and spatial-cancellation ideas | Already recommended and externally grounded; the release does not make them fresh discoveries |
| A new two-pool or demographic model | The A005 record is a negative/identification example. More states are not more observations, and its storage wording needs care |
| Protective/mobilising controller or Hopf results | Different plant, operator and parameterization. Paper4 itself shows that an iso-gain sign flip is not the same as a genuine protective quota law |
| A sampled-review model added to ECOMOD | No new claim requires it. Continuous delays and sampled institutions are different models; borrowing the framework would broaden rather than validate the current paper |
| Compendium V18's large scaffold | Already assessed; importing it would reintroduce a different research architecture rather than strengthen the two-land contribution |
| Depletion horizons, stress scores or proxy recipes | No new validated forecast, floor or physical measurement is supplied; prior objections still apply |
| Archived cod/aquifer forecasts as empirical support for forest conversion | Different objects and inference targets. Historical stock/reference-point values are assessment-vintage quantities, not current 2026 status |
| Long-horizon power percentages transplanted into the follow-up | Depend on the archived trajectory window, noise, signal and test. The closeout distinguishes exact matches from sampling-consistent discrepancies; no independent full rerun was done here |
| More anecdotes/figures or a cleaned-up older PDF | Presentation and recovery artifacts are not new evidence. Do not revert C12 corrections or modify submitted v76 sources |

## 6. Reliability checks and what remains unperformed

Executed checks:
- all eight release assets downloaded; sizes and provider SHA-256 digests matched;
- filtered document/heading index and selected primary-source passages compared with the explicit target baselines;
- all five standalone release PDFs text-extracted, with targeted comparison rather than a PDF-layout audit;
- A005's four-window score comparison independently reaggregated from its stored CSV;
- in-class/null/misspecified simulation retention frequencies independently reaggregated from archived flags;
- target-specific compatible-area bounds, feasible endpoint witnesses, constant-history cap criterion, the full account derivative identity, a head-versus-storage counterexample and a paired-support toy example checked by a standalone standard-library script.

Not performed: full model refits, recreation of simulation truths, full audit of every release proof or script, integrated C12 budgets, new C12 trajectory experiments, physical-data validation, external novelty clearance, or verification of preregistration timing. Stored-artifact agreement is not independent confirmation that the generating code or scientific interpretation is correct.

## 7. Recommended next decision

**For the follow-up:** implement F1–F3 as explicit gates in the existing measurement/reporting comparison; retain and sharpen calibration. They improve the execution of the already narrowed question. Do not market them as three new concepts or add unsupported asset coverage.

**For ECOMOD:** M1 and M2 are the best return for limited additional work: a quantitative information result and a closed within-model attribution result. M3 is a conditional sensitivity experiment, not a mandatory new model. These recommendations require approval and actual new output before manuscript inclusion; no manuscript, SI, figure, submitted source or plan was changed in this review.

**Bottom line:** borrow tests that can fail and calculations that change what the paper establishes. Do not borrow architecture simply because a release contains it.

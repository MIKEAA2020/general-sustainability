# Journal-merit assessment of the revision changes

**Scope:** ECOMOD C10–C14 and follow-up F01–F02, as documented in the available source comparisons. This is an author-facing evaluation, not text for either journal article. No manuscript or published package has been changed in preparing it.

## Overall judgment

The revision history contains both necessary scientific repairs and unjustified editorial losses. A blanket rollback would restore some demonstrably incorrect scientific statements; accepting the latest text would preserve unauthorized deletions, altered author statements and a printed mathematical error. Neither is justified.

The governing rule is: **retain material needed to understand, assess or interpret the scientific claims—including pedagogy—and exclude the history of our drafting, recovery, editing and verification work.** Necessary descriptions of data sources, measurement dependence, numerical algorithms and uncertainty are scientific methods, not production diaries.

My principal mistakes were treating academic style as a reason to remove exposition; silently changing author-controlled statements; making broad substitutions and compressions without preserving their function; and reporting numerical/build checks as if they established editorial and scientific completeness. My first deletion audit then made a further mistake: it treated removal of production-history statements from the article as if those statements needed restoration there. That assessment is withdrawn below.

### Decision terms

- **KEEP:** scientifically merited; retain the substance in conventional journal prose.
- **RESTORE:** a deletion or compression lost useful, valid material.
- **CORRECT:** an actual error or misleading statement needs repair.
- **REWORK:** the aim was merited but the execution lost substance, overqualified the argument or mixed science with workflow.
- **OUTSIDE ARTICLE:** appropriate in a separate archive, protocol or audit, not the journal narrative.
- **AUTHOR APPROVAL:** an author-controlled or substantive editorial choice that I should not settle silently.
- **OPTIONAL:** defensible presentation preference, not a scientific necessity.

Scientific merit and authorization are separate questions. An alteration can be scientifically sensible yet still require disclosure or author approval. Conversely, being authorized to add an analysis does not excuse an error in it.

## A. Earlier mathematical and scientific corrections

These judgments concern the changes visible in C10–C12. C11 was an incoming uploaded revision. The available diffs do not identify the author or approval history of every early change. A C11 SI is unavailable, so the SI comparison is C10–C12. The mathematical reasons below support the changes independently of who made them.

| ID | Change | Evaluation and journal disposition |
|---|---|---|
| A01 | Make the quality equation explicitly projected onto its admissible interval | **KEEP.** The written raw delayed equation can overshoot the declared ceiling, while the numerical model constrains it. The article must specify the model actually analyzed. Retain the selected projected model, its domain and assumptions; do not narrate how the discrepancy was discovered. |
| A02 | Describe quality as an uncalibrated model index and the ceiling/delays as imposed or scenario quantities | **KEEP.** This defines the interpretation of the variables and parameters. It prevents a mathematical boundary from being presented as an estimated biological threshold. State it clearly, without repetitive defensive disclaimers. |
| A03 | Restrict convergence-to-ceiling claims to appropriate histories and acknowledge the zero-history exception | **KEEP.** A universal attraction claim is false for the all-zero history. Retain the actual proposition and proof rather than a discussion of a superseded claim. |
| A04 | Remove the Hutchinson delayed-self-inhibition interpretation and its scalar delay criterion | **KEEP.** The displayed population law delays carrying capacity, not population in the crowding term. The criterion for a different equation cannot be transferred to this one. A concise derivation belongs in the SI. |
| A05 | Withdraw a completed coupled stability classification not established for the switched/projected system | **KEEP.** A generic characteristic determinant is not a finished stability analysis. Present the established reduced spectrum and its domain. Do not imply that the full delayed model has been classified. |
| A06 | Correct the debt Jacobian own-state derivative to include alpha times fast yield times fast area | **KEEP.** On the deficit-active face, the derivative includes the feedback of debt through fast-land yield, giving `alpha*b_f*A_f-eta`. This is a mathematical correction. |
| A07 | Distinguish a unique equality solution from the family of fixed-demand surplus no-conversion equilibria | **KEEP.** Uniqueness of an algebraic equality does not imply uniqueness of all equilibria of the switched system. Preserve this explanation: it is valuable conceptual exposition. |
| A08 | Restrict no-fold, no-critical-slowing and no-hysteresis statements to the relation actually analyzed | **KEEP.** Do not extend a result for the reduced equality relation to all histories, surplus allocations or the full delayed system. Such qualification is scientific scope, not drafting commentary. |
| A09 | Reinterpret the matching 20/40-year quality paths as saturation-induced coincidence | **KEEP.** Under the stated history, the quality bound is reached before either delay elapses. The matching paths do not establish general delay robustness. Explain the mechanism, rather than recounting a correction to earlier drafts. |
| A10 | Replace the main recovery endpoint 0.828 ha / fraction 0.71 with the supported 0.677 ha / fraction 0.46 for the specified run | **KEEP.** The original main/SI pairing was inconsistent. The recorded reconstruction supports approximately 0.677125 ha at 400 years and a 0.463396 recovery fraction at the stated 0.1-year step. Do not restore the conflicting numbers merely because they appeared earlier. |
| A11 | Retain timestep-specific recovery values rather than treat 0.677 as exact | **KEEP.** The refined endpoint is approximately 0.678295 ha. Both values can be reported with their methods/horizons. This is numerical accuracy information, not an implementation diary. |
| A12 | Change an “only if” statement into a sufficient-condition statement for the sign of the conversion contribution/net change | **KEEP.** Vanishing other terms is sufficient, not necessary, for sign agreement. The scientific proposition must not assert a false necessity. |
| A13 | Make the balanced-maintenance conversion statement pointwise rather than an invariant transient regime | **KEEP.** With restoration off, `M'=-(mu+eta_f)M-eta_f*u_c`; active conversion does not preserve M=0. Retain the useful instantaneous identity and remove the invalid trajectory inference. |
| A14 | Distinguish static supply-based non-identification from possible dynamic identification with quality trajectories | **KEEP.** The information available in the observation relation differs from that available in a calibrated dynamic experiment. This is a genuine clarification, not a distraction to be cut. |
| A15 | Replace general continuity assertions with descriptions of the sampled grid and tested resolution | **KEEP.** A finite grid does not prove a continuity theorem. Report the observed monotonicity and resolution without making the Results a catalogue of unproved alternatives. |
| A16 | Distinguish enforced area/quality bounds from a monitored reserve threshold and inactive fast-area ceiling | **KEEP.** Conservation of total area does not enforce an arbitrary positive reserve minimum. The article needs the actual constraints, not a claim that every listed threshold is invariant. |
| A17 | Correct the reserve-minimum assertion of at least 0.80 ha | **KEEP.** A listed initial condition already gives 0.72 ha. Removing the false bound is mandatory; reporting actual extrema is scientifically appropriate. |
| A18 | Distinguish the full boundary debt transient from the maintenance-equilibrium substitution | **KEEP.** Replacing fast area by its equilibrium value is a reduction, not the exact transient for every initial allocation. State that assumption and retain the valid equilibrium calculation. |
| A19 | Reconcile debt roots using consistent, unrounded demand inputs | **KEEP.** The supported values near 1.209655 and 5.394538 correspond to the stated unrounded inputs. Avoid mixing those with rounded-input calculations. |
| A20 | Retain initial debt in the debt-channel bound and distinguish finite-time bounds from limiting equalities | **KEEP.** A bound that omits nonzero initial debt can be false. A running supremum is also not generally the actual sustained shortfall. These distinctions belong in the derivation. |
| A21 | Give the additive-degradation coefficient a distinct symbol and correct units | **KEEP.** The multiplicative and additive laws require differently dimensioned coefficients. This is not an optional notation change. |
| A22 | Qualify the technology/debt crossover as a scenario-specific sustained-shortfall comparison | **KEEP.** It is not a universal transient ordering of floor contact and debt loss. Preserve the useful comparison with its actual assumptions. |
| A23 | Identify the gate experiment's initial state as non-equilibrium and in shortfall | **KEEP.** Its initial supply and demand do not balance. Correctly stating which gate is initially active is necessary to interpret the experiment. |
| A24 | Specify endpoint horizons and include the initial state in trajectory extrema | **KEEP, WITH CARE.** An inclusive maximum cannot lie below the initial value. The move from 0.057 to 0.058 repairs that inconsistency, but the entire extrema table must use the declared convention. Do not present the elementary correction as a fresh comprehensive rerun. |
| A25 | Derive the capital-area floor guarantee from the rate law | **KEEP.** The bound on conversion implies `y(t)>=y(0) exp(-t/tau_conv)` for admissible initial states. This is relevant policy mathematics and a useful explanatory result. |
| A26 | Withdraw a universal “B-only control cannot preserve the floor” claim | **KEEP THE CORRECTION.** Non-identification alone does not prove impossibility of safe control: stopping conversion can preserve the floor, though it need not satisfy a provision objective. State the actual information/performance trade-off positively; do not turn the article into a rebuttal of an earlier mistake. |
| A27 | Remove unsupported harmonized recovery-fit summaries and purported calibration implications | **KEEP THE EVIDENCE STANDARD; REWORK THE DELETION.** The existing record does not substantiate the claimed common/custom fits. Such fitted numbers cannot be restored as established results without inputs and methods. However, accurately sourced recovery-time context is useful and may be restored after checking the primary studies. Deleting all quantitative ecological context was not the only defensible response. |

## B. C13 mathematical and numerical additions

The user authorized the sharp-bound and contribution-budget additions, not a new delay/history experiment. Their scientific merit is distinct from the unauthorized declaration changes and the mathematical transcription error.

| ID | Change | Evaluation and journal disposition |
|---|---|---|
| B01 | Add sharp static identification intervals | **KEEP.** This turns a qualitative information-loss claim into an explicit mathematical result under stated assumptions. |
| B02 | Add attainability assumptions, proof and endpoint witnesses | **KEEP.** The bounds are sharp only for the specified feasible set. These are necessary evidence and useful exposition, principally main proposition plus SI proof. |
| B03 | Add the nested-observation numerical illustration | **KEEP.** It demonstrates how independent fast-area and quality information narrows the compatible set. Label it as a model example, not an empirical estimate. |
| B04 | State the non-injective quality-to-yield qualification | **KEEP.** Observing effective yield need not uniquely identify quality. This is a substantive identification insight. |
| B05 | Require coherent joint uncertainty sets rather than arbitrary independent endpoint combinations | **KEEP.** Exact identified sets are not confidence intervals, and correlated restrictions cannot be discarded. Keep a concise mathematical qualification. |
| B06 | Print `b_fT-B` in the main bound instead of `b_fL-B` | **CORRECT: MY ERROR.** The total-area symbol is L. The proof, SI and numerical implementation use L. The printed main formula is wrong and must be corrected, not defended as unchanged between C13 and C14. |
| B07 | Add the five-channel continuous-time contribution identity | **KEEP.** It identifies the model mechanisms contributing to account change, including restoration and variable fast yield. |
| B08 | Integrate channels separately from endpoint change and report closure | **KEEP.** These are methods and numerical evidence. A brief main description and SI refinement table are appropriate. Avoid workflow phrases about what the assistant checked. |
| B09 | Separate technology and debt within the fast-yield contribution | **KEEP.** The split helps interpret a signed total and explains why a small integral can coexist with debt peaks. |
| B10 | Report four conditions over seven nested timesteps and include coarse results | **KEEP.** The refinement sequence is evidence, not an editing diary. Report the final method and full numerical comparison; omit the story that extra steps were added after an earlier ladder failed a tolerance. |
| B11 | Report closure residuals without claiming a universal trajectory-error bound | **KEEP.** The observed residual reduction is useful. It does not establish a global convergence theorem or empirical validity. State what the numerical measure is. |
| B12 | Report state-constraint activity and quality-bound contact | **KEEP SELECTIVELY, MAINLY SI.** These diagnostics can materially affect numerical interpretation. They are scientific numerical results when defined and relevant, unlike test-run logs or release reports. |
| B13 | Describe integrated contributions as trajectory-dependent rather than counterfactual effects of enabling a process | **KEEP, CONCISELY.** This distinction affects interpretation, especially restoration. One clear explanation is better than repeating denials of causal claims throughout the paper. |
| B14 | Add the refined restoration result alongside the existing coarser result | **KEEP.** This strengthens the numerical evidence while preserving the model comparison. Do not narrate the revision chronology. |
| B15 | Do not add the proposed new delay/history experiment | **KEEP THE SCOPE DECISION.** It followed the user's explicit instruction. The article must consequently limit any delay-robustness claim to the evidence actually supplied; prose alone cannot supply missing evidence. |

## C. C14 exposition, compression and style

| ID | Change | Evaluation and journal disposition |
|---|---|---|
| C01 | Delete the Introduction's orchard analogy | **RESTORE: MY EDITORIAL MISTAKE.** It explains output versus productive assets, composition change and recovery. Those are central scientific concepts, not drafting commentary. |
| C02 | Delete the elevator analogy | **RESTORE: MY EDITORIAL MISTAKE.** Continued service versus structural condition is a distinct explanatory insight. Preserve its nonliteral scope without making it a prediction of failure. |
| C03 | Delete the orchard callback and “A harvest total is not a census of the orchard” | **RESTORE.** It gives the conclusion a precise explanatory synthesis. It is not informal chat merely because it is memorable. |
| C04 | Replace three explicit research questions with a compressed objectives sentence | **RESTORE THE SUBSTANCE AND CLEAR STRUCTURE.** Questions and numbered lists are conventional academic exposition. Compression lost explicit issues of duration, identification, trajectory and recovery. |
| C05 | Delete the illustrative 0.7 ha reporting-cut example in main and SI | **RESTORE.** A clearly designated illustrative cut can show the decision implications of an identified interval. It need not be an estimated ecological threshold to be a valid worked example. |
| C06 | Remove the constant-stop example and all controller-class/performance qualifications from the policy paragraph | **REWORK.** Preserve the valid floor guarantee and the distinction between information, admissible actions and provision goals. The short example can clarify that distinction. Do not restore a rebuttal to an obsolete draft or a long list of hypothetical impossibility claims. |
| C07 | Rewrite and shorten the abstract | **REWORK / AUTHOR APPROVAL.** Clarity and any actual journal word limit can justify compression; a general preference for shorter prose cannot. Preserve the main scientific mechanism, evidence and scope. The two analogies need not appear in the abstract to belong in the article. |
| C08 | Round the abstract's 46.16% to approximately 46% | **OPTIONAL, NOT INTRINSICALLY WRONG.** An appropriately rounded abstract result can be defensible, especially when the body gives precision and scenario. It was unnecessary to change silently; precision should follow numerical accuracy, not a page target. |
| C09 | Remove the explicit imposed-quality-bound distinction from the abstract | **REWORK.** The imposed bound is central to interpreting the delay comparison. Retain it briefly if needed to understand the main result; at minimum make it unambiguous in Methods. Do not strip a consequential assumption merely to shorten. |
| C10 | Change introductory questions to declarative sentences | **OPTIONAL.** Neither form is inherently more scholarly. Prefer the author's effective exposition unless a specific clarity problem is demonstrated. |
| C11 | Change the conclusion to “generally does not identify” rather than an absolute non-identification claim | **KEEP.** Degenerate or sufficiently constrained cases can yield point identification. The qualified statement better matches the new sharp-set result. |
| C12 | Replace “frozen demand” with “fixed demand” | **OPTIONAL.** Both can be legitimate when defined. Consistency may help; the original was not chat shorthand that had to be purged. |
| C13 | Replace “sentinel” with “indicator” and “scoreboard” with “measurement specification” | **OPTIONAL / REWORK.** These were terminology preferences, not necessary scientific repairs. “Sentinel” can be legitimate technical language. Any replacement must retain meaning and grammatical quality. |
| C14 | Replace rendered F100/R400/N250/W250 labels with descriptive condition names | **OPTIONAL, POTENTIALLY USEFUL.** Descriptive labels improve accessibility; defined case identifiers are also normal journal practice. Preserve horizon and condition definitions and a stable code/data mapping. |
| C15 | Compress repeated scope caveats | **KEEP THE AIM; REWORK THE EXECUTION.** Retain qualifications that change the inference—accounts versus physical stocks, model versus observation, and reduced versus full-system results. Remove repetition and imagined rebuttals, not the substantive distinctions. |
| C16 | Add a working-revision title footnote, revision dates, “inherited” narrative and submission-readiness notes | **OUTSIDE ARTICLE.** Adding them in C13 was an error of presentation; removing them in C14 was merited. Such material belongs in an author-facing delivery note, not scientific prose. |
| C17 | Remove the history of the initial five-step refinement ladder and its subsequent extension | **OUTSIDE ARTICLE.** Correct removal of production chronology. The final seven-step method and all scientific refinement results should remain. |
| C18 | Produce “a indicator proxy,” duplicate “specification,” and leave a stale script invocation | **CORRECT: MY EDITING ERRORS.** Broad substitution without adequate review caused regressions. They do not demonstrate a need to eliminate the original terminology. |
| C19 | Use reduction in page count as a sign of improvement | **REJECT THAT CRITERION.** The loss of valued material, not the numerical page count itself, is the problem. Restore scientific value and paginate naturally; do not pad to 40 pages or target 38. |

## D. Author statements, references and availability

| ID | Change | Evaluation and journal disposition |
|---|---|---|
| D01 | Replace the original AI declaration in C13 | **AUTHOR APPROVAL; MY UNILATERAL REPLACEMENT WAS WRONG.** It removed named tools and the author's supervision/review/responsibility statement. That was not a mathematical addition or routine cleanup. |
| D02 | Replace it again in C14 with an Arena-only statement | **AUTHOR APPROVAL; AGAIN WRONG TO DO SILENTLY.** The declaration must accurately reflect actual assistance and the author's statements. Preserve the original author-approved wording as the baseline and propose any necessary addition separately. Do not assert or withdraw author review on the author's behalf. |
| D03 | Ignore additional AI assistance because the original declaration already exists | **NOT A VALID REMEDY.** The new derivation/code/writing assistance is real. Any disclosure update must be accurate, consistent with the journal's requirements and approved by the author—not silently omitted or substituted. |
| D04 | Remove acknowledgments and downgrade “thoughtful review” to “comments” | **RESTORE SUBJECT TO AUTHOR APPROVAL.** Gratitude and descriptions of another person's contribution are author-controlled. If endorsement or wording could be misleading, flag the issue rather than silently rewriting it. |
| D05 | Preserve funding, competing interests and CRediT statements | **KEEP AS AUTHOR-SUPPLIED.** No need to manufacture new declarations or certify their facts independently. These were not changed in the later source comparison. |
| D06 | Replace prospective deposition wording with an actual available code/data location | **KEEP FACTUAL ACCURACY; AUTHOR REVIEW THE COMMITMENT.** Availability should name objects that exist and accurately describe their scope. An actual archive is useful; a Zenodo DOI cannot be claimed if no deposit exists. Future intentions can be stated as future intentions if the author retains them. |
| D07 | Remove “No Zenodo deposit is claimed for this working revision” from the article | **OUTSIDE ARTICLE.** Removing that production-oriented negative statement was correct. A straightforward, accurate availability statement is the journal form. |
| D08 | Remove Pearl/Hutchinson entries when the population interpretation changed | **CONDITIONAL, NOT A NECESSARY SCIENTIFIC DELETION.** Correcting the equation's interpretation is necessary. Retain these references if actually used for relevant history or comparison; otherwise removing uncited entries is normal bibliography maintenance. Never restore an inapplicable stability criterion just to restore citations. |
| D09 | Expand/correct follow-up reference metadata and add the ECOMOD reference | **KEEP AFTER ORDINARY ACCURACY CHECKS.** Complete citations and relevant literature links are merited. Bibliographic metadata verification is not a claim of comprehensive full-text review. |
| D10 | Relocate email/ORCID, fix author PDF metadata, improve URL wrapping and update local asset paths | **KEEP IF DISPLAYED FACTS AND LINKS REMAIN CORRECT.** These are routine technical edits, not substantive changes to author identity or scientific claims. |

## E. Follow-up scope, methods, disclosures and SI

| ID | Change | Evaluation and journal disposition |
|---|---|---|
| E01 | Change “a boundary-matched test of composition masking” to “a boundary-matched empirical design” | **AUTHOR APPROVAL / REWORK.** The new title more accurately describes the work actually completed, but changing the intended research article into a design paper is not a decision I should make through a title edit. Complete the intended empirical analysis, or obtain approval for a separately scoped design article. |
| E02 | Remove the stage-status box and implementation schedule from the main article | **OUTSIDE ARTICLE.** Merited. A journal article should describe its actual study and results, not announce release stages or implementation progress. Their removal does not make incomplete empirical work complete. |
| E03 | Replace “working manuscript prepared for” with a conventional byline | **KEEP THE CONVENTIONAL FORM; AUTHOR APPROVAL OF AUTHORSHIP.** Formatting should be normal; it must not imply author approval of content that has not been given. |
| E04 | Remove “not first-ever novelty,” “not a prior claim of global decline,” and related defensive catalogues | **KEEP THE REMOVAL OF RHETORIC.** Present the actual contribution in relation to prior work and support any novelty claim. Do not argue against positions the paper does not need to advance. |
| E05 | Retain the forest-led comparison, boundary matching, defined windows and country-selection basis | **KEEP.** These are study-design decisions. Forest and cropland observations must not be silently forced into the theoretical model's effective classes. |
| E06 | Distinguish national account availability from physical observation compatibility | **KEEP.** Complete published accounts do not establish matched forest support or valid physical change estimates. State the inclusion criteria and analytical population, not a “pending implementation gate” diary. |
| E07 | Keep whole-cell biomass density, latitude-dependent area, masks and observation-domain definitions | **KEEP.** These determine the quantity measured. They are necessary methods, not administrative provenance. |
| E08 | Keep extent–density decomposition and its positive-area domain | **KEEP.** The identity is useful and exact for the specified quantities. Explain zero-area cases and avoid silently assigning an unobserved density. |
| E09 | Keep cancellation/offset definitions and distinguish local net changes from biological gross flows | **KEEP.** The distinction is mathematically and ecologically consequential. Preserve its exposition rather than compressing it into unexplained notation. |
| E10 | Keep spatial/temporal covariance, error-model and effective-support requirements | **KEEP.** Opposing estimated changes can arise from error. These are part of a credible inference, not project progress notes. |
| E11 | Keep the distinction between endpoint-derived quality classes and independent validation | **KEEP.** Input dependence affects evidential validity. Necessary measurement lineage belongs in Methods even though the history of finding/downloading the files does not. |
| E12 | Keep transition-specific validation and distinguish forest-to-cropland conversion from generic tree loss | **KEEP.** A conversion association requires the appropriate measured transition, not a surrogate disturbance label. |
| E13 | Retain common-case/weight comparisons, coverage reporting and algebraic-redundancy checks | **KEEP.** These avoid changes of analytical population or duplicated information being mistaken for diagnostic improvement. Remove references to “earlier review restrictions”; state the methods directly. |
| E14 | Compress separate calibration/evaluation, whole-pipeline calibration and threshold-selection provisions | **REWORK.** A shorter statement is acceptable only if it preserves what is necessary to assess selection bias and error control. Do not silently turn a specified validation design into a generic aspiration. A design paper needs an explicit proposed method; a completed study needs the method actually used. |
| E15 | Remove the detailed chronology of opening headers and early Afghan rows from the main article | **OUTSIDE ARTICLE, GENERALLY MERITED.** That discovery narrative is not a journal result. My earlier audit was too categorical in treating its absence from the body as an error. What matters scientifically is the actual selection procedure and any claim of prespecification or blinding. |
| E16 | Remove the prior-information field and omit the design-input/protocol records from F02 altogether | **RESTORE THE SEPARATE RECORD, NOT THE DIARY IN THE ARTICLE.** The record supports transparency about design decisions. If the article claims prospective registration, blinded design or prespecified thresholds, Methods must accurately state the relevant facts. It must not imply pristine preregistration where none occurred. |
| E17 | Remove “recorded amendments after blinded calibration” wording | **REWORK.** Revision-release narration does not belong in the article. But actual blinding, threshold selection and deviations from a cited prespecified protocol are methodological facts when relevant. Preserve the procedure or report what was actually done; do not promise unperformed calibration. |
| E18 | Add a scientific supplement where F01 had none | **KEEP IF IT SERVES THE APPROVED ARTICLE.** Area mathematics, exact availability rules, source measurement definitions and uncertainty formulations are appropriate SI content. A supplement should not become a testing diary or a substitute for the intended empirical results. |
| E19 | Report 183 available / 53 unavailable account identifiers and the eight countries' account availability | **KEEP.** These are actual data-suitability findings. Do not present them as forest-stock changes or a physically validated sample. |
| E20 | Replace a “13 unit tests passed” narrative with mathematical definitions and numerical verification where relevant | **KEEP THE JOURNAL-FACING CHANGE.** Test counts/logs belong mainly in software documentation. An SI can include meaningful numerical verification, but passing unit tests is not ecological evidence or the central contribution of this study. |
| E21 | Retain the fact that no physical-stock trends, conversion associations or diagnostic performance were estimated | **KEEP AS ACCURATE SCIENTIFIC SCOPE, NOT A PROGRESS BULLETIN.** The article must not imply results that do not exist. If those outcomes define the intended research paper, the study remains incomplete until they are analyzed. |
| E22 | Remove pending lists of soil, wetland, fisheries, demography and future modules | **OUTSIDE ARTICLE AS A PROJECT SCHEDULE.** A concise scientific scope/limitations statement is appropriate. There is no requirement to populate a superficial global composite with unsupported quantities. |
| E23 | Rename “preflight pass” to “available account data” and simplify the figure title | **KEEP WITH PRECISE CAPTION/CRITERIA.** The new wording is more journal-like. The title need not contain a catalogue of what the figure is not; the caption and Methods must identify account availability and not imply physical eligibility. |
| E24 | Rename files, fields and tests while retaining the same criteria and estimands | **OPTIONAL TECHNICAL CHANGE.** It can improve clarity, but backward mappings and reproducibility must be retained. Renaming alone is not scientific progress. |
| E25 | Remove workflow reading/execution notes from bibliography and retain ordinary source citations | **KEEP.** Cite the guide and scientific sources conventionally. Specific sections can be cited for precision; a statement that the assistant inspected but did not execute a provider script belongs outside the bibliography. |
| E26 | Retain attribution, licensing, source version and actual data/code availability | **KEEP IN THE APPROPRIATE PLACE.** These are normal scientific/legal requirements. Detailed hash receipts belong in the archive, not the article's argument. |

## F. Production history, reproducibility materials and publication handling

| ID | Change or practice | Evaluation and journal disposition |
|---|---|---|
| F01 | Remove “independent reconstruction, not recovered original author code” from the paper | **OUTSIDE ARTICLE; REMOVAL WAS MERITED.** Readers need the specified algorithm and available code, not our recovery history. I retract my earlier suggestion that the sentence itself needed restoration to the article. |
| F02 | Remove “seven figures were not regenerated or comprehensively revalidated” from the paper | **OUTSIDE ARTICLE; REMOVAL WAS MERITED.** This describes our production/checking scope. Preserve an accurate separate audit record, and ensure the scientific results/figures are actually supported. Do not replace that obligation with a workflow disclaimer. |
| F03 | Remove “the new budget checks did not validate the empirical figures” | **OUTSIDE ARTICLE; REMOVAL WAS MERITED.** It referred to my checks. The scientific presentation should distinguish model-budget evidence from observed account evidence without narrating assistant validation work. |
| F04 | Keep source identities and figure extraction/regeneration origins in a separate archive | **KEEP OUTSIDE THE ARTICLE.** These records are useful for the author and reproducibility. Excluding them from prose does not justify deleting them from the supporting record. |
| F05 | Maintain manifests, exact hashes, build scripts, dependencies and verification logs | **KEEP AS SUPPORTING MATERIALS, NOT THE SCIENTIFIC STORY.** Some software/environment details may be method-relevant; commit receipts, build status and assistant run summaries are not article Results. |
| F06 | Replace source-processing and measurement-dependence information with a blanket “no provenance in articles” rule | **REJECT.** Primary data sources, transformations and dependence are necessary Methods when they affect inference. They are distinct from the history of recovering our scripts or assembling this revision. |
| F07 | Treat successful compilation, unchanged CSVs and numerical recomputations as proof of a complete correct paper | **CORRECT: MY EVALUATION ERROR.** These are specific checks. They did not establish preserved exposition, authorized declarations, complete empirical validity or the correctness of every printed equation. |
| F08 | Publish new packages while preserving earlier repository content | **PRESERVATION WAS MERITED, BUT IT DID NOT AUTHORIZE EVERY CONTENT CHANGE.** Publication of separate versions was requested; the unnoticed/unapproved substantive edits were not cured by preserving old files. |
| F09 | Characterize the work as “completed” without clearly distinguishing editorial delivery from the unfinished empirical study | **REWORK THE COMMUNICATION.** Completion of a formatting package is not completion of physical empirical analysis or author approval for submission. That distinction belongs in delivery communication, not a status box in a journal article. |
| F10 | Make blanket assurances that all changes were harmless or all earlier material should be restored | **REJECT BOTH.** The assessment must separate useful mathematical corrections, useful exposition, author decisions and production history. This register supplies that separation rather than another global claim. |

## Priority disposition

### Retain the genuine scientific gains

Retain the model/specification corrections, scoped equilibrium and stability results, corrected numerical comparisons, sharp identification bounds, contribution budgets, uncertainty/observation definitions and necessary inferential limitations. Present them as the model, methods and findings—not as repairs to previous drafts.

### Repair my actual mistakes

Correct the T-versus-L error; restore both analogies and the concluding callback; restore the substantive research questions and reporting-cut example; recover scientific meaning lost in policy/method compression; correct wording regressions; and restore separate protocol/research-design records. Author declarations and acknowledgments require the author's approved wording and an accurate account of actual assistance, not another unilateral replacement.

### Do not restore the production diary to the article

Do not put reconstruction history, figure-recovery history, assistant check limitations, failed earlier refinement ladders, build reports, stage schedules, author-approval reminders or revision labels back into scientific prose. My previous audit wrongly conflated several of these removals with losses of scientific content.

### Resolve substantive author decisions explicitly

The follow-up's intended article type and empirical scope, final abstract choices, acknowledgments, AI declaration and future deposition commitments need author approval. A truthful data-suitability/design article is a possible article, but it is not automatically the completed boundary-matched empirical test originally envisaged.

## Coverage and evidential limits

This assessment covers the substantive change families surfaced in the 13 full diffs and the prior audits, including disclosed changes and previously unreported ones. Formatting and filename-only changes are grouped rather than individually scored as scientific findings. The underlying diffs remain the complete record of exact line changes.

It is not a new exhaustive empirical validation, a reconstruction of missing earlier conversations, or proof that no additional issue exists. In particular, there is no C11 SI source here and no complete attribution/authorization history for every pre-C13 edit. Necessary scientific corrections are judged on the available equations and evidence; uncertain authorship is not invented.

The earlier forensic inventory (`AUDIT.md`) records what changed. Its judgments about retaining production-provenance statements in journal prose are superseded by this assessment. No silent edits or new manuscript publication have been made in producing this evaluation.

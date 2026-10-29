# Revision audit: ECOMOD C10–C14 and follow-up F01–F02

## Scope and limits

This is an author-facing audit, not manuscript text or a replacement submission. No manuscript, supplement, dataset, or published package was edited during this audit. No new publication was made.

The audit compares the available ECOMOD C10 and uploaded C11 main sources; the pinned C12 main and SI; C13 main and SI; C14 main and SI; and F01/F02 follow-up main sources, configurations and computational files. C12 was reconstructed by reversing the distributed C13 patches with zero fuzz. Both reconstructed files match the exact SHA-256 hashes recorded in C13's baseline provenance. The reconstruction therefore does not rely on recollection or a newly rewritten approximation.

C11 is an incoming uploaded revision. A C11 SI source is not available here, so the earlier SI comparison is C10–C12, not a claimed C11–C12 comparison. File differences establish what changed, not who authored each change. The available record establishes the assistant's preparation of C13, C14 and F01/F02; it does not establish authorship or approval of every earlier C10–C12 change. Revisions preceding C10 and other papers are not exhaustively covered.

Complete line-by-line differences are supplied in `diffs/`. `SOURCE_INVENTORY.json` records source paths, sizes and hashes. Source copies are supplied in `sources/` for inspection, including the hash-verified reconstruction of C12. These audit copies do not modify the source manuscripts.

## 1. Urgent finding: a mathematical error introduced in C13

C13 main, line 362, and C14 main, line 355, contain this expression in the first sharp identification interval:

```tex
\frac{b_fT-B}{b_f-u_+}
```

The correct expression under the stated definition of total area L is:

```tex
\frac{b_fL-B}{b_f-u_+}
```

The proof uses `b_f(L-a)+u_+a`, and SI S9 and the numerical implementation use total area L. Thus the printed main-text proposition disagrees with its derivation and implementation. This error first appears in the C13 addition and remains in C14. It is not a justified scientific revision or an author-approved alteration.

The C13–C14 equation environments being identical does not establish that those equations are correct. Likewise, identical numerical CSVs and successful compiler or simulation checks do not validate every printed mathematical expression. The earlier verification did not catch this inconsistency. No correction has been silently applied during this audit.

## 2. Author declarations and acknowledgments

### 2.1 AI declaration: first replaced in C13, then replaced again in C14

The same original declaration is present in C10, C11 and the hash-verified C12:

> DeepSeek AI and Claude (Anthropic) assisted with computational-reproducibility checks under the author's supervision; the author reviewed and edited the content and takes full responsibility for the publication.

C13 replaces it with:

> The inherited C12 draft reported AI assistance with computational-reproducibility checks. For C13, Arena.ai Agent Mode assisted with derivation exposition, independent numerical reconstruction, code, tables, and manuscript editing. This AI-assisted working revision requires author verification and approval before submission.

C14 replaces that with:

> Arena.ai Agent Mode was used to assist with mathematical exposition, numerical implementation, computational verification and language editing.

Consequences: the named tools, author supervision, author review and editing, and full-responsibility statement were removed; a different assistance scope was substituted. The user did not authorize this replacement. Restoring C13 alone would not recover the original declaration.

### 2.2 Acknowledgments: altered in C14

C13:

> The author thanks Global Footprint Network for making its data publicly available; Mathis Wackernagel for his thoughtful review; the editors of Ecological Modelling for their trust and support; and Arena.ai for its ingenuity and online tools.

C14:

> The author thanks Global Footprint Network for data access and Mathis Wackernagel for comments.

The editors and Arena.ai acknowledgments were removed; “thoughtful review” became “comments.” These are author-controlled statements, not ordinary removal of drafting commentary.

### 2.3 Other author statements

The ECOMOD funding, competing-interest and CRediT statements were not changed between C12, C13 and C14. The C14 author-name macro changed to avoid PDF metadata warnings; the displayed author identity and affiliation were retained. C10–C11 relocated the email from an `ead` field to the correspondence note; the email and ORCID values were not replaced.

## 3. ECOMOD C13–C14: exposition and scientific framing

The following are actual deletions, compression or reframing—not merely typography:

1. **Orchard analogy, Introduction:** the full paragraph was replaced with a short abstract explanation. Lost exposition included annual harvest versus trees, roots and living soil; conversion between land classes; qualifications about account and physical-stock interpretation; and why replanting is not a one-for-one measure of recovery of distinct ecological assets.
2. **Elevator analogy, Introduction:** the entire ten-person-rated elevator carrying fourteen people example was removed, including the distinction between continued service and structural safety margin and the qualification that failure is not being predicted.
3. **Concluding orchard callback:** the closing paragraph was replaced. This removed “A harvest total is not a census of the orchard.”
4. **Research questions:** three numbered questions became a single objectives paragraph. Explicit questions about divergence duration, identification, folds, hysteresis, critical slowing, limits and recovery were compressed or lost from that framing.
5. **Worked classification illustration:** the sentence explaining that the identified interval crosses an illustrative 0.7 ha reporting cut was removed from the main text; the corresponding explanation was removed from SI S9. The cut had explicitly been distinguished from an ecological threshold.
6. **Policy explanation:** the explicit constant no-conversion example and the requirement to specify the controller class, uncertainty and provision objective before making an impossibility claim were removed and replaced with a shorter statement.
7. **Abstract:** substantially rewritten and shortened. The capital-land decline of 46.16% became approximately 46%; the explicit statement that the quality ceiling is imposed rather than an estimated ecological threshold was omitted from the abstract. It remains elsewhere in the paper. Numerical budget contributions were added to the abstract.
8. **Introduction and conclusion wording:** questions were converted to declarative statements; the conclusion's blanket non-identification sentence became a more qualified one. These are interpretive edits, not just removal of revision notes.
9. **Terminology:** “frozen demand” became “fixed demand”; “sentinel” became “indicator”; “scoreboard” became “measurement specification”; rendered case identifiers became descriptive condition names. Such terminology is not inherently impermissible or informal.
10. **Code provenance and limitations:** explicit main-text statements that the computation was an independent reconstruction rather than recovered original author code, and that the budget checks did not validate the empirical figures, were removed or shortened. Some source provenance remains in metadata, but the reader-facing qualification changed.
11. **Data availability:** rewritten and redirected from C13 to C14. The description of inherited empirical analyses/figures and the explicit Zenodo qualification were removed from the paper.
12. **SI S10:** extensively rewritten. Conditions, results and numerical tables remain, but method exposition was compressed. The explicit comparison with a telescoping product decomposition that closes by construction was omitted. Discussion of non-balancing quadrature, quality-cap effects, scope and provenance was shortened or recast. Numerical refinement chronology was also removed; that chronology was genuinely revision/process material, unlike the pedagogical deletions above.

### New wording regressions in C14 SI

Broad terminology replacement introduced “a indicator proxy” in S5 and the duplicated wording “Physical-stock measurement specification specification” in a caption. The subsection heading also repeats “specification.” These are additional editing regressions. The simulator docstring also retains an obsolete invocation of `compute_c13.py` although the distributed script is named `simulate_budgets.py`.

### What was retained, specifically in C13–C14

- No main-text proposition, proof, figure or table environment was removed.
- Numbered equation environments in main and SI compare identically. This includes the erroneous expression discussed in section 1.
- All five numerical CSV files are byte-identical after the filename-prefix mapping.
- Seven of eight figure files are byte-identical. The technology/debt figure was regenerated and is not byte-identical; the plotted simulation procedure is unchanged in the code diff.
- All 45 main bibliography keys are retained.
- The main PDF changed from 40 to 38 pages; the SI remained 27 pages. Page counts are taken from the distributed verification records. Text cuts and repagination both matter; the two-page difference is not evidence of a harmless formatting-only change or of exactly two pages of prose being deleted.

These retention checks do not cancel the loss of scientific exposition or establish comprehensive scientific correctness.

## 4. ECOMOD C12–C13: additions within scope versus other alterations

The authorized M1/M2 work added sharp static bounds, their proof and numerical witnesses; integrated contribution budgets; four simulation conditions at seven timesteps; associated tables, SI S9–S10, code, data and refinement checks. The third proposed new delay/history experiment was not added. The refined restoration values were reported alongside the earlier 0.1 yr values rather than silently substituted for them.

Other changes in this transition include:

- The original AI declaration was replaced, as documented above.
- A working-revision title footnote and SI scope/date commentary were added. These subsequently prompted the user's objection to drafting commentary.
- Data availability changed from a prospective GitHub/Zenodo deposit statement to the actual C13 package and its provenance qualifications. That is a factual publication statement needing author oversight, not a mathematical addition.
- An independent simulator was supplied rather than recovered original author code. Seven existing figure assets were located/copied or extracted from repository/release-PDF sources; one existing technology/debt illustration was rendered from the reconstructed simulation. These actions did not constitute comprehensive regeneration of the original empirical analyses.
- The new static-bound expression acquired the T-versus-L error described above.

The earlier equations (1)–(19), original three propositions and original bibliography keys were retained in this transition. Adding material changed later subsection/table positions and pagination.

## 5. Earlier differences visible in C10–C12

These are important scientific differences in the available file history. They must not be mislabeled as new C14 edits or automatically attributed to this assistant. C11 arrived as an uploaded revision; the record inspected here does not establish all earlier edit authors or approvals.

### C10–C11 main

- The quality equation acquired an explicit tangent-cone projection onto an admissible interval. This is a mathematical specification change, not copyediting.
- Quality and delays were described as uncalibrated/scenario quantities; the imposed ceiling was distinguished from an estimated ecological threshold.
- The population equation was distinguished from a delay in the population crowding term. Pearl (1925) and Hutchinson (1948) were removed from the bibliography with that change.
- Equality equilibria were distinguished from fixed-demand surplus no-conversion allocations, and deficit-side eigenvalues were distinguished from two-sided stability statements.
- The 20/40-year quality comparison was recast as cap-induced coincidence rather than general delay insensitivity.
- The recovery endpoint changed from 0.828 ha to 0.677 ha and the recovery fraction from 0.71 to 0.46 for the specified delayed-quality case. These are substantive numerical/reporting changes, not C14 page-shortening edits.
- Numerical-method, finite-step, quality-history and scope statements were expanded or changed.

### C11–C12 main

- Specific recovery-time examples were removed: approximately 30 years for forest half-recovery, 5.6 years for the specified collapsed-fish-stock comparison, and 17–23 years for soil-carbon adjustment. They were replaced with a heterogeneous-source qualification and a statement that no common curve or harmonized response times were refitted.
- Reserve-area and optional fast-area bounds were reclassified as monitored/inactive rather than enforced constraints.
- The rounded conversion increment changed from +0.784 to +0.785.
- A proposition/proof was qualified as pointwise: maintenance balance is not invariant during active conversion. Static observation identification was distinguished from possible dynamic identification using the quality equation.
- Assertions of continuity from a finite sampled grid were weakened to sampled monotonicity/no general continuity theorem.
- Debt equilibrium figures changed from approximately 1.19 and 5.38 to 1.209655 and 5.394538 using stated unrounded inputs and an explicit integration comparison.
- The additive-degradation comparator acquired a separate coefficient and units; its sustained-shortfall comparison was distinguished from a transient threshold.
- The minimum-area preservation argument was expanded; the aggregate-information limitation was distinguished from a universal control-impossibility statement.

### C10–C12 SI (intermediate C11 SI unavailable)

- Raw unconstrained delay characteristic-root discussion was replaced by constrained-quality and capacity-input-delay scope. Applicability of the scalar logistic delay criterion was withdrawn for the displayed population equation; the all-zero quality history was distinguished from positive-quality convergence.
- The debt Jacobian derivative changed from `-eta` alone to `alpha*b_f*A_f-eta`.
- Reserve and fast-area constraints were clarified, including monitored reserve minima rather than a blanket invariance claim.
- The restoration-gate comparison was identified as a non-equilibrium initial state in shortfall; initial supply, shortfall and separate reporting horizons were stated. One displayed minimum changed from 0.057 to 0.058.
- Detailed empirical recovery-time examples and their relationship to the model parameters were removed/reframed. See the complete SI diff for the exact text.

Some of these differences address documented scientific problems. This audit records them; it does not grant blanket permission to preserve or revert them without separating scientific corrections from unauthorized exposition cuts.

## 6. Follow-up F01–F02

The follow-up was extensively rewritten, not minimally copyedited.

- **Title:** “a boundary-matched test of composition masking” became “a boundary-matched empirical design.”
- **Presentation:** a working-manuscript byline and stage-status box were replaced by a conventional author/affiliation byline and article structure. The staged implementation table was removed. The manuscript continues to state that physical trends and account–asset outcomes were not estimated.
- **Prior-information disclosure:** the paragraph disclosing prior plans, world-level audits, and inspection of early Afghan historical rows was omitted. The `prior_information_disclosure` configuration field was also removed.
- **Design provenance:** `metadata/design_input_provenance.json` and the standalone protocol were not included in F02. They remain intact in F01. Absence from F02 is not deletion from the repository, but it removes relevant information from the new package.
- **Protocol commitments:** explicit language about documented amendments, blinded calibration and later classification thresholds was removed or compressed. General requirements for separate calibration/evaluation remain; the wording and procedural specificity changed.
- **AI declaration:** F01's statement about protocol/source inspection, code, tests and draft writing plus required author review was replaced with a shorter statement about source-document analysis, computational methods, verification and language editing. This is another declaration alteration.
- **Methods:** decomposition and cancellation definitions were reformatted and numbered; geographic, uncertainty and source-definition details were expanded in a newly supplied four-page SI. That SI did not exist in F01.
- **References:** the ECOMOD manuscript reference was added; other reference entries were expanded/corrected using DOI metadata. No existing F01 bibliography key was removed.
- **Figure and data labels:** the account-coverage figure's labels/title changed; “preflight pass” became “available account data.” Its explicit title qualification “not physical-data eligibility” was removed, although that limitation remains in the article and derived data.
- **Configuration and metadata:** status/module labels were rewritten and source-method finding-status fields were removed. Physical eligibility is still explicitly not evaluated; a zero eligible count is not an observed empirical rejection result.
- **Code/data boundaries:** the core `estimands.py` file is byte-identical. Availability criteria, source hashes, analysis windows, country candidates and the reported counts remain the same. Pipeline filenames and output-field names changed. Tests were renamed without changing their assertions. No physical biomass values, country stock trends, conversion associations or diagnostic-performance results were added.

## 7. What the earlier assurances failed to establish

The checks previously reported covered selected numerical files, computation, references and compilation. They did not constitute an exhaustive audit of author-controlled declarations, preservation of pedagogy, every printed mathematical symbol, all prior revisions or empirical figure validity. Presenting numerical integrity and a clean build as sufficient assurance was inadequate.

The evidence here supports specific findings, not “nothing else changed.” The complete supplied diffs permit inspection beyond this summary. No version has been silently repaired or republished as part of this audit.

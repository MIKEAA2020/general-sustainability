# DOI-link audit: ECOMOD C17 and empirical follow-up F10 — R01

Checked 29 October 2026. This is a citation/update map, not a manuscript revision. No historical source/PDF, companion paper or branch was modified or merged.

## Scope and verified current source

Inspected the current `main` repository's ECOMOD C17 main/SI sources and the published F10 main source. There are **five GitHub-only companion-manuscript links in C17** (three main, two SI), plus **one ECOMOD manuscript citation in F10**. Code/data availability links are separate and should not be indiscriminately replaced.

C17 source Git blobs:

- `batch 9/agent 2/ecomod_c17/ecomod_C17_main.tex`: `391b680cc6f189071b59521d87284216dfdcbd4e`.
- `batch 9/agent 2/ecomod_c17/ecomod_C17_SI.tex`: `ba9944c9fc7ca59822a5cf66a5810c0f58c10433`.

## 1. Exact citation-update map

| Current reference / location | Deposited paper and preferred DOI | Necessary qualification |
|---|---|---|
| `Abaee2026a`: governance-delay companion; C17 main line 576 and SI line 690. Currently links GitHub `paper4_delay_dynamics_v41.pdf`. | **Delay-Induced Regime Change in Harvested Stocks: The Mobilising and Protective Channels of Institutional Feedback, and the Review Interval as Control**. https://doi.org/10.5281/zenodo.22554217 | Deposit is v1 and contains `paper4_delay_dynamics_v30.pdf`, not the cited GitHub v41. Use the deposited title/version if its content supports the cited statements; otherwise deposit the intended later revision. Do not retain a later title/version while silently pointing to the earlier PDF. |
| `Abaee2026b`: transition-assessment/separation companion; C17 main line 577 and SI line 691. Currently links GitHub `paper06_assessment_separation_v71.pdf`. | **Transition Certification with Composite Indices: The Acceptance Gap Between Compensatory and Noncompensatory Rules**. Author-supplied DOI: https://doi.org/10.20944/preprints202610.2983.v1 . Publisher landing page: https://www.preprints.org/manuscript/202610.2983/v1 | Publisher page confirms Amin Abaee, title, version 1, posted 29 October 2026. The supplied DOI returned DOI Not Found, and an exact Crossref lookup returned 404 during this audit; this could be registration/propagation timing and is not proof the author-supplied identifier is wrong. Confirm DOI resolution before finalizing. The cited Sections 2/4 and Theorems 2/4(iii) must be checked against the deposited version, not assumed to retain the numbering/content of GitHub v71. |
| `Abaee2026c`: typed-ledger companion; C17 main line 578. Currently links GitHub `paper3_material_ledgers_v50.pdf`. | **Typed Flux Ledgers and Depletion Arithmetic: Conservation, Componentwise Diagnostics, and the Semantics of Depletion Horizons**. Version-specific DOI: https://doi.org/10.6084/m9.figshare.33942451.v1 . General DOI supplied by author: https://doi.org/10.6084/m9.figshare.33942451 | Public Figshare API confirms version 1 and its version-specific DOI. Files are `paper3_material_ledgers_v49.pdf` and `paper3_supplementary_v18.pdf`, not cited GitHub v50. Verify the cited Sections 1.1 and 10.1 against that deposit or archive the later revision. |
| `Abaee2026`: ECOMOD citation in F10 main line 217. Currently links GitHub `ecomod_c17`. | Earlier ECOMOD deposit: **How Aggregation Can Conceal Composition: Aggregate Biocapacity and the Identifiability of Modelled Ecological-Capital Drawdown**. https://doi.org/10.5281/zenodo.22554480 | Author correctly identified this as an earlier version. Deposit v1 contains `manuscript_ECOMOD_v35.pdf` and `.tex`, not C17. Do not relabel it as the deposited C17 manuscript. Prefer a DOI for the intended current ECOMOD revision; otherwise cite the earlier deposited title/version explicitly where it supports the claim and distinguish current source/code access. |

The cleaned DOI URLs above omit malformed nested Markdown and sentence-ending punctuation from the user's pasted links.

## 2. Additional deposit not in the supplied list

An earlier assessment/separation deposit was located and verified:

- **The Limits of Compensatory Aggregation: A Formal Separation of Weak and Strong Sustainability Assessment**.
- https://doi.org/10.5281/zenodo.22545740 .
- Published 6 September 2026, version v1; files `paper1_assessment_separation_v22.pdf` and `paper1_supplementary_v3.md`.
- Concept DOI: https://doi.org/10.5281/zenodo.22545739 .

This is an earlier related assessment/separation paper, not a reason to add an unrelated fourth companion citation. It is useful for version history or if a specific cited result belongs to that deposited text. It should not be substituted automatically for the newer Preprints.org manuscript and its version-specific theorem references.

## 3. Missing or unverified links that still need attention

1. **A DOI for the intended current ECOMOD/C17 version.** The supplied ECOMOD DOI identifies v35. No DOI identifying the current C17 source was verified in this targeted audit.
2. **A DOI identifying the intended later governance/ledger versions**, if C17 depends on content changed after deposited governance v30 or ledger v49. Existing deposits can be cited if their actual content suffices; otherwise update the deposits through legitimate new-version workflows.
3. **Working resolution of the new Preprints.org DOI**, plus checking its section/theorem numbering before updating `Abaee2026b`.
4. **An archival DOI for F10**, if it is to be cited elsewhere as a deposited manuscript. No F10 deposit DOI was supplied or verified here; its current GitHub package remains an implementation/source location.

The three companion families cited in C17 are all represented by the user's supplied links. The principal omissions are version-matched identifiers, not necessarily additional papers. This was a targeted audit, not a claim that no other deposits exist.

## 4. Links to retain as implementation access

- C17 main line 566: GitHub data/code availability for `ecomod_c17`.
- F10 main line 211: GitHub data/code availability for `ecomod_empirical_followup/F10`.
- Corresponding SI implementation/provenance links and code/data source URLs where applicable.

These can remain as live development/source links alongside archival DOIs. A manuscript deposit does not necessarily archive its complete executable data/code package. In particular, the supplied earlier ECOMOD deposit is not an archive of C17's current computational artifacts.

Use DOI landing pages as the primary bibliographic identifiers; keep GitHub as a clearly labelled implementation/supplementary source where needed. Use version-specific DOIs for claims checked against a particular text. Concept/general DOIs may support discoverability/version history but should not conceal which version supports section- or theorem-specific citations.

## 5. Citation labels and status

- Replace generic “Working paper. Manuscript [GitHub]” wording with accurate deposited-preprint metadata and the deposited title.
- Do not describe any of these deposits as peer-reviewed publications merely because they have DOIs.
- `2026a/b/c` currently identifies governance/assessment/ledger. If the bibliography is reordered under journal style, update author-year suffixes consistently through main and SI; preserve citation keys or document any controlled key changes.
- Do not overwrite C17/F10 merely to patch historical artifacts. Apply approved citation corrections in a new version and verify both visible bibliography text and PDF hyperlink targets.

## Verification sources

- Figshare public API: https://api.figshare.com/v2/articles/33942451 . Confirms deposited title, v1 DOI and file names; HTML landing page returned 403 through one access route.
- Governance Zenodo API: https://zenodo.org/api/records/22554217 . Its latest-version endpoint still identified record 22554217 during the check.
- ECOMOD Zenodo API: https://zenodo.org/api/records/22554480 . Its latest-version endpoint still identified record 22554480 during the check.
- Earlier assessment API: https://zenodo.org/api/records/22545740 .
- New assessment publisher page: https://www.preprints.org/manuscript/202610.2983/v1 . Accessible through page retrieval; one direct HTTP route returned 403. DOI and Crossref lookup failure are recorded separately from the successful publisher-title verification.

This record identifies where citations should change and where content/version checks remain necessary. It does not claim those checks have already established equivalence between the newer GitHub manuscripts and older deposits.

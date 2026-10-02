# Preprints.org author-review package — 2 October 2026

**Prepared, not posted or submitted.** The author must review the PDFs, approve the metadata and rights/CC BY 4.0 declarations, and use their own Preprints.org/MDPI account. No DOI or portal record has been created.

| Manuscript | Article PDF to review/upload | Standalone LaTeX source archive | Other upload |
|---|---|---|---|
| **03 — computational viability, v22** | [14-page article PDF](content_audit/journal_submission/preprints_org_ready_2026-10-02/paper03/paper03_computational_certification_v22.pdf) | [source + two figures + supplement TeX (.zip)](content_audit/journal_submission/preprints_org_ready_2026-10-02/paper03/paper03_computational_certification_v22_latex_source.zip) | [4-page supplement PDF](content_audit/journal_submission/preprints_org_ready_2026-10-02/paper03/paper03_computational_certification_v22_supplementary.pdf) |
| **09 — conditional cod/Edwards certification, v41** | [52-page article PDF](content_audit/journal_submission/preprints_org_ready_2026-10-02/paper09/paper09_cod_certification_v41.pdf) | [source + eleven figures (.zip)](content_audit/journal_submission/preprints_org_ready_2026-10-02/paper09/paper09_cod_certification_v41_latex_source.zip) | [linked methods and limitations audit](CONDITIONAL_MODEL_CLASS_AND_ERROR_SCOPE_2026-10-02.md) |

**Build integrity:** Each source ZIP was extracted into an empty directory and compiled without missing figures or TeX dependencies; the resulting PDF text and page count matched the staged upload PDF ([build verification](content_audit/journal_submission/preprints_org_ready_2026-10-02/BUILD_VERIFICATION.log)). SHA-256 manifests are in each package folder. Compilation is not proof review. Paper09 Table 1 still passes all 78 displayed cells ([check](content_audit/revision_pair_cod_2026-10-02/TABLE09V41.log)). Paper03's pair proof has only been internally checked; it has **not** received an independent referee read or Lean formalization.

## Metadata for author confirmation

| Field | 03 | 09 |
|---|---|---|
| Title | *Computational Viability Certification under Incomplete Observation: A Continuous-to-Finite Bridge with Exact Certificates, a Solver-Assisted Certified Campaign, and a Finite-Side Reference Library* | *Certification, not simulation: the viability of harvest rules on two real resource systems, and the horizon of what can be certified* |
| Article type suggestion | Research article | Research article |
| Author (from manuscripts; confirm) | Amin Abaee | Amin Abaee |
| Affiliation (from manuscripts; confirm) | Independent Researcher | Independent Researcher |
| Corresponding contact (from manuscripts; confirm) | amin_abaee@ut.ac.ir | amin_abaee@ut.ac.ir |
| ORCID (from manuscripts; confirm) | 0000-0002-0019-1842 | 0000-0002-0019-1842 |
| Keywords (from manuscripts) | viability; incomplete observation; obstruction certificates; linear programming; delayed observation; exact arithmetic; certified computation | viability certification; Northern cod; Edwards Aquifer; harvest rules; feedback; uncertainty sensitivity |
| Portal abstract | Use the article's first-page abstract, **not** the supplementary material's title page | Use the **short composite first-page abstract**, not either System I/II authored lead-in abstract |
| Funding/conflict statements | Manuscript says none; author to confirm | Manuscript says no external funding or conflict; author to confirm |
| Data/code | Manuscript declares no external data and cites repository code | Manuscript cites source data/code and a pinned reproducibility record; author to confirm rights and accessibility |

Both article PDFs place title, author, affiliation, corresponding address, abstract and keywords on **page 1**. The part-level abstracts in 09 were **retained** after the composite abstract; they are not replacements for the portal abstract. Conflict statements were placed directly before the references, as Preprints.org requests; author confirmation of their truth is still necessary. The manuscripts already contain AI-use declarations, but the author should verify whether they accurately describe **all** AI assistance and whether the platform wants any additional Methods or portal-field disclosure.

## Checks the author must decide before uploading

1. **Scientific sign-off.** Read the exact pair proof in 03, including the all-measurable-control argument. A preprint is not externally refereed; do not say that this proof has been independently validated. In 09, the proposition is a *local LRP* condition for a fixed q10 floor, not a global all-state protection theorem. The epsilon table assumes an imposed uniform defect; ACI/EnbPI-style diagnostics in the linked audit do not create one. The fixed-floor F-cut is an approximate conditional region, and a posterior HPD is a credible region, not a frequentist confidence set.
2. **Authorship and declarations.** Confirm name, affiliation/contact, ORCID, sole authorship, funding, conflicts, AI-tool declaration, and permissions for all eleven 09 figure files/two 03 figures and for underlying data. Do not treat an archived figure or external assessment record as automatically relicensed.
3. **Rights/policy.** Preprints.org posts under **CC BY 4.0**, expects rights to all uploaded material, asks authors to check target-journal preprint policies, and warns that a posted preprint cannot normally be completely removed [1]. Author consent to those terms is **not** inferred from preparation of this package.
4. **Linked material.** Verify that the pinned Git repository URLs and cited external studies resolve for the public without credentials. The 09 main text links to the audit at an immutable repository revision; the new v41 source and package will be deposited separately. Decide whether the separately titled 09b companion should also be posted as its own preprint; it is *not* silently bundled as a second article here.
5. **Portal work.** Preprints.org asks for title, abstract, keywords, author details, manuscript source, all figures and supplementary files; a LaTeX ZIP is appropriate [1,2]. The author must select categories and accept any license/withdrawal terms in their account. This workspace contains no portal login and makes no claim of acceptance, publication, or DOI.

### Platform references

[1](https://www.preprints.org/instructions-for-authors) Preprints.org, *Instructions for Authors*, viewed 2 October 2026 (first-page metadata, complete LaTeX source, permissions, COI placement, data, CC BY 4.0 and withdrawal policy).

[2](https://www.preprints.org/blog/post/submit-a-preprint) Preprints.org, *How Do I Submit a Preprint?* (portal fields, supplementary files and account requirement).

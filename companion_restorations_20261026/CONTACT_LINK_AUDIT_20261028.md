# Contact-link audit — 2026-10-28

This audit covers the current working papers in scope and their available supplementary files. Historical releases are left unchanged.

| Paper/file | Email link | ORCID link | Result |
|---|---|---|---|
| ECOMOD Continued 11 main PDF | `mailto:amin_abaee@ut.ac.ir` | `https://orcid.org/0000-0002-0019-1842` | Both valid PDF annotations; 35 pages. |
| ECOMOD Continued 11 SI PDF | `mailto:amin_abaee@ut.ac.ir` | `https://orcid.org/0000-0002-0019-1842` | Both valid PDF annotations; SI ORCID is present; 21 pages. |
| Paper06 v77 main PDF | `mailto:amin_abaee@ut.ac.ir` | `https://orcid.org/0000-0002-0019-1842` | Both valid PDF annotations; 46 pages. |
| Paper06 v77 SI PDF | `mailto:amin_abaee@ut.ac.ir` | `https://orcid.org/0000-0002-0019-1842` | Both valid PDF annotations; SI ORCID is present; 25 pages. |
| Paper4 v42 existing PDF | `mailto:amin_abaee@ut.ac.ir` | `https://orcid.org/0000-0002-0019-1842` | Both valid annotations in the existing 45-page PDF. No separate SI PDF was found. |
| Paper3 v54 original PDF | Email annotation is valid. | The original annotation URI was malformed because `\allowbreak{}` was embedded in the ORCID destination. | Original v54 source/PDF preserved unchanged. A separate local contact-link repair copy was built and verified. |
| Paper3 v54 local contact-link repair | `mailto:amin_abaee@ut.ac.ir` | `https://orcid.org/0000-0002-0019-1842` | Both valid annotations in a 54-page PDF. The one-line source repair and evidence are in `Paper3_v54_contactlink_repair_20261028/`. |
| Paper8 v47 TeX source | `\href{mailto:amin\_abaee@ut.ac.ir}{...}` | `\href{https://orcid.org/0000-0002-0019-1842}{...}` | Both links are present in source. No Paper8 PDF or separate SI PDF exists in the inspected workspace, so no PDF-level check was possible. |

`mutool show` was used for PDF annotation verification. The C11 and Paper06 rendered title pages were also visually checked; both show the linked email and ORCID. No separate SI PDFs were found for Paper3 v54, Paper4 v42, or Paper8 v47; C11 and Paper06 are the available SI PDFs in this working set, and both are verified above. No C10, C8/C9, Paper06 v75-or-earlier, Paper4 v42, or original Paper3 v54 release was changed by this audit. The current working snapshot was pushed to branch `agent/p06-ecomod-c11-local-draft-20261028`; no DOI deposit or publication was made.

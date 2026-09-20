# Paper 3 v1 (rev. 2) — change summary

Software description: *SafeTransition: exact rational certification of
transition safety for sustainability assessment* (EMS submission draft).

## Initial draft (v1)

- 8 pp, elsarticle `3p,11pt`; abstract 137 words (EMS limit 150); 3 figures
  (benchmark panel, readings, graphical abstract at 1328 x 531); QA table;
  5 highlights (<=85 chars each); S-Note supplementary (math digest, 24-check
  enumeration, artifact tree).
- Anatomy per the landmark style notes (Pywr/SPOTPY/SALib): decades-of-practice
  opening; fair classification of related tools with verified DOIs; gap as
  improvement; roadmap paragraph; availability fields per the EMS guide.
- QA at draft: compile exit 0; 0 `??`; overfull baseline 2.43 pt only; tone
  scan clean; all citations Crossref-verified (unverified candidate dropped;
  Raven author list corrected against Crossref before inclusion).

## Revision 2 (author corrections + style-guide completion)

1. ORCID and e-mail hyperlinks render visibly blue (`hypersetup`,
   `colorlinks`); all `href` links verified live in the PDF.
2. Remaining plan items assessed and implemented where warranted (see below).
3. Generative-AI declaration reworded to the author's exact text: "Deepseek
   AI and Qwen (Alibaba) assisted with code development. The author reviewed
   and edited the content as needed and takes responsibility for the
   content."
4. Section 6 reflowed from an `itemize` (long labels overran the text
   width) to a labelled availability table; block-level width audit confirms
   no text block crosses the body's right edge on any page.
5. Fig. 2(b): FP-witness label shortened and repositioned right of the
   kappa* line, clear of the black curve and left of the dashed x = 1
   guide; regenerated from the same exact values.
6. CRediT statement uses initials: "A.A.".
7. Style-guide completion: the availability table now names the pinned
   third-party distributions in the deposit (verifiability of the
   environment claim), and Section 4.2 gains one reviewer-perspective
   sentence ("From the reviewer's perspective this means..."), the
   Pywr-idiomatic device. Deliberately not imported from the landmarks:
   "novel" and changelog-flavoured "currently contains" phrasing (excluded
   by the standing tone rules).

## Still open before submission (not manuscript defects)

- Figshare deposit NEW VERSION adding `safetransition/` (same item, DOI
  stable) — submission requirement "software availability" is otherwise met.
- Cover letter at submission time; graphical abstract TIFF/EPS export if
  requested by the portal (PNG at spec is accepted by SFINCS-style portals;
  EMS prefers TIFF/EPS/PDF/Office).
- "Adoption and penetration" statement: cannot be claimed pre-publication;
  the manuscript limits itself to factual availability and test coverage.

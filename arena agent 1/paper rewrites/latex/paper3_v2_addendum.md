# Paper 3 v2 — change summary (revision of v1; v1 preserved unchanged)

## Version-ledger repair

The revision was initially pushed over the v1 files, violating the
standing new-version rule. Repair: the original v1 (tex and PDF) was
recovered byte-exact from the repository's first-push commit and restored
at the v1 paths; the revision now lives as new v2 files. v1 and v2 are
both in the repository; nothing further is overwritten.

## v1 (original draft, restored)

- 8 pp, 2 figures in-PDF; abstract 137 words; itemize-format availability
  section; AI declaration in the "During the preparation of this work"
  form; CRediT with full name; hyperlinks rendered in plain black.

## v2 (this version)

1. Hyperlinks visible: `\hypersetup{colorlinks}` — ORCID and e-mail render
   blue and are live in the PDF.
2. Author corrections: generative-AI declaration reworded to the author's
   exact text (Deepseek AI and Qwen (Alibaba) assisted with code
   development; the author reviewed and edited the content as needed and
   takes responsibility for the content); CRediT uses initials "A.A.".
3. Section 6 reflowed from an itemize (long labels exceeded the text
   width) to a labelled availability table; block-level width audit
   confirms no text block crosses the body's right edge on any page.
4. Fig. 2(b): FP-witness label shortened and repositioned right of the
   kappa* line, clear of the curve and left of the dashed guide;
   regenerated from the same exact values.
5. Style-guide completion: the availability table notes that pinned
   third-party distributions are listed in the verification deposit
   (backed by `requirements-figures.txt`, package 1.1.0); one
   reviewer-perspective sentence added in Section 4.2.

## QA

v2: compile exit 0; 8 pp; 2 images; 0 `??`; overfull 2.43 pt baseline only;
abstract unchanged (137 words); all citations resolve.

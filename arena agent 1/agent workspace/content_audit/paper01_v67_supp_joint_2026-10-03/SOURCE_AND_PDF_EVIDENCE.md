# Source and PDF extraction evidence — Paper01 v67 supplement

This record compares **the same SHA-256-pinned PDF** with two named text extractors and its LaTeX source. A different uploaded PDF build could differ; supply its bytes/hash to compare. Source/render findings here do not validate mathematical proofs.

- Supplement PDF: `paper 2 family/01_obstruction/paper01_obstruction_calculus_v67_supplementary.pdf` · SHA-256 `9f3c212bafb54437965f9906fdecec185bd173bbb64cb0119ee6674c962640da` · 21 pages.
- Supplement source: `paper 2 family/01_obstruction/paper01_obstruction_calculus_v67_supplementary.tex` · SHA-256 `99819f72de9c85570ab2daa2f8610ca5c1e8fb703d0a5be8c593b08f2022ce62`.
- Main source: `paper 2 family/01_obstruction/paper01_obstruction_calculus_v67.tex` · SHA-256 `4f5cc909e9035319e7056d9d9b8d64f60285d9a68bcf801cf5b8154aff9fad39`.
- Extractors: **pdftotext version 25.03.0**, invoked as `pdftotext -f PAGE -l PAGE -layout`; **PyMuPDF 1.28.2**, `Page.get_text(sort=True)`. Also visually rasterized pages 8, 9, 16 and 19 with Poppler `pdftoppm` and inspected them; images are scratch, not pushed.

## Representative continuous passages on disputed PDF pages 8 and 9

**Supplement PDF p. 8:**

- **Poppler:** “That same scenario is admissible against every policy; attainment of the infimum is unnecessary.”
- **PyMuPDF:** “That same scenario is admissible against every policy; attainment of the infimum is unnecessary.”
- Extracted lengths: Poppler 4,440 characters; PyMuPDF 4,416 characters. Both pages also passed a direct visual check: equations and successive paragraphs are visible, not repeated `1`s.

**Supplement PDF p. 9:**

- **Poppler:** “Complete discussion of the obstruction ladder (main text, Section 3). The rungs of”
- **PyMuPDF:** “Complete discussion of the obstruction ladder (main text, Section 3). The rungs of”
- Extracted lengths: Poppler 4,216 characters; PyMuPDF 4,048 characters. Both pages also passed a direct visual check: equations and successive paragraphs are visible, not repeated `1`s.

## Exact source lines for the disputed symbols

| Source line | Verbatim TeX | Interpretation |
|---|---|---|
| Supplement `paper01_obstruction_calculus_v67_supplementary.tex:413` | `\[\mathcal{Y}_{\mathrm{safe}} \;=\; \big\{ y \in O(Z) : O^{-1}(y) \subseteq K \big\}.\]` | Supplement Corollary 1: Y-safe, not V-safe; main article line 1461 has the same macro. |
| Supplement `paper01_obstruction_calculus_v67_supplementary.tex:820` | `\textbf{(a) Veliov's output-feedback condition.} Veliov (1993) considers the same problem as Section 3 (a tube in the state space under incomplete and inexact measurement) and gives a sufficient condition for the` | The S2 heading has Veliov, not Velivor. |
| Supplement `paper01_obstruction_calculus_v67_supplementary.tex:1021` | `\(\big(\dot S_1, \dot S_2\big)\big|_{p^*} = \left(\tfrac{\kappa}{2}(C_2 - C_1), \tfrac{\kappa}{2}(C_1 - C_2)\right) \ne 0.\)` | A.2 uses κ/2, not π/2. |
| Supplement `paper01_obstruction_calculus_v67_supplementary.tex:1317` | `Sontag, E.D.: Mathematical Control Theory: Deterministic Finite Dimensional Systems, 2nd edn. Springer, New York (1998)` | Reference name is Sontag, not Sentag. |
| Supplement `paper01_obstruction_calculus_v67_supplementary.tex:1319` | `Veliov, V.M.: Sufficient conditions for viability under imperfect` | Reference name is Veliov, not Veliv. |
| Supplement `paper01_obstruction_calculus_v67_supplementary.tex:1203` | `Now take the injective, biased observation \(\hat S = S + b\) with` | Biased observation is hat S. |
| Supplement `paper01_obstruction_calculus_v67_supplementary.tex:1206` | `observation, \(u = g(\hat S) = g(S + b)\). Then` | Controller reads hat S. |
| Supplement `paper01_obstruction_calculus_v67_supplementary.tex:1207` | `\[\dot S = g(S + b) - g(S) > 0 \qquad \forall S,\]` | Dot S is the state derivative, not the name of the observation. |
| Supplement `paper01_obstruction_calculus_v67_supplementary.tex:484` | `(main text, Section 3; Proposition prop:helly).}` | This is a genuine raw label in the supplement. |
| Supplement `paper01_obstruction_calculus_v67_supplementary.tex:654` | `for infinite beliefs a finite-witness reduction is not automatic --- the Helly-type witness of Proposition prop:helly of the main text (Section 3.4) supplies one under the convexity hypotheses stated in Section 3.4. The worked instance of this certificate --- the two-floor pair with multiplier \(\lambda = (1/2, 1/2)\) and margin \(1/10\) --- is carried in the worked certificates below.` | Second genuine occurrence of that raw label. |
| Main `paper01_obstruction_calculus_v67.tex:1461` | `\[\mathcal{Y}_{\mathrm{safe}} \;=\; \big\{ y \in O(Z) : O^{-1}(y) \subseteq K \big\}.\]` | Main safe-observation notation agrees with supplement 413. |
| Main `paper01_obstruction_calculus_v67.tex:994` | `\begin{proposition}[sparse common-action witness]\label{calc-prop:helly}` | The article defines a functioning Helly label, unlike the supplement raw strings. |

## Primary-source cross-check and falsifiability boundary

- Reproduce from repository root with `python3 content_audit/paper01_v67_supp_joint_2026-10-03/capture_pdf_evidence.py` after installing Poppler (`pdftotext`) and `PyMuPDF`; the script **refuses** different source/PDF hashes.
- `pdf p. 19` visibly distinguishes the hatted reading from the dotted derivative (the glyph extraction may lose accents). Supplement source lines 1203/1206/1207 settle which macro was actually compiled.
- The source/PDF evidence supports **false for this pinned v67 artifact**, not a claim about a different or unknown PDF build. If a reviewer supplies a PDF whose SHA-256 differs, re-run these tests on that build before dismissing its observation.
- `Proposition prop:helly` is **not** an OCR artifact. The main article defines `\label{calc-prop:helly}` and uses `\ref{calc-prop:helly}`; supplement lines 484/654 are literal text, not functioning cross-references. Check both PDFs after replacing the supplement text with an article-specific reference.


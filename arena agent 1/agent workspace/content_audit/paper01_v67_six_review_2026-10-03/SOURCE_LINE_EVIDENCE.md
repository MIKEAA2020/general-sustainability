# Pinned v67 source quotations for the six-review report

These are **raw TeX-file** SHA-256 hashes (`sha256sum FILE` on the individual bytes), not a project/tarball digest. The script asserts the hashes before reading. This establishes source content, **not** the truth of a theorem. Source files and PDFs remain untouched.

| Artifact | SHA-256 |
|---|---|
| `paper01_obstruction_calculus_v65.tex` | `57cbbd95367314d1e43fd69e3dcda1e2800746b722020488925841ed5670bc0e` |
| `paper01_obstruction_calculus_v65_supplementary.tex` | `112cd44cce57ac39a1cab77240dd05789e01f7bb0d8c5cd410d35c80b47e0d24` |
| `paper01_obstruction_calculus_v66_supplementary.tex` | `99819f72de9c85570ab2daa2f8610ca5c1e8fb703d0a5be8c593b08f2022ce62` |
| `paper01_obstruction_calculus_v67.tex` | `4f5cc909e9035319e7056d9d9b8d64f60285d9a68bcf801cf5b8154aff9fad39` |
| `paper01_obstruction_calculus_v67_supplementary.tex` | `99819f72de9c85570ab2daa2f8610ca5c1e8fb703d0a5be8c593b08f2022ce62` |
| `paper01_obstruction_calculus_v67.pdf` | `95904c62c4b4f5d618e992a6f5e522a510ff6bd154bfff7653359f834c7f4bb2` |

The v66 and v67 supplement `.tex` files are **byte-for-byte identical**; both differ from the v65 supplement. The v65 article hash also differs from v67. These results agree with the earlier [layout/review map](../../PAPER01_V67_LAYOUT_AND_REVIEW_MAP_2026-10-03.md).

## One-line source quotations

| Source file and line | Verbatim TeX line | What it establishes |
|---|---|---|
| `paper01_obstruction_calculus_v67.tex:375` | `\(\mathcal{R}_{\mathcal{V}}(x) = U(x)\). Two levels of the tangency condition are distinguished throughout. (i) \emph{Local reading.} The correspondence is applied to the constraint set itself: by Nagumo's theorem (Nagumo, 1942) in its robust form, if \(\mathcal{V}\) is closed and` | Nagumo, not Nagumoy |
| `paper01_obstruction_calculus_v67.tex:490` | `\(\mathcal{I} = (Y, O)\) with observation map \(O : X \to Y\); the` | observation structure is calligraphic I, not Game |
| `paper01_obstruction_calculus_v67.tex:951` | `Two branches share \(z^{+} = \tfrac{9}{10} z \pm u\) from a common \(z_{0}\), floor` | Example 2 base, not 5/10 |
| `paper01_obstruction_calculus_v67.tex:953` | `\(z^{+}_{k} + z^{-}_{k} = 2 (\tfrac{9}{10})^{k} z_{0}\) is invariant under the control, so both` | Example 2 recurrence |
| `paper01_obstruction_calculus_v67.tex:1298` | `The cap sum is the affine function \(\tfrac{67}{25}-\tfrac{Y-2}{5}\), which equals \(2\) at` | aggregate cap sum |
| `paper01_obstruction_calculus_v67.tex:1307` | `\lambda^{\top}(\mathrm{cap}-u)\;\le\;\tfrac{\mathrm{cap}_1(Y)+\mathrm{cap}_2(Y)}{2}-1` | dual half-factor |
| `paper01_obstruction_calculus_v67.tex:1461` | `\[\mathcal{Y}_{\mathrm{safe}} \;=\; \big\{ y \in O(Z) : O^{-1}(y) \subseteq K \big\}.\]` | certainly-safe symbol |
| `paper01_obstruction_calculus_v67.tex:1488` | `Now take the injective, biased observation \(\hat S = S + b\) with` | reading is hat S |
| `paper01_obstruction_calculus_v67.tex:1492` | `\[\dot S = g(S + b) - g(S) > 0 \qquad \forall S,\]` | derivative is dot S |
| `paper01_obstruction_calculus_v67.tex:1521` | `\textbf{(a) Veliov's output-feedback condition.} Veliov (1993) gives a sufficient condition for the existence of an output-feedback regulation map under incomplete and inexact measurement, reducing under perfect measurement to the classical viability condition (Haddad, 1981). Veliov's theorem certifies existence; the obstruction calculus certifies nonexistence; a problem satisfying neither requires a stronger observer or a finer observation structure.` | literature name is Veliov |
| `paper01_obstruction_calculus_v67_supplementary.tex:413` | `\[\mathcal{Y}_{\mathrm{safe}} \;=\; \big\{ y \in O(Z) : O^{-1}(y) \subseteq K \big\}.\]` | same safe symbol |
| `paper01_obstruction_calculus_v67_supplementary.tex:820` | `\textbf{(a) Veliov's output-feedback condition.} Veliov (1993) considers the same problem as Section 3 (a tube in the state space under incomplete and inexact measurement) and gives a sufficient condition for the` | literature name is Veliov |
| `paper01_obstruction_calculus_v67_supplementary.tex:1021` | `\(\big(\dot S_1, \dot S_2\big)\big|_{p^*} = \left(\tfrac{\kappa}{2}(C_2 - C_1), \tfrac{\kappa}{2}(C_1 - C_2)\right) \ne 0.\)` | kappa, not pi |
| `paper01_obstruction_calculus_v67_supplementary.tex:1203` | `Now take the injective, biased observation \(\hat S = S + b\) with` | reading is hat S |
| `paper01_obstruction_calculus_v67_supplementary.tex:1207` | `\[\dot S = g(S + b) - g(S) > 0 \qquad \forall S,\]` | derivative is dot S |
| `paper01_obstruction_calculus_v67_supplementary.tex:1317` | `Sontag, E.D.: Mathematical Control Theory: Deterministic Finite Dimensional Systems, 2nd edn. Springer, New York (1998)` | reference is Sontag |
| `paper01_obstruction_calculus_v67_supplementary.tex:1319` | `Veliov, V.M.: Sufficient conditions for viability under imperfect` | reference is Veliov |

## Negative-token inventory and limits

A one-line quotation cannot prove a token is absent *throughout* a file. The script checks that **neither pinned v67 `.tex` file** contains the exact tokens `\Game`, `Nagumoy`, `Empitied`, `Velivor`, `Sentag`, `\mathcal{V}_{\mathrm{safe}}`, `\tfrac{\pi}{2}` or `\dot S = S + b`. Equivalent spelling variants or a different PDF are not covered by this literal search. The positive source quotations above show the intended notation and names.

Reviewer-artifact extraction software and underlying bytes are **unknown**. The separate [source-and-PDF record](../paper01_v67_supp_joint_2026-10-03/SOURCE_AND_PDF_EVIDENCE.md) documents Poppler `pdftotext` 25.03.0 and PyMuPDF 1.28.2 checks on the pinned *supplement* PDF; it does not identify or reproduce the reviewer’s tool.

Reproduce with `python3 content_audit/paper01_v67_six_review_2026-10-03/capture_source_lines.py`. A differently hashed source or PDF requires separate adjudication.


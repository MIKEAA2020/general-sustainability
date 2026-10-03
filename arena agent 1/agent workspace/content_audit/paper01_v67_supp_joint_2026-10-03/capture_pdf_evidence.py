#!/usr/bin/env python3
"""Reproduce source/PDF evidence for v67 supplement disputed extraction claims.
Read-only; input is the frozen 21-page v67 supplementary PDF and TeX.
Writes short, shareable source snippets and independent Poppler/PyMuPDF excerpts.
"""
from pathlib import Path
from hashlib import sha256
import subprocess
import pymupdf
R=Path(__file__).resolve().parents[2]
D=R/'paper 2 family/01_obstruction'
SRC=D/'paper01_obstruction_calculus_v67_supplementary.tex'
PDF=D/'paper01_obstruction_calculus_v67_supplementary.pdf'
MAIN=D/'paper01_obstruction_calculus_v67.tex'
s=SRC.read_text().splitlines()
a=MAIN.read_text().splitlines()
assert sha256(PDF.read_bytes()).hexdigest()=='9f3c212bafb54437965f9906fdecec185bd173bbb64cb0119ee6674c962640da'
assert sha256(SRC.read_bytes()).hexdigest()=='99819f72de9c85570ab2daa2f8610ca5c1e8fb703d0a5be8c593b08f2022ce62'
assert sha256(MAIN.read_bytes()).hexdigest()=='4f5cc909e9035319e7056d9d9b8d64f60285d9a68bcf801cf5b8154aff9fad39'
ver=subprocess.run(['pdftotext','-v'],capture_output=True,text=True,check=True).stderr.splitlines()[0]
doc=pymupdf.open(PDF)
assert len(doc)==21
L=['# Source and PDF extraction evidence — Paper01 v67 supplement','',
   'This record compares **the same SHA-256-pinned PDF** with two named text extractors and its LaTeX source. A different uploaded PDF build could differ; supply its bytes/hash to compare. Source/render findings here do not validate mathematical proofs.','',
   f'- Supplement PDF: `{PDF.relative_to(R)}` · SHA-256 `{sha256(PDF.read_bytes()).hexdigest()}` · 21 pages.',
   f'- Supplement source: `{SRC.relative_to(R)}` · SHA-256 `{sha256(SRC.read_bytes()).hexdigest()}`.',
   f'- Main source: `{MAIN.relative_to(R)}` · SHA-256 `{sha256(MAIN.read_bytes()).hexdigest()}`.',
   f'- Extractors: **{ver}**, invoked as `pdftotext -f PAGE -l PAGE -layout`; **PyMuPDF {pymupdf.VersionBind}**, `Page.get_text(sort=True)`. Also visually rasterized pages 8, 9, 16 and 19 with Poppler `pdftoppm` and inspected them; images are scratch, not pushed.','',
   '## Representative continuous passages on disputed PDF pages 8 and 9','']
for page,needle in ((8,'That same scenario is admissible'),(9,'Complete discussion of the obstruction ladder')):
    pop=subprocess.check_output(['pdftotext','-f',str(page),'-l',str(page),'-layout',str(PDF),'-'],text=True)
    mu=doc[page-1].get_text(sort=True)
    L += [f'**Supplement PDF p. {page}:**', '']
    for label,text in (('Poppler',pop),('PyMuPDF',mu)):
        found=[ln.strip() for ln in text.splitlines() if needle.lower() in ln.lower()]
        assert found,(page,label,needle)
        L += [f'- **{label}:** “{found[0]}”']
    L += [f'- Extracted lengths: Poppler {len(pop):,} characters; PyMuPDF {len(mu):,} characters. Both pages also passed a direct visual check: equations and successive paragraphs are visible, not repeated `1`s.','']
L += ['## Exact source lines for the disputed symbols','', '| Source line | Verbatim TeX | Interpretation |', '|---|---|---|']
items=[
(413,'\\mathcal{Y}_{\\mathrm{safe}}','Supplement Corollary 1: Y-safe, not V-safe; main article line 1461 has the same macro.'),
(820,"Veliov's output-feedback condition",'The S2 heading has Veliov, not Velivor.'),
(1021,'\\tfrac{\\kappa}{2}','A.2 uses κ/2, not π/2.'),
(1317,'Sontag, E.D.', 'Reference name is Sontag, not Sentag.'),
(1319,'Veliov, V.M.', 'Reference name is Veliov, not Veliv.'),
(1203,'\\hat S = S + b','Biased observation is hat S.'),
(1206,'g(\\hat S)','Controller reads hat S.'),
(1207,'\\dot S =','Dot S is the state derivative, not the name of the observation.'),
(484,'Proposition prop:helly','This is a genuine raw label in the supplement.'),
(654,'Proposition prop:helly','Second genuine occurrence of that raw label.')]
for n,token,meaning in items:
    assert token in s[n-1],(n,token,s[n-1])
    line=s[n-1].replace('`','\\`').strip()
    L.append(f'| Supplement `{SRC.name}:{n}` | `{line}` | {meaning} |')
assert '\\mathcal{Y}_{\\mathrm{safe}}' in a[1461-1]
assert '\\label{calc-prop:helly}' in a[994-1]
L += [f'| Main `{MAIN.name}:1461` | `{a[1460].strip()}` | Main safe-observation notation agrees with supplement 413. |',
      f'| Main `{MAIN.name}:994` | `{a[993].strip()}` | The article defines a functioning Helly label, unlike the supplement raw strings. |',
      '', '## Primary-source cross-check and falsifiability boundary','',
      '- Reproduce from repository root with `python3 content_audit/paper01_v67_supp_joint_2026-10-03/capture_pdf_evidence.py` after installing Poppler (`pdftotext`) and `PyMuPDF`; the script **refuses** different source/PDF hashes.',
      '- `pdf p. 19` visibly distinguishes the hatted reading from the dotted derivative (the glyph extraction may lose accents). Supplement source lines 1203/1206/1207 settle which macro was actually compiled.',
      '- The source/PDF evidence supports **false for this pinned v67 artifact**, not a claim about a different or unknown PDF build. If a reviewer supplies a PDF whose SHA-256 differs, re-run these tests on that build before dismissing its observation.',
      '- `Proposition prop:helly` is **not** an OCR artifact. The main article defines `\\label{calc-prop:helly}` and uses `\\ref{calc-prop:helly}`; supplement lines 484/654 are literal text, not functioning cross-references. Check both PDFs after replacing the supplement text with an article-specific reference.','']
MAIN_LABEL='\\label{calc-prop:helly}'
assert any(MAIN_LABEL in ln for ln in a)
assert not any('Velivor' in ln or 'Sentag' in ln or '\\Game' in ln for ln in s)
(R/'content_audit/paper01_v67_supp_joint_2026-10-03/SOURCE_AND_PDF_EVIDENCE.md').write_text('\n'.join(L)+'\n')
print('EVIDENCE_WRITTEN pages 8/9 Poppler/PyMuPDF, disputed source lines, PDF/SRC digests; main Helly label verified')

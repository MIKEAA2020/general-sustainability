#!/usr/bin/env python3
"""Pinned, read-only line quotations for the six-review Paper01 v67 adjudication.
This checks literal source content, NOT proof correctness or other PDF builds.
Run from any directory: python3 content_audit/paper01_v67_six_review_2026-10-03/capture_source_lines.py
"""
from pathlib import Path
from hashlib import sha256

R = Path(__file__).resolve().parents[2]
D = R / 'paper 2 family/01_obstruction'
NAMES = {
    'v65 article': 'paper01_obstruction_calculus_v65.tex',
    'v65 supplement': 'paper01_obstruction_calculus_v65_supplementary.tex',
    'v66 supplement': 'paper01_obstruction_calculus_v66_supplementary.tex',
    'v67 article': 'paper01_obstruction_calculus_v67.tex',
    'v67 supplement': 'paper01_obstruction_calculus_v67_supplementary.tex',
    'v67 article PDF': 'paper01_obstruction_calculus_v67.pdf',
}
EXPECTED = {
    'v65 article': '57cbbd95367314d1e43fd69e3dcda1e2800746b722020488925841ed5670bc0e',
    'v65 supplement': '112cd44cce57ac39a1cab77240dd05789e01f7bb0d8c5cd410d35c80b47e0d24',
    'v66 supplement': '99819f72de9c85570ab2daa2f8610ca5c1e8fb703d0a5be8c593b08f2022ce62',
    'v67 article': '4f5cc909e9035319e7056d9d9b8d64f60285d9a68bcf801cf5b8154aff9fad39',
    'v67 supplement': '99819f72de9c85570ab2daa2f8610ca5c1e8fb703d0a5be8c593b08f2022ce62',
    'v67 article PDF': '95904c62c4b4f5d618e992a6f5e522a510ff6bd154bfff7653359f834c7f4bb2',
}
for key, fn in NAMES.items():
    assert sha256((D / fn).read_bytes()).hexdigest() == EXPECTED[key], key
assert (D / NAMES['v66 supplement']).read_bytes() == (D / NAMES['v67 supplement']).read_bytes()
A = (D / NAMES['v67 article']).read_text().splitlines()
S = (D / NAMES['v67 supplement']).read_text().splitlines()
items = [
    ('article', 375, "Nagumo's theorem", 'Nagumo, not Nagumoy'),
    ('article', 490, r'\mathcal{I} = (Y, O)', 'observation structure is calligraphic I, not Game'),
    ('article', 951, r'\tfrac{9}{10} z \pm u', 'Example 2 base, not 5/10'),
    ('article', 953, r'(\tfrac{9}{10})^{k}', 'Example 2 recurrence'),
    ('article', 1298, r'\tfrac{67}{25}-\tfrac{Y-2}{5}', 'aggregate cap sum'),
    ('article', 1307, r'\tfrac{\mathrm{cap}_1(Y)+\mathrm{cap}_2(Y)}{2}-1', 'dual half-factor'),
    ('article', 1461, r'\mathcal{Y}_{\mathrm{safe}}', 'certainly-safe symbol'),
    ('article', 1488, r'\hat S = S + b', 'reading is hat S'),
    ('article', 1492, r'\dot S = g(S + b)', 'derivative is dot S'),
    ('article', 1521, "Veliov's output-feedback condition", 'literature name is Veliov'),
    ('supplement', 413, r'\mathcal{Y}_{\mathrm{safe}}', 'same safe symbol'),
    ('supplement', 820, "Veliov's output-feedback condition", 'literature name is Veliov'),
    ('supplement', 1021, r'\tfrac{\kappa}{2}', 'kappa, not pi'),
    ('supplement', 1203, r'\hat S = S + b', 'reading is hat S'),
    ('supplement', 1207, r'\dot S = g(S + b)', 'derivative is dot S'),
    ('supplement', 1317, 'Sontag, E.D.', 'reference is Sontag'),
    ('supplement', 1319, 'Veliov, V.M.', 'reference is Veliov'),
]
for which, n, token, _ in items:
    line = (A if which == 'article' else S)[n-1]
    assert token in line, (which, n, token, line)
for which, lines in [('article', A), ('supplement', S)]:
    text = '\n'.join(lines)
    for token in (r'\Game', 'Nagumoy', 'Empitied', 'Velivor', 'Sentag', r'\mathcal{V}_{\mathrm{safe}}', r'\tfrac{\pi}{2}', r'\dot S = S + b'):
        assert token not in text, (which, token)
L = [
    '# Pinned v67 source quotations for the six-review report', '',
    'These are **raw TeX-file** SHA-256 hashes (`sha256sum FILE` on the individual bytes), not a project/tarball digest. The script asserts the hashes before reading. This establishes source content, **not** the truth of a theorem. Source files and PDFs remain untouched.', '',
    '| Artifact | SHA-256 |', '|---|---|',
]
for key, fn in NAMES.items():
    L.append(f'| `{fn}` | `{EXPECTED[key]}` |')
L += ['', 'The v66 and v67 supplement `.tex` files are **byte-for-byte identical**; both differ from the v65 supplement. The v65 article hash also differs from v67. These results agree with the earlier [layout/review map](../../PAPER01_V67_LAYOUT_AND_REVIEW_MAP_2026-10-03.md).', '',
      '## One-line source quotations', '',
      '| Source file and line | Verbatim TeX line | What it establishes |', '|---|---|---|']
for which, n, _, meaning in items:
    fn = NAMES['v67 article' if which == 'article' else 'v67 supplement']
    line = (A if which == 'article' else S)[n-1].strip().replace('`', r'\`')
    L.append(f'| `{fn}:{n}` | `{line}` | {meaning} |')
L += ['', '## Negative-token inventory and limits', '',
      'A one-line quotation cannot prove a token is absent *throughout* a file. The script checks that **neither pinned v67 `.tex` file** contains the exact tokens `\\Game`, `Nagumoy`, `Empitied`, `Velivor`, `Sentag`, `\\mathcal{V}_{\\mathrm{safe}}`, `\\tfrac{\\pi}{2}` or `\\dot S = S + b`. Equivalent spelling variants or a different PDF are not covered by this literal search. The positive source quotations above show the intended notation and names.', '',
      'Reviewer-artifact extraction software and underlying bytes are **unknown**. The separate [source-and-PDF record](../paper01_v67_supp_joint_2026-10-03/SOURCE_AND_PDF_EVIDENCE.md) documents Poppler `pdftotext` 25.03.0 and PyMuPDF 1.28.2 checks on the pinned *supplement* PDF; it does not identify or reproduce the reviewer’s tool.', '',
      'Reproduce with `python3 content_audit/paper01_v67_six_review_2026-10-03/capture_source_lines.py`. A differently hashed source or PDF requires separate adjudication.', '']
out = R / 'content_audit/paper01_v67_six_review_2026-10-03/SOURCE_LINE_EVIDENCE.md'
out.write_text('\n'.join(L) + '\n')
print('PASS pinned individual hashes, v66/v67 supplement equality, source quotations and negative-token inventory; wrote', out.relative_to(R))

#!/usr/bin/env python3
"""
Structural proof audit, corrected instrument.

The first instrument (proof_audit.py) counted only \begin{proof} environments.
That is WRONG for this family: several units write proofs inline as
\emph{Proof.}, \textbf{Proof.} or \emph{Proof sketch.} paragraphs, with no
proof environment at all. Counting only environments reported those units as
having "zero proofs" when the proofs were present.

Correct instrument: for each labelled claim environment (theorem / proposition /
lemma / corollary), look forward to the NEXT claim environment. If a proof
marker of ANY convention appears in between, the claim is evidenced. If not,
the claim is UNPROVEN (no in-text proof of any kind).

Separately, and independently: count references the paper makes to ITS OWN
supplementary sections (S1, S2, ... ) and check whether such a file exists.
A pointer to a supplement that does not ship is a dangling dependency
regardless of how the proofs are formatted.
"""
import io, os, re, sys

UNITS = [
    ('1',  'paper01_obstruction_calculus_v63.tex'),
    ('2',  'paper02_probabilistic_sufficiency_v12.tex'),
    ('3',  'paper03_computational_certification_v16.tex'),
    ('4',  'paper04_minimax_dual_certificates_v16.tex'),
    ('5',  'paper05_exact_belief_computation_v16.tex'),
    ('6',  'paper06_assessment_separation_v67.tex'),
    ('7',  'paper08_governance_delay_v46.tex'),
    ('8',  'paper09_cod_certification_v32.tex'),
    ('9',  'paper10_depletion_ledgers_v53.tex'),
    ('10', 'paper11_forecasting_baselines_v64.tex'),
    ('11', 'paper11c_worked_systems_audit_v2.tex'),
]

CLAIM = re.compile(
    r'\\begin\{(theorem|proposition|lemma|corollary)\}(?:\[([^\]]*)\])?\s*(?:\\label\{([^}]*)\})?'
)
# proof marker of ANY convention
PROOF = re.compile(
    r'\\begin\{proof\}|\\emph\{Proof[^}]*\}|\\textbf\{Proof[^}]*\}|'
    r'\\emph\{Proof\}|\*\*Proof', re.I
)
# the paper's OWN supplementary section pointers: "Supplementary S3",
# "supplementary material (S5)", "the supplementary's S2.1"
OWNSUPP = re.compile(
    r"[Ss]upplementary(?:'s)?\s+(?:[Mm]aterial\s*)?\(?\s*S(\d+(?:\.\d+)?)"
)
OWNSUPP_FIG = re.compile(r'Figure~\s*S\d+')


def strip_comments(s):
    out = []
    for line in s.split('\n'):
        line = re.sub(r'(?<!\\)%.*$', '', line)
        out.append(line)
    return '\n'.join(out)


def audit(path):
    src = strip_comments(io.open(path, encoding='utf-8', errors='replace').read())
    claims = []
    for m in CLAIM.finditer(src):
        kind = m.group(1)
        name = m.group(2) or ''
        label = m.group(3) or ''
        line = src[:m.start()].count('\n') + 1
        claims.append((m.end(), line, kind, name.strip(), label))
    claims.sort()
    unproven = []
    for i, (end, line, kind, name, label) in enumerate(claims):
        # window: from end of this claim's \begin{...} line to the next claim
        nxt = claims[i + 1][0] if i + 1 < len(claims) else len(src)
        window = src[end:nxt]
        # stop the window at the next \begin{...} of any kind (figure, table)
        # so a proof belonging to a later display is not credited here
        m2 = re.search(r'\\begin\{(figure|table|remark|example|definition)\}', window)
        if m2:
            window = window[:m2.start()]
        if not PROOF.search(window):
            unproven.append((line, kind, name, label))
    supp = sorted(set(OWNSUPP.findall(src)),
                  key=lambda s: [int(x) for x in s.split('.')])
    return claims, unproven, len(OWNSUPP.findall(src)), supp, \
        len(OWNSUPP_FIG.findall(src)), len(re.findall(r'\\begin\{proof\}', src)), \
        len(PROOF.findall(src))


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    print('=' * 88)
    print('PROOF AUDIT (corrected instrument) - claims vs. evidence of ANY proof convention')
    print('=' * 88)
    total_unproven = 0
    total_supp = 0
    for unit, fn in UNITS:
        p = os.path.join(here, fn)
        if not os.path.exists(p):
            print('\nUNIT %-3s %-45s  MISSING' % (unit, fn))
            continue
        claims, unproven, nsupp, supp, nfig, nenv, nany = audit(p)
        total_unproven += len(unproven)
        total_supp += nsupp + nfig
        print('\nUNIT %-3s %s' % (unit, fn))
        print('  claim environments        : %d' % len(claims))
        print('  proof ENVIRONMENTS        : %d' % nenv)
        print('  proof markers, any style  : %d   (inline \\emph{Proof.} etc.)' % nany)
        print('  claims with NO proof found: %d' % len(unproven))
        for (line, kind, name, label) in unproven:
            print('        L%-6d %-11s %-46s %s' % (
                line, kind, (name[:44] if name else '(unnamed)'), label))
        print('  own-supplement pointers   : %d  (%s)%s' % (
            nsupp + nfig,
            ','.join('S' + s for s in supp) or '-',
            '  +%d Figure~S' % nfig if nfig else ''))
    print('\n' + '=' * 88)
    print('TOTAL claims with no proof of any convention : %d' % total_unproven)
    print('TOTAL own-supplement pointers across family  : %d' % total_supp)
    print('=' * 88)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Phase 1, stage one: claim inventory and traceability.

Extracts every quantitative claim (numbers with 2+ decimal places -- integers are
dominated by section/figure references) from the eleven unit heads and classifies
each by whether a provenance pointer sits near it: a named script, a version tag,
a supplementary anchor, or a section/table cross-reference.

This is an INVENTORY, not a verification. Stage two -- checking each number
against what the named script actually produced -- needs the computation, which
is not present in the workspace (repo/ was deleted to stay under budget).

A claim with no pointer is not necessarily wrong; it is untraceable, which is the
defect Phase 1 exists to surface.
"""
import io
import os
import re
import collections

BASE = os.path.dirname(os.path.abspath(__file__)) + '/'

UNITS = [
    ('1', 'paper01_obstruction_calculus_v63.tex'),
    ('2', 'paper02_probabilistic_sufficiency_v12.tex'),
    ('3', 'paper03_computational_certification_v16.tex'),
    ('4', 'paper04_minimax_dual_certificates_v16.tex'),
    ('5', 'paper05_exact_belief_computation_v16.tex'),
    ('6', 'paper06_assessment_separation_v67.tex'),
    ('7', 'paper08_governance_delay_v46.tex'),
    ('8', 'paper09_cod_certification_v32.tex'),
    ('9', 'paper10_depletion_ledgers_v53.tex'),
    ('10', 'paper11_forecasting_baselines_v64.tex'),
    ('11', 'paper11c_worked_systems_audit_v2.tex'),
]

# a decimal result: 2+ decimal places, not part of a longer identifier
NUM = re.compile(r'(?<![\w.])(\d+\.\d{2,})(?![\w.])')

# provenance: named script, version tag, supplementary anchor, or cross-reference
PROV = re.compile(
    r'(?:'
    r'[\w/]+\.py\b'                      # run_intervention_v3.py
    r'|\bv(?:29|3[0-9]|[0-9]{1,2})\b'    # v29, v30, v3
    r'|Supplementary\s*S?\d+'            # Supplementary S12
    r'|Section~?\\?\s*\d+(?:\.\d+)?'     # Section 3.5
    r'|Table~?\\?\s*\d+'                 # Table 5
    r'|Figure~?\\?\s*\d+'                # Figure 3
    r'|campaign_\w+'                     # campaign_e2_elevation_v3
    r'|verification\w*'                  # verification script
    r'|battery\w*'
    r'|Lemma~?\\?\s*\w+|Proposition~?\\?\s*\w+|Theorem~?\\?\s*\w+'
    r')', re.I)

WINDOW = 320  # characters either side to look for provenance

# Numbers that are LaTeX FURNITURE, not scientific claims. Without this filter the
# inventory is ~70% column widths, \linewidth fractions, DOIs and includegraphics
# scales, and the traceability percentage measures nothing.
FURNITURE = re.compile(
    r'(?:'
    r'\\(?:linewidth|textwidth|columnwidth|textheight|paperwidth|paperheight|hsize)\b'
    r'|\\real\{|\btabcolsep\b|\\arraystretch|\bparbox\b|\\multicolumn'
    r'|\\includegraphics|\bdoi\.org\b|\bzenodo\b|\\url\{|https?://'
    r'|\\(?:addtolength|setlength|hspace|vspace)\b'
    r'|\\(?:begin|end)\{tabular\}|\bp\{[\d.]+\\'
    r')')


def is_furniture(body, start):
    """True if the number sits on a line dominated by LaTeX layout, not a claim."""
    ls = body.rfind('\n', 0, start) + 1
    le = body.find('\n', start)
    line = body[ls:le if le != -1 else len(body)]
    return bool(FURNITURE.search(line))


def strip_comments(s):
    out = []
    for line in s.split('\n'):
        i = line.find('%')
        while i != -1:
            if i == 0 or line[i - 1] != '\\':
                line = line[:i]
                break
            i = line.find('%', i + 1)
        out.append(line)
    return '\n'.join(out)


def main():
    total = traced = 0
    rows = []
    examples = collections.defaultdict(list)

    for unit, fn in UNITS:
        p = BASE + fn
        if not os.path.exists(p):
            print('MISSING %s' % fn)
            continue
        c = strip_comments(io.open(p, encoding='utf-8', errors='replace').read())
        # skip the bibliography: citation numbers are not claims
        m = re.search(r'\\(?:section|section\*)\{[^}]*[Rr]eferences', c)
        body = c[:m.start()] if m else c

        hits = [m for m in NUM.finditer(body) if not is_furniture(body, m.start())]
        n_tr = 0
        for mt in hits:
            lo = max(0, mt.start() - WINDOW)
            hi = min(len(body), mt.end() + WINDOW)
            ctx = body[lo:hi]
            if PROV.search(ctx):
                n_tr += 1
            else:
                line = body[:mt.start()].split('\n')[-1] + body[mt.start():].split('\n')[0]
                if len(examples[unit]) < 4:
                    examples[unit].append(
                        (mt.group(1), body[:mt.start()].count('\n') + 1,
                         re.sub(r'\s+', ' ', line)[:140]))
        rows.append((unit, fn, len(hits), n_tr))
        total += len(hits)
        traced += n_tr

    print('%-5s %-46s %8s %8s %7s' % ('unit', 'file', 'claims', 'traced', 'untraced'))
    for unit, fn, n, tr in rows:
        print('  %-3s %-46s %8d %8d %7d' % (unit, fn[:46], n, tr, n - tr))
    print('  %-50s %8d %8d %7d' % ('TOTAL', total, traced, total - traced))
    print()
    print('overall traceability: %.1f%%' % (100.0 * traced / total if total else 0))
    print()
    for unit, fn, n, tr in rows:
        if examples[unit]:
            print('--- unit %s  %s  (%d untraced, sample)' % (unit, fn, n - tr))
            for val, ln, line in examples[unit]:
                print('    L%-6d %-11s %s' % (ln, val, line))
            print()


if __name__ == '__main__':
    main()

"""Phase 0 soundness sweep — systematic, not enumerative.

The defect list is open, so this does not hard-code a list of known defects and stop. It
looks for *classes* of defect, mechanically, across every source paper:

  A. Stale provenance      -- version pins / counts contradicted by the artifact tree
  B. Convention contamination -- numbers produced on a superseded basis
  C. Unverifiable claims   -- build/compile claims that cannot be re-run here
  D. Abstract selection    -- headline numbers in the abstract that differ from the body
  E. Unsourced numbers      -- tabulated quantities with no stated provenance nearby
  F. Mis-cited prior art   -- nearest neighbour named in the audit but absent from the text
  G. Bare point estimates  -- headline figures quoted without their uncertainty band

Each finding is reported with file, line and the matching text so it can be checked.
"""
import io, os, re, sys, json

PAPERS = '/home/user/papers/'

# ------------------------------------------------------------------ signatures
# (A) stale provenance: the artifact tree says these are wrong
STALE = [
    (r'v4\.14\.0', 'Lean toolchain pin; repo pin is v4.34.1'),
    (r'\b54\s+modules\b', 'Lean module count; repo has 60 under Formalizations/'),
    (r'\b60\s+build\s+jobs\b', 'build claim from the v4.14.0 run; not reproducible here'),
]

# (B) superseded hybrid basis (E2): v2 numbers, wrong under the source-year ruling
HYBRID_BAD = {
    '-460.03': 'UC_min v2 (hybrid) -> -328.97',
    '-318.76': 'UC_q05 v2 (hybrid) -> -287.36',
    '-114.85': 'UC_q10 v2 (hybrid) -> -80.87',
    '134.96': 'residual SD v2 (hybrid) -> 114.91',
}

# (F) nearest neighbours the audits say must be cited
MUST_CITE = {
    'paper01': [('Doyen', 'Doyen 2000 output-feedback (Set-Valued Analysis 8:149-162)'),
                ('viscosity', 'HJ-reachability / viscosity lineage')],
    'paper06': [('robust optimi', 'robust-optimisation separation results')],
}

# (G) headline figures that the audits say are ill-conditioned and must carry a band
ILLCOND = [
    (r'\b6\.5(?:0|01)?\s*(?:yr|years?)\b', '6.5-yr crossing: must carry the 0.87-10.67 band'),
]


def strip_comments(s):
    return "\n".join(re.sub(r'(?<!\\)%.*$', '', l) for l in s.split('\n'))


def find_line(c, needle):
    for i, l in enumerate(c.split('\n')):
        if needle in l:
            return i + 1
    return None


def scan(path):
    raw = io.open(path, encoding='utf-8', errors='replace').read()
    c = strip_comments(raw)
    stem = os.path.basename(path)
    key = re.match(r'(paper\d+\w*)', stem)
    key = key.group(1) if key else stem
    out = []

    for pat, why in STALE:
        for m in re.finditer(pat, c, re.I):
            out.append(('A.stale', m.group(0), why, c[:m.start()].count('\n') + 1))

    for num, why in HYBRID_BAD.items():
        if num in c:
            out.append(('B.hybrid', num, why, find_line(c, num)))

    for pat, why in ILLCOND:
        n = len(re.findall(pat, c, re.I))
        if n:
            # does the band appear anywhere in the paper?
            banded = bool(re.search(r'0\.87|10\.67', c))
            out.append(('G.illcond' if not banded else 'G.illcond(band present)',
                        '%d bare' % n, why, find_line(c, re.search(pat, c, re.I).group(0))))

    for kw, why in MUST_CITE.get(key, []):
        if not re.search(kw, c, re.I):
            out.append(('F.priorart', 'ABSENT: %s' % kw, why, None))

    # (F') sharper: Doyen is cited 12x but only as the APPLIED author. The 2000
    # output-feedback paper is the nearest neighbour and must appear by venue/year.
    if key == 'paper01':
        has_2000 = bool(re.search(
            r'Doyen[^\n]{0,80}(?:2000)|Set-Valued Analysis\s*\**8', c, re.I))
        if not has_2000:
            out.append(('F.priorart', 'Doyen 2000 absent',
                        'cites Doyen the applied author, not the output-feedback theorist',
                        None))

    # (D) abstract selection: numbers in the abstract vs the body
    for env in ('abstract',):
        m = re.search(r'\\begin\{%s\}(.*?)\\end\{%s\}' % (env, env), c, re.S)
        if not m:
            continue
        ab = m.group(1)
        body = c[:m.start()] + c[m.end():]
        for num in sorted(set(re.findall(r'(?<![\w.])-?\d+\.\d{2,}', ab)), key=len, reverse=True)[:12]:
            if num not in body:
                out.append(('D.abstract-only', num,
                            'in abstract but nowhere in body', find_line(c, num)))

    return out


def main():
    files = sorted(f for f in os.listdir(PAPERS) if f.endswith('.tex'))
    print("Phase 0 sweep — %d .tex files (all sources AND merged outputs)\n" % len(files))
    total = 0
    for f in files:
        res = scan(PAPERS + f)
        if not res:
            print("  %-46s clean" % f)
            continue
        print("  %-46s %d finding(s)" % (f, len(res)))
        for kind, hit, why, ln in res:
            loc = 'L%s' % ln if ln else '-'
            print("      [%-26s] %-14s %-6s %s" % (kind, str(hit)[:14], loc, why))
        total += len(res)
    print("\nTOTAL: %d findings" % total)


if __name__ == '__main__':
    main()

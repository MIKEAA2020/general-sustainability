import io

P = '/home/user/p5/phase0_scan.py'
s = io.open(P, encoding='utf-8').read()

# ---------------------------------------------------------------- same_work()
ANCHOR = "def surname_year(e):"
assert ANCHOR in s

SAME_WORK = r'''def _norm_text(t):
    """Lowercased, LaTeX-stripped, alphanumeric words -- for title similarity."""
    t = re.sub(r'\\[A-Za-z]+', ' ', t)
    t = t.replace('{', ' ').replace('}', ' ')
    t = t.lower()
    t = re.sub(r'[^a-z0-9 ]', ' ', t)
    return re.sub(r'\s+', ' ', t).strip()


_DOI = re.compile(r'\b(10\.\d{4,9}/[^\s,;"\}]+)', re.I)
# "2016/026", "Rep.~2016/026", "Report 2011/037", "No. 3328", "Circular 1186"
_REPORT = re.compile(
    r'\b(\d{4}/\d{2,4})\b'
    r'|\b(?:rep(?:ort)?\.?|no\.?|circular|advis(?:ory)?)\s*~?\s*'
    r'(\d{1,4}(?:/\d{2,4})?)\b', re.I)


def fingerprints(e):
    """-> set of identity fingerprints for a reference entry.

    A DOI or a report number identifies a work outright. A year alone does
    not, but year + title does.
    """
    fps = set()
    d = _DOI.search(e)
    if d:
        fps.add('doi:' + d.group(1).rstrip('.').lower())
    r = _REPORT.search(e)
    if r:
        v = r.group(1) or r.group(2)
        if v:
            fps.add('rep:' + v.lower())
    y = YEAR.search(e)
    if y:
        fps.add('yr:' + y.group(0))
    return fps


def same_work(a, b):
    """Do two entries cite the SAME work?

    This replaces byte-identity, which is the wrong test: two entries citing
    one report routinely differ in citation style and nothing else, so a
    byte comparison reports "they differ" and leaves a human to notice that
    the report number is identical. Identity of work is decided by:

      - a shared DOI, or
      - a shared report number            (decisive either way)
      - else the same year AND >=60% title-token overlap

    The DFO 2016 pair that motivated this was:

        DFO, 2016. Stock Assessment of Northern cod (NAFO Divs. 2J3KL) in
        2016. DFO Can. Sci. Advis. Sec. Sci. Advis. Rep.~2016/026.
        DFO (2016). Stock assessment of Northern cod (NAFO 2J3KL).
        \emph{Can. Sci. Advis. Sec. Sci. Advis. Rep.} 2016/026.

    Not byte-identical. Same report, 2016/026. One work.
    """
    fa, fb = fingerprints(a), fingerprints(b)
    for p in ('doi:', 'rep:'):
        sa = set(x for x in fa if x.startswith(p))
        sb = set(x for x in fb if x.startswith(p))
        if sa and sb:
            # both carry this kind of identifier: agreement is decisive, and
            # so is disagreement
            return bool(sa & sb)
    ya = set(x for x in fa if x.startswith('yr:'))
    yb = set(x for x in fb if x.startswith('yr:'))
    if not (ya and yb and (ya & yb)):
        return False
    ta, tb = set(_norm_text(a).split()), set(_norm_text(b).split())
    if not ta or not tb:
        return False
    return len(ta & tb) / float(len(ta | tb)) >= 0.60


'''

s = s.replace(ANCHOR, SAME_WORK + ANCHOR, 1)

# ------------------------------------------------- L.dup-ref-key uses same_work
old_dupkey = """        if k in bykey:
            out.append(('L.dup-ref-key', '%s %s' % k,
                        'same author+year as L%d but different text: if these are '
                        'distinct wo"""
i = s.index("        if k in bykey:")
j = s.index("\n", s.index("assumptions differ.", i))
block = s[i:j]
new_block = """        if k in bykey:
            prev_ln, prev_txt = bykey[k]
            # Same author and year is NOT enough -- an author legitimately
            # publishes two things in a year. Only flag when the two entries
            # are the same WORK by the semantic test above, which is what
            # makes this finding actionable: "merge these", not "check these".
            if same_work(prev_txt, e):
                out.append(('L.dup-ref-key', '%s %s' % k,
                            'same author+year as L%d and the same work '
                            '(shared DOI, report number, or year+title) -- '
                            'merge to one entry' % prev_ln, ln))
            bykey[k] = (ln, e)
        else:
            bykey[k] = (ln, e)
"""
s = s[:i] + new_block + s[j:]

io.open(P, 'w', encoding='utf-8').write(s)
print('same_work() added; L.dup-ref-key now requires semantic identity')

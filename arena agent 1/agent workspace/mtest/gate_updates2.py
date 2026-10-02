import io

P = '/home/user/p5/phase0_scan.py'
s = io.open(P, encoding='utf-8').read()

OLD = """    bykey = {}
    for ln, e in ents:
        k = surname_year(e)
        if k[1] is None:
            continue
        if k in bykey:
            out.append(('L.dup-ref-key', '%s %s' % k,
                        'same author+year as L%d but different text: if these are '
                        'distinct works they need %s letters; if it is the same '
                        'work entered twice, merge them'
                        % (bykey[k], 'a/b/c'), ln))
        else:
            bykey[k] = ln
    return out
"""

NEW = """    bykey = {}
    for ln, e in ents:
        k = surname_year(e)
        if k[1] is None:
            continue
        if k in bykey:
            prev_ln, prev_txt = bykey[k]
            # Same author and year is NOT enough to call two entries a
            # duplicate: an author legitimately publishes two things in a
            # year, and flagging those was most of this rule's output. It now
            # fires only when the two entries are the same WORK by the
            # semantic test (shared DOI, shared report number, or same year
            # plus title overlap). That makes the finding actionable --
            # "merge these", not "go and check whether these conflict".
            if same_work(prev_txt, e):
                out.append(('L.dup-ref-key', '%s %s' % k,
                            'same author+year as L%d and the SAME WORK '
                            '(shared DOI, report number, or year+title) -- '
                            'merge to one entry' % prev_ln, ln))
            # keep the FIRST entry as the comparison point
            continue
        bykey[k] = (ln, e)
    return out
"""

assert OLD in s, 'L.dup-ref-key block not found'
s = s.replace(OLD, NEW, 1)
io.open(P, 'w', encoding='utf-8').write(s)
print('L.dup-ref-key now requires semantic identity (same_work)')

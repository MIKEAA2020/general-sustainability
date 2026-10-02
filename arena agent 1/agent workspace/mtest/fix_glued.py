import io

P = '/home/user/p5/mergelib.py'
s = io.open(P, encoding='utf-8').read()

OLD = """    out = []
    for e in entries:
        pieces, prev = [], 0
        for m in GLUED.finditer(e):
            sm = re.search(_NAME_YR, e[m.start():])
            if not sm:
                continue
            cut = m.start() + sm.start()
            if cut <= prev:
                continue
            pieces.append(e[prev:cut].strip())
            prev = cut
        pieces.append(e[prev:].strip())
        out.extend(p for p in pieces if p)
    return out
"""

NEW = r'''    out = []
    for e in entries:
        out.extend(_split_glued(e))
    return out


def _split_glued(entry):
    """Undo one paragraph holding several references run together.

    Some sources put two or three references in a single paragraph with no
    blank line between them, e.g.

        Adamson, M. W., and Hilker, F. M. 2020. ... 425--434.
        {\AA}str{"o}m, K. J., and Wittenmark, B. 1997. ... Alkire, S., ...

    A candidate seam is a period, whitespace, then a "Surname," token. It is
    accepted only when the text that follows it contains a four-digit year --
    that is what separates a genuine next reference from a publisher line such
    as "Introduction to Interval Analysis. SIAM, Philadelphia.", which carries
    no year and is therefore stitched back onto its head.
    """
    seams = [m.end() for m in _SEAM.finditer(entry)]
    if not seams:
        return [entry]
    bounds = [0] + seams + [len(entry)]
    segs = [entry[bounds[i]:bounds[i + 1]].strip()
            for i in range(len(bounds) - 1)]
    out = []
    for seg in segs:
        if out and not _YR.search(seg):
            out[-1] = out[-1] + ' ' + seg
        else:
            out.append(seg)
    return [o for o in out if o]
'''

assert OLD in s, 'glued loop not found'
s = s.replace(OLD, NEW, 1)

# define the seam + year patterns next to the other module-level regexes
anchor = "_NAME_YR = "
i = s.index(anchor)
j = s.index('\n', i) + 1
s = (s[:j]
     + "\n# seam between two references run together in one paragraph, and the year\n"
       "# test that distinguishes a next reference from a publisher line\n"
       "_SEAM = re.compile(r'(?<=\\.)\\s+(?=[{\\[A-ZÄÖÅ]\\S{0,40}?,)')\n"
       "_YR = re.compile(r'\\b(?:19|20)\\d{2}\\b')\n"
     + s[j:])

io.open(P, 'w', encoding='utf-8').write(s)
print('glued-splitter replaced with seam + year-discriminated splitter')

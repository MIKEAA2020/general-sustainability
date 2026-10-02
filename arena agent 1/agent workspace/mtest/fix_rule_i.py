import io

P = '/home/user/p5/phase0_scan.py'
s = io.open(P, encoding='utf-8').read()

OLD = """    # I -- more than one supplementary-material passage
    supp = []
    for m in SUPP_HEAD.finditer(c):
        supp.append((c[:m.start()].count('\\n') + 1, 'heading'))
    for blk in re.split(r'\\n\\s*\\n', c):
        if SUPP_OPEN.match(blk):
            ln = c[:c.find(blk)].count('\\n') + 1 if blk in c else None
            supp.append((ln, 'paragraph opener'))
    if len(supp) > 1:
        out.append(('I.duplicate-supplement', '%d passages' % len(supp),
                    'supplementary-material passages at lines %s (%s) -- at most '
                    'one can describe this paper'
                    % (', '.join(str(s[0]) for s in supp if s[0]),
                       ', '.join(s[1] for s in supp)), supp[1][0]))
"""

NEW = r"""    # I -- two supplementary-material passages that describe the SAME supplement.
    #
    # A merged paper legitimately carries TWO passages when they point at two
    # different supplementary files (paper08 v46: ..._supplementary_delay.md and
    # ..._supplementary_governance.md -- both files state that both are required,
    # because the main text cites sections from each). Counting passages and
    # failing on >1 therefore flagged a correct merge as broken. A passage is a
    # DUPLICATE only if it describes the same supplement as another one, which is
    # decided by the file it names, or by near-identical wording when it names
    # none.
    supp = []
    for m in SUPP_HEAD.finditer(c):
        tail = c[m.end():]
        nxt = re.search(r'\\(?:sub)*section\*?\{', tail)
        supp.append((c[:m.start()].count('\n') + 1, 'heading',
                     tail[:nxt.start()] if nxt else tail))
    for blk in re.split(r'\n\s*\n', c):
        if SUPP_OPEN.match(blk):
            ln = c[:c.find(blk)].count('\n') + 1 if blk in c else None
            supp.append((ln, 'paragraph opener', blk))

    def _supp_file(text):
        m = re.search(r'\\texttt\{([^}]*supplementary[^}]*)\}', text, re.I)
        return m.group(1).strip() if m else None

    def _tokens(text):
        t = re.sub(r'\\[a-zA-Z]+\*?(?:\{[^}]*\})?', ' ', text)
        t = re.sub(r'[^a-z0-9 ]', ' ', t.lower())
        stop = set('the a an of and or in for with to is are be this that '
                   'these those it its as at on by from we our which material '
                   'supplementary file provided accompanying'.split())
        return set(w for w in t.split() if len(w) > 3 and w not in stop)

    # 1. two passages naming the same file are duplicates
    named = {}
    for ln, kind, text in supp:
        f = _supp_file(text)
        if f:
            named.setdefault(f, []).append((ln, kind))
    dupes = [v for v in named.values() if len(v) > 1]

    # 2. passages naming no file: duplicates only if near-identical wording
    unnamed = [(ln, kind, text) for ln, kind, text in supp if not _supp_file(text)]
    tok = [_tokens(t) for _, _, t in unnamed]
    for i in range(len(unnamed)):
        for j in range(i + 1, len(unnamed)):
            if not tok[i] or not tok[j]:
                continue
            jac = len(tok[i] & tok[j]) / float(len(tok[i] | tok[j]))
            if jac >= 0.6:
                dupes.append([unnamed[i][:2], unnamed[j][:2]])

    # 3. a named passage and an unnamed one that is the same text
    for f, group in named.items():
        for ln, kind, text in unnamed:
            for gln, gkind in group:
                gt = next((t for l, k, t in supp if l == gln and k == gkind), '')
                a, b = _tokens(text), _tokens(gt)
                if a and b and len(a & b) / float(len(a | b)) >= 0.6:
                    dupes.append([(ln, kind), (gln, gkind)])

    if dupes:
        flat = []
        for d in dupes:
            for ln, kind in d:
                if ln is not None and (ln, kind) not in flat:
                    flat.append((ln, kind))
        out.append(('I.duplicate-supplement', '%d passages' % len(flat),
                    'supplementary-material passages at lines %s (%s) -- these '
                    'describe the same supplement; keep one'
                    % (', '.join(str(l) for l, _ in flat),
                       ', '.join(k for _, k in flat)),
                    flat[1][0] if len(flat) > 1 else flat[0][0]))
"""

assert OLD in s, 'rule I block not found'
s = s.replace(OLD, NEW, 1)
io.open(P, 'w', encoding='utf-8').write(s)
print('rule I rewritten: duplicates judged by supplement identity, not count')

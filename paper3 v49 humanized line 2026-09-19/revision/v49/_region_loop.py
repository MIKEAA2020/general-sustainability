LISTMARK_RE = re.compile(r'^(\s*)(?:([-*+])|(\d+)\.)\s+(.*)$')


def _is_flush_para_start(block):
    """a unit that ends the list run: a heading, a rule, display math, or a flush-left paragraph"""
    first = block.split('\n')[0]
    return bool(re.match(r'^(#{1,5}\s|---|@@@DOLLAR@@@)', first)) or (len(first) - len(first.lstrip())) == 0 \
        and not LISTMARK_RE.match(first)


def emit_list(units, i):
    """render one markdown list run into tex, starting at units[i].

    The previous branch handled only `- ` items, chose the environment from the FIRST unit of the whole
    region, and — the damaging one — on meeting a non-list block appended the rest of the section into
    the current item and kept consuming. That is why the introduction reached the page as two giant
    blocks with no paragraph spacing. Runs now end where the markdown ends them, nested bullets stay
    under their parent item, indented continuation paragraphs stay inside their item, and a numbered
    list renders its own numbers by setting the counter instead of restarting at 1 for every run.
    """
    top = []                                   # list of {'text': str, 'kids': [str]}
    cur = None
    j = i
    while j < len(units):
        u = units[j]
        lines = [x for x in u.split('\n') if x.strip()]
        first = lines[0] if lines else ''
        m = LISTMARK_RE.match(first)
        ind0 = len(first) - len(first.lstrip())
        if m and ind0 == 0:
            cur = {'num': int(m.group(3)) if m.group(3) else None, 'text': m.group(4).strip(), 'kids': []}
            top.append(cur)
            for extra in lines[1:]:
                mm = LISTMARK_RE.match(extra)
                if mm:
                    cur['kids'].append(mm.group(4).strip())
                else:
                    cur['text'] += ' ' + ' '.join(extra.split())
            j += 1
            continue
        if cur is not None and not _is_flush_para_start(u):
            # an indented continuation paragraph or a run of sub-bullets belonging to the last item
            for extra in lines:
                mm = LISTMARK_RE.match(extra)
                if mm:
                    cur['kids'].append(mm.group(4).strip())
                elif (len(extra) - len(extra.lstrip())) > 0:
                    cur['text'] += ' ' + ' '.join(extra.split())
                else:
                    break
            j += 1
            continue
        break
    numeric = all(it['num'] is not None for it in top)
    body = []
    for k, it in enumerate(top, 1):
        if numeric and it['num'] is not None and it['num'] != k:
            body.append('\\setcounter{enumi}{%d}' % (it['num'] - 1))
        txt = to_tex(it['text'])
        if it['kids']:
            env = 'itemize'
            txt += ('\n\\begin{%s}\\setlength{\\itemsep}{1pt}\n' % env
                    + '\n'.join('    \\item ' + to_tex(x) for x in it['kids'])
                    + '\n\\end{%s}' % env)
        body.append('\\item ' + txt)
    env = 'enumerate' if numeric else 'itemize'
    tex = '\\begin{%s}\\setlength{\\itemsep}{2pt}\n%s\n\\end{%s}' % (env, '\n'.join(body), env)
    return tex, j


out = []
_blocks = [b for b in fm_md.split('\n\n') if b.strip()]
bi = 0
while bi < len(_blocks):
    b = _blocks[bi]
    if b.startswith('# '):
        bi += 1; continue                                     # the title lives in \title{}, already v48's
    if b == '---':
        out.append('\\vspace{0.8em}'); bi += 1; continue
    if b.startswith('### '):
        txt = b[4:].strip(); num = txt.split()[0] if re.match(r'^\d', txt) else ''
        lab = old_head_labels.get(num, bc.slug(re.sub(r'^\d+(\.\d+)*\s*', '', txt)))
        out.append('\\subsection*{%s}\\label{%s}' % (to_tex(txt), lab)); bi += 1; continue
    if b.startswith('## '):
        txt = b[3:].strip()
        if txt.lower() == 'abstract':
            out.append('\\section*{Abstract}\\label{abstract}'); bi += 1; continue
        num = txt.split()[0] if re.match(r'^\d', txt) else ''
        lab = old_head_labels.get(num, bc.slug(re.sub(r'^\d+(\.\d+)*\s*', '', txt)))
        out.append('\\section*{%s}\\label{%s}' % (to_tex(txt), lab)); bi += 1; continue
    if b.startswith('#### '):
        out.append('\\textbf{%s}' % to_tex(b[5:].strip())); bi += 1; continue
    if b.startswith('$$'):
        buf = b
        while buf.count('$$') % 2 and bi + 1 < len(_blocks):
            bi += 1; buf += ' ' + _blocks[bi]
        out.append('\\[ ' + re.sub(r'\s*\n\s*', ' ', buf.replace('$$', '')).strip() + ' \\]')
        bi += 1; continue
    if LISTMARK_RE.match(b.split('\n')[0]) and (len(b.split('\n')[0]) - len(b.split('\n')[0].lstrip())) == 0:
        _tex, _nxt = emit_list(_blocks, bi)
        out.append(_tex); bi = _nxt; continue
    out.append(to_tex(b)); bi += 1

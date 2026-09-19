#!/usr/bin/env python3
"""v36 kernel: the five open items that `uploads/open.txt` claimed to close, after each was checked against
the repo and the web.  Applied to md and tex together; every edit is logged so v36 -> v35 reverses exactly.

Provenance: review/open_items_v4_closed.md (this turn's evaluation of open.txt) and
repo_audits/ (LSIT optimal-loss LP; the companion record's own PDF, text-extracted for the eq. (1) /
Section 2.4 pointer; the NFA Guidebook for the carbon-biocapacity convention).
"""
import re, sys, json

HERE = '/home/user/revision/v7'
sys.path.insert(0, HERE)
from build_v35_kernel import m2t, pattern, SQ          # noqa: E402  (import only defines helpers)

MD_IN, TEX_IN = f'{HERE}/paper3_material_ledgers_v35.md', f'{HERE}/paper3_material_ledgers_v35.tex'
MD_OUT, TEX_OUT = f'{HERE}/paper3_material_ledgers_v36.md', f'{HERE}/paper3_material_ledgers_v36.tex'
LOG = f'{HERE}/revisions_v36_kernel_log.json'

E = []


def sub(name, old, new, old_tx=None, new_tx=None):
    E.append((name, old, new, old_tx, new_tx))


def ins(name, anchor, block, anchor_tx=None, block_tx=None):
    """Insert `block` before `anchor` (logged as anchor -> block + anchor so it reverses)."""
    E.append((name, anchor, block + anchor, anchor_tx, (block_tx or block) + anchor_tx if anchor_tx else None))


# ---- 1. the deadline block: Def 45, Prop 41, Def 46, Remark 35 (LSIT + envelope + additionality gate)
BLOCK = open(f'{HERE}/v36_block_deadlines.md').read()
BLOCK = BLOCK.replace('unit per year$^2$', 'unit per year per year')          # keep the math runs balanced
ins('def45-46-prop41-rem35',
    """These three statements are the calculus the article's own citations had deferred to a companion: an""",
    BLOCK)

# ---- 2. the per-parameter identifiability field, in the article's own status vocabulary
sub('cert-parameter-status',
    """each entry taking one of three values: established, not established, and not applicable to this
object. The third value is not a failure and the second is not a refutation.""",
    """each entry taking one of three values: established, not established, and not applicable to this
object. The third value is not a failure and the second is not a refutation. The same three values are the
vocabulary of the per-parameter field of the declaration protocol, applied to identification rather than to
proof: a declared parameter is *established* when the observation map pins it, *not established* when the
record leaves it free, and *not applicable* when no identification question is live for it, as for a
normalising convention. Status is a property of the pair (model, record) and never of a parameter alone, so a
value that is unidentifiable for one readout may be identifiable for another, and the field is reported per
readout --- which is the entry-level content of Proposition 39.""")

# ---- 3. Remark 33: the carbon row is the accounts' convention, and the vintage is named
sub('remark33-convention-cited',
    """Which convention a reported premium uses is a
property of the accounts, not of the theorem --- including the zero-biocapacity carbon row makes
$\\tau_{\\min} = 0$ identically, and a construction over positive components alone can return
$\\tau_{\\mathrm{agg}} > 365$ d, which states that no component overshoots within the year rather than that
no overshoot occurs --- so the convention is declared with the figure, and the figures above are world
totals, not any territory's.""",
    """Which rows enter the ratio set is fixed by the accounts, not by this
construction: the Guidebook to the National Footprint and Biocapacity Accounts states that no biocapacity
figure is computed for carbon uptake, because carbon demand is charged against forest land biocapacity and a
carbon biocapacity of its own would double count it (Global Footprint Network, 2021, Section 9.1.2). The zero
row is therefore a published convention, and it is what makes $\\tau_{\\min} = 0$ identically, so the premium
above equals the whole aggregate date by construction rather than by dispersion. Excluding the carbon
*demand* instead is a different object --- the non-carbon components only --- on which
$\\tau_{\\mathrm{agg}} > 365$ d states that no included component overshoots within the year, not that no
overshoot occurs. Both figures are world totals of one data vintage: the accounts are recomputed for every
year of the series at each release, so the 2022 row of the 2025 edition (213 d) need not reproduce the date
announced for 2022 (28 July, the 209th day of that year), and that four-day difference is vintage and
nowcasting rather than arithmetic. The figures are world totals, not any territory's.""")

# ---- 4. the new Guidebook entry, in the reference list after Gale
# No URL in the entry: the hosted file name carries underscores, which are text-mode characters in LaTeX
# and emphasis markers in markdown. The edition, publisher and section number identify it; the file path is
# recorded in review/open_items_v4_closed.md.
ENTRY = ('Global Footprint Network, 2021. Working Guidebook to the National Footprint and Biocapacity '
         'Accounts, 2021 edition. Global Footprint Network, Oakland, CA.')
sub('guidebook-reference',
    """Gale, D., 1957. A theorem on flows in networks. Pacific Journal of Mathematics 7, 1073–1082.""",
    """Gale, D., 1957. A theorem on flows in networks. Pacific Journal of Mathematics 7, 1073–1082.

""" + ENTRY,
    old_tx="""Gale, D., 1957. A theorem on flows in networks. Pacific Journal of Mathematics 7, 1073--1082.""",
    new_tx="""Gale, D., 1957. A theorem on flows in networks. Pacific Journal of Mathematics 7, 1073--1082.

""" + ENTRY)

# ---- 5. the companion pointer, made checkable against the companion's own text
sub('companion-precision',
    """(Abaee, 2026, doi:10.5281/zenodo.22554217; eq. (1) and Section 2.4 of that analysis)""",
    """(Abaee, 2026, doi:10.5281/zenodo.22554217; its eq. (1), where the memory--effort pair is defined on the
gated three-state core with the stock-decline rate as memory input, and its Section 2.4, which relates that
core to the four-state working model in which the input is $qEN - R(N, A)$)""")

# ---- 6. numbering note: the counter now runs to 46, with Proposition 41 and Remark 35
sub('numbering-range-46',
    """runs on the single 1–44 sequence counter""",
    """runs on the single 1–46 sequence counter""",
    old_tx="""runs on the single 1--44 sequence counter""",
    new_tx="""runs on the single 1--46 sequence counter""")

sub('numbering-added-46',
    """Definitions 21–23 and 34–35 and 38 and 40–44, Lemma 4, Theorem 24, and Propositions 25–32 and 36–37 and 39–40, with Remarks 33 and 34,""",
    """Definitions 21–23 and 34–35 and 38 and 40–46, Lemma 4, Theorem 24, and Propositions 25–32 and 36–37 and 39–41, with Remarks 33–35,""",
    old_tx="""Definitions 21--23 and 34--35 and 38 and 40--44, Lemma 4, Theorem 24, and Propositions 25--32 and 36--37 and 39--40, with Remarks 33 and 34,""",
    new_tx="""Definitions 21--23 and 34--35 and 38 and 40--46, Lemma 4, Theorem 24, and Propositions 25--32 and 36--37 and 39--41, with Remarks 33--35,""")


# ---- 7. the other mention of the companion pointer (Section 2.4 of this article), made consistent
sub('companion-precision-2',
    """(under review; eq. (1) and Section 2.4 of that analysis), not an object of this article""",
    """(under review; its eq. (1), the gated three-state core, and its Section 2.4, which relates that core to
the working four-state model), not an object of this article""")


def unescape_display(tx):                      # same rule as the v35 kernel (display math verbatim)
    lines = tx.split('\n')
    out, i = [], 0
    while i < len(lines):
        st = lines[i].strip()
        if st.startswith('\\[') and st.endswith('\\]') and len(st) > 4:
            out.append(re.sub(r'(?<!\\)\\_', '_', lines[i])); i += 1; continue
        if st == '\\[':
            j = i + 1
            while j < len(lines) and lines[j].strip() != '\\]':
                j += 1
            if j < len(lines) and j - i <= 12:
                out += [re.sub(r'(?<!\\)\\_', '_', l) for l in lines[i:j + 1]]
                i = j + 1
                continue
        out.append(lines[i]); i += 1
    return '\n'.join(out)


def main():
    md, tx = open(MD_IN).read(), open(TEX_IN).read()
    hits, applied = [], []
    for name, old, new, old_tx, new_tx in E:
        m_md = pattern(old).search(md)
        o_tx = old_tx if old_tx is not None else m2t(old)
        n_tx = new_tx if new_tx is not None else m2t(new)
        m_tx = pattern(o_tx).search(tx)
        hits.append((name, 'md' if m_md else 'MD-MISS', 'tex' if m_tx else 'TEX-MISS'))
        if not (m_md and m_tx):
            continue
        md = md[:m_md.start()] + new + md[m_md.end():]
        tx = tx[:m_tx.start()] + n_tx + tx[m_tx.end():]
        applied.append((name, old, new, o_tx, n_tx))
    for n, a, b in hits:
        print(f'{n[:28]:30s} {a:9s} {b}')
    if any('MISS' in h[1] + h[2] for h in hits):
        print('\naborted: unmatched anchors'); sys.exit(1)
    tx = unescape_display(tx)
    bad = sorted({c for c in tx if ord(c) > 127})
    # only the inserted block is checked for balanced math delimiters: the shipped md legitimately
    # carries math runs that straddle a line break.
    unbal = BLOCK.count('$') % 2
    print('tex non-ascii:', bad, '| square left:', SQ in tx, '| block $ count:', BLOCK.count('$'),
          '(even)' if not unbal else '(ODD)')
    if bad or unbal:
        print('aborted: dialect problem'); sys.exit(1)
    open(MD_OUT, 'w').write(md)
    open(TEX_OUT, 'w').write(tx)
    json.dump([{'name': n, 'old': o, 'new': nw, 'old_tex': ot, 'new_tex': nt}
               for n, o, nw, ot, nt in applied], open(LOG, 'w'), indent=1)
    print(f'\nwrote {MD_OUT} ({len(md)} B), {TEX_OUT} ({len(tx)} B) | edits: {len(applied)}')


if __name__ == '__main__':
    main()

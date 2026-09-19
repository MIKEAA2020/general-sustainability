#!/usr/bin/env python3
"""v37 kernel: the undefined object the article had been using five times without defining it (the
`\mathcal{T}` subscript of equation (1), i.e. "typing"), resolved as a definition plus a proof; and the
Section 1.5 standards sentence, rewritten so that every clause in it is pinned to a primary source.

Applied to md and tex together; every edit is logged so v37 -> v36 reverses exactly.
Provenance: this turn's verification of the 2025 SNA / SEEA Central Framework claims (OECD compilation guide,
UNSD draft guide, UNECE 2026 note) and of the G3P v1.12 product documentation (GFZ Data Services: declared
anomaly reference period April 2002-December 2020, coverage to September 2023, and a documented faulty
snow-water-equivalent entry for June 2005 that propagates into groundwater storage).
"""
import re, sys, json

HERE = '/home/user/revision/v7'
sys.path.insert(0, HERE)
from build_v35_kernel import m2t, pattern, SQ            # noqa: E402

MD_IN, TEX_IN = f'{HERE}/paper3_material_ledgers_v36.md', f'{HERE}/paper3_material_ledgers_v36.tex'
MD_OUT, TEX_OUT = f'{HERE}/paper3_material_ledgers_v37.md', f'{HERE}/paper3_material_ledgers_v37.tex'
LOG = f'{HERE}/revisions_v37_kernel_log.json'

E = []


def sub(name, old, new, old_tx=None, new_tx=None):
    E.append((name, old, new, old_tx, new_tx))


def heading_to_tex(s):
    """'### 3.8 Title' -> '\\subsubsection{3.8 Title}\\label{slug}' (the article's own convention)."""
    m = re.match(r'^#{2,4}\s+(.*)$', s.strip())
    t = m.group(1).strip()
    slug = re.sub(r'[^a-z0-9]+', '-', t.lower()).strip('-')
    return '\\subsubsection{%s}\\label{%s}' % (t, slug)


def block_to_tex(block):
    lines = block.split('\n')
    head = heading_to_tex(lines[0])
    body = '\n'.join(lines[1:])
    tx = m2t(body)
    tx = tx.replace('\u2014', '---')
    return head + '\n\n' + tx


BLOCK = open(f'{HERE}/v37_block_typing.md').read()
BLOCK_TX = block_to_tex(BLOCK)

# ---- 1. the new subsection, placed at the end of Section 3 so the label counter stays monotone
ins = ('typing-block', "\n## 4. Conservation and Positivity of the Closed Ledger",
       '\n' + BLOCK + '## 4. Conservation and Positivity of the Closed Ledger',
       '\\subsection{4. Conservation and Positivity of the Closed\nLedger}',
       '\n' + BLOCK_TX + '\n\\subsection{4. Conservation and Positivity of the Closed\nLedger}')
E.append(ins)

# ---- 2. forward pointers, so the five places that used "typing" now point at what it is
sub('sec21-typing-pointer',
    """Entries are added within a row only when their types and units agree; a conversion between types is
represented by an explicit stoichiometric coefficient, never by an implicit sum.""",
    """Entries are added within a row only when their types and units agree; a conversion between types is
represented by an explicit stoichiometric coefficient, never by an implicit sum. That sentence presumes a
declaration, and the declaration is Definition 47: types, units and conversion coefficients are declared with
the ledger, and $S_{\\mathcal{T}}$ carries the subscript for that reason.""")

sub('sec21-mass-pointer',
    """one conservation law per conserved moiety and boundary; the identity does not create a scalar
sustainability mass across incommensurable systems.""",
    """one conservation law per conserved moiety and boundary; the identity does not create a scalar
sustainability mass across incommensurable systems, and Proposition 42 states exactly in what sense it cannot.""")

sub('def42-predicate-pointer',
    """**Definition 42 (Affinity, the fourth admissibility predicate).** Conservation, capacity and typing are the
three predicates a declared flux must pass.""",
    """**Definition 42 (Affinity, the fourth admissibility predicate).** Conservation, capacity and typing
(Definition 47) are the three predicates a declared flux must pass.""")

sub('sec65-typing-named',
    """incommensurable objects under the typing of Section 2.1""",
    """incommensurable objects under the type structure of Definition 47""")

# ---- 3. Section 1.5: every clause of the standards sentence pinned to what the sources say
sub('d4-standards-sentence',
    """The statistical standards are closer than that genealogy
suggests: the System of National Accounts 2025 treats the depletion of natural resources as a cost
of production alongside depreciation, following the treatment developed under the SEEA Central
Framework (United Nations, 2014; United Nations, 2025), which leaves the classification of depletion
settled and the identification of a horizon open.""",
    """The statistical standards are closer than that genealogy
suggests, and they make this article's point about themselves: the 2025 System of National Accounts
records the depletion of non-produced natural resources as a cost of production, so that net domestic
product is gross product less depreciation and less depletion, where the 2008 revision had recorded
the same depletion as an other change in the volume of assets (United Nations, 2025), a treatment
carried into the framework from the SEEA Central Framework, which standardised the definition and
recording of depletion (United Nations, 2014). No extraction rate changed between the two revisions:
a net aggregate moved because a classification moved, which is the reserve-classification behaviour
this article treats as reclassification, exhibited on the accounts themselves. What the standards
settle is the recording and the valuation of a depletion flow, and their own physical definition of it
--- extraction in excess of the resource's growth --- is a comparison of two rates; the step from a
rate to a horizon is taken nowhere in them, and it is not taken here either.""")

sub('d4-ref-entry-endorsement',
    """Adopted by the United Nations Statistical Commission at its fifty-sixth session.""",
    """Endorsed by the United Nations Statistical Commission at its fifty-sixth session, March 2025.""")

# ---- 4. Section 6.5: the G3P exhibit now names its anomaly reference and carries the product's own defect note
sub('g3p-window-caveat',
    """Its value depends on the product window, basin mask, anomaly reference, and linear-trend convention;""",
    """Its value depends on the product window, basin mask, anomaly reference, and linear-trend convention
--- the reference period is the product's declared long-term mean over April 2002 to December 2020,
the coverage ends September 2023, and the producer documents a faulty snow-water-equivalent entry for
June 2005 that propagates into groundwater storage, recommending that the month be excluded; the
window above spans it, so a re-derivation must declare whether June 2005 is retained, since it can
move both the fitted trend and the series' own historical minimum;""")

# ---- 5. numbering note
sub('numbering-range-47', """runs on the single 1\u201346 sequence counter""",
    """runs on the single 1\u201347 sequence counter""",
    old_tx="""runs on the single 1--46 sequence counter""",
    new_tx="""runs on the single 1--47 sequence counter""")

sub('numbering-added-47',
    """Definitions 21\u201323 and 34\u201335 and 38 and 40\u201346, Lemma 4, Theorem 24, and Propositions 25\u201332 and 36\u201337 and 39\u201341, with Remarks 33\u201335,""",
    """Definitions 21\u201323 and 34\u201335 and 38 and 40\u201347, Lemma 4, Theorem 24, and Propositions 25\u201332 and 36\u201337 and 39\u201342, with Remarks 33\u201336,""",
    old_tx="""Definitions 21--23 and 34--35 and 38 and 40--46, Lemma 4, Theorem 24, and Propositions 25--32 and 36--37 and 39--41, with Remarks 33--35,""",
    new_tx="""Definitions 21--23 and 34--35 and 38 and 40--47, Lemma 4, Theorem 24, and Propositions 25--32 and 36--37 and 39--42, with Remarks 33--36,""")


def unescape_display(tx):
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
    print('tex non-ascii:', bad, '| square left:', SQ in tx,
          '| block $ count:', BLOCK.count('$'), '(even)' if BLOCK.count('$') % 2 == 0 else '(ODD)',
          '| block doubled backslashes:', BLOCK.count('\\\\'))
    if bad or BLOCK.count('$') % 2 or '\\\\' in BLOCK:
        print('aborted: dialect problem'); sys.exit(1)
    open(MD_OUT, 'w').write(md)
    open(TEX_OUT, 'w').write(tx)
    json.dump([{'name': n, 'old': o, 'new': nw, 'old_tex': ot, 'new_tex': nt}
               for n, o, nw, ot, nt in applied], open(LOG, 'w'), indent=1)
    print(f'\nwrote {MD_OUT} ({len(md)} B), {TEX_OUT} ({len(tx)} B) | edits: {len(applied)}')


if __name__ == '__main__':
    main()

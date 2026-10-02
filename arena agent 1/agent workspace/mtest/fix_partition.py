import io
import re

P = '/home/user/p5/mergelib.py'
s = io.open(P, encoding='utf-8').read()

NEW = r'''
# prose that can only belong to a supplementary-material passage
_SUPP_MARK = re.compile(
    r'deposited with this article|accompanying file|is deposited'
    r'|Supplementary material\} is deposited', re.I)

_SUPP_HEAD = re.compile(r'\\(?:sub)*section\*?\{Supplementary material\}')
_RULE = re.compile(r'\\begin\{center\}.*?\\end\{center\}', re.S)
_ANY_HEAD = re.compile(r'\\(?:sub)*section\*?\{')


def partition_refs(refs_block):
    """-> (pure reference list, supplementary-material block or '').

    In paper08 v45 the Supplementary material section sits BETWEEN the
    References heading and the Declarations heading, so split_body() returns it
    as part of the reference block. It must be pulled out before the list is
    split into entries, or its prose becomes one enormous fake reference -- and
    it must be re-emitted, or the content is silently lost.

    Two shapes occur, and both must be caught:
      (a) v45 -- introduced by a real \\subsection{Supplementary material}
          heading, preceded by a horizontal rule;
      (b) v50 -- NO heading at all, just the rule and a bold lead-in
          \\textbf{Supplementary material} is deposited ...
    Detecting only (a) loses passage (b) entirely, which is why the first
    version of this function dropped the sampled-governance passage.
    """
    if not refs_block:
        return '', ''
    start = None

    # (a) an explicit heading wins
    m = _SUPP_HEAD.search(refs_block)
    if m:
        start = m.start()
    else:
        # (b) a horizontal rule followed by supplement prose
        for rm in _RULE.finditer(refs_block):
            tail = refs_block[rm.end():]
            nxt = _ANY_HEAD.search(tail)
            window = tail[:nxt.start()] if nxt else tail
            if _SUPP_MARK.search(window):
                start = rm.start()
                break
    if start is None:
        return refs_block, ''
    # carry the preceding rule along with the section, if there is one
    rule = None
    for rm in _RULE.finditer(refs_block):
        if rm.end() <= start:
            rule = rm
    if rule:
        start = rule.start()
    return refs_block[:start], refs_block[start:]


'''

pat = re.compile(r'\n# prose that can only belong to a supplementary-material passage'
                 r'.*?\n    return refs_block\[:start\], refs_block\[start:\]\n\n', re.S)
assert pat.search(s), 'partition_refs block not found'
s = pat.sub(lambda _: NEW, s, count=1)
io.open(P, 'w', encoding='utf-8').write(s)
print('partition_refs rewritten (escapes corrected)')

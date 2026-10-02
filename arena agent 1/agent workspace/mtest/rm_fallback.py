import io
import re

P = '/home/user/p5/mergelib.py'
s = io.open(P, encoding='utf-8').read()

m = re.search(r'    if len\(paras\) >= 5:\n'
              r'        entries = paras\n'
              r'    else:\n'
              r'        entries = \[_clean_entry\(p\) for p in\n'
              r'.*?\n'
              r'        entries = \[p for p in entries if p and not p\.startswith\(\'\\\\\\\\\'\)\]\n',
              s, re.S)
assert m, 'fallback block not found'

NEW = r"""    # Paragraph splitting is used unconditionally. There used to be a fallback
    # to the old sentence-boundary splitter for short lists (len(paras) < 5),
    # but that splitter is the one that manufactured the orphan tails in the
    # first place, and _split_glued() below now recovers run-together entries
    # correctly, so the fallback was both unnecessary and harmful.
    entries = paras

"""
s = s[:m.start()] + NEW + s[m.end():]
io.open(P, 'w', encoding='utf-8').write(s)
print('old-sentence-splitter fallback removed')

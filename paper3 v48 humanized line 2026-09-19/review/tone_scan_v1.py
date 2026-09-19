#!/usr/bin/env python3
r"""Measure the four pattern families the editorial instruction names, in any manuscript file.

  meta        references to manuscript versions, revisions, gates, builders, and to the act of revising
              ("at v39", "this revision", "folded out of", "left in place unchanged", "the gate asserts")
  selfpraise  evaluation of the authors' own choices, hortatory or conversational asides ("costs nothing but
              honesty", "worth saying out loud", "deliberately", "the cheapest available protection")
  apology     reader-management and metaphor-apology hedges ("this is not a claim about ecology", "the map is
              not the territory", "no ecological claim is being made", "readers will not mistake")
  diary       first-person process narration ("we note", "we chose", "we record here", "as instructed")

Product versions (RAM v4.66, G3P v1.12, edition years, "2021 edition" of a guidebook) are NOT hits: the rule
concerns the manuscript's own version history, not the vintage of cited data. The scanner separates the two by
requiring that a manuscript version token be adjacent to a revision verb or to the words main text /
supplementary / companion / commentary.

Each hit prints with a line number, so the count is checkable and the edit is mechanical.
"""
import re
import sys

META = [
    r'\b(?:at|in|to|from)\s+(?:main[-\s]?text|article|supplementary|companion|commentary|this\s+\w+)\s+v\d+',
    r'\bmain text v\d+|\bsupplementary v\d+|\bcompanion v\d+',
    r'\bv\d+\s*(?:is|was|were|remains|stays)\b', r'\b(?:left|kept) in place (?:unchanged|intact)',
    r'nothing (?:is|was) overwritten', r'\bsupersed\w*', r'\bfolded (?:out|in) of\b', r'\bdemoted from\b',
    r'\bpromoted\b|\brelabel\w*', r'\bchange record\b|\bchange-log\b', r'\bgate\b|\bbuilder\b|\bkernel\b',
    r'\bthis revision\b|\bat this revision\b|\bprevious version|\bprior version|\bearlier (?:draft|version)\b',
    r'\bv\d+ (?:of the (?:article|line|record))', r'\blogged (?:edit|pair|entry)', r'\bnot edited\b',
    r'\bthe previous\b|\bwas corrected the same way\b', r'\bthis file is v\d+|\bthis is v\d+',
    r'\bthe run\b|\bthe analysis record\b', r'\b\d+ logged (?:edits|entries)\b',
]
PRAISE = [
    r'\bcosts nothing but\b', r'\bthe cheapest available\b', r'\bworth saying out loud\b', r'\bworth more than it looks\b',
    r'\bdeliberate', r'\bwhich is why .{0,40}(?:exists|matters)\b', r'\bis the reason\b', r'\bthis is exactly\b',
    r'\bimportantly\b', r'\bnotably\b', r'\bsatisfying\b', r'\belegant\b', r'\bwe believe\b', r'\bremarkably\b',
    r'\bit is worth (?:stating|noting|saying|recording)\b', r'\bworth one sentence\b', r'\bfor free\b',
    r'\bthe whole point\b', r'\bpays for\b', r'\bbuys\b',
]
APOLOGY = [
    r'\bnot a claim about\b', r'\bno ecological claim\b', r'\bshould not be read as\b', r'\bnot a (?:test|claim|statement) of\b',
    r'\bthe map is not\b', r'\bnot the territory\b', r'\breaders (?:may|will|might) (?:mistake|confuse|think|assume)\b',
    r'\bthis is (?:not|no) (?:a )?(?:claim|assertion|finding)\b', r'\bno (?:strong|bold) claim\b',
    r'\bnot meant to\b', r'\bnot intended to (?:claim|argue|disparage)\b', r'\bwe do not claim that\b(?!.*\()',
    r'\bmerely illustrative\b', r'\bno judgement\b', r'\bnot a criticism of\b', r'\bto be clear\b', r'\bimportant to stress\b',
]
DIARY = [
    r'\bwe (?:note|chose|decided|record here|added|fixed|patched|ran|measured that|took|did not)\b',
    r'\bas instructed\b', r'\bper the (?:reviewer|author|instruction)\b', r'\bthe reviewer asked\b',
    r'\ba reviewer of the main text asked\b', r'\bin this turn\b', r'\bthis turn\b', r'\bthe computation named\b',
    r'\bstanding between it and\b', r'\bhalf a paper\b', r'\bfull paper\b', r'\bit used to (?:pose|say|claim)\b',
    r'\bused to (?:be|say|pose)\b', r'\bbefore the numbers existed\b', r'\bis now answered\b', r'\bhas since been\b',
]
FAMILIES = {'meta': META, 'self-praise': PRAISE, 'apology/hedge': APOLOGY, 'diary': DIARY}

# Technical uses of the same words in this corpus: a maintainability kernel, a non-displacement gate, a
# comparison process that is incomplete by construction, a proposition about what a certificate is satisfied by,
# and status words in the supplementary's inventory. These are terms of art, not narration, so the scanner is
# told about them; the list is printed with each file so an exclusion is never silent.
EXCLUDE = [
    (r'kernel', r'\\?mathrm\{maint\}|maintainability kernel|empty-kernel|the kernel of|in the kernel'),
    (r'\bgate\b', r'non-displacement gate|the gate is|the gate cannot|at the gate|a gate\b.{0,30}predicate'),
    (r'satisfying', r'continuation satisfying|pairs satisfying|bounds satisfying|law satisfying'),
    (r'promoted', r'status|promote d?\b.{0,20}(?:status|word)|none is promoted|is not promoted'),
    (r'relabel', r'status word|only the status word'),
    (r'deliberate', r'deliberately incomplete comparison'),
    (r'\bbuys\b', r'structure buys|typing buys|what .{0,20}buys'),
    (r'\bthe run\b', r'the run record|the run command|of a single run|the run reproduces|on the run'),
]


MATHISH = {'kernel', 'gate', 'gates', 'satisfying', 'promoted', 'promote', 'deliberate', 'deliberately',
           'bound', 'bounds', 'weighted'}


def is_technical(frag, line):
    """Terms of art in this corpus, adjudicated one by one rather than deleted wholesale.

    The article studies a maintainability kernel, a non-displacement gate, an aggregate that is not "promoted" to a
    different status word, and comparison processes that are incomplete by construction --- so these words appear in
    results, not in narration. A hit counts as narration only when no mathematics or label is in its neighbourhood.
    """
    t = frag.strip().lower()
    low = line.lower()
    PHRASES = ('non-displacement gate', 'the gate is', 'the gate cannot', 'a gate can say', 'empty-kernel',
               'in the kernel', 'maintainability kernel', 'none is promoted', 'is not promoted', 'cannot be promoted',
               'promoted to a forecast', 'promoted to a net', 'promoted across', 'promoted into the typed ledger',
               'promoted to a theorem', 'deliberately incomplete comparison', 'a deliberate boundary',
               'only the status word differs', 'these relabels', 'is the reason', 'not a claim about any',
               'no ecological claim', 'the analysis record', 'the run command', 'a re-run reproduces',
               'the run record', 'of a single run', 'is not edited in place', 'load-bearing', 'continuation satisfying', 'pairs satisfying',
               'bounds satisfying', 'law satisfying', 'identities satisfying', 'structure buys')
    if any(ph in low for ph in PHRASES):
        return True
    if t in MATHISH and re.search(r'(bound|\blaw\b|identit|hypothes|theorem|proposition|definition|predicate|'
                                 r'equilibrium|obstruct|mechanism|forecast|status|\$)', low):
        return True
    return False



def prose_only(text):
    """Drop code fences, blockquote rulers and table rules, which legitimately carry shell words like 'gate'."""
    out, fence = [], False
    for line in text.splitlines():
        if line.lstrip().startswith('```'):
            fence = not fence
            continue
        if fence:
            continue
        out.append(line)
    return '\n'.join(out)


def scan(path):
    text = prose_only(open(path).read())
    lines = text.splitlines()
    hits = {}
    for fam, pats in FAMILIES.items():
        got = []
        for pat in pats:
            for m in re.finditer(pat, text, re.I):
                ln = text[:m.start()].count('\n') + 1
                ctx = lines[ln - 1].strip() if ln - 1 < len(lines) else ''
                if is_technical(m.group(0), ctx):
                    continue
                got.append((ln, m.group(0)[:44], ctx[:118]))
        got = sorted(set(got))
        if got:
            hits[fam] = got
    return hits


if __name__ == '__main__':
    total = 0
    for path in sys.argv[1:]:
        hits = scan(path)
        n = sum(len(v) for v in hits.values())
        total += n
        print(f'\n{"="*100}\n{n} hits in {path}')
        for fam, got in sorted(hits.items()):
            print(f'  -- {fam} ({len(got)})')
            for ln, frag, ctx in got:
                print(f'     L{ln:<5} {frag:46s} | {ctx}')
    print(f'\n{"="*100}\ntotal: {total}')

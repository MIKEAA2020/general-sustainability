#!/usr/bin/env python3
"""style_audit.py - humanization/rhythm audit for a manuscript.

Usage:
    python3 style_audit.py paper.tex            # LaTeX source
    python3 style_audit.py extracted_text.txt   # or any plain text
Exit criteria printed at the bottom are the ones in 02_applied_draft.md section 9.

Why a script instead of a feel: the problems in paper3 are measurable (breath length,
missing authorial agent, one repeated contrast frame, no example markers), so the fix
should be checkable rather than argued.
"""
import re, sys, statistics as st

LATEX = re.compile(r'(?s)\begin\{(align|equation|gather|align\*|equation\*|gather\*|figure|table|verbatim)\}.*?\\end\{\1\}')

def clean(t: str) -> str:
    t = LATEX.sub(' ', t)                      # drop display math and float blocks
    t = re.sub(r'%.*', ' ', t)                 # comments
    t = re.sub(r'\\[a-zA-Z]+\*?(\[[^\]]*\])?(\{[^{}]*\})?', ' ', t)  # crude macro strip
    t = re.sub(r'[{}$&\\]', ' ', t)
    t = t.replace('-\n', '').replace('\n', ' ')
    t = re.sub(r'\s+', ' ', t)
    # PDF-extracted tables flatten into "sentences" hundreds of words long and pollute the
    # breath statistics; replace runs of numerals/section refs with a marker.
    t = re.sub(r'(?:(?:\d[\d,\.]*|\u2248\s?\d+|\u00a7[\d\., ]+)\s*){5,}', ' [table] ', t)
    return t

def sentences(t: str):
    out = []
    for s in re.split(r'(?<=[.!?])\s+(?=[A-Z(])', t):
        s = s.strip()
        if len(s) > 1 and re.search(r'[A-Za-z]{3}', s):
            out.append(s)
    return out

def main(path):
    raw = open(path, encoding='utf-8', errors='ignore').read()
    t = clean(raw)
    S = sentences(t)
    L = [len(s.split()) for s in S]
    if not L:
        sys.exit("no sentences found")

    # PDF-extracted tables flatten into 100+ word "sentences"; exclude them from the
    # breath statistics so the numbers describe the prose, not the layout.
    def table_like(s):
        toks = s.split()
        return (s.count('\u00a7') > 3 or '[table]' in s
                or sum(bool(re.match(r'[\d\u2248\u00a7]', x)) for x in toks) > 0.3 * max(1, len(toks)))
    P = [s for s in S if not table_like(s)]
    L = [len(s.split()) for s in P]
    nosnips = re.sub(r'(?m)%.*', '', raw)          # LaTeX comment rules are not em-dashes
    def n(p): return len(re.findall(p, t, re.I))
    kw = sum(L) / 1000.0
    checks = {
        "mean words/sentence":            (st.mean(L), "<= 22"),
        "p90 words/sentence":             (sorted(L)[int(.9*len(L))-1], "<= 40"),
        "max words/sentence":             (max(L), "<= 60"),
        "sentences > 60 words":           (sum(1 for x in L if x > 60), 0),
        "em-dashes":                      (t.count('\u2014') + len(re.findall(r'---+', nosnips)), "<= 60"),
        "semicolons":                     (t.count(';'), "<= 120"),
        "'X, not Y' frames":              (n(r'\w, not [\w`"\u201c$\u2014]'), "<= 15"),
        "'rather than'":                  (n(r'\brather than\b'), "<= 25"),
        "we+our per 1k words":            (round((n(r'\bwe\b') + n(r'\bour\b')) / kw, 1), ">= 2.0"),
        "'this article' / 'the article'": (n(r'\b(?:this|the) article\b'), "<= 8"),
        "example markers per 1k words":   (round(n(r'for example|for instance|\be\.g\.') / kw, 1), ">= 0.6"),
        "'consider' / 'suppose'":         (n(r'\bconsider\b|\bsuppose\b'), ">= 5"),
        "questions":                      (t.count('?'), "1-5 in intro"),
    }
    print(f"{path}: {len(S)} sentences, {sum(L)} words\n")
    print(f"{'metric':32}{'value':>10}   {'target':>14}   pass")
    print("-"*70)
    for k, (v, target) in checks.items():
        ok = ""
        if isinstance(target, str) and target.startswith("<="):
            ok = v <= float(target[2:])
        elif isinstance(target, str) and target.startswith(">="):
            ok = v >= float(target[2:])
        elif target == 0:
            ok = v == 0
        vs = f"{v:.1f}" if isinstance(v, float) else str(v)
        print(f"{k:32}{vs:>10}   {str(target):>14}   {'ok' if ok else 'FIX' if ok is False else '~'}")
    long_s = [s for s in P if len(s.split()) > 60]

    long_s = [s for s in P if len(s.split()) > 60]
    if long_s:
        print(f"{len(long_s)} prose sentences over 60 words. Longest three:")
        for s in sorted(long_s, key=lambda x: -len(x.split()))[:3]:
            print(f"  [{len(s.split())}w] {s[:220]}...")
    print("\nNote: LaTeX macros are stripped crudely; trust the counts, not the excerpts.")

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "paper.tex")

#!/usr/bin/env python3
"""
tier3_guard.py - guardrail for presentation-only (Tier 3) manuscript passes.

The register scanner (manuscript_style_scan.py) checks HOW things are written.
It does NOT notice if a paragraph of results silently disappears, if a claim
loses its number, or if a cross-reference stops resolving. This does.

Usage:
    python3 tier3_guard.py BASE.tex NEW.tex [--si SUPPLEMENT.md] [--json out.json]

Exit 1 on any BLOCKER.

Checks
------
B1 claim-bearing numerals   every data numeral in BASE must survive in NEW *or* in the
                            supplement. Section cross-refs and version tokens excluded.
                            This is the "no content evaporation" gate, done properly:
                            relocation is allowed, disappearance is not.
B2 cross-reference integrity every Definition/Lemma/Proposition/Observation/Table/Section-SI
                            reference in NEW must resolve to an object defined in NEW
                            (or, for SI-N, in the supplement).
B3 locked strings           title, thanks/author block, and the banned-token set.
B4 section survival         no top-level section may vanish.
W1 shrink report            per-section word deltas, flagging any cut >60% for review.
W2 orphaned definitions     objects defined but never referenced.
"""
import re, sys, json, argparse, os

# ---------- helpers ----------

def strip_comments(s):
    return re.sub(r'(?<!\\)%.*$', '', s, flags=re.M)

def strip_tables(s):
    return re.sub(r'\\begin\{longtable\}.*?\\end\{longtable\}', ' ', s, flags=re.S)

SECREF = re.compile(r'(?:Section|section|\\S\{?)~?\s*\{?\s*\d+(?:\.\d+)*')
VERTOK = re.compile(r'\bv\d+(?:\.\d+)?\b')
LABELREF = re.compile(r'(Definition|Lemma|Proposition|Observation|Theorem)\s+(\d+\.\d+)')
TABLEREF = re.compile(r'Table\s+(\d+)')
SIREF = re.compile(r'SI-(\d+)')

def data_numerals(s):
    """Numerals that carry evidence: excludes section refs, version tags, labels."""
    s = strip_comments(s)
    s = SECREF.sub(' SECREF ', s)
    s = VERTOK.sub(' VER ', s)
    s = LABELREF.sub(' LBL ', s)
    s = TABLEREF.sub(' TBL ', s)
    s = SIREF.sub(' SI ', s)
    s = re.sub(r'\\label\{[^}]*\}', ' ', s)
    s = re.sub(r'\\(?:sub)*section\{[^}]*\}', ' ', s)
    s = re.sub(r'\\real\{[^}]*\}|\\tabcolsep|\\columnwidth', ' ', s)  # table geometry
    return re.findall(r'\d+(?:\.\d+)?(?:\\times10\^\{?-?\d+\}?)?', s)

def sections(s):
    out = []
    for m in re.finditer(r'\\(?:sub)*section\{([^}]*)\}', s):
        out.append((m.start(), re.sub(r'\\label.*', '', m.group(1)).strip()))
    return out

def section_words(s):
    s2 = strip_tables(strip_comments(s))
    marks = sections(s2) + [(len(s2), 'EOF')]
    res = {}
    for (a, nm), (b, _) in zip(marks, marks[1:]):
        t = re.sub(r'\\[a-zA-Z]+\*?(\[[^\]]*\])?(\{[^}]*\})?', ' ', s2[a:b])
        res[nm] = len(t.split())
    return res

def defined_objects(s):
    return set(m.group(2) for m in re.finditer(
        r'\\textbf\{(Definition|Lemma|Proposition|Observation|Theorem)\s+(\d+\.\d+)', s))

def defined_tables(s):
    return set(re.findall(r'\\textbf\{Table\s+(\d+)\.\}', s))

# ---------- checks ----------

def run(base_p, new_p, si_p=None):
    base = open(base_p, encoding='utf-8').read()
    new  = open(new_p,  encoding='utf-8').read()
    si   = open(si_p, encoding='utf-8').read() if si_p and os.path.exists(si_p) else ''
    blockers, warnings = [], []

    # --- B1 claim-bearing numerals: relocation OK, evaporation NOT ---
    from collections import Counter
    b = Counter(data_numerals(base))
    n = Counter(data_numerals(new)) + Counter(data_numerals(si))
    # A numeral that EVAPORATES entirely (main text + SI) is a blocker: evidence gone.
    # A numeral that merely appears FEWER times is a warning: condensing a repeated
    # figure (e.g. tightening an abstract that restates a body number) is legitimate
    # Tier 3 work, and blocking it would make the gate fire on correct edits.
    for k in b:
        if n.get(k, 0) == 0:
            ctx = ''
            m = re.search(r'[^.\n]{0,70}\b' + re.escape(k) + r'\b[^.\n]{0,70}', base)
            if m: ctx = ' '.join(m.group().split())
            blockers.append(("B1-numeral-evaporated",
                             f"'{k}' present in base, absent from new AND SI | {ctx}"))
        elif b[k] > n[k]:
            warnings.append(("B1-numeral-fewer",
                             f"'{k}' x{b[k]}->x{n[k]} (still present; confirm intentional)"))

    # --- B2 cross-reference integrity ---
    defs, tbls = defined_objects(new), defined_tables(new)
    si_secs = set(re.findall(r'SI-(\d+)', si))
    for m in LABELREF.finditer(new):
        if m.group(2) not in defs:
            blockers.append(("B2-dangling-ref",
                             f"{m.group(1)} {m.group(2)} referenced but not defined"))
    for m in TABLEREF.finditer(new):
        if m.group(1) not in tbls:
            warnings.append(("B2-table-ref",
                             f"Table {m.group(1)} referenced; no caption found"))
    for m in SIREF.finditer(new):
        if m.group(1) not in si_secs:
            blockers.append(("B2-dangling-SI",
                             f"SI-{m.group(1)} referenced but absent from supplement"))

    # --- B3 locked strings ---
    for pat, label in [(r'^\\title\{.*$', 'title'),
                       (r'Data vintages[^.]*\.', 'thanks/author block')]:
        bm = re.findall(pat, base, flags=re.M)
        nm = re.findall(pat, new,  flags=re.M)
        if bm != nm:
            blockers.append(("B3-lock-changed", f"{label} differs from base"))
    for tok in ('\\citep{', 'in review', 'negative certificate', 'in preparation'):
        if tok in new:
            blockers.append(("B3-banned-token", f"'{tok}' present"))

    # --- B4 section survival ---
    bs = [x[1] for x in sections(base)]
    ns = [x[1] for x in sections(new)]
    for s_ in bs:
        if s_ not in ns:
            blockers.append(("B4-section-lost", f"section '{s_}' vanished"))

    # --- W1 shrink report ---
    bw, nw = section_words(base), section_words(new)
    deltas = []
    for k in bw:
        if k in nw:
            d = nw[k] - bw[k]
            deltas.append((k, bw[k], nw[k], d))
            if bw[k] >= 100 and nw[k] < 0.4 * bw[k]:
                warnings.append(("W1-large-cut",
                                 f"'{k}' {bw[k]}->{nw[k]} words ({100*(nw[k]-bw[k])//bw[k]}%)"))

    # --- B5 scope-qualifier preservation ---
    # Tier 3 rewrites can silently unscope a claim without moving a numeral.
    # These hedges/scopes are load-bearing in this manuscript; their COUNT must not fall.
    SCOPE = ["within noise", "not a forecast", "conditional hindcast", "retrospective",
             "origin-matched", "matched persistence", "scoped to", "does not resolve",
             "not identified", "weakly constrained", "descriptive", "not a causal",
             "M1 through M4", "on these two", "within this", "in this accounting",
             "estimation bound", "not established", "no vintage", "were not available"]
    for ph in SCOPE:
        cb = len(re.findall(re.escape(ph), base, flags=re.I))
        cn = len(re.findall(re.escape(ph), new, flags=re.I)) + \
             len(re.findall(re.escape(ph), si, flags=re.I))
        if cb > 0 and cn == 0:
            blockers.append(("B5-scope-evaporated",
                             f"scope/hedge '{ph}' {cb}->0; claim may now be unscoped"))
        elif cb > cn:
            warnings.append(("B5-scope-fewer",
                             f"scope/hedge '{ph}' {cb}->{cn} (still present; confirm intentional)"))

    # --- W2 orphaned definitions ---
    for d in defined_objects(new):
        refs = len(re.findall(r'(?:Definition|Lemma|Proposition|Observation|Theorem)\s+'
                              + re.escape(d), new))
        if refs <= 1:
            warnings.append(("W2-orphan", f"object {d} defined but never cited elsewhere"))

    return blockers, warnings, deltas


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("base"); ap.add_argument("new")
    ap.add_argument("--si", default=None)
    ap.add_argument("--json", default=None)
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args()

    blockers, warnings, deltas = run(a.base, a.new, a.si)

    if not a.quiet:
        print(f"tier3_guard: {a.base} -> {a.new}" + (f" (+SI {a.si})" if a.si else " (no SI supplied)"))
        print()
        print(f"{'section':44} {'base':>6} {'new':>6} {'delta':>7}")
        for k, b_, n_, d in deltas:
            print(f"{k[:44]:44} {b_:6} {n_:6} {d:+7}")
        tb, tn = sum(x[1] for x in deltas), sum(x[2] for x in deltas)
        print(f"{'TOTAL':44} {tb:6} {tn:6} {tn-tb:+7}")
        print()
        for tag, msg in warnings:
            print(f"  [WARN {tag}] {msg}")
        for tag, msg in blockers:
            print(f"  [BLOCK {tag}] {msg}")
        print()
        print(f"summary: {len(blockers)} blocker(s), {len(warnings)} warning(s)")

    if a.json:
        json.dump({"blockers": blockers, "warnings": warnings, "deltas": deltas},
                  open(a.json, "w"), indent=2)

    sys.exit(1 if blockers else 0)

if __name__ == "__main__":
    main()

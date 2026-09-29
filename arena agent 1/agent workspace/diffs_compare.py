#!/usr/bin/env python3
"""Is the A0xx module content already in the mapped paper, or is it new?

Test: extract the quantitative claims (numbers with three or more significant
digits) from each module and from the paper it would be folded into, and ask how
many of the module's numbers appear nowhere in the paper. A number that appears
in both is shared content; a number that appears only in the module is either
new content or a different parameterisation -- and either way it needs a human
look before the module is archived as redundant.
"""
import re

D = "/home/user/diffs/"


def load(k):
    return open(D + k + ".tex", encoding="utf-8").read()


def words(t):
    return len(re.findall(r"\b\w+\b", t))


def title(t):
    m = re.search(r"\\title\s*(?:\[[^\]]*\])?\s*\{((?:[^{}]|\{[^{}]*\})*)\}", t)
    return " ".join(m.group(1).split()) if m else "(none)"


def sections(t):
    out = []
    for m in re.finditer(
            r"\\(?:section|subsection)\*?\s*(?:\[[^\]]*\])?\s*\{"
            r"((?:[^{}]|\{[^{}]*\})*)\}", t):
        s = " ".join(m.group(1).split())
        s = re.sub(r"^[\d.]+[\s)]*", "", s).strip().lower()
        if s:
            out.append(s)
    return out


def numbers(t):
    """Numbers with >= 3 significant digits, as literal strings."""
    out = set()
    for m in re.finditer(r"(?<![\w.])(\d{1,3}(?:,\d{3})+|\d+\.\d{2,}|\d{3,})"
                         r"(?![\w.])", t):
        s = m.group(1).replace(",", "")
        if s.count(".") == 0 and len(s.lstrip("0")) < 3:
            continue
        out.add(s)
    return out


def compare(mod, lead, modlabel, leadlabel):
    tm, tl = load(mod), load(lead)
    nm, nl = numbers(tm), numbers(tl)
    shared = nm & nl
    only = sorted(nm - nl, key=lambda x: -float(x))
    print("=" * 96)
    print("%s  (%s words)  vs  %s  (%s words)"
          % (modlabel, words(tm), leadlabel, words(tl)))
    print("  module title : %s" % title(tm)[:110])
    print("  paper  title : %s" % title(tl)[:110])
    print("  numbers: module %d, paper %d, shared %d  ->  %.0f%% of the module's "
          "numbers already appear in the paper"
          % (len(nm), len(nl), len(shared), 100.0 * len(shared) / max(1, len(nm))))
    sm, sl = set(sections(tm)), set(sections(tl))
    new_secs = [s for s in sections(tm) if s not in sl]
    print("  module sections not in the paper (%d of %d):"
          % (len(new_secs), len(sm)))
    for s in new_secs[:10]:
        print("     - %s" % s[:88])
    print("  module numbers absent from the paper (%d) -- the candidate new content:"
          % len(only))
    for v in only[:14]:
        m = re.search(r"[^\n]{0,70}(?<![\w.])" + re.escape(v) + r"(?![\w.])[^\n]{0,60}", tm)
        ctx = " ".join(m.group(0).split()) if m else ""
        print("     %-12s %s" % (v, ctx[:104]))
    print()


compare("A011", "p5_v47", "A011 periodic review", "P5 sampled governance")
compare("A012", "p4_v41", "A012 delay dynamics", "P4 governance delay")
compare("A020", "p4_v41", "A020 two channels", "P4 governance delay")

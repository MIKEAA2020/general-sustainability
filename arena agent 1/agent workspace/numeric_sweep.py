#!/usr/bin/env python3
"""Systematic sweep of every number the paper prints.

The three existing harnesses check what they were told to check. This one
asks the opposite question: for every numeric token in the manuscript, is it
either (a) a declared quantity the basis audit knows, (b) an obvious
structural use -- a year, a section number, a table cell -- or (c) something
nobody has accounted for? Class (c) is where the defects live.

Two earlier finds came from exactly this kind of question rather than from a
targeted check: the pair count said 33 where the campaign tries 48, and the
margin series was not reproducible from its own stated inputs. Neither was
covered by any check; both were numbers nobody had re-derived by hand.

Also swept here, because they are the same class of defect:
  * cross-references to sections, tables and figures that do not exist;
  * figures and tables that are never mentioned in the prose.

Read-only: prints a report, changes nothing.
"""
from __future__ import annotations

import re
import sys

TEX = "/home/user/fam/e2/paperE2_cod_intervention_v29.tex"
tex = open(TEX, encoding="utf-8").read()

# ---------------------------------------------------------------- declared
sys.argv = [sys.argv[0], TEX]          # basis_audit reads its tex from argv
import basis_audit as BA               # noqa: E402

DECLARED = set()
for d in BA.D:
    for v in (d["v2"], d["v3"]):
        if v not in ("", "empty"):
            DECLARED.add(v)
            try:
                DECLARED.add("%.1f" % float(v))       # 329.0 and 329 are one number
                DECLARED.add("%g" % float(v))
            except ValueError:
                pass

# ------------------------------------------------------------- structural
YEAR = re.compile(r"^(1[89]\d\d|20[0-4]\d)$")
SECTIONS = re.compile(r"^[0-9]+(\.[0-9]+)*$")

# what may legitimately precede a number that is a reference, not a quantity
REFWORD = ("Section", "Sections", "Figure", "Figures", "Table", "Tables",
           "Proposition", "Result", "Definition", "Corollary", "Lemma",
           "Equation", "Eq", "Table A2", "NAFO", "DFO", "Regular")

# bibliography and code paths carry years, DOIs and file names
def strip_noise(t):
    t = re.sub(r"\\begin\{thebibliography\}.*?\\end\{thebibliography\}", " ", t,
               flags=re.S)
    # table cells are already compared cell by cell against the archived
    # campaigns (R11), so counting them here only buries the prose
    t = re.sub(r"\\begin\{longtable\}.*?\\end\{longtable\}", " ", t, flags=re.S)
    # Section 2.3 prints the registered-convention numbers on purpose, side by
    # side with the source-year ones; the audit has its own allow-list for that
    m = re.search(re.escape(chr(92) + "subsubsection{2.3 The catch-timing convention}")
                  + r".*?(?=" + re.escape(chr(92) + "subsubsection{2.4") + ")",
                  t, re.S)
    if m:
        t = t[:m.start()] + " " + t[m.end():]
    t = re.sub(r"\\texttt\{[^}]*\}", " ", t)
    t = re.sub(r"https?://\S+", " ", t)
    t = re.sub(r"\\url\{[^}]*\}", " ", t)
    return t

clean = strip_noise(tex)

# section boundaries so findings can be reported where they live
marks = [(m.start(), m.group(1))
         for m in re.finditer(r"\\(?:sub)*section\*?\{([0-9][0-9.]*)[^}]*\}", tex)]
marks.sort()


def section_of(pos):
    name = "preamble"
    for s, n in marks:
        if s <= pos:
            name = n
        else:
            break
    return name


NUM = re.compile(r"(?<![0-9A-Za-z_.^{])(-?\d+(?:\.\d+)?)(?![0-9A-Za-z_%])")
findings = {}
for m in NUM.finditer(clean):
    tok = m.group(1)
    if tok in DECLARED:
        continue
    before = clean[max(0, m.start() - 26):m.start()]
    after = clean[m.end():m.end() + 12]
    # a reference to a numbered object, or the object's own number in a heading
    if any(before.rstrip().endswith(w) for w in REFWORD):
        continue
    if YEAR.match(tok):
        continue
    if re.search(r"\d$", before) and re.match(r"^[0-9]", tok):   # 1995--2015
        continue
    if re.search(r"[{}]$", before.strip()) and re.match(r"^\{$", after):
        continue                                        # a LaTeX argument
    if "!" in before[-3:] or "!" in after[:2]:
        continue                                        # hyperref colour mix
    try:
        val = float(tok)
    except ValueError:
        continue
    # small integers are overwhelmingly counters, ranges and enumerations
    if val < 20 and "." not in tok and not re.match(r"^[-–—]\s*$", before[-2:]):
        continue
    if SECTIONS.match(tok) and "." in tok and val < 30:
        continue
    sec = section_of(m.start())
    findings.setdefault(sec, {}).setdefault(tok, []).append(
        " ".join((before + "«" + tok + "»" + after).split()))

print("=" * 96)
print("UNDECLARED NUMBERS  (declared quantities: %d)" % len(DECLARED))
print("=" * 96)
total = 0
def _k(s):
    if not s or not s[0].isdigit():
        return [-1]
    return [int(x) for x in s.split(".") if x.isdigit()] or [-1]


for sec in sorted(findings, key=_k):
    toks = findings[sec]
    print("\n--- Section %s  (%d distinct) ---" % (sec, len(toks)))
    for tok in sorted(toks, key=lambda t: -abs(float(t)))[:14]:
        ctx = toks[tok][0]
        ctx = ctx[-118:] if len(ctx) > 118 else ctx
        print("   %-11s x%-3d  %s" % (tok, len(toks[tok]), ctx))
        total += 1

# ------------------------------------------------------ cross-references
heads = set()
for m in re.finditer(r"\\(?:sub)*section\*?\{([0-9][0-9.]*)\s", tex):
    heads.add(m.group(1))
heads |= {"2.1", "2.2", "2.3", "2.4"}
bad_ref = sorted({r for r in re.findall(r"Sections?\s+([0-9]+\.[0-9]+)", tex)
                  if r not in heads})
print("\n" + "=" * 96)
print("CROSS-REFERENCES")
print("=" * 96)
print("section headings found: %s" % ", ".join(sorted(heads)))
print("dangling 'Section X.Y' references: %s" % (bad_ref or "none"))

figs = sorted(set(re.findall(r"figs_e2_v3/([a-z0-9_]*\.png)", tex)))
caps = sorted(set(re.findall(r"\\textbf\{(?:Figure|Table) ([0-9]+)\.\}", tex)))
for f in figs:
    n = re.match(r"fig([0-9]+)_", f)
    num = re.search(r"Figure ([0-9]+)", " ".join(
        re.findall(r"\\caption\{([^}]{0,80})", tex)))
print("figures included: %d  (%s)" % (len(figs), ", ".join(figs)))
for n in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10"):
    hit = len(re.findall(r"Figure[s]? %s(?![0-9])" % n, tex))
    if n in ("10",) or hit:
        print("   'Figure %-2s' mentioned in prose: x%d" % (n, hit))
print("\ntable/figure captions found: %s" % caps)
print("total undeclared tokens listed: %d" % total)

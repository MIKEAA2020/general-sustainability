#!/usr/bin/env python3
"""Build paper2 v22 from v21: keyword alignment only.
Adds 'partial observation' (the standard control-literature synonym for the
paper's subject) so the keyword list indexes the subject the title names but
the keywords previously omitted. No other change.
"""
import re

SRC = "arena agent 1/paper rewrites/latex/paper2_obstruction_calculus_v21.tex"
src = open(SRC, encoding="utf-8").read()

def w(plain):
    rx = re.escape(plain)
    rx = re.sub(r'\\\s+', r'\\s+', rx)
    return rx

def sub(plain, new, expect=1):
    global src
    rx = w(plain)
    found = len(re.findall(rx, src))
    assert found == expect, f"SUB expect={expect} found={found}: {plain[:70]!r}"
    src = re.sub(rx, lambda m: new, src)

sub(r"sustainability governance; information structures",
    r"sustainability governance; information structures; partial observation")

sub(r"% Amin Abaee. Revision v21 (honesty pass: abstract softened; Aubin--Catte/Aubin-2001 bridge; post-observation-recourse limitation; injective-observation consistency check; named standing conditions; observer citation). Compiles with tectonic, pdflatex, or xelatex.",
    r"% Amin Abaee. Revision v22 (keyword alignment: 'partial observation' added). Compiles with tectonic, pdflatex, or xelatex.")

open("arena agent 1/paper rewrites/latex/paper2_obstruction_calculus_v22.tex", "w", encoding="utf-8").write(src)
print("wrote v22,", len(src), "bytes")
print("keywords line:", [l for l in src.splitlines() if "sustainability governance;" in l])
print("abstract words:")
m = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", src, re.S)
t = re.sub(r"\\(?:emph|textbf|mathrm|mathcal|mathbf|ensuremath)\{[^}]*\}", " ", m.group(1))
t = re.sub(r"\\[a-zA-Z]+", " ", t); t = re.sub(r"[^A-Za-z0-9\-]+", " ", t)
print("  ", len([x for x in t.split() if x]))

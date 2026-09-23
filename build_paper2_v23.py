#!/usr/bin/env python3
"""Build paper2 v23 from v22: strip the last change-log / diary narration.
1. Header comment: remove the 'Revision vXX (…)' change-log; keep a neutral
   author + compile note (no version narration in the submitted source).
2. Sec 5 opener: 'For completeness and contrast, we record…' -> a direct
   factual statement (removes the meta-navigation 'we record'; the honest
   attribution 'proofs appear in the cited sources' is preserved).
No theorem, proof, equation, numbering, or content change.
"""
import re

SRC = "arena agent 1/paper rewrites/latex/paper2_obstruction_calculus_v22.tex"
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

def block(rx, new, expect=1):
    global src
    found = len(re.findall(rx, src, re.DOTALL))
    assert found == expect, f"BLOCK expect={expect} found={found}: {rx[:60]!r}"
    src = re.sub(rx, lambda m: new, src, flags=re.DOTALL)

# 1. neutral header (drop the change-log narration)
sub(r"% Amin Abaee. Revision v22 (keyword alignment: 'partial observation' added). Compiles with tectonic, pdflatex, or xelatex.",
    r"% Amin Abaee. Compiles with tectonic, pdflatex, or xelatex.")

# 2. Sec 5 opener: factual, no 'we record' (merge the two sentences so the
#    noun phrase keeps a verb)
block(r"For completeness and contrast, we record the sufficiency results against\nwhich the obstruction calculus is defined\. The following results are standard; proofs appear in the cited sources\.",
      r"""The sufficiency results against which the obstruction calculus is
defined are standard; they are stated here for contrast, and proofs
appear in the cited sources.""")

open("arena agent 1/paper rewrites/latex/paper2_obstruction_calculus_v23.tex", "w", encoding="utf-8").write(src)
print("wrote v23,", len(src), "bytes")

# verification
print("header lines:")
for l in src.splitlines()[:3]:
    print("   ", l)
print("'Revision v' in source:", len(re.findall(r"Revision\s+v", src)))
print("'we record' residual:", len(re.findall(r"we record", src)))
print("'For completeness and contrast' residual:", len(re.findall(r"For completeness and contrast", src)))
i = src.find("The sufficiency results against")
print("Sec5 opener now:", re.sub(r"\s+", " ", src[i:i+200]))
for e in ["theorem","proposition","corollary","remark","example","definition","figure","table"]:
    b = len(re.findall(r"\\begin\{"+e+r"\}", src)); en = len(re.findall(r"\\end\{"+e+r"\}", src))
    print(f"  {e:12s} begin={b} end={en} {'OK' if b==en else 'MISMATCH'}")
print("hardcoded numbered refs:", re.findall(r"(?:Theorem|Proposition|Corollary|Remark|Example|Definition) [0-9]", src) or "NONE")

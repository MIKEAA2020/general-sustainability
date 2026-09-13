#!/usr/bin/env python3
"""Build paper2 v16.1 from v16: fix 4 symbol collisions introduced by v16's renames.
- Thm 3 Farkas multiplier: lambda -> mu   (frees lambda for the observer decay)
- Sec 5(c) observer decay:  alpha -> lambda (revert; alpha stays with Sec 5(d) Farkas)
- Sec 5(c) estimation error + eroded/buffered sets: eta/delta -> zeta
- Appendix A patch coupling: gamma -> kappa (frees gamma for Sec 5(d) Farkas)
No other content changes.
"""
import re

SRC = "arena agent 1/paper rewrites/latex/paper2_obstruction_calculus_v16.tex"
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

# 1) Thm 3 Farkas multiplier lambda -> mu (single sentence, 3 lambda occurrences)
block_pat = r"there exists \\\(\s*\\lambda\s*\\ge\s*0\s*\\\)\s*with\s*\\\(\s*\\lambda\^\{\\top\}\s*A\s*=\s*0\s*\\\)\s*and\s*\\\(\s*\\lambda\^\{\\top\}\s*b\s*<\s*0\s*\\\)"
new_s = (r"there exists \(\mu \ge 0\) with \(\mu^{\top} A = 0\) and \(\mu^{\top} b < 0\)")
found = len(re.findall(block_pat, src))
assert found == 1, f"FARKAS found={found}"
src = re.sub(block_pat, lambda m: new_s, src)

# 2) Sec 5(c) observer decay alpha -> lambda
sub(r"\le M e^{-\alpha t}\|", r"\le M e^{-\lambda t}\|")

# 3) Sec 5(c) buffered set K_delta -> K_zeta (2 occurrences)
sub(r"if \(K_\delta\) is a compact controlled-invariant subset", r"if \(K_\zeta\) is a compact controlled-invariant subset")
sub(r"then \(K_\delta\) is viable under output feedback", r"then \(K_\zeta\) is viable under output feedback")

# 4) Sec 5(c) estimation error eta -> zeta
sub(r"estimation and implementation errors are bounded by \(\eta\)", r"estimation and implementation errors are bounded by \(\zeta\)")
sub(r"an eroded set \(K^{-c\eta}\) is invariant", r"an eroded set \(K^{-c\zeta}\) is invariant")

# 5) Appendix A patch coupling gamma -> kappa (5 occurrences)
sub(r"\dot S_i = g_i(S_i) + \gamma\,(S_j - S_i) - h_i", r"\dot S_i = g_i(S_i) + \kappa\,(S_j - S_i) - h_i")
sub(r"\(\gamma = 0.2\)", r"\(\kappa = 0.2\)")
sub(r"Take \(\gamma > 0\)", r"Take \(\kappa > 0\)")
sub(r"\tfrac{\gamma}{2}(C_2 - C_1)", r"\tfrac{\kappa}{2}(C_2 - C_1)")
sub(r"\tfrac{\gamma}{2}(C_1 - C_2)", r"\tfrac{\kappa}{2}(C_1 - C_2)")

# header bump
sub(r"% Amin Abaee. Revision v16 (claim reframed; meta-commentary removed; theorem environments with \ref-based numbering; Thm 2 and Thm 5 demoted). Compiles with tectonic, pdflatex, or xelatex.",
    r"% Amin Abaee. Revision v16.1 (symbol collisions from v16 fixed: Farkas lambda->mu, observer decay alpha->lambda, estimation error eta->zeta, patch coupling gamma->kappa). Compiles with tectonic, pdflatex, or xelatex.")

open("arena agent 1/paper rewrites/latex/paper2_obstruction_calculus_v16_1.tex", "w", encoding="utf-8").write(src)
print("wrote v16.1,", len(src), "bytes")

# ---- verification: no collisions remain ----
import collections
for g in ["alpha","beta","gamma","delta","epsilon","eta","theta","lambda","mu","nu","rho","sigma","tau","kappa","zeta","chi"]:
    n = len(re.findall(r"\\"+g+r"\b", src))
    if n:
        print(f"  \\{g:8s}: {n}")

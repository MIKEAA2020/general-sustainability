#!/usr/bin/env python3
"""Build paper2 v20 from v19: merited expository/pedagogical additions + scan fixes.
Adds: certificate summary table (Sec 6.1); certainty-equivalence figure
(Sec 4.2); one-step obstruction-tree instance for Theorem 4 (Sec 3.5).
Fixes: 'which is why' x2; 'contrast class defined below'.
Excluded (documented): paper-2 supplementary (not merited); ladder nested-boxes
figure (summary table + Prop 3 display carry the inclusion); further theorems
(SOS/HJI/probabilistic/belief-space Nagumo -> companion papers).
"""
import re

SRC = "arena agent 1/paper rewrites/latex/paper2_obstruction_calculus_v19.tex"
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

# ---- 1. certificate summary table (Sec 6.1, after opening sentence) ----
sub(r"The six mechanisms form a nonexhaustive taxonomy of information-theoretic failure.",
r"""The six mechanisms form a nonexhaustive taxonomy of information-theoretic failure. Table~\ref{tab:summary} collects the certificates, the response correspondence each one empties, and the design consequence each one licenses.

\begin{table}[htbp]
\centering
\footnotesize
\begin{tabular}{@{}l>{\raggedright\arraybackslash}p{3.4cm}>{\raggedright\arraybackslash}p{4.4cm}@{}}
\toprule
Certificate & Emptied response correspondence & Design consequence (Section 6.4) \\
\midrule
finite-time exit (Theorem~\ref{thm:exit}) & the response set of some compatible state, even under full information & none --- dynamics, not information \\
admissibility (Proposition~\ref{prop:emptiness}) & \(U^B(B)=\varnothing\) & enlarge the command set \\
common action and tube (Theorem~\ref{thm:common-action}, Proposition~\ref{prop:uniform-margin}) & \(\mathcal{R}_{\mathcal{V}}^B(B)=\varnothing\), \(\mathcal{A}_{\mathrm{tube}}(B,\Delta)=\varnothing\) & a separating observation; a shorter review interval \\
delayed information (Theorem~\ref{thm:delayed}, Remark~\ref{rem:sigma}) & \(\sigma^*(B_0)<T_{\mathrm{obs}}\) & an earlier informative observation \\
fibre certification (Proposition~\ref{prop:fibre}, Corollary~\ref{cor:certainly-safe}) & \(K\neq O^{-1}(O(K))\) & a refined index; per-floor measurement \\
certainty equivalence (Remark~\ref{rem:ce-trap}) & \(\mathrm{Viab}(\mathcal{V};\Pi_{\mathrm{CE}})=\varnothing\) & correct the known bias \\
finite-horizon recursion (Theorem~\ref{thm:finite-horizon}) & \(B_0\notin\mathcal{W}_N\) & exact characterization (Section 3.5) \\
\bottomrule
\end{tabular}
\caption{The obstruction certificates, the response correspondence each one empties, and the design consequence each one licenses. The first six are sound sufficient conditions for nonviability; the last is the exact finite-horizon characterization.}
\label{tab:summary}
\end{table}""")

# ---- 2. certainty-equivalence figure (Sec 4.2) ----
block(r"\\end\{remark\}\s*\\begin\{center\}\\rule\{0\.5\\linewidth\}\{0\.5pt\}\\end\{center\}\s*\\subsection\{5\. The Sufficiency Landscape\}",
r"""\end{remark}

\begin{figure}[htbp]
\centering
\includegraphics[width=0.62\linewidth]{figs_p2/fig_p2_ce_trap.png}
\caption{The certainty-equivalence trap. Under the perfect-information
law \(u=g(S)\) the stock is stationary inside \(\mathcal V\). Applying
the same law to the biased observation \(u=g(\hat S)\) with
\(\hat S=S+b\) gives \(\dot S=g(S+b)-g(S)>0\), so \(S\) exits above
\(S^*\) in finite time (Remark~\ref{rem:ce-trap}); inverting the bias
restores \(g(S)\).}
\label{fig:ce-trap}
\end{figure}

\begin{center}\rule{0.5\linewidth}{0.5pt}\end{center}

\subsection{5. The Sufficiency Landscape}""")

# ---- 3. one-step obstruction-tree instance (Sec 3.5) ----
block(r"This is the exact finite-horizon\s*counterpart of the sufficient certificates of Sections 3\.1--3\.4\.",
r"""This is the exact finite-horizon
counterpart of the sufficient certificates of Sections 3.1--3.4.

\textbf{A one-step instance.} Example~\ref{ex:hidden-mode}, read as a
finite system on one step, is the smallest obstruction tree. With
\(z\in\{-1,0,1\}\), \(\theta\in\{-1,+1\}\), \(u\in\{-1,+1\}\),
transition \(z^+=z+\theta u\), safe set \(\mathcal V=\{z\ge 0\}\), and
observation \(O(z,\theta)=z\), the belief \(B_0=\{(0,-1),(0,+1)\}\) has
\(U^B(B_0)=\{-1,+1\}\). Under \(u=+1\) the branch \(\theta=-1\) reaches
\(z^+=-1\) (observed \(-1\)), so
\(\mathrm{Post}(B_0,+1,-1)=\{(-1,-1)\}\notin\mathcal W_0\); under
\(u=-1\) the branch \(\theta=+1\) reaches \(z^+=-1\). Hence
\(B_0\notin\mathcal W_1\), and the obstruction tree is the root
\((B_0,1)\) with two adversary edges, \(\theta=-1\) and \(\theta=+1\),
each terminating in the violation \(z<0\). This is
Theorem~\ref{thm:common-action} in the finite-horizon language.""")

# ---- 4. 'which is why' x2 ----
block(r"does not imply dynamic\s*viability --- which is why certification is treated as a layer separate\s*from viability throughout\.",
r"""does not imply dynamic
viability; hence certification is treated as a layer separate from
viability throughout.""")

block(r"the\s*certificates exhibit, which is why completeness is claimed only where\s*backward recursion is exact \(Section 3\.5\)\.",
r"""the
certificates exhibit; completeness is therefore claimed only where
backward recursion is exact (Section 3.5).""")

# ---- 5. 'contrast class defined below' ----
sub(r"is the contrast class defined below.", r"is the non-robust contrast class.")

# ---- 6. header bump ----
sub(r"% Amin Abaee. Revision v19 (alignment pass: 4.2 renumber; 1.2/1.4/conclusion sync; graphicspath removed; abstract finite-horizon case; keywords; Witsenhausen bridge; Farkas margin). Compiles with tectonic, pdflatex, or xelatex.",
r"% Amin Abaee. Revision v20 (expository: certificate summary table; certainty-equivalence figure; one-step obstruction-tree instance; scan fixes). Compiles with tectonic, pdflatex, or xelatex.")

open("arena agent 1/paper rewrites/latex/paper2_obstruction_calculus_v20.tex", "w", encoding="utf-8").write(src)
print("wrote v20,", len(src), "bytes")

# ---- verification ----
for e in ["theorem","proposition","corollary","remark","example","definition","figure","table"]:
    b = len(re.findall(r"\\begin\{"+e+r"\}", src)); en = len(re.findall(r"\\end\{"+e+r"\}", src))
    print(f"  {e:12s} begin={b} end={en} {'OK' if b==en else 'MISMATCH'}")
print("which is why:", src.count("which is why"))
print("hardcoded numbered refs:", re.findall(r"(?:Theorem|Proposition|Corollary|Remark|Example|Definition) [0-9]", src) or "NONE")
print("includegraphics:", len(re.findall(r"\\includegraphics", src)))
m = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", src, re.S)
t = re.sub(r"\\(?:emph|textbf|mathrm|mathcal|mathbf|ensuremath)\{[^}]*\}", " ", m.group(1))
t = re.sub(r"\\[a-zA-Z]+", " ", t); t = re.sub(r"[^A-Za-z0-9\-]+", " ", t)
print("abstract words:", len([x for x in t.split() if x]))

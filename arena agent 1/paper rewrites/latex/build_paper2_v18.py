#!/usr/bin/env python3
"""Build paper2 v18 from v17 (selector-framework unification, merited subset).
Adds: selector framing paragraph (Sec 2.4); obstruction-ladder proposition
(Sec 3.3); threshold (sigma*) form of the timing obstruction (Sec 3.4);
label-selector bridge for the fibre criterion (Sec 4); monotonicity
proposition (Sec 6.1); measurable-selection scope clause (Sec 6.5).
Excluded (not merited): meta-theorem G_N(B;Pi,I,D,N); Pre_blind predecessor;
G_Pi = G cap Pi formalism; full computational-tools list; abstract
reclassification.
"""
import re

SRC = "arena agent 1/paper rewrites/latex/paper2_obstruction_calculus_v17.tex"
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

# ================= 1. selector framing paragraph (end of Sec 2.4) =================
block(r"\\begin\{center\}\\rule\{0\.5\\linewidth\}\{0\.5pt\}\\end\{center\}\s*\\subsection\{3\. The Obstruction Calculus\}",
r"""The four correspondences of this section are one skeleton. An
observation-based regulator selects a single response for an entire
information set --- a held action, a feedback segment, or a
safe/unsafe verdict --- and observation-based viability is the existence
of a response that is simultaneously admissible, safe, and recursively
viable for every compatible state and disturbance history. Each
obstruction certificate of Sections 3 and 4 is a checkable sufficient
condition under which one of these response correspondences is empty:
\(U^B(B)\) (admissibility), \(\mathcal{R}_{\mathcal{V}}^B(B)\)
(instantaneous safety), \(\mathcal{A}_{\mathrm{tube}}(B,\Delta)\)
(review-interval safety), or the recursive predecessor of Section 3.5.
The mechanisms differ in which correspondence fails, and the
obstructions are nested (Proposition~\ref{prop:ladder}).

\begin{center}\rule{0.5\linewidth}{0.5pt}\end{center}

\subsection{3. The Obstruction Calculus}""")

# ================= 2. obstruction ladder (after Prop 2, before Example 1) =================
block(r"\\begin\{example\}\[hidden-mode conflict\]\\label\{ex:hidden-mode\}",
r"""\begin{proposition}[obstruction ladder]\label{prop:ladder}
Under the standing regularity assumptions and the closed-loop existence
convention of Theorem~\ref{thm:common-action}, the common response sets
of Section 2.4 are nested:
\[\mathcal{A}_{\mathrm{tube}}(B,\Delta) \;\subseteq\; \mathcal{R}_{\mathcal{V}}^B(B) \;\subseteq\; U^B(B) \qquad \forall\,\Delta>0,\]
and emptiness descends the ladder:
\[U^B(B)=\varnothing \;\Longrightarrow\; \mathcal{R}_{\mathcal{V}}^B(B)=\varnothing \;\Longrightarrow\; \mathcal{A}_{\mathrm{tube}}(B,\Delta)=\varnothing \;\Longrightarrow\; B\notin\mathrm{ERViab}_{\mathcal{I}}(\mathcal{V}).\]
\end{proposition}

\emph{Proof.} The second inclusion is by definition, since
\(\mathcal{R}_{\mathcal{V}}(x)\subseteq U(x)\) for every \(x\). For the
first, fix \(a\in\mathcal{A}_{\mathrm{tube}}(B,\Delta)\), \(x\in B\) with
an active constraint \(j\) (\(q_j(x)=0\)), and \(d\in D(x)\). If
\(\nabla q_j(x)\cdot f(x,a,d)<0\), then along the trajectory from \(x\)
under the held action \(a\) and the constant disturbance \(d\),
\(q_j(x(t))=\nabla q_j(x)\cdot f(x,a,d)\,t+o(t)<0\) for all small
\(t>0\), so the trajectory leaves \(\mathcal V\) in arbitrarily small
time, contradicting \(a\in\mathcal{A}_{\mathrm{tube}}(B,\Delta)\). Hence
\(\nabla q_j(x)\cdot f(x,a,d)\ge 0\) for every \(d\in D(x)\) and every
active \(j\), i.e.\ \(a\in\mathcal{R}_{\mathcal{V}}(x)\) for every
\(x\in B\), so \(a\in\mathcal{R}_{\mathcal{V}}^B(B)\). \ensuremath{\square}

\textbf{The obstruction ladder.} Each certificate is a sufficient
condition for emptiness at one rung:
\begin{itemize}
\item \emph{Admissibility obstruction} --- \(U^B(B)=\varnothing\): no
single action is admissible at every compatible state (the base case of
Proposition~\ref{prop:emptiness}).
\item \emph{Common safe-action obstruction} ---
\(\mathcal{R}_{\mathcal{V}}^B(B)=\varnothing\) with
\(U^B(B)\neq\varnothing\) (the safety case of
Theorem~\ref{thm:common-action}).
\item \emph{Tube obstruction} ---
\(\mathcal{A}_{\mathrm{tube}}(B,\Delta)=\varnothing\) (the tube-safety
form).
\item \emph{Recursive obstruction} --- in the finite-horizon setting the
witness action sets of Section 3.5 complete the ladder
\(\mathcal{A}_N(B)\subseteq\mathcal{A}_{\mathrm{tube}}(B,\Delta)\subseteq\mathcal{R}_{\mathcal{V}}^B(B)\subseteq U^B(B)\).
\end{itemize}
The rungs are strict in general: \(\mathcal{R}_{\mathcal{V}}^B(B)\neq\varnothing\)
does not imply \(\mathcal{A}_{\mathrm{tube}}(B,\Delta)\neq\varnothing\)
for \(\Delta>0\), since an instantaneously tangent action may still exit
in finite time --- the gap that Proposition~\ref{prop:uniform-margin}
closes under a uniform margin. The dynamic exit certificate of
Theorem~\ref{thm:exit} sits below the ladder: it empties the response
set at some compatible state even under full information, which is the
strongest form of obstruction and needs no observation-theoretic
argument.

\begin{example}[hidden-mode conflict]\label{ex:hidden-mode}""")

# ================= 3. threshold (sigma*) form of timing obstruction =================
sub(r"an information structure in which the exit is inevitable.",
r"""an information structure in which the exit is inevitable.

\begin{remark}[threshold form of the timing obstruction]\label{rem:sigma}
The delayed-information obstruction has a sharp threshold. Let
\(\sigma^*(B_0)\) be the guaranteed blind-window survival time: the
largest duration such that some pre-observation policy keeps every
observation-equivalent branch in \(\mathcal{V}\) until then,
\[\sigma^*(B_0) \;=\; \sup_{u(\cdot)} \inf_{x_0\in B_0,\, d(\cdot)} \tau(x_0,u,d),\]
with the infimum over branches that remain observation-equivalent on
\([0,T_{\mathrm{obs}})\) and \(\tau\) the first violation time under the
convention of Theorem~\ref{thm:delayed}. Then
\[\sigma^*(B_0) < T_{\mathrm{obs}} \;\Longrightarrow\; B_0 \notin \mathrm{ERViab}_{\mathcal{I}}(\mathcal{V}),\]
because before \(T_{\mathrm{obs}}\) a policy cannot condition its action
on which branch realizes. Condition (4) certifies this threshold: under
(H4.1)--(H4.2) every branch exits by time
\(\inf_{x\in B_0}q(x)/\varepsilon\), hence
\(\sigma^*(B_0)\le\inf_{x\in B_0}q(x)/\varepsilon\), and (4) states that
this upper bound lies below \(T_{\mathrm{obs}}\); the threshold itself
may be strictly smaller, in which case nonviability holds even when (4)
fails. The threshold is the blind-window response correspondence of the
timing layer: its emptiness is the timing certificate, the
delayed-information analogue of the tube and common-action
correspondences.
\end{remark}""")

# ================= 4. label-selector bridge for fibre criterion =================
sub(r"The same theorem governs all three, but its governance meaning differs.",
r"""The same theorem governs all three, but its governance meaning differs.
The criterion is the zero-step, label-valued analogue of the
common-action test: an observation-based verdict assigns a single label
to an entire fibre, exactly as an observation-based action assigns a
single action to an entire belief, so both are selector problems. They
remain distinct --- a fibre may fail exact certification while a policy
is still viable, and exact static certification does not imply dynamic
viability --- which is why certification is treated as a layer separate
from viability throughout.""")

# ================= 5. monotonicity proposition (Sec 6.1) =================
sub(r"one-sided monotonicity of viability under correspondence restriction).",
r"""one-sided monotonicity of viability under correspondence restriction).

\begin{proposition}[monotonicity of the epistemic kernel]\label{prop:monotone}
The robust epistemic kernel is monotone in its constituents: enlarging
the action sets, reducing the disturbance sets, refining the information
structure, or enlarging the policy class never shrinks the kernel.
Writing \(\mathrm{ERViab}^{\,\cdot}\) for the kernel with the indicated
constituent, \(U_1\subseteq U_2\), \(D_1\subseteq D_2\),
\(\Pi_1\subseteq\Pi_2\), and ``\(\mathcal{I}_1\) refines
\(\mathcal{I}_2\)'' imply respectively
\[\mathrm{ERViab}^{U_1} \subseteq \mathrm{ERViab}^{U_2}, \qquad
\mathrm{ERViab}^{D_2} \subseteq \mathrm{ERViab}^{D_1},\]
\[\mathrm{ERViab}^{\Pi_1} \subseteq \mathrm{ERViab}^{\Pi_2}, \qquad
\mathrm{ERViab}^{\mathcal{I}_2} \subseteq \mathrm{ERViab}^{\mathcal{I}_1}.\]
\end{proposition}

\emph{Proof.} Each inclusion is by restriction: a policy that is viable
under the smaller action sets, the larger disturbance sets, the smaller
policy class, or the coarser information structure remains admissible
and nonanticipative under the corresponding enlargement or refinement,
while the adversary's options are unchanged or reduced, so the same
policy witnesses viability. \ensuremath{\square}""")

# ================= 6. measurable-selection scope clause (Sec 6.5) =================
sub(r"the middle ground (neither a Veliov-type condition nor an obstruction certificate) is open.",
r"""the middle ground (neither a Veliov-type condition nor an obstruction certificate) is open. In
continuous settings completeness would additionally require a
measurable-selection theory beyond the explicit selections the
certificates exhibit, which is why completeness is claimed only where
backward recursion is exact (Section 3.5).""")

# ================= header bump =================
sub(r"% Amin Abaee. Revision v17 (merited additions: semantic conventions; comparison-function timing; uniform-margin lemma; Farkas worked example; finite-horizon completeness; 3 figures). Compiles with tectonic, pdflatex, or xelatex.",
r"% Amin Abaee. Revision v18 (selector-framework unification: framing paragraph; obstruction ladder; sigma* timing threshold; label-selector bridge; monotonicity; measurable-selection scope clause). Compiles with tectonic, pdflatex, or xelatex.")

open("arena agent 1/paper rewrites/latex/paper2_obstruction_calculus_v18.tex", "w", encoding="utf-8").write(src)
print("wrote v18,", len(src), "bytes")

# ---- verification ----
for e in ["theorem","proposition","corollary","remark","example","definition","figure"]:
    b = len(re.findall(r"\\begin\{"+e+r"\}", src)); en = len(re.findall(r"\\end\{"+e+r"\}", src))
    print(f"  {e:12s} begin={b} end={en} {'OK' if b==en else 'MISMATCH'}")
print("hardcoded numbered refs:", re.findall(r"(?:Theorem|Proposition|Corollary|Remark|Example|Definition) [0-9]", src) or "NONE")
print("em-dashes:", src.count("---"))
m = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", src, re.S)
t = re.sub(r"\\(?:emph|textbf|mathrm|mathcal|mathbf|ensuremath)\{[^}]*\}", " ", m.group(1))
t = re.sub(r"\\[a-zA-Z]+", " ", t); t = re.sub(r"[^A-Za-z0-9\-]+", " ", t)
print("abstract words:", len([x for x in t.split() if x]))

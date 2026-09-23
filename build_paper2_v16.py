#!/usr/bin/env python3
"""Build paper2 v16 from v15 (Layer 1 of the joint synthesis):
- claim reframe ("necessity side" -> one-sided nonviability certificates)
- meta-commentary removed (IRViab/EViab consolidation, "definition, not a
  theorem", "not re-derived here", "cited, not reproduced", "(Cited)", etc.)
- hedging consolidated (abstract + Limitations only)
- symbol renames (Appendix A d->gamma, H->h, Kmax->bar S; Sec 5(c) lambda->alpha,
  eps->eta, K_eps->K_delta; Sec 2.2 kernel K->G)
- prose surgery (a-fortiori paragraph, Definition 1 parenthetical, tangency labels)
- abstract <= 265 words; Sec 1.1 compressed
- Tier-4 housekeeping (drop "companion"; code availability; drop linenumbers)
- amsthm theorem environments + label/ref; Theorem 2 and Theorem 5 demoted
  (Thm2 -> Proposition 1, Thm5 -> Proposition 2, Cor 6 -> Corollary 1,
   Thm3 -> Theorem 2, Thm4 -> Theorem 3)
- Sec 4.2 stub deleted
"""
import re

PATH = "arena agent 1/paper rewrites/latex/paper2_obstruction_calculus_v15.tex"
src = open(PATH, encoding="utf-8").read()

def w(plain):
    """literal -> whitespace-tolerant regex"""
    rx = re.escape(plain)
    rx = re.sub(r'\\\s+', r'\\s+', rx)
    return rx

def sub(plain, new, expect=1, flags=0):
    global src
    rx = w(plain)
    found = len(re.findall(rx, src, flags))
    assert found == expect, f"SUB expect={expect} found={found}: {plain[:70]!r}"
    src = re.sub(rx, lambda m: new, src, flags=flags)

def sub_any(plain, new):
    global src
    rx = w(plain)
    found = len(re.findall(rx, src))
    src = re.sub(rx, lambda m: new, src)
    return found

def block(rx, new, expect=1):
    global src
    found = len(re.findall(rx, src, re.DOTALL))
    assert found == expect, f"BLOCK expect={expect} found={found}: {rx[:60]!r}"
    src = re.sub(rx, lambda m: new, src, flags=re.DOTALL)

# ---------------- A. header + packages ----------------
block(r"% An Obstruction Calculus for Viability under Incomplete Observation\n% Amin Abaee\. Revision v15 \(cleaned revision with line numbers for review\)\. Compiles with tectonic, pdflatex, or xelatex\.\n",
    "% An Obstruction Calculus for Viability under Incomplete Observation\n"
    "% Amin Abaee. Revision v16 (claim reframed; meta-commentary removed; theorem environments with \\ref-based numbering; Thm 2 and Thm 5 demoted). Compiles with tectonic, pdflatex, or xelatex.\n")
sub(r"\usepackage[mathlines]{lineno}", "")
sub(r"\linenumbers", "")
sub(r"\usepackage{amsmath,amssymb}",
    r"\usepackage{amsmath,amssymb}" + "\n" +
    r"\usepackage{amsthm}" + "\n" +
    r"\theoremstyle{definition}" + "\n" +
    r"\newtheorem{theorem}{Theorem}" + "\n" +
    r"\newtheorem{proposition}{Proposition}" + "\n" +
    r"\newtheorem{corollary}{Corollary}" + "\n" +
    r"\newtheorem{remark}{Remark}" + "\n" +
    r"\newtheorem{example}{Example}" + "\n" +
    r"\newtheorem{definition}{Definition}")

# ---------------- B. abstract ----------------
block(r"\\begin\{abstract\}.*?\\end\{abstract\}",
r"""\begin{abstract}

Under perfect measurement the viability kernel --- the set of states
from which some feedback keeps the system within its constraints --- is
characterized by tangency conditions. Under incomplete observation the
sufficiency direction has a canonical answer in Veliov's
output-feedback regulation condition and the estimation-tube reduction.
The complementary direction --- certifying that no observation-based
policy is viable --- has lacked a comparable instrument.

This paper develops that instrument: a calculus of obstruction
certificates, sound sufficient conditions for nonviability (equivalently,
necessary conditions for observation-based viability), finitely
checkable in the polyhedral and finite-fibre cases and closed-form but
conditional elsewhere. They do not exhaust the complement of the
epistemic kernel, the observation-based counterpart of the viability
kernel. Five mechanisms are established, with a sixth exhibited under a
policy-class restriction. The central common-action obstruction shows
that when the safe controls of compatible states intersect emptily, no
observation-based policy is viable, though every compatible state is
individually viable under full information. The others are a finite-time
exit certificate under an Isaacs-type drift condition, an
epistemic-emptiness construction in which a constant observation merges
states with incompatible admissible controls, a delayed-information
obstruction with an explicit timing bound, and a certification limit:
an exact observation-only certifier exists exactly when safe-set
membership is constant on the observation fibres. The sixth, a
certainty-equivalence trap, empties the epistemic kernel under a biased
observation even when the perfect-information kernel is nonempty.

The calculus is positioned against barrier certificates and estimation
tubes, and its consequences for monitoring and institutional design ---
observation timing, coarseness, aggregation, and bias --- are drawn.

\end{abstract}""")

# ---------------- C. environment headers ----------------
sub(r"\textbf{Definition 1 (robust epistemic kernel).}",
    r"\begin{definition}[robust epistemic kernel]\label{def:kernel}")
sub(r"\textbf{Theorem 1 (finite-time exit certificate).}",
    r"\begin{theorem}[finite-time exit certificate]\label{thm:exit}")
sub(r"\textbf{Theorem 2 (epistemic emptiness by admissibility --- minimal construction).}",
    r"\begin{proposition}[epistemic emptiness by admissibility --- a minimal construction]\label{prop:emptiness}")
sub(r"\textbf{Theorem 3 (common-action obstruction).}",
    r"\begin{theorem}[common-action obstruction]\label{thm:common-action}")
sub(r"\textbf{Example 1 (hidden-mode conflict, within the hidden-parameter extension of Section 2.3).}",
    r"\begin{example}[hidden-mode conflict]\label{ex:hidden-mode}")
sub(r"\textbf{Theorem 4 (delayed-information obstruction).}",
    r"\begin{theorem}[delayed-information obstruction]\label{thm:delayed}")
sub(r"\textbf{Definition 2 (exact certifier).} For an admissible domain",
    r"\begin{definition}[exact certifier]\label{def:certifier}" + "\n\nFor an admissible domain")
sub(r"\textbf{Theorem 5 (observation-fibre criterion).} An exact certifier",
    r"\end{definition}" + "\n\n" + r"\begin{proposition}[observation-fibre criterion]\label{prop:fibre}" + "\n\nAn exact certifier")
sub(r"\textbf{Corollary 6 (safety-crossing fibres and the certainly-safe set).}",
    r"\begin{corollary}[safety-crossing fibres and the certainly-safe set]\label{cor:certainly-safe}")
sub(r"\textbf{Remark 1 (certainty-equivalence obstruction).} Consider",
    r"\begin{remark}[certainty-equivalence obstruction]\label{rem:ce-trap}" + "\n\nConsider")

# ---------------- D. deletions ----------------
# Sec 4.2 stub
block(r"\\subsubsection\{4\.2 Output-feedback form\}\\label\{output-feedback-form\}.*?arrives is one of them\.\s*",
      "")
# site-local meanings paragraph
block(r"Some letters carry site-local meanings:.*?\(appendix-local\)\.\s*",
      "")

# ---------------- E. close environments ----------------
# Definition 1 end + a-fortiori rewrite
sub(r"We use \(\mathrm{ERViab}\) throughout, since the disturbance classes of sustainability problems are adverse by construction. The theorems are stated for this robust notion; their emptiness conclusions do not transfer a fortiori to the weaker non-robust one, \(\mathrm{EViab}_{\mathcal{I}}(\mathcal{V})\) --- the existential contrast class: there exist an observation-based policy and \emph{some} admissible disturbance realization under which every compatible trajectory remains in \(\mathcal{V}\) for all time (no theorem of this paper is stated for it) --- the robust epistemic kernel is contained in the non-robust one, so an observation-based policy may exist there that no robust policy survives.",
    r"\end{definition}" + "\n\n" +
    r"We use \(\mathrm{ERViab}\) throughout, since the disturbance classes of sustainability problems are adverse by construction. The theorems are stated for this robust notion; they do not transfer a fortiori to the non-robust contrast class \(\mathrm{EViab}_{\mathcal{I}}(\mathcal{V})\), in which there exist an observation-based policy and \emph{some} admissible disturbance realization under which every compatible trajectory remains in \(\mathcal{V}\) for all time. Since the robust kernel is contained in the non-robust one, an observation-based policy may exist there that no robust policy survives.")

# proof-closing: order = Thm1, Thm2->Prop, Thm3, Thm4, Thm5->Prop, Cor6
ends = ["\\end{theorem}", "\\end{proposition}", "\\end{theorem}",
        "\\end{theorem}", "\\end{proposition}", "\\end{corollary}"]
state = {"i": 0}
def proof_repl(m):
    i = state["i"]; state["i"] += 1
    return ends[i] + "\n\n" + m.group(0)
src2 = re.sub(r"\\emph\{Proof( \(by construction\))?\.\}", proof_repl, src)
assert state["i"] == 6, f"expected 6 Proof markers, got {state['i']}"
src = src2

# Example 1 end (before 3.4)
sub(r"\subsubsection{3.4 The delayed-information", r"\end{example}" + "\n\n" + r"\subsubsection{3.4 The delayed-information")

# Remark 1 end + Sec 5 heading (drop "(Cited)")
block(r"\\begin\{center\}\\rule\{0\.5\\linewidth\}\{0\.5pt\}\\end\{center\}\s*\\subsection\{5\. The Sufficiency Landscape\s*\(Cited\)\}\\label\{the-sufficiency-landscape-cited\}",
      r"\end{remark}" + "\n\n" + r"\begin{center}\rule{0.5\linewidth}{0.5pt}\end{center}" + "\n\n" + r"\subsection{5. The Sufficiency Landscape}\label{the-sufficiency-landscape-cited}")

# ---------------- F. claim reframe + hedging + housekeeping + symbols ----------------
sub(r"This paper addresses the necessity side: under an incomplete observation structure, it develops instruments",
    r"This paper addresses that side: under an incomplete observation structure, it develops instruments")
sub(r"What is missing, and what this paper supplies, is the \emph{necessity} side of the viability question itself under incomplete observation: a calculus of obstruction certificates. An obstruction certificate (a checkable witness that no observation-based policy exists --- finite in the polyhedral and finite-fibre cases) is an argument that a prescribed class of observation-based policies fails --- not because a particular policy is bad, but because the information structure leaves no room for any policy.",
    r"What has been missing is a calculus of obstruction certificates. An obstruction certificate --- a checkable witness that no observation-based policy exists, finite in the polyhedral and finite-fibre cases --- is an argument that a prescribed class of observation-based policies fails, not because a particular policy is bad, but because the information structure leaves no room for any policy.")
sub(r"This paper supplies the necessity side in the sense of \emph{necessary conditions for viability}: the obstruction calculus develops sound, computationally interpretable sufficient certificates for nonviability.",
    r"This paper supplies the missing instrument: the obstruction calculus develops sound, computationally interpretable certificates for nonviability --- sufficient conditions for nonviability, equivalently necessary conditions for viability.")
# hedging
sub(r"a problem that satisfies neither is the open middle ground, where a stronger observer or a finer observation structure is the natural remedy.",
    r"a problem that satisfies neither requires a stronger observer or a finer observation structure.")
sub(r"These results delimit the middle ground: under margins and convergence, output feedback \emph{can} work;",
    r"These results bound the sufficiency side: under margins and convergence, output feedback \emph{can} work;")
sub(r"They do not exhaust the complement of the epistemic kernel --- Section 6.5 states the open middle ground --- and the paper claims no complete characterization.",
    r"They do not exhaust the complement of the epistemic kernel (Section 6.5), and the paper claims no complete characterization.")
sub(r"we do not claim the underlying elementary facts (quantifier commutation; Dini comparison) as new.",
    r"the elementary facts on which they rest (quantifier commutation; Dini comparison) are classical.")
# "not itself an exhibit of failure"
sub(r"not itself an exhibit of failure.", "")
# housekeeping
sub(r"the control-space analogue of the material-substitution separation certificates in the companion assessment-separation analysis (Abaee, 2026).",
    r"the control-space analogue of the material-substitution separation certificates in the assessment-separation analysis of Abaee (2026).")
sub(r"Verification code for the worked examples is available from the author on request.",
    r"No code was used or produced; all constructions are symbolic.")
# tangency labels + kernel K->G in 2.2
sub(r"Two levels of the tangency condition are distinguished throughout. The \emph{local} reading applies the correspondence to the constraint set itself:",
    r"Two levels of the tangency condition are distinguished throughout. (i) \emph{Local reading.} The correspondence is applied to the constraint set itself:")
sub(r"When \(\mathcal{V}\) is not invariant, viability of a point \(x_0 \in \mathcal{V}\) requires instead a selection \(u(x) \in \mathcal{R}_K(x)\) along the trajectory, where \(K = \mathrm{RViab}(\mathcal{V})\) and \(\mathcal{R}_K\) is the same correspondence computed on the kernel:",
    r"(ii) \emph{Kernel reading.} When \(\mathcal{V}\) is not invariant, viability of a point \(x_0 \in \mathcal{V}\) requires instead a selection \(u(x) \in \mathcal{R}_G(x)\) along the trajectory, where \(G = \mathrm{RViab}(\mathcal{V})\) and \(\mathcal{R}_G\) is the same correspondence computed on the kernel:")
# Definition 1 parenthetical
sub(r"(This is the standard exists-strategy-for-all-realizations form; the quantifier order is essential, because the record is generated by the realization --- any qualifier conditioning the admissible realizations on the record would be circular.)",
    r"(This is the standard exists-strategy-for-all-realizations form. The quantifier order is essential: the record is generated by the realization, so conditioning the admissible realizations on the record would be circular.)")
# Definition 1 last sentence (EViab single definition)
sub(r"The existential --- non-robust --- counterpart \(\mathrm{EViab}_{\mathcal{I}}(\mathcal{V})\) is defined as a contrast class only, for the a-fortiori caveat below; no theorem uses its coupled-record semantics.",
    r"The existential (non-robust) counterpart \(\mathrm{EViab}_{\mathcal{I}}(\mathcal{V})\) is the contrast class defined below.")
# EViab mentions
sub(r"\(\mathrm{EViab}_{\mathcal{I}}(\mathcal{V})\) is defined as a contrast class only (see the a-fortiori caveat in Section 2.3); no theorem of this paper is stated for it.",
    r"\(\mathrm{EViab}_{\mathcal{I}}(\mathcal{V})\) is the non-robust contrast class (Section 2.3).")
sub(r"\(\mathrm{EViab}_{\mathcal{I}}(\mathcal{V})\) is defined as a contrast class only (Section 2.3's a-fortiori caveat; no theorem is stated for it).",
    r"\(\mathrm{EViab}_{\mathcal{I}}(\mathcal{V})\) is the non-robust contrast class (Section 2.3).")
# IRViab consolidation
sub(r"where \(\mathrm{IRViab}_{\mathcal{J}}(\mathcal{V})\) is the institutionally restricted counterpart (Section 6.4), defined as the viability kernel of the system whose command correspondence is restricted to the institutionally admissible set \(U_{\mathcal{J}}(x) \subseteq U(x)\). This is a definition, not a theorem: it fixes the symbol's meaning, and no theorem of this paper is stated for it.",
    r"where \(\mathrm{IRViab}_{\mathcal{J}}(\mathcal{V})\) is the institutionally restricted kernel of Section 6.4.")
sub(r"The institutionally restricted kernel is \(\mathrm{IRViab}_{\mathcal{J}}(\mathcal{V})\) (Section 6.4): a definition, not a theorem --- the viability kernel of the system whose command correspondence is restricted to the institutionally admissible set \(U_{\mathcal{J}}(x) \subseteq U(x)\).",
    r"The institutionally restricted kernel is \(\mathrm{IRViab}_{\mathcal{J}}(\mathcal{V})\) (Section 6.4).")
sub(r"The epistemic-institutional kernel \(\mathrm{IRViab}_{\mathcal{J}}(\mathcal{V})\) --- defined in Section 2.1 as the viability kernel of the system whose command correspondence is restricted to the institutionally admissible set \(U_{\mathcal{J}}(x) \subseteq U(x)\), a definition with no theorem claimed for it --- combines them:",
    r"The epistemic-institutional kernel \(\mathrm{IRViab}_{\mathcal{J}}(\mathcal{V})\) (Section 2.1) combines them:")
# "not re-derived here"
sub(r"the epistemic kernel is the greatest recursively viable collection of information states in the sense of the estimation-space reduction cited in Section 5, not re-derived here; common-action compatibility",
    r"the epistemic kernel is the greatest recursively viable collection of information states in the sense of the estimation-space reduction cited in Section 5; common-action compatibility")
# Sec 5 opening
sub(r"Their proofs repeat established literature and are cited, not reproduced.",
    r"The following results are standard; proofs appear in the cited sources.")
# Appendix A
sub(r"They are stated in full with their scope remarks; none of them is stated as a theorem of the main text.",
    r"They are stated in full with their scope remarks.")
# Theorem 1 Lipschitz caveat (statement)
sub(r"Let \(q : X \to \mathbb{R}\) be a constraint function of class \(C^1\) --- the class for which the proof below is carried out; the locally Lipschitz reading is an extension not proved here --- with",
    r"Let \(q : X \to \mathbb{R}\) be a constraint function of class \(C^1\) --- the class assumed throughout the exit theorems --- with")
# Theorem 1 Lipschitz caveat (proof)
sub(r"The statement and proof below are for \(q\) of class \(C^1\); the locally Lipschitz case is an extension not proved here: the Clarke derivative is only upper semicontinuous in \(x\), and the Dini comparison must be re-derived for almost-everywhere-differentiable arcs before the same conclusion may be asserted there.",
    r"The proof is carried out for \(q\) of class \(C^1\), as assumed; the locally Lipschitz case requires a separate comparison argument for almost-everywhere-differentiable arcs and is not treated.")
# ---- symbol renames: Appendix A ----
sub(r"\[\dot S_i = g_i(S_i) + d\,(S_j - S_i) - H_i, \qquad i, j \in \{1,2\},\ i \ne j,\]",
    r"\(\dot S_i = g_i(S_i) + \gamma\,(S_j - S_i) - h_i, \qquad i, j \in \{1,2\},\ i \ne j,\)")
sub(r"with \(g_i(s) = s(1-s)\), \(d = 0.2\), constraints \(S_i \in [0,1]\) and \(H_i \ge H_{\min,i}\) (harvest floors), and admissible controls the constant harvest vectors \(H = (H_1, H_2)\) with \(H_i \ge 0\).",
    r"with \(g_i(s) = s(1-s)\), \(\gamma = 0.2\), constraints \(S_i \in [0,1]\) and \(h_i \ge h_{\min,i}\) (harvest floors), and admissible controls the constant harvest vectors \(h = (h_1, h_2)\) with \(h_i \ge 0\).")
sub(r"Define harvest floors by the equilibrium equations: \(H_{\min,1} = g_1(0.5) + 0.2(0.8 - 0.5) = 0.31\); \(H_{\min,2} = g_2(0.8) + 0.2(0.5 - 0.8) = 0.10\).",
    r"Define harvest floors by the equilibrium equations: \(h_{\min,1} = g_1(0.5) + 0.2(0.8 - 0.5) = 0.31\); \(h_{\min,2} = g_2(0.8) + 0.2(0.5 - 0.8) = 0.10\).")
sub(r"\(\max_s g_1(s) = 0.25 < H_{\min,1} = 0.31\)",
    r"\(\max_s g_1(s) = 0.25 < h_{\min,1} = 0.31\)")
sub(r"with \(H = (0.31, 0.10)\) admissible",
    r"with \(h = (0.31, 0.10)\) admissible")
sub(r"Take \(d > 0\), \(C_1 \ne C_2\), \(H_{\min,i} = r_i C_i / 4\) (MSY level), in the same coupled system with \(\phi_i(S_i) := g_i(S_i) - H_{\min,i}\)",
    r"Take \(\gamma > 0\), \(C_1 \ne C_2\), \(h_{\min,i} = r_i C_i / 4\) (MSY level), in the same coupled system with \(\phi_i(S_i) := g_i(S_i) - h_{\min,i}\)")
sub(r"the constraint set is the box \([C_1/2, K_{\max,1}] \times [C_2/2, K_{\max,2}]\)",
    r"the constraint set is the box \([C_1/2, \bar S_1] \times [C_2/2, \bar S_2]\)")
sub(r"Each isolated system has kernel \([C_i/2, K_{\max,i}]\)",
    r"Each isolated system has kernel \([C_i/2, \bar S_i]\)")
sub(r"\[\big(\dot S_1, \dot S_2\big)\big|_{p^*} = \left(\tfrac{d}{2}(C_2 - C_1), \tfrac{d}{2}(C_1 - C_2)\right) \ne 0.\]",
    r"\(\big(\dot S_1, \dot S_2\big)\big|_{p^*} = \left(\tfrac{\gamma}{2}(C_2 - C_1), \tfrac{\gamma}{2}(C_1 - C_2)\right) \ne 0.\)")
# ---- symbol renames: Sec 5(c) ----
sub(r"the observer satisfies \(\|\hat x(t) - x(t)\| \le M e^{-\lambda t}\|\hat x(0) - x(0)\|\)",
    r"the observer satisfies \(\|\hat x(t) - x(t)\| \le M e^{-\alpha t}\|\hat x(0) - x(0)\|\)")
sub(r"if \(K_\varepsilon\) is a compact controlled-invariant subset of the interior of the kernel",
    r"if \(K_\delta\) is a compact controlled-invariant subset of the interior of the kernel")
sub(r"then \(K_\varepsilon\) is viable under output feedback",
    r"then \(K_\delta\) is viable under output feedback")
sub(r"and estimation and implementation errors are bounded by \(\varepsilon\)",
    r"and estimation and implementation errors are bounded by \(\eta\)")
sub(r"then an eroded set \(K^{-c\varepsilon}\) is invariant",
    r"then an eroded set \(K^{-c\eta}\) is invariant")

# ---------------- G. cross-reference renumbering ----------------
# multi-token first
sub(r"Theorems 1 and 4", r"Theorem~\ref{thm:exit} and Theorem~\ref{thm:delayed}", expect=2)
sub(r"Theorems 2 and 3", r"Proposition~\ref{prop:emptiness} and Theorem~\ref{thm:common-action}", expect=1)
sub(r"Theorems 3 and 5", r"Theorem~\ref{thm:common-action} and Proposition~\ref{prop:fibre}", expect=1)
sub(r"Theorems 1--4", r"Theorem~\ref{thm:exit}--\ref{thm:delayed} and Proposition~\ref{prop:emptiness}", expect=1)
sub(r"Theorems 2--5", r"Proposition~\ref{prop:emptiness}, Theorem~\ref{thm:common-action}, Theorem~\ref{thm:delayed}, and Proposition~\ref{prop:fibre}", expect=1)
sub(r"Theorems 3--5", r"Theorem~\ref{thm:common-action}, Theorem~\ref{thm:delayed}, and Proposition~\ref{prop:fibre}", expect=1)
# singles
for old, new in [
    (r"Theorem 1", r"Theorem~\ref{thm:exit}"),
    (r"Theorem 2", r"Proposition~\ref{prop:emptiness}"),
    (r"Theorem 3", r"Theorem~\ref{thm:common-action}"),
    (r"Theorem 4", r"Theorem~\ref{thm:delayed}"),
    (r"Theorem 5", r"Proposition~\ref{prop:fibre}"),
    (r"Corollary 6", r"Corollary~\ref{cor:certainly-safe}"),
    (r"Example 1", r"Example~\ref{ex:hidden-mode}"),
    (r"Remark 1", r"Remark~\ref{rem:ce-trap}"),
    (r"Definition 1", r"Definition~\ref{def:kernel}"),
    (r"Definition 2", r"Definition~\ref{def:certifier}"),
]:
    sub_any(old, new)

open("arena agent 1/paper rewrites/latex/paper2_obstruction_calculus_v16.tex", "w", encoding="utf-8").write(src)

# ---------------- verification ----------------
residual = re.findall(r"(?<![\w])(Theorem|Theorems|Corollary|Remark|Example|Definition)\s+[0-9]", src)
print("residual hardcoded numbered refs:", residual if residual else "NONE")

for bad in ["no theorem", "definition, not a theorem", "not re-derived here",
            "cited, not reproduced", "not itself an exhibit", "not proved here",
            "contrast class only", "(Cited)", "companion", "site-local"]:
    n = src.count(bad)
    print(f"  '{bad}': {n}")

m = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", src, re.S)
t = m.group(1)
t2 = re.sub(r"\\(?:emph|textbf|mathrm|mathcal|mathbf|ensuremath)\{[^}]*\}", " ", t)
t2 = re.sub(r"\\[a-zA-Z]+", " ", t2)
t2 = re.sub(r"[^A-Za-z0-9\-]+", " ", t2)
print("abstract words:", len([x for x in t2.split() if x]), "(limit 265)")
print("file bytes:", len(src))

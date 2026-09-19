#!/usr/bin/env python3
"""v34: the composition kernel.  The two objects the audits flagged as undefined --- the calculus in
which certificates are composed (deployment-plan row 17, which had been deferred to a companion
paper) and the identifiability sets for aggregate-determined event times (row 11) --- are defined
here, in the article, with proofs and machine-checked instances
(`kernel_exhibits.py`: closure LPs, the interface price, L_max, and the fibre scan).  Applied to
both members of the v33 pair, so the LaTeX and the markdown stay identical in content.

Run from the workspace root:  python3 revision/v7/revisions_v34_kernel.py
"""
import hashlib
import json
import os
import re

WS = os.environ.get("WS", "/home/user")
FILES = {
    "md": (os.path.join(WS, "revision/v6/paper3_material_ledgers_v33.md"),
           os.path.join(WS, "revision/v7/paper3_material_ledgers_v34.md")),
    "tex": (os.path.join(WS, "revision/v7/paper3_material_ledgers_v33.tex"),
            os.path.join(WS, "revision/v7/paper3_material_ledgers_v34.tex")),
}

KERNEL_MD = r"""### 3.7 Composition of ledgers and the calculus of certificates

Everything above is stated for one ledger. Applications assemble ledgers --- a resource module, a
process module, a territory --- and an assembled object inherits its obligations only if the
assembly is itself an object of the theory. This section supplies that missing definition, and with it
the two results the rest of the article needs: closure is not compositional, and the margin an
interface costs is computable.

**Definition 34 (Composition of typed ledgers).** Let $L_1 = (x^1, v^1, S_1, B_1, C_1)$ and
$L_2 = (x^2, v^2, S_2, B_2, C_2)$ be ledgers over disjoint compartment sets, and let an *interface*
$\Theta = (J, \Phi, \bar v)$ consist of a finite set $J$ of declared identifications pairing a
compartment of $L_1$ with a compartment of $L_2$, a finite set $\Phi$ of declared exchange fluxes
with boxes $0 \le f_\varphi \le \bar v_\varphi$, and, for each $\varphi$, the two endpoints it drains
and fills. The composition $L_1 \oplus_\Theta L_2$ is the ledger on the quotient compartment set
(disjoint union modulo $J$) whose incidence is the block-diagonal $\mathrm{diag}(S_1, S_2)$ extended
by the identification rows and by the endpoint columns of $\Phi$, with readouts carried over unchanged
on each side. The composition is *admissible* when three conditions hold on the declared data:

1. like with like: every identification pairs compartments of the same material type and the same
   unit, and the *interface defect*
   $d_\Theta = \sum_{(a,b) \in J} \bigl[\,\mathbf 1\{\mathrm{type}(a) \ne \mathrm{type}(b)\} +
   \mathbf 1\{\mathrm{unit}(a) \ne \mathrm{unit}(b)\}\bigr]$ vanishes;
2. joint boxes declared: no capacity constrains fluxes of both ledgers unless that sharing is one of
   the declared objects, in which case the shared box is a constraint of the composition and not of
   either part;
3. antisymmetry: each exchange enters one ledger as an outflow and the other as an inflow of the same
   magnitude, $\textstyle\sum_{i} B_i\, e_\varphi = 0$ on the identified compartments.

The admissible compositions are exactly those for which the flux polytope of the whole is the fibre
product of the parts' polytopes over the interface coordinates. The defect and the antisymmetry
residual are computed from the declaration, not assumed away; a composition with $d_\Theta > 0$ is not
a ledger, and no statement below applies to it.

**Definition 35 (Interface price).** Suppose each part is certified as in Theorem 24, with multiplier
$\lambda_i \ge 0$, margins $m_i(x^i) = G_i x^i + a_i$, and readout $y_i = c_i^{\top} v^i$. For a
declared exchange $\varphi$ draining compartment $c$ on the paying side, its *price* is
\[
\pi_\varphi = \bigl(\lambda_1^{\top} G_1\bigr)_c - \bigl(\lambda_2^{\top} G_2\bigr)_c ,
\]
evaluated at the identified compartments. A non-positive price means the exchange enters the combined
budget of the composition with the wrong sign to cost anything; a positive price is margin consumed per
unit of flux per unit of time.

**Proposition 36 (Conservation composes; closure does not).** Let $\Theta$ be admissible. Every
left-null vector of $S_1$ and of $S_2$ lifts to a left-null vector of the composition, constant along
identified compartments, so the conserved totals of the parts are conserved in the whole. Closure of
the cycle at a demanded rate does not compose: the closure capacity of the composition can be strictly
below the minimum of the parts' closure capacities. Instance: two cycles, each with demand $1$ unit
per year and return capacity exactly $1$ unit per year, each therefore closing tightly at
$\lambda^{*} = 1$; when the two return fluxes draw on a single declared capacity of $1.5$ units per
year, the composition has $\lambda^{*} = 0.75$ and closure deficit $0.25$. Every trajectory of the
composition meeting the demanded rate then has non-stationary stock, so by Definition 22 the shortfall
appears as support drawdown together with sink accumulation, at a rate the linear programme fixes.

*Proof.* For the lift, $\ell^{\top} \mathrm{diag}(S_1, S_2) = 0$ with equal entries on identified
compartments gives $\ell^{\top} S = 0$ on the quotient, since the identification rows are the only
further constraints and they are annihilated by equality of the paired entries. For the instance, the
composition's programme is $\max \lambda$ subject to $q = \lambda$, $s = \lambda$, $q + s \le 1.5$
with $q, s \ge 0$, whose optimum is $\lambda = 0.75$; the parts' programmes are $q \le 1$ and $s \le
1$, both with optimum $1$. □

**Proposition 37 (Margin needed, and the admissible exchange rate).** Let $\Theta$ be admissible and
let each part satisfy Theorem 24 with budget $B_i = V_i(x^i(0)) + \int_0^T \lambda_i^{\top} G_i
b_i\,dt$. Then the composition satisfies the same bound for the summed service $y_1 + y_2$ with budget
\[
B_1 + B_2 + \sum_{\varphi \in \Phi} \pi_\varphi^{+}\, \bar v_\varphi\, T,
\qquad \pi^{+} = \max\{\pi, 0\}.
\]
The sum is the *margin needed* to absorb the interface; the interface is free, in the sense that the
parts' budgets add without remainder, exactly when $\pi_\varphi \le 0$ for every declared exchange.
With a single exchange of box $[0, L]$, price $\pi > 0$ and horizon $T$, the composition is certified
if and only if
\[
L \;\le\; L_{\max} := \frac{B_1 + B_2}{\pi\, T}.
\]
Instance: $G_1 = G_2 = 1$, $\lambda_1 = 2$, $\lambda_2 = 1$, so $\pi = 1$; with $B_1 + B_2 = 9$ units
of margin and $T = 30$ yr, $L_{\max} = 0.30$ unit per year --- an exchange at $0.2$ stays inside the
combined budget ($6 \le 9$) and one at $0.5$ does not ($15 > 9$).

*Proof.* Take $V = V_1 + V_2$. Along the composition, $\dot V \le -(y_1 + y_2) + \lambda_1^{\top}
G_1 b_1 + \lambda_2^{\top} G_2 b_2 + \sum_\varphi \pi_\varphi f_\varphi$: the exchange terms are the
only ones that do not decouple, because a flux that leaves margin in one part enters it in the other at
the partner's multiplier. Bounding $f_\varphi$ by $\bar v_\varphi$ on $\pi_\varphi > 0$ and by $0$
otherwise, and integrating with $V(T) \ge 0$, gives the stated budget. The one-dimensional case is the
equality $L \pi T = B_1 + B_2$ solved for $L$. □

These three statements are the calculus the article's own citations had deferred to a companion: an
object of composition, the predicate that survives it, and the number that prices what does not. No
further deferral is made here, and nothing in Sections 4 to 10 depends on a claim about composition
that is not proved above.

"""

IDENT_MD = r"""### 6.6 What an aggregate record fixes

**Definition 38 (Identifiability set of an event time).** Fix the readout, the declared boxes and
bounds, and an observed aggregate record $z$. The *fibre* $\mathcal F(z)$ is the set of admissible
component initial states whose induced aggregate trajectory equals $z$. The *identifiability set* of
the first component exit time is
\[
\mathrm T(z) \;=\; \bigl\{\tau(x_0) : x_0 \in \mathcal F(z)\bigr\},
\]
and the event time is identifiable from the aggregate record if and only if $\mathrm T(z)$ is a
singleton.

**Proposition 39 (The set is a polytope image, and it is usually an interval).** On the decay pair of
Proposition 31, with $\dot x_i = -x_i$, $Z(t) = 100 e^{-t}$ and barrier $x_i \ge 1$, the fibre is
$\{x_1 + x_2 = 100,\ 1 \le x_1, x_2 \le 99\}$ and
\[
\mathrm T(z) \;=\; \bigl[\,0,\ \log 50\,\bigr] \;=\; [\,0,\ 3.9120\,] \ \text{yr},
\]
its supremum attained at the balanced start $(50, 50)$ and its infimum approached as either component
nears its barrier. Both recorded instances lie in the set, $0.6931$ yr from $(2, 98)$ and $3.9120$ yr
from $(50, 50)$, and the aggregate record is silent on everything between them. More generally, where
the declared constraints are linear and the event time is monotone in the initial state along the fibre,
$\mathrm T(z)$ is the image of a polytope, so its endpoints are the values of two linear programmes
over that polytope, and identifiability from an aggregate record holds exactly when the declared
component data reduce the fibre to a point --- which is a statement about the input, never about the
aggregate.

*Proof.* $\tau(x_0) = \min\{\log x_1(0), \log x_2(0)\}$ with $x_2(0) = 100 - x_1(0)$: the function is
increasing then decreasing in $x_1$ on $[1, 99]$, symmetric about $50$, with maximum $\log 50$ and
limit $0$ at the ends, so its image is $[0, \log 50]$. The fibre is an intersection of the declared
boxes with the invariant hyperplane, hence a polytope, and monotonicity supplies the two extremal
programmes. □

"""

NOTE_UPDATES = [
    ("runs on the single 1\u201333 sequence counter", "runs on the single 1\u201339 sequence counter",
     "1--33 sequence counter", "1--39 sequence counter"),
    ("the statements added at this revision carry the consecutive labels Definitions 21\u201323, Theorem 24, Propositions 25\u201332 and Remark 33, so no label is repeated",
     "the statements added at this revision carry the consecutive labels Definitions 21\u201323 and 34\u201335 and 38, Theorem 24, and Propositions 25\u201332 and 36\u201337 and 39, with Remark 33, so no label is repeated",
     "the statements added at this revision carry the consecutive labels Definitions 21--23, Theorem 24, Propositions 25--32 and Remark 33, so no label is repeated",
     "the statements added at this revision carry the consecutive labels Definitions 21--23 and 34--35 and 38, Theorem 24, and Propositions 25--32 and 36--37 and 39, with Remark 33, so no label is repeated"),
]


def to_tex(s):
    ESC = {"%": r"\%", "&": r"\&", "#": r"\#", "_": r"\_", "$": None}
    out, i = [], 0
    for m in re.finditer(r"\$\$(.+?)\$\$|\$(.+?)\$", s, flags=re.S):
        out.append(prose(s[i:m.start()]))
        if m.group(1):
            out.append("\\[ %s \\]" % " ".join(m.group(1).split()))
        else:
            out.append("\\(%s\\)" % " ".join(m.group(2).split()))
        i = m.end()
    out.append(prose(s[i:]))
    return "".join(out)


def prose(p):
    p = re.sub(r"^(#{2,4})\s+(.*)$", lambda m: "\\subsubsection{%s}" % m.group(2).strip(), p, flags=re.M)
    p = re.sub(r"\*\*(.+?)\.\*\*", lambda m: r"\textbf{%s.}" % m.group(1), p, flags=re.S)
    p = re.sub(r"\*([^*\n]+)\*", lambda m: r"\emph{%s}" % m.group(1), p)
    for k, v in [("%", r"\%"), ("&", r"\&"), ("#", r"\#"), ("_", r"\_")]:
        p = p.replace(k, v)
    p = p.replace("\u25a1", r"\ensuremath{\square}").replace("\u2265", r"\ge").replace("\u2264", r"\le")
    p = p.replace("\u2014", "---").replace("\u2013", "--").replace("\u2019", "'")
    p = p.replace("\u201c", "``").replace("\u201d", "''")
    p = re.sub(r"\\\[ \\\]", "", p)
    return p


results = {}
for kind, (src, dst) in FILES.items():
    t = open(src, encoding="utf-8").read()
    log = []
    if kind == "md":
        ker, ident = KERNEL_MD, IDENT_MD
        ker_at = t.index("\n## 4. Conservation")
        t = t[:ker_at] + "\n" + ker.rstrip("\n") + t[ker_at:]
        log.append({"tag": "3.7 kernel section", "old": "", "text": "\n" + ker.rstrip("\n")})
        ident_at = t.index("\n## 7. First-Passage")
        t = t[:ident_at] + "\n" + ident.rstrip("\n") + t[ident_at:]
        log.append({"tag": "6.6 identifiability section", "old": "", "text": "\n" + ident.rstrip("\n")})
    else:
        body = to_tex(KERNEL_MD.replace("\n\n", "\n\n")).replace("\\subsubsection{3.7 Composition of ledgers and the calculus of certificates}",
                  "\\subsubsection{3.7 Composition of ledgers and the calculus of "
                  "certificates}\\label{composition-of-ledgers-and-the-calculus-of-certificates}")
        m = re.search(r"(?m)^\subsection\{4\. Conservation", t)
        pos = m.start()
        blk = "\n" + body.strip("\n") + "\n"
        t = t[:pos] + blk + t[pos:]
        log.append({"tag": "3.7 kernel section", "old": "", "text": blk})
        body2 = to_tex(IDENT_MD).replace("\\subsubsection{6.6 What an aggregate record fixes}",
                  "\\subsubsection{6.6 What an aggregate record fixes}"
                  "\\label{what-an-aggregate-record-fixes}")
        m = re.search(r"(?m)^\subsection\{7\. First-Passage", t)
        pos = m.start()
        blk2 = "\n" + body2.strip("\n") + "\n"
        t = t[:pos] + blk2 + t[pos:]
        log.append({"tag": "6.6 identifiability section", "old": "", "text": blk2})
    for old_md, new_md, old_tex, new_tex in NOTE_UPDATES:
        old, new = (old_md, new_md) if kind == "md" else (old_tex, new_tex)
        assert t.count(old) == 1, (kind, "note target", old[:40], t.count(old))
        t = t.replace(old, new, 1)
        log.append({"tag": "numbering note (%s)" % kind, "old": old, "text": new})
    non = {c for c in t if ord(c) > 127}
    base = {c for c in open(src, encoding="utf-8").read() if ord(c) > 127}
    print("%s: non-ASCII introduced: %s" % (kind, sorted(non - base) or "none"))
    open(dst, "w", encoding="utf-8").write(t)
    json.dump(log, open(dst.replace(".md", "_log.json").replace(".tex", "_log.json"), "w"), ensure_ascii=False)
    # reverse check now, at build time
    r = open(src, encoding="utf-8").read()
    cur = t
    for op in reversed(log):
        assert cur.count(op["text"]) == 1, ("reconstruction", kind, op["tag"])
        cur = cur.replace(op["text"], op["old"], 1)
    results[kind] = dict(chars=len(t), grew=len(t) - len(open(src, encoding='utf-8').read()),
                         reconstructs=(hashlib.sha256(cur.encode()).hexdigest()
                                       == hashlib.sha256(r.encode()).hexdigest()))
for k, v in results.items():
    print("%-4s %8d chars (+%5d)  insert-only reconstruction: %s" % (k, v["chars"], v["grew"], v["reconstructs"]))

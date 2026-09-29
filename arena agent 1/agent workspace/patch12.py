src = 'paper2_probabilistic_sufficiency_v11.tex'
t = open(src).read()


def rep(old, new, n=1):
    global t
    if t.count(old) < 1:
        print("MISSING:", old[:70])
        raise SystemExit(1)
    t = t.replace(old, new, n)
    print("patched:", old[:48].replace("\n", " "))


rep("""viable-set recursion \\(\\mathcal{W}_{k}\\), and outside it the deficit""",
    """viable-set recursion \\(\\mathcal{W}^{\\mathrm{fb}}_{k}\\), and outside it
the deficit""")

rep("""\\(\\mathcal{W}_{k}\\) the calculus's viable-set recursion (a family of
state sets), and \\(\\mathcal{W}^{\\mathrm{bel}}_{k}\\) its belief-space
analogue (a family of beliefs); unsuperscripted values do not appear.""",
    """\\(\\mathcal{W}^{\\mathrm{fb}}_{k}\\) the calculus's feedback viable-set
recursion (a family of state sets), \\(\\mathcal{W}_{k}\\) the blind
recursion (the same, but with one action for the whole set, chosen
before the observation arrives), and
\\(\\mathcal{W}^{\\mathrm{bel}}_{k}\\) the belief-space analogue of
\\(\\mathcal{W}_{k}\\) (a family of beliefs); unsuperscripted values do
not appear.""")

rep("""\\(\\mathcal{W}_{k}\\) denote the calculus's viable-set recursion:
\\(\\mathcal{W}_{0} = \\{B \\subseteq \\mathcal{V}\\}\\) and
\\(\\mathcal{W}_{k} = \\{B : \\text{some admissible } a \\text{ maps every }
x \\in B \\text{ into } \\mathcal{W}_{k-1}\\text{-supported posteriors}\\}\\).""",
    """\\(\\mathcal{W}^{\\mathrm{fb}}_{k}\\) denote the calculus's feedback
viable-set recursion:
\\(\\mathcal{W}^{\\mathrm{fb}}_{0} = \\{B \\subseteq \\mathcal{V}\\}\\), and
\\(B \\in \\mathcal{W}^{\\mathrm{fb}}_{k}\\) if some admissible \\(a\\)
admits, for every observation \\(y\\) that \\((B,a)\\) can produce, a
\\(\\mathcal{W}^{\\mathrm{fb}}_{k-1}\\)-continuation of
\\(\\mathrm{Post}(B,a,y)\\). The blind recursion \\(\\mathcal{W}_{k}\\) is
the special case in which the continuation may not depend on \\(y\\):
\\(\\mathcal{W}_{0} = \\{B \\subseteq \\mathcal{V}\\}\\) and
\\(\\mathcal{W}_{k} = \\{B : \\text{some admissible } a \\text{ maps every }
x \\in B \\text{ into } \\mathcal{W}_{k-1}\\text{-supported posteriors}\\}\\).
Thus \\(\\mathcal{W}_{k} \\subseteq \\mathcal{W}^{\\mathrm{fb}}_{k}\\),
strictly in general (Remark~\\ref{rem:feedback-strict}).""")

rep("""\\(\\mathrm{supp}(b) \\in \\mathcal{W}_{k}\\), while if
\\(\\mathrm{supp}(b) \\notin \\mathcal{W}_{k}\\) then every policy loses a""",
    """\\(\\mathrm{supp}(b) \\in \\mathcal{W}^{\\mathrm{fb}}_{k}\\), while if
\\(\\mathrm{supp}(b) \\notin \\mathcal{W}^{\\mathrm{fb}}_{k}\\) then every policy
loses a""")

rep("""viable sets at every stage, so every branch survives and
\\(V_{k}(b) = 1\\). For the converse, with deterministic observations the
realized observation path is fixed by the declared sequence, so
\\(V_{k}(b) = \\max_{\\text{seq}} \\sum_{x \\text{ surviving}} b(x)\\); if
\\(\\mathrm{supp}(b) \\notin \\mathcal{W}_{k}\\) no declared sequence keeps
every compatible branch, so each sequence loses at least one branch of
mass \\(b(x) \\ge \\min_{x'} b(x')\\), giving
\\(1 - V_{k}(b) \\ge \\min_{x \\in \\mathrm{supp}(b)} b(x)\\). Monotonicity:""",
    """viable sets at every stage, so every branch survives and
\\(V_{k}(b) = 1\\). For the converse, induct on \\(k\\); for \\(k = 0\\)
there is nothing to prove. Let
\\(\\mathrm{supp}(b) \\notin \\mathcal{W}^{\\mathrm{fb}}_{k}\\) and let
\\(\\pi\\) be any policy, with first action \\(a\\). For each observation
\\(y\\) that \\(a\\) produces with positive probability from \\(b\\), the
posterior \\(b^{+}(\\cdot \\mid a, y)\\) has support
\\(\\mathrm{Post}(\\mathrm{supp}(b), a, y)\\) by the support identity; if
that support lay in \\(\\mathcal{W}^{\\mathrm{fb}}_{k-1}\\) for every such
\\(y\\), then \\(\\mathrm{supp}(b)\\) would lie in
\\(\\mathcal{W}^{\\mathrm{fb}}_{k}\\) by the recursion's definition.
Hence for some \\(y\\) the posterior support lies outside
\\(\\mathcal{W}^{\\mathrm{fb}}_{k-1}\\), and by the induction hypothesis
the continuation of \\(\\pi\\) after \\((a,y)\\) loses a branch of that
posterior of positive mass. Composing, \\(\\pi\\) loses a branch of
\\(b\\) of positive mass; every lost branch carries mass at least
\\(\\min_{x \\in \\mathrm{supp}(b)} b(x)\\), and there are finitely many
branches, giving
\\(1 - V_{k}(b) \\ge \\min_{x \\in \\mathrm{supp}(b)} b(x)\\). Monotonicity:""")

rep("""absorption at \\(\\bot\\) is permanent, so a policy safe for \\(k+1\\)
stages is safe for \\(k\\) (equivalently, the survivable families are
prefix-nested).
\\end{proof}
""",
    """absorption at \\(\\bot\\) is permanent, so a policy safe for \\(k+1\\)
stages is safe for \\(k\\) (equivalently, the survivable families are
prefix-nested).
\\end{proof}

\\begin{remark}[observation-dependent continuation is strictly
stronger]\\label{rem:feedback-strict}
Both recursions are downward closed and
\\(\\mathcal{W}_{k} \\subseteq \\mathcal{W}^{\\mathrm{fb}}_{k}\\); the
inclusion can be strict, even under the hypotheses of
Theorem~\\ref{thm:support}. Let \\(p \\neq q\\) be safe states and
\\(a_{0}\\) the only admissible action that keeps both alive, sending
them to distinct successors \\(p^{+} \\neq q^{+}\\) that the observation
map distinguishes; let the unique safe continuation at \\(p^{+}\\) be
\\(b\\) and the unique safe continuation at \\(q^{+}\\) be
\\(c \\neq b\\). Then
\\(\\{p,q\\} \\in \\mathcal{W}^{\\mathrm{fb}}_{2}\\) --- play \\(a_{0}\\),
read the observation, continue with \\(b\\) or \\(c\\) accordingly ---
while \\(\\{p,q\\} \\notin \\mathcal{W}_{2}\\): the first action must be
\\(a_{0}\\), and no single second action is safe at both \\(p^{+}\\) and
\\(q^{+}\\).
For a belief with support \\(\\{p,q\\}\\) it follows that
\\(V^{\\Pi_{\\mathrm{seq}}}_{2}(b) = 1\\) while
\\(V^{\\Pi_{B}}_{2}(b) < 1\\): the value of observation is strict here in
the strongest form available, all or nothing. The two recursions agree
when no information arrives --- on a blind window,
\\(\\mathcal{W}^{\\mathrm{fb}}_{k} = \\mathcal{W}_{k}\\), the set-level
content of Theorem~\\ref{thm:lattice}'s
\\(V^{\\mathrm{ol}} = V^{\\mathrm{seq,blind}}\\). Theorems~\\ref{thm:support}
and~\\ref{prop:degen} therefore differ in their class, not only in their
normalization: the first is a feedback theorem, the second a blind one,
and Proposition~\\ref{cor:closed} is accordingly not a corollary of
Theorem~\\ref{thm:support}.
\\end{remark}
""")

open('paper2_probabilistic_sufficiency_v12.tex', 'w').write(t)
print("wrote", len(t), "bytes")

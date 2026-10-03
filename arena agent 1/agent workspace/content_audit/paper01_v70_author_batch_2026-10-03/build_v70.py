#!/usr/bin/env python3
"""Hash-pinned v69 -> new v70 article/supplement author draft.

Only approved B editorial/layout/reproducibility repairs and A4's demotion.
A1--A3 and A5 are NOT changed; C is preserved separately verbatim.
Every anchor must match exactly once. Never rewrites v69 or earlier.
"""
from pathlib import Path
from hashlib import sha256
R=Path(__file__).resolve().parents[2]
D=R/'paper 2 family/01_obstruction'
ARTICLE_OLD=D/'paper01_obstruction_calculus_v69.tex'
SUPP_OLD=D/'paper01_obstruction_calculus_v69_supplementary.tex'
ARTICLE_NEW=D/'paper01_obstruction_calculus_v70.tex'
SUPP_NEW=D/'paper01_obstruction_calculus_v70_supplementary.tex'
assert sha256(ARTICLE_OLD.read_bytes()).hexdigest()=='ce30c72500f6793b5faa6445540a839e1724e05e06ce5e1654bcb7dfb1b67763'
assert sha256(SUPP_OLD.read_bytes()).hexdigest()=='24e138d143e8716d642e094e22ebafcf89aeca4320a230703b5fe49bb95a2d23'
a=ARTICLE_OLD.read_text();s=SUPP_OLD.read_text();changes=[]
def rep(text,old,new,label):
    assert text.count(old)==1,(label,text.count(old))
    changes.append(label)
    return text.replace(old,new,1)
def span(text,start,end,new,label):
    assert text.count(start)==1,(label,'start',text.count(start))
    i=text.index(start);j=text.find(end,i+len(start));assert j>i,(label,'end')
    changes.append(label)
    return text[:i]+new+text[j:]

# --- A4: demote, rather than fabricate a uniform quantitative theorem. ---
a=span(a,r'\begin{proposition}[uniform margin gives a tube obstruction at every review length]',r'\begin{proposition}[obstruction ladder]',r'''\paragraph{Immediate consequence of the held-action adverse-path premise.}
For a declared held-action review class, suppose every candidate common command
\(a\in U^B(B)\) has a compatible admissible original-system path from some
\(x_a\in B\) whose active constraint becomes strictly negative at every
sufficiently small positive time, as in the exiting-path premise (H2.3).
Then \(\mathcal A_{\mathrm{tube}}(B,\Delta)=\varnothing\) for each
\(\Delta>0\), and there is no viable policy \emph{required to hold}
its first command for that review. Indeed, each candidate has an unsafe
point before that review ends. No action-uniform negative margin or
uniform exit interval is used or inferred; this is a consequence of the
assumed original-system paths, not a separate uniform-margin theorem.

''','A4 article proposition demoted')
s=span(s,r'\begin{proposition}[uniform margin gives a tube obstruction at every review length]',r'\begin{proposition}[obstruction ladder]',r'''\noindent\textbf{Immediate held-action consequence (main article, Section 3.2).}
For each \(a\in U^B(B)\), suppose a compatible admissible
original-system path exits through an active constraint at every
sufficiently small positive time as in (H2.3). For any \(\Delta>0\),
that path contains an unsafe point before the review ends, so
\(a\notin\mathcal A_{\mathrm{tube}}(B,\Delta)\). This exhausts the
common held commands and proves tube emptiness only for the declared
hold class. The interval can depend on \(a\); no uniform \(\eta\)
or uniform exit time is supplied. This is not a numbered proposition
or a claim against unrestricted within-review switching.

''','A4 supplement proposition demoted')
a=rep(a,'a uniform-margin\ncondition connects the instantaneous and tube obstructions\n(Proposition~\\ref{calc-prop:uniform-margin});',
      'the original-system held-action path premise gives an immediate tube consequence (Section 3.2);','intro A4 dependency')
a=rep(a,r'Propositions~\ref{calc-prop:uniform-margin}--\ref{calc-prop:emptiness}',
      r'Propositions~\ref{calc-prop:ladder}--\ref{calc-prop:emptiness} and the unnumbered held-action consequence','organization A4 range')
a=rep(a,r'common action and tube (Theorem~\ref{calc-thm:common-action}, Proposition~\ref{calc-prop:uniform-margin})',
      r'common action and tube (Theorem~\ref{calc-thm:common-action}; held-action consequence, Section 3.2)','table A4')
s=rep(s,'the gap that Proposition~\\ref{prop:uniform-margin}\ncloses under a uniform margin.',
      'the gap addressed by the separately assumed original-system exiting paths of (H2.3).','supp ladder A4')
s=rep(s,'article Propositions 2/3 correspond to supplementary Propositions 1/2; article Proposition 6 has its recourse proof in S1; article Proposition 9 has its two-phase argument in S2.',
      'the unnumbered article held-action consequence is detailed in S1; article Proposition 2 (ladder) corresponds to supplementary Proposition 1; article Proposition 5 (recourse) has its extended proof in S1; article Proposition 8 (two-phase decomposition) has its argument in S2.','supp crosswalk after A4')

# --- B: line-breaking, without changing mathematical conditions. ---
a=rep(a,r'\[\mathcal A_{\mathrm{tube}}(B,\Delta)=\{a\in U^B(B):\ \text{every compatible original-system held trajectory exists, remains action-admissible and stays in }\mathcal V\text{ on }[0,\Delta]\}.\]',
      r'''\[\mathcal A_{\mathrm{tube}}(B,\Delta)
=\{a\in U^B(B):\operatorname{Safe}_{\rm hold}(B,a,\Delta)\}.\]
Here \(\operatorname{Safe}_{\rm hold}(B,a,\Delta)\) means that every compatible original-system trajectory under the held command exists, remains action-admissible and stays in \(\mathcal V\) throughout \([0,\Delta]\).''','tube overfull fixed by defined predicate')
a=rep(a,r'\[\sum_{t=0}^{k-1}F_r A_j^{k-1-t}B_j u_t\le g_r-F_r A_j^k x_{j,0}-\sum_{t=0}^{k-1}h_{W_j}\!\left(E_j^{\top}(A_j^{k-1-t})^{\top}F_r^{\top}\right).\]',
      r'''Set \(\zeta_{j,r,k,t}=E_j^{\top}(A_j^{k-1-t})^{\top}F_r^{\top}\). Then the robust row is
\[\begin{aligned}
\sum_{t=0}^{k-1}F_r A_j^{k-1-t}B_j u_t
&\le g_r-F_r A_j^k x_{j,0}\\
&\quad-\sum_{t=0}^{k-1}h_{W_j}(\zeta_{j,r,k,t}).
\end{aligned}\]''','LP overfull aligned with support direction')
a=rep(a,r'\[\Gamma_N^{\mathrm{fin}}(B)=\{a\in U^B(B):\mathrm{Post}(B,a,y)\in\mathcal W_{N-1}\ \text{for every possible }y\}.\]',
      r'''\[\begin{aligned}
\Gamma_N^{\mathrm{fin}}(B)=\{a\in U^B(B):\ &\mathrm{Post}(B,a,y)\in\mathcal W_{N-1}\\
&\text{for every possible }y\}.
\end{aligned}\]''','finite selector overfull aligned')

# --- B: eliminate clear local contradictions. ---
a=rep(a,'Five consequences follow directly from the certificates. Each translates\na formal impossibility into a concrete design specification for\nmonitoring systems under partial ecological information.',
      'Five design consequences are discussed below: timing, coarseness, aggregation, bias and institutions. The intervening sensor-regularity paragraph is a model-specific caveat, not a sixth consequence proved by the certificates. These consequences are class-relative where the underlying certificate is.','five design items plus sensor caveat')
a=rep(a,'and the kernel empties although the information was sufficient.',
      'and the safety set of that one uncorrected law empties although a corrected output-feedback policy remains viable.','bias not general kernel')
a=rep(a,'(iv) \\emph{Bias:} the trap of Remark~\\ref{calc-rem:ce-trap} empties a nonempty kernel under the uncorrected law;',
      '(iv) \\emph{Bias:} the trap of Remark~\\ref{calc-rem:ce-trap} makes the one uncorrected law unsafe despite a viable corrected law;','monitoring rule bias')
a=rep(a,'--- in the admissibility form of Section 3.6.',
      '--- with a nonempty common admissible set but an empty common safe-action set (Section 3.6).','table discussion safety rung')
a=rep(a,'state-dependent admissibility example (Proposition~\\ref{calc-prop:emptiness}) &',
      'state-dependent safety-rung example (Proposition~\\ref{calc-prop:emptiness}) &','table row accurately names safety rung')
a=rep(a,'\\caption{Delayed information. The constraint margin \\(q\\) reaches zero at\n\\(t^*=q_0/\\varepsilon\\), before the first informative observation at\n\\(T_{\\mathrm{obs}}\\): the information is accurate but arrives too late\n(Theorem~\\ref{calc-thm:delayed}).}',
      '\\caption{Delayed information. Under the compatible original-path hypothesis, a still-safe branch reaches \\(q=0\\) by \\(t^*=q_0/\\varepsilon<T_{\\mathrm{obs}}\\); continuing the adverse path while it remains safe forces strict exit before the later observation deadline (Theorem~\\ref{calc-thm:delayed}). The bound need not equal the first contact time.}','figure contact bound caption')
a=rep(a,'the first informative observation must precede the enforced\nexit time \\(\\inf q / \\varepsilon\\).',
      'to avoid \\emph{this} sufficient failure test, the informative observation cannot arrive strictly after the bound \\(\\inf q / \\varepsilon\\); an earlier reading is not by itself a viability guarantee.','timing design only necessary to escape this test')
a=rep(a,'(the three two-point codices of the companion monitoring paper)',
      '(as the nonconvex safe-set example in Section 3.4 illustrates)','remove opaque companion allusion')
a=rep(a,'''\\footnotesize
\\begin{tabular}{@{}l>{\\raggedright\\arraybackslash}p{3.4cm}>{\\raggedright\\arraybackslash}p{4.4cm}@{}}''',
      '''\\footnotesize
\\resizebox{\\textwidth}{!}{\\begin{tabular}{@{}l>{\\raggedright\\arraybackslash}p{3.4cm}>{\\raggedright\\arraybackslash}p{4.4cm}@{}}''','wide certificate table fit')
a=rep(a,'''\\end{tabular}
\\caption{The obstruction certificates,''',
      '''\\end{tabular}}
\\caption{The obstruction certificates,''','close table width box')
a=rep(a,'& a separating observation; a shorter review interval \\\\',
      '& a finer observation (removes this test only) \\\\','no shorter interval promise for all-delta hold obstruction')

# --- B: accurately typed symbols and a self-contained primal in main. ---
a=rep(a,'\\(\\lambda\\): the Farkas multiplier of Theorem 3\'s certificate; the observer decay rate of Section 5(c)',
      '\\(\\lambda\\): a Farkas multiplier of Theorem 4\'s LP certificate or a recourse weight in Proposition~\\ref{calc-prop:recourse}; the observer decay rate in Section 5(c)','companion lambda attribution')
a=rep(a,'\\(\\Gamma_{h}\\): the recourse certificate of Section 5(d)',
      '\\(\\Gamma_{h}\\): the recourse certificate of Section 3.7','companion Gamma attribution')
a=rep(a,'For a finite linear model in which a resource-typed system must meet a demand vector through specified substitution pathways, exactly one of the following holds (Farkas, 1902; Gale, 1960):',
      'For the finite linear system \\(a\\in\\mathbb R^k_{\\ge0}\\), \\(Ra\\le x\\), \\(Ea\\le e\\), \\(Qa\\ge s^{\\mathrm{req}}\\), with \\(R\\in\\mathbb R^{n\\times k}\\), \\(E\\in\\mathbb R^{m\\times k}\\), \\(Q\\in\\mathbb R^{p\\times k}\\) and conformable \\(x,e,s^{\\mathrm{req}}\\), exactly one of the following holds (Farkas, 1902; Gale, 1960):','main substitution primal made explicit')

# --- B: narrow positioning; retain v69's verified numerical/source fixes. ---
a=span(a,'It does not reach the setting considered here, for a reason that is', 'Two further contrasts are worth',r'''The physical-state Hamilton--Jacobi formulation cited here does not directly solve the present record-constrained set-membership problem: its value is indexed by a physical state, whereas this article tracks sets of compatible states. Partial-observation reachability and belief-state safety have their own information-state formulations (including qualitative finite-POMDP safety); they are not excluded by the existence of a physical-state grid. Probability beliefs in Section 10 are distinct from the set-valued beliefs used in the main viability statements. Our explicitly finite/polyhedral certificates and the separately conditional original-path tests address a different verification task; no claim that every Section 3 certificate is a finite algebraic object or that every partial-observation method requires an infinite-dimensional probability-measure grid is intended. ''','related work no sweeping HJ impossibility')

# --- B: make the versioned runner and formal trust scope findable. ---
a=rep(a,'The archived \\texttt{paper2\\_coverage\\_audit.py} reproduces the\nfinite-grid classification;',
      'The versioned \\texttt{coverage\\_v70.py} runner recomputes the 48-cell hold-class classification and the plotted figure using relative repository paths;','current coverage runner in case study')
a=rep(a,'\\textbf{Code availability.} The coverage-audit script \\texttt{paper2\\_coverage\\_audit.py} is publicly available at \\url{https://github.com/MIKEAA2020/general-sustainability} (folder \\texttt{arena agent 1/paper rewrites/latex}); it regenerates Table~\\ref{calc-tab:coverage} and Figure~\\ref{calc-fig:coverage} verbatim.',
      '\\textbf{Code availability.} The versioned runner \\texttt{coverage\\_v70.py} and its hash record reside in the Paper01 v70 author-batch folder on the \\texttt{e2-v3-source-year} branch at \\url{https://github.com/MIKEAA2020/general-sustainability}; it reproduces the 48-cell discrete held-class classifications and generates the versioned Figure~\\ref{calc-fig:coverage}, not a continuous-time proof.','correct code availability')
a=rep(a,'figs_p2/fig_p2_coverage_v68.png','figs_p2/fig_p2_coverage_v70.png','new versioned coverage asset')
a=span(a,r'\noindent\textbf{Current Lean provenance.}',r'\paragraph{Two scope limits, stated plainly.}',r'''\noindent\textbf{Formal provenance and scope.} The pinned Lean~4 build previously recorded \(60/60\) jobs passing. Named finite-fragment declarations have no \texttt{sorryAx}; the audited aggregate-import footprints include nine generated axiom names from three \texttt{native\_decide} source sites, which rely on the compiler/runtime and are not kernel-only proofs. The continuous-time results, this draft's revisions, and three historical modules outside the default import closure have not been newly formalized or independently checked by that build. Exact release pin, declarations, permitted generated names, CI run identifiers and the failed old-toolchain comparison are preserved in the versioned repository provenance note; no fresh Lean rebuild is claimed here.

''','move detailed Lean CI provenance to companion note')
s=rep(s,'article Proposition 8 (two-phase decomposition) has its argument in S2.',
      'article Proposition 8 (two-phase decomposition) has its argument in S2.','supp concordance asserted')
s=rep(s,'\\noindent\\textbf{Complete proof of the linear-programming instantiation theorem (main text,\nSection 3.3).}',
      '\\noindent\\textbf{Complete proof of article Theorem 4, the linear-programming instantiation (Section 3.3).}','supp LP proof heading identifies result')

assert r'\ref{calc-prop:uniform-margin}' not in a
assert r'\ref{prop:uniform-margin}' not in s
ARTICLE_NEW.write_text(a);SUPP_NEW.write_text(s)
print('WROTE',ARTICLE_NEW.name,SUPP_NEW.name,'with',len(changes),'asserted changes:')
print('\n'.join(changes))

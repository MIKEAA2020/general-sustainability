"""Build paper5 v38 main tex from v37: venue-synthesis Nature Sustainability elevation."""
import re

SRC = '/home/user/paper5_v37/paper5_sampled_governance_v37.tex'
DST = '/home/user/paper5_v38/paper5_sampled_governance_v38.tex'
s = open(SRC, encoding='utf-8').read()
n0 = len(s)

def rep(old, new, tag):
    global s
    c = s.count(old)
    assert c == 1, f'{tag}: count={c}\n---\n{old[:200]}'
    s = s.replace(old, new, 1)
    print(f'{tag}: OK')

def repw(old_joined, new, tag):
    global s
    pat = re.compile(re.escape(old_joined).replace(r'\ ', r'\s+'))
    ms = pat.findall(s)
    assert len(ms) == 1, f'{tag}: count={len(ms)}\n---\n{old_joined[:200]}'
    s = pat.sub(lambda _: new, s, count=1)
    print(f'{tag}: OK (flex)')

# N1 version comment
rep('% Periodic Review as Sampled Governance (paper 5, revision v37): six open-items discharges (U5 case table/log, eta basis, Icelandic-cod audit, Lemma 2.2 seal application, Prop 2.1 demotion, I5 data/code split, 4.4(iii) illustration, T_r-ranked test) with line numbers for review.',
    '% The decision clock (paper 5, revision v38): venue-synthesis Nature Sustainability elevation (title, abstract, Box1-to-S1, extractive grounding, cross-sector clock, conceptual Figure 1, regimes Box, advice chain, 4.8 design principles, subsidies/UNFCCC refs) with line numbers for review.',
    'N1-version')

# N2 title
rep(r'\title{Periodic Review as Sampled Governance: Sample-and-Hold Dynamics of Assessment-Driven Effort Control, a Selected 42-Stock Spectral Screen, and the Northern Cod Case}',
    r'\title{The decision clock: review intervals as a design lever for stable resource governance}',
    'N2-title')

# N3 date
rep(r'\date{September 11, 2026}', r'\date{September 12, 2026}', 'N3-date')

# N4 abstract span replacement
bi = s.find(r'\begin{abstract}')
ei = s.find(r'\end{abstract}')
assert bi > 0 and ei > bi and s.count(r'\begin{abstract}') == 1
inner = s[bi:ei]
assert 'The review interval is a design choice with stability consequences' in inner.replace('\n', ' ')
NEW_ABSTRACT = '''Fisheries are managed on a schedule: stocks are assessed at fixed intervals and the resulting catch limits held until the next review. Standard models treat this institutional response as a continuous delay or a single annual step. We show the substitution matters. Modelling periodic review as sample-and-hold governance --- a loop that observes and updates only at review times --- we establish two exact properties, forward invariance of the sampled state space and rapid-review consistency over finite horizons only, and compute stability review-interval by review-interval. Stability boundaries move or vanish when the operator is changed: at an illustrative baseline the exact map crosses once near a 6.5-year interval while one-step approximations report artefact crossings, and the protective channel is stable at every tested interval. A multiplicity-controlled screen of 42 stocks finds no robust institutional cycles and a 32-system case search no unconfounded oscillator, showing periodicity alone cannot diagnose governance feedback; the northern cod record splits into a formulation-dependent crash and an unresolved post-collapse identification problem. What decides whether management stabilises or destabilises a fishery is therefore not biology alone but the decision clock --- the timing and form of policy revision --- a design variable with stability consequences, to be treated explicitly in management strategy evaluation.

'''
s = s[:bi + len(r'\begin{abstract}')] + '\n\n' + NEW_ABSTRACT + s[ei:]
print('N4-abstract: OK (span)')

# N5 keywords
repw('bifurcation; fisheries management',
     'bifurcation; fisheries management; decision clock; management strategy evaluation',
     'N5-keywords')

# N6 Box 1 -> short paragraph + S1 pointer
i1 = s.find(r'\textbf{Box 1. Claims at their exact evidential status.}')
i2 = s.find(r'\subsection{1 Introduction}')
assert i1 > 0 and i2 > i1
span = s[i1:i2]
assert 'Distributive constraints' in span and span.count(r'\end{longtable}') == 1
s = s[:i1] + r'''\textbf{Evidential status.} Every central claim carries its exact status --- exact, conditional, archived, provisional, or prospective --- in the statement inventory (Supplementary S1); the main text states each result once with its record pointer, and Section 4.7 collects the limitations.

''' + s[i2:]
print('N6-box1-move: OK (span)')

# N7 extractive framing paragraph
repw('serve as comparators. Conclusions drawn inside the extractive class',
     '''serve as comparators.

The extractive rule is not proposed as desirable management. It is a diagnostic representation of perverse pressure: when a perceived shortfall threatens short-term employment or revenue, the political-economic response --- subsidies that sustain effort, pressure to hold catches up --- can push extraction upward as the base declines. Capacity-enhancing subsidies are the documented form of this pressure (Sumaila et al., 2019). The protective controller is the policy-relevant comparator; the pair exists to show how controller sign interacts with review timing, not to recommend the extractive rule.

Conclusions drawn inside the extractive class''',
     'N7-extractive-frame')

# N8 cross-sector para + Figure 1
repw('analysis must state which operator a given stability claim is computed on. \\subsection{2 Material and methods}',
     '''analysis must state which operator a given stability claim is computed on.

The architecture is not unique to fisheries. National climate pledges under the Paris Agreement are communicated every five years and informed by five-yearly global stocktakes (UNFCCC, 2015, Articles 4.9 and 14): held commands under periodic review (Figure 1A). Failures then take a common form across sectors: the governance clock (the review interval), the ecological clock (the recovery rate), and the environmental clock (exogenous cycles such as ENSO, Section 3.7) fall out of phase. The timing and form of policy revision --- the review interval together with the revision rule --- is the decision clock. This article develops the fisheries case in full; Section 4.8 returns to the cross-sector reading.

\\begin{figure}[htbp]
\\centering
\\includegraphics[width=\\linewidth]{figs_p5/fig_concept_v38.png}
\\caption{The decision clock. \\textbf{A:} Three institutional architectures: continuous-delay feedback, the annual-step compression, and sample-and-hold governance, which observes at review times and holds the command between them. \\textbf{B:} Review-interval stability slice (schematic): the extractive exact update is marginally unstable at annual review (\\(\\rho=1.00035\\)) and crosses once near a 6.5-year interval (unstable \\(\\to\\) stable), while the protective update is stable throughout (\\(\\rho=0.9838\\) at annual review). Curves are schematic; markers show computed values (Section 3.4).}
\\label{fig:decision-clock}
\\end{figure}

\\subsection{2 Material and methods}''',
     'N8-crosssector-fig1')

# N9 old Figure 1 -> Figure 2
rep('complete (Figure 1). It is computed', 'complete (Figure 2). It is computed', 'N9-renumber')

# N10 terminology bridge before Table 1
rep(r'''\textbf{Table 1.} The governance-time ontology.''',
    r'''For fisheries readers, the control-theoretic vocabulary maps onto management-procedure language: the controller is the harvest control rule; the command is the catch or effort limit it sets; the review interval is the advice cycle; the hold is the plan period between revisions; and the operator --- the decision architecture on which a stability claim is computed --- is the management procedure itself. Assessment error and implementation error enter where observation meets advice and where decisions meet deployment (Table 1).

\textbf{Table 1.} The governance-time ontology.''',
    'N10-bridge')

# N11 advice-chain display after Table 1
rep('''institutional signal; not a discrete delay \\\\
\\end{longtable}

Reviews can be annual while deployment''',
    '''institutional signal; not a discrete delay \\\\
\\end{longtable}

\\[ \\text{observation} \\to \\text{assessment} \\to \\text{advice} \\to \\text{decision} \\to \\text{implementation} \\to \\text{ecological response} \\] The chain is the sequence Table 1 resolves into distinct objects; collapsing any two stages without a stated aggregation rule is the measurement-level form of architecture substitution.

Reviews can be annual while deployment''',
    'N11-advice-chain')

# N12 regimes Box 1 before Notation
rep(r'''\emph{Notation.} Throughout,''',
    r'''\textbf{Box 1. Management regimes as sample-and-hold architectures.}

Four institutional regimes in the review--hold vocabulary.

\begin{longtable}[]{@{}
  >{\raggedright\arraybackslash}p{(\columnwidth - 10\tabcolsep) * \real{0.2000}}
  >{\raggedright\arraybackslash}p{(\columnwidth - 10\tabcolsep) * \real{0.2000}}
  >{\raggedright\arraybackslash}p{(\columnwidth - 10\tabcolsep) * \real{0.2000}}
  >{\raggedright\arraybackslash}p{(\columnwidth - 10\tabcolsep) * \real{0.2000}}
  >{\raggedright\arraybackslash}p{(\columnwidth - 10\tabcolsep) * \real{0.2000}}@{}}
\toprule\noalign{}
\begin{minipage}[b]{\linewidth}\raggedright
Regime
\end{minipage} & \begin{minipage}[b]{\linewidth}\raggedright
Review
\end{minipage} & \begin{minipage}[b]{\linewidth}\raggedright
Instrument
\end{minipage} & \begin{minipage}[b]{\linewidth}\raggedright
Hold
\end{minipage} & \begin{minipage}[b]{\linewidth}\raggedright
Emergency clause
\end{minipage} \\
\midrule\noalign{}
\endhead
\bottomrule\noalign{}
\endlastfoot
Annual TAC fishery & 1 yr & TAC (quota) & 1 yr & in-year adjustment where provided \\
Multiannual plan & 3--5 yr & fishing-mortality rule & multi-year & trigger review \\
Moratorium & indefinite & closure & until review & reopening rule (Section 3.8) \\
Data-limited system & irregular & effort controls & variable & crisis response \\
\end{longtable}

\emph{Notation.} Throughout,''',
    'N12-regimes-box')

# N13 6.5 baseline clause
repw(r'a complex pair at 6.501 yr (unstable \(\to\) stable), stable on \([6.501, 200]\) yr',
     r'a complex pair at 6.501 yr (unstable \(\to\) stable) at the baseline parameter vector (Table 3), stable on \([6.501, 200]\) yr',
     'N13-baseline-clause')

# N14 rho sensitivity frame
rep('the annual-instability verdict is read at that status.',
    'the annual-instability verdict is read at that status. Near-unit-circle behaviour of this size is read as high sensitivity of the verdict to the parameter vector, not as a robust claim about annual-review institutions in general.',
    'N14-rho-frame')

# N15 F-reparameterisation next step in 4.7(ii)
rep('and they are not reproducible numerical propositions until the original computational record is attached.',
    r'and they are not reproducible numerical propositions until the original computational record is attached. The effort scale is uncalibrated: results are reported at imported catchability values, and reparameterising the controller in fishing mortality (\(F = qE\)) is the stated next step for the stage operator.',
    'N15-F-next-step')

# N16 new 4.8 before Conclusion
rep(r'''\subsection{5 Conclusion}''',
    r'''\subsubsection{4.8 Design principles for the governance clock}\label{design-principles}

The results support four design principles for the decision clock (Box 2).

\textbf{Box 2. Design principles for the governance clock.}

\begin{longtable}[]{@{}
  >{\raggedright\arraybackslash}p{(\columnwidth - 4\tabcolsep) * \real{0.3333}}
  >{\raggedright\arraybackslash}p{(\columnwidth - 4\tabcolsep) * \real{0.6667}}@{}}
\toprule\noalign{}
\begin{minipage}[b]{\linewidth}\raggedright
Principle
\end{minipage} & \begin{minipage}[b]{\linewidth}\raggedright
Content
\end{minipage} \\
\midrule\noalign{}
\endhead
\bottomrule\noalign{}
\endlastfoot
Treat timing as a control variable & The review interval is optimised alongside harvest limits in management strategy evaluation; annual review is not assumed stabilising. \\
Match the rule to the clock & Protective rules tolerate institutional rigidity; extractive rules require frequent review to contain destabilisation. \\
Decouple observation from decision & High-frequency monitoring does not require high-frequency revision; multi-year plans are stable under protective rules. \\
Design for structural breaks & Scheduled review is paired with asynchronous emergency triggers (circuit breakers) that bypass the review clock during regime shifts. \\
\end{longtable}

\textbf{Implications for management design.} Eight implications follow for review-interval choice. \begin{enumerate} \def\labelenumi{(\arabic{enumi})} \tightlist \item The review interval is a control variable: stability is computed per interval, not per loop (Section 3.4). \item Annual review is not automatically stabilising: the baseline annual verdict is unstable with a near-unit-circle margin (Section 3.4). \item Protective rules are more robust across review intervals than extractive rules: the exact protective map is stable at every tested interval (Section 3.4). \item Fixed and responsive plans are not equivalent instruments: a held multi-year command and an annually revised rule are different operators (Sections 2.6 and 4.4). \item Emergency triggers are modelled separately from scheduled reviews: structural breaks between reviews are invisible to the fixed clock (Sections 3.8 and 4.5). \item Management strategy evaluation treats the review interval as an explicit factor alongside the control rule (Section 4.5). \item Spectral periodicity is not evidence of institutional cycles: the screen's null carries no controller-sign information (Sections 3.5--3.7). \item Observation, assessment, decision, deployment, and response lags are not collapsed into one governance lag (Section 2.1). \end{enumerate}

Beyond fisheries, the framework is reusable as a modelling discipline: it answers how periodic governance should be represented in ecological models, how the stages of the advice chain should be kept distinct, and how modellers can test whether a stability claim survives a change of decision operator.

The logistic core is illustrative; the structural results are the operator-dependence of the stability verdict, the finite-horizon scope of the rapid-review limit, and the non-equivalence of one-step and exact updates as a caution within the studied class.

Sample-and-hold architectures beyond fisheries face the same clock-mismatch failure mode: five-yearly climate pledges held between global stocktakes (UNFCCC, 2015) align a political review clock with ecological and environmental clocks only by design, not by default.

\subsection{5 Conclusion}''',
    'N16-design-principles')

# N17 conclusion closing
repw('and one descriptive split.',
     'and one descriptive split. The decision clock --- the timing and form of policy revision --- is therefore a design variable with stability consequences.',
     'N17-conclusion')

# N18a Sumaila reference
repw('Stuart, A. M., and Humphries, A. R. 1996. Dynamical Systems and Numerical Analysis. Cambridge University Press, Cambridge.',
     '''Stuart, A. M., and Humphries, A. R. 1996. Dynamical Systems and Numerical Analysis. Cambridge University Press, Cambridge.

Sumaila, U. R., Ebrahim, N., Schuhbauer, A., Skerritt, D., Li, Y., Kim, H. S., Mallory, T. G., Lam, V. W. L., and Pauly, D. 2019. Updated estimates and analysis of global fisheries subsidies. Marine Policy, 109: 103695.''',
     'N18a-sumaila')

# N18b UNFCCC reference
rep('World Bank. Poverty and Inequality Platform. World Bank, Washington, DC.',
    '''UNFCCC. 2015. Paris Agreement. United Nations Framework Convention on Climate Change.

World Bank. Poverty and Inequality Platform. World Bank, Washington, DC.''',
    'N18b-unfccc')

print('--- post-checks ---')
print('decision clock:', s.count('decision clock'))
print('Sumaila:', s.count('Sumaila'))
print('UNFCCC:', s.count('UNFCCC'))
print('(Figure 1A):', s.count('(Figure 1A)'), '(Figure 2):', s.count('(Figure 2)'))
print('Box 1:', s.count('Box 1.'), 'Box 2:', s.count('Box 2.'))
print('math-open:', s.count('\\('), 'math-close:', s.count('\\)'))
print('begin-figure:', s.count(r'\begin{figure}'), 'end-figure:', s.count(r'\end{figure}'))
print('begin-enumerate:', s.count(r'\begin{enumerate}'), 'end-enumerate:', s.count(r'\end{enumerate}'))
print('len delta:', len(s) - n0)
assert s.count('Sumaila') >= 2 and s.count('UNFCCC') >= 3
assert s.count('(Figure 1A)') == 1 and s.count('(Figure 2)') == 1
assert s.count(r'\begin{figure}') == s.count(r'\end{figure}') == 2
assert s.count('\\(') == s.count('\\)')
assert 'Claims at their exact evidential status' not in s

open(DST, 'w', encoding='utf-8').write(s)
print('WROTE', DST)

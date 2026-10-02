#!/usr/bin/env python3
"""One abstract, two part lead-ins, a non-diary supplement and scoped fold claims."""
from pathlib import Path
import re,difflib
R=Path('/home/user');P=R/'papers';D=R/'content_audit/journal_submission/diffs';D.mkdir(parents=True,exist_ok=True)
def once(t,a,b):
 assert t.count(a)==1,(a[:130],t.count(a));return t.replace(a,b,1)
def save(name,source,t):
 p=P/name;old=P/source;assert old.exists();p.write_text(t)
 (D/(name+'.diff')).write_text(''.join(difflib.unified_diff(old.read_text().splitlines(True),t.splitlines(True),fromfile=source,tofile=name)))
 print(name,len(t.splitlines()))
src='paper08_governance_delay_v47.tex';t=(P/src).read_text()
abstract=r'''\begin{abstract}
Institutional response delay and periodic review are distinct ways of representing governance latency in renewable-resource models. For a calibrated continuous-feedback model, the linearized characteristic equation identifies two mobilising-channel stability crossings, whereas a small-gain condition establishes delay-independent local stability for the protective channel. Interval enclosures certify local characteristic roots at the declared coefficients; the numerical periodic-orbit topology is not a proved fold theorem for the continuous delay equation. For periodic review, exact sample-and-hold monodromy and one-step command approximations yield different stability boundaries at the illustrative baseline: the exact mobilising map crosses near a 6.5-year review interval, while Euler steps produce artefact crossings; the exact protective map stays spectrally stable over the tested grid. The 6.5-year crossing is parameter-sensitive and is not a policy threshold. A multiplicity-controlled screen of 42 fish stocks finds no robust target-band institutional cycle, and a 32-system case search finds no unconfounded cross-sector oscillator. Thus the supported representation result is local and model-specific: changing a specified feedback or review operator can change its computed stability verdict. No identity between continuous deployment delay $\tau$ and discrete review interval $T_r$, or transfer of one operator's threshold to the other, is asserted.
\end{abstract}'''
a=t.index(r'\begin{abstract}');b=t.index(r'\end{abstract}',a)+len(r'\end{abstract}');t=t[:a]+abstract+t[b:]
# Preserve both authored part abstracts as section lead-ins while keeping only one abstract environment.
p=t.index(r'\part*{Part I');head=t[:p];body=t[p:]
assert body.count(r'\begin{abstract}')==2 and body.count(r'\end{abstract}')==2
body=body.replace(r'\begin{abstract}',r'\subsection*{Study scope and principal findings}',2).replace(r'\end{abstract}',r'\par',2)
t=head+body
# Remove source-provenance description but keep a brief, reader-oriented roadmap.
old=r'''\noindent\textbf{Structure.} Part I is the continuous-delay study and Part II the sampled-review
study. Each is self-contained --- its own model, results, discussion and conclusions --- and each is
reproduced in full from its companion paper without condensation, opening with that paper's own
abstract. A cross-regime conclusion follows, stating what transfers between the two formalisations
and what does not.'''
# Old paragraph is outside the replacement and therefore gone with the composite abstract.
assert old not in t
# Put all authored keyword phrases in one journal-frontmatter list.
kw=r'''\noindent\textbf{Keywords:} delay differential equations; Hopf bifurcation; institutional feedback; renewable resource management; fisheries governance; sample-and-hold control; regime shifts; maturation delay; recruitment dynamics; sample-and-hold governance; review interval; decision clock; institutional delay; management strategy evaluation; fisheries management; environmental governance
'''
t=once(t,r'\maketitle',r'\maketitle'+'\n\n'+kw)
t=once(t,r'''\textbf{Keywords:} delay differential equations; Hopf bifurcation;
institutional feedback; renewable resource management; fisheries
governance; sample-and-hold control; regime shifts; maturation delay;
recruitment dynamics''','')
t=once(t,r'''\textbf{Keywords:} sample-and-hold governance; review interval; decision clock; institutional delay; management strategy evaluation; fisheries management; environmental governance''','')
# Part I lead-in and core descriptions cannot claim a validated infinite-dimensional fold.
t=once(t,'two folds certified at the discrete collocation level (continuum stages\nopen), and a basin-boundary transition toward an unverified\nlarge-amplitude attractor.', 'two Krawczyk-enclosed candidates in the finite collocation systems, with\ncontinuous-delay fold validation open; the basin-transition and\nlarge-amplitude attractor interpretations remain numerical.')
t=once(t,'Institutional form and timing, not ecological lag, decide\nwhether governance stabilises or destabilises the stock;', 'In this calibrated model, feedback form and timing affect local stability;')
t=once(t,'meet at one \\emph{discrete-collocation} Krawczyk-certified fold ---\n  and the upper boundary carries a second fold certified at the\n  discrete-collocation level near 64.4 yr of a second S-branch.', 'meet near a Krawczyk-enclosed Moore--Spence zero of the finite collocation system ---\n  and an analogous enclosure occurs near 64.4 yr for the second branch.\n  The latter has recorded finite-dimensional nondegeneracy checks; neither\n  enclosure by itself establishes a fold of the continuous delay equation.')
t=once(t,'combines a certified-fold structure with an uncollocatable,','combines finite-dimensional fold candidates with an uncollocatable,')
t=once(t,'certified at the discrete collocation level (the rebuilt\nMoore--Spence/Krawczyk stage for the lower fold; the interval-Krawczyk\ncertificate for the second fold --- for each, the continuum off-grid\nresidual stage remains unimplemented and the continuous-delay lift\nremains open); no continuous-delay fold proof is claimed.', 'enclosed as Moore--Spence candidates in finite collocation systems\n(Krawczyk enclosures for both; a discrete nondegeneracy record for the\nupper candidate). Off-grid residual bounds and a lift to the continuous\ndelay equation have not been established; no continuous-delay fold\nproof is claimed.')
t=once(t,'whose lower and upper boundaries are both fold-certified at the discrete\ncollocation level, and whose basin boundary lies between the two folds\nrather than at either; the saddle-node classification remains\nprovisional.', 'with two Krawczyk-enclosed finite-dimensional turning candidates and\na distinct basin-transition interval; the corresponding continuous-delay\nfold and saddle-node classifications remain open.')
t=once(t,'one fold. The fold is interval-certified at the discrete collocation\nlevel --- the rebuilt Krawczyk stage of the A025 pipeline encloses the\nunique Moore--Spence zero', 'one apparent turning point. For the finite collocation map, a\nKrawczyk inclusion encloses a unique Moore--Spence zero')
t=once(t,'the fold-location certificate is the Krawczyk enclosure above,','the finite-collocation location enclosure is the Krawczyk box above,')
# Replace literal overcertification claims consistently without altering root/Hopf certificates.
subs={'from the certified second fold':'from the Krawczyk-enclosed second turning candidate',
 'single Krawczyk-certified fold':'Krawczyk-enclosed finite-dimensional turning candidate',
 'at the certified \\(\\tau_{f2}':'near the collocation-enclosed \\(\\tau_{f2}',
 '\\textbf{certified second fold at':'\\textbf{finite-collocation second turning candidate at',
 'interval-Krawczyk-certified Moore--Spence zero':'interval-Krawczyk-enclosed Moore--Spence zero',
 'Krawczyk-certified\nat the discrete collocation level':'Krawczyk-enclosed\nin the finite collocation system',
 'the certified second fold at':'the finite-collocation second turning candidate near',
 'certified three-state second fold':'finite-collocation second turning candidate',
 'the certified second fold sits':'the finite-collocation turning candidate lies',
 'two certified folds at the discrete\ncollocation level':'two Krawczyk-enclosed finite-collocation turning candidates',
 'provisional saddle-node against a crisis reading, and the fold\n  certification registered for both folds at the discrete collocation\n  level':'provisional saddle-node against a crisis reading, with Krawczyk\n  enclosures registered for both finite-dimensional turning candidates',
 }
for x,y in subs.items():
 assert x in t,x;t=t.replace(x,y)
# Make independence of the representation result and the unproved global fold explicit as a scientific scope condition.
bridge=r'\noindent\textbf{Bridge between operators.} Part I varies an institutional response lag \(\tau\) inside a continuous feedback law; Part II varies the review interval \(T_r\) of a sample-and-hold map. Their spectral boundaries are not estimates of one shared delay, so each result retains its own model and evidential scope.'
bridge2=bridge+' The local spectral comparisons use the characteristic equation and sampled monodromy, not a fold theorem for periodic orbits. A continuous-delay fold theorem would strengthen the global-attractor interpretation, but is not a premise of the operator-contrast result.'
t=once(t,bridge,bridge2)
# Eliminate narrative version history from the supplement pointer; scope both attachments by their own content.
t=once(t,"S3's status list describes the pre-rebuild state of the A025 fold\ncomputation; the status note, S12, records the current state", 'S3 and S12 distinguish finite-collocation enclosures from the open\ncontinuous-delay lift')
t=t.replace('paper08\\_governance\\_delay\\_v47\\_supplementary\\_delay.md','paper08\\_governance\\_delay\\_v48\\_supplementary\\_delay.md').replace('paper08\\_governance\\_delay\\_v47\\_supplementary\\_governance.md','paper08\\_governance\\_delay\\_v48\\_supplementary\\_governance.md')
t=''.join(l for l in t.splitlines(True) if not l.lstrip().startswith('%')).lstrip('\n')
assert t.count(r'\begin{abstract}')==1 and t.count(r'\end{abstract}')==1
save('paper08_governance_delay_v48.tex',src,t)
# Delay supplement: state current facts once; no obsolete list or version history.
src='paper08_governance_delay_v47_supplementary_delay.md';t=(P/src).read_text();t=once(t,'(version 47).','.')
t=once(t,'The rebuilt fold pipeline at $m = 64/96/128$','The finite-collocation pipeline at $m = 64/96/128$')
a=t.index('## S3. The Fold-Certificate Gap');b=t.index('\n---\n\n## S4.',a)
new_s3=r'''## S3. Finite-collocation turning candidates and the continuous-delay gap

The two periodic-orbit turning candidates are distinguished from folds of the infinite-dimensional delay equation. For the lower candidate, a Krawczyk inclusion encloses a zero of the phase-fixed Moore–Spence equations of the $m=64$ Fourier collocation map near $\tau_f=5.587236198690$. A separate interval-Krawczyk enclosure and reported finite-dimensional nondegeneracy constants pertain to the upper candidate near $\tau_{f2}=64.402327203370$ (S12). These statements are about finite algebraic discretisations, not continuous-time periodic orbits.

**Definition S3.1** (Phase-fixed Moore–Spence system). With $m=64$ Fourier nodes, $Y\in\mathbb{R}^{192}$, unknown period $T$, phase-fixed residual $F(Y,T;\tau)\in\mathbb{R}^{193}$, right nullvector $v\in\mathbb{R}^{193}$ and normalisation $\ell$, the augmented system is
$$\mathcal{M}(Y,T,\tau,v)=\bigl(F(Y,T;\tau),\ D_{(Y,T)}F(Y,T;\tau)v,\ \ell^\top v-1\bigr)=0.$$
It has 387 unknowns and equations. Inclusion of a zero of $\mathcal M$ is not by itself an infinite-dimensional saddle-node theorem. Discrete nondegeneracy requires an enclosed left nullvector $w$ and exclusion of zero from both $w^\top F_\tau$ and $w^\top D^2F[v,v]$, with a regular phase condition; the upper candidate reports these checks, while their full enclosure is not established here for the lower candidate.

**Open validation obligations.** A contracting free-$\tau$ enclosure suitable for the lower turning region, a complete interval nondegeneracy record for that candidate, off-grid Fourier residual bounds, and a bordered radii-polynomial or comparable lift to the continuous delay equation are not supplied. Truncation does not eliminate the tail of $f(U,SU)$: softplus, rational terms and gated products create infinitely many Fourier modes even when $U$ has finite support. Thus the finite-dimensional enclosures and numerical multipliers do not establish a fold of periodic orbits for the continuous-delay system. The global five-regime attractor interpretation remains numerical and basin-dependent; the local characteristic-spectrum and sampled-map stability analyses do not require this fold claim. Rigorous delay-equation saddle-node results for other specified classes (Beretka and Vas, 2020) do not close this gap.

**Model scope.** The numerical branch concerns the gated inner three-state core. Nothing here transfers a fold to the turnover-corrected four-state core, the finite-donor primitive system, stage-structured models or spatial systems.
'''
t=t[:a]+new_s3+t[b:]
t=once(t,'## S7. Evidence-tier synopsis','## S7. Evidence-tier synopsis') if False else t
t=once(t,'This section is an evidence-tier synopsis, not a complete per-statement inventory. The latter is not supplied with this supplementary file; individual main-text claims must therefore be checked against their displayed proof or named computational record.', 'The classification below is a thematic evidence-tier synopsis rather than an exhaustive claim-by-claim table. The scope of each result is given in its statement, proof, interval record or computational protocol.')
a=t.index('**S3 status note.**');b=t.index('\n\n**Statement-label mapping.**',a)
t=t[:a]+'''**Collocation-certificate scope.** The lower candidate is enclosed as a Moore–Spence zero for the $m=64$ collocation map in $[5.587236198689,5.587236198691]$; the upper candidate has a finite-dimensional Krawczyk enclosure and reported nondegeneracy tests. Off-grid residual estimates and a lift to a continuous-delay periodic-orbit fold remain open. See S3 for the precise distinction.''' + t[b:]
t=t.replace('fold-certified','collocation-enclosed').replace('pre-rebuild','').replace('rebuilt','')
save('paper08_governance_delay_v48_supplementary_delay.md',src,t)
src='paper08_governance_delay_v47_supplementary_governance.md';t=(P/src).read_text();t=once(t,'(version 47).','.');save('paper08_governance_delay_v48_supplementary_governance.md',src,t)

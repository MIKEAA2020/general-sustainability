"""Deterministic additive v43/SIv10 build; old files remain immutable."""
from pathlib import Path
import json,re,difflib,shutil
ROOT=Path(__file__).resolve().parents[1];M=ROOT/'manuscript';BASE=(ROOT/'inherited_v42/manuscript/paper4_delay_dynamics_v42.tex').read_text();text=BASE;ledger=[]
def replace(old,new,reason):
 global text
 if old not in text:raise ValueError('Missing target: '+reason)
 text=text.replace(old,new);ledger.append({'reason':reason,'old':old,'new':new})
def block(start,end,new,reason):
 global text
 a=text.index(start);b=text.index(end,a);old=text[a:b];text=text[:a]+new+text[b:];ledger.append({'reason':reason,'old':old,'new':new})
ext=(M/'main_extensions_v43.tex').read_text()
def part(name):return ext.split('% BLOCK '+name+'\n',1)[1].split('% END '+name,1)[0]
block('\\begin{abstract}','\\textbf{Keywords:}',r'''\begin{abstract}
Governance delay links observed resource decline to deployed effort. A
stock--memory--effort model compares mobilising effort escalation with
protective quota tracking, separating deployment latency from periodic
review. For four registered mobilising vectors, an analytic
characteristic-root count and interval crossing-order checks classify
equilibrium stability on the entire positive delay axis. Candidate A
has two stable delay windows, not only the interval between the
fundamental Hopf crossings. Classical nonlinear Hopf hypotheses are
verified at the declared crossings; these local results do not classify
all nonlinear attractors.

For the protective law, a nonlinear asymptotic-gain theorem identifies
the complete positive-equilibrium basin within the physical state space.
It covers every fixed finite delay and every positive fixed cadence
under native signal-hold and exact nonlinear quota review. A sufficient
gain is below 0.475 at the common point and below 0.687 throughout a
declared parameter box. The excluded extinction and saturated-effort
faces remain invariant; Euler and mixed-channel laws do not inherit the
result.

Periodic continuation and capture checks connect the upper stable
family. Odd-grid fold refinements and rigorous infinite-Fourier orbit
and kernel residual bounds advance continuum validation, without
substituting for the missing bordered inverse and contraction proof.
Retrospective North Sea herring tests add quantitative field challenges:
the protective response narrowly beats AR(1), but the ecological and
recursive annual-surrogate stock predictions fail baseline comparisons.
These mixed outcomes distinguish conditional response skill from joint
dynamic validation of the autonomous delay model. Response law,
latency and cadence are mathematical design coordinates whose field
identification requires direct institutional measurements and an adequate
ecological observation model.
\end{abstract}

''','Abstract integrates new complete theorems and genuine mixed field outcomes')
replace('\\subsection{6. ',part('SPECTRUM')+'\n\\subsection{6. ','Add complete all-delay equilibrium theorem')
replace('\\subsection{8. Global Numerics',part('BASIN')+'\n\\subsection{8. Global Numerics','Add complete nonlinear protective basin theorem')
replace('\\subsection{9. The Delayed-Recruitment',part('FOLD')+'\n\\subsection{9. The Delayed-Recruitment','Add rigorous infinite-series residual evidence and its limits')
replace('\\subsubsection{11.5 Certification levels}',part('FIELD')+'\n\\subsubsection{11.5 Certification levels}','Add quantitative field tests including negative endpoints')
replace('both, the continuum off-grid residual stage and the continuous-delay\n  lift remain \\textbf{open};','both, rigorous full Fourier residual bounds are supplied in Section 8.7,\n  but the continuous-delay existence lift remains \\textbf{open};','Update introductory fold status')
replace('collocation system, the continuum off-grid residual stage is still open,','collocation system; full infinite-series residual bounds are now available,\nbut the continuum inverse/contraction argument is still absent,','Update lower-fold certification status')
replace('certificate for the second fold --- for each, the continuum off-grid\nresidual stage remains unimplemented and the continuous-delay lift\nremains open)', 'certificate for the second fold --- for each, full infinite-series\nresidual bounds are now available, but the continuum inverse/contraction\nand nondegeneracy proof remains open)', 'Update section-wide residual status after whole-series validation')
replace('All results in this section are numerical results at their declared','Except for the rigorous residual bounds of Section 8.7, the results in\nthis section are numerical results at their declared','Distinguish interval residual proof from nominal continuation')
replace('What the documented timelines ground is the scale of the two timing\ncoordinates, not the coefficients of any theorem. No stock, effort law,\nor delay value in this paper is calibrated to a named fishery,','What the documented timelines ground is the scale of the two timing\ncoordinates, not the coefficients of any theorem. The registered\ntheoretical vectors are not calibrated to a named fishery,','Distinguish new fitted proxy predictors from unchanged theoretical vectors')
replace('and they mark the empirical programme named in\nthe conclusion as prospective.','and they motivate the direct dynamic tests below rather than supplying\nan identified institutional mechanism.','Remove obsolete purely prospective field-test claim')
replace('without\nconverting any theorem into a claim about a named institution.','without\nconverting any theorem into a claim about a named institution. The\nfollowing assessment-based tests are a separate predictive investigation.','Separate event clocks from quantitative field tests')
a='The paper\'s results carry three distinct certification levels, and the'
b='Rigorous saddle-node results for delay equations exist'
block(a,b,r'''The results distinguish four evidential levels:
\begin{enumerate}
\item \textbf{Theorems.} The modulus and loop-gain algebra, nonlinear
Hopf hypotheses, complete equilibrium root count (Theorem 5.2), review
operators and complete protective basin (Theorem 7.5) have their stated
analytic assumptions and proofs. The protective robustness box is not
an empirical confidence region.
\item \textbf{Interval bounds.} Outward arithmetic encloses fundamental
and recurrent crossing delays, nonlinear Hopf coefficients, protective
gain margins and whole-series fold residuals. Finite Krawczyk fold
inclusions concern their declared collocation systems. Neither narrow
finite intervals nor a small infinite-series residual alone proves a
continuum fold.
\item \textbf{Numerical global evidence.} Periodic continuation,
finite-history capture and computed Floquet multipliers support the
reported branches on the explored domain, not complete mobilising
basins or the entire periodic spectrum. Continuum inverse/contraction
and nondegeneracy estimates remain necessary for fold existence.
\item \textbf{Field tests.} Event endpoints constrain timing
interpretation. Assessment-based predictors have explicit splits,
baselines, observation gauges and negative endpoints; they do not
identify latent institutional delay or validate the autonomous DDE.
\end{enumerate}

''','Replace obsolete status list with theorem/interval/numerical/field distinctions')
replace('The model class is a mathematical parameterisation: no stock, effort\n  law, or delay value is calibrated to a named fishery, and the\n  institutional coefficients have not been identified from field data;','The model class is a mathematical parameterisation. The theoretical\n  vectors are not fishery calibrations; fitted assessment-proxy predictors\n  do not identify institutional coefficients or deployment delay. The\n  joint ecological and recursive stock tests fail their baseline comparisons;','Update limitation without conflating predictive fits and institutional identification')
replace('complete basin classification in regime (iii) remains open.','complete mobilising basin classification in regime (iii) remains open.\n  This does not limit the distinct complete protective basin theorem.','Separate achieved protective closure from open mobilising closure')
replace('and the continuum lift of both fold systems, and','and the continuum existence lift of both fold systems beyond the full\ninfinite-series residual bounds, and','Identify actual residual-to-existence obstruction')
replace('and 7.4 already supply a separate parameter-box result, without','through 7.5 already supply separate local, viability and complete-basin\nparameter-box results, without','Update protective theorem coverage in open problems')
replace('(for each fold the continuum off-grid\nresidual stage and the continuous-delay lift remain open, and the\nsaddle-node classification is provisional).','(for each fold the whole-series residual is rigorously bounded, but the\ncontinuum inverse, contraction and saddle-node nondegeneracy proof remain\nopen). The equilibrium root-count theorem additionally resolves every\npositive delay, including a second Candidate A stability window beyond\nthe fundamental range.','Update conclusion with complete spectrum and remaining fold obstruction')
replace('stock-floor guarantee on an admissible operating region, and an Euler','stock-floor guarantee, a complete interior basin under the strict global\ngain inequality with parameter-box margin, and an Euler','Elevate protective conclusion to actual global theorem')
replace('The empirical programme that follows is the identification\nof these coordinates in field institutions.','The herring tests provide a first quantitative challenge: a small\nprotective response advantage is not sufficient when ecological and\nrecursive stock predictions fail. Identifying these coordinates in field\ninstitutions therefore requires direct process measurements and a stock\nmodel that passes independent predictive comparisons.','Conclusion reflects completed dynamic tests and their failures')
replace('The supplementary material, \\texttt{paper4\\_supplementary\\_v9.pdf},','The supplementary material, \\texttt{paper4\\_supplementary\\_v10.pdf},','Versioned supplement reference')
replace('extraction and identification protocol (S16). Numerical and interval','extraction and identification protocol (S16); complete equilibrium root\ncounts (S17); the full protective basin proof (S18); infinite-Fourier\nresidual validation (S19); and dynamic field methods and results (S20).\nNumerical and interval','Supplement cross-references cover all new proofs and field evidence')
replace('event table are provided in the versioned v42 computational package at','event table are preserved in the versioned v42 computational package at','Preserve exact earlier package citation')
replace('The stage-analysis machinery of Section 9 is','The new complete-spectrum and basin calculations, exact-decimal fold\nresidual bounds, frozen public ICES responses, analysis amendments and\npointwise field predictions are supplied in the additive v43 package at\n\\url{https://github.com/MIKEAA2020/general-sustainability/tree/main/batch%209/agent%202/governance_elevation/P4_v43_P02}.\nThe stage-analysis machinery of Section 9 is','Add current evidence location without changing prior citations/deposits')
replace('\\subsection{References}\\label{references}','\\subsection{References}\\label{references}\n\nICES (2025). Stock Assessment Graphs: her.27.3a47d, assessment key 19373,\nassessment year 2025. StockDownload, SummaryTable and StockSettings API\nresponses, retrieved 29 October 2026.\n\\url{https://sag.ices.dk/SAG_API/api/StockDownload?assessmentKey=19373}.\n','Cite actual frozen API source; no misattributed special-request DOI')
replace('\\input{theorems_v42.tex}','\\input{theorems_v43.tex}','Versioned theorem-source filename')
for old in ['fig1_global_topology_v42.png','fig2_upper_branch_v42.png','fig3_waveform_match_v42.png']:
 new=old.replace('v42','v43');shutil.copyfile(ROOT/'inherited_v42/figures'/old,ROOT/'figures'/new)
 if old in text:replace(old,new,'Versioned retained figure '+old)
th=(ROOT/'inherited_v42/manuscript/theorems_v42.tex').read_text().replace('fig3_waveform_match_v42.png','fig3_waveform_match_v43.png');(M/'theorems_v43.tex').write_text(th)
text=text.replace('% Governance v42: additive revision of the pinned v41; prior source preserved.','% Governance v43: additive revision; earlier sources preserved.')
(M/'paper4_delay_dynamics_v43.tex').write_text(text)
(ROOT/'data/manuscript_operations_v43.json').write_text(json.dumps(ledger,indent=2)+'\n');(ROOT/'data/manuscript_v42_to_v43.diff').write_text(''.join(difflib.unified_diff(BASE.splitlines(True),text.splitlines(True),fromfile='v42.tex',tofile='v43.tex')))
# Supplement: preserve all prior scientific sections and append full proofs.
s=(ROOT/'inherited_v42/manuscript/paper4_supplementary_v9.md').read_text().replace('Governance manuscript v42; supplementary material v9','Governance manuscript v43; supplementary material v10')
s=s.replace('S13--S16 give','S13--S16 give').replace('and institutional-event protocol.','and institutional-event protocol. S17--S20 supply complete equilibrium spectra, the complete protective basin, full Fourier residual bounds and quantitative field tests.')
s=s.replace('Proposition 6.1.2','Proposition 5.2')
s=s.replace('The continuous-delay saddle-node theorem remains open.','S19 adds interval bounds for the whole infinite orbit/kernel residual series. The continuous-delay saddle-node theorem still requires the bordered inverse, contraction and nondegeneracy proof.')
s=s.replace('The current package supplies the endpoint data and exact model symmetries needed to make that test identifiable rather than implying it has already been achieved.','S20 supplies quantitative assessment-based dynamic tests; its observation gauge, non-confirmatory amendment, ecological competitors and negative recursive endpoints are separate from these event-clock data.')
e=(M/'supplement_extensions_v10.md').read_text().replace('silently lost early targets differently across lag candidates','had unequal early target availability across lag candidates')
d=lambda name:json.loads((ROOT/'data'/name).read_text())
t='| Candidate | Gate | All stable intervals (approximate endpoints, yr) | Eventual-instability cutoff (approx., yr) |\n|---|---|---|---:|\n'
for r in d('global_equilibrium_spectrum_v43.json')['records']:
 windows='; '.join('('+f"{float(w['left_Hopf_interval'][0]):.9f}, {float(w['right_Hopf_interval'][1]):.9f}"+')'for w in r['all_positive_delay_stability_windows']);t+=f"| {r['candidate']} | {'gated'if r['gated']else'ungated'} | {windows} | {float(r['no_stable_delay_above'][1]):.6f} |\n"
e=e.replace('SPECTRAL_TABLE',t)
t='| Fold | Orbit residual upper bounds, N/Z/E | Kernel residual upper bounds, N/Z/E |\n|---|---|---|\n'
for r in d('interval_fourier_residual_v43.json')['records']:
 # Deliberately round UP to three significant digits for displayed upper bounds.
 from decimal import Decimal,ROUND_CEILING
 def ceil3(x):
  z=Decimal(x);q=Decimal(10)**(z.adjusted()-2);return str(z.quantize(q,rounding=ROUND_CEILING))
 t+=f"| {r['fold']} | "+', '.join(ceil3(x)for x in r['residual_weighted_l1_component_upper_bounds'])+' | '+', '.join(ceil3(x)for x in r['null_residual_weighted_l1_component_upper_bounds'])+' |\n'
e=e.replace('FOURIER_TABLE',t)
t='| Biomass scenario | Response | RMSE | RMSE/persistence | RMSE/AR(1) |\n|---|---|---:|---:|---:|\n'
for scenario,rr in d('field_response_test_v43.json')['scenarios'].items():
 for law,r in rr.items():t+=f"| {scenario} | {law} | {r['RMSE']:.8f} | {r['RMSE_ratio_to_persistence']:.8f} | {r['RMSE_ratio_to_AR1']:.8f} |\n"
e=e.replace('RESPONSE_TABLE',t)
f=d('field_stock_and_recursive_v43.json');t='| Stock component | RMSE | RMSE/persistence | RMSE/AR(1) |\n|---|---:|---:|---:|\n'
for law,r in f['one_step_test'].items():t+=f"| {law} | {r['RMSE']:.8f} | {r['RMSE_ratio_to_persistence']:.8f} | {r['RMSE_ratio_to_AR1']:.8f} |\n"
e=e.replace('STOCK_TABLE',t);t='| Recursive law | Stock/persistence | Stock/VAR(1) | Proxy/persistence | Proxy/VAR(1) |\n|---|---:|---:|---:|---:|\n'
for law,r in f['recursive_test'].items():t+=f"| {law} | {r['stock_RMSE_ratio_to_constant_persistence']:.8f} | {r['stock_RMSE_ratio_to_VAR1']:.8f} | {r['proxy_RMSE_ratio_to_constant_persistence']:.8f} | {r['proxy_RMSE_ratio_to_VAR1']:.8f} |\n"
e=e.replace('RECURSIVE_TABLE',t)
s+='\n'+e
s=s.replace('fig3_waveform_match_v42.png','fig3_waveform_match_v43.png')
(M/'paper4_supplementary_v10.md').write_text(s)
meta=(ROOT/'inherited_v42/manuscript/pdf_metadata_SIv9.tex').read_text().replace('v9:','v10:').replace('nonlinear stock floors and institutional event evidence','complete equilibrium spectra, protective basins, full Fourier residual bounds and dynamic field tests');(M/'pdf_metadata_SIv10.tex').write_text(meta)
print('Built v43/SIv10 sources;',len(ledger),'explicit main operations')

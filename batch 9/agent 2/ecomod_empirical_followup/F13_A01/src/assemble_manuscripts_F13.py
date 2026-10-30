#!/usr/bin/env python3
"""Additive single-paper integration. Only minimal frozen typesetting inputs copied.
No protected source package is edited. Scientific substitutions are explicit here.
"""
import hashlib,json,re,shutil
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
F11=ROOT.parent/'ecomod_empirical_elevation_F11_A01'
if not F11.is_dir():F11=ROOT.parent/'F11_A01'
SUPPORT=ROOT/'paper_support'
TITLE='Ecological assets behind improving accounts: national forest evidence and biomass-change identifiability'
OLD='Ecological assets behind improving accounts: a boundary-matched test of biomass-change identifiability'
URL='https://github.com/MIKEAA2020/general-sustainability/tree/main/batch%209/agent%202/ecomod_empirical_followup/F13_A01'

def require(ok,msg):
 if not ok:raise ValueError(msg)
def once(t,old,new):
 require(t.count(old)==1,'Integration anchor count: '+old[:75]);return t.replace(old,new,1)
def rewrite_paths(t):
 for prefix in ['inherited_F10/','results/','src/']:
  t=t.replace('\\input{'+prefix,'\\input{paper_support/'+prefix)
 return t

def prepare_support():
 records=[]
 paths=['inherited_F10/results/availability_numbers.tex',
        'inherited_F10/results/account_coverage_F06.pdf',
        'inherited_F10/results/brazil/BRA_F05_support_fractions.pdf',
        'results/numbers_F11.tex','results/coverage_table_F11.tex','results/contrast_table_F11.tex','results/frontier_table_F11.tex',
        'results/joint_identification_F11.pdf','results/identification_frontier_F11.pdf',
        'src/methods_addition_F11.tex','src/results_addition_F11.tex','src/SI_addition_F11.tex']
 for name in paths:
  src=F11/name;dest=SUPPORT/name;dest.parent.mkdir(parents=True,exist_ok=True)
  b=src.read_bytes();data=rewrite_paths(b.decode()).encode()if src.suffix=='.tex'else b
  dest.write_bytes(data);records.append(dict(original_relative_path=name,vendored_relative_path=str(dest.relative_to(ROOT)),
   original_sha256=hashlib.sha256(b).hexdigest(),vendored_sha256=hashlib.sha256(data).hexdigest(),
   edit='input path prefix only'if data!=b else'byte-identical copy'))
 for kind in ['main','SI']:
  src=F11/f'followup_F11_A01_{kind}.tex';dest=SUPPORT/'templates'/f'F11_{kind}.tex';dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,dest)
  records.append(dict(original_relative_path=src.name,vendored_relative_path=str(dest.relative_to(ROOT)),original_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),vendored_sha256=hashlib.sha256(dest.read_bytes()).hexdigest(),edit='byte-identical template'))
 (ROOT/'metadata/minimal_typesetting_dependencies_F13.json').write_text(json.dumps(dict(original_package='F11_A01',immutable_commit='ce9a36f1bc17a84c3fd0994500766e1df72f3ae8',files=records,no_full_package_copy=True),indent=2)+'\n')

def build():
 if not(SUPPORT/'templates/F11_main.tex').exists():prepare_support()
 t=(SUPPORT/'templates/F11_main.tex').read_text();t=rewrite_paths(t)
 t=once(t,'\\graphicspath{{results/}{inherited_F10/results/}}','\\graphicspath{{paper_support/results/}{paper_support/inherited_F10/results/}}')
 t=once(t,'\\emergencystretch=3em','\\emergencystretch=3em\n\\renewcommand{\\topfraction}{0.9}\n\\renewcommand{\\textfraction}{0.07}\n\\renewcommand{\\floatpagefraction}{0.85}\n\\setcounter{topnumber}{3}')
 t=t.replace(OLD,TITLE).replace('Ecological assets behind improving accounts:\\\\a boundary-matched test of biomass-change identifiability','Ecological assets behind improving accounts:\\\\national forest evidence and biomass-change identifiability')
 abstract=r'''Increasing productivity-weighted accounts need not identify ecological asset gains. We combine national account trajectories, source-specific mapped forest series, official inventory evidence and a boundary-matched biomass identification experiment. Of 183 eligible account identifiers in 2015--2023, 91 increase in total biocapacity; 68 of these have a decreasing forest account component, an accounting result rather than independent forest-loss evidence. Published mapped groups decline by 10.863, 0.703 and 3.303 million ha in Brazil, Indonesia and the Democratic Republic of the Congo, respectively, without calibrated change intervals. Annual transition constraints bound the Indonesian 2015-forest-to-2023-oil-palm cohort at 0.112--2.326 million ha, conditional on classifications, without equating repeated events with unique hectares. Official inventories yield conditional positive volume differences for Finnish and French campaign windows without assuming cross-inventory independence; Canada's earlier inventory-domain AGB change interval includes zero and its uncertainty representations require reconciliation. On the fixed 61,830 ha Brazilian footprint, the auxiliary whole-cell biomass point-map total increases by $\MapNet\times10^3$ Mg, while $\MapCancellation\%$ of absolute local differences cancels. Constructive allocations preserve every cell total and mapped fraction yet permit all four joint sign quadrants for nested cover groups. Native-cell mass information narrows identification sets by $\ReductionForm\%$ and $\ReductionSav\%$ relative to one-window totals but identifies neither sign; density-contrast restrictions identify sensitivity thresholds, not established ecological facts. None of eight candidates supplies the original calibrated national 2015--2023 forest-AGB comparison. The results establish national evidence and increments of identification while distinguishing mapped extent, inventory volume, biomass and uncertainty. They do not establish national ecological composition masking, conversion associations or independent reporting accuracy.'''
 t=re.sub(r'\\begin\{abstract\}.*?\\end\{abstract\}',lambda m:'\\begin{abstract}\n'+abstract+'\n\\end{abstract}',t,count=1,flags=re.S)
 start=t.index('The ecological hypothesis motivates');end=t.index('\\section{Materials and methods}')
 intro=r'''The ecological hypothesis motivates five linked measurement questions:
\begin{enumerate}
\item What national account trajectories and component sensitivities are observed, and how do they differ from source-specific physical forest quantities?
\item Within a matched local footprint, can an increasing whole-cell biomass point-map total rule out a decline in a separately defined mapped-cover group?
\item How do spatial aggregation, native-cell mass information and explicit density-contrast restrictions change group-change identification sets?
\item What unique endpoint cohorts are constrained by annual national class-transition tables, without treating repeated events as unique converted area?
\item What stock-change statements do official inventory designs and defensible dependence or bias bounds support on their actual periods and domains?
\end{enumerate}
The first question is answered by the national trajectories and typed source comparisons (Section~\ref{sec:nationalresults}); the second and third by constructive allocation, joint sets and information sensitivities; the fourth by the marked-flow bounds (Section~\ref{sec:flowresults}); and the fifth by the inventory results (Section~\ref{sec:inventoryresults}). The original calibrated national 2015--2023 forest-AGB target is retained separately. Neither nominal mapped discordance nor conditional inventory-volume change substitutes for it. Exact paired field censuses and known covariance are not imposed as universal prerequisites: compatible marginal inventory designs, direct change estimates or defensible dependence and bias bounds can also support an inference.

'''
 t=t[:start]+intro+t[end:]
 t=once(t,'\\subsection{External land-cover support}','\\input{src/national_methods_F13.tex}\n\n\\subsection{External land-cover support}')
 t=once(t,'\\subsection{Territorial and endpoint compatibility}','\\input{src/national_results_F13.tex}\n\n\\subsection{Primary AGB territorial and endpoint compatibility}')
 t=once(t,'No candidate has yet met all territorial, forest-support, complete-coverage and change-validation requirements for analytical admission.','No candidate has yet met all territorial, forest-support, complete-coverage and change-validation requirements for the original calibrated national 2015--2023 forest-AGB comparison. The mapped and inventory results above answer separately defined questions and are not excluded by this primary-target hold.')
 old='National forest-stock trends, account--asset divergence and conversion associations are not estimated.'
 new='Source-specific national mapped extent and conditional inventory-cycle stock results are now quantified, but calibrated national primary-period forest-AGB trends, independently supported account--asset divergence and conversion associations are not established.'
 t=once(t,old,new)
 t=once(t,'The public reference-point downloads inspected are labelled Collection 9; compatibility with Collection 11, sample reuse, design weights and transition-specific reference interpretation require assessment before change validation.',"The public older reference-point representations and the current Collection 11 assessment use different reference vintages; sample reuse, design weights, boundary exclusions and transition-specific interpretation require compatibility assessment before change validation.")
 anchor='\\section{Conclusions}'
 discussion=r'''National physical evidence should neither be erased by a primary-target hold nor promoted into a different estimand. Indonesia's improving total account and decreasing mapped forest are a concrete nominal discordance; Brazil and Congo retain decreasing accounts alongside their mapped declines. They do not constitute a representative sample or an independent reporting-accuracy evaluation. The oil-palm cohort bound adds information unavailable from annual event totals, but its transfer to ecological conversion requires class-set error control. The French longer inventory contrast also adds information unavailable from heavily overlapping recent cycles, while retrospective method bias remains explicit. Canadian direct-change reporting avoids an arbitrary endpoint-covariance assumption yet still requires scrutiny of projection, geography and inconsistent uncertainty representations.

A practical reporting sidecar should therefore show the aggregate account and its components, a separately defined physical extent or stock, its period and territory, an appropriate interval or feasible set, and conversion diagnostics distinguished from event counts. Improving information availability is not the same as demonstrating improved reporting accuracy. That latter claim needs independent physical outcomes on common cases. Nor can subnational units replicate a single national account change for an association test. The present analyses concern what the observations support; broader causal attribution requires a separate design.

'''
 t=once(t,anchor,discussion+anchor)
 start=t.index('\\section{Conclusions}')+len('\\section{Conclusions}');end=t.index('\\section*{Data and code availability}')
 conclusion=r'''
Actual national accounts show both increases and decreases, with frequent offsets among components. Three executed national mapped-cover series, conditional unique endpoint-cohort bounds and official inventory-cycle quantities add substantive empirical evidence. Their definitions, geographic domains, time operators and uncertainty remain distinct. Finnish and French volume increases are conditional sampling results, not national exact-endpoint AGB validation; the Canadian reported total-change interval is unresolved. In the fixed Brazilian footprint, increasing whole-cell point-map biomass coexists with offsetting local differences and both signs of cover-group change under coherent nonnegative allocations. Native-cell information narrows those sets without resolving either sign, while density-contrast boundaries specify testable auxiliary-information requirements. All eight primary calibrated national 2015--2023 forest-AGB comparisons remain open. The combined results establish observed account trajectories and specific gains and limits in physical identification, not measured national ecological composition masking. Compatible inventory designs, direct change estimates, reference-based marginal intervals and defensible dependence or bias bounds provide legitimate routes for the remaining ecological test.

'''
 t=t[:start]+conclusion+t[end:]
 t=t.replace('https://github.com/MIKEAA2020/general-sustainability/tree/main/batch%209/agent%202/ecomod_empirical_followup/F11_A01',URL)
 t=once(t,'Source datasets are cited in the text.','Source datasets are cited in the text. National account trajectories, mapped extent series, marked-flow capacities and certificates, inventory source cells, uncertainty diagnostics and the integrated numerical workbook accompany the local identification results. The deposit identifies the immutable earlier numerical dependencies and their original source hashes.')
 refs=r'''
\bibitem[MapBiomas Indonesia(2026)]{MapBiomasIDN2026} MapBiomas Indonesia (2026). Collection 4.1 and Collection 3 land-cover statistics; Algorithm Theoretical Basis Document, Collection 4.1. \url{https://landy.mapbiomas.id/en/statistics}. \url{https://landy.mapbiomas.id/en/atbd}.
\bibitem[MapBiomas DR Congo(2026)]{MapBiomasCOD2026} MapBiomas Project (2026). Collection 1 of the Annual Land Use and Land Cover Maps of the Democratic Republic of the Congo, national statistics, legend and ATBD v1. \url{https://rdc.mapbiomas.org/telechargements/statistiques/}. \url{https://rdc.mapbiomas.org/telechargements/atbd/}.
\bibitem[Korhonen et al.(2021)]{Korhonen2021} Korhonen, K. T., Ahola, A., et al. (2021). Forests of Finland 2014--2018 and their development 1921--2018. \emph{Silva Fennica}, 55, article 10662. Supplementary S2, Table 20a. \url{https://doi.org/10.14214/sf.10662}.
\bibitem[Korhonen et al.(2024)]{Korhonen2024} Korhonen, K. T., et al. (2024). Forests of Finland 2019--2023 and their development 1921--2023. \emph{Silva Fennica}, 58, article 24045. Supplementary S2, Table 55. \url{https://doi.org/10.14214/sf.24045}.
\bibitem[IGN(2018)]{IGN2018} IGN (2018). \emph{Le m\'emento, inventaire forestier, \ edition 2018}, pp. 28--29; and \emph{M\'ethodologie 2013--2017}, pp. 5, 9, 16--17. \url{https://inventaire-forestier.ign.fr/IMG/pdf/181127_memento_2018_v4.pdf}. \url{https://inventaire-forestier.ign.fr/IMG/pdf/181011_methodologie.pdf}.
\bibitem[IGN(2026)]{IGN2026} IGN (2026). \emph{R\'esultats nationaux}, standard production-forest volume tables, campaigns 2021--2025, with retained 2018--2022 and 2019--2023 editions. \url{https://inventaire-forestier.ign.fr/spip.php?rubrique250}. Historical publications: \url{https://inventaire-forestier.ign.fr/spip/spip.php?article709=}.
\bibitem[Canada's NFI(2025)]{CanadaNFI2025} Canada's National Forest Inventory (2025). \emph{First remeasurement and forest change estimates}, version 3.1, November 2025, Tables 17.0 and 17C.0 and associated relative-standard-error and interval tables. \url{https://nfi.nfis.org/en/resources}. General estimation procedures v1.13: \url{https://nfi.nfis.org/en/estimation}.
'''
 t=once(t,'\\end{thebibliography}',refs+'\n\\end{thebibliography}')
 (ROOT/'integrated_F13_A01_main.tex').write_text(t)
 si=rewrite_paths((SUPPORT/'templates/F11_SI.tex').read_text()).replace(OLD,TITLE)
 si=once(si,'The results supplied here are account availability counts, product definitions, territorial and observation-support screening, local mapped-cover endpoints and conditional biomass-allocation sets. No country-level physical stock changes, conversion associations, ecological change-resolution probabilities or reporting-rule accuracy estimates are supplied.', 'The local analyses supply account availability, product definitions, support screening, mapped-cover endpoints and conditional biomass-allocation sets. The additional national analyses below supply account trajectories, source-specific mapped extent, endpoint-cohort bounds and conditional inventory-cycle stock quantities. They do not supply calibrated primary national AGB changes, conversion associations, ecological change-resolution probabilities or independent reporting-rule accuracy estimates.')
 si=once(si,'\\section*{Source attribution and availability}','\\input{src/national_SI_F13.tex}\n\n\\section*{Source attribution and availability}')
 extra=r'''National extensions: MapBiomas Brazil Collection 11; MapBiomas Indonesia Collection 4.1 and Collection 3; MapBiomas DR Congo Collection 1, statistics, legend and ATBD; IGN national standard volume tables and 2018 historical national row; Canada's NFI Tables 17.0 and 17C.0 and associated interval/RSE tables; Finnish Luke APIs and the supplementary tables of Korhonen et al. (2021, 2024). Source URLs and SHA-256 identities accompany derived outputs. MapBiomas DR Congo data/code access and attribution are documented by its ATBD, p.~19. IGN factual numerical extractions are attributed to IGN; provider PDF bodies and raw workbooks are not redistributed. The numerical workbook preserves original table meanings and adds separate source and scope notes.

'''
 si=once(si,'National accounts: Lo, K., et al.',extra+'National accounts: Lo, K., et al.')
 # Keep explicit old F11 URLs for inherited files, and add the integrated package link.
 si=once(si,'\\section{Provider technical references}','Integrated manuscript, national tables, new analyses, source identities and dependency verification: \\url{'+URL+'}.\n\n\\section{Provider technical references}')
 (ROOT/'integrated_F13_A01_SI.tex').write_text(si)
 print(json.dumps(dict(main='integrated_F13_A01_main.tex',SI='integrated_F13_A01_SI.tex',one_publication=True,protected_packages_edited=False),indent=2))
if __name__=='__main__':build()

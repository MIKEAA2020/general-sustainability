#!/usr/bin/env python3
"""Deterministic content-based redistribution; protected deposits are read-only.
F13 inputs are frozen verbatim in inputs/. All revised text is assembled here.
"""
from pathlib import Path
import csv,json,re
ROOT=Path(__file__).resolve().parents[1]
URL='https://github.com/MIKEAA2020/general-sustainability/tree/main/batch%209/agent%202/ecomod_empirical_followup/F14_A01'
def require(ok,msg):
 if not ok:raise ValueError(msg)
def section(text,a,b):return text[text.index(a):text.index(b)]
def table(label,caption,headers,rows,spec):
 return '\\begin{table}[htbp]\n\\centering\\small\n\\caption{'+caption+'}\\label{'+label+'}\n\\begin{tabularx}{\\textwidth}{'+spec+'}\\toprule\n'+' & '.join(headers)+r'\\\midrule'+'\n'+'\n'.join(' & '.join(row)+r'\\'for row in rows)+'\n\\bottomrule\\end{tabularx}\n\\end{table}\n'
def figure(file,label,caption,width='1'):
 return '\\begin{figure}[htbp]\n\\centering\\includegraphics[width='+width+'\\textwidth]{'+file+'}\n\\caption{'+caption+'}\\label{'+label+'}\n\\end{figure}\n'
def build():
 old=(ROOT/'inputs/F13_main.tex').read_text();nat=(ROOT/'inputs/national_results_F13.tex').read_text()
 main=old[:old.index('\\section{Materials and methods}')]
 main=main.replace('\\graphicspath{{paper_support/results/}{paper_support/inherited_F10/results/}}','\\graphicspath{{figures/}{paper_support/results/}{paper_support/inherited_F10/results/}}\n\\input{src/SI_reference_numbers_F14.tex}')
 methods=r'''\section{Materials and methods}
\subsection{Accounts, physical quantities and comparison domains}
The National Ecological Footprint and Biocapacity Accounts, Edition 2026, results and metadata v1.0, supply annual biocapacity in global hectares (gha) \citep{Lo2026}. We require complete 2015--2023 records, admissible publication flags, finite nonnegative components, positive population and component-sum consistency. Of 236 country/territory identifiers, 183 satisfy these account criteria; physical-data eligibility is assessed separately (Supplementary Figure~\SIref{fig:SI_coverage} and Table~\SIref{tab:countries}). We calculate endpoint changes, component contributions, exclusions of fishing and built land, and separately labelled per-person changes. The 2010--2020 account sensitivity includes 182 members of the primary cohort. Full sensitivities appear in Supplementary Table~\SIref{tab:SI_account_sensitivity}.

The eight physical candidates are an exploratory logistical set, not a representative or outcome-naive sample. Acquisition continued with account directions and earlier results known. We retain all eight, including concordant, discordant and unexecuted cases. Complete MapBiomas national tables supply source-specific mapped extent for Brazil Collection 11, Indonesia Collection 4.1 and DR Congo Collection 1 \citep{MapBiomas2026,MapBiomasIDN2026,MapBiomasCOD2026}. Brazilian formations comprise classes 3, 5, 6 and 49; the distinct formations-plus-savanna group adds 4 and 7. Indonesian forest comprises 3, 5 and 76; Congolese source forest comprises 3, 4 and 5. Plantations are separate. These groups are not a harmonized forest definition. Leaf classes are summed once; Brazilian and Indonesian annual transition margins are reconciled to extent. Congo's country series is used rather than forcing nonclosing subunit totals into a partition. Source definitions and support sensitivities are documented in Supplementary Figure~\SIref{fig:SI_Indonesia} and Table~\SIref{tab:SI_class_support}.

\subsection{Matched support and conditional biomass allocation}
The geometry-selected Brazilian rectangle contains 65,536 native ESA CCI Biomass v7.0 cells covering 61,830.34 ha. Both biomass and MapBiomas endpoints are 2015 and 2023; the footprint is fixed, not chosen by observed change. Native biomass density refers to a whole pixel, not its forest part \citep{SantoroCartus2026,PUG2026}. WGS84 overlap areas map finer cover fractions to that support; missing support is not renormalized away. Product/quality definitions, boundary screening, native access diagnostics and stored-SD diagnostics are given in Supplementary Tables~\SIref{tab:products}--\SIref{tab:quality} and \SIref{tab:domain}, \SIref{tab:nativecoverage} and \SIref{tab:native_sd}; local cover endpoints are in Table~\SIref{tab:brazil_cover}.

Let $q_{it}=A_i\widehat d_{it}$ denote observed full-cell mass. Knowing a group's area fraction does not allocate $q_{it}$ within a mixed cell. Holding point maps and cover exact, we allow nonnegative component masses without finite density caps or temporal coupling. Cells entirely in group $g$ anchor its lower mass bound; every cell intersecting $g$ contributes to its upper bound:
\begin{equation}
\widehat{\mathcal I}_t^g=\left[\sum_{i\in P_t^g}q_{it},\ \sum_{i\in H_t^g}q_{it}\right].\label{eq:allocationmain}
\end{equation}
Endpoint subtraction gives the compatible difference range. All cells, including zeros and mixed/changing cover, remain included. A coherent three-component allocation defines the joint set for formations, added savanna and complement. These are identification sets conditional on observations, not confidence intervals for true forest change.

We compare nested block observations on the identical footprint: coarser blocks preserve mass but remove internal information. Positive and negative local differences quantify arithmetic cancellation, not biological gross turnover. A separate sensitivity bounds the ratio of component densities within each mixed cell by an assumed $R\ge1$; $R=1$ imposes homogeneous allocation and $R\to\infty$ recovers the unrestricted model. No finite $R$ is calibrated here. Observed zeros are retained; zero AGB or stored SD does not certify ecological absence or zero true error. Proofs, reconstructed witnesses, full width comparisons and contrast grids are supplied in the SI, including Tables~\SIref{tab:frontier} and \SIref{tab:contrast}.

\subsection{Endpoint cohorts from annual transition capacities}
Annual transitions count events and may count a hectare repeatedly. We instead mark the land mapped as forest in 2015 and follow its feasible flow through annual class-to-class capacities. Marked flow is bounded by each observed transition and conserved at interior class--year nodes. Minimizing and maximizing its final inflow into a 2023 destination bounds a unique endpoint cohort, allowing intermediate classes. The bounds are sharp for the balanced continuous-area capacity model, not reconstructions of actual histories. We evaluate national and fixed fine-geography networks; geographical restrictions prevent rearrangement across 49 Brazilian units or 38 Indonesian provinces. All 634 saved primal/dual certificates were independently verified. Outward numerical allowances are not classification-error intervals. Supplementary Table~\SIref{tab:SI_conversion_exact} gives all seven fine-geography ranges; the SI provides the model and proof.

For endpoint net-area errors bounded by $e$, change error is bounded by $2e$. Conversion requires a different error control: if initial-forest and final-destination class sets have combined symmetric-difference area at most $E$, a mapped lower cohort bound $L$ transfers only as $\max(0,L-E)$. Small net-area error does not imply small class-set error.

\subsection{Inventory periods, sampling uncertainty and measurement error}
Finnish NFI12 (2014--2018) and NFI13 (2019--2023) supply growing-stock volume and biomass components for productive and poorly productive forest, including \AA land \citep{Korhonen2021,Korhonen2024}. French tables supply living stem volume on metropolitan production forest including Corsica, across four pooled campaign windows \citep{IGN2018,IGN2026}. Inventory-cycle centres are not exact annual endpoints; stem volume is not AGB. Canadian NFI v3.1 supplies earlier-domain AGB stock and annualized change using remeasured 2007--2017 and projected 2006--2017 observations \citep{CanadaNFI2025}.

For approximately normal marginal inventory estimators, Bonferroni endpoint intervals give
\begin{equation}
\Delta\widehat V\ \pm\ z_{0.9875}(s_0+s_1),\qquad z_{0.9875}=2.241403,\label{eq:invbonf}
\end{equation}
with approximate 95\% sampling coverage without assuming cross-inventory independence. We retain a separate Finnish second-moment sensitivity conditional on unbiased errors and reported standard errors representing true error standard deviations; exact coverage is not asserted for estimated variances. For French reported 95\% endpoint halfwidths, direct subtraction guarantees at least 90\% contrast coverage; approximate 95\% rescaling additionally assumes marginal normality. Source rounding is included outward. Neither calculation covers an unbounded differential systematic bias. Canadian provider intervals are retained without inferring precision from the inconsistent RSE representation. Full source cells, comparisons and Canadian components are given in Supplementary Tables~\SIref{tab:SI_inventory_cells}--\SIref{tab:SI_Canada_components}.

Stock validation is not change validation: spatial and temporal dependence, reference error, forest allocation, converted land and differential bias require separate assessment \citep{Olofsson2014,E3UB2025,PVIR2026}. Public local reference artifacts do not supply compatible paired-endpoint validation here; their counts, source compatibility and biomass-reference eligibility are documented in Supplementary Table~\SIref{tab:reference_coverage} and the associated SI protocols. Exact paired censuses and known covariance are not universal prerequisites: compatible designs, direct change estimates and defensible dependence/bias bounds can suffice.

'''
 main+=methods+'\\section{Results}\n'
 national=section(nat,'\\subsection{National account trajectories','\\subsection{Unique mapped endpoint cohorts')
 # Replace the narrow F13 overview with an explicit, typed physical-evidence summary.
 start=national.index('\\begin{table}');end=national.index('\\end{table}',start)+len('\\end{table}')
 rows=[['Brazil','$-1.21/-3.15$','Mapped formations: $-10.863$ Mha ($-2.64\\%$), 2015--2023. No calibrated change interval.'],['Indonesia','$+5.46/-5.92$','Mapped forest: $-0.703$ Mha ($-0.66\\%$), 2015--2023. No calibrated change interval.'],['DR Congo','$-2.91/-7.64$','Source mapped forest: $-3.303$ Mha ($-2.01\\%$), 2015--2023. No calibrated change interval.'],['Cameroon','$+0.54/-3.16$','No completed physical numerical module.'],['Canada','$+0.08/-1.10$','Earlier inventory-domain AGB: $+17.639$ Mt/year; labelled range $[-21.279,56.557]$. Not 2015--2023.'],['Finland','$-1.60/-1.01$','Cycle volume: $+76.772$ million m$^3$, 2014--2018 to 2019--2023. Conditional sampling result.'],['France','$-4.47/+2.91$','Production-forest volume: $+200$ million m$^3$, 2013--2017 to 2021--2025. Method bias not bounded.'],['Australia','$+12.95/-0.33$','No completed physical numerical module.']]
 overview=table('tab:nationalcases','National account changes and separately typed physical evidence. Account columns are percentage changes in gha; mapped extent, volume and biomass are not interchangeable. None completes a calibrated national 2015--2023 forest-AGB comparison. Inventory periods and domains differ.',['Country','Total/forest account (\\%)','Physical evidence and qualification'],rows,'lp{2.7cm}X')
 national=national[:start]+figure('account_composition_F14.pdf','fig:accounts','Account composition across all eight exploratory candidates, 2015--2023. Both series are accounting quantities, not independent observations of ecological stock. Full account-domain and per-person sensitivities appear in Supplementary Table~\\SIref{tab:SI_account_sensitivity}. Data: Lo et al. (2026); derived account values retain CC BY-SA 4.0.')+overview+national[end:]
 national=national.replace('The Indonesian earlier-collection forest decline is 3.106 million ha, but its footprint is 43,130 ha larger; the collection-and-support sensitivity is substantial.','The Indonesian earlier-collection forest decline is 3.106 million ha, but its footprint is 43,130 ha larger; the collection-and-support sensitivity is substantial (Supplementary Figure~\\SIref{fig:SI_Indonesia}).')
 national=national.replace('Domain choice matters:', 'Figure~\\ref{fig:accounts} displays the eight candidate trajectories. Domain choice matters:')
 main+=national
 # Local map and essential allocation result; specialist diagnostic subsections remain in SI.
 local=section(old,'\\subsection{Mapped cover on a common Brazilian support}','\\subsection{Reference coverage and compatibility}')
 cover=re.search(r'\\begin\{table\}.*?\\end\{table\}',local,re.S).group(0)
 (ROOT/'src/local_cover_table_SI_F14.tex').write_text(cover+'\n')
 local=local.replace(cover,'').replace('Table~\\ref{tab:brazil_cover}','Supplementary Table~\\SIref{tab:brazil_cover}')
 local=local.replace('\\subsection{Mapped cover on a common Brazilian support}','\\subsection{A common local support does not identify the forest-group trend}')
 local=local.replace('The fixed footprint has area', 'Figure~\\ref{fig:brazil_support} shows the mapped fractions on the matched grid. The fixed footprint has area')
 main+=local
 main+=section(old,'\\subsection{Conditional biomass-allocation sets}','\\input{paper_support/src/results_addition_F11.tex}').replace('\\subsection{Conditional biomass-allocation sets}', '\\paragraph{Conditional allocation ranges.}')
 added=(ROOT/'paper_support/src/results_addition_F11.tex').read_text()
 added=added.replace('\\input{paper_support/results/frontier_table_F11.tex}','')
 added=added.replace('Table~\\ref{tab:frontier}','Supplementary Table~\\SIref{tab:frontier}')
 added=added.replace('\\subsection{Offsetting point-map differences on matched support}', '\\paragraph{Offsetting point-map differences.}').replace('\\subsection{Constructive sign ambiguity and information increments}', '\\paragraph{Coherent sign ambiguity.}').replace('The one-window information set has', '\\subsection{Information increments and assumption-dependent signs}\nThe one-window information set has').replace('\\subsection{Allocation restrictions required for a positive sign}', '\\paragraph{Restrictions required for a positive sign.}')
 main+=added
 flows=section(nat,'\\subsection{Unique mapped endpoint cohorts','\\subsection{Inventory evidence')
 flows+=figure('endpoint_cohorts_F14.pdf','fig:flows','Unique mapped 2015-forest-to-2023-destination cohort ranges under fine-geography transition capacities. Panels have different horizontal scales. F denotes each source forest/formation group; F+S adds Brazilian savannas. Numerical endpoints are in million ha; all include outward numerical allowances. These are feasible ranges, not confidence intervals, direct clearing events or calibrated ecological conversion. Supplementary Table~\\SIref{tab:SI_conversion_exact} gives exact values.')
 flows=flows.replace('Brazilian formations have', 'Figure~\\ref{fig:flows} summarizes all seven endpoint-cohort ranges. Brazilian formations have')
 main+=flows
 inventory=nat[nat.index('\\subsection{Inventory evidence'):]
 inventory=inventory.replace('Component point changes are $-16.158$ (coniferous), $-16.115$ (mixedwood), $+43.065$ (broadleaf) and $+6.847$ (non-treed) Mt/year; they concern changing class-defined stocks, not tracked biological cohorts or a decomposition of causal growth. All component intervals are retained in the data.','Subtype estimates concern contemporaneous class-defined stocks, not tracked biological cohorts; the complete component intervals are retained in Supplementary Table~\\SIref{tab:SI_Canada_components}.')
 inventory+=figure('inventory_uncertainty_F14.pdf','fig:inventories','Inventory evidence on distinct periods and domains, not a pooled comparison. (a) Finnish cycle-volume difference: the approximate marginal-normal 95\\% sampling band is positive; a second-moment sensitivity includes zero. (b) French longest cycle contrast: direct marginal-interval subtraction gives at least 90\\% sampling coverage; the separate approximate 95\\% band assumes marginal normality. Both exclude unbounded differential method bias. (c) Canadian earlier-domain annualized AGB change: the provider-labelled interval includes zero; its confidence level is not independently certified. Canadian RSE, projection and northern-coverage issues remain explicit. Units and horizontal scales differ.')
 inventory=inventory.replace('Finnish NFI12 and NFI13', 'Figure~\\ref{fig:inventories} separates the inventory quantities, periods and uncertainty constructions. Finnish NFI12 and NFI13')
 main+=inventory
 main+=r'''\paragraph{Scope of the national biomass comparison.}
None of the eight calibrated national 2015--2023 forest-AGB analyses is complete. Mapped extent is not forest biomass, pooled volume is not an annual AGB endpoint, and a regional or earlier-domain inventory is not a national target-period observation. Canada's omitted northern geography is not assigned zero biomass. French method comparability and Finnish biomass precision require evidence distinct from the reported volume intervals. Australia and Cameroon remain unexecuted physical modules, not demonstrated cases of permanent data unavailability. Completion is distinct from sign resolution: a valid calibrated comparison could include zero. The conditional results above are retained on their actual estimands rather than excluded or promoted to a different target.

'''
 tail=old[old.index('\\section{Discussion}'):]
 tail=tail.replace('All eight primary calibrated national 2015--2023 forest-AGB comparisons remain open.','All eight primary calibrated national 2015--2023 forest-AGB analyses remain incomplete; this is not a count of completed negative or inconclusive findings.')
 tail=tail.replace('/F13_A01','/F14_A01')
 tail=tail.replace('The deposit identifies the immutable earlier numerical dependencies and their original source hashes.','The deposit identifies the immutable earlier numerical dependencies and their original source hashes. Supplementary Information provides source definitions, analytical derivations and exact supporting tables; machine-readable results and computational code are supplied in the deposit.')
 main+=tail
 # SI retains scientific protocols and exact supporting data, not a second results/discussion story.
 si=(ROOT/'inputs/F13_SI.tex').read_text()
 si=si.replace('\\usepackage{amsmath,amssymb,booktabs,tabularx,array,longtable}','\\usepackage{amsmath,amssymb,booktabs,tabularx,array,longtable,graphicx}\n\\renewcommand{\\thefigure}{S\\arabic{figure}}\n\\graphicspath{{figures/}{paper_support/results/}{paper_support/inherited_F10/results/}}')
 si=si.replace('/F13_A01','/F14_A01')
 # Correct hard-coded section numbers after redistribution; use semantic locations instead.
 si=si.replace('criteria in S1','criteria in this section')
 marker='\\section{Biomass products, units and spatial support}'
 sensitivity_rows=[]
 rr=list(csv.DictReader((ROOT/'data/accounts_candidate_changes_F12.csv').open()))
 for code in ['BRA','IDN','COD','CMR','CAN','FIN','FRA','AUS']:
  vals=[]
  for domain in ['total','terrestrial_excluding_fishing','excluding_built','terrestrial_excluding_built','forest_component','per_person_total']:
   value=next(float(r['percent_change'])for r in rr if r['ISO3']==code and r['domain']==domain and r['start']=='2015'and r['end']=='2023');vals.append(f'{value:+.2f}')
  sensitivity_rows.append([code]+vals)
 sensitivities=table('tab:SI_account_sensitivity','Complete eight-country account-domain sensitivity, 2015--2023 (percentage change). Fishing/built exclusions remain gha quantities; per person is a different denominator. No column is independently observed physical forest change.',['ISO','Total','No fishing','No built','Neither','Forest','Per person'],sensitivity_rows,'lrrrrrr')
 si=si.replace(marker,figure('paper_support/inherited_F10/results/account_coverage_F06.pdf','fig:SI_coverage','Regional availability of national accounts under the primary eligibility rules. This describes account availability, not physical-data availability or ecological condition. The original separate-row and wrapped-label layout is preserved. Data: Lo et al. (2026); CC BY-SA 4.0.')+sensitivities+'\n'+marker)
 # Add the relocated local endpoint and width tables next to the matching protocols.
 si=si.replace('\\section{Brazilian mapped-cover fractions and observation operators}',cover+'\n\\section{Brazilian mapped-cover fractions and observation operators}')
 si=si.replace('\\input{paper_support/src/SI_addition_F11.tex}','\\input{src/identification_protocols_SI_F14.tex}\n\\input{paper_support/results/frontier_table_F11.tex}')
 specialist=(ROOT/'paper_support/src/SI_addition_F11.tex').read_text().split('\\section{Subsequent ecological comparisons')[0]
 (ROOT/'src/identification_protocols_SI_F14.tex').write_text(specialist)
 ns=(ROOT/'inputs/national_SI_F13.tex').read_text()
 # Main owns the conclusions and unfinished-target account; SI ends with supporting reference protocols.
 ns=ns.split('\\section{Primary national AGB target and remaining evidence requirements}')[0]
 ns=ns.replace('\\section{Reference compatibility and limits on ecological claims}','\\section{Reference compatibility protocols}')
 ns=ns[:ns.index('No conversion association, causal effect or independent reporting-rule accuracy is estimated.')]
 ns=re.sub(r'The 2023 timber forest account has.*?proof of observed ecological loss\.', '', ns, flags=re.S)
 ns=ns.replace('\\section{National trajectories, source tables and comparison domains}','\\section{National trajectory and source-support specifications}')
 # Promote existing unnumbered supporting tables to properly captioned, linked SI tables.
 idx=ns.index('\\begin{center}');end=ns.index('\\end{center}',idx)+len('\\end{center}')
 raw=ns[idx:end];ns=ns[:idx]+raw.replace('\\begin{center}\\small','\\begin{table}[htbp]\\centering\\small\n\\caption{Exact fine-geography endpoint-cohort ranges in million ha. Entries correspond to main Figure~5 and retain the outward numerical allowances. These are feasible mapped ranges, not confidence intervals.}\\label{tab:SI_conversion_exact}').replace('\\end{center}','\\end{table}')+ns[end:]
 # Avoid precision loss in the seven-row table by regenerating from pinned CSV.
 m=re.search(r'\\begin\{table\}.*?\\label\{tab:SI_conversion_exact\}.*?\\end\{table\}',ns,re.S)
 rows=[]
 for r in csv.DictReader((ROOT/'data/endpoint_conversion_path_bounds_F12.csv').open()):
  if r['constraint_level']=='finest_reported_geography':rows.append([r['country'],r['initial_group'].replace('_',' '),r['final_target'].replace('_',' '),f"{float(r['lower_unique_endpoint_area_ha'])/1e6:.9f}",f"{float(r['upper_unique_endpoint_area_ha'])/1e6:.9f}"])
 ns=ns[:m.start()]+table('tab:SI_conversion_exact','Exact fine-geography endpoint-cohort ranges (million ha), corresponding to main Figure 5. Values include outward numerical allowances; they are feasible mapped ranges, not confidence intervals.',['Country','Initial group','2023 target','Lower','Upper'],rows,'lllrr')+ns[m.end():]
 # French source windows table and Canadian component table already exist; add captions and labels.
 centers=list(re.finditer(r'\\begin\{center\}.*?\\end\{center\}',ns,re.S))
 for m,label,caption in reversed(list(zip(centers,['tab:SI_France_windows','tab:SI_Canada_components'],['French published national volume estimates and 95\\% marginal halfwidths. Campaign windows are pooled observations, not exact annual endpoints.','Canadian annualized change by contemporaneous forest type, with provider-labelled halfwidths. No confidence level is assigned here; components are not fixed biological cohorts.']))):
  raw=m.group(0).replace('\\begin{center}\\small','\\begin{table}[htbp]\\centering\\small\n\\caption{'+caption+'}\\label{'+label+'}').replace('\\end{center}','\\end{table}');ns=ns[:m.start()]+raw+ns[m.end():]
 # A compact explicit inventory source-cell table supports the two published Finnish source cells.
 cells=[]
 for r in csv.DictReader((ROOT/'data/FIN_inventory_volume_SE_source_cells_F12.csv').open()):cells.append([r['inventory'],r['volume_million_m3'],r['SE_million_m3'],r['sheet'],r['volume_cell']+'/'+r['SE_cell']])
 ns=ns.replace('\\section{Inventory source cells, period operators and dependence bounds}',table('tab:SI_inventory_cells','Finnish inventory source cells and reported volume standard errors. Units are million m$^3$ after conversion from the source thousand-m$^3$ cells; source identities are pinned in the numerical dependency.',['Inventory','Volume','SE','Sheet','Cells'],cells,'lrrll')+'\n\\section{Inventory source cells, period operators and dependence bounds}')
 # Class/support summary and source sensitivity are verification companions, not new results.
 support=table('tab:SI_class_support','Source-specific class groups and geographic support checks. Numeric class codes are initiative-specific. Footprint differences are not geometry symmetric differences.',['Source','Mapped group','Support qualification'],[['Brazil C11','3, 5, 6, 49; plus 4, 7 only for F+S','850.645 million ha; annual margins reconciled.'],['Indonesia C4.1','3, 5, 76; oil palm 35 separate','189.044 million ha; C3 footprint 43,130.051 ha larger.'],['DR Congo C1','3, 4, 5; plantation 9 separate','Country footprint 231.405 million ha; province/biome totals not forced into a partition.']],'lp{4.0cm}X')
 ns=ns.replace('\\section{Sharp endpoint-cohort bounds',figure('Indonesia_definition_support_SI.png','fig:SI_Indonesia','Indonesia definition and collection/support sensitivity, 2015--2023. Left: changes in source forest subclasses and their union. Right: C3 versus C4.1 mapped forest changes; differing support prevents interpretation as a pure collection effect or confidence interval. Main national results summarize this sensitivity. Source: MapBiomas Indonesia; original numerical figure retained.')+support+'\n\\section{Sharp endpoint-cohort bounds')
 # Exact French sensitivity table, all three comparisons and all confidence constructions.
 fr=[]
 for r in csv.DictReader((ROOT/'data/FRA_volume_change_bounds_F13.csv').open()):
  mode='90\\% union'if r['mode']=='union90'else'95\\% normal, '+r['endpoint_family']+' ends'
  fr.append([r['initial_cycle'].replace('-','--'),mode,r['delta_Mm3'].split('.')[0],f"{float(r['lower_Mm3']):.6f}",f"{float(r['upper_Mm3']):.6f}"])
 ns+=table('tab:SI_France_contrasts','All French earlier-to-2021--2025 volume contrasts (million m$^3$), including full-unit rounding. Normal rows are approximate and conditional on marginal normality. An unbounded differential-method bias is not covered.',['Initial cycle','Construction','Difference','Lower','Upper'],fr,'llrrr')
 (ROOT/'src/national_protocols_SI_F14.tex').write_text(ns)
 si=si.replace('\\input{src/national_SI_F13.tex}','\\input{src/national_protocols_SI_F14.tex}')
 # SI has no new standalone result/discussion section. Add explicit main links for all captioned items below.
 main=main.replace('Full source cells, comparisons and Canadian components are given in Supplementary Tables~\\SIref{tab:SI_inventory_cells}--\\SIref{tab:SI_Canada_components}.','Finnish source cells are given in Supplementary Table~\\SIref{tab:SI_inventory_cells}; French windows and all contrasts in Tables~\\SIref{tab:SI_France_windows} and \\SIref{tab:SI_France_contrasts}; Canadian components in Table~\\SIref{tab:SI_Canada_components}.')
 main=main.replace('Biomass fields and reference eligibility are documented','Biomass fields and reference eligibility are documented')
 main=main.replace('None of eight candidates supplies','None of eight candidates supplies')
 # Cross-document numbers are generated from the SI aux by build_F14.py, never guessed.
 (ROOT/'integrated_F14_A01_main.tex').write_text(main)
 (ROOT/'integrated_F14_A01_SI.tex').write_text(si)
 if not(ROOT/'src/SI_reference_numbers_F14.tex').exists():
  (ROOT/'src/SI_reference_numbers_F14.tex').write_text('\\newcommand{\\SIref}[1]{\\ifcsname SIlabel:#1\\endcsname\\csname SIlabel:#1\\endcsname\\else ??\\fi}\n')
 print('Assembled F14 main and SI; six main figures and two main tables.')
if __name__=='__main__':build()

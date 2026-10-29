from pathlib import Path
import shutil,json,hashlib,difflib
B=Path('/home/user/ecomod_followup_F08');P=Path('/home/user/ecomod_followup_F09');assert not P.exists()
shutil.copytree(B,P,ignore=shutil.ignore_patterns('.cache','__pycache__','artifact_manifest.json','followup_F08_main.pdf','followup_F08_SI.pdf'))
for part in ['main','SI']:
 (P/f'followup_F08_{part}.tex').rename(P/f'followup_F09_{part}.tex')
(P/'README.md').rename(P/'README_inherited_F08.md')
(P/'REMAINING_EMPIRICAL_WORK.md').rename(P/'REMAINING_EMPIRICAL_WORK_inherited_F08.md')
(P/'src/build.sh').rename(P/'src/build_F09.sh');p=P/'src/build_F09.sh';p.write_text(p.read_text().replace('followup_F08_','followup_F09_'))
p=P/'tests/test_xlsx_f08.py';s=p.read_text().replace("f'followup_F08_","f'followup_F09_").replace("'followup_F08_main.tex'","'followup_F09_main.tex'");p.unlink();(P/'tests/test_xlsx_F09.py').write_text(s)
main=P/'followup_F09_main.tex';s=main.read_text()
old='Scientific interpretation additionally used the Product User Guide and the published change-processing implementation \\citep{PUG2026}.'
new='Product definitions and uncertainty interpretation follow the Product User Guide, Algorithm Theoretical Basis Document, end-to-end uncertainty budget and validation report \\citep{PUG2026,ATBD2025,E3UB2025,PVIR2026}.'
assert old in s;s=s.replace(old,new)
anchor='Eight countries were selected for evaluation'
insert=r'''The observation system combines C- and L-band radar retrievals with structural calibration and land-cover-dependent processing. The C-band branch is generated at 150 m spacing and resampled to the 100 m L-band grid. Interannual refinement of merging weights, including land-cover-specific exceptions, improves consistency but does not establish independent endpoint errors or independent 100 m observations. Land-cover information affects calibration, masking of selected classes and merging decisions; the product does not impose a universal forest mask over vegetated land. Published zero estimates are retained separately from missing observations without interpreting them as independent evidence of absent woody vegetation \citep[pp.~57--59, 82--83, 87, 91, 95, 101--102]{ATBD2025}.

'''
assert anchor in s;s=s.replace(anchor,insert+anchor)
anchor='Reporting comparisons require common cases and weights'
insert=r'''CCI's uncertainty model already propagates correlated retrieval errors within annual image stacks and spatially correlated errors in aggregated products. Those terms must be distinguished from cross-year covariance of the final maps. In particular, the L-band within-stack correlation assumption of 0.5 is not an estimate of correlation between the 2015 and 2023 endpoint errors. The uncertainty budget's change-variance expression sums endpoint variances without a cross-year term; this omission does not establish that the true covariance is zero \citep[pp.~14--22, 23--28]{E3UB2025}. Change inference on fixed support requires the joint endpoint covariance structure and the difference of systematic endpoint errors. Uncertainty in forest classification, mixed-cell allocation and observation support remains separate.

'''
assert anchor in s;s=s.replace(anchor,insert+anchor)
anchor=r'\subsection{Conditional biomass-allocation sets}'
insert=r'''CCI's v7 stock validation includes the primary endpoint years and uses plot and LiDAR reference data reported as withheld from map production \citep[pp.~11--14]{PVIR2026}. Reference preparation includes growth-rate adjustment for temporal mismatches of up to ten years and forest-fraction harmonization of small plots \citep[p.~18]{PVIR2026}. These stock comparisons provide relevant evidence about the observation system, but epoch-specific reference counts are not counts of paired change observations. The reported standard-error layer represents random error; the variance-consistency diagnostic does not estimate confidence-interval coverage for the local forest-stock difference \citep[p.~19]{PVIR2026}.

'''
assert anchor in s;s=s.replace(anchor,insert+anchor)
anchor=r'\section{Conclusions}'
insert=r'''The provider validation and the present identification limits address different questions. A held-out stock comparison can assess map agreement on its reference support without identifying forest-specific biomass inside a mixed cell or calibrating a paired 2015--2023 change on the present footprint. The described validation screening excludes plots deforested between inventory and map dates, and temporal harmonization uses growth assumptions; transferring its error characteristics to converted land requires evidence beyond agreement among retained forest observations \citep[pp.~13, 18--19]{PVIR2026}. Reference measurement error, geolocation and within-pixel sampling also contribute to map--reference discrepancies. Accordingly, neither RMSD nor a globally pooled bias pattern is adopted as a local change-error model, and the absence of such a model here is not a claim that the v7 stock product lacks validation.

'''
assert anchor in s;s=s.replace(anchor,insert+anchor)
s=s.replace('ecomod_empirical_followup/F08}', 'ecomod_empirical_followup/F09}')
s=s.replace('Raw country land-cover images, biomass files and the Product User Guide are not redistributed.', 'Raw country land-cover images, biomass files and provider technical reports are not redistributed.')
refs=r'''\bibitem[CCI Biomass(2025a)]{ATBD2025} CCI Biomass (2025a). \emph{Algorithm Theoretical Basis Document, v7.0}. 17 December 2025. \url{https://climate.esa.int/media/documents/Algorithm_Theoretical_Basis_Document_ATBD_V7.0.pdf}.
\bibitem[CCI Biomass(2025b)]{E3UB2025} CCI Biomass (2025b). \emph{End to End ECV Uncertainty Budget, v7.0}. 17 December 2025. \url{https://climate.esa.int/documents/3354/End-to-End_ECV_Uncertainty_Budget_E3B_V7.0.pdf}.
\bibitem[CCI Biomass(2026b)]{PVIR2026} CCI Biomass (2026b). \emph{Product Validation and Intercomparison Report, v7.0}. 24 April 2026. \url{https://climate.esa.int/documents/3356/Product_Validation_Intercomparison_Report_PVIR_V7.0.pdf}.
'''
s=s.replace(r'\begin{thebibliography}{9}',r'\begin{thebibliography}{99}').replace(r'\end{thebibliography}',refs+r'\end{thebibliography}')
main.write_text(s)
p=P/'followup_F09_SI.tex';s=p.read_text()
anchor=r'\section{Geographic area calculation}'
insert=r'''\subsection{Spatial averages, endpoint dependence and systematic error}
For a density average $\widehat{\bar d}=\sum_i w_i\widehat d_i$ with fixed weights satisfying $\sum_i w_i=1$, the random-error variance is
\begin{equation}
\operatorname{Var}(\widehat{\bar d})=\boldsymbol w^{\mathsf T}\Sigma\boldsymbol w.
\end{equation}
For equal weights this is $N^{-2}\sum_i\sum_j\Sigma_{ij}$, reducing to $N^{-2}\sum_i\sigma_i^2$ under independence. An area-weighted mass total instead uses weights $a_i$ in hectares and has variance in Mg$^2$. Average and total normalization cannot be interchanged. The validation plan gives the equal-weight $N^{-2}$ covariance sum (PVP v6, p.~26).

Write each endpoint density vector as $\widehat{\boldsymbol d}_t=\boldsymbol d_t+\boldsymbol b_t+\boldsymbol\varepsilon_t$, where $\boldsymbol b_t$ is systematic error and $E(\boldsymbol\varepsilon_t)=0$. On common fixed support, the estimation error of the mass difference is
\begin{equation}
\widehat{\Delta Q}-\Delta Q=\boldsymbol a^{\mathsf T}(\boldsymbol b_1-\boldsymbol b_0)+\boldsymbol a^{\mathsf T}(\boldsymbol\varepsilon_1-\boldsymbol\varepsilon_0).
\end{equation}
With $\Sigma_{st}=\operatorname{Cov}(\boldsymbol\varepsilon_s,\boldsymbol\varepsilon_t)$, its random-error variance, conditional on the support and systematic terms, is
\begin{equation}
\operatorname{Var}(\widehat{\Delta Q})=\boldsymbol a^{\mathsf T}(\Sigma_{11}+\Sigma_{00}-\Sigma_{10}-\Sigma_{01})\boldsymbol a.
\end{equation}
This identity neither removes systematic error nor represents uncertain classification, within-cell allocation, missingness or support changes. The cross-year matrices must be compatible with a valid joint covariance structure. Positive or negative endpoint dependence can respectively reduce or increase random difference variance; neither direction is assigned without evidence.

The uncertainty budget describes within-stack retrieval covariance for C-band and L-band observations (E3UB v7, pp.~14--22), followed by a spatial error-correlation model fitted across 142 one-degree cells from eight regional reference datasets (pp.~23--26). It explicitly notes that these data are not representative of global forests and treats the model as a plausible assumption. The within-stack L-band correlation of 0.5 and the spatial ensemble coefficient are not estimates of the final-map 2015--2023 error covariance for this footprint. Existing propagated components must not be counted twice. The change-variance expression on p.~28 omits cross-year covariance and introduces additional bias-correction uncertainty only if such a correction is applied at the bias-map scale. No local covariance, bias correction or calibrated coverage is inferred from those expressions.

'''
assert anchor in s;s=s.replace(anchor,insert+anchor)
anchor='Practical-change and classification thresholds require calibration'
insert=r'''The v7 Product Validation and Intercomparison Report describes independent stock comparisons through 2024 and states that its plot and LiDAR reference data were withheld from production (PVIR v7, pp.~11--14). The reference preparation permits growth-rate adjustment over temporal offsets of up to ten years and applies a forest-fraction correction to small plots (p.~18). Its documented screening includes exclusion of plots deforested between inventory and map dates (p.~13). These are relevant response-design and selection conditions, not direct repeated observations of the present local 2015--2023 forest-stock difference. The reported random-error variance diagnostic omits positional, within-pixel representation and harmonization components; it is not a coverage estimate for a nominal confidence level (p.~19). The report's within-pixel sampling examples show that apparent low- and high-biomass bin biases can arise even when the underlying pixel means are correctly specified (pp.~96--98). Such discrepancies cannot be assigned wholly to map error.

The validation plan identifies repeated NFI and LiDAR observations as potential change references (PVP v6, pp.~17--18, 42), but their dates, uncertainty and availability differ. Its appendix lists a Brazilian LiDAR candidate for 2011--2018 while the accompanying account of the currently retained change-reference data does not include Brazil. Candidate identification therefore does not establish an available, eligible 2015--2023 local validation sample. The change-development plan describes stock differencing, trend methods and further validation needs (ADPC v7, pp.~9--18); a proposed validation activity is not a completed assessment of the present interval. In particular, the trend example's assumption of serially uncorrelated annual estimates cannot substitute for estimation of endpoint covariance.

'''
assert anchor in s;s=s.replace(anchor,insert+anchor)
old='The results supplied here are account availability counts, product definitions and computational verification.'
new='The results supplied here are account availability counts, product definitions, territorial and observation-support screening, local mapped-cover endpoints and conditional biomass-allocation sets.'
assert old in s;s=s.replace(old,new)
old="The Cerrado appendix documents GEDI-derived canopy-height information in training-mask refinement. CCI's PUG describes LiDAR-informed allometric development in the biomass product lineage. This identifies a potential shared auxiliary-information family, not proof that identical footprints or error realizations enter both products. Exact overlap and error dependence remain to be traced."
new="The Cerrado appendix documents GEDI-derived canopy-height information in training-mask refinement. CCI's structural inputs have distinct roles: ICESat GLAS supports canopy-density--height calibration, while ICESat-2 heights and national or subnational inventory statistics support the current height--biomass relation, supplemented by FRA statistics where inventory information was not identified. The ATBD explicitly excludes GEDI Level-4 biomass from ingestion and states that the validation inventory-plot database was not used to calibrate or fine-tune this relation (ATBD v7, pp.~57--59, 67--71). Consequently, neither a generic LiDAR label nor the word `inventory' establishes reuse of the same observations. Structural comparisons, historical inputs and current calibration must be distinguished. Exact auxiliary overlap and its implications for error dependence between the selected products remain to be traced."
assert old in s;s=s.replace(old,new)
anchor=r'\subsection{Reference information and dependence}'
insert=r'''The provider's small-plot validation harmonization multiplies a temporally adjusted forest-plot density by forest fraction to construct a comparable reference quantity (PVIR v7, p.~18; PVP v6, p.~15). This introduces assumptions about reference representativeness and nonforest contributions; it does not observe the unknown component densities of a mixed map cell. It is therefore distinct from multiplying an already full-cell-normalized map density by forest fraction. Likewise, model-derived maximum-biomass layers used to constrain retrieval are not independently validated upper bounds on true forest-component density within a mixed cell (ATBD v7, pp.~73--79). Neither operation alone narrows the minimal allocation sets.

'''
assert anchor in s;s=s.replace(anchor,insert+anchor)
anchor=r'\end{document}'
links=r'''
\section{Provider technical references}
Document-specific page references above use PDF page numbers. The cited editions are:
\begin{itemize}
\item CCI Biomass, \emph{Algorithm Theoretical Basis Document}, v7.0, 17 December 2025: \url{https://climate.esa.int/media/documents/Algorithm_Theoretical_Basis_Document_ATBD_V7.0.pdf}.
\item CCI Biomass, \emph{End to End ECV Uncertainty Budget}, v7.0, 17 December 2025: \url{https://climate.esa.int/documents/3354/End-to-End_ECV_Uncertainty_Budget_E3B_V7.0.pdf}.
\item CCI Biomass, \emph{Product Validation and Intercomparison Report}, v7.0, 24 April 2026: \url{https://climate.esa.int/documents/3356/Product_Validation_Intercomparison_Report_PVIR_V7.0.pdf}.
\item CCI Biomass, \emph{Product Validation Plan}, v6.0, 22 December 2025: \url{https://climate.esa.int/documents/3364/Product_Validation_Plan_PVP_V6.pdf}.
\item CCI Biomass, \emph{Algorithm Development Plan Change}, v7.0, 29 April 2026: \url{https://climate.esa.int/documents/3371/Algorithm_Development_Plan_Change_ADPC_V7.0.pdf}.
\end{itemize}
'''
s=s.replace(anchor,links+anchor);p.write_text(s)
(P/'metadata/companion_review_F09').mkdir()
shutil.copyfile('/home/user/.cache/cci_companion_R02/registry.json',P/'metadata/companion_review_F09/source_registry_F09.json')
for part in ['main','SI']:
 before=(B/f'followup_F08_{part}.tex').read_text().splitlines(True);after=(P/f'followup_F09_{part}.tex').read_text().splitlines(True)
 (P/f'metadata/manuscript_{part}_F08_to_F09.diff').write_text(''.join(difflib.unified_diff(before,after,fromfile=f'followup_F08_{part}.tex',tofile=f'followup_F09_{part}.tex')))
# Every original result and freeze file remains byte-identical. Source changes are enumerated separately.
rec={}
for p in B.rglob('*'):
 if p.is_file() and p.parts[-1]not in ['artifact_manifest.json','README.md','REMAINING_EMPIRICAL_WORK.md'] and not any(x in p.parts for x in ['.cache','__pycache__']):
  rel=str(p.relative_to(B));q=P/rel
  if q.exists()and q.read_bytes()==p.read_bytes():rec[rel]=hashlib.sha256(p.read_bytes()).hexdigest()
(P/'metadata/inherited_unchanged_files_F09.json').write_text(json.dumps(rec,indent=2)+'\n')
print('F09 created; unchanged inherited files:',len(rec))

from pathlib import Path
import json,csv,difflib
P=Path('/home/user/ecomod_followup_F07');old=Path('/home/user/ecomod_followup_F06');rows=list(csv.DictReader((P/'data/allocation/endpoint_envelopes_F07.csv').open()));diff=list(csv.DictReader((P/'data/allocation/difference_envelopes_F07.csv').open()));e={(r['group'],int(r['year'])):r for r in rows};changes={r['group']:r for r in diff};fmt=lambda x:f'{float(x)/1000:,.2f}';interval=lambda r:f"[{fmt(r['lower_Mg'])}, {fmt(r['upper_Mg'])}]";di=lambda r:f"[{fmt(r['lower_change_Mg'])}, {fmt(r['upper_change_Mg'])}]"
p=P/'followup_F07_main.tex';s=p.read_text().replace('The results concern account availability, measurement compatibility and local mapped-cover endpoints;','The results concern account availability, measurement compatibility, local mapped-cover endpoints and conditional biomass-allocation sets;');s=s.replace('The inspected reference artifacts do not provide paired endpoint labels within the Brazilian footprint, preventing local change validation from those files.','Within the Brazilian footprint, allocation-only biomass-difference sets contain zero for both mapped-cover groups even when the point maps are treated as exact. The inspected reference artifacts do not provide paired endpoint labels for local change validation.')
marker=r'\subsection{Spatially offsetting local changes}'
method=r'''\subsection{Conditional within-cell biomass allocation}
Native CCI AGB is a full-pixel density, so a finer mapped group fraction does not allocate biomass within a mixed cell. A conditional allocation calculation holds the published point maps, grid and epochs fixed and allows any nonnegative within-cell biomass distribution, without a finite subcell density cap or temporal allocation constraint. These assumptions define a minimal algebraic model, not a complete ecological or measurement-error model.

Let $q_{it}=A_i\widehat d_{it}$ be the auxiliary full-cell biomass mass, $P_t^g$ the cells entirely mapped as group $g$, and $H_t^g$ all cells with a positive-area intersection with that group. The compatible aggregate allocation set is
\[
\widehat{\mathcal I}_t^g=[L_t^g,U_t^g],\qquad
L_t^g=\sum_{i\in P_t^g}q_{it},\quad U_t^g=\sum_{i\in H_t^g}q_{it}.
\]
Integer counts of intersecting finer pixels determine these categories; no near-zero/near-one ecological fraction threshold is imposed. All cells remain in the target footprint. Using pure cells to anchor the lower bound is not a persistent-pure-only analysis sample. Endpoint sets imply the allocation-difference set $[L_{2023}^g-U_{2015}^g,\,U_{2023}^g-L_{2015}^g]$ under the stated absence of temporal restrictions. The Supplementary Information establishes attainability within this minimal model. The sets are not confidence intervals or guaranteed bounds on true forest biomass: map error, density error, epoch mismatch and additional ecological constraints are not represented.

''';assert s.count(marker)==1;s=s.replace(marker,method+marker)
marker=r'\section{Discussion}'
section=r'''\subsection{Conditional biomass-allocation sets}
Table~\ref{tab:allocation} reports the local allocation sets for the same two mapped groups. Both endpoint-difference sets contain zero, permitting negative, zero and positive differences under the minimal allocation model. Thus the sign is not identified by these point maps and nonnegativity alone, before considering measurement uncertainty. Adding savannas changes the mapped domain rather than supplying a confidence interval for the formations target.

\begin{table}[htbp]
\centering\small
\caption{Conditional allocation sets in the fixed Brazilian footprint, in $10^3$ Mg of above-ground woody biomass. Published cover and biomass point maps are treated as exact. Entries are compatible allocations under nonnegativity and unrestricted component density, not statistical confidence intervals or validated forest-stock changes.}\label{tab:allocation}
\begin{tabular}{lrrr}
\toprule
Mapped domain & 2015 & 2023 & 2023 minus 2015\\\midrule
@ROWS@
\bottomrule
\end{tabular}
\end{table}

The auxiliary sum of full-cell masses is $463.92\times10^3$ Mg in 2015 and $529.16\times10^3$ Mg in 2023. These totals refer to every native cell in the local rectangle, not only mapped forest; their increase does not identify a forest-specific gain and does not replace the primary forest-stock target. Observed zero-density cells remain included. The formations group has 791 and 876 mapped-pure cells at the two endpoints, with mixed cells retained in the upper sets. No within-forest mean-density point estimate or extent--density decomposition is inferred from these allocation sets.

'''
labels={'forest_formations':'Formations','formations_plus_savanna':'Formations + savanna'};section=section.replace('@ROWS@','\n'.join(f"{labels[g]} & {interval(e[g,2015])} & {interval(e[g,2023])} & {di(changes[g])} \\\\"for g in labels));assert s.count(marker)==1;s=s.replace(marker,section+marker)
s=s.replace('The evidence comprises account availability, geographic-domain screening, local mapped-cover endpoints, product definitions and the analytical design.','The evidence comprises account availability, geographic-domain screening, local mapped-cover endpoints, conditional allocation sets, product definitions and the analytical design.')
s=s.replace('No forest-only biomass estimate is obtained by multiplying native density by mapped forest fraction.','No forest-only biomass estimate is obtained by multiplying native density by mapped forest fraction. The computed allocation sets quantify one part of the identification problem while conditioning on uncertain point maps; they do not supply a calibrated change-resolution rule.')
s=s.replace('The extent--density and spatial-cancellation estimands provide explicit quantities for that comparison while preserving distinctions among accounts, stocks, condition and biological flows.','The extent--density and spatial-cancellation estimands provide explicit quantities for that comparison while preserving distinctions among accounts, stocks, condition and biological flows. In the local Brazilian example, both mapped-group biomass-difference sets contain zero under the stated minimal allocation model, so that model does not identify a direction of group-specific change.')
s=s.replace('MapBiomas-derived cover summaries identify Collection 11 and the processing used;','Conditional allocation summaries and topological intersection counts are also supplied; raw native-density arrays are not redistributed. MapBiomas-derived cover summaries identify Collection 11 and the processing used;');p.write_text(s)
p=P/'followup_F07_SI.tex';s=p.read_text();marker=r'\section*{Source attribution and availability}'
section=r'''\section{Conditional allocation sets on mapped domains}

For a native cell of area $A_i$ and fixed published full-cell density $\widehat d_{it}$, write $q_{it}=A_i\widehat d_{it}$. Consider an operational mapped group $g$ with area fraction $f_{it}^g$. Conditional on exact cover, density and epoch correspondence, let its unknown biomass allocation be $s_{it}^g$. Under nonnegativity alone,
\begin{equation}
s_{it}^g=0\quad(f_{it}^g=0),\qquad
s_{it}^g=q_{it}\quad(f_{it}^g=1),\qquad
s_{it}^g\in[0,q_{it}]\quad(0<f_{it}^g<1).
\end{equation}
For a mixed cell and any $s\in[0,q]$, choosing component means $s/(Af)$ and $(q-s)/(A(1-f))$ attains the allocation with nonnegative densities. No finite component-density cap, minimum biomass threshold, growth constraint or cross-cell coupling is included. Consequently these are exact allocation bounds within the specified minimal algebraic model, not a claim that every extreme is ecologically plausible.

Let $P_t^g$ be the map-pure cells and $H_t^g$ all map-present cells. Summing the independently compatible allocations gives
\begin{equation}
\widehat{\mathcal I}_t^g=\left[\sum_{i\in P_t^g}q_{it},\;\sum_{i\in H_t^g}q_{it}\right]=[L_t^g,U_t^g].
\end{equation}
All intermediate aggregate values are compatible in this model. With no additional temporal constraint, the endpoint difference set is
\begin{equation}
\widehat{\mathcal D}^g=[L_{2023}^g-U_{2015}^g,\;U_{2023}^g-L_{2015}^g].
\end{equation}
Subtracting the lower endpoints or the upper endpoints alone would not give the full compatible difference set. The interval is conditional on published point maps, not a frequentist confidence set, posterior interval or guaranteed enclosure of true biomass. AGB-SD values are checked for valid support but are not converted to change uncertainty without an appropriate joint error model.

\subsection{Topological support and numerical safeguards}
The classifications are the unchanged Collection 11 subsets and the native densities are the exact hash-matched Brazilian payloads used for earlier observation-support counts. Both density and AGB-SD are valid at all $65{,}536$ target cells at each endpoint. The observed zero counts remain $44{,}546$ and $44{,}767$, respectively. Zero density is not recoded as nonforest, and missing cells are not substituted with zeros.

For each axis, an integer incidence matrix records every finer interval having strictly positive overlap with a native interval. Products of the two axis-incidence matrices with the finer binary group labels give integer counts $c_{it}^g$ of intersecting group pixels; corresponding total counts are $n_i>0$. Absent, pure and mixed cases are determined by $c=0$, $c=n$ and $0<c<n$, respectively, rather than by a rounded forest-fraction threshold. This is an exact topology classification for the recorded grids, not a certification of the ecological classes. Area-weighted fractions recalculated on those overlaps agree with the stored cover fractions to within $3.34\times10^{-16}$.

Each full-pixel mass is multiplied by its WGS84 cell area, not a nominal $100\,\mathrm m\times100\,\mathrm m$ area or a forest fraction. Pure cells number 791 and 876 for formations, and 6,056 and 5,616 for formations plus savanna. Mixed and changing cells are not discarded. The full 61,830.3436 ha rectangle remains the domain, and the pure-cell intersection across years is not used as the analysis sample.

The two formations allocation sets are $[44.2303,279.1932]\times10^3$ Mg and $[55.2216,326.2323]\times10^3$ Mg. The corresponding difference set is $[-223.9717,282.0020]\times10^3$ Mg. Including savannas gives $[229.7548,434.4732]\times10^3$ Mg and $[256.3634,489.2885]\times10^3$ Mg, with difference set $[-178.1098,259.5338]\times10^3$ Mg. Both sets contain zero. They describe distinct mapped domains; neither validates actual forest land use, a national biomass stock or an account--asset divergence. Additional ecological constraints could narrow an allocation model, whereas measurement/classification error requires a separate uncertainty treatment and need not be represented by these endpoints.

The additional XLSX reference alternative was inspected only at ZIP/workbook/shared-string metadata level, not as a complete worksheet. No additional local paired labels, source equivalence or independent validation is inferred from that limited inspection.

''';assert s.count(marker)==1;s=s.replace(marker,section+marker);p.write_text(s)
# Current scope: local conditional mass sets are now computed, not national or validated stock changes.
p=P/'configs/study_design.json';d=json.loads(p.read_text());d['revision']='F07';d['status']='Developing empirical study: local conditional allocation envelopes and bounded XLSX metadata; national physical sample and measurement-error inference incomplete';d['physical_outcome_scope']='Bounded mapped-cover endpoints, conditional map-domain biomass-allocation sets and auxiliary full-cell masses; no validated or national forest stock/change';d['conditional_local_biomass_allocation_envelopes_computed']=True;d['auxiliary_local_full_pixel_masses_computed']=True;d['prior_information_disclosure']+=' F07 subsequently computed auxiliary full-cell masses and minimal-model allocation/difference sets for both fixed mapped groups. The existing local cover and zero/valid outcomes were known before the F07 specification. No untouched held-out or outcome-naive claim is made; both group difference sets are reported regardless of sign. XLSX inspection was metadata-only, not a completed reference audit.';p.write_text(json.dumps(d,indent=2)+'\n')
p=P/'protocol/STUDY_PROTOCOL.md';s=p.read_text()+'''

## F07 conditional allocation exercise and observed mass information

The F06 protocol is archived verbatim at `archive/PROTOCOL_F06.md`. `ALLOCATION_ENVELOPE_F07.md`, the configuration and source input hashes were fixed before computing F07 mass summaries or accessing XLSX ranges. Prior F04 support and F05/F06 local outcomes were known. The frozen supplementary rules are not external registration or held-out evaluation.

Both mapped domains are reported. Conditional on exact point maps/epochs, arbitrary nonnegative within-cell allocation and no finite component-density or temporal constraint, lower/upper aggregates are pure-cell/present-cell full masses. Integer positive-overlap counts, not ecological near-purity thresholds, classify support. All 65,536 cells remain in the fixed footprint. Auxiliary full-cell mass is not silently substituted for forest-only stock. Neither allocation-difference set excludes zero. Actual forest/land-use identity, density/classification error, spatial/temporal covariance and reference timing are not calibrated by these sets.

These computations expose actual local mass summaries and model-conditional difference ranges, so statements that no physical outcomes have ever been computed no longer describe current F07. Earlier records remain historical with their stated scope. No national forest/biomass change, validated local forest-stock change, account–asset sign or reporting performance is estimated. All national admissions remain on hold.

The Excel alternative is 33,714,740 bytes and its worksheet declares 371,343,772 uncompressed bytes. Standing caps were not increased: 160,308 distinct source bytes provide ZIP/workbook/shared-string metadata only. The worksheet was not opened/decoded. No populated-column, complete endpoint, file-equivalence or independent-reference claim is made from shared-string tokens.
''';p.write_text(s)
p=P/'REMAINING_EMPIRICAL_WORK.md';s=p.read_text().replace('## 2. Establish change uncertainty and independent reference information','**F07 status:** the fixed Brazil window now has conditional map-domain biomass allocation/difference sets computed from hash-matched native densities and integer cover-overlap certificates. Both reported difference sets contain zero, even with point maps treated as exact. This is partial identification under a minimal allocation model, not a calibrated uncertainty interval or validated forest stock. All cells remain included; the primary forest target is not replaced by auxiliary whole-cell masses. The XLSX alternative received bounded ZIP metadata inspection only; its full reference population remains unaudited under the standing caps. See `ALLOCATION_RESULTS_F07.md`.\n\n## 2. Establish change uncertainty and independent reference information');s=s.replace('The XLSX link has not been decoded and is not certified equivalent.','The XLSX worksheet has not been decoded; F07 inspected ZIP/workbook/shared-string metadata only and did not certify equivalence.');s=s.replace('No such national stock or account–asset outcomes have been estimated. The bounded F05 mapped-cover endpoints are observed descriptive outcomes, not national stock/change estimates.','No such national stock or account–asset outcomes have been estimated. F05 mapped-cover endpoints and F07 local auxiliary masses/conditional allocation sets are computed, but do not constitute validated or national forest-stock/change estimates.');p.write_text(s)
p=P/'metadata/SOURCE_USE.md';s=p.read_text()+'''

## F07 local allocation summaries and bounded workbook metadata

CCI Biomass v7.0 is credited under the existing CEDA terms. Two old Brazilian native payloads are retrieved again and verified against their exact F04 SHA identities; only own aggregate conditional allocation/auxiliary-mass summaries are redistributed, not the source density arrays. Pinned MapBiomas Collection 11 subsets are redecoded and verified against old subset/range hashes; derived integer overlap counts and own aggregate envelopes are supplied with MapBiomas attribution. These are transformed scientific summaries, not provider-endorsed forest estimates. Classification and density estimates are conditioned on, not validated.

The public Excel reference alternative is inspected through ETag-pinned HTTP206 ranges: ZIP directory, workbook and shared strings only. Full workbook size exceeds the 25MB transfer cap; worksheet size exceeds the full-member decompression guard. It is not opened or decoded. No full-object SHA from this partial access is claimed. Exact range and fully read metadata-member hashes identify the actual scope in `reference/xlsx_metadata_F07.json`. No raw workbook, byte blocks or source PDFs are redistributed; public/free source attribution conditions are unchanged.
''';p.write_text(s)
rows=list(csv.DictReader((P/'data/support/physical_admission_F06.csv').open()));
with (P/'data/support/physical_admission_F07.csv').open('w',newline='')as f:w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
D=P/'metadata/source_comparisons'
for n in ['main','SI']:
 a=(old/f'followup_F06_{n}.tex').read_text().splitlines(keepends=True);b=(P/f'followup_F07_{n}.tex').read_text().splitlines(keepends=True);(D/f'F06_to_F07_{n}.diff').write_text(''.join(difflib.unified_diff(a,b,fromfile=f'F06/{n}',tofile=f'F07/{n}')))
print('F07 main/SI updated from generated results; current scope and disclosures qualified')

"""One-time, additive preparation of F10 from protected F09. Refuses existing F10.
Historical data/results/source-review records are copied without recalculation.
"""
from pathlib import Path
import shutil, json, hashlib, difflib
BASE=Path(__file__).resolve().parents[2]
OLD=BASE/'ecomod_followup_F09';NEW=BASE/'ecomod_followup_F10';R03=BASE/'ecomod_followup_feasibility_R03'
if NEW.exists():raise SystemExit('F10 exists; do not recreate or overwrite')
shutil.copytree(OLD,NEW,ignore=shutil.ignore_patterns('.cache','__pycache__','artifact_manifest_F09.json','followup_F09_main.pdf','followup_F09_SI.pdf','finalize_checks_F09.py','publish_F09.py','build_F09.sh'))
for part in ['main','SI']:(NEW/f'followup_F09_{part}.tex').rename(NEW/f'followup_F10_{part}.tex')
(NEW/'README.md').rename(NEW/'README_inherited_F09.md')
for name in ['test_scientific_scope_F09.py','test_xlsx_F09.py']:
 p=NEW/'tests'/name;s=p.read_text().replace('followup_F09_','followup_F10_').replace('ScientificScopeF09Tests','ScientificScopeF10Tests');p.unlink();(p.parent/name.replace('F09','F10')).write_text(s)
for f in ['native_sd_summary_R03.csv','local_reference_candidate_R03.csv']:shutil.copyfile(R03/'data'/f,NEW/'data/reference'/f)
for f in ['native_sd_audit_R03.json','native_payload_registry_R03.json','reference_archive_inspection_R03.json','agbref_preprint_identity_R03.json']:shutil.copyfile(R03/'metadata'/f,NEW/'metadata'/f)
main=NEW/'followup_F10_main.tex';s=main.read_text()
end=s.index(r'\section{Results}')
methods=r'''
Stored native uncertainty is described separately from uncertainty calibration. On the fixed Brazilian rectangle, AGB and its SD are screened jointly against the delivered valid ranges, retaining valid zeros and distinguishing declared fill values. Counts and positive-AGB SD quantiles describe the stored values; they do not estimate error-correlation parameters or confidence coverage. A separate reference-eligibility assessment considers released 500 m AGBref aggregates, target epochs, available census provenance, plot counts and published support-quality flags \citep{AGBref2026,AGBrefData2026}. Shared coordinates or multiple target-epoch labels are not sufficient evidence of repeated field measurements.

'''
s=s[:end]+methods+s[end:]
# Add empirical SD results immediately before the existing national-admission subsection.
anchor=r'\subsection{Conditional biomass-allocation sets}'
paragraph=r'''
Within the fixed Brazilian rectangle, 1,032 cells in 2015 and 946 in 2023 have positive AGB but stored SD equal to zero; their AGB estimates range from 1 to 4 Mg/ha. All 65,536 cells have valid AGB and SD at each endpoint. Median SD among positive-AGB cells is 6 and 7 Mg/ha, respectively. These are descriptive properties of integer-valued source layers, not evidence of zero true error. The source fields examined do not identify the origin of those zeros. Nor do the 44,021 cells with zero AGB at both endpoints establish persistent ecological absence (Supplementary Material, S7).

'''
s=s.replace(anchor,paragraph+anchor,1)
# Distinguish biomass-reference eligibility from the existing mapped-cover reference audit.
anchor=r'\subsection{Conditional biomass-allocation sets}'
pos=s.index(anchor)
reference=r'''\subsection{Biomass-reference eligibility}

The open AGBref release contains one 500 m aggregate centroid inside the fixed Brazilian rectangle in each of its inspected 2010, 2015 and 2020 files \citep{AGBrefData2026}. Each local record has one contributing plot, a zero AGB estimate and zero minimum-plot, local-representativity and strict-filter flags. The descriptor requires more than one plot at 500 m; these records therefore fail that support criterion \citep{AGBref2026}. Their target-epoch labels do not disclose original census dates, and their different aggregate identifiers do not establish repeated original observations. The archive has no named 2023 member; an inspected unnamed file supplies no date field. This is accessible local reference information, but not a compatible paired 2015--2023 sample. No map--reference performance statistic is calculated from it (Supplementary Material, S9).

'''
s=s[:pos]+reference+s[pos:]
s=s.replace('/ecomod_empirical_followup/F09','/ecomod_empirical_followup/F10')
bib=r'''\bibitem[Araza et al.(2026a)]{AGBref2026} Araza, A., Herold, M., Avitabile, V., et al. (2026a). AGBref: A global reference dataset of above-ground forest biomass. \emph{Research Square}, preprint, posted 9 January 2026. \url{https://doi.org/10.21203/rs.3.rs-8211898/v1}.
\bibitem[Araza et al.(2026b)]{AGBrefData2026} Araza, A., Bielig, C., and Flores, R. A. A. (2026b). AGBref---Global Reference Dataset for Above-Ground Biomass (AGB). Zenodo, record 20793072, file \texttt{agb-ref-v2.zip}. \url{https://doi.org/10.5281/zenodo.20793072}.
'''
s=s.replace('\\end{thebibliography}',bib+'\\end{thebibliography}');main.write_text(s)
si=NEW/'followup_F10_SI.tex';s=si.read_text();anchor='\\section{Brazilian mapped-cover fractions and observation operators}'
native=r'''\subsection{Stored uncertainty and zero estimates}

The same native payloads contain the AGB and \texttt{agb\_sd} arrays. Their Int16 units are Mg/ha, declared fill is $-32768$ and valid range is 0--10,000. Both arrays have valid values at all 65,536 cells per endpoint. The AGB ancillary-variable attribute names \texttt{agb\_se}, although the listed variable is \texttt{agb\_sd}; this name discrepancy is not interpreted as data corruption or silently repaired. No separate forest mask, zero-origin field or covariance variable occurs in the examined native variable list.

\begin{table}[htbp]
\centering\small
\caption{Stored native AGB/SD diagnostics on the fixed Brazilian rectangle. Zero is retained as a valid source value. These counts and quantiles do not measure ecological absence or calibrated uncertainty.}\label{tab:native_sd}
\begin{tabular}{lrr}
\toprule
Diagnostic & 2015 & 2023\\\midrule
AGB $=0$ & 44,546 & 44,767\\
SD $=0$ & 45,578 & 45,713\\
AGB $>0$, SD $=0$ & 1,032 & 946\\
AGB $=0$, SD $>0$ & 0 & 0\\
Positive-AGB SD: lower quartile (Mg/ha) & 3 & 3\\
Positive-AGB SD: median (Mg/ha) & 6 & 7\\
Positive-AGB SD: upper quartile (Mg/ha) & 12 & 14\\\bottomrule
\end{tabular}
\end{table}

Positive AGB at stored SD zero ranges from 1 to 4 Mg/ha at both endpoints. The storage precision alone does not establish whether rounding, clipping, retrieval conventions or another process caused these cases, and no unverified SD floor is imposed. Stored zero/nonzero AGB states contain 44,021 zero--zero, 525 zero--positive, 746 positive--zero and 20,244 positive--positive cells. They exhaust the rectangle, but are not ecological transition classes. The values supply neither final-map cross-year error covariance nor a forest/nonforest allocation of whole-cell biomass.

'''
s=s.replace(anchor,native+anchor,1)
anchor='\\section{Conditional allocation sets on mapped domains}'
reference=r'''\subsection{AGBref stock-reference compatibility}

The AGBref descriptor distinguishes harmonized target-epoch stocks from original field dates. Its preprocessing adjusts references within ten years of a target epoch using IPCC growth rates; its timeliness flag uses a three-year criterion. At 500 m and 1 km, the minimum-plot criterion is more than one plot. Local representativity and a strict combined filter are separate criteria (preprint PDF pp. 7--8). Temporal harmonization does not create a measured repeat census, and uncertainty in that adjustment does not independently validate a satellite change estimate.

The open Zenodo record 20793072, file \texttt{agb-ref-v2.zip}, supplies named 2005, 2010, 2015 and 2020 products but no named 2023 product. Complete 2010, 2015 and 2020 500 m CSVs and its unnamed CSV were inspected. Each has 200,152 rows and one released aggregate centroid inside the fixed native rectangle, at $49.6825^\circ$W, $14.2175^\circ$S. Centroid inclusion is not proof of compatible polygon support or original plot representativeness. The three labelled local records have distinct aggregate identifiers, $N=1$, AGB zero, and zero minimum-plot, large-size, local-representativity and strict-filter flags. SDs are approximately 22.55, 22.55 and 23.02 Mg/ha. Their timeliness flags are zero, one and one. The unnamed record has no date field and is not assigned a 2023 epoch.

The selected exports do not provide original census dates, source-provider codes or original plot identity. Consequently, neither the repeated centroid nor the epoch labels establish an independent repeated-plot pair. The observed plot count also fails the stated 500 m minimum criterion, independently of the zero AGB estimate. No local biomass comparison is admitted from these rows. This conclusion concerns the inspected support and primary interval, not all inventories or every coarser reference product. A four-row, attributed derived subset and the eligibility fields are supplied with the data; no full reference archive is redistributed.

'''
s=s.replace(anchor,reference+anchor,1)
s=s.replace('/ecomod_empirical_followup/F09','/ecomod_empirical_followup/F10')
anchor='Source hashes, metadata, derived account-availability tables and computational methods are available'
s=s.replace(anchor,'AGBref: Araza, A., Bielig, C., and Flores, R. A. A. (2026), \\emph{AGBref---Global Reference Dataset for Above-Ground Biomass (AGB)}, Zenodo record 20793072; \\url{https://doi.org/10.5281/zenodo.20793072}, CC BY 4.0. The limited local subset is derived from the released aggregate CSVs, with source member and record attribution. Descriptor: Araza, A., et al. (2026), Research Square preprint; \\url{https://doi.org/10.21203/rs.3.rs-8211898/v1}. Source files and reference metadata do not establish paired field observations.\n\n'+anchor)
si.write_text(s)
# Record actual deltas, outside manuscript prose.
for part in ['main','SI']:
 a=(OLD/f'followup_F09_{part}.tex').read_text().splitlines(True);b=(NEW/f'followup_F10_{part}.tex').read_text().splitlines(True)
 (NEW/f'metadata/source_comparisons/F09_to_F10_{part}.diff').write_text(''.join(difflib.unified_diff(a,b,fromfile=f'F09_{part}',tofile=f'F10_{part}')))
inherited={str(p.relative_to(NEW)):hashlib.sha256(p.read_bytes()).hexdigest()for p in NEW.rglob('*')if p.is_file()and (OLD/p.relative_to(NEW)).is_file()and p.read_bytes()==(OLD/p.relative_to(NEW)).read_bytes()}
(NEW/'metadata/inherited_unchanged_files_F10.json').write_text(json.dumps(inherited,indent=2)+'\n')
print('F10 prepared; inherited byte-identical files:',len(inherited))

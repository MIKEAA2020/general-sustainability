from pathlib import Path
import json,csv,shutil,hashlib,difflib
P=Path('/home/user/ecomod_followup_F09');D=Path('/home/user/.cache/cci_companion_R02');M=P/'metadata/companion_review_F09'
# Limited derived table transcription, not paired records or new ecological results.
rows={2015:[('0-50',3008,28,46,17,29),('50-100',2231,69,78,9,34),('100-150',604,121,131,10,72),('150-200',312,173,192,19,90),('200-250',178,223,219,-4,85),('250-300',135,274,245,-28,88),('300-400',81,339,237,-101,136),('>400',52,694,279,-415,490)],2023:[('0-50',900,33,48,15,25),('50-100',1525,71,73,2,27),('100-150',347,119,99,-20,58),('150-200',108,172,163,-9,71),('200-250',58,221,199,-22,83),('250-300',29,275,270,-5,63),('300-400',30,329,233,-95,132),('>400',37,754,297,-457,594)]}
with (P/'data/reference/provider_stock_examples_F09.csv').open('w')as f:
 w=csv.writer(f);w.writerow(['map_year','reference_AGB_bin_Mg_ha','n_0p1deg_cells','mean_reference_Mg_ha','mean_map_Mg_ha','reported_MD_Mg_ha','reported_RMSD_Mg_ha','source_table','source_pdf_page','source_url','paired_change_observations'])
 for year,rr in rows.items():
  tab,page=(66,64)if year==2015 else(74,67)
  for r in rr:w.writerow([year,*r,tab,page,'https://climate.esa.int/documents/3356/Product_Validation_Intercomparison_Report_PVIR_V7.0.pdf#page='+str(page),'no'])
# Page/table addresses of each scientific addition. No source raw page text included.
findings=[
('C01','E3UB','14-19','source','C-band image-stack covariance is modelled','Not final-map cross-year covariance','Main uncertainty; SI S3'),
('C02','E3UB','21-22','source','L-band within-stack correlation assumption is 0.5','Not endpoint rho(2015,2023)','Main uncertainty; SI S3'),
('C03','E3UB','23-26','source','Spatial covariance ensemble from 142 one-degree cells and eight regional datasets','Not representative global/local calibration','SI S3'),
('C04','E3UB','23','visually verified source discrepancy','Printed mean-variance equations use 1/N and 2/N','Provider executable implementation not verified','External review only'),
('C05','PVP','26','visually verified source plus algebra','Equal-weight mean covariance sum uses 1/n^2','No local covariance supplied','SI S3'),
('C06','E3UB','24-26','visually verified source discrepancy plus algebra','Printed increasing Eq3-19 contradicts prior equations and descending plots','Do not infer a verified code correction','External review only'),
('C07','E3UB','28','source','Change-variance expression sums endpoint variances','Omission does not establish zero true cross-year covariance','Main uncertainty; SI S3'),
('C08','E3UB','28','source','Bias-correction uncertainty is discussed conditionally at 0.1degree','No applied local correction established','SI S3'),
('C09','PVIR','11-14','source','Independent current v7 stock validation and held-out reference data','Not validation of our paired local forest change','Main and SI S6'),
('C10','PVIR','14','source','Listed plot totals 2015=112334 and 2023=52428','Not paired counts or counts in every later table','External review'),
('C11','PVIR','13','source with retained older epoch wording','Screening describes exclusion of deforested plots','Exact execution for each new year not verified','Main Discussion; SI S6'),
('C12','PVIR','18','source visually cross-checked','Growth-rate harmonization permits up to ten-year offsets','Not necessarily contemporaneous repeated observation','Main and SI S6'),
('C13','PVIR','18','source visually cross-checked','Small-plot forest-fraction correction and at least five plots per 0.1degree cell','Does not identify component biomass from a full-pixel map','SI S8'),
('C14','PVIR','19','source','SE random-only; spatial covariance included; IVar is a variance diagnostic','Not 95percent coverage and RMSD not pure map error','Main and SI S6'),
('C15','PVIR','64,67','reported numerical stock summaries','Tables66/74 directly assess 2015/2023 stocks at 0.1degree','Different reference cohorts; no temporal-bias difference inferred','Derived source CSV; main citation'),
('C16','PVIR','85-88','source; p86 visually inspected','Brazilian NFI comparison uses 2018 map and fixed wood density0.632','Not local paired2015-2023 validation','External review'),
('C17','PVIR','96-98','source','Within-pixel sampling can create apparent bin bias','Discrepancy is not necessarily map-only error','Main Discussion; SI S6'),
('C18','PVP','17-18,22,42','source with internal candidate/current-use discrepancy','Repeated NFI/LiDAR candidates include Brazil2011-2018 in appendix','Does not establish available eligible local2015-2023 reference','SI S6; remaining work'),
('C19','PVP','23-26','source','Map, reference, support and harmonization errors distinguished','Proposed identification is not completed local calibration','SI S3/S6'),
('C20','ADPC','9-18','source','Stock-difference/trend development and further validation activities','Plans and serial-independence assumption do not validate our endpoint difference','SI S6'),
('C21','PVIR/PVP/ADPC','1,13-15,18,99','source provenance discrepancy','Current covers coexist with stale headers/counts and differing harmonization thresholds','No silent repair or relabelling of entire edition','External review and source-scope metadata'),
('C22','derived','not applicable','general mathematical identity','Weighted spatial/endpoint covariance and systematic-error difference','No empirical parameter or coverage is estimated','SI S3')]
reg=json.loads((D/'registry.json').read_text());urls={x['key']:x['url']for x in reg['documents']}
with (P/'EVIDENCE_MATRIX_F09.csv').open('w')as f:
 w=csv.writer(f);w.writerow(['id','document','pdf_pages','evidence_type','finding','limit','integration','url'])
 for row in findings:w.writerow([*row,urls.get(row[1],'See source register / ATBD review R01')])
scope={'review_date':'2026-10-29','four_full_pdfs_acquired':True,'total_pdf_pages_acquired':202,'all_pages_closely_reviewed':False,'targeted_sections':{'E3UB':'Core precision, within-stack covariance, spatial aggregation and change sections pp7-9,14-28','PVIR':'pp11-19, selected endpoint tables pp30/32/64/67, Brazil pp85-88, support discussion pp96-99; other text only screened','PVP':'pp15-18,20-26,42; some long early extraction outputs were truncated','ADPC':'pp9-18 methods/discussion; earlier sections screened'},'visually_opened_pdf_pages':{'E3UB':[23,24,25,26,28],'PVIR':[18,86],'PVP':[26],'ADPC':[]},'rendered_but_not_opened_pages_not_counted_as_visual_review':True,'source_provenance_discrepancies':['PVIR v7 cover versus v3/v1 body headers and older dates','PVIR Table1 tier counts versus retained smaller conclusion ranges','PVP15 versus PVIR18 age-category thresholds differ','PVP18 currently retained change-reference account versus Brazil candidate in Appendix2','ADPC v7 cover versus V6 reference and v5 body headers','E3UB23 average normalization conflicts with general identity and PVP26','E3UB25 printed correlation contradicts E3UB24/25 preceding equations and plotted decay'],'transfer_guard_per_document_bytes':25000000,'raster_guards_changed':False,'raw_source_pdf_text_or_images_redistributed':False,'new_paired_reference_acquired':False,'provider_executable_implementation_verified':False,'local_covariance_estimated':False,'local_change_coverage_calibrated':False,'national_admission_changed':False}
(M/'review_scope_F09.json').write_text(json.dumps(scope,indent=2)+'\n')
# Hashes are source identities, not a redistribution of full copyrighted text.
pagehash={}
for k in urls:
 d=json.loads((D/(k+'_pages.json')).read_text());pagehash[k]={n:hashlib.sha256(t.encode()).hexdigest()for n,t in d.items()}
(M/'extracted_page_hashes_F09.json').write_text(json.dumps(pagehash,indent=2)+'\n')
# Current primary manuscript cites actual endpoint result pages as well as method pages.
p=P/'followup_F09_main.tex';s=p.read_text().replace(r'\citep[pp.~11--14]{PVIR2026}',r'\citep[pp.~11--14, 64, 67]{PVIR2026}');p.write_text(s)
# Refresh complete editorial differences after all changes.
for part in ['main','SI']:
 before=(P.parent/'ecomod_followup_F08'/f'followup_F08_{part}.tex').read_text().splitlines(True);after=(P/f'followup_F09_{part}.tex').read_text().splitlines(True)
 (P/f'metadata/manuscript_{part}_F08_to_F09.diff').write_text(''.join(difflib.unified_diff(before,after,fromfile=f'followup_F08_{part}.tex',tofile=f'followup_F09_{part}.tex')))
print('Evidence matrix',len(findings),'findings; derived source table',sum(map(len,rows.values())),'rows')

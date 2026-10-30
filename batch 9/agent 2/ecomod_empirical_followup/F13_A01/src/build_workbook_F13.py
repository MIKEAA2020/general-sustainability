#!/usr/bin/env python3
"""Integrated readable workbook. Original F12 file is read, never overwritten."""
import csv,datetime,hashlib,json,math
from pathlib import Path
import openpyxl
from openpyxl.styles import Font,PatternFill,Alignment
from openpyxl.worksheet.table import Table,TableStyleInfo
from analyze_sources_F13 import ROOT,require
F12=ROOT.parent/'ecomod_empirical_closure_F12_A01'
if not F12.is_dir():F12=ROOT.parent/'F12_A01'

def sheet(w,name,rows):
 require(name not in w.sheetnames,'Duplicate sheet '+name)
 s=w.create_sheet(name)
 for row in rows:s.append(row)
 s.freeze_panes='A2';s.auto_filter.ref=s.dimensions
 for cell in s[1]:cell.font=Font(color='FFFFFF',bold=True);cell.fill=PatternFill('solid',fgColor='164A50');cell.alignment=Alignment(wrap_text=True,vertical='center')
 s.row_dimensions[1].height=42
 for col in s.columns:
  n=col[0].column_letter;values=[str(c.value)for c in list(col)[:50]if c.value is not None]
  s.column_dimensions[n].width=min(48,max(13,max(map(len,values),default=10)+2))
  for cell in list(col)[1:]:
   if isinstance(cell.value,float):cell.number_format='#,##0.000000;[Red]-#,##0.000000'
   cell.alignment=Alignment(vertical='top',wrap_text=isinstance(cell.value,str)and len(cell.value)>45)
 return s

def csvrows(name,predicate=None):
 with (ROOT/'data'/name).open()as f:rows=list(csv.reader(f))
 if predicate:rows=[rows[0]]+[r for r in rows[1:]if predicate(dict(zip(rows[0],r)))]
 header=rows[0];out=[header]
 for row in rows[1:]:
  outrow=[]
  for x in row:
   try:y=float(x);outrow.append(int(y)if y.is_integer()and abs(y)<1e15 else y)
   except ValueError:outrow.append(x)
  out.append(outrow)
 return out

def run():
 src=F12/'national_results_F12_A01.xlsx';w=openpyxl.load_workbook(src)
 notes=[['Topic','Definition or interpretation'],
 ['One publication','Integrated main manuscript and SI; F12 is an immutable earlier deposit, not a separate submission.'],
 ['Original sheets','The first 19 sheets preserve the F12 workbook values and definitions.'],
 ['Primary national AGB','0 of 8 original calibrated 2015–2023 national forest-AGB comparisons admitted.'],
 ['FRA volume','Living bois fort tige on production forest, metropolitan France including Corsica; not whole AGB.'],
 ['FRA windows','2013–2017, 2018–2022, 2019–2023 and 2021–2025 campaign pools; not exact endpoint censuses.'],
 ['FRA union90','At least 90% per contrast under published marginal 95% sampling coverage; no endpoint independence.'],
 ['FRA normal95','Additional marginal-normal interpretation; endpoint_family=4 jointly covers all three latest-cycle contrasts approximately 95%.'],
 ['FRA rounding and bias','Full published-unit outward allowance for each estimate/CI; differential bias B remains unbounded and widens each side by B.'],
 ['CAN change','Inventory-domain annualized AGB change, combined remeasured and projected data, not exact 2015–2023.'],
 ['CAN intervals','Provider-labelled halfwidths; confidence level of current change export not independently established.'],
 ['CAN RSE','Separate change RSE and interval tables do not reconcile under usual RSE definition; no smaller change SE inferred.'],
 ['CAN geography','262.190 million ha of specified northern regions not inventoried; omitted biomass not assumed zero.'],
 ['COD grouping','Source forest classes 3, 4, 5; class 4 is woodland here, not Brazil savanna. Plantations separate.'],
 ['COD support','Country, biome and province totals differ; subunits not certified to partition country footprint.'],
 ['COD uncertainty','Mapped extent changes and break-even errors are not reference-calibrated confidence intervals or biomass changes.'],
 ['BRA current vector','Freshly linked October 2026 archive still has annual fields only through 2022; URL date is not reference epoch coverage.'],
 ['Dependencies','F11 and F12 original numeric sources, manifests and receipts remain immutable and are SHA-verified.'],
 ['Assistance','Arena.ai Agent Mode was used to assist with computational methods and literature review.']]
 sheet(w,'F13 interpretation',notes)
 specs=[('FRA endpoints','FRA_inventory_endpoints_F13.csv',None),('FRA change bounds','FRA_volume_change_bounds_F13.csv',None),
 ('CAN biomass intervals','CAN_NFI_biomass_intervals_F13.csv',None),
 ('COD national changes','COD_C1_extent_changes_F13.csv',lambda r:r['level']=='country'),
 ('COD subunit changes','COD_C1_extent_changes_F13.csv',lambda r:r['level']!='country'),
 ('COD national annual','COD_C1_extent_annual_F13.csv',lambda r:r['level']=='country'),
 ('COD support summary','COD_C1_support_audit_F13.csv',None),('COD support gaps','COD_C1_subunit_footprint_differences_F13.csv',None),
 ('COD class crosswalk','COD_C1_class_crosswalk_F13.csv',None)]
 for name,file,pred in specs:sheet(w,name,csvrows(file,pred))
 registry=json.loads((ROOT/'metadata/source_registry_F13.json').read_text());rows=[['Source key','URL','Bytes','SHA256','Provider file redistributed']]
 for key,r in sorted(registry.items()):rows.append([key,r['url'],r['bytes'],r['sha256'],False])
 sheet(w,'F13 source registry',rows)
 w.properties.title='Integrated national evidence and uncertainty results';w.properties.creator='Amin Abaee'
 w.properties.description='Typed national account, mapped forest, conditional flow and inventory results. Original primary national AGB holds retained.'
 w.properties.created=datetime.datetime(2026,10,30);w.properties.modified=datetime.datetime(2026,10,30)
 dest=ROOT/'national_results_F13_A01.xlsx';w.save(dest);w.close()
 # Read every cell back, including all inherited sheets.
 a=openpyxl.load_workbook(src,read_only=True,data_only=False);b=openpyxl.load_workbook(dest,read_only=True,data_only=False);checked=0
 try:
  for s in a:
   t=b[s.title];require((s.max_row,s.max_column)==(t.max_row,t.max_column),'Inherited sheet dimensions changed')
   for r0,r1 in zip(s.values,t.values):
    for x,y in zip(r0,r1):
     if isinstance(x,float)and isinstance(y,(float,int)):ok=math.isclose(x,y,rel_tol=1e-13,abs_tol=1e-9)
     else:ok=x==y
     require(ok,'Inherited workbook cell changed '+s.title);checked+=1
  sheets=[dict(name=s.title,rows=s.max_row,columns=s.max_column)for s in b]
 finally:a.close();b.close()
 result=dict(file=dest.name,sha256=hashlib.sha256(dest.read_bytes()).hexdigest(),sheets=sheets,
             inherited_sheets_verified=19,inherited_cells_compared=checked,source_workbook_unmodified=True)
 (ROOT/'metadata/workbook_QA_F13.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':run()

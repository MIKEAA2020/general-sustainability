#!/usr/bin/env python3
"""Read back deliverables, inspect numerical workbook lineage and render every page.
--confirm-visual-review is only used after a human/agent has actually inspected
all generated layout sheets; rendering alone is not called visual review.
"""
import argparse,hashlib,json,math,re
from pathlib import Path
import openpyxl,pymupdf
from PIL import Image,ImageDraw
from analyze_sources_F13 import ROOT,require
from build_workbook_F13 import csvrows
CACHE=ROOT.parent/'.cache/F13'
DECLARATION='Arena.ai Agent Mode was used to assist with computational methods and literature review.'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def pdf(kind):
 path=ROOT/f'integrated_F13_A01_{kind}.pdf';d=pymupdf.open(path);bad=[];fonts=set();text='';counts=[];links=[];sheets=[]
 try:
  for i,page in enumerate(d):
   t=page.get_text();counts.append(len(t));text+=t+'\n';links.extend(l.get('uri','')for l in page.get_links())
   for block in page.get_text('dict')['blocks']:
    for line in block.get('lines',[]):
     for span in line.get('spans',[]):
      x0,y0,x1,y1=span['bbox']
      if x0<-.5 or y0<-.5 or x1>page.rect.width+.5 or y1>page.rect.height+.5:bad.append(dict(page=i+1,text=span['text'],bbox=span['bbox']))
   for f in page.get_fonts(full=True):fonts.add(f[0])
  font_checks=[]
  for f in sorted(fonts):
   embedded_font=bool(d.extract_font(f)[3]);kind_of_font='extractable font program'
   if not embedded_font:
    obj=d.xref_object(f);match=re.search(r'/CharProcs\s+(\d+)\s+0\s+R',obj)
    if '/Subtype /Type3'in obj and match:
     procs=d.xref_object(int(match.group(1)));refs=re.findall(r'(\d+)\s+0\s+R',procs)
     embedded_font=bool(refs)and all(bool(d.xref_stream(int(r)))for r in refs)
     kind_of_font='embedded Type3 CharProcs verified'
   font_checks.append(dict(xref=f,embedded=embedded_font,method=kind_of_font))
  embedded=all(r['embedded']for r in font_checks)
  require(not bad,'PDF text outside page '+kind);require(embedded,'Unembedded PDF font '+kind)
  require(all(n>400 for n in counts),'Unexpected near-blank page '+kind)
  norm=' '.join(text.split());orcid=any('orcid.org/0000-0002-0019-1842'in u for u in links)
  require(orcid,'Missing hyperlinked ORCID '+kind)
  if kind=='main':
   require(DECLARATION in norm,'Exact approved AI declaration missing')
   for token in ['3.303','17.639','104','296','90.502','309.498','634']:
    require(token in text,'Integrated scientific value missing '+token)
   require('none is admitted to a national physical-change comparison'not in text,'Obsolete universal national exclusion')
   require('no completed physical numerical module'in norm.lower(),'Remaining work omitted')
  layout=CACHE/'layout';layout.mkdir(exist_ok=True)
  for start in range(0,len(d),6):
   images=[]
   for i in range(start,min(start+6,len(d))):
    pix=d[i].get_pixmap(matrix=pymupdf.Matrix(1.1,1.1));im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples);im.thumbnail((650,920));tile=Image.new('RGB',(680,960),'#d6d6d6');tile.paste(im,((680-im.width)//2,30));ImageDraw.Draw(tile).text((12,8),f'{kind} | Page {i+1}',fill='black');images.append(tile)
   canvas=Image.new('RGB',(1360,960*((len(images)+1)//2)),'#d6d6d6')
   for j,im in enumerate(images):canvas.paste(im,((j%2)*680,(j//2)*960))
   p=layout/f'{kind}_{start+1:02}_{min(start+6,len(d)):02}.jpg';canvas.save(p,quality=88);sheets.append(str(p))
  log=CACHE/'latex'/f'integrated_F13_A01_{kind}.log'
  errors=[line for line in log.read_text().splitlines()if any(t in line for t in ['Overfull','undefined references','undefined citations','LaTeX Error'])]
  require(not errors,'Typesetting diagnostics unresolved '+kind+str(errors))
  return dict(file=path.name,sha256=sha(path),pages=len(d),text_characters_by_page=counts,
   text_outside_page_bounds=bad,all_fonts_embedded=embedded,font_embedding_checks=font_checks,ORCID_hyperlink=orcid,
   exact_AI_declaration=DECLARATION in norm if kind=='main'else'not repeated in SI',
   source_values_checked=kind=='main',layout_review_sheets=sheets)
 finally:d.close()
def equal(x,y):
 if x=='':x=None
 if y=='':y=None
 if isinstance(x,(float,int))and isinstance(y,(float,int)):return math.isclose(x,y,rel_tol=1e-13,abs_tol=1e-9)
 return x==y
def workbook():
 path=ROOT/'national_results_F13_A01.xlsx';w=openpyxl.load_workbook(path,read_only=True,data_only=False);checked=0
 specs=[('FRA endpoints','FRA_inventory_endpoints_F13.csv',None),('FRA change bounds','FRA_volume_change_bounds_F13.csv',None),
 ('CAN biomass intervals','CAN_NFI_biomass_intervals_F13.csv',None),('COD national changes','COD_C1_extent_changes_F13.csv',lambda r:r['level']=='country'),
 ('COD subunit changes','COD_C1_extent_changes_F13.csv',lambda r:r['level']!='country'),('COD national annual','COD_C1_extent_annual_F13.csv',lambda r:r['level']=='country'),
 ('COD support summary','COD_C1_support_audit_F13.csv',None),('COD support gaps','COD_C1_subunit_footprint_differences_F13.csv',None),('COD class crosswalk','COD_C1_class_crosswalk_F13.csv',None)]
 try:
  for name,file,pred in specs:
   expected=csvrows(file,pred);s=w[name];actual=list(s.values);require(len(actual)==len(expected),'Workbook row mismatch '+name)
   for row0,row1 in zip(expected,actual):
    require(len(row0)==len(row1),'Workbook column mismatch '+name)
    for x,y in zip(row0,row1):require(equal(x,y),'Workbook value mismatch '+name);checked+=1
  count=len(w.sheetnames);require(count==30,'Expected 30 integrated workbook sheets')
 finally:w.close()
 old=json.loads((ROOT/'metadata/workbook_QA_F13.json').read_text());require(old['sha256']==sha(path),'Stale workbook lineage QA')
 return dict(file=path.name,sha256=sha(path),sheets=count,new_CSV_cells_independently_checked=checked,
   inherited_sheets_compared=old['inherited_sheets_verified'],inherited_cells_compared=old['inherited_cells_compared'])
def run(confirm):
 results=dict(main=pdf('main'),SI=pdf('SI'),workbook=workbook(),visual_review_completed=confirm,
  visual_review_pages={'main':list(range(1,22)),'SI':list(range(1,22))}if confirm else{},
  review_scope='Page layout, clipping, typography, figures, captions, tables and references; numeric statements additionally checked against source-derived tables',
  no_new_provider_PDF_body_redistributed=True)
 (ROOT/'metadata/deliverable_QA_F13.json').write_text(json.dumps(results,indent=2)+'\n');print(json.dumps(results,indent=2))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--confirm-visual-review',action='store_true');run(p.parse_args().confirm_visual_review)

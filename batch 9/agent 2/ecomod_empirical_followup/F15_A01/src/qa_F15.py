#!/usr/bin/env python3
"""PDF, source/cross-reference and workbook QA; visual confirmation is separate."""
from pathlib import Path
import argparse,json,re,hashlib
import pymupdf
from PIL import Image,ImageDraw
from build_F15 import ROOT,CACHE,expand,require
DECL='Arena.ai Agent Mode was used to assist with computational methods and literature review.'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def pdf(kind):
 p=ROOT/f'integrated_F15_A01_{kind}.pdf';d=pymupdf.open(p);texts=[];bad=[];links=[];fonts=set();sheets=[]
 for i,page in enumerate(d):
  texts.append(page.get_text());links.extend(l.get('uri','')for l in page.get_links());fonts.update(f[0]for f in page.get_fonts(full=True))
  for block in page.get_text('dict')['blocks']:
   for line in block.get('lines',[]):
    for span in line['spans']:
     x0,y0,x1,y1=span['bbox']
     if min(x0,y0)<-.5 or x1>page.rect.width+.5 or y1>page.rect.height+.5:bad.append(dict(page=i+1,text=span['text'],bbox=span['bbox']))
 checks=[]
 for xref in fonts:
  ok=bool(d.extract_font(xref)[3]);method='font program'
  if not ok:
   obj=d.xref_object(xref);m=re.search(r'/CharProcs\s+(\d+)\s+0\s+R',obj)
   if '/Subtype /Type3'in obj and m:
    refs=re.findall(r'(\d+)\s+0\s+R',d.xref_object(int(m[1])));ok=bool(refs)and all(bool(d.xref_stream(int(r)))for r in refs);method='Type3 embedded CharProcs'
  checks.append(dict(xref=xref,embedded=ok,method=method))
 require(not bad,'PDF clipping '+kind);require(all(r['embedded']for r in checks),'Unembedded font '+kind)
 norm=' '.join(' '.join(texts).split());require(any('orcid.org/0000-0002-0019-1842'in u for u in links),'ORCID link')
 require(all(len(t)>400 for t in texts),'Unexpected near-blank page')
 if kind=='main':
  require(DECL in norm,'AI declaration')
  for value in ['17.639','38.918','104','296','634','183','68','3.303','17.293','136.251']:require(value in norm,'Key result missing '+value)
 layout=CACHE/'layout';layout.mkdir(parents=True,exist_ok=True)
 for start in range(0,len(d),6):
  tiles=[]
  for i in range(start,min(start+6,len(d))):
   pix=d[i].get_pixmap(matrix=pymupdf.Matrix(1.2,1.2));im=Image.frombytes('RGB',(pix.width,pix.height),pix.samples);im.thumbnail((650,920));tile=Image.new('RGB',(680,960),'#dedede');tile.paste(im,((680-im.width)//2,30));ImageDraw.Draw(tile).text((12,8),f'{kind} | Page {i+1}',fill='black');tiles.append(tile)
  canvas=Image.new('RGB',(1360,960*((len(tiles)+1)//2)),'#dedede')
  for j,im in enumerate(tiles):canvas.paste(im,(680*(j%2),960*(j//2)))
  name=f'{kind}_{start+1:02}_{min(start+6,len(d)):02}.jpg';canvas.save(layout/name,quality=90);sheets.append(name)
 r=dict(file=p.name,sha256=sha(p),pages=len(d),page_text_characters=[len(t)for t in texts],text_outside_page_bounds=bad,all_fonts_embedded=True,font_checks=sorted(checks,key=lambda r:r['xref']),ORCID_hyperlink=True,AI_declaration=DECL in norm,contact_sheets=sheets)
 d.close();return r

def run(visual=False):
 main=(ROOT/'integrated_F15_A01_main.tex').read_text();full=expand(ROOT/'integrated_F15_A01_main.tex');si=expand(ROOT/'integrated_F15_A01_SI.tex')
 require(full.count('\\begin{figure}')==6 and full.count('\\begin{table}')==2,'Main figure/table allocation')
 results=main.split('\\section{Results}')[1].split('\\section{Discussion}')[0];require(results.count('\\subsection{')==5,'Five result sections')
 require('\\section{Discussion}'not in si and 'Subsequent ecological comparisons and their admission requirements'not in si and 'Primary national AGB target and remaining evidence requirements'not in si,'Standalone discussion/work plan remains in SI')
 abstract=re.search(r'\\begin\{abstract\}(.*?)\\end\{abstract\}',main,re.S)[1];keywords=re.search(r'\\textbf\{Keywords:\}([^\n]+)',main)[1].split(';');require(len(abstract.split())<=250 and len(keywords)==7,'Abstract or keyword count')
 linkage=json.loads((ROOT/'metadata/SI_linkage_F15.json').read_text());require(linkage['every_SI_figure_and_table_cited_in_main']and len(linkage['labels'])==27,'SI linkage')
 q=dict(main=pdf('main'),SI=pdf('SI'),main_figures=6,main_tables=2,main_result_sections=5,SI_figures=2,SI_tables=25,all_SI_items_explicitly_cited=True,abstract_whitespace_words=len(abstract.split()),keywords=7,visual_review_completed=visual)
 q['visual_review_pages']={kind:list(range(1,q[kind]['pages']+1))for kind in ['main','SI']}if visual else{}
 q['workbook']=json.loads((ROOT/'metadata/workbook_QA_F15.json').read_text());require(q['workbook']['sha256']==sha(ROOT/q['workbook']['file']),'Stale workbook QA')
 (ROOT/'metadata/deliverable_QA_F15.json').write_text(json.dumps(q,indent=2)+'\n')
 print(json.dumps({k:v for k,v in q.items()if k not in ['main','SI']}|dict(main_pages=q['main']['pages'],SI_pages=q['SI']['pages']),indent=2))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--confirm-visual-review',action='store_true');run(p.parse_args().confirm_visual_review)

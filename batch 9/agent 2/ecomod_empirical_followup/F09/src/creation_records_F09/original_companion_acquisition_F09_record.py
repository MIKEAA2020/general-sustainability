from pathlib import Path
import requests,json,hashlib
from pypdf import PdfReader
P=Path('/home/user/.cache/cci_companion_R02');rows=json.loads((P/'heads.json').read_text());names=['E3UB','PVIR','PVP','ADPC']
for name,row in zip(names,rows):
 size=int(row['bytes_header'])
 if size>25000000:raise ValueError('Download cap')
 path=P/(name+'.pdf');n=0;h=hashlib.sha256()
 with requests.get(row['final_url'],headers={'If-Match':row['etag'],'Accept-Encoding':'identity'},stream=True,timeout=(20,90))as r:
  if r.status_code!=200 or r.headers.get('ETag')!=row['etag']:raise ValueError('Source identity mismatch')
  with path.open('wb')as f:
   for b in r.iter_content(262144):
    n+=len(b)
    if n>min(size,25000000):raise ValueError('Download cap')
    h.update(b);f.write(b)
 if n!=size:raise ValueError('Length mismatch')
 reader=PdfReader(path);pages={str(i):p.extract_text()for i,p in enumerate(reader.pages,1)};(P/(name+'_pages.json')).write_text(json.dumps(pages,ensure_ascii=False,indent=2));row.update({'key':name,'sha256':h.hexdigest(),'bytes':n,'pages':len(pages),'full_download_success':True,'text_extracted':True});print(name,n,len(pages),'pages\n',pages['1'][:1500],flush=True)
 for i,t in pages.items():
  if 'Table of Contents' in t or 'Table\tof\tContents' in t or 'Contents' in t and int(i)<8:print('CONTENTS',i,t[:18000],flush=True)
(P/'registry.json').write_text(json.dumps({'date':'2026-10-29','source_scope':'Four full source downloads under standing 25MB per-document transfer guard; detailed reading scope recorded separately','acquisition_note':'If-Match targets resolved media URL: the /documents/ redirect endpoint has its own ETag and returned 412 when compared against the final PDF ETag. No source was unpinned.','documents':rows},indent=2)+'\n')

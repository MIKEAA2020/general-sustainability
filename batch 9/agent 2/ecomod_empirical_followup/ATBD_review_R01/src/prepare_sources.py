"""Hash-check uploaded/release PDF chunks and extract a page-addressed review corpus."""
from pathlib import Path
import json,re,hashlib,requests,argparse
from pypdf import PdfReader
P=Path(__file__).resolve().parents[1]
def run(cache,uploads,release):
 cache.mkdir(parents=True,exist_ok=True);assets=json.loads(release.read_text());rows=[];pages={}
 for a in assets['assets']:
  name=a['name'];m=re.fullmatch(r'(\d{3})-(\d{3})\.pdf',name)
  if not m:continue
  start,end=map(int,m.groups());path=uploads/name;origin='user upload'
  if not path.exists():
   origin='release asset download';path=cache/name
   if not path.exists():
    if a['size']>25000000:raise ValueError('Per-asset 25 MB cap exceeded')
    total=0
    with requests.get(a['browser_download_url'],stream=True,timeout=(20,90))as r:
     r.raise_for_status()
     try:
      with path.open('wb')as f:
       for b in r.iter_content(262144):
        total+=len(b)
        if total>min(a['size'],25000000):raise ValueError('Transfer cap exceeded')
        f.write(b)
     except Exception:
      path.unlink(missing_ok=True);raise
  b=path.read_bytes();h=hashlib.sha256(b).hexdigest()
  if len(b)!=a['size']or 'sha256:'+h!=a['digest']:raise ValueError('Release digest/length mismatch '+name)
  reader=PdfReader(path)
  if len(reader.pages)!=end-start+1:raise ValueError('Chunk page count mismatch')
  rows.append({'filename':name,'start_page':start,'end_page':end,'page_count':len(reader.pages),'bytes':len(b),'sha256':h,'release_asset_id':a['id'],'release_url':a['browser_download_url'],'obtained_from':origin})
  for i,page in enumerate(reader.pages,start):
   if i in pages:raise ValueError('Overlapping page ranges')
   pages[i]=page.extract_text()
 if sorted(pages)!=list(range(1,139)):raise ValueError('Incomplete 138-page source coverage')
 (P/'metadata/source_registry.json').write_text(json.dumps({'document':'ESA CCI Biomass Algorithm Theoretical Basis Document v7.0','document_reference':'CCI_BIOMASS_ATBD_V7','title_page_last_modified':'2025-12-17','release_tag':assets['tag_name'],'release_url':assets['html_url'],'source_scope':'All 138 PDF pages available through 12 release-matched chunks; every chunk SHA-256 matched against the release asset digest. No full original-PDF hash equivalence is implied by independently split/reencoded chunks.','raw_PDFs_redistributed':False,'chunks':rows},indent=2)+'\n')
 (cache/'pages.json').write_text(json.dumps(pages,ensure_ascii=False,indent=2));(cache/'all_pages.txt').write_text('\n\n'.join(f'===== PDF PAGE {i} =====\n{pages[i]}'for i in sorted(pages)));(P/'metadata/source_coverage.json').write_text(json.dumps({'page_numbers':sorted(pages),'pages_available':len(pages),'missing_pages':[],'pages_with_text':sum(bool(v.strip())for v in pages.values()),'extraction_not_full_visual_review':True},indent=2)+'\n');print('Verified all 12 chunks; 138 PDF pages; missing pages recovered from release.',flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--cache',type=Path,required=True);p.add_argument('--uploads',type=Path,required=True);p.add_argument('--release',type=Path,required=True);a=p.parse_args();run(a.cache,a.uploads,a.release)

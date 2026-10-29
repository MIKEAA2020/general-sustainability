"""Optional text-only equivalence check using strict bounded HTTP ranges, not a full PDF download."""
from pathlib import Path
import io,requests,re,json,hashlib,argparse,logging
from pypdf import PdfReader
P=Path(__file__).resolve().parents[1]
class RangeReader(io.RawIOBase):
 def __init__(self,url,total,etag,cap=25000000):self.url=url;self.total=total;self.etag=etag;self.cap=cap;self.pos=0;self.blocks={};self.bytes=0;self.cap_encountered=False;self.s=requests.Session()
 def readable(self):return True
 def seekable(self):return True
 def tell(self):return self.pos
 def seek(self,offset,whence=0):
  pos=offset if whence==0 else self.pos+offset if whence==1 else self.total+offset
  if pos<0:raise ValueError('Negative seek')
  self.pos=pos;return pos
 def read(self,size=-1):
  size=max(0,self.total-self.pos)if size<0 else min(size,max(0,self.total-self.pos))
  if size>self.cap:raise ValueError('Oversized PDF read rejected')
  start=self.pos;end=start+size;out=[]
  for k in range(start//65536,(end-1)//65536+1)if size else []:
   if k not in self.blocks:
    lo=k*65536;hi=min(lo+65535,self.total-1);n=hi-lo+1
    if self.bytes+n>self.cap:self.cap_encountered=True;raise ValueError('25 MB distinct range cap reached')
    with self.s.get(self.url,headers={'Range':f'bytes={lo}-{hi}','If-Match':self.etag,'Accept-Encoding':'identity'},stream=True,timeout=(20,90))as r:
     if r.status_code!=206 or r.headers.get('Content-Range')!=f'bytes {lo}-{hi}/{self.total}'or r.headers.get('ETag')!=self.etag:raise ValueError('Range/source identity mismatch')
     b=bytearray()
     for block in r.iter_content(65536):
      if len(b)+len(block)>n:raise ValueError('Range response exceeded request')
      b.extend(block)
     if len(b)!=n:raise ValueError('Short range response')
    self.blocks[k]=bytes(b);self.bytes+=n
   b=self.blocks[k];lo=max(start,k*65536)-k*65536;hi=min(end,(k+1)*65536)-k*65536;out.append(b[lo:hi])
  self.pos=end;return b''.join(out)
def run(cache):
 probe=json.loads((P/'metadata/official_range_probe.json').read_text());total=int(probe['content_range'].split('/')[-1]);r=RangeReader(probe['url'],total,probe['etag']);expected=json.loads((cache/'pages.json').read_text());report={'scope':'Text-only equivalence of published original PDF and supplied/release chunks under unchanged 25 MB range cap; no whole-file hash or image equivalence asserted','url':probe['url'],'object_bytes':total,'etag':probe['etag'],'range_cap':r.cap,'whole_file_downloaded':False,'images_compared':False,'page_text_comparisons':[]}
 try:
  reader=PdfReader(r);report['official_page_count']=len(reader.pages)
  if len(reader.pages)!=138:raise ValueError('Unexpected official page count')
  for i,page in enumerate(reader.pages,1):
   t=' '.join(page.extract_text().split());old=' '.join(expected[str(i)].split());report['page_text_comparisons'].append({'page':i,'same_whitespace_normalized_text':t==old,'official_text_sha256':hashlib.sha256(t.encode()).hexdigest(),'chunk_text_sha256':hashlib.sha256(old.encode()).hexdigest()})
   if i%20==0:print('Official PDF text checked through page',i,'distinct bytes',r.bytes,flush=True)
  report['completed']=True
 except Exception as e:report['completed']=False;report['failure_type']=type(e).__name__;report['failure_reason']=str(e)
 report['all_138_extracted_page_texts_match']=len(report['page_text_comparisons'])==138 and all(x['same_whitespace_normalized_text']for x in report['page_text_comparisons']);report['range_cap_encountered_in_optional_object_reads']=r.cap_encountered;report['parser_limitations']='Malformed/zero xref offsets and optional XObject errors may be reported by pypdf; extracted-text equality does not establish complete PDF/object/image equivalence.';report['full_original_PDF_sha256']=None;report['distinct_bytes_accessed']=r.bytes;report['blocks']=[{'first_byte':k*65536,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}for k,b in sorted(r.blocks.items())];(P/'metadata/official_text_comparison.json').write_text(json.dumps(report,indent=2)+'\n');print('Official text comparison completed:',report['completed'],'pages',len(report['page_text_comparisons']),'bytes',r.bytes,flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--cache',type=Path,required=True);a=p.parse_args();run(a.cache)

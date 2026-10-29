"""Guarded seekable reference ZIP reader. Identity scope is explicitly partial.
No full-archive hash claim: require immutable version URL, size, range hashes,
metadata checksum consistency and selected-member CRC. Range responses do not
return an ETag or Last-Modified; see the frozen protocol and acquisition report.
"""
import io,json,hashlib
from pathlib import Path
import requests
class ReferenceRanges(io.RawIOBase):
 def __init__(self,url,size,modified,cache,cap=25000000,block=65536):
  self.url,self.size,self.modified,self.cache=url,size,modified,Path(cache);self.cache.mkdir(parents=True,exist_ok=True);self.cap,self.block,self.position=cap,block,0;self.blocks={};self.transferred=0;self.network_bytes=0
 def readable(self):return True
 def seekable(self):return True
 def tell(self):return self.position
 def seek(self,offset,whence=0):
  p=offset if whence==0 else self.position+offset if whence==1 else self.size+offset
  if p<0:raise ValueError('Negative seek')
  self.position=p;return p
 def fetch(self,index):
  if index in self.blocks:return self.blocks[index]
  start=index*self.block;end=min(start+self.block,self.size)-1;expected=end-start+1
  if expected<=0:return b''
  if self.transferred+expected>self.cap:raise ValueError('Cumulative reference transfer cap')
  dest=self.cache/f'{start}_{end}.bin';meta=dest.with_suffix('.json')
  if dest.exists()!=meta.exists():raise ValueError('Incomplete cached range')
  if dest.exists():
   b=dest.read_bytes();m=json.loads(meta.read_text())
   if m['url']!=self.url or m['modified_HEAD']!=self.modified or m['sha256']!=hashlib.sha256(b).hexdigest():raise ValueError('Range identity mismatch')
  else:
   with requests.get(self.url,headers={'Range':f'bytes={start}-{end}','If-Unmodified-Since':self.modified,'Accept-Encoding':'identity'},stream=True,timeout=(20,90))as r:
    if r.status_code!=206 or r.headers.get('Content-Range')!=f'bytes {start}-{end}/{self.size}':raise ValueError('Range rejected/ignored; no full body read')
    buf=bytearray()
    for chunk in r.iter_content(65536):
     buf.extend(chunk)
     if len(buf)>expected:raise ValueError('Range exceeded requested length')
   b=bytes(buf);self.network_bytes+=len(b)
   m={'url':self.url,'modified_HEAD':self.modified,'start':start,'end':end,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'whole_archive_hash_verified':False};dest.write_bytes(b);meta.write_text(json.dumps(m,indent=2)+'\n')
  if len(b)!=expected:raise ValueError('Truncated range')
  self.transferred+=len(b);self.blocks[index]=b;return b
 def read(self,n=-1):
  if n<0:n=self.size-self.position
  if n>self.cap:raise ValueError('Unbounded read prohibited')
  end=min(self.position+n,self.size);out=bytearray()
  while self.position<end:
   index=self.position//self.block;b=self.fetch(index);off=self.position-index*self.block;count=min(len(b)-off,end-self.position)
   if count<=0:raise ValueError('Invalid range progress')
   out.extend(b[off:off+count]);self.position+=count
  return bytes(out)
 def readinto(self,b):
  d=self.read(len(b));b[:len(d)]=d;return len(d)
 def prefetch(self,first,last):
  """Batch adjacent fixed-size blocks in one bounded HTTP Range request."""
  missing=[i for i in range(first,last+1)if i not in self.blocks and not (self.cache/f'{i*self.block}_{min((i+1)*self.block,self.size)-1}.bin').exists()]
  runs=[]
  for i in missing:
   if runs and i==runs[-1][-1]+1:runs[-1].append(i)
   else:runs.append([i])
  for run in runs:
   start=run[0]*self.block;end=min((run[-1]+1)*self.block,self.size)-1;expected=end-start+1
   if self.transferred+expected>self.cap:raise ValueError('Cumulative prefetch cap')
   with requests.get(self.url,headers={'Range':f'bytes={start}-{end}','If-Unmodified-Since':self.modified,'Accept-Encoding':'identity'},stream=True,timeout=(20,120))as r:
    if r.status_code!=206 or r.headers.get('Content-Range')!=f'bytes {start}-{end}/{self.size}':raise ValueError('Batch range rejected before body')
    out=bytearray()
    for chunk in r.iter_content(262144):
     out.extend(chunk)
     if len(out)>expected:raise ValueError('Batch range overflow')
   if len(out)!=expected:raise ValueError('Truncated batch range')
   self.network_bytes+=len(out)
   for i in run:
    a=i*self.block;b=min((i+1)*self.block,self.size)-1;chunk=bytes(out[a-start:b-start+1]);m={'url':self.url,'modified_HEAD':self.modified,'start':a,'end':b,'bytes':len(chunk),'sha256':hashlib.sha256(chunk).hexdigest(),'whole_archive_hash_verified':False};dest=self.cache/f'{a}_{b}.bin';dest.write_bytes(chunk);dest.with_suffix('.json').write_text(json.dumps(m,indent=2)+'\n');self.blocks[i]=chunk;self.transferred+=len(chunk)

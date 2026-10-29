"""Seekable, generation-pinned HTTP range reader with hard transfer limits.
Rejects a 200 response to a Range request before reading a raster body. Cached
blocks are checksummed. This does not download a whole country/global raster.
"""
import io,re,json,hashlib
from pathlib import Path
import requests

class RangeReader(io.RawIOBase):
    def __init__(self,url,size,etag,cache,cap=25000000,block_size=65536):
        self.url=url;self.size=int(size);self.etag=etag;self.cache=Path(cache);self.cache.mkdir(parents=True,exist_ok=True);self.cap=cap;self.block_size=block_size;self.position=0;self.transferred=0;self.blocks={};self.session=requests.Session();self.network_bytes=0
    def readable(self):return True
    def seekable(self):return True
    def tell(self):return self.position
    def seek(self,offset,whence=0):
        p=offset if whence==0 else self.position+offset if whence==1 else self.size+offset
        if p<0:raise ValueError('Negative seek')
        self.position=p;return p
    def _block(self,index):
        if index in self.blocks:return self.blocks[index][0]
        start=index*self.block_size;end=min(self.size,start+self.block_size)-1
        if start>=self.size:return b''
        expected=end-start+1
        if self.transferred+expected>self.cap:raise ValueError('Bounded transfer limit exceeded')
        p=self.cache/f'{start:012d}_{end:012d}.bin';m=p.with_suffix('.json')
        if p.exists() != m.exists():raise ValueError('Incomplete cached range or missing hash')
        if p.exists() and m.exists():
            b=p.read_bytes();rec=json.loads(m.read_text());
            if not (rec['url']==self.url and rec['etag']==self.etag and rec['sha256']==hashlib.sha256(b).hexdigest()):raise ValueError('Cached source identity changed')
        else:
            r=self.session.get(self.url,headers={'Range':f'bytes={start}-{end}','If-Match':self.etag,'Accept-Encoding':'identity'},stream=True,timeout=(20,60))
            if r.status_code!=206:r.close();raise ValueError(f'Range request rejected or ignored: HTTP {r.status_code}')
            if r.headers.get('Content-Range')!=f'bytes {start}-{end}/{self.size}':r.close();raise ValueError('Unexpected source range or object length')
            if r.headers.get('ETag')!=self.etag:r.close();raise ValueError('Source object ETag changed')
            buf=bytearray()
            for chunk in r.iter_content(65536):
                buf.extend(chunk)
                if len(buf)>expected:r.close();raise ValueError('Range response exceeded declared length')
            r.close();b=bytes(buf);self.network_bytes+=len(b);rec=dict(url=self.url,etag=self.etag,start=start,end=end,bytes=len(b),sha256=hashlib.sha256(b).hexdigest());p.write_bytes(b);m.write_text(json.dumps(rec,indent=2)+'\n')
        if len(b)!=expected:raise ValueError('Truncated range response')
        self.transferred+=len(b);self.blocks[index]=(b,rec);return b
    def read(self,n=-1):
        if n<0:n=self.size-self.position
        if n>self.cap:raise ValueError('Unbounded TIFF read prohibited')
        end=min(self.size,self.position+n);out=bytearray()
        while self.position<end:
            i=self.position//self.block_size;block=self._block(i);off=self.position-i*self.block_size;n=min(len(block)-off,end-self.position);out.extend(block[off:off+n]);self.position+=n
        return bytes(out)
    def readinto(self,b):
        data=self.read(len(b));b[:len(data)]=data;return len(data)
    def receipts(self):return [self.blocks[i][1]for i in sorted(self.blocks)]
    def close(self):
        self.session.close();super().close()

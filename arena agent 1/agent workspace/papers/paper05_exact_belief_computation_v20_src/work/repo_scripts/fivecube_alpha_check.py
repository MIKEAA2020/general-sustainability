#!/usr/bin/env python3
"""Independent, vectorized full enumeration of 4- and 5-cube 4-step alpha masks.
Run python3 alpha_check.py. Requires NumPy; uses exact integer tenths.
Prints full 16-level counts and checks reproductions/counterexamples.
"""
import numpy as np
from itertools import product
v=np.asarray(list(product((1,-1),repeat=5)), dtype=np.int8)
d=np.asarray([[-5+2*sum(int(a[i]*th[i]) for i in range(5)) for th in v] for a in v]+[[-5]*32],dtype=np.int16)
assert d.shape==(33,32) and d[0,0]==5 and d[0,1]==1
seq=np.indices((33,)*4,dtype=np.uint8).reshape(4,-1)
assert seq.shape==(4,33**4)
counts=[]
for L in range(16):
  stock=np.full((33**4,32),L,dtype=np.int16)
  alive=np.ones((33**4,32),dtype=bool)
  for t in range(4):
    stock+=d[seq[t]]
    alive &= stock>=0
  masks=np.packbits(alive,axis=1)
  # Four bytes per 32-bit outcome mask, unique dedup exactly.
  counts.append(len(np.unique(masks.view(np.dtype(('V',4))).reshape(-1))))
print('five-cube L=0..15 4-step distinct outcome masks:',counts)
assert counts[:3]==[945]*3 and counts[15]==11145
assert counts[12]==14649 and counts[13]==15929
print('FALSE ceiling: at L=13 (z0=2.3), 15929 > published 11145 max')
# Cross-check with the four-cube, using exactly the source v13 simulation
# rule: keep each trajectory above the floor at every step.
m=4
v4=np.asarray(list(product((1,-1),repeat=m)),dtype=np.int8)
d4=np.asarray([[-5+2*sum(int(a[i]*th[i]) for i in range(m)) for th in v4]
               for a in v4]+[[-5]*16],dtype=np.int16)
seq4=np.indices((17,)*4,dtype=np.uint8).reshape(4,-1)
c4=[]
for L in range(16):
  stock=np.full((17**4,16),L,dtype=np.int16)
  alive=np.ones((17**4,16),dtype=bool)
  for t in range(4):
    stock+=d4[seq4[t]]
    alive &= stock>=0
  masks=np.packbits(alive,axis=1)
  c4.append(len(np.unique(masks.view(np.dtype(('V',2))).reshape(-1))))
print('four-cube L=0..15 4-step distinct outcome masks:',c4)
assert c4[12]==857 and c4[15]==545
print('FALSE ceiling: at L=12 (z0=2.2), 857 > published 545 max; z0=2.5 does give 545')

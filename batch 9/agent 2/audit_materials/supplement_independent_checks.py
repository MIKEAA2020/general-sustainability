"""Checks for the v76 SI audit. Rational log enclosures are certified;
mpmath root estimates are numerical corroboration, not global certificates.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json, re
import mpmath as mp

def log_interval(x,n=120):
    x=F(x)
    if x<1:
        lo,hi=log_interval(1/x,n)
        return -hi,-lo
    z=(x-1)/(x+1)
    partial=2*sum((z**(2*k+1)/F(2*k+1) for k in range(n)),F(0))
    tail=2*z**(2*n+1)/(F(2*n+1)*(1-z*z))
    return partial,partial+tail

def mul(a,b):
    p=[x*y for x,y in product(a,b)]
    return min(p),max(p)

def geom_certificate(a,b):
    A,B,C,D=map(log_interval,[a-1,b+1,a+1,b-1])
    ad,bc=mul(A,D),mul(B,C)
    margin=(bc[0]-ad[1],bc[1]-ad[0])
    assert margin[0]>0 or margin[1]<0
    return {'s':[str(a),str(b)],'verdict':'accept' if margin[0]>0 else 'reject',
            'BC_minus_AD_interval_float':[float(x) for x in margin],
            'certificate_method':'120-term rational artanh-series with geometric tail bound'}

certs=[geom_certificate(F(707,500),F(707,500)),geom_certificate(F(607,500),F(807,500)),geom_certificate(F(5,4),F(3,2)),geom_certificate(F(5,4),F(7,4))]
mp.mp.dps=70
r=lambda s:-mp.log(s-1)/mp.log(s+1)
h=lambda s:mp.diff(r,s)/r(s)
a,b=mp.findroot(lambda a,b:(r(a)*r(b)-1,h(a)-h(b)),(mp.mpf('1.15'),mp.mpf('1.67')))
assert mp.mpf('1.14796785390')<a<mp.mpf('1.14796785398')
assert mp.mpf('1.67460191085')<b<mp.mpf('1.67460191093')
assert mp.mpf('2.82256976476')<a+b<mp.mpf('2.82256976491')

# Verify the harmonic cover polynomial reduces to the stated circle on (1,2)^2.
for i,j in product(range(1,20),repeat=2):
    s,t=1+F(i,20),1+F(j,20)
    A,B,C,D=1/(s-1),1/(t+1),1/(s+1),1/(t-1)
    power_cover=C*(B-1)+A*(1-D)-(B-D) >= 0
    circle=(2*s-1)**2+(2*t-1)**2>=10
    assert power_cover==circle

si=Path('/home/user/uploads/paper06_assessment_separation_v76_supplementary.txt').read_text()
labels=re.findall(r'\\label\{([^}]+)\}',si)
refs=re.findall(r'\\(?:ref|eqref)\{([^}]+)\}',si)
result={
  'certified_geometric_witnesses':certs,
  'numerical_tangencies_not_global_proof':{'a':str(a),'b':str(b),'t_star':str(a+b),'inside_reported_brackets':True},
  'harmonic_circle_checks':361,
  'S4_omitted_coordinate_cut_counterexample':{'x':'1/2','s1':'1/10','s2':'39/20','delta':'1/4','sum_requirement_passes':F(1,10)+F(39,20)>=F(3,2)+2*F(1,4),'coordinate_requirement_fails':F(1,10)<F(1,4)},
  'missing_internal_labels':sorted(set(refs)-set(labels)),
  'nested_example_error':'0 belongs to [0,1/k] for every positive integer k; intersection is not empty.'
}
print(json.dumps(result,indent=2))
Path(__file__).with_name('supplement_independent_checks_results.json').write_text(json.dumps(result,indent=2)+'\n')

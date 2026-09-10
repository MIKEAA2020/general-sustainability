import sympy as sp
w = sp.symbols('w', positive=True)
c = -1/(4*w**2+1)
s = (200*w**3+48*w)/(4*w**2+1)
eq = sp.expand(sp.together(c**2+s**2-1))
print("tau_m=0  sin^2+cos^2-1 =", sp.factor(sp.simplify(eq)))
print("numerator simplified:", sp.expand(sp.numer(sp.together(eq))))

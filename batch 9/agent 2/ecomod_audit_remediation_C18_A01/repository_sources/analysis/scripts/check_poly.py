import sympy as sp
w = sp.symbols('w', positive=True)
# Constants scenario A
a11 = sp.Rational(-1,2)   # -0.5
r   = sp.Rational(1,50)   # 0.02
gea = sp.Rational(1,100)  # gamma*e*a21 = 1*1*0.01

# ---- tau_p = 0 case: lambda = i w ----
# char: lam^2 - a11 lam + r(lam - a11) + gea*exp(-lam*tau_m) = 0
# re: -w^2 - a11*r + gea*cos = 0  => cos = (w^2 + a11*r)/gea  ... check sign
# Actually char: lam^2 - a11 lam + r lam - r a11 + gea e^{-lam tau_m}
# Real(w): -w^2 + r*a11*? ; let's just do it generally with sympy
lam = sp.I*w
expr = lam**2 - a11*lam + r*(lam - a11) + gea*sp.exp(-lam)  # set tau_m via exp(-i w tau); but we eliminate the exp
# Instead do the sin/cos elimination for tau_p=0:
# char(lam=i w)=0 with tau_p=0:
# -w^2 + (r - a11)*I*w - r*a11 + gea*(cos - I sin)=0
# Real: -w^2 - r*a11 + gea*cos =0  -> cos=(w^2 + r*a11)/gea
# Imag: (r-a11)*w - gea*sin =0 -> sin=(r-a11)*w/gea
cosT = (w**2 + r*a11)/gea
sinT = (r-a11)*w/gea
eq1 = sp.expand(cosT**2 + sinT**2 - 1)
print("tau_p=0  sin^2+cos^2-1 (unscaled):", sp.factor(sp.simplify(eq1)))
print("tau_p=0  simplified:", sp.nsimplify(sp.expand(eq1)))
print("tau_p=0  rational:", sp.nsimplify(sp.expand(sp.together(eq1))))

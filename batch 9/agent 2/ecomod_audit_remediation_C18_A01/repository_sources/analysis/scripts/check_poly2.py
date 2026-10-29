import sympy as sp
w = sp.symbols('w', positive=True)
a11 = sp.Rational(-1,2); r=sp.Rational(1,50); gea=sp.Rational(1,100)
# tau_m = 0 case. lam = i w.
# char: lam^2 - a11 lam + gea + r(lam - a11) e^{-lam tau_p} = 0
# Real part: -w^2 + gea + r*( w*sin - a11*cos ) = 0   (theta = w*tau_p)
# Imag part: -a11*w + r*( w*cos + a11*sin ) = 0
th=w  # theta = w*tau_p; we treat cos(th),sin(th) as unknowns; use sin^2+cos^2=1
c,s=sp.symbols('c s', real=True)
expr_re = -w**2 + gea + r*(w*s - a11*c)
expr_im = -a11*w + r*(w*c + a11*s)
# solve linear system for c,s
sol = sp.solve([sp.expand(expr_re), sp.expand(expr_im)], [c,s], dict=True)
print("solutions:", sol)

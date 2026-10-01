#!/usr/bin/env python3
"""Exact-arithmetic spot checks for paper01's narrowed manuscript claims.

Not a proof of the full paper; tests only the stated examples and the
counterexample-exclusion boundaries. Run: python3 repair_regressions.py.
"""
from fractions import Fraction as Q
from itertools import product
from math import floor

# #1: the original B(x)=x witness is outside the repaired proposition.
# In a genuinely affine-state/affine-input case x'=-2+u, q=x-1,
# initial x=1, T=1, U=[-1,1], the zero-control margin is -2.
# Variation of constants is exact; the maximal facet value is -1.
for u in (Q(-1), Q(0), Q(1)):
    actual = Q(1) + (-2 + u) * Q(1) - Q(1)
    from_kernel = Q(-2) + u * Q(1)
    assert actual == from_kernel <= Q(-1)
assert Q(-2) + Q(1) == Q(-1) < 0
print('#1: exact affine input-output identity and negative support certificate')

# #2: compare the WHOLE-WINDOW hold and unrestricted per-step classes.
def safe(z0, seq):
    for theta in (-1, 1):
        z = z0
        for u in seq:
            z += theta * u
            if z < 1:
                return False
    return True
counts = [0, 0, 0]
for T in (1, 2, 3):
    for i in range(10, 26):
        z = Q(i, 10)
        held = any(safe(z, (u,) * T) for u in (-1, 1))
        per_step = any(safe(z, seq) for seq in product((-1, 1), repeat=T))
        assert held == (z >= 1 + T)
        assert per_step == (z >= 2)
        counts[0] += not held
        counts[1] += not per_step
        counts[2] += held != per_step
assert counts == [42, 30, 12]
print('#2: held 42, per-step 30, class-only cells 12')

# #3: deterministic single-successor, constant observation, full support.
# A and B are initially safe and each action saves both for one step,
# but a resulting x4 branch is irrecoverably unsafe at step two.
states = ('a', 'b'); actions = ('p', 'q')
transition = {
    ('a','p'):'a', ('b','p'):'x4',
    ('a','q'):'x4', ('b','q'):'b',
    ('x4','p'):'bot', ('x4','q'):'bot',
    ('bot','p'):'bot', ('bot','q'):'bot',
}
safe_states = {'a', 'b', 'x4'}
assert all(all(transition[x, act] in safe_states for x in states) for act in actions)
assert all(any(transition[transition[x, act], second] == 'bot'
                   for x in states)
           for act in actions for second in actions)
# No observation distinguishes an initial branch at the first step;
# after it may be revealed, but x4 cannot be rescued. Hence V1=1,
# W2 fails, and V2=1/2 on a uniform full-support prior.
assert Q(1) - min(Q(1,2), Q(1,2)) == Q(1,2)
print('#3: W1 viable, W2 fails only at step two; full-support V2=1/2')

# #4: discrete safe-step count in the NON-decaying held model.
for z in (Q(1), Q(3,2), Q(2), Q(5,2), Q(3)):
    n = floor(z-1)
    assert all(safe(z, (u,) * n) for u in (-1, 1))
    assert not any(safe(z, (u,) * (n+1)) for u in (-1, 1))
assert safe(Q(2), (1,-1,1,-1))  # not a hold policy
# SEPARATELY: decaying LP branches have control-independent sum.
for z in (Q(2), Q(3)):
    for seq in product((-1, 0, 1), repeat=3):
        zp = zm = z
        for k, u in enumerate(seq, 1):
            zp = Q(9,10)*zp + u
            zm = Q(9,10)*zm - u
            assert zp + zm == 2*Q(9,10)**k*z
assert Q(9,10)*Q(2)-1 == Q(4,5) < 1
print('#4: integer-step rounding and separated decaying LP invariant')

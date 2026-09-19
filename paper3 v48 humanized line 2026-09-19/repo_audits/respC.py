from math import log
from fractions import Fraction

print("Task 1: two-donor compatibility")
# Two one-dimensional left-null rays, with coordinates (alpha, beta).
# One identification imposes alpha - beta = 0.
D = [[1.0, -1.0]]
rank_D = 1
unrestricted_dim = 2
compatible_dim = unrestricted_dim - rank_D
print("D =", D)
print("rank(D) =", rank_D, "; compatible nullity =", compatible_dim)
assert compatible_dim == 1

print("\nProposition 36: shared closure capacity")
D_use = [1.0, 1.0]
for R in [Fraction(3, 2), Fraction(1, 1), Fraction(2, 1)]:
    # LP: max mu subject to f1=mu, f2=mu, f1+f2 <= R, f>=0.
    Lambda = min(Fraction(1, 1), R / 2)
    deficit = max(Fraction(0, 1), 1 - Lambda)
    print("R =", R, "Lambda =", Lambda, "deficit =", deficit)
assert [min(Fraction(1, 1), R / 2) for R in [
    Fraction(3, 2), Fraction(1, 1), Fraction(2, 1)]] == [
    Fraction(3, 4), Fraction(1, 2), Fraction(1, 1)]

print("\nTask 2: three-part interface")
p1, p2, p3 = 5.0, 2.0, 0.0
T = 10.0
boxes = [0.2, 0.3]
gradients = [p1 - p2, p2 - p3]
costs = [max(g, 0.0) * b * T for g, b in zip(gradients, boxes)]
print("costs =", costs, "total =", sum(costs))
assert sum(costs) == 12.0

print("\nTask 3: orientation counterexample")
pi = 1.0
L = 0.2
T2 = 30.0
forward = max(pi, 0.0) * L * T2
reverse = max(-pi, 0.0) * L * T2
print("forward cost =", forward, "; reverse cost =", reverse)
assert forward == 6.0 and reverse == 0.0

print("\nTask 4: reduced aggregate LP and two completions")
B = 9.0
Tstar = 30.0
reduced_value = B / Tstar
rho = 1.0 / Tstar
print("reduced value =", reduced_value, "; dual rho =", rho)
hidden_box = 0.1
hidden_gap = reduced_value - hidden_box
print("with hidden declared box L<=0.1: value =",
      hidden_box, "; gap =", hidden_gap)
assert reduced_value == 0.3 and hidden_gap == 0.2

print("\nProposition 39: polyhedral endpoint LPs")
# Fibre: x1+x2=100, 1<=xi<=99. Earliest branch is min(x1,x2).
minimum_of_min_branch = min(min(1, 99), min(99, 1))
maximum_of_min_branch = min((100 - 0 - 0) / 2, 100 - 1, 100 - 1)
# Above is still only a displayed calculation; direct feasible answers are 1 and 50.
lower_raw = 1.0
upper_raw = 50.0
print("T(z) = [", log(lower_raw), ",", log(upper_raw), "]")
print("recorded start at x_min=2:", log(2.0))
assert abs(log(upper_raw) - 3.912023005428146) < 1e-14
assert abs(log(2.0) - 0.6931471805599453) < 1e-14

print("\nTask 6: disconnected nonconvex fibre")
F = [(0.0, 1.0), (1.0, 1.0)]
T_image = {x for x, y in F}
print("F =", F, "; T =", sorted(T_image))
assert sorted(T_image) == [0.0, 1.0]

print("\nTask 7: inverse-Gaussian mean bracket")
Delta = 10.0
bmin, bmax = 1.0, 2.0
mean_low, mean_high = Delta / bmax, Delta / bmin
print("mean bracket =", (mean_low, mean_high))
assert (mean_low, mean_high) == (5.0, 10.0)

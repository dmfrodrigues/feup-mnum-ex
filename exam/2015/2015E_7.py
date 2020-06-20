from math import sin
def f(x): return x**3-10*sin(x)+2.8
l, r = 1.5, 4.2
for i in range(2):
    m = (l+r)/2
    if f(m)*f(l) > 0: l = m
    else            : r = m
print("%.5f \t%.5f"%(l, r))

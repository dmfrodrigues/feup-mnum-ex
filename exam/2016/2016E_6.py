from math import sqrt, exp
def f(x): return sqrt(k**2*exp(2*k*x)+1)
k, a, b, h = 1.5, 0.0, 2.0, 0.5
def trapezium(f, a, h, n):
    ret = 0.0
    for i in range(1, n): ret += f(a+i*h)
    ret *= 2.0
    ret += f(a)+f(a+n*h)
    return ret*h/2.0
def simpson(f, a, h, n):
    ret = 0.0
    for i in range(1, n, 2): ret += f(a+i*h)
    ret *= 2.0
    for i in range(2, n, 2): ret += f(a+i*h)
    ret *= 2.0
    ret += f(a)+f(a+n*h)
    return ret*h/3.0
h0, h1, h2 = h, h/2, h/4
L1t = trapezium(f, a, h0,  4); L1s = simpson(f, a, h0,  4)
L2t = trapezium(f, a, h1,  8); L2s = simpson(f, a, h1,  8)
L3t = trapezium(f, a, h2, 16); L3s = simpson(f, a, h2, 16)
QCt = (L2t-L1t)/(L3t-L2t); QCs = (L2s-L1s)/(L3s-L2s)
et  = (L3t-L2t)/3; es = (L3s-L2s)/15
print("%.5f \t%.5f"%(h0, h0))
print("%.5f \t%.5f"%(h1, h1))
print("%.5f \t%.5f"%(h2, h2))
print("%.5f \t%.5f"%(L1t, L1s))
print("%.5f \t%.5f"%(L2t, L2s))
print("%.5f \t%.5f"%(L3t, L3s))
print("%.5f \t%.5f"%(QCt, QCs))
print("%.5f \t%.5f"%(et , es ))

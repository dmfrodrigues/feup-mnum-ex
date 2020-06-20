def trap(f, a, h, n):
    ret = 0.0
    for i in range(1, n): ret += f(a+i*h)
    ret *= 2.0
    ret += f(a) + f(a+n*h)
    return ret*h/2.0
def simp(f, a, h, n):
    ret = 0.0
    for i in range(1, n, 2): ret += f(a+i*h)
    ret *= 2.0
    for i in range(2, n, 2): ret += f(a+i*h)
    ret *= 2.0
    ret += f(a) + f(a+n*h)
    return ret*h/3.0
from math import sqrt, exp
def f(x): return sqrt(k**2*exp(2*k*x)+1.0)
k, a, b, h = 2.5, 0, 1, 0.125
n = 8
h0, h1, h2 = h, h/2, h/4
I0t = trap(f, a, h0, n  ); I0s = simp(f, a, h0, n  )
I1t = trap(f, a, h1, n*2); I1s = simp(f, a, h1, n*2)
I2t = trap(f, a, h2, n*4); I2s = simp(f, a, h2, n*4)
QCt = (I1t-I0t)/(I2t-I1t); QCs = (I1s-I0s)/(I2s-I1s)
ert = abs((I2t-I1t)/3)   ; ers = abs((I2s-I1s)/3)
print("%.5f \t%.5f"%(h0,h0))
print("%.5f \t%.5f"%(h1,h1))
print("%.5f \t%.5f"%(h2,h2))
print("%.5f \t%.5f"%(I0t,I0s))
print("%.5f \t%.5f"%(I1t,I1s))
print("%.5f \t%.5f"%(I2t,I2s))
print("%.5f \t%.5f"%(QCt,QCs))
print("%.5f \t%.5f"%(ert,ers))

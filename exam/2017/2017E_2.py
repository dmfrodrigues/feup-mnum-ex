import math
def f(x): return math.sqrt(k**2 * math.exp(2*k*x) + 1)
def trapezium(a, h, n, f):
    ret = 0.0
    for i in range(1,n):
        ret += f(a+i*h)
    ret *= 2.0
    ret += f(a) + f(a+n*h)
    return ret * h/2.0
def simpson(a, h, n, f):
    ret = 0.0
    for i in range(1, n, 2):
        ret += f(a+h*i)
    ret *= 2.0
    for i in range(2, n, 2):
        ret += f(a+h*i)
    ret *= 2.0
    ret += f(a)+f(a+h*n)
    return ret * h/3.0
k, a, b, h = 2.5, 0.0, 1.0, 0.125
n = 8; h_, h__ = h/2.0, h/4.0; tL, sL = [0]*4, [0]*4
tL[1] = trapezium(a, h  ,   n, f); sL[1] = simpson(a, h  ,   n, f)
tL[2] = trapezium(a, h_ , 2*n, f); sL[2] = simpson(a, h_ , 2*n, f)
tL[3] = trapezium(a, h__, 4*n, f); sL[3] = simpson(a, h__, 4*n, f)
tQC = (tL[2]-tL[1])/(tL[3]-tL[2]); sQC = (sL[2]-sL[1])/(sL[3]-sL[2])
te  = (tL[3]-tL[2])/3.0; se = (sL[3]-sL[2])/15.0
print("%2.5f \t%2.5f"%(h  , h  ))
print("%2.5f \t%2.5f"%(h_ , h_ ))
print("%2.5f \t%2.5f"%(h__, h__))
for i in range(1,4): print("%2.5f \t%2.5f"%(tL[i], sL[i]))
print("%2.5f \t%2.5f"%(tQC, sQC))
print("%2.5f \t%2.5f"%(te, se))

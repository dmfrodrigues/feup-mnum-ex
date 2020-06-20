from math import sin
def f(t,x):
    return sin(a*x)+sin(b*t)
def rk4(f, t, x, dt):
    d1 = dt*f(t     , x     )
    d2 = dt*f(t+dt/2, x+d1/2)
    d3 = dt*f(t+dt/2, x+d2/2)
    d4 = dt*f(t+dt  , x+d3  )
    return d1/6 + d2/3 + d3/3 + d4/6
def iterate(t0, x0, dt, n):
    ret = [(t0, x0)]
    for _ in range(n):
        t, x = ret[-1][0], ret[-1][1]
        dx = rk4(f, t, x, dt)
        t, x = t+dt, x+dx; ret.append((t, x))
    return ret
a,b,h,t0,x0 = 2.0, 2.0, 0.5, 1.0, 1.0
print("a)")
I3 = iterate(t0, x0, h/4, 4)
for i in range(len(I3)):
    print("%.6f  \t%.6f"%(I3[i][0], I3[i][1]))
print("b)")
S2 = I3[-1][1]
I1 = iterate(t0, x0, h  , 1); S0 = I1[-1][1]
I2 = iterate(t0, x0, h/2, 2); S1 = I2[-1][1]
QC = (S1-S0)/(S2-S1)
print("QC=%.6f"%QC)

def f(u, v):
    return u*(u/2+1)*v**3+(u+5/2)*v**2
def euler(f, u0, v0, h, n):
    u, v = u0, v0
    for _ in range(n):
        du = h
        dv = du*f(u,v)
        u, v = u+du, v+dv
    return (u,v)
u0, v0, h = 1, 0.1, 0.08
S0 = euler(f, u0, v0, h  , 10)
S1 = euler(f, u0, v0, h/2, 20)
S2 = euler(f, u0, v0, h/4, 40)
QC = (S1[1]-S0[1])/(S2[1]-S1[1])
err = S2[1]-S1[1]
print("%.6f  \t%.6f"%(h  , S0[1]))
print("%.6f  \t%.6f"%(h/2, S1[1]))
print("%.6f  \t%.6f"%(h/4, S2[1]))
print("\t\t%.6f"%QC)
print("\t\t%.6f"%err)

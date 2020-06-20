from math import exp
def f1(t, C, T): return  -exp(-b/(T+273))*C          #=C'
def f2(t, C, T): return a*exp(-b/(T+273))*C-b*(T-20) #=T'
a = 15.00000; b =  0.10000; h = 0.25000; dt = h
tv,Cv,Tv=[0]*3,[0]*3,[0]*3; tv[0],Cv[0],Tv[0] = 0.5, 2.00000, 20.00000
print("a) Euler:")
for i in [1,2]:
    t, C, T = tv[i-1], Cv[i-1], Tv[i-1]
    dC = dt*f1(t, C, T); dT = dt*f2(t, C, T)
    tv[i], Cv[i], Tv[i] = t+dt, C+dC, T+dT
for i in [0,1,2]: print("%d\t%.5f\t%.5f\t%.5f"%(i, tv[i], Cv[i], Tv[i]))
print("b) RK4:")
for i in [1,2]:
    t, C, T = tv[i-1], Cv[i-1], Tv[i-1]
    d1C=dt*f1(t     , C      , T      );d1T=dt*f2(t     , C      , T      )
    d2C=dt*f1(t+dt/2, C+d1C/2, T+d1T/2);d2T=dt*f2(t+dt/2, C+d1C/2, T+d1T/2)
    d3C=dt*f1(t+dt/2, C+d2C/2, T+d2T/2);d3T=dt*f2(t+dt/2, C+d2C/2, T+d2T/2)
    d4C=dt*f1(t+dt  , C+d3C  , T+d3T  );d4T=dt*f2(t+dt  , C+d3C  , T+d3T  )
    dC = d1C/6+d2C/3+d3C/3+d4C/6       ;dT = d1T/6+d2T/3+d3T/3+d4T/6
    tv[i], Cv[i], Tv[i] = t+dt, C+dC, T+dT
for i in [0,1,2]: print("%d\t%.5f\t%.5f\t%.5f"%(i, tv[i], Cv[i], Tv[i]))
print("c)")
h0 = h  ; t, C0, T0 = tv[0], Cv[0], Tv[0]
for _ in range(2):t,C0,T0=t+h0,C0+h0*f1(t+h0,C0,T0),T0+h0*f2(t+h0,C0,T0)
h1 = h/2; t, C1, T1 = tv[0], Cv[0], Tv[0]
for _ in range(4):t,C1,T1=t+h1,C1+h1*f1(t+h1,C1,T1),T1+h1*f2(t+h1,C1,T1)
h2 = h/4; t, C2, T2 = tv[0], Cv[0], Tv[0]
for _ in range(8):t,C2,T2=t+h2,C2+h2*f1(t+h2,C2,T2),T2+h2*f2(t+h2,C2,T2)
print("%.5f\t%.5f"%(h1, C1)); print("%.5f\t%.5f"%(h2, C2))
QC = (C1-C0)/(C2-C1); print("%.5f"%QC); err = C2-C1; print("%.5f"%err)
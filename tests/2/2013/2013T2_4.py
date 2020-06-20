from math import exp
def f1(t, C, T): #=C'
    return  -exp(-b/(T+273))*C
def f2(t, C, T):
    return a*exp(-b/(T+273))*C-b*(T-20)
a, b, t0, dt, C0, T0 = 20.0, 0.5, 0.0, 0.2, 2.0, 20.0
print("a)")
t, C, T = t0, C0, T0
print("%.6f  \t%.6f  \t%.6f"%(t, C, T))
for i in [1,2]:
    dC = dt*f1(t, C, T); dT = dt*f2(t, C, T)
    t, C, T = t+dt, C+dC, T+dT
    print("%.6f  \t%.6f  \t%.6f"%(t, C, T))
print("b)")
t, C, T = t0, C0, T0
print("%.6f  \t%.6f  \t%.6f"%(t, C, T))
for i in [1,2]:
    d1C=dt*f1(t     , C      , T      );d1T=dt*f2(t     , C      , T      )
    d2C=dt*f1(t+dt/2, C+d1C/2, T+d1T/2);d2T=dt*f2(t+dt/2, C+d1C/2, T+d1T/2)
    d3C=dt*f1(t+dt/2, C+d2C/2, T+d2T/2);d3T=dt*f2(t+dt/2, C+d2C/2, T+d2T/2)
    d4C=dt*f1(t+dt  , C+d3C  , T+d3T  );d4T=dt*f2(t+dt  , C+d3C  , T+d3T  )
    dC =d1C/6+d2C/3+d3C/3+d4C/6        ;dT =d1T/6+d2T/3+d3T/3+d4T/6
    t, C, T = t+dt, C+dC, T+dT
    print("%.6f  \t%.6f  \t%.6f"%(t, C, T))
print("c)")
t, Ch0, T = t0, C0, T0; h0 = dt  
for _ in range(1): t,Ch0,T=t+h0,Ch0+h0*f1(t,Ch0,T),T+h0*f2(t,Ch0,T)
t, Ch1, T = t0, C0, T0; h1 = dt/2
for _ in range(2): t,Ch1,T=t+h1,Ch1+h1*f1(t,Ch1,T),T+h1*f2(t,Ch1,T)
t, Ch2, T = t0, C0, T0; h2 = dt/4
for _ in range(4): t,Ch2,T=t+h2,Ch2+h2*f1(t,Ch2,T),T+h2*f2(t,Ch2,T)
QC = (Ch1-Ch0)/(Ch2-Ch1)
err2 = (Ch2-Ch1)/3
print("%.5f  \t%.5f"%(h0, Ch0))
print("%.5f  \t%.5f"%(h1, Ch1))
print("\t\t%.5f"%QC)
print("\t\t%.5f"%err2)

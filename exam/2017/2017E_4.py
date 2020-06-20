from math import exp
def fC(t, C, T): return -exp(-b/(T+273.0))*C
def fT(t, C, T): return a*exp(-b/(T+273.0))*C-b*(T-20.0)
t0, C0, T0, a, b = 0.0, 2.5, 25.0, 30.0, 0.5
print("a)")
h, t, C, T = 0.25, t0, C0, T0
print("%d\t%.5f\t%.5f\t%.5f"%(0, t, C, T))
for i in range(1,3):
    dt = h; dC = fC(t, C, T)*dt; dT = fT(t, C, T)*dt
    t, C, T = t+dt, C+dC, T+dT
    print("%d\t%.5f\t%.5f\t%.5f"%(i, t, C, T))
print("b)")
dt, t, C, T = 0.25, t0, C0, T0
print("%d\t%.5f\t%.5f\t%.5f"%(0, t, C, T))
for i in range(1,3):
    d1C=dt*fC(t     , C      , T      );d1T=dt*fT(t     , C      , T      )
    d2C=dt*fC(t+dt/2, C+d1C/2, T+d1T/2);d2T=dt*fT(t+dt/2, C+d1C/2, T+d1T/2)
    d3C=dt*fC(t+dt/2, C+d2C/2, T+d2T/2);d3T=dt*fT(t+dt/2, C+d2C/2, T+d2T/2)
    d4C=dt*fC(t+dt  , C+d3C  , T+d3T  );d4T=dt*fT(t+dt  , C+d3C  , T+d3T  )
    dC = d1C/6+d2C/3+d3C/3+d4C/6; dT = d1T/6+d2T/3+d3T/3+d4T/6
    t, C, T = t+dt, C+dC, T+dT
    print("%d\t%.5f\t%.5f\t%.5f"%(i, t, C, T))
print("c)")
h0, h1, h2 = h, h/2, h/4
t, C, Th0 = t0, C0, T0
for _ in range(2): t,C,Th0 = t+h0, C+h0*fC(t, C, Th0), Th0+h0*fT(t, C, Th0)
t, C, Th1 = t0, C0, T0
for _ in range(4): t,C,Th1 = t+h1, C+h1*fC(t, C, Th1), Th1+h1*fT(t, C, Th1)
t, C, Th2 = t0, C0, T0
for _ in range(8): t,C,Th2 = t+h2, C+h2*fC(t, C, Th2), Th2+h2*fT(t, C, Th2)
QC = (Th1-Th0)/(Th2-Th1)
err = Th2-Th1
print("%.5f \t%.5f"%(h1, Th1))
print("%.5f \t%.5f"%(h2, Th2))
print("\t\t%.5f"%QC)
print("\t\t%.5f"%err)

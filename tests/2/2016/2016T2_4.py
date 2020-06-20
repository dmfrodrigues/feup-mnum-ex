def f(t, T):
    return -0.25*(T-Ta)
Ta, t0, dt, T0 = 42.0, 5.0, 0.4, 10.0
t, T = t0, T0
for i in [1,2]:
    dT = f(t, T)*dt
    t, T = t+dt, T+dT
print("%.5f"%T)
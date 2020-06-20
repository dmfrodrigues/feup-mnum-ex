def f(t, T):
    return -0.25*(T-Ta)
t0, dt, T0, Ta = 1.0, 0.4, 23.0, 45.0
t, T = t0, T0
for i in [1,2]:
    dT = f(t, T)*dt
    t, T = t+dt, T+dT
print("%.5f"%T)
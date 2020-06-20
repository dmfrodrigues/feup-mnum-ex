def fT(t, T): return -0.25*(T-Ta)
t0, T0, Ta, dt = 5.0, 3.0, 37.0, 0.4
t, T = t0, T0
for _ in range(1, 3):
    t, T = t+dt, T+dt*fT(t, T)
print("Resposta: %.5f"%T)
def simpson2(f, dx, dy):
    S0 = f[0][0] + f[0][2] + f[2][0] + f[2][2]
    S1 = f[0][1] + f[1][0] + f[2][1] + f[1][2]
    S2 = f[1][1]
    return (S0+4*S1+16*S2)*dx*dy/9
f = [[1.1, 1.4, 2.6],\
     [2.1, 4.9, 2.2],\
     [6.3, 1.5, 1.2]]
dx = dy = 0.9
integral = simpson2(f, dx, dy)
print("%.5f"%integral)

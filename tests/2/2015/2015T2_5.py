def f1(x, y, z): #=y'
    return z
def f2(x, y, z): #=z'
    return A*z-y
A, B = -7.0, -2.0
x0, h, y0, z0 = 0.0, 0.25, 1.0, 0.0
x, y, z = x0, y0, z0
for i in [1,2]:
    dx = h
    dy = f1(x,y,z)*dx
    dz = f2(x,y,z)*dx
    x, y, z = x+dx, y+dy, z+dz
    print("%.5f\t%.5f\t%.5f"%(x,y,z))

A = 2
def f1(x,y,z):
    return z
def f2(x,y,z):
    return A+x*(x+z)
dx = 0.25
xv, yv, zv = [0]*3, [0]*3, [0]*3
xv[0], yv[0], zv[0] = 1, 1, 0
print("Euler:")
for i in [1,2]:
    x,y,z=xv[i-1],yv[i-1],zv[i-1]
    dy = dx*f1(x,y,z)
    dz = dx*f2(x,y,z)
    xv[i], yv[i], zv[i] = x+dx, y+dy, z+dz
for i in [0,1,2]:
    print("%d\t%.5f\t%.5f"%(i, xv[i], yv[i]))
print("Runge-Kutta de 4a ordem:")
for i in [1,2]:
    x,y,z=xv[i-1],yv[i-1],zv[i-1]
    d1y=dx*f1(x     , y      , z      ); d1z=dx*f2(x     , y      , z      )
    d2y=dx*f1(x+dx/2, y+d1y/2, z+d1z/2); d2z=dx*f2(x+dx/2, y+d1y/2, z+d1z/2)
    d3y=dx*f1(x+dx/2, y+d2y/2, z+d2z/2); d3z=dx*f2(x+dx/2, y+d2y/2, z+d2z/2)
    d4y=dx*f1(x+dx  , y+d3y  , z+d3z  ); d4z=dx*f2(x+dx  , y+d3y  , z+d3z  )
    dy = d1y/6+d2y/3+d3y/3+d4y/6; dz = d1z/6+d2z/3+d3z/3+d4z/6
    xv[i], yv[i], zv[i] = x+dx, y+dy, z+dz
for i in [0,1,2]:
    print("%d\t%.5f\t%.5f"%(i, xv[i], yv[i]))

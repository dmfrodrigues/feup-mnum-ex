def fy(t, y, v): return v
def fv(t, y, v): return A+t*(t+v)
A, h, t0, y0, v0 = 0.5, 0.25, 0.0, 0.0, 1.0
dt = h
print("Metodo de Euler:")
t, y, v = t0, y0, v0
for n in range(3):
    print("%d\t%.5f\t%.5f"%(n, t, y))
    dy = dt*fy(t, y, v)
    dv = dt*fv(t, y, v)
    t, y, v = t+dt, y+dy, v+dv
print("Metodo de Runge-Kutta de 4a ordem:")
t, y, v = t0, y0, v0
for n in range(3):
    print("%d\t%.5f\t%.5f"%(n, t, y))
    d1y=dt*fy(t     , y      , v      );d1v=dt*fv(t     , y      , v      )
    d2y=dt*fy(t+dt/2, y+d1y/2, v+d1v/2);d2v=dt*fv(t+dt/2, y+d1y/2, v+d1v/2)
    d3y=dt*fy(t+dt/2, y+d2y/2, v+d2v/2);d3v=dt*fv(t+dt/2, y+d2y/2, v+d2v/2)
    d4y=dt*fy(t+dt  , y+d3y  , v+d3v  );d4v=dt*fv(t+dt  , y+d3y  , v+d3v  )
    dy = d1y/6 + d2y/3 + d3y/3 + d4y/6 ;dv = d1v/6 + d2v/3 + d3v/3 + d4v/6
    t, y, v = t+dt, y+dy, v+dv

import numpy as np
def f(x):
    return 4*x[0,0]**2+3*x[1,0]**2-4*x[0,0]*x[1,0]+x[0,0]+10
def grad(x):
    return np.matrix([[-4*x[1,0]+14*x[0,0]+1],\
                      [-4*x[0,0]]])
def quadric_h(x):
    return np.matrix([[-x[0,0]],\
                      [-x[1,0]+0.25]])
x1 = np.matrix([[10.0], [10.0]])
f1 = f(x1)
l = 0.001
r = 1.5
for _ in range(20):
    #print("x1=", x1)
    g = grad(x1)
    print("g=", g)
    print("l=", l)
    print("f1=", f1)
    if np.linalg.norm(g) < 0.01: break
    x2 = x1-l*g
    f2 = f(x2)
    if f2 < f1: l *= r; x1, f1 = x2, f2
    else      : l /= r
print(x1)
x1 += quadric_h(x1)
print(x1)

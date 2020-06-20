def w(x): return -1.1*x[0]*x[1]+12*x[1]+7*x[0]**2-8*x[0]
def grad(x): return [-1.1*x[1]+14*x[0]-8, 12-1.1*x[0]]
x0 = [3,1]
l0 = 0.1
x = x0; l = l0
fx = w(x)
for i in range(1,2):
    g = [l*y for y in grad(x)]
    xn = [x[i]-g[i] for i in range(len(x))]
    fxn = w(xn)
    if fxn < fx: x, fx = xn, fxn
    else       : l /= 2
print("Resposta: %.5f"%(fx))
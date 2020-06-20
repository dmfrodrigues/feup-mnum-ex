import math
def g0(x): return (math.exp(x)*(x-1)+11)/(math.exp(x)-1)
def g1(x): return math.exp(x)-11
def g2(x): return math.log(x+11)
def apply(f, x):
    x_prev = x-1
    while x_prev != x:
        x_prev = x
        try   : x = f(x)
        except: return "NaN"
    return x
xi, xf, h = -12, 10, 0.01
x = xi
while x < xf:
    print("x=%s\t%s\t%s\t%s"%(x, apply(g0, x), apply(g1, x), apply(g2,x)))
    x += h

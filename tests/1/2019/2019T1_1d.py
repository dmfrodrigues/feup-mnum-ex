import math
def g0(x): return (math.exp(x)*(x-1)+11)/(math.exp(x)-1)
def g2(x): return math.log(x+11)
err = 0.000000000001
def apply(f, x):
    x_prev = -1000
    i = 0
    while abs(x_prev-x)/x > err:
        i += 1
        x_prev = x
        x = f(x)
    print(x, i)
x = 2.61
apply(g0, x)
apply(g2, x)

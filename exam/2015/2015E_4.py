from math import log
def g(x): return 2*log(2*x)
x0 = 1.1
x = x0
print("%d\t%.4f"%(0, x))
for i in range(1, 2):
    x_prev, x = x, g(x)
    print("%d\t%.4f\t%.4f"%(i, x, x-x_prev))
    
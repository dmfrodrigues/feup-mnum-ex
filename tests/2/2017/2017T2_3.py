import numpy as np
def simpson(y, h):
    n = int((len(y)-1)/2)
    integral = (h/3)*(y[0]+y[2*n]+4*sum([y[i] for i in range(1,len(y)-1,2)])\
                                 +2*sum([y[i] for i in range(2,len(y)-1,2)]))
    return integral
y = [1.04, 0.37, 0.38, 1.49, 1.08, 0.13, 0.64, 0.84, 0.12]
h = 0.25; n = 4
P2 = simpson(y, 0.25); y = [y[i] for i in range(0, len(y), 2)]
P1 = simpson(y, 0.50); y = [y[i] for i in range(0, len(y), 2)]
P0 = simpson(y, 1.00); err = (P2-P1)/15
print("%.4f\n%.4f"%(P2,err))

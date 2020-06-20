def simpson(y, h):
    n = int((len(y)-1)/2)
    ret = y[0] + y[2*n] + 4*sum([y[i] for i in range(1,len(y)-1, 2)])\
                        + 2*sum([y[i] for i in range(2,len(y)-1, 2)])
    return ret * h/3
h, y = 0.25, [0.36, 1.19, 1.32, 0.21, 1.15, 1.39, 0.12, 1.22, 0.60]
S2 = simpson(y, h); y = [y[i] for i in range(0,len(y), 2)]; h *= 2
S1 = simpson(y, h); y = [y[i] for i in range(0,len(y), 2)]; h *= 2
S0 = simpson(y, h); err = (S2-S1)/15
print("%.4f; %.4f"%(S2, err))

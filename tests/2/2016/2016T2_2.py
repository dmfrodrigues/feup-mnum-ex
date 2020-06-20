def simpson(y, h):
    n = int((len(y)-1)/2)
    return h/3*(y[0]+y[2*n]+4*sum([y[i] for i in range(1,len(y)-1,2)])\
                           +2*sum([y[i] for i in range(2,len(y)-1,2)]))
y = [0.18, 0.91, 0.83, 1.23, 0.88, 1.37, 0.80, 1.34, 0.43]
P2 = simpson(y, 0.2); y = [y[i] for i in range(0,len(y),2)]
P1 = simpson(y, 0.4); y = [y[i] for i in range(0,len(y),2)]
P0 = simpson(y, 0.8)
err = (P2-P1)/15
print("%.4f\t%.4f"%(P2, err))
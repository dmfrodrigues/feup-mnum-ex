from math import sqrt, exp
def g(x):
    return sqrt(k*k*exp(2*k*x) + 1)
def trapezium(f, x0, h, n):
    ret = f(x0) + f(x0+n*h) + 2*sum([f(x0+i*h) for i in range(1, n)])
    return ret*h/2
def simpson(f, x0, h, n):
    n = n//2
    ret = f(x0)+f(x0+2*n*h)+4*sum([f(x0+i*h) for i in range(1, 2*n, 2)])\
                           +2*sum([f(x0+i*h) for i in range(2, 2*n, 2)])
    return ret*h/3
k, a = 1.5, 0.0
Lt, Ls = [0]*4, [0]*4
Lt[1] = trapezium(g, a, 0.25  ,  4); Ls[1] = simpson(g, a, 0.25  ,  4)
Lt[2] = trapezium(g, a, 0.125 ,  8); Ls[2] = simpson(g, a, 0.125 ,  8)
Lt[3] = trapezium(g, a, 0.0625, 16); Ls[3] = simpson(g, a, 0.0625, 16)
for i in [1,2,3]: print("%.5f  \t%.5f"%(Lt[i], Ls[i]))
QCt = (Lt[2]-Lt[1])/(Lt[3]-Lt[2]); QCs = (Ls[2]-Ls[1])/(Ls[3]-Ls[2])
print("%.5f  \t%.5f"%(QCt, QCs))
errt = (Lt[3]-Lt[2])/3; errs = (Ls[3]-Ls[2])/15
print("%.5f  \t%.5f"%(errt, errs))

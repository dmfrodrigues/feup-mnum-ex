def f(x): return a*x**7+b*x-c
a, b, c, xe0, xd0 = 1.0, 0.5, 0.5, 0.0, 0.8
xe, xd = xe0, xd0
fe, fd = f(xe), f(xd)
for i in range(4):
    xn = (xe*fd-xd*fe)/(fd-fe)
    fn = f(xn)
    print("%.5f \t%.5f \t%.5f \t%.5f \t%.5f \t%.5f"%(xe,xd,xn,fe,fd,fn))
    if(fn*fe >= 0.0): xe, fe = xn, fn
    else            : xd, fd = xn, fn
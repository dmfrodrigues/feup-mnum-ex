def g(x, m, R):
    return x-x/m+R/(m*x**(m-1))
m = int(input())
R = float(input())
x = max(R,1.0)
i = 0
while i < 100:
    x_ = x
    x = g(x, m, R)
    print("%+.31f"%(x))
    if(x == x_): break
    i = i+1

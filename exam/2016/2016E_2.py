def gh(x,y): return (y**2+(2*x**2+2*a)*y+b)/(4*x*y-1)
def gk(x,y): return (2*x*y**2+x**2+2*b*x+a)/(4*x*y-1)
a, b, x0, y0 = 1.2, 1.0, 1.0, 1.0
x, y = x0, y0
print("%.5f\t%.5f"%(x, y))
for _ in range(1,3):
    x, y = gh(x,y), gk(x,y)
    print("%.5f\t%.5f"%(x, y))

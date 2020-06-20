from math import *

l = log(10)

def J(x,y):
    return 3/l + x -2*y*(4*x-5-y);
def Ah(x,y):
    return -x*y*y+3*x*log(x)/l+x*x-2*y*(-x*y+2*x*x-5*x-1)
def Ak(x,y):
    return (-y+4*x-5)*(-y*y+3*log(x)/l+x)-(3/(l*x)+1)*(-x*y+2*x*x-5*x-1)

def h(x,y):
    return Ah(x,y)/J(x,y)
def k(x,y):
    return Ak(x,y)/J(x,y)

def gx(x,y):
    return x-h(x,y)
def gy(x,y):
    return y-k(x,y)

x = float(input())
y = float(input())
for _ in range(20):
    x_ = x
    y_ = y
    x = gx(x_,y_)
    y = gy(x_,y_)
    print("%.32f %.32f"%(x,y))
    if(x == x_ and y == y_): break
    

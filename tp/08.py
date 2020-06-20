from math import sin, cos, pi
import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return sin(x)

def solution(x):
    return -cos(x)+1

"""
Euler
"""
def euler(Deltax_n, x_n, y_n):
    return Deltax_n*f(x_n,y_n)

def function_euler(xi, xf, yi, h):
    x = np.arange(xi, xf, h)
    yn = yi
    y = [yn]
    for xn in x[1:]:
        Deltay_n = euler(h, xn, yn)
        yn = yn + Deltay_n
        y.append(yn)
    return (x, y)

"""
Runge-kutta de 4a ordem
"""
def rk4(Deltax_n, x_n, y_n):
    delta1 = Deltax_n*f(x_n             ,y_n           )
    delta2 = Deltax_n*f(x_n+Deltax_n/2.0,y_n+delta1/2.0)
    delta3 = Deltax_n*f(x_n+Deltax_n/2.0,y_n+delta2/2.0)
    delta4 = Deltax_n*f(x_n+Deltax_n    ,y_n+delta3    )
    return delta1/6.0 + delta2/3.0 + delta3/3.0 + delta4/6.0

xi = 0.0; xf = 4*pi
yi = 0.0
h = 0.1

x, y_euler = function_euler(xi, xf, yi, h)
P0 = y_euler
P1 = function_euler(xi, xf, yi, h/2)
P1 = P1[1]
P1 = [P1[i] for i in range(0,len(P1), 2)]
P2 = function_euler(xi, xf, yi, h/4)
P2 = P2[1]
P2 = [P2[i] for i in range(0,len(P2), 4)]

sz = min([len(x), len(P0), len(P1), len(P2)])
x = x[:sz]
P0 = P0[:sz]
P1 = P1[:sz]
P2 = P2[:sz]

QC = []
for i in range(len(P0)):
    divisor = P2[i]-P1[i]
    if divisor != 0:
        QC.append((P1[i]-P0[1])/divisor)
    else:
        QC.append(0)

plt.grid()
#plt.scatter(x, y_euler, s = 5)
plt.plot(x, P0)
plt.plot(x, P1)
plt.plot(x, P2)

print("Euler:")
for i in range(len(x)):
    print("%+.30f\t%+.30f\t%+.30f"%(x[i],y_euler[i],y_euler[i]-solution(x[i])))

plt.show()

plt.ylim([-1000,1000])
plt.grid()
plt.scatter(x[:len(QC)], QC)
plt.show()

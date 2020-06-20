from copy import deepcopy
import numpy as np
def gauss_jacobi(A, b, x):
    x_ = deepcopy(x)
    N = len(x_)
    for i in range(N):
        x_[i,0]=b[i,0]
        for j in range(     i): x_[i,0] -= A[i,j]*x[j,0]
        for j in range(i+1, N): x_[i,0] -= A[i,j]*x[j,0]
        x_[i,0] /= A[i,i]
    return x_
A = np.matrix([[ 4.5, -1.0, -1.0,  1.0],\
               [-1.0,  4.5,  1.0, -1.0],\
               [-1.0,  2.0,  4.5, -1.0],\
               [ 2.0, -1.0, -1.0,  4.5]])
b = np.matrix([[1.0],[-1.0],[-1.0],[0.0]])
x0 = np.matrix([[0.25],[0.25],[0.25],[0.25]])
print("a)")
x1 = gauss_jacobi(A, b, x0)
x2 = gauss_jacobi(A, b, x1)
for i in range(len(x1)):
    print("%.5f  \t%.5f"%(x1[i,0], x2[i,0]))
print("b)")
A_ = np.absolute(A)
s  = [[A_[i,i]] for i in range(len(A_))] - \
     (np.sum(A_, axis=1) - [[A_[i,i]] for i in range(len(A_))])
print(s)
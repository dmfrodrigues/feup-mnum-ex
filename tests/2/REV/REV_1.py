from copy import deepcopy
import numpy as np
def gauss_elimination(A, b):
    A_, b_ = deepcopy(A), deepcopy(b)
    N = len(A_)
    for i in range(N):
        b_[i,0] /= A_[i,i]
        for j  in range(N-1, i-1, -1): A_[i,j] /= A_[i,i]
        for i_ in range(i+1, N      ):
            b_[i_,0] -= b_[i,0]*A_[i_,i]
            for j in range(N-1, i-1, -1): A_[i_,j] -= A_[i,j]*A_[i_,i]
    for i in range(N-1, -1, -1):
        for i_ in range(i):
            b_[i_,0] -= A_[i_,i]*b_[i,0]
            A_[i_,i] -= A_[i_,i]*A_[i,i]
    return b_
A = np.matrix([[ 2, -6, -1],\
               [-3, -1,  7],\
               [-8,  1, -2]], np.double)
b = np.matrix([[-38],[-34],[-20]], np.double)
x = gauss_elimination(A, b)
print("x=\n", x)
print("a)")
dA = np.matrix([[0.3,0.3,0.3],\
                [0.3,0.3,0.3],\
                [0.3,0.3,0.3]], np.double)
db = np.matrix([[0.3],[0.3],[0.3]], np.double)
dx = gauss_elimination(A, db-dA*x)
print("dx=\n", dx)
print("b)")
e0 = b-A*x
d = gauss_elimination(A, e0)
print("e0=\n", e0)
print("d=\n", d)

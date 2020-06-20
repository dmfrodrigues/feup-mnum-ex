import numpy as np
from copy import deepcopy
def gauss(A, b):
    A_, b_ = deepcopy(A), deepcopy(b)
    N = len(A_)
    for i in range(N):
        b_[i,0] /= A_[i,i]
        for j  in range(N-1, i-1, -1): A_[i,j] /= A_[i,i]
        for i_ in range(i+1, N      ):
            b_[i_,0] -= A_[i_,i]*b_[i,0]
            for j in range(N-1, i-1, -1): A_[i_,j] -= A_[i_,i]*A_[i,j]
    for i in range(N-1, -1, -1):
        for i_ in range(i):
            b_[i_,0] -= b_[i,0]*A_[i_,i]
            A_[i_,i] -= A_[i,i]*A_[i_,i]
    return b_
A = np.matrix([[ 0.70,  8.00,  3.00],
               [-6.00,  0.45, -0.25],
               [ 8.00, -3.10,  1.05]])
b = np.matrix([[12.00],[15.00],[23.00]])
print("a)")
x = gauss(A, b)
for l in x: print("%.5f"%l[0])
print("b)")
dA = np.matrix([[0.5,0.5,0.5],\
                [0.5,0.5,0.5],\
                [0.5,0.5,0.5]])
db = np.matrix([[0.5],[0.5],[0.5]])
db_dAx = db-dA*x
dx = gauss(A, db_dAx)
for l in dx: print("%.5f"%l[0])

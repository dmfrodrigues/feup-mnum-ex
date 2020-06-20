import numpy as np
from copy import deepcopy
def triangularize_bot(m_, b_):
    m = deepcopy(m_); b = deepcopy(b_); N = len(m)
    for l in range(N):
        b[l,0] /= m[l,l]
        for c in range(N-1, l-1, -1): m[l,c] /= m[l,l]
        for l_ in range(l+1, N):
            b[l_,0] -= m[l_,l]*b[l,0]
            for c in range(N-1, l-1, -1):
                m[l_,c] -= m[l_,l]*m[l,c]
    return (m, b)
def triangularize_top(m_, b_):
    m = deepcopy(m_); b = deepcopy(b_); N = len(m)
    for c in range(N-1, -1, -1):
        for l in range(c):
            b[l,0] -= m[l,c]*b[c,0]
            m[l,c] -= m[l,c]*m[c,c]
    return (m,b)
A = np.matrix([[1  , 1/2, 1/3],
               [1/2, 1/3, 1/4],
               [1/3, 1/4, 1/5]], dtype=np.float)
def solve(A, b):
    A_, b_ = triangularize_bot(A, b)
    x, I = triangularize_top(A_, b_)
    return x
b = np.matrix([[-1],[1],[1]], dtype=np.float)
print("a)")
A_, b_ = triangularize_bot(A, b)
print(A_); print(b_)
print("b)")
I, x = triangularize_top(A_, b_)
print(x)
print("c)")
dA = np.matrix([[0.05,0.05,0.05],
                [0.05,0.05,0.05],
                [0.05,0.05,0.05]], dtype=np.float)
db = np.matrix([[0.05],[0.05],[0.05]], dtype=np.float)
c = db-dA*x
A_,c_ = triangularize_bot(A, c)
print(A_); print(c_)
I, dx = triangularize_top(A_, c_)
print(dx)

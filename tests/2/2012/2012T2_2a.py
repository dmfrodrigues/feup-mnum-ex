from copy import deepcopy
def gauss_seidel(A, b, x0):
    x = deepcopy(x0)
    N = len(A)
    for i in range(N):
        x[i][0] = b[i][0]
        for j in range(     i): x[i][0] -= A[i][j]*x[j][0]
        for j in range(i+1, N): x[i][0] -= A[i][j]*x[j][0]
        x[i][0] /= A[i][i]
    return x
A = [[ 4.8, -1.0, -1.0,  1.0],
     [-1.0,  4.8,  1.0, -1.0],
     [-1.0,  2.0,  4.8, -1.0],
     [ 2.0, -1.0, -1.0,  4.8]]
b = [[1.0],[-1.0],[-1.0],[0.0]]
x0 = [[0.0],[0.0],[0.0],[0.0]]
print("a)")
x1 = gauss_seidel(A, b, x0)
x2 = gauss_seidel(A, b, x1)
for i in range(len(x1)):
    print("%.5f  \t%.5f"%(x1[i][0], x2[i][0]))

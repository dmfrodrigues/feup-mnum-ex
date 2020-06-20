def cubatura_trapezios(f, h):
    N = len(f); ret = 0
    for i in range(N-1):
        for j in range(N-1):
            ret += f[i][j]+f[i][j+1]+f[i+1][j]+f[i+1][j+1]
    return ret*h*h/4
f = [[1.1, 1.4, 7.7],
     [2.1, 3.1, 2.2],
     [7.3, 1.5, 1.2]]
print("%.6f"%cubatura_trapezios(f, 1.0))
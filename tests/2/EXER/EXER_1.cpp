#include <bits/stdc++.h>
using namespace std;
typedef long double ld;
typedef vector<ld> line;
typedef vector<line> matrix;
pair<matrix,matrix> lower_triang_gauss(matrix A, matrix b){
    const int &N = A.size();
    for(int i = 0; i < N; ++i){
        b[i][0] /= A[i][i];
        for(int j = N-1; j >= i; --j) A[i][j] /= A[i][i];
        for(int i_ = i+1; i_ < N; ++i_){
            b[i_][0] -= b[i][0]*A[i_][i];
            for(int j = N-1; j >= i; --j) A[i_][j] -= A[i][j]*A[i_][i];
        }
    } return pair<matrix,matrix>(A, b);
}
pair<matrix,matrix> upper_triang_gauss(matrix A, matrix b){
    const int &N = A.size();
    for(int i = N-1; i >= 0; --i){
        for(int i_ = 0; i_ < i; ++i_){
            b[i_][0] -= A[i_][i]*b[i][0]; A[i_][i] -= A[i_][i]*A[i][i];
        }
    } return pair<matrix,matrix>(A, b);
}
matrix solve_gauss(const matrix &A, const matrix &b){
    matrix A_ = A, b_ = b;
    auto p = lower_triang_gauss(A_, b_);
    p = upper_triang_gauss(p.first, p.second);
    return p.second;
}
matrix mul(matrix lhs, const matrix &rhs){
    const size_t &A = lhs.size(), &B = lhs[0].size(),
                 &C = rhs.size(), &D = rhs[0].size();
    assert(B == C);
    matrix ret(A, line(D));
    for(size_t i = 0; i < A; ++i) for(size_t j = 0; j < D; ++j){
        ret[i][j] = 0;
        for(size_t k = 0; k < B; ++k) ret[i][j] += lhs[i][k]*rhs[k][j];
    }
    return ret;
}
matrix sub(matrix lhs, const matrix &rhs){
    const size_t &M = lhs.size(), &N = lhs[0].size();
    assert(M == rhs.size()); assert(N == rhs[0].size());
    for(size_t i = 0; i < M; ++i) for(size_t j = 0; j < N; ++j)
        lhs[i][j] -= rhs[i][j];
    return lhs;
}
int main(){
    cout << setprecision(5) << fixed;
    matrix A({line({0.1, 0.5, 3.0, 0.25}),
              line({1.2, 0.2, 0.25, 0.2}),
              line({-1, 0.25, 0.3, 2.0}),
              line({2.0, 0.00001, 1.0, 0.4})});
    matrix b({line({0.0}), line({1.0}),
              line({2.0}), line({3.0})});
    const int &N = A.size();
    cout << "a)" << endl;
    auto p = lower_triang_gauss(A, b);
    for(int i = 0; i < N; ++i){
        for(int j = 0; j < N; ++j) cout << p.first[i][j] << "   \t";
        cout << p.second[i][0] << endl;
    }
    cout << "b)" << endl;
    matrix x = solve_gauss(A, b);
    for(int i = 0; i < N; ++i) cout << x[i][0] << endl;
    cout << "c)" << endl;
    matrix db({line({0.5}),
               line({0.5}),
               line({0.5}),
               line({0.5})});
    matrix dA({line({0.5, 0.5, 0.5, 0.5}),
               line({0.5, 0.5, 0.5, 0.5}),
               line({0.5, 0.5, 0.5, 0.5}),
               line({0.5, 0.5, 0.5, 0.5})});
    matrix db_dAx = sub(db, mul(dA, x));
    matrix dx = solve_gauss(A, db_dAx);
    for(int i = 0; i < N; ++i) cout << dx[i][0] << endl;
    return 0;
}

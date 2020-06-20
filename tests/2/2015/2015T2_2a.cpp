#include <bits/stdc++.h>
using namespace std;
typedef long double ld;
typedef vector<ld> line;
typedef vector<line> matrix;
void gauss_jacobi(const matrix &A, const matrix &b, matrix &x){
    matrix x_ = x;
    const size_t N = A.size();
    for(size_t i = 0; i < N; ++i){
        ld &x__ = x_[i][0]; x__ = b[i][0];
        for(size_t j = 0  ; j < i; ++j) x__ -= A[i][j]*x[j][0];
        for(size_t j = i+1; j < N; ++j) x__ -= A[i][j]*x[j][0];
        x__ /= A[i][i];
    } x = x_;
}
ld dist(const matrix &a, const matrix &b){
    ld ret = 0.0;
    for(size_t i = 0; i < a.size(); ++i) ret += fabs(b[i][0]-a[i][0]);
    return ret;
}
int main(){
    cout << setprecision(5) << fixed;
    matrix A({line({ 4.50000, -1.00000, -1.00000,  1.00000}),
              line({-1.00000,  4.50000,  1.00000, -1.00000}),
              line({-1.00000,  2.00000,  4.50000, -1.00000}),
              line({ 2.00000, -1.00000, -1.00000,  4.50000})});
    matrix b({line({ 1.00000}), line({-1.00000}),
              line({-1.00000}), line({ 0.00000})});
    matrix x({line({ 0.25000}), line({ 0.25000}),
              line({ 0.25000}), line({ 0.25000})});
    matrix x_prev; int n = 0;
    gauss_jacobi(A, b, x); ++n;
    cout << "x" << n << ":\n"; for(const line &l:x) cout << l[0] << endl;
    gauss_jacobi(A, b, x); ++n;
    cout << "x" << n << ":\n"; for(const line &l:x) cout << l[0] << endl;
    do{
        x_prev = x; gauss_jacobi(A, b, x); ++n;
    }while(dist(x, x_prev) > 1e-12);
    cout << "x" << n << ":\n"; for(const line &l:x) cout << l[0] << endl;
    return 0;
}
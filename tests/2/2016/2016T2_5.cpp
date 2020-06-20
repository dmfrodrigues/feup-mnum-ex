#include <bits/stdc++.h>
using namespace std;
typedef long double ld;
typedef vector<ld> line;
typedef vector<line> matrix;
void gauss_seidel(const matrix &A, const matrix &b, matrix &x){
    const size_t N = A.size();
    for(size_t i = 0; i < N; ++i){
        ld &x_ = x[i][0]; x_ = b[i][0];
        for(size_t j = 0  ; j < i; ++j) x_ -= A[i][j]*x[j][0];
        for(size_t j = i+1; j < N; ++j) x_ -= A[i][j]*x[j][0];
        x_ /= A[i][i]; 
    }
}
int main(){
    matrix A({line({ 6.00000, 0.50000, 3.00000, 0.25000}),
              line({ 1.20000, 3.00000, 0.25000, 0.20000}),
              line({-1.00000, 0.25000, 4.00000, 2.00000}),
              line({ 2.00000, 4.00000, 1.00000, 8.00000})});
    matrix b({line({ 2.50000}),
              line({ 3.80000}),
              line({10.00000}),
              line({ 7.00000})});
    matrix x({line({0.00000}),
              line({0.00000}),
              line({0.00000}),
              line({0.00000})});
    gauss_seidel(A, b, x);
    cout << setprecision(5) << fixed;
    for(const line &l:x) cout << l[0] << endl;
    return 0;
}
#include <bits/stdc++.h>
using namespace std;
typedef vector<double> VD;
typedef vector<VD> VVD;

void print_matrix(const VVD &m){
    for(const auto &v:m){
        for(const auto &d:v) cout << d << " ";
        cout << endl;
    }
}

VVD solve_linear(VVD M, VVD Y){
    assert(M.size() == M[0].size());
    assert(M.size() == Y.size());
    const size_t N = M.size();
    for(int diag = 0; diag < N; ++diag){
        Y[diag][0] /= M[diag][diag];
        for(int col = N-1; col >= diag; --col) //(1) <===============
            M[diag][col] /= M[diag][diag];
        for(int lin = diag+1; lin < N; ++lin){
            Y[lin][0] -= Y[diag][0]*M[lin][diag];
            for(int col = N-1; col >= diag; --col)
                M[lin][col] -= M[diag][col]*M[lin][diag]; //(2) <==============
        }
    }
    //print_matrix(M); print_matrix(Y);
    for(int diag = N-1; diag >= 0; --diag){
        for(int lin = 0; lin < diag; ++lin){
            //cout << Y[lin][0] << " " << M[lin][diag] << " " << Y[diag][0] << endl;
            Y[lin][0] -= M[lin][diag]*Y[diag][0];
            M[lin][diag] = 0;
        }
    }
    //print_matrix(M); print_matrix(Y);
    return Y;
}

VVD mult(const VVD &v1, const VVD &v2){
    size_t M = v1.size(),
           N = v1[0].size(),
           P = v2.size(),
           Q = v2[0].size();
    //print_matrix(v1);
    //print_matrix(v2);
    assert(N == P);
    VVD ret(M, VD(Q, 0));
    for(size_t lin = 0; lin < M; ++lin){
        for(size_t col = 0; col < Q; ++col){
            for(size_t i = 0; i < N; ++i){
                ret[lin][col] += v1[lin][i]*v2[i][col];
            }
        }
    }
    return ret;
}

VVD sub(const VVD &v1, const VVD &v2){
    VVD ret = v1;
    for(size_t i = 0; i < v1.size(); ++i)
        for(size_t j = 0; j < v1[0].size(); ++j)
            ret[i][j] -= v2[i][j];
    return ret;
}

VVD add(const VVD &v1, const VVD &v2){
    VVD ret = v1;
    for(size_t i = 0; i < v1.size(); ++i)
        for(size_t j = 0; j < v1[0].size(); ++j)
            ret[i][j] += v2[i][j];
    return ret;
}

int main(){
    cout << setprecision(7) << fixed << showpos;
    VVD M(3);
    M[0] = VD({3,2,3});
    M[1] = VD({2,5,1});
    M[2] = VD({4,2,3});
    VVD Y(3);
    Y[0] = VD({16});
    Y[1] = VD({15});
    Y[2] = VD({17});
    ///

    //VVD X = solve_linear(M, Y);
    VVD X(3);
    X[0] = VD({0.95});
    X[1] = VD({2.25});
    X[2] = VD({2.90});

    VVD Y_ = mult(M, X);
    VVD e0 = sub(Y, Y_);
    VVD d = solve_linear(M, e0);
    print_matrix(d); cout << endl;

    X = add(X,d);
    print_matrix(X);
    return 0;
}

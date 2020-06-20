#include <bits/stdc++.h>
using namespace std;
double g(double x){
    double x_ = x+1.2;
    double c = cos(x_);
    double s = sin(x_);
    double d = c*c;
    double up = -d*(3.0L*x*s+c)+3.6L;
    double dw = 1.0L-3.0L*d*s;
    return up/dw;
}
int main(){
    double x; cin >> x;
    cout << setprecision(10) << fixed << g(x) << endl;
    return 0;
}

#include <bits/stdc++.h>
using namespace std;
const double epsilon = 1e-8;
double fx(double x, double y){
    double up = x*x+0.3L;
    double dw = 2.0L*x+1.0L;
    return up/dw;
}
double fy(double x, double y){
    double up = x*x+1.4L*x+1.0L;
    double dw = 2.0L*x+1.0L;
    return up/dw;
}
int main(){
    double x, y; cin >> x >> y;
    double x_, y_;
    for(int i = 0; i < 1000; ++i){
        x_ = x; y_ = y;
        x = fx(x_, y_); y = fy(x_, y_);
        if(fabs(x-x_) < epsilon && fabs(y-y_) < epsilon) break;
    }
    cout << setprecision(7) << fixed << x << " " << y << endl;
    return 0;
}

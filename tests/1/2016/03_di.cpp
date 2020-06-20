#include <bits/stdc++.h>
using namespace std;
double fx(double x, double y){
    return -sqrt(1.0L-y);
}
double fy(double x, double y){
    return 0.7L+x;
}
int main(){
    double x, y; cin >> x >> y;
    double x_, y_;
    int i;
    for(i=1; i<40; ++i){
        x_ = x; y_ = y;
        x = fx(x_, y_);
        y = fy(x_, y_);
        printf("%+.7f %+.7f "
               "%+.0E %+.0E\n",
               x, y, x-x_, y-y_);
    }
    printf("%d\n%+.32f\n%+.32f\n",
           i, x, y);
    for(; i < 10000000; ++i){
        x_ = x; y_ = y;
        x = fx(x_, y_);
        y = fy(x_, y_);
        if(x == x_ && y == y_)
            break;
    }
    printf("%d\n%+.32f\n%+.32f\n",
           i, x, y);
    return 0;
}

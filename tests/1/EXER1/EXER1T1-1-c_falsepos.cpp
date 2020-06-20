#include <bits/stdc++.h>
using namespace std;
typedef double T;
T f(T x){
    return sin(10.0L*x)+
           cos(3.0L*x);
}
T falsepos(T l, T r, T e){
    T x_prev = l;
    T x = (l*f(r)-r*f(l))
         /(f(r)-f(l));
    cout << l << " " << r << endl;
    while(fabs(x-x_prev) > e){
        if(f(l)*f(x) > 0) l = x;
        else              r = x;
        x_prev = x;
        x = (l*f(r)-r*f(l))
           /(f(r)-f(l));
        cout<<l<<" "<<r<<endl;
    }
    return x;
}
int main(){
    T l, r, epsilon;
    cout<<setprecision(15)<<fixed;
    cin >> l >> r >> epsilon;
    cout << falsepos(l,r,epsilon)
         << endl;
    cin >> l >> r >> epsilon;
    cout << falsepos(l,r,epsilon)
         << endl;
    return 0;
}

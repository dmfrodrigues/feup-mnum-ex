#include <bits/stdc++.h>
using namespace std;
typedef double T;
T f(T x){
    return sin(10.0L*x)+
           cos(3.0L*x);
}
T bisection(T l, T r, T e){

    T m = l+(r-l)/2.0L;

    cout << l << " " << r << endl;
    while((r-l)/m > 2.0L*e){
        if(f(l)*f(m) > 0) l = m;
        else              r = m;

        m = l+(r-l)/2.0L;

        cout<<l<<" "<<r<<endl;
    }
    return m;
}
int main(){
    T l, r, epsilon;
    cout<<setprecision(15)<<fixed;
    cin >> l >> r >> epsilon;
    cout << bisection(l,r,epsilon)
         << endl;
    cin >> l >> r >> epsilon;
    cout << bisection(l,r,epsilon)
         << endl;
    return 0;
}

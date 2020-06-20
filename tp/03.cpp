#include <bits/stdc++.h>
using namespace std;
typedef long double ld;

ld g(ld x){
    //return (ld(2)*x*x+ld(3))/(ld(4)*x-ld(5));
    return ld(0.4)*x*x-ld(0.6);
}

ld solve(ld guess){
    for(int i = 0; i < 20; ++i){
        guess = g(guess);
        cout << fixed << setprecision(100) << guess << endl;
    }
    return guess;
}

int main(){
    ld in; cin >> in;
    cout << fixed << setprecision(100) << solve(in) << endl;
    return 0;
}

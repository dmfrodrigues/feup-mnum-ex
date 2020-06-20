#include <bits/stdc++.h>

typedef long double ld;

ld f(ld x){
    return ld(2.0L)*x*x-ld(5.0L)*x-ld(2.0L);
}

ld bissec(ld a, ld b, ld p){
    while(fabs(b-a) > p){
        ld m = (a+b)/ld(2.0L);
        if(f(a)*f(m)) <= 0){
            b = m;
        }else{
            a = m;
        }
        cout << a << " " << m << " " << b << " " << f(m) << endl;
    }
    return (a+b)/ld(2.0L);
}
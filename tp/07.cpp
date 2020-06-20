#include <bits/stdc++.h>
using namespace std;

#include <ctime>

long double f(long double x){
    return sin(4.0L*x);
    //return x*x;
}

long double int_f(long double a, long double b){
    return -cos(4.0L*b)/4.0L+cos(4.0L*a)/4.0L;
}

long double trapezium(long double a, long double b, long long n){
    long double h = (b-a)/n;
    long double ret = 0.0L;
    for(long long i = 1; i <= n-1; ++i){
        ret += f((b-a)*i/n);
    }
    ret += (f(a)+f(b))/2.0L;
    ret *= h;
    return ret;
}

long double simpson(long double a, long double b, long long n){
    long double h = (b-a)/n;
    long double ret = 0.0L;
    for(long long i = 1; i <= n-1; i += 2){
        ret += 4.0L*f(a+i*h);
    }
    for(long long i = 2; i <= n-2; i += 2){
        ret += 2.0L*f(a+i*h);
    }
    ret += f(a)+f(b);
    ret *= h;
    ret /= 3.0L;
    return ret;
}

int main(){
    cout << setprecision(20) << fixed;
    long double real = int_f(0,1);
    cout << "Trapezium:" << endl;
    for(long long n = 2; n < 1L<<20; n *= 2){
        long double S0 = trapezium(0,1,  n);
        long double S1 = trapezium(0,1,2*n);
        long double S2 = trapezium(0,1,4*n);
        long double QC = (S1-S0)/(S2-S1);
        long double err = S0-real;
        cout << S0 << "\t" << err << "\t" << QC << "\tn=" << n << endl;
    }
    cout << "Simpson:" << endl;
    for(long long n = 2; n < 1L<<20; n *= 2){
        long double S0 = simpson(0,1,  n);
        long double S1 = simpson(0,1,2*n);
        long double S2 = simpson(0,1,4*n);
        long double QC = (S1-S0)/(S2-S1);
        long double err = S0-real;
        cout << S0 << "\t" << err << "\t" << QC << "\tn=" << n << endl;
    }
    return 0;
}

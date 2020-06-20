#include <bits/stdc++.h>

using namespace std;

const double EulerConstant = exp((double)1.0);

int main(){
    double n = EulerConstant - 1.0L;
    for(long long i = 1; i <= 25; ++i){
        n = n*(double)i - (double)1.0L;
    }
    cout << setprecision(20) << scientific << n << endl;
    return 0;
}
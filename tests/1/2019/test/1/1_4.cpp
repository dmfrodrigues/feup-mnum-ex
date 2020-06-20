#include <bits/stdc++.h>
using namespace std;
double g1(double x){
  return (exp(x)*(x-1.0L)+11.0L)/(exp(x)-1.0L);
}
int main(){
  double x = 2.0L, x_;
  cout << setprecision(20) << fixed;
  for(int i = 0; i < 1000; ++i){
    x_ = x;
    x = g1(x);
    cout << x << endl;
    if(x == x_) break;
  }
  return 0;
}

#include <bits/stdc++.h>
using namespace std;
double g3(double x){
  return log(x+11.0L);
}
int main(){
  double x = 2.0L, x_;
  cout << setprecision(20) << fixed;
  for(int i = 0; i < 1000; ++i){
    x_ = x;
    x = g3(x);
    cout << x << endl;
    if(x == x_) break;
  }
  return 0;
}

#include <bits/stdc++.h>
using namespace std;
double g2(double x){
  return exp(x)-11.0L;
}
int main(){
  double guess = -10.0L;
  cout << setprecision(10) << fixed;
  while(guess < 10.0L){
    double x = guess;
    for(int i = 0; i < 1000; ++i) x = g2(x);
    cout << "guess=" << guess << "\t, x=" << x << endl;
    guess += 0.1L;
  }
  return 0;
}

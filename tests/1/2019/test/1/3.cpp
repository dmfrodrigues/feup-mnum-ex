#include <bits/stdc++.h>
using namespace std;
double g3(double x){
  return log(x+11.0L);
}
int main(){
  double guess = -20.0L;
  cout << setprecision(10) << fixed;
  while(guess < 20.0L){
    double x = guess;
    for(int i = 0; i < 1000; ++i) x = g3(x);
    cout << "guess=" << guess << "\t, x=" << x << endl;
    guess += 0.1L;
  }
  return 0;
}

#include <iostream>
#include <cmath>

using namespace std;
double f(double x, double a){
    return pow(x,3)-a;
}
double df(double x){
    return 3*x*x;
}
int main(){
    double indep, x_ant, x, guess;
    int i = 1;
    cout << "a=? " << "x0=? ";
    cin >> indep >> guess;

    x = guess;

    do{
        x_ant = x;
        x = x_ant-(f(x_ant, indep)/df(x_ant));
        cout << "Iteraccao: " << i << " -> " << x << endl;
        i++;
    }while(x-x_ant > 0.001 || x_ant-x > 0.001);

    system("PAUSE");
    return 0;
}
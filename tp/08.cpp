#include <bits/stdc++.h>
using namespace std;

double f(double x, double y){
    return sin(x);
}

double solution(double x){
    return -cos(x)+1;
}

/**
 * Euler
 */
double euler(double Deltax_n, double x_n, double y_n){
    return Deltax_n*f(x_n,y_n);
}

/**
 * Runge-kutta de 4a ordem
 */
double rk4(double Deltax_n, double x_n, double y_n){
    double delta1 = Deltax_n*f(x_n             ,y_n           );
    double delta2 = Deltax_n*f(x_n+Deltax_n/2.0,y_n+delta1/2.0);
    double delta3 = Deltax_n*f(x_n+Deltax_n/2.0,y_n+delta2/2.0);
    double delta4 = Deltax_n*f(x_n+Deltax_n    ,y_n+delta3    );
    return delta1/6.0 + delta2/3.0 + delta3/3.0 + delta4/6.0;
}

int main(){
    cout << setprecision(30) << scientific;
    double xi = 0.0; double xf = 2*3.14159;
    double yi = 0.0;
    double h = 0.1;

    double Deltax_n = h;
    cout << "Euler:" << endl;
    for(double x = xi, y = yi; x < xf;){
        double Deltay_n = euler(Deltax_n, x, y);
        x = x + Deltax_n;
        y = y + Deltay_n;
        double err = y - solution(x);
        cout << x << "\t" << y << "\t" << err << endl;
    }
    return 0;
}

#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

double F(double x)
{
    return x * x + sqrt(x);
}

double research(double C)
{
    double EPS = 1e-7;
    double l = 0;
    double r = C;
    while (r - l > EPS)
    {
        double x = (r + l) / 2;
        if (F(x) < C)
            l = x;
        else
            r = x;
    }
    return (r + l) / 2;
}
int main()
{

    double C;
    cin >> C;
    cout << fixed << setprecision(7) << research(C);

    return 0;
}
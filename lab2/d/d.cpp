#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

double eq(int a, int b, int c, int d, double x)
{
    return a * x * x * x + b * x * x + c * x + d;
}

double research(int a, int b, int c, int d)
{
    double l = -1001;
    double r = 1001;
    double EPS = 1e-7;
    while (r - l > EPS)
    {
        double x = (r + l) / 2;
        if (eq(a, b, c, d, l) * eq(a, b, c, d, x) <= 0)
            r = x;
        else
            l = x;
    }
    return (r + l) / 2;
}
int main()
{
    int a, b, c, d;
    cin >> a >> b >> c >> d;
    cout << fixed << setprecision(7) << research(a, b, c, d);
}
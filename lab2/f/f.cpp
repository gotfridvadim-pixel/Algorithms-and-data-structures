#include <iostream>
#include <vector>
using namespace std;

bool good(int cnt, int q, int s, int t)
{
    return t / q + t / s >= cnt;
}

int bin_r(int n, int quick, int slow)
{
    int l = 0;
    int r = (n - 1) * slow;
    while (r - l > 1)
    {
        int m = (r + l) / 2;
        if (!good(n - 1, quick, slow, m))
            l = m;
        else
            r = m;
    }
    return r + quick;
}

int main()
{
    int n, x, y;
    cin >> n >> x >> y;
    int q = min(x, y);
    int s = max(x, y);
    cout << bin_r(n, q, s);
}
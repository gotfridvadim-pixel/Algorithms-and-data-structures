#include <iostream>
#include <vector>
using namespace std;

bool good(const vector<int> &a, int x, int k)
{
    long long cnt = 0;

    for (auto ln : a)
    {
        cnt += ln / x;

        if (cnt >= k)
            return true;
    }

    return false;
}

void inpute(vector<int> &arr, int size)
{
    int x;

    for (int i = 0; i < size; i++)
    {
        cin >> x;
        arr.push_back(x);
    }
}

int main()
{
    int n, k;
    vector<int> a;

    cin >> n >> k;
    inpute(a, n);

    int l = 0;
    int r = 10000001;

    while (r - l > 1)
    {
        int m = (r + l) / 2;

        if (good(a, m, k))
            l = m;
        else
            r = m;
    }

    cout << l;
}
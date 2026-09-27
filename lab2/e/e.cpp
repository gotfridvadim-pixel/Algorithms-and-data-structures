#include <iostream>
#include <vector>
using namespace std;

void inpute(vector<int> &arr, int size)
{
    int x;

    for (int i = 0; i < size; i++)
    {
        cin >> x;
        arr.push_back(x);
    }
}

bool good(vector<int> &a, int k, int m)
{
    int cows = 1;
    int last = a[0];

    for (int i = 1; i < a.size(); i++)
    {
        if (a[i] - last >= m)
        {
            cows++;
            last = a[i];
        }
    }

    return cows >= k;
}

int muuu(vector<int> &c, int n, int k)
{
    int l = 0;
    int r = c[n - 1] - c[0] + 1;

    while (r - l > 1)
    {
        int m = (r + l) / 2;

        if (good(c, k, m))
            l = m;
        else
            r = m;
    }

    return l;
}

int main()
{
    int n, k;
    cin >> n >> k;

    vector<int> coor;
    inpute(coor, n);

    cout << muuu(coor, n, k);

    return 0;
}
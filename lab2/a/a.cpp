#include <iostream>
#include <vector>

using namespace std;

void binary_research(vector<int> &A, int n, vector<int> &B, int k)
{
    for (int i = 0; i < k; i++)
    {
        int l = -1;
        int r = n;
        while (r - l > 1)
        {
            int m = (l + r) / 2;
            if (A[m] < B[i])
            {
                l = m;
            }
            else
            {
                r = m;
            }
        }
        if (r == n || A[r] != B[i])
        {
            cout << "NO\n";
        }
        else
        {
            cout << "YES\n";
        }
    }
}

int main()
{
    int n, k;
    cin >> n >> k;

    vector<int> arr_1;
    int x;
    for (int i = 0; i < n; i++)
    {
        if (cin >> x)
        {
            arr_1.push_back(x);
        }
    }

    vector<int> arr_2;
    for (int i = 0; i < k; i++)
    {
        if (cin >> x)
        {
            arr_2.push_back(x);
        }
    }
    binary_research(arr_1, n, arr_2, k);
    return 0;
}

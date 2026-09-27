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

void bin_s(vector<int> &A, int n, vector<int> &B, int k)
{
    for (int i = 0; i < k; i++)
    {
        int l = -1;
        int r = n;

        while (r - l > 1)
        {
            int m = (r + l) / 2;

            if (A[m] < B[i])
            {
                l = m;
            }
            else
            {
                r = m;
            }
        }
        if (l == -1)
        {
            cout << A[r] << '\n';
        }
        else if (r == n)
        {
            cout << A[l] << '\n';
        }
        else if (abs(A[l] - B[i]) <= abs(A[r] - B[i]))
        {
            cout << A[l] << '\n';
        }
        else
        {
            cout << A[r] << '\n';
        }
    }
}

int main()
{
    int n, k;
    cin >> n >> k;

    vector<int> arr1, arr2;

    inpute(arr1, n);
    inpute(arr2, k);

    bin_s(arr1, n, arr2, k);

    return 0;
}
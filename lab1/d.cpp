#include <iostream>
#include <vector>

using namespace std;

int BubbleSort(vector<int>& A) {
    int k = 0;
    for (int i = 0; i < A.size() - 1; i++) {
        for (int j = 0; j < A.size() - 1 - i; j++) {
            if (A[j] > A[j + 1]) {
                k += 1;
                swap(A[j], A[j + 1]);
            }
        }
    }
    return k;
}

int main() {
    int n;
    cin >> n;

    vector<int> data(n);

    for (int i = 0; i < n; i++) {
        cin >> data[i];
    }

    int count = BubbleSort(data);

    cout << count << endl;

    return 0;
}

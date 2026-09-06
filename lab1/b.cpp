#include <iostream>
#include <vector>
using namespace std;

void InsertionSort(vector<int>& A) {
    for (int i = 0; i < A.size(); i++) {
        int key = A[i];
        int j = i - 1;
        while (j >= 0 and A[j] > key) {
            A[j + 1] = A[j];
            j--;
        }
        A[j + 1] = key;
    }

}

int main() {
    vector<int> data;
    int x;
    while (cin >> x) {
        data.push_back(x);
    }

    InsertionSort(data);

    for (int i = 0; i < data.size(); i++) {
        cout << data[i] << " ";
    }
    cout << endl;

    return 0;
}

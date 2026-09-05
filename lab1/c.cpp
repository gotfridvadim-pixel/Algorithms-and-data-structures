#include <iostream>
#include <vector>
#include <sstream>
using namespace std;

void BubbleSort(vector<int>& A) {
    for (int i = 0; i < A.size() - 1; i++) {
        for (int j = 0; j < A.size() - 1 - i; j++) {
            if (A[j] < A[j + 1]) {  
                swap(A[j], A[j + 1]);
            }
        }
    }
}

int main() {
    vector<int> data;
    string line;
    getline(cin, line);
    stringstream ss(line);
    int x;
    while (ss >> x) {
        data.push_back(x);
    }

    BubbleSort(data);


    for (int i = 0; i < data.size(); i++) {
        cout << data[i] << " ";
    }
    cout << endl;

    return 0;
}

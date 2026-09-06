#include <iostream>
#include <vector>
#include <algorithm>



using namespace std;

void CountSort(vector<int>& A) {
    if (A.empty()) return;
    
    int k = *max_element(A.begin(), A.end());
    vector<int> count(k + 1, 0);
    
    for (int i = 0; i < A.size(); i++) {
        count[A[i]]++;
    }
    
    A.clear();
    for (int num = 0; num <= k; num++) {
        for (int j = 0; j < count[num]; j++) {
            A.push_back(num);
        }
    }
}

int main() {
    vector<int> arr;
    
    int num;
    
    while (cin >> num) {
        arr.push_back(num);
    }
    
    CountSort(arr);
    
    for (int i = 0; i < arr.size(); i++) {
        cout << arr[i];
        if (i < arr.size() - 1) cout << " ";
    }
    cout << endl;
    
    return 0;
}

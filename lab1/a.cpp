#include <iostream>
#include <vector>
#include <sstream>
using namespace std;

void SelectionSort(vector<int>& A) {
    int n = A.size();
    for (int i = 0; i < n - 1; i++) {
        int max_idx = i;
        for (int j = i + 1; j < n; j++) {
            if (A[j] >= A[max_idx]) {
                max_idx = j;
            }
        }
        swap(A[i], A[max_idx]); // меняем местами
    }
}
//--------
int main() {
    vector<int> data; //создание пустого дин. массива data
    string line; // строка для ввода всех чисел line

    getline(cin, line); // ввод строки строки


    stringstream ss(line); // создание потока для чтения line
    int x;
    while (ss >> x) { // пока ss считается числом, т.к. x является типом int
        data.push_back(x); //добавление x в конец data
    }

    SelectionSort(data);


    for (int i = 0; i < data.size(); i++) {
        cout << data[i] << " ";
    }
    cout << endl;

    return 0;
}

#include <iostream>
#include <queue>
#include <string>
using namespace std;

int main() {
    priority_queue<int> heap;
    string command;
    int x;

    while (cin >> command) {
        if (command == "ADD") {
            cin >> x;
            heap.push(x);
        }
        else if (command == "EXTRACT") {
            if (heap.empty()) {
                cout << "CANNOT" << '\n';
            }
            else {
                cout << heap.top() << '\n';
                heap.pop();
            }
        }
        else if (command == "CLEAR") {
            heap = priority_queue<int>();
        }
    }

    return 0;
}

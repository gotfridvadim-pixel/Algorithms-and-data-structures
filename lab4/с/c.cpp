#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

class MinHeap {
private:
    vector<int> heap = {0};
    int size = 0;

    void shiftup(int i) {
        while (i > 1 && heap[i] < heap[i / 2]){
            swap(heap[i], heap[i / 2]);
            i = i / 2;
        }
    }

    void shiftdown(int i){
        while (i*2 <= size){
            int j = i * 2;

            if (j + 1 <= size && heap[j] > heap[j + 1]) j += 1;
            
            if (heap[i] > heap[j]){
                swap(heap[i], heap[j]);
                i = j;
            }
            else break;
        }
    }

public:
    void add(int x) {
        heap.push_back(x);
        size += 1;
        shiftup(size);
    }

    int extract() {
        int minimum = heap[1];

        swap(heap[1], heap.back());
        heap.pop_back();
        size -= 1;
        shiftdown(1);

        return minimum;
    }

    void clear() {
        heap = {0};
        size = 0;
    }

    bool empty(){
        return size == 0;
    }

};



int main() {
    MinHeap h;
    string command;
    int x;

    while (cin >> command) {
        if (command == "ADD") {
            cin >> x;
            h.add(x);
        }
        else if (command == "EXTRACT") {
            if (h.empty()) {
                cout << "CANNOT\n";
            }
            else {
                cout << h.extract() << '\n';
            }
        }
        else if (command == "CLEAR") {
            h.clear();
        }
    }

    return 0;
}

    
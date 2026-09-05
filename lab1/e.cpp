#include <iostream>
#include <vector>
using namespace std;

void merge(vector<int>& arr, int left, int mid, int right) {
    // Создаём временные массивы для половинок
    int n1 = mid - left + 1;
    int n2 = right - mid;

    vector<int> left_arr(n1);
    vector<int> right_arr(n2);

    // Копируем данные
    for (int i = 0; i < n1; i++) {
        left_arr[i] = arr[left + i];
    }
    for (int i = 0; i < n2; i++) {
        right_arr[i] = arr[mid + 1 + i];
    }

    // Сливаем обратно в исходный массив
    int i = 0, j = 0, k = left;

    while (i < n1 && j < n2) {
        if (left_arr[i] <= right_arr[j]) {
            arr[k] = left_arr[i];
            i++;
        }
        else {
            arr[k] = right_arr[j];
            j++;
        }
        k++;
    }

    // Копируем остатки
    while (i < n1) {
        arr[k] = left_arr[i];
        i++;
        k++;
    }
    while (j < n2) {
        arr[k] = right_arr[j];
        j++;
        k++;
    }
}

void merge_sort(vector<int>& arr, int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;

        // Сортируем половинки
        merge_sort(arr, left, mid);
        merge_sort(arr, mid + 1, right);

        // Сливаем
        merge(arr, left, mid, right);
    }
}

int main() {
    int n;
    cin >> n;

    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    merge_sort(arr, 0, n - 1);

    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    return 0;
}
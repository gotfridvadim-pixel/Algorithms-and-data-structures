from random import *


def fast_sort(arr):
    if len(arr) <= 1:
        return arr
    val = arr[randint(0, len(arr) - 1)]
    left = [i for i in arr if i < val]
    midle = [i for i in arr if i == val]
    right = [i for i in arr if i > val]
    return fast_sort(left) + midle + fast_sort(right)


n = int(input())
arr = input().split()
for i in range(n):
    arr[i] = int(arr[i])

arr = fast_sort(arr)
print(*arr)

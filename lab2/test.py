def binary_search(arr, key):
    l = -1
    r = len(arr)
    while r -l > 1:
        m = (r + l) // 2
        if arr[m] <= key:
            r = m
        else:
            l = m
    if r == len(arr):
        return -1
    return r

data = [9, 8, 8, 6, 6,6, 4, 3, 3, 2, 0]

print(binary_search(data, 6))
print(binary_search(data, 11))
print(binary_search(data, 2))
print(binary_search(data, 5))
print(binary_search(data, -3))
print(binary_search(data, 0))


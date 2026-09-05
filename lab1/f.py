def CountSort(A):
    if len(A) <= 1:
        return A
    min_val = min(A)
    max_val = max(A)
    range_size = max_val - min_val + 1
    count = [0] * range_size

    for i in A:
        count[i - min_val] += 1

    A[:] = []
    for num in range(range_size):
        A.extend([num + min_val] * count[num])


arr = input().split()
for i in range(len(arr)):
    arr[i] = int(arr[i])

CountSort(arr)
print(*arr)

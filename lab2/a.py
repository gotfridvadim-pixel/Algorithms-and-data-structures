
def binary_research(arr1, arr2):
    for key in arr2:
        l = -1
        r = len(arr1)
        while r - l > 1:
            m = (l+r) // 2
            if arr1[m] < key:
                l = m
            else:
                r = m
        if r == len(arr1) or arr1[r] != key:
            print('NO')
        else:
            print('YES')


n, k = list(map(int, input().split()))
arr_1 = list(map(int, input().split()))
arr_2 = list(map(int, input().split()))

binary_research(arr_1, arr_2)

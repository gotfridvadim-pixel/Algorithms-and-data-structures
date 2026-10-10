def funct(n, a, m, b):
    a.sort()
    res = [0] * m

    for i in range(m):
        l = -1
        r = n
        while r - l > 1:
            x = (l + r) // 2

            if a[x] < b[i]:
                l = x
            else:
                r = x
        left = r

        l = -1
        r = n
        while r - l > 1:
            x = (l + r) // 2

            if a[x] <= b[i]:
                l = x
            else:
                r = x
        right = r

        res[i] = right - left

    return res


n = int(input())
a_1 = list(map(int, input().split()))

m = int(input())
a_2 = list(map(int, input().split()))

print(*funct(n, a_1, m, a_2))
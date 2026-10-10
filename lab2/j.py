def good(d, a, b, w, h, n):
    x = a + 2 * d
    y = b + 2 * d

    count1 = (w // x) * (h // y)

    count2 = (w // y) * (h // x)

    return max(count1, count2) >= n


def bin_search(n, a, b, w, h):

    l = 0
    r = 10**18 + 1

    while r - l > 1:
        m = (l + r) // 2

        if good(m, a, b, w, h, n):
            l = m
        else:
            r = m

    return l


n, a, b, w, h = map(int, input().split())

print(bin_search(n, a, b, w, h))
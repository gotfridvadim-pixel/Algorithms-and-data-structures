from collections import deque

n, k = map(int, input().split())
a = list(map(int, input().split()))

deq = deque()

for i in range(n):
    if deq and deq[0] <= i - k:
        deq.popleft()

    while deq and a[deq[-1]]>= a[i]:
        deq.pop()
    deq.append(i)

    if i >= k - 1:
        print(a[deq[0]])



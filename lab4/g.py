import heapq

n = int(input())
a = [int(input()) for _ in range(n)]

heap = []

for i in range(n):
    t = max(1000 - a[i], 1)
    heapq.heappush(heap, (t, i, a[i] + 1))

current_time = 0
pos = 0

while True:
    t, i, count = heapq.heappop(heap)

    if abs(i - pos) > t - current_time:
        print(t)
        break

    current_time = t
    pos = i

    next_time = t + max(1000 - count, 1)

    heapq.heappush(heap, (next_time, i, count + 1))

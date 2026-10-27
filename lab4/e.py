
import heapq

n = int(input())
heap = list(map(int, input().split()))

heapq.heapify(heap)

res = 0

while len(heap) > 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)

    s = a + b
    res += s

    heapq.heappush(heap, s)

print(f"{res * 0.05:.2f}")

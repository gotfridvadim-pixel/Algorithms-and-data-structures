import heapq

n = int(input())

fish = []
heap = []

for i in range(n):
    f = int(input())
    fish.append(f)
    dt = max(1000-f, 1)
    heapq.heappush(heap, (dt, i))

pos = 0
current_time = 0

while heap:
    time, ind = heapq.heappop(heap)

    if current_time + abs(pos-ind) > time:
        print(time)
        break

    pos = ind
    current_time = time
    fish[ind] += 1
    dt = max(1000-fish[ind], 1)
    heapq.heappush(heap, (time+dt, ind))


class MinHeap():
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def shiftup(self, i):
        while i > 1 and self.heap[i] < self.heap[i // 2]:
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i //= 2

    def shiftdown(self, i):
        while i*2 <= self.size:
            j = i * 2

            if j + 1 <= self.size and self.heap[j] > self.heap[j + 1]:
                j += 1

            if self.heap[i] > self.heap[j]:
                self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
                i = j
            else:
                break
    def insert(self, x):
        self.heap.append(x)
        self.size += 1
        self.shiftup(self.size)

    def extract(self):
        minimum = self.heap[1]
        self.heap[1] = self.heap[-1]
        self.heap.pop()
        self.size -= 1
        self.shiftdown(1)
        return minimum

n = int(input())
s = list(map(int, input().split()))


h = MinHeap()

for el in s:
    h.insert(el)

res = []

while h.size > 0:
    res.append(h.extract())

print(*res)





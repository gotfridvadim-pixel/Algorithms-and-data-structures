
class MaxHeap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def insert(self, x):
        self.heap.append(x)
        self.size += 1

        i = self.size

        while i > 1 and self.heap[i] > self.heap[i // 2]:
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i //= 2

    def extract(self):


        maximum = self.heap[1]

        self.heap[1] = self.heap[-1]
        self.heap.pop()
        self.size -= 1

        i = 1

        while i * 2 <= self.size:
            j = i * 2

            if j + 1 <= self.size and self.heap[j + 1] > self.heap[j]:
                j += 1

            if self.heap[i] < self.heap[j]:
                self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
                i = j
            else:
                break

        return maximum


h = MaxHeap()

for _ in range(int(input())):
    s = list(map(int, input().split()))

    if s[0] == 0:
        h.insert(s[1])
    else:
        print(h.extract())

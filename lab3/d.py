from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def push(self, n):
        self.queue.append(n)
        print('ok')

    def pop(self):
        if not self.queue:
            print('error')
            return
        print(self.queue.popleft())

    def front(self):
        if not self.queue:
            print('error')
            return
        print(self.queue[0])

    def size(self):
        print(len(self.queue))

    def clear(self):
        self.queue.clear()
        print('ok')


queue = Queue()

while True:
    c = input()

    if c.startswith('push'):
        queue.push(int(c.split()[1]))
    elif c == 'pop':
        queue.pop()
    elif c == 'front':
        queue.front()
    elif c == 'size':
        queue.size()
    elif c == 'clear':
        queue.clear()
    elif c == 'exit':
        print('bye')
        break
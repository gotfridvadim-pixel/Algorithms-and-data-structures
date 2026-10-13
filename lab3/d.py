from collections import deque

class Queue:
    def __init__(self):
        self.init = []

    def push(self, n):
        self.init.append(n)
        print('ok')

    def pop(self):
        if not self.init:
            print('error')
            return
        print(self.init.pop(0))

    def front(self):
        if not self.init:
            print('error')
            return
        print(self.init[0])

    def size(self):
        print(len(self.init))

    def clear(self):
        self.init.clear()
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
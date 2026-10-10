class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, n):
        self.stack.append(n)
        print('ok')

    def pop(self):
        if self.is_empty():
            print('error')
            return
        print(self.stack.pop())

    def back(self):
        if self.is_empty():
            print('error')
            return
        print(self.stack[-1])

    def size(self):
        print(len(self.stack))

    def clear(self):
        self.stack.clear()
        print('ok')


commands = []
st = Stack()
flag = True
while flag:
    x = input()
    commands.append(x)
    if x == 'exit':
        flag = False

for command in commands:
    if command.startswith('push'):
        st.push(command.split()[1])
    elif command == 'pop':
        st.pop()
    elif command == 'back':
        st.back()
    elif command == 'size':
        st.size()
    elif command == 'clear':
        st.clear()
    else:
        print('bye')










s = input().split()
stack = []
for i in range(len(s)):
    if s[i] not in '+-*/':
        stack.append(s[i])
    else:
        if s[i] == '+':
            a = int(stack.pop(-2))
            b = int(stack.pop())
            stack.append(a + b)
        if s[i] == '-':
                    a = int(stack.pop(-2))
                    b = int(stack.pop())
                    stack.append(a - b)
        if s[i] == '*':
                    a = int(stack.pop(-2))
                    b = int(stack.pop())
                    stack.append(a * b)
        if s[i] == '/':
                    a = int(stack.pop(-2))
                    b = int(stack.pop())
                    stack.append(a / b)
print(*stack)
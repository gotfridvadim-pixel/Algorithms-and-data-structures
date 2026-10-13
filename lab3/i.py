
balls = list(map(int, input().split()))

stack = []
result = 0

for ball in balls[1:]:
    if stack and stack[-1][0] != ball:
        if stack[-1][1] >= 3:
            result += stack[-1][1]
            stack.pop()

    if stack and stack[-1][0] == ball:
        stack[-1][1] += 1
    else:
        stack.append([ball, 1])

if stack and stack[-1][1] >= 3:
    result += stack[-1][1]
    stack.pop()

print(result)

    
        





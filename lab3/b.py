

flag = True
s = input()
stack = []
for el in s:
    if el in '([{':
        stack.append(el)
    elif el in ')]}':
        if len(stack) == 0:
            flag = False
            break
        elif el == ')' and stack[-1] == '(':
                stack.pop()
        elif el == ']' and stack[-1] == '[':
                stack.pop()
        elif el == '}' and stack[-1] == '{':
                stack.pop()
        else:
            flag = False
            break
if flag and len(stack) == 0:
    print('yes')
else:
    print('no')
from collections import deque

first = deque(map(int, input().split()))
second = deque(map(int, input().split()))

c = 0

while first and second and c < 10**6:
    a = first.popleft()
    b = second.popleft()
    if a == 0 and b == 9:
        first.append(a)
        first.append(b)
    elif a==9 and b == 0:
        second.append(a)
        second.append(b)
    elif a > b:
        first.append(a)
        first.append(b)
    else:
        second.append(a)
        second.append(b)
    c += 1

if not first:
    print('second', c)
elif not second:
    print('first', c)
else:
    print('botva')
from collections import deque
commands = []
deq = []
flag = True

while flag:
    x = input()
    commands.append(x)

    if x == 'exit':
        flag = False


for c in commands:
    if 'front' in c:

        if 'push' in c:
            deq.insert(0, c.split()[1])
            print('ok')

        elif deq == []:
            print('error')

        else:
            if 'pop' in c:
                print(deq.pop(0))
            else:
                print(deq[0])

    elif 'back' in c:

        if 'push' in c:
            deq.append(c.split()[1])
            print('ok')

        elif deq == []:
            print('error')

        else:
            if 'pop' in c:
                print(deq.pop())
            else:
                print(deq[-1])

    elif 'size' in c:
        print(len(deq))

    elif 'clear' in c:
        deq = []
        print('ok')

    else:
        print('bye')
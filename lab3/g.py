
n = int(input())
wagon = list(map(int, input().split()))
stack = []
need = 1
for i in range(n):
    stack.append(wagon[i])
    while stack and stack[-1] == need:
        stack.pop()
        need += 1
if not stack:
    print("YES")
else:
    print("NO")
    
    

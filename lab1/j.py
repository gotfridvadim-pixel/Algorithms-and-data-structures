import sys

a = sys.stdin.read().split()

for i in range(len(a)):
    for j in range(len(a) - 1 - i):
        if a[j] + a[j + 1] < a[j + 1] + a[j]:
            a[j], a[j + 1] = a[j + 1], a[j]

result = "".join(a)

if result[0] == "0":
    print(0)
else:
    print(result)

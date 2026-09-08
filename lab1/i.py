from collections import Counter

w1 = input()
w2 = input()


if len(w1) != len(w2):
    print("NO")
else:

    if Counter(w1) == Counter(w2):
        print("YES")
    else:
        print("NO")

from collections import Counter

w1 = input()
w2 = input()

# Если длины разные, они точно не анаграммы
if len(w1) != len(w2):
    print("NO")
else:
    # Сравниваем частотные словари букв
    if Counter(w1) == Counter(w2):
        print("YES")
    else:
        print("NO")

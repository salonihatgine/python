#Lower Triangular Matrix (including diagonal)
import sys

L = [10, 20, 30, 40, 50]

print("while version")

i = 0
while i < len(L):
    j = 0
    while j <= i:
        print("Index Pair:(%d,%d)" % (i, j))
        print("Element Pair:(%d, %d)" % (L[i], L[j]))
        print("*" * 30)
        j = j + 1
    print("-" * 60)
    i = i + 1

print("For version")
for i in range(len(L)):
    for j in range(0, i + 1):
        print("Index Pair:(%d,%d)" % (i, j))
        print("Element Pair:(%d,%d)" % (L[i], L[j]))
        print("*" * 30)
    print("-" * 60)

    
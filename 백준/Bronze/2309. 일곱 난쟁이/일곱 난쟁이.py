lst = []
a, b = 0, 0
for i in range(9):
    n = int(input())
    lst.append(n)

total = sum(lst)

for j in lst:
    for k in lst:
        if j != k and total - j - k == 100:
            a, b = j, k
lst.remove(a)
lst.remove(b)
lst.sort()
for l in lst:
    print(l)
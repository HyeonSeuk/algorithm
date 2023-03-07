n = int(input())
lst = []
for i in range(n):
    a, b = input().split()
    lst.append([int(a), i, b])
lst.sort()
for j in lst:
    print(f'{j[0]} {j[2]}')
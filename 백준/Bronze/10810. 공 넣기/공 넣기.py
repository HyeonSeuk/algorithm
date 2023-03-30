n, m = map(int, input().split())
lst = []
for _ in range(1, n+1):
    lst.append(0)

for _ in range(1, m+1):
    a, b, c = map(int, input().split())
    for j in range(a, b+1):
        lst[j-1] = c
print(*lst)
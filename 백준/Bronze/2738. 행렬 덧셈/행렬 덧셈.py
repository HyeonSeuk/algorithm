n, m = map(int, input().split())
a, b = [], []
for _ in range(n):
    line = list(map(int, input().split()))
    a.append(line)

for _ in range(n):
    line_1 = list(map(int, input().split()))
    b.append(line_1)

for i in range(n):
    for j in range(m):
        print(a[i][j] + b[i][j], end = ' ')
    print()
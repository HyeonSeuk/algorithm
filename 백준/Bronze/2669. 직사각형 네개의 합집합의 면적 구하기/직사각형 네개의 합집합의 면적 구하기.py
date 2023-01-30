matrix = [[0] * 100 for _ in range(100 + 1)]
cnt = 0
for i in range(4):
    x, y, x1, y1 = map(int, input().split())
    for i in range(x, x1):
        for j in range(y, y1):
            if matrix[i][j] == 0:
                matrix[i][j] += 1
                cnt += 1
print(cnt)
from itertools import combinations

n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

for a,b,c in combinations(range(m), 3):
    sum = 0
    for i in range(n):
        sum += max(lst[i][a], lst[i][b], lst[i][c])
    cnt = max(cnt, sum)
print(cnt)
n, m = map(int, input().split())

arr = [[0]*(m+1)] + [[0] + list(map(int,input().split())) for _ in range(n)]

for i in range(1, n+1):
    for j in range(1, m+1):
        arr[i][j] += arr[i][j-1] + arr[i-1][j] - arr[i-1][j-1]

k = int(input())
for w in range(k):
    i, j , a, b = map(int, input().split())
    print(arr[a][b] - arr[a][j-1]-arr[i-1][b] + arr[i-1][j-1])
T = int(input())

for t in range(1, T+1):
    cnt = 0
    a, b, c = map(int, input().split())
    d = min(a, b)
    while c >= d:
        cnt += 1
        c -= d
    print(f'#{t} {cnt}')
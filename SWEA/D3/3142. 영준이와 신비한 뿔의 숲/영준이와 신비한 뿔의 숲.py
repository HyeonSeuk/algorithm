N = int(input())
for t in range(1, N+1):
    n, m = map(int, input().split())
    tw = 0
    u = 0
    for i in range(m, 0, -1):
        if n > i:
            n -= 2
            tw += 1
        elif n <= i:
            n -= 1
            u += 1
    print(f'#{t} {u} {tw}')
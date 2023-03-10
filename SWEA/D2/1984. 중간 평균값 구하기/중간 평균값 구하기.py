T = int(input())
for t in range(1, T+1):
    n = list(map(int, input().split()))
    n.sort()
    a = n[0]
    b = n[-1]
    c = sum(n)
    print(f'#{t} {round((c-a-b)/8)}')
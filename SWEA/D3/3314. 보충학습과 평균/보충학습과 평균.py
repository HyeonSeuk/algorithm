T = int(input())
for t in range(1, T+1):
    cnt = 0
    a = list(map(int, input().split()))
    for i in a:
        if i <= 39:
            cnt += 40
        else:
            cnt += i
    print(f'#{t} {cnt//len(a)}')
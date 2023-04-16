N = int(input())
for t in range(1, N+1):
    cnt = 0
    a, b = map(int, input().split())
    for i in range(a, b+1):
        c = i**(1/2)
        if c == int(c):
            i = str(i)
            c = str(int(c))
            if i == i[::-1] and c == c[::-1]:
                cnt += 1

    print(f'#{t} {cnt}')
T = int(input())
for t in range(1, T+1):
    a = input()
    for i in range(1, len(a)):
        if a[:i] == a[i:2*i]:
            break
    print(f'#{t} {len(a[:i])}')
T = int(input())
for t in range(1, T+1):
    a, b = map(int, input().split())
    lst = sorted(list(map(int, input().split())), reverse=True)
    cnt = sum(lst[:b])
    print(f'#{t} {cnt}')
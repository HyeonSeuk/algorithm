for t in range(1, int(input())+1):
    n = int(input())
    lst = []
    for i in range(n):
        a, b = map(int, input().split())
        for j in range(a, b+1):
            lst.append(j)

    print(f'#{t} {len(lst)}')
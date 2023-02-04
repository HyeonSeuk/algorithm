for t in range(1, int(input())+1):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(f'#{t}', *a)
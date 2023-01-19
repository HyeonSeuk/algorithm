for t in range(1,int(input())+1):
    n = int(input())
    a = list(map(int, input().split()))
    profit = 0
    max = a[-1]
    for i in range(n-1, -1, -1):
        if a[i] >= max:
            max = a[i]
        else:
           profit += max - a[i]
    print(f'#{t} {profit}')
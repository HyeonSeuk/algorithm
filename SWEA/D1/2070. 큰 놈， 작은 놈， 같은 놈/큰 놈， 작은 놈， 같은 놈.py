T = int(input())

for t in range(1, T+1):
    a, b = list(map(int, input().split()))
    print(f'#{t} ', end='')
    if b > a:
        print('<')
    elif b == a:
        print('=')
    else:
        print('>')
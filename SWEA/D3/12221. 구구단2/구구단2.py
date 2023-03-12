T = int(input())
for t in range(1, T+1):
    a, b = map(int, input().split())
    if a <= 9 and b <= 9:
        print(f'#{t} {a*b}')
    else:
        print(f'#{t} {-1}')
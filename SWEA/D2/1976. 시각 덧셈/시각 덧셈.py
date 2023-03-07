n = int(input())
for t in range(1, n+1):
    a, b, c, d = map(int, input().split())
    x = a+c
    y = b+d
    if x > 12:
        x-=12
    if y >= 60:
        x+=1
        y-=60
    print(f'#{t} {x} {y}')
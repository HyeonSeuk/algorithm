T = int(input())
for t in range(1, T+1):
    n = int(input())
    if n % 2 == 1:
        print(f'#{t} Odd')
    else:
        print(f'#{t} Even')
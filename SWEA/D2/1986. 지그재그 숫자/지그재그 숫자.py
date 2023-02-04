for t in range(1, int(input())+1):
    n = int(input())
    odd = 0
    for i in range(1, n+1):
        if i%2 != 0:
            odd += i
        else:
            odd -= i
    print(f'#{t} {odd}')
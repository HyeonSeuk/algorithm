T = int(input())
for t in range(1, T+1):
    n = input()
    win = n.count('o') 
    cnt = 15 - len(n)   

    if win + cnt >= 8:
        print(f'#{t} YES')
    else:
        print(f'#{t} NO')
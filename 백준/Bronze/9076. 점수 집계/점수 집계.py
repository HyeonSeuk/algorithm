for _ in range(int(input())):
    N = list(map(int,input().split()))
    N.sort()
    N.pop(0)
    N.pop()
    if N[2] - N [0] >= 4:
        print('KIN')
    else:
        print(N[0]+N[1]+N[2])
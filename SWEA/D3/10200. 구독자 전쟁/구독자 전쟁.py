T = int(input())
for t in range(1, T+1):
    N, P, T = map(int, input().split())
    if P + T > N:
        print(f'#{t} {min(P, T)} {P+T-N}')
    elif N == P == T:
        print(f'#{t} {P} {T}')
    else:
        print(f'#{t} {min(P, T)} {0}')
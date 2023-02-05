for t in range(1, int(input())+1):
    P, Q, R, S, W = map(int, input().split())
    A = P * W
    B = 0
    if R > W:
        B += Q
    else:
        B += Q + (W-R)*S

    print(f'#{t}', min(A, B))  
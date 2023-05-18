T = int(input())
for t in range(1, T+1):
    n = input()
    a = '0'
    cnt = 0
	
    for i in range(len(n)):
        if n[i] != a:
            a = n[i]
            cnt += 1
    print(f'#{t} {cnt}')
T = int(input())
for t in range(1, T+1):
    n = int(input())
    m = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    lst = []
    for i in m:
        lst.append(n // i)
        n = n % i
    print(f'#{t}')
    print(*lst)
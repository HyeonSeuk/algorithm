while True:
    n = int(input())
    if n == 0:
        break
    lst = []
    cnt = 0
    for _ in range(n):
        a, b = input().split()
        b = float(b)
        if b > cnt:
            lst = [a]
            cnt = b
        elif b == cnt:
            lst.append(a)
    print(*lst)
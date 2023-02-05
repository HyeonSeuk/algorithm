for _ in range(int(input())):
    n = input()
    m = str(int(n) + int(n[::-1]))
    if m == m[::-1]:
        print('YES')
    else:
        print('NO')
for t in range(1, 11):
    a, b = input().split()
    lst = []
    for i in b:
        if lst and i == lst[-1]:
            lst.pop()
        else:
            lst.append(i)
    password = ''.join(lst)
    print(f'#{t} {password}')
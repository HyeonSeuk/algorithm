for t in range(int(input())):
    a = input()
    s = 0
    cnt = 0
    for j in a:
        if j == 'O':
            cnt += 1
            s += cnt
        else:
            cnt = 0
    print(s)
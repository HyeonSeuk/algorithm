while True:
    a = input()
    n = 0
    if a == '#':
        break
    for i in a:
        if i in 'aeiouAEIOU':
            n += 1
    print(n)
for t in range(int(input())):
    a =input()
    while '()' in a:
        a = a.replace('()','')
    print('NO' if a else 'YES')
for i in range(int(input())):
    lst = []
    a = map(int,input().split())
    for i in a:
        lst.append(i)
        lst.sort()
    
    x = lst[3] - lst[1]

    if x < 4:
        print(sum(lst[1:4]))
    else:
        print('KIN')
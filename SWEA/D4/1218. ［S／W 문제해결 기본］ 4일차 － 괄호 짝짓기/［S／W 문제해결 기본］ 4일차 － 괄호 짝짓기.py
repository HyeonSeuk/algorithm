for t in range(1, 11):
    n = int(input())
    lst = list(map(str,input()))
    
    a1 = lst.count('(')
    a2 = lst.count(')')
    b1 = lst.count('[')
    b2 = lst.count(']')
    c1 = lst.count('{')
    c2 = lst.count('}')
    d1 = lst.count('<')
    d2 = lst.count('>')
    if a1 == a2 and b1 == b2 and c1 == c2 and d1 == d2:
        result = 1
    else:
        result = 0
    print(f'#{t} {result}')
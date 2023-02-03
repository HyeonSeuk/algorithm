T = int(input())
for t in range(1, T+1):
    N, K =  map(int, input().split())
    number = map(int, input().split())
    lst = []
    lit = []
    for i in range(1, N+1):
        lst.append(i)

    for j in number:
        lit.append(j)

    set1 = set(lst)
    set2 = set(lit)
    set3 = (set1 - set2)
    
    print(f'#{t}', *set3)
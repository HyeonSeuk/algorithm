T = int(input())
for t in range(1, T+1):
    n = list(input())
    n.sort()
    lst = []
    for i in n:
        if lst and lst[-1] == i:
            lst.pop()
        else:
            lst.append(i)
    m = ''.join(lst)
    if not lst:
        print(f'#{t} Good')
    else:
        print(f'#{t} {m}')
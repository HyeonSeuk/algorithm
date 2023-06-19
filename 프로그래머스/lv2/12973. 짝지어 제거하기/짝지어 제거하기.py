def solution(s):
    lst = []
    for i in s:
        if len(lst) == 0:
            lst.append(i)
        elif lst[-1] == i:
            lst.pop()
        else:
            lst.append(i)
    if len(lst) == 0:
        return 1
    else:
        return 0

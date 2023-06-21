def solution(n):
    lst = []
    for i in range(1, n+1):
        if i % 2 == 1:
            lst.append('수')
        else:
            lst.append('박')
    return ''.join(lst)
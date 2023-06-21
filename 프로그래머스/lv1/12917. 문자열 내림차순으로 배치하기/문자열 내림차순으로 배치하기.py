def solution(s):
    lst = []
    lit = []
    for i in s:
        lst.append(ord(i))
    lst.sort()
    lst.reverse()
    for j in lst:
        lit.append(chr(j))
    return ''.join(lit)
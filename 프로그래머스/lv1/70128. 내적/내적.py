def solution(a, b):
    lst = []
    for i in range(len(a)):
        c = a[i] * b[i]
        lst.append(c)
    answer = sum(lst)
    return answer
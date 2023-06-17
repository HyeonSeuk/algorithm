def solution(left, right):
    a = []
    b = []
    for i in range(left, right+1):
        lst = []
        for j in range(1, i+1):
            if i % j == 0:
                lst.append(j)
        if len(lst) % 2 == 0:
            a.append(lst[-1])
        else:
            b.append(lst[-1])
    answer = sum(a) - sum(b)
    return answer
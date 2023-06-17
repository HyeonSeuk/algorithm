def solution(arr, divisor):
    lst = []
    for i in arr:
        if i % divisor == 0:
            lst.append(i)
    if len(lst) == 0:
        return [-1]
    else:
        lst.sort()
        return lst

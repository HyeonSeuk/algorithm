def solution(n):
    lst = []
    for i in range(1, n+1):
        if n % i == 1:
            lst.append(i)
    answer = min(lst)
    return answer
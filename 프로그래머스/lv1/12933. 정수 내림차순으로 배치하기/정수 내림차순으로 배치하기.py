def solution(n):
    lst = list(map(int, str(n)))
    lst.sort(reverse=True)
    answer = int(''.join(map(str, lst)))
    return answer
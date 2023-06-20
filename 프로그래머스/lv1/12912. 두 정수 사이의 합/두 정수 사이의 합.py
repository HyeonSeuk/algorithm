def solution(a, b):
    cnt = 0
    if a < b:
        for i in range(a, b+1):
            cnt += i
        return cnt
    elif a == b:
        for i in range(a, b+1):
            cnt += i
        return cnt
    else:
        for i in range(a, b-1, -1):
            cnt += i
        return cnt
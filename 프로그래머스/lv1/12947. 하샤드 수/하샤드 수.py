def solution(x):
    y = list(map(int, str(x)))
    z = sum(y)
    if x % z == 0:
        return True
    else:
        return False
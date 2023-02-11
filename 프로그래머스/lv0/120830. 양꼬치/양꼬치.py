def solution(n, k):
    a = 12000 * n
    if n >= 10:
        b = (k *2000) - ((n//10)*2000)
    else:
        b = k*2000
    answer = a + b
    return answer
def solution(price, money, count):
    lst = []
    cnt = 0
    for i in range(1, count+1):
        lst.append(price*i)
    if sum(lst) > money:
        answer = sum(lst) - money
    elif sum(lst) <= money:
        answer = 0

    return answer